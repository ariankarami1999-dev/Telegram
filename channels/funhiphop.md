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
<img src="https://cdn4.telesco.pe/file/H2FM_5IEDeMOrF-i7-wkP1WoMNr2CYbgUL4y9ZaeLgUOX2w__m5MybFM3HUUhqj3sHymSQWR05cpPZO3YefN_oxAsUw3yFbAQbxhS3wgUvNh0HPYeGMwlsryaCllKcDXhNPjcm7_dVWR5WfMPIUX4Ybpdz7-OvseLBcRfnKveN5KqKh6UT6hLR06smeBg0HqKjY56Ph2yaeZOp47LYmxZUSgDZv_6uniwl1cSrLx16Aiw7hyW2mPiL1M060DBbUJabHNrGavlpb8n8SAhiENd9jv8ccsgubHPyNT9XtG5uUHdiMHs-Iwm4eCMimBER8JudlAo5RakL83bBZtg2vOvQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 183K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡صاحب سبک🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-05 18:41:18</div>
<hr>

<div class="tg-post" id="msg-78781">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">کاش این قضیه حمایت از همجنس گرایی رو زمانی که شیث رضایی و فرهاد مجیدی تو تیم ملی بودن گسترش میدادن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 1.88K · <a href="https://t.me/funhiphop/78781" target="_blank">📅 18:30 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78780">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lYaDawQsbnx4vzTotWN34-y7ie4_Q5Y_gUn65sD1igFoD0aB2BfcfmHk70GGCaavO-23YIf0z_ECjN6PyAjyxsYSeKrEUg_34cCuqySkUO44xUp59VAisajMkbTszCbjpDdnXgEC-SwzMGkkc1p3qfV5z8zjcP7R01ulsvDEvf8UCd8QbdH9LM5CisTLSCnony9noFM5xTF6u2X7mMFMfPKyIgIDOP3tXVPRz3v_PLKyxLRSh06cRMAdfQaRAMX3izioO3YrdlSuNF2uruYJY7eKERaQd4a_72rEb5P2-E-zeiuWwg8Sk78Qy8q1zDcDObmHVL_2HBVZAa3mrIBy3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آقا دسخوش
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 2.31K · <a href="https://t.me/funhiphop/78780" target="_blank">📅 18:27 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78779">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kyIUXq_rdrP8hBmMg0mOrq-acEICn4DOGOm9cDwEksINQ0J_TmIDHePnI8NPt0UWKv4byFepxwFDTOMXTqCTo8ObVDmCvhUTxGyfEsOJbJGdPOOWg8mhPUkMqxO4qRQF6IGVuo_ve9nzzsRXYvY8MRp_BXEFrfaAJR3TDVPFStSEgGWvSm581ZQTIBTLAXM6XgIDKp1ZN2a9kHXi434a7hvG0Ks65VMUiP0VBcG_cwtK-ND4tSjOEIP3O6CqER0UfgdPDfZQmoilDquLA-PwWox-H6x3HrCxA7ExIOV4tLWrI2b2vw5uZwdWove1pFiFWpv2hcsG9yu-jT0ek4UiqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
شبی هیجان‌انگیز از جام جهانی ۲۰۲۶ در ریتزوبت
🔥
⚽️
فرانسه
🇫🇷
- نروژ
🇳🇴
⚽️
عراق
🇮🇶
- سنگال
🇸🇳
⚽️
عربستان
🇸🇦
- کیپ‌ورد
🇨🇻
⚽️
اسپانیا
🇪🇸
- اروگوئه
🇺🇾
⚡️
وقتشه شانس خودت رو با بهترین ضرایب و متنوع‌ترین بازارهای شرط‌بندی امتحان کنی.
🎯
دانلود اپلیکیشن بدون فیلتر اندروید
🎯
لینک ورود به ریتزوبت
💎
امکان شارژ حساب با کریپتو ، انواع ووچر و کارت بانکی.
✅
G5
🅰
🌍
ریتزوبت؛ همراه شب‌های فراموش‌نشدنی جام جهانی 2026
🆔
@RitzoBet_ir</div>
<div class="tg-footer">👁️ 2.25K · <a href="https://t.me/funhiphop/78779" target="_blank">📅 18:27 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78778">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/923838e44b.mp4?token=VO2KRxEiOBzsUU1ljebpjclBGr99g6pCHUAf3sDEVLOJvBvogfT0eYDUwFv77oPWXgjkfmKsjbJFYw7Ts3ZWBfMktOPk60C4FKPWU_GsJ7uTlNqGt9ZD3zHegcFc4FuneiPQ13ifT1WW53k8quCLvWYs7LIO8mwgSBGitfsep0FlgvnXIawUFglYa5Uch80wL4RxMk_SaAZK_vX2FZtX4DbQY9wP1a_YIV4nZIamichNGF7nifjYqil0S3v0wp5Be9_-fZvgfbulgWULCOMnBUhLlNhs94KtDSzSyIru108JwbETgKdAWqLG3sToS9MsIfn7MNCV_VDlOSrSOyMJOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/923838e44b.mp4?token=VO2KRxEiOBzsUU1ljebpjclBGr99g6pCHUAf3sDEVLOJvBvogfT0eYDUwFv77oPWXgjkfmKsjbJFYw7Ts3ZWBfMktOPk60C4FKPWU_GsJ7uTlNqGt9ZD3zHegcFc4FuneiPQ13ifT1WW53k8quCLvWYs7LIO8mwgSBGitfsep0FlgvnXIawUFglYa5Uch80wL4RxMk_SaAZK_vX2FZtX4DbQY9wP1a_YIV4nZIamichNGF7nifjYqil0S3v0wp5Be9_-fZvgfbulgWULCOMnBUhLlNhs94KtDSzSyIru108JwbETgKdAWqLG3sToS9MsIfn7MNCV_VDlOSrSOyMJOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پشمام سجاد شاهی عجب موزیک خفنی داد
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 5.35K · <a href="https://t.me/funhiphop/78778" target="_blank">📅 17:44 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78777">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U9Ysskb73pT5WItdHP-aPndZ0L4tBNunXBTyYgVm6wXO6ZKA05D6Y01Dv7DDHhex7xguz-yOkEhnIUjMr_Kru-_-UFo9ynvO74qndtVxOG-kceh6atL2sE1diT4gnixPLwHQRejUPdgKX-_qmwN7AtwESI-D7IDVLgrg5DJzBtNRntGMrRKqeQRrP-zpO9-SX-bST6bIV_ZLjJoGDKYCaB5jxaGsENPlUKciKUpPLsANAV0lx44rRYlaFyasbY95dw3MyzEGdQa3lyH33nb2NFJB-b6HhRSwCWdH6WZlRr691J1Av_Iti1f1ymCvwIHv171airkKc7QP5rvMWVU1sA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رپفارسی نمونه واقعی جمله "کینه میماند"
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 5.82K · <a href="https://t.me/funhiphop/78777" target="_blank">📅 17:39 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78776">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">منابع عربی از هشدار حمله موشکی تو امارات میدن  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 8.06K · <a href="https://t.me/funhiphop/78776" target="_blank">📅 16:56 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78775">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">منابع عربی از هشدار حمله موشکی تو امارات میدن
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 8.1K · <a href="https://t.me/funhiphop/78775" target="_blank">📅 16:54 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78774">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v4rC53no_eKAuWxELdfZLaWxlFfwjV1jMxM4jqN-3tZo26xAH05_a0drrv0UOpR40Qa-yq6bULd2irhVaw108yIgM8T26SHFmbahMR7FRMI4Q_wuZ9VnQ-ziyRQOS0l8vkMjAcuJjHpFDvWhR2EG-EAEWJJ7lQna_AWnqmFcBPAHmW8smvZkKik9VrzALBJOUKMXgU5vfG-m_s8w7rnpgPcnnGNvaeIat1ztSvkeyG3VRHHnpnZG59diYxCM4pLYGHfDhmeA8DJ7-10Sf77f-DTn6SrS_uWupTbj58hpWrZ4xhtqFnI89bJNzflFkonyz0zSA4b_9-qPMdran_u7Dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر دفاع اسرائیل برداشته یه توییت به زبان فارسی زده و عراقچی پزشکیان و قالیباف رو هم تگ کرده
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 9.14K · <a href="https://t.me/funhiphop/78774" target="_blank">📅 16:31 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78771">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">رئال نیکو پازو ۶۰ میلیون فروخت به کومو
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 9.39K · <a href="https://t.me/funhiphop/78771" target="_blank">📅 16:17 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78770">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b4e63ecc73.mp4?token=vBEQBP2AHMF0HdSjELSqmoI1IoAN4RgvlrziMBfY1AwNibe6b3HGqFUr9jqlM3S3JWRJDWM5fe2h_U5M7UAIHJxIoIFp6VVSn0FgNQ5Gigpaj83HNsqFAdm7dsEGNa-6Shtsu7P8-ezURChEHKPHUMidbNT39rDcjREm6i50ebFFYSpQ4ENFu6rQCtJq2zVUScST0Hoo0JATl7cS_qy1nULEV9T_f1h7QFVvPqK31Hn-bHxfxVD7gPpg1FTiiq0T37yTGoll2aPl5slS-I30jEfYwAqWAVM2YfAZUksJ3nztyW9DnENYLpV8AcZ-d35rjIhkW8O9QapksLAO2Y79cQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b4e63ecc73.mp4?token=vBEQBP2AHMF0HdSjELSqmoI1IoAN4RgvlrziMBfY1AwNibe6b3HGqFUr9jqlM3S3JWRJDWM5fe2h_U5M7UAIHJxIoIFp6VVSn0FgNQ5Gigpaj83HNsqFAdm7dsEGNa-6Shtsu7P8-ezURChEHKPHUMidbNT39rDcjREm6i50ebFFYSpQ4ENFu6rQCtJq2zVUScST0Hoo0JATl7cS_qy1nULEV9T_f1h7QFVvPqK31Hn-bHxfxVD7gPpg1FTiiq0T37yTGoll2aPl5slS-I30jEfYwAqWAVM2YfAZUksJ3nztyW9DnENYLpV8AcZ-d35rjIhkW8O9QapksLAO2Y79cQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مسنّین خلق
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 9.85K · <a href="https://t.me/funhiphop/78770" target="_blank">📅 15:51 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78769">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">وا  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/funhiphop/78769" target="_blank">📅 15:37 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78768">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ueobnusgu-4ZclXuUlkdT_YDyiyfM1OlalU3xuhIlr7pInAcJBkYLW-ksjo1gEyTa0A8luVdez6_BoD88aX_uGaovSb2b3hmYgW7_eCHqzbGA-SKKanQ83B7RisUJHk4YxdwP5Lvuc9ntDtkGQimlVyfvpcZ-tyqXQ63RgT2PI4uNta8G4Ou-advGF1RgiJmBFysK82jOK75n5ATw0FaKFKZ330tH21FkNUzXsgE1pjkVKU0rbsEhIqFf1FCl2hL8XEBi0LLSeLAp2zcxEGxjl8xgPrEbSJzNBT7m8rv3w_g1xAE8suT6Y3PXmrAMWludgAgqV0OL7Kh6MGKhutoyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وا
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/funhiphop/78768" target="_blank">📅 15:32 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78767">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">بهترین ترکی که بعد جنگ منتشر شد چی بود بنظرتون؟
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/funhiphop/78767" target="_blank">📅 15:22 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78766">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">اینایی که از علی گرامی حمایت میکنن اینستا بهش شماره کارت دادن یا تلگرام
@Funhiphop
| Mmd</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/funhiphop/78766" target="_blank">📅 14:10 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78765">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tCdoJJUhw7f3cE13RFgNQtbga0hhVPWyzvuPu4WaoGZBTjQA7sPfM3ozRr0ebRHA4G9wGcu_fb_JFTptw1WuU6WbIN3FkhgUZYnXudfmnRol9XmOVoJOtLONyiTX9t9fbgf62vzuGIgqTMXkyge3j2Bb6V6ffrtjLPp3fmXWAFvIM5kPjDGKvPG6LXlCYRM5VxL1w-m1S8bpn0uoyjAeOOaScdrhSyBzTgUM9VkXxM7Mx02aZN5pt4qvltIyk1dV-CLXO5QZFvcN_06RxFcbNatL0_WhCAoE2OFGYYSq_t7T4BJ-8nRvZNkDbFjCNX9N0H0iPWyNoXh5qDZ4NwmckQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کمبود خواب داره بهم فشار میاره، چرا دارم دونفرو تو عکس میبینم
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/funhiphop/78765" target="_blank">📅 13:53 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78764">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">علی گرامی به کدوم قبله قسمت بدم نخونی
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/funhiphop/78764" target="_blank">📅 13:49 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78759">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">یه‌چنل بزنم فرم بزارم برعکسشو بزنید؟</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/funhiphop/78759" target="_blank">📅 13:31 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78758">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">یه‌چنل بزنم فرم بزارم برعکسشو بزنید؟</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/funhiphop/78758" target="_blank">📅 13:29 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78757">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">یعنی چی که به بابام میگم سند خونه رو بده هفته‌ بعد دوتا سند میارم برات میگه نه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/funhiphop/78757" target="_blank">📅 13:21 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78755">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TZvq3xeum-ZZchJQNTLrt3g7UKQScH1tXWvnJdj5LqGf6DZ52YRkIA6AHnYylVXoBVPu7YVaOd2nJQiNh4Hg_CjTZ6bcl4L6VR0DDaNDChEC1cvHXOjLmaOivO5RipC6Qr7fdhLfiU1ExKy0mPgY5meqOgJ3ka_vxTRwsVLft1D8Xx4Ohov6XXpdMEUUbywBcBFSXhAa8MIticHA7eL2Z5nuKt2YVwJhv0_9gnYCdTEWtscU5qaXZ5txvAGHLWRL2xnvaO3ndp_l-B-Wm3FNgzEP8CmKDk-Y3XXXx6hceb-pN5gAOv1A1rHTGY5P5JnhGcO9Xn40n-W4XUvWaclwQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وا مگه شما به لباسش هم نگاه کردید؟  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/funhiphop/78755" target="_blank">📅 12:50 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78754">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CDzQhHSqEUkZyj4deuiKqgE05lmDXzfU7y6lrqE1YpLITgZIgBix7A6SyH6gg6pQ-EBp3Zs-pydmB-YKwvmjZpKfqWtGjt55Q140gMxJ-5fu7owMQ0hO0XIgL0BV23bVINZX4dQSOsU4_umXIPhbMvmDlLZDtDo1TpEKtxF15iFkdPl5hBmVOuJKJGNh1AJR0JuEcrNKy5ikttlI0L8FsPd-fWRajEl4W0iqTZRpqmLb126XtDJAyQQaNp0JWvKQYVn6-zjyRzpVAJLRHVFmV9A6_H_Y5q_vfBNxaji33oe4vhoMFdYvgUPpizUgmtFbskVQBT6qUSlk0b-QBnNooA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تمومش کن تروخدا
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/funhiphop/78754" target="_blank">📅 12:16 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78753">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">مصرو خوب نگاه کنید، وضعیت ده سال ایندمونه اینطور که مشخصه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/funhiphop/78753" target="_blank">📅 11:51 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78752">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">وا مگه شما به لباسش هم نگاه کردید؟  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/funhiphop/78752" target="_blank">📅 11:41 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78751">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OqDZrqqmVHZfTADy1nDyF2jNSLwVhXahCL9dl87dzbOvgE1bA4BqyP3UJOXJX8ovE3pEUXG_8yfXyvRkdDP938crsq3lvlcMw1DtHsJrqjfslXpakoBYrMANbXHo2W21o5hOi8qRfqX7fm_PT5cz_Vkp5qoMjnfekdRcMb48PzG57lZcYLL9R3E6EX3Wji0Oiy_GvIRSGzgnTzbawnKFmo3GyKiG3zBjh2IM6U__DDg17R0sOa5IWCwRDLwyLtuFKn-NSj79bKD5hoPbVhkzof45sU_tn_RRKO1ihtlN-NEBrumRaCbUTlBRrbcjwNu237L5zeI7M9I9qfNE9imfPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وا مگه شما به لباسش هم نگاه کردید؟
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/funhiphop/78751" target="_blank">📅 11:29 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78750">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🎉
پیش‌بینی بدون باخت
🎉
بیمه پیش‌بینی
👇🏻
ویژه مسابقه ایران
🇮🇷
vs مصر
🇪🇬
همین الان وارد شو و علاوه بر
0️⃣
0️⃣
2️⃣
🔣
بونوس اضافه اولین واریز با معرفی هرکدوم از دوستات به وینرو تا
🤩
🤩
🤩
🤩
دلار درآمد کسب کن
💰
فرصت محدود
🙂
🔤
Winro.io
🔤
Winro.io</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/funhiphop/78750" target="_blank">📅 11:29 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78749">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tWcBNZYK3F82uDEsqu6mpw4YbVDLHm2WXHiEs73xSIlRSIuNGMm5EvD3NkvhhtAKeQWijgBoZbn_N1xJGTobFg2WtutAJzFfApqU9azOJIw4yjvpJf-gz7TVOq2b9lfjtNjYlh-BPHuNjqB0gMOde-eI344pOUdc45hCABNjARSHZwKmL4pyQODYPiNmdfpGMiakn2tlfTBVNyE-jdpvQoFiADIIH6XXiXw0xTG2YZAlk7_UUKY7eF-flZHRC-mL8Xlr5UiyovWwW-w4HknhFrOK41FkU2YIsqxb2YLDFfql62LI5-t4ajYPAUlXHPsakXXI9XxItVxPeDibw4962g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
برای اولین بار در ایران و فقط در Winro
🇮🇷
🎉
پیش‌بینی بدون باخت
🎉
ویژه مسابقه ایران
🇮🇷
vs مصر
🇪🇬
✔️
حداقل
0️⃣
1️⃣
میلیون ریال واریز کنید و روی برد ایران
🇮🇷
شرط بزار ، در صورت باخت از وینرو فری بت بگیر
🟩
⚽️
اگر ایران بازی را ببازد، تا سقف
0️⃣
1️⃣
میلیون ریال،
0️⃣
0️⃣
1️⃣
🔣
مبلغ شرط شما به‌صورت فری‌بت (Free Bet) به حسابتان بازگردانده می‌شود.
✔️
تنها سایتی که این بونوس را ارائه می‌دهد
✔️
فقط برای مسابقه ایران مقابل مصر معتبر است
✔️
حداقل شارژ موردنیاز:
0️⃣
1️⃣
میلیون ریال
چگونه فری‌بت را نقد کنیم؟
کل مبلغ فری‌بت را روی یک شرط با ضریب 1.80 یا بالاتر قرار دهید و سپس سود حاصل را برداشت کنید.
🅰
r5
⏳
فرصت را از دست ندهید!
🎰
همین الان وارد شو و فرصت را از دست نده!
🔤
Winro.io
معتبرترین سایت ایران
🔤
Winro.io
📱
کانال اخبار و هدایــا
🌟
📱
@winro_io</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/funhiphop/78749" target="_blank">📅 11:29 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78748">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">دکی ناموسا بیار پول این ویناکو بده کصونه واویلا بازیاشو بس کنه، همین مونده بود بیف سر قرضو قوله ببینیم
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/funhiphop/78748" target="_blank">📅 11:12 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78747">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">بابا خستم کردید، چطوری هر ده روز یبار روز دختره</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/78747" target="_blank">📅 10:42 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78746">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">بابای رافینیا پولای رافی رو پیچونده، و الان رافینیا هیچ پولی نداره.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/funhiphop/78746" target="_blank">📅 10:32 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78745">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">ویناک خطاب به دکی.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/78745" target="_blank">📅 10:08 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78744">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">چند روز بعد شب جمعه خود را چگونه گذراندید؟  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/funhiphop/78744" target="_blank">📅 03:21 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78743">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">هرچی دارید رو ببندید روی برد هلند و ژاپن
این سری دیگه جدیم
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/funhiphop/78743" target="_blank">📅 01:21 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78742">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">هرچی دارید ببندید رو برد آلمان و ساحل عاج  بماند به یادگار   @Funhiphop | Farid</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/funhiphop/78742" target="_blank">📅 01:08 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78741">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">سلام فرید جان خیلی وقته که دیگه صدای انفجار شنیده نمیشه
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/funhiphop/78741" target="_blank">📅 00:46 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78738">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">سیتی عجب سکسیه، هیچوقت تیمش ناقص نیست، همیشه بهترینارو میخره
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/funhiphop/78738" target="_blank">📅 00:35 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78737">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">۹۰ درصد رپرا و اطرافیانشون حرومزادن، سعی نکنید بین اینا خوب و بد رو جدا کنید.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/funhiphop/78737" target="_blank">📅 00:23 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78736">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IcbGWApviBWG6c9xXYQKyMsKCSvwovYARVkexZeVC3WnAoZjCWWiViWyLb2GTGaTQGnDs6LdYLw5jhP2h1L_x-sRPW9xik6a1W2n6p4VBNBk_6aahhtj6my6T-PSBUtXinVPEBNbdByj35mETqDdLV6CP-ybGz_WaFEb2YYhMrsePC_C0Ir-4ZNsmIPXrC12RjB8MKnpOahtzJ2XDOB5a5siHOeG6L_9KmIWCWUDLHbPuDWon8icT2ArUr4GLKZDZnTFZGgaRf1uHV0mp8xY_QYVYDiOanETxlBUE_mbq53Q5c1sBXARtJ6wAOI2SOLh-0LOjU3-rwTrXp5fB_nNdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تو اسرائیل دنبال قاآنی میگشتیم
تو هیئت بغل عکس خامنه ای پیداش کردیم
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/funhiphop/78736" target="_blank">📅 00:20 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78735">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fID0pX8f6j3V4PTglVkSV2Ad4gNy2QBLR99dJMXuTAXrkHhZDKLpp2DAWU7n-ye2no6a3BDfVRzIuvuS1SGs_n-xoF6wioQ3eJX7VDDwhvKDUzDyACpBgySbiG_gLwRtttg_XCddm1dOIR8yYCcrFCT5RfsWpjGXveKSZ9P8OQ6gTdo1dzrZzyrNt3kWreLBp9Cw-cNM6K2s9gihCoeiB_mRs5YjxyJUVM45muQkNpGY0eoBuNJw1usSbAAFoIwgKsVEasxl5oOzxJqjx__6F5GkrPUKPVs5Uh9VfmDOmIssDQU0SIFdqYncI_ManXwkBl8CefvkkUyUsStFt9OmSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">باقر شاه با حجاب
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/78735" target="_blank">📅 23:56 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78731">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">هرچی دارید ببندید رو برد آلمان و ساحل عاج
بماند به یادگار
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/78731" target="_blank">📅 23:25 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78730">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r1NYoff3hr6TOBs4d3vO5jYx3uq8lWpK1ZRcTrenlyyK9rTiaJo-WGyHAvYOnCb3o1xEmoWGfa-_k3_ASyzhBof8uj_SWren0Fytb0jWpNz2a5v7ckaVCXWS5qmqbrp6gki9fJaTtkxFcV0Dwy_VanxD3mb-Vdlr4_oeLwVxNkR5s0e-QcogBgm3tvlLgGYP5rfQ2CCXzimKtwjNYPwXpDi8SkUCL0hpYZW4YI-AYOFhRrpkyp8gqvjea1Vpm2H8yQcSlIc3azNeWrgwqYC65thFGBTN9aUbUH4b9pSa3Fn9OdAoli8rmE5BMy29ZfNlremAxJSR2sajJXQpTp5c5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تروخدا منو از ایران نجات بدید، مگه میشه تو کشور ۱۰۰ میلیونی یه نفر عاقل پیدا نشه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/funhiphop/78730" target="_blank">📅 21:57 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78729">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S_Gc-_K5HN2fu57DLKs0eM9E6VIdGtgdU4zeIMJKuRMOpJrHAg7joVdZe97N0OigWlgLKh0_TdHUMKvS-z0g2aH-QxDm4g_XlGE_KJX9p5Wqz4r71KaCKI5WynsfvZWy_YctwIcub8vwTc8h7rKdq57X3YEtX6kwRz7FCL4QROaokdQzhf50P_4iX6jxfoBKXkRopORu1lA6UY5x6GuSr6PYVMaMrZuWQYdsXbW4kAVoT5y0-57duxU1HhfLIUU3WXvgIpnwiC6MYQKttidUG1TNI1PIUpAMIOofqHrEsL2aG7l3IiGZSRnJzKVHT89x9kkobDtCaE50HzjDdUCFuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/funhiphop/78729" target="_blank">📅 21:26 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78728">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YcLUV9eeFyyD_J62IoNVrlyOai9jWf3Sc1KXgOe8Oc61gk9D7gAkMc5BPeIRrgdKmOwnCJF4Hr-x79cjRLBoThieAGIVf3zm-u5u9HFgPkZn2mUJwoqPuPZCK8XpbJgrZyrG8qEgEIz_Ugff3tEd42KXD5XAV7z_BtKPGTYDpKep3oJReH4YTOkBImIft6TBpOOMzEaK4TG15IlTINP9pX7YGgbR3WXfE8EhJFWU_oWX2blo7Qfro4JFTcoUmi-P2mK3qqeSTT7pESe5cVLQEWe563Y0OWzsuGGGEErbrsLOpw2jGn_Wd2Anwfy3g9j5y8jA1JEG4y3TDuxdnp7iCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیگه هوش مصنوعی داره مرز هارو رد میکنه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/funhiphop/78728" target="_blank">📅 20:57 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78725">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">تو چند ساعت اخیر کریپتو ریخت و ۵۰۰ میلیون دلار آب شد رفت زیر زمین.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/78725" target="_blank">📅 20:32 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78724">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">لازمه یادآوری کنم که کوچک‌ترین ارزشی از ارزش‌های ما کم نشد هنوز تنگه هرمز دست ماست.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/funhiphop/78724" target="_blank">📅 20:24 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78723">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">یاد صابر کاظمی افتادم چقد این پسر گل بود
روحش شاد
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/funhiphop/78723" target="_blank">📅 20:04 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78721">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HwSB6TNi2tnTxlK8TWy2MAaZfyZb5Lp7oYfwxdOCeKcAZJOxOwHN_mlOG0SsDrHlfL5PXCqXG51nMkD0tfS9B5HRUqV4YbGhzYYm0uAY-kJbomy-SA6bpcyPArJuZyeNX9ETdwD_a901SpUrahpYISD9XFMGAyZVeLbgpYVdH8ny3HtChX9mWdyY19Zp8UVA-zCYJzmi6D4q0ZwHv07dZGg0Kc5H1TTloPZOg5xo9u4hWxdbJCuV6FcgngFX1wea1TYAtOrfV_EsTeKVkDNrtv1nOgOzszxyxckioDH9qdO-UMNu-th420QKXJYz248NMQcqVl12dBkcHN_zZCOdmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توافق حاجی توافق
سپاه باز اعلام کرده تنگه بسته‌ست و فقط کشتی‌هایی که مجوز سپاه رو داشته باشن می‌تونن رد شن.
برا اثبات جدی بودنش هم الان یه کشتی که می‌خواست از تنگه رد شه رو زد.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/funhiphop/78721" target="_blank">📅 18:52 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78720">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">شمر و حسین رفتن برا فایت آخر
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/funhiphop/78720" target="_blank">📅 17:06 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78719">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">مارکو روبیو درباره ایران:
سیستم ایران هنوز توسط روحانیون رادیکال هدایت می‌شود.
همیشه اینگونه بوده و همچنان به همین صورت هدایت می‌شود.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/funhiphop/78719" target="_blank">📅 16:35 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78718">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">میشی فروزان
بلاد بودم نبودی اونروزا
یروز نبودم زدنت فرودگاه
@Funhiphop
| Mmd</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/funhiphop/78718" target="_blank">📅 14:59 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78717">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WOjMws5xS_VLRKn4bl7epB3raoNd-iXgZRG3Zra44nOP2MpOgR1vBG8UqYXN7fqLmaSYKZTX40lNb-jusnlF4FjGQlNu6oz98mr7IB-rxvCooo-o3KN9qerQr21j8td2vt-dXOsnF-hEtrErwr26ELSuEFWGVWMXoskGfn1XAnJoALECPq4-YqLSiIVthw501y4b1fi4dxmLdsi9ZNZwpx50PMc8KOZlFlClVagcFW-L52Nzei0Va-rNnGwhcvOuvB6thvfqpcjWxVxRdqZApeiC8sw0j4ItoEQI2PWCV6UjMaJlohO3YSL3naRyg6APSIFZIX3KtsHm1zO0Awt-1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موزیک جدید ویناک به نام "Gin" ریلیز شد.
📺
Youtube
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/funhiphop/78717" target="_blank">📅 14:57 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78716">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🏳
سرور مولتی لوکیشن موجود شد
💎
🟣
لیست قیمت سرور ها
⬇️
🟡
سرور 10g - کاربر و زمان نامحدود - 60000 تومان
🟡
سرور 20g - کاربر و زمان نامحدود - 120000 تومان
🟡
سرور 30g - کاربر و زمان نامحدود - 180000 تومان
🟡
سرور 50g - کاربر و زمان نامحدود - 300000 تومان
🟡
سرور 80g…</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/78716" target="_blank">📅 14:42 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78715">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BqPLfyg_doChe-5P7_wQZTkndZpHJusYXoHC9VTSbVmOGAwvp_3BShHHLWKVcEzI2JCdyvhPkL0tBj4o90EuUNb27Cnif4Rd24JiOBOErXY7uLv_JFrJxYfwqjkgK9fRXP5LW6Tv6h8FW73wH7y6kumUCj1-2hgtJP7YNzrqdQj27l8s_lc7R-atcx5AL8LcitGz7k_HHfn2XXS-tziucE0BZVPCl39hsoPNeYTwa8ibbxczVZA4DlvZmkWusiEaF6Ofw76xi_Qkba1LV4N9Qg6DhA9HF9ReruaaBhe460k8mbYZAZsWJudV5_HJxiinGeI_AS7HSAZoIL2Z7MB0Vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Gta خریدم تا عشق حال به راه باشه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/78715" target="_blank">📅 14:33 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78714">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">من نمیدونم داستان چیه ولی علی الحساب کصمادر علی گرامی تا ببینم چخبره
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/78714" target="_blank">📅 14:15 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78713">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">ویس جدید آدرویت
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/funhiphop/78713" target="_blank">📅 14:11 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78712">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LJDqfO0c1lYZNu-_8dWylBWbtPm3YJJ6zyQAbQ6BlbFz9sD7fmQnhqyxNkZVXaPFTp42bGcq_b6vxmhxFPZNaPrH5tKJZDZhIGYF5mEmpzQk47D4s9mDgtQ2mKT5GfFNMTUH7hi-6q44Ppd-OTb65aG1qJI_QEJSSE4eVj1LBRN66rhC1e6_-yal1DIuWlokzmWvfTdBoeG6qnnsgnfbqJQYy6aGfunWFcfFQsvH9fAzMsVcG_Os8o1uruIKt_7iFUN9if4kaygVZ0y32H-GNmC16_1YicBDSOzBr89DXFXYsLNJ4WNfORBCVDxgDKDceOzQIKWiFP9oZSkULobKDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چی بگم والا
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/funhiphop/78712" target="_blank">📅 12:10 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78711">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">کاش اینایی که برا محرم شهریه یماه باشگاهو دادن بیارن کارتاشونو بدن من حیف نشه از فردا که نمیان
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/78711" target="_blank">📅 11:51 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78710">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6ade4f7604.mp4?token=sLl84mK68Elaq1Wj6vQGmvF2UFVOjWF_r6QFhOLdMPPQ8HrrYPJB8yv--j0VXu-Vew7MLGNwqcEcFZO67wmaDQFYJO1FwSvQ38ZjPBszsacBfb8xLivn9Xntag7EsCAocNHCnCYWUdEHZLRcIxC7CqJQvu4tGrk06yiEY0l-G2C7fm27G4YzXbrWopoCpYka9xkVQstCNSqKefzzPYI3lvXnIH5M9pbDCOZhUtl1OpNGQJC-LVG6or2hp53fdQDIanWzU3uO2KnYUiSj9ngLl-k3PQ0aZrYnJOfSmiBoBifGrAexjBF01jKl5EkjU-ofOMCUZ8y9YCT0Giu0FFRgQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6ade4f7604.mp4?token=sLl84mK68Elaq1Wj6vQGmvF2UFVOjWF_r6QFhOLdMPPQ8HrrYPJB8yv--j0VXu-Vew7MLGNwqcEcFZO67wmaDQFYJO1FwSvQ38ZjPBszsacBfb8xLivn9Xntag7EsCAocNHCnCYWUdEHZLRcIxC7CqJQvu4tGrk06yiEY0l-G2C7fm27G4YzXbrWopoCpYka9xkVQstCNSqKefzzPYI3lvXnIH5M9pbDCOZhUtl1OpNGQJC-LVG6or2hp53fdQDIanWzU3uO2KnYUiSj9ngLl-k3PQ0aZrYnJOfSmiBoBifGrAexjBF01jKl5EkjU-ofOMCUZ8y9YCT0Giu0FFRgQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/78710" target="_blank">📅 11:41 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78709">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">شیر امسال خوب غرش میکنه، فک کنم بازیگر عوض شده</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/78709" target="_blank">📅 11:32 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78708">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">ذرت حاجی ذرت
ترامپ : وای! سنا رأی خود در مورد ایران را از ۵۰ به ۴۸ مخالف به ۵۰ به ۴۷ موافق تغییر داد. رند پال و بیل کسیدی تغییر کردند. از رهبر جان تون، لیندسی گراهام، برنی مورنو و همه متشکرم.
این رأی، ایران را در معرض توجه قرار می‌دهد
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/78708" target="_blank">📅 11:29 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78707">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">کص ننت آروم بزن خوابیدیم</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/78707" target="_blank">📅 11:22 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78706">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">امروز قراره توسط آمریکا تجاوزی سنگین رخ بده از همین الان میگم چیزی از ارزش هامون کم نشده
❤️
@Funhiphop | Jenayi</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/funhiphop/78706" target="_blank">📅 10:34 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78705">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">امروز قراره توسط آمریکا تجاوزی سنگین رخ بده
از همین الان میگم چیزی از ارزش هامون کم نشده
❤️
@Funhiphop
| Jenayi</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/78705" target="_blank">📅 10:25 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78704">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TfoFowTFRgcDzSrzqtTFSP3G_ukmu7WueGnQR5OzxURqJDGjQ2OfKZpUbYi4IBaxbIRzmHxizXsWXlCM3KSn1lmRxkDVvXRcNY9JaXZOXeLv_FkSkvohQRF31LG8todAyQiIYLR7miivkiMH3dxLDHWMCm0CQ_vqnvKu7ElhM38OCQnIykxjF4W97BfaPiLf_vfrncdxKf2eKSMs1OgeUCN0tfKdf5tX0pr27ZC7p6mFICqrZ016T_k9LlxYX_M6f3I1nlunctCL2tnDFBu1e9Qv6_AseG1S7DbDym4TYda-X1xkDaWlqmDWAvHtbACHxwzxAW5RVgF-R1QpT3AThQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیشب 20 دقیقه بازی کرد و حتی یک بار هم مصدوم نشد
اینه شاهزاده فوتبال
🔥
@Funhiphop
| Jenayi</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/funhiphop/78704" target="_blank">📅 10:20 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78701">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bbd2d4d123.mp4?token=IQpqteabzNKasC9vmflD3n6L9rczlX2RKrGoxRaFQZxZTrcqBlWqPXM2INkN83liltxA4r6PHHY4Y3moyoxdD_aqVP9_GhbKUJTW4s8EPldYEAudSgbRt241w5x1OQfbqAJ6DYJhR3yCupyGUhdNCGkAZkRTBOlOf2C1U0weKHBbRHUutfKgcYmgoqtAbPH3JRLz6SEai4G8LDcicI23yFSt8jDW1sLUocQZsgj9gAxqtuyHIzu1ybnJQloXCOhUym8GtXAd8azQ4UNfOggBKffAA5VihQiEoayx9SrJ0bLJr7gXsmpKLrR8WuwYY0z93KEo4VCYJgFbh_0B6W-JTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bbd2d4d123.mp4?token=IQpqteabzNKasC9vmflD3n6L9rczlX2RKrGoxRaFQZxZTrcqBlWqPXM2INkN83liltxA4r6PHHY4Y3moyoxdD_aqVP9_GhbKUJTW4s8EPldYEAudSgbRt241w5x1OQfbqAJ6DYJhR3yCupyGUhdNCGkAZkRTBOlOf2C1U0weKHBbRHUutfKgcYmgoqtAbPH3JRLz6SEai4G8LDcicI23yFSt8jDW1sLUocQZsgj9gAxqtuyHIzu1ybnJQloXCOhUym8GtXAd8azQ4UNfOggBKffAA5VihQiEoayx9SrJ0bLJr7gXsmpKLrR8WuwYY0z93KEo4VCYJgFbh_0B6W-JTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حاج اقا بنظر شما آقای روحانی کلید تدبیرش کار انجام میده؟
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/78701" target="_blank">📅 10:06 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78698">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">هیچوقت فکر نمی‌کردم با صدای علی اکبر که داره آماده میشه بره نبرد از خواب بیدار شم
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/78698" target="_blank">📅 09:32 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78694">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">خب دوستان یک ساعت استراحت کنید تا بریم سراغ بازی جذاب چک و مکزیک
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/funhiphop/78694" target="_blank">📅 03:33 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78692">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">وینیسیوس تو بهترین شبش هم باید ثابت کنه کصخله
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/funhiphop/78692" target="_blank">📅 03:16 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78690">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qMauUy55GOaJEoLniNiuf_949wbcn9EmO-T8oP-olYloNEC1LVOrkkFfFRFHs0sTWxMGKO3LSTVYP0KlxRQxg3hL27kg-PdIRdC2w32scAXT0zMpIvQp9kEOLIPlJ43qTlLjqPWWVyPhI2exttBiDw1Fb3C00ZCdmMMRlWVKWb_Q4aurO3OQRquj9nQrLmRTE-XPx-c0xzZ5lqxxo7atmm77LrPb9nusyBEYFUgRrd4rRgv7hYImiJua2ieAY830RJUSPq1ZI1QKB9Ph5B-jbhDdxL6mtKnHcg63KVQFd0jnW1LAeZFr8bUS6RKy-KfWkvJNiqrMOBMDrkN7V7NDDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بایرن عجب جواهری قاپید</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/funhiphop/78690" target="_blank">📅 03:07 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78688">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">ونزوئلا زلزله 7.5 ریشتری اومده
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/funhiphop/78688" target="_blank">📅 02:55 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78684">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">با این جدول تیمای سوم که همشون دارن سه امتیازی میشن، ایران از مصر امتیاز نگیره نمیره بالا</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/funhiphop/78684" target="_blank">📅 02:21 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78682">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">من یچیو نفهمیدم، تیم ملی فوتبال تیم جمهوری اسلامیه تیم ملی والیبال تیم پهلوی؟
خب خار هردو رو بگایید چرا تبعیض</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/funhiphop/78682" target="_blank">📅 02:18 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78681">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">کصخلا آدم فضاییا یه فرد باهوش میبرن به دردشون بخوره، میمونو میخوان چیکار</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/funhiphop/78681" target="_blank">📅 02:15 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78677">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">من دقت کردم از وقتی که دیگه کشتی کج ندیدم کیر رفت تو زندگیم
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/funhiphop/78677" target="_blank">📅 01:49 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78674">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">ی پیشگوی شیشه ای خارجی گفته امشب مسی و رونالدو(آدم فضاییا)، وینی و نیمارو میدزدن.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/funhiphop/78674" target="_blank">📅 01:31 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78673">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">شاید باورتون نشه ولی تیم ملی ایتالیا دوازده ساله که تو جام جهانی هیچ باختی نداشته.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/funhiphop/78673" target="_blank">📅 01:07 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78672">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">قضیه لست دنس رو جمع کنید، مسی گفته اگه بدنم یاری بده ۲۰۳۰ هم هستم
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/funhiphop/78672" target="_blank">📅 23:38 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78671">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EKT4XTQD49Yk0PjzJJGPck0QPiUH2bdQNVwqSJKZu2_7goHRWQxDSvJ-Wtc8JdMTFaPvaIvb0XuLkdPqPVopuXxBNkaD9hN69qNlIw2LnhDLHajjaWdfywqBKaJvWqz1eVHJbhNcguAzXvT6Yzc7f0Vf7ZC3s03HD7X8I5wUqMTX2AWNAoJie9Vy9OPivC0UxJcWpEkors9InjF9OymL7H2c4T6sfu3-n-jwqTZKxgDgAuc3ttKgGJVkP6MJlNPz4YE3O5wM8MjPw7ccqaWGWLzhZIvJRnahyf60P1WhxOhDbb6yWt0HBUFUCFEAcmHnki56kwtuH1K_xCoyf64Akg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه سخنی هم از مادر عروس
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/funhiphop/78671" target="_blank">📅 23:00 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78670">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">تلگراف: ترامپ با توافقی که الان با ایران کرده؛ فقط میخواست جنگ رو تموم کنه و تنگه هرمز رو باز کنه تا قیمت نفت پایین بیاد و از فشارهای دموکرات ها کم کنه. ترامپ بعد از انتخابات ۱۲ آبان ماه کنگره و سنا این توافق الان رو کنار میذاره و دنبال توافق جدیدی میره که هرچی ایران داره رو ازش بگیره.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/funhiphop/78670" target="_blank">📅 22:00 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78669">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromApexNet Shop | اپکس نت شاپ</strong></div>
<div class="tg-text">🏳
سرور مولتی لوکیشن موجود شد
💎
🟣
لیست قیمت سرور ها
⬇️
🟡
سرور 10g - کاربر و زمان نامحدود - 60000 تومان
🟡
سرور 20g - کاربر و زمان نامحدود - 120000 تومان
🟡
سرور 30g - کاربر و زمان نامحدود - 180000 تومان
🟡
سرور 50g - کاربر و زمان نامحدود - 300000 تومان
🟡
سرور 80g - کاربر و زمان نامحدود - 480000 تومان
🟡
سرور 100g - کاربر و زمان نامحدود - 540000 تومان
🟣
همچنین سرور تست موجوده حتما قبل خرید از ربات سرور تست دریافت‌ کنید و بعد اگر راضی بودید خرید کنید
✅
🟣
برای خرید از ربات زیر استفاده کنید
⬇️
🤖
@ApexNetShop_bot
🟣
برای ارتباط با پشتیبانی و مشاوره با آیدی زیر در ارتباط باشید
✅
👨‍💻
@mehdi_splus</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/funhiphop/78669" target="_blank">📅 21:23 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78668">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Uph-bqCOQP6MuuWu6C5EMJXg_WK4DLn3uEPLvCVr_OsKHHG7D3fV6GYOjpTTv_sfQuKyzSbFe7yMLcQvpECpZeH-nxL2Y-Gah4dhYKRe4nHZBqbs7fvkJSue6WrQsbCnil5nRR4iW-oWTKZmzK1BS2CgRmuKas-4JbxJjZzLrgFeS8ULiTxrreY8N7BWYppcaBI14dfFyZtdT69nQglxhlCAQjquFvGO4WNBcaqnuF2-YPzPDaseI7HGnmOXhkuELUo5xeXvLYONW_Ej4YF5bNOgE3vc14IuwLZ4BHe3NPzF-EoR_IamdLRc6GM2Yzm6ZJyft0--l5_YZoeXkf8nmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سلام آقا ببخشید این رپر کیریاتون چند؟
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/78668" target="_blank">📅 21:14 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78667">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZI3vNm_nqlLHjA8yfXfO-bUAZNHPhk4l0TRoiEHiUFuguuNt5NEyUKxOmhKjjWi4IMdztlH3SkgxXzaQJNbZyptvtaAfTCG7Br6L1st3HXue_kPTQ4NVQ4N-lo7aKdA3mTDb9CpREdO7WzEOZeLa8Wm2sk3LlG3R3h46VsRkV5nqH3UhsViLE4PPJwjvLhbIZS-ltxcoTNjzEUxWBduyHZfqluNo8A51YhVvxLe_Qd9HbBxmuf850SqdoNVetKgqyWbBfFTR6Z_1IcpYSEF7k7byOdjfgC-4MbqdABMd8_OdN154AK5R6Q10JOZ32UOa8LeUtu4dYyEa2RG6OmCouw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خدا زده ها شما چرا اینجوری صحبت میکنید
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/funhiphop/78667" target="_blank">📅 20:13 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78666">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">بنیامین نتانیاهو: چهره خاورمیانه را تغییر دادیم، بیشتر هم تغییر خواهیم داد  @FunHipHop | Farid</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/78666" target="_blank">📅 19:40 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78665">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">بنیامین نتانیاهو:
چهره خاورمیانه را تغییر دادیم، بیشتر هم تغییر خواهیم داد
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/78665" target="_blank">📅 19:38 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78663">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0af0e4cc84.mp4?token=QuZvWhw99TRQC-Sxn7iVenUpMJXSudMZ7TKd-mJYsR_54ZEECxQog0zOPL6n71yYYKNUaRaDtdZuZV_NjssblnGxZKW1ZhV4aV3dJSfbuhXxgNI0a-UZjnC0FsYa14-E7wKOza5FjtYF7TwDv0Tf6SzQ1Bown2iIPnYpUP5djhKgscbBmInSeVLnLD8hu3N_oumx426DG6fTENOmSEgKKPOPWvk8fMXRtNYvEpvYOlhFLcTTY83_MiTrjxBmmXd5SS6RMhAmukWq7sDNhRDAKAJs8M4cl4SWhrXle93kUgtOHHER0HAPDUVci04Y9CgrfC31QR-4XBmCU1vwRF-gNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0af0e4cc84.mp4?token=QuZvWhw99TRQC-Sxn7iVenUpMJXSudMZ7TKd-mJYsR_54ZEECxQog0zOPL6n71yYYKNUaRaDtdZuZV_NjssblnGxZKW1ZhV4aV3dJSfbuhXxgNI0a-UZjnC0FsYa14-E7wKOza5FjtYF7TwDv0Tf6SzQ1Bown2iIPnYpUP5djhKgscbBmInSeVLnLD8hu3N_oumx426DG6fTENOmSEgKKPOPWvk8fMXRtNYvEpvYOlhFLcTTY83_MiTrjxBmmXd5SS6RMhAmukWq7sDNhRDAKAJs8M4cl4SWhrXle93kUgtOHHER0HAPDUVci04Y9CgrfC31QR-4XBmCU1vwRF-gNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ماشالا مهدی، ماشالا به این تاکتیک پسر
🔥
@FunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/funhiphop/78663" target="_blank">📅 18:53 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78660">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">خدایا کاش سریعتر GTA 6 بیاد که GTA 5 ارزون شه بتونم GTA 4 بخرم بازی کنم</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/78660" target="_blank">📅 18:50 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78659">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">راکستار:
نسخه فیزیکی GTA 6 فقط شامل کد دیجیتال هست؛ دیسکی در کار نیست (البته فعلا به خاطر جلوگیری از لیک شدن بازی)
- پلی‌استیشن: GTA 6 بهترین تجربه خودش رو روی PS5 ارائه میده؛ همکاری سونی و راکستار گیمز تأیید شد
-گیم GTA 6 روی PS5 تقریبا بدون هیچ لودینگی اجرا میشه!
-ظاهرا داستان GTA 6 مثل Red Dead Redemption 2 به صورت فصل‌بندی‌شده و اپیزودی روایت میشه
-بازی GTA 6 در استور پلی‌استیشن به‌عنوان یک تجربه کاملا سینگل پلیر ثبت شده
﻿
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/78659" target="_blank">📅 18:40 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78656">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/79017d5ab5.mp4?token=TqIwe_TNhTZNu4b5zBv38LLXiK8-oARjmb5TelMoPZs_2wOJXnT8lIDLtIjW90DofbwLUq4GudDVsNFYfhX9W-7BUCsVz9z_P9EeBTMIQOymQEKQVMHOAwdkHH-oxTLu4gGrsJcOsc3WDIvpHXFDb-5w3u6UJ4jDmYZxQguBj48oQdZxhoynrEozXJlxY-k2U71jil0aQXaa2y0Id0sgViUWBDoMlBzrdIsxwpNo5A3Eff6G-cBf7aWoRhF3L538tCzIZc5g6rRULtIOqmZB53AWoMK_oMm4fSfnuLCBktYQz4xU49fQyv7B8baRdxr9pw3ZjUaAS-Lz5nM1xS8iDykyplpwydyt3KK7wiV4hX9bnS9VTHWFbXkTPlFQlcgRxCR6VMYmGgTEj9Y19PydE4DhK21Pdf0kTSkzzYCflMRRiYT9D2rXFdjQMQ9jp8c9twdqxMBl1TRaAFdgaRHBJSQwZNsIqV_uwVzU8zbaYIaXFc9H6RJIwuFjhLqwqrvWBfyNG4agBakS9QFCdBCKHKFj3VRjwjl2BoCZTifAkbP3YZTMiPPRwBr3SELx_4OoJxnC5e2jwZVY3vyWvnU2NDsS7CqeCV5zkEBG2mI2AMiF-OFaKWbgZY4hr83xAxcg9Te8O3oZGHX4vu1ZSXHOlaPz28c6zMMTzOUmOw4TG3s" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/79017d5ab5.mp4?token=TqIwe_TNhTZNu4b5zBv38LLXiK8-oARjmb5TelMoPZs_2wOJXnT8lIDLtIjW90DofbwLUq4GudDVsNFYfhX9W-7BUCsVz9z_P9EeBTMIQOymQEKQVMHOAwdkHH-oxTLu4gGrsJcOsc3WDIvpHXFDb-5w3u6UJ4jDmYZxQguBj48oQdZxhoynrEozXJlxY-k2U71jil0aQXaa2y0Id0sgViUWBDoMlBzrdIsxwpNo5A3Eff6G-cBf7aWoRhF3L538tCzIZc5g6rRULtIOqmZB53AWoMK_oMm4fSfnuLCBktYQz4xU49fQyv7B8baRdxr9pw3ZjUaAS-Lz5nM1xS8iDykyplpwydyt3KK7wiV4hX9bnS9VTHWFbXkTPlFQlcgRxCR6VMYmGgTEj9Y19PydE4DhK21Pdf0kTSkzzYCflMRRiYT9D2rXFdjQMQ9jp8c9twdqxMBl1TRaAFdgaRHBJSQwZNsIqV_uwVzU8zbaYIaXFc9H6RJIwuFjhLqwqrvWBfyNG4agBakS9QFCdBCKHKFj3VRjwjl2BoCZTifAkbP3YZTMiPPRwBr3SELx_4OoJxnC5e2jwZVY3vyWvnU2NDsS7CqeCV5zkEBG2mI2AMiF-OFaKWbgZY4hr83xAxcg9Te8O3oZGHX4vu1ZSXHOlaPz28c6zMMTzOUmOw4TG3s" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اجرای جدید هیپهاپولوژیست
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/funhiphop/78656" target="_blank">📅 18:21 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78655">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🔴
پسر چی داره میشه تو این دنیا
ترامپ دو ساعت پیش: همه از نتانیاهو متنفرن
قوه قضائیه یه ساعت پیش: ازین به بعد هر کس علیه آمریکا شعار بده یا حرف بزنه، 1 سال حبس یا جریمه نقدی میشه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/funhiphop/78655" target="_blank">📅 18:01 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78654">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pd6XMLWgddL3sMxKJopt0F3-KdRHrM_Sz4R-UHo3mqAv0RJXFUrdmLbBdORX80e9WocVI1YZuXJnfOGsidlQcU31l-ajedSTN5UaCFB7csR2aBmp3QbaOmR4c9zLMcjwEmppUmKKHToNKxTv-wMrm4puajTzb_FxDAbK-Rg6IvhzW_v3x4Bzguj4VeIbr6Kzv2dHcJC4dEuToRQrewrnGZ65JXCqawlYF5VkcKW4cql5MdaJSbgXDgoT9utkuFfDMZrlroICkICSlgDqlgvut6eQLyB5ahGioU52yEaSph0AREiDlL8ZwcDHoTd26h_D0OW3LiSPGV1EsNFxo_Z1Pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دادا بخدا داری اشتباه میزنی، سیستم بدنی باید حین پیر شدن افت کنه نه پیشرفت.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/78654" target="_blank">📅 17:50 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78652">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">از این ۲۰.۳۰ روز نهایت استفاده رو از کل کل سر مسی و رونالدو ببرید، فردا روزی که اینا نیستن بشینید راجب یامال و وینی بحث کنید همتونو فحش کش میکنم
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/78652" target="_blank">📅 17:42 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78651">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">نفت wti شده 70دلار
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/78651" target="_blank">📅 17:32 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78650">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/222f81be11.mp4?token=UuQV8XBHY-cq69b8KSpJF9oXF7TDEMCopbeY2sKRoUwyQobvFhN_X9empEhGSIT7wjFPYSnYPZO8YafmiyLi7y_Mz2qfr0hkFvnib0ncICws0XkONuWQMmUTiR5Z_xtbx9VZlTZR6tTUEYRU4DbWVSsyIBfIMCpQBKtcGS62ec4jbkms0NdezDm5T4b3f4SHt5WYySOehR2sMRqybJV6Zs98gQLn6FpN8H5Q3FGgvKatxiXkOckAZtltkuOu-x79McE0pv12EuwgYrJwkDZusxwW4xXMzmIDLqnDbYMg81C3LqTx9rCeZ-PJ_5zzQ3gBbGI9jGSdGe1VGd0nwOPgFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/222f81be11.mp4?token=UuQV8XBHY-cq69b8KSpJF9oXF7TDEMCopbeY2sKRoUwyQobvFhN_X9empEhGSIT7wjFPYSnYPZO8YafmiyLi7y_Mz2qfr0hkFvnib0ncICws0XkONuWQMmUTiR5Z_xtbx9VZlTZR6tTUEYRU4DbWVSsyIBfIMCpQBKtcGS62ec4jbkms0NdezDm5T4b3f4SHt5WYySOehR2sMRqybJV6Zs98gQLn6FpN8H5Q3FGgvKatxiXkOckAZtltkuOu-x79McE0pv12EuwgYrJwkDZusxwW4xXMzmIDLqnDbYMg81C3LqTx9rCeZ-PJ_5zzQ3gBbGI9jGSdGe1VGd0nwOPgFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">که ترامپ گفته آمریکا میخواد به ایران ذرت بفروشه؟
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/funhiphop/78650" target="_blank">📅 16:37 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78649">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">سامان خب آخه...
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/78649" target="_blank">📅 16:13 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78648">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ueRoCsjPb5_9yxQ8nsIlJxXG02GN0wn4xWaSh0qd7-Hq6XejnT9qVFRvsLZqY2cDIh9JXtJBQn30AeAicBNeW3k7Nks6JV4PCV-28oK2teWcNa9TmiyH6pPrQ-lKOYP51xFHMF8lsQbsE7J3FMUSqYb_dWhp5GS_a_bsuifxkomR8Ztdo5rPPVy7_ZOlRba3CrwoVAM4S5mzYviv6RnCz5KsNMKKs9gStxInly6ILIVlP0aY8wOQC8lpRQ3GMzpw90hqt5hJDHLQNZA1-LANI2kxX7-EnaAHeg541A5wpBVZVhQi8MENrfpzJxtdDbRutuPm5CMjSBdUBLci7DjZCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حکم اعدام مهنام نواب صفوی، از معترضین دی ماه صادر شد
فرصت ۲۰ روزه برای اعتراض به حکم داده شده و اگه اعتراض مورد تایید قاضی قرار نگیره، حکم اجرا میشه
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/funhiphop/78648" target="_blank">📅 15:18 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78647">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">5 گلزن برتر جام جهانی تا اینجای کار  @FunHipHop | Farid</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/78647" target="_blank">📅 14:38 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78646">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gh6p-O65Cs7iLoFExKp7_gydr8CQdel3sV_PO9S-bDNGumEbd-YHrRBrzfKBLzxpn0k7iWQRrzONaGEt1Din-8AWKdT-hpDZicQK2Gd8X26_d5HIxqLtoUxg1xWahAJI7Q_GRVUcVPwVyNGCnBtWU6GedkIspK0x3g7ft-cTGuHlRzd_tWjzWgqIlh0-znLrH3QP79Xyf0NzB4iOtv2imvVZ983DsA_6CGkU0m3V8HU8E_RRIpvCG2JG00ewhbH08jErJE5HiTG-wpSyUAyfnFikQ3HNkK103HAm0-BgJRTwGMbir945XUdgGJsLB82bzIf_qq6ml3hL513PcifYvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">5 گلزن برتر جام جهانی تا اینجای کار
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/funhiphop/78646" target="_blank">📅 14:32 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78645">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dOBa5X4BqQRqLan8oyZ3yaUv7UM_4HwDxT_YqCOCMUsXsI3XI_1z93Wff5uJkBdXbEJYMChRfDkbWFEOYDEdXSvZ9eay24UFTVS4Ge3GlBmcs5AeC2HSjCS1eRTldOyo45cDs4oj85UCQDoV1lkSaPbdAshqowjtJpfYk2z73FkJA1JSHyWLALUb9jET3Kwa0amcYjbQFP6b0U23XFt3NUeuNsD5DFbeYXAiWCprcXykBrDdM0h4BqBa08P6qB9cUtOTo7sn_tMjPRpOs2cgIpRmvv2WgCVLoMKaiACm9IlFvdVKYpl5MqifsKwA-ILd1led8xaldpwqIB8_dSyxFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قیمت بازی GTA VI مشخص شد:
نسخه Standard به قیمت 80 دلار یعنی تقریبا 12 میلیون و 800 هزارتومان
نسخه Ultimate Edition به قیمت 100 دلار یعنی تقریبا 16 میلیون تومان
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/funhiphop/78645" target="_blank">📅 14:07 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78644">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">قبض تلفن تماسا تتلو رو کی میده یعنی
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/78644" target="_blank">📅 13:59 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78643">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">وزیر خارجه پاکستان: برای عبور از تنگه هرمز، هزینه یا عوارض یا اجازه یا کسب مجوز وجود ندارد.
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/funhiphop/78643" target="_blank">📅 13:52 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78642">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eecASTpwFRAiaFWgNkHs5oSnIkpnTwwx4wakMenESqy8jL98UZqZT0Wu_FyGYx9TwgNdtq7JlRE9cVOO2ydf_dy-PWm44skk0b-mMehblo2q8Y3Cg1Ms3bcr5TjZfmKV0B6jLit2VIulEKpxghPKeP0fl3WLiQpgu0aDXyzZA2Ixsk4988afkwSLUZy1G1BR-1ZvyIcvmYyVUHCQ6XVGnYfIuTebbgNbTyVhBSpMrevh2EVQVseTCXa3rHfg1Jrspz0tBP4XP3uklR1_YjoAeOS1L88NriTGIFRKyVYauQhMFfOJBql4hV2SNiB8MdzJGBcKUij9msotjvXq7jtOIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تو مغز پدر مادر شماره 2 پاناما چی گذشته که اسمشو این گذاشتن
@Funhiphop
| Jenayi</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/funhiphop/78642" target="_blank">📅 12:18 · 03 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
