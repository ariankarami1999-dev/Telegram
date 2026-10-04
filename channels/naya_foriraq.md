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
<img src="https://cdn4.telesco.pe/file/cQFBfWzxi_twoemKTIE28fsIA2wlv5jDAbKq0NRGE7_mtpJrHCu2NuczNbSxN3NF57D539HIPWLzjJrDQQv5NHDgq44p2MipeLLiZfOUd5ruQP-t-HpytOZ1VQaHXeDpcPsuAZc7uDIF4LPM6W06m7-tCbL1ReqGQVGmb0tmhj9Nsw6B7eTjm34b5CuN2zF66l9cHWo_NB-7e2aVFI2ep8pAt_sta4_82FNr-tLlj7IP8Ea0r4K9ghSGtMbmiCe829MUJVXBt5LizRVmVM0CZkdKSHo8CNH3-_-k7bnyrzJROKg9oi5adtiOf4wF2WlxJ7QsBa9SDRs_htNwy_gnFw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 265K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-12 20:42:00</div>
<hr>

<div class="tg-post" id="msg-92516">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🇾🇪
القوات المسلحة اليمنية:
تمكنت قواتنا المسلحة بفضل الله من التصدي لتشكيلين قتاليين سعوديين نوع" F15" قبل قليل،  في أجواء محافظة تعز وتم إجبارهما على المغادرة، تمت عملية التصدي بعدد من الصواريخ أرض جو محلية الصنع.</div>
<div class="tg-footer">👁️ 1.32K · <a href="https://t.me/naya_foriraq/92516" target="_blank">📅 20:36 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92515">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🇮🇱
الاعلام العبري:
أفاد الطيار العماني خلال التحقيق، بأنه كان يخطط لتحطيم الطائرة بالقرب من مطار بن غوريون.
كان يخطط للهبوط بشكل طبيعي، وفي اللحظات الأخيرة، عندما لم يعد من الممكن اعتراضه، كان سيحطّم الطائرة على المبنى.</div>
<div class="tg-footer">👁️ 2.56K · <a href="https://t.me/naya_foriraq/92515" target="_blank">📅 20:29 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92514">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c113cf919.mp4?token=jj4HMYwvYs_G4X5EozpW_zRBqL2kkBvDPdf7ORrfPlwiqTgYBIZNqT0LpC4cefLhORk941UmVie3bdFcpxHN1ude5GHsRDX-ZreQ2SG38rq_teXX4NjihQrD5wD2Jlk1SbAZ8oUNEs-Ybf0sadBiLacpaDNGLmKgvfx77uB_Mf0XXuNDI1qB9fAA3efHBjoHYeLYNNRT4LUdrLM5KT4FY_lXGc38w2mrnJsn3RbBwVW2CQrEugknU2Y-NtTQ4AwObbQpPjd8mWQCRp9UkPPjoZsHqsxzOEg-kZmlAU1HimrI_v_1d_q4TCliXxbCn7VjaqvwK0XIvoSmWb7RSXrf4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c113cf919.mp4?token=jj4HMYwvYs_G4X5EozpW_zRBqL2kkBvDPdf7ORrfPlwiqTgYBIZNqT0LpC4cefLhORk941UmVie3bdFcpxHN1ude5GHsRDX-ZreQ2SG38rq_teXX4NjihQrD5wD2Jlk1SbAZ8oUNEs-Ybf0sadBiLacpaDNGLmKgvfx77uB_Mf0XXuNDI1qB9fAA3efHBjoHYeLYNNRT4LUdrLM5KT4FY_lXGc38w2mrnJsn3RbBwVW2CQrEugknU2Y-NtTQ4AwObbQpPjd8mWQCRp9UkPPjoZsHqsxzOEg-kZmlAU1HimrI_v_1d_q4TCliXxbCn7VjaqvwK0XIvoSmWb7RSXrf4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇦
دوي صفارات الإنذار خلال جولة المستشار الألماني فريدريش ميرتس والرئيس الأوكراني زيلينسكي في كييف ما دفعهما إلى مغادرة الموقع والتوجه إلى مكان آمن بالتزامن مع هجمات روسية عنيفة.</div>
<div class="tg-footer">👁️ 4.62K · <a href="https://t.me/naya_foriraq/92514" target="_blank">📅 20:11 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92513">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0bf58c285b.mp4?token=pz8behAvo8TGyWCSlti_AX9vu1wjpZSWdkTQh1w4_K9HVEVaOGYcU9gZ568h37gfTyMn8FOeLoIgVCR1m-e5R1fAl_azWakTauD-5B4kXzSFHUK34fod0cSif6cF1Hpmu8yU_FkWcWFgHdYXjvhgKp9XD0QdyDs6aJr7sQ1K0YbcNz4iYnnAsgwJLdvz3pbjYe6AQtxZ1dqz6GvzxJjiAABE9q71A4Vdg77bnsaj7bcJPVWvZPhG0JjjBmoi7VgTu0LfdosbmTRg5uN0o5P0KuzSunk7M7cpz0W2yEm86bpW_9Sl-ou961AZMHa-mOGxKYvnvfy3_91dg2Ejk2Twqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0bf58c285b.mp4?token=pz8behAvo8TGyWCSlti_AX9vu1wjpZSWdkTQh1w4_K9HVEVaOGYcU9gZ568h37gfTyMn8FOeLoIgVCR1m-e5R1fAl_azWakTauD-5B4kXzSFHUK34fod0cSif6cF1Hpmu8yU_FkWcWFgHdYXjvhgKp9XD0QdyDs6aJr7sQ1K0YbcNz4iYnnAsgwJLdvz3pbjYe6AQtxZ1dqz6GvzxJjiAABE9q71A4Vdg77bnsaj7bcJPVWvZPhG0JjjBmoi7VgTu0LfdosbmTRg5uN0o5P0KuzSunk7M7cpz0W2yEm86bpW_9Sl-ou961AZMHa-mOGxKYvnvfy3_91dg2Ejk2Twqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
🔻
الشيخ اكرم الكعبي:
#إجرامكم_تحت_اقدامنا</div>
<div class="tg-footer">👁️ 7.32K · <a href="https://t.me/naya_foriraq/92513" target="_blank">📅 19:41 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92512">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ocmgABEtGhQ_OKkE6lceqGSsBFstZgQRsrKuiMs2nnAWO4fsIi2WHiokaG0k05aaRzjjxGSENMLcF5uVZ2xgJqDS_MzEQaqhK4AgYwFv1OSDOI3-FV0arzpIoEi-j42oad2RJQsK_apm7jvNapPQGd2Ob63z1-hNpXjSCPJpaSM82l9PUbMO_QzSzmO0blzplit_nQYt0f9Hiy2tSUH4M5qPr981YRwJm240NY4yOQg06Txe3Z3HKKRRPg50Uwh0-ZgNGiyfqzylew2pfV14--yEnH3HW9hgds9K4ZR56iRBrdlIQe_2LH35V7KsJLT1DlNMYuJaSJIFxnjYqQQRxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇾🇪
انتشار قوات المسلحة اليمنية في ارجاء مدينة التربة بعد معارك مع المليشيات الموالية للسعودية.</div>
<div class="tg-footer">👁️ 9.05K · <a href="https://t.me/naya_foriraq/92512" target="_blank">📅 19:20 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92511">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🇮🇶
🔻
تفاصيل العملية النوعية الكبرى التي نفذتها هيئة الحشد الشعبي، والتي أسفرت عن الإطاحة بعدد من كبار تجار المخدرات الدوليين.</div>
<div class="tg-footer">👁️ 9.35K · <a href="https://t.me/naya_foriraq/92511" target="_blank">📅 19:16 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92510">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/89f1232971.mp4?token=M6AFBC5PdyD4j4FVYmpkpMOcXut5DoMqSI1gIBX1ZlDluvCA5fHiDkPXmacvmcrofO345N2Th7f5QB2ON-XsCMFQnkRzkAbAh9_Kh95EsoEIde6NkgWUQEhQp9Jh7LW-9dvQ648f497S0aHMRD4FSTQ6Uaeijh9JeBLpnNwW6Zgdz0xJFF0T1driOk7K64UGP-fXsnjS7K3cY1gXEfWdkw1x0L0lJ5qwizaJjVotFaO5YSEu_LWK43oM3KHJv3EfWCsPCMLszX7T83y7LBqRuNJNxWwijfNnPLiN_Q7Ehs3XNKGN72E0LhW8n1jl8c9VLyZ4RD4l6k4MIw3fdc57sQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/89f1232971.mp4?token=M6AFBC5PdyD4j4FVYmpkpMOcXut5DoMqSI1gIBX1ZlDluvCA5fHiDkPXmacvmcrofO345N2Th7f5QB2ON-XsCMFQnkRzkAbAh9_Kh95EsoEIde6NkgWUQEhQp9Jh7LW-9dvQ648f497S0aHMRD4FSTQ6Uaeijh9JeBLpnNwW6Zgdz0xJFF0T1driOk7K64UGP-fXsnjS7K3cY1gXEfWdkw1x0L0lJ5qwizaJjVotFaO5YSEu_LWK43oM3KHJv3EfWCsPCMLszX7T83y7LBqRuNJNxWwijfNnPLiN_Q7Ehs3XNKGN72E0LhW8n1jl8c9VLyZ4RD4l6k4MIw3fdc57sQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">القوات المسلحة اليمنية تبدأ بالانتشار في مدينة التربة وتبسط سيطرتها على المباني والمؤسسات الحكومية.  https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 9.04K · <a href="https://t.me/naya_foriraq/92510" target="_blank">📅 19:14 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92509">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🇮🇱
‏إعلام العبري:
3000 جندي أميركي ينتشرون في إسرائيل تحسبا لاندلاع مواجهة جديدة.</div>
<div class="tg-footer">👁️ 8.76K · <a href="https://t.me/naya_foriraq/92509" target="_blank">📅 19:10 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92508">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QlaZTLyHg62F3IhmI9PCuyN5oInULz9OOSm0H5vnRh98smLGjw1lPxL0bpu9rskiBHqQzPbNv_wC9755aSXDKx5FmG7BRqyhnAY_KrTiPZUqouX17yF3o4eqLLUvtN0TBXNp9J4ezBEm2kLBcFHYughwesvmNsFR3jFLKtUrnf_CptN-0JYqZ9AW43_q_ojMAaLnQIucYgRESXtCF6ctWp_j3FD2eaXuipO-jYEGyX7qM0ro60wFiFRttCxN0aaeKC3XXyU7bbznuXiJH3Prm4vEyNupLRcxAifEaorEYzGVm5D1VlBPkbxjOaM8ChO509xGp7KVNPntgCm_PBBikQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
🇮🇶
حول العالم حرق علم امريكا ليس جنحة جنائية إلا في العراق !</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/naya_foriraq/92508" target="_blank">📅 18:38 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92507">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🇺🇸
اكسيوس عن مسؤول أميركي:
لن نتخذ إجراء عسكريا مباشرا في الوقت الراهن بشأن التطورات في اليمن.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/naya_foriraq/92507" target="_blank">📅 18:27 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92506">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ecbo2c20pgaD1n1x-EpfNKJ8UUiBdJ4E0AftmPLw6D2MqKt44ddZwp16NGikPMc-GW40dPUzZuh2aLuaiJifH2QjrBkLD5xv_N0zYk5g5hfzjqHbD3O8xyQ0LG3VhTlv9vHvEzoh4FdjT9_v3IrUUgnAsI4E2DtXFubFuifhYCxATLDZP4TgI2IdY2joQp0Ihc-TnguOA-LudRlHbmNbMXy2t93AIf8l7y-ZTrMA3Y09JlahYoR0iKpsrgLDm9_7mTn64kUSfa0tsW3hg7fXfnSJEVIIISapeo47XAdE8oEDlIExuWiG8MnLg3uD1gc7n_fABjPHQdNI5s8WSo3RTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مطار النجف الأشرف الدولي يستقبل أول طائرة إيرانية بعد استئناف الرحلات
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 9.75K · <a href="https://t.me/naya_foriraq/92506" target="_blank">📅 18:25 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92505">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">القوات المسلحة اليمنية من داخل التربة  قلعت البيضا ثارت  كل نشمي حر ثار</div>
<div class="tg-footer">👁️ 9.54K · <a href="https://t.me/naya_foriraq/92505" target="_blank">📅 18:18 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92504">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">القوات المسلحة اليمنية من داخل التربة  قلعت البيضا ثارت  كل نشمي حر ثار</div>
<div class="tg-footer">👁️ 9.59K · <a href="https://t.me/naya_foriraq/92504" target="_blank">📅 18:15 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92503">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50253c8a21.mp4?token=igZRHQxPnUYwdP0ah_BreXF421xiz4th23ItWaBbacYlCOQd3RkJdPDlbiYQKy7udH82PWtxgRa0NFzUF7Ptk762e09h0vBrJ28VVY1hLNGmp52wSJ92_7BWq5VtLYSyXAXRKTairqGQIv6OX6p-VFedblAFmThThIq0xDYUHm0GlUmUQJt75Vw-tg4EFbdLdXaAJTo9JdYPYNJpXEA6Css11QTI4umCYaMO6VQrE_mTxQCIYLr0hhJniocjqqXBW13P8WraofJIwPPTKQDW4qdFjb-dxhpjuHWzyVVGnCdFtqNMPm_bIT8zfU9NautBjUA4suRUjRrJkDOVMo2Syw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50253c8a21.mp4?token=igZRHQxPnUYwdP0ah_BreXF421xiz4th23ItWaBbacYlCOQd3RkJdPDlbiYQKy7udH82PWtxgRa0NFzUF7Ptk762e09h0vBrJ28VVY1hLNGmp52wSJ92_7BWq5VtLYSyXAXRKTairqGQIv6OX6p-VFedblAFmThThIq0xDYUHm0GlUmUQJt75Vw-tg4EFbdLdXaAJTo9JdYPYNJpXEA6Css11QTI4umCYaMO6VQrE_mTxQCIYLr0hhJniocjqqXBW13P8WraofJIwPPTKQDW4qdFjb-dxhpjuHWzyVVGnCdFtqNMPm_bIT8zfU9NautBjUA4suRUjRrJkDOVMo2Syw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">القوات المسلحة اليمنية تبدأ بدخول مدينة التربة</div>
<div class="tg-footer">👁️ 9.86K · <a href="https://t.me/naya_foriraq/92503" target="_blank">📅 18:09 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92502">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">القوات المسلحة اليمنية تبدأ بدخول مدينة التربة</div>
<div class="tg-footer">👁️ 9.42K · <a href="https://t.me/naya_foriraq/92502" target="_blank">📅 18:03 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92501">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JqslLHRiqe0KakroJJ-Vvi5XTW4UtQg8-4hhHgixs5mh1siXBxC42JfEdu1qL9kpUz643-Xu3fHlj5FTfQBXKztSS9zNoPSN98YmBWVEc3G3OuSe-mqL5yku5GrHtfuD_Mc0kImpDowjaZQiHmwhNJyKSjDk_AauLSVGrJ8gVH6eD_fijXQspRmX9kO6CVKKBjvACq_LE2IBp-7jZFur73WSW5elmKuTMc04ylikHwaErRRzeSGijIbdaEaP8ncUlFOYqUbvdheDvRRhHVvB6xBkYMndyqyjTzKzp6VdBqSLFKGUIHvKBRxo8VgAMM5mNAikCcvZeWLsYEbMrBT0zQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طيران العدو السعودي يستهدف مرتزقته ومواقعهم في تعز بعد فرارهم امام القوات المسلحة اليمنية  https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/naya_foriraq/92501" target="_blank">📅 17:46 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92500">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cfa1ecee80.mp4?token=VqinAV7kR652onvcLWsOeBwjfXMkpSHFmNpMsTm2mpA3nkTr5ahH9WgEDo_lkwQyhpeNXPnZ40zsMsKpNPLfB2WrrXu-iNT7O7puGtGAs9e1wTCpjM4RIWFbLcfPDg29reC4egf8QM8ibDJvrktLN8fsm4xK0LytvDuEtlWycesB8DU83mdNbPDSraZUaHJpid9b_IiPAMl4mPwwOnK9odvQrOqedJ9LD-4a7UATOd09v-N-Ze5h5NJtgVY83_8nLJrE6Dzs3JiAEcVWsmkj-gmMPK3jxbCF6rJoNJUZheC_YnkCnL993ZK3tFr8I0hJtkF9TCHJ1kOlgYWBmLW72Hzb62tQNFT--fShuMDhJvxDBd4RyTB2nDO2UIQTIR8enKWaxqBvoSvOstkOZ6KVOQN1KXQGjVgC5ZFh53ZROS9Qottk880XSTAuvdwCjnXDB0ZPo0kQETcwmdfi_HdCma2JtDUPxH1-x8BjsqCfEDjhi744HyRJEdEuvfBfy65vmNUgFaBdkqf9OqQACgxh2b977rs-1y_cx0V1NCx-flSLnWkDHmX8ESK6LnD7LhgS48Vvalvfofx7Yy7j-j2MI8k-PvkeOe3CSMeCUttAa4lObNYI3CEi6TXX8SCLNsa8nvDGnk7EEfHEMo1gwE1h1IhFA7CGJQnV-8r_sThJNgM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cfa1ecee80.mp4?token=VqinAV7kR652onvcLWsOeBwjfXMkpSHFmNpMsTm2mpA3nkTr5ahH9WgEDo_lkwQyhpeNXPnZ40zsMsKpNPLfB2WrrXu-iNT7O7puGtGAs9e1wTCpjM4RIWFbLcfPDg29reC4egf8QM8ibDJvrktLN8fsm4xK0LytvDuEtlWycesB8DU83mdNbPDSraZUaHJpid9b_IiPAMl4mPwwOnK9odvQrOqedJ9LD-4a7UATOd09v-N-Ze5h5NJtgVY83_8nLJrE6Dzs3JiAEcVWsmkj-gmMPK3jxbCF6rJoNJUZheC_YnkCnL993ZK3tFr8I0hJtkF9TCHJ1kOlgYWBmLW72Hzb62tQNFT--fShuMDhJvxDBd4RyTB2nDO2UIQTIR8enKWaxqBvoSvOstkOZ6KVOQN1KXQGjVgC5ZFh53ZROS9Qottk880XSTAuvdwCjnXDB0ZPo0kQETcwmdfi_HdCma2JtDUPxH1-x8BjsqCfEDjhi744HyRJEdEuvfBfy65vmNUgFaBdkqf9OqQACgxh2b977rs-1y_cx0V1NCx-flSLnWkDHmX8ESK6LnD7LhgS48Vvalvfofx7Yy7j-j2MI8k-PvkeOe3CSMeCUttAa4lObNYI3CEi6TXX8SCLNsa8nvDGnk7EEfHEMo1gwE1h1IhFA7CGJQnV-8r_sThJNgM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏القوات المسلحة اليمنية داخل منزل ما يسمى بـ"رئيس البرلمان اليمني" سلطان البركاني جنوبي تعز  https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/naya_foriraq/92500" target="_blank">📅 17:38 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92499">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🇮🇱
🇺🇸
تقول السفارة الأمريكية إن نقاط التفتيش في جميع أنحاء الضفة الغربية ستغلق يومي 5 و7 أكتوبر، مما سيمنع فعلياً الدخول إلى " إسرائيل " باستثناء الحالات الطبية والإنسانية.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 9.96K · <a href="https://t.me/naya_foriraq/92499" target="_blank">📅 17:36 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92498">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gm2K_bX3YNvLTfIwb69UqH_jpiWjdZdInReJ1spy9NlyXYDnaI-TxlbQHtOdstX_TzjsBz0uS-OqE62rucurJjwkhu3_as8-IH_7Q_fBOhtYEG4PO8dT1luh3P6B4Gceqf05IuIk5tGGdAZahAPEaMthRYqHqeMnZsr3dNFEZujj03uUMtbm3qpBIjuAA712vnQU3hD3DcLh1MqIRRPCxb4XtBjkKtljG8TKwx_VvnlLej_XPmtdpwy1x-E_3bD22-T8gMCqWffonbSUJMmgametj7aeUnDvymV4UGIy5vHsRRfsH_c3I80wjOSdu2NDS7lYCTsFzQK4swKXJhrZMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
🇮🇶
حول العالم حرق علم امريكا ليس جنحة جنائية إلا في العراق !</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/naya_foriraq/92498" target="_blank">📅 17:32 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92497">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🇮🇱
بينيت:
هناك رابط مباشر بين الطائرة وبين 7 أكتوبر، والشعب يستحق إجابات عاجلة.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/naya_foriraq/92497" target="_blank">📅 17:13 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92496">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qjkeUJBEV_gYxa5Qt07gJn_t8w8inrT7r9SJau0APQEto6kRQc2Dmcl9lS1K9Lk1yHIgjGhucxQRoUBd2R5TOjXdaMMVEz8kHIc_EVBbA5n8605navf_VuTsv7-reRFedgmd2iC6yPvrzYhl9oBdWtLv7rZwEdyk4c4rkmAcaHuVv2RGG_KOM8y_hvB8GGK7cjnKxSLbRatJxg36jQQ14ic4NrsLzbT_A4Sa8gTy1gT-YXrkP3m5VSO_V1-PwMCxGy_CLn1kI_TmDOvVZlVJhzHau6desOw51sQFuSnCBJDXWF899t_i7V8FxZG8ZNoWRf3eu-VXlrWG3nUMcnhvSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">القوات المسلحة اليمنية تسيطر على طريق تعز–عدن في عدة نقاط على محور التربة
وسيطرت على عدد من المناطق، بينها سوق الصافية، السمسرة، جبل سمدان، والزكيرة، ما أدى إلى استكمال تحرير كل الطرق الحيوية لتعز، تمهيدا للسيطرة على مداخلها ومخارجها، دون دخول قلب المدينة، وإدارتها بالتعاون مع الشرطية المدنية المتواجدة داخلها
كما أن القوات سيطرت دون اشتباكات على الزريقة ومرتفعات جبل منيف، فيما تتواصل المعارك في منطقة البركاني، بالتزامن مع تقدم باتجاه المنصورة والتربة ونجد النشمة جنوب تعز.</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/naya_foriraq/92496" target="_blank">📅 16:46 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92495">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🇮🇶
رئيس الوزراء العراقي يأمر بتشكيل لجنة تحقيقية بشأن التجاوز على علم الولايات المتحدة خلال يوم السيادة  https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/naya_foriraq/92495" target="_blank">📅 16:38 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92494">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🇾🇪
🇾🇪
القوات المسلحة اليمنية
:
بسمِ اللهِ الرحمنِ الرحيمِ
قالَ تعالى: {فَمَنِ اعْتَدَى عَلَيْكُمْ فَاعْتَدُوا عَلَيْهِ بِمِثْلِ مَا اعْتَدَى عَلَيْكُمْ} صدقَ اللهُ العظيم
يواصلُ العدوُّ السعوديُّ المجرمُ عدوانَه الظالمَ على شعبِنا بشنِّه المزيدَ من الغاراتِ العدوانيةِ والتي بلغت خلالَ 12 ساعةً الماضيةَ 50 غارةً جويةً وصاروخًا استهدفَ بها العاصمةَ صنعاءَ والمحافظاتِ الجوفَ وتعزَ وعمرانَ وحجةَ وصعدةَ
ليبلغَ إجمالي غاراتِه العدوانيةِ على شعبِنا منذُ بدءِ التصعيدِ 1460 غارةً جويةً وصاروخًا.
وفي إطارِ الردِّ على هذا العدوانِ نفذتِ القواتُ المسلحةُ اليمنيةُ بعونِ اللهِ عمليتينِ عسكريتينِ نوعيتينِ بعددٍ من الصواريخِ الباليستيةِ والطائراتِ المسيرةِ.
الأولى استهدفت شركةَ أرامكو في عاصمةِ العدوِّ السعوديِّ الرياضِ.
والأخرى استهدفت شركةَ أرامكو في منطقةِ خريصَ.
وقد حققتِ العمليتانِ أهدافَهما بنجاحٍ بفضلِ اللهِ تعالى وكانتِ الإصاباتُ دقيقةً بفضلِ اللهِ وتسببت بنشوبِ حرائقَ كبيرةٍ في المواقعِ المستهدفةِ.
ستواصلُ القواتُ المسلحةُ دكَّ قواعدِ العدوِّ السعوديِّ المجرمِ ومنشآتِه النفطيةِ بالصواريخِ والمسيراتِ اليمانيةِ الصنعِ والتي أثبتت قدرَتَها على إصابةِ الأهدافِ بدقةٍ ونجاحَها في اختراقِ منظوماتِ التصدي والاعتراضِ الغربيةِ ولن تتوقفَ القواتُ المسلحةُ عن تنفيذِ المزيدِ من العملياتِ المؤلمةِ للعدوِّ السعوديِّ وفي استهدافِ تحشيداتِه وتثبيتِ معادلةِ الحصارِ بالحصارِ والتصعيدِ بالتصعيدِ حتى وقفِ العدوانِ وإنهاءِ الحصارِ عن بلدِنا العزيزِ.
واللهُ حسبُنا ونعمَ الوكيلُ، نعمَ المولى ونعمَ النصيرُ.
عاشَ اليمنُ حراً عزيزاً مستقلاً،
والنصرُ لليمنِ ولكلِّ أحرارِ الأمةِ.
صنعاءُ، 23 ربيع الثاني 1448هـ
الموافقُ 4 أكتوبر 2026م.
صادرٌ عنِ القواتِ المسلحةِ اليمنيةِ</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/naya_foriraq/92494" target="_blank">📅 16:31 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92493">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🇾🇪
🇾🇪
القوات المسلحة اليمنية:
تمكنت قواتنا المسلحة _بفضل الله تعالى_ من طرد واستهداف تحشيدات العدو السعودي من شرقي الجوف إثر محاولات فاشلة للتقدم باتجاه مواقع قواتنا المسلحة ونتج عن عملية الاستهداف والطرد ما يلي:
-إحراق عدد كبير من الآليات التابعة لتحشيدات العدو السعودي.
-مصرع وإصابة العشرات من تلك التحشيدات.
-ملاحقة ومطاردة من تبقى منهم في صحراء الجوف.
-استهداف تجمعات تلك التحشيدات بعدد من الصواريخ الباليستية والطائرات المسيّرة.
​التحية لأبناء الجوف ومأرب وهم يقفون موقف الحق مع شعبهم وبلدهم، يقفون إلى جانب قواتهم المسلحة في التصدي الفعال والمؤثر للعدو فأفشلوا _بعون الله_ تحركاته وكسروا بفضل الله زحوفاته فهزموا أدواته ونكلوا بعملائه وأسقطوا خططه وأهدافه ودفنوا في الصحارى والأودية أحلامه وطموحاته وأمانيه .. وهذا هو اليمن الحر العزيز.</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/naya_foriraq/92493" target="_blank">📅 15:40 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92492">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">في خبر غير مهم
رئيس مرتزقة السعودية:
أعلن بدء العمليات العسكرية لاستعادة ما تبقى من أراضي الجمهورية وبسط سلطة الدولة
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/naya_foriraq/92492" target="_blank">📅 15:36 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92491">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">‏مصادر يمنية: الحوثيون سيطروا على منزل رئيس البرلمان اليمني سلطان البركاني جنوبي تعز بعد اشتباكات مع القوات الحكومية</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/naya_foriraq/92491" target="_blank">📅 15:34 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92490">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🇮🇱
اعلام العدو:
جبهة اليمن على جدول أعمال الكابينت اليوم
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/naya_foriraq/92490" target="_blank">📅 15:30 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92489">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🇾🇪
وكالة الانباء الفرنسية: عناصر أنصار الله يقطعون طريقاً رئيساً لمدينة تعز ويحاصرونها  https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/naya_foriraq/92489" target="_blank">📅 15:11 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92488">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🇾🇪
وكالة الانباء الفرنسية:
عناصر أنصار الله يقطعون طريقاً رئيساً لمدينة تعز ويحاصرونها
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/naya_foriraq/92488" target="_blank">📅 15:08 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92487">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🇮🇶
رئيس الوزراء العراقي يأمر بتشكيل لجنة تحقيقية بشأن التجاوز على علم الولايات المتحدة خلال يوم السيادة
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/naya_foriraq/92487" target="_blank">📅 14:39 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92486">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">انصار الله يسيطرون على سوق المركز ويستمرون في التقدم باتجاة التربة في تعز</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/naya_foriraq/92486" target="_blank">📅 14:15 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92485">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XNsgZ5zFTc7vybnHstNPX_m3ZIqET8Pj0KfJUBiteL0Omwpkco_qDCetQzywlV4sD_toSnu7bZUF2pLbQugFcekVJLBIb8t-NMmRdtYMJIystTMOTwQ7jmRlQwUdEMYTXSWSsE-OXtVyyqOWQlPX9zASg4FTopJFVPNmq4AYC5z7mrZdzMj5AkPaOM15BsnEMkSN0ME0kZUgJ8ancn2V5FmPiD7AbdghSpbQCvQlBqnrn-vF5JRKpbGX2v6bg4lYOU7Gm9Dg21yHl7zw5r4o19yHVsY4V9k1Wu9nWWW5Ky6EpHB4WN5IIw6A_bCfj4Ilz1BtjDZNzK4herbys2aEgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
🇮🇱
غضب في الشارع العراقي بسبب غزو المنتجات الصهيونية للاسواق العراقية عن طريق الاردن.
العراق كان قد اعفى الاردن من ادخال نحو 399 منتج من الكمارك وهو رقم هائل اكبر مما تستطيع الاردن انتاجه الامر الذي سمح للكيان الصهيوني بادخال منتجاته الى العراق عن طريق الاردن.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/naya_foriraq/92485" target="_blank">📅 14:06 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92484">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b3fa96286.mp4?token=RNsh9wuU7oPWVF7AY12lfV2Vp_R5-JUSJOCEvGdSWIRMRsSdsR6DSf1wGnZMQvntoVxb0NY_NI19wRZem2uMIVApP0ubC8cuy2dQhktrihVIPF_ujQIoHXzviA-OqVhCEN-WM0nWuQbmPiLqy24UZojvBtRGN1c3481RwxQYbBpgJJWh8RDMLXH7l0MHYbRCYXSkaMuJn54K1JwZfFQoKRucIwd349uDRqUBAk4FUgfrIahNmSjd2mJM1AFVCMdd3ZPAYhkFoAdRzWNQevEPNY8bR5foYzANsiEfvo8NgUca-1zQIK2VPejjShe2V-QCtCYusoK3MXB69gZHFHuUIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b3fa96286.mp4?token=RNsh9wuU7oPWVF7AY12lfV2Vp_R5-JUSJOCEvGdSWIRMRsSdsR6DSf1wGnZMQvntoVxb0NY_NI19wRZem2uMIVApP0ubC8cuy2dQhktrihVIPF_ujQIoHXzviA-OqVhCEN-WM0nWuQbmPiLqy24UZojvBtRGN1c3481RwxQYbBpgJJWh8RDMLXH7l0MHYbRCYXSkaMuJn54K1JwZfFQoKRucIwd349uDRqUBAk4FUgfrIahNmSjd2mJM1AFVCMdd3ZPAYhkFoAdRzWNQevEPNY8bR5foYzANsiEfvo8NgUca-1zQIK2VPejjShe2V-QCtCYusoK3MXB69gZHFHuUIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏مصادر يمنية: الحوثيون سيطروا على منزل رئيس البرلمان اليمني سلطان البركاني جنوبي تعز بعد اشتباكات مع القوات الحكومية</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/naya_foriraq/92484" target="_blank">📅 13:51 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92482">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">‏مصادر يمنية: الحوثيون سيطروا على منزل رئيس البرلمان اليمني سلطان البركاني جنوبي تعز بعد اشتباكات مع القوات الحكومية</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/naya_foriraq/92482" target="_blank">📅 13:43 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92481">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rKShszTQRss8m0Ab-7CVCngr2PMzpNNLO-s8UHzOhBn_9JN6plegcxGIslycqv_43AO0iOCKQ1KClDJk2VnoJlW1HA8GrDYzIzvlyWjhwV1kUDlb65NjVWwuOPFYOd6LwKOctQ8NWy5F9HIAfZzNJhrdKtPFJNfJFE7YJvNQ0lDTa2xKlk4ul1sn6PdaRehb2db0hjO8T0Mauzb8Dm38JMgfhuejp6iJhWwNi6VUA_8TZVNFmsOre6_WlcrIR_eLmVbMn3uI1L3RW9YAtrIqerac8FF6KH49BTLF36lXHgt-NiuqeBdlb0KFV6e5OANqsCd1n8AyK8NtWpqO2WbiZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
بعد أن أغلقت نتيجة الإقتحام..
القائم بالأعمال السويدي يعلن توجه حكومة بلاده نحو إعادة فتح سفارتها في بغداد.</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/naya_foriraq/92481" target="_blank">📅 13:16 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92478">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hDBDTh1o-HLIWWoBuQuOvk7jRXKdyiHBNCBFeqNNlvAwEYO2mdrZ-zIudKRhq2IVHhWt_4vAxYGREvEKSdtCPgearkvxtF56xWmyRnl9_2b5m2G15Q0hpba9h_E7pyJcODUjAu1geOkIMh3yMM-9EBM0ZbUpk-IesSxO9Nca8FO-CsOWztwL7xvabyI3q2gMACwif_PFdjEqeohr5ibOrRL6J8jUzPEimFAUYb2C8i9y3El9et2cJH8e-Qwu_MtIGRHp8RehqI0I27ddfShE35hjJz-lYAay7E2Vq0g0BLO9bt7eYGdwu2yDGyjOLoki5AoXFnybnsDq39DCaPYqEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dvuE0rqzGCb6Q5duoeOcRXNnEv8IjQgiqNBTTAGxo-ovsy6eKn7w1S6eqW9trY_KQ1vAtatmc_qX0JNC259YeBiBpyslFL3r-YHic3VzR2Wtv3G3MvJfcFWOr1bWc8UC9QXDD0LZieYxntNE4nZVUKZ88XBeTfr6JgEH9i6HO0snaSth_Mw7wTrUW4no2xUxvLo0mcV0y2IVYv0QK8QukGOMdX61jzFdi9rzroWMjFR3vMtBDRp_i19LUzzuiKwx3yVCB-zE4vUynFnDcr9cDlB7DCps_E3nFq6jAV35zio3azuCFm9UlQRuiSdrsP23LMfk_jdsbt7jMK1dZGR5fQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GoGbDKtRCHRBUPw-gl_DzIUUZ4zLwSLjBVMWcFDdfbejP46mrQ1z5A_5FBGAct5-iRoS_Y0NXKbnkO1I4qr2vgA5ipmQmo4DyJTC3p6AfH3LDcYEj-epzNO3Hu8w1tz8THJ77IwZvBxbdjZPySijMlOOgdmq7s_RSKaUgdju0K4TUxT0qsUCvZxqHehWl9_U-30jStxzXMcRB4ob8kwO8vD47gk7losADmcsUiK_p9EIqTHwvuhlLYHmKvfV4JijxuzDelDVdLBzbewe4mCjrwgGHVTlr_Yty_9DgHpbDMcA1QbuExvXLV-0WkgXTzQamsABmYCbZOPUjywoymrXmA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇮🇶
من إنفجار العبوة الناسفة التي طالت عجلة تابعة للجيش العراقي في صحراء راوة جنوبي محافظة الموصل؛ حيث أدى ذلك لإستشهاد وإصابة 4 منتسبين من الجيش العراقي.</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/naya_foriraq/92478" target="_blank">📅 13:04 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92477">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🇸🇦
توقف العمليات الجوية في مطار الطائف الدولي بالسعودية.</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/naya_foriraq/92477" target="_blank">📅 13:00 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92476">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🇮🇱
عملية دهس في القدس المحتلة؛ مقتل مستوطنة كحصيلة أولية.</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/naya_foriraq/92476" target="_blank">📅 12:22 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92475">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🇮🇶
🇮🇷
مطار النجف الأشرف يعلن استئناف عدد من الرحلات الإيرانية.</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/naya_foriraq/92475" target="_blank">📅 11:58 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92474">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0012925a86.mp4?token=af1LBbNnAaG02Hx9d6hn2GxqP2khRJ7FMZGsA2hwZBYvo3KNDtn0IWIfsJ5nw0Le9FS7v1E2QHSqkKw20onSG4tifmTi6w3YDaSarigsNCRdN__TXd2nH1KRX1mJqZv0czwVIM9j5CPemsRwaAy-X_xM5q24S58jiFW47eURy0RvHciQ3GyP0hf5LV6aAAeSltahQpBVQpOpcdXrrncK1QhNuxf-7lnArGZ5Bye5wmXYq9K40qSHCQZRyOoealA1uVDnP2Aa0bpqH8r9b4I_I1kIQ0aF08yHNYQS1TxWcc35vUk9qx_xd8cbcZ0tz9AJi1pIEHPJkqYi-swXyN5ZaDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0012925a86.mp4?token=af1LBbNnAaG02Hx9d6hn2GxqP2khRJ7FMZGsA2hwZBYvo3KNDtn0IWIfsJ5nw0Le9FS7v1E2QHSqkKw20onSG4tifmTi6w3YDaSarigsNCRdN__TXd2nH1KRX1mJqZv0czwVIM9j5CPemsRwaAy-X_xM5q24S58jiFW47eURy0RvHciQ3GyP0hf5LV6aAAeSltahQpBVQpOpcdXrrncK1QhNuxf-7lnArGZ5Bye5wmXYq9K40qSHCQZRyOoealA1uVDnP2Aa0bpqH8r9b4I_I1kIQ0aF08yHNYQS1TxWcc35vUk9qx_xd8cbcZ0tz9AJi1pIEHPJkqYi-swXyN5ZaDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇷🇺
🇺🇦
إنفجارات وتصاعد أعمدة الدخان في العاصمة الأوكرانية كييف عقب هجوم روسي.</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/naya_foriraq/92474" target="_blank">📅 11:45 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92473">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MYEduEDLuTV4eHAMx_vMeowMzAvvKC1oMr_wtdBhAC4tPSLwViJ6DFPtajig5m1G3-eiGzNx1ehbnJeBBhDUsL-YxgAZ52NdOnzCS79JhX7PkpaWP5ZSlp0zIKTCivAOBl-4JZUKVg8puZJHklnFdkS4a1MXf-NKUMGceMI_y8oQEb7lLfByQWveHtnTP2aIKg-LIwHBpI-CpgCrX1PwDqhqfZFBaNFDJMw5lCSwsOUABW2jOliq73SDkRQ4OzB9g2Xlo27aYwJKb--fdatYE36Xw4Eh7jOmD6WqWPxOk3GcnSO0iR6sTtosvLSdEKJNBEvfOwaBq6DEzHnb7LUDhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
الهيئة البحرية البريطانية:
ناقلة نفط أبلغت عن تعرضها لمقذوف مجهول بمضيق هرمز ألحق أضرارا بغرفة المحركات.</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/naya_foriraq/92473" target="_blank">📅 11:19 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92472">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FqoTBbctfAJrs22_nEPvBKMMsE4wF2IJL69AIHGBopXArfgsqyfE4BKPqt6X83asDdhk1-56q86tmpJtaEwrA5iBa5xzv6VWV8qno2akhL7LB0CaOJhDq-jz1UAdNqohkkcB-5z1GA-f3etkJfNnIyxcYZPbzzpqxtnMNfHOe8bDlcOLuJTUcrOtjETyNNzdBHOYa-cFRxzVgzFzUVCOlxx5ABU2lu9euBoKAz6tM1_D0ln3Tk2uhx2_xe4ExqtcrMnwG-eS8c1r86uj9kYdKIPmmiFaNya4Brx-IC2-0GMJyaZlgQ5___d5IMMBIrm8VFGPGrHTrkp1XArae0uQwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▫️
‏الكويت تقرر سحب الجنسية الكويتية من 415 شخصاً وممن اكتسبها معهم عن طريق التبعية  عيل منو بقى بالكويت</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/naya_foriraq/92472" target="_blank">📅 11:14 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92471">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🇸🇦
🇾🇪
توثيق من نقطة قريبة لمخازن النفط المشتعلة داخل مصفاة أرامكو بالعاصمة السعودية الرياض جراء دكها بالصواريخ والمسيرات الإنقضاضية اليمنية.</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/naya_foriraq/92471" target="_blank">📅 10:52 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92470">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">النظام السعودي يواصل عملية اخماد الحرائق</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/naya_foriraq/92470" target="_blank">📅 10:45 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92469">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🔻
أوبك بلاس تتوصل إلى اتفاق مبدئي للإبقاء على أهداف إنتاج النفط دون تغيير في نوفمبر المقبل.</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/naya_foriraq/92469" target="_blank">📅 10:19 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92468">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OIVsZS-pIkVKWnb08RwWN6A8VzwDItfOIVmhHIouqkOAumKss-U0IkAhXuFdBqAwGUU7xvsCEkdHM9Z-gmE3g-J-dpDIqhBqUsfKNQhOMuqrpqfjWDYg3_hJsPZ5ORVSdq7H09j7o3VuxT8fesje-NQD6QZSdaJs5gRepjVN0nh9aQT4P4YA63SQ5nVeIQrnW_CJDYPm6b8NwaSX_J0JctiMrDii2G7zFuQ9j8DjlUJC2S0hzUMVwz9hpCwdlrPFkBShko7n_ktCuB7TfUAMyOlMaPm5wzJZDUngqm_9PxUZg4bG-eNA0aW7qw0gwz1YsnsLnzcLGDTVIByu0WPoKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇷🇺
🇺🇦
إنفجارات وتصاعد أعمدة الدخان في العاصمة الأوكرانية كييف عقب هجوم روسي.</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/naya_foriraq/92468" target="_blank">📅 09:56 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92467">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa57f09733.mp4?token=rTm7fSzXQm6IaJ-w1poKkDKIflQmcrmPh_ZJYjepmSWcpim7FoyFv7LiuKiCuX_v5ejop_kuI-qgrB-NTffN6eXy9ak4AUa4K_5tkWQmJJLQpTzAAFv11VmFrNICM4FnetjUGwEt7s6INodv1Pt9Gd1a9NcLZHZ6qNn4EyCua-UXR_kzfx3g3VsZ1gaVuavE1uMHk2C1vFx6KlHAbOyHdJ1SZUl6DfOoK8jC-RpVLc0cGi8kKgVhpOiYZbKH2s5qbk3b8SN0gsiZJ2d4rU1xGhf_kzI3yuniVwiFUzBrqQ1qvIMciJowpw_sFjmXzcb63iTnEv6i8ijvK9ro5g0p5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa57f09733.mp4?token=rTm7fSzXQm6IaJ-w1poKkDKIflQmcrmPh_ZJYjepmSWcpim7FoyFv7LiuKiCuX_v5ejop_kuI-qgrB-NTffN6eXy9ak4AUa4K_5tkWQmJJLQpTzAAFv11VmFrNICM4FnetjUGwEt7s6INodv1Pt9Gd1a9NcLZHZ6qNn4EyCua-UXR_kzfx3g3VsZ1gaVuavE1uMHk2C1vFx6KlHAbOyHdJ1SZUl6DfOoK8jC-RpVLc0cGi8kKgVhpOiYZbKH2s5qbk3b8SN0gsiZJ2d4rU1xGhf_kzI3yuniVwiFUzBrqQ1qvIMciJowpw_sFjmXzcb63iTnEv6i8ijvK9ro5g0p5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
رئيس البرلمان الإيراني محمدباقر قاليباف:
الأمريكيون، الذين يتحدثون شيئًا مختلفًا في وسائل الإعلام، قد طرحوا مؤخرًا مقترحات من خلال وسيط. ولكن يجب أن يدركوا أن عصر إضاعة الوقت وإملاء المطالب من جانب واحد قد انتهى. وموقف الجمهورية الإسلامية الإيرانية واضح وثابت تمامًا. ولن يتم فتح مضيق هرمز إلا عندما يتم تحقيق الشروط السبعة التي وضعناها استنادًا إلى اتفاقية إسلام آباد.
بناءً على استراتيجية القوة والعقلانية، نحن لا ننفعِل ولا نُرهَب. نحن نقاتل ونتفاوض في الوقت نفسه. نحن موجودون بكل قوتنا في ساحة المعركة العسكرية وسنواجههم بمفاجآت جديدة، وفي الوقت نفسه، نستخدم أدوات الدبلوماسية لترسيخ تفوقنا في الساحة العسكرية وفرض حقوق الشعب الإيراني. لقد ذكرت مرارًا وتكرارًا أن الفائز في ساحة التفاوض هو من أعد نفسه للحرب.</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/naya_foriraq/92467" target="_blank">📅 09:36 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92466">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🇮🇶
🇮🇷
هزة أرضية بقوة 3.6 ريختر تضرب الحدود الشمالية بين العراق وإيران.</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/naya_foriraq/92466" target="_blank">📅 09:10 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92465">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zy2oJdp_xa36MD4yjLbdSKiM8CS34PAZd_PoFBNHCu8-2LjjTwfabb2U96k-lApsUZ-kJLTO0o2upINflh-bKjXSG1T-vxUiD2bheS2-Z4PN05MrjwZZR5pJPE1pfZ4ytdIiqWmuuaQJU_FnFsjxG2MIQmM563iooLJ1TYr0q_186Z0KfaqHW56nMqYVu_DY_fyJbg9irZnMEOn1j0cwiWWW4sDsSwPbDSAcaTab2oh-GGFPIGsm-qebmo_RFztIlnId2HmATIsZH4VbSUxoLPrDtB8dmBwwDy_8DY6cV9DBOZma6SnGpadYSuZr8D75KZycHkWL7Vcf5VOrJfVl7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
🇮🇶
النائب الامريكي جو ويلسون ينتفض
😆
:
شوهدت قوات الحشد الشعبي، وهي قسم رسمي من الأجهزة الأمنية للحكومة العراقية، وهي تدنس العلم الأمريكي بدافع عدم الاحترام وتمجيد النظام القاتل في إيران.</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/naya_foriraq/92465" target="_blank">📅 03:31 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92463">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">▫️
‏الكويت تقرر سحب الجنسية الكويتية من 415 شخصاً وممن اكتسبها معهم عن طريق التبعية
عيل منو بقى بالكويت</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/naya_foriraq/92463" target="_blank">📅 01:48 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92462">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SQwDGbdw7UAyZVx6DkfU2zTO9bWw9GG1Ow9XOOxP2mfjDPqSDH2z7EybJwkOhygvSJIRvUWq-3qEeUGytk2SciEMgn7nBTfPSI0nE3HahCs471uT0o7XdAWQkIKTEI6P_nTppmmiRSjqrIZy_u-FzeeSBzOF2hUNMmSeDET6ULyzeLdKenWCv4pD4kPrUgqkGsKE5I2fckBgBD747gN8WfZyiiUghgDl222OBSTxoRJfsODWB2GJYsEfPAsn_RSBm1z1_OQmLKrn51p6O7j8iqSLTtr_dCs8Bp3AvSDenqfZ4oVuV8krpJRrVQuekQZ9jgmVt3h2enaOONcpeHkAdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الرد اليمني وصل،هجوم صاروخي عكسي من اليمن يستهدف السعودية في ينبع واصابة عدد من  المواقع النفطية</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/naya_foriraq/92462" target="_blank">📅 01:28 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92461">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hnKAoEklZ2PyXaFXxNUwv7PEwIU96oNa8VOJLQnBAo1wopxoAJ2fRYTe-McwLciaGHxcPPAraXFKMkRb5Wn9vSX1JTUKDo3f8Fi0dwC-uHM-yIqePcxGKvD8Xf2QT7aWGGmfe8bU3qpy3UfNpBC9h-JO9EGLT2jDYtXFhMaZEFlwJbnSpe5hxYxaJXIX9LyXE9EBg3CM-Il8Kw9M0_BJwyqTMqY1RVZO8giX3KHwQCx2dRCQpREVSv8zQmuZpQnwBEd4WoWNJqZ3kgziP2PkqagDZLbw-dwnGlVNno-QdKJ3dtmwQvcksS0S3LZS0404wJckA93mI0wMuLja6vTttw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">القوات اليمنية المسلحة تستهدف الدمام شرق السعودية</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/naya_foriraq/92461" target="_blank">📅 01:15 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92460">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">القوات اليمنية المسلحة تستهدف الدمام شرق السعودية</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/naya_foriraq/92460" target="_blank">📅 01:06 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92459">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HP9-7RMjFgiQS18uJRlVFZ72ZwDMcC7FatSrTnVBqQ4j0XltGgcpoYXjATzvjz_vQ-oplAFSYSJE4eJY3Q4GLwlSaDDaAU2LxDlso8WzTH_7wQN8HjNsV_ZgJbwj4QbNoTRlDi15PhcytLoAVvjUBD3XzmewApTcJmX0rDt4pw6nUYL31QR48uJectWyOpmDam8J5sf63zHDh7dgWzxoRxUf2Dj3hsfecvaLDx-Xaoxmu8Xj-mcTFnG6NmRxiJbT6CGWvo6-uovM6KuLrvgPLcYDtVBaUCMhYcarupXjtSu23D4yRtyYze-jjLjR2pgQt3rmt-VpUJAYpvd4n5skyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
تداول ناشطون على مواقع التواصل الاجتماعي وثيقة تشير بمؤشرات امنية خطرة تخص والد مرشح حقيبة وزارة التخطيط و تؤكد انتماء الأخير لعصابات داعش الارهابية</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/naya_foriraq/92459" target="_blank">📅 00:43 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92458">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🇸🇦
🇾🇪
غارات سعودية تستهدف محافظة عمران والعاصمة صنعاء</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/naya_foriraq/92458" target="_blank">📅 00:43 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92457">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ab78e7a2b6.mp4?token=lDNanNd18TVyHx_cccRYzEqU_V4jjuOjWfjs9YNOuiBkRIps-YAMhNN0mqswig79Qi94hm-1aSTASjyRaPz2trOrTFwbBBdZVVNwYRkDzvpHnxrrsyQzJLN-K5sfi-3CgzSrz1Xj7io3l1GG2pewej1xJyyv82phZQDHI3PtwAtXWoRDKqxfEQ5npaBlQT7AmhBEUrwPxb_74V4dzvK2B4Ynl5Ar3wbqj3_e5Q2cpvl-FlJg0ER3KYQp9bU3_-zHiq8_FqQQxWmPAV6ag4RZYTFEEUxLg5gHzLEch-2jlA2o_OjzJkbtQQmobTqb-muUk6NN_6KtUcRR6zRrljn-yQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ab78e7a2b6.mp4?token=lDNanNd18TVyHx_cccRYzEqU_V4jjuOjWfjs9YNOuiBkRIps-YAMhNN0mqswig79Qi94hm-1aSTASjyRaPz2trOrTFwbBBdZVVNwYRkDzvpHnxrrsyQzJLN-K5sfi-3CgzSrz1Xj7io3l1GG2pewej1xJyyv82phZQDHI3PtwAtXWoRDKqxfEQ5npaBlQT7AmhBEUrwPxb_74V4dzvK2B4Ynl5Ar3wbqj3_e5Q2cpvl-FlJg0ER3KYQp9bU3_-zHiq8_FqQQxWmPAV6ag4RZYTFEEUxLg5gHzLEch-2jlA2o_OjzJkbtQQmobTqb-muUk6NN_6KtUcRR6zRrljn-yQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏ترامب: لدي قرار سأتخذه بشأن إيران. وسنتخذه بالطريقة السهلة أو الصعبة.
‏-لا يمكن لإيران أن تمتلك سلاحاً نووياً. بالمناسبة، كما تعلمون، تخلت إيران فعلياً عن أي خطط لامتلاك سلاح نووي.</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/naya_foriraq/92457" target="_blank">📅 00:37 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92456">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🇷🇺
🔻
خوفا من مسيرات روسيا
‏تقوم ولاية مكلنبورغ-فوربومرن الألمانية ببناء شبكة للكشف عن الطائرات بدون طيار على طول ساحل بحر البلطيق بأكمله، حيث من المقرر أن توفر مئات أجهزة الاستشعار السلبية بيانات في الوقت الفعلي للسلطات بحلول الربيع</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/naya_foriraq/92456" target="_blank">📅 00:09 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92455">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالإعلام الحربي</strong></div>
<div class="tg-text">🔴
الرصد اليومي لطلعات العدو الجوية التي يخرق بها السيادة العراقية.</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/naya_foriraq/92455" target="_blank">📅 23:46 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92454">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🇾🇪
بيان القوات المسلحة اليمنية بشأن تنفيذ عملية عسكرية نوعية استهدفت شركة أرامكو في عاصمة العدو السعودي الرياض وأدت إلى اشتعال النيران في المواقع المستهدفة   بيانٌ صادرٌ عن القواتِ المسلحةِ اليمنيةِ  بسمِ اللهِ الرحمنِ الرحيمِ قالَ تعالى: {فَمَنِ اعْتَدَى عَلَيْكُمْ…</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/naya_foriraq/92454" target="_blank">📅 23:35 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92453">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🇸🇦
تعليق الدراسة غداً الأحد في جيزان خوفا من هجمات القوات المسلحة اليمنية.</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/naya_foriraq/92453" target="_blank">📅 23:22 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92452">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🇺🇸
🇮🇷
الاعلام الاميركي:
طرد دبلوماسيين إيرانيين من الولايات المتحدة بعد تجاهلهما أمر المغادرة.</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/naya_foriraq/92452" target="_blank">📅 23:04 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92451">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LjfoaLyUpULWISLPElz4N1kErVkR4q2YVmqhczat46cUpxnakOycvhO37g8OBDBpnWivvL9oGZ7g93eetME3xoA--rsEb67_DcKPHbf6XohcBtWD70ZWIX1_LcMsfg_pCoRPjBufhKKavBLWWIrKtRv_BGaZWimEUFiCfewdt_qdT3SlgynysTG6l2dunUXcax-VRu_0jr04izHBwJjvi_uCIzz4UyFWtrxPii3UcRPHF3V-GyybtKvQ1tFV_LcFjU1AKF69TiE7jNenbXfQY_Ar30_7o11ImbTUCE5ghVhj4R8JR74F9oOdRC6RWNjFsYU-QERqT8S7-h8cbeduKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
الرئيس الايراني: ‏
اتخذت الحكومة نهجاً جديداً في إدارة هذه الظروف الاستثنائية. تمثلت خطة العدو في الأشهر الأخيرة في قطع شرايين البلاد الحيوية بهدف الضغط على الشعب الإيراني الكريم. وقد ازداد الضغط الاقتصادي، ولكن بفضل الله، وبدعم من الشعب، وبجهود زملائنا في الحكومة، لم نسمح للعدو بتحقيق أهدافه في الحرب الاقتصادية.</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/naya_foriraq/92451" target="_blank">📅 22:53 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92449">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🇾🇪
بيان القوات المسلحة اليمنية بشأن تنفيذ عملية عسكرية نوعية استهدفت شركة أرامكو في عاصمة العدو السعودي الرياض وأدت إلى اشتعال النيران في المواقع المستهدفة
بيانٌ صادرٌ عن القواتِ المسلحةِ اليمنيةِ
بسمِ اللهِ الرحمنِ الرحيمِ
قالَ تعالى: {فَمَنِ اعْتَدَى عَلَيْكُمْ فَاعْتَدُوا عَلَيْهِ بِمِثْلِ مَا اعْتَدَى عَلَيْكُمْ} صدقَ اللهُ العظيم
في إطارِ الردِّ على العدوانِ السعوديِّ على العاصمةِ صنعاءَ والمحافظاتِ الحرةِ والتي بلغت خلال 24 ساعة الماضية 60 غارة جوية وصاروخ ليبلغ إجمالي غارات العدوان السعودي منذ بدء التصعيد على بلدِنا 1410 غارة وصاروخ
نفذتِ القواتُ المسلحةُ اليمنيةُ عمليةً عسكريةً نوعيةً وذلك بعددٍ من الصواريخِ الباليستيةِ والطائراتِ المسيرةِ استهدفت شركةَ أرامكو في عاصمةِ العدوِّ السعوديِّ الرياضِ.
​وحققتِ العمليةُ هدفَها بنجاحٍ بفضلِ اللهِ
وكانتِ الإصاباتُ دقيقةً ومباشرةً وأدت إلى اشتعالِ النيرانِ في المواقعِ المستهدفةِ.
​إنَّ سفكَ دماءِ اليمنيينَ بهذا الإجرامِ وبهذه الوحشيةِ يُحَتِّمُ على القواتِ المسلحةِ ومعها كلُّ أحرارِ شعبِنا ضرورةَ اتخاذِ ما يلزمُ من خطواتٍ تصعيديةٍ وإجراءاتٍ رادعةٍ تؤكدُ للجميعِ أنَّ ثمنَ الاستهتارِ بدماءِ شعبِنا المؤمنِ سيكونُ كبيرًا وباهظًا وليدركَ العدوُّ المجرمُ أنَّ الاستمرارَ في سفكِ دماءِ شعبِنا سيكلفُه الكثيرَ.
مستمرونَ في فرضِ معادلةِ الحصارِ بالحصارِ والتصعيدِ بالتصعيدِ واستهدافِ التحشيداتِ التابعةِ للعدوِّ السعوديِّ حتى وقفِ العدوانِ وإنهاءِ الحصارِ عن بلدِنا العزيزِ
واللهُ حسبُنا ونعمَ الوكيلُ، نعمَ المولى ونعمَ النصيرُ.
عاشَ اليمنُ حراً عزيزاً مستقلاً،
والنصرُ لليمنِ ولكلِّ أحرارِ الأمةِ.
صنعاءُ، 22 ربيع الثاني 1448هـ
الموافقُ 3 أكتوبر 2026م.
صادرٌ عنِ القواتِ المسلحةِ اليمنيةِ</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/naya_foriraq/92449" target="_blank">📅 22:20 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92448">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🇮🇶
شركة ناقلات النفط العراقية:
تنفيذ عملية نقل مليوني برميل من النفط الخام العراقي بواسطة ناقلة عملاقة من نوع (VLCC) إلى خارج مضيق هرمز.</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/naya_foriraq/92448" target="_blank">📅 22:08 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92447">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromنايا احتياط</strong></div>
<div class="tg-text">🇮🇶
🇬🇧
العثور على جثة موظف هندي يعمل في شركة النفط البريطانية BP داخل أحد الفنادق في محافظة كركوك شمالي العراق.</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/naya_foriraq/92447" target="_blank">📅 21:13 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92446">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67e7e6594e.mp4?token=ct1fUcd3j8in0q-p5vkhKu-frKysX95n6g3Ct4-1hU7B4t-zU2-imV_PQVOS_GSZ73On7ySgTYfAciy3z2z1DcftOTfXEcrh38kXJ9FARsBXuoOQQ8Or33zJX6JXf0BmYAgn9_68BcuBuoyRdqWwMMYFG8XTMvh2V58ETc8IUlmJGJrxgD_MzYGmKx0FFUlEjH6Y27HgMNUeV4FkYtWpIScq0H-6z1XwAtswOjO1P25PCMXOoNj-_tcXMoyY5HRj7QNDMLX_Iwg6BMEDebmeSXdHIbbmuLUmXbzHGkUOvp0FWp_r553u0Fu5RigxXW_SUOSygersYaL8IEIVhcpMAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67e7e6594e.mp4?token=ct1fUcd3j8in0q-p5vkhKu-frKysX95n6g3Ct4-1hU7B4t-zU2-imV_PQVOS_GSZ73On7ySgTYfAciy3z2z1DcftOTfXEcrh38kXJ9FARsBXuoOQQ8Or33zJX6JXf0BmYAgn9_68BcuBuoyRdqWwMMYFG8XTMvh2V58ETc8IUlmJGJrxgD_MzYGmKx0FFUlEjH6Y27HgMNUeV4FkYtWpIScq0H-6z1XwAtswOjO1P25PCMXOoNj-_tcXMoyY5HRj7QNDMLX_Iwg6BMEDebmeSXdHIbbmuLUmXbzHGkUOvp0FWp_r553u0Fu5RigxXW_SUOSygersYaL8IEIVhcpMAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇱
حريق كبير مجهول في حيفا المحتلة بالكيان الصهيوني.</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/naya_foriraq/92446" target="_blank">📅 21:12 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92445">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h7Oud6JUbaBns3_3M1gpoM3HEm6qiFOfWb3lzd5YuoZhNK5foaTM-5KM9ckOZPPykKt5kmjlPp-Fwa8s0NlKygvNNfwWNYnXZZNmWvVKuF_d3wgxgJGzkc21gEIAaGpXlaff6KKZ9PJFe3tGBZeadtgJlPD2qBqNRwOYCAPRHTd5NEYhAZ0xvHnwZK6Q7kboExg0FC_V8l3RXkyi70cE4D9pU3UQFp093d2mNivkkLnGBmD8x29LN9fuwoSslAU5a_RuDBwcF1wZHNDtPZsC77kPhbnQ6bbrFkI8BUFSl7yz_06Axno59AwlmN6NgfKmcnKxYIi9ANNwB73VYCLQxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
رئيس منظمة الطيران المدني الايراني: ستأنف رحلات الطيران بين إيران والعراق اعتبارًا من الغد، وذلك من خلال شركات الطيران الإيرانية والعراقية.</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/naya_foriraq/92445" target="_blank">📅 20:39 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92444">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🇮🇷
رئيس منظمة الطيران المدني الايراني:
ستأنف رحلات الطيران بين إيران والعراق اعتبارًا من الغد، وذلك من خلال شركات الطيران الإيرانية والعراقية.</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/naya_foriraq/92444" target="_blank">📅 20:32 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92443">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🇾🇪
العميد يحيى السريع:
شن الطيران الحربي السعودي خلال الـ24 ساعة الماضية 60 غارةً جويةً وصاروخاً استهدف بها الأعيان المدنية في محافظات صنعاء وصعدة وتعز وحجة ومأرب وذلك من خلال طائرات "F-15" و "تايفون" أقلعت من قاعدتي خميس مشيط والطائف والعدوان الصاروخي من نجران.
ليبلغ إجمالي غارات العدوان السعودي منذ بدء التصعيد 1410 غارات جوية وصواريخ.</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/naya_foriraq/92443" target="_blank">📅 20:13 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92442">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🇬🇧
وزير دفاع بريطانيا:
سندرس الرد المناسب بعد التوصل لاستنتاجات مؤكدة في ما يتعلق بقاعدة فيرفورد.</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/naya_foriraq/92442" target="_blank">📅 19:54 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92441">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🇮🇷
انفجار ناقلة نفط ثانية في مضيق هرمز بعد استهدافها بصاروخ من قبل بحرية الحرس ااثوري.</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/naya_foriraq/92441" target="_blank">📅 19:14 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92440">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🇮🇱
مسؤول أمريكي:
إسرائيل حذرت ألمانيا من مخاطر على قواعد أمريكية خاصة قاعدتي سبانغدالم ورامشتاين.</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/naya_foriraq/92440" target="_blank">📅 19:12 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92439">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🇮🇶
رسائل تصل للمواطنين في العراق:
مشتركينا الاعزّاء، نظراً لتوجيهات وزارة الإتصالات، غداَ سيتم قطع خدمة الإنترنت من المصدر مؤقتاً خلال أوقات الإمتحانات الوزارية من الساعة 6:30 صباحاً إلى 7:05 صباحاً، علماً بأن التوجيهات تشمل جميع الشركات المزودة لخدمات الإنترنت.</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/naya_foriraq/92439" target="_blank">📅 18:31 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92438">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🇮🇶
اشتباکات مسلحة في قضاء كلار ضمن محافظة السليمانية شمالي العراق وإصابة عدة اشخاص كحصيلة اولية</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/naya_foriraq/92438" target="_blank">📅 18:12 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92437">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7f9b9a634d.mp4?token=j8VhKB37Jf7C6RCCViwg0AC_RiqfZIm9m2JsXDsvLZxiUy8QoHMtctr-1F01L3U1N9mhieAoqXWzNWZ4j9zjMxlTgzg0rQST_WBS75uj3XEtw1F1YOdVtmSV5zgcgrVPMTOfjE4WHEicwY0_PxVnkITftPI501Gwy8zvfOzWbmZTqOco-TwsVYebXZZbL7z5anom7zJuxPKiMznm4f1pPEKEHlmak9UiXIMjuAPbse9Lkh5E4lOqsTcIn6DV0ASFq8M6rKU3O2P-jjikZfmdOJnFrzqM1tWkeQbJPYcROnCSzPpg3qi1Mqk5Q-xgowVOHPYqqUgtRjlPpqDciDe61Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7f9b9a634d.mp4?token=j8VhKB37Jf7C6RCCViwg0AC_RiqfZIm9m2JsXDsvLZxiUy8QoHMtctr-1F01L3U1N9mhieAoqXWzNWZ4j9zjMxlTgzg0rQST_WBS75uj3XEtw1F1YOdVtmSV5zgcgrVPMTOfjE4WHEicwY0_PxVnkITftPI501Gwy8zvfOzWbmZTqOco-TwsVYebXZZbL7z5anom7zJuxPKiMznm4f1pPEKEHlmak9UiXIMjuAPbse9Lkh5E4lOqsTcIn6DV0ASFq8M6rKU3O2P-jjikZfmdOJnFrzqM1tWkeQbJPYcROnCSzPpg3qi1Mqk5Q-xgowVOHPYqqUgtRjlPpqDciDe61Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">النظام السعودي يبدأ باخماد الحرائق في الرياض الناجمة عن ضربات القوات المسلحة اليمنية</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/naya_foriraq/92437" target="_blank">📅 18:06 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92436">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ce85fd1ad6.mp4?token=NDhGdx_whbXJOTVZCUxDdPsl8b8QV414KG6-GuRsMlEVCVrwbQvleI70M0l0PvE4olT13BK9rW0gejA5F_63zLT-ghOj8F-L0fxZvqO89lb0z-dMN9yD_UXTLVYUJCvom9EJNXOJ6hsPOQWscEMR4ajY3BFDFhAZzk-7qJ6JkCEIMpBv1kL8kqLd22PDRh8c2T12LiANGjGyYzDjA8GLEMfNTcpWg_jC33EA-r0t4MonPcBsFOvy83WUFjiGa3Xj-2Tn6oUSLk3TlJU402dbVclmf3IcW0js9W0L4ShK3R1xqCVDpFEDLaaaBiXvcMIHfWydp2n_xFIKRcP8jKmCI7e7jiWEPNt0QM2_g5zZXn8jQ2q0us-gD6mZq4DZjCmJJ9_Bw2bX8R6eHXkEQtNlmCcnscemgCuwW8suItxjc_j9r3SjC5Tuhgh0-wq754Eor_Cnik96m3BECaR6l_W6UCDJJPyzso8wu4jcPpZSuBMI2uMuSnRoVlCG5hRmPQyoCP1pnTh60mViBBGF8Mi1mULkvgv7EoFXe2sFSoFQe3Mxhar0vKZHGZ87npL_JBGGLzBQWwz-dZi_gpu-M5KxABRQxAgAsCv36lfymvh_Z1uRmArMl_VyCTl7hVZ6mSiWbVe44Ww74EZcoyEjzEfJ9Mm7iy1XnkSUi-e50mEi8Mc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ce85fd1ad6.mp4?token=NDhGdx_whbXJOTVZCUxDdPsl8b8QV414KG6-GuRsMlEVCVrwbQvleI70M0l0PvE4olT13BK9rW0gejA5F_63zLT-ghOj8F-L0fxZvqO89lb0z-dMN9yD_UXTLVYUJCvom9EJNXOJ6hsPOQWscEMR4ajY3BFDFhAZzk-7qJ6JkCEIMpBv1kL8kqLd22PDRh8c2T12LiANGjGyYzDjA8GLEMfNTcpWg_jC33EA-r0t4MonPcBsFOvy83WUFjiGa3Xj-2Tn6oUSLk3TlJU402dbVclmf3IcW0js9W0L4ShK3R1xqCVDpFEDLaaaBiXvcMIHfWydp2n_xFIKRcP8jKmCI7e7jiWEPNt0QM2_g5zZXn8jQ2q0us-gD6mZq4DZjCmJJ9_Bw2bX8R6eHXkEQtNlmCcnscemgCuwW8suItxjc_j9r3SjC5Tuhgh0-wq754Eor_Cnik96m3BECaR6l_W6UCDJJPyzso8wu4jcPpZSuBMI2uMuSnRoVlCG5hRmPQyoCP1pnTh60mViBBGF8Mi1mULkvgv7EoFXe2sFSoFQe3Mxhar0vKZHGZ87npL_JBGGLzBQWwz-dZi_gpu-M5KxABRQxAgAsCv36lfymvh_Z1uRmArMl_VyCTl7hVZ6mSiWbVe44Ww74EZcoyEjzEfJ9Mm7iy1XnkSUi-e50mEi8Mc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">السحب السوداء تغطي العاصمة السعودية الرياض</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/naya_foriraq/92436" target="_blank">📅 18:05 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92435">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/564139a66e.mp4?token=ZcROwtFA_9JeBOIfMXmtgn10ApXD0Ds3jKr3nLne38UW7pIJhAzXmbHJVs6u7FHZmak8cBfEjlrtATDq8V72LpKAJm2_Xd5TtAhzkN9pWmIRBUNOMiuEVvEX5w37hImd6ZgJnv7wYgrEytOfFiq24kmSfBSoQEInbViy0-pwo9kaO48A9XwjxAPGqu52PlW3Cv2gNCFoV7sLQQ_RhYBJcVh9UvAPI12biOhGK5jHnqbTTfevERkbDQijg5s_4UqLHnwh8tGtx19IDnjSqDAHRk9wAdJW16AQ5gymOOMZDHfIrgCjG3IhKgZZZ-pF1QZbxFahNqHtWmbAE4gBbPpz9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/564139a66e.mp4?token=ZcROwtFA_9JeBOIfMXmtgn10ApXD0Ds3jKr3nLne38UW7pIJhAzXmbHJVs6u7FHZmak8cBfEjlrtATDq8V72LpKAJm2_Xd5TtAhzkN9pWmIRBUNOMiuEVvEX5w37hImd6ZgJnv7wYgrEytOfFiq24kmSfBSoQEInbViy0-pwo9kaO48A9XwjxAPGqu52PlW3Cv2gNCFoV7sLQQ_RhYBJcVh9UvAPI12biOhGK5jHnqbTTfevERkbDQijg5s_4UqLHnwh8tGtx19IDnjSqDAHRk9wAdJW16AQ5gymOOMZDHfIrgCjG3IhKgZZZ-pF1QZbxFahNqHtWmbAE4gBbPpz9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عودة الاحتجاجات في سوريا بسبب سوء الوضع المعيشي والمتظاهرين يقطعون الطرق لمنع صهاريج النفط من الخروج من دير الزور</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/naya_foriraq/92435" target="_blank">📅 17:57 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92434">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e7164999ac.mp4?token=VZUDdKGIbTorXUeV_CtwC4SFgxL7eqEIp82kN3sJYjFHwA-6pBmNi-Ic261Xtlia-hLiWutZAfE9tCCQ6QCAbVGj-eQDsrSwI5VJyvniWff_s6BAkbMzZXpptqpJN0o21joXeVikTWZhTN_OpGQ5nw_a0tXG-gX8xJAkCXa3eA0Dhe8PATVBziHHjmEsUPvZBngnmrkfb1YCGMNfbCwOvUJ4sAx3Xnvr6BeXxWeUtwvg8LXZOS0pTQmzj8coV_DcnXCbIgiM0ojrc9s_osjW1XyG-1nu-puCb_BdyVacDaXeZsnvODnpobZc0GD2bt2OStFOpn-bDLxr0yp8N-_FYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e7164999ac.mp4?token=VZUDdKGIbTorXUeV_CtwC4SFgxL7eqEIp82kN3sJYjFHwA-6pBmNi-Ic261Xtlia-hLiWutZAfE9tCCQ6QCAbVGj-eQDsrSwI5VJyvniWff_s6BAkbMzZXpptqpJN0o21joXeVikTWZhTN_OpGQ5nw_a0tXG-gX8xJAkCXa3eA0Dhe8PATVBziHHjmEsUPvZBngnmrkfb1YCGMNfbCwOvUJ4sAx3Xnvr6BeXxWeUtwvg8LXZOS0pTQmzj8coV_DcnXCbIgiM0ojrc9s_osjW1XyG-1nu-puCb_BdyVacDaXeZsnvODnpobZc0GD2bt2OStFOpn-bDLxr0yp8N-_FYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">القوات المسلحة اليمنية تدخل منطقة المساحين في مديرية الشمايتين بمحافظة تعز</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/naya_foriraq/92434" target="_blank">📅 17:31 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92433">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">إصابة شخصين نتيجة عدوان سعودي استهدف قسم الشرطة في مدينة صعدة اليمنية</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/naya_foriraq/92433" target="_blank">📅 17:04 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92432">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OX03tE0lGg69t_xtB_oZJaV0oKUSQbP0Yvr4UquY_EPBc0j_rFoCb5FQch41yBRYZI_RUrdVih28-DzcF6tCzjcnQPDNPpNzswVybS5zeVRNzW3NVXgNzTWw7SBi3su849zfd8pts82iEpZkaOzkwfxX2exEM-Z7D-7pLAxDvPAsVE035Us9iWePSh7IBOZ9YutDfiRWvH0GrQV7VbqibEwchAR-YZRgdWjJ45l8ts9NeBmLvhpB0rV2jN6voN0n7h_7Komd5hoQV-z2_E7w6hy7g5sP_wW3UxPbJR1QAgtpivx6IHw9hqE_lhHM2LDTSwnejx-zeB5LYOxZ8sL2uQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">العاصمة السعودية الرياض تحترق</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/naya_foriraq/92432" target="_blank">📅 16:49 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92431">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/567da1e998.mp4?token=dr5d_zKTvs30PpgSAMHRjTqG0gSAVRr9LkHqS1SFO0GrPQNHL_6jf9QoeFD5ofaByDOnAJo3UvSf6gA2x0HzxfvGePInbMkropDd1EVjgo71t9GDZxB00PoC1aDVxdGKBEGhlAqCccvv2RJMP4bE6wqbh94tN_ieR-tpNQ_rLOQPpFcDamaGSaznH_5Aem32MTK8enT6tOWxpLcG8DekxVSmCdpKLLAyvo3nsKYQaMA6LmwIHLf0xtcQP6bO9dZlb-m4q0oh1W4N1r1H4v6vWO-0djw8v55xvFl8ssTqVHfPIO_fOzk1VW3vE_OP1_Q0-lk5yn5li20HGH3HQ5WlZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/567da1e998.mp4?token=dr5d_zKTvs30PpgSAMHRjTqG0gSAVRr9LkHqS1SFO0GrPQNHL_6jf9QoeFD5ofaByDOnAJo3UvSf6gA2x0HzxfvGePInbMkropDd1EVjgo71t9GDZxB00PoC1aDVxdGKBEGhlAqCccvv2RJMP4bE6wqbh94tN_ieR-tpNQ_rLOQPpFcDamaGSaznH_5Aem32MTK8enT6tOWxpLcG8DekxVSmCdpKLLAyvo3nsKYQaMA6LmwIHLf0xtcQP6bO9dZlb-m4q0oh1W4N1r1H4v6vWO-0djw8v55xvFl8ssTqVHfPIO_fOzk1VW3vE_OP1_Q0-lk5yn5li20HGH3HQ5WlZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">منشأت ارامكو تحترق</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/naya_foriraq/92431" target="_blank">📅 16:45 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92430">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d52d0e3bdb.mp4?token=GxpnV4ptxwXJst8PCoBoA1tCA_RPuqFv6CYrWcCk0EXOhcfX8NPKvQ5L9fwNgM4d3ME4LQsKrljifJgNzh0sPVSe0VC2c2FAnSsYw1tuVMIHeFhO7z5ebw5TtkNWh61wukUMGaWe5uZRePRpO-Ki6s_3HhGYOBfg9sHq3WkCsgPeg_2i7fjfF21GcO6rDRLRNg8dozs3L_uwkCnRybkrwDrcneCf0xCl_CK2P8FkBSg1U9jKqGb_woFnEwHiW5SsTWiQ6zOjmM2yLlRLPgmWuxAxGvvN4cKlFuxTm_zkaJGbo9mUMBR6SRj16JJ4KE19w4H7_Mf_YiGnY1cqVmm_kg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d52d0e3bdb.mp4?token=GxpnV4ptxwXJst8PCoBoA1tCA_RPuqFv6CYrWcCk0EXOhcfX8NPKvQ5L9fwNgM4d3ME4LQsKrljifJgNzh0sPVSe0VC2c2FAnSsYw1tuVMIHeFhO7z5ebw5TtkNWh61wukUMGaWe5uZRePRpO-Ki6s_3HhGYOBfg9sHq3WkCsgPeg_2i7fjfF21GcO6rDRLRNg8dozs3L_uwkCnRybkrwDrcneCf0xCl_CK2P8FkBSg1U9jKqGb_woFnEwHiW5SsTWiQ6zOjmM2yLlRLPgmWuxAxGvvN4cKlFuxTm_zkaJGbo9mUMBR6SRj16JJ4KE19w4H7_Mf_YiGnY1cqVmm_kg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">منشأت ارامكو بعد هجوم القوات المسلحة اليمنية</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/naya_foriraq/92430" target="_blank">📅 16:44 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92429">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b2f30f9744.mp4?token=udBI-7PJtEY79CF2mOOBWlFjkfor-rXlGtYcV1LZmCkzwyKo_FUBqZZrVN1FehnGfJw4rSkOj6i_Cjs5YjKiwNW4hQmIjupk31I40QkWTSKB-pD3xBi1DqYFJxTR1b5z7ct4mDaP3avh4iMVcyTUIg7gJcXqPf7IdOzV2AIScfih1rasHWteBT6FUt9fAjJxlEZw_TJmuG8oPzifB-fE1iJ6WSt9HWtMKkdBUgiyOHtVCGly05v5E311KVxZu1hNaElXfBCx2Ci4ojLLEqOtORStctyl806WiQa6c-drOdpi2NwUdPXe3J7Y5VeMF5kujU0RUmiiG45n9wWt7q0r8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b2f30f9744.mp4?token=udBI-7PJtEY79CF2mOOBWlFjkfor-rXlGtYcV1LZmCkzwyKo_FUBqZZrVN1FehnGfJw4rSkOj6i_Cjs5YjKiwNW4hQmIjupk31I40QkWTSKB-pD3xBi1DqYFJxTR1b5z7ct4mDaP3avh4iMVcyTUIg7gJcXqPf7IdOzV2AIScfih1rasHWteBT6FUt9fAjJxlEZw_TJmuG8oPzifB-fE1iJ6WSt9HWtMKkdBUgiyOHtVCGly05v5E311KVxZu1hNaElXfBCx2Ci4ojLLEqOtORStctyl806WiQa6c-drOdpi2NwUdPXe3J7Y5VeMF5kujU0RUmiiG45n9wWt7q0r8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاهد من العاصمة السعودية الرياض بعد هجوم القوات المسلحة اليمنية</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/naya_foriraq/92429" target="_blank">📅 16:42 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92428">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7cd6222851.mp4?token=uX3FZYF7pDt8oNtqpVcmhboNtmHo6zkoZSJX7t95AgqlX3r-6WHTkmqHjxQ1y1lvyCKoXFztC7Up13ditKz4FDu2F3JQa_gaccfPUVPZbr3Ith6Tf8BZEe6dI2uvHXFhE-4_vbiAUhp-2NZydwb9TQpvq4y6vio8AP2IZz0T0GISU3F28Als2q2TRilcZRZkGmbcSUFW8WWEZW5RlblJT3xAiO1gFbSTmZYf4HJlUn0EIXM-ZRnQ2ANIkGf9R_7iUR9_wSDIwOOFlDx0j7FQeV-cj1URA-zzvv_ZmQFySqsDN9uzPohYuUfrOSJYawR9DFH-kTnT6YypdcRNZzxrCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7cd6222851.mp4?token=uX3FZYF7pDt8oNtqpVcmhboNtmHo6zkoZSJX7t95AgqlX3r-6WHTkmqHjxQ1y1lvyCKoXFztC7Up13ditKz4FDu2F3JQa_gaccfPUVPZbr3Ith6Tf8BZEe6dI2uvHXFhE-4_vbiAUhp-2NZydwb9TQpvq4y6vio8AP2IZz0T0GISU3F28Als2q2TRilcZRZkGmbcSUFW8WWEZW5RlblJT3xAiO1gFbSTmZYf4HJlUn0EIXM-ZRnQ2ANIkGf9R_7iUR9_wSDIwOOFlDx0j7FQeV-cj1URA-zzvv_ZmQFySqsDN9uzPohYuUfrOSJYawR9DFH-kTnT6YypdcRNZzxrCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاهد من العاصمة السعودية الرياض بعد هجوم القوات المسلحة اليمنية</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/naya_foriraq/92428" target="_blank">📅 16:42 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92426">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/im6ONHWW-431DhwlFYdliiBX-z8wjxafca06qFojsx_CiYO8ftTgHiyllhXLSjfXltfpAGCLdQDZFxaXVUGaz844hzu9kgy529seGKH9c8Yb82qQ_7jDaQ04-qZRDIy3yPRwrePZt0uL8A2sLnxfSis14g7oHI-5n5NAUXEF7p16UHcGVOQglpLFxDtSRSdz6eNuuGap00zKv2Fmf-rwLmaldzgQkNF_DmLKuPjDtudDgfdRGCrH4J7JTusm0b4UAlP3YZkOWtPuZwdLJhWJnERRXVZiS0PJFnTzQlCQ4ahTLf3jVWonEWXYev7AAxCecOwYQdKL9i-46NsyP5j-lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LEH2KDKKLlSv6aekgksFs7QtueWC4fqP4NwbgTpHsVIzzYq1ylsKzaFbvmv9UnaUed17A3r-3D2_NdmocBI3u0arJ9s7wmbyd_7ZLy6UwEoGz1X1dJ7lGRKKtTTiLjRecmzM7KCSDAg2D0T1aSfVRNAiNHxmoCo67FTIua5CaNweK6SSj-7STQaxLwzh5A_Qdu8GQ3aCnAOs_Ns2zs_59qXfUTWquCVAXEx0FvmnWHRKXbcE_1jhr5Slq69wcuv-cU3a6l_b7I0zIi8PiaiQJR2_wMgAi9-qeE7Pzr_xQBrl2wkMatOPXghIdygtsk6IznFVelDT6YdYMrJVD-yvMg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">صور أقمار صناعية جديدة تُظهر اشتعال صهاريج الوقود وخزانات الضغط في مصفاة أرامكو في الرياض عقب ضربات القوات المسلحة اليمنية</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/naya_foriraq/92426" target="_blank">📅 16:30 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92425">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">انفجارات جديدة تهز مضيق هرمز</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/naya_foriraq/92425" target="_blank">📅 16:22 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92424">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">جيش الاحتلال يعلن اصابة 8 جنود امس من لواء المدرعات السابع، بجروح نتيجة حادث سير عملياتي في جنوب لبنان حيث اصطدمت مركبتان ببعضهما بالقرب من بلدة رب ثلاثين ما ادى إلى نقل 6 من الجنود لتلقي العلاج الطبي في أحد المستشفيات وتم إبلاغ عائلاتهم.</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/naya_foriraq/92424" target="_blank">📅 16:19 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92423">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">عضو المكتب السياسي لأنصار الله حزام الأسد: العاصمة بالعاصمة ومن كانت عاصمته من بترول لا يُشعل النار في عواصم الآخرين</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/naya_foriraq/92423" target="_blank">📅 16:06 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92422">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">وزارة الصحة اليمنية: اضرار بمستشفى السبعين للأمومة جراء العدوان السعودي على العاصمة صنعاء</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/naya_foriraq/92422" target="_blank">📅 15:59 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92421">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vIur-6bj819jB_RBOWIWzo3H9LHd4ZwMOy7FsA4vWFHvqh08iXaQ4a_f_Cga1t8rPQyjzoJWCOOtt1sbTkN0x4B0Li6w3G7zcvaV0dmrDNYJVxFLPlECPt0trW6IPrahVbbWyWyFmWttnr-NzdyAJ-36NQvalaH5IocRYsHNiyevWNyDHlO1nOiDS4BAwNArLgmgMAldimaYiHXUpxzw5iwHmWqG2Z7_lDQ6BNZgkeOu95NtisLhQAFvNZjk-vP5fVz2QcFVSt0uMTjBZNNQ_g7qc2ag-FdgeiX9R2K_qY3VdEWgVjFVuGNr9W6SNEOWjInsjYZj7pG9FqTEGgKSlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خفر السواحل الأمريكي: اختفاء طائرة إسعاف جوية كانت تقل 6 أشخاص قبالة سواحل مدينة "نانتاكيت" بولاية ماساتشوستس. وعمليات البحث جارية.</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/naya_foriraq/92421" target="_blank">📅 15:53 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92420">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">القوات المسلحة اليمنية تتقدم في عدة مديريات في مدينة تعز</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/naya_foriraq/92420" target="_blank">📅 15:37 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92419">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">اطلاقات صاروخية من العاصمة صنعاء باتجاه الاصول العسكرية والاقتصادية للعدو السعودي</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/naya_foriraq/92419" target="_blank">📅 15:23 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92418">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🇮🇶
🔻
الحشد الشعبي يطيح بعدد من كبار تجار المخدرات الدوليين في منفذ ربيعة الحدودي مع سوريا و
التفاصيل لاحقاً.</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/naya_foriraq/92418" target="_blank">📅 15:19 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92417">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tsgx0p9eRsBLVz1OoTabHdR8M6i2VFZ0HHJ5C9u-CFvTSj3UtbdyMRhD1lULTZGE8LJ-B8mkTQGwddOOO_7TvPYyrSDgHI4g36GUDuacG969VUSik3ONdx5TyF9rOzDlCVuSnlW7Tp-hqOWJ5ogEatSYCZsuK8olIfkebNtQroEroqHbjc04cvEOIzwcuIs7VQpF5cw97L4HFvOZwekRSTVHmrE85E8ZsaHqUdUuf-BRlIoWywBMdwQvC6b8g7BqhZvJPY06UBZMPkgCHGQUc1kErysVUNzM4MVvOWIGXHTDld3tgiNC8yPHplHdVxorBjx8VJno1xucb3h2_qihQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وكالة رويترز: شوهد عمود دخان كبير وألسنة نار بالقرب من منشأة تابعة لشركة أرامكو في الرياض</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/naya_foriraq/92417" target="_blank">📅 15:14 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92416">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">انفجارات تهز مضيق هرمز</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/naya_foriraq/92416" target="_blank">📅 15:07 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92415">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">ممثل المرجعية الدينية العليا الشيخ عبد المهدي الكربلائي يعلن استعداد العتبة الحسينية المقدسة لتقديم العلاج المجاني للمرضى القادمين من فلسطين وتحمل تكاليف علاجهم ونقلهم</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/naya_foriraq/92415" target="_blank">📅 15:03 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92414">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">وكالة رويترز: شوهد عمود دخان كبير وألسنة نار بالقرب من منشأة تابعة لشركة أرامكو في الرياض</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/naya_foriraq/92414" target="_blank">📅 15:03 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92413">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/49a5b43795.mp4?token=SzuT5rjNqTLPqGJQ3Qexn14472gr9mEiZbq-iusjcAt23QtvTYZB-dBO0Cf81n2S4yk9ieWVQ26vJ4Vg6DkkldfQpIBbYfeciPU5-EUsri8T-mT9azgSzu3Cjg38fgILk6HZSdL1ASiDQehhu-MkTalCyKve-DASO_Ozgri49fhGzZoXAQeu0FFczbf6LFj-3wGW2XhIl7xSdXb6JPqOtwjcboMDxjdpQ1UZDqwoE79WalnJxjn4biGkNgRudnmgctgcsZkE1zUjLnLkZgDjG0M88opKSaCpQyAN41c9YdvyQpilzhqg6uJSuWcfK4KQC48SIIVZLKMCksUYJuFieg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/49a5b43795.mp4?token=SzuT5rjNqTLPqGJQ3Qexn14472gr9mEiZbq-iusjcAt23QtvTYZB-dBO0Cf81n2S4yk9ieWVQ26vJ4Vg6DkkldfQpIBbYfeciPU5-EUsri8T-mT9azgSzu3Cjg38fgILk6HZSdL1ASiDQehhu-MkTalCyKve-DASO_Ozgri49fhGzZoXAQeu0FFczbf6LFj-3wGW2XhIl7xSdXb6JPqOtwjcboMDxjdpQ1UZDqwoE79WalnJxjn4biGkNgRudnmgctgcsZkE1zUjLnLkZgDjG0M88opKSaCpQyAN41c9YdvyQpilzhqg6uJSuWcfK4KQC48SIIVZLKMCksUYJuFieg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇦
🇾🇪
توثيق يظهر إشتعال النيران في موقع نفطي أخر بالعاصمة السعودية الرياض بعد قصف صاروخي عنيف من قبل القوات المسلحة اليمنية صباح اليوم.</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/naya_foriraq/92413" target="_blank">📅 14:58 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92412">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">القوات المسلحة اليمنية تتقدم في عدة مديريات في مدينة تعز</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/naya_foriraq/92412" target="_blank">📅 14:56 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92411">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f77d1d4ff.mp4?token=da_E1rt1kp9vxxPOD3R8mwJpqPeNWYIkTZqz-8W1n6PgHXpgBnMxJOaZ7tCrZ1XVUyaJHmqX87v-F0cBlCBuROKhHyy1e2IuDjdCkYm4i5_APoGCV_PgDjNXWp3-lVzO4-HWjPGWK2XLqdovWvmM2Ssdfjfus3x3ReHekYIL3wYfYK9Eq2b6QnsocvGj9Zo6hnWiaoCs0haRNot3YqkbZ2N1uzuPCgFTYo_ayoeMRdSfs2U-NS5BRXMymzytogZ3-MDlLNy0fmflpf8OnWNlsIxNktgY7lzs1UOqajaUYjY79s3yU99ZIRvGV6-A4aFbSBZ46UYFYfCCpf8rwulk_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f77d1d4ff.mp4?token=da_E1rt1kp9vxxPOD3R8mwJpqPeNWYIkTZqz-8W1n6PgHXpgBnMxJOaZ7tCrZ1XVUyaJHmqX87v-F0cBlCBuROKhHyy1e2IuDjdCkYm4i5_APoGCV_PgDjNXWp3-lVzO4-HWjPGWK2XLqdovWvmM2Ssdfjfus3x3ReHekYIL3wYfYK9Eq2b6QnsocvGj9Zo6hnWiaoCs0haRNot3YqkbZ2N1uzuPCgFTYo_ayoeMRdSfs2U-NS5BRXMymzytogZ3-MDlLNy0fmflpf8OnWNlsIxNktgY7lzs1UOqajaUYjY79s3yU99ZIRvGV6-A4aFbSBZ46UYFYfCCpf8rwulk_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">من العدوان السعودي الاجرامي على العاصمة اليمنية الابية صنعاء</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/naya_foriraq/92411" target="_blank">📅 14:05 · 11 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
