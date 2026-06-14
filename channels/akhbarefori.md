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
<img src="https://cdn4.telesco.pe/file/NUIVp5sXc4mLUFnGkYtWYqTUH0o9d3nRD2hFLP1oWZ4FEQKW7B0vxN-UAoGh85xLLm9Brr4M2QsURcyj1pr8fkrPo98mM7rKVK-od_KhHaoWZLIGjLP_yn6L3V_gbGTK45G6vE4-mQAuwb3OGtpFbvIuHjy7kOE4zUdgjAcgqNBXK2O_1iwERdrolucPb52KqZ916QTxs5ZcKsu75rCUxS0cS081Zf-s_zStKGg6k38xKRHDc92E17Snm1FHSzSLLM7h3gPyNOZH7L4rQ-5XJVkwKK7G_Be9adoEEuBYriLd5uxbszbdZUvuvY8miYXQJqwiE-o7AaZVwXIp0ZwUPw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.55M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforii</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-24 18:06:42</div>
<hr>

<div class="tg-post" id="msg-659341">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/svn7KanoTEOA96Eie_YECNuSaF2F5Kfb-vTebPkcvtsFyhbnF8L-8uQoqvR_e8XCwOUApIrbReC4VZFQ6jLZ0CJEYnlYmBPNJQ_Fy2p8fJXKhwIZC8nBlukU6kHliviKxIPWz_w5XOLObhKxu2El6-nWQJvxNKJi3qh4RMhhTR2pt4i5QRsTRZ7RVzG0x1QtKimshCcDaU0Cxxs2HJJI-RZyI-9Ww1KxiaLGO7QtO0ss3E2WKZo48iANgadc1Z1Qde0M8VonLzc8vm58hGMS0FL8yTlmRYQjEbCSDsRGxtx28T3CbpJFdLfz9LOX1ttZoh8o-tZdHL8HsJesNlXnNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Y2z9pUUz4C4L5OQQjZI_jelD_yB79OA1U9p21va3_VGAJV01BQH2JpyrdskyWvBhFviZPucSSAq9zUfeyNfVP6shRKnPnxqQuarJ0WL7JLG1XsHDyfchTNL_uoHrbrTTdgjAMn6Mn2FEPEaOJFZv64nTSQwEKy2iO6b_CoYCN1-N0uej3Qy7cCejoU1Hwxsa5dSqO0KO7QxrrzHfEXLkrBSTE7HvmfeAop-BvbNOSN6pAha9jTGvvZBPXwlL-9AoK236sYkmXMqq2p9xISfG7RFHypw69Sd0uS1olLo9ueD7sdhPQEzOvu3HIxGtFQLgyXXReHduNL4qj_n6TYZLhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sOe5oaYGxd1id9oqDWvC09NUmL7fZd8ZEKCJ5c5Q6oPRfRDdwCjVboliezURoRm9Ec-6OhO3iFkzAPH9jYKsdzqMQrui378BiGO4oNWvcgnwVlsF3xi3DrDLsSNdbEyF_8TZDa_MzD1OTy7jt83z_KmYWl1CpUiELRC-vvkhJq3H_XLoPK3ZNQWFfM154ZJrJ7v8vyjGHDcWND3UhLzVz9EBRmk93TS-wgdkkUr_q4eyagYh7Up7NLtOd0Gq3P5GCBdxvYg1D2my6PCqdkFkWlYUg_4zQPF-SoanSeZwWMXAu6IWFCe8XiM2XvxU9FiS717HprHzcIyFfDQmquUb9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Xk3_IBtQcGyd-HgiKgKTrSGvKDef7HgeC-6EEVtbumMFzJ9cnIPJMpMx42NywFjG074X6dN3p2kBWm9fYGyrDXp9sVV6Tg1arqMbAAnoXpmIXN0Y3DbYRAt2xKHgf5wT2XMzyvdYqeh3D8ZHOwahQZurxb5BszRWm3noIL2c1rX1Wn7JrM3WE_AE4ffp7q-E6MHYmvPrGnHahqQEp-th2Gh8YHkUUS4vIzbN1kSXU9jzRjl2r4D6BFAQGAEnYC10hjVmbhgGrQ66umie3lwR8OA2mFrDVe9YMMVAJms-26FWqI1z8SH82Kb3vjfpray_RrhMClQ_0JCRmLs4JiGpOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rrTtRy6kzJj-kB2LXJziCerDYmtCsN7ZNM2Z0IhgMxq9qMZmbGlX2v2dpGZt666xCg1bHY_iuj7y5Cjr_h5k5qkiIOCVWdZDHDCbFKsrOzLlZC3ZWQMmBn-T6VCwZZPn3Ww7Xb3hhURY9M9-PFY5PPcSO9pU1OPmgZmOSpQqpNmbIDW4JaL2iHTQDqB6zBnM7CjX-gO0tond3KYEr01vy4a8VKGadu3REaNv86wjQJ3slLaBORAw5efd2mGj4GVXuuU5YiGtKif-6R2mDwapgZ1eBs0R1v9L59U3XIkTysduRmn6pDTT5f4ZH9To9x7vPR5O71an3cHE7FwnAmB0GA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eeyxzgSnVwR8MJPyX47j4Sxy5R24xiZc9Kb8ewCSuKS_9GE8B-c0Wj2JUHn4CSuOgLN39Wh4NhwXA-0XwGcxINsGNA_uFZqOh08e6CypNc76M5bSm_PSgYCh5yT72ZO2hp7acJYcPTfvAq68Xkvc5_MTVFTeFhZD_HVUxD-i4IpJGEm8eolIbDHhTK1rVtwFyowCF76SmVviBRiIIguOkhhYPuCDnpuTz403o-OWK-K-CfFA1pteJpoiD9q-2m__9ELCJ56MiM8_oRqKn4Bty0B3S1_hdgnpDvCkXLIUuPEGwEMpshbNX906NbKUuCdPlVL4TxK4CrH_iobXcfe1yA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/h2IQVFTOU_dnMDkWpHONkZUIHdCEPTjQ6bQRRkTdjoRUD4M9b5O_utAAqQWWd45VFvgodRvdZ_snqpy0T3JyqCIbSawYq20tFkq3B65o42Sg9OAqCvF5HSypjY_Ow2LqCwaTsVMtL4BdSsBdGf6lw0pS2oSV9Urkg_momBOaUDXV9oOkr3FdVCLMRx0b2GVOHA5E_v89WLxoLvjmQ3MsATi7RYHJ3QzWIq-C4SJkrMaaKMkXrYp1MkMB8FLQwNf_Zpoo4vsjj1E_HiIteKSrzl8aLyZVPSvt60JHhMgwZBdANsT6u-nWpwUXj2EsxrBBTQZ07C6EH2xAx-CshN6U5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sV5DUkYTSCzGSgzH7qiX7fSxpnqA9F-r3MXAzVkYDEZvn4-Uizct6UXi_Xsb1qT4HHl3bGgNQfkcTkU5j_OKhXdH-pNi6c-aJE3wNYDkLTCXs3j_y8pQnlBd43P61WKD46hK8BP61jC2gLhMVcyqvGyRFvKFsU8bzcZZrHCukTb0qBlpiktl5caH-ghQPPYXDCfxCT3XZoHqDn2vqcz7od52CWCegjHGdOs2CkhQLqgTaXZpjEWSjFmao77A-e2M1AqzvkW2rN437IPigVmeKFrkYzFyYDpsiQ4G4nblyDknE0Fcro-ME8w-6ekDguz3D5yfj0fxhGmadLN6DZ_67w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
همایش تخصصی «نقطه تصمیم»
🔹
گزارش تصویری از همایش اقتصادی نقطه تصمیم به میزبانی هلدینگ تبلیغاتی رسانه‌ای باران در مشهد، با حضور احمد جانجان در حال برگزاری است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 1 · <a href="https://t.me/akhbarefori/659341" target="_blank">📅 18:06 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659340">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nADj-x52yZRm7VNmRBhQndjzx8SGBZgfExClxqMsKIP20CTt-ynTnfQnbVUq6bPgYQYywwGtqpWGTngLXU-pgFZYsNNlUcY6UrWVw60o2epPF3JnCAB8SSpd_C5-lTQlfKxNc1snAJIoIoXG1013LV9jNwhhetvD06PIMJDFibZPmZb-DYfybAgUKOH-YFgQ5oXhW3-sYPDvZCjP_4uA7v-ecH2-iPwU5QdVdA48QeH0crm8dynOkVYGq2CSZe0qQGcPAhPeONSUCqb9mYH23WW4W7DMzqUY16wZ9jn89PVflldXUXH1NzWiN5qUlQ9quFvr_PuPpE1_qF0EsQsByw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
میزبانی زیر سایه ICE؛ فستیوال فوتبال یا دژ نظامی؟
🔹
طراح: کمال شرف
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 1 · <a href="https://t.me/akhbarefori/659340" target="_blank">📅 18:06 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659339">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dlvetbt8RgT_6VtOWllYATxXrTRACWJD93pmm5YXigc-lWfKLEwF-1pU0ciFnFA1EBgW3yj1CHtDrIMXMgE7AycIQyWm0H5zINmfKDV9M6GZ1CL733iZ1aptsjukYbP57QXV5LP6CKl-pfLN8pGSnZItbQVqD1crgexf9fhOktPGy_f3T-KKliij_4AJvJHDMCAb-NA1HT8FEnioXzzqdvCOPrjDghv7mIisq1JgyYQA3EBD6sQILirpTCubTnUWr3x5HT0e5Xhm9oLZrSGgqapdDPheWFjPxtyiNTyE-HqHVRFuEhqM1bwi2OwbZtlpeNxD2mTYhOhQr9tknlhGfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مهم‌تر از پایان جنگ، نظم جدید پساجنگ است، چیزی که رسانه‌های خارجی بیش از توافق درباره آن تیتر زده‌اند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 3.09K · <a href="https://t.me/akhbarefori/659339" target="_blank">📅 18:01 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659338">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">♦️
آماده‌باش ارتش صهیونیست‌ها برای حملات موشکی ایران
ارتش اسرائیل:
🔹
در پی حمله ساعتی پیش به ضاحیه بیروت، خود را برای حملات موشکی ایران آماده می‌کنیم.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/akhbarefori/659338" target="_blank">📅 17:58 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659337">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">♦️
احتمال شنیده‌شدن صدای انفجار در بندرعباس
سپاه هرمزگان:
🔹
روز دوشنبه ۲۵ خرداد، عملیات انهدام مهمات عمل‌نکرده در بندرعباس از ساعت ۸ صبح تا حوالی عصر انجام می‌شود.
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 7.13K · <a href="https://t.me/akhbarefori/659337" target="_blank">📅 17:56 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659336">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ae2908bdd.mp4?token=RXdzxyu5GYTRgGDUKWmc-LZEAhpVRKE38t_WBPjgDeUroq_iKdtXkb7uvgSqMCnPcKRTIB9gBw4nnmGMDp47C5ENs5h218sZMtCyau2DpXUYmaeMgBpB0EsBotGbmiMvdd-ba2E4jGEQvnMVibURNUQDSk2Br3UjLmHJ3uJyDHnNr3LgR7Krno0ifurF-42StXEhraozL7V_1P_G1lt-S2KxnXqIRmC0OiDMzB475SvLRbqdM_qdkzlAjkN8W1bP6hgDEVwEf--aLNjJeYMFZ4m-fYrwKVrnSpfEHeVdxDZV4cR1qeL0K-7R3xkg3V7exc-8eBvAlfq2xOkWKmv1zA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ae2908bdd.mp4?token=RXdzxyu5GYTRgGDUKWmc-LZEAhpVRKE38t_WBPjgDeUroq_iKdtXkb7uvgSqMCnPcKRTIB9gBw4nnmGMDp47C5ENs5h218sZMtCyau2DpXUYmaeMgBpB0EsBotGbmiMvdd-ba2E4jGEQvnMVibURNUQDSk2Br3UjLmHJ3uJyDHnNr3LgR7Krno0ifurF-42StXEhraozL7V_1P_G1lt-S2KxnXqIRmC0OiDMzB475SvLRbqdM_qdkzlAjkN8W1bP6hgDEVwEf--aLNjJeYMFZ4m-fYrwKVrnSpfEHeVdxDZV4cR1qeL0K-7R3xkg3V7exc-8eBvAlfq2xOkWKmv1zA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جمعِ سلاطینِ فوتبال در یک قاب!
👑
⚽️
ویدئوی جذابی از سلاطین فوتبالی که در شبکه‌های اجتماعی در حال وایرال شدنه!
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.13K · <a href="https://t.me/akhbarefori/659336" target="_blank">📅 17:55 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659335">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e8f70e9f0.mp4?token=ak8_EOkCRlrG2GymuxDCS8sZVJiMldyx6sgPueO-VzKsi-ZRQkjAPPaOFexOCasZ8Lwf4mjyl3YR8_7UgMJkTSZKB2UvizMwo8UtOxdoCJ9yggOmN0YIbgsPUCcx_WRSv9vtJy1otDs6QxJ_4ZIQUPRGaXEd7tQ9RlcqxjTvcFRoLXI4NmFhcmyjyWwkzsolCBS1CN7aO_7YcYUZIRCdNihiQxPU7P_zmLHeOp2_Oh-1XoNi4icdt2KK6rJP40EL76GKGZvNz4_u7WzWIg8SkJoqsRYYk9rfIGrI8N-aJxOaRcqsZBpy09LLupWq9fkvj3pc7XzwhNbyS94OMrmBPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e8f70e9f0.mp4?token=ak8_EOkCRlrG2GymuxDCS8sZVJiMldyx6sgPueO-VzKsi-ZRQkjAPPaOFexOCasZ8Lwf4mjyl3YR8_7UgMJkTSZKB2UvizMwo8UtOxdoCJ9yggOmN0YIbgsPUCcx_WRSv9vtJy1otDs6QxJ_4ZIQUPRGaXEd7tQ9RlcqxjTvcFRoLXI4NmFhcmyjyWwkzsolCBS1CN7aO_7YcYUZIRCdNihiQxPU7P_zmLHeOp2_Oh-1XoNi4icdt2KK6rJP40EL76GKGZvNz4_u7WzWIg8SkJoqsRYYk9rfIGrI8N-aJxOaRcqsZBpy09LLupWq9fkvj3pc7XzwhNbyS94OMrmBPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
در چند دقیقه عیارهای طلا رو یاد بگیر #دارایی_هوشمند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.15K · <a href="https://t.me/akhbarefori/659335" target="_blank">📅 17:52 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659329">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RRoVGuZAGrlfEPIovcPb2Vu9qg2IMYpCJjms1Sbo5xquGhmemXElxrygSVtjDFsZdPPygeKknw5xI_3_88Wr6VlJ6P1Qpan3na0fscqzIg2dwZvYvgb3-VZkCSf10-FH_ITiOq7WtjTt7QH3FUTaqsMwuna5iZBoAGKP--X2sYOGoTung5xbIxuVl8TEKHi7AOoI7XC87GKmxbDYPsqs-Ax1LDmMZd5yBRc1WMtxNwt1FfESOntLLWaLEBhOVYoHBdSUh0oWW7YGFN72aqL5aiz3hA6264HeUPev0jkAeUnYbL6IHwSLSh-Mc62ZfUlDeth0kM3GIGBQPsK3rgif-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tpdMsN9isUIFpZ00acTCsaornVJf3Zk0QixhJhvbAnM5s1iNLCMqt7zQV9yWM9QyxB06Ix419sAhu3JUK0ZHU3VUVZTR51xeYo7C0WwfFTwyE4YhiER9eBh4fZFJxrBnkhGNoh9ie8jGcXduBOEE3X-pJ5boS0wlEGY3lW-xPhycFYM_cfO3JQlT0rPT8wKq67JzyjfEQIlbEaAXz1Lfrymt63uC3OBMgqO-dgPy6I6pwfsMBadUU9ox8m0zmEY0L2mT9O1sg_vNAG072WqLlL7Ud-bS9fRTTZn4B4nJ5-n1ONi1Pxj2ZU5iv86NhIWBSOiFmSDv4Lz-Hqlyqctkjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kIAXieh3mrYf3_5D0a9ZVpPSyveg9htoVXoq-h0x4MJ1zawLFDjSp6VsWKzj2aL_0dIQ3TRebIev4hS1JIOa9zPMr-Ydv1VDkGVL4Ik37NPm57autQAB_VuDRZjB2OB4ZhXeVW99hCf1FpX-wMSmqrQloxH462OkqeJat-joZ4pNjOtj89Qlstdfu08hI_1uLLs0-uHytZ2QoCaGXgv-3o2lXsTcl4mk_gazfKiEyAM_yA7Uu7pPuw1XmPMNt1-TdgamWf1ydRF2Gvsc2Yydk4CE6vSvXC_R5PG0f3XRm26g8DIB6RXn1FsR4giCWneAxFr-L9UCu_gJAeoi1biO0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/f5U2vpAaWw9810qZWQLsARYfG3XfvnrhVzpQXNmq1bk34XbkHFCKy0D7aEfnQLhXrKoc0PtoSRJ3Aj4VW0dnLUFLFypR433cPU2BbZUB6pEqt4LsfOQWHP6ycVs_g1yKk2hEgz8LDsc2rzBt2aK7bFxVZWc9DjG2Zwr-ErUG2MrLycPXbpf4cv8W6YO0K1Dtca0JCUHPCJKBf4PURBIW4-LUQX6xl7prJ0UdLx2skbIzeyf2xRZ9hpkk5cv8SXhpSo4TCL_3MxY-XFhgFo7X9WbN61l-26d0u2p4fSN3TLB3ZWk3GE5UC81dM9v7BOFBHQ8ZGy12w5v7kYDSRurYfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LCD3dUE9Ohj6CPr7ObRletMXKebNnVi2h5GX7eN8kx6qKior7oG570gbdGSwLqHefpG9YV1eZ4KRHtijWVXzIIHAOwvpIaA39TdUictu6BR5dcHYwb0DZYxoQb5RFbnXHvWMT3x8HKjhonOmgIYipaa7SMET4OxsbuscKxZFoqMpY1huD_1lLJtxptnvFp0QNoH7y3JQrcw57DGRDSI8vt1EFgV7lBl__sMMUBFkaUFa5q8xhrlefGo3mGAUsssZDv2xXQPkK5HcmN5hQXHKhKnQafvqZTKXLuSzRnjdGjybzOyJ7h_EytlMhVgxyp-gqfn5_YSyypinUIUpJ7SxWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BfhfFR-u6r0TiEkn56k6HYdb98GYwlFznpUxV0L25k34F0p4O29FoVD_H_Qz5X01vUtkW0MosS69Mc4TfZBhMW6zdjhETh7bAUEHDxOXHTHjGdV7OXyIEtl2PysB_ZJd4ik1ylZC-ugIMgupJN1D5zF_QIh6q8RXb2V8EoLjwcu0Vel5FSJ9_1PwWGD8DiUVBx8XM9MaFshP5gIfg9eoUW5zm0gcuddTe1NgDCdPoe6E7WMkjgD7Ce43lrChGfIR1sq8AUPU5LPBFRSeB6lzz-tRU5s9YuRUQy8XiCIVq_cc7TkkeqD0XSMC7hH-YTjGrCBtVjqcnKlRJbtX0iX2bQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
همایش تخصصی «نقطه تصمیم»
🔹
گزارش تصویری از همایش اقتصادی نقطه تصمیم به میزبانی هلدینگ تبلیغاتی رسانه‌ای باران در مشهد، با حضور احمد جانجان در حال برگزاری است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.2K · <a href="https://t.me/akhbarefori/659329" target="_blank">📅 17:45 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659328">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
معاون وزارت کشور: دولت برنامه‌ای برای افزایش قیمت آرد و نان ندارد
🔹
وزارت خارجه لبنان از اسرائیل به شورای امنیت شکایت کرد
🔹
اوباما: آمریکا باید درس ناکارآمدی جنگ را بیاموزد؛ با بمباران به نتیجه نمی‌رسیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.2K · <a href="https://t.me/akhbarefori/659328" target="_blank">📅 17:45 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659327">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oOj5OjfhbsIUcy_oHDNVWwwV167UEHDObyWIQqd_mxvNvrSslwrkZs6_AXRUkhCn9bsSb_hXS5cD3FIu8v7GyrVxmwh7ASKXrUai1IOK28ZvAKqyULK1vetIWc08jcBd4qV9OvxSbvlAC5DnHomtDehFUblm19UC6Eb7rdnZMSf8zoshKay50w9kJRiNhlia7f91PsRsJfvkpftWUodRB6xo6OwScgdDYZ1exRpAZ9M_I85LHvBGxxNwzZhgJ2oYSlbMFGnkdUlvWWMSNNcCr_8NOR_tPqGqoj-WkDjV6GPjE5aLlLEsV67Ktqkne3nnmkqFheTQte4BeO1i8KeyVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
احتمال اخراج «تریتا پارسی» از آمریکا به خاطر جنگ ایران
🔹
دولت ترامپ تحقیقات برای لغو اقامت «تریتا پارسی»، از منتقدان شناخته‌شده جنگ با ایران، را آغاز کرده است. فعالیت‌های پارسی فراتر از یک کارشناس بوده و ممکن است بر سیاست خارجی آمریکا تأثیرگذار باشد.
🔹
پارسی، ۵۱ ساله و ساکن ۲۵ ساله آمریکا، متهم است که آگاهانه یا ناآگاهانه روایت‌های جمهوری اسلامی را در واشنگتن تقویت کرده است./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/akhbarefori/659327" target="_blank">📅 17:40 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659326">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">♦️
منبع آگاه: تیم قطری برای پیگیری مذاکرات در تهران حضور دارد
یک منبع نزدیک به تیم مذاکره‌کننده ایران:
🔹
تیم قطری در تهران حضور دارد و تهران دیدگاه‌ها و جزئیات مدنظر خود را از طریق این میانجی به طرف مقابل منتقل می‌کند؛ هنوز هیچ توافقی نهایی نشده و حتی در صورت پذیرش همه نظرات ایران نیز توافقی در زمان اعلامی ترامپ امضا نخواهد شد.
🔹
این اظهارات ساعاتی پیش از حمله اسرائیل به ضاحیه بیروت مطرح شده است./ فارس
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/akhbarefori/659326" target="_blank">📅 17:35 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659325">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f086bda5b0.mp4?token=SIFu3ruAO16ZCOpC4kStbA8jHomt7m9b8gFXuqc-l98e2FyzGqErtH2jPM1YAnQTA9chyamqdzHhdC3mgmw8i-CsURKQfTtF7dfyU_9cDgkyWVETIipyxl_xNQtdp1bH9oTLOCpYJc4Dt49XHIuP-wqbLtmE6zOb1RGgUdgpGTLadQg5oBKQ5M8N3WiAgVlUjYuPMV51HVEaQKRXbc3KLdi1q7T8RCf_MrRX6wtGygYOawDNnz3yF-5dvcnCoTvJP4KeatX2rSvTAJy_vrbQWapGcbAWV0A3deK3dPrl7llG6qcbpJXVzbe-DVOiq5Bwo-3iWVSAIlzNj40iD5utEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f086bda5b0.mp4?token=SIFu3ruAO16ZCOpC4kStbA8jHomt7m9b8gFXuqc-l98e2FyzGqErtH2jPM1YAnQTA9chyamqdzHhdC3mgmw8i-CsURKQfTtF7dfyU_9cDgkyWVETIipyxl_xNQtdp1bH9oTLOCpYJc4Dt49XHIuP-wqbLtmE6zOb1RGgUdgpGTLadQg5oBKQ5M8N3WiAgVlUjYuPMV51HVEaQKRXbc3KLdi1q7T8RCf_MrRX6wtGygYOawDNnz3yF-5dvcnCoTvJP4KeatX2rSvTAJy_vrbQWapGcbAWV0A3deK3dPrl7llG6qcbpJXVzbe-DVOiq5Bwo-3iWVSAIlzNj40iD5utEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رویداد تخصصی «نقطه تصمیم» هم‌اکنون توسط هلدینگ تبلیغاتی رسانه‌ای باران در حال برگزاری است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/akhbarefori/659325" target="_blank">📅 17:32 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659324">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
قول مجلسی؛ امسال در هیچ شهری مشکل آب نخواهیم داشت!
علیرضا عباسی، عضو کمیسیون کشاورزی و منابع آب در
#گفتگو
با خبرفوری:
🔹
امسال به لطف خدا افزایش بارندگی داشتیم و در بسیاری از استان‌ها بارندگی در حد نرمال یا بالاتر از نرمال بود اما نسبت به بلندمدت پنجاه ساله هنوز فاصله داریم اما نسبت به سال قبل وضعیت‌مان خیلی بهتر است.
🔹
در هیچ شهری از کشور به مشکل نخواهیم خورد اما نباید بی‌رویه آب مصرف کنیم و نیاز به مصرف بهینه و بهره‌ور داریم و در بعضی استان‌ها نسبت به سال قبل تا هفتاد درصد افزایش بارندگی داشتیم.
@Tv_Fori</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/akhbarefori/659324" target="_blank">📅 17:29 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659323">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P6Zh2aVm4Mxz98O-zBljZGcH2jugDFCr7aQ8IhDUHy-72K8Q3Vs9ecVYQglveyUdRR-Bh4C7TsCXrc29RssrAI1TyEj4OzS5xmFylwJV0MOhp-CvdUlzbMii4NWU9li7U91ihXtYKJVn-h1pokRTUp8NCIEonkjLAsZKpO4987oZHT33Y4tQ2Ijla-Zi4ZmdFrLSxQW7cMCk0IU5oIqyUF-ybfFMlEYoZv79T0Wm3MfbT9pt9UH-NF4pnzpw6OJgw3V7ke4PyGgOtQRcNeZeBexlYPHs3m3-6R3ijbJT4L4hi7duJx1RDfpC6xe3BUuT-2TwoY1tnWoIl_nwjRXztA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مرندی: فعلاً مذاکره دیگری در کار نخواهد بود
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/akhbarefori/659323" target="_blank">📅 17:27 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659322">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">♦️
ادعای آمریکا: می‌خواهیم امروز یادداشت تفاهم امضا شود
سفیر آمریکا در سازمان ملل در مصاحبه با ای‌بی‌سی:
🔹
رئیس‌جمهور ترامپ و معاونش کاملاً به امضای توافق در همین امروز متعهد هستند.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/akhbarefori/659322" target="_blank">📅 17:19 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659321">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UX_sjJSVukP6zzgy3s5f0K5DxkbZGA01G1jjpuIw6QDvY5_HeIzTAwnDgVp6lSJiVDW40nv5a-RO-vIkboxYcJ_WLA9d5x1tFfh07q91JFguqQhP8LMpgUEQX5vL5Qm9uzhsJK3Vjdu_wdNRfIB_KkdMesg9wzxoC_mwhJ5cPWhWcBXrV_c9Euw5NXNUxlQh0TiRAicqreLVbQk8wnlBaLAb5t3o5gtLj3yZ1lks1R0ZZ_2tBTk_SRisfD0dRKAWVWNBXocUX4Okelx8iiNRQwcGEobiHMTZU60zJcoER5m3VKlRky6Utln8N4FOTPJdXLvyxcvNbIvW8tAsznS0ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
والیبال لیگ ملت ها؛ صف آرایی ایران برای بلژیک، امروز
🔹
تیم ملی والیبال ایران از ساعت ۱۷:۳۰ امروز در چهارمین دیدار خود در مرحله مقدماتی لیگ ملت‌های ۲۰۲۶ به مصاف بلژِیک می‌رود. #ورزشی
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/akhbarefori/659321" target="_blank">📅 17:17 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659320">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">♦️
تکذیب شایعه ترور شیخ نعیم قاسم
🔹
گزارش‌ها درباره ترور یا زخمی شدن شیخ نعیم قاسم تکذیب شد؛ بر اساس اطلاعات منتشرشده، در حمله امروز به ضاحیه بیروت «حاج علی موسی دقدوق» معروف به «ابو حسین ساجد»، از فرماندهان ارشد حزب‌الله، به شهادت رسیده است./ مهر
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/akhbarefori/659320" target="_blank">📅 17:06 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659319">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاکوهشت - دیده‌بان رشد اقتصادی ایران</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d47fdce55a.mp4?token=eA_7mwXpLgIX5hEMiCv1fqgaY3FUZ5T3vIn1lA3YVPSEDERo_CD717pzPE7oBUIfWeK3fKCwGFkdKdLFN6MZJxdBTyiUPlNIkTaEUtugeS4zNigoHtRaxqFmxgl31GnQSV2F07HUdobI-4wyUbLUkU900ODkHGGWhVzmQoGcSM15QuQe8Mdoeg5WJ2NSWfcleC7usflRFf7L5yLAyQ3DjDAFetCWzXhSzbsbFr2CGOWAzQHzy-5KBEHP_l3BYfy6JeCsqTpJhsMmDJG_p_XRk02KgduJoGuWAYh0BTENTdBt41PdVfaDNMCluIb2K8vhwCWKgVBCN8GoyiNT2MFjW0x1wsvAkEZkvYCLPSMScQsB9gKRHNz_2_8fh-MsT0uan6i3VC8zdUEhqIRvsLiu0ScjZLCfAoy_juNLOfe3HWwU4cRKXDMzEQ_DJgH2pXNnxf9T0NAZjswYtlAKg2aaP2sUVk1z9sXFWFXqfvZIgfJ5jGhePwPcOmn6OTF_Jl2DzBmjRU0heemRNaLVrPrxYDC_nc_vvQKWvNoxC2Q9btxh2O6pFhB5Pf8y5cFqtRhCCqP_hEnyN0MIlppXp1nb73gwyA-AqCfgyWG1oDBoFU2eSE_lJIlIfJn7MGozrutmkPb8tvetRv22K48_oAIv_Mie2sKF30lWg7V2IskGOQE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d47fdce55a.mp4?token=eA_7mwXpLgIX5hEMiCv1fqgaY3FUZ5T3vIn1lA3YVPSEDERo_CD717pzPE7oBUIfWeK3fKCwGFkdKdLFN6MZJxdBTyiUPlNIkTaEUtugeS4zNigoHtRaxqFmxgl31GnQSV2F07HUdobI-4wyUbLUkU900ODkHGGWhVzmQoGcSM15QuQe8Mdoeg5WJ2NSWfcleC7usflRFf7L5yLAyQ3DjDAFetCWzXhSzbsbFr2CGOWAzQHzy-5KBEHP_l3BYfy6JeCsqTpJhsMmDJG_p_XRk02KgduJoGuWAYh0BTENTdBt41PdVfaDNMCluIb2K8vhwCWKgVBCN8GoyiNT2MFjW0x1wsvAkEZkvYCLPSMScQsB9gKRHNz_2_8fh-MsT0uan6i3VC8zdUEhqIRvsLiu0ScjZLCfAoy_juNLOfe3HWwU4cRKXDMzEQ_DJgH2pXNnxf9T0NAZjswYtlAKg2aaP2sUVk1z9sXFWFXqfvZIgfJ5jGhePwPcOmn6OTF_Jl2DzBmjRU0heemRNaLVrPrxYDC_nc_vvQKWvNoxC2Q9btxh2O6pFhB5Pf8y5cFqtRhCCqP_hEnyN0MIlppXp1nb73gwyA-AqCfgyWG1oDBoFU2eSE_lJIlIfJn7MGozrutmkPb8tvetRv22K48_oAIv_Mie2sKF30lWg7V2IskGOQE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
با این رویه تا چند سال دیگه ما قبرستان پنل‌ها‌ی خورشیدی خواهیم شد!
🎬
نسخه کامل قسمت ۲ برنامه
#نمودار
را در
یوتیوب
مشاهده کنید.
تحلیل‌های به‌روز اقتصاد ایران را در
اکوهشت
دنبال کنید:
@ecohasht</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/akhbarefori/659319" target="_blank">📅 17:05 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659318">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y7171K0_44xhtiuu01CgODpiqM1hvwPvkMqtIWSuihIRDYv1PMo_ZJ1dpIM3hbaQvgMiRNlC9ApHlTSBj3XcrerCKx3994l_ISxYSfKq6DZ_N909D9GsrlolelT-xWmmcG7IwDsAWMXIy6KzsvO56bMsNDRy9-JgVFPeRmv-a5k-9JqF_C5WOP-WXEMx6tZTUboWkogKz4r3nkWyWmHqSAHP_U2-hZW0L6Ln14r-nsYSjkflC3PxXp38BR6GT5lSmEXdzY9YdPyKi168mvTXtQk806Jp2Q-Ce89E7rB1mECvLTvlzNRZhU6tb4zh7T_g0QYMSFCZri_sB6DGvcv_sQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فواید اهدای خون
🔹
هر روز در بیمارستان‌ها، افرادی چشم‌انتظار دریافت خون هستند؛ بیمارانی که ادامه درمان و حتی زندگی آن‌ها به حضور اهداکنندگان خون وابسته است. با یک اقدام ساده و چند دقیقه زمان، می‌توانیم نقشی ارزشمند در نجات جان انسان‌ها داشته باشیم.
🔸
چرا اهدای خون اهمیت دارد؟
کمک به نجات جان بیماران و مصدومان
تأمین خون مورد نیاز برای جراحی‌ها و درمان‌های حیاتی
ایجاد امید برای خانواده‌هایی که چشم‌انتظار بهبود عزیزان خود هستند
🔸
فواید اهدای خون برای اهداکننده
کمک به تولید سلول‌های خونی جدید در بدن
بهره‌مندی از بررسی‌های اولیه سلامت پیش از اهدا
تجربه حس رضایت و آرامش ناشی از کمک به همنوعان
🔶
اگر برای اهدای خون اقدام کرده‌اید یا قصد شرکت در این کار خیر را دارید، به ما پیام دهید
👇
@Ertebat_baforii
@Alo_fori</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/akhbarefori/659318" target="_blank">📅 17:04 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659317">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1f10a10f9f.mp4?token=kP0ZeIuSipCgqYjFEK9zT-z9zUCF6PbT3FHbfZ_Ws53vRNwctiyoODjT_nJGA-OANOUKXHAPXdx4g3zpCq-AZcWTuZ1XOcvGYRWGatxuLABHETtiEJTIRaovP-T7-3WiF9dkq7Q4lk_Wigi8hKnEsmSjtiFm9VGzCJ8Ow9xHXah29WyZgmFu72nMa_kRK2UBMwc9mxL9-BiN94isMZrvWYI9iIIWpXX0h1_8ukeU5tM54AhDZXKSVVfs-tTgvPjw18SVEwtH6hqHA0bJTXnmA9pzDFx2SNot48MVZT0phuAlzg-4QSo65-cdWYgqnjyAijD772aZWTm_vFymaXJW6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1f10a10f9f.mp4?token=kP0ZeIuSipCgqYjFEK9zT-z9zUCF6PbT3FHbfZ_Ws53vRNwctiyoODjT_nJGA-OANOUKXHAPXdx4g3zpCq-AZcWTuZ1XOcvGYRWGatxuLABHETtiEJTIRaovP-T7-3WiF9dkq7Q4lk_Wigi8hKnEsmSjtiFm9VGzCJ8Ow9xHXah29WyZgmFu72nMa_kRK2UBMwc9mxL9-BiN94isMZrvWYI9iIIWpXX0h1_8ukeU5tM54AhDZXKSVVfs-tTgvPjw18SVEwtH6hqHA0bJTXnmA9pzDFx2SNot48MVZT0phuAlzg-4QSo65-cdWYgqnjyAijD772aZWTm_vFymaXJW6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جنون تماشاگران آمریکایی در میدان تایمز نیویورک
🔹
پس از قهرمانی تیم نیکس در مسابقات لیگ بسکتبال حرفه‌ای آمریکا، در خیابان‌های نیویورک، هواداران نیکس در «میدان تایمز» دیوانه وار به تخریب اموال عمومی پرداختند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/akhbarefori/659317" target="_blank">📅 17:02 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659316">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/acbe41861d.mp4?token=AoB-U_MILzGMGAbIfpqjjhKEJi-mor_ILEtFAjs9A1PFzRmBJ8AmWzdwoDOx1CjGUhCdwVTAas8eMT4j-IsYUcWQwzPE12DxxyTjw7OYlsNQOtnarAyQ6MH2b9AYq9DW9SuQLodwkDDPLb8PhkY1BV5KL8-fRWkUQHE9opbxjPeoyNdj5sXdmAwJthQZoEdaY3fg3lsYzrk07_uCXf5N-yxgPEW4meCDbOppSy269vKqu4lU1kwPqC-m5CHJF15htxFWh0SVRrSm5rStFapDHPWvZLkLWNpEh9KUGC9stXgZ8SJ5FCB-HU1Q4-G3CDQLWx_xQXg-y_InrJ1a2bDqnA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/acbe41861d.mp4?token=AoB-U_MILzGMGAbIfpqjjhKEJi-mor_ILEtFAjs9A1PFzRmBJ8AmWzdwoDOx1CjGUhCdwVTAas8eMT4j-IsYUcWQwzPE12DxxyTjw7OYlsNQOtnarAyQ6MH2b9AYq9DW9SuQLodwkDDPLb8PhkY1BV5KL8-fRWkUQHE9opbxjPeoyNdj5sXdmAwJthQZoEdaY3fg3lsYzrk07_uCXf5N-yxgPEW4meCDbOppSy269vKqu4lU1kwPqC-m5CHJF15htxFWh0SVRrSm5rStFapDHPWvZLkLWNpEh9KUGC9stXgZ8SJ5FCB-HU1Q4-G3CDQLWx_xQXg-y_InrJ1a2bDqnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جنون تماشاگران آمریکایی در میدان تایمز نیویورک
🔹
پس از قهرمانی تیم نیکس در مسابقات لیگ بسکتبال حرفه‌ای آمریکا، در خیابان‌های نیویورک، هواداران نیکس در «میدان تایمز» دیوانه وار به تخریب اموال عمومی پرداختند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/akhbarefori/659316" target="_blank">📅 17:00 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659315">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">♦️
رئیس ستاد ارتش رژیم صهیونیستی دستور تشدید عملیات تجاوزکارانه در جنوب لبنان را صادر کرد
🔹
ایال زامیر، رئیس ستاد کل ارتش جنایتکار رژیم صهیونیستی با تأکید بر اینکه لبنان در حال حاضر «مرکز ثقل» تحولات است، از برنامه‌ریزی برای گسترش حملات به حزب‌الله خبر داد.
🔹
در حال آماده‌سازی برای تشدید حملات و تعمیق عملیات‌های مانور زمینی علیه حزب‌الله در جنوب لبنان هستیم.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/akhbarefori/659315" target="_blank">📅 16:57 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659314">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">♦️
دستگیری عامل مرتبط با موساد در ایلام
وزارت اطلاعات:
🔹
«علی.ح» که با یک سرپل وابسته به سرویس جاسوسی رژیم صهیونیستی در ارتباط بود و قصد نفوذ به مراکز داده و سامانه‌های حساس کشور را داشت در استان ایلام دستگیر شد‌.
#اخبار_ایلام
در فضای مجازی
👇
@akhbarilam</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/akhbarefori/659314" target="_blank">📅 16:56 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659313">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9d10200809.mp4?token=RCAnypPjww4ZyFEQr9Zj9TjUsZUx-vBMGP6p65bZwaIANsK-eDK4L3OBqrA2oYRYLJIDdwZA9VyIk1XEHQFnjx607T4WB4LLX3A31Fo5ATIjoIh3gqV7rJYE1y0dyF1A5HWB8bCeqPXp_IwK_ba5GnKXkSc6L59_WJ0K-rwKLgiH5x-Ic9PsiiFN-heaDicXrww_GXdVTu66rTj5Qqm5in1r6LnZenQDOYbxD-znc4qZmfOdQMzgD7AnqbGkUUtgDIZ4PfNtnJg7RuNoBIdjz_GTgf8Xj7lVNmJO_rgF-51m1vYNlD1Tyt0GTxIeJ1RQQyipzajBPnOZAehDWDZ7og" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9d10200809.mp4?token=RCAnypPjww4ZyFEQr9Zj9TjUsZUx-vBMGP6p65bZwaIANsK-eDK4L3OBqrA2oYRYLJIDdwZA9VyIk1XEHQFnjx607T4WB4LLX3A31Fo5ATIjoIh3gqV7rJYE1y0dyF1A5HWB8bCeqPXp_IwK_ba5GnKXkSc6L59_WJ0K-rwKLgiH5x-Ic9PsiiFN-heaDicXrww_GXdVTu66rTj5Qqm5in1r6LnZenQDOYbxD-znc4qZmfOdQMzgD7AnqbGkUUtgDIZ4PfNtnJg7RuNoBIdjz_GTgf8Xj7lVNmJO_rgF-51m1vYNlD1Tyt0GTxIeJ1RQQyipzajBPnOZAehDWDZ7og" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هجوم زنبورها پرواز هواپیما در مکزیک را به تأخیر انداخت
🔹
تجمع یک دسته بزرگ زنبور روی بال یک هواپیما در فرودگاه بین‌المللی کانکون مکزیک باعث تأخیر بیش از ۴۰ دقیقه‌ای در پرواز شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/akhbarefori/659313" target="_blank">📅 16:51 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659312">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d8df3566a9.mp4?token=kpB6Tc-JcPHqZt1yn2-3IdDt4L1I2UCoDtg_VICnNlOjzKbxaCfRqoVaywXv9CW7qKmMYnomCdhZCzmyfbpyNf2_t_begRmB_6fwZK56IJ3TwM7VZfryMtjCSFLQALffgW4nXGEm9hDxVnr9gLmaTl3y1UvzDbKJ6wO05Xqbz8Qj1dR--8VlpRgbM3v7RiW6ZI9gNX4hZPKOkDec0xALRSpHTh2_rLnuoDrV0bXyN0wLe8C8_N4soFSuQ0AuDx0s2fZ0D2ukY6wG3HwREFPIrh8xO8KCIDtZ5ty0SKBrkZyvysez1elaT_itoBQeq8G-VQklZzRFuqP30NnT2f-PwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d8df3566a9.mp4?token=kpB6Tc-JcPHqZt1yn2-3IdDt4L1I2UCoDtg_VICnNlOjzKbxaCfRqoVaywXv9CW7qKmMYnomCdhZCzmyfbpyNf2_t_begRmB_6fwZK56IJ3TwM7VZfryMtjCSFLQALffgW4nXGEm9hDxVnr9gLmaTl3y1UvzDbKJ6wO05Xqbz8Qj1dR--8VlpRgbM3v7RiW6ZI9gNX4hZPKOkDec0xALRSpHTh2_rLnuoDrV0bXyN0wLe8C8_N4soFSuQ0AuDx0s2fZ0D2ukY6wG3HwREFPIrh8xO8KCIDtZ5ty0SKBrkZyvysez1elaT_itoBQeq8G-VQklZzRFuqP30NnT2f-PwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جذاب‌ترین گزارش فوتبال
🔹
پدری که برای فرزند نابینای خود بازی قطر و سوئیس را اینگونه گزارش می‌کند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/akhbarefori/659312" target="_blank">📅 16:42 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659311">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">♦️
ادعای شبکهٔ ۱۲ رژیم صهیونیستی: هدف حمله به ضاحیه فرمانده واحد ارتباطات حزب‌الله بود
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/akhbarefori/659311" target="_blank">📅 16:34 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659310">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">♦️
پیام پزشکیان در سالگرد جنگ تحمیلی ۱۲ روزه
رئیس‌جمهور:
🔹
دشمن صهیونیستی با وجود ترور فرماندهان، دانشمندان هسته‌ای و حمله به زیرساخت‌ها و مناطق مسکونی، در تحقق اهداف خود ناکام ماند.
🔹
جنگ ۱۲ روزه نمادی از انسجام و وحدت ملی بود چرا که ملت ایران فارغ از هر سلیقه و دیدگاه، در دفاع از کشور یکپارچه عمل کرد و دشمن را به پذیرش آتش‌بس وادار کرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/akhbarefori/659310" target="_blank">📅 16:24 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659309">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">♦️
حمله پهپادی رژیم اشغالگر به نبطیه لبنان
🔹
منابع محلی از حمله پهپادی رژیم اشغالگر صهیونیستی به شهرک «انصار» در شهرستان نبطیه در جنوب لبنان خبر دادند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/akhbarefori/659309" target="_blank">📅 16:17 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659308">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HPtlV1iAvEyJmelka_iaxGxeam0Y1La363chwfoAEROpHsg9jztGjbsyHoqRMeylUnD3t8RaIFf9_IYRoI1BH2XCzILdaifyRkRbYtQx_54aaExiwCgt5eFQsWxxdS7t-mMdeECn2P_zwNh3LIG-FjOdVlE5aAALcWMzxJ91Yq1NW5s48K7xKP2YS9kgUAN1ha_slZv9Rl90rLI7My1Wuz93hx2VAda3kpLTnYWsoDXB_GQkeYPxu0Oo8fUTM4xqOdySESj1LVKojJunla7S-oSz0AbHsFj_aitnA_ZVCfZ1IyhKdDm0HMhHKkNvPKxJFPOljjo9ZKUCnyGie_xzJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قالیباف: پس از چراغ سبز آمریکا به رژیم برای تجاوز به ضاحیه، سخن گفتن از ادامه مسیر ممکن نیست
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/akhbarefori/659308" target="_blank">📅 16:04 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659306">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XDfqRZkv6j2PqHP1peU7uNFnHcGLNO8Qi9ZqLu3O5hkj6MB5UOvFvg_l-EWv9VPf4OrfShqfl6MgZjL1_EagIw89RC9n1TAj3Pv0GCUlHT23_fp-4b2BlLFWphlCxaPyHV9n2e6XU8S_6O4TJC2-Me_axL7R0OC1TMnXVaZplh8VjTdIIP0wu0K1v_9t-HrxNjpP38CtOTu4apM_M-EkjAOwc-Tsxtl3qT-HoKaoMQSFPLv-1PPekrGNPvy3unH1OG_pHjoRJp37G9rVIgt2w066Yr5-mhUhO883CYptJK5IGCT9nTeki277HsCpB1-dQtxNQdyXnxH5I9hhTjfAIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RXRCocIws_d0bVqIltTAcig_--8x4n0eaddtqEty6xB8EyTyrzh3ghho8DyUPNpV7VOVuH14ey9vZ304URYhfKiz7KpD1Yza1sTUtYoa4cIvZk6FA4aS_wgLBjpezfv_ik0dF68hYuH_hw3PnCyxzGsyxdNHYq5s59wuBhZGq5fmvmIp7JB0PuJwDPjmL2YIpJK0zmcxTb4KC52dRkkZmNErzIZFoNFucWo-s392ZRcDnD0geiwgC2ZPhEoIYYACuXgc3QstJqp2NUNChDTgXFUFqbBwMsiYbSmYZ9LhQEwKZJgseuNxEh_2E6XwrMAOcmcdXwB2F20_X_tjKrcuZQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
هماهنگی تل‌آویو و واشنگتن پیش از حمله به ضاحیه بیروت  مقامات ارشد صهیونیستی و آمریکایی فاش کردند:
🔹
ارتش رژیم صهیونیستی دقایقی پیش از انجام تجاوز اخیر در ضاحیه بیروت، فرماندهی مرکزی ارتش تروریستی آمریکا (سنتکام) را در جریان این حمله قرار داده بود.
📲
🇮🇷
✊
…</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/akhbarefori/659306" target="_blank">📅 16:03 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659303">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/84a4da2cab.mp4?token=t1kT3TOlt-I11k_35OyCDhiQ_yaXGtrjh-8nySz5SJg-yUPmEjomqN8IxrUwxcPlWYvBvshm9sfkPm4X8IUfmVN9ih6gkVKpWMeab3JW_7YbRRTrbzI_r_80xwzlo-x9N1vSuXx9lN3GLaYF3czezMIf2-NzZ4SeS62ZWllPua0gexXpVgAnOgQOEUF0E46NNTHrR6JjteGYZJpq5lt3yALvi6W_V35nsxmO7TnQz9vb2zrkQX0bpBKs9jdlf08mjWtUgxF4dcPcIChLD1J-AVdspBhr_vmGKldxTC2R3kfATq88fzrJ74lycdnbQCSDknJYpMymlY59O1c2PKiB-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/84a4da2cab.mp4?token=t1kT3TOlt-I11k_35OyCDhiQ_yaXGtrjh-8nySz5SJg-yUPmEjomqN8IxrUwxcPlWYvBvshm9sfkPm4X8IUfmVN9ih6gkVKpWMeab3JW_7YbRRTrbzI_r_80xwzlo-x9N1vSuXx9lN3GLaYF3czezMIf2-NzZ4SeS62ZWllPua0gexXpVgAnOgQOEUF0E46NNTHrR6JjteGYZJpq5lt3yALvi6W_V35nsxmO7TnQz9vb2zrkQX0bpBKs9jdlf08mjWtUgxF4dcPcIChLD1J-AVdspBhr_vmGKldxTC2R3kfATq88fzrJ74lycdnbQCSDknJYpMymlY59O1c2PKiB-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مکرون: فرانسه در جنگ هوش مصنوعی مقابل آمریکا و چین است!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/akhbarefori/659303" target="_blank">📅 15:54 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659302">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">♦️
ادعای شبکه ۱۴ رژیم صهیونیستی: یکی از شخصیت‌های ارشد حزب‌الله در حمله به ضاحیه هدف قرار گرفته است
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/akhbarefori/659302" target="_blank">📅 15:53 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659301">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f1c79a541a.mp4?token=ckYgrfiPymZluT8uSSgFRibJGFpyI_3CKVkZT3cfUvMb7f25KPxI12xCj_QpraRa-2sgMlZKnOkxmGL1Ni_8rNvNvkX0tOx40LTbEOidqOHs_I7guBcMR00T7gpCARnPi7e4BwNQ8_kz1AGmli0NMhV78_LNBjcTJqkG9b19EgBAn22HOnhyzypEOUaVKqoqApe6FZaeeGrl9WNXGkfVoTZszQ4KvHMoSkJRfoCt05wpZjHTuXk9A4iUpR5cY086ZdWIG-f-N9ySc0bmPt4Qer51GwJiPOLt1DFIbrJtbeMHBk9VPKarZKCq33CTjPmHS6IV1-CM3bzvTRhwjpbUgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f1c79a541a.mp4?token=ckYgrfiPymZluT8uSSgFRibJGFpyI_3CKVkZT3cfUvMb7f25KPxI12xCj_QpraRa-2sgMlZKnOkxmGL1Ni_8rNvNvkX0tOx40LTbEOidqOHs_I7guBcMR00T7gpCARnPi7e4BwNQ8_kz1AGmli0NMhV78_LNBjcTJqkG9b19EgBAn22HOnhyzypEOUaVKqoqApe6FZaeeGrl9WNXGkfVoTZszQ4KvHMoSkJRfoCt05wpZjHTuXk9A4iUpR5cY086ZdWIG-f-N9ySc0bmPt4Qer51GwJiPOLt1DFIbrJtbeMHBk9VPKarZKCq33CTjPmHS6IV1-CM3bzvTRhwjpbUgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تداوم درگیری‌ها میان معترضان و پلیس در کشمیر پاکستان
🔹
به گفته منابع خبری، درگیری میان معترضان و پلیس در کشمیر تحت کنترل پاکستان طی روزهای اخیر ادامه داشته و شماری کشته و زخمی شدند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/akhbarefori/659301" target="_blank">📅 15:49 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659300">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wu8Yki_WOHMSgQQdJpq2ufvbmX2z0YsZWMO_qapkrTd-bb2lfW-lMe35gxIyvUwErbqjUgt38Ilu0xYr1XG9PAy_upSdfCJFliOUypgZliiXR9SJJL_NEc2WhJn21LqoY9AYZrWbqhXzNSgT5wEhW-hpQZBviEfyNg0TM0zgx68TytI7oHqKNDTsdb2_rFZjFdurLeAsmHHsWZ4lllagMPPTRDNNlDqMPayPkDylxquIGDWCP79qN8367gzcgSuKxaDNeiyIHdMufJnNlswi2ZxezhsK_zZrCrqOXRvLKBuq95gQJbeQlKnYM-nM2W0G6pndw071TcX6y59TSZnp-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ادعای رسانه‌ اماراتی: امارات ۳ میلیارد دلار به ایران داد تا حمله نکند!
بیزینس‌رکوردر:
🔹
دو منبع منطقه‌ای گفتند که امارات موافقت کرده که در مجموع ۱۰ میلیارد دلار آزاد کند که بیش از ۳ میلیارد دلار آن قبلاً تحویل داده شده است.
🔹
دو منبع دیگر که از این توافق مطلع بودند، کل وجوه مورد نیاز را ۲۰ میلیارد دلار اعلام کردند و افزودند که این اقدام در ازای توقف حملات ایران به امارات مورد توافق قرار گرفته است./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/akhbarefori/659300" target="_blank">📅 15:47 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659299">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cbRo5iHqO5hE35xbXQrQS12717Q78RZ8W5Bug78FgGIY4I8a0nPGSU5D2kUkcQZdux-T6HrQtLdyzyzaTtxMhk4jimHrs9ztoXQXOwf1uobg-v5HO58samk5icjxmOPxWSu24T3lpOWnHsbPaPCPY1u3CvDRQAod6pUgmwAW8Io4foXgk1616JafX3H4obnR4CIXDJjDgS1RsIZ5et9_mTdGlwnSdcWe41iGxSRGRWCmOhuQiUkNTfv2PFuoQCvrXqR34WQXmGQdZOxHDJNN6ZZ-BYQcUeiNN4LL73TkAcP5DrlANsuhY83nfnF_hVl8-uHOjtHlVdooeg0i_UtmgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کم‌خوابی به خاطر تماشای مسابقات جام جهانی طبیعی است، اما هواداران کدام کشور بیش از همه دچار اختلال در خواب می‌شوند؟
🔹
ایران در رتبه یازدهم.
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/akhbarefori/659299" target="_blank">📅 15:38 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659298">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TDdRkZ6_XSpM84jvYSmGCvg9YYG56Tg87Uyoi3ixSFri0zFAzHNEl1YfHOdQWUEpxehsoI9r6N7Yid7KM-cHvGDR3DAdifp73eNl-9tlyAIOW_oo1wuoQUw1Kk-8zTJ9raZrfxQ38EZ8yOUutchwa9U2pihYFqjNQzaXehH0mRKO2jkXeJ_fCgp7iReCk7BZ-14O8dDTkoxmNdtx3f6a93RUaD4dyeOXXi8CN-Mzk8H2bn9ibvxujNPPiqocHLs448Yg95sh9j4x1DrMcCFKR1kLYaibcn5Vwy6ZDQsv5Ntzuvi3xti5pGwW_VeE0H_GXTySrpKZkfFKRtKYggeruA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
طعم نوشابه‌ات فرق نکرده؟ شاید این آخرین جرعه تو باشه
#WillPayThePrice
#تقاص_خواهید_داد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/akhbarefori/659298" target="_blank">📅 15:36 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659297">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/566ae393cf.mp4?token=JHRzsgQHmdGwRFgTHFRzNxByefMKT-iHBp8hRRlU6ydJ5z4n-EHwpd4lTIYWy_oEnHcJy5LL3TOsGfF-XmvK12IZtc-CHtRy25A99DhTn0ywRrwHnNlpUPLK9N3JlLByijb9KpAkOsqfked6wHcdRwJrfYgxpSG7KOHIq1g3GBC0hgId8XZlxfUlg0qcJAwJFB-2Tcu61W8BkFC7sQ6jLmU90uFimcNVGbWt7608KMW9afD4VVp5dQV9ELkYVxpkMtU71zURyeH9XYPDqR2HKGG_Mu_PCxSxLCU8MfwWoJ2pX495_0lJomigUbPNqQCCLHZHwBQJOeD8DoGXNhOhsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/566ae393cf.mp4?token=JHRzsgQHmdGwRFgTHFRzNxByefMKT-iHBp8hRRlU6ydJ5z4n-EHwpd4lTIYWy_oEnHcJy5LL3TOsGfF-XmvK12IZtc-CHtRy25A99DhTn0ywRrwHnNlpUPLK9N3JlLByijb9KpAkOsqfked6wHcdRwJrfYgxpSG7KOHIq1g3GBC0hgId8XZlxfUlg0qcJAwJFB-2Tcu61W8BkFC7sQ6jLmU90uFimcNVGbWt7608KMW9afD4VVp5dQV9ELkYVxpkMtU71zURyeH9XYPDqR2HKGG_Mu_PCxSxLCU8MfwWoJ2pX495_0lJomigUbPNqQCCLHZHwBQJOeD8DoGXNhOhsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
لحظه سقوط هواپیمای ترابری نیروی هوایی هند
🔹
تمام پنج نفر حاضر در هواپیما کشته شدند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/akhbarefori/659297" target="_blank">📅 15:34 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659296">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jtTeYuXlw0N3bzlgGbC8wuW1S3ORUCEm7jqnLK9ToY3yRpdhRd8WtO3U55nY55lZK4ThPPxHlpIO4f9cwwtYXU55CIzEzopXZEUKbjCgHfkrM3KPz8mF3C1V577U3JHN2sk4uPzURJZ37lDJD-r6lVNvTW2s10HbSK-K5UVqvJPuzhfMEu-fU3eCwiK2Jm71j-jJkpcDrWCcs9r5F2LFRUPQvK2CgrASKR5xHMZ-XlB84RifORhO9UpY-Vh3oOmcNk6uGxaj2Yj0PhwKsF9wHmTrtEYl0XykdXc5MA_KzEEhmsg8iiOeTM9c9pZ_7Yj7_RgnWjsMtA5ys5ZWiINcVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ضرغامی: مگر می‌شود موضوعی به این مهمی، تحت نظارت دقیق رهبر انقلاب نباشد؟
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/akhbarefori/659296" target="_blank">📅 15:32 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659295">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">♦️
زیاده‌گویی کانال ۱۲ اسرائیل به نقل از یک مقام امنیتی: این بار، ما حتی پرتاب یک موشک از ایران به خاک اسرائیل را تحمل نخواهیم کرد
🔹
اگر چنین اتفاقی بیفتد، اسرائیل آماده است تا یک حمله نظامی گسترده و خردکننده علیه زیرساخت‌های نظامی و اقتصادی ایران انجام دهد.…</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/akhbarefori/659295" target="_blank">📅 15:28 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659294">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">♦️
آماده باش رژیم صهیونیستی درپی رد کردن خط قرمز ایران  رسانه‌های اسرائیلی:
🔹
رژیم صهیونسیتی از ترس واکنش ایران به بمباران ضاحیه بیروت و موشک باران سرزمین‌های اشغالی توسط ایران، به همه تشکیلات و نهادهای خود آماده باش داده است.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/akhbarefori/659294" target="_blank">📅 15:26 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659293">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FHw1ytwNt1KhwnSNONtLcdAfuZK2lWVSnzHoA6Nb2sXr4-Pd21ZaLFGqMTpW7QT4W-sriwTdXab996RbuaDnS4TJvbIHjY6CgXiT52wYUbvYB-EtVjC6VX95-ul-jAQyGgrruPUtGYNDGlVv2837RvFhZz7rUMf5WQwo0hd4YHKxHQjtleoS73HdzIxRaL3PUG1b2XS8hjUV9QEMlbomm65z_wqMt2zScAjaWZe9IRYX2ZwPhoqKS4yF4FbbS304wsG8HZN52vcZWGQmiJXgTDNeLKtg69gGpSyeLckvniKR04PoRBSCCtmPmg6xkPkzx5jUMxe1EshqvHl9HSoweg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
جاسوسی برای ایران با ۷۴۰ دلار!/ رسوایی امنیتی در اسرائیل
ادعای تایمز اسرائیل:
🔹
یک شهروند ۴۴ ساله ساکن حیفا به اتهام جاسوسی برای ایران بازداشت شده است.
🔹
«رنان بن حایم اوهانا» در دوران تنش‌های مستقیم ایران و اسرائیل، اطلاعاتی از جمله نقاط ضعف بازرسی بنادر، مسیرهای احتمالی قاچاق سلاح و تصاویر اسکله نیروی دریایی آمریکا و سواحل حیفا را در اختیار یک مأمور ایرانی قرار داده است. در ازای این اقدامات تنها ۲۵۰۰ شِکِل (حدود ۷۴۰ دلار) و از طریق ارز دیجیتال دریافت کرده است./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/akhbarefori/659293" target="_blank">📅 15:24 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659292">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SSHunX07nqYZpTxnx2Hx3ofa0ntDgttemLrsUIgZj7cax0XKQZtWAokzZKlIR8pbxLvsSSv_Fg_xYJdTDap-t3BMs3QQAeNXgofUpFMg39Byb-Ua9q19pJWpyJzJu5MNA5gyEjfpVPfydwMhVL6OD9jaU0HOFLHezEFZtMhPL-gs6bNiLsFEm7J3HBDjM1EjmrK_MlWNabY-GSoRzDCWLXQAF1MCgDPpWrEHqab4B7EahyhUoS_ip_YnhErMyQdYNXvHA5Q2foi4exLt6wfVf2bOvU3frea-LtqfFpOHX2-msi9oiKOPXkKwPYy5EX11ZA-q7RgxC3STLD3fpnCVFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
غول لبنیاتی شستا در راه بورس؛ دوشنبه منتظر «تادیکو» باشید!
🔹
خبر فوری: بورس تهران بالاخره زمان عرضه اولیه شرکت «سرمایه‌گذاری کشت و دام صنایع لبنی تأمین» با نماد
#تادیکو
را اعلام کرد.
📍
جزئیات مهمی که باید بدانید:
✅
تاریخ عرضه: دوشنبه ۲۵ خرداد ۱۴۰۵
✅
سهمیه هر کد: حداکثر ۲,۵۰۰ سهم
✅
نقدینگی مورد نیاز: حدود ۱ میلیون و ۶۰۰ هزار تومان (سقف قیمت)
✅
روش عرضه: ثبت سفارش (بوک بیلدینگ)
💡
چرا تادیکو مهم است؟
صنعتی استراتژیک است‌و سود آوری بالا و ریسک کمی دارد
در شرایط بحرانی کمترین آسیب را می بیند و تاب آوری بالایی دارد. نواوری و دانش بنیان از ارکان اصلی تادیکو است
🔔
یک قدم تا خرید:
زمان دقیق ثبت سفارش روز دوشنبه اطلاع‌رسانی خواهد شد. برای اینکه از ساعت دقیق و استراتژی خرید (سفارش‌گذاری بهینه) جا نمانید، حتماً به سایت
tahdico.ir
مراجعه کنید</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/akhbarefori/659292" target="_blank">📅 15:22 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659291">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/868f7e306b.mp4?token=ppK0W_AeS7FLr_xySbaXDfYvZNBgo60PVP-yGEXCs4aq7rF_s0-A_8rj0ETefc6fP_DgpsxMRvE2c5CzEekZ9dEULl31_ECj_aanpOsQXto3Cq0Bmv1YKiGEANDHzcEdy-PLHTeF8NOSm37wT5X6K_9Zr_FWrktyNFX__EIphBYaXHfFN8ZlqqPdIeV5IebjSywCk1L6hnznvieVic7Ps4KOkMx6fGCnISf6_JchJvup3_Iq197UHnTKUIWkPIGLPMjGL0ZKJkcs66uLi9ZA4E2B0E2E_r9-HTX6SkLgQa3HJPrilDvedyxpFA9Y1Q-sqaGD__65Aehd4K9COqrqCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/868f7e306b.mp4?token=ppK0W_AeS7FLr_xySbaXDfYvZNBgo60PVP-yGEXCs4aq7rF_s0-A_8rj0ETefc6fP_DgpsxMRvE2c5CzEekZ9dEULl31_ECj_aanpOsQXto3Cq0Bmv1YKiGEANDHzcEdy-PLHTeF8NOSm37wT5X6K_9Zr_FWrktyNFX__EIphBYaXHfFN8ZlqqPdIeV5IebjSywCk1L6hnznvieVic7Ps4KOkMx6fGCnISf6_JchJvup3_Iq197UHnTKUIWkPIGLPMjGL0ZKJkcs66uLi9ZA4E2B0E2E_r9-HTX6SkLgQa3HJPrilDvedyxpFA9Y1Q-sqaGD__65Aehd4K9COqrqCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حرم حضرت ابوالفضل (ع) در آستانه حلول ماه محرم
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/akhbarefori/659291" target="_blank">📅 15:21 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659290">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/86e11a7f2f.mp4?token=I8dorTJGax3Oh2xkexlJDwEs8bjAZxwqXCwPKjAJdM4LpW1I_9PO6eFeU_CvMWbLCcuaw-hL3kkbi-KXr_0L_g20YqN11eWd1qniL8AY7jYuIV2E4oz_1SoXLeceOKNLvPdPJs012JeMDzTcxnfqDlbuhc3BJnsMTMIX2SUmdhh_Ll4Nc2_XST4c-XS_XaUJPMtbycNsdoX-6IDtSLTtu53GxPtdKu2ORe-B-2oTiZ7BaONgpXQJr-PPnAvtXnxcKeva3YFpj6BcD0bCjRWuMYxJIFNMylCNwlrP83W7fCu0-ADumYuZxL_6vZ0ZhRyI1wN9m_D9oOFq0j7DUGIuPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/86e11a7f2f.mp4?token=I8dorTJGax3Oh2xkexlJDwEs8bjAZxwqXCwPKjAJdM4LpW1I_9PO6eFeU_CvMWbLCcuaw-hL3kkbi-KXr_0L_g20YqN11eWd1qniL8AY7jYuIV2E4oz_1SoXLeceOKNLvPdPJs012JeMDzTcxnfqDlbuhc3BJnsMTMIX2SUmdhh_Ll4Nc2_XST4c-XS_XaUJPMtbycNsdoX-6IDtSLTtu53GxPtdKu2ORe-B-2oTiZ7BaONgpXQJr-PPnAvtXnxcKeva3YFpj6BcD0bCjRWuMYxJIFNMylCNwlrP83W7fCu0-ADumYuZxL_6vZ0ZhRyI1wN9m_D9oOFq0j7DUGIuPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حواشی حضور ایران در جام‌جهانی پیش از آغاز اولین مسابقه
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/akhbarefori/659290" target="_blank">📅 15:18 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659289">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/615ef428a8.mp4?token=lNdQ0yqzMN_WTscnN7XwzdbCWdiGw26-2h2HqboLdlHJzDUCCHak7hE2MsCMCUbuE-PNIHlK1cjK8TH0TzPbpkdyC2KTH_UUg-ZxrJW6tuRS3IjuOUR18h2refvMTaxOPRoTaMfkHnEnoIAeOCK0z4XjLs7W-tCuAsl3wkxCzwY9DzxdZ0RJrmkcrAASDqRVrmc7Pxg5AvQIpQUKYxW2fJdFPyH5NiiIYtO_WriN545kJYkTocfoMXKXbqtqA4Nru17viSMvSByqLiz8lRA5YG-V879Nb6G09f0MV06BVK8JIa-Rf68Lyv7K74Cbly0nI1f-V_rgc0SJ1njHosDHHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/615ef428a8.mp4?token=lNdQ0yqzMN_WTscnN7XwzdbCWdiGw26-2h2HqboLdlHJzDUCCHak7hE2MsCMCUbuE-PNIHlK1cjK8TH0TzPbpkdyC2KTH_UUg-ZxrJW6tuRS3IjuOUR18h2refvMTaxOPRoTaMfkHnEnoIAeOCK0z4XjLs7W-tCuAsl3wkxCzwY9DzxdZ0RJrmkcrAASDqRVrmc7Pxg5AvQIpQUKYxW2fJdFPyH5NiiIYtO_WriN545kJYkTocfoMXKXbqtqA4Nru17viSMvSByqLiz8lRA5YG-V879Nb6G09f0MV06BVK8JIa-Rf68Lyv7K74Cbly0nI1f-V_rgc0SJ1njHosDHHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویدیویی بسیار تماشایی از طبیعت فوق‌العاده دماوند
#ایران_زیبا
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/akhbarefori/659289" target="_blank">📅 15:08 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659288">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c0a7191a0.mp4?token=NF4ZNDyX72fUE1V6RCdcTBnVGLyAO0kHX1XrJTj2DSpTmHUmVeTVJFNBZ9rz4jQHx4AcdWZqxNErPdWYxPByCeln5kh3i2qnpUIM1sbs-m9qo-k58gMQKdSPHag8HJLYKVPxZfcYgpvOcZGFCpV0-GskR6Pm-yOjaPgk41wmDLpPfm1zwQ32k-6VSpJvaRc-rvC6DK3HmXalxChB2V0fOrbDuapt-JQ7pMHXF8grIcf2_b7d_uOObEWcET-t5Yx3js04b61p0n01XVAhQH1Dfy4h-C3NRYxNQH3bJHkJ34XcymVoEZ5hTZqB30kUD6Xc5qBgLyjeOAGUCW07H8qKtg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c0a7191a0.mp4?token=NF4ZNDyX72fUE1V6RCdcTBnVGLyAO0kHX1XrJTj2DSpTmHUmVeTVJFNBZ9rz4jQHx4AcdWZqxNErPdWYxPByCeln5kh3i2qnpUIM1sbs-m9qo-k58gMQKdSPHag8HJLYKVPxZfcYgpvOcZGFCpV0-GskR6Pm-yOjaPgk41wmDLpPfm1zwQ32k-6VSpJvaRc-rvC6DK3HmXalxChB2V0fOrbDuapt-JQ7pMHXF8grIcf2_b7d_uOObEWcET-t5Yx3js04b61p0n01XVAhQH1Dfy4h-C3NRYxNQH3bJHkJ34XcymVoEZ5hTZqB30kUD6Xc5qBgLyjeOAGUCW07H8qKtg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دستگیری ۱۲۶ عضو شبکهٔ اغتشاشات و متلاشی‌شدن یک گروهک تروریستی توسط وزارت اطلاعات  وزارت اطلاعات:
🔹
یک هستهٔ ۴ نفره گروهک تروریستی-تکفیری متلاشی، یک مزدور متصل به سرپل رژیم صهیونیستی و ۱۲۶ نفر از اعضای شبکه اغتشاشات خيابانی دشمن در طول جنگ تحمیلی سوم دستگیر…</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/akhbarefori/659288" target="_blank">📅 15:02 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659287">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-poll">
<h4>📊 معمولا بازی ‌های تیم ملی در جام جهانی را چگونه دنبال می کنید؟</h4>
<ul>
<li>✓ پخش زنده تلویزیون و شبکه‌های داخلی</li>
<li>✓ اینترنت، گوشی و پلتفرم‌های آنلاین</li>
<li>✓ پیگیری نتایج بعد از مسابقه</li>
<li>✓ خیلی پیگیر فوتبال نیستم</li>
</ul>
</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/akhbarefori/659287" target="_blank">📅 14:59 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659286">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">♦️
آماده باش رژیم صهیونیستی درپی رد کردن خط قرمز ایران
رسانه‌های اسرائیلی:
🔹
رژیم صهیونسیتی از ترس واکنش ایران به بمباران ضاحیه بیروت و موشک باران سرزمین‌های اشغالی توسط ایران، به همه تشکیلات و نهادهای خود آماده باش داده است.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/akhbarefori/659286" target="_blank">📅 14:59 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659285">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qvbkCKDip8bDpHn3Zkd82UyGLuikwxE-J-5mTUI3n-EoNg1C6QBQg-0YlJqgLLMZkESleczD0NFaer2IY6b-3oLI_oSVsWB9nRJ6vZwbKI0qgrkO-C4PdZPo8wSwOw2bOdbF0Oj7kDHD5zuCNsX7MUgCOiVKRuI7VhQP4Vo7ZlE55BBWuJkplRsly_SNr3XLuyNzwJBEBokUNXfiCrs6V0hMG9gUn24y9rKAVftBksF9TllaQgLUJ8d_jrgdCUlcrDSf5xM5mylOCrTOXn8fVlLgjzIYJNYymMwOqky8bzb0a5irQ_yv-kkq44kmAjMZRTl2rOPs_U6gCCOrjP9OLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
دستخط منتشر نشدهٔ رهبر شهید انقلاب در ابتدای قرآنی که ثواب تلاوت آن را به شهدای جنگ ۱۲ روزه هدیه کردند
🔹
بسم الله الرّحمن الرّحیم
شروع در تلاوت هدیه به ارواح طیبۀ سرداران و دانشمندان شهید در جنگ اخیر و دیگر شهیدان عزیز این واقعه در سحر.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/akhbarefori/659285" target="_blank">📅 14:56 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659284">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">♦️
حمله رژیم صهیونیستی به ضاحیهُ تاکنون یک شهید و ۴ زخمی بر جای گذاشته است
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/akhbarefori/659284" target="_blank">📅 14:55 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659283">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">♦️
عراقچی: امنیت منطقه نمی‌تواند بر پایه نادیده گرفتن ایران شکل بگیرد
وزیر خارجه:
🔹
آنچه تصویر واقعی قدرت ایران را به جهان نشان داد، تنها توان نظامی نبود، بلکه انسجام ملی، ایستادگی ملت و حضور آگاهانه مردم در صحنه بود؛ سرمایه‌ای که امروز پشتوانه اصلی اقتدار ایران در عرصه دیپلماسی محسوب می‌شود.
🔹
تجربه جنگ اخیر نشان داد که امنیت منطقه نمی‌تواند بر پایه حذف یا نادیده گرفتن ایران شکل بگیرد. کشورهای منطقه به تدریج به این واقعیت رسیده‌اند که امنیت پایدار، توسعه اقتصادی و ثبات منطقه‌ای تنها در سایه همکاری، تفاهم و در نظر گرفتن منافع مشترک همه کشورهای منطقه از جمله جمهوری اسلامی ایران امکان‌پذیر است.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/akhbarefori/659283" target="_blank">📅 14:54 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659282">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y7piSX4-Fr0yPDL0xtGE_IGIBMBF52HETqJxdaF1QQH4o9dxCy6qXsB7QLj9XQAoUiN_RE_nXKnrpaEu3p0uitVH_CRfyMiYib7L2RZDL5Ak3Lrw0_lGCA9mVBF6_7pgPUgMhUOs7zjr1mZZNVra9Fb4NFPvWq3N9Iz32hrjN6utnVkAzoAT3RNoqBkKu2PpSMj3dFQgoxtEnDA8D_g_x7EZzGGgCKNtQIGIeUASNhdwSVPRH57oF_bRoKV_COZM6z1ZVZT2CBFqvH-8jk6yaqHv9CqoYrlyCYPDjCq0PTttMo5zctUEObvaijgmYosEGwA77DBYFU0HqP7lTyJdEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پوستر فدراسیون فوتبال ایران برای دیدار با نیوزیلند
🔹
تیم ملی فوتبال ایران در اولین بازی خود در جام جهانی ۲۰۲۶ صبح سه شنبه ۲۶ خرداد و از ساعت ۰۴:۳۰ به وقت تهران رو در روی تیم ملی فوتبال نیوزیلند قرار می گیرد.
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/akhbarefori/659282" target="_blank">📅 14:52 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659281">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">📷
سلبریتی آمریکایی پرچم ایران را به اهتزار درآورد
🔹
«جکسون هینکل» اینفلوئنسر معروف آمریکایی امروز در تمرین تیم ملی فوتبال ایران در تیخوانا، مکزیک حضور پیدا کرد و حمایت خود را از شاگردان قلعه‌نویی در جام جهانی اعلام کرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/akhbarefori/659281" target="_blank">📅 14:51 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659280">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/304e288b78.mp4?token=Vx4bJ3LTe_lHj7rnY-13tL3sq3hQEHd8Kq7XnQpZGD-Lk0kKQiZ4I6FQJI65aQeptjgmUaRt1h2otdEHEyhjyVhvSjBYKLfi93HyJUzcGg6fWcjxZ0gRKhQt7kFmUSFmcmgeza6Yg13SnSB4VAMpUKB05OluY8eqqdpVGf_k8LekCw5UaycZUJYGxTQ41ywrGGVwqdLS36Zg8bbMXocAv-F45VyuXlto7dyAZsANMIHwQz7nI9Cw-mNX4mTHDEZcJPrLK3ae--RGgi-v22109Vsoxy_weFNOdVvb5-OFDjCbj8HUG2abJs3v72AWgFAVfhGa__XNIRLs5oAUHlBRbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/304e288b78.mp4?token=Vx4bJ3LTe_lHj7rnY-13tL3sq3hQEHd8Kq7XnQpZGD-Lk0kKQiZ4I6FQJI65aQeptjgmUaRt1h2otdEHEyhjyVhvSjBYKLfi93HyJUzcGg6fWcjxZ0gRKhQt7kFmUSFmcmgeza6Yg13SnSB4VAMpUKB05OluY8eqqdpVGf_k8LekCw5UaycZUJYGxTQ41ywrGGVwqdLS36Zg8bbMXocAv-F45VyuXlto7dyAZsANMIHwQz7nI9Cw-mNX4mTHDEZcJPrLK3ae--RGgi-v22109Vsoxy_weFNOdVvb5-OFDjCbj8HUG2abJs3v72AWgFAVfhGa__XNIRLs5oAUHlBRbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تنگۀ هرمز تا اطلاع بعدی همچنان مسدود است
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/akhbarefori/659280" target="_blank">📅 14:51 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659279">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">♦️
تصاویر منتشرشده توسط ارتش رژیم صهیونیستی از لحظهٔ حمله به ضاحیهٔ بیروت
🔹
کانال ۱۲ رژیم صهیونیستی مدعی شد که اسرائیل یک مقر حزب الله را در ضاحیه هدف قرار داده است.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/akhbarefori/659279" target="_blank">📅 14:49 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659278">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
۶۵۳ اصابت در تهران و آسیب به بیش از ۵۰ هزار واحد مسکونی در دوران جنگ
علی نصیری، رییس سازمان پیشگیری و مدیریت بحران شهر تهران در
#گفتگو
با خبرفوری:
🔹
در جریان جنگ، تهران ۶۵۳ مورد اصابت را تجربه کرده که ۳ مورد آن مربوط به حملات بامداد پنجشنبه به پایگاه‌های نظامی بوده و خسارت مردمی نداشته است.
🔹
۵۰ هزار و ۸۴۹ واحد مسکونی آسیب دیده‌اند که از این تعداد، ۳۹ هزار و ۴۷۲ واحد خسارت جزئی، ۸ هزار و ۹۲۰ واحد خسارت متوسط، ۴۵۶ واحد نیازمند مقاوم‌سازی و ۲ هزار و یک واحد نیازمند تخریب و نوسازی هستند. روند تعیین تکلیف و بازسازی بخش عمده این واحدها در حال انجام است.
@Tv_Fori</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/akhbarefori/659278" target="_blank">📅 14:46 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659277">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">♦️
حملات رژیم صهیونیستی به صور لبنان
🔹
منابع محلی از حمله هوایی رژیم صهیونیستی به منطقه «الحوش» در شهر صور در جنوب لبنان خبر دادند.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/akhbarefori/659277" target="_blank">📅 14:40 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659276">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c876708ff0.mp4?token=bDcyoMXB0zPmf270Q3OBfW9tKrpNXoRbvxvb2Sf14zaQb14URiByvhL55BwBkvkc-Sy9Q23QKd5yHfWV5LcABg9vVNqe4S1QtYnI7rzYKUnWYGbmvQ0S879uMs56DnbGK5noTQl7-LJj7sNgrrAd-7kvTHqtnS-lfH10FujlKuxetM348UqdSX5KzQkn24HrymCtv_PgNMyywehdgPVy_JZ_S_uC4sEh2USpiO9vqXhuaNE3msmoVsv9NaE5j9LJ_ZxLT_qKblGeAkR074QGfBn27M6YkhFQMlRWmeUI-aueKW_eLwY_QAJCI6lIj8aD19EdLr24IC8UYYowfJwmDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c876708ff0.mp4?token=bDcyoMXB0zPmf270Q3OBfW9tKrpNXoRbvxvb2Sf14zaQb14URiByvhL55BwBkvkc-Sy9Q23QKd5yHfWV5LcABg9vVNqe4S1QtYnI7rzYKUnWYGbmvQ0S879uMs56DnbGK5noTQl7-LJj7sNgrrAd-7kvTHqtnS-lfH10FujlKuxetM348UqdSX5KzQkn24HrymCtv_PgNMyywehdgPVy_JZ_S_uC4sEh2USpiO9vqXhuaNE3msmoVsv9NaE5j9LJ_ZxLT_qKblGeAkR074QGfBn27M6YkhFQMlRWmeUI-aueKW_eLwY_QAJCI6lIj8aD19EdLr24IC8UYYowfJwmDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادعای سخنگوی ارتش اسرائیل: زیرساخت‌های حزب‌الله در ضاحیه بیروت را هدف قرار داده‌ایم
🔹
حمله دشمن صهیونیستی به ساختمانی مسکونی در محله الغبیری انجام شد و تا کنون تعداد بالایی زخمی به مراکز درمانی منتقل شدند.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/akhbarefori/659276" target="_blank">📅 14:34 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659275">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">♦️
حریری، رئیس اتاق بازرگانی مشترک ایران و چین: در سال ۱۴۰۴، ۱۸ میلیارد دلار واردات از چین داشتیم
🔹
پنل‌های خورشیدی و لوازم جانبی ساخت نیروگاه خورشیدی در صدر کالاهای وارداتی از چین بوده و خودرو به صورت قطعات منفصله یا ساخته شده و لوازم مربوط به ساخت ابزار الکتریکی از دیگر اقلام عمده واردات رسمی از چین هستند.
🔹
اقلام مصرفی هم در صدر اقلامی قرار دارند که از چین قاچاق می‌شوند./ خبرفردا
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/akhbarefori/659275" target="_blank">📅 14:34 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659274">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">♦️
ادعای رویترز به نقل از مقام ایرانی:  بر اساس یادداشت تفاهم، آمریکا ۲۵ میلیارد دلار از دارایی‌های ایران را از طریق انتقال مستقیم نقدی، همکاری میان کشور‌های منطقه و خطوط اعتباری مالی، آزاد می‌کند/ انتخاب
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/akhbarefori/659274" target="_blank">📅 14:30 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659273">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">♦️
خدمات کارتی بانک ملی تا ساعاتی دیگر وصل می‌شود
شرکت خدمات انفورماتیک:
🔹
ارائه خدمات حضوری در شعب بانک ملی از ساعتی قبل آغاز شده و خدمات کارتی این بانک نیز تا ساعاتی دیگر برقرار می‌شود. بر اساس این گزارش، تا ساعت ۱۳ امروز بیش از ۷.۶ میلیون تراکنش در بانک صادرات با موفقیت بالای ۹۹ درصد و حدود ۳.۴ میلیون تراکنش در بانک تجارت با موفقیت ۹۸ درصد انجام شده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/akhbarefori/659273" target="_blank">📅 14:27 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659272">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">♦️
حمله به ساختمان ۵ طبقه در ضاحیه جنوبی بیروت
🔹
شبکه خبری المیادین از حمله هوایی رژیم اشغالگر صهیونیستی به یک ساختمان پنج طبقه در ضاحیه جنوبی بیروت خبر داد.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/akhbarefori/659272" target="_blank">📅 14:23 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659271">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64c7423cdc.mp4?token=pwOfdY9vlw9fUQw5_EK29QPUIMiYm65d-XtZhUpnbILVvp6O3A6_JJ9kXPL4Koi9pUmXGQ_mLoDuAp2clIgcZpBYqVULtiBTD_OFUkGK3YcG0azKRNi84rqh8IvOinSU9mWYP9JX5DDdXLOxJ_NQ45XSIkAZz8EX4FYkoq3EO0YWZxg_uMx1LlWzTWJPuMNxL1cgJzdQeTPY9266Kh061kZB3SqiyGCIeZlnFGQgW8fv47kTucgBopIra3s7NclyDCekLBcgHspwo1hcF2__XFMntFdQz_sT9LpUZwMiHz5vtUDrrRmYp0ZDuUPJidV7uHrqZxemZqE1pQLs94G8gQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64c7423cdc.mp4?token=pwOfdY9vlw9fUQw5_EK29QPUIMiYm65d-XtZhUpnbILVvp6O3A6_JJ9kXPL4Koi9pUmXGQ_mLoDuAp2clIgcZpBYqVULtiBTD_OFUkGK3YcG0azKRNi84rqh8IvOinSU9mWYP9JX5DDdXLOxJ_NQ45XSIkAZz8EX4FYkoq3EO0YWZxg_uMx1LlWzTWJPuMNxL1cgJzdQeTPY9266Kh061kZB3SqiyGCIeZlnFGQgW8fv47kTucgBopIra3s7NclyDCekLBcgHspwo1hcF2__XFMntFdQz_sT9LpUZwMiHz5vtUDrrRmYp0ZDuUPJidV7uHrqZxemZqE1pQLs94G8gQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حمله به ساختمان ۵ طبقه در ضاحیه جنوبی بیروت
🔹
شبکه خبری المیادین از حمله هوایی رژیم اشغالگر صهیونیستی به یک ساختمان پنج طبقه در ضاحیه جنوبی بیروت خبر داد.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/akhbarefori/659271" target="_blank">📅 14:22 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659267">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TzFa17A6K6Sd1w4IZ9Qi982ndi7TisdE2mjLK3m9f_XjuwHikOXz_B8_rlArArOimYSPaMLzUfHlJ8KutaTAetieaOF73exERCkIwDMrSCmVGfFbl7_fgqHZwnnPvLCxpk_22PElR-5grh3gI-lM9bDyfvmKBZFb6UeYRUaoa_AT2wNT9se4ZWI8yIjGEI47NviolDM3J1tJGWNWfm-qkwjSUZmk5G6bgC2Dw0bTkQXl9jE63v53nbGb-R2s-iAv8_lFfZGBgsjQ1Zurlrh5iz7CsBYnMVNoRzLg8CxgBKGjEh8dehLMInO6z3hJba1YgExaYsIAv-jczpqInbkCWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/is5wgJds4Q-iWoE-6Rh6ote5XZ-nqtRMbp-S8K94gTzoqpHZFWmkjmm4qFAWG-J0x32RTYFktBv-9Y2c5gL_RrdcUhOlfPRxFPWYDQF0wO24ATO13vnzD--jg5VzxPYBn6TTtI-AHH39zZcxORCMzVRLfirSCSbVfZT8nEeQ2Nu4fXG2Stal74jEL9ZTO3ryUE6kLY9E5wC4ghNVg0D5IE_T0h-Rbc_hD7-YiQ3IkybrpB4gRNvbyf6NuHiODh-OK6cwzVc5QJcp4YuoOgV0MX7W_I7Q5GzudOgBoyE7YwsHji3gpJDIefd0OEaNPhSuJVx_C9_AKDBZ_vx9zu8HyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/p70OCOwsTlp18Opa2G7M4U2X-B8NCh0OblopvAf15DWSAoi_2wxssVaY0907Bcd8mqQTWOtzWG4LjXx8TiVUjag24ScZuC-jjnTbnl39EVdfs57HE91XJyDcst_gDF4eGYwmzWzwnUk62hsje2gTm6xdlmjWFUGYgLJGn3IR7VqifCUyu6voO68akFQA0Lkh-MHKn59bRAZ6pqt4mDJFsWGc_s9lDIqfW1WzrfmwdpEWgXxjPn1lOHjY_P-cJ5TTOZHVng46UOvmXumD2Lqd6QOc1x9kPqjzv7o9VulEBYOP_rko64TAW2uchZxZLGBvqqVhboNi_Czw9pYS2kytSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DdN13eIrFwOr8VL2ipdsufHtkgfE_HKfKqdMduqR2g4l1vZMElaEJ4vXkmzNga-lYpeuS-k5iQO0mluZbfXcxmJvTwMdSltszA0p-xQzHXrWuHV2hI3c9sB8mNApbstI45Mp65KfQs7HtlJoWb47tJrBnhFHgpf8GcEEGb37-1RE0Dhglhnv14K08-oXc3UQ18aSUp3JjRcArda9uA37RjeOzd-cC2DpWglanDAUmv2Dxbz-t_CQycwHCG8HV7udfeam9WnkHdu1gvIpPEAHEW-RAug2BykZV5iCD-D2Tz0jA6TLZtbUpGmXsEn2xYc1AOUfa46YvziMqdEwzwOyYg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
تصاویری از محل مورد هدف قرار گرفته توسط رژیم صهیونسیتی در ضاحیه جنوبی بیروت
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/akhbarefori/659267" target="_blank">📅 14:18 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659266">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cae8cb26f2.mp4?token=nAJpFp32j2t7KU6hfhX7t_C7Cg6YnT52xNNkpI-uC-OnVuz9UeqAxcD6GSSloeK2Xzzpv48qRfab1jr0woctyxmYKw9-6LTsIfsIq-IdmpQSYTIsrs3GGVK6bXnev3Vb-UWzOb3W6kWzMFHx4ZqB4v08XlRq8HCvucnz_qJ72PKSIKti8IrDMtYTvHnNdPv6KuOehKAOFYl_Do1WwKwgU_pMJ9yhpuO4OlY7Q_FXIb0Qy1EYfRh-g1gozT-8qk6UBdV9rLnELK_GkPvjggjWhWgolQY6_BTSMLADmrjICJVuMBMsCbKx6Fpuok1ODFxFw_zBQSZ9Y2T6tLrkTDQ06x7dt7ayZ9ruXPk1_ON0dTkhsYeX-1smXqW0Z1-RKT040gqeSJIHnsNLfXexXdWGfvXFtEzGLssksf06nadfBq_wTrKOkxWHBxrvTVlvLjzZGbzgmJZ4dnsOd0xmjqA0hEYG7y7WpUywn7EYNe2QG28N8gE3iJkAeUAeAu-maF-bkg_sjXtVgZQZwXowYCKXzQ8tosfHhoXK3Abu1JFqke59w1-yhblbYAn7tafN4nWlRkQ7XqMfQz16d6cUdWJr5x70HsuSunadqkjPMQcAyvuDmHjcPN28cdWiG1yazUTefzB2yrLWBCtApRPzX6_-enuXz3l0veQ04WHFS0df0pY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cae8cb26f2.mp4?token=nAJpFp32j2t7KU6hfhX7t_C7Cg6YnT52xNNkpI-uC-OnVuz9UeqAxcD6GSSloeK2Xzzpv48qRfab1jr0woctyxmYKw9-6LTsIfsIq-IdmpQSYTIsrs3GGVK6bXnev3Vb-UWzOb3W6kWzMFHx4ZqB4v08XlRq8HCvucnz_qJ72PKSIKti8IrDMtYTvHnNdPv6KuOehKAOFYl_Do1WwKwgU_pMJ9yhpuO4OlY7Q_FXIb0Qy1EYfRh-g1gozT-8qk6UBdV9rLnELK_GkPvjggjWhWgolQY6_BTSMLADmrjICJVuMBMsCbKx6Fpuok1ODFxFw_zBQSZ9Y2T6tLrkTDQ06x7dt7ayZ9ruXPk1_ON0dTkhsYeX-1smXqW0Z1-RKT040gqeSJIHnsNLfXexXdWGfvXFtEzGLssksf06nadfBq_wTrKOkxWHBxrvTVlvLjzZGbzgmJZ4dnsOd0xmjqA0hEYG7y7WpUywn7EYNe2QG28N8gE3iJkAeUAeAu-maF-bkg_sjXtVgZQZwXowYCKXzQ8tosfHhoXK3Abu1JFqke59w1-yhblbYAn7tafN4nWlRkQ7XqMfQz16d6cUdWJr5x70HsuSunadqkjPMQcAyvuDmHjcPN28cdWiG1yazUTefzB2yrLWBCtApRPzX6_-enuXz3l0veQ04WHFS0df0pY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ماکان کجاست؟!
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/akhbarefori/659266" target="_blank">📅 14:17 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659265">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4d4a213e37.mp4?token=X-WJ4z508DJugwegz0HVhg4h3GPlgeRQKcbud9STSPrO4blzh2n31tDQ1gPIMYNZXEbZt0i7eEJGiYhG2y6-2yq3jqwI0tOJQIKLm6o3mt2eF2vXmPNgvGNmrXxgH_z3vR4nAAEc80vc2qilvNzp-8kKXKwSNrESty0A1AsbG1rcoztOPePVtmlutavlG1TCRVOHeOs_IcWJ8J1XUJe3t3QD7ScEl9N2D_VveDorafW7VgGbTdWll_gde3h9O8vdQ5GSsN2hs22_DHPJ4vm-xrfvkwStVaofMtcQ7raQ2Cim6rkg13LSyv2wLnMW1BCrHjCWwmhwD0pb3ZjgSaw3Eg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4d4a213e37.mp4?token=X-WJ4z508DJugwegz0HVhg4h3GPlgeRQKcbud9STSPrO4blzh2n31tDQ1gPIMYNZXEbZt0i7eEJGiYhG2y6-2yq3jqwI0tOJQIKLm6o3mt2eF2vXmPNgvGNmrXxgH_z3vR4nAAEc80vc2qilvNzp-8kKXKwSNrESty0A1AsbG1rcoztOPePVtmlutavlG1TCRVOHeOs_IcWJ8J1XUJe3t3QD7ScEl9N2D_VveDorafW7VgGbTdWll_gde3h9O8vdQ5GSsN2hs22_DHPJ4vm-xrfvkwStVaofMtcQ7raQ2Cim6rkg13LSyv2wLnMW1BCrHjCWwmhwD0pb3ZjgSaw3Eg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
قلبِ من این وطن است...
🇮🇷
♥️
#ایران_من
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/akhbarefori/659265" target="_blank">📅 14:16 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659264">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qS8zQGLDwLjo0ckt4m309w0LhAMuK0tTUJahyc5gXx6DewyjmXYGdzbCj5W11kO-9A2CyXRut9sOoRyzzK3oGGTKgsXUoBkyZjZZ37oYNEja36z3muoBsIuOhN3_RgW8A-XrSyAaJk0O6gxhXHj8dPBnRE64ZfwHlGdg_lYUhL0LXQeBH7tBqGHJ9tiwaAa3lZwf7_Qy2rQHBeI2O2cx2-Ec3dB6E3KiDo9hbks2a6wK9KUM5tXgSkLdGCmega2vDULbYPTkFLmyK8t-VaU8o9K5CVBRLwkxOm99kDv7jPAFgyH_pTxMYjcYb_MdTmuimUKRli4A5bwht98vQH-pMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آخرین فرصت انجام خدمات دندانپزشکی با شرایط اقساطی ویژه و بدون سود
🦷
💳
کامپوزیت ونیر و لمینیت سرامیکی
✨
ترمیم و عصب‌کشی دندان
بلیچینگ و سفید کردن دندان
🦷
⚪️
به صورت اقساط تا یک سال
📅
🎁
آفر ویژه فقط ۲۴ ساعت:
جرم‌گیری با ۵۰٪ تخفیف
🎉
❗️
ظرفیت محدود
رزرو و مشاوره:
📞
09150156363
☎️
05138112425
📸
@asha
(
https://t.me/asha
).dental.studio
🌐
ashadentalstudio.com
(
http://ashadentalstudio.com/
)</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/akhbarefori/659264" target="_blank">📅 14:15 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659263">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e85d2e96f.mp4?token=ZCbz4su6dB2-Q1gov5VXh5MiChCkQ-xxQDM4Jexib0k2DeX2rX8dN9wkJnuLqzonwmGMdfHU4V_3Yw75VsyXIzBPrbPWe6zm0zvhJ-rsiRqLSXHPOYk5QWCWaK88IJ1C0FX_NdZSFArOwF3kwyc43iCC3utuNaZVOQWWpMcJUR3f67Uc9Vdx6MXbZNeUJWJo1ttxJztE5wdpmFos52ePu3jNAVj2di74MCNNYadlbMDUmCPCuXzLaeItIzK3ZsU33Ve4l3b4YVD3VG6Vw7XQJrwz1eYpPSPZjYzT68zEZLwzD0r8D8_wHPoo2sDY4XDdOYgowgqzieGsMqW_ex0AZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e85d2e96f.mp4?token=ZCbz4su6dB2-Q1gov5VXh5MiChCkQ-xxQDM4Jexib0k2DeX2rX8dN9wkJnuLqzonwmGMdfHU4V_3Yw75VsyXIzBPrbPWe6zm0zvhJ-rsiRqLSXHPOYk5QWCWaK88IJ1C0FX_NdZSFArOwF3kwyc43iCC3utuNaZVOQWWpMcJUR3f67Uc9Vdx6MXbZNeUJWJo1ttxJztE5wdpmFos52ePu3jNAVj2di74MCNNYadlbMDUmCPCuXzLaeItIzK3ZsU33Ve4l3b4YVD3VG6Vw7XQJrwz1eYpPSPZjYzT68zEZLwzD0r8D8_wHPoo2sDY4XDdOYgowgqzieGsMqW_ex0AZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویری از محل مورد هدف قرار گرفته توسط رژیم صهیونسیتی در ضاحیه جنوبی
بیروت
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/akhbarefori/659263" target="_blank">📅 14:10 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659260">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qcrOjdeoHa7_8DV87rlEI-4zp5oSq-I-FIhIoitdhIJ60hjqoQk6GuFcomI_dorfdPdhTCnHnyDakvZb1Jp45vDNWRkQJ7TAvGflb-UxNdK87RB_cUzpxb-v1i-jYgvIFa3htPEVJkAZ0YVSpZ19P_3oYx79cNJEDu4nAOS0QGcQq39mVcH_YHZbMzKn6litxhiDUEQ9r3Fp8yevuvX7Pu32fQ3xXK1bjK5Buk0RwfBtG3zspKpEDWm_mqFPmlFmuLcyOu4-lp2_gi904KMYm1_w2srjXt0yBzFAM5h1Y1fzeO5lEJWmZYaglJDoefzEM02HoK0eAu5EWzEg5NausA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hsqFdvnIYYixbJxtOid-TCUEOgB79xVZKTrncuU-n6i0mmOLlrSOl4XdMLiBu5WxgVH_f9SaW1805IMvQNyui-vFBHWQmNXcJ7dyYe5TswA16wcdwNhVKdrI6f1MgPMqxqpIKXWbBMkFjMbcZs0tuQ7wP9p1VOvIO0e8yWrGgbyuXlNF5c69iRYw_-ALWLTC2qAHXhAIUzTDYm8dqigYaQjiNjXkUfxvszjILbWx1b_9v8zHU_PUEzgpVYi0jCiKvuzuwy3aPNHS1at0pRG-cI4KEbwV9oy_SdYW2xNyb9pBnlj1nWIHmsx-bux_l0v6P65DUR7vR_qrnArzm8IOqw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db832997e8.mp4?token=Kc7qRL77YtFxKSzgZ4va2FK_u-40aFRfYwxNnrI-YOqGPW4xFfFsuJZZOZatjpcFrLxjsZtS02zoSuaByR3QeOPloBtve9jGNFndNiI5IBAlFx54jsas4CoiB12r7aCNUPMtZZmOKKjNkB1S2rpdwsL7CczG4_u3IWzlZe9kfdfL0Zu7CaRj1CTE-zEoaWGt8RUMDlVYEHnlVeQ7bX3rhE95w1siO6D0_y_VMMX_527PtRhtv5QRBF5N2mjhjtPFDG91FD0G83FBX8hXTJn3oTEjoPm9CPiKKfp5LP_SYwNG30NQaUyJj9dE79cKTlMOj2xAkJd4ExejTOJ5SGb3Gw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db832997e8.mp4?token=Kc7qRL77YtFxKSzgZ4va2FK_u-40aFRfYwxNnrI-YOqGPW4xFfFsuJZZOZatjpcFrLxjsZtS02zoSuaByR3QeOPloBtve9jGNFndNiI5IBAlFx54jsas4CoiB12r7aCNUPMtZZmOKKjNkB1S2rpdwsL7CczG4_u3IWzlZe9kfdfL0Zu7CaRj1CTE-zEoaWGt8RUMDlVYEHnlVeQ7bX3rhE95w1siO6D0_y_VMMX_527PtRhtv5QRBF5N2mjhjtPFDG91FD0G83FBX8hXTJn3oTEjoPm9CPiKKfp5LP_SYwNG30NQaUyJj9dE79cKTlMOj2xAkJd4ExejTOJ5SGb3Gw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حمله رژیم صهیونیستی به ضاحیه بیروت
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/akhbarefori/659260" target="_blank">📅 14:09 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659259">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f5931c2cb.mp4?token=HNacvoBknKi1hR0D9M6xCuJ6k9NcjoBMKDV6rRo0RNUxU-o78Y78ZQnTpbDkf7kCqmONZeHFpP-RE4UGAKUYmOC3qY4Y9hRFBUqVW7ZUO57sDilHTRodiIdr110vLpMRPU3YigjgioaOdVVxgnuN9rWoqju6vYUzVBJjHzoo2dST_NjAAiKuxcnpco1uIPOQ0plcQxk19N9MU-qxiwPQVWRvfBOwa5dluBIrUtH9_rtg3r8vlY4oUfmov0kSAOVfyMwdzQH6Rn9t4ITcazOzfrHvXCsRXPXCyCZoonhvvqWwNwx5pCms6dSKLsWE03CYRu5cs13AimaLVREvots_ng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f5931c2cb.mp4?token=HNacvoBknKi1hR0D9M6xCuJ6k9NcjoBMKDV6rRo0RNUxU-o78Y78ZQnTpbDkf7kCqmONZeHFpP-RE4UGAKUYmOC3qY4Y9hRFBUqVW7ZUO57sDilHTRodiIdr110vLpMRPU3YigjgioaOdVVxgnuN9rWoqju6vYUzVBJjHzoo2dST_NjAAiKuxcnpco1uIPOQ0plcQxk19N9MU-qxiwPQVWRvfBOwa5dluBIrUtH9_rtg3r8vlY4oUfmov0kSAOVfyMwdzQH6Rn9t4ITcazOzfrHvXCsRXPXCyCZoonhvvqWwNwx5pCms6dSKLsWE03CYRu5cs13AimaLVREvots_ng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کارشناس شبکه افق: ترامپ اعلام کرده نه پولی به ایران داده می‌شود و نه تحریمی لغو خواهد شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/akhbarefori/659259" target="_blank">📅 14:06 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659258">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/abR1kVuDH6vjL-6ontejl5ZtchKXvybyhDQsgr8726YGLR_f20IeCSv78efPnMWtMpTRVKjr-poS3iOX1oPTHhnQucv1hoV_ABJu54aqhzFL95jNdf0snaZYOyH-FXhJFNZeHj71KLZsBJ96BK0ZJ897NBIJmrEtCmkWkQhNHaLf-C-DkpDI3qVz5uyamCyXDP4CaevMyOeuRnQJ3J_ztUGtDVEkOaotRE1Aw_H282LjfXZWuitIRydvWgtZTCWSrxux8wYWMYHd3TypLAAlbPjeiZg5NsERX_r2NHR-ejzeMjZxfukpW1tsfULltOQMoBOLHKMZLXDysLj2ML2VjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
حمله رژیم صهیونیستی به ضاحیه بیروت
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/akhbarefori/659258" target="_blank">📅 14:04 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659257">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">♦️
دستگیری ۱۲۶ عضو شبکهٔ اغتشاشات و متلاشی‌شدن یک گروهک تروریستی توسط وزارت اطلاعات
وزارت اطلاعات:
🔹
یک هستهٔ ۴ نفره گروهک تروریستی-تکفیری متلاشی، یک مزدور متصل به سرپل رژیم صهیونیستی و ۱۲۶ نفر از اعضای شبکه اغتشاشات خيابانی دشمن در طول جنگ تحمیلی سوم دستگیر شدند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/akhbarefori/659257" target="_blank">📅 14:02 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659256">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">♦️
ادعای رویترز به نقل از مقام ایرانی:  بر اساس یادداشت تفاهم، آمریکا ۲۵ میلیارد دلار از دارایی‌های ایران را از طریق انتقال مستقیم نقدی، همکاری میان کشور‌های منطقه و خطوط اعتباری مالی، آزاد می‌کند/ انتخاب
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/akhbarefori/659256" target="_blank">📅 14:01 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659255">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tOtMtg9BUnTjrCretkBv48P7ugiYFL_v5PRFdmj4N8JKKgY5jbTqdqzY9yRVwD1QSYbGR75nI65WV1WwXkSM1_npZkrcwvoLRKlh5Y0JefRiqSGG-HF74i5UnfXMKmrXxD3stP89URcs_LE1yNfcvw7zhgAqtXnNamlHQXx68kNHuTrlyaZIAOkZNzI9VHLWfwaT5dyn9H4hmv_9OCZODNWfBYg4k4L-sF3_CyTuXrOwv30PuarROVpgG-Xs6b7QHfIByDsIx7lO4mJL9f17CNUMmnR3Sbp8ZhF5jp6Y2UnR-bF6H6RdzZkN6upG9IeQve4lo_VqZ6BCZRcIrD6mOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تشکیل صف خرید ۴۰ همتی در بورس!
🔹
امروز یک روز تاریخی دیگر در بازار رقم خورد؛ ۴۰ همت صف خرید در پایان معاملات ماندگار شد و حقیقی‌ها با قدرت ۸ همت پول تزریق کردند.
🔹
ارزش معاملات خرد به ۲۰ همت رسید و ۹۷ درصد نمادها سبزپوش و مثبت بسته شدند. در نهایت، شاخص کل با یک جهش ۱۲۲ هزار واحدی در ارتفاع ۴ میلیون و ۸۱۸ هزار واحدی ایستاد./ خبرفوری
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/akhbarefori/659255" target="_blank">📅 13:56 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659254">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآوش</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/22853fbdc2.mp4?token=PM6419WX8aRfQJsQaoc6M5ZULaCEMlQaf3AGdPYAKzt3Nhh8nRqHf6q4V-wJmea6iWIdiO7R8hlDkgF3HhspPI2NJp8exQZbNR9QqBhIaHngXb7sCU2P6_OJD6q3kQxiMsvueJ_aFYYV-Dy8hgXQluBaKrEWTUqdr2lJ36Q2bMINzNdQxqj9UuwGp5wpFKefnznzRktf0-GJ92Mb509coqkcgvW25UfDfzjmOZklbPeVdohjfa3GnzmThlsoIK7wENMaCbhfhhkrqUXFwKnbP0YNaIxdI5KECkwW2c9U1mTzwtH_V7gVMaDEsIR5nL2bGpqm1iVHFUgo9AoQ1Ip0mCLUq3dLY8tqLISXgrryCRbktJs16C-zXvOb_lsi_FBdBb65a3FsPwda5Yg5QHVOSHv2CxdkfyCVPvrIhrUME3ug_s8zNO2IcCiytonu9BHm0Ssq4HcIGm53pP21Ni5bAAVbCfisUwO9d_Udv2Frc10wIjeKnrTbP4UYZvCb1eqxSTnvMrjGuEBUpBQl7-xQ-1vPsUbsz4treUTWWeuq9gul_sdtSNifnG3n7UzBDFlj9WvOIjeuD_xeJLuhuwJ0cf7lTjZvz3vtIhFQas0DAIt96JXO2TJ6jhzaj7k-xUwDFI1NOmerF_uIJ_5HtGjBNYH1csCcxy-CCcoPy3387nI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/22853fbdc2.mp4?token=PM6419WX8aRfQJsQaoc6M5ZULaCEMlQaf3AGdPYAKzt3Nhh8nRqHf6q4V-wJmea6iWIdiO7R8hlDkgF3HhspPI2NJp8exQZbNR9QqBhIaHngXb7sCU2P6_OJD6q3kQxiMsvueJ_aFYYV-Dy8hgXQluBaKrEWTUqdr2lJ36Q2bMINzNdQxqj9UuwGp5wpFKefnznzRktf0-GJ92Mb509coqkcgvW25UfDfzjmOZklbPeVdohjfa3GnzmThlsoIK7wENMaCbhfhhkrqUXFwKnbP0YNaIxdI5KECkwW2c9U1mTzwtH_V7gVMaDEsIR5nL2bGpqm1iVHFUgo9AoQ1Ip0mCLUq3dLY8tqLISXgrryCRbktJs16C-zXvOb_lsi_FBdBb65a3FsPwda5Yg5QHVOSHv2CxdkfyCVPvrIhrUME3ug_s8zNO2IcCiytonu9BHm0Ssq4HcIGm53pP21Ni5bAAVbCfisUwO9d_Udv2Frc10wIjeKnrTbP4UYZvCb1eqxSTnvMrjGuEBUpBQl7-xQ-1vPsUbsz4treUTWWeuq9gul_sdtSNifnG3n7UzBDFlj9WvOIjeuD_xeJLuhuwJ0cf7lTjZvz3vtIhFQas0DAIt96JXO2TJ6jhzaj7k-xUwDFI1NOmerF_uIJ_5HtGjBNYH1csCcxy-CCcoPy3387nI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">افزایش مستمری، تکمیل متناسب‌سازی و پرداخت منظم؛ پاسخ تامین اجتماعی به فشار تورم
ترمیم قدرت خرید بازنشستگان با نسخه ۱۴۰۵ تامین اجتماعی
در سالی که فشار تورم و افزایش هزینه‌های زندگی همچنان بر دوش خانوارهای ایرانی سنگینی می‌کند، تامین اجتماعی با مجموعه‌ای از تصمیم‌ها تلاش کرده تا نشان دهد که از کنار دغدغه معیشت بازنشستگان و مستمری‌بگیران عبور نکرده و همچنان در پی حفظ قدرت خرید و ثبات دریافتی گروه‌های تحت پوشش خود است. افزایش مستمری‌ها، اجرای مرحله نهایی متناسب‌سازی و استمرار پرداخت منظم حقوق، مهم‌ترین نشانه‌های این رویکرد در سال جاری‌اند.
https://avash.ir/n/Rjk
@Avash_media</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/akhbarefori/659254" target="_blank">📅 13:53 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659253">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d-7fGHGYv4mIsNVK5YKwsJUZyJzFaza4ZJfF811aAe9MAZG7eUy5Xe4D0A5V-SsZ4mq6tKkNcD0rYRmQeoa0nxHIWxGDjF_7lfi7kzbQrefj5YtRj9X6fthbDFo31B-IVz1RQ8IzKQIkohIFdL3K2F8bVP12Pvq8ZMC5g3rChtP8Drh-uGhyeuQiKp3Zs48JOYTvloOtRFGMG3uvSRtqauTh6xLD2Ix8_r3hIARckbL6AcN1Q6qbauWVOxWpriMdlonw4cYUFCEtl0vu3CYnm0a8Xd8MOIN9VxvO1vrIy1giWFWTSQtQHdkL3VbQFza2lBub4Huq3DNTYYTX6neBzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کاربر توییتر: چرا باید کودکی مثل این مجبور شود بقیه عمرش را بدون دست و پا زندگی کند، فقط به این خاطر که یک سرباز اسرائیلی دنبال سرگرمی بوده؟ واقعاً دلخراش است که چطور این همه وحشت بدون هیچ مجازاتی می‌گذرد. کوچولو، متأسفانه، انگار دنیا برای تو اهمیتی قائل نیست
😔
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/akhbarefori/659253" target="_blank">📅 13:52 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659252">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3eeb7fe4ee.mp4?token=K9-qYEfE3nY674_2-D4VI_uB2YeJh8PSyco_Gdm7mAh9yBlp514_RBIGFkceeafcvmalpfEjNQ4M242MoeQ40fvKcEYXLHXYT_1Di9JYyyjCg-lG7dhnp799vqDOHmivOLYV3wD4AJhyfmOG23oPwzke_Zl0dpTS7-KdIhfmsEiJd5nVez_rihNTa-VDH-3H3p3nYDYyitsskn0C1Tw5HgkNvG4L8JzqOAknBMnUWeNkXLERmewd33rPCkvkl4hAdyU4uw-ra7OIhsxNLDvSn1NorSokaEYHBGn7zfEZY2wZpC-NQEzkjNOL3BvqGl_AvEogM-6KvhLJS92-pkXWvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3eeb7fe4ee.mp4?token=K9-qYEfE3nY674_2-D4VI_uB2YeJh8PSyco_Gdm7mAh9yBlp514_RBIGFkceeafcvmalpfEjNQ4M242MoeQ40fvKcEYXLHXYT_1Di9JYyyjCg-lG7dhnp799vqDOHmivOLYV3wD4AJhyfmOG23oPwzke_Zl0dpTS7-KdIhfmsEiJd5nVez_rihNTa-VDH-3H3p3nYDYyitsskn0C1Tw5HgkNvG4L8JzqOAknBMnUWeNkXLERmewd33rPCkvkl4hAdyU4uw-ra7OIhsxNLDvSn1NorSokaEYHBGn7zfEZY2wZpC-NQEzkjNOL3BvqGl_AvEogM-6KvhLJS92-pkXWvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کارشناس شبکه افق: پاکستانی‌ها برای میانجی‌گری به ایران نمی‌آیند، بلکه مرتب پیام تهدید و‌ ترور می‌آورند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/akhbarefori/659252" target="_blank">📅 13:52 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659251">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aX2KiT4HeL-fN8pJOAAjsReSlFtMUXGNUCvTrx4MvJiIN9iqJdf6sb7Llb2JbU0df6CqWVRj3G_Aa3WtKpUf5G2hQKcIlBQDyQXwySbKwtVGtmLhF3r1A54LT19_ZwVsFujKWw2bsPN_rHazzaJwvxAItOYoNhqgtfK2NCoXoM8z7feDTdcffPEwESz0Nv9ZRQdQI8i-xE8EojCTW_VeErK-g1uqmkGB96oqS4WJjRBceGIckEK_NhePFEFvCovTNge1U_csWmldCe1uUHL8s_GYMoOBpykRS3ENENN1Cnqk2o0ppu-ypWUmWuaGnney5hoV_2sCiRayE90zoImtKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📣
اگر به‌دنبال تبلیغاتی مؤثر و دیده‌شدن واقعی هستید
این کانال آماده همکاری با مجموعه‌ها و برندها و تیم های تبلیغاتی بزرگ است
🎯
مخاطب فعال |
📊
بازدید بالا |
💼
همکاری حرفه‌ای
📩
برای رزرو و هماهنگی پیام دهید
👇
@newsadmin</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/akhbarefori/659251" target="_blank">📅 13:49 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659250">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromتیتر تجارت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OhhBPmUG27Duy_sAoFaMip9eudxc-2o4o585dbohSEk5JFdVgM1IKLnAN5dJcOXQxFmmtMhp48AL-3JCRchj4TpZOhojLHWzdYgEV2ovOG9cUfXm6v0VwbtfkHfUtaTYc7F5m4kCIb_IxXJk2PUcMPNiJ3tuyZgxMHpOxkzLkPwmh2wGBBYx3wefgHdA8n7zw-PX3MRgwA-ETPBPjG5W6GA7QC07kUSOPByJgRKWWYEvu-ecBmCStB_nrj-_PbC5zkMfxpymbMcSrWluUoiS5JO2E7Iew0PreG0DZPrL_Xj-QLr0CI4mldI0Uzo5iTJeEOso2-QkyJ1KXrGVq9gJyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
#نبض_بازار
| قیمت طلا و ارز؛ امروز ۲۴ خرداد ۱۴۰۵؛ ساعت ۱۳:۳۰
🔹
افزایش خوش‌بینی نسبت به توافق احتمالی ایران و آمریکا، بازار طلا را وارد فاز اصلاحی کرد.
🔹
بازار طلا امروز با موجی از ریزش قیمت‌ها روبه‌رو شد. هر گرم طلای ۱۸ عیار در کانال ۱۷ میلیون و ۱۰۰ هزار تومان نوسان می‌کند و سکه نیز در تمام قطعات عقب‌نشینی کرده است.
🔹
هم‌زمان دلار پس از مدت‌ها از مرز حمایتی ۱۷۰ هزار تومان پایین رفت و در محدوده ۱۶۹ هزار تومان معامله شد؛ عاملی که فشار نزولی را بر بازار طلا و سکه تشدید کرد، در حالی که اونس جهانی روی سطح ۴۲۱۹ دلار بدون تغییر مانده است./تیترتجارت
@Titretejarat</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/akhbarefori/659250" target="_blank">📅 13:48 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659249">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">♦️
والیبال لیگ ملت ها؛ صف آرایی ایران برای بلژیک، امروز
🔹
تیم ملی والیبال ایران از ساعت ۱۷:۳۰ امروز در چهارمین دیدار خود در مرحله مقدماتی لیگ ملت‌های ۲۰۲۶ به مصاف بلژِیک می‌رود.
#ورزشی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/akhbarefori/659249" target="_blank">📅 13:47 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659248">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
بخشایش: احتمال آزادسازی ۱۲ میلیارد دلار و لغو تحریم‌های نفتی ایران
احمد بخشایش، عضو کمیسیون امنیت ملی مجلس در
#گفتگو
با خبرفوری:
🔹
در این تفاهم تنگه هرمز باز می‌شود و به خاطر رفت و آمد کشتی‌ها تعرفه‌ای اخذ نمی‌شود، اما بابت خدمات بیمه‌ای، سوختی، محیط زیستی و...ایران می تواند عوارض را دریافت کند
🔹
به احتمال قوی ۱۲ میلیارد دلار پول‌های بلوکه شده ایران در قالب کالاهای اساسی و بهداشتی دریافت می‌شود، اما ایران اصرار داشت این ۱۲ میلیارد را نقدی دریافت کند و آمریکا گفته است در قالب کالای اساسی؛ در این مسئله اختلاف نظر وجود داشته است.
🔹
پول را متناظر با انجام تعهدات ایران در طی ۳۰ روز یا ۶۰ روز آزاد می‌کنند. بعد از ۶۰ روز بحث ایران است که روی غنی سازی هسته‌ای صحبت شود؛ ایران قبول کرده است آن ۶۰ درصد را زیر نظر آژانس در داخل رقیق کند.
🔹
همچنین روی بحث ۴۰۰ کیلو اورانیوم آمریکایی‌ها می‌گفتند به کشور ثالث منتقل شود، اما ایران می‌گفت از ابتدا در داخل می‌توانیم آن را رقیق تر کنیم. فکر می‌کنم لغو تحریم‌های نفتی ایران انجام می‌شود، اما تحریم‌های ثانویه و تحریم‌های کنگره شاید ماندگار باشد.
@Tv_Fori</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/akhbarefori/659248" target="_blank">📅 13:43 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659247">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">♦️
امضای ۲ مدیر دولتی غیرقانونی اعلام شد
🔹
طبق نامهٔ حسابرس دیوان محاسبات به صندوق بازنشستگی کشور، تعهد و امضای مدیرعامل‌های «شرکت آتیه صبا» و «صنایع شیر ایران» واجد اشکال قانونی است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/akhbarefori/659247" target="_blank">📅 13:42 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659246">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">♦️
ادعای
العربی الجدید: تهران هنوز توافق را تأیید نکرده است
العربی الجدید:
🔹
ایران هنوز تأیید نهایی خود را برای یادداشت تفاهم اعلام نکرده است.
🔹
به گفته یک منبع آگاه ایرانی، احتمال امضای توافق در روز یکشنبه منتفی است و بررسی‌ها در داخل ایران ادامه دارد؛ هرچند ممکن است تهران امروز نظر نهایی خود را اعلام کند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/akhbarefori/659246" target="_blank">📅 13:41 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659245">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/420013fdd3.mp4?token=SZ7TtaFhbhdwUzwpnpAZulBTJago5ZUe03Zoy2eDg8eqwFDuw5HAfYrBUaLwxknxnpxlAI4TBNJFRWfjl9Tt_fJ3rqUrOIxShss0QqCw-GISU7-NeiGIZbAf_vOmeTGL3upSGGwt6cJ5QuHfzxlJ45Hpi-ztNmZdIg22S-EH9laDLkJOZvK8jh1lLKfE6_lhyvOo3OuxFpFqdKn8U_VpkckjC2wAPiYPugAVBeQi8imD_5nwign1nvM3miYAlvpsjlAo7Mtc4DYfeK8lZoPmQkwP7IBrPXOiGiYC27HFhrxUtx4-OIudqMxHy0AO_-aZeCweHyiRQshiSpu_48ZYgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/420013fdd3.mp4?token=SZ7TtaFhbhdwUzwpnpAZulBTJago5ZUe03Zoy2eDg8eqwFDuw5HAfYrBUaLwxknxnpxlAI4TBNJFRWfjl9Tt_fJ3rqUrOIxShss0QqCw-GISU7-NeiGIZbAf_vOmeTGL3upSGGwt6cJ5QuHfzxlJ45Hpi-ztNmZdIg22S-EH9laDLkJOZvK8jh1lLKfE6_lhyvOo3OuxFpFqdKn8U_VpkckjC2wAPiYPugAVBeQi8imD_5nwign1nvM3miYAlvpsjlAo7Mtc4DYfeK8lZoPmQkwP7IBrPXOiGiYC27HFhrxUtx4-OIudqMxHy0AO_-aZeCweHyiRQshiSpu_48ZYgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سقوط مرگبار یک دختر در دره ای در برزیل بر اثر اشتباه پرسنل مرکز تفریحی
🔹
در ایالت سائوپائولو برزیل، یک دختر هنگام اجرای طناب‌جهش (نوعی پرش با طناب) جان باخت؛ سازمان‌دهندگان این وسیله تفریحی، تجهیزات ایمنی را به او نبستند و او را به داخل دره پرتاب کردند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/akhbarefori/659245" target="_blank">📅 13:37 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659244">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفوری گرافی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DWCjw0X8ZR7nU8H4VqM7NxPRwpNNrDtQ6qwDwwPieaDZ7kV4DZRxCZinEomYGjCyAxp4VLDM4hPHxP-eQweaFTRl_lE-xwP9jXEHArSI7lVFvTEUdhbk5efbzca_FMvE07Bz3JIVSdwAmBdrUi1id_jutZ0STNmEj6qu9qnihtj3rtANdvsj8CM4t_bDYRn5PL5HH1F6skk4FxtK8MnQ6V86AdUhcKxEQEyaGJFjDxk4-eqOrGiQqbDMsauDWpHl1BKbUREc9SIlI6Gqrq9iBYXWXKs5ScokjocQNk0W9m0Lo73q94ktlDIDRj3NhxQI28bkoMGhU47PFX07H8DqYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تعداد خودروهای فرسوده ایران به بیش از ۲۲ وسیله نقلیه رسید!
#اینفوگرافی
@Fori_Graphi</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/akhbarefori/659244" target="_blank">📅 13:34 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659243">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">♦️
خروج ناو هواپیمابر شارل دوگل از منطقه
🔹
ناو هواپیمابر فرانسوی «شارل دوگل» پس از پایان دوره مأموریت ادعایی خود در مدیترانه شرقی و دریای عمان، در حال بازگشت به پایگاه نظامی «تولون» در فرانسه است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/akhbarefori/659243" target="_blank">📅 13:31 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659242">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WdO656ujeZGWWKAh7gP4ZTaAYVksjgeCH92MK66HjILv15CWxTQKEJZmGky7E6vSvOXsxsGbDCyqoZ9VIzyf2W_UyERBlow2szSKH5HM5SwKZ1KW3wP920ugHp79BaB_mQdJXyzDPkBgPxUoYng7vd8CrwMI4WkLFE81ImNFuIacc3tBJREyb_09QlKOgMsnxhM5u4y_9SdmuMxVOue9BdBxG_wq0YOhaTonaooQ_0x2m8cjzZgeo6XhfFXvySouqXNqQaH7LElSmGwadiAB0WlYxb1lSrCKztwcs6lM8ouPGd3tI1Iv544lO51cjV4cbGyuWzNPuf2aryL4COF1PQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رئیس قوه قضاییه: دشمن به مخدوش کردن وحدت و انسجام ملی چشم دوخته است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/akhbarefori/659242" target="_blank">📅 13:29 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659241">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
حاجی‌بابایی: دولت وضعیت استخدامی معلمان را تعیین تکلیف کند.
🔹
آموزش و پرورش: امتحانات نهایی از ۲۱ تیر برگزار می‌شود.
🔹
شنیده شدن صدای انفجار ناشی از مهمات عمل‌نکرده در تبریز/جای نگرانی نیست.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/akhbarefori/659241" target="_blank">📅 13:25 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659240">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2583a92d5f.mp4?token=vEHOlmoQr3FYU1hgpiy0yyTKBmwJ2MkygIVkYQVAOoHg3bLwYgsp2wYzUvEEUHokTb9dACVZm56hBcfTYYt_ua6FxsDF_3d12i6kZY-lxC1g3K9VJjgs-_ASMVaud2-fHXQSK5_2GQulL3KZ6_2GBSx_m7zo22F7KrSfEwqHTPr9Q2QJiuJYegZmX64rLCq1_UzXe7kvYNhrCPh_7iLxB6v2a8dukCghgYuphbosag0TrTPZuUhowiannsG7dcLicaV6BCD39leizwjZFRhcQzemgX7l-Og4rgYfpRAm1aZ5mTO1Wjug-5zQXMoYXpMJivBqHa8GwUBdVO8Fzp2JYRM5UvZVfPZs-nLD3db-4SpPoT9wsp5TV-KHWQPsWATy3iaGSsbC0orAA1Q5ze5021eH6BhRCRdbBfut3XByg2XRu_p2wZRtkylN5uoEzJaAnz0iv5-UyYMBK81jsKxlMYhRonpt56uCY9GvXbBH6kQdP_3w5YZKe7oM2-djBf_OHVDmPw-KgW9BM7VScDPS5_h7-YrN1JUjMpDlNGL8VP5oJkXOPW3mHAkjP2vl6sXN2jO3TrOXsvjnQbWI1FUfEwlIt0_R2y2Rgw0j-i7w5UClB7XDKEMYTdPw75MsCsnsjQTs3PTwKfVUIKgJ8QDR1pNIlDglfpXRJ-gPQAvhI18" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2583a92d5f.mp4?token=vEHOlmoQr3FYU1hgpiy0yyTKBmwJ2MkygIVkYQVAOoHg3bLwYgsp2wYzUvEEUHokTb9dACVZm56hBcfTYYt_ua6FxsDF_3d12i6kZY-lxC1g3K9VJjgs-_ASMVaud2-fHXQSK5_2GQulL3KZ6_2GBSx_m7zo22F7KrSfEwqHTPr9Q2QJiuJYegZmX64rLCq1_UzXe7kvYNhrCPh_7iLxB6v2a8dukCghgYuphbosag0TrTPZuUhowiannsG7dcLicaV6BCD39leizwjZFRhcQzemgX7l-Og4rgYfpRAm1aZ5mTO1Wjug-5zQXMoYXpMJivBqHa8GwUBdVO8Fzp2JYRM5UvZVfPZs-nLD3db-4SpPoT9wsp5TV-KHWQPsWATy3iaGSsbC0orAA1Q5ze5021eH6BhRCRdbBfut3XByg2XRu_p2wZRtkylN5uoEzJaAnz0iv5-UyYMBK81jsKxlMYhRonpt56uCY9GvXbBH6kQdP_3w5YZKe7oM2-djBf_OHVDmPw-KgW9BM7VScDPS5_h7-YrN1JUjMpDlNGL8VP5oJkXOPW3mHAkjP2vl6sXN2jO3TrOXsvjnQbWI1FUfEwlIt0_R2y2Rgw0j-i7w5UClB7XDKEMYTdPw75MsCsnsjQTs3PTwKfVUIKgJ8QDR1pNIlDglfpXRJ-gPQAvhI18" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خلاصه بازی جذاب برزیل و مراکش
🔹
🇲🇦
1️⃣
🏆
1️⃣
🇧🇷
🔹
طرح
طلای
بیمه زندگی
پارسیان
▪️
آینده‌ای طلایی با سود طلایی
▪️
بیمه‌ای متصل به صندوق طلا
#بیمه_پارسیان
#بیمه_زندگی_پارسیان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/akhbarefori/659240" target="_blank">📅 13:20 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659239">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">♦️
کنکور سراسری ۲۹ و ۳۰ مرداد برگزار می‌شود
وزیر علوم:
🔹
کنکور سراسری سال ۱۴۰۵ به صورت قطعی در روزهای ۲۹ و ۳۰ مردادماه برگزار خواهد شد و با توجه به زمان‌بندی جدید، به احتمال زیاد دانشجویان جدیدالورود از نیمسال دوم تحصیلی وارد دانشگاه‌ها خواهند شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/akhbarefori/659239" target="_blank">📅 13:16 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659238">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">♦️
منبع آگاه: تصمیم نهایی تهران دربارۀ تفاهم‌نامه در دست بررسی است  یک منبع آگاه:
🔹
ایران هنوز تصمیم نهایی خود دربارۀ تفاهم‌نامه پیشنهادی را اعلام نکرده است.
🔹
بررسی ابعاد سیاسی، حقوقی و فنی پیشنهادهای مطرح‌شده همچنان ادامه دارد./فارس
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/akhbarefori/659238" target="_blank">📅 13:09 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659237">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">♦️
هشدار سازمان بازرسی به بانک‌های دارای عملکرد نامطلوب در پرداخت وام ازدواج و فرزندآوری
؛
اخطار قانونی صادر شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/akhbarefori/659237" target="_blank">📅 13:06 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659236">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ei8PXk53ubTNRVcCB7WARMxxUsmM5HLA2frhtU0Ke7jLRXPzJe0UUdt2tXrKSs6bZDQ8dAx829j-z_QMdYwxHBnlwqtiKh8OSye9QuLzol3b_1ZSoayvzEM0zmo7QN84_OROOH8wUcvcNXLz5_gpBlCfgmNEU-xBE32J2_ao1ui-0Xgg19HwoqoP5P7UYWUShBCv6txcORv83XEmdOYUDxhwjWzOHayjkEDpM_x7jO8VS23nz-5TkD-UrfNmBFM5GQADnIpNE1mNnfzH5raXgXCA4mLbBO0xOnB0j7eZf-EqkKHIuIvpnIXNlKefxTnHoTiJ3VW8bARAuqf27yp8eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
۴ دقیقه‌ای که آب ۳.۵ میلیون نفر را تأمین می‌کند
🔹
با کاهش ۴ دقیقه‌ای استحمام یک میلیون نفر، ۱۱.۸ میلیارد لیتر آب ذخیره می‌شود؛ معادل نیاز اصفهان و شیراز. در جنگی که منابع ما با فشارهای اقتصادی هدف قرار گرفته، اقدامات خردِ جمعی را در خنثی کردن نقشه‌های دشمن دست‌کم نگیریم.
#سنگر_آب
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/akhbarefori/659236" target="_blank">📅 13:04 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659235">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BM5JaZDX1f64SjxgYNlfaP0qCXHEtOE0plGwXI1smrkvWONbHu2sdE6HhssHQxVrmTWzrPQGHMM4uTJCdngoxBkrYP6a_Nb7rxJxZPEIIzZnZYttNjH0fUZKe5PxHpvr9EDPbxKIi4HEEgrFJyePJVnEEdVOQ2HAPOWl3RpcILKRz6VhuRKRhg3z1tc0sd50yDt4nC0Lay3EOdmPOKTlpEJk8c4WW9eErXEJLQgCt9qIs9YR0cal_0QqkWKyOjAGzvcTB1Cu6wS-zPYkyFP4kNhorXSRF-jM1yyXbsecH5jWfE6KPhDqHnNnjVpUWWLzcEs-aVhENgNh2OwI_XFEUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قطر با تساوی مقابل سوئیس، اولین امتیاز خود را در ادوار حضور در جام‌های جهانی کسب کرد @AkhbareFori</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/akhbarefori/659235" target="_blank">📅 12:58 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659233">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9bfd5ffba2.mp4?token=a0Tp5tVozcOF_HfftgQx6X-I25Y-xoGnBP7ixDFs4h064hneuN5Y92TFzFnQ1akk-6qmOBlnb3OaSo55NBB8QBE83JQXF8ujLj_zQvH7cUjouUJZ4xsGbZLhADD0phl9ASlYU8MDI-tUMu1Rt_ej60M3fOscZfTkaHu3HoWpCO00EZZZNlEp8IiHsk7gBRCcM_wy0Q1qs-cALYM-T_P5OUeCaJXiZmgGvG4R4c_4wL3eRDwTfuHRwxk9FKYYx9HEHSMNUMEaDMOpTWcdoq1VZURPBG-Y3S46_zsx_Qh70p1n1a3_j2Og1UuTd_UQiW4DoSu5HyexUJp9wWRSaNQ_TQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9bfd5ffba2.mp4?token=a0Tp5tVozcOF_HfftgQx6X-I25Y-xoGnBP7ixDFs4h064hneuN5Y92TFzFnQ1akk-6qmOBlnb3OaSo55NBB8QBE83JQXF8ujLj_zQvH7cUjouUJZ4xsGbZLhADD0phl9ASlYU8MDI-tUMu1Rt_ej60M3fOscZfTkaHu3HoWpCO00EZZZNlEp8IiHsk7gBRCcM_wy0Q1qs-cALYM-T_P5OUeCaJXiZmgGvG4R4c_4wL3eRDwTfuHRwxk9FKYYx9HEHSMNUMEaDMOpTWcdoq1VZURPBG-Y3S46_zsx_Qh70p1n1a3_j2Og1UuTd_UQiW4DoSu5HyexUJp9wWRSaNQ_TQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کمدین آمریکایی: تنها کاری که آمریکا می‌تواند در مورد ایران انجام دهد این است که دمش را روی کولش گذاشته و فرار کند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/akhbarefori/659233" target="_blank">📅 12:54 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659232">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb3ceaef5a.mp4?token=jOoh34hPU16Rxdw_ePKClTSZfn1VaUkiBYVgoLcICc4vqckSvx8mvcX011okDZq_79_9mh6tVIWoHruj2bEu26fOJPR2Q_HfXm6Y4siuntpJ4pRjFhTl9NtkHXOHrvzwQnJnNKRhonmm6IiPA5uUp5FIaKT3oikeg_tT_V-I6-SCAT5pZnZfnZ9ILJqaHw14QjW_z6xezCMGZuLtMWYW-nKPRlv25m4UuJF6Uixb05oxtUCQnIj8BZouP_apBCBotd829n4RXld3oFqoxHOs_41HFQKi6iykEa7an40LHi5bKl1r4VAL5i71o6j_elPdp25KaIM59rwP-x3Ijf6CyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb3ceaef5a.mp4?token=jOoh34hPU16Rxdw_ePKClTSZfn1VaUkiBYVgoLcICc4vqckSvx8mvcX011okDZq_79_9mh6tVIWoHruj2bEu26fOJPR2Q_HfXm6Y4siuntpJ4pRjFhTl9NtkHXOHrvzwQnJnNKRhonmm6IiPA5uUp5FIaKT3oikeg_tT_V-I6-SCAT5pZnZfnZ9ILJqaHw14QjW_z6xezCMGZuLtMWYW-nKPRlv25m4UuJF6Uixb05oxtUCQnIj8BZouP_apBCBotd829n4RXld3oFqoxHOs_41HFQKi6iykEa7an40LHi5bKl1r4VAL5i71o6j_elPdp25KaIM59rwP-x3Ijf6CyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
انیمیشن با نقاشی دیواری بر پلی در کالیفرنیا!
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/akhbarefori/659232" target="_blank">📅 12:47 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659231">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">♦️
مشکل خدمات بانک‌های تجارت و صادرات رفع شد  شرکت ملی انفورماتیک:
🔹
طبق آخرین گزارش‌ها درپی اختلالات به‌وجود آمده در ۴ بانک ملی، صادرات، تجارت و توسعه صادرات، مشکل خدمات کارت های بانکی بانک تجارت و صادرات رفع شده و تراکنش‌ها با موفقیت درحال انجام است.
🔹
موضوع…</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/akhbarefori/659231" target="_blank">📅 12:41 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659230">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FO-VDV_JbByoNHlMlgc38K-FREOQRagFFC_CuitUClzCj0vBj6jm2lmQohjuKIvw_RSu4GfD33OsWlA1YBORDN_eQNrR9YFfJo5ioRhzmfvv4tiS-7mKceAV1mL-WVxPTPRUvFujYibgWLtruWtpYSz6c6iDbCnIjY4eHg7bUl03MUBUjRbzKxSXNoiKDQaKlBiL5WYw_V4iij8HrQgIyTg8QWpzH9w5qqHl0Yy5CDvo4YHZ_qsUo7zk8J3BOSfZ1CfsK-aaoNJW0V3lCdIFWhaIhRcAl33tGOQgQt-i9AnkZw33HeZaNcjQcJkSH4XyYPb0pUFkEi5Y6PJHRnJxXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بورس از ۴.۸ میلیون هم عبور کرد
🔹
شاخص کل بورس امروز با رشد ۱۲۳ هزار واحدی به ۴ میلیون و ۸۱۹ هزار واحد رسید و یک رکورد تاریخی جدید ثبت کرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/akhbarefori/659230" target="_blank">📅 12:38 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659226">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ae92df0369.mp4?token=MRr47eVQBuCLuAklazw9aRud7NeprxU8YzQzH_ov7AL-Ih1i4fWsWluuCCoemzKQrHBN3Bt0sTxBzZellxRmzv79gVwOv1OTXDw5r6FQ4aEZxRs8OnyY0FvpvdsMgxD4GYHGXivF7gxZanbhYoiX9EiSZgkAAJo6nnoUbD_5713CcuAKtq1Sm6u9Q1J1z89J3QBFxhBVJXj5lVoj6Qz3UACULkyGruzdzWKnpkIBgSW28nM6aIa2Jf-8MIQWtrCdelKeqadjnCDT88sYAI01wmU1ceHD7YoHFJQp8IewHd-yfxjdNmqjjtrsnMOSlmz6OfFg7WPGBeJQbyXXSTr4Dg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ae92df0369.mp4?token=MRr47eVQBuCLuAklazw9aRud7NeprxU8YzQzH_ov7AL-Ih1i4fWsWluuCCoemzKQrHBN3Bt0sTxBzZellxRmzv79gVwOv1OTXDw5r6FQ4aEZxRs8OnyY0FvpvdsMgxD4GYHGXivF7gxZanbhYoiX9EiSZgkAAJo6nnoUbD_5713CcuAKtq1Sm6u9Q1J1z89J3QBFxhBVJXj5lVoj6Qz3UACULkyGruzdzWKnpkIBgSW28nM6aIa2Jf-8MIQWtrCdelKeqadjnCDT88sYAI01wmU1ceHD7YoHFJQp8IewHd-yfxjdNmqjjtrsnMOSlmz6OfFg7WPGBeJQbyXXSTr4Dg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ذوق‌ کردن زلنسکی از حملات پهپادی به روسیه
🔹
رئیس جمهور اوکراین با انتشار یک فیلم اعلام کرد که پهپادهای این کشور در عمق خاک روسیه به یک تأسیسات نفتی در یاروسلاول حمله کرده‌اند و این عملیات باعث اختلال در ۶ فرودگاه و اعلام هشدار حمله هوایی در ۲۸ منطقه روسیه…</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/akhbarefori/659226" target="_blank">📅 12:35 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659225">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa4dd5e434.mp4?token=DtVhXG7jXkEFez0P87llOaXgIeifl3c7pqOqqr-dsupr40MHSwBggVx26vnZ329WPDPOgXDCvTTqcocCMUAimxJvKUif0BYIycWme86xvnuRK1dOIRBzIjILdurvVhTzvoPfA1LbcLaiNKn9DGsrAIrsZOxLziwDzm8C3eXPuJdUm8SwiYklyLyOw6lHoBokZm2ln_GSvy1_mWghQE2X96vMEm3vQUPcYl0Nkk_hzGmYHNu9o2IlnltVyeKNCHdk9-N_cdkEnYfF7-RhyC-NBnmRur-BkDBamPWXL4Dp3zJVliYBJrR4Q18blF7-AICQ6C9szLRCdoLhm5Ku2u3CwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa4dd5e434.mp4?token=DtVhXG7jXkEFez0P87llOaXgIeifl3c7pqOqqr-dsupr40MHSwBggVx26vnZ329WPDPOgXDCvTTqcocCMUAimxJvKUif0BYIycWme86xvnuRK1dOIRBzIjILdurvVhTzvoPfA1LbcLaiNKn9DGsrAIrsZOxLziwDzm8C3eXPuJdUm8SwiYklyLyOw6lHoBokZm2ln_GSvy1_mWghQE2X96vMEm3vQUPcYl0Nkk_hzGmYHNu9o2IlnltVyeKNCHdk9-N_cdkEnYfF7-RhyC-NBnmRur-BkDBamPWXL4Dp3zJVliYBJrR4Q18blF7-AICQ6C9szLRCdoLhm5Ku2u3CwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویر حزب‌الله از حمله به سایت نظامی «بلاط» متعلق به ارتش رژیم صهیونیستی
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/akhbarefori/659225" target="_blank">📅 12:30 · 24 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
