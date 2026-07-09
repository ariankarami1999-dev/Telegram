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
<img src="https://cdn5.telesco.pe/file/KX6WaudVpnhPjmhPkiCidedTWThIbMksinPEOu-qhPEugewpb1EwhLwr1sQbob9rBUbqUBzVnCfbwwGseXgIp6JmvBAn4ZFxKLiy_R8JQ9Aw_AW77ZNXA0vwq8F-RCL5pqa5qDKQw4LBgN-0lBWoFoHy-UbUJElEd_hAbOhp5nKt8eKpdS4LfdnS9gZbIAWx5GQUvC7aRYZLRxd1A5L4nOm_C0E9J1POBKKKi_7k-Bktv6YxkeLfbWv-_5FdJK-pVNB3eMfW4akYsCbYofXxkrF1QJBJUM58EObip5i9W6wVD5jp9feq7d0z25VLb1gEpvArO2UthRXk6JWylS4U6w.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 جام جهانی 2026 | فوتبال 180</h1>
<p>@Futball180TV • 👥 607K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-18 15:21:46</div>
<hr>

<div class="tg-post" id="msg-99189">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e54edf8ef7.mp4?token=LPV8UvtwlR7F9ESpMHSJwoRdp71db12lGd7NJ9pmY8axxE-jik0Qr8JEAusHMP-8Mn9PlwhO29vxPi_or9ALJgkKANCFhetYU9XuRVp-KWDvev1a0Z-oEpT1fykB9sdtMzywbCAcWSfJbTSyAcrl8BXNXUIYaLye293r-74cAwodY8cnjzrh_86-3DwuE39TxoAjU5gRXqrsCJ0NA0zgcnOLtCLEMD977HV0bj2wfYk3kh0Q_0B_E95ydECB-pPleMtarRQuACw0k-Qs3pRq1gCxfDEQzi21nB85mBSk2_7uPQLIXJmqZDQEvtMAJB7l4sb7Hf5MhW7soeA80erw-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e54edf8ef7.mp4?token=LPV8UvtwlR7F9ESpMHSJwoRdp71db12lGd7NJ9pmY8axxE-jik0Qr8JEAusHMP-8Mn9PlwhO29vxPi_or9ALJgkKANCFhetYU9XuRVp-KWDvev1a0Z-oEpT1fykB9sdtMzywbCAcWSfJbTSyAcrl8BXNXUIYaLye293r-74cAwodY8cnjzrh_86-3DwuE39TxoAjU5gRXqrsCJ0NA0zgcnOLtCLEMD977HV0bj2wfYk3kh0Q_0B_E95ydECB-pPleMtarRQuACw0k-Qs3pRq1gCxfDEQzi21nB85mBSk2_7uPQLIXJmqZDQEvtMAJB7l4sb7Hf5MhW7soeA80erw-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🏆
🇦🇷
از کودکی تا تاریخ‌سازی با لیونل‌مسی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1.22K · <a href="https://t.me/Futball180TV/99189" target="_blank">📅 15:20 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99188">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4241c19a19.mp4?token=nwSAWC3AFhNlpoVYiBz79L46Py6hea1TCmcVwl_DvLfHSFUTjAmrPrngll8cMpX9mcbplkvNyiBYu35w3WcqFcoloao7WmwzfzgF_WYuMZk_xVoeWoPgFYlBDGmSMK6Mtulkg36eemDtizhwQ-zrcSNfnEXIKHFYOOt3H217wUEprnkX-CExwuxq2eIKSkr1P4Hnd2PPjnuzXmSSrD6Bz0jrLy34MN5nzCOXd1ZnIcpH7skPcm2O0XH2Lm6zbhfgh9nOg8jdhh3u_DxtsJ8DYhYgfhRldZJh8GZ7q2KAOgbguY1CEKo84sGxHt-YD-wLvZkxo7xJlZ3uBacpqDQr9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4241c19a19.mp4?token=nwSAWC3AFhNlpoVYiBz79L46Py6hea1TCmcVwl_DvLfHSFUTjAmrPrngll8cMpX9mcbplkvNyiBYu35w3WcqFcoloao7WmwzfzgF_WYuMZk_xVoeWoPgFYlBDGmSMK6Mtulkg36eemDtizhwQ-zrcSNfnEXIKHFYOOt3H217wUEprnkX-CExwuxq2eIKSkr1P4Hnd2PPjnuzXmSSrD6Bz0jrLy34MN5nzCOXd1ZnIcpH7skPcm2O0XH2Lm6zbhfgh9nOg8jdhh3u_DxtsJ8DYhYgfhRldZJh8GZ7q2KAOgbguY1CEKo84sGxHt-YD-wLvZkxo7xJlZ3uBacpqDQr9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
▶️
حرف‌های ژوله راجب فوتبال که محمدبحرانی از یه زاویه دیگه برامون تعریف میکنه. جالبه ببینین حتما
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.95K · <a href="https://t.me/Futball180TV/99188" target="_blank">📅 15:03 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99186">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TkChTrs5DheEOn_KcE-7YPTW3o50Fwe8tfnlQwT1FedtzA6GwFoTPxtFtrprtFXi_ckqz_b8vEspPN_wO_6SgVa3M8hKxmazalfCFaBhf0335Ei2xzpJ48MecNv18JphKWgJ1TFKcqx6D9LI9E9FDrnJb6TndM0Ys7L-gAJA8lsnB53CKwOpsZp9ScASohB4iyqdLqoAw2k4UoR4y-8wsfqt5cR2k2aTvyHRKKanskh6L94uRqxh6MseVLDLZ8Se3yU8T1ivHw0MhQTVGIRoZlevn4VgDKA_fonyWczitNCmDKnM5GoMCCqncZgkmDN4qDxAlRtA0jEMaXBAJzemkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QkBtFk_ceNmQcN-Gr8vRLpWleEpsg7yRb7SDHD1R5mmTOatXBOyeMuC3nQUGDZRmELg1AQL71d1vJGI4TYCt4Cuw_fM05svvvsp9ALDsUtuwgqYZrcWooCTerjbLcNlhFv_D6WEq5EdlHkOGVqR7ttEsfRsI3uJAFDL-dy9LnIpYB82-ekKPPGVtCPJ-veKYU0aV7Ogo4LJ7mb5XatM5LTryapGRzL_KC-m9vMkV5DGVdPjn4wmgMUcBAjw5lpWCEtMk6_wumvNusmq7RAZhZNuDGYU5F-upFYhf5qek3ATf6QuuxsQSFVZJJ5THwzE8dZgDkadAMT9dqGnA33I11w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
وضعیت اسکله بنود شهرستان عسلویه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.39K · <a href="https://t.me/Futball180TV/99186" target="_blank">📅 14:52 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99185">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🚨
گزارش ها مبنی بر برخورد موشک و پهباد به سپاه ثارالله کرمان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/Futball180TV/99185" target="_blank">📅 14:45 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99184">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🚨
فوری؛ از اکثر شهرهای ایران به سمت پایگاه های آمریکایی موشک شلیک شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/Futball180TV/99184" target="_blank">📅 14:44 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99183">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4beeec2583.mp4?token=lSzTT1JN6iJe6Z1MdgSSZCT_5v9E5-liASHJBqz3-OissLeNNxtS2MMPpUcxowRnyNg9V6yoSp4pJpyiiN1uM1C5EYeWJhcoOQmQR4nYmDuH_udm_7ju2kUu9AXGXL9Cq5Guuhhxtjwg3Pyc51ae43Vx_XFjTLeMjQV8usqhume6MrojjEgs8-xXK74aWIKr7Q58vdDqn-l0uRe5EpyGuH0bATMCY2f-xu4OnheIRYP70_T2UsCogG7dnmF37l9XcYXF_HWO5L6keDFtaLtYSwTRETewSO0qX-VqN_S2Y_I2nLe-qht9Xwe3gO44bXn1GtKD9fa1-Ntd8x2d3j_-cQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4beeec2583.mp4?token=lSzTT1JN6iJe6Z1MdgSSZCT_5v9E5-liASHJBqz3-OissLeNNxtS2MMPpUcxowRnyNg9V6yoSp4pJpyiiN1uM1C5EYeWJhcoOQmQR4nYmDuH_udm_7ju2kUu9AXGXL9Cq5Guuhhxtjwg3Pyc51ae43Vx_XFjTLeMjQV8usqhume6MrojjEgs8-xXK74aWIKr7Q58vdDqn-l0uRe5EpyGuH0bATMCY2f-xu4OnheIRYP70_T2UsCogG7dnmF37l9XcYXF_HWO5L6keDFtaLtYSwTRETewSO0qX-VqN_S2Y_I2nLe-qht9Xwe3gO44bXn1GtKD9fa1-Ntd8x2d3j_-cQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇬
‼️
نمایی از سرمربی پرحاشیه مصری در هنگام اعلام مردود شدن گل تیمش مقابل آرژانتین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/Futball180TV/99183" target="_blank">📅 14:40 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99182">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CeXEPGuSWm1htsKRnV0d4txYhJAMavF_YkLYz8eY4W4CQZ7vHYAv_LZV9BRfJwfCqaRS-FPjwfFr7sxZfdSzg6OiSm2X9yUTDPK4ERRf8ZTSYocBYC8048xi5zjjPhVtHo6D3bLxJa753j7XCC7VAteGa_UVEBWVHgkIFaqncKX7h6J89T19_UXsXKMQQyDY0zyCtRsNgRJVddWXyQMj3zt0RrQnVPVMhs46p1eXVaR7I8RATXR9J2aIwN2xpBtmC1x_qkTDoE1p_tlGCg7RT-GKjDShTY1lE57eU4JUQrK0M45gWLXdmz8L8amC4xo69dzef5z3XTOmLk2WoQpfLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
لحظه امضای قرارداد ژابی‌آلونسو با چلسی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/Futball180TV/99182" target="_blank">📅 14:22 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99181">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🚨
🚨
🚨
⭕️
#فوووووری
؛ یک مجموعه صنعتی در کشور اردن مورد اصابت قرار گرفت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/99181" target="_blank">📅 14:17 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99180">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🚨
🚨
🚨
⭕️
#فوووووری
از منابع خبری عراق: چند قایق و ناو جنگی آمریکا مورد اصابت قرار گرفت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/99180" target="_blank">📅 14:16 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99179">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🚨
🚨
🚨
⭕️
#فوووووری
؛ گزارشات از شلیک موشک‌های کروز به سمت بحرین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/99179" target="_blank">📅 14:15 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99178">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇮🇷
🚀
#فوووووری؛ رویت موشک‌های سپاه در آسمان اردن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/99178" target="_blank">📅 14:14 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99177">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f3cb5d140b.mp4?token=ayVu0wYhrWTrnZLESAsriBbG5YkuJ1vQAiIbZ-ZmdjMWc_zcFBipq5RbQ_SGzFjsnMYablAU3fmodN0b_jq__Vr9WNZXcExCnB7k_ZMVC645HyLGC9-f-0Y6hhTGPXe23LlvzhEqkt9e8XpsEBU2uXUdoIH5V1vmM-8CoF8EGY3KuVOOhTOM9bN-OR7GacQpxzM8DcO8lFeo-4FbfAMqi6zR15rvbMR2jhZT9Tmo324gxD3pHbmIqlG2pX_qAETP2IpOz3rn14QbVAbyMZYLnBI5mW5nnHr1nrCoqbXkyqx4xhwcb0A_vAPV9FOX1ECEcxBchfAYSYwgyljuPvO17w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f3cb5d140b.mp4?token=ayVu0wYhrWTrnZLESAsriBbG5YkuJ1vQAiIbZ-ZmdjMWc_zcFBipq5RbQ_SGzFjsnMYablAU3fmodN0b_jq__Vr9WNZXcExCnB7k_ZMVC645HyLGC9-f-0Y6hhTGPXe23LlvzhEqkt9e8XpsEBU2uXUdoIH5V1vmM-8CoF8EGY3KuVOOhTOM9bN-OR7GacQpxzM8DcO8lFeo-4FbfAMqi6zR15rvbMR2jhZT9Tmo324gxD3pHbmIqlG2pX_qAETP2IpOz3rn14QbVAbyMZYLnBI5mW5nnHr1nrCoqbXkyqx4xhwcb0A_vAPV9FOX1ECEcxBchfAYSYwgyljuPvO17w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇮🇷
🚀
#فوووووری
؛ رویت موشک‌های سپاه در آسمان اردن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/99177" target="_blank">📅 14:13 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99176">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🚨
⭕️
❌
🇮🇷
گزارش‌هایی از شلیک موشک سپاه از نواحی مرکزی ایران به سمت کشورهای عربی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/99176" target="_blank">📅 14:11 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99175">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🚨
🚨
🚨
🚨
⭕️
اخبار غیررسمی از شنیده شدن صدای انفجار در بندرعباس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/99175" target="_blank">📅 14:08 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99174">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TPcXjhE1jt5khrEyKEflcobSBKcBFTk6KuTrxHCFKDkNxgZPG6n2-JPKQsc51TIHK-7leeTWKVm5Xjl6luMTD1R93lbdAOAS19yMNp0AwRyntNKlkmrB0OHYwUnEyhSw68abVqk_e0zhELbpd6aT7OzY0-fnN6MwY2KszHFmANvS5OK_DyJYUfa5capHpibha-a4wC3zTkQfWqv4La7FKrS6sKLZNcVNIs_2p-Ut-7iKBDMoA12h72s7PDJuc_-WbyYz9L8fqgrHTAV4a3XQNhZLID1MuuZc25Bv3lKBExLupuNjLs3-uT4f3oFWXZFykcY6Smhk8Tbua5XKIe5aMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فلوریان پلتنبرگ:
نیوکاسل با فرایبورگ به توافق کامل رسید تا یوهان مانزامبی را با 60 میلیون یورو جذب کند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/99174" target="_blank">📅 13:59 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99173">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🚨
🚨
شنیده شدن صدای چند انفجار در چغادک بوشهر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/99173" target="_blank">📅 13:53 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99172">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U9LQxt8phLwA-U64p0ZB7BYMO94osCaSY-6SeGqnnMOozTiCCuSRiYscLUn-Kv1nZIh95EIH83G5U4R23gxWz7FFBO9HTuuFaQc2LWwNM8W2CmDH3p7edl7fgrQ_MPJ8THgDzPe3ZT1erRRb2yEIr9bFP_SzKjE8517kuI9NROpJH3fo8oAe0mE36MW5V7Jn3MtTgwJNC5RcJzno3TJK9480GnNh6RMNVcZQtU6xER8PrqupS13p_WY37Rj2omVyaCjJ86UgqrdoOy-si0ecX58SWtj3OTdwxka9OuObAhulJ_JSXjlpTVQzfIPFgvyxtuK-ecpFdC8UPRi0_JE1xA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🏆
بهترین ترکیب فعلی جام‌جهانی فوتبال تا پایان مرحله ⅛نهایی با حضور علیرضا بیرانوند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/99172" target="_blank">📅 13:48 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99171">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🚨
🚨
شنیده شدن صدای چند انفجار در چغادک بوشهر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/99171" target="_blank">📅 13:47 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99170">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7337d363d9.mp4?token=f0kT0SZpfcu7LHN1afpiGUNYQmiSv_IzDcKV7fGDsKLmRIa7TxmNyF-F34vs8G21AyZMBc1zysFTjmfHkAIn9h7mfBPTzubphiurg3DRqI_20Snyzu9aavwXi7fgt8ZrJaQAP_Mi7AtzArNMNunuAuNRXhG0dXDq-6AW3lGJEh3ILuw_sQdmCCN-ObSZL8oaozVIBojMQBm5GaRONvInhFz5hiLmwAG_JbF2GkkOA7SO80Bvjzj0wZh26xzu-p_kh2TqSSWdstYruQmRK1kRrMvvHYKuIgsJhxY7ZmHRKuoeRzPUq69n3JOC8-SV9ba00IxmY9xSP7D7YhW-wjL4BA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7337d363d9.mp4?token=f0kT0SZpfcu7LHN1afpiGUNYQmiSv_IzDcKV7fGDsKLmRIa7TxmNyF-F34vs8G21AyZMBc1zysFTjmfHkAIn9h7mfBPTzubphiurg3DRqI_20Snyzu9aavwXi7fgt8ZrJaQAP_Mi7AtzArNMNunuAuNRXhG0dXDq-6AW3lGJEh3ILuw_sQdmCCN-ObSZL8oaozVIBojMQBm5GaRONvInhFz5hiLmwAG_JbF2GkkOA7SO80Bvjzj0wZh26xzu-p_kh2TqSSWdstYruQmRK1kRrMvvHYKuIgsJhxY7ZmHRKuoeRzPUq69n3JOC8-SV9ba00IxmY9xSP7D7YhW-wjL4BA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
👀
هواداران اسپانیا در آستانه بازی فرداشب
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/99170" target="_blank">📅 13:40 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99169">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64d3a36342.mp4?token=ZZtBcCbIEcigoF3nnmuU2Si4k0b0VdO0_4N9B_Yzhp_4Sbl8VYxlMYUJ5W3XyT6NWTmt5-SJnYyD7a0qo91_xgW9xq5piVl1NYYMCwua6gIlqxBY2IuksXfvMb5XvRVjdoX8-MTlI8gRIgC24W8Mbbgnvk9WiMnrdylkREqJVn1FUjCSYL_bNxqoBlGH-1nrDTnQiMll5fVCHdb_-EYy_yRc2A155O1E7GmpCmS5DCgoLOvS-TtIJBhjP_ppK8hfU2dizeTPjWdkpH-aXA119P0bTlZv46cH58Ezo9XjnQ2z_Eowu2Zt3ELQ1q0Eg7B2sKUD_owPFRie-XcrTr2Ziw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64d3a36342.mp4?token=ZZtBcCbIEcigoF3nnmuU2Si4k0b0VdO0_4N9B_Yzhp_4Sbl8VYxlMYUJ5W3XyT6NWTmt5-SJnYyD7a0qo91_xgW9xq5piVl1NYYMCwua6gIlqxBY2IuksXfvMb5XvRVjdoX8-MTlI8gRIgC24W8Mbbgnvk9WiMnrdylkREqJVn1FUjCSYL_bNxqoBlGH-1nrDTnQiMll5fVCHdb_-EYy_yRc2A155O1E7GmpCmS5DCgoLOvS-TtIJBhjP_ppK8hfU2dizeTPjWdkpH-aXA119P0bTlZv46cH58Ezo9XjnQ2z_Eowu2Zt3ELQ1q0Eg7B2sKUD_owPFRie-XcrTr2Ziw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🔥
🏴󠁧󠁢󠁥󠁮󠁧󠁿
لحظه‌ورود ژابی‌آلونسو به لندن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/99169" target="_blank">📅 13:27 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99168">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A1WVQk8q36jYhvoG_wLKtGzsPhDF63zL6cJKptEKNAwn2Wzrxv8SzSGXWpnDsMHUoz8J4vvu02hEE6GRBbs6bK51LJmMHhWxbY30zLkICfbOGcELJwF9mGfiozBfi1XiqBrhaonK5feSN4JZoxd7Z0QsbNEPSb98MWGWASmAbztUDq-RibltE5s_RAgEGJmiA7gkbavOu3FmJY0zmEkysp0PuGn79OJnx1jLjH1CljR-Y1L7ULp0QZn5eZ5xM_5sVhZVVOUXOC-4T4cqcVzYX-21zqlIwDFdjgb7n0iOeXNy8_Mbd2sGIk-EqOBEqY8CGn8uHMroAlIWFZ8Wt7zTow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🎙
🏆
کولینا رئیس کمیته داوران فیفا خطاب به اعضای تیم‌ملی مصر: پذیرش شکست از اصول اخلاق در ورزش است و هیچکس نباید داوران را مقصر باخت خود نشان دهد.‌ تیم داوری بازی آرژانتین و مصر کاملا عالی قضاوت کردند و از آنها سپاسگزاریم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/99168" target="_blank">📅 13:18 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99167">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🚨
🇩🇪
🇪🇸
آدیمی‌با بارسلونا برای یک قرارداد پنج‌ساله به توافق رسید. مذاکرات میان دو باشگاه درحال انجام است و بزودی اعلامیه رسمی صادر خواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/99167" target="_blank">📅 13:09 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99166">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DAxzkP2MbsXUM7neMDZH0kpG3E87TdDmdBaixAzVTiQ8bE19TVz8dUqKy7wt-Mz0NDei0c9Ab_ALqOmX1JSrOaHLIng03OYt1RxkXFaykGH0aNfcOUJeDvazQuw_ECq0-ZU5mYWQApDiuyC_k9bR_N9gs16baGryf_VIl_n98KpNuwtlf7MXTaltvqbp95eC7HRVl_4UKFwqKCdgndznL2GXOVe8UQ5iQYoKW4C-8H4QJS8VvQAD1EKNrBJAGq-ldDywNYgaP48AN9dc0u4xgUcVAFxk6RjyoYcmi64Hjyj0L5Ddsz4oOkZXD9GhevaXxlgoE01IYdojcfYzAeAzrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇩🇪
🇪🇸
آدیمی‌با بارسلونا برای یک قرارداد پنج‌ساله به توافق رسید. مذاکرات میان دو باشگاه درحال انجام است و بزودی اعلامیه رسمی صادر خواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/99166" target="_blank">📅 13:08 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99165">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ekj_SaE6MiaTVlgA5hAUjfemwhHQit35t1HoevzSQYUFmDO38TnYQdIvebyfBcUyRX643HgWV49ja7PAhooK2RtCoFsL_anfmANDsLWy6sCkZ7lrKs8qe2Hqnh-Zc1cLLfX-HfRjtFLbcsjbaumhVpMS4AXtLvSkCa3ZG64wnr264bHXuQ5E74V8UfHg1Ih64MVL0o9MnUE7ZkPcro5KYkLCHdzmnGnfYOPe2oQlvYGDFl7VfZ7vfXqz97gT2mdmK1jq-pkBcbFTEEdHth0CTl9knBfENGO1v6bxVc0Krh05f6yXbmZzNI07TsbOXv5qPkUdvhrCM3zQw8ySuJx0lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
🏆
هشت‌تیم برتر جام‌جهانی از دوره 1986
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/99165" target="_blank">📅 13:03 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99164">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🚨
🚨
🚨
🚨
#فووووری
؛ اخبار غیررسمی از شنیده شدن صدای انفجار در بوشهر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/99164" target="_blank">📅 12:58 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99163">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🇵🇹
این ویدیو یه کم حجمش زیاده ولی ارزش دیدن داره؛ تو این ویدیو به وضوح یه تفاوت جالبی رو ما میبینیم؛ کنار مسی، هم‌تیمی‌هایی که همیشه پشت کاپیتانشون هستن و تحت هر شرایطی واسش سنگ تموم میذارن در سمت دیگه، رونالدو که حداقل در این تصاویر، تنهاتر به نظر میرسه و آدم احساس میکنه فاصله زیادی بین او و هم‌تیمی‌هاش وجود داره. دلیلش رو نمیدونم چیه از شرایط تیم گرفته تا تفاوت شخصیت‌ دو بازیکن، اما یه چیز قابل انکار نیست: کریس در پرتغال اغلب تنها دیده میشد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/99163" target="_blank">📅 12:51 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99162">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a6b5ea886a.mp4?token=TSRiARXSqTxTbUq3_AwFNEimfUgyS6uXPqRvGJhzdphhcqNYc1d4A2FthY5S1HB3UGDqcOR_5lFAC3Spn2JM19LrcRzh67x_s_Hf-N3oI64CkTVqQxzS3x32ENKIRQPLkPiBzANuDSoRcdVhuC0WFZsYOBd08BhQjbNVOcvK1uDHa45v1CeW7-VvVZpGbwNmXWKnPdUyuTpsXZTSX487o7QRZnnCbJi6Ms9E7nPFrvur3V43nZMN6k2v1L9itCHJzwiK_vrB4cMfExeMAdfIbkphpkz-T3Qf8k2cjLwkvGypjpahvkSpHw_ErSd2nEAF4aOA0iE1LDfIaw-YXb5MyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a6b5ea886a.mp4?token=TSRiARXSqTxTbUq3_AwFNEimfUgyS6uXPqRvGJhzdphhcqNYc1d4A2FthY5S1HB3UGDqcOR_5lFAC3Spn2JM19LrcRzh67x_s_Hf-N3oI64CkTVqQxzS3x32ENKIRQPLkPiBzANuDSoRcdVhuC0WFZsYOBd08BhQjbNVOcvK1uDHa45v1CeW7-VvVZpGbwNmXWKnPdUyuTpsXZTSX487o7QRZnnCbJi6Ms9E7nPFrvur3V43nZMN6k2v1L9itCHJzwiK_vrB4cMfExeMAdfIbkphpkz-T3Qf8k2cjLwkvGypjpahvkSpHw_ErSd2nEAF4aOA0iE1LDfIaw-YXb5MyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وسط کنفرانس مطبوعاتی براهیم دیاز دو تا از خبرنگارا دعوا کردن و کنفرانس متوقف شد
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/99162" target="_blank">📅 12:44 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99161">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a986561ad0.mp4?token=gwo8k4kNKYbinU6-wAzfIDVojmpiBIkTqxHf_EU7n2eAdlHwWazuPEXJpUQdiDeWoHjhX5ZR4TaOeyX5Puh8xaJqFYLYxAcEkkHYXewEN9TnaASAFi4ZWdmBJRoj37eCM8b9P9wl1U6STfy70elNty9sM-1vV0xkXOhgPcg_W_6K7jBcyyfInJDTNXkbLL8Tnv7xnCpr95FoQB4THZlJH6y2TCPD1Dy96FfCChJUbVmzAd_Tnb6dG-WTfE6HVtBqQRHDanWWlW90vqU8LwqJrGTsZ_zYEtOG1ckE694jdEEdxpQi_l69A9Dp0pK7ePaiwMyqOgMsDjku3ZiIfSIg3L8BKgoyF33isWiIAP3m5RcxeC_JnzcA55h0ibBmgC3sbZWnugcCYNqHntVNDSjTzzXHNiFUirP7HsQr2M9ZUxjXztkXFjd-M4K-kBv5RC5E4o4iQiRriL8HWhC11p8n18lO51onWswxu8Wu242oA1BpFWE3W1Vh-sIXIIwviresDDhfrweIQhy7fOO_y7z8DESxUDOHUdDGMGr1UMpLMr_JGkd-U5vzn30xiSACXFsetdzBYx2GdzLggS4p6qVjyaYw4Sa8TJYh02skWdYQ_pV7jt3aDVAd5ILFiese8lhV0HYE0HHxHa72UODmq7lTkDrWHLsvoQBQ1lYQSdy5AZk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a986561ad0.mp4?token=gwo8k4kNKYbinU6-wAzfIDVojmpiBIkTqxHf_EU7n2eAdlHwWazuPEXJpUQdiDeWoHjhX5ZR4TaOeyX5Puh8xaJqFYLYxAcEkkHYXewEN9TnaASAFi4ZWdmBJRoj37eCM8b9P9wl1U6STfy70elNty9sM-1vV0xkXOhgPcg_W_6K7jBcyyfInJDTNXkbLL8Tnv7xnCpr95FoQB4THZlJH6y2TCPD1Dy96FfCChJUbVmzAd_Tnb6dG-WTfE6HVtBqQRHDanWWlW90vqU8LwqJrGTsZ_zYEtOG1ckE694jdEEdxpQi_l69A9Dp0pK7ePaiwMyqOgMsDjku3ZiIfSIg3L8BKgoyF33isWiIAP3m5RcxeC_JnzcA55h0ibBmgC3sbZWnugcCYNqHntVNDSjTzzXHNiFUirP7HsQr2M9ZUxjXztkXFjd-M4K-kBv5RC5E4o4iQiRriL8HWhC11p8n18lO51onWswxu8Wu242oA1BpFWE3W1Vh-sIXIIwviresDDhfrweIQhy7fOO_y7z8DESxUDOHUdDGMGr1UMpLMr_JGkd-U5vzn30xiSACXFsetdzBYx2GdzLggS4p6qVjyaYw4Sa8TJYh02skWdYQ_pV7jt3aDVAd5ILFiese8lhV0HYE0HHxHa72UODmq7lTkDrWHLsvoQBQ1lYQSdy5AZk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🔥
🔥
Maradona.
🇦🇷
🇦🇷
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/99161" target="_blank">📅 12:40 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99160">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/80d77513fa.mp4?token=snsRb-C02aZJAq85aRBTzcstNFYlWHrPJYBCE9OJUvzrmz34m5X0wAQ-Jt4MUGin-ja1CeaN5ZYfE1KMZ4C48V13gWKLLsMajHEJHCXVDNwHtWjq0gDXgZr5uWsJf2D4cCMnSJUa5mTL78AnzWpr-f9syQGG-bjs3KdRUbYw52ZfeKJQWLAD3ne3FxZU_czue8yeI35PQj8mXuaDFLhPCO57lcoKBcvNoGSUouC2hm2vWk_7uchXfBjL9TkTPVJCLl5qmcIWKWrNaG9cfVar97-FiGuCS3279h5q1V4QRgMM6Y73Ln_jszKdqW4IfqQPjaK1J0JbK06GcHnL-eXUwWslRIn3EVZmKugNv_HGH8SPrZBV5pZ-sDXNd36rjpELAG4MDQYJwvsubUr-h40k4WsjaHYZXMXkk9Y1nIg1SbsioHus97UksDaAHFKfuFazIBS9BD3q1vXgNagPyR2k6CW0FGcNe_zt_tPX5SwcR9AAv0--rmP27EvuJiNK-WY9bmbLqubhYoLxzerBnVP_XiwY9aQzYEtEPlU2PFUVySk9SYQF9aAWR3_QNd-GpJ5CPwCN6e3POll578vpaKJwu910Z9k0vT7xvoN3FiaOfxPDNqefeliaXLNbAGgyTA1op26nyjXcwcJUmSugV4j6QyTltGNpDnhwZGKxdJb6-Mk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/80d77513fa.mp4?token=snsRb-C02aZJAq85aRBTzcstNFYlWHrPJYBCE9OJUvzrmz34m5X0wAQ-Jt4MUGin-ja1CeaN5ZYfE1KMZ4C48V13gWKLLsMajHEJHCXVDNwHtWjq0gDXgZr5uWsJf2D4cCMnSJUa5mTL78AnzWpr-f9syQGG-bjs3KdRUbYw52ZfeKJQWLAD3ne3FxZU_czue8yeI35PQj8mXuaDFLhPCO57lcoKBcvNoGSUouC2hm2vWk_7uchXfBjL9TkTPVJCLl5qmcIWKWrNaG9cfVar97-FiGuCS3279h5q1V4QRgMM6Y73Ln_jszKdqW4IfqQPjaK1J0JbK06GcHnL-eXUwWslRIn3EVZmKugNv_HGH8SPrZBV5pZ-sDXNd36rjpELAG4MDQYJwvsubUr-h40k4WsjaHYZXMXkk9Y1nIg1SbsioHus97UksDaAHFKfuFazIBS9BD3q1vXgNagPyR2k6CW0FGcNe_zt_tPX5SwcR9AAv0--rmP27EvuJiNK-WY9bmbLqubhYoLxzerBnVP_XiwY9aQzYEtEPlU2PFUVySk9SYQF9aAWR3_QNd-GpJ5CPwCN6e3POll578vpaKJwu910Z9k0vT7xvoN3FiaOfxPDNqefeliaXLNbAGgyTA1op26nyjXcwcJUmSugV4j6QyTltGNpDnhwZGKxdJb6-Mk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😆
😆
احتمالا بهترین تیم‌ملی تاریخ ایران :)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/99160" target="_blank">📅 12:20 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99159">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d456e6fe3e.mp4?token=vj_kKk183YMMe4j-GhPGc_a9tzYRiwoYzLXWbZW5tog_kVfy8cTqpNexkpCpcqSY8dpe7rUJ4hEB49RdvbAD6eOuUvuY18t_WZx6UEujEzGnOb5S3OOVkwvaOFJ_-qKeNzNR99W_fE9ZL3eNLu_JDgzocR3gC7tOS_GJVKpmUc1VUIYZEr8cf0sNVHa9ut9e7Q63ng0ZuqLCDae2UWeiAsvtNFO8V_A0UDc1nL8ZnmYWv8jj65IkiwmA0MPfr_AOmAcm5JhgQsWqkRbX1520j5TWLqOF_ARTwH8ywtseX8ccjLN9BWMELEOB9JCrmIs02PSi4y6kYvb6zs4dF0_UVYwz9mtpj4RI_JldJnSFFKjxoPWmXpXxABlltQbXl7mPqpsiA9hKYLyFLmjbsvgPzNTPLkP4pdDnT6MjrWsmE2XYQv-B90N7QwGOjepYOlT08xgS7XcrCcRe7q05T0X41fyz4OWC8bU1qxKrTBQQX8fqK4BSWNXm0WvIZ7f5Kg0JHlFhbq2BkMg8NcKF56Nv6jvoMKHbVVg68iw3j8lcKtLwMAKtRNFDsCaU965JH030CrPsf_hlNYTKW2cVz-P_SnATQxs7G0CyooJQuH0JD-csnX3z_8CTOhnv1lXwFHLHApXijAnEj9FELKh9QyKHtZwHfQh2HdNgWwNNTsQY_qs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d456e6fe3e.mp4?token=vj_kKk183YMMe4j-GhPGc_a9tzYRiwoYzLXWbZW5tog_kVfy8cTqpNexkpCpcqSY8dpe7rUJ4hEB49RdvbAD6eOuUvuY18t_WZx6UEujEzGnOb5S3OOVkwvaOFJ_-qKeNzNR99W_fE9ZL3eNLu_JDgzocR3gC7tOS_GJVKpmUc1VUIYZEr8cf0sNVHa9ut9e7Q63ng0ZuqLCDae2UWeiAsvtNFO8V_A0UDc1nL8ZnmYWv8jj65IkiwmA0MPfr_AOmAcm5JhgQsWqkRbX1520j5TWLqOF_ARTwH8ywtseX8ccjLN9BWMELEOB9JCrmIs02PSi4y6kYvb6zs4dF0_UVYwz9mtpj4RI_JldJnSFFKjxoPWmXpXxABlltQbXl7mPqpsiA9hKYLyFLmjbsvgPzNTPLkP4pdDnT6MjrWsmE2XYQv-B90N7QwGOjepYOlT08xgS7XcrCcRe7q05T0X41fyz4OWC8bU1qxKrTBQQX8fqK4BSWNXm0WvIZ7f5Kg0JHlFhbq2BkMg8NcKF56Nv6jvoMKHbVVg68iw3j8lcKtLwMAKtRNFDsCaU965JH030CrPsf_hlNYTKW2cVz-P_SnATQxs7G0CyooJQuH0JD-csnX3z_8CTOhnv1lXwFHLHApXijAnEj9FELKh9QyKHtZwHfQh2HdNgWwNNTsQY_qs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🏆
فینال جام‌جهانی ۱۹۹۴ میان برزیل و ایتالیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/99159" target="_blank">📅 12:03 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99158">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🚨
🚨
🚨
🚨
⭕️
شنیده شدن صدای انفجارهایی در بحرین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/Futball180TV/99158" target="_blank">📅 11:42 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99157">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sja9WFgEO3EEbs02qOW4m5wmR8RUsMkUIYBVsCjBEQ62P_7Re0MsjGWF3hMhYk2SF1cJxMjvAc4MbxqrqSV0L9nv6bX6PTsc9Qwe-zbfeFFoG-0anXvFmvhwrbrUqzLOg9Ii9A9jQAge5UmpvY_DB9Kc1WaNcBYFDygFPQEnSOQk9YzUbLLgsGs42ijFB_nca-vBVvKXXEHg5wSHo-vG177gJrmn00FxiQP_63ZQl4KoPqksw25lZQXsUEmIWV-T4xDapMdrP4Ymrpc8IVfmeOZCkYfWAsbUg9Lcmd1rvKqFEAEoIHJuSn8wb_l4y3zqCSDO0EoVBMtbNho0NAm0ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇲🇦
❌
#فوووووری
؛ اسماعیل سایباری ستاره مراکش بدلیل مصدومیت امشب جلو فرانسه غایبه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/Futball180TV/99157" target="_blank">📅 11:33 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99156">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🚨
🚨
🚨
🚨
⭕️
شنیده شدن صدای انفجارهایی در بحرین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/Futball180TV/99156" target="_blank">📅 11:32 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99154">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e5cb5d89e5.mp4?token=djQ5DeLIvwhmyh5au8nV8uHUkwY1e6NTEbr2cUCWibjqs08BIJccSLTU52AL7aTYtUzPt03VVc4PS4z_0GHRxgZxgIWE6zyln-PNWovCMudWcR_KV-QkzSboxV2UNJaIJcfKG4uBR2ph_IbQBjDdoF64YsfDtVvSZ9jA05cZNciGPmmX3GPyu8Hd72idOSPmCXR3obtyEo0T5pT3sCDvDLmPH6Zd6k1c78pW3k2UxYUEcTk6k2Z-af0mflvwvC1OSqScFPWa3bXH4EZLtY8xiraF-q22eze_D5xiJ09IWGCNV6EnGIlODVYAlGoFaxWeDJONST4UUahaPOy0A5oRVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e5cb5d89e5.mp4?token=djQ5DeLIvwhmyh5au8nV8uHUkwY1e6NTEbr2cUCWibjqs08BIJccSLTU52AL7aTYtUzPt03VVc4PS4z_0GHRxgZxgIWE6zyln-PNWovCMudWcR_KV-QkzSboxV2UNJaIJcfKG4uBR2ph_IbQBjDdoF64YsfDtVvSZ9jA05cZNciGPmmX3GPyu8Hd72idOSPmCXR3obtyEo0T5pT3sCDvDLmPH6Zd6k1c78pW3k2UxYUEcTk6k2Z-af0mflvwvC1OSqScFPWa3bXH4EZLtY8xiraF-q22eze_D5xiJ09IWGCNV6EnGIlODVYAlGoFaxWeDJONST4UUahaPOy0A5oRVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
🇦🇷
🇪🇬
حرکت زشت و تحریک‌آمیز بازیکن آرژانتین در مقابل چشمان محمد صلاح!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/Futball180TV/99154" target="_blank">📅 11:20 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99153">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6cfbfdf007.mp4?token=p-f2DCHU4oNp4mjdMAQJshOG1xiTsuvVqR1seoXSE3rotf7UmADETeizSkatNIlt4RzFEYMOXpLIyKjgf3bIrojnwEo73s_HfP2TtT-KHL6KW9qCa75kDwvi5qWJl7mWmoLpqOG7kcTemA6hVk5BCnUbvIyJb5oY176OutTiRCfLLYb56x4s7iNdh0lXbuDW9Qvauos4rd5_VsdAsoKQS8GNqHBcbbuy0zCqvLoHeNTEvsYHlG-vaBnEZ4OBJ9UfNZjOI5tP9bIGe1orTQEv2t-Ul2npJPW8p5BLOf7kRnC_wPgeWQWYqKJvJXuAPpGP66Kod_Xi0O0XHTNieV3X0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6cfbfdf007.mp4?token=p-f2DCHU4oNp4mjdMAQJshOG1xiTsuvVqR1seoXSE3rotf7UmADETeizSkatNIlt4RzFEYMOXpLIyKjgf3bIrojnwEo73s_HfP2TtT-KHL6KW9qCa75kDwvi5qWJl7mWmoLpqOG7kcTemA6hVk5BCnUbvIyJb5oY176OutTiRCfLLYb56x4s7iNdh0lXbuDW9Qvauos4rd5_VsdAsoKQS8GNqHBcbbuy0zCqvLoHeNTEvsYHlG-vaBnEZ4OBJ9UfNZjOI5tP9bIGe1orTQEv2t-Ul2npJPW8p5BLOf7kRnC_wPgeWQWYqKJvJXuAPpGP66Kod_Xi0O0XHTNieV3X0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رونالدو فنا در حال امضای قرارداد 10 ساله با تیم ملی فرانسه
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/Futball180TV/99153" target="_blank">📅 11:17 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99152">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QEMKX-Y54gMPQLSpGxlrpdgsGBCCEDCAkjjvJQksEYaPbERIPbB26_hceLKtRZCcKLhONlf0RcwtYVAC4_52ZIqV88HzL1Ud-xvp444nuRXWMOzOHDqKBSbYVSJFgOyWQBjrdHIyKNAiUAWM89kpwpyxucuvBgwwvLOUEkc8NoMAn6zSUtVcpb74dUG4-hdQCmwzYhRP_m5czKSHtmrtD-3XnT36xXKyg437rGBTTZvpmrQ3P3_sxUkNZUuIW_kEhdwTzW852gAKzosOEFSku1YCW14klHvPTPkSqmJDXDE3TBEtEABOd9NSFhykqUDq2z6U8qSs2CxdBhkvvpVSIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇩🇪
🇪🇸
#فووووری
؛ هانس یواکیم واتسکه، رئیس باشگاه بوروسیا دورتموند:
"ارلینگ هالند علاقه زیادی به رئال مادرید دارد و این را پنهان نمی‌کند. به نظر من، او ظرف دو یا سه سال آینده در آنجا بازی خواهد کرد، نه الان، اما به زودی."
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/Futball180TV/99152" target="_blank">📅 10:49 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99151">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WznEtGxYDWmG8ZJzzXe0mAOKebp54na5OriVxcQbFHW1qmQU3_hidomJKucJs0PvT0-BA3UPdN0J673YfAH8img7NCtI6Js2cKlLv6b4Q3QguxLIcSYOk9J9VIHLTfzBCNZO9AkvKvKer00OFDGmUoMxSVZY7zx6cmgSJa_dlyQf6RZ9hdUtWn27ri3ox4L0NKDN6o3Ie0udbqUfDlJ-43HX16Z2pnteAAg7jCP-LHCXyvRaYT8PJFLsia7b07j3ygUMvYzBx7hjHXRTfna_0dPi7BkeVsJzkm14Tt7iQhWB1eVmznZx2w0gygBqbM-t1DE6pseyvzWooKPLTLnDIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
#فوووری
— نیکولا شیرا:
- باشگاه آرسنال و برونو گیمارئش به توافق کامل در مورد شرایط شخصی رسیده‌اند. قرارداد پیشنهادی تا تابستان سال 2031 اعتبار خواهد داشت.
🔥
󐁧󐁢󐁥󐁮󐁧󐁿
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/Futball180TV/99151" target="_blank">📅 10:48 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99150">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🔥
🇫🇷
🇲🇦
تنها چند ساعت تا بازی مراکش - فرانسه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/Futball180TV/99150" target="_blank">📅 10:40 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99149">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🔥
مرور ده سوپرگل تاریخ مسابقات جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/Futball180TV/99149" target="_blank">📅 10:20 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99148">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a9ed1c618.mp4?token=Wvmu1QArre9ZARW7fX_SKPKpHwniZS1FTebgHtUBdKApfdcdLByeqFoI3NpD2eYkuB2QwZVuD-8ME32Maj4_2pnhVrynTuSSTwUyArHgo7pSbV4Z0RTbEUSrS21h8GUilKkTBJNaPZN0qRwtIAYDFiGen5-4Ehmj0U_ENchPxlCVsCuWUN_WdkLlt8uI-C2MfRzwowvmxg3ZKrLgeSz5ty6MV3h3jjLOQp44WNf6EVwAPUBI3TtdWnw1IByao1X4knPxp2So8k_Zfy_yfMHa0FZef2Vyl-TrGP6b9gyBOUXY0X41z2yeeSbVs_8UnWIjUot2gCimmv__33wafWda8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a9ed1c618.mp4?token=Wvmu1QArre9ZARW7fX_SKPKpHwniZS1FTebgHtUBdKApfdcdLByeqFoI3NpD2eYkuB2QwZVuD-8ME32Maj4_2pnhVrynTuSSTwUyArHgo7pSbV4Z0RTbEUSrS21h8GUilKkTBJNaPZN0qRwtIAYDFiGen5-4Ehmj0U_ENchPxlCVsCuWUN_WdkLlt8uI-C2MfRzwowvmxg3ZKrLgeSz5ty6MV3h3jjLOQp44WNf6EVwAPUBI3TtdWnw1IByao1X4knPxp2So8k_Zfy_yfMHa0FZef2Vyl-TrGP6b9gyBOUXY0X41z2yeeSbVs_8UnWIjUot2gCimmv__33wafWda8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
آنچه در بازی آرژانتین - مصر رخ داد:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/Futball180TV/99148" target="_blank">📅 10:03 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99147">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/frpyZswgjM8o4U2hbqnrW64NLij21bv-ew9FVm0bN_2n9g-pJrq9vkifJM6JdmKsAEcSeTBcEaRT-m36QxILU04ijOVTLcrG1rCiOQpaHwy170jfjDZmbMmwxCrNcxI4N-dTdJxdPHE3krlguSXK6N5qdRHTG2pMdQEMQoBbnmrBE7SxtTet29CtUyyGznxykVVgBqzFFMvQ2JXvamd_49tkZWQdNw4HTJbj713bElvzDdH_S7m2SNxvtR8R0Iub8fVdUATDQo7YMvm2W1MhKPqcxf4BCaLI7aQX7PSxmf7aNrjRgnaURi4lkXzz1QFGXOVTY4_jdUToI5p0kGct0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
جرارد رومرو: بارسلونا به جذب کریم آدیمی نزدیک شده است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/Futball180TV/99147" target="_blank">📅 09:55 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99146">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/37e88795bc.mp4?token=KU6LeBb9nQCFDyw2LEzZVI01EpupbsAvbIr-kl_ljl4pzqQTG3NJkAUDNxp-yeKkjCejdhk8qaGNr2woWagLrf6KK1vcpFyLgL4qccIFt4LvPAYYg2E9F2wKgQ-LAuagXouALHA9ZozRLayCvxXrDX-oWRV-xOpxSoadZibscJnI3GIYknzdytvfIyqjNbucIZQUT65k3lcfhjVH8mxiig_fDU6Z09c_q6DfUw6t4H7Y3lbtoMdJtgOTV0U0O60y0Pz6Gvoasv0p3Z-H5sSPTxwjKEpzRbAwKX2nj21GVB2ZVCffCvtbjlR02_4W3yLP6yg6qgp3SbIrGhCbHr22vw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/37e88795bc.mp4?token=KU6LeBb9nQCFDyw2LEzZVI01EpupbsAvbIr-kl_ljl4pzqQTG3NJkAUDNxp-yeKkjCejdhk8qaGNr2woWagLrf6KK1vcpFyLgL4qccIFt4LvPAYYg2E9F2wKgQ-LAuagXouALHA9ZozRLayCvxXrDX-oWRV-xOpxSoadZibscJnI3GIYknzdytvfIyqjNbucIZQUT65k3lcfhjVH8mxiig_fDU6Z09c_q6DfUw6t4H7Y3lbtoMdJtgOTV0U0O60y0Pz6Gvoasv0p3Z-H5sSPTxwjKEpzRbAwKX2nj21GVB2ZVCffCvtbjlR02_4W3yLP6yg6qgp3SbIrGhCbHr22vw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
👀
شادی عجیب و غریب خانواده آرژانتینی بعد گل‌ سوم و برتری مقابل مصر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/Futball180TV/99146" target="_blank">📅 09:40 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99145">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/395ec83e2c.mp4?token=EWWlVdcm4tNcopGGskNmBwN4h51VLqJxmNHtg3x_0Ub1Q3W3Pb-F52h-dQl7tvxQAVfOflCMIRUvX9D8nmO2Ajb6UPrcoxYhhD2BL10Qn6ZMBF8zF5EHhme2mXlEUhPpsd32CTETvdCnBpT_NZ_9wN9DHgvsjvWoZQN7wjC4Bjl2a0DyJirLb97GHQXwlAqwpLrd1sSSHJ9n5ujTxVa3O1qVHmJJAsJip0aKhwWTOjNMQMEq7ldX38aE6ccg6Wlv7kmxXIIBZbxQ7WKWd4C4rfdfHy9i_UW1K6EigQpKDWJEk1YY7wwTmXGpdLnEQknZg-rCdNIf0AFWK7cJbrBHtg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/395ec83e2c.mp4?token=EWWlVdcm4tNcopGGskNmBwN4h51VLqJxmNHtg3x_0Ub1Q3W3Pb-F52h-dQl7tvxQAVfOflCMIRUvX9D8nmO2Ajb6UPrcoxYhhD2BL10Qn6ZMBF8zF5EHhme2mXlEUhPpsd32CTETvdCnBpT_NZ_9wN9DHgvsjvWoZQN7wjC4Bjl2a0DyJirLb97GHQXwlAqwpLrd1sSSHJ9n5ujTxVa3O1qVHmJJAsJip0aKhwWTOjNMQMEq7ldX38aE6ccg6Wlv7kmxXIIBZbxQ7WKWd4C4rfdfHy9i_UW1K6EigQpKDWJEk1YY7wwTmXGpdLnEQknZg-rCdNIf0AFWK7cJbrBHtg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
اشتباهات مشکوک داور بازی کلمبیا و سوئیس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/Futball180TV/99145" target="_blank">📅 09:20 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99144">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🚨
به نقل از آکسیوس:
مقامات آمریکایی خود را برای یک جنگ چند روزه یا چند هفته‌ای با ایران در تنگه هرمز آماده می کنند که بزودی آغاز خواهد شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/Futball180TV/99144" target="_blank">📅 09:00 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99143">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ox08oR1_FcrKXDD-NP-PwE65dbQ2_uITGVj6y4M6WOkBEgKzudZQNjIS4Rkj-U2QZozZaIu-2eUDIOR_WwDotDruH923TZi6ayS7fQIWEew_VXo3P9v-8Q4UM69czouOPFQtL2K6x5JNhxmBwgzK_nrC8cG5GJz0kl0BfiN1RGhfXesDE3557NQxXQyb-AMdsoCSJdDDiwI2C1CCXrbTUdiOY6QTpRa5mS6-lZErGWw6OC6p1JtOMK_I-10ytRypCNj2CESAaNkyPmbSg-Jy0X1wmJQl6PvGI41_a0kMMGaQGl1-WEQecDxCq6LbgNlxhVhx3QJOHjcGEKhumL-BQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇬
در اقدامی عجیب و برگ‌ریزون؛ دولت مصر ورود لیونل مسی و خانواده‌اش رو به خاک این کشور ممنوع اعلام کرده.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/Futball180TV/99143" target="_blank">📅 08:56 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99142">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🚨
بیانیه سپاه:
زیرساخت‌ها و تأسیسات مهم پایگاه‌های عریفجان و علی‌السالم در کویت و پایگاه‌های الجفیر و شیخ عیسی در بحرین را هدف قرار دادیم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/Futball180TV/99142" target="_blank">📅 08:51 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99141">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eSIF0GBAJ8EDBNmVZjhkDlCFiusMpWUBk5WILJj8ipd303cmtUBtyzaqscKF3L-bP7F78KHi5_MDwrnVgrCxh9owObhsPvcZjkxkoDlzM4saji4P6G2R1GoBQ9ADf_0eoQY10kzPSAy2flEYTWy5X8ZLvwgeLTwU8CwskS748E3uwMETlzUXsu126XqJenm1EkPIvM4zfr0FYCuqSqaUIiucBtdjJcXEiW_a8Gtso7wvyFxDZFZhf9hURmQhUltAmnWJgEDeUtPoSmuDlVjaHtDdkUFULN3gaJoa8C4CZAfuzuKZAas8w0ABVDCMnVpoMKc_8jPyBMHwRTX2fOXxtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔺
🔻
دوست دختر جدید لاپورتا
: «من بخاطر لبخند لاپورتا عاشق او شدم و نمی‌دانستم که او رئیس باشگاه بارسلونا است.»
😆
😆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/Futball180TV/99141" target="_blank">📅 03:37 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99140">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/318d7f4ff5.mp4?token=eR0LMA5IwQ-VgELPkYZd8IwsdcKsN29uuD-0Pbxd6yCs667ATltIsfuE9IeiPAtlRZAn3o9-4MkffkuWgf9ZEMXERp0vshM3gRfdFXMXUiDggwEoIsGUuVWvmSdU73O949H7qYRayJFBMnYI0pSc6uao_-hT2BsnydVBoMmdnYEGFDH580t2aTCEZo3xurVVQ2fq_TAw4BNrB8wNsl-fhDXJpsfkNVwyZpkDtrw98DYht7mm2_Kf7teLaVihhaoa9_LPe_Ovgl6GzXzQ2q3lxxXgeO29myHLapzPuI6YUKLVE_E_hhnj6emGOr7ofwiLLPU6OuH8W6QjU2r8iWCjzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/318d7f4ff5.mp4?token=eR0LMA5IwQ-VgELPkYZd8IwsdcKsN29uuD-0Pbxd6yCs667ATltIsfuE9IeiPAtlRZAn3o9-4MkffkuWgf9ZEMXERp0vshM3gRfdFXMXUiDggwEoIsGUuVWvmSdU73O949H7qYRayJFBMnYI0pSc6uao_-hT2BsnydVBoMmdnYEGFDH580t2aTCEZo3xurVVQ2fq_TAw4BNrB8wNsl-fhDXJpsfkNVwyZpkDtrw98DYht7mm2_Kf7teLaVihhaoa9_LPe_Ovgl6GzXzQ2q3lxxXgeO29myHLapzPuI6YUKLVE_E_hhnj6emGOr7ofwiLLPU6OuH8W6QjU2r8iWCjzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
❌
تعجب مهران مدیری از درآمد علیرضا فغانی وقتی در ایران بود: به من برای قضاوت هر بازی ۶۵۰ هزار میدادن که ۵۰ تومن هم مالیات می‌گرفتن!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/Futball180TV/99140" target="_blank">📅 02:47 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99139">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aC-FfBGGuNwWHQ5Vplgb3vAzBrXGhGB3_4Wa559YiAXn08LxeAsDmdnyjRo5TKXa66Ino_ZXG4XTOh9uLv9jg105W-b3-sGFyOPzOhvzd4XixsnXVCMEWAEaCHQWA-jEUrVhTgYwy1776LAZ-CW3r8QybXqnXG6ydXv8WIfXZPLfyjrnq3rTGtxYE85LB8bbM04kTZ0Ik4DlqlMFWg23Sq7UOLFREkEjESGk3V_ZMleP0yWrpevY43FVefGaC55k3Orbs7Amj595MAPORqjHdcQ7S4wX1parW3RM2mwqmJoRPhe7_wyNU9kwDM-lmRLqJN79e5xaYhImkkbsmVoOsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
جرارد رومرو: بارسلونا به جذب کریم آدیمی نزدیک شده است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/Futball180TV/99139" target="_blank">📅 02:14 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99138">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bv0X3x9lqCuQYFPJe02fVxAjIA6xgkl5HLgmudPfVF5F0H2Zh9OBonlj8BKeMBBDMaImSu7zzKHLt8D8w1MPnTA1yNxBkYGuOdDDdz5sAX2J56ltzH-qgIQ6DGERRjvyHPpc5d7ykUayMZoU-HrmsO1xuUjujpzPCOw1eOVVUzorOpc7CVBUuQlP0tqIW7XJlpcPbne6VX0Iak-5hARPfYaMUoDxj1JxyE0ZZh14A52aC2nuwZEdf8imHb21vNq5ayJpXFKyWu5F5mzOhm5QJFXAzMwBUFcC5Tq13nrSXcfmC5YQPl6QnI4JmgTlgvQcX5H20YV-JWFwIQxmJ29B6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
تفکیک 3 هزار گل جام جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/Futball180TV/99138" target="_blank">📅 02:12 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99137">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FuckBet @FuckBet @FuckBet @FuckBet @FuckBet @FuckBet</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/Futball180TV/99137" target="_blank">📅 02:12 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99136">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LgRzkMunuWmUhth9s7DSa90NbKD7PdrJnyyspnYjhdb4xLNxFGS9e3GaGAk1eDtqORnvT7mfngVjAo4d6vbxqUQLUu5EleLV0Yk2e6ofIFavrt6D-onQyOmXt0pX0N7nAL-yveJftvzVaq2zAw1dGefG-4JS0n5R2wID3fKwdqxZj96h4Ei7lqT3MPfALW-xd7ynSM1P5VOfyELS_mdKJyHW_4iTpKrTrI5GSdIBLzo4NBKvk-fCKZAMCvTIFa7DZ_Yj7iUChl1m0-2UTj_mf7UHW5mN6rHSS-vYeBnV0xieh60OZSWq8FQiahMEu7F7CaFijT6FPNyNjtQRmiXSKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FuckBet
@FuckBet
@FuckBet
@FuckBet
@FuckBet
@FuckBet</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/Futball180TV/99136" target="_blank">📅 02:12 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99135">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🚨
🚨
رسانه های برزیلی:
ممکن است نیمار در روزهای آینده از فوتبال خداحافظی کند.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/Futball180TV/99135" target="_blank">📅 02:00 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99134">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fYeictgruHL5fOmHNhgEe7qXSmiN2J3_G7um6Z-ehw7KAG8IqGlHC1qdXKG3PgVxPyy0l0BJSbV14HUBjCFWf1QQ3ngkWoSZg05zn-715VRONNumD_7RYoFnrFhEcQMEUmbOWnwnGgaZeQACACaJM-TXWUbyeaa16srIad4mEs-paUGpTnHMFv_dCN_19mJclreBKNMIu-ox2rZQSCgOIppxCPuuU9FbHNoaBfgDRDXSJcLvHX4GBqZovnCm5G6tyCmHF77TKBkkZCDfiTOiS5wCpso1OEIe9lR2pLEk8cC_Fx0gD9oT0Xvzq2d_Le79c7iDTqHPlJw95qjGjVxxeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
جرارد رومرو:
بارسلونا به جذب کریم آدیمی نزدیک شده است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/Futball180TV/99134" target="_blank">📅 01:40 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99133">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c8ZNe7bL8bQ8IDiLUNSWpIZQLbhLNIgAwp0ikgCiecHBOeKy8AqN2_weviK8o2w9AmeyyIE0qY1zKxdzqSvbN9X2Ss601Jvfzx5wmYE-LApXV-Pega1MC9KoTPe03UHECn210GxCZAYqUlW6pYrwAjCmjmIorHWGmvPITXHXEOZWG1d5ec2UCWDFZDNDIP7LUGnYlZx3yJmx3ZXAqgg6a7hCguOV5ymtT9VX9fE8wPXqPVZDgF4IV23A6KQy6gHLN2lmGLfqnI41fbEkUnqQX9KX3SUfru-60yYth9H3EVonGcgM5jtDSSXSFNzcsJCKpBX5UJQbxuk4tDE1CIc2wQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
نقاطی که امشب مورد حملات آمریکا قرار گرفتن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/Futball180TV/99133" target="_blank">📅 01:31 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99132">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🚨
حملات امشب آمریکا رسما به پایان رسید و تا ساعاتی دیگر حملات سپاه به مواضع آمریکا آغاز خواهد شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/Futball180TV/99132" target="_blank">📅 01:24 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99131">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jpuWvVLTgQvr-tiZqqWexIUdXfJc6b6JSn0XTTGp9ATm4MkHEEOsMhhfoSqsOrgI877M5oI2Ykxi4S2GTuRPKBijU7Q7QVWcyR3l3GO9PYrf80MRSz0YtImb5SN0-CDxzDNZRwdmio3d7bThQGx8c7BRrVOLTU-47S0ckoUsYYREvcZNBaUpUVVnWB0QpHV0YE7iFrPHXMZ5NzhV35rLRVQyqBrs6joJx1R0qvvCngtLO5DVknuQmXZ8elzhDiG4dbDcRDKbN1aPRiDLYdLGNzBQcJDBDtR-IGlSnBoX_cadHoH0xhL0X3WFw6uJl6pkvAGDhlkOl-1XFbAMyrLIfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
زیدان:
لیونل مسی بار دیگر ثابت کرد که بازیکن سیاره دیگری است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/Futball180TV/99131" target="_blank">📅 01:19 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99129">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JE8X5QZqoHJsNBr8W5qlEPVSAPlyTrEjTf2j6YY-tMqhy8lXhl-XjWZ1HVUS53J8PCjJQoqMGDVRSKwpDJag4xUOOLoEEnmfOfU4AYWr_jg53t7sba8eGzJ01LwQVIi7YoR8QK2z8vsoKECkkY5wE7yh_f3VLFOt15N8tKXjz4J0s___uM20-U22TYaws2WPthkgS9XnUhaxl-9cG_hgQqpEsZVDolPM-kupigON2XArYFbOIUkELkBZcSN83AgyUqXnJNA9Bx6224MzgPA6FLtTHx_TVD4r5HwbnFGMpDF0kEswKw1bbRQT3hbKdGuvGnCp0EsoYtZ4qWuseeaM_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
ترامپ: این اقدام، تلافی بمباران کشتی‌ها توسط ایران در دیروز است. اگر این اتفاق دوباره تکرار شود، اوضاع بسیار وخیم‌تر خواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/Futball180TV/99129" target="_blank">📅 01:10 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99128">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🚨
🚨
🚨
⭕️
#فوووووری
؛ شنیده شدن صدای انفجار در مناطقی از کنگان استان بوشهر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/Futball180TV/99128" target="_blank">📅 00:56 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99127">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q8JM8jFJcSFPOeop5pAYPfByXpI0HdPAAx7yquGVQSC32VLqGm2jPhjWryssPrwt66npyhPl9Yk40TVzNLhpulK7B4--fndpJts3yUt7ecTo3sfCIvQR0GOQQqpdNhiSTB0lvGEyJUPwDGJLsm7xgMZlL7vIXF1stDIPm_GTU8Pq41B4XAmN4ALmSZDKIvMOCkjJjio66mAuXEWL7kqcWwzOKpqTcXbnHhq3dhVjDhnnnTxnH0E59k1rnCQkOqupJuHz9JTKRMN6GU9qWjJv-A6pxyVOUEzqsPtF9eq944WFBdX2Y86F8emaTGFXxPUtGZksMEG09xA0xXeHhLlVoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
⭕️
محسن رضایی: دشمن متجاوز و هم دستانش به شدت تنبیه خواهند شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/Futball180TV/99127" target="_blank">📅 00:50 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99126">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🚨
🚨
🚨
⭕️
یک‌پهپاد آمریکا در جنوب ایران هدف قرار گرفت و سرنگون شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/Futball180TV/99126" target="_blank">📅 00:46 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99125">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🚨
فارس: دقایقی پیش مردم در چغادک استان بوشهر ۳ انفجار نسبتا شدید را حس کردند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/Futball180TV/99125" target="_blank">📅 00:45 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99124">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cgZ2KrkxEbzgYhTV6HU5phssQH_NTVVsN19uEbOAsTVPUF-jw2gYxBmAU6olTso7crBhs5qKHwG3MWcnC81I45N53ZaUbQP11NXRAflf2XHPhxXyeBGAukxY08iru41pGKlqhj9hs8u9Y0jo3owBtaqTc1VDBDFAzI2ZIoaXQ-1I1HRhBKCkFButHCQfgF0RD-BWLIn_yMHSmbxcxH_jcslHObzJ9q0NnhqdtLS82Ze9QpBEHxJzk9R4bBFbkBchJon8rnVf-qZpLtqfhE5vZxDuCRV2HVbkeT1rR5MnqNQFsiE9z2XPka0_7SXBuaQ8pL4IjywAV3nT635a9zFLaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔥
پست جدید کریستیانو رونالدو:
‏"پرتغال، همیشه و برای همیشه."
🇵🇹
🇵🇹
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/Futball180TV/99124" target="_blank">📅 00:42 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99123">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🚨
🚨
🚨
مقامات ایرانی: تاسیسات‌نفتی در حملات امشب هیچگونه آسیبی ندیده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/Futball180TV/99123" target="_blank">📅 00:37 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99122">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🚨
🚨
انفجار های مهیب مجدداً در بوشهر رخ داد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/Futball180TV/99122" target="_blank">📅 00:37 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99121">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🚨
🚨
#فوووووری
؛ انفجارهای شدید در جاسک
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/Futball180TV/99121" target="_blank">📅 00:29 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99120">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🚨
🚨
🚨
🇮🇱
#فوووووری
؛ اسرائیل هشدار شلیک موشک از سوی ایران و حزب‌الله را به شهروندان خود اعلام کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/Futball180TV/99120" target="_blank">📅 00:26 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99119">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🚨
🚨
آکسیوس به نقل از یک مقام آمریکایی: حملاتی که امشب انجام شد، گسترده‌تر از حملات روزهای گذشته بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/Futball180TV/99119" target="_blank">📅 00:23 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99118">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🚨
🚨
#فوووووری
؛ شنیده شدن صدای دو انفجار در جزیره ابوموسی/صداوسیما
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/Futball180TV/99118" target="_blank">📅 00:23 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99117">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LeUBxtQHaY23857FYZbtgkTHOBmC8ENg8EdNa0mYZTCqcALPSUOD6IDmv8yV-E6eXFQucPJFxX3g-cXYNjnqhOUsXN9OTXyNWymkZOrDGP0-jDUEChICp_Iree1uwSnhjJVXgIxOIxfn55iutwVf1pj2dON8U-uq-gpqhm6D2PBUfTROZ9e3i_LytWxPYCv2U7uoDPTtuX2rLLAl3V4apo1ZxXAP4kvmQLV32mcM0h_FZBB0tEgwy_vdWUqPt21mvHcaRNRFw5Fr33-IdMWG9zOkJqKAn_HmUWj0r4JPiQuh4Vg0EZ82cm01c1rL77DRSV1oTwgG4JdmS6bWH1ytpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
⭕️
تصویری منتسب به شهر بوشهر
!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/Futball180TV/99117" target="_blank">📅 00:22 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99116">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🚨
🚨
🚨
⭕️
کمیسیون امنیت ملی مجلس: بزودی پاسخ قاطع رزمندگان اسلام در سطوح بسیار خاص و ویژه انجام خواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/Futball180TV/99116" target="_blank">📅 00:20 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99115">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🚨
منابع داخلی: قرار است نیروهای مسلح ایران به زودی حمله‌ای گسترده به پایگاه‌های نظامی آمریکا در منطقه انجام دهند..
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/Futball180TV/99115" target="_blank">📅 00:18 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99114">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/991a36705c.mp4?token=I1HyKd_tSYGZNz2OP6et9UxnIFI-f7YwNRTVDij71fd5KbArbTf5A8tFzGYbcPplmrgMpoYtd81KIB7-A9oeSib5USxhR_AxJNzuTlan4NPxiaCdzq7yp8ezrtyKggZWJaspolYMPxwZLWA8DmSFFnrJIa-gYDZoP-crzoYWYNE1yBX6kKsS1HIil4q9jwf5yRdmixJW4tjoSRP2xoAM0v3KHO4u3h-0ryWkXkPa4pRPewf8mt7SIyg9dbSQqt_qkVhQuWoyJG8H4k6PWlpbR7puSRc_yWqQLAG7gytokZhPkV9j_Af84fa0Y9yW3W4LliiHGHV5b73IZts9Y27i8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/991a36705c.mp4?token=I1HyKd_tSYGZNz2OP6et9UxnIFI-f7YwNRTVDij71fd5KbArbTf5A8tFzGYbcPplmrgMpoYtd81KIB7-A9oeSib5USxhR_AxJNzuTlan4NPxiaCdzq7yp8ezrtyKggZWJaspolYMPxwZLWA8DmSFFnrJIa-gYDZoP-crzoYWYNE1yBX6kKsS1HIil4q9jwf5yRdmixJW4tjoSRP2xoAM0v3KHO4u3h-0ryWkXkPa4pRPewf8mt7SIyg9dbSQqt_qkVhQuWoyJG8H4k6PWlpbR7puSRc_yWqQLAG7gytokZhPkV9j_Af84fa0Y9yW3W4LliiHGHV5b73IZts9Y27i8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🚨
#فوووووری
؛ ویدیو منتسب به حملات امشب آمریکا و انفجارات شدید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/Futball180TV/99114" target="_blank">📅 00:16 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99113">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
#فوووووری
؛ پدافند اصفهان فعال شده!!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/Futball180TV/99113" target="_blank">📅 00:14 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99112">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🚨
🚨
تصاویر منتسب به نیروگاه برق پایگاه نداسا در چابهار   @News_Hut</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/Futball180TV/99112" target="_blank">📅 00:13 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99111">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PPW4kogOWvKNWnxTxtN0CMp0jGfZ8JIqGTFEpPGm3xmA_vDpj4eVUD0d5e9kUc6PsNSWXTGHXPa_wyBzPO_Rq1j6_ANhB4YDfRUirmOahywNubQ7WdxKU5Xdhvx4WU8DB4mZmyT41BHvFQSW_WGpN-6Pa8dngwQPsJv2S8wnAzmtZXmMWjBa7GN57FgKLj7d_m2_3loex6GueWE0_GBzHX3gjAsLci-UMFhow-2PcPDrwyXQW28cfId8jU3ofmhdBrt-Rj0O4lV6qnJpky6UOvAsRt6y-0Z_gVBQpYQ07G8dGaBv77i4zg3UD6JKxRjl9NnjSv5-rUZXKUKBu_oofw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
رومانو:
چوامنی تا سال 2031 با رئال مادرید تمدید کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/Futball180TV/99111" target="_blank">📅 00:13 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99110">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/82d743a24e.mp4?token=Fj-_NHcUbo-CEeu47wvG9SPCsfAXYmkK3CCmgBowe6O7QrnfJQfR8ju9tdJrwwwA8hRYQwRflYUHDI5THvAs5W-yz25dROIg3A47XHRjMWKwEQ6iBnNMY2q9izttCM-6lCtpF9nmjXW7hOcqv-ktIqbWF1vhquglet-HHKJ9t0uyp8zm5OQItY4ebRsF0_8rSaJt4YzbeJqdsfgwfQB_4MXlX97mWwqU2G44yngEkuI_0-8T4D67q8-MEMYPEOE8eSnuxFnD6hPcrKUgaUhsi-cK7a5qGIBCYj25G_KR8LHfLlh90mkJ1swx4VNRUOzZGtoAIUys6AAglo0jrHip3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/82d743a24e.mp4?token=Fj-_NHcUbo-CEeu47wvG9SPCsfAXYmkK3CCmgBowe6O7QrnfJQfR8ju9tdJrwwwA8hRYQwRflYUHDI5THvAs5W-yz25dROIg3A47XHRjMWKwEQ6iBnNMY2q9izttCM-6lCtpF9nmjXW7hOcqv-ktIqbWF1vhquglet-HHKJ9t0uyp8zm5OQItY4ebRsF0_8rSaJt4YzbeJqdsfgwfQB_4MXlX97mWwqU2G44yngEkuI_0-8T4D67q8-MEMYPEOE8eSnuxFnD6hPcrKUgaUhsi-cK7a5qGIBCYj25G_KR8LHfLlh90mkJ1swx4VNRUOzZGtoAIUys6AAglo0jrHip3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
حملات متعدد به جنوب از این زاویه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/Futball180TV/99110" target="_blank">📅 00:12 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99109">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/acf4c74933.mp4?token=ciRXpiCBc-_BjgDmdc7pRy6T1I1lzk7CiQe05PQgeN5vZqK0fZUhV3CPr0ZrRMwcJZ_kCFfb13mdnzXV1LMfsrrQDZk9x1RA4B3P0kZWIRXbS7THrL6vX4VssdE6RPkGgL5X5fiyyU0ptJeyJ7nUp61hYW22sZhrNzaTo0cmEJjWQwfEnFncNEFMhbcu6DjiQJK83QF_SaV9XH4cyRG8oUKVWSoMcJUMZ5duQ725eX2mMZS1UWdQsrqheRSOjcpXLwD-ZmJpa0GegaQLsEZ4HNcjfkaL-CTPuweQXnhpT7lFK8vJA-_3NlzxMWJncrMYHK3zqv0OeOZd_a8uq_AKcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/acf4c74933.mp4?token=ciRXpiCBc-_BjgDmdc7pRy6T1I1lzk7CiQe05PQgeN5vZqK0fZUhV3CPr0ZrRMwcJZ_kCFfb13mdnzXV1LMfsrrQDZk9x1RA4B3P0kZWIRXbS7THrL6vX4VssdE6RPkGgL5X5fiyyU0ptJeyJ7nUp61hYW22sZhrNzaTo0cmEJjWQwfEnFncNEFMhbcu6DjiQJK83QF_SaV9XH4cyRG8oUKVWSoMcJUMZ5duQ725eX2mMZS1UWdQsrqheRSOjcpXLwD-ZmJpa0GegaQLsEZ4HNcjfkaL-CTPuweQXnhpT7lFK8vJA-_3NlzxMWJncrMYHK3zqv0OeOZd_a8uq_AKcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
نیروگاه اتمی بوشهر هدف قرار گرفته
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/Futball180TV/99109" target="_blank">📅 00:10 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99108">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🚨
ایرنا: در پی حملات امشب برق بعضی مناطق چابهار قطع شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/Futball180TV/99108" target="_blank">📅 00:08 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99107">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🚨
ایرنا: در پی حملات امشب برق بعضی مناطق چابهار قطع شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/Futball180TV/99107" target="_blank">📅 00:05 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99106">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🚨
بیانیه سنتکام؛ فرماندهی مرکزی ایالات متحده:
‼️
به دستور فرمانده کل نیروهای مسلح، نیروهای فرماندهی مرکزی ایالات متحده، حملات بیشتری را علیه ایران آغاز کرده‌اند تا توانایی این کشور در تهدید آزادی کشتیرانی در تنگه هرمز را بیشتر تضعیف کنند. ایالات متحده، ایران را مسئول اقدامات تجاوزکارانه اخیر و غیرموجه علیه کشتی‌های تجاری و خدمه غیرنظامی که به صورت آزادانه در یک آبراه بین‌المللی حیاتی تردد می‌کنند، می‌داند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/Futball180TV/99106" target="_blank">📅 23:58 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99105">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d1d5e85683.mp4?token=azHms0aYJwG6VHRwgOM7uRWZpSpcqOeHQY6gNXPdJYbp4ngxeWq8W-n8PN93skidoivWwB6gAACKj30mO7fRZTathRpWZrCFX_O9flTvIBaSN6nvrQhA0Rtm_bS5pBUymrNAHz7Ks6uZZDevdVYTqCmK_LySoXXCl9yZBelQDaoNZI6WFiGEstlWfLN0LSCCoKLJtd04o1plVp9g36V5akVdaj2dhHHNYGGclNIofmj74l2nRzKohMi-8SUnRz6_wODVjlRMLKGbSMaFP6k_Q_GXnXBHXj4d2eL7ZMGBZL-KeUaN_FCjl2N4VMH7Czpf3sSHY5jUIg3-6-f24K4jBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d1d5e85683.mp4?token=azHms0aYJwG6VHRwgOM7uRWZpSpcqOeHQY6gNXPdJYbp4ngxeWq8W-n8PN93skidoivWwB6gAACKj30mO7fRZTathRpWZrCFX_O9flTvIBaSN6nvrQhA0Rtm_bS5pBUymrNAHz7Ks6uZZDevdVYTqCmK_LySoXXCl9yZBelQDaoNZI6WFiGEstlWfLN0LSCCoKLJtd04o1plVp9g36V5akVdaj2dhHHNYGGclNIofmj74l2nRzKohMi-8SUnRz6_wODVjlRMLKGbSMaFP6k_Q_GXnXBHXj4d2eL7ZMGBZL-KeUaN_FCjl2N4VMH7Czpf3sSHY5jUIg3-6-f24K4jBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
حملات سنگین آمریکا به پایگاه سپاه در چابهار
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/Futball180TV/99105" target="_blank">📅 23:42 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99104">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🚨
🚨
موج جدید حملات آمریکا به جنوب کشور آغاز شده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/Futball180TV/99104" target="_blank">📅 23:41 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99103">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🚨
🚨
موج جدید حملات آمریکا به جنوب کشور آغاز شده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/Futball180TV/99103" target="_blank">📅 23:26 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99102">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RuCJwrOB3hZwUD71EWQPVuMmeF2wBRkwmS3hzEadbmOP4hxKySuoFipOVc34had_W13ezd5N4MlXhdQ1XDfRL-vlnd7iM0PNpUTZDM9xShSlBdTqe8VgK5LclR6cx2AW5_zvXBhReIC7fqqvOvjeAwwsAgyVTK8rWKv-UTDumqUwNrmIszwTznRluv6lNiHdLzVyi1ngZkll26_5J3oR5KSLZuUiwcvqhQBcha8AD-u7uLbmwY-mL3JQJCbH2hQz3VWihXIcIn7zsT1atDvoAkEEBIVohDak7m466Tki3b-4bwPEsiiZyEs9dSNu4bX-SkPIGT86xv3wPkAmmiqhUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
آنژ پوستکوغلو:
چه سال اول، چه دوم یا سوم باشد، تمریناتم را تا قهرمانی ادامه خواهم داد.
میخواهم امسال با باشگاه النصر بهترین باشم.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/Futball180TV/99102" target="_blank">📅 23:25 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99101">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e2cb709e88.mp4?token=RinE2I920dLnBm5p6gJAAnJF1pELX1I847UuGbvuT7A2_s8fKpgLGGZi1vq9bKudWm8Pnfn0SW5IFmNtkKkq8y2VvdpiNS8GJ_mbGOU-CN-rn-oZbAAbvyPMDTv5kup0n1skxoImg6WZG-JFC5wEgcUYAWwzBd_2GowwCCLsiICRUXQD711J0hshXRbDhzUyk8BuN2sFbO-uE85hbCSX8njhIx_du6tg2Y8QP71ETEpB4x7Ta3d3z6NXZP4Ai8MGn_iXoKHzCUnV3GhvqINU6LTdHUm-jk2MtwX33JnLzC4Nh3ie4nZvbS8wsOQ69JtP-aEsVE1B08H4XzrUESPKRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e2cb709e88.mp4?token=RinE2I920dLnBm5p6gJAAnJF1pELX1I847UuGbvuT7A2_s8fKpgLGGZi1vq9bKudWm8Pnfn0SW5IFmNtkKkq8y2VvdpiNS8GJ_mbGOU-CN-rn-oZbAAbvyPMDTv5kup0n1skxoImg6WZG-JFC5wEgcUYAWwzBd_2GowwCCLsiICRUXQD711J0hshXRbDhzUyk8BuN2sFbO-uE85hbCSX8njhIx_du6tg2Y8QP71ETEpB4x7Ta3d3z6NXZP4Ai8MGn_iXoKHzCUnV3GhvqINU6LTdHUm-jk2MtwX33JnLzC4Nh3ie4nZvbS8wsOQ69JtP-aEsVE1B08H4XzrUESPKRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چی شده که برنده توپ طلا اینقدر با ما احساس راحتی میکنه؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/Futball180TV/99101" target="_blank">📅 23:16 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99100">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZlNYCbd_GCq-XI8l_Q3ak59QPfx7kwq3r-YOhagSA6FD1zgM5ZNWaJoNGJ0LlbTjQspM5BuxHqG70mhASCz1Lhr-rPrX6rdwu6rm-tyr2icXFIe3EqjsNYdIBFb0aaVyEUaKAsfdiqyhb45Yx8MIqqZrcpK_VExSb3uy2dzKXsDvS1hjKeihPvnOG5iiJOljEpCDKB3HiE6ABMpYr4-aaQH2oW0rCyRcTUYoBA8uqq04685vxwH5pgGawyzBdfQPqO4Oedqrp-PzxBFiwHIuTAIpPvmId5_Up96tnz-JjG8aXmehCwtJAaNRK_-lEPOx_fMvIkcxmTlBjKCDIpZJsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جاستین بیبر بین دو نیمه فینال جام جهانی قراره اجرا داشته باشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/Futball180TV/99100" target="_blank">📅 23:13 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99099">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PrmfamWz3gAbk501kUo_kTNkU5qxc1Y2Sfz64mz6mFDJ9yQiJYA3omwggctI5I9BDz-2qci3QjDxP__3uyJxpPDHlCviuVLv6TzIDgKoJD-2AVxv7GewMN_45270IdVw7KKTE1tw2Eb6XHJy9Y7jkIyV4d-ZIJYoweQn8YMp02k8k4gHFkw8HMvcK64qu8tgWcmMTYiv5YmYIXFE7E6ezwrz0WHoElMD1oAQKQemY86UmBYiorp_XAPF89_RjVbDYByliGhaZTWvXZd6rJY-ECAnsouvwI3Q-tM5jSAqecuFmV0LlzFSZUrn7PgfeEYuXnycLCpYidKOzU0hupXU6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
رافا مارکز به عنوان سرمربی مکزیک به جای خاویر آگیره انتخاب شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/Futball180TV/99099" target="_blank">📅 22:57 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99098">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CLrhlY8cg2CeypuVLkWN2KD--NRC9DvjPD3FbiZwzcFE6HkvZqArfrksaxO8l3L_VXQFavm8-5CtjrPoDqQsS6WiTbtTG4UiavvVtDGxR2kINeV9Nx8dQVPq-qvu5DASsXM9IoKgGdSs52vLyCz6cWSLSizmTkhD6sUkROgqAl_8FcqwUne9Msdu8M7z8fJEEYW470ThnU94XBSOpe0Jk_nyqNqQbQ-3vxQoot-b_AFl7nY4WjPouUFtUVlceTz6HgC_w_EHoO2syam6iqN-5JZ7nPyuplVxRMZWvTFLrOqovZtmo2p_acZsoHVuWBC0Rs6KeP2SJyJwmZBkffIh5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سلسته آماریا بار دیگر به کیلیان امباپه حمله کرد :
"این حروم‌زاده فرانسوی نیست."
سلام و احوالپرسی یک رسم همیشگیه؛ صبح بخیر، عصر بخیر... این یه سنت پاراگوئه‌یه. چیزی که ما رو عصبانی کرد این بود که وقتی اورلاندو گیل این پسر جوون، با نهایت احترام و فروتنی دستش رو برای دست دادن به سمت امباپه دراز کرد این حروم‌زاده نه‌تنها دستش رو رد کرد، بلکه سرش داد هم کشید.
این رفتار، رفتار یک فرانسوی نیست؛ یک فرانسوی واقعی هیچ‌وقت همچین کاری نمی‌کنه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/Futball180TV/99098" target="_blank">📅 22:52 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99097">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gmJ19Z4vWIJDXERrrNZfSzltwJEiTgEbyIxmMXKgaqHBqoQDGDdZkL-fdVinDlI4xZKxPkVqpEV0MSJruwvHvrMGwmj4CqbLtHr0S6D0k0xvOpCw-1ej3_C-B9M7TKZh4d0fWy0sXhZ_58nyp6Fk0H3PRmN9hpe8SBYm27E4j0jgl0fvF_YES3AyW-vfU6HNFa8ZwFB6_j3kPSYjPUBhm6M_niE4D2HUt8nZFSgsnrXsVMfyj9ZQLuxul06jXqk2zTAKMi-n4_FSGi_6UJ7tlgY0GfeLnoERDYCYgN2NqgvvRwOypNVE4gWufdi7xcpg1OswhZR5Q3pe-i6eRPL2_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در چنین روزی در سال 1990، آلمان با بردن آرژانتین برای سومین بار در تاریخ خودش، قهرمان جام جهانی شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/Futball180TV/99097" target="_blank">📅 22:25 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99096">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DrFmZ8jlxCVRR4MaedFEpYj2XwUT2ozFCNQ5T44aR1rKPLfXqtEJco0MgopL5RmyrzD8R3vJ9pDZ4mO8RMsZxtTd8qPI5oYIvC8xwMh0cRuwhAyblw54egOZXVY8GfSauBmybaHRDDOgAJqozWQmSwqClom59hQLwlG1VOV6_DQ6p7rwfOUSi6unc2diqh2DISAhwwLHCblbI9uja0oHemyFAv-SYkBq08qs7ueE_4J_xwcikRNF5tt3lzThwjaOH5NifOTJ2U0cOlPCEWCO3rc4wSkSfpENIsAkHJri3uVzsWV_6BsYeX-StpUy2N0MuCTa4UXNteg_V1gk4ccZYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
شانس بردن ۱۱ جایزه ۴۵میلیون تومانی داری
فکر می‌کنی از بقیه سریع‌تری؟
😉
⚽️
وارد این چالش شو و
کارت فوتبالی اختصاصی
خودتو بساز
⏳
فقط ۴۵ ثانیه
وقت داری؛ سریع جواب بده، امتیاز بگیر
و ببین
سرعتت شبیه کدوم فوتبالیت و ماشینه
👇
👈
شروع بازی
👉</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/Futball180TV/99096" target="_blank">📅 22:25 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99095">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i3rOQ15k849MsC7Rrj-c_eX4ozKcR_TYKGw8u3H-_bCzl20PA5X60i38qNkAXXlf3-rH1Pv4Rg_H2vpPb084ZptCu8x1vyJjTH78qH3oSPzH-nyhB675du040dRAfwych6hyEZrTfxnHm_UBf3qfnuTv65o53bAuxzogceID7ZkMrI37Io2_iM3sLgV7GhYDXsZol1GXh10bfukqFr0hJojkQ5CRGgjnQ2gvWctPbeUBbgp5lS0nPh66CaytB7-EbM-dzCUmWqWgx2tBxtwS7TCp7gdm6_uVNNyXYb5QNrVCJQVLC1IVHzZqVeQ4-tiHjZWcpKhWoKd8wvJH5xJpsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟢
فران گارسیا رسما به رئال بتیس پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/Futball180TV/99095" target="_blank">📅 22:16 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99094">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WZnHK-dKsDc5Os4GjF9VWOe2Rtluigb1AWr_jQbUnKJc7YLkIJFSGe1AwIWcvONVZRe43SItABSG028T8_N7j6MwBv1ejv_KN_zNssmyGxiKa2n1_I2qC4y6jK1Tg1mGcPRGf6OJcL5LFl70Gmf9WXIbdEa-f0NWHhz8ABKwZYD77gKsyZW0vhSg2Mkaii1aYtddEV1eBsM6oVR98Ov-Zv6AV2xZnnb7GW_CrMHoG25ETIe1X23EYkVBcMpO79zV2-uG0t_qkFeEigFHwDz6lyzt1d-eba7o1c_vNgbGmIKuZNYa45syHIXaGXso_mp61QZ9HHY0edtwqg-vyTbGWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این هوادار یونایتد رو که یادتون نرفته؟ هنوزم بعد 634 روز منتظره تا من‌یونایتد، 5 تا برد متوالی بدست بیاره تا کله رو بتراشه
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/Futball180TV/99094" target="_blank">📅 22:02 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99093">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OdYkuVwxfP0RDL2-p1JkM5LpifmSYrIeJR6k2IORLlJUM-DyUiLAFS0FhbnLzoG3XSWMFtMUoDfbY5ogxb2jcCfwnTzk99oIPV65hgQEG2hjbLO22zAE_-KOM6Fly5WFb08jYgwdYe7aG3foBb6nBVRyILQY-mqv3JvjAD2l9WbwTgbw_PoCDgc4lal5boIGEhnOdw0or90gZM_xSSCW0vz72i30zVymbVQiLJL_FOD5Qg1hnx1zMojva-qWMBggbqs9BcktyYmIQqyCDAAYo2Oi5UgdadYRj4TnVrQ6m-ba4dCikZjEPrDV_PiuklcMcBiydaAtggEbDaGBH5HHxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇵🇹
ژرژ ژسوس رسما سرمربی تیم پرتغال شد.
🔻
ژرژ ژسوس رهبری پروژه لیگ ملت‌ها، یورو ۲۰۲۸ و جام جهانی بعدی را بر عهده خواهد داشت. او این فصل به همراه کریستیانو رونالدو در النصر قهرمان لیگ برتر عربستان شده است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/Futball180TV/99093" target="_blank">📅 21:39 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99088">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QA8QpvXs_EZEh6XA6uYT5qz-jivfNToJ34t_0XygANPJ0Lod--KpDHV9Vq5nnPU6RmM40uQUKEhJ3j_dT-kIeGc8-0yvydCzYKUtCrqPHbmGRF3O7mLMcoutWRgEXYfJCdRNZJ69r6AoQQ6o9VKR45KHLxjVpOwVTXthNXLlPCPNllxYnN56wKGagwtjaFlSB3lGn7xXB75alPI6X3FQz8JNN0zKiZzfkhDlSwqm2sQceOwEtOO-0M5rbatm2sBZUbe5PFcOiTvfowRfeNZR8OliMCAJHl_Nv1ltR4ShIk5SAcP0u6E-9XULIryLVLFOduWXhK3oYI-Jmcpoi1Ht8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nEan-SK5S59EjhnBOKYnpO9R3wVF5d3Xec9mPq_PACB4FWnWVntfCMyLEb_ExUXk_Fsy1v5LnXq0UX4Pa2UvjUPGohm786LWIRzBHJ2rlXDvOIeSmey90j6ezJOG26hmaDF9yUVtE1gecOLj4uuEp81Ju4YIgCAOFHxcqsUP16S2fgnNlN2aGXY3kDUYIKfMxAVM4tMZTA3Dpz-BxccEmr0J9XGVabeZZxqMuiEsdxMKlEoZ8QUCO5MgZK50NlrlRvoAnzRVRw-nyJS8VdOq3oxNE40tl-gZKmt38RNDyu1F6jAGPDSIkbYaJ46dVa7vzeRfsDH42HMDAA5DFMo74Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VbRtBnaeBDbQHaFPXGIrgy7Mq0-78n9qVcjlxY-qpfLVsf-A2UQJPdyFPPw_ilPi67KwyqVi586iF4pG3bLnhtao2dRWW2ePP37PXF0cGLUetEXPq_5uG9kXeXGTVWtQKYHI0M-P8rEdnZOAGYQeFrvJa8FXE9Zw2bqVS3Lgnm2jd-KN_uEBW2eG1sG2BjPU0QJwJFuhUsMnMAxFxjzdiYLQbd27ETk2GiJJvT0mKT8SDtuAI9tB8BjRT2iGXecKWlnxwH5Ag0iISjneVmzduEhHXOg1VitGJPalFdZYUZm0niHmo_kUEGDt5yDEZZlkqTuxCJANn3J5VpOyTXqfow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PH8r-P7OPypzMb7Bc_zO7pkrExl-_unT14ycZLZ1rDANMOAr6JntMMIUpcWUGah221D5mnEL8um6hleAqlZMQNRs3Uu2mSv5jbaJfSerOtI2JwMrNlL8VPX0i78lSrXRrSzhbND_lKw7OpxPsR2Sr2au0ePmA3g2WenGGDKNeZXzB4Na18MgrTOm_ihBX4J7cLccSOTLPJY27gsjPOxg4TiZO0liCvvor-G-fc9yaYj3aO4wSoF7a20L4M3bbUV9ld_0GxjjXiF2TF7L0nofSYvdWvdqIlA_niqcYO9laQQENxMHOuEBv6VxzkgQCG4Idh6a3B-vxnNXNW53wMNoFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hmjvgoT6xMqNP-7InOIhIUnihE_jqF4BtxD-81le-YF15Aey5UluLhjHPQX0TOBpaNvj_nbfUeJ1hIGVWs8P9XSTwNW8ab0nTk8DtsVWZ88bK5x-JkWriq1baLSthCtJszz-Z8VJUfJ8LaPipI66_tcjUAlW5ZPagr6vhF2Tyf3rTx3lxhq1h9_itHFoKe2B0LijTR9ldqarLGyoc_a2s-xRXQc8z66M59FtUSzKvPonauJ-Vjlu4zgqPiYb_Js3Re1e4WalzBbqZwmHxi1IB_C-WNRKnhB5AkMR3yo3slE3zpQgNsXB9kf6JVy7kKW3wqTgN2G__gblbu2e_eek4A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇦🇷
والپیپر آوردم براتون :
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/Futball180TV/99088" target="_blank">📅 21:21 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99087">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cP3eKYkt7VsvAFrNL7t3-o4cAsIT9rkar9RNEkG3_OoSXa_VcjaoT9uAEXkchibhxvzunGZteRZLjad_I8dtTgK33hmCzsQfMLgNA8kMOOIqVujwtGE-LSPMaoO6VDHNhHphZzGCCc2-Tze3eLw0IlrmHNkI7TMEOhbrDXiaU0_79s3ny1Vnwf4C7ohhTZi7dYU7DcYDGvnhpXjlrKqaK5O8iv-iAh-vqvO3f8J4crbQDwao--T6OD2AWF8OKCTQtokqLoyQlpT7QcQdUhFgXWWlVHMziWlfIlitv-2M-LRi7o3Py_ms8SzFut0uMu9dBkUn208LKfiMnsx7usWguA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#فوووووری
؛ رسانه‌ UOL برزیل: نیمار احتمال بسیار زیاد بزودی از فوتبال خداحافظی میکنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/Futball180TV/99087" target="_blank">📅 21:12 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99086">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ir8B1hM2SfQGcTe9CyAH0VrdQlZhCtFpVzK_ZEO4WMfZVLlSkpLPvsLCnRZGAp_o4kK6OLB_KuXz7sOkIYwZREmDwMYmFwd05hdGJRnTezbAtMuIje8Uzt2USEekbkyJe5h3nqrxPMaa7K7YZmcYEzLOPuMx5PHg4c0NKPFHgdIeM2o7bRhzPy3TG1h4qfUh44of9NampDTNI4aw1UktovP9khniqfMAzf131xYIfiX5vLyDvszVvtkAQkfgn3qbVQLxWkxNSzuG7Ysjg9CY0E7OAvU0OW7EbkDhVosnpFVO_wASVzYj9cYITzmZJqya7QMHN_vkaOJWbUFb9RuFJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
آرژانتین میتونه بدون بازی با حتی یک تیم از ۱۰ تیم برتر رنکینگ فیفا به نیمه‌نهایی جام جهانی برسه
‼️
🔺
علاوه بر اون اگه آرژانتین سوئیس رو شکست بده و نروژ هم انگلیس رو شکست بده، آرژانتین میتونه با شکست دادن نروژ در نیمه‌نهایی بدون اینکه با ۱۰ تیم برتر رنکینگ فیفا بازی کنه به فینال جام جهانی برسه.
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/Futball180TV/99086" target="_blank">📅 20:55 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99085">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UxlzL5op3uTD53Lkx1wBjk2-F0KtN_5W772-s8F7ywYtRnhIkWEGNJ5807uk8-QCGmtCdnCs6aixsuUjzgrT0kIE1_MP2tdJcp_jNewcNOL4L0zneFVUlz5satVQM5X_034MVdCY3N7-sTpO21ssD-h-RpaM_ETOg1WQnVn5Q62m9RWjd1OzIJDZwpg0T-ZlQUnKvLzPi77g3ODdmvgQllXjHthhqjo_55iWRjXsNvnjL8-Zm1S54SCXlgdPdRA159xzOyErPRCFByqs4zqoHT8piacSyqv8yEfCzTsTKLRjrLIr_dJAB_cQgMZOD7v0Btq0hO15FyfuLuKCRT21iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇹🇷
#فوووووری
؛ فنرباغچه ترکیه با مارسی به توافق نهایی برای جذب گرینوود رسید تا این بازیکن را از تیم اتلتیکومادرید هایجک کند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/Futball180TV/99085" target="_blank">📅 20:55 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99084">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hUoW_d5D86iPID3QmTUQdIc7sdo_xKxGI65ThSXwH-sw3NndrmGlgSvmVC0fKUx_WHffw6389hjPHGPBYVYgULAi7tS3_NST3IjJLq7BbxQJUTUboTHdKPRh-Np0EoWS5sMwpgb2bjtTQXatOh2E8K5NC3vDL7IlGMXiIoYW7-9CLPg5RseElXSanHxRv8SDfliCI3M-y0qr-oW8E9pzKRNEE4LdGjWeT5j980IHyyDA20divFFhGN1dHz6HlBIyPvWcNNRehRXth69Dl661_aIHvjLHPP4NseW9SP4Ny4ydvnp7OwADraFv-l5bD2lobfrOCRwzdpLZ1OGj2oK_KA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیش‌بینی خودت را ثبت کن!
🇲🇦
مراکش
🆚
🇫🇷
فرانسه
🎁
۵۰۰ دلار جایزه
بین تمام کاربرانی که نتیجه مسابقه را به‌درستی پیش‌بینی کنند، مطابق قوانین سایت تقسیم خواهد شد.
⏳
فرصت شرکت فقط تا قبل از شروع مسابقه.
👇
انتخاب شما کدام است؟
🇲🇦
مراکش یا
🇫🇷
فرانسه؟
🤖
برای ثبت پیش‌بینی روی لینک زیر کلیک کنید:
https://t.me/betegram_bot?start=p4_r4EF37DCE
🎁
جایزه به‌صورت فری‌بت و مطابق قوانین سایت پرداخت می‌شود</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/Futball180TV/99084" target="_blank">📅 20:55 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99083">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FSuJF50VvcoHgjE3iscbQ1lxjpUzn_TOQdFC6erJ9YPVHAmEEphzNsaTPIZ4UZmEoygDZjfseAYCFmBYkTE6HufGvXoCUF9gdv8DHx3opf7PMD7uob8eFSnZlS4FsIbk5_WmMrqIBrJxrAtfO_wtRU-tKDPrxrChMqMAQXNLi5Cxn3fMkAcSyqatYI4s8fiLZmb2fA-lzJtfeuu4I13b76JXaMNWlQcFHaf2XbPhmFAR85pjxQ6V3rcdWQRnnmL7NDmUp0wnZ5DsSuY40-nf6HOu07Svo5M3nC9odv7IGzY7jhH-X5ckZL71QOz26s0kU4_rPaTlEQNy-k-h1L-UdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁳󠁣󠁴󠁿
#فوری
؛ روبرتو مارتینز سرمربی اخراجی پرتغال گزینه اصلی هدایت تیم‌ملی اسکاتلند است!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/Futball180TV/99083" target="_blank">📅 20:49 · 17 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
