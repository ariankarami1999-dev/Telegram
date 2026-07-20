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
<img src="https://cdn4.telesco.pe/file/muQNAevQnzCpyE6TwLUaFcwc77yvDswawaAvRoEzAL3HdtvFRZScQv13OhImWgsuf5x0mwx-UzPHflXzdcvU8nPHxIIWyMd2SG96HhcbUDIYKAedV1F1PpoAZd3Tm88smepCgW_NMPlxOo7KV1pjtDvQ9nZQbGB5ehnxS909mhc2Kq72TtqHLMnpt9CvMAPJLsAagcqsHsbpswbcjUZ9w0yRBZP98hn01ev_RVhD6fWZO5F2eYK7azai4gWO_TYkQtNRMh_yNta26tRTLNxNE0CeOr67MEFXL67RA8Av3R_QDN-UhhjZeJyhDh2Rcws2L6OGgmRPm54QcY4dWRAIwQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 937K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directمالک کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-30 01:08:35</div>
<hr>

<div class="tg-post" id="msg-136230">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uUS9_CGUvB8hybJDgTCS6TcvGuYlSal5QA6dpjxmxshp_gT8l7JjGxUEbnt937HQMb-Al3wrXJ3PtYDhM08ya8AEBAs1k4D4Tz1Ka7CaibDzILFflu61gAgyIoWdf5mlHUX2oBPbi8OAy_Rqort1p8_QqEuFhNzoMxi0bpwHTtcVKnjpmChSxRIxWpKyunwmuO0TRe2iQQAxoP7Vzwi4e2fVqQKK97-FWLGji_MyzpimYezzGcNjRawFyRi8grNQ1-rOe_sedgP-cL4goDeSzj2isgCgJxQs_AK9Ocm_UKSCk717ddILm8mThyDCU--s5JLgHEPESsZEXLrJEB6l5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سایت و برنامه فوتبال ۳۶۰ متعلق به عادل فردوسی پور بعد از انتقاد به شهرنویی فیلتر شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 1.01K · <a href="https://t.me/alonews/136230" target="_blank">📅 01:07 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136229">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/REjuYxE4-oquvkpA6N-dM-zGOSQoSD6RBB1-lrrNuitY4x408rm9TIs-glRYnaT8fvrBA1vEN1NnpL6SD3aSDFDRou4PedJmJS8YLNcragpPh9umLviGANYTlMEmJVfMFtHdm4lm-y04aSXtx7klSNjxPmM_OuOm5i5NyxvZEVlF8-NzYgLH0DraKZMMnbUA5s1Qt-dgI8WA5R2YYKTmnyDaz4krwThJJqVUJ9VDTK_gCmY1RUQJGuYjhExm4oTNdGzcmGRfbRtq6plurfaRabiWFRnqPQIhT872YrNxl52CyZRSHmOiA_gszoiz0mrQaYrgHbugVH0_7mtHbh0lcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
استوری جدید ترامپ و عکس اینفانتینو
😐
✅
@AloNews</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/alonews/136229" target="_blank">📅 01:01 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136228">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i5ZryoWHg3fxcwcTJXpjyIudIRqBx8Q0HfIFfYdZkXZjTCkzEA2o93iJbzP6v7ypLVS4fAKFtEIUpMBNKAgFxcUYq-wHfDByxfJt6-rNU5D2M3N5sse4RL8ln-ofxWpzbwG5PqRP9aA5u6g0lwS6Kvs18lQStTVcXwI0p1CmjzGe4ne0R6RY-n-3ltHytc10ZvWimAc-F_2wceunkXfvSCZv8XR97cqZVrEpBi-rbCceBzJXPuC9pYpLlDz_vscDgTclMjJfzI8hgMubREiEzeXRS8Wys4_9B4zXNq6ZKRdJAFlwNukGJiamMPNliEeGIKvNrqvvqZ95I0GCBtq0UA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
شیراز کوه دراک
✅
@AloNews</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/alonews/136228" target="_blank">📅 00:59 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136227">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c1e0618ffa.mp4?token=RCl9LhfKlY-BtpDw2Z0Ii1zeewfwk5HhSgntmlrOkWdNrsPmtpxhinnKABmm7Mo5vMBmZX8-26EQe6cKdIae_535QEEWU_FzOzNswcmKf3uyuiI3yKyAwqm13TWwcPDkYte3asKqxUFQeP5NNcqweJ_xOM2NLqWFEeTxL2OU2PXRdvul9B793OAOnSG-ohR3Ns_fCqMikZx2xgIaWBnLr6lGOLfLq8Ys3uzXjIyAKilCGPTuiSFMjQrtI4DSCabUR45kajAnduoywOhHtneF4Gau-QEB7yGIaJF-DvyBrixt9mPdlIaEgNWpIxyukDQAopcwd-1yf8VR-KyL24wte43MxBlQOjmvk8sSOWS8nTK28ov8WLdykjscUgbzNkdKxluL2DL_AEO0i578QQ0xWKaNIeTCbHRkxbIBAC2K_GbUHrW1pGHTUmcDCasFaq92x9jMaXt8C5iFLUf696WOL0XTWs2jSiUcYTB7lnk0TH61KcmCFdUer76rsiNdOIYuiiCMKrtOwSxNdKvi4ZlIHAfyrGpil2J-_SyzDf4pYW_Fz1SN99YLNgSd7sAYc9Qfj_-EsiUFACCT-n-w1srCxXPoRFhSKMa1MC7C9FgqoGhK4wSEKs-9U2KdcE2YSxKun6F1Y3-ooYcAoS0Bs6rIKZybp5H3fTi-b6Zfx-DvZbE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c1e0618ffa.mp4?token=RCl9LhfKlY-BtpDw2Z0Ii1zeewfwk5HhSgntmlrOkWdNrsPmtpxhinnKABmm7Mo5vMBmZX8-26EQe6cKdIae_535QEEWU_FzOzNswcmKf3uyuiI3yKyAwqm13TWwcPDkYte3asKqxUFQeP5NNcqweJ_xOM2NLqWFEeTxL2OU2PXRdvul9B793OAOnSG-ohR3Ns_fCqMikZx2xgIaWBnLr6lGOLfLq8Ys3uzXjIyAKilCGPTuiSFMjQrtI4DSCabUR45kajAnduoywOhHtneF4Gau-QEB7yGIaJF-DvyBrixt9mPdlIaEgNWpIxyukDQAopcwd-1yf8VR-KyL24wte43MxBlQOjmvk8sSOWS8nTK28ov8WLdykjscUgbzNkdKxluL2DL_AEO0i578QQ0xWKaNIeTCbHRkxbIBAC2K_GbUHrW1pGHTUmcDCasFaq92x9jMaXt8C5iFLUf696WOL0XTWs2jSiUcYTB7lnk0TH61KcmCFdUer76rsiNdOIYuiiCMKrtOwSxNdKvi4ZlIHAfyrGpil2J-_SyzDf4pYW_Fz1SN99YLNgSd7sAYc9Qfj_-EsiUFACCT-n-w1srCxXPoRFhSKMa1MC7C9FgqoGhK4wSEKs-9U2KdcE2YSxKun6F1Y3-ooYcAoS0Bs6rIKZybp5H3fTi-b6Zfx-DvZbE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
رضا پهلوی : من خودم رو مقصد نهایی نمی‌دونم
🔴
فقط پلی هستم تا مردم به انتخاب نهایی برسند
🔴
نه طرفدار سلطنت هستم، نه جمهوری
🔴
وظیفه‌م اینه که شرایط یه گفت‌وگوی سالم فراهم بشه و آخرش مردم خودشون تصمیم بگیرن چه نظامی می‌خوان
✅
@AloNews</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/alonews/136227" target="_blank">📅 00:57 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136226">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">👈
آژیرها در کویت به صدا درآمدند
✅
@AloNews</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/alonews/136226" target="_blank">📅 00:53 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136225">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">نمیخوام جو بدم یا ته دل کسی رو خالی کنم ولی این چنلو داشته باشید بدونید چ‌خبره :
@khabar
◀️</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/alonews/136225" target="_blank">📅 00:52 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136224">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👈
انفجار در بندر لنگه
✅
@AloNews</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/alonews/136224" target="_blank">📅 00:48 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136223">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
انفجار در شیراز
✅
@AloNews</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/alonews/136223" target="_blank">📅 00:47 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136222">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">👈
انفجار در اصفهان
✅
@AloNews</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/alonews/136222" target="_blank">📅 00:46 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136221">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yi9tnjQfre94MfvaNemUJyamj3dndBEIQ4Z7Ewtv09iQ13NzI1wJ19J3PICJ8weUU25eHmqVy9ezcWEAxgMTCr-SR90d2mopAgN1l27aOAQJNPiwAHgQUTtqvzRHyHYc5Y6pDjUcdwUxrzY7eZx1dZJr1jQKBZj7yxujTrlJ9P3TOvBLlQaZDQVdPKaUDJcb91p7HuJyiBJHwR_gq0VmKQED0iqzFIK8rpo2Fnw9D7iOPRc-J-MKOtvDD2rH_VSL6vhJq0L3kTrGMaLOdjI7J510K_SXU7LXzRrQiWwBf0FIRY_1P3YVo_iYEZfFZcYgISRehqW4k7A8HmsQBBREEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قلعه نویی:
هرکی با تیم‌ملی حال نمیکنه، بی وطنه
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/alonews/136221" target="_blank">📅 00:40 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136220">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kR0tCF2Ublpi7oY22bQQsrXuEsAvnLqwECGr8reGMWW_MQn_SWmtRL_Ls_btWogCUeJluPjON1Cg_gPpuWD73tt8mbkduiW-Wl3v9TSF9DH3KXd07Rv_cAAMEupfcF3uev9hgtY2nYQWLnebdVzdmzU1-caCBkRkg6BTLadjIuBSNmvJUFsvgDXbLnoVHFN9OGWuYeT56La4unNkK4TtwI5t1SjOWbAEfoeewtPFWUg3YdhQYgFSpxO_TJGeTiT0txaXhF2zFWnAZsZ9KEjDOJoh-gcJNdicE47DLkoBDyRJECqNY7IRX-5F02Fjo4a1jjIAMmTIbr4Nz7oUSLEyCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
خورشید در چابهار طلوع کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/alonews/136220" target="_blank">📅 00:37 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136219">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e7843e2638.mp4?token=PeD2lWcXnlogE5cyY9WCP_qNYAfCOHt2hM67eIZ9iI9pUfcA1blzq4HT_DcGUAO8vqlQBSpXjw4B2MK7tTSvSRanNcbDOP5njLX7Stu7CIocMic3RIyGjB6uUn9u_aCWi8l2ICQUmZsP4JRksiVzvbGfwduhaiSGH_e2Z_5dQp8jV0dFjIHtbiDY3x0o_staLXJgX2nH6qaXWeGtnokUmSATA8WKv9Yabm-7o5N9Ase1W9vQ46d0EFqwFwiAkoswd03RTU576DGyp2_GOQDnnpJdSqNSIJQKX_taBMYxqsa_Onahg0W_V8o2EUfS_pbsnQm52QkS2B7uGNuNDGLPxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e7843e2638.mp4?token=PeD2lWcXnlogE5cyY9WCP_qNYAfCOHt2hM67eIZ9iI9pUfcA1blzq4HT_DcGUAO8vqlQBSpXjw4B2MK7tTSvSRanNcbDOP5njLX7Stu7CIocMic3RIyGjB6uUn9u_aCWi8l2ICQUmZsP4JRksiVzvbGfwduhaiSGH_e2Z_5dQp8jV0dFjIHtbiDY3x0o_staLXJgX2nH6qaXWeGtnokUmSATA8WKv9Yabm-7o5N9Ase1W9vQ46d0EFqwFwiAkoswd03RTU576DGyp2_GOQDnnpJdSqNSIJQKX_taBMYxqsa_Onahg0W_V8o2EUfS_pbsnQm52QkS2B7uGNuNDGLPxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
قلعه نویی قبل و بعد واریز صدها میلیارد پول نقد به حسابش به عنوان پاداش
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/alonews/136219" target="_blank">📅 00:33 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136218">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a37ac31eab.mp4?token=szXH3AuQZpXCMeAMkndKqy5doQqfYezXX9EDRliMX93ZDa9736QVss5xfmdpbFcnI757qij991hmrgU0dRUNkH_2KRhXd88bMgj_gqLawvsku_4Odp-7YZkQbvPm1TMjwNdgTEQcoBfrGsWhDtJouVnFnTYhnK-55OF43a9MKVsfh_hH6OkBX1EPgDTqkitdK92MphF0W50rFcw_JXny6VVBBfY49m95fxHLhQWiLWhHsuBcyOrbPOrT7xSObdcTAaB04XnGq63Hg9rzfsg4X4cwMPYlBVrEFy9Lw1zB1V71IN21PBoVwRoZPyR3n8pGx6F2-QgnPNW07CGDpfcEMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a37ac31eab.mp4?token=szXH3AuQZpXCMeAMkndKqy5doQqfYezXX9EDRliMX93ZDa9736QVss5xfmdpbFcnI757qij991hmrgU0dRUNkH_2KRhXd88bMgj_gqLawvsku_4Odp-7YZkQbvPm1TMjwNdgTEQcoBfrGsWhDtJouVnFnTYhnK-55OF43a9MKVsfh_hH6OkBX1EPgDTqkitdK92MphF0W50rFcw_JXny6VVBBfY49m95fxHLhQWiLWhHsuBcyOrbPOrT7xSObdcTAaB04XnGq63Hg9rzfsg4X4cwMPYlBVrEFy9Lw1zB1V71IN21PBoVwRoZPyR3n8pGx6F2-QgnPNW07CGDpfcEMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مثل اینکه به دستور قلعه‌نوییِ پرونده‌ساز و خایه مال، واسه عادل فردوسی‌پور مشکل پیش آوردن و اپلیکیشن و سایت 360 اومده پایین!
🔴
عادل رفته تو لایو اینستاگرام داره اجرا می‌کنه...
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/alonews/136218" target="_blank">📅 00:29 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136217">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">👈
حملات مکرر آمریکا به منطقه چابهار-کنارک
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/alonews/136217" target="_blank">📅 00:26 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136216">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l4sNo27B710m4pJ0Lvm3Q3y-WNOze5s1ykYhS6jnCa0-g3OPjYhknxh_bDdfZV-ySmy5q8O841pGsdzWUBTxb-CuGyTsAmTPQTFrmZsXRJwuAfXiKn_goezSQxzY_ZknLUw487DYQiQNeGkGFQmkLi9dgCoTvbGSI2UDecugronpVLx_aZS3iclz0jOAGiiIB24vkM4gD-CvtyXSt4NaJ1HMJPNN74Qpecb1FUKD_H2Ui60fNEPNympUF1DAqtAEkb9ovsJMOgyC7QuIsNXkTWyICvHICLPmCFNPiz5LaOehmpzuGaVEbe4fMQG2nQmqTe7nRVbH5yznYujyjjrdvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
خبرنگار فاکس :
احتمال اینکه آمریکا دوباره وارد یه جنگ تمام‌عیار تو خاورمیانه بشه هم داره بیشتر می‌شه
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/alonews/136216" target="_blank">📅 00:25 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136215">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">👈
انفجار مجدد در بوشهر
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/alonews/136215" target="_blank">📅 00:23 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136214">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
پایگاه امام علی چابهار رو زدن
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/alonews/136214" target="_blank">📅 00:23 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136213">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👈
قلعه‌نویی:
مایه آبروی فوتبال ایران بودیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/alonews/136213" target="_blank">📅 00:22 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136212">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/22b1cf00f2.mp4?token=H8rbdWFQbiyHsyMj0YhqbenCQiLKq155NdXEwrIH9JtetsTR3funyurN_lBr9MwNsC1_UpEjp2e3mdwk6OAahONuKLVR063dtyxn-C_qq-j2NO-gAicWuuPd0KmSB-5kVcfylw6et6eKI_Y5ANUEt4TFgVZZyBcZnnvoHRfv0apm_XvIFhkTXK5tBspWR6nzSY5pOLAwjjO2cBu25GwcWUH3yqVFHgweMWgssgNVkO3tyPROsFPa81rWf1jU4kaYutkbiDb8eUi75tjfjV49H-HCIAfjC4ZbljtgarCU5lGA_80iMmTfhJfZI7xAhTtWUbg63ackYqEhDL4bogDOYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/22b1cf00f2.mp4?token=H8rbdWFQbiyHsyMj0YhqbenCQiLKq155NdXEwrIH9JtetsTR3funyurN_lBr9MwNsC1_UpEjp2e3mdwk6OAahONuKLVR063dtyxn-C_qq-j2NO-gAicWuuPd0KmSB-5kVcfylw6et6eKI_Y5ANUEt4TFgVZZyBcZnnvoHRfv0apm_XvIFhkTXK5tBspWR6nzSY5pOLAwjjO2cBu25GwcWUH3yqVFHgweMWgssgNVkO3tyPROsFPa81rWf1jU4kaYutkbiDb8eUi75tjfjV49H-HCIAfjC4ZbljtgarCU5lGA_80iMmTfhJfZI7xAhTtWUbg63ackYqEhDL4bogDOYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
در جواب به حرفای عراقچی باید بگم که تمامیت ارضی مهمترین شرط رضاپهلوی برای قرار گرفتن کنار ایشونه.
🤔
جمهوری اسلامی هنوز نمیخواد بفهمه که دروغ دیگه جواب نمیده و ما تو سال 57 ننگین نیستیم که رسانه ای نباشه تا دروغ هاتون رو نشه.
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/alonews/136212" target="_blank">📅 00:21 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136211">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
چابهار زیر بمباران سنگین
🔴
۲ تا دیگه سنگین زدن
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/alonews/136211" target="_blank">📅 00:16 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136210">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/56b2b31776.mp4?token=aCjALI3FFCE7Ph8_gyEhRoLiAM1tFjkONOsU6XHAGNpAuIYAbWhB6WfuT6R-eaGjVBqLZ4uw4Q8efoIbt4bR89Om-j3Qwn6PfI0JJ4KPgoeEM9tiww1S2q4oHakgA81t48w9mu51Thp8OO2XjCB_nDKHiVZbHff3Z_qqxPqnF6WBdiXM9iM965mro2AktT8QRxGYvjgr67LqKCRMCPMkBH5weRpJbqW0y09OOGYa-Ubwaxf3O5w027N1iDKtOOszwwrWVtF_BDEhwwRcQzsWpUDLq46w-TwoEHJDvHwvgKgGFx_w6j4RXhQQMOtAT3qY5LdAgpgEbaEsMmLXoW4m1DzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/56b2b31776.mp4?token=aCjALI3FFCE7Ph8_gyEhRoLiAM1tFjkONOsU6XHAGNpAuIYAbWhB6WfuT6R-eaGjVBqLZ4uw4Q8efoIbt4bR89Om-j3Qwn6PfI0JJ4KPgoeEM9tiww1S2q4oHakgA81t48w9mu51Thp8OO2XjCB_nDKHiVZbHff3Z_qqxPqnF6WBdiXM9iM965mro2AktT8QRxGYvjgr67LqKCRMCPMkBH5weRpJbqW0y09OOGYa-Ubwaxf3O5w027N1iDKtOOszwwrWVtF_BDEhwwRcQzsWpUDLq46w-TwoEHJDvHwvgKgGFx_w6j4RXhQQMOtAT3qY5LdAgpgEbaEsMmLXoW4m1DzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سخنگوی ارتش: اگه آمریکا بخشی‌از خاک ما رو تصرف کنه، ما خاک خودمونو موشک باران میکنیم!
😐
😐
😐
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/alonews/136210" target="_blank">📅 00:13 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136209">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🔴
فوری/انفجار در بوشهر
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/alonews/136209" target="_blank">📅 00:10 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136208">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🔴
فوری/انفجار در بندرعباس
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/alonews/136208" target="_blank">📅 00:07 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136207">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🔴
فوری/انفجار در کنارک
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/alonews/136207" target="_blank">📅 00:05 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136206">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">💢
فوووووووری/پرواز جنگنده‌های آمریکایی در مرز ایران
🚨
@AkhbareFouri</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/alonews/136206" target="_blank">📅 00:03 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136205">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mJM5As4sa_s1mC5dOQBRh_glT2xCQSqLw-OjH_kL1fEEgBLKppG_FGVAO3PdANdTEUc5XKYRUMRhgeWv9tJkEk3tAqYsi3myuEP9cqtl-sNEYyrOcXIJZBavGjCAJjrOScv8ZHqUwPiXUEqjyu0kC-15qVYK7EgHXLmqDf7FyhHo4OH-qlgtSk93pUDYqniw2WrmhIYmzFUfz6FfMfsoDxGMc-gS1N0rFGHInbWQU4ILzXV0q7DtjlSSybmgMx5Pvb_FzxDKRAhHD6RLMELH4_28EH9KdZwOyhXjH_2N6OClHITJHTVfveXUsGaAzHV1JtL4KgBBIJs3TzUG07joAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
گویا از طرف صدا و سیما به محمدحسین میثاقی به پاس مجاهدت رسانه‌ای یک واحد آپارتمان پاداش داده شده
✅
@AloNews</div>
<div class="tg-footer">👁️ 58K · <a href="https://t.me/alonews/136205" target="_blank">📅 00:01 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136204">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👈
گزارش انفجار در چابهار
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/alonews/136204" target="_blank">📅 00:00 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136203">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
عربستان: ما از کشتی‌های تجاری‌مان در تنگه باب‌المندب محافظت خواهیم کرد و با قاطعیت و قدرت به منابع تهدیدها پاسخ خواهیم داد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/alonews/136203" target="_blank">📅 23:59 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136202">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👈
لغو امتحانات نهایی هرمزگان در روز سه‌شنبه
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/alonews/136202" target="_blank">📅 23:58 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136201">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
صدای پدافند در بوشهر
✅
@AloNews</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/alonews/136201" target="_blank">📅 23:56 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136200">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
صدای پدافند در بوشهر
✅
@AloNews</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/alonews/136200" target="_blank">📅 23:54 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136199">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
سفارت ایران در فرانسه: امنیت تنگه هرمز با نادیده گرفتن حقوق و منافع مشروع ایران تأمین نخواهد شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/alonews/136199" target="_blank">📅 23:54 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136198">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">👈
صداوسیما: صدای انفجار در بخش بمانی شهرستان سیریک شنیده شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/alonews/136198" target="_blank">📅 23:53 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136197">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
مهر: قشم هدف حمله قرار گرفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/alonews/136197" target="_blank">📅 23:53 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136196">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">👈
انفجار در بوشهر
✅
@AloNews</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/alonews/136196" target="_blank">📅 23:52 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136195">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">👈
روسیه: آلمان یک سال تا ساخت بمب اتم فاصله دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/alonews/136195" target="_blank">📅 23:52 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136194">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6ce5b8423f.mp4?token=C27WARLadtwyb4yE34xxM7QSAAf2pk2dDhbOb6AbTEvnh_Xxu4hswYapmBvrt10mZ0C2NqLqMf2rM8WW_aCUUDC-weC55NKB-OxAEW48tJoe0C9KZVMr0UXR_5f939FaV7ZaQ7_mC2U5kROLzG4d6PFIc4McIsN5SjEgrtNadwmTBd-53aAQRmDNELWegpUxHKGB8oifZHdN-3yNFz-dzbCEbSI8hH8anxSLNQSTisnVhd3sl6z6cq-31vYyKv7pl5ad1NQ1OoFPKxFuOM6MskNTic3lIg26ThbI6BC-KkUjzDoBIIAZE6kJxqSsrEpNaEXAP33OjNc9RbttfjW-tA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6ce5b8423f.mp4?token=C27WARLadtwyb4yE34xxM7QSAAf2pk2dDhbOb6AbTEvnh_Xxu4hswYapmBvrt10mZ0C2NqLqMf2rM8WW_aCUUDC-weC55NKB-OxAEW48tJoe0C9KZVMr0UXR_5f939FaV7ZaQ7_mC2U5kROLzG4d6PFIc4McIsN5SjEgrtNadwmTBd-53aAQRmDNELWegpUxHKGB8oifZHdN-3yNFz-dzbCEbSI8hH8anxSLNQSTisnVhd3sl6z6cq-31vYyKv7pl5ad1NQ1OoFPKxFuOM6MskNTic3lIg26ThbI6BC-KkUjzDoBIIAZE6kJxqSsrEpNaEXAP33OjNc9RbttfjW-tA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
تهاجم واقعی دشمن به بندرعباس در 18 دی 1404 اتفاق افتاد.
🔴
زمانی که حرام زاده های حکومتی به مردم بی‌دفاع ایران که تنها سلاحشون برای دفاع سنگ بود، شلیک مستقیم میکردن.
🤔
الان که رو لبه سقوط واستادن صحبت از وطن میکنن و حمایت مردم رو میخوان که گوشت قربانی جلوی حمله خارجی باشن.
✅
@AloNews</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/alonews/136194" target="_blank">📅 23:51 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136193">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kSb-1U9_cIH6QnMwbrZQrFktIODNPoO7b2g8gp3ZjUT25egZdtLh6TIqcTRM2C2jhNsw16xi1LRM-ZvL2Cq4_UGtHrNht9riBbsLah73POVO8yNKj_DiRMEzsNArvxU0Jsro-_h1yKZMRm1g1upCOcaYFq7WtUbztHj_1Jkq__NL6sSleqIixZ5y0k4R6MPL6hJbqBGQ4etszttEFEFn3E5u-J8yG9cAHn4EmE11dpkLUKZ4u-n7k8M31-eA1xBNUEMraT3YmKJFORBbb9rMA8l4MNaR1h7gwDEahNAtjuaE6YRQJ_n8QAZ1NQnlaMiYnQfMyx2ayeTmMW6FvRYJFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فوری / سنتکام دهمین دور حملات به ایران رو شروع کردیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/alonews/136193" target="_blank">📅 23:48 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136192">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">👈
هم اکنون فعالیت جنگنده های آمریکا در آسمان بندر عباس
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/alonews/136192" target="_blank">📅 23:47 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136191">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
طبق گزارش ها بیش از ۸ انفجار در بندر عباس شنیده شده
✅
@AloNews</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/alonews/136191" target="_blank">📅 23:45 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136190">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">👈
انفجار در سیریک
✅
@AloNews</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/alonews/136190" target="_blank">📅 23:43 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136189">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">👈
احتمال حملات آمریکا به بندرعباس. گزارش‌ها حاکی از آن است که انفجارها بسیار بزرگ بوده‌اند و نمی‌توان آن‌ها را به پرتاب موشک‌های کروز ضدکش مرتبط دانست.
🔴
احتمالاً انفجارهای سیریک نیز نتیجه حملات آمریکا بوده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/alonews/136189" target="_blank">📅 23:42 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136188">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🔴
فوری / انفجار در قشم
✅
@AloNews</div>
<div class="tg-footer">👁️ 58K · <a href="https://t.me/alonews/136188" target="_blank">📅 23:38 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136187">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🔴
فوری / بندر عباس صدای انفجار
✅
@AloNews</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/alonews/136187" target="_blank">📅 23:38 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136186">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🔴
فوری / بندر عباس صدای انفجار
✅
@AloNews</div>
<div class="tg-footer">👁️ 58K · <a href="https://t.me/alonews/136186" target="_blank">📅 23:37 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136185">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🔴
فوری / بندر عباس صدای انفجار
✅
@AloNews</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/alonews/136185" target="_blank">📅 23:36 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136184">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">👈
عوستاد رائفی پور: ترامپ و امارات، خارک‌ و‌ سه جزیره را نخواهند دید
✅
@AloNews</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/alonews/136184" target="_blank">📅 23:34 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136183">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">👈
وزارت خارجه آمریکا در  یک هشدار امنیتی از شهروندان آمریکایی خواست درپی افزایش تنش‌ها در خاورمیانه، سریعا ایران را ترک کنند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/alonews/136183" target="_blank">📅 23:33 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136182">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k_Gm5c2BaPpcDOYkyPbJkhsV8j_Ulw3s1WuuzBpgzKL-ZjLzeoCWgD07M3AgWAM-D0phg5YLVMIUCMB9bbcXvRS0Xg_6TM529v-HLyn1U-I6aSxwjclDtd3vLvUwv9knl__EQyc1L5Gr61IOKy2wNdn13ig-DpPNJBSjrMVJIXvUjo4QdT-rP4r6nunMO0jwhtr9hNQw7WoRjM7Eep9O3PTuiv5Z1_kTVOI4l1lr8A00m4XfCCc6BoRqPcOyl9LkBT0i7NdoBbBxTKXEw8nKsrRka5s05U8vOPNjBbQywr0LGw36rpMPG8ibSWdL6UDgQ-NBLyM-4ViL3DKLJHC_2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
روایت متفاوت یک سایت روسی از سرنوشت سومین نظامی مفقود آمریکایی
🔴
یک سایت روسی مدعی شده برخلاف اعلام سنتکام، جسد سومین نظامی مفقود آمریکایی پیدا نشده و احتمال فرار و درخواست پناهندگی او قوت یافته است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 60K · <a href="https://t.me/alonews/136182" target="_blank">📅 23:30 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136181">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
صدای چند انفجار از حوالی شهرستان سیریک در شرق هرمزگان شنیده شد و تاکنون جزئیاتی درباره محل دقیق یا علت این انفجارها اعلام نشده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 58K · <a href="https://t.me/alonews/136181" target="_blank">📅 23:30 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136180">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🔴
فوری / هم اکنون گزارش‌های اولیه حاکی از شلیک موشک‌هایی از ایران به سمت تنگه هرمز است می‌باشد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/alonews/136180" target="_blank">📅 23:26 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136179">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
یک مقام آمریکایی به الجزیره:
گفت‌وگوها بین ایالات متحده و ایران ادامه دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.1K · <a href="https://t.me/alonews/136179" target="_blank">📅 23:21 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136178">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
سی بی اس: تو حملات ایران به پایگاه‌های آمریکا تو خاورمیانه حدود ۱۰۰ نظامی آمریکایی زخمی شده
🔴
بعضی‌هاشون آسیب مغزی شدید دیدن، اما ۹۶ درصدشون دوباره به خدمت برگشتند
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.1K · <a href="https://t.me/alonews/136178" target="_blank">📅 23:17 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136177">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🔴
فووووری/سی بی اس:
یک توافق موقت درحال شکل گیری است
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.2K · <a href="https://t.me/alonews/136177" target="_blank">📅 23:13 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136176">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lZ04aaPmWTejgs6iW_qhXVA5nyNQs_2XcCzajnPuh-DPonxZV_jE4AMK15DRKsICxCsRI8dLGqyh3M8WtRtOupAjfbvrSvG1b0JrdmTHddVzb3QDOrf9z85AuzoaNXm6627fVy_aKc1geIoXuNkFt6GA3ZCWX3jNCtXdZ0q7X-TqH80GkV_zBnMaTOCKp6OtZU_YDKg6Oww_ZvKcyem2-5IsDmp0Ry7ggEF0tjtXh4oUa9OJVtgBTQ9_7OJTVl4ominqdW67AIQdMYYNJDn3pRtLhyc46EGeNFmtL-XQQxV7sHUHM4XUKrearbOKDH1qSjE3ZCLbn8dep1aOQHxT1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استوری دنیا جهانبخت از حضور در مراسم عزاداری.
وقتش شد یادی کنیم از ..... زدن دنیا خانوم جهانبخت برای تتلو
😂
😂
😂
◀️
◀️
مشاهده فیلم</div>
<div class="tg-footer">👁️ 68.3K · <a href="https://t.me/alonews/136176" target="_blank">📅 23:09 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136175">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C5xQixAuY-MTdOIzsru65j5aqLRL5UMzbHAVBHPgCnB9asGlwzBxMR9omg8sP4nCtwXTNgVUcaDN1Ve9dY-MQpvO2VuC2d2mcHhPIvPpzAMfBSPl3XAPv1g-Yl8-c814DTBIoCPuq60_hl_zh7WtLpUsqkHIbzjwrc06BkCQkidzyuSgfLsi_YnJBJg1TW1khXgLsCQidH0hWtTHysJTsKvcw0vhSocnAhbCFMPJuguv8eB9V9YYNPAt42nfrc0DYjts-mrehfH-iWePFnuM8lQUFU9qfhyHh3ZhCMvSZrizuSBAmLkaBGVIVygQ3QHi95ZYc1TBMlpKj_BxMySIng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
باراک راوید: احتمال برگزاری مذاکرات برای توقف درگیری‌ با ایران وجود داره
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.2K · <a href="https://t.me/alonews/136175" target="_blank">📅 23:06 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136174">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UDd8WWLad0UMptrJmF8gPNOVOFjHQrFbHwLFa9siIRn3Xhxhy0DbNyqDj63KNg2d3mmTvZWIVau6KYwbL4EGj9cG6bDaPmrbMv7U08Cge-C3lsJHwrq0KiA1MwvWLN6o1-HQtxgsIVjsvjUT3Z9ZxPlB9XS2KpXZIJsIU_rlHGAhES09I3A5IjYMaGF1VVay27qSas-qO9IcdIo9JvkofGc6A1wtGRIACHjzCIfn8mY35aHpLC8iU25Xs_GrNVVQbqjWM01TEpvag3znY6PO8MIl0tQV34KF32hsDISpkUQUM2hme2YK4DOZWpH51UZu0gB-xbtvSt-Eem2roH6uhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رسایی: فوتبال تمام شود، کار آقایان در وزارت ارتباطات برای قطعی اینترنت شروع میشود، اگر نشود دوباره تماس خواهم گرفت.
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.3K · <a href="https://t.me/alonews/136174" target="_blank">📅 22:59 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136173">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/JO9xy6clG5HNQgKm-YbjuDLeXjjjvAetpCMAEf5EuXDXH4n5LjtxFS3wHRzEK4HTgJ2Sn45fAx-k--EeUXvvFYCyt9V5lkkB3J3bqZYfA1QzlYXvY_g8Wejsdv7NpznvjH7ZmiILtztkA7lHpA2z67Fam9TA5Dt5_gfwASiUq5kqPewvfirOmmHswsr0lTEqdd1DBHXMRHFwCE5h3jKcfSY8_QyvpL6BmuxcBY4FsFtd5iaPqqXPhAsibMtozZyQG4e4HTT2gMS4zBC009EQkoVukzSsYmDgoCpE1nM8S4OH5PWil6y3Q9Ui9wf9_ELUD2cHWeHrq_M3dPjKLtL1jQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
متاسفانه رومینا رحیمی و ترانه رحیمی، دوقلوهای 18 ساله
🔴
بخاطر شرکت در اعتراضات دی ماه و تخریب اموال عمومی و... قراره بزودی اعدام بشن.
#نه_به_اعدام
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.3K · <a href="https://t.me/alonews/136173" target="_blank">📅 22:55 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136172">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b921e97792.mp4?token=A6t5NtqrqXJlkJLtML1Sx4qZXVHflpxVuxl9Ze9zoGh9WpRFaFI6FuBwPcULrE6P0gMeO8TGoc4pGaispQDFGmzA9t-02t6kmVWo88h6j1wSFO0zWSFWOeDRbJbRdrw-I-5SuoBRghyxyOMf5CvVK0u2DkloFHrds9ycabqWZJ-5uPjD98VQHMNTO97FBBv_7GDG4WXmMPuEzRO-J1dyvTckiXeoEAPdZau2k6NGRJpxoWsmvrFtowIbwKSHhQLxUM8OaYcwBMEbR9Iu7nGhKouE8_2l7VmAXnnkujrKUQOfUXmkvPuTYeTm9P7nhMEF9hxjx5RUg01sbdaid-_YGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b921e97792.mp4?token=A6t5NtqrqXJlkJLtML1Sx4qZXVHflpxVuxl9Ze9zoGh9WpRFaFI6FuBwPcULrE6P0gMeO8TGoc4pGaispQDFGmzA9t-02t6kmVWo88h6j1wSFO0zWSFWOeDRbJbRdrw-I-5SuoBRghyxyOMf5CvVK0u2DkloFHrds9ycabqWZJ-5uPjD98VQHMNTO97FBBv_7GDG4WXmMPuEzRO-J1dyvTckiXeoEAPdZau2k6NGRJpxoWsmvrFtowIbwKSHhQLxUM8OaYcwBMEbR9Iu7nGhKouE8_2l7VmAXnnkujrKUQOfUXmkvPuTYeTm9P7nhMEF9hxjx5RUg01sbdaid-_YGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
توهم پناهیان
‼️
🔴
ما الان داریم منطقه رو آزاد میکنیم، مردم اگه بی برقی و بی آبی رو تحمل کنن، جهان رو آزاد میکنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.3K · <a href="https://t.me/alonews/136172" target="_blank">📅 22:50 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136171">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
وال استریت ژورنال:
مقامات آمریکایی جزئیات سه حمله موشکی جداگانه به پایگاه هوایی موفق السلطی را شرح دادند:
🔴
حمله اول به باشگاه ورزشی پایگاه که منجر به زخمی شدن تعدادی از سربازان در مسیر رفتن به پناهگاه‌ها شد
حمله دوم به یک آشیانه خالی هواپیما
🔴
حمله سوم به یک خانه کانتینری که سربازان در آن خوابیده بودند
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.3K · <a href="https://t.me/alonews/136171" target="_blank">📅 22:47 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136170">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🔴
حمله زمینی ایران به کویت</div>
<div class="tg-footer">👁️ 70.3K · <a href="https://t.me/alonews/136170" target="_blank">📅 22:46 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136169">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
شبکه اسرائیلی کان:
ترامپ به اسرائیل دستور داده است که در هیچ رویارویی نظامی با ایران شرکت نکند، مگر اینکه خود تهران ابتدا به هدف قرار دادن اسرائیل اقدام کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.4K · <a href="https://t.me/alonews/136169" target="_blank">📅 22:37 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136168">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
شرکت هواپیمایی ایرفرانس، تمامی پروازها به کشور های خلیج فارس را به مدت هفت روز متوقف کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.4K · <a href="https://t.me/alonews/136168" target="_blank">📅 22:30 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136167">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/iuOruwZqLevlb35oK6sPCCUtTMvboUrqZJaRrt2TFcQMRoBngYe0MARkF5KYrfSAK10UJgjlAREkSsAHe7HBWzGriRbcQTt5l39FhBf-s5w26HgMXvhYCuZAX3VEnQ10nNISCFR6hJG9RsfYt37P1fGdiQ6d1-ei5Ww1x9Q6vwqFk7vT8_M50R0HVa6Tzu1jqbUQbWa0RM5UvXw-DiVTAxfBniYD4npFWf8Gd0w7IQ3NLX3nunUDmD26vh2aAZ4Iy7HyluVqKuSBsXBmeFpSj3J5BzvOVbjsK8ZJI3y6S46nIyfgMdRCoN_ZECCCa6cH6rXgZ7etf5YeJ1jtI37y4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
توی بالاشهر تهران، نیمرو میدن 2 میلیون و 137 هزار تومن ناقابل! تازه با 5 درصد تخفیف.
✅
@AloNews</div>
<div class="tg-footer">👁️ 79.5K · <a href="https://t.me/alonews/136167" target="_blank">📅 22:25 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136166">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👈
ارتش اردن : ۳ موشک شلیک‌شده از ایران رو رهگیری کردیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.4K · <a href="https://t.me/alonews/136166" target="_blank">📅 22:18 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136165">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
تعداد سوخت رسانهای آمریکایی در اسرائیل به عدد 90 فروند رسید
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.4K · <a href="https://t.me/alonews/136165" target="_blank">📅 22:13 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136164">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">👈
وزیر راه: بازسازی سالن مسافری فرودگاه بوشهر به‌زودی آغاز می‌شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.4K · <a href="https://t.me/alonews/136164" target="_blank">📅 22:08 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136163">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">👈
اطلاعیه جدید آموزش‌وپرورش درباه امتحانات نهایی
🔴
آموزش‌وپرورش: بر اساس تصمیم ستاد عالی آزمون‌ها، امتحانات نهایی پایه یازدهم تمامی رشته‌های تحصیلی، در روز چهارشنبه ۳۱ تیر ۱۴۰۵ در همه استان‌های کشور، به جز استان هرمزگان، مطابق برنامه ابلاغی برگزار خواهد شد.
🔴
امتحانات نهایی پایه دوازدهم در روز پنجشنبه، یکم مرداد ۱۴۰۵ در تمامی استان‌های کشور، از جمله در استان هرمزگان مطابق برنامه برگزار می‌شود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.4K · <a href="https://t.me/alonews/136163" target="_blank">📅 22:04 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136162">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
طبق گزارش i24NEWS با استناد به یک منبع امنیتی اسرائیلی: ایالات متحده در حال آماده‌سازی مرحله بعدی از کمپین نظامی خود علیه جمهوری اسلامی در روزهای آینده است و افزود که طرح‌های عملیاتی نهایی شده‌اند و در انتظار تایید رئیس‌جمهور ترامپ هستند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.4K · <a href="https://t.me/alonews/136162" target="_blank">📅 21:58 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136161">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
پرس‌تی‌وی: گزارش‌هایی از انفجارهای شدید در پایگاه‌های نظامی آمریکا در اردن
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.3K · <a href="https://t.me/alonews/136161" target="_blank">📅 21:55 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136160">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">👈
شهردار نیویورک، ممدانی : نتانیاهو حکم بازداشت داره اگه وارد نیویورک بشه، باید طبق قانون، برخورد بشه
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.3K · <a href="https://t.me/alonews/136160" target="_blank">📅 21:55 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136159">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c3bbc33d8c.mp4?token=GmmMWuB1rmya6n8YHtLpaxY3BlVo8EfgvH9_m8WPbro6C4LO1d5JUPlgBv-joYOW_dhQcdxblfAFMeIB2XCtV49D9W02DE6YlLWpRHwCoAzUK6rEX-zr8ZalmS-PTLyJdWgCsOtzRQQE-fEDQLTp3-VlcWfSblUwTMM7QnRboq6rtF84biVXUezOOF0-jk6l9bq8IOFz_atRqJwsK6QQwkGabb266mwb8j9XKETtuavVzqCNWTlry_6XTZeaox3dfDSAsFLzMlpHtl306RF1ZAd3wEvQNvAq808I4u85pf837b9pYcpdfIkY4kAavTMzxyEdSckSsdzdLCxk_WyzZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c3bbc33d8c.mp4?token=GmmMWuB1rmya6n8YHtLpaxY3BlVo8EfgvH9_m8WPbro6C4LO1d5JUPlgBv-joYOW_dhQcdxblfAFMeIB2XCtV49D9W02DE6YlLWpRHwCoAzUK6rEX-zr8ZalmS-PTLyJdWgCsOtzRQQE-fEDQLTp3-VlcWfSblUwTMM7QnRboq6rtF84biVXUezOOF0-jk6l9bq8IOFz_atRqJwsK6QQwkGabb266mwb8j9XKETtuavVzqCNWTlry_6XTZeaox3dfDSAsFLzMlpHtl306RF1ZAd3wEvQNvAq808I4u85pf837b9pYcpdfIkY4kAavTMzxyEdSckSsdzdLCxk_WyzZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
فعالیت سامانه‌ی پدافندی پاتریوت در اطراف پایگاه هوایی الازرق اردن جهت دفع حملات موشکی سپاه
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.3K · <a href="https://t.me/alonews/136159" target="_blank">📅 21:55 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136158">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
شبکه اسرائیلی کان: ترامپ به اسرائیل دستور داده است که در هیچ رویارویی نظامی با ایران شرکت نکند، مگر اینکه خود تهران ابتدا به هدف قرار دادن اسرائیل اقدام کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.3K · <a href="https://t.me/alonews/136158" target="_blank">📅 21:53 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136157">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👈
تحلیل نیویورک‌تایمز: ایران و آمریکا به لحظه «بیدار باش» رسیده‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.3K · <a href="https://t.me/alonews/136157" target="_blank">📅 21:50 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136156">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">👈
هم اکنون وضعیت در اردن عادی است
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.3K · <a href="https://t.me/alonews/136156" target="_blank">📅 21:45 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136155">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/34da7dc70f.mp4?token=MKL__vvG4OfYNQlNWKGBf_M-Zf9mwHXBOlav30ukDBTR9IJhlblDGgiA2gWDz8rWVUQoHaWeKKZGMoC0ZNWuUVyEp1HtR3nli6V5MecHqm9ORrN2Qd0LAqOAfFRsxYLiHegCjt4vH6nqXgWmq4Zxef9VjNuagiILhB3n5lJAdnfT6Rw0cY6B49tkAJrlNQsGKGpJHVwLsXf7vZ0Yj75Z1EEN29nhPcwKLfTHhVi0BjDvG7UaPqy9QYfivvM_9sRp-VhdfOx8SEQCgYAvv-qQQpyvMLeSPcSXLkgz7p6ULqqWZaCh2gg46Lfmv5vap4fO5BV0NcvEV67QPUO60FTQJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/34da7dc70f.mp4?token=MKL__vvG4OfYNQlNWKGBf_M-Zf9mwHXBOlav30ukDBTR9IJhlblDGgiA2gWDz8rWVUQoHaWeKKZGMoC0ZNWuUVyEp1HtR3nli6V5MecHqm9ORrN2Qd0LAqOAfFRsxYLiHegCjt4vH6nqXgWmq4Zxef9VjNuagiILhB3n5lJAdnfT6Rw0cY6B49tkAJrlNQsGKGpJHVwLsXf7vZ0Yj75Z1EEN29nhPcwKLfTHhVi0BjDvG7UaPqy9QYfivvM_9sRp-VhdfOx8SEQCgYAvv-qQQpyvMLeSPcSXLkgz7p6ULqqWZaCh2gg46Lfmv5vap4fO5BV0NcvEV67QPUO60FTQJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حرکت پهپاد شاهد به سمت پایگاه آمریکا
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.3K · <a href="https://t.me/alonews/136155" target="_blank">📅 21:43 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136154">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4ded62ba49.mp4?token=ViGTIRKm58JTj2z8wvO7-el2yzM-8qNGEduXzooik9Qlb7jfAvdWiRVPrqMlCUftfyghA2JBINhODvUHrwlnyQZQa15GJ-V3ZMEzmU3D7Oefwj6-YbSr6LADJ2wt_t1uRTOAQJoowQQKXMw6EHFdUvZlRnYucXSXlgmXg4BQplChl_LY8xmebIv8eY9sAEyNIO9erdpVsN2eKxQC9c537aEWSkWBjVyNNKsvfUpbsIp9-ddLBAvktJixII6MfZ2zBP4m884MZkzSbVPUre56wcHGKOLnq7IBq9n-jbzRywy191FpPAjVIxtVzGsJL1ioO-oXlAHTq4xhql1uzALxyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4ded62ba49.mp4?token=ViGTIRKm58JTj2z8wvO7-el2yzM-8qNGEduXzooik9Qlb7jfAvdWiRVPrqMlCUftfyghA2JBINhODvUHrwlnyQZQa15GJ-V3ZMEzmU3D7Oefwj6-YbSr6LADJ2wt_t1uRTOAQJoowQQKXMw6EHFdUvZlRnYucXSXlgmXg4BQplChl_LY8xmebIv8eY9sAEyNIO9erdpVsN2eKxQC9c537aEWSkWBjVyNNKsvfUpbsIp9-ddLBAvktJixII6MfZ2zBP4m884MZkzSbVPUre56wcHGKOLnq7IBq9n-jbzRywy191FpPAjVIxtVzGsJL1ioO-oXlAHTq4xhql1uzALxyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
موشک
های رهگیر بر فراز آسمان اردن
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.2K · <a href="https://t.me/alonews/136154" target="_blank">📅 21:42 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136153">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd5d359683.mp4?token=bQ_QVgI0QhM78iH0Iw_7B-RPzCR_X99s4Mxzhq-2QtddSGnaqMen_8vk7r8xwPgAciTT4LPmWwRPBt7G4q_dmT9GBUDqjD1yBpquro1-IWxSZEkaGVlTbnKcuVwRPtj-H1zwS-2PuWI0X2169F58yVyh-gHOWzNXxCqX5J9_92jm9bU76kZmXVGWip-RClgmcpIbcQH19Qajg4_KtPnwmQs0XxuHeJn9ZwUEPfvwP0EtsEc3KKA2PcDOmL6NCEQZwKAJOeY6xNFlJNci-kr22ENgFnLtuOmrmp57-FYLWtScJCXKmk_BHc5J6Rhw34VVGaFONPwXOLwh6f3phui7yw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd5d359683.mp4?token=bQ_QVgI0QhM78iH0Iw_7B-RPzCR_X99s4Mxzhq-2QtddSGnaqMen_8vk7r8xwPgAciTT4LPmWwRPBt7G4q_dmT9GBUDqjD1yBpquro1-IWxSZEkaGVlTbnKcuVwRPtj-H1zwS-2PuWI0X2169F58yVyh-gHOWzNXxCqX5J9_92jm9bU76kZmXVGWip-RClgmcpIbcQH19Qajg4_KtPnwmQs0XxuHeJn9ZwUEPfvwP0EtsEc3KKA2PcDOmL6NCEQZwKAJOeY6xNFlJNci-kr22ENgFnLtuOmrmp57-FYLWtScJCXKmk_BHc5J6Rhw34VVGaFONPwXOLwh6f3phui7yw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏
👈
امان پایتخت اردن
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.2K · <a href="https://t.me/alonews/136153" target="_blank">📅 21:40 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136152">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">👈
انفجارهایی نیز در اربیل، کردستان عراق رخ داد. ممکن است برخی از موشک‌ها به سمت اربیل هدف‌گذاری شده باشند، یا این یک حمله پهپادی بوده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/alonews/136152" target="_blank">📅 21:39 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136151">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
حداقل یک چهارم از موشک‌های بالستیک توسط سیستم‌های دفاعی MIM-104 Patriot در آسمان فرودگاه بین‌المللی پادشاه حسین، واقع در شهر عقبه، اردن، مورد هدف قرار گرفتند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.2K · <a href="https://t.me/alonews/136151" target="_blank">📅 21:39 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136150">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78558531db.mp4?token=iZhTPqTp8sjbX0WfwdKtQXRt1W3oyCC26lRAFRIjDMc24yQQi8CvJnTNB9PgtfjFq6H7Z-IJPE68NqORuFylrtKGqc-inTbL5Q6TJJ6t398xHfRVPwtqExsmIz0oohY27ituoRiPsmJQqTqiUlfz2S-7L0odYgi3ByIue7umtj9Z12yp0lAwDvQ7yYxbYE-rHwf0DQIJcdzfP601KHHdxIu1t_6U0KTEAxCslnHLBbZ8nhw2Gl5tq7LHzmXi87_l2FjNZcjSubRrvyVoLv53Rzkn78r3s3jAVCMuwea5kKUYbQ1OM9BW3S6V-6GMPm3DDznf0LVbsVH_En0PP-tNiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78558531db.mp4?token=iZhTPqTp8sjbX0WfwdKtQXRt1W3oyCC26lRAFRIjDMc24yQQi8CvJnTNB9PgtfjFq6H7Z-IJPE68NqORuFylrtKGqc-inTbL5Q6TJJ6t398xHfRVPwtqExsmIz0oohY27ituoRiPsmJQqTqiUlfz2S-7L0odYgi3ByIue7umtj9Z12yp0lAwDvQ7yYxbYE-rHwf0DQIJcdzfP601KHHdxIu1t_6U0KTEAxCslnHLBbZ8nhw2Gl5tq7LHzmXi87_l2FjNZcjSubRrvyVoLv53Rzkn78r3s3jAVCMuwea5kKUYbQ1OM9BW3S6V-6GMPm3DDznf0LVbsVH_En0PP-tNiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
آژیرها در اردن
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.2K · <a href="https://t.me/alonews/136150" target="_blank">📅 21:37 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136149">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">👈
شنیده شدن صدای انفجار در بندر ایلات
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/alonews/136149" target="_blank">📅 21:36 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136148">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">👈
آژیر ها در اردن به صدا درآمدند
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/alonews/136148" target="_blank">📅 21:35 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136147">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">👈
انفجار در اربیل عراق
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.2K · <a href="https://t.me/alonews/136147" target="_blank">📅 21:35 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136146">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
گزارش شلیک موشک از اصفهان
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.3K · <a href="https://t.me/alonews/136146" target="_blank">📅 21:34 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136145">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
تبریز هم اکنون
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.2K · <a href="https://t.me/alonews/136145" target="_blank">📅 21:33 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136144">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">👈
صدای انفجار در آسمان اردن
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/alonews/136144" target="_blank">📅 21:32 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136143">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d4EQBnSuQUvoKmJdDBxNsyZaYNaz3RCt49pTJzlPRXL5g9U2pCown-kmTsgB2GZdrYwefxyzSevldJSDzVWenOFJUY6fMNBssrtw1bFOibVvLn-wmivqBNQ5Wz2MZWKxiOKO8U9nBaWzQRkm1_3-rFAbwWSbdAPChos8Vhsd9e3sG55s3JTF-FO6mxU35Mu_CYZ-Wj2q2E9FLFZD2fAl4Jc8X8NRCesKpTXuYIFyooNenhTL2sEA9NHLrXH0uQS_-P58KiSiN6MI8qISYPtv18HBPJyIs3Fk4ROS30vEzbCDdgYianfqjaj-0C0-_sH-70fJrucixHiGXj2uwXuBSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تبریز هم اکنون
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.2K · <a href="https://t.me/alonews/136143" target="_blank">📅 21:31 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136142">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
شلیک موشک از تبریز
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/136142" target="_blank">📅 21:30 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136141">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">👈
شلیک موشک از تبریز
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/alonews/136141" target="_blank">📅 21:30 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136140">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">👈
شلیک موشک از تبریز
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/alonews/136140" target="_blank">📅 21:27 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136139">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">👈
کارولین لویت، سخنگوی کاخ سفید گفت که ترامپ در مراسم انتقال نظامیان کشته‌شده آمریکا به پایگاه  هوایی دوور که عصر سه‌شنبه به وقت محلی برگزار می‌شود، حضور خواهد یافت
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/alonews/136139" target="_blank">📅 21:21 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136138">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">👈
رویترز: حملات هوایی اسرائیل در تاریخ ۷ و ۹ مارس (۱۷ و ۱۹ اسفند) به دست‌کم ۱۱ محوطهٔ تاریخی ایران آسیب وارد کرده است که  ارزیابی‌های یونسکو، شامل میدان نقش‌جهان و کاخ چهلستون در اصفهان می‌شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/alonews/136138" target="_blank">📅 21:20 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136137">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">👈
تعداد سوخت رسانهای آمریکایی در اسرائیل به عدد 90 فروند رسید
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.2K · <a href="https://t.me/alonews/136137" target="_blank">📅 21:19 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136136">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">نمیخوام جو بدم یا ته دل کسی رو خالی کنم ولی این چنلو داشته باشید بدونید چ‌خبره :
@khabar
◀️</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/alonews/136136" target="_blank">📅 21:18 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136135">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">👈
ایالات متحده در روزهای آینده، مرحله بعدی عملیات نظامی خود علیه ایران را آغاز خواهد کرد - به نقل از یک منبع امنیتی اسرائیلی توسط شبکه i24NEWS
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.2K · <a href="https://t.me/alonews/136135" target="_blank">📅 21:18 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136134">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
نماینده اردن: نظامیان آمریکایی برای گردش به اردن آمده بودند!
🔴
پس از کشته‌شدن ۲ نظامی آمریکایی، علی الخلایله، نماینده پارلمان اردن گفت: نظامیان آمریکایی به‌صورت اتفاقی و هنگام گشت‌وگذار همراه یک چوپان در صحرای اردن، بر اثر اصابت ترکش موشک کشته شده‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/alonews/136134" target="_blank">📅 21:17 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136133">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
کانال ۱۲ اسرائیل:
افراد نزدیک به ترامپ از او می‌خواهند که پیشنهاد قطر برای آتش‌بس ۱۰ روزه را بپذیرد
🔴
ایالات متحده آتش‌بس را رد نمی‌کند، اما می‌خواهد که مدت بیشتری ادامه داشته باشد و ملاحظات بیشتری در مورد تنگه هرمز وجود داشته باشد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/136133" target="_blank">📅 21:14 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136132">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🔴
فوری /  تجهیزات نظامی ایرانی از خوزستان به سمت مرزهای کویت در حرکت است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/136132" target="_blank">📅 21:14 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136131">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/baac3e6178.mp4?token=r57VOpXzfo0pM1Eb8v07akjughu0diMwGG1a6MxKMYAjMmAnFq07KgtzcSs6dgubu8TEYZaI_fkFaRI2xp0cxIRonCr5QuApBMWR8jTvGi69hI46jodaJpCLegGhdtP--QxZ77qMUn08cedan7nKlPGEH3ko0cExskfyLOPcdnfFILM8_9ZNZpIvIXbFGA_VdYpNNR3ulIcHwB-tnnY8I5VkQj5cQgm2fe1hztbdxOYXVaSiqy-58wUoMynd1S0-Xmdufr2dcqo-Ov-n1K4nF21PH3GwFx7rNqWPsfFjxP4OsSjZeJDjZB2Bx7m4uLGFaCj8Lnsmb-DzvfJ9u-gUKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/baac3e6178.mp4?token=r57VOpXzfo0pM1Eb8v07akjughu0diMwGG1a6MxKMYAjMmAnFq07KgtzcSs6dgubu8TEYZaI_fkFaRI2xp0cxIRonCr5QuApBMWR8jTvGi69hI46jodaJpCLegGhdtP--QxZ77qMUn08cedan7nKlPGEH3ko0cExskfyLOPcdnfFILM8_9ZNZpIvIXbFGA_VdYpNNR3ulIcHwB-tnnY8I5VkQj5cQgm2fe1hztbdxOYXVaSiqy-58wUoMynd1S0-Xmdufr2dcqo-Ov-n1K4nF21PH3GwFx7rNqWPsfFjxP4OsSjZeJDjZB2Bx7m4uLGFaCj8Lnsmb-DzvfJ9u-gUKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مجریای صدا و سیما و دایی یکتا مثلا اومدن برن جنوب و بگن شجاعیم، بلند شدن رفتن بهمنشیر که ۱۲۰۰کیلومتر با بندرعباس فاصله داره
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/136131" target="_blank">📅 21:13 · 29 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
