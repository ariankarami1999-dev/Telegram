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
<img src="https://cdn5.telesco.pe/file/ZEzTZQGvM9NxmsM2Qm5055YaR0sFNFYwMoiiUsJvzvmx5b_EBeMtBCyLRd9pd7a7QlhG-y3DWv5avILRclvKBuXpkYlfaHt_YIdDX_2hed_qDe_nOQqq9zjc8MmKn4fza_7sRwhgiBP-Oou3vHFvmK6QDjxn8349LS0k4bV38JQEei1uV1qGe2zWEv5_Cjbra9isfC7AgyXv_stE_O0gCjlZbqSMrt9dB-LR02Yl87mx3dGwP1WF_XA8sLB5Rc5zctH8JjI5p0t3Y8pH5jnYcO85Hantv_s4c34q6aRKYNNQSvxZazOU8b-WfxYFJxGSXZBnpajlgrKaCi4ATdwqQw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فوتبال 180</h1>
<p>@Futball180TV • 👥 478K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-19 23:37:40</div>
<hr>

<div class="tg-post" id="msg-103292">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rCY-1ehmcze0Z8K2EzFz37kg3eFfgCzu2nxQ-iCobrReH943pz_RDL3Hc5xwYw1x76jtWFnCBWDPaRuPjrAWLunFROQJ7dksjc2WRowzoyx-TwLTowHcOIESE5K6BS7dw6xW38OG4B9ueNPhKPOfkOVl92VFz1US_aev_ap_fS3qODyEENpzVv4WhXaSdTp20TdMU3V-gB3g24W7JzTeIAMUpV3900dw5F7_rpXBMw-tFKEuX7gpomkKLTSoanqxFw8dBYKJaPEagzIIleoBphOXVsCMM-RJ8n0cmTg72NoB_FYhiz5L_1dKnd4f2eq9vLEw5w2iNWLfNVLxLLBSIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#رسمیییییی
؛ قرارداد میکی‌ون‌دفن ستاره هلندی با تاتنهام انگلیس تمدید شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2 · <a href="https://t.me/Futball180TV/103292" target="_blank">📅 23:39 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103291">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec95bffbb1.mp4?token=nZFL94Mzf-akqYkifPF7LVh5UXI-D_n2eN0S1k6d1e3fXNYhf-OvzeEkim_Asp26i5RyOm6MxMgoBeyUU6PHnm0DUKLzAFShywdDNvzS5mQ_IraHGXL8rlC6nQ_yOx2eU3vAXwMnL3y0sowh4rkINhjewl110kXpDjt_zkHcl7hAv8AIN9z1T3L5C5Vu0-mssDSs6Xr5rlQ8EJq1Y4yW4jShml52L_FWANXPnq67OmTHozIIhNKOMscknxHCfpP81csm5sF8xwlEDzWT06HBPsUWB2R_LRhVx3vEAMCMwC47CasAdQY4PJLxv8i-DffHLuQIHavj28KNI2rRf3LlAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec95bffbb1.mp4?token=nZFL94Mzf-akqYkifPF7LVh5UXI-D_n2eN0S1k6d1e3fXNYhf-OvzeEkim_Asp26i5RyOm6MxMgoBeyUU6PHnm0DUKLzAFShywdDNvzS5mQ_IraHGXL8rlC6nQ_yOx2eU3vAXwMnL3y0sowh4rkINhjewl110kXpDjt_zkHcl7hAv8AIN9z1T3L5C5Vu0-mssDSs6Xr5rlQ8EJq1Y4yW4jShml52L_FWANXPnq67OmTHozIIhNKOMscknxHCfpP81csm5sF8xwlEDzWT06HBPsUWB2R_LRhVx3vEAMCMwC47CasAdQY4PJLxv8i-DffHLuQIHavj28KNI2rRf3LlAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
❌
میثاقی: ممبینی مگر هافبک چپ است که با تیم ملی به ترکیه رفته بود؟
تاج: حالا دیگر رفته بود که کمک کند!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1.46K · <a href="https://t.me/Futball180TV/103291" target="_blank">📅 23:37 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103290">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/586f4ea605.mp4?token=fwdEuIkBanA9nBs-CSIiOKb3xTWS_ImxDL7bl75wI4Rd2dzlBbuBQJp4PLi2KaivkOyQ3jYfEIDd3NA1xWkwHwexdmWfKAj2kdWdDMEMXlLVrJ0ckZHVMWoUa2VnywCcQdyc0bU1-B6c267ahzn2mDmHAK64c7M-L_N9fdEo58ZdvEM-GO-S9e-xqRxQEssfQHCsVGpgyMmpq1rpI0Uap5F99weiKCUaJH1fItf26FSmX7Zv4iShM-vN4RFCGf8Ibkhuimpe_o37CoRjmXSHbQG2S1QSCN3yqgJ_Z95ZvdshMAKUevm2cShmOpyE3LrHEjxsW7FdNL-RQGim9x53QiGx3Ndj9ogAuxyGNUeud72Ygu0QDL6C36e7kbNTIPN5u3OL2Yt4lKMswoyE92yPR1v9MsZK_QoWOSUZJUg9XEtw3gZGVmpx9pU94m6rjpxLSVSwp_MsWRp0sCKmcaXzgSOjXVD2Q6hi5pOqnLHi9k-PSSB_jEMEwXTcCCS45456daKP_gjCxu3mDBPcRRIRwYZDXaLHFnfyT--82ElrjwsBYrL4ej0mBajIdfbCZb_GnHn96oYnCViDscjWpiSxOKd3y3o7E2bxMnCVyGGzBYuSGoOzaR7YesXTuserAbiEC0-9BF2dvSoAorcrR2AiPCd364e6rUUH_qW4zaUbD3k" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/586f4ea605.mp4?token=fwdEuIkBanA9nBs-CSIiOKb3xTWS_ImxDL7bl75wI4Rd2dzlBbuBQJp4PLi2KaivkOyQ3jYfEIDd3NA1xWkwHwexdmWfKAj2kdWdDMEMXlLVrJ0ckZHVMWoUa2VnywCcQdyc0bU1-B6c267ahzn2mDmHAK64c7M-L_N9fdEo58ZdvEM-GO-S9e-xqRxQEssfQHCsVGpgyMmpq1rpI0Uap5F99weiKCUaJH1fItf26FSmX7Zv4iShM-vN4RFCGf8Ibkhuimpe_o37CoRjmXSHbQG2S1QSCN3yqgJ_Z95ZvdshMAKUevm2cShmOpyE3LrHEjxsW7FdNL-RQGim9x53QiGx3Ndj9ogAuxyGNUeud72Ygu0QDL6C36e7kbNTIPN5u3OL2Yt4lKMswoyE92yPR1v9MsZK_QoWOSUZJUg9XEtw3gZGVmpx9pU94m6rjpxLSVSwp_MsWRp0sCKmcaXzgSOjXVD2Q6hi5pOqnLHi9k-PSSB_jEMEwXTcCCS45456daKP_gjCxu3mDBPcRRIRwYZDXaLHFnfyT--82ElrjwsBYrL4ej0mBajIdfbCZb_GnHn96oYnCViDscjWpiSxOKd3y3o7E2bxMnCVyGGzBYuSGoOzaR7YesXTuserAbiEC0-9BF2dvSoAorcrR2AiPCd364e6rUUH_qW4zaUbD3k" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
⚪️
تاج: قرارداد قلعه نویی و کادرش را قصد داریم برای جام ملتهای آسیا هم تمدید کنیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.1K · <a href="https://t.me/Futball180TV/103290" target="_blank">📅 22:55 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103289">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ltDwVrZ4HsQRUltZbg3oxkOI4ejmLAduNR-XhCHSHcsTq6UX_zKKjJLlpFtKMsxWS0qJJa_hGBi5StiUG0d9WMrIeUN2euCm-YgeYhEhBZQHYgT-1Hnww03VGIyJiJGK9tjfQZPdXP_kSusRvTj8XRmMGTe0ah7DXRSIcSJ4LL04KvJuZvyLtQU2fIj04xsfbie78b18cssfXVH_YKsrFkOB31BtXCl3n4J64TRz1zmagy-WmGJnhHnDwrzr8iCpRyFrsgMpwQ3knLuRChD8uniBNjsEp4dZQOlwK4shK8CPDa3POn3lQkMMUwq58bOcgXnWWk-0Xf95830kWS6xLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بورهان خبرنگار ورزشی مشهور ترکیه به دلیل نشر خبر دروغ انتقال موسیالا از بایرن به گالاتاسرای بازداشت شده.
در حالیکه مهمترین رسانه‌های فوتبالی جمهوری اسلامی (فوتبال برتر + ورزش سه) در اختیار مجرمین پرونده فساد مس رفسنجانه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.37K · <a href="https://t.me/Futball180TV/103289" target="_blank">📅 22:54 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103288">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pX93_-de_7U_xAJBtCJMQOlnWXykWvUvDsOZ4tS4p71qHGFRB09tz63ohJ-uLRASbJWI-oJNQ62jaUPx5ZHHEBl-JubNCh5O7bHdpdI0wKEqp7pyeaL2zophBIlqCb2F89oCjAcyUOnu_wY2EMTkamjQoGotgqYyQTcZcxe_BYfLKzZGB67M9eEkRWt-ExyWf-HuDyJ98d_IN2BJfgwU-MY1DRdzkfAy7HShSJSNX9LPLvTIrynwkRhChi7fmz9oUTPtIVxheHGjVSYmfo0j5tVCErcBDdGmI_ZuGWxRE1bGFBVEw0Im-5G9Nn4SmhiYv8emR1NKKG6NetnAEjUAxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🟣
مارکا
: اینتر میامی در حال حاضر محتمل‌ترین مقصد نیمار بعد از تموم شدن قراردادش با سانتوس به حساب میاد.
🔺
اگه این انتقال انجام بشه، یکی از جذاب‌ترین انگیزه‌های نیمار از نظر ورزشی و تجاری، دوباره کنار هم قرار گرفتن مثلث معروف MSN یعنی مسی، سوارز و نیمار در اینتر میامی خواهد بود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/Futball180TV/103288" target="_blank">📅 21:55 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103285">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kaLT95Jsxgn59Yl_9rb2-zIIs-vuM4BtZ2-diFrmOegpZnA6iwsMpvWG2Sihk_H32iKTA74Qz4p5Ptf9fHrYTudcyCb2GY70wIQB0N870NqZU0jBgaHWp-tzdr_BI2FlWO3QusbTbhZfECxB5qp4Ho3iXWgLTMBQLsU3nG9efmzhZcAk9Ls81JMYi5e0IR5dphqz_rghLc7W5r4aUgrFyZJb-RA8YeCY3ygxS0zTv5gWUveGeqpReKgSI057uBAaFIm6ezfiMbqSxSrSpSFxMERqJWpOHrLT0jlD3EfbDTpqayvqdrW-94nH6yGpxi3J_AUXsL7BnpjksrWrfxuDgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OOTbrofyuh_ShM_AHgakCMO8zdrds7PROFEeEPIyxV-19I9uRD-KgZG9r48Npozw00znMjRHG5PkedD_IPq70m7QOXR0a86L1evnjTcICJzVuxgjYfKSkVPa9eBNqeqrSV_eMcKQpjm-6aBASX5SeETUfodUptyKUyu5olnnCCuFMXh9pSplj93jOcVxLSYcY5tyAi-n06kTZE5uSEOkpwuFwz7f-at1HLqTD2uFb9n_ynb9QhNp0G_BG8Be6xtHpMzrq0yWjscl6hFIZ3GGqNTzA8bghf2Tvywac40mK2hKCSLGtnj1NqyJ4OBdc-Hnb829zvDo-KqW8d6WlQW7Xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jd4l2XQ3LSuPSfYs1_ts5qBz95yhTmU4aopdaAPT55Ol0dRAjaprcOTmS58-MlvBopQItOhAzIVXD_vSTvTkV7pXpAgkTCRWRgN9fmnVlULiK1w0ycKfpQdk_lmEClwFcq7hdT8-wiZH-TS7jNptWnw9MZUyd1-3rD0T5GMJly4Dg3M6sQ9uc5Cf5h36UrHsyJwAFxXbOzuhao9UC8mhgSVhmyQxUJ96k7hfnWjTSwkUkKG5xWPBRd1iOAw8a-r-k21vQRbTOnLeWj1HLeprNxuhNMv_B5NbjClhjEEGJBRfB5GwpXQW-f2H5q14JBulAW-n5oVe7zMFrN7pts84PA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
✅
🏴󠁧󠁢󠁥󠁮󠁧󠁿
اولین تمرین رونالد آرائوخو در لیورپول
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/Futball180TV/103285" target="_blank">📅 21:54 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103284">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
🇪🇸
#فوووووری از رومرو: آلوارز امروز با وکیلش جلسه داشته و گفته که به اتلتیکومادرید بگه فقط میخواد به بارسلونا بره و راهی برای موندن نیست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/Futball180TV/103284" target="_blank">📅 21:49 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103283">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🚨
🚨
🚨
#فوووووری
از میگل‌ گالان (وکیل ورزشی اسپانیایی)
🔻
احتمالا‌ آلوارز از اتلتیکو به دادگاه ورزشی شکایت کنه تا بتونه یک طرفه فسخ قرارداد بکنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/Futball180TV/103283" target="_blank">📅 21:37 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103282">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b_P5LPKfFNv_1qvEz9bPu5i7MYWsUhi1y2zXfgei7ZXrFhYcZdy_Ov-1T9Ctk0_8JegG-PevmY34fSjeKd1QnU3rYwOo5g9q3Zo6TMIO6PXITBoR921YJXWGXaZtWaL-z9myVONVylqgYhJUvgunB4ygtRWiJbTVHCn9qYUMYWofZIuXcELv8LgQaqRIT4uX22uHGN6LAtoyPljC_6lgGnE2RqAOuhS-LCfFKEBLrcPLy9tK0ln5zhyzq7wCjShplYnB7U1gvQ8psU9nyvxIddn-XTIZ4Oenf7cNk46jEKMJmrLAzpCVkrHkquSgbPK30dvyzwmf-MuZHXqgbYgdow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
🇪🇸
#فوووووری
از رومرو: آلوارز امروز با وکیلش جلسه داشته و گفته که به اتلتیکومادرید بگه فقط میخواد به بارسلونا بره و راهی برای موندن نیست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/Futball180TV/103282" target="_blank">📅 21:20 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103281">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NWGR7cXEv5gjg_IFJMIOPlAjwB_DG_fdpQAx1o2AGTccIt0BxtrjyfPVUz5jGeaYLGAEaO2A_o5ZqDxaNBiTw8SIr0m7y-d9FytsB56R71XwVgLPr_-Sr52HDG4njuXMiX92gUi-5f3MkOuPU0fz93lH5TOpIATh33VIIc-i68Jy7VKJrLN17zZcELjJxjv-4dzsUVUASgLy8KlxotKO08KoeYJTGG1ad5FMbgzMBzJdlZm1kPiHxC4L1JhJQ4g95yPF7v6goFlljhKSXsuw5N7qFqOZtFv9TXZZN5uAR3saMpH1-j4oaJg43eialnjV7IqxsdhC-yK_pdCE3BjA1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🔴
رونالد آرائوخو رسماً به لیورپول پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/Futball180TV/103281" target="_blank">📅 21:03 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103280">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hADcj_GLQzZ11_chpRUQflagxN-JltrnvV5ovxnZfa95kSiVEwz4ZgrvSUHksDPS7Qp8dbzB-WB2zLjfCn1whpDvBLrHS_T3H_-nNgjMrOWH6FmrLYNTSmF7tKXdSWpSZrTd6gx1eSv7PvjLA4r32UR3NCIj29KmzwvL79CaAaNZfkm0N9kgIiCjt-vi9LrUz0S3Um9OYnKGV_U9ILjSYF0OF2Jzb653UCPIxLRTV8yglfoMCci_K7tLXmCVSnOfXxuVYcoKvPiSTkfMdarsZGZnO4t86H4p81kaa84dMJ68cmskrQZ2UU71VO8XpCDpBgZRvMTRDPFakHQSh5rqJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🇪🇸
رسانه TNT برزیل: بارسلونا برای جایگزینی آرائوخو به جذب ناتان، مدافع بتیس فکر می‌کند. بارسا در مورد امکان جذب این بازیکن از بتیس پرس‌وجو کرده است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/Futball180TV/103280" target="_blank">📅 20:58 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103279">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eAsZYZttSNGYa8MyAkJwf_PXS60pCqCQqnFPgrvnZHsjfuhXB7lkMMXZ4lF9LEEp7gVLNvW5JcNrVUlezWo0Pol3oMZJ0HeuTCNf6wgfrBK7bQfL_tFSNRdz5yWTmhjKKmUx1s216E51XbXAb5gkllwX0Z-P8oA5_W3Sf6w_w0t8QU4FV5XJCCpjKtF6QHaOsu_p2Kj3hUMrwpku5RTYpNGNzY5hCrd4wpYieuX4AyKcrZbiaibVdWjE6fnvAbUsDa7WpCb2KmqCnlYNQqPU0kNxmN3NmmkrbcwAKZi4wJQPH61NjG7VjJ9QkItfTRolQ6iMTaublCPy4zwftGed0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
پائول هیرست
:
⚽️
منچسترسیتی برای فروش رودری ۷۰ میلیون یورو می‌خواهد. بارسا اماده است ۶۴ + ۶ بپردازد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/Futball180TV/103279" target="_blank">📅 20:41 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103278">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IcHD9nk5nfW8ZGhJY3hqkXXg5KZk6lsUzOfMOh5WtBdGfYLcAZTQrnL4pmUGldnJQQ428rZw7RtSShi-f9rGJpBZJSeKFWo30UgZI8d0NXmG03hJoFli7A6Ny-nIG5zMQ4UlL1FO-RafLt9kL2-cD26GmWNGo4lCR9lWPq2kiN4hjGRd9L4eiwIeNwtKn3-I1KSFU1WCDYJ1A2l5LTTkES7UmAOF4bKH87BTjhCh5XYOr2K7lbsqGFbFII0CLBu044hLacgdFkaq1By-XPqsHLbdF3_n1FobrEprIyzXdMSdapWAWbjM2_UOLGULtbM9mEZWv5qridIqnrUoPHXJrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
😐
ترامپ:
ایران خواستار غرامت خسارات درگیری نظامی ۵ ماهه است و من هم از آنها غرامت می‌خواهم
چون سربازان امریکایی را کشته اند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/103278" target="_blank">📅 20:12 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103277">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VfyvTqOR3rS5ofhycTWhWbdQ4mcFb9E4wvOYujAcYjxxcRWSGZoo7NZv92ghbVobuSTPTu44toW0LF2zBj-A-1nkRSOXN9KkiH4LX1meBfGY-k2G6W0aRmnzuIkkdO3uSaPkOQJlovPFgFAXRacoMS033pOll1G0QQ1djk61H9wyvukTJnUhYOUStHnOOa3rlpIhVgLgbJ2nNaA9MxSOsw7z0AaEfM_jxesleebajrp2QnlkNxE5ACC0AngS1-UWAKxNrOjZncnXVHmtQ_SRRGm3z61_TJbS67To_krQ99RvrDcxYwCw5VHuZVHaF9TKKaOQHU8da5gnr1Q26DwknQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇪🇸
#فوووووری
از داوید ایبانز:
🔺
🔻
لاوتارو مارتینز پلن B  بارسلونا در صورت شکست انتقال خولیان آلوارز است. هانسی فلیک و دکو از او خوششان می‌آید و این مهاجم آرژانتینی را زیر نظر دارند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/103277" target="_blank">📅 19:55 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103276">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sSvCLk13EK-Nq8x9R5fINvjlGp0Op_nN6BG7vad1mj5i8wsfovPkXcIw-ET44R-1T9kt2t934KyvHy-6uTW8YKHduQWDMKM0s5cMCrT3H8W64j4cP9jcrzI_Px70Tp60jVxWGY8pS0xoGk1Wxumg4kxP5nRXh7lj4RL-Nrw-CQIwKDOfj8fCV2ubj6b59UQdxk_j6dk9Hx_mYy0N3XHyZTz89gt_hLFwyMBOfDdhzob1bVMD5RClvuYpwSCzvSYdLbRnDojeBTm00jQqlrlsC-XsmEfmJrSQACDckIM-xRLzBuOA9QgMg8z7UCNqC5hdVDii-fyjD6TFo5QPNfhKNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پریمیرلیگ در این تابستان بیشتر از مجموع چهار لیگ اصلی دیگر اروپا هزینه کرده است!
🇬🇧
پریمیرلیگ:
۲.۰۵ میلیارد یورو هزینه شده است.
🇫🇷
🇪🇸
🇮🇹
🇩🇪
لیگ 1 + لالیگا + سری آ + بوندسلیگا 2.047 میلیارد یورو خرج شده است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/103276" target="_blank">📅 19:37 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103275">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pbdb454k3Y6hRxw9qfdOYK5x1-dGB6dhplrKsjLwigmao3r8AKGsdEM07eg34WjM_XbVZCutE4AwvjWrIxw9vwjMhwmQKfpZJ0KZv_MT8j5sPwBmii6oxw-18f6PV39r0iCR7RwYVfL2xQ7QihPYUNkOka7dT8aqbUV-72F6Zl0bx_YCng9rrpLpwawdV3UVPXSmkKgh6IKoHL2iB_eru7iMhyOcv1FL6vX6jUhcSx0pff9caH1rUmJWSeyDF61S4Bg9VmdQUiF7KMOfJO-jdX4OlX6NBKXH7TAD3pFs-7BfxajWFscPepwgdIpaphsS7wOI_fl_TySFBeW8Bnw-0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
اولین بازیش برای PSG تو فینال سوپرجام اروپا مقابل تیم سابقش استون ویلا خواهد بود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/103275" target="_blank">📅 19:24 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103274">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8023c35480.mp4?token=Gb6-NBjbcW5sxHZ0wH4WFAOjpMQyylrjQOqsROm1o3xsmHW18NLaS2Rve2pSlCvcwviQvVERyuva7xofwgoWbBQHFcFNgvjyJMhftJrKC7dl_U2c_zB0O84HcZolgA_JXuLwRt8HuZAa8hyjeM8dtmF-bVtciLlSVzLp1QPjbKDdZbpHwARqKPfsFChY3xcmBqcUKFjMqHi8SWjTfjxERgPo4gvkPOB6HjynHcLt0Q4gmrQ4CPC8Vfds4oDmdheX7w4gDgLYbrKOjgpxj5OFybXolUrGnwkj_Rjy1H4cvrgsh0ulRNNvLgVJqBqWNUVDtY_qg6wyChS2gxTSnrnC8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8023c35480.mp4?token=Gb6-NBjbcW5sxHZ0wH4WFAOjpMQyylrjQOqsROm1o3xsmHW18NLaS2Rve2pSlCvcwviQvVERyuva7xofwgoWbBQHFcFNgvjyJMhftJrKC7dl_U2c_zB0O84HcZolgA_JXuLwRt8HuZAa8hyjeM8dtmF-bVtciLlSVzLp1QPjbKDdZbpHwARqKPfsFChY3xcmBqcUKFjMqHi8SWjTfjxERgPo4gvkPOB6HjynHcLt0Q4gmrQ4CPC8Vfds4oDmdheX7w4gDgLYbrKOjgpxj5OFybXolUrGnwkj_Rjy1H4cvrgsh0ulRNNvLgVJqBqWNUVDtY_qg6wyChS2gxTSnrnC8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شاهکار دوست پسر استر اکسپوزیتو تو اولین تمرینش با مورینیو
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/103274" target="_blank">📅 19:21 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103273">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5629191c63.mp4?token=Hskl6n4Asfk5cjAc2ygqzY5dD_Cv42sj-R95Lsr0_uU4aEeG3Injg-zX8N_e53_6whOSRO4NH_e3iyCvWjhTWSmi5_wI1sKF3SMUHTIndFwTh00ldV4GzAVoPOyVvUK48En-d1BYxQ_qLaJVB2FCjuX9_vJzQBuht0EuNL2jIw7hskDwJ5I-HiOwY1X68XttCg88QFewBuJySgDvzO7xK7s0nOf5i6aT_1InZDQhOdxLuyliXI2TapJIUqXmKgbbYSgldmx3TPmWGhkFAjYpd-8tXGs3wUtXuJPuPu3FBebfITN9_Tiojd1hXcMMiTRWel_Z4gAM3vUoorbaduXb1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5629191c63.mp4?token=Hskl6n4Asfk5cjAc2ygqzY5dD_Cv42sj-R95Lsr0_uU4aEeG3Injg-zX8N_e53_6whOSRO4NH_e3iyCvWjhTWSmi5_wI1sKF3SMUHTIndFwTh00ldV4GzAVoPOyVvUK48En-d1BYxQ_qLaJVB2FCjuX9_vJzQBuht0EuNL2jIw7hskDwJ5I-HiOwY1X68XttCg88QFewBuJySgDvzO7xK7s0nOf5i6aT_1InZDQhOdxLuyliXI2TapJIUqXmKgbbYSgldmx3TPmWGhkFAjYpd-8tXGs3wUtXuJPuPu3FBebfITN9_Tiojd1hXcMMiTRWel_Z4gAM3vUoorbaduXb1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مسی قصد داره از تمام خبرگزاری های آرژانتین به دلیل رعایت نکردن حریم خصوصی (تصاویر از مراسم پدرش) شکایت کنهو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/Futball180TV/103273" target="_blank">📅 19:19 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103272">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ps_zI2c8kTDfObPE_jSlvNNbC1_IPDz9pRu_KF6f67SVFgWxNEjb7u_fo3htf_EnyczGDRwZygiFMyaRaXqPL2MA3ARnlrWsaxurRRu7WEMgCR_2uuf2CxU02AzkmCWluDpJ9OYL5lNS8TJ_YjK9Tyt-zhdBO8TqVN6myReJ4NiacnEFlhkgQRh53NeOVea9YVc6wvmEfSX82nbrYLyPP0sMW1r-88HegZE56sQBux07Kc10sS9ymQ28Ulh2d55slkEIwqlVF5RAZbC1F6pIx3aNEov0WXbfnGSRx9KuWOjfXpfb8xtjwyrLa30KyfqZLO_L0tEVoBX2mDiug5Fn8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
👤
علیرضا جهانبخش با عقد قراردادی به اکسلسیور هلند پیوست. باشگاه اکسلسیور فصل گذشته در رتبه سیزدهم لیگ هلند قرار گرفت.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/Futball180TV/103272" target="_blank">📅 19:05 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103271">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/29f11cd214.mp4?token=WXIvnCArD9tz5Wc_jy7w4-V4owwfzwVlL2UH7Nw2Yit8ClZ4cmwLpiO0Twz6FAvNhvSrc-oUY2cVxJ4rabicXEqTjXfMRTT4cftJ48LLc2sT1UJIijTKK8OXSdCKj0fMyj1FwoF0K9mfzyGvptmkqVrP8KcZbhN1AmboluFcGg6-ibAZoL_Lr-OYYGvdJMoc2C3GFKpyCsKBRjFjstD-J5y6XK_POwLDfX2Ub4ejRFTmeXm2Ljpcz1v170Ev5qnPOnp_Eod1Xcjq-pD_7xsPJiEC6hbpLpoljblkHVAptD8LEwhHG9Xrr0M7pnOnS2hjkIVrYbtTv9lz6mcN9k8ckQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/29f11cd214.mp4?token=WXIvnCArD9tz5Wc_jy7w4-V4owwfzwVlL2UH7Nw2Yit8ClZ4cmwLpiO0Twz6FAvNhvSrc-oUY2cVxJ4rabicXEqTjXfMRTT4cftJ48LLc2sT1UJIijTKK8OXSdCKj0fMyj1FwoF0K9mfzyGvptmkqVrP8KcZbhN1AmboluFcGg6-ibAZoL_Lr-OYYGvdJMoc2C3GFKpyCsKBRjFjstD-J5y6XK_POwLDfX2Ub4ejRFTmeXm2Ljpcz1v170Ev5qnPOnp_Eod1Xcjq-pD_7xsPJiEC6hbpLpoljblkHVAptD8LEwhHG9Xrr0M7pnOnS2hjkIVrYbtTv9lz6mcN9k8ckQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😆
😆
یجوری پنالتی زد که فقط اینجوری میتونست جمعش کنه..
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/Futball180TV/103271" target="_blank">📅 19:01 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103270">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17c6dda8f2.mp4?token=RNPBvLvJqeUY4CY1U715j1wOsZ48sOvpJlQkv3MOrNRJnMQi-nY1u68V6yMjOigXlx1haJRewT-ujp9nrUr6bOX9CxkA_ER7fAJPaA1yuukZhL7Lap41-B3xPRs0g2qTUfZ1VFsi9IlFOzzW1w4-M5a5ZCWBShcOsFwoHgJv2qtkuHAqFQjDRBHBwIjihxoMaAkkZJPIybSx94B5VrfMver-ejzZQFjqpmTq1EEDPJFCCK_S9v2VJe_5F-VTICncF4Dx9kF_a7eVbQo_P8o8OKrk_kSitwDm-LAeDJ531M_tcPIIOS25t_0XRToeyjUpzJm428KUOC6TaPgZHkJCsw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17c6dda8f2.mp4?token=RNPBvLvJqeUY4CY1U715j1wOsZ48sOvpJlQkv3MOrNRJnMQi-nY1u68V6yMjOigXlx1haJRewT-ujp9nrUr6bOX9CxkA_ER7fAJPaA1yuukZhL7Lap41-B3xPRs0g2qTUfZ1VFsi9IlFOzzW1w4-M5a5ZCWBShcOsFwoHgJv2qtkuHAqFQjDRBHBwIjihxoMaAkkZJPIybSx94B5VrfMver-ejzZQFjqpmTq1EEDPJFCCK_S9v2VJe_5F-VTICncF4Dx9kF_a7eVbQo_P8o8OKrk_kSitwDm-LAeDJ531M_tcPIIOS25t_0XRToeyjUpzJm428KUOC6TaPgZHkJCsw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کی باورش میشه رئال در 9 سال گذشته 300+ میلیون یورو هزینه کرده تا برای ایشون جانشین پیدا کنه ولی هنوز موفق نشده.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/103270" target="_blank">📅 18:36 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103269">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sMMSeY31QiV70_kah95PnX7v9BCO1nJWLPPVicdCuKMG2cdXH269Bn7QHD5Z_u432ICW7waPU2r9ZVRi5D4ww6iROr0qXBCfeI55E0VAoqGJ7__WiXPaxjFI96Tx196M3py9v4mCDWUVqbVT-GtzNyCnZl45cLWTg2Ieu5C2-YMUCDj9LuixTEgv1trJtfzughGos9GfOXvwpDSOGnSweOk3kTkMj7IjrE6MuyBOycu8gISThwTlkKSnWBw-ZMQ5xvEneyGZtxpXGNJRcZX3Rk8pr7goX5W14DUHbeTF5XTjgG1SSlw3EhAi0ymwqjrO3pH0ilvw_e-NW9-7BNdhJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇬🇧
باشگاه‌های پریمیر لیگ که بیشترین حقوق رو به سرمربیان خودشون میدن:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/103269" target="_blank">📅 18:34 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103268">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qi3y7zv9TfXYcp_femcIhCvrWoSMeIKTMv4lWrDKdSBYk0TMIRU2vi3bS6vnrvleT5Zu4g0GSnluxCnshM-BpaDno6NTdYF-euvfaJp15zJzrFAJimadUUYF5qdJyz8471SWfKMugilZu_ToWl2mdLRkyceexuO8QfcTynLerLrbHHrLO6e-E_D9XOgLi0gwP75Xs1dURTGQ8HO4E5tYsiyV-WlvCc2-NxNgxO0TPJNgJTXOEki-pHhSUsyP4okvqCphHTa44Yym_ys5Q8pXVKsQLCTT_oSQe1UWUvH3oq8M5Lj26pEL-tSbQKyt_G-Bc9IXFfqJKkcIBimjm715tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
⁉️
فقط یه فوتبالیِ واقعی میتونه هویت هر 6 تا کله کچل رو حدس بزنه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/103268" target="_blank">📅 18:20 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103267">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tb1ladMD6vx3FvBocIDRt-xYkpCQuGV_5wc8rYZajA3hLFWZOkivtVpGBzIIdVG5Id-eASiqjI6HAre5OjR45dGD8L-R-EfJIZ_alLkY2T4KFN3Akg8cptjgRw3J3F4t_gOIIHUE3FQJKZ8q242SeMb9d_UoPMrMsxHJPRIrbPMGJom_f5HK1vjPcHwsRuTwF4R0knV8HXCHomrah_LL2UwlcIt5RK-sfqdCezpYFgUrIeZP3g87jBe_eoVqs1OL3wAoV5rv62laH2CZdhDjbMQF-ndDpELmRvkPEG2P4-YXT0Cb-i4T31yAxnvT8y0o90db7wWvxrMtJxR7GEQFDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وینیسیوس کلی پول خرج کرده روی صورتش که نهایتا شبیه کینگ اومتیتی بشه :))
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/103267" target="_blank">📅 18:06 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103266">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ad5bakeJRG0vdgeFld3ePhCtBpGgZ5kCO-8PycamtwGmGY_3DIO6blz0UpqErnGvTvTSpgENEwZdJjHmhBraBJfR63EK6VYrZSLzm1SGP6yMcg08xVOz96ReOEzLYW_6nrYwffODTNRTfZmt1-_ARtRsHgrURQ_nInes7Udhu7jpAvyWIenI1RDUg_zZMFL8xR6W395CxrVBL4cYwfACN03f4RMMsb3DDzJdZNDcjmbJoAgFo1sZS1Lq6RfYQJVI47egiAJaDKgd6Pei5OkgKNpdcfDYDtMowo8SRjv_d6EUiJd6s94Uf8aLsbDfPS19yAUy9m3Jbdk4CYDVxRa2YA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
👤
علیرضا جهانبخش با عقد قراردادی به اکسلسیور هلند پیوست. باشگاه اکسلسیور فصل گذشته در رتبه سیزدهم لیگ هلند قرار گرفت.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/Futball180TV/103266" target="_blank">📅 18:06 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103265">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">app (7).apk</div>
  <div class="tg-doc-extra">53.1 MB</div>
