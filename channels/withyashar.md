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
<img src="https://cdn4.telesco.pe/file/USzuQ-_WMO9EQ7m1ivOsIlqfykWAj9Uamf8sRrY3kYd5GROKWz5NpHCF33fkprbMclC55NaplaLw-VuVdXp6rcJsLLrLlkvS2rvXMbJy6E3PwfPYEpb3Eo_Nn1Wg6bK47IoXIyzy6WDY6kK7bRRTa0EFOwMPeinOpYwvQ1eiLu85racfOh0yNTzrBwHieQshJBNYxDmb2h6nxOU6AdKMbLCAx9Z-pik0-FteLpI9E6QKzpx97ZGwBtqscRy05o5wSQ1h-x4_-zw2H1_lSuKVqFKLBh1hFN1aOnqJG-nM-Vey-Usg54YnVt7YPXmUwq-eCNxtYQGgud1DLaRuad2yHQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 269K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیلinstagram.com/yasharDonatePaypal :https://www.paypal.com/paypalme/yasharrapfaUSDT trc20: THebHKGpmnhWZzNZAbdSdr4fUAK3qkxDgkhttps://X.com/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-02 00:22:47</div>
<hr>

<div class="tg-post" id="msg-12029">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-footer">👁️ 6.27K · <a href="https://t.me/withyashar/12029" target="_blank">📅 00:17 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12028">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-footer">👁️ 8.33K · <a href="https://t.me/withyashar/12028" target="_blank">📅 00:15 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12027">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">moamelegari-trump(@withyashar).pdf</div>
  <div class="tg-doc-extra">23.5 MB</div>
