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
<p>@farahmand_alipour • 👥 62.6K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-11 15:33:43</div>
<hr>

<div class="tg-post" id="msg-5835">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iJRkbhs9IbWoRZovuIbAdCL8RXSrfv_LsUrHECXlOyAb2uyCnEEv9ImGnUkRyGmvAC06Z2YVpGx7izQ-p_b2WD9xm-bTyR5IzbJa30aWfPj3lmO4UruESejP3oMsOJpBG7NLchPSl77nDA5NmHdAG5jEjqbm4o8iZQyOB8lfip-ciniSz7YpCk9ZbLMGfjSmj_rW69BB-5xaFhnYeIyVHfGFt8KxkjcULSzASE3rL-HTEk3EI1vda8CAZRClwHoNtnY5UOogMYIUFLiFLHvjQw7AKDT1iD_I28FYmfPpNWm07UmLfMN-GmjQr4YYQyUOtDqs0B-TrusDlkbR-DeOtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/farahmandalipur/status/2072405978012844407?s=46</div>
<div class="tg-footer">👁️ 3.74K · <a href="https://t.me/farahmand_alipour/5835" target="_blank">📅 14:35 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5834">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YYpS2AGyOFJVNJHDIntWcTTBzu3PdjdY18dppzEwL1jCxfGZv6syisx77E5hiMHQEPYnJtUTSN9gZXYvTd177TsveVJqvA0LGWivRTQChf1q5mzc4OG542pY63Y5_CSOZgNYufdzZz-B3Yd_U8TlsXDG9NEsdRvjAQnl97Cgtu2iWJI-GYu-Fbcn96_Ol_EWdmmJwESqGPryWonkVcZphsPFW_ju0RB1ZI5L3FWhEzAHL0zhw5psoQPDc1xzjYkbeyqPUNtH2cw3TGnubrI2qyZJVsAmo5TIr4H1iisaf-1ECwLlTi1o6uFduvMAV5l3KqysaEt2kONB3pF3l_-EKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چرا صفویه به این کتاب «روضه الشهدا» اینقدر بها داد؟؟  ایران کشوری است که عمدتا در جغرافیای گرم و خشک واقع شده،  قحطی‌ها بسیار زیاد بود، فقر گسترده بود، جنگ و ناامنی بسیار! صفویه با گسترش شدید مناسک‌هایی مثل سوگواری  برای محرم و قمه‌زنی و گریه‌های شدید و…..…</div>
<div class="tg-footer">👁️ 9.43K · <a href="https://t.me/farahmand_alipour/5834" target="_blank">📅 10:48 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5833">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B-6p8jGj_erqIzymuNNH7CqkXx7WFj5Q67dTmM0GBCBTeKO2JR06nEfkRn9O--Fj-ljU-O-lSSsZBWprk3mezHBDePIVi6ZjUF3FZURIId_wEl9OlAYkOpwlELJFhxj4DgcLBTxFZrFoOlFTdV4VSGqmuYJ0tj1Wx54wQ-ALKBxgXghOtmRcN-gvflFwaXBQRoihdZHMEZEEmZVsOiI8TqnmgyXs_L89XSsfht6uupp8xnV-1Iw5xVqdMeBTBmYb6za4XWJr5VUiSDnX9nfo4nHs82iiRl17m8SqKxXsUqbeAqTY3PETy5hS2adcg-GXXnROgf4GmPAdS_AWJqIHtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خود خامنه‌ای هم در اسفند ۸۴  یک سخنرانی در جمع روحانیون در آستانه محرم داشته و گفته که باید روی  «گریه» و «احساسات» و «عواطف» کار کرد!  و امر میکنه به «گریاندن»!  چون روی همین احساساته که به قول خامنه‌ای فضایی ایجاد میشه که بتوان خیلی از سیاست‌ها رو پیش برد!…</div>
<div class="tg-footer">👁️ 9.05K · <a href="https://t.me/farahmand_alipour/5833" target="_blank">📅 10:42 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5831">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VZKiyY-aTp0qDEKrp6Yrrqa54CWEEkg5V7dIZrjj1SRcHW-wGLJ9xc9Nz3dP3nVQw9r3RH68-cRAaIg-ffBOPlUwaftTKPrTf0r3o5KurJrpTOCc4LOBslM5TKEz7XbKDZJv1FeI4oaTTf5JfLNDGtQ-XjMI5g7VmBjOsI37QepOpewMYYgfwIz6HdwIasc8nyqHBHrypuSS7IbalJdUWBwmI2Dd18MMGr5Vvb1q6k_SsGw5-wGuEXJT0OA131dZ1haGl7dyMrFf-eh37JwXLCOEE-ddBazRIvzf99d0X0D3ims1q_VAJDVh7SMPfrmr5xJmXe9DDHHhaivLJNYdIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KJyICSScG8w5gh4zHFUwgeBMPU78Ocf3sPu_Oy7a8kmg8xJq_CVlElx0QDixCzfbNFcCHHRKMJeWxK7-Ptinzu0Z2PRp4NxiOhZj_BSQT3nrRxm3BmiD2Vj8liPfNH8SrTExP_t-muWmu05ULgg2aoXohpu69PLaN7x0A6Katy8_aaiEEVtoMMksasWxOp42smVKf23pScPC9Nj_jUr8veXI3ed010P1PZcn-4oahzw_A6PVdXi3bhiKbx-vvqpWhrQer58M_uV21OI99eedtM3x_Qwz-6mVoF3hSep2OWpM31ovvP33L3NPhPcNTgvZj83-vsb62VPnGxtpWbCgiA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">نکته دیگه اینکه خود صفویان،  از فرقه صوفیان خانقاه اردبیل بودن که در این فرقه یک «مرشد» داشتند که قزلباش‌ها، باید با «شور و احساسات بالا»  نسبت به مرشد حرف شنوی داشته باشن و اطاعت و‌ پیروی می‌کردن!   این کتاب «روضه الشهدا» برای صفویه خیلی خوب بود، چون شور…</div>
<div class="tg-footer">👁️ 9K · <a href="https://t.me/farahmand_alipour/5831" target="_blank">📅 10:38 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5830">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EtohJesNZbSJmgFGg6BfdC2n4_8K8nNkEX_hgtwNsihYrqRbio9pkVAiC5zX-fNZJB6hC2vrooeuXqAFd9L8M8qt3mimgp-llY3SKQ_gUNOySYYAFEIcAyIqRp5zOkurtHiCnzLrq7erwAb41Kd_v-kyLSXTalerTCZ8lTyNEYuIkYTt6Nv_LOKZu8S_PV8KD6WUspY3yTLdP0gMx48LVXAGs1R-yRX3hnlN4Ey1Pi17aGlfGpCV8DHAW1fhGVXWvL4yhm_s-q9Bo022yCFvmJQAUvNNUw7yB-5rdVxHucLu5WcSQ6HW2XUlQGr0YHsT-CU8DZ4Jqws2Mkggb_pSvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چرا صفویه به این کتاب «روضه الشهدا» اینقدر بها داد؟؟  ایران کشوری است که عمدتا در جغرافیای گرم و خشک واقع شده،  قحطی‌ها بسیار زیاد بود، فقر گسترده بود، جنگ و ناامنی بسیار! صفویه با گسترش شدید مناسک‌هایی مثل سوگواری  برای محرم و قمه‌زنی و گریه‌های شدید و…..…</div>
<div class="tg-footer">👁️ 9.51K · <a href="https://t.me/farahmand_alipour/5830" target="_blank">📅 10:17 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5829">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CNTYxJ77ojeY7zQleopB_UcHLTvcFvN1qfGY2PASFcLVRp3SWs8BdFg4uEIH4F0s0x62vRuQq-TP68L1HvP15RPtIE07aWBI0w2gVXUiZG6CZCorqqIYkviaXKLkaQPU1cjKwL6ipRgexiYl5u2RmKLIRKePqAJN1s0Lc6G9mFzqCw_TE6yMFmqshVj0oub7iVMUGYt7hvFvoYazDI8t89eCdzc1k2hTzp6qy4U257xUNnqofz5pmmmLGUw8YGc_ZkMbSwg2TTMv31ctymPn_HAniifMH-keA-WqYf6Lpm_7Sdwzvs11bnDKjP9YVvczXNVLhH1M_dx7FF9xpsbOGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای با الگو گرفتن از صفویه و با پول نفت.  این خرافات رو تشدید هم کرد!  به «مداحی» و «مداحان» پر و بال داد!  بودجه‌های سنگین! تبلیغات گسترده از طریق رسانه‌ها از جمله صدا و سیما،  که این‌ مداحان با خوندن همین دروغ‌ها! احساسات رو به نفع حکومت مصادره کنن!…</div>
<div class="tg-footer">👁️ 9.54K · <a href="https://t.me/farahmand_alipour/5829" target="_blank">📅 10:06 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5828">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QfvVUcn0nncvG0HoZzOuLrTxwkAP-ZoM3mdCktSzHWlwyiI00K6qwEpvDhrq6E-ejROreuxedUXZYNl-3Q_7-ChSUyb9rRsdxmgtV2hr9bEnPjw1kCdYufWBKc14DerjipadA1PgSzwAf3AQBhQoq_0EOCBAkCaIQ74LEmKFaMSiW9KapYXbGx6RI5vqSML1eEgBnTr5SB5Wnc8YYqed4PU9CSev6SCLyu0ztjxOW6aX9ouXRisxhx3YLZxkcZ1QnFNiDV6DcihXbCWrkc3SIcjUModRWVoTEqMqUQ8rgt7eNFv4AzjqW9GFcoXMUGT_uEF4jaWJTbVddu7AP1x_Ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مرتضی مطهری در یک سخنرانی عمومی  کل این کتاب و داستان‌هاش رو «دروغ»  و افسانه خوند!  گفته از خودش نوشته شده!  کتابی که داستان‌هاش صدها ساله در ایران خونده میشه و براش گریه میکنن!!  کتابی که حکومت خرافه‌پرور صفوی عامدانه ترویجش کرد بین ایرانیان!  مرتضی مطهری…</div>
<div class="tg-footer">👁️ 9.96K · <a href="https://t.me/farahmand_alipour/5828" target="_blank">📅 09:56 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5827">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">در زمان صفویه کتابی منتشر شد  به نام «روضه الشهدا»  توسط «حسین واعظ کاشفی»  این کتاب عملا مبدا روضه خوانی  و ذکر مصیبت در ایران شد.  و اصطلاح «روضه» ، که امروزه برای ذکر مصیبت و گریه به کار میره (در حالی که اصل معنای واژه، به معنای بهشته)  برگرفته از همین…</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farahmand_alipour/5827" target="_blank">📅 09:41 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5826">
<div class="tg-post-header">📌 پیام #92</div>
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
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farahmand_alipour/5826" target="_blank">📅 09:33 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5825">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e54b01c817.mp4?token=EUkl6ZftdcjVAYUPk6zo5BlTUuUNZpkql8lv7lyL9vWuDHjgo36BUoBkJ8n0vF7G5iGemZO1xOfcUtFEKpE66PqNEgkAUjunbg27Uhpmitk-ExQKrRdqwkL4H6SNkiauzYUMcyAoZ5msdi7khcZFGagbww0PBPQQpmGwJbmZdOZcJ1A5DRBGzK9DeYKUbtQCxU4u2l5tSO-NBBqdYJFW6OhHUxrvyPKhrC-YNfSXTqO7ljHjRSgwjv3nEEaI4Nqoj_RYZbwfQOgMsMqk1k3Ik2elJliisby7wE6yXRsSORGgsptp6qow6MQ75h7smGXS4ZU66sdglxdNZ_A7VbIv5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e54b01c817.mp4?token=EUkl6ZftdcjVAYUPk6zo5BlTUuUNZpkql8lv7lyL9vWuDHjgo36BUoBkJ8n0vF7G5iGemZO1xOfcUtFEKpE66PqNEgkAUjunbg27Uhpmitk-ExQKrRdqwkL4H6SNkiauzYUMcyAoZ5msdi7khcZFGagbww0PBPQQpmGwJbmZdOZcJ1A5DRBGzK9DeYKUbtQCxU4u2l5tSO-NBBqdYJFW6OhHUxrvyPKhrC-YNfSXTqO7ljHjRSgwjv3nEEaI4Nqoj_RYZbwfQOgMsMqk1k3Ik2elJliisby7wE6yXRsSORGgsptp6qow6MQ75h7smGXS4ZU66sdglxdNZ_A7VbIv5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">روضه خوانی سحر امامی در شبکه خبر</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farahmand_alipour/5825" target="_blank">📅 09:09 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5824">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/43703b5179.mp4?token=nJIojmQXwvhDlyNAcV0qRwjUwwNjXVCQfVBg6AKqn1IQogoaHs5iIn5Z4Z5UoOo1nTfcW6R0ZPdu0BRGFcWyrwSuqzrKqc-8_bnWaFLbXtBADrW-26qv35K2X0eDkWQPTLAq_B_YRFXiBNYZefnXX6-K2uBY3hk9xqImUxULcDPOoCBv8yuzevVU95BHkPveR1EIjNk9sSizqBvcWnqtS9wb_3wPtLKYgpUU0tFd8YCXlqmMS2ETBjALrYzJKU2mQEV_GFDW-rocRAdmsFL139ruNi9T5RDphFA3SKFkczRCC0JaEmRXrB2txaNRZKAUpKxpINqvjvG2LqGjAO3Q-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/43703b5179.mp4?token=nJIojmQXwvhDlyNAcV0qRwjUwwNjXVCQfVBg6AKqn1IQogoaHs5iIn5Z4Z5UoOo1nTfcW6R0ZPdu0BRGFcWyrwSuqzrKqc-8_bnWaFLbXtBADrW-26qv35K2X0eDkWQPTLAq_B_YRFXiBNYZefnXX6-K2uBY3hk9xqImUxULcDPOoCBv8yuzevVU95BHkPveR1EIjNk9sSizqBvcWnqtS9wb_3wPtLKYgpUU0tFd8YCXlqmMS2ETBjALrYzJKU2mQEV_GFDW-rocRAdmsFL139ruNi9T5RDphFA3SKFkczRCC0JaEmRXrB2txaNRZKAUpKxpINqvjvG2LqGjAO3Q-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farahmand_alipour/5824" target="_blank">📅 08:27 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5823">
<div class="tg-post-header">📌 پیام #89</div>
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
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/farahmand_alipour/5823" target="_blank">📅 22:52 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5822">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad33cb95d6.mp4?token=fJmyzrsMTEmfYg_rMFPn0Ixn8MTnBtAu658X_H3B2GgjFg1-z26rZdrknyz52DkUrTn5TN-fK20rdloKGq4Ohh7UNt4StDLaeZ9_GU36Waig4_lBAvuS7I6GviSBcmb4KWJiQepjpV9dhLLIgkTulpugjVunI2_6SSFsH7fYaofSRIoszhxrTO-dfW4gXUSFU0PudgFxJokIqBp_Brof6wpOjFQ-rLMXOlo4OHAS8fwo53mACjK8ibfUz0PxxOe4h_mquukU8liulEiGtUEkxzU6uQQBP4z4SpYqDD_JqQXrUOmS7GGsVd_hUMZLFKG9W6wPAPUcvzFifND9Ot1fig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad33cb95d6.mp4?token=fJmyzrsMTEmfYg_rMFPn0Ixn8MTnBtAu658X_H3B2GgjFg1-z26rZdrknyz52DkUrTn5TN-fK20rdloKGq4Ohh7UNt4StDLaeZ9_GU36Waig4_lBAvuS7I6GviSBcmb4KWJiQepjpV9dhLLIgkTulpugjVunI2_6SSFsH7fYaofSRIoszhxrTO-dfW4gXUSFU0PudgFxJokIqBp_Brof6wpOjFQ-rLMXOlo4OHAS8fwo53mACjK8ibfUz0PxxOe4h_mquukU8liulEiGtUEkxzU6uQQBP4z4SpYqDD_JqQXrUOmS7GGsVd_hUMZLFKG9W6wPAPUcvzFifND9Ot1fig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حرف راست رو از این خانم بشنوید که میگه بعد از انتشار خبر کشته شدن خامنه‌ای مردم در‌کوچه و خیابان‌های تهران کل میکشیدن و‌ دست می‌زدن.</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/farahmand_alipour/5822" target="_blank">📅 21:52 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5821">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a22e78d39b.mp4?token=FarxS6zgpjZbJtdjVKsI9PYgizVHgSdHTRQkkHiVO1uiiEyFskU0N-Rdx88iIw6GUtGQumGrL86zi7yK7WO4CaVsDDnRWOejKWDSfJOHFxXQy0Vpd895tyP7mTGh261_3VJqYcznM_vEvUM2O63enKKqRBAlMiw4E8IyPQaJFY_HAvTu6vwDCB2vtY71JarmLXp3l32UoGp--hQWkEugyvx8_-kt3OJCz66VJmyCy0KkKt9X_Temnh3m4uuG1ALOTT3xV4Xhek2MMrZQvTue_PR-Iu6Y6V13t_21kNlw2bJIDOZln7eTOaejovHSZ9dboFgBQ_Pi5ylN81kygCjqJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a22e78d39b.mp4?token=FarxS6zgpjZbJtdjVKsI9PYgizVHgSdHTRQkkHiVO1uiiEyFskU0N-Rdx88iIw6GUtGQumGrL86zi7yK7WO4CaVsDDnRWOejKWDSfJOHFxXQy0Vpd895tyP7mTGh261_3VJqYcznM_vEvUM2O63enKKqRBAlMiw4E8IyPQaJFY_HAvTu6vwDCB2vtY71JarmLXp3l32UoGp--hQWkEugyvx8_-kt3OJCz66VJmyCy0KkKt9X_Temnh3m4uuG1ALOTT3xV4Xhek2MMrZQvTue_PR-Iu6Y6V13t_21kNlw2bJIDOZln7eTOaejovHSZ9dboFgBQ_Pi5ylN81kygCjqJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">میگه خامنه‌ای وقتی کشته شد امتش ریختن توی خیابون بر سر و صورت میزدن  ولی دروغ میگه :)</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/farahmand_alipour/5821" target="_blank">📅 21:52 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5820">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/256cc521e9.mp4?token=HHocNLqPVi8CabV33iE6qhkEZcdwdKu8xOzgj0sVNWNYQkEMxHTzZOEPjFtB8R6zgrNwrwDlzKCG8731c9pDP63fwsZXXIp54ql2u3ZJbmL2uR9sPVmQZgWhmgsCpASl4OO-umJRWXN5X9rXHo8y4YvagG3EmuuDoXHBXCUpEbB2mPeiwqGAGggKEHMkiH_SXjx_66574fxQZu8-BW08s4GykFLy_cQR-ZZkAeA1aMkfDxU4ujz0fh804VtZkOEO7uJTa82bVKxlqh68X8VnBXnZWCPW4O9WBjmRUgs2R58W14qz3WiT3sHHJbfuSfNcKGSG4XpPMLizpi3_tNsZDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/256cc521e9.mp4?token=HHocNLqPVi8CabV33iE6qhkEZcdwdKu8xOzgj0sVNWNYQkEMxHTzZOEPjFtB8R6zgrNwrwDlzKCG8731c9pDP63fwsZXXIp54ql2u3ZJbmL2uR9sPVmQZgWhmgsCpASl4OO-umJRWXN5X9rXHo8y4YvagG3EmuuDoXHBXCUpEbB2mPeiwqGAGggKEHMkiH_SXjx_66574fxQZu8-BW08s4GykFLy_cQR-ZZkAeA1aMkfDxU4ujz0fh804VtZkOEO7uJTa82bVKxlqh68X8VnBXnZWCPW4O9WBjmRUgs2R58W14qz3WiT3sHHJbfuSfNcKGSG4XpPMLizpi3_tNsZDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">میگه خامنه‌ای وقتی کشته شد امتش ریختن توی خیابون بر سر و صورت میزدن
ولی دروغ میگه :)</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/farahmand_alipour/5820" target="_blank">📅 21:50 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5819">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ed6be978db.mp4?token=Mq-bcTPjzoOviHrwKgqre8iZP98zVqAL62SUwcn-4ZgIjvIvNF_AqmNTnuGoWVoSBhzjB3ulInQekp4DaJ7hExKFGXCIie35TO9LNsm638VY1QKI8y0f88JnHCUoju-gegeoo6UYwd_BcW95gXmxFRwAwtpBTzTZEKlfMBSBipjBNMaOysJ5jGQnV7TbtnHNaJ_Y8wy0uQTK6RNKzruuyLI28bDqjMBr8mCHFVjBaWcdQMxnlJjXRxKhDyfCWd125FU19T32etbiKAldPXKFiY10OXNmAAMw9DYTHcBQMSrTF-l0V4rbsVw_yZeWGNCaJxX5OnVkZJzyRn6PgSJEWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ed6be978db.mp4?token=Mq-bcTPjzoOviHrwKgqre8iZP98zVqAL62SUwcn-4ZgIjvIvNF_AqmNTnuGoWVoSBhzjB3ulInQekp4DaJ7hExKFGXCIie35TO9LNsm638VY1QKI8y0f88JnHCUoju-gegeoo6UYwd_BcW95gXmxFRwAwtpBTzTZEKlfMBSBipjBNMaOysJ5jGQnV7TbtnHNaJ_Y8wy0uQTK6RNKzruuyLI28bDqjMBr8mCHFVjBaWcdQMxnlJjXRxKhDyfCWd125FU19T32etbiKAldPXKFiY10OXNmAAMw9DYTHcBQMSrTF-l0V4rbsVw_yZeWGNCaJxX5OnVkZJzyRn6PgSJEWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به امید شکست و تحقیر یک به یکتون!</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/farahmand_alipour/5819" target="_blank">📅 20:05 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5818">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pialK1hk9HI2hstF9Bak8n6E24Whj9d9TY9oqsM3ZlOChJO8T5JClSiGEx8sM0ZbkgaSwZBljwne77_rkVaL6PG5maf9dsvVkCtEQFGzZxJRNExnNymIeaWCEGUxXjWjilHElaLgnKLYUeomOau7iUIkkYQG33exnYnW1j8rs0ps684fIcLFqje48DeOMgmFnN6HJtS-wXS2EjFto_rl5NEyOypP3nuWUE7GT9p_onMyz6SklOvuaBO1zmnlFqM6GJB5147mvItjtD2nJ367wB3yXDM9JirmJ-Zxo5B_IULXWHik0eA545yCEjx9aX-O4MD9uTuJBqDbjdBNzZVm3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/5818" target="_blank">📅 17:21 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5817">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7862dff401.mp4?token=uM5ZU1dLXBaDc7vcDrW2e_wuanDsWlVoKBe4NahKBWDAejduDkwsTsIqihRAGfhp7WaFYEqiMkvP04ju6XneDjGPpNzcz_fI5rD9lCubl9d2Jdac-9JMH9-614SJM04aZVq2wXfbrj_zjddo9QUPV8HrkY4wOWyvUn73RDxumOtT_yXskLT71jPXx81Rey9KHAjYs8GVKmZ8nYp_AKYfrrSy7AN-MwrxWp7uskm_Gxot5nYh6upzSI95ymwGuFCi91ht0SHFRmX_6pX71qhV6mcC21iLGdV_hqnZ8QutXMESneokbpnsDAsxj4088tQkSNbeykR-rtn4Fhy-DSY0rA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7862dff401.mp4?token=uM5ZU1dLXBaDc7vcDrW2e_wuanDsWlVoKBe4NahKBWDAejduDkwsTsIqihRAGfhp7WaFYEqiMkvP04ju6XneDjGPpNzcz_fI5rD9lCubl9d2Jdac-9JMH9-614SJM04aZVq2wXfbrj_zjddo9QUPV8HrkY4wOWyvUn73RDxumOtT_yXskLT71jPXx81Rey9KHAjYs8GVKmZ8nYp_AKYfrrSy7AN-MwrxWp7uskm_Gxot5nYh6upzSI95ymwGuFCi91ht0SHFRmX_6pX71qhV6mcC21iLGdV_hqnZ8QutXMESneokbpnsDAsxj4088tQkSNbeykR-rtn4Fhy-DSY0rA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جی‌دی‌ونس میگه ترامپ میخواد با این تفاهم‌نامه با جمهوری اسلامی،  بازارها و مخازن رو از نفت پر کنه،  و بازار سهام و اقتصاد رو درست کنه بعد تصمیم بگیره با ج‌ا چه کنه.</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/5817" target="_blank">📅 16:36 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5816">
<div class="tg-post-header">📌 پیام #82</div>
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
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/5816" target="_blank">📅 16:31 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5815">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🚨
نتانیاهو : اگه نیاز باشه به تنهایی و برای سومین بار به جمهوری اسلامی حمله خواهیم کرد.</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5815" target="_blank">📅 00:04 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5814">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/60c1fdbeee.mp4?token=uFLSuXOPZnZ__3He_2spLuuivD36_nEmfzRuaX8VwO9VWO6uBE5TAlE6htAHGNsfDysl1j4Z3rDANDB0r8aAaFRKRLcBhplHKQkHwOUjwQr94H5-4BvHZYOYtZC6VVR1xC39sb7P5PdhyDEtonQaDJap4hPSg55n_xzybz-7d26x5JNn5_r2qaE8ozgdJUsG_ihwak5UybM30vTymDPC-GBeBaHE2S1hMBxtYu7B837dTOgiQ9r1Z5Yrj_48zSjYjPPOPwRiClpGOKjrvqneqjIs9x9kDZ0EBLA4FyBYiM35Fqkcmwks7qzIFQbWIjDfktDFo0F6N48xQgGbalIHZ7jBJQ8oNee25KMzZta97h7nstK2qFppea8rcHjbA9NJu_LZ8u587dfW13okevLi-HNrjXpC66__Hn6w4kP036v4XAt9zi1evnYQ5PrBqTyZI2lJ74glTuUPEvuRHSh1DPaMETCCnZhZnvtfRacYM5D2Sg3a6Obx9BvQtdny1XXUufHp6VGrZa7Eg36G6T47mPPddRxIir2H-8YVuXd4zFBB6t3DxjIcuvID1wvR6CAurgZid-F6JN1F4Cu4qtzLK-v00aJUqDlPn3ygzY6onYwaxd0Doyh_kwMttc1ErYOaCbTF2_Yt3NsUH8dRu8Aa1UHnHKXXm4Eg3nh6GBz0LKM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/60c1fdbeee.mp4?token=uFLSuXOPZnZ__3He_2spLuuivD36_nEmfzRuaX8VwO9VWO6uBE5TAlE6htAHGNsfDysl1j4Z3rDANDB0r8aAaFRKRLcBhplHKQkHwOUjwQr94H5-4BvHZYOYtZC6VVR1xC39sb7P5PdhyDEtonQaDJap4hPSg55n_xzybz-7d26x5JNn5_r2qaE8ozgdJUsG_ihwak5UybM30vTymDPC-GBeBaHE2S1hMBxtYu7B837dTOgiQ9r1Z5Yrj_48zSjYjPPOPwRiClpGOKjrvqneqjIs9x9kDZ0EBLA4FyBYiM35Fqkcmwks7qzIFQbWIjDfktDFo0F6N48xQgGbalIHZ7jBJQ8oNee25KMzZta97h7nstK2qFppea8rcHjbA9NJu_LZ8u587dfW13okevLi-HNrjXpC66__Hn6w4kP036v4XAt9zi1evnYQ5PrBqTyZI2lJ74glTuUPEvuRHSh1DPaMETCCnZhZnvtfRacYM5D2Sg3a6Obx9BvQtdny1XXUufHp6VGrZa7Eg36G6T47mPPddRxIir2H-8YVuXd4zFBB6t3DxjIcuvID1wvR6CAurgZid-F6JN1F4Cu4qtzLK-v00aJUqDlPn3ygzY6onYwaxd0Doyh_kwMttc1ErYOaCbTF2_Yt3NsUH8dRu8Aa1UHnHKXXm4Eg3nh6GBz0LKM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چرا جنوب لبنان سقوط کرده؟
چرا ۱۱ هزار ساختمان صاف شده؟
چون رفتن دنبال «خونخواهی خامنه‌ای»!
به قول خودتون چون «پای نظام» شما ایستادند! به خاطر افکار شما!
خواستید جنگ راه نندازید!
یک میلیون شیعه ۴ ماهه آواره شدن!
شکست‌هاتون بیشتر و سنگین‌تر!</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/5814" target="_blank">📅 17:59 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5813">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6a28a5f6ff.mp4?token=QuRwcKKQiIilmCFiPb6I5uhQUmTy24eRyRnt3A4wh3QGzt5KknQ6eqTGraFEJft9PvyLkJP3-HaXt2yD6H7pDS4Dvs1gf0ZvAAB1b0heKQSGIPG-BFmirKEb-MfHWi7ZYenbzzR_A-oDme2BGV3iIRWTPdJCzo79dZ48GEftt3ZlNnyzli2D-ZV8BrL8ZwnnDSEjs8xPIXBCScbgGlELUJ0NbRNe97elsrHX_EoPcY0DLqyadPEvRGDROE_2XAKAtDrEn7hKW9lBIblelN_MX5qjx_ZeMjFBaphPdOVR6tkpCUCPy2-gNqY2Aw4wtCvI99hYMaN90187TLlEaFC1Gw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a28a5f6ff.mp4?token=QuRwcKKQiIilmCFiPb6I5uhQUmTy24eRyRnt3A4wh3QGzt5KknQ6eqTGraFEJft9PvyLkJP3-HaXt2yD6H7pDS4Dvs1gf0ZvAAB1b0heKQSGIPG-BFmirKEb-MfHWi7ZYenbzzR_A-oDme2BGV3iIRWTPdJCzo79dZ48GEftt3ZlNnyzli2D-ZV8BrL8ZwnnDSEjs8xPIXBCScbgGlELUJ0NbRNe97elsrHX_EoPcY0DLqyadPEvRGDROE_2XAKAtDrEn7hKW9lBIblelN_MX5qjx_ZeMjFBaphPdOVR6tkpCUCPy2-gNqY2Aw4wtCvI99hYMaN90187TLlEaFC1Gw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5813" target="_blank">📅 17:53 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5812">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/085c31b1b8.mp4?token=VmxCJir4HdETxGD3VntXdgxClS-0_n68xUrMUZuHO9NMWPBanQ31MBQ_3Sihmh658GA6rpxxGDhc4Jm-A8FHByBXCUStfnEeoK3cJKddrUaoZ6ZeLQ4DOUkd_FDpWlNPSqss2taSle4KHCI9KUCmStPk_7fNpacx1fv0430O0Jd0-56Y9SgXo3GCdJQH2nHFw4dxJX3g-jMaCv0ljXSIySUWUpILMT-GmEfpE5zFlLT9phz8ALVYiUWewAfgScd8UYdssjidOxqwPAZpnV8TK5_6eTfhGil4IiCbLrK1tvLKnVzwXcVUOxL4LiYbUkehm--adXYMFsSqLR-TCDXMfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/085c31b1b8.mp4?token=VmxCJir4HdETxGD3VntXdgxClS-0_n68xUrMUZuHO9NMWPBanQ31MBQ_3Sihmh658GA6rpxxGDhc4Jm-A8FHByBXCUStfnEeoK3cJKddrUaoZ6ZeLQ4DOUkd_FDpWlNPSqss2taSle4KHCI9KUCmStPk_7fNpacx1fv0430O0Jd0-56Y9SgXo3GCdJQH2nHFw4dxJX3g-jMaCv0ljXSIySUWUpILMT-GmEfpE5zFlLT9phz8ALVYiUWewAfgScd8UYdssjidOxqwPAZpnV8TK5_6eTfhGil4IiCbLrK1tvLKnVzwXcVUOxL4LiYbUkehm--adXYMFsSqLR-TCDXMfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محمد اکبرزاده،
‏ معاون سیاسی نیروی دریایی سپاه،
‏شب گذشته در یک سانحه رانندگی ساعاتی پیش کشته شد.
او در یکی از اجتماعات حکومتی به صراحت گفته بود حملات آمریکا «واکنش» بودند! یعنی ما حمله کردیم و آمریکا پاسخ داده.
جنگ‌هاشون در لبنان و فلسطین هم همینه! حمله می‌کنن، وقتی جوابشون رو میدن میگن ما در حال دفاع هستیم!
۴۷ سال گنده گویی کردند و سرمایه گذاری روی تروریست‌ها و وعده جنگ و… تا بهشون حمله کردن، گفتن ما مظلومینم و داشتیم ماست‌مون رو می‌خوردیم که مورد حمله قرار گرفتیم!</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/5812" target="_blank">📅 14:57 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5810">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GsQSQycjwXfdCa4WorY2dAHpGLwq2kcuMSCWgtTo7z6cLqR2j_Zk6gnFcxd1wgjp0yjVt3XOJxfpoLP7tYb_0JfOjSNCKUI6JIOYFcoFmill77ptS2hgmJ4aIkFjNzXynlCLalCElYzCoavxB80T4xupCaEiQDDDNZimvpC-iJYg3IwW3ntsK47qk5skNmsbgRIGKa3fFIzTv09hzZqkpN7ncsF7S4MWp95m5opaYXVOLcFZffR4kEMXdnduWkZl3j2J3bBnKENv4v6_Uys4HN70DWFS8D6VWW7LSOquTgZri0va-1zqHPf0GsSc0VrIdh-nfJF-250OGyS5yRHpUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qlO8xQNDVvKcgYU8toMr8_F3h3_YaPPVhTbVCsOTyiljrQjkQR2mXCbrlnN24J-dddAxRhrFSPr4CWBHu21Q5DyIb3G6nr61XlySALGcXx-La5YDZ6MxUzJGMJsnXow-yMn90BG1-Y-5FA7VyM6nGlTFyLATNLewHI5l5dHH1hJW7QRT2rYeMb99iTiwg0C795pTVYQ2WIL5rVuetW2T0jVgVvKzUYguWTAxwEeNmpcpCJUGlguE3PWkG9lJgwWGDMINuDFc11GZTZSw-hTavRy2VTmGCeFbFM0Fkbi6Wz7XbQ-2rn-CQpM6vv3PxFeSZ_kiNXuNKLVZv8pwxXZZWw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ده‌ها تن‌ از‌ سران و مقامات عراقی بازداشت شدند. از خونه‌هاشون میلیاردها دلار پول نفت و طلا  پیدا شده!
خیلی هاشون از نزدیکان جمهوری اسلامی هستن.
با تصویر خامنه‌ای و سلیمانی و سیستانی در خونه‌هاشون و سوتین و شرت طلا!</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/5810" target="_blank">📅 13:32 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5809">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee0be552a1.mp4?token=EEXCdD1Fz_jfWI5koghxFx0q-5DT_76mXtVDQBnZhOcjxpbjlWujhglqQZz5Z-qFbSmLuBIiIE3FAciojA3WvY494UkqUSlTnq9Gq_zKK8V2IKpBzBpyeWUoXV1HdJKLYplhVtrO5wt-ZpondxXH0AoQFwiCx7Gj_k1aAhB_ZcexKM5bZildE636FBfvHWyQfoC5YNY2vaWYkzY9HkfIkye-1ofjfv9qynh0-M8wbNDrEpFMibgx7X6y3ia-pPnUubMaoDWEsxQAI1Uqkogpoj6uKCShWSn_osnVxPLKcW6z7NNPS_6mcQcfxjW_yiJ3cKzpt8Ot9qmFT3fur25NI4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee0be552a1.mp4?token=EEXCdD1Fz_jfWI5koghxFx0q-5DT_76mXtVDQBnZhOcjxpbjlWujhglqQZz5Z-qFbSmLuBIiIE3FAciojA3WvY494UkqUSlTnq9Gq_zKK8V2IKpBzBpyeWUoXV1HdJKLYplhVtrO5wt-ZpondxXH0AoQFwiCx7Gj_k1aAhB_ZcexKM5bZildE636FBfvHWyQfoC5YNY2vaWYkzY9HkfIkye-1ofjfv9qynh0-M8wbNDrEpFMibgx7X6y3ia-pPnUubMaoDWEsxQAI1Uqkogpoj6uKCShWSn_osnVxPLKcW6z7NNPS_6mcQcfxjW_yiJ3cKzpt8Ot9qmFT3fur25NI4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بیش از این‌ها تحقیر بشید !
چه در ایران، چه  در لبنان، چه در فلسطین،
چه  در دریا ، چه  در آسمون!
در ضمن بهتون دینار و درهم نمیدن!
قراره یونجه بهتون بدن و پولش رو هم بگیرن!</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farahmand_alipour/5809" target="_blank">📅 12:55 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5808">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V3I6Z_GMgcgk3ne9JKF7W59sfENv4zDNu_QUyOA51cPiH5eTaaLJzDxquzvbo1oK4i4Ip6AkX0RTr586Ho2s2VoskLHYjH_YWfhneKFIEYYYEt7SfIU9kCZsLSwy7mld1yN3GXoFS3t2LlJNKeYegSJtCmzYz7_q-fMak88ji64PWFOCn8v2gTZWiwa9BuKFBMxbSJnT91Jamcy6i0t_PdxfzfMgBcLGKrvYezTfJLXv0IW6ycOyZObp3HYbwUL37PjJ_GkQwY6luFGA8TKsDJSZWHCCl4_Fw-lftTSaurmTJ2_gL_4MWTtUiCUJuVaiomcvr6YgAIOAJ8eEb777fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقبره رهبر مستضعفین! که در زمان حکومت خامنه‌ایِ ساده زیست! ساخته شد،  با مقبره فرعون‌های ظالم!  که به قیمت و نرخ امروزه، مقبره خمینی ۲ برابر مقبره‌های فرعون هزینه برده!  ولی عرزشی که نمی‌فهمه! بهش میگن رهبرت ساده زیسته خیار نمیخورده، خوشحال میشه! دیگه بقیه‌اش…</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farahmand_alipour/5808" target="_blank">📅 12:47 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5806">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VbGs16n50-2B5m2uGhbpYiJS3dmm9DT9autczct5pQrvZMRqVmB-YHvKZR8sy-zrhh52qtbLh1cuWU4Arua4RC0e1iaMu7ipLh48gJVUj0vPA0nHVHvErug6_QXClyHOV11f5JutUgISyu2x5m5YY6iT6R13lHI0PDclpL24CKaa2mzb95P0c5ODlcr4AfSRQ4LNZ8ulaJEOitr57k0YFyg3zyrbS6m_IH_o_iPyuM6HnFvglEtsarrD0fxwcw9SBdxmCk5E_HDeuWP7WWKSJOLY4FxEAPLDTclBFn6MagSznOluSP1iB63514lP6SMDwi5_xzImC1Qwomsmdj42iA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FOfV4tfps633A8Cdk7Ggm2ircEzPr8K4WgK_b1GsmRdPY0zsGUjqp8PsQsilGDgrKCqraJJlHC2T3JXNK-AFr6Uaz4nLlmcK_irng5qYNFbXgZKRlM3Z1qizXEwahPI7bSJJhGhhe85wdMPscE9AQMY9nsMkCU7W0jLZ9VucD7AslJC1Qi1srMIDNLo2iuNpvNYPBbpOZMAoWbrnVXW3AUaNcEMMU4ya48MtdG0oRbhmyvIqzdTWbgRenzMJoyOASQUCE2mPcxGOW0Xm-eel6gueMq1K4Uq2juhLxirddf0lhdgFMFOVxr9wL3IQ5MHvWkbup9Hy7gpatvjNT4rqUw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">هزینه هر روز تعطیلی تهران،  ۲۴۰۰ میلیارد تومن خسارت به اقتصاد کشوره!  اینها فقط ۳ روز برای خامنه‌ای تعطیلش کردن! یعنی فقط این تعطیلات ۷۲۰۰ میلیارد تومن خسارت به اقتصاد میزنه!  این فقط یک قلم از این هزینه هاست!!  ولی خب رهبرشون «ساده زیسته»!  خیار و هندونه…</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/farahmand_alipour/5806" target="_blank">📅 12:35 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5805">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vdmU0DYG7JHyjo2m50Oq3tJFjkhEj0OOok9SpecxZhOfhoqFOL3ASa_WLApU3c6V3AgjPeCWhN5YXMo6EoTPrEaA70E02Svc3aSj9BhMWyNvrQeGYfbi9fjU71zZ7IvEYmvYDS4kScfzmc1anjqURYq-Fj4Tlq6I8vjCjTY6PVooZB8nUkCaMU3J_9S6ZXe-_vC2TkPlgpnBRMrHTplWiBTLr-92wb8UXEfUNJo5fDuggVF-fsbTMYL_d1qoygElamoKYqtJSHpfwN4ZKpqvhGGz1vZxYTR7lTpn1jizMQnOndWQ13-99K3FxBoqAZJR0SYlugVvLAqSjc3yKApwuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هزینه هر روز تعطیلی تهران،
۲۴۰۰ میلیارد تومن خسارت به اقتصاد کشوره!
اینها فقط ۳ روز برای خامنه‌ای تعطیلش کردن! یعنی فقط این تعطیلات ۷۲۰۰ میلیارد تومن خسارت به اقتصاد میزنه!
این فقط یک قلم از این هزینه هاست!!
ولی خب رهبرشون «ساده زیسته»!
خیار و هندونه نمیخورد!</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/farahmand_alipour/5805" target="_blank">📅 12:29 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5804">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b7a3755d2.mp4?token=HJXSqhArk3zR9Ey4fRpCD56w6LfP2WQnufp3cm_qSoB-pkUsECGSq0maHmPv2ZGYBo6Z3lBNQGXE246uJjSuswEOyNv9uBhGGgMMiaKc5fpDtoGBXzLKSE6eRh1Hu9tIjVC0dzoaiSKItkkHQ2VlB-fu_MDO_AZiKfEnNth-tEEP3nBZd_uUoxPZ6gKy03xQjAdtHIT_XJSO05kJMUEOnMc6kY0flIwBkzKr7y4CRO3DyDXeo7KC6Of4tHCgte4qdLVyKvt_IBAIXX8JxIR8ARUYdiI_vgPHmgmDW16Y4zqfQWaeWHTwxrXB72J1O9EKc5zvHKyQYjz-iBEwFnV9DA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b7a3755d2.mp4?token=HJXSqhArk3zR9Ey4fRpCD56w6LfP2WQnufp3cm_qSoB-pkUsECGSq0maHmPv2ZGYBo6Z3lBNQGXE246uJjSuswEOyNv9uBhGGgMMiaKc5fpDtoGBXzLKSE6eRh1Hu9tIjVC0dzoaiSKItkkHQ2VlB-fu_MDO_AZiKfEnNth-tEEP3nBZd_uUoxPZ6gKy03xQjAdtHIT_XJSO05kJMUEOnMc6kY0flIwBkzKr7y4CRO3DyDXeo7KC6Of4tHCgte4qdLVyKvt_IBAIXX8JxIR8ARUYdiI_vgPHmgmDW16Y4zqfQWaeWHTwxrXB72J1O9EKc5zvHKyQYjz-iBEwFnV9DA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">برنامه «زیر آسمان ستارگان سینما»  در شهر بلونیا در ایتالیا  که ۵۰ شب در طول تابستان برگزار می‌شود.   (در عنوان برنامه در استوری اشتباه کلمه سینما جا افتاده بود)</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/5804" target="_blank">📅 11:16 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5800">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf427145cc.mp4?token=J2NSO_4WKH2tMNztbsmXNX2R-H9NdEKPXjgq-5SdQB1pw22CouEGsyJ3oFpEUwq0iJNafY5TwjqH7Y6GHeyftMaGpKCLkc0NmhM5AQE8zz2oc-3ct6b62njJj6V0r7AcpHEjcCSikn6VaSzGxq3z44CS9edc5GdU6EnoiHIZ5dHJWP3yuTYhOoGIXfCxPAYZkVRGDgACEdyGtpLXbOZbnoPYC8PX9w_AAZAbQHxLNlO1lQnSXf1F_RF1_nKfQ1ENOV5EtqRG6w3dGpVCfWzN4p4sTMY2Y3REEmgZCK68ux9L9DedQjTgS6GAHFKZsCZGEKY88-Q78_yMHDNApNVqkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf427145cc.mp4?token=J2NSO_4WKH2tMNztbsmXNX2R-H9NdEKPXjgq-5SdQB1pw22CouEGsyJ3oFpEUwq0iJNafY5TwjqH7Y6GHeyftMaGpKCLkc0NmhM5AQE8zz2oc-3ct6b62njJj6V0r7AcpHEjcCSikn6VaSzGxq3z44CS9edc5GdU6EnoiHIZ5dHJWP3yuTYhOoGIXfCxPAYZkVRGDgACEdyGtpLXbOZbnoPYC8PX9w_AAZAbQHxLNlO1lQnSXf1F_RF1_nKfQ1ENOV5EtqRG6w3dGpVCfWzN4p4sTMY2Y3REEmgZCK68ux9L9DedQjTgS6GAHFKZsCZGEKY88-Q78_yMHDNApNVqkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">برنامه «زیر آسمان ستارگان سینما»
در شهر بلونیا در ایتالیا
که ۵۰ شب در طول تابستان برگزار می‌شود.
(در عنوان برنامه در استوری اشتباه کلمه سینما جا افتاده بود)</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farahmand_alipour/5800" target="_blank">📅 10:42 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5799">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Frx-EGHs72snNooBr_fe1tm3ngSodWWnVUFE10xjbmgWtll2MS26NapaIbrjSxyejAlMa70Bj7eYFDQSsRK45nIUObHIrIgtcWI2qzzvNP_3OUIWKBQ2LqYi1NpOOtEEx5urCTedYRcqFQyy0Fsy7-JbVjXTWeK06vg9MwiGt29vBZMnBxyyqxMUBmITuIGeAiDxZS1C5FSNUbWwBWVAgcUX_yKCtmD-SwED3fJ_82SABnaiPLdxa0r1CxHPcPz43tJ1LvdT-bW9WEnUO19M9DBtexlsDTRvrbv2CxumZTmWQQb4TbUqlyQlMlyeSsRRsM3W3BPEDKkG-8up19nSRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هرگز به مردم ایران نخواهند گفت!  اما کاملا قابل پیش بینیه که هزینه این مراسم بارها و بارها از هزینه جشن‌های ۲۵۰۰ ساله بیشتر خواهد بود! چندین برابر!  درست مثل راهپیمایی‌های هر ساله اربعینشون که باید از جیب ملت ایران مصرف بشه!  یادآوری : هزینه جشن‌های ۲۵۰۰ ساله،…</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/5799" target="_blank">📅 09:26 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5798">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2dc44e27bf.mp4?token=vgqFhhJJub4_i0GuLOjxfROJELW9BBuX0gdhhJn7-zVTLolEQL6HymgoJq160orqJPKipCUnPWqmLi6aGMiGJtNInH5oZvsdKYxzR2ox10m8U6Xu192y14PhSXeD4pBGPABEC_amoB9zMDqsweoeeKLCW47pVZi1f0XJeaiGaTlexqqgl8X-MNZt5D78L2M950Jr5RSemwysCK-fKdfgMFKv1jtTk3PF3oFvu6gsKpRwqxahxuDlKFE8zuQz3UgnzCHgaFjdxx_fUwQ8VlZmcBeSoK7EVMs5RPq8i2avr-gZkA1MZ4J2oPvbQyOqgd2Riu9ihu5indbRl68tZGd8Ww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2dc44e27bf.mp4?token=vgqFhhJJub4_i0GuLOjxfROJELW9BBuX0gdhhJn7-zVTLolEQL6HymgoJq160orqJPKipCUnPWqmLi6aGMiGJtNInH5oZvsdKYxzR2ox10m8U6Xu192y14PhSXeD4pBGPABEC_amoB9zMDqsweoeeKLCW47pVZi1f0XJeaiGaTlexqqgl8X-MNZt5D78L2M950Jr5RSemwysCK-fKdfgMFKv1jtTk3PF3oFvu6gsKpRwqxahxuDlKFE8zuQz3UgnzCHgaFjdxx_fUwQ8VlZmcBeSoK7EVMs5RPq8i2avr-gZkA1MZ4J2oPvbQyOqgd2Riu9ihu5indbRl68tZGd8Ww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هرگز به مردم ایران نخواهند گفت!
اما کاملا قابل پیش بینیه که هزینه این مراسم بارها و بارها از هزینه جشن‌های ۲۵۰۰ ساله بیشتر خواهد بود! چندین برابر!
درست مثل راهپیمایی‌های هر ساله اربعینشون که باید از جیب ملت ایران مصرف بشه!
یادآوری : هزینه جشن‌های ۲۵۰۰ ساله، به ارز امروز، حدود ۱۲۰ میلیون دلار بود!
هزینه سالانه گروه تروریستی حزب الله لبنان
یک میلیارد دلاره! ۱۰ برابر!</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/5798" target="_blank">📅 09:21 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5797">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d3b713ac56.mp4?token=Edp9mIQ9mIiAxGVLvGflf3kwxZOjNVWmBF_mRWbTBJA30R46dWYPussSrOmF49iSf8RqAbGrLPilT67Z9c9gmtAbV8lwbClzp9An_cstAN9RoBzQLrABhuFDBvk4NE3vuyqOxm-2swBbi_2PWvyKLGLIgAYSdLbBjx3H1raJ5f63nxU1a51WlFcxMzclN8IeePennyQvJXL785ctCN0woIKT67VL7T8Uw0HyYbJF9HfeM16PhsizFykqGBvELvsbPMkdJXAj29skmr5eAQLq0duyCm-TaoOWIDU1cPS66gD067g-i_OSLHSZJvxbxVaoTXaU5QF3gOyYD6aN6ozxEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d3b713ac56.mp4?token=Edp9mIQ9mIiAxGVLvGflf3kwxZOjNVWmBF_mRWbTBJA30R46dWYPussSrOmF49iSf8RqAbGrLPilT67Z9c9gmtAbV8lwbClzp9An_cstAN9RoBzQLrABhuFDBvk4NE3vuyqOxm-2swBbi_2PWvyKLGLIgAYSdLbBjx3H1raJ5f63nxU1a51WlFcxMzclN8IeePennyQvJXL785ctCN0woIKT67VL7T8Uw0HyYbJF9HfeM16PhsizFykqGBvELvsbPMkdJXAj29skmr5eAQLq0duyCm-TaoOWIDU1cPS66gD067g-i_OSLHSZJvxbxVaoTXaU5QF3gOyYD6aN6ozxEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لحظه‌ای که «سپهر بابا» ستاره رفیعی را دید.</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/5797" target="_blank">📅 22:28 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5796">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e1e05c8825.mp4?token=KuPn1Oq4gISjdK4PnN__-Y7ooIlvN9hJBDQ77L2HaNNw2VeyQ2y0-9l3e-iKfgGFm4iTltwHRpmG_OaOWGmwNuVPZfNRHlh1C8X2i5tAhHagFrwMBjwgvOdoj7xdAkVWU8FJLy_ru8jsxPwqdcP3f9uOnVU0cscUjCLd3u5zK4PD1XXz21opAk7tTarBFkXzlJbOpA-iiWrfOubiWA0ErPeAJU0zIzTRYfjzAEVhZIgttDBuGAKPh7z5pxccS07g7FNaIwVbhONLcbt-F18fjmuMk0DlibnTOnfHXD65F60I_mMST59kNuTS5ljjUzHB6IJxctDl_h2iqSAaV5hQ9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1e05c8825.mp4?token=KuPn1Oq4gISjdK4PnN__-Y7ooIlvN9hJBDQ77L2HaNNw2VeyQ2y0-9l3e-iKfgGFm4iTltwHRpmG_OaOWGmwNuVPZfNRHlh1C8X2i5tAhHagFrwMBjwgvOdoj7xdAkVWU8FJLy_ru8jsxPwqdcP3f9uOnVU0cscUjCLd3u5zK4PD1XXz21opAk7tTarBFkXzlJbOpA-iiWrfOubiWA0ErPeAJU0zIzTRYfjzAEVhZIgttDBuGAKPh7z5pxccS07g7FNaIwVbhONLcbt-F18fjmuMk0DlibnTOnfHXD65F60I_mMST59kNuTS5ljjUzHB6IJxctDl_h2iqSAaV5hQ9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تفاهم‌نامه ج‌ا و آمریکا رو به طور نمادین آتش زدند و گفتند که این قرارداد حقارت‌آمیزه که خب این بخش رو درست میگن!</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/5796" target="_blank">📅 18:49 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5795">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dCyg1TNa_IQd5xdjC3G7FtnwPKePxrzh54fyzrWlSiI0Hm4lNYPSz09hL6nI5CQWT2GSqXDv_xCvQguJ_VoRlLT25qTNQGKbakc10p_vUNaoZT6pJGVZ6cw44DdhuO8_4KYDMSQ3yKOPby_6lEpkZtqwOo1l7MQW2cqFgDcj8DrwByG8Vdje9sLcmfbBzjBzywXDI9c13SLddTOef6cP_jpxZR3SMC8O8OcJMRFVg6SNGECwasy76Chxbn1dkoFY7PfiZssPQT0DruRRoMU3RtrKe-NOYQs6-HA6OubF2ESidF2t3clcGe8kyL_nXbnu8TW4fLJ1a8y70o2gx6-EDQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e972609e9.mp4?token=TIT0KWjrze8LPTuFMAE8wzQ-WvKju3mbWYP-rNspTjdE5MkFeJiL0zSrKha2ns65s-0OOk5wp9Po4-Zdep6QiohbSuX6wrPNgEQpI_Luc1Bax6AcHodZtwADF1UGdg58IWkQD2OiSYPWB7FI5QLm__hm7vFqPwTGVr1nt13NbNGOi2IKqqz04OHAoTpCvyFExOE1Q5hE_XLssemjqykVa80qY1nxU4eSDGa9yNAPfoZrsT8O73_hm_FEy8x3wLeQ20vONEV1Yxsdu-8gSNmGZWdOCsn4wLOa7oZPNkJ1eGe2CLL053UYqCJ8mG4ZlEEhUiWnphybgNnIFV8YR0B68Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e972609e9.mp4?token=TIT0KWjrze8LPTuFMAE8wzQ-WvKju3mbWYP-rNspTjdE5MkFeJiL0zSrKha2ns65s-0OOk5wp9Po4-Zdep6QiohbSuX6wrPNgEQpI_Luc1Bax6AcHodZtwADF1UGdg58IWkQD2OiSYPWB7FI5QLm__hm7vFqPwTGVr1nt13NbNGOi2IKqqz04OHAoTpCvyFExOE1Q5hE_XLssemjqykVa80qY1nxU4eSDGa9yNAPfoZrsT8O73_hm_FEy8x3wLeQ20vONEV1Yxsdu-8gSNmGZWdOCsn4wLOa7oZPNkJ1eGe2CLL053UYqCJ8mG4ZlEEhUiWnphybgNnIFV8YR0B68Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این شب‌ها، همین‌ها توی هیئت‌ها در حال عزاداری هستن
ده تا مرد مسلح افتادن به جون یک زن معترض ایرانی.</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/5794" target="_blank">📅 18:39 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5793">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kpU01mEfj5BeXP-P316-dnAOnZEbQv1_fyebgP4MawNgvOqWanekzwufqbA-qVaGsDCSdC3dHd00fGqXNVPxwUb1H6AZsdLy7EAW0XKX38LJu6QKyFpwbnuiuus9075eyuBr2OwYT-cI38D31WrbMCAkqxFcQt1BW7_tpzmxN3cVubx7Wjp4DEWH13xlZPYnDZcK1o9rLtRz7_ektfKsbMjc1dKzhPCDA1V6pC9L4AnJ4Z0tj8MputNhqH34_62uhs7BBG4QZPkDceFJc_wcZqCY8oc7JuVjW1LJV9Pgmb_P-eFDGWK0esqq0J6ANzQLI-bmNDctsOoEgWYg3cjnFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حالا در حد یونجه و ذرت ایراد نداره</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/farahmand_alipour/5793" target="_blank">📅 18:33 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5790">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kHL92Ub2G-W_1uIGx2cOitD2NprJ4PB_r2MhiIHEB1ZclvnAy7vYxRC0bbeJnJZhyjIgSuJ5CX6ZyFLN98A6UqGn8Nd5RU8VuvN1WYIr5li3hL1XrQ0lppgtTJUFvZ_d1MelnnumKSYvG98_-uFK5PvB2PFcRclWDzGC78ELg8-8gbFkEztVrA8rqnwYbdG6D7Ntz8baWI7ecs7I2BqPv1N4CfaFcGDFt8VAQbLrieBPV2wDsStNuWmFC4EPpKUNI1U5zwtqB0o9hbcb6wLQTsuKaW1nb81Aaaxggy13at38ZqJq8NLhHz5FJ1CuUh36IZyuWPySV7qMUDiBG5PElw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/651901a9ca.mp4?token=qzeFJlO8MTH-4u5GljDNVrX08JhmIypEyrNB-XeSphFSThqouv3EB3OfV-vz5x5BD75IgY2Y0mgdXU5PBDP_5GvkbKxBfdMnfzviXmFJX2b3xbsFSis0sm_WLCgqIN6cn7tsUw4x5UdqtyjjZmKb7zDu3Nq3rVu4xRAM-uKv9zwkJCP1R3FcDly91iXq18LPNqGpiN2lqFnHkMtbUTWyXT1XPliqcSRkmFBL5oBj076LdTvMC_wzXzpFKhBBHrRIuuhN16LppbCu3L4bchxWyGFguyt2bGs48RkI1dFNs-KcYB1-H_yCenpJ6OsRRmwjNLjALhIE1gqt13U5DivmPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/651901a9ca.mp4?token=qzeFJlO8MTH-4u5GljDNVrX08JhmIypEyrNB-XeSphFSThqouv3EB3OfV-vz5x5BD75IgY2Y0mgdXU5PBDP_5GvkbKxBfdMnfzviXmFJX2b3xbsFSis0sm_WLCgqIN6cn7tsUw4x5UdqtyjjZmKb7zDu3Nq3rVu4xRAM-uKv9zwkJCP1R3FcDly91iXq18LPNqGpiN2lqFnHkMtbUTWyXT1XPliqcSRkmFBL5oBj076LdTvMC_wzXzpFKhBBHrRIuuhN16LppbCu3L4bchxWyGFguyt2bGs48RkI1dFNs-KcYB1-H_yCenpJ6OsRRmwjNLjALhIE1gqt13U5DivmPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">«عالیه نصیف جاسم» نماینده پارلمان عراق،
عضو کمیسیون مبارزه با فساد، از نزدیکان جمهوری اسلامی، معروف به مواضع تند علیه فساد در عراق، چند روز پیش میوه نذر امام حسین کرده بود. دیشب در موج دستگیری چهره‌های فاسد اقتصادی توسط دولت عراق دستگیر شد، در خونه‌اش ۱۶ میلیون دلار نقد و مقدار بسیار زیادی طلا کشف شد!</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5790" target="_blank">📅 18:03 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5789">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">شعارها رو گوش بدید،  اینها اعضای سازمان مجاهدین خلق هستند. خوشحال هستند از صدور حکم اعدام برای «حبیب القانیان» ، توسط خلخالی بدنام!  جمهوری اسلامی اعدام می‌کرد، حذف می‌کرد، مصادره می‌کرد، بقیه  گروه‌های از جمله همین سازمان مجاهدین خلق هم تایید می‌کردن، میگفتن…</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farahmand_alipour/5789" target="_blank">📅 17:05 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5788">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/583cd57ba5.mp4?token=ZlA4FUq-X2sOP7DoSj0pHxLttQqF7tNStUiXN62RDg2NRznFgTe_nKJORQHxxk5uhJThvWHiauT42-3rqXI9nQ55Q2XJv3n_A-BVcl84Eqd6KfQbzFy5WjtpOi4GTDY6LIcXQ0nE_1AjFisXCqscXMr8xXubm7oquy7_oi8UvCRRnimuOZnJ0fmu8BEmbYAJ3cL8XwzXZ57zE7RlcKxdyMAx9NfUOSsHbN7IpMOPTCPpM6lxUDaMwBT0mmHDCpFUO2O7ZrwEN10_YeIFyz2dvaLUhQsN5AKtV6sNfJAAPphM2ujdNrRI_3ElVQHtPtoJQ7PZpZSAKsbtrSkJnaHz0iqXyFOrSURmkx-LLPr4LluStq2XQkEbDatazCuXko_eIxKFTGx3BVy0JgRg5h1KNbZZgnPy4gj3CLVyAn6zjHOwJgy4WF8Sw60fzXUQVTIGp_S2khh8muuuGl5MHOXiUCeJ4u9jWXMU2MGAGNdwR7H5UXeMmyrjfcajLGz5DdPPz2lBUVOAKyqlgC7evoHMmPCxXWGHj5bO9TG--lHOs9CDYEGcrYtt0guoAdICyYO7tSeAoW_3T2UXPuJFVrMbRVuQbjiipXJ2d0CFowgOnxj-cMUWMxHqcm5SLCt7VgEP-P60B63FGzXmzp70BE_xtJxsvbtZOBhzoddi_oFfPyU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/583cd57ba5.mp4?token=ZlA4FUq-X2sOP7DoSj0pHxLttQqF7tNStUiXN62RDg2NRznFgTe_nKJORQHxxk5uhJThvWHiauT42-3rqXI9nQ55Q2XJv3n_A-BVcl84Eqd6KfQbzFy5WjtpOi4GTDY6LIcXQ0nE_1AjFisXCqscXMr8xXubm7oquy7_oi8UvCRRnimuOZnJ0fmu8BEmbYAJ3cL8XwzXZ57zE7RlcKxdyMAx9NfUOSsHbN7IpMOPTCPpM6lxUDaMwBT0mmHDCpFUO2O7ZrwEN10_YeIFyz2dvaLUhQsN5AKtV6sNfJAAPphM2ujdNrRI_3ElVQHtPtoJQ7PZpZSAKsbtrSkJnaHz0iqXyFOrSURmkx-LLPr4LluStq2XQkEbDatazCuXko_eIxKFTGx3BVy0JgRg5h1KNbZZgnPy4gj3CLVyAn6zjHOwJgy4WF8Sw60fzXUQVTIGp_S2khh8muuuGl5MHOXiUCeJ4u9jWXMU2MGAGNdwR7H5UXeMmyrjfcajLGz5DdPPz2lBUVOAKyqlgC7evoHMmPCxXWGHj5bO9TG--lHOs9CDYEGcrYtt0guoAdICyYO7tSeAoW_3T2UXPuJFVrMbRVuQbjiipXJ2d0CFowgOnxj-cMUWMxHqcm5SLCt7VgEP-P60B63FGzXmzp70BE_xtJxsvbtZOBhzoddi_oFfPyU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شعارها رو گوش بدید،
اینها اعضای سازمان مجاهدین خلق هستند.
خوشحال هستند از صدور حکم اعدام
برای «حبیب القانیان» ، توسط خلخالی بدنام!
جمهوری اسلامی اعدام می‌کرد، حذف می‌کرد، مصادره می‌کرد، بقیه  گروه‌های از جمله همین سازمان مجاهدین خلق هم تایید می‌کردن، میگفتن خیلی هم خوبه!
تا اینکه جمهوری اسلامی بعدش رفت سراغ
خودشون! و در ابعادی دست به قتل عامی در زندان‌ها در سال ۶۷ زد که در تاریخ ثبت شد.</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/5788" target="_blank">📅 16:57 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5787">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/938419e982.mp4?token=lPbuMj3kTGnnxbRqCTaeD_qWyj7Xd-ABpvV0MZsL_hDW2LpSUVUDabl7LknW_CotzPPuKUiwucqViaI_caQE4ejdcnCrI2g9IYKebm535MF1F5CmZZJ29zSuOOWKYjUaCY4kiYSEiD7HwrrsF8qSibrtuBPPzmLE_5iR59InLO0C1Oa_8wkIBw36Kok0ipkpZ_wuWgob43t-icQyY7WJlCj9FHpKCQYtwv0tGDdQY_lw0voEaUqaiFRaOmltzriqeM78jALKPkclYHRPI3Mo7rjexOQMrzfKi-_v-xk-hDI_zXc7qpeipBfSuCtksQVH4WRyDCZ4X56GKd4lv_pLaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/938419e982.mp4?token=lPbuMj3kTGnnxbRqCTaeD_qWyj7Xd-ABpvV0MZsL_hDW2LpSUVUDabl7LknW_CotzPPuKUiwucqViaI_caQE4ejdcnCrI2g9IYKebm535MF1F5CmZZJ29zSuOOWKYjUaCY4kiYSEiD7HwrrsF8qSibrtuBPPzmLE_5iR59InLO0C1Oa_8wkIBw36Kok0ipkpZ_wuWgob43t-icQyY7WJlCj9FHpKCQYtwv0tGDdQY_lw0voEaUqaiFRaOmltzriqeM78jALKPkclYHRPI3Mo7rjexOQMrzfKi-_v-xk-hDI_zXc7qpeipBfSuCtksQVH4WRyDCZ4X56GKd4lv_pLaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قدرت حضرت عباس</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/farahmand_alipour/5787" target="_blank">📅 16:27 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5786">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iChtrtWK03Y1AghEjK26_59hzO7SAa_drOmskmgN-tfqvfsBrz4uM2Y3wLvgSeHl8WM5eVJTGaj0QpDRKsN4_BUu4uZ-E9GdavNqyWSIOWNX1-dhdYtVHv3UWLYY9TAmaM-MWsT4eN-B19WmPnQJi72O7nfL8DUWZkYj29fxBIN0F1IVstxQOfINOwYw1GoT9LNuGKffg3KNHj1HCkNM4ZrnKx-MzxA0OzCi9kwm7WcrvS11hY3ET1jSyxrem0EEFUnTqnhGOze-zxFVZQ8Q_vpkKjYyGiHns0mSq82W_E_bjDrapef75V2Z-jxZZ4aZ2Go10MzSjcoKg4IezM-dng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای فروردین ۱۳۹۹  همکاری جن‌های دشمن با سرویس‌های اطلاعاتی علیه جمهوری اسلامی!  همین آخوندها وقتی اصفهان در محاصره ارتش محمود افغان بود به شاه سلطان حسین میگفتن اصلا نگران نباش که ارتشی از جن‌ها میاد به کمک حکومت شیعه!  ولی این جن‌های نامرد نه به امام‌حسین…</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/5786" target="_blank">📅 11:31 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5785">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b91e9581d.mp4?token=Yn7Bos8aX2uDdRa_oG4e2C9BNKTZ5xUWi2QJ2cLv7JkllMITvitu0O9bJQc3uONhecsHITUUB2M1uExDvhgkOAmwTY6LkuP6L3faEu6nJ4stwKgBtnlWMwbSDhnnPD1LYPf38CjNBMUh8tMTF0SSyCwRyLI13vzFgOzxv0uJvcGyBHvwVj1UUXx5i4_O2ibWTEYUd1bxdlJo2MX4K_8-CeqGIjBohdMwpC-5jfn_Q-kjn87ro6uNJkLLs8Uz194cf6TB4otCIDa0k_BTZxHVXNjhJRm5ET0Q8ckFCUOpamV6oK60Cu_hMXiZ2wWe4g5qJuEyu2C_zy_yEy6zkcpdmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b91e9581d.mp4?token=Yn7Bos8aX2uDdRa_oG4e2C9BNKTZ5xUWi2QJ2cLv7JkllMITvitu0O9bJQc3uONhecsHITUUB2M1uExDvhgkOAmwTY6LkuP6L3faEu6nJ4stwKgBtnlWMwbSDhnnPD1LYPf38CjNBMUh8tMTF0SSyCwRyLI13vzFgOzxv0uJvcGyBHvwVj1UUXx5i4_O2ibWTEYUd1bxdlJo2MX4K_8-CeqGIjBohdMwpC-5jfn_Q-kjn87ro6uNJkLLs8Uz194cf6TB4otCIDa0k_BTZxHVXNjhJRm5ET0Q8ckFCUOpamV6oK60Cu_hMXiZ2wWe4g5qJuEyu2C_zy_yEy6zkcpdmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زعفر جنی، پادشاه‌های جن‌های شیعه
😅
حامیان همین‌ها میان کامنت میگذارن که تاریخ مطالعه کنید! محتوای تاریخ‌هاشون!</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/5785" target="_blank">📅 11:29 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5784">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb5c00112a.mp4?token=q4UnUt_vnbvhiziRuHqPJeN9NvrQrsSi6jFn5UvbXiVpLJ-APya92weL4gMS54veRfZJZji7j93ulXgb6EJtrhUzGdJ9_u2FQUZTMMB5FZQYirEgV8fY6NYJEbRz8w3CSqVtTRcMC1rVeNlDUQqae_9OCJrs4L2P8Wdkg7Yk4R2iPQzrBXJBhSB6ZliaxBF_mVSE5aNKgN9It29OD3FDAvR-cA-NSo7Fzp4DK06GhOXV2OLG3PQkolKcKIFnw7WprgYGcQpqi55pge327-qHhvC4jtU_YrLsPQt2y_goKVl1xk5cxbSJ-NaEm_3lvTuXzMYGWaIn_XkKPwvoyZjAUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb5c00112a.mp4?token=q4UnUt_vnbvhiziRuHqPJeN9NvrQrsSi6jFn5UvbXiVpLJ-APya92weL4gMS54veRfZJZji7j93ulXgb6EJtrhUzGdJ9_u2FQUZTMMB5FZQYirEgV8fY6NYJEbRz8w3CSqVtTRcMC1rVeNlDUQqae_9OCJrs4L2P8Wdkg7Yk4R2iPQzrBXJBhSB6ZliaxBF_mVSE5aNKgN9It29OD3FDAvR-cA-NSo7Fzp4DK06GhOXV2OLG3PQkolKcKIFnw7WprgYGcQpqi55pge327-qHhvC4jtU_YrLsPQt2y_goKVl1xk5cxbSJ-NaEm_3lvTuXzMYGWaIn_XkKPwvoyZjAUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زعفر جنی، پادشاه‌های جن‌های شیعه
😅
حامیان همین‌ها میان کامنت میگذارن که تاریخ مطالعه کنید! محتوای تاریخ‌هاشون!</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/5784" target="_blank">📅 11:29 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5783">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/383f2c1b20.mp4?token=qyFgjKL20HppYk0okpzdkxaYpD_cbybeV-Mw62l3PxV8i2Vebhr9_8LXHP2Y6KDiB0Z8BCX3xxEcsUEcI7pTdAvXM68jTgg06hd4SUCRHWHTL26Pm64KQ1ozHEQl2SS0KjrMe_wqPgo9uxu-SfEEl2cUobmCSK-mF5CbKQZAYa9W9Uyi8rJrcDpYgNtBY2zHp4kCrSdDyc_tfbw-PIRpE2lFvbjsGho4EQntjgfmQDJii6WA972Wg-W5k1BGC_RzHx9DT1H3RihuUXMFe5BY1OAmlcQ6_1TFIOLnLtx2ApNpxPmWPO5I4tyK12SfohK8Adiaw5B0-Qm15Fmf96_xzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/383f2c1b20.mp4?token=qyFgjKL20HppYk0okpzdkxaYpD_cbybeV-Mw62l3PxV8i2Vebhr9_8LXHP2Y6KDiB0Z8BCX3xxEcsUEcI7pTdAvXM68jTgg06hd4SUCRHWHTL26Pm64KQ1ozHEQl2SS0KjrMe_wqPgo9uxu-SfEEl2cUobmCSK-mF5CbKQZAYa9W9Uyi8rJrcDpYgNtBY2zHp4kCrSdDyc_tfbw-PIRpE2lFvbjsGho4EQntjgfmQDJii6WA972Wg-W5k1BGC_RzHx9DT1H3RihuUXMFe5BY1OAmlcQ6_1TFIOLnLtx2ApNpxPmWPO5I4tyK12SfohK8Adiaw5B0-Qm15Fmf96_xzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همش ثوابه :)</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/5783" target="_blank">📅 11:08 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5782">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a9c5c701b.mp4?token=BJXSjF5FOoRPCDcFruGtmEDA2JhB_PHAT_vkjqx9UfrO4JzDbAS_3ygFutZspwdatC52k6TEcQQLCV-jRm1PMQ-EAy1XFD5_GAsLg1eZApSx5V4T6N2cWMQYIhG4zEe09xpKEN477wR6QhGAQ1Tbp-UJLcPB6cWzNddvwtARwEir_4MNJrMF7G6xfUzrQPLwdgb7dBCbPIHNL6iANHpoyFXnh1Zf3MA4huQWWEtvPaAGBhBa8vhA4YZwJz3oc8weZIJUrcChyntf4v3B1-bPiP4vZhYqO1_v6bdG2ByiCONMozJTupbIGawNgOo_n8man164f5UpIc2Xp4nxyu8DlQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a9c5c701b.mp4?token=BJXSjF5FOoRPCDcFruGtmEDA2JhB_PHAT_vkjqx9UfrO4JzDbAS_3ygFutZspwdatC52k6TEcQQLCV-jRm1PMQ-EAy1XFD5_GAsLg1eZApSx5V4T6N2cWMQYIhG4zEe09xpKEN477wR6QhGAQ1Tbp-UJLcPB6cWzNddvwtARwEir_4MNJrMF7G6xfUzrQPLwdgb7dBCbPIHNL6iANHpoyFXnh1Zf3MA4huQWWEtvPaAGBhBa8vhA4YZwJz3oc8weZIJUrcChyntf4v3B1-bPiP4vZhYqO1_v6bdG2ByiCONMozJTupbIGawNgOo_n8man164f5UpIc2Xp4nxyu8DlQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آورده فرهنگی شیعه برای ایرانیان</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/5782" target="_blank">📅 09:32 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5781">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GJ1lP-BS7Gfs8A2fcIpvgzUclAeUSuGFzbMP2fhumrjCsJcx0VcP8LzpdYYBD6I52Kly4o1o8_LVQNG9skwVdXIb8D0btcKXvce7jI_gwZ0qOkOe7j5rOUGb3XRV1-oJTvUPp4oRqu0KIEIiqG2dXXe3H50iH13VF1mdeZK5Kb-G9KfaFgeKtp7GP3KuN4piy3nfR7oLpAVh47weho6KtIfBqxaZDPItvG29JxmP7qNNQ-i2dEnQpe3uX45D5W2tE5hkGV3ymLx-agbCYPWdEMsyvudSpuY1VwJz69cftQryIpyF55vN7XU79STldj8e_lYsMcEkfdPLgZzu7oLpCg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🚨
جمهوری اسلامی و آمریکا موافقت کرده‌اند که حملات را ادامه ندهد و سه‌شنبه در قطر دیدار کنند.</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5780" target="_blank">📅 00:08 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5778">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/409f2a841d.mp4?token=FfR57RdsJxPDXwif5nJEF-4ZDgMu8BHDRWy9CIiyUsUypwyWEvixFbvR8zwMADeZH6F1iyQz9Z6YpN5bgCd6LXAgKKss6JqJfnK1Wen42XY9ix1gkGwu-DtsEsWIrissRKTacKWl0Jw2NcY_gq1zpgWEtO5hezDSAHm5xlidgu63AojgLnVYgW5biGtuEFH5gFJZRM7uQQLax3Y2-VLHZJxDLR77U3Lt3yS759zImRkjvrzHG13_AzsP0phYwu00ZACCK9sPvV5x8pgvBWfDxpTi5WrTRFMS0bHW9rmo5Fn8Ii8XTkyiZ1nOJbAYo-2jWSGrv3uFJrj9_Qght6v6Uw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/409f2a841d.mp4?token=FfR57RdsJxPDXwif5nJEF-4ZDgMu8BHDRWy9CIiyUsUypwyWEvixFbvR8zwMADeZH6F1iyQz9Z6YpN5bgCd6LXAgKKss6JqJfnK1Wen42XY9ix1gkGwu-DtsEsWIrissRKTacKWl0Jw2NcY_gq1zpgWEtO5hezDSAHm5xlidgu63AojgLnVYgW5biGtuEFH5gFJZRM7uQQLax3Y2-VLHZJxDLR77U3Lt3yS759zImRkjvrzHG13_AzsP0phYwu00ZACCK9sPvV5x8pgvBWfDxpTi5WrTRFMS0bHW9rmo5Fn8Ii8XTkyiZ1nOJbAYo-2jWSGrv3uFJrj9_Qght6v6Uw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/06f2d554a0.mp4?token=UmzGv54VU7QTSTNx9CZrMRH4Zf7YtAzsgUB7nBqMXYAXIp1LEXZMFyT6cjX9osYdhUrHUUlMgs115qTX0VO7uVp90gUBXkSsv-dCkhoq_fknSr-xq7TmO2SCDg9LkWpWlIefM32ryC_kSCXZCMTDG30CJs3zTmLPmq_EO29pi5DDEdtBbpRqh-xis8VkdjcrToqR3wRwWG2a4j54iLwJGiZYhXOaml6q1tMpdOzr6mPVwSZKMzykSjc2IbwIwGJEZWPLpeH2Ah1k-KhOW7PmlNwvtk6M-LcgHCSiugMZCDKLv7EN_HMJ-NTeet8ncvflLXZ4ENh5IxFMcHHeMGg7_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/06f2d554a0.mp4?token=UmzGv54VU7QTSTNx9CZrMRH4Zf7YtAzsgUB7nBqMXYAXIp1LEXZMFyT6cjX9osYdhUrHUUlMgs115qTX0VO7uVp90gUBXkSsv-dCkhoq_fknSr-xq7TmO2SCDg9LkWpWlIefM32ryC_kSCXZCMTDG30CJs3zTmLPmq_EO29pi5DDEdtBbpRqh-xis8VkdjcrToqR3wRwWG2a4j54iLwJGiZYhXOaml6q1tMpdOzr6mPVwSZKMzykSjc2IbwIwGJEZWPLpeH2Ah1k-KhOW7PmlNwvtk6M-LcgHCSiugMZCDKLv7EN_HMJ-NTeet8ncvflLXZ4ENh5IxFMcHHeMGg7_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">منطق جمهوری اسلامی
و تعریف «امن» و «ناامن»
میگه اگه  یه کشتی بخواد از مسیر «ناامن» عبور کنه بهش شلیک میکنیم :)</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5777" target="_blank">📅 23:26 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5776">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j7TlAQhOiNEAyLyL4tKJMGCqwW5bL_B5r7KvbAX-NapgtYj3xQXL4ck8o8CN1HvzTqTGKf1HPRGcabS2P3DV0oe6jc87oCP111Z9-q0nQ_68UUqRpk5e8aMOpi0W9iqtvDrKZkulMfI-ahI8mFPJJRyiYJPkGSV4JblviCXIzWYMY2sqXKG9kzGpOHxitlcZ1YdpNOpxSdDiGERn92w6gLmU4vjpkk6Qbq62sCswz5job3iQsmDA1VMsbZrsHSuJ05jXsb2E0g1hlSkuHAzUmSP59xonkxAb6SjU8FvPy7bpNYg9lRgZoTWlAeqc-q9x7TpkZPgAIYW1bmxMBgMRXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس: چاره‌‌ای جز ساخت بمب اتم نیست.</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/5776" target="_blank">📅 19:39 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5775">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e4e9d7782.mp4?token=HG1IoBw0QmL1NETbG4CodUxpw2dCe4iFl5Tv4cA71-mQB6rOG6x2LIuP_xDOCBaI7RL6ANbj0RNJrvh93ZuT_O3zaGLzmot8sF0gPcjsESPiSnTuu_Jq0o5S_MXQxaQKvJQqs5PgQZRVTGCq-9Isqxg7LHdncltwn-ybbwHgdzNXgv5KcUHPhGSWmtZS9WBpnW6oaf-P9JFgbXZa7WbPlN9chQiiNsJ-0b9euTyjUZolhEpAmrZoAd1YDoSYPmVLl_SCMFy35YTwCWr3k80z1qSAfZoYkAXtBdCrMxKKkf84tOaDYj_pn8cDFohOYnL7wa_kQIO3cGOC1bGX_qCQBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e4e9d7782.mp4?token=HG1IoBw0QmL1NETbG4CodUxpw2dCe4iFl5Tv4cA71-mQB6rOG6x2LIuP_xDOCBaI7RL6ANbj0RNJrvh93ZuT_O3zaGLzmot8sF0gPcjsESPiSnTuu_Jq0o5S_MXQxaQKvJQqs5PgQZRVTGCq-9Isqxg7LHdncltwn-ybbwHgdzNXgv5KcUHPhGSWmtZS9WBpnW6oaf-P9JFgbXZa7WbPlN9chQiiNsJ-0b9euTyjUZolhEpAmrZoAd1YDoSYPmVLl_SCMFy35YTwCWr3k80z1qSAfZoYkAXtBdCrMxKKkf84tOaDYj_pn8cDFohOYnL7wa_kQIO3cGOC1bGX_qCQBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تیمی که با بدرقه قاتلان جوانان ایران راهی جام‌جهانی شده بود.</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/5775" target="_blank">📅 17:23 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5774">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🚨
شب گذشته یک عضو تیپ ‌گولانی ارتش اسرائیل در جنوب لبنان کشته شد.</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5774" target="_blank">📅 13:06 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5773">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">ولی ما می‌د‌ونیم چرا شانس با شما همراه نیست.</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/5773" target="_blank">📅 10:17 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5772">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1220ffd18e.mp4?token=Lf0lDqWRJEFrli2IClUQHQGq8QCxETQWaCbc0b52zVnhbLkAHZrSvU86xGIhN_kzUBfmk_T16DWHeyKHiPxglahncAzQ1lsX6KUijgNW3SSxrw6IzZ588DfpWIdFBmmDK2KBoAJiyPiAXYdzg1WWPdFVavz3ucF3ldTlk7ZXyl9EV1guVuiT7rAwwqNXZP320zwapD-TK5dAQiqiN7RWcQDSa16pVMuyPWhaqsnpT0lzhyhkyQOaBFlY9qD4PppTFIq8ol4UErjAHoW-IsnzJKK3Pz4rz7Oga5NQ-PU20STiuxJQ3ZosKzpxV6_BekPKyylYiq8E-ahv2PiNR_tpow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1220ffd18e.mp4?token=Lf0lDqWRJEFrli2IClUQHQGq8QCxETQWaCbc0b52zVnhbLkAHZrSvU86xGIhN_kzUBfmk_T16DWHeyKHiPxglahncAzQ1lsX6KUijgNW3SSxrw6IzZ588DfpWIdFBmmDK2KBoAJiyPiAXYdzg1WWPdFVavz3ucF3ldTlk7ZXyl9EV1guVuiT7rAwwqNXZP320zwapD-TK5dAQiqiN7RWcQDSa16pVMuyPWhaqsnpT0lzhyhkyQOaBFlY9qD4PppTFIq8ol4UErjAHoW-IsnzJKK3Pz4rz7Oga5NQ-PU20STiuxJQ3ZosKzpxV6_BekPKyylYiq8E-ahv2PiNR_tpow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شجاع خلیل زاده میخواست گل بزنه و تقدیم رهبرش کنه!  ولی اراده خدا تحقیر اینها بود!</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/farahmand_alipour/5772" target="_blank">📅 09:32 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5771">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d645372fb2.mp4?token=u12lgC8LxJEnPSjP64PadKbb_0PXvpZjfBb9Fhhh38Yi4vFTTgWlZduZTYMCV8aPA3j2eyGY7apT-uQs1t0GzWpUT5gsm1K7dCFp-xvhargzx4mxJ4toelmowasYZY43ywGZnLnuxbfocLKuquKsrFKnQ24WhxLcHuEkkIXyeTzRVK-dVyqRQ7IcONl7GiML9vtP3PHoGFVIi1zvVVY1AhyF6vteNkdU_dI55n7fcld0oVw3ekRL8pdUFIoGr7rAnsApi0fQQZvJdmj_UToajbfkvd0C7ST25_MmyF0lM914K88GN39cwwxytIyUBu0KI5CjdskD748F_wZ_Si9SGjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d645372fb2.mp4?token=u12lgC8LxJEnPSjP64PadKbb_0PXvpZjfBb9Fhhh38Yi4vFTTgWlZduZTYMCV8aPA3j2eyGY7apT-uQs1t0GzWpUT5gsm1K7dCFp-xvhargzx4mxJ4toelmowasYZY43ywGZnLnuxbfocLKuquKsrFKnQ24WhxLcHuEkkIXyeTzRVK-dVyqRQ7IcONl7GiML9vtP3PHoGFVIi1zvVVY1AhyF6vteNkdU_dI55n7fcld0oVw3ekRL8pdUFIoGr7rAnsApi0fQQZvJdmj_UToajbfkvd0C7ST25_MmyF0lM914K88GN39cwwxytIyUBu0KI5CjdskD748F_wZ_Si9SGjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شجاع خلیل زاده
میخواست گل بزنه و تقدیم رهبرش کنه!
ولی اراده خدا تحقیر اینها بود!</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/5771" target="_blank">📅 09:31 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5768">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HIF3fjjAKHI1Qn_81LHTTtk6fom0Y-MuwSdJ_Ij4p0fPz6kH53XtiPJemnW1IyxDMgxE5A1B47EIV0BrVnt2lhqocdz_dPqvFfLYesWJmIjQNvCDWQ6oc1oaZxFQXOpur3KZlm-OX4mpmJhrYuOk0Gbfrs8OgnDDLWH7V4I1jdAKroJWBYwlqSrXQdOEEcOkEeuXyye5WMGlzac4nXmwL8Zz9mgIaF_NpjbAvVHDJcU1AjBRwh1RvbSL6dWGZNdktFUnmcrhqSDWAXdazAifA2IevQbEZnrBz1Cya8JWITSMaCaTL_Rp0WwNMLxjRIyxykPkEo4DV0c8ky5UtDqFaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XGWoY7W8X5tSTzq2hT5LSo-YoKAt4xo3EhSzrI2R7Vu23Ne8nCkQpjE3uB_qBoMzLeCDfMCRThDCn5ujomivItzTpr-8CaFRQ0QUebJtLOkk82LpZY5chz23HuaHi_s5s75PltbICzKu3fQhxFxRoKsQEmJccQKft_NkIA_NhFLZrgL9fyM_oqqS0rjmVEgQCogrbyGj7oJQBUS96WJ-5U1klkUL6TlzQ_jY4EdsZxeGbaLatarw5f5uhuPptZHTB15IMTXBkGI2op5l8_CRkDQjZ621qIHzGTyQeyhUWtWULAQECSM-sPEsyISUAUqE6AiOIYmxQSOsMN_qPtpA8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rQJxkAGkOBh0UMdbG2fVvV8Puadxb2r8rFQPH5gLe2hQ9QViZoYyoSFJ6qSwQoLLx60n0ZowJrG6ypifyoCfFdxSxfF0JZB6DWbUbw5J2ikNJyl_qV58hRAkkHvhxXO0FdcCUy3DpT3sVfyJ8ZPY-aG1uv3PDoPaMGHCY1G5meDMBaRQ88g_zkb5mrnhC9ZVcY-Mt9RzpNtNgFdPlxTBirtUYnK2CRJ_C6tbcxRMh_SMHSkJExaal6c-GAxWkdEbPaul4JKVmQm45OoRvUELpKF8Tx30yPTXvl2hLiNQv8bJLFkHYqK2qFk-Wdzm0DElf8VcGxcJMyHv1ir2lQGrAA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">در جاده فرودگاه بیروت، بیلبوردهای تصویر خامنه‌ای رو حذف کردن و به جاش تصاویری از «اول لبنان» زدند،
که البته دیشب برخی از اعضای گروه تروریستی حزب‌الله رفتن و تخریبشون کردن.
بالاخره زندگی و حیات‌شون در مزدوری رسمی و علنی برای جمهوری اسلامیه.</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5768" target="_blank">📅 09:26 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5767">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">تیم ملا</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5767" target="_blank">📅 08:52 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5766">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/10689e4ea8.mp4?token=IdXpb45jrLzQQ1qcm7BvQPNvmNTtLNmFRWx9tjeu2yYK4f-JWR0xMTNdmOR2435tVj7IG6IcwidiyJJ5RzLGHEcwUoX-Go4adAQUH_fYveqAgEnlPp8DcVR41h1xxgbNy5NypVKXgoXPbHQ0eSGELO8mfLnEmuMhTu8XmiCCqGqpCc11TDpi2Kr9YsHwr0LGeEtDJRjdZeEzYfp7DEKb3rHmP-k1B5qZjWzYRyks8EZGmafKgfCLG5f8_fEgup9BZOtBhR-DRT1K8aanBO__B4qaleGomVT4meJchx8CkVexXMaPwfKzp4PF5JCj2tu4aw9zzpxVVJ6N1HidK9lRwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/10689e4ea8.mp4?token=IdXpb45jrLzQQ1qcm7BvQPNvmNTtLNmFRWx9tjeu2yYK4f-JWR0xMTNdmOR2435tVj7IG6IcwidiyJJ5RzLGHEcwUoX-Go4adAQUH_fYveqAgEnlPp8DcVR41h1xxgbNy5NypVKXgoXPbHQ0eSGELO8mfLnEmuMhTu8XmiCCqGqpCc11TDpi2Kr9YsHwr0LGeEtDJRjdZeEzYfp7DEKb3rHmP-k1B5qZjWzYRyks8EZGmafKgfCLG5f8_fEgup9BZOtBhR-DRT1K8aanBO__B4qaleGomVT4meJchx8CkVexXMaPwfKzp4PF5JCj2tu4aw9zzpxVVJ6N1HidK9lRwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فقط مدل گزارشگری فوتبال رو!!
یه کشور مسلمان [الجزایر] داره کاری میکنه که یه کشور مسلمان دیگه [تیم ج‌ا] تو دور بعدی باشه!
‏یهووو یه کشور مسیحی[اتریش] گل زد و اینها هم حذف شدن!!  :)</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5766" target="_blank">📅 08:43 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5765">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17301f18ad.mp4?token=QULzo3rvzxGgtlWKbr09sAjSPdBNLTTD6v4ZnFO0pB-mF8HJbDAFMF1UVBRtzUIfdobam9wrfnicbWw69Sa9ne42x177tzGSmC5cVhwpisHBfiSUOOJNMRHklUGbL7FUhFewM8f9UTea7YYxWrIZVVwR2YwADLb4ZBaVviEU74dHdhA5HZyOfa0mViNiNFiufRGoxSt82afiYFnhqWJlfy8eqPPnJdmJuhT-Fatqf3-Dpm03dm2AfkLJwwDb-VDd3qa_cEgejAl-1W35A2EifYsy_-CMQC17meJSicJSEsXVftGuTO1-P5trXE66yUnnJF6QXMs7wjDqmRYuDLPLaZk7ym4AGOfkBogEoZ5ON2kBr64CQ7Hgr6nWlwB1Yxt8F-hZm50W3qRoHTV_wIcyxNJaY7VWD20mEsxC456djGNgIrlnL5AHWq_VcG_8KLJ8IDPXO50XkMJ4ktDTzfNBzALIlayLtb_4UKMqiUDDRUbV67TwwR1lqc79n7wdeyVzocVUW2PcWskFO7cNxjh5tlX3IFVRqisFXWy_V78YMnXz4hkjBiGG5DFJiaRePUlycmrS2VQdYMcNp-3M0IdEzClwerX7b8pQnBPFLHQA365WSQ_Xzw5jOChFFp08tA8UUcsltrnDbTdjQBgMQr9-YhcMthjIvI6Kk_PzGvEUh00" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17301f18ad.mp4?token=QULzo3rvzxGgtlWKbr09sAjSPdBNLTTD6v4ZnFO0pB-mF8HJbDAFMF1UVBRtzUIfdobam9wrfnicbWw69Sa9ne42x177tzGSmC5cVhwpisHBfiSUOOJNMRHklUGbL7FUhFewM8f9UTea7YYxWrIZVVwR2YwADLb4ZBaVviEU74dHdhA5HZyOfa0mViNiNFiufRGoxSt82afiYFnhqWJlfy8eqPPnJdmJuhT-Fatqf3-Dpm03dm2AfkLJwwDb-VDd3qa_cEgejAl-1W35A2EifYsy_-CMQC17meJSicJSEsXVftGuTO1-P5trXE66yUnnJF6QXMs7wjDqmRYuDLPLaZk7ym4AGOfkBogEoZ5ON2kBr64CQ7Hgr6nWlwB1Yxt8F-hZm50W3qRoHTV_wIcyxNJaY7VWD20mEsxC456djGNgIrlnL5AHWq_VcG_8KLJ8IDPXO50XkMJ4ktDTzfNBzALIlayLtb_4UKMqiUDDRUbV67TwwR1lqc79n7wdeyVzocVUW2PcWskFO7cNxjh5tlX3IFVRqisFXWy_V78YMnXz4hkjBiGG5DFJiaRePUlycmrS2VQdYMcNp-3M0IdEzClwerX7b8pQnBPFLHQA365WSQ_Xzw5jOChFFp08tA8UUcsltrnDbTdjQBgMQr9-YhcMthjIvI6Kk_PzGvEUh00" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب خیابانی پیام عربی
به تیم الجزایر داد که ای مسلمین پیروز بشید بر تیم اتریش،
تا اینطوری تیم جمهوری اسلامی
هم بره مرحله بعد،
ولی اراده و برنامه خدا
ناکامی و شکست جمهوری اسلامی بود.</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5765" target="_blank">📅 08:36 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5764">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/27a845337c.mp4?token=nIXV3aAW3PX-_1aQm7NrlkbFFCfK2Od3F3ykrH7dzapaEqrT1VufsLpQ6GMsIFTy0Za7HMnccdc9RJ7IbQz1Ls7DqKa49zqSDBRokzv0hDTVgxi148zrLsK__kJo-Vw4CAoP09GRP7lq8XhUAhOMp_JlpcTHZGPY7SAvOIh0Yl9XST_0f-cHdXLKB6ZaVB8iDy_erZ4NXjbMKQMeGgGMP-3RCy9OS2EBA2q6OPilndRmcIkZDMMFqf3VzmSpeCglIPYQclBCgI9kZ7mlNUxAEDf0y5xsZSB_UGj16BJbM7Hujq84hemkksbF14d5HbtCZvGLwns8074H97zA5b5_Fg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/27a845337c.mp4?token=nIXV3aAW3PX-_1aQm7NrlkbFFCfK2Od3F3ykrH7dzapaEqrT1VufsLpQ6GMsIFTy0Za7HMnccdc9RJ7IbQz1Ls7DqKa49zqSDBRokzv0hDTVgxi148zrLsK__kJo-Vw4CAoP09GRP7lq8XhUAhOMp_JlpcTHZGPY7SAvOIh0Yl9XST_0f-cHdXLKB6ZaVB8iDy_erZ4NXjbMKQMeGgGMP-3RCy9OS2EBA2q6OPilndRmcIkZDMMFqf3VzmSpeCglIPYQclBCgI9kZ7mlNUxAEDf0y5xsZSB_UGj16BJbM7Hujq84hemkksbF14d5HbtCZvGLwns8074H97zA5b5_Fg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
تیم فوتبال جمهوری اسلامی رسما از ادامه رقابت‌های جام جهانی حذف شد!</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5764" target="_blank">📅 08:26 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5763">
<div class="tg-post-header">📌 پیام #39</div>
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
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/5763" target="_blank">📅 08:18 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5762">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🚨
🚨
حمله به جزیره قشم
امشب، دومین شب حملات آمریکا به منطقه تنگه هرمز است.</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5762" target="_blank">📅 01:40 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5761">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VtF-5pthzXwSRISmR-aDY_m1QDC3lYmKVpWamYGRJ_0hhoT60GOzTrd_2rdSS05FQ7uDyeyrViZ5OagcUjtXSwoqDnv6LN7rvmdajc-0yBxSHDBSXVdm2YaFkeVlcHyFI56Hv64SoSgn-ksbk6rGCv_bja4q5HvwOkSXtVWFkBht-_rVXyGnAsb2Zy9Fy9ibvRkbXtLd7RMQ4VQUDn8V2-q1beGYb-4L3ZcPKY15uLJNr3hat6T8NaQfE-zw6Gg3qVR3C6PL-xsKWDhTndJicik_pHtsecGq2rQiNewEhJMb2gzwuFPS7LtV5zvHVV9JFrlpXwHoRKmCm7HpKMq5FA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🚨
🚨
اکسیوس:
‏ارتش ایالات متحده در حال انجام حملاتی در منطقهٔ تنگه هرمز است.
این حملات در پاسخ به حمله جمهوری اسلامی به یک کشتی تجاری است.</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/5760" target="_blank">📅 01:10 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5759">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">‏خبرنگار صداوسیما در سیریک:
‏دقایقی پیش صدای چند انفجار شنیده شد.</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5759" target="_blank">📅 00:56 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5758">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0cee64931e.mp4?token=kPbjLZ1DreRAqQfOeEm2Lp2vpSznEnqo1aRGZKBRaFtruIGJdEnR1RBbY_Q9DgRx2oXMaQ8zcfVU11VTwsZFO5BjXgIT2bFqxGIFkpLuUjc4KAoCcbZpp3WeyU5AgNQtzbhig2mvA1MmtFqtfcDf-wCb3s5jKmswlFACmtMKylHP6lXjbWA3y0BKSDZ42Kt30PqQ7e-gNVc3BYbF0jWjsf_zGecxtXe7mPvrSMj2RLgNFcP4TLso3NpvLwySgH5gRbZe2oHRkAxNLd5KDendL_vzAxNTdm5a5E6d1R9lBg-_ms_hwH72eIfERYvx6V-0zvj3yeahwJ8q67fR3rJuTgUe3AgILSC7VTkENHssZPY2RcW-hRn9U77sD3pDPbJNco7W8dRpPuErbEMaZQpdWkSNZb2dNmPr4TMRVEq4ggE0eLyR6vQ2QOIhlrvC-GZgeLxXEQFqoA2ndwyJkX-qzfFFAJAR3gXvIhmT9FSRihM6kXN5iSXaHAu4w4ZWkF0ZiSOOe1Y_L2ccRk1hQyPOVyaHGN29ar3i5mn4o5JLhXvB7NJa3VEHhJTm44NZCvCekFteCtpgnqYdX8VidohHd9vdL4QKDjLZKbrlE6ddWBRv--euVIA7tp29Y4j7EA83nSyV5xJF2Pv2G-ao5JHA2w6oV1K4agyCT__GRsaQACE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0cee64931e.mp4?token=kPbjLZ1DreRAqQfOeEm2Lp2vpSznEnqo1aRGZKBRaFtruIGJdEnR1RBbY_Q9DgRx2oXMaQ8zcfVU11VTwsZFO5BjXgIT2bFqxGIFkpLuUjc4KAoCcbZpp3WeyU5AgNQtzbhig2mvA1MmtFqtfcDf-wCb3s5jKmswlFACmtMKylHP6lXjbWA3y0BKSDZ42Kt30PqQ7e-gNVc3BYbF0jWjsf_zGecxtXe7mPvrSMj2RLgNFcP4TLso3NpvLwySgH5gRbZe2oHRkAxNLd5KDendL_vzAxNTdm5a5E6d1R9lBg-_ms_hwH72eIfERYvx6V-0zvj3yeahwJ8q67fR3rJuTgUe3AgILSC7VTkENHssZPY2RcW-hRn9U77sD3pDPbJNco7W8dRpPuErbEMaZQpdWkSNZb2dNmPr4TMRVEq4ggE0eLyR6vQ2QOIhlrvC-GZgeLxXEQFqoA2ndwyJkX-qzfFFAJAR3gXvIhmT9FSRihM6kXN5iSXaHAu4w4ZWkF0ZiSOOe1Y_L2ccRk1hQyPOVyaHGN29ar3i5mn4o5JLhXvB7NJa3VEHhJTm44NZCvCekFteCtpgnqYdX8VidohHd9vdL4QKDjLZKbrlE6ddWBRv--euVIA7tp29Y4j7EA83nSyV5xJF2Pv2G-ao5JHA2w6oV1K4agyCT__GRsaQACE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جاوید نام ۲ ساله
💔
‏فرزند ایران و جان فدای میهن، جاویدنام علی محمدصادقی، کودک ۲ ساله، روی شانه‌های پدرش بود که با شلیک گلوله جنگی کشته شد.
‏پیکرش را همان شب تا صبح در برف نگه داشتند و روز بعد به خاک سپردند.</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/5758" target="_blank">📅 22:09 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5757">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EeclZWPxRlYliqpK4oGDN6H6TLudOItAsr3zLJA-rAtmQpTiaZpullNO_hBMZxz2eMJFsGNF9X1HPKWzxzPXVZR_TzpFY-dfnuGhyVh6oQNXdI5FLy45dHeWFZ51EB4_bME78e0eLexvWcmlOuKezzYLFmvgclEFISTDOky7i3znKKn3aKO6ictKYOSFfor12ZsIub2IM-YHL2ceIa0eYxbzHDj4OxQeZqMqn_4YyCKDxqs4UMn4SGt2RtmqCAQwKiGGX_Te8LasMniW2Fikm1s149hgRe-gvV_GrL-Sk-kqn6fYPY9PAtKVpptlE9-Dnjog9h33m6wj0Hep5WYXgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
پنج حمله هوایی اسرائیل به نبطیه</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/5757" target="_blank">📅 20:23 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5756">
<div class="tg-post-header">📌 پیام #32</div>
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
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">دبیرکل حزب‌الله لبنان، توافق میان‌ دولت لبنان و اسرائیل را که بر مبنای آن حزب‌الله باید خلع سلاح شود و سرزمین‌های لبنان تحویل ارتش لبنان داده شوند را رد کرد و بر ضرورت نگهداری اسلحه تاکید کرد.
حالا این اسکله براتون چی کار کرد؟ یه جنگی شروع کردید و یک پنجم خاک لبنان رو دادید و فرار کردید و از دنیا خواستید بیان آتش‌بس برقرار کنند.</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5755" target="_blank">📅 16:48 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5754">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db5841aafe.mp4?token=fQraopmtdYdaK6B9esOtEhbHKD_y9KfcM4dyLHOYlh3dN5VWkcOrDbzKb8M0iT-UAcjwicTM3IB0S6gNJIUhBPLyAMxdu0o76DTj5AiEzChiiWdhFz8aHIMlZwmt9lUrZXKI60ssjimtrKI1819F5r2r1I3MP5aciBn57-QqXXA2tOOPoyfqm-qADz4yUS9TorBzngI5AbU-wc-eEyUdrd_T8aSQiQGOamuV-r8ZwtKMtZYIunX-Hk0jMUnneehwB2ub7hxzEua9oqNikl4L1QoDiBnqxZNRfx9K5ZdeOAlTHFVEpQ9T0JgEG6Wo6u5z1U5G5bfNV34IDfQaA87ppg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db5841aafe.mp4?token=fQraopmtdYdaK6B9esOtEhbHKD_y9KfcM4dyLHOYlh3dN5VWkcOrDbzKb8M0iT-UAcjwicTM3IB0S6gNJIUhBPLyAMxdu0o76DTj5AiEzChiiWdhFz8aHIMlZwmt9lUrZXKI60ssjimtrKI1819F5r2r1I3MP5aciBn57-QqXXA2tOOPoyfqm-qADz4yUS9TorBzngI5AbU-wc-eEyUdrd_T8aSQiQGOamuV-r8ZwtKMtZYIunX-Hk0jMUnneehwB2ub7hxzEua9oqNikl4L1QoDiBnqxZNRfx9K5ZdeOAlTHFVEpQ9T0JgEG6Wo6u5z1U5G5bfNV34IDfQaA87ppg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">:)</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5754" target="_blank">📅 16:33 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5753">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f038d1dce.mp4?token=ERtGPzQLr3uHuYzdhcbGpfTYRe1yBvx0KBeLuC-QkqHLndJrsMK9VCkXxJe8dkl02plXKep83enwK7A7e7sKy-kGJS61Z_QD8pBLQ1PiEOA9qOXuYAMR4d_uesI-CzJ1u8gOpFKnUp8kCkEGM_zc-Huz3jhWLZ2Y0p_SaYSgKqR84omGdYLuXZrGu1hpBQKxX4PZe0dFUqp97miTPCdzZuxnLBdwilhqz3TbnIYmMbSGtZvSy7ucQ0ndbNHGYiL_FdgJTiswvmlKRs7PBK7Hs5QfppwKeZNVSt2SuozdTfr9vpRyqYdDmTI8CDDysAiEEmMb8L1jShWbkw6v-cEM8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f038d1dce.mp4?token=ERtGPzQLr3uHuYzdhcbGpfTYRe1yBvx0KBeLuC-QkqHLndJrsMK9VCkXxJe8dkl02plXKep83enwK7A7e7sKy-kGJS61Z_QD8pBLQ1PiEOA9qOXuYAMR4d_uesI-CzJ1u8gOpFKnUp8kCkEGM_zc-Huz3jhWLZ2Y0p_SaYSgKqR84omGdYLuXZrGu1hpBQKxX4PZe0dFUqp97miTPCdzZuxnLBdwilhqz3TbnIYmMbSGtZvSy7ucQ0ndbNHGYiL_FdgJTiswvmlKRs7PBK7Hs5QfppwKeZNVSt2SuozdTfr9vpRyqYdDmTI8CDDysAiEEmMb8L1jShWbkw6v-cEM8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جشن و شادی در غزه
در پی‌ موفقیت تیم فوتبال مصر
در برابر تیم فوتبال جمهوری اسلامی</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/farahmand_alipour/5753" target="_blank">📅 10:20 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5752">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b07e212ab.mp4?token=UkAXot2EwTBJE7-uYUcHdhh1UV5AnmHDscuOQSiQNUGTqloJLLmQJsw5DDRZh5UuJwmD_8gbi4gkzG7Tr_hJtq0b1RBHTQHba6JuIxmKoKnRmJrio2zMRPcZQThyhCaUsBzhq0tw1HozEHbHSukoJylLNF2pNsXPmbuxz4dDmIijfiSBkDV1SOcCIiWWJ3ZD8XnFKFz7pWwBWxxG6jswPamFS6xdlM3pMT0PHkSHQe58iGT-pKHZeC4NJe70FgD8u1Oe8eqEKQ6TH5L099bLkRtIrOrHQZgXlZAAUTP6SsKjWTV8Bv82fn5pTykAEJ1S3_N0E251AZNg-8BoJ5YznQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b07e212ab.mp4?token=UkAXot2EwTBJE7-uYUcHdhh1UV5AnmHDscuOQSiQNUGTqloJLLmQJsw5DDRZh5UuJwmD_8gbi4gkzG7Tr_hJtq0b1RBHTQHba6JuIxmKoKnRmJrio2zMRPcZQThyhCaUsBzhq0tw1HozEHbHSukoJylLNF2pNsXPmbuxz4dDmIijfiSBkDV1SOcCIiWWJ3ZD8XnFKFz7pWwBWxxG6jswPamFS6xdlM3pMT0PHkSHQe58iGT-pKHZeC4NJe70FgD8u1Oe8eqEKQ6TH5L099bLkRtIrOrHQZgXlZAAUTP6SsKjWTV8Bv82fn5pTykAEJ1S3_N0E251AZNg-8BoJ5YznQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش لبنان برای برخورد با حامیان گروه تروریستی حزب‌الله وارد خیابان‌های بیروت شد.</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/5752" target="_blank">📅 02:02 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5751">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🚨
🚨
🚨
حمله ارتش آمریکا به اطراف تنگه هرمز  ‏فرماندهی مرکزی ایالات متحده (CENTCOM) اکنون تأیید کرده است که هواپیماها در اوایل امروز، 26 ژوئن، به تلافی حمله پهپادی دیروز ایران به یک کشتی تجاری در تنگه هرمز، حملاتی را علیه انبارهای موشک و پهپاد ایران و همچنین سایت‌های…</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/5751" target="_blank">📅 01:17 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5749">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q-EUULPM0u6JISnx3KkOnPWzzCQKN2deHQpYa25eIluicpLvqpwyeI6BIwb3vCtQVzgrA382H5E6FRJLo1N63I-MkwNcFSwP9LjSovejJVzuPtRaH0iBBNwGo42pk7rByx4_jOcbAdifu-VJtAHXclD1Vu6Rwy_wXCFMubdehH-j9o_HagSM8HQonZdM36DbkoDcZNgC99TroZD-ZPu3n1C4hLmrKB5Avhg6nOxFIQI4cXNa70pBJc1ttove5l-SY3hK0KLQKHYkqxUJ7JZS5jlDAEP5-RVak3qvBA_8er8XEhJqMhAWnymrprXzvlqGjxPiu_DV3gOgQlFKi3IuoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/farahmand_alipour/5749" target="_blank">📅 01:02 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5748">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YlC76umdQOngHWQpRjHlQ4agaNuCuxeVnGqw627J0xz9sBJxo1r8Cmivs7lB7VmYCJGpSse_5ir1XXnUL9kgo-PBOZXqKaQi8xGxUZ-vjcyaibghMrzZ4pU_WqkUZ7-iCihUfkB44b_mR7FNKrbX4CqfFfXLzzDdDhGd9KtGtFugBtP029NZbaTSvmc82OKckz2jjM6Wfwpp2rZMnxQqhXe7-Iggyx_WjdDhcaack6qtBNwpV4gwttsmBqOmHGdtLL4NcgXSRFOJe_jYlSYSXiuuBaZSdq27pY38VV_QamOsCmMFHvc8ZPd8nJhnhjMALQnBcFwdmRgEH3n6yCbFiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش لبنان برای برخورد با حامیان گروه تروریستی حزب‌الله وارد خیابان‌های بیروت شد.</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/5748" target="_blank">📅 00:59 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5745">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e245d71920.mp4?token=r1odpbV3_eWo3ZYVuxKMJ-ZazJN0BpkQeKU9sy8bqCIEAalFlDgYrEKSGokQvYiWvvhfO8-0M0S7ReY1IkL4zPSYO6kBZmAYPiXhhOo2IjfeL4bgkUKBprlZvJylfyfvMmqrQOZnBVLNx3YGWeH4QDSxzQ0DxSJim6zIUv4fb3q5_duY4oKIURIGmfIV6-B9sfqnL-cm3W5eJXxt2jOZtJoU8j9kkrBsSDhewItNL3JDqlN0JE9s1S4JYLLgJvgsjhGi6TFl3rn1Ox7BZ17pD41FdXyUbUoxFQQ0H1xcLkwSp05VTDPp3OUzfEQueN22N8TUWi0UMP8t6HmQ7pKMsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e245d71920.mp4?token=r1odpbV3_eWo3ZYVuxKMJ-ZazJN0BpkQeKU9sy8bqCIEAalFlDgYrEKSGokQvYiWvvhfO8-0M0S7ReY1IkL4zPSYO6kBZmAYPiXhhOo2IjfeL4bgkUKBprlZvJylfyfvMmqrQOZnBVLNx3YGWeH4QDSxzQ0DxSJim6zIUv4fb3q5_duY4oKIURIGmfIV6-B9sfqnL-cm3W5eJXxt2jOZtJoU8j9kkrBsSDhewItNL3JDqlN0JE9s1S4JYLLgJvgsjhGi6TFl3rn1Ox7BZ17pD41FdXyUbUoxFQQ0H1xcLkwSp05VTDPp3OUzfEQueN22N8TUWi0UMP8t6HmQ7pKMsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حامیان گروه تروریستی حزب‌الله
در اعتراض به توافق دولت‌ لبنان و اسرائیل به خیابان ریختند
بر اساس یکی از مفاد این توافق حزب‌الله باید خلع سلاح شود!
اینها مخالف خلع سلاح هستند! تاکید بر مبارزه مسلحانه با اسرائیل دارند! جنگ رو شروع میکنن و بعد سریع از همه دنیا میخوان بیان مداخله کنن برای آتش‌بس!
خب مبارزه کنید!</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5745" target="_blank">📅 00:49 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5744">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lFVv7NaMJUJs4FXG_6sjayLe6t9scTIPUEpLOtfc4GYUmiPQu9cHa3fWzced-YkZC6_oNvemLX8VBJOSdVW4A_7d65rjp03I5ghtROSjVzT4x1SLtZQYQxOaRaoEhybO3nnCcnTaig6JcP0carVfRnd26qr5ZgHUKCzK_3iD8uwvgJm96GUR3XNW5qGrvp8ncLqELiGI-f8PcQ7pH4LFPK1dlKs9cW57Vnr9G6XU69Q1HKdELH-t_xuALipDrCoHY9c3jxVSOshLZcIlRck6jI6adnM9Ke89NwPlQaYxyzpO6SGit2dds1_mv_8AwTxst-YuQP7yXdvRMVuPZpYpzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/5744" target="_blank">📅 00:31 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5743">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E_oHzU2TOuyi_ZQ7XTz9Jh9ICNydj5qSM9SsejVQh3wrYlEI6vquwiPyM4JOFwK3FuWuGZFw6mjWNGYHjGjiU7rfsVuiHmy94VmbHXSBh0WvqKOiVWvIkiByRXLNLJa6PSSoBBAWnVBfQYbrzt-0zB2E_q2ToaPKfOJW_daGzaKf_nXnjp_5-VwVbahICHkIqfOITTyP5XRyvjYdXtGMqGPtZ2gdNp-cJAlpbgfNXL5CZdYA1aF1u288xUhI1oSmq-U_A7ptJKmWIgqoEG9WcqQGAG9qPu1OM__SVoz4wcDDAoGdhLpL-GYglCw1RadeWS_JRh0SDJIxuUo6wx3Uog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
حمله ارتش آمریکا به اطراف تنگه هرمز
‏فرماندهی مرکزی ایالات متحده (CENTCOM) اکنون تأیید کرده است که هواپیماها در اوایل امروز، 26 ژوئن، به تلافی حمله پهپادی دیروز ایران به یک کشتی تجاری در تنگه هرمز، حملاتی را علیه انبارهای موشک و پهپاد ایران و همچنین سایت‌های رادار ساحلی انجام داده‌اند.</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5743" target="_blank">📅 00:27 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5742">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac9a1f1d75.mp4?token=IfaVDXztZDYiqMNi6v_jj5gj6WM1YbqNLIcKyAbA5bffZ3ELAmMptq9536jfIQYo8BxETKRKwG1EKbMOHoFzFlOEHY7KMRZ0zkZuSFXYMllDJAKtKm8E-rxt13b8u9ULKdW7EM6eZQ3G9u5mJFmuQoy0pzgaYecAb1PkaD67pMHaQUvx1s-wsW57-AVLZxvtBCsuAKVW_L0CIFBs0UpxwovmBL9w_h0J3dKjBho_eYvbrSSWjpU-d8EY3qvHqXPDEJeusaKUMi03ZPZx6k6cseyuHaVWKymvRYRgenY44ymfgib-7IoaJIJBSUxZEuaGTsP3foIzNTnnaus_tQ-iSB62GUEuAr1A10RsJRBFcBZmT3-WG9ZRRhtYgohR4oD-YlnKQ92KgtSKk0k1rTmilIEu1puEHTs9yU1df6LXvO14Xlbacv8-45vFGWCdaHMo-UPunGVGQx1lM6vXWo-7Czbz6-2UFmoLPfAA0VqfOZ2JmiJGgVjiOGJhE15MXkT0YEgs49zDakX9kzMqBPaELEoZpVHBGsgbCp0RMHjougmLsz1FprVlyE_L29XgR_tQIEp0Rat6vJmYZ_OpfDsxXLO5bcrN7kejbl4y0a-4t9wmVE_lgLER-IthmbJX6tFHSIu7x8dmGcfc8QWQeDQSc3m51x3zy-zN_1S8vA3wq7I" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac9a1f1d75.mp4?token=IfaVDXztZDYiqMNi6v_jj5gj6WM1YbqNLIcKyAbA5bffZ3ELAmMptq9536jfIQYo8BxETKRKwG1EKbMOHoFzFlOEHY7KMRZ0zkZuSFXYMllDJAKtKm8E-rxt13b8u9ULKdW7EM6eZQ3G9u5mJFmuQoy0pzgaYecAb1PkaD67pMHaQUvx1s-wsW57-AVLZxvtBCsuAKVW_L0CIFBs0UpxwovmBL9w_h0J3dKjBho_eYvbrSSWjpU-d8EY3qvHqXPDEJeusaKUMi03ZPZx6k6cseyuHaVWKymvRYRgenY44ymfgib-7IoaJIJBSUxZEuaGTsP3foIzNTnnaus_tQ-iSB62GUEuAr1A10RsJRBFcBZmT3-WG9ZRRhtYgohR4oD-YlnKQ92KgtSKk0k1rTmilIEu1puEHTs9yU1df6LXvO14Xlbacv8-45vFGWCdaHMo-UPunGVGQx1lM6vXWo-7Czbz6-2UFmoLPfAA0VqfOZ2JmiJGgVjiOGJhE15MXkT0YEgs49zDakX9kzMqBPaELEoZpVHBGsgbCp0RMHjougmLsz1FprVlyE_L29XgR_tQIEp0Rat6vJmYZ_OpfDsxXLO5bcrN7kejbl4y0a-4t9wmVE_lgLER-IthmbJX6tFHSIu7x8dmGcfc8QWQeDQSc3m51x3zy-zN_1S8vA3wq7I" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اگه خورده گرفتن که چرا میگید سگ هستید …</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/5742" target="_blank">📅 19:53 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5741">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fad365bb7a.mp4?token=ZDr-STvQFPYHiROFw6OPE7okjr7IEHAwGcDfqUYyBg4k0-Dvk9qRQIKcE5xG2aewUJ912dVo_83a_jiYAwUcvSQphHICVJSnFHRCEsILiVyq2xA7qkuZr3bk5_ki9cNSYAuQW9RXOvqhjOSU2zL83IZYkxIZ15AIiPW56JRm1EuZ3RUKct9SeWjS-LFiZfgVlvHezTVkjslzw-S6Ybnjf4E8HQGRf9U2lczcyRXgE_g6QFYzHZV-PLIL5FT8yd0mL40Sp7E4N3lG-LybSPWDd_qpdQBnRXlbNlM4oOGZPr3XikHkTMJCVShwXA1Nnrb6TaFoTfgoL74RMT_P6d5E65P3JaO1zR0E2My4HBpfQaUPvqNY2jkVJxq8aBaTHdh2pTC_QSuEGz3EwOiTOz0Q2BU5Ex029vIMd7wPDONB20Gsqh11fba92Ym9ha0qqVc49qdTIpvpgQ8OpXr2ck4WIxVGBojJjhstpzJEWlIsJIcYXKVFrlr05QGQHuinRgne5v3NuQtk2Kkn7L7ggmUjxoL2-pupn-oSXqMBEcRUxsnlE8GXrWkcuOU_-px0uEHkmk-bufeK8k_oC8xQ8Q-MIM6L_Wod_xgYBRIiHrXVyNBd9zLCNVOr7-EEnid0zQaByZfjfAYT6g3wAbpNr8fbP8EwIDhduGwh2PJR9mjhb_o" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fad365bb7a.mp4?token=ZDr-STvQFPYHiROFw6OPE7okjr7IEHAwGcDfqUYyBg4k0-Dvk9qRQIKcE5xG2aewUJ912dVo_83a_jiYAwUcvSQphHICVJSnFHRCEsILiVyq2xA7qkuZr3bk5_ki9cNSYAuQW9RXOvqhjOSU2zL83IZYkxIZ15AIiPW56JRm1EuZ3RUKct9SeWjS-LFiZfgVlvHezTVkjslzw-S6Ybnjf4E8HQGRf9U2lczcyRXgE_g6QFYzHZV-PLIL5FT8yd0mL40Sp7E4N3lG-LybSPWDd_qpdQBnRXlbNlM4oOGZPr3XikHkTMJCVShwXA1Nnrb6TaFoTfgoL74RMT_P6d5E65P3JaO1zR0E2My4HBpfQaUPvqNY2jkVJxq8aBaTHdh2pTC_QSuEGz3EwOiTOz0Q2BU5Ex029vIMd7wPDONB20Gsqh11fba92Ym9ha0qqVc49qdTIpvpgQ8OpXr2ck4WIxVGBojJjhstpzJEWlIsJIcYXKVFrlr05QGQHuinRgne5v3NuQtk2Kkn7L7ggmUjxoL2-pupn-oSXqMBEcRUxsnlE8GXrWkcuOU_-px0uEHkmk-bufeK8k_oC8xQ8Q-MIM6L_Wod_xgYBRIiHrXVyNBd9zLCNVOr7-EEnid0zQaByZfjfAYT6g3wAbpNr8fbP8EwIDhduGwh2PJR9mjhb_o" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همین‌ها رو یک تلویزیون غربی پخش کنه، سریع میگن این برای اسلام هراسیه!</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5741" target="_blank">📅 19:50 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5740">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">ترامپ در شبکه «تروث سوشال»: «جمهوری اسلامی ایران دست‌کم چهار پهپاد انتحاری یک‌طرفه را به‌سوی کشتی‌هایی که از تنگه هرمز عبور می‌کردند، شلیک کرد. یکی از این پهپادها مستقیماً به عرشه بالایی یک کشتی باری بزرگ و بسیار گران‌قیمت برخورد کرد. کشتی آسیب دید، اما توانست به مسیر خود ادامه دهد.
ما سه پهپاد دیگر را سرنگون کردیم.
روشن است که این اقدام، نقض احمقانه توافق آتش‌بس ماست.»</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/5740" target="_blank">📅 19:23 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5739">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/726fb491ae.mp4?token=kDXJLGApS5qxf80xISqH_g6LcuFgC1e1TQVfqow6RPdxlUeuAMO0QTP0V0Ql433-JiVHEaSPaW1MFBd5UKM1nSBeZgKfJsMfUgapkpw_jQh2A6Tk08Ven5wu77JUJlf_63L0Sf9UkEv8Xe0DGG08cLkLKN2nVDukH09rQtJzpfJct3QhVHojxGFexSvX40meU_IkXJuA0Ia75eQmITvJ_ZebiL1aq3eqlD4-8CajirDh9omdd1sZSMm6neheXNtj6-ikA3T9beg8WC-n4C8oqpObD_osnpVbSkpBHKQUA39xywhQsfh0XGzWdO3UZ_9OEdEuGI8UYsnuhocxshtJ4oi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/726fb491ae.mp4?token=kDXJLGApS5qxf80xISqH_g6LcuFgC1e1TQVfqow6RPdxlUeuAMO0QTP0V0Ql433-JiVHEaSPaW1MFBd5UKM1nSBeZgKfJsMfUgapkpw_jQh2A6Tk08Ven5wu77JUJlf_63L0Sf9UkEv8Xe0DGG08cLkLKN2nVDukH09rQtJzpfJct3QhVHojxGFexSvX40meU_IkXJuA0Ia75eQmITvJ_ZebiL1aq3eqlD4-8CajirDh9omdd1sZSMm6neheXNtj6-ikA3T9beg8WC-n4C8oqpObD_osnpVbSkpBHKQUA39xywhQsfh0XGzWdO3UZ_9OEdEuGI8UYsnuhocxshtJ4oi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قمه زنان امام حسین رو چرا می‌برید بیمارستان؟  بگید خودش شفا بده!</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5739" target="_blank">📅 19:16 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5738">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e184bbb012.mp4?token=J-ArluWpgSRfLgOxkmM71o2L-LaBHAWHUk8UfksurYkCSzG37cS9VAU3pOq2qvjpjGpDZD0WdKhGRwBjkqzZnLU--40dIGb43Re1VN7hh1nvYm8QH9eGqujLmFdIDeGzh_toYZX13lWreba6gXfYA0JTIt6A2eAz-2fpjnjO2ve2lTgIelA7cygpb0QrkMhcv4YWwKZ2O7SDnsAuEdQ20-NeJsea3oikjSQKsxasdOeSMj96-22m0NwPFF1iTc6KRjhfPo_DihEg6Zhp5Hz6cDl6NlD_ZypdtXfkhJV_O8S2h8Z-072KGPfzOmjXgeiE_IUP1YatDDrbJJuaV-fmfg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e184bbb012.mp4?token=J-ArluWpgSRfLgOxkmM71o2L-LaBHAWHUk8UfksurYkCSzG37cS9VAU3pOq2qvjpjGpDZD0WdKhGRwBjkqzZnLU--40dIGb43Re1VN7hh1nvYm8QH9eGqujLmFdIDeGzh_toYZX13lWreba6gXfYA0JTIt6A2eAz-2fpjnjO2ve2lTgIelA7cygpb0QrkMhcv4YWwKZ2O7SDnsAuEdQ20-NeJsea3oikjSQKsxasdOeSMj96-22m0NwPFF1iTc6KRjhfPo_DihEg6Zhp5Hz6cDl6NlD_ZypdtXfkhJV_O8S2h8Z-072KGPfzOmjXgeiE_IUP1YatDDrbJJuaV-fmfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قمه زنان امام حسین رو چرا می‌برید بیمارستان؟
بگید خودش شفا بده!</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/5738" target="_blank">📅 19:09 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5737">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OGMcpItsx22SV1bJeZKdQPPOKy0W4AN6hiOWRofkg9HRNVaQfKZczt8MEEo359rsvVqzjvFrpAW8N3HG2I-nUEnYz9HnGfy7HgCAs4pKMAiATD1zem68DuhmJY2IyX6DUY6mnnDTGrKICzpGfC5AsEoMFf27QWdc8-pDoM0CrDSx6Pdys5vAnttKyLikg_MQDqU-GewG9fwNtify27I6foZ9dU7UB7YqbmbvA-MBUH8M1_XvFGu_q80HfMPKYobbkhm6VEkWPixuDCOjvogrUD5WyadC6jiCGo9Fz6l0OWlmOa_XfxRi2Sf4w4WCVTZD15tFXQ7uUtYBXLw7LIoPKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیام فارسی وزیر دفاع اسرائیل خطاب به قاآنی فرمانده سپاه قدس
آماده‌ایم کار را به پایان برسانیم.</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5737" target="_blank">📅 17:53 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5736">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">نحوه اعلام خبر کشته شدن خامنه‌ای
و عدم تعطیلی مدارس</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/farahmand_alipour/5736" target="_blank">📅 16:55 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5735">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KhyRXFE0TkDRCrgJASqqgtWc1LuACCfwZ7VbvWEovkrGZak4l-Vgto5ai_dUoftQ2KrZm31a4pAZyHXLANiQzVyoxqUzqh1l-JCT9z83ARgYqmKThlVSMbm1hJRVBVIzPhWzFZ8_Qe2QgmXBYkXPr1wpdaorEUgM-I-SCHlUGftsdA1OqSWr65WFC_8wxvEerG3U61nVXwjEjF_tpIum1V8B2pbpi7QYqJJ6ViMf3LBupiOKCXVoViUrtkrIUF0QjbyYxctW2QGHx65c-GQf_W_MCsB1cX-JQzW5Se_J7YpKZutwKQnyFc0ri5pu_kO0zL8jFplKSMiu2ncvFMJHDw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TO66bnejJVIeY_gX1yDhxBGybs1me7KWmzUCMglJpGAVY9WPg32cPYqdrCCHX5QKoQadossbn0ApU2BeL8puOjFXVSGroJ5HcRVWH9F0WsUlPGgcasxa705Kq6BYHeIJnK1LmWIQe74mlQPTPoAZCMkCqN_ddoeCdToVTGlh5TthTw6E_1h2cPRx190GhPRGVyDukBF7g4St1xGZk1TBI8lR1uJUTdp-5AtCZlkBFLHFgBydJugXzXau8fV6F-qE78yv1uF6vqNvE4B7L8cb_F1D7E2jT5F0UAYOgZnByLkDj-SoxD5DlnPFp_M_EaZ7h9vndhparhyntTseSWPk5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر علوم جمهوری اسلامی  در ترکیه،
خامنه‌ای را از اولاد حسین عنوان کرد.</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/5734" target="_blank">📅 22:29 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5733">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IknhAyebS96ui24g9cjOXgPozhHVnBL7FnJZmBpYr7Z_ShV_Ur7EUabiEGICVt7DiGcrdGdoxWbW_GylM3pJgwgUe3aLk7BkcXuxI3sE9lM3cuH-rlbEkYENco1ej4J0q1g8TWicz2RrrBqm319ydcyw209G3nSxoQrWim4DmhaJzii295HKQy-yP999D5HnIuXi7H9oYJsCyvEzLumLMwYo5zCZ30UYiD_DqtVwpKBvjHthcwTNS7jxa9gXV5EOn_SQOoOpnB6BDQPhRf8V7yFUxJQAS2J_d_36rOTePs4KjzcSVelJqVLGnstM4pHYrQSJs4_zzUmF7nsbkgL8Vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسرائیل به یک خودرو در نبطیه در جنوب لبنان حمله کرد و در نتیجه ۳ تن کشته شدند. مشخص نیست سرنشینان خودرو چه افرادی بودند.
صبح امروز هم در جنوب لبنان یک سرباز اسرائیلی در جریان حملات
حزب الله کشته شد.</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/5733" target="_blank">📅 18:23 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5732">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rsok4IApyHrj71ejqXkviuFVAuy4DE1OSqKXzdbPasB6LxZ_VV7i_V_ISvdW5V1ilWAzwKh1NBZnk4x-tgr4R6L6tBd22sXudf6Ah3xSdj8KyrzMbw-8dpkaFNjPVsFM5a238oG68-CCrl6S2U7muXdyuvRZ_rOTG59jB-olzCDy5xNhv5HMnYXyKsJxd-eoBXV21XtnsOiBK4StnrrLrlAtq3-iX0sFSEkPBmDKjC4YUkQsbOXR8VSXy159g4_ZuvqZup5WeXXfSiiJ-uBUGiPCjv4M6PgbNR3FV_38DmBWNKdJ2k0ASkNnVNQDuxa80BffDWRJcVj9HUVizo3_lA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صد رحمت به اهل کوفه!
لااقل به دینارهای طلا فروختند!</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/5732" target="_blank">📅 15:21 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5731">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIran International ایران اینترنشنال</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6715f87786.mp4?token=qYrMsAry78ZqDKh4jlSCGAtMwdW2vG3gauvJSIwy5y6oNMearLfBTDk-E8Httkrew3p0OpjMv_LHXioSQd5kfx5u6VxtdsACrbBm76IP_IIDcNzyNj7r-OvuDu92YX1de9qIi1_2Dm_Urc9yN1-bxSY4nuNlZ1luMoRryRgnqAcMLrqRL3KDKrOiRb5OrCr_lWVObIdC3U-ohiRPIevJrynNUcMqvMb5_YV-lxD86D_vmfYdKfSCIG-um-3nZXkOrU9hC11eCDsBakaNsOJ5lnRxFswK4rx3_CxwHg4p_HWX8fIVPBafuFHThjxpM96zwlXEM4fxBsCbuvH3aekVcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6715f87786.mp4?token=qYrMsAry78ZqDKh4jlSCGAtMwdW2vG3gauvJSIwy5y6oNMearLfBTDk-E8Httkrew3p0OpjMv_LHXioSQd5kfx5u6VxtdsACrbBm76IP_IIDcNzyNj7r-OvuDu92YX1de9qIi1_2Dm_Urc9yN1-bxSY4nuNlZ1luMoRryRgnqAcMLrqRL3KDKrOiRb5OrCr_lWVObIdC3U-ohiRPIevJrynNUcMqvMb5_YV-lxD86D_vmfYdKfSCIG-um-3nZXkOrU9hC11eCDsBakaNsOJ5lnRxFswK4rx3_CxwHg4p_HWX8fIVPBafuFHThjxpM96zwlXEM4fxBsCbuvH3aekVcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیوی ارسالی به ایران اینترنشنال نشان می‌دهد که صبح چهارم تیرماه در همایونشهر اصفهان پرچمی با نام‌ها و چهره‌های جاویدنامان انقلاب ملی ایرانیان برافراشته شد. بر اساس روایت رسیده، این اقدام «بدون ترس و با قدرت» در جریان مراسم مذهبی «عاشورا» انجام گرفت.</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5731" target="_blank">📅 15:20 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5730">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/afaf9624af.mp4?token=CDHk1_4NJNM30BXQGwWCWmI9W7ym1Gsek5Roez35ftY_IXwkKl7RwXmihK0eUJuA8lRQQxk5EpBk5095Ub_Y8iYIGRoUyuqyiEqEr1sJM8yNzpcwIiwwVGzV9w8yOimogmrNnlrXkQ4yTVzhxUkUyo5r82-8pr1rHUOnBiZstuU8TYnSwIJnaM5Qjv39CzbZPvBGSHOBEgY0FmV0PqCc2CVZISbJUcbiJjCBP-yGibQa6hZqgtO7HDfbDoyotYdYj935GnsqbZhLNTs6tV0In-qezmMaEWy-s_wF4yWWpqT5xHDG66wZg4wHWNne-6JJqksjvxuTK7C4seXjnm4wSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/afaf9624af.mp4?token=CDHk1_4NJNM30BXQGwWCWmI9W7ym1Gsek5Roez35ftY_IXwkKl7RwXmihK0eUJuA8lRQQxk5EpBk5095Ub_Y8iYIGRoUyuqyiEqEr1sJM8yNzpcwIiwwVGzV9w8yOimogmrNnlrXkQ4yTVzhxUkUyo5r82-8pr1rHUOnBiZstuU8TYnSwIJnaM5Qjv39CzbZPvBGSHOBEgY0FmV0PqCc2CVZISbJUcbiJjCBP-yGibQa6hZqgtO7HDfbDoyotYdYj935GnsqbZhLNTs6tV0In-qezmMaEWy-s_wF4yWWpqT5xHDG66wZg4wHWNne-6JJqksjvxuTK7C4seXjnm4wSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گوشه‌ای از جنایت‌های دیماه جمهوری اسلامی</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5730" target="_blank">📅 12:24 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5729">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">اینفلونسرهای عقب‌‌افتاده‌شون‌ میگردن توی دنیا تا سطل آشغال کشورهای دیگه رو نشون بدن  و بگن ببینید اینجا هم آشغال وجود داره! پس اگه کشور ما رو کلا آشغال گرفته و به زباله‌‌ دانی تبدیل شده، عالیه! عادیه! معمولیه!   مثل همین حمید معصومی نژاد  که دیروز براش نوشتم،…</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5729" target="_blank">📅 12:00 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5728">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pcW7SZzLz2CaH1YWTP1gQ9KEuqqBgcAZ7ItMwnaveLGEAWcnmDFXokprJTRHkzBjGRKEE5UIX3P_z-BMLf7RfQFvfUvhrZ4EGG5SEPxi1SVZYkaakEjvqZX-WWLnohyOFZ4PJI6C7qaE4BZ9faTde2bDApU9hNlhno4E1bAUTqrzVd4UP2xLg1Xp1sK_TbK3KpajHv2XWhmgc6M-uIktpWOrHSgQSVVZPVH-ycH6UmdXqmVqa14Js4XNEq9-96pKrJhjB5H-Um_aOtBs8EGhwJOrKLRXwtN8ViOBY5cFonbibtTeAkY5FkfUB1AICGCGyG-iNv8RaMbH1pfreckvwg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🚨
یک سرباز اسرائیلی در جنوب لبنان کشته شد.</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5727" target="_blank">📅 10:30 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5726">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rR8pr30zW5l7fehFQayuyC_FQuY-kg0gs6lT6pdvoVkYErUEpNyfUjJHxbNN0yXQA5i9-y6VrUxI86NR56E6l0i-s4VhoDscbsDy1Y1Azys-1uJym0C1cj2mwqtdOwdeQC8Tix3zNGsREcsux4zIJ-XLkE2y9z0xcNesYw1aqsKx51hE4g1G-ZUMyomOk73hKfHBHfcKL4A_lWY0EnAK1m9-s18uA78VPw33ddvaIRyHYjuLsNnwbcju-M-n8odAGChC0pctz-MQX8Ld4Bz3BQF6iTvEebw4NVDzoprvTB3t5Hfq4UqmZGwyy8f8fy34WomPRX4QSidQA8CgzJnihA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرمانده گروه هکری «حنظله» که در جنگ ۴۰ روزه کشته شد، ولی خبرش الان منتشر شده.</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/5726" target="_blank">📅 09:39 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5725">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/86c17f6d3c.mp4?token=DTsxCwC4XgtF-Xj9KZI0lGsv93z-myLncHR15rjk7beXy-QQ-zM8mFP0ldSAhCIFCs6d36aPWs2XHjyE_p-4-js7kNkT_lZn-FEJrlGyaZ-kG_DPBDI71npxdxpx5wJR5bFtmCF7TWtQWwflGNn0iA2f4Wgt10th7MfUJ-agd8CwHGQGvz5HEXxWIBxDxMHXUmbnK1GK27QGL4bao-7_G1YBITmlSfcpp519lVctZA_HeYCLivpe6Gj0IXnDWHn8f-tG5Ly7vkuqpovMqwkopyYskX-i77fAlDcEMRUEXOjBVcKcpSP-uR-IieVG3qK0RSUzF8Sm8VqzZ-KlleSglg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/86c17f6d3c.mp4?token=DTsxCwC4XgtF-Xj9KZI0lGsv93z-myLncHR15rjk7beXy-QQ-zM8mFP0ldSAhCIFCs6d36aPWs2XHjyE_p-4-js7kNkT_lZn-FEJrlGyaZ-kG_DPBDI71npxdxpx5wJR5bFtmCF7TWtQWwflGNn0iA2f4Wgt10th7MfUJ-agd8CwHGQGvz5HEXxWIBxDxMHXUmbnK1GK27QGL4bao-7_G1YBITmlSfcpp519lVctZA_HeYCLivpe6Gj0IXnDWHn8f-tG5Ly7vkuqpovMqwkopyYskX-i77fAlDcEMRUEXOjBVcKcpSP-uR-IieVG3qK0RSUzF8Sm8VqzZ-KlleSglg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ میگه جمهوری اسلامی خیلی رفتار خوبی داره با هر چیزی که من میخواستم موافقت کردن!
باید هم موافقت کنن و گرنه دوباره
برمیگردیم سراغشون!</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/5725" target="_blank">📅 22:56 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5724">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">وحید اشتری، فعال رسانه‌ای حکومتی :
تنگه هرمز شبیه یک بومرنگ برگشت به صورت خود ما، در ۴۰ روز گذشته حتی یک بشکه نفت نفروختیم. از لحاظ نظامی توان شکست این محاصره را نداشتیم.
گقتم تنگه هرمز میشه تنگه احد براتون!
به هوای غنیمت گرفتید، ولی فهمیدید باید دو دستی خودتون پس بدید!</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/farahmand_alipour/5724" target="_blank">📅 22:23 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5723">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/171eba79df.mp4?token=ErygqJEGYHeYSvSSnqqd2HyzvPg3IrGXKUbOMGnBAWpt8BuL0huYVdxekpMxUBIi3XRlA5rQV-4B8C60yZtL1d40LyFhSRaccv-0yCKKLQI_b_t73fSkcfya-7nYJCCA__Adxf_80-H5rWqcY7Md9bmqEvRSOdrXRICnzZWU9PhIDlTAevnae4Jr48RJOOTZ62AvbHmHguYeHQtq22s4BCvTnu_p5Xdf1G3p8XqFgXHhDTJsYdH1C0sY6r6BgT-pZHf7v_XH4j2C5gHp0IHhkbV1BcEtctej7K2IDyhYD3H-1iZJWIyizNfdfzPm6rZrXDcWJADaYZ8w6iEc63XHIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/171eba79df.mp4?token=ErygqJEGYHeYSvSSnqqd2HyzvPg3IrGXKUbOMGnBAWpt8BuL0huYVdxekpMxUBIi3XRlA5rQV-4B8C60yZtL1d40LyFhSRaccv-0yCKKLQI_b_t73fSkcfya-7nYJCCA__Adxf_80-H5rWqcY7Md9bmqEvRSOdrXRICnzZWU9PhIDlTAevnae4Jr48RJOOTZ62AvbHmHguYeHQtq22s4BCvTnu_p5Xdf1G3p8XqFgXHhDTJsYdH1C0sY6r6BgT-pZHf7v_XH4j2C5gHp0IHhkbV1BcEtctej7K2IDyhYD3H-1iZJWIyizNfdfzPm6rZrXDcWJADaYZ8w6iEc63XHIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قمه زنی گروه بزرگی از شیعیان در کربلا</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/5723" target="_blank">📅 21:46 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5721">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dzL6Lt3UyuZYb25daF_N-EV2KaBxFU_x1eELq5o6YOjyEerc3yoQ3Uu2232Jgh7ET6TnbCRF6hkw99PkEF6ZHLdypFYYUIiAi2eZnFgf9otwOsmrr79PMPjMfbiDIv0GcttV0fxujaavz91sZNJnkfWQQIQTtOLYlr2xE8J5Civmz1zOxoQKRWBWfzFTKH2pLfBiyxsWwhQh7W2v0Mij7sJcpAV9-mxEQIl-zFh5N22WhtRA2fieQdrzyBgNbg8nAo78Qul4ZODji4zhM1M8xO0XWM-er2z4KGViQbLFyLVFshbrLGePLd7YvpnLqmSf8tLjSjtd_PzWC89PYiKr3Q.jpg" alt="photo" loading="lazy"/></div>
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

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
