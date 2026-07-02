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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-11 21:52:34</div>
<hr>

<div class="tg-post" id="msg-5838">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pFR9mP27XuuGctu-j9UIthXRXcR2HkauBcp1vLGDZucKGnJvm6eCgYqeLOvCJYxlxP_FsBBPQArNZnG5bWZDEwg8-oRrf-Vs395QhuFLe4n0xgtcckZPJNY5zaXOh57Dn2kPUElOb_GIltlAf_xxkne8VsmO5yH0tHkbhceyuXQVw48OkPF6o13-oWWgXwHuGqHV_kMRmdG_2cieuC8UaZz-wOvzGoDrem8KfCz2jRHSP2VrOUFiX6qglWYIWeM0Iu44DJe1d3irDKrX5zLqC4gT-lw5sJi9TyfIXlCj8YcxMBdPEm4W35CEv8IZAj0QYitzECSm04Z6x6YqyGioJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بارها نوشته بودم بستن تنگه هرمز
علیه خودتون میشه و میشه تنگه احدتون!</div>
<div class="tg-footer">👁️ 7.13K · <a href="https://t.me/farahmand_alipour/5838" target="_blank">📅 19:51 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5837">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sYSlidjSFGizuNxf7akejcFa-W0V3nxfwB2eUuasb1PzDVKm0REuO1QswdLgrZ4WyJV93uCy9_BZpeXJ-KEUYHDlX1b-9z7fZsAG2ydDh8z4RuMEgvzHWtqlhFOA9VrxDnu_5UYxLANrAAMNGawKNtqU4TjMISXHHNav543K7N4L01Y_MaezrDdVVXcZRU2YQtIddfM9WrdazZWIOSQCCqda5ucIkrYtJolCCDPEoYH7b0kMEvRE_7G6_4OxaMWA1ga4wICJlt4ERIUinY75EczzXSj5N7NNnHfwjJue1jvnSR05_ZdA28_T9idA13qdvgyflc3HR_lQKUVqdP-x2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روسیه، چین و هند حتی حاضر نشدند «وزیر خارجه» شون رو هم بفرستن برای مراسم ولی‌امر مسلمین.</div>
<div class="tg-footer">👁️ 7.31K · <a href="https://t.me/farahmand_alipour/5837" target="_blank">📅 19:45 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5836">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lxbQzXGl1WrvlN9I1lmnND2NVF945lmXSD8zphNG79RXXIsZ82X5Iugs0692acWqBXfB6u7Rj82YgnNyijd1KQ2hAhhc5wZANS_qyBB9d_2iTpz9tmQD0gAXQcsCP3WY8Z1xloET6OosZziCYCUgQH93Jxz4q_5YzWzrZfB5UVjMMiBjkHPDraHMngf-3mtEYLQ3MP8Ysajo2BR1KqfaA00qokDrdaLRwRyACaELmwVUpmXg0e3zBG7E5AvDzKftNByph9k6dD4NbNlKM6ABkE9XD4ccs0vXxocoD0zsWzrH2d-MReZQ66Yrf00Yv9v1UNLKuuNWZcHQVcnpV_B3jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روسیه، چین و هند
حتی حاضر نشدند «وزیر خارجه» شون
رو هم بفرستن برای مراسم ولی‌امر مسلمین.</div>
<div class="tg-footer">👁️ 7.43K · <a href="https://t.me/farahmand_alipour/5836" target="_blank">📅 19:41 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5835">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iJRkbhs9IbWoRZovuIbAdCL8RXSrfv_LsUrHECXlOyAb2uyCnEEv9ImGnUkRyGmvAC06Z2YVpGx7izQ-p_b2WD9xm-bTyR5IzbJa30aWfPj3lmO4UruESejP3oMsOJpBG7NLchPSl77nDA5NmHdAG5jEjqbm4o8iZQyOB8lfip-ciniSz7YpCk9ZbLMGfjSmj_rW69BB-5xaFhnYeIyVHfGFt8KxkjcULSzASE3rL-HTEk3EI1vda8CAZRClwHoNtnY5UOogMYIUFLiFLHvjQw7AKDT1iD_I28FYmfPpNWm07UmLfMN-GmjQr4YYQyUOtDqs0B-TrusDlkbR-DeOtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/farahmandalipur/status/2072405978012844407?s=46</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farahmand_alipour/5835" target="_blank">📅 14:35 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5834">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YYpS2AGyOFJVNJHDIntWcTTBzu3PdjdY18dppzEwL1jCxfGZv6syisx77E5hiMHQEPYnJtUTSN9gZXYvTd177TsveVJqvA0LGWivRTQChf1q5mzc4OG542pY63Y5_CSOZgNYufdzZz-B3Yd_U8TlsXDG9NEsdRvjAQnl97Cgtu2iWJI-GYu-Fbcn96_Ol_EWdmmJwESqGPryWonkVcZphsPFW_ju0RB1ZI5L3FWhEzAHL0zhw5psoQPDc1xzjYkbeyqPUNtH2cw3TGnubrI2qyZJVsAmo5TIr4H1iisaf-1ECwLlTi1o6uFduvMAV5l3KqysaEt2kONB3pF3l_-EKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چرا صفویه به این کتاب «روضه الشهدا» اینقدر بها داد؟؟  ایران کشوری است که عمدتا در جغرافیای گرم و خشک واقع شده،  قحطی‌ها بسیار زیاد بود، فقر گسترده بود، جنگ و ناامنی بسیار! صفویه با گسترش شدید مناسک‌هایی مثل سوگواری  برای محرم و قمه‌زنی و گریه‌های شدید و…..…</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/farahmand_alipour/5834" target="_blank">📅 10:48 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5833">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B-6p8jGj_erqIzymuNNH7CqkXx7WFj5Q67dTmM0GBCBTeKO2JR06nEfkRn9O--Fj-ljU-O-lSSsZBWprk3mezHBDePIVi6ZjUF3FZURIId_wEl9OlAYkOpwlELJFhxj4DgcLBTxFZrFoOlFTdV4VSGqmuYJ0tj1Wx54wQ-ALKBxgXghOtmRcN-gvflFwaXBQRoihdZHMEZEEmZVsOiI8TqnmgyXs_L89XSsfht6uupp8xnV-1Iw5xVqdMeBTBmYb6za4XWJr5VUiSDnX9nfo4nHs82iiRl17m8SqKxXsUqbeAqTY3PETy5hS2adcg-GXXnROgf4GmPAdS_AWJqIHtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خود خامنه‌ای هم در اسفند ۸۴  یک سخنرانی در جمع روحانیون در آستانه محرم داشته و گفته که باید روی  «گریه» و «احساسات» و «عواطف» کار کرد!  و امر میکنه به «گریاندن»!  چون روی همین احساساته که به قول خامنه‌ای فضایی ایجاد میشه که بتوان خیلی از سیاست‌ها رو پیش برد!…</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farahmand_alipour/5833" target="_blank">📅 10:42 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5831">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VZKiyY-aTp0qDEKrp6Yrrqa54CWEEkg5V7dIZrjj1SRcHW-wGLJ9xc9Nz3dP3nVQw9r3RH68-cRAaIg-ffBOPlUwaftTKPrTf0r3o5KurJrpTOCc4LOBslM5TKEz7XbKDZJv1FeI4oaTTf5JfLNDGtQ-XjMI5g7VmBjOsI37QepOpewMYYgfwIz6HdwIasc8nyqHBHrypuSS7IbalJdUWBwmI2Dd18MMGr5Vvb1q6k_SsGw5-wGuEXJT0OA131dZ1haGl7dyMrFf-eh37JwXLCOEE-ddBazRIvzf99d0X0D3ims1q_VAJDVh7SMPfrmr5xJmXe9DDHHhaivLJNYdIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KJyICSScG8w5gh4zHFUwgeBMPU78Ocf3sPu_Oy7a8kmg8xJq_CVlElx0QDixCzfbNFcCHHRKMJeWxK7-Ptinzu0Z2PRp4NxiOhZj_BSQT3nrRxm3BmiD2Vj8liPfNH8SrTExP_t-muWmu05ULgg2aoXohpu69PLaN7x0A6Katy8_aaiEEVtoMMksasWxOp42smVKf23pScPC9Nj_jUr8veXI3ed010P1PZcn-4oahzw_A6PVdXi3bhiKbx-vvqpWhrQer58M_uV21OI99eedtM3x_Qwz-6mVoF3hSep2OWpM31ovvP33L3NPhPcNTgvZj83-vsb62VPnGxtpWbCgiA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">نکته دیگه اینکه خود صفویان،  از فرقه صوفیان خانقاه اردبیل بودن که در این فرقه یک «مرشد» داشتند که قزلباش‌ها، باید با «شور و احساسات بالا»  نسبت به مرشد حرف شنوی داشته باشن و اطاعت و‌ پیروی می‌کردن!   این کتاب «روضه الشهدا» برای صفویه خیلی خوب بود، چون شور…</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/farahmand_alipour/5831" target="_blank">📅 10:38 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5830">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EtohJesNZbSJmgFGg6BfdC2n4_8K8nNkEX_hgtwNsihYrqRbio9pkVAiC5zX-fNZJB6hC2vrooeuXqAFd9L8M8qt3mimgp-llY3SKQ_gUNOySYYAFEIcAyIqRp5zOkurtHiCnzLrq7erwAb41Kd_v-kyLSXTalerTCZ8lTyNEYuIkYTt6Nv_LOKZu8S_PV8KD6WUspY3yTLdP0gMx48LVXAGs1R-yRX3hnlN4Ey1Pi17aGlfGpCV8DHAW1fhGVXWvL4yhm_s-q9Bo022yCFvmJQAUvNNUw7yB-5rdVxHucLu5WcSQ6HW2XUlQGr0YHsT-CU8DZ4Jqws2Mkggb_pSvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چرا صفویه به این کتاب «روضه الشهدا» اینقدر بها داد؟؟  ایران کشوری است که عمدتا در جغرافیای گرم و خشک واقع شده،  قحطی‌ها بسیار زیاد بود، فقر گسترده بود، جنگ و ناامنی بسیار! صفویه با گسترش شدید مناسک‌هایی مثل سوگواری  برای محرم و قمه‌زنی و گریه‌های شدید و…..…</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/farahmand_alipour/5830" target="_blank">📅 10:17 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5829">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CNTYxJ77ojeY7zQleopB_UcHLTvcFvN1qfGY2PASFcLVRp3SWs8BdFg4uEIH4F0s0x62vRuQq-TP68L1HvP15RPtIE07aWBI0w2gVXUiZG6CZCorqqIYkviaXKLkaQPU1cjKwL6ipRgexiYl5u2RmKLIRKePqAJN1s0Lc6G9mFzqCw_TE6yMFmqshVj0oub7iVMUGYt7hvFvoYazDI8t89eCdzc1k2hTzp6qy4U257xUNnqofz5pmmmLGUw8YGc_ZkMbSwg2TTMv31ctymPn_HAniifMH-keA-WqYf6Lpm_7Sdwzvs11bnDKjP9YVvczXNVLhH1M_dx7FF9xpsbOGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای با الگو گرفتن از صفویه و با پول نفت.  این خرافات رو تشدید هم کرد!  به «مداحی» و «مداحان» پر و بال داد!  بودجه‌های سنگین! تبلیغات گسترده از طریق رسانه‌ها از جمله صدا و سیما،  که این‌ مداحان با خوندن همین دروغ‌ها! احساسات رو به نفع حکومت مصادره کنن!…</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/farahmand_alipour/5829" target="_blank">📅 10:06 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5828">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QfvVUcn0nncvG0HoZzOuLrTxwkAP-ZoM3mdCktSzHWlwyiI00K6qwEpvDhrq6E-ejROreuxedUXZYNl-3Q_7-ChSUyb9rRsdxmgtV2hr9bEnPjw1kCdYufWBKc14DerjipadA1PgSzwAf3AQBhQoq_0EOCBAkCaIQ74LEmKFaMSiW9KapYXbGx6RI5vqSML1eEgBnTr5SB5Wnc8YYqed4PU9CSev6SCLyu0ztjxOW6aX9ouXRisxhx3YLZxkcZ1QnFNiDV6DcihXbCWrkc3SIcjUModRWVoTEqMqUQ8rgt7eNFv4AzjqW9GFcoXMUGT_uEF4jaWJTbVddu7AP1x_Ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مرتضی مطهری در یک سخنرانی عمومی  کل این کتاب و داستان‌هاش رو «دروغ»  و افسانه خوند!  گفته از خودش نوشته شده!  کتابی که داستان‌هاش صدها ساله در ایران خونده میشه و براش گریه میکنن!!  کتابی که حکومت خرافه‌پرور صفوی عامدانه ترویجش کرد بین ایرانیان!  مرتضی مطهری…</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/farahmand_alipour/5828" target="_blank">📅 09:56 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5827">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">در زمان صفویه کتابی منتشر شد  به نام «روضه الشهدا»  توسط «حسین واعظ کاشفی»  این کتاب عملا مبدا روضه خوانی  و ذکر مصیبت در ایران شد.  و اصطلاح «روضه» ، که امروزه برای ذکر مصیبت و گریه به کار میره (در حالی که اصل معنای واژه، به معنای بهشته)  برگرفته از همین…</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/farahmand_alipour/5827" target="_blank">📅 09:41 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5826">
<div class="tg-post-header">📌 پیام #89</div>
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
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/farahmand_alipour/5826" target="_blank">📅 09:33 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5825">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e54b01c817.mp4?token=EUkl6ZftdcjVAYUPk6zo5BlTUuUNZpkql8lv7lyL9vWuDHjgo36BUoBkJ8n0vF7G5iGemZO1xOfcUtFEKpE66PqNEgkAUjunbg27Uhpmitk-ExQKrRdqwkL4H6SNkiauzYUMcyAoZ5msdi7khcZFGagbww0PBPQQpmGwJbmZdOZcJ1A5DRBGzK9DeYKUbtQCxU4u2l5tSO-NBBqdYJFW6OhHUxrvyPKhrC-YNfSXTqO7ljHjRSgwjv3nEEaI4Nqoj_RYZbwfQOgMsMqk1k3Ik2elJliisby7wE6yXRsSORGgsptp6qow6MQ75h7smGXS4ZU66sdglxdNZ_A7VbIv5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e54b01c817.mp4?token=EUkl6ZftdcjVAYUPk6zo5BlTUuUNZpkql8lv7lyL9vWuDHjgo36BUoBkJ8n0vF7G5iGemZO1xOfcUtFEKpE66PqNEgkAUjunbg27Uhpmitk-ExQKrRdqwkL4H6SNkiauzYUMcyAoZ5msdi7khcZFGagbww0PBPQQpmGwJbmZdOZcJ1A5DRBGzK9DeYKUbtQCxU4u2l5tSO-NBBqdYJFW6OhHUxrvyPKhrC-YNfSXTqO7ljHjRSgwjv3nEEaI4Nqoj_RYZbwfQOgMsMqk1k3Ik2elJliisby7wE6yXRsSORGgsptp6qow6MQ75h7smGXS4ZU66sdglxdNZ_A7VbIv5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">روضه خوانی سحر امامی در شبکه خبر</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/farahmand_alipour/5825" target="_blank">📅 09:09 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5824">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/43703b5179.mp4?token=nJIojmQXwvhDlyNAcV0qRwjUwwNjXVCQfVBg6AKqn1IQogoaHs5iIn5Z4Z5UoOo1nTfcW6R0ZPdu0BRGFcWyrwSuqzrKqc-8_bnWaFLbXtBADrW-26qv35K2X0eDkWQPTLAq_B_YRFXiBNYZefnXX6-K2uBY3hk9xqImUxULcDPOoCBv8yuzevVU95BHkPveR1EIjNk9sSizqBvcWnqtS9wb_3wPtLKYgpUU0tFd8YCXlqmMS2ETBjALrYzJKU2mQEV_GFDW-rocRAdmsFL139ruNi9T5RDphFA3SKFkczRCC0JaEmRXrB2txaNRZKAUpKxpINqvjvG2LqGjAO3Q-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/43703b5179.mp4?token=nJIojmQXwvhDlyNAcV0qRwjUwwNjXVCQfVBg6AKqn1IQogoaHs5iIn5Z4Z5UoOo1nTfcW6R0ZPdu0BRGFcWyrwSuqzrKqc-8_bnWaFLbXtBADrW-26qv35K2X0eDkWQPTLAq_B_YRFXiBNYZefnXX6-K2uBY3hk9xqImUxULcDPOoCBv8yuzevVU95BHkPveR1EIjNk9sSizqBvcWnqtS9wb_3wPtLKYgpUU0tFd8YCXlqmMS2ETBjALrYzJKU2mQEV_GFDW-rocRAdmsFL139ruNi9T5RDphFA3SKFkczRCC0JaEmRXrB2txaNRZKAUpKxpINqvjvG2LqGjAO3Q-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/farahmand_alipour/5824" target="_blank">📅 08:27 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5823">
<div class="tg-post-header">📌 پیام #86</div>
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
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/farahmand_alipour/5823" target="_blank">📅 22:52 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5822">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad33cb95d6.mp4?token=TG-HwvHnlVrhX6yqgcI_lvaVzXAA2MxldVOO3WSTLTPb0RJerPnlE7fRW1loAtHeqTi3Q4KI-hMOqRF-vlC5es3kAuOx45X_2RgnXcxhN4b4jImFw2-dtK4eUrCTNsLHtcZBmYWAsSd5vchn3_wn68ILLbIwnIMt1x_WyVuehmuAjwN8JJ3YK3JX58VmSP72P8OoVUiqe40yG1qDD7XOoL2HR2MYRopnv8TZEtXAiNgbZgtD84VHsZLbG_E50j9aNFuQsizme3e3LDHh7pHPCAliLUZIdXSKM9vR0mXqiyARA4Y9WrWFffSg9VPZntb9yyOtVyuBkZEGS5MRrkjZWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad33cb95d6.mp4?token=TG-HwvHnlVrhX6yqgcI_lvaVzXAA2MxldVOO3WSTLTPb0RJerPnlE7fRW1loAtHeqTi3Q4KI-hMOqRF-vlC5es3kAuOx45X_2RgnXcxhN4b4jImFw2-dtK4eUrCTNsLHtcZBmYWAsSd5vchn3_wn68ILLbIwnIMt1x_WyVuehmuAjwN8JJ3YK3JX58VmSP72P8OoVUiqe40yG1qDD7XOoL2HR2MYRopnv8TZEtXAiNgbZgtD84VHsZLbG_E50j9aNFuQsizme3e3LDHh7pHPCAliLUZIdXSKM9vR0mXqiyARA4Y9WrWFffSg9VPZntb9yyOtVyuBkZEGS5MRrkjZWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حرف راست رو از این خانم بشنوید که میگه بعد از انتشار خبر کشته شدن خامنه‌ای مردم در‌کوچه و خیابان‌های تهران کل میکشیدن و‌ دست می‌زدن.</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/farahmand_alipour/5822" target="_blank">📅 21:52 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5821">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a22e78d39b.mp4?token=p4D0fddbrxN5ygxU-ME0-YppT_OWtQvfvyIR05SxcVOvGx7h6Jg4g7NT8DyLeHEM_D9ekSqBDq_18jMa4uiRcMf51Mm0MkpfFNqSya2T15J5CnawGC3Fd3x5RSz00OBX-S2ts0rS-inV9ZVKbYgBsjADRK7JcI1jGwN6KbQbARZ31skvhyRclr8FK11Q8VZ1soYXRCJPcqmdEnYSLD9zg7Gbh3bVh3XJ6EPMAi1xoilXAIgmd6QPxqzLQ5J8jU0WYAy4Tznwlu4rME50tHyRca7XG8a8uEJGnu77y7g9S3lHBDq7qHy5Ab7eBnIpQBCNVxE3JgLm9m-Lv2T0RGEnkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a22e78d39b.mp4?token=p4D0fddbrxN5ygxU-ME0-YppT_OWtQvfvyIR05SxcVOvGx7h6Jg4g7NT8DyLeHEM_D9ekSqBDq_18jMa4uiRcMf51Mm0MkpfFNqSya2T15J5CnawGC3Fd3x5RSz00OBX-S2ts0rS-inV9ZVKbYgBsjADRK7JcI1jGwN6KbQbARZ31skvhyRclr8FK11Q8VZ1soYXRCJPcqmdEnYSLD9zg7Gbh3bVh3XJ6EPMAi1xoilXAIgmd6QPxqzLQ5J8jU0WYAy4Tznwlu4rME50tHyRca7XG8a8uEJGnu77y7g9S3lHBDq7qHy5Ab7eBnIpQBCNVxE3JgLm9m-Lv2T0RGEnkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">میگه خامنه‌ای وقتی کشته شد امتش ریختن توی خیابون بر سر و صورت میزدن  ولی دروغ میگه :)</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/farahmand_alipour/5821" target="_blank">📅 21:52 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5820">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/256cc521e9.mp4?token=dwxprBU3C2Iib9lj9TGidlLI62c3QwLZxO7JUNHDTbcUPX7uA8IVRU1EaSAd1HzEW8-_X6WQhhn3PPuNGOvvl32Csrof25bn0w8FjO-EJy7uxUfuJzuuIBYpZiFRykr4NvQnmCzfd8GMQd9Tvk7EEYD81C99S9sn5VroE1B6uvGwo7nNc52tuZQ5Zo3wcNZEA3knIdGwmHdLRiFWJOiRcJcXg_EJlxOs605LRv4k6fItde5gagu201KtbtFgWF5cmvlgpbnGcDk5pFKZWFd7Cn3lLA6fMAoPdAuKCmyjDDFH0zIi6fVDXkGPFsMRmuBPbyHCdXPnQhpDEsIIJc2V1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/256cc521e9.mp4?token=dwxprBU3C2Iib9lj9TGidlLI62c3QwLZxO7JUNHDTbcUPX7uA8IVRU1EaSAd1HzEW8-_X6WQhhn3PPuNGOvvl32Csrof25bn0w8FjO-EJy7uxUfuJzuuIBYpZiFRykr4NvQnmCzfd8GMQd9Tvk7EEYD81C99S9sn5VroE1B6uvGwo7nNc52tuZQ5Zo3wcNZEA3knIdGwmHdLRiFWJOiRcJcXg_EJlxOs605LRv4k6fItde5gagu201KtbtFgWF5cmvlgpbnGcDk5pFKZWFd7Cn3lLA6fMAoPdAuKCmyjDDFH0zIi6fVDXkGPFsMRmuBPbyHCdXPnQhpDEsIIJc2V1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">میگه خامنه‌ای وقتی کشته شد امتش ریختن توی خیابون بر سر و صورت میزدن
ولی دروغ میگه :)</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/farahmand_alipour/5820" target="_blank">📅 21:50 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5819">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ed6be978db.mp4?token=RQ_jY_0qKgdfRnmMiIvRp5XJPhIQGYcCUrJxWx4BFtwPBbR3YESLC9GuMNzw2RLT-LitFye5rvBt7YFb5ZZE8lYVcz7TLuoeW2MJIjFPJPK8KMblmfzHG2NnPnMeW5kuSGDpPkWPNCMXqew9R1_vgjNi8U-XhkC1HZ-XfRTUISpbnSlVw3hptMuqW3Ilk-v7TRMZd2w8q7xNcV4xZj3Lk3NcRwWfENWxiCqdzFXoffD41z_7h_alminNnklbwABbmIcYiTF1t_4WIlo_LtizmvXefXszZY2jX6gHA5DeWi4JKpv3NZaiPM35DXGjHZ8j2GgKhK3heVoeXlFBTh7Mug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ed6be978db.mp4?token=RQ_jY_0qKgdfRnmMiIvRp5XJPhIQGYcCUrJxWx4BFtwPBbR3YESLC9GuMNzw2RLT-LitFye5rvBt7YFb5ZZE8lYVcz7TLuoeW2MJIjFPJPK8KMblmfzHG2NnPnMeW5kuSGDpPkWPNCMXqew9R1_vgjNi8U-XhkC1HZ-XfRTUISpbnSlVw3hptMuqW3Ilk-v7TRMZd2w8q7xNcV4xZj3Lk3NcRwWfENWxiCqdzFXoffD41z_7h_alminNnklbwABbmIcYiTF1t_4WIlo_LtizmvXefXszZY2jX6gHA5DeWi4JKpv3NZaiPM35DXGjHZ8j2GgKhK3heVoeXlFBTh7Mug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به امید شکست و تحقیر یک به یکتون!</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/farahmand_alipour/5819" target="_blank">📅 20:05 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5818">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nobOoYOFwfs8IBfABfQoDTpZW11TVnPpIPEy3z8jlBMKpR7LV_wDEUA3YK-0rz6zsPjP3JdMnZWNRvHfvoXjYm5KnWEnKN3w2vfGw7GsaLIVCe8tIdjBe7UPuYdnEnbQAadbFrpF3qnSc757xibniiH8p9WizX1lSxOUkGtIGS3E5JO_KzcYpBDYsoC5jOIBDY8JnIQFiSFEjw-6IuDn_vxzHEfh5_7OvQ_1suexZ2KuDmZaEISMvsrisE7jZ7dX8Rx2BNw7jC9DRS2G9GB1j96nPaFTNGlyRh1TxFdyrdhBZ1BHaEewxMf4hJuxwlwNdz8zBVArTX8UdogoqmYKqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/5818" target="_blank">📅 17:21 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5817">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7862dff401.mp4?token=WnROKNqdIpOIAgRyb0DZuw0MdVO5FKdTENOKNu1qf_edDkDPZONR7gbTgC-8l1FvlV3-A3xra26L4m601uDiJ9Ce3lbLA0hxXCxsQhJUwicG_56YI_9Oa0t_i7pFHQb7yF_71S1Xm2X0pTDsJgWjw2W-OMpSOksE1euT9dL9YBGZTo25Wy9B8Nmv1MV1lpoAWDDqWEylDb5AW3OR6oJNmfibTUgc6PurKMl33idwKVp1q1qhmXl9QXz-m8wx4ViB3F7XkcqndlsN7cEdHBi_KlXQvdqHw-WsJQuuV3gu1qFj4YHsF4bNCPbK-yNp1geVbU9jGQKL2UAnB2fMAXeUkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7862dff401.mp4?token=WnROKNqdIpOIAgRyb0DZuw0MdVO5FKdTENOKNu1qf_edDkDPZONR7gbTgC-8l1FvlV3-A3xra26L4m601uDiJ9Ce3lbLA0hxXCxsQhJUwicG_56YI_9Oa0t_i7pFHQb7yF_71S1Xm2X0pTDsJgWjw2W-OMpSOksE1euT9dL9YBGZTo25Wy9B8Nmv1MV1lpoAWDDqWEylDb5AW3OR6oJNmfibTUgc6PurKMl33idwKVp1q1qhmXl9QXz-m8wx4ViB3F7XkcqndlsN7cEdHBi_KlXQvdqHw-WsJQuuV3gu1qFj4YHsF4bNCPbK-yNp1geVbU9jGQKL2UAnB2fMAXeUkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جی‌دی‌ونس میگه ترامپ میخواد با این تفاهم‌نامه با جمهوری اسلامی،  بازارها و مخازن رو از نفت پر کنه،  و بازار سهام و اقتصاد رو درست کنه بعد تصمیم بگیره با ج‌ا چه کنه.</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/5817" target="_blank">📅 16:36 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5816">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f9a10fc62.mp4?token=WvuE-elYBg2W3qL3cUqAN6Kdtut-JUG5OO3uU5hLRdYP4XRDtdHxPQmvnX4-LUbQwId0E7JAfFFZVtJOgJYUY-ioSpeSosBydeuoXnHdJoJIQdl_Pq6_dOQputLCuHZwXD1zxZILSS-G-mK06e6L_X_ONYE9wTbxUPA9lkSoer--g5BTdHgANUfVztuvDhE47617Mka3mPMVHdnQK16VY2TWqMDzXdo3MLddwxiyFDYhW54QT2OtosTbVc_qbK1vCgrhZucYQDUcP-XP-XMqK_LAg438wSIjbrywberupadcVMZTCrmwuBgs5y38IFpfBKA-363-_JE2n-kcSLRQIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f9a10fc62.mp4?token=WvuE-elYBg2W3qL3cUqAN6Kdtut-JUG5OO3uU5hLRdYP4XRDtdHxPQmvnX4-LUbQwId0E7JAfFFZVtJOgJYUY-ioSpeSosBydeuoXnHdJoJIQdl_Pq6_dOQputLCuHZwXD1zxZILSS-G-mK06e6L_X_ONYE9wTbxUPA9lkSoer--g5BTdHgANUfVztuvDhE47617Mka3mPMVHdnQK16VY2TWqMDzXdo3MLddwxiyFDYhW54QT2OtosTbVc_qbK1vCgrhZucYQDUcP-XP-XMqK_LAg438wSIjbrywberupadcVMZTCrmwuBgs5y38IFpfBKA-363-_JE2n-kcSLRQIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جی‌دی‌ونس میگه ترامپ میخواد با این تفاهم‌نامه با جمهوری اسلامی،
بازارها و مخازن رو از نفت پر کنه،
و بازار سهام و اقتصاد رو درست کنه
بعد تصمیم بگیره با ج‌ا چه کنه.</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/5816" target="_blank">📅 16:31 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5815">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🚨
نتانیاهو : اگه نیاز باشه به تنهایی و برای سومین بار به جمهوری اسلامی حمله خواهیم کرد.</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5815" target="_blank">📅 00:04 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5814">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/60c1fdbeee.mp4?token=F6qOFVcJLEi1D2vcXC5eVSTCv1aa2sSuXi0PKT16L7nYFI9xSEycgwBxsMm7Ms0sc7APtVqKCoO_5K9shDGY0GmWaG0qx4mOHWKwnRtTYKHhN9r3LP1Ng6m1o3MZ7qQotjHU-MgMNev_ORgjnq65Gby_W1CYPxW4w8z5tMsjkwBagda0jMJ-Z_UvpnjbDeiR7soRPJxsVBizCNMjV54loUttW7N3-ExjyRGr4P8UBzefKo6t3TOlywattiflnmhctl9nc1R9IWccJXpXF-Vz98UQKkfg-VTgs4vC7Rk0mB7ZoPdoOdB03vEU6EsXFxxD87fgXmdj70dsPABLn_YkMT83Q0umTuH1bq7B_ZxQK68kOEUwB3a-1QDM4wdNhox8y7S8NImh5SlkbTJaTq8OZ6DaOyvrfWo8SMUCnYgQ3tGzB3ctLR7KwdNisYsj9e-OAgmlHRlAXXZmXqBKJFCCjgdKGWqwYVkYpH6lyATyCpimorU0ZQbOkVcxlsFeMQz1tiHv9Pa2WdZC2cBbG0s1qNMlaKVhzpKU41Uj-0V6-cqjBU9b4SN2fQ3Ni2I5NrY7P9sx8jHarNIZVOg6AobWsI_JHRX_WzrzAxB-yPwhTmfDXzuL1NxFL5ESC8S_WMg53cuRhpr1T9hYt0mugVrbuOomH52sj70GUY_v101nMCY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/60c1fdbeee.mp4?token=F6qOFVcJLEi1D2vcXC5eVSTCv1aa2sSuXi0PKT16L7nYFI9xSEycgwBxsMm7Ms0sc7APtVqKCoO_5K9shDGY0GmWaG0qx4mOHWKwnRtTYKHhN9r3LP1Ng6m1o3MZ7qQotjHU-MgMNev_ORgjnq65Gby_W1CYPxW4w8z5tMsjkwBagda0jMJ-Z_UvpnjbDeiR7soRPJxsVBizCNMjV54loUttW7N3-ExjyRGr4P8UBzefKo6t3TOlywattiflnmhctl9nc1R9IWccJXpXF-Vz98UQKkfg-VTgs4vC7Rk0mB7ZoPdoOdB03vEU6EsXFxxD87fgXmdj70dsPABLn_YkMT83Q0umTuH1bq7B_ZxQK68kOEUwB3a-1QDM4wdNhox8y7S8NImh5SlkbTJaTq8OZ6DaOyvrfWo8SMUCnYgQ3tGzB3ctLR7KwdNisYsj9e-OAgmlHRlAXXZmXqBKJFCCjgdKGWqwYVkYpH6lyATyCpimorU0ZQbOkVcxlsFeMQz1tiHv9Pa2WdZC2cBbG0s1qNMlaKVhzpKU41Uj-0V6-cqjBU9b4SN2fQ3Ni2I5NrY7P9sx8jHarNIZVOg6AobWsI_JHRX_WzrzAxB-yPwhTmfDXzuL1NxFL5ESC8S_WMg53cuRhpr1T9hYt0mugVrbuOomH52sj70GUY_v101nMCY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چرا جنوب لبنان سقوط کرده؟
چرا ۱۱ هزار ساختمان صاف شده؟
چون رفتن دنبال «خونخواهی خامنه‌ای»!
به قول خودتون چون «پای نظام» شما ایستادند! به خاطر افکار شما!
خواستید جنگ راه نندازید!
یک میلیون شیعه ۴ ماهه آواره شدن!
شکست‌هاتون بیشتر و سنگین‌تر!</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/5814" target="_blank">📅 17:59 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5813">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6a28a5f6ff.mp4?token=bg9XFY25-g3D3UEG3J1yFX_mEU25mExNnDSFq3qc39nWAPWTzzyA-8u18jQyfVOeCdFXa3M6ctogfbD5k-bCnRnDyuZtuSpcQtY_4f4r59an0h9XvpUP7ApJlLiokyfZFwqpPg4sFbEXQ3HBubgdC23rKtJEGnv3btU6sazPzjpm_w46xjGi0trmJXgp3VeCxPFgXOEY0u9Oa9P6nJSb30S8emMeahVdZDkPF5UB4AeDoYcgrxUC2AUajDej5cC4tIXHnqPWs8B5AbBmdxzhwSDJC2GL0A3DPWF9n72POFg8GWWy0h6TW_fNYlwbYPiCnuzB7yMamfd6MqHmKrlYog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a28a5f6ff.mp4?token=bg9XFY25-g3D3UEG3J1yFX_mEU25mExNnDSFq3qc39nWAPWTzzyA-8u18jQyfVOeCdFXa3M6ctogfbD5k-bCnRnDyuZtuSpcQtY_4f4r59an0h9XvpUP7ApJlLiokyfZFwqpPg4sFbEXQ3HBubgdC23rKtJEGnv3btU6sazPzjpm_w46xjGi0trmJXgp3VeCxPFgXOEY0u9Oa9P6nJSb30S8emMeahVdZDkPF5UB4AeDoYcgrxUC2AUajDej5cC4tIXHnqPWs8B5AbBmdxzhwSDJC2GL0A3DPWF9n72POFg8GWWy0h6TW_fNYlwbYPiCnuzB7yMamfd6MqHmKrlYog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5813" target="_blank">📅 17:53 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5812">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/085c31b1b8.mp4?token=pwC8oMUqbRmreE0C8WzpkI2guG8J-sS6AaL5s_PM1m1hMq2hQwItmpZQKvqNm-k_Zw-Stt7f-XEvPR--s5epSfqbuaBgizKxcBqsL4MDtu7lecKrRQBjgK-C0aTQ18A-pJ_MJlChgFEGAXnNPygKrJMKciVm3SJGa8um31-n9-io5a85yobLCdZUNSmQOBCrH_wQz82kRUB8P1ocmFCtGcyQcYMnf_dDVW5KbVNlLEsp09okxND7f5jHIJ7l-kIXlI1JRRmgLdFBP8EXk4C-mJRFEOS7j2zCyOxzfHjHkXVGroX4BPSTMo9Wfnj5fPKz48rSYd0eVHX7PCgH6YLzpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/085c31b1b8.mp4?token=pwC8oMUqbRmreE0C8WzpkI2guG8J-sS6AaL5s_PM1m1hMq2hQwItmpZQKvqNm-k_Zw-Stt7f-XEvPR--s5epSfqbuaBgizKxcBqsL4MDtu7lecKrRQBjgK-C0aTQ18A-pJ_MJlChgFEGAXnNPygKrJMKciVm3SJGa8um31-n9-io5a85yobLCdZUNSmQOBCrH_wQz82kRUB8P1ocmFCtGcyQcYMnf_dDVW5KbVNlLEsp09okxND7f5jHIJ7l-kIXlI1JRRmgLdFBP8EXk4C-mJRFEOS7j2zCyOxzfHjHkXVGroX4BPSTMo9Wfnj5fPKz48rSYd0eVHX7PCgH6YLzpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محمد اکبرزاده،
‏ معاون سیاسی نیروی دریایی سپاه،
‏شب گذشته در یک سانحه رانندگی ساعاتی پیش کشته شد.
او در یکی از اجتماعات حکومتی به صراحت گفته بود حملات آمریکا «واکنش» بودند! یعنی ما حمله کردیم و آمریکا پاسخ داده.
جنگ‌هاشون در لبنان و فلسطین هم همینه! حمله می‌کنن، وقتی جوابشون رو میدن میگن ما در حال دفاع هستیم!
۴۷ سال گنده گویی کردند و سرمایه گذاری روی تروریست‌ها و وعده جنگ و… تا بهشون حمله کردن، گفتن ما مظلومینم و داشتیم ماست‌مون رو می‌خوردیم که مورد حمله قرار گرفتیم!</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5812" target="_blank">📅 14:57 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5810">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cspURCWeyWP6T096CJaTW5-TiHLPbplbn9xz1ROel1ygL5QMt_Eq2fsjJQ19COrT_f1ESRRycv4S2QtsCFhS004psqmdn54cTr3XS6sMMkrnl92bzYv1hi9gqjo_mzZbBBfKz-27hOPZV3NHTUOp81gwSrNeGHxt6MlJ-0iFmPji8yoHizdqEfzMEYy4QIjkEV5m4opfJENInb3K5VQV9nhyHGQCKB-yb7ooPHhpVvhR79-hoK-1S7KdAXHkQK46Vl2j9HUnz-uxQGeoSsAz1iW2zQZKB8dzHE8un3z79ocx60lY8kg4a2IdE4BEg1FeC6GXmEQYr3_uj8U5xHx3LQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Irg033fSRv4t20w-ywRczmoymGbZgZG2NUyUcTPtfwjRat03r9uZ5I4PiF8KItNi_JVvtuLUNyQrKibZVgvlKlLFYmsbD4UpFkeQxpwd7t9U-VTAI8dJscDG_slN3qFDn48hEuUXxvsIon246guVN6uxOkVRHTaz0Lrigfn00ldTeahMjCfvRLVtZcAamp44VeWK4zH1UaURM6MoxqTsZCgXlvUXSam32ysD75SZBldOBOmjeYLInz73PX1Fa61m_-Mu92_Lj3gN1lhSz7QesKAc1bk8SKg9EasR1WsYjuDJhyhRqbePznJBVrHD982EzHRUub6_uZj5sg_E4j36fQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ده‌ها تن‌ از‌ سران و مقامات عراقی بازداشت شدند. از خونه‌هاشون میلیاردها دلار پول نفت و طلا  پیدا شده!
خیلی هاشون از نزدیکان جمهوری اسلامی هستن.
با تصویر خامنه‌ای و سلیمانی و سیستانی در خونه‌هاشون و سوتین و شرت طلا!</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/5810" target="_blank">📅 13:32 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5809">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee0be552a1.mp4?token=RLzM5o_jUi3PyYmNZ9pndjN39dh5asAgYO9acxHBP9PXS7HKHdAE_YZFKzuwLd6-HhkA-wRnBeY287zjQ26QFIVsZnid6VGYW90zpUq9p6qRELbQTK64PMkeNXqEuZNXwxHAOW3jztcrBqK6VUIXV_lDkUfjp6aW61W6tK-4Q9e4bdsL3lpIokwuIRSp7Xnn8Mf29zRqVZOLCCTSjyK3rMLzc3MgKIiUhU0XWnoNxuv0KNa7dbVuPCc1YPqKF4pO4RiFFazClCxBZ4zoXNOMJfCxZQcAcTz_6V5APMLIftUe7qi34SHR1XxCe_j5rJ8mkFUjQBUPP4X0Nsimyy79nIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee0be552a1.mp4?token=RLzM5o_jUi3PyYmNZ9pndjN39dh5asAgYO9acxHBP9PXS7HKHdAE_YZFKzuwLd6-HhkA-wRnBeY287zjQ26QFIVsZnid6VGYW90zpUq9p6qRELbQTK64PMkeNXqEuZNXwxHAOW3jztcrBqK6VUIXV_lDkUfjp6aW61W6tK-4Q9e4bdsL3lpIokwuIRSp7Xnn8Mf29zRqVZOLCCTSjyK3rMLzc3MgKIiUhU0XWnoNxuv0KNa7dbVuPCc1YPqKF4pO4RiFFazClCxBZ4zoXNOMJfCxZQcAcTz_6V5APMLIftUe7qi34SHR1XxCe_j5rJ8mkFUjQBUPP4X0Nsimyy79nIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بیش از این‌ها تحقیر بشید !
چه در ایران، چه  در لبنان، چه در فلسطین،
چه  در دریا ، چه  در آسمون!
در ضمن بهتون دینار و درهم نمیدن!
قراره یونجه بهتون بدن و پولش رو هم بگیرن!</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farahmand_alipour/5809" target="_blank">📅 12:55 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5808">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h_xZarAFdtiVGPpVgGolH6CH7APRgQaQu2wAZxyIqnJvAKK-KQRh0YT3cpBaKhujvnmgPl3hBwvNNWdBHbrfUoMSZloHh8ZUpCPj4ExzjvXQTE_1esBXUKznUvTOs765-6SWzQYngpVcW2Q2Ee6wL5NUHRuR48xcK83NC_FRHSyi5o6bYkwg2EaKERRJiA28LrXCJAM3S2LicDCpF69tYRt_d1FItBbIOgRVRhoV9urElrtPGG_UfT_WgkY8qPMhGEVWKjysoyj0MNUOKhDB-iXMN8SOukTl1a-KEs8NpCSp0Wtp-O_2KSCNx4Vn0Y-y3bHWn5Q1IauUGk0O3kVk_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقبره رهبر مستضعفین! که در زمان حکومت خامنه‌ایِ ساده زیست! ساخته شد،  با مقبره فرعون‌های ظالم!  که به قیمت و نرخ امروزه، مقبره خمینی ۲ برابر مقبره‌های فرعون هزینه برده!  ولی عرزشی که نمی‌فهمه! بهش میگن رهبرت ساده زیسته خیار نمیخورده، خوشحال میشه! دیگه بقیه‌اش…</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/5808" target="_blank">📅 12:47 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5806">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WWFasbeI8L6rLbCXxYF2RicLZZIy6g9-ODkPLs1ZAJ9XcQnLy3blDEmQgBlo5jAd9Wy17-5euIHmiBRHE8CRZxyTmZOEkPKJkBDEOClpELy7qTW6KoRk3xQ1TRcBsmrUYuWHU5g-jMkhIn753jF8s3I5DrBpUY1YjxHph4wUEZd9BmhCiZXtVbdyXnj0WEo7a2ypXYzrsRwbQuqX93lVSLlsm0fnfz7V1hlq7TtNDMqNdgIhxa1NR6uggvkqfp5ZwUitYjK-LN3aY9DQ36pJHjXaulxZ-UNQvv3XOJlGb2-X4KaRnBVouAwbZguVpfgRKxJtO45DDWi680l_mseD_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VtkNNEixXfT_iWYnp7h_H540-mInUo4Whe9Z0D31To7fyZZXCj5QNsj2aTNbq2jAs78X1KXMTiVmPdtK8MOHTRKy5O8RVCoqm58MwoDtdvJkRSv_5uvmj3tFmeMS0Yo0dUI45hNEWZtDnSx6Kfh6oTT3ZYUUn8i9nhMo6oFzToni1uGyOrtQE6GlN_YrRcqIag1eFlNNIGKgcsSqdWLWWuhB30ADdTucQ85rLKhDhJUMfmF4pSmuqrMCMmM392lZDI7vCjfAijd8WMPvDtwRqHRKtsG9bmzROcCvZTotTU9--1HOlMV6F4H53xLDD0vHvH6JpGUxeOMGiun9QVvavA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">هزینه هر روز تعطیلی تهران،  ۲۴۰۰ میلیارد تومن خسارت به اقتصاد کشوره!  اینها فقط ۳ روز برای خامنه‌ای تعطیلش کردن! یعنی فقط این تعطیلات ۷۲۰۰ میلیارد تومن خسارت به اقتصاد میزنه!  این فقط یک قلم از این هزینه هاست!!  ولی خب رهبرشون «ساده زیسته»!  خیار و هندونه…</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/farahmand_alipour/5806" target="_blank">📅 12:35 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5805">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k8ixnTLlxNeccg9ny7fz-5g-Cgf-Fwa_eCIe-wa8kDiUaE2swqfMb1ny_w_GMtffzupPP1KWnCUyVfNr0gt_yvhsZWeXz4WN1KW00s_-_wysMCMbiRHXAP2QYPgRsnJsv4RQLjWp8_EZAMK1Or27-kfV49U2AahcIlnEFrMY8V2ViXC29fitt4PlY1aZ4nLGUWD0UUwcJ8Z28ZEtNnacx71NSL8HfY9HMKMqczee6i2RL47MDQZL_4C-RBiEnWcrdS6y7b_5DAv0PX8xgnAtMQn7heclXhoJgSHHQ4JVMP3fUqN97aXyhnbCJ1MleMHgeiBvWKaxId5DcT2shNt0eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هزینه هر روز تعطیلی تهران،
۲۴۰۰ میلیارد تومن خسارت به اقتصاد کشوره!
اینها فقط ۳ روز برای خامنه‌ای تعطیلش کردن! یعنی فقط این تعطیلات ۷۲۰۰ میلیارد تومن خسارت به اقتصاد میزنه!
این فقط یک قلم از این هزینه هاست!!
ولی خب رهبرشون «ساده زیسته»!
خیار و هندونه نمیخورد!</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/farahmand_alipour/5805" target="_blank">📅 12:29 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5804">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b7a3755d2.mp4?token=rqzHeu17fIq_aSeWUl7x3NSz2LVg9AQxUiq6ejL_MIQ5OKEBgFdwYsnUxDM-lahfnx53slYRCwtN4mCCbVwHBA0SzKUdtRjcg_NPd0gVFfwIQmhwbfgOVsT4-CXMIxtiIZ57Zl98IO-gKShKGDOSw03oS01zKxJ646IveV0tcvsIRP1i_jiPpSe0YVo7ydhD6GpdHhUWaIj120GvC9yh0_2IqExoF0J5X7JAGEYr3PG1lt09Bq26MeY487QlGWq_MilezOnZMShT2__zbCRn83cUcEEurmMqDuzogLEjUbtOhUsZlRPygwO_TmJTY1elEXHWEmgTyVlpSXTMcZGl8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b7a3755d2.mp4?token=rqzHeu17fIq_aSeWUl7x3NSz2LVg9AQxUiq6ejL_MIQ5OKEBgFdwYsnUxDM-lahfnx53slYRCwtN4mCCbVwHBA0SzKUdtRjcg_NPd0gVFfwIQmhwbfgOVsT4-CXMIxtiIZ57Zl98IO-gKShKGDOSw03oS01zKxJ646IveV0tcvsIRP1i_jiPpSe0YVo7ydhD6GpdHhUWaIj120GvC9yh0_2IqExoF0J5X7JAGEYr3PG1lt09Bq26MeY487QlGWq_MilezOnZMShT2__zbCRn83cUcEEurmMqDuzogLEjUbtOhUsZlRPygwO_TmJTY1elEXHWEmgTyVlpSXTMcZGl8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">برنامه «زیر آسمان ستارگان سینما»  در شهر بلونیا در ایتالیا  که ۵۰ شب در طول تابستان برگزار می‌شود.   (در عنوان برنامه در استوری اشتباه کلمه سینما جا افتاده بود)</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/5804" target="_blank">📅 11:16 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5800">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf427145cc.mp4?token=SrlQyobqv8c1iB7ys4KyAVrOXquoa607-9z0meVGW4Zq3nfnhl6v-xGPgMPTBumBGouZrAxOtnrDk3PfBUhwVVjtTGd_SV454_vqWxFv7kgNCX6leH5cNQG4wDzoL_1caLDa2O8TRNVbH5yy9e_85SQwok1YN4GS6YTYAhHc-LC6rAuXV4SuQOaZqR5ki07IU0eUyAwsJsU4HBcMA4yYnJX5TtAvV8XMQ0tHwekiy38iVojb0_z_DbEkC1OSOuXQzreNIbD_EZfdMiNdtG8QofGpkmgSuoISN_fZTWr9ZG8-fiErTJwGD7tgqhur7-_xP5TmBFaVgvfCNZGhn6PAjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf427145cc.mp4?token=SrlQyobqv8c1iB7ys4KyAVrOXquoa607-9z0meVGW4Zq3nfnhl6v-xGPgMPTBumBGouZrAxOtnrDk3PfBUhwVVjtTGd_SV454_vqWxFv7kgNCX6leH5cNQG4wDzoL_1caLDa2O8TRNVbH5yy9e_85SQwok1YN4GS6YTYAhHc-LC6rAuXV4SuQOaZqR5ki07IU0eUyAwsJsU4HBcMA4yYnJX5TtAvV8XMQ0tHwekiy38iVojb0_z_DbEkC1OSOuXQzreNIbD_EZfdMiNdtG8QofGpkmgSuoISN_fZTWr9ZG8-fiErTJwGD7tgqhur7-_xP5TmBFaVgvfCNZGhn6PAjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">برنامه «زیر آسمان ستارگان سینما»
در شهر بلونیا در ایتالیا
که ۵۰ شب در طول تابستان برگزار می‌شود.
(در عنوان برنامه در استوری اشتباه کلمه سینما جا افتاده بود)</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farahmand_alipour/5800" target="_blank">📅 10:42 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5799">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ciMQVVjPLEDL8kkYw_Ql1menQfnecqfvllhDkaL10pjk9ilNjRHuw8MQIWe23pAUmIITGJBKWncj72uiVTULg6Gd9aNUmMJbTv4fj6F5bfuzolgf7nkirroH2GoHgjMI3Uqo7hWurmslXx5y03ij3WpVGICaY88kHHunYgllpNWOgwLuICzx4m-p4Wlyd-eOXzODiPAxo4je74g8L7G68OZ3tQFfZr68luCIn0EgCmXHP6roU5eb6Eh5VD9aGepDr6frOhVYBYl4f7jLaDk0Pu5I4F9aFwaHJ-kDblc4-Fjnzys7TzhKzA2RklXoBLPhzlu3cdd5yEwe8kIHSjpywA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هرگز به مردم ایران نخواهند گفت!  اما کاملا قابل پیش بینیه که هزینه این مراسم بارها و بارها از هزینه جشن‌های ۲۵۰۰ ساله بیشتر خواهد بود! چندین برابر!  درست مثل راهپیمایی‌های هر ساله اربعینشون که باید از جیب ملت ایران مصرف بشه!  یادآوری : هزینه جشن‌های ۲۵۰۰ ساله،…</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/5799" target="_blank">📅 09:26 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5798">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2dc44e27bf.mp4?token=lSACDvIvSEkO1oOJzT3QXu0gYYd2X6_MLHzVAhzOaXr7ejtq32fhUI6FFiJf4VRq9opGZULSxnEnIpKA3U8Ke_Dq85E6cEgiFLxv0Mz_ZggdUywg5MvAIHbElCtecwSgPsUS90JnyLm6sxk59iUoC9GVLe6JaF2AWybDG-E-aVRMcNmu9n1F9yipBqbECgvQez7TA1ARYF_zPn9yDEvRlTo_TAKBH_pNyDrvjoex8abDY_COCPFmjVp7CsXNzv4yAVWaW4rQ6SUyTD0V8K5kmEXNyKeaUFryFBn_b5tLugpeRFcl2FH9_-qGU5-LZvcOrkkdYEK6X19oqQK_xXacMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2dc44e27bf.mp4?token=lSACDvIvSEkO1oOJzT3QXu0gYYd2X6_MLHzVAhzOaXr7ejtq32fhUI6FFiJf4VRq9opGZULSxnEnIpKA3U8Ke_Dq85E6cEgiFLxv0Mz_ZggdUywg5MvAIHbElCtecwSgPsUS90JnyLm6sxk59iUoC9GVLe6JaF2AWybDG-E-aVRMcNmu9n1F9yipBqbECgvQez7TA1ARYF_zPn9yDEvRlTo_TAKBH_pNyDrvjoex8abDY_COCPFmjVp7CsXNzv4yAVWaW4rQ6SUyTD0V8K5kmEXNyKeaUFryFBn_b5tLugpeRFcl2FH9_-qGU5-LZvcOrkkdYEK6X19oqQK_xXacMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هرگز به مردم ایران نخواهند گفت!
اما کاملا قابل پیش بینیه که هزینه این مراسم بارها و بارها از هزینه جشن‌های ۲۵۰۰ ساله بیشتر خواهد بود! چندین برابر!
درست مثل راهپیمایی‌های هر ساله اربعینشون که باید از جیب ملت ایران مصرف بشه!
یادآوری : هزینه جشن‌های ۲۵۰۰ ساله، به ارز امروز، حدود ۱۲۰ میلیون دلار بود!
هزینه سالانه گروه تروریستی حزب الله لبنان
یک میلیارد دلاره! ۱۰ برابر!</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/5798" target="_blank">📅 09:21 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5797">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d3b713ac56.mp4?token=fhPuHxv_QpdCuTkDJN3qGUzplIPaAMGijNzDVGR2bkIUHCsEeZHMpxe89Vv_Xodp5axLzNz9Cfo6Rd9j--Srrre3o0pP2RAlQZ2649dSlefN-UF7wgftEsRjx5G-yo631YcidlubB0dVWL5sxB3ZUoVOdrMcutY6QSqpYdobbO0ww9IDIMBDCOiAGbVwz-ZQJb5yDrDk8g4QppWBOzBjTatz5edyDXleZVyvFfYu11BT0PHkk8QCg1aMGrTFHlwffwoPg1F4UOnJKcY7r6IKvCWN9DmVOU5yXaYBwWmZfpbjIH1fxQ-WgXcPV6NFsRkJIt2VR9dMPuN8f9us6_jbgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d3b713ac56.mp4?token=fhPuHxv_QpdCuTkDJN3qGUzplIPaAMGijNzDVGR2bkIUHCsEeZHMpxe89Vv_Xodp5axLzNz9Cfo6Rd9j--Srrre3o0pP2RAlQZ2649dSlefN-UF7wgftEsRjx5G-yo631YcidlubB0dVWL5sxB3ZUoVOdrMcutY6QSqpYdobbO0ww9IDIMBDCOiAGbVwz-ZQJb5yDrDk8g4QppWBOzBjTatz5edyDXleZVyvFfYu11BT0PHkk8QCg1aMGrTFHlwffwoPg1F4UOnJKcY7r6IKvCWN9DmVOU5yXaYBwWmZfpbjIH1fxQ-WgXcPV6NFsRkJIt2VR9dMPuN8f9us6_jbgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لحظه‌ای که «سپهر بابا» ستاره رفیعی را دید.</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5797" target="_blank">📅 22:28 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5796">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e1e05c8825.mp4?token=fDRWuOH8hr0kprN602uDZ29hzMcysYk4E0GPBZ35254_h1EZSYcbQzGwI9aziJAyJ9ZmFUcW51NdyqHyVVJPr2bFjeI1wJs1yiO14VrgFuPqyZFnZbRHufLzEppySBTEwczk1BBWfrYYGehd6_KW4XIUiKXf9E9U9RzpmMX9Mddk4PV4SvUbkGRPwfBbPezUU89FWv4hT-ZvR9wrzLwaSdYmuPxOqqdqkxtfhsU7PSw0pePud8ASj3lHSCuYp57xX7e8IC8sHVcox4ShOQez5Gnb-h6LnDTqC5eGN2X3YEhOypjQ0jySJQOSC5cNkYF9O7zND6tG3vxLrXb-5HAVHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1e05c8825.mp4?token=fDRWuOH8hr0kprN602uDZ29hzMcysYk4E0GPBZ35254_h1EZSYcbQzGwI9aziJAyJ9ZmFUcW51NdyqHyVVJPr2bFjeI1wJs1yiO14VrgFuPqyZFnZbRHufLzEppySBTEwczk1BBWfrYYGehd6_KW4XIUiKXf9E9U9RzpmMX9Mddk4PV4SvUbkGRPwfBbPezUU89FWv4hT-ZvR9wrzLwaSdYmuPxOqqdqkxtfhsU7PSw0pePud8ASj3lHSCuYp57xX7e8IC8sHVcox4ShOQez5Gnb-h6LnDTqC5eGN2X3YEhOypjQ0jySJQOSC5cNkYF9O7zND6tG3vxLrXb-5HAVHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تفاهم‌نامه ج‌ا و آمریکا رو به طور نمادین آتش زدند و گفتند که این قرارداد حقارت‌آمیزه که خب این بخش رو درست میگن!</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/5796" target="_blank">📅 18:49 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5795">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hXpDzqBBQfovYvX1_tgVSNdCodQQettIHe6uQyOm8MD2b005OkfP9qmV_uX4_pv9deQAAlndfApy6-zXdCyLrC9J1Qwvfk2ncz4Plba1y-HCTCEtxKlBWp4evNMBzzirvpl7ed6c9UM9G-FVnhBXAtXAsrNj4n_HRb-Po_ZAVC5OP-HDJfejmYvlFXCgK3XbuaNehywrGPzXf2tvIrn4mnJAJmUmrUcpthBMBxV43PSP4PqFX5sourDesekZW8-6-3JJCjiqlS02xGXo9BkBCLSvTNRZ8yr7tVis34JLAeifSl1mGpgBeyoeuuwCzhO8toTDGPYjHB4UdzCIulfTmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امروز - دیدار فرمانده سنتکام با رئیس جمهور لبنان،
یادآوری : دولت لبنان چند ماه پیش
حکم اخراج سفیر جمهوری اسلامی رو صادر کرد
و ج‌ا را متهم به تحمیل جنگ علیه لبنان کرد.
مقامات لبنانی و اسرائیلی چند روز پیش هم مذاکراتی داشتن و گفتن مشکل مرزی و ارضی نداریم!
مشکل دولت لبنان و اسرائیل شده گروه تروریستی حزب‌الله لبنان که با پول مردم ایران تغذیه میشن برای جنگ افروزی!
در جنگی گه برای خون‌خواهی خامنه‌ای راه انداختن و فرار کردن، ۴ هزار لبنانی کشته شدند از جمله ۷۰۰ کودک، قالیباف هم به صراحت گفت لبنان ۴ هزار شهید تقدیم جمهوری اسلامی کرده!
لبنان ولی نمیخواد! جمهوری اسلامی به زور یک گروه مسلح رو راه انداخته اونجا!</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/5795" target="_blank">📅 18:44 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5794">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e972609e9.mp4?token=KTz__n8QgFUUNvXpusYypjMhM_XPXdLypCTXhCZT_63jeNz1-fAgY6tGLInrWHOo5hPxEzCI5oMRCqrqrKmMO5mojSKImv2VE-LdLEXxY-5oyO4atW5Kmoi6qFn_by1VgGAmyJDqM2oeB19_et4_tJfTux5oP3a8h6zhrKFaKqFPeIMxTSR3gZXuYQSIz6UQDhMVhBFm2DwtVcT4QUKpGe22Rf7Hj80b6k7uH5RgEl2Y1bw-yyC_ARiGQVULCL6MVrrKYGqpdhyxb2klVJJXuWkCYDknnG2F1kYtkO3NQMBNBC6Ml-lvHlLN8VZayhp88_ArXgjAKNRPBqERa0LLYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e972609e9.mp4?token=KTz__n8QgFUUNvXpusYypjMhM_XPXdLypCTXhCZT_63jeNz1-fAgY6tGLInrWHOo5hPxEzCI5oMRCqrqrKmMO5mojSKImv2VE-LdLEXxY-5oyO4atW5Kmoi6qFn_by1VgGAmyJDqM2oeB19_et4_tJfTux5oP3a8h6zhrKFaKqFPeIMxTSR3gZXuYQSIz6UQDhMVhBFm2DwtVcT4QUKpGe22Rf7Hj80b6k7uH5RgEl2Y1bw-yyC_ARiGQVULCL6MVrrKYGqpdhyxb2klVJJXuWkCYDknnG2F1kYtkO3NQMBNBC6Ml-lvHlLN8VZayhp88_ArXgjAKNRPBqERa0LLYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این شب‌ها، همین‌ها توی هیئت‌ها در حال عزاداری هستن
ده تا مرد مسلح افتادن به جون یک زن معترض ایرانی.</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/5794" target="_blank">📅 18:39 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5793">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hGntDd79QN9joeorGQMeLXqU5sr0Mu07a0SDbSGOyGyIwc2X10hVgi42llrRTENqpgDY_fbg0oV2F17lIymOEPfYGIfpIO_hLeFbq7jdfn--pTxwkrLnSyfWul5TcAVPmReBXezwBoxv8ZvUw3crz4uc1mwgnY9_bghAhsDNHo0fh1Ex7Iv23MlmebfsTHq67rebRfQ55gt9i3M9G_ssgtZ4_6n1X8Qo03bvNHBeVa7ETz0Jles4LZFL7Yc7P747f_rU9IQXzSQ7mmKNDLdX0uVVumxy3tvioW1M6dvlUBvs4Pm7Cew6wMCyifac460woFVtTPWza4i3UZXoUWcE_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حالا در حد یونجه و ذرت ایراد نداره</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/farahmand_alipour/5793" target="_blank">📅 18:33 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5790">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MC0TutO6E_bPCmPvgcAvZpqMWEyZANVY49bSbE63W2FgMjC_I992j-KoUgKe6zvAY8gRg-UwedNbjxTbYHzobYebmp1QxSexOygpqxDQYLhGLOUZdaaHGF9PKVF1JbvlnMq341CQGR63YM5kQy6V3A_PnkhSQ8b2kCbrEVQpwHRzJ3JaZ13yRtQeC9OKTevh7qhoI-RKIqYvzdQ3uE34k2nyX_AmwiaBgrz94k6y_vTCwfvfsqJh63QmQHJ6RGDz_jq-GQN2z8J9po0bYY1b7bfiPZsw53vq4Ec_Z8BVRStYpaZ2gq3IFTMnpECZD031tgBeeRMoW-yiqZD5hGpTdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/651901a9ca.mp4?token=NIdE5YKLBd-NlbmmhejzP9JuQVst6YkbcQqcfjeBmotZJzZmsqWB_xC3r-eNHyxWeWIM1zGwge7D8JqEeLf9xK7xLJf0KoeLQ1-5UmXTtiHyVvyAhjLtVkJXZMflV97Tzt7Hyh_x1SZ0HQsOLTJjxHxfsmJRhY5etIY54hrG6LXMuKDMawPWR1UBVSTA2fajZmwkMDEy2XxjZl0HEuIJ0WQRjA7dfbivWE9nFjUkNsMeIkVnhiD8T-Kbl2kYNcV3LKMNsNxOYWL83aLTBgW0N7lRv7RpBQYxf6oDktft6Ak_vfHX2ZxG9x1DAU7VSC1x-7DRA_iee5qh4sTWlBBHtg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/651901a9ca.mp4?token=NIdE5YKLBd-NlbmmhejzP9JuQVst6YkbcQqcfjeBmotZJzZmsqWB_xC3r-eNHyxWeWIM1zGwge7D8JqEeLf9xK7xLJf0KoeLQ1-5UmXTtiHyVvyAhjLtVkJXZMflV97Tzt7Hyh_x1SZ0HQsOLTJjxHxfsmJRhY5etIY54hrG6LXMuKDMawPWR1UBVSTA2fajZmwkMDEy2XxjZl0HEuIJ0WQRjA7dfbivWE9nFjUkNsMeIkVnhiD8T-Kbl2kYNcV3LKMNsNxOYWL83aLTBgW0N7lRv7RpBQYxf6oDktft6Ak_vfHX2ZxG9x1DAU7VSC1x-7DRA_iee5qh4sTWlBBHtg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">«عالیه نصیف جاسم» نماینده پارلمان عراق،
عضو کمیسیون مبارزه با فساد، از نزدیکان جمهوری اسلامی، معروف به مواضع تند علیه فساد در عراق، چند روز پیش میوه نذر امام حسین کرده بود. دیشب در موج دستگیری چهره‌های فاسد اقتصادی توسط دولت عراق دستگیر شد، در خونه‌اش ۱۶ میلیون دلار نقد و مقدار بسیار زیادی طلا کشف شد!</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/5790" target="_blank">📅 18:03 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5789">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">شعارها رو گوش بدید،  اینها اعضای سازمان مجاهدین خلق هستند. خوشحال هستند از صدور حکم اعدام برای «حبیب القانیان» ، توسط خلخالی بدنام!  جمهوری اسلامی اعدام می‌کرد، حذف می‌کرد، مصادره می‌کرد، بقیه  گروه‌های از جمله همین سازمان مجاهدین خلق هم تایید می‌کردن، میگفتن…</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/5789" target="_blank">📅 17:05 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5788">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/583cd57ba5.mp4?token=NcndDMkcAfVw4qZaWqzAIyzTRudl6vpdLj9YvVWxQzIpPntqhPMSrrEpceKYZgtzSe4cA2RlmbyUYXMK7_EaFN8wtUDh3ZuwQjqWnblkjOWOAB31CbB9yk8RZUX7rTzLIbiFSIyRMzNAqu9TsF0CkQS1NlRZtsbYX5140VxKQl8RUi8W9jTq6CbjJ-ALBoMYIk4uS5PWWJl_3Hb54ZmAoBbQXYLAVltm9ssov38ypSpoxeRJaSr0glzJuM2QWoVyoogDapNUBvtX0zc4ZbuAjtYX-e-yrs6fIuYSAeIFo7qHLX9LPb1sfHqFqleQvxDoxlHtf9CSHlmAfETsVxAD9YgMW4OlU_Gv7xb14o7bu633Xv9bcESnBLs6UTuexD1GQqnNa-fKBuofW8l0WJJuT9UCwUJDkFNe0olbskday5xcnituc8X97xZ0VGBpqnCOlMIscwhGpVCxpYJkkzqkfeYmLN6VwMh6S_OLDSXZCR1AAQnXZUVab_RlAG6iykjyVUF9SaBPuy_tbsdhcn8HK0klDJviL2HpMAHhcBhjfCnNqnLyur38wysmmJ7ZRb8qlqxei3As-L49SbTNnKCu3rLuxQygza2ZR4sgT8PzJTkfI4MP99nSsLn98XjVhRhmOkvs7fcCd_KJJcWKmV-kWFS2W-r5BFh5OtvNt0mSyqo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/583cd57ba5.mp4?token=NcndDMkcAfVw4qZaWqzAIyzTRudl6vpdLj9YvVWxQzIpPntqhPMSrrEpceKYZgtzSe4cA2RlmbyUYXMK7_EaFN8wtUDh3ZuwQjqWnblkjOWOAB31CbB9yk8RZUX7rTzLIbiFSIyRMzNAqu9TsF0CkQS1NlRZtsbYX5140VxKQl8RUi8W9jTq6CbjJ-ALBoMYIk4uS5PWWJl_3Hb54ZmAoBbQXYLAVltm9ssov38ypSpoxeRJaSr0glzJuM2QWoVyoogDapNUBvtX0zc4ZbuAjtYX-e-yrs6fIuYSAeIFo7qHLX9LPb1sfHqFqleQvxDoxlHtf9CSHlmAfETsVxAD9YgMW4OlU_Gv7xb14o7bu633Xv9bcESnBLs6UTuexD1GQqnNa-fKBuofW8l0WJJuT9UCwUJDkFNe0olbskday5xcnituc8X97xZ0VGBpqnCOlMIscwhGpVCxpYJkkzqkfeYmLN6VwMh6S_OLDSXZCR1AAQnXZUVab_RlAG6iykjyVUF9SaBPuy_tbsdhcn8HK0klDJviL2HpMAHhcBhjfCnNqnLyur38wysmmJ7ZRb8qlqxei3As-L49SbTNnKCu3rLuxQygza2ZR4sgT8PzJTkfI4MP99nSsLn98XjVhRhmOkvs7fcCd_KJJcWKmV-kWFS2W-r5BFh5OtvNt0mSyqo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شعارها رو گوش بدید،
اینها اعضای سازمان مجاهدین خلق هستند.
خوشحال هستند از صدور حکم اعدام
برای «حبیب القانیان» ، توسط خلخالی بدنام!
جمهوری اسلامی اعدام می‌کرد، حذف می‌کرد، مصادره می‌کرد، بقیه  گروه‌های از جمله همین سازمان مجاهدین خلق هم تایید می‌کردن، میگفتن خیلی هم خوبه!
تا اینکه جمهوری اسلامی بعدش رفت سراغ
خودشون! و در ابعادی دست به قتل عامی در زندان‌ها در سال ۶۷ زد که در تاریخ ثبت شد.</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/5788" target="_blank">📅 16:57 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5787">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/938419e982.mp4?token=LjmQkr_w1KboC-Z60ltjW8HKgcqhRhAWwn-ruULkXYFTq8DvdqzwaUXwhoQ9gxX72zsarE9eIRBvYsU3ikHF2qN-b9FUfARHy5lJYhKoR3SsvICyHdXGzAnXSoxul4cKAae00wGNZXtVStdHLCMxsshbHnPgKHFLMzWXVF3Myw-uicUsayUvmLLb6ELGqKVdiGByf87eZYQgQ5h8-sugp9jK2mGrW2GFGKR2N_-NotGPzfVMIfMsnMzZx5tLGskvVa2ilsZ9L3VwAdcUSU6PYiUA96W26ZH7soIBhANiwEsoZ9eQ-kQLWgirHjf_hzmJZ9MZgzbfwW-TGy7sfMrwmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/938419e982.mp4?token=LjmQkr_w1KboC-Z60ltjW8HKgcqhRhAWwn-ruULkXYFTq8DvdqzwaUXwhoQ9gxX72zsarE9eIRBvYsU3ikHF2qN-b9FUfARHy5lJYhKoR3SsvICyHdXGzAnXSoxul4cKAae00wGNZXtVStdHLCMxsshbHnPgKHFLMzWXVF3Myw-uicUsayUvmLLb6ELGqKVdiGByf87eZYQgQ5h8-sugp9jK2mGrW2GFGKR2N_-NotGPzfVMIfMsnMzZx5tLGskvVa2ilsZ9L3VwAdcUSU6PYiUA96W26ZH7soIBhANiwEsoZ9eQ-kQLWgirHjf_hzmJZ9MZgzbfwW-TGy7sfMrwmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قدرت حضرت عباس</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farahmand_alipour/5787" target="_blank">📅 16:27 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5786">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AIlR-1svOcEgIhCrvicNBptXGAeb3jxCLaNQXIlSaTaZFLv0LwDE3Q6kV0Zvb8AjfG69JgtDmP7ET4Ht1_X00YvP3Nreqq2qh2L5sc2qnzR6jHDHnN5Nz-hWB8hISvaTEIDAAnGyzgfnkF5PVk_BPKis3HmtuRh7mU0EUrWdAVFaFbPUKTROmAQGwX56bdHjVqmOPjya77thlZOmERmw8aP8Cf39Mi50igbkkQlRE8lnWXdiqIm0F2bHuPtKyWF1NbHGOCvay2bQDwZhLnhiv2Ul6yiMplrvFKOgw3M4WelipwBVPvFinkvGRrHgywqG1JhAXJX3GMDfJX2_FsI0Yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای فروردین ۱۳۹۹  همکاری جن‌های دشمن با سرویس‌های اطلاعاتی علیه جمهوری اسلامی!  همین آخوندها وقتی اصفهان در محاصره ارتش محمود افغان بود به شاه سلطان حسین میگفتن اصلا نگران نباش که ارتشی از جن‌ها میاد به کمک حکومت شیعه!  ولی این جن‌های نامرد نه به امام‌حسین…</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/5786" target="_blank">📅 11:31 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5785">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b91e9581d.mp4?token=gmEj89lPRaqRbbhmvSdchpeVslvC5cJ0PXn_bYcpqOPf7l17oAIQlLBeESBpNmNFHzgBl_rwCUHPHaFsHEiK7GvD-pKRukEThKoMR8y67U2QfAeHVQFQW1q_vmVCl23mG3Jg4oeH18Jfv5OaPyuWKLpXTy00gDN3houeFI-GgAek6ewG1ZAE5vTXZ74BrK22A9MryhiTuXgHZNZb9kDown8yR8rsliEgTS3UPrM49xqNdpi8GW-RyUeGLLWCWjhPtlGifOaPzcqg9Kf6PkP_rHGr59pHK90maW5NTaH_AsWvOlwdsXSOSUSFUVwd8q45ZiA0PLXzmrZJ2F_EBF8h6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b91e9581d.mp4?token=gmEj89lPRaqRbbhmvSdchpeVslvC5cJ0PXn_bYcpqOPf7l17oAIQlLBeESBpNmNFHzgBl_rwCUHPHaFsHEiK7GvD-pKRukEThKoMR8y67U2QfAeHVQFQW1q_vmVCl23mG3Jg4oeH18Jfv5OaPyuWKLpXTy00gDN3houeFI-GgAek6ewG1ZAE5vTXZ74BrK22A9MryhiTuXgHZNZb9kDown8yR8rsliEgTS3UPrM49xqNdpi8GW-RyUeGLLWCWjhPtlGifOaPzcqg9Kf6PkP_rHGr59pHK90maW5NTaH_AsWvOlwdsXSOSUSFUVwd8q45ZiA0PLXzmrZJ2F_EBF8h6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زعفر جنی، پادشاه‌های جن‌های شیعه
😅
حامیان همین‌ها میان کامنت میگذارن که تاریخ مطالعه کنید! محتوای تاریخ‌هاشون!</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/5785" target="_blank">📅 11:29 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5784">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb5c00112a.mp4?token=Ye6sPjTG8VCHs5SmtamsFH5UHP9X5kLc651ROxvTV3uyVq4astxyxpFd4FtJdTYcHqVGvbxXC1tsv6jOFY4XiE_Ito-GIK57YvvlfRMvWYXDANx0fkhQeHF_dLncCrUpMIGhfPUJV9-LXS7XnZyAzYnQTgMFuP8J4aZf5wYXeIgXhM45n6cvkmXeZmP9mXLpE5FidIhKXhXw6X5-A-GHwwYZ95-o-uEmGfqF2o6MeBlKmDsnK34pFmDN9HmPIOqYWg9wwej4ITTPYe4WxVpMdA8RolI3O5fapUOMnoZsmKHdH3_YgDwTmf4FhFGjPyExyVDSn4Z0HMtR1xGWsMnAsg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb5c00112a.mp4?token=Ye6sPjTG8VCHs5SmtamsFH5UHP9X5kLc651ROxvTV3uyVq4astxyxpFd4FtJdTYcHqVGvbxXC1tsv6jOFY4XiE_Ito-GIK57YvvlfRMvWYXDANx0fkhQeHF_dLncCrUpMIGhfPUJV9-LXS7XnZyAzYnQTgMFuP8J4aZf5wYXeIgXhM45n6cvkmXeZmP9mXLpE5FidIhKXhXw6X5-A-GHwwYZ95-o-uEmGfqF2o6MeBlKmDsnK34pFmDN9HmPIOqYWg9wwej4ITTPYe4WxVpMdA8RolI3O5fapUOMnoZsmKHdH3_YgDwTmf4FhFGjPyExyVDSn4Z0HMtR1xGWsMnAsg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زعفر جنی، پادشاه‌های جن‌های شیعه
😅
حامیان همین‌ها میان کامنت میگذارن که تاریخ مطالعه کنید! محتوای تاریخ‌هاشون!</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/5784" target="_blank">📅 11:29 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5783">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/383f2c1b20.mp4?token=Z148SplB2B7xWSN94JP6CxUTKQNVnPr7laP13-6Qat8K37Lr20NX_FuP9iS5BSlNK40T7NlADzHLhQSoV9hzrWfBqUVdVjn1llFAcGXvDu_xH4dNxv8J3Kcv3rfOG_ZJa_JCFUXsminywJF9elD01wvRUIJmXM75PU9sSCCazm_OeHTzKpHQuPx8pJPAWJoiJpXy9s-6Zuh0hsASr1qI8VohcCANGFs3jz1YDXX6p4bPqpHZx9NIybnx7-Js_RzffXxbBhl3STdnNb0aD53uwPkK1AcNqoIuzAxyrPxJKe1iWe8VYq0HldWdBGenY-kh1oq5kSl1CTaivUUaVBYgFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/383f2c1b20.mp4?token=Z148SplB2B7xWSN94JP6CxUTKQNVnPr7laP13-6Qat8K37Lr20NX_FuP9iS5BSlNK40T7NlADzHLhQSoV9hzrWfBqUVdVjn1llFAcGXvDu_xH4dNxv8J3Kcv3rfOG_ZJa_JCFUXsminywJF9elD01wvRUIJmXM75PU9sSCCazm_OeHTzKpHQuPx8pJPAWJoiJpXy9s-6Zuh0hsASr1qI8VohcCANGFs3jz1YDXX6p4bPqpHZx9NIybnx7-Js_RzffXxbBhl3STdnNb0aD53uwPkK1AcNqoIuzAxyrPxJKe1iWe8VYq0HldWdBGenY-kh1oq5kSl1CTaivUUaVBYgFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همش ثوابه :)</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/5783" target="_blank">📅 11:08 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5782">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a9c5c701b.mp4?token=OBhwM6flK5tM_JlkC1NADNv8AhRMZiDao0i7cbvuo8ZdVia8WJxYNqgf11b43s6OQatJ3_vaKdpmnjSk7xzIrtDMGewlECj06-qjrEOYyedTKrjS3OVceWINluvzPruYuoZYbulM2d6S8n1MHiRpP-Y9yK5jh235BruOw9KbCd5-FcgQTNOW0h6t9m08EUTuoKhQc3s9qUGSHAjgnmVc__pbNtXYYNlaVwXzQK-3li1Z6SYbbUlyLo5yNXRM-h5RyPBZ7ToBgx_ZKaRXBb6edDE037gHEs-GvKekg9yN4jwYvd-n8Asvjeqt7M4LRTb6dULXNYl6riPvlqEZOtm6kg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a9c5c701b.mp4?token=OBhwM6flK5tM_JlkC1NADNv8AhRMZiDao0i7cbvuo8ZdVia8WJxYNqgf11b43s6OQatJ3_vaKdpmnjSk7xzIrtDMGewlECj06-qjrEOYyedTKrjS3OVceWINluvzPruYuoZYbulM2d6S8n1MHiRpP-Y9yK5jh235BruOw9KbCd5-FcgQTNOW0h6t9m08EUTuoKhQc3s9qUGSHAjgnmVc__pbNtXYYNlaVwXzQK-3li1Z6SYbbUlyLo5yNXRM-h5RyPBZ7ToBgx_ZKaRXBb6edDE037gHEs-GvKekg9yN4jwYvd-n8Asvjeqt7M4LRTb6dULXNYl6riPvlqEZOtm6kg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آورده فرهنگی شیعه برای ایرانیان</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/5782" target="_blank">📅 09:32 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5781">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KBOomjrjOCDsWqM3YxyJT_IzYIkXeUzVsPLkLIPqX-qq8EcbwPSVSNFRIEzHS0bZqz1dads6Qk9-YxMdfIMfaoIvPdUhYt7hx0lCCaqjRkih0Kqg9cRwTHFdiTU-WMV9hUeLVQEpp1SrIvEAxkPGRhb3ot8WsK6STZp9jaujFS4YwbLl_r56Z-crhlsOVyRH3r2GvHittV390MlQBQzD0SK4rVtSDNbuNFwHmD8aXqKntBPsf-da1gsDbmaKyEwH25KT-dvydkic3vKJ-Qtw2jIzYMR5mCXlDYmTxYsE9yaJZJWtDGxtdjSFuN1zVdUxOytfdV1d2h4Qp6AzgWFLwg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/5781" target="_blank">📅 09:29 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5780">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🚨
جمهوری اسلامی و آمریکا موافقت کرده‌اند که حملات را ادامه ندهد و سه‌شنبه در قطر دیدار کنند.</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5780" target="_blank">📅 00:08 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5778">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/409f2a841d.mp4?token=OXwNs90CyLNNineZWJ21XltHnBP04oy64JSRUPzAKyotzdcSIAzP46BDXpqAjopucfTUCpFCLly550pngBIpwB124HJcT9wsf7gefWoKWtooX1drHyTptyk21EmDAK27Xdk1cbHf8HUiu9c4KJk7QTZ9CaQki_pN1JdMA3JRjlOERk900Y-3FFNJCpEQn2A2MpADdZ5Srsu3LenIXTdr878OTQttBr4Y0FIGYihdeXjAhiH1gORLyjevOgy0Fx1YLsTZOB-gNGqgTLcFoJuH69Qq7Uo5-GNowct2rXd32qONzx68WHU9e_K1bQXyMIfctIYh2nTW6wk3eqstmBnPrw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/409f2a841d.mp4?token=OXwNs90CyLNNineZWJ21XltHnBP04oy64JSRUPzAKyotzdcSIAzP46BDXpqAjopucfTUCpFCLly550pngBIpwB124HJcT9wsf7gefWoKWtooX1drHyTptyk21EmDAK27Xdk1cbHf8HUiu9c4KJk7QTZ9CaQki_pN1JdMA3JRjlOERk900Y-3FFNJCpEQn2A2MpADdZ5Srsu3LenIXTdr878OTQttBr4Y0FIGYihdeXjAhiH1gORLyjevOgy0Fx1YLsTZOB-gNGqgTLcFoJuH69Qq7Uo5-GNowct2rXd32qONzx68WHU9e_K1bQXyMIfctIYh2nTW6wk3eqstmBnPrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش اسرائیل از نابودی یک تونل
در روستای مجدل زون در جنوب لبنان خبر داد.
این تونل ۲۰۰ متر طول داشت و در عمق
۲۵ متری زیر زمین ساخته شده بود و در آن
سلاح نگهداری میشد و دارای چند دهانه
برای شلیک به مناطق شمال اسرائیل بود.
اسرائیل گفته که پیش از نابودی این تونل
آمریکا را در جریان قرار داده.</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/5778" target="_blank">📅 23:57 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5777">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/06f2d554a0.mp4?token=Jm7bS_Rnawgxn_lRz9beNTQpinM6TEp1f5f2EMCvwbZWz6sZj-YWGqWY4IktPRfcl2fi7ksSOhHipIDFizER0GoXVq6FxSKJ-Gme57Z8Xg4Ck31Fw01YHzRJRBKCMN5O1dB3agSE629pbCQeXyLa5DoUBmxUffCJLhH5r2nwnrLlEeOcB6Evl4Yq0p07BHcHHfAnxUKKb7YaSqzW0T_HEpTBdD4d-XmNETnbvtm_CWABWI6Wdt0IFkvSszJkXEHs7xQIZWKX0jFrvFnx-2tQaIEEul1pAw541JXQdD0F3q2lx1TSuLuF0imv1GJtpDDw2Go65PUQMsh_SDGJondEpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/06f2d554a0.mp4?token=Jm7bS_Rnawgxn_lRz9beNTQpinM6TEp1f5f2EMCvwbZWz6sZj-YWGqWY4IktPRfcl2fi7ksSOhHipIDFizER0GoXVq6FxSKJ-Gme57Z8Xg4Ck31Fw01YHzRJRBKCMN5O1dB3agSE629pbCQeXyLa5DoUBmxUffCJLhH5r2nwnrLlEeOcB6Evl4Yq0p07BHcHHfAnxUKKb7YaSqzW0T_HEpTBdD4d-XmNETnbvtm_CWABWI6Wdt0IFkvSszJkXEHs7xQIZWKX0jFrvFnx-2tQaIEEul1pAw541JXQdD0F3q2lx1TSuLuF0imv1GJtpDDw2Go65PUQMsh_SDGJondEpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">منطق جمهوری اسلامی
و تعریف «امن» و «ناامن»
میگه اگه  یه کشتی بخواد از مسیر «ناامن» عبور کنه بهش شلیک میکنیم :)</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5777" target="_blank">📅 23:26 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5776">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RsfFJYc_Jai72unX-aLrzL50NxBBI8eDO9f7DTA6j5YxynGvwpsl5UO2hOL0iC1AnXpnaC53lotXz-4oRQaYF531eVrINrEcE6Qy0gfWCNzZmgQ67lnpXQnbzIdmNnvOVGrC1XvKSPIhkuocPvLS2Obkobwf9FxhlQMao4AAHcGwypKBAmYmLFTwWjkBBVm-a_ZCxO062z4wXyxq_w8wZCl6EBdw45Up68Q5BXcwzqbH_eqgIjP1ltLhVyVH9v6liEZFqYzmBzaXSVTuId3vRuYuUJT6f-qIZfriBS6F7Nsm6eOJhOlAJ4kw6RoTIa2MNXOSL9jQAQBYmiIGkJoVIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس: چاره‌‌ای جز ساخت بمب اتم نیست.</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/5776" target="_blank">📅 19:39 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5775">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e4e9d7782.mp4?token=pRQDhGzNJTDpxIJaUF82pV_Bppgn9wSZchpklFvGMJjn8JT1zgE6N16ERr036wQe4W7UBQj-Vn56-eVTnfxH0pzQ9c47RWzsvtcVVOl36f-NBLYC3G56Q_1wVKAHQtw73CU6-hPpAJYRnOCT7itseiM_k_olq06dtwYxQOUICD9eS6mgxOTzDSu62_jPvmxgmmYhcObmcAfDVBlBneR5bvaABDEqmhjybNlPFFXx8SFKvxp06aqaoE6K-vaS46GO_3MV8h89Y4J3bKu1unDHGcy1VJGcAm5EHXkD0Szc_p6ZgRgeHW4cNRdHKWEzskP1AIX8bndm9n-LUeTAKicl5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e4e9d7782.mp4?token=pRQDhGzNJTDpxIJaUF82pV_Bppgn9wSZchpklFvGMJjn8JT1zgE6N16ERr036wQe4W7UBQj-Vn56-eVTnfxH0pzQ9c47RWzsvtcVVOl36f-NBLYC3G56Q_1wVKAHQtw73CU6-hPpAJYRnOCT7itseiM_k_olq06dtwYxQOUICD9eS6mgxOTzDSu62_jPvmxgmmYhcObmcAfDVBlBneR5bvaABDEqmhjybNlPFFXx8SFKvxp06aqaoE6K-vaS46GO_3MV8h89Y4J3bKu1unDHGcy1VJGcAm5EHXkD0Szc_p6ZgRgeHW4cNRdHKWEzskP1AIX8bndm9n-LUeTAKicl5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تیمی که با بدرقه قاتلان جوانان ایران راهی جام‌جهانی شده بود.</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/5775" target="_blank">📅 17:23 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5774">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🚨
شب گذشته یک عضو تیپ ‌گولانی ارتش اسرائیل در جنوب لبنان کشته شد.</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5774" target="_blank">📅 13:06 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5773">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">ولی ما می‌د‌ونیم چرا شانس با شما همراه نیست.</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/5773" target="_blank">📅 10:17 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5772">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1220ffd18e.mp4?token=GBWi9lGiJA5y-NveKDGwACh8TO0_KpKeiBpIl-QvgTRTGwgTmT5XsXX2T6WYGWfjdtZOurM4Vi8zrQytQg3WQ7jxiwpDKXJpY_E-EATO-a6TpNFz__RA_pKm4qIbOst3iuZbfVjLEr2wo5_vdGGVwyrQBIRWJc-Rp68ZlOY32QiW8BFSWQE26T7L1mXD6mZg0mHBVp5ENN6xQlxXBVHrWnkt6r288XHmivlcNrb6Y0YLKqFryni6qTR1gFzsuDeW2bClIJwML1tbMbbDw3jF7smqkWwa3dh3qOByGZjNSJxmYB7ykWiGaDYSxJ6Zn928Uq3REI9DwFYs9CeWZHKZsg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1220ffd18e.mp4?token=GBWi9lGiJA5y-NveKDGwACh8TO0_KpKeiBpIl-QvgTRTGwgTmT5XsXX2T6WYGWfjdtZOurM4Vi8zrQytQg3WQ7jxiwpDKXJpY_E-EATO-a6TpNFz__RA_pKm4qIbOst3iuZbfVjLEr2wo5_vdGGVwyrQBIRWJc-Rp68ZlOY32QiW8BFSWQE26T7L1mXD6mZg0mHBVp5ENN6xQlxXBVHrWnkt6r288XHmivlcNrb6Y0YLKqFryni6qTR1gFzsuDeW2bClIJwML1tbMbbDw3jF7smqkWwa3dh3qOByGZjNSJxmYB7ykWiGaDYSxJ6Zn928Uq3REI9DwFYs9CeWZHKZsg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شجاع خلیل زاده میخواست گل بزنه و تقدیم رهبرش کنه!  ولی اراده خدا تحقیر اینها بود!</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/farahmand_alipour/5772" target="_blank">📅 09:32 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5771">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d645372fb2.mp4?token=Wzpl_tGNXxFQHYvMllAn4BZnmalIyTFFdybB8jDakyZ6ke_CbwRzqsiIwzDlHi0qgjptb4jH7Yu3WrPmltaSj8fpYUNZVa2FWosEGuPk7Rg9HvbMX_ltwm5ICViPE87_olNPuJRDeljJ_fZSfHEqh4Ry4kmJoLX6HA1KYUxfh5yJIxI2lgeVxKoFlawg5xsFTYAfyoL-L5-yJphk15hoZKdsH_0-MzFxWNlhKdQ1H6e6BB9zJeAbZb4EK6qjhQfVV4WmrsC1-MQnZXPrjiN2yC-LX247pjyrPc6RV235gsGgPvvW2dEMEyxDpMRchOKbcAqF5UkMTvTtvk2GI2Uz5DzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d645372fb2.mp4?token=Wzpl_tGNXxFQHYvMllAn4BZnmalIyTFFdybB8jDakyZ6ke_CbwRzqsiIwzDlHi0qgjptb4jH7Yu3WrPmltaSj8fpYUNZVa2FWosEGuPk7Rg9HvbMX_ltwm5ICViPE87_olNPuJRDeljJ_fZSfHEqh4Ry4kmJoLX6HA1KYUxfh5yJIxI2lgeVxKoFlawg5xsFTYAfyoL-L5-yJphk15hoZKdsH_0-MzFxWNlhKdQ1H6e6BB9zJeAbZb4EK6qjhQfVV4WmrsC1-MQnZXPrjiN2yC-LX247pjyrPc6RV235gsGgPvvW2dEMEyxDpMRchOKbcAqF5UkMTvTtvk2GI2Uz5DzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شجاع خلیل زاده
میخواست گل بزنه و تقدیم رهبرش کنه!
ولی اراده خدا تحقیر اینها بود!</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/5771" target="_blank">📅 09:31 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5768">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qCK8MudohmsVETevv1kYQCgctlKoSW_kjgl65qT0k2Uuycmnfw8UzehEZkJhpvdKSHKYJrDnp4eM-3ToBE4Z6bSlvY5iSEYmVEzcJuQfqOCcWBXrboQXe9heiFuz2DexG7DQUsntuRD_fq7zOqHHcd6QWF9bxwxGBsvPgLYLNtH6wziPwymWDk1OOOpZX4svFh1V8DRP6YPhhQ8k8KcPhrCaxBjkiPkvEUvlTcRSdqL6XiuvuU5KJWPaw5nfWgCme9MsQQFN2f4X821AoD-nYV09K6iWwmMMMyzTgaPRQ4CVdr5w20z2jiJ-rB3_tC3VZV8vjgmKBulj48mwAbCjug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/h7gHE7t83uZWgwvXrTBAYQvvIYfd1F5WTnpQ81WWHBDaAdRMumNLhwLop1Yzm8QI1Gz_V3ProEPMqGrPvIULh9BUo9EZDw8NoCWb3f_UBzzeFbIZIOfWXieo2IOJeNipD5JNPbGf5t0RYumedydWOY5F4NMVMCNYCQBMcT7FS5s0cMll7RTzDZ3tczl0OGl0t4w33h0v3_t6VY-36fM1S8-Itn9gqlXNyfTJmSfGyvxUYnGe0AreXyJriwsu8lOnlEm59Vy3eOwnapAH3Jphblwotgl49YsInqZuq3ANXEKVmdJi0JzKzk3WYo0JComYMwCQB-e0EAvHKXn-AB_KYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/i7GG9cXZBTfRNxgZjx2lFilLiQGC_OpvCj9MLnqzoWuTony9HUG94nu5Pcq7BFcdgLW1oLIDFiWLARaOlb9NKXijcOfCB6lWZiE52WowBQZ9vrE1__FYGkjD8yqLe6AEFoSrcXdIGBXS0SzxZyRn2JQLP-L_bQQVqdX1R9myGqzuXC6liICc9irWqyMgSx0JlWfKXSGraq5LujkoltbX0t1nOhliToT1o6Vf1BLcFTEVyIccIGuOqo2aQdYzU7i7sAgYB4kvC_Z4xEzXhu7i48zVzUGkrZa7ocRCZsCiJwWHUugbLdkbKN_PfnQzPMsLl4WB2A0hRU02Hgt2nZg8Jg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">در جاده فرودگاه بیروت، بیلبوردهای تصویر خامنه‌ای رو حذف کردن و به جاش تصاویری از «اول لبنان» زدند،
که البته دیشب برخی از اعضای گروه تروریستی حزب‌الله رفتن و تخریبشون کردن.
بالاخره زندگی و حیات‌شون در مزدوری رسمی و علنی برای جمهوری اسلامیه.</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5768" target="_blank">📅 09:26 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5767">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">تیم ملا</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5767" target="_blank">📅 08:52 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5766">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/10689e4ea8.mp4?token=Lm19J3Ii1EqU6z9Ifk51aljY-i0auDpJgPRQxezxo48uCz4T5IyaLdUjGRqefWuMmRjd0lSefYbJIQXS645FB8fv4GdSE1XrcC64vCx4mY_W7XMjUVdB9-9rU9Mhlsc9hZKrGqlCm5fsVwEAO5hQxTvSSy5RnLxqDdY6tlCBJAJYXGSHs8lIQJgpV7zD3tlpYuC0EUBNngd0ZrzUndnCaeVqbiDJS6e40SGOuMd_1d0DO5W4wzL8jq0RwOdXtNnBsyz1oG2EcTBPWuEUQSy183Sa4jIzdBYtcpc9zd0EEbXb1cT1mzcpldQQMlDQyVAtLlsxVj7-af1kTt2aS9zKVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/10689e4ea8.mp4?token=Lm19J3Ii1EqU6z9Ifk51aljY-i0auDpJgPRQxezxo48uCz4T5IyaLdUjGRqefWuMmRjd0lSefYbJIQXS645FB8fv4GdSE1XrcC64vCx4mY_W7XMjUVdB9-9rU9Mhlsc9hZKrGqlCm5fsVwEAO5hQxTvSSy5RnLxqDdY6tlCBJAJYXGSHs8lIQJgpV7zD3tlpYuC0EUBNngd0ZrzUndnCaeVqbiDJS6e40SGOuMd_1d0DO5W4wzL8jq0RwOdXtNnBsyz1oG2EcTBPWuEUQSy183Sa4jIzdBYtcpc9zd0EEbXb1cT1mzcpldQQMlDQyVAtLlsxVj7-af1kTt2aS9zKVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فقط مدل گزارشگری فوتبال رو!!
یه کشور مسلمان [الجزایر] داره کاری میکنه که یه کشور مسلمان دیگه [تیم ج‌ا] تو دور بعدی باشه!
‏یهووو یه کشور مسیحی[اتریش] گل زد و اینها هم حذف شدن!!  :)</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5766" target="_blank">📅 08:43 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5765">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17301f18ad.mp4?token=QULzo3rvzxGgtlWKbr09sAjSPdBNLTTD6v4ZnFO0pB-mF8HJbDAFMF1UVBRtzUIfdobam9wrfnicbWw69Sa9ne42x177tzGSmC5cVhwpisHBfiSUOOJNMRHklUGbL7FUhFewM8f9UTea7YYxWrIZVVwR2YwADLb4ZBaVviEU74dHdhA5HZyOfa0mViNiNFiufRGoxSt82afiYFnhqWJlfy8eqPPnJdmJuhT-Fatqf3-Dpm03dm2AfkLJwwDb-VDd3qa_cEgejAl-1W35A2EifYsy_-CMQC17meJSicJSEsXVftGuTO1-P5trXE66yUnnJF6QXMs7wjDqmRYuDLPLaaXkpzHgrPDSxWGEw_ZL9P451xGFZZxKyJ2ZpE-6bXMCeIZbZit_S2i_fzhFfQ-UYhmRGod9SXATvXIRJzHzpE9t4PKU97GDn2ZMPNO9BL-PHWThwgRtElhM8PQeHA2e81r3JsPMvlDf9gAm_Nccrsb2nl7mp53bc29uNx4yukVbEV0ULFid9CtNvaVi_Ti0XjPtNwjv4CJU434QEe2E0Yhq2VwA-3-ktH_CT9gnVP6AJonhot-s5fjiZZ-iGN24sya7nBJffU4oePytxLmLl3v9lPOcuB0XICLufVZp3Ev30TercbVM8-94x31Ufl5PJljTmLBMZ78sEdJkbfUs9NI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17301f18ad.mp4?token=QULzo3rvzxGgtlWKbr09sAjSPdBNLTTD6v4ZnFO0pB-mF8HJbDAFMF1UVBRtzUIfdobam9wrfnicbWw69Sa9ne42x177tzGSmC5cVhwpisHBfiSUOOJNMRHklUGbL7FUhFewM8f9UTea7YYxWrIZVVwR2YwADLb4ZBaVviEU74dHdhA5HZyOfa0mViNiNFiufRGoxSt82afiYFnhqWJlfy8eqPPnJdmJuhT-Fatqf3-Dpm03dm2AfkLJwwDb-VDd3qa_cEgejAl-1W35A2EifYsy_-CMQC17meJSicJSEsXVftGuTO1-P5trXE66yUnnJF6QXMs7wjDqmRYuDLPLaaXkpzHgrPDSxWGEw_ZL9P451xGFZZxKyJ2ZpE-6bXMCeIZbZit_S2i_fzhFfQ-UYhmRGod9SXATvXIRJzHzpE9t4PKU97GDn2ZMPNO9BL-PHWThwgRtElhM8PQeHA2e81r3JsPMvlDf9gAm_Nccrsb2nl7mp53bc29uNx4yukVbEV0ULFid9CtNvaVi_Ti0XjPtNwjv4CJU434QEe2E0Yhq2VwA-3-ktH_CT9gnVP6AJonhot-s5fjiZZ-iGN24sya7nBJffU4oePytxLmLl3v9lPOcuB0XICLufVZp3Ev30TercbVM8-94x31Ufl5PJljTmLBMZ78sEdJkbfUs9NI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/27a845337c.mp4?token=njLh5i4ZH0kcepXTggrRJb3Xm3DwZ7V-S5nR6PHRcyEPS__DPEYV2U6C5qnOSIyXqoIBoHV_0RtEIstP8ZjxfTH-YAOiE2bnq6EYX2m5Wr3f-AJnZS2CqFhU4AjPulmo2nFYAi4CzMwoh35D5t_CgnR7wKZFenIdLpidML4X7V6_AwBxumBfkA85SEaOLQBnrEelqX4Mw4Y0MUAUd0fsGtEVGZB1ipMGmYlIUl5-WqVsD4nZtWdg00gMwqCm9cvkjQkVq1d5kEKu7MlmBx4OWL0hwuiDCl6PVCyXn6FDDeiz-2Ji7iifiDyoZcvDSJYJgqK57fhc-2D7Ubyn0R0XzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/27a845337c.mp4?token=njLh5i4ZH0kcepXTggrRJb3Xm3DwZ7V-S5nR6PHRcyEPS__DPEYV2U6C5qnOSIyXqoIBoHV_0RtEIstP8ZjxfTH-YAOiE2bnq6EYX2m5Wr3f-AJnZS2CqFhU4AjPulmo2nFYAi4CzMwoh35D5t_CgnR7wKZFenIdLpidML4X7V6_AwBxumBfkA85SEaOLQBnrEelqX4Mw4Y0MUAUd0fsGtEVGZB1ipMGmYlIUl5-WqVsD4nZtWdg00gMwqCm9cvkjQkVq1d5kEKu7MlmBx4OWL0hwuiDCl6PVCyXn6FDDeiz-2Ji7iifiDyoZcvDSJYJgqK57fhc-2D7Ubyn0R0XzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
تیم فوتبال جمهوری اسلامی رسما از ادامه رقابت‌های جام جهانی حذف شد!</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/5764" target="_blank">📅 08:26 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5763">
<div class="tg-post-header">📌 پیام #36</div>
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
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/5763" target="_blank">📅 08:18 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5762">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🚨
🚨
حمله به جزیره قشم
امشب، دومین شب حملات آمریکا به منطقه تنگه هرمز است.</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5762" target="_blank">📅 01:40 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5761">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P6Xb5yKfwJ-o4ywm49hqpe3N5zfngkkIioRKnDKqy_-INjFqmTwdbC-Kezy7Si4i5fdDfS5OegZiCFK2o1JkEyHICm2eoA5mm8Zc4R4HEhrSVZAu5NqgSFw0aznTFKp69bgMc3WgMi-lmTCBzhivky0QIGy6xOJhgFCdVV70rZ2YneD0Pg9Luz2SwTujXVvnLoYJ4I52qrCN4YdoVNMVj3By6ciFbk2BkMFYQeQyAFIWM_4QqUNCyQks31pWr2HBcptyLkEQZBZbI1BnHihy07DFkuoGJAiES8Og4h4cyKFBiJSrWCD2M8xBgWfR_o6857mqcjXDwp29LFXtr5bdZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیانیه سنتکام : به سایت‌های ذخیره پهپاد و سیستم های ارتباطی جمهوری اسلامی حمله کردیم.
متن کامل :
نیروهای فرماندهی مرکزی ایالات متحده (سنتکام)، به دستور فرمانده کل قوا (رئیس‌جمهور آمریکا)، در تاریخ ۲۷ ژوئن حملات دیگری را علیه چندین هدف در ایران انجام دادند.
پس از حملات دیروز آمریکا که در پاسخ به حمله ایران به کشتی
M/V Ever Lovely
صورت گرفته بود، به ایران فرصتی داده شد تا به توافق آتش‌بس پایبند بماند؛ اما ایران با پرتاب یک پهپاد انتحاری در بامداد امروز ساعت ۴:۳۰ (به وقت شرقی) که به نفت‌کش
M/T Kiku
اصابت کرد، نشان داد که این مسیر را انتخاب نکرده است. این نفت‌کش با پرچم پاناما و حامل بیش از دو میلیون بشکه نفت خام، در حال عبور از نزدیکی تنگه هرمز بود.
نیروهای سنتکام امروز در پاسخ مستقیم به ادامه اقدامات خصمانه ایران علیه کشتیرانی تجاری، دست به حملاتی زدند. هواپیماهای نظامی ایالات متحده زیرساخت‌های نظارتی و جاسوسی نظامی، سیستم‌های ارتباطی، سایت‌های پدافند هوایی، تأسیسات ذخیره‌سازی پهپاد و تجهیزات مین‌گذاری ایران را هدف قرار دادند.</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/5761" target="_blank">📅 01:27 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5760">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🚨
🚨
اکسیوس:
‏ارتش ایالات متحده در حال انجام حملاتی در منطقهٔ تنگه هرمز است.
این حملات در پاسخ به حمله جمهوری اسلامی به یک کشتی تجاری است.</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/5760" target="_blank">📅 01:10 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5759">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">‏خبرنگار صداوسیما در سیریک:
‏دقایقی پیش صدای چند انفجار شنیده شد.</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/5759" target="_blank">📅 00:56 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5758">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0cee64931e.mp4?token=M4lB4JLXoCrTgUWi7_QH_ctNglzJHF4UCrLsHZjQfGGznLYf00LFmi_o5rE8w2tj8zwuZqX-0cx-Ut6WAlRr7Spk0d7ladt8Pz-5Y93WLPBwb2EpgkJvm5DANDIq6_hXLMmqU7-20JZ8jXVJxoShcLF9sK2ZUAoj8PCziJAX6hx4DuosgXJ0uw2rv2FEurj-enwhhgOLxrVqYnurEKogJEM5MmdEH9Fg0FsFQanfP21l4eIbueLVu6KIFovLyrael5W8tZyjMoQs7sO7KdGEgydJH2zzXLgD-SntKeSdztMuPrIDZgE6o5jL0hylWVlMCubiVm6TQItyIWjtdrKXHCWg3mysgFwQASh0SybrcjzlKqhCJ84Xqrr3KUVmIIQSc1-uyeCkb3R8e0I5kL-REZ7iIqneIAaj4MqHn_sh5FC7LwrhlkgaPMPnmw64KzLr4WLNQK59LlUCEB9XiWahDX-Nf29cIGLgsKDrWkbZt1rbgBJSXynSkMKCMMwhYSHyvnpNTR8UqU3i72kx4XykPMSzEdho_iJHyYeFZ4ISd_YbnVyn0btirIH0LABrD9ZNugAML88uxx13rY9E9XZ8lsCRQ8SwQdm_szW_JsZb_riuwjy5GeL-omBkuM9DaxrURxcXPvCUO_W8qeOELIRKtP-LAlEtllmlXyFt1KsgEoU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0cee64931e.mp4?token=M4lB4JLXoCrTgUWi7_QH_ctNglzJHF4UCrLsHZjQfGGznLYf00LFmi_o5rE8w2tj8zwuZqX-0cx-Ut6WAlRr7Spk0d7ladt8Pz-5Y93WLPBwb2EpgkJvm5DANDIq6_hXLMmqU7-20JZ8jXVJxoShcLF9sK2ZUAoj8PCziJAX6hx4DuosgXJ0uw2rv2FEurj-enwhhgOLxrVqYnurEKogJEM5MmdEH9Fg0FsFQanfP21l4eIbueLVu6KIFovLyrael5W8tZyjMoQs7sO7KdGEgydJH2zzXLgD-SntKeSdztMuPrIDZgE6o5jL0hylWVlMCubiVm6TQItyIWjtdrKXHCWg3mysgFwQASh0SybrcjzlKqhCJ84Xqrr3KUVmIIQSc1-uyeCkb3R8e0I5kL-REZ7iIqneIAaj4MqHn_sh5FC7LwrhlkgaPMPnmw64KzLr4WLNQK59LlUCEB9XiWahDX-Nf29cIGLgsKDrWkbZt1rbgBJSXynSkMKCMMwhYSHyvnpNTR8UqU3i72kx4XykPMSzEdho_iJHyYeFZ4ISd_YbnVyn0btirIH0LABrD9ZNugAML88uxx13rY9E9XZ8lsCRQ8SwQdm_szW_JsZb_riuwjy5GeL-omBkuM9DaxrURxcXPvCUO_W8qeOELIRKtP-LAlEtllmlXyFt1KsgEoU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جاوید نام ۲ ساله
💔
‏فرزند ایران و جان فدای میهن، جاویدنام علی محمدصادقی، کودک ۲ ساله، روی شانه‌های پدرش بود که با شلیک گلوله جنگی کشته شد.
‏پیکرش را همان شب تا صبح در برف نگه داشتند و روز بعد به خاک سپردند.</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/5758" target="_blank">📅 22:09 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5757">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D0nqB49AarjaY7yCvWbp1Tnb3Qyw0Ei_iLgbCJnxEaE8uN1Xuxmajz2uohKfOZTQ2MhsuzRHHG-PXyvqM7GEQCaUsG-3F8qconrvLF4fViTJczO2XOd0zDWLqTUs2Rrcg3wsuMxf3ulSKDitI930VJw09EA0_EHk32LLFTbfQCLN6iWfCNfx8CEKOV2aAL3jP0pANKLgTeTfRp0C3ENizUCaXYgRGKEYzwfGrqlZX6xlPwVRMAyhd2FPDvHu8MMp9YIvKtwa9Txw4cmSt5d-maMKFQqemU-8H1akVvVsgQjRxlgVzZz8QKRtrh_wh_CbVm8OR9jAnZny_9InUpJ22A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
پنج حمله هوایی اسرائیل به نبطیه</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/5757" target="_blank">📅 20:23 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5756">
<div class="tg-post-header">📌 پیام #29</div>
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
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">دبیرکل حزب‌الله لبنان، توافق میان‌ دولت لبنان و اسرائیل را که بر مبنای آن حزب‌الله باید خلع سلاح شود و سرزمین‌های لبنان تحویل ارتش لبنان داده شوند را رد کرد و بر ضرورت نگهداری اسلحه تاکید کرد.
حالا این اسکله براتون چی کار کرد؟ یه جنگی شروع کردید و یک پنجم خاک لبنان رو دادید و فرار کردید و از دنیا خواستید بیان آتش‌بس برقرار کنند.</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5755" target="_blank">📅 16:48 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5754">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db5841aafe.mp4?token=koQ-5nMRGSaiIKLsmfo2letRyVh2vW1XBXuqp7bYKJ9gERDClR3YgExF_QIP9ZHXKs9zBmO7RLxTNI2AEQnAP7EVWeQkNNOfjEWMCvV50uvC-j3-qNkidaCRmDQ7cgO_BXjwtcF2kNohBkrZ84sp-O2wFns6rYrFvU23BYyZJd6XxGjUfdmdow8AM1FF1B4WBX7rNxlEckY7wKrJ-ogZnMaBAe0l0dQxyoPRuw1WZa9YLlcM6O_tQSxoG63wlnXsQ6_dFsim7S7SzvIiXIn0EagQsB157xH1y4oGmTywlCk3QSvvSefvY5rkggx4bVJIqZpd9W9L7XmNZjOPIF4eDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db5841aafe.mp4?token=koQ-5nMRGSaiIKLsmfo2letRyVh2vW1XBXuqp7bYKJ9gERDClR3YgExF_QIP9ZHXKs9zBmO7RLxTNI2AEQnAP7EVWeQkNNOfjEWMCvV50uvC-j3-qNkidaCRmDQ7cgO_BXjwtcF2kNohBkrZ84sp-O2wFns6rYrFvU23BYyZJd6XxGjUfdmdow8AM1FF1B4WBX7rNxlEckY7wKrJ-ogZnMaBAe0l0dQxyoPRuw1WZa9YLlcM6O_tQSxoG63wlnXsQ6_dFsim7S7SzvIiXIn0EagQsB157xH1y4oGmTywlCk3QSvvSefvY5rkggx4bVJIqZpd9W9L7XmNZjOPIF4eDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">:)</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5754" target="_blank">📅 16:33 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5753">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f038d1dce.mp4?token=byoujczRJ-S63YiACWWeUuyGEiaWZzg7QNIhUDC14ESJe35PtVab6HGNm8niftCZAdM0p-PzBIBY3wcq4Vu_jfXk2N8UhDPxsr_m01h9ffz7qTGSTbE_FtAPiRtD3omXq2AZvSOLOKUAkQE_DrCTytGPd4IhssMNDzPXMdvzkG66yJMDuDGefH405Va_e6BGtjlZ1BsLDvTdy5cbNSLd8DRi4fWk74Yvi5WJZMUCGoqeY7Mn-InEWWd9jlPhLb2TTBbD8wjz0targB1DIiKq9U1Ov5N8nqtMhiBYBAW5YlCp-4XfFXiS5o1EvjvjZ9o6zlMZjKghxMn_cKN9U58gXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f038d1dce.mp4?token=byoujczRJ-S63YiACWWeUuyGEiaWZzg7QNIhUDC14ESJe35PtVab6HGNm8niftCZAdM0p-PzBIBY3wcq4Vu_jfXk2N8UhDPxsr_m01h9ffz7qTGSTbE_FtAPiRtD3omXq2AZvSOLOKUAkQE_DrCTytGPd4IhssMNDzPXMdvzkG66yJMDuDGefH405Va_e6BGtjlZ1BsLDvTdy5cbNSLd8DRi4fWk74Yvi5WJZMUCGoqeY7Mn-InEWWd9jlPhLb2TTBbD8wjz0targB1DIiKq9U1Ov5N8nqtMhiBYBAW5YlCp-4XfFXiS5o1EvjvjZ9o6zlMZjKghxMn_cKN9U58gXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جشن و شادی در غزه
در پی‌ موفقیت تیم فوتبال مصر
در برابر تیم فوتبال جمهوری اسلامی</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/farahmand_alipour/5753" target="_blank">📅 10:20 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5752">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b07e212ab.mp4?token=S-E3Jn6BWRhRePK96ZRLrsJOCCnKCBSb8OntXFzhc6ClXSZlznTONnBq6-nE2gFvKp7dqhzRZ3H_IBHODtks0Neaa7hhJAP9HH9kzPnSItbw7d709MM-UpYgUM5e-ZV1psD23HY25vw9KscwKqbVWh9VOGq1AbkwWeBA3tiIZJHqRDtc6Z0ti0VXVNQAckwxXvnc5_DR6oAnMIrFnDfymtx7nvf4q2yuyy092tzDx7LWpwsjKQ6yidoTGcc9T8dXShkN12RsSp--A3AGcTdvFW4MMcmRxofv_ER-Ypmn24eIdDUc8O-m6SbuwvE-kBfNDDjVpA-vIvXfGFdveDHrDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b07e212ab.mp4?token=S-E3Jn6BWRhRePK96ZRLrsJOCCnKCBSb8OntXFzhc6ClXSZlznTONnBq6-nE2gFvKp7dqhzRZ3H_IBHODtks0Neaa7hhJAP9HH9kzPnSItbw7d709MM-UpYgUM5e-ZV1psD23HY25vw9KscwKqbVWh9VOGq1AbkwWeBA3tiIZJHqRDtc6Z0ti0VXVNQAckwxXvnc5_DR6oAnMIrFnDfymtx7nvf4q2yuyy092tzDx7LWpwsjKQ6yidoTGcc9T8dXShkN12RsSp--A3AGcTdvFW4MMcmRxofv_ER-Ypmn24eIdDUc8O-m6SbuwvE-kBfNDDjVpA-vIvXfGFdveDHrDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش لبنان برای برخورد با حامیان گروه تروریستی حزب‌الله وارد خیابان‌های بیروت شد.</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/5752" target="_blank">📅 02:02 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5751">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🚨
🚨
🚨
حمله ارتش آمریکا به اطراف تنگه هرمز  ‏فرماندهی مرکزی ایالات متحده (CENTCOM) اکنون تأیید کرده است که هواپیماها در اوایل امروز، 26 ژوئن، به تلافی حمله پهپادی دیروز ایران به یک کشتی تجاری در تنگه هرمز، حملاتی را علیه انبارهای موشک و پهپاد ایران و همچنین سایت‌های…</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/5751" target="_blank">📅 01:17 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5749">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o1hY0MFpLN-nQY_fXSnIUcpvTnYc2uLVxJTMZJugI4PMP3Yky0tWp02ryt4b1EUjmhj3UIB8ID6KsuORhXFoXcVOXhvcERgXmuxH9t8nF1oadSAy9dx_muUuAJzLJvD-_HRZ2kyjhU-7tb_JA6E4TAklk-JO6VBHWB89nob4jRdaNcUGY0-5QeXy69qLTz6SU_ntl8mkm8TE5HvSdxvKcnmkvVtpvsPKS08XJdZagxb1WsyP58fVah7d_XvgpGjvvtmr5o9SjN9ExP4w27V9n-jfPo0c7d8V7gzSyObS6JjGR0CWaoDTDtAMLVc_l_FTq22jMHvuEEpns0pAJAn6rQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/farahmand_alipour/5749" target="_blank">📅 01:02 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5748">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B4BDLsvSTsTGzLgS3-RxrOxoBooxCaGJf1Ve-frw1UfH7mXlSPN4vp3QSAm6bzWR5pxGr7LkX3Va-AtWIGi4JapVEGmJO8_QgrU5tgsZ8Ul8K4oDZoo1Y6eYjdrN-B3uXH8Uqq3GxVDc4hCq_WLBbDiku6vCPcdnSz_P5PcovKkkF9M-G03n3ZhoqoZY38uBUiXtpNtguKLHKa5KBV1Uk5aD0Jv9p2sWpIwtgRyQje5kddAgFuKWGfzoXZCjuXCNR_jkzVkTTRA8uhdvoEmTTjP6LfvuOuhJPKX_KsqKQfzbs7EaAtJHWBNZBdgOzw0lcVc3OV1FPs_g0BHcZzhLYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش لبنان برای برخورد با حامیان گروه تروریستی حزب‌الله وارد خیابان‌های بیروت شد.</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/5748" target="_blank">📅 00:59 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5745">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e245d71920.mp4?token=QqVaG-h1qHxmDsEf2hjUf1v9y3QflQ6lnwJf-ev_quksj4F-08RkgR2vWtkP4BLP_oaIrTj58pTsiNf_-zhIsm7cb4BfNMCF3BxmtC_bFcvbI_Sf9z4DZeeEybMHoms88XuzTXMEHkP4363Vwi7H0kI-99uuE6u8X8V5ngEtBfGNIMGAxapZecZ5zzrQr95pHY5X-eghVNubKxXdo0DaObuyu1I2FvtPOl6bk-vYiUv-eyWjMJ1Fk4HWXhPtbUnQV3bYOToDtmym7JocRW9AWvumnnaiIlQtDR9E8bl17COAWGHuQtm_sQjVJOtjbHdx-Q0uvnEJR6wXQnFdl4--Rw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e245d71920.mp4?token=QqVaG-h1qHxmDsEf2hjUf1v9y3QflQ6lnwJf-ev_quksj4F-08RkgR2vWtkP4BLP_oaIrTj58pTsiNf_-zhIsm7cb4BfNMCF3BxmtC_bFcvbI_Sf9z4DZeeEybMHoms88XuzTXMEHkP4363Vwi7H0kI-99uuE6u8X8V5ngEtBfGNIMGAxapZecZ5zzrQr95pHY5X-eghVNubKxXdo0DaObuyu1I2FvtPOl6bk-vYiUv-eyWjMJ1Fk4HWXhPtbUnQV3bYOToDtmym7JocRW9AWvumnnaiIlQtDR9E8bl17COAWGHuQtm_sQjVJOtjbHdx-Q0uvnEJR6wXQnFdl4--Rw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حامیان گروه تروریستی حزب‌الله
در اعتراض به توافق دولت‌ لبنان و اسرائیل به خیابان ریختند
بر اساس یکی از مفاد این توافق حزب‌الله باید خلع سلاح شود!
اینها مخالف خلع سلاح هستند! تاکید بر مبارزه مسلحانه با اسرائیل دارند! جنگ رو شروع میکنن و بعد سریع از همه دنیا میخوان بیان مداخله کنن برای آتش‌بس!
خب مبارزه کنید!</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5745" target="_blank">📅 00:49 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5744">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZtlcrSCITPqxnK2OHCdGADbqMU2XfuhdDM5md6Gq0NeEYtKHFThVSiMkAjXrbUR3zwPeM6gN8a-CNXZ5u50SUMHnjjZG-UlaLe4hHsq5azJb4TY7p9MiAim8jYX5npb6MA6_kbhUnsKSu5NCiJidj9501cU0OFkg3T85bk15i-m1ejurmERn6gqXitbXBG8VVrWjfU7Sb32Fhi-R4OSHtI5yKnmsNRyRl2h6oPWIHuwBY9VndKjJbXOyA7dl_Sne1pVpM2Z7udlKsHwwRFO6LbbSe3iPwVQx-B3XiwLUEOGCFRJBpxwaZUD3X29S_ryY0cRGsOCbyWwehpS-mh88RQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/5744" target="_blank">📅 00:31 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5743">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l3r85Ihjs8H35iUxzMo2qncswHbJPhagiHByYa2M6tlWelZcuhypOK5iL7FLfYQUnux9gb1jXUQ7ErGfJ3AUEcYLeuWxRgJW26sr0bYMkmNEr4ZhWOEk72n4P1yqIBSlc0tbYGL-65bf_COA1b2OgJuzZ1eXLQKaqJf__xdSw4-XbDL51nBu55Eg-3gZTU1-10Kc-mH-mU1FcrHBXQP-Ris3qAQag7QgZmjsqVWvlR27wIeVFi6YkjRF9necKyRyKAdSrSpTodeozBbJtQhyDZlaNJJaXartkDzXBU4r-TMa1KPwryMHbJl9n72qBZw4JR_dlzf6n-cVtzIhfGTPDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
حمله ارتش آمریکا به اطراف تنگه هرمز
‏فرماندهی مرکزی ایالات متحده (CENTCOM) اکنون تأیید کرده است که هواپیماها در اوایل امروز، 26 ژوئن، به تلافی حمله پهپادی دیروز ایران به یک کشتی تجاری در تنگه هرمز، حملاتی را علیه انبارهای موشک و پهپاد ایران و همچنین سایت‌های رادار ساحلی انجام داده‌اند.</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5743" target="_blank">📅 00:27 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5742">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac9a1f1d75.mp4?token=kyEmjI2F0SRhUKDoAgy0Dhhx53o-caK-C8v7erfleivmMw7005_W0bi147SJd1oans6KWhbfc8EcJhImiXNNHddAdxYJxU1ckPWC17Zec3uDCY1U36-8gBF_um23vuWZu_7BPMLuEzmtRRE9Bw84tCauNhlK-3qgfxvbnPaXL6mfwhDKPMhb7KrGwOeIva2q2gn6nwwOoRhKazN9L1l-C2tWn6_9N6iUXvwjtpOJjpwJGK08SSniBWZag4xY0bBCfah9sopc6n88Gh7Fdqy5GVLFZWQF3u-mo71IO4jIWDcxJj_c32Sax9XQhx0VtXqS49XwNGRRl4fsAx8ov5zEYylYj_edild6XxwMldfU3Kl9hnGJsf1DiLC8VqFAZM_guqqm5TT4o0oPLQwefeX2ctrYbyfIH3RM1AXNCl8p9CfVvRYbAEmSUHPukPWBGxF3pEODqiIL4eta2WKkf88sVDkDmg1DN9cq5s3wO4a6Zjz-sxGbQy5okGHfVZdY6NTnIhkgTxSOqqR3yg6kaZkRuay4h0i-M7GJ0wRYKmV7R4OE_r6bEwNA8P9aMOObGSh28FCX-p93ra0GQXqLQD5t63F0IzuUEB770fvwqN_89hs5Vrcdnkg_gVYPMOL-bblD1xhRjehr67kpqqobE5QWV92dCEcYBOhm0vCROd2OvBk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac9a1f1d75.mp4?token=kyEmjI2F0SRhUKDoAgy0Dhhx53o-caK-C8v7erfleivmMw7005_W0bi147SJd1oans6KWhbfc8EcJhImiXNNHddAdxYJxU1ckPWC17Zec3uDCY1U36-8gBF_um23vuWZu_7BPMLuEzmtRRE9Bw84tCauNhlK-3qgfxvbnPaXL6mfwhDKPMhb7KrGwOeIva2q2gn6nwwOoRhKazN9L1l-C2tWn6_9N6iUXvwjtpOJjpwJGK08SSniBWZag4xY0bBCfah9sopc6n88Gh7Fdqy5GVLFZWQF3u-mo71IO4jIWDcxJj_c32Sax9XQhx0VtXqS49XwNGRRl4fsAx8ov5zEYylYj_edild6XxwMldfU3Kl9hnGJsf1DiLC8VqFAZM_guqqm5TT4o0oPLQwefeX2ctrYbyfIH3RM1AXNCl8p9CfVvRYbAEmSUHPukPWBGxF3pEODqiIL4eta2WKkf88sVDkDmg1DN9cq5s3wO4a6Zjz-sxGbQy5okGHfVZdY6NTnIhkgTxSOqqR3yg6kaZkRuay4h0i-M7GJ0wRYKmV7R4OE_r6bEwNA8P9aMOObGSh28FCX-p93ra0GQXqLQD5t63F0IzuUEB770fvwqN_89hs5Vrcdnkg_gVYPMOL-bblD1xhRjehr67kpqqobE5QWV92dCEcYBOhm0vCROd2OvBk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اگه خورده گرفتن که چرا میگید سگ هستید …</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/5742" target="_blank">📅 19:53 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5741">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fad365bb7a.mp4?token=FGbthytExUGlv7VVAMnFmTdW2bUIzMJvOsp7pkwDL8lVYtKO2oDVE5D20Q0KsyG4SD44BmJ8_L-WU2g-cP21D4bZBnOLcyzxmCcSX2g6dvqZp0VrN-onBZwhIyyNrLnCckiy2Smdrk9uUiHTG3OSBdq6akCLIGCKZK6nv4R0g8NT2C8t4zRz6uO1HkQ6KBEWVHz-OMvyBq27flYBTNYdPEdpFxJEhy-bHYGI66whvt5myxonPcRIA4fgN4jCCtovGNP20hJnbpBqKeUngG2-ZJxKxipqTzLHgP-GLTq_eRqRKd9kIMfYNQxHa7JzE_3Q7-3O-dKm6q2MH3r7el9ETkAgn0NSpx2-GDcZmMfkojhq1Rv1wQXq1Q9-Oyb9H6IZ35OGLwlcz4phYBpovxKlBAZIdfrNLqLECP9l-d6sX6evW9CT7lpQhGA_AsMDAi98MO3LqoecaXzKp5r5LksWYh6NAPU_FscnrgQ9SDwAa3LH6COwu6uKnZInIad2CUGpl6zVkSYdJdPMGdjOIv6jYwfQRIk5TwL0VUFbAQbV01NOOZ_09-5QV2atTa_T088NAJyAoXBFT1ES9NRuDEPIpYYSzSNJcpg5W8XJLpWmyIQmxuIlbdgnELp-c46sC_02cEwsGDckWw4MEz1uLG2tMHMKoUm-c5SNDZBErH8MlOI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fad365bb7a.mp4?token=FGbthytExUGlv7VVAMnFmTdW2bUIzMJvOsp7pkwDL8lVYtKO2oDVE5D20Q0KsyG4SD44BmJ8_L-WU2g-cP21D4bZBnOLcyzxmCcSX2g6dvqZp0VrN-onBZwhIyyNrLnCckiy2Smdrk9uUiHTG3OSBdq6akCLIGCKZK6nv4R0g8NT2C8t4zRz6uO1HkQ6KBEWVHz-OMvyBq27flYBTNYdPEdpFxJEhy-bHYGI66whvt5myxonPcRIA4fgN4jCCtovGNP20hJnbpBqKeUngG2-ZJxKxipqTzLHgP-GLTq_eRqRKd9kIMfYNQxHa7JzE_3Q7-3O-dKm6q2MH3r7el9ETkAgn0NSpx2-GDcZmMfkojhq1Rv1wQXq1Q9-Oyb9H6IZ35OGLwlcz4phYBpovxKlBAZIdfrNLqLECP9l-d6sX6evW9CT7lpQhGA_AsMDAi98MO3LqoecaXzKp5r5LksWYh6NAPU_FscnrgQ9SDwAa3LH6COwu6uKnZInIad2CUGpl6zVkSYdJdPMGdjOIv6jYwfQRIk5TwL0VUFbAQbV01NOOZ_09-5QV2atTa_T088NAJyAoXBFT1ES9NRuDEPIpYYSzSNJcpg5W8XJLpWmyIQmxuIlbdgnELp-c46sC_02cEwsGDckWw4MEz1uLG2tMHMKoUm-c5SNDZBErH8MlOI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همین‌ها رو یک تلویزیون غربی پخش کنه، سریع میگن این برای اسلام هراسیه!</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5741" target="_blank">📅 19:50 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5740">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">ترامپ در شبکه «تروث سوشال»: «جمهوری اسلامی ایران دست‌کم چهار پهپاد انتحاری یک‌طرفه را به‌سوی کشتی‌هایی که از تنگه هرمز عبور می‌کردند، شلیک کرد. یکی از این پهپادها مستقیماً به عرشه بالایی یک کشتی باری بزرگ و بسیار گران‌قیمت برخورد کرد. کشتی آسیب دید، اما توانست به مسیر خود ادامه دهد.
ما سه پهپاد دیگر را سرنگون کردیم.
روشن است که این اقدام، نقض احمقانه توافق آتش‌بس ماست.»</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/5740" target="_blank">📅 19:23 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5739">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/726fb491ae.mp4?token=gsF1trprqzpfDtVhaUNQwJkLyUEHiWJx9bDSMhsGdlnwGt-nr69RE84PPRRg9NkyMPBO6day9CBMHIvpxt4HxVRohTl9-UQCIDkkuW36exxpr2-vs0tf7SfVSz3rhgJBdApyhZLPd2FY-EB-kABhmKaxdNSOpNzGm3VjJ-DnpPnKF2qMhsfzhjJAw530HfKRPmPwsTl2c09PGkyHgieyUT9j6cnNkz9pWB03Gce_KU72Tx2jotX82fvQ_J_YVdhlEcy14vH2Vs2fygQxA6d-EULGtmYPsJ2p65TvWMEbthauluJ5YqS3X96DK-Le8a7Bdl2iZjtwTC18wcYtLi2GLIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/726fb491ae.mp4?token=gsF1trprqzpfDtVhaUNQwJkLyUEHiWJx9bDSMhsGdlnwGt-nr69RE84PPRRg9NkyMPBO6day9CBMHIvpxt4HxVRohTl9-UQCIDkkuW36exxpr2-vs0tf7SfVSz3rhgJBdApyhZLPd2FY-EB-kABhmKaxdNSOpNzGm3VjJ-DnpPnKF2qMhsfzhjJAw530HfKRPmPwsTl2c09PGkyHgieyUT9j6cnNkz9pWB03Gce_KU72Tx2jotX82fvQ_J_YVdhlEcy14vH2Vs2fygQxA6d-EULGtmYPsJ2p65TvWMEbthauluJ5YqS3X96DK-Le8a7Bdl2iZjtwTC18wcYtLi2GLIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قمه زنان امام حسین رو چرا می‌برید بیمارستان؟  بگید خودش شفا بده!</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5739" target="_blank">📅 19:16 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5738">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e184bbb012.mp4?token=NfOUDOfwzC8fbmBkzlDUHHITQ7phbmhYcKDa4Umg-TU8JxmaHYHo1FFOaoYeCVS1vBCSXK-YHJ0FDP7TYKxcgnwDaIe9Gayhs-3FML8-O_oBQsd5pLJyvYus_dh4IVfcKvIqQIGa04zv_uOymlGLCqKbrX6p0Lk5qZdCoSXiOYhe4rUTPipcjmqUanjhB84v-m6WVTFRKhmRZ12RKLcNNtYoDSlNhf7OVV6hVxDCCXpTmpOSm8uMHO492_nyAqz2ArcFZeHC3KZb3y7hJC9W31NzNw6L4I4LcJF2iAULU8vMCNX_1v9V68zroGpCXHAbfoo_lkD4gsQTu2usckkaBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e184bbb012.mp4?token=NfOUDOfwzC8fbmBkzlDUHHITQ7phbmhYcKDa4Umg-TU8JxmaHYHo1FFOaoYeCVS1vBCSXK-YHJ0FDP7TYKxcgnwDaIe9Gayhs-3FML8-O_oBQsd5pLJyvYus_dh4IVfcKvIqQIGa04zv_uOymlGLCqKbrX6p0Lk5qZdCoSXiOYhe4rUTPipcjmqUanjhB84v-m6WVTFRKhmRZ12RKLcNNtYoDSlNhf7OVV6hVxDCCXpTmpOSm8uMHO492_nyAqz2ArcFZeHC3KZb3y7hJC9W31NzNw6L4I4LcJF2iAULU8vMCNX_1v9V68zroGpCXHAbfoo_lkD4gsQTu2usckkaBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قمه زنان امام حسین رو چرا می‌برید بیمارستان؟
بگید خودش شفا بده!</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/5738" target="_blank">📅 19:09 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5737">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BOzwguJjkJxo00HcM6WhCKP2HscmINDUECwf2K_r-cl1uLeJcJFsIBsrWnkKRa5Eja8DAlOEu1YQ75g2qjimCYnA7i9py2Y11fAg1KMien-MLDH8wZS7npzbYOtPhSPAMo6t4Fc5VyoeiSKnMGQET0NsWlwy6z2fHzY9PBFhbcE5WXpmhhgp72gSMrEZQ-lO9ldDaQD9tFsseImY6jmUabvRnQjS4SwRrugjDPlFl58RDhwWGuuS-Ohp5l16YqVipQlFrbPygQNMW-0OxPD7vksH9IWO3x_bogh9tOPimQV3dyl56P2ZWn-rwNPNbmJMtZqmtl-H6NmwS7zCJXHK1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیام فارسی وزیر دفاع اسرائیل خطاب به قاآنی فرمانده سپاه قدس
آماده‌ایم کار را به پایان برسانیم.</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5737" target="_blank">📅 17:53 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5736">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">نحوه اعلام خبر کشته شدن خامنه‌ای
و عدم تعطیلی مدارس</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/farahmand_alipour/5736" target="_blank">📅 16:55 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5735">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CA7Sp5h87bC4NnRnvTbyfB3oLB_PcIqn5QcbMdd9e11OTriRYRjKg4-Xzb06MBIJjF9ZDpiQwkSEvgYZUN7_M7ENEyfgjNPL9UFaXfi7Mtrj6d4OO8aO0Xsoh9bwzBkvvY8nISWX6SQsS5hZbvizxqMIabp0NSwNis967wYKlYtghiSmiYlc5Ny7m2Y_L-0N3KS9pmxl-PBCsTgvDVgdA6xoC8ydCFwGx5zRNQu2fyb2xGu4cZ2fNsL3F5WDykI4PP6ju0ksTu16MokJko9fcjnan-QRezXqPXvUhKiHRIDE5ao2BhjjIGmzDd0WxIuw4eWU4eyeJnEPiYOpgRoAmw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lv9cN_Y26fsWjPXZd44lKyHWQGnatfV5-9xvFm7WugehF0sHRQ3W-RdPqjt-wcfqodNzMjoRz9tiLe5mAHQsIAulvFPs6-UjejMUKD8Tc3wGLCVMiyQ66kIJ2HzVcSQeIzY9zNvdjo5OnXrjRDX9VmGgl648UYIkHKcjwf5o3w_ODjfea-a1khUEkyBBaYF7qXp60FrbEKDTPfb1fKbErXzIFHxjfHmTkkXakMz067toaU2ybdPLTZHDYnnqn-esEfjbhociR2icTw1eNcEwiUXx71IqMgJBxtoZMOfXPFOzYJhHvJo79y_FTT5aMHNBpRGX5bIFkpaY47wDpYi6xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر علوم جمهوری اسلامی  در ترکیه،
خامنه‌ای را از اولاد حسین عنوان کرد.</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/5734" target="_blank">📅 22:29 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5733">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WnYPxOYp0bZm6LTekB_7EA1Rdv7qruOjoIN05X5qScXmByva_IqI9ORiUduFP_rBEZHYJzgl75EeRKDG0K85DrTODge027uMfhhZ9987gMZuErQRbsut5Jzbw0orfaKJ6Sq8r8tYj9APVKpfEIcuy4wX1q1saXdPQMTve-rOj2UQSdkI7AF-accGBCCn9-8TCPJO8L_8b_fYs8C5XihiCGEj5A-NOkj7SqdpmpTFgn8Jcnpdn4ISKqs6YADhXwGAbjg0x2T_dZ5KrI8Ojt1xjWPbiXoCGLlh9oyAeDIejBHGekYbmk5A1wmk4QK2dm_8WA38FmDgMTOjE6_rOG5w9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسرائیل به یک خودرو در نبطیه در جنوب لبنان حمله کرد و در نتیجه ۳ تن کشته شدند. مشخص نیست سرنشینان خودرو چه افرادی بودند.
صبح امروز هم در جنوب لبنان یک سرباز اسرائیلی در جریان حملات
حزب الله کشته شد.</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/5733" target="_blank">📅 18:23 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5732">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aVkDwigGk0d8BS8X40We7e4VnSFsE0msW4FW2V2XpKZlQHM_MD07f56rGqEXu3rvzO-DW1mWJ9J9-xm-x0djmocTF0hyutYeysReAOB3ZRfb0eZX-OjugAw8mGuYGEHnFKaOaLtM8fETz90E_NXDsNfXvu-Df7M2Lr23SL7IPIFRXtTUCfThBJwQCoRc98Ioc6B7Y6iVZyBB_fzCyRVNpa5yGJ9P8s0abbNRt4zG8f5iNLxbG-nbMgb3slLIVDeBaApPRDr5SJ_JrNE4Z8jzQRDUF9Wqq8AI-8qflYbWJo0nXpJMrl-9F5CsS9mbGD1XWCYGk2MymvMWuPsKuS0C6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صد رحمت به اهل کوفه!
لااقل به دینارهای طلا فروختند!</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/5732" target="_blank">📅 15:21 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5731">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIran International ایران اینترنشنال</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6715f87786.mp4?token=ddPjbxuTJn4yh_XYXn4VntX7Oefh7CGLoj1aHkst1gUJEDf65bgxxigLVVql93YejjCP6INQWUU1xTsFZ0MIs_esak40_GKWDGSKBGmVA11X8KV7iG-3VJrx-iWEyHjQtTFVTS4Yom3vuv03DEfsWrA0zz6V96lc3eIAWClbb_1XvYEoLGrUU0dTZjChvIzJ56Uka028XZ1s1WPND2b1iuh7TkL9HUsE6FcfkBcp4mjKHlqT790WoPWTYhuagf1BRDj2iV6AEqZOS5Uciz76YjS59FnYjXftpDcqtnNzE5E3fxDw-O2olyOIvKWhpG5LtMNN5NwDlTFEmydZXDM_wg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6715f87786.mp4?token=ddPjbxuTJn4yh_XYXn4VntX7Oefh7CGLoj1aHkst1gUJEDf65bgxxigLVVql93YejjCP6INQWUU1xTsFZ0MIs_esak40_GKWDGSKBGmVA11X8KV7iG-3VJrx-iWEyHjQtTFVTS4Yom3vuv03DEfsWrA0zz6V96lc3eIAWClbb_1XvYEoLGrUU0dTZjChvIzJ56Uka028XZ1s1WPND2b1iuh7TkL9HUsE6FcfkBcp4mjKHlqT790WoPWTYhuagf1BRDj2iV6AEqZOS5Uciz76YjS59FnYjXftpDcqtnNzE5E3fxDw-O2olyOIvKWhpG5LtMNN5NwDlTFEmydZXDM_wg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیوی ارسالی به ایران اینترنشنال نشان می‌دهد که صبح چهارم تیرماه در همایونشهر اصفهان پرچمی با نام‌ها و چهره‌های جاویدنامان انقلاب ملی ایرانیان برافراشته شد. بر اساس روایت رسیده، این اقدام «بدون ترس و با قدرت» در جریان مراسم مذهبی «عاشورا» انجام گرفت.</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5731" target="_blank">📅 15:20 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5730">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/afaf9624af.mp4?token=D23FxxfW-vVkl3rWYnv92hA4pKyMQDLNy9QgDQxXpatzTbSffSPvW7rS-BDtUX-cwsnYjvoHo8sbKKN5ykUlKnEOKgpIPNIkA5_uPd-2ev53eRklWFKFPwM3Fypovzinp2TuMKusMjcA6aUTzq9uL7KSI0Yzma5p1sGBDA1qNavwPKwLG_LY_WuL0N3fotNPbcQUZT7QOajWL45-LEUjO_pGBZ_YDYsNtyU2FclBjdl14cF87robTVERiwR2-1-tmLjfvKiiEU4A1BuVwybDM7TuKbASSPI-G2QYTlC5yXg-_jB2cKA9tF-jQZ-9G6HSqCEy6oRmD1NJS1tf521UEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/afaf9624af.mp4?token=D23FxxfW-vVkl3rWYnv92hA4pKyMQDLNy9QgDQxXpatzTbSffSPvW7rS-BDtUX-cwsnYjvoHo8sbKKN5ykUlKnEOKgpIPNIkA5_uPd-2ev53eRklWFKFPwM3Fypovzinp2TuMKusMjcA6aUTzq9uL7KSI0Yzma5p1sGBDA1qNavwPKwLG_LY_WuL0N3fotNPbcQUZT7QOajWL45-LEUjO_pGBZ_YDYsNtyU2FclBjdl14cF87robTVERiwR2-1-tmLjfvKiiEU4A1BuVwybDM7TuKbASSPI-G2QYTlC5yXg-_jB2cKA9tF-jQZ-9G6HSqCEy6oRmD1NJS1tf521UEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گوشه‌ای از جنایت‌های دیماه جمهوری اسلامی</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5730" target="_blank">📅 12:24 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5729">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">اینفلونسرهای عقب‌‌افتاده‌شون‌ میگردن توی دنیا تا سطل آشغال کشورهای دیگه رو نشون بدن  و بگن ببینید اینجا هم آشغال وجود داره! پس اگه کشور ما رو کلا آشغال گرفته و به زباله‌‌ دانی تبدیل شده، عالیه! عادیه! معمولیه!   مثل همین حمید معصومی نژاد  که دیروز براش نوشتم،…</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5729" target="_blank">📅 12:00 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5728">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/REs4PjIo9y5aeQq3ZOKirrKjOH7N1m6lLo5zLoLDliVMgOSzX015Bp0js0RMC5gyo490A1cvihskXfW0wAOPFYHc6CK4WCD7AVnaTMjQnYTF4aSZQtJGF5WQCVJ6PcWKKHkG1Yqs581nG5zeMdjMTSLOvg_wO3YgmxP9auQuAlsgYovgPnlAHTx6cVosbItSXclkahwbwTL88_PFOlsVO3FlNZRL2Jc1DncbS9YIx7ZB0sGq5HJcne26cwOlXtuSmYhf-huck9kLWRs0SCSzGD3CkFNeREyzlDyYjGhBNSuhzyEcoQPtwbjheSF5U43iu0oPQ-V-3Oyx1BHXk65JmA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/5728" target="_blank">📅 12:00 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5727">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🚨
یک سرباز اسرائیلی در جنوب لبنان کشته شد.</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5727" target="_blank">📅 10:30 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5726">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fy49och0kWCvQO9z37SZ6tjhLO91Tx8A-w2BGVKcMK8bzYDCzvn46ZMfwYUSiseTWmu8q0MsThZc6ZEjrE_szrkJvmfOF3kCiurOkvJHAEMeU4MBOxScIMHrH42okwKds4CtLXTb_jX0QjqSfvllz5TdTRNgbdWfOACh9cNxUrUXwjReFMF_rsGw2v_AIIfKirOuc9znN-FJ2mLr0vw6xqJmKTtDIawrVlFrmtDMQqkxvoT5ltvqOV9Xvb6us24D8Cq7DlZ8up8Dz6RTGOC17mUvyS_eVH-zPLnuf9EaaW-Q1MSwsXd_CFaRkaw1JMwnT0oP6QHosBADBk6sIL9ALw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرمانده گروه هکری «حنظله» که در جنگ ۴۰ روزه کشته شد، ولی خبرش الان منتشر شده.</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/5726" target="_blank">📅 09:39 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5725">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/86c17f6d3c.mp4?token=lIfg69Zh_H7gnJs6rGt8QULU0ExfdgUos4bo-9U_mJhheVB_leMP0I7A2WaRFj8wIahxEfb4Xc1kaSJNulTrIpuvFeUBPWzlFllY09JuD09LvwUnSyVp0cIPjZ9uQa2IuEsFshswpJh1xv31_K0CdTcPTI4OyQClZbEAz7wqMJX4oUCUo3htsQPse_fdtdyZLG_1NPGMVJKIqd99VBKYjJRaqp0bMarVPMZxQahl6J7_uiSgSSgH2aF91uXHHg7ag1zzrfYJV_bGkIXfIEHE3b8Uhkhq7KJCJnDcm8R6wRRVOFTcrup5q4PkGYKG3FLsNLvg3shYACuntbdT2XnZug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/86c17f6d3c.mp4?token=lIfg69Zh_H7gnJs6rGt8QULU0ExfdgUos4bo-9U_mJhheVB_leMP0I7A2WaRFj8wIahxEfb4Xc1kaSJNulTrIpuvFeUBPWzlFllY09JuD09LvwUnSyVp0cIPjZ9uQa2IuEsFshswpJh1xv31_K0CdTcPTI4OyQClZbEAz7wqMJX4oUCUo3htsQPse_fdtdyZLG_1NPGMVJKIqd99VBKYjJRaqp0bMarVPMZxQahl6J7_uiSgSSgH2aF91uXHHg7ag1zzrfYJV_bGkIXfIEHE3b8Uhkhq7KJCJnDcm8R6wRRVOFTcrup5q4PkGYKG3FLsNLvg3shYACuntbdT2XnZug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ میگه جمهوری اسلامی خیلی رفتار خوبی داره با هر چیزی که من میخواستم موافقت کردن!
باید هم موافقت کنن و گرنه دوباره
برمیگردیم سراغشون!</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/5725" target="_blank">📅 22:56 · 03 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
