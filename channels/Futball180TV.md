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
<img src="https://cdn5.telesco.pe/file/vbDUPXRmE4AEGMmclH3iI-z3NYy4UU8ToIOq0ntwZy7gCrB49NE9oF1HjSe0ChxWbaFi_Jn4gVQIO4R8SebIFVFYv358Gpk66OD1FNyAsbLFTXQZlmMclvZQGKMRKbCUvpIPb8OXYwOldAZ-w_1eXE9vx3hmASntZOYCgOLSlEaZSc20v8aoFpTSEzvL7GhdevVxzhkk2rWrjwoQCOXuxz5XTGqpLNrDuNZGV_-Ra54ydJ_UZiZDUsDKEntIlYCtis_Y4-W8opPPnYzNAPmcPZZWLK-TjfyCbDHr6Dwtwibio0t45JVYgJy6w0ClQMG7QLy34yKTzkJbcPPp7-cwEw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 جام جهانی 2026 | فوتبال 180</h1>
<p>@Futball180TV • 👥 576K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-24 10:05:15</div>
<hr>

<div class="tg-post" id="msg-100223">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🏆
گوشه‌ای از بهترین سیوهای جام‌جهانی ۲۰۲۶
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1.23K · <a href="https://t.me/Futball180TV/100223" target="_blank">📅 10:00 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100222">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f24ohMNDBKLJGXQjWvBTDCW9cwCJoeftSxnraprO6tsOKYJVvTa2AWQXaq3asRDpIYpd5Xe-q1bo78OFC9BFFLNB1FWt5O6MFzBuHC_FcwNiKFcopCiCHxMQmermwPHCXf95FMvF0qa43xfoZbwatxfBQPW86LbctbSph6OrqlmV5QPNjwxvuEJXLO6uSUiGa7THyj4YXaigA_HrmKtwP3Ok3WlRzzgLZdbYtduN8shFYSU03igKmG25wzGV6XLN1H17BdByOR4JOLPvTQEhMS5dXr0etD1yKAdMrgK3HcX374MWyD0w5lTmyt9SSd5K2WJhX9ZEnLunk7Rg5cvsTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بیشترین رشد فالوور بازیکنان در جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.69K · <a href="https://t.me/Futball180TV/100222" target="_blank">📅 09:40 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100221">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">👀
🇦🇷
آرژانتینی‌ها از سنین کودکی به فرزندانشون میفهمونن که لیونل‌مسی کی بوده و چیکار کرده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.15K · <a href="https://t.me/Futball180TV/100221" target="_blank">📅 09:20 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100220">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">در حمله شب گذشته آمریکا بیش از ۱۰ موشک به تیپ ۳۸۸ ارتش در ایرانشهر - سیستان بلوچستان برخورد کرد که گزارش‌های اولیه به ده‌ها کشته در محل انفجار که عمدتاً سربازان وظیفه بودن و دست‌کم دو کشته‌ی دیگر پس از انتقال به بیمارستان حکایت دارند؛ تعداد بسیار زیادی هم مجروح شدن.
💔
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.37K · <a href="https://t.me/Futball180TV/100220" target="_blank">📅 09:13 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100219">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pELxHSWEWLAruGWjGG0YEKaHtoSRNkngNp4WF6OEDKBIKv8X3YxdQLEqsJw0w1hWCEHKQsXbDts7p5s3HonbapP7ocARTdBWaekl5i93o-2P-YUehvOiOi6zn_IT9f-ccg-4nP1TRg6Tn8Y5AtrUhVcdjHYdmOnyIc2xue6c1zNziSByu5ux_INYO6xoZ1KlvvAV5Ag58l2h3lRB6tL00HgntJLXWfVypARs7JIqMJAdR0ZxxEU2cJtGI_XFivB74XKoOaF7x0WB3Lf7pSscaPwkPwzRctJ0NAMRbcEoWC-Qq0Do-I5KgIbDGt_OnBsIesF6MfI1tsN2kWug78RTxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇫🇷
با اعلام فدراسیون فوتبال فرانسه، زیدان رسما سرمربی خروس‌ها شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/Futball180TV/100219" target="_blank">📅 08:54 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100218">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uxRZ4u1fLbmcNFY7YxUc0f8ZpeTj_5lQQbndzJWUNE4IDTAN9Do5cwYOsQNNNbTkXAysamdKZUqdB282n--HD3eo66huqad0V9jC79bFvXs1N--2opHkVmI5kHlv5EhkqEt7kfIggJc6HlhYcvLI9hDqkiC81oPoH1_pkLcBfZQHFzFKuoGya64YPTHq0xCMem3wp2DWDHWF791Qxu3tNYZHiTnZQgzBGz1BJybMA8koRKFR0a3ClofanWg2kxLOeO0Sm9Z8rRA-udlBSisTOB2fFuJWJzQWbTrFB7raUp6-9VlwW64Tuh0T9bcHbEirxnOQrnVB4sOJecBpxH__2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🧠
رودری با 11 بار پیروزی در دوئل‌های خودش در بازی با فرانسه به تنهایی از کل خط هافبک فرانسه (9) بیشتر دوئل موفق داشت
‼️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/100218" target="_blank">📅 06:09 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100217">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d888d31120.mp4?token=WkPCyO6RQYa0srN3qKccw1pIvvqDcZmAEqTcm-ljFDwdrm0BTzZHXV6ODBj2GjeMVhOSp3wqQzsGQhfGHBXrtolLSpJcf4LauZ5elI_ILvy_717AFH7-davrbR94zvSqE6M6bjQYLgct0YunhARLzEo0MQ5CC6sbPyl-D_l-4Cf-jA7riE8LBvOCjuoy6kZwex_2Y1OFEcJx4PGc7a0H-heVHH87eeoOWQ__TLp-JKZ3s_JosXNBWymcyJTtGhmaEaCBF64RxyLua21GmMptnw27ULT0riUVMKdblgHCxXfUXXIT4ahhzQe-4YoBf2s7Vp-hEFkHzTvSwpFKypvXJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d888d31120.mp4?token=WkPCyO6RQYa0srN3qKccw1pIvvqDcZmAEqTcm-ljFDwdrm0BTzZHXV6ODBj2GjeMVhOSp3wqQzsGQhfGHBXrtolLSpJcf4LauZ5elI_ILvy_717AFH7-davrbR94zvSqE6M6bjQYLgct0YunhARLzEo0MQ5CC6sbPyl-D_l-4Cf-jA7riE8LBvOCjuoy6kZwex_2Y1OFEcJx4PGc7a0H-heVHH87eeoOWQ__TLp-JKZ3s_JosXNBWymcyJTtGhmaEaCBF64RxyLua21GmMptnw27ULT0riUVMKdblgHCxXfUXXIT4ahhzQe-4YoBf2s7Vp-hEFkHzTvSwpFKypvXJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
👀
🇪🇸
شعار هواداران اسپانیا: امباپه کجاست؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/100217" target="_blank">📅 04:01 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100216">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af8960eb8b.mp4?token=J-Q3PKe36U4gFXC9gV1LPmzUK87ewnpAkBc_EzGPuRiVtbuHFDF8uXIpr7jli_zUASRHL4uGpzh6boCDn_apfqg4KlgiTxwfEVM-rYBwNTln09caFYjjTGPNE47aCwFdpsYDvVbl5MTSzBntpQhszNOV5aPjxWigkeGS7l3hL-wvXJpuEKlFkaAavK5R9OsFOfehckM2iUFZ4znx2Z-0NFq498m8vGUYL5Zh3xVVO0IIIVdUEPg_pKNVxm4sTRk-VBjqlGS05G9sX_qp6GC45QNv__C8rGsG4SYm6wzjjDVPOrOMEVvwCc9JIg_8EUWI2Ysampc23StKmWcy4ugeMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af8960eb8b.mp4?token=J-Q3PKe36U4gFXC9gV1LPmzUK87ewnpAkBc_EzGPuRiVtbuHFDF8uXIpr7jli_zUASRHL4uGpzh6boCDn_apfqg4KlgiTxwfEVM-rYBwNTln09caFYjjTGPNE47aCwFdpsYDvVbl5MTSzBntpQhszNOV5aPjxWigkeGS7l3hL-wvXJpuEKlFkaAavK5R9OsFOfehckM2iUFZ4znx2Z-0NFq498m8vGUYL5Zh3xVVO0IIIVdUEPg_pKNVxm4sTRk-VBjqlGS05G9sX_qp6GC45QNv__C8rGsG4SYm6wzjjDVPOrOMEVvwCc9JIg_8EUWI2Ysampc23StKmWcy4ugeMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صعود اسپانیا به فینال جام جهانی 2026!
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/100216" target="_blank">📅 03:32 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100215">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/60bb44d472.mp4?token=lIla79vh4uP8YI4UumVMEMX_vhfgFWNHzqRMODwwkL4AQ614EnC6v8XPGEtGnz49mq1E15D79ggCpi3-zqdzkTcRrkXHL_jxlgwVjp-eCMBW9PB837JQAl4D-NdGBlQlu_sfHz30gxQai-MS6PMpsoab8ioYloZ_hMXhp32Soa8fZ5NvFkOdxjtSqs2XJ6PLdZ3eNsA-99Cy9mHlTWYcwl0eqTgbxbYmEIYLde22rLBlToR6z2CwLkqrGzRLldnFe0SO8HX-D4kCzkZ88fMiFSJpSWyp4zdPvdvH6d8bM6uQEnvoVyhqVivvpFUbxaKQlymqFwet-_UcY34fO2PPtQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/60bb44d472.mp4?token=lIla79vh4uP8YI4UumVMEMX_vhfgFWNHzqRMODwwkL4AQ614EnC6v8XPGEtGnz49mq1E15D79ggCpi3-zqdzkTcRrkXHL_jxlgwVjp-eCMBW9PB837JQAl4D-NdGBlQlu_sfHz30gxQai-MS6PMpsoab8ioYloZ_hMXhp32Soa8fZ5NvFkOdxjtSqs2XJ6PLdZ3eNsA-99Cy9mHlTWYcwl0eqTgbxbYmEIYLde22rLBlToR6z2CwLkqrGzRLldnFe0SO8HX-D4kCzkZ88fMiFSJpSWyp4zdPvdvH6d8bM6uQEnvoVyhqVivvpFUbxaKQlymqFwet-_UcY34fO2PPtQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😂
😂
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/100215" target="_blank">📅 03:03 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100214">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3f573ba753.mp4?token=S5pOjQ2SJ1JAG95LBetXzsom_M3t-P0tcOi0zVwiwY1zID8I_aryldGxEtWc9dMcupI9IvQDnIswJayUnV2BWvZS5SNgFGESFl8-AC9K7R5DxO4rLW8nAnZ5Qk1azmbRFhqBzo2FRfiCXsh_fGOY55NQu9rGpkNs8ADFqW8tM9lzCo3_Nt2SysX3fH5p-jMOZk4tIfFpN64ve88x3aMwf7rJZ06z2w8Mbcwehd77EOPNY9eYLbsCs9-qIAVzbKjdH4tRfU3JuVNB0nVe9tMCp5OdsRfupIMgpbyiQuvms5QBao9w_uWUM80QVtKAVoxJHtmQE02g7Xfa2ShTxus1Rw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3f573ba753.mp4?token=S5pOjQ2SJ1JAG95LBetXzsom_M3t-P0tcOi0zVwiwY1zID8I_aryldGxEtWc9dMcupI9IvQDnIswJayUnV2BWvZS5SNgFGESFl8-AC9K7R5DxO4rLW8nAnZ5Qk1azmbRFhqBzo2FRfiCXsh_fGOY55NQu9rGpkNs8ADFqW8tM9lzCo3_Nt2SysX3fH5p-jMOZk4tIfFpN64ve88x3aMwf7rJZ06z2w8Mbcwehd77EOPNY9eYLbsCs9-qIAVzbKjdH4tRfU3JuVNB0nVe9tMCp5OdsRfupIMgpbyiQuvms5QBao9w_uWUM80QVtKAVoxJHtmQE02g7Xfa2ShTxus1Rw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
تشویق تماشاگران فرانسوی توسط امباپه:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/100214" target="_blank">📅 02:35 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100213">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AUyolGa4CdnKaUy09jEkG-Df6Ot6ektFBHQaQ0_J-fp051XeGLRAJ1ZH2lW9hBPURMZG8MgUDAdYrg2dIhD5Q22HCu_vzRXkEv_GYm1SnSew5bBry6OKJDtUBzWtXpqvLWGmrhH8G55a5uN_2z4GsjUM8zrA_0qmfA4GWesZAcBLgJjBcgX0VMKfHMS_CXlaHpAg3OIQRHswZSWNRvphXlU5eyCPfrTaPg9twXbundcvhj-48aQW5WNBAR_TwTIZplXwvSa0Alef2aTmbXkAUlGz0X7BqcQbr32z3_hmzXlThl1vVLK6zGuqCOYW2vmK_IeF1lzMkqZrBOg57oQkGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😆
🏆
‼️
از میزان هوش داور بگیم که بنده‌خدا یادش رفته بود اسپری محو‌شونده خودشو بیاره و وسط بازی داور چهارم رسوند دستش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/Futball180TV/100213" target="_blank">📅 01:56 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100212">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
#فوووووری ترامپ: اگر ایرانی‌ها به مذاکرات وین نروند، هفته‌آینده تمامی پل‌ها و نیروگاه‌های برق ایران نابود می‌شود
❌
روز دوشنبه‌آتی دقیقا اولین روز هفته پس از پایان جام‌جهانی!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/Futball180TV/100212" target="_blank">📅 01:52 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100211">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
#فوووووری: ترامپ در مورد یک حمله زمینی به جزیره خارک: " کافیه کمی صبور باشید. من این کار را مطمئنآ خواهم کرد."
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/Futball180TV/100211" target="_blank">📅 01:49 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100210">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f60a4ce9f7.mp4?token=OISB8AUlejg_AKlIeG0CflWlF5cKLLQnQWZCJcn2trsb_Iwz9n_qjeBkLfzHhES9dASEqOD7l1yJnFCeeYqM8AiOnQcAoAailbXdedy9OoiqaYxScxG5YYa6lxzHpP1NCxWzAcoXD5ocisHwdZu11N0vJGDFLa3NYf1yzTgqMA9lRR6s8-Lhu_wWdyJUIr4mw_ej90oLPqxzkfOCHVMihXrN_3j5MOXmz6bihuZ7AJPGmraegX4RSbC6zzQVqI7mnruVlUlzaFb8Y3Mg2I01J121T_ePtpoBPEAPjha_krVzVRDiDHyA9xVtOP2o8QhIbfwDH-qtawkhOV2Gc_h4NQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f60a4ce9f7.mp4?token=OISB8AUlejg_AKlIeG0CflWlF5cKLLQnQWZCJcn2trsb_Iwz9n_qjeBkLfzHhES9dASEqOD7l1yJnFCeeYqM8AiOnQcAoAailbXdedy9OoiqaYxScxG5YYa6lxzHpP1NCxWzAcoXD5ocisHwdZu11N0vJGDFLa3NYf1yzTgqMA9lRR6s8-Lhu_wWdyJUIr4mw_ej90oLPqxzkfOCHVMihXrN_3j5MOXmz6bihuZ7AJPGmraegX4RSbC6zzQVqI7mnruVlUlzaFb8Y3Mg2I01J121T_ePtpoBPEAPjha_krVzVRDiDHyA9xVtOP2o8QhIbfwDH-qtawkhOV2Gc_h4NQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/Futball180TV/100210" target="_blank">📅 01:48 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100209">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
#فوووووری
: ترامپ در مورد یک حمله زمینی به جزیره خارک: " کافیه کمی صبور باشید. من این کار را مطمئنآ خواهم کرد."
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/Futball180TV/100209" target="_blank">📅 01:47 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100208">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/70a1bfb1af.mp4?token=VZEN6RDovN4bJ-02vwZf9XufzIVXmjpvqSkA-HZ6C9FrQ-AzXTpeV1EpTj7KRZXKjmJ1-dGpydTZitlAOQCkKOHBHPlnS_T1HUBjtQgyN2ryXilAzlVtnvkjcDIVjcvxPzIJdrIcV2K433-oO3EWYUMRktxX9T6BgTl-t-qdWvep7Nl-zsBnVI5ACriyizbcXe4xv1icKvZdMSN77OXdEyN68P5dBGEbxnlIJkJhxYxpDm3m9GjVkSpzXJcdxAXM7zv0VqK_ADAytWa3qp_IB9uddqyGYAy_RSQ7G5rg7r2XYWDwqvJfuc_axHReHJALuU1DG4PK2qC6B8YoX-YOtA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/70a1bfb1af.mp4?token=VZEN6RDovN4bJ-02vwZf9XufzIVXmjpvqSkA-HZ6C9FrQ-AzXTpeV1EpTj7KRZXKjmJ1-dGpydTZitlAOQCkKOHBHPlnS_T1HUBjtQgyN2ryXilAzlVtnvkjcDIVjcvxPzIJdrIcV2K433-oO3EWYUMRktxX9T6BgTl-t-qdWvep7Nl-zsBnVI5ACriyizbcXe4xv1icKvZdMSN77OXdEyN68P5dBGEbxnlIJkJhxYxpDm3m9GjVkSpzXJcdxAXM7zv0VqK_ADAytWa3qp_IB9uddqyGYAy_RSQ7G5rg7r2XYWDwqvJfuc_axHReHJALuU1DG4PK2qC6B8YoX-YOtA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
❌
داداش‌یامال بعد گلی که لامین زد و مردود شد حسابی زد زیر گریه و اشکاش بند نمیومد
😂
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/Futball180TV/100208" target="_blank">📅 01:45 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100207">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/QbR-lLw860UR3Y6Ddf8T3qXpIf9PcvPqIRgcrEi14L4GpTuQMv1vBNkhFIagpOArDWoCPP9M-dg3jnxLRiEajb0Qb20tfo9x2MZgwC1vGBCtCNH7XnuK4YaBYiWu6yxiDK1FruOmrPvQgNk6zD2uZbzU9QdxBwX5RPhvQVTcUtMMm3wLxgU8awmDRZIYsXwfwHAbaFQ2H7RCud3mJoeFGPA1zItuqUG9k1dzNmsUfXGgAcebIymhauzkuyS2PLhrKozk1OEHK5KddiStWMPx-sxuaN-idyyeOLe055kRDaYhS7zpZON28GIUDO9C0nJbzelu8KjGhHZc7mTK7zOxkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔥
پدری، یک سال پیش، پستی با عنوان "19/7/2026" منتشر کرد، که به تاریخ فینال اشاره داشت.
و امروز، پدری به فینال صعود کرد.
🫡
🫡
🇪🇸
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/Futball180TV/100207" target="_blank">📅 01:35 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100206">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e25e4d415.mp4?token=PV5k1D7saXfjHsSNCQ2edanaYSFJCQahXO6J9JfUKW0T6W0bnqZAEMVd1okFDAj9Ftb7tTTX8lyJt2CPfFfLUre02KIBqltcw06KTyv_ltEao8tlyBxzu2Of1hTBoHB6hh0EuvqsgYcNrCWSRRIu0tEXoGePHrj-chClwzoIvvc7pUGtVq_staZAlqcrVuzmNtc_wPDtASOAhiLo2CEraypGGn8DbcOOn22v1YQWje-HN0--smFQ9oC8lNGcOsynb4fawcDXmsEjuGkcxpwc18Jl_rZMGQvNg4FEr3cHpCMacsRviVuvT8-8gBMk4pY0deoaWPzxr5-qoPFVcW-OKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e25e4d415.mp4?token=PV5k1D7saXfjHsSNCQ2edanaYSFJCQahXO6J9JfUKW0T6W0bnqZAEMVd1okFDAj9Ftb7tTTX8lyJt2CPfFfLUre02KIBqltcw06KTyv_ltEao8tlyBxzu2Of1hTBoHB6hh0EuvqsgYcNrCWSRRIu0tEXoGePHrj-chClwzoIvvc7pUGtVq_staZAlqcrVuzmNtc_wPDtASOAhiLo2CEraypGGn8DbcOOn22v1YQWje-HN0--smFQ9oC8lNGcOsynb4fawcDXmsEjuGkcxpwc18Jl_rZMGQvNg4FEr3cHpCMacsRviVuvT8-8gBMk4pY0deoaWPzxr5-qoPFVcW-OKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🇪🇸
خانواده سلطنتی اسپانیا خوشحال از صعود کشورشون به فینال جام‌جهانی فوتبال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/Futball180TV/100206" target="_blank">📅 01:30 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100205">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a763ec0bd.mp4?token=qM-0xfRUd3LwDVm3TG9U0eNc3MBrTUzknIBUPFICsxvLFuGkbZQ1cWBy3aIV-F_L_ADExKZNCXZS6db1RKfcR-0azBLDbTZBJJWyLdgpDwn4G0iw6rYa7y3WENcjtZ0kk6CRry155xvuaVjgfJQfkki1EqD_Q4MjYWpHLa9rjfG-6tR_C1ZTMg4pjWSn-ARsKsTVdQy1wVvcZckjIb1ii77UM6XCndVWTGRbrP5JwsoYZ1i_WshUUobdWiBcvSJ2MTuilnRU5Y_cCLxYwhhQywe8ooAY7Uv_PNFc8vNaDq5R8kgrJ8hshwTs8jyLFRjSNwdut7h7ILFbJVdJ1jj__A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a763ec0bd.mp4?token=qM-0xfRUd3LwDVm3TG9U0eNc3MBrTUzknIBUPFICsxvLFuGkbZQ1cWBy3aIV-F_L_ADExKZNCXZS6db1RKfcR-0azBLDbTZBJJWyLdgpDwn4G0iw6rYa7y3WENcjtZ0kk6CRry155xvuaVjgfJQfkki1EqD_Q4MjYWpHLa9rjfG-6tR_C1ZTMg4pjWSn-ARsKsTVdQy1wVvcZckjIb1ii77UM6XCndVWTGRbrP5JwsoYZ1i_WshUUobdWiBcvSJ2MTuilnRU5Y_cCLxYwhhQywe8ooAY7Uv_PNFc8vNaDq5R8kgrJ8hshwTs8jyLFRjSNwdut7h7ILFbJVdJ1jj__A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
یکی جواد خیابانی رو بگیره. بعد بازی رد داده سرود خداحافظی میخونه برا امباپه
😂
😂
😂
😳
😳
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/Futball180TV/100205" target="_blank">📅 01:18 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100204">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PVRP8sAzOrbmYx8vKe2bZogzxPXNKQzH4Ex-gP2P0-52VQkj_aaxE_HHDQZNx6HTwMssedLbyupopxERPt9voqf3-wOPymspJUFEKtWR0BwYaSC0M3YqMc1uhdY32U4cqwc4NsPdrEijiYTA5Klc8cw8GTklgH30vezqZzFWmDewXzC46ubCjZE9MHIUxVTnDR6AW3lfqH3e_QagdZcb2eH7YivbqQsEnQxVR7KK8Uxzc7rb78OEHdfvirgoWw6Pa_SCcr-Up-DPTlaCIq0pw-WfJjHI2jH7TmIYJ0nNCazntIcrXuEswTzvREQrSOQ6FUn5KS9bCrGT_LK95Q_9hA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">25 درصد از شکست‌های دشان به عنوان سرمربی فرانسه در بازی‌های رسمی مقابل اسپانیا بوده است
16 شکست
4 شکست مقابل اسپانیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/Futball180TV/100204" target="_blank">📅 01:16 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100203">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZPypnt7T3CCfgDBRrcZ7rcwwEFt_K2In-80DRyY0Khi80cZ9HEC1nos7eHBu4wki5JtDSuqLKsGiX97WpvSzB-WabT3j73GQKLiYytUkx5zOVz4ZM744PU_dIjCbfk6NRWAA8WJkSy1Np8twi5rqYANqgBPfhmAmMfZj1DDQ0QoVe1cUjjRD61Se9e1iD8PDkaCor-t6YvuAVALZKp_I_30ptiMOdRh0SUa6yC4_SaBn1crcJeKdH4mxPDAmdO5jCQBHgphcV6pLEeca92gBSOrOuQZAFN24sN5SkG3VYZWeI5tE9011jpB1H4n1HTIN9PNtfAthh3OEgnHAJasnng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇫🇷
رایان‌چرکی علیه دشان: مشکل داوری؟ قبول ندارم چون اون باعث این نبود که ما گل نزنیم. ما به تاکتیک‌های خودمون و قدرت حریف باختیم نه داور مسابقه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/Futball180TV/100203" target="_blank">📅 01:14 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100202">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oP-fDKxntqfnSbHaqVJmNI_GzHWNvrt-xVDYlniGaf5oUp6q8N_8uvLhfPko5Xyr88fc2Cu3_7uJGR-Uy7U1U8J73AHLqH3HgxqDsC2GwUu6Mcp7w-kW4R0YhZT9UUI21NfOyZeHnT1VG9BByi5bNt1wEy0Fg6YTRw-JitJ8c4U118FxahO-F3kQ_IEGKql4ydt4lze2aEdXadJvNZvpjP9RV4BR1l8u0vcrig5iymMqxrHY55AuszlMIZ-GT7FoSn-r1zHJUkOHD-k0wmxhtt4yvr9MMNcGvvA97m2-jadtdt7D05Vp79mftzD_eGPglFkkha2m9TQMFbV2ANwZ1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
👤
لامین یامال در 12 بازی، به عنوان بازیکن اصلی در مسابقات یورو و جام جهانی شرکت کرد و 12 پیروزی با نرخ 100% کسب کرد.
😮‍💨
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/Futball180TV/100202" target="_blank">📅 01:05 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100201">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jrEU_6hb3SpYJWja2-UQ5I8CeY9DEBY8ZRroarQ-JQWaG4TT5qt28LnZfx_mQbuVRcRQZbTtKBwKq3xyg5QNYgl3q2ZlASTgj-cQbihkjlUCk4BHvMUjwxv9pYG3wSvVXfRFFA4TunrMJxetdfYSxXHRK4413i5CGAwQlUSWG3OdvXYfvXjysD7AeKDirROu9wEqcT94Mp7rtEsD58XPZFYj7vLuLogduskx7TSvh9x--5UGahKl4fz_u3lwLo3ZE9I912bLPaGx6q23W7dx3fFGZc7AJ4RfCHKQWlOgjTQd8y3UYzSLjg_jRM4OVl-FRAi8VWWBWPisU0kMllKbBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🤯
🤯
امباپه در تماس با اکسپوزیتو: امشب انتقام سختی در راه است. خواهیم دید چه خواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/Futball180TV/100201" target="_blank">📅 01:01 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100200">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rQ5_t5pUgO-EbzRntJE3-Hm3Am_mang-sL3tpT-rqb9qGAcaHm1-dZ70nl7MMgDgTo4VH5IWhB6VYVxIzN9hfLk9AvUFbw3jL05WMoLRmSW-t2NCIRSXdzbGvJz609qpzOs7m8gYQmQUyOBodl0BVE5BQjubPKmBON3zl1vT-ZTmJor2MrKz_gtTZL8AGZ62umjgt7_07XFWm_nKyGa24RkoyFrPsWnvUBSYR-uct-WJFzskqU586DHe0BV08yeDyLm9y2S-iWM2J3oO9IyCIi1OKU1SQKLtBW3YTvTEtyMzttn4BRt6QIcXXEmkKOpNNhh-1c9EhMt8TeLBCkmP-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😆
یه‌کم جمع و جور تر بشینید مهمون داریم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/Futball180TV/100200" target="_blank">📅 01:00 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100199">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/256044b0fc.mp4?token=m_ukYFcd4I6QMhyElr9yAyr4ZNlZLIqx9mTVa5yjq4OOqbKugYZjmaE9UEhER8kLuBEoju6fg0-_zgcdZZRO_PhpxWlEbyPh1p65mzTZ0rmydq_-5XwZqMYa8Pw0H27rIykvUDmZ6uH7wu0omnBQlefYLvxXJrkkEq7AK1x7c9b-yTL4HAtlrdK-sGrqFbbTYE-tHZjX1EG1rCFqpMPtLRRf5dMwMVEgW55qRySDjLdGxuJpCZgNJss76BJhquNlFF9uDqRQOUc9foGjoc4nwlQDTMg1fhSfalwUEH8-5SAUBNkTHqFOZSEVy40km7CFWMeFBpBTkEaDEZ2dp7n2JQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/256044b0fc.mp4?token=m_ukYFcd4I6QMhyElr9yAyr4ZNlZLIqx9mTVa5yjq4OOqbKugYZjmaE9UEhER8kLuBEoju6fg0-_zgcdZZRO_PhpxWlEbyPh1p65mzTZ0rmydq_-5XwZqMYa8Pw0H27rIykvUDmZ6uH7wu0omnBQlefYLvxXJrkkEq7AK1x7c9b-yTL4HAtlrdK-sGrqFbbTYE-tHZjX1EG1rCFqpMPtLRRf5dMwMVEgW55qRySDjLdGxuJpCZgNJss76BJhquNlFF9uDqRQOUc9foGjoc4nwlQDTMg1fhSfalwUEH8-5SAUBNkTHqFOZSEVy40km7CFWMeFBpBTkEaDEZ2dp7n2JQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🇪🇸
ولی این صحنه خیلی حیف شد که اسپانیا گل نزد. یکی از بهترین کارای ترکیبی جام
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/Futball180TV/100199" target="_blank">📅 00:58 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100198">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mHO3u6afEhdTluGstwaXDR00Qwoa8dITvv27v_quWEV3yNxojid6OHYOIHpPnUEaW7EsVTgjQ13tODl0rsjr4vkH4HP22z7A4IQkBPnsANZB76tI0lcY5tUrx5T4Vfaj8fX7pFHxYvioPvrALAgwcAZqmbvlc_rE40dEVWoPs5u4A6Iky39BwswT_EUGY_JQ0o34txU5OC9lrKlVCvWtlMfzPwR1GnV2DT7-vgAEGw5T3QVV898JmrKlt09m9podKZrVtC16u-3_A6Dx0pDJ5yD7zJHdX0PZ76j65hTz_UT6viwd3KHujiGwE3-kPueOUGLf0iNGJ_lk3cTysfqvKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔥
رختکن اسپانیا بعد از بازی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/Futball180TV/100198" target="_blank">📅 00:56 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100197">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🚨
🚨
🚨
❌
🇫🇷
دیدیه‌دشان: یک سوال جدی از اینفانتینو دارم. آیا داور امشب عقل سالم و صلاحیت کامل برای قضاوت در این دیدار مهم داشت؟؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/Futball180TV/100197" target="_blank">📅 00:53 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100196">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a2aabbea3.mp4?token=vgR0ZitOBq61Hlb1bGt1Mpe_z5BY4wHmyYtTwpDF-vvqndvgxAdO5om4j_PHjG83zjapUFHmo0GwTd6yUg97C5cOVzXp--rbPxQiT4_PzNsjWYX-fsX5wkXVEOyZUb1l3LDv7YwzTApMhqCHF1e0v81ozsfBEGVMU-rnexQp8ujz680e92zhcW7bLLPg6gtjqMeKPmtmSUviy4woLPeQfA0JTBuy514fNvlXZPU4WO3Toxrpnw-AWXmTa9ciWc432jyJdbihvDZbmEbHFai702UHKn1qLaU2E3g9yeKdonLO_l1rcveVo44f2f4y2Ya7TaQlvL73Qzve4GrxW65eYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a2aabbea3.mp4?token=vgR0ZitOBq61Hlb1bGt1Mpe_z5BY4wHmyYtTwpDF-vvqndvgxAdO5om4j_PHjG83zjapUFHmo0GwTd6yUg97C5cOVzXp--rbPxQiT4_PzNsjWYX-fsX5wkXVEOyZUb1l3LDv7YwzTApMhqCHF1e0v81ozsfBEGVMU-rnexQp8ujz680e92zhcW7bLLPg6gtjqMeKPmtmSUviy4woLPeQfA0JTBuy514fNvlXZPU4WO3Toxrpnw-AWXmTa9ciWc432jyJdbihvDZbmEbHFai702UHKn1qLaU2E3g9yeKdonLO_l1rcveVo44f2f4y2Ya7TaQlvL73Qzve4GrxW65eYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تکراری ترین صحنه دو سال اخیر تقابل یامال و امباپه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/Futball180TV/100196" target="_blank">📅 00:50 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100195">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🚨
🇪🇸
کری‌خوانی دلافوئنته سرمربی اسپانیا: امروز مقابل یکی از بهترین تیم‌های جهان بازی کردیم هرچند حریف مقابل بهترین تیم جهان شکست خورد
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/Futball180TV/100195" target="_blank">📅 00:47 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100194">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wr5VUiAmevuZSgzk1ivcTG3mosbdDTyad9LIwpt7NwCeegYBNyXd3zykWNquUQHhWxGgHnUXbrgshKW3WbqguY9kF8zlzGrxxRexwET9o15yEgIh2MlkiM6dwNVr5kWCCOuTTgerGYUSLyLVAnnbl13nrCu8CxC2wjbVgkjktJSD-gcFGMplK6ihF0E-BHdQ03s6Qwchk0Cdb9KHHCCCUrmuJczt8iRzbFhzWjIFi7veEES83KCX0rWiUFdt7CijEaewVmMINKzyv8sIcsW7oFPzURYUTK-3lNcu9jh8sJ4_Oh8d6I2gdKTwzjt0x1t0VxHgfmP2DotJE-IDahQ_4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇫🇷
فرانسه در یک بازی برابر اسپانیا، کمترین میزان گل‌های مورد انتظار (0.30 xG) را از سال 1966 به بعد ثبت کرد.
❌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/Futball180TV/100194" target="_blank">📅 00:46 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100192">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oyPnKWAPNM3vIxHpvLpvks0CNqfCxI3AjdoxES7Bn59i4fBv91NO56FOz6hfnDXsRJPMIMQcIXgFfgBpnMR7KVnL2WY4an8llDhopdkW-Q88r_CfvKP81wORTd3uUwWutBuAm3WlGJC8JLMsftDq_lb-Xd5bMO6B9S_uhvgg81oYPJUVK8IjbE1GML8XvaRwDjhtnsf9ielD68BJc7i2wqtOPPhmM--NgHnxqPuOC2VgreHUDeTO8fPWLOrNSW6W8VUeVoAYmO-R26gaJCIEu97rxpD5HrrKXgM0kNtq3K-EfcWNXQN4USY7bymd5X0MWMSwMkqpuU2wdmwl0PdnNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🤯
🤯
پائو کوبارسی: کیلیان امباپه ترسناک نبود. قبل از بازی هم گفتم که ترسی ندارم. من در لالیگا بارها وی را مهار کردم و برای از آب خوردن آسان تر بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/Futball180TV/100192" target="_blank">📅 00:45 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100190">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn5.telesco.pe/file/BpliGVFJAc0OLOsfsAyXZAEEGA0PNMQdY3Bc-CqwteGKgL163NNHzIHZgPH8_XD-SXnV71rOGKGXpaj2P7C3290GVGZE6nhHT6kDZrNngNGlsomxCqf2PLtBZEnaBNd_Lc92l2MLMcXlA6B1Pnk_h4FJk5HUd8z_iSkg6p-alzXbYbNrW2wfFAaqvk1s9tRQgn5KOnvweEJfOaXZ2znbjZdQxLts0Jmn4ooZ1ywXn2YVq4Yfp5CHlikDflSjBQk0XiRNWxW9KrK6RuU2yzLBPdvaIkH3695PhzckyM57e0fCKHbpQTuW4REDMOsOd4NJjuUyZRSgl2mB-n-iBVcnQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn5.telesco.pe/file/oZdqeIMjc6E3bgqxf-P9WN9deYLGKvzhOf2-QnyxTryNxDflwgq25UC9cUcasFWPZSmQKqRjEIEDVSf8sKeGAgr8w2eHbkZm3NQFGZ1iYZi4V_NY5M8SafRwcYwEVYOcRUUk-m6Mu7MCJ_OGRLDcCRG9HIBj9jjCOgMFxPmCFb50SKSytXyJXUWCaINi_WgODasc3bHaNOPhPTgXM_t7_N20iZKIeY6wDRMBh2t7VshJTNJFVTSqYxMC-ScmJyUwFBZdphAseY3BAlJEhBGSOKcvkkUa_bjawTD3GP0oizNo6R2fiE7pYpaffQsL-3Fa9bRfA3aEOhKrMPxdEQP1_A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">رسانه و این حرفا
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/Futball180TV/100190" target="_blank">📅 00:44 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100189">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/DCJwSRWLKebqwAZiP2D04GncGRs1RfoWrYQJEZN5_lFaHnXVqT8XuY1B5KhQA3T-wEOb4foWzevCEdXB71TeILbP7kFKo59eOqDJdv-HIeSXWTOdwZnanTWuXjH2OPDUX88U7aLY3YaJ5Dt-1KOemqgXcKKTRMNY93acY7Ix_kkD2uhSVdsy7NNuY_U4ZVmHs_3CWJg39qUlfPu24cE4UL4PbAUBW_r1ojCZqw4wU0QYCWZQFbDP5lctpn1RCRnYtoOC7vkrZKJGR1ycgdCGSUb-EYXKygGQ8xqdPcH-5Mnu6ud21PQYNJZSQluJcLrnfmg296r3Ff1oqiYbW7M6rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🫡
🫡
🫡
🫡
🫡
🔥
Respect For Olmo
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/Futball180TV/100189" target="_blank">📅 00:43 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100188">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/HuPZ2MLU5yv1GckVhp4rtjFcApsiEbgQA6OstD8p6nRstLQi5mrfUcNiThky0xmBsii34igCb9E16EAmRB9QC7umArbBAFd7nbBKBynxDM2PIhp_MpFS8zgH9S3pH7VQe4WPxMA7EQaJFx_lGLyN0pJWFJzvuKsx8YH-bwJpDPtQ0YdUSu7NIdTzyjny4JJ9pFvfT4aY0H-Ik2MYPGjvMLQ00gu_roJcNUpdY9L-M_7cTwklvOXJqsfnsoa6WfolEZXYur0f7n8M5Ism7lE3Abt6RT8zxjQUPwEgOcH4eRP68AC6c5T4OVDH3THHtEoels7yA_Sacl0VpPjm1xBV_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رونالدو کورتوا امباپه بعدی بلینگهامه برا
شون
زانو بزنه؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/Futball180TV/100188" target="_blank">📅 00:42 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100187">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">قابوووووو از دست نده
😆
😆
😆
😆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/Futball180TV/100187" target="_blank">📅 00:42 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100186">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lST0Sdio9_LZqkvqmL5hf1WiV1TsMxIKWKcoIytrWv0BNRb4UEXDGJObkamJoiXIGY7IwAtVhIEcejDHxhnciBlDXOHxOmKfUnwmxw2URyMwqYDidYfM-8V4PrYi4cwQ_uUtuVDZ4JxmgYoXsuf-lm2XGglbo141u0tF-nXudbzFpAtJ5ZPQJ6QCCSXD8D0lhZMu2XfG12x3l2eWJ7yJiZsH2hRwwCWVBI6tWMFqt0QqXxdMuL_ty3WKevsVUiX93O3C9hhIZKs3aGXqhqYIGRq0E2YstzqyPpomoyED1Nc4Tt2WULxOndh6eooTxf0IbFmctJ0_jeI6__tjtA7Nlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇫🇷
#فوووووری؛ دیدیه‌دشان از سرمربیگری فرانسه برکنار شد و بزودی زیدان جانشین وی خواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/Futball180TV/100186" target="_blank">📅 00:41 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100185">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ohSfqnqTG-_7t0jyUUTHUE3uXaJULldH6Qq7w1eRRb1kgwPfC5Vb3hzdTGcI6v-CzzBLxnn0GvvIYeFJHsOmsiAKvk4p-X58Gz0LTJuKlB0gXzbg9avZxPSHWJh_DJjg6AQst90UhkHBd1NaRU7G0u2Arh7KeGPbOjDHUxLdRca67YDk7Y6jdon-reAaBlngztPVNCCSb8xSGpSHIccS9pzDItkrDdPsJ4bSZOlGCdXaTityuwm_8v73XaiytYwyik5qSbE8RZ8c8BRFRaK9llRuSqXYGSK3dX4u-tQrP1lkxsghe65bfsXjZEHTztqBLrFykabrVPe__8JswxTP9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قابوووووو از دست نده
😆
😆
😆
😆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/Futball180TV/100185" target="_blank">📅 00:40 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100184">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sRtsxAAKalkVW3AT8lhh1S58yELgd6WYmF8P8-bZVrb964A-AOcYEYSx0BSPdRnh4Nl97vMqcVrfeGBxAsgA6v48gSIio4Rz_HS8fSdhh1LfJr8xy-atGU6cQCYttg67Tx0IPmqJBMKf_H5HF7c9TUmcsdLHcEUj8efMwJeUbHchyHZeFw9rl7eoBX4ELI_S2vu6WSHadQOZsuJrbU8A4ggrk_EJVDjXeskL3ZyM2yUxkR47-qXbiUYHRKZyDOT2JTTTAJ8gMK6DOgqvc4196QdMuidwEuR67E-Nf7eGQ9zDamrt1m46rRft_TkQ_JATbroeoCZJhvacDRuTcpoNSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
🔥
🔥
نقل‌وانتقالات تابستونی رو رئال‌مادرید با خرید کوکوریاااااا بردددد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/Futball180TV/100184" target="_blank">📅 00:38 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100183">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">فک کنم تنها بلنگهام موند و نصف دنیا مهاجر شدن انگلیس 🫩</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/Futball180TV/100183" target="_blank">📅 00:37 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100182">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇫🇷
#فوووووری
؛ دیدیه‌دشان از سرمربیگری فرانسه برکنار شد و بزودی زیدان جانشین وی خواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/Futball180TV/100182" target="_blank">📅 00:37 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100181">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iRAYcbWz0GFcMkBFReri37tRtLVnrUHv_Rdf-8uJSdoERi0ihx2UHgolieir-jUHH_LY-dgs57BLG-7NU5cH_Mr-rSL6gsfck2Rd3dj-HESyG4tKkHKX3iLzgVOqjs6sgR_sXfRogo7K9PU0VwQGiGj1hpjIqwvPsTTByu1zgQMco_aZDk6z6EvJIZzcS8POoBVI2wAeCCAHCwjFxxfUxH9lGpHXRAQMMNtFdYNzKRLwDecPxoYilkwIkqw7uPoOfTEcj33UpxuNXspk5hPxoDz8V-dUwb-bDi0qzSU1QBhYi-xofxA9NqdQEOjRq9D3n-nritWEinVeec3IQyUjpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
#فکت
؛
کیلیان امباپه تا این سن هرگز از جام‌جهانی حذف نشده بود و اینجاست که یامال 19 ساله وارد می‌شود..
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/Futball180TV/100181" target="_blank">📅 00:37 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100180">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/sIIXoANaDZx76DdM31dsCu7QKlLZs-J09zc0eaGglH2t-npX-JZFCdp-u0tTEVj1VLyT75wT1OYEV8LsG7MyIc5QFswglo69HkRQLlesETLv_d3y6zqWAHPyQc3hXxzv6GtaPsh6a5cUxl0FHxrM-fdrTKZZS0qL-nd_LlVix2rk2KOCMm0N3GG6iJYT0o8kV8nP5T8bvi0F3t7M29Cdx8ZrIrAXREn9ppgbwDhQbxaUt-WXnGnvPOyiyV3RUodykZxUh3bc8odIH6JBmocX2X8xsdAh8tWvqab0OPYqQqGl2mECQ1nMGPGKja717mXTP187nuU_9T1JSFOsSKFQww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مثل یه مرد کری خوند و مثل یه مرد یه تنه گایید تموم تیم فرانسه رو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/Futball180TV/100180" target="_blank">📅 00:36 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100179">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OCQov6Hh_xCl38NAEgGjA7np3yF_BLTSjQMn8x3aKm5q0gk1RZPz2EUcOWOShAQnvIUJvWx7UtcefAFtIJ5f_K30QBM5X_CSdiWnZbLOdJgMt2JthS8ODb-r2e9IVWv1IxipyBS2eWL36Dum_igHGisjkx7vSqClUyL6ncjMVs0JDF0FrasbYw1AIPfnNs4mx__liLM9rBm-kAUW3hIl27Wsr40GUTD_0wdmzTdd5NZEJvcfpiJwbkSmTP_ObjVEG8K2dxgqM2KoaPifXBQcey-ZJIp4dvzHkCWBLDf98Qe4bwfR8cr31XAq3zSyrRmyjyVI8tTHAQ4VWIgMI3L_qA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🔥
🔥
🔥
📊
اسپانیا با رکورد ایتالیا برای طولانی‌ترین نوار شکست‌ناپذیری در تاریخ فوتبال ملی مردان برابری کرد.
✔️
۳۷ بازی بدون شکست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/100179" target="_blank">📅 00:33 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100178">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IOr48PT8UYGVfyoNeezdPoLNQQwK0tPAmCIs22YmElLZaN6YD6UAY0FL6qv0E_DctoPbdb_-lH8wCRts3I_LZ-3nlYT66ItYAKhC8ijO_wRa7aZvrRCYcM4AtOsbhuZ9SFlVkOkS1ZMRKk3lNe83uTV_tX2VRIrMy2WR41jOQkGXFbu153z1ddf-GoiZlTte7ZgR9Av-jAJBCKP5RJenEuA5etsMp-cSjjHSMkpR8YAKIUqQbTzroR_HnpuYe5_7eNLRcXmUDY3SXHfs-3IC3uHeU9I9lLK-sWuWkG8vNRcJ7XlRR5YPZJrMZD9QfjYGETyVYP5gwMsHrx5Cbydrsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
🔥
😆
۱۹ سالگی کری میخونه و حریفشو میگااااد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/Futball180TV/100178" target="_blank">📅 00:32 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100177">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QrmBXhiH7Lrv4gZCuWQAloPh_1Bms83SdzQv6j08Wd9dleHEkesA5y4bGcrJm3LutOLL1Po_dz0jaBuVslbcWl72STy6fleO1Sc2V0BIyq6BdTR-fSsK1Kkb28m1R0kQ5x0mh2vLdJDecqfrCDXHIGl92DqJcPkcaRG9wIVCKyjkSONWW0HfRr3NWUPZyyHOGQ6m4v2mxHr74BBufMzd56_VJcmKfs_XpcmrhZ8cFFp2lLjpC83Iv0g3hBNLOve5RgyM7MoLPEZFzFZGHrlr2qA0ut4evzc-PQmgEDMsM0hLFnpRJoEpB4Q2J_5uI57AxlbYFqvG9ZPeuCidQ5RLmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🏆
پدرو پورو بهترین بازیکن زمین شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/100177" target="_blank">📅 00:31 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100176">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Byibf6bapnRbKL-tymTWpAzY2o4FYUJ86ivbbwbksPI2Fe5-cyogZYTOSloKDmODopc5r5mKhB-rA5FtbKqQswZS8BLtcrLngaataCBUewLQAukMhrfE-0hl5F-O9ktKvS4fqOExh_KMSdNjqVLnnDIjrJXzBgHPFEt6IRvCmgMFzex3hVjuwBzkUARu91hyRYWXp3dyEyr-sWk3Tk8NAqMzT6tGCQsFIFcSxdi482ZvYpljahKdpFs6xPxErGUJJWL_QAlkiUiGP0eYFF2j1VaCyLWqj3o3W2_wjU1cuZWFtHhjjkMdKSRDKxV7ocYXebaO7-DMqsSGHjaD7QZfQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امباپه باااااای بااااااای
😆
😆
😆
😆
😆
😆</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/100176" target="_blank">📅 00:30 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100175">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🚨
🏆
پایان بازی | ۹۰ دقیقه شکوه اسپانیا؛ فرانسه قربانی فوتبال تماشایی ماتادورها شد. خروس‌ها با تمام توان جنگیدند اما اسپانیا برای فینال لایق تر بود!
🇪🇸
اسپانیا
😀
-
😏
فرانسه
🇫🇷
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/100175" target="_blank">📅 00:30 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100174">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vHOddRHjpejIQse9WqXgiyF8wzy_9U-L1fdJKR4DGgxYOZnzduBY7fZ066AgkOZoHeqoJRcuL4VA4nIW3SHFmzc4sUnHhapIPm9jYbe8dNcaSA9ICbaIBhz41pPZnPvZy1dse0Lvo5lBtipx4PkVDTqQxswJquG9W7SKyuTiXkY6K0z6_fTmSA_BZrwSKE_AEsuqa2_Mj19Perp0v5Qute2Pt7FCR_FAJR3J4cnvLyiNKv54mASXkPhBOjkerWXCklfjBoUXj4uL8BqZYqQM27sGdvE2e-iDVoFgEAPpH33MDBuTZkrV9oXiKcZCJfEbfaK9ORA9FIl4lYKOuY0yCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
پایان بازی | ۹۰ دقیقه شکوه اسپانیا؛ فرانسه قربانی فوتبال تماشایی ماتادورها شد. خروس‌ها با تمام توان جنگیدند اما اسپانیا برای فینال لایق تر بود!
🇪🇸
اسپانیا
😀
-
😏
فرانسه
🇫🇷
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/Futball180TV/100174" target="_blank">📅 00:29 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100173">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">امشب یامال نشون داد ریس کییییه
😎
😎
😎
😎</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/100173" target="_blank">📅 00:28 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100172">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">۷ دقیقه وقت اضافه</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/100172" target="_blank">📅 00:22 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100171">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">‏
🚨
🚨
🚨
🚨
عصام الشوالی:
‏به نظر من، توپ طلایی سال 2026 به سه نفر محدود خواهد شد:
‏لامین یامال، هری کین و لیونل مسی.</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/Futball180TV/100171" target="_blank">📅 00:22 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100170">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">امباپه رید تو کاشته</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/Futball180TV/100170" target="_blank">📅 00:20 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100169">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">زرد واسه امباپه</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/Futball180TV/100169" target="_blank">📅 00:18 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100168">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Knovjh-P5GG7U74mwwfUWeNJ-FSMYDRs6Y4axonOKq7Gln68b6TP2IbS2O0I8So126QCcTAy8YJAdJ5s_AznZvowhAI4hJq48EzFvmOH7o21lJ9NOrvtSUWqW1KKx9E_gIHYgmOJ-elBR3AkoOoTt1IxZjRgOw2Gfyminmo-4ZdesrgaYe-YY-cYOjzemB3ZnMMruQxIDksBohbOcRCof1HEOeTV6yFO8RUUsaXxNq0_YWs-Cfg7b80ToaOOVtW9DQ7DIBcyDeJMRATsLGxXDq9V2tXN7WczI1Lii7HUsWbkgDIwoYViJ0v92ePcABFYvVN0WlHyi2-97w1fOgqNVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شاهکار لحظاتی پیش دوئه
😐
😐
😐
😐</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/Futball180TV/100168" target="_blank">📅 00:16 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100167">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">یورنته هم بجای بائنا</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/100167" target="_blank">📅 00:15 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100166">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">نیکو ویلیامز به جای پورو وارد زمین شد</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/100166" target="_blank">📅 00:15 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100165">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">سیمون گاییده شد</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/100165" target="_blank">📅 00:14 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100164">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">امباپه به لطف یامال امشب از ژنرال به سرباز وظیفه آشخور تنزل درجه داده</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/Futball180TV/100164" target="_blank">📅 00:14 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100163">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">چقدر بد استفاده کردن از این فررررصت بازیکنای فرانسه</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/Futball180TV/100163" target="_blank">📅 00:13 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100162">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">واااااااای</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/100162" target="_blank">📅 00:13 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100161">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aRBMm6lGmm8fxG847zDkjSpAQ97yGXgCMpT2LPzbMUwyVbFfJrZA06XYS_BhIzh6xoyqWmgatTIFRh1rXNdiWv549eGneQluMooszzAjodvd-bfcjw58yQxi6NYAQ-br6t1AlXK2zD0yh0m8CPRhYl_C69nBAh2xSgR4dXLa7Z1DqikE4chjRDCkFIsqfgCl-CWKygSLJfc3NhfoMAgHbw2jrlmSjQTJ9-jGKGsQhGnFa3DR8_0i9WF5h0cWpi1v4o4REZQs0uYKSZLpEredKnkNVhyMNsCF9ixS2s2k8VA90Ov6r1p_6ujbxnxC_TwwCMul08t3rzZWCLuvacEjYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رفیق رونالدو وارد زمین شد</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/100161" target="_blank">📅 00:12 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100160">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">اولیسه امشب جوری بازی کرد که بایرن‌مونیخ اسمشو بزنه دیوار مهربانی</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/100160" target="_blank">📅 00:04 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100159">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">اولیسه و دینیه رفتن تئو و چرکی اومدن</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/100159" target="_blank">📅 00:04 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100158">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">زیدان هم بیاری این بازیو نمیبری اقای دشاااااان
🤣
🤣
🤣
🤣
🤣</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/100158" target="_blank">📅 00:03 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100157">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">لوکاس دینیه نمره ۵.۶ رو تا الان گرفته</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/100157" target="_blank">📅 00:02 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100156">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GRHzPIiXg45oIsPYp5JC2h3j5buoeARHCiu4MUxXUcaJ1ZOx1yDml1BOjQT1aPgIA3Plkoc-nbBMlN3YtSsCxfSbnB8LW-QdpRnt0amr6rHTwVzi6C1ZxVLxFmzAcmAoRLaaoKocYIrju8qRJ2KKOycUlfYIl2hKw5LCd0AKPySsLa9U6p22UmEJEXbZl_-M3V-hVbnPKHRK4yvhjpxJaaGBbeC3bxaMeAfe-TN6wcF0GV1jUM6-HiIS1y18fJkX-Ncx-hhVoboF86r2Snv19mbxZL65-8nNrqGHA0jusmQR-OGP9wd-uIaOrDhNAZ5IdGpahX4YRg98g4yvo5KKCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
🔥
🔥
🥶
🥶
🥶
تو ۱۹ سالگی ترکووووووووووند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/100156" target="_blank">📅 00:01 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100155">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">امباپهههه داشت میزدددد</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/100155" target="_blank">📅 23:58 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100154">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">واااااای</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/100154" target="_blank">📅 23:58 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100153">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">فرانسه این بازی خروس نبوده مرغ بوده</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/100153" target="_blank">📅 23:53 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100152">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">گلللل سوم ولی افساید</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/100152" target="_blank">📅 23:52 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100151">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/c10bc62198.mp4?token=QAE0SG-5J_c00qJ-y4omYPtmYocneOvVKVADvWezn1hoZUKdV2dGo-nhMjCrvaQUu4coueNO0h7eJUYyJG_pRkXJobROZ3zpYlvauBKQtYGxVXYshshpdqV477kD6e6ivjJ66v9HpiwJb2nvRNVE5cXy6rFhwWGcnR4CnYx4mx0ll7MdZ33Cagtk7_NcBy55Z-uTAyggJYRD6kp3wObBB3AlCe--d8qjWtOHclvLUuFq-x_lKHZUYaRtYhR4888fLVPx24r9yzVXjrGU3hUqW5-urCE-G6kmiMKtu1Gr8BYR7fHy23eRywYoYiyESsOFypcJs8vle6MYvQkDHVQyzw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c10bc62198.mp4?token=QAE0SG-5J_c00qJ-y4omYPtmYocneOvVKVADvWezn1hoZUKdV2dGo-nhMjCrvaQUu4coueNO0h7eJUYyJG_pRkXJobROZ3zpYlvauBKQtYGxVXYshshpdqV477kD6e6ivjJ66v9HpiwJb2nvRNVE5cXy6rFhwWGcnR4CnYx4mx0ll7MdZ33Cagtk7_NcBy55Z-uTAyggJYRD6kp3wObBB3AlCe--d8qjWtOHclvLUuFq-x_lKHZUYaRtYhR4888fLVPx24r9yzVXjrGU3hUqW5-urCE-G6kmiMKtu1Gr8BYR7fHy23eRywYoYiyESsOFypcJs8vle6MYvQkDHVQyzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
گل دوم اسپانیا به فرانسه توسط پدرو پورو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/100151" target="_blank">📅 23:52 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100150">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🤣
🤣
🤣
🤣
🤣
خوب این‌ پاراگوئه نیستتتت عزیزاننممممم</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/100150" target="_blank">📅 23:51 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100149">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">پدرو پوووووورووووو</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/100149" target="_blank">📅 23:50 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100148">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">فرانسنسنسنسنسنسسهههه نگایدیدیدیدیدیدیدمممممم</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/100148" target="_blank">📅 23:50 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100147">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">چه گلییییی چه کار ترکیبی اییییی</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/100147" target="_blank">📅 23:50 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100146">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">اسپانیااااااااااا</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/100146" target="_blank">📅 23:50 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100145">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">گلللللللللللل دومممم</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/100145" target="_blank">📅 23:49 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100144">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">داور قشنگ با فرانسه مهربون بوده</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/100144" target="_blank">📅 23:42 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100143">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">آغاز نیمه‌دوم بازی فرانسه و اسپانیا</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/100143" target="_blank">📅 23:37 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100142">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">ربیو رفت بیرون و کونیه اومد</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/100142" target="_blank">📅 23:35 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100141">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SFVj0AdCDG-bnxrleb1iNlnJR9idCCDnFR3Qv3Nw1MZ9-h63lQV2-J9e7lhUhILeYGjqggVmBS_6wEg8YLeHawuRPH-Zyo1mjnmDQVFC6EiUXYiYlBWAOgFx_MQCF5D1cA_h_H0EYm7Sf7MFC1Hh66apZJRtHhfR6rTpmtLSHA2-h0MG5LZupdcta1KMcPfcD-zO3O75UYdosIZmgm9RrTmIo2rj8sCHMTGzqcdmh-N4v00qfKd0ild-9aSY8DI2aHJPOamDAFGtnd6v91SqpPiE4BDZMLMpScdvoYXUtUv483sMRC7PRPmp8SPWWEmrZ8NrfJttXguKo9rjLQCYgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
🏆
آمار نیمه‌اول بازی اسپانیا و فرانسه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/100141" target="_blank">📅 23:34 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100140">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">فرانسه نیمه‌دوم بازیو برمیگردونه؟
👀
⁉️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/100140" target="_blank">📅 23:33 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100139">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f_X7tb-6a1pW_zd9fLh80xbIbK2FkZIQPJXbVav_GMl4v7I8g0vDM4JAMDP0mXWO5jSMVoC7CaNsJI36GnWkdfOkdV9cI8PJw1dj1ebAPqgMlgJtVlRHjBRYJ762_U7sVua7ln2-Oz0qeGv5VodWY5h5vdSMY5vOAPgwHbNEEwM6wjvYzHw9xHAwOXAq7oYr3ZbHaIfExpFZWbxpUCE_hLaoWeyWJwV3bPjgcRBUlzQ0_B4QDugrhlo-dAxHG2b09cQ3hMshw08blSZ3237rhMjN0jOIjwwKLzke8n8a0KtDM-6RwmajEkdVd-dQzSo1iMdrQTCrJGxR415XDYXb-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرانسه نیمه‌دوم بازیو برمیگردونه؟
👀
⁉️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/100139" target="_blank">📅 23:31 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100138">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/R0IE_Ay-f31A1fG5k-8aPqiAL1mGyVPvYonAH15ski6OUWUaGFHIve0Vmpzi-T3L0NbU2AZi4mULvj7HHQifMIb6PmkkwTIgrxO2SCvaqZFPuVu-lTVzZvd7gstoH7V_uz1QBavPwNo_O7uXMltDhDMp2NThKtR0JQAJ0LTqsfC8AURjyihnUv26pM24WpwoWVK8PLE3_rgPBnFnzJoGeENa31zS8ZjvCVvD5QWuf7kVzkPzAO-nZkYa2uh_ynOoDkgHAlJvOrv65_gYqJrUrB0Oys9rWlM2dthpPCrvEsX-3Yjn5Rf3-NOKGNHhYt7KgxlwuuuyOchBb6QBgeuU_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
🔥
🔥
🔥
اولمو امشب تو نقش مسی داره خط هافبک فرانسه رو میگاد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/100138" target="_blank">📅 23:29 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100137">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l8Iy6HLKp2dQiL6nYXUKXthXxIyvQKdxYHghtTMJBJdxfy2pujnef8lbVxzKJsFMUbyhJyeK4uoLCpFHIpMGurExsGJ7mZlczIjLkvKUNndXq2uYwk6sFNXF8UyyBdUDsB1INFxncTzKsw9pHcha6VmCC62CVrreeNOyHNiCIpXgIieeKaFYD_Si2nO_CPBFEjC1sW6YvrpD6iy9j-aeahwF1hl6UQ2-LJ9wUztzZJElSr8JLv_1FkXXUDYwXF1qev-9XP6TdYIo0bsNU-AOKOqq6eSmuCmKnGVYDnZY-AP3p677zxYB68VK4yBuwfKNlqq4qo6I9ZxAr32gB6VmuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
🏆
آمار نیمه‌اول بازی اسپانیا و فرانسه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/100137" target="_blank">📅 23:27 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100136">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qSyxgPvcogePCFCFAmGLChLa6ecQTYx5eItoKc6xSczhmH-SS-FfpiU4audS0cupVOVnV1uRRFcw4Qj-sd54Vv5rCzUSsQJPzcBVkmgBMkfbMztP4KIw-8-_9RyulextoRLsDaEm2qG5tWEfCyXfGz7BBG6cKyBIiRr-Yt_Q9ErUSZLNMuwnMLwQpP1GmBy-apPojgT-MmRjROOBVf0XzfNEqxjRczfUxtTwcE7kroov7WXVJgTiUOafokDPHD6jbCmOAXGYW-LL07k4q8pMIlneIFy9yxs75Jx02fmXQwr51iXG06SiYdT3W8UrzxQ5JQWqVMvmVCR0u-EMecC7Zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇫🇷
برای اولین بار در جام جهانی 2026، فرانسه در نتیجه بازی عقب افتاده.
❌
❌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/100136" target="_blank">📅 23:26 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100135">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f951af3a7c.mp4?token=aXTueyAhfQrVsl4vVJIrwYqcbrF3sfvk0KYgmEYcpUhpwogJqy88UemGlGvlW5syC__L-kja1wduj3d0ZmRHtNRqkDWJFb8pBxdB0Uhr7o98031QbHiTqdlhO0IjFJfPOChlJXv2O8tLKcMeYJC_H3a_nscvO7Ni6C_7r-qguWUt_Sn_BVXKiXNoLc8txgAJuBF2xsiYPc1EN6NxsOrM1SF3q6VFeAEca976FVNjTZTlbp4-m9uhH0Lsrw90b0NjPeKIVq04XlTOVDNWBDfidaG2aYu7-oSJjDuQZy5jCB0rFAwB-kUDvSIQuDSpDk333ll83mymdqL5EuxZyVwSqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f951af3a7c.mp4?token=aXTueyAhfQrVsl4vVJIrwYqcbrF3sfvk0KYgmEYcpUhpwogJqy88UemGlGvlW5syC__L-kja1wduj3d0ZmRHtNRqkDWJFb8pBxdB0Uhr7o98031QbHiTqdlhO0IjFJfPOChlJXv2O8tLKcMeYJC_H3a_nscvO7Ni6C_7r-qguWUt_Sn_BVXKiXNoLc8txgAJuBF2xsiYPc1EN6NxsOrM1SF3q6VFeAEca976FVNjTZTlbp4-m9uhH0Lsrw90b0NjPeKIVq04XlTOVDNWBDfidaG2aYu7-oSJjDuQZy5jCB0rFAwB-kUDvSIQuDSpDk333ll83mymdqL5EuxZyVwSqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت اسپانیا تو بازی امشب:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/100135" target="_blank">📅 23:25 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100133">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🚨
پایان نیمه اول؛ اسپانیا 1 فرانسه 0
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/100133" target="_blank">📅 23:21 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100132">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">۶ دقیقه وقت اضافه</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/100132" target="_blank">📅 23:15 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100131">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">اولیسه خیلی بد بوده این نیمه</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/100131" target="_blank">📅 23:15 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100130">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">داور گل کشیده؟؟</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/100130" target="_blank">📅 23:14 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100129">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">خطای خووووش جا برای فرانسه</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/100129" target="_blank">📅 23:14 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100128">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">خطای خووووش جا برای فرانسه</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/100128" target="_blank">📅 23:13 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100127">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">چه حرکتی زد سیمون</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/100127" target="_blank">📅 23:12 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100126">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f1RDi-A0zYZy---hCeBG0POw1P7jkQyHVHCfyrLYprjlfo-8vYLmMXHKs-3zOq-bZbavOOYg326iEj0MtZ78xoE0L8P-LPNd8em59D7dg7xf2lRuFProh5FEGPAa3QDFhOtbaRGbNQZRtPdZFKYqmMhbr0N618RlXLEmkwenEEq4GAPIKz5WBnavevUGTmzZVra5GQf9v-_mL2FdbyCQrMDAQDg96xy5vn4VSl_0gZcgV8FaPXs5g_yDk-TuZLKu0DKi0IJtZ5vgV3x-xfTJESTQi7hMBjIv4N6o0aKN6PXhQWPVOnucuZruB2IU58LINq3nlfCjnM2gbhwTA9bL6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🥶
🥶
🥶
🥶
🥶
🫣</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/100126" target="_blank">📅 23:12 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100125">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">امباپه همچنان تو آفسایده</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/100125" target="_blank">📅 23:11 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100124">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">امباپه همچنان تو آفسایده</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/100124" target="_blank">📅 23:11 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100123">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g9Bb39F6R91nTWIFRGSAYLYw2f47zIYSqk-V3VaSorL112dG4RsCzqTMPNwxitIyo_BdUSVYA9bFB46a8vrw3urXS4N_BxXiv_WQxBf3wRRrtKhBffqRJ1UDBZ_X4-ycXRQ4Q7acYNfBiBButYEffImwAs5xJvlLF4lWh6T5r9jA-UMqwnT0_lHHvqYisOIBWE6PgH9I8vIAKeUZl9N2-USAd75VmD-1zKn6QoEIozRW6axXfJzKdBuOH2sP8yKvX5Co9612H8JusDSvwjYjLu2GA1_aaQMv-US9_QFIJ3xJIV6s1LMbf6BoQZ1rRemYgSoM2CMPVVPH_ZIwe1q1bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استوری نیمار از وضعیتش:
دختر داشته باشی و وضعیت خونت دیکتاتوری نباشه؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/100123" target="_blank">📅 23:10 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100122">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/767e8b3586.mp4?token=Z2GCGE9SeCMqUszfRWP8oHkti9qdOcEr7p0rzu09GMMk_R3lLpqNyLn2-9O6VrXykBotcCu_8BAPBcMH_KGO0pi0Vh4rB1Vv21oNX_GqCaORc3BB2FZlINZffbPMps11OLHxUy_S4EnI4sfgAE1sSVaS5MmRYKymQO_lgYMazvqJEK7qSo9JQUBQBrADKOXxst5xyay8R8hdpJdxbC3U03vehStWXUB5GyUW5PuBCurD3x5lUdTonsCL1gduBl3Up2UDDatADqSzcm6k0XJESkzOTMLKI9nNs5bceroiv0Ao59XEY_xeYTM5hJocWGfV51er2HTfnZ21_cKNwz8yt6ytmVcCzZ9T50PWURykBpJPo9U-MO6IrhADRI2oqp4U7Y388yBR0sf8xj89qtDiFo7cmkyajyaOjuE_2j7_j5aeKP6EgEx7WlTsw72-6GNGP3j_iolMG_AmmFw6Yvuz2qgvlscjeTacEPqNj18QW-yJ4e5u1dlkgcJ0ebDopO12HLQSyE4a4jjl587Zo8RMj8-Vbx11E2ITDQKkN1HsIbAhrh_Qs3bw5irlgSU67QdESCiMMVlanBZcjQM-WTBYlQQF006Ll1THzZYWPrWw2NbP3aUKvi2V_IeL-t47Vm2iUGS8L_e6GplVbWeQtvgwY8BD0cuOeOqPpIpKF5uOgu4" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/767e8b3586.mp4?token=Z2GCGE9SeCMqUszfRWP8oHkti9qdOcEr7p0rzu09GMMk_R3lLpqNyLn2-9O6VrXykBotcCu_8BAPBcMH_KGO0pi0Vh4rB1Vv21oNX_GqCaORc3BB2FZlINZffbPMps11OLHxUy_S4EnI4sfgAE1sSVaS5MmRYKymQO_lgYMazvqJEK7qSo9JQUBQBrADKOXxst5xyay8R8hdpJdxbC3U03vehStWXUB5GyUW5PuBCurD3x5lUdTonsCL1gduBl3Up2UDDatADqSzcm6k0XJESkzOTMLKI9nNs5bceroiv0Ao59XEY_xeYTM5hJocWGfV51er2HTfnZ21_cKNwz8yt6ytmVcCzZ9T50PWURykBpJPo9U-MO6IrhADRI2oqp4U7Y388yBR0sf8xj89qtDiFo7cmkyajyaOjuE_2j7_j5aeKP6EgEx7WlTsw72-6GNGP3j_iolMG_AmmFw6Yvuz2qgvlscjeTacEPqNj18QW-yJ4e5u1dlkgcJ0ebDopO12HLQSyE4a4jjl587Zo8RMj8-Vbx11E2ITDQKkN1HsIbAhrh_Qs3bw5irlgSU67QdESCiMMVlanBZcjQM-WTBYlQQF006Ll1THzZYWPrWw2NbP3aUKvi2V_IeL-t47Vm2iUGS8L_e6GplVbWeQtvgwY8BD0cuOeOqPpIpKF5uOgu4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🔥
🔥
نجات دروازه فوق‌العاده اوپامکانو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/100122" target="_blank">📅 23:10 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100121">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">فرانسه پر اشتباهه</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/100121" target="_blank">📅 23:07 · 23 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
