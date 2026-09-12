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
<img src="https://cdn4.telesco.pe/file/jA0K8baJmMmMnPAfSP4H0MiMvLrasszTqdjZK5FYaHDGOOxHBYPwS88mWIkKOR9-cK3bJJJoMstjYhcz7s0r0l9PkuF6EuHXNwB9KXAp1SalohM8fj_Q8bSCu1KQaSxvKD2R_PeoluWq78D8rLBkU0T6m8AGo10pPdD6zoI-EgaqSA_LtMREWJpPr88mvxUaMnj6nN_OBZoBx8oUMr9OZeeubnPKo0lBXrHfERNrh_SMEVxNrMfXu9gvJfwqi8vD06YLx-piszm5F5hyZYy2bUqBMR7lKf8x9NMjYdKZxc3RYrYAld704pLKb4BjEgaOt1HC62tm3tG4U_o8HYK0qw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 110K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-21 17:45:14</div>
<hr>

<div class="tg-post" id="msg-71528">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af4b43f033.mp4?token=usW4mDcrWQvbNLvtbFC4O7HJPK8f_8Zez61nj9SOu86gBSqxaXIuAqzNVYDMQrN6QNu6A_osDqjP2Yz8_f-S0llKC-asV0KZJiF3PPRDFGUVMiH3E7W97xL1V_2vszV8vutiSDiB5ykT6aIhCNst0K2M10yzv73YwlTNVjZDbyGAENhw6bop6PMdtEqJjf9Utw3m0Uu5hd7L8ReZupTW6N8_ljL3Uz43X1UR5JtY2quADL8hVR1MgLa4v2tsFCYpOkio03PZCyz9dMTm4JNRmNKrK1pyVeSWz722KoCcxffDsp8-ixDWgXSdQAYmnWbJIxOw4t5oEJ3APGRA9wq1-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af4b43f033.mp4?token=usW4mDcrWQvbNLvtbFC4O7HJPK8f_8Zez61nj9SOu86gBSqxaXIuAqzNVYDMQrN6QNu6A_osDqjP2Yz8_f-S0llKC-asV0KZJiF3PPRDFGUVMiH3E7W97xL1V_2vszV8vutiSDiB5ykT6aIhCNst0K2M10yzv73YwlTNVjZDbyGAENhw6bop6PMdtEqJjf9Utw3m0Uu5hd7L8ReZupTW6N8_ljL3Uz43X1UR5JtY2quADL8hVR1MgLa4v2tsFCYpOkio03PZCyz9dMTm4JNRmNKrK1pyVeSWz722KoCcxffDsp8-ixDWgXSdQAYmnWbJIxOw4t5oEJ3APGRA9wq1-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
شعار «مرگ بر روحانی» در تجمع شبانه عرزشی‌ها
:
@News_Hut</div>
<div class="tg-footer">👁️ 1.87K · <a href="https://t.me/news_hut/71528" target="_blank">📅 17:32 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71527">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e506b56e1e.mp4?token=qPahvCUSqjpooTMom5B-FdEFqW-2gevF5hGwt5i9auiM_447iQd562pDuIMq53LIS4oYCCL42IHbwg1zLxkn4PxBp95vPP0_xkdNmrX9pQToAQ9hqNAWZO96WnCdLktANXuqkO8QD6pUua7dWrnUbhLMxddogJ8FkFhWN9kt24alAw_tZQRTW2KvgdvLfX3g4hlvG99Mss0o1sEEipbHsCAO-Ot3KJczq0MbtpNBcyajlth1eE26MwQ39za6aDzvWXZPGsFY0RqM6Gi4xFdOVVyO73oFnneP0LfBPCRuR0_zqBPMr0qns9CJPB6Ccr4FlA_uQaKo1sgE3ELTzZ3IZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e506b56e1e.mp4?token=qPahvCUSqjpooTMom5B-FdEFqW-2gevF5hGwt5i9auiM_447iQd562pDuIMq53LIS4oYCCL42IHbwg1zLxkn4PxBp95vPP0_xkdNmrX9pQToAQ9hqNAWZO96WnCdLktANXuqkO8QD6pUua7dWrnUbhLMxddogJ8FkFhWN9kt24alAw_tZQRTW2KvgdvLfX3g4hlvG99Mss0o1sEEipbHsCAO-Ot3KJczq0MbtpNBcyajlth1eE26MwQ39za6aDzvWXZPGsFY0RqM6Gi4xFdOVVyO73oFnneP0LfBPCRuR0_zqBPMr0qns9CJPB6Ccr4FlA_uQaKo1sgE3ELTzZ3IZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇹🇷
یک شهروند ایرانی با انتشار ویدیویی اعلام کرد ترکیه مرزش رو به روی ایرانیا بسته و اجازه عبور و مرور رو نمیده.
@News_Hut</div>
<div class="tg-footer">👁️ 4.97K · <a href="https://t.me/news_hut/71527" target="_blank">📅 17:04 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71526">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/89e47bf456.mp4?token=tDdP_Ekrkqw_9ucqT2oYNN_TjH_XExS5v-Pj_FPvj9ghYm76aBUddVk40SvnWLZ0WnlUMyyWgfPhU7l7Z9DxmdoUjGXT6lVi1WbOC6TK1A8IT0a543GAunce2CW-74aPD8mZfkW8f7H7U3sSeBo6p-pu7rPo1322eVq5bwwLFkKNAh16ln32m4jOz-GxPmYvqTzz1yQXDjNG_qMzMgvePFkyOldu4D4NVZXW5ulciySVTIcShpaEo5fMqVgZNLmKwoSEWmkEaXInuL3A27PfIOxWGKJpu1H7GP5hvIX3dIUrtAInDEYd_Y1tl_7XrzRumfbWNUAJTuVvGyxLrG1T1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/89e47bf456.mp4?token=tDdP_Ekrkqw_9ucqT2oYNN_TjH_XExS5v-Pj_FPvj9ghYm76aBUddVk40SvnWLZ0WnlUMyyWgfPhU7l7Z9DxmdoUjGXT6lVi1WbOC6TK1A8IT0a543GAunce2CW-74aPD8mZfkW8f7H7U3sSeBo6p-pu7rPo1322eVq5bwwLFkKNAh16ln32m4jOz-GxPmYvqTzz1yQXDjNG_qMzMgvePFkyOldu4D4NVZXW5ulciySVTIcShpaEo5fMqVgZNLmKwoSEWmkEaXInuL3A27PfIOxWGKJpu1H7GP5hvIX3dIUrtAInDEYd_Y1tl_7XrzRumfbWNUAJTuVvGyxLrG1T1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
این ویدیو از عشق و ابراز علاقه زیبای یه پیرمرد و پیرزن ایرانی توی پارک خیلی وایرال شده:
@News_Hut</div>
<div class="tg-footer">👁️ 7.02K · <a href="https://t.me/news_hut/71526" target="_blank">📅 16:31 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71525">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/401752fb0e.mp4?token=iUGpLS3Znua01q6C3F759PaNJi2j22scl3AXPURS9GuMp5AAAovk1dKtJpbdR-Qi805jg8s_Aoi3OO-vvvekd3JyL_rMDV28KcVuaVjydNM6CAfBCopA4SnzOaG8H-XPZ_D7iSUCIIYeipzl0PLg6fOkcDduX9BqO1frLXBBD40qyyQVrdKSIwzOI_NYP6mUzamS8bGGVs70Nvc13Wv0_2uLzEMkELPLMVbFIXa84ZjZ4WDT_Ph8lszAb4QaLacAKpFgo3I8XgOWjRIRyBu-OUbS7gqI8W3ISxy7v7xZdfAlpJAc6u7Sg_M2hmOXL4HD7JvZBzAadpcl9tborzb4pg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/401752fb0e.mp4?token=iUGpLS3Znua01q6C3F759PaNJi2j22scl3AXPURS9GuMp5AAAovk1dKtJpbdR-Qi805jg8s_Aoi3OO-vvvekd3JyL_rMDV28KcVuaVjydNM6CAfBCopA4SnzOaG8H-XPZ_D7iSUCIIYeipzl0PLg6fOkcDduX9BqO1frLXBBD40qyyQVrdKSIwzOI_NYP6mUzamS8bGGVs70Nvc13Wv0_2uLzEMkELPLMVbFIXa84ZjZ4WDT_Ph8lszAb4QaLacAKpFgo3I8XgOWjRIRyBu-OUbS7gqI8W3ISxy7v7xZdfAlpJAc6u7Sg_M2hmOXL4HD7JvZBzAadpcl9tborzb4pg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
یه دختر حامی حکومت:
چرا پزشکیان ۱۷ شهریور که تولد مجتبی خامنه‌ای هست بنزین رو گرون کرد؟ چرا روز تولد خودش گرون نکرد؟
میخواین همه تقصیرات رو بندازین گردن امامِ ما یعنی مجتبی؟ کور خوندین!
ما دیگه فریب بازی‌هاتون رو نمی‌خوریم که میخواین علیه رهبرمون کودتا کنین.
@News_Hut</div>
<div class="tg-footer">👁️ 8.77K · <a href="https://t.me/news_hut/71525" target="_blank">📅 16:03 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71523">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e93a51beb4.mp4?token=Sx7PcaJ33Nd365hrTDB7TJcUtI8BBCbKAXYw19j4Rh9U_utGYSS4aeK5vmZYzGlpDHFLJwQ2-CWsXaaspAoozKtmOGpueru9E5GIitPnHmAKyeAQU5-nwARI-oxeoQOukIzKkrg7cPwgo5lw98a65xCd_o-vW6TeXgS_mxmN8q4o8IOa6XNTf2cpuxgITSY2IfXMfq_tIqhnGJmXosUFLRpcmbEqGkV1HQpr6zbjBj6m7H0BKIfLcRB9MlcloL-8BUDFtvH80HrKHcmKAga9CysVEw9sh8X46pU5fI3mhmBxfM8etTa1W8Zl1nBc_9uekLVMUwxuH-8NJNYuMckiHwUTmtx9wTHrTXfmwoVM-NkAhi2hS1c-b74w_bwjzi1NuGBmeaFtcykvJlD29UHCQmQJ3h4bK09lb0Q1eB5DDbZDL6IN9kn4qZ7-vSxuQSwc75yYcdUxDjNASpZDWsdkgaOtVJkVqiztu9NbEyjo59uqfjsdjAj1hKO2_NsuchrU3Y_m-XfvpQxGp7NQuppAZnpO-VeySygRMEIwfrPq_M8URCEo3NU85zY2Sk8BHKkOrJHBDoCZM63EBOuFxTmgl-xgfOWG2zx0DdSqE3G-DEwu55q_opJHmKsmD06mCAVMYnVQK8EtdvX69CoO55B33IGtntr-TIRQDtpFcr4kgMM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e93a51beb4.mp4?token=Sx7PcaJ33Nd365hrTDB7TJcUtI8BBCbKAXYw19j4Rh9U_utGYSS4aeK5vmZYzGlpDHFLJwQ2-CWsXaaspAoozKtmOGpueru9E5GIitPnHmAKyeAQU5-nwARI-oxeoQOukIzKkrg7cPwgo5lw98a65xCd_o-vW6TeXgS_mxmN8q4o8IOa6XNTf2cpuxgITSY2IfXMfq_tIqhnGJmXosUFLRpcmbEqGkV1HQpr6zbjBj6m7H0BKIfLcRB9MlcloL-8BUDFtvH80HrKHcmKAga9CysVEw9sh8X46pU5fI3mhmBxfM8etTa1W8Zl1nBc_9uekLVMUwxuH-8NJNYuMckiHwUTmtx9wTHrTXfmwoVM-NkAhi2hS1c-b74w_bwjzi1NuGBmeaFtcykvJlD29UHCQmQJ3h4bK09lb0Q1eB5DDbZDL6IN9kn4qZ7-vSxuQSwc75yYcdUxDjNASpZDWsdkgaOtVJkVqiztu9NbEyjo59uqfjsdjAj1hKO2_NsuchrU3Y_m-XfvpQxGp7NQuppAZnpO-VeySygRMEIwfrPq_M8URCEo3NU85zY2Sk8BHKkOrJHBDoCZM63EBOuFxTmgl-xgfOWG2zx0DdSqE3G-DEwu55q_opJHmKsmD06mCAVMYnVQK8EtdvX69CoO55B33IGtntr-TIRQDtpFcr4kgMM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت
ترامپ درباره ایران:
«ما کنترل تنگه هرمز را به دست گرفتیم. تمام مین‌ها را پاکسازی کردیم.
من گفتم: «خب، پس چرا آنها مین‌روب‌های ما را هدف قرار نمی‌دهند؟»
گفتند: «قربان، این مین‌روب‌ها زیر آب هستند. آنها همیشه در زیر آب فعالیت می‌کنند.»
گفتم: «چرا این کار را می‌کنید؟»
گفتند: «خب، به‌طور کلی، وقتی مین وجود دارد، بیرون از آن منطقه هم خصومت و درگیری زیادی وجود دارد.»
یعنی اگر در یک آبراه مین وجود داشته باشد، معمولاً افرادی هم هستند که به سمت شما تیراندازی می‌کنند. بنابراین اگر زیر آب باشید، آنها نمی‌دانند شما آنجا هستید.
حالا دیگر هیچ مینی آنجا نیست، هیچ چیز دیگری هم نیست. و اگر ببینیم آنها [دوباره مین‌گذاری می‌کنند/اقدام به این کار می‌کنند]، آن‌وقت می‌بینید چه اتفاقی می‌افتد.»
@News_Hut</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/news_hut/71523" target="_blank">📅 15:21 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71522">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ffb4e73a23.mp4?token=O_-rAhY26j4zX4JpW2icL67x8tZ9rKtKB0NpI-Dltpqpc0cpD-VNAds2yBkYgP4PZmSy59CM2hYmUIOSc_5jeJDY5aV4SLLFQ2OfLQzOdWgflJhyryaYeLPMavc7ZGy1MJazIxlzGzM3StXuH_hRg-XZpLFkG4j6WLZ5kkG99iDtENYqIwj1yDtU2RgNzNz83eJ859JMAIhuu8Uu2Nm7KTV6u9yY4S8MNWRMYm_Hsr56zLFtya4mE2ngcNzgWndWqRrpZpo7osO9Sq5wh6bueQrKa6bnoB2osyJ65PyMNAaqO3jkJlWmr7RjjiKYeAd5aKrnmY9yReNjPQsx0qmWZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ffb4e73a23.mp4?token=O_-rAhY26j4zX4JpW2icL67x8tZ9rKtKB0NpI-Dltpqpc0cpD-VNAds2yBkYgP4PZmSy59CM2hYmUIOSc_5jeJDY5aV4SLLFQ2OfLQzOdWgflJhyryaYeLPMavc7ZGy1MJazIxlzGzM3StXuH_hRg-XZpLFkG4j6WLZ5kkG99iDtENYqIwj1yDtU2RgNzNz83eJ859JMAIhuu8Uu2Nm7KTV6u9yY4S8MNWRMYm_Hsr56zLFtya4mE2ngcNzgWndWqRrpZpo7osO9Sq5wh6bueQrKa6bnoB2osyJ65PyMNAaqO3jkJlWmr7RjjiKYeAd5aKrnmY9yReNjPQsx0qmWZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
هادی چوپان :
هانی رامبد از پشت بهم خنجر زد.
گفت پشت جمهوری اسلامی نباید باشی ولی من قبول نکردم و اونم همکاریشو کامل باهام قطع کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/news_hut/71522" target="_blank">📅 15:03 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71521">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jh77uiDscwS5cFtxaX2vW6VHB4BwhI3-BY_7Pcnv4MHZO8HO3YKOp8hj-RQblogz3TjPXUe4GO9LG36H2W_n1x_LUqULZmBwVkiJVuYEHDM6FCFw82xtjt5CSiRbZKHuLFxxcTLoznjdrMHRtgtaFtLPgPdp0R9_Tr9qkuPQJg2HWAih2EIhrnmA-RurdL6tVxz3M2R1LVGfNNDjujKanHIhKo5u5bcSTCpYowa5Om8K6DrgF24d9ZrW8c9_wbRMT_r8VRldq66MSzXj3aA8iZWMDaqkSZF5sqpXLRQz6m7fLJGWhjPy08QILLmJTzLBOJdIn4Ntktimx87AwltJYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
🇦🇪
پزشکیان در جریان حضور در اجلاس سران بریکس با محمد بن زاید آل نهیان رئیس امارات متحده عربی دیدار کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/news_hut/71521" target="_blank">📅 14:30 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71520">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64984e2da7.mp4?token=nhn5xTtLIk7S8wQqVakpL0gX1Aggg_STFJUuij1h8toRkTvHep_AB_kGZd6Z_9cI2UtAi-m2kfFxTmjuicyPZhbgtdO7qeYi0QUOicJ_LPFe959c6IR9oMV1_sf1gnf3jsyCNBz9J3kBUMrRkdlV3dNn5szbtXAadRqEiildySJNTeNKWTYNcH9eozoREmpZg2vhtBjqP-rHs1rPVQGHnThmfyKWlqIVfAyFcWM_8sF9cRdGdUEFfPnk5hqA4hF3M2gzpAsIpNznIgwq1xRavgFGHQnuLlfwiGnGOkqzuY2iUdDZoX8AX1oKOs5vM47jbJltqQP6NX-AA-9tHjB_vogp9fHqruN92u6IGJsy-0ZSW1Ctb2LX1jhuIhiQFnqlNPjn2TRGvC_Q0gAxKyPo3jEYcCMxqt5zjtQ2BKg8tjvl0Rcs5vzrgNuVQ1d2OA6hR6Pd4SNLLqUSODhzAfKsEE9ulSWisrqGudvFYIUdMSpvdfv4CLXdrv_pSfs-C_P0aHrumXF_JuKdZrRk1RPr_Dmp7nkfNYLUX1nKbvbME0cbn7xr9eaBNKJntsuVjcEXP1OpJusbZj2q7bKHFTIr58bVEqqERhR8-PkqarbywjPB3fQVUIRJtuiaAVfIpsItjLAqXfnB_mKlWBTXQpwRHz6qOTWvvPrhyy8ViiLMMKk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64984e2da7.mp4?token=nhn5xTtLIk7S8wQqVakpL0gX1Aggg_STFJUuij1h8toRkTvHep_AB_kGZd6Z_9cI2UtAi-m2kfFxTmjuicyPZhbgtdO7qeYi0QUOicJ_LPFe959c6IR9oMV1_sf1gnf3jsyCNBz9J3kBUMrRkdlV3dNn5szbtXAadRqEiildySJNTeNKWTYNcH9eozoREmpZg2vhtBjqP-rHs1rPVQGHnThmfyKWlqIVfAyFcWM_8sF9cRdGdUEFfPnk5hqA4hF3M2gzpAsIpNznIgwq1xRavgFGHQnuLlfwiGnGOkqzuY2iUdDZoX8AX1oKOs5vM47jbJltqQP6NX-AA-9tHjB_vogp9fHqruN92u6IGJsy-0ZSW1Ctb2LX1jhuIhiQFnqlNPjn2TRGvC_Q0gAxKyPo3jEYcCMxqt5zjtQ2BKg8tjvl0Rcs5vzrgNuVQ1d2OA6hR6Pd4SNLLqUSODhzAfKsEE9ulSWisrqGudvFYIUdMSpvdfv4CLXdrv_pSfs-C_P0aHrumXF_JuKdZrRk1RPr_Dmp7nkfNYLUX1nKbvbME0cbn7xr9eaBNKJntsuVjcEXP1OpJusbZj2q7bKHFTIr58bVEqqERhR8-PkqarbywjPB3fQVUIRJtuiaAVfIpsItjLAqXfnB_mKlWBTXQpwRHz6qOTWvvPrhyy8ViiLMMKk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
🇺🇸
ترامپ:
ببینید، ما کار فوق‌العاده‌ای انجام دادیم. می‌دانید، ما آنجا را تحت کنترل گرفتیم. ما واقعاً با اقتدار کامل بر «تنگه هرمز» مسلط شدیم و هیچ‌کس متوجه این ماجرا نشد.
ما کنترل بسیار قدرتمندی بر آن داشتیم.
ما یک محاصره دریایی اعمال کردیم که واقعاً بی‌نظیر بود.
ما تعداد زیادی از شناورها را بیرون می‌کشیم؛ به‌طور میانگین روزی ۲۵ شناور را خارج می‌کنیم که بیشترشان در شب انجام می‌شود.
اما به‌طور متوسط، هر روز حدود ۲۵ شناور را از کار می‌اندازیم.
@News_Hut</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/news_hut/71520" target="_blank">📅 13:53 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71519">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🎙
خبرنگار:
آقای رئیس‌جمهور، جنگ در ایران چه زمانی پایان می‌یابد؟
🇺🇸
ترامپ:
فکر می‌کنم خیلی زود. گمان می‌کنم احتمالاً درست پس از پایان دوره [فعلی انتخابات] باشد. آن‌ها سعی دارند تا جای ممکن مقاومت کنند تا وضعیت انتخابات را پیچیده سازند. اما فکر می‌کنم مردم متوجه ماجرا هستند، چرا که ایران نمی‌تواند سلاح هسته‌ای داشته باشد. موضوع بسیار ساده‌ای است؛ مسئله خیلی ساده‌ای است. ایران نباید چنین سلاحی داشته باشد. آن‌ها تنها دو هفته با دستیابی به سلاح هسته‌ای فاصله داشتند.
اگر این کار را نکرده بودند [و جلوی آن‌ها گرفته نمی‌شد]، اسرائیل را نابود می‌کردند، خاورمیانه را به آتش می‌کشیدند و به برخی شهرهای اروپا — و حتی فراتر از شهرها — حمله می‌کردند. و احتمالاً پیش از آنکه ما بتوانیم آتش را خاموش کنیم، به خود ما هم حمله می‌کردند. اما آن‌ها نباید سلاح هسته‌ای داشته باشند. با این حال، می‌گویم که [این اتفاق] به‌زودی رخ خواهد داد و قیمت نفت به‌شدت سقوط خواهد کرد. وقتی آن اتفاق بیفتد، قیمت نفت به‌شدت پایین خواهد آمد.
@News_Hut</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/news_hut/71519" target="_blank">📅 13:48 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71518">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">⏺
🇮🇷
قرارگاه قدس نیروی زمینی سپاه:
درپی انهدام یک تیم تروریستی حرفه‌ای که قصد اجرای عملیات ترور در سراوان را داشت، ۴ نفر از این تروریست‌ها به هلاکت رسیدند؛ همچنین تعدادی سلاح و مقادیری مهمات و مواد انفجاری از مخفیگاه این تیم کشف گردید.
در این عملیات که تا پیش از ظهر امروز ادامه داشت ۳ نفر از پاسداران گمنام امام زمان(عج) نیز به شهادت رسیدند.
@News_Hut</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/news_hut/71518" target="_blank">📅 13:43 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71517">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea8136d3aa.mp4?token=HAQbzVITYPQPs90yV0PbL9NHxxZebMpzQxzZIwikWKa-lzKwvO_EpJnatr9K8_ptDgyp3oXLNGukxj72RlqvbsgjxLingXQOFAqDc-18JxdlXqHgvqhJvyf7eaEqIh9w-BWh5xzMawv1E6Wep4qrZZWlQZOsqNERuOtJN3InJuMBu6HOXYezkUAHVKkErcR_GnfGsg6MSBHxZtC-ZsZFHqoR0skZhinGWzyrDV687CzTxwXWR9Pr_rQ2cf1rgHi3wfIhyOHXyikpb98qEBuLGcfL28jkRn31NF3nWidALH5LtWt3cPdohhkZE8W5A3JxJFrMbZcxvy15KPPEJTVj_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea8136d3aa.mp4?token=HAQbzVITYPQPs90yV0PbL9NHxxZebMpzQxzZIwikWKa-lzKwvO_EpJnatr9K8_ptDgyp3oXLNGukxj72RlqvbsgjxLingXQOFAqDc-18JxdlXqHgvqhJvyf7eaEqIh9w-BWh5xzMawv1E6Wep4qrZZWlQZOsqNERuOtJN3InJuMBu6HOXYezkUAHVKkErcR_GnfGsg6MSBHxZtC-ZsZFHqoR0skZhinGWzyrDV687CzTxwXWR9Pr_rQ2cf1rgHi3wfIhyOHXyikpb98qEBuLGcfL28jkRn31NF3nWidALH5LtWt3cPdohhkZE8W5A3JxJFrMbZcxvy15KPPEJTVj_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خبرنگار:
آیا ایران مسئول حمله به خط لوله «شرق-غرب» است؟
و به نظر شما عربستان سعودی چه کاری می‌تواند انجام دهد؟
🇺🇸
ترامپ:
خب، فکر می‌کنم همین‌طور است. احتمالاً همین‌طور است.
آن‌ها در حال حاضر در وضعیت آماده‌باش و هوشیاری کامل هستند، اما فکر می‌کنم مسئول آن هستند.
آن‌ها مدتی است که کنترل آن را در دست دارند.
@News_Hut</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/news_hut/71517" target="_blank">📅 13:35 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71516">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9946b1f32a.mp4?token=KZcluJn6pHMRgV-77atGb8CBXA9ac9nZ_rE7iCL7ng0yPXKK5qEYisga6VWSqWYwN-LQOrF8BqGWoU4aZz8lzTs9GqGFJZ0LZjW9eGe5F1ywRZ09q3jru8XXC9WtneaRdDjop1s9NZY828GJTtoMa5h9d8DExs_vg7E993MGYe8H2yxCJBPj5zvzrQWR2aXLNmxsb9PeqxkvRS7fsgDUspxLZDcKTG651mmpMEWM83NTpYyWwNKwa2DGQ976Ejy_lZWjJNgz2JDaVVH6nLosiWa_xEkkp6w5qp28q0F_ZtCP3PI2Nhov8w79VHTiXVd_Y_EO2_sxAh0OTv4jfFE5RQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9946b1f32a.mp4?token=KZcluJn6pHMRgV-77atGb8CBXA9ac9nZ_rE7iCL7ng0yPXKK5qEYisga6VWSqWYwN-LQOrF8BqGWoU4aZz8lzTs9GqGFJZ0LZjW9eGe5F1ywRZ09q3jru8XXC9WtneaRdDjop1s9NZY828GJTtoMa5h9d8DExs_vg7E993MGYe8H2yxCJBPj5zvzrQWR2aXLNmxsb9PeqxkvRS7fsgDUspxLZDcKTG651mmpMEWM83NTpYyWwNKwa2DGQ976Ejy_lZWjJNgz2JDaVVH6nLosiWa_xEkkp6w5qp28q0F_ZtCP3PI2Nhov8w79VHTiXVd_Y_EO2_sxAh0OTv4jfFE5RQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇱
این رستوران توی تهرانه
نوشته : هیچی کتلت بی بی نمیشه:)))
@News_Hut</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/news_hut/71516" target="_blank">📅 13:17 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71515">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db0f6d97e2.mp4?token=AXUUeMxVX8FCeWpMGk6tMYaLwo-GrAfRf-U9et-w7Ozm1jBX-EUNvjCOtUCTwbu89YeMqIieW8CujlJ-yBfRbgbrc6rSq0oO5U6QuqYxw1WN396IgOlX7fDgQARFGv44GOb_1PkLFAOUaX8XZ_8vpd8jA7PizprmEF8BY2VL-5JJ-5sGggL-sPRcqzDzfQbrlxaPEB8TgWnVaPnQqS1TCjb3qk3duK_1BV5vjkvcyjDs7Jx0HxG0gt7CHIRDmxM2zEPmf93VZ2UkLG9IVrNHZk998krN2R_YJ-uOz8SwO-r078GDicZytugC8gsFCD1ChkCijp9bri3CYkiYsyy6LA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db0f6d97e2.mp4?token=AXUUeMxVX8FCeWpMGk6tMYaLwo-GrAfRf-U9et-w7Ozm1jBX-EUNvjCOtUCTwbu89YeMqIieW8CujlJ-yBfRbgbrc6rSq0oO5U6QuqYxw1WN396IgOlX7fDgQARFGv44GOb_1PkLFAOUaX8XZ_8vpd8jA7PizprmEF8BY2VL-5JJ-5sGggL-sPRcqzDzfQbrlxaPEB8TgWnVaPnQqS1TCjb3qk3duK_1BV5vjkvcyjDs7Jx0HxG0gt7CHIRDmxM2zEPmf93VZ2UkLG9IVrNHZk998krN2R_YJ-uOz8SwO-r078GDicZytugC8gsFCD1ChkCijp9bri3CYkiYsyy6LA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">〰️
🇺🇸
پست جدید دونالد ترامپ در تروث سوشال:
با این رئیس جمهور بازی نکنید، زیرا نتیجه خوبی نخواهد داشت.
@News_Hut</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/news_hut/71515" target="_blank">📅 12:51 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71514">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OsXG0WlGe3znJbIqCF_brXEoPVyBT2lzLNyxUd8gsnPJZ-cICprOAoYb7OJLvlyRKQQwQWDoIS90bf2z3vyUdKFI9_12q8FbYpFL4SV5Sha-N_Nd2yIzio5Y0WTE-wxmdfe9Qod5bGTG5iHotjVEV67DhPTx6x5euwub1XvY8RPGaXqGkbC0gjR0Ug1dHqzjYicNc1JCo20aF3_73H72cBJt_E2d8SxiKbaEyWmiaqnUZY4N9e2qZf09GOU-MIsgZRvlJUttZLAuXX1ut0xGL6e3_EXAggbPlCphKEjor4KwFN_AFmag-Vk1S5JnvhBpoBfd8WOe1bXS3vVoROriXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🙂
طبق پیش‌بینی‌ها، یکی از پربارش‌ترین پاییزها تو راهه.
@News_Hut</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/news_hut/71514" target="_blank">📅 12:44 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71513">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71513" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/news_hut/71513" target="_blank">📅 12:44 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71512">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SrDuqbNKLXhqc_lrNr75EoRL8zoozDnj40LIESNF1I3yOIGihs8UG_GOWHcmna531c8Dc7HZdc8xScUrJ15MthMrIRntZiVaOVhzV1RSdv-JC3k9aWKE1w5X6Bz33IDy5eCjITCxS7WlsjGhqRmoHNcBfnBhOw42Oe_ME8ltCc01MkNu7239lW1_MCWfpPdUF4buJyqlPM3amg5aqGK3diov9bpgnTJargefKsJv0Z4w5qoYNIOikCWIixFlhT4ROakV4cUbE-BbDy6TjJ2Fl3WOwK3vW95TujRHMDMZnzNl2UAIfOdTKVxxei8_suOrUOLn6mXF4PqOevaKOiWp4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
مچ‌های مهم امروز در سایت‌بین‌المللی
TrexBet
پیش ‌بینی کنید.
چلسی
🆚
لیدز یونایتد
فولام
🆚
لیورپول
اورتون
🆚
تاتنهام
ساندرلند
🆚
آرسنال
رایو وایکانو
🆚
رئال مادرید
میلان
🆚
لاتزیو
کالیاری
🆚
آتالانتا
پادربورن
🆚
دورتموند
🦖
🦖
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب برای بازی‌های امروز
🦖
واریز آسان و امن از طریق کارت به کارت و ارز های دیجیتال
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/news_hut/71512" target="_blank">📅 12:44 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71511">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🚨
🇮🇷
معاون امنیتی و انتظامی استاندار سیستان‌وبلوچستان: محل تجمع اعضای «گروهک‌های معاند و تروریستی» شناسایی شده و نیروهای امنیتی در یک عملیات غافلگیرانه به آن ضربه زده‌اند.
در گزارش‌های اولیه، نام جیش‌العدل/جیش‌الظلم به‌عنوان عامل درگیری امروز به کار برده شده که هنوز به صورت رسمی تایید نشده.
@News_Hut</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/news_hut/71511" target="_blank">📅 12:03 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71504">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5d436ab6a3.mp4?token=e_a2TXjA5kputxgMo6ZOy7UcC4Q4xP86MGYwvXDggqKvyzN80ps0knTWG6EVW9AZKPK4bZP8gZgCU-aVNRpssg_0vp1lkeKpZ0t8TY-nvuDDIdf0YwP07l538-1taw9ixd8KEJ0uwZ1bjdyVJizM-CaGiP2Jk-R2mzW4hmHs3OmVUQ7MsdnuUt0NSx0kINI_cV2wpN95oq7NDR9QtbwF1uK9zkFdyTYhX_gijG8F5fU-cMxKh4cbGOjbA1cO7G4kB5f8yz0rigSdi8SeyVw_2X9xEaD1PlKTJPq4976EaUP97FRfawTNfFFde0cJg0JlVHaT_zw-p5JgOh6hdSS6Nw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5d436ab6a3.mp4?token=e_a2TXjA5kputxgMo6ZOy7UcC4Q4xP86MGYwvXDggqKvyzN80ps0knTWG6EVW9AZKPK4bZP8gZgCU-aVNRpssg_0vp1lkeKpZ0t8TY-nvuDDIdf0YwP07l538-1taw9ixd8KEJ0uwZ1bjdyVJizM-CaGiP2Jk-R2mzW4hmHs3OmVUQ7MsdnuUt0NSx0kINI_cV2wpN95oq7NDR9QtbwF1uK9zkFdyTYhX_gijG8F5fU-cMxKh4cbGOjbA1cO7G4kB5f8yz0rigSdi8SeyVw_2X9xEaD1PlKTJPq4976EaUP97FRfawTNfFFde0cJg0JlVHaT_zw-p5JgOh6hdSS6Nw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
⭕️
🇮🇷
درگیری های بی سابقه نیروهای جمهوری اسلامی و نیروهای مسلح در سراوان سیستان بلوچستان
ویدیو ها مربوط به چند ساعت پیش
@News_Hut</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/news_hut/71504" target="_blank">📅 11:54 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71503">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🚨
🇮🇷
🇮🇶
رسانه عراقی نایا به نقل از یک منبع:  دستور فوری و جدیدی از سوی فرماندهی کل نیروهای مسلح به بصره ابلاغ شده است که بر اساس آن، گذرگاه مرزی شلمچه با ایران از همین لحظه و تا اطلاع ثانوی به‌طور کامل بسته می‌شود. این تصمیم شامل تردد مسافران و همچنین جابه‌جایی…</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/news_hut/71503" target="_blank">📅 11:32 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71498">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ba81cb21e1.mp4?token=gzXkjx259SgSV9tABWZdtKPB-MEOrmjFakibXeTIdysti-Ao9SiZh-lm6xoPVunsZmKhQ6TxcsUhD-iqynqOQ1L6Ue_O3u1gRMTCuzRl8B1WEQ2hOuOK07Sa-Xz3w--OouuF_wIj_EecOEwCPoNWzJcLxUdaq9Siy-667iSrEAfa6RIqOCxYYEo6zyLwt2Uu_rCnAwp7PmdSClsh00lZwSjUbKGcsa3CeFwaTvWWMc-SwTnoDRXFc3xhClGUhI_9B-pRfz92WcoVBMg13B7hWj9bOfJ3dT8BUN2agZMd6q3BqfAG7U1g96hWi3zISrocigKgJFoMYazkS7Ql7Jugwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ba81cb21e1.mp4?token=gzXkjx259SgSV9tABWZdtKPB-MEOrmjFakibXeTIdysti-Ao9SiZh-lm6xoPVunsZmKhQ6TxcsUhD-iqynqOQ1L6Ue_O3u1gRMTCuzRl8B1WEQ2hOuOK07Sa-Xz3w--OouuF_wIj_EecOEwCPoNWzJcLxUdaq9Siy-667iSrEAfa6RIqOCxYYEo6zyLwt2Uu_rCnAwp7PmdSClsh00lZwSjUbKGcsa3CeFwaTvWWMc-SwTnoDRXFc3xhClGUhI_9B-pRfz92WcoVBMg13B7hWj9bOfJ3dT8BUN2agZMd6q3BqfAG7U1g96hWi3zISrocigKgJFoMYazkS7Ql7Jugwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پسر تهرانی بعد از اینکه با دوس دخترش کات کرد، رفته تمام اکسای دختره رو جمع کرده، واسش دسته جمعی آهنگ خوندن تا قشنگ دختره رو بسوزونه و عقده هاش رو خالی کنه...
@News_Hut</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/news_hut/71498" target="_blank">📅 11:03 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71497">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0aa7081550.mp4?token=IA9zrriYkZQ2e5AQ0dvjWtlXeYVndl5jEZKqVlIHH2rCRhF5GWAFaIsNVO7vA5fmUsFJ_qaS9j14vx5wEj0wh11Z2OdNxUMxtnmwvFkfB9zhSJxWi-LzNCVS3xZWF7V05bJdUbq0WBPArd43I-NBfc3EwWxSwJ2lBIktEVJ3ZBRYb1kQAB_u2LKEFNKk9KKeuW16fEVYsOXiziuRjzAi-6W_OZqiqe07bB73gO3Xwrr9jsaM393mKMI_w7PfaZ9VlY9pQliknhy0sKdA4fJKGn0Cks5ASY-wwzmIxGE0ytu-jpivE5CHb-mH0Do_UrPIhTudnTZB3y4Fb9Tv7C_WFzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0aa7081550.mp4?token=IA9zrriYkZQ2e5AQ0dvjWtlXeYVndl5jEZKqVlIHH2rCRhF5GWAFaIsNVO7vA5fmUsFJ_qaS9j14vx5wEj0wh11Z2OdNxUMxtnmwvFkfB9zhSJxWi-LzNCVS3xZWF7V05bJdUbq0WBPArd43I-NBfc3EwWxSwJ2lBIktEVJ3ZBRYb1kQAB_u2LKEFNKk9KKeuW16fEVYsOXiziuRjzAi-6W_OZqiqe07bB73gO3Xwrr9jsaM393mKMI_w7PfaZ9VlY9pQliknhy0sKdA4fJKGn0Cks5ASY-wwzmIxGE0ytu-jpivE5CHb-mH0Do_UrPIhTudnTZB3y4Fb9Tv7C_WFzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇹🇷
یه گزارشگر تو شهر وان ترکیه طی یه گزارشِ خیابونی، نظر مردم این شهر رو درباره گردشگران ایرانی پرسیده که حسابی وایرال شده؛
@News_Hut</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/news_hut/71497" target="_blank">📅 10:31 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71495">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/faeed5163b.mp4?token=Uxnb51uYJVlRK1DRd4RMbLem4s8pGWkLCTG0jsqaLdkKbCHSqBpe-cyZrENcZRBalm6NBu9jFF1dEN70ikseXD-6nAWPPaaK1cyVPe_aPsVRtDT25wo5lfElr0wJBzjagXCWI1xPMza3B6GjOoFDKClmS0301aifk47oKE72mz1IE0WRVnHShIc-ldWrOJSuMyj--btBbsOXrIbqHXAFHhFu6i4fiS_K6oLUiNd-dY7RE-0CN41h8bORbGJeeilfB36Pkkugfcj3Aks6KRCkP8OdJb2UQf5hntKBriMZ9x6NiTEg5_-0s_BLW8spxTCQnQyUhduIL_q-kVcCSiWwZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/faeed5163b.mp4?token=Uxnb51uYJVlRK1DRd4RMbLem4s8pGWkLCTG0jsqaLdkKbCHSqBpe-cyZrENcZRBalm6NBu9jFF1dEN70ikseXD-6nAWPPaaK1cyVPe_aPsVRtDT25wo5lfElr0wJBzjagXCWI1xPMza3B6GjOoFDKClmS0301aifk47oKE72mz1IE0WRVnHShIc-ldWrOJSuMyj--btBbsOXrIbqHXAFHhFu6i4fiS_K6oLUiNd-dY7RE-0CN41h8bORbGJeeilfB36Pkkugfcj3Aks6KRCkP8OdJb2UQf5hntKBriMZ9x6NiTEg5_-0s_BLW8spxTCQnQyUhduIL_q-kVcCSiWwZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدئو وایرال شده و پشم ریزون از کنسرت تیلور سوییفت؛
خودتون ببینید به چه دلیل وایرال شده
😏
@News_Hut</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/71495" target="_blank">📅 10:01 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71494">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">‼️
خورلسوخ، رئیس‌جمهور ۵۸ ساله مغولستان، هنگام بازدید از یک یگان نظامی، حرکت پرس سینه را با وزنه ۱۰۰ کیلوگرمی در ۲۰ تکرار انجام داد.
او که پیش‌تر افسر ارتش بوده، نامش در لغت به معنای «تبر برنزی» است، باشگاه هارلی-دیویدسون مغولستان را تأسیس کرده و در یک گروه موسیقی گیتار می‌نوازد؛ او همچنین جانشین «باتولگا» شده است که خود قهرمان جهان در رشته سامبو بود.
﻿
@News_Hut</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/71494" target="_blank">📅 09:31 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71493">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a695c5e874.mp4?token=oXLinVcZbyZVgwtMiP55Okrtg0cEnUvyikaDz0lM1HdCbIUpgZZc2Zw1vJIsrsDyMyyVAtTJl8LoIrGnFubAPX5jCRdgZO7Eya5eoGKbD5nbYPOGqVaCEC2Wm19mn_xERVoMAvB32f7KuKvrN3ens4INCA1VeZ5vip6x9tkMTdDvG6vf7LHJUKV_OvaiQgeGha89wAwZka4dC1r56--JsHuuANJELHK7BV5C1sPqdWADdegBUXTKyHKVGvb62pc_37X3Gj--Y3CShO16Yl9IpALUBLs7uN2Z_pC2UJjhggF7zAZ16CjEFJiYNGw0MrXTT-jX_EBIVGZzY0AqJ_V8Ug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a695c5e874.mp4?token=oXLinVcZbyZVgwtMiP55Okrtg0cEnUvyikaDz0lM1HdCbIUpgZZc2Zw1vJIsrsDyMyyVAtTJl8LoIrGnFubAPX5jCRdgZO7Eya5eoGKbD5nbYPOGqVaCEC2Wm19mn_xERVoMAvB32f7KuKvrN3ens4INCA1VeZ5vip6x9tkMTdDvG6vf7LHJUKV_OvaiQgeGha89wAwZka4dC1r56--JsHuuANJELHK7BV5C1sPqdWADdegBUXTKyHKVGvb62pc_37X3Gj--Y3CShO16Yl9IpALUBLs7uN2Z_pC2UJjhggF7zAZ16CjEFJiYNGw0MrXTT-jX_EBIVGZzY0AqJ_V8Ug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
حسن روحانی خطاب به ارزشی ها : انتقام خامنه‌ای رو امام زمان که ظهور کنه میگیره
وسط مذاکره برای اینکه راهی پیدا کنیم که جنگ زورتر تموم شه یه عده میگن باید انتقام بگیریم خب چجوری ؟
@News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/71493" target="_blank">📅 09:02 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71492">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🚨
🇮🇷
🇮🇶
رسانه عراقی نایا به نقل از یک منبع:
دستور فوری و جدیدی از سوی فرماندهی کل نیروهای مسلح به بصره ابلاغ شده است که بر اساس آن، گذرگاه مرزی شلمچه با ایران از همین لحظه و تا اطلاع ثانوی به‌طور کامل بسته می‌شود.
این تصمیم شامل تردد مسافران و همچنین جابه‌جایی کالاها می‌گردد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/71492" target="_blank">📅 07:30 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71491">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🦖
فردا، شکار شروع میشه...
🦖
• هر روز در TrexBet، بین ۲ تا ۴ عکس چالشی منتشر می‌کنیم که داخل هرکدوم یک Promo Code یک‌دلاری مخفی شده!
🦖
دو زمان، دو کد، دو فرصت شکار 1 دلاری.  18:30 → اولین شکار  20:00 → شکار دوم
🦖
• شرایط دریافت جایزه
🦖
فردا ساعت‌ها رو یادت…</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/71491" target="_blank">📅 01:33 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71490">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZVMzAd4wSGjRJaHpN08c8w7YQnsN2-b0OGS8O2P0JxIOihaFls_y7MqXGzPqiHXtBx4F9QtC0t0qb2DBB0QMoHvztPDC9xNYuiKU1t7C_AUTZc0_0jXIOeFjCtJI0grCYyj_aRgTj9UsUodsOFVRnFQEu0FkRLP3Yli7HQbNvgaGRHhzYVpHxzRT58PMMuK1qp9TJFZ3HUz7iNGFYxo4VctbgZhkna3MpccbCGKgS0zljflIMX-GFqLsxQzEkUHxrcMy8HBSWeJ14My6Ar-g9fQ3J0yyIj0O57kaM7QhQoWASy479YOc10rTy_Ur6PqecovXRiTGrciWWuymrMDcVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
فردا، شکار شروع میشه...
🦖
• هر روز در
TrexBet
، بین
۲ تا ۴ عکس چالشی
منتشر می‌کنیم که داخل هرکدوم یک
Promo Code یک‌دلاری
مخفی شده!
🦖
دو زمان، دو کد، دو فرصت شکار 1 دلاری.
18:30 → اولین شکار
20:00 → شکار دوم
🦖
•
شرایط دریافت جایزه
🦖
فردا ساعت‌ها رو یادت نره...
ممکنه کدی که دنبالش هستی، فقط چند ثانیه با تو فاصله داشته باشه.
🦖
🦖
🦖
🦖
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/71490" target="_blank">📅 01:33 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71489">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/c20cfcda3a.mp4?token=AlxdUmjrrWsp-jZ8HF9VCf-I9fObj5MQa9O9EBSeYbo4Z8AxF_T18ahxLbuGZNaFf9I1ApGuzCOjFqMPIcWUbURUI3UpTqoQTkQ7GPnuGycnr6JXLX0p_NYP--3DjsLPTXZR9uHlMXGIpGq9Dc67SxOtdYMeUj4IIUxoys2zNlj64UpxWIf_QpIrDUQRQiVV-Q5xTlk3BoZgLGc9bfdPXFKf9302kTVhsVKhanFh3Lw_N-EILy5-tl6dYBlnIB2AVzFgu4tiZ0y2uF1QxIP0cxi3zYUJE8mJ8IpVFmYp4P8hs0TpL_ggHTAlwjpIXMKON0BoA3UFYFP2kZBsVzhXKA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c20cfcda3a.mp4?token=AlxdUmjrrWsp-jZ8HF9VCf-I9fObj5MQa9O9EBSeYbo4Z8AxF_T18ahxLbuGZNaFf9I1ApGuzCOjFqMPIcWUbURUI3UpTqoQTkQ7GPnuGycnr6JXLX0p_NYP--3DjsLPTXZR9uHlMXGIpGq9Dc67SxOtdYMeUj4IIUxoys2zNlj64UpxWIf_QpIrDUQRQiVV-Q5xTlk3BoZgLGc9bfdPXFKf9302kTVhsVKhanFh3Lw_N-EILy5-tl6dYBlnIB2AVzFgu4tiZ0y2uF1QxIP0cxi3zYUJE8mJ8IpVFmYp4P8hs0TpL_ggHTAlwjpIXMKON0BoA3UFYFP2kZBsVzhXKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇦
❌
🇾🇪
تصاویری از حملات هوایی نیروی هوایی سلطنتی عربستان سعودی به بندر «مخا» در جنوب غربی یمن که تحت کنترل انصارالله قرار دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/71489" target="_blank">📅 00:25 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71488">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uIDmMeufIKXNZ8R4XIz80JcYf863dpoC_D4fcDI8Lgw9Li3ldwM6GDJjELsjsXZYxu7SOSFCGT_mWNgKoOUOu8AqBK-nBHDHt9AKW0Guhv9UUV_oqKf98mHytoRg1zZoaoJLpAwWYJO6omdZICf6vHyuHgpeLM4mHG_BchmrAh1fVRcPcyyQfm4tn_vM0qiRIgbwWHS1RcFQ8OCkZ_2xgdSrdW6gHdGXZsz4xZywUb6zILa8KWdWu3sLq2AVHcm69f8xHzDHW3kX_QO50VweSILlMMqRE4Pj3Uo-XMWMQ9WfS7pKOu64clhENEppp2Xcxp1v4zMQqa-6RB3sfqIuTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
با پول ۲۰۷ در ایران تو کشورهای مختلف چه ماشینی میشه خرید؟
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/71488" target="_blank">📅 23:30 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71487">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2da32c63e2.mp4?token=TX-lY29P3dlWwOukpRW8BZZoEMM1Z_VEwqME_pWB6SGhYPrj1XAeoYdYO7-5LaGoA0ImoDWlPbpauH1X4V9ObRyMGDbA-6Ifwk-n6Kpr0hg0FzsL5IYRNG08PZYSAIYWmSVJq1G81DrmzmpWNFV3Mtk7DTYbhSK1A84Z4jW2gClahI6e4y7Mb515OizHYRNgXPn5cSiATXn97gXcRZXdWquPM24hadUe-zpA2BKilHfMkOoaekHMKOTUV86R7UQFEz8NuUt-yyQwv8h-bHhXaDxrGY_izOZhawi2rDGTpl-xO6d0gU4Q7Jp2xB74qPh_Zb_ESQsoXATgSCxhGLhctQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2da32c63e2.mp4?token=TX-lY29P3dlWwOukpRW8BZZoEMM1Z_VEwqME_pWB6SGhYPrj1XAeoYdYO7-5LaGoA0ImoDWlPbpauH1X4V9ObRyMGDbA-6Ifwk-n6Kpr0hg0FzsL5IYRNG08PZYSAIYWmSVJq1G81DrmzmpWNFV3Mtk7DTYbhSK1A84Z4jW2gClahI6e4y7Mb515OizHYRNgXPn5cSiATXn97gXcRZXdWquPM24hadUe-zpA2BKilHfMkOoaekHMKOTUV86R7UQFEz8NuUt-yyQwv8h-bHhXaDxrGY_izOZhawi2rDGTpl-xO6d0gU4Q7Jp2xB74qPh_Zb_ESQsoXATgSCxhGLhctQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇱🇧
🇱🇧
رسانه های نزدیک به حزب‌الله لبنان وویس هایی رو از اعضای حزب‌الله منتشر کردن که در زیر ارتفاعات علی‌الطاهر در تونل ها گیر افتاده بودن و درخواست کمک میکردن.
همه این افراد بعد از حملات ارتش اسرائیل و نابودی تاسیسات زیرزمینی کوه علی‌الطاهر کشته شدند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/71487" target="_blank">📅 23:05 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71486">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/68083de4e6.mp4?token=jdw2dpTGKLfatf7UBQOiarE1LHz7BngQG98-CikeYjwou0FcIkTbBEWQBmh9ySjDbtlSB8bH5QHnwHdtZLs_DGx-NiSNBsSqKIYtTBf27OPjz2I6UTLcLFLAmQIC0XaPxDPhRT1QtsM66NRO--jg39zShgqLRt_Ujj0VKq8UrSvOd0kJhOSST1Wg7sTNgAgCSROiQEMLM-jrbohWa5de14Vfd9HNW-t92Zw6HelVM_iMX8311YAVurdUtD551GK_J1Oh5WnhvHdvPZ1_-VwpDC0NW0dl5rc99WVU85lsxHZn2REVPD8JFotG7TUTAtkcIC4gtzZw2Y32tcKuzlNO3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/68083de4e6.mp4?token=jdw2dpTGKLfatf7UBQOiarE1LHz7BngQG98-CikeYjwou0FcIkTbBEWQBmh9ySjDbtlSB8bH5QHnwHdtZLs_DGx-NiSNBsSqKIYtTBf27OPjz2I6UTLcLFLAmQIC0XaPxDPhRT1QtsM66NRO--jg39zShgqLRt_Ujj0VKq8UrSvOd0kJhOSST1Wg7sTNgAgCSROiQEMLM-jrbohWa5de14Vfd9HNW-t92Zw6HelVM_iMX8311YAVurdUtD551GK_J1Oh5WnhvHdvPZ1_-VwpDC0NW0dl5rc99WVU85lsxHZn2REVPD8JFotG7TUTAtkcIC4gtzZw2Y32tcKuzlNO3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیو وایرال شده از یه دختره که پارتنرش یه ترنسه
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/71486" target="_blank">📅 22:15 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71485">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c1f7e0a7d.mp4?token=qvlaFC2XEZx1XEEdLOs1zuxjJaCtWNNvxkMq4aYy7q65hZwPBtM-2br85XflTHU3eMsWIKC8aNdin1ydx23zG41WVwcvtSZ4qYWln4zYkwgDFPz28wAKmPr8fFkPsBS5sbIfxGtL_Ws01pZO4t5vj6aEhK_lRzN9BSX4TEu8Gl72p0v49v-DeXeHEmSGCtuuFT_a_hlQRJFK8iR9b2ngCSi4-UhvKC8ZhFSOnB5vbYFEuDCNs6zolrWdRA5Tf89nbZXPjcUTOjjsWokS_ZIWwkCYFlQlOwA5IqXl32tyaa-J_OFxJzWlLjcbwDm_Poojn52IVa0f22lk1gJyky2J4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c1f7e0a7d.mp4?token=qvlaFC2XEZx1XEEdLOs1zuxjJaCtWNNvxkMq4aYy7q65hZwPBtM-2br85XflTHU3eMsWIKC8aNdin1ydx23zG41WVwcvtSZ4qYWln4zYkwgDFPz28wAKmPr8fFkPsBS5sbIfxGtL_Ws01pZO4t5vj6aEhK_lRzN9BSX4TEu8Gl72p0v49v-DeXeHEmSGCtuuFT_a_hlQRJFK8iR9b2ngCSi4-UhvKC8ZhFSOnB5vbYFEuDCNs6zolrWdRA5Tf89nbZXPjcUTOjjsWokS_ZIWwkCYFlQlOwA5IqXl32tyaa-J_OFxJzWlLjcbwDm_Poojn52IVa0f22lk1gJyky2J4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
حرفای زن دعوت شده به صداوسیما درباره ترامپ و نتانیاهو:
ما میخایم با پول حلقه های ازدواجمون طناب داری بر گردن نتانیاهو و ترامپ بندازیم
درست ۷ کیلو و ۲۰۰ گرم طلا به قاتل ترامپ جایزه میدیم
ما میخایم خون بر شمشیر پیروز بشه
از مامان های محترم تعهد گرفتیم و به مقدار توانشون طلا کمک کردن که به قاتل ترامپ بدیم
از ارزشمند ترین دارایی هامون می‌گذریم تا ترامپ کشته بشه
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/71485" target="_blank">📅 21:33 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71484">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🚨
🇮🇷
۱۰ دقیقه پیش، نیروی دریایی سپاه پاسداران یک موشک کروز ضدکشتی را از سیریک به سمت تنگه هرمز شلیک کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/71484" target="_blank">📅 20:58 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71483">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/dcbed492f8.mp4?token=Yc_edyAsiHaBz9dHEgOkRYADvRC01dO_S31xLHE7hxrPJUcWLmSn92Uqgxnap8aYhiSoqabNzWf4dt_GPdgJtDP9N5fv1lUlS67sEGeku70pbgfhTb_C8SMQvju0zHTTQ1ULh9PrmpjHti28yMIMHUk_8x1khzAvxzYuxBL07zqSX3FZaxrKmvn2fb_GHzlfR-sadQVJHM7D85yRKrxUWdov_yjBCckyAz0huwU9HVf0GqgZS5n7cLQSSLg6dARy69wqEBfg-1PAxzj4d4hbHFQxpY6k6sCKM7GFL6VSfoybvOREmgXrqtFVc_oiQRCZeIceZx_aVIWD4NAwo53NfA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/dcbed492f8.mp4?token=Yc_edyAsiHaBz9dHEgOkRYADvRC01dO_S31xLHE7hxrPJUcWLmSn92Uqgxnap8aYhiSoqabNzWf4dt_GPdgJtDP9N5fv1lUlS67sEGeku70pbgfhTb_C8SMQvju0zHTTQ1ULh9PrmpjHti28yMIMHUk_8x1khzAvxzYuxBL07zqSX3FZaxrKmvn2fb_GHzlfR-sadQVJHM7D85yRKrxUWdov_yjBCckyAz0huwU9HVf0GqgZS5n7cLQSSLg6dARy69wqEBfg-1PAxzj4d4hbHFQxpY6k6sCKM7GFL6VSfoybvOREmgXrqtFVc_oiQRCZeIceZx_aVIWD4NAwo53NfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇯🇵
آتشفشان ساکوراجیما در جزیره کیوشو ژاپن فوران کرد و خاکستر و مواد آتشفشانی را تا ارتفاع چند هزار فوتی به هوا فرستاد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/71483" target="_blank">📅 20:15 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71482">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d66564850.mp4?token=C0BRAkfKGtI2j4jK0kfricER-s2X5PziNKW3Yz_qKNvrvstnoATaUxGFlFN8R49pJ2Uqp_Q432ANUCQhCh28pa3gvKcdkNN0QA0cspiajGpAairEULSEOjgLlzKIja9BwgDkDcg59iQ1r917KnjbUh39S_BnGFMgpREuvyppCVXx9NOnfMyHh1H898ylLV1FsK5Bhp3mJLvl_XHKFiga4y0QGjCUjY80GbU6H7UNqek37AiukcirUDXHvTJvllo9O5f160m1d4s6gqVs34B2WBJjM91dNWknH1JUod31OWn4aqUgLmP6725FDSN3Fg5PG0-kz517aKIWFbOXYv5zDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d66564850.mp4?token=C0BRAkfKGtI2j4jK0kfricER-s2X5PziNKW3Yz_qKNvrvstnoATaUxGFlFN8R49pJ2Uqp_Q432ANUCQhCh28pa3gvKcdkNN0QA0cspiajGpAairEULSEOjgLlzKIja9BwgDkDcg59iQ1r917KnjbUh39S_BnGFMgpREuvyppCVXx9NOnfMyHh1H898ylLV1FsK5Bhp3mJLvl_XHKFiga4y0QGjCUjY80GbU6H7UNqek37AiukcirUDXHvTJvllo9O5f160m1d4s6gqVs34B2WBJjM91dNWknH1JUod31OWn4aqUgLmP6725FDSN3Fg5PG0-kz517aKIWFbOXYv5zDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
🇮🇷
صحبت های عجیب
پوریا بختیاری کارشناس اقتصادی در مصاحبه با علی ضیا درباره ابراهیم رئیسی:
نزدیکان رئیسی گفتند که حاج‌آقا خودش اقرار کرده که اقتصاد متوجه نمی‌شود.
بعد گفتیم خب، یعنی باید برای رئیس‌جمهور کلاس اقتصاد بگذاریم؟
گفتند نه، کلاس اقتصاد که نه؛ حاج‌آقا ذهنش می‌پرد و خسته می‌شود. بیاییم موشن‌گرافی بسازیم.
ما یک تیم انیمیشن آوردیم که برای رئیس‌جمهور مملکت کلیپ‌های اقتصادی درست کند. قانون هم گذاشته بودند که هر کدام از کلیپ‌ها بیشتر از سه دقیقه نشود، چون ذهن حاج‌آقا می‌پرد.
ببینید چقدر این موضوع تلخ و «دارک» است که برای رئیس‌جمهور مملکت و بالاترین قدرت اجرایی، بروی انیمیشن درست کنی تا بلکه اقتصاد را بفهمد!
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/71482" target="_blank">📅 19:37 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71481">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c90c5de5a1.mp4?token=PhD6V8B_UjbUKcC6yPu4Lx9gPWUCO1bWBnB0OMBK_HWsw34zCnqmgdAzdck-ebh9fQIrDi5Wq-sRzwten_U6wvXVcHmrBLgncrMLLnycfZT4dcTExy2xvv3XjB_OMW0mugNrN58I9_tSFBeCfDnfKmlzf0_rS0EYFe9KW8L1ot9IRQP8zTOB1VbkdfVzQW-PJpca6iBhUumpxkaLIkXIgjaK6FwpS4YmAfxA0jdB80ZhB0nVf6JFh7LDfrvfuer5SAOBoVtL_K3_eYTssvLnMh8KsxDkWjYV9paSZcVp0HFv2JD6l2zF-fht8PQE9qAmmjVTE2A-SMNjXlDVQdaKGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c90c5de5a1.mp4?token=PhD6V8B_UjbUKcC6yPu4Lx9gPWUCO1bWBnB0OMBK_HWsw34zCnqmgdAzdck-ebh9fQIrDi5Wq-sRzwten_U6wvXVcHmrBLgncrMLLnycfZT4dcTExy2xvv3XjB_OMW0mugNrN58I9_tSFBeCfDnfKmlzf0_rS0EYFe9KW8L1ot9IRQP8zTOB1VbkdfVzQW-PJpca6iBhUumpxkaLIkXIgjaK6FwpS4YmAfxA0jdB80ZhB0nVf6JFh7LDfrvfuer5SAOBoVtL_K3_eYTssvLnMh8KsxDkWjYV9paSZcVp0HFv2JD6l2zF-fht8PQE9qAmmjVTE2A-SMNjXlDVQdaKGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇦
❌
🇷🇺
اوکراین پایگاه دریایی نووروسیسک روسیه - بندر اصلی باقی مانده ناوگان دریای سیاه - را با حمله ترکیبی پهپاد و موشک در طول شب هدف قرار داد.
لیست خسارات تایید شده قابل توجه است
؛
ستاد کل ارتش می‌گوید سه کشتی جنگی (مین‌روب ژلزنیاکوف، ناوچه حامل کالیبر، دریاسالار اسن، و کشتی پهلوگیری پیوتر مورگونوف) به علاوه انبار سوخت مورد اصابت قرار گرفته‌اند.
اطلاعات و OSINT اوکراین، ناوچه دریاسالار ماکاروف، یک کشتی موشک‌انداز بویان-ام (غیرعملیاتی ارزیابی شده)، کشتی گشت‌زنی واسیلی بیکوف، چندین قایق موشک‌انداز و دو رادار دفاع هوایی در نزدیکی گلندژیک را اضافه می‌کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/71481" target="_blank">📅 19:25 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71480">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71480" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/71480" target="_blank">📅 19:25 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71479">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bfaB5A5bfV0lhZ7KS1lVZuSBTdoSHVb3PUzC_k8SX7lPFbFk4HUh1Zh1kein1XvDiO8BCtsLRE2VdpOY8cwxL8hoWUiTXlTZ0E_zX_Q_hV_IBlxOgZkG9nLdV-Po5tPmcXc2BVl8ymgS5V-TOXOZVqxBu_oz3p-eFqFTbw8CI0t6xtKON-BEnG7rmViNNLXl5OsnMc6Mi3lcPAZ-VUmSFGcPSiseMqAiyuwvr63eDp23AKFudBweSAhH7nFa5pxNbds3q4YtE2qzvvMcf2emGqCzlC0m2aXEYHo7GkArfL3c42mQJJrF2K_zP6C4uOb43fV8al8VcDYdjIewXZlLnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
آماده‌ای هیجان واقعی رو تجربه کنی؟
🦖
در
TrexBet
، دنیایی از اسلات‌های جذاب، بازی‌های کازینوی زنده و لحظه‌های هیجان‌انگیز منتظر توئه!
🦖
صدها بازی متنوع
🦖
تجربه‌ای سریع و روان
🦖
هیجان در هر اسپین
🦖
🦖
🦖
🦖
🦖
🦖
🦖
🦖
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/71479" target="_blank">📅 19:25 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71478">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mi9B9FHQ1p1t_HkHxwVjt0qRxg-YsEzjZmak2tenFnqAOlLjpWI4b8CA2NYcusVVjOJKr3Fj1XGQKMPV77JJ7AP_N5n-lNSlEUtOf-PZImxak8d_oIx7StsfndcKZ0NJA0yEhAIdE-8LY8tcYxSXewF_JCGTMleBQNxxS11LsDrBoo5N1Bfi1zab7FR5etXfcd6OgvLveeWzzEK96Se86a_EuEW0Snv4StXnRGOrf8KEMZjAgX960ea0R2qJaiU_4N-dx-Nwl3cPvqITdwQGoiQ2S2OOPIFsukGrSSg9lpQKsbkuaLhEzO3GdmaQ7TCpV1d3D3skxJ17lPZqqqth5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
🇮🇱
🇺🇸
نخست‌وزیر نتانیاهو:
می‌خواهم برای رئیس‌جمهور دونالد جی. ترامپ، خانواده‌اش و مردم آمریکا آرزوی «شانا تووا» (Shana Tova) داشته باشم؛ سالی نو همراه با شادی و سلامتی.
در طول سال گذشته، ایالات متحده و اسرائیل با یکدیگر به پیشرفت‌های تاریخی دست یافته‌اند. ایران و محور شرارتِ آن، ضعیف‌تر از هر زمان دیگری شده‌اند، در حالی که اتحاد میان آمریکا و اسرائیل قوی‌تر از همیشه است.
من به رئیس‌جمهور ترامپ بابت اعمال محاصره علیه رژیم شرور ایران و فشار اقتصادی بر بزرگ‌ترین منبع بی‌ثباتی در جهان، تبریک می‌گویم.
مردم اسرائیل در مقابله با نیروهای ترور، در کنار مردم ایالات متحده و رئیس‌جمهور ترامپ ایستاده‌اند.
در سال پیشِ رو، ما همچنان به تلاش برای امن‌تر ساختن جهان برای همگان ادامه خواهیم داد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/71478" target="_blank">📅 18:49 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71477">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0625ae5db9.mp4?token=Z08VJALKYBaIwVoZDUPfB8D4KUeB-mOayFAEFAFM6mUf0YpJG7hSRwdXiXGnRxh7fD0nGUUKrhDP33SHxcOhP16SfsumQXf4I61-ngf28eF0qreRMrshcYOGDfUj_ev2JqNBa0pa8spAQEBJktooOZ3lbu9ns1RzjIrnllz3IUo5SKgLBw-zCfp76krYjx_fT6f2hlpVcnNIjTYI3VxsI0-OYmA1fbVVcB1l65QQm7LayL3Lpfp5MS-pQIkoV9uvWfTlk9f_FOi4efLBg7_BM_ao-X0ufzt3F3tTTRH00h5s0yYkekgfBffDB-v_VLswmAotmSrWO3yZ4CTJul7bFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0625ae5db9.mp4?token=Z08VJALKYBaIwVoZDUPfB8D4KUeB-mOayFAEFAFM6mUf0YpJG7hSRwdXiXGnRxh7fD0nGUUKrhDP33SHxcOhP16SfsumQXf4I61-ngf28eF0qreRMrshcYOGDfUj_ev2JqNBa0pa8spAQEBJktooOZ3lbu9ns1RzjIrnllz3IUo5SKgLBw-zCfp76krYjx_fT6f2hlpVcnNIjTYI3VxsI0-OYmA1fbVVcB1l65QQm7LayL3Lpfp5MS-pQIkoV9uvWfTlk9f_FOi4efLBg7_BM_ao-X0ufzt3F3tTTRH00h5s0yYkekgfBffDB-v_VLswmAotmSrWO3yZ4CTJul7bFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ:
ما به نیروهای نظامی‌ای که هم‌اکنون در تلاشند تا اطمینان حاصل کنند بزرگ‌ترین حامی تروریسم در جهان — یعنی جمهوری اسلامی ایران  — هرگز و به هیچ وجه به سلاح هسته‌ای دست نخواهد یافت، ادای احترام می‌کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/71477" target="_blank">📅 17:59 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71475">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3dd606e096.mp4?token=vOcEo1XB7k8lVrhhCkd5h1zXAtnHE_NiXXaYRxSc_3qgY23N_hp5Oaxglivmkwz3dCGHGaTkR6KrZT_rHQsonGhYFfILfDhQQ2I4d8tEH9rRAFD3djHDwO0sA8Hgt4Vb9Dy4feOSN_UgFkw6XrcJ8_DbVdNn41uZiFlje38mt5i5rUoKfmPJJcVwrkokgufeR6GjyqsrEl4Rra9YBH8Q_eWOtwUDo2qNkKLD5oOGHwHMEWYNAcz5Q63EYKxeX7ClE0NnGG-XbilGFysYtrG0--91iKdxdxp468MuARCI0lXD6SO7SSbJnxfOOUEm7bV5JWBLPQ2FRE-AVJaKvisd6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3dd606e096.mp4?token=vOcEo1XB7k8lVrhhCkd5h1zXAtnHE_NiXXaYRxSc_3qgY23N_hp5Oaxglivmkwz3dCGHGaTkR6KrZT_rHQsonGhYFfILfDhQQ2I4d8tEH9rRAFD3djHDwO0sA8Hgt4Vb9Dy4feOSN_UgFkw6XrcJ8_DbVdNn41uZiFlje38mt5i5rUoKfmPJJcVwrkokgufeR6GjyqsrEl4Rra9YBH8Q_eWOtwUDo2qNkKLD5oOGHwHMEWYNAcz5Q63EYKxeX7ClE0NnGG-XbilGFysYtrG0--91iKdxdxp468MuARCI0lXD6SO7SSbJnxfOOUEm7bV5JWBLPQ2FRE-AVJaKvisd6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
🇺🇸
پرزیدنت ترامپ واقعه ۱۱ سپتامبر را به جنگ خود علیه ایران پیوند می‌دهد:
به همین دلیل است که امروز می‌جنگیم. ما چاره‌ای نداریم؛ تنها گزینه، پیروزی است. ما سرسختانه می‌جنگیم. برای پیروزی می‌جنگیم.
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/71475" target="_blank">📅 17:54 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71474">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c788d5732.mp4?token=s_SkeFWS3ohm_dRgrNXIKTqTjLVaa1xGVOf2x3s5nUi5XFGLjJ1ha_18Y0OPGyGN4iv01dH5hqJp9virKAqvjTQobfcTZ4GQhIG2CjXXWAoY_J9Z1FV9Dxuku0XnvCB-uQg-DQPQyEKB16pOSWqXr42mBIzv16SU0X3Envz-U3SFkwZwZxOUbKvhjrTPia6_Yqt9bin15Tjc8SretjlA0y4c50tol1kUAKJBCE15ZeEdWwX-8_GIxWTt1bLAEO-RSlTKiokjTxWC-4eQnnMg49A1tzAZxGpi-mJ1mjMvB8wdmKfm9RGrN-2VZYzz1wKM2m1yEC7igD63l366ghWutg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c788d5732.mp4?token=s_SkeFWS3ohm_dRgrNXIKTqTjLVaa1xGVOf2x3s5nUi5XFGLjJ1ha_18Y0OPGyGN4iv01dH5hqJp9virKAqvjTQobfcTZ4GQhIG2CjXXWAoY_J9Z1FV9Dxuku0XnvCB-uQg-DQPQyEKB16pOSWqXr42mBIzv16SU0X3Envz-U3SFkwZwZxOUbKvhjrTPia6_Yqt9bin15Tjc8SretjlA0y4c50tol1kUAKJBCE15ZeEdWwX-8_GIxWTt1bLAEO-RSlTKiokjTxWC-4eQnnMg49A1tzAZxGpi-mJ1mjMvB8wdmKfm9RGrN-2VZYzz1wKM2m1yEC7igD63l366ghWutg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
اسکات بسنت وزیر خزانه‌داری آمریکا:
آنچه اکنون در مورد ایران شاهد آن هستیم، حیوانی است که در تنگنا گرفتار و زخمی شده است.
این آخرین نفس‌های رژیمی رو به احتضار است.
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/71474" target="_blank">📅 17:34 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71473">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/971b0d1003.mp4?token=kOfBlGpoBECaAyYgU0y2XTKFEsnnayyQ03HasBZtjgM0_b3NzEh6i_T4yuFVBohmg7q8J0ZBGEOMS5eFoupTzpLikrdDDbuNiK_gp6OxHiK3d88Q3DfRPgOSZQ1r8-d7_kNTwFBW3aweGpKOPPWSL-Hl4b45cPZnsO5897y9cJ3dASYRIEY1Cxy1ikesRjTG8I-L_Ivr9bsH0arPsopXA5Ej5IVMNgYEGPHaJzuzejDM8s075RhDjR5DfiDfIPBmN0i97fXpk1YJQQYSpSc-ZWVJYNyvub2NWCbBfrn5wcWLyqdFK3LyzsUAGruYFizDKhsZ9AKVCV30BpwxpeJj4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/971b0d1003.mp4?token=kOfBlGpoBECaAyYgU0y2XTKFEsnnayyQ03HasBZtjgM0_b3NzEh6i_T4yuFVBohmg7q8J0ZBGEOMS5eFoupTzpLikrdDDbuNiK_gp6OxHiK3d88Q3DfRPgOSZQ1r8-d7_kNTwFBW3aweGpKOPPWSL-Hl4b45cPZnsO5897y9cJ3dASYRIEY1Cxy1ikesRjTG8I-L_Ivr9bsH0arPsopXA5Ej5IVMNgYEGPHaJzuzejDM8s075RhDjR5DfiDfIPBmN0i97fXpk1YJQQYSpSc-ZWVJYNyvub2NWCbBfrn5wcWLyqdFK3LyzsUAGruYFizDKhsZ9AKVCV30BpwxpeJj4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇵🇱
اعتراض ربات های انسان‌نما در مقابل وزارت امور دیجیتال لهستان و سردادن شعارهایی با مضمون«ما خواهان قانون‌گذاری هستیم»و «از مشاغل دفاع کنید»
😳
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/71473" target="_blank">📅 17:13 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71472">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff3ddeb433.mp4?token=egpQ8kRQw1EyrhIoLpweNhl5gOBoxlyGAz8B5pIql9m66WLoo5Pq12t-9VibeiMtKWOFIH-CEacyN58dtoK_cwk_vbqfMuroAmwAloiVB8OfImWnWVpDgN09TlRZyEO5e-LbkpfSd1kwue7nzkXDw2Q_8YJkTjLHq7Hz4CBzviv1IfGE8ZPmwVlFnzTg8KZIJY0SBc-FGks1LDiF2UcvHgQ2RjrQxVtfbOJi8KmriPeEGIQcXV0xm5NN8SuGgoQGEvW9NyjNUXthm8tSgASGUdC7zRKPo1WSbi1pjvRThXG2FyPxHgl_5nQaxcIiOLp5FmNEi9r6QsQXsXohseUzKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff3ddeb433.mp4?token=egpQ8kRQw1EyrhIoLpweNhl5gOBoxlyGAz8B5pIql9m66WLoo5Pq12t-9VibeiMtKWOFIH-CEacyN58dtoK_cwk_vbqfMuroAmwAloiVB8OfImWnWVpDgN09TlRZyEO5e-LbkpfSd1kwue7nzkXDw2Q_8YJkTjLHq7Hz4CBzviv1IfGE8ZPmwVlFnzTg8KZIJY0SBc-FGks1LDiF2UcvHgQ2RjrQxVtfbOJi8KmriPeEGIQcXV0xm5NN8SuGgoQGEvW9NyjNUXthm8tSgASGUdC7zRKPo1WSbi1pjvRThXG2FyPxHgl_5nQaxcIiOLp5FmNEi9r6QsQXsXohseUzKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇱
❌
🇶🇦
هم‌زمان با نخستین سالگرد حمله هوایی اسرائیل به دوحه (قطر) در سپتامبر ۲۰۲۵ — که نخستین حمله اسرائیل به خاک قطر محسوب می‌شود — تصاویر جدیدی از این رویداد منتشر شده است.
این حمله، مقامات ارشد حماس از جمله «خلیل الحیه»، مذاکره‌کننده ارشد این گروه را در جریان مذاکرات آتش‌بس هدف قرار داد.
اگرچه رهبران ارشد حماس از این حمله جان سالم به در بردند، اما شش نفر، از جمله پسر خلیل الحیه و یک مأمور امنیتی قطری، کشته شدند.
این تصاویر جدید که منبع آن‌ها شبکه تلویزیونی «العربی» (Al-Araby TV) اعلام شده، لحظه اصابت را از زوایایی که پیش‌تر دیده نشده بودند، نشان می‌دهند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/71472" target="_blank">📅 16:31 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71471">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e182f67792.mp4?token=EWWhFd6t_u5xvH9Q4Bf4X84jzP__OxMoEMd0Ubn6PocvFR89E13Y-rIfcf3URkb4U84rPaUOwVHgfNGGNTwv1owVjaJlUzbm9aQDNonzMtv6BAoJZ3IfNr1k9mWBDTTYPaTq9Gm85D_fakWmO8TGILji-74cGbCz1D88-UyeTB0B8fI43Uh36QaQlLBETYRwXQzkEIB8AzAa_QLqp6Fs5sXaJ8jct463Me-6gi7ztkznPqBCDSnoZfxD-6a2NBnvFNo_wazacq9mRhbMG5xoweB1KN43d2D85AIbRGcALeCmwFHc1e-UpJyRsg8C1XtvUZTCK6PMwQXnt76eTwRuOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e182f67792.mp4?token=EWWhFd6t_u5xvH9Q4Bf4X84jzP__OxMoEMd0Ubn6PocvFR89E13Y-rIfcf3URkb4U84rPaUOwVHgfNGGNTwv1owVjaJlUzbm9aQDNonzMtv6BAoJZ3IfNr1k9mWBDTTYPaTq9Gm85D_fakWmO8TGILji-74cGbCz1D88-UyeTB0B8fI43Uh36QaQlLBETYRwXQzkEIB8AzAa_QLqp6Fs5sXaJ8jct463Me-6gi7ztkznPqBCDSnoZfxD-6a2NBnvFNo_wazacq9mRhbMG5xoweB1KN43d2D85AIbRGcALeCmwFHc1e-UpJyRsg8C1XtvUZTCK6PMwQXnt76eTwRuOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
توصیه های این بانو درباره وظایف زن مرد توی ازدواج ۳ میلیون ویو گرفته واقعا مفید بود
😏
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/71471" target="_blank">📅 16:04 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71470">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f28a9989cd.mp4?token=uRwRHHBYMOgAESUetzLCMv1toApLk7BbEgJpDELxqUNyxZ_5fTCGeZkDumDYHDG5WhiTKr7pxo1Zk5oQythAKZVUZDCWOJSxK_OJPsG3DPl1t_i_LI-9E5ZhZRDNLG8il5LW0Zogmacql_QPZASPclqIxfMF85ahdE8tl0dhQxMzyUPtNUdFyp481XpwFJhb-xyIJHY9654wgwqaJlHjRyXwCpcAgGAym5KZQZoJ4UF6tUY8gUCKFo9aQ7bdTXkutvRKV3_va9-TTTdoMFBIYBfRVYVnT87Yf2yHH-Zj4fp3f9ZZLEgfppR2_nhbZXkSiQ3vHmuB-jTO-1rCEKV6QQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f28a9989cd.mp4?token=uRwRHHBYMOgAESUetzLCMv1toApLk7BbEgJpDELxqUNyxZ_5fTCGeZkDumDYHDG5WhiTKr7pxo1Zk5oQythAKZVUZDCWOJSxK_OJPsG3DPl1t_i_LI-9E5ZhZRDNLG8il5LW0Zogmacql_QPZASPclqIxfMF85ahdE8tl0dhQxMzyUPtNUdFyp481XpwFJhb-xyIJHY9654wgwqaJlHjRyXwCpcAgGAym5KZQZoJ4UF6tUY8gUCKFo9aQ7bdTXkutvRKV3_va9-TTTdoMFBIYBfRVYVnT87Yf2yHH-Zj4fp3f9ZZLEgfppR2_nhbZXkSiQ3vHmuB-jTO-1rCEKV6QQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
شرکت پخش فرآورده‌های نفتی:
موفق شدیم رقم ۱۰ هزارتومان را در پمپ بنزین‌ها نشان دهیم و برچسب‌های صفر ثابت را بردارید
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/71470" target="_blank">📅 15:31 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71469">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5fc8b06f7d.mp4?token=MwKwcCcPyV32reA5zSBm4GSUVt_DPn0afHHsEs3SzwTnc9bnbn0zwVoDO60Z78pnV0ZvJMlJDhsBascgxMwBCJCQEOLkaOfXZrusIPD-oVXnYu0-rNYxyn0mKPrbsBlRZeY_aoVOAuN1VvAg0b2W1tRTdcV2nULqfCF22wwuyz69u_yIAsKDW0sYYe8eXqCx9Sy-9yyXOXp12SwE6FOcIf1JdEdcD5g5vLyvoT8Ecxmcm7nlWeWPtyaP0NHkAyGWEBusQstTwoFZDw725VQKDVTdntAXVXCdoH9fkJigfrra0mcDoHiJnRLyiNHVnSRRD4xMw3B4ShBES7tPDTADiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5fc8b06f7d.mp4?token=MwKwcCcPyV32reA5zSBm4GSUVt_DPn0afHHsEs3SzwTnc9bnbn0zwVoDO60Z78pnV0ZvJMlJDhsBascgxMwBCJCQEOLkaOfXZrusIPD-oVXnYu0-rNYxyn0mKPrbsBlRZeY_aoVOAuN1VvAg0b2W1tRTdcV2nULqfCF22wwuyz69u_yIAsKDW0sYYe8eXqCx9Sy-9yyXOXp12SwE6FOcIf1JdEdcD5g5vLyvoT8Ecxmcm7nlWeWPtyaP0NHkAyGWEBusQstTwoFZDw725VQKDVTdntAXVXCdoH9fkJigfrra0mcDoHiJnRLyiNHVnSRRD4xMw3B4ShBES7tPDTADiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🔞
اگه بدون کاندوم رابطه جنسی برقرار می‌کنید؛
این پست رو یه گوشه‌ای تو تلگرامتون ذخیره کنید که یه روزی بدجوری به کارتون میاد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/71469" target="_blank">📅 15:03 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71465">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/54fcf2b7ac.mp4?token=vmb_U045kl8fW1nOaoV2YaivKa7wsyUBBc1lslct20OA-clQO9EQ6XZruW9ana3TXuZjuF9M85oL5Wnegtf2m919-vYHdPp9fOcna3CRRq42hLyDs_1xGURW33G8kntIAMYdTRusTwVnCsRqcYWK7W55BdHfCLbnEfjZlEufAre43BjXL9YZH2MvcuZA2rR2cFN50Z5wbQ7YA0AS6c1_PkKi-_YYe0Fw3cJOSb4d92JIR1gQk0TfaOCUsyqQr1WEwe8sKpPzDktkerb8FVFykSCtYKbq7iXbF9drFaCy9q_HodpNkMe5r47FxHUyBpLGpMzphxV3zb454Ue7-jE9eA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54fcf2b7ac.mp4?token=vmb_U045kl8fW1nOaoV2YaivKa7wsyUBBc1lslct20OA-clQO9EQ6XZruW9ana3TXuZjuF9M85oL5Wnegtf2m919-vYHdPp9fOcna3CRRq42hLyDs_1xGURW33G8kntIAMYdTRusTwVnCsRqcYWK7W55BdHfCLbnEfjZlEufAre43BjXL9YZH2MvcuZA2rR2cFN50Z5wbQ7YA0AS6c1_PkKi-_YYe0Fw3cJOSb4d92JIR1gQk0TfaOCUsyqQr1WEwe8sKpPzDktkerb8FVFykSCtYKbq7iXbF9drFaCy9q_HodpNkMe5r47FxHUyBpLGpMzphxV3zb454Ue7-jE9eA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
🇺🇸
در ۱۱ سپتامبر ۲۰۰۱، شبکه تروریستی القاعده به رهبری اسامه بن‌لادن، حملاتی هماهنگ‌شده علیه ایالات متحده انجام داد.
🗣️
در این عملیات، ۱۹ عضو القاعده چهار هواپیمای مسافربری را ربودند.
🇸🇦
۱۵ نفر تبعه عربستان سعودی.
🇦🇪
۲ نفر از امارات متحده عربی.
🇪🇬
۱ نفر از مصر.
🇱🇧
۱ نفر از لبنان.
دو هواپیما به برج‌های دوقلوی مرکز تجارت جهانی در نیویورک برخورد کردند و هواپیمای سوم به ساختمان پنتاگون در ویرجینیا اصابت کرد.
هواپیمای چهارم نیز در پنسیلوانیا سقوط کرد؛ پس از آنکه مسافران برای بازپس‌گیری کنترل هواپیما تلاش کردند.
در مجموع، ۲٬۹۷۶ نفر در این حملات کشته شدند و هزاران نفر نیز مجروح شدند.
تحقیقات گسترده FBI، ارتباط مستقیم این حملات با القاعده و نقش این شبکه در سازماندهی و آموزش هواپیمارباها را تأیید کرد.
پس از حملات، آمریکا عملیات نظامی در افغانستان را با هدف سرنگونی حکومت طالبان و مقابله با القاعده آغاز کرد.
اسامه بن‌لادن سرانجام در ۲ مه ۲۰۱۱ در پاکستان کشته شد.
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/71465" target="_blank">📅 14:34 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71464">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🇹🇷
پهپاد «آکینجی» (AKINCI) ترکیه اکنون با موفقیت موشک‌های UAV-300 و UAV-122 ساخت شرکت «روکت‌سان» (ROKETSAN) را آزمایش و شلیک کرده است.
نقطه عطف این آزمایش، شلیک موشک بالستیک مافوق‌صوت UAV-300 بود که با اصابت دقیق به هدف در فاصله‌ای بیش از ۲۵۰ کیلومتر، توانمندی آکینجی در انجام حملات بالستیک دوربرد را به اثبات رساند.
موشک کوچک‌تر UAV-122 نیز در جریان این آزمایش با موفقیت شلیک شد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/71464" target="_blank">📅 14:02 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71461">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ccd5a9f3c7.mp4?token=htZ6lIwQdcEmxZB4aVi_p2DooG2LwlLB34ZBS7OBZcvrQM1ORCCfuqbdqdXP8sRjNXYGv031gpJe1JfNw_7b5dpY_op1Av0k0AvbAxoFWrXHhytv3XPfBupU157SxnG4WNVYTWubEQ7ZjxXfdXuFgJCs6xZftQrA_9ZBbgBEdq8wvpE6EVH_zlzoZ3ET1zrDXjVymL4k1Rf82keqbTI33kaj_a5sSeOVjTZi4hzZIZlQr6Ske7UMuJV1xGNXS5CpfPe9ZjZuundVnvh6lRtmEUY_2Z5IrFcXMLsu21QuQawV5Cn_teMkv-FAweVyULwp1ZN-690JSiOhXy5RCxSu7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ccd5a9f3c7.mp4?token=htZ6lIwQdcEmxZB4aVi_p2DooG2LwlLB34ZBS7OBZcvrQM1ORCCfuqbdqdXP8sRjNXYGv031gpJe1JfNw_7b5dpY_op1Av0k0AvbAxoFWrXHhytv3XPfBupU157SxnG4WNVYTWubEQ7ZjxXfdXuFgJCs6xZftQrA_9ZBbgBEdq8wvpE6EVH_zlzoZ3ET1zrDXjVymL4k1Rf82keqbTI33kaj_a5sSeOVjTZi4hzZIZlQr6Ske7UMuJV1xGNXS5CpfPe9ZjZuundVnvh6lRtmEUY_2Z5IrFcXMLsu21QuQawV5Cn_teMkv-FAweVyULwp1ZN-690JSiOhXy5RCxSu7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇦
❌
🇷🇺
حمله شناورهای بدون سرنشین (USV) اوکراین به بندر سوچی در منطقه کراسنودار روسیه
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/71461" target="_blank">📅 13:20 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71460">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/icEOHvYSrD7bW-8wo9wBRA3okd4_Fq6-aJLstuKEGKBCdTJokuTob-AUE0jTQlcWVFybRF9MkuVRYq3OaNgeC6Itr0BpOYq0Qyi-uALb4E69ht0EzN1CAKImYnzEtqt-NL24870b61mUoEW8rUGWxUeyiWQose-g0LVGO43r9OFf1V2ghNSD-hOJIcxupfQyNu_FeOoVWV4z5hek4nZOEEjlB22yyrvdcUoey0d1AdqZtw3AtDAxk8FS_FD9Zy_pIxyorD7Gzm88XyB6Y7FtMSSMUBwY1dOKl_4wuYfnHNzHQYtk4MpSvQaa1wB5L_wAFMbL4_06dCfZlsjHa2HzrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇾🇪
🇾🇪
حوثی‌های یمن جزیره پریم (میون) را تصرف کرده و کنترل خود را بر تنگه باب‌المندب تکمیل کردند.
⏺
🗞
خبرگزاری رویترز نیز در گزارشی جداگانه اعلام کرده است؛
حوثی ها به شهر ساحلی «ذوباب» — که درست در کنار این تنگه واقع شده — رسیده‌اند.
حوثی‌ها اکنون تقریباً تمام نوار ساحلی یمن در دریای سرخ را در کنترل خود دارند.
این دستاورد سرزمینی را می‌توان از نظر راهبردی، مهم‌ترین پیشروی در کل جنگ یمن دانست.
جزیره پریم در میانه این تنگه ۲۹ کیلومتری قرار گرفته و عملاً آن را به دو مسیر کشتیرانی مجزا تقسیم می‌کند.
تسلط بر این جزیره و همچنین نوار ساحلی مجاور آن بدین معناست که حوثی‌ها می‌توانند کشتی‌های عبوری را با استفاده از توپخانه و تسلیحات کوتاه‌برد تهدید کنند؛ نه صرفاً با موشک‌های دوربرد و پهپادهایی که از مناطق داخلی‌تر شلیک می‌شوند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/71460" target="_blank">📅 12:54 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71459">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71459" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/71459" target="_blank">📅 12:54 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71458">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fRFvICSGAsETo_zpiGEOgzzs0CRZU9TrKf3ZEYGe0IMCez1F5RCiLQZ8drxbUcEzjOJ1dKcj5gfV-oR4AGjH2g2Tb1VhRV874SCJTD-dFMxnFMF7TYOhgQeCWk-VDV4OrIeyXZFi2R4x3Zqase78_WD8F_Dk6sO52oJmNwovSDOoFVhBJ9n8klTjRYMwqTV9sN3iPwfE0JX5b2WC9QVrhkKjxKJPde2EaZMbrA9OUefT5vbkexepcma85MEUPXRufIIM2n5W29-JzUdkhWT_AxBO4oOYAGlgdbe9d1yziLc4cf7INBr8kWaSrdqdggkODqZ_YF4Sd_qbBrwDIUBqcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
مچ‌های مهم امروز در سایت بین‌المللی
TrexBet
والنسیا
🆚
سویا
فیورنتینا
🆚
ونزیا
شالکه
🆚
انیون برلین
مارسی
🆚
رن
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
انتخابت رو انجام بده و آماده‌ی هیجان باش!
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/71458" target="_blank">📅 12:54 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71457">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4149a89627.mp4?token=ulhMcsjdIvr3e_-SzE8iVxid1DuoZRGEQIbW_8NyrMMHrLMRMxsibXEcXDM4YFhxk_MkE2ZkeSbRhnUiyjaaczHms52suicxscwGMaxCRaNkFyeYBuMr_DBHEDWcN_QI8QUsflTrrZ8Nk4_JTYsmh9s82jSOTO_jxozfHH_BUwCPpfCBHm5G_AE6mCPT_XIYRKYgmT3i695t4rRGzgKl6xDt7laM4iaSGkJ3dtN3QeL1noy3a3WAPcK5ARTPlnGW0PpuVrme59Gfw1siztUCJowW9fNj96FAuf5dgcwwrHCFBsZelTvdYfBlaUALDwzffe_Tc4lNv1XxmVXPDJGW8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4149a89627.mp4?token=ulhMcsjdIvr3e_-SzE8iVxid1DuoZRGEQIbW_8NyrMMHrLMRMxsibXEcXDM4YFhxk_MkE2ZkeSbRhnUiyjaaczHms52suicxscwGMaxCRaNkFyeYBuMr_DBHEDWcN_QI8QUsflTrrZ8Nk4_JTYsmh9s82jSOTO_jxozfHH_BUwCPpfCBHm5G_AE6mCPT_XIYRKYgmT3i695t4rRGzgKl6xDt7laM4iaSGkJ3dtN3QeL1noy3a3WAPcK5ARTPlnGW0PpuVrme59Gfw1siztUCJowW9fNj96FAuf5dgcwwrHCFBsZelTvdYfBlaUALDwzffe_Tc4lNv1XxmVXPDJGW8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
کارشناس صداسیما: ما ۵۰۰ میلیون تُن طلا داریم.
ـ مجری:  الحمدلله
+ کل طلای استخراج شده تو جهان ۲۲۰ هزار تنه
😂
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/71457" target="_blank">📅 12:03 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71456">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/27045da6d6.mp4?token=tuWLbwhGX200B5n34Lu1bO5zeJE6ozCyvUbImJrx6c9aj_zb5DpU-erskRJ1LNI5n6uk2Hnp-RPDcT6tMk27Ezs3N1wd9NJcVQpwfjzf74EzkBoICeO2ymR_60vbkWPy7NBkeht3yoih23gsaM4-NbI2Rfd896S6B384LI2pow4_VjQB6NdObSkyAlx2dYbslB5WJL9osBpzYhzCLtID0EefcJTgNrybPvHSoObn8hxO1y_yCO3bTpibk4_Jx5Fwez2OLf7UlIyfK8XUyECPtkoTGLsTekWhYJWhLaja3NRgBEbTkgdtm09BImeaUz8yY4KOhGCdySJFza_V82Lh5g" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/27045da6d6.mp4?token=tuWLbwhGX200B5n34Lu1bO5zeJE6ozCyvUbImJrx6c9aj_zb5DpU-erskRJ1LNI5n6uk2Hnp-RPDcT6tMk27Ezs3N1wd9NJcVQpwfjzf74EzkBoICeO2ymR_60vbkWPy7NBkeht3yoih23gsaM4-NbI2Rfd896S6B384LI2pow4_VjQB6NdObSkyAlx2dYbslB5WJL9osBpzYhzCLtID0EefcJTgNrybPvHSoObn8hxO1y_yCO3bTpibk4_Jx5Fwez2OLf7UlIyfK8XUyECPtkoTGLsTekWhYJWhLaja3NRgBEbTkgdtm09BImeaUz8yY4KOhGCdySJFza_V82Lh5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یه نفر به زنش گفته دست پختت رو سگم نمیخوره! اونم برای اینکه شوهرش رو ضایع کنه، رفته غذاشو گذاشته جلوی سگ!
در نهایت سگه این شاهکارو خلق کرد:
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/71456" target="_blank">📅 11:34 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71455">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c6ecedd2b.mp4?token=sWXmFXOpVn2tJxmAYtN9AFz3VTjBrYgO1xElO4Q5qObr8rnKXl1jljAej5ApU4dFQwK857NaRbiVlydt3hxIb4vJfbcwSV18wTIJIkyhviThyfM83-hh1k0_URfe3lvBawzYUPDQWwenaXAFbmQDA7aSdbu-U8PwMGeXAvlaKYuNVoPmAMaNRj79Qr7zUh-UMgqYVCwvMxP5iJjPO1GlhoRS184EiBTbHtxXsInegQQFvryHD4o7pCjjpbi8VlswHBsGWrOI_sYOzxHd_uIym46qDvBnGYudI922varZnZyyUz6I4ajFP7GDQvtar3cDv29gEL1Um0vPRnFsPL089w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c6ecedd2b.mp4?token=sWXmFXOpVn2tJxmAYtN9AFz3VTjBrYgO1xElO4Q5qObr8rnKXl1jljAej5ApU4dFQwK857NaRbiVlydt3hxIb4vJfbcwSV18wTIJIkyhviThyfM83-hh1k0_URfe3lvBawzYUPDQWwenaXAFbmQDA7aSdbu-U8PwMGeXAvlaKYuNVoPmAMaNRj79Qr7zUh-UMgqYVCwvMxP5iJjPO1GlhoRS184EiBTbHtxXsInegQQFvryHD4o7pCjjpbi8VlswHBsGWrOI_sYOzxHd_uIym46qDvBnGYudI922varZnZyyUz6I4ajFP7GDQvtar3cDv29gEL1Um0vPRnFsPL089w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
این آقا یه ویدیو از چینی‌ها گذاشته که یه شیشه‌دودی واسه ماشین ساختن که با یه بیلبیلک میشه درصد دودی بودنش رو کم و زیاد کرد؛
حالا به جای اینکه پشمای ملت از تکنولوژی بریزه، 98 درصد کامنت‌ها اینه:
بهترین مکان واسه اونایی که مکان ندارن
😟
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/71455" target="_blank">📅 11:04 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71454">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d8c4f2b29b.mp4?token=f3QjYToP5PNBWUKfz5HhTK1_WP0Axz75_9icUaVXgIVxXsrDbo307mYIBf6lVvcQMbJqOaWXj1bkVq-0vTXS5HMe-WTY6jWX01vaHWN5ItacRb0HfxYb1CwWgtmge6Fe8HwMaMXxh_2sbwaNjMup1pFOItHk6z2QlLtNTvcGgXDKRpktJX878umAeRA9GS3FwpvENzXGybG_FrMYFJZlIFH9WmeD6q62cTBVXtM94ac-rNE3_Lhima4z36AEydcWbfoivTgC6YQOURuZFqYeSLaofCkkbc4GIV_bfBBGhGlec0hAURI8Wk70mPEGKaJWJz5Rg2XHLwnP4viVPCjxag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d8c4f2b29b.mp4?token=f3QjYToP5PNBWUKfz5HhTK1_WP0Axz75_9icUaVXgIVxXsrDbo307mYIBf6lVvcQMbJqOaWXj1bkVq-0vTXS5HMe-WTY6jWX01vaHWN5ItacRb0HfxYb1CwWgtmge6Fe8HwMaMXxh_2sbwaNjMup1pFOItHk6z2QlLtNTvcGgXDKRpktJX878umAeRA9GS3FwpvENzXGybG_FrMYFJZlIFH9WmeD6q62cTBVXtM94ac-rNE3_Lhima4z36AEydcWbfoivTgC6YQOURuZFqYeSLaofCkkbc4GIV_bfBBGhGlec0hAURI8Wk70mPEGKaJWJz5Rg2XHLwnP4viVPCjxag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
از سالن زیبایی مذهبی برای عروسی رونمایی شد، از آپشن‌های خاص این سالن میشه به این موارد اشاره کرد:
رد شدن از زیر قرآن هنگام ورود به سالن.
عکس گرفتن با سران مملکت که کشته شدن.
پخش مداحی و قرآن به جای موزیک.
داشتن وضو توسط پرسنل قبل از میکاپ.
خوندن نماز دسته جمعی برای خوشبختی.
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/71454" target="_blank">📅 10:30 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71453">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b9e0d9418.mp4?token=PpkoX6mcqhfJF-KyWWoxsWeVxzU_VllEQ0bkZT_FyAS5p1kMaXo3JUzztZ16sgKNr2ANwVNEgA1TibMp7B4PAOlWML4SIHFCom4tVjKZp-tdBqPo72neGxG1XqjkT78lq0aYyVY3Aer90AxI3fuf_XbbrOb4YcOzXddbnEJbnx7buBFBDXO0wBKaHl_qfL1qflbIgpp9JP28YIBXsqJzLy2TKXM2sLu5O1Nu-DKUhN2XNAlHu67UlURNvRz-uStArGxB_avhuCUrn3_uZv-dowLNzcRXPonGoMg-ALv-llSqmCxgaCK4GcAk6md0Gb7i6iJJ7rqxcjcdnJAXDzBm_IwNIrQzgigVYPIB9i4QloBaO8JMDFG3dGL-1VmKkBLVsLFqi_sQQN0wTcot5-uDbBm2g7ot3lFHARfTK7W8pM-WMXetAdVDV2IUGWSplzr7jcbZzriZmdTZdA0Hy5uwJOXeuzFMp5EapRfDQJYnT8NCN6ZEpVfy3d_380IXGl_RZHODtjuwFGQeuW93lPwZp61gNaRvksLQevgGwze3I9fkqU73EtDvkaIpMXmASLEYsLcUDh4J3F_DpGfyYZFC6KJ7S6X26vPr0dfOYZ7KbkYlC6U1IZKZ_4XBIp31OGX2DfJcxNN5fPKx9smG2R5wkZmUwBvd7D8IEG7MWM6mdJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b9e0d9418.mp4?token=PpkoX6mcqhfJF-KyWWoxsWeVxzU_VllEQ0bkZT_FyAS5p1kMaXo3JUzztZ16sgKNr2ANwVNEgA1TibMp7B4PAOlWML4SIHFCom4tVjKZp-tdBqPo72neGxG1XqjkT78lq0aYyVY3Aer90AxI3fuf_XbbrOb4YcOzXddbnEJbnx7buBFBDXO0wBKaHl_qfL1qflbIgpp9JP28YIBXsqJzLy2TKXM2sLu5O1Nu-DKUhN2XNAlHu67UlURNvRz-uStArGxB_avhuCUrn3_uZv-dowLNzcRXPonGoMg-ALv-llSqmCxgaCK4GcAk6md0Gb7i6iJJ7rqxcjcdnJAXDzBm_IwNIrQzgigVYPIB9i4QloBaO8JMDFG3dGL-1VmKkBLVsLFqi_sQQN0wTcot5-uDbBm2g7ot3lFHARfTK7W8pM-WMXetAdVDV2IUGWSplzr7jcbZzriZmdTZdA0Hy5uwJOXeuzFMp5EapRfDQJYnT8NCN6ZEpVfy3d_380IXGl_RZHODtjuwFGQeuW93lPwZp61gNaRvksLQevgGwze3I9fkqU73EtDvkaIpMXmASLEYsLcUDh4J3F_DpGfyYZFC6KJ7S6X26vPr0dfOYZ7KbkYlC6U1IZKZ_4XBIp31OGX2DfJcxNN5fPKx9smG2R5wkZmUwBvd7D8IEG7MWM6mdJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یه دختر موقع پریود اومده نوار بهداشتی استفاده کنه و با یه صحنه شوکه کننده مواجه شده!
خودتون ببینید...
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/71453" target="_blank">📅 10:04 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71452">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6849173423.mp4?token=D7iLVKp4QvJYKhEvp6s7qgShjgWDNtXPkft_XCVTi9bQfy7JR4JWS5bsrFgb0_R-nv0xSasCXTQAUmm0LpT8Xwjv4zisJhHZPuDSsDThwKQdkVNDkojrkYZoBir3pw_616wq4S8PBiRJQy1LJ5Pt3PZ-MOBM-GyknlXFPvqzLdee16CIKKjRPwGvH6X2x0iTp2CtUjY8MwybRZzvdxvZuFfC2Etv4W2TxPrFRh90pScGzHd7X572nB6RDVoiXX-vH1ZqHstLbcuzw3YGnKauGqw3BOoN6pNUZDh70SvqIh4L44MK0Kc1Lg8toyhz0H75iIPNEyfAcvEe7oCS1kO70oMVarrgXLKij37Y_AFOlFlkarwp4nToBjbW1dE1cb9SONbgrltvd8xUgFWNqePWxzkzOp46QLKS0o2RR9Z2AmxZihpWa5uMJVajHg3ezbdu8iLDcbeUnK-oaN6S4h99e6zJtVcfNCN5Wz8sm-U6T6h77rTREGZrZbNYVHH7QvHUsNIm_UAd-u3kY02I6lP73rkih76gsXetUKtNysYR76soonDZ0VQK2SCP08tHogtRNgI8d2mzqL-tRyrhf2U5Y3uG1e-eVMp5T2R1kGtBx3XEdubwrKoFl7KFSmFY0T5Ltouc2kxGdYE4Ef3H_Xiqrg26m_YE0pdTn3ZutPMLrmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6849173423.mp4?token=D7iLVKp4QvJYKhEvp6s7qgShjgWDNtXPkft_XCVTi9bQfy7JR4JWS5bsrFgb0_R-nv0xSasCXTQAUmm0LpT8Xwjv4zisJhHZPuDSsDThwKQdkVNDkojrkYZoBir3pw_616wq4S8PBiRJQy1LJ5Pt3PZ-MOBM-GyknlXFPvqzLdee16CIKKjRPwGvH6X2x0iTp2CtUjY8MwybRZzvdxvZuFfC2Etv4W2TxPrFRh90pScGzHd7X572nB6RDVoiXX-vH1ZqHstLbcuzw3YGnKauGqw3BOoN6pNUZDh70SvqIh4L44MK0Kc1Lg8toyhz0H75iIPNEyfAcvEe7oCS1kO70oMVarrgXLKij37Y_AFOlFlkarwp4nToBjbW1dE1cb9SONbgrltvd8xUgFWNqePWxzkzOp46QLKS0o2RR9Z2AmxZihpWa5uMJVajHg3ezbdu8iLDcbeUnK-oaN6S4h99e6zJtVcfNCN5Wz8sm-U6T6h77rTREGZrZbNYVHH7QvHUsNIm_UAd-u3kY02I6lP73rkih76gsXetUKtNysYR76soonDZ0VQK2SCP08tHogtRNgI8d2mzqL-tRyrhf2U5Y3uG1e-eVMp5T2R1kGtBx3XEdubwrKoFl7KFSmFY0T5Ltouc2kxGdYE4Ef3H_Xiqrg26m_YE0pdTn3ZutPMLrmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇱
❌
ویدیویی پشم‌ریزون که ارتش اسرائیل از عملیات تخریب تونل‌های زیر ارتفاعات علی‌الطاهر در جنوب لبنان منتشر کرده
😨
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/71452" target="_blank">📅 09:32 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71451">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c57019ecf0.mp4?token=v8G0vIPZUZt3VimVI6t4WyLF7nc-jEBcx9_SgUptp7TK11jpZxEDesQrlzG92TdvIneN-rKzEnRtUSCG-IWNO-UGxS6T_rhsIauMgwvuwreZ_ub09Ws1bvo_D2EpeiBALZQdpkM3G5LNGUDfApZm8VSsXMVez04fMjg0rGpfu15_xjHd9xiTcyN-aaEOihd6_hf0ZRGc7yxxWCMFHJK0JjNXc879cZgNpXj573WJZUEDn7lV5ekiwF_UPF0VbBks4H5Aw_my--1tMiYvjEfDmyRoEnTv4izrm3X1qNXzYqCLazYpGhCzLv0HeUo99ioCGKe52b16Dph7vW7Mevic0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c57019ecf0.mp4?token=v8G0vIPZUZt3VimVI6t4WyLF7nc-jEBcx9_SgUptp7TK11jpZxEDesQrlzG92TdvIneN-rKzEnRtUSCG-IWNO-UGxS6T_rhsIauMgwvuwreZ_ub09Ws1bvo_D2EpeiBALZQdpkM3G5LNGUDfApZm8VSsXMVez04fMjg0rGpfu15_xjHd9xiTcyN-aaEOihd6_hf0ZRGc7yxxWCMFHJK0JjNXc879cZgNpXj573WJZUEDn7lV5ekiwF_UPF0VbBks4H5Aw_my--1tMiYvjEfDmyRoEnTv4izrm3X1qNXzYqCLazYpGhCzLv0HeUo99ioCGKe52b16Dph7vW7Mevic0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
🇺🇸
ترامپ:
اگر ایران سلاح هسته‌ای داشت، ما با آن‌ها تماس می‌گرفتیم و می‌گفتیم: «جناب، آیا ممکن است با هم دیداری داشته باشیم؟»
آن‌وقت رفتارمان با آن‌ها بسیار متفاوت می‌بود.
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/71451" target="_blank">📅 08:45 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71450">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/534815e8ce.mp4?token=cboU2peQgkZHecH86ApFtALJ3Zc1g-mLUy7w3uenmaCBaLKcmfI4EN_9c1gsZBkAhfxIE9Zx5en9KWambtiADlXk-JsAEgiSsslmg-crlinhiwNRIY4YUFxfoAQO65N7X2NoSk9QqvfAYxV-qnk-y80BNIOrEKUdoczqFI-a_X2mB2jOjwKI2IZpmtTEcgYLgtOthED05I0XEe55IDCu-GshncZ1eLon-kve27RCTv0f7bzsMbmvNlsoI0BRil01tQlxwOMRO7BZLIhYn_k0eWiW82FpW35f2FDjy5uYmyNu-Qw4nOJsROIM-G9tykCT0PYiZpyi8pGCetoCPZum5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/534815e8ce.mp4?token=cboU2peQgkZHecH86ApFtALJ3Zc1g-mLUy7w3uenmaCBaLKcmfI4EN_9c1gsZBkAhfxIE9Zx5en9KWambtiADlXk-JsAEgiSsslmg-crlinhiwNRIY4YUFxfoAQO65N7X2NoSk9QqvfAYxV-qnk-y80BNIOrEKUdoczqFI-a_X2mB2jOjwKI2IZpmtTEcgYLgtOthED05I0XEe55IDCu-GshncZ1eLon-kve27RCTv0f7bzsMbmvNlsoI0BRil01tQlxwOMRO7BZLIhYn_k0eWiW82FpW35f2FDjy5uYmyNu-Qw4nOJsROIM-G9tykCT0PYiZpyi8pGCetoCPZum5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
🇺🇸
پرزیدنت ترامپ:
دیشب ما ۲۲ قایق را از تنگه هرمز بیرون راندیم. می‌دانید، ما کنترل تنگه را در دست داریم. آن‌ها کنترل تنگه را در دست ندارند. آن‌ها هیچ‌چیز را کنترل نمی‌کنند.
آن‌ها تورم ۳۰۰ درصدی دارند. حقوق ارتش خود را نمی‌پردازند. حقوق نیروهای انتظامی‌شان را هم نمی‌دهند.
و بالاخره زمانی فرا می‌رسد که ارتش و نیروهای انتظامی دست از شلیک به معترضان برمی‌دارند. شگفت‌انگیز است که چطور آن‌ها [تاکنون] چنین کاری می‌کنند.
می‌دانید، چین با استفاده از تانک ارتش این کار را با موفقیت انجام داد. یادتان هست؟ کشورهای دیگر نتوانستند. ترکیه نتوانست این کار را بکند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/71450" target="_blank">📅 08:40 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71449">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3fa815d3aa.mp4?token=UnKeeYr9WGtD9ZwaWaFnBJZ-uwiWTxdKknTT0N2Z32zNY_LJ7MV-iNaBtN8XB02wGRa88mcIg8hSbve7DL_xONZOu4YD99L4mgpYoAvZSEvn8kVEkdIHYIVZP-Lm5FEI1SRkLrej7ictDIGF3aw6A8Nkgle5t_Cs45tSB5JLJc6siCZEd9D4yn6WKuIO_lyrYMR8h5WnLkU6nBglT47wkiRflXgi83DRI-QtHK_H-za4arm1J0o6PKpbRNPbEXKCcRR2gL6slTxonEf2zgKlGZ1BEwe-7OqjESPjmR9xgi6xLT1tNmCdGshGmy3MeJrNS55g2swk6GLGgnsaVbrm6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3fa815d3aa.mp4?token=UnKeeYr9WGtD9ZwaWaFnBJZ-uwiWTxdKknTT0N2Z32zNY_LJ7MV-iNaBtN8XB02wGRa88mcIg8hSbve7DL_xONZOu4YD99L4mgpYoAvZSEvn8kVEkdIHYIVZP-Lm5FEI1SRkLrej7ictDIGF3aw6A8Nkgle5t_Cs45tSB5JLJc6siCZEd9D4yn6WKuIO_lyrYMR8h5WnLkU6nBglT47wkiRflXgi83DRI-QtHK_H-za4arm1J0o6PKpbRNPbEXKCcRR2gL6slTxonEf2zgKlGZ1BEwe-7OqjESPjmR9xgi6xLT1tNmCdGshGmy3MeJrNS55g2swk6GLGgnsaVbrm6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
مجری:
حتی نومحافظه‌کاران هم می‌گویند اگر قرار است وارد ایران شوید، باید تمام‌عیار وارد شوید؛ فقط بروید و کارشان را تمام کنید.
🇺🇸
ترامپ:
خب، شاید به خاطر انتخابات چنین کاری نکنم.
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/71449" target="_blank">📅 08:33 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71448">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2230f2a78e.mp4?token=E7LjR5nE39-Fy0mPrRkWGM9bMPCRKSWepZdrqphcX7T9mlv7Q5rjZpv5yFerU36LQmRco-8hyd5PSwzTFxEZqOlZaWYZORYjmai0g8kZsXBtEz5Scr7bmjP1_C6UrrrpgS5PlwpDXKgGha1UNGL7RrV7lL2ADmpbpoUg7Sgy7KF8dyLcuNVHO1OpS1IjJYB_2BKx3t16mBS_n6AU3TAMAns3uQgiXtEcBh5QoOaYsu0t_hRB6Wy0kdYlM-BkoIcxViWR6ZsxjFW2fOd0uG4BmC4rQzEtXApJsqF9LFI9rWbuh0w66HufxkgMfxN21n5zUdFtWgxeT5fK85lJbs1oaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2230f2a78e.mp4?token=E7LjR5nE39-Fy0mPrRkWGM9bMPCRKSWepZdrqphcX7T9mlv7Q5rjZpv5yFerU36LQmRco-8hyd5PSwzTFxEZqOlZaWYZORYjmai0g8kZsXBtEz5Scr7bmjP1_C6UrrrpgS5PlwpDXKgGha1UNGL7RrV7lL2ADmpbpoUg7Sgy7KF8dyLcuNVHO1OpS1IjJYB_2BKx3t16mBS_n6AU3TAMAns3uQgiXtEcBh5QoOaYsu0t_hRB6Wy0kdYlM-BkoIcxViWR6ZsxjFW2fOd0uG4BmC4rQzEtXApJsqF9LFI9rWbuh0w66HufxkgMfxN21n5zUdFtWgxeT5fK85lJbs1oaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
مجری:
اگر ما توان نظامی ایران را درهم کوبیده‌ایم، پس چطور آن‌ها همچنان موشک شلیک می‌کنند؟
🇺🇸
ترامپ:
آن‌ها همیشه می‌توانند موشک شلیک کنند. آن‌ها تعداد زیادی موشک داشتند و هنوز هم تعدادی دارند؛ هرچند بخش عمده‌ای از توانشان نابود شده است.
تولید موشک برایشان دشوار است. بخش اعظم تأسیسات تولیدی آن‌ها از کار افتاده، اما همچنان موشک در اختیار دارند. آن‌ها همیشه تعدادی موشک خواهند داشت، و ما [موشک‌هایشان را] سرنگون کردیم.
آن‌ها ۱۱ موشک به سمت ما شلیک کردند و ما تک‌تک آن‌ها را سرنگون کردیم. البته اجازه دادیم دو تا از آن‌ها رد شوند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/71448" target="_blank">📅 08:25 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71447">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a731a8039.mp4?token=TbiXA71URw-hZwb01Qgwh7kzxylzbmcUaq1sw1dOhFqLgFZmaHzDpp1Z2vxjgSH2HnWFQxZy8kJpWjvOJKb5Aj9FACKIJm4SmIy9VzaRAqBlenG44wqm8XvBcVscxSmAU6IruVYTZYGXazC1HV-95bPWMAbaTKdCr2UDThFOgTcoqP7Q5P9tMs_a-8bIhEG4Bj9wDR80Y5t8RmR25JasS_yb85XGgMkN7CfrAarUoN51FQCV7liAw1Uk1fInFpotblWq4ZaETP4qkLc7p9Tan8WNQNU3KHDSHqoaPwti_Nohlp8sVl_O8FvnLjQuTXUX8eQDQ49ZzXXv91IcW2usyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a731a8039.mp4?token=TbiXA71URw-hZwb01Qgwh7kzxylzbmcUaq1sw1dOhFqLgFZmaHzDpp1Z2vxjgSH2HnWFQxZy8kJpWjvOJKb5Aj9FACKIJm4SmIy9VzaRAqBlenG44wqm8XvBcVscxSmAU6IruVYTZYGXazC1HV-95bPWMAbaTKdCr2UDThFOgTcoqP7Q5P9tMs_a-8bIhEG4Bj9wDR80Y5t8RmR25JasS_yb85XGgMkN7CfrAarUoN51FQCV7liAw1Uk1fInFpotblWq4ZaETP4qkLc7p9Tan8WNQNU3KHDSHqoaPwti_Nohlp8sVl_O8FvnLjQuTXUX8eQDQ49ZzXXv91IcW2usyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
🇺🇸
پرزیدنت ترامپ:
ماجرا درست پس از انتخابات به پایان خواهد رسید.
نمی‌گویم چه زمانی، اما فکر می‌کنم درست بعد از انتخابات تمام می‌شود.
آن‌ها به‌سختی و با لنگ‌لنگان پیش می‌روند؛ در مخمصه‌ای عمیق گرفتار شده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/71447" target="_blank">📅 08:15 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71446">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dedfdd2dfa.mp4?token=ANhrSRm1U0K0ch45_3MDujA7770Eg2NS3uFXD3QhW_i723YULwOqyyP3LYlOIMVeutBVYVCJbZfMdo1Zl_HQthU49JnJqDyl-Cc1PUpxv2BKL6fHl_9MbXUTNpoRYx72lGpwMzFHNBCT_hCc8_YX_twYT6llmLLg60MxgZEAD19LMO60H7BiNY3Smmg600mlKAyjUAHNu5dJlHFnFouy_IDMtWtrYIUaeSvOqAu-EIqARDQT1_IJ1Pw_d4L7Eq6P4dvIHhL_RfM_U6TYPGEO6LBdR1flEM9IP6Ub9oXFRWXBvoFnez0TNJZLSIaaMrILzUfsp_Cbl-u3JEbHuTrcjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dedfdd2dfa.mp4?token=ANhrSRm1U0K0ch45_3MDujA7770Eg2NS3uFXD3QhW_i723YULwOqyyP3LYlOIMVeutBVYVCJbZfMdo1Zl_HQthU49JnJqDyl-Cc1PUpxv2BKL6fHl_9MbXUTNpoRYx72lGpwMzFHNBCT_hCc8_YX_twYT6llmLLg60MxgZEAD19LMO60H7BiNY3Smmg600mlKAyjUAHNu5dJlHFnFouy_IDMtWtrYIUaeSvOqAu-EIqARDQT1_IJ1Pw_d4L7Eq6P4dvIHhL_RfM_U6TYPGEO6LBdR1flEM9IP6Ub9oXFRWXBvoFnez0TNJZLSIaaMrILzUfsp_Cbl-u3JEbHuTrcjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
مجری:
اگر ماجرای ایران پیش نیامده بود، با خیالی آسوده به سمت پیروزی در انتخابات میان‌دوره‌ای پیش می‌رفتید؛ ۲۲۵ [کرسی].» آیا حسرتی دارید؟»
🇺🇸
ترامپ:
«نه، من به واژه "حسرت" اعتقادی ندارم.
آدم همیشه ممکن است کمی به کار خودش شک کند؛ چند نفری هم این سؤال را از من پرسیده‌اند.
اگر قرار بود دوباره آن کار را انجام دهم، دقیقاً همان‌طور عمل می‌کردم. من توانمندی هسته‌ای آن‌ها را از بین بردم.
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/71446" target="_blank">📅 08:00 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71445">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🦖
فردا، شکار شروع میشه...
🦖
• هر روز در TrexBet، بین ۲ تا ۴ عکس چالشی منتشر می‌کنیم که داخل هرکدوم یک Promo Code یک‌دلاری مخفی شده!
🦖
دو زمان، دو کد، دو فرصت شکار 1 دلاری.  18:30 → اولین شکار  20:00 → شکار دوم
🦖
• شرایط دریافت جایزه
🦖
فردا ساعت‌ها رو یادت…</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/71445" target="_blank">📅 01:35 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71444">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Woq7ojaT2qw5-7iOcTFJMKuNhf5xI5CxiQ2-oqtJzAo94BQUrizHfAtEZKEkHLZASrYaxXsZXuoWTczpYlJF1a04YsJSNr2m6qxxHo9jfdEljErjvt93cB6LKIEBjGyTdt1WISlitiGVFu9r-CqY7KVLYAVrHpkQh9MikLFLr8BxJdsiBNB3B6Uw5xagoQRiEIkG2YQajyGfAdqCj_jwm0fJvUGQpxIlljzzZkZ2H-TJg9Sl4HZbiqnTq9GgDt9fIodshmW95uhI0DybvYpvyyWXIMtWgCSX4S3YJ27ZpXjN1lw9ImA_yFHvQNRyrOfvljLDB1dAWRpqITKRRCXaXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
فردا، شکار شروع میشه...
🦖
• هر روز در
TrexBet
، بین
۲ تا ۴ عکس چالشی
منتشر می‌کنیم که داخل هرکدوم یک
Promo Code یک‌دلاری
مخفی شده!
🦖
دو زمان، دو کد، دو فرصت شکار 1 دلاری.
18:30 → اولین شکار
20:00 → شکار دوم
🦖
•
شرایط دریافت جایزه
🦖
فردا ساعت‌ها رو یادت نره...
ممکنه کدی که دنبالش هستی، فقط چند ثانیه با تو فاصله داشته باشه.
🦖
🦖
🦖
🦖
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/71444" target="_blank">📅 01:35 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71443">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U8VduBH5ixV8oBQoa2_sqIO0dIqlB5ZoT_nl6hC12GXKnGj4pUKm0PiAR8Dv6fgEwciOitBTIoOeFKCvN62rXhew-IgLwHoGSPd8CEbPWuyWeV18OToOmhUYd3bFCnE6P0gjpOEQg0qKZB3gTzmZ2U8OuHhzGoUVmmO20CLhnm-wS_xAu_lx4Zc17EGdSjG6xPVyR0t0e0Kw-RAfZ3T6qLgR91IWR2ruWoDtZv6mAwc7B6kmVLpjBuw2_hKNOnnaWvL75SYQNPTpZgIu9H4i3T5o1HDl9OrqJhyDk4i0bI-EHGKGCFPblAWNre0ud3w84yFqVTIjMx7jx58oHBJ3OA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💸
🛢
بهای نفت خام برنت به ۱۰۹ دلار در هر بشکه رسید.
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/71443" target="_blank">📅 01:19 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71442">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ied6cP_bzgzvHEze7M8l1MFGUDsDrBfZNFeytNPsTI0d7O05VoDW2HYCcuV7moUovkIV-Hbu7c7G7YxnyqLSYAsYgFlY-NvFfbhZvk8QMSVFq_cjysVS98IEfSGh5N5trXmNmDX6lQtqZlpE7lItSj9fNVyzN8K6nlU565KUCapPayBZgUZvbsZrXwVXrb8tRkT6Vg4BI6Tu7hcpvxQKKqfwWx7NdmfpONZnmZ0nbdH7n_nPZwc3Exf7-oQG7FyNHxXSKTUqERX642k7U0qV2DE7EGIGQuDcbfrN5-jo1yRIz0UuU5aney14Z_8U8tnnA-yVVHJdYm6GhCrwI5vnJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇾🇪
❌
🇸🇦
میدل‌ایست:امروز برای نخستین بار، حوثی ها خط لوله «شرق-غرب» عربستان سعودی را هدف قرار داد؛ خط لوله‌ای که نفت خام را از «ابقیق» به «ینبع» در ساحل دریای سرخ منتقل می‌کند.
تقریباً هم‌زمان و در حوالی ساعت ۱۷:۵۶ به وقت هماهنگ جهانی (UTC)، کانون‌های متعدد آتش‌سوزی در شش نقطه از مسیر این خط لوله شناسایی شد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/71442" target="_blank">📅 00:57 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71441">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J58H8SckyeclphSRpSA6R16dFn-YUeDkoZ6ftqNk7HqL0TgqZNIdKWTJWl1kCFHwVZg2EMnqR_cBWqVaHR7un92H5oxBBUu0YUTY0RFPZzVF1fI9bd8BW5yzmXs_s7S7v6foijTTujuT9bryKyu7Gv28MA4QTiIhbZeHhW2mBiUG6IKRkxBkIrOjUTSDFExAZigGOv1bMJu18q-lz02XZc6QVpQ0OgHwh7IW3Iahe-6gRK8XLSj6iwWS0mAiS-34TAOUUoTAAmRChUAMXfXGGevoZF1enW1KMuiCp7fnV2CfrjGDacpTLr9IKvz0GUtxoGrKtaUfvHzE6jRVm2wxOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⭕️
دو شناور در تنگه هرمز، در فاصله ۴ مایل دریایی غرب عمان، هدف قرار گرفتند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/71441" target="_blank">📅 00:36 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71440">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">⏺
🇮🇱
❌
🇱🇧
ارتش اسرائیل اعلام کرد که برای تخریب زیرساخت‌های تونلی در زیر ارتفاعات «علی طاهر» در جنوب لبنان، بیش از ۱۱۰۰ تن مواد منفجره به کار گرفته شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/71440" target="_blank">📅 00:28 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71439">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ae4183a669.mp4?token=Vox7wNW_dHagDpbyzMCaF7_aYPgcdKXAqFqfg1r6FNoMpwI2QLG6U3x9WoVkXoxvFkA2sf1KF0XSaAFER9OCSNbQzgCO1xGVA6YJ82UOz39-UvPveSJFN8wh9wQJhCvmDUiPEURngKiRZSFw28KHVzIKAzllUjbkZD22ZsK2juX28ynePWO3Ylb_A-EW1a_mQMyaFZmoq7LDDRrdMaSRoNHhrWu_Y8xTr8KqFEU5t_S5bf9hKY9Sp2IfcI00DimDfO4jSZLc5wz4gRWdDyAfwQfNN9Eywqj74j9OVDnsTlr-nVzq-6WrHYX0inevy1K8-OOpzDqll8qgjJkaFx2gUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ae4183a669.mp4?token=Vox7wNW_dHagDpbyzMCaF7_aYPgcdKXAqFqfg1r6FNoMpwI2QLG6U3x9WoVkXoxvFkA2sf1KF0XSaAFER9OCSNbQzgCO1xGVA6YJ82UOz39-UvPveSJFN8wh9wQJhCvmDUiPEURngKiRZSFw28KHVzIKAzllUjbkZD22ZsK2juX28ynePWO3Ylb_A-EW1a_mQMyaFZmoq7LDDRrdMaSRoNHhrWu_Y8xTr8KqFEU5t_S5bf9hKY9Sp2IfcI00DimDfO4jSZLc5wz4gRWdDyAfwQfNN9Eywqj74j9OVDnsTlr-nVzq-6WrHYX0inevy1K8-OOpzDqll8qgjJkaFx2gUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ویدئو دیگر از تخریب کامل پایگاه عماد ۴ حزب‌الله
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/71439" target="_blank">📅 00:12 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71437">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f4770f428.mp4?token=KrC7H60psR_RO8fLeOIfbuIHzli2hVIigX8oTl4I3fVEXphs-Fgu8HbivqMSZgzhGOBv7lpmlOaQwmgGbzCyxOll5YsTdKe25YBY7vsYq9z-0WIu--lzKO2ZzgHHBVqNpZcaw1EcUvhsBL7PLx3kbyTp74fFsc0D4abSMQfB2Ws50R9OQxaRp7e484Kk0K88sPM6oTUjqTj0-z0hWB8DWNuW2B9n8dRJIjGocsJ6hf9lS1QPysUhzo0yENigzu0-BYFyHkPY6hYy9YfQBd6sy5AdL4JwzXEemPYiHAarq2qvPueWu9I-2nns6wazMRPVNH19yjOTDotTIW4H5qarzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f4770f428.mp4?token=KrC7H60psR_RO8fLeOIfbuIHzli2hVIigX8oTl4I3fVEXphs-Fgu8HbivqMSZgzhGOBv7lpmlOaQwmgGbzCyxOll5YsTdKe25YBY7vsYq9z-0WIu--lzKO2ZzgHHBVqNpZcaw1EcUvhsBL7PLx3kbyTp74fFsc0D4abSMQfB2Ws50R9OQxaRp7e484Kk0K88sPM6oTUjqTj0-z0hWB8DWNuW2B9n8dRJIjGocsJ6hf9lS1QPysUhzo0yENigzu0-BYFyHkPY6hYy9YfQBd6sy5AdL4JwzXEemPYiHAarq2qvPueWu9I-2nns6wazMRPVNH19yjOTDotTIW4H5qarzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
🇱🇧
#فوری
؛ارتش اسرائیل عملیات تخریب تونل های زیر ارتفاعات علی الطاهر را شروع کرد.
تصاویری که لحظه انفجار تونل‌های زیر «ارتفاعات علی‌الطاهر» در جنوب لبنان توسط نیروهای اسرائیلی را در همین لحظات پیش نشان می‌دهد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/71437" target="_blank">📅 22:30 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71436">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/249279a367.mp4?token=oL0lmSImjC3Q-mYHmk6uuCprouuU9btUBNiNo-pDqsXa8bGkbt3AlZr5nXaId93x3dq37CFjVdfmxo106ej4K0xbnigrjXH4yfLV0wN8A7kyTJZ44wETocHjDqWA10GLDldCFuIhhsg76hTdcVn8HEfLyiF7LW_C1OVoUajJqlsU9wg9qdlQA1zK0uPuQetPINqaKaYUIPXQx1JrSs87UJ8AxPJeqHIGtOkcIW5LQHXDhOaL7PCl__tL7l24C3cLraWrZBaJmNkLnOELn6wBs_2DZxfnPxB7PHIFmHr6QYVaoRKE-Qgx7UFDVKW5urhixvxD081eraNXXGSTPVImnA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/249279a367.mp4?token=oL0lmSImjC3Q-mYHmk6uuCprouuU9btUBNiNo-pDqsXa8bGkbt3AlZr5nXaId93x3dq37CFjVdfmxo106ej4K0xbnigrjXH4yfLV0wN8A7kyTJZ44wETocHjDqWA10GLDldCFuIhhsg76hTdcVn8HEfLyiF7LW_C1OVoUajJqlsU9wg9qdlQA1zK0uPuQetPINqaKaYUIPXQx1JrSs87UJ8AxPJeqHIGtOkcIW5LQHXDhOaL7PCl__tL7l24C3cLraWrZBaJmNkLnOELn6wBs_2DZxfnPxB7PHIFmHr6QYVaoRKE-Qgx7UFDVKW5urhixvxD081eraNXXGSTPVImnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🇮🇱
#فوری
؛نخست‌وزیر نتانیاهو درباره ایران:
رئیس‌جمهور ترامپ امشب اعلام کرد که ایران بار دیگر در تلاش است تا به سلاح‌های هسته‌ای مجهز شود. این سخن درست است.
پس از آنکه ما توانایی فوری آن‌ها برای تولید بمب‌های هسته‌ای را از بین بردیم، آن‌ها دوباره دست به کار شده‌اند.
من اینجا، در کنار «دیوار ندبه» و در آستانه «روش هشانا» (سال نو یهودی) به شما قول می‌دهم: تا زمانی که من نخست‌وزیر هستم، ایران به سلاح هسته‌ای دست نخواهد یافت.
هم‌زمان، ما در حال ضربه زدن به محور ایران هستیم؛ نه تنها ضربات سنگین در نوار غزه، بلکه در لبنان نیز. ما ارتفاعات «بوفورت» را درهم کوبیدیم و اکنون در حال نبرد بر سر ارتفاعات «علی طاهر» هستیم.
اقدامات بیشتری در راه است.
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/71436" target="_blank">📅 22:21 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71435">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">یه بوهایی میاد، مثل اینکه آماده دارن آماده می‌شن تا دوباره مراکز هسته‌ای ج.ا رو بزنن
#hjAly‌</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/71435" target="_blank">📅 21:18 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71433">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P4NGupTLCIGPgVUMQLbNSYD3zGBIzEQWlsqu1GpRISqckbjWqM2D3GW2IKJt6MFAhvOMVTvZd9XqlHVIR8zV3iVwlbaDgr32VpGXt94ixt1Gjy_fXOEAH_Jvtag4fzNkJTXq-9JBxRXOVnIqsPxFyICFNB_mw2-PGIFyWGxOac-Bcxna1mbEJZxdRou6zY-daGvZu1d0xUMGwRNOrGMbyT6Z8kR2hjmjI4H5rCboQ_y0W6PpKFmEKiy6xF_M0KnIPJCDzCjac8ZXZj2bu5mPrMnazEAruLBnb2lAU64ILf8DTHVYg6EaDCrVuFJr4RGALsbMVmyfpiZdObxOV6s-8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4d882666df.mp4?token=I7GUFwOfE0ZDOYAQ06AnLjNTaQIZamutAveJtJMc7QEeu9RfBXe0R4KMGvtcJJ5sSE51VImKnIk7TG_7NWOUrCWjctMFeDb4dIB2zwKrEmzsbm5p1SLheQ8S_YXNraZE-BffohvDz-lq11FW0bUNyunzitN-guiK_awkYp8ltrLVndgCciL4LR292RO-j2ow4scG9aownqMtl9qbdpBLBiN0WSVab8QJi1VATu_EQ1ppCypfgH7qF7FcTAU-mnZLNokp7vmRiOPFbW3AC1oU2Q_5FGfbrZ4Bfmc-43YnsJ-NUr3oytnS2JxZDTheQKxRRwWHW6h5ZUNGPGBURjtw_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4d882666df.mp4?token=I7GUFwOfE0ZDOYAQ06AnLjNTaQIZamutAveJtJMc7QEeu9RfBXe0R4KMGvtcJJ5sSE51VImKnIk7TG_7NWOUrCWjctMFeDb4dIB2zwKrEmzsbm5p1SLheQ8S_YXNraZE-BffohvDz-lq11FW0bUNyunzitN-guiK_awkYp8ltrLVndgCciL4LR292RO-j2ow4scG9aownqMtl9qbdpBLBiN0WSVab8QJi1VATu_EQ1ppCypfgH7qF7FcTAU-mnZLNokp7vmRiOPFbW3AC1oU2Q_5FGfbrZ4Bfmc-43YnsJ-NUr3oytnS2JxZDTheQKxRRwWHW6h5ZUNGPGBURjtw_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
نیروی دریایی سپاه پاسداران انقلاب اسلامی  اعلام کرد که یک فروند «سیل‌درون» (Saildrone) — یک شناور سطحی بدون سرنشین (USV) که برای نظارت و شناسایی دریایی به کار می‌رود — را در ورودی تنگه هرمز هدف قرار داده است.
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/71433" target="_blank">📅 20:54 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71432">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🚨
بلومبرگ:
آژانس بین‌المللی انرژی اتمی می‌گوید فعالیت‌های جدیدی را در سایت بسیار مستحکم کوه پیکاکس ایران شناسایی کرده است، اما هنوز هیچ مدرکی مبنی بر آنچه در داخل این مجتمع زیرزمینی اتفاق می‌افتد، ندارد.
رافائل گروسی، رئیس آژانس بین‌المللی انرژی اتمی، گفت بازرسان به این سایت دسترسی پیدا نکرده‌اند و به تصاویر از راه دور متکی هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/71432" target="_blank">📅 19:45 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71431">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d3ebe5e9d2.mp4?token=UM5YYHL8uskSjAhGnd_HkuptfP8CD0MPcgb0Y5Zn_8A66JCT9_a4OrGrqRGZuQP12n_aRfwSJboW0E7wnBujAuKtG9G9bgTkMm1VF4Dd_vdweNKW_kuGnZC_9T9-Bzhx0LAJ8qgrDKQC0yidUHLOjzdyqlAaesXSFqVttoJgNusRnnOAZp4I2wnkYVuP3dudLLoLeqbs6W2AK9iAgd0Y-PjJi4ldoKD3_SZ3aMS9PqXNw7swI9V4mnyC7u0HGP224rL3f80fyZDEYn8BWDuM29wMt-PCoDLlsQp06CQtQjnv6sVCEe2UUlb3PrOApXH0tswnwVeFOhPvnvBi0DGd8KZwfMDRFqfGz8iKR3eQi7RiwPkycqgV-9SysyzRh4-RX5g4ID5BVJmYk6Msi2Fd-a5BPrTD_2FO6vX_yHBeUwb_d-KEIQajBxdfbLjRQ8k1zfdQY-vtk5glIhTWNRL1mIlElhjGKJdS7Hk8kWyAR-YX4_MPgsV2jLbhlhxo5FKaAEt764DS9qYG_ZG2xSlYEHeJSKVwPKo11k4iLeWYbWV5mKX5w48eY1qqCbJcxwShXiCF8CCtwV2KCl-HsS6e5MrLzlfWkVvYGutDpyOCHoLzb0eVlYeilaabQaTDwqzEgm3wNmQHbkKS2zOhsu4BRhId17dVXLAVlHKc4ZLAYnM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d3ebe5e9d2.mp4?token=UM5YYHL8uskSjAhGnd_HkuptfP8CD0MPcgb0Y5Zn_8A66JCT9_a4OrGrqRGZuQP12n_aRfwSJboW0E7wnBujAuKtG9G9bgTkMm1VF4Dd_vdweNKW_kuGnZC_9T9-Bzhx0LAJ8qgrDKQC0yidUHLOjzdyqlAaesXSFqVttoJgNusRnnOAZp4I2wnkYVuP3dudLLoLeqbs6W2AK9iAgd0Y-PjJi4ldoKD3_SZ3aMS9PqXNw7swI9V4mnyC7u0HGP224rL3f80fyZDEYn8BWDuM29wMt-PCoDLlsQp06CQtQjnv6sVCEe2UUlb3PrOApXH0tswnwVeFOhPvnvBi0DGd8KZwfMDRFqfGz8iKR3eQi7RiwPkycqgV-9SysyzRh4-RX5g4ID5BVJmYk6Msi2Fd-a5BPrTD_2FO6vX_yHBeUwb_d-KEIQajBxdfbLjRQ8k1zfdQY-vtk5glIhTWNRL1mIlElhjGKJdS7Hk8kWyAR-YX4_MPgsV2jLbhlhxo5FKaAEt764DS9qYG_ZG2xSlYEHeJSKVwPKo11k4iLeWYbWV5mKX5w48eY1qqCbJcxwShXiCF8CCtwV2KCl-HsS6e5MrLzlfWkVvYGutDpyOCHoLzb0eVlYeilaabQaTDwqzEgm3wNmQHbkKS2zOhsu4BRhId17dVXLAVlHKc4ZLAYnM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
جورج دبلیو بوش درباره افغانستان:
این باور وجود دارد که همه خواهان آزادی هستند؛ و ما این را در افغانستان دیدیم.
برخی می‌گفتند: «خب، آن‌ها نمی‌خواهند آزاد باشند؛ آن‌ها... می‌دانید، اصلاً تفاوت را نمی‌دانند.»
البته که آن‌ها تفاوت را می‌دانند.
دختران جوانی که برای نخستین بار در زندگی‌شان به مدرسه می‌رفتند، تفاوت را درک می‌کردند. زنانی که پزشک و استاد دانشگاه می‌شدند، تفاوت میان یک جامعه آزاد و یک جامعه استبدادی را می‌دانند.
و متأسفانه، آن زنانی که در مسیر شکوفایی کامل استعدادهایشان گام برداشته بودند، دیگر فرصتی برای تحقق آن پتانسیل کامل ندارند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/71431" target="_blank">📅 19:40 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71430">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71430" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/71430" target="_blank">📅 19:39 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71429">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ViG2cUxSiwRKeWiZFzu5qGwlwcGH41aDUak5KaAJw1bmz66ggj6ls0PpaQUlMeBmn70Ciu5ouVAwZYY-5I6FBXWeQ-4SsZO58nadYQCLKZ3WJjeuw2fm2LfQEiq48IHcJjiUydtpGoF6cYx6HixZFAgOMbGs1l2hzHKyG1EOAN0MlT2XQNWPNOu46li_Rvvh-OcRgozk8-7gnBYDFI-VU5L0vacw3Os7Wrg-GIbuY4_LiUPMJdMh_jkUf_WplHCYgmPaK8h1q9U6-l-Llgl6AZyi2kfbncsLuthzgnC5THO91FhprpLxvgup6Bx5EH_ZvAqLRJnaPIduAgvb18aZaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
فوتبال اروپا امشب دیدنی‌تر از همیشه!
🦖
بازی جذاب صباح
🆚
منچستریونایتد را در سایت بین‌المللی
TrexBet
پیش‌بینی کنید.
📊
نگاهی به آمار ۲ تیم در تقابل‌‌های اخیر:
صباح: ۵ بازی, ۴ برد, ۱ شکست و ۱۳ گل زده
منچستریونایتد: ۵ بازی, ۱ برد, ۲ تساوی, ۲ شکست و ۱۰ گل زده
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
🦖
🦖
🦖
🦖
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/71429" target="_blank">📅 19:39 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71427">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd5897a7d3.mp4?token=UV8_8OC5LcJblpM72aIVdQwKBUH5X79JAH1XhcfSBiDPASlkiEd47EhzpQdW2L3PWRHtU0qwcUnRf1IqbxFgu_h8ESQrmdDzwipl_V196oTdIrxZtx8qKW1sr_9ubI-sQ8MBsCsPbYPWraaz6r3KEglBWSPVB1mEEJLmyo3_IzCaAO-sQjGSXpAJK96STu0WaEe2JFRWxUsTgiAw4d6YkG0aq9UKSwo9066YpMC9BS1gvznP-yKGF4bCdhoACJMn8DLUGU5tBynQzqPCW96LvIroLHWB13zZqQQ8S0Dlchdn47JSLVEFwfSRsF39E01Zns3nMfKxs78wcpOOZl0k5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd5897a7d3.mp4?token=UV8_8OC5LcJblpM72aIVdQwKBUH5X79JAH1XhcfSBiDPASlkiEd47EhzpQdW2L3PWRHtU0qwcUnRf1IqbxFgu_h8ESQrmdDzwipl_V196oTdIrxZtx8qKW1sr_9ubI-sQ8MBsCsPbYPWraaz6r3KEglBWSPVB1mEEJLmyo3_IzCaAO-sQjGSXpAJK96STu0WaEe2JFRWxUsTgiAw4d6YkG0aq9UKSwo9066YpMC9BS1gvznP-yKGF4bCdhoACJMn8DLUGU5tBynQzqPCW96LvIroLHWB13zZqQQ8S0Dlchdn47JSLVEFwfSRsF39E01Zns3nMfKxs78wcpOOZl0k5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
🇾🇪
تنش‌ها میان نیروهای تحت حمایت عربستان سعودی — یعنی «نیروهای ملی» (NRF) و «نیروهای امنیتی ملی» (NSF) — و نیروهای جنوب یمن که پیش‌تر وابسته به تشکیلات جدایی‌طلبِ منحل‌شده‌ی «شورای انتقالی جنوب» (STC) بودند، رو به افزایش است.
فرماندهان جنوب یمن مسیر عقب‌نشینی نیروهای NRF و NSF را در کریدور جنوب‌غربی «عدن-لحج-تعز» مسدود کرده و از ورود این «نیروهای شمال یمن» — که کاملاً مسلح هستند — به قلمرو جنوب جلوگیری می‌کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/71427" target="_blank">📅 19:32 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71426">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uZwI3FEv41GdVVb_3Wj91mWn8_YK31hSBhKkL0GSg89kENuM4d15mMLZREKTPi69ph-xUNiPAVRunahPBiM7c0blzBJl-WD1s7e-C0X9HldUnmhuJK0z3GwuA3sQ3n7kRNzoX1IPhFcSVCXEVgxJ7DczeFDghsEgBp3SAvM1UZdJxvApBlgG7Ty2fA9vHG2-1evJhSjB7ljQOfOmA2Tx4rtk-5CiU_Syy5K1m9slbMMCvQPDWyBRBAcmcAEt4z7dbr0XONylMN3ylQpWbW_pF1LYwO9PSqGVJU81i7Zn6k7jGWFb2dpbaa5LRmPXGTHLSy3-gu-juIR4HJT69R9R5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
🇨🇳
🗞
به گزارش رویترز، ایران از یک سازوکار محرمانه و شبیه به تهاتر برای تبدیل درآمدهای نفتی به اعتبار جهت خرید کالاهای چینی استفاده کرده است؛ اقدامی که به تهران در دور زدن تحریم‌ها کمک می‌کند.
طی سال گذشته، مبلغی بین ۲ تا ۲.۵ میلیارد دلار از طریق یک «سازوکار ویژه» (SPV) جابه‌جا شده و صرف خرید اقلامی همچون دارو، وسایل نقلیه، تجهیزات مخابراتی و — دست‌کم در یک مورد — تجهیزات پدافند هوایی به ارزش میلیون‌ها دلار شده است.
این سیستم شامل نهادهای مرتبط با چین و ایران است که مدیریت درآمدهای نفتی را بر عهده دارند؛ بدین ترتیب که حدود ۷۰ درصد از وجوهِ تحت مدیریت شرکت چینی «چو‌شین» (ChuXin) به پروژه‌های زیرساختی اختصاص می‌یابد و مابقی آن برای پرداخت به تأمین‌کنندگان چینی، به آن سازوکار ویژه (SPV) منتقل می‌شود.
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/71426" target="_blank">📅 19:01 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71425">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🍏
اپل از نخستین گوشی هوشمند تاشوی خود با نام «آیفون دو» (iPhone Duo) رونمایی کرد.
این گوشی در حالت بازشده، باریک‌ترین آیفون ساخته‌شده تا به امروز است و نمایشگری ۵۰ درصد بزرگ‌تر از آیفون ۱۸ پرو مکس (که به‌تازگی معرفی شده) دارد.
قیمت مدل ۲۵۶ گیگابایتی آن ۱۹۹۹ دلار تعیین شده و عرضه آن از ۲۳ اکتبر آغاز خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/71425" target="_blank">📅 18:15 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71424">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/VqeJI_FQ4QyCSq7ir3giEWnoGmw7uw_TeBlAb5IlHJk9pl8ulgXe2S1nmoqLQ2h7Bv1gK5MEKi1d-P_-Vqs-pzDFmnLlvaH9SA3PMN-Bknos6h3XXlIIsMJEcwcjVIFHiChSjN0xDt2dK9JNiwChR66wFlxz3AiSIp1J8gYCkz6-Qw9WybtQF9fRoGzHKpYGl21zwj5TDHVLIlD7ZhdU9FUdmH8Q0r-J_1949IV4G_O0olRb9ADE6uREohslPREz5HK5im2eR7aXXo0-w9imSNRC3SSU-wfkWTk4iA3I0P5hXI3tOM4Eij0qcg2CBMaboVXYdM7xNfKD99-H4JASuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شروط عجیب پدر عروس برای ازدواج
😳
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/71424" target="_blank">📅 17:31 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71422">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GEnOckDgqA4C6ts33EoifNAJ1g69qv4edmfNN2HFE2E0cD0a9RlC8yPABvMPIWicPkQhCuDSjAVTwXp1mBERDJkXqtZt_3gZGNvYfieuZ7kmijAr0LRkPzvzxhn5tWiIhmivWqLe5yAyf_WctFQE7d9pTzDHCoxE5G87yL51R_Qb1UyLWzIiqYm0mi6P-0Ua3yJbMmOVapmbHQLhzxlheXhO3JeVPi2lrNIJfYPTC7OI1moSfW-5udgSlBRg_MTvtY4Sdq99jE7UugGPyC959EdLUtE6JNvRoE6NGwe383m5qtx2AmuvglH_dR_hzeEfhQ31DqcVxj_AzI4rjsf2Qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0dfa56bc26.mp4?token=mj5_vIPWt7eru1EhPOyMcDrJ3xhHEsy35Dsf71kht84XpOEDx23hRkkyO5qT8Up5E36jsX-DCCBU4bGAC_t313QMPiae5gkTRK0v9DY6AeA4bG3qi0OBrIOMH-rhbKV-mD8GQMbZ5WuAaTnCgknImmWpxhmeYvzO7K9If7Ahh2OL8toSpz0Bx7rU5VqKAXOu7iqlXbKdWcePkrvgi-KiZGUlq650WoarJFskid_zH4zA7U2BITCrHECxLcG1Iz06xM-GPKj7UuKycZ0Ou_QKqxnOD_OO7fnocHa9177RcGr-U5K0_l87Xa1O7yuK7sjwKSA_DRAg26mFn6tXRNmZVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0dfa56bc26.mp4?token=mj5_vIPWt7eru1EhPOyMcDrJ3xhHEsy35Dsf71kht84XpOEDx23hRkkyO5qT8Up5E36jsX-DCCBU4bGAC_t313QMPiae5gkTRK0v9DY6AeA4bG3qi0OBrIOMH-rhbKV-mD8GQMbZ5WuAaTnCgknImmWpxhmeYvzO7K9If7Ahh2OL8toSpz0Bx7rU5VqKAXOu7iqlXbKdWcePkrvgi-KiZGUlq650WoarJFskid_zH4zA7U2BITCrHECxLcG1Iz06xM-GPKj7UuKycZ0Ou_QKqxnOD_OO7fnocHa9177RcGr-U5K0_l87Xa1O7yuK7sjwKSA_DRAg26mFn6tXRNmZVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
⁉️
به گفته تحلیلگران CSIS، تصاویر ماهواره‌ای امسال «افزایش آشکار فعالیت‌های ساختمانی» را در کوه عمیقاً مدفون پیکساکس (Pickaxe Mountain)ایران نشان می‌دهد.
آنها ارزیابی می‌کنند که این سایت پوشیده از گرانیت «احتمالاً» به عنوان مکانی محافظت‌شده برای کارهای مرتبط با هسته‌ای، احتمالاً محل مونتاژ سانتریفیوژ، غنی‌سازی اورانیوم یا سایر فعالیت‌های «مرتبط با سلاح‌های هسته‌ای» در نظر گرفته شده است.
این تحلیل افزایش فعالیت جاده‌ای، ورودی‌های تونل تقویت‌شده و مرتفع، جاده‌های داخلی آسفالت‌شده و سایر کارها را نشان می‌دهد که نشان می‌دهد ساخت‌وساز از حفاری به سمت توسعه داخلی تغییر کرده است.
اطلاعات اسرائیل حاکی از آن است که ایران می‌تواند سانتریفیوژها را به آنجا منتقل کند، در حالی که ترامپ اخیراً هشدار داده است: «ما ممکن است خیلی زود پیکساکس را بزنیم» و افزود: «ما همه کسانی را که در حال حرکت هستند می‌شناسیم.»
پیکساکس حتی برای سنگین‌ترین بمب‌های متعارف سنگرشکن پنتاگون نیز بسیار عمیق دفن شده است. سی‌ان‌ان گزارش می‌دهد که ایالات متحده برنامه‌های حمله عملیاتی برای این تأسیسات دارد و به مطالعه راه‌هایی برای حمله به سایت‌های عمیقاً مدفون ایران ادامه داده است.
چند روز قبل از شروع جنگ ایران، پنتاگون همچنین یک قرارداد اضطراری ۱.۲ میلیون دلاری برای آماده‌سازی در یک مرکز آزمایش زیرزمینی گرانیتی در محدوده موشکی وایت سندز (White Sands Missile Range) صادر کرد. منابع به سی‌ان‌ان گفتند که این کار با توسعه و آزمایش قابلیت‌ها علیه عمیق‌ترین تأسیسات زیرزمینی ایران مرتبط بوده است.
ارتش به‌طور جداگانه در حال توسعه یک «نسل بعدی نفوذگر» است تا جایگزین نفوذگر مهمات عظیم مورد استفاده علیه سایت‌های هسته‌ای ایران در طول عملیات میدنایت هامر (Midnight Hammer) در سال ۲۰۲۵ شود.
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/71422" target="_blank">📅 17:03 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71421">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e8709946e.mp4?token=QAZczl_cLRDyTG3q4DXs9sHuRss1y6edXS2RCtv6nJPsWe7tZXolpA7eSHXSeRNHTwYf9ds3nlUGt4r5fvTucvmbIEQXnv1tpbrl8x3A5qAIHj0eI9JkawySCws_8Gwcot2aEVvGW7496tCG-qa-ngACse6Zmo3sniM_vC_GA3Qi1Zhuq2VZbjgbFShfJKGO9Mh0FzuqQWJKE601EPVrfq51mOqYyUv7unCMPIZQBSFxJ8YEcNYP947ELZjgWB5gjCTp0PnITw26Eqz86PldTwkU6d06TCaXkiTegqf06Sx4hz8bWBGC31Yo_RVi8MuYL5ndTmwqtwNkdPLJOZ6Opg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e8709946e.mp4?token=QAZczl_cLRDyTG3q4DXs9sHuRss1y6edXS2RCtv6nJPsWe7tZXolpA7eSHXSeRNHTwYf9ds3nlUGt4r5fvTucvmbIEQXnv1tpbrl8x3A5qAIHj0eI9JkawySCws_8Gwcot2aEVvGW7496tCG-qa-ngACse6Zmo3sniM_vC_GA3Qi1Zhuq2VZbjgbFShfJKGO9Mh0FzuqQWJKE601EPVrfq51mOqYyUv7unCMPIZQBSFxJ8YEcNYP947ELZjgWB5gjCTp0PnITw26Eqz86PldTwkU6d06TCaXkiTegqf06Sx4hz8bWBGC31Yo_RVi8MuYL5ndTmwqtwNkdPLJOZ6Opg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
عباسی معاون وزیر راه و شهرسازی دولت سیزدهم:
آقای رئیس‌جمهور!
مگه نمی‌گید هرکی می‌تونه کار کنه بیاد؟
من می‌تونم
کجا بیام؟
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/71421" target="_blank">📅 16:31 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71420">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4aea684770.mp4?token=cdv6XRs3c1TIpHiH-1yP25z31pOiQbYm4i1XphHX0-uds7R9taBcU_0YPNf7EeUOyM_sVEkw0Funp_dsCZpW6AVjJJyMi7GO_bvzK5pZn1i6ogSIQSSVeL-rVv9MYY3W-1Hdq9gzaKnc76tfFIirIUOFz4cEVMt5Y_ZZfnqoB_4zgKAh0i2NUJWtSYfcfv01ITgFZzf5hNX1sw_YnPMlI4r9iHM2XNt-m4REHqEQD9xs70JFpLlQCFI7xxrJiZ7CT_opG5sd98FYalmXWy5d8Fo0-lJqF5LH2EvuUhj-4oeh5kX7L0AFLwC2QirCGHTSXvNCUDu-9NoF4fgXg5BsXzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4aea684770.mp4?token=cdv6XRs3c1TIpHiH-1yP25z31pOiQbYm4i1XphHX0-uds7R9taBcU_0YPNf7EeUOyM_sVEkw0Funp_dsCZpW6AVjJJyMi7GO_bvzK5pZn1i6ogSIQSSVeL-rVv9MYY3W-1Hdq9gzaKnc76tfFIirIUOFz4cEVMt5Y_ZZfnqoB_4zgKAh0i2NUJWtSYfcfv01ITgFZzf5hNX1sw_YnPMlI4r9iHM2XNt-m4REHqEQD9xs70JFpLlQCFI7xxrJiZ7CT_opG5sd98FYalmXWy5d8Fo0-lJqF5LH2EvuUhj-4oeh5kX7L0AFLwC2QirCGHTSXvNCUDu-9NoF4fgXg5BsXzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
حامیان حکومت این شکلی موافقت خودشون رو با قطعی برق و افزایش قیمت بنزین، دلار، طلا و گوشت نشون دادن:
تو تاریکی می‌نشینیم، ذلت نمی‌پذیریم.
بنزین رو کم میگیریم، ذلت نمی‌پذیریم.
دلاری گوشت میگیریم، ذلت نمی‌پذیریم.
مهریه کم میگیریم، ذلت نمی پذیریم.
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/71420" target="_blank">📅 16:02 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71419">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1669b7ca35.mp4?token=F108mBlAueuh5CdVpr_f05P0ZZ9RQxCVICjMtUAFzqz6bdxzuYz_dUPIsulPxH1GFWGKD4T9JNmwtnuNB4N4g2OsPyOISIYFbqp53S1Wb0sDsghxUQmaM_2ZYPpFO0xOXH-lKSeeDx8ULFhUKaVbASl3f1FXke00jCADrckiLQSdSYy187Mw255wOkFO5cUtBT1zor2o3Thsj5xZMcq6AJq3Y5OlQqBAABTUhp0IwVWpwiEqR9FM0N47mtNsz4wczUbS6ET1JIunGg3C4AHzGjq3EoWFsK7FfX0J-huq-4ILYNynJY8VvAUKaH7mxJRcNoZWBRIDJ2WeuzRIy0mCXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1669b7ca35.mp4?token=F108mBlAueuh5CdVpr_f05P0ZZ9RQxCVICjMtUAFzqz6bdxzuYz_dUPIsulPxH1GFWGKD4T9JNmwtnuNB4N4g2OsPyOISIYFbqp53S1Wb0sDsghxUQmaM_2ZYPpFO0xOXH-lKSeeDx8ULFhUKaVbASl3f1FXke00jCADrckiLQSdSYy187Mw255wOkFO5cUtBT1zor2o3Thsj5xZMcq6AJq3Y5OlQqBAABTUhp0IwVWpwiEqR9FM0N47mtNsz4wczUbS6ET1JIunGg3C4AHzGjq3EoWFsK7FfX0J-huq-4ILYNynJY8VvAUKaH7mxJRcNoZWBRIDJ2WeuzRIy0mCXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
رقابت رژیم جمهوری اسلامی با اپستین در کثیف بودن:
یه مرد ۴۲ ساله دختر ۱۴ ساله رو به عنوان زن سوم صیغه کرده، بچه حامله‌ست است و داره سزارین میکنه
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/71419" target="_blank">📅 15:31 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71417">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e97f71ba05.mp4?token=UF48A3rWIonNXknFHBt3x3icjjwu7HPrfTeqYY_LHBe4oQpfgbFQ6Y5VBs4-mRij6XyY4vmeqPtBzpV7rBS_bnNoLIrePEFbCIPwFZJotTMGpSZ6hmbeTMrJdZlIaM6kDSlyuPmEdf9n_DGB2_G7ujcbqG2D9X5nuLmJG6Zyl71Fbw7NDKlaFANGvTSbqr4C6RLLQDfxbttOkfNZCT4chtoKG5DElvStLvgUFkYNuMKeAeWCuAHhUF-Rhlgr8gh3iV_3bgnxO-dYhPExxrPwdpoNg_KkIxorbeUxeU_DLwTfmZ0PIvDQU28XPQbLNa8BmnVkuYT_xPCy1RNw7DQs2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e97f71ba05.mp4?token=UF48A3rWIonNXknFHBt3x3icjjwu7HPrfTeqYY_LHBe4oQpfgbFQ6Y5VBs4-mRij6XyY4vmeqPtBzpV7rBS_bnNoLIrePEFbCIPwFZJotTMGpSZ6hmbeTMrJdZlIaM6kDSlyuPmEdf9n_DGB2_G7ujcbqG2D9X5nuLmJG6Zyl71Fbw7NDKlaFANGvTSbqr4C6RLLQDfxbttOkfNZCT4chtoKG5DElvStLvgUFkYNuMKeAeWCuAHhUF-Rhlgr8gh3iV_3bgnxO-dYhPExxrPwdpoNg_KkIxorbeUxeU_DLwTfmZ0PIvDQU28XPQbLNa8BmnVkuYT_xPCy1RNw7DQs2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیو وایرال شده از مراسم ازدواج فوق لاکچری «سامان گوران» بازیگر؛ کمدین و مجری صداوسیما
سامان گوران ۲۶ مرداد ۱۴۰۴ در صداوسیما: نتانیاهو از موتوری جنس میگیره که میگه برنده جنگ شده. نمیزاریم آب خوش از گلوی اسرائیلیا پایین بره.
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/71417" target="_blank">📅 15:01 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71413">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KWX-VnG2JNtGqwsJFsivZbrZBgGkAAl4HjJu5KHPiR6278XKxInSIX3xQP9LJ_QTh_agGGkCuAs2_o56mZ7cPPAGmsa2K2lB0I5IcXlSUJOo9-1nWPZCEW2cd0tffK-b0OHquYxkB3rcpUoiebVj-OLNj8ATqBG9q2esd54EEDRwLAyTKlzFlkFp0nZsgs85jthfcrN8gdXEiSp4cjt5-rWB-tbigYxd1rPaSUs0ehwUc3sZeY8gEG4ax2J3HWYqhWL-jC06pA9QYlZtk2ZtrfbKNhoRXBUxpMuUDhWa8Q0xCyO2r3jgqpIYsp0BtdUPvYYoL2OkRS-XqBgtFmN6Mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JIc2nkm2b-_PV2AAQKKZVpons7BtPjvzef1XRva9vPcGHc1NtFiXy7-Y67L9ay6LM-u6I0XLlPvcPVwaJB5CIDGJvjEJ7U2_64Wwg75FcF8aIAP3vFAtSOZunnDyovstVJi38Ae_2vnRMR5VKkSjHTY7oV_Ve4Je9dkxqmQs03TP7XzVvLERigXPD34FZ_TalUxNcl1dgbIgGNweaxggR7eFUMh24FAhGkWO-Omcz04i9L9iGu8Pq1T4iZ7vUrAXSdUXKM2O8w1z1cqslgSfZR-lKEirQHgBiOTV3P7GvFwQGwN3XDYT_7ljaL3GopXFBzvZVRwEgAQiC8ZOKBuUiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Trq6mkDnhRYAGVP0Ir1WdO2_ecJAPHx-9zL_SyJ4ZTbEP4JkzNvg06WLlb52E8hX8dl2W73xbVMBnScmuPKfuXG0m5JtRkWRvaZVTbhR0q2xZluZ_S3cLDPEvI-PdMc_9ykqGnzRgyw0eWJsK60aE8wEpYu7pt5u48KMMfF3ToUlKy60go6jRmKAwIODVN4vn_gfFeoP6DJRLdippXoWI4ZCWczT8bMn8PQXpl5qAA_pwFZyXA-Zqxk-XODvMiQm8-OY1UhVQAroNhtDRKHG8yz8eqGkOe-oQrbF78ejcwaSKnMXF4IwSdGDE6XzVd-nwjfLCbkhUqjW9WQwa3XF6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/b_YYU8Q8pitI-pKhskhRx_djwg5ah4GcZNtOqo4QICQa_UYy1OwFSb5kky1A4iLJ6wouNTqcrWG0fnVw-tDUonJsoyoOWFdbklCKZIn6mOzuwEEwzMhcLL_MeaF0VTdDIF-k8G6_w3MQAeFt_cHSzb0TiUsk-RC5zw9xP3x7-g8Ny9OVp2iycviYBGp4BriIs6gcBpfC1-5m4uB4Mk-RIKqwUKCZ--HNBBpe9VfdXfUm5dZrZFytsKpzoY1Fh7HN2EASCmLwwvwwfb6W6TfZzDVIr9h1Zp-2fPB2xqU6LB3JB3dKIHZ54o6D5Sa0JLv3MebnUa5t6uUujONGay2mIw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇯🇵
👀
شب‌های ژاپن هم قشنگه
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/71413" target="_blank">📅 14:32 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71412">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63d4414bb2.mp4?token=tL6xbWRQ5WziLSHVNObXW21KD4OCAzF7XwTHSJeMWHE6vxD-1fjP5sB2MVDHeK4YB0JmhhLT18CgqhOCgtTb7ca18qF64sQpa-RVEa1W3pxORLZ0pSe9TOr8BCy6FMQtREmjujN5wVaZpDOEtwxeWqB_v-WmZRRiCRXfcAtpy31nf0MotBDc215mZS9jGo6umJbXY48Fmg0H9DXRP5Y-uS0IBjDYGOJPNiMy9FdWQ6dd2sHN8bdBiaCKvQM7tnBc8rx2Y6BzdVE6UetSLVw3BKnqgZJTQpY-H1ASFQQC9KyAhIis7NujfNtJNC93LhI3Zc15FrXJpNdg1bhrU5W3Ww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63d4414bb2.mp4?token=tL6xbWRQ5WziLSHVNObXW21KD4OCAzF7XwTHSJeMWHE6vxD-1fjP5sB2MVDHeK4YB0JmhhLT18CgqhOCgtTb7ca18qF64sQpa-RVEa1W3pxORLZ0pSe9TOr8BCy6FMQtREmjujN5wVaZpDOEtwxeWqB_v-WmZRRiCRXfcAtpy31nf0MotBDc215mZS9jGo6umJbXY48Fmg0H9DXRP5Y-uS0IBjDYGOJPNiMy9FdWQ6dd2sHN8bdBiaCKvQM7tnBc8rx2Y6BzdVE6UetSLVw3BKnqgZJTQpY-H1ASFQQC9KyAhIis7NujfNtJNC93LhI3Zc15FrXJpNdg1bhrU5W3Ww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
یسرائیل کاتز وزیر دفاع اسرائیل:
به مناسبت سال نو یهودی، می‌خواهم برای جامعه یهودیان ایران سالی نیکو را آرزو کنم و برای آنها سالی خوب و امن آرزو دارم. شما بخشی از تاریخ پرافتخار یهودیان هستید و همیشه در قلب ما خواهید بود.
و برای مردم ایران آرزو می‌کنم که در سال آینده، ایرانِ آزادشده از سرکوب و استبداد را به خانه خود تبدیل کنند.
با توجه به این احتمال که به دلیل خفگی اقتصادی و فشار سنگینی که ایران تحت آن قرار دارد، تصمیم بگیرند علیه اسرائیل اقدام کنند، به رهبری ایران هشدار می‌دهم: هر حمله‌ای به اسرائیل، به هر دلیل و در هر مکانی، با پاسخی قدرتمند مواجه خواهد شد که ایران را با ضرباتی سخت‌تر از هر آنچه تاکنون متحمل شده است، هدف قرار خواهد داد؛ از جمله تأسیسات انرژی اصلی آن که منابع و توانمندی‌های لازم برای ماشین جنگی و تروریستی ایران و آسیب‌رساندن به شهروندان اسرائیل را تأمین می‌کنند.
به دستور نخست‌وزیر و با دستور من، ارتش اسرائیل آماده و در حالت آماده‌باش برای اجرای این مأموریت است.
چنین ضربه‌ای ایران را ده‌ها سال به عقب بازخواهد گرداند و رژیم آخوندها را بیش از پیش متزلزل خواهد کرد؛ رژیمی که مردم ایران تا این اندازه آرزوی سقوط آن را دارند و مشتاقانه در انتظار فروپاشی آن هستند
.
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/71412" target="_blank">📅 13:47 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71411">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O8y2Xl4se-_2xz4xavRrvmyhcwuhrC4swEL0RpciiVnuYgdf4VBzic-rKKVma2X-ZN8Gz8wnjIAjj-GOpew67t9lASEJlP1a73nG0p_j2aN_MbW0SYLLp6kRLj17nPIMO9mRpBiJom8y1cbXvY6F7OOXUyrIudCDQyGZGmX1hZ9_4vBfXBnW2sVoifQtuvIvH8STeb3H96W7Gb9w3yCforzh49ukkxk5YCl_kOJNQ4o7ceoGZxuKOxmIUtnS21lWYntkhUEairG6INh89_8pn3n6cZ1v4z5gNR_qXkPDRP3zNAO5081-yM1HuD0qixRqxzwjbS3f2xpK1c1DO5HEXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
توییت سفارت جمهوری اسلامی:
سرآشپز رضایی در حال آشپزی‌ست..
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/71411" target="_blank">📅 13:14 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71410">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb607ca379.mp4?token=ZiUqivETsbhG1szPoCZI3836Qtu0r8rst_4eR6Pk64Ff3ulsLMfKQN66aSwPdSMpqJN5JAibKh1zE-1TMlDYyisbqO0LYX9sTIEu6x3HELwNA8ToH1KdlK9X8A1v_wZf09PbcSAJTnANLH1AAxLKL0qPLRIp3k_Jm-WgUm7Ml2Ehe0N6r2PDUssDRcgX8PnfIe0FWwicBzlKP4GsiFEr57tCklIRNJzCboaBuvsPrqHZcH000oSLZVRo1Mr5TnMvxK_iIE1mric1wDp2JupW4rfNKEk-_rgWtMsF1GLMaYYfajXp6-9Upp8QJIffh4zQGZ7E5pkr4IfbozyJgQ9kQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb607ca379.mp4?token=ZiUqivETsbhG1szPoCZI3836Qtu0r8rst_4eR6Pk64Ff3ulsLMfKQN66aSwPdSMpqJN5JAibKh1zE-1TMlDYyisbqO0LYX9sTIEu6x3HELwNA8ToH1KdlK9X8A1v_wZf09PbcSAJTnANLH1AAxLKL0qPLRIp3k_Jm-WgUm7Ml2Ehe0N6r2PDUssDRcgX8PnfIe0FWwicBzlKP4GsiFEr57tCklIRNJzCboaBuvsPrqHZcH000oSLZVRo1Mr5TnMvxK_iIE1mric1wDp2JupW4rfNKEk-_rgWtMsF1GLMaYYfajXp6-9Upp8QJIffh4zQGZ7E5pkr4IfbozyJgQ9kQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇦
❌
🇷🇺
انهدام پهپاد شاهد روسی به وسیله‌ موشک اوکراینی
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/71410" target="_blank">📅 12:32 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71409">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🇺🇸
ترامپ درباره ایران:
باید بگویم که این به لطف «نیروی فضایی» (Space Force) است؛ پروژه‌ای که فرزند معنوی خودم محسوب می‌شود.
از همان لحظه اول، ما می‌توانیم همه چیز را ببینیم.
حتی می‌توانیم برچسب روی کت آن‌ها را هم بخوانیم؛ «محمد الفاید»... «میامید» (Miamid)... البته هیچ‌وقت «میامید» نیست؛ هیچ‌وقت «محمد جونز» هم نیست.
«محمد»... «محمد العزوری». و این نام دقیقاً روی همان برچسب نوشته شده است. ما می‌توانیم آن را از فضا بخوانیم. باور می‌کنید؟ از فاصله هزاران مایلی، داریم نوشته‌های روی لباس یک نفر را می‌خوانیم.
ما دقیقاً از اوضاع خبر داریم، اما متوجه تحرکات مختصری در منطقه «پیک‌اکس» (Pickax) شدیم.
به ایران توصیه می‌کنم که دست از شیطنت و کارهای زیرکانه بردارد.⁩
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/71409" target="_blank">📅 11:55 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71408">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/f498f58530.mp4?token=nldc6oqBcwWuJEM8g6z1-hkzGSWD9IgyievpZ_iGmknmbItl1zo7BKbyTQVH_ojG1AVgXCsUEua8GTcjvwJtqpFHgwMVgZguYOYp6EshO_wNFdWGpAYIRT6N3yGCu76MU8c9oS7KZ13Ya-tMVG3g2bdFiqZ6FQkaNTjBuifTq6ebbRfl-PFkyENqduvGpcdOTg5b3Bsh5FUevhuZE6VVVGmNRKAXNxUT_24Ir0tJ4fG-8WgjHSrcKzY2jEmLwXQv7OhBrghvYE-_a2pSmsxe6gxEWRTEEbLwbMC-c969aDXAhe1zk9fiEUXGiTXuODncS5sZLu9d4PU5pSQXjLrMTS5_lrsGxHD_OeweNDybKyOOkikV4sRYXPKIJ_twdq07JsNyY1IgBozbAcpBtr6Q1NWrM4o-5ahpOZSUJhumLDOBfzVZ2GT_hdanfMOqFANwAFzkWs41FBpq9pyLmP8biP1r-epGpAflffHRJ5PuS7Hu6_XEtHBzoWlsbn0iFZrjSvHdMH-jyt_r80Pj8zf55rjAlYy70UlVIVFApFSP3jnsXqAVDtRqR5Q0dqfeGLKTMDfWc2N9A1Z3ci9l2SaWnQc_2sQzPJBY1OPPLDOInszfCkiWlVqJab-NZ7Ek2K-yTj2FPr8ln6gk7RoDXsobUxPaQXyHGVJpBYxOEYglfRI" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/f498f58530.mp4?token=nldc6oqBcwWuJEM8g6z1-hkzGSWD9IgyievpZ_iGmknmbItl1zo7BKbyTQVH_ojG1AVgXCsUEua8GTcjvwJtqpFHgwMVgZguYOYp6EshO_wNFdWGpAYIRT6N3yGCu76MU8c9oS7KZ13Ya-tMVG3g2bdFiqZ6FQkaNTjBuifTq6ebbRfl-PFkyENqduvGpcdOTg5b3Bsh5FUevhuZE6VVVGmNRKAXNxUT_24Ir0tJ4fG-8WgjHSrcKzY2jEmLwXQv7OhBrghvYE-_a2pSmsxe6gxEWRTEEbLwbMC-c969aDXAhe1zk9fiEUXGiTXuODncS5sZLu9d4PU5pSQXjLrMTS5_lrsGxHD_OeweNDybKyOOkikV4sRYXPKIJ_twdq07JsNyY1IgBozbAcpBtr6Q1NWrM4o-5ahpOZSUJhumLDOBfzVZ2GT_hdanfMOqFANwAFzkWs41FBpq9pyLmP8biP1r-epGpAflffHRJ5PuS7Hu6_XEtHBzoWlsbn0iFZrjSvHdMH-jyt_r80Pj8zf55rjAlYy70UlVIVFApFSP3jnsXqAVDtRqR5Q0dqfeGLKTMDfWc2N9A1Z3ci9l2SaWnQc_2sQzPJBY1OPPLDOInszfCkiWlVqJab-NZ7Ek2K-yTj2FPr8ln6gk7RoDXsobUxPaQXyHGVJpBYxOEYglfRI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامپ:
دو نکته وجود دارد. اگر من برجام را لغو نکرده بودم و اگر آن‌ها را با آن بمب‌افکن‌های فوق‌العاده‌مان — آن بمب‌افکن‌های بی‌نظیر B-2 — هدف قرار نداده بودیم، الان آن‌ها سلاح هسته‌ای داشتند. و من مجبور بودم با عنوان «رهبر عالی» خطابشان کنم؛
مثلاً: «جناب رهبر عالی، حال شما چطور است؟»
اما حالا دیگر نیازی به این کار نیست. اگر آن‌ها سلاح هسته‌ای داشتند، من به رهبر عالی زنگ می‌زدم و می‌گفتم: «جناب رهبر عالی، حالتان چطور است؟ آیا کاری هست که بتوانیم برایتان انجام دهیم — البته به جای اینکه حسابی بمبارانشان کنیم؟»⁩
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/71408" target="_blank">📅 11:42 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71407">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/1bfc54b65c.mp4?token=aRyqz2JTRpkIsG0jcQYyY1wWOsNrsB0dsmheo3c0p712rz__acOs1jzzOsCKd1G8qp7DMgM7b6ksY7UtqNPhnopcOT-O06hnLCHvVvRPJPYtaQRgZovKIochpzvW5IlpRfRnpC6JELtFjKWUczMwuuL5EtXyAgH4HtTedu0SqxBILFGy1e5nnPBW4LGLWZIS5zrDOxQr-fkcekM1coTr1VDCcBBFd6cUSS8QnQzBr0UWB55EFZAqhks7Cya23fExh1PtgQ6z2XNX1_1wwhC6UJK7jsosPQyUtH7N-7GC0wJh-29bpo8dPE24WWQtaY4wbXfL_aiKiwqAtMJ41yXwoTNo_Moav7wMAzWUX9K8oV2C9hBjwwCEJwIrWiIp5RpO_422yBquOMbNoErQsZrYEh2qG91tskjBGb-UpzMmsm9f7mIYNLNcZ1-dbD-hbFn7JmVRw0RAi5YqMUbL99OJsvHS2POJpJyg47cMMqeink9ZlPHCvY03dF53vYxbG4gwme2cox0qdFrH7fown6Fq73uS1lC96ngZdI2zaP1zsG0rCexh61lOr02iGlrYE-B6L6vZHP9hsV7nL7J2ghOkWSxsfnTqGdpgmRtbOrl67peWHb4OIBCdUdJ8X5rZlubDzoQXv4l8DMayCfySqLacNWsbmDPQ66Yhc6af9IHrJ2w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/1bfc54b65c.mp4?token=aRyqz2JTRpkIsG0jcQYyY1wWOsNrsB0dsmheo3c0p712rz__acOs1jzzOsCKd1G8qp7DMgM7b6ksY7UtqNPhnopcOT-O06hnLCHvVvRPJPYtaQRgZovKIochpzvW5IlpRfRnpC6JELtFjKWUczMwuuL5EtXyAgH4HtTedu0SqxBILFGy1e5nnPBW4LGLWZIS5zrDOxQr-fkcekM1coTr1VDCcBBFd6cUSS8QnQzBr0UWB55EFZAqhks7Cya23fExh1PtgQ6z2XNX1_1wwhC6UJK7jsosPQyUtH7N-7GC0wJh-29bpo8dPE24WWQtaY4wbXfL_aiKiwqAtMJ41yXwoTNo_Moav7wMAzWUX9K8oV2C9hBjwwCEJwIrWiIp5RpO_422yBquOMbNoErQsZrYEh2qG91tskjBGb-UpzMmsm9f7mIYNLNcZ1-dbD-hbFn7JmVRw0RAi5YqMUbL99OJsvHS2POJpJyg47cMMqeink9ZlPHCvY03dF53vYxbG4gwme2cox0qdFrH7fown6Fq73uS1lC96ngZdI2zaP1zsG0rCexh61lOr02iGlrYE-B6L6vZHP9hsV7nL7J2ghOkWSxsfnTqGdpgmRtbOrl67peWHb4OIBCdUdJ8X5rZlubDzoQXv4l8DMayCfySqLacNWsbmDPQ66Yhc6af9IHrJ2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
املاکی:
به نظرم باید اسم آن تنگه را عوض کنیم. باید آن را «تنگه ترامپ» بنامیم.
بالاخره باید سودی هم برای من داشته باشد. قرار است نامش «تنگه ترامپ» باشد.
خانم‌ها و آقایان، می‌خواهم خبری را اعلام کنم: ما آن را «تنگه ترامپ» خواهیم نامید و مطمئنم که رهبران ایران از این بابت بسیار خرسند خواهند شد.⁩
@News_Hut</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/71407" target="_blank">📅 11:34 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71406">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2660237e39.mp4?token=eluLdFcqtXlPmGYRbs_OBUY24Y4S1_uHa7fq8EZolYRyUophwOC-SnMLbgaCehmU93VybN6le3POvPE33zbgx2BQXYTHA7EYgXZNdJVKy4GobD_w4E1BUveIKTuWBXwhlzKaiz6oCKibGp-WlM8UKmC3LSUmNyCkPZsW_6LXQLqBoq0_rcgUbZ4TrgUlNawqXWp6FcUBcvbiWSwSkYLB-nVHIed-MMe4U1GxRHCHXkHQRyUpG0kj8Z30ECi1dFJDouy5PlIDC-Wql_MSXrbB_zOAZLHkPYxlLHXMX6sezjFpBGQJf-N_TZYvxWc3hc9GeOkZlz0KNetPQYOqthNQGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2660237e39.mp4?token=eluLdFcqtXlPmGYRbs_OBUY24Y4S1_uHa7fq8EZolYRyUophwOC-SnMLbgaCehmU93VybN6le3POvPE33zbgx2BQXYTHA7EYgXZNdJVKy4GobD_w4E1BUveIKTuWBXwhlzKaiz6oCKibGp-WlM8UKmC3LSUmNyCkPZsW_6LXQLqBoq0_rcgUbZ4TrgUlNawqXWp6FcUBcvbiWSwSkYLB-nVHIed-MMe4U1GxRHCHXkHQRyUpG0kj8Z30ECi1dFJDouy5PlIDC-Wql_MSXrbB_zOAZLHkPYxlLHXMX6sezjFpBGQJf-N_TZYvxWc3hc9GeOkZlz0KNetPQYOqthNQGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🍏
اپل از AirPods 5 هم رونمایی کرد؛
▫️
ترجمه همزمان و زنده
▫️
نویز کنسلینگ فعال قوی‌تر
▫️
صدای فضایی شخصی‌سازی‌شده
صدا رو جوری تنظیم میکنه که حس کنی از اطراف و جهت های مختلف مياد؛ مثلاً تو فیلم انگار وسط صحنه ای تنظیمش هم متناسب با گوش و سر خودت انجام میشه.
اکولایزر تطبیقی نسل جدید
ایریاد خودش لحظه‌ای صدا رو بررسی
میکنه و بیس، زیر و بم و جزئیات صدا رو خودکار تنظیم میکنه تا بهتر به گوشت برسه.
تا 5 ساعت شارژدهی با نویز کنسلینگ روشن
💸
قیمتش تو آمریکا 149 دلار اعلام شده.
@News_Hut</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/71406" target="_blank">📅 11:30 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71405">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71405" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/71405" target="_blank">📅 11:29 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71404">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GgMeIYQk2enaLPUt9gnYUs107bSMYczoI_SegJaikFguI0HezxDQT3JC6DjkHsEFm4IGXs6bRsjSpbbaaKbYlEfaO2W467KKlxvtFK1lKEAf13_tjY-PcIEZuCyUsUsEyM9Df8d-9SS4xS83RFSD2UO_h8dVVN7-JBGlTOh1fngAjujE0GXCATU_6SKan-nyM2pVWPt_rR3bBMk3qs458MDsZxQf3pykPSlwki4A61cB-oG5wXrTgclfVBOjm9t2_Z6CX5AixVoowgTlA6PRXK7CXQ2euWoEO0Hr5EblLZ39EM_ghNiZPHo2gbQezCTH7f-Yy9YtKQF81jd2t7KO_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
پیکان
🆚
استقلال
⚽️
رو در
TrexBet
از دست نده!
📉
نگاهی به آمار ۲ تیم
در ۵ بازی اخیر :
⚽️
پیکان : ۲ برد، ۲ تساوی، ۱ شکست
⚽️
استقلال : ۲ برد، ۳ تساوی
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/71404" target="_blank">📅 11:29 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71403">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/86c3602295.mp4?token=NwYvlUw3ZudKRVqRbUa9x_B-H18CZpIuY5TFdt_BfNRoHllJlXU5Y0K0j0z_9yXygKrFw28_UYfTbYlelopbNaQgJ3_yNfH8SFJly5dxGpCyvKpS8hhoorppsOJNBRx4x1OFGB3hcyK8wHDffcRw_ieNA8l2ZYAatRQUa-FzN7EyCEXFTPtPzQpejR0EpstRReu3Zn3LyppIvyoi-b4SxXrYtrLz-kSG9b_IfOlOLcVuvGr8gcULxpQon-vo3plpgU_-xxWb-PqPn31G3HjMliLa9xOCoc6aWuDBf89afgPZ-nX3QTTa2oJe5HK9zQtTEgqID8_gnhBvJAZBc6UILA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/86c3602295.mp4?token=NwYvlUw3ZudKRVqRbUa9x_B-H18CZpIuY5TFdt_BfNRoHllJlXU5Y0K0j0z_9yXygKrFw28_UYfTbYlelopbNaQgJ3_yNfH8SFJly5dxGpCyvKpS8hhoorppsOJNBRx4x1OFGB3hcyK8wHDffcRw_ieNA8l2ZYAatRQUa-FzN7EyCEXFTPtPzQpejR0EpstRReu3Zn3LyppIvyoi-b4SxXrYtrLz-kSG9b_IfOlOLcVuvGr8gcULxpQon-vo3plpgU_-xxWb-PqPn31G3HjMliLa9xOCoc6aWuDBf89afgPZ-nX3QTTa2oJe5HK9zQtTEgqID8_gnhBvJAZBc6UILA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
رئیس بی غیرت دانشگاه سمنان: از همه دانشجوهای عراقی معذرت میخوام، قول میدیم براشون جبران کنیم!
دانشجوهای عراقی فرزندان ما هستن و نمیذاریم کوچیک‌ترین آسیبی بهشون برسه.
اگه خدایی نکرده یوقت اذیت شدن معذرت میخوایم و بهترشو براشون جبران میکنم.
تمام افرادیم که برای دانشجوهای عراقی مزاحمت ایجاد کردن، بازداشت شدن و انداختیم‌شون زندان.
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/71403" target="_blank">📅 11:00 · 19 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
