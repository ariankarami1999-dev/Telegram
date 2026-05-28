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
<img src="https://cdn4.telesco.pe/file/ZXgNxLRwGeFgrDEcxLYBwncoRleNzzsGzS8a6uz6ogWlj1d4lmtFsDXOqTiNH5_ohJqZIP6j5NfKEaU4s2RlIUy-F0rbA3C5_WR4OZ2oS-jMQLUXpXufhKVtdK9eR_M-9BlOIA419_nKHySppgwFZoe1kr7MDmGp_DP0LWTxAQe2sdBbD3lnrvfxLOwYXfLqWqY6q0PqcWLpn6hqwItlWNEqfa0NJNCHOs-9A4ZDvJmVasBlSKxv3LdpHawF-cwQsu9j_ErKIHRl4D87sPAIZ9_xrFOJjf_T6EUsyxX3l58GQUmy6gIfFmhuZ0vS1DOm6sjppqDJfOG83Y70s1OtbA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فوتبال 180</h1>
<p>@Futball180TV • 👥 123K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-07 10:05:14</div>
<hr>

<div class="tg-post" id="msg-90319">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/49f9845215.mp4?token=Higc6-I9oXt4iG-YOSWS2k777yB9yfoUG3sIZ5w8nQdhqkUZsVrkBuisx1RvMI5XHj68YmzJQw3FoX_7FtFyk5D855A7HLbqYqmuYZx1MrwX8Em2mQ3qAJ17wtNDrFm3JtJGPpFWnMlXmKjg_58KECg36krKmLD6kX5b2xOwzpRBof_N_w78fZld36TlT9n2EYBOV5O8iaiBHAEZoSHbNa9k4Wc0MD7grQOnVsfvmF5_TM8fw_rBoHyjRliU-K1QRqz-Gic1HsPnyG9Ckv7eQlVBXluls0b-p2sTgGXqSquj37c33yHYpf79YHOfXbeaFYpNrXLa76yZzLLkj17MKXlt71BvPbsGPPRsboiCnoHHWcUGsEAxl8VC76wOCeWJdbdy-hVSrhM920QGSbkFrKahw4HSp5SarsFb2y8pAP2-Not0icf4QkSLqp-UBPyOlI0mqguCMoraLCytULpeiShj5OOnbA5QQAZUb_1d3k9Ff1qBJrS9jbL_yp0dFGPTQ8O3XqvBW7wRzh5PVwpN3n0nkjL7qtKmp6JHf3W1CZ2nTs30_1lMIzO7f0Osqu2OaK9erZHGV9m-O2D1Z2FcWTgtl074xFwplaHe_uxiDKAnEk6I7Y6RuPDBkTT7VUOt8aA9EDwYBQ1qoN6yMGFK-n1mAUfeKQQ61jFlGZ8CdZY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/49f9845215.mp4?token=Higc6-I9oXt4iG-YOSWS2k777yB9yfoUG3sIZ5w8nQdhqkUZsVrkBuisx1RvMI5XHj68YmzJQw3FoX_7FtFyk5D855A7HLbqYqmuYZx1MrwX8Em2mQ3qAJ17wtNDrFm3JtJGPpFWnMlXmKjg_58KECg36krKmLD6kX5b2xOwzpRBof_N_w78fZld36TlT9n2EYBOV5O8iaiBHAEZoSHbNa9k4Wc0MD7grQOnVsfvmF5_TM8fw_rBoHyjRliU-K1QRqz-Gic1HsPnyG9Ckv7eQlVBXluls0b-p2sTgGXqSquj37c33yHYpf79YHOfXbeaFYpNrXLa76yZzLLkj17MKXlt71BvPbsGPPRsboiCnoHHWcUGsEAxl8VC76wOCeWJdbdy-hVSrhM920QGSbkFrKahw4HSp5SarsFb2y8pAP2-Not0icf4QkSLqp-UBPyOlI0mqguCMoraLCytULpeiShj5OOnbA5QQAZUb_1d3k9Ff1qBJrS9jbL_yp0dFGPTQ8O3XqvBW7wRzh5PVwpN3n0nkjL7qtKmp6JHf3W1CZ2nTs30_1lMIzO7f0Osqu2OaK9erZHGV9m-O2D1Z2FcWTgtl074xFwplaHe_uxiDKAnEk6I7Y6RuPDBkTT7VUOt8aA9EDwYBQ1qoN6yMGFK-n1mAUfeKQQ61jFlGZ8CdZY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">برزیل و هواداران جذابش در جام‌جهانی
🔥
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1.15K · <a href="https://t.me/Futball180TV/90319" target="_blank">📅 09:45 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90318">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T-tzbO_IFHf8u1dVRjHKjudaQuxOU2a-H13RtimPxThje6QPN3XX7Azeg2FeBemdtwutdqDFiqcEBkDTMJd2o2sVQNDWwxLlIxk7lFRztXDsrgmXI_51KlYVR2YsA2YHg4xv3tIw-bIZLekUYC4Z8xjsqSZBU4vbiqa-15KSjl6yBQvmbbwlju8GHYUAjUz-fJedPe9h1bAG7QDWlKkbnEUlqulqjFLj0QF22Hfo9o7-jO5722a_sab-j-z0wJUM17y8ynArmEwQCWFqPJnLnF-OCBv01c4hIoYmFA12TgZyuGaoZuxxxM_Kb-8dWhqf0n1lgya-cimOGHfDmL6SSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پرافتخارترین تیم‌های ملی تاریخ فوتبال جهان
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.16K · <a href="https://t.me/Futball180TV/90318" target="_blank">📅 09:20 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90317">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e84afd40a9.mp4?token=GY0lauXs2WMFWTnrDGtuU1OPEjBhASnx1ibgDVNQbuX2wij32q7B8lpcbqJRmyyKYb0cVAICA7oDO0g1LK6tnl9orAoHevKFk3R1BHCxZPFcCVgc0MY0WVIpbwRuJtMfh8A0MqW6NqRLJfSnvME_Jc_eVesbStEaliQzx7IxYm1LhxuQBJEtKp1CX0Fuz_3ubwD8OFRdqtWGhW4RYYUGiIX3ePjIZ39kl1KVmIBtR0Oen4_WOMS30AhrkZ9x7n4Y-IcSVfFgtXww00Dr621dyM8aadsCVweuMJLATCWHqr50dXeMFL8xDLcMUJ5y3GCjjRGHryeNyPATYjIK-mPDDj7nd05y64eqSQK4_RxY549vRF1dTxN-j_uXyTSMWroRBcH3Aew_qcso4UTIZcRZXIDvcnP_Wzu1KA2NFX3jE43WTBmUHyivzibEQJDX-0-HMY9P5UTbUs51aUJ_tHw9jrENPDwbFT4c3fZJOj01XbhXikNMagUc907F47pHJF0WubuuEYJh_Qbp7wqNB90eAarlyx_ohgiw6dPOAW-NQV8XNGoq4QuJyIiHMY68xoukRKGLnhyxNV5elE_2fOX7j7QoSkRVIteGmHCDkTHbNsGgKc52B5Jj5jX5wEwDz5Yh_U_xWz5XsSrcW-htm86a3Ivh8I3dLJspj9k0ppe9blo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e84afd40a9.mp4?token=GY0lauXs2WMFWTnrDGtuU1OPEjBhASnx1ibgDVNQbuX2wij32q7B8lpcbqJRmyyKYb0cVAICA7oDO0g1LK6tnl9orAoHevKFk3R1BHCxZPFcCVgc0MY0WVIpbwRuJtMfh8A0MqW6NqRLJfSnvME_Jc_eVesbStEaliQzx7IxYm1LhxuQBJEtKp1CX0Fuz_3ubwD8OFRdqtWGhW4RYYUGiIX3ePjIZ39kl1KVmIBtR0Oen4_WOMS30AhrkZ9x7n4Y-IcSVfFgtXww00Dr621dyM8aadsCVweuMJLATCWHqr50dXeMFL8xDLcMUJ5y3GCjjRGHryeNyPATYjIK-mPDDj7nd05y64eqSQK4_RxY549vRF1dTxN-j_uXyTSMWroRBcH3Aew_qcso4UTIZcRZXIDvcnP_Wzu1KA2NFX3jE43WTBmUHyivzibEQJDX-0-HMY9P5UTbUs51aUJ_tHw9jrENPDwbFT4c3fZJOj01XbhXikNMagUc907F47pHJF0WubuuEYJh_Qbp7wqNB90eAarlyx_ohgiw6dPOAW-NQV8XNGoq4QuJyIiHMY68xoukRKGLnhyxNV5elE_2fOX7j7QoSkRVIteGmHCDkTHbNsGgKc52B5Jj5jX5wEwDz5Yh_U_xWz5XsSrcW-htm86a3Ivh8I3dLJspj9k0ppe9blo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از جذاب‌ترین هواداران کشورهای حاضر در جام‌جهانی بدون شک کلمبیا هستن
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.78K · <a href="https://t.me/Futball180TV/90317" target="_blank">📅 08:55 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90316">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c6e129bd0.mp4?token=qjEb2kOkszOTTtktXJ_fsv8dbVjrXeI59r8U_eUbkJYIEsHzHwCQ27kA_03bpEkbQcyupBLlw2275oFlZf_uGwxEq3ZGmnkCxiPNpG4hyyl5iSInMFM5IuDg9TRUe2iJN862olIAQN3WTqi2q-lo1HIKsiBMwAeifHC6ddN-K33Mb2Q1JhS8PUd1BhC-4Y8gvJt_KUeBqJ0L8goZCll0JhDolD3ZW4a43vmrsMCIRMK5eoV6wzLcAIr-ex_iS5yiOGkKNi9ySuPFA58654NWHV6GRPCQuHbX8TE7uz0RqpfCYZDp9dKXlLcPnbibqF9ILCU5gQaPpUJkBYLfASdKPgfzDkBDorv0emIKEMFqu_Azgl01XcVj0cyfLNGvjOWauZZLpLsMyP1Z3R14SkMMf3Kd82fjF1tsAxnbuJpLu5Dp5KKroJv2fgfxoNAZXJi6QPOtqQePExWK0yKyH4bW_8nvSfURNIUnmZR1-0c1KXjLBLWaPt1SEZgx5l8AulZMx2vB28p1MbWnyTELH0l7xHzi_RZD43Jwj3h5FTEVfFAusAQJmCCp_roPhzmAiTahkXcfkbeQECFI7QglV4B31JMqhW2WxN9rK-R8j-PwM9SxVw5upsVZpfW3dY-MPMHW7lS04Xx0c2GS1ZVQZyxj1n7PDQgkMCKpMOQt7JhtN2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c6e129bd0.mp4?token=qjEb2kOkszOTTtktXJ_fsv8dbVjrXeI59r8U_eUbkJYIEsHzHwCQ27kA_03bpEkbQcyupBLlw2275oFlZf_uGwxEq3ZGmnkCxiPNpG4hyyl5iSInMFM5IuDg9TRUe2iJN862olIAQN3WTqi2q-lo1HIKsiBMwAeifHC6ddN-K33Mb2Q1JhS8PUd1BhC-4Y8gvJt_KUeBqJ0L8goZCll0JhDolD3ZW4a43vmrsMCIRMK5eoV6wzLcAIr-ex_iS5yiOGkKNi9ySuPFA58654NWHV6GRPCQuHbX8TE7uz0RqpfCYZDp9dKXlLcPnbibqF9ILCU5gQaPpUJkBYLfASdKPgfzDkBDorv0emIKEMFqu_Azgl01XcVj0cyfLNGvjOWauZZLpLsMyP1Z3R14SkMMf3Kd82fjF1tsAxnbuJpLu5Dp5KKroJv2fgfxoNAZXJi6QPOtqQePExWK0yKyH4bW_8nvSfURNIUnmZR1-0c1KXjLBLWaPt1SEZgx5l8AulZMx2vB28p1MbWnyTELH0l7xHzi_RZD43Jwj3h5FTEVfFAusAQJmCCp_roPhzmAiTahkXcfkbeQECFI7QglV4B31JMqhW2WxN9rK-R8j-PwM9SxVw5upsVZpfW3dY-MPMHW7lS04Xx0c2GS1ZVQZyxj1n7PDQgkMCKpMOQt7JhtN2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">علی لطیفی پیشکسوت فوتبال: کی روش شارلاتان بود، پول می گرفت و بازیکن دعوت می کرد!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.3K · <a href="https://t.me/Futball180TV/90316" target="_blank">📅 08:31 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90315">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🎯
شانستو #رایگان امتحان کن
⚠️
🤔
میدونستی توی #وینرو میتونی  رایگان شرط ببندی؟
👍
تنها کاری که باید بکنی اینه که عضو سایتش بشید و
🤩
🤩
🤩
هزارتومان جایزه بگیرید بدون نیاز به واریز
💖
تنها سایت مورد اعتماد ما با بونوس های کاملا واقعی و رویایی:
🌐
Winro.io
🌐
Winro.io…</div>
<div class="tg-footer">👁️ 6.61K · <a href="https://t.me/Futball180TV/90315" target="_blank">📅 01:14 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90313">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QFBGWfbsmH2X--9Tf6XXoZFCJ2ixvTQ_ez9TxGmZV_ifilpwNOwcqD6ULGJsdWZk9-_taUXpPGl5_PcMYyHrYfulQUmlKz8dox8JtCsiND6lCRSX6cDPy5b3ExjwMBuE5y-tnnEdG_DU7-pdQjfHz1t9GE6p_5SGcHcqPSwraEw1BJxS1zEh52LQO_lOkCFF4CEwwqxF-RCa_XNazkx4qABedBQykNZJAdglIuRfbuMv0bE0ggdXZXx4gEvsZiSbbCu-iwtq8H6myq4RPSQKZaaEQzHQGCL70DIidr1ODFeIyBKxclEWbmBUNpduMzlCjukLR_q9ERUAMy3mSz8btQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎯
شانستو
#رایگان
امتحان کن
⚠️
🤔
میدونستی توی
#وینرو
میتونی  رایگان شرط ببندی؟
👍
تنها کاری که باید بکنی اینه که عضو سایتش بشید و
🤩
🤩
🤩
هزارتومان جایزه بگیرید بدون نیاز به واریز
💖
تنها سایت مورد اعتماد ما با بونوس های کاملا واقعی و رویایی:
🌐
Winro.io
🌐
Winro.io
کانال بونوس های رایگان
a6
📱
@winro_io</div>
<div class="tg-footer">👁️ 6.59K · <a href="https://t.me/Futball180TV/90313" target="_blank">📅 01:13 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90312">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qRzMJReUmk8hwMRfWCy8xSvYXoZ6KaSGxdiQwN5cRaAKq4Sqvt9jZPk_n1atP-ncz7s_ScO6Xvp8atB14bZ8GgmDkpUCieR5ZEZs_TI0hwqO8JtI1imWZ-Ur3j45Iub9Oj1ypEbrOymUaTvfjoNboNNEOejz38pJqxgvnLe4uJiKwM79kAeyNkmzvDN8t9pWormPb4AQsgTQ2UskFFXii_efGyU5s47gOeeNEyGFJN_bA8AM7T_dddP9V4EdgiXdMRWuEVgaDsrCPrYG5mzUL0il5mE_KO8W63Sva12upOexZ9GZxwrcldJfr8V2Tt-6wYLabqE1L1pB9jBN53XWsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تیم‌فوتبال کریستال‌پالاس قهرمان لیگ‌کنفرانس شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.23K · <a href="https://t.me/Futball180TV/90312" target="_blank">📅 01:12 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90311">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aAc81RRyjuVoidZHMTmEXwJXhRd6SICxPzzINra_MBHHT58BQ-vC6kPoKGdyRtbD97LUSureFU2PGsxdlvjRFA8EggUQThW1JEj26nXRdAxqvDHrcfAVucATn8f9pwSenTZ6dqKBbpRsRrxEPc_1sPRyQXfbl_tB4n_ST_gS8G49GCnObt9vWwUiEtcZHhUFXutq1z7LaIsO9dQZLI8xZpUz-bhEDfEoQx066Vmf3u80qIWIPJMt5i2n6f3SJ7clqxirF4L2RN0il1vs3m5vtnVes62PUUCyFQ5DTeM_PsTHoqU0XkPVMiBussZSTKpD7-Rc2rImjf8iRb6hpjlxnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کافو تنها بازیکن تاریخ فوتبال است که توانسته سه دوره به فینال جام‌جهانی دست‌یابد. حالا لیونل‌مسی و امباپه این فرصت را دارند که در کنار کافو تاریخ‌ساز شوند
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.72K · <a href="https://t.me/Futball180TV/90311" target="_blank">📅 23:55 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90310">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🚨
🚨
برخی اخبار کاربران گویا این است که سرویس گوگل‌پلی درحال‌حاضر رفع فیلتر شده است
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.52K · <a href="https://t.me/Futball180TV/90310" target="_blank">📅 23:30 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90309">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l4BuwOmX5Q5hXdTzQJWh-J_RJgAf5JTQy7dw4YIepMpum9XXgOQw3HD0o67z5ILG-DzWoPYfrdBGbH0b8k8B9_u8U41zDh3qkTE4p_onJ5LoWlQVsTfqcg0uj8rITQC6oP1_1QWfo7c28dzx5GsHH66_HPyMDPHuQx_FWmmVZQwZd2ci6-IRvsI2M-AU_TmNhx_M1YbSvT9Htt8vBnWSA-xFUaof9Wc5bEhm_3dlctlM5lUuKFYb-vqp6Jw3rna2pO7gBNo2ER_xoE1q_mqCULdccTeIUqPeKxCPYchLAkw9_9mmI7gVzTNFCJsc-ez0Y3pBRCLMS0LXGvxVIQBv-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عملکرد تاریخی اسطوره فوتبال مردان و زنان بارسا
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.49K · <a href="https://t.me/Futball180TV/90309" target="_blank">📅 23:25 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90308">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W3evZK2281CBnBTeIzi5ZTiv3wdHSp5MH1pFnlFuLelmBDa1gjJvtt5IoMwpfsT-yp74Zd1ejUvmDG_mE6s_C7Gh_shh02lDwWur0W4vBH7yCcPjojVxqRygOxjBWTATMec8Ouhf78WTWW12yp6EEvPiupHR4Y0TQxnmUj7ohbm06P_zmxkX-JClgVzfkGfX-uGcM2l-ZPody6NGGmpFjfnCa-nyK9QtIq47QlyF8Z7HAeQuJLjb2XFuz4N6gpXRlCVpPadSa-O3UDWR1gFfcaixDR-e-fBRUFSbWUpV5Barnu3bZR3MosHP9LDRAyWgwL4gNfUA4U-6QZPxkTpxtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
گردونه شگفت‌انگیز جام جهانی
🏆
⏩
با پیش‌بینی رقابت‌های ورزشی و بازی‌های کازینویی، مراحل هفتگی «گردونه شگفت‌انگیز» ویژه جام جهانی را تکمیل کرده و هر هفته تا دو چرخش دریافت کنید.
اطلاعات بیش‌تر و قوانین:
🔗
bfrd.link/WCW
🌐
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
💻
@BetForward</div>
<div class="tg-footer">👁️ 8.23K · <a href="https://t.me/Futball180TV/90308" target="_blank">📅 23:25 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90307">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/84204a485b.mp4?token=FNiHnsJ9tejIJH450uUiGl_vn409uzHytbHYk0qgqTjyX5jIO5QqmNVT5k-nQ2VK7dedbh0skW7xB9bcu2QB73QsRJC9hnb5ZLxgMusDjMsZP3gSKnJsMdvqOnbtGyjgTuoZwZTA53sGOO3DmpATbU98Pg-tkJM4UE4EzJENJN-rg-3TDZ-wvRvYfYuGNFxwErXbStcGTVfBwGbrpvFV3WPdZrfW0AmAyiud-Ma4qpnJHMlBo-wzhuTA2GD0fHUZvEmomT6Uy6D2i2thpyPW1C5o1GSq1w64z0Dvk39CztF4_RpDe8NpnDPb01JVGTh-Ayl2sM7XtZpntjpsz-KdDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/84204a485b.mp4?token=FNiHnsJ9tejIJH450uUiGl_vn409uzHytbHYk0qgqTjyX5jIO5QqmNVT5k-nQ2VK7dedbh0skW7xB9bcu2QB73QsRJC9hnb5ZLxgMusDjMsZP3gSKnJsMdvqOnbtGyjgTuoZwZTA53sGOO3DmpATbU98Pg-tkJM4UE4EzJENJN-rg-3TDZ-wvRvYfYuGNFxwErXbStcGTVfBwGbrpvFV3WPdZrfW0AmAyiud-Ma4qpnJHMlBo-wzhuTA2GD0fHUZvEmomT6Uy6D2i2thpyPW1C5o1GSq1w64z0Dvk39CztF4_RpDe8NpnDPb01JVGTh-Ayl2sM7XtZpntjpsz-KdDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">امیر قلعه‌نویی به سبک لوئیز انریکه درحال هدایت شاگردانش برای جام‌جهانی فوتبال!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.11K · <a href="https://t.me/Futball180TV/90307" target="_blank">📅 23:05 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90306">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fa7TUkEfvWd3apo-jfpcfv5fovppJLiM8nRVN8bJW5JGowgQHYCHeAP8JfP4UOWqAFGE-EZa9RB-45SOUGnbTZjI1SA0qWUwhT7VnD9SQ2JovCoc7BBV46N7nFEEVguFx0h_cFet_wh_g2Qmdv605plb6aBnJsVDJKSZH0Q7rz9OAdzuxTxnxpkrues-OwdALcR7gqmnnjEqGB849543FRvUtqsI7zQGmsYm6EUfx2_qnv0qw8au7i_h37ehUIcngLBADc6A3LloJhiPfCPtxcA_n8NG3Po_UmS3PO_TtzxZimocEw8RU8wVMskPyxuZWitCjAuMA87YwwGFi34A3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اندی رابرتسون ستاره خط‌دفاعی لیورپول با عقد قراردادی به عنوان بازیکن آزاد به تاتنهام پیوست
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.96K · <a href="https://t.me/Futball180TV/90306" target="_blank">📅 22:58 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90305">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/80080a6ded.mp4?token=hEuIBkcw_KhUmWPz7qRaLsyXfrT5OEsUdGRu54Yjr0b7rMu2x90GrPHAiIY4TFfdx5ELdsnrrXY_qtXWkOlZN7lhyDVvWPwObVY1mSy-00yMUW3LnZaKZXLYNVFB5g20XtWoTyflqSYcENLO3PuJvyYLSQPMRV1yEOmCLe1FSmkJ9xUqhkoVPG9h5OZo4mN_Kbl1BK6MX9Oxvg5o9K40w4RGc8KjKoLnBeiK-d9rMVJISpGstOf6AXbOoAHpFxR0P8BGaWL7UdnqTYjBwyNGzu0XQ8imHkABBVK_yNBgQ_P3XgS3KetgHyMPpilYdRlwqx9f0xk1hWjUtHMI2Hy3zA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/80080a6ded.mp4?token=hEuIBkcw_KhUmWPz7qRaLsyXfrT5OEsUdGRu54Yjr0b7rMu2x90GrPHAiIY4TFfdx5ELdsnrrXY_qtXWkOlZN7lhyDVvWPwObVY1mSy-00yMUW3LnZaKZXLYNVFB5g20XtWoTyflqSYcENLO3PuJvyYLSQPMRV1yEOmCLe1FSmkJ9xUqhkoVPG9h5OZo4mN_Kbl1BK6MX9Oxvg5o9K40w4RGc8KjKoLnBeiK-d9rMVJISpGstOf6AXbOoAHpFxR0P8BGaWL7UdnqTYjBwyNGzu0XQ8imHkABBVK_yNBgQ_P3XgS3KetgHyMPpilYdRlwqx9f0xk1hWjUtHMI2Hy3zA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جنگ هادی‌چوپان با رقبایش برای عکس گرفتن با آرنولد در رقابت‌های اوهایو!!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.16K · <a href="https://t.me/Futball180TV/90305" target="_blank">📅 22:40 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90304">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/35b0dae947.mp4?token=uSKvF1pAkWivot-Bq5-2hpjxtpgGnWhnn7FPgmz7-CiMxx6IzpO0Lo3qDBz0IYjmidLZHifeAXq9MHhdUF9hb3eTAIAd7iRnWsrsryWlaj78eszSYJtPAbQeAfMPWRnO5HDXvsFNuUAqz3L-oGiAVoNvrs15SpuvAkIFAOJYYrW6m_kvjdp_MkU9ZQDw0XUE1LEGGPo-RkjLWIrIimgkLVj1ZpL0Qg_kLZqgGzqVwg-ALon2zToeXuXg1GU71jpZCxE3DtqtRrZzm9tC8bJ4_LOM-yvx7jRU96D2fB426E9ZZf5J7F8BvcWtQzl4a5wQBa-4RF_Reie8-XPSN1mJuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/35b0dae947.mp4?token=uSKvF1pAkWivot-Bq5-2hpjxtpgGnWhnn7FPgmz7-CiMxx6IzpO0Lo3qDBz0IYjmidLZHifeAXq9MHhdUF9hb3eTAIAd7iRnWsrsryWlaj78eszSYJtPAbQeAfMPWRnO5HDXvsFNuUAqz3L-oGiAVoNvrs15SpuvAkIFAOJYYrW6m_kvjdp_MkU9ZQDw0XUE1LEGGPo-RkjLWIrIimgkLVj1ZpL0Qg_kLZqgGzqVwg-ALon2zToeXuXg1GU71jpZCxE3DtqtRrZzm9tC8bJ4_LOM-yvx7jRU96D2fB426E9ZZf5J7F8BvcWtQzl4a5wQBa-4RF_Reie8-XPSN1mJuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حق‌ترین جمله‌ای که درباره وضعیت فعلی میشه گفت:
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.63K · <a href="https://t.me/Futball180TV/90304" target="_blank">📅 22:15 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90303">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/05aa244672.mp4?token=S5Bs8B989P8yOojO8GbbWbghTAEu4aaZzoJD6ra8K01MTocVPRfR5GNriR_skic3uhwocElBE1EqqOYYnz3_GdGpMVz4EdUKmDlSdd-ZM8ydPrBXV4K59ZkG0f-4WGJf6QSEVpAAoTUQaNW31H9VlYQsdQ6Mtm6gwvln6S9SMhyx1zdFjwqYXV9OnQYtIhzDKp5vI6j4WiTY3TiVykxj2JesRO6qvbmD57_AIseQ9cxdpuQs4z0j7OqdSNjXqfonY2viXSdclueiwQVJxHsVp2hJkFi_qnt3IJ2vZzCd1eaIXJ8UTkYtBpMdzzMADcfdsWqDQHyDfeGxDKlSKhGHMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/05aa244672.mp4?token=S5Bs8B989P8yOojO8GbbWbghTAEu4aaZzoJD6ra8K01MTocVPRfR5GNriR_skic3uhwocElBE1EqqOYYnz3_GdGpMVz4EdUKmDlSdd-ZM8ydPrBXV4K59ZkG0f-4WGJf6QSEVpAAoTUQaNW31H9VlYQsdQ6Mtm6gwvln6S9SMhyx1zdFjwqYXV9OnQYtIhzDKp5vI6j4WiTY3TiVykxj2JesRO6qvbmD57_AIseQ9cxdpuQs4z0j7OqdSNjXqfonY2viXSdclueiwQVJxHsVp2hJkFi_qnt3IJ2vZzCd1eaIXJ8UTkYtBpMdzzMADcfdsWqDQHyDfeGxDKlSKhGHMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دنیا برای آخرین جام جهانی شما آماده نیست.
💔
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.71K · <a href="https://t.me/Futball180TV/90303" target="_blank">📅 21:50 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90302">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NthtgRDn9nWUDg6MyoVPh6chkWF7NAZ7NEvhnemShEhzp5eE-pGL7dDmiPCZZ3rvxkc89H5y-dwt7tzYHWnrSVuEwaL47BX7lIbeaPQye519qYfEf6oSjxVZ87PfdhZZ8G0a0StRSG9Wdpwf2pdQp1QjYyAStrgHTW1iAiL_uI_I1zn0cD1bWS7h6ZSAWwrcWTQoyI5DAoWsZ6ZfuGjq-Ab3QxU8BcpcUFax5BuYKHNulNugRGcptvgIVtCdIXqgmT1CCFxzjxSi7Q7hudozickn7Owk7ngAxR7iuK_gPYivvugLt9EfLBkH2pwMy3sOy9Fd-7b5EAPvxqfhVH7bxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#غیررسمی
؛ آنتونی گوردون با عقد قراردادی به ارزش ۷۰ میلیون یورو از نیوکاسل به بارسلونا پیوست
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.3K · <a href="https://t.me/Futball180TV/90302" target="_blank">📅 21:28 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90301">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b45e4bbf26.mp4?token=aJlbmzh7TI7Fi5QDcaeo4kDJFWn5YxOOD2Wmt_sOfYprhHsGsi_lJhElp_2Aeeg-V02zOzCHSw0hPw80pTaIdcVru0oVKHzQa2k7S33ppp3DbmJE0_Yl2spt24KbLTZID2AfXZ_I8obLPmAd89wL0ihuk3IA0RdpUnSNyJN2gUqEM7OdIY9tPCo_dDQFwtVK21_g87zfjlznMeGQ8f7afJixKBUS628xpDgsgloZMD24veK0Jf2_cY25Ze-IdgH-gK0FCcVTwReD3VEbSiglnAJc8f43htnM6kJOKu__tLktHs5TiKfjU3SufmwJgnM6boiVZ5bCPds9PR_R1zob_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b45e4bbf26.mp4?token=aJlbmzh7TI7Fi5QDcaeo4kDJFWn5YxOOD2Wmt_sOfYprhHsGsi_lJhElp_2Aeeg-V02zOzCHSw0hPw80pTaIdcVru0oVKHzQa2k7S33ppp3DbmJE0_Yl2spt24KbLTZID2AfXZ_I8obLPmAd89wL0ihuk3IA0RdpUnSNyJN2gUqEM7OdIY9tPCo_dDQFwtVK21_g87zfjlznMeGQ8f7afJixKBUS628xpDgsgloZMD24veK0Jf2_cY25Ze-IdgH-gK0FCcVTwReD3VEbSiglnAJc8f43htnM6kJOKu__tLktHs5TiKfjU3SufmwJgnM6boiVZ5bCPds9PR_R1zob_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چالش جنجالى و جالب مجری با محمد نوری پيشكسوت باشگاه استقلال
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.89K · <a href="https://t.me/Futball180TV/90301" target="_blank">📅 21:25 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90300">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KInlT9wEkb3vaIuEqlinV4EzZw_Hq53bRXbwjQ4-uiVjx0xxQkqplT2cvI9ULRBd0l-vxMhaoea-A0OWeL_iwFH2gZ7rCRdWk9SPZx6NLloWAp_dCOUAJyaj_keM0Lzh5q7HuFODt_Rgu5_lpapQHymSSoxptu-hHePMIaZDA2n03jiu9_9z7QD9gL5745wyaehpS_ZLgkHZDctw7kDE_T1IXbSeDjVKquHUYiW0veP__StD2Wp7lOD33S5mQtewaHkz_hT59EIRfyYGd1MkYOm3K26AKRD3goHqdK1FFGf8x7Gh6yYdu26GGKUl__BzfEbERiZXQVjOozBClsaH8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شات‌تاریخی از مراسم جدایی الکس‌پوتیاس ستاره تاریخ فوتبال زنان بارسلونا
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.1K · <a href="https://t.me/Futball180TV/90300" target="_blank">📅 21:02 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90299">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q-trhlD_zjHfP9Z1RBOA8c8q0NsYhyPezdNUpaH6e-hjIuSZej5JtJLnSZQVoYX1NTE_laNDErlBjT4-UFu5jND1Cm443lzHWM-W4mBXzRTmk1VzOPdEunz1qOsw7OTfj62Rs0CY_2qbncA0J5Obh_Rshc5F-zM5fU1vRbIRWXgxlD3bALyxVG4Chy8WZX2Yhi31CB9MtA2Gv8DdS21XD8V9nWequWrB2j7MqNPWiS_ZaSG9Cm9VNotzrZYVy622SEEGq9pnrDM15CJRvakRITh0EkXEtpWLhY-aVuUPmOI-eq6pm8OPx8bW0hROA2HP45mobtrUngDolJxbsJnKTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قهرمانان تاریخ لیگ‌کنفرانس اروپا به مناسبت فینال امشب این‌فصل از رقابت‌ها
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.31K · <a href="https://t.me/Futball180TV/90299" target="_blank">📅 20:35 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90298">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57a28e2aed.mp4?token=pVF1O8YNWNx5oGtz249NF-_wpSku1kW4dPFXp4WTYoIVkyk1sru5KktfV6bSwPwmaGx7ng8IYot8J2JHpVoxDk5e1IZcW5a1Z1w390n_p2FEI8HaKhqvQ-u7DVn3_4OTuoEXvXWtl19BiROn_alqAbrK9PEmtGD3sTjyaGeJ0rnwqDWKW9elSm1tA6Bb9u6rw5AAY0z8SfPLT02zupw1q5bChMntp4Miyf7jfwsZ2NEyP_3ihHEsnYPnkTDRfKlt4qoC9ucszt3ulz2X_WWRTH-g4qVlg9KMTyplj1CEEHlz3lvj-pGM2k6BQJ_C3dbXQYh_PR7bwJXdVunGp1slnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57a28e2aed.mp4?token=pVF1O8YNWNx5oGtz249NF-_wpSku1kW4dPFXp4WTYoIVkyk1sru5KktfV6bSwPwmaGx7ng8IYot8J2JHpVoxDk5e1IZcW5a1Z1w390n_p2FEI8HaKhqvQ-u7DVn3_4OTuoEXvXWtl19BiROn_alqAbrK9PEmtGD3sTjyaGeJ0rnwqDWKW9elSm1tA6Bb9u6rw5AAY0z8SfPLT02zupw1q5bChMntp4Miyf7jfwsZ2NEyP_3ihHEsnYPnkTDRfKlt4qoC9ucszt3ulz2X_WWRTH-g4qVlg9KMTyplj1CEEHlz3lvj-pGM2k6BQJ_C3dbXQYh_PR7bwJXdVunGp1slnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمله عجیب مجری پرسپولیس صداوسیما به سروش رفیعی: پرسپولیس باید یقه بازیکنی را بگیرد که حال نداشت بازی کند
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.13K · <a href="https://t.me/Futball180TV/90298" target="_blank">📅 20:10 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90297">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ac28b3311.mp4?token=tLIN2-KIzc7z12ZQb0uoxK9aGOuApf9JRddMMx_edPO1CBwnRx18lCbMaeswiOeRkcCppGjD7aWlEWDq_fgWXQtp2C8kLfrr2U_spJTtBLZEDls6bzJ9coQrcBBuYPeIQbbFzY5paKUaMkG8rJheZE9ntxyCeI3QZC4wMtYnmp8VsEMp_AGheKWKcdpYgVacvMnwDZW1gATl4GfeMOp582tdNr7r4-PNpA4vtOfKbqZSllCrPtoIHTZXgqN3qoDJzpAvHgBrDrpR2s6JAfENqbBR9wVMlR2CgnEqAluIj9Ganqj8D0WzRZtgDlau8Ou96gdeLYQF4Ovu0HZv2ZB3aA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ac28b3311.mp4?token=tLIN2-KIzc7z12ZQb0uoxK9aGOuApf9JRddMMx_edPO1CBwnRx18lCbMaeswiOeRkcCppGjD7aWlEWDq_fgWXQtp2C8kLfrr2U_spJTtBLZEDls6bzJ9coQrcBBuYPeIQbbFzY5paKUaMkG8rJheZE9ntxyCeI3QZC4wMtYnmp8VsEMp_AGheKWKcdpYgVacvMnwDZW1gATl4GfeMOp582tdNr7r4-PNpA4vtOfKbqZSllCrPtoIHTZXgqN3qoDJzpAvHgBrDrpR2s6JAfENqbBR9wVMlR2CgnEqAluIj9Ganqj8D0WzRZtgDlau8Ou96gdeLYQF4Ovu0HZv2ZB3aA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">استقبال شیک نمایندگان آمریکا از تیم‌ملی عربستان در بدو ورود به این کشور برای جام‌جهانی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.21K · <a href="https://t.me/Futball180TV/90297" target="_blank">📅 19:35 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90296">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e4496fe5fe.mp4?token=OCoLVxE1kFCLVhEDIonDcm5Wyurqc82uMLd1l-WGuBbcWWNVUt-zZGpSCAOJKd6MWbKHPbpvtMX2YlRZiuJ0_8USV1qxsKv9tXo1e3luXRweHOuCo9_p92nPwOodQYX5zVxA2nHk55ZhE1Rz0hGjK-Fp5mJQErGsYX42QCOUXtq17yHRxGbz6O3EpSlKpAdOfkqd-QC9BshK0O2sbm0b8Bll76w-i0DltK92n_qOtN0X89JmdrT3mGww26Yvzvte507u5mPyK6AI-RlE8OuZRW2jmSWBigDAkIZfjk9HKcfP0FtSH_8MY6YuWMdfmyE92NHpHbdhStxeimpTVCdMzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e4496fe5fe.mp4?token=OCoLVxE1kFCLVhEDIonDcm5Wyurqc82uMLd1l-WGuBbcWWNVUt-zZGpSCAOJKd6MWbKHPbpvtMX2YlRZiuJ0_8USV1qxsKv9tXo1e3luXRweHOuCo9_p92nPwOodQYX5zVxA2nHk55ZhE1Rz0hGjK-Fp5mJQErGsYX42QCOUXtq17yHRxGbz6O3EpSlKpAdOfkqd-QC9BshK0O2sbm0b8Bll76w-i0DltK92n_qOtN0X89JmdrT3mGww26Yvzvte507u5mPyK6AI-RlE8OuZRW2jmSWBigDAkIZfjk9HKcfP0FtSH_8MY6YuWMdfmyE92NHpHbdhStxeimpTVCdMzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حضور نیمار در اردوی‌تیم‌ملی برزیل با بالگرد شخصی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.12K · <a href="https://t.me/Futball180TV/90296" target="_blank">📅 19:23 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90295">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aFKqbup26FCEMHhtNHLFItxy8ExxXhmfrMcln3jTN4_4RS1Q7nDH3C2EWQNpqHgA9mYLe22lN09uf89PPIyGOouBvHYYB2fzSdqcQkzR1aY3o2baErX0t64NYBgWXHvfM6bX8ks7C5g38Zv-umLB1uSEzQcxHp2raifuG2nuPQPfkoDmDflk1IV2pB9he92PYdUwubtjAwcGsLmXnBJDT_wjq37V5-OoYD2eXsoksb0l1tKQZBFflbqttJrB1nemOfDaMLQLybXzBclPQUY0WRryoFMI1ru6hKv6EYtFLdALTsvRkVFNN6TgH0lu2Ms8lpsOdg8lH0cIIjQRpScOXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
جیکوبز خبرنگار مطرح اروپایی: چلسی برای فروش انزو فرناندز درخواست ۱۲۰ میلیون یورو از رئال‌مادرید که جدی‌ترین مشتری وی است، داشته!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.75K · <a href="https://t.me/Futball180TV/90295" target="_blank">📅 19:15 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90294">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c0fba26b8.mp4?token=vrb9jf-euJTJmMdkV-W2Icv_G5X274ea1ttQZIQVvcHVFldY9-IT3JGOHoWsHnr1T0EfL3kkTfFjBr5aCa6y631GFDHRyc2pbR5IAhloHlQ8vzb_KSQSOiPUydEFCnlV_gTnXKspEBbScjFiqKlVXtom7EahVwOA69b1NifNEP9sm3_mchE2KuSVmMK-UJQopZegTnvZOs3_YnVqlkWOKcJtqIEaylPwFpzEtqPR0H83C7e1koUAWxj4ZoUczP-zO8PCuXv15VNbHrYWk0R-WFS2fha4yFMwDCvC4UGe0k4niVMz1OhA1jHm1lX74mM_-deA7uS0TgMSSzDxULBrs1gZtWtZ8nDHuuYwIHWjXkXeEKcCIhpf6x7JPZaoy4C9JGM4uoRUVeZoMM_WG0z1L7vUxGa4gU1Fu1FM-QLLxzEonI76swZv2KLtf13TeWXc1Hq2oufS2Ls7hBCs2_XsA69KCBE02FSjJI4xjn3U3EZAtLP3Y8cerAyLKEeiK4PsNg_Fgdv-PPLIkmyO_3W_ltlohb91PCpalX7R8BBIT5WMkEmMb2iztj22sykcLUPdDMYJzlwRej0ESHmvAFr6_iNzS8JBZEvqOgYRq9BomicIA4JwRJQsJZN4R7fMBcswWaVYRUyH8NaWxtQ415UEdDHwDus5CuW3nQoW56vewYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c0fba26b8.mp4?token=vrb9jf-euJTJmMdkV-W2Icv_G5X274ea1ttQZIQVvcHVFldY9-IT3JGOHoWsHnr1T0EfL3kkTfFjBr5aCa6y631GFDHRyc2pbR5IAhloHlQ8vzb_KSQSOiPUydEFCnlV_gTnXKspEBbScjFiqKlVXtom7EahVwOA69b1NifNEP9sm3_mchE2KuSVmMK-UJQopZegTnvZOs3_YnVqlkWOKcJtqIEaylPwFpzEtqPR0H83C7e1koUAWxj4ZoUczP-zO8PCuXv15VNbHrYWk0R-WFS2fha4yFMwDCvC4UGe0k4niVMz1OhA1jHm1lX74mM_-deA7uS0TgMSSzDxULBrs1gZtWtZ8nDHuuYwIHWjXkXeEKcCIhpf6x7JPZaoy4C9JGM4uoRUVeZoMM_WG0z1L7vUxGa4gU1Fu1FM-QLLxzEonI76swZv2KLtf13TeWXc1Hq2oufS2Ls7hBCs2_XsA69KCBE02FSjJI4xjn3U3EZAtLP3Y8cerAyLKEeiK4PsNg_Fgdv-PPLIkmyO_3W_ltlohb91PCpalX7R8BBIT5WMkEmMb2iztj22sykcLUPdDMYJzlwRej0ESHmvAFr6_iNzS8JBZEvqOgYRq9BomicIA4JwRJQsJZN4R7fMBcswWaVYRUyH8NaWxtQ415UEdDHwDus5CuW3nQoW56vewYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ماجرای بازداشت نیکبخت در پارتی شبانه؛ این همه آدم معروف آن‌شب آن‌جا بودند چرا فقط چسبیدید به علی نیکبخت؟ گفتم نفرینت می‌کنم یک روز جای من زندگی کنی ببینی جنبه‌اش را داری!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.76K · <a href="https://t.me/Futball180TV/90294" target="_blank">📅 18:55 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90293">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SvgOTvvQ9xpGz60O5qNam82e68sujU4h377XekGO4iPlKPK1vfkZmiQMECJcSCM9ZWU53Ca1JeewAYiVuIsIYwRsS_rEimyUjCyX6inDWPN9pe8MAxZe5JDpCM4qbZKAYPlDFdWwLRlRhzkNRIrrED6S5YNkqyfFM5T8ziG6zWS-WA8S7BY9Pgyfjg84OilKDuAgfNv8royGUPF2k5NSj6SjtU0K15onNZiH11bgteuvNe7wwiC60VETnuQHyGDkCa5ATQWd8icGHbslhNpou1zNgtSIvnOAzsXAXSH-XXeW6_zBRelIomHvmUJw3pDmcztx0w8pRMBuYOtQY01gYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بهترین هتریک‌های تاریخ ستارگان فوتبال
😂
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.66K · <a href="https://t.me/Futball180TV/90293" target="_blank">📅 18:28 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90292">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">⭕️
تا حالا بدون واریزی روی فوتبال ها شرط بستی؟!
🎉
500 هزارتومن بونوس رایگان فقط با ثبت نام بدون هیچگونه واریزی!
💳
شارژ سریع و امن با درگاه ریالی ، تتر یا ترون فقط با یک کلیک!
⌛
پشتیبانی 24 ساعته
💖
تنها سایت مورد اعتماد ما با بونوس های کاملا واقعی و رویایی:…</div>
<div class="tg-footer">👁️ 8.29K · <a href="https://t.me/Futball180TV/90292" target="_blank">📅 18:28 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90291">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fBMN4k15SFfLweXvwG9RYaJpfHf3kmxyFLWt5cA6LlerM9ySF4SbfXHTN_78R6QiTAtWgw19zk-Uxc4m07J6XQU4OhZevCT_rmLX6567bjDw7Pl28zuAughMhDfUyvPl_1YMEg9E8fK9eVcXrxvdBaSTv43F0ppGo4FlB6XYxDI1G9Ve7TqMovzN8NfnLg4KrCWulUMbdISn5PoYKzlLrSt6WYXd1dabOmB5eKaDboG2w-73cC-HCwWsxQ-MNCOsuHZbQnGgEhWu8vz9RwW84N3pyB9gF6sWS-gdbtNpqsNuzy5j2Lijl5nIgf_CckMAYkvPKQE1Fu-UEBd7zyu39A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
تا حالا بدون واریزی روی فوتبال ها شرط بستی؟!
🎉
500 هزارتومن بونوس رایگان فقط با ثبت نام بدون هیچگونه واریزی!
💳
شارژ سریع و امن با درگاه ریالی ، تتر یا ترون فقط با یک کلیک!
⌛
پشتیبانی 24 ساعته
💖
تنها سایت مورد اعتماد ما با بونوس های کاملا واقعی و رویایی:
🌐
Winro.io
🌐
Winro.io
کانال بونوس های رایگان
g6
📱
@winro_io</div>
<div class="tg-footer">👁️ 9K · <a href="https://t.me/Futball180TV/90291" target="_blank">📅 18:28 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90290">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cs5XFl-scToXIR1p0vwnjz4hBffCfxhyPF4hh541h3-uy2xCrENigDuwhnSBlhmiuZn3PKhSXS5LoBCfSmuM3pbVM2pESSqh13vpsPygXdGPEPh63r3l_vjfhJqrqciY5PshiC--pJAH_j-c9anF-9fGrHt0vm6M_1FWa5nJ6qN-V0kEg-_9Rzw2e_M3pJP5Hm5bGc2qw_PbSpYVNvlrAq-PyxMOr-sBEgFGmM5QDhifq2RDziKT87vLTHbjgAoB7XCBMmzfi8-4AKPB0T6V3fUUi3sN5l1Wx8NrdL0bGjLjRHhfn1OgX4Z8jpQC-1zBjRD_RZiq5rgCFpKlqZNvZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تمامی قهرمانان جام‌جهانی در یک نگاه
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.41K · <a href="https://t.me/Futball180TV/90290" target="_blank">📅 18:05 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90289">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Coe5SXlJ3GBuYSYiHIlHmtS8FHeabG6JQn42kdqxBVHz8db5JstUmCVxF2CAaebbVki7w78-vEzKTLKRoBpW5X7DCBVjlcfovcOxVmP4IFBaYRfZx1TMbc25f9qViV6qElYvtE7uGqBjgddUXOtvr541DR7C-i6G7I6JtotoIRIqM87NSj337LwApTNX5uNiJLbyBlpKljAZ71y098lUWFkYpYgoV4oE5H4Jf6yGB0KT-hJsoRH0ubSsIb5V4y-sFEpGt8rwnGMLKYzYPpVdMK40yOSk2Bxpp_5chfNt51BOac0NZ3eV18bI7R-vfqz9VqKIWbhchK3jw2YvHqksIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
به گفته اکثر منابع خبری، قرارداد آنتونی گوردون با بارسلونا تا ساعاتی دیگر نهایی خواهد شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.19K · <a href="https://t.me/Futball180TV/90289" target="_blank">📅 17:36 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90288">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eXzQW_o8F2W6gqwPid1kVl_qJF6SlrfJ6gmfjJRiR-ULDRwFvMS70YbwgPF4T5FhlTSY0YlrbTf3w6MFE15KkV5Z8e-l6xnBg5HZeu3-doF1Ir0KhXHf_nPiO20gw_D3hWuEYlBEgAsRWxgVWqGDD_nxgALi4zMetfDSwacnFppD7FvIq1cHs4keIwBnDhMZuqqM0Xsi5VbsUnFE3sUHOnZU3wuXnm_q6tsML3U08gQoSSXzv3TyqezOzTxSdZcQ6FJlyqHOMgeoOCQvDNLGPKqjedD3KRO1l3bxnvd0RqxtsC3g7ZcgZBLpWLuWtXg-qRt7Pw81G-ERHVCam1FjVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقایسه میزان بازدید پست معروف جام‌جهانی با پست اخیر نیمار در صفحه شخصی‌اش
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.07K · <a href="https://t.me/Futball180TV/90288" target="_blank">📅 17:15 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90287">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hu729zj7E4x21Qjz9ZkvIK4XzNuvtPRNt6toX1q4hT4v3nJXQ8BmYt_JIw7cEeAC7wOqTuOMNEFjVPM7rPqHWfmjUP9dKqASVvQc5S9iJqAIkyOgvT9Wu0pelPdEpKrSiC_mxQNTOMFjlm-kOMT3vo-FdxwuIpsFcdtz3GIwsw9YVfKRNVpehKcdXm6DH5JvFzgmTft5YrJJJ2PyINjTY7SjZejKacRWaqkOmUDUKJGpc6BSkpGrn1CEHow27KNv7KxfAeIJ6CpScf9OBPym6eiM8dI0Qbd2ZouF6mYgn4xsF9m7P0YySXh8iUJVU51uwz3f8jBq1gqydx_m8YaXZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
جرارد رومرو: بارسلونا قصد داره قبل از جام‌جهانی قرارداد گوردون رو نهایی کنه و سپس به آرامی در طول تابستان مذاکرات با آلوارز و اتلتیکومادرید رو جلو ببره
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.29K · <a href="https://t.me/Futball180TV/90287" target="_blank">📅 16:54 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90286">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/30945cae67.mp4?token=sQmW_I_RMzPoLCGX04LpAYWfHi0RPlBCKBOSURqQfCZw7XhhlOPht1aScJLJrhZaRy4RYjSmt2zctV85H-G8opQYxf0oj-2xrRfy-MFP8ZDH1ncfKIfdidvMhYWj8LvHCOoK9YP5p94YUJScJ--tiS7nX3XxpZpq2W0kpKQa2GcXOBXeptuAeJgdF23hf0gWatQWxa13Edmtc0rjaY7ln0i74OEen4HHlL1rXVqwetStBGIAwecoHe_HkT67EZ7cB-E9VrOr5z8FV1kbEVB_QegSwL3XM-vh7bK4Fu1MEQgU82Qrblid8YYNOSRsGBr0m-HIFvBxYt3S3AEmXjs8wg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/30945cae67.mp4?token=sQmW_I_RMzPoLCGX04LpAYWfHi0RPlBCKBOSURqQfCZw7XhhlOPht1aScJLJrhZaRy4RYjSmt2zctV85H-G8opQYxf0oj-2xrRfy-MFP8ZDH1ncfKIfdidvMhYWj8LvHCOoK9YP5p94YUJScJ--tiS7nX3XxpZpq2W0kpKQa2GcXOBXeptuAeJgdF23hf0gWatQWxa13Edmtc0rjaY7ln0i74OEen4HHlL1rXVqwetStBGIAwecoHe_HkT67EZ7cB-E9VrOr5z8FV1kbEVB_QegSwL3XM-vh7bK4Fu1MEQgU82Qrblid8YYNOSRsGBr0m-HIFvBxYt3S3AEmXjs8wg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از حواشی بامزه مراسم خداحافظی باشکوه پپ با سیتیزن‌ها
😂
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.17K · <a href="https://t.me/Futball180TV/90286" target="_blank">📅 16:50 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90285">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c42b3ba26.mp4?token=HsprUocrlvDe_Ki-suB-S_FbrGMwMGNk5rPP7LPI7wdcy2ElXMBGvPLoSnyCaSNRaBjQqC9jaOxuIuh5WpHTjTCNQKH7YOfFOmAT7tAMpVxz4WpzIxCaArsCNx5ZOi8UOnE2kYf7RIi83vzDby6PAUPybazLgvq8VsHijxMbwUGBdv7p5XPkmBCgN0AwlcNllW3ED3q2MdmAQiM4AIwjVujxM5KuyIjT0KzEBOrgg_SDz-568IXXx0Yr7UPO5KzrTTZw9-I0LJdbnPxc1NqLYrZ6PoUL54r82vjX_6zYZcTS9EUA1MRB_2zYCwVG3TQGQoDNzlNEIO_HM4NYw-uQCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c42b3ba26.mp4?token=HsprUocrlvDe_Ki-suB-S_FbrGMwMGNk5rPP7LPI7wdcy2ElXMBGvPLoSnyCaSNRaBjQqC9jaOxuIuh5WpHTjTCNQKH7YOfFOmAT7tAMpVxz4WpzIxCaArsCNx5ZOi8UOnE2kYf7RIi83vzDby6PAUPybazLgvq8VsHijxMbwUGBdv7p5XPkmBCgN0AwlcNllW3ED3q2MdmAQiM4AIwjVujxM5KuyIjT0KzEBOrgg_SDz-568IXXx0Yr7UPO5KzrTTZw9-I0LJdbnPxc1NqLYrZ6PoUL54r82vjX_6zYZcTS9EUA1MRB_2zYCwVG3TQGQoDNzlNEIO_HM4NYw-uQCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آرتتا و همسرش در جشن قهرمانی آرسنال
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.04K · <a href="https://t.me/Futball180TV/90285" target="_blank">📅 16:25 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90284">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QZZUBhClMlC2Pffqsey1BSCVonztJMGScNWDPvcguZDmO3pvHDOw5E9soAcI32tJP3RR4bTzFEvMdgrjFxnkNn3lcaJssnQ6SvrC1KBGb61oVanHiC4lIsdHhCO_U2qANWhoNI0-PyY_ZtTygkGSfT6PdIzqC1MIk5qShRDIMnkhgRMlCjoom2b2OHjjtB-GMYCSEv3z0j3QMzCg-wpx30-hLAFBTfflVz2foOQ0IOvqTpEiyhaoqHEUE-y0UxNAsvY4TlX8WTjV7SqDxfibiHi2035iYLDJEXF1Th8-MfaQoz2eVVivZ1joRfMdcXt5jcrrcoMIjQ_8CWeHHVmtvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
لیست تیم‌ملی هلند برای جام‌جهانی ۲۰۲۶
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.19K · <a href="https://t.me/Futball180TV/90284" target="_blank">📅 15:42 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90283">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UDAmxhI6I1VGqJBIMfP2JcSIIdO6Gr3YlkPzT4rxvVWBIEtVi5RZ8vbIiRhp-oxvlYUr335S1BXzSGkxCEDmxc6xSH_HdUbN0vpAJq7i7ziH-pPu0Sm2DENh_ohbc-T4SrfgJY_hHH9N6Z160ugx80MC2GCS5wYReB4ScNBDhv_s1QfWoaWJRv7_Hib-67MqWF0TL1rlyIomAAmkBuYKjb0nxwVWbuxYou7Y_WcMXQpd3xTGj-QvbTvl92gMTsCXDM3Mw75c5IIaoIyVyfGUo1_w2XoCPBpm78bippvdQHGAaj_pW0GYs5023RdnJUzMDqowLwX7Wq_eCbvGi9yFfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پنج سال گذشته: کریستیانو رونالدو ۵ عنوان کسب کرده است، در حالی که لیونل مسی به طور چشمگیری ۱۳ عنوان به دست آورده است.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.59K · <a href="https://t.me/Futball180TV/90283" target="_blank">📅 15:37 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90282">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MZMVn6YWe3uDlsjKCPt1H469iSvqVsvHgWpYJS1rOt6-CtEvRWTftUVEYWvq49dbNtsnAu5sdwBpwyJyR8MhnE37pMmSCC6xaCPmHrJxX_2q3RViBaK4RBIks05r0N7HNpZ-j2DxTVydxdIL-VaK_5LkezCxv0LqMT0epYsAVvPBwHA08QJRFEq_0hs0pUXodNHyhAJSE2VVHyB3dvZJP9V9O2w3gnrlml4maY_ZP0vUxmF00umGQq2w1SVgOASR3CE4yDCv2_V9odvzDUtYinjDuQlD5DeWVA3GULK1EAEXhoignczJGvxUvbqXcUufZwMQk0xaMf6hzGF9il2GRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">180TV
🤩
🌐
دوست‌دختر جدید دوگلاس لوییس در عرض چند روز به ستاره اینستاگرام فوتبالی تبدیل شد.
👙
طرفداران نه تنها درباره رابطه عاشقانه این فوتبالیست‌، بلکه درباره عکس‌های نیمه‌برهنه این مدل ۱۹ ساله با مایو بحث می‌کنند.
1️⃣
جذاب‌ترین عکس‌های دوست‌دختر جدید این فوتبالیست در کانال ما قراردارد</div>
<div class="tg-footer">👁️ 8.28K · <a href="https://t.me/Futball180TV/90282" target="_blank">📅 15:37 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90281">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">آخرین وضعیت بازسازی ورزشگاه آزادی؛ 3.2 هزار میلیارد تومان دیگر بودجه نیاز است
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.49K · <a href="https://t.me/Futball180TV/90281" target="_blank">📅 15:35 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90280">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bbe3da6710.mp4?token=PyY4CFc5hOP5Jm2klbwah4LaQnsctRsXZNi5qAvB-QyjgFhcPx1FUFJWUWwq-FZ47CYViU_1U3vz9PxZqxR3JGsSdcjcTOM8u-FsyP20slkobce4b6R3RGuzJHP1ysSQjXPTW1PWnG1qJBCvOzqLbZ6jlUsB5QdW4zbZYDiX5xesbJwO3madtPj7AgN5wVPLWWYoN98flyTwX6OW5ejd9T5rYwOp4tpV4htgunCggjZ7OWEYN0DMNbTSvuGzp3-BG7QTMtce_EyFC8Gpuz1-5v1alHctItZSu1TL5yd3msOSiuoACumqk0HNvf1HuE5XinYyzsLd7JdJv8i17MKiAKZdghAV6N3RDlPEzggS7Iiw3H844wWcPuEnBKgIStn27tmDtFuSfGfa8ZIkYTNPrT2YIy1Qo8yPFnRnorc8xx-ruM-tooW-WGLZeV29ox8b4ybZT9dowdMTfRJRNOLjPNzV_gTZZk_ImfU-FvHq7QPOw1G0bRBN3L68h-T_shCnisYltGZRPfCZZObgmRA5YBsTQeiONmBSvxT29ii4Rws0q4v_DT2Rd66X4YCRdyRrwsxa4TElG-9sfeDt9l0VfDG4O6qMvjyZPvBiTN9HgCXWe6KSijWu9W_-6eOB8Qhzq43zoM2-h48jNtrOnjve9NHomwD1u3jn3SBLEFM4tI0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bbe3da6710.mp4?token=PyY4CFc5hOP5Jm2klbwah4LaQnsctRsXZNi5qAvB-QyjgFhcPx1FUFJWUWwq-FZ47CYViU_1U3vz9PxZqxR3JGsSdcjcTOM8u-FsyP20slkobce4b6R3RGuzJHP1ysSQjXPTW1PWnG1qJBCvOzqLbZ6jlUsB5QdW4zbZYDiX5xesbJwO3madtPj7AgN5wVPLWWYoN98flyTwX6OW5ejd9T5rYwOp4tpV4htgunCggjZ7OWEYN0DMNbTSvuGzp3-BG7QTMtce_EyFC8Gpuz1-5v1alHctItZSu1TL5yd3msOSiuoACumqk0HNvf1HuE5XinYyzsLd7JdJv8i17MKiAKZdghAV6N3RDlPEzggS7Iiw3H844wWcPuEnBKgIStn27tmDtFuSfGfa8ZIkYTNPrT2YIy1Qo8yPFnRnorc8xx-ruM-tooW-WGLZeV29ox8b4ybZT9dowdMTfRJRNOLjPNzV_gTZZk_ImfU-FvHq7QPOw1G0bRBN3L68h-T_shCnisYltGZRPfCZZObgmRA5YBsTQeiONmBSvxT29ii4Rws0q4v_DT2Rd66X4YCRdyRrwsxa4TElG-9sfeDt9l0VfDG4O6qMvjyZPvBiTN9HgCXWe6KSijWu9W_-6eOB8Qhzq43zoM2-h48jNtrOnjve9NHomwD1u3jn3SBLEFM4tI0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رمزگشایی سامان آقازمانی بازیکن سابق پرسپولیس از علت اختلاف با قدیمی‌ترهای باشگاه: جوان بودم و خوب بازی می‌کردم برای همین از من خوششان نمی‌آمد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.43K · <a href="https://t.me/Futball180TV/90280" target="_blank">📅 15:35 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90279">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c7_BJmb0ABTb-aDUQFjvvcXEoEoZzQ_28-drbG7sjEN-PJOsNKAo-CGXDpP8UOZMCmBvTkOvdK4VkBbitMCo01zLiqlPKsvkUOVx83_H9q8iNv1s_us_N_jggmg7ymlpXL6nZ69iOsHO3UqGCwPaUnPVwiY-wfIZ3nivlr1vZn0WYxW77DNkADVHUBG67upnIw1DzjXQvbG2yphqFcmtKmFoHUK5byYBRvhFEL5qt8UJx0MnvKM0K8Db4drSbRXEBOQxBMkZTg-RfY2iUOiT6IcKkgkgeyThggiixefnomOZdDHqTmzU9pDpffZmT3BLGJmjfz6-kHbpIfk56G3-Ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تیم‌های ملی که توانسته‌اند دو بار پیاپی قهرمان رقابت‌های جام‌جهانی شوند؛ تاریخ برای آرژانتین رقم خواهد خورد؟!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.49K · <a href="https://t.me/Futball180TV/90279" target="_blank">📅 15:10 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90278">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2cbec1c58c.mp4?token=tJzVN8U2puyDIy-d8yR_vs0Yd18qpj9LkHcQY9PLodlkLzQ5ti4ea4vsV31pkqkz4_ull27V6b7Rsd0cHgqiTiEbBIjnBZgfdbeCHu01An1mzdsJTCzmoaUKfF3p0IZSpz-mQXKZzb9QNnDkIcZ4f3c2HffsH1b4RtbKdAFGsy0EEV6IdhHvMh03jjlQgblvEaF-scAIIWSsNpWVJBjDcFTWPFLrKbSIqgiJKoxL49D8HBYlKwV0fxdfJ_fBqz4D6rsaf8_PK328EwZHHwV1GaFh1WUMKbUXkbbc9JHxgr_THJ1gpda_mEYhVgyquvnp1agETH4mwAi8slblQ955Mw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2cbec1c58c.mp4?token=tJzVN8U2puyDIy-d8yR_vs0Yd18qpj9LkHcQY9PLodlkLzQ5ti4ea4vsV31pkqkz4_ull27V6b7Rsd0cHgqiTiEbBIjnBZgfdbeCHu01An1mzdsJTCzmoaUKfF3p0IZSpz-mQXKZzb9QNnDkIcZ4f3c2HffsH1b4RtbKdAFGsy0EEV6IdhHvMh03jjlQgblvEaF-scAIIWSsNpWVJBjDcFTWPFLrKbSIqgiJKoxL49D8HBYlKwV0fxdfJ_fBqz4D6rsaf8_PK328EwZHHwV1GaFh1WUMKbUXkbbc9JHxgr_THJ1gpda_mEYhVgyquvnp1agETH4mwAi8slblQ955Mw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انتقاد شدید صداوسیما از دستور پزشکیان برای اتصال اینترنت بین‌الملل!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.09K · <a href="https://t.me/Futball180TV/90278" target="_blank">📅 14:45 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90277">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/083cb252a0.mp4?token=bMm5zKvi6CUrXm_3nxNs03WGAqZVzSe3rL7Yh4a1FFn9sSpescEPmB67dKyYM3bGK4tTVwQrCZ2vO_X_6mNpLjfoowK44jOLcEPpe6CWCKXOtbjIowx045yFrs8JtufZbvB4FS1ThiqUKhjDR0O-pw_WpY1wqUc6N0yAbEpI_oihxBBh-Pnc3cZXQfwusoseBukPTNfgg1Wer0DtmYFU4bRLfT2cFch6pz4wxH0oLQLEiljf9ZP2R8uJ7H5XM99sTTDFOOz-zChCkaolO7nGqGrNWxJUvT5zeb0scNv2LF9s0ylLIFT7gWRjxUILXqTuwmLetWLKHymG4K2SPUnXig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/083cb252a0.mp4?token=bMm5zKvi6CUrXm_3nxNs03WGAqZVzSe3rL7Yh4a1FFn9sSpescEPmB67dKyYM3bGK4tTVwQrCZ2vO_X_6mNpLjfoowK44jOLcEPpe6CWCKXOtbjIowx045yFrs8JtufZbvB4FS1ThiqUKhjDR0O-pw_WpY1wqUc6N0yAbEpI_oihxBBh-Pnc3cZXQfwusoseBukPTNfgg1Wer0DtmYFU4bRLfT2cFch6pz4wxH0oLQLEiljf9ZP2R8uJ7H5XM99sTTDFOOz-zChCkaolO7nGqGrNWxJUvT5zeb0scNv2LF9s0ylLIFT7gWRjxUILXqTuwmLetWLKHymG4K2SPUnXig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محمد نوری پیشکسوت فوتبال: سردار آزمون را ببخشيد. اشتباه كرده و عذرخواهى ميكنه
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.3K · <a href="https://t.me/Futball180TV/90277" target="_blank">📅 14:20 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90276">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ThkrgbjTwkYQEtBcqiAFVgbEFaWw7cUSmcXx5mkwCApxPaYIVXSvaIxHbkc7eq8FYac-hx7ylIFIyy_HhIXg7G8zWssaj8PD0UoaUpVH8aMA5tpHCViWSaScElCiYRnNcOjExQZ8xFunVJHd94M4hpxKA5r9HpDb3iCuR6LJxgBirHiOYZqRCX0-RLvqHbv72nQipQT4i1qcvFQ_wXOr9Fu-Z0rbDL5KLTeGfczElyZ2BXhNEh_RTgWcLi299ysYengs5gNZeWQc1sW3kT6UO23yXbumiim8r6cBdBj0H2yiN92I0N8d0Bi7DMXzvGSqFAvJjDE1XjEp7kBn6Ex94w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آخرین باری که باشگاه بارسلونا ۸ بازیکن در تیم‌ملی اسپانیا داشت، این کشور قهرمان جام‌جهانی شد و حالا پس از گذشت ۱۶ سال بار دیگر ممکن است تاریخ تکرار شود
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.19K · <a href="https://t.me/Futball180TV/90276" target="_blank">📅 13:55 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90275">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be02e7f18e.mp4?token=QY_2vAYOKxGmLv-qZPRSgj_nPsoNCc-SG5FNlOvwTN1FxNvs-Y2P31NUEyBx59VTUU5oCzw0r87BraHD_YJp4xs-HbzRFmVqilCEBysLZgL1gx6UDaksQTRVa6Rt67jq9fTqIDhSZl_kOhE0_JMsrQKuMgdaP_3wmwraEvZrDUsPrLiWLOLV80PZuxGHHoim7jP3szUO7B0HhreU5x54YpDPzHPQg2M_PnHCDtbtcw5W0FPbZ_JB-IcKYnAHq-mSNZDvcITZqhPP_-QQ21NFFpWl3exVGZEZ4R5cpg7AnMEJcN7OdzdqS0j9jDY8Wv3ZvbknCJ9UgHtbCzLkOtLinQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be02e7f18e.mp4?token=QY_2vAYOKxGmLv-qZPRSgj_nPsoNCc-SG5FNlOvwTN1FxNvs-Y2P31NUEyBx59VTUU5oCzw0r87BraHD_YJp4xs-HbzRFmVqilCEBysLZgL1gx6UDaksQTRVa6Rt67jq9fTqIDhSZl_kOhE0_JMsrQKuMgdaP_3wmwraEvZrDUsPrLiWLOLV80PZuxGHHoim7jP3szUO7B0HhreU5x54YpDPzHPQg2M_PnHCDtbtcw5W0FPbZ_JB-IcKYnAHq-mSNZDvcITZqhPP_-QQ21NFFpWl3exVGZEZ4R5cpg7AnMEJcN7OdzdqS0j9jDY8Wv3ZvbknCJ9UgHtbCzLkOtLinQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از عجایب فوتبال بانوان در آمریکا؛ بازیکنی باردار درحال انجام بازی🫪
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.29K · <a href="https://t.me/Futball180TV/90275" target="_blank">📅 13:36 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90274">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oMolkyy4GZIjfMPJIci9P6Q9LZ1tJiiLuknNWO4jIjL-GbXhe9OjvSD-jc9gXbE3wBWJJP-_MJJa_0FafozdAloCl79QQtpnKtRbA5VwQWPDaeeeYNV90jPQxohp-fWSFwKpC9qWliCwDWD8Fay6BEojOzNvoDCJOWDhNq4Wgf_F6lpwJqVta3P6q8bJEV7rtaVeV2GCvQx0OdWwnxLuBypzR0m2aqI_FyEofsgtSkuo-xBY0ga5oIN723ExHt6QkaMsTnbjGR404PovKm5ZCVFUOOr4ghVSMopETtc5-yrbxCdd2OLlx6iVGy8AWwhGpfmsNqWrMxlkgAi9o7e1fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
متئو مورتو:
مذاکرات بین بارسلونا و نیوکاسل برای جذب آنتونی گوردون در حال انجام است. با وجود علاقه باشگاه‌های لیگ برتری و بایرن مونیخ، گوردون اولویت خود را به بارسا داده است. نیوکاسل برای جدایی او آماده است.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.15K · <a href="https://t.me/Futball180TV/90274" target="_blank">📅 13:25 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90273">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qhfTNAdyaPS6KVnJ4nKO3fgSp0BUFcmjoXPtqrXX0G6Feo1twF5TJQz0N7a3Zfc5CwC_vMgspx1ddD7vs6_pg9iaUJY5V9VPIWLKhnowGyRiPUZh9nUV0Mqmhwj5UDgPOVTQbYDQ_ALFihfS8G-E3JoCSBtslDiJCMsnTPjENlQBniD3oYsM7sskZ4nF01Vmaru5LBpKmQBDjA8OmGsc3r6gqe1jC6jyY_0d3Td4GziohT8X7Qc4QbPnF7IsRYWR-_esico9TaUrfimCYOSKL9YJ7IMlZRTvw00r2uOhr1FiPbakzmI1qJKDpH6_VMx4XqSN89nXwbVbRr8SOTChCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بهترین گلزنان فصول اخیر لیگ‌قهرمانان اروپا
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.12K · <a href="https://t.me/Futball180TV/90273" target="_blank">📅 12:50 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90272">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">⭕️
تنها جایی که در لحظه عضویت بهت 500 هزارتومان موجودی میده اینجاس
❌
🎉
کافیه فقط عضو بشی تا #وینرو  بهت
🤩
🤩
🤩
هزارتومان جایزه بده ، نیازی هم به واریز نیست.
⌛
پشتیبانی 24 ساعته
🍆
تنها سایت مورد اعتماد ما با بونوس های کاملا واقعی و رویایی:
🌐
Winro.io
🌐
Winro.io…</div>
<div class="tg-footer">👁️ 8.87K · <a href="https://t.me/Futball180TV/90272" target="_blank">📅 12:50 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90269">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ejZt9fe6UkoXe0Kamvw7y8LJCXY4jwHTYZXiuJ_2yZP5I3IczxHObl-QKQS7OzlDnc-EgT2jVVZKjwkuOzFzvRzL1byAyNd76UV9BYJQJb0rAa4Uc5Y8rCqQYHlDwYbXoAQCMsCvMg2JXanfeCrDfpbmL7AZPXZ8lW35t_W5nt5hoyWsRBKcFvCuZGe-KArGBd9MZZoJRfSoUNNVgJ6-btYdDKVVSyKQr9wDD2GnDJRzF5o8URgpRKKu0qCUD4HShxtlSvkjlqh2rAUGT91R6GdGKJLeMnkJfWosHYm1eZzee2GYxwy-qeivX8uPeoKTEJWX50JOxl-69mX2E2WXOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
تنها جایی که در لحظه عضویت بهت 500 هزارتومان موجودی میده اینجاس
❌
🎉
کافیه فقط عضو بشی تا
#وینرو
بهت
🤩
🤩
🤩
هزارتومان جایزه بده ، نیازی هم به واریز نیست.
⌛
پشتیبانی 24 ساعته
🍆
تنها سایت مورد اعتماد ما با بونوس های کاملا واقعی و رویایی:
🌐
Winro.io
🌐
Winro.io
کانال بونوس های رایگان
r6
📱
@winro_io</div>
<div class="tg-footer">👁️ 9.21K · <a href="https://t.me/Futball180TV/90269" target="_blank">📅 12:49 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90268">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4cf55f690d.mp4?token=NEn5MAvmmw8ZMmnqdBHO8JV0EHaMIa7Ozf58WUc1d7gmXmKQRTOJF1L4yI5jswWPdbV6yhorUl4d7D2OlFo29DLmGDyVUpyZ9cLX6yskKtPT11IwGnd7Wnfjp7tNgo6YaYLApSbuSIdl7eZktjl5btlSwKIQDaO3fAzb0yAR97X3R3P0CApanRlsJObPitsRHsvn7QKkLc9x6mRq9dTqrVh8VANnQtZ3y5bQp0hXTykQbBDzdP_tk4PCtXgc0L7OQ57ol6QReFhvXmno_pfLvbmZ6GPKyWxIioLDRC0ZFAYcpIWYg10k53qJnkFgrQxSaVvuZSMihGQY56Dkgusd3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4cf55f690d.mp4?token=NEn5MAvmmw8ZMmnqdBHO8JV0EHaMIa7Ozf58WUc1d7gmXmKQRTOJF1L4yI5jswWPdbV6yhorUl4d7D2OlFo29DLmGDyVUpyZ9cLX6yskKtPT11IwGnd7Wnfjp7tNgo6YaYLApSbuSIdl7eZktjl5btlSwKIQDaO3fAzb0yAR97X3R3P0CApanRlsJObPitsRHsvn7QKkLc9x6mRq9dTqrVh8VANnQtZ3y5bQp0hXTykQbBDzdP_tk4PCtXgc0L7OQ57ol6QReFhvXmno_pfLvbmZ6GPKyWxIioLDRC0ZFAYcpIWYg10k53qJnkFgrQxSaVvuZSMihGQY56Dkgusd3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اظهارات تند نیکبخت واحدی: افشین قطبی کاره‌ای نبود. چرا در تیم ملی نتیجه نگرفت؟ قطبی ذات قشنگی نداشت
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.62K · <a href="https://t.me/Futball180TV/90268" target="_blank">📅 12:40 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90267">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/98d2b87299.mp4?token=S8QvqawS2cO6n-_SDB_yzUmn6AEPON28vKCocAlz79L1O6J-28D4wT4lpzhRzirAMd5u-BuoAJQqL8luwXfpLohKhZpVceQcr-C8oVyjb3Jac4Evwz0daYsfnJhor3okzB4r9f06cCiYkbrwEKsD_Wd1xjfPd0XrLD-lsIsl9qey_LmRa4Q32pyCnJ-wRPoVImnLK2-Yo85fJlV5ZI_YEV8FiDIaYO1dYUtWSZniz2HnR8Tz9xoAwdH_JCXvp4Nz5X0hcT9ql7xEAHPQYDWtdShvpijaKwVFdqaA1xlFYws-40sTbk0x5WTdfCUPiIwLWccdLQ9L0nOhBacsytswAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/98d2b87299.mp4?token=S8QvqawS2cO6n-_SDB_yzUmn6AEPON28vKCocAlz79L1O6J-28D4wT4lpzhRzirAMd5u-BuoAJQqL8luwXfpLohKhZpVceQcr-C8oVyjb3Jac4Evwz0daYsfnJhor3okzB4r9f06cCiYkbrwEKsD_Wd1xjfPd0XrLD-lsIsl9qey_LmRa4Q32pyCnJ-wRPoVImnLK2-Yo85fJlV5ZI_YEV8FiDIaYO1dYUtWSZniz2HnR8Tz9xoAwdH_JCXvp4Nz5X0hcT9ql7xEAHPQYDWtdShvpijaKwVFdqaA1xlFYws-40sTbk0x5WTdfCUPiIwLWccdLQ9L0nOhBacsytswAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
اسپویلِ بازی آرسنال و پی اس جی.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.76K · <a href="https://t.me/Futball180TV/90267" target="_blank">📅 12:15 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90266">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/99be172cd9.mp4?token=UFfQSCRebhDIHM7ryAHWyrRScjOoYBiU-H8dUrxIxRhsXRI4CbxVxwfBow6TFLO-J1R0a99BjPvcsq78tqrSYgUWacAKkLjDqYgHnhEeXo_TR9swR6qNBfM_DuBLpffGPCpjnMAXSJheWsRJL8K6RCTUmrNr5rbbK8SCM_eBxLAAo8GRfw_HDVj7CHulrb5j8mj_Yq5tEvYOloNpqDYqHYLzeOj3CajM2cwjbCoyaiKj-57cPvCTaoW_T7RKKXQdJzsfX1pLKmYDhWvb_y6wWRMR8XAAqqLcg671lno0cTjcBd9-yh_MeJ_ANtKEtLpIGptnbgWEi90fDRTw7snonlKw2uYICWZb94Tyxyu1V9fTXigOjmbDKFvbZ7bmTdGnvKbjcztOjrgqzxxKlWO6ICsEsidOy6O5rSQseV9YWb3cwDfF52FCnIQnyKk0DU8MP9iVvHGkRzn2sQzLN60alHcIA1PwP242My27Hj22JXjoP21fRIsP4FiEg6hA7nTojm5M_gNat2tkfHHmvCqfTpwxHfRx4MIxnLpKS8WJReNgB4GR3HVHH4lk0PwxEvUvJXyX0sLFJGBHVbB38JSEKbAAzPxpIr7PP0Wqc2UfX5EM-VaZiy8VIZvMi_IqyOfZkHO2BfY3tvYKnRItWAoGkkr6N6mohzNzPAZw02KRFHc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/99be172cd9.mp4?token=UFfQSCRebhDIHM7ryAHWyrRScjOoYBiU-H8dUrxIxRhsXRI4CbxVxwfBow6TFLO-J1R0a99BjPvcsq78tqrSYgUWacAKkLjDqYgHnhEeXo_TR9swR6qNBfM_DuBLpffGPCpjnMAXSJheWsRJL8K6RCTUmrNr5rbbK8SCM_eBxLAAo8GRfw_HDVj7CHulrb5j8mj_Yq5tEvYOloNpqDYqHYLzeOj3CajM2cwjbCoyaiKj-57cPvCTaoW_T7RKKXQdJzsfX1pLKmYDhWvb_y6wWRMR8XAAqqLcg671lno0cTjcBd9-yh_MeJ_ANtKEtLpIGptnbgWEi90fDRTw7snonlKw2uYICWZb94Tyxyu1V9fTXigOjmbDKFvbZ7bmTdGnvKbjcztOjrgqzxxKlWO6ICsEsidOy6O5rSQseV9YWb3cwDfF52FCnIQnyKk0DU8MP9iVvHGkRzn2sQzLN60alHcIA1PwP242My27Hj22JXjoP21fRIsP4FiEg6hA7nTojm5M_gNat2tkfHHmvCqfTpwxHfRx4MIxnLpKS8WJReNgB4GR3HVHH4lk0PwxEvUvJXyX0sLFJGBHVbB38JSEKbAAzPxpIr7PP0Wqc2UfX5EM-VaZiy8VIZvMi_IqyOfZkHO2BfY3tvYKnRItWAoGkkr6N6mohzNzPAZw02KRFHc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پاسخ شفاف سهراب بختیاری‌زاده سرمربی استقلال به پرسپولیسی‌ها: فاسد نیستم!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.41K · <a href="https://t.me/Futball180TV/90266" target="_blank">📅 11:50 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90265">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VNDnq0wzrNdDzTYnBlLOoMvXLbMGTsUhKckiepBlnS5Ja_tiV22vy-xtKvxN_kd3MGwu2hgSgdmCCaA4jddlmWSdQw2Kj6IuFnPwwYU8m3drYZMRiyXDdSb2cC5ntsrIhMZ4TjqXpSpsXMBiLjxBKU-qZE-Q8mXpvsy1g3jL8yv0vOHCg2WL_8DiX9QFn1KWIus1230qFc8scyJ1d3UtP-7Nnp2y9dyRY0cB7lnSMx653yu7TdrrPLZ3af6H8RlZQ7FLSMSh64IIQ29GHvydhF-dFM5WwP9SIGhwQKJCZNkd1GB18UetuColLSw51QXX_mq1QHSWPrSUX5xaQpkAdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
به گزارش رومانو، باشگاه بارسلونا بدنبال عقد قرارداد با آنتونی گوردون ستاره نیوکاسل است
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.41K · <a href="https://t.me/Futball180TV/90265" target="_blank">📅 11:25 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90264">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/426e74bc07.mp4?token=ot9F94mn8WicqtB02S7skhFNy_1cpUJnroCxlM6iW7gwPkklPS6GpjxAcF9jTfOMHkHZxQfB7MMCPu7bS2HN4yMNtOe55djHS3oDWhtaAuqrJ1241vxiMzNC5B93qw6hH-guhubXMI8I9Ak5NAUao0bVPohJ9vZr9oNgfM6_56BbH6nKCQ73r1BkgATK3uV_g2rJrn4hrxF8yZqer6NRIG836ITPqMed5rBdC6AbUUjvpabEpJUYMQerjNOkNX4tOtq0C99XkzFbyDhFih-jgtgB9dUmu6qqTSP4hJDVdLRzFVtkroDiMm6XQJP6hkTv4x5tWBGsrVcpNU3l_djtMCKfiM6Mj_s2MuLSH3mNebvIFtOI9Pm4gQiQE8SS6-rTtYTLUsfppu1Jg7dFnrFW-bQblD1jHQ9WbReeNSu94rH5XWdZPGvPPdGXJyQNxC8bkhNvImMKQw4RvT6DKoR9Y9ho0vXqdQOX4pohFGCWNA4R40IxKJ89OHYCHIgNoqjUS-Hox6JB9xfBSWYQtRkmOblk06oQvYGlhd14gL5Swat7_3bq6gPyGgO14G0G__WHyglr2CpCballuGABXpy3SH4tD7QEjKrW_ZIB7UKi4oqGgxNRWxLu0FkePS4HJYxj7Nlou2UqdrAV0E4Q1N9-VGqRibjrlYAT82inT-IuEwU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/426e74bc07.mp4?token=ot9F94mn8WicqtB02S7skhFNy_1cpUJnroCxlM6iW7gwPkklPS6GpjxAcF9jTfOMHkHZxQfB7MMCPu7bS2HN4yMNtOe55djHS3oDWhtaAuqrJ1241vxiMzNC5B93qw6hH-guhubXMI8I9Ak5NAUao0bVPohJ9vZr9oNgfM6_56BbH6nKCQ73r1BkgATK3uV_g2rJrn4hrxF8yZqer6NRIG836ITPqMed5rBdC6AbUUjvpabEpJUYMQerjNOkNX4tOtq0C99XkzFbyDhFih-jgtgB9dUmu6qqTSP4hJDVdLRzFVtkroDiMm6XQJP6hkTv4x5tWBGsrVcpNU3l_djtMCKfiM6Mj_s2MuLSH3mNebvIFtOI9Pm4gQiQE8SS6-rTtYTLUsfppu1Jg7dFnrFW-bQblD1jHQ9WbReeNSu94rH5XWdZPGvPPdGXJyQNxC8bkhNvImMKQw4RvT6DKoR9Y9ho0vXqdQOX4pohFGCWNA4R40IxKJ89OHYCHIgNoqjUS-Hox6JB9xfBSWYQtRkmOblk06oQvYGlhd14gL5Swat7_3bq6gPyGgO14G0G__WHyglr2CpCballuGABXpy3SH4tD7QEjKrW_ZIB7UKi4oqGgxNRWxLu0FkePS4HJYxj7Nlou2UqdrAV0E4Q1N9-VGqRibjrlYAT82inT-IuEwU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیو وایرال شده از اظهارات عجیب شیدا یوسفی بازیگر گمنام سینمای خانگی: در کارخانه پدرم، روی شمش‌های طلا راه می‌رفتم!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.38K · <a href="https://t.me/Futball180TV/90264" target="_blank">📅 11:00 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90263">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6b5959b18a.mp4?token=TnnGmaomh6xwaF2-tlro75FTLfmmBpHOBcuTx-cwjfRFr9n2fSpe6c4TFhwKjWZEiQP4YVzEpZvFvzfQp324cE9zc30eneuYr95nvwD32DbeB5az6RcEnn7EYvt8fIRjeD2QGAIca3QvGtUIldoTUFbsBQp-ySJ2SXtKv1iUiX0k5j8zlbT6gTx1M-uTUjqOTw6OVMINb7zkaq_e478PK7vRLJ999EZtiEaCmlaQSJQ95GWlBHckaLPuHPHlezo9gfC35YpkIkhPKLNGRbR95tO084tXKJ4n7-dHb6V70GHSfugbRVKiCGgc7kEE1a-uCcYG7UchX9dRNcAaGe3a1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6b5959b18a.mp4?token=TnnGmaomh6xwaF2-tlro75FTLfmmBpHOBcuTx-cwjfRFr9n2fSpe6c4TFhwKjWZEiQP4YVzEpZvFvzfQp324cE9zc30eneuYr95nvwD32DbeB5az6RcEnn7EYvt8fIRjeD2QGAIca3QvGtUIldoTUFbsBQp-ySJ2SXtKv1iUiX0k5j8zlbT6gTx1M-uTUjqOTw6OVMINb7zkaq_e478PK7vRLJ999EZtiEaCmlaQSJQ95GWlBHckaLPuHPHlezo9gfC35YpkIkhPKLNGRbR95tO084tXKJ4n7-dHb6V70GHSfugbRVKiCGgc7kEE1a-uCcYG7UchX9dRNcAaGe3a1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وقتی صحبت از مهارت و دقت میشه
🔥
🔥
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.37K · <a href="https://t.me/Futball180TV/90263" target="_blank">📅 10:35 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90262">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e_4MZGvzRdOEXN-zBAcgzuL39VgkQIOPEdVV7WQv_MIeP6no7R69N8AQeygLJdZuxFcejHNBnOrY7DH5j2kReMGsgoCc-t4bZV8CdWJWmuRmM7fhDor9uQYksjxi-wxpG1En8MwqaOnn6feyvTIDdMttwaramuSKVq5RCVbfdwFw_5o5KslyX9SpL9W_EQy0l7ZhAPRfv-lFzl1rpGyidFSQ65vC7ot6PtHu35tQTPHpB4h4lcMKtfb5oRTky0rwGWGZkOM6URUGccoeAp5YUuL-Ik9qykDt4bcGlQhOGFV3LkQjbTcYwrI6-7G4ocuhrntLMzpx27xmFHueUR7lGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در ترکیب اصلی رئال‌مادرید در فصل گذشته هیچ بازیکنی از اسپانیا فیکس نبود و بنظر عدم حضور بازیکنی از این تیم در تیم‌ملی اسپانیا برخلاف بارسلونا طبیعی است
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.5K · <a href="https://t.me/Futball180TV/90262" target="_blank">📅 10:10 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90261">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8d64b58d74.mp4?token=AaOnsacdT1kK1OSH-dC2q0eFfoIa6INHWl20j6SQH8NsUTEnWNAdeww4c0na_LPAH3XbNAMRq3FcUMCKlIrXRB_eYgfjl3NVEKYC2XQNoYhqSIbbGE7PSwM4tv4_77N1_7WaCvDQeiWqsj4oF-OswmtHT7zLdFrEKHXlNjQQHwtTT8L5tksUw4KWU4iLS-crITO25mg4n6JR3B4zfLzH9HqTEa8xm6arUMn6npFxxUC7PYo15fsyJe9iCI9w3kKlsBrXGXEBD3OYRNb5qSMW78vrXuPoQ5yKgzW5JbN3lXx41FpdknBHOQlFcutiJeisojFyHFa7_ar71pNwWmtFhIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8d64b58d74.mp4?token=AaOnsacdT1kK1OSH-dC2q0eFfoIa6INHWl20j6SQH8NsUTEnWNAdeww4c0na_LPAH3XbNAMRq3FcUMCKlIrXRB_eYgfjl3NVEKYC2XQNoYhqSIbbGE7PSwM4tv4_77N1_7WaCvDQeiWqsj4oF-OswmtHT7zLdFrEKHXlNjQQHwtTT8L5tksUw4KWU4iLS-crITO25mg4n6JR3B4zfLzH9HqTEa8xm6arUMn6npFxxUC7PYo15fsyJe9iCI9w3kKlsBrXGXEBD3OYRNb5qSMW78vrXuPoQ5yKgzW5JbN3lXx41FpdknBHOQlFcutiJeisojFyHFa7_ar71pNwWmtFhIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بهترین گل‌های فعلی در سال ۲۰۲۶ فوتبال
🔥
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.44K · <a href="https://t.me/Futball180TV/90261" target="_blank">📅 09:45 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90260">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/26b4bc8543.mp4?token=AxJrZmwDBeOwdD0nTzrySc1A3ZQ-E8QC56SOIunsuxFj86znqgf_6_WE4EcycoTdJl4DhqwkH29kPOXnWe9Ldrk7CpMRX0WaS1wurQUeY-9DlY_MR0aoXz7r3_TY_WRKjaFjQHgCLqQQ1DVK_1ONwyk6muz31eGnlTdd4NCs-0pwbkAuuPZS9XpCTKHtwbiWlQa74Qe4tQYXtxHbU-ZBezg2vRy-5JcURF8Hb5BMWuBaZtRRBi2jcyWJgEaazPgP7luF-bLQWwA7vhzcvAcvP1VUTfUaigaMhsP-QrczxRXXzfD0xwgi5WPY9Mr_NK3lz22J7k1drYhY94HafLpRQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/26b4bc8543.mp4?token=AxJrZmwDBeOwdD0nTzrySc1A3ZQ-E8QC56SOIunsuxFj86znqgf_6_WE4EcycoTdJl4DhqwkH29kPOXnWe9Ldrk7CpMRX0WaS1wurQUeY-9DlY_MR0aoXz7r3_TY_WRKjaFjQHgCLqQQ1DVK_1ONwyk6muz31eGnlTdd4NCs-0pwbkAuuPZS9XpCTKHtwbiWlQa74Qe4tQYXtxHbU-ZBezg2vRy-5JcURF8Hb5BMWuBaZtRRBi2jcyWJgEaazPgP7luF-bLQWwA7vhzcvAcvP1VUTfUaigaMhsP-QrczxRXXzfD0xwgi5WPY9Mr_NK3lz22J7k1drYhY94HafLpRQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وحید قلیچ برا خودش عالمی داره
😂
😂
😐
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.45K · <a href="https://t.me/Futball180TV/90260" target="_blank">📅 09:20 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90259">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c4b0e0df75.mp4?token=cPNMi4rsrxnurOxGj7jX2ZD2ypIHrBFS7wo_7NX1re5Q73igJTi_5T_NMrR55BjujfbQxs4CWGpbCk2AhmeAcUVG-7gIKUfSdeDT9EVjBiPwfAa2RGEUnvv4VsEOo4vsX9JS9NedC867BsoIlwNavSWKgWXtTA-xGiiA_cjbThWb_rJuLGIZstTKxHtLsAq7fxIJq6MyG7yauqFofsK8EyKHONWwlcdkKyN4Qcsf3tZQTuQnzxwZLA6bkflloWenLcJnnDm3raLxTmUqlkZsyaT4JgKm3VFpkLWCcI-DsLnKREh64Pd0xm75KXismTKTDJkFm5iyiaiZJ1bXh3MR2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c4b0e0df75.mp4?token=cPNMi4rsrxnurOxGj7jX2ZD2ypIHrBFS7wo_7NX1re5Q73igJTi_5T_NMrR55BjujfbQxs4CWGpbCk2AhmeAcUVG-7gIKUfSdeDT9EVjBiPwfAa2RGEUnvv4VsEOo4vsX9JS9NedC867BsoIlwNavSWKgWXtTA-xGiiA_cjbThWb_rJuLGIZstTKxHtLsAq7fxIJq6MyG7yauqFofsK8EyKHONWwlcdkKyN4Qcsf3tZQTuQnzxwZLA6bkflloWenLcJnnDm3raLxTmUqlkZsyaT4JgKm3VFpkLWCcI-DsLnKREh64Pd0xm75KXismTKTDJkFm5iyiaiZJ1bXh3MR2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
همسر ناصر حجازی: به او یک میلیون تومان پیشنهاد دادند تا گل بخورد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/Futball180TV/90259" target="_blank">📅 08:55 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90258">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">روایت قرارداد نجومی فرزاد آشوبی با راه‌آهن در ایام مالکیت بابک زنجانی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/Futball180TV/90258" target="_blank">📅 08:32 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90257">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">Soren-VPN.apk</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/Futball180TV/90257" target="_blank">📅 01:45 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90256">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Soren-VPN.apk</div>
  <div class="tg-doc-extra">62.2 MB</div>