</div>
<a href="https://t.me/Futball180TV/103265" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🙄
همه بت باز های حرفه ای دنبال
🔞
شکار این بونوس ها هستن
✅
لیگ های معتبر اروپایی شروع شده بهترین فرصت برای جبران ضرر های جام جهانی
💯</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/Futball180TV/103265" target="_blank">📅 18:06 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103264">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W4A095Rrg12Trlge16LWGypGodoBVQk6bLSwlgyG5SHv1SXG4SbEEuGQ0pBdPb6Ymctulhq7IP1VEAnXM_MyGkiJL5I83cyUyzBeL4bY_AoVliWUBkp1bPyLAqi3m3LGqQr29AN6m9dEBzdUo9jdcAPu24Z-IOqO7UYUpVnj3IdGMkQcriARy_e1zBplnz1ahBUaLaYXRIPU7NsZpugIn5IPKzIVI4sBo_oEt4iNQ0-5i7GNPWYnaVqlFm6zvtTYffIoXd6fVXHcfII-ietuuCFJ60jTijViAeHFP0WXgX_4nrjo1IPT-ez04WGOsFImXstwApXTT5SydqMDju12WQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤔
شروع رسمی لیگ های اروپا
❄️
🆕
بهترین فرصت برای جبران ضرر های جام جهانی با جشنواره رویایی مرداد  ماه
⚠️
هر افزایش شارژ مساوی
2️⃣
1️⃣
🔣
شارژ بیشتر بدون محدودیت
☄️
به همراه
🤩
🤩
🔤
کش بک باخت همه روزه:
🌐
betinja.bet
🌐
betinja.bet
کانال بونوس های رایگان
g19
@betinjabet</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/Futball180TV/103264" target="_blank">📅 18:06 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103262">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dikhEfWGcNBQKK15Ljy8mOBuFtf_PWTtL0HabWdZF0yp2jiVrZIJh-vVYvgR393_XqKtUl2KKYJuy67AldW7YzYu2aUqqTfT0CpMKgrQX9RNBTA7uMF46ayZdsK6jGBV-035dMOXuFcN86aZCEtOZx5un2FZCzn0hPEGOGIJcK08KQjbSLhPQjKje517gvcFXwmLcszGICRIwYDFB2mzTZF77gsSiA1TJah6c--vOKDzHjUBOsVhhbCt_4Sm1fxiaPNS5MyK9Hkl-giOj5UWvQR1PiwXX2YA_xoHV9vdbOSi5zQk0PVWFNnJTVEVpFyK6qkqYN07jWq1zbNyvVN4nA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/naF0kF_3kt7bLmkP4I1npCBTGCMnixGV-yRKrVqESbAqcDZFxbRM40JSDyL_YnPdKEOaQlwYH2IoDaV-j-mVY4PYkWGBbohts_QcmN3Ezooxv2X3q_SueoLiUgrpfuFRgs2Zvp3md1yL6XZ_LRrClZ-XwAa1KDvugs2SAfmxG7kNLCQI-Imex0NeMkCwN19rRHqWzUSbaLZeQWGVA3M0Jn-z-5JJ10dsDaBOQE6MYJcjdMb90zyE5IWYRa6iTNS79yN5bwHNrngJY-2UZXaccxt0JZQ_oOhDNF4zj7eCC9wW82OxzaOm-qeJNXEN8zono6PcsNO4HAzbh--w5SlqOQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
⚪️
رونالدو تو آخرین قرارداد خودش با رئال مادرید، سالانه ۲۲ میلیون یورو خالص درآمد داشت. رونالدو ۳۰ میلیون یورو درخواست کرد، اما فلورنتینو پرز از ۲۵ میلیون یورو فراتر نرفت و رونالدو در نهایت جدا شد. وینیسیوس جونیور ۲۵ میلیون یورو درآمد داشت و پس از تهدید به ترک باشگاه، قراردادی ۳۱ میلیون یورویی امضا کرد. پرز بزرگترین بازیکن تاریخ رئال مادرید رو رد کرد، اما برای وینی جونیور استثنا قائل شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/Futball180TV/103262" target="_blank">📅 17:44 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103259">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/p94hdlgbH3wN7TMs6LjuaOfDjwp9cJguloqvSa9ZqQuzkWHJ8xzsSTVU6c3zOqR2geMeC8LrCE0ic0Q5hn4qJ09kOQxt0Ru_ixD14rTAvO7gMe9ZNTj2o5WjTLLpKei1udM_5T6lDHBtfrxZF_RQAjZZ-lvTn_bZ65zrQWBmhHBORUAVJBCH7Pwh-gNOYk9kxWGJ298n3XVyeJCkXIbL-YczwD6JA57DLQxoKKwzmvFd9Ewi-xllUfrCrN9zjN5J1LNh-fYCNuBN4inlKWvsWlB1_HMXXsEofsAEDp9KncfReJGtXRjcJwpYGzHIdLQi-l4y6WR2rrF-5ZJ0m-a_pA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GTa8CNS1zIPI9QJ8vIEMhNYhrqB6EHigLRyCmIZsOJ5Nft8Uxc98oLEAGPyBeIakwCmHG3bzGIqQGN4icn29SOUboDy_EYlBAFV903BrdrqphBS5orz92gn-qEHFwZV1RDeO2G8xslfMWScgYfGE5QlcvUrbsn_bNAtslyfBDt-cFAazQCiM75Zq7ULezSE4-8JtlqBZqSCE_osgMEEjmh31HeGnj_uDJTS1ibcjma1d4Aw4mey6Iq4pCA4ZzbwiK9LY-uznONzkq-2OOituA_VSTZRHB6l10b-eEfdvQxTyvYxA5ecOPnb2Y1s-MvHg9A8hV2VEaMx3osY7UJKVaQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/71c6e02cf3.mp4?token=GBaoLPg-M6YKakj3L9Bom5Sva1JY5WDO6hy4L9ObZaWRUJVID2uQIGnLiw3JcfhnZ6vHRt8XGya6BVkArwm3RHXjH7acw3l_jy5r7OH_EXWrfO6U8jvirWPIu5Hp23VJpOhLESrmN-3u4LE9YA963R5as6t-7p1rx1EWkb9AwIKzhosKgwWUaSPB_16a39P3XY5Yh55lpkqAlcYyDM31B1IBF3k3Y3IZCAz4abm2sobuwrrC2EsACgTR9l4quEwhpUU0TpF4JeXhS2yGPqjfkwkSkC4MQbXK-YS-54RJbdpEXXsbBJy6V1Ea02WqX2zMNMkswQ2x4gdvGhl_7AJigg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/71c6e02cf3.mp4?token=GBaoLPg-M6YKakj3L9Bom5Sva1JY5WDO6hy4L9ObZaWRUJVID2uQIGnLiw3JcfhnZ6vHRt8XGya6BVkArwm3RHXjH7acw3l_jy5r7OH_EXWrfO6U8jvirWPIu5Hp23VJpOhLESrmN-3u4LE9YA963R5as6t-7p1rx1EWkb9AwIKzhosKgwWUaSPB_16a39P3XY5Yh55lpkqAlcYyDM31B1IBF3k3Y3IZCAz4abm2sobuwrrC2EsACgTR9l4quEwhpUU0TpF4JeXhS2yGPqjfkwkSkC4MQbXK-YS-54RJbdpEXXsbBJy6V1Ea02WqX2zMNMkswQ2x4gdvGhl_7AJigg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پست جدید بانو جورجینا
🍑
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/Futball180TV/103259" target="_blank">📅 17:38 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103258">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LZv37qQHlO6BJ0QWTyAKeuMGobjyZnCGn_r9MmGTfAuVgbW3ZPYPCLpzv9qbGM59HsDPK5ooJaL9jbGdYmDp5T_XNvRQ82fOnLBbCYEKjgSSD69p2uah9cOfX-fjJxb93H9OHDl2oH6xBuPqUIeZlEISKPl6qBl3sxc8LzfEHVemtQ3-GVYNw9GheO6-ZfSLNl56TPMWhPqtl61SobbeWaG2nU1yJ_fkqR7drZQj2Ztu1Mx88GVSNCVCQceYSpRkoTG2vK5ICvvZ9iXPn1LvMw1RbyrqndtKFcTg6T_GheJXWaJCSjkVA4YVRvcwdkY5wBQ6Jv7UExBI5Azmlwyl6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚑
🇪🇸
رونی‌بردغجی بازیکن بارسلونا در تمرینات امروز دچار پارگی رباط صلیبی شده و فصل‌جدید را به طور کامل از دست می‌دهد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/103258" target="_blank">📅 17:14 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103257">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9099fd2879.mp4?token=QrB7-6hK6jZ8i5IkmrUxnOSYNQhma6hbZVL8nfGbmUHELs-rHPnn8UQRhcPHv4CbvYlbDi8NtIqX2uxLiPVRLlb3NYoOxF87bH8zQfhImZkeUJnziBKB14cOPfB1_DQik-z0GOHeh3K75E971z-n_nd3gej1jTSHP5bIhGW1jV3vkTly6iQrb_xDjEL_9u27bxuzNAzrO6-7ZfSAaetvWqdckd-JZN-m6A88pQNG6pSuAvxVog5caKLVRhvb7p45kmLZFYjAg4aon_EhQ9PK9O3HCSfc_1yew_r1ZdRtDbnPnnOAV9_88ivghNrOktba8iFhqnh0VmXEEj0sk-8RFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9099fd2879.mp4?token=QrB7-6hK6jZ8i5IkmrUxnOSYNQhma6hbZVL8nfGbmUHELs-rHPnn8UQRhcPHv4CbvYlbDi8NtIqX2uxLiPVRLlb3NYoOxF87bH8zQfhImZkeUJnziBKB14cOPfB1_DQik-z0GOHeh3K75E971z-n_nd3gej1jTSHP5bIhGW1jV3vkTly6iQrb_xDjEL_9u27bxuzNAzrO6-7ZfSAaetvWqdckd-JZN-m6A88pQNG6pSuAvxVog5caKLVRhvb7p45kmLZFYjAg4aon_EhQ9PK9O3HCSfc_1yew_r1ZdRtDbnPnnOAV9_88ivghNrOktba8iFhqnh0VmXEEj0sk-8RFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
واکنش خبرنگار صداوسیما اژدهایی به کنایه‌های اخیری که عادل فردوسی‌پور به‌وی زده بوده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/103257" target="_blank">📅 16:55 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103256">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ujd4YgIQ49WvHsIDgmwN6jKkqW_O4J8Na6hjF3jbOLYRdYy1PZmd2JKS1hHkY7oHCMDQHjbGCzqt7k5AVSNy9cRzwjsNMX3ANs96DzilqwzXtqtj47Tf0veqUonFj0uN77eByza9y92GtTMvAMFbenDpYcTsjBi0OBu0Uf50KTbUP1PLI6G9lazaUyhcqwT0PbUQXMoG4Us17z_zoMgaNUYxQvQzPqhBmIZd4IdUFUahyUZw13G8eFgEP35N44nzxDT1DJ583liYKn2ouD_BfotuxgpFXRJ1U9FD90dQzq7EHK_aq0I1M4nsSwo9GeShtds3DQNkaELa7cpdAYTtqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
اسکای نیوز:
جف بزوس در آستانه خریدبخش زیادی از سهام لیورپول قرار داده.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/103256" target="_blank">📅 16:53 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103255">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/86e349ee52.mp4?token=MDJqdGibwnP1jC8eMDUowMXpagneGa_C4qFTnnTvtYQGsK2P7g8BdbN371-EO07dmk4o9jUi8aVCV-TFnmHJ-EVwFxpVl0paooUcunUH8XkvIPVxgN_8c4iBuaEeYiBKu7Ii9Ic7g5IGgx8LVVXhRDOVTeR2hdfU5bW_7NhGSEPs4-Xld9e6F-XdSao77OBdfuF-Hkl5aSw8g_0bZ0MxcpRQ3U_S7tErvb7-8zmvne75im3wgcQC3LsEkR192sr7X9pSEugnpWaagEm-eWVK2IvJZPK14hdbflQgHZlhqLtk-ZTeOG6OqJVfz_nmnxtwJ1zPkgBkDWscA0nsl8-9uw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/86e349ee52.mp4?token=MDJqdGibwnP1jC8eMDUowMXpagneGa_C4qFTnnTvtYQGsK2P7g8BdbN371-EO07dmk4o9jUi8aVCV-TFnmHJ-EVwFxpVl0paooUcunUH8XkvIPVxgN_8c4iBuaEeYiBKu7Ii9Ic7g5IGgx8LVVXhRDOVTeR2hdfU5bW_7NhGSEPs4-Xld9e6F-XdSao77OBdfuF-Hkl5aSw8g_0bZ0MxcpRQ3U_S7tErvb7-8zmvne75im3wgcQC3LsEkR192sr7X9pSEugnpWaagEm-eWVK2IvJZPK14hdbflQgHZlhqLtk-ZTeOG6OqJVfz_nmnxtwJ1zPkgBkDWscA0nsl8-9uw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
خبرنگار به نکونام: زیاد تعریف نمی‌کنم شاید فردا مجبور باشم بکوبمت!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/103255" target="_blank">📅 16:33 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103254">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🇪🇸
Xavi and Iniesta
🆚
Italy
🇮🇹
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/103254" target="_blank">📅 16:05 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103253">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a709379c25.mp4?token=V3Fe51frv7DMPoCqc5Lsbi8waB6N8RLe7GRewYuGaIbIxSq9azlaNIUDaLvfpkXF-4Rh7FCLvotPpTEOavwOWK4Shsr94PfRHWq70s2LroOgAuCkpdr2VyRamt-Eq27Uaqw9sYYxLQ1o0Vhv5STb03KJDZxd8AXdi9SS3uAix7qJovyd-4eVhq77ALiJjIRkUZb0H8JbCM7D2i-5dfYcATRICoXdqrqwaKMnfbqv0PJtpmQYWrQgnOTm9MiMHatKcWjbgSoiJ6PhKU7vYrcZRI2MLNYgI35n8UwAs9pFDQxgl-C30XefignLltXdiQ6fFZHGByOANvOlWytVZbXG6EvjWJ5u6MPIYDAbhFfMTLKImgH950mJsEpnBIue1tCjwEqcaimdllE3691or8YC25hPHV2ypkNKtYhd7giMkWCeBZxnGJ8dpg2azQMtTkYWMaND7UuGz8QHH7DYUHdwVZ4EEQOXFZrw4QSDCfv42YtuSlTYDR1j4SL-1PAbtqQes4AiU0ZalXkmSolSexzh2FH-1L9muRyvOKltiIZg75jg1TtbK0YzbF7kKiZlEiSqbKIbIGMKpBRP8W_kz4I6h5ucUIHyoUbZO7NmfjzF4_pwTkM-ZzRXH-Hf-MaD_zGNxeqEaXV1UkXCmm6qSRurOKZjDeGaj5zsy0UMuD85614" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a709379c25.mp4?token=V3Fe51frv7DMPoCqc5Lsbi8waB6N8RLe7GRewYuGaIbIxSq9azlaNIUDaLvfpkXF-4Rh7FCLvotPpTEOavwOWK4Shsr94PfRHWq70s2LroOgAuCkpdr2VyRamt-Eq27Uaqw9sYYxLQ1o0Vhv5STb03KJDZxd8AXdi9SS3uAix7qJovyd-4eVhq77ALiJjIRkUZb0H8JbCM7D2i-5dfYcATRICoXdqrqwaKMnfbqv0PJtpmQYWrQgnOTm9MiMHatKcWjbgSoiJ6PhKU7vYrcZRI2MLNYgI35n8UwAs9pFDQxgl-C30XefignLltXdiQ6fFZHGByOANvOlWytVZbXG6EvjWJ5u6MPIYDAbhFfMTLKImgH950mJsEpnBIue1tCjwEqcaimdllE3691or8YC25hPHV2ypkNKtYhd7giMkWCeBZxnGJ8dpg2azQMtTkYWMaND7UuGz8QHH7DYUHdwVZ4EEQOXFZrw4QSDCfv42YtuSlTYDR1j4SL-1PAbtqQes4AiU0ZalXkmSolSexzh2FH-1L9muRyvOKltiIZg75jg1TtbK0YzbF7kKiZlEiSqbKIbIGMKpBRP8W_kz4I6h5ucUIHyoUbZO7NmfjzF4_pwTkM-ZzRXH-Hf-MaD_zGNxeqEaXV1UkXCmm6qSRurOKZjDeGaj5zsy0UMuD85614" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نیمه‌نهایی UCL2012 و بازی جذاب بارسا - چلسی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/103253" target="_blank">📅 15:40 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103252">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1fbe5b387a.mp4?token=jgoWL3GUAHU-Bs9E0F4O-KOBEAsv2UD3uEmx4McvCG_bai0BAL8erdTPJGt1XChn8f-lxsFcebONqs8i1zfulqB6hySNMBGnWS8vk2ZCymoHz_mSX-8gjlYk1LExx4ksUQ9b3cyFSQegUBCnpMwO88HONOJfcpcopu3e-uku9cZ6NcsOfNVWk6bFFbWkNAvjdXkgwObPn_OxA0KOQh7Bir77_xvpZskgnswIJXEfLaKvt2pV14HOUa1uIvSbJh5QjdYlUTL4lnsT4MkOPd-JVZviasGmg1jdJVKdummoyCuTxRohecmsNXGQ74yckJSoJtP4cKew7ES2H92I3C4FEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1fbe5b387a.mp4?token=jgoWL3GUAHU-Bs9E0F4O-KOBEAsv2UD3uEmx4McvCG_bai0BAL8erdTPJGt1XChn8f-lxsFcebONqs8i1zfulqB6hySNMBGnWS8vk2ZCymoHz_mSX-8gjlYk1LExx4ksUQ9b3cyFSQegUBCnpMwO88HONOJfcpcopu3e-uku9cZ6NcsOfNVWk6bFFbWkNAvjdXkgwObPn_OxA0KOQh7Bir77_xvpZskgnswIJXEfLaKvt2pV14HOUa1uIvSbJh5QjdYlUTL4lnsT4MkOPd-JVZviasGmg1jdJVKdummoyCuTxRohecmsNXGQ74yckJSoJtP4cKew7ES2H92I3C4FEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
❌
ادعای خنده‌دار وزیر ارتباطات: به اپراتورها هشدار دادم که هیچگونه ضریبی روی بسته‌های اینترنت قرار ندن و باهاشون برخورد میشه!!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/103252" target="_blank">📅 15:15 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103251">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d8870e38c3.mp4?token=DMxdd2iNKehJAlRfIrfQ5VtClWvcCwsb9WNo5jIDwnWC0-80YuSDQru6f2KvugCFgFpdSxplNU3px5BiAo9R_KcOZl6QIOsRyrIcXe5Lq9XOuEa1-RAEm8DhmEMhg6xX1c7qjeI18KRgV36uLgbUtZ9JHRrZWyKzgwkaHCSmLogTvAootPOKZFkIJH7eRUmSi8JTiJr9It-qbHQiB8uEsWAOZZAB1cBM8_227EpQcgXUMQmYRIQ_tHKcE_tsNCaBk-tnMVSYajlIFh8rAyksc5kkXZPdGvi2nJ48YL3MRL-_cZTkYe2h6ZbyQF1XQm83DbrRnz1aeM9YJR_q41w20w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d8870e38c3.mp4?token=DMxdd2iNKehJAlRfIrfQ5VtClWvcCwsb9WNo5jIDwnWC0-80YuSDQru6f2KvugCFgFpdSxplNU3px5BiAo9R_KcOZl6QIOsRyrIcXe5Lq9XOuEa1-RAEm8DhmEMhg6xX1c7qjeI18KRgV36uLgbUtZ9JHRrZWyKzgwkaHCSmLogTvAootPOKZFkIJH7eRUmSi8JTiJr9It-qbHQiB8uEsWAOZZAB1cBM8_227EpQcgXUMQmYRIQ_tHKcE_tsNCaBk-tnMVSYajlIFh8rAyksc5kkXZPdGvi2nJ48YL3MRL-_cZTkYe2h6ZbyQF1XQm83DbrRnz1aeM9YJR_q41w20w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
🇪🇸
امباپه، گولر، مورینیو! این مثلث رو قبلا جایی ندیده بودیم؟
👀
🤔
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/103251" target="_blank">📅 14:50 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103250">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vsDMaGuhulaJpVe8x3c-Ehm0DDaJbJAPpD7wuTBKYfoJJNUj25-rr0QmW-MaW2on0TRwLmGjr4FYatqP8JZgzJhsNYYPD2Dz0JYE3eBkpRqMfDZZEZe0IKrMG7ttDs5Z3bkRTngBr0drd9dd_3dRiSY4HRAGwj7B8WgqNk3A5oA19JZU3ugKSKwZgS9g02V-pbBroJeZFeknkd2FUsC69YwNTYrdQOeYAl-oYCqKaD7JKu7UpNJlGpxUNmLjFElmX7ECYrby-fGjovNaW46scz5_44TQEXfYetjo72QTFUh3Q3LkaFsXlqlpKSmvXHfJKN0b4uNkOcIutrBpGTNWhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
پس از تشکیل تیم ماهیگیری باشگاه استقلال، تیم دوچرخه‌سواری استقلال نیز افتتاح شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/103250" target="_blank">📅 14:22 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103249">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hrzau2RriuNtXxUEB_tsPFt9hn8uN_mXJM1GTJ99iJ6xKksn_h07ImIKrv-GQgyz1qtyBu5rO_asEj08cnJKt0Ozy6NfZaOP1tVzL9deLOIj5gIzzqVVjxOx_PIaZ2unlUULNXDEDlOR0tUILuuw8RUhuZHw_4-PssJOSNOZjbKCGD3MKGFRyhvEwChHZ6_fhyHqD6vTnJhYnAz-Dis_qUhr4pjL5xzhtZmGtzagfpNOrScJZ3Ynoz2tZkvV6qvSXDJ4cJtvKLhhyy7my8J3M8E4QQNuu-K9Vyi1FlW6YVgm8ENBVAj9OtNiBBwoj6PY4N7GjZ4F3s0ZiWbOP3UmDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
🇫🇷
#فوووووری
از متئو مورتو: بارسا و پاریس برای فران‌تورس بر سر مبلغ ۵۰ میلیون یورو به توافق رسیدن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/103249" target="_blank">📅 14:17 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103248">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🚨
🔵
#اختصاصی_فوتبال‌180 #فوری
🔵
باشگاه استقلال با چندین ستاره‌جوان لیگ‌برتری به توافق نهایی رسیده اما تا باز شدن پنجره نقل‌وانتقالات آبی‌پوشان، هیچ امضای قرارداد رسمی صورت نخواهد گرفت. هرچند شانس بازشدن پنجره استقلال کم است اما پیگیری‌های وکلای خارجی این باشگاه…</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/103248" target="_blank">📅 14:09 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103247">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b442857f8c.mp4?token=FoEQtjiIsZQFXCj4kdj9E-D0kG1ZLg4AH8KLI1SuNn7ZHOL4UOklk0mAPJ3jEXFJhKnt5zWvOokWilbSRPHY2lSWqXUpcZ5RPsvltRGiInHHnETpbwac-HZ5r3e8fmyeg1RmgrI75HjSeLMU6-u5I23UaYktGqK7JdaCkEFAcsZYVIKsMiZCeMAfyOh5JSa2EF4LMDloQ2ORjvTMUfowFfQNhScLOUThPQOvrxA64ifh5xxpravkq9sNbKp5Tps9UMiBgfpaMC_YocTPW54ohgh8pJ-I-M_By5zowZpxzsnd-Qin8k-SlzQrkjhQv0vIb6bL2CcQLbvSaYFl4u7fnHBVVO96jhuOvVroM7T08Yp_le4TU35hBj2D9pEmaHQXss2_d0EMfRr0pGjUGD9Il4ZY9lRrb9HSkAtHaxUC2Y_oWrE1bz6xm6B8NyaJbdW3KoSF1wJSY2aibRhY3J60lA0lIsLjsoayV51o0NOkbQF64YJAF8JoMRy-674FaOe04nBzJIkJmsaFn2DfrUpWc5nj3lE3LocFrpI2HorPdtcmI6Ie2iDImqR_ZTaMuE_en5W_PjmzyKxQFq8hPL3wKuMfvjzfR0mSBrEblnGXhwcJrBsgSEeimHgtSIoAZlbnceBfenuC86ieszCc_1-6gkllRjOL_SE54Jbw3vETLao" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b442857f8c.mp4?token=FoEQtjiIsZQFXCj4kdj9E-D0kG1ZLg4AH8KLI1SuNn7ZHOL4UOklk0mAPJ3jEXFJhKnt5zWvOokWilbSRPHY2lSWqXUpcZ5RPsvltRGiInHHnETpbwac-HZ5r3e8fmyeg1RmgrI75HjSeLMU6-u5I23UaYktGqK7JdaCkEFAcsZYVIKsMiZCeMAfyOh5JSa2EF4LMDloQ2ORjvTMUfowFfQNhScLOUThPQOvrxA64ifh5xxpravkq9sNbKp5Tps9UMiBgfpaMC_YocTPW54ohgh8pJ-I-M_By5zowZpxzsnd-Qin8k-SlzQrkjhQv0vIb6bL2CcQLbvSaYFl4u7fnHBVVO96jhuOvVroM7T08Yp_le4TU35hBj2D9pEmaHQXss2_d0EMfRr0pGjUGD9Il4ZY9lRrb9HSkAtHaxUC2Y_oWrE1bz6xm6B8NyaJbdW3KoSF1wJSY2aibRhY3J60lA0lIsLjsoayV51o0NOkbQF64YJAF8JoMRy-674FaOe04nBzJIkJmsaFn2DfrUpWc5nj3lE3LocFrpI2HorPdtcmI6Ie2iDImqR_ZTaMuE_en5W_PjmzyKxQFq8hPL3wKuMfvjzfR0mSBrEblnGXhwcJrBsgSEeimHgtSIoAZlbnceBfenuC86ieszCc_1-6gkllRjOL_SE54Jbw3vETLao" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
🔥
🐐
برخی از گل‌های کاشته تماشایی لیونل‌مسی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/103247" target="_blank">📅 14:03 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103245">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DMUsRe6Ic5A_7YdWA5ukDllkeHokK2qZMrWcmvv-KjuncbJvQsxFvJT3XFeuxoOZ7S0lxvpkPQDRmx4K_UqDFplZPLb3fbU4-hMLrSUP69_axvnFhjRmpL_wohMkbtJ7VqgiYT7jJ0vSBifN7Kxof97_cmUzEAZFWBgWXIymo7YPPKjOY7o6XyStQoZ3XrRPefgxHJU9uDmM8v8ESMR9vS_HIVq65OV9Fi-3ZUgrv04s_6RbwjDC7JzkSNdXNqXmjNyPEtFebdYiSfDvMrWGL4MhX0RbgyMVWEZcR8GD-T-pUjDZ8lxlTNA_Zp1j3xD8kHUWRiL1XVXILP5qz9pExg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AkoK-Y6cWbpHwDwtCAnw5lkcvvxpzksRhtfiVoJl5h1obAFkRU55pm6KP0wgGcutswl5EWM791g-CtaXru2U-q3sov3blAAnmsFTrVOQbq5uokf-kDu2At-LZU-jQrd9dTwfesGL3LC-rb97OekonavzarFAkztNlgaDlGnfr4ld-ZTVjOjr0XJT5GLSIIA4_aSDY56fc9z2PIhaKyWIXtdO0uIzwLNI-6c4ZcmC8wGn5Q6ZV8CajLga_w5o_SGCEkvcfLrtm2E2Q6w4Yo9_ndhbTI7YYyP7SQdnhGmhKkbVDElDBjMQndqQ0qSirw9Ee7XbT8JxM-hihu7kDCQ-4w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👀
⚪️
تمرینات امروز رئال مادرید.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/103245" target="_blank">📅 13:58 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103244">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e730d0e84.mp4?token=KRhk3QuRth3dhVTrDrinJ06y34GAyNL3HqAXXDPXrTMZZw2Why7cVmDTp7CQjgLzw2PJ5za9x7AdIVlnZRgvk9ENH9Op37muUCwWaD9xK_Gb7py60NfPIw1JUrW5aeL-Oay4f2ooErXfI5w-2Nl-msoxh9J3nZvP132lBa3evYZkPQcMjED63-yga7l9uuzAQJwjMx3lhhT4nBDeq7-ASZ49S53Gnz6sdBbEa6YQOGP5lflJAbFJNX4Xgj3LhKHLSiDGpjFr9zBCkOg0Dsw3VRZ2mi8j1yad-dqwjRmuwzgK3YhYYGN81qS-ELouTg2hcs1yrS9hAUDolxAXrcRdrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e730d0e84.mp4?token=KRhk3QuRth3dhVTrDrinJ06y34GAyNL3HqAXXDPXrTMZZw2Why7cVmDTp7CQjgLzw2PJ5za9x7AdIVlnZRgvk9ENH9Op37muUCwWaD9xK_Gb7py60NfPIw1JUrW5aeL-Oay4f2ooErXfI5w-2Nl-msoxh9J3nZvP132lBa3evYZkPQcMjED63-yga7l9uuzAQJwjMx3lhhT4nBDeq7-ASZ49S53Gnz6sdBbEa6YQOGP5lflJAbFJNX4Xgj3LhKHLSiDGpjFr9zBCkOg0Dsw3VRZ2mi8j1yad-dqwjRmuwzgK3YhYYGN81qS-ELouTg2hcs1yrS9hAUDolxAXrcRdrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤯
👀
با موسیالا هر غیرممکنی به راحتی ممکن میشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/103244" target="_blank">📅 13:35 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103243">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f008e3e11.mp4?token=k9AHxA4EiwqeIaN0q1kUbnpSNI1FkGeiXMKytEpzWxQUu2rnVbimKqbyKhpKw33FQ6bdErreJ3sUjKZSWfDW5EUw2Xonxk0oiC8XYkGumWAWsQjudF2JALxRsI1lHRkkTKVG39L8nisNSHGlR2G5VyikpZKC05oO6j-j-WNZv0uvPbdT6r8euePBpREKD4Nlh8GTvg8S2ca5WF8Q7c3AtssLb_74nkvyuiNavqdGePus0UWU6l-8WzOSD2sgU2cMdwQBxtocfWQhJS3dINqp-WOBbRFY0ulLJJ2cVEeaO4fqMy3OXLERlRl7LAZ42dc3ToavTp0RjV3TSy9tSVn9iQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f008e3e11.mp4?token=k9AHxA4EiwqeIaN0q1kUbnpSNI1FkGeiXMKytEpzWxQUu2rnVbimKqbyKhpKw33FQ6bdErreJ3sUjKZSWfDW5EUw2Xonxk0oiC8XYkGumWAWsQjudF2JALxRsI1lHRkkTKVG39L8nisNSHGlR2G5VyikpZKC05oO6j-j-WNZv0uvPbdT6r8euePBpREKD4Nlh8GTvg8S2ca5WF8Q7c3AtssLb_74nkvyuiNavqdGePus0UWU6l-8WzOSD2sgU2cMdwQBxtocfWQhJS3dINqp-WOBbRFY0ulLJJ2cVEeaO4fqMy3OXLERlRl7LAZ42dc3ToavTp0RjV3TSy9tSVn9iQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🤯
وقتی گواردیولا به جای بازی پاریس-بایرن، دسته سوم انگلیس رو نگاه کرد
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/103243" target="_blank">📅 13:10 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103242">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bfa14f9fec.mp4?token=VOWbcLBpUBW3wfD-3uFPapkO3g2qAWr1N248pfjnAzqRnuWRToNxWLLOmAXkYqPL0ILRaeEfeVkUHp-dTOEXUgZthIZ92M2sFGkbxu3ZUincPg6V9RVSp7ZNgX_2oQohh5TVVJY1cwxndTc0BtUW5DCbLJ1fc1ZWjIAXRQlMOXnvkNZ5gWkiAG0-InvltQz_hz-XZpAUdihCzpXOeuHzUch85euMs5yGKTqiCOlLRp3mdEDoMyB_MP4b8X5NB4lC6DS2f8ZHvjFculyWq1tc3okT_ahQj_KsBDHH7uhDOQSdd615NdtTLIekHG5F7bkUqnDaM6KCqNGrfpT0df_TClFr-WYBGIenV73DIrrZZNq8tRvHcFPpUOUxYjpf7RUxBTNKIEOm8m8TvHWTiB5KsnrWqzgMud17rRZHTrl1wRnI7jk8iiYkSVA3TVScG9xcJJ5o-dU576yesM6MTamrJ-S0yRqcP3o7q0zQbLh6WWgnp3KLwjID5N2BYeZd8hutPd-q3AiqvUYguTT04BMHwL7wiSrrvvSW0RnQ35dsE1Ogh9brYvb-HchXPR50jviaeuS8BhAjrn9ioKF2fHcU8qc4FguZdrq4kyCW_QaNJxgFGAancEUZf5m52Sm-7-JsVcW7wUNt-XS4L-sGUN3lVXgt8zwmKacJ3IpYYd20Jwk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bfa14f9fec.mp4?token=VOWbcLBpUBW3wfD-3uFPapkO3g2qAWr1N248pfjnAzqRnuWRToNxWLLOmAXkYqPL0ILRaeEfeVkUHp-dTOEXUgZthIZ92M2sFGkbxu3ZUincPg6V9RVSp7ZNgX_2oQohh5TVVJY1cwxndTc0BtUW5DCbLJ1fc1ZWjIAXRQlMOXnvkNZ5gWkiAG0-InvltQz_hz-XZpAUdihCzpXOeuHzUch85euMs5yGKTqiCOlLRp3mdEDoMyB_MP4b8X5NB4lC6DS2f8ZHvjFculyWq1tc3okT_ahQj_KsBDHH7uhDOQSdd615NdtTLIekHG5F7bkUqnDaM6KCqNGrfpT0df_TClFr-WYBGIenV73DIrrZZNq8tRvHcFPpUOUxYjpf7RUxBTNKIEOm8m8TvHWTiB5KsnrWqzgMud17rRZHTrl1wRnI7jk8iiYkSVA3TVScG9xcJJ5o-dU576yesM6MTamrJ-S0yRqcP3o7q0zQbLh6WWgnp3KLwjID5N2BYeZd8hutPd-q3AiqvUYguTT04BMHwL7wiSrrvvSW0RnQ35dsE1Ogh9brYvb-HchXPR50jviaeuS8BhAjrn9ioKF2fHcU8qc4FguZdrq4kyCW_QaNJxgFGAancEUZf5m52Sm-7-JsVcW7wUNt-XS4L-sGUN3lVXgt8zwmKacJ3IpYYd20Jwk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤯
برخی از سریع ترین گل های تاریخ فوتبال
⚽
🙌🏻
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/103242" target="_blank">📅 12:45 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103239">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ullyv4QXWUyfFa3N2kI0QHz5bqEXDc5yn-hNNplb_Xg2X1Q92gGY8NU0QMkyoNoaahj2wQEbgMvbjzvr_g-w3MlScGreHffFcwYEwkG4dgoR-ovElpym1j3X2wkwk761FWeyBCCMvu-ivrmjX08Sdy2kI3afKKJI-pIBkm15Zk97vq_M6yx7I0kCjQYoYhhLXWCi8RQZcjPxlvNX5IftYA67eX8QofZ7CYYAai170rI_vjyzoDGm-cPnzJo_cv5_KuZmB4DvWqVzqVBDjEuvpD_Hz4sreRd3j_9jXBVpaIw42IQQdBCiG9WBil1zLqmPZezCf-PiBqCTrQAksYGu6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/THhX7w6C0IjrubHycIgtdJYZ7q788K5-FKVV4NIrWxdRaPT0zLKtm9nMDqftareYjXpB7wRtFNdNF9AL99lFhiPoa2dFY1WlXkUjWfPACUSCRcocyk70GWQaG-D14xQ4rSAxJ0bKtqWuNq_s9D9B1PnG9GyglPxfZtkSu0NPDFUk3ppAIWXrDXfgwk2RNUKsYHq9XJvp266rp-EVCbQnli3f1bAPeklfNWfT3gOwC3ceQIYO8j1IIClNnMH7KqcFq7xpxSQNfZ3tQ1BehHoCmy1b7FXfsuJZia_FotDBP8mPwrTNCrUgQLHrEkNP453yQ_mEsJcjKCr5R6gOqrU3hA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WAZk6WEXLpVMlO6vb-FRP-kPmNkm6HW16GDFOMybvRtu8NXXyUKhKpf33mdzR56KvABg_7EWL0z4USp2y7aMixxRpm7fOOLyiEzwnf1sfUtN5edwzEwxbTLgbtNoea1aToGS-olQnv-6CRMawtjXgL6HZ2QrhKUqyEL6k9IEVK7aOybOHtZ-b-WTPn2fMBl2O_zOhlJ3emGZrFFRAWwq1dzJ64GgwvuDv_zwhQHFP4AWKTRk3RZT9s5Bt6zIo5EutIHwTEPL7wKa2vl9y3HIwFkNjLs6M9rSxoyu7HjWe6oukGbsPOJJCuA2QHe9SAKitA1yH2hszzgwgIWM-orXMA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">امباپه ، کوناته و کوکوریا بعد از پشت سر گذاشتن تعطیلات تو تست پزشکی رئال شرکت کردن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/103239" target="_blank">📅 12:29 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103238">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f4861e800.mp4?token=M7bIZFWV6Z6zSkBEWjQkzlTrl4M3K5s-d9Hm6NFw14-rH2GaWNgqvtjzenEWj4U75ra2qlCCjV-liAToDRCtTuWqOf2YBd4UHAXTt5bEMwMkjPH80wOZxAPvKanHCpfwuWFrdOrrUSic0MNNpfaUeZQbOSeYTkuFnzc3eC8BeVSLpJIpsmVUt0oOH5cIa60mjiO9KIpolsNjOWAwmrhqnW6XS8PLVY66aA-nMS-gywj690Jl4lbpzr2U8Y3PpTQXG9iWvuLuoEK19mA6gsS-HoxQaQD_FQKJa-EmZhqawOcP4vtjpW4YNLwn-h53oyKoPKMOlnebx6tUtoAxeKB-Uw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f4861e800.mp4?token=M7bIZFWV6Z6zSkBEWjQkzlTrl4M3K5s-d9Hm6NFw14-rH2GaWNgqvtjzenEWj4U75ra2qlCCjV-liAToDRCtTuWqOf2YBd4UHAXTt5bEMwMkjPH80wOZxAPvKanHCpfwuWFrdOrrUSic0MNNpfaUeZQbOSeYTkuFnzc3eC8BeVSLpJIpsmVUt0oOH5cIa60mjiO9KIpolsNjOWAwmrhqnW6XS8PLVY66aA-nMS-gywj690Jl4lbpzr2U8Y3PpTQXG9iWvuLuoEK19mA6gsS-HoxQaQD_FQKJa-EmZhqawOcP4vtjpW4YNLwn-h53oyKoPKMOlnebx6tUtoAxeKB-Uw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🙂
علی‌فتح‌الله‌زاده: مسی بهم گفته منیرالحدادی بهترین بازیکنی است که با او همبازی بوده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/103238" target="_blank">📅 12:20 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103237">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ccEVuyVkBw2sqUZRLUOTifU7EAlLE6CWmALI07_nKwRRvxyIIG-GACsSxbY6UCNP5cQSq_TfEvT9YqtFJ4tBWLWRRRnUGYGX0L5RiMcCggW3bPQo_tT6Jm424j0khk6yVWdw4JeDIL_AE99AaLhFvWqoyeu4zwEs-gQnn0V930W0ATYenViI009G3mtrwUikWeQmWSGmSs4zdiuZwOkFGU5zha2whNBLPQgxG1cusTK399VE5cEdpNNAK1fDFbqJF48IjbCwvF_lmnwBycoJN4CBTmg5ZoTUtJi18oIH9Q8Jwd1TBBz0jhaUi6Rq04c85yY1vdL2BmNgcnnyTITWow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
❌
بن جیکوبز | یوفا، کونکاکاف و ای‌اف‌سی نامه‌ای مشترک به فیفا ارسال کردن و خواستار یک بازبینی مستقل دربارهٔ FIFA Forward Enterprise یا همون برنامه اینفانتینو برای فروش سهام جام جهانی شدن.
نامه که توسط چفرین، شیخ سلمان و مونتاگلیانی امضا شده تاکید میکنه که اعتماد به‌واسطهٔ فریب از بین رفته.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/103237" target="_blank">📅 11:59 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103236">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/82a19a1124.mp4?token=H7y7dmJuKNpMwTxe3PqJy22BqL5RIVOwsExTBA0H0N4N3HRxecm1czrmJ2ss02stxLKWK1BEn83hkitIa_nx2tC_qrYLDun5wDJ0sx2LLf6mW3siK7MKG_uSxroGj53wTyMIMeshRhDfcLrU-H2n1dNZ1NXtCmuNB94sp-KKSPNggic8EDKDSx0BwIHNBjR5Sao71YgAnBqbQfzXmWmQnt5elkcxaX-CTVHBSK0UvfMAxAVoGHOYSP9ORdb_aszPMwW22UJ6U32kvAdvm79DjNWkhSM3OwW-E3E4RgxvttRiOPcbH-knr1pBb-bOcmnbdtbO7g1FxGUzAYnTxrAI_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/82a19a1124.mp4?token=H7y7dmJuKNpMwTxe3PqJy22BqL5RIVOwsExTBA0H0N4N3HRxecm1czrmJ2ss02stxLKWK1BEn83hkitIa_nx2tC_qrYLDun5wDJ0sx2LLf6mW3siK7MKG_uSxroGj53wTyMIMeshRhDfcLrU-H2n1dNZ1NXtCmuNB94sp-KKSPNggic8EDKDSx0BwIHNBjR5Sao71YgAnBqbQfzXmWmQnt5elkcxaX-CTVHBSK0UvfMAxAVoGHOYSP9ORdb_aszPMwW22UJ6U32kvAdvm79DjNWkhSM3OwW-E3E4RgxvttRiOPcbH-knr1pBb-bOcmnbdtbO7g1FxGUzAYnTxrAI_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🤡
محبوبیت‌ دیدنی لئاندرو پاردس در آرژانتین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/103236" target="_blank">📅 11:55 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103235">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e57eb2f58.mp4?token=Q4Dgs0uH7P-4q6tYyaH0zzyBMJH9gWl3k5x4oy2zROMrQufRxB8EHIsQNNkk2deyXla1PfDsF8zIbjGihlwIR6vTPWCs_fc3lwga9-6rUKYXjsWbZ0mpIUWTwfPoRrkTyFHKtqipQzWrduoLt-rZ9OwVCnOWYsFmMD-jti_LpKPm3C-13ImY-ad8TeXao61j_CaWj9DJMWIsUBAkbAZNrjkqm6TchZn-C6Zafu1AI1IXgyvcZUhs9_QymiFOvFj992pNE5uR2Z9AGr_iFRGEzcJuegONzGGokOT-3zEmBGFzTZHBQAS_4U5UVUHcAwqeedcoMZqpKIP4guXCWqy2uQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e57eb2f58.mp4?token=Q4Dgs0uH7P-4q6tYyaH0zzyBMJH9gWl3k5x4oy2zROMrQufRxB8EHIsQNNkk2deyXla1PfDsF8zIbjGihlwIR6vTPWCs_fc3lwga9-6rUKYXjsWbZ0mpIUWTwfPoRrkTyFHKtqipQzWrduoLt-rZ9OwVCnOWYsFmMD-jti_LpKPm3C-13ImY-ad8TeXao61j_CaWj9DJMWIsUBAkbAZNrjkqm6TchZn-C6Zafu1AI1IXgyvcZUhs9_QymiFOvFj992pNE5uR2Z9AGr_iFRGEzcJuegONzGGokOT-3zEmBGFzTZHBQAS_4U5UVUHcAwqeedcoMZqpKIP4guXCWqy2uQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🔵
🔴
🎙
داریوش: شجاعیان: شفر قبل دربی گفت اگر پنالتی شد فرشید بزند. رحمتی به منشا گفت بیرانوند تو را می‌شناسد و نذاشت پنالتی بزند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/103235" target="_blank">📅 11:31 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103234">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e7df2b7b9.mp4?token=lxJOR1wCjuypSQDzeYzWlQD4BEhpIbInpwx4vCPoNM_ZDjghl0VjORLyuAu2DNX-29EBIswNp9030xf9UxqEIICgNo6wP8YbfxVOjm73GuCMB6a6RRUz2OJHV9yiwgTWbWRzqbFWKFvp_I0JPRntNRoraTFf71w8XK2hZUxqnSt-dbHgzKF1ztRGIfuYVGrdc4oFTo5GP2uSEjkZUiTAgDM8o4x6hJ9dZbLJ2_CDngl-w59u5Yi2L2Kv0NoeUAS65HPcU-qSomRVgTmrtJd4mlSE8q3v31hiIEv_PFKXAnaEq-rctwRbo2jsn_HxTUWvCLPd_ekkulLwIdUpoEClYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e7df2b7b9.mp4?token=lxJOR1wCjuypSQDzeYzWlQD4BEhpIbInpwx4vCPoNM_ZDjghl0VjORLyuAu2DNX-29EBIswNp9030xf9UxqEIICgNo6wP8YbfxVOjm73GuCMB6a6RRUz2OJHV9yiwgTWbWRzqbFWKFvp_I0JPRntNRoraTFf71w8XK2hZUxqnSt-dbHgzKF1ztRGIfuYVGrdc4oFTo5GP2uSEjkZUiTAgDM8o4x6hJ9dZbLJ2_CDngl-w59u5Yi2L2Kv0NoeUAS65HPcU-qSomRVgTmrtJd4mlSE8q3v31hiIEv_PFKXAnaEq-rctwRbo2jsn_HxTUWvCLPd_ekkulLwIdUpoEClYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دومین‌بازی ضعیف دومفریس در‌ رئال‌مادرید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/103234" target="_blank">📅 11:05 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103233">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f7ItAT4X3scIY0vtTL5143FlnKR3muQrco1-1csXic5lbXbmERU9crH0x2H88538DeTHWbJa5JrObu65cCGePHqkanjK03F3T0Yg4vHw1Q3HK_bHlYBBzsa9uc4eCj9iBZ4ui6xc_Susaj72lOcECuQ5eD-bcuC657aaAW7GtJoomHlSGtqv9PbwhmNHxhH-JUk4plenCfIS_g-eg40RCZ6f6CLnRot7iPcWD1R9GAknEwbRNJWKWXjbh0qjgvu75OAQT5MaaB78xs-ftxijE_dJ8ELJwDta1maTDG0OqHQKvJLPmNsq3YaP0Q6_PDMWVaslv32H3bk8JR91VUkI5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
5 سال پیش در چنین روزی؛ لیونل مسی اسطوره فوتبال در انتقالی پشم ریزون به PSG پیوست..
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/103233" target="_blank">📅 11:00 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103232">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WuSQIds7s9NDbJQ9bcUpyRikGuHyGd7CsiwD_SFbF2zUcitDLXj9pXW7EFnvUu9nXml3bxddmRMygU2DR0pSPOvhZACjGkS4ISxEIzGroG6vzi4NDQZ82ZCe52RfeXnFDO1ewM7viOrY3DVfN-60_Ovxreo6zBjlewc6Ujy2J6NHMr08Cbnqg74Ig1i7RYNtiIy7QvgAylVNLBlJrErN4EHaEoIg6enmPNic7TL0v8avS11x5IP19MBgiz14G8o0hKjg5LBdJ7wk6LQ4eIzHv97tGkuDZK1rxDZUxIzDFdrdXE_XpeCfXWI1IhUJ0_CKMvMjsbXswy3WgU8mDAuKmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
😳
😳
جرارد رومرو خبرنگار بارسایی امروز کسخل شده سر صبح داره دوربین‌های سطح شهر مادرید رو بررسی میکنه تا ببینه آلوارز کی رد میشه و کجا قراره بره
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/103232" target="_blank">📅 10:54 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103231">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QtY0n_BXsEm3MvxevMgJ3mp8-suYPSXzUGTpyfCds3aVZPb0IPSjw4KCScUUN5whgibriOiTI9qbWNBa8g870IuaQvWBpG0M2o0TuBLw08y-X9IfIak5YX5YyMtJlRBO8TVYMWhJzhXr2jLnQ4PyPHqry6fGhijEBl4bTM9gRARC-sAxCO9zqpP5BkhnN-p3zGZ5l8Gq9uzVXXl049xz1SdPsPimLZwQqZUKXbIDGpd0rXVQKd-Ub_CbpCXvA32HZDzbzt4NAA2a8zIPc1syFMAeG1_p4qKympiMxZg7OKvHQuH-yJyPBnAWsIDl9I9IUZQk3ux1ZFVQ8h5cOwziVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#فوووووری
از رومانو: ایوب‌بوعدی ستاره تیم‌ملی مراکش با منچسترسیتی به توافق شخصی رسیده و مذاکرات با باشگاه لیل‌ در جریانه. بوعدی جانشین رودری میشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/103231" target="_blank">📅 10:45 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103230">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a8c797d10.mp4?token=iBa6U1S9oWFnMhW3r5iCH8c32MlUcM1Kujj2kIR-hEv4lNYBPtwUj4Rcwo20wM_pUP0hQ7mPXwYGSk9axp7t3bdeza5Ub4n9B1KwX85tz4F_WPl5ShAWSM1MLjsZiRGm1ofe0NZt5pTx4JcgflK6MClvBjoS-IKhqQfo1jSwxv2IKgD49pHuuFitgKnwYXS93UnZ5feoapqiCQkCZCxXkgqu3KZiBLSxKwgyIpKnAImas9lfjQF2UXRKE-QSR3DD7bl3KAWVZ23JWnrJd3ARyB62Afsl_Fy0wLYVDrDHTnIP4v6EIeAi_N-ME3domRJFAYpcnvFRuG09a4_JSS4yebs5W9Q04WcyrsC9_3m9oyzzkc7bStLvJQaj9n07BYEekgIjsESSI4kXw00tahaf5sh1p_24rxnzvdNNAkqb0A-QWlMz-Lnf1qCeV1b_roR8rvbuihmiX3X9CCoKM1s_jdFdQN2uTOvzjNpF7WfuIHSAoXuoe2CaBmosBhNQAPXDrMXiPv8fbJx2_Cc_yaMyZcRLV0Oq1ugh-LRrF6orHnF8EpaTHYmtiwhcX71xtSsihZqC6Dv57iqiYtw-vU1cimDI1cEQhoOjqNFLgwIn1Bv4FVabtdxmgPcrgxcC1xRafyC8qjrORsyTGtu2TudAvDPwgywtXafcMcoycZbLPL0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a8c797d10.mp4?token=iBa6U1S9oWFnMhW3r5iCH8c32MlUcM1Kujj2kIR-hEv4lNYBPtwUj4Rcwo20wM_pUP0hQ7mPXwYGSk9axp7t3bdeza5Ub4n9B1KwX85tz4F_WPl5ShAWSM1MLjsZiRGm1ofe0NZt5pTx4JcgflK6MClvBjoS-IKhqQfo1jSwxv2IKgD49pHuuFitgKnwYXS93UnZ5feoapqiCQkCZCxXkgqu3KZiBLSxKwgyIpKnAImas9lfjQF2UXRKE-QSR3DD7bl3KAWVZ23JWnrJd3ARyB62Afsl_Fy0wLYVDrDHTnIP4v6EIeAi_N-ME3domRJFAYpcnvFRuG09a4_JSS4yebs5W9Q04WcyrsC9_3m9oyzzkc7bStLvJQaj9n07BYEekgIjsESSI4kXw00tahaf5sh1p_24rxnzvdNNAkqb0A-QWlMz-Lnf1qCeV1b_roR8rvbuihmiX3X9CCoKM1s_jdFdQN2uTOvzjNpF7WfuIHSAoXuoe2CaBmosBhNQAPXDrMXiPv8fbJx2_Cc_yaMyZcRLV0Oq1ugh-LRrF6orHnF8EpaTHYmtiwhcX71xtSsihZqC6Dv57iqiYtw-vU1cimDI1cEQhoOjqNFLgwIn1Bv4FVabtdxmgPcrgxcC1xRafyC8qjrORsyTGtu2TudAvDPwgywtXafcMcoycZbLPL0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❗️
🏟️
آخرین وضعیت استادیوم آزادی تهران
✅
قرار است به‌جای دروازه‌هایی که به‌ صورت ثابت در دل چمن نصب می‌شدند، از تیر دروازه‌های سوکتی استفاده شود تا در مواقع لازم ؛ امکان نصب، تعویض سریع یا جمع‌آوری آن‌ها فراهم باشد. عمق محل نصب سوکت‌ها، بسته به مدل ، معمولاً حدود ۴۰ تا ۵۰ سانتی‌متر است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/103230" target="_blank">📅 10:37 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103229">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P3E7Fx3MB35Ubim0LOVN2qzQ657VJORaiq2NL28S2mSZcB6xO_2-2eMTm33teP7iCcFtMwud5Qk_TMhRutXuU0ss0k60s_GrYFxEFrkdzhPcWPY7mQjjpV9tiytgySthTAUXFEA770FICvmihWhZVlaUhVDxLWH-z33214o-Giz20-LOcjSjCtxbYu79eWXkzstj-UidYaGiCjMPZQEpXn2DLElEhZiH2vTdy_ZfJ0K9rBzzBlaxiGRDzGbnwcp5fDtgInxEs3yWNd1zsyjpTGidhdgkuSyUS6CVChIIIBBI8AaT2UTaZRwix_APCneIM8gi33_2O-g3Uu5pVB7MFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🔻
آرسنال برای فروش زوبیمندی خواستار دریافت رقم ۹۰ میلیون یورو شده است!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/103229" target="_blank">📅 10:15 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103228">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d8748509dd.mp4?token=ur4TLzVBpPFRYtL8qwFFeFTR3bnEfhpj_Pn_YtTkwZ5U2n1yzcDvGLtzEtfhs0ltuutCUdUqIZeMIzzvxpHJp9XuMKxKeK1oU7ajYep49_C2CdNJ2tIkCj3UaSIEZ5kvuu4YADRplhB5gTZOANUbWvLH7R0a5BSX00Xc8I79cXo4EE4-Nx6JewL0Bkk7gpSrBKTFQNJ3lmoMeURzrPzXSib_aIfDw9o3IPcvgtwogKPIoPLqsLcABO_s90zPlj2cSl87e5KF-Rs4z9qVqFoHqAzsz2aJ3VmbXT3TM2LGZmEiznpX-aNa6MZvL90520gLGjwB72s_tV-cWZlNxtQ5mi31WFq9F30xv9LFBixz-1IyjjNQ3LcWKXBds4l1VLO3LEXVOiNLEquYZAZz8SvNMSE_Hf8WjIzgEKHEczWdkMcDYaSMLZ5uSeJxDnBvhn4CkBqTFVk1QuyEHMr3Duh7v1598fSsCbayVljiEZJL7R9L963YELEo26VxBd-hIzWfIw_POs8Ed7Q2gSE8GrH8-txTh3Ln9j8UqsrmOJomQynkWjxgKQ_bnegbVuvHLmXE_yttNsWzUiGe_VeGDeVno9w-AqDCrHJfQwPi8CdtxEeelZkCfv-6aeQlZ3o5KjKqtqR5gzdi4nCthK26SSiVy2twRqL76TDYcb2N2WExSYk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d8748509dd.mp4?token=ur4TLzVBpPFRYtL8qwFFeFTR3bnEfhpj_Pn_YtTkwZ5U2n1yzcDvGLtzEtfhs0ltuutCUdUqIZeMIzzvxpHJp9XuMKxKeK1oU7ajYep49_C2CdNJ2tIkCj3UaSIEZ5kvuu4YADRplhB5gTZOANUbWvLH7R0a5BSX00Xc8I79cXo4EE4-Nx6JewL0Bkk7gpSrBKTFQNJ3lmoMeURzrPzXSib_aIfDw9o3IPcvgtwogKPIoPLqsLcABO_s90zPlj2cSl87e5KF-Rs4z9qVqFoHqAzsz2aJ3VmbXT3TM2LGZmEiznpX-aNa6MZvL90520gLGjwB72s_tV-cWZlNxtQ5mi31WFq9F30xv9LFBixz-1IyjjNQ3LcWKXBds4l1VLO3LEXVOiNLEquYZAZz8SvNMSE_Hf8WjIzgEKHEczWdkMcDYaSMLZ5uSeJxDnBvhn4CkBqTFVk1QuyEHMr3Duh7v1598fSsCbayVljiEZJL7R9L963YELEo26VxBd-hIzWfIw_POs8Ed7Q2gSE8GrH8-txTh3Ln9j8UqsrmOJomQynkWjxgKQ_bnegbVuvHLmXE_yttNsWzUiGe_VeGDeVno9w-AqDCrHJfQwPi8CdtxEeelZkCfv-6aeQlZ3o5KjKqtqR5gzdi4nCthK26SSiVy2twRqL76TDYcb2N2WExSYk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚀
شلیک‌های سهمگین سوبوسلای ستاره لیورپول
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/103228" target="_blank">📅 10:08 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103227">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">app (7).apk</div>
  <div class="tg-doc-extra">53.1 MB</div>
