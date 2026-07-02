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
<img src="https://cdn5.telesco.pe/file/UFXmewFz6qrOO05Si9vO9AO3mISN0q_I0dmegawcwKTzy9aAvSWmv5q3vjGfA_LLgIC2zWexCbKYs5FuPSTigErLQMe8oRqSulMXqJ_elp58EN-cPU5syjIh2zre6QfLWAwcBSQdyWHddcsOIGJcekg4YKT_LWaWSOGRW87HbuLJJLLUJIKft0Yq0n7uhl0UNIMhcvbvJt2YSYXXFzlWq7lzP_XcChLJfE6ZYz81Eq0la7TI2-0_OLH9r5QPtAoss23lJ2zKyA14MhqnxOD77R1zHi4wNROZ5ATH1Qw583JRGwYZz0-HnBxg5sShLqwg7JWNh_fUJLFyj20wh3jj5w.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 جام جهانی 2026 | فوتبال 180</h1>
<p>@Futball180TV • 👥 662K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-11 05:59:55</div>
<hr>

<div class="tg-post" id="msg-97574">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kur5vj6BPftoSKdefLoNq0lS-0pQzkHQMgscoB_pUK9-PWx4qDXZ2wP2VRHzx5Mzbu9cDVrptXHfEDxQs_n5dP1YA_9wkj2JvePhn_aQGZAb8P-FDN420bhRdJaB6ENUn_8s9_fOkV6vmdBPUhPlMLamifNziI3ERBtDfGkeEUfLOpTgIl2aU26rjjpa_wl3Szh7ZK0Eu3urnfpxKyDl7dviF7-wcWxnXAFa-wlPOxV4d7dWNwRYnH5wgJJVN9jJqFfN0V7VJbI1lQVX8M9QPdaUXZ6wE4MevJYhuCmKEZItnuS0WWDOQoqTRX-_hNjUyD8B2O-6Quiv8A2sSOKj2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
آپدیت نمودار درختی مراحل‌حذفی جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 315 · <a href="https://t.me/Futball180TV/97574" target="_blank">📅 05:55 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97573">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HqiNFChl7eQgmSc4W68m-cmUk1b-nieKW0_MFeHOdXFsBpH3EvGTJ7TUkPmQRpOdLAKrlkMRyi575IHrRZAwVbpoo0WoKo86v1rfaMGMn-k-gXy7FXe-VVfDACP9zcedVxDF0YPE2VpydBk6eOnhMq-6PImY34RatE7ewTn_XH3oopSVhH_j_W_yfeDf-bfGvI52vmAQxwFWEQdCUM46dkcwiY2H1hhsXWjDaV8ekF9HxkFEoyuF7M-uMSUKEgQAronUAm-VWFhDyhgrz2_IkxCsLkOeFyE6zPdeQd9Cai0ddi460DnyOKSNsG6EMNO0wKjvm8Syx3ePg-Ndmv-Oyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
مرحله‌ ⅛نهایی جام‌جهانی فوتبال:
🇧🇪
بلژیک
🆚
آمریکا
🇺🇸
🗓
سه‌شنبه 16 تیر ساعت 03:30
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 929 · <a href="https://t.me/Futball180TV/97573" target="_blank">📅 05:45 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97572">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QhP9lU6Uo_ALZwp7j6QbTjJcjfOHZNRFmYBusiibCRVo6ZBulZ5eiTRqk2V02wUN_YwNOhrt8xeaO1w2BnSDvfvl4c-1lOUStsbVJCt0JoiS-r3uuvvC5JjMO_FxmlA0pmrvGKJVdqmx5SFiNnjGSAxbvs7hGxMTytA0PKQ_71hVWy-pmEVTeHFYh5gRz36E0STtmvDSOxfYJS_ekaM8DvuUzE_r4yIjVt3v5GApJoFA9Sy22uVMKzlp_TPbZq2t1WeQt7lf1NCq4NDM1r4hsoqAnRd_Gj2cnYxvqr-NEK989ZJ1WRaKDJ_Opf4lk2WuBsrB8FO7W5krjZmrAJP4Gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
پایان بازی | پوچ» بدون بالوگان در یک‌هشتم به بلژیک رسید؛ ژکو و یارانش به خانه برگشتند.
🇺🇸
آمریکا 2 -
🇧🇦
بوسنی 0
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1.54K · <a href="https://t.me/Futball180TV/97572" target="_blank">📅 05:39 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97571">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RMiDm_OgeJziEEeE4cYUSfDjrYk-SetCyrOSWKLSGPxKWsZZ_skjx22RvPJlMjk8DdQp4UYVn_KY2puv3XOfyQ6D7vqqSLlDM9gIb6ouiKh8yytrOSSufSub8Fd2lauxOYlK6CsNEyb_SFPr4QVHjrYRdNVVvAxpOW5NKQzcwMTRXoPZb2Pkti1__ybtw3XU0UsXfvv_d98nQ7Xd5aFWrtAu_kuhN1kBtmzJJzrP_WF7SzKr_gZQimE7JgcCrpSIeryGTl3JlUzNiCdbG501-9wDqDuP7KOEavnejGDugLIA5G3E-iUfuCNuTgiNY1jQwauu34fONa6fKa6-sf9edA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
#رسمیییییی
؛ آمریکا راهی مرحله یک‌هشتم نهایی جام‌جهانی شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1.55K · <a href="https://t.me/Futball180TV/97571" target="_blank">📅 05:37 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97570">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">ده دقیقه وقت اضافه</div>
<div class="tg-footer">👁️ 1.86K · <a href="https://t.me/Futball180TV/97570" target="_blank">📅 05:27 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97569">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/76ea16f99e.mp4?token=JWzeW2AJ6t12Dz8-JehdYBfyKfpWM2YQIHwKKKzyMy-BERs-5G-ZOcyGt0AStqXYlaEIjQQ9PFHt9Cyp3dJxzZPGuF2GHjUAFew1QNvtzb-VI911KbSLn5BQAWSAzRr-tm5W61P6n20S77G42JIoSbUtxAlmRi6dry3_i9ZvXY1xh8eD7aDd28deYXV4dfn8DaUHc8H3J3fVQHJ0XrWkquwAxvXQv5P8_4xJkwknIfhT4hZGs_zMGLoMWhNiSuc4vzl9UcRQsKyjlCsUzB9o9mEqmEl0ha8tU1KqFpLtWoO7sx0gFwDbbY84ChP3al4EWogxvZYr4Q76hcz6CTWcHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/76ea16f99e.mp4?token=JWzeW2AJ6t12Dz8-JehdYBfyKfpWM2YQIHwKKKzyMy-BERs-5G-ZOcyGt0AStqXYlaEIjQQ9PFHt9Cyp3dJxzZPGuF2GHjUAFew1QNvtzb-VI911KbSLn5BQAWSAzRr-tm5W61P6n20S77G42JIoSbUtxAlmRi6dry3_i9ZvXY1xh8eD7aDd28deYXV4dfn8DaUHc8H3J3fVQHJ0XrWkquwAxvXQv5P8_4xJkwknIfhT4hZGs_zMGLoMWhNiSuc4vzl9UcRQsKyjlCsUzB9o9mEqmEl0ha8tU1KqFpLtWoO7sx0gFwDbbY84ChP3al4EWogxvZYr4Q76hcz6CTWcHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
گل دوم آمریکا به بوسنی توسط تیلمن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.17K · <a href="https://t.me/Futball180TV/97569" target="_blank">📅 05:23 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97568">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">عجب تیمی ساخته پوچ
🔥
🔥</div>
<div class="tg-footer">👁️ 2.48K · <a href="https://t.me/Futball180TV/97568" target="_blank">📅 05:18 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97567">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">ده نفره زدن</div>
<div class="tg-footer">👁️ 2.48K · <a href="https://t.me/Futball180TV/97567" target="_blank">📅 05:18 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97566">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">دومی آمریکااااااا</div>
<div class="tg-footer">👁️ 2.48K · <a href="https://t.me/Futball180TV/97566" target="_blank">📅 05:18 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97565">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">گلللللللللللللللللللل</div>
<div class="tg-footer">👁️ 2.48K · <a href="https://t.me/Futball180TV/97565" target="_blank">📅 05:18 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97564">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u4zHfmNKLRgOLRnwKggD3VYC3BXje_mZawTffn08R2AYPPmQjMtjyzTAoibzYvIZQa-ADkvTHs2Qx18WX3j_l5wVlen8NSV3yMnRu3nGYcRIpVKjkii6A-dnOt0U7zwFVYsmfTPSehR2dyJPE7s1Ski37EaipQpppc8YfHtOEIAWFdVGyK5epIvpNegj0asxFSYNyV0_MsEevsHAb6NUDw_b3usXmF1ET7dgZt_YV3KltQEh2Ijm0_MQAIauygpuGNuCq0LkCDL8dyTaUR_sVm4r5483FqTBAlSCwSzi3D9mFBG-TSCGvwWYkAcKy3YhmpHpIAo_ILncTPNizccthA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 2.48K · <a href="https://t.me/Futball180TV/97564" target="_blank">📅 05:17 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97563">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">دومییی آمریکا که رد شد
❌</div>
<div class="tg-footer">👁️ 2.48K · <a href="https://t.me/Futball180TV/97563" target="_blank">📅 05:15 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97562">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F6OdY9lA6JzyMsXaILGGrxWLkM2QWFIsF9FIwZg5AxdLrNrRi2yAEP7wl1UMTNAK5Pqk4bFr3IUyX7PA7SBPBoAGSo4PI53dIJLf4ZqkEHT0aIDl6okFttpT9ZFLp8k4QvUhcUiJYV3IQBMhL28ZinZY1QtM5hMl77F9Mr15PMXSuCPm6jaP2emtRArMU89fO-wITEgCWt6Am5urv-pJFp57GW6kMpqhmN_3cqc_bDhXkLHUxO_H36VxiOzbYM7DQQl3MvGtMSIc0qzy0V-4jyjkHM1kbzg9HHXflwyd_ch2GI36Ncn8IxiFqBSKqmou0vnGJmqdqiEoOMCpsY5Duw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بالوگان اخراججججججج شد.</div>
<div class="tg-footer">👁️ 2.79K · <a href="https://t.me/Futball180TV/97562" target="_blank">📅 05:10 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97561">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">بالوگان اخراججججججج شد.</div>
<div class="tg-footer">👁️ 2.8K · <a href="https://t.me/Futball180TV/97561" target="_blank">📅 05:00 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97560">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">دقیقه 62</div>
<div class="tg-footer">👁️ 2.99K · <a href="https://t.me/Futball180TV/97560" target="_blank">📅 04:59 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97559">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">اوه اوه رفت کارت قرمز برای بازیکن آمریکا چک بشه</div>
<div class="tg-footer">👁️ 3.02K · <a href="https://t.me/Futball180TV/97559" target="_blank">📅 04:59 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97556">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DQ4NzZ8zQmTgIx3wpYaySfp7FUF28bvoDYZlNYtuy6dJ1kKSBEQExl9Sh1nPZiJC-OcB49BpdtmSKZ5lCbjppbWKlC_f43li4HDyCFmlzVfysKL96pGxkogi37E4RPOzQR0ftUSMnFjI4_MRV7NCvuWfhDxjKj3gJFz5sWn3iaMCgQb-z8Trx1IHn2UI3BtGSLbNDG5T8Op0G9mDQcsNQs2BWk8_9HWf00C26KdkGsfCh8UrgWDBFyVleuUxafFjE91q7LoDvctzFFNaeo70FQ40vkGOoDhza30rKTSzFbzjabfJVxketr1J1TWCpO4eQVM81l5FB5DP-skI1aue_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bm0biyx8TG4jVYnunv6vGrJTgdoQtATJHnNr43Ec-Cp726O7mIet6WZouwTAfr-7puqGHNxOn7elbLuh6fUlfOeFcRc8Vubc0IqKvjH6IddOstHxw8PSozjECccA7fqubMgYNAxcSd5I9j72HPKbG-H-Kp5Dd2ZsIiVipthI2atihrLnlX9xg5slsgE5fKW3ibvBgj2sIxOb0HjK3ZZJb8M3qXWyX5BEx1kfQn1RQWiE24zk2rg0XhuWt41D8RCziCz1I0DHZd0hM9aAgBLsO_1Hktnl9NVxnfgW2L3IBOwfPF79yFC88mLeECj72X8pfWMwfOkxYRuRl1N8Ktx9Tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vaDyBLvndWTOKAmnHbxLFuVAF6Ad6fWGzeP1dDfp3YqRFOgu9q6s1fddBeQJjuz--Uq07kwpfEn89FAk2qculob1oZNtzFukOdcrgeEzQbSUV8Ii_fnDVToGhnOYWDUFEV1Wj3dk142s9q3tNhZJr5zyzZt80zTm5DKMkxlhOpsdBysQBXEhWMYuGEPGLaQRoPGJT_qlt_zyusbt7scTmUGr2EoOnxQG8NP_0Q7kLmLhqiKD7Kbz76dhYLQ9OBoWwno_ukHHTLGU5Zt-qNU3bh5gHubaQq2fq_qWWWBBCJ3iM1WqEjfs-F-qApoocBlewNh_pgOlsmkPU2Ajy0pZmw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👀
بانو میروسلاوا مونته‌مایور مجری شبکه TNT اسپورت جام جهانی هستن
🐸
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.11K · <a href="https://t.me/Futball180TV/97556" target="_blank">📅 04:58 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97555">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g_OmyihyEFJPV3aWOUAJ52o0ttcvUsd2zXSXAhe94uoQRmakufLf4G6ZMJDb61n9hEMtBnXzi8KoZoQRoP8bfGcZ_RwtzT4FbAUyZMxbmFDJLiRQ8qMg__pA5z809G7iy3M8cnxPJhiT-3v9icsmnHrAtAXK6g-UDd8Ky9aoCzjTXxpvlQyPSKD7YH8-SL8Stc0y_EBcmKJoP-2aWsp21pklbfIo8va3OZfLYTfjAHGTb4pfkCpem6DqHUguuYQRP_iph82RujcrqUQI66eRdea4nd46Bq-KcNLksuYEWOqvlWeCH4VqqYg3VsHBXvhiVmZvkUdoi-wo-wWMzahkoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
تاریخچه دیدارهای تیم‌های اروپایی مقابل آفریقایی در مراحل حذفی جام جهانی:
🗺
اروپا: ۱۴ پیروزی
🤝
دو تساوی (که نتیجه در ضربات پنالتی مشخص شد).
🌍
آفریقا: 4 پیروزی که دو تای آن در ضربات پنالتی بوده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.83K · <a href="https://t.me/Futball180TV/97555" target="_blank">📅 04:54 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97554">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TN5H_L4yvCtEkr90HDODyrdS77qeomgp95lCKyok2i80fM7ZEcI4iWXAR8mAPaOS7oQeKrxAwSdzKEgoaPplSXLbIgL03DJqPxbHMXdHhJrmxdur3hyieQngvIKhlG8Jsd8L5rqnz0t9LrQicXxh0ileVCHFv0AvQM6FNFdxJdu02_7X0AG240JVav3NAN2BGEM2Sg6Cp3AyF8H0TNvIoIsVTaHH22vvwBqAFmFECdOTH4LIosyaCBxOgjS0u188SPxJEAHlZYosFBPcPfBg_RX9BZAUXTYYXksIkgG_PDIP0Gc5XT7x89e2MxVyCbrZkzAX93gwGZ82T6u50GzfLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نخ داد پرز بخرش
😛
🎙
ویتینیا : لوکا مودریچ برای من یه الگوعه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.39K · <a href="https://t.me/Futball180TV/97554" target="_blank">📅 04:41 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97553">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/94e4656d07.mp4?token=UKA32oZiwdKPnGsLEQROfQ_e0kpnsXkMZ48D_KfD0JW9t_VV9xiD6dRRQT38sC4bOWhzsGAJuVVor_A5wbkxrYjqpi1kQpEh5bfqjY_VtzTzBp1gcmSu5c5bluK1p-4KRtALJi3vdijEcDsVZ0OTr3q0fI_TVqZzCs4Gi0_lphqXDCXelEuGsSUn31e6ivlBqdh-3fEUeG0DhNx7znMri-CnyGYFWMJkS_22XteNSNBqt533w2GjqfJ0MUQx4mruxu5U4GZ_DbpJ3rOzMn_p-DKg_3IekCnOQt6i4eRE1VQAINIXioeKlbeHA0pjnzTLJquNJU_998FwO_Yl6cFwdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/94e4656d07.mp4?token=UKA32oZiwdKPnGsLEQROfQ_e0kpnsXkMZ48D_KfD0JW9t_VV9xiD6dRRQT38sC4bOWhzsGAJuVVor_A5wbkxrYjqpi1kQpEh5bfqjY_VtzTzBp1gcmSu5c5bluK1p-4KRtALJi3vdijEcDsVZ0OTr3q0fI_TVqZzCs4Gi0_lphqXDCXelEuGsSUn31e6ivlBqdh-3fEUeG0DhNx7znMri-CnyGYFWMJkS_22XteNSNBqt533w2GjqfJ0MUQx4mruxu5U4GZ_DbpJ3rOzMn_p-DKg_3IekCnOQt6i4eRE1VQAINIXioeKlbeHA0pjnzTLJquNJU_998FwO_Yl6cFwdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گللللللل اول آمریکا به بوسنی
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.69K · <a href="https://t.me/Futball180TV/97553" target="_blank">📅 04:35 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97552">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VRboSNJY7H6plK4stEBq0J-Sfn-i4oveq-haTI7-4wXiZVydM_zUtNzHpj_yBZYcuVnfbvTgq1J6_YaBPTIqZVS7n_ECxD5uQhRpNsfDkddk5q5I5csy6-3SLelYX6W6aMAwHInTha_7pdQozFAYL6Gb2Vrd2R-Q_UB5pKim1pb6rMo7TH5A30tkNfwZRvTp34wMiTUer-aybB4rsRDlxuImXNaFL7fAbd9sSbyJUefd-FU43ypiv3A38Pz56U5EWWQQ8DAWBv1FXkRM0qt_nQiGA_z0302dvUM85MTSWI3iDxFs-eef1ahqiISQcgdP5Anvs9ErU70dgWTt-hQFJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
لامین یامال :
🔺
"به کوکوریا گفتم که بازی اول ال‌کلاسیکو رو از ابتدا شروع می‌کنه و بازی دوم روی نیمکت خواهد بود چون قراره زنده‌زنده بخورمش."
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.99K · <a href="https://t.me/Futball180TV/97552" target="_blank">📅 04:26 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97551">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cMz9BT4M1RM1RjoTWrpe9sE1P4FNMM1MvT9eZrGpR6hp6igGjnAe44PrcKpxuU08_ouYuBWM6Zw6aNhLk6DQHex3ogEa31XTiln9GYS4QCOpRZdS_beDlEDNZoC9IZCP4-tSejqmHZx2fbj6GR0TmiT5L2z341c1fm7eRunoGSi6q_-XA_tbHXa2Y4rJ3y-OBWrodhJGCYSnrj8D6Q0_V-fe-jVUX7esCsfTs2CCa5FQN9BDCyQFCwz3sX4sb-YOGD0vptg2-fhkqrAnOAYoc_lj4HCPOK9GU7qnZL0pHmmEm1p2llIhk3MlwrhAvtfOPrccz8PuCIbbTBB8J2FZJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇸🇳
| تیم ملی سنگال اولین تیم در تاریخ شد که پس از پیش افتادن با دو گل در دقیقه ۸۵، از مراحل حذفی جام جهانی حذف می‌شود.
❌
❌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.32K · <a href="https://t.me/Futball180TV/97551" target="_blank">📅 02:36 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97550">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yjq-TPgkiR4pjxedA-tgXN-clenkML-QqgcltawjP-5YX2tFJAVd2w9x7-qr91-SvCcuyxJfiOW-XD6Pgr0ePxoaiPf7FIN2TMpn9Bq_pz_rxdEOwhQCm8PKmrFWN46cHflsF6kn7ykShP_nGfOwlOFJyNnfmvgZYA-VDo8FvZcFBc_syLjQSVcNi8DrJ9N_ZGPs_j9ue-H3yLzpISWt0TH_GlN0VUNI0bT2b591wped5OW_4T2TdZ5zMpmtAWogrGpaJZprk6Ij2FekdMIAQjZ8R99aYSKmX0pEaHkiToQrc_E6LG8ogsp-VbNeJBaZamiXL1xFXEyVRLLKKlcrBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
🇧🇪
بلژیک در ۱۷ بازی آخر خود در تمامی رقابت‌ها شکست نخورده است:
11 پیروزی
✅
6 تساوی
🤝
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.52K · <a href="https://t.me/Futball180TV/97550" target="_blank">📅 02:32 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97549">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nNE_4keijOAGWcnq7nZ8ZQBiHpPtsq9TDQqE0oXWVgETrySkDqiF6-qw_TYDWZnZgFTDZ8I_XtNHGKirybG0JdtzJx4YGXmR5ZgA6h3kwZtrsM1LtAWpwcd9lxCozm2CZjdjoah366LCd2v1yMrKQCOcqvsAH4OIcskugzCprt5wdXyNnjpmT9SirWPjW6aErBdPpPE7Hrn63SR1_I_6e2HioXC3kLpInppR2PB0F3nMH50ITJzx67ETytmuIGBd0DQ4oedfz9mmyltobTt4AlKWlblz0TZr1ahzYy871-aujZGclyDb7SRPAt1233aLXoPTNJm0VMt2Yk-Zw2HNlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⁉️
🔥
🏆
بهترین بازی جام‌جهانی تاکنون
؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.17K · <a href="https://t.me/Futball180TV/97549" target="_blank">📅 02:31 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97548">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pzhj44-GI3cNanrxffLW8rudmAXd7PSB7MnOQ3li0A06nvfPIhOxLAyczgp3bltkClkD4NSdZ6PvAHJUBXkqivxYYDi7Yylw10XNSKjMFTIr1A3cjnaunXq4PTy98uavHiRZIoOq2JH5sedyzzfF9yxnGiy6Dvqc4Vk93EknkcF-BIFJkmzDc4dVV5lKT5aDgELNUglFpDGPq_pufSKyFJ8ZjQOgr-nqG6vOsXrSa14YJsR4TDIN8taoAX5VT2YICN-JMxuErVO0M53XwQ90WzcRpUnroC2_FgO2dtm8cfqtrIPUxCnvTlucHgCrqGZMTYsOhB1CpMylHzfVr0fc_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🏆
🇧🇪
| بلژیک برای نهمین بار در تاریخ به مرحله یک‌هشتم نهایی جام جهانی صعود کرد:
‏— دوره ۲۰۲۶
‏— دوره ۲۰۱۸
‏— دوره ۲۰۱۴
‏— دوره ۲۰۰۲
‏— دوره ۱۹۹۴
‏— دوره ۱۹۹۰
‏— دوره ۱۹۸۶
‏— دوره ۱۹۳۸
‏— دوره ۱۹۳۴
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.88K · <a href="https://t.me/Futball180TV/97548" target="_blank">📅 02:30 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97547">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kB6H3spm_zBKrP9F0Svlq5dCSidDfZwTv7JkrOo5wrWrXe_3YCdBvYn8-NDK8mxm89-KDepD_77iN1nnF8gdjK_dKiR37rWI8qyQFEbbK8mwtpjH0wiUxcLZo0AyzmPyGnNxUN8WraPW1idLzhyObdlJOVk22EC7qVqHrZnN6-VI3Tjtm_C1H9X97xxBEU4Udox9NwBmwbZz2_pkX81E-wLusqLcAN33CMbU33NsYZKXBuy3PTvUJd5dOWHtbjKj4d8wO2G7g6JVc5Riq1zeOqzbNtWUf2HYUd7Kyuerv5M2CaMvEX4cQrZVAKK0_FOtQsjSez9STx6rAuaGxI_FHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🏆
| سنگال چهارمین تیم آفریقایی است که از مرحله یک‌شانزدهم جام جهانی ۲۰۲۶ حذف می‌شود.
‏ــــ سنگال
🇸🇳
❌
‏ــــ ساحل عاج
🇨🇮
❌
‏ــــ کنگو دموکراتیک
🇨🇩
❌
‏ــــ آفریقای جنوبی
🇿🇦
❌
‏• تنها تیمی که صعود کرده، مراکش است!
🇲🇦
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.7K · <a href="https://t.me/Futball180TV/97547" target="_blank">📅 02:29 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97546">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WxNY3Twov77PGwGjFtc967LNGJuYDuexAP2sc46ft13SHF1oqyKTDbXyfrhXYOTh43WGOjqY2ga45usWKEAHqA1c_gH0HaREFQAjtYbvuyE8TC3YUrleHDo9evmX0bVNvX6TdiRrvQnlZ1-R_mVYUkAqyVVRP7sVv4TcW-pAIemoctUSIq7zOZ5wZJBduN6YAfct9H2u-P7LqTmGNb4b7Aet0kbh_AZB8qTW6sPuSKIWE6Cl3NsNJ22zH_C3O55E8ifTov3zccp8_p0cTOXY2lTD1o3khROyVSh6aym7mMa6eknKVi_jm6_N2lD95LM634iP2oKiXud7ewukmJD2Vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک تیم از بین آمریکا و بلژیک تو یک‌چهارم بازی میکنه. بعد هلند و ژاپن باید حذف شن
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.4K · <a href="https://t.me/Futball180TV/97546" target="_blank">📅 02:27 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97545">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j_pOuWUO9KOs1bJVgaT7nBBhR3Vm0ieJMPrhF8N8zAWY4BOIuJ-5JDb1z0SenB8CBVUqveSSqWOBp0DYfpvVKKMR7Mh_nTM58MfAsXL_SNPaB-BL4-j2UCaugi8vXC0-stj-YGAPt_gL6RIuN9nbSQcacqd3pK7BgrAj-tI9sO0T68y_sY37zZXYhw2VTYI29XQvH3EjtPqrckO8QDVElCf7WJLDuDpUv1YPd1sTePZS2eL4sc9D1bxjL7jz_vlPi8ystHzWdJz2BNrTkDFcAGAR4qc8c57ZsosqzcqbZRIW0jCXSDCcDScwvsjcuNetgXKdEDydFKkVB7Xqm6_wYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
آپدیت نمودار درختی مراحل‌حذفی جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.13K · <a href="https://t.me/Futball180TV/97545" target="_blank">📅 02:27 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97544">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TtmwdztcF88VQOvzNn4Z7eixaKJlFTep9mmJbmvydgH_o849x6nZoGqwkv6eBMktc-AZ4iK2tA1u2gUXT5TJ5D00aUBim3c_NAGgpixVlzZEqxRWgNkNwfJxPDtJTmLwlycfldCOSrefMVoGJXTtzZcfr1rwB6yR2CvroBCtAxomdFVANtixz7YbuEpFnpax-CnY47lYcdj_cMisbwn6pman7bHxrmrZQOANVEs4jndmrJ5RyzrxpFSGUGWTev8yPKUiAXfCZ6SLzB1b7Z4lz4LzJfZ3PThU_kcviD8hgkjGNOURr7t571IzfamiIZ_lo275PQmqHj3P4-leq3prcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔥
🏆
گل‌دقیقه 120+4 یوری تیلمانس دیر هنگام‌ترین گل تاریخ جام‌جهانی فوتبال لقب گرفت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8K · <a href="https://t.me/Futball180TV/97544" target="_blank">📅 02:26 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97543">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nJj6-ibqI588kVscxmdiLUHozRPyrKTcV-rKTKuk-hO9qOeizSnEd7bDdSjw6vh7wvEMUHWmqV6Xn8Ub_06JTLtHQpZtEymzXT_EF4XfcDUOEDVkPof0LS8A0cCOGOMOK8fwj5Saf4Ghu2JQM1up8I1K5CCvakhjHiTYZolpjWNA84TK5i5fS85emAlOC2zXGk-S5PWN0an08G00QItP8MDVWNhM8InOF_SeyRtIaYAvpBKVrBT0rl7P9PhHUATSOvocRLbpETkoosRkCx6llxrZ_NlKooBRsIicc3OfLCKOvUbk8nMAN3kHyH-TqAJwESOKZAItm9Wx9bcirShffQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇧🇪
آرشیو وار:
پنالتی بلژیک درست نبود و به اشتباه گرفته شد، بازیکن بلژیک خودش باعث برخورد شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.68K · <a href="https://t.me/Futball180TV/97543" target="_blank">📅 02:26 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97539">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/l-fzd86ku4ySltq1JbnCehQ9l-J_R4XbGHZQdA_uD2gkBnjAqQNDH0ZLjQOogf9DwI1lMzuY_6LsLZjy477auNCWx5yEw-5pFpOVP-5fatWUQ_BbAeJpVuSIyMybO5qfwn_poNN9ZvP4xAUVsJH_xaonha9voKU_WOXythvQRnJ5vISraCjA3EaYxRNt2MKByGNsFS8t25chusBfdIvkK_BUB0VmfyF1qQ49JqCa9UN7GLzQML8Oh6RsStLxA9N96fO0GTR_GE7RqHlpBtwhHOH_fNOuAKj2TWr8id-Gn3o30hc3kTcz798tVqqOOXctFb7J1jTAEd_NBc0nf66PJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/o-fwXfk7fbCuQwB2JcLpRhXRgmzLigKdVuJpMuNAzTqj28vD9oXRxdnOc0oCmNQnOgXbKuQraHd6NABaIzxoYkiSONH1GhU6aq7N-dIhpoHe5Cwc6tBkfqrZsR7eOCByPz2F6Rl8XBJ2b_OaJNJ4vcUsZ1PzX-QKyWjFYXDkKAB3uqufHaT55xDRy1nHHtmP-jlnk_3KnteDFKcTdBqaVgcNS4kqSUmINVBX251yeaCK8x8Y7XdFW74JPzXjVp0sVFLE7wF-SuZJz8ZlHJDKMXtgJmsBPOLLRzWHfA-fZINY5vEQzzD8YnO4WjT3IuyCNiRrkcqeEjZws8Fil7Zkkg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🇺🇸
🏆
🇧🇦
ترکیب آمریکا و بوسنی
⏰
ساعت 03:30
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.75K · <a href="https://t.me/Futball180TV/97539" target="_blank">📅 02:25 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97538">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/luqk9cVrvp8iQI5xI9RGqZGADZRqfV7gHhU_MYAi3QzPDiluA9FC7LQO8xVz1ZBedkt6-zzlXwWlKpJ-QVteFOx4TRgj-kC7ls5LdK-uMZrSeWgrPqtwfYarrJ9fnvJLdZeQOFooJhHmxdvXGrDC_v5YW4TbpqsL8mQS0noXymfGRGPqZvUG1MmCMAUstGuhaXLgjNmTTSpbCMw1K-6monXRHvxY1HK4kc6R8V2KIr2CvsSjNxonp2VE-xgHcH3lXPu41i9MK74joNPabjt-8p92t2zmUJjK88-gcrCvBAt0Fjqc99WbD6hnaiImVCm9g-CrWOhWQHQmMoZ90JWH3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🏆
🇧🇪
برنده دیدار ساعت‌دیگه آمریکا و بوسنی حریف بلژیک در ⅛نهایی خواهد بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.05K · <a href="https://t.me/Futball180TV/97538" target="_blank">📅 02:24 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97537">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O80UA9W5lnqQsFo4gQH3lYcgmrXbO0897vXTA5_sKE4t9T4NJZV8SlT7wS8wditZfMmgUrwzR9sun4CaIfkQzOo1EO3oM8K5_CKWnC6tkDVBkLXNwvnu5A3SHisI3NpX3CQw1LK9XaXi698GE1c87Hfa_V_NsqPJxMHN1QhPrRd5RV00E8maooicTKjqIoGtYwc2_5yKrxOkbXEEomLPwHGcpeabXJWPD2Xy27t8P1_kmXhFOPzL_Vcl7qJkkbDx7pD8ASJ72ZqqGo58A_jVsJPnLc_NkHvwy2ly74P1YAROflt1UhFythv6rvtwo0v5TqgYE3uqw0leyRwyYEpMWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
تیم‌های فعلی مرحله ⅛نهایی جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.7K · <a href="https://t.me/Futball180TV/97537" target="_blank">📅 02:23 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97536">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VLMXXHN6Ql7wUAHDVVvxtApuAlqqm3mCuRwK4wheNzc0ZYXNDDovzJ6MQiq7r39Sok9w9JnC9HqEQo1qPq5c1idK1NNcYNNEsaOzgwT-HFdBLesg6SkmrudTgqwjPl1_9blSCzIBVatIB6zMaej-YzL5kiTcacg86zdi6onlJMhKnR6F2J_gJqykssADOqyZSq1yXU9pqaXOLPUZXOdyYjFpDdpaetve6gwiq2N-bke0CQhDtHsIBn6BFCnMYDU0X5-SgOh8UMYzPM2EjILc9efhD5OPLx0_lVOr7KiE6fE_o6JUDPsEEm2z9B387JhXDneH-GpxlERBKqoDz8i2zQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
و تاریخ که باز هم برای بلژیک تکرار شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.9K · <a href="https://t.me/Futball180TV/97536" target="_blank">📅 02:21 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97535">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i11h5z2V-dne8AOabimSfiA74F4Ie3-TVa6fCqLx4pIIB6alsslA5GM5I2zyvPHyPnm_TWcGQXzrKThdAYk7hOUQ7Pu-FgqIQtIYm1r6aHLZJAgmBaeNIhU9DPuNv-3xvSlYBbVAtw9NOfPcewwU7CJoaLnWW3EjzVmnb2TjhZnnO8QKUWo6uaOOonOIu3idIpCFHFDjAtF-_slDvPM45iJJkpgsQ55f2ydsNrVXrimkhxiffLOcVQoKLoVhEiF--8lXspQT7YR1KHxHoUfSWNZPFnVvn8W8hi1Vmx2lD66eq9axvl7gE0MG33jR1nA4c7JWm2p55eZ3L8pNTYvkkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
پایان بازی | کامبک بلژیکی‌ها با پنالتی دقیقه 120 تکمیل شد؛ بدون دوکو، بدون دی‌بروینه، با تیلمانس!
🇧🇪
بلژیک 3 -
🇸🇳
سنگال 2
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.34K · <a href="https://t.me/Futball180TV/97535" target="_blank">📅 02:20 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97534">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">بلژیککککک صعود کردددددد</div>
<div class="tg-footer">👁️ 7.84K · <a href="https://t.me/Futball180TV/97534" target="_blank">📅 02:19 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97533">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">تمامممممممم</div>
<div class="tg-footer">👁️ 7.86K · <a href="https://t.me/Futball180TV/97533" target="_blank">📅 02:19 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97532">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">تسلیت به هرکی گرفت خوابید
😐
😐</div>
<div class="tg-footer">👁️ 7.97K · <a href="https://t.me/Futball180TV/97532" target="_blank">📅 02:19 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97531">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">دقیقه 131
😐
😐</div>
<div class="tg-footer">👁️ 8.18K · <a href="https://t.me/Futball180TV/97531" target="_blank">📅 02:19 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97530">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">میگن پنالتی شدددددههههههه</div>
<div class="tg-footer">👁️ 8.62K · <a href="https://t.me/Futball180TV/97530" target="_blank">📅 02:19 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97529">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">چه حساس شددددده</div>
<div class="tg-footer">👁️ 8.56K · <a href="https://t.me/Futball180TV/97529" target="_blank">📅 02:19 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97528">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">سنگال فشار آوردههههه</div>
<div class="tg-footer">👁️ 8.44K · <a href="https://t.me/Futball180TV/97528" target="_blank">📅 02:18 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97526">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/0db93ce7eb.mp4?token=BIdrZH9br8VwgIM4DpyOTzfUbgVPBJ5JLvxak9i0tkKXpq_LT9jYHNg0qgwHMkm0xMwWYYF95HlVqkDX25ah6qSJY4pUZXiPSPZ-l6oMXPFnHVeFrPkrrjAMt7AC4aGPGDojiINXsLfWUt_eUCyYbSnwLGG7oyvnenAsYh2CgybyO8ptxgWvLoaSIGnnn2mAKUV1D8t9VZNPddhbCk6mxlwynW77EqzDRVjYW5W3GnWSgwXbVB6Kaxki8u8vg7fDMk1-tWZAXUSsV3lpd5w-aFR-GCLI9cr_hJUjComwt5vO92umvI0NbRxsZlnGVERrP8kcfSoXmo82q8mL6K5I5A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/0db93ce7eb.mp4?token=BIdrZH9br8VwgIM4DpyOTzfUbgVPBJ5JLvxak9i0tkKXpq_LT9jYHNg0qgwHMkm0xMwWYYF95HlVqkDX25ah6qSJY4pUZXiPSPZ-l6oMXPFnHVeFrPkrrjAMt7AC4aGPGDojiINXsLfWUt_eUCyYbSnwLGG7oyvnenAsYh2CgybyO8ptxgWvLoaSIGnnn2mAKUV1D8t9VZNPddhbCk6mxlwynW77EqzDRVjYW5W3GnWSgwXbVB6Kaxki8u8vg7fDMk1-tWZAXUSsV3lpd5w-aFR-GCLI9cr_hJUjComwt5vO92umvI0NbRxsZlnGVERrP8kcfSoXmo82q8mL6K5I5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇧🇪
گل‌سوم بلژیک توسط یوری تیلمانس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.17K · <a href="https://t.me/Futball180TV/97526" target="_blank">📅 02:15 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97525">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MErExgKpX0J9CsgguTxpuu_yeSsysQvWXcfPx-lN6bqOcGYt_lhl5-2HSk4lM66i9GaDTOoR4wD8_H247WF2UbvVVP8CgyM2KC2e09Tj4LlhzOJNCnixMYHdTR8uHR1IfA6rln21T91svSySjCAdLDLWgn8ueLBkvH6wZL8nQOo_6VW_6LS3QNL9ag8INHyOlxJERNDb7-jD3vqOnDm6v8QntGCs6ThHfrzdSYwTT1xqX1rpoEzmXd6XObBEl2pb8jSWM8nOzDFzYJdj8DLgJJDU7T3xNWI_2v__Iecu8uEcFxuCOcDqLsePSurz_W-BrUsuoj_bs9etISoDv6_hWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عجب کامبکی
عجب دقیقه‌ای
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.59K · <a href="https://t.me/Futball180TV/97525" target="_blank">📅 02:14 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97524">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">عجب کامبک تمیزی زدن
یکی از بازیای قشنگ جام بود واقعا</div>
<div class="tg-footer">👁️ 7.95K · <a href="https://t.me/Futball180TV/97524" target="_blank">📅 02:14 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97523">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">بالاخرههههههه زدننننننننننن کامبکوووووووووو</div>
<div class="tg-footer">👁️ 8.06K · <a href="https://t.me/Futball180TV/97523" target="_blank">📅 02:13 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97522">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">کامبک تکمیل شد</div>
<div class="tg-footer">👁️ 8.28K · <a href="https://t.me/Futball180TV/97522" target="_blank">📅 02:13 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97519">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">گلللللللل</div>
<div class="tg-footer">👁️ 8.55K · <a href="https://t.me/Futball180TV/97519" target="_blank">📅 02:12 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97518">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">گلگگلگلگلگلگگلگلگلگلگلگلگگلگلگلگلگلگلگگلگلگلگلگگلگلگلگلگلگلگگلگلگلگلگلگلگگلگلگلگلگگلگلگلگلگلگلگگلگلگلگلگلگلگگلگلگلگلگگلگلگلگلگلگلگگلگلگلگلگلگلگگلگلگلگلگگلگلگلگلگلگلگگلگلگلگلگلگلگگلگلگلگلگگلگلگلگلگلگلگگلگلگلگلگل</div>
<div class="tg-footer">👁️ 8.71K · <a href="https://t.me/Futball180TV/97518" target="_blank">📅 02:12 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97517">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">لوکاکو رفته پشت توپ</div>
<div class="tg-footer">👁️ 9.49K · <a href="https://t.me/Futball180TV/97517" target="_blank">📅 02:12 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97516">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WNZpU3zF_6SDRQedY2nFjjObRvwRxKHSKRgHFmSOMOfJRdhweBNPUjDdjg6c6lf0HYwLBCiMHdVs8Mvp3eYobGmIS4byoTAuidFg5zgpdThzwyKerKnhq_U9v1hul-OlFHxypGBeayaJuhPcfNBGff8j6O5V4VHlalB-x-Jjk_fREl9xvUPQ8PgtmahSAnZCjzL3XTQckMhv49QSFJsFaOkv4LJQby5-SpHXfbJshA3SjUYFhj9yg70vjKsKZnDfhvULkQl6dJsWyDLPOFKqph9E5GIVhtHfWZtvR4MznZFsB0aYRymgZYxUZZqbSjURbpXhsYg4OfFhYWlgTqHcSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چه کااااریههههه ناموساااا
😐
😐
😐
😐
😐</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/Futball180TV/97516" target="_blank">📅 02:11 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97515">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">خوابیده رو نقطه پنالتی بازیکن سنگال
😂
😂
😂</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/Futball180TV/97515" target="_blank">📅 02:11 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97514">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">دارن کرم میریزن تمرکز بازیکن بلژیک برینه</div>
<div class="tg-footer">👁️ 9.11K · <a href="https://t.me/Futball180TV/97514" target="_blank">📅 02:11 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97513">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">دعوا شد</div>
<div class="tg-footer">👁️ 8.02K · <a href="https://t.me/Futball180TV/97513" target="_blank">📅 02:10 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97512">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">سنگال دعوا راه انداختتتتتت</div>
<div class="tg-footer">👁️ 8.54K · <a href="https://t.me/Futball180TV/97512" target="_blank">📅 02:10 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97511">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🚨
🚨
🚨
🚨
پنالتی احتمالی برای بلژیک</div>
<div class="tg-footer">👁️ 8.97K · <a href="https://t.me/Futball180TV/97511" target="_blank">📅 02:09 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97510">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">سناریو فینال جام ملت‌های آفریقا برای سنگال اما اینبار تخمشو ندارن تیمو بکشن بیرون</div>
<div class="tg-footer">👁️ 8.4K · <a href="https://t.me/Futball180TV/97510" target="_blank">📅 02:08 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97508">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">چه دقیقه ایهههه</div>
<div class="tg-footer">👁️ 8.39K · <a href="https://t.me/Futball180TV/97508" target="_blank">📅 02:07 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97506">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F95GQ5ky5KS-GahYcv9B-pbsIpvQFQPjzcwZTvO3683rD5rgI35m086fGGZLf1aOMAhQjOq347_dmaxPeEU6qIFRUwRMsBtPRX5hZW2fItUKGqcutkroyl0n4-Z7xqcQ3B0qQPyTOlmsaZYQsKPKTSHkSXa6so_2SMIoCRoM38Gnbv6x4EIJk1IVFBS2l0W9YQsfNUONPdjIF_DrxbhWjTDAEG-FlpeBF-JsaCKH479XYIU-8erwqG-KSzxdywsPOxTXkJDxdbmTRcJuoZGsmvzYOB1hust1GpFTcPvtn0EZbHg2pUBP6eRyQhV5L0N9c3deUW2F945KB1RYCmQK2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
پنالتی احتمالی برای بلژیک</div>
<div class="tg-footer">👁️ 8.4K · <a href="https://t.me/Futball180TV/97506" target="_blank">📅 02:06 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97505">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">اوه اوه بلژیک زد تیرک</div>
<div class="tg-footer">👁️ 7.73K · <a href="https://t.me/Futball180TV/97505" target="_blank">📅 02:05 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97503">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gz2VpYEs6VOzrc2Qy3N4IEoDl-PGCLoePAREcGQYp2MkQqLgebiWhDtnVvvwCHDbi--d8iAefEcjXhfFXzyjYUW1rQ33CGZnZXQ-yiyIi_HzvtT3M8ocBzIkvczkJE5PIIbLnZDceogFRzWVFx3oF10V37GAmVaLSPfGSGu-0bTFdigP8TOURe_Jhz3xzZ2iQFS12uNScrHn9oMmo5NmeYWWV7XsM8tPSKMXXdZcuurHc3Y-R8o2Ffu4O3Rg4x9lwdR3xeJYXZbnuszUf1H4BYskh1Sqty19ytwjptovEZfxSWTNcdfLLn7Dp9-1qhEZhIzjl7amcGaZYhburrBJhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/u6ARWBGTCk6ev3f6AYbvIo9a-N9dC9JAh3C7dMnAGFsDlRC9VvOfrFPWkv8EemCR8usKGf1E9oP9IignLQ3B_6aOE3ZDz6HfLxD9QHd9awAruANOrT3JYs7Jv8Ntio_ox1QIgqCqv0FRUkKNEub0mYFgjPUYbdJQTwMhbCZeY2MaHBuhlrsP1LOuSYkSx7MmHz2yo0y8_YBVLFupwGd3W13ZBg7ekOYNcEmvwaoPIZfJuNg-KYpPl9UsUTH06_0Sw58FDArGJLFzVnK8Yt8lzll-m_Fcgwx7y-0r-zA6GgCtRYgA-RkAGi9YF5OtYgzQDNYC20qIZws1KJ4jqiq7QA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🚨
🚨
🚨
اوه اوه اینجارو  تروسارد و تیلمانس نزدیک بود وسط زمین کون هم بذارن که لوکاکو و بقیه جداشون کردن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.59K · <a href="https://t.me/Futball180TV/97503" target="_blank">📅 02:00 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97502">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ftqygteHkd5Sd-Kf9NhrxQn31ftNJkknUveaEn7fj_UzkKm8nm4Y55zH09An_3Evsq1aEZ_-dubnbedwffnC9Taq-HlNyoBNZCBO8dirSymPUSUlJBYgZxVDmz17xu2o56jhk02pl8AI-MEI6mhlzhko70FklHEwh5XjNsvWjGz8vCpDM6Nmk7py0M0TP4di5jjUKPPt3-yHFjEAUbRZOzTtIcppurc6zLnnd-FlVtvCfZxdO7lHzI8rcBn0HaB7RVJpfwGM7YIMKysitdI5T1qdoxlMJdxIpVeTQMfZJW2_AWkRHRLTIDNnFfmnu_WQCKu5vPBwoUj_LTH0IuiUYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🎙
لامین‌یامال: به کوکوریا گفتم که اولین الکلاسیکو که جلوم بازی می‌کنی جوری میخورمت که تو بازی‌های بعدیش خودت به مورینیو بگی بذارتم نیمکت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.25K · <a href="https://t.me/Futball180TV/97502" target="_blank">📅 01:59 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97501">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c0badec474.mp4?token=RY_XmY-LdIqL0echmpIOSkrfUdU6faY7zhOqbwTh1l87LP6XeULqSLMEjjI1lp7Lj7xd1ANX3fZLX13Nj1OBov6SRG-wp9LO3hCZcdW4deDJ3poJ4GfI_Abps29FjLHIWw1U2PvEgQjsOVSNCdEcenrH7Qmk0RBuO94mDtnvfgy9ub4g-UBW-HTaW4NCcXwYIJ_gg2JWtzO5yq8eiIvUl7XVlMRyc_P11NUWO1S-gM32ZAWHflD0FiNnhAAI5oMRdjGZ-ZjWkKolbti2O6E7OHMfl0-cyRumGjBXFGbAqIApSdGtL0Cw2sbWbAXP0bHfShUlWuEETPjd_ALN84LidQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c0badec474.mp4?token=RY_XmY-LdIqL0echmpIOSkrfUdU6faY7zhOqbwTh1l87LP6XeULqSLMEjjI1lp7Lj7xd1ANX3fZLX13Nj1OBov6SRG-wp9LO3hCZcdW4deDJ3poJ4GfI_Abps29FjLHIWw1U2PvEgQjsOVSNCdEcenrH7Qmk0RBuO94mDtnvfgy9ub4g-UBW-HTaW4NCcXwYIJ_gg2JWtzO5yq8eiIvUl7XVlMRyc_P11NUWO1S-gM32ZAWHflD0FiNnhAAI5oMRdjGZ-ZjWkKolbti2O6E7OHMfl0-cyRumGjBXFGbAqIApSdGtL0Cw2sbWbAXP0bHfShUlWuEETPjd_ALN84LidQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😐
هوادار پاراگوئه و سگش‌ موقع پنالتی های بازی با آلمان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.11K · <a href="https://t.me/Futball180TV/97501" target="_blank">📅 01:56 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97500">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
Join Join Join Join Join Join Join Join Join Join Join Join</div>
<div class="tg-footer">👁️ 8.13K · <a href="https://t.me/Futball180TV/97500" target="_blank">📅 01:56 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97499">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/diiFgEGm6NiMyuQzO6aHdpmrg4OVLSM3IELddOkyqdZ7mwgQaQV36Xi4ABW5zZSQV36vJMcbS6DwlHt4ZLrQwacchUF8pKp0kPmiUJseRQYsT6wFZ0Dmc8vPkIO575kbP8BoMyfHFyca9pidcXXy8lbb4FnQL7vR6Sz0ndQ9jRidEDbk3b3x1cq1_k0Ag4vcFqBu2rbL8wQkiWrop0KFNgt1JJdovAvXT6JETAGvYABtu654nKEtVBAnVCq8pJ7fu7B_2M1mwJ3C44Hq0Qc4SyJuIKPFqHdnuHUfPDN5NasuipcX341FeIhUoc-bIrDIgdp2-r9sqVVjTsvB_TubKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
Join Join Join Join Join Join
Join Join Join Join Join Join</div>
<div class="tg-footer">👁️ 8.35K · <a href="https://t.me/Futball180TV/97499" target="_blank">📅 01:56 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97498">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">نیمه‌دوم وقت اضافه آغاز شد</div>
<div class="tg-footer">👁️ 8.31K · <a href="https://t.me/Futball180TV/97498" target="_blank">📅 01:54 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97497">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2410738935.mp4?token=A-OY2KD3Rz-OqUGS6ZLG9XVhKoZ1xgQX9TpDIXNBcfxonRiynMtV6JGmsrGNIaxEiPPi9zKUyJk7JlsbemyZzIPugQeXRJwFgskpi-OsFWBsiKdZj9ESqQ0y1LH6J-DpNvZeS5DX16eBbvL3AsouPjHqmqGCnqUgs7f1zwFDbciBsEXKliUqNlrwlDZfCRtvGD-U9Bv25pKOtnXYxLlVB-jh-2QGo_63KHoPurUeNYuycuNfMEctsH40kY__S8N6KDcXnJGyWLaIfVVIInxonDDDg0XGY1fDovskKRCltispXk6bYem2Az-74RGxSzD_VQFJyFvQBkPzQYhAV1WoIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2410738935.mp4?token=A-OY2KD3Rz-OqUGS6ZLG9XVhKoZ1xgQX9TpDIXNBcfxonRiynMtV6JGmsrGNIaxEiPPi9zKUyJk7JlsbemyZzIPugQeXRJwFgskpi-OsFWBsiKdZj9ESqQ0y1LH6J-DpNvZeS5DX16eBbvL3AsouPjHqmqGCnqUgs7f1zwFDbciBsEXKliUqNlrwlDZfCRtvGD-U9Bv25pKOtnXYxLlVB-jh-2QGo_63KHoPurUeNYuycuNfMEctsH40kY__S8N6KDcXnJGyWLaIfVVIInxonDDDg0XGY1fDovskKRCltispXk6bYem2Az-74RGxSzD_VQFJyFvQBkPzQYhAV1WoIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🤪
اشتباه نکنید اینجا اروپا نیست. اینجا یزد خودمونه که ملت از گرما اینجوری رد دادن
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/Futball180TV/97497" target="_blank">📅 01:46 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97496">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">بازی رفت وقت اضافه</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/Futball180TV/97496" target="_blank">📅 01:30 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97495">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/e236b4c020.mp4?token=B5t6ZpXh9z5l4fR3R8TL6XR7gP65LXuBk7u5jGTH60sc5qk2mLDUdRUSBp6eCuFDnz2_tV_MmIaZRd4hlk0_cuiEE2bAFW_YoFFKtupIO9fa7DzIUYwoz-j9qWF-JwLNRZ2r_TC-TC45_wsVmeXzn3OSRmYJGKRG3JzpXK_FF8avNKylPgnI8y6Km40INxfj8lOyBnmUJHytGLY_h-NEA6roKDyTZsZ4_WrPz6OH20UCs2-PXC2cQJNErZqGp2BRgqctQBeXsWbk2oWGKAxXk4WhpxwKFN-K-ItY6SaYRO1qPVoEHYMJrX1FVpBOb4CHk741PsPy_PUgW-tjyfcWTSgXX9gJQoh450-cWpvvogpUEarWZuLuE8w-2G4A8deveubcNnM6NRVmp8NjfKa0PYbpXYV3SMGPjjeVg8PajqTztIIqIyVhw077ATBcf1c2PmD1OmOjkMUVlQU_EmOSxmU654d8vf9YyOAh57c6twAcDIXVWeir9nN5e32D6_nIsI4zGMZfWwO_ilAHTHxOPRmyL1Db7KVor0NaLUHFTFcODdmMBiHSIB7XEiTcFe1XoB4vNsVJ0Rvg_RMmGguUhn-TD98jyb-BrOHoUpwl_VhW3N-mirSBfdqxR-G4EKiLcUOR87lEO3fCq6LjWvT40vyuVp5JX_vSvsLmexM2sG4" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/e236b4c020.mp4?token=B5t6ZpXh9z5l4fR3R8TL6XR7gP65LXuBk7u5jGTH60sc5qk2mLDUdRUSBp6eCuFDnz2_tV_MmIaZRd4hlk0_cuiEE2bAFW_YoFFKtupIO9fa7DzIUYwoz-j9qWF-JwLNRZ2r_TC-TC45_wsVmeXzn3OSRmYJGKRG3JzpXK_FF8avNKylPgnI8y6Km40INxfj8lOyBnmUJHytGLY_h-NEA6roKDyTZsZ4_WrPz6OH20UCs2-PXC2cQJNErZqGp2BRgqctQBeXsWbk2oWGKAxXk4WhpxwKFN-K-ItY6SaYRO1qPVoEHYMJrX1FVpBOb4CHk741PsPy_PUgW-tjyfcWTSgXX9gJQoh450-cWpvvogpUEarWZuLuE8w-2G4A8deveubcNnM6NRVmp8NjfKa0PYbpXYV3SMGPjjeVg8PajqTztIIqIyVhw077ATBcf1c2PmD1OmOjkMUVlQU_EmOSxmU654d8vf9YyOAh57c6twAcDIXVWeir9nN5e32D6_nIsI4zGMZfWwO_ilAHTHxOPRmyL1Db7KVor0NaLUHFTFcODdmMBiHSIB7XEiTcFe1XoB4vNsVJ0Rvg_RMmGguUhn-TD98jyb-BrOHoUpwl_VhW3N-mirSBfdqxR-G4EKiLcUOR87lEO3fCq6LjWvT40vyuVp5JX_vSvsLmexM2sG4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇧🇪
گل‌تساوی بلژیک به سنگال توسط تیلمانس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/Futball180TV/97495" target="_blank">📅 01:24 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97494">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">هفت دقیقه وقت اضافههههه</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/Futball180TV/97494" target="_blank">📅 01:23 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97493">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🚨
🚨
🚨
🚨
اوه اوه اینجارو  تروسارد و تیلمانس نزدیک بود وسط زمین کون هم بذارن که لوکاکو و بقیه جداشون کردن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/Futball180TV/97493" target="_blank">📅 01:22 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97492">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">تروسارددددددد پاس گلللل داد
😂
😐</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/Futball180TV/97492" target="_blank">📅 01:22 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97491">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">کاپیتان تیلمانسسسسسسسس</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/Futball180TV/97491" target="_blank">📅 01:21 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97490">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">اللللللللههههههه
🔥
🔥
🔥
🔥
🔥</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/Futball180TV/97490" target="_blank">📅 01:21 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97489">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">مساووووووی شدددددددد</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/Futball180TV/97489" target="_blank">📅 01:21 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97488">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">یا خدااااااااا</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/Futball180TV/97488" target="_blank">📅 01:21 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97487">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">گلگللگلگلگگگلگلگلگلگللگلگلگلگلگالگلگل</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/Futball180TV/97487" target="_blank">📅 01:21 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97486">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">لگلگللگلگلگگلگل</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/Futball180TV/97486" target="_blank">📅 01:21 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97485">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/b0dcdf5a8a.mp4?token=JMcebbkfdElwGohqEDNIOlv9NU4L6sKv4ARGO6K9tNCLAYpAyue0kWQ18lhOehrvgehL_sQjp0wpyRcPFBbN5uM55I5zVhM_nOhHPW1r6-2N4r0k4u2v-6TzaN93TK8Uph54uBgsZwUPyzi6CPyqifYOYh30kqoDlybd5yes8ZL7QaxXqROfPhDDoGfXmEOkHvXBK8UcabomsPDxjjTi5IKrjBq-1l3bvR0Ubv013RXZaKwBA_cjVeHKpKTLT5C0pfQ-UpsCKV38_13VgXyPyZ1cXlHGgdvgGnc0UuUP6VqJ_xbcYJvg1DylzMFsHmw_JzZ9ODXeoa2fkCnxs7ZZTyeU5FPSQ0c_n5ryCRNV4k5zySkJDZ4o3T5pwhALKQP27NMt_mgXHdDTeTA_fBZp8BeNDyz6X6uqW2GslOq9LRHxPRR0SnA5F54g6QqEYzS-N5IAqGWoaqHzrHXCKpAPxUt9jPEpYjsobMIdyV0xp98IG7gJ1gA_ne3kQMv3NRpRIzNgZ2waG_O_7yztWN9DHnawopCyI0YZM31-6zUshzhg1WhYHiu-g5r7DQ_Sars4y51jEak2_VEgngl6dC3MuK3tOokVqfPO5hoXW7u3dFkJ9YMNhMKtIdc4AuOm7aSSOQFFASnEnaFjMhU0n3in2yVYhFm1TMkd_z2kR0ywSvo" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/b0dcdf5a8a.mp4?token=JMcebbkfdElwGohqEDNIOlv9NU4L6sKv4ARGO6K9tNCLAYpAyue0kWQ18lhOehrvgehL_sQjp0wpyRcPFBbN5uM55I5zVhM_nOhHPW1r6-2N4r0k4u2v-6TzaN93TK8Uph54uBgsZwUPyzi6CPyqifYOYh30kqoDlybd5yes8ZL7QaxXqROfPhDDoGfXmEOkHvXBK8UcabomsPDxjjTi5IKrjBq-1l3bvR0Ubv013RXZaKwBA_cjVeHKpKTLT5C0pfQ-UpsCKV38_13VgXyPyZ1cXlHGgdvgGnc0UuUP6VqJ_xbcYJvg1DylzMFsHmw_JzZ9ODXeoa2fkCnxs7ZZTyeU5FPSQ0c_n5ryCRNV4k5zySkJDZ4o3T5pwhALKQP27NMt_mgXHdDTeTA_fBZp8BeNDyz6X6uqW2GslOq9LRHxPRR0SnA5F54g6QqEYzS-N5IAqGWoaqHzrHXCKpAPxUt9jPEpYjsobMIdyV0xp98IG7gJ1gA_ne3kQMv3NRpRIzNgZ2waG_O_7yztWN9DHnawopCyI0YZM31-6zUshzhg1WhYHiu-g5r7DQ_Sars4y51jEak2_VEgngl6dC3MuK3tOokVqfPO5hoXW7u3dFkJ9YMNhMKtIdc4AuOm7aSSOQFFASnEnaFjMhU0n3in2yVYhFm1TMkd_z2kR0ywSvo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇧🇪
گل‌اول بلژیک به سنگال توسط روملو لوکاکو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/Futball180TV/97485" target="_blank">📅 01:20 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97484">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">وقت زیادی برای بلژیکی‌ها نمونده</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/Futball180TV/97484" target="_blank">📅 01:19 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97483">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">لوکاکوووووو</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/Futball180TV/97483" target="_blank">📅 01:18 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97482">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">بلژیککککک یکی زدددددد</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/Futball180TV/97482" target="_blank">📅 01:18 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97481">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">گلگلگللگلگل</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/97481" target="_blank">📅 01:18 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97480">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🚨
‼️
نیویورک تایمز: یه شهروند ایرانی - آمریکایی با تهیه لایحه‌ای علیه فیفا از طرف 90 میلیون ایرانی از ترامپ و اینفانتینو شکایت کرده و خواستار پرداخت یک میلیارد دلار غرامت به ایران بابت حذف از جام‌جهانی شده
😐
😐
😐
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/Futball180TV/97480" target="_blank">📅 01:13 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97479">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🚨
🚨
🚨
🚨
اوه اوه اینجارو  تروسارد و تیلمانس نزدیک بود وسط زمین کون هم بذارن که لوکاکو و بقیه جداشون کردن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/Futball180TV/97479" target="_blank">📅 01:07 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97478">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RfIPOzYoMBIYzAA-TQbfRt7-G3J05uepg5gFsxJ0-2BtArJhUQz1A2ZXr-7ltT6NkZtjtwsBOu-hdkqNKyYf8ow8NvucYzGajSlCEABtWvIB13mxeY5ZRxDwUxywpUswXk6JR9jdPcJtpJDTNUgsxquC4dbWT_Gnq0WqEh_BdUa4-ihOZtQ_DoEi-uQjThC62ESd7OUNs3h6Uu3puFNfxFK4P0WcGf8upyWI3A80GtYjKLkl04NEh8MrdG6eGfqOCsrzsxdMvWPGhfkk9Ha-HVBRL6epWLJ0eJD4fKbrfElu6gCao49s77NvJM5qYYEl6J0nQYR8DPDsCXmLgy4INg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
اوه اوه اینجارو
تروسارد و تیلمانس نزدیک بود وسط زمین کون هم بذارن که لوکاکو و بقیه جداشون کردن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/Futball180TV/97478" target="_blank">📅 01:05 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97477">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d52150cb58.mp4?token=Kso1-r6tMvocfG69uw0AO4aWxlEVM9Gd6itU-y73Krb_cf-q1-6rMsDBN0hFEnA9KyOix3XpiR7cnrhXCT0xLJ9HS9Ut_GZDMA8T2aIqR8NMGWlKmkQv0i9MgGsH1IZOQvyMf_Mx8clhXw5ttzruPniR4UGo3ZFWJvsTyu9FlUesSkRfpNTt4SC6-97nLWk5za6_rzF4VTpBpXNgWozLbKoycuAgDMx2Ba4h2KwIoY9nO0f-jj8Y1SiRsobFJCBlIYGYrpVIrSOmbVRFn1Xv-83Azrnuu9hUPht6mH_UucBIGJ0FG-w9uLn4PsMz38vpZ_Xx5nib8Y83iCWU_22qdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d52150cb58.mp4?token=Kso1-r6tMvocfG69uw0AO4aWxlEVM9Gd6itU-y73Krb_cf-q1-6rMsDBN0hFEnA9KyOix3XpiR7cnrhXCT0xLJ9HS9Ut_GZDMA8T2aIqR8NMGWlKmkQv0i9MgGsH1IZOQvyMf_Mx8clhXw5ttzruPniR4UGo3ZFWJvsTyu9FlUesSkRfpNTt4SC6-97nLWk5za6_rzF4VTpBpXNgWozLbKoycuAgDMx2Ba4h2KwIoY9nO0f-jj8Y1SiRsobFJCBlIYGYrpVIrSOmbVRFn1Xv-83Azrnuu9hUPht6mH_UucBIGJ0FG-w9uLn4PsMz38vpZ_Xx5nib8Y83iCWU_22qdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇻🇪
آسمون ونزوئلا چرا اینجوری شده
😐
😐
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/97477" target="_blank">📅 01:00 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97476">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🚨
🇸🇳
گل‌دوم سنگال به بلژیک توسط سار
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/97476" target="_blank">📅 00:48 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97475">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🚨
🇸🇳
گل‌دوم سنگال به بلژیک توسط سار
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/97475" target="_blank">📅 00:47 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97474">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🚨
🇸🇳
گل‌دوم سنگال به بلژیک توسط سار
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/97474" target="_blank">📅 00:45 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97473">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🔥
🔥
🔥
🔥
🔥
اسماعیلااااااا ساااااااارررررررر</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/97473" target="_blank">📅 00:44 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97472">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">سنگال دومیوووووو زدددددد</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/97472" target="_blank">📅 00:43 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97471">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">گلگلگلگلگلگلگا</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/97471" target="_blank">📅 00:43 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97470">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">لوکاکو بین نیمه وارد زمین شده تا نتیجه رو تغییر بده</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/97470" target="_blank">📅 00:40 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97469">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ut2sn2TPhmfwjXjvn4Ww7b3vHHqO_fNfQrIb_vPpoJiQGM8BBnf6i_wEQimXzWUy2pymqUHLPrcJwYd97Hgi5rRoXVDu3rknpq_slpt31T6Uji6-NefLH6DzkMJkTePCwxmGn3MfW5tquPFqtKS7vnf_a7A8D-HdxNqJ7CVZa88dgs0IPfHuCyIVmIY3_L8UoTZmw4BzQZG_xdSEdHok4tDoxevjxFqSUoJw_CecZYWzQoVSwh07-oStqPSPwK4ufFJBw9j2qRlM-dE4V1XAtVg8hTvZDCdqw29k3vvCJPjXyMYCKA65ZZq6YgfLwoDM4sdbq-IxFbNf1qy_UXmYuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
روبرتو مارتینز:
فردا جام جهانی واقعی برای ما آغاز میشود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/97469" target="_blank">📅 00:32 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97468">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r3VR_k6Rx3iO6BsUsrJcfJpT5xf7ZL9pOAcWJLZECJnhqHNWJ45Pvl22NPifmIC9VkIzPsxilwML7pCNcsvQyZuk8Ix8ciOB_rYe7237xw_GTG13V1JvMLfruQui1RDr-RnLHsQBttMJr1PfqKf1_6zilruLNGz3Ywa6HToXwPE7npHTdW_6HhaHZqnRCBaKgGJwgyMANOZ2U4Rruz29M-dUtFS7eKs7xEqhxHiC162pGVWvTM8eXGQjn4jlo8vyUR9xg0XsMfxVufK4YJE7xiRqBLUNQ3d0G5FEhet9x4SGBFRYfLKUojMCMfaZ2XBCULd4JCZOv7QC2cYuavGPNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🎙
متئو مورتو:
الساندرو باستونی به یکی از گزینه‌های اولویت‌دار رئال مادرید برای تقویت خط دفاع تبدیل شده.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/97468" target="_blank">📅 00:22 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97465">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bopFgr9pGbgtu6Qh6HEI3pLzBPa_s-U7_Fj2FXI53cQEt5JYxtWVe2nYMqwWZtoBpEzB-bDwrcdytp5yWJlt1UboZqH77mfU1i9scQH8pnnHiiNh8bkg5tQrmvYuBoPdviqgBR2FbFcVZ_z5ZWVgXpnjNf-4mMkSGHUKaMmd08lOkH_iBQJnJeXAjTP2UbwM_erENZUri7puHAj6EimvdLiSNBmj0a_lDVxeNH58OUVgs-0uVx6Vk8AYPYeWP33IAX9zvtdz1sOsmPIueRjaETHIauqwAU5d-owFVzfsnvRAENFKUwkWfb8VCaAqyyxCrymh9mirjQd3UPw7gkpaHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ci4mbYO3UMrgCvgjJeB-sD5QnF0xeYB5mmD6OP04oK2g61TaJ0L13V1rSQnxbn_PmRG-9quPfaj6iMqtWmprmD5wirbvr0h8YTVM-qrq0MTGO5lIpo5fVCzZKkU1jZ2gY8fMWo7La2s0EsA07TcrM6iPHkvTYysfcf8FmZa6ADNvtKcYStQnoVkIH4m4UQr9oN4-l3dyyptPp2RXuxshhLxvqCFFmXsBTbYR0I39OVr_KHFMWdaa8Nl7TmbXxVkUnCvp8Un2PH1FPISVSvmvrEbo1EsQkEAcoy4QPwp9IgKVdHIyuljfoX-0R_04kyCxgVDWSal77Qt8Cin4K9E9WQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/P8DJ5OO6HuERq_0ad-0y0QRPef_7bBXqqBfw9z5N5AvBHRcRMVdiNJqJzWAa_K3z_GFxravXC8RWUsgPoJxUt33vVMzbitfYcL00cWYPlXql9R4VepY6mkPIJd5oerN5pfzU9HQihIfhJpQnWssvy-KmhKz9T1CiARzFvyoL2gPUAi5NZbiJH90175VzNR6B_0lHrGjh3B7uIyluBmJRn9a18QR-mSBJw-aeFtmGWHFs6t3Rztrxtksxyxk6JohQTJrDjnYR3Vsif7HBwnZqzO4FMvR1DuHM4UBIn9ua-u8siTzEqSCNyMR-x4AoeNRgZKJD5ovzYlK8kHvsx88THA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">جیمی جامپ های بازی امشب
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/97465" target="_blank">📅 00:12 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97464">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OR4LS9hKb6u0BfOcrgDrFW22jiJQiEJ0-zID10Bg7GjtyjCMfAri0ekikYdccsolTaUFFGd7ec9YQIKkh57ALtPBXultufXceDYL5RKg7HZnwzAzbkGFT3pvEBk3aoHeTVIabtPo64aNVRQRKOHa6X3JOnRFJ0hh55h8DAQI9bu17bRE-gagc3QgbhdPO5OZrYmo1eb9kz21EPHuphYbvwCwlGqSW5ONySnyN3qshH1TQJ_h3YOPqOIpqxXUJsvHM3BDdvIt2gF0ZjDIRecox9TG5fheaHuJVd_aedIZkLpQBcmCa3ESD9YiHqKGsuhdSTo3NShExLJki4GjYaemMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#فووووووری متئو مورتو: بعد پیوستن تونالی به تاتنهام، کاماوینگا هدف منچسترسیتی شده و احتمالا مذاکرات بزودی آغاز میشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/97464" target="_blank">📅 00:10 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97463">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#فووووووری
متئو مورتو: بعد پیوستن تونالی به تاتنهام، کاماوینگا هدف منچسترسیتی شده و احتمالا مذاکرات بزودی آغاز میشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/97463" target="_blank">📅 00:06 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97462">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">گل اول سنگال به بلژیک توسط دیارا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/97462" target="_blank">📅 23:56 · 10 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
