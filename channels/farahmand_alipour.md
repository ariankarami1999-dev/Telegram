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
<img src="https://cdn4.telesco.pe/file/L6eANzg5E2ope30iE-H-ULCvd7G7wVWIzTloBYNqXcmq7zn-BobyVwCd0ZwAclmZtL_4gOq305cOK_MNfXllWc9Ghw-N5A-7QcSViJlWV32TqHyeaEgq8bzSO_VEmRmyYqaAbOdW_vCzZ-JcIb07rKRQLOFSjUuM5iS6zvwXmoMvJua5fn0wrpvSzoQ9IMvMi_pwZhmhqxKiIlhITFeABtp7aJT7qOuu73bYRJCtsrv958Q73_FuX_29Ohm1VrCwbsH7Y0Y0jWezT3ftlakOfIwZMVPTN-iDEDm_jFnCuG7Yl3sQV64eReV09A-6N68B1MZWsFNVBiZk5FFidrM78g.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 62.5K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-10 20:12:33</div>
<hr>

<div class="tg-post" id="msg-5819">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ed6be978db.mp4?token=Mq-bcTPjzoOviHrwKgqre8iZP98zVqAL62SUwcn-4ZgIjvIvNF_AqmNTnuGoWVoSBhzjB3ulInQekp4DaJ7hExKFGXCIie35TO9LNsm638VY1QKI8y0f88JnHCUoju-gegeoo6UYwd_BcW95gXmxFRwAwtpBTzTZEKlfMBSBipjBNMaOysJ5jGQnV7TbtnHNaJ_Y8wy0uQTK6RNKzruuyLI28bDqjMBr8mCHFVjBaWcdQMxnlJjXRxKhDyfCWd125FU19T32etbiKAldPXKFiY10OXNmAAMw9DYTHcBQMSrTF-l0V4rbsVw_yZeWGNCaJxX5OnVkZJzyRn6PgSJEWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ed6be978db.mp4?token=Mq-bcTPjzoOviHrwKgqre8iZP98zVqAL62SUwcn-4ZgIjvIvNF_AqmNTnuGoWVoSBhzjB3ulInQekp4DaJ7hExKFGXCIie35TO9LNsm638VY1QKI8y0f88JnHCUoju-gegeoo6UYwd_BcW95gXmxFRwAwtpBTzTZEKlfMBSBipjBNMaOysJ5jGQnV7TbtnHNaJ_Y8wy0uQTK6RNKzruuyLI28bDqjMBr8mCHFVjBaWcdQMxnlJjXRxKhDyfCWd125FU19T32etbiKAldPXKFiY10OXNmAAMw9DYTHcBQMSrTF-l0V4rbsVw_yZeWGNCaJxX5OnVkZJzyRn6PgSJEWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به امید شکست و تحقیر یک به یکتون!</div>
<div class="tg-footer">👁️ 1.89K · <a href="https://t.me/farahmand_alipour/5819" target="_blank">📅 20:05 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5818">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pialK1hk9HI2hstF9Bak8n6E24Whj9d9TY9oqsM3ZlOChJO8T5JClSiGEx8sM0ZbkgaSwZBljwne77_rkVaL6PG5maf9dsvVkCtEQFGzZxJRNExnNymIeaWCEGUxXjWjilHElaLgnKLYUeomOau7iUIkkYQG33exnYnW1j8rs0ps684fIcLFqje48DeOMgmFnN6HJtS-wXS2EjFto_rl5NEyOypP3nuWUE7GT9p_onMyz6SklOvuaBO1zmnlFqM6GJB5147mvItjtD2nJ367wB3yXDM9JirmJ-Zxo5B_IULXWHik0eA545yCEjx9aX-O4MD9uTuJBqDbjdBNzZVm3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farahmand_alipour/5818" target="_blank">📅 17:21 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5817">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7862dff401.mp4?token=uM5ZU1dLXBaDc7vcDrW2e_wuanDsWlVoKBe4NahKBWDAejduDkwsTsIqihRAGfhp7WaFYEqiMkvP04ju6XneDjGPpNzcz_fI5rD9lCubl9d2Jdac-9JMH9-614SJM04aZVq2wXfbrj_zjddo9QUPV8HrkY4wOWyvUn73RDxumOtT_yXskLT71jPXx81Rey9KHAjYs8GVKmZ8nYp_AKYfrrSy7AN-MwrxWp7uskm_Gxot5nYh6upzSI95ymwGuFCi91ht0SHFRmX_6pX71qhV6mcC21iLGdV_hqnZ8QutXMESneokbpnsDAsxj4088tQkSNbeykR-rtn4Fhy-DSY0rA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7862dff401.mp4?token=uM5ZU1dLXBaDc7vcDrW2e_wuanDsWlVoKBe4NahKBWDAejduDkwsTsIqihRAGfhp7WaFYEqiMkvP04ju6XneDjGPpNzcz_fI5rD9lCubl9d2Jdac-9JMH9-614SJM04aZVq2wXfbrj_zjddo9QUPV8HrkY4wOWyvUn73RDxumOtT_yXskLT71jPXx81Rey9KHAjYs8GVKmZ8nYp_AKYfrrSy7AN-MwrxWp7uskm_Gxot5nYh6upzSI95ymwGuFCi91ht0SHFRmX_6pX71qhV6mcC21iLGdV_hqnZ8QutXMESneokbpnsDAsxj4088tQkSNbeykR-rtn4Fhy-DSY0rA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جی‌دی‌ونس میگه ترامپ میخواد با این تفاهم‌نامه با جمهوری اسلامی،  بازارها و مخازن رو از نفت پر کنه،  و بازار سهام و اقتصاد رو درست کنه بعد تصمیم بگیره با ج‌ا چه کنه.</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farahmand_alipour/5817" target="_blank">📅 16:36 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5816">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f9a10fc62.mp4?token=RUYbYCMtpUa38zQUnGs3Q7WxPe3AMuajBMmf4oWPMuWqD2TIH2jHX2oQguCExT3zcZbwLOEuJ_E_EUT3xV_dZBbhOSe9gBh7haS2C7heEJd11x3aJ3yVvxnLy64WKf-_oNgn-IoE2C3-Ka-ryvK7M_kPD5rQ2vc5AQhUoIOXFbDlhZy5CSzxXT9YHn5EKvqHdDckfmWo0FRV0PqpoBDtU70n6n03Frf7B9mZtszDiIMR8Zamsv4gT4DRrrzptfCazXiqncNjxK5PNTTn8ne3P0M-2oO9AgEvaPAJDrutbrNwbzCyG36ZDUixGu5FmidJBQxYAzxAs1KQuhI0oG1Xow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f9a10fc62.mp4?token=RUYbYCMtpUa38zQUnGs3Q7WxPe3AMuajBMmf4oWPMuWqD2TIH2jHX2oQguCExT3zcZbwLOEuJ_E_EUT3xV_dZBbhOSe9gBh7haS2C7heEJd11x3aJ3yVvxnLy64WKf-_oNgn-IoE2C3-Ka-ryvK7M_kPD5rQ2vc5AQhUoIOXFbDlhZy5CSzxXT9YHn5EKvqHdDckfmWo0FRV0PqpoBDtU70n6n03Frf7B9mZtszDiIMR8Zamsv4gT4DRrrzptfCazXiqncNjxK5PNTTn8ne3P0M-2oO9AgEvaPAJDrutbrNwbzCyG36ZDUixGu5FmidJBQxYAzxAs1KQuhI0oG1Xow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جی‌دی‌ونس میگه ترامپ میخواد با این تفاهم‌نامه با جمهوری اسلامی،
بازارها و مخازن رو از نفت پر کنه،
و بازار سهام و اقتصاد رو درست کنه
بعد تصمیم بگیره با ج‌ا چه کنه.</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farahmand_alipour/5816" target="_blank">📅 16:31 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5815">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🚨
نتانیاهو : اگه نیاز باشه به تنهایی و برای سومین بار به جمهوری اسلامی حمله خواهیم کرد.</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/farahmand_alipour/5815" target="_blank">📅 00:04 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5814">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/60c1fdbeee.mp4?token=lwZdIZBcH58DkCMaATQw31Fv7hm2Y1uQBSkZNMu6b8U1l5_JTPdybrEepT8QJKal8owTD7Ka9aqqymBXxOFI1lyde07IwmtV1RhjNSCO09UyDx5prSaWM_lTL7OrBoSYvHCmTVV7jJSZysarJMkm7ZVI7-jPKRn7-kN0-lKZeszUcZF1xv2theYxUZSWyep_MFEoRE28S9At6e3iZywyMcIMlScJIOJ0BOAEPnq5y8f-EBB783puu1mjLNx50x-DwWTSKQdDLWSg7Z4JGMc3wzD0k97t7BvP0OQ4p67-dhpYv0WuUF10eGJGGrPEepoqMy9FNGry1hMaeEWZ8tU-5ERJrxOULTFtPP-_LkocEemiBdGDhwXglpGloFsyV644F_PRzIOmcDAnSdBU9FVQxHsOUvF9p51eoEPJVDGWM6ZYmLku4IgrzdpvBNRL_D9EByaTnwSROzqQTAAs7W9f-uoqxRUebrLkIkY6ZhG9NvduNExBwaorUhnCwyKCFFpCqq2N1YqQQgvyoRlShaHnvBb3XRDKW_GEHM69L-oF0OdtXAqYCcFW3vZSdVRHZP_lEOhvSYxLR1ezTBO8pbDWW3VxaotTsfCS06kmq1Tx5LbdfCWffDlmHUnBGXVeIpz1H5PGewDEQm95uCcbSKAJEK61sbmEKqLwqBlV3FonMcc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/60c1fdbeee.mp4?token=lwZdIZBcH58DkCMaATQw31Fv7hm2Y1uQBSkZNMu6b8U1l5_JTPdybrEepT8QJKal8owTD7Ka9aqqymBXxOFI1lyde07IwmtV1RhjNSCO09UyDx5prSaWM_lTL7OrBoSYvHCmTVV7jJSZysarJMkm7ZVI7-jPKRn7-kN0-lKZeszUcZF1xv2theYxUZSWyep_MFEoRE28S9At6e3iZywyMcIMlScJIOJ0BOAEPnq5y8f-EBB783puu1mjLNx50x-DwWTSKQdDLWSg7Z4JGMc3wzD0k97t7BvP0OQ4p67-dhpYv0WuUF10eGJGGrPEepoqMy9FNGry1hMaeEWZ8tU-5ERJrxOULTFtPP-_LkocEemiBdGDhwXglpGloFsyV644F_PRzIOmcDAnSdBU9FVQxHsOUvF9p51eoEPJVDGWM6ZYmLku4IgrzdpvBNRL_D9EByaTnwSROzqQTAAs7W9f-uoqxRUebrLkIkY6ZhG9NvduNExBwaorUhnCwyKCFFpCqq2N1YqQQgvyoRlShaHnvBb3XRDKW_GEHM69L-oF0OdtXAqYCcFW3vZSdVRHZP_lEOhvSYxLR1ezTBO8pbDWW3VxaotTsfCS06kmq1Tx5LbdfCWffDlmHUnBGXVeIpz1H5PGewDEQm95uCcbSKAJEK61sbmEKqLwqBlV3FonMcc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چرا جنوب لبنان سقوط کرده؟
چرا ۱۱ هزار ساختمان صاف شده؟
چون رفتن دنبال «خونخواهی خامنه‌ای»!
به قول خودتون چون «پای نظام» شما ایستادند! به خاطر افکار شما!
خواستید جنگ راه نندازید!
یک میلیون شیعه ۴ ماهه آواره شدن!
شکست‌هاتون بیشتر و سنگین‌تر!</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/5814" target="_blank">📅 17:59 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5813">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6a28a5f6ff.mp4?token=oE9Gz8HfKiK1GNeA4IQkn6E-S-GkCIKRQaXQSNUhy2rmw-Eec-glvVS1jAtMdwkAQ1QZG82-sjOLVZmdBCm9r7kDpTJ3plE1UfEq_SZTiEmZjJyvosEjY_xOtluTid3i6aupSLb2Oz3MunembQcOH2eMfoMev-Q1noTCXPob2oVfOFy_QoN4bD4OazGPlTmTEVTYYoYpiiema1zKd89n3OqUeTbQqBn_Ql8Bx4Ge7r5gZDZTI44D52b16Mg7wXUPaeIGNpya97hdhMKUDXHrYi6-ps3Mrd0uGaeWUBik6CcVuu5Ek1lk0X1bH-R-9xxTuoHtHBqV3i0UbrkgIQkwhg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a28a5f6ff.mp4?token=oE9Gz8HfKiK1GNeA4IQkn6E-S-GkCIKRQaXQSNUhy2rmw-Eec-glvVS1jAtMdwkAQ1QZG82-sjOLVZmdBCm9r7kDpTJ3plE1UfEq_SZTiEmZjJyvosEjY_xOtluTid3i6aupSLb2Oz3MunembQcOH2eMfoMev-Q1noTCXPob2oVfOFy_QoN4bD4OazGPlTmTEVTYYoYpiiema1zKd89n3OqUeTbQqBn_Ql8Bx4Ge7r5gZDZTI44D52b16Mg7wXUPaeIGNpya97hdhMKUDXHrYi6-ps3Mrd0uGaeWUBik6CcVuu5Ek1lk0X1bH-R-9xxTuoHtHBqV3i0UbrkgIQkwhg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گروه تروریستی حماس
در شهر رفح در نوار غزه یک تونل ساخته به طول ۱۶ کیلومتر!
تقریبا به طول خط دو متروی تهران!
که این تونل از طریق خونه‌ها و مدارس
به سطح زمین ارتباط دارند.
این یکی از تونل‌هاست!
خود گروه تروریستی حماس سال ۲۰۲۱ ادعا کرده بود که ۳۶۰ کیلومتر تونل ساخته!
این همه پول رو صرف ساخت تونل و موشک و
اسلحه و….. کردن که مثلا مبارزه کنن!
میارزه هم کردن و نابود شدن و ۷۰٪ خاکشون رو هم‌از دست دادن! می‌تونست صرف مدرسه و دانشگاه و بیمارستان و غذا بشه!</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/5813" target="_blank">📅 17:53 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5812">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/085c31b1b8.mp4?token=K_hVU1REAgYCzV5qh5_zXIlC_NX8aVqpvDyJtRZUoF-DKmUheuQsj-nxqd5RD8PLyvv4LAXuy_THpOOWCegaaMRGu3IX3-TRd63UfRzFJsjb9GE3-MwMOLnfBtBLSHCdc637qkbGct8PdiQIj9BdfFqM1MXTQ3tkCUQgYLeynQF4g5KtZ5Dd1LzsKFUsRd7EGaKkhbEExvjNAzvz9NHdwiYA9z1YQVWVqnC3cba2zzHNFY-W6WqU1sYfra6_2i2jGjU4vB0VI0zAxOGIQ05QX0K7DzNSrnIRVysjM_DnzVAfR0JTWb9czCH26dxS8UdDpEMN_Psst_UmvG46SJBsCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/085c31b1b8.mp4?token=K_hVU1REAgYCzV5qh5_zXIlC_NX8aVqpvDyJtRZUoF-DKmUheuQsj-nxqd5RD8PLyvv4LAXuy_THpOOWCegaaMRGu3IX3-TRd63UfRzFJsjb9GE3-MwMOLnfBtBLSHCdc637qkbGct8PdiQIj9BdfFqM1MXTQ3tkCUQgYLeynQF4g5KtZ5Dd1LzsKFUsRd7EGaKkhbEExvjNAzvz9NHdwiYA9z1YQVWVqnC3cba2zzHNFY-W6WqU1sYfra6_2i2jGjU4vB0VI0zAxOGIQ05QX0K7DzNSrnIRVysjM_DnzVAfR0JTWb9czCH26dxS8UdDpEMN_Psst_UmvG46SJBsCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محمد اکبرزاده،
‏ معاون سیاسی نیروی دریایی سپاه،
‏شب گذشته در یک سانحه رانندگی ساعاتی پیش کشته شد.
او در یکی از اجتماعات حکومتی به صراحت گفته بود حملات آمریکا «واکنش» بودند! یعنی ما حمله کردیم و آمریکا پاسخ داده.
جنگ‌هاشون در لبنان و فلسطین هم همینه! حمله می‌کنن، وقتی جوابشون رو میدن میگن ما در حال دفاع هستیم!
۴۷ سال گنده گویی کردند و سرمایه گذاری روی تروریست‌ها و وعده جنگ و… تا بهشون حمله کردن، گفتن ما مظلومینم و داشتیم ماست‌مون رو می‌خوردیم که مورد حمله قرار گرفتیم!</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/5812" target="_blank">📅 14:57 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5810">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ePD7R4akJNHgtADoLLrEGmggcBlHSCWonPMhTvzps1rXUU5QHyOhW7AEJU-wsoCKCUkneA0rIVGxQdV09hWNvoY_TGlJ5JscAuvtZwx_FjQPBCNolGMx4uy_2miPHn3C0he8F-Gdy5AhkwXxOAByaQgsQ6GpjfFXJ4p_LDkiDMTeeIU7FewLD761zzIK_nzdyGFUILhJoniqmXXl9-JDzIa8tRb9z7d-WDIwbk4RDxJ302fMiZ5dqD3kwvZ6QpD9-bgN2Xcb8y5ApKiAcjQ1GStsDV-1ajjMCVLCx40W1Q92zkQk43Tf-lPU9Wl2idMzPSEFegspk8Z5VfDYGxnJqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fahTgi4jsNM3S9IweY50s1VBGNfoHpiiZlJ1GG4UftA0KGr1gEJy8J-zr4MhwZ-xKyLYgzPjYRgkxJgtuXDJCLQYxnqjIsn6yowDqYlu7yIpsWs93Z5j-MppWVYNi8GMJOdoZUwlM-cSJHRx2JWfmljPzCP6Y7_8Mxf-yGHtVHEZWj0zfPgXUZc4Oe8QlqmovLr-ViaaCaqSe-U0ZoO4S2VTwtWyVXVxBnz3hdD7_r28_ydLtBIATwbt6qFTAlD_8jyV19w0aJzIN4o8ep0ZMIaiwXTfojX8gmDD66CPQP_35DRgUUfe0oDfTavWdnVLieTvkCe8yQYqlN3ctkyt4w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ده‌ها تن‌ از‌ سران و مقامات عراقی بازداشت شدند. از خونه‌هاشون میلیاردها دلار پول نفت و طلا  پیدا شده!
خیلی هاشون از نزدیکان جمهوری اسلامی هستن.
با تصویر خامنه‌ای و سلیمانی و سیستانی در خونه‌هاشون و سوتین و شرت طلا!</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/farahmand_alipour/5810" target="_blank">📅 13:32 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5809">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee0be552a1.mp4?token=J12XfAPqKXlUM3VTbQnv_Pigmgu0Cht8-m5YH83LY3s7Dv7YY_aD2lus0Wy6Ab2TbczCRabL6jz24YD9rqjl_ePmHkEUvz_kdPSGudU_kFGOfEiO_86R3Q4_s9gHig_ycWkjn7Oe1ko-2U3ce5CN4PXQg1c2Hag2tprbmiuVlFaORd1pZ794YtLxwsvw_kjqrxl4BaUC0Axo1_sAbFdDv5qFt-UHD2F3-4mFJknlAap30fdecSK0U5-AP2bmgxPwKJ0IP1U60HTqjEdfFtuAfmYg0cZLgogazA136V_E4HalsR5GnraXRxJAzS7BOZGbHdIz0YlRWfMDLK1pn2Bl2IWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee0be552a1.mp4?token=J12XfAPqKXlUM3VTbQnv_Pigmgu0Cht8-m5YH83LY3s7Dv7YY_aD2lus0Wy6Ab2TbczCRabL6jz24YD9rqjl_ePmHkEUvz_kdPSGudU_kFGOfEiO_86R3Q4_s9gHig_ycWkjn7Oe1ko-2U3ce5CN4PXQg1c2Hag2tprbmiuVlFaORd1pZ794YtLxwsvw_kjqrxl4BaUC0Axo1_sAbFdDv5qFt-UHD2F3-4mFJknlAap30fdecSK0U5-AP2bmgxPwKJ0IP1U60HTqjEdfFtuAfmYg0cZLgogazA136V_E4HalsR5GnraXRxJAzS7BOZGbHdIz0YlRWfMDLK1pn2Bl2IWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بیش از این‌ها تحقیر بشید !
چه در ایران، چه  در لبنان، چه در فلسطین،
چه  در دریا ، چه  در آسمون!
در ضمن بهتون دینار و درهم نمیدن!
قراره یونجه بهتون بدن و پولش رو هم بگیرن!</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/farahmand_alipour/5809" target="_blank">📅 12:55 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5808">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t4fKtz9aVfS6J92jL69gAiGDLK-hG0_m_Du9Y2aq_OjI1YQUEsBqRGdm1rNOwFBZFWpQY1Qyvm18NDHceTCKgn5vRB_LWiExThmh8TkQ6f7cGwXIc-aV7YhrQUYgHJT6rRXHehEP-aosnmcK9z2Bvv71pt_Xo4wx00bpAcrgZJtPo7wcpRaT8tHOmL_hxZpB0EDZQiw6kS8u-hyX6BX-wc7CEDlEXqBbjNbOh0PP3ONGn0L_dX2hQCxkjgB4lBpL_qw7WhyPdfJ4-hxX9AGeowUnGHk2_5FwgXo1P50MSQ-8AyaqOF8R8aKCDxqcaNOzABPwBgoofO7RS3isGG6oVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقبره رهبر مستضعفین! که در زمان حکومت خامنه‌ایِ ساده زیست! ساخته شد،  با مقبره فرعون‌های ظالم!  که به قیمت و نرخ امروزه، مقبره خمینی ۲ برابر مقبره‌های فرعون هزینه برده!  ولی عرزشی که نمی‌فهمه! بهش میگن رهبرت ساده زیسته خیار نمیخورده، خوشحال میشه! دیگه بقیه‌اش…</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/farahmand_alipour/5808" target="_blank">📅 12:47 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5806">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/v4HqklxJfku_mrrXqYQ1CIzBAaSAdMXnTBy2XWgsIZ8NLZpYhdYtn_0Ffil2ADCLPv5yaEQLKbn-1vkJRDS4nQJNYSdsJlnh_ev36mChCgcKMggsMDhaNSi_KyKQA5p675Mf9Pd3eDlUTcCJJrjAuHhTqAeN2sodFUvihxE92uuUigBTsTgyrn7CVmuUPICvqDNITQBDMw6q1IbVqcI929Dg08qTsuwE_3iEWeC3HwJWisRYmWud7z_-PoUxJEERLLbI7p2ycV6DFRuL4e_u_n1Xqj6u52voOKN9gn3d6a6uSPSnCmJZRekX9_iU6-6Fx0FKaWuLy2XRmpe9_Gjn9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PSh8XnVVJtqMeqBeoxSdMkzBP_9sBj26r_9c7BS5O8G50pjkEuePFJQs5eo_jZGjkFvKIoU3A7UhkGeML7_jHBDPg7_jYGZ8Ufy7LCfo_XN9HuwXrMHjrtDPwGs9MXLshAfn4KYhEYO1kIxBEObAKUfhEELYFiUPtJNNpWvfY7gOV2twztQrUqAcD94kxPXcBt7xKe_WTsTodQSqcx_OCm-dqyBoLnjbODXdqhZ1NK9XYaf7iuuLbOcDMECGn7ObWNXsGTAjXWhYWia_4xk0U5IylXiR64mEu7ObKRNND4F2k1Nyn2c7_NBzdCsKHWDQdngLx7rizzeCc7pYRja47g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">هزینه هر روز تعطیلی تهران،  ۲۴۰۰ میلیارد تومن خسارت به اقتصاد کشوره!  اینها فقط ۳ روز برای خامنه‌ای تعطیلش کردن! یعنی فقط این تعطیلات ۷۲۰۰ میلیارد تومن خسارت به اقتصاد میزنه!  این فقط یک قلم از این هزینه هاست!!  ولی خب رهبرشون «ساده زیسته»!  خیار و هندونه…</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/farahmand_alipour/5806" target="_blank">📅 12:35 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5805">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/smUgyRuPHGfoBzNjz_qKV2ynpKmsOiKaDYcjLsTVVo8MQI0VqP0uRnyqfoDbmHADBRSVMQW4krTK4Avt-bHYhBn3rwQvEhCMMOtwm73H_EyzxX3MXo_oAPoAcWF9qC_BFuzFWVirrGe4HQo_6dMxdgLWM_a5IdPyFqbYBTYhaFko-G-mvJentcqXn3qnUR_ponLAuvlw2c95RnsorSuEJNWnNyy661Ev3OrnCSin44VR7goG6AYs5sI3PSZuTVo7Uk0Jmo0M7gcn95z0TJRJzJ-ZCqX3A68VmAQ_k1Updg-20aWhVXplP9t7TSeBQIPFMJWD_MzcE6B0-YLijBu3Vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هزینه هر روز تعطیلی تهران،
۲۴۰۰ میلیارد تومن خسارت به اقتصاد کشوره!
اینها فقط ۳ روز برای خامنه‌ای تعطیلش کردن! یعنی فقط این تعطیلات ۷۲۰۰ میلیارد تومن خسارت به اقتصاد میزنه!
این فقط یک قلم از این هزینه هاست!!
ولی خب رهبرشون «ساده زیسته»!
خیار و هندونه نمیخورد!</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/farahmand_alipour/5805" target="_blank">📅 12:29 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5804">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b7a3755d2.mp4?token=p9cfUxdsT5kiqt9RnqXR2_DlfpyKzrdcapghQ_9W5lt5pQcbO68VygWZBmVWlmcG5__A1w_WGx7ea6ba7i1BLh4Ix0Vp-UeH_kKfr4h5YKX0TlOVAAssoObnZuJzXNhnVuQf9tfJ4ZNex_fHmMkkH7TkHHtgIjYsecS7KLrCW8-yi3DQlw-5kyJnrcx-U0U4Nap35HVgQHiB1YXsDN6lw2kBR0EV8rSxBFMECJbiO2C98aKoctUPRavoMCdDabpqVSED6bOjKfcwXO6dCo0hZsKM1wM12tMGcibdynFhF8Uk0FWWbhm16WgSQTAAhSgVQFCrkI_ZXVRcT8KEEHfgjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b7a3755d2.mp4?token=p9cfUxdsT5kiqt9RnqXR2_DlfpyKzrdcapghQ_9W5lt5pQcbO68VygWZBmVWlmcG5__A1w_WGx7ea6ba7i1BLh4Ix0Vp-UeH_kKfr4h5YKX0TlOVAAssoObnZuJzXNhnVuQf9tfJ4ZNex_fHmMkkH7TkHHtgIjYsecS7KLrCW8-yi3DQlw-5kyJnrcx-U0U4Nap35HVgQHiB1YXsDN6lw2kBR0EV8rSxBFMECJbiO2C98aKoctUPRavoMCdDabpqVSED6bOjKfcwXO6dCo0hZsKM1wM12tMGcibdynFhF8Uk0FWWbhm16WgSQTAAhSgVQFCrkI_ZXVRcT8KEEHfgjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">برنامه «زیر آسمان ستارگان سینما»  در شهر بلونیا در ایتالیا  که ۵۰ شب در طول تابستان برگزار می‌شود.   (در عنوان برنامه در استوری اشتباه کلمه سینما جا افتاده بود)</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/farahmand_alipour/5804" target="_blank">📅 11:16 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5800">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf427145cc.mp4?token=QQJIZr0MEjxAsoODBxMHx604QVqgejCzXidAFUSZJV87DGrtFSobyC7ooX64Y2JMzRuzsTwbONnjy8V7N7klLSenKYIA5YdGzLEYYvgZUvBdYyyCCZQI8m_Pbw3iTJl1D7Rb4s4mMAksFaOZYeeA7D6HkgDWMEy-vY583-leNKj6SvfJzybnkKd8VpCBZCBg-YZFH7UrU4NIO2fRNqvxNSJP5C0lqk5_lN5FiB2JkatF-sBSt5IMPLHahwI6JbfArSQEzCdTlfMR4o0h-e4gMGNh5n5IoEox12K57uwQs0Cah-sV_391H_KNm_uSxr0pL9a7ee1Rnbu6mlXIEcm4WA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf427145cc.mp4?token=QQJIZr0MEjxAsoODBxMHx604QVqgejCzXidAFUSZJV87DGrtFSobyC7ooX64Y2JMzRuzsTwbONnjy8V7N7klLSenKYIA5YdGzLEYYvgZUvBdYyyCCZQI8m_Pbw3iTJl1D7Rb4s4mMAksFaOZYeeA7D6HkgDWMEy-vY583-leNKj6SvfJzybnkKd8VpCBZCBg-YZFH7UrU4NIO2fRNqvxNSJP5C0lqk5_lN5FiB2JkatF-sBSt5IMPLHahwI6JbfArSQEzCdTlfMR4o0h-e4gMGNh5n5IoEox12K57uwQs0Cah-sV_391H_KNm_uSxr0pL9a7ee1Rnbu6mlXIEcm4WA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">برنامه «زیر آسمان ستارگان سینما»
در شهر بلونیا در ایتالیا
که ۵۰ شب در طول تابستان برگزار می‌شود.
(در عنوان برنامه در استوری اشتباه کلمه سینما جا افتاده بود)</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/farahmand_alipour/5800" target="_blank">📅 10:42 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5799">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m46TuP3PAp490yyTC_6e09TgZAx8XWoRcMECmbj6fcvYVRoeicLLevldZpWfnzBzyY4woizHV0xqr0FG4zfqtSoOZ4iLdrOrkLOXw79rp_1EZd-PyPvlw-0GqVJLZlQIvtRaRAMTlUHkVpbIKdfjXT42CvmUxKyPNp7YQa8L7gtI2aImBYzy3FM05CHdDZYei0B5Mf2meSKimT_160ytU_tTh0L9vL94IdqjyTmeMsUl_ybzBXveR2O3rEnX-aanuHjlN2dKwdIN0t_58qagDMn90noEcYuBuMa-vjw3PZRd6kUVBZk5DXPoVX_JBnNQm6gHPWbx69tyAohLzN79fQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هرگز به مردم ایران نخواهند گفت!  اما کاملا قابل پیش بینیه که هزینه این مراسم بارها و بارها از هزینه جشن‌های ۲۵۰۰ ساله بیشتر خواهد بود! چندین برابر!  درست مثل راهپیمایی‌های هر ساله اربعینشون که باید از جیب ملت ایران مصرف بشه!  یادآوری : هزینه جشن‌های ۲۵۰۰ ساله،…</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/5799" target="_blank">📅 09:26 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5798">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2dc44e27bf.mp4?token=R7TroFU-Qti_nte0G899C1BPgXz5QdQoZgO9Ft8oygNVy816D3bLsZeWMGnzIIsY51aWVNq3okT8JruA-5RBII3cKG_IdF1EUmhXui3oLlheaYfYoxg7Vm8LPVMsP28DODQcRB0q1buzIEqLCYU2Z_nk9LaYbftUdcn9jndOFEtPqzKmQVd2V5fNln1eVHu_ggYnKDX6vuk4eOsFElOMXYgGoE9h0H099KkyDMZ_WDbfPd0GQRixwWn1SbjXILdnV7RUE-Fws1s3iMcUREUhra6bIuVI_4HDn89Z4rC1Msr391W1tiYKxkHOS7EdJ3PlsnlaCLrloKqxddsVKR7wDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2dc44e27bf.mp4?token=R7TroFU-Qti_nte0G899C1BPgXz5QdQoZgO9Ft8oygNVy816D3bLsZeWMGnzIIsY51aWVNq3okT8JruA-5RBII3cKG_IdF1EUmhXui3oLlheaYfYoxg7Vm8LPVMsP28DODQcRB0q1buzIEqLCYU2Z_nk9LaYbftUdcn9jndOFEtPqzKmQVd2V5fNln1eVHu_ggYnKDX6vuk4eOsFElOMXYgGoE9h0H099KkyDMZ_WDbfPd0GQRixwWn1SbjXILdnV7RUE-Fws1s3iMcUREUhra6bIuVI_4HDn89Z4rC1Msr391W1tiYKxkHOS7EdJ3PlsnlaCLrloKqxddsVKR7wDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هرگز به مردم ایران نخواهند گفت!
اما کاملا قابل پیش بینیه که هزینه این مراسم بارها و بارها از هزینه جشن‌های ۲۵۰۰ ساله بیشتر خواهد بود! چندین برابر!
درست مثل راهپیمایی‌های هر ساله اربعینشون که باید از جیب ملت ایران مصرف بشه!
یادآوری : هزینه جشن‌های ۲۵۰۰ ساله، به ارز امروز، حدود ۱۲۰ میلیون دلار بود!
هزینه سالانه گروه تروریستی حزب الله لبنان
یک میلیارد دلاره! ۱۰ برابر!</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/5798" target="_blank">📅 09:21 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5797">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d3b713ac56.mp4?token=Pu2m1zUet0Snpz7Z_VD-kX_eijakF61C7EnK8z2WCli1MPD3EYUx5ACmQ6Nuak-S3ih1BJps2ikgVlsLkU8oIVxwwitKr3lVbxUywKhHiYV4ZiLLBKzB36_hD3wQYW03zC6ntjs4zyHsUpK1vcQ2mSBkXoGIJhr4w2s3CK80bSjfn0OGm9c7Ou18kqf-3xZAf4kbkCG8qHGswzakzgKYlddMu6GcwJcQfS0K8ck6vo9jSmuCEP7ebg7pEHu0p_yVkLhxRFevmq440O-a8zc1idTyNcY2DBHsbCQ6n-xazGOUKn-6C3DYc24YXwCWEvYW1ZwpYW8fGDf0-KRrN_dJ6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d3b713ac56.mp4?token=Pu2m1zUet0Snpz7Z_VD-kX_eijakF61C7EnK8z2WCli1MPD3EYUx5ACmQ6Nuak-S3ih1BJps2ikgVlsLkU8oIVxwwitKr3lVbxUywKhHiYV4ZiLLBKzB36_hD3wQYW03zC6ntjs4zyHsUpK1vcQ2mSBkXoGIJhr4w2s3CK80bSjfn0OGm9c7Ou18kqf-3xZAf4kbkCG8qHGswzakzgKYlddMu6GcwJcQfS0K8ck6vo9jSmuCEP7ebg7pEHu0p_yVkLhxRFevmq440O-a8zc1idTyNcY2DBHsbCQ6n-xazGOUKn-6C3DYc24YXwCWEvYW1ZwpYW8fGDf0-KRrN_dJ6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لحظه‌ای که «سپهر بابا» ستاره رفیعی را دید.</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/5797" target="_blank">📅 22:28 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5796">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e1e05c8825.mp4?token=U79MOaUAub3L3xLlwb5uk3CwTPS1fzspFGy5TVGm1PtA5yR3aTUH2r8SMWRMeVCLWM0PBaQ8g8teL5c9LG7S3n9Fg1LG95si61SOPLi-9I6LNbw7l08nFVPyCT9GnYLuJoB9hhdpvNMgL4RKGFfTQ_M-uTEEmx64sNj0RRx_GL4qPSCtI7M4ijpRCkBDa5W6svR0CeapAJa3j3F0MTTbqumvZ850ByHIv1AY5Y6utYwE7J0NWeTzm1WZx958UAFeIqlRTR60QGBX-G2Fp6O9yTt8o3ana1dN5fyYQtRAB6lAdUBy5MSher8YSo1S87KKjUHXroka39KFryze-wX-lg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1e05c8825.mp4?token=U79MOaUAub3L3xLlwb5uk3CwTPS1fzspFGy5TVGm1PtA5yR3aTUH2r8SMWRMeVCLWM0PBaQ8g8teL5c9LG7S3n9Fg1LG95si61SOPLi-9I6LNbw7l08nFVPyCT9GnYLuJoB9hhdpvNMgL4RKGFfTQ_M-uTEEmx64sNj0RRx_GL4qPSCtI7M4ijpRCkBDa5W6svR0CeapAJa3j3F0MTTbqumvZ850ByHIv1AY5Y6utYwE7J0NWeTzm1WZx958UAFeIqlRTR60QGBX-G2Fp6O9yTt8o3ana1dN5fyYQtRAB6lAdUBy5MSher8YSo1S87KKjUHXroka39KFryze-wX-lg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تفاهم‌نامه ج‌ا و آمریکا رو به طور نمادین آتش زدند و گفتند که این قرارداد حقارت‌آمیزه که خب این بخش رو درست میگن!</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/5796" target="_blank">📅 18:49 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5795">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PNsPYGZ0qvEJfuL9Z4J5N1VHys0RiZdUrqdWm8bGwSZNU03sND2ojuxXl1sHTTNoWRS6gRYB2ANuYFtB2R-dvRpUCBVr91dGBwZBfNQi-IN2lWDJ4rqXTvJugZR5WrD6g2vxT-cSUB733sBfEFwwBXBO5tDAzi8dmHa2cE244Igp-kcrbCg_X6ezBruOmcHKl1-6KoTf_vxNeMvs1sr7IilNPTp3wABVo1Yz-0kjo0nq35sU8fYP-JMdgR19hWSpQRGpH3E2GUWNm3LN94S3cHESndtySP7r3iccWFPkhRshLdwwHEU2JmsHBj8REOaYQ-m_1UJUAQ2dRnW6mvExeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امروز - دیدار فرمانده سنتکام با رئیس جمهور لبنان،
یادآوری : دولت لبنان چند ماه پیش
حکم اخراج سفیر جمهوری اسلامی رو صادر کرد
و ج‌ا را متهم به تحمیل جنگ علیه لبنان کرد.
مقامات لبنانی و اسرائیلی چند روز پیش هم مذاکراتی داشتن و گفتن مشکل مرزی و ارضی نداریم!
مشکل دولت لبنان و اسرائیل شده گروه تروریستی حزب‌الله لبنان که با پول مردم ایران تغذیه میشن برای جنگ افروزی!
در جنگی گه برای خون‌خواهی خامنه‌ای راه انداختن و فرار کردن، ۴ هزار لبنانی کشته شدند از جمله ۷۰۰ کودک، قالیباف هم به صراحت گفت لبنان ۴ هزار شهید تقدیم جمهوری اسلامی کرده!
لبنان ولی نمیخواد! جمهوری اسلامی به زور یک گروه مسلح رو راه انداخته اونجا!</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/5795" target="_blank">📅 18:44 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5794">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e972609e9.mp4?token=Tel3TvWVVx058MLNn7oP6biJ0kEIJQsK7FppMx2FWdZxPvOt3Nezqy1077q3cdj3sMAzRlrNSy8aXpvFNIn9xI4oc4O_6uAQCeV-3_G7AEwMJI3A8Z9y8_0uiyvbjGEa716zHViRHoYkNxcKHEe6iFqBV-rNdSqAwqpJ2_seH2r5CpVFInnL0R9HQsoBoyfpe9Tylq5tlXiqxCZELs_NZ8erKdd9JVI83hYjo-mytuEpGWoJd0fJer6H8isuQcnj1bIVt_eAqy4usbd8UPMD1sTDA6Rrv2LvqA4hGqRDKXeIapq-2HGUke5EpMRG5Yd3Rnlj-e3JMaVQhzDvKSqmgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e972609e9.mp4?token=Tel3TvWVVx058MLNn7oP6biJ0kEIJQsK7FppMx2FWdZxPvOt3Nezqy1077q3cdj3sMAzRlrNSy8aXpvFNIn9xI4oc4O_6uAQCeV-3_G7AEwMJI3A8Z9y8_0uiyvbjGEa716zHViRHoYkNxcKHEe6iFqBV-rNdSqAwqpJ2_seH2r5CpVFInnL0R9HQsoBoyfpe9Tylq5tlXiqxCZELs_NZ8erKdd9JVI83hYjo-mytuEpGWoJd0fJer6H8isuQcnj1bIVt_eAqy4usbd8UPMD1sTDA6Rrv2LvqA4hGqRDKXeIapq-2HGUke5EpMRG5Yd3Rnlj-e3JMaVQhzDvKSqmgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این شب‌ها، همین‌ها توی هیئت‌ها در حال عزاداری هستن
ده تا مرد مسلح افتادن به جون یک زن معترض ایرانی.</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farahmand_alipour/5794" target="_blank">📅 18:39 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5793">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pMLjZqa8jDGvb4V2lZZZxJ8AbeO7z1pePiRzy5uueSZQeTZa5B8v8usbLhaBXZdjYxhoYM9LapDgbByc2XExWGewCLpoYDsC47MOfHtw_E6xoeX2Bu-rBhP6c_Uq-b3Z74BgWbCfsYtPMdQLU8A-bhSzpv4eo-n5LCYw1PJPYI4m32rC4qSltmMeFoigQh3T-KTC2xCpD1iZXEINfDklBbGXwu-xK_rJv-J54JI7Fau373WmU1ytfec_oEgWE4jTx2b_e8BkCB8ODVQ7pA6ejt3QDexfEg-gxYwOqqy1X0vndVNSpY5NOuBeDvYsocdpzdejTerkDlaCz78eGTj3sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حالا در حد یونجه و ذرت ایراد نداره</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/farahmand_alipour/5793" target="_blank">📅 18:33 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5790">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uZKe_ndlkB6Z53lpiXzbOZDt9hURQwjWaFHJ2NmsB6YQPkMojpZSJXj10z9e3HS8pYQJIq4yBZEXmJujOGpCoa7hTvIzYUKY6Aps_IcyJSDOIZnXk8EmTsWnufM4D6p8qAuswsjqzEHT-irMctM3ie7ZeXlEIJgy6lvorHNhmMEK82IGak5x1w32szLizqOh9Yx9PrFndzzKIOf5r0HIPXg_d-0nQozjWt6GMbDS0ElH3G4Y2QcCeqNgVwfcV0NUmFMfNfx49SDGwCfNMLqkPomH7RdQpVNexpqHC8_wqtsmMxBXBRlx4KfIrTz32IeHkW_6svYaYYNqqwPBL0hPyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/651901a9ca.mp4?token=UW6aVgQNU7_j9pQAS7IBoqgoe6NTP4vfRrBDxj0SxhTx_AaB80H28j1k3qojVj6oBCHOC5Q-QHObmEs0UFiAbXifEGc9b2Sg6iY0d08S0JUg6sznxjwmGEwEaClUhePQwhCiwTjfM7e0qrmkzr3kvFmfz5F-riOD-sXu3M3wgBwYAkQNa7Y9H59MvTwkB5mutfNARJdhzA25z7j5V3QRijf_sa_f_7wXaL4yFCRYSTxHlZ4z-Gxds9W8NpNIU4-jg6WhU-o96BWlApDJfa-K3ml3nUuQRyGDBoCfpIjEyEMzmVo8ijuji1aNgLnMDQsNiMDjzixctfHI_m72oT9tgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/651901a9ca.mp4?token=UW6aVgQNU7_j9pQAS7IBoqgoe6NTP4vfRrBDxj0SxhTx_AaB80H28j1k3qojVj6oBCHOC5Q-QHObmEs0UFiAbXifEGc9b2Sg6iY0d08S0JUg6sznxjwmGEwEaClUhePQwhCiwTjfM7e0qrmkzr3kvFmfz5F-riOD-sXu3M3wgBwYAkQNa7Y9H59MvTwkB5mutfNARJdhzA25z7j5V3QRijf_sa_f_7wXaL4yFCRYSTxHlZ4z-Gxds9W8NpNIU4-jg6WhU-o96BWlApDJfa-K3ml3nUuQRyGDBoCfpIjEyEMzmVo8ijuji1aNgLnMDQsNiMDjzixctfHI_m72oT9tgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">«عالیه نصیف جاسم» نماینده پارلمان عراق،
عضو کمیسیون مبارزه با فساد، از نزدیکان جمهوری اسلامی، معروف به مواضع تند علیه فساد در عراق، چند روز پیش میوه نذر امام حسین کرده بود. دیشب در موج دستگیری چهره‌های فاسد اقتصادی توسط دولت عراق دستگیر شد، در خونه‌اش ۱۶ میلیون دلار نقد و مقدار بسیار زیادی طلا کشف شد!</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/5790" target="_blank">📅 18:03 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5789">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">شعارها رو گوش بدید،  اینها اعضای سازمان مجاهدین خلق هستند. خوشحال هستند از صدور حکم اعدام برای «حبیب القانیان» ، توسط خلخالی بدنام!  جمهوری اسلامی اعدام می‌کرد، حذف می‌کرد، مصادره می‌کرد، بقیه  گروه‌های از جمله همین سازمان مجاهدین خلق هم تایید می‌کردن، میگفتن…</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/farahmand_alipour/5789" target="_blank">📅 17:05 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5788">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/583cd57ba5.mp4?token=NcndDMkcAfVw4qZaWqzAIyzTRudl6vpdLj9YvVWxQzIpPntqhPMSrrEpceKYZgtzSe4cA2RlmbyUYXMK7_EaFN8wtUDh3ZuwQjqWnblkjOWOAB31CbB9yk8RZUX7rTzLIbiFSIyRMzNAqu9TsF0CkQS1NlRZtsbYX5140VxKQl8RUi8W9jTq6CbjJ-ALBoMYIk4uS5PWWJl_3Hb54ZmAoBbQXYLAVltm9ssov38ypSpoxeRJaSr0glzJuM2QWoVyoogDapNUBvtX0zc4ZbuAjtYX-e-yrs6fIuYSAeIFo7qHLX9LPb1sfHqFqleQvxDoxlHtf9CSHlmAfETsVxAD9TLI1_RUX7wBQVb_nHgE64i_FqHtP_Nxd-IXAomsJtnffWt2Fz8RMeWXF9Stq45iTFZJjOk1jNI9eIRbjhnKokmugia3nZwArpZyxph3hvBRKXP_NWdR7Dhb3gV7AXU2-SWP-UQ2RkEK0mr1IabLksU1KPF9YUncPzMwGecXEmnJeQYVlTUnbGL092ueRXBvEAmqg6AW-WH24NIw3KxaGCs9f9D5MN1bpdokQTta86hLn1V2un9P1m3GU4zsNZsy97kr0ZqWX-O4WgMsc1kDbAV1ST7YkBo3_vF7AGdg9oRloEN1z-J_U_yon8HLv1wUO3Ro8CyRNsWLjv4MQG86rVk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/583cd57ba5.mp4?token=NcndDMkcAfVw4qZaWqzAIyzTRudl6vpdLj9YvVWxQzIpPntqhPMSrrEpceKYZgtzSe4cA2RlmbyUYXMK7_EaFN8wtUDh3ZuwQjqWnblkjOWOAB31CbB9yk8RZUX7rTzLIbiFSIyRMzNAqu9TsF0CkQS1NlRZtsbYX5140VxKQl8RUi8W9jTq6CbjJ-ALBoMYIk4uS5PWWJl_3Hb54ZmAoBbQXYLAVltm9ssov38ypSpoxeRJaSr0glzJuM2QWoVyoogDapNUBvtX0zc4ZbuAjtYX-e-yrs6fIuYSAeIFo7qHLX9LPb1sfHqFqleQvxDoxlHtf9CSHlmAfETsVxAD9TLI1_RUX7wBQVb_nHgE64i_FqHtP_Nxd-IXAomsJtnffWt2Fz8RMeWXF9Stq45iTFZJjOk1jNI9eIRbjhnKokmugia3nZwArpZyxph3hvBRKXP_NWdR7Dhb3gV7AXU2-SWP-UQ2RkEK0mr1IabLksU1KPF9YUncPzMwGecXEmnJeQYVlTUnbGL092ueRXBvEAmqg6AW-WH24NIw3KxaGCs9f9D5MN1bpdokQTta86hLn1V2un9P1m3GU4zsNZsy97kr0ZqWX-O4WgMsc1kDbAV1ST7YkBo3_vF7AGdg9oRloEN1z-J_U_yon8HLv1wUO3Ro8CyRNsWLjv4MQG86rVk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شعارها رو گوش بدید،
اینها اعضای سازمان مجاهدین خلق هستند.
خوشحال هستند از صدور حکم اعدام
برای «حبیب القانیان» ، توسط خلخالی بدنام!
جمهوری اسلامی اعدام می‌کرد، حذف می‌کرد، مصادره می‌کرد، بقیه  گروه‌های از جمله همین سازمان مجاهدین خلق هم تایید می‌کردن، میگفتن خیلی هم خوبه!
تا اینکه جمهوری اسلامی بعدش رفت سراغ
خودشون! و در ابعادی دست به قتل عامی در زندان‌ها در سال ۶۷ زد که در تاریخ ثبت شد.</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/5788" target="_blank">📅 16:57 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5787">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/938419e982.mp4?token=T6rfoxW1gs4JtTfWefge5AVPtV8R6Sg0NHsD0RKlHWsxJ_dbUy_FXnIuW9BshjXy--9LJhBW1NPwnULPf4TaSid_r77TNyRca18AOrlO1pZ7cxqVsdJ_RPctwpIBatefGccpCgrN_mRxA_1zZcN_VokbH6N85ajyuDL_qm7X5JX9S7VSG08kkzysrDM52mPdJRjArnxJXdP6B3mcpY4MxIux8-n2OOq3hMTvZc4JFWlFilaUtL3Ysjq2Q5vKba8D6XeNRMD0Gpvb56tS4aKQOJ81dIx0DkEiDmkV0Wd90NJAGcJNU2QSKnD-SUEfRnpC04t4c1Pr6DPdfgDYMeFK6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/938419e982.mp4?token=T6rfoxW1gs4JtTfWefge5AVPtV8R6Sg0NHsD0RKlHWsxJ_dbUy_FXnIuW9BshjXy--9LJhBW1NPwnULPf4TaSid_r77TNyRca18AOrlO1pZ7cxqVsdJ_RPctwpIBatefGccpCgrN_mRxA_1zZcN_VokbH6N85ajyuDL_qm7X5JX9S7VSG08kkzysrDM52mPdJRjArnxJXdP6B3mcpY4MxIux8-n2OOq3hMTvZc4JFWlFilaUtL3Ysjq2Q5vKba8D6XeNRMD0Gpvb56tS4aKQOJ81dIx0DkEiDmkV0Wd90NJAGcJNU2QSKnD-SUEfRnpC04t4c1Pr6DPdfgDYMeFK6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قدرت حضرت عباس</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/farahmand_alipour/5787" target="_blank">📅 16:27 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5786">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MTYINf5jIb_qqi6b_WJbiOgUvCsLiDsdWIWtWWF6nDtbn-iBDq4PpJ86RrKz_fwuqPZga-mnl4jNf2JDCuP5F1DpnrjkOH-3D7bNhRAN2ru-eiUTqPTeLdh2iQHFvZUBThjet_x5S8UiYtptaqz-fUjuo0HX2w3HFqjQCXCIXaGOytzXiRXxETnYHmx9lODctau-Ir6cBECt5fq00krmGwpT7hXP79zYWnYfwgocHChd0INBBFFersnTRGKzGPXDol4NdFWL5RkbcsTHNqHG2Fy_DbnynUsL2gIm2ztk6V96xHEwHTOAjgSoXRVLhGZaPEBy7YgPDVnLETpRL-xeAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای فروردین ۱۳۹۹  همکاری جن‌های دشمن با سرویس‌های اطلاعاتی علیه جمهوری اسلامی!  همین آخوندها وقتی اصفهان در محاصره ارتش محمود افغان بود به شاه سلطان حسین میگفتن اصلا نگران نباش که ارتشی از جن‌ها میاد به کمک حکومت شیعه!  ولی این جن‌های نامرد نه به امام‌حسین…</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/5786" target="_blank">📅 11:31 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5785">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b91e9581d.mp4?token=uco046HITQDwxIWPmsOrLYSMI7TkGhM7QJ2_vaenl1gsynwtCRtghPQSsH6w2MCsxb7CCd3yxniB8G0oHJxnBiqEkNJ0pWpdcZOTx9gfIUIvEZZ2ukn783AWSXhHiZM6CGz3_2SfoW6y7XfKC695FnC-x2oohZrIIfS99otYrXJJ6NN4H7ixaf9FMkVrXxMuBtXSfakNTxLClN5WKWjoPPrujtAtietw4QbnSu88y3yGbEiXUM9pUbOtTYfbWSRqf64EZymdbVmWNsVmykir3YpdTxPgYHpJuPDixQbojVBxDtF8fPdPGADulCXWsmTmY4F-SxIbJLU0tY2VNLcTHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b91e9581d.mp4?token=uco046HITQDwxIWPmsOrLYSMI7TkGhM7QJ2_vaenl1gsynwtCRtghPQSsH6w2MCsxb7CCd3yxniB8G0oHJxnBiqEkNJ0pWpdcZOTx9gfIUIvEZZ2ukn783AWSXhHiZM6CGz3_2SfoW6y7XfKC695FnC-x2oohZrIIfS99otYrXJJ6NN4H7ixaf9FMkVrXxMuBtXSfakNTxLClN5WKWjoPPrujtAtietw4QbnSu88y3yGbEiXUM9pUbOtTYfbWSRqf64EZymdbVmWNsVmykir3YpdTxPgYHpJuPDixQbojVBxDtF8fPdPGADulCXWsmTmY4F-SxIbJLU0tY2VNLcTHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زعفر جنی، پادشاه‌های جن‌های شیعه
😅
حامیان همین‌ها میان کامنت میگذارن که تاریخ مطالعه کنید! محتوای تاریخ‌هاشون!</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/5785" target="_blank">📅 11:29 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5784">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb5c00112a.mp4?token=AZBdFupQhWgghvYWg32AqbD7qM54Ue3CgOlkLynTuU3TBXozdsE2yCJFWeEFIFrhlIwOhTAkox5487QNV-ySh09txz47DgdwKWyxUmGA23nyCmJzTtFnXFzUvvlnGMyKi-49aohdpmx29lQ00kTKsUqX_xl5Ce5j6elBFl9611xgNsARl1LiOq5C_mCLdKOD5DSST9rSMkaTaHj-p35qmSkEHYRmpl00vuqcJh2OH0mU9isY79hsKH6AuK62k3h57DsXul_sHjcH5oriBpZk6ZgylsLjPBN9CVsICXvTejcgkoUbZ63Y5DOSf25wT2QwIx5n1WqBThf5Xiq3ic5fsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb5c00112a.mp4?token=AZBdFupQhWgghvYWg32AqbD7qM54Ue3CgOlkLynTuU3TBXozdsE2yCJFWeEFIFrhlIwOhTAkox5487QNV-ySh09txz47DgdwKWyxUmGA23nyCmJzTtFnXFzUvvlnGMyKi-49aohdpmx29lQ00kTKsUqX_xl5Ce5j6elBFl9611xgNsARl1LiOq5C_mCLdKOD5DSST9rSMkaTaHj-p35qmSkEHYRmpl00vuqcJh2OH0mU9isY79hsKH6AuK62k3h57DsXul_sHjcH5oriBpZk6ZgylsLjPBN9CVsICXvTejcgkoUbZ63Y5DOSf25wT2QwIx5n1WqBThf5Xiq3ic5fsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زعفر جنی، پادشاه‌های جن‌های شیعه
😅
حامیان همین‌ها میان کامنت میگذارن که تاریخ مطالعه کنید! محتوای تاریخ‌هاشون!</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/5784" target="_blank">📅 11:29 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5783">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/383f2c1b20.mp4?token=hABnTbjC27Id9IpxzTUa_4SO6A6DCotJ0Llkl7Btco1Mdjxh1970Dm3P0jDzVi9MgV3i-jLeM4phg1E_CPMJK1qq4ac-Rx3cBniwykqAsfY9to9t_oN94vhPzwA6f8oGjmsAbSXOiHoE0Vz30wUpvT5_cfmqv-hEGwXg7a4ijXplMuLX0KQaR_BjuUeF_ibsiInJ8ckNf0BgZo0wY9yALmeFVtbawfAB_tymwBtVpUCPJc4sz_iGK5jhIFMzshHXJ_r53Ksq4q0bGel3fQDah7AN0g-KqI5ZeAKliZFOR3Ka2sphmh-wln1pdSsTQd6q-LTTZkAX7_nDukMlCeEZiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/383f2c1b20.mp4?token=hABnTbjC27Id9IpxzTUa_4SO6A6DCotJ0Llkl7Btco1Mdjxh1970Dm3P0jDzVi9MgV3i-jLeM4phg1E_CPMJK1qq4ac-Rx3cBniwykqAsfY9to9t_oN94vhPzwA6f8oGjmsAbSXOiHoE0Vz30wUpvT5_cfmqv-hEGwXg7a4ijXplMuLX0KQaR_BjuUeF_ibsiInJ8ckNf0BgZo0wY9yALmeFVtbawfAB_tymwBtVpUCPJc4sz_iGK5jhIFMzshHXJ_r53Ksq4q0bGel3fQDah7AN0g-KqI5ZeAKliZFOR3Ka2sphmh-wln1pdSsTQd6q-LTTZkAX7_nDukMlCeEZiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همش ثوابه :)</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/farahmand_alipour/5783" target="_blank">📅 11:08 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5782">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a9c5c701b.mp4?token=C2fQrEX525lbmrGMMpnBYcZW6pyvQLd25BqGJNyV5krrgrBQOUBnWdH16Q2enbeffNlUOA6CrZxNYRdJYWX9ZKcZxjEAkIfnAj81Ov5NwVysYC49tpUGwURya0aok4xD61RALax9DaYipGjwnBEOX9xtOpraZKZQL2uxzLbgL0M1guSDBMK2AFZ-OYjzUAsr9iGZ_4ZxIyYyCfgSsU14r-8blonT1vpy6INe-kBkPoCaGjwZgSEbE8967OlRZ3GZfoawS3xjjZGxRx5WwiVHkhJ8MUvgeF64sZC7TLZOzFSZYT_mL2yCVhM5TDP2uhZUzXSKu-hbEYZluH9ucgzHaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a9c5c701b.mp4?token=C2fQrEX525lbmrGMMpnBYcZW6pyvQLd25BqGJNyV5krrgrBQOUBnWdH16Q2enbeffNlUOA6CrZxNYRdJYWX9ZKcZxjEAkIfnAj81Ov5NwVysYC49tpUGwURya0aok4xD61RALax9DaYipGjwnBEOX9xtOpraZKZQL2uxzLbgL0M1guSDBMK2AFZ-OYjzUAsr9iGZ_4ZxIyYyCfgSsU14r-8blonT1vpy6INe-kBkPoCaGjwZgSEbE8967OlRZ3GZfoawS3xjjZGxRx5WwiVHkhJ8MUvgeF64sZC7TLZOzFSZYT_mL2yCVhM5TDP2uhZUzXSKu-hbEYZluH9ucgzHaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آورده فرهنگی شیعه برای ایرانیان</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/farahmand_alipour/5782" target="_blank">📅 09:32 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5781">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jGjEBqrDpeb5VhHjZ-gkDsW9586Wri8OSPLReLPd9vqPb-69-NLyXOeZtqlH9erPg4VTn0NcAybYOEs2ffxGYXA_JBTdVbbqf64iLQ2MSbqo8Uxh6En6uEeQrlZjEIBncglYclUey5GtioKTIusUmqplDUdgk2gCh9PWtaZA0egoeNBz1SJ3mtAIicHxMCbVfadJBErH4mPWNVU_4Z-pEjzxb-ka3Xw4VJIGTObC8MYfms3q08YddVi52WgunAFG9Eq4cEFrzoPgcSsblQNyBy30IdXbw6uBSqhNdUC8rixYCn8D7We95JeF5Hah8oOIzOUh5Z80cbpMsaFN-cbavw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«نبیه بری» دبیر کل حزب امله
همون حزبی است که «موسی صدر»
در لبنان راه اندازی کرده،
همون حزبی که جمهوری اسلامی رفت دو شقه‌‌‌اش کرد
و از دلش، گروه تروریستی حزب‌الله رو ایجاد کرد و باعث یک جنگ حدود دو ساله بین شیعیان لبنان شد.
یعنی روی هم اسلحه کشیدن!
سوریه در زمان حافظ اسد حامی شیعیان امل شد، و جمهوری اسلامی حامی حزب‌الله لبنان.
سایه یکدیگر رو هم با تیر میزدن! برای سال‌های طولانی!
حزب امل، از زمان سقوط رژیم اسد یتیم شده.
جمهوری اسلامی ماهانه حدود ۵۰۰ هزار دلار به نبیه بری پول میده. میشه سالی حدود ۶ میلیون دلار، مه در برابر حدود یک میلیارد دلاری که به حزب الله میده تقریبا هیچه! اما همین ۶ میلیون دلار امورات نبیه بری رو میگذرونه، که در چنین روزهایی دهان باز کنه و به سود جمهوری اسلامی حرف بزنه! بعد از ۳۰ سال دشمنی!</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/5781" target="_blank">📅 09:29 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5780">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🚨
جمهوری اسلامی و آمریکا موافقت کرده‌اند که حملات را ادامه ندهد و سه‌شنبه در قطر دیدار کنند.</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5780" target="_blank">📅 00:08 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5778">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/409f2a841d.mp4?token=sECweXOokX7ozfq4r3uzDaOvOt4K9rR01CRnHCB86YHYEYthwHCIcQncftWLtyEHLAnEG3c2zVcMP4R9FpZ8Si6fQujZCpKDjgNir7JJGi3orUE_b1RKqi0JGOLLgjMH0cnJzRYnpj3dGAxLPjq24BJ3LdmrZ4zVjHe14ArI7gm1gIp-OHEhcKuv_GJiTelLa42T51tbhpJ5loLZkHUF02VJCj1SDWCIbHDTtgFxINAavF0yGrgnkKBcKh4S9cXo2emBVAi2kl7f8ZDgChqrp_L6YnLFh9HpvVvLuQuE_DFR5PvAVgzxwhfruWxvSDwmZAHobOPYg_Jl27y5560Kcw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/409f2a841d.mp4?token=sECweXOokX7ozfq4r3uzDaOvOt4K9rR01CRnHCB86YHYEYthwHCIcQncftWLtyEHLAnEG3c2zVcMP4R9FpZ8Si6fQujZCpKDjgNir7JJGi3orUE_b1RKqi0JGOLLgjMH0cnJzRYnpj3dGAxLPjq24BJ3LdmrZ4zVjHe14ArI7gm1gIp-OHEhcKuv_GJiTelLa42T51tbhpJ5loLZkHUF02VJCj1SDWCIbHDTtgFxINAavF0yGrgnkKBcKh4S9cXo2emBVAi2kl7f8ZDgChqrp_L6YnLFh9HpvVvLuQuE_DFR5PvAVgzxwhfruWxvSDwmZAHobOPYg_Jl27y5560Kcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش اسرائیل از نابودی یک تونل
در روستای مجدل زون در جنوب لبنان خبر داد.
این تونل ۲۰۰ متر طول داشت و در عمق
۲۵ متری زیر زمین ساخته شده بود و در آن
سلاح نگهداری میشد و دارای چند دهانه
برای شلیک به مناطق شمال اسرائیل بود.
اسرائیل گفته که پیش از نابودی این تونل
آمریکا را در جریان قرار داده.</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5778" target="_blank">📅 23:57 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5777">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/06f2d554a0.mp4?token=vQ0Y5Sz8RGuL061l4MW663dR89TAgyHpdmBbT_I9pctG6ssRBAE80B7ETVGwKFhrr0o-d3edLvdNbLhtJ37ydwU6Lwb2h1C61G_SsiVJkmIZ4vN544eV6C7xnP09iOvSOKCWZKeTuSWBozLRua_WOkyZ_m7tKAdM_KFLTXd_G94VhgI2tNwarhL3mQkqz1GCJY2uvlP1iOYNMjXpzzY0YE18Gacip1LFOE9-g1it8k-JMxXt2RZiCAjs4HE0prvxk2UfkEh5pXz8rnmzYMWhZGxrZ_3TrOnj3I3au1dLJVQ_FY_NTBHtZE3_ULwlflknXorSjPKKq-HEyjBLz4IQOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/06f2d554a0.mp4?token=vQ0Y5Sz8RGuL061l4MW663dR89TAgyHpdmBbT_I9pctG6ssRBAE80B7ETVGwKFhrr0o-d3edLvdNbLhtJ37ydwU6Lwb2h1C61G_SsiVJkmIZ4vN544eV6C7xnP09iOvSOKCWZKeTuSWBozLRua_WOkyZ_m7tKAdM_KFLTXd_G94VhgI2tNwarhL3mQkqz1GCJY2uvlP1iOYNMjXpzzY0YE18Gacip1LFOE9-g1it8k-JMxXt2RZiCAjs4HE0prvxk2UfkEh5pXz8rnmzYMWhZGxrZ_3TrOnj3I3au1dLJVQ_FY_NTBHtZE3_ULwlflknXorSjPKKq-HEyjBLz4IQOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">منطق جمهوری اسلامی
و تعریف «امن» و «ناامن»
میگه اگه  یه کشتی بخواد از مسیر «ناامن» عبور کنه بهش شلیک میکنیم :)</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5777" target="_blank">📅 23:26 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5776">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZjDYI1MNOoc7NwBylFAPHKRlWM8NcOm1tzh_g8IXxdrDFQBTQ1J3fXOQRqx2RG5L-XwZX8KxxjyDYQ-qQ6aElQz9dgCr6bUxgsKJFcCeyK6yRXDucqUJiZ2jbDYlyHOB7ZJbem7ls0cnvhajyIQe9TGXCJJlBMmsQpX--Fe3j42hSqUypL4soIoJIfuIRj7JPkT5GIy0IuQwBJhA-EGIqavTudhSg0knJcWPMEmTzZ0jDldkAAjaKN15npg_Yh3ju5ylxvUYOfSF2RJ98VoRs4JO83yknYL0WKQzySZBNyGdJBgwYPKDeoUsCS3-tpAsUUKfQNyRXWLcu28-FNt6pQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس: چاره‌‌ای جز ساخت بمب اتم نیست.</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/5776" target="_blank">📅 19:39 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5775">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e4e9d7782.mp4?token=Q7tRCoqsHXqJ2Og9zWly6bhtQYc_1I31jUuCY5lDy-KPnUnUIykkPiQL7gmO7RkdxXjGSjvmBqDs3wFqpTS6j3kF-dF_RRJ-lzI3QsRxZqn_4ui0O4EtAbi8lvYk-lenkyUqxhQ0fnNaBvz904R4089BlssS-GCK9D--g50UnOanXqB9vX6T7_J3svO2fG-NSCHuGuw4Cmv1Ne5JR_wcM0GclNggPzJ_jiqDkHAQRXbBBA3OfAPb9g_VQYoTYldIo4KTv9tccB8oluZ72Y75MP0rdl2XLLENLQY-qAOYw2nUo5z73JnYrRrcU76gk_Tdxq61XsL10jiYm7ZMh8Z5mQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e4e9d7782.mp4?token=Q7tRCoqsHXqJ2Og9zWly6bhtQYc_1I31jUuCY5lDy-KPnUnUIykkPiQL7gmO7RkdxXjGSjvmBqDs3wFqpTS6j3kF-dF_RRJ-lzI3QsRxZqn_4ui0O4EtAbi8lvYk-lenkyUqxhQ0fnNaBvz904R4089BlssS-GCK9D--g50UnOanXqB9vX6T7_J3svO2fG-NSCHuGuw4Cmv1Ne5JR_wcM0GclNggPzJ_jiqDkHAQRXbBBA3OfAPb9g_VQYoTYldIo4KTv9tccB8oluZ72Y75MP0rdl2XLLENLQY-qAOYw2nUo5z73JnYrRrcU76gk_Tdxq61XsL10jiYm7ZMh8Z5mQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تیمی که با بدرقه قاتلان جوانان ایران راهی جام‌جهانی شده بود.</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/5775" target="_blank">📅 17:23 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5774">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🚨
شب گذشته یک عضو تیپ ‌گولانی ارتش اسرائیل در جنوب لبنان کشته شد.</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5774" target="_blank">📅 13:06 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5773">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">ولی ما می‌د‌ونیم چرا شانس با شما همراه نیست.</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/5773" target="_blank">📅 10:17 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5772">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1220ffd18e.mp4?token=au5uQBlvD1pcZx1Tneajm-bxUGw2jo2PZ1IDDDQY4lzYI5ozDk5qgdNOTrVZjq_SkbBTjqqx8iSLsg3UwKQNxLuDP_1XFK-0ZYZlbL8GE1Ec244qb24EWrpwxU6ZKnhuGvRSyFmbv8idPM1rcXy8zbHyR1kdwWK5i0IxcpHA3kEOc7iLK3Kt3jeNo7Aoh8lGUXwQSiobGNecRZ6JYgzw-ku6BTczSyH6YRr-wv6fNqYVfWa5dXoZKcXAl5EduUQnYbBLixiIn2hJQzMze2Tn-B0hTTD-b4IW0RFApRJqgw5uiHZCdO-Gh2QU8GkgGCgA2198rq54ucnPjrgVwJSywg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1220ffd18e.mp4?token=au5uQBlvD1pcZx1Tneajm-bxUGw2jo2PZ1IDDDQY4lzYI5ozDk5qgdNOTrVZjq_SkbBTjqqx8iSLsg3UwKQNxLuDP_1XFK-0ZYZlbL8GE1Ec244qb24EWrpwxU6ZKnhuGvRSyFmbv8idPM1rcXy8zbHyR1kdwWK5i0IxcpHA3kEOc7iLK3Kt3jeNo7Aoh8lGUXwQSiobGNecRZ6JYgzw-ku6BTczSyH6YRr-wv6fNqYVfWa5dXoZKcXAl5EduUQnYbBLixiIn2hJQzMze2Tn-B0hTTD-b4IW0RFApRJqgw5uiHZCdO-Gh2QU8GkgGCgA2198rq54ucnPjrgVwJSywg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شجاع خلیل زاده میخواست گل بزنه و تقدیم رهبرش کنه!  ولی اراده خدا تحقیر اینها بود!</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/5772" target="_blank">📅 09:32 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5771">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d645372fb2.mp4?token=Dn1eve5tJLhNtx5XC-uQ9Ki8cSURkKt9bCkclDtT7dOksLO9gXOMcjYzH_P_9Ew69w5nibUfBmLyP5mXAHTN7X5-uNcGriAvA7HrENbDBa7GnYRw1L_ZVN4z8v5_mMzpWiqbG1R8OyFysuVvkEcm-PbpGtImNzrpBY1ca0GbscShJ9IFUXy_I3WDbwAH6M3r7d3LgKzNdQHDdQsC7kunlYLlxxDlNQ8PNYd-kgm8GZ_88-trO_6fvMawNBwcRQy6Vu9Bx4WVDWN64olblm0z2mLbEy3Y-5711QKyV-NgpbhdU77mwjT3EKdUrbog04ffIAt7e4o3TLT9RZOCCcafATzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d645372fb2.mp4?token=Dn1eve5tJLhNtx5XC-uQ9Ki8cSURkKt9bCkclDtT7dOksLO9gXOMcjYzH_P_9Ew69w5nibUfBmLyP5mXAHTN7X5-uNcGriAvA7HrENbDBa7GnYRw1L_ZVN4z8v5_mMzpWiqbG1R8OyFysuVvkEcm-PbpGtImNzrpBY1ca0GbscShJ9IFUXy_I3WDbwAH6M3r7d3LgKzNdQHDdQsC7kunlYLlxxDlNQ8PNYd-kgm8GZ_88-trO_6fvMawNBwcRQy6Vu9Bx4WVDWN64olblm0z2mLbEy3Y-5711QKyV-NgpbhdU77mwjT3EKdUrbog04ffIAt7e4o3TLT9RZOCCcafATzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شجاع خلیل زاده
میخواست گل بزنه و تقدیم رهبرش کنه!
ولی اراده خدا تحقیر اینها بود!</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/5771" target="_blank">📅 09:31 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5768">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rcDKMvVRkVUBDFlsIUzRRpX2KUdkYAOBmq3Tzz6R9zpSCVLd-AEUW4VyhHCR0QYRq19dWAOJ127Gf0aJzyAEyDmiuGpGXFPXh6hqB6PUPVnqQ2pFlBx7UiO_D7qZ1Si1Debw7MK37CCiBLOql4XwdjiVqR2Tz1YeZ3-THEdqL3whDhJB7RXK1N3X5hbGLwUPdbE5HilivlWBq_KtBdsRczDDkmUOUUjnJZVhRxfp5F1W3D4fZ2Ha7_Ldi4k9JzaqIJAmbi6pJMnSjFgpKsWciFzrTG58IkshW08_wQOs994vvBnQQywES7Xtbank6WJt8fLalPKz2FkBKxlkC2KQYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qisZf8MxQIBx5W4dgu8ZfMn75n7xes4FogTao1zfXHdIDAhAge92tZbOKBEClzzAQCz4FE5E3Grjse36ZB0mhOLWgXQR8wlFghsWz2YczBkMmVQH-uPfc9r4i74sXEFqfxyCGm-cWEbI6s4BDZndBMrut366sf_D8qp_LjdmSgiN1_EwmeHXMQP6EEU-lGmwLd3fLDWTyMkLtUW5yE7DmlkhGpCiAu0OyVVi1uj7hyke5A9wdTCT1FMTsaLq3XCyp3GR4VWkFMzmXGNkue9MBMJrw3ApwB4H2XCCaL5vX6abk4fezmWb40JBTztG2RdK28jS1--N5qYLdx0o8DR5yQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/q4GPZHShKODZ3Syq0E2bflqarm2Xf6rSezyVu7LUwvLTBXWKF7Hl33VfdcBnB9rfiUPFfBf8myFIup9pmkQHyncEZ6Fpyi7-aMmfCjSpB0iozn-ZV-hmV0uePGjX2XNQp5vgWkG5wRWi26djN9chuHgq0d9cj0PmVZEcXqnnIqodPjW_fKX7rAmdmseK5bn0dPIvH5guIZJjAPDFvKu5Bvg6pO6PX5UKyh5ut4zDiZh2xNY7KfHBXUIM7t2BE83ZV9m1e33rCnJQteOjOv0z5brPjO8jJXVl-hNlBVLFea_UgRzaZxujgJ4MARNUAnFhhvVZ4zQcBSR82nVvpl8p5g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">در جاده فرودگاه بیروت، بیلبوردهای تصویر خامنه‌ای رو حذف کردن و به جاش تصاویری از «اول لبنان» زدند،
که البته دیشب برخی از اعضای گروه تروریستی حزب‌الله رفتن و تخریبشون کردن.
بالاخره زندگی و حیات‌شون در مزدوری رسمی و علنی برای جمهوری اسلامیه.</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5768" target="_blank">📅 09:26 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5767">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">تیم ملا</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5767" target="_blank">📅 08:52 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5766">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/10689e4ea8.mp4?token=VsccBaxmnhc7juJF9CqlDI_X5BjsbF6PtrcxUx-XRWY1yffgKn9hC_YhEUlqZYaDB_-phQBM2dDE8Gz06UBolqIWv-Vxftn5ABWh_JRhfIhdlQkV6zFdsc4X9cJQ2G4qkgARTLFLiGPPdlkcARYlOMQ0jyewFpuzMe1FBCTyatD7QVSGONoKtrMJPWYfoHdm_mzb4A7hxil4RedMyNtG7e-LjO5Ab0-ggVS2sNLHPNWlgsUabdH87oW3ye7p-zNozgR9JpFyikNQ9WA1HDBJIBUEYmc8CN8ZkQBS8suIsu0_5chRS6uHMA-VZpkDttURL75qx3ZTP15lGB0EwdojDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/10689e4ea8.mp4?token=VsccBaxmnhc7juJF9CqlDI_X5BjsbF6PtrcxUx-XRWY1yffgKn9hC_YhEUlqZYaDB_-phQBM2dDE8Gz06UBolqIWv-Vxftn5ABWh_JRhfIhdlQkV6zFdsc4X9cJQ2G4qkgARTLFLiGPPdlkcARYlOMQ0jyewFpuzMe1FBCTyatD7QVSGONoKtrMJPWYfoHdm_mzb4A7hxil4RedMyNtG7e-LjO5Ab0-ggVS2sNLHPNWlgsUabdH87oW3ye7p-zNozgR9JpFyikNQ9WA1HDBJIBUEYmc8CN8ZkQBS8suIsu0_5chRS6uHMA-VZpkDttURL75qx3ZTP15lGB0EwdojDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فقط مدل گزارشگری فوتبال رو!!
یه کشور مسلمان [الجزایر] داره کاری میکنه که یه کشور مسلمان دیگه [تیم ج‌ا] تو دور بعدی باشه!
‏یهووو یه کشور مسیحی[اتریش] گل زد و اینها هم حذف شدن!!  :)</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5766" target="_blank">📅 08:43 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5765">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17301f18ad.mp4?token=QULzo3rvzxGgtlWKbr09sAjSPdBNLTTD6v4ZnFO0pB-mF8HJbDAFMF1UVBRtzUIfdobam9wrfnicbWw69Sa9ne42x177tzGSmC5cVhwpisHBfiSUOOJNMRHklUGbL7FUhFewM8f9UTea7YYxWrIZVVwR2YwADLb4ZBaVviEU74dHdhA5HZyOfa0mViNiNFiufRGoxSt82afiYFnhqWJlfy8eqPPnJdmJuhT-Fatqf3-Dpm03dm2AfkLJwwDb-VDd3qa_cEgejAl-1W35A2EifYsy_-CMQC17meJSicJSEsXVftGuTO1-P5trXE66yUnnJF6QXMs7wjDqmRYuDLPLaWmNc4_-ZcNg7e2cm3diIlhwz93tuzslZ3AX57HtIb-lbrUMMw5-6Wk2HpgHsqipdF3QgEGD3WPYHKMmgXe_3gYnZJRlczR21z87Z_CXwu6cV1OYoedceiTev2DaJquvbmO2Q3iB8nsWdv_tDq4aNgrfECj945yEnWU8jXQYj5UYgh7PEyaq-JbjWNZwa0n3j33KFesTvkW7OuAP9IlAeSy_sS4-c1sxsjthLLoyDL44Tg_XyXuGftAPihmscodi6eYs5GjqwxzB_PEsxpCjSL3pyYzeTzhoe6Qsvm78p_UrswY2FEHSljyko9YxiYkcpS15wUZImUnC9ASgNPno6hA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17301f18ad.mp4?token=QULzo3rvzxGgtlWKbr09sAjSPdBNLTTD6v4ZnFO0pB-mF8HJbDAFMF1UVBRtzUIfdobam9wrfnicbWw69Sa9ne42x177tzGSmC5cVhwpisHBfiSUOOJNMRHklUGbL7FUhFewM8f9UTea7YYxWrIZVVwR2YwADLb4ZBaVviEU74dHdhA5HZyOfa0mViNiNFiufRGoxSt82afiYFnhqWJlfy8eqPPnJdmJuhT-Fatqf3-Dpm03dm2AfkLJwwDb-VDd3qa_cEgejAl-1W35A2EifYsy_-CMQC17meJSicJSEsXVftGuTO1-P5trXE66yUnnJF6QXMs7wjDqmRYuDLPLaWmNc4_-ZcNg7e2cm3diIlhwz93tuzslZ3AX57HtIb-lbrUMMw5-6Wk2HpgHsqipdF3QgEGD3WPYHKMmgXe_3gYnZJRlczR21z87Z_CXwu6cV1OYoedceiTev2DaJquvbmO2Q3iB8nsWdv_tDq4aNgrfECj945yEnWU8jXQYj5UYgh7PEyaq-JbjWNZwa0n3j33KFesTvkW7OuAP9IlAeSy_sS4-c1sxsjthLLoyDL44Tg_XyXuGftAPihmscodi6eYs5GjqwxzB_PEsxpCjSL3pyYzeTzhoe6Qsvm78p_UrswY2FEHSljyko9YxiYkcpS15wUZImUnC9ASgNPno6hA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب خیابانی پیام عربی
به تیم الجزایر داد که ای مسلمین پیروز بشید بر تیم اتریش،
تا اینطوری تیم جمهوری اسلامی
هم بره مرحله بعد،
ولی اراده و برنامه خدا
ناکامی و شکست جمهوری اسلامی بود.</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/5765" target="_blank">📅 08:36 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5764">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/27a845337c.mp4?token=O7-V2WRERUEPeH0cXappVstghDVLI6Zh8ufYpBcX2ifqVAF0iXTO2jKsacG0BETBJYh9kWq8Hw-7DtY5PaDWpzkHtkxYZpuWSGtnmZ6MQmCGHb67suCDRzYUtfpi-H1qBFPxT_TqiJoqfMsVJhW2Xww1bseN8s2ljYRbQGT9EYjTgClSlg1_E84_2gByI9An5-_OjUd1gx_XrSTmLhCCLtNCrCkgySiPutMolp2XytVxwVhaFZmqfQ8nJbQpwvUxGDgCOWc-BLLnAZyS0QP3JBu0WIrVvUOEdPjIfOmilwImNBK0Vz31Y3cJmpGf5cuwsx7EKI41830pH2YqWY6O4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/27a845337c.mp4?token=O7-V2WRERUEPeH0cXappVstghDVLI6Zh8ufYpBcX2ifqVAF0iXTO2jKsacG0BETBJYh9kWq8Hw-7DtY5PaDWpzkHtkxYZpuWSGtnmZ6MQmCGHb67suCDRzYUtfpi-H1qBFPxT_TqiJoqfMsVJhW2Xww1bseN8s2ljYRbQGT9EYjTgClSlg1_E84_2gByI9An5-_OjUd1gx_XrSTmLhCCLtNCrCkgySiPutMolp2XytVxwVhaFZmqfQ8nJbQpwvUxGDgCOWc-BLLnAZyS0QP3JBu0WIrVvUOEdPjIfOmilwImNBK0Vz31Y3cJmpGf5cuwsx7EKI41830pH2YqWY6O4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
تیم فوتبال جمهوری اسلامی رسما از ادامه رقابت‌های جام جهانی حذف شد!</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5764" target="_blank">📅 08:26 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5763">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🚨
🚨
حمله سپاه به بحرین و کویت
سپاه پاسداران اعلام کرده که در پی حملات شب گذشته ارتش آمریکا به تاسیسات نظامی جمهوری اسلامی در اطراف تنگه هرمز، به ۸ سایت نظامی آمریکا در بحرین و کویت حمله پهپادی و موشکی داشت.
🔺
سنتکام شب گذشته به ۱۰ هدف در اطراف تنگه هرمز حمله کرد.
فاکس نیوز این حملات را وسیع‌تر از حملات پریشب توصیف کرده.
🔺
سپاه گفته است که در روزهای آینده حملات بیشتری به پایگاه های آمریکا انجام خواهد داد و پایگاه‌های آمریکایی جهنم را تجربه خواهند کرد.
🔺
کویت و بحرین اعلام کردند که موشک‌‌ها و پهپادهای جمهوری اسلامی را رهگیری و منهدم کردند.
🔺
ترامپ در واکنشی به افزایش تنش‌ها گفت : شاید کار ایران را از طریق نظامی کامل کنیم و دیگر جمهوری اسلامی وجود نخواهد داشت.</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/5763" target="_blank">📅 08:18 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5762">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🚨
🚨
حمله به جزیره قشم
امشب، دومین شب حملات آمریکا به منطقه تنگه هرمز است.</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5762" target="_blank">📅 01:40 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5761">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jURU3ZLmc1dj2ArZFGAf2Nll8VQ3TSU8wvnVsXRwo88JrnfJNwHDGNGjCLCTQOdRtErCSrKzKxSxoNZMSXREO_vWwpml0H6beEnI6Pfu6X5f6aOD0a1L6qUn6V-EcOQbRzztPas4wdnkp6l2i_WX_tbVuYpLeQSkuNc87_Ptfd7WDBnmPOlMWT8bA9mak6k6qjCkGFG2wQqKEvyHDpKhCYgAo1tHpaZ5YiAaqje8VcU4TII5WV_voLjNzlWJZ6kzBaq3-00AR3wfJUGSRDofzdMba0octKd5Q1FEaYK7-fr_4xWw03VcKH3mvayAUaxw-uYsqx6GbC_Rs0HhpJKuFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیانیه سنتکام : به سایت‌های ذخیره پهپاد و سیستم های ارتباطی جمهوری اسلامی حمله کردیم.
متن کامل :
نیروهای فرماندهی مرکزی ایالات متحده (سنتکام)، به دستور فرمانده کل قوا (رئیس‌جمهور آمریکا)، در تاریخ ۲۷ ژوئن حملات دیگری را علیه چندین هدف در ایران انجام دادند.
پس از حملات دیروز آمریکا که در پاسخ به حمله ایران به کشتی
M/V Ever Lovely
صورت گرفته بود، به ایران فرصتی داده شد تا به توافق آتش‌بس پایبند بماند؛ اما ایران با پرتاب یک پهپاد انتحاری در بامداد امروز ساعت ۴:۳۰ (به وقت شرقی) که به نفت‌کش
M/T Kiku
اصابت کرد، نشان داد که این مسیر را انتخاب نکرده است. این نفت‌کش با پرچم پاناما و حامل بیش از دو میلیون بشکه نفت خام، در حال عبور از نزدیکی تنگه هرمز بود.
نیروهای سنتکام امروز در پاسخ مستقیم به ادامه اقدامات خصمانه ایران علیه کشتیرانی تجاری، دست به حملاتی زدند. هواپیماهای نظامی ایالات متحده زیرساخت‌های نظارتی و جاسوسی نظامی، سیستم‌های ارتباطی، سایت‌های پدافند هوایی، تأسیسات ذخیره‌سازی پهپاد و تجهیزات مین‌گذاری ایران را هدف قرار دادند.</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5761" target="_blank">📅 01:27 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5760">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🚨
🚨
اکسیوس:
‏ارتش ایالات متحده در حال انجام حملاتی در منطقهٔ تنگه هرمز است.
این حملات در پاسخ به حمله جمهوری اسلامی به یک کشتی تجاری است.</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/5760" target="_blank">📅 01:10 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5759">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">‏خبرنگار صداوسیما در سیریک:
‏دقایقی پیش صدای چند انفجار شنیده شد.</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/5759" target="_blank">📅 00:56 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5758">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0cee64931e.mp4?token=kPbjLZ1DreRAqQfOeEm2Lp2vpSznEnqo1aRGZKBRaFtruIGJdEnR1RBbY_Q9DgRx2oXMaQ8zcfVU11VTwsZFO5BjXgIT2bFqxGIFkpLuUjc4KAoCcbZpp3WeyU5AgNQtzbhig2mvA1MmtFqtfcDf-wCb3s5jKmswlFACmtMKylHP6lXjbWA3y0BKSDZ42Kt30PqQ7e-gNVc3BYbF0jWjsf_zGecxtXe7mPvrSMj2RLgNFcP4TLso3NpvLwySgH5gRbZe2oHRkAxNLd5KDendL_vzAxNTdm5a5E6d1R9lBg-_ms_hwH72eIfERYvx6V-0zvj3yeahwJ8q67fR3rJuTnAlrUJXA25D2BacymdNh2pQIVJ5xFulVoQTuogDGhPHhdy2fHXJYqKzrkkrDTvdCd9Oawp78c3ZhK7h_3to9WeEGZuqLMFNw34tpnoZ85HdLF_6bXV9oNKBrRdP7zAi-KfW09UDCHQNPoBPltNfMq44CSgQFo9lQ8yseAKKQ5cQUEdF4l69Y5R-mKpuTFI9Qpw1gfk3FcYirSE7ievFoWgOSFc8zfxbDa0h7o8qqMqbIt8_UwKsx7Oo8JMoeoesAPvjCColRo1lLcbefXRmbqlVqPb9RZpb07ihRmMxbAJj65ZdD64lBczhpfhZme2_Xa8L8viZzTXa6UhCFk-7X9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0cee64931e.mp4?token=kPbjLZ1DreRAqQfOeEm2Lp2vpSznEnqo1aRGZKBRaFtruIGJdEnR1RBbY_Q9DgRx2oXMaQ8zcfVU11VTwsZFO5BjXgIT2bFqxGIFkpLuUjc4KAoCcbZpp3WeyU5AgNQtzbhig2mvA1MmtFqtfcDf-wCb3s5jKmswlFACmtMKylHP6lXjbWA3y0BKSDZ42Kt30PqQ7e-gNVc3BYbF0jWjsf_zGecxtXe7mPvrSMj2RLgNFcP4TLso3NpvLwySgH5gRbZe2oHRkAxNLd5KDendL_vzAxNTdm5a5E6d1R9lBg-_ms_hwH72eIfERYvx6V-0zvj3yeahwJ8q67fR3rJuTnAlrUJXA25D2BacymdNh2pQIVJ5xFulVoQTuogDGhPHhdy2fHXJYqKzrkkrDTvdCd9Oawp78c3ZhK7h_3to9WeEGZuqLMFNw34tpnoZ85HdLF_6bXV9oNKBrRdP7zAi-KfW09UDCHQNPoBPltNfMq44CSgQFo9lQ8yseAKKQ5cQUEdF4l69Y5R-mKpuTFI9Qpw1gfk3FcYirSE7ievFoWgOSFc8zfxbDa0h7o8qqMqbIt8_UwKsx7Oo8JMoeoesAPvjCColRo1lLcbefXRmbqlVqPb9RZpb07ihRmMxbAJj65ZdD64lBczhpfhZme2_Xa8L8viZzTXa6UhCFk-7X9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جاوید نام ۲ ساله
💔
‏فرزند ایران و جان فدای میهن، جاویدنام علی محمدصادقی، کودک ۲ ساله، روی شانه‌های پدرش بود که با شلیک گلوله جنگی کشته شد.
‏پیکرش را همان شب تا صبح در برف نگه داشتند و روز بعد به خاک سپردند.</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5758" target="_blank">📅 22:09 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5757">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mG6kZMZkXsK71jTQi3YWyK9zlqy8jZ49aMhVjryN99m1Rl4LsIczqfTy12YDhPQMNHChVW0h3RwZf0XKSvSDuDst2zZuEkscgt1AtkBA3xSVK07zf_FSmVry2Ibv5St3DVUIRcAWk8pa3_kjnPWY1poMv7yuGYsu1gsKFpdfMFgR5JsWpXKUin-jHWxCH1uqWQtjsiVTRdKkpNiwXpK7c6QSD19bXFewGd7oJnW6PIwQfbc56fNLXEn1fXQdNirpdX3Bc2f16uknCqcKsT5RmXWqiOc-YGRTN5Q0DWAVsyBLtsZyd7ix4r5vt2hgL0LyfPU8AKNYjT3m372GwiIseg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
پنج حمله هوایی اسرائیل به نبطیه</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/5757" target="_blank">📅 20:23 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5756">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">«ما و حزب‌الله لبنان تا ابد همسنگریم» !
خب ذوالفقارها!!
چرا آتش بس با اسرائیل رو گدایی میکنید؟
چرا «آتش‌بس» در لبنان رو به عنوان پیش شرط مذاکره با آمریکا اعلام می‌کنید! خب با اسرائیل مبارزه کنید! ببینیم این اسلحه‌ها رو کجاتون فرو میکنه!
در ایام جنگ قیافه مظلوم میگیرن  و کبوتران صلح میشن و دنبال آتش بس هستن! آی سازمان ملل کو! آی حقوق بشر کو!
و در ایام آتش بس یهو شروع میکنن به گنده گویی و شعار و تهدید!
همین جمع اسلحه به دست، همین‌ها! از جمله قاتلان فرزندان ایران در دیماه بودن، که حیدر حیدر کنان مردم ایران رو به خاک و خون کشیدن!
هم‌ایران و مردم ایران رو، هم‌ لبنان رو به گروگان گرفتن!
نتیجه سیاست‌هاشون در فلسطین و شعار اینکه مشت اونها رو موشک کردیم هم جز ویران کردن غزه و دادن ۷۰٪ خاک غزه به اسرائیل نبود! اصلا هم به روی خودشون نمیارن! کارکرد موشک‌هاشون در غزه چی بود؟ ثمره این سیاست‌ها چی بود؟ ثمره ۲۰ سال سیاست هسته‌ای در ایران چی بود؟؟
ثمره جنگ خونخواهی برای خامنه‌ای که در لبنان راه انداختن چی بود؟ جز کشته شدن ۴ هزار لبنانی و گدایی آتش بس؟؟</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5756" target="_blank">📅 18:41 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5755">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">دبیرکل حزب‌الله لبنان، توافق میان‌ دولت لبنان و اسرائیل را که بر مبنای آن حزب‌الله باید خلع سلاح شود و سرزمین‌های لبنان تحویل ارتش لبنان داده شوند را رد کرد و بر ضرورت نگهداری اسلحه تاکید کرد.
حالا این اسکله براتون چی کار کرد؟ یه جنگی شروع کردید و یک پنجم خاک لبنان رو دادید و فرار کردید و از دنیا خواستید بیان آتش‌بس برقرار کنند.</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5755" target="_blank">📅 16:48 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5754">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db5841aafe.mp4?token=eVchJPq3s_s1lw-Owsmv_W7mzwmZammpEzrQywCgxyVlDbOxCrLuXemST8pn9eaPKk9qVyBa19YrdoEsiQppB2XVWrySV9Yv_G7l1G7oihuv2TtMIWNz-YrqN5svnsCV1KHM6IC9YjX2rEwIegPVMWR8ujU5FHsR8OGNMBOcqbU1qQHpkSz7Z-uIcq9WE0NRX1IoVoK3rPDb1y8H6mloZhTbqjwolpgy0tS_jS4Ab02pSF_CMWPQjHjQaBUzVFUYyBZ2oQ4WnLjg3_KMfWX8DScYbuQdfeBH9zejExKwjNIu2bojstapHGNHl6C18WS_-c561C4Ur0sCCNIGok-Rpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db5841aafe.mp4?token=eVchJPq3s_s1lw-Owsmv_W7mzwmZammpEzrQywCgxyVlDbOxCrLuXemST8pn9eaPKk9qVyBa19YrdoEsiQppB2XVWrySV9Yv_G7l1G7oihuv2TtMIWNz-YrqN5svnsCV1KHM6IC9YjX2rEwIegPVMWR8ujU5FHsR8OGNMBOcqbU1qQHpkSz7Z-uIcq9WE0NRX1IoVoK3rPDb1y8H6mloZhTbqjwolpgy0tS_jS4Ab02pSF_CMWPQjHjQaBUzVFUYyBZ2oQ4WnLjg3_KMfWX8DScYbuQdfeBH9zejExKwjNIu2bojstapHGNHl6C18WS_-c561C4Ur0sCCNIGok-Rpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">:)</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5754" target="_blank">📅 16:33 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5753">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f038d1dce.mp4?token=UgKyRoQ_YvOAa_7dVeJjpW9azxGZVBL2D5IQVz4ecqFSLOsLX9nMDZbKTukeNNN5E9qqkxccHNhRsGRc2yEL-Tfj1TTRPM7_iQXFxqrmaAxkA-EsKqR-DgYSxYf7SlrrDHtdna1ZTElk3EWGUM4T2VDH5S-3uZWhk1zndJWQ9KNUBJPKL1dqtN06JGBzene2uX3TeADVQGIgb71z9Q7RSdlaTt-Rg0wXJQQLIJVwukycx7IL2fZr02tokV3zH4IW-LAV40viWlGkX7uz0xhSatzUDfvn1CJBwj2H2YFqKRjVYcoHdtgrfhcCe9-gKbai4LnRJzcdFJNNESWJ5Z7diA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f038d1dce.mp4?token=UgKyRoQ_YvOAa_7dVeJjpW9azxGZVBL2D5IQVz4ecqFSLOsLX9nMDZbKTukeNNN5E9qqkxccHNhRsGRc2yEL-Tfj1TTRPM7_iQXFxqrmaAxkA-EsKqR-DgYSxYf7SlrrDHtdna1ZTElk3EWGUM4T2VDH5S-3uZWhk1zndJWQ9KNUBJPKL1dqtN06JGBzene2uX3TeADVQGIgb71z9Q7RSdlaTt-Rg0wXJQQLIJVwukycx7IL2fZr02tokV3zH4IW-LAV40viWlGkX7uz0xhSatzUDfvn1CJBwj2H2YFqKRjVYcoHdtgrfhcCe9-gKbai4LnRJzcdFJNNESWJ5Z7diA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جشن و شادی در غزه
در پی‌ موفقیت تیم فوتبال مصر
در برابر تیم فوتبال جمهوری اسلامی</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/farahmand_alipour/5753" target="_blank">📅 10:20 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5752">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b07e212ab.mp4?token=LWXNIDyw5x4HaZD6FbMRWV1nUPs60GUZE2PwaN_OPEfzE1kx7FTUumD007299hUMkyEmD_bYKQiMqtf2G4FGGmEnDUBuqXGtvJ2MAJNTlXR9c3M9AL4rwmYnBKoU760GKlkmD0wetCKsDhgVVPpWB1yPosZVhqf2WEp-kIXcl5nOiGOvxtM48tqBF0pg9iH9hAM03jatVTgye_6vxLnm5N55ztxztC_QgJTwcggt3jx9qbcLLDhSevwzGkXJsLOH36ZlM5RtosYVkEuOninofVNA3MGRwLPZabV68t0kxqao7h8fPRdiCQr7-R0N_3iqS1DW_QVQoFdGq3qbQ8pKcw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b07e212ab.mp4?token=LWXNIDyw5x4HaZD6FbMRWV1nUPs60GUZE2PwaN_OPEfzE1kx7FTUumD007299hUMkyEmD_bYKQiMqtf2G4FGGmEnDUBuqXGtvJ2MAJNTlXR9c3M9AL4rwmYnBKoU760GKlkmD0wetCKsDhgVVPpWB1yPosZVhqf2WEp-kIXcl5nOiGOvxtM48tqBF0pg9iH9hAM03jatVTgye_6vxLnm5N55ztxztC_QgJTwcggt3jx9qbcLLDhSevwzGkXJsLOH36ZlM5RtosYVkEuOninofVNA3MGRwLPZabV68t0kxqao7h8fPRdiCQr7-R0N_3iqS1DW_QVQoFdGq3qbQ8pKcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش لبنان برای برخورد با حامیان گروه تروریستی حزب‌الله وارد خیابان‌های بیروت شد.</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/5752" target="_blank">📅 02:02 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5751">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🚨
🚨
🚨
حمله ارتش آمریکا به اطراف تنگه هرمز  ‏فرماندهی مرکزی ایالات متحده (CENTCOM) اکنون تأیید کرده است که هواپیماها در اوایل امروز، 26 ژوئن، به تلافی حمله پهپادی دیروز ایران به یک کشتی تجاری در تنگه هرمز، حملاتی را علیه انبارهای موشک و پهپاد ایران و همچنین سایت‌های…</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/5751" target="_blank">📅 01:17 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5749">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jLjOIX_ITlo3oMVuKkYe7HdDMIg8go0-f5nSEYFnQpPr9jorCjx31Xwv5ukw6KTTGT-forIan88QRZGRq9wAWb_WgBiSyCsdgv-bv-QAfpdIhJ-Jp6dtpN7G0GzhFzru72MyBkiJ9Asdhprc4W_yMehx6rHO4a_4w25egfFfXDVEC8-1Cb0BG2ZTCKChuoKDWkPWBtkeDsjPAFl2PYqmoaT-flgBv38oCgopSleDFvL87XjW9KmDzL3aZOhyVXgRCqvSUqtIhqgiqI-n9e3tYXQf_xNCCDEjidRK53Hhmz6byuV7Di8rT6si4imbAXlGkXAEi22pQs5SQyTCoY-Uhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/farahmand_alipour/5749" target="_blank">📅 01:02 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5748">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jp2bUmR3dBWSXRFwkNrDtGUexUuUEaYFp2_ESFmrVDU9QEhMKYIOvf3URVv9Z5vy6AClvbBYtS3sqzYSwylJ46sXVf9dPr1DjQ-YcOzVI47XUj6g29GAbt6tsEP76uil2Y-UQr0ubL-pKfwdxv9SBDjn4MycUM0gLuWGG6pW1s4nrBGrYMFjmHj_jx5bfQahxApOGFGNfTSlvMMm0OAJfkbjfUKdZOGnNGOTMMh9A9x5-A-cm1l_M9SF47UQry6Pg8f_M05GE3KiNhzN9-kraaNPkxHgLFIflz-Lcvqu83nlo_nQJ8hMayAI00IjcFHZazMfdQmq8E8OWMdRpcXW_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش لبنان برای برخورد با حامیان گروه تروریستی حزب‌الله وارد خیابان‌های بیروت شد.</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/5748" target="_blank">📅 00:59 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5745">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e245d71920.mp4?token=bPh6ZYBeDfMQQTdwzVC12CIClgCPHaD9MPk6FAZKBlepgzkxSpFy6orJmJOJ5Fpo1f5whIgo746NhCctRtInpmEErGKvCwbFL7wRIphqWbT9ZUIIAKVIVHgWK6nR55DEyqsdjVCHW1Pkpdl5C-5__Dla578RbYGrCdaj1x888Mw_xYOo543P6lCbLezmCbDBrJNtdG8WHkn7qZyXmIClONj0r9Xzmu-x12QcQkd9IMqEboZ_6y37vLTU8P4-s6Wyo7qGc_0rraurLTA6ks9HBwYtsx9IPdxujPNJPiIsCfubfXVhJCMaFE_paF4dc_z6aJUir4NlSu5yv2Np4YYapA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e245d71920.mp4?token=bPh6ZYBeDfMQQTdwzVC12CIClgCPHaD9MPk6FAZKBlepgzkxSpFy6orJmJOJ5Fpo1f5whIgo746NhCctRtInpmEErGKvCwbFL7wRIphqWbT9ZUIIAKVIVHgWK6nR55DEyqsdjVCHW1Pkpdl5C-5__Dla578RbYGrCdaj1x888Mw_xYOo543P6lCbLezmCbDBrJNtdG8WHkn7qZyXmIClONj0r9Xzmu-x12QcQkd9IMqEboZ_6y37vLTU8P4-s6Wyo7qGc_0rraurLTA6ks9HBwYtsx9IPdxujPNJPiIsCfubfXVhJCMaFE_paF4dc_z6aJUir4NlSu5yv2Np4YYapA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حامیان گروه تروریستی حزب‌الله
در اعتراض به توافق دولت‌ لبنان و اسرائیل به خیابان ریختند
بر اساس یکی از مفاد این توافق حزب‌الله باید خلع سلاح شود!
اینها مخالف خلع سلاح هستند! تاکید بر مبارزه مسلحانه با اسرائیل دارند! جنگ رو شروع میکنن و بعد سریع از همه دنیا میخوان بیان مداخله کنن برای آتش‌بس!
خب مبارزه کنید!</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5745" target="_blank">📅 00:49 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5744">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bkFg86CFiQTZRSTWOl4Buns7NEIWEwwuAk-GW26TbnflzZ8RwORHcXmaVdDq5tQRJXkh3GN0a8cPAl9KIDPb20IUs5ro5SD1u6PLFcolLYTJJ8jzhNQXETHD_sxKscpKsnEoht3nafr_ABaTZh_Jp-nuk_RSAq71hMLks6URxZ_ypdOHodr8HLQEPwAlCA-I2X9gUeKMUJfCtk-FSgbfuM_MZUJgAtHvKFHafyguADn9e62oeBoYPgoXm1eg-c4kcNq3GuKbkZdJPxtExeMHnPqM_nFjI95tKQ9-_TCSHR_ptBBfC4fU6Wi2eBU4hU8iuEQCxT7WOvfqUlAaoy3gIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/5744" target="_blank">📅 00:31 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5743">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KcLpIFMO5oRuwcxL48DaatGd2gsviFgd18FZKgbXazG1YnVqUWg4bp33GVdPz6AXrmuctV3_yhJzMTRS0hPsmyvzLyqGimBTy0IiTZmQ558r91jcfvcUO48VH8g-tRHhuDtk0-WUYNixdgwLJT_Rke0UnxT5Jxa23HJ8Qwn3Z-7is2_ccTgbzjf7EI9Jt3nBnLB2vnCqqRBsECPgQfB07ieen21lTQ8QKF3xpVIdvmwY-VsybA-oOqRvGC7TXDSy1NtNizvlJoYVjw3RuAHa7wJxR1KWw8IjN1Xox-61bp0yxXm4yOx2_kwlyaP8cmChmbvpefK1TuRhlE-PFac-rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
حمله ارتش آمریکا به اطراف تنگه هرمز
‏فرماندهی مرکزی ایالات متحده (CENTCOM) اکنون تأیید کرده است که هواپیماها در اوایل امروز، 26 ژوئن، به تلافی حمله پهپادی دیروز ایران به یک کشتی تجاری در تنگه هرمز، حملاتی را علیه انبارهای موشک و پهپاد ایران و همچنین سایت‌های رادار ساحلی انجام داده‌اند.</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5743" target="_blank">📅 00:27 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5742">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac9a1f1d75.mp4?token=bIW5EsNKI0WFjv_fK6aucTS74KWf8gutJomrDfHfBD7Fu5CYxOIq78SE6JyC4i6-m2iRvu978wdzQa0n-yCU1Bbv5BvEBO2iGr1chYVFJjvdhZ-h-Osul2z-WOQYTDewOjyb5H0YuV6IkwIN46-htiimSEkZ_NllfSJTKQ1lVGuz_okKqAXm6YJJUAUqgmBGnTirBYhIeQNFyfi-E-QUoSFEN9WbTKO4VbHGfvgRj8mUzzDHsExr4SOLeWIdhUTxE0AGraP4HpSWxL-1UrHgrmKEx6k82C3u6qMRRqHxIlvGcWrXbqXg_lh-MyZLXMc4vGIJBDi_EJisBayVy1DAdLPbRkV6KFC9mC27NMLcvYZ8ffOlsoYIvCWywCnlU-ick1xlSPolUGzmGtoDv7m2tFL0_E1W0t-wSEFRA4rb7V6WFiw-j6cDU7nH_xqB9Tsb7eIYGC8Qj2UIEKjZDZezHACD5nqbYt5eO4UvmzEGaPK5ceY58Dv19wx1wdMBLi5s3oYDuuysEsZL7qiijS9AXxTa5RlGZIBsGnUh-XLoWir3HUPAFu4AqgJdcrPdvnlDlCwzy1PLCqiIJH9mzmjPQSMM5KtIx6H-HKxN8PDQFQ0KY0fq2popDIPlTSVXz888T01Kc87ls6XGp1JDiCRVezMwUrtn_09k2jA9hVPZS8E" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac9a1f1d75.mp4?token=bIW5EsNKI0WFjv_fK6aucTS74KWf8gutJomrDfHfBD7Fu5CYxOIq78SE6JyC4i6-m2iRvu978wdzQa0n-yCU1Bbv5BvEBO2iGr1chYVFJjvdhZ-h-Osul2z-WOQYTDewOjyb5H0YuV6IkwIN46-htiimSEkZ_NllfSJTKQ1lVGuz_okKqAXm6YJJUAUqgmBGnTirBYhIeQNFyfi-E-QUoSFEN9WbTKO4VbHGfvgRj8mUzzDHsExr4SOLeWIdhUTxE0AGraP4HpSWxL-1UrHgrmKEx6k82C3u6qMRRqHxIlvGcWrXbqXg_lh-MyZLXMc4vGIJBDi_EJisBayVy1DAdLPbRkV6KFC9mC27NMLcvYZ8ffOlsoYIvCWywCnlU-ick1xlSPolUGzmGtoDv7m2tFL0_E1W0t-wSEFRA4rb7V6WFiw-j6cDU7nH_xqB9Tsb7eIYGC8Qj2UIEKjZDZezHACD5nqbYt5eO4UvmzEGaPK5ceY58Dv19wx1wdMBLi5s3oYDuuysEsZL7qiijS9AXxTa5RlGZIBsGnUh-XLoWir3HUPAFu4AqgJdcrPdvnlDlCwzy1PLCqiIJH9mzmjPQSMM5KtIx6H-HKxN8PDQFQ0KY0fq2popDIPlTSVXz888T01Kc87ls6XGp1JDiCRVezMwUrtn_09k2jA9hVPZS8E" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اگه خورده گرفتن که چرا میگید سگ هستید …</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/5742" target="_blank">📅 19:53 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5741">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fad365bb7a.mp4?token=ZDr-STvQFPYHiROFw6OPE7okjr7IEHAwGcDfqUYyBg4k0-Dvk9qRQIKcE5xG2aewUJ912dVo_83a_jiYAwUcvSQphHICVJSnFHRCEsILiVyq2xA7qkuZr3bk5_ki9cNSYAuQW9RXOvqhjOSU2zL83IZYkxIZ15AIiPW56JRm1EuZ3RUKct9SeWjS-LFiZfgVlvHezTVkjslzw-S6Ybnjf4E8HQGRf9U2lczcyRXgE_g6QFYzHZV-PLIL5FT8yd0mL40Sp7E4N3lG-LybSPWDd_qpdQBnRXlbNlM4oOGZPr3XikHkTMJCVShwXA1Nnrb6TaFoTfgoL74RMT_P6d5E6wDZIK2pCnijOMtEqc0R0oOCinzAs2nhWjEWijDJfdpAu7yR8nbm8YPllMmHXNhsLQ21uDdtaJm5cPtvyyjyqUtlrSJIZmlzZoBjoZWIOq_aZdGz4mUpi85AqDmv4MgapVkRlwUVa-ZIMPXQTDk3Q7K5wOPxpbEWRK9vpkwjtE4Eo0bdJD1Nznax_9-I_zmq_PesGGBKU0bXPmwwQbJD06zRTD2JvqEDjDnIxE23kvtETO8GrbR9A_jr4jGPdm6LQ0ica0lypeya9QjXA3ib-tNYA-VbNWpRO8VoYEYraocWEY8jLObdCTvagDtR5jcZ6hleQBi26e5V1T7CCwcp1Rk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fad365bb7a.mp4?token=ZDr-STvQFPYHiROFw6OPE7okjr7IEHAwGcDfqUYyBg4k0-Dvk9qRQIKcE5xG2aewUJ912dVo_83a_jiYAwUcvSQphHICVJSnFHRCEsILiVyq2xA7qkuZr3bk5_ki9cNSYAuQW9RXOvqhjOSU2zL83IZYkxIZ15AIiPW56JRm1EuZ3RUKct9SeWjS-LFiZfgVlvHezTVkjslzw-S6Ybnjf4E8HQGRf9U2lczcyRXgE_g6QFYzHZV-PLIL5FT8yd0mL40Sp7E4N3lG-LybSPWDd_qpdQBnRXlbNlM4oOGZPr3XikHkTMJCVShwXA1Nnrb6TaFoTfgoL74RMT_P6d5E6wDZIK2pCnijOMtEqc0R0oOCinzAs2nhWjEWijDJfdpAu7yR8nbm8YPllMmHXNhsLQ21uDdtaJm5cPtvyyjyqUtlrSJIZmlzZoBjoZWIOq_aZdGz4mUpi85AqDmv4MgapVkRlwUVa-ZIMPXQTDk3Q7K5wOPxpbEWRK9vpkwjtE4Eo0bdJD1Nznax_9-I_zmq_PesGGBKU0bXPmwwQbJD06zRTD2JvqEDjDnIxE23kvtETO8GrbR9A_jr4jGPdm6LQ0ica0lypeya9QjXA3ib-tNYA-VbNWpRO8VoYEYraocWEY8jLObdCTvagDtR5jcZ6hleQBi26e5V1T7CCwcp1Rk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همین‌ها رو یک تلویزیون غربی پخش کنه، سریع میگن این برای اسلام هراسیه!</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5741" target="_blank">📅 19:50 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5740">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">ترامپ در شبکه «تروث سوشال»: «جمهوری اسلامی ایران دست‌کم چهار پهپاد انتحاری یک‌طرفه را به‌سوی کشتی‌هایی که از تنگه هرمز عبور می‌کردند، شلیک کرد. یکی از این پهپادها مستقیماً به عرشه بالایی یک کشتی باری بزرگ و بسیار گران‌قیمت برخورد کرد. کشتی آسیب دید، اما توانست به مسیر خود ادامه دهد.
ما سه پهپاد دیگر را سرنگون کردیم.
روشن است که این اقدام، نقض احمقانه توافق آتش‌بس ماست.»</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/5740" target="_blank">📅 19:23 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5739">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/726fb491ae.mp4?token=uiHHvebMOJGS4jaSfruV8MNUkv9-zO5bgNjoGZT0dx-zzzARh86Cd5SJjQ5mbcuPkzl64cnpNgaYLsavNyx8HS3OEnUuOmVwbN5E6n561p0mly0mojXIaPmt5t9fQuu_pdmk-nXXg8vnLYfjIhQSZKvAzmUTHxnFWhLtyMwKjipIac3iWOkNARiM3t66Qrkv3V9BlRuHrcFWVImLZQTKhEBLR37zRBVZRYhSGbIHNpVmLbJT_SvbDlc24ei8_S98P7oMBvFkr16AmBJj9c79_vNOxGQruX5LOS-HKJH637Ih1Gn8FhZJr1NmltkzXHC4RvZ41Jp5cMSVYRmcs28pxYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/726fb491ae.mp4?token=uiHHvebMOJGS4jaSfruV8MNUkv9-zO5bgNjoGZT0dx-zzzARh86Cd5SJjQ5mbcuPkzl64cnpNgaYLsavNyx8HS3OEnUuOmVwbN5E6n561p0mly0mojXIaPmt5t9fQuu_pdmk-nXXg8vnLYfjIhQSZKvAzmUTHxnFWhLtyMwKjipIac3iWOkNARiM3t66Qrkv3V9BlRuHrcFWVImLZQTKhEBLR37zRBVZRYhSGbIHNpVmLbJT_SvbDlc24ei8_S98P7oMBvFkr16AmBJj9c79_vNOxGQruX5LOS-HKJH637Ih1Gn8FhZJr1NmltkzXHC4RvZ41Jp5cMSVYRmcs28pxYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قمه زنان امام حسین رو چرا می‌برید بیمارستان؟  بگید خودش شفا بده!</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/5739" target="_blank">📅 19:16 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5738">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e184bbb012.mp4?token=Y4QRI87rYCrq5fsn4JbT98SWxUzlye_A5exYefpF5d2ZRYxt0ij-o5O0w2QQVCLT3FOoNQ9wLwEusn3hmYm_iju0zAm-asiR_WThTuE5RlYCbdn7y7RIOTdLkjU38brvN6tix8N5LX7iKUarYWbsmBjSYa1U3nyd6lOsT3bMfQl8W9D8RRHMxyUZYdFTjk9sK_uMPae1QipR2IRvzziniaB0NC65ZrRc4kq5ayDBqTJrUubhYYox_9Ntki4ErvXJAZtSU6BdANuY9_0OToTgL3qjgsl6FJXYq8t3TpOKRJBKo3TSEdEcuUe8mBI0yOS6OHOVxKbQHZFtVcZ4Ur-zZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e184bbb012.mp4?token=Y4QRI87rYCrq5fsn4JbT98SWxUzlye_A5exYefpF5d2ZRYxt0ij-o5O0w2QQVCLT3FOoNQ9wLwEusn3hmYm_iju0zAm-asiR_WThTuE5RlYCbdn7y7RIOTdLkjU38brvN6tix8N5LX7iKUarYWbsmBjSYa1U3nyd6lOsT3bMfQl8W9D8RRHMxyUZYdFTjk9sK_uMPae1QipR2IRvzziniaB0NC65ZrRc4kq5ayDBqTJrUubhYYox_9Ntki4ErvXJAZtSU6BdANuY9_0OToTgL3qjgsl6FJXYq8t3TpOKRJBKo3TSEdEcuUe8mBI0yOS6OHOVxKbQHZFtVcZ4Ur-zZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قمه زنان امام حسین رو چرا می‌برید بیمارستان؟
بگید خودش شفا بده!</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/5738" target="_blank">📅 19:09 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5737">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gTN2hkb79Tzm98FZG1GF08TxB0lKRjD7ypligkP-0Gv3YkZNQqxrQTOOOcw7wM9afE87shmq6Pi0YeFi3lKk_ytWeW7acFpLvJr4GEXsojrhhYN6UfMMK08C2waIaP3XeR4sLmA39Jvz0mSnrkK-NR_B9vzmYooXIRo-igGV9VTQBhccZjI6urfJdb3Qv1L5DoUVz6Ie-jc07lpvBQogm11ABbwf29LVG5ONwTgU_2n2Fbw1k4ZGdgmCf48eKaHKvCYtqOnL5cKEgjmQw9OLpr1I_GOrxDtXEM3btJ054lzmHy2jUZeVVWT85yQLeiaA3RT8DJwitjRwOfmeIwnxyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیام فارسی وزیر دفاع اسرائیل خطاب به قاآنی فرمانده سپاه قدس
آماده‌ایم کار را به پایان برسانیم.</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5737" target="_blank">📅 17:53 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5736">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">نحوه اعلام خبر کشته شدن خامنه‌ای
و عدم تعطیلی مدارس</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/farahmand_alipour/5736" target="_blank">📅 16:55 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5735">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MtNh35QrsFNhe07MNGh2s2YYOVRkcz9gdSRdKjiosEGIlV_GmkK6sKIoOTyvQhuSJ4XUwJwAVUhxXMf6z58unA5eVDtEAv7dK-a_TsPKFaUrXmXxDTvS7NiAz9etej3ZbaaiX30oHjiDFkNq7BfEHay3YupPQXSl6Y5WDC0QfnI6O-bjKVbnW-YEIT1EQRQAAssF9n87IZ2E9r__7vO9Mo3b2QYQD3JRk41GQQiypM5TT45KCGFe6TtQWUlacyvHZxii3tjjfgoAyRzQ6tQJOy9VXOEEMxJUfKeNMlgX8MFo178Wff2qADxJRnfRf-_jy8-s6FPPTAE0RHeydJUzvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آتش‌بسی که دولت لبنان و دولت آمریکا
به دست آورده بودند رو رد کردند،
اول ۳ پ در یک بیانیه و بعد حز‌بالله،
۳ هفته آتش‌بس رو انداختن عقب،
۵۰۹ نفر دیگه کشته شدن، از جمله ده‌ها کودک،
تا بگن «جمهوری اسلامی» این آتش‌بس
رو آورد! جمهوری اسلامی و زاده‌هاش،
اینطوری با خون مردم بازی میکنن!
اساسا چرا این جنگ رو شروع کردید که بعد رفتید دنبال آتش بس؟ برای خوانخواهی خامنه‌ای بود دیگه؟!
چرا بعدش افتادید به گدایی آتش‌بس؟؟
ادامه میدادید تا شکست و اخراج دشمن از خاک لبنان!
مگه الان ۲۰٪ خاک لبنان رو ندادید اسرائیل،
آتش بس چرا؟؟  آشغالا!</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/5735" target="_blank">📅 11:38 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5734">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ga9xruGv1StE1MxWz_eca7LoauVIv-Mkb8ua3MQb1L5qyEh3pmnIlbwzorup50r5x5OThby9IZUcEcZUxzV0WKsxwKbZfwQHhla3LkwMTgi8M1KsyAyGJKq7bXoVWY9tbNuT49AvsGr879zFhDLgtAQNSXuIWgdXEGYlGvI89lvWCHnjXiqim214NxyAzDJ2KTE1VMXE3GLuzSTbnsqmxLBkv4nVXQzVtzqCe8aWsE-9NBF-shV5d1nfwFl7cd1hnAr3VDb2MehJO8piso3XkYQRnTJVS7mRr6yGZVwmsvKmy0Vs116e2ApCoh026cWSjh1sf1KrpksFFZBve7iY3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر علوم جمهوری اسلامی  در ترکیه،
خامنه‌ای را از اولاد حسین عنوان کرد.</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/5734" target="_blank">📅 22:29 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5733">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WFoaVNFI1QLLo1nB76IpF__IJhAXYMFW-SqbM3usd5I5uRD_qcZkXZR7uU0bTs5rIOO3sNtYSLBXYK_W8a6bxcmM8wHKxIYxyLeN5YWbeWTCpZquSTflkIztpKxNyK2a5Nw1OzuNMfhsMu0TE3RzkuDpqqiycvxN2qDllE0FiE44YCKLzDGrR0Fl3FUPZ3NSBIOp-MHFnehqrDLNxKPa0f2PnRDMWRm_a3kdUWpnuzGJpm1HEWc7QER-89MfMz4Yvi7Ta8xb3gZc6sbzPIWLyikam2ESOk-sxtuPJ_MMf_F-HYOXVMBdzW2lHXNIBUi1SMqo_AUR1vU5mTKc4Yo4IA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسرائیل به یک خودرو در نبطیه در جنوب لبنان حمله کرد و در نتیجه ۳ تن کشته شدند. مشخص نیست سرنشینان خودرو چه افرادی بودند.
صبح امروز هم در جنوب لبنان یک سرباز اسرائیلی در جریان حملات
حزب الله کشته شد.</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/5733" target="_blank">📅 18:23 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5732">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BmUH9Meq0YXvAeL2MLFsWzYnl8ijpL1m8WDew9aQByhcHpau4ByNEdy-ZE9knDVMtHfNk6QUZoT2qLh9u9Sbh-e3iBbB8CPjZ2wlEg951zrYyaEGdILikLJkoews0xl9jxsH2PUgd0GxOT7tUyquIIMI_73XWvP3rpm9dIzNMzTl_juUjWzor9Xq5RzGh82FFjT4gU9qi20x0rTP3he2VE1R5pg5Rllx_ZmxumVsHYs7DzZylNJhOmA5BT8Yr9QSABtsKBBvI1I5L3C88Dk0CJYrIIVNITTI_fzhkEhuqoYRJnpsRIQpRFiz6DmbcDIjXryBN36r433WQ5ElimPW4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صد رحمت به اهل کوفه!
لااقل به دینارهای طلا فروختند!</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/5732" target="_blank">📅 15:21 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5731">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIran International ایران اینترنشنال</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6715f87786.mp4?token=D8UB6xtzN5z_tbh-WOH1NgshISPnd-1cSxKKW6QLBEk0Y1LjzdiFoAmsC5tSQ69GJTmsYPVtGtA0CGoAbRmvOrC3yNhsSzJ83O8QG4lKbLwbHVlDfMBoZbI2-L2GBLEFevvn7B24Qp_wDqZdAozrBu_64ikanApcwLTkkPRIKKRmElXzYpYWBZ-3K2EZSl1tM2xD_vTY0jueYzXKaam55LHb_H6xxsaZ9jZ4mGQIQkAHTkxt3q3TDM5M68D15sfeXCjnPzK24b4QEvTBzGdClSghZaSYByifyyx-JYQV4VxGXRaQvdkS2PsK70wChNdQB8CZAeCf1x5rcaA365i7nQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6715f87786.mp4?token=D8UB6xtzN5z_tbh-WOH1NgshISPnd-1cSxKKW6QLBEk0Y1LjzdiFoAmsC5tSQ69GJTmsYPVtGtA0CGoAbRmvOrC3yNhsSzJ83O8QG4lKbLwbHVlDfMBoZbI2-L2GBLEFevvn7B24Qp_wDqZdAozrBu_64ikanApcwLTkkPRIKKRmElXzYpYWBZ-3K2EZSl1tM2xD_vTY0jueYzXKaam55LHb_H6xxsaZ9jZ4mGQIQkAHTkxt3q3TDM5M68D15sfeXCjnPzK24b4QEvTBzGdClSghZaSYByifyyx-JYQV4VxGXRaQvdkS2PsK70wChNdQB8CZAeCf1x5rcaA365i7nQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیوی ارسالی به ایران اینترنشنال نشان می‌دهد که صبح چهارم تیرماه در همایونشهر اصفهان پرچمی با نام‌ها و چهره‌های جاویدنامان انقلاب ملی ایرانیان برافراشته شد. بر اساس روایت رسیده، این اقدام «بدون ترس و با قدرت» در جریان مراسم مذهبی «عاشورا» انجام گرفت.</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5731" target="_blank">📅 15:20 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5730">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/afaf9624af.mp4?token=kVOIqT7sPPPJf33Xg3_edwt77BF6fyiil2JAEBz5WRZkGSCuUMJ469QCZWRYLfOeZ6v-VVzt2Q8zc8WuFV0KgLQ4oiOw9q9kEggiT70P45u-7ZomN_JVPdEsLyY4y2xfIvwmk3Eijii1EihCGAmawC5SnDB4jFIpBrohVmr6Fi0HPCHcuNEqAxsl9Xy2hBGvHa4mdEgTH7jiv1ywrNYfjNrEGcsNgv7ps1mG8q0L4XNgk1cj8aNZQvh4sqEKI37KvzhRtVt6j5GxbI6ca_Ndp2MCJz8OxByg6PSDVzoce4OHMiG_UWro68zfvuwb5iCCFvp4Sdve0f5jf5SoQOvKHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/afaf9624af.mp4?token=kVOIqT7sPPPJf33Xg3_edwt77BF6fyiil2JAEBz5WRZkGSCuUMJ469QCZWRYLfOeZ6v-VVzt2Q8zc8WuFV0KgLQ4oiOw9q9kEggiT70P45u-7ZomN_JVPdEsLyY4y2xfIvwmk3Eijii1EihCGAmawC5SnDB4jFIpBrohVmr6Fi0HPCHcuNEqAxsl9Xy2hBGvHa4mdEgTH7jiv1ywrNYfjNrEGcsNgv7ps1mG8q0L4XNgk1cj8aNZQvh4sqEKI37KvzhRtVt6j5GxbI6ca_Ndp2MCJz8OxByg6PSDVzoce4OHMiG_UWro68zfvuwb5iCCFvp4Sdve0f5jf5SoQOvKHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گوشه‌ای از جنایت‌های دیماه جمهوری اسلامی</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5730" target="_blank">📅 12:24 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5729">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">اینفلونسرهای عقب‌‌افتاده‌شون‌ میگردن توی دنیا تا سطل آشغال کشورهای دیگه رو نشون بدن  و بگن ببینید اینجا هم آشغال وجود داره! پس اگه کشور ما رو کلا آشغال گرفته و به زباله‌‌ دانی تبدیل شده، عالیه! عادیه! معمولیه!   مثل همین حمید معصومی نژاد  که دیروز براش نوشتم،…</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5729" target="_blank">📅 12:00 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5728">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u5UkqTjrfDok2viswKFs1iEWZQBvOLf4DBZTgRD7KOHBecL0PdynKmNOftjEfw2yxY5Fve92orPbMVknBQQuxr_epsuLZMPkMciB3i4zWyApq3EIEUERhPd0LODBicDwnbBj-wEb2_BFygZ35PkeiY3Vh3Mr7R68W3s9nRMm6lG1FjyvIaXlNk7uGv8OQ3fPaX3FfVbggENVtvD7Z9z5Oo-0lDyipgTUPSOcl1_QMtMxcnsIU6nImCCTK8zoowCqUNOq4-B-PesC0fWPKWnwmg4RYz1noigoptBonggCCY3qifLgBD6K6V70JL2Q0zG4XtQPipwQlg9Le69nacfgXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینفلونسرهای عقب‌‌افتاده‌شون‌
میگردن توی دنیا تا سطل آشغال کشورهای دیگه رو نشون بدن  و بگن ببینید اینجا هم آشغال وجود داره!
پس اگه کشور ما رو کلا آشغال گرفته
و به زباله‌‌ دانی تبدیل شده، عالیه! عادیه! معمولیه!
مثل همین حمید معصومی نژاد
که دیروز براش نوشتم، میگه فلان مراسم
عزداری، توی چند روستا در جنوب ایتالیا انجام میشه! هر سال هم این موضوع رو یادآوری می‌کنه!  خب اهمیت این چند روستا چیه؟
پارلمان و حکومت و بودجه کشور و قوه قضاییه  نیروی انتظامی و قضات ایتالیا رو از این مجموعه و از این ‌افکار انتخاب میکنن؟
آموزش و دروس و دانشگاه و رسانه‌ها، دست اینهاست؟
از افکار این عده است که صنایع مد و فشن و خوردروی لوکس و ….. ایتالیا در اومده؟
یا از مناطق دیگه کشوره؟
توی اون مناطقی که موجب شدن ایتالیا قدرت‌ هفتم صنعتی جهان بشه و از مراکز مد و فشن،
اصلا این‌ افراد رو راه میدن؟ چی کاره‌ان؟
یه مشت عقب افتاده در حاشیه کشورن! هیچ کاره!</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/5728" target="_blank">📅 12:00 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5727">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🚨
یک سرباز اسرائیلی در جنوب لبنان کشته شد.</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5727" target="_blank">📅 10:30 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5726">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KjASSgFMPmpJfu9PcmP6gbH-InY5yoCJAT5SBxLEMBO877VomEXS5SBYuuj5nzqUx_6VM4F7Q72h12fYk8bzoqHdeXirU5pIjByqlnlplBaxZ5Xl_KXtoZHq9-38ah_czXOO7SxLh0Lgke_KtyPUa-d4QEDB_GJairiKWlDyMRRJXkwBJhIBcmewvIaCUvkDDbPAv0GzkSWvqqDzky1v04_4Ny92NTCP9IhzeVDCme7F-L59XUd97upISn1Yyi5zwhKSyRJqOHecTOBo5auoB61WZy6cdZQEcKFSXY9ms-O4QqJG1CSUBTVpwBFzcrdJGlsXO1cv0Yj3zOrHpoSxtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرمانده گروه هکری «حنظله» که در جنگ ۴۰ روزه کشته شد، ولی خبرش الان منتشر شده.</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/5726" target="_blank">📅 09:39 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5725">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/86c17f6d3c.mp4?token=apA-5834t-pGHPs2gAySnsD4ZtKKqNi5lo983JPvZFtHuSmo8IYcvd16WsbW36Rko3KGMVZttLCsN1maQ-luH1iDdBYJzwFewjoEsSXarhKASavJtJjLAX8FKWxBfp2VH7e-1TOQWRHAjg7Nv1RtTK-RK3LjYp81_FFRmYBKlBDgDypVK-v1w0-yPd79ZYRlPx37-VH-AcjVtPzuMwuz8wPSKD__V98vMUDEmmcm_Thv1uFcSHVMzB2a6GMxMdg32bk2Sn0XWqpwOdFvZTyCjK1afvDqSiSTTSz4CX3SciDNBQJtGxaMKLAR2dFXo9SNj2t16OvwgakjesInsHH10A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/86c17f6d3c.mp4?token=apA-5834t-pGHPs2gAySnsD4ZtKKqNi5lo983JPvZFtHuSmo8IYcvd16WsbW36Rko3KGMVZttLCsN1maQ-luH1iDdBYJzwFewjoEsSXarhKASavJtJjLAX8FKWxBfp2VH7e-1TOQWRHAjg7Nv1RtTK-RK3LjYp81_FFRmYBKlBDgDypVK-v1w0-yPd79ZYRlPx37-VH-AcjVtPzuMwuz8wPSKD__V98vMUDEmmcm_Thv1uFcSHVMzB2a6GMxMdg32bk2Sn0XWqpwOdFvZTyCjK1afvDqSiSTTSz4CX3SciDNBQJtGxaMKLAR2dFXo9SNj2t16OvwgakjesInsHH10A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ میگه جمهوری اسلامی خیلی رفتار خوبی داره با هر چیزی که من میخواستم موافقت کردن!
باید هم موافقت کنن و گرنه دوباره
برمیگردیم سراغشون!</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/5725" target="_blank">📅 22:56 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5724">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">وحید اشتری، فعال رسانه‌ای حکومتی :
تنگه هرمز شبیه یک بومرنگ برگشت به صورت خود ما، در ۴۰ روز گذشته حتی یک بشکه نفت نفروختیم. از لحاظ نظامی توان شکست این محاصره را نداشتیم.
گقتم تنگه هرمز میشه تنگه احد براتون!
به هوای غنیمت گرفتید، ولی فهمیدید باید دو دستی خودتون پس بدید!</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/farahmand_alipour/5724" target="_blank">📅 22:23 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5723">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/171eba79df.mp4?token=pwYjgUxn0ZD6zlvvLJL_67zm7ZylmHd5NGmFuce2Scap1sWDYQ2Hi2gIdlR0Jrq6_4CT38pGiQ6MmCcopOBOlsSkrKILoX-5YNACzKKvJxHjYt0KbKo_t87poprZYNi_Je54RImKvzoQmBUpGVzY2sbbnMLEbUY-lkOD7PPYYV4NURnlPim7R1BXAZi0QqqYYudWQ7_wIITMlAmJhAw4Apmrrsd31ShDeH4wcNgkAxMgLYNQDW8qZqk2zkKY5e85gm8UjAP-_IG7HxGmfUC-WGwSDiY4xJdDkBd7DazNC9rIztVem5y2yV16ieJRZ6LYpteAY1R-B5RB-h8To6iCIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/171eba79df.mp4?token=pwYjgUxn0ZD6zlvvLJL_67zm7ZylmHd5NGmFuce2Scap1sWDYQ2Hi2gIdlR0Jrq6_4CT38pGiQ6MmCcopOBOlsSkrKILoX-5YNACzKKvJxHjYt0KbKo_t87poprZYNi_Je54RImKvzoQmBUpGVzY2sbbnMLEbUY-lkOD7PPYYV4NURnlPim7R1BXAZi0QqqYYudWQ7_wIITMlAmJhAw4Apmrrsd31ShDeH4wcNgkAxMgLYNQDW8qZqk2zkKY5e85gm8UjAP-_IG7HxGmfUC-WGwSDiY4xJdDkBd7DazNC9rIztVem5y2yV16ieJRZ6LYpteAY1R-B5RB-h8To6iCIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قمه زنی گروه بزرگی از شیعیان در کربلا</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/5723" target="_blank">📅 21:46 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5721">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j1SwpmvwOBPJMYMMOJdhvwFSfbF6IZ0kqktoYA0EzPW-SeiBfxLwFOux-WEPVzD-Rue1beN0JuF3f3Et0iObTea8ViSfb5b4s0gqV0DGVjhZIjojkb9UvVCnRZ8fawt-EGVdr8nwTkAyRXCz4lXpXrgiPnQuOr1RC3Uz_dyC4cm2f7ofVk2s6fqZINRfXtMsxmasoc3OCG3uddVzTxroENfHitFsuDBl3csHeZyAJzvaBUZJ6kP3OCj9SQANexpdBy9ro4EzMnGEuGvRy3YLHmlzOSTJz8L34_AxmPBrT0Nh_PfF3GheFIpEhScpdX0xPMXDWi4lrEtdYk4ZoxQWkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تاکید مجدد ترامپ بر ذرت و سویای آمریکایی
و اینکه ج‌ا حق دریافت هیچ درآمدی از تنگه را ندارد.
ترامپ : ایران به ایالات متحده اطلاع داده است که برخلاف گزارش‌های دروغین و جنجال‌آفرین رسانه‌های جعلی، ایران نه از کشتی‌های عبوری از تنگه هرمز عوارضی مطالبه یا دریافت می‌کند،
نه هزینه بیمه‌ای و نه هیچ‌گونه مبلغ دیگری.
اگر این اطلاعات نادرست باشد،
مذاکرات فوراً متوقف خواهد شد!
🔺
همچنین، ایالات متحده هیچ پولی به ایران نداده و هیچ‌یک از دارایی‌های ایران را نیز برای در اختیار گذاشتن به آن‌ها آزاد نکرده است.
🔺
ما بخشی از پول‌های ایران را که کاملاً تحت کنترل ماست، در اختیار کشاورزان و دامداران آمریکایی قرار خواهیم داد تا با آن برای ایران ذرت، گندم،
سویا و محصولات دیگر خریداری شود.
🔺
ایران به‌شدت به مواد غذایی نیاز دارد و ما این مواد غذایی را برای آن‌ها،
منحصراً از ایالات متحده خریداری خواهیم کرد.</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/5721" target="_blank">📅 15:52 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5719">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KcZWWc8wdk9I0yi12uHTC8CiQWkCzNKncM24kxEydM1TC2Jylf8OqJiB-NFLeuiRP04zMJ1GWEX5YI-jXWn2qyVbsG36Ci5zxdUIv4d3XQSfU05a6bdjnNmjELFnToPO67m4BQfom1AnORBqgPasuVQM3zyU-P3mBa2UgUXbo_ORCpDFztWQQk4lVO9__FqQeggnhLOyAL48AYlpogOWz9o12ZRaRSe6Nb-STfM4LSnCQisbk929OAsl5Df6-Vc_DwdNASx-VEHZ88PExE1h1RPBnLiEjcyEjuP_kcN5P8JU86XPk8VIepekacd4wSu5d0Joe0yQjwOhluc5bKX25Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ts6wJTL_jqTM_A2tbG5ql02I78hzRVf-w8V7jK1aa5pEHUzPAO74WaCc3fpgJdfb4YGk9fFjAojFShkus1DaEBXdI8S5t5ku495bzjVYqcUyeqeiYUnWDdqNTxmi9ZZdZtm3luzQdGu5F-3tvsqn9avkrL8hWO5NMemjH3L5s3edYF99R3Ut3D-8RyV70YGLw_0h9fzzTbuNg9DRSjjKob7dX3tW8miOwsa7LPi5QL4TpOaC0ylYJ0kkRa-TF5Hx6fQWia3OWql7IUzSf-Gst5uqtQjkC5szu7clX3VYS0QiEQoNzeOj34HOqE3JA9UkA__QOuD2hYCB-Gjjjj562g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دیروز تولد «آیدا عقیلی» بود
آیدا ۳۴ ساله بود که به دست جمهوری اسلامی و در جریان کشتار ۱۸-۱۹ دیماه به قتل رسید.</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/5719" target="_blank">📅 14:39 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5718">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">‏خبرنگار : اونا می‌گن هیچ بازدید برنامه‌ریزی‌شده‌ای برای بازرسان آژانس وجود نداره؟
‏ترامپ :
بلوف میزنن ، ۱۰۰٪ بازرسی رو ثبت و قطعی کردیم.
‏اگر راست می‌گفتن، همین الان مذاکرات رو لغو می‌کردم.</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/5718" target="_blank">📅 23:27 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5717">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/975d16374b.mp4?token=YAH1uyghocWtVbakbxf29WSBZZa4ca8Bqkzp-gK19l6iZ1l8X7LmCpF0mEc5xmwwxccAN8dx3nRwe1aIhqLSjXsxYFo1ypxZQvOR8K1KD_dNmAWpcywCZvK3HsMq14fqWYCP9HdeSnW8G9yIxBNRfQknW4iYKXvOYXvhYoSCgbH1LcX-sx-3kOslJq9gOu9Pcl_cKQjOZYFxFSVMMwpaFW0pm2-TCVlbHaMMcFHtaC6uOWPRYyDw6uXUsA6nNjIAw2CPE1-ba2rfi1fPmwSb2yZXVmOLP5HPoJ3C3CSgYAz9kQ5d81D4LTBcPlStHk9H-3Ha3HvI3EtgfPE_v454og" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/975d16374b.mp4?token=YAH1uyghocWtVbakbxf29WSBZZa4ca8Bqkzp-gK19l6iZ1l8X7LmCpF0mEc5xmwwxccAN8dx3nRwe1aIhqLSjXsxYFo1ypxZQvOR8K1KD_dNmAWpcywCZvK3HsMq14fqWYCP9HdeSnW8G9yIxBNRfQknW4iYKXvOYXvhYoSCgbH1LcX-sx-3kOslJq9gOu9Pcl_cKQjOZYFxFSVMMwpaFW0pm2-TCVlbHaMMcFHtaC6uOWPRYyDw6uXUsA6nNjIAw2CPE1-ba2rfi1fPmwSb2yZXVmOLP5HPoJ3C3CSgYAz9kQ5d81D4LTBcPlStHk9H-3Ha3HvI3EtgfPE_v454og" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سیرک‌های جمهوری اسلامی</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/5717" target="_blank">📅 23:26 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5716">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zp_CbI5hBsCl3VSpv8qgW5_GEAa5cWWE05-l3D-D6_xbujJZgtrTgY92DO1QKA3u0p2Bv8fT89yXvQvMsW1Vygr0zRg_EhMiJxevgTH6mZp3hyu4tmVFKBLIaW_zTGk_5I4AUg_ZQFRBmBebXuS5oYbonGoOVyonDG3561EUzivX824GGGa5FUH5Klbp7Wo1o8-idcNaB4ekb-fkA8L2pay8EABL4LwcZudVGOSwp7JTmCF5jhyC7Ic8aDiDtdshbMvftqOxJcMolSfTljOV9mVRUsLv2le8HQQ10pvHn5dlA1e5BRca3HHVEq9fnuBjums4DD_63IW78i_DjZ1esQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
شهباز شریف نخست‌وزیر پاکستان:
‏«مذاکرات شامل برنامه موشکی ایران نیز هست و آمریکا و جمهوری اسلامی ظرف ۶۰ روز آینده درباره برنامه موشک بالستیک و موضوع هسته‌ای گفتگو خواهند کرد»</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/5716" target="_blank">📅 19:00 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5715">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EEAnXq1BVi3_zBtmF7dJbZWfpixSxOaVhQuGnEVhWpJjOBtzW8KKJKc7JVkyjZQVkA3FLfp3JT3btd8iOOsdEn5LhsTyNjPTSeL3DInvA4F95xPjvebziinPVKq5_anVV9BmL4i0ImB1zm3KHH5tXHtK0Oc9n1X_rv-0Xspm3xGR68nAHBRLzkU0tyUQP9ixzAJdA_AD7TFfcZdDPdKSG8Qu9pHPwzXkiW_KB1ZSy4zFq53XG-VDpVcjWbgzSD4z6NyHbXcZqRozYrJzmsj6z9YNbJURUieEA8hiKPFf53kXwHDWYER47GIOHWaedBb-sUyvNEuRJ01r_cANfMmHrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/farahmand_alipour/5715" target="_blank">📅 16:50 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5714">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">فکر کن رهبرت رو بدی و سویا و ذرت بگیری.</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/farahmand_alipour/5714" target="_blank">📅 15:27 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5713">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ND1nPx8ShtRTRyABzdhDUapxG53ptS5I40a7LsbFJQEaTOUI-GmHpEp0H76E6baKN9urxoXfeKRF6P2rmhraC6UDQ1f0qla8Ymm3LHqfwMBpmGUL6cMFe1tB4gx22R0sB0Y0PciJTvkU0Y9x72KRLMXLtJ8bh7rZcTsEhb1_2-m6SNYbfioicuPjBAeIMcAj-352dwqRzV92xxjn8LpjodOcQV2C8a9tNBrTj3bJN9sFPwpQiLqsjb0IYGkxtKR9J5AW-lrMqXv_1mG_1KgCxnvckuPjRpLVjey3UAkv0xh_TdjwX29P6hWCsRHVy8Gl1nJ33pIeccr5BqVtwHDd_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان ملل گزارش داده که در عملیات خون‌خواهی خامنه‌ای، توسط تروریست‌های حزب‌الله ،
۱۱ هزار ساختمان،  که میشه
۱۸ هزار واحد مسکونی کاملا ویران شده!
بیش از ۵ هزار واحد مسکونی
هم بالای ۵۰٪ آسیب دیدن!
هزینه‌ این عملیات قهرمانانه!  ۱.۳۸ میلیارد دلار بود
که قاعدتا باید از جیب مردم ایران
پرداخته بشه!
بیش از ۴ هزار نفر رو هم به کشتن دادن
از حمله حدود ۸۰۰ کودک! بیش از ۲۰٪ خاک لبنان رو هم دادند دست اسرائیل!
🔺
آمارهای این گزارش سازمان ملل، شامل ساختمان‌های ویران شده در یک ماه اخیر نمی‌شود!</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/5713" target="_blank">📅 15:12 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5712">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">ترامپ :  با وجود اعتراض‌ها و ادعاهای خلاف واقع آن‌ها، ایران به‌طور کامل و قطعی پذیرفته است که در آینده‌ای بسیار طولانی ــ عملاً برای همیشه ــ تحت بالاترین سطح بازرسی‌های هسته‌ای قرار بگیرد.  این موضوع «صداقت هسته‌ای» را تضمین خواهد کرد. اگر آن‌ها با این شرط…</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5712" target="_blank">📅 14:59 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5711">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ronk4nc-BV618RJTKQ7KUC4wmgqDSuB9IF6wDNsPjPrmcc8rQ9ro49IrvWM8fanOZ_SI1YDx5enMPfwc40oFQw7FIC9OX0oWptHdJlaK1xRDPjVSuEdBM4YzwykUBR2nQ3CPdT3Gl4PuI2CVgkvTFsWYZRnjqz2bLnADJaRC7lLfEZL3uRptIzNIzqLMtBv0jAJGnXxxTEy6dRqc1ntxORHlIE32eyC1EGCs-dkX8AsEEP7IkgCEJvoENNp4hfEE58Z556OLC5fpnhbdpBOMNFwJybzXMRgkCcYhAFPNcAOuQDzCwIVbhGGZCJ4F2GW8feoql2lipVmocfT5V2jS1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ :
با وجود اعتراض‌ها و ادعاهای خلاف واقع آن‌ها،
ایران به‌طور کامل و قطعی پذیرفته است که در آینده‌ای بسیار طولانی ــ عملاً برای همیشه ــ تحت بالاترین سطح بازرسی‌های هسته‌ای قرار بگیرد.
این موضوع «صداقت هسته‌ای» را تضمین خواهد کرد. اگر آن‌ها با این شرط موافقت نمی‌کردند، دیگر هیچ مذاکره‌ای ادامه پیدا نمی‌کرد.
بر اساس این توافق و دیگر امتیازات بزرگی که ایران داده است، من موافقت کرده‌ام که تنگه هرمز باز بماند و محاصره دریایی دیگری اعمال نشود. با این حال، تمام کشتی‌های نظامی همچنان در محل باقی خواهند ماند تا در صورت لزوم، محاصره دوباره برقرار شود.</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5711" target="_blank">📅 14:59 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5710">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c4fa249d98.mp4?token=caS0NfrI2ew_J5tJtKOLsP57ivuQV8JfutRBYil9sfue7VS50LvWZU0b3aSeHbDvE_Wtpyn7vRTIrEuEN94Wrg5YHaQqR42jczu3I1IK0ISOUKUNeOwtCASneqHtdxIgP4NRZEG77siOPogqh2EoJw0e3q7vcvVoQAfMd8nAcTry842WnHhRCXMXB7pV5PNucGq1XrBBXlpN3xtUnXIw-DiH4r7c1J7n7_wqCFFC1UkXKQqjSrDDmuNWMC2cqS8Ljb4W9DB_scROx6d07RSl7bOBf1svOowzW7R90_umzjIMUctgh3Jyau-AVSinNY5GxwS_qxHxKiyrw4xIa61zFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c4fa249d98.mp4?token=caS0NfrI2ew_J5tJtKOLsP57ivuQV8JfutRBYil9sfue7VS50LvWZU0b3aSeHbDvE_Wtpyn7vRTIrEuEN94Wrg5YHaQqR42jczu3I1IK0ISOUKUNeOwtCASneqHtdxIgP4NRZEG77siOPogqh2EoJw0e3q7vcvVoQAfMd8nAcTry842WnHhRCXMXB7pV5PNucGq1XrBBXlpN3xtUnXIw-DiH4r7c1J7n7_wqCFFC1UkXKQqjSrDDmuNWMC2cqS8Ljb4W9DB_scROx6d07RSl7bOBf1svOowzW7R90_umzjIMUctgh3Jyau-AVSinNY5GxwS_qxHxKiyrw4xIa61zFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار  شبکه «الجزیره» ، احمد ویشا
که دو روز پیش توسط  اسرائیل کشته شد</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5710" target="_blank">📅 12:15 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5709">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FgVA9fcYjAdY83lVaBrY6_62qPszJV6WLGBwfQSYmAVhJNZSQJdQJ_nTT3xSjOsnQCBGLtLHQ7unj5iUs58nFgFZx6VMC4xt5ydWlAqbssRaJ7svjhnuNE7akQWjZDCUT_pgqv1NypjFFwfJQpzDh09dhTlqIKn2s_4ZM5SzzhVv07QBFnQ2qSAxZ_TooPq6-zAIkVwelz7L4zMVqVZ7y0nKoZIjo8RQvJfIo6A7sIxUOUO-lZNoEuIT757WwVaO5eUvhan9iKGifIKRj2CqZu6VwNfcdkf77p3k2RpEej6xDwjhXNETjbtZ_wogRjGR5LQBTwl7Eiyvki7yYHQYnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حالا هم‌دیر نشده.
«شیخ نعیم قاسم» می‌تونه از اندوه پیجر‌ها و کشته شدن نصرالله و کشته شدن خامنه‌ای و کشته شدن ۴ هزار لبنانی در جریان خون‌خواهی خامنه‌ای، برای همه یک جا از غصه و اندوه بمیره!</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/5709" target="_blank">📅 12:12 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5708">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y3dK1mWxonWD6wMwG_SdEDgR8XzKgPcoY0rjWko7L2eXa-rD5SNRVvDuYEhzXT_DgzCyPOWRPxY-9_IKbvgi-BwrQ7a9XfEyod5QYGxbff1lcc26HF3BY1IoAGZYfrp6DIJDOCPmCzwcyAOadLZYybX-dddwtes8XQpwrxjhkC45EcoSzn6KNJWPA_5vc3B1FL_bxpXB-dYDbGP-_2fEfCofwigHNrPVB2EKdsBkNM7gUOccGOD00Gv2W4tZ1ajco_iMclBOyejYFZ6bMBiI35hpHsLqvxvEEbtM1hSbXIeDbSP5UYboWbDH26q3cms7pBbJ0SZyTxzgW8CfyZtA9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فکر میکنید شیعیان افراطی فرقه جمهوری اسلامی  فقط با سنی‌ها دشمنی دارند؟  با یهودیان؟ با مسیحیان؟  حتی با شیعیان مذهبی که از فرقه خودشون نیستن هم مشکل دارند! تحملشون نمیکنن.  توی کربلا و نجف وقتی اونها رو می‌بینن دست به انواع کارها میزنن، تا براشون ایجاد مزاحمت…</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/5708" target="_blank">📅 11:43 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5706">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VsR7yjZvHKKYd5GWkf3Mnti2lwA0ChJhd7FgIaz47HbydJrfMfXie5_FIWwN4_SNSVKUg337V4Jh05xgrdMpgiiOWcMXOsFrKob6CfvyFO7lSuBkQnFJXbTWYBcVa-8L9zUWJKVEkO-iO8wXMl29JeAbSFl8qMY6yAVVLVVdtNAN0bA9HsrBhXzR7S-A445gqjOSmU8_k_AIJhZoKA-r6kUxI1n46xD8lYWumJZy-dTeUxkRmycGKmKhxWkKxI7CXu69RmnKGnHrGBr92PXWKbwV5jVNbOX2YGkoBItU2EjfUf3ihxPKwi3tCi-wmoYrDm9SmVjgjgMeBp6L9LPL6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فکر میکنید شیعیان افراطی فرقه جمهوری اسلامی
فقط با سنی‌ها دشمنی دارند؟
با یهودیان؟ با مسیحیان؟
حتی با شیعیان مذهبی که از فرقه خودشون نیستن هم مشکل دارند! تحملشون نمیکنن.
توی کربلا و نجف وقتی اونها رو می‌بینن
دست به انواع کارها میزنن، تا براشون ایجاد مزاحمت کنن. با افتخار هم میگن
بیرونشون کردیم! انحصار طلب‌تر و افراطی‌تر
از این فرقه که با پول نفت و با پول مردم ایران
فربه و وقیح شدند، وجود نداره.</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5706" target="_blank">📅 11:26 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5705">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c656e44d19.mp4?token=TCL-l85Cleixr9TNSznlSU4_4cRhvCObE5ZlonHhZQtyHOMR-Vkx9ACDauvhQFtUC3xobdU7sjx6lDYOlg_Wrcc9b1AgU4vFeHb6cYpGiFRzKIhfswiIYvHqP6Bbbd5pkCEngEmglTX3ag9J65qnWRDn5k-o2aMj9MvE6w22_q8FDzKyz0m1f3EErDs5LG3wEHXxAZEGkelupFF-AgjotYZe1-erlk4_o_ss20DAPsZOtgpEL3Ei7lCkUPTRlRuej5IrR0sZXrLwPRjUAWXThCAV5iCjsnA_WM8gAc9333VK6yhfPy1WJPz953SXbXpT716ChHz6QTEHjqS27NktxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c656e44d19.mp4?token=TCL-l85Cleixr9TNSznlSU4_4cRhvCObE5ZlonHhZQtyHOMR-Vkx9ACDauvhQFtUC3xobdU7sjx6lDYOlg_Wrcc9b1AgU4vFeHb6cYpGiFRzKIhfswiIYvHqP6Bbbd5pkCEngEmglTX3ag9J65qnWRDn5k-o2aMj9MvE6w22_q8FDzKyz0m1f3EErDs5LG3wEHXxAZEGkelupFF-AgjotYZe1-erlk4_o_ss20DAPsZOtgpEL3Ei7lCkUPTRlRuej5IrR0sZXrLwPRjUAWXThCAV5iCjsnA_WM8gAc9333VK6yhfPy1WJPz953SXbXpT716ChHz6QTEHjqS27NktxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تنگه مفتی مفتی گشاد شد</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5705" target="_blank">📅 10:37 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5704">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa6e1aeb6b.mp4?token=DyM8-n9V28qXLUjBGZsij7DauS_f_f4p-4U-542NtzDVViSYmS5rpQtHZUzjR-6c0eZj-ggXelcWPoG06iBZ2Uy6leThm_hurHIrmkUGLCX909qmL494-wb3hRkq5DfTbHz0P9PDzYQ-Yj5yuTRH2174kA9-uUS3MzYnZcJVzJdd2DXZ2foiZIEp5XXTEQztc__GU4bCvmdbdGGGs3irpRBkipz_v08_u5vKCicn06VEv34F46HgGKPfmnCBGTDxFDdSSgsz7lUhe73dA887CtyiOogQ6cTG0ARd2Ci58cl1quuBhrctBHSmmcyo-oy0sIICRp4zNmNU_qWCn-iXlw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa6e1aeb6b.mp4?token=DyM8-n9V28qXLUjBGZsij7DauS_f_f4p-4U-542NtzDVViSYmS5rpQtHZUzjR-6c0eZj-ggXelcWPoG06iBZ2Uy6leThm_hurHIrmkUGLCX909qmL494-wb3hRkq5DfTbHz0P9PDzYQ-Yj5yuTRH2174kA9-uUS3MzYnZcJVzJdd2DXZ2foiZIEp5XXTEQztc__GU4bCvmdbdGGGs3irpRBkipz_v08_u5vKCicn06VEv34F46HgGKPfmnCBGTDxFDdSSgsz7lUhe73dA887CtyiOogQ6cTG0ARd2Ci58cl1quuBhrctBHSmmcyo-oy0sIICRp4zNmNU_qWCn-iXlw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏ترامپ:
‏اگر ایران به توافق خود پایبند نباشد یا رفتار مناسبی نداشته باشد، من کاری را که لازم باشد انجام خواهم داد.</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/5704" target="_blank">📅 23:51 · 01 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