</div>
<a href="https://t.me/Futball180TV/103227" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">⚠️
#پیشنهاد_ویژه
⚠️
🔥
حتما ویدیو‌ آموزشی بالا رو‌ببینید بازی ساده و بسیار شیرینی که راحت میشه میشه ازش کلی پول درآورد
👌🏼
دنیای سرگرمی و بازی های جذاب رو در این‌اپلیکیشن تجربه کنید
⭐</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/103227" target="_blank">📅 10:08 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103226">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/936a75dbba.mp4?token=md0gKlWCrVv-OigtD_vZy0h6e6ex0aV77VpqmCW9MAfhSlNS_jkYnM6ftl2tfoifAI_nMGImn9YDiSQMdc33JOp3V8sr4SWSwxx0T6DIJl8_TA3iFveLWPwD3YNC_HOv-FBQr0SvUw4I6YOCPutSQ-U-2_5eaZ615fE1zWYS3yqMAuRqF6txsgKDIj-_zZJgMl_priPKAlG2Hp9WAMvtYqN5MvNwnoXZe4Reo7dRE7LrobR4VSNOm0STk3yk4DLBsJhybl3v-JYJi1amfQe2m0vVNa8D5SWpIoFw036MVTCY85OTFi-AnlvK69gBFFrrFGRb74RQXwOQtsANUZR4Cw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/936a75dbba.mp4?token=md0gKlWCrVv-OigtD_vZy0h6e6ex0aV77VpqmCW9MAfhSlNS_jkYnM6ftl2tfoifAI_nMGImn9YDiSQMdc33JOp3V8sr4SWSwxx0T6DIJl8_TA3iFveLWPwD3YNC_HOv-FBQr0SvUw4I6YOCPutSQ-U-2_5eaZ615fE1zWYS3yqMAuRqF6txsgKDIj-_zZJgMl_priPKAlG2Hp9WAMvtYqN5MvNwnoXZe4Reo7dRE7LrobR4VSNOm0STk3yk4DLBsJhybl3v-JYJi1amfQe2m0vVNa8D5SWpIoFw036MVTCY85OTFi-AnlvK69gBFFrrFGRb74RQXwOQtsANUZR4Cw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🖱
به راحتی کسب درامد کن
💵
💰
🟢
ویدیو
#آموزش
بازی chicky choice رو براتون گذاشتم خیلی راحت و بدون ریسک و میتونی بازی کنی و کلی پول دربیاری
🔥
💖
حتما ویدیو رو تا انتها ببینید
💻
لینک سایت بازی:
💻
betinja.bet
💻
betinja.bet
🌐
کانال بونوس های رایگان
r19
@betinjabet</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/103226" target="_blank">📅 10:08 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103225">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iQHf_1ZHQLJLOMgkijB2M0B4VVgwPE0hbSA-A15lzVaMqZpzZ4unmfERiO_pKgmLCyMmGr42c80JFeLC327CIIjBd-I1GjDCFRWTxR9YEuJSxdcgFAJOWz8AK5eKMBuc9UeukcN3JTLSwcy5Vg1iNBl54eowWg1tDHjFGDtYQaL3jL7vBoUeG45KOIakRfmnMBnfIpYjk03b-tRDu6hko3FBvWcnrp-WPOraCTsSLWx1xdP6NzlRKmTcIU06YzLOSZDoLIGnWhjX4KkRDyfwGv6Jz4CsEhkJYz0hr9TYrrIjx3yITzXQkfPtXoY6FDurX_jbVbKXdVmTq3gBugHjJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
🇪🇸
مقایسه آمار فرنکی‌دی‌یونگ و رودری
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/103225" target="_blank">📅 09:50 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103224">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MJIHAdALsxGa0XN7yYoyXOgN4gf3482RX4drsrHk0V36suknCXaF0sHRdldegRCfeBGaRJGVHBCyU4EbnlUK352L5fA4A0FDbF-iBOzV6j-G5gz7Qstju9AxOvLWz6Em-_PjhZwsUIlcdpkrEzLlkd8DPjuq9r7WEuOgYFD_qg6EzmCPSJn1m0Qh1slx9ogeVTxzguVLYDjxRxDI_pk_kb4LGM2NMkdezw9ebh4lVikRiDXuxrYtWzB4bZ4zIPSv0m1W0c8R4XXWgBEWlfRRJQPG-ERYh5GAnCrVLt_sxdgJ8XDH4oyimNczfxS0CM0C6Kr5rO3D6HRtJ5EDW_aEPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خطوط هجومی فصل‌آینده الکلاسیکو
🥶
🥶
🥶
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/103224" target="_blank">📅 09:25 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103223">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👀
🔥
برخی از گل‌های چیپ تاریخی فوتبال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/103223" target="_blank">📅 09:01 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103222">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oCnI3bCl42jCUqZ6d4u9LHxbnC5ST5oIFrpgIMNxhV-81JuSt-NDdc5UpCI40odFgJ3qO0niikFVOylqCdUA6Rv0lGVymbFwF3rR2TlSx8BF6gw7DBek3tqvRsvu8bC6N2E2wgXwOH1jQ7O0FLmFm-Nh_khuX9hWXCXQNwy-kGBX9VSC66EMtFnFes7Vi2acKY0utS3mBY7LlNgcmugMQFsKvxCRMLN-bo431X-J59KVb9kwg1TLuVDzuvjRz3Oj8ikJUuf_tDz8Qgqt3JfvW-2pD8qa3S2rCXToQIn2PqSzKDVYHh1jR5IBgbi78Hj6fVNypMt4sZYKHUEq4AyIOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
🇩🇪
نشریه‌تایمز انگلیس: هری‌کین بزودی قرارداد خود را با بایرن‌مونیخ تا ۲۰۲۹ تمدید میکند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/103222" target="_blank">📅 08:38 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103221">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PnImtYjvBxX_ROz1eD6ochORCpJ7tbpb7u_c9QHx1l_67OSczylNI3PaXGyISrNjpJJOHQR3K4onJ2yXdoX5mTTPMmdlIuOzvTykMWHU5bZtPN5mClyW6k8S3ACec-8uAytPHcViqmKhEBxwnHnfdanLiUr5fNyF0XtcSbSCtLRFO9OzD7RQunFxh3_vY7N8wfqVULc9NgVfUa5vNv3HOi16f_llgSCL8f33ViBPv5DkrxKVn3B4remv8PmffgC97-iVyZ91vyadKmF9O1bbCv40InpWhDjfFrQMm5qPLYYQdJcpaajkSQIImkt2K8xn6ASxtyldijBcuO0aFRcKlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🗞
🇪🇸
#فوووووری
از رومانو: اندریک خواهان موندن در رئال‌مادرید شده. از طرفی استون‌ویلا و رم برای جذب این بازیکن اقدام کردن و مشخص نیست که رئال راضی به قرض دادن مجدد این بازیکن میشه یا نه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/Futball180TV/103221" target="_blank">📅 01:36 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103220">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IbbML7wfuHe9rfIU4cylLptvNqkGWfovSaMD0lxv47ub7YWUD_qTKfvuEagt6BVZDwJ4lKhgOBUrusAAOymVfqTJiFcsaL2WFFxYfQWBhz5FyD-uf2KAwX9QYbZI-SX4CwktR4TuQzous_OODjJr1wM793GKZltQDhJS4qy3CwPMCGTOhUKwXTWkkTl_vPQ1dsa42JwWr7uPPlLb9zYuiBYqFq5nrJONAMHV0AGDqm3ReF9wujYzioR5_aMnblb4dS0FYxO1tDXsbETcggtMJbWqfkdPhXobcygUCWs0IdD1oOt_OMF7otZU3GxTwE8QARgIv4O-3yAUu0cEGWpPqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇪🇸
#فوووووری
از جرارد رومرو: کونده مدافع تیم‌ملی فرانسه و بارسلونا از یک تیم در لیگ‌برتر انگلیس پیشنهاد خوبی دریافت کرده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/Futball180TV/103220" target="_blank">📅 01:34 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103219">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🚨
🚨
👀
⚠️
حمله تُند و بی سابقه محمود فکری به عادل فردوسی پور: زورت برسه همه رو لِه می کنی! نرسه هم دستشون رو می بوسی!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/Futball180TV/103219" target="_blank">📅 01:12 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103218">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🚨
🎙
‼️
📰
علیرضا دبیر: شبکه به‌دردنخور، آدم‌کش، جاسوس و کثافتِ اینترنشنال! من محکم تا تهش هستم؛ مسئولین هم نترسن، بزنن، بترکوننشون، به مردم بشناسونن این کثافت‌ها رو!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/Futball180TV/103218" target="_blank">📅 00:54 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103217">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RViCptTfny9sNAeiyun0ZvfO9B7CvUYJzjbBUutX0n8i3U8AyRuofNyMIvC-THOGQxa3DoV_J8S-bONfzlLSYXZ65_hbKenoZH8esp3pkWGwLu92xu0cGHBXZKSOoilXwUOk7-AUZHKodkx4hVauAA4s656Jm8ViGyoFKKiIkQx7JceWGjD6EACY28T-lgy9musue4LCk_LhkzBAp5eNqJ5IoWwI_M1vnQRQACiJGjCDPsWTqnBdUaGqLJIoRoVlSPaX_b0EnP5SBpt97T4TZw7IpLsM964u3TXfG9JMl2L8zAhutsqkrckLdaCAwQeqiK7B1ftlIlmd20kOr9UlDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
🇮🇹
برنامه فصل‌آینده مسابقات کوپا ایتالیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/Futball180TV/103217" target="_blank">📅 00:54 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103213">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🚨
🚨
⭕️
🇮🇷
سپاه پاسداران یک کشتی در تنگه هرمز را با موشک هدف قرار داد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/Futball180TV/103213" target="_blank">📅 00:42 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103212">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/sksmXgffHX9dgELCic9VwqDa5LZ-SPp9pB4xf6t6Xe2b41hG_t1T0AqnF_n2CS4oMBsx7yIGh9mOSCTUg1SfsrRPouT9IgEAoJ0Us2cj253f93M12AM8-fR8o2oM1KYrBpIjgIcQt02GLKD5GeOEjsdP8O3cXrWqNd_cDKv03l3LJu7IxIm_7ofX2KN2MBweZo01fDvlQZ8_Zs4QhyoHraPckYbLq51iIiu0GpevEC0S5cz0v3XfzTckmUiIJAfehX2Km874VoTQw7nFS2RiJBFHtE6ochfDaczVM3MbhZb8UxTCcDeSKhFY5naJiCzS-4eH6YkJE9_gF_m4_nrvag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#فوووووری
از گستون‌ایدول: کریستین رومرو مدافع آرژانتین به اتلتیکومادرید پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/Futball180TV/103212" target="_blank">📅 00:06 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103211">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
#فوووووری
گستون‌ایدول:
🔻
بارسلونا به خولیان قول داده بعد از صحبت او با مدیران تمام تلاششو می‌کنه و پیشنهاد مالی چشمگیری به اتلتیکو میدن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/Futball180TV/103211" target="_blank">📅 00:05 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103210">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dMXl4vsKNp2-oQoF-ZMuB5jDuDDsTIJtAcywjrKuETqy4z9UzSSwo1FuSiS_eDu-s6XvroK9RPh0fXGXyrS2k4-USnWLQsd-413hOTtMxbG_Ss_GEVZ1p4JscmmDw9FkY8JRAyvr9qy2fuPtNq7shggfv5g-CnrIx9e5zu0yez8BBYIP2FbQ4Gc5R0m5RxCaMwyWeR5MKX55xRlqMWqlQs3Ebpfvm2VYcg4iQnIlr6aH_C-gwSkAjxnjS13fadxDB-GpwF-thBWxljzSZMHoPjr1I4YYHerC3AvvQ4tRoEFRmD9EAMhWxvbsY0Xmbri52Dbgekuxg2bIXFVjRKDY4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇹🇷
#فوووووری
و
#رسمیییییی
: داروین نونیز با عقد قراردادی به ترابوزان‌اسپور پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/Futball180TV/103210" target="_blank">📅 00:00 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103209">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🚨
🚨
🇪🇸
🇪🇸
#فوووووری از گستون‌ایدول: جولیان آلوارز قبل از جام جهانی با مالکان باشگاه اتلتیکو مادرید صحبت کرد و از آنها خواست پیشنهاد باشگاه بارسلونا را بپذیرند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/Futball180TV/103209" target="_blank">📅 23:59 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103208">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🚨
🚨
🇪🇸
🇪🇸
#فوووووری از گستون‌ایدول: جولیان آلوارز قبل از جام جهانی با مالکان باشگاه اتلتیکو مادرید صحبت کرد و از آنها خواست پیشنهاد باشگاه بارسلونا را بپذیرند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/Futball180TV/103208" target="_blank">📅 23:58 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103207">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🚨
🚨
🇪🇸
🇪🇸
#فوووووری از گستون‌ایدول: جولیان آلوارز قبل از جام جهانی با مالکان باشگاه اتلتیکو مادرید صحبت کرد و از آنها خواست پیشنهاد باشگاه بارسلونا را بپذیرند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/Futball180TV/103207" target="_blank">📅 23:57 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103206">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pRNFsP5-bBcez9BuQ1EJsuq5kduBTNzqSjjut48-kDNxOt7MHS_5Hh-plM2QqDYYAM7GoQ0jkXgNNJYI8nxRNi0X0Q6urSIItH9IoWFmEnPmGsYpRmMiKNIl96oZqcI4Pg28LBh7o_zpn7xRyYCmUKaa7Fnz2S1FThi-vpxSVNlklT2r_MDidkByGCHiHI225JsctS2WEfgBnaB5MK1O8GZzx5gsrCNtH0U8merPLwFKCFFg5rD9SmSltj1m8vjCW6wUZ2hqYegpJyZppG_Yj8g6VO4oBBKxrmWTuAdnLOfRQA_Uk_UPdlDS2o0nqNcwPSqaFgf5kEc7YPSZF-MPtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇪🇸
🇪🇸
#فوووووری
از گستون‌ایدول: جولیان آلوارز قبل از جام جهانی با مالکان باشگاه اتلتیکو مادرید صحبت کرد و از آنها خواست پیشنهاد باشگاه بارسلونا را بپذیرند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/Futball180TV/103206" target="_blank">📅 23:56 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103205">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vJlPdTxywKulLcOA4txcoPKZ9qE4iAdvYtWdVAErb22mXY4HxObmAFLJf2eUqxbXUe-2zD9iHZF83j7itqgZrZsX5DDvwX_4qvlqVv2VnApFP3CuUtfn7fajzQmT33Dff9f0HCajyukrXIcvFvO4nfKSZ-YQkw8C5hZmBiHY-PqPXUFL84wsrdf7K8d-qKLX_wCJMcHLVVVsvOsqIwmeSONoPAPdTRNRwHQ3KytcnbPVy5Fblagw5EKY-jLtOUL__P-lk7Hfof1tN_ApFj8WypAOi3gKqi5cCK5-1KsvwxN6jxIDtn0PJaRn5DxKo1rHaYTZbK0pDTPUpKV3A0AZOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
🇪🇸
باشگاه بارسلونا در اقدامی‌جالب نام رابرت لواندوفسکی رو‌ در لیست اساطیر تاریخ کاتالان‌ها قرار داد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/103205" target="_blank">📅 23:52 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103204">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S8A9h2Nm6MTdO0yazYFowdjcgqu80ManuxkoV4VeMxzwesx-xnmmbCPmyLg1SzeQtmz5FPQzHo5Gbqqgt-t3ZEMmJJkL3kyLZ8Jx_F_60AS2WdMnywhJjmXMtY4l6ngjYpsHpGjPTdyuXweHDbyv5JbmmUR2vITrnRM1OcRO6kzJdIEBD3EZhG9xfhc3nE8SXVA9TnXHcNwj_ioJjUx_ZPdTscOL0kFIIP-lEBPbKfjfmjFhxzNb_7FzN0W-ASnMHpVZKSdke_0sV2JLz3b13pcQjBsDL0D8f8xc5wmKZ36UU0kNxW4e5NlP__znnXhIEBn52KZzXBJNCmeGKtfe5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
دفاع وسطای لیورپول در فصل 2026/27:
🇳🇱
ویرجیل فن دایک — قد 195 سانتی‌متر
🇫🇷
جرمی ژاکه — قد 188 سانتی‌متر
🏴󠁧󠁢󠁥󠁮󠁧󠁿
جو گومز — قد 188 سانتی‌متر
🇮🇹
جیوانی لئونی — قد 196 سانتی‌متر
🇺🇾
رونالد آرائوخو — قد 191 سانتی‌متر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/Futball180TV/103204" target="_blank">📅 23:37 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103203">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qTHsCA09kDx_YkOj027YrNOZGYx6TiCYZh0UsLTVucbJ7byAD2Z6dynrqe1xjZZHEVmfHrHnkyVKKxPDJKdSrM_8BxZHcs6QRHv0X2b8_uLnB3WvRyqH5MlqTwUVeYzqR5MTfRMZcjFhAAsYuE-ejfY1LAojVouIJ3KguhtK7PbQ_OPwtfWlGKphMtsVqatmPalYLraNcWYubTWwdpsM-7BM9itfwmoiblc-ITcifkiHktje-MxKeZM-cmdNUO-oYd_mvG62uG6O9iR9EFuBeTOZLLvzezJdGjawVB5d8rBt2I0bsp39US160PIsKWT72Ht-mIWqiPtsazURXMor3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
‼️
پیشبینی هوش مصنوعی از جدول فصل بعد پرمیرلیگ
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/103203" target="_blank">📅 22:51 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103202">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EwtfzRIvr_iUyIUlm3fKAQMSAazOeecoeyYSp015Qb-QWQMEa1uwMuzv6D8hpObYh6mhJocPCBFI6kJVta4ERCKhgLUS4cRddJQ64oWZpo4EagWr0LqHsD24H_pmg9qj41GmDr9SDgsN8-gWrYlNsvKmGwLu-r-ojl3mfoE6bEwKZ6HVTx2PATkZBdB85tMqL8UvN2LcpHxn2aPD27ydeRd57IujgEiHpsV-jUuLN2Qpo4rix40nCWWCqGJwHZL-0LdQBf8pVXZ8Z2x0eeRoRee0KUy4_ht_SC_gO14Q58npoyoN_wblYfmPU7PmkWncjZhjq3NalbGHlaSgzITLJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
#فوووووری از موندو :
✅
🇪🇸
🏴󠁧󠁢󠁥󠁮󠁧󠁿
توافق اولیه بین بارسلونا و منچسترسیتی حاصل شده. فقط حل چند جزئیات باقی مانده؛ این انتقال بسیار نزدیک است و وارد مراحل نهایی شده.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/103202" target="_blank">📅 22:17 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103201">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c0HXg7sJK3bKH1aJfQkq3iYDAFTfvps_NIwB1cDTQzGjH3bppEzWXt9nEHFcKS2hcTBsObHimbRI5YMop9KfbxYbLCanoEDoioVHn0YYv1TwQZ4SBGV7XR_VxTTL7exRwYOy2rQH-JLApwWmiMfCs8xm11oRB188veWfPcnHFW9Vz54DZ6KcrwU6Zdsiz43Q6s6tCjBPmGGDgkLtqtf-_e3Y5yRZSkKTxmaV8ikN63nMElv01-tAZHqRPF08Xg7-vSTqSAdRoRXGQccxHzQRJ9w_mt454U2CtVrsiZzlgh9olWDk36MGxU5TmixgbCwTDcsiFrcyyOEPd0NCu9ZX6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
#فوووووری
از موندو :
✅
🇪🇸
🏴󠁧󠁢󠁥󠁮󠁧󠁿
توافق اولیه بین بارسلونا و منچسترسیتی حاصل شده. فقط حل چند جزئیات باقی مانده؛ این انتقال بسیار نزدیک است و وارد مراحل نهایی شده.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/103201" target="_blank">📅 22:14 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103200">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b666d08ac3.mp4?token=o5Z6abMmKMvb05YDONWyp1OOcdo9sTciR2Hd61yPzVPJS3zPDMXyjhk0XkL2bTulPSID8C_mbs23hIcsqiY4kkY-ItT84vUr7j3Ug_JvA2IgC-_-Cvq5oFS4l5G0uf81xuB_4oUizZDAskw_Up_340mxSW_SHpUxCmupa3Dj2ss_mBBu_gP2rfalxi2VqnJXD0GP-qzKbRzxrrakYLDH9BHv77oDG3EmYzibG1eFgnAdyYRJXEgUDSJLZ1yvoSiSHNlRJIoSKfH3Z0YlLg4HI1T8O3lkL9CwoPjlbzmFhnE0F-Dx_FukABV42YecLZXY5q4dFa6H_E16zPYF7tWvSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b666d08ac3.mp4?token=o5Z6abMmKMvb05YDONWyp1OOcdo9sTciR2Hd61yPzVPJS3zPDMXyjhk0XkL2bTulPSID8C_mbs23hIcsqiY4kkY-ItT84vUr7j3Ug_JvA2IgC-_-Cvq5oFS4l5G0uf81xuB_4oUizZDAskw_Up_340mxSW_SHpUxCmupa3Dj2ss_mBBu_gP2rfalxi2VqnJXD0GP-qzKbRzxrrakYLDH9BHv77oDG3EmYzibG1eFgnAdyYRJXEgUDSJLZ1yvoSiSHNlRJIoSKfH3Z0YlLg4HI1T8O3lkL9CwoPjlbzmFhnE0F-Dx_FukABV42YecLZXY5q4dFa6H_E16zPYF7tWvSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
😳
😳
😂
😂
کوروش اژدهاکش بازیکن جوان پرسپولیس: می گویند اجداد ما اژدهاکش بوده اند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/103200" target="_blank">📅 22:04 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103199">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h9c9R0FloJBjdBoOsqbZL5M6C05JGS-Dr_GhtdmGSb673bufCIHlp2e60i0CtCd-Z0uvwwatdQrS7ou9OWr_SDl4cp7aKeFlnYNmZu_QA7lWNYBrB6RgG3mCpM8W2PD8GcflUD_mP5PNhy_dUeJRPMOI52Z0jICH17GA49Ptzv2SFfCNWg5QNDjPRRuP5uX3AO-WPjGQmYnBcdpDf-sArK40AxLyvSFMtgr_hdqjPeRZtefmI1tfwmazAWha2NEz0ieqhWeKoSfIrwxiWkm-FYy9zVYRn8Tspp4OvB8XmQrWqC2wTHUWMvLC51dYTK9mtPtYnbW6qYvTu5llPYrHqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
🔵
‼️
درصد شانس قهرمانی در چمپیونزلیگ فصل بعد تو سایت های شرط بندی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/103199" target="_blank">📅 21:58 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103196">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/e_UbKu5NFWoIlx-j8O2VquRNbwA26RcKq-BHs_ltDvYuGU8B4MfsPRy5E5YZnBUrVddLfrlB_bq8mDYlQT9v_ESb4wgBuvtLmXh9gIbHNk7hB49SIsTv_XT1iMSZ7b7PVmUxpyjMYsdM9lErCrdXuOOJ5trcUZ0KPTQAsFy11Y1AoHL8LQLeRpFDjpAC4-DXNiv6mSfZDOvDOrmziK_Ojkrt40fFbrVT1RTPPt0yIE0m8FpsJMN5MutmfmA3N6xBjIkzA1b0EWLfG7F9oC2uBHUSzPm2lzn2FdvcUxomHzF6Sfx9hQKes6yZiKokc_xG8-JaIxoHrxBkVN2Uii2M-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SyGVIjDlFkfJPErx-KxhYiyOYRNfsqJxMzETAiayLm_c7uwVkQ46MX4-RaFv9H-j2UGKNN39CXI3bKzDJ_V8gASSSnWUC-Llh_l6RHzqXhxAaqGx6qEsn38SOGXlv88WFOR2uAEDFuSW7OfBf2-2TB1cKZ7dfzn3Oap7WwSoqNCvsVch9c0_K6sgQ63XbTplX3Nn6tJZofmj_IDwKcbruij_eOWULOG7-iw2zatpHeP08JOpyjskCHD1b-exT9VRP-gCnQmqSSf_4HFhVD0e9QPTQ92IuhFhovnBKdZAxWj203RjGLk-RW8a-VtpriMIez2jfVmpIuczTs982DUAmA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9bef03110d.mp4?token=AMoBQsh_8JRjE3PqmotDZBhAj09RsauP3ymZwz7YnTdHYBGkNxqT7Nnk-K1a5Vp5dSZIu0cnITIcnof6Mv6MErgn98mfscYCgb7DYGOCcgSPANnnmepbNIr_ZnoilWK3fGgw0nfwna4Eja8JrUe_m-7w9WK9m1HEO5nDq8goYiE0rGdOgpr9OH_Ir5dl40KS0jcG5oiH46_gddqEygollwtHbO4ARU_gc-zfmC6pl-V31aEyag3gsVaHMcmhOpaG6TWDqtAIF-RYtHm-Rg1CZ_WOf072USEoQTe0vPKLQ7wTs96u2jhfsojGWwojsJWxvoFeJ7AaPoOD6ckQ3TPkCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9bef03110d.mp4?token=AMoBQsh_8JRjE3PqmotDZBhAj09RsauP3ymZwz7YnTdHYBGkNxqT7Nnk-K1a5Vp5dSZIu0cnITIcnof6Mv6MErgn98mfscYCgb7DYGOCcgSPANnnmepbNIr_ZnoilWK3fGgw0nfwna4Eja8JrUe_m-7w9WK9m1HEO5nDq8goYiE0rGdOgpr9OH_Ir5dl40KS0jcG5oiH46_gddqEygollwtHbO4ARU_gc-zfmC6pl-V31aEyag3gsVaHMcmhOpaG6TWDqtAIF-RYtHm-Rg1CZ_WOf072USEoQTe0vPKLQ7wTs96u2jhfsojGWwojsJWxvoFeJ7AaPoOD6ckQ3TPkCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دوستان پیشنهاد میکنم حتما از ست‌های برند mimoa استفاده کنید
🐸
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/103196" target="_blank">📅 21:54 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103195">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iBZVDX359FA6ifjG43ne_bzsTonyu5zwEjC_WLJ45B4T8HCtID0hvrIxdMUd3S_e1AGjQdpTHHQcCmEYtqhgUQtbcAS-1vvUy8r4OLxX78hGmcRao-_Dvzs84tTTo5wLNwCXB_rqQwltEs-K2xB6W-k3Z2ae8qwxhWRYagrHIYftA9nntGRKL1mmdl0k_XA2glwnB8bZ74LE5bcnnJtt9KPYT8xn9Vv0Mkui-ldet3wnEWjZuVxq-upI_EycpMmfDHL_wl9WMHd9UWV-DZbC_Bxg2_nqJ2zxelp5YHa0IRkRzE3UmWaoa2FPDWw3knyVZXFhtJ028ju_9a1eJfUh9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇹🇷
🇹🇷
#فوووووری
از گری‌جیکوب: دو باشگاه گالاتاسرای و فنرباغچه ترکیه بدنبال جذب گابریل مارتینلی ستاره آرسنال هستند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/103195" target="_blank">📅 21:40 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103194">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vg5CtWU0AxkfWp23DoshOjrJBjUj-3Wo8kQhaJ_uo8JcNq0hYpoZOobYI6BXVsDbmUD2wc1RaT78NETw05Afc3KMFEYy1wCxMSHt3DFS-uaR2kMOncvBuFpb9Tl1JYy3f6IZeYYXn1w5L9veC6j3a78d3i0KQFB6XBLNDgAKwGe9gWavRg4Ve-Ny_IeAVw8UjWtO1npgN1sh5gOr1smosznfYb-JyzC2N2GKo8HkhXbZWPTkvNFsz1QmO1N-Ha_xrwJ_ajyA0xy2u2gMUHOr3_RbLVNOh3OMjJRnctAckJuhVlgdApqOd215PE_sYD1maIkUHcWwrkbhHI9zx75afg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🔻
باشگاه فولام‌انگلیس بدنبال ارائه پیشنهاد برای جذب هکتور فورت بازیکن بارسلونا است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/103194" target="_blank">📅 21:14 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103193">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n5qWMOIgfUpIRYjl9mZt39kKZR03cxbNpInQaLsPx2fD2ERJmEooJyb4d-z4XS5bvyZHSfc6Fv7ShVX5eX3PiBrDvucAuLAsKQYEBkutDp9jeliefsQmldIYlbPH7t899wOKNFaeqOJhKexNdDja3fEfxpUgfKzw2999T9czbOOnvZBlIIBWonEPBGi0s2dxNUIJl4NA92RP2IRvSeSHcMRreFu_HPLUmuXGtS-UcUywuoEwQIjT0RVN5gLA12zuFnyB2SRAJHEx9ezWnWsIRBu9ztrrQC4z_f6mfISUHZKTeY4n3a39bdDetrl_xZUZHPgF37U_SAJD2la-oei-BA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🚨
🚨
🇫🇷
🇪🇸
لپاریسین: مذاکرات بین پاری‌سن‌ژرمن و بارسلونا هنوز آغاز نشده، اما ارزش انتقال او کمتر از ۵۰ میلیون یورو برآورد میشه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/103193" target="_blank">📅 20:48 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103192">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VeYmYekVIl3iBd9rYMP7xKtkWHLPqR9HxUERa282Zi2cbPCPtpDXSrDz835hzzyGucLDPPkZzfBXZZnIDkDCePvuoVOIXFNnroIIvn4ysHHp86K-euIQAeGcDsi2lUbtirUJLWiwSt7vouRmQmBO89PODhbE2nV3xsiC_Jk7bw_iOfZHomfI_ZfI_qukgIzfkaIKR2sly3QvzgY_KSvX0ifs0m1JykFC0zocx_ZI1sLa0Wnv01MxeH9caMSqt2jrl2woVfo3NBfcn0anB3DpF5brPb9lKgRZQZAPo2-ylyttQVbM9tSV859M-qv4aFmNjZJOfwBh450i6OIh5_Y_HA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇮🇹
🗞
#فوووووری از رومانو: چالوباه از چلسی به کومو با مبلغ ۳۰ میلیون یورو   HERE WE GO
🔥
🔥
🔥
🔥
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/103192" target="_blank">📅 20:34 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103191">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TxrnlnUxmXetSVCKKIzWSI2XEfeLWVC0DbWXJFfyDWVGPJw5pOd-uRNT3ZDzKbaUBuS7QWBfrj8ehxaoYR7KpAETxKRdV9AUMENf77Q6-FhkCXEepkaMGY7G9JwL5r_eG-vpFgVszsHvwBG4SauOlImL1fZeiQtcRhGgXtwEXG56mWmbMs758lvThNrqS_NBiMy0xutHOexuM9npYVix3-N7Jnw7y7tcwrRVI1pg4mODfVi_tqJwektH-KGxSHzaILNGIDuPKgkNg9EAXhOfwjnPVZ7mQNLMSqGwwyYOK_h-pmLZM9xXlH3Iw0Rmtm3wVcKa6iz8-ZSnwvbztIokCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
✅
رونمایی‌رسمی پاری‌سن‌ژرمن از لوکاس‌دینیه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/Futball180TV/103191" target="_blank">📅 20:05 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103190">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NA9wNYXrrgFOiTLW2dOkqCG2nGSEY8J1bkriNKdOn4pq4kNidVwzvQuVYlRGJceaDWXj_Mf0JAqXSE_bqXmB26Kh5gkyhC8hNdQvduBKf5r15wKJNdkODLv3vMm4hrk2EmbB03Gw5nx1Ck07JkFg8CBkM6iFGOFeeIz88sB8RVB8Dk48w0W4UyWWqD7xPZq3SlJWQFBUBpMW_1YGiDeNEGFBkhi2x8Kfp6VFYb8lMvmQyQ5nyDX9RBTNCglHj1_wHXVCzwuk9beXLy7dPnjppT6VV__ExiXXn4XvUVNP3SF3ZsXn-l9jasrJ5vawroSQqFlQHJfMqs6EZAd2JFVBLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسطوره لیونل‌مسی در مراسم خاکسپاری پدرش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/103190" target="_blank">📅 19:48 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103189">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/79470446aa.mp4?token=oIno1iZfBl9to673TnkzGasBXljdFzPbrfsRHjpgQYKIuo6hb0hTxJd9Ws77HrFU1k06TkE5nFuHpYfy5TU9x473-KDzFemHfCYAoin_naWeMawLk3xEyhWfIkrpyvWBgpyvKQV39W-7J2xWeM_CJuytXdPABJ47dxdNfRuCyv5VR8FNgiZ5qiKRAmU6maKkFdeByl3SxoR3f5kWxFBSbUgW4Nl1N7sFq9ICHJbcMlVWQaD1GLle2uwWH7WKc5rNsOjruF5WrECT6NDj4Gz0ipPx01Pm5ByxHffaZ65a6-nlrrSNLxWacCegFeEUukkB3zrzmtBwdLrJoXIAYVD4WKkcx6iPij-uOQ31N1nPdOZYgX5IhYNdz6rve6V8elQ9u4CjkMSqsDvySvZbmeknjX8lposLkUPAI-jm_oa5rr3i9QNo5glkjF2wUfPpSM2sZS9OETaa7zh4Q6UIF0VCh1uE3V9R7Gyx85ZChsFmxklPcOZAM0kcmKGxPyhWoAh4A2uFH_L9TYsv2UTWPnBaBi24DvoVKexMmaHwFlRCjPrHyPO0mC-V44gKyRR8qbT1LOquoP6Rv2Jc5ZSQlIXHgPpTG9uADBEB_AaSz5lJZIIjyzQ-g7Y1rSV_rNeDdTqbHduLNxjCe1ZzaWD8L2VxbpHRwdPFHp8W87Gp9u7GEbQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/79470446aa.mp4?token=oIno1iZfBl9to673TnkzGasBXljdFzPbrfsRHjpgQYKIuo6hb0hTxJd9Ws77HrFU1k06TkE5nFuHpYfy5TU9x473-KDzFemHfCYAoin_naWeMawLk3xEyhWfIkrpyvWBgpyvKQV39W-7J2xWeM_CJuytXdPABJ47dxdNfRuCyv5VR8FNgiZ5qiKRAmU6maKkFdeByl3SxoR3f5kWxFBSbUgW4Nl1N7sFq9ICHJbcMlVWQaD1GLle2uwWH7WKc5rNsOjruF5WrECT6NDj4Gz0ipPx01Pm5ByxHffaZ65a6-nlrrSNLxWacCegFeEUukkB3zrzmtBwdLrJoXIAYVD4WKkcx6iPij-uOQ31N1nPdOZYgX5IhYNdz6rve6V8elQ9u4CjkMSqsDvySvZbmeknjX8lposLkUPAI-jm_oa5rr3i9QNo5glkjF2wUfPpSM2sZS9OETaa7zh4Q6UIF0VCh1uE3V9R7Gyx85ZChsFmxklPcOZAM0kcmKGxPyhWoAh4A2uFH_L9TYsv2UTWPnBaBi24DvoVKexMmaHwFlRCjPrHyPO0mC-V44gKyRR8qbT1LOquoP6Rv2Jc5ZSQlIXHgPpTG9uADBEB_AaSz5lJZIIjyzQ-g7Y1rSV_rNeDdTqbHduLNxjCe1ZzaWD8L2VxbpHRwdPFHp8W87Gp9u7GEbQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
⚠️
حمله‌بیشرمانه مجری صداوسیما به علی‌دایی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/Futball180TV/103189" target="_blank">📅 19:30 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103188">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lqHpxe_CWA5yzhbn0ZV2zIvWrFvjEaUY4biQ-Fxfm70A0DTunVXao-7U8nldnc4p18jqjNVXOeRVa_QuHTFJ9N4Rrk8VXXAkFniJFc89_a-NXk_SrXK7VIT2zXikU9Yrxr-66EIxY0tcfP9PlgGzk7XCNFNvcpttHoCceqh322Hic8GUnRjB0p4NC43dCEOhhW3VRr1Dss3zwkAi5zpo4Y7HQeZoWYcFjaqT60FndVF6rn_C6DN-8vTLsCGHnp8NCoeJD1SluyD7s9-YA1j0875QxsjVnYV4x6fePZOiE-jdvUxwm3Qa4jKkX85rV2y4kpD3t6KrZDsFdDY6deNnmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✅
🔴
پرسپولیس در دیداری تدارکاتی، منتخب کرج را با نتیجه پرگل ۱۱ بر صفر شکست داد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/103188" target="_blank">📅 19:11 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103187">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hHPysjT6Lank21xPoyLbJ-IRFyDLgB_CjasS08IDNTJoVNtdYqfalAAL3cOPrck57uT8YseIkU-U3RT7dWFY8iUT54YGfxfWvNnXN6GuZ9K-GTAfbogFdXuR3PogMvSGfvnaU7pFQ3vZrGsE7q0DuoFMu3tTT-gVMwvoRTbcW1epAJko_7vUEvIwtUkYr__D5whe33fwbwpWJgQrvqvOXjo8gyc9XgypLt_Ekku-Uof7512NcttDdW-LcvLwB8-Dgy8q8cGxc9Jz3EPb1f1CW5uEZswrqMCU36rTEDq9WAbvE_yRieLG-6oLXEzccUqKX7Vpy5iotoEswyABUEUTYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🎙
انزو مارسکا: رودری؟ فعلاً او روز چهارشنبه در منچستر خواهد بود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/103187" target="_blank">📅 19:09 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103184">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dd83a8ae00.mp4?token=NRl0_S5SniwnaxKAITDTgUhemfLT0XgCv7Jefuk7uSleaUZp8BSEqr-M5r6WsG4PeYjShTJm-Zr4Dhn6nncIZcx-L2uFccuXHfziiYyNLY01c0IWbiJt7rb7NeCUo6zOye4m-2SOK4K6m2Jvvv4CDSOej179K6lbLxKxZnprrlARWUqT6jkeQ3M6ngMel57puhvBWMPtdoGy303ANjHCJ2o47LIPHbW180g8tUzTzWS8aoyJzLcYlxwTokmjPxtZjeHSXMPaHrKE7FwJ3OBTRzV3NBy40lhUuZDUoJgeYerQn0mUb8FxRgpRrnXfKkHX6fWXAPvc9iu6OEmyIOBQyycE8vJnnfWC7HB11okmDUgKl8TAUgNJkmMI3VqD_fcBqzWVXFFnBGvBGUyuD2n-5ClyNFWiCx1bvEitPnTjh1ZuFqQicva4buHxEulrTE5fKf6nBn9WRTJihcowyNsT8R_LxC3U5pRLHKEsBKislKsiLC14PxVMoUlHVt2aVRHDz3LxWuItVWK1XMyuSw224aayK9aU68I8pOrWx7xKevaFUKKbRnNQVvVzPXV6Ji7ttilKa0NK2rGRfZKZVuWG9YAThaAjzNDdzYkg5YzB4ItL6bc0yBOvKgYEVhrgJokN0s9i2kIyDrfcWb3dr-xa3gncfCtWKvt__I8uuTh5hik" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dd83a8ae00.mp4?token=NRl0_S5SniwnaxKAITDTgUhemfLT0XgCv7Jefuk7uSleaUZp8BSEqr-M5r6WsG4PeYjShTJm-Zr4Dhn6nncIZcx-L2uFccuXHfziiYyNLY01c0IWbiJt7rb7NeCUo6zOye4m-2SOK4K6m2Jvvv4CDSOej179K6lbLxKxZnprrlARWUqT6jkeQ3M6ngMel57puhvBWMPtdoGy303ANjHCJ2o47LIPHbW180g8tUzTzWS8aoyJzLcYlxwTokmjPxtZjeHSXMPaHrKE7FwJ3OBTRzV3NBy40lhUuZDUoJgeYerQn0mUb8FxRgpRrnXfKkHX6fWXAPvc9iu6OEmyIOBQyycE8vJnnfWC7HB11okmDUgKl8TAUgNJkmMI3VqD_fcBqzWVXFFnBGvBGUyuD2n-5ClyNFWiCx1bvEitPnTjh1ZuFqQicva4buHxEulrTE5fKf6nBn9WRTJihcowyNsT8R_LxC3U5pRLHKEsBKislKsiLC14PxVMoUlHVt2aVRHDz3LxWuItVWK1XMyuSw224aayK9aU68I8pOrWx7xKevaFUKKbRnNQVvVzPXV6Ji7ttilKa0NK2rGRfZKZVuWG9YAThaAjzNDdzYkg5YzB4ItL6bc0yBOvKgYEVhrgJokN0s9i2kIyDrfcWb3dr-xa3gncfCtWKvt__I8uuTh5hik" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😞
مراسم ترحیم پدر مسی اگه تو ایران بود...
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/103184" target="_blank">📅 19:01 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103183">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/edc71e63ff.mp4?token=hQhkr5TsyO68BYs9jsly2S898q_jYkpCZ8gAu7EbKG-t4liWU_xdIA7UlrZnBj-T1AUfQDNTznh9DS2ckr9I3BKPHyTrL0VFq3AlbUzVXZtDCDmcAKJavEDfxd3cJzh0U1oBtzL2jL_-qjThYxByVwc55VULEmSHv5A7bjB35upCXCsWNO5GLaFq77GSwjlwhv_26-d0GghnNbmC_5jB9IO8m3zibVPMg84uEQ7Jyyrwx44GY4MgDGYyXFtUWL596Rl-KvCoWISu23b0XUQ38qABPusZ6_2PNg4fkZ-jJ4z9XdcrF8uSoiiQ6jtSdnFYbK0dbfX3aPubm8V8gTnm-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/edc71e63ff.mp4?token=hQhkr5TsyO68BYs9jsly2S898q_jYkpCZ8gAu7EbKG-t4liWU_xdIA7UlrZnBj-T1AUfQDNTznh9DS2ckr9I3BKPHyTrL0VFq3AlbUzVXZtDCDmcAKJavEDfxd3cJzh0U1oBtzL2jL_-qjThYxByVwc55VULEmSHv5A7bjB35upCXCsWNO5GLaFq77GSwjlwhv_26-d0GghnNbmC_5jB9IO8m3zibVPMg84uEQ7Jyyrwx44GY4MgDGYyXFtUWL596Rl-KvCoWISu23b0XUQ38qABPusZ6_2PNg4fkZ-jJ4z9XdcrF8uSoiiQ6jtSdnFYbK0dbfX3aPubm8V8gTnm-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این کارا چیه مرد حسابی
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/103183" target="_blank">📅 18:58 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103182">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇩🇪
هایلایت بازی آرسنال 2-3 دورتمند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/103182" target="_blank">📅 18:36 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103181">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c55e5129ef.mp4?token=cp2xUhFryljhKtON2bRDKqrfVpygA0wN0Vl3o6Tgb7_Zf7G52kZ1jb9MBYsm-4bDlMGecA8cuqX4LX8uV6botQVeex6-Bo8aRzpOUqrF2O-PSslkgmJRqaYZAz3LffKNsQEBAhu644NQ-3wNy3Wllgf3f-7kWCygpoO6lsn2GZXcGNj7sB-_eleOpk1qPhujhctFa8mECXonGUeAx02fMTr8s6wdiNHom5bsxTefkmEjPcjFD_jYxMtlq9fA8r8VibjfkZGZuL-CKNs2gXyfSnGuB3nA25OmXcHW6H9GTD-0WRtnW75a8LJc1BxedjS9RQeDOpSzxkYt_2C9hl3KFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c55e5129ef.mp4?token=cp2xUhFryljhKtON2bRDKqrfVpygA0wN0Vl3o6Tgb7_Zf7G52kZ1jb9MBYsm-4bDlMGecA8cuqX4LX8uV6botQVeex6-Bo8aRzpOUqrF2O-PSslkgmJRqaYZAz3LffKNsQEBAhu644NQ-3wNy3Wllgf3f-7kWCygpoO6lsn2GZXcGNj7sB-_eleOpk1qPhujhctFa8mECXonGUeAx02fMTr8s6wdiNHom5bsxTefkmEjPcjFD_jYxMtlq9fA8r8VibjfkZGZuL-CKNs2gXyfSnGuB3nA25OmXcHW6H9GTD-0WRtnW75a8LJc1BxedjS9RQeDOpSzxkYt_2C9hl3KFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قلبم گرفت حقیقتا
💘
💔
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/103181" target="_blank">📅 18:35 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103180">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pPGo4oXIo_8BUpZHDDvCaXJJmpvECqQhofG-ZkipjU3JgfqDkFB_tlNm74GIU9hvCa2pMgUS9M5MXb7JOCupE5mQ25WD3GS9wELXLYQuBm-mhuaMsQsSHpIdu-81yXz-Rwi2jvyQrPcGDFQJMdTv_9egSdR6761akXVT0mtkZs8EGFhLehlgv96I4AXl8sZ74YNVx1TLHpDwajS3UacJaw6ebPKR4VvBOSkK9xwApi_rSxp4cpklzBMZ3ygcZMNS6Xf1fJ84lzSMTXuuNwooQOct7ukJyelqSZhXu7pfcJBZRkbgMwMQnHzKLINHPrXfOnX_RGp2CUbSN0tSkCmK0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇫🇷
🇪🇸
فابریزیو رومانو: پاری سن ژرمن زنگ زده بارسا و گفته با بازیکن تون به توافق رسیدیم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/103180" target="_blank">📅 18:12 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103179">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f5ca064762.mp4?token=oQxCHCNrf6BKR2o-uGRHjm328Dt9HpxBSGbCZvYdQarFs0_zH3jr5ZqkoTAdvdlqpA_F5k9n6ykMdUpXDt_cOrn6W1cruFHQyANkLfqET4MWVS7s7UNfhgL-yadb8_N_NbsYq6Px-XUmad2_TaP-q7HPBj3TUcxtcSok0Vne6isFSw8x0VUlTa-Qoxo2LwpA_po_jRGktlt94NGeF9DdthEEo6lGINeDqm6m8A4JFFm2e3sF-uzG6KG_AdqgApoejUngiTxCjyS1wGrcQgWaYMBsKpZfpvIXE2j5W2X1HPv3uYzr-tonVrBdUpF9cOvr2v9WiEHkJZi6-Z32rFIvLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f5ca064762.mp4?token=oQxCHCNrf6BKR2o-uGRHjm328Dt9HpxBSGbCZvYdQarFs0_zH3jr5ZqkoTAdvdlqpA_F5k9n6ykMdUpXDt_cOrn6W1cruFHQyANkLfqET4MWVS7s7UNfhgL-yadb8_N_NbsYq6Px-XUmad2_TaP-q7HPBj3TUcxtcSok0Vne6isFSw8x0VUlTa-Qoxo2LwpA_po_jRGktlt94NGeF9DdthEEo6lGINeDqm6m8A4JFFm2e3sF-uzG6KG_AdqgApoejUngiTxCjyS1wGrcQgWaYMBsKpZfpvIXE2j5W2X1HPv3uYzr-tonVrBdUpF9cOvr2v9WiEHkJZi6-Z32rFIvLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
🏴󠁧󠁢󠁥󠁮󠁧󠁿
ساندرو تونالی هنوز فصل شروع نشده حواشی خودشو آغاز کرده و تو بازی دیروز تاتنهام وسط بازی با بازیکن حریف به شکل عجیبی درگیر شده!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/103179" target="_blank">📅 18:10 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103177">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EsmxL4jrLitTytNGNIfx8F0D39UOQYR7WDCql-RDcctsKzUeVfPDR583Cxrf55FvPtCVFYdmdceoPyzAVvoFoHBOchJlVnG5RMH8oDxeFrP-lrqMVRFlRqf2tXfqeiWWhRhLXtI-biTqDGqpAYESLkS7Q_nu_atcdU8PR4nmCxB3ef0Rl1ZKn-kfQ7wfUX-EhdMJCwzJfD0NyhxnqfXmJds5paVrnYWYMwpi3esyd0pO1cTA3QDUOgePNrnSl0sAYYUoNn6wzZKHSZZugOUos_J16pE6bsl-2ZpmRyc7tKDrgb4bx3_2ALYttaKk5Itxt2eIMywBO5veUNweVrQegA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vpi7itI2w10UtSOpa0FJ_vclwYDURRzY3DTGZVIQz-XSgXE1vWai6K4Ki6ybUXuoeqV6HTrW3dwqiSWPtERtDihfv56h-jj7k-S7p3l7WY33HKVEteA0x6-Jq2w5s0AyNX-KDOukod2Za85Sjldv7e1WXTDE8-9cbu7K-Y7Huk4ktzfaeXjuVQcAty1FylTw1qqz5gDTiUSQPywMnVESdqjiqN1_PP0tAGQc55ljTqN-eN_QRlOD9_D8GyIroMUuuQfhbDAu9_9rPDVNqNInuG3zWBXuFOrVzeLwVIkjAMv5szNO9bvzDKBvz4Sse-_Mo9KelZb4b1-DeWq--wN6Tw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👀
🔴
رونمایی از برونو گیمارش پیش از بازی آرسنال و دورتموند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/103177" target="_blank">📅 17:55 · 18 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