</div>
<a href="https://t.me/withyashar/12027" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">کتابی از دونالد ترامپ یکی از بحث برانگیز ترین شخصیت های سیاسی جهان.
رئیس جمهور آمریکا دونالد جی ترامپ ، جهان بینی حرفه ای و شخصی خود را در این کتاب جذاب و خواندنی بیان می کند، روایتی دست اول از ظهور مهمترین معامله گر آمریکا.
دونالد ترامپ : هنر معامله گری
🌐
@withyashar
🌐
instagram.com/yashar</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/withyashar/12027" target="_blank">📅 00:11 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12026">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f3db1344e8.mp4?token=vLDFO0-5v3Bb-SOCBLcpP7lt87_wX1bGnutpa49SIHRwlFbhG-mC3-MbrE2Ys-UmQu52KVxhv3UiDvHVlm2a1HL0zvyarKG8NLpLXUezZ-xom_PPwa-CF_d-gGLSQl9Lhvn_Oe67T9cJdLqH4gUj__0AbX_iD4gCuyqIGlU05Vcf7ALMC--Ky-vdZ5mCFRQnDMIWiEqWL8FxtwcXYulRI9U2-wD-X4aQPuvg-zDxO-ZiSe6Z2X2ivEWqeV374ZFvuRrwvfPLPMASMMSUilsYYT6a2Qs1aSSQ8umRJrmWbPPNAqBRDJNOv9ib5LgHELq7QIbuSeyENN5aUi7xArm-MA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f3db1344e8.mp4?token=vLDFO0-5v3Bb-SOCBLcpP7lt87_wX1bGnutpa49SIHRwlFbhG-mC3-MbrE2Ys-UmQu52KVxhv3UiDvHVlm2a1HL0zvyarKG8NLpLXUezZ-xom_PPwa-CF_d-gGLSQl9Lhvn_Oe67T9cJdLqH4gUj__0AbX_iD4gCuyqIGlU05Vcf7ALMC--Ky-vdZ5mCFRQnDMIWiEqWL8FxtwcXYulRI9U2-wD-X4aQPuvg-zDxO-ZiSe6Z2X2ivEWqeV374ZFvuRrwvfPLPMASMMSUilsYYT6a2Qs1aSSQ8umRJrmWbPPNAqBRDJNOv9ib5LgHELq7QIbuSeyENN5aUi7xArm-MA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">من باهوش‌ترین آدمی هستم که تا حالا باهاش روبه‌رو می‌شید
✌🏾
@withyashar
یاشار : چقدر بجا و به موقع این حرف رو زد !!!</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/withyashar/12026" target="_blank">📅 23:57 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12025">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">@withyashar
حسود هرگز نیاسود</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/withyashar/12025" target="_blank">📅 23:50 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12024">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/848c770050.mp4?token=IolNsP3mW2FTxrpFHBSfMA4X5up14dCIzd1rziznz8JR0tJzCi3apWYT4nOBSONy1qbz_bEgSExMvDY8uwLy0P7cN70jnW5h9VLHJ-FB8Okh-2o2TGrbieBMIUv2vQ7PFATttvQusIHtMNLxP8ZmSkItUJ3cfJGJa407VT1QCk75_sn0RrvA8PB4dFGVd2w9S0KBdHV00-zu1R-Z0jnfmt-s4W_TqYLaziQ3EzNxntyEE4aIxUbPeTFR47JLYYe98pPI0bfZIPCdoQL3qVL9Iopgh48Olv17p12kbE7qzIRarHH9ci-eQ-eRYb951Oe71na3txrwskjIkEPF8uzf8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/848c770050.mp4?token=IolNsP3mW2FTxrpFHBSfMA4X5up14dCIzd1rziznz8JR0tJzCi3apWYT4nOBSONy1qbz_bEgSExMvDY8uwLy0P7cN70jnW5h9VLHJ-FB8Okh-2o2TGrbieBMIUv2vQ7PFATttvQusIHtMNLxP8ZmSkItUJ3cfJGJa407VT1QCk75_sn0RrvA8PB4dFGVd2w9S0KBdHV00-zu1R-Z0jnfmt-s4W_TqYLaziQ3EzNxntyEE4aIxUbPeTFR47JLYYe98pPI0bfZIPCdoQL3qVL9Iopgh48Olv17p12kbE7qzIRarHH9ci-eQ-eRYb951Oe71na3txrwskjIkEPF8uzf8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ : اعتراض کردن تو تجمع‌های من خطرناکه من چیزای خطرناک دوست ندارم دوست ندارم ببینم کسی کتک می‌خوره پس این کارو نکنید
@withyashar</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/withyashar/12024" target="_blank">📅 23:47 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12023">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ed9df0fb0.mp4?token=IbgBF4vSPCcrQgr-59X6jc6WMGWACkq7i0VLFDaOfvwq5tMjOcZIovC1u9cU0TjZLUneiEYBYUqfE9WPk7jnYxB4L3Mwecp3_lXiykoEDsmktb9R58g1jSn3q3fuDiKq87i0cVG5uhgnzT5Y-jiXaDzmkqmt14ZHZW3eN6voWVfFcwi4cyrc9z2ElTobEzCN-7liBvb6ifiRYsXeJX4rs6DNnQ-tutn2VIJyIp0g873hzZp2bG3SBiNLB0kqh1SgfenEzUs1eNbyR6Wb2Gau3m152YS1sWfddYnzqv_shtuSPbt8JWATQRJWzjGhxGSdHZpveu_lNiHxNcAGq3oeYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ed9df0fb0.mp4?token=IbgBF4vSPCcrQgr-59X6jc6WMGWACkq7i0VLFDaOfvwq5tMjOcZIovC1u9cU0TjZLUneiEYBYUqfE9WPk7jnYxB4L3Mwecp3_lXiykoEDsmktb9R58g1jSn3q3fuDiKq87i0cVG5uhgnzT5Y-jiXaDzmkqmt14ZHZW3eN6voWVfFcwi4cyrc9z2ElTobEzCN-7liBvb6ifiRYsXeJX4rs6DNnQ-tutn2VIJyIp0g873hzZp2bG3SBiNLB0kqh1SgfenEzUs1eNbyR6Wb2Gau3m152YS1sWfddYnzqv_shtuSPbt8JWATQRJWzjGhxGSdHZpveu_lNiHxNcAGq3oeYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ شاکی شد
😬
از اونی که اومد فحش داد
@withyashar</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/withyashar/12023" target="_blank">📅 23:45 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12022">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e2f574807e.mp4?token=OKjKr1sgG5WcGNw7z9A0g0KwV7gDt2bmin_tAf2yEYCJmXZnlIOokdCtnmJJz5iGS5MsRn_kbUUkVxqRqNWq2dPhbKF78FN0c2hM_DTM1AHFtU9vHztGc-_zPkasENP21PRG0H_MUFAXZGu4o-nzx7CzJNolXrK-aIRmNyWCdfQ-D8io671naHmNODozkVDikfpJ8uqJF6uCSNsmgOOYP1g1VZCGMXyBO3kL-xsmXaHFiLUk-Mbre6R_VcKXHRawC_vtA-UdzdlYd5EGDuO9UgtRb87_6QQD_6FXl-THjML0q_anBkqw7tuh7et0_csm9RiaIIErI-MPFDO5oThD_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e2f574807e.mp4?token=OKjKr1sgG5WcGNw7z9A0g0KwV7gDt2bmin_tAf2yEYCJmXZnlIOokdCtnmJJz5iGS5MsRn_kbUUkVxqRqNWq2dPhbKF78FN0c2hM_DTM1AHFtU9vHztGc-_zPkasENP21PRG0H_MUFAXZGu4o-nzx7CzJNolXrK-aIRmNyWCdfQ-D8io671naHmNODozkVDikfpJ8uqJF6uCSNsmgOOYP1g1VZCGMXyBO3kL-xsmXaHFiLUk-Mbre6R_VcKXHRawC_vtA-UdzdlYd5EGDuO9UgtRb87_6QQD_6FXl-THjML0q_anBkqw7tuh7et0_csm9RiaIIErI-MPFDO5oThD_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ به یک معترض:
برو خونه، پیش ننت
@withyashar</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/withyashar/12022" target="_blank">📅 23:44 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12021">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8de3b319ce.mp4?token=b4BReWS3FvlFASI8g_K5QKZhXAN7WxPAuokF8N61vajBzEo0RPZdb-TcplLrKKjTMMeJfRnudk38-skeQoTC7LvRo8T1CeqDi-thLKaAO-_NiVHNJvIZpSOI1-Aci5-rG1QDtmcaHF8t3JKFk4pX6KVMANp42RQqiVVGSkEUOZMAM48nO9YABA_Bue2GwLuDPUfHikIPPQh4uB7XpltjSlgs2APotWxUq7drPW_0-dp671i6kpq_tilhk7Xz_Pux2VSYMukHzjumPkNFrYsfm-H0hYj3TllroibvggNpq0aPdzRNDuWhphJCrIyn4A3_JLM7uvNXsk9mLjY1tK4pfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8de3b319ce.mp4?token=b4BReWS3FvlFASI8g_K5QKZhXAN7WxPAuokF8N61vajBzEo0RPZdb-TcplLrKKjTMMeJfRnudk38-skeQoTC7LvRo8T1CeqDi-thLKaAO-_NiVHNJvIZpSOI1-Aci5-rG1QDtmcaHF8t3JKFk4pX6KVMANp42RQqiVVGSkEUOZMAM48nO9YABA_Bue2GwLuDPUfHikIPPQh4uB7XpltjSlgs2APotWxUq7drPW_0-dp671i6kpq_tilhk7Xz_Pux2VSYMukHzjumPkNFrYsfm-H0hYj3TllroibvggNpq0aPdzRNDuWhphJCrIyn4A3_JLM7uvNXsk9mLjY1tK4pfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دونالد ترامپ
در‌ نیویورک
:
من ۹۹٪ رأی نیروهای اجرای قانون را گرفتم می‌توانید باور کنید؟
هنوز داریم تلاش می‌کنیم بفهمیم آن ۱٪ چه کسی بوده است.
@withyashar</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/withyashar/12021" target="_blank">📅 23:36 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12020">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">داداشی میشه جریان علی کریمی رو یکم باز کنی الا از شاهزاده حمایت نمیکنه ؟</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/withyashar/12020" target="_blank">📅 23:19 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12019">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromEmad</strong></div>
<div class="tg-text">داداشی میشه جریان علی کریمی رو یکم باز کنی
الا از شاهزاده حمایت نمیکنه ؟</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/withyashar/12019" target="_blank">📅 23:19 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12018">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">@withyashar</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/withyashar/12018" target="_blank">📅 23:16 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12017">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">پنتاگون ویدئویی از بشقاب پرنده انتشار داده که چند سال پیش با فاصله ای بسیار نزدیک از کنار قایقهای تندروی سپاه عبور میکند … @withyashar یاشار : این سپاهی ها آدم فضایی هم دیدند ولی اون دوستمون این جمعه  هم نیامد
😬</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/withyashar/12017" target="_blank">📅 23:12 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12016">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAmin</strong></div>
<div class="tg-text">آدم فضایی دیدیم ولی موشتبی رو ندیدیم</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/withyashar/12016" target="_blank">📅 23:12 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12015">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">بذار تریاکامو بفروشم ۱۰۰دلار برات میزنم</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/withyashar/12015" target="_blank">📅 23:02 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12014">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMohamad S</strong></div>
<div class="tg-text">بذار تریاکامو بفروشم ۱۰۰دلار برات میزنم</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/withyashar/12014" target="_blank">📅 23:02 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12013">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/withyashar/12013" target="_blank">📅 23:01 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12012">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/withyashar/12012" target="_blank">📅 22:57 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12011">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">آکسیوس، به نقل از یک منبع نزدیک به ترامپ: رئیس جمهور احتمال آغاز یک عملیات نظامی بزرگ دیگر، اعلام پیروزی و پایان دادن به جنگ را مطرح کرد
@withyashar</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/withyashar/12011" target="_blank">📅 22:56 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12010">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/85be7040dd.mp4?token=TRYvs_Ab2x5QsTJ0uNd_Lwimadpd88DGNECeV8zXBd1ukKUicGXdmtOQH8ZbJEgmV8hcjXpdbnGBTw5Qn9jsZNV8rIoXD2lLBj0NMZuFAJpV7uKqeFxS6ZuFGCoJxGe6JS5x6ilsX4aRusWsKBK82EVPRHRH-Ab5IT9EMcSyiSaW2NCoIvIH_IDB0BUrMUrrcYsao57uoCcjXk578F5c24hSvvtWLp61PxrsDDf8IVfTxeuduiEoKSA4ockdp6FNNZOnlvfrIkq868WcsiN9mIXQgbKqHajP7mmR5gY12kmMWphUMaGdCR2_haT31JM7bm4ofISWrP_YqpxLUpI1Sw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/85be7040dd.mp4?token=TRYvs_Ab2x5QsTJ0uNd_Lwimadpd88DGNECeV8zXBd1ukKUicGXdmtOQH8ZbJEgmV8hcjXpdbnGBTw5Qn9jsZNV8rIoXD2lLBj0NMZuFAJpV7uKqeFxS6ZuFGCoJxGe6JS5x6ilsX4aRusWsKBK82EVPRHRH-Ab5IT9EMcSyiSaW2NCoIvIH_IDB0BUrMUrrcYsao57uoCcjXk578F5c24hSvvtWLp61PxrsDDf8IVfTxeuduiEoKSA4ockdp6FNNZOnlvfrIkq868WcsiN9mIXQgbKqHajP7mmR5gY12kmMWphUMaGdCR2_haT31JM7bm4ofISWrP_YqpxLUpI1Sw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پنتاگون ویدئویی از بشقاب پرنده انتشار داده که چند سال پیش با فاصله ای بسیار نزدیک از کنار قایقهای تندروی سپاه عبور میکند …
@withyashar
یاشار : این سپاهی ها آدم فضایی هم دیدند ولی اون دوستمون این جمعه  هم نیامد
😬</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/withyashar/12010" target="_blank">📅 22:53 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12009">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">حریت ترکیه : صاحب مجموعه تفریحی معروف «کلاب روبی» در منطقه اورتاکوی استانبول، پس از تذکر دادن به گروهی از افراد مزاحم، در محل کسب خود با شلیک گلوله مجروح شد.
بنا بر گزارش‌های دریافتی، حدود ساعت ۳:۴۵ بامداد شب گذشته، گروهی از افراد با پوشش نامناسب و ایجاد مزاحمت قصد ورود به این کلاب معروف را داشتند که با ممانعت و هشدار علی اونال، صاحب این مجموعه، مواجه شدند. در پی بالا گرفتن مشاجره لفظی، فردی با هویت اختصاری «اِس.کی» با سلاح گرم به سمت اونال شلیک کرد. مالک این مجموعه تفریحی بلافاصله جهت مداوا به بیمارستان منتقل شد.
پس از وقوع این حادثه، نیروهای پلیس استانبول تحقیقات گسترده‌ای را آغاز کردند و ضارب را که با اسلحه از صحنه متواری شده و در مخفیگاهی در منطقه سنجاق‌تپه پنهان شده بود، شناسایی و دستگیر کردند
@withyashar</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/withyashar/12009" target="_blank">📅 22:45 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12008">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">خبر ویژه رسانه های اسرائیل : در یک ساعت گذشته چندین شرکت تحویل کالا و شرکت‌های حمل‌ونقل بار شروع به لغو پروازهای باری به اسرائیل کرده‌اند. یکی از این شرکت‌ها آی‌هرب است
@withyashar</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/withyashar/12008" target="_blank">📅 22:33 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12007">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">اکسیوس : ترامپ عصر امروز (به تایم امریکا)پس از یک سخنرانی برنامه‌ریزی شده در نیویورک به کاخ سفید باز خواهد گشت و آخره هفته در کاخ سفید میماند
@withyashar</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/withyashar/12007" target="_blank">📅 22:26 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12006">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">مقام آمریکایی به اکسیوس:
مذاکرات بسیار دست و پا گیر است و پیش نویس‌ها هر روز بدون پیشرفت زیادی به این سو و آن سو می‌روند.
@withyashar</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/withyashar/12006" target="_blank">📅 22:23 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12005">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/withyashar/12005" target="_blank">📅 22:10 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12004">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/withyashar/12004" target="_blank">📅 22:09 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12003">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eUWo0lXYL02KmUyZVUSBF_oIYFZCKqojE3ejR0F0p2SKqFRsojuClMoYpvGD7ZbQdID8qBVcRBoL1mUmqBq9xDWEFzkCdqmZBR7JEkeI2Ev1KcJLhQVCr8L8Z8OSsMLPfI3VN9NuPSrAER5mk9plEFOmPnO_pID5lVjW3b3qY8V_ArHEP2rtQ8ci6B9ptxUJ8iR-UCVgGI-EQl5bbVNbIZphltk1EU9W8sR9lmiAYg7HvvvU3dfTr4QFI1JTgoBpEws1Lx4fO11m1XO7-9XQkeuaqMf-fvwI4jvJeT3ebkdl6hYTphSKtsZoieXhAIaSzHMVkhRjWm6vGTffRFYweQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">2300ton یا ۴۵۰۰$
🥲
😭</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/withyashar/12003" target="_blank">📅 22:08 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12002">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">https://t.me/boost/withyashar  ۵۰۰ بوست لازم داریم
😭
🥲</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/withyashar/12002" target="_blank">📅 22:07 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12001">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">https://t.me/boost/withyashar
۵۰۰ بوست لازم داریم
😭
🥲</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/withyashar/12001" target="_blank">📅 22:05 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-12000">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/trQLPnTz-G7pcQB5ki9ap_JpHCKZQ44kZZM6WpaTMEazJ7TpWuj_lmnlYk-2Ys_c-KsALTDShn6ujulxNcp1SJAwPgdaDClFqzXzkI8MI1AspmFfVD3HuUxBxZCjRAVBrDuGt9Xh0lP1pWIxAY2yn5lmQI24xE-1iMG8GDvgBLfzzw_XW0aLNEu2ej2ki0lypA59V-YaHZq2SUDCPzckS4kzMv1inU8ku6Rl3w9mXqT_xOhSeaGY6d5hVDyMq6u4fSm_8KlJKDeIdvk7AWjhRTSAZlBzLghyTmHU3AwcKZSOIYMKmefBcXv4NUi02mOlM_HYFWB0wfsAWh9Zd2v4tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«دونالد ترامپ» اعلام کرد «آرون لوکاس» به عنوان مدیر موقت اطلاعات ملی منصوب شد.
@withyashar</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/withyashar/12000" target="_blank">📅 22:01 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-11999">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">سخنگوی وزارت خارجه اسمائیل باقری : یک هیئتی از قطر درحال مذاکره با وزیر خارجه کشورمان هستند اما میانجی مذاکرات همچنان طرف پاکستانی است
نمی‌توانیم بگوییم که به نقطه‌ای رسیده‌ایم که توافق نزدیک است؛ خیر، اینطور نیست.
تفاوت‌ها بین ایران و آمریکا آنقدر عمیق و متعدد است که نمی‌توان گفت با چند دور رفت و برگشت یا مذاکرات در چند هفته حتماً باید به نتیجه برسیم.
تمرکز این مذاکرات بر پایان جنگ است و در این مرحله، بحثی درباره مسائل مرتبط با موضوعات هسته‌ای نخواهد بود. مسائلی مانند «پایان جنگ در همه جبهه‌ها، وضعیت تنگه هرمز و پایان دزدی دریایی آمریکا» هنوز در حال بحث است.
موضوع مذاکرات هسته‌ای بسیار روشن است؛ ما عضو معاهده ان‌پی‌تی هستیم و حق استفاده از انرژی هسته‌ای برای اهداف صلح‌آمیز را داریم.
@withyashar</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/withyashar/11999" target="_blank">📅 21:55 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-11998">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">پرزیدنت ترامپ سفر خود به باشگاه ملی گلف ترامپ را هم لغو کرد و در آخر هفته در کاخ سفید خواهد ماند.
@withyashar</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/withyashar/11998" target="_blank">📅 21:53 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-11997">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">رویترز: کاخ سفید گابارد را مجبور به استعفا کرد
درحالی‌که ترامپ استعفای تولسی گابارد از سمت مدیر اطلاعات ملی آمریکا را به بیماری همسرش مرتبط کرده، خبرگزاری رویترز به نقل از منابعی نوشته کاخ سفید او را مجبور به استعفا کرده است.
گابارد در سمت مدیر اطلاعات ملی نظارت بر ۱۷ دستگاه اطلاعاتی آمریکا را برعهده داشت.
او چندی پیش هنگام ارائهٔ گزارش ارزیابی سالانهٔ تهدیدها علیه آمریکا نظراتی دربارهٔ ایران داشت که به مذاق ترامپ خوش نیامده بود.
محورهای اصلی اختلاف‌نظر گابارد با ترامپ دربارهٔ ایران چه بود
گابارد در کنگره صراحتاً اعلام کرد که ایران پس از حملات پیشین، تلاشی برای بازسازی برنامهٔ هسته‌ای خود نکرده است.
او همچنین از تایید اینکه ایران یک تهدید نظامی فوری علیه خاک آمریکاست خودداری کرد.
@withyashar</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/withyashar/11997" target="_blank">📅 21:45 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-11996">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/withyashar/11996" target="_blank">📅 21:42 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-11995">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/withyashar/11995" target="_blank">📅 21:40 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-11994">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">تحلیلت دست مریزاد داره واقعا
❤️
🔥
حتی اگه در آخر اینطوری نشه باتوجه به داده های موجود  تحلیل واقعا عالی بوده</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/withyashar/11994" target="_blank">📅 21:36 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-11993">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromA i</strong></div>
<div class="tg-text">تحلیلت دست مریزاد داره واقعا
❤️
🔥
حتی اگه در آخر اینطوری نشه
باتوجه به داده های موجود
تحلیل واقعا عالی بوده</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/withyashar/11993" target="_blank">📅 21:35 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-11992">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">ولی اگه بخواهیم عقلانی بررسی کنیم این هفته احتمال حمله ۲۰٪ هست در صورتی که هفته دیگه ۸۰٪ ولی ترامپ هم اهل این حرف ها نیست و همیشه وسط مذاکره لحظه ای که همه فکر میکنن توافق شکل گرفته میزنه !
@withyashar</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/withyashar/11992" target="_blank">📅 21:26 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-11991">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">ترامپ دیدن رسما دقایقی پیش گفت که عروسی پسر ارشدش هم نمیره و برای‌ مسئله ایران کاخ سفید میمونه دست به ماشه ! دوشنبه امریکا تعطیل رسمی هست و این آخر هفته مارکت ۱ روز‌ بیشتر تعطیله و خیلی خاصش کرده !
@withyashar</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/withyashar/11991" target="_blank">📅 21:23 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-11990">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">پس رو کاغذ نشانه ها این رو نشون میدن حمله هفته دیگه انجام میشه و اینا یه پیش نویسی از مذاکره حتی شاید بنویسن ! ولی این چیزی‌ از عرزش های امشب ‌کم نمیکنه ! امشب بسیار روز مناسبی هست برای ترامپ ! و قانونی هم آتش بس تمام شده !
@withyashar</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/withyashar/11990" target="_blank">📅 21:17 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-11989">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">الان این ۹ مورد که میگن اینه ! خود سپاه این هفته آماد‌ه باش نیست و خیالش راحته خیلی هم مطمعن!
حالا هم  آب و هوا هست هم وحیدی و هم حج !!!  آمریکا داره یک تیر و چند نشان میزنه !
@withyashar</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/withyashar/11989" target="_blank">📅 21:14 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-11988">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">ادعای العربیه درمورد پیش‌نویس نهایی توافق مورد انتظار بین آمریکا و ایران که طی ساعات آینده برای توقف جنگ در همه جبهه‌ها تنظیم می‌شود:  ۱. توقف کامل، فوری و بی‌قیدوشرط آتش‌بس در همه جبهه‌ها (زمینی، دریایی و هوایی).  ۲. تعهد دو طرف به عدم هدف‌گیری هرگونه تأسیسات…</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/withyashar/11988" target="_blank">📅 21:12 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-11987">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">ادعای العربیه درمورد پیش‌نویس نهایی توافق مورد انتظار بین آمریکا و ایران که طی ساعات آینده برای توقف جنگ در همه جبهه‌ها تنظیم می‌شود:
۱. توقف کامل، فوری و بی‌قیدوشرط آتش‌بس در همه جبهه‌ها (زمینی، دریایی و هوایی).
۲. تعهد دو طرف به عدم هدف‌گیری هرگونه تأسیسات نظامی، غیرنظامی یا اقتصادی طرف دیگر.
۳. توقف کلیه عملیات نظامی، فعالیت‌ها و جنگ تحریک‌آمیز رسانه‌ای.
۴. احترام به حاکمیت کشورها، تمامیت ارضی آنها و عدم دخالت در امور داخلی.
۵. تضمین آزادی دریانوردی در خلیج فارس، تنگه هرمز و دریای عمان.
۶. تشکیل کمیته مشترک برای نظارت بر اجرای توافق و حل و فصل اختلافات.
۷. آغاز مذاکرات درباره موضوعات حل‌نشده حداکثر ظرف مدت ۷ روز.
۸. لغو تدریجی تحریم‌های آمریکا علیه ایران در مقابل پایبندی ایران به مفاد توافق.
۹. دو طرف تأکید می‌کنند که این توافق در چارچوب احترام به حقوق بین‌الملل و منشور ملل متحد است.
این توافق از لحظه اعلام رسمی آن توسط دو طرف، لازم‌الاجرا خواهد بود.
@withyashar</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/withyashar/11987" target="_blank">📅 21:11 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-11986">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">حالا امشب چی‌میشه …</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/withyashar/11986" target="_blank">📅 21:09 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-11985">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">از اول کسی گردن نگرفت ولی خبر درست درز پیدا کرده بود… آتش بس ۴۵ روزه بود و امشب تموم میشه !
@withyashar</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/withyashar/11985" target="_blank">📅 21:06 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-11984">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">آکسیوس: ایران برای آتش‌بس ۴۵ روزه، برگ برندۀ خود را رها نمی‌کند  وبگاه آکسیوس به‌نقل از منابع آگاه گزارش کرد، درحالی که برخی میانجیگران منطقه‌ای ترامپ، به‌دنبال آتش‌بس [تنفس]  ۴۵ روزه هستند، [باید بدانند] ایران از برگ برنده‌های خود دست نمی‌کشد.  @withyashar</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/withyashar/11984" target="_blank">📅 21:05 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-11983">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">ترامپ:  چه کسی از ۴۵ روز صحبت می‌کند؟  تنها کسی که قرار است آتش‌بس برقرار کند، من هستم. من هیچ آتش‌بس قطعی‌ای تعیین نکرده‌ام.  @withyashar</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/withyashar/11983" target="_blank">📅 21:05 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-11982">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">یک مقام ارشد کاخ سفید به ان‌بی‌سی نیوز گفت پیشنهاد آتش‌بس ۴۵ روزه با ایران «یکی از موارد متعددی است که مورد بحث قرار گرفته است». این مقام گفت که پرزیدنت ترامپ این ایده را امضا نکرد.  @withyashar</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/withyashar/11982" target="_blank">📅 21:05 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-11981">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">مسج هاتون رو میبینم ! حتی اگه بخونه باز هم باید بیاد ، اره در باسن هست ،   جلو بره پاره میشه عقب هم بره پاره میشه … آخرش چی ؟ مقامات پاکستان برای‌ همین اومدن ! قطر اومده ! همه فقط توافق با اون رو قبول دارن ! قشنگی‌ این بازی کثیف‌ همین جاست
😂
@withyashar</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/withyashar/11981" target="_blank">📅 21:00 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-11980">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">وحیدی الان فرد شماره یک و  زننده حرف آخر در تمامی تصمیمات هست برای‌ همین  مذاکرات به نظر خیلی به توافق نزدیک نشون داده  میشه ! تا اون بیاد بیرون و حرف آخر رو بزنه ! آخرش باید این کار رو بکنه و همون جاست که دم به تله میده !
@withyashar</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/withyashar/11980" target="_blank">📅 20:56 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-11979">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">همه در انتظار بیرون اومدن یا نشانه ای از موقعیت وحیدی هستند … شک نکنید</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/withyashar/11979" target="_blank">📅 20:54 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-11978">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">من میرم میخوابم میدونم امشب من بخوابم میزنه
😂
♥️
شب بخیر</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/withyashar/11978" target="_blank">📅 20:51 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-11977">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromK1..Mostafa..</strong></div>
<div class="tg-text">من میرم میخوابم میدونم امشب من بخوابم میزنه
😂
♥️
شب بخیر</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/withyashar/11977" target="_blank">📅 20:50 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-11976">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">رئیس کمیته نیروهای مسلح سنای آمریکا: ترامپ باید به ارتش اجازه دهد تا انهدام توانمندی‌های نظامی ایران را تکمیل کند.
@withyashar</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/withyashar/11976" target="_blank">📅 20:49 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-11975">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">ترامپ در تروث : در حالی که خیلی دلم می‌خواست با پسرم، دان جونیور، و جدیدترین عضو خانواده ترامپ، همسر آینده‌اش، بتینا، باشم، شرایط مربوط به دولت و عشق من به ایالات متحده آمریکا اجازه این کار را به من نمی‌دهد. احساس می‌کنم مهم است که در این دوره مهم در واشنگتن دی سی، در کاخ سفید بمانم. به دان و بتینا تبریک می‌گویم! رئیس جمهور دونالد جی. ترامپ
@withyashar
دمت گرم عمو ترامپ بمون بزن یه عروسی هم بعد براش هتل رامسر میگیریم
😂
🙌🏾</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/withyashar/11975" target="_blank">📅 20:44 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-11974">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">اتاق جنگ با یاشار : خواهیم دید چه خواهد شد</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/withyashar/11974" target="_blank">📅 20:40 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-11973">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">یک منبع بلندپایه به «العربیه»: دیدار فردا میان عاصم منیر، فرمانده ارتش پاکستان و احمد وحیدی، فرمانده سپاه پاسداران ایران در تهران برگزار خواهد شد. @withyashar</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/withyashar/11973" target="_blank">📅 20:39 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-11972">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">یک منبع بلندپایه به «العربیه»: دیدار فردا میان عاصم منیر، فرمانده ارتش پاکستان و احمد وحیدی، فرمانده سپاه پاسداران ایران در تهران برگزار خواهد شد.
@withyashar</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/withyashar/11972" target="_blank">📅 20:38 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-11971">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eeefe24f2f.mp4?token=EaQXFD3h3LoF7tNwJjCO-cTkcJRNzB6RQWtglsNX1oLh96GI_wJUMqrF9MqR_NSp1qb7Nkx-Diu1g5unf3TILbsoxFCUd2IkLLsofkgicYaApX2Pz4tfCl2pWBSx6NEEAQfBYmiAbPr1tGaTzHLNgZL-dnQL6aLVk6P390PqavaDYQkJLkTfpV_O3_nfnDhftrj76PhbIuktCT7G2WtkKD0C_dOCG4AvV0o31HfvF8Ozk5XddypwuknDYMGj-z2p64q6Ln3ImwiTde2owHgqqn_rz0mWW5FBv1rln2Viz_6t3TXwlrB_Fl4oD4mG6pNrWl8xM2pN94FkovgbczCaSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eeefe24f2f.mp4?token=EaQXFD3h3LoF7tNwJjCO-cTkcJRNzB6RQWtglsNX1oLh96GI_wJUMqrF9MqR_NSp1qb7Nkx-Diu1g5unf3TILbsoxFCUd2IkLLsofkgicYaApX2Pz4tfCl2pWBSx6NEEAQfBYmiAbPr1tGaTzHLNgZL-dnQL6aLVk6P390PqavaDYQkJLkTfpV_O3_nfnDhftrj76PhbIuktCT7G2WtkKD0C_dOCG4AvV0o31HfvF8Ozk5XddypwuknDYMGj-z2p64q6Ln3ImwiTde2owHgqqn_rz0mWW5FBv1rln2Viz_6t3TXwlrB_Fl4oD4mG6pNrWl8xM2pN94FkovgbczCaSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیده بان اتاق جنگ : الان شکار ۳ پهپاد شناسایی بالا سر منطقه ویژه ماهشهر
@withyashar</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/withyashar/11971" target="_blank">📅 20:36 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-11970">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">وزیر کشور پاکستان که هم اکنون در تهران بسر می برد با همتای عربستانی خود گفت وگوی تلفنی انجام داد.‌.
@withyashar</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/withyashar/11970" target="_blank">📅 20:32 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-11969">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">علیرضا سلیمی، عضو هیات رئیسه مجلس : «یکی از دستاوردهای جنگ اخیر، مدیریت جمهوری اسلامی بر تنگه هرمز است که هرگز قابل مذاکره و معامله نیست و رژیم حقوقی جدیدی بر این تنگه حاکم خواهد شد که قواعد آن را تنها ما تعریف و اعمال می‌کنیم.»
وی‌ اشاره کرد : «شرایط عبور و مرور همچنین نرخ عوارض بر تنگه هرمز را جمهوری اسلامی مشخص می‌کند و با توییت نمی‌توانند اوضاع تنگه را تغییر دهند.»
@withyashar</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/withyashar/11969" target="_blank">📅 20:23 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-11968">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">ترامپ: همان کاری رو که در ونزوئلا انجام دادیم، در ایران انجام میدیم.
@withyashar</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/withyashar/11968" target="_blank">📅 20:20 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-11967">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">سپهبد عاصم منیر، فرمانده ارتش پاکستان، وارد تهران شد و مورد استقبال اسکندر مومنی، وزیر کشور ایران، قرار گرفت.
پاکستان می‌گوید این سفر بخشی از تلاش‌های میانجیگری مداوم است.
@withyashar</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/withyashar/11967" target="_blank">📅 20:08 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-11966">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">نورمن، خبرنگار وال استریت ژورنال : یه منبع میگه هر چیزی درباره پیش‌نویس توافقی که داره می‌چرخه، دروغه و صحت نداره
@withyashar</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/withyashar/11966" target="_blank">📅 20:08 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-11965">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">آکسیوس:نتانیاهو بزرگ ترین عامل برای عدم توافق بین دو کشور است
@withyashar</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/withyashar/11965" target="_blank">📅 20:06 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-11964">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">ایسنا:  برخی مقامات تاکید کردند که حضور عاصم منیر فرمانده ارتش پاکستان لزوما به معنای قطعی بودن تفاهم بر سر چارچوب اولیه نیست.
@withyashar</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/withyashar/11964" target="_blank">📅 20:04 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-11963">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">العربی الجدید به نقل از منبعی در وزارت خارجه پاکستان: واشنگتن و تهران انعطاف کافی در پرونده‌های اصلی از خود نشان نمی‌دهند
@withyashar</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/withyashar/11963" target="_blank">📅 20:02 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-11962">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">ایسنا: عاصم منیر وارد تهران شد
@withyashar</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/withyashar/11962" target="_blank">📅 19:58 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-11961">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e47ec9ff0.mp4?token=XfDBqEuHEi0qAJ3kTSUw6IBuVeEbWoCBH9DJDNgNvozfRmk7isbtG8cY9wPh_gRCnETzqhVY0UFx_YDScDvsWmcjKS8UtrIpizB7NanYlODoR0K7DI9NTyivhuo9-jU_B7xYZaVOq9wopd44GskYuRpwBLJuPkDGsu6WcGD-NBYMbrbFcjOHyvjcDy2bgAFPGVv1dftJFgrIYL51AICD0tOMkwTqiBC_I_q4xuT6PBWh8YwHwEF54vtUelH6i2TziUsU65RBwVVeK0Ry75865oBCscm1K-wM0xuuKSAXjBCLb4OfAkBGAgyV4K3WY4PJOZVgvE_D-lNWKuNx-Dy0Ug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e47ec9ff0.mp4?token=XfDBqEuHEi0qAJ3kTSUw6IBuVeEbWoCBH9DJDNgNvozfRmk7isbtG8cY9wPh_gRCnETzqhVY0UFx_YDScDvsWmcjKS8UtrIpizB7NanYlODoR0K7DI9NTyivhuo9-jU_B7xYZaVOq9wopd44GskYuRpwBLJuPkDGsu6WcGD-NBYMbrbFcjOHyvjcDy2bgAFPGVv1dftJFgrIYL51AICD0tOMkwTqiBC_I_q4xuT6PBWh8YwHwEF54vtUelH6i2TziUsU65RBwVVeK0Ry75865oBCscm1K-wM0xuuKSAXjBCLb4OfAkBGAgyV4K3WY4PJOZVgvE_D-lNWKuNx-Dy0Ug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کوین وارش رسماً به عنوان رئیس فدرال رزرو سوگند یاد کرد.
@withyashar</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/withyashar/11961" target="_blank">📅 19:54 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-11960">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ef5b5017b.mp4?token=CVlsjO0Ud4_72CCzdQEgkBr6KtZJpxqYWshkYLMoS67waIzSEr_yqB8SfXo9sPcwzxD3x-G_QroHWdvCkneoEDkbw96F99kAcH_JcgPkmAyZveqO3A7u3zwQyg7-ea1QxwdUxnlHt5X2wuRtY0flPdcOoMR4wu7VfO_lzKbphiaQCo5IrOgNLX83jJBneORFWYjf-DQ4KxSqUxjlPAnltYE12xPnVqW6xjhxgO6uf5LKp5DTk6JaFwsMLi-yuU_rDUJYUJy8nqJd55SXVYTOQWexBeU4Gkx63e8-uXYhm4KN0IObKjxMwFnAY_Qp6DT6MEFn_EpoFzjPgAPKMCfjCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ef5b5017b.mp4?token=CVlsjO0Ud4_72CCzdQEgkBr6KtZJpxqYWshkYLMoS67waIzSEr_yqB8SfXo9sPcwzxD3x-G_QroHWdvCkneoEDkbw96F99kAcH_JcgPkmAyZveqO3A7u3zwQyg7-ea1QxwdUxnlHt5X2wuRtY0flPdcOoMR4wu7VfO_lzKbphiaQCo5IrOgNLX83jJBneORFWYjf-DQ4KxSqUxjlPAnltYE12xPnVqW6xjhxgO6uf5LKp5DTk6JaFwsMLi-yuU_rDUJYUJy8nqJd55SXVYTOQWexBeU4Gkx63e8-uXYhm4KN0IObKjxMwFnAY_Qp6DT6MEFn_EpoFzjPgAPKMCfjCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران:
«ایران داره جون میده برای توافق.
ما حسابی زدیمشون؛ چاره‌ای هم نداشتیم، چون ایران نباید سلاح هسته‌ای داشته باشه.»
@withyashar</div>
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/withyashar/11960" target="_blank">📅 19:49 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-11959">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/withyashar/11959" target="_blank">📅 17:05 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-11958">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/609141a267.mp4?token=p9P4xJo2HQMgxWeSf9SOeR_PvETKzSbaJe5itV3wKNvgimah25i-KNIfO8L-W8iYA-iWOyXkQVBCDrUmq33O5qCa3KHWVfsMEospxrRjN1NezcU3Jj96zgPB53_3NGFXoyvlu3WDUv9g1CmRfV9IYcV6O5QqUn7yw0o0B7EFKZgiNwifHkKq-J98uxIZLLVu-uBxcOhohK3LzLPMogDZ5osFQqH4r8G31EXylPU3yffVUvYcWjqu28dFBXioc3iTEcA0-UNi2WeZ45kKfmofH2nwbt_d5SBbYJlmz5HMhlZmkxAWSXEaTRkOsRSQLiGoSjJhGNQor50nW-qZRiyXDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/609141a267.mp4?token=p9P4xJo2HQMgxWeSf9SOeR_PvETKzSbaJe5itV3wKNvgimah25i-KNIfO8L-W8iYA-iWOyXkQVBCDrUmq33O5qCa3KHWVfsMEospxrRjN1NezcU3Jj96zgPB53_3NGFXoyvlu3WDUv9g1CmRfV9IYcV6O5QqUn7yw0o0B7EFKZgiNwifHkKq-J98uxIZLLVu-uBxcOhohK3LzLPMogDZ5osFQqH4r8G31EXylPU3yffVUvYcWjqu28dFBXioc3iTEcA0-UNi2WeZ45kKfmofH2nwbt_d5SBbYJlmz5HMhlZmkxAWSXEaTRkOsRSQLiGoSjJhGNQor50nW-qZRiyXDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/withyashar/11958" target="_blank">📅 17:01 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-11957">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">امشب مراسم دعای سرخپوستی در اتاق جنگ برگزار میکنیم
💨
😬
😂
🙌🏾</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/withyashar/11957" target="_blank">📅 16:57 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-11956">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">الجزیره: شهباز شریف، نخست‌وزیر پاکستان، قصد دارد فردا به چین سفر کند. برداشت این است که او پیام‌هایی را از تهران به پکن می‌برد.
پاکستان در حال تعامل با بازیگران متعددی است: آمریکا، ایران، کشورهای منطقه و البته چین.
@withyashar</div>
<div class="tg-footer">👁️ 54.7K · <a href="https://t.me/withyashar/11956" target="_blank">📅 16:54 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-11955">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">رویترز به نقل از منابع آگاه:
قطر با هماهنگی آمریکا تیم مذاکره کننده‌ای رو برای کمک به دستیابی به توافق برای پایان جنگ با ایران به تهران اعزام کرده.
@withyashar
این هیئت دقایقی پیش به تهران رسید</div>
<div class="tg-footer">👁️ 54.7K · <a href="https://t.me/withyashar/11955" target="_blank">📅 16:53 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-11954">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">مارک لوین تحلیلگر و از نزدیکان ترامپ :
"زمان نابودی رژیم ایران فرا رسیده است. بیایید کار را تمام کنیم.
بگذارید کار را به انجام رسانیم.
تیک‌تاک ساعت را می‌شنوید."
@withyashar</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/withyashar/11954" target="_blank">📅 16:48 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-11953">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/withyashar/11953" target="_blank">📅 16:47 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-11952">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">وال استریت ژورنال: ترامپ درحال بررسی امکان تکیه بر گروه‌های مخالف مسلح ایرانی، از جمله جناح‌های کرد، در صورت اقدام مسلحانه اونا برعلیه دولت تهرانه.
@withyashar</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/withyashar/11952" target="_blank">📅 16:40 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-11951">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/withyashar/11951" target="_blank">📅 16:39 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-11950">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">یجور دایرکت میدید که انگار من این چند ماه قصه حسین کرد شبستری تعریف میکدم !!!
🤬
بد میگین عصبی‌نشو</div>
<div class="tg-footer">👁️ 54.7K · <a href="https://t.me/withyashar/11950" target="_blank">📅 16:06 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-11949">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">ادعای الحدث: عاصم منیر، فرمانده ارتش پاکستان در راه تهران است. @withyashar</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/withyashar/11949" target="_blank">📅 16:04 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-11948">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">خضریان، عضو کمیسیون امنیت ملی مجلس: جمهوری اسلامی در خصوص خروج اورانیوم از ایران هیچ مصالحه‌ای انجام نخواهد داد
@withyashar</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/withyashar/11948" target="_blank">📅 15:57 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-11947">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">ادعای الحدث: عاصم منیر، فرمانده ارتش پاکستان در راه تهران است.
@withyashar</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/withyashar/11947" target="_blank">📅 15:54 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-11946">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">تلویزیون منو‌تو : به اطلاع مخاطبان گرامی می‌رسانیم که پس از مدت‌ها تامل و ارزیابی، سرانجام به این تصمیم دشوار رسیده‌ایم که به پخش برنامه‌های منوتو پایان دهیم. آخرین پخش ما از ماهواره و یوتیوب، شامگاه ۲۴ مه ۲۰۲۶ (۳ خرداد ۱۴۰۵) خواهد بود.
@withyashar
🥲</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/withyashar/11946" target="_blank">📅 15:52 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-11945">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">بقائی: مرحله بعدی جنگ، قابل کنترل نیست / آمریکایی‌ها در حال ارسال سلاح به منطقه هستند
@withyashar</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/withyashar/11945" target="_blank">📅 15:31 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-11944">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Sonnat Shekan (t.me/withyashar)</div>
  <div class="tg-doc-extra">Pishro (instagram.com/yashar)</div>