</div>
<a href="https://t.me/Futball180TV/90256" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔵
فیلترشکن سورن (اندروید)
• نسخه 2.1
برای اینترنت ملی و بین‌الملل، عملکرد خوبی داره.
وصل نشد، مجدداً برای اتصال تلاش کنید.</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/90256" target="_blank">📅 01:45 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90255">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n214y2KYZr2TNFANOU_GHG4rLEuUX6TRnhJAt0OcbFppqbb5bZKHYhCJWsHnKvVtxLxV3wWVudt7XfyA16bonXgBVLtgMbhJZO7FLEoDL2xmP6F1r8tLjP_i21br954n2QT96NWDaVvZNV3EHF_N1o1352P5gG2B5TcJkbX1tPwRjmB7BzIdh1SENr67QgG0OZchnOvZPtNIRrj5B8QXHlDliXnZDlfPO7Bx7fmWeOAEoUczL4Ci1lpfYlIzwrCtj4VShpMrrvuXrb1wptd4v5VG-gRq34sQnwsbz-4h8bFY9ljiBYN_latH3hAUMWPxB3_1qoguaZMGDODOeANfqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">میکل آرتتا بهترین سرمربی فصل لیگ‌برتر شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/Futball180TV/90255" target="_blank">📅 00:56 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90254">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🔥
برترین گل‌های این فصل سوبوسلای در لیورپول
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/Futball180TV/90254" target="_blank">📅 00:54 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90253">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SZRD4ItFbwrSK4ZMdSjUkas07RqT2dOGzu_wF3e3R3fPcYoHJ53BwIIB8RBv7KsIof6bYPVgoEdrRNsp1OUQB2jaSjYGWzfIbX9NTu-ttWX7eOXcDEEFZ79b7rh0MYEchlfo4ML2POA0u7Iz50u4sVWO57HgYUqeY0COkmtfHKHrlTxETnNGjBilVFYFJnJhMQV4vKtxswoF3GFfju4T8bjYsfm2Q4098VdG8ytQl-aVI4EoEjzVb8dkuQQeEGPTY0Uho4c8_kS0Vo66MvQ6AgVln8tgUxF5i5ax4CWFxfmngbo6hCZY2_Hhn9k4rCFJm7o6hgCJOwTrkWqG3Pkvpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الکسیا پوتیاس بعد از ۱۴ سال از بارسا جدا شد.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/90253" target="_blank">📅 21:34 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90252">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea61c87680.mp4?token=TJig3jOsFl_hhZyWDetzX-cB0L2dxKS_4gbOf_7_4DdtzTWYx6YtGUqV0iMtU_SubGlFEmXYEAjRxsLFI5p_w4niM685K0jYuA-2MbzDJWjr-sSiv8HswY0UYcvst2Rzn8Pbg_gyf9q8dFpPMJRtqMf1AFq-GwquASIWnUQWKQ9wADRbRfLlGySFHSwvWVYkzNpbrMuAj1L7K1SKzG4ig5bMohPVKTj8saUCvE35w7sQI1pkShjimBEjm5ULO35XaqRKjCcIeq27AwcQQzVLArsMckcS8ZApE6UghqLzltDIhxpFnLE-s0FLdhZr91P_8HZX-3SQ4HaR8_tOvkzqDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea61c87680.mp4?token=TJig3jOsFl_hhZyWDetzX-cB0L2dxKS_4gbOf_7_4DdtzTWYx6YtGUqV0iMtU_SubGlFEmXYEAjRxsLFI5p_w4niM685K0jYuA-2MbzDJWjr-sSiv8HswY0UYcvst2Rzn8Pbg_gyf9q8dFpPMJRtqMf1AFq-GwquASIWnUQWKQ9wADRbRfLlGySFHSwvWVYkzNpbrMuAj1L7K1SKzG4ig5bMohPVKTj8saUCvE35w7sQI1pkShjimBEjm5ULO35XaqRKjCcIeq27AwcQQzVLArsMckcS8ZApE6UghqLzltDIhxpFnLE-s0FLdhZr91P_8HZX-3SQ4HaR8_tOvkzqDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">واکنش ناصر حجازی به پیشنهاد گرین کارت؛ آمریکایی ها باید به دستبوس ما بیایند!
همسر مرحوم حجازی: وقتی بهش پیشنهاد گرین کارت آمریکا رو دادم چنان فریادهایی میزد که ستون خونه می‌لرزید!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.73K · <a href="https://t.me/Futball180TV/90252" target="_blank">📅 21:15 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90251">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">51.9 MB</div>
</div>
<a href="https://t.me/Futball180TV/90251" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 8.72K · <a href="https://t.me/Futball180TV/90251" target="_blank">📅 21:14 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90250">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/myhqImm0FhggYf4J16wfaUUKeumRpo2-CUBH22G2JOppRwuIrDd_odn30XZmy5a6_xNON0yYQzA5sAbHor5v9LBFomHLmpdNVak_N_rYAe_B5zEFgZzmgYsFLlLtE5MkpPFNlou5NmZpu7AgfzocmHBNaSjGEqjc-UV0zKEoVYaJScLxX8LYxxZOQTSsGgDB9Qd450jmsCOsbMeh7xTtNfH2KZ0bOW2emgz6XGhE7c-zp2ZwV87AoIRiAVYCxlNkntZxK46MCZwvrEXpJ8i_Cu1rv-D408lTnpOHAELp8BNbE8Ii2R2y10OcBtoCcA0VUHYiHBkrkO00vUR4iVD5hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤑
پروموی Crypto Freebet
🤑
💠
حداقل 5$ با ارز دیجیتال واریز کن (حداقل 5 بار در هفته، در 3 روز متفاوت)
💠
هر دوشنبه
💎
یه پروموکد می‌گیری برای 30% بازگشت وجه از میانگین واریزت
💠
سقف بازگشت:
💸
تا 300$ در هفته!
┅━━━━━━━━━━━━┅
🟦
آدرس وان‌ایکس‌بت:
🌐
bitly.uk/connect1xbet
🌐
bitly.uk/connect1xbet
🔓
برای ورود به سایت از فیلترشکن کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
فایل نصب اندروید 1XBET
⬇️</div>
<div class="tg-footer">👁️ 9.06K · <a href="https://t.me/Futball180TV/90250" target="_blank">📅 21:14 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90249">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/baad93a3a8.mp4?token=cE5yWmMt-CkYOt-_vLPzR4raWFv_iTPjYIQPMBQs7nF3g0ORW6S5lOGQJNB0je-4ymIhAjk3wTOaS_UXs-qXIZChGgAnuoHVHdOzE7iL3mccKSj0JJ7lZK4N8Mqv4sdFPxXbMEp42um2nIaYNCE8IgoJsr2eNHiLdXx37LukL9nDGbH98VyB2-ctg2lUqERk2-vTq7vDoYZ1pQpilals5ePqjb5d2CuhtCJyv_T_yqc1kilbVblzWP0VnkjmG_Nyrs3b_-k5wkksGPX_s8_KJQOu3H9AM--cW7hx0LfzYOXUVnwANGwWVE3ksTJ1pYBn9vITBmSanK5_IgJDycWk-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/baad93a3a8.mp4?token=cE5yWmMt-CkYOt-_vLPzR4raWFv_iTPjYIQPMBQs7nF3g0ORW6S5lOGQJNB0je-4ymIhAjk3wTOaS_UXs-qXIZChGgAnuoHVHdOzE7iL3mccKSj0JJ7lZK4N8Mqv4sdFPxXbMEp42um2nIaYNCE8IgoJsr2eNHiLdXx37LukL9nDGbH98VyB2-ctg2lUqERk2-vTq7vDoYZ1pQpilals5ePqjb5d2CuhtCJyv_T_yqc1kilbVblzWP0VnkjmG_Nyrs3b_-k5wkksGPX_s8_KJQOu3H9AM--cW7hx0LfzYOXUVnwANGwWVE3ksTJ1pYBn9vITBmSanK5_IgJDycWk-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ازبک‌ها آماده حضور در جام‌جهانی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.74K · <a href="https://t.me/Futball180TV/90249" target="_blank">📅 20:28 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90248">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ide3u4y6nSsFCI0d3hEWV7EapE2eoM9h9QW6jHW4mw0NaJsh2C0tdpGYgw6QPKCVpII_teESB4IuAlc7AakehoMKXm_4F3myz7mxypW355xvHIRZmqKCCBOxHbv9Uz3p4zCwzjdmq0dS1GECHQKWx1Z2q2-7K1kYaZ8tEvHhmpazYEhd8-zd8DB6llmnlJ2O9tAxHk8WlJfbB9m5WuTpQD6nqLltOP359p0PaqTADR5RW20ujtKjKJuC8C-HpGN5_eArmNgvVm0n_VbehSEmfJglhcrFF5LctGVTcKn53bhUPr0zyZoIJtPV5JoYoagZfZpbcRAL5DL25_r5RgprkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">با اعلام رومانو، قرارداد آنتونی رودیگر با رئال‌مادرید یکسال دیگر تمدید شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.06K · <a href="https://t.me/Futball180TV/90248" target="_blank">📅 20:03 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90247">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🚨
🔺
دسترسی به ChatGPT روی خطوط همراه اول و ایرانسل برقرار شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.03K · <a href="https://t.me/Futball180TV/90247" target="_blank">📅 19:59 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90246">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nrClzSuf1COOevSAV-tihNF43uYYsa72SJbQqhF_tAH45SaJxStc8n_tdfJtn3Wg96tumIFEgNpa0B7-FT3kHtNQakx7iyT9GQSKKYwlHgk9YsD2MYrLCz_YdhKYZIb3m4RERbcVNjerS9g53a0rCga9t4YDGpWnAWjkhk3MxZixx_TF00MmacR_pizhVdEo0RPqJ7414tAvUsw_W5W3Rdbwp2_ybRmh84mtHQa1FKvi67nt3dDIiOCRuQTmX7GChHFwzgjiSuvvwxw-UVYbyHxQsyNTuN844-HWLpI8qMTnFZokgbT7iwIe0UxHOA7CbREA8HDG_hlLOYFKdVNGLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
سیدبندی فصل‌آینده لیگ‌قهرمانان مشخص شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.16K · <a href="https://t.me/Futball180TV/90246" target="_blank">📅 19:21 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90245">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">تا ۲۴ ساعت آینده سطح دسترسی به اینترنت به حالت قبلی برخواهد گشت. درحال حاضر اتصال وای‌فای درحال بازگشت به شرایط قبل است
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.71K · <a href="https://t.me/Futball180TV/90245" target="_blank">📅 19:16 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90244">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">تا ۲۴ ساعت آینده سطح دسترسی به اینترنت به حالت قبلی برخواهد گشت. درحال حاضر اتصال وای‌فای درحال بازگشت به شرایط قبل است
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.03K · <a href="https://t.me/Futball180TV/90244" target="_blank">📅 19:09 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90243">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H_gsoghwTUItYuSDQ7URSXk-WDBcjh-lF6bZmryE9kgF39FDf8K5LNiKQQosguQgrxeIj_0p7Xb9vg91AD8qkkXD2GgUs1Evx0tC5fAtfDIwv5CTeKWxGAlK4ERwHVAjMwYnqtXKlPKI1AeCET9aD9gx_dtLS_BTFd6JHwDy3cAlEWpfzDUssfIeSs2ZoKPIm5CPYJnB7WdW3j0frfIas6k2fORhMpaU2fQXNttmSe9dq1IajUiMdbMuMnYDvonkKNj6QEHf8iasdWs0GlK-bZPixMOqmY9FON4qUWRsZq4pU0aeUIlmZkA_HYm4sI7OLsO60mGg815Ibwj78uBWdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توپ‌فصل 2026/27 سری‌آ ایتالیا
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.19K · <a href="https://t.me/Futball180TV/90243" target="_blank">📅 18:09 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90242">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XwzantDe48LrtrteQqyfwySuKR3p-apqyt3-JLt1GO_NJducUgSoBk4j8Ey5zO6DuetBm3tiGmCV0X1M67V0aZ6yhefeEAZJcijYN67UET5Am9Wkev_t5aqiKOTNJQi861pi5q8gUjeCVlhwXzKXN-Fuv56Kh1a1tB1ToPqZ-5WhuWPJE0p2z6oaPMu1rYAZeTG8CpnGHJNbtA_RQXnXhix9P69rZd-m4F1Y18JFL1mqHuVKzqfq2ZA9-9djl-hyS_69xvGSuWw8GmEKr6DOfZVVt1VAA2tHWqcem_Vmf-g7YS4xQ9_QcBFKkb8xRwVdAB5uz4UxcMbq8p41Safrpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توپ فصل 2026/27 لیگ‌برتر جزیره
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.88K · <a href="https://t.me/Futball180TV/90242" target="_blank">📅 17:53 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90241">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XCU8glBKHCB9W4Ca0jB-Y-ZMkmC-31cyMNDY1DFX_6ZldXvPPYGVbFGTaE1G1v5Neo8GEmt23t-FGSQ7bchkFkvyxLSXSLshyhUqgWg3szq4tcO9LoaDGcWD2qg7t4EUSzwz9zVyOvV1x77PUtu_aVnRr4Qwj85mWCzLOkDKc5nHa4L0MItCuyDh7Vs6JIwA86apjxcLXZpGTjegSIzUEpjZQuQfF8uaMqQszJEvMkfLezYs2T9GNgGFtlGEKXIzTPO4igXgwS9tTXo05SManeoeObXDgwjrrXG9UgdBT9gzPIy_G6gpBzhKKS1qiFwZZkLXHPX0DfVucd3AD7U1Kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
باشگاه بارسلونا برای جذب آلوارز پیشنهاد پرداخت ۱۰۰ میلیون یورو + مارک کاسادو را به اتلتیکومادرید ارائه کرده است
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.11K · <a href="https://t.me/Futball180TV/90241" target="_blank">📅 17:30 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90240">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hTl9G8_3ciMOxpyoO0-zIsANiehC-_tc0NC7WwzFaYQNHxbKyb60uhQA619HwxDsJlRuvdE_HjLvXo5AS8RbUb9qIvThbQYbGUvXuo1Kzum3iP_gceux2975VNapg7IrprjWuAxjfNoQnAsvvbRMvU5YjtISEm9fy5mcRFPe7dxNBwLsULhD5XZnfnLiogMSwaoq0qIl2Dm5eXweQVw2aL6aOPr6EePIo2V9KmMD84w2_0-_Z0oUpDfjM41-EsY9uPDOGbg0rcUiJWI0x7rEa1ldcWtYyVv3iKq7l98GgdNiejgNWsqYIH7ClcU4TQ7DPX2s2X4z7yDeD4fQxFR8OA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۱۶ ورزشگاهی که میزبان بازی‌های جام‌جهانی هستند
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.64K · <a href="https://t.me/Futball180TV/90240" target="_blank">📅 17:21 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90239">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/er4b1SlXzSWKo9PEecpVYB49te9wczvA3CCKxfJgVA6yoHy-bZQ8_N3TpsDdV0kn761wKsykzx0qQtKbVgHYvA1cUmdaygJ9L0e1zQg8qFZZt7wZHyvhZgKKtrKrkW-P8OMcWfKayK8upODxMb5uQo1Bl3XfyBABdKe81JAev2NAyOAirk7uVnT7hdiiZc7OsCUxIl9vfhhB9ewJQ4tit0c5PhL2A8vd46JeufUFtUgfCjKu4ChVjPzr59zCJLH9gRI0d6cF5z4pIEPZlztXBXALAs0lipniWZ4BQB6bVBYjwQLcSbueZ09jGu-A9Jhs8yaWDhPxozJVIycpDwx4tA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
محمدرضا عارف معاون اول پزشکیان: اینترنت بین‌الملل در دسترس قرار گرفت
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.87K · <a href="https://t.me/Futball180TV/90239" target="_blank">📅 16:58 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90238">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">مخصوص وای‌فای :
https://t.me/proxy?server=87.248.129.199&port=25565&secret=79e344818749bd7ac519130220c25d09</div>
<div class="tg-footer">👁️ 6.82K · <a href="https://t.me/Futball180TV/90238" target="_blank">📅 16:40 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90237">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tbsk6zam2so_tQm27NKpW_ShJITevoRZqD5gRJcDlWz3OSBNvQKvrAYQA_PRmtt161BUVHughWyWXk2A7FmY7uWCHG9dmqph7AK3KsWD6D5MgRuRYgK2W3dYZy-khRUHB6t3NfDYKxauAHUiHBfw8GbThzgkKtBjk1LIxtA41rCyk6tLfuXv1d5Y0VTJG3ZMEQl3s_Xt3TycnslEoOf8ceOSVXWskTQfifwXt_w85V4uk-3O7_DiTvUaPdimRDrhMIXQ2nMDuJH8P5RNTqeEmWLSO9qMR_9ZFniUZFN_ftIJD0hUD8L9k3E8WFRfR-oMFD25z9ZzL97GfcgNACSUog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
نت بلاکس: نمودار زنده نشان‌دهنده بازگشت نسبی اتصال اینترنت بین‌الملل در ایران است.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.32K · <a href="https://t.me/Futball180TV/90237" target="_blank">📅 16:34 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90236">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CR54oOfYUatqpegOun5M2VFTNqIIZF8GO2FymwtjAVC_qgupmRF_KO_y2L53eKaz7k8Jvzs_D5wpDM0ZAYQE3SSThdNPUhMPr1cKiNTJWuwAjfcWynbqwQzJx55g-1eIV3tv0oFQaF0DGZY74kScYmo644MGfwxmRGncqg2cnmPhoEICPjRZd0n-vSPtg8pX9Cz9pgspXJjbFBIslM6KTL_gZYuoMa7sflPT5aJd4LiDNFYaF1tBq7ecP6hMCdEpekxvqHerNfUl3Ls30_IHSCqlRGZ5BYDi1CgS6x5rpyZY-JiUzrd4O5y0jQfpAr_8gy4j5Wr4Cg6p7l4k6zThiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حضور خوسلو در مراسم خداحافظی کارواخال؛ این دو نفر باجناق هستن و با خواهران دوقلو ازدواج کردند
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.4K · <a href="https://t.me/Futball180TV/90236" target="_blank">📅 14:35 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90235">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Be1bcWMXUKZuDDVc4N318wFjMkfZgNj4RXyZLOvDgRWJL_tf9ND1K4TQVb4pJ8tHA24ckglrN8vOIkOprVd9aT7ougTN63fC6qpoO51bCgr3MwCjwP38YzwUQ7jrHSEllTmZgNiwr7-qGGvUOon_K1HelwSobY3D0HKM_LBV0Wy5NKIpzY5nManm9kaNBIN1Z9HSIwWZMprLXCNrERrjgPBpHSgux5rQMwO0taK-o7fe0wQTBO5G_tJ5ZJP94ga_tVxxSnLITs7cw_Sg9f6G41xI_kfcFog5PUDSmfdWOD0Pr7aXNCJcuJ6hj4ehdb3uCaJGBj81QVKZw1ACvRpncw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
این ۴ نفر، شاکی قضایی «اتصال اینترنت بین‌الملل» هستند
خبرنگار «انتخاب» دقایقی پیش کسب اطلاع کرد که ۴ نفر شاکی حقیقیِ «توقف اتصال اینترنت بین‌الملل» هستند. این ۴ نفر که گرایش سیاسی آن‌ها کاملاً مشخص است و تحت راهبری یک مقام ابقا شده‌ی دولت رییسی، دست به شکایت زده‌اند، عبارتند از
کامیار ثقفی، رضا تقی پور، رسول جلیلی و محمد حسن انتظاری
. / انتخاب
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.93K · <a href="https://t.me/Futball180TV/90235" target="_blank">📅 14:24 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90234">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🚨
وزیر علوم اعلام کرد که تکلیف امتحانات پایان ترم دانشجویان کارشناسی طی چند روز آینده مشخص و اعلام خواهد شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.54K · <a href="https://t.me/Futball180TV/90234" target="_blank">📅 13:54 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90233">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🚨
🚨
#فوری؛ سیتنا:
🔸
دستور وزیر ارتباطات برای اتصال اینترنت صادر شد؛ اتصال جهانی ایران از همین دقایق احیا می‌شود؛ اتصال کامل مردم تا 24 ساعت آینده
🔸
معاون سیاست گذاری و برنامه‌ریزی توسعه فاوا و اقتصاد دیجیتال وزارت ارتباطات، در پی دستور رییس جمهور از بازگشایی…</div>
<div class="tg-footer">👁️ 7.06K · <a href="https://t.me/Futball180TV/90233" target="_blank">📅 13:44 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90232">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OL2bF3eeq9z8zlspitnNS0NKh_fEDvAAxeks5sGXa5bWcqWfzRSqAHlbbDhIYMhWqdG3pHADBRHIW51O-6Fl0lqH721lnT-gkXxjN4l-ytWeWg1eGO8LjPwz8h48irk2foWcPnfA9Z2Wqc6oXcwDFHH05uQRX6x1WkLkx7GXhRyJDqZXA2rt_kuiduBhb74wlyoWbmS7NSzr-ObINsycgYEMnyNWYENe0TxHXjx8B9i-VTIPr3S8M2rYZXnwrN7TrG2NqMA5FRA2Mqzwj2bli3Iluaf6bZ_3AlhWCA2xQ1IsYDZ_TbSdUN6-IzH1OYCu0mtkHQtNoteCHo3npMLCpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
#فوری
؛ سیتنا:
🔸
دستور وزیر ارتباطات برای اتصال اینترنت صادر شد؛ اتصال جهانی ایران از همین دقایق احیا می‌شود؛ اتصال کامل مردم تا 24 ساعت آینده
🔸
معاون سیاست گذاری و برنامه‌ریزی توسعه فاوا و اقتصاد دیجیتال وزارت ارتباطات، در پی دستور رییس جمهور از بازگشایی تدریجی اینترنت تا دقایقی دیگر خبر داد و گفت: دسترسی کامل مردم به اینترنت تا 24 ساعت آینده میسر می شود.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.06K · <a href="https://t.me/Futball180TV/90232" target="_blank">📅 13:17 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90231">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0edb93becd.mp4?token=nZXVti_K97XQ6u28vak__x9LFq-VT9qDkF0zVp-fTtsvqLtg4CujFa2Ds7PJJ2DWLgnBPI70s4WijCDkMYrQv3Ru1Wihx39GLIC9WEbP880ylSblOFG_U5XI0MomIVlE4SAsJqiFg_5BwGuPMTpMcbTvol8uta4PCY-HjlVFf5tquVRov71g3ya4nhYxH2I6nscfcZq4ygpyhH3a4COx5Zo9M1uu1Vej-T17a5nuEmqZWZ4r19Va6O9hrxEq1XIP8BlsEwuwwj6sUBOX0eK0X5l3PZQMFz2L8HhEXQRF16Mz3jSnh8taVcueEKqf2JzayaVE5tTYSUdL-yTts6K5y5lP2_TBF4KyPzjv2CivHOjIgAC7WB03YsHyRO23gQMHpwzV2BPKSGS4w8AO8ursouz3YCdlQ0Gl4gPfv-BzNPNS1HgSZJkk74fd6JzgI55UiLT1yb84XbXO1spuTRJGeXQX7VT6yHmLxmjjpaQwitA2j5OYc0uwi8YbHGfMOc4L0LFlP_Qf_k7eWVvtCJSMgk7eZw1-zhjjUGXX53xRfdBENoFTYfUB9hJ0hhEYENme11VSDyQGOYTeouFS4_Z2YUJ_GDlwJ0qNmbIa2a6cTp04DnvNcG3TC12rK4PmK7mTqAkLR0tXgbsodGl-6vVt9ZlarD7DY0rQg09UUvt-sZs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0edb93becd.mp4?token=nZXVti_K97XQ6u28vak__x9LFq-VT9qDkF0zVp-fTtsvqLtg4CujFa2Ds7PJJ2DWLgnBPI70s4WijCDkMYrQv3Ru1Wihx39GLIC9WEbP880ylSblOFG_U5XI0MomIVlE4SAsJqiFg_5BwGuPMTpMcbTvol8uta4PCY-HjlVFf5tquVRov71g3ya4nhYxH2I6nscfcZq4ygpyhH3a4COx5Zo9M1uu1Vej-T17a5nuEmqZWZ4r19Va6O9hrxEq1XIP8BlsEwuwwj6sUBOX0eK0X5l3PZQMFz2L8HhEXQRF16Mz3jSnh8taVcueEKqf2JzayaVE5tTYSUdL-yTts6K5y5lP2_TBF4KyPzjv2CivHOjIgAC7WB03YsHyRO23gQMHpwzV2BPKSGS4w8AO8ursouz3YCdlQ0Gl4gPfv-BzNPNS1HgSZJkk74fd6JzgI55UiLT1yb84XbXO1spuTRJGeXQX7VT6yHmLxmjjpaQwitA2j5OYc0uwi8YbHGfMOc4L0LFlP_Qf_k7eWVvtCJSMgk7eZw1-zhjjUGXX53xRfdBENoFTYfUB9hJ0hhEYENme11VSDyQGOYTeouFS4_Z2YUJ_GDlwJ0qNmbIa2a6cTp04DnvNcG3TC12rK4PmK7mTqAkLR0tXgbsodGl-6vVt9ZlarD7DY0rQg09UUvt-sZs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
جزئیات درگیری علی دایی و علی کریمی در مراکش:
🔺
رضا جباری: فکر نمی کردم اینقدر علنی و شدید با هم اختلاف داشته باشند
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.93K · <a href="https://t.me/Futball180TV/90231" target="_blank">📅 12:51 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90230">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">51.9 MB</div>
</div>
<a href="https://t.me/Futball180TV/90230" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید</div>
<div class="tg-footer">👁️ 6K · <a href="https://t.me/Futball180TV/90230" target="_blank">📅 12:51 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90229">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b0TPgB9W7zQBPjTxW_LaFb8-4zGLAFBOE6V_ks2gQyM1-EVyL40_oVQ8CaQ6Ti29KxIrqbjpYLEKiTK1QHNSCVlwTaFW4i4Hl5tSoqSZpBLFoZflMOXsqdKAsABpiSl2dsmf2Eq6iiH1qeOCoZNDzrG05R9JKz8rSsrNVDzGOU3nMQi3ZDzv_8LCxfCn0e5BfcKLPXEXbcgnsM0E-CMTQiwSCN2pZ5j_jvkLO9aUgYraGAnLmRSG3Wx7M7j8iF5nKGawGeKtBAbQuyoTrs9Wo8hXJl5sUS6ewrXonftcK5JlFe16fgDtFfw1iG4HqBJYcXlNgsOWM8YEAuas6CGR9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
وان‌ ایکس بت برترین و خفن ترین سایت پیشبینی بین المللی که به کاربران  ایرانی خدمات میدهد
🔥
🎁
با افتتاح حساب در 1XBET از طریق کد هدیه
1x_1566529
تا سقف ۱۳۰ درصد به شما کاربران گرانقدر  بازپرداخت هدیه میدهد
🌐
Link:
bitly.uk/connect1xbet
🌐
Link:
bitly.uk/connect1xbet
🔑
برای ورود به سایت از کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
⬇️
اپلیکیشن وان‌ایکس بت
🔽
🔽</div>
<div class="tg-footer">👁️ 6.42K · <a href="https://t.me/Futball180TV/90229" target="_blank">📅 12:51 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90228">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1d9611d964.mp4?token=eH4DVYiKKiDTMj2dcfEkmWVVhbcM4weOFYQHjHfRvitOTrjGK4NUw63EWpll5G0OTQYPwA_86W_sOsHNx3DFUNnalR8VCrsxvdFv_q2tm6smEKARcfl4mhMpnVfSA1jfyRCbeD-UOYGkZKnliK0eeV8PTnNTSR8o3UzK3rQBz6l0EtS7TKXJcuTsqSNiZ-Zo-CzEETV6hPlZAk6IJUa2e7cnCtcEZknsz4df8f31X7_G30QPt7MFxiTB7VJePy2NE3e_KzOGeBLyL_FbRUWp3C0gxi9f96pNvRVJqQ7IKLdndRfL4DBpiQeMu0RTtNZlOxoBiZYG7_h7yVIZvWonZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1d9611d964.mp4?token=eH4DVYiKKiDTMj2dcfEkmWVVhbcM4weOFYQHjHfRvitOTrjGK4NUw63EWpll5G0OTQYPwA_86W_sOsHNx3DFUNnalR8VCrsxvdFv_q2tm6smEKARcfl4mhMpnVfSA1jfyRCbeD-UOYGkZKnliK0eeV8PTnNTSR8o3UzK3rQBz6l0EtS7TKXJcuTsqSNiZ-Zo-CzEETV6hPlZAk6IJUa2e7cnCtcEZknsz4df8f31X7_G30QPt7MFxiTB7VJePy2NE3e_KzOGeBLyL_FbRUWp3C0gxi9f96pNvRVJqQ7IKLdndRfL4DBpiQeMu0RTtNZlOxoBiZYG7_h7yVIZvWonZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ریکشن گاوی و لامین‌یامال پس از حضور در جام‌جهانی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.47K · <a href="https://t.me/Futball180TV/90228" target="_blank">📅 11:30 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90227">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🚨
آیت‌الله مجتبی خامنه‌ای: رژیم صهیونیستی مطابق گفته پدرم، ۲۵ سال آینده را نخواهد دید
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.08K · <a href="https://t.me/Futball180TV/90227" target="_blank">📅 11:18 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90226">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5d0834d346.mp4?token=D6pd4aYt9p5BpHUgSKtg0D08Zz25q1lY7OlpcDaxJxhlzPbINqdeYgUty4NLPzTCr-BUNu5bntGBAHIT5Mdgu4SWtulqWmwY9gT8DcDLAxQyXgNUcv11DwuPYsLs4IJ5twZFyGniR2Sy5lksl3ewSiLKO6h8zt2NWazFIgVuAtGp0w_MziWyiEhFgskOQjp_yQYeHPrFIHZXOMHARdowsiqXuZRiZ06cJLNq667vW-AzLC8KXs70zMfRIFdsi3dCbwaU0_OuPOzcfFWpTOYa-m8PPL4Rcim8_G1CnPti7Y2VJHiWfDLFVgdqA-PwwLkV2jgdMV3FM5QVP4qc5UgGiw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5d0834d346.mp4?token=D6pd4aYt9p5BpHUgSKtg0D08Zz25q1lY7OlpcDaxJxhlzPbINqdeYgUty4NLPzTCr-BUNu5bntGBAHIT5Mdgu4SWtulqWmwY9gT8DcDLAxQyXgNUcv11DwuPYsLs4IJ5twZFyGniR2Sy5lksl3ewSiLKO6h8zt2NWazFIgVuAtGp0w_MziWyiEhFgskOQjp_yQYeHPrFIHZXOMHARdowsiqXuZRiZ06cJLNq667vW-AzLC8KXs70zMfRIFdsi3dCbwaU0_OuPOzcfFWpTOYa-m8PPL4Rcim8_G1CnPti7Y2VJHiWfDLFVgdqA-PwwLkV2jgdMV3FM5QVP4qc5UgGiw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اینترنت بین الملل چه زمانی وصل می‌شود؟
🔘
سخنگوی دولت: امیدواریم با ابلاغ رئیس جمهور ظرف روزهای آتی اینترنت بین الملل بازگشایی شود.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.45K · <a href="https://t.me/Futball180TV/90226" target="_blank">📅 11:07 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90225">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kkmK2usE2M6Om1lQUfSWf1C1iDnWlLCaPZgkULxe-tY56RGqQ8upWnmR9wsurPAdetAT793_i89b4AhlcDs6UltKh4BLRSOUrmEXMnAZhz-YF_yODMA-vRFlktPfcI5dQrPNP3yIpFfPP_hb4AXGeoD-NhitNbytmWnwo6JTb7LXK_W3tU-lkUbvYmJt7UhTSSIdAcEPk6Azw5uu6qx-TFYuMe2cyzGnqLR8gDA1rc39Vn7b7NvbIdre35OIbGDmmM5oUzI5E3IjF0ZqSj-aMIXysBZ9VwoMlJO222ypXAXtgtgVrdIQqIztrQD4I665Pv669ZxBSwbGxcLCNlf19A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
قهرمانان دو جام‌جهانی اخیر در مرحله گروهی در گروه C قرار داشتند. برزیل مهمترین تیم گروه C در جام‌جهانی است
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.75K · <a href="https://t.me/Futball180TV/90225" target="_blank">📅 11:03 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90224">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DpjtQ7edqfqGa_kKEcl8HC2NI1vFqRTRKz5IcSiH7GZWdpv-ygEDcJ2x7Q6I5PK2fxwMWhHvBMAS64hOmPF9SppL_0RNSzhXu910Oj5njlwlI0EooPVvoXsJHE7d7n-Ed7eHintRIpgumkc4fjoA1n3UUEdRPrg5Jykpq6061WlKN-eE0OvPSNmGLgzfk2U3BDJyiYLfHPt0MMEW1AYLshZ-H_Iffjw977CNLtjbAXvl1SrJkU-MBagKkFvSS6h91emCFUHUdWgbUcJs9rydAUAcRKTPKhdcMLip-hnNOs9f0avUENZQRZE4-sja5Kj0G3YBhm58iKBBD9q245so6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
با آغاز اتصال احتمالی اینترنت بین‌الملل؛
ساعاتی است جیمیل در دسترس کاربران ایران قرار گرفت.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.3K · <a href="https://t.me/Futball180TV/90224" target="_blank">📅 10:26 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90223">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7673ee9149.mp4?token=sxhqy5Y9b4dKM6U8dmb21fiIWEOFBa8ZN7zIZ85xeXpKfvqSxbPRyfce_UYGLOiV9bY-qzQZiXTJXqksIUqXtxLLJ28DVUtX8H2Xz6udZysI3xeTayNRb-jLCc8uNzzqjEfmeUKdBO4F8AQHEdjz1HpuN7lvAz-gXvgLa5jFtFRBhV19A1tehSQm7z4Q9JLd0TqotwNTFqRYgKEzLVVxBRMJJ8YUGeuD9RiugC7Vz1Z0u7EpJoCenpxaEgHZnwbrawGQfsJe4UIT9ftWYFtpkPKlET8QXR3c0FjGXPSL5VTUEQe8DzSPmg96ZcE-Sw5E8BwOh7TahsHEf7bwThEYHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7673ee9149.mp4?token=sxhqy5Y9b4dKM6U8dmb21fiIWEOFBa8ZN7zIZ85xeXpKfvqSxbPRyfce_UYGLOiV9bY-qzQZiXTJXqksIUqXtxLLJ28DVUtX8H2Xz6udZysI3xeTayNRb-jLCc8uNzzqjEfmeUKdBO4F8AQHEdjz1HpuN7lvAz-gXvgLa5jFtFRBhV19A1tehSQm7z4Q9JLd0TqotwNTFqRYgKEzLVVxBRMJJ8YUGeuD9RiugC7Vz1Z0u7EpJoCenpxaEgHZnwbrawGQfsJe4UIT9ftWYFtpkPKlET8QXR3c0FjGXPSL5VTUEQe8DzSPmg96ZcE-Sw5E8BwOh7TahsHEf7bwThEYHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هواداران ترکیه در آستانه جام‌جهانی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.38K · <a href="https://t.me/Futball180TV/90223" target="_blank">📅 10:03 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90222">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ed589fd9b.mp4?token=Qx4sUJg43FhvmXb1MoLFOHWdxKIA8fYFXR72DvUcHbR5ObKYhVeVqRjnmHyXkKb29u5EhvP49rMGia7i6_W0JIgTzcJCF526RXjcsVMiAgmMx380QW8S1bbnESXTh2unQFuON7Q_2TlyrGY5pBLQlzMyD9ZXwhysxmt2WmlsBeZDsqpPFQNthMk2LH-5iGudTWhohgpi1dLLk-IgK9k0Fp9M0C4TpVBpDcjXf0W3d4aNqe39Iv1TwkQEwiD-C3kqI4thnTG6ThrlmBduoeZRhifCzmJKrmSo8pZzpwBTJ4pihKwa1GKvIow8Mx1gDvzgLwnZJyw6VE-Mfld7ohie3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ed589fd9b.mp4?token=Qx4sUJg43FhvmXb1MoLFOHWdxKIA8fYFXR72DvUcHbR5ObKYhVeVqRjnmHyXkKb29u5EhvP49rMGia7i6_W0JIgTzcJCF526RXjcsVMiAgmMx380QW8S1bbnESXTh2unQFuON7Q_2TlyrGY5pBLQlzMyD9ZXwhysxmt2WmlsBeZDsqpPFQNthMk2LH-5iGudTWhohgpi1dLLk-IgK9k0Fp9M0C4TpVBpDcjXf0W3d4aNqe39Iv1TwkQEwiD-C3kqI4thnTG6ThrlmBduoeZRhifCzmJKrmSo8pZzpwBTJ4pihKwa1GKvIow8Mx1gDvzgLwnZJyw6VE-Mfld7ohie3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
سیاوش اکبرپور: جرمی دوکو رو می‌شه مهار کرد!
😁
محسن مسلمان: ولی نمی‌شه؛ فکر نکنم!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.84K · <a href="https://t.me/Futball180TV/90222" target="_blank">📅 08:51 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90221">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">51.9 MB</div>
</div>
<a href="https://t.me/Futball180TV/90221" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 5.86K · <a href="https://t.me/Futball180TV/90221" target="_blank">📅 00:33 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90220">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RNMKrJaQrYbepNWCs0PBT5ABoszWY6zWuVQOlJ0R-HBje1zHGt1UMDqLAHGEx5WEHvppMeNUoSTWKll0gypDCiqNK2k6HrLWccWOW9S2LUtsGTppHZHW50D8XqmkNDJvdzHP5TawWu50Mlx3e6Ulc6OvSm4YHCN5SrbkbIlL192LwE0biLnGK8WVJf1n3kwoq_CYF2b-B59oHCa7nTc82xOn_vMvc4fbSSepfdcBCXNRayh1kyQrGkbnwXQIWQxDGbdY_BLpiOZdTFtlK0Iw3wzGVMLDep_G8MP0g3TAQf0CJiifIAwwsmMJbCV3etm1OTduYHPASKyzRdR-cFnW8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎾
با پیش‌بینی روی مسابقات افسانه‌ای Roland Garros در پروموی Grand Slam Tournaments، فری‌بت‌های تضمینی و شانس برنده شدن جوایز بزرگ رو به دست بیارین!
🏆
جوایز ویژه قرعه‌کشی:
📱
گوشی iPhone 17 Pro Max
📱
گوشی Samsung Galaxy Z Flip7
⌚️
ساعت Apple Watch Ultra 2
🎧
هدفون Samsung Galaxy Buds3 Pro
🎫
فری‌بت و امتیازهای بونوس
┅━━━━━━━━━━━━┅
🟦
آدرس وان‌ایکس‌بت:
🌐
bitly.uk/connect1xbet
🌐
bitly.uk/connect1xbet
🔓
برای ورود به سایت از فیلترشکن کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
فایل نصب اندروید 1XBET
⬇️</div>
<div class="tg-footer">👁️ 6.1K · <a href="https://t.me/Futball180TV/90220" target="_blank">📅 00:33 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90219">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/utokif54HHYevXAifMuzf96bykY7HlvYE4M8yJnpQxB8l8v9_eWA7fFtPg3UJCU2X5UP8di57vq5u214S0kKP3eCidBLmTETcd9ni6GbkQuavvs9Wav9nlwn2yP4Tywd75h2Et4fb-8jz9lRE7BJ1RLyqfUpd6aBH6R_8wKT2vEbWi-xVErsvzl-LjEyH8h1AeDaxTjTTU_mRo91Owx2WDmy6DqTbWdsC-YfNdx20qcTSjS8YkqOAB9mtjG2pJQeGZv33_8b8LhDUSCQC_4cyywFHwGVKtjpFDnb78r1sEI12-97fXryyRiu87dIMcAoGPHNQYOWFf-D_tCqDOxBmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇨🇴
لیست تیم ملی کلمبیا برای
#جام_جهانی2026
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.65K · <a href="https://t.me/Futball180TV/90219" target="_blank">📅 23:43 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90218">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nhvG-2g19TJvc1G_4Vtenfk5hwuV0OItYKdjTELYhNkAmdXvmQzEDCTfTYrOtdAclVXTby35YQTPH4LL6KZBR4jc_48yNQ8Uo0CeYe0MaDAJjclJPfN1yT4GO0KUYq-eYi47z04Eq5WWq9UhURkNnyu4FkJR2a4Hj0pV3BWJqIsqmf0L1MaElPk0QcpbQ2ASODhXsu0GyzCYrCpd0s2zBiUiJt6KJi_uqAJotRwDDTYocZ6IwqIqvJYL9sN6oeyexkCAqkqU06aTfwsCWkyX3Hi5QreUFNcqElSqQ2LHJeX9552yu2HMUN12Ywr4Ccmsnm9h8MvjlP9fNxcVbvfgDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مکس آلگری از هدایت میلان برکنار شد.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.57K · <a href="https://t.me/Futball180TV/90218" target="_blank">📅 23:10 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90217">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3602a6e5c9.mp4?token=iKO_1PocbSnNqJPEeni-zwt1pmH4iXF_x09SRYavNi1EOq-UsP7c_hk7A0GXeModMrjRvsd8jp-JZHKZ42GKC9GMfHr0QkQ3sIMjS1bvR3vScsqrMDnT-JqfytUL3LwQTeIvjjbiC086XcspmpUnHBLMyNe3arQLFi9poNmLO_1LJWZqrLhw9ZxcbtXjGpBhWJx7MLo9xmctguPEZG0BMIHZxQAeVzXJhIel_VSFnUNXgZ47kSCaAa32VVanuLWTZl8cG2AoCEfGP_DPwVH1kmz0y2CQjyEigGbK4j5JCOTq3YfciceC-BO4pkRoC8bdw71ur5mdnw14TCApatur-U279OiNM2rCYW3A_g9lyIF8EQ43kXFuMjtaKMyJT6kl18YNeZrL5nBScuzmGZK0ME9nRpVetipCSM-xNfdRsKSa1uGHUwChCaSDsoNNEkRhjIuiLD8CxvpCq9_NzfJBg3MWS83H4hIQqTnxbDlUMaZAQLn_PUlyCFGhSk06WLCwbS_Gkv0I267tSZzwVbS9kzxLFqJRhS0-XEigQkSXFhpKZbaRtOX8ePv3g_oW0AyzUWwXRztrRoQuo6enU4Ar3NQdRe-eGXWsbYujYYsgrYhYmSQidqeyT9dDDkiNsmSWYGg-_oL_7IokZpQQcSPNN3SnaTIHqo1jJpRthxSo0o4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3602a6e5c9.mp4?token=iKO_1PocbSnNqJPEeni-zwt1pmH4iXF_x09SRYavNi1EOq-UsP7c_hk7A0GXeModMrjRvsd8jp-JZHKZ42GKC9GMfHr0QkQ3sIMjS1bvR3vScsqrMDnT-JqfytUL3LwQTeIvjjbiC086XcspmpUnHBLMyNe3arQLFi9poNmLO_1LJWZqrLhw9ZxcbtXjGpBhWJx7MLo9xmctguPEZG0BMIHZxQAeVzXJhIel_VSFnUNXgZ47kSCaAa32VVanuLWTZl8cG2AoCEfGP_DPwVH1kmz0y2CQjyEigGbK4j5JCOTq3YfciceC-BO4pkRoC8bdw71ur5mdnw14TCApatur-U279OiNM2rCYW3A_g9lyIF8EQ43kXFuMjtaKMyJT6kl18YNeZrL5nBScuzmGZK0ME9nRpVetipCSM-xNfdRsKSa1uGHUwChCaSDsoNNEkRhjIuiLD8CxvpCq9_NzfJBg3MWS83H4hIQqTnxbDlUMaZAQLn_PUlyCFGhSk06WLCwbS_Gkv0I267tSZzwVbS9kzxLFqJRhS0-XEigQkSXFhpKZbaRtOX8ePv3g_oW0AyzUWwXRztrRoQuo6enU4Ar3NQdRe-eGXWsbYujYYsgrYhYmSQidqeyT9dDDkiNsmSWYGg-_oL_7IokZpQQcSPNN3SnaTIHqo1jJpRthxSo0o4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: ما ۱۳ نظامی در عملیات خشم حماسی از دست دادیم تا مطمئن شویم ایران به سلاح اتمی دست پیدا نمی‌کند.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.66K · <a href="https://t.me/Futball180TV/90217" target="_blank">📅 21:10 · 04 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
