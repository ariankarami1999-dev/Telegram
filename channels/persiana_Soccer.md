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
<img src="https://cdn4.telesco.pe/file/RGcu3xmIcfBQPfslLY6VZyssRALkeDEjz3-XfK_3Newv4EzX2eMXZ36aTBQpCrzPGMidn6AzyxyQjuu-MPlPish4jsl4manRXxMD6Wn5g68VH0fxDNeU6Jq_bwnGYGyHvGilN60Na4oFdQ11LfcLR3lhCNVcnkT5llqvW3y188HrKfxTfrsQGElzQ8BAEyDZMJCVGfgr6nKQTiWWV_OHtvF0sqUDlNTDXvNaOsPMFT7HvfEsUUasTQatDETSVBMYCgmrrO1lCUKHWix7yuq5vdir-D_sejNDoL0AJiiQyxPl8PQMFbNM1q8JkzShlMkdEQhfJEBXY9x9WViKMRchRg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 460K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@ads_Persianaaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-23 16:14:42</div>
<hr>

<div class="tg-post" id="msg-25673">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1aeff2dd56.mp4?token=Zuc-4Apwc8w9gVyfbpIH5UQYL9R9tknWth5Pcu0YF47moFKsE9dD8YDUWe1PrYLIum0uweKWfTrgHZhcTMrXp0bB52gNFT2z5znzOSF4o1kT992RISTBEKGOUjGLRMkrCSIjtqqpZgipg0YZTKliT9xee3AjO3Ti0f1TeWUpLX5uCO5h8ZSM6C8pTF5o5aawCeZL8Pmbc4FUV4sh2tM4jC7fEjhE62rhDQEuEAbUDK5W1Gtvucwe3MWyFQDo4_Ot5-Qm0OxDwnUCbDmcAf4f47KAnCoC7twUA2-M58DcZ6thutW3Lm8ye8wdea1K3g266DBZpsp_--gUFm-Cq_hymw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1aeff2dd56.mp4?token=Zuc-4Apwc8w9gVyfbpIH5UQYL9R9tknWth5Pcu0YF47moFKsE9dD8YDUWe1PrYLIum0uweKWfTrgHZhcTMrXp0bB52gNFT2z5znzOSF4o1kT992RISTBEKGOUjGLRMkrCSIjtqqpZgipg0YZTKliT9xee3AjO3Ti0f1TeWUpLX5uCO5h8ZSM6C8pTF5o5aawCeZL8Pmbc4FUV4sh2tM4jC7fEjhE62rhDQEuEAbUDK5W1Gtvucwe3MWyFQDo4_Ot5-Qm0OxDwnUCbDmcAf4f47KAnCoC7twUA2-M58DcZ6thutW3Lm8ye8wdea1K3g266DBZpsp_--gUFm-Cq_hymw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
#اختصاصی_پرشیانا #فوری؛طبق‌اخبار دریافتی پرشیانا؛ اگر اوضاع منطقه آرام باشد در جام ملت‌ های آسیا سرمربی خارجی روی نیمکت تیم ایران خواهد نشست. با امیر قلعه نویی قطع همکاری خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://telegram.me/persiana_Soccer/25673" target="_blank">📅 14:42 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25672">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YeCY7yzELLfWhYa1L8cBls2uT7yWFCTOHTzTgqYoflT18dSdLMbE0BSe6NDvnkhvqvGBcDAwKJR--EXQiMVAKqW6Clc2Su-0Eh3CzRmyHSbHcWqjZBzI2oKwTj7PWBb6-9amSDdOp0apf0p-4NlWAv2KprnOqzfdJ2tyr6cSU-Hm2r6Ck_sI8iV9vCIIp9_6c6GGfFD-5z_zGbJOpxAzbObZ0oauFCkHWW-QeUO0QjXrd0wBw0ysdwHt7tbpmyRjftJZAFeMGSesBAMv5zC9qXitrGYYO3PRE6RnmvwI-iN-MTWq3CbY1urCTzTD3tphy8wiHnyyURgU4j4ZABNbuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#فوری؛فرناندو پولو خبرنگارمعتبر اسپانیایی: بارسایی‌ها یه‌فرصت 72ساعته به اتلتیکو برای خرید خولیان آلوارز به ارزش 100 میلیون یورو داده است و سران اتلتیکو رو تحت فشار قرارداده تا زودتر این انتقال انجام شود. آلوارز به اتلتیکو اعلام کرده تحت هیچ شرایطی فصل آینده…</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://telegram.me/persiana_Soccer/25672" target="_blank">📅 14:34 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25671">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3bc72012ce.mp4?token=uesQdjV1W0msJ5AMVwf0I5R5G_AadY_aA5qA2rMAI8UJYnHWJDUJIu8qRBegiJDOWUE97QNC9oaSVPRCZELEmmQ76ol1BNAVPm9ArvlxqM2-8L6WIiHMFqFiwDIDUVKUONBaNlreEmNPp_Lhjs3FxYZbMRWyWAl8ezTUuC6dgc5pRR-CkzgrwwhCN82fgsB-i7d4F9ftVgf_M_j4EyNuAYtmfWo-sk4Qz-VkFdYT3yHdF037uHFTwgXW3RkXLTFGwRSB_cxhLcl7oXGIeNH4mgyr3Zgoal7V5ph1nKkQ439kwFiMQDaHAgofbuFjLsdHx8pDBjN_gV_Gb9Y5d9MxEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3bc72012ce.mp4?token=uesQdjV1W0msJ5AMVwf0I5R5G_AadY_aA5qA2rMAI8UJYnHWJDUJIu8qRBegiJDOWUE97QNC9oaSVPRCZELEmmQ76ol1BNAVPm9ArvlxqM2-8L6WIiHMFqFiwDIDUVKUONBaNlreEmNPp_Lhjs3FxYZbMRWyWAl8ezTUuC6dgc5pRR-CkzgrwwhCN82fgsB-i7d4F9ftVgf_M_j4EyNuAYtmfWo-sk4Qz-VkFdYT3yHdF037uHFTwgXW3RkXLTFGwRSB_cxhLcl7oXGIeNH4mgyr3Zgoal7V5ph1nKkQ439kwFiMQDaHAgofbuFjLsdHx8pDBjN_gV_Gb9Y5d9MxEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
👤
کریم باقری اسطوره‌باشگاه پرسپولیس:
تو عیدها و مناسبت‌ها هرکسی بهم پیام بده جوابش رو میدم. اصلا برام‌فرقی نمیکنه طرف روبشناسم یا نه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32K · <a href="https://telegram.me/persiana_Soccer/25671" target="_blank">📅 14:14 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25670">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bb91ba980d.mp4?token=P9ijkgYwO2VT0eKcAl1Qm6CuM--sUuYQjI-NMLxrPQlIs8GvQgSR_9jhBHikI_gav_cdBjGVP6iNydX6gjhqfORP4HbTZZTqh-N-KR-2qT1b2yzz8AQ0NIfAujNfAmvU9ld5k3qw34sD-w_eslAqs9DzpiX8n707pJmvMBSnVM4jyTEA8vOkHuw2LcHguEPBA0jcKphQnzHE3vcm-JqE-NY3729789pUZSi37nUBn-IX1V6VWr95HpKv1G9H1IKEczxComMNPJjAEVtatpr61G5Pvpx89tlE2l_yEzLx4xlmkcp079vlH5HDe24kKVwxPUAvuD8SoN0P-KStN2YRu25EiJ6-GkPNsTLDFvXCBlA_a71pXS8V_Osz0RvhziO-a1b0kxFcYkTo7OvSb2hKMqSrXRQ7km6sEg4AbD7rMHnhvh9GMQHR-sDvkg38Y3io648eXSpxOXvYeyPBX9_S3fkfSZ8b2xCp894cyhV5ZY6bFzhFv3q8C3SnXYbb1WghIsm_vyphPlBJ5Ky0GQkywDedgpUt1k0dfzcSNhC7BIvoxCG-cHRwlAjEuOlAHFkgi1cmnUNV0N8uZNMRFrbHLN0vHdNRQovs9klpG3JxfajUKFD_3VauGOcHL5ptnUv39wdQc8kcLb9th4eitI-Wy5AjwlaXUJGPYrpSRxqGz5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bb91ba980d.mp4?token=P9ijkgYwO2VT0eKcAl1Qm6CuM--sUuYQjI-NMLxrPQlIs8GvQgSR_9jhBHikI_gav_cdBjGVP6iNydX6gjhqfORP4HbTZZTqh-N-KR-2qT1b2yzz8AQ0NIfAujNfAmvU9ld5k3qw34sD-w_eslAqs9DzpiX8n707pJmvMBSnVM4jyTEA8vOkHuw2LcHguEPBA0jcKphQnzHE3vcm-JqE-NY3729789pUZSi37nUBn-IX1V6VWr95HpKv1G9H1IKEczxComMNPJjAEVtatpr61G5Pvpx89tlE2l_yEzLx4xlmkcp079vlH5HDe24kKVwxPUAvuD8SoN0P-KStN2YRu25EiJ6-GkPNsTLDFvXCBlA_a71pXS8V_Osz0RvhziO-a1b0kxFcYkTo7OvSb2hKMqSrXRQ7km6sEg4AbD7rMHnhvh9GMQHR-sDvkg38Y3io648eXSpxOXvYeyPBX9_S3fkfSZ8b2xCp894cyhV5ZY6bFzhFv3q8C3SnXYbb1WghIsm_vyphPlBJ5Ky0GQkywDedgpUt1k0dfzcSNhC7BIvoxCG-cHRwlAjEuOlAHFkgi1cmnUNV0N8uZNMRFrbHLN0vHdNRQovs9klpG3JxfajUKFD_3VauGOcHL5ptnUv39wdQc8kcLb9th4eitI-Wy5AjwlaXUJGPYrpSRxqGz5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
رونمایی‌جالب‌از شباهت مربیگری پپ گواردیولا و فیروزخان‌کریمی دربرنامه‌جام‌جهانی شبکه جم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://telegram.me/persiana_Soccer/25670" target="_blank">📅 14:02 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25669">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e-g_760eFBS4glTmHdN1V6JBV9b-vUt36D9sW4kOuml-lrcuBw_jT91NFZy3D3z4vXW_eO_AjsbAMHAlqV_as639xtlRABgACnIu5T0AFugtKmis9wsPTF8NDqr4oT7PYl98E3xB7GBnARnK2_8J_glULzrQxjqGVt_5HiPPTcjVrvcfHUZ_67liX5Gv3r4l8qste4dYYLkweeoMHqFh1avdO68xjqP6HSlfNgZHoeo5BuuA3pmAMecR0rRd8FnElc8XhBKmONKrcL4QXHBKrsa48qKOSzALzyxL06Dx_Z8RvZQvci2ftlDRx_3Hqwt0_TUBgAGo1wUXPFrRWSC3Vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
‼️
کرک و پرتون بریزه
؛ رئیس فدراسیون فوتبال سنگال گفته که: من‌اعتراف‌میکنم که بعد از حدود 10 سال متوجه‌شدیم‌پزشکی‌که همراه تیم ملی بود، اصلاً پزشک‌ورزشی نبود؛ بلکه متخصص زنان و زایمان بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://telegram.me/persiana_Soccer/25669" target="_blank">📅 13:52 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25668">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd10299011.mp4?token=QQBRza5k5GcuT6dfFI5QJUfx9DErIt-mmetRX5B4pNwqoczEPSNU5QcpcUxGFKejZlc4wXhIZWa1AphsAujMB1T2CW04aI_NfMTrVEJuU45pfu7mvlpISGxxhYZZwJjtgxzo01yOWNYvMZVrUhJ71B-IUa-tVrsliW2shTFaS_MJfArc3u0kKYgVgjqby2HV-IgJtqHSol__nUM_VDx82K3Dcq14X33e78OgR07PYfldOIg18Cgx0_5C_cibE1zqO6rWpCrtVMgIXy03Smf6f-5tP_EwBS4fdKdJNIF1H0XnuzuPlDcK8ssPXAUw35-5wmw-edVKH7E5C60G9U6UdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd10299011.mp4?token=QQBRza5k5GcuT6dfFI5QJUfx9DErIt-mmetRX5B4pNwqoczEPSNU5QcpcUxGFKejZlc4wXhIZWa1AphsAujMB1T2CW04aI_NfMTrVEJuU45pfu7mvlpISGxxhYZZwJjtgxzo01yOWNYvMZVrUhJ71B-IUa-tVrsliW2shTFaS_MJfArc3u0kKYgVgjqby2HV-IgJtqHSol__nUM_VDx82K3Dcq14X33e78OgR07PYfldOIg18Cgx0_5C_cibE1zqO6rWpCrtVMgIXy03Smf6f-5tP_EwBS4fdKdJNIF1H0XnuzuPlDcK8ssPXAUw35-5wmw-edVKH7E5C60G9U6UdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🖤
متاسفانه مادر عمو پورنگ صبح امروز درگذشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://telegram.me/persiana_Soccer/25668" target="_blank">📅 13:43 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25667">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b3e0f878ea.mp4?token=h9zustLE1RR_wJ8EsOHKwf0Eq2dH8OsWnkaRa0MiPQ3n2ow0F1EReCkEb4_uS2itELxj1boHTzjejF-nTZNvwYTXV_plGVf9Wgb_-UM18lE2SwCw22017WnN5hwLKTYHB64QSyA77YpN6gWfsTJxad5Fqeu6Pe9uw1JmECOgZkx_donnzVD7usBpphPAABi1ovLX1d3YqWi7E3pn2LYD2KmDxO9ChaU4pLeplsuKiocHxqVDfGg9QrtCaVuZ86vU_hYT8FgwgyfvsBIoW4FiZ-x7GpSvFVv9-xa_C3uWKxR7VqMHGdP9LW--HbvaawwXwRWHT9V8gEPkfQK8zl7LAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b3e0f878ea.mp4?token=h9zustLE1RR_wJ8EsOHKwf0Eq2dH8OsWnkaRa0MiPQ3n2ow0F1EReCkEb4_uS2itELxj1boHTzjejF-nTZNvwYTXV_plGVf9Wgb_-UM18lE2SwCw22017WnN5hwLKTYHB64QSyA77YpN6gWfsTJxad5Fqeu6Pe9uw1JmECOgZkx_donnzVD7usBpphPAABi1ovLX1d3YqWi7E3pn2LYD2KmDxO9ChaU4pLeplsuKiocHxqVDfGg9QrtCaVuZ86vU_hYT8FgwgyfvsBIoW4FiZ-x7GpSvFVv9-xa_C3uWKxR7VqMHGdP9LW--HbvaawwXwRWHT9V8gEPkfQK8zl7LAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🔹
فدراسیون فوتبال و سازمان لیگ بزودی خبر به تعویق افتادن لیگ برتر تا اوایل مهر ماه رو منتشر خواهند کرد؛ با این‌ شرایط موندن بازیکنان و مربیان خارجی در ایران سخت و سخت تر خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://telegram.me/persiana_Soccer/25667" target="_blank">📅 13:18 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25665">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KfugoIbsbMo4pq081ZSxLCYSQsf12SZQiervVSMMTXXxqptruOFz9IJ-5frUMTib2cD1vnY5IUN9WwJls5bJCuYobkvJEdA6zekRndAaiW8g1uagjo9-BtrzA9dSPdKahx9ibgOcPsJryaak49yipz1nL8BTY8yW5NdbyT-JJ5pTLskp4dez3xd1JHwJkwrX7L5QlGVTIl2KnXTJEZFY2PuVRtZ9Vg1mtRale_Sla180yqdTb2pPaSp2e6sJYXPKnzW8_6KsvTWlKgg-r5HRqmYcLEX4SIwY37zC5R0BbdtDtJqAV8PsSrHWLM-H5vYmg8-vLfaTGNxm2nxP9iQR1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/700f8025d4.mp4?token=drmlS5H_oE6ov8QN4CxouvVS6FhE2EdEnp0CYj8MSNlJqMNEte299hpMblrJbednRrIFjp0E397GfdboZMsGTAK26LSN_-OkhRgaFl_QbkxYEzNzRj1B2kK9ufgCsuuG6IkfeDlqO8TpGz1XxEfxB9rXA1rm-PvFmzhStT41sQFlkj0qE4pVoy34reCmt7v7vnFxhP4qmHFuOckXtZYh4qLTBIWtKgQbU4TR6Doo5csZw75Qcu4G_5OkyZFUFpQwwFXg80vshiTVCThEhCczy06cSvS0PYE-JlkDFGVzMFlhEZw6CC9_M2qVHVLhUVeOevM4sTal-qx9fgIAMXTzrg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/700f8025d4.mp4?token=drmlS5H_oE6ov8QN4CxouvVS6FhE2EdEnp0CYj8MSNlJqMNEte299hpMblrJbednRrIFjp0E397GfdboZMsGTAK26LSN_-OkhRgaFl_QbkxYEzNzRj1B2kK9ufgCsuuG6IkfeDlqO8TpGz1XxEfxB9rXA1rm-PvFmzhStT41sQFlkj0qE4pVoy34reCmt7v7vnFxhP4qmHFuOckXtZYh4qLTBIWtKgQbU4TR6Doo5csZw75Qcu4G_5OkyZFUFpQwwFXg80vshiTVCThEhCczy06cSvS0PYE-JlkDFGVzMFlhEZw6CC9_M2qVHVLhUVeOevM4sTal-qx9fgIAMXTzrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
بیژن مرتضوی خواننده‌وآهنگسازایرانی با تصمیم فیفا در بین دو نیمه فینال جام جهانی ۲۰۲۶ به اجرای زنده ۱۱ دقیقه‌ای خواهد پرداخت. عمو بیژن بابت این یازده دقیقه مبلغ ۱۷۰ هزار دلار نقد میگیره از فیفا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://telegram.me/persiana_Soccer/25665" target="_blank">📅 12:55 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25664">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/URFy2dV9_j9mGqY5ibJ3XdEsjKET4QYN8_S1-x2Hr2utCNW5_9J4NDvjOkh5IHsw_MaNuB-qoEmzZVg6hGZEenaX6OcIUigQtIhgFkCytL-j0XZ5sIPhkn20hQ9aoIGIfPuR-Pj0e-QhK31r7zvgqHRTD0bMeC6z5mE4sJer4RGO6b-V9ELMBfX1BMobJJv1wfaMgl1hJP2jvwBDJYiINSUdPyCRZ-eKpZja6Ntk6OjDV34nljJGDzXO0TOj1o29HMG9SRBMwfwBIWjhvRIB0z7Bojh3hnLr2wzY7MChMYzO-uCbxBy2CL9TGnX-ZIFzAeielVxZofaZJcC0mxTSAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟡
🔵
#اختصاصی_پرشیانا #فوری؛ مدیریت باشگاه‌سپاهان‌برای‌جذب‌قطعی‌سامان تورانیان مدافع راست آبی‌ها به باشگاه استقلال نامه زده. با توجه به اینکه‌باشگاه‌استقلال‌تمایل به‌جذب امید نورافکن داره و مذاکرات‌مثبتی با او نیزصورت‌گرفته درصورت باز شدن‌پنجره آبی ها این معاوضه…</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://telegram.me/persiana_Soccer/25664" target="_blank">📅 12:36 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25663">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f07accb99f.mp4?token=HzSQ8szYbF4l6hN9lLUCAWdFv826Fctegxs2RdYa1ug0qDIDfB1Qu3Qupsge9VyE7m1SfW7KIaBvpDOLkn16z2VoT2QPqRpdtt7YwxSVGCMnu47NYdq_hSuUvcNz1Toy3C169CLg6fruQot6vMsNq0F-zw8Ln34siPUY2E1V5WAEQY0Z7i7lPOxAE0aoC75VdXCg8hFmsj0t0w5pecr1_7db9hN1zHkOlJ8l3jO0GOyWGHv14nJ7SAVXmtnQkFFYS20zF2svui0j4WBhIGMyIiRTt7wWcpc_dd08wuoSf86ZelJcWkprwsI9ctJJkHOGYBue0VOkZSn1sDY-cmVBQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f07accb99f.mp4?token=HzSQ8szYbF4l6hN9lLUCAWdFv826Fctegxs2RdYa1ug0qDIDfB1Qu3Qupsge9VyE7m1SfW7KIaBvpDOLkn16z2VoT2QPqRpdtt7YwxSVGCMnu47NYdq_hSuUvcNz1Toy3C169CLg6fruQot6vMsNq0F-zw8Ln34siPUY2E1V5WAEQY0Z7i7lPOxAE0aoC75VdXCg8hFmsj0t0w5pecr1_7db9hN1zHkOlJ8l3jO0GOyWGHv14nJ7SAVXmtnQkFFYS20zF2svui0j4WBhIGMyIiRTt7wWcpc_dd08wuoSf86ZelJcWkprwsI9ctJJkHOGYBue0VOkZSn1sDY-cmVBQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🖤
متاسفانه مادر عمو پورنگ صبح امروز درگذشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://telegram.me/persiana_Soccer/25663" target="_blank">📅 12:21 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25662">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IjqczQ2hFjEwU5rLhHLeod6FfwNprPgAUu5TNpMlUXzVIyBdndff2ot7tzD41lt39MDjJj5-F_rvhaaJCiUwgAnkb6Mn7S9acozqR6ZwvfEDXu7CRZJhk1XFuplFBN8m8TPG4ZhiEHXM2YpIFa_UvqhaxG9E6hdf3kTJ08P0a8qw5Wem_V44V_SgQsmzqP3l9YiPKKYvwfl7m0W0Sil817JBd2V93FadZEr51nMjv5wR7LSy6C1d99drDB-tvpily2Eyp936ZPk3Jy9pBW4nabAHvM6yo4sVWZ0jpNnWLDcP89miJVSeRNJnlrUM0YIUzmgKSqHrx3XiCifq4wNfjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏐
برنامه‌دیدارهای روز 24 تیر لیگ ملت‌های والیبال؛ هفته سوم لیگ ملت‌ها از فردا شروع خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://telegram.me/persiana_Soccer/25662" target="_blank">📅 12:19 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25661">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/thff6Fel2Bxpk8tIkoFktChDg3wjNunqBgKR367EZ7vtDFPmfvgfaqYY5RDjLToLfNE879mEFZGVz_i8Pj0AYZZF6KjpSnc-5NDGbNgdPPCY4L2sZ80SXx6Kw1EM1LvRhmxZNqVzaQFMU9MNjM7RhqydjaZEkvbPMpoBj8n07qdo4S2kbK_nfPBHEBlTYAoJFhG4yHtwr97_eH7kZkZlpmxoypurQNgQmGLA4UYdTro9WmLD5zQKCr_AtSXTTUO7W-0HakcpLjFYqHyrnk7Q35-7UsnZymbAx8P4sp3Gtx6aiW0wHVz4HWhvxqFfHjbj1eWNJ02CL8h1L5Y7fr2m3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
اولین تصویر از حضور یاغی جدید فوتبال ایران درتیم‌جدید؛ سیدابوالفضل جلالی بعد از پنج فصل با لباس آبی امروز با لباس قرمز پرسپولیس دیده شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://telegram.me/persiana_Soccer/25661" target="_blank">📅 12:05 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25659">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FcwOCiV0Iay2BsuD-MEtFD2R1nXrsxriAPrpxvVTSKxQbgdKj8-3BMs0SLNZjJzGeS22FbnfQU-ljWVtBs0pTVo-FEERq03druKbj1aZCsXDza5Hz5Y564R-HPdD6GmH4qebjGeUE63quA2vG9UGFbcLmmHfYPB2ULb-ov6yY7pBHOtWOuCJoCAKphmt9h5Zd_lDR9Z9R3s7sORUMsOpHTVeZeokXkGY9uUwVqHCBPNJNoflaaX6afFMO0y9mC47EQ09jKW2iJXSI0lT3CsGAtzSBtYEKC2vUZab4uLx4bm1cPDs-SV-PabizoYR7s9K4fG3beyHMBVNR7D86N8ekQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
#فوری
؛ افشاگری‌برگ‌ریزون عادل فردوسی از امیرقلعه‌نویی:
ماجرا از این‌قراره که چند روز قبل از دیدار بانیوزیلند؛ امیر قلعه نویی به مهدی تاج زنگ میزنه و میگه‌من تو فشارمالی‌قرارگرفتم و همین الان 140 میلیاردتومان‌میخوام‌اگه‌جورکردی خب دمتگرم اگه نکردی من انصراف میدم و روی نیمکت تیم ملی دربازی هفته اول جام جهانی مقابل نیوزیلند نمشینم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://telegram.me/persiana_Soccer/25659" target="_blank">📅 11:53 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25658">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OKY87OkvvJkWdtJFwZ-a_QhEOAFWuxBrVb5in188nSLqa5hNnnmsCAoOQm3SSLLY4zABcM3D2n5BrN--RgeRSvzDW70vHwipS-ZJrZ5DJA2arP4bsS0xgK7-baGte8Ie1DlBUYRmI4zoi9oz5ltIPTeZPL_U9zXgcwADYy7FKS6-RC3CaMyVtjO850BuniDBJSvDy1-rMJKdXH9jolw8umJDqSVP9AwgRfk9SQAKNZ4V0b8-caNRoOLYF-gOyRubBGqnwjqZKSpZ5CsKSBucdDNag2hYJAC5rID-BhhLHblxIwXil90qXbNrmBY_etRZfZYx_BJBpVOevHU4fatsow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
5 داور نامزد اصلی قضاوت مسابقه فینال رقابت های جام جهانی؛ علیرضا فغانی در رتبه سوم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://telegram.me/persiana_Soccer/25658" target="_blank">📅 11:40 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25657">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/91bb7a3c33.mp4?token=F9ao35pfWVJNf-gfAOcpgk_qbeGXwFIYe5i1S0vQLSgxF6aDgIMtwHZJsA9p6egK-KF-TNyztGTbJfneIunf4jEW14_LE6aYWB7aLj_k6IHmULowDslnzQeaVG8sB4_ttuNkrqNWGkueS_6Nw1V8bZbgh0qaKDTeT4y2V8WPk532qaC2clDKJRs3JH3e9K3wL_oUdlNtsNYXRcAveBtYkIuIkXZGkefdvIyjhWTp0mC3pMSRObtRbuAzNTFlcv3uILuEQG1ijprQmXprmXSd644iIBy4kgX3IlAbrvMHSq8kC8IVrATWGJfWC6pturpgZ0-b2GIMLI4BxIgzD2Ax3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/91bb7a3c33.mp4?token=F9ao35pfWVJNf-gfAOcpgk_qbeGXwFIYe5i1S0vQLSgxF6aDgIMtwHZJsA9p6egK-KF-TNyztGTbJfneIunf4jEW14_LE6aYWB7aLj_k6IHmULowDslnzQeaVG8sB4_ttuNkrqNWGkueS_6Nw1V8bZbgh0qaKDTeT4y2V8WPk532qaC2clDKJRs3JH3e9K3wL_oUdlNtsNYXRcAveBtYkIuIkXZGkefdvIyjhWTp0mC3pMSRObtRbuAzNTFlcv3uILuEQG1ijprQmXprmXSd644iIBy4kgX3IlAbrvMHSq8kC8IVrATWGJfWC6pturpgZ0-b2GIMLI4BxIgzD2Ax3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
افشاگری دختر علیرضا بیرانوند گلر تیم تراکتور دربرنامه‌امیرحسین‌قیاسی: بابام خودش استقلالیه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.7K · <a href="https://telegram.me/persiana_Soccer/25657" target="_blank">📅 11:13 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25656">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c1f067d59f.mp4?token=TkH12maaxsESPIB4J2zGr3rgYDpYwvnbbtATCdUDd4FItdgL8s7GJ7Tifs_ICZbgoiWaB-N0o9PGE8teR4gjx5kKOfUKXQpSbTarVyhAhNlnfjWnT3-nN0QDAVm4B-vKQGReL1e3nPZ2ecrderuD7GSLkRUHZqlH2oag6keTaFSXbKgn-KlqaZ8AB3xUUOfvZLSdKQJzTNnly-utYfmL_vo6Mi2BjkYY8QR7_Eavo860Zk_s7piOtlQ2Ax9pGv1fzM86P-IdMb05lfBWyonTawYuu-IhDb9SLQMb3x1iiub7spZUFKM1xQxS8E-Bgn0TKe8b4f9e2OCEMN-MrWfTCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c1f067d59f.mp4?token=TkH12maaxsESPIB4J2zGr3rgYDpYwvnbbtATCdUDd4FItdgL8s7GJ7Tifs_ICZbgoiWaB-N0o9PGE8teR4gjx5kKOfUKXQpSbTarVyhAhNlnfjWnT3-nN0QDAVm4B-vKQGReL1e3nPZ2ecrderuD7GSLkRUHZqlH2oag6keTaFSXbKgn-KlqaZ8AB3xUUOfvZLSdKQJzTNnly-utYfmL_vo6Mi2BjkYY8QR7_Eavo860Zk_s7piOtlQ2Ax9pGv1fzM86P-IdMb05lfBWyonTawYuu-IhDb9SLQMb3x1iiub7spZUFKM1xQxS8E-Bgn0TKe8b4f9e2OCEMN-MrWfTCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
کسری طاهری مهاجم جدید نساجی:
من اونشب تو شوک دعوای آقاخداداد باجواد خیابانی بودم که به یک‌باره‌رسانه‌ها خبر دادند که پیوستنم به پرسپولیس منتفی شده. بله از الان به بعد بازیکن نساجی هستم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://telegram.me/persiana_Soccer/25656" target="_blank">📅 10:51 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25655">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OylnSll1Zio04qumMO2xUQ3qnnmS0VFX1a78kKGXtAsBxSmqGEbAnzU7qj3oT-UxM0gYuyoNDqult2idAYKr4tqM51AhuBjffj_zkesGjsBe_SN_svDGIDZU4DQ5Nwekuz0moAbaBIMzYjTrHqfWTl0vICJZu2dCnWiatRpI3xMOv_-DyLET7Aup2DX7V90WfiTH994XU63IR_zzwQYgD3qIIdcc3eaFo71_iJGysBqVbC_SWbnh8Wl0_yRuBsiDaaegqZEHvF_QdQkaXoTmxTwBUW0c90P_hIhBTe3Cdxm5JSczdtWOVHVDz2gzKLLw3UkvZOAbxSZK0_jCFHFwWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تاییدشد؛ باصلاحدید کادرفنی استقلال؛ آرمین سهرابیان دیگر مدافع میانی استقلال در لیست مازاد آبی‌ ها قرار گرفته و بزودی از جمع شاگردان سهراب بختیاری زاده جدا خواهد شد. پیش تر عارف غلامی نیز در لیست خروج استقلالی‌ها قرار گرفته بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://telegram.me/persiana_Soccer/25655" target="_blank">📅 10:27 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25654">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a5705053c4.mp4?token=CmxMzGg8Z9n7MeRJ_zkMB4Pf5kfsI0ttrwCDCAu4ZYm3nqUpjDCFfQ6TW5CVFUDbl7Elnr9S30w111zH7Ac0ZVzGkFV8hke0h_OzK9bgiLB-WLXON88nfCD7tgnGHwOsr9JZU88DnRZjtY6vNXmP2ASRoGTyr5ieQCZ-0_FCnvIm9OLjtCS40f_dyf_h9tmFyaxyGN_OuS7r6rrG_Vu5OltF2bJB2rLKMK01kkqjLRALc9_qoEMToYdYSIZIiJgEdrkP5lzqMXjGMw62XuvMkzYitKUdSxVj_7P8JV5tFvvrz32gTUdyQZNWZ5kBkS-xgi7m1IJJS1pXmOLwlrpOqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a5705053c4.mp4?token=CmxMzGg8Z9n7MeRJ_zkMB4Pf5kfsI0ttrwCDCAu4ZYm3nqUpjDCFfQ6TW5CVFUDbl7Elnr9S30w111zH7Ac0ZVzGkFV8hke0h_OzK9bgiLB-WLXON88nfCD7tgnGHwOsr9JZU88DnRZjtY6vNXmP2ASRoGTyr5ieQCZ-0_FCnvIm9OLjtCS40f_dyf_h9tmFyaxyGN_OuS7r6rrG_Vu5OltF2bJB2rLKMK01kkqjLRALc9_qoEMToYdYSIZIiJgEdrkP5lzqMXjGMw62XuvMkzYitKUdSxVj_7P8JV5tFvvrz32gTUdyQZNWZ5kBkS-xgi7m1IJJS1pXmOLwlrpOqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صحبت‌های ایسان اسلامی درخصوص درگیری شدید دوشب‌پیش جوادخیابانی
🆚
خداداد عزیزی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://telegram.me/persiana_Soccer/25654" target="_blank">📅 10:08 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25653">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d33fe4e361.mp4?token=TS-bGC3qsO0zTeRGfUZmm_3Kqwz0Hl0QZdHyZjDibeWYUVi2Fd56atIOjZP06MJ01IGmXkrCptPWfBl5szsO8_fhtea9WzxLz8uw-akcKQDRO1ZDu_SzbZRLkHbn6CR8EGDokig5ZbT7_qnpqZlikRD2-aNUOb_vFx53cOunCvRrK0BPTLfUWa52BiLX11UYGs_MjlxqIs-OT16VAuRo9zaB82RCMi4a4A_dyDhd8y0lR2KhNDLYpf3EkF1rg8pysrOIfb-EPCSKcehNmPXuoKbO7_OcO0355Tn73Ms7t6BJ8AVjknwJ97X-K0o-c-iM4TvZjZYHNF74rfGRSb-dGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d33fe4e361.mp4?token=TS-bGC3qsO0zTeRGfUZmm_3Kqwz0Hl0QZdHyZjDibeWYUVi2Fd56atIOjZP06MJ01IGmXkrCptPWfBl5szsO8_fhtea9WzxLz8uw-akcKQDRO1ZDu_SzbZRLkHbn6CR8EGDokig5ZbT7_qnpqZlikRD2-aNUOb_vFx53cOunCvRrK0BPTLfUWa52BiLX11UYGs_MjlxqIs-OT16VAuRo9zaB82RCMi4a4A_dyDhd8y0lR2KhNDLYpf3EkF1rg8pysrOIfb-EPCSKcehNmPXuoKbO7_OcO0355Tn73Ms7t6BJ8AVjknwJ97X-K0o-c-iM4TvZjZYHNF74rfGRSb-dGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
علیرضابیرانوند: توقع‌داشتم‌عادل حتی به دروغ از من حمایت کنه و بگه‌مورینیو از من تعریف کرده:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://telegram.me/persiana_Soccer/25653" target="_blank">📅 09:39 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25652">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b3c3b52fc8.mp4?token=LMmLVHYwTjFfCRVSx0BGe82946OvTa3sOiG7vjvDoh3E1ZGVTe_3EzWBxR54AKOH-XAb7Ms6iGZ8Jd0k5DCTsIqDSlCE68A8_5SbtR1aIxEXYvBVfjMoFrZ5evjvuDrlhBJevqfh-8QFfRgwnnXdiGesjUgJ1I2rXxfBRmjNAan8v5mJQ4V4v_O-u0dOS3YsIpZmQVik-AsuFWCL4b-C-aYoFH2n_I0htSQDsHm3NEXkjgcQReoq7U3yEz9MRpYadCy2uX4gSWmAwfsitLcSoYndz-V0eFkuqRMOtdCGnjuys_dmNOPukJegybag0uQYzQ93q65mVrHj1x2W3rpcNDti0c1X-m4S-PvUuwqqj3xa_4wqao-LeBJgBjQbZZqIvjpDn8QSUNhksDie0269enwB3xTVAcQ-pL4Ge3htPgnUlr9E-hx07-APCwUUJ38YDYrEkocmMGq93KMFsDWHWRcf7OEU1b4_eMyf3SSHS0SZBlA9AhR7dffzcWckpnHYyp9PB-FvcbBY4z9QROBCfJNM7UOw6Ma-0lbLQw4FHLAc9ZitXlT8PUArRI-AXya3rFlK9dZWOEZeo8QnttLw5bgtqFVQa30JtHNoQ1Np5Dog25PYtKYqC5vqDeAdy1dVzzzejB6oH66ic9rEFSJ5yzjNXmUZAb9LDu7h4a3IJ2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b3c3b52fc8.mp4?token=LMmLVHYwTjFfCRVSx0BGe82946OvTa3sOiG7vjvDoh3E1ZGVTe_3EzWBxR54AKOH-XAb7Ms6iGZ8Jd0k5DCTsIqDSlCE68A8_5SbtR1aIxEXYvBVfjMoFrZ5evjvuDrlhBJevqfh-8QFfRgwnnXdiGesjUgJ1I2rXxfBRmjNAan8v5mJQ4V4v_O-u0dOS3YsIpZmQVik-AsuFWCL4b-C-aYoFH2n_I0htSQDsHm3NEXkjgcQReoq7U3yEz9MRpYadCy2uX4gSWmAwfsitLcSoYndz-V0eFkuqRMOtdCGnjuys_dmNOPukJegybag0uQYzQ93q65mVrHj1x2W3rpcNDti0c1X-m4S-PvUuwqqj3xa_4wqao-LeBJgBjQbZZqIvjpDn8QSUNhksDie0269enwB3xTVAcQ-pL4Ge3htPgnUlr9E-hx07-APCwUUJ38YDYrEkocmMGq93KMFsDWHWRcf7OEU1b4_eMyf3SSHS0SZBlA9AhR7dffzcWckpnHYyp9PB-FvcbBY4z9QROBCfJNM7UOw6Ma-0lbLQw4FHLAc9ZitXlT8PUArRI-AXya3rFlK9dZWOEZeo8QnttLw5bgtqFVQa30JtHNoQ1Np5Dog25PYtKYqC5vqDeAdy1dVzzzejB6oH66ic9rEFSJ5yzjNXmUZAb9LDu7h4a3IJ2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
به‌ بهانه بازی امشب فرانسه
🆚
اسپانیا در نیمه نهایی یادی‌کنیم‌از بازی دوتیم درجام جهانی 2006؛ فرانسه‌ای که به زحمت از گروهش بالا اومده بود به اسپانیای آماده خورد که هرسه بازی‌گروهی رو برده بود و اغلب فکر میکردن فرانسه رو هم میبره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52K · <a href="https://telegram.me/persiana_Soccer/25652" target="_blank">📅 09:32 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25651">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y9cNZh8-Ho7SR6tmYJZWCCQ5PREJUG2TRc531obHfByhHMatBzKu5FukuA4ji6GLTHnBJbmYnIS9NUSRHATfj6vJGEqNCIKfMlHqlKE7OGrWfEIRSrN9aXF1LeYikIpnXPHrIRbU3DHlARJSXyjR1uVyWg4FL0_k6OU0hbSr92NatBAbLUM2RE77jqm6Zub8JF-zxeYQVvRqroEjWYHHzS920CgRZQvbxFtcPmrxy5SG3KMznwEavRki1jjUPM-eTWXtzizq9aTfS9nCqHmQ5mGGQc9RRMAzUZS9kFPnnnTH8muw1fxDIKYV7ORzWfq9n5a0Hvqh-TVJp_HPUGjSQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
👤
#تکمیلی؛ با توجه به اینکه قضاوت دیدارهای نیمه‌نهایی به علیرضافغانی نرسید؛ شانس ایشان برای قضاوت بازی فینال جام جهانی بسیار بیشتر شده.
🔴
فکرکنم‌دیگه هممون دوست‌داریم که آقای فغانی فینال رو سوت بزنه. انشالله که نخوره تو ذوقمون و فغانی بعنوان داور فینال جام…</div>
<div class="tg-footer">👁️ 52K · <a href="https://telegram.me/persiana_Soccer/25651" target="_blank">📅 09:18 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25648">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/298c4f2fe3.mp4?token=ULxb71JDSZb1AEbQadLJMLYHCR2RHFqKMwFt-TpdsjGqftOIqYnrhQQX4qvPgGkV6SRRS4Wk7PBrm2dA8HqGKfbBswRZ0cTf9k2Qa372hmtapO-_gwqsusNuaQVo0kPUR3GPVxxyf-VrxWEdIlMJ5QlVbyzEtfU6zSvgGLm-3Yxw83SRDI1C4OKlqiN2BOWIVsHXKrAhYfeANhoqnohMXRyVZGWsSYRBQP245HgQ664Q4ajGzheC3xZWlvuLGfWf4gOmxny6d9l1GbQncoCoZE6UDgn9_73aQG3Ypb1fLSLi4-jWkVvWPySSwPfRsFSI0s89njm3DwCV6B4UBOiXgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/298c4f2fe3.mp4?token=ULxb71JDSZb1AEbQadLJMLYHCR2RHFqKMwFt-TpdsjGqftOIqYnrhQQX4qvPgGkV6SRRS4Wk7PBrm2dA8HqGKfbBswRZ0cTf9k2Qa372hmtapO-_gwqsusNuaQVo0kPUR3GPVxxyf-VrxWEdIlMJ5QlVbyzEtfU6zSvgGLm-3Yxw83SRDI1C4OKlqiN2BOWIVsHXKrAhYfeANhoqnohMXRyVZGWsSYRBQP245HgQ664Q4ajGzheC3xZWlvuLGfWf4gOmxny6d9l1GbQncoCoZE6UDgn9_73aQG3Ypb1fLSLi4-jWkVvWPySSwPfRsFSI0s89njm3DwCV6B4UBOiXgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
👤
افتادن شال یکی از مهمون‌های امشب ویژه برنامه عادل فردوسی پور؛
تعجب عادل عالی بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61K · <a href="https://telegram.me/persiana_Soccer/25648" target="_blank">📅 01:21 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25647">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dlyp7QnlZ-DM6220aLNe3r2M49NyU_QifVckbIgBDR6cFdExiqAo6gqS7QJvt1HYxSakQ1SX6igojlyl-heg5oSnizLC8omXbxzr58CJjx1gRLXMICIFuyDQ-xqd5WxDEKcX-Exx4yqxqve6hPLxnK4_yxNl9KvEDrYY6tt7AVK0sMGMAHebRsRwcrMrZSHSrIUZTQuaPbwpwh7WIgRQMVL8q8m-vXt_nyVJy-no8GheOLL-Is2CSpFnCYHPlEkMLoY39ooR-CDtfubU-CrjdE8Mc8PEBi5ge5nzzA3EBs8CKYSq2SBA-Z1M_5u0KXGm4B8-5XhQyW6SI0jMFVTOeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔵
👤
علیرضاجهانبخش کاپیتان 32 ساله تیم ملی:
تا یکی دو هفته آینده از باشگاه جدیدم رونمایی میکنیم‌. اگه‌ایران‌بیام بین استقلال و پرسپولیس یکی روانتخاب میکنم که از همین حالا انتخابم رو از بین این‌دو تیم کردم اما همچنان دوس دارم اروپا باشم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.7K · <a href="https://telegram.me/persiana_Soccer/25647" target="_blank">📅 01:08 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25646">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U98Ut2NyL3zWMm6CwRhKecP_XPbYAagN1B-wOUcZfcmCykXZG8vjP5khGSS8tf_RV7lBNai0tuqVlSIW57ao8bbl-U6zBOwsG_rkFnSXbudbAgcwLUQg_VtXIoUrl7ieKo2NnpWbuT-MWYWhojcsz8k1V5PvZWOMmw4vllyDauPGpe6Ky8M85lY30CuGovb3bMlqul1wTWDfU9sijHvaLM-UsC_aNy5Y9C0Zjz0pziDKShF70rFemQjZvXp1G5VJmDFJLQJ3QAJ4Teao4d0R4SqGJqn_OLRgtHSZc-OkeXeQ6eCot8moKaxJpG0QjyHnbq8TORKJ-TjqM0eGdwBlyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تنها دیدار مهم امروز؛
نبرد فوق‌العاده حساس دو تیم فرانسه و اسپانیا در نیمه‌نهایی جام‌جهانی 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60K · <a href="https://telegram.me/persiana_Soccer/25646" target="_blank">📅 01:00 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25645">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e3e63bfe28.mp4?token=pAOuclXc7VqvjvzDptGyDa81Ceu5UvgRFHkhRigUZ8uEviIqlTV9a5RVfQDq5IhQOX_UQlvpf77cQp7fVyWBPRqVK3L18RPLc6j8NzGd0sgPGr4ncjYljkYZTgQgbwpPke0Uf_d1uGmVJYR2TnTsI9B0b6EyyT3NN4cqNeDS-c3GAVhNsK3l5LGypLPf8Ei-3gXBDFuVk8BhLJ5A3orAu8j4xJlrbiyubgzqemh0rd_V-NpEUtWaVl4uSP3YysJWy6EOfVn6dHJCV9yZ1zGR96g9hfKtV2QuNl2K1_4TXJ5rw0R8qFXKRJwzYkJvZeZIknFp-VPBspPXgfRvxHjdfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e3e63bfe28.mp4?token=pAOuclXc7VqvjvzDptGyDa81Ceu5UvgRFHkhRigUZ8uEviIqlTV9a5RVfQDq5IhQOX_UQlvpf77cQp7fVyWBPRqVK3L18RPLc6j8NzGd0sgPGr4ncjYljkYZTgQgbwpPke0Uf_d1uGmVJYR2TnTsI9B0b6EyyT3NN4cqNeDS-c3GAVhNsK3l5LGypLPf8Ei-3gXBDFuVk8BhLJ5A3orAu8j4xJlrbiyubgzqemh0rd_V-NpEUtWaVl4uSP3YysJWy6EOfVn6dHJCV9yZ1zGR96g9hfKtV2QuNl2K1_4TXJ5rw0R8qFXKRJwzYkJvZeZIknFp-VPBspPXgfRvxHjdfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
#فکت؛ازوقتی‌توخل‌به‌‌یارانش‌اجازه‌داده بازیکنان انگلیس دراردوی تیم‌ملی‌میتونن با پارتنراشون رابطه داشته‌باشند جود‌بلینگهام یه تنه این‌تیم رو به مراحل بعدی جام برده. انگلیس دیشب با دبل بلینگهام برد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://telegram.me/persiana_Soccer/25645" target="_blank">📅 01:00 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25643">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hZUb9zJGgXOLUJriy4iUeTkgXJ4QfxxtfD7NGpMMqLWNDzBx2QosNRO_p03cpLyblD59Ukyw-RBn6EAdMzy890KJFhhxGBJJrRgbqYs6zbpBDLHXfkuh4J02g4Jawso0c5w1fV-2vMO9omMQW3nCTQh_1IMZbL080SkaS1gmx43aLGZaii5nyjPxkrQBg2uKVB-iroBaNPzsF-CMjlHazdedrWmIh6HjD5W-w96f1TyQOalka3RaGDjcxRutXWdswFpFIwxD9oMvYKB4Q5vUeH4QKm12Bcx-aQ2om-qFa1bI3xM1abYrZlMZMh266BJny3RlIiUDG6OxmLlCqYjOCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇹🇷
با اعلام باشگاه فنرباغچه؛ اسماعیل کارتال با عقد قرار دادی دو ساله رسما سرمربی این باشگاه شد. ارزش قرار داد دوساله کارتال پنج میلیون یوروعه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://telegram.me/persiana_Soccer/25643" target="_blank">📅 00:43 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25642">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/98ca4a5638.mp4?token=TdAwcMwyyWaYKc4I7b6r_xZomaqiBBNxi_4HLY27jNsoGU0zDpILuCKAV7_SsmSi35uQDY5remP4X2-Ssqvc9UK4ngSmkG0Aqy-cpevs3Zyo6pIdfTa16rOf-Ly-bD5KqYvDj6SHXRV3GlY0sv49_s_4N9p2VinNRbac1choWHcUR-CB6kdNzUs4UmTNRqtIhb_E11dvUOcX38AnogE6kuQ6nHPAesQYPbbmusAhMk-puHqQctAzDSjfFo_CFJy9zfXLUu-dbLLqId1LfCMr51G3kEa4XZbU7bcFdZKJFR8RzK_Y1DgxRwmpUZmzRdyolEsR90gN5CAYDka72Nj_MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/98ca4a5638.mp4?token=TdAwcMwyyWaYKc4I7b6r_xZomaqiBBNxi_4HLY27jNsoGU0zDpILuCKAV7_SsmSi35uQDY5remP4X2-Ssqvc9UK4ngSmkG0Aqy-cpevs3Zyo6pIdfTa16rOf-Ly-bD5KqYvDj6SHXRV3GlY0sv49_s_4N9p2VinNRbac1choWHcUR-CB6kdNzUs4UmTNRqtIhb_E11dvUOcX38AnogE6kuQ6nHPAesQYPbbmusAhMk-puHqQctAzDSjfFo_CFJy9zfXLUu-dbLLqId1LfCMr51G3kEa4XZbU7bcFdZKJFR8RzK_Y1DgxRwmpUZmzRdyolEsR90gN5CAYDka72Nj_MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دعوای شدید و مجدد خیابانی و خداداد عزیزی که مجبور شدن پخش زنده برنامه رو قطع کنند:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.8K · <a href="https://telegram.me/persiana_Soccer/25642" target="_blank">📅 00:29 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25641">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5d3d13a462.mp4?token=F7WMF42KCbpAxeiAC4PWSvM0BdFPrsH6VPNOMWQX08mEPNfPgw_4tyS4s22G4Gu1NOc5G83KXo-fANpMZ5X4Pp_9q95XWzmMttR_6jyEwVviOjZZWNYPeN2Z3C5iO38qx7FHmHJec09zB7xRjtMBoOqgLCdqeMd86ofH_Mq2Thcvfll8RtFeTFDezhhbKIFQCIcnQf9wkwlzB0yuZF4ARNUf6O2YX1Qic3WlqMGlHtDzcu5_FD-NGzsok8VcqSMWin4g61DfgpATDlFEq0d-foXDfsb0V2kg3_SCB7Bkp_s4LMv4WxXFHzo5AGI0SwNqPpeTp_nuhGNPdG8xl9qEpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5d3d13a462.mp4?token=F7WMF42KCbpAxeiAC4PWSvM0BdFPrsH6VPNOMWQX08mEPNfPgw_4tyS4s22G4Gu1NOc5G83KXo-fANpMZ5X4Pp_9q95XWzmMttR_6jyEwVviOjZZWNYPeN2Z3C5iO38qx7FHmHJec09zB7xRjtMBoOqgLCdqeMd86ofH_Mq2Thcvfll8RtFeTFDezhhbKIFQCIcnQf9wkwlzB0yuZF4ARNUf6O2YX1Qic3WlqMGlHtDzcu5_FD-NGzsok8VcqSMWin4g61DfgpATDlFEq0d-foXDfsb0V2kg3_SCB7Bkp_s4LMv4WxXFHzo5AGI0SwNqPpeTp_nuhGNPdG8xl9qEpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
👤
فیروز کریمی درباره‌انتخاب دومادش بعنوان سرمربی تیم پرسپولیس: انتخاب خیلی خوبی بود‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://telegram.me/persiana_Soccer/25641" target="_blank">📅 00:18 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25640">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c-g1P5_rbGE-IignzlkknBCbvY2B9BA68Rn9eShAE9cTHZ2Y1GHPStqRSxIz0u4-3WAC1WG3yIVWO9MPDkqYcg9Ze8woNfjYtJOyU5CYzDVTN6HrEUYEMXpjKZhmb1fuEO53JJ4EmpJYUI33DTOmEKUZn-pZ9PzvxAkDZRQbHunLIZ2m4ViN_CjTJYX20uNmtbuO8YYzCrX8YoqOzxtr_2Z72hH8NwUo99IVMt2BdkZu5R_JXbqn7l_Cwu29h4jmVHmdeMFywpOXJjO0ccXkU24RNdRMRBb4hX9CW6mEuPQMr74L9DX_F0a_rtEoa9Q3NdiqXqBErBZhnljERur4Bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇮🇷
رامین‌رضاییان ستاره‌استقلال درسفر خود به فرانسه‌کیفی‌از برندمشهورHermes به همراه داشت که مدل‌آن Birkin 40 است و قیمتی حدود 21000 دلار دارد؛ معادل 3 میلیارد و 800 میلیون تومان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://telegram.me/persiana_Soccer/25640" target="_blank">📅 00:07 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25639">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FnU6Rv4oM2vLuFkQvzuZBdFZrDpQVQ2CXuAKXunWe4REqmSxXKR5KItmBO3flvjB_qa-ASihGK7-wR6gigP4ut4b8mRKF877rDaN4Zy8H9uZu-kX40ZcGYmCYiU8B7KLkIdN3HOhUy4ycJe4yodHyQI74F6Zt5-4sNSRnKLY_xX2-K-DDc3V-ovqZQGLVLroo7YxMzQzUuC_Vjrmn0G7rXxZDAc-yLril-30eYSJhYPTQytYeu0PxC0R_CezGvgYRmfIGMh_6xksN7BsBoWgdK5LDLIDrwEH37sSRyIQrI9ZbvnNsAC65yeRKrXbY6YAuHs_oqw0ixJIgtGuxOrBfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ باشگاه پرسپولیس باارسال ایمیلی به‌باشگاه‌‌الاهلی‌خواستارجذب رضا غندی پور مهاجم 20 ساله این تیم شد. اماراتی‌ها پیش‌تر مبلغ رضایت نامه غندی پور رو 2 میلیون دلار اعلام کرده بودند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://telegram.me/persiana_Soccer/25639" target="_blank">📅 00:01 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25638">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NwaYKvm5ETecedpAls7JctjksrxgsahYjcc9b1Kmmb4CZjclXIgiKudRld1xtWNrvs_Nhl4IYi8AeiVhAOsEnPqIygzjT5DX74h0be8xfpq6TSeowpUMutduCbGXTG-qdnMO79gTWnrQkmv3avkgGPZCd8TddsZ3ZBemHNdJQo_sBGvgjbEuJDKcqBKKuL9Bm0zGmZ5CpJdESBSwsT65OgtphYEjaRFOG5p8VYzAwFCfkAAtKCaFdkIyvwGAPTNKx5fOyQiU4qt1fNwBBd2u6js_UikEnkThNI8Pb03pwhZeTJrNrjRpG6u-EPKbRxaKOEXbc1DEwfeRlD9CqUKBhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
این صحبت‌های مدیرعامل تیم نساجی نشان میدهد درصورتی که باشگاه استقلال در جذب جواد حسین نژاد عزمش روجذب‌کنه با مبلغ زیر 3 میلیون دلارم میشه این بازیکن رو خرید. فقط مذاکرات باید حرفه‌‌ای‌باشه و بی‌تعلل مثل آقای زندی‌. گفتنی است باشگاه استقلال برای جذب حسین…</div>
<div class="tg-footer">👁️ 58.8K · <a href="https://telegram.me/persiana_Soccer/25638" target="_blank">📅 23:55 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25637">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8ae1ae07d.mp4?token=Ei4qEH_XFgwIn4EFzpAq3Nbmmw19ixWaP2DLcEFsYPa8Q_cE1QAxID-nZr7T_mPA3QXSY_TsD4au9wDDAKTbBFBWPt8_tVbkRMoKdBEYkJ4CR_CUUVlZXhkMvR1eZQ2Kv2wNr2ZWR-rnHTK7xXCA530k8FDLS3slXpgSdlqpQVvllHG-vFOY9JHRV4597DIqSwsMJwBFL3mXtmGeP7Z4QDD-UhdEQ_cVsJTEw61d-qAax8K_7dOYHwLNvNhUC3kJeIpR5apBuMV8cl8uWTZU17qRs3jWo0UPXK_mXtVRwsMaOpkiqLRf9pbrtBNh3YjrvuWGGHhsEq7qoj6U4DHkkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8ae1ae07d.mp4?token=Ei4qEH_XFgwIn4EFzpAq3Nbmmw19ixWaP2DLcEFsYPa8Q_cE1QAxID-nZr7T_mPA3QXSY_TsD4au9wDDAKTbBFBWPt8_tVbkRMoKdBEYkJ4CR_CUUVlZXhkMvR1eZQ2Kv2wNr2ZWR-rnHTK7xXCA530k8FDLS3slXpgSdlqpQVvllHG-vFOY9JHRV4597DIqSwsMJwBFL3mXtmGeP7Z4QDD-UhdEQ_cVsJTEw61d-qAax8K_7dOYHwLNvNhUC3kJeIpR5apBuMV8cl8uWTZU17qRs3jWo0UPXK_mXtVRwsMaOpkiqLRf9pbrtBNh3YjrvuWGGHhsEq7qoj6U4DHkkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
علیرضابیرانوند:
توقع‌داشتم‌عادل حتی به دروغ از من حمایت کنه و بگه‌مورینیو از من تعریف کرده:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://telegram.me/persiana_Soccer/25637" target="_blank">📅 23:37 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25636">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b4483a354d.mp4?token=YAZQRGkB1JF_lp_0H8zTtUP4TB4LcLxR7wJWrBo7v9enywvrmkM_olw3tYVzDR4V8cCfowXhGzNVJNgNg6942s6K-pFp47hvfA9KmbJIqnz7iICCSrDoAgOhogxF1_TcokpZqKwHvWEo5lKOzphfxjDXoDdR6WM-SOp6ZrDtLpWa0GcysA0-ytEGj9TUH8y2vdrvQ1t5XI7-2M0OZpy2OZ2s42VGKoMFIaCaVZhSAAkyGBmWEHdb3iSfi9LHP27lvFesRGWW8V7jPZTaT5Ff52f7HT3rFXHSFWc6dpdtYu40DdZCUTz9cn2l0tm3WwNNu6tJ_tocvCDes1X8ada1eg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b4483a354d.mp4?token=YAZQRGkB1JF_lp_0H8zTtUP4TB4LcLxR7wJWrBo7v9enywvrmkM_olw3tYVzDR4V8cCfowXhGzNVJNgNg6942s6K-pFp47hvfA9KmbJIqnz7iICCSrDoAgOhogxF1_TcokpZqKwHvWEo5lKOzphfxjDXoDdR6WM-SOp6ZrDtLpWa0GcysA0-ytEGj9TUH8y2vdrvQ1t5XI7-2M0OZpy2OZ2s42VGKoMFIaCaVZhSAAkyGBmWEHdb3iSfi9LHP27lvFesRGWW8V7jPZTaT5Ff52f7HT3rFXHSFWc6dpdtYu40DdZCUTz9cn2l0tm3WwNNu6tJ_tocvCDes1X8ada1eg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
وسط برنامه زنده شبکه ورزش برق رفت!
رسول مجیدی مجری‌برنامه: بازماانتقادکردیم نذاشتن ای‌بابا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.9K · <a href="https://telegram.me/persiana_Soccer/25636" target="_blank">📅 23:24 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25635">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oBptpEfh46Ic6ZncMBpys2af5e-io0lofpgMqCyICJu6NpJa3xD5kPAXVOlRwz_r8ChcAX7Ca5v82mAG8gsFGtSqHmygaXXy9JDGAuJJQg42pTYlDcYccOrrcEciprnu0sUh7yA9EW9TTofEouySkWCqoxW8897v0g-RQH60gl68wsLOptFUn61yReiJNgbi1vTPMz75AzttRfqqeVz50m_NiaF-RfaLJA3q776gTJd1YEMqaRGJ7jxKJ5TfNZEuOJhNUbU3_mCom-0N9MIt11tqv-L-0fweFh9KDjBskwc_3cWvz5d7AOSRcpJfyscsiUHGD8-w0FUNneo1Te08zQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇫🇷
خوزه فلیکس دیاز: مایکل اولیسه به سران بایرن مونیخ اعلام کرده میخواد بعد از جام جهانی بلافاصله جلسه فوری باهاشون برگزار کنه تا تکلیف نهایی‌اش‌مشخص‌بشه. اولیسه میخواد که در همین تابستون از بایرن جدا شه و راهی رئال مادرید بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.7K · <a href="https://telegram.me/persiana_Soccer/25635" target="_blank">📅 23:12 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25634">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eaDyQfOB81QB-i3zcje95CaNask3ZBXXsa7TcpG8oY5pxAtR6-crpFXPpj_7h8CLbnDO5pNqqjk-QPqNnCRlxL2Blb3T0myeRpDorIOTxlM1jpxBJcC4b31DuZ3L6otvvvOJHLtqwNfue-DJqM3CJ_hg7tQaIg6Pjc-ht157j-VR-uU3qOFamUl5c0S5W2J240Ws8FnAHmkgODDATSuT_cTB1uL0R1jxboMlEz7Hz2CHOW3lMqHcA5fxaS7gxy8sywTYZIMQzt75m4BwA5q-Wetb_ycNO9uM-UBUOlGrXNL_LasVgpPGXprMpbf8kQlbapC-u6JIp_7WZwxyIGaS9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🏆
خبر شوکه‌کننده دنیای فوتبال؛ جیدن آدامز بازیکن ۲۵ ساله تیم‌ملی‌آفریقای‌جنوبی که همین چند هفته پیش در رقابت‌ های جام جهانی ۲۰۲۶ هم به میدان رفت، به علت افسردگی خودکشی کرد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://telegram.me/persiana_Soccer/25634" target="_blank">📅 23:06 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25633">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JQIBUP1Ctg8G0JzGjhksHbUG0gl7TUTrCqsmyv1nX3N1yjbpcZS12rB89B8hYUGWuRd8TZunJFwWCVJdd8yXGu5tiBs-GU3kktxO5LJQi32TXO2V96zybixnxqXeja1A5bFrHusA1gliFwuW9DQmoKZJkWFjeRHdhSxJo9zgo7pI0LGELQYg-9ETgFYpM08jO7SZQfYqwdPUo4GxrudbXgOxTkudsKfdLU5N0tQS6HA-ekcvoHN5bbRQgfEWgYiMqBN9roRZZD4sLhgBqRdl-cO3EzLTnqUWQH-dqoanEV92PXH88VLHEybPgMoOcgASuasVhsqaDFI_20Lsqo-qhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
علی تاجرنیا رئیس هیات مدیره باشگاه استقلال ساعتی قبل بازمصاحبه‌کرد و گفت کار انتقال محمد خلیفه و بهرام گودرزی نهایی شده و باشگاه بزودی پوستر رونمایی از این دو بازیکن رو منتشر میکنه‌
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.6K · <a href="https://telegram.me/persiana_Soccer/25633" target="_blank">📅 22:47 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25632">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vVj0QlHeF7CqQwqpK1P-PfKdeCGsP6FvhkKdA56p9OC5OZ3O6Xs8ImgZ6yohKh71FkcjLZukYAroxRIwImEzbGhAgIIgmxtsXiccwlvlKG0shIHLRo88OMLJV8Ln66y3Sb_9mQ4wGAITiXnjEtcqy4OWSaBqI_8U6RxpBa43-yN3ESM42HFZtJvZMN6KU58fV-H0_oizKXP0pO6QW5gIfPuW8HZhcxd2r-1vwiSWP2K33wk_W3rBId5onx0kOJjdTXnuO7chCsVIqoyDIzkeXlpBdt2ZfecEX8-McTkvgYQsHCKNbjat2_i2uBhH2DYMybJrzk20c9mnDOzuJjDfkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
نادیا خمز دختر خانوم پاکو خمز سرمربی سابق تراکتور هم با پارتنرش ازدواج کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://telegram.me/persiana_Soccer/25632" target="_blank">📅 22:24 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25631">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e4c24c7d9e.mp4?token=ULi3Zv1KXulmwwEbQudXfsLOVbU-EzpTPOf4qtXuGOngjDDKD5lqSvVzJEo13k-KecpYsypr_uu1Y6Vq8dS_N-5-S26TfnPQMN8HCaAScnfnyOvDvGhsPZkpXCYbewlJiC0Kimp0WqbLo2-52k-R1q0nS3XIZoaO7Ds55f82q_DKBzEBlr_ZiRxw7T60rz0Bd1fsWGlXNoRSH36N3ksgPyOleZOX6n83bEhPloWIyusY8gxeWqqJYYMk0rS_uH8TCmj8PbffFpdACGxzGxS4yoeCuUWzVhmPoqAkixCAhPnRztUszGl1rdtMW1OiaitcSNIeSvF23m5XKyFH2Nm-Vg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e4c24c7d9e.mp4?token=ULi3Zv1KXulmwwEbQudXfsLOVbU-EzpTPOf4qtXuGOngjDDKD5lqSvVzJEo13k-KecpYsypr_uu1Y6Vq8dS_N-5-S26TfnPQMN8HCaAScnfnyOvDvGhsPZkpXCYbewlJiC0Kimp0WqbLo2-52k-R1q0nS3XIZoaO7Ds55f82q_DKBzEBlr_ZiRxw7T60rz0Bd1fsWGlXNoRSH36N3ksgPyOleZOX6n83bEhPloWIyusY8gxeWqqJYYMk0rS_uH8TCmj8PbffFpdACGxzGxS4yoeCuUWzVhmPoqAkixCAhPnRztUszGl1rdtMW1OiaitcSNIeSvF23m5XKyFH2Nm-Vg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تیم استون ویلا یوهان مانزامبی پدیده ۲۰ ساله سوییس در جام جهانی رو از نیوکاسل هایجک کرد با پرداخت ۷۰ میلیون یورو. اینجا هم مارتینز ازش میپرسه میای ویلا که میگه آره آره بزودی میام.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.6K · <a href="https://telegram.me/persiana_Soccer/25631" target="_blank">📅 22:12 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25630">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ojQq1zb-9hh1RFukt3V_ib8COC6ed2koGXrQVN_wZ3XiWXG4Oz5rMhfL4d_MdtbKhwvndxjuM_w7cMwjYFvAQtXE53OiJvyUHhAM4UGKxjDPJdV1Fggj72UC_-vdPegV2-IPYdFgUNzmAk6CzOsctCfzrV-7L6AxhCdTEbH3No51buUAbmafrbGkjG2umUtvX5O04Tg9kyeeMJjvqCkGrDA2BRxGSdr3JqItA4Nko8lNGUMU6XzxvhHEM5mXPkQhq3YyvGHjNL3OhRg4eKRKVSEGZt5o5tUWCL8VQRMBlfCxoDlyk7_dUnCdnIQejrGkuM0EGzB4KTVQnXW9KJc2ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
پارتنر جود بلینگهام ستاره انگلیس هستند که قبل از هر بازی حسابی به جود انرژی میده.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://telegram.me/persiana_Soccer/25630" target="_blank">📅 22:12 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25629">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F1ae6Pe-k-RR5hJGYsBf21HhJg3rsshZl_gLvIAPsr1VoyYRsFDouZSuMBzgEwlxkeQLLcx-r8u8D8eqr3f7D9H6pkmniJVWAolIZtrQ043wJ95JR7eAq_reemd9sWnnNlsAml3LhGWhrCeEWPBFtU7Hn1l4MS-lH9JOpfE8Qsafh0tZwZbkvBE5ffJQ8zWu6i3ymHKqltdxAw4OieMn7iVBavwhaD83md_1-kbokXPxmvKi_Oq_4Uu9YuRWVK11X-soMTte2H5ANdyb7VsDu3589YWcHDCPAMEoZamGjjmmVaWI4IdF-QZUS6XlueB93tueSvhqekOgP57eEIw9Tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💰
۵۰۰ دلار جایزه نقدی + ۱ گیگ اینترنت رایگان!
🎁
🇫🇷
فرانسه
🆚
اسپانیا
🇪🇸
🔥
نیمه‌نهایی جام جهانی ۲۰۲۶
فقط کافیه نتیجه بازی رو
قبل از شروع مسابقه
درست پیش‌بینی کنی.
🏆
۵۰۰ دلار بین تمام پیش‌بینی‌های صحیح بصورت FreeBet تقسیم میشه.
🎁
علاوه بر اون، همه برنده‌ها
۱ گیگ اینترنت یک‌ماهه رایگان
دریافت می‌کنن.
⏳
فرصت ثبت پیش‌بینی محدوده؛ بعد از شروع بازی دیگه امکان شرکت وجود نداره.
👇
همین حالا وارد شو:
https://t.me/betegram_bot?start=p7_r4EF37DCE</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://telegram.me/persiana_Soccer/25629" target="_blank">📅 22:12 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25628">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LvboEmy1pEA_wzOuvsM_PasdTWlgmqRZwAA8LHEzkaqCgHQ_2RCLUobJYHr09gYf9YX2qFm3twaUvIbbTsMlGG7rAjbyFglecIMU1mXWJcGfcpxzvt8mEE2dC1kRC9Z5ooUyYkeuvqjcOQbnsdoO-lhXH6-DnJfjPvGLVRZRUxkNYgMrQIdjTyQYfjsmdi5pxJZxom_Fv5vJ3Xt9i5AmFI18dHb0eUoJOioC7OKOgomAUCc0UaWl7sP_OE03cawE-aoxg3Jc4cSZlh8kC4aQc6pR0Ny0inAXo13oMYphcTD01aSUD6_GWrt2jrdrgzmecpSG2WVyO7oBJ_VmZJJWrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
#نقل‌‌انتقالات
؛
کرارنماری‌وینگرسرعتی 19 ساله آکادمی فولاد با عقد قرار دادی به تراکتور پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.9K · <a href="https://telegram.me/persiana_Soccer/25628" target="_blank">📅 22:00 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25627">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H7aVOKXpVfEY4H6xDGvE8MoSibal015qIQ2geIEAQQuEn1gKA64LFt-TZqCwA9ktylNc4Ds9Qo-HQG4z8rjAIo148qO8MfryMr4PexEonwwg2ZCNzRktv5LiXTsLZ4y_3gcJymXmfplpclNitnyKb40ujfHSQ73uor184V3cVzTFoy24XtzqIkDEoVnL1Ws2f8qGUIZkXm27ZulrrvXPr_5vMOZF851BmS2512rn-THrR650yo8ciOzm3WFlQfMDpBeSQEf7Qc2DOdM_xYX4wEJWKwT29J-9gQ9JBD-CWvHOpDTxOMlaA6Wk6lAJHMaSZqTKmrQ0Mwv9scIHU4Ryzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ادعای‌فوری‌نیویورک‌تایمز: ترامپ رسماً به کنگره اطلاع داد که جنگ با ایران از سر گرفته خواهد شد.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 61.9K · <a href="https://telegram.me/persiana_Soccer/25627" target="_blank">📅 21:50 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25626">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sl8GOJcYyxv4puWp2xYQoozj-zE6UrK64N7FK5GrQ1JrZBw0WfdTzO8UckegfZBlQ63QJ4KQ0jVDBYa5YU-AsjMkcN9t3Rh5cDA_zAMfEX9iVHNmREmWysWxUleEOpuLY6ynd9hpek5_Q9ayE3yxk2ySDl7UU19zADlrUZLPBRO7f4vFVJFhR-CRrtRM18YINVOhspezZEdVIeucit016ya_5pdMo_lpuj5pRvGGBAys9UCvq6_6SnWwrIBq6HvKMWVMHZ37MvyPJIX6bj77xyhuJWCV3s7jYlKcEDDS3nhKVLHm5pvR0JRaYQuSUDa3dv9DmkZwTH0smGkuXA_Edw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
برنامه مرحله نیمه‌نهایی جام جهانی 2026
🗓
سه‌شنبه 23 تیرماه
🇫🇷
فرانسه
🆚
اسپانیا
🇪🇸
⏰
ساعت 22:30
🗓
چهارشنبه 24 تیرماه
🏴󠁧󠁢󠁥󠁮󠁧󠁿
انگلیس
🆚
آرژانتین
🇦🇷
⏰
ساعت 22:30
‼️
دیدار رده‌بندی‌ جام جهانی ساعت 30 دقیقه بامداد روز یکشنبه 28 تیرماه و دیدار فینال هم ساعت 22:30 همین روز…</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://telegram.me/persiana_Soccer/25626" target="_blank">📅 21:41 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25624">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dI_4t6a5Lx_lBZ2zdFK3p25rrkYXjuA3MfpqxufbJUEnzUaWKJwmZAtFhhtfqqGTTUevVt_fZ-f47Oq_A_RiL5VKWBRSzjM4iV5py3yUzJalfJoSArNtWenk1FwhdMl_gUHaz6UPWqpPJTaNlpi2-VKKt6DEuHkHsd94497Ojt6ixCKixDg73WJz_yCIzX8M_lipVhhQDK3xpcxuGbCR7OKRB3ZYguow9ju0NDr8vtVUVgL1v8abKy9xF4YOcrRQStE0-ywnGX0hpMSCn1o2eKd2HRK24qnLqGcMq6w-WaAnkhUBJv2assXVeelwVBmYxiaIdDRNeEH9Rn4eJCGzFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ReKx38A3OmGfVOQlEtlEN4mIVGSgWCzgEY6rZGv3d9ap3ofWR_JnYzC9CVkA6m9WNbff37f-hCT8yePivvhwDb6E3ZKabOrergQX0AdVq5icfPbqi7ZwLeFm305qddt2Z3l4lcf3-SVkVKlLgVW7sdLWmC-mFRU5nONExkXzOKZR6dvPiQTmL6mKpjRQeMH7FtIDCY7uYZ_MPtQ7qoXpR4z-mp3VjhHTpNg1oX6e_ni6I35i2dkwELIyLv83w06JubyC70FRdgjoT5y30__iUnVFSUgS_IqJYbwmoqVyafgpEPYyHRHnRD1jDAeOYkGfSX5wwd8ZP03h7mk1mEgKdg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
🎙
نادیا خمز دختر پاکو خمز: من علاقه زیادی به‌فوتبال ندارم اماامروز همراه‌پدرم بازی ایران مقابل مصر رو دیدم.ایرانیاخیلی‌خوب بازی‌کردند اما شانس باآن‌هایارنبود وگرنه میتونستند با اختلاف دو الی سه گل مصر رو شکست بدهند. امیدوارم ایران به مرحله بعدی صعود کنه و…</div>
<div class="tg-footer">👁️ 60.8K · <a href="https://telegram.me/persiana_Soccer/25624" target="_blank">📅 21:32 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25623">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gaZ_EjqDGd0lRrg-cCivya30W3y-CtJpy2z9-od7OYMdKN_w4MMcFMzOGOF3RsG8W3ICz5SLUNHpKw7tZOIwILW_t5uXYd16HTnWjgo3qdNI9mzLNl1hNqK-0YFMdQMx3fu9d8guU1OQRBFxhcPbPuo1fsH5ZPZI80aprhRCYpZTkEC-G8HXtCbHjx7IxK0pHWrDWXuRM-TEu5lUiONiZcGfqsYKCXMpTaTcjh5emggtWnxSSFjZLKHr2_VXT1I1Y31lii-PxMqE2HAvAoVPllrYI4jN-QAsBsgm4ztMo710hdyrzCSSVqoQCL8oziAbEcGYA907_XhbKe7v1M8r3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#تکمیلی #اختصاصی_پرشیانا؛ محمد خلیفه ظرف 48 ساعت‌آینده قرارداد چهار ساله خود را با استقلال‌امضاخواهدکرد. حالا درصورتیکه پنجره باز شود از ابتدای فصل برای آبی ها به میدان خواهد رفت و درصورتیکه پنجره باز نشود قرضی شش ماه درآلومینیوم بازی خواهدکرد. در کل شماره…</div>
<div class="tg-footer">👁️ 66.5K · <a href="https://telegram.me/persiana_Soccer/25623" target="_blank">📅 21:14 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25622">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/au7alZzwf76tn10-bpLfIdKwVDDdS2KvR0QBTGJMPaUM01tImv2gSJzv2wnXhFGFw1-5T2sPfFqni4yHzy0iVeNF0rzZacfKP8at_rjf1-PYE_S__T5N5rwpKi_On0B7zBQYJ3CFpyHTGqnfJ0WRDY8zJB-QElW838K5WSejVJTjvlAe4WAND3ohFddZaqu-KcSVWdZzhqBDTT1p97yTsweKrIJ7xXVpy5FaIHQjlwUnPbZ1gssrAy-vqc0hpioraHveMSwMdsmCTrxm82wIF1ONKlT8I-tQHHZ5Z-V3oPh8O1wYgTBC3oXtKv3RhgiPiFGlO5E_oL0KCB-WJ4G8OA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#اختصاصی_پرشیانا #فوری؛ بعداز منتفی شدن حضورطاهری‌درپرسپولیس؛تارتار سرمربی این باشگاه در پایان تمرین امروز با حدادی تماس گرفته و خواستار جذب رضا غندی پور شده. قراره باشگاه بزودی با ایجنت غندی پور ارتباط برقرار کنه. غندی پور از تراکتور و استقلال نیز آفر رسمی…</div>
<div class="tg-footer">👁️ 70.1K · <a href="https://telegram.me/persiana_Soccer/25622" target="_blank">📅 20:42 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25621">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V_DybvBs-uTVXK0X0AOzq-lmwJpb_1HMVsMRUrA4IUePAXcYvJHYbv9kzAOH2XHiRefyErt9TnOBL1xtAOt2fKAQDl37hc9s42Fpf21aiKAA9uBRHoCObDu7U5tIRMt8OdF15Iv5zah9BCuFr5uBowUXQD9TWVtcmAM4oJKFYl9YefzmJ6LjAjErXAua-l0tmEC5slbh55Fs8W1ibtkLhN3l9MhBDdUJ36DHoQ8ujrt-V-fYetRWs02HgnbpJPRWIEg1Cx9pXOSVkZGDK0WC9iRFywdjc0nW6LdhnlSE4DQDpO7ZLe5mWE_FP-1T3lRBfI7-Y71K37m4EgC1EEcFBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
طبق آخرین اخبار دریافتی رسانه پرشیانا؛ رضا شکاری بعد از دوجلسه تمرین با تیم پرسپولیس در لیست مازاد مهدی تارتار قرار گرفت و به مدیریت باشگاه اعلام کرده قرارداد این بازیکن رو فسخ کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.6K · <a href="https://telegram.me/persiana_Soccer/25621" target="_blank">📅 20:38 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25620">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EKqBCXxIWstegcidDN9YO6Uv_xfOepe-X9brXfk2xSpaTlJZPvkaNa0OJO-YRIGu8obGb32mCD49LcBIbIxBUHMlyJGCY1oeCUPAl289y3wUgsPrjBD2pQg4YsiuWr7jlR4uagItHPHdvn1zeToiF9lYuZ8lQuMA9AqOrhJoldPsCjmdglq4x8UObvpsK1PZREMpwvKfNl0rfOC2GeTMkQ1xTh0S67-3Xm6WKVqENynyzt8vbiHhpOPfCTPIJfrjb2AaHbwmnZfejFiQXMZOlUNv-QxfL7vhQfKgkv5TTDcdAfcaLuBpjYLieLknEDphkFHtnvx3YA0z7I-PSVMP5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
👤
خبرگزاری CBS: علیرضا فغانی داور ایرانی الاصل قضاوت‌فینال‌جام‌جهانی2026 برعهده خواهد داشت. فیفادی بزودی این خبر رو اعلام خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 69K · <a href="https://telegram.me/persiana_Soccer/25620" target="_blank">📅 20:18 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25619">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E8enc-fVIwwIJIF0h466DjurWjxSiH2-K5lMRRQ92lrNXujT5boejsgJmKnQV91z78sTgKtFvczMUvQIJ2dLvsibne8mK8f-h85F3Sc3ueF49ScXYWG8LiTObkF5I-PQ6wBDf-bjAt5zx8wRBCEElJ-fHffGEABXiofDIBKVHuzLYmTV6Linwj0NrCAx9Fi10kRI4dKtgSqMd8pD-R7x-FJz8LpqPWM8zYS75Jkm580MeOSBl4dpC16dmJxjLly8V8n5uiP0XSQbGW2u9LPFyVsBzef_2_NS8WMsDcX90QVUnw0wQLiEQ3B7CFZPfKpz0qh9eTZnpybtyFxCQ7ykUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
باشگاه‌استقلال: باآسانی برای‌تمدید قرار داد او به مدت سه فصل دیگر مذاکرات مثبتی داشتیم و توافقات خوبی بین طرفین شکل گرفت. امروز آسانی برای دیدار با خانواده اش به ترکیه رفت و به محض بازگشت به ایران قرار دادش تمدید خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.8K · <a href="https://telegram.me/persiana_Soccer/25619" target="_blank">📅 20:02 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25617">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KcSBet09iz_zdutFM4-8ZWtQCi6onzpKfoaUJYOsByuZOCfO7i26fb-53aeop0VVu3NlrPLESuj0HoieYmk4OEBY0Y36gagYOnfkzI60QkE1wP0i0E0yo0rxxo3RcZHJWNgM5kfH-OshA5iI-y4yq-tOwmw3OhG0aVYLwVJ94zZO5MHK0oskLTxJYVr-Lcad_vgrVqpXcesPS-m7QQ-pl3m7i3hHx2Mz6D10pL3VC6evGVNdgA8vHon9lYS71U3PGz24wBy1mMw23imGnvfw1UoKhTo_dBnTITsMi6D9cPMijL-R69tOAvJFJ9RsjHPABtvyfH9vZpTeCoOp9FQ49Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#اختصاصی_پرشیانا #فوری؛ باشگاه استقلال به مدیربرنامه های یاسر آسانی اطلاع داده قصد داره که قبل از شروع فصل جدید لیگ قرارداد ستاره 30 ساله آبی‌ها رو تا سال 2030 تمدید کنه.
❌
آسانی آمادگی خود را برای انجام مذاکرات برای تمدید قرارداد بلند مدت خود به ایجنتش…</div>
<div class="tg-footer">👁️ 70.2K · <a href="https://telegram.me/persiana_Soccer/25617" target="_blank">📅 19:39 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25616">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EyYXx9SgQ2B1a7UoRJv2vTqCA6LgKoDKtnt_O5Q4kDHj0bP5HWviT774kIF7Rzxzw16K5b4lVZnEaOnyXJiu9Sb0-_XdvRUwlNnIIIz2gcZIh7QvKB7FbhedOoH3hfe3hnG8WU_cDatqMBGwOg60rzGraHVaTZObUWwwij7mFSlT_-dp5rZQoLBYptevvrxDNy_XiSA59ldsa1ysUzJKredYlt88_xRkUKJSqWAUkIaOSC47GL1rdO1IT87XAsZSpbxmdWU4JG_OQO_FPqo9FV0wKLB4gHatpz8diBZebCn1kD8ws3-ZG08su3D1k8C7TUPNJDPsOFpILSr91Vh7cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#اختصاصی_پرشیانا #فوری؛ بعداز منتفی شدن حضورطاهری‌درپرسپولیس؛تارتار سرمربی این باشگاه در پایان تمرین امروز با حدادی تماس گرفته و خواستار جذب رضا غندی پور شده. قراره باشگاه بزودی با ایجنت غندی پور ارتباط برقرار کنه. غندی پور از تراکتور و استقلال نیز آفر رسمی…</div>
<div class="tg-footer">👁️ 82.6K · <a href="https://telegram.me/persiana_Soccer/25616" target="_blank">📅 19:26 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25615">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BVB5blF7U5cMKinG0rO6uhdDAdxJCEGgY4flVjVzK3x9nK6NxEg7RVCwtSuYwmmyrwm6LqyAsbf9A345a3BEFqVrM2X9lHJ3Jp_JkjqzMN-kLryCsOebo7LzjGC2TpT0Ve-rJDKqeb57EeA--EDiEMJAuSUegLd24zL5zwTuC-c0ATgYhSdoNisZlid7w6D03dUshYmTLIuUE4DvW-w3y3QVeCJAixV2GDYE_sGtBmg8jkDUauDqJ_p-b9nO0YlvhLrFkYPjzDup0kKKZ8n49fyj1zrR2v4fso5yzomK2wxhga6SAKNjV21Rmfs2XpDGZy73nBPmKrgsee8OIgHaJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔵
👤
#تکمیلی #اختصاصی_پرشیانا؛ باشگاه شباب‌الاهلی پاسخ نامه باشگاه استقلال رو در ایمیلی داد: 2 میلیون دلار نقدی پرداخت پرداخت کنید تا ما رضایت نامه رضا غندی پور رو براتون صادر کنیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 83K · <a href="https://telegram.me/persiana_Soccer/25615" target="_blank">📅 19:21 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25614">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d281ac96dd.mp4?token=OZ5k372RExgf9YpYf8LP9qh3Je6xAs3woXFEDJBnL73g_Ysk7JuHwsWcv78aMVFMdalsh0TDGAcEUUQsGNn4vM3I02XWMPuxCIBFBeAuK9QliJQgQEC_5YVfa7G9RMsG97_SGV3qZGkf7qOYXPyMH5Y4sUbqil-FDFwVP70UkL3OfW9Ml9x6Bz8Y6EvFWviUk559nKYDzRowBzyrhvf8w1AzpS1ga8KvAaYXYwmLsc4F1PCKYQWLx84TRg6C_gQ4YLUYSVoPDzXYy-QlKbt1f2XkXamq6keeel-kRuJEOBrV1PptNTWtfnSLtop-9HYbnkAtj-MTJi8KtGWOkB6LKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d281ac96dd.mp4?token=OZ5k372RExgf9YpYf8LP9qh3Je6xAs3woXFEDJBnL73g_Ysk7JuHwsWcv78aMVFMdalsh0TDGAcEUUQsGNn4vM3I02XWMPuxCIBFBeAuK9QliJQgQEC_5YVfa7G9RMsG97_SGV3qZGkf7qOYXPyMH5Y4sUbqil-FDFwVP70UkL3OfW9Ml9x6Bz8Y6EvFWviUk559nKYDzRowBzyrhvf8w1AzpS1ga8KvAaYXYwmLsc4F1PCKYQWLx84TRg6C_gQ4YLUYSVoPDzXYy-QlKbt1f2XkXamq6keeel-kRuJEOBrV1PptNTWtfnSLtop-9HYbnkAtj-MTJi8KtGWOkB6LKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#تقویم
؛ یک سال پیش در چنین روزی؛
تیم چلسی با‌آتش‌‌بازی‌ مقابل‌ شاگردان لوئیز انریکه در تیم پاریسن‌ژرمن قهرمان جام باشگاه‌های جهان شد. دوره بعدی این رقابت‌ها احتمالا در قطر برگزار میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 81.9K · <a href="https://telegram.me/persiana_Soccer/25614" target="_blank">📅 18:46 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25613">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c5adfb3366.mp4?token=eaUMKWh74kjmYKxW_w2-IcsXlPDHAARFWizzp1XRns1DwySwfJKtu8-4qgTJJT2BDRqrMULN6gPSVpQcI3DbwHjyecxsBwZccdweBTcj3Re0QkWrlJLLTVNY_hp-Y4-UPojT9dW6JXUWffd7ba4eoWvDyndbCcYJgIET9P4ghjvtk0ZQ3k6aZPGRVNoKXs8SIe4YH4h8SsFXUEkT-Keh5S3KCPAwSJg0HtJIyADUWzD-RksleN_cgyOUSq7pqKLQ4u48hdDVLRG7j8-rKeu91LiFx3PWR8cKOp0B9fHmWL9kaXcd7RbgBdpi8Yv6nOVtD8p6Ob1QxCOzrTlrmgd0pQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c5adfb3366.mp4?token=eaUMKWh74kjmYKxW_w2-IcsXlPDHAARFWizzp1XRns1DwySwfJKtu8-4qgTJJT2BDRqrMULN6gPSVpQcI3DbwHjyecxsBwZccdweBTcj3Re0QkWrlJLLTVNY_hp-Y4-UPojT9dW6JXUWffd7ba4eoWvDyndbCcYJgIET9P4ghjvtk0ZQ3k6aZPGRVNoKXs8SIe4YH4h8SsFXUEkT-Keh5S3KCPAwSJg0HtJIyADUWzD-RksleN_cgyOUSq7pqKLQ4u48hdDVLRG7j8-rKeu91LiFx3PWR8cKOp0B9fHmWL9kaXcd7RbgBdpi8Yv6nOVtD8p6Ob1QxCOzrTlrmgd0pQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
برنامه مرحله نیمه‌نهایی جام جهانی 2026
🗓
سه‌شنبه 23 تیرماه
🇫🇷
فرانسه
🆚
اسپانیا
🇪🇸
⏰
ساعت 22:30
🗓
چهارشنبه 24 تیرماه
🏴󠁧󠁢󠁥󠁮󠁧󠁿
انگلیس
🆚
آرژانتین
🇦🇷
⏰
ساعت 22:30
‼️
دیدار رده‌بندی‌ جام جهانی ساعت 30 دقیقه بامداد روز یکشنبه 28 تیرماه و دیدار فینال هم ساعت 22:30 همین روز…</div>
<div class="tg-footer">👁️ 65.1K · <a href="https://telegram.me/persiana_Soccer/25613" target="_blank">📅 18:36 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25612">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oSs2ty3zUKKZwoyInQpQ7yzdCQUuelqvX0a69He2vC3TXBKLt-VDyECvzaianhUMbQqmvnM7G_SIQKTwO5buSli6mpbk2itY-T69TkCfb_fo56uzY7W7EPSl8zcdNPi5xa-b2H3j3v7lcYWxhxgzGLIlEKRs_04mZqn-zwEbmLAjqK9HLmRO-Q0WcbNZIxVPi-Pbi04RFHRwKptcIs_IR_kFZdLvuirsWNZ7R1LyhqlsnJOVVyABb3LwrH9LKpbJXTmcEewdGG1ICgXo5WFXWwPFviiq8eNS1zcouvtHLcBdMqGILbgrVvZwfiwnUxHm_BpIPjDL7Qu6B74WLLCqig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق اخبار دریافتی رسانه پرشیانا؛ باشگاه نساجی برای فروش دانیال ایری به باشگاه استقلال دوهفته زمان خواسته تا درصورتیکه پیشنهاد بهتری برای‌فروش این‌ مدافع‌‌جوان‌ملی پوش دریافت نکند این بازیکن با قراردادی چهار ساله آبی‌پوش شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.7K · <a href="https://telegram.me/persiana_Soccer/25612" target="_blank">📅 18:07 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25611">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pXjxxxczPdfKrS0EM4Jw0EAKv0CyVv88rMdWt2xsZh9sufIkmgWaxX6xaqAeiPrmPEsTcOd5sfvOK0zXJykwA0lAKCbKlrI3w4szbTnwzlBVW8YKI4vJfSp_aor_FDdXNDc8SpDQ4Qt3R1Qsd4eWmdVeeJZG13XhJ7fATea1Vy3dV5VFc_AJn45xMn39zlmG1Wl_v6cTLWamuTJ1mNxsxVJIzsSFh4Bp2sYUtBoW81o1XiYR-363otz-fAaXhFHMx-uQQSypUj_wbgGqj0H5aelzgB_Nw4tA4GnRzOuqzN0roYXxPlYyjArYD9dIA01aTWwDiRGXGAteQZpqu7YklQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟠
مهرداد محمدی وینگر سابق استقلال و تراکتور؛ باعقدقراردادی دوساله رسما به تیم فولاد پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://telegram.me/persiana_Soccer/25611" target="_blank">📅 18:00 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25610">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/smUBbs9yM-DMciIv5UbnhpmZzEXEKCgZFAFHjZ6xuaWMmbCipwh8-5Eqs3RD5ikAupDh6NMhQOcm7k8MavKlQiSfp5V27hz1Cq1_c9QyGUk3aDhw9LuniJfjEEtLaGZwxt0LT8Kz3dMNh6vhWcMISzYLI9Ei3IgpatGIGRXJZHYZqe5TGTGpTu5SYvLSiX5QSZ_TpCYjz0K9d5cOmkx4PM8h8Dk2UYKX_ssp_7kgq_0G-P6PWusd4mBJsrgtWwzmePr3IK6tcin1nTQtLJsk8-Oj0K2FEkj8CETvTda0w1MwFbT0lEu_LYZslSP54OvTLpZw9WGTrpSr8dGSlFzSCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
محمد کریمی هافبک طراح سپاهان قرارداد خود را به مدت‌یک‌فصل به ارزش 65 میلیارد تومان باطلایی‌پوشان تمدیدکرد و در این تیم موندنی شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://telegram.me/persiana_Soccer/25610" target="_blank">📅 17:47 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25609">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IM2UdBDEnANKPLQWzefhh_EbEEYkDC2b7Oa2QHQwRGyAK8BH7I3QJMUSv_iqHKqF0CyJm6GxiBGb_g8HzWcvq_b578ge-WWByoTSYTEq6_u1lEAfwHg-yO5OvUBsIDq3bXECzxTmZgMj2LQq6M-kMNQe2WtLeKQBflBb27SxyKpeX6DyXfSJIL7orz8focdYEDiim0uGoUr-LyTKGi55SkcSbRpnuqkY3R0D8hdredi5drg1tej8DUZwrGW1ziV_qQZfS8TVSFaUgmQu2pz3rT7Tt0zsRW84L7ap7MChtz27Hv8oRR9liCcsiNU2M2gQD0Lge4VsDWFISTl8uVleaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
باشگاه پرسپولیس دو هفته پیش با ارسال نامه ای خواستار جذب فرهان جعفری هافبک تهاجمی 20 ساله ملوان‌انزلی‌شد که‌درکانال گفتیم. باشگاه با خودِ جعفری به‌ توافق رسیده و توافق با ملوان باقی مانده که باتوجه به‌فشار بازیکن به باشگاه در روزهای آینده رضایت‌نامه این…</div>
<div class="tg-footer">👁️ 57.7K · <a href="https://telegram.me/persiana_Soccer/25609" target="_blank">📅 17:27 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25608">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X6cHCg4ltmYUHpGMDHPImcgW6JTZ02koYtwLUAyL8YX1R7Q95FxwBZ1PBguUJg698I92F7W_3t6GLmS2gQMR_f2ouYIKsgxx3jEBGot_i05X7W5Gmkkm6cMlP-O_spQITJosWwjk-f4Guv7cYLVWQ1GjbkOM-bZK89J-eNVbLIipDTUcK0r1lVH5ZPsKvizmr4KbLzF0u1K9rl54YF49J1refcwfls5EGxQfTv0BPj3cmLTqvCZa5AjIsX8luJyWfGrRuR0uOdYQu-YccPxf5gfhGN_cOM9zxYHGHm6FGgVu3naYw0g9OqUFtF81givxXnjfHFFN5rxTZ35uepP8BQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
🇫🇷
خریدخوب انریکه‌برای PSG
؛ لوکاس دینیه مدافع‌ چپ آستون‌ویلا با عقد قراردادی رسما به تیم پاری سن ژرمن پیوست. آستون ویلا 10M€ گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://telegram.me/persiana_Soccer/25608" target="_blank">📅 17:13 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25607">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AaueZ6_5bAu1GkM_zHtoD66fZRIXKHQ-RSsBbYTEs6nAWSRiPjakuAnBqeiEHnZG4UD2j5Ob57btXYPKC82ijYY6WXXYNIyks2uVko2UcoqW0MeOshDXEFXOPO2ozp6-7n2IVNnny_z9UBrqo4yNdALaroDakzZ7lPB8QZZAGpo7b8_HuM4In-k9JZfREGJi3179bcUBVFq6qf1ZB8jlcpdp02TYNA3-2SkzC5WbNr03pbail9W5lRG_g5EEn6OzwQROilQdlWniYW_XGPWrq_SENUFMbomUtJzt3zSE0F1KV6Xe-nadOfo7SyCK87GK3f-hOqQZhyF-lnKk1gV3Gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🗓
#تقویم؛ 5 سال پیش در‌چنین‌روزی؛ ایتالیا مدل روبرتو مانچینی دست بکار بزرگی زد و قهرمان یورو شد. آتزوری بعد از مانچینی دیگه روز خوش ندید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://telegram.me/persiana_Soccer/25607" target="_blank">📅 17:07 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25606">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LLu6b98MlVIng2DJiASNDG0reGt8CEZ3O58mc_WAvmhqscWFoPP7ll4pfnMG9k03EYb5dkg4CKFdneGt5BxjD1jm6fq1SP_I3lxQvKv3K2bpYzFVJ5FubG3DeYoCbvG1g5CGJNFcRsIwXZFoIEJwoX646nDwVHTfLS6xvHy3GiAT8NnmKjigHVjQfUBz9sH2kG6GVG6dcGSefU3FP89HQ5RnS6BMcw2Te3yA-X-30zwIk35FPRdfFg1UjPLnFbpIj66MPYCjdVtpejh--K2e7veBpSXHxqcpoles-Vi7dEmhEqRdSlPZT94EGEUn3YF9NItfW6wjRhTgb3KMPerrEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
پارتنر جود بلینگهام ستاره انگلیس هستند که قبل از هر بازی حسابی به جود انرژی میده.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://telegram.me/persiana_Soccer/25606" target="_blank">📅 16:58 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25605">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lJZsC8py1c-ltZ6zDG67cssQBSYlPP4w677ugmZuEK74qb5_VrP8DG5F7mEPXQawksj7CQWHVXmlCsJxMTjd_87-iBQUdEFrxffSjzS3tcHd0tWgrwZDn6sTuRuJtvSJu83Lfq_yL3BeFmSpGtEfMN71wIvsK3dXZ2lysH9_ivKJ03HiNTZHElUu8TiCHo4VJ8Xoh-B_vft2H27Bu-xkNcFeMBIrFy2DsmixGwFlAwdv-A1bGIBIMjdMt86r9XUuA17-A453u1Whxxncj09CJ2zNC99qBnecDIzsFlFFseH6EaDuZ8J3a_64ww0EZuYNrvD9giPRp61AW_IgshHhKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
علاقه‌ویکتوریا همسر دیویدبکام به فوتبال کاملا درتصویرمشخصه‌چقدر زیاده:)از سِر الکس فرگوسن پرسیده‌بودن‌اگه یه اسحله بادوتا تیر داشته باشی به کی شلیک میکنی؟ گفته بود آرسن ونگر و ویکتوریا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://telegram.me/persiana_Soccer/25605" target="_blank">📅 16:40 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25604">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JSKHTPWCkLX0antVrWIAS_pzufLbaqCn5JT_Visn-nOaIkleyoyz0e65WQjGTDPVTy8jdR2RH0SgpsHhppBB65qlN_bbgp6IjZec3m8_4KiD6pBHzIAOhCCc4cgjg02W9kKMfA65wPsRzQApCjw9OciXtQwl0Hv0Dp1mvaQdabCGnzJoPAE3rJZgou__9Kfero0iiJz_2Z9pk5BEPeEaYfvYoVYYWYRvaBXFpvKpzugAMYJFdL2vaQifFU-V-EkfYpEIPqnypFmbjUsjKVRm7xH1wcD1tN00w4Uj1QfzC91vh_BXsMegkIaZroKrpjIZFnuCFzVyM9F4h28qr9caiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇧🇪
خرید خوب‌کریک‌برای‌شیاطین‌سرخ؛ یوری تیلمانس ستاره 29 ساله تیم ملی بلژیک با عقد قرار دادی چهار ساله رسما به منچستریونایتد پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://telegram.me/persiana_Soccer/25604" target="_blank">📅 16:23 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25603">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kHIEeiz0vjFyPnJd4jC1zSSZaDonZit279v3Scv4_3vuUfhHfbdojo8D6CU0VNRw7o8nMnOpsz52rYVFHnjp34rDB3CVXZQY402j7l9Nukm9QmfsVryCjRxT8oJgGRPbEsZQ3a35m-EmJavysVIMI6_9yzIHoT3BXr08NfY8l5iSPcjS1FGlAAJBi4E8nj4XdFITI9YbUl3ULbUhPIh4ouDUWVPy8-wZI_Meg3W40sQneJ7jd_W_-lEIPe23HE_CW7bk3k5BIJddUuTlvUiTYDD1QYRDBuX2nNqzpeJo-R8Bem-Kim3q9PcE9gxOiOzbCyiitth-GkTD3MZEXA6HcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
طبق‌اخباردریافتی‌پرشیانا؛ باشگاه استقلال برای تمدیدقرارداد روزبه‌ چشمی کاپیتان 32 ساله آبی‌ها به مدت دوفصل باایجنت او به توافق کامل رسید و بعد از بازگشت به ایران قراردادش رو تمدید خواهد کرد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.5K · <a href="https://telegram.me/persiana_Soccer/25603" target="_blank">📅 16:17 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25602">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QX1qmIgjMs-TFqkEt0dra_ILGxHl9rb0E7OmJABESfo931Vzt-4HhKyJGztAr7Fn0Sr00cYo542sDl6VEtqw6gDp0A9sspHN6sLlGLEYbLvg5NjXYEXv4keDtjUxLIXs1Jjtnxa5wdcPVDfjMdGbilqTNCTXP1g0u4aMSiGhuwS-jNl0cFpnqwdB9cdOKdNzTPXST1dD76VGHQBzXX9a5IVuQiG1U4VUiEw4JI-zSBa6hWljZfQy3MBvgzBFMd3RbyGIfce7GQ1RmFqMbfcov7lj3YTzkrcKPJPRZ0rVrFV2rcFwtFnAm5QD0V5-aLomHCw5mJLKhh-XYEswtT-vPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همچنین مهرداد محمدی جدا شد.</div>
<div class="tg-footer">👁️ 63.7K · <a href="https://telegram.me/persiana_Soccer/25602" target="_blank">📅 16:17 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25601">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">📱
دیگه وقتشه دانلود از اینستاگرام و یوتیوب رو بسپری به یه ربات خفن!
🤖
👑
هرچی بخوای فقط با ارسال لینک برات آماده‌ست
😎
👇
📥
دانلود پست، ریلز، استوری و ویدیوهای اینستاگرام
🎥
دانلود ویدیوهای یوتیوب با سریع‌ترین حالت ممکن
🚀
بدون دردسر، بدون سایت اضافی، بدون اتلاف وقت
✅
فقط لینک رو بفرست
✅
فایل رو تحویل بگیر
✅
به همین راحتی!
اگه دنبال یه ربات کاربردی و تمیز برای دانلود از اینستا و یوتیوبی، اینو از دست نده
👀
🔥
🤖
لینک ربات:
@instafilerrr_bot
📱</div>
<div class="tg-footer">👁️ 55K · <a href="https://telegram.me/persiana_Soccer/25601" target="_blank">📅 16:17 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25600">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NXUHN9ww6ImPKt-mFHlkM718d6ERBa1baK4Cj5Ob0koCpBXErFQgXrY2tLzy_zRiPNc_91snigsZZVRymRJsEXD3Uv2Qj1Ii6PWTGwfNg2jmbuM9B09Cg8WgtOsMSGVkU9DG6qm0aN9ao5FiADvIMswK8a2dn9Z6ezYKViqCQZXSS6uUvjxd0OVch_vCHN7v0VNxiC_D_TswDa1AvmD61B_zl8b5Xd5XrFklNjkRaTpiWHmPAJXBdrKf2NblHVSH_Cgi-cC3N2GAxxKJtpinRLwL1286PIUi79DuE6r8TqKxDRaiezs4GWIHnHoeiDjB_zHibD497V3nlWTvcaiXig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
طبق اخرین اخبار دریافتی رسانه پرشیانا؛ امیر هوشنگ‌سعادتی‌ایجنت پارسا جعفری دروازه‌بان‌ سابق ذوب‌آهن او روبه‌باشگاه تراکتور پیشنهاد داده و عصر امروز جلسه‌ای بین طرفیت برگزار خواهد شد که به احتمال زیاد به عقد قرارداد منجر خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://telegram.me/persiana_Soccer/25600" target="_blank">📅 16:03 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25599">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a69b3302b.mp4?token=HiaaTAtC6qryHymm_msnETJ9NRvgz1yTowOcr2VlHNhkS87wr9Ql-IekXg8BWl0oBCjyJQ1gEbmYQw2GFb5Rac6zw64aZiluG9eGX2cAhJY0wElx5sMKRECOMPWI8_Maq9C53y1XOJDzPb1ayPbjezrIu8Y56Rnu0JddFeOC2c84ZTzlSxF9NkVBgoTCHk3mUjaydTUv8nIVSWHOwcuK_iP2UfSdmex2n6yd53G5gaqwTCnQNp_55m8SDTzA3l__lUISEwxGLouGuLkEc8cuSF2D6kHfj8qe4zQFqMqevC0x1tLc6HVSaeYd1wZWN8hZuDNGjuhPolxA4C6vr7sZvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a69b3302b.mp4?token=HiaaTAtC6qryHymm_msnETJ9NRvgz1yTowOcr2VlHNhkS87wr9Ql-IekXg8BWl0oBCjyJQ1gEbmYQw2GFb5Rac6zw64aZiluG9eGX2cAhJY0wElx5sMKRECOMPWI8_Maq9C53y1XOJDzPb1ayPbjezrIu8Y56Rnu0JddFeOC2c84ZTzlSxF9NkVBgoTCHk3mUjaydTUv8nIVSWHOwcuK_iP2UfSdmex2n6yd53G5gaqwTCnQNp_55m8SDTzA3l__lUISEwxGLouGuLkEc8cuSF2D6kHfj8qe4zQFqMqevC0x1tLc6HVSaeYd1wZWN8hZuDNGjuhPolxA4C6vr7sZvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
👤
علی رضا بیرانوند: یه‌ روز طاها پسرم گفت بابا دوتا اکرم تو رو دیوانه‌کردند. یکی اکرم عفیف که همیشه بهت‌گل‌میزنه یکیم اکرم خانومت. منم گفتم اکرم خونه خیلی خطرناک تر از کرم قطری هاست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://telegram.me/persiana_Soccer/25599" target="_blank">📅 15:44 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25598">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ecWq23H3vDN6tv5pUh7Fl6gBwnbR_89XHAR33YCsS4mdD5ace8SkSpp_eoCFRmbqU6KzEtLUR4hdxeVasWOGMJwxwr9nAezfv76pS7ED7iQeHMk9cdRIvFT7DEFqVhTfaLBXi9P5LUAi9S-zwKyqQHH_6_xzkP9XbzkZbsXoQcsctFSqwt59ltLbr0KKCi0CXJ4GWnrUORLk1VnS91FvejCaYAQNgyuEbkmTJr6SGAXEhINZPKvk3a2XISAe0QeEKq5LQ5XsJB3831cFsWvkxCuJCWu1EmdWzbxSf3ZVXOn4hcuY_QRYah125XcY1TxqLzQ-UNw9Zr0XE9o0QX70Mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
فدراسیون فوتبال کرواسی رسما جدایی زلاتکو دالیچ از سمت‌سرمربیگری‌این‌تیم رااعلام کرد. دالیچ سال 97 دریکقدمی‌پیوستن به استقلال قرار داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://telegram.me/persiana_Soccer/25598" target="_blank">📅 15:32 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25597">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N81Pkw73AbHnfmjBFnSOJCykOUws-Xebq_b4FBMwVum7_R2Ag7FpKwmI0qnxDxBle_rMsm8XBwrRCx6gndVBNdvhFwpbn8PzYM1_zws49TE7s-j7IpgoP06an_8eJ0SBR2XaeAcEGv5cacCq7Sdp2IIyEOHkyd3lCXtIX3U9oLUu99RTAjL7tkNgiHda76A25q26D6hl9cKzz3y6Wvr3YAsW51YEDOl0-nDhREb2r8te31ffe-8MuiAjBd9HJsUVI_NbYqDKqx9y8oX9fWB071ZIziwrdJpnsAdZUiebYx1d9hwEEcjEuW6kuntJuSuLJT1mSltBZW8DOWI07XsaeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">◽️
👤
محمد جواد آقایی پور 26 ساله که دو فصل پیش سپاهان برای جذبش 100 میلیارد تومان هزینه کرد باعقدقراردادی به نساجی پیوست. آقایی پور در استقلال خوزستان فوق العاده بود اما بعد از پوستن به‌سپاهان با اون رقم فوق العاده سنگین افت کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.5K · <a href="https://telegram.me/persiana_Soccer/25597" target="_blank">📅 15:20 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25596">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZpynCMG5V1MIkGwnm1HtMrcM3Fgw7-aHJZoAfa3pSKqyiJXNDUEGvE6qXL7Vp31JhUjcVuWyE-1gPE8Ke4Zks9NkTDW3Jc3iQfr2MrjKshGNShYmGIKluxMd_kU60dahMK45Hb4ctN_iooOCskPq0kc-sPAp-sZ5gnB0YDU2C16-3crwQOG3gPFpIwOzk3kAuqEBlgqMh1ZrQeWtffD0h_imR1Wzep-4oxcrEPZJmOs3FVHaK1WbMRs_rCR8JwQ_fiObC32LqvyMdcx8mlxwJTvbeQ20YcBtLI6t7KnXH1q5M1Z5fhTJeXQpPSiuYxyOlJtbYBzfQaN0Dviea4AbaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇸🇦
فرانسیسکو ترینکائو مهاجم26 ساله سابق بارسا باعقدقراردادی سه ساله رسما الاهلی پیوست. ارزش این قرارداد سه ساله 45 میلیون یوروعه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://telegram.me/persiana_Soccer/25596" target="_blank">📅 15:11 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25595">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MMtBA9tokcWV-Tm1ENaOHcJwb4XK9phmCVXOyryZ_aJ16NjLpBn6S4x9VTzmFsNsMqBP77qB5ScST-jrsdiR8rg3WOYfYhUDC2JUyTJCVRxeOSCSc3pddQOxZddeCiBDXkQIJqrcDwT-NdjRvp0fgTXZnMrMIwnpirT7OhiXb2ThOPTZno6fXdJmGFiOVvjwnwsvvXtyghByBMtRak9ip6tBIVbEiZ1AJ8h4vTogOBMKCoHrCIM9TfKJFyGYnV0klgaqOHq9k8BUChQ5qASllMoxQFsJNMiLFS2zgN9lD7_tpa9owIyO7jWZsS5SS6hvBIfD3bynaqLUia05nF-Pow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
🇮🇷
بااعلام باشگاه سپاهان؛ سید حسین حسینی دروازه‌بان 33 ساله این تیم قراردادش رو به مدت دو فصل دیگر با طلایی پوشان زاینده رود تمدید کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://telegram.me/persiana_Soccer/25595" target="_blank">📅 15:00 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25594">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q8mKbsuRh4wMliAlu46GRHnfTPJN6DZtHPGGxKIQeYqXsrnlMOdO3Tx4kF9jJtepF-42P54MVPobvyLXLQj3Rs1_UlBNcoc5zTTXCmgdQPteJfqFNgEgrQXt9D-M-j2rqZIJQ8k71QPpFSXlvUKaAqfeMBvYs-NA9Q92z_pVUyC_o2T-FHcXxPridmBY4_Gj-T_m0HfMe6kAQ3C023M_aO_bN53w1NWl08pNwSD8vTYkxzjsWweSUdENuVW7xwT0HmppNFsdm1qfjly57e1GVbi1lJiUI7fvTtnUAeA7_T5PHsXv9uRDrUZ6lDvrOjlz7tDubVE24Fjx7G4XBixuvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
بیژن مرتضوی خواننده‌وآهنگسازایرانی با تصمیم فیفا در بین دو نیمه فینال جام جهانی ۲۰۲۶ به اجرای زنده ۱۱ دقیقه‌ای خواهد پرداخت. عمو بیژن بابت این یازده دقیقه مبلغ ۱۷۰ هزار دلار نقد میگیره از فیفا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://telegram.me/persiana_Soccer/25594" target="_blank">📅 14:40 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25593">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o3z-pU9Q3h_LFKVjPQPBKaPx8AnWHZRawUP2YoR-eh9LZAnfOcMpBUTk9JkjIvV0WVDXgR51ZJNc5zREEKUfpSq9L5OOrhhczP6k1vv4H5hPLKZSJZyGUhepmHWiy_9hXaPZRaJVgCJe5fLx9Juj97vIhdh4Nzr3CXB7-yvx3-u-xZTZJuz852wWztuFCp0u8Edxx9c4EhR8sDMy4m_4TFTPbufDIC0YLUxr9vK-Mi1-nOi1oo6rUF7VPo8d5KXeQH-X8tZrWMTBHt6KHFGhKxWVCiG63s87jxRi75iu3XhATzo_v1_yK0uRs-cU0XnpokNFBWmzB1REmirN5mOE3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ حسین حسینی با تخفیف 10 میلیاردی که‌به‌مدیریت سپاهانی‌ها داد در این تیم ماندنی شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://telegram.me/persiana_Soccer/25593" target="_blank">📅 14:28 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25592">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cYF5mN6DVU_gfF0MoQy2v_LJJvMyiQp_P_heJDn7F_zSSGpwDYIVQgNsy-PfY2Mff15813vWFTnNPv3Qbgi71HOy17j6Oe15pKSdjUxCeMXjVQr1IjswE7E_N7zYEKzEzUomHLAC6PdhdMRyjyc7GAeKxZ-ZeA3oftaEC8huD79-7FP7567wqyKlA7ltZ53jZCZFgamoBU3kdlcCIAJzFqF71iAkOHiccZEI_7IOqkrcvxf8G_YxaaAohEnlGVYq-xyLz9DHX2EsrsnE0vg0iktF94yCZ8eyjze2cT595q-sJEYfvW5j0uYvjg7R0qAChO31ztY_XkDKvxIMWdaRcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_پرشیانا #فوری؛ نماینده علی علیپور امشب با حدادی برای تمدید قرارداد دو ساله این بازیکن ملی پوش به توافقات خوبی رسیده و به احتمال فراوان بعد از بازگشت به ایران با حضور در ساختمان باشگاه قراردادش رو تمدید خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://telegram.me/persiana_Soccer/25592" target="_blank">📅 14:23 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25591">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ujjruUWnbMH7kIU02u2UR9VebWTkOBpKQphQnGN3bkhLvbseR7OLn7A6_Z1zyLDX53RnqAK62vYcMOFKVMYd3yx8VzVBOzhy8z0FF35DAd_gqU83hNhL2sPe0K-uitmIxCDp6kZ60uuwJxOx46qNlW0QOWvxgi2oQxmPQsbDvAyPtNChTXEpbSqloVTwGaVEGhVv_1XNURK0J2txL7_XGDJyu3ReA30wbTgMVpUPrjt1tMg6J5SQeii4bu2kDaD1XygQP5ILBauqVJyN94ML_WR_mFG3c2NmyzoDR87uAGSftOSlLecohe06TdTMktfB6BWy2UCjquj66jhI7l5CWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
خورخه ژسوس سرمربی سابق دوتیم النصر و الهلال با عقد قراردادی تا پایان جام جهانی 2030 بعنوان سرمربی جدید تیم ملی پرتغال انتخاب شد. دستمزد سالانه او 1.8 میلیون یورو خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://telegram.me/persiana_Soccer/25591" target="_blank">📅 14:10 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25590">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bo99Y48w61mArhwQbZAru-Jvn1cLQvoba3BXBfGugwijCMDgBQBFTQdZtL85TjqoWyRRlc-Yw5nYrcDUJ8f6atfvthYKmV9FE4WA1ZlJ0enudKrm-bBi4K5lVfDOAz-IpDWe4qnDPRqbKsSLloLDoOH5yz4iVFC_cebARjD8OQ-5PhFLiZFGpIbb9wdbA2eTdDUeJeKkIgO5Fp5wz4JzlMViVTxq7iHmWgbB1U70Wnf6lr3StiLQJSe1gST2ewJWX0SJMQLWoh6v9GdMZfqYx--fjuJATQUEAsJ6RxBvjpy9vmG9F5qHvrF49nmIH18J9qLouw9jFNL_xwerE0Vt9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
🔴
#اختصاصی_پرشیانا #فوری؛ یکی از بازیکنان فصل قبل پرسپولیس از دست مدیریت این باشگاه بشدت دلخور است و به دوستان نزدیک خود گفته اگر پنجره استقلال باز میبود تا حالا قراردادش رو با آبی‌پوشان امضا کرده بود و یاغی شده بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58K · <a href="https://telegram.me/persiana_Soccer/25590" target="_blank">📅 13:55 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25589">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dWordWeV8Y0ZXuLr3RK_561WEnrtfgljG5KoCax_B-N3Lxrr4CQ-_twRnjGhPUv99uj_7H4gPDsWG1l51zdjDgk0s6LxE-5Qhv6jvnzdQDDApl5roFIkt56Ueao5aphpQYNl_ocNEgElVTRUjX21m-iFlpROjQUc3bKaddoeNyEdw8DOQ6LJi7_8CFIPB4dOzqUP-dHEGAR57W6YINkxu6M4rEASx_H-eXgyzoq4qdxbMFkL7fl9B6MmM1UKwffomDGtlQAxFGC6BdwN7t4GJGeqVB_wyyBApn79FjcxD4u2BO9gVPDO_sVxzcdabLTMlux3aV5DWtsXP7y1xpifMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇧🇪
خرید خوب‌کریک‌برای‌شیاطین‌سرخ؛
یوری تیلمانس ستاره 29 ساله تیم ملی بلژیک با عقد قرار دادی چهار ساله رسما به منچستریونایتد پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://telegram.me/persiana_Soccer/25589" target="_blank">📅 13:40 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25587">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Q1dUAAwNiP7LfGx1yGUyStfIhDOSaNNK37K4dbPpOSNyaSZ7okRtxnNL0DuslZmR3llQb-eA3NlaNPb8DaameCYF6EIwR3b87n_kf-xKxY1c9ltUJQn4LIvn8skUeKThDu9KIuWDgeBL7ttfUXgXmbppuR6_5C5uSWE2CkWzHTmvOZTgtjCCKrUgXjKDgIHwmN_1HhoHjGQazSRxPEeKxq3csKWuk9ReWiTKqgozeIYhcwQ_0gV4YjYMZLVUMKkQW1f_yYzAHN-K8idCgWL-6tbRrypdVw9yY8gI-KuH_zrcNLYsLQj4bEemkfTA5bTFRswQ2krXgzvQBbIYkT8tAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/e7F6mggaWLoN1CCNYpPw1UlFOJ7UyGTyhn1K0bUqapgGB6WQ2gIidDwCkGDFb037wKtOdRZwYlyKtcUcAnacW4P9QEOOpttT9xpbk9XY9tAm2S1P4-7SVQXd7o29yjYAzeHlv9d8PhMEIr2U0mnrNp725MHk96AnwVxH2vSr_BgyieCeG-n1zmx5Qxfq6mic9gVNGMMeesTm0cs_67brA_BFD0eigFRmB-OIKRuuwNOX08s4FaskrMdeE7Cevv7nFCHorvNXSBFw3u_alP0iuT9JHT4dKKuaX9f1somFtj6ShIFg2f2kaPLqpvXX5pqZi4tPZZT3V1AvdTsKzBknUg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">امیر سام دلیری مدافع میانی 23 ساله نساجی روز گذشته ازدواج کرد. جالبه‌بدونید که همسر ایشون مدافع میانی تیم بانوان پرسپولیسه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://telegram.me/persiana_Soccer/25587" target="_blank">📅 13:34 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25586">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qFSoFqu-Ky28bQOEMa8gaHx6d2gkuEcPtt2jt_yqffOx3tR9uVwJJRJCWeHeOJXIZuDCNUH_IuU45YfAi0SZ79QkRMfIodLaX_zobYp6k1Erly1z5FEM0eRv5TCgkDkfwKnbGVIQZjt7Gh9HoBZEN8nszgVxUUnel_DwHRbapGINZFm_Ypqk-68nckA_PJ3lwoaIHBdo98hg2DDf2_7CKW5CoNr8U2GQzVk9byH3wKTWJWeK57J849ItBmsMEctIGZ0EqNGumnZzNDmEMr8AUFua-IbkkblmPIQR7wEkyQAnbJOUEcG9SmiO0N7C_P5pAMqjqqq9o2M9YrP8OLcwvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_پرشیانا #فوری؛ نماینده علی علیپور امشب با حدادی برای تمدید قرارداد دو ساله این بازیکن ملی پوش به توافقات خوبی رسیده و به احتمال فراوان بعد از بازگشت به ایران با حضور در ساختمان باشگاه قراردادش رو تمدید خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://telegram.me/persiana_Soccer/25586" target="_blank">📅 13:22 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25585">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/acb9b44092.mp4?token=dJY3atiG5SExej72Bx-MSbnE31X-14MfF7MqKLI4_1q9aQxCbayTQRPS5oDyZ-2X-82CQzrMeYkrCS3u8ppr4sjYZQTj00L_ybCFFQ4UIrES7Iz21NqC3XgJcBez6OWtgYoyh_7wxnSLa8cjCFMqDLeLD11CQjTyHn9cEud_x-sh8HW3eo72O2kCgeXUb_7ussgko80DXRiuzMzK2rFIva3c5f41rut039g0y99Q-NQnelZFNPjJDTerCVHvdCnIJN9xzEkoR2C9ypcI94QJ0DnAj77zrv2EmEr0ZA-fkyV2MYeNb9OiYGLz_CMU4ET5FMJqxrc3gO82L7lWhVqWbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/acb9b44092.mp4?token=dJY3atiG5SExej72Bx-MSbnE31X-14MfF7MqKLI4_1q9aQxCbayTQRPS5oDyZ-2X-82CQzrMeYkrCS3u8ppr4sjYZQTj00L_ybCFFQ4UIrES7Iz21NqC3XgJcBez6OWtgYoyh_7wxnSLa8cjCFMqDLeLD11CQjTyHn9cEud_x-sh8HW3eo72O2kCgeXUb_7ussgko80DXRiuzMzK2rFIva3c5f41rut039g0y99Q-NQnelZFNPjJDTerCVHvdCnIJN9xzEkoR2C9ypcI94QJ0DnAj77zrv2EmEr0ZA-fkyV2MYeNb9OiYGLz_CMU4ET5FMJqxrc3gO82L7lWhVqWbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
افشاگری دختر علیرضا بیرانوند گلر تیم تراکتور دربرنامه‌امیرحسین‌قیاسی: بابام خودش استقلالیه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://telegram.me/persiana_Soccer/25585" target="_blank">📅 13:12 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25584">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PSKHHbZvAhIW2ppYs9KwwZagYi-LOHDLzv6G9WxQLvTGWLKYXDIimqGa9GHjgpVk5MzEVfSNiQ1NLBrL9HkYPqVOquRtK6_j_1AYSCiCTawm3PmTJfhNbmnY8KhZqJByS2uRJZOU_JqADY8DGOMpIVjJChQZm3gtTOdpa3SFlqwk1h_pZiQsxgP0xDknfsvepxhb-VAp2cjDRF684l9ASNUUaYbfxZpeJ8le-KunT7BBLNzc7D-TCg6Dic2nkQPS_N0Kcb5QTlABRaKEGir_NDytT5ceOzs5Tym3032W9cfrpDeRsOl348zR7e6yidIP_r46lqbxAQZHSSTwsjRcXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بیرانوند: چرابعضی‌رسانه‌هااومدن‌گفتن مصاحبه‌ های مورینیو درباره من فیکه؟ اصلا فیک باشه وقتی می‌بینی همون‌مصاحبه فیک داره به من روحیه میده چرا توهم نمیای همون مصاحبه فیک رو پخش کنی؟
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.6K · <a href="https://telegram.me/persiana_Soccer/25584" target="_blank">📅 12:50 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25583">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Oq5vEXHp1ihGY2d9nzlECIdyxnKD2LnOAqenLIlfGNLUg2KqYy94POQvL9vRMcl6MsaD_rOnq7XvSroFlYCIfvU4v8KHXSE21L3ZEamw7GKH2wHxo1avtT4Eo-hR0savfhWjoAi55yrdUeMtl6y8U8nV-YKMwdFRIyM_q6mtAXfiwBqJdDN97kXy8zmDws6IMcz-6-g9y_XS-rKop4r_4IXJFXVIQe5u_ZifMaDf8kU7cWiw7mm6Py67BsUxijZcXdbg-r3pfNWTm1zNmT6o4nQ7MjNwdK_bq57YBg8NYYC5ikxMT6j2CutUXKRH2m-vfTFnZGpaDGbyTP5CTMm9wA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
خوزه فلیکس دیاز: وینیسیوس جونیور تصمیم نهایی خود را گرفته و اعلام کرده بعد از جام جهانی قراردادش رو تا سال 2030 با رئال تمدید میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://telegram.me/persiana_Soccer/25583" target="_blank">📅 12:40 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25582">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QugvP6TVVVToEVfAuD5egrGe-JqgDouLaz0SVjqGIcKtKK9-DV82XkczU6MaJZSSA_RA6DxR6QzDtdQO5BuNxkL5NtxPHMpmyYqYZyg9fld9k2hC_ChYfgWUYyZ5xIuGTnVMTjN0pSZ4ghi8kAp5vRcZi-OckbG4fSf-vcp5ZZMz0qKMrp-IaRdONY2ZcFk6ukHwxk6NLenXB0f6Inuk2E-s42qEG3UZntXA7KDt1QQe0LVuTrGxUDpVbObZ2_MRQVtsWc04HYNurwlm4vGhO5qjGOTlU54JbdOWHBcYN63l91JOhs14-N72lJwQh0UGj0IqQ3-n-Sqr94nPH6pAbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دوست‌دختر بلینگهام: امیدوارم‌امشب انگلیس با گلزنی جودبلینگهام نروژ روشکست دهد و راهی نیمه نهایی شود. بلینگهام رو بیشتر از خودم دوست دارم. هرزمان رابطه بخواهد با کمال میل همراهی میکنم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.8K · <a href="https://telegram.me/persiana_Soccer/25582" target="_blank">📅 12:27 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25581">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/njsVvb71V5xecCEw3hW2H16G20F0aRROtcJO9PnXw5td2d1S96ldxGDxYA94UCXr52M__ThTWEvT9RId8YYoqioe2LmRAwW9PjFMdm2cR9NMNqhKOpKyRpy6bAYwbKdZC10ZhOMMBSaaQcvY0147npNeKtGY2l5Yvntk4V5rNFDUGk3GmU_vCMCi-ZL9aSBHSSpsypeynXi9HoJbGOLAZVwagEIGVkgBU09C2dGHEhqDABcqVX_X8zRRwVdgFb4wCyQzQXIhWfe804JV0ZDO8LiLW9QWgNILGyZU-kOND3aUuB5bnb1TsQ2cLLhX75imJ4tNBCoj9qeYG8blSKA7vQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری؛ امیررضا رفیعی سنگربان24ساله‌پرسپولیس مذاکرات‌خود را با باشگاه تراکتور آغاز کرده تا درصورت توافق‌نهایی بین طرفین با عقد قراردادی سه ساله راهی این تیم شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.8K · <a href="https://telegram.me/persiana_Soccer/25581" target="_blank">📅 12:17 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25580">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Uts3awtfReOooQgadH_5JVrxtlEa8tCdXfQURRRHV8ptXqfZweDbrFjRQ8afBDHE8gMZe46pQITjSXCGtKP3blmW5JWEfMqm3morl7F9T5w_FxIc4LiyYxDC_LrI9V_q7TFIsdZQ3s9MM1NlWs7OOWL_PEOkJAOtW6aYzcRv9RIcYKpFB5W83rALBzuwChR-f7vkFY-jIJT8Kky26cH-Fx54-GrZAJ2mAXsD8jKp0N3Fl43LPV5Uzey2VRJ52bXNsgfF2_70au8C93AcCf9R91ZdLY2HB69mcN_KL8k0qHXCEfNRrrd1FsQ38HxQhDlv46fkjbcrQX60YsTxMhuyEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
افشاگری‌جالب عادل از مصاحبه های ساختگی از اسطوره‌های‌فوتبال جهان از عملکرد تیم ایران در جام جهانی در رسانه های حکومتی: همش فیک بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://telegram.me/persiana_Soccer/25580" target="_blank">📅 12:10 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25579">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V2gnZqYqnlVlD2OkIgXvy99BF4idYzgQlQ5KAUJda4askbMqpEyRe1COeTyz5ncR-iz4nwILDwUaw9gWfPcPjxxih4FVprNjInat97KrlAhkeDDa9CL3ZuoVeai5x5e9gGXVq8_B-_PVryTnMtkUB0nV55H_CkiGzsmOyuCLBumdoliLP7Rd-ecx-s5t_dfHoEergetaFWhhW9o-crObFXFVEbGnUSJILzXEeVA4jrVbRsdja_6WRiDu4wrNZsCXpGKfJ2I09HLHBda6N-fXbvilRbG4G3_6CkGgQw5ni0aL6COztj6-_6jXUIyme-kY42aBTBoE5joyTP-wDgcDmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
شهاب‌زندی‌‌مدیرعامل‌‌تیم‌نساجی: برای خرید یک بازیکن‌دیگر از روسیه باباشگاهش‌به‌توافق رسیدیم که روی 1.8 میلیون‌دلار این‌بازیکن تهاجمی روبخریم اما خودِ بازیکن حاضر به امضای قرارداد نشد. پدر کسری طاهری به نماینده از خودِ او امضازد و به تیم‌ما اومد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://telegram.me/persiana_Soccer/25579" target="_blank">📅 12:02 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25578">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nzLEcgIJFrV9guyXJ2lDDQ0331Ka5v-zlWJd_hzscoHDjvs-oeydnTwOf0cXnkMz2xGVos9_6S3d1xDt7pegi6AVb8FSsCVeQMddSo3qE2OxbMIgkyoCuYNLZw9CdWsDfe7cWsO_bHI5P-FfGw-i9dSlTSbiZpTqWRAgTs_OI22fVuNRryC-EV5AhaKzIw77vbpg65_MXaSDmvGuz5MURCQTTtwQ2Toelv5n_r3NXT_7_0PyZcMsdnDo8KRN6cYCzOc1xK8Ib6UtPgaHM5wo0ClUICn8Du2zJp7nKw69MsvrCJ6dM4tQ9H03Ym3XjlfHxg34jqRv4TbBJOtR7EG0Uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
#اختصاصی‌پرشیانا #فوری؛ باشگاه استقلال با ارسال نامه‌ ای رسمی به باشگاه ماخاچ قلعه خواستار جذب‌قطعی محمدجواد حسین‌نژاد ستاره22ساله این باشگاه شد. آبی‌ها با خودِ حسین نژاد به توافق کامل رسیده‌اند و تنها رضایت باشگاه روسی باقی مانده.
🔵
باشگاه استقلال به روس‌ها…</div>
<div class="tg-footer">👁️ 58.9K · <a href="https://telegram.me/persiana_Soccer/25578" target="_blank">📅 11:46 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25577">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oho9CVVJc8c-n9omqQNIm6AfDILqf6eef8khMOBAKymgicwVHqMvPUHvSBbMwdKXJrhciclqxWFGK7Vil_HnFSzCbYAUQntP0dgRj0BWngiJBn2_9HJyg2cYbDoWQvgRgI1NDXwruBWqiHlva-d-lBjqVsrP0d2tchywMvmOqmwJR24DDBpQ24Aa9RPxuSkfKcdWPA45wjqUDsvff0w1vD76z2Xp7kwn6YFunECfzoQHYmluW_DKLnOSTxqdd5S1tR_k-1pobi54gzZJ3S94uNmfVLOAZQkrAAKW0hojM5KPVjd9HLE74UK9QR5TKoNzD7HBnQNXfFGChAYwJbkoMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اقدامات لازم برای زمانی که مبلغی را اشتباهی واریز کردید؛
این پست رو سیو کنید و بفرستید برای دوستانتون. ممکنه یه روزی یه جایی بکارشون بیاد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59K · <a href="https://telegram.me/persiana_Soccer/25577" target="_blank">📅 11:16 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25576">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cTj-2UPmZnKtPxt_5puSM-o1tfX5nXVWJF5kW7oOawJjeqeqZjDLjs4CeFkjO5eEbykrcwx8St5flC0W0Rf0X-TOfgJ2a1fqTYASR0HJRxdfcHdxD-rwYyzsG8_j1Nva6PPUccFgrZY_eukNjaJT8ijih7zeBEksnPEe4Y3QCbePN6THMJInIp6UUnN6rz1sWqxZI-X7oZL8DS9HHWdyAStu1pdTva8_Yfwp620_7Md25Hr-THL9eTXNkrprXV8WR6kn3c0t-SnUEKV7t0ZWR3Y6SpRlVd0CKkNl5Uzz2Muwp3NErYhoSE89vkB1LuVrOHt5o87ryM56DZ77kX9WtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
#تکمیلی؛ شوک‌شبانه باشگاه نساجی به باشگاه پرسپولیس؛ طاهری ناگهانی بازیکن نساجی شد.
‼️
درحالی که روز گذشته باشگاه پرسپولیس برای پرداخت رقم‌رضایت‌نامه کسری‌طاهری به ارزش 700 هزار دلار به توافق‌کامل رسیده بود شهاب زندی مدیر عامل جوان‌نساجی امروز صبح به مدیریت…</div>
<div class="tg-footer">👁️ 57.5K · <a href="https://telegram.me/persiana_Soccer/25576" target="_blank">📅 11:15 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25575">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dr_xd2vnz7E7QqsGNCxPxerAS5yRPKSmSqktCubdEoxJfoU3M3g8BhsCjwX8tQ3CPMM2_sI-7BgUVoK4qTWecv9RYsN9MPH32nT21s0PRweTIl9XvPtAgTKG6kGdWENw3GS-hys0wSHkTbKo65_PEb7mzx9j16sZ4DzhmWAyfhxrCgoKlWcNy-GCXXunlTRMZyEUjSWaYqELYU1q0kQ02xKryeXXtFOTq8oQJdxSYrgtX6deRKHyp-0whN3yA_vuLzJdZPeSt-AD4JmZ9Lz_Xca5p_lziKGyvn-NxAHQkA-RBU-3HFsEy1EwfXvYeKyzLRrqLR0vOClFqm7LNLV1gA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اسپید و این بلاگر آمریکاییه که میبینید در مرحله حذفی جام جهانی طرفداری از هر تیمی کردند بلافاصله از جام جهانی حذف شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://telegram.me/persiana_Soccer/25575" target="_blank">📅 11:15 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25573">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c16c61fa5e.mp4?token=Y9yPA_gdILQnLAyacPs-7UpWRErXEayg5AFKoPdZs1T3JB0KpDOUqXQD3rZksxTjYmJEnAnm_OpZQi4RrzQteqmgZbOHSccM4IIn6xzP1svKgix2L5KW1yp3iBYl7ok5Q4h1RSlsZ1uugzrxEXy9Cem7M8iSWhzrs2WFNA1ZPi9IA6Or8G3ITOGJ-XlV03ttSPjmI5g262T2HwyKG3uNyMHqEkLJE5HWcwKfeSC52ijoSN2BC2kLZ-ITLs_FtKLJl2fg299H7nXcImBRsW20BSI9FJUkoKPCUnwopGluQhUJrKL_aMZ5ehwVk3CgDkaSLrrRGz7ymjclLB4SPJYmKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c16c61fa5e.mp4?token=Y9yPA_gdILQnLAyacPs-7UpWRErXEayg5AFKoPdZs1T3JB0KpDOUqXQD3rZksxTjYmJEnAnm_OpZQi4RrzQteqmgZbOHSccM4IIn6xzP1svKgix2L5KW1yp3iBYl7ok5Q4h1RSlsZ1uugzrxEXy9Cem7M8iSWhzrs2WFNA1ZPi9IA6Or8G3ITOGJ-XlV03ttSPjmI5g262T2HwyKG3uNyMHqEkLJE5HWcwKfeSC52ijoSN2BC2kLZ-ITLs_FtKLJl2fg299H7nXcImBRsW20BSI9FJUkoKPCUnwopGluQhUJrKL_aMZ5ehwVk3CgDkaSLrrRGz7ymjclLB4SPJYmKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
خاطره‌جالب‌وباحال فیروز کریمی سرمربی‌سابق دوتیم استقلال و تراکتور درباره یکی از شاگردانش.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.5K · <a href="https://telegram.me/persiana_Soccer/25573" target="_blank">📅 10:55 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25572">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IS2sc7vadJTdu694tL29q-Egkrthw0TxOf04Wt6fMICC3vd29Zr7_pVcRi3xhjxATjJQHz9R7wtlYVej_9NqgDKQUdn2LlP_TLK7nZbL6QjWVP-yGRjK-yKpR2koZBVDj18yZbMn5E52Jr-imTGYPPRoA5CIMhd2L4nC3n8qP50NlBkfhO1OKs7A7FHylpR8-6mQC6EzBNF81fyzHRQUWlZdSd6nqzs5q1r21yu4EqxFUpLlwpF57mpx2XXxAPL80UoaczQt13b2-Actl3GkmKIhFlDOzNbWLMy62WUyaIb-_7tAYky2DFos9LOXprKU4ozbIbyoQQ_K2KRb_td9ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
#تکمیلی؛ شوک‌شبانه باشگاه نساجی به باشگاه پرسپولیس؛ طاهری ناگهانی بازیکن نساجی شد.
‼️
درحالی که روز گذشته باشگاه پرسپولیس برای پرداخت رقم‌رضایت‌نامه کسری‌طاهری به ارزش 700 هزار دلار به توافق‌کامل رسیده بود شهاب زندی مدیر عامل جوان‌نساجی امروز صبح به مدیریت…</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://telegram.me/persiana_Soccer/25572" target="_blank">📅 10:35 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25571">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HTxJYYzBmCpzdp1C1HFoc0Z3evIHNVqcFF6cw4eUHg-4sME7FPNULXp48e2tfd8_xmzm3RQJT0rLPz9qUcYiKtg1LTJ_aV-pjg7ZAWk5veHzzPPREuSMu-12Rd8hXht99mGUCJ3dosAUA1Dwlu2ZOMq8FsPy-A6fdswywh5RS5bQmMTZtH6pnv9-4qxxi3DmSurBX4RqpAUcoDanIwxQq9iEliwUU6jPHEPVCTCx--WA41lft7B3vT5F-Cc7WA6dAx8lJBRdN7AFRO7EVLoMafYg8rTHpJB0rOEawtVjPTzes60w_IhT5AxApLXtlDFQulGYRB60QHUNFRJ-diL9bA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
#تکمیلی؛ شوک‌شبانه باشگاه نساجی به باشگاه پرسپولیس؛ طاهری ناگهانی بازیکن نساجی شد.
‼️
درحالی که روز گذشته باشگاه پرسپولیس برای پرداخت رقم‌رضایت‌نامه کسری‌طاهری به ارزش 700 هزار دلار به توافق‌کامل رسیده بود شهاب زندی مدیر عامل جوان‌نساجی امروز صبح به مدیریت…</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://telegram.me/persiana_Soccer/25571" target="_blank">📅 10:04 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25570">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2501cb2ee1.mp4?token=RE6bgfYHsPaybO__HMu83utB9wuPZX81dGHLzvzgy4nwVQJs6l7WBG6aYkopp2_29qRXp2VQzDTLZgKSFUuoECscdt3ZqzO-tyX627_wYMaUDwjZIWVpU7bziadKUVYJlAKzl6fBQw7IQXAmvz8zewhGiryUJmhq08fzYt2vPkyJsFo9EDoRlVDxyMpJyqCGPfrphIAkq-uoF5LdUCNp725RNinmbXaJC5cOzmx_lxAPtmLm7FY3M_OUsx5TleBl38uUXXtI-F3SRw7CSfZl9CXrjuOfbtjCgwLrIH6GeQ5SIvIPNxSGJGibqW3X1QIOa8M-diWn568reNgF-A1Gqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2501cb2ee1.mp4?token=RE6bgfYHsPaybO__HMu83utB9wuPZX81dGHLzvzgy4nwVQJs6l7WBG6aYkopp2_29qRXp2VQzDTLZgKSFUuoECscdt3ZqzO-tyX627_wYMaUDwjZIWVpU7bziadKUVYJlAKzl6fBQw7IQXAmvz8zewhGiryUJmhq08fzYt2vPkyJsFo9EDoRlVDxyMpJyqCGPfrphIAkq-uoF5LdUCNp725RNinmbXaJC5cOzmx_lxAPtmLm7FY3M_OUsx5TleBl38uUXXtI-F3SRw7CSfZl9CXrjuOfbtjCgwLrIH6GeQ5SIvIPNxSGJGibqW3X1QIOa8M-diWn568reNgF-A1Gqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دعوای شدید و مجدد خیابانی و خداداد عزیزی که مجبور شدن پخش زنده برنامه رو قطع کنند:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://telegram.me/persiana_Soccer/25570" target="_blank">📅 09:46 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25569">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ktUqNSNMiuINEvjOszZ3PtzxZgfU_VuAV-4suWXVnSs2x-dfkJvvPWDA74NSRBF-Kyo7ZIicm-ypVcLKB6yDwA2pZDfkvqXNmprc8xSy6xbyOVVrb0jp1BfaFf_pucW6i4FE_LRAuPc1LeTQL2S6Bz6k_oe3QkCvrcDTLeWfeTRLKwFBZzo7eyvWt1DwloYTZujw2c3Irnn2qVN2ghy_L7XJXSxk8v95wG9LYdrHgdjEkm8gx41YqXNFdONYoRzcPrfJE8B8WEFxntNVb0R45o5iYHlHwzZIbdhQzf3eSPaQOj0xAum8nHmjyzaFZ5KBLXBJr6J3UyAe9BEKUiUZ-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
بعداز پائولو دیبالا؛ دین‌هویسن دفاع رئال مادرید هم درویژه برنامه‌عادل‌فردوسی‌پور حضور پیدا کرد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.4K · <a href="https://telegram.me/persiana_Soccer/25569" target="_blank">📅 09:43 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25567">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GTPmCJgslqD3VONCLFnnaIL1e5VrUTDphgT7czdWL9iI2P239HVR9mfzp8UsN6d51gB6IjThNwOrNLq6Tap7_ObFPNvu1VKjNNhRxIzi2c3sGUEDss37gi0_MsqCZY3wozByFIHyp3FmqO_Z94co4P0xEiHiZVO6esUkinwq6Rpds46o1qUeIIlMZNn6VP54xEp4nLauT_YKi6DjK8Yo-nFALMCeS7D8cDyB_Q94ZJ7FREmNCj9_rYcooOGoDfNbfyNVU4PPLYaWFNXhJ4eP_8dIia50ACiZHq6pmC7PQg63cb2uR918dtXKqjZf0CZxjw57sDFXYXei-F0B-i-7KA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ae3LHq2ejMe_pxmpfi-2igT_-YoCrRa39rYn_V-7klfRv9mVKvdsxf0N4LNFWAZnF6_o2LmFmYTPuGsxTEB7jJO7c_d8vtavX-oTez7-ytB2lw9mrsNyP5nsjNHYvUzVQ3rBoa61_uSWAD7KZ-q1tE9whCfk3HiQh5gmbEU-fT49J1b7EFubt2V0nIEeCBU_XhUGNe21Dg1KpsB8HTp-iUJny2pFNUouY2gSIeCzh-VhN5GTlXVYV42LmpE8JWKGPCO5p1Lt9sfduUVryjWnWgxDWIw1oB1eVQmVslcDvOmO8mhXfD6v5s8kDwZWT8TIdqkgdrPODUuaeY9U4jUf_w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
برنامه مرحله نیمه‌نهایی جام جهانی 2026
🗓
سه‌شنبه 23 تیرماه
🇫🇷
فرانسه
🆚
اسپانیا
🇪🇸
⏰
ساعت 22:30
🗓
چهارشنبه 24 تیرماه
🏴󠁧󠁢󠁥󠁮󠁧󠁿
انگلیس
🆚
آرژانتین
🇦🇷
⏰
ساعت 22:30
‼️
دیدار رده‌بندی‌ جام جهانی ساعت 30 دقیقه بامداد روز یکشنبه 28 تیرماه و دیدار فینال هم ساعت 22:30 همین روز برگزار خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://telegram.me/persiana_Soccer/25567" target="_blank">📅 01:47 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25566">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vqu0toMYubbXklOPHhwp_QEoQ1rGbmMf3FnAJSQVV39MpB9Q10yn9HTjOriQJGztJjbadFNevIFZp7zkVYBg6GahGmAFMZWh3t7yEk0GtaY3mnVFpPNTsuWZMSIfARq-VqUE0omVcMODwOg_voiR69eCfdOMPmcy-wxryP1cqI9nILmllKXdl46oGhjDWcuW82Xb6LgZP230ZtO_dNmlFRzFQAxFmRwfs5LozF5Io-Mjdt-jpvHfptKS7plwHvasDXoMxtXhjx6avfVJkf-bikbBweVncDckSGCNa98qtXhgdrkewrKgH4XXlAthEV_4YAzIeCl-AUGER7XaAYcKlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
افشاگری دختر علیرضا بیرانوند گلر تیم تراکتور دربرنامه‌امیرحسین‌قیاسی: بابام خودش استقلالیه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.9K · <a href="https://telegram.me/persiana_Soccer/25566" target="_blank">📅 01:37 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25565">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f1294ecf8b.mp4?token=m41ZXEcJwiPZK4SKITEdpSgR-rnrUS01cv4cDHyCj-hQpDZi1VD9RpxInLEFDk-G4Ma1PwJxoVQscD5Ri1dPKJ8o4y6ZOi_YR4mw75HCwxlYRE9kh31Od6JRAG8MNh-NlyK_nAw8dBs_X_rtF_g2Lb7bxT8Imoz8gZqw70JdEGjLpCR6kfIYf5_KxXvPXhNd8PJNbsGfaqlCHJAoQxiTv3qU2yLvSpM4ZG5IGixDDh9Kg4yPsLxr7FBW1ZCvOelzEPbY5qDahzJ-NYDaKF_8lvxaHUrTXez9VTCPcY7oWqq19MdflBM4v1KWUcXpFiO8RqGYiTC0p9nT911okopVrw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f1294ecf8b.mp4?token=m41ZXEcJwiPZK4SKITEdpSgR-rnrUS01cv4cDHyCj-hQpDZi1VD9RpxInLEFDk-G4Ma1PwJxoVQscD5Ri1dPKJ8o4y6ZOi_YR4mw75HCwxlYRE9kh31Od6JRAG8MNh-NlyK_nAw8dBs_X_rtF_g2Lb7bxT8Imoz8gZqw70JdEGjLpCR6kfIYf5_KxXvPXhNd8PJNbsGfaqlCHJAoQxiTv3qU2yLvSpM4ZG5IGixDDh9Kg4yPsLxr7FBW1ZCvOelzEPbY5qDahzJ-NYDaKF_8lvxaHUrTXez9VTCPcY7oWqq19MdflBM4v1KWUcXpFiO8RqGYiTC0p9nT911okopVrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
افشاگری دختر علیرضا بیرانوند گلر تیم تراکتور دربرنامه‌امیرحسین‌قیاسی: بابام خودش استقلالیه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.7K · <a href="https://telegram.me/persiana_Soccer/25565" target="_blank">📅 01:21 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25564">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd764fc92f.mp4?token=jdjIJflrEXLozmxDih7rjsKoBwSy7Z-oo9JaPBDghujLXQWb_qoZvPAEG9f3NCl7sQMZnG92VMyZJYkzTEdcgXX01A6hPs4TSH0S7vo9BJLfm0DF0WKK0RqhKPrFAgw48Ola195EAXeeRV0fpDTaFz0xMiJXXLBjB1KwaN0dj1A5o0pX-8mC82Pryc-kk1yXK9EMW1c2JRbKM-tQZ5la1zI9INnnNpX7UXkYTT9beQKGVFzwj-4hfSZyTyFzJodrsU9Hj9Qrh8XaSkJ2230icRER5yKrn8DncSNU-qpeSOu_VrN6edbdXF_cyjPSAR3TQ8qj97ShA19MMbsHICxh6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd764fc92f.mp4?token=jdjIJflrEXLozmxDih7rjsKoBwSy7Z-oo9JaPBDghujLXQWb_qoZvPAEG9f3NCl7sQMZnG92VMyZJYkzTEdcgXX01A6hPs4TSH0S7vo9BJLfm0DF0WKK0RqhKPrFAgw48Ola195EAXeeRV0fpDTaFz0xMiJXXLBjB1KwaN0dj1A5o0pX-8mC82Pryc-kk1yXK9EMW1c2JRbKM-tQZ5la1zI9INnnNpX7UXkYTT9beQKGVFzwj-4hfSZyTyFzJodrsU9Hj9Qrh8XaSkJ2230icRER5yKrn8DncSNU-qpeSOu_VrN6edbdXF_cyjPSAR3TQ8qj97ShA19MMbsHICxh6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#تکمیلی؛ علیرضامنصوریان سرمربی‌سابق‌نفت تهران از بیرانوند خواسته‌قبل‌از پیوستن به‌تیم استقلال این پستش‌رو از حالت‌ارشیو برداره و تو پیجش پین کنه!  علیرضا بیرانوند از چندپیشکسوت‌استقلال خواسته حمایتش کنند. منتظر استوری‌های حمایتی هاشمی نسب، منصوریان و مهدی…</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://telegram.me/persiana_Soccer/25564" target="_blank">📅 01:13 · 22 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
