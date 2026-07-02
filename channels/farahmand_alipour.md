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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-11 20:14:51</div>
<hr>

<div class="tg-post" id="msg-5838">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pFR9mP27XuuGctu-j9UIthXRXcR2HkauBcp1vLGDZucKGnJvm6eCgYqeLOvCJYxlxP_FsBBPQArNZnG5bWZDEwg8-oRrf-Vs395QhuFLe4n0xgtcckZPJNY5zaXOh57Dn2kPUElOb_GIltlAf_xxkne8VsmO5yH0tHkbhceyuXQVw48OkPF6o13-oWWgXwHuGqHV_kMRmdG_2cieuC8UaZz-wOvzGoDrem8KfCz2jRHSP2VrOUFiX6qglWYIWeM0Iu44DJe1d3irDKrX5zLqC4gT-lw5sJi9TyfIXlCj8YcxMBdPEm4W35CEv8IZAj0QYitzECSm04Z6x6YqyGioJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بارها نوشته بودم بستن تنگه هرمز
علیه خودتون میشه و میشه تنگه احدتون!</div>
<div class="tg-footer">👁️ 2.86K · <a href="https://t.me/farahmand_alipour/5838" target="_blank">📅 19:51 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5837">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sYSlidjSFGizuNxf7akejcFa-W0V3nxfwB2eUuasb1PzDVKm0REuO1QswdLgrZ4WyJV93uCy9_BZpeXJ-KEUYHDlX1b-9z7fZsAG2ydDh8z4RuMEgvzHWtqlhFOA9VrxDnu_5UYxLANrAAMNGawKNtqU4TjMISXHHNav543K7N4L01Y_MaezrDdVVXcZRU2YQtIddfM9WrdazZWIOSQCCqda5ucIkrYtJolCCDPEoYH7b0kMEvRE_7G6_4OxaMWA1ga4wICJlt4ERIUinY75EczzXSj5N7NNnHfwjJue1jvnSR05_ZdA28_T9idA13qdvgyflc3HR_lQKUVqdP-x2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روسیه، چین و هند حتی حاضر نشدند «وزیر خارجه» شون رو هم بفرستن برای مراسم ولی‌امر مسلمین.</div>
<div class="tg-footer">👁️ 3.42K · <a href="https://t.me/farahmand_alipour/5837" target="_blank">📅 19:45 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5836">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lxbQzXGl1WrvlN9I1lmnND2NVF945lmXSD8zphNG79RXXIsZ82X5Iugs0692acWqBXfB6u7Rj82YgnNyijd1KQ2hAhhc5wZANS_qyBB9d_2iTpz9tmQD0gAXQcsCP3WY8Z1xloET6OosZziCYCUgQH93Jxz4q_5YzWzrZfB5UVjMMiBjkHPDraHMngf-3mtEYLQ3MP8Ysajo2BR1KqfaA00qokDrdaLRwRyACaELmwVUpmXg0e3zBG7E5AvDzKftNByph9k6dD4NbNlKM6ABkE9XD4ccs0vXxocoD0zsWzrH2d-MReZQ66Yrf00Yv9v1UNLKuuNWZcHQVcnpV_B3jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روسیه، چین و هند
حتی حاضر نشدند «وزیر خارجه» شون
رو هم بفرستن برای مراسم ولی‌امر مسلمین.</div>
<div class="tg-footer">👁️ 3.68K · <a href="https://t.me/farahmand_alipour/5836" target="_blank">📅 19:41 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5835">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iJRkbhs9IbWoRZovuIbAdCL8RXSrfv_LsUrHECXlOyAb2uyCnEEv9ImGnUkRyGmvAC06Z2YVpGx7izQ-p_b2WD9xm-bTyR5IzbJa30aWfPj3lmO4UruESejP3oMsOJpBG7NLchPSl77nDA5NmHdAG5jEjqbm4o8iZQyOB8lfip-ciniSz7YpCk9ZbLMGfjSmj_rW69BB-5xaFhnYeIyVHfGFt8KxkjcULSzASE3rL-HTEk3EI1vda8CAZRClwHoNtnY5UOogMYIUFLiFLHvjQw7AKDT1iD_I28FYmfPpNWm07UmLfMN-GmjQr4YYQyUOtDqs0B-TrusDlkbR-DeOtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/farahmandalipur/status/2072405978012844407?s=46</div>
<div class="tg-footer">👁️ 9.97K · <a href="https://t.me/farahmand_alipour/5835" target="_blank">📅 14:35 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5834">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YYpS2AGyOFJVNJHDIntWcTTBzu3PdjdY18dppzEwL1jCxfGZv6syisx77E5hiMHQEPYnJtUTSN9gZXYvTd177TsveVJqvA0LGWivRTQChf1q5mzc4OG542pY63Y5_CSOZgNYufdzZz-B3Yd_U8TlsXDG9NEsdRvjAQnl97Cgtu2iWJI-GYu-Fbcn96_Ol_EWdmmJwESqGPryWonkVcZphsPFW_ju0RB1ZI5L3FWhEzAHL0zhw5psoQPDc1xzjYkbeyqPUNtH2cw3TGnubrI2qyZJVsAmo5TIr4H1iisaf-1ECwLlTi1o6uFduvMAV5l3KqysaEt2kONB3pF3l_-EKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چرا صفویه به این کتاب «روضه الشهدا» اینقدر بها داد؟؟  ایران کشوری است که عمدتا در جغرافیای گرم و خشک واقع شده،  قحطی‌ها بسیار زیاد بود، فقر گسترده بود، جنگ و ناامنی بسیار! صفویه با گسترش شدید مناسک‌هایی مثل سوگواری  برای محرم و قمه‌زنی و گریه‌های شدید و…..…</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farahmand_alipour/5834" target="_blank">📅 10:48 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5833">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B-6p8jGj_erqIzymuNNH7CqkXx7WFj5Q67dTmM0GBCBTeKO2JR06nEfkRn9O--Fj-ljU-O-lSSsZBWprk3mezHBDePIVi6ZjUF3FZURIId_wEl9OlAYkOpwlELJFhxj4DgcLBTxFZrFoOlFTdV4VSGqmuYJ0tj1Wx54wQ-ALKBxgXghOtmRcN-gvflFwaXBQRoihdZHMEZEEmZVsOiI8TqnmgyXs_L89XSsfht6uupp8xnV-1Iw5xVqdMeBTBmYb6za4XWJr5VUiSDnX9nfo4nHs82iiRl17m8SqKxXsUqbeAqTY3PETy5hS2adcg-GXXnROgf4GmPAdS_AWJqIHtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خود خامنه‌ای هم در اسفند ۸۴  یک سخنرانی در جمع روحانیون در آستانه محرم داشته و گفته که باید روی  «گریه» و «احساسات» و «عواطف» کار کرد!  و امر میکنه به «گریاندن»!  چون روی همین احساساته که به قول خامنه‌ای فضایی ایجاد میشه که بتوان خیلی از سیاست‌ها رو پیش برد!…</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farahmand_alipour/5833" target="_blank">📅 10:42 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5831">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VZKiyY-aTp0qDEKrp6Yrrqa54CWEEkg5V7dIZrjj1SRcHW-wGLJ9xc9Nz3dP3nVQw9r3RH68-cRAaIg-ffBOPlUwaftTKPrTf0r3o5KurJrpTOCc4LOBslM5TKEz7XbKDZJv1FeI4oaTTf5JfLNDGtQ-XjMI5g7VmBjOsI37QepOpewMYYgfwIz6HdwIasc8nyqHBHrypuSS7IbalJdUWBwmI2Dd18MMGr5Vvb1q6k_SsGw5-wGuEXJT0OA131dZ1haGl7dyMrFf-eh37JwXLCOEE-ddBazRIvzf99d0X0D3ims1q_VAJDVh7SMPfrmr5xJmXe9DDHHhaivLJNYdIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KJyICSScG8w5gh4zHFUwgeBMPU78Ocf3sPu_Oy7a8kmg8xJq_CVlElx0QDixCzfbNFcCHHRKMJeWxK7-Ptinzu0Z2PRp4NxiOhZj_BSQT3nrRxm3BmiD2Vj8liPfNH8SrTExP_t-muWmu05ULgg2aoXohpu69PLaN7x0A6Katy8_aaiEEVtoMMksasWxOp42smVKf23pScPC9Nj_jUr8veXI3ed010P1PZcn-4oahzw_A6PVdXi3bhiKbx-vvqpWhrQer58M_uV21OI99eedtM3x_Qwz-6mVoF3hSep2OWpM31ovvP33L3NPhPcNTgvZj83-vsb62VPnGxtpWbCgiA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">نکته دیگه اینکه خود صفویان،  از فرقه صوفیان خانقاه اردبیل بودن که در این فرقه یک «مرشد» داشتند که قزلباش‌ها، باید با «شور و احساسات بالا»  نسبت به مرشد حرف شنوی داشته باشن و اطاعت و‌ پیروی می‌کردن!   این کتاب «روضه الشهدا» برای صفویه خیلی خوب بود، چون شور…</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farahmand_alipour/5831" target="_blank">📅 10:38 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5830">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EtohJesNZbSJmgFGg6BfdC2n4_8K8nNkEX_hgtwNsihYrqRbio9pkVAiC5zX-fNZJB6hC2vrooeuXqAFd9L8M8qt3mimgp-llY3SKQ_gUNOySYYAFEIcAyIqRp5zOkurtHiCnzLrq7erwAb41Kd_v-kyLSXTalerTCZ8lTyNEYuIkYTt6Nv_LOKZu8S_PV8KD6WUspY3yTLdP0gMx48LVXAGs1R-yRX3hnlN4Ey1Pi17aGlfGpCV8DHAW1fhGVXWvL4yhm_s-q9Bo022yCFvmJQAUvNNUw7yB-5rdVxHucLu5WcSQ6HW2XUlQGr0YHsT-CU8DZ4Jqws2Mkggb_pSvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چرا صفویه به این کتاب «روضه الشهدا» اینقدر بها داد؟؟  ایران کشوری است که عمدتا در جغرافیای گرم و خشک واقع شده،  قحطی‌ها بسیار زیاد بود، فقر گسترده بود، جنگ و ناامنی بسیار! صفویه با گسترش شدید مناسک‌هایی مثل سوگواری  برای محرم و قمه‌زنی و گریه‌های شدید و…..…</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farahmand_alipour/5830" target="_blank">📅 10:17 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5829">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CNTYxJ77ojeY7zQleopB_UcHLTvcFvN1qfGY2PASFcLVRp3SWs8BdFg4uEIH4F0s0x62vRuQq-TP68L1HvP15RPtIE07aWBI0w2gVXUiZG6CZCorqqIYkviaXKLkaQPU1cjKwL6ipRgexiYl5u2RmKLIRKePqAJN1s0Lc6G9mFzqCw_TE6yMFmqshVj0oub7iVMUGYt7hvFvoYazDI8t89eCdzc1k2hTzp6qy4U257xUNnqofz5pmmmLGUw8YGc_ZkMbSwg2TTMv31ctymPn_HAniifMH-keA-WqYf6Lpm_7Sdwzvs11bnDKjP9YVvczXNVLhH1M_dx7FF9xpsbOGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای با الگو گرفتن از صفویه و با پول نفت.  این خرافات رو تشدید هم کرد!  به «مداحی» و «مداحان» پر و بال داد!  بودجه‌های سنگین! تبلیغات گسترده از طریق رسانه‌ها از جمله صدا و سیما،  که این‌ مداحان با خوندن همین دروغ‌ها! احساسات رو به نفع حکومت مصادره کنن!…</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farahmand_alipour/5829" target="_blank">📅 10:06 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5828">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QfvVUcn0nncvG0HoZzOuLrTxwkAP-ZoM3mdCktSzHWlwyiI00K6qwEpvDhrq6E-ejROreuxedUXZYNl-3Q_7-ChSUyb9rRsdxmgtV2hr9bEnPjw1kCdYufWBKc14DerjipadA1PgSzwAf3AQBhQoq_0EOCBAkCaIQ74LEmKFaMSiW9KapYXbGx6RI5vqSML1eEgBnTr5SB5Wnc8YYqed4PU9CSev6SCLyu0ztjxOW6aX9ouXRisxhx3YLZxkcZ1QnFNiDV6DcihXbCWrkc3SIcjUModRWVoTEqMqUQ8rgt7eNFv4AzjqW9GFcoXMUGT_uEF4jaWJTbVddu7AP1x_Ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مرتضی مطهری در یک سخنرانی عمومی  کل این کتاب و داستان‌هاش رو «دروغ»  و افسانه خوند!  گفته از خودش نوشته شده!  کتابی که داستان‌هاش صدها ساله در ایران خونده میشه و براش گریه میکنن!!  کتابی که حکومت خرافه‌پرور صفوی عامدانه ترویجش کرد بین ایرانیان!  مرتضی مطهری…</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farahmand_alipour/5828" target="_blank">📅 09:56 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5827">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">در زمان صفویه کتابی منتشر شد  به نام «روضه الشهدا»  توسط «حسین واعظ کاشفی»  این کتاب عملا مبدا روضه خوانی  و ذکر مصیبت در ایران شد.  و اصطلاح «روضه» ، که امروزه برای ذکر مصیبت و گریه به کار میره (در حالی که اصل معنای واژه، به معنای بهشته)  برگرفته از همین…</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/farahmand_alipour/5827" target="_blank">📅 09:41 · 11 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/farahmand_alipour/5826" target="_blank">📅 09:33 · 11 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/farahmand_alipour/5825" target="_blank">📅 09:09 · 11 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/farahmand_alipour/5824" target="_blank">📅 08:27 · 11 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/farahmand_alipour/5823" target="_blank">📅 22:52 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5822">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad33cb95d6.mp4?token=fJmyzrsMTEmfYg_rMFPn0Ixn8MTnBtAu658X_H3B2GgjFg1-z26rZdrknyz52DkUrTn5TN-fK20rdloKGq4Ohh7UNt4StDLaeZ9_GU36Waig4_lBAvuS7I6GviSBcmb4KWJiQepjpV9dhLLIgkTulpugjVunI2_6SSFsH7fYaofSRIoszhxrTO-dfW4gXUSFU0PudgFxJokIqBp_Brof6wpOjFQ-rLMXOlo4OHAS8fwo53mACjK8ibfUz0PxxOe4h_mquukU8liulEiGtUEkxzU6uQQBP4z4SpYqDD_JqQXrUOmS7GGsVd_hUMZLFKG9W6wPAPUcvzFifND9Ot1fig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad33cb95d6.mp4?token=fJmyzrsMTEmfYg_rMFPn0Ixn8MTnBtAu658X_H3B2GgjFg1-z26rZdrknyz52DkUrTn5TN-fK20rdloKGq4Ohh7UNt4StDLaeZ9_GU36Waig4_lBAvuS7I6GviSBcmb4KWJiQepjpV9dhLLIgkTulpugjVunI2_6SSFsH7fYaofSRIoszhxrTO-dfW4gXUSFU0PudgFxJokIqBp_Brof6wpOjFQ-rLMXOlo4OHAS8fwo53mACjK8ibfUz0PxxOe4h_mquukU8liulEiGtUEkxzU6uQQBP4z4SpYqDD_JqQXrUOmS7GGsVd_hUMZLFKG9W6wPAPUcvzFifND9Ot1fig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حرف راست رو از این خانم بشنوید که میگه بعد از انتشار خبر کشته شدن خامنه‌ای مردم در‌کوچه و خیابان‌های تهران کل میکشیدن و‌ دست می‌زدن.</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/farahmand_alipour/5822" target="_blank">📅 21:52 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5821">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a22e78d39b.mp4?token=FarxS6zgpjZbJtdjVKsI9PYgizVHgSdHTRQkkHiVO1uiiEyFskU0N-Rdx88iIw6GUtGQumGrL86zi7yK7WO4CaVsDDnRWOejKWDSfJOHFxXQy0Vpd895tyP7mTGh261_3VJqYcznM_vEvUM2O63enKKqRBAlMiw4E8IyPQaJFY_HAvTu6vwDCB2vtY71JarmLXp3l32UoGp--hQWkEugyvx8_-kt3OJCz66VJmyCy0KkKt9X_Temnh3m4uuG1ALOTT3xV4Xhek2MMrZQvTue_PR-Iu6Y6V13t_21kNlw2bJIDOZln7eTOaejovHSZ9dboFgBQ_Pi5ylN81kygCjqJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a22e78d39b.mp4?token=FarxS6zgpjZbJtdjVKsI9PYgizVHgSdHTRQkkHiVO1uiiEyFskU0N-Rdx88iIw6GUtGQumGrL86zi7yK7WO4CaVsDDnRWOejKWDSfJOHFxXQy0Vpd895tyP7mTGh261_3VJqYcznM_vEvUM2O63enKKqRBAlMiw4E8IyPQaJFY_HAvTu6vwDCB2vtY71JarmLXp3l32UoGp--hQWkEugyvx8_-kt3OJCz66VJmyCy0KkKt9X_Temnh3m4uuG1ALOTT3xV4Xhek2MMrZQvTue_PR-Iu6Y6V13t_21kNlw2bJIDOZln7eTOaejovHSZ9dboFgBQ_Pi5ylN81kygCjqJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">میگه خامنه‌ای وقتی کشته شد امتش ریختن توی خیابون بر سر و صورت میزدن  ولی دروغ میگه :)</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/farahmand_alipour/5821" target="_blank">📅 21:52 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5820">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/256cc521e9.mp4?token=HHocNLqPVi8CabV33iE6qhkEZcdwdKu8xOzgj0sVNWNYQkEMxHTzZOEPjFtB8R6zgrNwrwDlzKCG8731c9pDP63fwsZXXIp54ql2u3ZJbmL2uR9sPVmQZgWhmgsCpASl4OO-umJRWXN5X9rXHo8y4YvagG3EmuuDoXHBXCUpEbB2mPeiwqGAGggKEHMkiH_SXjx_66574fxQZu8-BW08s4GykFLy_cQR-ZZkAeA1aMkfDxU4ujz0fh804VtZkOEO7uJTa82bVKxlqh68X8VnBXnZWCPW4O9WBjmRUgs2R58W14qz3WiT3sHHJbfuSfNcKGSG4XpPMLizpi3_tNsZDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/256cc521e9.mp4?token=HHocNLqPVi8CabV33iE6qhkEZcdwdKu8xOzgj0sVNWNYQkEMxHTzZOEPjFtB8R6zgrNwrwDlzKCG8731c9pDP63fwsZXXIp54ql2u3ZJbmL2uR9sPVmQZgWhmgsCpASl4OO-umJRWXN5X9rXHo8y4YvagG3EmuuDoXHBXCUpEbB2mPeiwqGAGggKEHMkiH_SXjx_66574fxQZu8-BW08s4GykFLy_cQR-ZZkAeA1aMkfDxU4ujz0fh804VtZkOEO7uJTa82bVKxlqh68X8VnBXnZWCPW4O9WBjmRUgs2R58W14qz3WiT3sHHJbfuSfNcKGSG4XpPMLizpi3_tNsZDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">میگه خامنه‌ای وقتی کشته شد امتش ریختن توی خیابون بر سر و صورت میزدن
ولی دروغ میگه :)</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/farahmand_alipour/5820" target="_blank">📅 21:50 · 10 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/farahmand_alipour/5819" target="_blank">📅 20:05 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5818">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cYyU5LTG5HhxNA_ZifLqyxziFlTnQi_e4aPmG0ThCypRHEMYyVSnzz3hv5PwD1Nfmb9c85lAdEWx8NFt_WkY3dFx2X6YENOxIptVozFR0ul7PdsCjnc_mG6J3GgoyjaFPTPJSN5Z0aR2WPGJlXhbjgLglG6Zh0kRd9azVh6X76D4sqRGZcYsPMN2LLk2Osbk4MAj65E8a9XS6QqJadkS_lrv2NSksaKr3UvKtvlfkfFx825Ka1E43_0c8PPJ5nVMsFgPfTswCDcl2TNbq_FT36jFe0s_VJeM8y2JKSRp-CQlPrVkv0qcseqxscajZbuG9GYDR0VacUIfkM1ftQ8gUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/5818" target="_blank">📅 17:21 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5817">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7862dff401.mp4?token=oN9cTWOCCUTUV_vR55qG8y-JPBCPvM-LVa-7wg_DsNxOPpdSW7TeBgQiIZbTfHP_gb9-6FBdKcOqd1QclvTBsiACxoLww1r_50dmzXIW1wwMOyrNbVd7t8cnYoKNmwTYeuiWjaD52j6WA7dx8XfO5DOaLoGB0cotUgAGiDxLbv5anaJ_0j8nIJ75A8vmqo2-FPjFvgJp8WQZ59pNaVM17whSRfPeMFtO0Ljm6mw-TyjNtyefVn3BNewLfl5yD9_aYBgnRwKKTq8Wf8fwRv4gvCP9J4ocHJaY5m7q38WK0k3YLN2tY39vxDKneXhKEh31O_Kitx4P_1Pmckpq5PGHsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7862dff401.mp4?token=oN9cTWOCCUTUV_vR55qG8y-JPBCPvM-LVa-7wg_DsNxOPpdSW7TeBgQiIZbTfHP_gb9-6FBdKcOqd1QclvTBsiACxoLww1r_50dmzXIW1wwMOyrNbVd7t8cnYoKNmwTYeuiWjaD52j6WA7dx8XfO5DOaLoGB0cotUgAGiDxLbv5anaJ_0j8nIJ75A8vmqo2-FPjFvgJp8WQZ59pNaVM17whSRfPeMFtO0Ljm6mw-TyjNtyefVn3BNewLfl5yD9_aYBgnRwKKTq8Wf8fwRv4gvCP9J4ocHJaY5m7q38WK0k3YLN2tY39vxDKneXhKEh31O_Kitx4P_1Pmckpq5PGHsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جی‌دی‌ونس میگه ترامپ میخواد با این تفاهم‌نامه با جمهوری اسلامی،  بازارها و مخازن رو از نفت پر کنه،  و بازار سهام و اقتصاد رو درست کنه بعد تصمیم بگیره با ج‌ا چه کنه.</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/5817" target="_blank">📅 16:36 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5816">
<div class="tg-post-header">📌 پیام #79</div>
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
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/5816" target="_blank">📅 16:31 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5815">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🚨
نتانیاهو : اگه نیاز باشه به تنهایی و برای سومین بار به جمهوری اسلامی حمله خواهیم کرد.</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5815" target="_blank">📅 00:04 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5814">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/60c1fdbeee.mp4?token=WbdlT17sJu1wAShgWpg4k5DzZQ3_iyRkTFPP309NobJmeZr2UCLAIR9ZK6aFdMAPk3NqXCabxaNjDYdSfjhBN3mUWReI1qOuA-qGK85Rs_Cu4JiuXGpxMBz2YMHHDkAreYjfSN3TEghIFTpfDY1hjZysWYfPbsFd5U-nMVJVJtUfSLGj7txnxYMpc-toGt5itkKIsfQsxTg41wvNFjuNZrvoN6u5XuFgHNDAnEq8t84kg_BEezNg_8qXLd79gDaWd3-uMP0Ekm3t-3NZ_COAZIPx8L0EOUjv2KwYR0g7XEce58PW8vkft7YmRBQqd8La3eiumeaeiSTWZ27WsMjM9j-Te8Gw15suum_RBLBc3DVHpn_r-Z8xWCNJAo5oJpYB9OjEZIYZJOuj9bZXzFCkwqKgkQSN-6rZ8srjoz0pg-p_wS0Zkw2qEFaF9iVxw6_MCt7YBSbb5IEX-9kgIdU1mNUZgWuFroAEGDql0JGqdkQru6AIKSHbDq_vBTbhD4I3NJSOo3eGnd4lgIXhxJkSSZJsl68NcK_VPPAJHVzPiE7FIdpjfREi_U9c6kJAZfFk7Ps9S_TYFy2SclT5tYUyBRD4MuFRxvpgny4B3vKj3Sm0FNSbJS5mLPOTNUqiWKm0570QIG2KuvmHhWMtxrNoiTznWF5Dwa9NnH74XNpiC7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/60c1fdbeee.mp4?token=WbdlT17sJu1wAShgWpg4k5DzZQ3_iyRkTFPP309NobJmeZr2UCLAIR9ZK6aFdMAPk3NqXCabxaNjDYdSfjhBN3mUWReI1qOuA-qGK85Rs_Cu4JiuXGpxMBz2YMHHDkAreYjfSN3TEghIFTpfDY1hjZysWYfPbsFd5U-nMVJVJtUfSLGj7txnxYMpc-toGt5itkKIsfQsxTg41wvNFjuNZrvoN6u5XuFgHNDAnEq8t84kg_BEezNg_8qXLd79gDaWd3-uMP0Ekm3t-3NZ_COAZIPx8L0EOUjv2KwYR0g7XEce58PW8vkft7YmRBQqd8La3eiumeaeiSTWZ27WsMjM9j-Te8Gw15suum_RBLBc3DVHpn_r-Z8xWCNJAo5oJpYB9OjEZIYZJOuj9bZXzFCkwqKgkQSN-6rZ8srjoz0pg-p_wS0Zkw2qEFaF9iVxw6_MCt7YBSbb5IEX-9kgIdU1mNUZgWuFroAEGDql0JGqdkQru6AIKSHbDq_vBTbhD4I3NJSOo3eGnd4lgIXhxJkSSZJsl68NcK_VPPAJHVzPiE7FIdpjfREi_U9c6kJAZfFk7Ps9S_TYFy2SclT5tYUyBRD4MuFRxvpgny4B3vKj3Sm0FNSbJS5mLPOTNUqiWKm0570QIG2KuvmHhWMtxrNoiTznWF5Dwa9NnH74XNpiC7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چرا جنوب لبنان سقوط کرده؟
چرا ۱۱ هزار ساختمان صاف شده؟
چون رفتن دنبال «خونخواهی خامنه‌ای»!
به قول خودتون چون «پای نظام» شما ایستادند! به خاطر افکار شما!
خواستید جنگ راه نندازید!
یک میلیون شیعه ۴ ماهه آواره شدن!
شکست‌هاتون بیشتر و سنگین‌تر!</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/5814" target="_blank">📅 17:59 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5813">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6a28a5f6ff.mp4?token=Qxlz73vvXwZwMVAaif_lxMj-Ad532AlwvJ02m2xUpShMM9WTLAaEnLoXUsqDcz-tBsXzUR5QgnGZCRg8n1XPilmPbycna2vQrcxfS-WgvyuBIWtBA3JWZR5E3fBV7oCsC7nE5YuyWVpR_P6BIzOAaA_Sfn5ympvVBt4mZRNfOIL2XuB7F-vkW9QYDSkpugkj3XlOlImpH1BMS5f--oV4bzJy5bAVPcy4semMir1R3jnRBXbsIB73p4-DKA3KDy_pBl-UgdQup3Wbrl0aKvtev4Mo-MBbp2VIO_VFu_j9Jz4bMVUdTJ-0vtEgGT68FrUNfFT3CCo6b2-Iz2aeOcD_Og" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a28a5f6ff.mp4?token=Qxlz73vvXwZwMVAaif_lxMj-Ad532AlwvJ02m2xUpShMM9WTLAaEnLoXUsqDcz-tBsXzUR5QgnGZCRg8n1XPilmPbycna2vQrcxfS-WgvyuBIWtBA3JWZR5E3fBV7oCsC7nE5YuyWVpR_P6BIzOAaA_Sfn5ympvVBt4mZRNfOIL2XuB7F-vkW9QYDSkpugkj3XlOlImpH1BMS5f--oV4bzJy5bAVPcy4semMir1R3jnRBXbsIB73p4-DKA3KDy_pBl-UgdQup3Wbrl0aKvtev4Mo-MBbp2VIO_VFu_j9Jz4bMVUdTJ-0vtEgGT68FrUNfFT3CCo6b2-Iz2aeOcD_Og" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5813" target="_blank">📅 17:53 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5812">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/085c31b1b8.mp4?token=jYqvzUQ02FuJS50DL-Ri_svqCj60FKrcc0-yUh8V2TDKP9tD88io1_e8hdrN7_AbZpFkXWZg3GDKKaIXZq-YEZ1h-ep9ZLGCATXl_8BpdB5W_csrmF9cE2d3owCX8Aal8jtBo8MRRLAjlLFCI_UbTs6mbK2RnylP5_lSd-8sqSfZkymeTLuJfW19HFpTm70Qi-Oknp8eRSacexdZUO403892wfj07RrREAHA5jSsnD4GAEpIyLc926Ir7q6cxAcRMFnbP_OemWWjx0QKsl2R309C8Ye7KIC-yeyDgvsm-4EbYI7FWjnlOtBi2mJ_Qk4eoMpFPCrxNRHV-nEk1eHJQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/085c31b1b8.mp4?token=jYqvzUQ02FuJS50DL-Ri_svqCj60FKrcc0-yUh8V2TDKP9tD88io1_e8hdrN7_AbZpFkXWZg3GDKKaIXZq-YEZ1h-ep9ZLGCATXl_8BpdB5W_csrmF9cE2d3owCX8Aal8jtBo8MRRLAjlLFCI_UbTs6mbK2RnylP5_lSd-8sqSfZkymeTLuJfW19HFpTm70Qi-Oknp8eRSacexdZUO403892wfj07RrREAHA5jSsnD4GAEpIyLc926Ir7q6cxAcRMFnbP_OemWWjx0QKsl2R309C8Ye7KIC-yeyDgvsm-4EbYI7FWjnlOtBi2mJ_Qk4eoMpFPCrxNRHV-nEk1eHJQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محمد اکبرزاده،
‏ معاون سیاسی نیروی دریایی سپاه،
‏شب گذشته در یک سانحه رانندگی ساعاتی پیش کشته شد.
او در یکی از اجتماعات حکومتی به صراحت گفته بود حملات آمریکا «واکنش» بودند! یعنی ما حمله کردیم و آمریکا پاسخ داده.
جنگ‌هاشون در لبنان و فلسطین هم همینه! حمله می‌کنن، وقتی جوابشون رو میدن میگن ما در حال دفاع هستیم!
۴۷ سال گنده گویی کردند و سرمایه گذاری روی تروریست‌ها و وعده جنگ و… تا بهشون حمله کردن، گفتن ما مظلومینم و داشتیم ماست‌مون رو می‌خوردیم که مورد حمله قرار گرفتیم!</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/5812" target="_blank">📅 14:57 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5810">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Yw4YvHBMEKCLMrxw4xgOI3AJt53IFQG4-n0BgFWZFTVelyQcLkoW7eENmQ4yFI5Oh-qmxPeXoTIvqbtEl29B8igJy6IvZ3D5MikdnOA7ni4kEXiGFTyYVoPG-CtY8X2WJVLXEU4NuQI3OWgkL_mrzGY5UNXCjZIA0RKYWf7PP8MpkVMDiue1XV5cinaDZJEudhqEIjU-Zac7tAPUlmzMD2CYpVbcebT0f3LxEeHeQBAhuURf2SkXgOlIiIu4Oy0SlaHdfUhZ24QvznH7jnY6Ce_yK7kSEeW3qWKiXoSEiHl1CBAhKYL-NZ6UI4eCNiFouNgZii6SsL2kLflnmH5l1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/X6mprV4uApafEr51BUnXp7G_RARh9z5CNSdXVPAyArMOYpLCQQLMXmo6yub_oGvdsqYVVLnTohcnMWnPtbEQQ-JTQJ9CNrz6l6e9QRbPOtU3GkkZmWIOOBRgBqNsmLIkO1NnYT2MbsWOkP7sTPzc3hTCN7wZrGXg481dxjinnPD1LSPYrYFmUbCa6jiXhj5OObqBtpTQJRpng-v9hoj2BUwBL-uGQrbfKQ-PhLQxfDU4WFRTdZPX0z-jUYqBPmh1lFramfF7mb6DswrMGpQTf3cR-VYWSb4vkrZhK5Ka_85Wyojp2eQRri5lc_zKsG5mw87_d2Qu7qgg_sEN4Aagog.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ده‌ها تن‌ از‌ سران و مقامات عراقی بازداشت شدند. از خونه‌هاشون میلیاردها دلار پول نفت و طلا  پیدا شده!
خیلی هاشون از نزدیکان جمهوری اسلامی هستن.
با تصویر خامنه‌ای و سلیمانی و سیستانی در خونه‌هاشون و سوتین و شرت طلا!</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/5810" target="_blank">📅 13:32 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5809">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee0be552a1.mp4?token=dFxsb6thb2ioykWc_RKWGILPbvIubElTbp-PxkG7ccGFJjJyQHy2SZ_O_yxdA6iHBQ8NjtmAvv_lYxuy1QMENfpwMsWqIxZlgwPB71_ZKcik1GvWuFL8H4jHzocqzo7YfxdVRwvK2nO8jjqI5coxDMaY-ow8VHGik4QG6ROsoUzMQuxR7IZsu3LtZVyifUBLb3JaYzvjF56Su1qBZW3qsIKFde3yAQLwzDlVSadrl3BAfCVkLoZEgSjmQFRZ-WYdEq2tcEcCtgmwIdt26GPJr6c7ICNVQ3RttLf3EqZ5trs1QTPbgTgCCIeXd1AhIr3KYdTSuOCgJJyY86M6bIQu94WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee0be552a1.mp4?token=dFxsb6thb2ioykWc_RKWGILPbvIubElTbp-PxkG7ccGFJjJyQHy2SZ_O_yxdA6iHBQ8NjtmAvv_lYxuy1QMENfpwMsWqIxZlgwPB71_ZKcik1GvWuFL8H4jHzocqzo7YfxdVRwvK2nO8jjqI5coxDMaY-ow8VHGik4QG6ROsoUzMQuxR7IZsu3LtZVyifUBLb3JaYzvjF56Su1qBZW3qsIKFde3yAQLwzDlVSadrl3BAfCVkLoZEgSjmQFRZ-WYdEq2tcEcCtgmwIdt26GPJr6c7ICNVQ3RttLf3EqZ5trs1QTPbgTgCCIeXd1AhIr3KYdTSuOCgJJyY86M6bIQu94WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cdGAIiqcqJuZa_MGiZGlg_2pXkvPqzCGDOT7sGvmjG9nSv82R7kY5qB3mF2jcfAf8JOyh_WYTOYbRVVL0F6rhSD7fHN9Cx7GmNErTHwxd9vkIliMRulUSa3xBpra33UiTbMNA5HIs_RFEh6WIXzl4HKgpk0cZK5a3xnac-AnYTp7RCvPN1U4lRLeokjD-LrK0T1vy1RWJ1AWV3uSojJcw3Q3hCac0zFwkQ2P2pJcoOGEERL-mzxR5sZwJ5HfKKh6FBSVmIJMKpqOGClDbvs0JBA-nDRoab0UQFkvofb2oWmbLPvI9FWxbm95-99r1KATXB70JTCwsE337011GsQMcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقبره رهبر مستضعفین! که در زمان حکومت خامنه‌ایِ ساده زیست! ساخته شد،  با مقبره فرعون‌های ظالم!  که به قیمت و نرخ امروزه، مقبره خمینی ۲ برابر مقبره‌های فرعون هزینه برده!  ولی عرزشی که نمی‌فهمه! بهش میگن رهبرت ساده زیسته خیار نمیخورده، خوشحال میشه! دیگه بقیه‌اش…</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/5808" target="_blank">📅 12:47 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5806">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CQue_DrVs1na7kWwnp6VgZFljD2seGGs4pCLWJUBv0FbxEilhjDgsfHnXPs3n2ez4q2xDZscRkT-UdF89J432IjGETbwS9j1a2XO6rTasky6XmleQhauS187upR3LyvyTqNPHJA-oO06uxz6DOGJkkQQJoXRRsffAy6V_lIpx599dVrEG7v8L1HCS-dOrcnY8zUaq24yD8xJ2fN_8uXhXZ6iQpgdimAnBq0k7zjADMm8N5L5ybzgcrtYJhiLbfZ_CNbjX6znKejLhaKBcNkIDjuD8kG_2wjlhvpcFHolK8VvOPVdriZ_Di4zS3MZNhHIuinrZ6IrSJsdv4hEi_qOVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vwriymA8SpSWFshTWGnpb04tFtg2J6ph000YVsnlIpiPLUMLFOywmwHQ_3NWBJDlJDGNZmF1ZeJi4OsmSEQsvMo5gI5dzaI0BsOEiU1r2Xc3mUVbBkVoCXc1Neb6Allmaaf0GXk4Y0eepVZiy3UAhVwS-EoyQHVCY43fwXkpbvEi99H2bnIT71iSQG8WZb6Q47BGNliVNRyrMjHCc0iCA4QbzkeYSuyruCHHn2qbBBD60Si8WG29Akq9busd2oZuRrF2iKCgFAduzHyIuJtW8oMN4DG4ZdyDDFqLMHGeyJirDWFby_bHQGxLgk4VLOftsXKQ2uTogKf8kjAvOreVuQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">هزینه هر روز تعطیلی تهران،  ۲۴۰۰ میلیارد تومن خسارت به اقتصاد کشوره!  اینها فقط ۳ روز برای خامنه‌ای تعطیلش کردن! یعنی فقط این تعطیلات ۷۲۰۰ میلیارد تومن خسارت به اقتصاد میزنه!  این فقط یک قلم از این هزینه هاست!!  ولی خب رهبرشون «ساده زیسته»!  خیار و هندونه…</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/farahmand_alipour/5806" target="_blank">📅 12:35 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5805">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GI4Gsc92NSSv_s7cDCK7H0PJrEyaDAKMkgRO-7FuXaEqLMCZb2g_4Q95Pcn1GM-96vK1kx76BEWUgbsAg1vgjsQ6nVmcemeQq_DCRSBiQUrzs1ooAq1HRnMB9eS2SfQd8MyHSy4SiUZGHuB0_qn4uNuV4-o21S-rrOc_gaoA80yJgVNx8Dgy1pOeIXMLx872bCGp-dNTqxZns07AMSiAjEJxktwwIfB-WBOug2AEK9gG4XZaISMmvpSa3fm4JhIzlVrMakgfPH6IevAewtf7koeC7sWMuO-0UDs5N0-5A-gtzVFG_1073CsS7m6ibhZEmTkoB7FdiTx9ZKsJwZEyOg.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/5b7a3755d2.mp4?token=pNiqdl0ZdhETQ2vFZ8lvQbggdCS6bLYtay3TaPku4JiNuTOt_ifIKF9xlQyVvSpTj9PdMkG1mkclCd3Fq8IAmDPRI5kvCi58AdQ01MN9mtHVf4PSADo1ZyeZEhcq1ALEp3hHWTjuLkdJZXvSadydxHBlISJRjyOtlLN-4kEMJPoNxMAzXZsIWZ5xmCN8Zi0RqFfH-AppiqxB2MgXvRXxzICsQzrekZzffuWrn0bRJiC1hKl2DBobSM4UCKRWdglIwb0Xo_OkTTqkFdhNq3189sOruNlVy0SyuzVp7qyc63vt8BqRcCj1P5cXRFEmDSucdPQ3EtiqYIEGXilxAGpAjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b7a3755d2.mp4?token=pNiqdl0ZdhETQ2vFZ8lvQbggdCS6bLYtay3TaPku4JiNuTOt_ifIKF9xlQyVvSpTj9PdMkG1mkclCd3Fq8IAmDPRI5kvCi58AdQ01MN9mtHVf4PSADo1ZyeZEhcq1ALEp3hHWTjuLkdJZXvSadydxHBlISJRjyOtlLN-4kEMJPoNxMAzXZsIWZ5xmCN8Zi0RqFfH-AppiqxB2MgXvRXxzICsQzrekZzffuWrn0bRJiC1hKl2DBobSM4UCKRWdglIwb0Xo_OkTTqkFdhNq3189sOruNlVy0SyuzVp7qyc63vt8BqRcCj1P5cXRFEmDSucdPQ3EtiqYIEGXilxAGpAjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">برنامه «زیر آسمان ستارگان سینما»  در شهر بلونیا در ایتالیا  که ۵۰ شب در طول تابستان برگزار می‌شود.   (در عنوان برنامه در استوری اشتباه کلمه سینما جا افتاده بود)</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/5804" target="_blank">📅 11:16 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5800">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf427145cc.mp4?token=YdfCOi0iM11x9M3_9UQpjjhgwm9thSKvNzc1zGTT6UDGgL8JAYKVDskKvQ3ghGD5IM0WVFamp2mPgxhT22tVZ9IcOp2EqnCzU1dFDU_2eokxnfLcrIM_74Kt6hALTNJjfwOaHhuOsuLgXCxTm6Ne49X6ayp3kD5oFbRKZYQOjCc2hORsaNATKwX4rk8sIeIAn7eiDjkd3OHp9Csq50RnfWV8e5Azh23dfeR-QuiBEBC68EdM4NjNQArZ-rl0uX7pPyr6swqtw6p7QiVOZal9ZWGYt8LbLXeVo-ubf0TCgb1i7EWuXUsS6OvAS1uO_Asjx83iT6x1pIh3CtS02mhmtA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf427145cc.mp4?token=YdfCOi0iM11x9M3_9UQpjjhgwm9thSKvNzc1zGTT6UDGgL8JAYKVDskKvQ3ghGD5IM0WVFamp2mPgxhT22tVZ9IcOp2EqnCzU1dFDU_2eokxnfLcrIM_74Kt6hALTNJjfwOaHhuOsuLgXCxTm6Ne49X6ayp3kD5oFbRKZYQOjCc2hORsaNATKwX4rk8sIeIAn7eiDjkd3OHp9Csq50RnfWV8e5Azh23dfeR-QuiBEBC68EdM4NjNQArZ-rl0uX7pPyr6swqtw6p7QiVOZal9ZWGYt8LbLXeVo-ubf0TCgb1i7EWuXUsS6OvAS1uO_Asjx83iT6x1pIh3CtS02mhmtA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">برنامه «زیر آسمان ستارگان سینما»
در شهر بلونیا در ایتالیا
که ۵۰ شب در طول تابستان برگزار می‌شود.
(در عنوان برنامه در استوری اشتباه کلمه سینما جا افتاده بود)</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farahmand_alipour/5800" target="_blank">📅 10:42 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5799">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aEwwbkOdKUUVsBFQEmH1qAR54xxY_KoyTd-zG4CfcKaeAZFXukKsO8UObFMbC2g2_uM6p0up2L9L81UQgVu_vDkKy3IiECYIIUs11J-MvIUhUlsnzc_CUl4gHfZl19tvsQVtR1bVvL2GFNh0_Z7SSJQYKedEZq0qijhwSvQZ1c9d5IvGF5veqSr6croHtXPCE75xIXxWLWyAJXJGc-2aWRkbaJDnuLf8RIX4urmZ9WdhFg0keiY20iPpOeM9erKwavl-HjvS32yFF5FMrnvRE84771u-s8OoifyXRexmYTb4JeOIYwqCzrKxD7VkfWsDU6zHM7-oUPmNJ7HD5o4L2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هرگز به مردم ایران نخواهند گفت!  اما کاملا قابل پیش بینیه که هزینه این مراسم بارها و بارها از هزینه جشن‌های ۲۵۰۰ ساله بیشتر خواهد بود! چندین برابر!  درست مثل راهپیمایی‌های هر ساله اربعینشون که باید از جیب ملت ایران مصرف بشه!  یادآوری : هزینه جشن‌های ۲۵۰۰ ساله،…</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/5799" target="_blank">📅 09:26 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5798">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2dc44e27bf.mp4?token=LTHw8aTtJfLc7WZ_ZHtFLoiN3VVYiTSH6i6zbPdfyp2lOvy2XHZATupMqJXVKOkODpduL6Cn-BCIy35_hd1pyBTiBn0osBg2--3pfy0v8hd8b6u9SOPFXsS00ZZtSJUnnNZwwtBpOqC1pWOjfE4s8E6_UsHL3IN3FVaqsqPhP-hmCu_vBCGkV8fNx3a9lgtwUi8f-ohKqGZNb_2jXHjchxePSvhthVagkGN_R74LSHk7DNRi4HMAcFX0TwKx6RziTFZO3_Ai9igh52zYZ3sj-NZkDqNqiWLWLx2_fagp4Il-LIhUXA53uuV-2OD0WC4PBz1fSKP5goaLr9GuNOQpIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2dc44e27bf.mp4?token=LTHw8aTtJfLc7WZ_ZHtFLoiN3VVYiTSH6i6zbPdfyp2lOvy2XHZATupMqJXVKOkODpduL6Cn-BCIy35_hd1pyBTiBn0osBg2--3pfy0v8hd8b6u9SOPFXsS00ZZtSJUnnNZwwtBpOqC1pWOjfE4s8E6_UsHL3IN3FVaqsqPhP-hmCu_vBCGkV8fNx3a9lgtwUi8f-ohKqGZNb_2jXHjchxePSvhthVagkGN_R74LSHk7DNRi4HMAcFX0TwKx6RziTFZO3_Ai9igh52zYZ3sj-NZkDqNqiWLWLx2_fagp4Il-LIhUXA53uuV-2OD0WC4PBz1fSKP5goaLr9GuNOQpIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d3b713ac56.mp4?token=Znh8VZg04vk9GpdBCOCZMc7Y_9GeN4mJkalbel66jvY5N0CcBVkTsObpWtwIJHS9YAHops07uPK7c0FsV8pYhBC-J-_Of0nMuvDO3arZfUMWsWruYf5FK91OHbLq8KwoJpIQnBN6J1hn4pRs9tesDDoyRPCptpAqBxRv7LVhhefw3iBdxMFqi00WcpsZEni1_1ej7Eu_OdhxXxzcPdzYqwvhvZE3GOxviNzNiOtcpPMQ84HREu2qZWbYilZa2YN_h0D7jsksJyRjSnptRLjkZWtwg3LgjnlRZN41dhT81wiMD24Kk9mnB2EtVj-IJXnoWCfH44jSv2V22i08j-5t-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d3b713ac56.mp4?token=Znh8VZg04vk9GpdBCOCZMc7Y_9GeN4mJkalbel66jvY5N0CcBVkTsObpWtwIJHS9YAHops07uPK7c0FsV8pYhBC-J-_Of0nMuvDO3arZfUMWsWruYf5FK91OHbLq8KwoJpIQnBN6J1hn4pRs9tesDDoyRPCptpAqBxRv7LVhhefw3iBdxMFqi00WcpsZEni1_1ej7Eu_OdhxXxzcPdzYqwvhvZE3GOxviNzNiOtcpPMQ84HREu2qZWbYilZa2YN_h0D7jsksJyRjSnptRLjkZWtwg3LgjnlRZN41dhT81wiMD24Kk9mnB2EtVj-IJXnoWCfH44jSv2V22i08j-5t-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لحظه‌ای که «سپهر بابا» ستاره رفیعی را دید.</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/5797" target="_blank">📅 22:28 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5796">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e1e05c8825.mp4?token=CfaCzA2BnfzSlKTOTYrly86541Paa3Fe_1z6U_35rBbLnL5w4CXyShtjrcCZTmOxNFOCyVxXGGR8HdG3_NzK1k5FKpvILZFj2FZduaIJbQw44qJDJVuWUJtxW86_xo0XKyVP70qe8dJS9FuENlTcWDjvzehVGS23M5VISxMECnX6Virb-NGl0Y7HipeMsiiPtiRJSIcBRd37l0kcxuGAlkiILVpPbu3ef1z5uftwuevE5XmqnygMMt-BdscfSueV-VcJbrjq0Ee_MkQaSqAsehD5QRLNGim41U0ahkLdovWH1g4lzms0WIHySDwnJ4-OmYtK4WG-faReWgfuBlMQ5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1e05c8825.mp4?token=CfaCzA2BnfzSlKTOTYrly86541Paa3Fe_1z6U_35rBbLnL5w4CXyShtjrcCZTmOxNFOCyVxXGGR8HdG3_NzK1k5FKpvILZFj2FZduaIJbQw44qJDJVuWUJtxW86_xo0XKyVP70qe8dJS9FuENlTcWDjvzehVGS23M5VISxMECnX6Virb-NGl0Y7HipeMsiiPtiRJSIcBRd37l0kcxuGAlkiILVpPbu3ef1z5uftwuevE5XmqnygMMt-BdscfSueV-VcJbrjq0Ee_MkQaSqAsehD5QRLNGim41U0ahkLdovWH1g4lzms0WIHySDwnJ4-OmYtK4WG-faReWgfuBlMQ5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تفاهم‌نامه ج‌ا و آمریکا رو به طور نمادین آتش زدند و گفتند که این قرارداد حقارت‌آمیزه که خب این بخش رو درست میگن!</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/5796" target="_blank">📅 18:49 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5795">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O7smZuFwCejYl0PlkoNIV85xuSqHvNrpbVoAkxNH1z0XB0Yhgq8HiZpVuPoF8b1gts3nAUmAyCyz6m-Jm7bKYijx7qU18PjiO_aAi_jRfRDX8VILIg7yucW0uZYCU9DDymYYOZgBqsh5Av0PI5yjCnJsLiIHfjefiCVrsJhSGq9iEsdR71QSKAP6Gl2zcqhpUE-70Dh_bZZ5_hiZcebRUq5LR51_wvVqALcg1zzgxytz4JHjg9CvN3498FdQ-sVbK2_-Wp0xGX23YiZu8lGCNkik7mkp2R2XPyv3HmtB4nowwf9AoXnJ0GVyMk1cFWk-e7xlQuYja9PfG0ZuvsnW-Q.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/8e972609e9.mp4?token=gQq0TD2w9IgkkOj3hNMgkD3gfQS8PdkcI49HX5HMgQdUxTw-4eE7TF9yiGhUPzHJ5sReiqC9tZ7oRLYX67B6EuL0ZhPOWIlivEel6xLZ3G4vHbs4wnoJ2zrfojlYysb-d2CfJ4eE6WLpXqEtwz-iwitYvqQjK2NbVZy8QvpH8JnYrVMiNNVrXaOUMwS0t2_OJK1DzISGrblpyZpneq-LF5kj3MtISeG29lloA4NOcl-rwFPt2cGpQZSZ1r6ZPBRXRuUn2xkzyUSXllcTQz9W_Q6TQM2TfQci38pSxOEhGTk2dQ4-AkIPJRgKt9A0_KNCWMgtlhJrFhowxSiCTmG4Mw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e972609e9.mp4?token=gQq0TD2w9IgkkOj3hNMgkD3gfQS8PdkcI49HX5HMgQdUxTw-4eE7TF9yiGhUPzHJ5sReiqC9tZ7oRLYX67B6EuL0ZhPOWIlivEel6xLZ3G4vHbs4wnoJ2zrfojlYysb-d2CfJ4eE6WLpXqEtwz-iwitYvqQjK2NbVZy8QvpH8JnYrVMiNNVrXaOUMwS0t2_OJK1DzISGrblpyZpneq-LF5kj3MtISeG29lloA4NOcl-rwFPt2cGpQZSZ1r6ZPBRXRuUn2xkzyUSXllcTQz9W_Q6TQM2TfQci38pSxOEhGTk2dQ4-AkIPJRgKt9A0_KNCWMgtlhJrFhowxSiCTmG4Mw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این شب‌ها، همین‌ها توی هیئت‌ها در حال عزاداری هستن
ده تا مرد مسلح افتادن به جون یک زن معترض ایرانی.</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/5794" target="_blank">📅 18:39 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5793">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PHb3eDcjjfrI1Wej9Q58NqlR9jY55wHIIYBKh0BsC0Sgo4eTS86dlt3ZwgighEjBzz7wIIR418xTQmrRIqA-emROzx-Dq17uLB3dSaGjn_jfLuDLF1rwKziPHXenHQmhE3CFMhUFzRco2QNl0y20yTtPFlT31ZpdDJ7gJOhSbaGtYYwgevqygMulFvOAutySG1ma4kMDE9YT7NfIgF3XOxAzWsCpo5l2cubrUXp2oAvi9LvKhq8c3WV20GQWvDrO-MXdhPsw1BdP5DKvNXjmuRuaH2mtDHvmJzXr4DJpDSdf9vNSW4IXIQIa_Wck7HIi977nxKXcd1waYUM1vd_1bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حالا در حد یونجه و ذرت ایراد نداره</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/farahmand_alipour/5793" target="_blank">📅 18:33 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5790">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I-DJvnyksrSXb47yiV_ugNGRI5DpTaFZYXa32Mo-Wj4BEg2VVjUWFe7KvsLMNzBzHG59hNpt8gxyRSnzaepAVv_yxj5pC7UV1aq9QKAwHkVYxhK7fgHyoQQeav1HLDrPt3MsDb1QxInQnQRg1crKZUTRwwG46EvimCwxAFgx_LVlPZDkCb7B3J3896aQ5Kx-sHQXte2hIdp-chpzKqojFi2AUqOBXlSbA2LJYI8cM8a2plYLGvP_bMVHP12RIritZlMojBMAk3SlQa7Yd127xRfutDvYbGJUeXT18PJ_jVb-eXXH0WufZYsy_iH9N4rEzlQN5IMM7egzB2uJyaF3Og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/651901a9ca.mp4?token=CsY7iYeug1H-qkFDauZQFRb8U-t3DvQPFNiYxTVq7pnbiVXxewrEfoaE2G6g5619xrXO05cZ4tzFLdnwdzig8aigPFHu2YZuAFBzBHwm_ZSv6ZF1bTOQ5UBE9Mb1uyQJ2fbfWzvt11Jarii7QFxlxRpJOfECfko-Hd2Q_QxdEmvwl46mu7ydiA9UfP55Zj6dKz2tL7dcdmUsmdsKbNcX2iUzd0Gd5i3qnZCahyF_IziEjdJbUYX2HCA9rSLiFjvsBRnKTxSlnAKjsHaKmOysJ5QWw-J7Upq1fqRnCJZungATTwOoBrJsP2cf1WymnukErdO-qrrBZntw1Yphs6FcHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/651901a9ca.mp4?token=CsY7iYeug1H-qkFDauZQFRb8U-t3DvQPFNiYxTVq7pnbiVXxewrEfoaE2G6g5619xrXO05cZ4tzFLdnwdzig8aigPFHu2YZuAFBzBHwm_ZSv6ZF1bTOQ5UBE9Mb1uyQJ2fbfWzvt11Jarii7QFxlxRpJOfECfko-Hd2Q_QxdEmvwl46mu7ydiA9UfP55Zj6dKz2tL7dcdmUsmdsKbNcX2iUzd0Gd5i3qnZCahyF_IziEjdJbUYX2HCA9rSLiFjvsBRnKTxSlnAKjsHaKmOysJ5QWw-J7Upq1fqRnCJZungATTwOoBrJsP2cf1WymnukErdO-qrrBZntw1Yphs6FcHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/583cd57ba5.mp4?token=ZlA4FUq-X2sOP7DoSj0pHxLttQqF7tNStUiXN62RDg2NRznFgTe_nKJORQHxxk5uhJThvWHiauT42-3rqXI9nQ55Q2XJv3n_A-BVcl84Eqd6KfQbzFy5WjtpOi4GTDY6LIcXQ0nE_1AjFisXCqscXMr8xXubm7oquy7_oi8UvCRRnimuOZnJ0fmu8BEmbYAJ3cL8XwzXZ57zE7RlcKxdyMAx9NfUOSsHbN7IpMOPTCPpM6lxUDaMwBT0mmHDCpFUO2O7ZrwEN10_YeIFyz2dvaLUhQsN5AKtV6sNfJAAPphM2ujdNrRI_3ElVQHtPtoJQ7PZpZSAKsbtrSkJnaHz0j39bJ0ZMHX8NcCtisMEUNYWhXA39SOlfcye3Y2Lq1PlU-yOs09CqPwxc5NOOyJOFmZEaLv4TAlrmezyMzCyxe8jjZ20-a8RWb95kq-OaNaHhs0GYSmMBX1B6-uIoZwVvIPcTY_MNBJW5Ep-FuOqqjLwQBMkZwEwmvIQC4PK3mdNfITp-dOy4JMrIUqcanfotqgEeFfS1yka7z_iXGHpOkawfEWva7-xSkFJ9ZyZwj-ZTpszQ76_73knbjD_dbZdL57tAuwqvFZpmRDtDry4fjHB7Ihy2ctrfaCRpUU6uog0ccaTALE3Yc6NWRaHAgTaFInqAllzYnY20k_j2y6OKXI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/583cd57ba5.mp4?token=ZlA4FUq-X2sOP7DoSj0pHxLttQqF7tNStUiXN62RDg2NRznFgTe_nKJORQHxxk5uhJThvWHiauT42-3rqXI9nQ55Q2XJv3n_A-BVcl84Eqd6KfQbzFy5WjtpOi4GTDY6LIcXQ0nE_1AjFisXCqscXMr8xXubm7oquy7_oi8UvCRRnimuOZnJ0fmu8BEmbYAJ3cL8XwzXZ57zE7RlcKxdyMAx9NfUOSsHbN7IpMOPTCPpM6lxUDaMwBT0mmHDCpFUO2O7ZrwEN10_YeIFyz2dvaLUhQsN5AKtV6sNfJAAPphM2ujdNrRI_3ElVQHtPtoJQ7PZpZSAKsbtrSkJnaHz0j39bJ0ZMHX8NcCtisMEUNYWhXA39SOlfcye3Y2Lq1PlU-yOs09CqPwxc5NOOyJOFmZEaLv4TAlrmezyMzCyxe8jjZ20-a8RWb95kq-OaNaHhs0GYSmMBX1B6-uIoZwVvIPcTY_MNBJW5Ep-FuOqqjLwQBMkZwEwmvIQC4PK3mdNfITp-dOy4JMrIUqcanfotqgEeFfS1yka7z_iXGHpOkawfEWva7-xSkFJ9ZyZwj-ZTpszQ76_73knbjD_dbZdL57tAuwqvFZpmRDtDry4fjHB7Ihy2ctrfaCRpUU6uog0ccaTALE3Yc6NWRaHAgTaFInqAllzYnY20k_j2y6OKXI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/938419e982.mp4?token=ZuA032RK0Dp3DuI-Iw9ogJYJr8ssp8-YkCMuZLO4dmiDy-ot3axyf7CclZRuXpg6brqKx0BJUjVyVjQ3kdvwrpxoIJ2ouRH1EkqCHpeCrA7tGaDu0rzRYCaXOLnt63p7VLTb7cDyX_kuq9ILMJCttU1hK6or1gPjkE6gDKXJD-0Ng9ir5qSY3ZRD8y_86DGDiLuyLFdkS7__iBZiyqbm7JkMT9H8lJ9GaDuN7DhyjB_6uhH0qB4gAg31bVvQ-J_gVPKun56LlxBrloTSoK1Kk0m-r3CA-ZzQ03-qFKlSIdrjoUvWidQjHzk9D8Qbn2MxT-b3_qCsvfED2VgvvbtdmA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/938419e982.mp4?token=ZuA032RK0Dp3DuI-Iw9ogJYJr8ssp8-YkCMuZLO4dmiDy-ot3axyf7CclZRuXpg6brqKx0BJUjVyVjQ3kdvwrpxoIJ2ouRH1EkqCHpeCrA7tGaDu0rzRYCaXOLnt63p7VLTb7cDyX_kuq9ILMJCttU1hK6or1gPjkE6gDKXJD-0Ng9ir5qSY3ZRD8y_86DGDiLuyLFdkS7__iBZiyqbm7JkMT9H8lJ9GaDuN7DhyjB_6uhH0qB4gAg31bVvQ-J_gVPKun56LlxBrloTSoK1Kk0m-r3CA-ZzQ03-qFKlSIdrjoUvWidQjHzk9D8Qbn2MxT-b3_qCsvfED2VgvvbtdmA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قدرت حضرت عباس</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farahmand_alipour/5787" target="_blank">📅 16:27 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5786">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d6uPauy9eX-SOSBbJl3iASiG86-4kkLCE-VPr4MN5Cp1wtiWdXjS4-DKbRo_LrkEFJeNkJ0do-LJi-C1LQTdDvosXVxZDo-hWzQvxClnhDF7W-gatTKDTluKcv7O1ImfMB52E-qolDNU0UpgGPIb1adPkMY3wcyNE8l_GZfHwcrV2PArJugao6toUcyAgf71iosE30eZIu3_gxZCC4W0fnJc4KPrxFrpy4MHKaflr-sBJjHlOa-dRrzk-A3OVQOCxKmVNa29wYEUSRJKaE3K_fxlbW-6SHL_6XjIAekR4WvQs4tr-zSDNd96C2PHvCfX4P6oI9JE1Nb0ZKimescWAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای فروردین ۱۳۹۹  همکاری جن‌های دشمن با سرویس‌های اطلاعاتی علیه جمهوری اسلامی!  همین آخوندها وقتی اصفهان در محاصره ارتش محمود افغان بود به شاه سلطان حسین میگفتن اصلا نگران نباش که ارتشی از جن‌ها میاد به کمک حکومت شیعه!  ولی این جن‌های نامرد نه به امام‌حسین…</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/5786" target="_blank">📅 11:31 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5785">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b91e9581d.mp4?token=FzNPnGpd-mYRo5RwCZLahWPfjx2Z11G11znfNZoywvC398OX4rppL1Y-L0VVJU0FjyHbv2XqCOrircm5rLAz7-81p7Qw61loHeaqtBZUMviSIY7fW8wMnxvv5LycR1k0vw8RgaNXqB-6VqPEOKXWBX1VjIGv2WWxFVhaaS0rJ5DgR4vy9XRLC6dk7n8Ry02PrvwXpnDNYkoPLJiKPwoOJ99BMJvKK7Ya5oxtfdmuZx0MxOiO-3jU_wjtu_KMTC4g_t5m2bUZ5VnDLFXsHo-KSmsqqeTLXGyFdGCE84MgZ7eo8E2CGywh1L_bfSGcGKHX1A3McaNBylv6zPYPhaHhSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b91e9581d.mp4?token=FzNPnGpd-mYRo5RwCZLahWPfjx2Z11G11znfNZoywvC398OX4rppL1Y-L0VVJU0FjyHbv2XqCOrircm5rLAz7-81p7Qw61loHeaqtBZUMviSIY7fW8wMnxvv5LycR1k0vw8RgaNXqB-6VqPEOKXWBX1VjIGv2WWxFVhaaS0rJ5DgR4vy9XRLC6dk7n8Ry02PrvwXpnDNYkoPLJiKPwoOJ99BMJvKK7Ya5oxtfdmuZx0MxOiO-3jU_wjtu_KMTC4g_t5m2bUZ5VnDLFXsHo-KSmsqqeTLXGyFdGCE84MgZ7eo8E2CGywh1L_bfSGcGKHX1A3McaNBylv6zPYPhaHhSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زعفر جنی، پادشاه‌های جن‌های شیعه
😅
حامیان همین‌ها میان کامنت میگذارن که تاریخ مطالعه کنید! محتوای تاریخ‌هاشون!</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/5785" target="_blank">📅 11:29 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5784">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb5c00112a.mp4?token=dXqJ-UmodiSPTdsrTNpaMCn5x3s-S-S_SSfAiDwo_T39q_rb1FiJEP80PyzYll5_OXp5kbMvxKTiU1-0K1zzSLrGaIZvEzSn5qIoNokMi1EubJCF99sUNl5wKOL5c1YcF5oYxaBsuwzcVaP2UW_emrvqsvpdI3bWTqEMw5sOuZlrBJP64vXob1fvdBC0dRjEmO0ywK_PqQTBR1JrV9nI46Nh2Jhrhdtypz_z78FTqh1JzZXm0b8IJ2azztzq_oK_CF8ZE7EzGW8G2naKwewDYGPVPnWXezkVR5B4rrJFtaBs_fX9nBL5YbpfoN2ZLdfdyVOo2KCi0NsTZyao1XfabQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb5c00112a.mp4?token=dXqJ-UmodiSPTdsrTNpaMCn5x3s-S-S_SSfAiDwo_T39q_rb1FiJEP80PyzYll5_OXp5kbMvxKTiU1-0K1zzSLrGaIZvEzSn5qIoNokMi1EubJCF99sUNl5wKOL5c1YcF5oYxaBsuwzcVaP2UW_emrvqsvpdI3bWTqEMw5sOuZlrBJP64vXob1fvdBC0dRjEmO0ywK_PqQTBR1JrV9nI46Nh2Jhrhdtypz_z78FTqh1JzZXm0b8IJ2azztzq_oK_CF8ZE7EzGW8G2naKwewDYGPVPnWXezkVR5B4rrJFtaBs_fX9nBL5YbpfoN2ZLdfdyVOo2KCi0NsTZyao1XfabQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/383f2c1b20.mp4?token=WGcrOq0vE0FqD66DO92HUojC1GIyHPkta1tkqpehmjL_V2UaEK_GV9I_SUCQ_EGDtQL7qNBUejDhY7k6iE9AZ_q2wJwPNsVspxKoFNdya2Aj7zYr0oaYsUrHuwPQsPl5DTHQgHQjg8bPflflXS0v1kMsxun_uA3pz7AWOgdoqHd4JnoPq-mQppA2Lusp7IWZJhuWVvvSgmGZHFq1N92Su-heOyFx5Fl5h6yreh759BbqnS13iVl73hm0b6nxFacYMFcJK6Ref3fQE4NqrjO9Qe95diTpn6NhpE2-F0H9erYGhtS70Jbt0UbBlELQcvu0my7raxyxVUVI_IomLg-ylQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/383f2c1b20.mp4?token=WGcrOq0vE0FqD66DO92HUojC1GIyHPkta1tkqpehmjL_V2UaEK_GV9I_SUCQ_EGDtQL7qNBUejDhY7k6iE9AZ_q2wJwPNsVspxKoFNdya2Aj7zYr0oaYsUrHuwPQsPl5DTHQgHQjg8bPflflXS0v1kMsxun_uA3pz7AWOgdoqHd4JnoPq-mQppA2Lusp7IWZJhuWVvvSgmGZHFq1N92Su-heOyFx5Fl5h6yreh759BbqnS13iVl73hm0b6nxFacYMFcJK6Ref3fQE4NqrjO9Qe95diTpn6NhpE2-F0H9erYGhtS70Jbt0UbBlELQcvu0my7raxyxVUVI_IomLg-ylQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همش ثوابه :)</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/5783" target="_blank">📅 11:08 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5782">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a9c5c701b.mp4?token=DIx8bzBAeLhwyXwcQhAKEkTdcG3IfHup7vQqroXh37iBW4Ar5qaLqG6IE1gQ405W_YZcZMYj6gPVfJd-Wz4xQDzWd0e5pQowi7tUKBIe8K0S5MX8trzmm_6rq7FrtrYdtYTseqVpIEnUqAGy5CMlENtQLoafiH0t1hPnSu98utgji_vAj_7RYYvAJiOlTTL_QGfmNyQMwfUQfw3TyYsrCGQH5Yl7QClOWkveOgIWjieB2pA9gduE51FkuhsWkMaq2r-A5D5bkBRnA5DnfrYpDfaCVXG6I1JWD3FvCVOKwD4Al1tDtX-udHZk8Lwh-B-DqJx8OnhraqHSMXutZZTDRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a9c5c701b.mp4?token=DIx8bzBAeLhwyXwcQhAKEkTdcG3IfHup7vQqroXh37iBW4Ar5qaLqG6IE1gQ405W_YZcZMYj6gPVfJd-Wz4xQDzWd0e5pQowi7tUKBIe8K0S5MX8trzmm_6rq7FrtrYdtYTseqVpIEnUqAGy5CMlENtQLoafiH0t1hPnSu98utgji_vAj_7RYYvAJiOlTTL_QGfmNyQMwfUQfw3TyYsrCGQH5Yl7QClOWkveOgIWjieB2pA9gduE51FkuhsWkMaq2r-A5D5bkBRnA5DnfrYpDfaCVXG6I1JWD3FvCVOKwD4Al1tDtX-udHZk8Lwh-B-DqJx8OnhraqHSMXutZZTDRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آورده فرهنگی شیعه برای ایرانیان</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/5782" target="_blank">📅 09:32 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5781">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SLZ2I5HF0DXUI-tCW8ddPeSW7RVQ__raf40hkUuWGPdcjQC1203DRlk4GedcbsbDdYoWh_IP4xco21MebVXmXLRDG5bHnIFVigVXvKYdysrQwAL1xs9oC3TatZua82MJtUD359cpZ5LCBosvfvThHYorvCYQvsETYOhraJBx_nyOcUgbrqIq0QTQTyPILmISWAtSITTTVy6O-BHG2O7PI2f0cZPRFzJj1aN2uurqnT8Pk9JmBbOXcKYnsOkcOFim5Wc39jj22YpeIl1uvJQ0_a6tKUsARwUwu0ek-Hlyjgkr66cQimIR1EHiVWTkM0IVAwFUEDPur1njjm46cFh1Ig.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5780" target="_blank">📅 00:08 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5778">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/409f2a841d.mp4?token=qo33F0kEuc37FovGLeEoocbhGvDFLp8d0YQTzXNDcu3iZIjyt_lMj6Kfuh1FI02u6BHI_cGxS6EPbrBKx4o5vSrzhczng5qJymU4MZSelsJkQ6dBpo_cgNEjGSeSmIAnAvr7vew72mlM2Vfs6U2M-frVY_2PvcDlbVch_Z-ZADskqb1QqUpWJpO5JR10GMa90kSU80Y1RJizvSwN4sc4MsqptX5UnQc-t3bknJGcJ0CK1uZT-wJ8aVzGxa0oLXDFwI_59cHr78EdacjZVdzJfvl3hHTg5ec4g5jVH2lfvnhMx63MWal7VbVEX51IpTTTfxURgh9fby3G7NPcYrvkuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/409f2a841d.mp4?token=qo33F0kEuc37FovGLeEoocbhGvDFLp8d0YQTzXNDcu3iZIjyt_lMj6Kfuh1FI02u6BHI_cGxS6EPbrBKx4o5vSrzhczng5qJymU4MZSelsJkQ6dBpo_cgNEjGSeSmIAnAvr7vew72mlM2Vfs6U2M-frVY_2PvcDlbVch_Z-ZADskqb1QqUpWJpO5JR10GMa90kSU80Y1RJizvSwN4sc4MsqptX5UnQc-t3bknJGcJ0CK1uZT-wJ8aVzGxa0oLXDFwI_59cHr78EdacjZVdzJfvl3hHTg5ec4g5jVH2lfvnhMx63MWal7VbVEX51IpTTTfxURgh9fby3G7NPcYrvkuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/06f2d554a0.mp4?token=faSlBJbAE5vAgjfEdHIY1U4D9YRFAH09cBAtTKVasl8tqyRso5sxQXoDCv26BzZ8Nem87dh0b9xGFAu0Pkq3RU2iVfB2Zo-c7Gf9xpdf8zC60Y25zAeJkiRcJW-iYkIV0SejIcpHA_KfXaQpFds6kJ6BDzpgO-vjLeDb676fU8fjxDZuZCYMF-HThXC19CZfFMlmU94eguINM-33sDm02yJew7lMgWmhFg3qslzavqWzIZS-9t_cjQnvvTHXANwuhbH2Yy-SQHHGCnW7U0GCLFoDPnZvR3Vg-uDXJvvJpC8OdhPfgyxLvGhGdTQ9zmOjK9zzUpQvAwNeSDQeUq3V9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/06f2d554a0.mp4?token=faSlBJbAE5vAgjfEdHIY1U4D9YRFAH09cBAtTKVasl8tqyRso5sxQXoDCv26BzZ8Nem87dh0b9xGFAu0Pkq3RU2iVfB2Zo-c7Gf9xpdf8zC60Y25zAeJkiRcJW-iYkIV0SejIcpHA_KfXaQpFds6kJ6BDzpgO-vjLeDb676fU8fjxDZuZCYMF-HThXC19CZfFMlmU94eguINM-33sDm02yJew7lMgWmhFg3qslzavqWzIZS-9t_cjQnvvTHXANwuhbH2Yy-SQHHGCnW7U0GCLFoDPnZvR3Vg-uDXJvvJpC8OdhPfgyxLvGhGdTQ9zmOjK9zzUpQvAwNeSDQeUq3V9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">منطق جمهوری اسلامی
و تعریف «امن» و «ناامن»
میگه اگه  یه کشتی بخواد از مسیر «ناامن» عبور کنه بهش شلیک میکنیم :)</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5777" target="_blank">📅 23:26 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5776">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LLFSOhgH2wK4j9Lv8mE3gA-dx6S_mtfDhojMFzu2ffmVU0ZKtGye0FnX46kpBw1xDZ3w6u9BF8vFT9zlYMKQT7tL0_jW2FGA7XwMD_68ONH9_BOUB_4outogFc5ye-53cGn3zw-VcNwSeIRqAET8pQu05R2sWJjZHaNftvFTorVS1yvS4alE2v8eJcyvBnaFTyHKdWWJx9L2TPn9ISohMyKUsxw9RUKxVfh4hhBhFtA19CBzC0xp9kgztEOa3EuuwVi8nnfDQXl0dzryeDTDkBP3105bQG7ukKO_n-w3d3b07g7rAGqziKy-HV0fJG0-4O4kAYa0IF3D9j9YLwGpgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس: چاره‌‌ای جز ساخت بمب اتم نیست.</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/5776" target="_blank">📅 19:39 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5775">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e4e9d7782.mp4?token=pVIKrOCenS2O_uqGAqT-VldkbqLgfUnqs0K32fTYWUDKwjaOuEqJGp9S3UNz_eD96dbrwzt5K6lxEBgSI4pB5245Fu6BbdPRHNmAxYgcekWzdwpl438bd5ow-6i9O_cBuRh-PRXCJKSYFCVermY5lxH8eooSqxabq_q0NoGpGBO52_y5mEisaDROln6wiIIkF_BaorbN5fHjZ55XckelPE759Tl0XH-yQHaV9I9HTj014L88V2FPZiBZkyaz8N6A6WIJsAROE27GbfAVUzAKYknH5ee70rMG85s27AFN18aE-0GgBuz_RInf_UE2bkK2my6UKOV0K-oFHAvRuI7I5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e4e9d7782.mp4?token=pVIKrOCenS2O_uqGAqT-VldkbqLgfUnqs0K32fTYWUDKwjaOuEqJGp9S3UNz_eD96dbrwzt5K6lxEBgSI4pB5245Fu6BbdPRHNmAxYgcekWzdwpl438bd5ow-6i9O_cBuRh-PRXCJKSYFCVermY5lxH8eooSqxabq_q0NoGpGBO52_y5mEisaDROln6wiIIkF_BaorbN5fHjZ55XckelPE759Tl0XH-yQHaV9I9HTj014L88V2FPZiBZkyaz8N6A6WIJsAROE27GbfAVUzAKYknH5ee70rMG85s27AFN18aE-0GgBuz_RInf_UE2bkK2my6UKOV0K-oFHAvRuI7I5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تیمی که با بدرقه قاتلان جوانان ایران راهی جام‌جهانی شده بود.</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/5775" target="_blank">📅 17:23 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5774">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🚨
شب گذشته یک عضو تیپ ‌گولانی ارتش اسرائیل در جنوب لبنان کشته شد.</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5774" target="_blank">📅 13:06 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5773">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">ولی ما می‌د‌ونیم چرا شانس با شما همراه نیست.</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/5773" target="_blank">📅 10:17 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5772">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1220ffd18e.mp4?token=L8SE1_0AMgf0TelF1m5X5uA6njXqcZbuSvj275I5bEGncgX4UQCNyVXLqErnT-KVFxCVxU9hrU7WSvH6E1F3Vt-z1v6bgQTv7X3o1Fd1cCydivNru_4NMu-lKZKzBq8pBlB3Z7XlF7azM-c6zD6FrTDzjMocx476KAwkQP8_eeWwf2RUbu00ydQU3yn5xX1pGHssf7op_0HwlkBHPquvHD-2eTk7QsRS5Num2qFWzsHV9nKDFavCoLgB9hu5mJhkg6Ktqvmvym6qh5x-usBteKet8jlcDDQvBvUzwzBWWaj79ZZ6zFXreG7t_C9Uz7t4HvLU_obZD3BfB0kLLYCbAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1220ffd18e.mp4?token=L8SE1_0AMgf0TelF1m5X5uA6njXqcZbuSvj275I5bEGncgX4UQCNyVXLqErnT-KVFxCVxU9hrU7WSvH6E1F3Vt-z1v6bgQTv7X3o1Fd1cCydivNru_4NMu-lKZKzBq8pBlB3Z7XlF7azM-c6zD6FrTDzjMocx476KAwkQP8_eeWwf2RUbu00ydQU3yn5xX1pGHssf7op_0HwlkBHPquvHD-2eTk7QsRS5Num2qFWzsHV9nKDFavCoLgB9hu5mJhkg6Ktqvmvym6qh5x-usBteKet8jlcDDQvBvUzwzBWWaj79ZZ6zFXreG7t_C9Uz7t4HvLU_obZD3BfB0kLLYCbAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شجاع خلیل زاده میخواست گل بزنه و تقدیم رهبرش کنه!  ولی اراده خدا تحقیر اینها بود!</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/farahmand_alipour/5772" target="_blank">📅 09:32 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5771">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d645372fb2.mp4?token=VVqdFFOlRJMg9oQP9YsYUN5FOI09QAzpWZ_folYfg69jI0q6EL5v-uvlIiviR6zvkCV63a0K0JZBFSCkVwZRHxYkCafgbCAbBFoI_iDFQ3XaTXDCnzmQgubOxImAa0HQbR7HVY1PdXqgE5fpfBAnOAm-ZvokLE4cO2FKzr851tco6Q3imk5WW_GBi5uS8Cvngzgn4TXpN5EuT0aZc2_fQkMx1lWJyxX-nYMSnGDn7n87jPx0GM1gBqcdnO3Gd9KyflOSBhuQ9DzEBz76IenWuvRekZUBurppom3DTECDOvepYgXSUf_uHhJ44yAX8jEnwj65yVktHrU-QuZ6AxtKCTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d645372fb2.mp4?token=VVqdFFOlRJMg9oQP9YsYUN5FOI09QAzpWZ_folYfg69jI0q6EL5v-uvlIiviR6zvkCV63a0K0JZBFSCkVwZRHxYkCafgbCAbBFoI_iDFQ3XaTXDCnzmQgubOxImAa0HQbR7HVY1PdXqgE5fpfBAnOAm-ZvokLE4cO2FKzr851tco6Q3imk5WW_GBi5uS8Cvngzgn4TXpN5EuT0aZc2_fQkMx1lWJyxX-nYMSnGDn7n87jPx0GM1gBqcdnO3Gd9KyflOSBhuQ9DzEBz76IenWuvRekZUBurppom3DTECDOvepYgXSUf_uHhJ44yAX8jEnwj65yVktHrU-QuZ6AxtKCTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شجاع خلیل زاده
میخواست گل بزنه و تقدیم رهبرش کنه!
ولی اراده خدا تحقیر اینها بود!</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/5771" target="_blank">📅 09:31 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5768">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LNWJSlMmt8kvnLeWEmQJdpPpfBlIzq0PWOex3v_cCS9zOpti9FxwftAFkJgYv2eIZ4GxPwqcxTsgme6m5h21WXfTk7Xv8E_Iev7mnBjIXIaV3m3RSrId_Tdxl7590lVVieGJrxQ79PmbkIspHS_nVz4T-roLTKRaanUcj5ygtNV7cLzroLn07L0ZsixHZKxnncYvZQ2m3Iv-RuyEPFYYWRvAK16QqMkNSPc56aHIYFvz9rnx0IDM0TPlsuaMacF7HmtwasoBLo2q0VjJpWxPFoR9V8FV-7Gktun8olvdDhGf8Oc45kCdXEHlmRW0GSVwk3XynKHMvp06ICo0A4OkMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TqzuWTKDT8zzg9SZ-F4uRf-JiUhtRjgjKJ5OL-nSpQaWU3UtT_QoDZHjD4sFCAbKBqctiu_UuHDf13G98X_YlJ9B35wwGp9YovJw92wv7LzCx_Hi7XCufDZw2KqCprDptj7Kc0AQdkpPAg6rFdbXK0U50LSSmCvSlS3xF4rEFiW-F5eIGM2PFFtbkpa-bjhZs6l-DuDnGOGdAqrTRkNh2Sq4rn95Epe-p29gGH4l3IkC0E6L19jqAb1YJ2GiqfXTKKHF3xZHqHIj15ep4iIanUOD5wWIwKPt89Zup4z6rM4JQNhbsgbfLa1_qXaaXKox-fBemWo6-7ozHANxnUQo7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XdtV9Muj4TSmUmiLMr1X6oLePqcwJyDKMmafBhRzNQFhv39I9z697wHQvD0ExcBa-xHmMhwB4Ydo56G6z1-g1531s62QydopF_9W1K2Gw34mLdElNlGDMDs9uGjLeL1b9WXN3aiHjfit8-7vYLMvWqa0VVzOFD7Fu21sJpf6tlg9ngF5FD_H5lhdk4Tei4PNHIUdtM7BDeqV6F35O0Dno48WI64AMC6-HaQcLSFNSmJRlcE6-_btyJdEG0LreCxatHLaRSjOwJkF-xStdlwAyxUl3eIH6J83DOOOr6CwKeDanb7gwnfqU-vPysbgmgGBALGCmOqp2ogNYgv4INk5EQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/10689e4ea8.mp4?token=Xu7RmuXo9K-_6qFx6lKvVMcScwvAuBtGfknnBFP2-B1n614YhIEPfEDu4GohgTI9GAoYLlF91JPoogdrfSrqDtTRJsd_sXDQwxsaYrhlSf0YYRCEg2M4fOomCyqAMh9XIzfzbTqF2_pug-VHd4yIrPEthzBUsCOPJIb3ExjvZYhrqOTNE8nPkXm5VhA8EuISan2nreZ9sWhh_pn-MbuIGOQnavbZ2WEfi2xgtr5lVVdSJ4T4_5bCxgyS7cliAGwhCRZ2gVBhf4RbH_kAKBpMPs1ZghVmRCOoFH00jh-LcG03nRuXOVqW4Gp4d30FFEozbvZf8UrYjICjy_-X8eyfDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/10689e4ea8.mp4?token=Xu7RmuXo9K-_6qFx6lKvVMcScwvAuBtGfknnBFP2-B1n614YhIEPfEDu4GohgTI9GAoYLlF91JPoogdrfSrqDtTRJsd_sXDQwxsaYrhlSf0YYRCEg2M4fOomCyqAMh9XIzfzbTqF2_pug-VHd4yIrPEthzBUsCOPJIb3ExjvZYhrqOTNE8nPkXm5VhA8EuISan2nreZ9sWhh_pn-MbuIGOQnavbZ2WEfi2xgtr5lVVdSJ4T4_5bCxgyS7cliAGwhCRZ2gVBhf4RbH_kAKBpMPs1ZghVmRCOoFH00jh-LcG03nRuXOVqW4Gp4d30FFEozbvZf8UrYjICjy_-X8eyfDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/17301f18ad.mp4?token=QULzo3rvzxGgtlWKbr09sAjSPdBNLTTD6v4ZnFO0pB-mF8HJbDAFMF1UVBRtzUIfdobam9wrfnicbWw69Sa9ne42x177tzGSmC5cVhwpisHBfiSUOOJNMRHklUGbL7FUhFewM8f9UTea7YYxWrIZVVwR2YwADLb4ZBaVviEU74dHdhA5HZyOfa0mViNiNFiufRGoxSt82afiYFnhqWJlfy8eqPPnJdmJuhT-Fatqf3-Dpm03dm2AfkLJwwDb-VDd3qa_cEgejAl-1W35A2EifYsy_-CMQC17meJSicJSEsXVftGuTO1-P5trXE66yUnnJF6QXMs7wjDqmRYuDLPLaUzXMnnGmdrBFoDlBvoUSoUd6EMmeCl1R4yCPUO39F4m0teXkfs1CmLKJpDI8pfdDczPMWiogZtWtdbRgHs8VAJsabrkZ80tmkmNSRvuW8FGYzpC8Pwarib9txS716XWurSJRVb0b1G1A0M5ZUBasPZWB-a-ptPuQ7WLXSetpbiEJDyza9aXHPPqVwLgoFgglyaUjduQJ8WEZG6ZDY0B-pPwLpoi0kgmSiCGxU88NS-nKbeVz66-RxjJWybGF32iNM1B92X0ZRe8PfWXdVKAOg4vw0bcHN8IMmOY8UIWTBi8wAXNZp4Y16h_pQ1cNcRLvtgfSut2ATSt9EuYsTajrZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17301f18ad.mp4?token=QULzo3rvzxGgtlWKbr09sAjSPdBNLTTD6v4ZnFO0pB-mF8HJbDAFMF1UVBRtzUIfdobam9wrfnicbWw69Sa9ne42x177tzGSmC5cVhwpisHBfiSUOOJNMRHklUGbL7FUhFewM8f9UTea7YYxWrIZVVwR2YwADLb4ZBaVviEU74dHdhA5HZyOfa0mViNiNFiufRGoxSt82afiYFnhqWJlfy8eqPPnJdmJuhT-Fatqf3-Dpm03dm2AfkLJwwDb-VDd3qa_cEgejAl-1W35A2EifYsy_-CMQC17meJSicJSEsXVftGuTO1-P5trXE66yUnnJF6QXMs7wjDqmRYuDLPLaUzXMnnGmdrBFoDlBvoUSoUd6EMmeCl1R4yCPUO39F4m0teXkfs1CmLKJpDI8pfdDczPMWiogZtWtdbRgHs8VAJsabrkZ80tmkmNSRvuW8FGYzpC8Pwarib9txS716XWurSJRVb0b1G1A0M5ZUBasPZWB-a-ptPuQ7WLXSetpbiEJDyza9aXHPPqVwLgoFgglyaUjduQJ8WEZG6ZDY0B-pPwLpoi0kgmSiCGxU88NS-nKbeVz66-RxjJWybGF32iNM1B92X0ZRe8PfWXdVKAOg4vw0bcHN8IMmOY8UIWTBi8wAXNZp4Y16h_pQ1cNcRLvtgfSut2ATSt9EuYsTajrZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/27a845337c.mp4?token=r4uUYk527WBMbWcyonKllI6qFKx_sIphZ2qW5iK2Ro6afIQ6JDYMH--Mlcu80UKKgfweZk61NWnUR3eI9hUG_-NBnHm80_up0jm2H9F8LepylEsH6r5Smujvj0HTxCzxUJth3ZRY5khuIlL5jlSG4rLajmMwlpEVXL5kpreqyMFpldOEU3f9CO0ikEtlzoyEaTvTbsj01u0hZV1iCscyL3ZWvAf_zThFHdHdvh_kt-btNFPVIohKhFDF4OhrXaV8J2zHErw6onBqf6vDXTLIQeIv4nEAdmQwyGNCx_JXdCwrzPs037pkPGUOgXbuZZyErHXKgTmLHuNcCLUWI7jzbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/27a845337c.mp4?token=r4uUYk527WBMbWcyonKllI6qFKx_sIphZ2qW5iK2Ro6afIQ6JDYMH--Mlcu80UKKgfweZk61NWnUR3eI9hUG_-NBnHm80_up0jm2H9F8LepylEsH6r5Smujvj0HTxCzxUJth3ZRY5khuIlL5jlSG4rLajmMwlpEVXL5kpreqyMFpldOEU3f9CO0ikEtlzoyEaTvTbsj01u0hZV1iCscyL3ZWvAf_zThFHdHdvh_kt-btNFPVIohKhFDF4OhrXaV8J2zHErw6onBqf6vDXTLIQeIv4nEAdmQwyGNCx_JXdCwrzPs037pkPGUOgXbuZZyErHXKgTmLHuNcCLUWI7jzbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/5763" target="_blank">📅 08:18 · 07 Tir 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HnL_totIta06Z9MXCTW3_ZiI5vYNsXp21DR1bcFYYbgJvieglPhrna1LhmC19pPMMvBLGL5TV8t80eGK6MXZ-abK8yZwaSOlZjpbn99xW-k_gESohIffG1SQaUpmz85jBzsNih3wbbYlMbKNLhzOkXs_ZTQAVzal5EoLigp4iry0ZyrD7UOO7xOXXhBYSlxOlXtbQr1XV1rXEMBX4jOHA1YJOgtpYUZswGDKSzGtT3sO_l5zWQiVftiDzmXC4w4w4dsIMO831vlNgBbcEk8G1J5gm6bV809zJwCCO93qzG0_syamq5l8QLhe9DSOvQ0kjnDoYEnEYyCcWFc26LsvFw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/0cee64931e.mp4?token=M4lB4JLXoCrTgUWi7_QH_ctNglzJHF4UCrLsHZjQfGGznLYf00LFmi_o5rE8w2tj8zwuZqX-0cx-Ut6WAlRr7Spk0d7ladt8Pz-5Y93WLPBwb2EpgkJvm5DANDIq6_hXLMmqU7-20JZ8jXVJxoShcLF9sK2ZUAoj8PCziJAX6hx4DuosgXJ0uw2rv2FEurj-enwhhgOLxrVqYnurEKogJEM5MmdEH9Fg0FsFQanfP21l4eIbueLVu6KIFovLyrael5W8tZyjMoQs7sO7KdGEgydJH2zzXLgD-SntKeSdztMuPrIDZgE6o5jL0hylWVlMCubiVm6TQItyIWjtdrKXHIc2-poryd_fWtQS_5SuCWVh4vKa5iP7OvzLnnpO_wTvcDSrZ9l20Wet-xpRZw3lUCbRmn6oSP9_9THgFXGYn3m4mDBBccn-n1g7RlACvz1qWFEfZtUcMK-nG5C6g6h6loAZjytcsR_5wo5P7ZyDxrCMZLx_3L2kSRLi7wY92SxivyZvCZP_HO1bVVz-xTyK4oKYJ9w3pV0Jv1rA15ONTKgLEdZ2iPwbBo3S2kb-AJBsyJfFqioXGqBiZeiOpCMImXNLGTtIp3AU51nC9i81Qjs7ANTCZJU0v1T5IhPV4zBNp0R768TXgxKF7pgTYqw37mbVkxtcIx9-icPb8Gm7vrk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0cee64931e.mp4?token=M4lB4JLXoCrTgUWi7_QH_ctNglzJHF4UCrLsHZjQfGGznLYf00LFmi_o5rE8w2tj8zwuZqX-0cx-Ut6WAlRr7Spk0d7ladt8Pz-5Y93WLPBwb2EpgkJvm5DANDIq6_hXLMmqU7-20JZ8jXVJxoShcLF9sK2ZUAoj8PCziJAX6hx4DuosgXJ0uw2rv2FEurj-enwhhgOLxrVqYnurEKogJEM5MmdEH9Fg0FsFQanfP21l4eIbueLVu6KIFovLyrael5W8tZyjMoQs7sO7KdGEgydJH2zzXLgD-SntKeSdztMuPrIDZgE6o5jL0hylWVlMCubiVm6TQItyIWjtdrKXHIc2-poryd_fWtQS_5SuCWVh4vKa5iP7OvzLnnpO_wTvcDSrZ9l20Wet-xpRZw3lUCbRmn6oSP9_9THgFXGYn3m4mDBBccn-n1g7RlACvz1qWFEfZtUcMK-nG5C6g6h6loAZjytcsR_5wo5P7ZyDxrCMZLx_3L2kSRLi7wY92SxivyZvCZP_HO1bVVz-xTyK4oKYJ9w3pV0Jv1rA15ONTKgLEdZ2iPwbBo3S2kb-AJBsyJfFqioXGqBiZeiOpCMImXNLGTtIp3AU51nC9i81Qjs7ANTCZJU0v1T5IhPV4zBNp0R768TXgxKF7pgTYqw37mbVkxtcIx9-icPb8Gm7vrk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جاوید نام ۲ ساله
💔
‏فرزند ایران و جان فدای میهن، جاویدنام علی محمدصادقی، کودک ۲ ساله، روی شانه‌های پدرش بود که با شلیک گلوله جنگی کشته شد.
‏پیکرش را همان شب تا صبح در برف نگه داشتند و روز بعد به خاک سپردند.</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/5758" target="_blank">📅 22:09 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5757">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nkeYL6GoevQQvUx4x9t6DtjGKzcuYPj0t4GVjs_nY8X0GlQIg9GZB3tHVPei2MrlmJxIfvVho-2ISjxjTdI1F-CQX9YlRUYll5y6lvJYeugiFf979CpGZC_IwM3dNLdfVpTKeekRG1VV66mnTJlPNnzkSaePlMeORZD0ymjbp2e5furt4tw9ATGaAhx35UC9YUNg6tFd-_Jr8ce1jqTNc8aTCEHONCk_GpIcXP__62kn5liPqWK1mQ6-FhqRnDOLz0oZhDlWh2ff1C-ogal2LnPvv8UH1Il5soyka-NoA5pNRUdFe0_W5riLOrPs8sDdPEWz3Rf9ZH5OduZzYx5EZw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/db5841aafe.mp4?token=RDL1SZW5RfGW_Jz-Dmd1_tiKTqpjVa_lGXJeaaOTZ0jExcTwXNgFEzjOEj1AYjB75vhaXjAFw8An4samNGSe8lLkWJCqw1dahKC_HfOTwiptZgRBOZd25jqKdSSO6bT0g8gClde3p6KhtBf_z7EjnquzM6I05Sf52HduCiSZnRuI-aJaJxG_V6WPl1zxfIdALa6KqpitF8lIxb-tbjsEAdajW7xzSMjAPRRgsZzjsLbcgULy_3abPNKRyVrzAXjceOpOrG9rPXFU6FfycPMQhJwIH6EM149mi6gMPTXWieGB4bSO5rxZHkBrPov4jhL-yZRYuxs0fF7xOtqgha04bw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db5841aafe.mp4?token=RDL1SZW5RfGW_Jz-Dmd1_tiKTqpjVa_lGXJeaaOTZ0jExcTwXNgFEzjOEj1AYjB75vhaXjAFw8An4samNGSe8lLkWJCqw1dahKC_HfOTwiptZgRBOZd25jqKdSSO6bT0g8gClde3p6KhtBf_z7EjnquzM6I05Sf52HduCiSZnRuI-aJaJxG_V6WPl1zxfIdALa6KqpitF8lIxb-tbjsEAdajW7xzSMjAPRRgsZzjsLbcgULy_3abPNKRyVrzAXjceOpOrG9rPXFU6FfycPMQhJwIH6EM149mi6gMPTXWieGB4bSO5rxZHkBrPov4jhL-yZRYuxs0fF7xOtqgha04bw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">:)</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5754" target="_blank">📅 16:33 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5753">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f038d1dce.mp4?token=eLCjThQADXAQU1NZWuAfZncnDWwIujE-y1zHYEGZr1MdjeO-WJyNSqXBYxJBrP9xs6PSiJz3O2xP-JuModdkYpM_CkI1FUhh0cL42o_E0cgYF45U81_uVqLEOH52islsnxrk7HC9_cEKY3UlMT8G6fEv3Jq5Qpjt6MIRtgi_I5dH_CrJTOyJoNA_00v1To-7hu_yOzsqPOHIqBIsGKmj4WQYZ1OEc-oB2iF7oTM4l2QG0zIUt-yfVT6tii2wddvkVt2yJc8uJMzXbpuApQX5Of5J6pOUdCRsQkvJ8daDdBnO2kJtf6yXkPchz0gWFu3Zi39T5fiLGJumBTQTRxE7mA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f038d1dce.mp4?token=eLCjThQADXAQU1NZWuAfZncnDWwIujE-y1zHYEGZr1MdjeO-WJyNSqXBYxJBrP9xs6PSiJz3O2xP-JuModdkYpM_CkI1FUhh0cL42o_E0cgYF45U81_uVqLEOH52islsnxrk7HC9_cEKY3UlMT8G6fEv3Jq5Qpjt6MIRtgi_I5dH_CrJTOyJoNA_00v1To-7hu_yOzsqPOHIqBIsGKmj4WQYZ1OEc-oB2iF7oTM4l2QG0zIUt-yfVT6tii2wddvkVt2yJc8uJMzXbpuApQX5Of5J6pOUdCRsQkvJ8daDdBnO2kJtf6yXkPchz0gWFu3Zi39T5fiLGJumBTQTRxE7mA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/8b07e212ab.mp4?token=Y3fYhsIcAA5DecKG4p5DSVI-zM4eEyuNtQ7_W9HRD1AQf146myFnfJ8q-ZBYETqOtYYSxV5Tc9Xh64gkFjTes-aa31N9YtHwdwVEq7fC1N7bSNFAm9O9ILAbUmml9BFcqiKgw9M9x549tuo222m-ecLazYeqdaB2JxkRGL_oPJGQ73elhAxWWgacMVshIyR27xlrWw9UT6g8z6ET6N7Iy78M8-VTQDPvpCNUhUe979jtOIVc5rWZwX-7-RDoN87jCh8OVSkwuyTgJPNxwaa4vCmMiOKmYAcy79yoLGdMOWq4udar-xXfSRpkVikZcIRuHLiCFQHgq5w4fJWY2OW3kg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b07e212ab.mp4?token=Y3fYhsIcAA5DecKG4p5DSVI-zM4eEyuNtQ7_W9HRD1AQf146myFnfJ8q-ZBYETqOtYYSxV5Tc9Xh64gkFjTes-aa31N9YtHwdwVEq7fC1N7bSNFAm9O9ILAbUmml9BFcqiKgw9M9x549tuo222m-ecLazYeqdaB2JxkRGL_oPJGQ73elhAxWWgacMVshIyR27xlrWw9UT6g8z6ET6N7Iy78M8-VTQDPvpCNUhUe979jtOIVc5rWZwX-7-RDoN87jCh8OVSkwuyTgJPNxwaa4vCmMiOKmYAcy79yoLGdMOWq4udar-xXfSRpkVikZcIRuHLiCFQHgq5w4fJWY2OW3kg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y6j-UcDETbXuKpOCDIsTULwZFAgHHESOS8FJps9-F38KIP2hrdDwK9iXHSq4igd9VFUJlW6GUVh4D0q4Wmzo8SqH9fDO8TtZatcR9lDDYXzIKibX7Tj1vkdDQVz25vb9zEfC0e8oVgYXTXwSFmT3sHf16g4b8jvrmfxJaYgAEPPTy9vlwXOK1J2ezVEetAP5tG5Jx1gdPQYTOfVO1AYCj9-AGB2fD29wLmJU9NpqjZV-J3T9CjiLhslwqpMy5RWYPSWcgbgga328mpx4J2oYYTyYy1yH9x3Z1po890eeK7Tm-FMngVjiwhtK9e0fPgqhFhyDFv1G5rZta8_2M3Md6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/farahmand_alipour/5749" target="_blank">📅 01:02 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5748">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TD5GDx6NbRvjjA8B59_eZqcsgFoJCX1bTRDDZQG_qFj3VihLT8VyEQhzbWoF1YnyjfljFSp9DWyvGos8kPR10MKIdYshbW-Ozt6qH0ci2xmYBGawyOkTtYVlKfw2GIkyq5JQeugpqUH2aYsnW-WreY2UYV3yLIILugd-6O6MUsHVYaWOo39RUMVwIuIcaJWhPrGJx3_CVsPIZCXcEcfjA_M8-LDKTpCah48gOAMXYmf4qXv_p92f3F3STwIecqnlzD4pQi1VjNELpa8MUJSvFo1fBjwCg2RKUSFkF3XJUwimREey1f1_C_X-1H4g91hSvYS4unW8Wp_Qzu4iVY8spg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش لبنان برای برخورد با حامیان گروه تروریستی حزب‌الله وارد خیابان‌های بیروت شد.</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/5748" target="_blank">📅 00:59 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5745">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e245d71920.mp4?token=I1Ug-dkOqgjr6DNNMCAre6XUsOffe2agrVsIOfwl95-_EvOVxZeBefKH_6HETG64YpZ7SgT44ko0hIyJw8kMPMpFSp0j7P4pc1CFqQnl8UharnXKbCqP_RSbvXgNE347X2z54LOJ2vB9EMIyr3f-EIEyFY4-WbDLZGjhU_hGeLPqHMKCnq9RqLLqRbsSlyBCld-Cx7kB98s_8wd4KDtCTUAi7AkO_tg3YanD4ESXpJoelRyWO73ZYYXuVw94xgOWPQyRy-2iNr8_7ACHPh7UycrTZli5weoiBbWocstNBW8PSQtqBP_j0RDpAaFRjoo9k7XTOo8Y5digpcatQ4xoZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e245d71920.mp4?token=I1Ug-dkOqgjr6DNNMCAre6XUsOffe2agrVsIOfwl95-_EvOVxZeBefKH_6HETG64YpZ7SgT44ko0hIyJw8kMPMpFSp0j7P4pc1CFqQnl8UharnXKbCqP_RSbvXgNE347X2z54LOJ2vB9EMIyr3f-EIEyFY4-WbDLZGjhU_hGeLPqHMKCnq9RqLLqRbsSlyBCld-Cx7kB98s_8wd4KDtCTUAi7AkO_tg3YanD4ESXpJoelRyWO73ZYYXuVw94xgOWPQyRy-2iNr8_7ACHPh7UycrTZli5weoiBbWocstNBW8PSQtqBP_j0RDpAaFRjoo9k7XTOo8Y5digpcatQ4xoZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EH3RyAaLuoIBPjuggNek0VU8NEaC-JZuuvhs_b12o8K5jPa5sGtCvX_LiA26BUW6OQXfdEXoCL72gVcKK8HXp2R5bYSguYLH6yhYuzY_gnFIrfaoCWUpJaqo1fcY5g60pSqf4FNYpjdOwJeuEvIfxxgU_sxbhwZfgtmOAE1sCjf-TREOqm0JFA-2xMbuVo1WsagS8d67WAKoeEdRTWYSQCA0RKHDee20ky8Qv9aU1I28ab5aM7TAiPdfakm69EEnpUmsyJd1JlPL95Nd_K7_IFJp93rwzySeKiqzdvWw2E8juswJXbywfargN9QQr59pKswhNN_E8c5hcCSXG7Ri1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/5744" target="_blank">📅 00:31 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5743">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pxYLZ8EZRUh4mQcTonFjOvT5LAHBUW2H4AVd5UgqxlVwZrJa2A9n7nhMDH_Vl8CTwkGmDQp2rdxcWZ3OkbkO6jIOJFW0oXDgeqgvvW6VTb_Jag-acEu60ySH1pH42hIGBLTfOeIKPRpA5UfoZ7W6GQ4LxT750QGkhYa0pBjmWZgb-QLT4N9KmSkN8CAjd2tddEVQqWWImTaGjkGYxNkDl_LN0iDnvY2y_KmjeOCODxJEXXlO-4CpfeGxwPzWpSJHHpXDg1VEnORy1lS6HKlXIn2NoohBJImO83jJxTAIlF8RN7Gfre4UQ_xLcr_LXPpMCEsez_JWJyiach-y6Zf4DA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/ac9a1f1d75.mp4?token=DZgKw6abEDPYeMQCP2EO0GDDU4xk0CTb0xFQvEO2kvKvm7Sb-Bzuqmi_9SJWRDQMSYukOxT4CKC8soIlu07J74hqrC3m_1FPbl3Mo_9S0riw8voEkSOI59WCmL06iTQsEJ3rxSgrlzKtIkNSG4Nl-ILeiqN0O5SlGCOKcfBzM8GBhnAc6BnaHLvFg4PXiGVQYNVT5YqPUKwQXIW6K6WsZZjGJ_6qCoR6NH856eAJsjMNcPyG78KjXD0Wjc6jnZZpq3MJE3sDDNesMTxfm14eBGMs_HEbm-EdXAUGpUMXq9jKRwPaWa0EcSqjIObWJDlKTPx-GY_3fdj-J1jAfG4vXnZkzQAl3DXbpEV5lRUX7XVECZjGl5-1SPW57avbctnOReidHb4c6_MrowZzm2SQzanz0GUnVGivDEZjpFf-zZHv9F50eydPvskjufOsg_jFccyU8iFWYYVhtYhvGSCrfVxBb_BMqqlx5OANUoSIhGj4oCucWqypDwCXvX7t3C3R2lqVbS8PdyqSaY-H8nmMQOkMn7iJvHDqWVy4I3XBT-vtqgHKqDoaVdDX54nG4Kp1oo6vPQIJ4da1A9BTDZ4dEx5NK01w-avEczjuuUmJLYiWyb0SNl5x-uaRB5Xn0z7op9-ZG8y2XwVVGCI9jSTTNHB5uteonifzjQvW9PnOIww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac9a1f1d75.mp4?token=DZgKw6abEDPYeMQCP2EO0GDDU4xk0CTb0xFQvEO2kvKvm7Sb-Bzuqmi_9SJWRDQMSYukOxT4CKC8soIlu07J74hqrC3m_1FPbl3Mo_9S0riw8voEkSOI59WCmL06iTQsEJ3rxSgrlzKtIkNSG4Nl-ILeiqN0O5SlGCOKcfBzM8GBhnAc6BnaHLvFg4PXiGVQYNVT5YqPUKwQXIW6K6WsZZjGJ_6qCoR6NH856eAJsjMNcPyG78KjXD0Wjc6jnZZpq3MJE3sDDNesMTxfm14eBGMs_HEbm-EdXAUGpUMXq9jKRwPaWa0EcSqjIObWJDlKTPx-GY_3fdj-J1jAfG4vXnZkzQAl3DXbpEV5lRUX7XVECZjGl5-1SPW57avbctnOReidHb4c6_MrowZzm2SQzanz0GUnVGivDEZjpFf-zZHv9F50eydPvskjufOsg_jFccyU8iFWYYVhtYhvGSCrfVxBb_BMqqlx5OANUoSIhGj4oCucWqypDwCXvX7t3C3R2lqVbS8PdyqSaY-H8nmMQOkMn7iJvHDqWVy4I3XBT-vtqgHKqDoaVdDX54nG4Kp1oo6vPQIJ4da1A9BTDZ4dEx5NK01w-avEczjuuUmJLYiWyb0SNl5x-uaRB5Xn0z7op9-ZG8y2XwVVGCI9jSTTNHB5uteonifzjQvW9PnOIww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اگه خورده گرفتن که چرا میگید سگ هستید …</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/5742" target="_blank">📅 19:53 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5741">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fad365bb7a.mp4?token=FGbthytExUGlv7VVAMnFmTdW2bUIzMJvOsp7pkwDL8lVYtKO2oDVE5D20Q0KsyG4SD44BmJ8_L-WU2g-cP21D4bZBnOLcyzxmCcSX2g6dvqZp0VrN-onBZwhIyyNrLnCckiy2Smdrk9uUiHTG3OSBdq6akCLIGCKZK6nv4R0g8NT2C8t4zRz6uO1HkQ6KBEWVHz-OMvyBq27flYBTNYdPEdpFxJEhy-bHYGI66whvt5myxonPcRIA4fgN4jCCtovGNP20hJnbpBqKeUngG2-ZJxKxipqTzLHgP-GLTq_eRqRKd9kIMfYNQxHa7JzE_3Q7-3O-dKm6q2MH3r7el9ETo-oovyrrkxaboU90cloR8nIY-wQpcA_EFh3CUw15M4aHtNurrYDorJNk103fgjdEBot9giqk-rpFxCS1rZBnenfzUNjLlIi3RQ6qHo6aR8eUWxKBVyuCFs9hyzAsfEJkCwCTTdn5qn_r64hQQzOmwdhJ1dEypGXabav5xt2FqQZkHzNQdeCA29MJl1-4ssBWduu8aNPnBetrohR3W2iJo2btMYV3uaRtFgMKj8UWxZXdRMaNz9zhq4OOxX-FRDZ7g3tHtDz4jiB2g0L4Wa1BhY2NJmhq6f3ImbLHMUjL9vvFf4JtuiQHnXJ_FjvrDEVc9h8FfDr4DXxjQEzr1xkslQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fad365bb7a.mp4?token=FGbthytExUGlv7VVAMnFmTdW2bUIzMJvOsp7pkwDL8lVYtKO2oDVE5D20Q0KsyG4SD44BmJ8_L-WU2g-cP21D4bZBnOLcyzxmCcSX2g6dvqZp0VrN-onBZwhIyyNrLnCckiy2Smdrk9uUiHTG3OSBdq6akCLIGCKZK6nv4R0g8NT2C8t4zRz6uO1HkQ6KBEWVHz-OMvyBq27flYBTNYdPEdpFxJEhy-bHYGI66whvt5myxonPcRIA4fgN4jCCtovGNP20hJnbpBqKeUngG2-ZJxKxipqTzLHgP-GLTq_eRqRKd9kIMfYNQxHa7JzE_3Q7-3O-dKm6q2MH3r7el9ETo-oovyrrkxaboU90cloR8nIY-wQpcA_EFh3CUw15M4aHtNurrYDorJNk103fgjdEBot9giqk-rpFxCS1rZBnenfzUNjLlIi3RQ6qHo6aR8eUWxKBVyuCFs9hyzAsfEJkCwCTTdn5qn_r64hQQzOmwdhJ1dEypGXabav5xt2FqQZkHzNQdeCA29MJl1-4ssBWduu8aNPnBetrohR3W2iJo2btMYV3uaRtFgMKj8UWxZXdRMaNz9zhq4OOxX-FRDZ7g3tHtDz4jiB2g0L4Wa1BhY2NJmhq6f3ImbLHMUjL9vvFf4JtuiQHnXJ_FjvrDEVc9h8FfDr4DXxjQEzr1xkslQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/726fb491ae.mp4?token=D8RUDqipkzdt8_m3L0aulFjaUcAIaWer5a2EkzbF9jR78PjunE2DapyWZID0i--QcaQbZAWqPaZjPOlLeXHI0_2V_Q3prNojM9fb5KUumoWJ1TnljFPC2OhJALDPO-lEvO1_K1jbo4_dj6TzeXcKzT79OfZJSzox2dUlgsUmLNL679fYUbE0Q--PHZlBdh5Xlqc1Aa2zLHnwiIQOVJsgUxkdnaRMgO5IYr_8u8Pvv2isHTWZplEpX0MqBm2S0bAbjAEN0u20B4muPx5tTcyrFh4KBtbSvezbcVCOOK5Pxr9oGCod9AQRReT8PIVb0_P9eAtKGjE71pf2vhEkvWXqSYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/726fb491ae.mp4?token=D8RUDqipkzdt8_m3L0aulFjaUcAIaWer5a2EkzbF9jR78PjunE2DapyWZID0i--QcaQbZAWqPaZjPOlLeXHI0_2V_Q3prNojM9fb5KUumoWJ1TnljFPC2OhJALDPO-lEvO1_K1jbo4_dj6TzeXcKzT79OfZJSzox2dUlgsUmLNL679fYUbE0Q--PHZlBdh5Xlqc1Aa2zLHnwiIQOVJsgUxkdnaRMgO5IYr_8u8Pvv2isHTWZplEpX0MqBm2S0bAbjAEN0u20B4muPx5tTcyrFh4KBtbSvezbcVCOOK5Pxr9oGCod9AQRReT8PIVb0_P9eAtKGjE71pf2vhEkvWXqSYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قمه زنان امام حسین رو چرا می‌برید بیمارستان؟  بگید خودش شفا بده!</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5739" target="_blank">📅 19:16 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5738">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e184bbb012.mp4?token=VGdeNaanCxd8NLeguGcutfQamKOUOkftmZJV-jccx923hxCWZxjx9W0j4lZVczt5pj6ffji4t_RraninkNYNgu5hDweCM4iEXt6oLRIhYj4ffTzT9kQ8uJd3hVZoEZJIh7pfGJ0U63h7n8AkAcYgFv50SJZLzgZOVTqElQf7aWZteNZDGyJM_qutxTeOn5oRm585cZo4rogVHchegqcb0Lb-019nP5sZEOg0_qDINTxGpkCMHzKT9eYBq-34AVA51fQui-ryooRVNPUmodtUUS9LRuNGteY6owzb2v2bXy78m4frf1cWCOa2JV_uoT27nXEDp2T6TQhs9jA2zCw1UA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e184bbb012.mp4?token=VGdeNaanCxd8NLeguGcutfQamKOUOkftmZJV-jccx923hxCWZxjx9W0j4lZVczt5pj6ffji4t_RraninkNYNgu5hDweCM4iEXt6oLRIhYj4ffTzT9kQ8uJd3hVZoEZJIh7pfGJ0U63h7n8AkAcYgFv50SJZLzgZOVTqElQf7aWZteNZDGyJM_qutxTeOn5oRm585cZo4rogVHchegqcb0Lb-019nP5sZEOg0_qDINTxGpkCMHzKT9eYBq-34AVA51fQui-ryooRVNPUmodtUUS9LRuNGteY6owzb2v2bXy78m4frf1cWCOa2JV_uoT27nXEDp2T6TQhs9jA2zCw1UA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قمه زنان امام حسین رو چرا می‌برید بیمارستان؟
بگید خودش شفا بده!</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/5738" target="_blank">📅 19:09 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5737">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m_wBGLl5YyU_a1jKBiZGoiGnwZWi_xdUopZEUc-5KES6O8N_dop9qWDq0tOy6oum8GZeIVw4lRurDuII-QeaH1MxthY8lakZYgDDeCvssri1pRPW0jsCfU4G4SgCAlqFdbvi8DG6-SrZ5ucWverbx1f4dr6jg-oJTPSjrojrd0Bf8j6QOF6E37EtOTxwM03B_j7DysP6cETpmq04mqHrULFw7OU-pB8TyPpQ54ay4OqEU3CRwKy91S9_BRTza50_RHiigjKPWIRSLFUo2_gCuY1wfBkPTzaTUA4HWzReez1jj6_350m7U3dlWOR0BSobqObELPPJ_FajXA7BQyfN5A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z2uZ1GhM0bmz40R0llouagH731CWutIDCh1FQzEMACcAeEl_7abh2LlSPmJwGCy3a0tlAqh4roE5g5jiE0RdxGznXKM1hLgCOiO3Qn-F-2naQ4nRBitdvs-UuQVn2sb6AhvaBefvFh8CnaMKo_oTl3Zkrp2lmOSAqkQwH8uwa1byiwv-L3-Jn73cu3HCyykMtnOTLaJhsLDixuOd_YVN49TYRUBAaKiz_SKPJJBK7p19UZX7N-pGA3FGxiNSjqXUNP_wmhIemrI5Mv7AW2rjURT0C0Ur2mKQd79jSveenMAq9Jq9vtxc2kHojhhgMqa7kpxWZCgmpCEZPpsp3K8S1A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tZ2G1-ORyvcIGdRJ_5d2IUj7Ks-LMMYMZKOKhlonfGNHL5cqvg_rOBaSvKfu69sHYiqnGvMxiV0JyFrI9hlL4L3FBhjWagbIc41dMhPBt6R0A4S4fsy2GJqbW1hAm3fjTKM4XHeUqKjP41oGC86A34EKUKI0sMeTsnORySmKKDzElpkXQn4YOM5TzUa3Z7IPfq6BnpHQoeLLcRiGc3-ZF1dyX9htJVvZuLIN-PFBC5hs6G8CohqjtmD-pmiNn5fKU5YBjEAWsB4IvmTDB2sRt7wfcr2ichEhDO66qU4mQwxd7sAXouahVYFJ_g6_564RnUq6PqEOtvuOLxbuAkaawA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر علوم جمهوری اسلامی  در ترکیه،
خامنه‌ای را از اولاد حسین عنوان کرد.</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/5734" target="_blank">📅 22:29 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5733">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TM_00EEdp5Hdx_crc5n0GiBNoXGYtyxFcofiLrX7cfZiWIWWMvn20t26DMgzCfP3rXDhYJx4OL2BwU1QgSXlH-QIiK9YHXaQMKmHvLD9zQXd2h8tIEQFpbV8-TEC_YgV73tnWTKty6vCDHRX2Yh8aJ_UOCgHeKWK62qEdZ-rVeyzkthkrqTB7hW7I5HU26XM_ZT_x_reN_9cLe39Af83l7dHBBJYvmmJY_BTjugmIRK-KUaJBh7IbAanvfev39KFWrw9yFVz6B7l-yWijeRKM8jS4ZWAIVUTs-mZojRa-OoGGKv3LGtYmxdcVjI86khJKyFL8ekIMRLI7GOV52t9og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسرائیل به یک خودرو در نبطیه در جنوب لبنان حمله کرد و در نتیجه ۳ تن کشته شدند. مشخص نیست سرنشینان خودرو چه افرادی بودند.
صبح امروز هم در جنوب لبنان یک سرباز اسرائیلی در جریان حملات
حزب الله کشته شد.</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/5733" target="_blank">📅 18:23 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5732">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/exYVGbsNK-3QtidAu2zoEF_fBZpF9pPHtHByeyUj-7DxzCwqOnCYPPsDwAHLZmqKB-2oDKX-rmVSuc7sLQ3KZdQ-siLQBJEhWWLfDJEC3Ssl87rkFUk34EMwvCyAMaaX-o8VBhhxIPRojjamuZHvRE-wEr9bpqjqbheabAhbrZ_zG7jIU94RDBTGbA-pL43XhR2XVpv9esMUSMWMDAvOTb6w0MI5od-39BU0subsvEiNeUZWF35ApKc8mJjE5_rC7UFLqttNI6FTpUnfSShgFq4ctLNLkrYDTeRBgwagOjh4C9GS99j_q1jB_Vb12BB4A5YUZy8ykJsLflvx6ShxzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صد رحمت به اهل کوفه!
لااقل به دینارهای طلا فروختند!</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/5732" target="_blank">📅 15:21 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5731">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIran International ایران اینترنشنال</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6715f87786.mp4?token=BUW5dPFEUGtkq4vqwygWvCSBKKDUqFq5mZ2oa2zEXxwUtkj7GCyw9GwpdiPMAWo_15k2_9RnDZWTQLjEIENtPA7EbYBwQCtAUNTuP9NA5SOWKUnQpaLvfoPGu2ArxwcGx89ssUcfIeZtrfUrpCRe-o5ASQ2PQ_WxvkrUCIQQvAVX_9PT0yL7SuKQk5F3e9BU02p-ivkl8hXuz0ouV5bFz7WOzQ5I-Emm40zxoTSZhn-Pin5am7kfEbBuJ1tesaCsIcKP4Sm-T0w_qQI81RIaYL_CQgOuPJG24wqlpH9nMsJxpf7cYu4BpIFVv0FXcDjxRzTg3NyYScpbVrwpy5tSUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6715f87786.mp4?token=BUW5dPFEUGtkq4vqwygWvCSBKKDUqFq5mZ2oa2zEXxwUtkj7GCyw9GwpdiPMAWo_15k2_9RnDZWTQLjEIENtPA7EbYBwQCtAUNTuP9NA5SOWKUnQpaLvfoPGu2ArxwcGx89ssUcfIeZtrfUrpCRe-o5ASQ2PQ_WxvkrUCIQQvAVX_9PT0yL7SuKQk5F3e9BU02p-ivkl8hXuz0ouV5bFz7WOzQ5I-Emm40zxoTSZhn-Pin5am7kfEbBuJ1tesaCsIcKP4Sm-T0w_qQI81RIaYL_CQgOuPJG24wqlpH9nMsJxpf7cYu4BpIFVv0FXcDjxRzTg3NyYScpbVrwpy5tSUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیوی ارسالی به ایران اینترنشنال نشان می‌دهد که صبح چهارم تیرماه در همایونشهر اصفهان پرچمی با نام‌ها و چهره‌های جاویدنامان انقلاب ملی ایرانیان برافراشته شد. بر اساس روایت رسیده، این اقدام «بدون ترس و با قدرت» در جریان مراسم مذهبی «عاشورا» انجام گرفت.</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5731" target="_blank">📅 15:20 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5730">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/afaf9624af.mp4?token=BlKyRmXe99QjUiXBNtuEZMJzLngjTxYyYfShYmVb-Vkh1kobi7eogqZ9RIPzKQ49Ar0sweE_zq7WR9CwV0tZwr93iH2NBU7He3Clsq0JxL9CGB_oNp9PtrGPPsH7NvOM3mnu6KV2a159ZnraL0ZE-TIIjBwqLEWFGrIt-dQ1uqeERQ3JwZyaddy6lUNBmNQs1X1URhPqTm9H0vjcYJsJx31U2rP_5YUcejalUFIXqycosMTR_iFI9dagMdMKwzwkMLv9ycFqp59DPyoK6oWL8-rqaalJfLSawGyE7k-BJOQtm-CximC3bwa4fEpeQyDTzc_2L8tZlihk5Z3qgUdo5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/afaf9624af.mp4?token=BlKyRmXe99QjUiXBNtuEZMJzLngjTxYyYfShYmVb-Vkh1kobi7eogqZ9RIPzKQ49Ar0sweE_zq7WR9CwV0tZwr93iH2NBU7He3Clsq0JxL9CGB_oNp9PtrGPPsH7NvOM3mnu6KV2a159ZnraL0ZE-TIIjBwqLEWFGrIt-dQ1uqeERQ3JwZyaddy6lUNBmNQs1X1URhPqTm9H0vjcYJsJx31U2rP_5YUcejalUFIXqycosMTR_iFI9dagMdMKwzwkMLv9ycFqp59DPyoK6oWL8-rqaalJfLSawGyE7k-BJOQtm-CximC3bwa4fEpeQyDTzc_2L8tZlihk5Z3qgUdo5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c0jRiR_6Ki51V51xQMy0GmXZaswjjq1pe5jrd1sQeYAKSMiZaf6yXRu5Tz3jEkhyk48ocQiqZX7II-73zaX0jrJlVzt8rvrxjO17sV_pCfRz8f2fbvlVITfeSCte6I1zdTdIfvFB2p6XUiRK5NI31iiDFs9kV1DHhxr8J_52SOxurE_7se5Dcd5Yo33-77EvC6KLp8TfQH1zKvjiMN1UG9IxRr8bp2jbeMiUhgiMaDjwUNjzFdXw9QPyx4-Ilrj24P6zM0uwu1xXqFLG-u_e2SKoX9NJOR_g5SQtRJGGdsslgC0LCxX2aoLRpTZU6vdEMa18p1nbmsRKikoEvz9gTw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5727" target="_blank">📅 10:30 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5726">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pXwVM4DC6WQXZqGI6f2Pmd6fZ9zae8UcwhJECIqIPDPGPX26-9FoER_drYk89G40th3qHquRjZloOmqb9pAkzMvdsAg57_QndQuoC_cdnZy6l6IMpmM6sfEb2DbQFLZD3GxnUzYW8JK2luU6MTmBrx1IC5nJ7XKGwOHi4lYVfXr0HAoV5cJ_cdwHXfpH_X7VGEcLtYeZzLaKVrPdi4YR2TQoRV5GN7RadNboe0hwxPyAP3zzY1Ea6UhDVoiEM-fkHjpSH9RSOuqSqgpyJh9hnjSQiBW-jUiQsMot71fAMA-WN4Fl3VRSKzpkcXb3FyiG1-wU17-t5Z_k5ITrtf1AAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرمانده گروه هکری «حنظله» که در جنگ ۴۰ روزه کشته شد، ولی خبرش الان منتشر شده.</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/5726" target="_blank">📅 09:39 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5725">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/86c17f6d3c.mp4?token=hOgCDsNQKR0KkQbM0Hqbrc2xDXLC-GAISW2G6uBcQ3HtBEw_fueLmp4UTCfY94dE1i56u6gEm4WQOEdRizCdxWCDA9m34SckmlJNwib2VRd4OAZmkILx_cw2gWKUkKKOsj3djVdAugVYFlMVb_TsPA2D3yFoQrs7zBt9Mcif5DEJpODMzrWYdBFIZEATazyMZlQpxenEDBiBw54mDA6GWRVcELBnK48iwgI8HBjKk0vI7bpZGY2lcYDCKj1eP1f2bInbEj1-DNnSYOFKcHA-P8ZVweBem1bclWKWEzK4n3z52rY9MdS5Cn7CrR3eg5x2Qpp0pA5kbh1tHhQOtsQXDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/86c17f6d3c.mp4?token=hOgCDsNQKR0KkQbM0Hqbrc2xDXLC-GAISW2G6uBcQ3HtBEw_fueLmp4UTCfY94dE1i56u6gEm4WQOEdRizCdxWCDA9m34SckmlJNwib2VRd4OAZmkILx_cw2gWKUkKKOsj3djVdAugVYFlMVb_TsPA2D3yFoQrs7zBt9Mcif5DEJpODMzrWYdBFIZEATazyMZlQpxenEDBiBw54mDA6GWRVcELBnK48iwgI8HBjKk0vI7bpZGY2lcYDCKj1eP1f2bInbEj1-DNnSYOFKcHA-P8ZVweBem1bclWKWEzK4n3z52rY9MdS5Cn7CrR3eg5x2Qpp0pA5kbh1tHhQOtsQXDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