</div>
<a href="https://t.me/withyashar/11944" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🌐
@withyashar
🌐
instagram.com/yashar</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/withyashar/11944" target="_blank">📅 15:25 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-11943">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAmirAli</strong></div>
<div class="tg-text">یاشار میدونی
تو همیشه خط شکن بودی
اون زمان که کسی رپ رو نمیشناخت و همه اش ریسک بود
تو رپفا رو اوردی، که خود من سالها ازش استفاده میکردم
الانم کانالت، نحوه جدید و درست برخورد با اخبار و تحلیل های سیاسی رو داره میده که برای امروز خوبه و مخاطب بدون ترس و تردید میتونه دنبالت کنه
واقعا کار درست، خوش فکر و درجه یکی
و این یکی برای تو فقط زحمت هست ولی مثل همیشه پای کار هستی</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/withyashar/11943" target="_blank">📅 15:24 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-11942">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">فاکس نیوز: مذاکرات بین ایالات متحده و ایران همچنان در جریان است، با نشانه‌هایی از خوش‌بینی محتاطانه که هر دو طرف ممکن است در نهایت به توافق برسند
@withyashar</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/withyashar/11942" target="_blank">📅 15:11 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-11941">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">poshte-pardehaye-enghelab (@withyashar).pdf</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/withyashar/11941" target="_blank">📅 15:06 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-11940">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">عمو ترامپ در‌ تروث : رکورد جدید بازار سهام!
@withyashar
یاشار : عمو باز ببین اگه کمه ما گلریزون میکنیم بقیشو ولی ‌زودتر بزن
😂</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/withyashar/11940" target="_blank">📅 15:01 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-11939">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">طبق روال هر روز حمله هوایی اسرائیل به جنوب لبنان
@withyashar</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/withyashar/11939" target="_blank">📅 14:54 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-11938">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">@withyashar
روشن فکران</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/withyashar/11938" target="_blank">📅 14:45 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-11937">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">اتحادیه اروپا: به دلیل بسته ماندن تنگه هرمز، تحریم‌های جدیدی علیه ایران وضع کرديم.
@withyashar</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/withyashar/11937" target="_blank">📅 14:01 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-11936">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">العربیه: بر اساس ارزیابی ایالات متحده، حدود ۱۰۰ افسر از نیروهای سپاه پاسداران انقلاب اسلامی در ماه‌های اخیر به لبنان رسیده‌اند و در حال تسلیح و آموزش فعال نیروهای حزب‌الله هستند.
@withyashar</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/withyashar/11936" target="_blank">📅 14:00 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-11935">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">طبق گزارش العربیه با استناد به یک منبع پاکستانی :   اسلام‌آباد به شدت رو چین برای کمک به پیشبرد یک توافق احتمالی بین ایالات متحده و ایران حساب می‌کنه و انتظار میره شهباز شریف، نخست‌وزیر پاکستان، تو مرحله‌‌ی بعدی به چین سفر کنه
@withyashar</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/withyashar/11935" target="_blank">📅 13:55 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-11934">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EDMCRuoiCUr-KmPT9Rod4ZTIiiGXB-mmWnQkxp1qo8U8XvP1E7mGn9uK35jXnPHso04qwrRFFEdF1QMskNTnSOZ12y8S_ZJClBZxDuDlv359EdObK7Hs2ADUkLiH6ZYVBYaxTAUm4sIBE_NWZOBLd-hHceeNJpuPkAQaEMayhWPwJfEnhdaVLXvRUw2ov2KQmBMF8GaJU6_F83Aqp4BzqEmWoIJGkZ8210yZv1J44rntzVVSc-9lJq3QjS6cCKtGFHrMSaWiKNIdouexAFkKErlh_RybMGhVmMhacgCWVmeb-VSM8lMPfNVdmzHSIP96VcrY2UU1fM2qcOhyKlHjhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصاویر ماهواره‌ای که امروز ثبت شده‌اند، آنچه به نظر می‌رسد بیش از یک دوجین هواپیمای سوخت‌رسان در محوطهٔ پایگاه هوایی شاهزاده سلطان را نشان می‌دهد، همچنین چندین هواپیمای شناسایی E-3 سنتری و دست‌کم ۲۰ جنگنده، به‌همراه چندین هواپیمای سوخت‌رسان که در وضعیت آمادهٔ برخاست هستند.
واشنگتن در حالی که دیپلمات‌ها در حال مذاکره هستند، ماشین جنگی خود را در وضعیت آماده شلیک نگه داشته است.
@withyashar</div>
<div class="tg-footer">👁️ 57.5K · <a href="https://t.me/withyashar/11934" target="_blank">📅 13:39 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-11933">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">کانال ۱۲ اسرائیل : بر اساس گزارش، پیش‌نویس توافق‌نامه در مجموع شامل ۹ ماده است
از جمله توقف عملیات نظامی و جنگ رسانه‌ای بین کشورها، احترام به حاکمیت و خودداری از دخالت در امور داخلی و همچنین رعایت قوانین بین‌المللی و منشور سازمان ملل.
@withyashar</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/withyashar/11933" target="_blank">📅 13:04 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-11932">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">امروز ۲۲ می (۱ خرداد) روز جهانی پیتزای بیت‌کوین است . این روز به یادبود اولین تراکنش واقعی برای خرید یک کالای فیزیکی با بیت‌کوین در سال ۲۰۱۰ نام‌گذاری شده است که در آن کاربری به نام لازلو هانیچ (Laszlo Hanyecz) دو پیتزا را در ازای ۱۰,۰۰۰ بیت‌کوین خریداری کرد.
@withyashar</div>
<div class="tg-footer">👁️ 58.6K · <a href="https://t.me/withyashar/11932" target="_blank">📅 12:28 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-11931">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">وزیر امور خارجه آلمان: ما در حال آماده شدن برای مشارکت در تأمین امنیت تنگه هرمز تحت رهبری بریتانیا هستیم، اما انتظار ماموریتی مشابه ناتو را ندارم
@withyashar</div>
<div class="tg-footer">👁️ 58K · <a href="https://t.me/withyashar/11931" target="_blank">📅 12:07 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-11930">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">وال استریت ژورنال:  میلیاردها دلار از طریق پلتفرم بایننس به شبکه‌هایی که نظام ایران را تامین مالی می‌کنند، جریان یافته است بابک زنجانی شخص مسئول ایرانی در معاملات از طریق پلتفرم بایننس است @withyashar</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/withyashar/11930" target="_blank">📅 11:49 · 01 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
