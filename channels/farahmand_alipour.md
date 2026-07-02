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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-11 18:05:51</div>
<hr>

<div class="tg-post" id="msg-5835">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iJRkbhs9IbWoRZovuIbAdCL8RXSrfv_LsUrHECXlOyAb2uyCnEEv9ImGnUkRyGmvAC06Z2YVpGx7izQ-p_b2WD9xm-bTyR5IzbJa30aWfPj3lmO4UruESejP3oMsOJpBG7NLchPSl77nDA5NmHdAG5jEjqbm4o8iZQyOB8lfip-ciniSz7YpCk9ZbLMGfjSmj_rW69BB-5xaFhnYeIyVHfGFt8KxkjcULSzASE3rL-HTEk3EI1vda8CAZRClwHoNtnY5UOogMYIUFLiFLHvjQw7AKDT1iD_I28FYmfPpNWm07UmLfMN-GmjQr4YYQyUOtDqs0B-TrusDlkbR-DeOtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/farahmandalipur/status/2072405978012844407?s=46</div>
<div class="tg-footer">👁️ 7.18K · <a href="https://t.me/farahmand_alipour/5835" target="_blank">📅 14:35 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5834">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YYpS2AGyOFJVNJHDIntWcTTBzu3PdjdY18dppzEwL1jCxfGZv6syisx77E5hiMHQEPYnJtUTSN9gZXYvTd177TsveVJqvA0LGWivRTQChf1q5mzc4OG542pY63Y5_CSOZgNYufdzZz-B3Yd_U8TlsXDG9NEsdRvjAQnl97Cgtu2iWJI-GYu-Fbcn96_Ol_EWdmmJwESqGPryWonkVcZphsPFW_ju0RB1ZI5L3FWhEzAHL0zhw5psoQPDc1xzjYkbeyqPUNtH2cw3TGnubrI2qyZJVsAmo5TIr4H1iisaf-1ECwLlTi1o6uFduvMAV5l3KqysaEt2kONB3pF3l_-EKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چرا صفویه به این کتاب «روضه الشهدا» اینقدر بها داد؟؟  ایران کشوری است که عمدتا در جغرافیای گرم و خشک واقع شده،  قحطی‌ها بسیار زیاد بود، فقر گسترده بود، جنگ و ناامنی بسیار! صفویه با گسترش شدید مناسک‌هایی مثل سوگواری  برای محرم و قمه‌زنی و گریه‌های شدید و…..…</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farahmand_alipour/5834" target="_blank">📅 10:48 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5833">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B-6p8jGj_erqIzymuNNH7CqkXx7WFj5Q67dTmM0GBCBTeKO2JR06nEfkRn9O--Fj-ljU-O-lSSsZBWprk3mezHBDePIVi6ZjUF3FZURIId_wEl9OlAYkOpwlELJFhxj4DgcLBTxFZrFoOlFTdV4VSGqmuYJ0tj1Wx54wQ-ALKBxgXghOtmRcN-gvflFwaXBQRoihdZHMEZEEmZVsOiI8TqnmgyXs_L89XSsfht6uupp8xnV-1Iw5xVqdMeBTBmYb6za4XWJr5VUiSDnX9nfo4nHs82iiRl17m8SqKxXsUqbeAqTY3PETy5hS2adcg-GXXnROgf4GmPAdS_AWJqIHtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خود خامنه‌ای هم در اسفند ۸۴  یک سخنرانی در جمع روحانیون در آستانه محرم داشته و گفته که باید روی  «گریه» و «احساسات» و «عواطف» کار کرد!  و امر میکنه به «گریاندن»!  چون روی همین احساساته که به قول خامنه‌ای فضایی ایجاد میشه که بتوان خیلی از سیاست‌ها رو پیش برد!…</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farahmand_alipour/5833" target="_blank">📅 10:42 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5831">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VZKiyY-aTp0qDEKrp6Yrrqa54CWEEkg5V7dIZrjj1SRcHW-wGLJ9xc9Nz3dP3nVQw9r3RH68-cRAaIg-ffBOPlUwaftTKPrTf0r3o5KurJrpTOCc4LOBslM5TKEz7XbKDZJv1FeI4oaTTf5JfLNDGtQ-XjMI5g7VmBjOsI37QepOpewMYYgfwIz6HdwIasc8nyqHBHrypuSS7IbalJdUWBwmI2Dd18MMGr5Vvb1q6k_SsGw5-wGuEXJT0OA131dZ1haGl7dyMrFf-eh37JwXLCOEE-ddBazRIvzf99d0X0D3ims1q_VAJDVh7SMPfrmr5xJmXe9DDHHhaivLJNYdIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KJyICSScG8w5gh4zHFUwgeBMPU78Ocf3sPu_Oy7a8kmg8xJq_CVlElx0QDixCzfbNFcCHHRKMJeWxK7-Ptinzu0Z2PRp4NxiOhZj_BSQT3nrRxm3BmiD2Vj8liPfNH8SrTExP_t-muWmu05ULgg2aoXohpu69PLaN7x0A6Katy8_aaiEEVtoMMksasWxOp42smVKf23pScPC9Nj_jUr8veXI3ed010P1PZcn-4oahzw_A6PVdXi3bhiKbx-vvqpWhrQer58M_uV21OI99eedtM3x_Qwz-6mVoF3hSep2OWpM31ovvP33L3NPhPcNTgvZj83-vsb62VPnGxtpWbCgiA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">نکته دیگه اینکه خود صفویان،  از فرقه صوفیان خانقاه اردبیل بودن که در این فرقه یک «مرشد» داشتند که قزلباش‌ها، باید با «شور و احساسات بالا»  نسبت به مرشد حرف شنوی داشته باشن و اطاعت و‌ پیروی می‌کردن!   این کتاب «روضه الشهدا» برای صفویه خیلی خوب بود، چون شور…</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farahmand_alipour/5831" target="_blank">📅 10:38 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5830">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EtohJesNZbSJmgFGg6BfdC2n4_8K8nNkEX_hgtwNsihYrqRbio9pkVAiC5zX-fNZJB6hC2vrooeuXqAFd9L8M8qt3mimgp-llY3SKQ_gUNOySYYAFEIcAyIqRp5zOkurtHiCnzLrq7erwAb41Kd_v-kyLSXTalerTCZ8lTyNEYuIkYTt6Nv_LOKZu8S_PV8KD6WUspY3yTLdP0gMx48LVXAGs1R-yRX3hnlN4Ey1Pi17aGlfGpCV8DHAW1fhGVXWvL4yhm_s-q9Bo022yCFvmJQAUvNNUw7yB-5rdVxHucLu5WcSQ6HW2XUlQGr0YHsT-CU8DZ4Jqws2Mkggb_pSvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چرا صفویه به این کتاب «روضه الشهدا» اینقدر بها داد؟؟  ایران کشوری است که عمدتا در جغرافیای گرم و خشک واقع شده،  قحطی‌ها بسیار زیاد بود، فقر گسترده بود، جنگ و ناامنی بسیار! صفویه با گسترش شدید مناسک‌هایی مثل سوگواری  برای محرم و قمه‌زنی و گریه‌های شدید و…..…</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farahmand_alipour/5830" target="_blank">📅 10:17 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5829">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CNTYxJ77ojeY7zQleopB_UcHLTvcFvN1qfGY2PASFcLVRp3SWs8BdFg4uEIH4F0s0x62vRuQq-TP68L1HvP15RPtIE07aWBI0w2gVXUiZG6CZCorqqIYkviaXKLkaQPU1cjKwL6ipRgexiYl5u2RmKLIRKePqAJN1s0Lc6G9mFzqCw_TE6yMFmqshVj0oub7iVMUGYt7hvFvoYazDI8t89eCdzc1k2hTzp6qy4U257xUNnqofz5pmmmLGUw8YGc_ZkMbSwg2TTMv31ctymPn_HAniifMH-keA-WqYf6Lpm_7Sdwzvs11bnDKjP9YVvczXNVLhH1M_dx7FF9xpsbOGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای با الگو گرفتن از صفویه و با پول نفت.  این خرافات رو تشدید هم کرد!  به «مداحی» و «مداحان» پر و بال داد!  بودجه‌های سنگین! تبلیغات گسترده از طریق رسانه‌ها از جمله صدا و سیما،  که این‌ مداحان با خوندن همین دروغ‌ها! احساسات رو به نفع حکومت مصادره کنن!…</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farahmand_alipour/5829" target="_blank">📅 10:06 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5828">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QfvVUcn0nncvG0HoZzOuLrTxwkAP-ZoM3mdCktSzHWlwyiI00K6qwEpvDhrq6E-ejROreuxedUXZYNl-3Q_7-ChSUyb9rRsdxmgtV2hr9bEnPjw1kCdYufWBKc14DerjipadA1PgSzwAf3AQBhQoq_0EOCBAkCaIQ74LEmKFaMSiW9KapYXbGx6RI5vqSML1eEgBnTr5SB5Wnc8YYqed4PU9CSev6SCLyu0ztjxOW6aX9ouXRisxhx3YLZxkcZ1QnFNiDV6DcihXbCWrkc3SIcjUModRWVoTEqMqUQ8rgt7eNFv4AzjqW9GFcoXMUGT_uEF4jaWJTbVddu7AP1x_Ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مرتضی مطهری در یک سخنرانی عمومی  کل این کتاب و داستان‌هاش رو «دروغ»  و افسانه خوند!  گفته از خودش نوشته شده!  کتابی که داستان‌هاش صدها ساله در ایران خونده میشه و براش گریه میکنن!!  کتابی که حکومت خرافه‌پرور صفوی عامدانه ترویجش کرد بین ایرانیان!  مرتضی مطهری…</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farahmand_alipour/5828" target="_blank">📅 09:56 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5827">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">در زمان صفویه کتابی منتشر شد  به نام «روضه الشهدا»  توسط «حسین واعظ کاشفی»  این کتاب عملا مبدا روضه خوانی  و ذکر مصیبت در ایران شد.  و اصطلاح «روضه» ، که امروزه برای ذکر مصیبت و گریه به کار میره (در حالی که اصل معنای واژه، به معنای بهشته)  برگرفته از همین…</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farahmand_alipour/5827" target="_blank">📅 09:41 · 11 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farahmand_alipour/5826" target="_blank">📅 09:33 · 11 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/farahmand_alipour/5825" target="_blank">📅 09:09 · 11 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farahmand_alipour/5824" target="_blank">📅 08:27 · 11 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/farahmand_alipour/5823" target="_blank">📅 22:52 · 10 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/farahmand_alipour/5822" target="_blank">📅 21:52 · 10 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/farahmand_alipour/5821" target="_blank">📅 21:52 · 10 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/farahmand_alipour/5820" target="_blank">📅 21:50 · 10 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/farahmand_alipour/5819" target="_blank">📅 20:05 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5818">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cYyU5LTG5HhxNA_ZifLqyxziFlTnQi_e4aPmG0ThCypRHEMYyVSnzz3hv5PwD1Nfmb9c85lAdEWx8NFt_WkY3dFx2X6YENOxIptVozFR0ul7PdsCjnc_mG6J3GgoyjaFPTPJSN5Z0aR2WPGJlXhbjgLglG6Zh0kRd9azVh6X76D4sqRGZcYsPMN2LLk2Osbk4MAj65E8a9XS6QqJadkS_lrv2NSksaKr3UvKtvlfkfFx825Ka1E43_0c8PPJ5nVMsFgPfTswCDcl2TNbq_FT36jFe0s_VJeM8y2JKSRp-CQlPrVkv0qcseqxscajZbuG9GYDR0VacUIfkM1ftQ8gUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/5818" target="_blank">📅 17:21 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5817">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7862dff401.mp4?token=oN9cTWOCCUTUV_vR55qG8y-JPBCPvM-LVa-7wg_DsNxOPpdSW7TeBgQiIZbTfHP_gb9-6FBdKcOqd1QclvTBsiACxoLww1r_50dmzXIW1wwMOyrNbVd7t8cnYoKNmwTYeuiWjaD52j6WA7dx8XfO5DOaLoGB0cotUgAGiDxLbv5anaJ_0j8nIJ75A8vmqo2-FPjFvgJp8WQZ59pNaVM17whSRfPeMFtO0Ljm6mw-TyjNtyefVn3BNewLfl5yD9_aYBgnRwKKTq8Wf8fwRv4gvCP9J4ocHJaY5m7q38WK0k3YLN2tY39vxDKneXhKEh31O_Kitx4P_1Pmckpq5PGHsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7862dff401.mp4?token=oN9cTWOCCUTUV_vR55qG8y-JPBCPvM-LVa-7wg_DsNxOPpdSW7TeBgQiIZbTfHP_gb9-6FBdKcOqd1QclvTBsiACxoLww1r_50dmzXIW1wwMOyrNbVd7t8cnYoKNmwTYeuiWjaD52j6WA7dx8XfO5DOaLoGB0cotUgAGiDxLbv5anaJ_0j8nIJ75A8vmqo2-FPjFvgJp8WQZ59pNaVM17whSRfPeMFtO0Ljm6mw-TyjNtyefVn3BNewLfl5yD9_aYBgnRwKKTq8Wf8fwRv4gvCP9J4ocHJaY5m7q38WK0k3YLN2tY39vxDKneXhKEh31O_Kitx4P_1Pmckpq5PGHsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جی‌دی‌ونس میگه ترامپ میخواد با این تفاهم‌نامه با جمهوری اسلامی،  بازارها و مخازن رو از نفت پر کنه،  و بازار سهام و اقتصاد رو درست کنه بعد تصمیم بگیره با ج‌ا چه کنه.</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/5817" target="_blank">📅 16:36 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5816">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f9a10fc62.mp4?token=OjrUuGc0XQW9wm9oganr5rJJfwrSCXeNGvi2qJjGEaAHc6B_rKEJptnq103N1e0I-Gr7ZrkLmBFLBCGP8o3a0747uTXE-UXzLHdNc1izSKtdICuCD8Y5W98N0rzfhaQvxMJWJKra-GXflIaGyAP3FJGOU3fafhBIZF-jsbiVRZQyDYqAiJ21AfeWnsZtUPc5-iSQKcZTmP313Fqec_q06Y4T9LL5yLpBiFYfYWAL3KW2ArPxOdngF7ZumdN_OZ0EHNerMwepLszQJDCAcSazM4p33yt66IpizuIDgCfIL05x82N_bjrtqNCtX8-X5golWcn_E9ObGW7FBPA3_8sMDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f9a10fc62.mp4?token=OjrUuGc0XQW9wm9oganr5rJJfwrSCXeNGvi2qJjGEaAHc6B_rKEJptnq103N1e0I-Gr7ZrkLmBFLBCGP8o3a0747uTXE-UXzLHdNc1izSKtdICuCD8Y5W98N0rzfhaQvxMJWJKra-GXflIaGyAP3FJGOU3fafhBIZF-jsbiVRZQyDYqAiJ21AfeWnsZtUPc5-iSQKcZTmP313Fqec_q06Y4T9LL5yLpBiFYfYWAL3KW2ArPxOdngF7ZumdN_OZ0EHNerMwepLszQJDCAcSazM4p33yt66IpizuIDgCfIL05x82N_bjrtqNCtX8-X5golWcn_E9ObGW7FBPA3_8sMDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جی‌دی‌ونس میگه ترامپ میخواد با این تفاهم‌نامه با جمهوری اسلامی،
بازارها و مخازن رو از نفت پر کنه،
و بازار سهام و اقتصاد رو درست کنه
بعد تصمیم بگیره با ج‌ا چه کنه.</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/5816" target="_blank">📅 16:31 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5815">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🚨
نتانیاهو : اگه نیاز باشه به تنهایی و برای سومین بار به جمهوری اسلامی حمله خواهیم کرد.</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/5815" target="_blank">📅 00:04 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5814">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/60c1fdbeee.mp4?token=ToSqXEMLP_7hil2C0m3krBdTBEFrYDti_XsnBIq_KyejsyUj87VyvNjjjbF-URprSCTsAOnZaRC2ubOwNTvTGutNRATyETcZoOetIPfwu8aCOZ5vPsOfs8hDIs3L0pxsMv5K-UyzNpssIRZYvr3AxWx1P2eXFSiaXJ2PWofS1g5CSBbwdif3cq2jGlMZFR3pn1qbboFGOUTBpSYBAUwJkaGByj6czX8l--Er144NsdoKqrE_Y5sLbTkteDxIWMPs7AHyYLAa_oFm3dF1yO7wUldt4rL1bzZKJv0cMu1E10mR45vhWrn-aZu_Ghn1dxSPiKgCpSjCsooAa6lpLFkcqTP6f5V9m-_ZZAFGe1qV0HhLGZ0tmFF0VV6qJeDvR8Zxl0oVUMFu4pe9Nar3c11g5buCLvEoigMz8fyzXiCraVdF-0FS7dhGXIlFGyn29PkbRDnzKRipl67LQbfjqyt-_iiItSiWLwNHJZjGX0wci5CLvt7cI_LH1ElLnhfzC_csnuAvKvRYwvpJjOBaB4aAEWiakfaHpk9o9vLcWg0FDlWMSjtZGQw7vPfbh0nN286iCjGdMNq4yEaYCPoTW8gfZBZISMUkFko8lGDdNWsPIcuvxaLi62mUBCJXk7jJlhaeW9rCYo0i5jkjRJ6_O5M_0RUkDrGYcXz-enutyW1TCa0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/60c1fdbeee.mp4?token=ToSqXEMLP_7hil2C0m3krBdTBEFrYDti_XsnBIq_KyejsyUj87VyvNjjjbF-URprSCTsAOnZaRC2ubOwNTvTGutNRATyETcZoOetIPfwu8aCOZ5vPsOfs8hDIs3L0pxsMv5K-UyzNpssIRZYvr3AxWx1P2eXFSiaXJ2PWofS1g5CSBbwdif3cq2jGlMZFR3pn1qbboFGOUTBpSYBAUwJkaGByj6czX8l--Er144NsdoKqrE_Y5sLbTkteDxIWMPs7AHyYLAa_oFm3dF1yO7wUldt4rL1bzZKJv0cMu1E10mR45vhWrn-aZu_Ghn1dxSPiKgCpSjCsooAa6lpLFkcqTP6f5V9m-_ZZAFGe1qV0HhLGZ0tmFF0VV6qJeDvR8Zxl0oVUMFu4pe9Nar3c11g5buCLvEoigMz8fyzXiCraVdF-0FS7dhGXIlFGyn29PkbRDnzKRipl67LQbfjqyt-_iiItSiWLwNHJZjGX0wci5CLvt7cI_LH1ElLnhfzC_csnuAvKvRYwvpJjOBaB4aAEWiakfaHpk9o9vLcWg0FDlWMSjtZGQw7vPfbh0nN286iCjGdMNq4yEaYCPoTW8gfZBZISMUkFko8lGDdNWsPIcuvxaLi62mUBCJXk7jJlhaeW9rCYo0i5jkjRJ6_O5M_0RUkDrGYcXz-enutyW1TCa0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/6a28a5f6ff.mp4?token=NDisNAIJryU9EjIaSgvp2HBq-GLAJYiMa9B7MoGlWle5rXuMQuzKs5BUPqligYwGm_A8uFkz4OSAcDQYcC1oCnwC63G6UnOL_g4N_MsxFPbVK6DTWnQaKwES1jq1l41BSAkTs6mNTkArO9mUiOZz-q8HuD84kA2t5KQ2wRHvUXv3QULth39079O7dNmTON9QlgMssdFCsBTrvYRA3zy35Ixj6LJAaxz2WtEnsGznQ2MJz5j7yYcHMORkmjN3SQ0sm5f8sjgs0bOFj68lxAPqUtk3cpHIX5YEcNwdmB0TQOyyBej-mjPXSm69TW3C9Ho92j-FKZHxMC8LNl11d7-DiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a28a5f6ff.mp4?token=NDisNAIJryU9EjIaSgvp2HBq-GLAJYiMa9B7MoGlWle5rXuMQuzKs5BUPqligYwGm_A8uFkz4OSAcDQYcC1oCnwC63G6UnOL_g4N_MsxFPbVK6DTWnQaKwES1jq1l41BSAkTs6mNTkArO9mUiOZz-q8HuD84kA2t5KQ2wRHvUXv3QULth39079O7dNmTON9QlgMssdFCsBTrvYRA3zy35Ixj6LJAaxz2WtEnsGznQ2MJz5j7yYcHMORkmjN3SQ0sm5f8sjgs0bOFj68lxAPqUtk3cpHIX5YEcNwdmB0TQOyyBej-mjPXSm69TW3C9Ho92j-FKZHxMC8LNl11d7-DiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5813" target="_blank">📅 17:53 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5812">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/085c31b1b8.mp4?token=SdfuCadWanZoxlg9Oze70KmYmlxe9MhoYo6PXOfnGzs4vhm-LEzkLGnf6JkyAiWRJfHcrMe8TNsC_Of81DjI5DZxeh2Xhd9RJaPdUgSg88AMf8KO04JiVgJPDufxKWw2GF56ZlXTR4avuNvC4nZ0E8GnSZ7b2K5eAu-mGdEuaNMOxuRDRHNmctPiYqGli67zHwV_GPXQNsnthqfgC0YwCuU1yHthXJK9ypGRzau88AP2B5VRvxqz--jOpS5x3Rwdvp6XO5W7FdBRo-u7tv4o-r3W1udlEHoSRLksohT8J1ryEdXIRnux3sEzJzGD-zaEqMZ3-qTFgpPcWeGP2WkzCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/085c31b1b8.mp4?token=SdfuCadWanZoxlg9Oze70KmYmlxe9MhoYo6PXOfnGzs4vhm-LEzkLGnf6JkyAiWRJfHcrMe8TNsC_Of81DjI5DZxeh2Xhd9RJaPdUgSg88AMf8KO04JiVgJPDufxKWw2GF56ZlXTR4avuNvC4nZ0E8GnSZ7b2K5eAu-mGdEuaNMOxuRDRHNmctPiYqGli67zHwV_GPXQNsnthqfgC0YwCuU1yHthXJK9ypGRzau88AP2B5VRvxqz--jOpS5x3Rwdvp6XO5W7FdBRo-u7tv4o-r3W1udlEHoSRLksohT8J1ryEdXIRnux3sEzJzGD-zaEqMZ3-qTFgpPcWeGP2WkzCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محمد اکبرزاده،
‏ معاون سیاسی نیروی دریایی سپاه،
‏شب گذشته در یک سانحه رانندگی ساعاتی پیش کشته شد.
او در یکی از اجتماعات حکومتی به صراحت گفته بود حملات آمریکا «واکنش» بودند! یعنی ما حمله کردیم و آمریکا پاسخ داده.
جنگ‌هاشون در لبنان و فلسطین هم همینه! حمله می‌کنن، وقتی جوابشون رو میدن میگن ما در حال دفاع هستیم!
۴۷ سال گنده گویی کردند و سرمایه گذاری روی تروریست‌ها و وعده جنگ و… تا بهشون حمله کردن، گفتن ما مظلومینم و داشتیم ماست‌مون رو می‌خوردیم که مورد حمله قرار گرفتیم!</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5812" target="_blank">📅 14:57 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5810">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HQB-dUh0lSv_l_IPAaMgUsHtNCjSzVaWeADJGRs3giy8KO7yFAJqqR_AlO2CBkK_FGH9_wICIo9zg9j_1JKnEAuUaizeJUnMGRSEWeohw5xWoZ_sim7XjWFhNL4TLZo0C4f9C7GCXQBMfdc3rRUEPqG8oSKqm2Px0GxG4DeA94aj14kIAeOm4O3oxGTffZtEXDpajcdqKkuUqorK7PU1uQEW4Ql3IiZGeyY79En3MALnepbJI-X3vvyp2ZVyot5M0eD1fuGrXYD-DHQdaGm2UZsaIJI6aNZ81prHxyJDmBjo0WjMspUl_lcq4uqH9n_tNEcWCvBSI4taJGUrAldm6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sGmYZx9QAxt5BWYZxvlrxp7boiFq4ZEWfVyTruVMLluHzp9MBX3IchtpG1Z4erbQ3lyQ4qfScITGmpPHMMzH34rT9LKCZK0bGtaUYwbdzFwWidIDq85h7hagM7EtRzYydXr3eicly0X9KLrPQeNTRPmgroBkyj32C68skbpaLWjYfjufcV2IT7ilHCN_z--cW0rBKygcTX14CkcKLKJDfs8ol1UBsILFOENeFBQGk-WAAfn0A7w_387C9MnBCEqE4EPFOgBEhKzhmRyagGhKU4l2VQycX7aNBpmCrdHrCTNejiJXC12Dt7lHjm5vyq2fsNR7m4Xy0YRs0dD0D91paA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ده‌ها تن‌ از‌ سران و مقامات عراقی بازداشت شدند. از خونه‌هاشون میلیاردها دلار پول نفت و طلا  پیدا شده!
خیلی هاشون از نزدیکان جمهوری اسلامی هستن.
با تصویر خامنه‌ای و سلیمانی و سیستانی در خونه‌هاشون و سوتین و شرت طلا!</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/5810" target="_blank">📅 13:32 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5809">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee0be552a1.mp4?token=nwurp0bEbz8M2u9UM2ZGpeUYS0VlIZPtBUovEVP5B3TtUeL8sk1j3QKVaNvWntsTaj4u6UEPEwEgKJPxU0vl65p0wX66N9DG6dE77JWdQqPPWvyXd_zPC1V9hUVTtu9YnMBewxAnhbOoo5AqocZlLXyi-GN3xKe0L98kdgSp1cn2oUg0ZN1ECGQEbpizLxrk5dYo4KBq52RIxWcyH-pWwkud_N81fh0TahbjIQKOvGjp7dBtUIewBn689ewisFeAnZtEvjD6O9EpBv3Ic2ccaOSkXPqNyqEfDadqWvp7l7uNrhCVq_2RHdjwcIEgU-UncTQdtJMns5VeJL35dtbcTzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee0be552a1.mp4?token=nwurp0bEbz8M2u9UM2ZGpeUYS0VlIZPtBUovEVP5B3TtUeL8sk1j3QKVaNvWntsTaj4u6UEPEwEgKJPxU0vl65p0wX66N9DG6dE77JWdQqPPWvyXd_zPC1V9hUVTtu9YnMBewxAnhbOoo5AqocZlLXyi-GN3xKe0L98kdgSp1cn2oUg0ZN1ECGQEbpizLxrk5dYo4KBq52RIxWcyH-pWwkud_N81fh0TahbjIQKOvGjp7dBtUIewBn689ewisFeAnZtEvjD6O9EpBv3Ic2ccaOSkXPqNyqEfDadqWvp7l7uNrhCVq_2RHdjwcIEgU-UncTQdtJMns5VeJL35dtbcTzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بیش از این‌ها تحقیر بشید !
چه در ایران، چه  در لبنان، چه در فلسطین،
چه  در دریا ، چه  در آسمون!
در ضمن بهتون دینار و درهم نمیدن!
قراره یونجه بهتون بدن و پولش رو هم بگیرن!</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/farahmand_alipour/5809" target="_blank">📅 12:55 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5808">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n5sKKqfq7klbbVnTyMY8LL5tkpX_JX43zMM2AMzFn0Wdm5_M4wtbfcdzRv2zhnGx9BZPBS1Dzql-u9HDgMpNdB2768p9dPSx9UUgyn7lj7J8pokljJXNoNvF6cV7OO2d3gyPCOMwYcgs-zR1RdcdFoLxfq4LcroFSn1FYXo5gPuGzQtPdu_C0807bId-jHRBpo9yhhZp8gEjHKBvQoHEak3jBwdcBco-XFrxibGwLEsfEFhC7MNcNeWJJqUYqz3FaVHfw4QVZU81foZ3vzkocphtMWpxEKSuGD3Sijzo20UeopuNyRXKUQXNSEvrfrGNsd-P0ki8iG5NMVzLOoEdEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقبره رهبر مستضعفین! که در زمان حکومت خامنه‌ایِ ساده زیست! ساخته شد،  با مقبره فرعون‌های ظالم!  که به قیمت و نرخ امروزه، مقبره خمینی ۲ برابر مقبره‌های فرعون هزینه برده!  ولی عرزشی که نمی‌فهمه! بهش میگن رهبرت ساده زیسته خیار نمیخورده، خوشحال میشه! دیگه بقیه‌اش…</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/5808" target="_blank">📅 12:47 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5806">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/U2vIf0o7UHO6WbI-gXEdqBy4ta5A5SqUxRPvOTt3o0qUIUZ2i4Cnl7utg0snefKidfyhNOeP8vDjxNsTfWhezPotSuuMYgIpGVHtd4EnIwEeNrMJazDrsNd6ve_YcYOHT6bXEle64QfeOlWCvKhEIdFBrub44aL4JhNLEmFsa_6dYXcaNhWBuyaSxdYYtaWhCRsnf52sxNAMaxbm6qGixdT6JI_De1CIsdTMlb0MUPYVdqncnL0LcL1yG79AWa_A0oXOS9DhJ7CRv90Gb2L2WppPR9t6rMKrJsy2p2jwKpTkyvv1Sbt8C1w14Rdz2SLRUUmsJK5GjzLCRQu50sa61A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DwUKmepNljWg3dU4PGn4M1ikmZ6Luj118rg4TG0r_9hdqHhpZex2KBUgwgSL13GyrA9EUTZRdp7EfibeiC9nfc3QZxO40TpfFkjiN4KXROsw7I2gq_JgjbRmlC_yZdJhpqTroGyjiIhLL_3EHpsTX-WRkFPeaZ1gBrvQ6xF_A61o0-uUMxWf_ij5P7lkfBWt9g8p27kUY3npOrLfLBRxot-JzuPhR6YF-ppSWHsuKtZld_QD_WcG6QB4ZRi0Y3LwTrHHDr76mKp87yAh9vrPlZ_tBaUIOTC9Ev8jtokF_bo7o6nfKLfpb-bcSgLFP1dBB_QxoFc3CwZoNEWlpWrNwQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">هزینه هر روز تعطیلی تهران،  ۲۴۰۰ میلیارد تومن خسارت به اقتصاد کشوره!  اینها فقط ۳ روز برای خامنه‌ای تعطیلش کردن! یعنی فقط این تعطیلات ۷۲۰۰ میلیارد تومن خسارت به اقتصاد میزنه!  این فقط یک قلم از این هزینه هاست!!  ولی خب رهبرشون «ساده زیسته»!  خیار و هندونه…</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/farahmand_alipour/5806" target="_blank">📅 12:35 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5805">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kpmkPDKw-UvrIrM9MjIQiAG1KumGeYELD96cRBytuk40wcZLBrAO2eh503n_AJgdtfWs2MwXoBGGal4H4q7Of_RaRm75EcQ98bX4KVH1nrZOzbgpTmL8HsO65PDvAyHlQau-ZUZSjrPlBE6uPU8Puoud-2CHV02ZlATIVVASYhSyme2WPTqKCjNKPkoCdJo7Zk-Rq5EUTfairBklOsKG-qiUoXowxWKNMRwxbYKstq1cLyN4cnKORqbh1D98rife26tR6SrB_F1egbLBwPMraDEOprjmcqvMGD_QhyH22Yb5-P1nB1r7a26RXtU1tGPxr7nrFayJD0YYuaENcx9k1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هزینه هر روز تعطیلی تهران،
۲۴۰۰ میلیارد تومن خسارت به اقتصاد کشوره!
اینها فقط ۳ روز برای خامنه‌ای تعطیلش کردن! یعنی فقط این تعطیلات ۷۲۰۰ میلیارد تومن خسارت به اقتصاد میزنه!
این فقط یک قلم از این هزینه هاست!!
ولی خب رهبرشون «ساده زیسته»!
خیار و هندونه نمیخورد!</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/farahmand_alipour/5805" target="_blank">📅 12:29 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5804">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b7a3755d2.mp4?token=P8NH9hragGVc-zMVIky-nPbnrw4nEyQjixJouBMkYl1t8j9aa3cqSsl9CZk7y_NfPs9bdt-xXLTmRhePFeBQpXQBJaXD7FuDoLgcqIqrI6LV2emAeQRG9Mo8ZYZWQ32pi6PBW7WLMZyfpM7C5lq_5gv4cFbpGsrKIonE__uucyvUa_YZud_VWudCgr1urg9SRAqad29zyM7Jv7zKpix8_VW_zBwx9pEQpOVmGdh1xGx4Om8IfD5r9OY9fAUaS5-XgJOBX2WThpEC1s8jb3KB-TfCUp6OX2z_Pq6F9YP3tMBJqpPFvb3fTNqKUnqiz2cbEcq4wfpZ19_JhOvYOggOxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b7a3755d2.mp4?token=P8NH9hragGVc-zMVIky-nPbnrw4nEyQjixJouBMkYl1t8j9aa3cqSsl9CZk7y_NfPs9bdt-xXLTmRhePFeBQpXQBJaXD7FuDoLgcqIqrI6LV2emAeQRG9Mo8ZYZWQ32pi6PBW7WLMZyfpM7C5lq_5gv4cFbpGsrKIonE__uucyvUa_YZud_VWudCgr1urg9SRAqad29zyM7Jv7zKpix8_VW_zBwx9pEQpOVmGdh1xGx4Om8IfD5r9OY9fAUaS5-XgJOBX2WThpEC1s8jb3KB-TfCUp6OX2z_Pq6F9YP3tMBJqpPFvb3fTNqKUnqiz2cbEcq4wfpZ19_JhOvYOggOxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">برنامه «زیر آسمان ستارگان سینما»  در شهر بلونیا در ایتالیا  که ۵۰ شب در طول تابستان برگزار می‌شود.   (در عنوان برنامه در استوری اشتباه کلمه سینما جا افتاده بود)</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/5804" target="_blank">📅 11:16 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5800">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf427145cc.mp4?token=SOxEKyK4UONVEs_jCvmcTkAVD6f3VoXuKGYugijsEe33NkInQANRuYAejVodolA1OZt54t33EngkcMSyR3pGr42gk1gwuTEHcQR_TGwcLtUGvgbDiIrAF_jrS_2a5oUseDC3mdArdMQzJRCmxWR2mWuFLdZGpQr05p-fVyNCvrhF9XjHVeiiEBgsmHyhbgBoAj4KZWIEzho4pJY2512Q7NlsC_YIj520LnnnnlqPQUKVQLsmI4m40Q_YJwHtUbntbMRIG8679Gk1zAGPo6dwA_cUmOMv0UOrvJ5vYPatfM5DBOY-MMl4qYuaKN-fBuaJbX81AbpDQEPwItIcRGAZLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf427145cc.mp4?token=SOxEKyK4UONVEs_jCvmcTkAVD6f3VoXuKGYugijsEe33NkInQANRuYAejVodolA1OZt54t33EngkcMSyR3pGr42gk1gwuTEHcQR_TGwcLtUGvgbDiIrAF_jrS_2a5oUseDC3mdArdMQzJRCmxWR2mWuFLdZGpQr05p-fVyNCvrhF9XjHVeiiEBgsmHyhbgBoAj4KZWIEzho4pJY2512Q7NlsC_YIj520LnnnnlqPQUKVQLsmI4m40Q_YJwHtUbntbMRIG8679Gk1zAGPo6dwA_cUmOMv0UOrvJ5vYPatfM5DBOY-MMl4qYuaKN-fBuaJbX81AbpDQEPwItIcRGAZLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">برنامه «زیر آسمان ستارگان سینما»
در شهر بلونیا در ایتالیا
که ۵۰ شب در طول تابستان برگزار می‌شود.
(در عنوان برنامه در استوری اشتباه کلمه سینما جا افتاده بود)</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/farahmand_alipour/5800" target="_blank">📅 10:42 · 09 Tir 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/2dc44e27bf.mp4?token=SuDO1b3U3XDUCtn1CjCHc0vMgLyOfuV64-KH7BfIpznWbBqPeRRQkIzyRaFjbItLvGFFspsPIy6KSWjnUeybaJ4eo5t7YmxuGaZSEgsmlTCuexYJsaDJ57m-N5sEFrNzf9LhbOhxMNpbMkJLeSDVhkBVND8-eyUiAtnnSeY3wH1vKcHvsNVXJvlJyMmfsP_MUbCXY5Axk0qyY_xKBajCgMDVmDepEqMiLzoHo7v_wLNnLDUhGuSYBZXSudlFjZGkQjXa44Esx0rRs_6uRf-TZsb-92A678tQnL13LSMvVUTQ6WtS4gmGQW5W41UQcqp6P5rfdR4F8Pwd95aSw6bBkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2dc44e27bf.mp4?token=SuDO1b3U3XDUCtn1CjCHc0vMgLyOfuV64-KH7BfIpznWbBqPeRRQkIzyRaFjbItLvGFFspsPIy6KSWjnUeybaJ4eo5t7YmxuGaZSEgsmlTCuexYJsaDJ57m-N5sEFrNzf9LhbOhxMNpbMkJLeSDVhkBVND8-eyUiAtnnSeY3wH1vKcHvsNVXJvlJyMmfsP_MUbCXY5Axk0qyY_xKBajCgMDVmDepEqMiLzoHo7v_wLNnLDUhGuSYBZXSudlFjZGkQjXa44Esx0rRs_6uRf-TZsb-92A678tQnL13LSMvVUTQ6WtS4gmGQW5W41UQcqp6P5rfdR4F8Pwd95aSw6bBkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هرگز به مردم ایران نخواهند گفت!
اما کاملا قابل پیش بینیه که هزینه این مراسم بارها و بارها از هزینه جشن‌های ۲۵۰۰ ساله بیشتر خواهد بود! چندین برابر!
درست مثل راهپیمایی‌های هر ساله اربعینشون که باید از جیب ملت ایران مصرف بشه!
یادآوری : هزینه جشن‌های ۲۵۰۰ ساله، به ارز امروز، حدود ۱۲۰ میلیون دلار بود!
هزینه سالانه گروه تروریستی حزب الله لبنان
یک میلیارد دلاره! ۱۰ برابر!</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/5798" target="_blank">📅 09:21 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5797">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d3b713ac56.mp4?token=BVpyswLbxD11Laly8HZt1o4AiSz06iWJAHAom-Z5-NOrPpKxg_GZf3aL8_6626wknDXBx4VUZx_QkWdJ0Fg4hSf_Vy-4ItyevTUjsJSCFTS-TcUgVLyO_Em8Mi46iEctfgsw9bRWmqGmjtdN9QkbsbvLhb0R76xEFfq2mMXQjwINxGDIwsP8vMgOGXDOWCYezO1pLStgqlYBajaIzcgs-IKc7K1-Zm6MlV8V4vaikGt5oGyglntHbc68IULY207zuH3h4puhBrz4ktxEZ1mioMMd-XiiYb2HUDIzgz3BwByxjJSRMnv01eIob40_r7Ch7OtpsBPfMHP-4hU6BxPsqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d3b713ac56.mp4?token=BVpyswLbxD11Laly8HZt1o4AiSz06iWJAHAom-Z5-NOrPpKxg_GZf3aL8_6626wknDXBx4VUZx_QkWdJ0Fg4hSf_Vy-4ItyevTUjsJSCFTS-TcUgVLyO_Em8Mi46iEctfgsw9bRWmqGmjtdN9QkbsbvLhb0R76xEFfq2mMXQjwINxGDIwsP8vMgOGXDOWCYezO1pLStgqlYBajaIzcgs-IKc7K1-Zm6MlV8V4vaikGt5oGyglntHbc68IULY207zuH3h4puhBrz4ktxEZ1mioMMd-XiiYb2HUDIzgz3BwByxjJSRMnv01eIob40_r7Ch7OtpsBPfMHP-4hU6BxPsqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لحظه‌ای که «سپهر بابا» ستاره رفیعی را دید.</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/5797" target="_blank">📅 22:28 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5796">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e1e05c8825.mp4?token=u8WsNPzY0OK26DxJi-exqMM6bCIX52Zb8XlUNyidZn3r0YFGuqVwOT-3E_UKAvhBITXqbLHmsufyp8-sxjkCb0o1M_WEli8NDSdRNksy4hWlltNqJV897gST5YP4S6CnSbYm_YGSxZveCFFC-TSq6ssX35xps7monvxb4Sj4hcR3NZAG8iPESjmDUUs7xgnPwvV5KgYUy19dz2q1ZmhMKHwafN6qobdFRG2udOBaIVVBrNpFqfgmELzNgLwutG7TlMp2eSLeNGADYAqyVpeBSH62f_4BTsK9d19mbrSDZTNiIZ5NzwPJ8Miv9Z1PIleWUx8yorLaow6NdEYeTHG69Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1e05c8825.mp4?token=u8WsNPzY0OK26DxJi-exqMM6bCIX52Zb8XlUNyidZn3r0YFGuqVwOT-3E_UKAvhBITXqbLHmsufyp8-sxjkCb0o1M_WEli8NDSdRNksy4hWlltNqJV897gST5YP4S6CnSbYm_YGSxZveCFFC-TSq6ssX35xps7monvxb4Sj4hcR3NZAG8iPESjmDUUs7xgnPwvV5KgYUy19dz2q1ZmhMKHwafN6qobdFRG2udOBaIVVBrNpFqfgmELzNgLwutG7TlMp2eSLeNGADYAqyVpeBSH62f_4BTsK9d19mbrSDZTNiIZ5NzwPJ8Miv9Z1PIleWUx8yorLaow6NdEYeTHG69Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تفاهم‌نامه ج‌ا و آمریکا رو به طور نمادین آتش زدند و گفتند که این قرارداد حقارت‌آمیزه که خب این بخش رو درست میگن!</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/5796" target="_blank">📅 18:49 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5795">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oRj_yeHKLGWtesWxhFR2T6aP1KRd2NlIp1EqatTw8F9t6-mObXWehxHU6SjCHzeymV7Nnw6BzMrgmW1STHxV2ua6C_Zb3AS5IxtqwTDLke26HlhPTIf3RZFhv218u4aQU_B-rZI1-TzmkBDMOaz1oyR-e_8fqA4mrgTwWMhftM0yNhitSXDJKmxcdMNhpyZTWBmIr9AZ4cyoDVlLPiYRcxQX4xJ5tE1Y1jjjvnkGSTEhAudtMcLP9VRPwqpbBbfqgxNycRLOCRn70_jxJdT-KnYBtdNOvfcL1udlodsPvwzYhE7-bW4gu46K-Mm8j7qMrMH7dQMTUqgkbG4OMadlpg.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/8e972609e9.mp4?token=My-VjezaqZCbgq6gLtgVb5asY4JC169LCUVrsR0Ay55hEpKudrlFJHCfDsIRWZIsfw8TlryfgqHUOd4Dkvdi5Ql1OmJc3twWIb2wwxmZV_85lUV4I_xtzGFtO3m4cn3HD4OuKwuECix0C0_6b_E43ArMNvBn9jISl2qTNGeGMJDpJDQz4ZjENzboAds5-5NwG5MTxBhm042vbosQWz4FGtqdaF9fmKdmiXfr86jH-C-au7dgkC0bQ0GJQXbUdOnK3sjTi7RytYd4W5e0QA0DyWp2qJqiadDwr-lapi2kovt9CbLXS284jRMDLv52QUkKI2mKJothrtACKzwtdkj_YA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e972609e9.mp4?token=My-VjezaqZCbgq6gLtgVb5asY4JC169LCUVrsR0Ay55hEpKudrlFJHCfDsIRWZIsfw8TlryfgqHUOd4Dkvdi5Ql1OmJc3twWIb2wwxmZV_85lUV4I_xtzGFtO3m4cn3HD4OuKwuECix0C0_6b_E43ArMNvBn9jISl2qTNGeGMJDpJDQz4ZjENzboAds5-5NwG5MTxBhm042vbosQWz4FGtqdaF9fmKdmiXfr86jH-C-au7dgkC0bQ0GJQXbUdOnK3sjTi7RytYd4W5e0QA0DyWp2qJqiadDwr-lapi2kovt9CbLXS284jRMDLv52QUkKI2mKJothrtACKzwtdkj_YA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این شب‌ها، همین‌ها توی هیئت‌ها در حال عزاداری هستن
ده تا مرد مسلح افتادن به جون یک زن معترض ایرانی.</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/5794" target="_blank">📅 18:39 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5793">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oAEEZlHyFGf2Aea3QIk_MrXkMyf6lnDOuKD3h48H6fAcdmuPJty2YftaYBD3m8YZyl9Vi-mQSfYp9Z4xl3Rec4wM_AqFs4GU-gS490G6YNFXaAp7OHlAaBYO-1Y0ChTrjFiTEVz9BhpBsoW5dNSWNpeBhm8BXdsnLrrC2rwVf1uGzzjx89I7V9MYoAEELJ-6-JJ65p7P034LPzGhTF9Ze_DaDf9HET6xWwuvQfCW7DQQDGtrkP4YGUYE-qB8_TWUVIW2gWdr4ETC6z4RKwLtjZnN4lsRSmz8Y4oOCaltgaK5X-UFniaa7mH3Wf2vXWl1dzt2oVPw8rJbHMMcttxrEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حالا در حد یونجه و ذرت ایراد نداره</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/farahmand_alipour/5793" target="_blank">📅 18:33 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5790">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E9gRJrgCVZnz1hSaOZOGT4IHUyraNGbfp1yLJyUfki4wP6u8NZY4msSoE4A749mTuwZaEbg9R-kJriyekIsNLWcQ0qmCeDSt-WH4v7jRgXeg9L9T5JB7wIOFMLXN0HuIBqTDdv5aESinq_fzj_fUFAl5NpMjQHeS2Lc7E6vfMchD1-aa8HLuNhC1xKjgDPE0VrUAFZlMrhMVe3LKwKfUCeLCfmtTdP9LaRyuPmtWjL75_hA3dbRr2P8wfqJrR3tFa0EwHYwN8-vIcA5en6vycX_vVNlpnSOiddwFpXEV0rko2b5EExMIxv91S38dbnlKT2DRQfIEonGWcCtYjeU3cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/651901a9ca.mp4?token=I481CjNkQbw3Np1YAq4fSe7IQMY84Jx2Aa_5K3EHACjC5KMn7jYZPkEp_iaMqk--hcBowxk8hAs_Yw_TkoMOP3AbY7YvzvtMm67vLfhkJ3NZnA0eUFSutm09j3xwYuGAEqmMFvtPjE4YL3VG0YDaDQWbF7mooQ6zP0CkAjCA-I98VIknvplwgIbUXd30No5R_d5020jgBEE9b9aeL_-rs9qpV-bZ3SOzhcZZR7g3gdflQ5hqsuyAAYYe6gp-fkGAyO9-aDzrXbtffWhkf9XEOMa616CSjI-euDNrnYnY-1fjrgXRoK4qBFoBiKvd0nywr_p2gKls6zSTnRy9wfry5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/651901a9ca.mp4?token=I481CjNkQbw3Np1YAq4fSe7IQMY84Jx2Aa_5K3EHACjC5KMn7jYZPkEp_iaMqk--hcBowxk8hAs_Yw_TkoMOP3AbY7YvzvtMm67vLfhkJ3NZnA0eUFSutm09j3xwYuGAEqmMFvtPjE4YL3VG0YDaDQWbF7mooQ6zP0CkAjCA-I98VIknvplwgIbUXd30No5R_d5020jgBEE9b9aeL_-rs9qpV-bZ3SOzhcZZR7g3gdflQ5hqsuyAAYYe6gp-fkGAyO9-aDzrXbtffWhkf9XEOMa616CSjI-euDNrnYnY-1fjrgXRoK4qBFoBiKvd0nywr_p2gKls6zSTnRy9wfry5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">«عالیه نصیف جاسم» نماینده پارلمان عراق،
عضو کمیسیون مبارزه با فساد، از نزدیکان جمهوری اسلامی، معروف به مواضع تند علیه فساد در عراق، چند روز پیش میوه نذر امام حسین کرده بود. دیشب در موج دستگیری چهره‌های فاسد اقتصادی توسط دولت عراق دستگیر شد، در خونه‌اش ۱۶ میلیون دلار نقد و مقدار بسیار زیادی طلا کشف شد!</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5790" target="_blank">📅 18:03 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5789">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">شعارها رو گوش بدید،  اینها اعضای سازمان مجاهدین خلق هستند. خوشحال هستند از صدور حکم اعدام برای «حبیب القانیان» ، توسط خلخالی بدنام!  جمهوری اسلامی اعدام می‌کرد، حذف می‌کرد، مصادره می‌کرد، بقیه  گروه‌های از جمله همین سازمان مجاهدین خلق هم تایید می‌کردن، میگفتن…</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/5789" target="_blank">📅 17:05 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5788">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/583cd57ba5.mp4?token=ZlA4FUq-X2sOP7DoSj0pHxLttQqF7tNStUiXN62RDg2NRznFgTe_nKJORQHxxk5uhJThvWHiauT42-3rqXI9nQ55Q2XJv3n_A-BVcl84Eqd6KfQbzFy5WjtpOi4GTDY6LIcXQ0nE_1AjFisXCqscXMr8xXubm7oquy7_oi8UvCRRnimuOZnJ0fmu8BEmbYAJ3cL8XwzXZ57zE7RlcKxdyMAx9NfUOSsHbN7IpMOPTCPpM6lxUDaMwBT0mmHDCpFUO2O7ZrwEN10_YeIFyz2dvaLUhQsN5AKtV6sNfJAAPphM2ujdNrRI_3ElVQHtPtoJQ7PZpZSAKsbtrSkJnaHz0jSEPh4pU9De0iYhVtlUHUgS8ZVTCLbKnKqtBMugpOS2b9hAAh7idMxoVPCeZcoP4B5j1ZPGp9ElsakykASAmRJ6tkNfCeM3oWhlstQKuz22-KOFRqZ_izYgqD8_ETDXRrF-szhRMygapXKiHm9z0mhHa1WGXRrvW7w8VAm56tLyLHh-SLaKd9_RuWDIBcC9IyWgjrAydkqw1oDoUa8Zvc8lMBo50mqrOGN39QFrsf-YEzYb8taZ7t1kbUGqIav_VPAtyfHE1IPz2WgVjxs7co50FHVjheZB0pBitf0Snk_dRFYbGomrvyywAdJLnGenGFcy4U343xIc0J50DonQtf8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/583cd57ba5.mp4?token=ZlA4FUq-X2sOP7DoSj0pHxLttQqF7tNStUiXN62RDg2NRznFgTe_nKJORQHxxk5uhJThvWHiauT42-3rqXI9nQ55Q2XJv3n_A-BVcl84Eqd6KfQbzFy5WjtpOi4GTDY6LIcXQ0nE_1AjFisXCqscXMr8xXubm7oquy7_oi8UvCRRnimuOZnJ0fmu8BEmbYAJ3cL8XwzXZ57zE7RlcKxdyMAx9NfUOSsHbN7IpMOPTCPpM6lxUDaMwBT0mmHDCpFUO2O7ZrwEN10_YeIFyz2dvaLUhQsN5AKtV6sNfJAAPphM2ujdNrRI_3ElVQHtPtoJQ7PZpZSAKsbtrSkJnaHz0jSEPh4pU9De0iYhVtlUHUgS8ZVTCLbKnKqtBMugpOS2b9hAAh7idMxoVPCeZcoP4B5j1ZPGp9ElsakykASAmRJ6tkNfCeM3oWhlstQKuz22-KOFRqZ_izYgqD8_ETDXRrF-szhRMygapXKiHm9z0mhHa1WGXRrvW7w8VAm56tLyLHh-SLaKd9_RuWDIBcC9IyWgjrAydkqw1oDoUa8Zvc8lMBo50mqrOGN39QFrsf-YEzYb8taZ7t1kbUGqIav_VPAtyfHE1IPz2WgVjxs7co50FHVjheZB0pBitf0Snk_dRFYbGomrvyywAdJLnGenGFcy4U343xIc0J50DonQtf8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/938419e982.mp4?token=KS0lK9yB5-Cv6rToRwmecGEn4Jcw8bro3cZPrYvRXiNLQZgumPx0I2PHWW3idDnPDQBGo2Nq4Jif5RCfMXyNGQMcf9vZw8849JHkvP96cj4uocfAqTkK01tJRl-4SkUMXXyq9GBzkKTbxAj99SIWYX__mOcHiOfy7gQPrIjrOCaeTQhPv7isagn6xfmU5MprvkGvVzpaf_OSyEYY4MPLniUpc-rgwH8LytMYqgiJ8nH2Hv61MejMoKLC_vNOGZNzw1lPx7WFdN0e8GQeV9ydlfhew6lCohM7OMrjpqs3h1yb9H-0hXETJ6B6uvS973XVyMcBLG8jAPdFxmvl1v8lJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/938419e982.mp4?token=KS0lK9yB5-Cv6rToRwmecGEn4Jcw8bro3cZPrYvRXiNLQZgumPx0I2PHWW3idDnPDQBGo2Nq4Jif5RCfMXyNGQMcf9vZw8849JHkvP96cj4uocfAqTkK01tJRl-4SkUMXXyq9GBzkKTbxAj99SIWYX__mOcHiOfy7gQPrIjrOCaeTQhPv7isagn6xfmU5MprvkGvVzpaf_OSyEYY4MPLniUpc-rgwH8LytMYqgiJ8nH2Hv61MejMoKLC_vNOGZNzw1lPx7WFdN0e8GQeV9ydlfhew6lCohM7OMrjpqs3h1yb9H-0hXETJ6B6uvS973XVyMcBLG8jAPdFxmvl1v8lJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قدرت حضرت عباس</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farahmand_alipour/5787" target="_blank">📅 16:27 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5786">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ivE-EABHWgM1J9Nk_-IlQB0e_OqHjbcqBdBNuMHqEpp2a3Zqu7vOrbzvkxOkI4IUG7hdflybw5uh0LYTzhma5dKp7bPCQxBpR2oDFpTlVXGRnFMUQ8T-pOj9BBjuF_wJmj-i83h8q1zBFby4DNFeP9wv_m2EzDSp1d7ehGOb1MRZxPOydi5vXJ0uOxrKLYjNp8fH-0MLTsTeGUJ2KJ5MglVzByATMFkAtonRRdUM6qCud21WEs0Y9Yo0JlAUJAJHwjmny7DHh84KtJL093fZJwDj88vPfjbAeVnTvv-Th9heIl8mSY_t7QLkzk3gfhK7g5E49o_mxBacZ1OZWNkMag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای فروردین ۱۳۹۹  همکاری جن‌های دشمن با سرویس‌های اطلاعاتی علیه جمهوری اسلامی!  همین آخوندها وقتی اصفهان در محاصره ارتش محمود افغان بود به شاه سلطان حسین میگفتن اصلا نگران نباش که ارتشی از جن‌ها میاد به کمک حکومت شیعه!  ولی این جن‌های نامرد نه به امام‌حسین…</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/5786" target="_blank">📅 11:31 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5785">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b91e9581d.mp4?token=Hc81d_igbeRh_BBV7_IBQ9_Dwuteyye4ElHw4aTbjvLBEhfXbpwd279sdRE2qS5ww5kY0NC4GJL9E83OkoblNFZGtCT8i88jsDQmYgYZwsKuXvFKOHpAWncjrbzYwjn0t685E5vG8vCyvjWW6GOiwSLYNqJb_pbMViENUx4NW4ZNigTtJIWZ-hk_0un6WXdQA5Mge6RW8W1sYABUOg4dQ6ZJidq0MBthEmtsFlBZOc0rMe33cQx6fP3KysHA6jrnh1F_mflfDQuGVYNtvUhYB95-pJddxgou0EGQzWR8JyOf3HaEpUI4t3MvuNE4ZMZVbbckgYv9SC8bWtqAOYP_Uw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b91e9581d.mp4?token=Hc81d_igbeRh_BBV7_IBQ9_Dwuteyye4ElHw4aTbjvLBEhfXbpwd279sdRE2qS5ww5kY0NC4GJL9E83OkoblNFZGtCT8i88jsDQmYgYZwsKuXvFKOHpAWncjrbzYwjn0t685E5vG8vCyvjWW6GOiwSLYNqJb_pbMViENUx4NW4ZNigTtJIWZ-hk_0un6WXdQA5Mge6RW8W1sYABUOg4dQ6ZJidq0MBthEmtsFlBZOc0rMe33cQx6fP3KysHA6jrnh1F_mflfDQuGVYNtvUhYB95-pJddxgou0EGQzWR8JyOf3HaEpUI4t3MvuNE4ZMZVbbckgYv9SC8bWtqAOYP_Uw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زعفر جنی، پادشاه‌های جن‌های شیعه
😅
حامیان همین‌ها میان کامنت میگذارن که تاریخ مطالعه کنید! محتوای تاریخ‌هاشون!</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/5785" target="_blank">📅 11:29 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5784">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb5c00112a.mp4?token=r0QADmPB42n1HfmEdmgska_t7ZaKo3IrhvdcIcGG_Yd7uToPPhNVRN4ppdDSpEL7T4Np5enNKGb-nQH17ASXHx-fk2wZIgt5mSLd2VMM3mId46fy2jll9z5KbPnyG6iZHWlfMUZMU3tfQd6DxTJQqHQ2q6wqgpbaVR9r8KBVryyBxOQlqMKZC8ywaeWJrXrrOda6qes4ibc8dkk6Vz3W1lWbBaQauGHns0RX2r_Y_A7vmwlZ6tKQe5efG0ulNmq6NepEnqRfYoyyR32dcpyYsFHmgFOnm0QOipDvGtBYehWYtUT9HtlCOIJhqWDz0Bh8C6ha2OJly2wsnAqC-B3mLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb5c00112a.mp4?token=r0QADmPB42n1HfmEdmgska_t7ZaKo3IrhvdcIcGG_Yd7uToPPhNVRN4ppdDSpEL7T4Np5enNKGb-nQH17ASXHx-fk2wZIgt5mSLd2VMM3mId46fy2jll9z5KbPnyG6iZHWlfMUZMU3tfQd6DxTJQqHQ2q6wqgpbaVR9r8KBVryyBxOQlqMKZC8ywaeWJrXrrOda6qes4ibc8dkk6Vz3W1lWbBaQauGHns0RX2r_Y_A7vmwlZ6tKQe5efG0ulNmq6NepEnqRfYoyyR32dcpyYsFHmgFOnm0QOipDvGtBYehWYtUT9HtlCOIJhqWDz0Bh8C6ha2OJly2wsnAqC-B3mLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/383f2c1b20.mp4?token=nwpwZwJ7PHcVKUZq_mumr5nQ2EzH_WnNQEwrZzdJbCuuoFJcQdDqNh-hPdHumCXdmFGObznFO0uggwqDF9tHXkWHZ5PBLR8ZsiWHxQEh00RVpzOx5LYsBqbV3UNzByc_8XNtSVusWz931zGp4yvvyVuUkYa5Lk5p2A_LOzAc-WhMJiOLq9VP9_7e8a26NQEnRUljRiIf9jO4be4lgyMQw7KItqvZtyR08Qx3D_8QNBfKJ4bp_ZcCgAPLS-9HZ8omhIeWRgLjWMFwbfwRmjE2wgJUSanWPtEA3cfLZbGjwGHBeK-9EdkLAorsOfN2efRJYWD3GNllf1TG-pCuIglkNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/383f2c1b20.mp4?token=nwpwZwJ7PHcVKUZq_mumr5nQ2EzH_WnNQEwrZzdJbCuuoFJcQdDqNh-hPdHumCXdmFGObznFO0uggwqDF9tHXkWHZ5PBLR8ZsiWHxQEh00RVpzOx5LYsBqbV3UNzByc_8XNtSVusWz931zGp4yvvyVuUkYa5Lk5p2A_LOzAc-WhMJiOLq9VP9_7e8a26NQEnRUljRiIf9jO4be4lgyMQw7KItqvZtyR08Qx3D_8QNBfKJ4bp_ZcCgAPLS-9HZ8omhIeWRgLjWMFwbfwRmjE2wgJUSanWPtEA3cfLZbGjwGHBeK-9EdkLAorsOfN2efRJYWD3GNllf1TG-pCuIglkNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همش ثوابه :)</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/5783" target="_blank">📅 11:08 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5782">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a9c5c701b.mp4?token=XcXlV0sk8DutevXzHMCR07za4US4mPq7ylRHQqF01Ijle85uXY8kfIq7h_zlu48jLXqfeQmqUxvZNwfkz3-kuYeViaSc3BlAV-EBWvyACgia8rJ-BUf6AcY6SAsUxVqdZd2IdzRg6V12jC6rTcf2w2I1goYRUqRYV9Vh-o2WJkWIqe_jPoka8IQU51lrU_C1aylbK6oLp8AvLAya1wS_Wga4u374wU3oXEVfsDJ6n46XQaXOLa6ITOo3Q_hYd9mVGGFw-aQ5I08SCSq6Cl9zHepOJyO9C7eoSbFRoQMNgUu1Y6Kcy6jvNrbC8hugCY_tRTlVEcJjjxWWOc8-CKiTOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a9c5c701b.mp4?token=XcXlV0sk8DutevXzHMCR07za4US4mPq7ylRHQqF01Ijle85uXY8kfIq7h_zlu48jLXqfeQmqUxvZNwfkz3-kuYeViaSc3BlAV-EBWvyACgia8rJ-BUf6AcY6SAsUxVqdZd2IdzRg6V12jC6rTcf2w2I1goYRUqRYV9Vh-o2WJkWIqe_jPoka8IQU51lrU_C1aylbK6oLp8AvLAya1wS_Wga4u374wU3oXEVfsDJ6n46XQaXOLa6ITOo3Q_hYd9mVGGFw-aQ5I08SCSq6Cl9zHepOJyO9C7eoSbFRoQMNgUu1Y6Kcy6jvNrbC8hugCY_tRTlVEcJjjxWWOc8-CKiTOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آورده فرهنگی شیعه برای ایرانیان</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/5782" target="_blank">📅 09:32 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5781">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tUw4qtKW5mA6ceqaPx19VnhW3InJ7awdeyvxIGW2FgkHn_Zznlbvi87JphhoQM5CSjGuLDQBekLHLYUpjCWKHJM4SfHrKed2sLnZ4xqdNjhTpcw8KtzqQruGDIkui_YSC_sdt09bABvcdxMB7H8nKKpFRbAa88rDUZRl_4YNulx5_llEl349mGizAHBrsBM1R10u23AJjriAznN7FzQExBWWQCj7S_YNZYH3ZmYYuw_c_g4SoB_F8kqbDFbcB-0GuTcNDcHvnI9HMrgN7RolO8E3lRWQHyauWGkeP4vWKDev0Jn5ugpngI1wRLEj5918oRrPBO4bZlDqAsgU_MxwAw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/409f2a841d.mp4?token=dvSGqVl4o1AHMYuJdGZ6c_PtdP-YZP8XryZSwTe_499-LCyDXTVZ723eC1ARajz7wKPUhhMKVZ0pyXA9sfuMag4nlLULf4mOT3IMOQOqXDANHGkO6ZpghJl0JJNb4c118MjexR9GYYmsDcbPLSZwI8dWZzKHS_GXE1r-P1z7J0ZZx5VF4Cym-FMQds3ERPNqgZeJi0XQ-5tLb8KNi-IMFuTT-x3GImDwaSCXgXiy0ujqR7SGhfwauGWElqdc2a9hFAiRJtMAUrjt8kxTglOZbtCSdmZhp5WrZsIKhIvx0WP7xbpPzmdLuf0hRyW30_XELVViFmKCXLbV3cOAQXIyTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/409f2a841d.mp4?token=dvSGqVl4o1AHMYuJdGZ6c_PtdP-YZP8XryZSwTe_499-LCyDXTVZ723eC1ARajz7wKPUhhMKVZ0pyXA9sfuMag4nlLULf4mOT3IMOQOqXDANHGkO6ZpghJl0JJNb4c118MjexR9GYYmsDcbPLSZwI8dWZzKHS_GXE1r-P1z7J0ZZx5VF4Cym-FMQds3ERPNqgZeJi0XQ-5tLb8KNi-IMFuTT-x3GImDwaSCXgXiy0ujqR7SGhfwauGWElqdc2a9hFAiRJtMAUrjt8kxTglOZbtCSdmZhp5WrZsIKhIvx0WP7xbpPzmdLuf0hRyW30_XELVViFmKCXLbV3cOAQXIyTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش اسرائیل از نابودی یک تونل
در روستای مجدل زون در جنوب لبنان خبر داد.
این تونل ۲۰۰ متر طول داشت و در عمق
۲۵ متری زیر زمین ساخته شده بود و در آن
سلاح نگهداری میشد و دارای چند دهانه
برای شلیک به مناطق شمال اسرائیل بود.
اسرائیل گفته که پیش از نابودی این تونل
آمریکا را در جریان قرار داده.</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5778" target="_blank">📅 23:57 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5777">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/06f2d554a0.mp4?token=INrtSCbxZEr3iLAoj7niL5umiI27KPVc1yoMn5TGChnURyO1QDyQNnVG0UhO9p1u3xajarlMmNCov82Kt6wnfMzA6-yiuA7EFXjj_Kk6-eqoCIi0DRXou37c4VZtB2XsWKohUydnM3JZXatUUjK1oKwQc2nyRKGnzNGu7bwWlehWkBrrtSPFPcN-k8S7siRm0ogiGFS4TIjttvBuirnG1J73P39nbF1dyVw6SP2VX9k8Hj8Ua4iq7c7lX82seWnUQbc086CMe74_Ad1guRULdg63ouEImTOcL6DyUBdIT1ko3CsI6VnK3UEqfGTY0DrcucrsFEMWRzIYq0zob6wbQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/06f2d554a0.mp4?token=INrtSCbxZEr3iLAoj7niL5umiI27KPVc1yoMn5TGChnURyO1QDyQNnVG0UhO9p1u3xajarlMmNCov82Kt6wnfMzA6-yiuA7EFXjj_Kk6-eqoCIi0DRXou37c4VZtB2XsWKohUydnM3JZXatUUjK1oKwQc2nyRKGnzNGu7bwWlehWkBrrtSPFPcN-k8S7siRm0ogiGFS4TIjttvBuirnG1J73P39nbF1dyVw6SP2VX9k8Hj8Ua4iq7c7lX82seWnUQbc086CMe74_Ad1guRULdg63ouEImTOcL6DyUBdIT1ko3CsI6VnK3UEqfGTY0DrcucrsFEMWRzIYq0zob6wbQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">منطق جمهوری اسلامی
و تعریف «امن» و «ناامن»
میگه اگه  یه کشتی بخواد از مسیر «ناامن» عبور کنه بهش شلیک میکنیم :)</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5777" target="_blank">📅 23:26 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5776">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s6dtMQHTU4TAcnHVCeNwWv0X6yCJ74CR3neVbVQsf-Qk9BuBr3LGT32mkohFiVTRCUGmcFTgVxgt3E5MpDexUvzC9QnYJy0VXi5S0y2sXNu72Vzw4oNcbYBCnY8t3lezW7vRXbVKBiyamj4Zhs9Ko55iEbD3vvpHZ3mfyOJ_Qp4eKk6SYqnqusa3aAYIMJvzy4CrdHUAu3AbLIE5SvFGg7I2NHwcJgcmwAeWUtTkjrb6ZNjbDLMGJgMpV3S5pwXqD4P7UQHgkhGRfACm_qsiwtdPC6UH_JbwwtRLiJlq22jSR0QCopU9x0zuyyKEopMY9XRaoO4ZKaiSqnhdm6WT8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس: چاره‌‌ای جز ساخت بمب اتم نیست.</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/5776" target="_blank">📅 19:39 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5775">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e4e9d7782.mp4?token=cdngsmArWKbruoPemEQx8JrEXkOHwvxNLbU3exkMbYui-1SV5n6KoyGvMQYHEPX5fZ56ASIG1U3d0awRByB_9aTXDdAKGyoWPHnkwlAlvD3lPDiRNqTBmwmVmC495c-yclAmne73XV2a_MwXInZ1wCjS3h-IYcp03Htb2A1v4nN-iQIk7VTRbA_t6hjo2_nywkQtbP52-NIBfafzOlWovuxMO0FpboxW9KEAOoiEvsv40OWMCgfYEOZ3aeGs4PRHxPhpjLOZbZGP5NiwBkO4tJcPBFT-wDe857bY5wtDz042I6thj3rHg3UKCpO9yl1qulTYV_5Gy976LqtFOCx6BA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e4e9d7782.mp4?token=cdngsmArWKbruoPemEQx8JrEXkOHwvxNLbU3exkMbYui-1SV5n6KoyGvMQYHEPX5fZ56ASIG1U3d0awRByB_9aTXDdAKGyoWPHnkwlAlvD3lPDiRNqTBmwmVmC495c-yclAmne73XV2a_MwXInZ1wCjS3h-IYcp03Htb2A1v4nN-iQIk7VTRbA_t6hjo2_nywkQtbP52-NIBfafzOlWovuxMO0FpboxW9KEAOoiEvsv40OWMCgfYEOZ3aeGs4PRHxPhpjLOZbZGP5NiwBkO4tJcPBFT-wDe857bY5wtDz042I6thj3rHg3UKCpO9yl1qulTYV_5Gy976LqtFOCx6BA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تیمی که با بدرقه قاتلان جوانان ایران راهی جام‌جهانی شده بود.</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/5775" target="_blank">📅 17:23 · 07 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/5773" target="_blank">📅 10:17 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5772">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1220ffd18e.mp4?token=PBXJnX1boq8WVsr1jJi3sHJbjk73gRvHWdbkPDMDLRmBjDSpl2onHkSjlACDpWDwMsYk81IJB5KP6rGudubvdE7VyrOARPwVdpLDbZIjBwXoohpsJlxQSVBWIVnQfhngKgwn2LbO8VpFUhkCy571TaAjG0hlE2skkuQhRQB92dEdlj37iDpAHNmTzwLV1kuTQr7MXmAE0hYK289Uij4jKv9JTD2DtGnV3TH9cFkiv4W9oXF9PHLrmbwa-O9DowjPNuWPyRqVGByCUX7Amn5jZQ1kK0cnV4caewcVLWVM-p2isCSt2mP234o6BqDRAaX_OnnRMQCqxMRoXGSRnRzozg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1220ffd18e.mp4?token=PBXJnX1boq8WVsr1jJi3sHJbjk73gRvHWdbkPDMDLRmBjDSpl2onHkSjlACDpWDwMsYk81IJB5KP6rGudubvdE7VyrOARPwVdpLDbZIjBwXoohpsJlxQSVBWIVnQfhngKgwn2LbO8VpFUhkCy571TaAjG0hlE2skkuQhRQB92dEdlj37iDpAHNmTzwLV1kuTQr7MXmAE0hYK289Uij4jKv9JTD2DtGnV3TH9cFkiv4W9oXF9PHLrmbwa-O9DowjPNuWPyRqVGByCUX7Amn5jZQ1kK0cnV4caewcVLWVM-p2isCSt2mP234o6BqDRAaX_OnnRMQCqxMRoXGSRnRzozg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شجاع خلیل زاده میخواست گل بزنه و تقدیم رهبرش کنه!  ولی اراده خدا تحقیر اینها بود!</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/farahmand_alipour/5772" target="_blank">📅 09:32 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5771">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d645372fb2.mp4?token=raSAl8e7oS0pQCextJ6I5q-Q-kTmqKM94Hp4C9oNeLbqvgJkv1INPKFzii43sqqECuFL8mYv_67B6zvy_w5IJJv-4X1WM8PmJdK8U00vgidEXL7D_7BZaywMQMwp_ttmu-GvmoEHlTlEhRY1Xl6ztJX35yjAxIJ5fxREkIguyULtbtYOVDNe0DiAM-KuQpQKKm39TF1FrBnxK8eTmTNadmwHdE4UyoB20PwW74iwzmlYNaFilbqalD1hYadhLBhuYJcp8PEfzWrS6TXEtb3fw6fCVv3oFABxGGxJatLULeezVNK-DMnepSUwMu1QCa_SrFNN_akVvffykEOLGohtFYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d645372fb2.mp4?token=raSAl8e7oS0pQCextJ6I5q-Q-kTmqKM94Hp4C9oNeLbqvgJkv1INPKFzii43sqqECuFL8mYv_67B6zvy_w5IJJv-4X1WM8PmJdK8U00vgidEXL7D_7BZaywMQMwp_ttmu-GvmoEHlTlEhRY1Xl6ztJX35yjAxIJ5fxREkIguyULtbtYOVDNe0DiAM-KuQpQKKm39TF1FrBnxK8eTmTNadmwHdE4UyoB20PwW74iwzmlYNaFilbqalD1hYadhLBhuYJcp8PEfzWrS6TXEtb3fw6fCVv3oFABxGGxJatLULeezVNK-DMnepSUwMu1QCa_SrFNN_akVvffykEOLGohtFYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شجاع خلیل زاده
میخواست گل بزنه و تقدیم رهبرش کنه!
ولی اراده خدا تحقیر اینها بود!</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/5771" target="_blank">📅 09:31 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5768">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FwFJllDlHSXPnS91BiOXztkp1FE-D9XlKQF_TatNQnDNdSq5LJ5sf2I2FeYdhOJYCBguIz9cVKM7JvGXP3DVnMguFrPndsQhKYLaDQXfdAQTmuBcPf_rSUN-tMLJjgELFrEcpxVUuvjJvW34YZLnZeh32XJ6Ru2ERme5jeJvxYHzFynG9CLWM3zJPgj6bVCNvDRjWqUxxWI292RRplpPUFSsTwTgoJrKwJNSJwKE3JNEYIs-0L0sav5bG60DfwW2SSRATCaD3jv0H1Oo8U3J7oWMspmhIXHBAV2dALJ0Vn8EaiSROo6j9fzTP0T-LxjSLA9x3mk6GREkgigJ__a2KA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bbef2BfcpaamjcPJqiDHn3rwMOM2WL_ab2ytv8Si6EnqPMoQPiDCU7gBny0935mJVUImV4PXDFb_8U393qZuZkb5FtZP_RjJKXvavGQorch5h-Z82CrA4MPbyvlMISpVnnWYMK1pqurNF47e_X9Lp8WSf_KlqngyeLzPRxzN6sSHMeqrtSfnfSqzl8LjB7Ub3Bt2mA9tkUods6h3Q04UJd-hFNXryov10cz1zbAfyKbP9aeA4_1lpje85Bzk7bonyz19rCbxeOfctXzD_nt3e_9_qHvk-8Ff2QpVEi5U_XvU2Yl7-xJ-IWEQ9XXzVoo_V6mDNwiQWkqO48WToMdzBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FId3IQUUDa11Dge4-yRE5XEMq9B60pZTeNbZRRKuOQup2LQGNjYJ7RE6JAE4x3iwMN5todAaL-Bgtjyjw2Kx0uWfj3YWkWtCzp8EyaZPDqQcdFuqp__UvUPgQREew00CpfQt8mwqBizHmQtxQEr0WhObCg7LBWXlkfqcdNri-Fx4eyFuPFDRt3XjADMTbzz6myqE_h-EfrGJ5FUATQIws5J8xNmpi5eiqlz2ypPJiIoTeppFfZlpGLwfahPEtZAu8haUxNnWvLrFlEJG6mU8XgEfwMyxiQ1Do-SYq479BBrzyQ2RKTUq99mWKWE6iOc0zTppGk0ycJ8Vt3hrI6YRlQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/10689e4ea8.mp4?token=QHFoDZqAN5HKiGDouVUTLKmv3r29RNfNc65w_0LUx8wVj9I6gVNsCRgxL37VuVxsIQ9dZ3CEmrfCXBZ5oUVCWscHUHbxfkal5v5jN_hGI6VayAw0Cc2inNKh9y_bwgkHX70o0NB4H6rg8ero2QgMmKnSDWfyxUmZDUBoQeZ2QxpvMrdCMheGIjyFEzYm92UfzarmJ_Poi8pLPeBji2gY7hdWEEg4Q9p3tefuLvDxkuhcVbDuM4fMbZZVN-w1rfNIYX2LSUfjuMHzPj1aPUTEigg_oxDfkDAW7d-3UfpX_JwOaO-uWzF-Ad1H1QkQ7RgoQgJJW_n3dIWCszckHmZY2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/10689e4ea8.mp4?token=QHFoDZqAN5HKiGDouVUTLKmv3r29RNfNc65w_0LUx8wVj9I6gVNsCRgxL37VuVxsIQ9dZ3CEmrfCXBZ5oUVCWscHUHbxfkal5v5jN_hGI6VayAw0Cc2inNKh9y_bwgkHX70o0NB4H6rg8ero2QgMmKnSDWfyxUmZDUBoQeZ2QxpvMrdCMheGIjyFEzYm92UfzarmJ_Poi8pLPeBji2gY7hdWEEg4Q9p3tefuLvDxkuhcVbDuM4fMbZZVN-w1rfNIYX2LSUfjuMHzPj1aPUTEigg_oxDfkDAW7d-3UfpX_JwOaO-uWzF-Ad1H1QkQ7RgoQgJJW_n3dIWCszckHmZY2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/17301f18ad.mp4?token=QULzo3rvzxGgtlWKbr09sAjSPdBNLTTD6v4ZnFO0pB-mF8HJbDAFMF1UVBRtzUIfdobam9wrfnicbWw69Sa9ne42x177tzGSmC5cVhwpisHBfiSUOOJNMRHklUGbL7FUhFewM8f9UTea7YYxWrIZVVwR2YwADLb4ZBaVviEU74dHdhA5HZyOfa0mViNiNFiufRGoxSt82afiYFnhqWJlfy8eqPPnJdmJuhT-Fatqf3-Dpm03dm2AfkLJwwDb-VDd3qa_cEgejAl-1W35A2EifYsy_-CMQC17meJSicJSEsXVftGuTO1-P5trXE66yUnnJF6QXMs7wjDqmRYuDLPLabRSYh4klMtLGTBISX3AZ7shdFfZS-7n0kHIGEfb25vl8f0GELKSXX1Y7a8P1e9cw2UDKQW-5wEF_VSDh4gTBv0DotgMw4wSts-QIY9n_pP4ew6lYIHbhFozf7oyQlJyheeaKGzb64PQq1A5w-XURm6Dag89ux3889XOjlBG7tX5ssOUVVa49wx6F4stoftXE4SmsiaybzdNoyaZI8eGkwESOoKo_yjkz5AN-bUhPkibV_c9PCwAfq76n_oye_ynHXX8UZcS9QVyU5GqSVudPA7naKJaO873FoKlLT207_N7NCdpVtBq9ZIQajX72uCJMRT7grB1-sWy1wJIrAT2Kzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17301f18ad.mp4?token=QULzo3rvzxGgtlWKbr09sAjSPdBNLTTD6v4ZnFO0pB-mF8HJbDAFMF1UVBRtzUIfdobam9wrfnicbWw69Sa9ne42x177tzGSmC5cVhwpisHBfiSUOOJNMRHklUGbL7FUhFewM8f9UTea7YYxWrIZVVwR2YwADLb4ZBaVviEU74dHdhA5HZyOfa0mViNiNFiufRGoxSt82afiYFnhqWJlfy8eqPPnJdmJuhT-Fatqf3-Dpm03dm2AfkLJwwDb-VDd3qa_cEgejAl-1W35A2EifYsy_-CMQC17meJSicJSEsXVftGuTO1-P5trXE66yUnnJF6QXMs7wjDqmRYuDLPLabRSYh4klMtLGTBISX3AZ7shdFfZS-7n0kHIGEfb25vl8f0GELKSXX1Y7a8P1e9cw2UDKQW-5wEF_VSDh4gTBv0DotgMw4wSts-QIY9n_pP4ew6lYIHbhFozf7oyQlJyheeaKGzb64PQq1A5w-XURm6Dag89ux3889XOjlBG7tX5ssOUVVa49wx6F4stoftXE4SmsiaybzdNoyaZI8eGkwESOoKo_yjkz5AN-bUhPkibV_c9PCwAfq76n_oye_ynHXX8UZcS9QVyU5GqSVudPA7naKJaO873FoKlLT207_N7NCdpVtBq9ZIQajX72uCJMRT7grB1-sWy1wJIrAT2Kzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/27a845337c.mp4?token=O8tWHsuNAkwP0etu9mxStGVCAu6gSxy2WxeAO6Eni-6vZLeELb-d5qgdaEdpBuosBezGLEHbdS5k81MZ0tI9BuMBJsOG9W4J5yfg1BFc1BFNTNak-pQymmhhR2pvts7pRz2p6u2xT3pCKngV6WZZRl_H84hBHWdCgj-7D75GoqhN4uMrX9WDwklq_Ng73UT3R8gSw3YL0_GSnJ97yzyC-kCCBMwmNpFWoO4JKtTU5ajKM80eULfXHCiDIZUugzteRCqr_pfdyd2Crmx4RCsqFqpgQCavK_toFtKj6DjwqgUTsZ44CkdrxLe3nck7girGZvwmWkz_KR6UyoUHjadGeQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/27a845337c.mp4?token=O8tWHsuNAkwP0etu9mxStGVCAu6gSxy2WxeAO6Eni-6vZLeELb-d5qgdaEdpBuosBezGLEHbdS5k81MZ0tI9BuMBJsOG9W4J5yfg1BFc1BFNTNak-pQymmhhR2pvts7pRz2p6u2xT3pCKngV6WZZRl_H84hBHWdCgj-7D75GoqhN4uMrX9WDwklq_Ng73UT3R8gSw3YL0_GSnJ97yzyC-kCCBMwmNpFWoO4JKtTU5ajKM80eULfXHCiDIZUugzteRCqr_pfdyd2Crmx4RCsqFqpgQCavK_toFtKj6DjwqgUTsZ44CkdrxLe3nck7girGZvwmWkz_KR6UyoUHjadGeQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
تیم فوتبال جمهوری اسلامی رسما از ادامه رقابت‌های جام جهانی حذف شد!</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/5764" target="_blank">📅 08:26 · 07 Tir 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HaduA_Zw0fovQLIqg_uMcbopOMeJfAVLtZ7M3cl7ura7vMnncKlQyMTAFWrBV4SPBkuHA6Xo1p8ptBBc44EV3g5LXnosU0wzXz8mdlrGg_9YhEYE9DKFXlZ3n2W96GOBiEVjxePsg3FZa1IYySywGq2uJnhioU_gJZRxNcDtd-qPJUG5XzBsMHhj1I8X_DkBmigFuxJgwNobDFvxMpy8kWyz0699sGqgYiN6mRCfRirWQviSM_Cj7ka15Hi5Of-2DRD1W749ayAm-qiG6wRVNuCa8w6rjpTQSREFVtJSRnMaVLTTX-6uMwaOkBVvdWYKlvYc-2G9OyqqN1qFoI_fLA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/0cee64931e.mp4?token=M4lB4JLXoCrTgUWi7_QH_ctNglzJHF4UCrLsHZjQfGGznLYf00LFmi_o5rE8w2tj8zwuZqX-0cx-Ut6WAlRr7Spk0d7ladt8Pz-5Y93WLPBwb2EpgkJvm5DANDIq6_hXLMmqU7-20JZ8jXVJxoShcLF9sK2ZUAoj8PCziJAX6hx4DuosgXJ0uw2rv2FEurj-enwhhgOLxrVqYnurEKogJEM5MmdEH9Fg0FsFQanfP21l4eIbueLVu6KIFovLyrael5W8tZyjMoQs7sO7KdGEgydJH2zzXLgD-SntKeSdztMuPrIDZgE6o5jL0hylWVlMCubiVm6TQItyIWjtdrKXHDsPMb-AzdKmcGxKGqoEW58z88ODTzThoVVheywWzLn5eB7tyfh-SsHKfg_wiDoYn81rj-jasbv9D57rVW_HogiswZBcYGvbIlv7tpiMO-2zlMQI-5kthR2Jc6nmYqpRJI3mxWZ-FWO4f5zU5-7DUMnsRdnaaAezYwG_SahQvsCTTFD8jszxuxHh2vKi_aAwH4w_SjS0irGPLd2-nab97fNVEkrrpG1ei5MwR9cHIZPCVbXu3wpVZWLMRKpI6WUZX04Kf-l9R08-Y_dnjc7egAmxOCfEprY_myEKTcZ0_ABma6EUcM1-yntZW2wZbK8MKnr67GTTEAzSj_YJtp-95xk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0cee64931e.mp4?token=M4lB4JLXoCrTgUWi7_QH_ctNglzJHF4UCrLsHZjQfGGznLYf00LFmi_o5rE8w2tj8zwuZqX-0cx-Ut6WAlRr7Spk0d7ladt8Pz-5Y93WLPBwb2EpgkJvm5DANDIq6_hXLMmqU7-20JZ8jXVJxoShcLF9sK2ZUAoj8PCziJAX6hx4DuosgXJ0uw2rv2FEurj-enwhhgOLxrVqYnurEKogJEM5MmdEH9Fg0FsFQanfP21l4eIbueLVu6KIFovLyrael5W8tZyjMoQs7sO7KdGEgydJH2zzXLgD-SntKeSdztMuPrIDZgE6o5jL0hylWVlMCubiVm6TQItyIWjtdrKXHDsPMb-AzdKmcGxKGqoEW58z88ODTzThoVVheywWzLn5eB7tyfh-SsHKfg_wiDoYn81rj-jasbv9D57rVW_HogiswZBcYGvbIlv7tpiMO-2zlMQI-5kthR2Jc6nmYqpRJI3mxWZ-FWO4f5zU5-7DUMnsRdnaaAezYwG_SahQvsCTTFD8jszxuxHh2vKi_aAwH4w_SjS0irGPLd2-nab97fNVEkrrpG1ei5MwR9cHIZPCVbXu3wpVZWLMRKpI6WUZX04Kf-l9R08-Y_dnjc7egAmxOCfEprY_myEKTcZ0_ABma6EUcM1-yntZW2wZbK8MKnr67GTTEAzSj_YJtp-95xk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جاوید نام ۲ ساله
💔
‏فرزند ایران و جان فدای میهن، جاویدنام علی محمدصادقی، کودک ۲ ساله، روی شانه‌های پدرش بود که با شلیک گلوله جنگی کشته شد.
‏پیکرش را همان شب تا صبح در برف نگه داشتند و روز بعد به خاک سپردند.</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/5758" target="_blank">📅 22:09 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5757">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aHGwxAH9IbVJPhlzOC2DvvppTYUukAm1YH4OkSZVKV4jFo5ljmZurr-mYBz1gHaeXMJyKGN1sDSfhT_2-CHhYGtZZIDB13YkNxc4ikA92s1NQKDwkJySpYaKv_Jtn0yRcVCK9pMEHOKXvV1Wz8QTdMKp_f5am45H5IQIWdNNFJrPyf6z7-DLmPr7cgupIefWhLYScmIdgUNvy06zIMK2g0iFToWIjgCpqLPb8LGuuW-P6UvdlLjwayVE0LSsiy5VAIA6Z7hAGhNslXzPyoH_AeJoLEw8oI5nJY3-nun4QWQAxRaLMldolrbP4QD-A8tY4aHML5yrkvn9TFBOMB5UBw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/db5841aafe.mp4?token=nvpHWrgNZ_nRxLHDs2IUyFbKDGNtYrvDoML7HnQdnNmcWeedrQ5f4a9LDk3ygx8l8qde-7TrliBazk2ojT_3vrxjJXVRa_d0rOEzFRjeph1_kQznOzQGELGmHbTVgLFbLwYVdcUYe4CUeP2Yk0T0CWiEVxOSLeKgk3GA3s1_9At7hmrmub-jXV-5KwQnoPGTPW15ul5JrzIuPeoqf5pAsX3a7y50ztg7Ui2PY-DH2Kb-M142g_623ZMncz3gs3G7ZRaTvRHAEV7CuD8P5pEBzlaTcd2RUY14WS8zIrbJx4ZXWb-LGgPvy0N56UfORa9o7yWIu_Jra-z21hmNxmVzQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db5841aafe.mp4?token=nvpHWrgNZ_nRxLHDs2IUyFbKDGNtYrvDoML7HnQdnNmcWeedrQ5f4a9LDk3ygx8l8qde-7TrliBazk2ojT_3vrxjJXVRa_d0rOEzFRjeph1_kQznOzQGELGmHbTVgLFbLwYVdcUYe4CUeP2Yk0T0CWiEVxOSLeKgk3GA3s1_9At7hmrmub-jXV-5KwQnoPGTPW15ul5JrzIuPeoqf5pAsX3a7y50ztg7Ui2PY-DH2Kb-M142g_623ZMncz3gs3G7ZRaTvRHAEV7CuD8P5pEBzlaTcd2RUY14WS8zIrbJx4ZXWb-LGgPvy0N56UfORa9o7yWIu_Jra-z21hmNxmVzQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">:)</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5754" target="_blank">📅 16:33 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5753">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f038d1dce.mp4?token=kdC5DOm7VSWZbmsLmLSw-au_DF6lSkxcn4gPPlxW0z_wzOvtWuY60ZDANHDJiqstEVscfHCHrM7Svg8hbfC3dGp8UQMmolRWQhocnEeK2nvXdSZwHPSD6R12exM6hGCNBV4rq-zhBacXitSws_6Wt_O4AcskfuhlGU7RViJ9sNlfueL_LEDOwU6N2mjZzXLZV73BUKAF7Ikqr8K_jfjYc3BbA4iwpJDCCne_byhCIqbG4da18yOvR-d-dMGd1Gw5IdsYTM1xHgL3FIj-51hbs2XV7oDNcefhTK_6sXw1aCqjN1ksUz_7mpZecLkumjsIkYGAsqQDhjvu0rCh823cIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f038d1dce.mp4?token=kdC5DOm7VSWZbmsLmLSw-au_DF6lSkxcn4gPPlxW0z_wzOvtWuY60ZDANHDJiqstEVscfHCHrM7Svg8hbfC3dGp8UQMmolRWQhocnEeK2nvXdSZwHPSD6R12exM6hGCNBV4rq-zhBacXitSws_6Wt_O4AcskfuhlGU7RViJ9sNlfueL_LEDOwU6N2mjZzXLZV73BUKAF7Ikqr8K_jfjYc3BbA4iwpJDCCne_byhCIqbG4da18yOvR-d-dMGd1Gw5IdsYTM1xHgL3FIj-51hbs2XV7oDNcefhTK_6sXw1aCqjN1ksUz_7mpZecLkumjsIkYGAsqQDhjvu0rCh823cIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جشن و شادی در غزه
در پی‌ موفقیت تیم فوتبال مصر
در برابر تیم فوتبال جمهوری اسلامی</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/farahmand_alipour/5753" target="_blank">📅 10:20 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5752">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b07e212ab.mp4?token=fEU403kQ08nmmSgJ73WEPNBjgdt4FHlykYkh_wbx1QSwUgE3qIasMrfZZbcwch9n_KhUSMlal5D1bM1c_YFNH4liIgDUQFE0ktNSLqzOogz4LzeKfZ7QeyOhvgkUwg3Zf41lCPIz1bfoo1guVIQ0BDDlwUZgsvCDBu-kFjYEjExislJt5FiLszL1hnt3_JqxNnUcb6B8by-wvWWSiHruLU8lcGbwD2VDp-VRHrNhQ5L7Y_8r9WbbMy1fM-llQ-avh3f3DWvhJ2MECy2jtEqP7s3wU-ZeBZYMCOl4jJchOQ7LwcImoKBwp7-uKD_bpaLYiEmedzMFumPw483NvZSFPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b07e212ab.mp4?token=fEU403kQ08nmmSgJ73WEPNBjgdt4FHlykYkh_wbx1QSwUgE3qIasMrfZZbcwch9n_KhUSMlal5D1bM1c_YFNH4liIgDUQFE0ktNSLqzOogz4LzeKfZ7QeyOhvgkUwg3Zf41lCPIz1bfoo1guVIQ0BDDlwUZgsvCDBu-kFjYEjExislJt5FiLszL1hnt3_JqxNnUcb6B8by-wvWWSiHruLU8lcGbwD2VDp-VRHrNhQ5L7Y_8r9WbbMy1fM-llQ-avh3f3DWvhJ2MECy2jtEqP7s3wU-ZeBZYMCOl4jJchOQ7LwcImoKBwp7-uKD_bpaLYiEmedzMFumPw483NvZSFPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش لبنان برای برخورد با حامیان گروه تروریستی حزب‌الله وارد خیابان‌های بیروت شد.</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/5752" target="_blank">📅 02:02 · 06 Tir 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HZx-0LjmGLp9x1VwNpXK0zrtokmF27CIItV5o9yVfTdl7dBeTzBvlblJO_K_5EMIQoFgBcRCQszri3zmmUOceA-qwCv6dLemTMHzl-oJZXmQIjU-SUo84SQvNb8kkBKp_kv-DhxQfjyrNK16FCqMe-tvuFSjYgGXiywf1ah9Tp6VET1k7Gql3M3JQHri-VJiDpmhhUyMhAN9uur_wbJz-1K55q17VKP7zLD-maju357TR7IWF0NvIYeWvd8fbC3MZt6LZUefxBp-xsBzndpXd1-Z8aqf82XuYwiceXb4sGZbTbkunbg_yd-i-2Clzo7RoVJt9ozLJxmCtn8FkROTjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/farahmand_alipour/5749" target="_blank">📅 01:02 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5748">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UP_tavchRvTgmFfz-mS-3uRB1qMEhXM0yGKWdb9Vw9WFPLVYLVCaxzLkNzUQ3F7h4eAvpwofA5f_Fs0u9n3onHoKUMMGC6DMAdQl5wrZH-GnfCRROZpnuuWv8PUF6iDVwBcN8PBadRxM9Twqb51MzIB65BGHbWYHjYhNXiRAMx0eqc7r_Kzvta4sBZ-_8WOgAUGTJVDWkZDbKZXEAE1aZC0GEqxRUZ5YoouMfXLe6-xKC06ilK_4j5qrielGldOnnj-0gnkuD-Aim6DyolfM9YfKppZ59glIBRicZp4F-BjSSalEIL0f26Wfn9crnLF21PTaUZQtqVGqTSIK5zvUjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش لبنان برای برخورد با حامیان گروه تروریستی حزب‌الله وارد خیابان‌های بیروت شد.</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/5748" target="_blank">📅 00:59 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5745">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e245d71920.mp4?token=gYxSfIA0ykcxPUM26MWj2tCMpoTTUlZMAPlkNY33T6f1ECR098zB3KQtwLVjECgUJAB11YGFsgqChG1JuR_BVphlHWohZ4lqzgeUYXGksDHlsprVugyapASBX-fpZwJC6uz2ezl1cy8NxGTRnoRK_cEFlbit0_GLPk_z7eTjXNJNOGu39KKroOGp83y8pKUXXk5jtSji9E3lW_4xQXqk2WT50Fapk6JgACohQK2xQhi-nfdILXBl1OlOvkhtxwXHywtSkcWC963xxlA3kqoAyuu5qIpmCrhhluXEjfpRtL7oLeft1LQyk-FLOS35Vqp6Phng2goBbGWa727xN6brBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e245d71920.mp4?token=gYxSfIA0ykcxPUM26MWj2tCMpoTTUlZMAPlkNY33T6f1ECR098zB3KQtwLVjECgUJAB11YGFsgqChG1JuR_BVphlHWohZ4lqzgeUYXGksDHlsprVugyapASBX-fpZwJC6uz2ezl1cy8NxGTRnoRK_cEFlbit0_GLPk_z7eTjXNJNOGu39KKroOGp83y8pKUXXk5jtSji9E3lW_4xQXqk2WT50Fapk6JgACohQK2xQhi-nfdILXBl1OlOvkhtxwXHywtSkcWC963xxlA3kqoAyuu5qIpmCrhhluXEjfpRtL7oLeft1LQyk-FLOS35Vqp6Phng2goBbGWa727xN6brBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IPVGDDmyBgF6ojAmD45JFIwLjACtySwrsS2LZIYpBNhXDNjDm9WVbtFQHeHV5nMEgo2vnZLUYTSbaFOMYZLPW9UGHpqPX5NZtQHQCWExNw16X3EehqnYFM0Hg98NMmsgaiRyw5eU2mmN4Mf0iM4H00Wy8rH-ajO4lYOr4hK9I-vYsw0o0ueZSHHBhF5Aok-NtVJDVPSEaC2R8UsjuKC3tqZeZBCZr-K2x61L2Zja4PBYLrbJJ4SGunVS4vTfzhtrLcy0MKOGRGpyw2bhD3P4fzPE840MLgQxdDBnT4VWA5JhDAZPvkgltjC-ojptsF-Q8SQoN6Af3BYQhvi_7V5shQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/5744" target="_blank">📅 00:31 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5743">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PyFafrdIivjLoL3uOQvi0MJkKhvr6j-aXRKIIvK7kWKwLWGUdUqTP3GdHyXwXGK_XFfw6QP9rblLpbA1CwKAiXSjVjMIV8NFU23OVGpz1KVsEUQbJ6qZo2BEJ7enokQ2vBKa-JX2Me12Epuqi5NtsWCnV_HBqg4tH9vHXmN61W1vPUIV2nI7EUJ7s9KBi5cKE3nZYD9X8Atfc1k1hxW-bQmpxpWfyUqoasVP0lYB_yJ9L-oW7i7hPQRK04ZFPehBnkI0ChFo8cnipxu__Ea7aVaq-KpEQ8GtXJ4IvGUberAaAvd_-a06iq_Z1b5KNrMlw2VW-Qc_GkuSvKRERTg4jw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/ac9a1f1d75.mp4?token=uMNX6ANJ72AOaT8PkRJyMmP1VpVHnqYJ9TttoRXZUXIhgCeSCK6dj6mrwAeyMmcXOMYLjOgxPYuJueKLll80u4q21hnAHuYh9tLwpkczqIiGGn6iJgQZvllAJtoqFc1QY3qbkVyQOsoj9Q8TjHjaqrMvh0xW--nskWwXM9KvGO0aNfh7P1WMt2blvdJjbarajLlhMsTAvyc1IORmCr99BygbVo66cNk5iCZ5oiYHN5rOVwrhXCO9oysHmUyG9izcncIpCq0RB40Axb5LfrYyRTP1o1fc6Cynil4ATEbI_H0Koo7G9PosPlLAP55V2uwm73uWVI5txxXrloaJywdz9gJJE5ZjYJZ4_L4Nkzr7BDRql9Ib_gnaSJe8lHerbB1HCMwSTxYGKFuqY0C4lSRYoYSm4Uc0fsGn13rqcq7O0-Ds6ysSw3Y2CJ8vz0VG8oKmjO3INd-pHSd8djgDOT1SDkIjAiaufvfKfTj0ksd-CwPZm8CeeSd8045G9sAEhk5nb5_GzUnNsQ01-HIRbdiyoijV8L2uGBKOUrPo1MnfygYbIaQQGKnwamQcMA7MHwxWADnqEAAuDCvWxE1vn_oYqgjq7ai5RwRQaMsup_3a2t5FLadydND_eY2yYL20nIXpIeSTy6ZUaoO8pGVslYRghbxD2RpJbrGIDu3ZnTuT-SY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac9a1f1d75.mp4?token=uMNX6ANJ72AOaT8PkRJyMmP1VpVHnqYJ9TttoRXZUXIhgCeSCK6dj6mrwAeyMmcXOMYLjOgxPYuJueKLll80u4q21hnAHuYh9tLwpkczqIiGGn6iJgQZvllAJtoqFc1QY3qbkVyQOsoj9Q8TjHjaqrMvh0xW--nskWwXM9KvGO0aNfh7P1WMt2blvdJjbarajLlhMsTAvyc1IORmCr99BygbVo66cNk5iCZ5oiYHN5rOVwrhXCO9oysHmUyG9izcncIpCq0RB40Axb5LfrYyRTP1o1fc6Cynil4ATEbI_H0Koo7G9PosPlLAP55V2uwm73uWVI5txxXrloaJywdz9gJJE5ZjYJZ4_L4Nkzr7BDRql9Ib_gnaSJe8lHerbB1HCMwSTxYGKFuqY0C4lSRYoYSm4Uc0fsGn13rqcq7O0-Ds6ysSw3Y2CJ8vz0VG8oKmjO3INd-pHSd8djgDOT1SDkIjAiaufvfKfTj0ksd-CwPZm8CeeSd8045G9sAEhk5nb5_GzUnNsQ01-HIRbdiyoijV8L2uGBKOUrPo1MnfygYbIaQQGKnwamQcMA7MHwxWADnqEAAuDCvWxE1vn_oYqgjq7ai5RwRQaMsup_3a2t5FLadydND_eY2yYL20nIXpIeSTy6ZUaoO8pGVslYRghbxD2RpJbrGIDu3ZnTuT-SY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اگه خورده گرفتن که چرا میگید سگ هستید …</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/5742" target="_blank">📅 19:53 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5741">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fad365bb7a.mp4?token=ZDr-STvQFPYHiROFw6OPE7okjr7IEHAwGcDfqUYyBg4k0-Dvk9qRQIKcE5xG2aewUJ912dVo_83a_jiYAwUcvSQphHICVJSnFHRCEsILiVyq2xA7qkuZr3bk5_ki9cNSYAuQW9RXOvqhjOSU2zL83IZYkxIZ15AIiPW56JRm1EuZ3RUKct9SeWjS-LFiZfgVlvHezTVkjslzw-S6Ybnjf4E8HQGRf9U2lczcyRXgE_g6QFYzHZV-PLIL5FT8yd0mL40Sp7E4N3lG-LybSPWDd_qpdQBnRXlbNlM4oOGZPr3XikHkTMJCVShwXA1Nnrb6TaFoTfgoL74RMT_P6d5E61-q8E0oWEzvbdPsjmcBXEz8m4htaDJIu9M4xysFhAmxaa4hWFfOt-LJjqwHH-zgaAyrfEAocxsbB4AMF1z6UiToCQLsuxCvMWbcmX-1awoe040KCF8NEnWxY1WbEXOVVWsKj2iquxWxDdQTEfFO-c7L_qLGdEfojvvZHXzHacwzePyY6cWOUoK5AiejvekjCw4lwJgFfOVj2HdhrHtR-Vyf62ke3j1h7TrffvpYy2tFuWf2vpZsr_PK_k7jKqFpS5yPahN_tXlAcM7kNt0fKuvhWabq0jXIF6qKl1D9NU5ZIlOxZ6qxGRQ3V3EXfFFbGsvlYD2H_NY7Ae0l1ocAxVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fad365bb7a.mp4?token=ZDr-STvQFPYHiROFw6OPE7okjr7IEHAwGcDfqUYyBg4k0-Dvk9qRQIKcE5xG2aewUJ912dVo_83a_jiYAwUcvSQphHICVJSnFHRCEsILiVyq2xA7qkuZr3bk5_ki9cNSYAuQW9RXOvqhjOSU2zL83IZYkxIZ15AIiPW56JRm1EuZ3RUKct9SeWjS-LFiZfgVlvHezTVkjslzw-S6Ybnjf4E8HQGRf9U2lczcyRXgE_g6QFYzHZV-PLIL5FT8yd0mL40Sp7E4N3lG-LybSPWDd_qpdQBnRXlbNlM4oOGZPr3XikHkTMJCVShwXA1Nnrb6TaFoTfgoL74RMT_P6d5E61-q8E0oWEzvbdPsjmcBXEz8m4htaDJIu9M4xysFhAmxaa4hWFfOt-LJjqwHH-zgaAyrfEAocxsbB4AMF1z6UiToCQLsuxCvMWbcmX-1awoe040KCF8NEnWxY1WbEXOVVWsKj2iquxWxDdQTEfFO-c7L_qLGdEfojvvZHXzHacwzePyY6cWOUoK5AiejvekjCw4lwJgFfOVj2HdhrHtR-Vyf62ke3j1h7TrffvpYy2tFuWf2vpZsr_PK_k7jKqFpS5yPahN_tXlAcM7kNt0fKuvhWabq0jXIF6qKl1D9NU5ZIlOxZ6qxGRQ3V3EXfFFbGsvlYD2H_NY7Ae0l1ocAxVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/726fb491ae.mp4?token=t6RXDEsdJUNLy3CkcIAuS80wxMBh24eSBu_p78viGUDaMcEeq2reS9VEX-VkoTT0e-PxuS1LtRKfsj9fGfhDQ1oUhoI2qAeLkHATfeCGK2YgoZTj-AMmvxUb786WHB4iQ7W4rqT6ySmZaq7r0nl3icZPllPgnqdXmySq9B1QiB6G3uIKotlgDxZhNa5MivqCAi3LMP4D6VuKKQ5JMsGATi54YrgrH6dNByhPU1Oji0zABd8wmsxaXuLhWvtojlPY86VTAe5oW9lUAtpB5yx52jYBhGMIrkCcKagBtCm0yyoc3EJvYMh2JqEOsXFcJcJPN7KXgkxWgtgxGnaLRf2qZIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/726fb491ae.mp4?token=t6RXDEsdJUNLy3CkcIAuS80wxMBh24eSBu_p78viGUDaMcEeq2reS9VEX-VkoTT0e-PxuS1LtRKfsj9fGfhDQ1oUhoI2qAeLkHATfeCGK2YgoZTj-AMmvxUb786WHB4iQ7W4rqT6ySmZaq7r0nl3icZPllPgnqdXmySq9B1QiB6G3uIKotlgDxZhNa5MivqCAi3LMP4D6VuKKQ5JMsGATi54YrgrH6dNByhPU1Oji0zABd8wmsxaXuLhWvtojlPY86VTAe5oW9lUAtpB5yx52jYBhGMIrkCcKagBtCm0yyoc3EJvYMh2JqEOsXFcJcJPN7KXgkxWgtgxGnaLRf2qZIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قمه زنان امام حسین رو چرا می‌برید بیمارستان؟  بگید خودش شفا بده!</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5739" target="_blank">📅 19:16 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5738">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e184bbb012.mp4?token=dmdEudY3R_nK1KysKnbCeaSuqO3n5TeKjDxDpm2I-PMpdV_OKnsHS2H5tsj8aZFPDRLcft93ljQF67-191VYof3qSnSfuyALg1r_5pLbGmDXZKyulYtCNX3-a-cPAQfXbBvhCXqQliWQXhmNzl51lHx64ELP7BV9wIPxrRZWD3v1sEPMC2SXtBLtH5wDh-YAxqmVUd-ZbJRdg9jPM-CafS0knFSDQbHaO4lAsjJoiy3Khx-kH9WfGnwV48JA-CinRd7dzBg-EmsLhjmGmd-E1pxGsktCQhLIJ9Vzgm1yFu-0rQEF9WJ-CmPjjxydXSQh1t0FFEBh9rbghwHY1KNqQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e184bbb012.mp4?token=dmdEudY3R_nK1KysKnbCeaSuqO3n5TeKjDxDpm2I-PMpdV_OKnsHS2H5tsj8aZFPDRLcft93ljQF67-191VYof3qSnSfuyALg1r_5pLbGmDXZKyulYtCNX3-a-cPAQfXbBvhCXqQliWQXhmNzl51lHx64ELP7BV9wIPxrRZWD3v1sEPMC2SXtBLtH5wDh-YAxqmVUd-ZbJRdg9jPM-CafS0knFSDQbHaO4lAsjJoiy3Khx-kH9WfGnwV48JA-CinRd7dzBg-EmsLhjmGmd-E1pxGsktCQhLIJ9Vzgm1yFu-0rQEF9WJ-CmPjjxydXSQh1t0FFEBh9rbghwHY1KNqQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قمه زنان امام حسین رو چرا می‌برید بیمارستان؟
بگید خودش شفا بده!</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/5738" target="_blank">📅 19:09 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5737">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RTA8sX-NRTmP3U_LpetvUmjmOQJdYwfuh0MKXMW4wxVhCHxizvgfS2N0IH2w4wwyr4h0p2Wv3w-DNckQthBMbdcFOmRmUX7vCS_EBYK8BrHCGK_Qv3O7I_ch5lsgqwT0Ce6M67DjeRBQTNYs9_8istQTbMelnq9OFgzsEAHKdJ_CpdB1TEM60oStxktS-azWVJiLRAKgGU2Qkjy8neyy-jt4AYBESz34dxDWUUMq2kZRT6HvtBBC4cTjZd-ZxQvIw0nabZultAtTVmL7gxMZKT-X737Z2gFQSdeDGd7SaULsGIebiMe8tFVYZMsO69wqD1AnvdpC5aEmZCCnd04ZsA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZTH3atvMnh0YyjRM1G87gOy5PFW_gKfGe0XkdB4ukRhtjl7_j0KbfP7eql2LMnThlIdPULHHoCuu2i9bgEF8WDv2efXKUXkjabEVtRYgPE3ulBCpAMhzjtX1pug_q8ny4sMfANGb3APyTpPM2hO6gypxLDmfusjVIJv7PjkYbMI4KIHT97Gr5ggIbcOCzwD7vwzXd4mxQhignVc9mpexb_UQArVfK9oBCibG4yK6XJHaHv-XtsDCJjQc3IkGG3WKeQouDi6c5bLiKq06X58gP6zYTRA6aoKXPuQXPhqvtpM5GUDkbJJO00CNLallV7x15ZLkri2UXdRwUoLLp0oqdw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/5735" target="_blank">📅 11:38 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5734">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hSLWnk4AAjBkODvH2A1dAy3YCx6xAiPpIyd_PnqpsGg_NRITKkhxCZnH60trBHJkwSRM7jp9Ss8yTAdLMxMmjc2Ug47ZPBfYtcc0T4VtNZshC6CUpVAQujqRBe2bPWZpELg0a6zMg0M9gatSo0Os-WvCRMkcTmGESHW3JQYMi7DyHgk6Ibx8n93UgBAGrMXbGDlvo9782ZhP8vD2BXqs0IF3Pu5BsVMSeoV46D6BJj93jG9P6ykLE8xh_5gux46brs6Tn8rw3DNeLh_Iaxnt9-j_yaxa1QN0UUqQyxPzTaon1qTOVt5RoY2kFFnCh5C40QaBT5aOdTAMMqpKoVcfjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر علوم جمهوری اسلامی  در ترکیه،
خامنه‌ای را از اولاد حسین عنوان کرد.</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/5734" target="_blank">📅 22:29 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5733">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SVkLa7MPHFMLUmV2MUTUUuZaUhNT5pFzDI3pM-T2Mtu99GAaDTgTJa4XBlx2BajKzEdtOgVg2_f9OmxB68T2JI8Emw7r1XopMXQjBwolPDRssoDUkFxV5qKRYXa9mvUWJ6hHNu_lH152GZuyfHje9urLZgVRSv34fQr9faxFTERXxuSXu5BfDMej0ENRrpdFq58pKoKdeCtCzAX0GhX4qZslpSQ6tM4Igs9CuGZ4XfOuR3laIY8FrnZcfoBoIa3jHFR9NtaZGDX9b6gBKO0zI2Q9Wfu93CD5zzKBHdZ2Q3-mJHPFFNjcxTid2BBIJssJx0Z5rjmetu-tA7hWWiODbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسرائیل به یک خودرو در نبطیه در جنوب لبنان حمله کرد و در نتیجه ۳ تن کشته شدند. مشخص نیست سرنشینان خودرو چه افرادی بودند.
صبح امروز هم در جنوب لبنان یک سرباز اسرائیلی در جریان حملات
حزب الله کشته شد.</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/5733" target="_blank">📅 18:23 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5732">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AKCsAkRTMK9PRwhz92SevjGcJhs1vAGgrMjMgA6Klx-sIok5xTDljR2-RjO367OcDvefnaTFcvKjOF1I7CsPcmfPTju5tN5mqv-7NTJIMbFewOMuF5IpBRB9wfzNewMESdXOtdg50H52HwfONXDARDtKkngt6oJ8c9gpzd78DkCYU8-CL5hKluCiE1mY-N_yyRkaIIz3M3lAExqfDrn7YnavRa2nL0AmG5G8fihioTCvVSaOqZYyJLwAj_M64c2-KedmCyazeqNQs5MBrJNCQRTezznGgmCJcxZhdFiuJJskrxEDqPRmbw5tnicXg9XHxf3k1UtUeO_nFNMikjxGIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صد رحمت به اهل کوفه!
لااقل به دینارهای طلا فروختند!</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/5732" target="_blank">📅 15:21 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5731">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIran International ایران اینترنشنال</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6715f87786.mp4?token=tzAq5FhY8ys_Piv48aSnvz1ujpBjD_zvP7txCEuF0Dv0jIDKT9aBpBQG38HwFNJ47gMcHRy9FzPx1o6kTiSrfLth3hQ4RJa3LuXg78bJCIfD40SIDd789NkKN5NjxqLgSf49Q7uutm0ex_E-H046IeG-G6z5PEH-eszAhDxt--oob4eyS2kfbxsME1M8pzeuJ5FuM5NrmInPymLu2bxulUKIkUF67cfupP-6FemcluRWEZswG7Xzp-wE7Mxe1zfTFl37G17-OKiWrfu_-RZTvi6WuDZreCfC12eoA5qA8s_XYLtv5TwB2a7HdslFnk9zPn4q2--c3T6jb-tH2WO8jg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6715f87786.mp4?token=tzAq5FhY8ys_Piv48aSnvz1ujpBjD_zvP7txCEuF0Dv0jIDKT9aBpBQG38HwFNJ47gMcHRy9FzPx1o6kTiSrfLth3hQ4RJa3LuXg78bJCIfD40SIDd789NkKN5NjxqLgSf49Q7uutm0ex_E-H046IeG-G6z5PEH-eszAhDxt--oob4eyS2kfbxsME1M8pzeuJ5FuM5NrmInPymLu2bxulUKIkUF67cfupP-6FemcluRWEZswG7Xzp-wE7Mxe1zfTFl37G17-OKiWrfu_-RZTvi6WuDZreCfC12eoA5qA8s_XYLtv5TwB2a7HdslFnk9zPn4q2--c3T6jb-tH2WO8jg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیوی ارسالی به ایران اینترنشنال نشان می‌دهد که صبح چهارم تیرماه در همایونشهر اصفهان پرچمی با نام‌ها و چهره‌های جاویدنامان انقلاب ملی ایرانیان برافراشته شد. بر اساس روایت رسیده، این اقدام «بدون ترس و با قدرت» در جریان مراسم مذهبی «عاشورا» انجام گرفت.</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5731" target="_blank">📅 15:20 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5730">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/afaf9624af.mp4?token=IA6ZVFatXwn7aaCHdmCBGlOdy-PagJkVD4nrtEJKotepSjmdwvnECQW4t6YBX3HRQMBtYI8AH_qvkpnrQkEiIs-tfpPAWtbOz25OAxb9ujpPu6qIYbcwZQb9fqynR8S4YJzl3Qv9TEO1zCVM_ei8ZybnXIK10SkqzfmpxehUw79v_D6i6euF-usFi51yfeqlgX96G7UYbtFY9TEQX9rhlBZxQ9WGsAq-wWfJIhTkAD_KMnlJRgf_XVT2FpATXoVA9TVVnH-TgXllGQEx3OMJkTQ0RIlhdn31cdqu7A9xYymFenUqZhZ9ajJFHy-mLg10oGcbVoI4fgWb8nyVPZ_a3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/afaf9624af.mp4?token=IA6ZVFatXwn7aaCHdmCBGlOdy-PagJkVD4nrtEJKotepSjmdwvnECQW4t6YBX3HRQMBtYI8AH_qvkpnrQkEiIs-tfpPAWtbOz25OAxb9ujpPu6qIYbcwZQb9fqynR8S4YJzl3Qv9TEO1zCVM_ei8ZybnXIK10SkqzfmpxehUw79v_D6i6euF-usFi51yfeqlgX96G7UYbtFY9TEQX9rhlBZxQ9WGsAq-wWfJIhTkAD_KMnlJRgf_XVT2FpATXoVA9TVVnH-TgXllGQEx3OMJkTQ0RIlhdn31cdqu7A9xYymFenUqZhZ9ajJFHy-mLg10oGcbVoI4fgWb8nyVPZ_a3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R5SKJjX13pQMV97aK_N6L09yzAcaqHrqZQr-F0_Y6VGFWPoiS45i1ho4Zpf6pxZd_g_piAj8gVJ2-0jnUNbc_3n9V7EXsrCIt1JhdMQ9actzlfZfEmd4yMO2uuM7asnjuT2R8Tegm619be1RmZ5K_-vC6wPhd9WJ-TaFItMLmuqYiV0vC7xkp4wsg_5TX2s4btBEBA68LDSVNodidPa_9FvwJidXit-8MxSeLEsutEeDCkkS3hjS8vG9z9jxIupcBfYpPjSSUiIJFGXkAT9sH4DYrwOZqYUABWw5S35ySQfgHI1d8GJe7CxAQuGfqLYCME7j9L8gU0JUu-mkid7kGA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HSAtcQMT5KbVDcXgnfYNg7FfI_YiCe5e4mKHRCVwECh_EsGfZ08_Y0mUVw61BVJZ5i4QbpmgHO1L6NrmbnxKpJYAQEr8Hzd9FqZ9biScnQXL9ipLBlq8DKztUbFutQKZ8cA_g4VcZlbnv0Z1eHGrwpcPQbMUTGIyf4cQwRjVPL2W9uwVPo0CTVIKGlUKBM1uDAGlIRu1q9bXcraq4CFpYpRtkJmKxb5V9GBTiQT55lByXjSF1ctJ9NwVbz8ilGuhR0wd6dZEcuZHRbAKGIXNE2UznJErZrU_a8PJyDnjINaDRQJvrW4UjneywHD6dYobMvrAG7CwNjA1OgL3-697Dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرمانده گروه هکری «حنظله» که در جنگ ۴۰ روزه کشته شد، ولی خبرش الان منتشر شده.</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/5726" target="_blank">📅 09:39 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5725">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/86c17f6d3c.mp4?token=rUZfOV_93Qag3AgiFd8fxjrSr50DJPojSBBRZwFNJ_WZALIt4CeKctqyUare8_BiKEVmKi-C9xw8FqmKO8Ub-yjltUfvIFJ8WMX73tExdowKLjHU0jV_AzuOAZWLy_H5WRTJ5p4sEH2NAYDMIZ8MqHIrzRpC2hw205a2DTYsnfDqghlKAiV6lKuZ7jg8CbxjITyeXYsPpXoGU4MYjaqpEX8LSdQLXXWJT6gdLQ2JZqOOrPE1u6EftAhEZWImW1J--yzWDEngocRIuOHM_zIFIheEsUHB6eI-zV540DxqVpA-sY1aELpZWiaIPyAeXZjxrUAiOvaayQSp1X712NfOhg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/86c17f6d3c.mp4?token=rUZfOV_93Qag3AgiFd8fxjrSr50DJPojSBBRZwFNJ_WZALIt4CeKctqyUare8_BiKEVmKi-C9xw8FqmKO8Ub-yjltUfvIFJ8WMX73tExdowKLjHU0jV_AzuOAZWLy_H5WRTJ5p4sEH2NAYDMIZ8MqHIrzRpC2hw205a2DTYsnfDqghlKAiV6lKuZ7jg8CbxjITyeXYsPpXoGU4MYjaqpEX8LSdQLXXWJT6gdLQ2JZqOOrPE1u6EftAhEZWImW1J--yzWDEngocRIuOHM_zIFIheEsUHB6eI-zV540DxqVpA-sY1aELpZWiaIPyAeXZjxrUAiOvaayQSp1X712NfOhg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/171eba79df.mp4?token=pzUS4wbbRyvYwfbn-at9A0QFVS2GkccFEqxJ9MYDXtgzcWje7wz839Qvcjs8lrLHKe6lUwk7Yw3XJZgJfdJMWUHuv6MEdgAafGgsYNXsBjqYvXoC53k-D3wVMtJ4dOkF23CQp1agrDVZODXBMTWVWL3tir9kjhmuAqyNr0JJC6Hsdq9qyFjvQ6GU8fOWPLebIS2q02tKADI_4kqo4o1fcWM8uA-1fbXR4t_MusNCCzkSLtN4X76RCGbhs7prUtzytFr2o2EJphFNhyMhlJERibSBz3DFDCm0mgSjhWNKK2kIQuk2SihdzVx6KeJia8JuPWrNImRtFNt1_B0lMD27lg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/171eba79df.mp4?token=pzUS4wbbRyvYwfbn-at9A0QFVS2GkccFEqxJ9MYDXtgzcWje7wz839Qvcjs8lrLHKe6lUwk7Yw3XJZgJfdJMWUHuv6MEdgAafGgsYNXsBjqYvXoC53k-D3wVMtJ4dOkF23CQp1agrDVZODXBMTWVWL3tir9kjhmuAqyNr0JJC6Hsdq9qyFjvQ6GU8fOWPLebIS2q02tKADI_4kqo4o1fcWM8uA-1fbXR4t_MusNCCzkSLtN4X76RCGbhs7prUtzytFr2o2EJphFNhyMhlJERibSBz3DFDCm0mgSjhWNKK2kIQuk2SihdzVx6KeJia8JuPWrNImRtFNt1_B0lMD27lg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قمه زنی گروه بزرگی از شیعیان در کربلا</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/5723" target="_blank">📅 21:46 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5721">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GBT1g5E3bO-VesaJYGlSFtlFFI_FR0E1IbaP1DRNTAxvMNji14noyTI0GHYUGHy7L6EV4_lVoJmRVX0VgfG93g0mVwWdK_Yev-5eFMEC791j1vv_k9jpgu3SfRLThSQuidMGaYmHH-xl67mgk9bRFjY8go67UrHuZv2yA0tSSG_dgl2o1I6KynIvIbIXCzXnQzzSLxKnYcHCZ8WwojpRfyTkK6Nnj7CplgOtAi-QPJcvESPh41GrQPPwz5m1kEjahNcx0YJ3RZbwpXCrkMosnbCj9UpFQmRCgiiAKFl2BIsc-NjJ_j22jIjvs1tTz1conP93qw1gCmNJk3u_8iC7Dg.jpg" alt="photo" loading="lazy"/></div>
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
