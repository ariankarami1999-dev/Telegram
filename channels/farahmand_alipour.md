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
<img src="https://cdn4.telesco.pe/file/OAnz6I64xVSrLJNzCYWhXoj1F9ir-H7_ZSwgU8iCYp2q2kkLn6i1v1BRXqAsu2IcwNZTRkbVRxgKYKc-zhM5mENjkQ92T3p6k85FnXxdCme2JbQj7xHN3zPOqYTiapuLH5IloMvI7fhUP_Ckm6h33NkLJ54sc7GAjbuVBmAgnQKZINXPoZtkDLMjv__6xSLB2E65wNZSlzEX-Wh1qbU3yloDz3659eYc8WAGeB3lBNmdlEgdbl09SwgrKX8sxJyyJ6Z-IcllKTMr9QI8VDnUtS5AX06zjkduyuaEp9qUedqAKAns0dcHPk40BmxidjWRBLdcslWy5CvJvXQcDmYARg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 62.5K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-11 13:10:54</div>
<hr>

<div class="tg-post" id="msg-5834">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YYpS2AGyOFJVNJHDIntWcTTBzu3PdjdY18dppzEwL1jCxfGZv6syisx77E5hiMHQEPYnJtUTSN9gZXYvTd177TsveVJqvA0LGWivRTQChf1q5mzc4OG542pY63Y5_CSOZgNYufdzZz-B3Yd_U8TlsXDG9NEsdRvjAQnl97Cgtu2iWJI-GYu-Fbcn96_Ol_EWdmmJwESqGPryWonkVcZphsPFW_ju0RB1ZI5L3FWhEzAHL0zhw5psoQPDc1xzjYkbeyqPUNtH2cw3TGnubrI2qyZJVsAmo5TIr4H1iisaf-1ECwLlTi1o6uFduvMAV5l3KqysaEt2kONB3pF3l_-EKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چرا صفویه به این کتاب «روضه الشهدا» اینقدر بها داد؟؟  ایران کشوری است که عمدتا در جغرافیای گرم و خشک واقع شده،  قحطی‌ها بسیار زیاد بود، فقر گسترده بود، جنگ و ناامنی بسیار! صفویه با گسترش شدید مناسک‌هایی مثل سوگواری  برای محرم و قمه‌زنی و گریه‌های شدید و…..…</div>
<div class="tg-footer">👁️ 6.13K · <a href="https://t.me/farahmand_alipour/5834" target="_blank">📅 10:48 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5833">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B-6p8jGj_erqIzymuNNH7CqkXx7WFj5Q67dTmM0GBCBTeKO2JR06nEfkRn9O--Fj-ljU-O-lSSsZBWprk3mezHBDePIVi6ZjUF3FZURIId_wEl9OlAYkOpwlELJFhxj4DgcLBTxFZrFoOlFTdV4VSGqmuYJ0tj1Wx54wQ-ALKBxgXghOtmRcN-gvflFwaXBQRoihdZHMEZEEmZVsOiI8TqnmgyXs_L89XSsfht6uupp8xnV-1Iw5xVqdMeBTBmYb6za4XWJr5VUiSDnX9nfo4nHs82iiRl17m8SqKxXsUqbeAqTY3PETy5hS2adcg-GXXnROgf4GmPAdS_AWJqIHtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خود خامنه‌ای هم در اسفند ۸۴  یک سخنرانی در جمع روحانیون در آستانه محرم داشته و گفته که باید روی  «گریه» و «احساسات» و «عواطف» کار کرد!  و امر میکنه به «گریاندن»!  چون روی همین احساساته که به قول خامنه‌ای فضایی ایجاد میشه که بتوان خیلی از سیاست‌ها رو پیش برد!…</div>
<div class="tg-footer">👁️ 6.15K · <a href="https://t.me/farahmand_alipour/5833" target="_blank">📅 10:42 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5831">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VZKiyY-aTp0qDEKrp6Yrrqa54CWEEkg5V7dIZrjj1SRcHW-wGLJ9xc9Nz3dP3nVQw9r3RH68-cRAaIg-ffBOPlUwaftTKPrTf0r3o5KurJrpTOCc4LOBslM5TKEz7XbKDZJv1FeI4oaTTf5JfLNDGtQ-XjMI5g7VmBjOsI37QepOpewMYYgfwIz6HdwIasc8nyqHBHrypuSS7IbalJdUWBwmI2Dd18MMGr5Vvb1q6k_SsGw5-wGuEXJT0OA131dZ1haGl7dyMrFf-eh37JwXLCOEE-ddBazRIvzf99d0X0D3ims1q_VAJDVh7SMPfrmr5xJmXe9DDHHhaivLJNYdIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KJyICSScG8w5gh4zHFUwgeBMPU78Ocf3sPu_Oy7a8kmg8xJq_CVlElx0QDixCzfbNFcCHHRKMJeWxK7-Ptinzu0Z2PRp4NxiOhZj_BSQT3nrRxm3BmiD2Vj8liPfNH8SrTExP_t-muWmu05ULgg2aoXohpu69PLaN7x0A6Katy8_aaiEEVtoMMksasWxOp42smVKf23pScPC9Nj_jUr8veXI3ed010P1PZcn-4oahzw_A6PVdXi3bhiKbx-vvqpWhrQer58M_uV21OI99eedtM3x_Qwz-6mVoF3hSep2OWpM31ovvP33L3NPhPcNTgvZj83-vsb62VPnGxtpWbCgiA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">نکته دیگه اینکه خود صفویان،  از فرقه صوفیان خانقاه اردبیل بودن که در این فرقه یک «مرشد» داشتند که قزلباش‌ها، باید با «شور و احساسات بالا»  نسبت به مرشد حرف شنوی داشته باشن و اطاعت و‌ پیروی می‌کردن!   این کتاب «روضه الشهدا» برای صفویه خیلی خوب بود، چون شور…</div>
<div class="tg-footer">👁️ 6.22K · <a href="https://t.me/farahmand_alipour/5831" target="_blank">📅 10:38 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5830">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EtohJesNZbSJmgFGg6BfdC2n4_8K8nNkEX_hgtwNsihYrqRbio9pkVAiC5zX-fNZJB6hC2vrooeuXqAFd9L8M8qt3mimgp-llY3SKQ_gUNOySYYAFEIcAyIqRp5zOkurtHiCnzLrq7erwAb41Kd_v-kyLSXTalerTCZ8lTyNEYuIkYTt6Nv_LOKZu8S_PV8KD6WUspY3yTLdP0gMx48LVXAGs1R-yRX3hnlN4Ey1Pi17aGlfGpCV8DHAW1fhGVXWvL4yhm_s-q9Bo022yCFvmJQAUvNNUw7yB-5rdVxHucLu5WcSQ6HW2XUlQGr0YHsT-CU8DZ4Jqws2Mkggb_pSvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چرا صفویه به این کتاب «روضه الشهدا» اینقدر بها داد؟؟  ایران کشوری است که عمدتا در جغرافیای گرم و خشک واقع شده،  قحطی‌ها بسیار زیاد بود، فقر گسترده بود، جنگ و ناامنی بسیار! صفویه با گسترش شدید مناسک‌هایی مثل سوگواری  برای محرم و قمه‌زنی و گریه‌های شدید و…..…</div>
<div class="tg-footer">👁️ 7.1K · <a href="https://t.me/farahmand_alipour/5830" target="_blank">📅 10:17 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5829">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CNTYxJ77ojeY7zQleopB_UcHLTvcFvN1qfGY2PASFcLVRp3SWs8BdFg4uEIH4F0s0x62vRuQq-TP68L1HvP15RPtIE07aWBI0w2gVXUiZG6CZCorqqIYkviaXKLkaQPU1cjKwL6ipRgexiYl5u2RmKLIRKePqAJN1s0Lc6G9mFzqCw_TE6yMFmqshVj0oub7iVMUGYt7hvFvoYazDI8t89eCdzc1k2hTzp6qy4U257xUNnqofz5pmmmLGUw8YGc_ZkMbSwg2TTMv31ctymPn_HAniifMH-keA-WqYf6Lpm_7Sdwzvs11bnDKjP9YVvczXNVLhH1M_dx7FF9xpsbOGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای با الگو گرفتن از صفویه و با پول نفت.  این خرافات رو تشدید هم کرد!  به «مداحی» و «مداحان» پر و بال داد!  بودجه‌های سنگین! تبلیغات گسترده از طریق رسانه‌ها از جمله صدا و سیما،  که این‌ مداحان با خوندن همین دروغ‌ها! احساسات رو به نفع حکومت مصادره کنن!…</div>
<div class="tg-footer">👁️ 7.29K · <a href="https://t.me/farahmand_alipour/5829" target="_blank">📅 10:06 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5828">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QfvVUcn0nncvG0HoZzOuLrTxwkAP-ZoM3mdCktSzHWlwyiI00K6qwEpvDhrq6E-ejROreuxedUXZYNl-3Q_7-ChSUyb9rRsdxmgtV2hr9bEnPjw1kCdYufWBKc14DerjipadA1PgSzwAf3AQBhQoq_0EOCBAkCaIQ74LEmKFaMSiW9KapYXbGx6RI5vqSML1eEgBnTr5SB5Wnc8YYqed4PU9CSev6SCLyu0ztjxOW6aX9ouXRisxhx3YLZxkcZ1QnFNiDV6DcihXbCWrkc3SIcjUModRWVoTEqMqUQ8rgt7eNFv4AzjqW9GFcoXMUGT_uEF4jaWJTbVddu7AP1x_Ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مرتضی مطهری در یک سخنرانی عمومی  کل این کتاب و داستان‌هاش رو «دروغ»  و افسانه خوند!  گفته از خودش نوشته شده!  کتابی که داستان‌هاش صدها ساله در ایران خونده میشه و براش گریه میکنن!!  کتابی که حکومت خرافه‌پرور صفوی عامدانه ترویجش کرد بین ایرانیان!  مرتضی مطهری…</div>
<div class="tg-footer">👁️ 7.81K · <a href="https://t.me/farahmand_alipour/5828" target="_blank">📅 09:56 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5827">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">در زمان صفویه کتابی منتشر شد  به نام «روضه الشهدا»  توسط «حسین واعظ کاشفی»  این کتاب عملا مبدا روضه خوانی  و ذکر مصیبت در ایران شد.  و اصطلاح «روضه» ، که امروزه برای ذکر مصیبت و گریه به کار میره (در حالی که اصل معنای واژه، به معنای بهشته)  برگرفته از همین…</div>
<div class="tg-footer">👁️ 8.64K · <a href="https://t.me/farahmand_alipour/5827" target="_blank">📅 09:41 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5826">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mFRJOLf7yUOZDG6O2-P9-XbuNcHV40g_NRT1u0ocoZ1qR3iadf3re8NBpxnniuPm4phQ2q2E4-AotiwJ73YEo0xq1eB8OTnIU12vsJAertDdXHmEBa5kBD6uIjzZ52yOwmXZ6Gm7Stv93GSIPa4GXuIYgKkeHW3-ag3M5B-9njyewMRFP7ghkqG0jSDyXnHQZaT-Z-v67o-ml3bN_KP0z7TSYklkT9lsocmKMMAIk8IH5BWaZcajNDWd1syMML4wC0hDIRsiEFUQmh9MCWlnJjQLz77eUId9r6B4YEAzHNcaR6-C6hFJmKtZR4ExHF4i8SdknRts-a7My4a-3MZuhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در زمان صفویه کتابی منتشر شد
به نام «روضه الشهدا»
توسط «حسین واعظ کاشفی»
این کتاب عملا مبدا روضه خوانی
و ذکر مصیبت در ایران شد.
و اصطلاح «روضه» ، که امروزه برای ذکر مصیبت و گریه به کار میره (در حالی که اصل معنای واژه، به معنای بهشته)
برگرفته از همین کتابه!
حکومت صفویه خوندن این کتاب در همه مساجد و تکایا و….. گسترش داد.
بحث حدود ۴۰۰ سال پیشه.
(کتاب دو سال قبل از به قدرت رسیدن
شاه اسماعیل صفوی نوشته شده بود،
صفویه اون رو گسترش داد)</div>
<div class="tg-footer">👁️ 8.76K · <a href="https://t.me/farahmand_alipour/5826" target="_blank">📅 09:33 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5825">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e54b01c817.mp4?token=EUkl6ZftdcjVAYUPk6zo5BlTUuUNZpkql8lv7lyL9vWuDHjgo36BUoBkJ8n0vF7G5iGemZO1xOfcUtFEKpE66PqNEgkAUjunbg27Uhpmitk-ExQKrRdqwkL4H6SNkiauzYUMcyAoZ5msdi7khcZFGagbww0PBPQQpmGwJbmZdOZcJ1A5DRBGzK9DeYKUbtQCxU4u2l5tSO-NBBqdYJFW6OhHUxrvyPKhrC-YNfSXTqO7ljHjRSgwjv3nEEaI4Nqoj_RYZbwfQOgMsMqk1k3Ik2elJliisby7wE6yXRsSORGgsptp6qow6MQ75h7smGXS4ZU66sdglxdNZ_A7VbIv5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e54b01c817.mp4?token=EUkl6ZftdcjVAYUPk6zo5BlTUuUNZpkql8lv7lyL9vWuDHjgo36BUoBkJ8n0vF7G5iGemZO1xOfcUtFEKpE66PqNEgkAUjunbg27Uhpmitk-ExQKrRdqwkL4H6SNkiauzYUMcyAoZ5msdi7khcZFGagbww0PBPQQpmGwJbmZdOZcJ1A5DRBGzK9DeYKUbtQCxU4u2l5tSO-NBBqdYJFW6OhHUxrvyPKhrC-YNfSXTqO7ljHjRSgwjv3nEEaI4Nqoj_RYZbwfQOgMsMqk1k3Ik2elJliisby7wE6yXRsSORGgsptp6qow6MQ75h7smGXS4ZU66sdglxdNZ_A7VbIv5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">روضه خوانی سحر امامی در شبکه خبر</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/farahmand_alipour/5825" target="_blank">📅 09:09 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5824">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/43703b5179.mp4?token=nJIojmQXwvhDlyNAcV0qRwjUwwNjXVCQfVBg6AKqn1IQogoaHs5iIn5Z4Z5UoOo1nTfcW6R0ZPdu0BRGFcWyrwSuqzrKqc-8_bnWaFLbXtBADrW-26qv35K2X0eDkWQPTLAq_B_YRFXiBNYZefnXX6-K2uBY3hk9xqImUxULcDPOoCBv8yuzevVU95BHkPveR1EIjNk9sSizqBvcWnqtS9wb_3wPtLKYgpUU0tFd8YCXlqmMS2ETBjALrYzJKU2mQEV_GFDW-rocRAdmsFL139ruNi9T5RDphFA3SKFkczRCC0JaEmRXrB2txaNRZKAUpKxpINqvjvG2LqGjAO3Q-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/43703b5179.mp4?token=nJIojmQXwvhDlyNAcV0qRwjUwwNjXVCQfVBg6AKqn1IQogoaHs5iIn5Z4Z5UoOo1nTfcW6R0ZPdu0BRGFcWyrwSuqzrKqc-8_bnWaFLbXtBADrW-26qv35K2X0eDkWQPTLAq_B_YRFXiBNYZefnXX6-K2uBY3hk9xqImUxULcDPOoCBv8yuzevVU95BHkPveR1EIjNk9sSizqBvcWnqtS9wb_3wPtLKYgpUU0tFd8YCXlqmMS2ETBjALrYzJKU2mQEV_GFDW-rocRAdmsFL139ruNi9T5RDphFA3SKFkczRCC0JaEmRXrB2txaNRZKAUpKxpINqvjvG2LqGjAO3Q-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farahmand_alipour/5824" target="_blank">📅 08:27 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5823">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d536abe797.mp4?token=CGJ2IYAY_HuuP9opo2RDZmPfUK9IrLdV6HJGrjMspqp_xVLj7ljyzwUtmifagjtJQJub3wJeo3p-MFm2C-RtYrESu8AHUOXZ9ObtxlwmmYIn6_vziXgCoSmCo5RH4VB8-J3a3IbRThW8KE-c4PK3IkBpHaqSowFE0tsfeLKTwL30doDT25wFFi1CJnbeoG6Ws1YF1YHXZMEHzRLWfLUFCQ-8ZxWjOAeeyVTPfupZBu8I9YLqMfcic2pSaQxsBQEk25g6nD6M1cqifVDlfYkOoVor4j2e1l6uS5O5s8QyY0Y3nE2737miUQnQMpTvTJm4wpKO6wiQAnpRunmLtKDHNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d536abe797.mp4?token=CGJ2IYAY_HuuP9opo2RDZmPfUK9IrLdV6HJGrjMspqp_xVLj7ljyzwUtmifagjtJQJub3wJeo3p-MFm2C-RtYrESu8AHUOXZ9ObtxlwmmYIn6_vziXgCoSmCo5RH4VB8-J3a3IbRThW8KE-c4PK3IkBpHaqSowFE0tsfeLKTwL30doDT25wFFi1CJnbeoG6Ws1YF1YHXZMEHzRLWfLUFCQ-8ZxWjOAeeyVTPfupZBu8I9YLqMfcic2pSaQxsBQEk25g6nD6M1cqifVDlfYkOoVor4j2e1l6uS5O5s8QyY0Y3nE2737miUQnQMpTvTJm4wpKO6wiQAnpRunmLtKDHNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هم‌ سوال کننده، هم‌ این خانم مصری
برای مثال زدن از کشورهای افراطی
و عقب افتاده اسلامی از «ایران،
افغانستان و پاکستان» مثال میزنن.
حاصل هم دستی آخوندهای شیعه و چپ‌های ضد غرب برای ایران.</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/farahmand_alipour/5823" target="_blank">📅 22:52 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5822">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad33cb95d6.mp4?token=fJmyzrsMTEmfYg_rMFPn0Ixn8MTnBtAu658X_H3B2GgjFg1-z26rZdrknyz52DkUrTn5TN-fK20rdloKGq4Ohh7UNt4StDLaeZ9_GU36Waig4_lBAvuS7I6GviSBcmb4KWJiQepjpV9dhLLIgkTulpugjVunI2_6SSFsH7fYaofSRIoszhxrTO-dfW4gXUSFU0PudgFxJokIqBp_Brof6wpOjFQ-rLMXOlo4OHAS8fwo53mACjK8ibfUz0PxxOe4h_mquukU8liulEiGtUEkxzU6uQQBP4z4SpYqDD_JqQXrUOmS7GGsVd_hUMZLFKG9W6wPAPUcvzFifND9Ot1fig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad33cb95d6.mp4?token=fJmyzrsMTEmfYg_rMFPn0Ixn8MTnBtAu658X_H3B2GgjFg1-z26rZdrknyz52DkUrTn5TN-fK20rdloKGq4Ohh7UNt4StDLaeZ9_GU36Waig4_lBAvuS7I6GviSBcmb4KWJiQepjpV9dhLLIgkTulpugjVunI2_6SSFsH7fYaofSRIoszhxrTO-dfW4gXUSFU0PudgFxJokIqBp_Brof6wpOjFQ-rLMXOlo4OHAS8fwo53mACjK8ibfUz0PxxOe4h_mquukU8liulEiGtUEkxzU6uQQBP4z4SpYqDD_JqQXrUOmS7GGsVd_hUMZLFKG9W6wPAPUcvzFifND9Ot1fig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حرف راست رو از این خانم بشنوید که میگه بعد از انتشار خبر کشته شدن خامنه‌ای مردم در‌کوچه و خیابان‌های تهران کل میکشیدن و‌ دست می‌زدن.</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/farahmand_alipour/5822" target="_blank">📅 21:52 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5821">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a22e78d39b.mp4?token=FarxS6zgpjZbJtdjVKsI9PYgizVHgSdHTRQkkHiVO1uiiEyFskU0N-Rdx88iIw6GUtGQumGrL86zi7yK7WO4CaVsDDnRWOejKWDSfJOHFxXQy0Vpd895tyP7mTGh261_3VJqYcznM_vEvUM2O63enKKqRBAlMiw4E8IyPQaJFY_HAvTu6vwDCB2vtY71JarmLXp3l32UoGp--hQWkEugyvx8_-kt3OJCz66VJmyCy0KkKt9X_Temnh3m4uuG1ALOTT3xV4Xhek2MMrZQvTue_PR-Iu6Y6V13t_21kNlw2bJIDOZln7eTOaejovHSZ9dboFgBQ_Pi5ylN81kygCjqJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a22e78d39b.mp4?token=FarxS6zgpjZbJtdjVKsI9PYgizVHgSdHTRQkkHiVO1uiiEyFskU0N-Rdx88iIw6GUtGQumGrL86zi7yK7WO4CaVsDDnRWOejKWDSfJOHFxXQy0Vpd895tyP7mTGh261_3VJqYcznM_vEvUM2O63enKKqRBAlMiw4E8IyPQaJFY_HAvTu6vwDCB2vtY71JarmLXp3l32UoGp--hQWkEugyvx8_-kt3OJCz66VJmyCy0KkKt9X_Temnh3m4uuG1ALOTT3xV4Xhek2MMrZQvTue_PR-Iu6Y6V13t_21kNlw2bJIDOZln7eTOaejovHSZ9dboFgBQ_Pi5ylN81kygCjqJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">میگه خامنه‌ای وقتی کشته شد امتش ریختن توی خیابون بر سر و صورت میزدن  ولی دروغ میگه :)</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/farahmand_alipour/5821" target="_blank">📅 21:52 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5820">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/256cc521e9.mp4?token=HHocNLqPVi8CabV33iE6qhkEZcdwdKu8xOzgj0sVNWNYQkEMxHTzZOEPjFtB8R6zgrNwrwDlzKCG8731c9pDP63fwsZXXIp54ql2u3ZJbmL2uR9sPVmQZgWhmgsCpASl4OO-umJRWXN5X9rXHo8y4YvagG3EmuuDoXHBXCUpEbB2mPeiwqGAGggKEHMkiH_SXjx_66574fxQZu8-BW08s4GykFLy_cQR-ZZkAeA1aMkfDxU4ujz0fh804VtZkOEO7uJTa82bVKxlqh68X8VnBXnZWCPW4O9WBjmRUgs2R58W14qz3WiT3sHHJbfuSfNcKGSG4XpPMLizpi3_tNsZDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/256cc521e9.mp4?token=HHocNLqPVi8CabV33iE6qhkEZcdwdKu8xOzgj0sVNWNYQkEMxHTzZOEPjFtB8R6zgrNwrwDlzKCG8731c9pDP63fwsZXXIp54ql2u3ZJbmL2uR9sPVmQZgWhmgsCpASl4OO-umJRWXN5X9rXHo8y4YvagG3EmuuDoXHBXCUpEbB2mPeiwqGAGggKEHMkiH_SXjx_66574fxQZu8-BW08s4GykFLy_cQR-ZZkAeA1aMkfDxU4ujz0fh804VtZkOEO7uJTa82bVKxlqh68X8VnBXnZWCPW4O9WBjmRUgs2R58W14qz3WiT3sHHJbfuSfNcKGSG4XpPMLizpi3_tNsZDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">میگه خامنه‌ای وقتی کشته شد امتش ریختن توی خیابون بر سر و صورت میزدن
ولی دروغ میگه :)</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/farahmand_alipour/5820" target="_blank">📅 21:50 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5819">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ed6be978db.mp4?token=Mq-bcTPjzoOviHrwKgqre8iZP98zVqAL62SUwcn-4ZgIjvIvNF_AqmNTnuGoWVoSBhzjB3ulInQekp4DaJ7hExKFGXCIie35TO9LNsm638VY1QKI8y0f88JnHCUoju-gegeoo6UYwd_BcW95gXmxFRwAwtpBTzTZEKlfMBSBipjBNMaOysJ5jGQnV7TbtnHNaJ_Y8wy0uQTK6RNKzruuyLI28bDqjMBr8mCHFVjBaWcdQMxnlJjXRxKhDyfCWd125FU19T32etbiKAldPXKFiY10OXNmAAMw9DYTHcBQMSrTF-l0V4rbsVw_yZeWGNCaJxX5OnVkZJzyRn6PgSJEWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ed6be978db.mp4?token=Mq-bcTPjzoOviHrwKgqre8iZP98zVqAL62SUwcn-4ZgIjvIvNF_AqmNTnuGoWVoSBhzjB3ulInQekp4DaJ7hExKFGXCIie35TO9LNsm638VY1QKI8y0f88JnHCUoju-gegeoo6UYwd_BcW95gXmxFRwAwtpBTzTZEKlfMBSBipjBNMaOysJ5jGQnV7TbtnHNaJ_Y8wy0uQTK6RNKzruuyLI28bDqjMBr8mCHFVjBaWcdQMxnlJjXRxKhDyfCWd125FU19T32etbiKAldPXKFiY10OXNmAAMw9DYTHcBQMSrTF-l0V4rbsVw_yZeWGNCaJxX5OnVkZJzyRn6PgSJEWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به امید شکست و تحقیر یک به یکتون!</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/farahmand_alipour/5819" target="_blank">📅 20:05 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5818">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pialK1hk9HI2hstF9Bak8n6E24Whj9d9TY9oqsM3ZlOChJO8T5JClSiGEx8sM0ZbkgaSwZBljwne77_rkVaL6PG5maf9dsvVkCtEQFGzZxJRNExnNymIeaWCEGUxXjWjilHElaLgnKLYUeomOau7iUIkkYQG33exnYnW1j8rs0ps684fIcLFqje48DeOMgmFnN6HJtS-wXS2EjFto_rl5NEyOypP3nuWUE7GT9p_onMyz6SklOvuaBO1zmnlFqM6GJB5147mvItjtD2nJ367wB3yXDM9JirmJ-Zxo5B_IULXWHik0eA545yCEjx9aX-O4MD9uTuJBqDbjdBNzZVm3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/5818" target="_blank">📅 17:21 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5817">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7862dff401.mp4?token=uM5ZU1dLXBaDc7vcDrW2e_wuanDsWlVoKBe4NahKBWDAejduDkwsTsIqihRAGfhp7WaFYEqiMkvP04ju6XneDjGPpNzcz_fI5rD9lCubl9d2Jdac-9JMH9-614SJM04aZVq2wXfbrj_zjddo9QUPV8HrkY4wOWyvUn73RDxumOtT_yXskLT71jPXx81Rey9KHAjYs8GVKmZ8nYp_AKYfrrSy7AN-MwrxWp7uskm_Gxot5nYh6upzSI95ymwGuFCi91ht0SHFRmX_6pX71qhV6mcC21iLGdV_hqnZ8QutXMESneokbpnsDAsxj4088tQkSNbeykR-rtn4Fhy-DSY0rA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7862dff401.mp4?token=uM5ZU1dLXBaDc7vcDrW2e_wuanDsWlVoKBe4NahKBWDAejduDkwsTsIqihRAGfhp7WaFYEqiMkvP04ju6XneDjGPpNzcz_fI5rD9lCubl9d2Jdac-9JMH9-614SJM04aZVq2wXfbrj_zjddo9QUPV8HrkY4wOWyvUn73RDxumOtT_yXskLT71jPXx81Rey9KHAjYs8GVKmZ8nYp_AKYfrrSy7AN-MwrxWp7uskm_Gxot5nYh6upzSI95ymwGuFCi91ht0SHFRmX_6pX71qhV6mcC21iLGdV_hqnZ8QutXMESneokbpnsDAsxj4088tQkSNbeykR-rtn4Fhy-DSY0rA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جی‌دی‌ونس میگه ترامپ میخواد با این تفاهم‌نامه با جمهوری اسلامی،  بازارها و مخازن رو از نفت پر کنه،  و بازار سهام و اقتصاد رو درست کنه بعد تصمیم بگیره با ج‌ا چه کنه.</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farahmand_alipour/5817" target="_blank">📅 16:36 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5816">
<div class="tg-post-header">📌 پیام #83</div>
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
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/5816" target="_blank">📅 16:31 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5815">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🚨
نتانیاهو : اگه نیاز باشه به تنهایی و برای سومین بار به جمهوری اسلامی حمله خواهیم کرد.</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/5815" target="_blank">📅 00:04 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5814">
<div class="tg-post-header">📌 پیام #81</div>
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
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/5814" target="_blank">📅 17:59 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5813">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6a28a5f6ff.mp4?token=quHtPA44pIewOtkRpmA_U8ZcSdobzLQf_8A1wLRXPVVKracOCitdt52I9N3AkXiqL2VVOOl84Wqhw50wy31cTP2yU-9p_TG1u9jOQMPrCJZz8Pqkga9SzyQ4gTfagc31UQnjgpYmPD-YD5c7_yn56xM9p1Z0EYwKychX5EfMrn-2RQLby6i2I5A2OKSrZ_aSC8I0UsXP42uqJmr2A0Iz5j-fN7lBt1ge-tXXvlbtojACjHkHyB0kX0mbw5LKAxuxLMbvUEBSyIXzEMyEkduCR8Psy5KMO7JeeKIRXH24uImiSn2IOaezzHFpp1WPIi6OJjOs8wkkMs9oTZSDvmWhdg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a28a5f6ff.mp4?token=quHtPA44pIewOtkRpmA_U8ZcSdobzLQf_8A1wLRXPVVKracOCitdt52I9N3AkXiqL2VVOOl84Wqhw50wy31cTP2yU-9p_TG1u9jOQMPrCJZz8Pqkga9SzyQ4gTfagc31UQnjgpYmPD-YD5c7_yn56xM9p1Z0EYwKychX5EfMrn-2RQLby6i2I5A2OKSrZ_aSC8I0UsXP42uqJmr2A0Iz5j-fN7lBt1ge-tXXvlbtojACjHkHyB0kX0mbw5LKAxuxLMbvUEBSyIXzEMyEkduCR8Psy5KMO7JeeKIRXH24uImiSn2IOaezzHFpp1WPIi6OJjOs8wkkMs9oTZSDvmWhdg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5813" target="_blank">📅 17:53 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5812">
<div class="tg-post-header">📌 پیام #79</div>
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
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/5812" target="_blank">📅 14:57 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5810">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/o8BgFXvKrE_n15rLczZJBDkY8IybRYVtwIfBt3duyJmhv5yvzlY6AksgRpcWiIehYTsvsmewEEHIhZDcLsTyM2aF9HyKNnv8FwhfOHnkh2cdO7KSVDpN0QpHEB_9jYVY2Pz3GKay1kEiT-cHV_H6JLmtt6BeQuytPfQqguyCwcQGJPQPTc7GwbPt8N5GNntHA8mbctoBGYDNrxXPmjlmzWf032KiCVObaNDX7lZFXXYSO8mUU4mDvWKiyRxLArwwaWQBktsNb6ZGNO53w35PPdRyFKJ3JbY349-lfQUVbvjJBpHyvBl3OSsLdSIkDKMTcEoUDNZJc24zbv7ULHBLRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Cu6f1emJ8tbReqOm-hZEcVPG8O22UgS0TKAsA9LsVSKNc_D6BiaecEQIm72Z6lpZFB3qQYR29VSE96AkAv32SgYJnhJRvhvI5lHTifZXTX4agygYtmyOgF_1HfZNogzleNFcn62jt42UmsokoJpiwPVZlGafMgA6-oV8Pyhex0i-Ss2YrAzBJfq1lnJRZW7b6k0JiLN1jKgubKFaSBmwlOcqzVSunul2esMc6eT7j2iTaQ1fDG6oceMzTxDtiMpZIAD0GiN9wltPG0l9rGN1AVpWFD85w6HBt3pXCXcSSRjct8RvKjhpGvyjAlSI89vXAspzpIAF-HOj1aFkvRC1Ow.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ده‌ها تن‌ از‌ سران و مقامات عراقی بازداشت شدند. از خونه‌هاشون میلیاردها دلار پول نفت و طلا  پیدا شده!
خیلی هاشون از نزدیکان جمهوری اسلامی هستن.
با تصویر خامنه‌ای و سلیمانی و سیستانی در خونه‌هاشون و سوتین و شرت طلا!</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/5810" target="_blank">📅 13:32 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5809">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee0be552a1.mp4?token=ElbniBNdOapi2JslyNr19f98QXVYVfGYArQoo8KEA1D9832k0LXZLMW7TO8ZYoST9k5WkhXsFul-aoeGNMyLebOExnocGsHG0LPo7u1SKtoESDSTLK1IpHsVNxB64ga4K2cmHr-nrd9ZeD4-mzLMozw8KfSEFcIfIl_hc_ExO0H8XQGWx39-tKQ8olwhvrvRc3DryJhNGYcwakErtRpayWmvTsOZg8XBE6Old3S8pqkj6dbjLQ7QPgEPSegHc5Zw-tyAtbqiDGSjLjcwxjlyCrm3a23AiH8yLq1Uy0v7_z5N4zR6cm4jq_txp2J5dgIA4CTJbtZk_q444RhH-SuSh4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee0be552a1.mp4?token=ElbniBNdOapi2JslyNr19f98QXVYVfGYArQoo8KEA1D9832k0LXZLMW7TO8ZYoST9k5WkhXsFul-aoeGNMyLebOExnocGsHG0LPo7u1SKtoESDSTLK1IpHsVNxB64ga4K2cmHr-nrd9ZeD4-mzLMozw8KfSEFcIfIl_hc_ExO0H8XQGWx39-tKQ8olwhvrvRc3DryJhNGYcwakErtRpayWmvTsOZg8XBE6Old3S8pqkj6dbjLQ7QPgEPSegHc5Zw-tyAtbqiDGSjLjcwxjlyCrm3a23AiH8yLq1Uy0v7_z5N4zR6cm4jq_txp2J5dgIA4CTJbtZk_q444RhH-SuSh4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بیش از این‌ها تحقیر بشید !
چه در ایران، چه  در لبنان، چه در فلسطین،
چه  در دریا ، چه  در آسمون!
در ضمن بهتون دینار و درهم نمیدن!
قراره یونجه بهتون بدن و پولش رو هم بگیرن!</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/farahmand_alipour/5809" target="_blank">📅 12:55 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5808">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gtAWp1ubK0MdV7BFgSvtnZjue2Z30AGR4EyWmzE4H96fpfG_IJYBavmnhKmd4tERyl2DEjR9xrWifYJGhYLB6jKF6rgTChaaaqFeh1SCltLDWAwEg75MEQZ5b8HKLE-Us5ai6jfjGRl938MykUhjobtpflRbK1Mknyxkn0LCbjFYGf5YRPARXFmE4PMCXwzPrtPzxMbp7emjPTuK4SGcawpqxDyecQ_JkOcEGHkcK7z12cNVKG1pOXU6y2W0551yPo11RVtr9d6U_aWpgv3_Xe5i6VwFKXv37zEjqtdntoJLkLTCClUfdarrgFHtEwhvXaW3aDwhhqH0niPg2wPtzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقبره رهبر مستضعفین! که در زمان حکومت خامنه‌ایِ ساده زیست! ساخته شد،  با مقبره فرعون‌های ظالم!  که به قیمت و نرخ امروزه، مقبره خمینی ۲ برابر مقبره‌های فرعون هزینه برده!  ولی عرزشی که نمی‌فهمه! بهش میگن رهبرت ساده زیسته خیار نمیخورده، خوشحال میشه! دیگه بقیه‌اش…</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/farahmand_alipour/5808" target="_blank">📅 12:47 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5806">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AmaYBxK2mwlB8b5yd5uOfOs0wYCGX68F7VPGdwXf1D-Okle-nYEKmjMHLi8VdzsJLQJouxIGkSpzXJsHt6NYXOipDeOcvBKu_1ey4ciEJdKyjUfQWoMlIOlBLua4FLfVbY1wZohsrgqUiUR_89QxcHdDr9rf5D9_vGgRFEd83j3tHc6dGC0_-B9czgVd0GPDCWdJaNxrqXW5t19zU3EYIzbc6QkZNxStZNs69cN86T56HTU63ON87-McR1U0R1Zh4Dy25bJcDVFyYeIeyHaoR6HEGZeT4tCmyZ9F7fpPSi1u6WOXX81zehUFIaXBfjyjRQroRw9v-r1xrWQsGkqyEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nEKkh-Ri_5_bXMGGrzItgmdY8zKc8oAjve6XVW9PtSyDzKI7s3-kegVuSD8K6Iv7GxYoeva_zlKyit0aCMOSBRYcbO-HYXRtHDbYervJdIhjkKlNyN7K6hOiQCpK3Vpqy7peo2G6v5SUfCadxuh9r0OCuy6vSQ3LEe_7ZgVMq-LmWm0BXie_TfGt_zzl0HXdkwAIXr3Rz9GhsV9bii-Mp7WdR8EwWo6S5ItUwa_UIrG9fyHutAi0BCaUvMVFPxrA1lHYRGHL26ACvDDPoljGrwsMRewV0ecv4wBoZhW3TprtMPfCRiDn3nkXrssiGG3KnwFLlq4rby2WhEMRT5Mezg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">هزینه هر روز تعطیلی تهران،  ۲۴۰۰ میلیارد تومن خسارت به اقتصاد کشوره!  اینها فقط ۳ روز برای خامنه‌ای تعطیلش کردن! یعنی فقط این تعطیلات ۷۲۰۰ میلیارد تومن خسارت به اقتصاد میزنه!  این فقط یک قلم از این هزینه هاست!!  ولی خب رهبرشون «ساده زیسته»!  خیار و هندونه…</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/farahmand_alipour/5806" target="_blank">📅 12:35 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5805">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f9VRPhULi4doFD2Oc5WJurTv01NfdTqVEjNuq-4ToR9pE2Ebv0DyZSclODtn0PEUnnXljtGOTgRx5iGc8yzn2zHRYwu8EEhSFzqUJX0WxneJJmMwCtsipjb4kwOnAh2G1cdHPZ3DfajWJ_8UwMbapcfuj9fRmTahTSqtbt0INgT7-Bc15szqmA4IGSgtKy0QDoeM5IyoWBwiwamnGf79WkHFDOO6sGLIEQvfIJp-gP8hLqHv39bsPKKGlwpPxdn28JyiTjn5Lhz3yAIhOBCsb-n1MLgq7kVfA7oKBzeZTJbBgYkYCKfu_8KWOo0LHC6vKIW6JuWR3ZizAskBcxnaag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هزینه هر روز تعطیلی تهران،
۲۴۰۰ میلیارد تومن خسارت به اقتصاد کشوره!
اینها فقط ۳ روز برای خامنه‌ای تعطیلش کردن! یعنی فقط این تعطیلات ۷۲۰۰ میلیارد تومن خسارت به اقتصاد میزنه!
این فقط یک قلم از این هزینه هاست!!
ولی خب رهبرشون «ساده زیسته»!
خیار و هندونه نمیخورد!</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/farahmand_alipour/5805" target="_blank">📅 12:29 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5804">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b7a3755d2.mp4?token=vzRt7ymobvAebhnN8_Lkn4G8e5FqcUIibg7zeVCy2zDHL847BZ0xv56Kjc6UfyWhZSTbe3CY-U9OW6d0UeSN8WNTbHR1MDBNiD3Dg058hSW_AKHfDN6dtFtcp-FN2t_PiMdPcrH3QegsMSFpjnO40Q8IFGemPSux36LQdzIa3TOEfDQtY93S4z6_mTR5YFzo96EuE0kt-qo5IoHxkrGC0AJK7fcVNdOH9FHxFqsqE-_buPyhEVwMKC1dUsRQ28-e_OwlAo37RetIEkj1pmt0FRnucxm3RI3WBUC_Pd8M0PmsC_-QyRGDU5GP7WrQMl20_1WdanFOuYros-zjizlzhg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b7a3755d2.mp4?token=vzRt7ymobvAebhnN8_Lkn4G8e5FqcUIibg7zeVCy2zDHL847BZ0xv56Kjc6UfyWhZSTbe3CY-U9OW6d0UeSN8WNTbHR1MDBNiD3Dg058hSW_AKHfDN6dtFtcp-FN2t_PiMdPcrH3QegsMSFpjnO40Q8IFGemPSux36LQdzIa3TOEfDQtY93S4z6_mTR5YFzo96EuE0kt-qo5IoHxkrGC0AJK7fcVNdOH9FHxFqsqE-_buPyhEVwMKC1dUsRQ28-e_OwlAo37RetIEkj1pmt0FRnucxm3RI3WBUC_Pd8M0PmsC_-QyRGDU5GP7WrQMl20_1WdanFOuYros-zjizlzhg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">برنامه «زیر آسمان ستارگان سینما»  در شهر بلونیا در ایتالیا  که ۵۰ شب در طول تابستان برگزار می‌شود.   (در عنوان برنامه در استوری اشتباه کلمه سینما جا افتاده بود)</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/5804" target="_blank">📅 11:16 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5800">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf427145cc.mp4?token=kMiyVbMzkx4QDkZFgArq9UWQyI61aoE2W7T44LokPLv0aBqIJQKiPjxGQHnaDhBo-jkdLfgtTWEzaz1rig1A1IKiM_linPWmRjqD3TwHRBWBigAvL_L2N1arRWXkSnjehEb1qGxHWzpYwJLrwPYEs7h-sTZLgze-WjWruUkhyyChdm45c2xFRrOT0LPKd3hEecp72IrYIE5IGeF1sAlxsnYk6XyjLic9LOvXOt2BkCxzbTGNgXbVBhFV0HxU77gAZmTj06wwCjiwlj8u5oAjt9_dCAb77dSrtugayK-6omIFEKtflD9jCu_Rh1RlupYQhpVGKu3mRBT0apd1476KRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf427145cc.mp4?token=kMiyVbMzkx4QDkZFgArq9UWQyI61aoE2W7T44LokPLv0aBqIJQKiPjxGQHnaDhBo-jkdLfgtTWEzaz1rig1A1IKiM_linPWmRjqD3TwHRBWBigAvL_L2N1arRWXkSnjehEb1qGxHWzpYwJLrwPYEs7h-sTZLgze-WjWruUkhyyChdm45c2xFRrOT0LPKd3hEecp72IrYIE5IGeF1sAlxsnYk6XyjLic9LOvXOt2BkCxzbTGNgXbVBhFV0HxU77gAZmTj06wwCjiwlj8u5oAjt9_dCAb77dSrtugayK-6omIFEKtflD9jCu_Rh1RlupYQhpVGKu3mRBT0apd1476KRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">برنامه «زیر آسمان ستارگان سینما»
در شهر بلونیا در ایتالیا
که ۵۰ شب در طول تابستان برگزار می‌شود.
(در عنوان برنامه در استوری اشتباه کلمه سینما جا افتاده بود)</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farahmand_alipour/5800" target="_blank">📅 10:42 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5799">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dIU5sESiscubGZ9MGkVGOGb1W2O3V6d8jIESxM3uL7zkdSWiRX5hasaKJBq68Sca9HrZQL0i-VfKhXd7bFOe7d6LmZKJ1aYlMo_n3Nvvt7-YvkQUI-qMX6WIgIvzyARhLcQBE7Tl9grG_RgwxVtu02qiCngnFECw8aQ7H3EUvIUshsSP4aoL98veOzq501wrowo29SO6b0C_b5-urh2meAW23mZgfX0u1MXSBuUE6KNSMeXt8VNJPTcVgveF5Rv8okVcsVCbccCXIa9VZhfx3qtWEno_4f7fA4-l2KuJ-yAzvX3BNgFoY1UGoHew0ST4qJlrhpE-_woBphVr5NLjHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هرگز به مردم ایران نخواهند گفت!  اما کاملا قابل پیش بینیه که هزینه این مراسم بارها و بارها از هزینه جشن‌های ۲۵۰۰ ساله بیشتر خواهد بود! چندین برابر!  درست مثل راهپیمایی‌های هر ساله اربعینشون که باید از جیب ملت ایران مصرف بشه!  یادآوری : هزینه جشن‌های ۲۵۰۰ ساله،…</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/5799" target="_blank">📅 09:26 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5798">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2dc44e27bf.mp4?token=TIx9GtMF0uM9wBYRfAePFQmWoeeCtNPSvVINpUpTG3mo5AHxBcGHrunZWDL1807IJ1L2Y2cnMsiHta7HP6eeMcV1cWuYt_JNYQ3xTT20JZRjgEo5Vwj5NnGSIjSJ7BI03IAAXDEHoWyn88OclvoI8oKNcXyiBg1xLC9h5qO4mO5LePiQe034pZIxd5t6GJ6F5CQOkz3LRyqhhy3QAINjkmMN2OwQQ0DxNFUh5rN_LswK35gksN0WlRPQrY88-meIuRfg7R1OoOpRmrDrLYE9vgZGNheXPxoKXrEYe5OXMKgNS-FWRHAXtwqGeQM_vPnD2eLN2cgVyx_hRWPLWokZoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2dc44e27bf.mp4?token=TIx9GtMF0uM9wBYRfAePFQmWoeeCtNPSvVINpUpTG3mo5AHxBcGHrunZWDL1807IJ1L2Y2cnMsiHta7HP6eeMcV1cWuYt_JNYQ3xTT20JZRjgEo5Vwj5NnGSIjSJ7BI03IAAXDEHoWyn88OclvoI8oKNcXyiBg1xLC9h5qO4mO5LePiQe034pZIxd5t6GJ6F5CQOkz3LRyqhhy3QAINjkmMN2OwQQ0DxNFUh5rN_LswK35gksN0WlRPQrY88-meIuRfg7R1OoOpRmrDrLYE9vgZGNheXPxoKXrEYe5OXMKgNS-FWRHAXtwqGeQM_vPnD2eLN2cgVyx_hRWPLWokZoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هرگز به مردم ایران نخواهند گفت!
اما کاملا قابل پیش بینیه که هزینه این مراسم بارها و بارها از هزینه جشن‌های ۲۵۰۰ ساله بیشتر خواهد بود! چندین برابر!
درست مثل راهپیمایی‌های هر ساله اربعینشون که باید از جیب ملت ایران مصرف بشه!
یادآوری : هزینه جشن‌های ۲۵۰۰ ساله، به ارز امروز، حدود ۱۲۰ میلیون دلار بود!
هزینه سالانه گروه تروریستی حزب الله لبنان
یک میلیارد دلاره! ۱۰ برابر!</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/5798" target="_blank">📅 09:21 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5797">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d3b713ac56.mp4?token=Bz9sAC3iFQr6pmnD31JcgzJuDxK82c4WjueU0slDw-bsxokjqkiRk1zKFEq7T8kEqKR88VdsOL71IS8fgF18nL6roEQjX5pLeDaASQozrdnwvu4aTAz0r-Wq2czlyTP7h_AxPSQiVh8uun7C4YfQvvi17pF23Jxr5k8CJxL7uSRvkSfRwXAmc0rzCGip88aPxBFrC--STlIhX8Qn5NceYq3sbfwK90BtSKCQ48e7mAdCudbBLWV9IUjq32hUZw1RaTWAC2EiedHZKf90Wjde2AJ00VMk5Inet2dkt2NkCVEKFOaWs6d06VxNx9OBwvJm7QNiGTZ-vdD7jI0t5Dd8WA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d3b713ac56.mp4?token=Bz9sAC3iFQr6pmnD31JcgzJuDxK82c4WjueU0slDw-bsxokjqkiRk1zKFEq7T8kEqKR88VdsOL71IS8fgF18nL6roEQjX5pLeDaASQozrdnwvu4aTAz0r-Wq2czlyTP7h_AxPSQiVh8uun7C4YfQvvi17pF23Jxr5k8CJxL7uSRvkSfRwXAmc0rzCGip88aPxBFrC--STlIhX8Qn5NceYq3sbfwK90BtSKCQ48e7mAdCudbBLWV9IUjq32hUZw1RaTWAC2EiedHZKf90Wjde2AJ00VMk5Inet2dkt2NkCVEKFOaWs6d06VxNx9OBwvJm7QNiGTZ-vdD7jI0t5Dd8WA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لحظه‌ای که «سپهر بابا» ستاره رفیعی را دید.</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/5797" target="_blank">📅 22:28 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5796">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e1e05c8825.mp4?token=SCVxwHcuT6-5JW-H8-D3sVlP8tw7NdOx7P7zI6waKUlqEBvowNB5pK1KHmHlHX9b-vicQry-9sdOfQeT8GSWC08omDJZX41E8-RJcHu0mP0szWS49vAUKoueznVvwiHMGKZa1XUalglFApM00ajs5cQweZDbr7XoQb1MC4XNS5E6Bn3dqhG-7ibT-p6Vik4nnhj4fAWPCudzcFjU-l4KbIkgHe3dLlqhN54fXyMhaVvg8gllZ5n4X7lYZgy8LxxU41zg67IqnIPmQa5AMsrqdgi0Rw4IZnlZqrQNuvOPdvJWxTMiu28BxxCt0eQUF1JANpRgqXQJF2loAyR_Nc1CqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1e05c8825.mp4?token=SCVxwHcuT6-5JW-H8-D3sVlP8tw7NdOx7P7zI6waKUlqEBvowNB5pK1KHmHlHX9b-vicQry-9sdOfQeT8GSWC08omDJZX41E8-RJcHu0mP0szWS49vAUKoueznVvwiHMGKZa1XUalglFApM00ajs5cQweZDbr7XoQb1MC4XNS5E6Bn3dqhG-7ibT-p6Vik4nnhj4fAWPCudzcFjU-l4KbIkgHe3dLlqhN54fXyMhaVvg8gllZ5n4X7lYZgy8LxxU41zg67IqnIPmQa5AMsrqdgi0Rw4IZnlZqrQNuvOPdvJWxTMiu28BxxCt0eQUF1JANpRgqXQJF2loAyR_Nc1CqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تفاهم‌نامه ج‌ا و آمریکا رو به طور نمادین آتش زدند و گفتند که این قرارداد حقارت‌آمیزه که خب این بخش رو درست میگن!</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/5796" target="_blank">📅 18:49 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5795">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PNsPYGZ0qvEJfuL9Z4J5N1VHys0RiZdUrqdWm8bGwSZNU03sND2ojuxXl1sHTTNoWRS6gRYB2ANuYFtB2R-dvRpUCBVr91dGBwZBfNQi-IN2lWDJ4rqXTvJugZR5WrD6g2vxT-cSUB733sBfEFwwBXBO5tDAzi8dmHa2cE244Igp-kcrbCg_X6ezBruOmcHKl1-6KoTf_vxNeMvs1sr7IilNPTp3wABVo1Yz-0kjo0nq35sU8fYP-JMdgR19hWSpQRGpH3E2GUWNm3LN94S3cHESndtySP7r3iccWFPkhRshLdwwHEU2JmsHBj8REOaYQ-m_1UJUAQ2dRnW6mvExeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امروز - دیدار فرمانده سنتکام با رئیس جمهور لبنان،
یادآوری : دولت لبنان چند ماه پیش
حکم اخراج سفیر جمهوری اسلامی رو صادر کرد
و ج‌ا را متهم به تحمیل جنگ علیه لبنان کرد.
مقامات لبنانی و اسرائیلی چند روز پیش هم مذاکراتی داشتن و گفتن مشکل مرزی و ارضی نداریم!
مشکل دولت لبنان و اسرائیل شده گروه تروریستی حزب‌الله لبنان که با پول مردم ایران تغذیه میشن برای جنگ افروزی!
در جنگی گه برای خون‌خواهی خامنه‌ای راه انداختن و فرار کردن، ۴ هزار لبنانی کشته شدند از جمله ۷۰۰ کودک، قالیباف هم به صراحت گفت لبنان ۴ هزار شهید تقدیم جمهوری اسلامی کرده!
لبنان ولی نمیخواد! جمهوری اسلامی به زور یک گروه مسلح رو راه انداخته اونجا!</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/5795" target="_blank">📅 18:44 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5794">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e972609e9.mp4?token=aCuri5eEPFMDQJ1KcNpNZgYEeOzL-WqTKa_UYuiIkHqs-A9sJdhulfR0bWkU_0Mq6Fm5JQwAr6HvK_y5DYmU-KddXpVljuXksVdax-O7hEaZ6Dbun7QKwpVFEIRCuP-76kbj5MYKMvc8jMTtfA9iZB7xZdaYbRmQnw51OxEoypZ5ZW_zqJmUN5nNE6ahgoLaHZ8AwSs6dgxevawEfhfKpH17En5-x98jkK7MbPF_xT69S0MfxsA4EGSYmslI6R5i6Ib-WBLAzKWmrrUff_H8rwsaRp64-qmniv2JR3IYnlj2VKAo-Rm2L9Bwp9_QX31Nl7G3Y2p1ZvIjDyn1XcpcQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e972609e9.mp4?token=aCuri5eEPFMDQJ1KcNpNZgYEeOzL-WqTKa_UYuiIkHqs-A9sJdhulfR0bWkU_0Mq6Fm5JQwAr6HvK_y5DYmU-KddXpVljuXksVdax-O7hEaZ6Dbun7QKwpVFEIRCuP-76kbj5MYKMvc8jMTtfA9iZB7xZdaYbRmQnw51OxEoypZ5ZW_zqJmUN5nNE6ahgoLaHZ8AwSs6dgxevawEfhfKpH17En5-x98jkK7MbPF_xT69S0MfxsA4EGSYmslI6R5i6Ib-WBLAzKWmrrUff_H8rwsaRp64-qmniv2JR3IYnlj2VKAo-Rm2L9Bwp9_QX31Nl7G3Y2p1ZvIjDyn1XcpcQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این شب‌ها، همین‌ها توی هیئت‌ها در حال عزاداری هستن
ده تا مرد مسلح افتادن به جون یک زن معترض ایرانی.</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/5794" target="_blank">📅 18:39 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5793">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QOHj3PUWCJBpm8H428lrOfm4wInDvYOjug4XvdUj6udqFI3KX3n_w3hKdKbgeL-WKTj0dA3XpZtuAKnyfne9Mk-khwNw0whnn4ccCzJDZbXZRfOnhiVAoxeQw-lR7JIxUzd-zUvKLEbxLWa8XiVPOZe19xN1Owzk4E7noJTh8bJk0jCl2RhW3FWcdlQ-o_59T4c86be91rQhqlY5Dv2aPEP0tnYsiswqKKKxikM_TzU7Ozg-eAhGEeVQ_P8-w8O6PdvBC0hMcPfvHQmS9FYx2hM4eJ_bZJuUlE1pVVvNb0EmHqCTgCZZDC97nX1VPEIyc2VnsrpHS-8fAB6ReIOFvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حالا در حد یونجه و ذرت ایراد نداره</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/farahmand_alipour/5793" target="_blank">📅 18:33 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5790">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TErMup8vOeJ2sgxpHY5IaTfVc1GobBVMJl3njhQZhox9i_pzaUowPz7vKw39quuKrhnIEs2dw8ORViPf-VS66UhCGM1k7IjYAEUOaPnCtuLW1BizOObZBCBRL9k4qWq4BrLkhYbQMPRPzUebCadw-pvm3EX6gGdd4HDABZ1BvPW7V-1a_1z5t7iTFsKzQMSoVczIkqY5ViuwXYiqHglr67cuTj3jjxqXidLOYuet7XXQMRMSlAeY4kDTVEwiypw3rMKkLxEdpB4KrCIQM0WazlWqZpbIjqvIErXD_q8gjl4G8Ao6rePDspPasB4PsQ73TT3nX23TpLSe7VXxljl4tA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/651901a9ca.mp4?token=sTMbDCCENWFk28N2CVOd_iN9qmChefG-wXTfyZ0-ZAug_J1GlzJ2iSf-Ri-NdIbML7hZSAofp3uXov6ovUol4Mf8uk9JL9PjbVkHwJ_gW3Pnvp8ZTXwdpgzdkLa92ep9KyhPZn5OCHhUEpJvYIvfuIQUhKJ_PgpgRqAhxsSD9xbPglCxPM7w1VTLkVh2OCOd80wEWgBblrsHLVOBeZkdMm45_r3L8HPureF1xrmFTJ-6ihGxCTKVBjqu9VPNsO7APayr8jfQfvvPRN9sF6BHK1q556uOEgGs5dpDmBfD5MJ459DBWc9pcYiHPOR1b1NnJj0E14grgh0TrxCloYkzWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/651901a9ca.mp4?token=sTMbDCCENWFk28N2CVOd_iN9qmChefG-wXTfyZ0-ZAug_J1GlzJ2iSf-Ri-NdIbML7hZSAofp3uXov6ovUol4Mf8uk9JL9PjbVkHwJ_gW3Pnvp8ZTXwdpgzdkLa92ep9KyhPZn5OCHhUEpJvYIvfuIQUhKJ_PgpgRqAhxsSD9xbPglCxPM7w1VTLkVh2OCOd80wEWgBblrsHLVOBeZkdMm45_r3L8HPureF1xrmFTJ-6ihGxCTKVBjqu9VPNsO7APayr8jfQfvvPRN9sF6BHK1q556uOEgGs5dpDmBfD5MJ459DBWc9pcYiHPOR1b1NnJj0E14grgh0TrxCloYkzWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">«عالیه نصیف جاسم» نماینده پارلمان عراق،
عضو کمیسیون مبارزه با فساد، از نزدیکان جمهوری اسلامی، معروف به مواضع تند علیه فساد در عراق، چند روز پیش میوه نذر امام حسین کرده بود. دیشب در موج دستگیری چهره‌های فاسد اقتصادی توسط دولت عراق دستگیر شد، در خونه‌اش ۱۶ میلیون دلار نقد و مقدار بسیار زیادی طلا کشف شد!</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/5790" target="_blank">📅 18:03 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5789">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">شعارها رو گوش بدید،  اینها اعضای سازمان مجاهدین خلق هستند. خوشحال هستند از صدور حکم اعدام برای «حبیب القانیان» ، توسط خلخالی بدنام!  جمهوری اسلامی اعدام می‌کرد، حذف می‌کرد، مصادره می‌کرد، بقیه  گروه‌های از جمله همین سازمان مجاهدین خلق هم تایید می‌کردن، میگفتن…</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farahmand_alipour/5789" target="_blank">📅 17:05 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5788">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/583cd57ba5.mp4?token=ZlA4FUq-X2sOP7DoSj0pHxLttQqF7tNStUiXN62RDg2NRznFgTe_nKJORQHxxk5uhJThvWHiauT42-3rqXI9nQ55Q2XJv3n_A-BVcl84Eqd6KfQbzFy5WjtpOi4GTDY6LIcXQ0nE_1AjFisXCqscXMr8xXubm7oquy7_oi8UvCRRnimuOZnJ0fmu8BEmbYAJ3cL8XwzXZ57zE7RlcKxdyMAx9NfUOSsHbN7IpMOPTCPpM6lxUDaMwBT0mmHDCpFUO2O7ZrwEN10_YeIFyz2dvaLUhQsN5AKtV6sNfJAAPphM2ujdNrRI_3ElVQHtPtoJQ7PZpZSAKsbtrSkJnaHz0i7daxxfgrK86uRF5Pqgjwz64ZPKuRdXipjW2MpJd2Hi7j8gq1ZDBOe-mvtB322VbXZNIk61d0sBjdYS4e7tHmNvePaePEUKF2Ymysc5Kxd9SN_w5p8f7sS8j2pdkZJDgaPN_sq0BS1NyDJxtkQmHgDp3l6V56MLZaEEd6Bke31zKfNGOQ_ASGFBDldVDb_dB5PpZK7vMxO3_RPFUS5KBqW5gEeVQgMffFkuUWFcznQ0zpUfZxCvNfiuFokC4YsdjG0rKggR7S-SFWLCK81tUbwcBud7FvcLpFGYceQ2sCWtYCukIOnKK3tzWZZMrVFlnWO7XNXe_5-ZWak_Gur5-V8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/583cd57ba5.mp4?token=ZlA4FUq-X2sOP7DoSj0pHxLttQqF7tNStUiXN62RDg2NRznFgTe_nKJORQHxxk5uhJThvWHiauT42-3rqXI9nQ55Q2XJv3n_A-BVcl84Eqd6KfQbzFy5WjtpOi4GTDY6LIcXQ0nE_1AjFisXCqscXMr8xXubm7oquy7_oi8UvCRRnimuOZnJ0fmu8BEmbYAJ3cL8XwzXZ57zE7RlcKxdyMAx9NfUOSsHbN7IpMOPTCPpM6lxUDaMwBT0mmHDCpFUO2O7ZrwEN10_YeIFyz2dvaLUhQsN5AKtV6sNfJAAPphM2ujdNrRI_3ElVQHtPtoJQ7PZpZSAKsbtrSkJnaHz0i7daxxfgrK86uRF5Pqgjwz64ZPKuRdXipjW2MpJd2Hi7j8gq1ZDBOe-mvtB322VbXZNIk61d0sBjdYS4e7tHmNvePaePEUKF2Ymysc5Kxd9SN_w5p8f7sS8j2pdkZJDgaPN_sq0BS1NyDJxtkQmHgDp3l6V56MLZaEEd6Bke31zKfNGOQ_ASGFBDldVDb_dB5PpZK7vMxO3_RPFUS5KBqW5gEeVQgMffFkuUWFcznQ0zpUfZxCvNfiuFokC4YsdjG0rKggR7S-SFWLCK81tUbwcBud7FvcLpFGYceQ2sCWtYCukIOnKK3tzWZZMrVFlnWO7XNXe_5-ZWak_Gur5-V8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شعارها رو گوش بدید،
اینها اعضای سازمان مجاهدین خلق هستند.
خوشحال هستند از صدور حکم اعدام
برای «حبیب القانیان» ، توسط خلخالی بدنام!
جمهوری اسلامی اعدام می‌کرد، حذف می‌کرد، مصادره می‌کرد، بقیه  گروه‌های از جمله همین سازمان مجاهدین خلق هم تایید می‌کردن، میگفتن خیلی هم خوبه!
تا اینکه جمهوری اسلامی بعدش رفت سراغ
خودشون! و در ابعادی دست به قتل عامی در زندان‌ها در سال ۶۷ زد که در تاریخ ثبت شد.</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/5788" target="_blank">📅 16:57 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5787">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/938419e982.mp4?token=XdRUSBMW1z0zCCZNb-E9KFnnE6IOIKGvjH8vns7XkZjdzehw7KLRYgqy6-7XZwsdrfLTfJA79MY0On0aQ5x82UcOTnQKkaAUXiaVBfeV0vVhWUW__y1d1v1ajIafsTSOKBYV4PufHIEgpDcfg8TwByj0nIWhC-G8xG71FtK_Bts3CoumKa2i-aPhLfwi6kY5KSPmFpaCyT35QEFaqp7bL1_qLuR4P8ZyBN_alcNa1Dui11Z6PxUVEvITBHAkQ4QE8CuS-a9jBdMd4JBerkGMH9-3AadLSnZPmfRAgcfjSL_200vazp0wUdyTXE9DDDWuEhxLrrmO9MzC4Qw4eclwXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/938419e982.mp4?token=XdRUSBMW1z0zCCZNb-E9KFnnE6IOIKGvjH8vns7XkZjdzehw7KLRYgqy6-7XZwsdrfLTfJA79MY0On0aQ5x82UcOTnQKkaAUXiaVBfeV0vVhWUW__y1d1v1ajIafsTSOKBYV4PufHIEgpDcfg8TwByj0nIWhC-G8xG71FtK_Bts3CoumKa2i-aPhLfwi6kY5KSPmFpaCyT35QEFaqp7bL1_qLuR4P8ZyBN_alcNa1Dui11Z6PxUVEvITBHAkQ4QE8CuS-a9jBdMd4JBerkGMH9-3AadLSnZPmfRAgcfjSL_200vazp0wUdyTXE9DDDWuEhxLrrmO9MzC4Qw4eclwXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قدرت حضرت عباس</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/farahmand_alipour/5787" target="_blank">📅 16:27 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5786">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JK7xLE-KeXy-s2AAQWncBheQJ2NYO0Vd89OVE-Xn10JYfVK1a07UTKpVOqF-WVZRhsAemwipHQ0t_LhTsLUwCsnQFKzRkKE5TLmKqJUpJ-qzh2N-R-eDBZoy7VK6LkZJteghgSxhKsdkjX9xV0rWjY6WHqwIK8RlSvuM6iDXBEuVK4m9-ip0Pvzz9A69cd15CqLIfKn07c6KkQD990eWZvLPMjVEDSAFRbrigu_R8wfJmR1UrzOmDU81y131HT6CYc9elB1qlkui2Ai-oXPelrngIZJ9UFQt2L3oe-8poOYY1-B06N9W9llNNsC-U2wNBs0htU-kWiBJTcmSLs_Nbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای فروردین ۱۳۹۹  همکاری جن‌های دشمن با سرویس‌های اطلاعاتی علیه جمهوری اسلامی!  همین آخوندها وقتی اصفهان در محاصره ارتش محمود افغان بود به شاه سلطان حسین میگفتن اصلا نگران نباش که ارتشی از جن‌ها میاد به کمک حکومت شیعه!  ولی این جن‌های نامرد نه به امام‌حسین…</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/5786" target="_blank">📅 11:31 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5785">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b91e9581d.mp4?token=F_l1rhi77L7_vMEr1jwvqFxLWB-xxwrSwkWMuSWn3jvwo0uuK6IsxO-eyXkuQBWtoX9sh93EB1NzIBQqITUObSWuNQ9pc7YKE0xOyRzjwehMQa0afWpslDxxJHa2AfDHWmBqpsRJAxc_j9s6_957D22pw5hEmmCjFeCKYw7_zZWZFephVStEF8zv8mQ9yXhnPDSt_Iyv8LPvpFvTiaqyfb0zBrT8C5rp0fVde2fVzEer1tVRdEp8xUq7p6CgcLvylrbZJPnuJDhdRZ4V5sQNxSDmQplTi9Edb4R7ktKM3iNwI9Pb7NTn9CrOfHkDvggE9-NcChdNLH0GRq6sJ6cCsw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b91e9581d.mp4?token=F_l1rhi77L7_vMEr1jwvqFxLWB-xxwrSwkWMuSWn3jvwo0uuK6IsxO-eyXkuQBWtoX9sh93EB1NzIBQqITUObSWuNQ9pc7YKE0xOyRzjwehMQa0afWpslDxxJHa2AfDHWmBqpsRJAxc_j9s6_957D22pw5hEmmCjFeCKYw7_zZWZFephVStEF8zv8mQ9yXhnPDSt_Iyv8LPvpFvTiaqyfb0zBrT8C5rp0fVde2fVzEer1tVRdEp8xUq7p6CgcLvylrbZJPnuJDhdRZ4V5sQNxSDmQplTi9Edb4R7ktKM3iNwI9Pb7NTn9CrOfHkDvggE9-NcChdNLH0GRq6sJ6cCsw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زعفر جنی، پادشاه‌های جن‌های شیعه
😅
حامیان همین‌ها میان کامنت میگذارن که تاریخ مطالعه کنید! محتوای تاریخ‌هاشون!</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/5785" target="_blank">📅 11:29 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5784">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb5c00112a.mp4?token=nd-lOohnCYd8qssipfo1tx9zrmOgGXXY4SiMD0QEYqrGkz3BTCeFh5rsNYdXrWCKb8Z5oVLY55bwzUjTcDe4CP03D-Vp0v6h6wRt_2jCihKCQs0hP0_hyZtunbtuHxIs5TpLchHr99XXN2CHj7QGtDYCazxX2G5smFoKbQju6wGtxxE8iIJlsOisP1-Fpi4d3xnYy030qF7e1oIyS7gJiWn-c-OLX7FYuZJAMV5dxWe9ipDc1-b5LtnD09moAGUoV5_p83_Z-DMCLPuu-B2DtBEznzKDcRU4Xxi9kE4It6X2s1mVPFHar--6tAK3RUvS6iAIIiCrxEQP1H9VBc-3EA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb5c00112a.mp4?token=nd-lOohnCYd8qssipfo1tx9zrmOgGXXY4SiMD0QEYqrGkz3BTCeFh5rsNYdXrWCKb8Z5oVLY55bwzUjTcDe4CP03D-Vp0v6h6wRt_2jCihKCQs0hP0_hyZtunbtuHxIs5TpLchHr99XXN2CHj7QGtDYCazxX2G5smFoKbQju6wGtxxE8iIJlsOisP1-Fpi4d3xnYy030qF7e1oIyS7gJiWn-c-OLX7FYuZJAMV5dxWe9ipDc1-b5LtnD09moAGUoV5_p83_Z-DMCLPuu-B2DtBEznzKDcRU4Xxi9kE4It6X2s1mVPFHar--6tAK3RUvS6iAIIiCrxEQP1H9VBc-3EA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زعفر جنی، پادشاه‌های جن‌های شیعه
😅
حامیان همین‌ها میان کامنت میگذارن که تاریخ مطالعه کنید! محتوای تاریخ‌هاشون!</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/5784" target="_blank">📅 11:29 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5783">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/383f2c1b20.mp4?token=bcbN8QXeB0kOxo9tNwMkA1-wD9lMtdpRu-vlLD9ziBfsADAtPdSjYmNsh4NzJUMJhfeBhgQ4hPUl4kTU8mTiQaoTpKUA2LrwVD8eGjW_N-AMzhucp_C8M5bXqCVQe2NaXPacfTMdnF2WB7n7feoEuMesxP49SExtu9tRR_yOPGrEbTz2EimJulSg2WTE36RveRgD5ls2rTZ5_ZvjLqw6QmdSMGhI7wPQOK20YXvB5dPFtouv7ireftq0fImm-VVaQbqk4r9r94rMInSTWewZswaQbbO_93V7FOMlD36T3cnxfoXXfEaHIjYBJHZ8ktzmEpB78Uc0fCgft0Y6Heu_Hw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/383f2c1b20.mp4?token=bcbN8QXeB0kOxo9tNwMkA1-wD9lMtdpRu-vlLD9ziBfsADAtPdSjYmNsh4NzJUMJhfeBhgQ4hPUl4kTU8mTiQaoTpKUA2LrwVD8eGjW_N-AMzhucp_C8M5bXqCVQe2NaXPacfTMdnF2WB7n7feoEuMesxP49SExtu9tRR_yOPGrEbTz2EimJulSg2WTE36RveRgD5ls2rTZ5_ZvjLqw6QmdSMGhI7wPQOK20YXvB5dPFtouv7ireftq0fImm-VVaQbqk4r9r94rMInSTWewZswaQbbO_93V7FOMlD36T3cnxfoXXfEaHIjYBJHZ8ktzmEpB78Uc0fCgft0Y6Heu_Hw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همش ثوابه :)</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/5783" target="_blank">📅 11:08 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5782">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a9c5c701b.mp4?token=dSyWCSFRmReG3hkixo73HhkWomwDa29HC578h_J0UAOtx09W3iYvjBfwBt4_pR2vIk_UMWpwUIQSYcpqGXKEr7wZHBVPOJl2kW8WbXODN1uUVhMTBMJrHt9QltEiwSpIjzVOX9G0H46SlcUvgsSNRpeW-YIU-RtdjxJGnEtQ6Uqr2aJxDrX6Y8QlYWUpXolA51c-GFqqOiDL-cycm2yMLCeMLBInyK1TQDa172MqzPEcLEi-AmkCxBLy9sjZM-uaMgcKJtlR9EvVKQHQoSjGGGF0H4yAZtc0BNdqXYYUHMxKncxVY1U1oegYIsVMH41NHK23JGWmW3jILwLJEw0UUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a9c5c701b.mp4?token=dSyWCSFRmReG3hkixo73HhkWomwDa29HC578h_J0UAOtx09W3iYvjBfwBt4_pR2vIk_UMWpwUIQSYcpqGXKEr7wZHBVPOJl2kW8WbXODN1uUVhMTBMJrHt9QltEiwSpIjzVOX9G0H46SlcUvgsSNRpeW-YIU-RtdjxJGnEtQ6Uqr2aJxDrX6Y8QlYWUpXolA51c-GFqqOiDL-cycm2yMLCeMLBInyK1TQDa172MqzPEcLEi-AmkCxBLy9sjZM-uaMgcKJtlR9EvVKQHQoSjGGGF0H4yAZtc0BNdqXYYUHMxKncxVY1U1oegYIsVMH41NHK23JGWmW3jILwLJEw0UUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آورده فرهنگی شیعه برای ایرانیان</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farahmand_alipour/5782" target="_blank">📅 09:32 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5781">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B01VjOGJClob9bAzzKVUSuXs8ODSxfJppO_qu6n62iFwCJuAMgJMWAo87HvjxSOUm1kgqat5iUdoxRa6OADXGPOwwAU24Lqq_JUbygQdxhuG8ZA7QCCUNwCpkeMSwAqr9QA2vIR-7NcOmgasnqobkHXQEYMXX2b0P0riv4oxrHtPUhqOGVtbs7nA-8zX4yXlNF66E8ChWkJfIZJ5_dm9E-q1Pwuc7J0hLpuQ6MH3qmqiWwZj8O4YLH0zcQ-axen3VcoSkDhp1lHIhrubzwPEiEHtxcB8FhFNHdWH18i6wSOhLW1kWj9__2f8uxB0GiAWROaK4yipY6RNy-482tFmAg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/5781" target="_blank">📅 09:29 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5780">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🚨
جمهوری اسلامی و آمریکا موافقت کرده‌اند که حملات را ادامه ندهد و سه‌شنبه در قطر دیدار کنند.</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5780" target="_blank">📅 00:08 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5778">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/409f2a841d.mp4?token=inGz_XIL8k_Uw7dDts3-1k-k7Rpkaiw8_rrOR2iW5GSwIQtaVP3gGHnjxWwXDdnXVzpwli2y2U7xEF9PecKp_UD5yw2rScIzY15ueg5S7h8yfEOE_mDiAGBcs-5spi2jU4IA8w2kM3lj_CKAifsXtrXawaCf7GiIi2JPh72y8TfuRX479bpfZhSqsHERKSu6t34oSw9mWWEM0aT0M5jcqlImgoUaVE1K_RV8qLmOj51DiMrRIOtiTCDgJv0g3lE8d2MeRozcJmOzBZbzT0fBhJqS8o4Z7IPX8Kb4j4whecUP5nOtR91cQyUY_B1TQzcEdNxcWLcNIUS-vpcglTMF4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/409f2a841d.mp4?token=inGz_XIL8k_Uw7dDts3-1k-k7Rpkaiw8_rrOR2iW5GSwIQtaVP3gGHnjxWwXDdnXVzpwli2y2U7xEF9PecKp_UD5yw2rScIzY15ueg5S7h8yfEOE_mDiAGBcs-5spi2jU4IA8w2kM3lj_CKAifsXtrXawaCf7GiIi2JPh72y8TfuRX479bpfZhSqsHERKSu6t34oSw9mWWEM0aT0M5jcqlImgoUaVE1K_RV8qLmOj51DiMrRIOtiTCDgJv0g3lE8d2MeRozcJmOzBZbzT0fBhJqS8o4Z7IPX8Kb4j4whecUP5nOtR91cQyUY_B1TQzcEdNxcWLcNIUS-vpcglTMF4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش اسرائیل از نابودی یک تونل
در روستای مجدل زون در جنوب لبنان خبر داد.
این تونل ۲۰۰ متر طول داشت و در عمق
۲۵ متری زیر زمین ساخته شده بود و در آن
سلاح نگهداری میشد و دارای چند دهانه
برای شلیک به مناطق شمال اسرائیل بود.
اسرائیل گفته که پیش از نابودی این تونل
آمریکا را در جریان قرار داده.</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5778" target="_blank">📅 23:57 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5777">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/06f2d554a0.mp4?token=LnHdFbwUpcwEl7gPYEWUqQgF_c6kPkxBPZQuz2bNhoP4lKgTq0oUtrzMGVKBjIPq0LS6fmAh3yLj8KMr2n8zJZ5xYoEr29nsUDRb5czZ3m6FeZ57QohZzoCyEWTEYeMsVNB7yqWcBjDa71B_KJD7Sk-uXXWkm1kATnOMNoGCAG3hjOsWM4QBSLT0XiKFcxBwXHuyBLiVKKUZYjsmJh6HfoOhx4JqMvYxtlO7HUo9wERloeMXaWNpe21WonZf3Ch-2ZiZGNshWE-LH9Dl3yGkPiJuyaF8KCZAqv_ef8om6ZwNlwZwpn3ojonNtMPTlpa-PAN1KGBUQDNNNdV_PF2AaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/06f2d554a0.mp4?token=LnHdFbwUpcwEl7gPYEWUqQgF_c6kPkxBPZQuz2bNhoP4lKgTq0oUtrzMGVKBjIPq0LS6fmAh3yLj8KMr2n8zJZ5xYoEr29nsUDRb5czZ3m6FeZ57QohZzoCyEWTEYeMsVNB7yqWcBjDa71B_KJD7Sk-uXXWkm1kATnOMNoGCAG3hjOsWM4QBSLT0XiKFcxBwXHuyBLiVKKUZYjsmJh6HfoOhx4JqMvYxtlO7HUo9wERloeMXaWNpe21WonZf3Ch-2ZiZGNshWE-LH9Dl3yGkPiJuyaF8KCZAqv_ef8om6ZwNlwZwpn3ojonNtMPTlpa-PAN1KGBUQDNNNdV_PF2AaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">منطق جمهوری اسلامی
و تعریف «امن» و «ناامن»
میگه اگه  یه کشتی بخواد از مسیر «ناامن» عبور کنه بهش شلیک میکنیم :)</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5777" target="_blank">📅 23:26 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5776">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FyGOTK6vggpAoijdqT4F37RefXaUt3ZzNckHka48NkIri7sccAR4w39xi8_qMsFsYdGy_9-7INScMzQpidJ3ne43NqvUR2WvA7eZeHV_SaQsipLGmsCUJDZcdJZM3ATsrPrcJomMKehuKLFmcMmuD9uu4Km1s3Uf1FyZ2tpaFGjXszl4_C4bBugS9MyBg_PNkkcbWeQ2NtgrqO8yc0nMUNEQq5Hy9yRGyt3kxtPGmxIzZvhKCSC22G2g2KfB5UPm2kLRn8BQ0J2fx2xdKtt8T8A6wunN-l_DtR4F6_PJqU4SQim-LbBHHlQZaGZdTFiqzZ9wwXCRPv1YbaVBt734Rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس: چاره‌‌ای جز ساخت بمب اتم نیست.</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/5776" target="_blank">📅 19:39 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5775">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e4e9d7782.mp4?token=WNicB_IBmp_pPcYYsUXTz-Fon9ciYX_fJ-cCi0cBLnzUg1funq773H7S3LejgKIygz1E0HjVIbIPFAw-rzy1OblsSDMofFZ5FKiJQq8-dgjusszRZmLimbaP3a06qvT7F2R8SAyUOKxJToch86pGIuF5Abi_yg4VkeQLWGebhkT001Fpt2H4NmbBrK0qJV-ZAH8_t-LMLOxRyA5kQUzjy4KqBhhoBanOJBzhW7e4Q2fUwh4r-n9zx2n-GARbqbzvGZ78VGw02h7p2q4Patkv6GgFbS5_bxj-aO1NObdmHGGBL8dxrW8jpnL_eGQAYRIWgAsQ8mOnFnDSkS4EnrzgSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e4e9d7782.mp4?token=WNicB_IBmp_pPcYYsUXTz-Fon9ciYX_fJ-cCi0cBLnzUg1funq773H7S3LejgKIygz1E0HjVIbIPFAw-rzy1OblsSDMofFZ5FKiJQq8-dgjusszRZmLimbaP3a06qvT7F2R8SAyUOKxJToch86pGIuF5Abi_yg4VkeQLWGebhkT001Fpt2H4NmbBrK0qJV-ZAH8_t-LMLOxRyA5kQUzjy4KqBhhoBanOJBzhW7e4Q2fUwh4r-n9zx2n-GARbqbzvGZ78VGw02h7p2q4Patkv6GgFbS5_bxj-aO1NObdmHGGBL8dxrW8jpnL_eGQAYRIWgAsQ8mOnFnDSkS4EnrzgSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تیمی که با بدرقه قاتلان جوانان ایران راهی جام‌جهانی شده بود.</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/5775" target="_blank">📅 17:23 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5774">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🚨
شب گذشته یک عضو تیپ ‌گولانی ارتش اسرائیل در جنوب لبنان کشته شد.</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5774" target="_blank">📅 13:06 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5773">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">ولی ما می‌د‌ونیم چرا شانس با شما همراه نیست.</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/5773" target="_blank">📅 10:17 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5772">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1220ffd18e.mp4?token=jZi9fndW0X0S5DiBuGqNIhZX9N5_zdbb2LHMGEubaZHHchnrVS4zhvcS2SqMU0tMUxkfZ0tknZ2o4oIq806KU74_5iuA3btJ3JK3iB-dAWIXBerS_FjDlJsKP2dUCYxTeDSUfw-a9D5FprY4RLPuJrW_DlpV6iIJWrdioRTlZEYaa2LrM3pG3zLMCkEFfwKQBogFgum4fMdJl1vh5EU59GHytWmh6c-_ZWJQ_LFSOQiDJ_x22YXalGgWa3XFpO37roUGH92eGOQrFzWoGOY6aNAkj9Gh0Dxns-g71VT9JP4aDxQS3hpG6wZwv3e7UepZokzbg6FrzhkZ-2YdbJ9Rtg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1220ffd18e.mp4?token=jZi9fndW0X0S5DiBuGqNIhZX9N5_zdbb2LHMGEubaZHHchnrVS4zhvcS2SqMU0tMUxkfZ0tknZ2o4oIq806KU74_5iuA3btJ3JK3iB-dAWIXBerS_FjDlJsKP2dUCYxTeDSUfw-a9D5FprY4RLPuJrW_DlpV6iIJWrdioRTlZEYaa2LrM3pG3zLMCkEFfwKQBogFgum4fMdJl1vh5EU59GHytWmh6c-_ZWJQ_LFSOQiDJ_x22YXalGgWa3XFpO37roUGH92eGOQrFzWoGOY6aNAkj9Gh0Dxns-g71VT9JP4aDxQS3hpG6wZwv3e7UepZokzbg6FrzhkZ-2YdbJ9Rtg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شجاع خلیل زاده میخواست گل بزنه و تقدیم رهبرش کنه!  ولی اراده خدا تحقیر اینها بود!</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/5772" target="_blank">📅 09:32 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5771">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d645372fb2.mp4?token=QM5t6h8v4oT1tOFO00EFsvyS0leI0EeoD9swLtb9lB5EOAuWh_ztLMyewuPEmoKklo4uqikk_DxjMvfM0B3zw7KhxFS41dNVj-dvKzi-EK34cRRD0KMlDN83mI8A1HgiSba_9zYhUuhgpHm5Ykia7Wkt3d9xGPLgT_uryWiu9Kyq_maxz3e2ixql6SyOsAe5WTwsXfreLTzQvlITyN2w1zMNMZic6tdqFuBrvyMkl3aYFPkozrmMxIXJ0p_8q4r6cQ7qA5Ol5-yij750n0w7JzE3cRSPB_Y5lMBqoepOVoV-yvg2NtuW-9gms3xAL14nna6O7SkWXPc9uovfxVXvjDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d645372fb2.mp4?token=QM5t6h8v4oT1tOFO00EFsvyS0leI0EeoD9swLtb9lB5EOAuWh_ztLMyewuPEmoKklo4uqikk_DxjMvfM0B3zw7KhxFS41dNVj-dvKzi-EK34cRRD0KMlDN83mI8A1HgiSba_9zYhUuhgpHm5Ykia7Wkt3d9xGPLgT_uryWiu9Kyq_maxz3e2ixql6SyOsAe5WTwsXfreLTzQvlITyN2w1zMNMZic6tdqFuBrvyMkl3aYFPkozrmMxIXJ0p_8q4r6cQ7qA5Ol5-yij750n0w7JzE3cRSPB_Y5lMBqoepOVoV-yvg2NtuW-9gms3xAL14nna6O7SkWXPc9uovfxVXvjDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شجاع خلیل زاده
میخواست گل بزنه و تقدیم رهبرش کنه!
ولی اراده خدا تحقیر اینها بود!</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/5771" target="_blank">📅 09:31 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5768">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XPlIymFX76q7RKC9Bv1gZUIvlGdarY6ORbcgjKFW52iqQPb70u7fe1wmpmFx73lTG1yQDxmVcYHIt_9vQLJ_nngmhFJoydlld8XdU_n_namco2Ij_NTWdqPN4pnxCqQiIVapjlwzb96AE8KrhtYBgjKwgNjuY3RnpzQdLLqh_ePpHfraOdXsQuIsq1szPjwh3KF3pZvB17YWqBuM5hAqfWQqS7872LU949wnA6E8K0VK6Ralk_W_rcXP0ItPRIthDcuB_mxXU7hAM0TQiMPYOhxcc_yFeXpf3YlDgCmRuJK_qKQOYCDcZIM_0uUM17h1tr1DjiOAp68W0uGu49xX0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cmHu-s8K2Yg-w9f4EnaUhMLeaUkmYW4_YGlpDLeXkLoAkQcl-8dDACNkDD7LzYSi980hFzuHZuo7Apre8WZOUm5W2T9w01ctPcYAFx-SEhk2yep0KzzH44qSwfHSkPZewUkpZ3Dx35KEm-RTFZAVs1Y2HnrDlT84mgJJAh-netCxbPgFKMhKWVirdX6yo2pI7yLt_CERFyh3iZsvV9wCicbae5kqCU33rFXAhmlqvYO8F7AiwqPeeQe9Qq7ycLlPAEyfB6CmhtWSJ0ewMY3uVsSd-lVifeGj5UY-TmBHenrNFSfWimjZbcL3fJwl1G2xqG_Sn0JWBAwUg8ouNOH58g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/g00YI77z82UqNAldLILF74AtDvpNPx5hhR5XGshdyye7lGuLrz0k1D0iRiLEmAwPRYkAWHfTWdmtKoys551vxPFp1bR6f62Q8g9C6GC-jmYpCXyDXzvVTEcsAi_bZE6PnuVOPijHroWlG1c39dF0P7yR3dpWZB6MG47BcEy-8oIIqDAGwEHC4ycucPt0rPm6MoLJvywzhhtGfPEr-pmNgUuxsQmHH0yqY21cntRBJrtTrzdcnjnIAuMxePhR54YjT0KAX2Ji7Pvad1Uce4C1iVfqqgazwfzAydad73pUlC0zaJ-Ry-QOhYcQ7I5E8wqpXbN9hymOvgY5dzXkqrmjLw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">در جاده فرودگاه بیروت، بیلبوردهای تصویر خامنه‌ای رو حذف کردن و به جاش تصاویری از «اول لبنان» زدند،
که البته دیشب برخی از اعضای گروه تروریستی حزب‌الله رفتن و تخریبشون کردن.
بالاخره زندگی و حیات‌شون در مزدوری رسمی و علنی برای جمهوری اسلامیه.</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5768" target="_blank">📅 09:26 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5767">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">تیم ملا</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5767" target="_blank">📅 08:52 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5766">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/10689e4ea8.mp4?token=uK9FDcBiPTNBdxsNm_eie3nU4gMBGrYNiymRzHdtur_-y9TARBgeAhJqRKHGS1n18A9Ou-QCL_4CvIr37HugJ_sTGGdip10AVaXy0CtfJ8EfUOkXncuBzKlTQUbhVAdRT3-lu2c3MWEy701FRI_W3lZT2--U-zm5KllzPTSAES9urpU63kRrvEmSzF-u21Tgwi3LJ5ZvSGCq6ZMA_w6f0DnaVI5Z88tLd_FwttSG0f_86WSWLt4lpq7UEsazb1aC_OshR7gUg6pfw9_CXuFN1ttohm7uo5d8myQDiIdA1qTAPBzdrNLv5Jb44GC6-bat4ZHdVajjPPVfeud3mLTeeg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/10689e4ea8.mp4?token=uK9FDcBiPTNBdxsNm_eie3nU4gMBGrYNiymRzHdtur_-y9TARBgeAhJqRKHGS1n18A9Ou-QCL_4CvIr37HugJ_sTGGdip10AVaXy0CtfJ8EfUOkXncuBzKlTQUbhVAdRT3-lu2c3MWEy701FRI_W3lZT2--U-zm5KllzPTSAES9urpU63kRrvEmSzF-u21Tgwi3LJ5ZvSGCq6ZMA_w6f0DnaVI5Z88tLd_FwttSG0f_86WSWLt4lpq7UEsazb1aC_OshR7gUg6pfw9_CXuFN1ttohm7uo5d8myQDiIdA1qTAPBzdrNLv5Jb44GC6-bat4ZHdVajjPPVfeud3mLTeeg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فقط مدل گزارشگری فوتبال رو!!
یه کشور مسلمان [الجزایر] داره کاری میکنه که یه کشور مسلمان دیگه [تیم ج‌ا] تو دور بعدی باشه!
‏یهووو یه کشور مسیحی[اتریش] گل زد و اینها هم حذف شدن!!  :)</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5766" target="_blank">📅 08:43 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5765">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17301f18ad.mp4?token=QULzo3rvzxGgtlWKbr09sAjSPdBNLTTD6v4ZnFO0pB-mF8HJbDAFMF1UVBRtzUIfdobam9wrfnicbWw69Sa9ne42x177tzGSmC5cVhwpisHBfiSUOOJNMRHklUGbL7FUhFewM8f9UTea7YYxWrIZVVwR2YwADLb4ZBaVviEU74dHdhA5HZyOfa0mViNiNFiufRGoxSt82afiYFnhqWJlfy8eqPPnJdmJuhT-Fatqf3-Dpm03dm2AfkLJwwDb-VDd3qa_cEgejAl-1W35A2EifYsy_-CMQC17meJSicJSEsXVftGuTO1-P5trXE66yUnnJF6QXMs7wjDqmRYuDLPLaU8OrxhRhnSeGZG1CfxofZlZv3KaJOiEF3dAcM36EHd4IGqTcRZpyW-KrlMTAPSf_fIjUPSvITS91be18L1kwbp-1jjZTybZoJv6keZduHCnFIALCuUdqrpJAg5W0Xa4cnBZ-LMF38U_EICa2ZhVcq3Qj3S0nE7LVHsvI2Zc75bh-TOoZFQPNLEBpNqNemvaoul-1gndqZxOOIfxAJ0aPvzszrsFpJlQK549vgpwk2G85Sn443w0Aud68sOkDpUBpu5pbkP9TM5-Ug_PApAeFB6ZylPTx4b0I_WfP48bAgeDvi1ijEwWXpyzU_1gI9MB7X9eb-f4vNDt-vMHtTNvLKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17301f18ad.mp4?token=QULzo3rvzxGgtlWKbr09sAjSPdBNLTTD6v4ZnFO0pB-mF8HJbDAFMF1UVBRtzUIfdobam9wrfnicbWw69Sa9ne42x177tzGSmC5cVhwpisHBfiSUOOJNMRHklUGbL7FUhFewM8f9UTea7YYxWrIZVVwR2YwADLb4ZBaVviEU74dHdhA5HZyOfa0mViNiNFiufRGoxSt82afiYFnhqWJlfy8eqPPnJdmJuhT-Fatqf3-Dpm03dm2AfkLJwwDb-VDd3qa_cEgejAl-1W35A2EifYsy_-CMQC17meJSicJSEsXVftGuTO1-P5trXE66yUnnJF6QXMs7wjDqmRYuDLPLaU8OrxhRhnSeGZG1CfxofZlZv3KaJOiEF3dAcM36EHd4IGqTcRZpyW-KrlMTAPSf_fIjUPSvITS91be18L1kwbp-1jjZTybZoJv6keZduHCnFIALCuUdqrpJAg5W0Xa4cnBZ-LMF38U_EICa2ZhVcq3Qj3S0nE7LVHsvI2Zc75bh-TOoZFQPNLEBpNqNemvaoul-1gndqZxOOIfxAJ0aPvzszrsFpJlQK549vgpwk2G85Sn443w0Aud68sOkDpUBpu5pbkP9TM5-Ug_PApAeFB6ZylPTx4b0I_WfP48bAgeDvi1ijEwWXpyzU_1gI9MB7X9eb-f4vNDt-vMHtTNvLKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب خیابانی پیام عربی
به تیم الجزایر داد که ای مسلمین پیروز بشید بر تیم اتریش،
تا اینطوری تیم جمهوری اسلامی
هم بره مرحله بعد،
ولی اراده و برنامه خدا
ناکامی و شکست جمهوری اسلامی بود.</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/5765" target="_blank">📅 08:36 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5764">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/27a845337c.mp4?token=tNbCAp7crIBHmkjaNlW4Ljyc6fZaxOspNFh1O-duGhs-jfbLmMX4T1MHBuK4FxVgsKDjfBZFoWiP1yZbBqmyxnIcKHgW8oLeeN_PNQ8pHRZdNlAkAdYfJl79WsGROfXhIDSbiqskkBfCSKRp5qp0pHOdrp1cY_efiXQXQB0VSHG6VChJRa7NTU08iLDzTE0B45V7CffcD78Fma3BoJK0yM7DEadt4e5SLxbuuikffooQ5MKrfXoeG1zwkImMv634g0nyuEHyJijbbI3uLYTVNRpeApNJEN31F3uO3k0YyYBbxQKqiETG3whUyuhyWEjJUPGC_7nHjrOBlSXEra3l_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/27a845337c.mp4?token=tNbCAp7crIBHmkjaNlW4Ljyc6fZaxOspNFh1O-duGhs-jfbLmMX4T1MHBuK4FxVgsKDjfBZFoWiP1yZbBqmyxnIcKHgW8oLeeN_PNQ8pHRZdNlAkAdYfJl79WsGROfXhIDSbiqskkBfCSKRp5qp0pHOdrp1cY_efiXQXQB0VSHG6VChJRa7NTU08iLDzTE0B45V7CffcD78Fma3BoJK0yM7DEadt4e5SLxbuuikffooQ5MKrfXoeG1zwkImMv634g0nyuEHyJijbbI3uLYTVNRpeApNJEN31F3uO3k0YyYBbxQKqiETG3whUyuhyWEjJUPGC_7nHjrOBlSXEra3l_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
تیم فوتبال جمهوری اسلامی رسما از ادامه رقابت‌های جام جهانی حذف شد!</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5764" target="_blank">📅 08:26 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5763">
<div class="tg-post-header">📌 پیام #40</div>
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
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/5763" target="_blank">📅 08:18 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5762">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🚨
🚨
حمله به جزیره قشم
امشب، دومین شب حملات آمریکا به منطقه تنگه هرمز است.</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5762" target="_blank">📅 01:40 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5761">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ehki3UAfU5AV7fpCCypxZCcdgGVEwLr5yPDo0whAHbDQNHv4-Q9YgrWglc8D42UKwL9InMMK_UP-PBEKAo_lHpu2V8uVBtHaNsIi_aYT0-BeXWyY4XfPwbWVoyxFOgAeE5cfBhSnALCKeX8MkR1lGIc7Dfui0brmOnUxNuFRxsCpSZuFAhR7mcKW8I9RKUxOgsd0Ya3UiWJn4Q96DAlkhqG6uApKck25D7ENqmeIAuqE4gQbBMVjCvnBF0I4Tyy4dbfSuPxjLq1I5iTKbgYhHzjNjMw17YVlwsQMHnPEm5-x2DHplI0nDV5K0t-_5tE_jwajFrVF8IPpks3Xy3ykOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیانیه سنتکام : به سایت‌های ذخیره پهپاد و سیستم های ارتباطی جمهوری اسلامی حمله کردیم.
متن کامل :
نیروهای فرماندهی مرکزی ایالات متحده (سنتکام)، به دستور فرمانده کل قوا (رئیس‌جمهور آمریکا)، در تاریخ ۲۷ ژوئن حملات دیگری را علیه چندین هدف در ایران انجام دادند.
پس از حملات دیروز آمریکا که در پاسخ به حمله ایران به کشتی
M/V Ever Lovely
صورت گرفته بود، به ایران فرصتی داده شد تا به توافق آتش‌بس پایبند بماند؛ اما ایران با پرتاب یک پهپاد انتحاری در بامداد امروز ساعت ۴:۳۰ (به وقت شرقی) که به نفت‌کش
M/T Kiku
اصابت کرد، نشان داد که این مسیر را انتخاب نکرده است. این نفت‌کش با پرچم پاناما و حامل بیش از دو میلیون بشکه نفت خام، در حال عبور از نزدیکی تنگه هرمز بود.
نیروهای سنتکام امروز در پاسخ مستقیم به ادامه اقدامات خصمانه ایران علیه کشتیرانی تجاری، دست به حملاتی زدند. هواپیماهای نظامی ایالات متحده زیرساخت‌های نظارتی و جاسوسی نظامی، سیستم‌های ارتباطی، سایت‌های پدافند هوایی، تأسیسات ذخیره‌سازی پهپاد و تجهیزات مین‌گذاری ایران را هدف قرار دادند.</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/5761" target="_blank">📅 01:27 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5760">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🚨
🚨
اکسیوس:
‏ارتش ایالات متحده در حال انجام حملاتی در منطقهٔ تنگه هرمز است.
این حملات در پاسخ به حمله جمهوری اسلامی به یک کشتی تجاری است.</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/5760" target="_blank">📅 01:10 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5759">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">‏خبرنگار صداوسیما در سیریک:
‏دقایقی پیش صدای چند انفجار شنیده شد.</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5759" target="_blank">📅 00:56 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5758">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0cee64931e.mp4?token=OdSDntw4GNWj6cce5W_huB1f4Uu_5peAdRrtK6mm-A4ubOWIzb16CjQKyESzwVg179V6FJq2SeE46Iqi8Fr90sPlFZJo4G01pHm9WxcOId_qjeQLJ4GS5POxGAeFJzSCpMJUWrSkAWXukpB0rXBzbj-1nv8aVrScss4Kd1ld2nRGSMuQuJ1NQusVxVRt9S_rTnnlj8N0n_ML43ntMZAAb2tvJaQO05dZfenqqAfQXZGndWLzajZFeUYPd4R78sV7hw59eX4liw2fjqqvFRNvN88m5CAtDXFNh1rFQ1k3m7dyUIdpxgPZRAHlwz2xHgvifX3VZc_julxnfUFMfHWyezHPQDkAi2M76dbEyLyCDi2y_UeQtk1OOj4cam17gxjT2FVfyw2vdf3-TqZMt9e7gyqcpIDiXY5wXGVIZJXa6xSHYJthmC6i_jWfc3_uKiezFKUJm_QzhD4PPH1VfSEzxbFxIzAo18Y0MHKGZigOwES3PnONs4cWAjiNKD52YJZjjUBgdHjvJ0t4BObGrMGaE5kX5N3x5uSH4fMOwk8b5-RsGRW1jShrbs_chYdrmjYphW1rjka0m2fmkMxqa5eI6v_K6M2YG4-8uMrt2splq2SSqQqQW6nSjfgHsFwPbkZxaDDmIvkX_gAU8Y6lD-IHjE-WfF7ofDRh3gj289Q7C8c" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0cee64931e.mp4?token=OdSDntw4GNWj6cce5W_huB1f4Uu_5peAdRrtK6mm-A4ubOWIzb16CjQKyESzwVg179V6FJq2SeE46Iqi8Fr90sPlFZJo4G01pHm9WxcOId_qjeQLJ4GS5POxGAeFJzSCpMJUWrSkAWXukpB0rXBzbj-1nv8aVrScss4Kd1ld2nRGSMuQuJ1NQusVxVRt9S_rTnnlj8N0n_ML43ntMZAAb2tvJaQO05dZfenqqAfQXZGndWLzajZFeUYPd4R78sV7hw59eX4liw2fjqqvFRNvN88m5CAtDXFNh1rFQ1k3m7dyUIdpxgPZRAHlwz2xHgvifX3VZc_julxnfUFMfHWyezHPQDkAi2M76dbEyLyCDi2y_UeQtk1OOj4cam17gxjT2FVfyw2vdf3-TqZMt9e7gyqcpIDiXY5wXGVIZJXa6xSHYJthmC6i_jWfc3_uKiezFKUJm_QzhD4PPH1VfSEzxbFxIzAo18Y0MHKGZigOwES3PnONs4cWAjiNKD52YJZjjUBgdHjvJ0t4BObGrMGaE5kX5N3x5uSH4fMOwk8b5-RsGRW1jShrbs_chYdrmjYphW1rjka0m2fmkMxqa5eI6v_K6M2YG4-8uMrt2splq2SSqQqQW6nSjfgHsFwPbkZxaDDmIvkX_gAU8Y6lD-IHjE-WfF7ofDRh3gj289Q7C8c" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جاوید نام ۲ ساله
💔
‏فرزند ایران و جان فدای میهن، جاویدنام علی محمدصادقی، کودک ۲ ساله، روی شانه‌های پدرش بود که با شلیک گلوله جنگی کشته شد.
‏پیکرش را همان شب تا صبح در برف نگه داشتند و روز بعد به خاک سپردند.</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/5758" target="_blank">📅 22:09 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5757">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q9gcNBekOv1pJarrcTqL35BBV0nW5uhx3SncOo8RtFMOnb-d5B1mRC5aBpYRgwyF06ri34wT_WK8ddIngcH9SVU0QO07oWs2lsil1xIVyeLPWzLF7rP1crtF0xFY_FRDqlduTeM9SnX86LOkEXpm36jDvmz-RjXYD5DAP3X_5T-oj4-jlJ7IueJAZhK386lC7T_5RzB5qxLl3rIa75-hrC6lNEMCvG1yc_0qPU1bkfxKg4wdVAq1K9-cj2HO70HFTyKeUxus3aKD6GKihwtV1bZDOfAIGlNu2yWx5VIINxwPvhjF_zoZTXlkNwm8AwxTEHhdOcHiMaQ5nAzXgn-hdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
پنج حمله هوایی اسرائیل به نبطیه</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/5757" target="_blank">📅 20:23 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5756">
<div class="tg-post-header">📌 پیام #33</div>
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
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5756" target="_blank">📅 18:41 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5755">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">دبیرکل حزب‌الله لبنان، توافق میان‌ دولت لبنان و اسرائیل را که بر مبنای آن حزب‌الله باید خلع سلاح شود و سرزمین‌های لبنان تحویل ارتش لبنان داده شوند را رد کرد و بر ضرورت نگهداری اسلحه تاکید کرد.
حالا این اسکله براتون چی کار کرد؟ یه جنگی شروع کردید و یک پنجم خاک لبنان رو دادید و فرار کردید و از دنیا خواستید بیان آتش‌بس برقرار کنند.</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5755" target="_blank">📅 16:48 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5754">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db5841aafe.mp4?token=SRwld_e7nvfxbw0vZPYTqirY9nE84eCUfOR3xKzgWmapyqilfMGaHZXgklF8K6bf5jhNLQpjW-MZAQJhQD3hLH5b0BbTYdJlnDoblwEwIJeI6C2LyCNYAGlfTKZKFmsTxcSfJmS6NFZKPm_rbHR-Oc9fKR-IIirxFoAmY9hG4ry9ROVnsdDzXuUrkk-485KltW2vEfBGbKCbBfYMo69168ogd2mZSzvD0nPd3Bd3UZA0D-DFqUWf_pjXiOaAv1_rCKL-9lYtIc7sXTS6XLhN0UvqIBDQhaILfmA_iF6akm68agqHUGN6K5acOZq8K457Tk6oOtIB07rLW2nqdR_oHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db5841aafe.mp4?token=SRwld_e7nvfxbw0vZPYTqirY9nE84eCUfOR3xKzgWmapyqilfMGaHZXgklF8K6bf5jhNLQpjW-MZAQJhQD3hLH5b0BbTYdJlnDoblwEwIJeI6C2LyCNYAGlfTKZKFmsTxcSfJmS6NFZKPm_rbHR-Oc9fKR-IIirxFoAmY9hG4ry9ROVnsdDzXuUrkk-485KltW2vEfBGbKCbBfYMo69168ogd2mZSzvD0nPd3Bd3UZA0D-DFqUWf_pjXiOaAv1_rCKL-9lYtIc7sXTS6XLhN0UvqIBDQhaILfmA_iF6akm68agqHUGN6K5acOZq8K457Tk6oOtIB07rLW2nqdR_oHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">:)</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5754" target="_blank">📅 16:33 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5753">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f038d1dce.mp4?token=Drfs887Cuu8Gv9g9hsA5_-NfklOlAPoasONbdh7GzhBqf25dpskD_1M3pKEEWcggSYWMulk_4QvAHh57LTiybm7lePyKkFRKlbWrGUvtv3R_oGcdZWO525UQOLW7MStQy-DNtGp9IcOqMEDCKYrnVMnDYTWWWaIONcPb3oXhw6IQQW9RyRK-67-wsZmPjPhX-6-51YCiRx3Z-jd88Vj1JDw7TWKCYu9smC-pMpTOCvu01ADZ9sX-UnPnkGuw2yKJD-ME9XMFkD1Y5x4fvOF8cjuAdBEunyWJWv9noKhyX7Mfqs8qMjSDfpNTJ0rPEz2qYwDqnFNtlp9u1ChBwfDS7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f038d1dce.mp4?token=Drfs887Cuu8Gv9g9hsA5_-NfklOlAPoasONbdh7GzhBqf25dpskD_1M3pKEEWcggSYWMulk_4QvAHh57LTiybm7lePyKkFRKlbWrGUvtv3R_oGcdZWO525UQOLW7MStQy-DNtGp9IcOqMEDCKYrnVMnDYTWWWaIONcPb3oXhw6IQQW9RyRK-67-wsZmPjPhX-6-51YCiRx3Z-jd88Vj1JDw7TWKCYu9smC-pMpTOCvu01ADZ9sX-UnPnkGuw2yKJD-ME9XMFkD1Y5x4fvOF8cjuAdBEunyWJWv9noKhyX7Mfqs8qMjSDfpNTJ0rPEz2qYwDqnFNtlp9u1ChBwfDS7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جشن و شادی در غزه
در پی‌ موفقیت تیم فوتبال مصر
در برابر تیم فوتبال جمهوری اسلامی</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/farahmand_alipour/5753" target="_blank">📅 10:20 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5752">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b07e212ab.mp4?token=VjnO234wxh6daJPQNbYnvgPnFRgHPeX1orh6SkdTFGEfr3EtKdOB6ZpWwxCvd6UVQjCkFgwETEGqQ1BQu2mBX-4csdJKYNp-kZU788OpYnUqoAMSrneN8Jlp1Zw8zJ730r2O-SyxibYgW7CjCQv-HDoBMv77JpFBv6bifD3WFPr0RWkK4X9vXI0lne3jRzb8zKbbMEILBSqVqjX7MGbV203yrFUCB8BDTsWJo5z4LEcpNSIKJ7EeW4S9xT9NoHtmVtwanavo2ks0R-LuwT2FyEGae_4osKfDb9E6lZfrkTW-UIN8QARmDDtj4w1PXvtDdoCkzxkuKtQ_opsaRrR7Lw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b07e212ab.mp4?token=VjnO234wxh6daJPQNbYnvgPnFRgHPeX1orh6SkdTFGEfr3EtKdOB6ZpWwxCvd6UVQjCkFgwETEGqQ1BQu2mBX-4csdJKYNp-kZU788OpYnUqoAMSrneN8Jlp1Zw8zJ730r2O-SyxibYgW7CjCQv-HDoBMv77JpFBv6bifD3WFPr0RWkK4X9vXI0lne3jRzb8zKbbMEILBSqVqjX7MGbV203yrFUCB8BDTsWJo5z4LEcpNSIKJ7EeW4S9xT9NoHtmVtwanavo2ks0R-LuwT2FyEGae_4osKfDb9E6lZfrkTW-UIN8QARmDDtj4w1PXvtDdoCkzxkuKtQ_opsaRrR7Lw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش لبنان برای برخورد با حامیان گروه تروریستی حزب‌الله وارد خیابان‌های بیروت شد.</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/5752" target="_blank">📅 02:02 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5751">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🚨
🚨
🚨
حمله ارتش آمریکا به اطراف تنگه هرمز  ‏فرماندهی مرکزی ایالات متحده (CENTCOM) اکنون تأیید کرده است که هواپیماها در اوایل امروز، 26 ژوئن، به تلافی حمله پهپادی دیروز ایران به یک کشتی تجاری در تنگه هرمز، حملاتی را علیه انبارهای موشک و پهپاد ایران و همچنین سایت‌های…</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/5751" target="_blank">📅 01:17 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5749">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UyuroYSm84yv_bPbmNd63rpmPEabSsHIu6cwsbZiyQ9I3QuwRw93AB6Km87MNz_7WhjrKcZbrFC9hWpRx2lIifgupG011WllnS5GyXI5dguHupdlnUO9nTi91jkHpC4H_Mu97zDKvyDp7vkUdoWTMIV6MhF5_3h2s9jOeKFOdE_uMCYMbQe7qLc7skGv691ajsYgwtJoERr97tv1135JmkLzG7zbUOcumXiJXKbu__vzh6Yc1BpbJKNkjfnbAxMx9yIv9QQbTDReQn-bORRa03PK_wi1G4gqzmT1EbTx2x4Cz2BWVpGsB6A7fL5KCjClwG8oiI39QQfZhTC3p5MKgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/farahmand_alipour/5749" target="_blank">📅 01:02 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5748">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BBKgyV5JgRse7NISZtdHe-4MQa-PYdoTzqKtfI59i4H4R7GYh89I6K2Cy-aTCuaZqhcyY4rTXizrX6wuehjsAYdB4goTI5xJ6Us1fDR3N0rmCOCd51qR3lncpnyiEzQrqxr0QJb7juUAnY4eoSyOWYjtqdIQGycvL3W2VqICKUGj1YfZ3td-V52ons2BqsoYC7wCiGCcbsZzdMq6hDH2yOKPrzYjmtH1eb4r9tPBriklgAR8005-Nk8euPNOnl8llSgE42suHI17d0EetDHBlO9_zdcLeHN_vcnoFbcTybocZpOteePd4WpQAf54aPjs1kZCn8e__3pFWWhu1FqlQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش لبنان برای برخورد با حامیان گروه تروریستی حزب‌الله وارد خیابان‌های بیروت شد.</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/5748" target="_blank">📅 00:59 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5745">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e245d71920.mp4?token=qVUPX7PJPvHo0SrCgiIT-GKF-IO_Zr_kV-mDzpF7hSRbkpRalkrvrgU_b7xDLJgXheXK2gWEm-Qv3qRutAnmyV0G6zOnqBZQhxG82dfoes3Ko4Kc0NW2y2LeLUpJ8Tewp9QGOSEUcdHYEDnpGzC3t7Jnqn-dO19xGKPpdMH7lUJ4dpA3mNjj17uUToI6AXM2StIfbRK-emmH2wKV40MtpsM_dZiH3yH9x_sgBcjHG1TIkEVPKp9mABCmvNllyjbdmr_kZmxqvulGY26Qks4jEt59_G1yJ3qszYjxN9o-PB07-4y9lwBBNQbfTUXI7JA9n5YZRT3mW_DBicm-XgFT2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e245d71920.mp4?token=qVUPX7PJPvHo0SrCgiIT-GKF-IO_Zr_kV-mDzpF7hSRbkpRalkrvrgU_b7xDLJgXheXK2gWEm-Qv3qRutAnmyV0G6zOnqBZQhxG82dfoes3Ko4Kc0NW2y2LeLUpJ8Tewp9QGOSEUcdHYEDnpGzC3t7Jnqn-dO19xGKPpdMH7lUJ4dpA3mNjj17uUToI6AXM2StIfbRK-emmH2wKV40MtpsM_dZiH3yH9x_sgBcjHG1TIkEVPKp9mABCmvNllyjbdmr_kZmxqvulGY26Qks4jEt59_G1yJ3qszYjxN9o-PB07-4y9lwBBNQbfTUXI7JA9n5YZRT3mW_DBicm-XgFT2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حامیان گروه تروریستی حزب‌الله
در اعتراض به توافق دولت‌ لبنان و اسرائیل به خیابان ریختند
بر اساس یکی از مفاد این توافق حزب‌الله باید خلع سلاح شود!
اینها مخالف خلع سلاح هستند! تاکید بر مبارزه مسلحانه با اسرائیل دارند! جنگ رو شروع میکنن و بعد سریع از همه دنیا میخوان بیان مداخله کنن برای آتش‌بس!
خب مبارزه کنید!</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5745" target="_blank">📅 00:49 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5744">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dsNSdu8fcV0g4erWGIszY4EVagpttTcwM5G6Cxfn8A_Vy14ec1d_9vRkaG0SAH2cqHnIHcHXzcgJrOLACXqJesMTHapkZeBXYAOVukPJrvNSBH3SySG5VtxavYVLqIN29B6_OAUH4sUpEQ355rZ8ExD9HOv77drreNfb16juSMRhrh8VTy6uXxFcQyfBqb5jPzF7eNtYR7cpoMLqhBdKjDYKPwBet6k93K6i2YhjybwTxFfjdjALjJLyeFmOECiBwIhI3c8lqCNlHtreNhQ4o2GTkVwdvACQ66HkUABYc_L-379BpRDakkS4paZgZNyqIK66J0-_1kty_gzdoG9Urg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/5744" target="_blank">📅 00:31 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5743">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PLEkZkFFfuWcD3qdk9Hskgt6fLTWGd39nRIqBRnBfVbngsLIyX0NJja_zGriQhsPSylEa554A2V6Uk4GqN63JIH-H03BLdAyNalhVu9rjEB5lLIx8IO62D_UFLmudSGd4EKRVQbBdMah_cet9wNyaXcL6HF4eEVxY_oI70vGdznDVDO_IS-NdfCI8_kluXfrukR41D03kekqr0zD0kvxhLQctQt_J2J_xtIT391347m8X3faaB_ABXWM3et9oK2-dbhMzVJa4_wiSWFCE7cTM-tvrudkyp5Zc0QWHZLnLoME1F-MxzNrAv1mqtuYWP64syw6Jl2iZUoKZ4L1jl7ttQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
حمله ارتش آمریکا به اطراف تنگه هرمز
‏فرماندهی مرکزی ایالات متحده (CENTCOM) اکنون تأیید کرده است که هواپیماها در اوایل امروز، 26 ژوئن، به تلافی حمله پهپادی دیروز ایران به یک کشتی تجاری در تنگه هرمز، حملاتی را علیه انبارهای موشک و پهپاد ایران و همچنین سایت‌های رادار ساحلی انجام داده‌اند.</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5743" target="_blank">📅 00:27 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5742">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac9a1f1d75.mp4?token=lfiqpFiySd1WCKHfV8ZOgK4sX6A8QvmSZLG7sOx698XMYMyznkKJjt_xfNPLyWVvbQejF_kTGRCiXD-MsDGORITCz7mBqbqsRcBC3vm7NN7rxLGYg2ymk4He9e0HTLpntk00mmFgew5SJgxXZKGEzWq47-4Icz5lmtLzPpR9Cw3ZMY7Lb1EYXS5BZq9jAIWonTCejRrbUD9o8RP6xKTLA7R_z0p3zkYSvA2LqVRfx3PIrR3QLmsxjsVS_8q5otii9-ufBM2kmyZsp3RiAea3bt461VvN2Inzxyw1aYhX54FmEZX9yHPB7RM7KgBadrEoLJrAu-SVZHszfiRVXOH48InWtcUozJVNl591ttO5GbbRgjWCbNO2ivzPEW0BoBgWXj-nnjmGWPOamBQbdvp8pv-GaV983Shp_VmeaS8xZlum_FekwLBa2ObXqJJvziXyiPdounQX_rSlNe4b0UdiMVmgG_y3YziOKSA4tZIjmwfrf2ylWvOPcSZNe4u8ON7uBBWacXC4a6zhI2JrldXz7JHHLSVzmF2D7NJyXzTcjIlIC--0rBU972QYeVe571P47voiNbazb4C_nLk0s6cJn6TBUH1QbtbTodVNZov1UDvPkaCtko1FKuIZECF4dqmxsjZwpYMG6Hh3Ql33LlcC-w_OlEFogyxCnw7kF2RbdSE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac9a1f1d75.mp4?token=lfiqpFiySd1WCKHfV8ZOgK4sX6A8QvmSZLG7sOx698XMYMyznkKJjt_xfNPLyWVvbQejF_kTGRCiXD-MsDGORITCz7mBqbqsRcBC3vm7NN7rxLGYg2ymk4He9e0HTLpntk00mmFgew5SJgxXZKGEzWq47-4Icz5lmtLzPpR9Cw3ZMY7Lb1EYXS5BZq9jAIWonTCejRrbUD9o8RP6xKTLA7R_z0p3zkYSvA2LqVRfx3PIrR3QLmsxjsVS_8q5otii9-ufBM2kmyZsp3RiAea3bt461VvN2Inzxyw1aYhX54FmEZX9yHPB7RM7KgBadrEoLJrAu-SVZHszfiRVXOH48InWtcUozJVNl591ttO5GbbRgjWCbNO2ivzPEW0BoBgWXj-nnjmGWPOamBQbdvp8pv-GaV983Shp_VmeaS8xZlum_FekwLBa2ObXqJJvziXyiPdounQX_rSlNe4b0UdiMVmgG_y3YziOKSA4tZIjmwfrf2ylWvOPcSZNe4u8ON7uBBWacXC4a6zhI2JrldXz7JHHLSVzmF2D7NJyXzTcjIlIC--0rBU972QYeVe571P47voiNbazb4C_nLk0s6cJn6TBUH1QbtbTodVNZov1UDvPkaCtko1FKuIZECF4dqmxsjZwpYMG6Hh3Ql33LlcC-w_OlEFogyxCnw7kF2RbdSE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اگه خورده گرفتن که چرا میگید سگ هستید …</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/5742" target="_blank">📅 19:53 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5741">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fad365bb7a.mp4?token=ZDr-STvQFPYHiROFw6OPE7okjr7IEHAwGcDfqUYyBg4k0-Dvk9qRQIKcE5xG2aewUJ912dVo_83a_jiYAwUcvSQphHICVJSnFHRCEsILiVyq2xA7qkuZr3bk5_ki9cNSYAuQW9RXOvqhjOSU2zL83IZYkxIZ15AIiPW56JRm1EuZ3RUKct9SeWjS-LFiZfgVlvHezTVkjslzw-S6Ybnjf4E8HQGRf9U2lczcyRXgE_g6QFYzHZV-PLIL5FT8yd0mL40Sp7E4N3lG-LybSPWDd_qpdQBnRXlbNlM4oOGZPr3XikHkTMJCVShwXA1Nnrb6TaFoTfgoL74RMT_P6d5E6zNW02V0mAbLYr2D2PFWrCUtuYLOoHRqrYgk0gIX-uJQd0Q8VHStAcX7RxU1tdCi-pP6pgoF73LsZHM1SFU5tMJTDM1nPSQt-wqe8uPMLb_E4bduW7eq2ge88f8zaWg5acGI9vpE1zWVc0nt1dnqmGqsS3GAA8K0QiT55EzHpfDooZ3Q-2cZ8UzzuIv4pxqjSyqkMWZVdNiB4RJhYUTBwJV8hg9EGnzMhZq9C5WjA76VdmqdWQEHtWMUfYThLzP0HMaXuMhbW_U04HMNzvI4dcZsceHl5uCrmePcIrFomzQSrEP-O_iGPXysU1Q5AQMtkuW5Gd3nqbyzZkBK9cXW3QM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fad365bb7a.mp4?token=ZDr-STvQFPYHiROFw6OPE7okjr7IEHAwGcDfqUYyBg4k0-Dvk9qRQIKcE5xG2aewUJ912dVo_83a_jiYAwUcvSQphHICVJSnFHRCEsILiVyq2xA7qkuZr3bk5_ki9cNSYAuQW9RXOvqhjOSU2zL83IZYkxIZ15AIiPW56JRm1EuZ3RUKct9SeWjS-LFiZfgVlvHezTVkjslzw-S6Ybnjf4E8HQGRf9U2lczcyRXgE_g6QFYzHZV-PLIL5FT8yd0mL40Sp7E4N3lG-LybSPWDd_qpdQBnRXlbNlM4oOGZPr3XikHkTMJCVShwXA1Nnrb6TaFoTfgoL74RMT_P6d5E6zNW02V0mAbLYr2D2PFWrCUtuYLOoHRqrYgk0gIX-uJQd0Q8VHStAcX7RxU1tdCi-pP6pgoF73LsZHM1SFU5tMJTDM1nPSQt-wqe8uPMLb_E4bduW7eq2ge88f8zaWg5acGI9vpE1zWVc0nt1dnqmGqsS3GAA8K0QiT55EzHpfDooZ3Q-2cZ8UzzuIv4pxqjSyqkMWZVdNiB4RJhYUTBwJV8hg9EGnzMhZq9C5WjA76VdmqdWQEHtWMUfYThLzP0HMaXuMhbW_U04HMNzvI4dcZsceHl5uCrmePcIrFomzQSrEP-O_iGPXysU1Q5AQMtkuW5Gd3nqbyzZkBK9cXW3QM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همین‌ها رو یک تلویزیون غربی پخش کنه، سریع میگن این برای اسلام هراسیه!</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5741" target="_blank">📅 19:50 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5740">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">ترامپ در شبکه «تروث سوشال»: «جمهوری اسلامی ایران دست‌کم چهار پهپاد انتحاری یک‌طرفه را به‌سوی کشتی‌هایی که از تنگه هرمز عبور می‌کردند، شلیک کرد. یکی از این پهپادها مستقیماً به عرشه بالایی یک کشتی باری بزرگ و بسیار گران‌قیمت برخورد کرد. کشتی آسیب دید، اما توانست به مسیر خود ادامه دهد.
ما سه پهپاد دیگر را سرنگون کردیم.
روشن است که این اقدام، نقض احمقانه توافق آتش‌بس ماست.»</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/5740" target="_blank">📅 19:23 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5739">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/726fb491ae.mp4?token=KvE8G2PLEanRG8OzpSFPWgcTzgANstnH8NNAq6B2GzM-Znx5zjWaZW7Elu_70WUVCDuJq1kcpmGUHwWskUwHvDWQYLbvdz6fHVjPcOcqQJAbxWUZs7cp-yy25MSSW8iimT2ft2KHPAxw2IpDK5XPrdMqOomm5eAfC8BZa-Fg9kRNEXM1kizQsfUbo8duEoEiU-Fa-DNRU9KSTj2vHYhNOB9zP6ubomHewz_FBGh-_yYLC2L9HSyeE5xtrT_cQn2EmwxUK78ViUHU040BfFF5HqH9pErGGWyQ-NzJdJjg_vToZYtGeJyzMJDDIvgLz0HdWD0iFwtIxduOtopzzPg-1Ii-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/726fb491ae.mp4?token=KvE8G2PLEanRG8OzpSFPWgcTzgANstnH8NNAq6B2GzM-Znx5zjWaZW7Elu_70WUVCDuJq1kcpmGUHwWskUwHvDWQYLbvdz6fHVjPcOcqQJAbxWUZs7cp-yy25MSSW8iimT2ft2KHPAxw2IpDK5XPrdMqOomm5eAfC8BZa-Fg9kRNEXM1kizQsfUbo8duEoEiU-Fa-DNRU9KSTj2vHYhNOB9zP6ubomHewz_FBGh-_yYLC2L9HSyeE5xtrT_cQn2EmwxUK78ViUHU040BfFF5HqH9pErGGWyQ-NzJdJjg_vToZYtGeJyzMJDDIvgLz0HdWD0iFwtIxduOtopzzPg-1Ii-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قمه زنان امام حسین رو چرا می‌برید بیمارستان؟  بگید خودش شفا بده!</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5739" target="_blank">📅 19:16 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5738">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e184bbb012.mp4?token=NSoxYogYVsfnZCOLNN6cZo9XVb1F5UeC8nOFaXAqgsDabuzCeRvevBSVF6rDoDdnMApt00rJxmsx_eI2mErfbDduDqT8tsOmflUmqDoer0c5qACUaDfBMShjvz74cGkVYUeYSChBOdToHIu07kG7iGwYqRXZaemW_FpXJjYYYuma1Uf3p7ErZfjBb0ZyccNpKuSAKOFzOVEgBGqfO1E539MRRojqp0EG2zNr8dUNNqutntqKLUMuDB-4XujlrcLB7VTc1ON3tY3MWBZ76XJ2vvgni4HuaMLznMSICTy58ppF4ZJtxk90dcjiu6PM3nBUYjYp-CgOVmNOQOEFkMJ8JQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e184bbb012.mp4?token=NSoxYogYVsfnZCOLNN6cZo9XVb1F5UeC8nOFaXAqgsDabuzCeRvevBSVF6rDoDdnMApt00rJxmsx_eI2mErfbDduDqT8tsOmflUmqDoer0c5qACUaDfBMShjvz74cGkVYUeYSChBOdToHIu07kG7iGwYqRXZaemW_FpXJjYYYuma1Uf3p7ErZfjBb0ZyccNpKuSAKOFzOVEgBGqfO1E539MRRojqp0EG2zNr8dUNNqutntqKLUMuDB-4XujlrcLB7VTc1ON3tY3MWBZ76XJ2vvgni4HuaMLznMSICTy58ppF4ZJtxk90dcjiu6PM3nBUYjYp-CgOVmNOQOEFkMJ8JQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قمه زنان امام حسین رو چرا می‌برید بیمارستان؟
بگید خودش شفا بده!</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/5738" target="_blank">📅 19:09 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5737">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tDPrdJAqnn2F7Z4QjkBHDgkrV-by7giEAv8dD69c6pnLYHbEwvASzqBy3zw-HRNbolTZ3OE9Y0vlWVP0VDtXDEbYXYndBUsRCHUliXduinlE6dcT_bI05YcTbGMjILvxm8Boi3RBJ5tojQmYreUAv_EtLMjd8P1Da5qsQikY4zV1fp2neo_iSCQ3ZFv9cqsJt4gyPjSCgwKsDW-rxONpmoy4mpm10D2ACs8NYaJou59gKYdHR1B6oCzODwY5UsCPhLGxwhvzWjzQOCfiKeBHFHPAtg3qOsI5-I5WY0YsnKEhN-P4Uzk1-hdPpgOmFMHJCqA47CHnCHzNAoZ8nO0HLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیام فارسی وزیر دفاع اسرائیل خطاب به قاآنی فرمانده سپاه قدس
آماده‌ایم کار را به پایان برسانیم.</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5737" target="_blank">📅 17:53 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5736">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">نحوه اعلام خبر کشته شدن خامنه‌ای
و عدم تعطیلی مدارس</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/farahmand_alipour/5736" target="_blank">📅 16:55 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5735">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iXE1JFtcK4kvz7n6sbHp925cD6LrDqW1S3B0S-K_0vNYeAuEDRgWbBxF1rMvCUdjPXyTyygEqkqiOO25ev6GLDEDTkS3ynaP8qDmFV_Lv7mWtWIQP6AqC4YAWtJqa3BLPMzSMXHtT4x5YCvoKobsTkS-2E6QfGEGU4ot7psec0zuam9pOgVMdMmQMPfQ5UXeWqXnroLhGU3D8Vayj-oBuINarQzBdTuokVvEU_8j3T79dawRQR4ad6g0nb1SjK8xVfC_jgU9X8lyxbmmUKUe3BiukBLys1yk8C4Gw3sueze5yN67lRS0tIHdS9y8t3j01-U5Ynlj2XUL__w83iF2-g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/5735" target="_blank">📅 11:38 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5734">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cYsgdCfVBmD24Z7PDjHAH7UFhWtbtYKaJv44GKzvMmmeBQ311XJy0Cp7cfDyN-09bsQCQsZMjJsoYjpiVzizO4iLUnkU_zVXKiZnnIqPh_5buaKr78g4fkEJyZatpjtyDKZE46hYkn_F71GMG0pa192Rhy708GIlTuHoS1nU2K70mxzfM8ZDxx3c46mNfeof2eLrQzRFB12XwNaPiIe3mwILJuc-JwXI7GyZUg3hswhTmVpuHUEqmM-mP0ObHYpOY98b5NfsSji861I33MF_MfAFS1kKJSaN6AKoa6xHBlC7Y9MheibK0XjyUizNXRErCuAkGz_sevPP2g_PcSxzBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر علوم جمهوری اسلامی  در ترکیه،
خامنه‌ای را از اولاد حسین عنوان کرد.</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/5734" target="_blank">📅 22:29 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5733">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KYkZ7qkvki8RyYtTV0sMUVEn9qXstNQpoedl2te1RHGg1xuDxyWTNCknkISR7hz9w7CJ_iSsc14FXcidMOkyiTeI3aCosO9QSOaLqpwNAIzv-tJHc1-cdRWMDB7QzzhBkYnQ0Cm03ijO3JoqopXgWzKo_-2UvJHDLqGnUZGReOlCsWGVla7db2AiGfGstTdyy4mpSOmgIPyNSchugKDPWNuJJY2SSeBv-gdi-l4vUQfVV3d6TvKicH6k_OKMXM-vUCj_hZ_UqiKNSWJw_DLpEo5Hyooa1AkyyHm6cRkKIaJxRS-yHSoXB4LdoHpk6vFzl1MVEron1y7wxAczUJHz7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسرائیل به یک خودرو در نبطیه در جنوب لبنان حمله کرد و در نتیجه ۳ تن کشته شدند. مشخص نیست سرنشینان خودرو چه افرادی بودند.
صبح امروز هم در جنوب لبنان یک سرباز اسرائیلی در جریان حملات
حزب الله کشته شد.</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/5733" target="_blank">📅 18:23 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5732">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mpl-eB_J4lJ9wfwjz0-TxiRzwI84RcorUU6c47CVRCdf14KRCgOrfZJTOrNCz6r9AgcJIqMa3CcJDsqqWg4w0jS6g_v7p3zoJbNFNxxqDWDvAHdcEUJJZTceNHYuGUqBz2t6RvFiUr3CHrC3Chaj3KWLxcRgL7Bibn4-fst86Z0YW_kxpGpml5xDTta7_XGmdD1aIYt6Bv45vDWTIzGr26clvwxcIin9KCaCiCENnlU2os3345nbriJPsGRP96kxewHz3R00Mzf3O0GIPc_6PfW_1jTHpZvdwLGsJl-vEoJCUGB86cuegWnQ6c8VNNY-WDuXqO1M-YwGVEad33XNAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صد رحمت به اهل کوفه!
لااقل به دینارهای طلا فروختند!</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/5732" target="_blank">📅 15:21 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5731">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIran International ایران اینترنشنال</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6715f87786.mp4?token=NdWvANzZQ7Ox5iCnBA96ur2zNW-eNrr2ObdBVI-oYT501ezLKutjr7HzHTzKpCrXLKFW59rM70T9XOkwNw7U1OP97mMymNSS_7_glnlxyjYMyZs4iUaSVAE6q_SMaTyslcG0sWAi_5Bm2CWkcFdxErumV5S6g2IED7_MEYgU_BwrIDbNRkiw_l3tXATqx398jtwIQXN6efUnC31lJnVATQCBs_st8i6XpYqM5L5Bk5RnVjpNPPk3xXoH9pbz7IRJTTlB6I14CMpfrxi-3TA5GxTrTuhCFxvC_IfzcAX807GLrI-r0xcJDwKSfUTAu55xl9kvB_OHCW78zlTj3FYf-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6715f87786.mp4?token=NdWvANzZQ7Ox5iCnBA96ur2zNW-eNrr2ObdBVI-oYT501ezLKutjr7HzHTzKpCrXLKFW59rM70T9XOkwNw7U1OP97mMymNSS_7_glnlxyjYMyZs4iUaSVAE6q_SMaTyslcG0sWAi_5Bm2CWkcFdxErumV5S6g2IED7_MEYgU_BwrIDbNRkiw_l3tXATqx398jtwIQXN6efUnC31lJnVATQCBs_st8i6XpYqM5L5Bk5RnVjpNPPk3xXoH9pbz7IRJTTlB6I14CMpfrxi-3TA5GxTrTuhCFxvC_IfzcAX807GLrI-r0xcJDwKSfUTAu55xl9kvB_OHCW78zlTj3FYf-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیوی ارسالی به ایران اینترنشنال نشان می‌دهد که صبح چهارم تیرماه در همایونشهر اصفهان پرچمی با نام‌ها و چهره‌های جاویدنامان انقلاب ملی ایرانیان برافراشته شد. بر اساس روایت رسیده، این اقدام «بدون ترس و با قدرت» در جریان مراسم مذهبی «عاشورا» انجام گرفت.</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5731" target="_blank">📅 15:20 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5730">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/afaf9624af.mp4?token=jfjTA_8Iz8OngWN5ih-8X-HNyD0XCOt08wd1VkMQU-xr1Eo-x6zSb6wzPajXdz4oqpESfxknht1FGmDVpG0ESIr6HoR-ezpiwmydvjo33-Sabp689I6YBcsqB2Q0JEjr1UuHju4soJh0pbLbVPB0E40dbIa1FE0IF2WPZKUeClK-UP1wZD5Ro63kiHZvhsIUk2Zw_RSiFK3xzizdc6gzb19s_40g1N6DQNOUAavH8wJ34TJTqY175-G4jGWmouZy0Pz314d4_3-BOhtyHDNHymvFRL__HzEaKM9R8zjOi4_L3hAo1giiKwOYVS579TVb9Ldz7j8g1yqMLFvug5avqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/afaf9624af.mp4?token=jfjTA_8Iz8OngWN5ih-8X-HNyD0XCOt08wd1VkMQU-xr1Eo-x6zSb6wzPajXdz4oqpESfxknht1FGmDVpG0ESIr6HoR-ezpiwmydvjo33-Sabp689I6YBcsqB2Q0JEjr1UuHju4soJh0pbLbVPB0E40dbIa1FE0IF2WPZKUeClK-UP1wZD5Ro63kiHZvhsIUk2Zw_RSiFK3xzizdc6gzb19s_40g1N6DQNOUAavH8wJ34TJTqY175-G4jGWmouZy0Pz314d4_3-BOhtyHDNHymvFRL__HzEaKM9R8zjOi4_L3hAo1giiKwOYVS579TVb9Ldz7j8g1yqMLFvug5avqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گوشه‌ای از جنایت‌های دیماه جمهوری اسلامی</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5730" target="_blank">📅 12:24 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5729">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">اینفلونسرهای عقب‌‌افتاده‌شون‌ میگردن توی دنیا تا سطل آشغال کشورهای دیگه رو نشون بدن  و بگن ببینید اینجا هم آشغال وجود داره! پس اگه کشور ما رو کلا آشغال گرفته و به زباله‌‌ دانی تبدیل شده، عالیه! عادیه! معمولیه!   مثل همین حمید معصومی نژاد  که دیروز براش نوشتم،…</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5729" target="_blank">📅 12:00 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5728">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FsYliuIaDNiVoHyQVOllGsaIHA9PoyYi5l3PLHoqVguezepTPq-aXitsg5navYr2eab6wxzDgg2C7kyEIsjiJBbZN3g-RlSyNd4Zeex7qAsMVPxEUG1FSlYIXXksrOU4C19Q6Kb3ZyCNjheg_nqdLY1t42XM7DPaihKxLvVt9r3XMMUXZ312W39eyErd0pXodUURnPlvorUaI_iHxQ6A_23WAx4aUOqZXg4lt4a2m8yEqN1Ct3663ENKSuJla9mCHMvyEihMP4cRQXJuLBay_t2crysy7sBrJwnq7hRRWa2chszHk1gp4gc-jSWikYtLeU2HVACipVwrjzfDRwSNCg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🚨
یک سرباز اسرائیلی در جنوب لبنان کشته شد.</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5727" target="_blank">📅 10:30 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5726">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C9fKE26ZJNHIcF-VrjtmnweFG7-hCYeqCmsWGU7TmgUisRBTDkwdShbfRloIKJZSVPDIXTHhyZJZLhsTlMx0nwjv2_jIb8QzxaROGUOdnD5YYPd-247TQSbh-3sOlt_ezZYJyGHT79KuD7gK5tXNmTGkmU2e8wJl7K2UeKwUTNdG7ouPpiY_ivPTmQ2xJ8M3PPBCqg85T6ljGnu9nsRI49DRK1_x---cKEKw2hxMxzXot-8ivGMk2vQbf3v6CXjM5918pNFdogwtBdNgcAHzxh6mmcoL6SmdtyDZEwI-EA-lAghLascOJslPlBrsg_PX5RPk1lRmOC4lsPFFgoTTHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرمانده گروه هکری «حنظله» که در جنگ ۴۰ روزه کشته شد، ولی خبرش الان منتشر شده.</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/5726" target="_blank">📅 09:39 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5725">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/86c17f6d3c.mp4?token=Oxo-LV6hUej9kkahysjUerSksbn2Lp0zwLYz7UKIuSvKFg2Rdmnf6TQzRBWGq9gdfnHR7ZSkxty56nmFCMhQiQesoqNIke5She1c7pu7jIqS3nIDLVF94Xn2aLfUrtj7wzn7_NCrPoVJ8broBrSJe5ekCicuRTj-dngzdbP0gKKCH1iXR-9eLDwUE2nSIrSGZYw-UTuhJ0CSQsqmPVu82E--ekYfOZWjEXtQ3Xnrbb5LXaEdD62vJYQ-lkdJJ5YrrUCwPMyseU2_hMxc1WR-8KCVCN_QLM2N7kH7r8Vw0MsKSkbc5s-HLDRN6pl1Sp78pFt7aDZ0R5Yj_o1gcxVSKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/86c17f6d3c.mp4?token=Oxo-LV6hUej9kkahysjUerSksbn2Lp0zwLYz7UKIuSvKFg2Rdmnf6TQzRBWGq9gdfnHR7ZSkxty56nmFCMhQiQesoqNIke5She1c7pu7jIqS3nIDLVF94Xn2aLfUrtj7wzn7_NCrPoVJ8broBrSJe5ekCicuRTj-dngzdbP0gKKCH1iXR-9eLDwUE2nSIrSGZYw-UTuhJ0CSQsqmPVu82E--ekYfOZWjEXtQ3Xnrbb5LXaEdD62vJYQ-lkdJJ5YrrUCwPMyseU2_hMxc1WR-8KCVCN_QLM2N7kH7r8Vw0MsKSkbc5s-HLDRN6pl1Sp78pFt7aDZ0R5Yj_o1gcxVSKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ میگه جمهوری اسلامی خیلی رفتار خوبی داره با هر چیزی که من میخواستم موافقت کردن!
باید هم موافقت کنن و گرنه دوباره
برمیگردیم سراغشون!</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/5725" target="_blank">📅 22:56 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5724">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">وحید اشتری، فعال رسانه‌ای حکومتی :
تنگه هرمز شبیه یک بومرنگ برگشت به صورت خود ما، در ۴۰ روز گذشته حتی یک بشکه نفت نفروختیم. از لحاظ نظامی توان شکست این محاصره را نداشتیم.
گقتم تنگه هرمز میشه تنگه احد براتون!
به هوای غنیمت گرفتید، ولی فهمیدید باید دو دستی خودتون پس بدید!</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/farahmand_alipour/5724" target="_blank">📅 22:23 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5723">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/171eba79df.mp4?token=fwuRmmwuGZw-V-H7x1WAcmFXeJAjtmCDON3R5UhQ-7tOqJxB2iiGe-bnibPqs-ne_ZiGJYUTXmjQa3eLRePtlnUW_SvVEKVAsBJvXCeuy41CP5-zNOVkWCYHx3ugciQfqyhvfgSdE-2d5Mhe7NMBklRXpLKGWNw3flwr7LV_OMjOtEJZ6kJpxkCwUGOiN_67WqhxHqw4A7q0sx_Yt6b4QiWCJSyejm7xK1F6ZPCl7FTJRTSHiy6TScsJxDgqnubGwKqmNjkrP1ZDfhpbF4LWfaHg5WSPjI3jUtjRVhc4HmBF1lpNUXdq2gxnsyy23nj_5t21x33d60BXCFVXnhaRCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/171eba79df.mp4?token=fwuRmmwuGZw-V-H7x1WAcmFXeJAjtmCDON3R5UhQ-7tOqJxB2iiGe-bnibPqs-ne_ZiGJYUTXmjQa3eLRePtlnUW_SvVEKVAsBJvXCeuy41CP5-zNOVkWCYHx3ugciQfqyhvfgSdE-2d5Mhe7NMBklRXpLKGWNw3flwr7LV_OMjOtEJZ6kJpxkCwUGOiN_67WqhxHqw4A7q0sx_Yt6b4QiWCJSyejm7xK1F6ZPCl7FTJRTSHiy6TScsJxDgqnubGwKqmNjkrP1ZDfhpbF4LWfaHg5WSPjI3jUtjRVhc4HmBF1lpNUXdq2gxnsyy23nj_5t21x33d60BXCFVXnhaRCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قمه زنی گروه بزرگی از شیعیان در کربلا</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/5723" target="_blank">📅 21:46 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5721">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eK2BgbhbK44vz2SHzv9H27UnY1qyNcvP0fD9QuAbEoiAG23-JOncaRZAwI3RAFabWVgRZ3Tv076OH2d-fLb4r0ZL_H_f8hXKmj0sbbonm7eYjgn4AVxlAg4b3jCBIQnaFqdzoRWYEE6LKQGZvRq5w8mCUYuWsLu680GQhyYlOgX4PJ8td351DFa45BFuz7FJbJZCo241If0-52TdeaVxDlMdt8BPZBM_QBYthlAqxNieHjlJQWxkBUcjm6qxE_1Ku93vD4UVfQNNn2YM0rrAmnI-g8Xfr0fUvk7LZvtTt1ABNUy0dQU6SvE76lREtkSz1Y5aw6JqGGArb3ivL0m1oQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/5721" target="_blank">📅 15:52 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5719">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YzWUaNGrrcNY7ndJWsP60Jy6Xu2s39_hcoD9bvfGIUhFzghcPETUHYPIw6Eq7wfXOygYsXLfjIgT5SjW4bfrGEVOj3Ab6oA-ayLfV2DLBi-vIwbj7AtGUeKds_qy6yQlEIr9cmKxgmKf9JkIlhKzinamE6lPeE49WJ7bpxNXmKjUgNlEUfpBoBN-CNWJ2etdidMUSt9W5wMRbRovtX-4TZrPB1zUXLt-P5N_9XwX5KHJrbwFct03nAy16YvLNQ2MGhlAJO1pmHoBawoHajw8KkIzl3ce349cKsMlHlWpG2BMQ1CitHnbr6WOgWz5QTm4UsTtT4c-IxEsUzMDfsjFUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Huh7DxCT_6trvvSGgMWzcU2FQbS7Xg_RagG3Ckq1qCoSnvrdOwi4soouovJr8NcKfMk4HQ0L_vx1LEp-AMjaTYIaFVV6BcOdLsvNlD_srfnpY9A-igJWUlKLsijzwSfe83wx8V123qzExcseI3gXUz4w0Yg0S-cIiFtI0lh2Uhj7vMT_mpaHTbA4otSd7TSzl1MNdEeEnrYNrFZNX6TqnX5IJuCSvAH8SoB0HLgiK7o0oMZdW6UUZ6b7w6jl7EJxiN_dr0F2GOiW2JtNpZ5PoH1GDsyy3rPrWYbyr4mdazayvTFIEZt9HKaYE8HicS-gzDA7sjhAcgLIZ8tp4cHaXQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دیروز تولد «آیدا عقیلی» بود
آیدا ۳۴ ساله بود که به دست جمهوری اسلامی و در جریان کشتار ۱۸-۱۹ دیماه به قتل رسید.</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/5719" target="_blank">📅 14:39 · 03 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
