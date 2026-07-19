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
<img src="https://cdn5.telesco.pe/file/S6hPPIUn8MKcCYJO4BYRBwmt2v8WL5tK-MeO3XvnJx6VXGmIvKs73K6whbguU45t3uC89LWRsADwWvhGCLvr-7UXzcgLgAY26Cv3fZl8rO4s8Y2RSHR-pviQ0uHwKQ24M16uI8EBod3zuKEw23BJvuCbYsvLEC8Oz95XDSFfFhTrLDRed85sCpNOeGHRDSuw8mgFPPwe-VHSaEdQwspRcHstzsXps6fnDbgFvoHJGpoJPLbDTsHmp3ypAalHeLnji-Eia74lpPvizKkh1LKuqSh1PTI1U9YmV85Gsv_IoUZghVoSvgHnPbBt8mRAhkZY4VC7I_5CKtrSfj9PKr1hjw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 جام جهانی 2026 | فوتبال 180</h1>
<p>@Futball180TV • 👥 556K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-28 21:20:57</div>
<hr>

<div class="tg-post" id="msg-101029">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bd6V6uP7ND8bR3e2EZPWtcb7TtgtgHE-hWB0_DpbdjWxSjuXB7KkUUUJ7H7nWbRmJdYKQhk0EkPz6tEyRLbbOcHbgIUYzofO8HB26oTt0bXnZIlZLoEkqWZvtVOY-KGduu21yWaBpP5s4drpoIbHlimy5lw--dWTiW_7yL3p-tUqsGgF0-CMju2WA4HYFMMhVl8H_M87ZPOCSlmEsa2WB3ACFUEJL9oThEhBbJiJloq0dKtD7KigGb2tgIIVEvP2_khHF_FPcpPvDnIg2-EJGEr_mdyfhp-RO56k_2tIGjZi_2LgUP4K7Qd_LIKKMVLCa3qfmm9kUqMFxpXbKwdcmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
😢
اسپید کسخل هم داره اجرا میکنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21 · <a href="https://t.me/Futball180TV/101029" target="_blank">📅 21:21 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101028">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/21f18b3a8a.mp4?token=nvh_Sn0QMGlEWxAensrsixTeI6BVQmivZ0oEv3otp4D_jtcGxXot1je0VuEJXTXAtqAQQJw2spdOqcf6fhd0Zf_fKHN0bG0Xuq_CLhtzKeZ6Otvli9mu7znHQuknDmFdfqWj5Bs7p2CcpwJIP_ZdyeuTmD6ikb3UH27swIHriUaosz17ng1108ZKOH-KA32Ztjp43Gql_-Y8eyK50iEnagk3ZNX3DuTBz0GOhlBZmipVwqJrODM048rqj3FG-Cvsdxf-OXhGLgKc04Xb3LlxoV4SOOrrCWD4mI__D1bxsSGg2fz95UJTW-3g1JLpGnEGmwTbJjXu-SM-XBBPENj--g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/21f18b3a8a.mp4?token=nvh_Sn0QMGlEWxAensrsixTeI6BVQmivZ0oEv3otp4D_jtcGxXot1je0VuEJXTXAtqAQQJw2spdOqcf6fhd0Zf_fKHN0bG0Xuq_CLhtzKeZ6Otvli9mu7znHQuknDmFdfqWj5Bs7p2CcpwJIP_ZdyeuTmD6ikb3UH27swIHriUaosz17ng1108ZKOH-KA32Ztjp43Gql_-Y8eyK50iEnagk3ZNX3DuTBz0GOhlBZmipVwqJrODM048rqj3FG-Cvsdxf-OXhGLgKc04Xb3LlxoV4SOOrrCWD4mI__D1bxsSGg2fz95UJTW-3g1JLpGnEGmwTbJjXu-SM-XBBPENj--g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🏆
گروه BTS در استادیوم مت‌لایف
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/Futball180TV/101028" target="_blank">📅 21:18 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101027">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VMsFVt6IKev5FBYF7FhoLUaRBF3c16MJ28tgY9HMuBjlw1epfHfWIe48OBw8rfoSyZlqcZLZHc1Mxcwow5cpr2hRr-gYW62Cx2r1V-sMWaG-uSaSKQkljCBIMkqs-1jcMR1TNPMMa5Hb1d3KYJI5YGwJ3ChiyuDkQKVzUPovCMbyCwo51pt3zoE_7lsARx85lieVwjzjEMqeq3jhB6oCuIKHaZ8c3vTVp2Yw_PqS_XZcb2-tFSEmQJd7VBjoetnyKfjJiarCzYCT1211wy6Y5jBr-Q-nF_kTrzSGirRGvG6sQ06utTaPlShi19k5jcCaWzpraKIeWDa42RkP0ZH7Lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
🔥
مراسم اختتامیه جام‌جهانی آغاز شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.09K · <a href="https://t.me/Futball180TV/101027" target="_blank">📅 21:15 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101025">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/klEegKutDJ_8I8rgbZ9oZuDo5T7S8xKs4gcEhoeN-wtgcYaI788yyT_XAcxrwaoZ_wYt0AhTQRGrmVsBpHBVtZssjZb8wOx6FGJ4xaFHy6Q7tz4BPH_T6rlasKAvDovFDYoIk_ROdab8tQd5C7eFrtJySUHOYgCULoNW1QwlbzDSX85wVonKCVXbwLf-19HU7-kDC8tNMQ6BD-E2FY65PVcLwryEQGmc5c2-cspkNCh3fREFoIlRP7f9n4SoY2LFbOx4vc2WICEWpZ_qDGBN_TVgFxAp-BW3K8rxkBtNksGfFP_p4xbQ0EPRZs05tnKLf55xg5kXWWQPqM1gVzVf9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
🔥
مراسم اختتامیه جام‌جهانی آغاز شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.08K · <a href="https://t.me/Futball180TV/101025" target="_blank">📅 21:14 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101024">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e_NQRKAkQPheATLaydyF9UJG9J-fs2U8TeZG8ZvKIRVJNPHRtWcWjBFctv8I0ZputnO7_BXrXRTSiXptN0K5xUGVDvE1sKrnKUC2HY0OOlQ5CAyMQ9JfQUtvBsA5es2qaWxqXybmoFjclXuOG3XMdEToMTWJuG3VmBghJP43M9570jPcp_RXTxR141LXB_Aocf6qi2JAu0zgadr8FVMAUrwPZdkgM6ywI9QsJAaIzdYznhvtsyDppUL_3zEwW5FKQUCec5-DCZ3tzi3sp46q-Tir0RD0aMMxS5-_q4bnAXhZG7eZw16Z3cuDouaK0TaoSS3sZ1qya_V7ucXAIe6CAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔥
🇪🇸
لامین‌یامال در استادیوم مت‌لایف
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.1K · <a href="https://t.me/Futball180TV/101024" target="_blank">📅 21:11 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101023">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q9FCAazLGY8R80LG2Rmf_kUCM7u95Ygbhe7juqD_rZl31JbVhOqK5D37Kny8fKkYLGb8VFc-AkwNqTJCynf-p0OTDqc6MM7JB_-Oko0ihM2G7h-qkbFkBTj3wOq36rMPRMzluzUmyyNX3Z10xcKodNdAQ2rGezLnIBw9prgysRJT3ZVxUFcDm0WWRuNEGfXs8Zw057eSqFK94EMwQkmQh1ttoFFE1OkB22iXdNbGKzwNjqk0D_TfxOfN8W9rwtitiP-7vF2BKU_CzmhpI3ZRY-AD5OiaqIXNIa9dSbZBbCTnI4WGraY0_Msk4aL6qgO_p8dbhS343HHh3NP5CAn1xQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👅
یامال گل میزنه، اولین چیزی که روی سکوها می‌بینه:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/Futball180TV/101023" target="_blank">📅 21:09 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101022">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🚨
🚨
‼️
🎙
حمله تند و شدید عادل فردوسی‌پور به امیر قلعه‌نویی: بدون اینترنت نمیتوان در پلتفرم اینترنتی برنامه ساخت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.12K · <a href="https://t.me/Futball180TV/101022" target="_blank">📅 21:07 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101021">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dTDoVFYE-pg2qFLGOYrTrf7G34XpUlc9WXSbnrlCOVgua_gtg16P0lzI2nUXIbmL0fZ7w9xfzjV6WpayyjDEE5DhAOnj_psmPL4i3YyKrIgZtOF81-nPI8UGCaI44YXWzxGMg07tKcF3Zga2Pb27wkHSOAvPGzLi-rb-oNYynyuvy_zALEeyqs5Gedwen5oaV7-nNy4RhrxoTkyb2tSjOkdWNoPAnP2RVgaZx4hnLXdkL78YC06lh504VF0o19Bve7WEJlSJmlvVsVrr1T6se082RfBK8uU7OGPPq5mWxocZc2quIfwjQvvsFaeIbYu_2PCjUwbzUfWOJiCAQWrBkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
🚨
😆
😆
😆
رونالدینیو: حسودا میگن این هوش مصنوعیه ولی من میگم این کسیه که برای دریبل زنی نیاز به وان حموم کسی نداشت.
😂
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.13K · <a href="https://t.me/Futball180TV/101021" target="_blank">📅 21:04 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101020">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/svkEnnRO0ujl6f5KkmffgR5W_gYCD1ab19YjFOmZn5kOl00aasoJbne4aPsHMi1BUOTYQ7gQAMzlcmgXULCqpxSaOKJubosI5zuI197zFmIMnwsiDBRn6N_rXSyGIzvK1uOIdjw7wU43PTbrfPKkE7YoRw8tJrW09p8IZVvXc5MnJH25quHRLBaHJmcA0ckz55ysxU4dEdqwD6KdGbS8pjGIDIbn8TB0Q5TKDuFkasDqam9Xhl8cw38LVQYGhSE-08Lm4REi6bY7nKbVF-X8Rb3V8AP-gqG9h_8Z8UslMHpmo21TWWGqquAw9gSSOBd4CAC7u64kiY-GHsqf4jVieA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🔥
بیژن‌مرتضوی در کنار تام‌کروز
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.14K · <a href="https://t.me/Futball180TV/101020" target="_blank">📅 21:00 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101019">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FMuq7-_ENlUQKR4FPjk-cG5Speek7Pv_uYqGDOmOmiqTwxKfJS1Z_yIgS7T_B3NjJ7z6Xr3n9rv9Dj1ee2MS5IQ_0KrCLTEyqXsQ1entKalNkPfEH9qY3m_bao5C1800oIs-Iuyc7GqyrAgsRYEJL3YCT1lhT80Y1bcWMY1fOG1VzuNyvufkwhqWrR7CVJNJ2tGUybK-4lHtxoUfPmPpfEiMtDCk4kusqqKRPWH0sfjRD3nNALtRMs9CnKUGX01yBOSrYlaKJqGJoLE-xPqJIiSq0V2w7eoVdp9F4cz2AsZcz5sadezfDGgSNswDN6rsKiY1wyWWOCTqgwuIz8pxVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🏆
لامین یامال، سومین بازیکن جوانی است که در ترکیب اصلی یک بازی فینال جام جهانی در تاریخ این مسابقات حضور داشته است:
🥇
🇧🇷
پله (17 سال، 249 روز، در سال 1958)
🥈
🇮🇹
جوزپه برگومی (18 سال، 201 روز، در سال 1982)
🥉
🇪🇸
لامین یامال (19 سال، 6 روز، در سال 2026)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.14K · <a href="https://t.me/Futball180TV/101019" target="_blank">📅 20:58 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101018">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ETnQYgkVv-Dg_sgZ5FRbaB1rpkZzdUGNGuDOId0n2vf28Jowm-cTDlGMZCTqKiwL67UVFySpFVokcU0LkqKMAXAg-P0osPF7XASzr2Pr4Mz2D989R_k1_8TFQ492Pj8JHKXR2aikLWrqdwyr1mLxDtrq1suYR3tDsdpuyjVO-vsu2kx1jWqPIVMUOL9rEG3D83GvujFltee8W1num_WeS7LVGpJ2Am6OaolQktpRbGEguZH6Ai6dflw0tX4Hl80ItPenHf6gdQsCm3RBgO_3w3G6pjawykwik7hFN4I7oYikl-cpNSSfeuJlR7Lh8L79vjRYKBWaBJ1VA6jcDCbUeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اوووووووف
🔥
😐
🔥
😐
🔥
😐
🔥
😐
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.15K · <a href="https://t.me/Futball180TV/101018" target="_blank">📅 20:56 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101017">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XqUgBATS5hEQCJTK1VQR_g6Mgt3e7rBhWCYlARvk61ykt88IcRol2j5zz-YsUIBOX2wndEt0RSegYaLX8KHz6bttjCImdW1vdUVfmB5oAuKGlzmcgS_1hsVc5T7sEzZMLbrfhIfqkwbwi344kETBwvr6CCm0Pg8ATGkxEgxGkPhZpudDi9IS1QgOuqQvC3K2VxdoyWOkMOM48gx0-PBdKCe-ACHcLfXHCzZzzkFUKKgCKKvACvqUWIt6_7v77XE-Sxb1Jiif-Q-zlzltzFDvPxHuSIev-JF9CotZ3oQvWwPqjeZnVySkGg7oMLDkBZxJRitafUDMpiPc239z53Djbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مارسلو به همراه خانواده‌اش وارد ورزشگاه شدن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.15K · <a href="https://t.me/Futball180TV/101017" target="_blank">📅 20:53 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101016">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TAaw_zJ6JjNfF51NtAI0lfrkeM9s1w13yA4uZycqZvDe4s9M-H7sek6Gsw8s4VuFS_g32qhh_hBhKVlFwVAJY_x2ncmEEOd-Xkog3bQFkWVfLbqZ2CAawuRiIJ8IKlJdKv_RvPOvezdxy6TSvKszrfCc5oSNnrWBb7sVDwA9ACVt_UHbqUswuYBTDRQe6R9rwdNml21i0NiiVMr-dVP4mY8QIDSLjY9nlAXc0xEJxWc0WrrAs_oaPN_RPRaKhT478DhMLk6oaQ6uvUfYOuj7NfvJ183TCujS6YPk29Hp9Q50IKEvkGq3SGepfsYZ_oOEFF0Ob-PINrw6tYzZBbIbJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بادوم زمینی هم وارد ورزشگاه شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.14K · <a href="https://t.me/Futball180TV/101016" target="_blank">📅 20:52 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101015">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5d6549a463.mp4?token=v_Y0H5qF4X1POkQMx8vK0Qa1xceNytQVdkKEt6JeZcuuAbBNxN1fsZFJvuhHN7k3GhFyTCoovknZ3_RPKxJ-KeBnzaJKOnde3X6ebmHayePdnWGctzrhTNwLwCSfUKaJLr_4Uy7LWtNoOSDtfeb9K09fIVnzlRpVi2-8iZ_-TpT6Ea5B_j5tzqDVziy2R6ikxuRIPDW-KJ0bvi4sLSg9HdPj2TgDdcQpD5qsc6jYKeeyCeMnyWNhm-9Hp482ee122PWslb8tXVgmiq5Bt2wTjR5d6eku3JWhaouLDzcb4ZYSBQeaTfC1TsT6GUiVsk7dq_6ASCHanUXnG_XJxCF4AA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5d6549a463.mp4?token=v_Y0H5qF4X1POkQMx8vK0Qa1xceNytQVdkKEt6JeZcuuAbBNxN1fsZFJvuhHN7k3GhFyTCoovknZ3_RPKxJ-KeBnzaJKOnde3X6ebmHayePdnWGctzrhTNwLwCSfUKaJLr_4Uy7LWtNoOSDtfeb9K09fIVnzlRpVi2-8iZ_-TpT6Ea5B_j5tzqDVziy2R6ikxuRIPDW-KJ0bvi4sLSg9HdPj2TgDdcQpD5qsc6jYKeeyCeMnyWNhm-9Hp482ee122PWslb8tXVgmiq5Bt2wTjR5d6eku3JWhaouLDzcb4ZYSBQeaTfC1TsT6GUiVsk7dq_6ASCHanUXnG_XJxCF4AA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
‼️
حمله شدید‌اللحن خداداد عزیزی به قلعه‌نویی: شما فرشته ما شیطان؛ شما خوب ما بد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/Futball180TV/101015" target="_blank">📅 20:48 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101014">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YM0upHvYEGQO7PaL19eI0C8ZNAeGABhAb-8zA1-Cd4x505c809thL6S-p85b2-i-vH8syFf_e0VBzuUrUu-tkBaPLbyjwVqjv4MY8dzatqsHeX8fU0AWqP89cHllKJJX5RQYRGNOmJXgtGzmNn9yn9QKXq_neBDvVKXMRCOvm-vdhv2sKwQNqvBoItAxEvwea0b6y-iCrqgLNshjQmoEH7NOMRwJ-tJHGGG81Gy_e6r-v0E-ObDhvMi0VqsBY6Mw4gio-gmHKOGpjzPrxFk0CXafWTpKnXY8M7SUI8YbEUsPyumX9ZjWpyAL_oNAAclDzTBWiMRfvca1DSCjSNte1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روبرتو کارلوس در مورد نحوه متوقف کردن لیونل مسی:
غیرممکن است ، او بهترین بازیکن جهان است.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/Futball180TV/101014" target="_blank">📅 20:44 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101013">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🚨
🏆
🇺🇸
#فوووووری
از دونالد ترامپ: به هیچ تیمی از فینال گرایش ندارم اما شرط‌بندی علیه لیونل‌مسی دشوار است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/Futball180TV/101013" target="_blank">📅 20:44 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101012">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VGtLo5_B74z4NHg92psjJYDLoHyTVhOY2WI1osGal6O-QpXs746aeWvpe_WAGC7y6wAc0fnQmFpdvxP3-3vN-HLJGNosyb58aBu9PVgAkMhFBH969_Axlh3velDcMdGg16rBl9WBYtiM2LMQ17Qzm1saOcSq9SQqCxLoiYr30bgMEtt5zeV-tju1WVGz8USQSeuuF_KkkSW9G_B12NMjyRI6u4D7a_30NX5fRf-t9fkTKhzH7p9W0Cnh0ensHPfGyy7LvT54xPOxKgIH5qb0Uw2s8lYyc-UGCj5N1zRbZKYncgDkKmzOFcdlqQOi9aw4tAqdEsiJ2IZxtBjpfYfYlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇪🇸
ترکیییببببببببب اسپانیا مقابل آرژانتین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/Futball180TV/101012" target="_blank">📅 20:43 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101011">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Olkmpb4SCAGWkw0lhKatcS_QUrn6J2xogMG8iRVbhGyQ1-BgJOnBB_XA93ysqS20Vu77eIcabQ2sfjlPhiSF1BfBM5VaDPtKdf-JrGAwql81fwAW8dPxMSIBUhYeAA3faHyzwZu8knz1jLkosbHSD7kBOsU8TN22h0D1UoUNhJqVj2tO3wTG47emx4ijR0tbh8q1WZ-C57-q4NsYTeqeOITtHbhx9Ltb5sHz2syV13s1HmyS4CEqDTaS-xcb3UesphHYz6CEUB16kD4ZivLFKhbI6epyyV1aUESD-IWxiJPlEFWcg7IWgUN5KiD6NfT4ekfUmQ8Y183mjts997IsoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇦🇷
ترکیب آرژانتین مقابل اسپانیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/Futball180TV/101011" target="_blank">📅 20:39 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101010">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JJb0VGp8n41tIs1O0M2vT3YY2BhvuBDRX1lEzq2bahGt1za3Ilmp8K8iZyua8BLetLc4xLE8lXWXMcTteBmQtxngRm6XnT7E8fIvovtsTIqatvVPECdG7HW4Egbb6Y5rxgeSZRFzisRzfnXWDTMq0pJ6TK8PJhWBV_ACPfU7VwN8SLSXPuAx_Imcit2vYhVxt-cq-d_zUS_gibivXjpSK7a4ruNaY0lF_J-mkHGxCmwUpnC0qkZwDvHA1AY9EOZ5wxVIGWaSDWqkG4hXBk8BIdHfF2NpQptkxO6-eAm3m1syeRwgB-z2g5CB9AP8eGU9_6k-UNYM0VtDr96EMndG5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
تام کروز داره میره برا فینال جام جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.96K · <a href="https://t.me/Futball180TV/101010" target="_blank">📅 20:38 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101009">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oxilG4VKMPFxmoU4ZaZ9UG1B4QA1AYcZxCNe_OGRTJQPSnZhbuJNmZjLwiAT8nJH70kOfYqYkWPngOb6U540NZA3OvLPvSl_MvDa7DegCmK7GCozMa_Qu3YBIJXBq5QfHQOeQ6fBOeFDn8eyGIv8dMm1_H65qvDF2TTiIIpWK0HA9Sp-d-yPJyv5S1KEJCoxNTd9b5EZAQ20YakU5qf0v5BWq_iBwjytJFQ_uYsQmBu1n-nJlLaEQqJG0_6NoeiwJoRQPaNcjeel1SvrLb1lPRiFXL4mXjLkfrD9mXXp92b1MqRxBXpL5t4dquePV0jSQS5PXYDCRVIQBdGaeZ-H5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇪🇸
ترکیییببببببببب اسپانیا مقابل آرژانتین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.97K · <a href="https://t.me/Futball180TV/101009" target="_blank">📅 20:38 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101007">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oPnzljksktWJd8LVytQZvP1Rl1a5dzSCqip90S6LoQC7TqmpHzPseKhFFPp6R8Eq7RwL-NfeDk-BONi3CeK3b330nYEGP2-qSCQyoPpyDMY4WeZJgbg08fFdsKL36NAVxy_1oCbPvvfq4q4aXhSI_G_7Oee9i6-djQA3YFGOo7TGkxfOdhoJBeC44dEpq3APceEgTZt_gUSO28YnNP_kZ-mhFjJ7Iy5ZgmTPA7_MP8M5cRxq10gTl2RHWDOrFCs3EIGpZdzbFR41gcXorAHHgE_MG3O9yGswRHumkvtWlvrJEXEuTETJCNe9_NZUy_k_iHv4-xgi0T27mNusb892Mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
رونالدو و کاپ قهرمانی جام جهانی.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.46K · <a href="https://t.me/Futball180TV/101007" target="_blank">📅 20:34 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101006">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k022H3ucwzE2wZmgWmqc_f0S1t4m0l_7mgC9KPs1nYkJEELolDLEvJweOH7CCH2RWaspkKgqUgQW7kyNks-wXe7bSGoXjg-UjWZr6-Xkp5JC98SEwFifJIv4zxbyPKikrFZWzniR4kd0yzHO_czV4sYqEx65Wy14PV5X_KfhlP31nFfz0nh4K56qTYIVHubaDFUkBMv4wWdrtX2fkKpBt_IhxTnbEbXnpZDJtgOiqLXTlwA1ZUFmE6capoeEpm5xvHVVWzoOC05c-c0v7iTUAg8K8yaXEK68138DLXJ0YH0yMUnQIDaEx7DkwYBfyvlIBEGMGd7okKSkUbSizab_0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇪🇸
ترکیییببببببببب اسپانیا مقابل آرژانتین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.77K · <a href="https://t.me/Futball180TV/101006" target="_blank">📅 20:33 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101005">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F478j2Cw5r9Kv6zIv89NyMF4jWg_DJ-PJ2X4if05iJlZA8emCUTT45xh6zueGLrGg2ejQWwvzfOrswR_k00S6rzWc0cThgRH6VcrrSELMcB52rsGS3DpXLXs1C_n0T0ESMoasqQGY4HjomMLOkQGqthj7RVh4XqBM-xANtYFPCH6NQne3hLdjkjehyGPoAYMsOW1CnacPj83HD4UIb2B_kdWB0LxKgXRv7w0MfOdpz71lYAO8_aqYpOwjJdp6Gc8VAUB2REdEnPs0mMXrZKZQEfJXje34uNRc4RYd_SovzFnOB7qvAFKHnvUUToimsH_lNfEOiiWW2W8QoTULRSxOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیس حسین اتوبوس به کوناته
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.96K · <a href="https://t.me/Futball180TV/101005" target="_blank">📅 20:27 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101004">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d6a399a945.mp4?token=gWgwofzwLukOelMQv_EkOt6c5y3OQB-kpHPe6QfNzRvucM2g3_pZWvBpWc57hzjT9-ectim7DSg6maaTOHD3NdUnC8QxV8pZef6bqjRwqjoHfEBDXwz7E8jOCK3VmP8h95Pf2-A0OC4Haysd4a2vXVwI4P1LuDeIOGhA2JxfHEvFhQIHEZ9hqno64JvP9k64rdkr6xfy7g7QTGbsWFtXzMDmbHTcAK2VMVpxv0iXmy5tp97S7wWTpuLJO1SMYwSIwI8nzytj5LGXyrgefr9Uxqsxq1jZMWvG-qxzkPHBd25JfQQWAxwv8-mjn9Be2kLDx_tQXIHKb71oeHc5CHwHQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d6a399a945.mp4?token=gWgwofzwLukOelMQv_EkOt6c5y3OQB-kpHPe6QfNzRvucM2g3_pZWvBpWc57hzjT9-ectim7DSg6maaTOHD3NdUnC8QxV8pZef6bqjRwqjoHfEBDXwz7E8jOCK3VmP8h95Pf2-A0OC4Haysd4a2vXVwI4P1LuDeIOGhA2JxfHEvFhQIHEZ9hqno64JvP9k64rdkr6xfy7g7QTGbsWFtXzMDmbHTcAK2VMVpxv0iXmy5tp97S7wWTpuLJO1SMYwSIwI8nzytj5LGXyrgefr9Uxqsxq1jZMWvG-qxzkPHBd25JfQQWAxwv8-mjn9Be2kLDx_tQXIHKb71oeHc5CHwHQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🏆
🇺🇸
تدابیر شدید امنیتی در آستانه حضور دونالد ترامپ در استادیوم محل برگزاری
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.56K · <a href="https://t.me/Futball180TV/101004" target="_blank">📅 20:23 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101003">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PC39b1iNoFLvxYB0IAHeUQlWTzk2U3zJZaUQZk-3__L8RCQGPY_AbFan-lUZG9ezfAfQxzWnM5P6Gk8TJT0NywBweFlZYRzpvNCsVkHqHs5Cs7Tw8u0XaKf08GFRHpFdlXE1LDbNiODHSupph6cBsbwqLWVcUqYsSH3D8xhZPKFaEwqoAdI-y6krTZwF7DQTy72pU6QC_N9s-V977OPlW2hnDeJvMYdb7pth1iow_7bevvCXgrgpRzCmVvictH4Dm3RRCplIOTgTgG8NDgmL5TOjUyenazzub9JJIAKa2ohpoZpcTktSZ8TRDhmfaDFc7j7pDEboi5z7fqbcDJnBNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
آرژانتین
🆚
🇪🇸
اسپانیا
📅
یکشنبه ۲۸ تیر ۱۴۰۵
🕥
ساعت ۲۲:۳۰
🎁
۷۰۰ دلار جایزه
به صورت
FreeBet
بین برندگان واجد شرایط تقسیم می‌شود.
📶
علاوه بر آن،
۱ گیگ اینترنت یک‌ماهه
نیز به برندگان واجد شرایط تعلق می‌گیرد.
✨
همین حالا پیش‌بینی خودت را ثبت کن و شانس خودت را برای کسب جایزه امتحان کن
https://t.me/betegram_bot?start=p10_r4EF37DCE</div>
<div class="tg-footer">👁️ 8.35K · <a href="https://t.me/Futball180TV/101003" target="_blank">📅 20:23 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101002">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KVC7Xq_UtMfAXgdWpw0z0DdXYoR6ch3VI8leaFAIxFQTI3wIWgd-jZMuNqIjCb2BuZEt7e13mIXNx57NqRYVjsaMFHtGSDe1VVroNtFHlQiTiDi2D57Q_M7Wm68QJWL8rUlhksTGGZfx4GswRRseXLK6eb84f8AxJFlNOfRQ0sT2q3pVFTqisxQN1uNsTIc-aHYQtLTHNo-E3zUVhRzU-c2cJAJIYrktjpY_EjeqB_5rkYZ2gWesTF8lM6D-YIePMDAmhWGLEo1flAF1--YoDnmq27MWIXGRks2gGnsdmM3r8kdUezQQsACt1jEikJigOil2-xRhkTGlXK6ziE5-pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
ارزشمندترین ترکیب فینال جام‌جهانی ۲۰۲۶
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.26K · <a href="https://t.me/Futball180TV/101002" target="_blank">📅 20:20 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101001">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f0WOEQv5_KDX6h5rU8s9BeMki3FOQg3Q0SRnt2Un42_cxR9aZcqtdFrGHL5OPGG5VRG3Ukr0Usb9lq3x9rwnYBw9IAwaOFNGuDSeiXhMPRSPDibpIirUQbgqsTF9fnIC0R8t4mE1RJ7If4-AddqfdQ9ITDLwTwXqs7ipxU0ep6RDACkutzkbLHaEj94cpbhCiFJI-H-DcpukeekViJwNaDdfMNvm5WyLKwkgnHz1NzD2X53h4DYeSs3cz65ta0K3mRP74gKnw9lXy4M6t48n3sn7vjkq9edyyEtiAYDeWRM8XqPI_gxeqI-Z2IvgM8nL_2tpDnzZd1V3D6ijCl7ewQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قابو ببین به به
🐸
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.56K · <a href="https://t.me/Futball180TV/101001" target="_blank">📅 20:17 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101000">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LXAIXQ2_aakPG5rD-9DgDWKH80w27g_qIMSNgQu5Nimeyq7Jfjf1m6GaqXC9fGOI0LA-XqikADawrK6hkjvrvTmCXSjJDFGH8_-aL4nO4TCIJn8UbVaLaQENRhJM13sDFBKPm-uuTmJaRVOLW0V-VpyFHdxTO_gpidKee7WdbDdTlhX9T8ytscoq5ZL0JXJJ15Kl3Rph9FNyIZ_Ka9l9eBb2XW6amVc8LA7TEp_t8_kod-8mTdpK9ZTm4UvzvL2x-bq1TMOMHdZOLN9zSXZSjuY_cO_AncVuUieoHCehxIcxsfgHVurjM3GQzw4vxuAVNCiZ8iRYLnaU3vc3CAfGag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
😍
داداش لامین‌یامال در استادیوم حاضر شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.86K · <a href="https://t.me/Futball180TV/101000" target="_blank">📅 20:15 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100999">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e5e73e748c.mp4?token=vbwWboYNOHef8u1aAuUd1YfrIJX3iT74G_5QkkW0fpQJBZU6ylA9U96hlVkz_ieosVHzTXwvRItx86zDDH3whRo37woJpXP3Ifn15fY6DC0dz2iIESxHtzp8DEs3jhc1mhokUgdjhwABupCj3z4SdOvi8zmcK80V3lVcw7YFwLdNWP1Sk_1Yq37PCOlOufzhUy4c-5sm50nk5qwD076RasFXuuuoO9rsqKnLGPshhxHI02aNk6fgqhMVP1NpDP5r1ukXsnatIdtIr2arBLgxU7neyPa-uEbRSDes85syLqYxbnGrrQleDk0pUpJjcGFh6DzktRtTKAc-qbucDMPETg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e5e73e748c.mp4?token=vbwWboYNOHef8u1aAuUd1YfrIJX3iT74G_5QkkW0fpQJBZU6ylA9U96hlVkz_ieosVHzTXwvRItx86zDDH3whRo37woJpXP3Ifn15fY6DC0dz2iIESxHtzp8DEs3jhc1mhokUgdjhwABupCj3z4SdOvi8zmcK80V3lVcw7YFwLdNWP1Sk_1Yq37PCOlOufzhUy4c-5sm50nk5qwD076RasFXuuuoO9rsqKnLGPshhxHI02aNk6fgqhMVP1NpDP5r1ukXsnatIdtIr2arBLgxU7neyPa-uEbRSDes85syLqYxbnGrrQleDk0pUpJjcGFh6DzktRtTKAc-qbucDMPETg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
🔥
𝑇ℎ𝑒 𝐿𝑎𝑠𝑡 𝑇𝑎𝑛𝑔𝑜.
🪩
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.16K · <a href="https://t.me/Futball180TV/100999" target="_blank">📅 20:10 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100998">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de520db6e6.mp4?token=ljH3GVTDTsjsRJ8vJkLth981EWOc45HaH5F_ywjH6q-qPE9p19RlVvDuSvRZacOy7oVdXNofkqCy8Hr_nEf3W-bHLxfda_wTajkEa_R7vW3paUU3Vfec9DLJ8AkK_IFJJIPOHLt_sax5aeeN7ym8KkrROBKpbbgMfILjxTyhzBpCxElvolnU8kKNIgPiaVZSOYNfQdaplh2wID5JWkw60nkOBtBK_xzGaAs_JMggnLDinp2iRmx-3lZvTAhCbXLLxvWWOzCk0Z9JupUNMJmvrLeVhtwddOFrV-f8aHNzV_cI6GKSuN9s5GwAZWLqvYV3m0ezfwv5e81EG6u5wioy4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de520db6e6.mp4?token=ljH3GVTDTsjsRJ8vJkLth981EWOc45HaH5F_ywjH6q-qPE9p19RlVvDuSvRZacOy7oVdXNofkqCy8Hr_nEf3W-bHLxfda_wTajkEa_R7vW3paUU3Vfec9DLJ8AkK_IFJJIPOHLt_sax5aeeN7ym8KkrROBKpbbgMfILjxTyhzBpCxElvolnU8kKNIgPiaVZSOYNfQdaplh2wID5JWkw60nkOBtBK_xzGaAs_JMggnLDinp2iRmx-3lZvTAhCbXLLxvWWOzCk0Z9JupUNMJmvrLeVhtwddOFrV-f8aHNzV_cI6GKSuN9s5GwAZWLqvYV3m0ezfwv5e81EG6u5wioy4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
🇦🇷
لیونل‌مسی بعد این لفظ عادل فردوسی‌پور دو بار راهی فینال جام‌جهانی شده
😆
😆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/Futball180TV/100998" target="_blank">📅 20:03 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100997">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">پویول در استادیوم محل برگزاری فینال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.78K · <a href="https://t.me/Futball180TV/100997" target="_blank">📅 20:02 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100995">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TYzHv-r5n5U0TUzmsKEFGWiQ4nJSNasfBnKS4Dv6ffJMPfGLiAVrQMkCth5LwSxgFTp8CJfZXSTUUBSEjrOR4LCryEtcLGMwT-9HwxQ7u4ikgQRvhkT3nvYTi1qmksvY9j1lf2b9N2KDEGhc67afqJjnYTGzhAdOt6Hkyy_mX8AOp2ObkY9lmWhG0OsI9BvTf3sxMeE7T6j10duu6JBMcFbOZLDa5_KXIyTII8HarSxi0Krug6JgibFlGab2-aeTipJVq4tLZMLVFHTE3AHyKcgEfgb6iOf9tAfEqg4cgQkdF_ULwrP1TzEtweAYo_uLpTvJi3HYycLCzkzYeXWD6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
تصویری رسمی از حلقه‌های تیم قهرمان جهان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/Futball180TV/100995" target="_blank">📅 19:51 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100994">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b8472215ca.mp4?token=HXbASzCADGLZZzh6b0aqFNi5HoxtNmFRCYjuW4BTrMTM3xdnz34tHw50Kogfh5o8v7Not7u-FjECe-3Rp3T4bi_VMlLbKkYRCd0OUdvkr6sg4tGHigWZat7Wr02QLtR8y_ppAWU7CCRx7xskvDQ4D2T1cV1gONimmdfiV5kwxsH_Cj-Ah7hnYx5LCXXQOCsTHN-kqiG9AZzQ5ak6EcgdYkTsBEBKNUw2X1ioKNIU8zYNPiih88s4WMugEPpTLl6Ngrsbx_bI0TvMbu_J29Tfdu3JRDahh_mdeIqR2YTUBCtyi_R8_4FRTNKijjVBjvMZagqcXfkxa8khPitfAuBa-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b8472215ca.mp4?token=HXbASzCADGLZZzh6b0aqFNi5HoxtNmFRCYjuW4BTrMTM3xdnz34tHw50Kogfh5o8v7Not7u-FjECe-3Rp3T4bi_VMlLbKkYRCd0OUdvkr6sg4tGHigWZat7Wr02QLtR8y_ppAWU7CCRx7xskvDQ4D2T1cV1gONimmdfiV5kwxsH_Cj-Ah7hnYx5LCXXQOCsTHN-kqiG9AZzQ5ak6EcgdYkTsBEBKNUw2X1ioKNIU8zYNPiih88s4WMugEPpTLl6Ngrsbx_bI0TvMbu_J29Tfdu3JRDahh_mdeIqR2YTUBCtyi_R8_4FRTNKijjVBjvMZagqcXfkxa8khPitfAuBa-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
▶️
👍
THE END OF FOOTBALL
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/Futball180TV/100994" target="_blank">📅 19:50 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100993">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rPWfX2n6TeDW151_JfzrmejKhR5qSZo3VxLjPtuPLixy3-KpDmGrw5bbf7NRT6fYl2vxBeACw8Uyqnon1-0L4v6CWWRhGCttiI3MXURxpbjqkd1kwn1axEeA-fdWziSRltOj-6IN_FqzmEvxkl17YHt_t5rDmf5qevRM-hv7xPPDEaGdARGlJeM5iCj-XAKlzOzLvaFhJiQ3O0xtIjKRjrjzdz07jYhqqZU8zk29X1F3vs8uKWYTbKHKmtILbiQoMjHX4UU3t4bwZeXQWkTNR41au3p1K-rw8naWBVvutpH1EK48zdinyQ2XxrEERbNaX5PiI_LuXixwRGGgUeAwLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🔥
رونالدو و خانومش در مت‌لایف
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/Futball180TV/100993" target="_blank">📅 19:45 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100992">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8d5a6cbf5d.mp4?token=vj2OKRf7EilW5WtYz5SgoPUPZQ-LEzFNXqZGyEuTMXZ8yF4eqOS4DJStVgQA-h7EkgIwwdDbWy17mJSnGXPnllCQdlMoyXfkkxFudjjB2xkS8iXM_U99WieQeRuoS0xVhyn-s1rYLMpWi8Ys6vHtoh_XSM0YAkhLyYKyfJYTO1ca9y2oHCUdCpGTcL4KvEpT-XQbSx58u9khHZx0J8xPbVkSUz-o7Ba_QWYP7WrX3o3gx0Y8f8DjKGetXM99nfYAm98QmZ3KXgR9c_qcZ0JX6upYfnT-6tzUzW-v0CJbIUbeP2uJ096sfv2_9f-49ROlwZOFMFwCl0Ogl8sGHVyKdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8d5a6cbf5d.mp4?token=vj2OKRf7EilW5WtYz5SgoPUPZQ-LEzFNXqZGyEuTMXZ8yF4eqOS4DJStVgQA-h7EkgIwwdDbWy17mJSnGXPnllCQdlMoyXfkkxFudjjB2xkS8iXM_U99WieQeRuoS0xVhyn-s1rYLMpWi8Ys6vHtoh_XSM0YAkhLyYKyfJYTO1ca9y2oHCUdCpGTcL4KvEpT-XQbSx58u9khHZx0J8xPbVkSUz-o7Ba_QWYP7WrX3o3gx0Y8f8DjKGetXM99nfYAm98QmZ3KXgR9c_qcZ0JX6upYfnT-6tzUzW-v0CJbIUbeP2uJ096sfv2_9f-49ROlwZOFMFwCl0Ogl8sGHVyKdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇦🇷
🤯
رونمایی از پرچم یک‌کیلومتری هواداران آرژانتین در پایتخت این کشور بوئنس‌آیرس پیش از فینال امشب مقابل اسپانیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/Futball180TV/100992" target="_blank">📅 19:35 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100991">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e_6Pb5oGWN2wCCxjNW8ajZtCDiTrCyUbrIp_RqlDiJwlrGmTpFTDOZpXH61fZjc6i7XI2ybq2c3jKOjfGObZVViwUw_bClEfU4nAIyKCCMD5Q2AGYsOoLCsjDQXpU6uKEDD1K_QmXMqgrltpQKW3AFNixcha-2Zx_D3AJQtL1RpUmwZErf73KXhPHvMtJzXGbap51o8kW0h-blvtZybOEuAqKiVEwEUDl_pdLmUdtZdSOtMCRMsu3m23KNjAJRYSw9r3kY8e0cEWV-gyi2p16-7GkCb63iyYVx9GRIQgmdomNwpoQMJW_g2JZ2XUj3SCcETuyX7b3f09YDiNEZC2rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حضور لواندوفسکی در ورزشگاه مت لایف
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/Futball180TV/100991" target="_blank">📅 19:28 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100990">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c65e3eab6.mp4?token=Sc9h3wECsoBOmzSopXrNs4iYyTMLUhcc7NxhY0gRXAdVrz7D2mkMCQCNNGHCCnbAtidhTOEjG362IHPZYYlrOygQWM5oQPzAC6Ru2IJ1n3Po6DINHpaOka2a7MULtU8kIFIbVnXT62WV_MOqD-Zct_OR1vwC0mUprrCdXwFcFrKGX15-M9-wV2yKEV1Bsqc-GX_dg5g-m6R4wLqqFZKfqu6Q5vr3wsRRvwVkmtgrCCGtrjzNHhkF-EACzN1VmEDWtIo6o1G-Gin5D_rVy9uZnYI6tlUrW-qlQu-AD6ZIZpW44yY_RbHwuEHoWzAg-Mab20aQz5B-qBkHkRCgpt3CCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c65e3eab6.mp4?token=Sc9h3wECsoBOmzSopXrNs4iYyTMLUhcc7NxhY0gRXAdVrz7D2mkMCQCNNGHCCnbAtidhTOEjG362IHPZYYlrOygQWM5oQPzAC6Ru2IJ1n3Po6DINHpaOka2a7MULtU8kIFIbVnXT62WV_MOqD-Zct_OR1vwC0mUprrCdXwFcFrKGX15-M9-wV2yKEV1Bsqc-GX_dg5g-m6R4wLqqFZKfqu6Q5vr3wsRRvwVkmtgrCCGtrjzNHhkF-EACzN1VmEDWtIo6o1G-Gin5D_rVy9uZnYI6tlUrW-qlQu-AD6ZIZpW44yY_RbHwuEHoWzAg-Mab20aQz5B-qBkHkRCgpt3CCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
قلعه نویی بعد از مصرف سوغاتی‌هایی که از مکزیک آورده: 6 میلیارد نفر (دو سوم مردم جهان) بازی‌ها و اخبار تیم ملی ایران رو دنبال میکردن!
😆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/Futball180TV/100990" target="_blank">📅 19:23 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100989">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/06a5c4e4ac.mp4?token=Wj1q0yGOlPVSkyWdxZd5qxfHm7m4BOtgccWdL6dk1WRXnTGYsjul0evtvic864QMHclTy3n9YR2WE5R2WnaJbIx0MrDaCUpTGIyGvVIzNYW3sYRDaoLBWJHzfyNkuRUXq8FF2ShwY_j5yfGsgnFXU5w5hzEUQPcICU6WY_iw3GPE3Z_CZABWAn5C6cmFc6-4PddAxvopsXxqq9TwCYpiyki-BTukBN4_ehxvbRDeKMSygp-ERY023igCPXjM4iMGBjCyCy-zn0aZ9kMi-uFfltfixR2djhlPPLQk3G9rZ-vq4HteXDD_wMuEW2gEbgkG01GvgX6-ueZYUK5k96-K6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/06a5c4e4ac.mp4?token=Wj1q0yGOlPVSkyWdxZd5qxfHm7m4BOtgccWdL6dk1WRXnTGYsjul0evtvic864QMHclTy3n9YR2WE5R2WnaJbIx0MrDaCUpTGIyGvVIzNYW3sYRDaoLBWJHzfyNkuRUXq8FF2ShwY_j5yfGsgnFXU5w5hzEUQPcICU6WY_iw3GPE3Z_CZABWAn5C6cmFc6-4PddAxvopsXxqq9TwCYpiyki-BTukBN4_ehxvbRDeKMSygp-ERY023igCPXjM4iMGBjCyCy-zn0aZ9kMi-uFfltfixR2djhlPPLQk3G9rZ-vq4HteXDD_wMuEW2gEbgkG01GvgX6-ueZYUK5k96-K6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
مقایسه میزان فالوور بازیکنان آرژانتین و اسپانیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/Futball180TV/100989" target="_blank">📅 19:20 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100988">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b8422005d7.mp4?token=jqgStkh9gpoDlKNeiD97dxa_asBHAB6sFKW6Z6GFHkntaI70mYiSqwesX3SQi10Pnk-eEqLNPGCSEo83KTnfOwZc7PqLhWCOc1omgEgnfSczVDAqCSGjCeav5X1nQthIVwblQgzIr4Px5ugPGCakgzW4ulonMBm-s6A4j4AylPzZEPq2neMCRh6Ww4TioRh8-an_ITsRmNVDKByd9cHg1zmQWvR8TmHOzJSPoEQI7ijZbItb-kBJ9J6sjFQ6azN_ty7QSgT0JizHjJ09xUj2WF9H3QbMpwYcfEPmpOlukZMz7QZbC4D3H5N-u3-eOkbwEOegD86WmQG_as81Bp4gmA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b8422005d7.mp4?token=jqgStkh9gpoDlKNeiD97dxa_asBHAB6sFKW6Z6GFHkntaI70mYiSqwesX3SQi10Pnk-eEqLNPGCSEo83KTnfOwZc7PqLhWCOc1omgEgnfSczVDAqCSGjCeav5X1nQthIVwblQgzIr4Px5ugPGCakgzW4ulonMBm-s6A4j4AylPzZEPq2neMCRh6Ww4TioRh8-an_ITsRmNVDKByd9cHg1zmQWvR8TmHOzJSPoEQI7ijZbItb-kBJ9J6sjFQ6azN_ty7QSgT0JizHjJ09xUj2WF9H3QbMpwYcfEPmpOlukZMz7QZbC4D3H5N-u3-eOkbwEOegD86WmQG_as81Bp4gmA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب بلینگهام داشت بین جمعیت دنبال دوست دخترش میگشت که راجرز اومد بهش کمک کرد.
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/Futball180TV/100988" target="_blank">📅 19:05 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100987">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/32720018d2.mp4?token=thQjFVeFZSBFftfo4cDbEqcIMIixouGDI8fwC4BViqce7dPr2305lQV4zfr3SD5hUt_xaymfwdxphgKrW5a_Bor6-J5zbzvXVsv7qxgR-N9qWtvYjv1iB3Ipnh0GHpaFkKUcKI6KHtE60-ruI9-QdOUJYb0SiNC2i7adlI-62Q1qpjzAxnNL70RjhfMj4UDeW4yVZRWYe7sFTmd2U41xUkz6dHyAyI-A2ZtCJgX5yoFeycdfbOTXDNL4YuWHSP4jyJE9CKKmJhvD-VmIsmEs586j-6csdIadO3ODtdM3MGLhoyGh_0I1kWtr95uZfi6lHzIS64VBNCDMqHcZswn6_ksW9bIXN2MqklkWYnAvYAEdAdRotcyd9KG1eQz47aT81FoG0eZfeL9PQ0uH8zTbP5PJbPuhI8fEF0TRzvW6Lni7YtblCJPFWRkur6llNecrdcW2C6eBiUEZol4Ugl0PSQTJ3yM9_4nKCvt2U_dCfTzpdMD1IBpkByoOdsu8CdbZsyfeseU4eqnSlETr7aC-gyCPuQ1XD2iTYGywg-EBPJmW1h8oJ7suIZI7RFiGZb1DSHhsgBRC0aOiolwJnKBHgHKETNMbe5_3ARHdekZgJyv1-NSlqpIZTgbUMdFxivy4hU53Ci552BKr-P3icbJhZsGREK0esPHgGUD03ayFDww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/32720018d2.mp4?token=thQjFVeFZSBFftfo4cDbEqcIMIixouGDI8fwC4BViqce7dPr2305lQV4zfr3SD5hUt_xaymfwdxphgKrW5a_Bor6-J5zbzvXVsv7qxgR-N9qWtvYjv1iB3Ipnh0GHpaFkKUcKI6KHtE60-ruI9-QdOUJYb0SiNC2i7adlI-62Q1qpjzAxnNL70RjhfMj4UDeW4yVZRWYe7sFTmd2U41xUkz6dHyAyI-A2ZtCJgX5yoFeycdfbOTXDNL4YuWHSP4jyJE9CKKmJhvD-VmIsmEs586j-6csdIadO3ODtdM3MGLhoyGh_0I1kWtr95uZfi6lHzIS64VBNCDMqHcZswn6_ksW9bIXN2MqklkWYnAvYAEdAdRotcyd9KG1eQz47aT81FoG0eZfeL9PQ0uH8zTbP5PJbPuhI8fEF0TRzvW6Lni7YtblCJPFWRkur6llNecrdcW2C6eBiUEZol4Ugl0PSQTJ3yM9_4nKCvt2U_dCfTzpdMD1IBpkByoOdsu8CdbZsyfeseU4eqnSlETr7aC-gyCPuQ1XD2iTYGywg-EBPJmW1h8oJ7suIZI7RFiGZb1DSHhsgBRC0aOiolwJnKBHgHKETNMbe5_3ARHdekZgJyv1-NSlqpIZTgbUMdFxivy4hU53Ci552BKr-P3icbJhZsGREK0esPHgGUD03ayFDww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
ماجرای پاداش دادن روسای جمهور به بازیکنان تیم ملی از زبان جواد کاظمیان: به ما پرشیا دادند و گفتند ۵ تومنش رو پس بده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/Futball180TV/100987" target="_blank">📅 19:00 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100985">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KGy8vlkGeZJeoNIQ36eeKOpn4UdDN_-Ezl--zAU4mi-00dAkiPOXTySH-8L2dLvUgAxKzGxFuXxgNZ357D6Vj9DdbKXzhr8OENbr_3RlNRwMHt74jkr7ClkU7pguh3jkjnV2yJbUB0F04frkhq9esIDmUMqC-04lMNUuYQl6q9dc5qv_LLD1ZhtBbR2YHqc3pp95zi9jy43Zex1Pa1ffI-Rr_yK2kmpMwh4WQnsbnCNZLO1jqgKok9CYEs2sjq5xE9LmkPsDepZKhJXHFlt4m2PPxmLgv0WSqWxoPsxLR4ifclQnpv8GMkJdO_JTajDbwvlTmetzv8Ta4mTnqJ6CMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aRzZyhBSKfrUTwbY6CEam06842bmJ8c31jfjd_OS4BkAFxoMwWS45dHzTfsYFt_2xOfzk5eCAsy2ouP4067h0skXeOJ_6ge4vBTJnOByTRNNbX8rzflgM2sbPhrNF6gCCni56gR6j1nFOFJtYdEhfboGICvcoIURR2p1KAfTw5LEWTyeYh3BeviuIDE2BIlb9a9x-rQ6KWQgJJPAn971GJ67Iy3n4d7WEU3o7F70Bv59yRWf2IeH175XStdoAbyggYcWJPWCZh1GWI4JVwZ7xWYxrW0JqpTGp65B_-wmx7VWEhFk7LxcceVCV5FP_1AHrI-i5zCz74W64GSyBDsytg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🏆
🇺🇸
در طول پخش سرود ایالات متحده امریکا ، مانور قدرت با اف ۱۶ بر فراز استادیوم مت‌لایف برگزار خواهد شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/100985" target="_blank">📅 18:49 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100984">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
🧾
امکان ویرایش شرط ثبت شده
💥
برداشت سریع با کد پریمیوم ووچر
💵
شرط بندی بدون محدودیت، بردهای نامحدود
🎁
جمعه و دوشنبه‌ها، شانس بردتان را دو برابر کنید
100% بانس میکس ورزشی تا سقف 30 میلیون ریال
🎁
با واریز کریپتو، سقف برداشت خود را به سطح جدیدی ببرید!
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
••••••••••••••••••••••••••••••••••
💠
لینک اخبار و هدایای سایت
👇
👇
🔸
https://t.me/+ioIBrQfqMLtmMmEy</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/Futball180TV/100984" target="_blank">📅 18:49 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100983">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ApwyV9wdbHwlafr1CMZD-Rl-sJAjoixgJ_LwjxWSvS1oXPtp8JsiRVpBsmpn95ayu-5o6RRmxm9_ukYOEjbMpASo-x_5p2gI6hGemuKDLhM89P9Ov_Y3lamMBhWB_2piubwgHYvv8Q4y4p4HGkhatYiReMdsuq8eb79-MzgWrHa0fC8WP5qIr-UEQsou4-XkVzE5goREXJGyP2vwQKS_EFzQIUUM1jJzb-LuPL0Vzm4pRdwzs2ixUYbf9HuAPZ5wfvG44XmtKCYtONlYci6vZ4Ym_ej2EwhACzdX3avq7gnl272oMyxjnI_9TZN_exYOK4QjfkxN4tilYiOXctOOEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
فینال جام‌ جهانی 2026
⚽️
اسپانیا
🇪🇸
-
🇦🇷
آرژانتین
⏰
شروع بازی ساعت 22:30
✔️
امکان ثبت پیشبینی با مبلغ نامحدود
🫰
محاسبه نرخ دلار با قیمت 2.200.000 ریال
⭐️
فرصت استثناییی چالش‌های پیشبینی فوتبالی سایت یک توتو، با جایزه 500 میلیون ریال
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
📲
@yekbet</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/Futball180TV/100983" target="_blank">📅 18:49 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100982">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/42861ec48d.mp4?token=gCo0-BfBhckobI8GNBFQ0gYWnnd74kzyWIfCrIaLf6lxFFuo-NFY1d_-n3H1sS3aKluGefk0yKBbMnO_cWQApL6AB4wo1Hr-b5dkIm4751V3dFsjN-HmRiu0nUsdRvSceH-Ugcy-Bqs7EwEwxlqNRd0bbHyCsblrFxXrHFwyGdsgwwGkJwDK8n6gUBduCjd_-ZF1t5MARKzWM8-6nBejJpQAx3nrdwX65zEoJteDtM0j7d4l8e6d_foR7a5kFgd49P-GK0puo-Ml05-78j9aDA471U_KHz75jOXENdZPWpP8pRV5bp_2YFWsEHYEo4aAdL7M8J83vN98k160wBiqSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/42861ec48d.mp4?token=gCo0-BfBhckobI8GNBFQ0gYWnnd74kzyWIfCrIaLf6lxFFuo-NFY1d_-n3H1sS3aKluGefk0yKBbMnO_cWQApL6AB4wo1Hr-b5dkIm4751V3dFsjN-HmRiu0nUsdRvSceH-Ugcy-Bqs7EwEwxlqNRd0bbHyCsblrFxXrHFwyGdsgwwGkJwDK8n6gUBduCjd_-ZF1t5MARKzWM8-6nBejJpQAx3nrdwX65zEoJteDtM0j7d4l8e6d_foR7a5kFgd49P-GK0puo-Ml05-78j9aDA471U_KHz75jOXENdZPWpP8pRV5bp_2YFWsEHYEo4aAdL7M8J83vN98k160wBiqSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
هوادارای اسپانیا: مسی بیا اینجا بخورش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/Futball180TV/100982" target="_blank">📅 18:38 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100981">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OVL85NYyq_oQQ7ftyCSlTepW_gu9voqH8ryerzRwedQLFOnI7-zK95l6zxMuOKE4mATXg-LTtQWo1MpxnnZJNmiCf2BGwJJzopK21UL23KFooKkX7ACra_Xkrg3roiUMjKrxPIwyEtKLHKDB1EdtwRJounknV9-hFzRIeUIUv3efviNuqgmo3NdLPoPV5rTnAau00LEo7hkSVBOITjZF6ZEnrLT9G0QbRBCX4dAIU_rBbvHIUwqo70p_GGepYy7US8OdQQvi8thON32TfBSeUf_a3UsYaScn0oiOZi-hkU9eoeWNSxdIsz3BRYOqgm40jacwnCtBgWyo0I-EFBUzLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
📊
👀
هر بار که جام جهانی در آمریکای شمالی برگزار شده، قهرمانی به تیم‌هایی از آمریکای جنوبی رسیده است:
‏
🇲🇽
1970 | برزیل قهرمان شد
🏆
🇧🇷
‏
🇲🇽
1986 | آرژانتین قهرمان شد
🏆
🇦🇷
‏
🇺🇸
1994 | برزیل قهرمان شد
🏆
🇧🇷
‏
🇺🇸
| آیا آرژانتین قهرمان خواهد شد؟
❓
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/100981" target="_blank">📅 18:25 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100980">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/631c2acef7.mp4?token=kAkYnpMQLBW_k3vP876xynEaodsEdCaXunhIHatRkJWY1seJQNur-wpBkLd2kj0XaUreI50S3GRFg3ySyg-U3SHmjVYRCpUM--w3JqNH7qGNO8FBE7kq3XhT5MIvVztHK5ngzRCIU6R8mdKXcgJgsbpBf-kvIO0BojhHQjO1M2f3S1kl_dqK6ucwjHT2D0NlUN-jdCAZ03VKR65NwDRGlwzNJrMdwx2UObZTHH-glVGaZ0xVxIko3SvY5I5znteJe_m5TRhvGws-imUg41g9qf2mRWElgN0n3ofn0NatC-ap-rtcqXQreCyFQk3REb5DdFdBNerng17wTEXkbQ0kaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/631c2acef7.mp4?token=kAkYnpMQLBW_k3vP876xynEaodsEdCaXunhIHatRkJWY1seJQNur-wpBkLd2kj0XaUreI50S3GRFg3ySyg-U3SHmjVYRCpUM--w3JqNH7qGNO8FBE7kq3XhT5MIvVztHK5ngzRCIU6R8mdKXcgJgsbpBf-kvIO0BojhHQjO1M2f3S1kl_dqK6ucwjHT2D0NlUN-jdCAZ03VKR65NwDRGlwzNJrMdwx2UObZTHH-glVGaZ0xVxIko3SvY5I5znteJe_m5TRhvGws-imUg41g9qf2mRWElgN0n3ofn0NatC-ap-rtcqXQreCyFQk3REb5DdFdBNerng17wTEXkbQ0kaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❗️
▶️
صحبت‌های تلخ ابوطالب
🖤
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/Futball180TV/100980" target="_blank">📅 18:20 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100979">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/SaMa7nQ96r5ERae2kZZGPkApyAC2xt8eFBNOs8sxpEGN8SMr7MZndFK3yXn4rVJmcPNA72sXJqymoydOC7efsA9PAImjjDKcxEHdpRSdumMdrnFZGEUzvWJC8vWo83URsnWEeUfuwJkAm7nWT-ZZ5OZC9r7WMV-VNuDb0II-k7xdelIYGP3HxugcMV53sAyT6YOm6zJToO1mPv12VZboCmgSr0NSP7FjOB8wqSNsgeMVRIE-NOu34hII-dCRKywoKiJtb_2t37Pb73nTH2vnDASe6BrONyDlKZFafNN5aQzmFd17sA4A4W-X1CNGl6ART8TzHFYR6FzIzhoi8EAr2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
آمار لامین یامال در بازی‌های حساس (تاریخی):
🏟️
• [6] بازی
🔥
• [4] تاثیرگذاری
⚽️
• [1] گل
🔴
• [3] پاس گل
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/100979" target="_blank">📅 18:10 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100978">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MFj_rMoxxhxsm14Z8Q7r1P398PtYb9-ZwVcBEsBcCsD615DcqnImqfERo1k6uukWbRmMxNhOPZzbqXs35M9_g3eUWQwiSwKeKC90ckBwlZwmUa_MxuOciH8jA8dtRFEhZE2Iou3iAw-EXrx1JUegCUjXyIA399zbtSDTObp6lKcqdyAA0WAEVUI2Nv2tey1WxJbqpXFwnVdlLAneAzTli8toaJuWJNCygOMNV9riaCYv-AXj2s5It7HGfO9ulGWozsHobgByYVFbktwImnXxG2PCdOxvyWMr1IIzDVfisu7rmsmW_gwEqOTKZ6odXHCazjDE9IIJLj1mpE1g_sNpDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
👤
#رسمیییییی
و عجیب؛ میلاد محمدی مدافع سابق پرسپولیس با قراردادی یک و نیم ساله به  مکس لاین ویتبسک بلاروس پیوست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/100978" target="_blank">📅 17:56 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100976">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/h67Q2Z2P84f_e4uU8DigdizZRF-fVGGxE_NlB4qKX7xJXC-M0HN2_azbSwiSBUcXUWM2AZ1o9aVhxnfvLr-jB_h-2OlAxjN_QHzGT3M05MUYDP8_p_q6VqD4WNC3MNcPJCeYYVJrREWyN8fS0dPajZHCQqJQaVAVhyjuqcobFeqiZoi4wubrzlR4uLH2XUFTAIjc4k8GiQYmzqhrIkiGcHstXwe0y7OoGl2FdY5hOpt_PTo7qjfgZ-sgZ_wczwblArs_l9xcAKEPe1dAnPzyRPPq1mP2E5yo8iLQmieVILz3Y8TXyYY7eacZ27i0ZbUJFoP7xglXnfsB6Ed_2KqEaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/A8LfuZJn4PzehkOh72Of7GJwoU1GqJWqsgcuc_zXUgOgzGaeHjJK7k1TG_LAPQlp6YqCnhVZ4oqyJd3l8UApB7TSiHOe_reJzHwOzP6eu_C-mRJwymSQl0uO8nQ9Y6CDXgbQO2k4hbkJwQ_V2-0d5UjcrHLBH4SezwlhlVSgKfRG086bkRI3aNJj-VZZJ4Ys1QsZr62VvNsgK6FyQcF9gg1rv41t2rsj7ZM9AJN3aWB47AvYOFDWEuQDNsZlcBLIotkxUELF5LKZsnRpWKaLty_K2wBuFECeHytqM5wn6k2tkKkLpuDvRUqwo7EKET1Cu7705032hXsYIYeIyyZxXw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‌‏
🏆
🇦🇷
آرژانتین در زمانی که به فینال می‌رسد پس از پیروزی در ضربات پنالتی در مرحله نیمه‌نهایی:
‏1990 | در فینال شکست خورد
❌
‏2014 | در فینال شکست خورد
❌
‏
🏆
🇦🇷
آرژانتین در زمانی که به فینال می‌رسد پس از پیروزی در وقت‌های قانونی در مرحله نیمه‌نهایی:
‏1986 | قهرمان شد
🏆
‏2022 | قهرمان شد
🏆
‏2026 | آیا قهرمان خواهد شد؟
❓
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/100976" target="_blank">📅 17:40 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100975">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B4GbtTmU5g1hG1uaTrQOUlwuFhDum5VZw1beDgCM0yIokN9qWAT2F6bAHAB9prIAvuiOf-Cjz7jRd40li0ibxe3vwo-X5U7h9re2DoRAIohm6Ch7UsJ-RCAAmTpj01ES7g8Emz0XwCtKdJLitkgEbWy0Tc1O1tEudXuV0uGahLpm8ymI3m0lzEeyBswSffM1jihcLxvpGfXJHpYQxJnRHhR7YwcEwKAHBtDdK3GP9dLgu-2jR7WIuSxow8vrVDNDIBh5mCq1Itk_lD-tPM_8ZqUJxZai0NhNeWIZMm3U7KA8VGhLESgVFh4Jpv7oxUwe2s2M6YxHZLi5NM9cdZ5Wog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚽️
توضیحات مارکا از پاداش‌های جام:
🏆
قهرمان: [50] میلیون دلار
🥈
نائب قهرمان: [33] میلیون دلار
🥉
مقام سوم: [29] میلیون دلار – انگلیس. 󐁧󐁢󐁥󐁮󐁧󐁿
مقام چهارم: [27] میلیون دلار – فرانسه.
🇫🇷
خروج از مرحله یک‌چهارم نهایی: [19] میلیون دلار.
خروج از مرحله یک‌هشتم نهایی: [15] میلیون دلار.
خروج از مرحله یک‌شانزدهم نهایی: [11] میلیون دلار.
خروج از مرحله گروهی: [9] میلیون دلار.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/100975" target="_blank">📅 17:20 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100974">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NzFdvwavg4iUQA9itrU2aq3aT39fAFwj2wqvcEduDnCx4COpsqM2KQP3nXzys4ow9iRYE_wGVdIFbB8wCZXPUt5J2hGl6mNr1sx2zDT_VW_PMT_YdaEjw14sV2IX0SYZaFi6YkxdwfWE3Qb4Jj76EceegbwtkgX0gIf1Gi0FSPcfgZUNEBbsdZ0oB175H3zCUH0NKAqNbqk5ZeGW19KqlwP3za8WREnUhuyDNFLlaN2BL6ER3ioyx2LghSjOx6gAzazu2juN1FkSlZwNTMzwwSw89Q4k_L4-8A0STSUUcvnEcDsB7ERYG03rT4l7WXkroweWl6AVRs78CHmYMdKqCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
🖼
پیش‌بینی ابررایانه Opta از فینال:
🇦🇷
پیروزی آرژانتین در ۹۰ دقیقه:
۲۶٪
🇪🇸
پیروزی اسپانیا در ۹۰ دقیقه:
۴۵٪
🇪🇸
🇦🇷
کشیده شدن بازی به ضربات پنالتی:
۲۹٪
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/100974" target="_blank">📅 17:09 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100973">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fcb3c56442.mp4?token=EJOxEb8RrV21gb_z3RcYJs_Ug6IS2js1cd3YE7JL2jJXsl9UDGC0lmI8c6o36HL3fBHIWc_PMTyArlCxXGUv9PBR2Nyt0G_ZaxTZ3aa84ndCwYRYicnIM5kajfPBeY5GsIvwWJbSatD_Ln5zNIALPyA4zZT3V9qvlJnuWNvZeOE2GHvYI1T_3iKted4VIeHtOZ4Djzhsid1Z9tP8LixHXu2TtueJJKASs1PnPfqLDUY4PltDI5inV_uehMYulbzACdpCG48eOAmSIX9VsrRJV59Rc7Bl1hTaTyzUvXGfN8Eaa7Lgz9DFwBH7d5NzdccZZUfQ_DJLRJRaH4J_2sF8Rw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fcb3c56442.mp4?token=EJOxEb8RrV21gb_z3RcYJs_Ug6IS2js1cd3YE7JL2jJXsl9UDGC0lmI8c6o36HL3fBHIWc_PMTyArlCxXGUv9PBR2Nyt0G_ZaxTZ3aa84ndCwYRYicnIM5kajfPBeY5GsIvwWJbSatD_Ln5zNIALPyA4zZT3V9qvlJnuWNvZeOE2GHvYI1T_3iKted4VIeHtOZ4Djzhsid1Z9tP8LixHXu2TtueJJKASs1PnPfqLDUY4PltDI5inV_uehMYulbzACdpCG48eOAmSIX9VsrRJV59Rc7Bl1hTaTyzUvXGfN8Eaa7Lgz9DFwBH7d5NzdccZZUfQ_DJLRJRaH4J_2sF8Rw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
🎙
ماجرای جدایی ابوطالب حسینی از عادل فردوسی پور: ما به خوبی از هم جدا شدیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/100973" target="_blank">📅 17:04 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100972">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7f39f39ffb.mp4?token=SV0V0CNquX_plm1b_IIHZ5Xu0d6_WmNDHuXKzsEUZiDOu2c6hlx1mCBZ8VeRx-NvZGc3JtVK03q49zfrnUH8kjmAWpvBGdU7IW7qikV8gXITf_IH1QBRjJ6UV6Uzj-9vQ_VFw10QscAMSQPrK4JhRm2zvZPf37WC8HORpEn-uEwOYnxl-FUH2dqLnssADDxPm_byKMXn3UVQnkPjAURvq1l6CC1hPS25lbHVeDOZG4VGAjfckHrV8nEids8TdV6oYuVhjarQularFb6Sa8gxkwEkp0tHPZtaxcOiiBmsbpvj4AS_hU77E4-5XN6CHIs9Leqy8fMzoKf6mj0ZojoL7b_ZsalU8EeQwp7YPVM05p7lH8cMTNqz1H3BOAf0Rt0E7DEKztTIFEicv7FsV9-EQcvAbvSqDSd2tZ53f_umzhEIK-C9INvGB-dU3fX7n0GOCHuzB17je5OHePppAvI-WVQtJSLHBVcm51msY-q_xshDsg4y8__WK5aa18hCAnbCoZ_ONW26DKY2MpIbY01Y1_Q299zVjo4PjtN7vy8BdRJLvNvo5lNDwOIABz5LejqBsY7WRrubhzQIy8NSF-1X6s2rQCzhimm-OGhvBNV54SPQE1FLVqHB7A_rQBW_fhuf7tasCfrKxsKjfGanue9F208NNhzUSjbbj1k3e6TQlM0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7f39f39ffb.mp4?token=SV0V0CNquX_plm1b_IIHZ5Xu0d6_WmNDHuXKzsEUZiDOu2c6hlx1mCBZ8VeRx-NvZGc3JtVK03q49zfrnUH8kjmAWpvBGdU7IW7qikV8gXITf_IH1QBRjJ6UV6Uzj-9vQ_VFw10QscAMSQPrK4JhRm2zvZPf37WC8HORpEn-uEwOYnxl-FUH2dqLnssADDxPm_byKMXn3UVQnkPjAURvq1l6CC1hPS25lbHVeDOZG4VGAjfckHrV8nEids8TdV6oYuVhjarQularFb6Sa8gxkwEkp0tHPZtaxcOiiBmsbpvj4AS_hU77E4-5XN6CHIs9Leqy8fMzoKf6mj0ZojoL7b_ZsalU8EeQwp7YPVM05p7lH8cMTNqz1H3BOAf0Rt0E7DEKztTIFEicv7FsV9-EQcvAbvSqDSd2tZ53f_umzhEIK-C9INvGB-dU3fX7n0GOCHuzB17je5OHePppAvI-WVQtJSLHBVcm51msY-q_xshDsg4y8__WK5aa18hCAnbCoZ_ONW26DKY2MpIbY01Y1_Q299zVjo4PjtN7vy8BdRJLvNvo5lNDwOIABz5LejqBsY7WRrubhzQIy8NSF-1X6s2rQCzhimm-OGhvBNV54SPQE1FLVqHB7A_rQBW_fhuf7tasCfrKxsKjfGanue9F208NNhzUSjbbj1k3e6TQlM0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
⚠️
امیرحسین صادقی خطاب به علیرضا بیرانوند؛ به بزرگترت احترام بگذار!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/100972" target="_blank">📅 16:40 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100971">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/abd765fe00.mp4?token=DV4hpkIIFdskNwVE7ykqVjmzBFPzyLEMQe_tzBZJPhKEbSn-JWqR3Uo5-dc2DAD2cy7BKnmy-ukNAfiSWM8z7Ccb070a6wD6YGObmOjwxy2jcUFmKmt4lY4nu5Gf92Uv3acUbDW21yx6GodtwpcyIsXRxz0JS2yY3NY-TlCEZ_qzTb1SA0Yn7y_L5qvgAI8G23AkCXjdbLdWGep5xa-AoUyflUl9KihBxMAPv9yc5fTcLE3vsZj9rVyLYCGBJ2ujuyQf-13zQ0GJ-d-DlE6vk3agLIM6sxUsRsw8Heevh67UMkmz-pP7Y6UhN-KnGr5AwSiFDirjv8sHU89MeHmRCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/abd765fe00.mp4?token=DV4hpkIIFdskNwVE7ykqVjmzBFPzyLEMQe_tzBZJPhKEbSn-JWqR3Uo5-dc2DAD2cy7BKnmy-ukNAfiSWM8z7Ccb070a6wD6YGObmOjwxy2jcUFmKmt4lY4nu5Gf92Uv3acUbDW21yx6GodtwpcyIsXRxz0JS2yY3NY-TlCEZ_qzTb1SA0Yn7y_L5qvgAI8G23AkCXjdbLdWGep5xa-AoUyflUl9KihBxMAPv9yc5fTcLE3vsZj9rVyLYCGBJ2ujuyQf-13zQ0GJ-d-DlE6vk3agLIM6sxUsRsw8Heevh67UMkmz-pP7Y6UhN-KnGr5AwSiFDirjv8sHU89MeHmRCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🙂
جواد کاظمیان: وقتی فوتبال بازی می‌کردم گونی گونی نامه از سمت مردم دستم می‌رسید که ۹۹ درصدش از سمت پسرا بود و نمیخوندم چون منتظر پیام دخترا بودم
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/100971" target="_blank">📅 16:20 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100970">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d154ff4095.mp4?token=HvQmVh0Nc2agS08j_0zcRWESAOFB2vWv4T5TP5lWvT0Y0Cj-cxQd8gt1IMvcFpvW_n_cujoZZ8QpMbRQPug1NdcRXBhIGQwqeoMvFd2DjUBG6uhowjJKVcdyP2hJhsSbaVU94QKVwCA2uw-BwL_4iee2CnANd02nyNuyN2Ny-2lCagTKgM0xmuqE6PREISETt3blUo3kxFmaLBKsQfYl6pd8hK_qPjEhH_SeeGrV6womtOsy8sF0hbRPtWdhAJIhZynAYkTBMD_y2HRGpg92KRtktMC0mTLvMqPBHvznbCryVkdfNVEi8YlT4nZLnjksciyFUBpZTrrMqeF0rzcd4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d154ff4095.mp4?token=HvQmVh0Nc2agS08j_0zcRWESAOFB2vWv4T5TP5lWvT0Y0Cj-cxQd8gt1IMvcFpvW_n_cujoZZ8QpMbRQPug1NdcRXBhIGQwqeoMvFd2DjUBG6uhowjJKVcdyP2hJhsSbaVU94QKVwCA2uw-BwL_4iee2CnANd02nyNuyN2Ny-2lCagTKgM0xmuqE6PREISETt3blUo3kxFmaLBKsQfYl6pd8hK_qPjEhH_SeeGrV6womtOsy8sF0hbRPtWdhAJIhZynAYkTBMD_y2HRGpg92KRtktMC0mTLvMqPBHvznbCryVkdfNVEi8YlT4nZLnjksciyFUBpZTrrMqeF0rzcd4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
🎙
▶️
پاسخ جالب و شنیدنی جواد کاظمیان به بازیکنان فعلی فوتبال ایران درباره بهترین نسل...
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/100970" target="_blank">📅 16:03 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100969">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2f31937c2b.mp4?token=DiG3Bcp7WqZzkFIwTbeZ44GHrfcpjB-Iy7Ny6q2WnSTdClKcdVGhWZudqDZaMnRef3ztYEPK2sMhsJStXERx6PCxrNCxXk07CFuXSWgsMMu1lkAxqTBCBxFCV4ARDos8UOFxWFOz8LRaef8OGaOpU7lQMNAox1goBz8ToYCXLbe5flT3Ia8pz5H4251uLldkGxX1l-DOMmfUqkSIk3bPYxyHryNxTB0qRqT2oKnQAl2PHw8cJhJ4kHaqS_4gSD6BzTOG028g_H8rce8TsF6n4dvaRktnxtCX7sO2zFdAs9cZynQqdrq69cs1ibVNjZkurHTQn7xqr2g_-_D_rtBZMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2f31937c2b.mp4?token=DiG3Bcp7WqZzkFIwTbeZ44GHrfcpjB-Iy7Ny6q2WnSTdClKcdVGhWZudqDZaMnRef3ztYEPK2sMhsJStXERx6PCxrNCxXk07CFuXSWgsMMu1lkAxqTBCBxFCV4ARDos8UOFxWFOz8LRaef8OGaOpU7lQMNAox1goBz8ToYCXLbe5flT3Ia8pz5H4251uLldkGxX1l-DOMmfUqkSIk3bPYxyHryNxTB0qRqT2oKnQAl2PHw8cJhJ4kHaqS_4gSD6BzTOG028g_H8rce8TsF6n4dvaRktnxtCX7sO2zFdAs9cZynQqdrq69cs1ibVNjZkurHTQn7xqr2g_-_D_rtBZMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">واکنش قلعه نویی به مسخره کردن ساعتش تو جام جهانی
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/100969" target="_blank">📅 15:50 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100968">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c4718d885.mp4?token=T6VNU1We4zU_3zJfP5Io2EvD3QRSQUQZe5rX901nsHdeHo8F48PDKINo5Bmez30vUQPMiNRjT1IuOPuhq1fbv_80Y_idYl0ExlvvUdoIqmo8D_odq1OmXiK-cGT_nPs-W0XR77kUU10ZgD7-_nSn-REhjtDQ5b0xIFv8kBxljfwU41rR1QV0aEx9kKX5zE_Ky2TMiY4gRcaB0WYJdh4l5LJJ9S7XE26sb9oJ82ozoES95dHC9KMsNDzHcj9fdfih70I5yHY8w4wA-DWMyvXWytq9ltaWNqQXXmWNWrr5-z7pfstVehqyHXxKhwSH81If7qzLcTjX1j_BXdEWY3nHfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c4718d885.mp4?token=T6VNU1We4zU_3zJfP5Io2EvD3QRSQUQZe5rX901nsHdeHo8F48PDKINo5Bmez30vUQPMiNRjT1IuOPuhq1fbv_80Y_idYl0ExlvvUdoIqmo8D_odq1OmXiK-cGT_nPs-W0XR77kUU10ZgD7-_nSn-REhjtDQ5b0xIFv8kBxljfwU41rR1QV0aEx9kKX5zE_Ky2TMiY4gRcaB0WYJdh4l5LJJ9S7XE26sb9oJ82ozoES95dHC9KMsNDzHcj9fdfih70I5yHY8w4wA-DWMyvXWytq9ltaWNqQXXmWNWrr5-z7pfstVehqyHXxKhwSH81If7qzLcTjX1j_BXdEWY3nHfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
🔥
عشق‌ابدی واقعی یعنی همین
👆🏻
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/100968" target="_blank">📅 15:40 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100967">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vTENxl_9op-l1xZYSdGEItgLsuINtxy53oFx-_5tqbZ1QMAQGGmt2ZrVO47Et5dpFBgi-oYBke1OBW7QBDV-yHid5KmhPM1uoMJYeCJbbdfd4acl3DkSz-hHZIWjnQI2phoiuF8CRbLhPOVsL5lAmQpchAn4dm6VF5r6nhHODB1W7YsU7oieDYtpMtwuX7dzgof3Kr9_Fwutn8YCB5b6ubSUTzN8P211ocTzkMofR6nfij77g8P9_HD02bcdU42vVzRJFO4IOuck_bTx_ia4O9fueea-OeWaIx7nuOtdgyhEjU4sSq_volDxJaqfy3JUgQhwL0yMCGzdxmugEQSHwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🏆
برای اولین بار در تاریخ جام جهانی، 6 بازیکن در یک دوره از این مسابقات، 6 گل یا بیش از 6 گل به ثمر رساندند:
🇫🇷
• کیلیان امباپه — 10 گل
🇦🇷
• لیونل مسی — 8 گل
🏴󠁧󠁢󠁥󠁮󠁧󠁿
• جود بلینگهام — 7 گل
🇳🇴
• ارلینگ هالند — 7 گل
🇫🇷
• عثمان دمبله — 6 گل
🏴󠁧󠁢󠁥󠁮󠁧󠁿
• هری کین — 6 گل
🏆
🏆
🏆
🏆
🏆
🏆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/100967" target="_blank">📅 15:38 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100966">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2eb072fb5f.mp4?token=ArZJtls0QsS5rlMVfPo5Sf83bvdDVtCusj_-OqbAv0wAk88VEyLwE8uLYuqdXCKiuBBBSS09YA43KkXE08-C7e6FWdhl5BeooWP-BCLETHNSWsS3-SzYuT9ZRAWO3OK4hlEineWx7Cgj0hiA4iZ6mKY_WlqQqe3j37yqrABnahbq9X7shIOjCDdtf3VPRuBHF9bavVQUhjeAfQBJvKF8YjIHjhB1CqUl3qKDdWMQqzPkEM-1tSoUwJpIvlz7nh6wJSCRoUEEPp0CeFt1Fy0s8mmsLTH6xPwjiy7HJScpiUuYs1L4uKm_R0Gx-sFyP15Ad6rUZnw63iCbLlNhKBPgdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2eb072fb5f.mp4?token=ArZJtls0QsS5rlMVfPo5Sf83bvdDVtCusj_-OqbAv0wAk88VEyLwE8uLYuqdXCKiuBBBSS09YA43KkXE08-C7e6FWdhl5BeooWP-BCLETHNSWsS3-SzYuT9ZRAWO3OK4hlEineWx7Cgj0hiA4iZ6mKY_WlqQqe3j37yqrABnahbq9X7shIOjCDdtf3VPRuBHF9bavVQUhjeAfQBJvKF8YjIHjhB1CqUl3qKDdWMQqzPkEM-1tSoUwJpIvlz7nh6wJSCRoUEEPp0CeFt1Fy0s8mmsLTH6xPwjiy7HJScpiUuYs1L4uKm_R0Gx-sFyP15Ad6rUZnw63iCbLlNhKBPgdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
⚠️
🏆
هواداران آرژانتین کف نیویورک
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/100966" target="_blank">📅 15:20 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100965">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nPsNgZJL_xLhkKNFgRAgQiyeGD86SJcp-sSzqWUCqJCAEKWpwYc8IZPCz7v2g7T96E5q-EhNEi4E4506L3dMTZWLmqlPVYN_Rl6aA8SfRDNKdVQEmDlv8qRnIKzpZ5bJb4lq8alLlPWiU6cTXochf71Tc73oJgJCqONliG_pFrjs5gruaMqVRQbuIEtmW3sckplUR63RK3RLmnDwcA474Yf6Tp6xw-gVlTIvlnFXhwysGfZRgt-59qgO9R4Ik_suQX-X28M2Tc2mrq2y4Gf5fb6ALEKmTBf3W9BqWFiZx39sBdorfeWPfWKwA7yikANhrXWM08O1w8-6oWeiPdLlcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لیونل مسی تنها بازیکنی در جام جهانی 2026 است که در بیش از 50 درصد حملات آرژانتین نقش داشته است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/100965" target="_blank">📅 15:19 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100964">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e43e2ab25.mp4?token=e0Iahu_Ay0agKLGiLWYFewS87LJ3L_kUsqWvX-aGCRYL-HDYRs70tE4q_UkEWONccK8P-h3WNAzNB8gBmDF5sEjCyTMe6Tir7lhDJznv_kGqQb1AJqctdD8llUJeUHeYOpcys7dSaz_R7RuYGVppO2JjSdLcE_wEjqOXgtZVIJUnQVLJofZgZQrGVh0TbLWwcTePdTH9xIIk_RzX0FWr4-GVMlFnw80IDQIXo-eR8MzVf7SsxaxLpX9NVBvwtj47jdY0_bEdzASlI1z5ER5NBQ_GqVPhyjsM3Zme4OFdSoOgVnfrM9JyoquTtJyN92c-FfNASKEf3MCdahEGT30hi7uq4GedLjxClVKRS8GJwvjcPTrHmAE0BzyOoqT2Cba-QsTFH6RfUnjK2m0cHMG-j2lRVLV7XDDni7QXAgUGdIrGz2hsJPWvPhLAfJ4plDByC-n_3YuzN1Spu647tX4OZqWcRoFaLa7emXIF9NW5FUd0RwiGfVZ1MSE_VeFN5KN4LkU6mtsKiEYFHRKUUNSaWh0PMKrAgWzfUFCwOh7tgGpUYK-yRIz6WHEyaykrcphiSp0fZNyKcue83wI48Jzfy9rJJRIEdrRXj2xlr26aYJO3u79acqzONZ6_MA6tOMRskd-ktwVgDbbWyJW_YNyAQwuZMnurSZyK1ylCasSfV7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e43e2ab25.mp4?token=e0Iahu_Ay0agKLGiLWYFewS87LJ3L_kUsqWvX-aGCRYL-HDYRs70tE4q_UkEWONccK8P-h3WNAzNB8gBmDF5sEjCyTMe6Tir7lhDJznv_kGqQb1AJqctdD8llUJeUHeYOpcys7dSaz_R7RuYGVppO2JjSdLcE_wEjqOXgtZVIJUnQVLJofZgZQrGVh0TbLWwcTePdTH9xIIk_RzX0FWr4-GVMlFnw80IDQIXo-eR8MzVf7SsxaxLpX9NVBvwtj47jdY0_bEdzASlI1z5ER5NBQ_GqVPhyjsM3Zme4OFdSoOgVnfrM9JyoquTtJyN92c-FfNASKEf3MCdahEGT30hi7uq4GedLjxClVKRS8GJwvjcPTrHmAE0BzyOoqT2Cba-QsTFH6RfUnjK2m0cHMG-j2lRVLV7XDDni7QXAgUGdIrGz2hsJPWvPhLAfJ4plDByC-n_3YuzN1Spu647tX4OZqWcRoFaLa7emXIF9NW5FUd0RwiGfVZ1MSE_VeFN5KN4LkU6mtsKiEYFHRKUUNSaWh0PMKrAgWzfUFCwOh7tgGpUYK-yRIz6WHEyaykrcphiSp0fZNyKcue83wI48Jzfy9rJJRIEdrRXj2xlr26aYJO3u79acqzONZ6_MA6tOMRskd-ktwVgDbbWyJW_YNyAQwuZMnurSZyK1ylCasSfV7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
توماس توخل:
نباید نسبت به شرایط خوب و بد واکنش افراطی داشت.حرف زدن برای من امتیاز و برد نمی‌آورد و باید در زمین بازی واکنش نشان میدادیم که همین کار را کردیم و بهترین نتیجه ۶۰ سال اخیر انگلستان را کسب کردیم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/100964" target="_blank">📅 15:09 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100963">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/80197f4616.mp4?token=HgW7oXmv3V6BBM45jSYKWCreLRoLog8tdLiNjQGJoTq4Quyt-oQ0LUievZHirRvvxOTnGDN2BOz4ada62HaMXPcecmyYx0Qpf4mwR01y9FlRyOTKDXL5itcX1eBxT5EeFKs7FqXiDeF2bhTNTNMtYc7BhgOunAuTFs93ERAfSddXcpfOPwSZzzVV1sL6_PzyIn2JZMG2C5NLOX8Ofc6r_7KNeZD4Qk6eoZOYgQmVMdlQ6uJ5_3EFJY7rmVcV2_JBq7rDbRNPl-Arvs9O1js1TaRVL837ESJ-ejBNlvWwjBaqaDPpXbpWUNfa1ufxKvdYFMzKnVt10uV67hjT_wmt0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/80197f4616.mp4?token=HgW7oXmv3V6BBM45jSYKWCreLRoLog8tdLiNjQGJoTq4Quyt-oQ0LUievZHirRvvxOTnGDN2BOz4ada62HaMXPcecmyYx0Qpf4mwR01y9FlRyOTKDXL5itcX1eBxT5EeFKs7FqXiDeF2bhTNTNMtYc7BhgOunAuTFs93ERAfSddXcpfOPwSZzzVV1sL6_PzyIn2JZMG2C5NLOX8Ofc6r_7KNeZD4Qk6eoZOYgQmVMdlQ6uJ5_3EFJY7rmVcV2_JBq7rDbRNPl-Arvs9O1js1TaRVL837ESJ-ejBNlvWwjBaqaDPpXbpWUNfa1ufxKvdYFMzKnVt10uV67hjT_wmt0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
🙂
علیرضا جهانبخش: یه سری سوغاتی از مکزیک برا خواهر و مادرم آوردم که نمیتونم بگم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/100963" target="_blank">📅 15:04 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100962">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2f148054f1.mp4?token=uTV79WHV6Z4orxNvYlkOOqbkHFGBaQuR2bQFrqVF2_LwT2rjVuBO963OrRqBcTEMzKM8AH0koJbmmwHtDgSafE74ILNk5gK2SykJmdCbcqhPEFKyNVN11-VS8GtrynYeAjCH_Uvyjz9vhuCwRDF4ESvBtsXZsot-bWIupT78UU_5sGSs5jQ28ATJTOL5TYvVStJoBp5tdUZ7rD7ceB__rRgdJpdxeGw-xM5oiam9Lw9HSkeHAqTqgFmZ3Zgl8eslAz5-tr-r08_okCP8rm8zDIWxETkyOtx8kkAZI5wNcQxIpg9V6ZpcMYS5ztmexKjUg3N5AKOw1iHeqRv6uW_KbQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2f148054f1.mp4?token=uTV79WHV6Z4orxNvYlkOOqbkHFGBaQuR2bQFrqVF2_LwT2rjVuBO963OrRqBcTEMzKM8AH0koJbmmwHtDgSafE74ILNk5gK2SykJmdCbcqhPEFKyNVN11-VS8GtrynYeAjCH_Uvyjz9vhuCwRDF4ESvBtsXZsot-bWIupT78UU_5sGSs5jQ28ATJTOL5TYvVStJoBp5tdUZ7rD7ceB__rRgdJpdxeGw-xM5oiam9Lw9HSkeHAqTqgFmZ3Zgl8eslAz5-tr-r08_okCP8rm8zDIWxETkyOtx8kkAZI5wNcQxIpg9V6ZpcMYS5ztmexKjUg3N5AKOw1iHeqRv6uW_KbQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🇦🇷
رقص آخر لیونل‌مسی امشب ساعت ۲۲:۳۰
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/100962" target="_blank">📅 14:40 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100961">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/opHE98aUIX7tgRPXQtBzyDa-5VuCNMQ4fT4m-rrgHrGlapPBrVYCPnNJf18S_EbhxO5N2ukFTmnEwZ5fbEYRptV2FYw0N0DKr23jLqhLxIHKIu8Bn9hHHPuM1MPEKpTCyI50cZWKYM8c4bM0cw7NaVnpgYncph6quyLa_qZ4jlvotO1KdkLFhqe8Y2VF9uZVadysiPag-yZi8coA0izQXsM060FF38V0_9YbHDQGcBAIkGFO7xWd2oulcni67jmtfQ4OoUSUXktpyMwR8ckzYFEl7sHaBHuj0U4cQ9tSqvMw0vxnL3zakZ1D39iD6PmE3r47242ndomZDrFJlhofrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیشبینی پیکه از فینال جام جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/100961" target="_blank">📅 14:35 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100960">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
🧾
امکان ویرایش شرط ثبت شده
💥
برداشت سریع با کد پریمیوم ووچر
💵
شرط بندی بدون محدودیت، بردهای نامحدود
🎁
جمعه و دوشنبه‌ها، شانس بردتان را دو برابر کنید
100% بانس میکس ورزشی تا سقف 30 میلیون ریال
🎁
با واریز کریپتو، سقف برداشت خود را به سطح جدیدی ببرید!
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
••••••••••••••••••••••••••••••••••
💠
لینک اخبار و هدایای سایت
👇
👇
🔸
https://t.me/+ioIBrQfqMLtmMmEy</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/100960" target="_blank">📅 14:35 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100959">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PBpO0jqoq8IkZsFojAdfQWZD8SzEZKkco0TN51crLIr0sm1Oif4J_40uYDHxkloo4jSqmSdl8TuDXb9mYyNb07gUtIsaNh1-MBL2ID6S4wsWEaNRyM4AtgUOxaeGQvKG4IlWSsw0-fdQPY37I8-0of_tfERybyB9qjz7iOHnjjcgqlUjt24kk_UvD5UDWnm335IDEojYdIyF1BeHa02CQozGgup1NXmPtgdyaO-rPO2eNJmHx2vgAq6UTr4aH5haSkiPaETUklEMo5juhtya9LJzSFj7qppEXGFwxA-B0fs3Ze7UB7UthJP7JofGCUB8m5rH5Qqnwmzx1K7j30hnMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
فینال جام‌ جهانی 2026
⚽️
اسپانیا
🇪🇸
-
🇦🇷
آرژانتین
⏰
شروع بازی ساعت 22:30
✔️
امکان ثبت پیشبینی با مبلغ نامحدود
🫰
محاسبه نرخ دلار با قیمت 2.200.000 ریال
⭐️
فرصت استثناییی چالش‌های پیشبینی فوتبالی سایت یک توتو، با جایزه 500 میلیون ریال
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
📲
@yekbet</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/100959" target="_blank">📅 14:35 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100958">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f2d8141062.mp4?token=sZtFyyChV0bl8ZELxXWlXlKS5jMr41H2VMJ0CxX5ATWC0zI04RwNKoDSUQ5fmdVNoTykjEC8lV_Qn3_CijApKowcvqVXrnpIt-dY4ckbOeTu9Zo3vFVUE0rjfFOFAmTpVbBa7aP-r-nrRDWM3KO9WJZ3fNJyyht16Qijg4csGFIK3oVN-Djrf_VpDf1QHURR_2MywzdGC46cStQr1aFgSVOEskWOrC3hH7-Rpa7diJStRF7B-NAxxHF5WaoNui-YCNRh5DIjKoxqNf2fh0jMO_qqMLWF-qdnZrsfBtcirm1PgJjPdf29mbrCVzLoaC5YOeP6AmfxaFu8XuAqQEbzHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f2d8141062.mp4?token=sZtFyyChV0bl8ZELxXWlXlKS5jMr41H2VMJ0CxX5ATWC0zI04RwNKoDSUQ5fmdVNoTykjEC8lV_Qn3_CijApKowcvqVXrnpIt-dY4ckbOeTu9Zo3vFVUE0rjfFOFAmTpVbBa7aP-r-nrRDWM3KO9WJZ3fNJyyht16Qijg4csGFIK3oVN-Djrf_VpDf1QHURR_2MywzdGC46cStQr1aFgSVOEskWOrC3hH7-Rpa7diJStRF7B-NAxxHF5WaoNui-YCNRh5DIjKoxqNf2fh0jMO_qqMLWF-qdnZrsfBtcirm1PgJjPdf29mbrCVzLoaC5YOeP6AmfxaFu8XuAqQEbzHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خلاصه که خیانت آخر و عاقبت نداره
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/100958" target="_blank">📅 14:20 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100957">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JhmeF5_heFVzkW9exhFX_8eQdnV6rdEH_LU3m8eK-JNJ53COlbSwJubhdmXYXWkyfSENhTPsUE0d9-ITPWLY6GCsBWcjV65GqKWyx1IW__xVhXEZJLZIzvHgByaqMfUt0rL-Z7YghY94FSgre9bAXWKDatIEgjPlDInpLTy5vVs9ROpM03Og0NVwz2BePaCbpWZHYlp1zlmkrUHQcuk1Iacc9T2cezEMdc0IvzuVq_wfmdMW6RAgEsQT2j9vLfCMLvE2trP6lnel3wb8nCDdjx4W2hfXDl4ZkSJ7HxdWRLqGMdeL-gFa5wVIvYLkDbb3xWkL8SDzqjqQevKfUzByAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استایل جدید یامال برای فینال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/100957" target="_blank">📅 14:04 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100956">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/71c23cc08b.mp4?token=FyHlGJe-bVkkfwLXWGbRWA0Mp0gsgCn8Jxn7TJC2L9m67RcQr0lce-0EvKVHKkZq-HBVp7xCFYxbXKIKmUW-ILCZkQ3JcWR8OC1eO9IHAj8txzEhJpw1wdIHgtIXiaVYDdrVnSHF9UK0XNe5pkkMHVSTF1XkNowt0gWsTx6Dqb5JSNCuuVY9nzGvgcAMOiTcKW54lAB9pSzswB7z0vtqpPgpY48hkcwjSVGsE_m2Irl8-SW5zLTOtHGV3NbgMtrGBoriNcRzcbohOFCqB0gOnOxGnJ3FschzcEOjZxjdctZ9Cbc1BhSIsRAVg_t7BRpNy-49f2PaHqgWQYJDsWpCvw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/71c23cc08b.mp4?token=FyHlGJe-bVkkfwLXWGbRWA0Mp0gsgCn8Jxn7TJC2L9m67RcQr0lce-0EvKVHKkZq-HBVp7xCFYxbXKIKmUW-ILCZkQ3JcWR8OC1eO9IHAj8txzEhJpw1wdIHgtIXiaVYDdrVnSHF9UK0XNe5pkkMHVSTF1XkNowt0gWsTx6Dqb5JSNCuuVY9nzGvgcAMOiTcKW54lAB9pSzswB7z0vtqpPgpY48hkcwjSVGsE_m2Irl8-SW5zLTOtHGV3NbgMtrGBoriNcRzcbohOFCqB0gOnOxGnJ3FschzcEOjZxjdctZ9Cbc1BhSIsRAVg_t7BRpNy-49f2PaHqgWQYJDsWpCvw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
😛
یادی کنیم از دلبری ها و لاسای سمییییی بیرانوند با دلبرجان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/100956" target="_blank">📅 14:02 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100955">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sAS0vpRwbDzc1PX6NGx1yCurN9crH0Bxerat5p4DZjKSFk41jncjglzv3QTCdI1KS7D1KalsD9AZqngi2uCDlsDni-ovUGAz18ArVZmjwBZm6SpD1jICH07uAOlWgJ3iRGlhtcS7OCPedQJwMNJzaQpm0VSwMdMj9hQcON75OXM5T4WS-iX50Qd0ALi5BQflN3snBIz5Q_2wEcF1neLL2jVqrs2kp85Zq0d3YG6W6AxfrIDEhWHTewP5e8eLwkITpfYY-mXJnsFoIfylD5UNYnv1aYoaksWREG8eFC2n3RoFlDCPKJea6PHCh7p_qLJaMuoS_aiil3b7yhlUzuAqZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
😍
استوری وریا غفوری: مشکلات داخلی یک کشور، با دخالت بیگانگان هرگز حل نخواهد شد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/100955" target="_blank">📅 13:49 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100954">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c09af135ae.mp4?token=DtbN0CsmSOQFFMTgsfG6G0hN0hDL0CL34lONmPA-ERS8NCXSkUYafm2WYBTVsgVt4g-zyhcf13slOM5auGgygj_9ccNhObIu9KZnPPkyq4VUTIqnMzPUQbBd6q1qyXyKBAP0bVeGHBbLh8z8QaMubr8_puMhWVREK2bHNyg1RGt3Hbe4M67Ln1UhGwJgwanl2G0mCqEVbpLSfuZuks77y-Dor0iMj2eVHIceefNEOjVo1V_PucwRqJpY5dUyZ8nI9OyQpMECyrtrSgLubRvqS1CSbskd2qxuhXbqp1uACu1XWlu3hFp2_152eOwZZRlaQkgGf0I5SHYMOamSSqA3_pJhR6g996zPdMC6E7smooUmFcMtLu6k9QG9FElVPKx7Xn2CwDmjgWgdvVjByek71bBIEKPy3wZWAlWZPuaU3nbuqwbZSvkA6c4czba_h6OLJxQu9XgbFS5qSG-mhdhL1zv5O7Jr7je4DJUr98N0ewv1yevfRczdgvy86T9wekr1gmroEqYRneplE_ZOOwvIYsQlwDF8dGMsN_UFQVhAaerL8ePzW-qRLAfwA_cNZSsEonZoiAJmPX3eidWCmDAPGicsxxHaS6uvThrmc6eXENuvC1MuxNh7xflle4pH-J9sspVvgHiaCgGaapD3UQCVMVQ9wQ6U051YWmNyZ6lSEhU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c09af135ae.mp4?token=DtbN0CsmSOQFFMTgsfG6G0hN0hDL0CL34lONmPA-ERS8NCXSkUYafm2WYBTVsgVt4g-zyhcf13slOM5auGgygj_9ccNhObIu9KZnPPkyq4VUTIqnMzPUQbBd6q1qyXyKBAP0bVeGHBbLh8z8QaMubr8_puMhWVREK2bHNyg1RGt3Hbe4M67Ln1UhGwJgwanl2G0mCqEVbpLSfuZuks77y-Dor0iMj2eVHIceefNEOjVo1V_PucwRqJpY5dUyZ8nI9OyQpMECyrtrSgLubRvqS1CSbskd2qxuhXbqp1uACu1XWlu3hFp2_152eOwZZRlaQkgGf0I5SHYMOamSSqA3_pJhR6g996zPdMC6E7smooUmFcMtLu6k9QG9FElVPKx7Xn2CwDmjgWgdvVjByek71bBIEKPy3wZWAlWZPuaU3nbuqwbZSvkA6c4czba_h6OLJxQu9XgbFS5qSG-mhdhL1zv5O7Jr7je4DJUr98N0ewv1yevfRczdgvy86T9wekr1gmroEqYRneplE_ZOOwvIYsQlwDF8dGMsN_UFQVhAaerL8ePzW-qRLAfwA_cNZSsEonZoiAJmPX3eidWCmDAPGicsxxHaS6uvThrmc6eXENuvC1MuxNh7xflle4pH-J9sspVvgHiaCgGaapD3UQCVMVQ9wQ6U051YWmNyZ6lSEhU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🎙
🤣
بیژن‌مرتضوی در آستانه فینال امشب: مردم می‌گویند لوند رو بزن، شکیرا برقصه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/100954" target="_blank">📅 13:37 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100953">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🇦🇷
🇪🇸
تیزر فوق‌العاده از تقابل امشب فینال جهان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/100953" target="_blank">📅 13:26 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100952">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/194b426cce.mp4?token=bYPbfgek2cziUyMNHWuM_sA5RmAwhDgMWgOsSTqbVIt-z3w_frQD5_NyoBwVgt0K-GjrLvQXOqV2UHVzdY-pAfQELrMRlUKtkTBM8atPRTZnddY8yjjjVps9-2XY-f4DlaspgIXeixvWK7il2wiXRp7vLp3fKiN2SfMJYb2NSGVVhs6bL3tzeP_2zZEnlu23CM0HhXjvWQSEYcyTFUi2FJAW8HjWUMjcDbXy_7mJm04SWaHDYsPye6MS9jRYZH7ZnmWnX6PY6kBS__h6JVqscAHcB-nxQRRWMrIr5y44twCLmpn8V9obc6E2avo6Qt5j_J3e0MgELme40tn4tK5VEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/194b426cce.mp4?token=bYPbfgek2cziUyMNHWuM_sA5RmAwhDgMWgOsSTqbVIt-z3w_frQD5_NyoBwVgt0K-GjrLvQXOqV2UHVzdY-pAfQELrMRlUKtkTBM8atPRTZnddY8yjjjVps9-2XY-f4DlaspgIXeixvWK7il2wiXRp7vLp3fKiN2SfMJYb2NSGVVhs6bL3tzeP_2zZEnlu23CM0HhXjvWQSEYcyTFUi2FJAW8HjWUMjcDbXy_7mJm04SWaHDYsPye6MS9jRYZH7ZnmWnX6PY6kBS__h6JVqscAHcB-nxQRRWMrIr5y44twCLmpn8V9obc6E2avo6Qt5j_J3e0MgELme40tn4tK5VEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
فوتبال در دوره‌ای که سیستم var نبود :)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/100952" target="_blank">📅 13:20 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100951">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fdf595645d.mp4?token=L7IRkGFaD4il_F9pEwpsf2b1HgaQVfwifEYw0LURwrqQtUXzF7InQOKPseL_YLVk-1dx-cu9lzgeWAxVYr-aJ5ElYtf6Bn_CWb2lXB_FIDIt24EuS-oIye-Ohysoseb0JaI3Wd8LexLwpyWBs-XNTHpJAc4qw2640NNoXy4GO8mhyNwH-PKIo9pdI4jx3nOAa1Q359m1hFhcvc3Y11WnbhGmFHWz5a1rs7KVmjIt6dtJhQjmJIgh6RdTubBnBJw0pAdB2Vcb0cWIbrImOpZQ5BkhyOFeOWkZKITcuYjn4qITkq34LOOAz6Xl44JpM3EfLlVZI7ydqu_duwCTvojrXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fdf595645d.mp4?token=L7IRkGFaD4il_F9pEwpsf2b1HgaQVfwifEYw0LURwrqQtUXzF7InQOKPseL_YLVk-1dx-cu9lzgeWAxVYr-aJ5ElYtf6Bn_CWb2lXB_FIDIt24EuS-oIye-Ohysoseb0JaI3Wd8LexLwpyWBs-XNTHpJAc4qw2640NNoXy4GO8mhyNwH-PKIo9pdI4jx3nOAa1Q359m1hFhcvc3Y11WnbhGmFHWz5a1rs7KVmjIt6dtJhQjmJIgh6RdTubBnBJw0pAdB2Vcb0cWIbrImOpZQ5BkhyOFeOWkZKITcuYjn4qITkq34LOOAz6Xl44JpM3EfLlVZI7ydqu_duwCTvojrXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
▶️
امباپه هم اکنون: بهترین گلزن تاریخ جام جهانی و بهترین گلزن جام 2026.
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/100951" target="_blank">📅 13:00 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100950">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">✔️
💥
استادیوم مت‌لایف در آستانه فینال امشب
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/100950" target="_blank">📅 12:40 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100949">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/772126c267.mp4?token=kSDk1VclZlpnWIXWbf6TedND6D5w-k_WYF1tfgZISt-rO8Pye4qmlAKYkWOedImx9UlP1CozJ6J7MQ8CPS7PjBb0GnK0b4BnKBTskuOlr4Ieynm-NWou9o8wO0CxI4aI2FpsaaCCTS_42q_ZyUHnG7wUkgsfWQ7VlYguE4dVEWMyWq_gI9B_ae48aIQf3hVmqn4zrrbllVPQJdPP_Qs5NU6zIxZRfzjaumpLOIEawaxNiFyX4XV1tsOEk-XJ4X7DZ3nhclydtxvDAws50mVgWN6DEj0MNvW4nkmPLk1s9KrO2lX396uj1hxFg6nzSfze-rAIoyYeK45Kg6bxf0QIr1vER7ontAOBCfg0K-FYnjbgPmWAyxwW3dwrF8ozQ9biu2o-UC0ZeV9Pcm4HymsNCE1Gf86gRpW2ccDRSfNjBsO2KrCKpyDIydeCffrHN4VbngrXGHi23lHsQYDrA8zJb4IOeaca3Y5K3_hs1Vq0Mdv4ZPaPp8BxRqFbCZH7sB5DzCoDq_gSaO04iDAPAIGQnHKg4RLfSqNQmYKFCKjhcALeOGemEawBeoC4raphCERIr8dHAFjLdiH-9C8uvlczkejktQu83NMGdzxYjLp7cCtH7bguQqqKR6ChHnzX7tEzJfEySgK2yQcYHtcQVv7T1rUTrT0-73_fnKBJu1haJD8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/772126c267.mp4?token=kSDk1VclZlpnWIXWbf6TedND6D5w-k_WYF1tfgZISt-rO8Pye4qmlAKYkWOedImx9UlP1CozJ6J7MQ8CPS7PjBb0GnK0b4BnKBTskuOlr4Ieynm-NWou9o8wO0CxI4aI2FpsaaCCTS_42q_ZyUHnG7wUkgsfWQ7VlYguE4dVEWMyWq_gI9B_ae48aIQf3hVmqn4zrrbllVPQJdPP_Qs5NU6zIxZRfzjaumpLOIEawaxNiFyX4XV1tsOEk-XJ4X7DZ3nhclydtxvDAws50mVgWN6DEj0MNvW4nkmPLk1s9KrO2lX396uj1hxFg6nzSfze-rAIoyYeK45Kg6bxf0QIr1vER7ontAOBCfg0K-FYnjbgPmWAyxwW3dwrF8ozQ9biu2o-UC0ZeV9Pcm4HymsNCE1Gf86gRpW2ccDRSfNjBsO2KrCKpyDIydeCffrHN4VbngrXGHi23lHsQYDrA8zJb4IOeaca3Y5K3_hs1Vq0Mdv4ZPaPp8BxRqFbCZH7sB5DzCoDq_gSaO04iDAPAIGQnHKg4RLfSqNQmYKFCKjhcALeOGemEawBeoC4raphCERIr8dHAFjLdiH-9C8uvlczkejktQu83NMGdzxYjLp7cCtH7bguQqqKR6ChHnzX7tEzJfEySgK2yQcYHtcQVv7T1rUTrT0-73_fnKBJu1haJD8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
🔥
میدان تایمز نیویورک در تسخیر آرژانتینی‌ها
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/100949" target="_blank">📅 12:20 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100948">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0afa3e469f.mp4?token=Z1oV7P2XTE47Hw-l6ujGKJmBktEh2sX4Vc0R_0RsqYjqeqen8NBDkA9EjhmbwN6Xy4DaE-0s1T4job8oOWmeUQ3yAzWMjxFGtu7pUbQ--LSoWj-W6MnAh_4L8ZcHVmDczlk1h35SftFPa1WBUnnpHHjog0f38m2hpebXTTNP4vgA44QCdmXy9Db2yN_vNpbpiDWjDl_FNSYqtvN9hS51mCvZksWzTdMnAXBBhgfnUMNDLXie0ivwaQ4HC8b4HqbAuQG4wzNsWMOYNrFjsV6ig8p7IXW_9gyYgvZ2yN3Ym_ncFgun9Y-S-iFxpkekhWoI5ZL9B4Ds1L9hTx61A-FCe2DYxGB1ACmcm8nicTckigRSgYUrEYCme-27w17YKXY0NT0d8mTQ7OCw0O6b7KjcK9N6ZecSNPUdgMJLJMvz-s7tIUKP5rBZqyhRViq7oFxv49HVHCeSHPmODX2qma0N1FFWKg2RSljJrvgHAGZa6bqf57RMhE708a2B1syqyLN_mn-3pYbs3qdXrHdG-CA-OVRxR31WosFoLxbisgpNBTF6wiOZVAuWdHGf4Pg7st3ZdVYBYTeYluql7663LHRauBeG8sA7yf4rSHOeSWPYxnUSzOs5zyS3YAm-jtfYx418fw68j5t3rcvbRd_NFwQupNBlefU6VwHu37FuhvbxcaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0afa3e469f.mp4?token=Z1oV7P2XTE47Hw-l6ujGKJmBktEh2sX4Vc0R_0RsqYjqeqen8NBDkA9EjhmbwN6Xy4DaE-0s1T4job8oOWmeUQ3yAzWMjxFGtu7pUbQ--LSoWj-W6MnAh_4L8ZcHVmDczlk1h35SftFPa1WBUnnpHHjog0f38m2hpebXTTNP4vgA44QCdmXy9Db2yN_vNpbpiDWjDl_FNSYqtvN9hS51mCvZksWzTdMnAXBBhgfnUMNDLXie0ivwaQ4HC8b4HqbAuQG4wzNsWMOYNrFjsV6ig8p7IXW_9gyYgvZ2yN3Ym_ncFgun9Y-S-iFxpkekhWoI5ZL9B4Ds1L9hTx61A-FCe2DYxGB1ACmcm8nicTckigRSgYUrEYCme-27w17YKXY0NT0d8mTQ7OCw0O6b7KjcK9N6ZecSNPUdgMJLJMvz-s7tIUKP5rBZqyhRViq7oFxv49HVHCeSHPmODX2qma0N1FFWKg2RSljJrvgHAGZa6bqf57RMhE708a2B1syqyLN_mn-3pYbs3qdXrHdG-CA-OVRxR31WosFoLxbisgpNBTF6wiOZVAuWdHGf4Pg7st3ZdVYBYTeYluql7663LHRauBeG8sA7yf4rSHOeSWPYxnUSzOs5zyS3YAm-jtfYx418fw68j5t3rcvbRd_NFwQupNBlefU6VwHu37FuhvbxcaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
حمایت کودکان آفریقایی از اسطوره علی‌دایی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/Futball180TV/100948" target="_blank">📅 12:04 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100947">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tek0pe2vMLSF8VN7idkQq0c6BlZnqFF98jveogx1gZWfiWAps9DMxDkU1n4a2uG-wSPeogH3O_u4xBFTechAgrbyd-JAhr52e5Nk3ogypoGkOcZagRBTY0pKAbRbtKtVuUd0Ku6825eMJ97v7vOx3CSuO51Tp4cQ7Qung4Zam_xZ_SMvXa-zAo1GuyUUMowW9w12Ks-x_R1g_t3rawWA_2wygyU4w2Ww2j9MM6h5i0UypLB5CydVSr-PwGkyZK-kLWyaIs-dzpZ-kBDVwWLShucujGwBqDwzPHqNSPO5NlFYrRbSznx7wlDjdkNdZ6PgcBdKQXshkjfZd4DEE1O-AA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😛
تصور اهالی فوتبالی پرتغالی از جام‌جهانی:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/100947" target="_blank">📅 11:40 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100946">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KAdBqWbtbyxI7Y7rwxI464kJjGw1iIR2NSgUPcR8U9ucLWVqSBRNrREQpNJJiRwQIUdGXoz04JRepxgtgUUFsu00yGFZe-WVRTipRUYa_LYXA0iLTfxMSyj2A0NFUJpQ8jEZVilfUGLxN_6uOUTErblBw0VsK0arzrYVbppw0kK_zP5-bYsOho8qEmhP6AII3RorX0bQDK0hAUS5d3tpKffK45aYxSYqVmBZAmAIRRb6Q1KXvvZenD_BRQ4XI9KSd2ceR7ZqLyDMBtT-mqdoSzO-uUkA5MV_BDb-mV25AaEuDEvk77PDYriiq986rOPhNFhpdNs_yqNJbLhyhLXmEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
کیلیان امباپه در جام جهانی 2018:
⚽️
7 بازی
⚽
4 گل
⚽️
4 پاس گل
🥇
قهرمانی
⚽️
در پست وینگر راست
🚨
📊
کیلیان امباپه در جام جهانی 2022:
⚽️
7 بازی
⚽
8 گل
🔴
2 پاس گل
⚽️
10 مشارکت
🥈
نائب قهرمان
⚽️
در پست وینگر چپ
🚨
📊
کیلیان امباپه در جام جهانی 2026:
⚽️
8 بازی
⚽
10 گل
🔴
4 پاس گل
⚽️
14 مشارکت
4️⃣
مقام چهارم
⚽️
در پست مهاجم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/100946" target="_blank">📅 11:27 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100945">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e1a0fbf718.mp4?token=D7armeisdE_-TuFP9fm_CUrKR_ZsEEuEWivN7Jc8cjz8Cd_A1Em8gIcsNwZA0DEUTEET-905Y283mX40fnAJ9yGTHL00hjnFlxZw5w42C1HbKNPB0q0Cr_aGoXLTOvRp2VJdg5VLcaBbRPs12RZqGjE9UFQY6isxfDuW2oDaYwQBqTpS3_uPyTJngeKgi4SxiyiIU_Z4dJdNbtu_qI2uHEOJccYnQlRI8CrbGte2SpDXloI3YRVdtpPzg6RLXnHbVFVzWbWxANvlAqswQWLS0ST9mR9waHzoECVAMAmpu3szkqyBGWVHL9kxMv_qJU8oOOsRtDnu5WtmnJXzn94ItA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1a0fbf718.mp4?token=D7armeisdE_-TuFP9fm_CUrKR_ZsEEuEWivN7Jc8cjz8Cd_A1Em8gIcsNwZA0DEUTEET-905Y283mX40fnAJ9yGTHL00hjnFlxZw5w42C1HbKNPB0q0Cr_aGoXLTOvRp2VJdg5VLcaBbRPs12RZqGjE9UFQY6isxfDuW2oDaYwQBqTpS3_uPyTJngeKgi4SxiyiIU_Z4dJdNbtu_qI2uHEOJccYnQlRI8CrbGte2SpDXloI3YRVdtpPzg6RLXnHbVFVzWbWxANvlAqswQWLS0ST9mR9waHzoECVAMAmpu3szkqyBGWVHL9kxMv_qJU8oOOsRtDnu5WtmnJXzn94ItA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
🏆
🇪🇸
تنها چند ساعت تا آغاز فینال جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/100945" target="_blank">📅 11:20 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100944">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GfhCKIqLlDYbLR4bLvi-k1_NBOqIr9ddNtofZ6baf-1mN6gySE2ZAiypzFpd-lLW3HNMRzSePH27n6bwebufCi6fTUpf7x7O2xvsp14U8Q6kF4u6NgogT8ZJkzUuGzpG4w6PshSwEx-ystokVcE3508c0h62YUVgAgck3-rqkXfXNP9WUxAV737_IlGpaJI3DsyNKNkwalOb5wy2UhK9xlxLfKA93pt8SmwKduumC-sahuaV9F0jAJ23emrX-pxiajN4B_wBHZg30yNusTAS_OTDQPLwRZpcSh_AQVa4yq0ykoZkwB03oydzf50Tj31_Taio-1cOEZ1iyC0jEtHB5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
بهترین گلزنان تاریخ برای تیم ملی فرانسه
کیلیان امباپه به تنهایی با 66 گل برای خروس ها میتازد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/100944" target="_blank">📅 11:03 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100943">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🇦🇷
🏆
🇪🇸
آماده‌سازی نقطه‌پنالتی استادیوم مت‌لایف برای بازی حساس فینال جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/100943" target="_blank">📅 11:02 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100942">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40b0455cf0.mp4?token=ClbbcT2Hc64-EsBSTCJxU6PSKElAMDtFczb9X48URati_3Pl3OC8iU54T2ygAWouJ1utJebi1FmGz0FrGAPta0ZH1Bcp7_sH-5qSD4VQ9KTf3pIbvTvcC8qlFJZCkNHvsmmp859bziks6A_U-p-IqImHN4XceRBimVYtbDSe_pZOlX1AY2dhaI3XNrBY7Zs19Ri3nhRpRa-YEdLtSFmR4AFmDaRJnkf2X4M6L26hDgdMCOjrKKGCNt_iakj-GDS2405oO9JdXdtrrNmUYEEY4DdYkYintTk-P1due-y-Uz3Flf967bpvzl_UwIEOM4YdByLN9u-QpZYmzGE52XG1-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40b0455cf0.mp4?token=ClbbcT2Hc64-EsBSTCJxU6PSKElAMDtFczb9X48URati_3Pl3OC8iU54T2ygAWouJ1utJebi1FmGz0FrGAPta0ZH1Bcp7_sH-5qSD4VQ9KTf3pIbvTvcC8qlFJZCkNHvsmmp859bziks6A_U-p-IqImHN4XceRBimVYtbDSe_pZOlX1AY2dhaI3XNrBY7Zs19Ri3nhRpRa-YEdLtSFmR4AFmDaRJnkf2X4M6L26hDgdMCOjrKKGCNt_iakj-GDS2405oO9JdXdtrrNmUYEEY4DdYkYintTk-P1due-y-Uz3Flf967bpvzl_UwIEOM4YdByLN9u-QpZYmzGE52XG1-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
👀
اولین شوک فرهنگی جهانبخش بعد از خروجش از ایران: من تو ۱۸ سالگی لژیونر شدم و رفتم آمستردام آزادترین شهر جهان؛ وقتی رفتم دیدم اینا بدون شورت باهم میرن حموم
😆
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/100942" target="_blank">📅 10:40 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100941">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NZjO3e537Mx9Sr-TP2qubrJBq6Yjrd17-yEUcZAVcncBD2X6CigHhQgUOD8PpLcC7VHiNoET-VKkeGwfMy9507n21JpWkVKsRyks7TKjojtiOYZ-yx7TI2Th4j8BWKKH1wAL3PPns3DlJC20pCk3kmURGEOmmDefZdFit755F_As3nqVcFF3HUhX3ndwNsCzMGblSSp-i1Yo0Ug5vuO9Ly45fgaPOwLgYeHJiqsJ8yiS5xwjYDIqRB-s83VONRjKRINZ4Va3LoiHsveg63gn4DCeLbM5VgLBKFV8ZKQ5XTVPS7_dA1JK5OT7WLO0U19Z_jqWyZY1D78q8iy3zzJdQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کمتر از دوازده ساعت تا فینال جام‌جهانی
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/100941" target="_blank">📅 10:35 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100940">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K5LLuKFk_2elQqU23Ov2B-yw7YWqHh8xrLfDCisZStY3g8dtpFruniN3r0_t_NcuVduoAso_dposh9shHqolRt152z4tPbvkzT3DPn9AKjJSd0_IFuBlip42Ul2iAxe9XRRwzHEnZdjx6chsBOfkI7h0TGn0kFe7leO68kekvjSa1-YvCegyg7Eg7Knc-tpt5fts2mD5-YEYBg3Ij9TCVrlC4Bry86azOyS6K2fIrqlLrQcm1dL1hFHXnX-tC3pJVdpgeXtzL9qUwuOLu-Civ5XJBEs1_9zcTBWEZKadfjUQAxjOch1RjrzQi2yqoPJHBL1ibzXPA-5lcPPmBZ6g7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤣
جوری که امشب اسپانیایی‌ها فوتبال میبینن:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/100940" target="_blank">📅 10:26 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100939">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jcfYkbkB5KdjMe_GY_joHgsnrDBgv8eGzNeow2Ic6FSupVznJXcBHNBAp4ymprCBRKF9YUS4BdJ0AUDGYgKmhTlqnl0dh7ZiL0GrmhVtwfFVgYtktBl8M69Py7S3Y3MCzJusnSQHqPxBKvfHDXiOgyeOUnZ0cpJNEAUTv36WWyqed1ANAYphYa71svUkxVsiyUqXaoZRGmh4R9lhOnBwJMxl50c1uL1nU5U7BIVoBRMB0AtTF69hDU6yRGahgxzml-B7aAwg8o09q6gxfM7MtPKQmXDfv3BdeG0WpYkBXCvkAYUZSdv8fEr0B2LsdKiEBYP3Hzd12BTswrq51pbRwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
رونالدو نازاریو:
فکر می‌کنم اسپانیا به‌راحتی آرژانتین را در فینال جام جهانی شکست می‌دهد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/100939" target="_blank">📅 10:22 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100937">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b1e84c807.mp4?token=Q-6v8ojhS8B6HnJHQPYlZWg6Ov6bQq-xJthCS0RGadPRg0eyuLKAmxDu3vaV2-dKdZkcIsqA67Za9iFmZwDH662IWoNQl4vmgUFLhZmL_TrJpv3jaBvqRdqE8hhC-Rn7nzyAxT_kaHHHFjuaZHiE3uvntGNuwMcdimJdFrZHletIXqIH9O_8v-9q4jQ2-Izb0wb7AlHbf8kW88HmptwAfcm1F4uzAgjr4Z_34VkYlUA2cBaFkkZo_kikMfPUGoKYFLsiebkEMBYg5h7pohZb3hkyBT11ufJvz0n8V8Y1lKmm_b6k1kiIWL4zwtAslv2lu2dSb055cj9UIns4n7oLCmqTXk5eYDI53ah1dWZSgE-NezUoL-9sYtGCEAWsd9ToBWVuGmRkglVz9y1hb4-HUYoSpf0UDLv7u9B8o3BI8Fduxc2ttzsGgJi372Bt0hzpTtDcXCK9EIktUtUBh55AEbuvwnwHr6lWHfDPOOi7RnizpZj4_R0lTiZLRko0vDZLDNbB92MXm1Io1MUrQZULgwxv1kGxMVfyMdacP1Gm6fUJT9vu7Fw944F0FJXt1qPoJtkuApYZCzORwYl0xvHFOjLvy6soV0Vpbqz_V0_hrHEvLmjx0GNLIOhsNjcGxEWjwKceap0EjF2vVfUyzehEHeJnnt7SWrbkb7sSknDyfbo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b1e84c807.mp4?token=Q-6v8ojhS8B6HnJHQPYlZWg6Ov6bQq-xJthCS0RGadPRg0eyuLKAmxDu3vaV2-dKdZkcIsqA67Za9iFmZwDH662IWoNQl4vmgUFLhZmL_TrJpv3jaBvqRdqE8hhC-Rn7nzyAxT_kaHHHFjuaZHiE3uvntGNuwMcdimJdFrZHletIXqIH9O_8v-9q4jQ2-Izb0wb7AlHbf8kW88HmptwAfcm1F4uzAgjr4Z_34VkYlUA2cBaFkkZo_kikMfPUGoKYFLsiebkEMBYg5h7pohZb3hkyBT11ufJvz0n8V8Y1lKmm_b6k1kiIWL4zwtAslv2lu2dSb055cj9UIns4n7oLCmqTXk5eYDI53ah1dWZSgE-NezUoL-9sYtGCEAWsd9ToBWVuGmRkglVz9y1hb4-HUYoSpf0UDLv7u9B8o3BI8Fduxc2ttzsGgJi372Bt0hzpTtDcXCK9EIktUtUBh55AEbuvwnwHr6lWHfDPOOi7RnizpZj4_R0lTiZLRko0vDZLDNbB92MXm1Io1MUrQZULgwxv1kGxMVfyMdacP1Gm6fUJT9vu7Fw944F0FJXt1qPoJtkuApYZCzORwYl0xvHFOjLvy6soV0Vpbqz_V0_hrHEvLmjx0GNLIOhsNjcGxEWjwKceap0EjF2vVfUyzehEHeJnnt7SWrbkb7sSknDyfbo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
💥
🏆
شکیرا رفته بهترین کسانی که چالش موزیک جام‌جهانی از سراسر دنیا رو اجرا کردن جمع کرده و قراره امشب باهاشون برنامه اجرا کنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/100937" target="_blank">📅 10:13 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100936">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c3ca27f4c.mp4?token=lZvetoxQEqzS-sryvc8i33mLTS-1jq8bYa_tm2r36zwbDBi0iYtE_S5VZnSgk1vTdL8V0TFN_s7Wco6gQ73_m1-86pA1n6bsClC63pDE7RhzVcdW0LYlWMwHLRsXpV0wQw-wLZck7iFr_R8PBMFtpOYWxosLvDK2FAh37FHCuibJCpw322jOM8-GV-Qbsy_RaAO29SMnkMRTFDfXauQk-hI7qb9qVi9tIk852bIoBEC7QKKXezZcNpxSRWMZ2Oan5Naf5_9bEHdIL5qqaTXO6epOuUwBNlHAf7lHYTqNdL-Liz6e6Z1_qpK_1Sz_z-lX_8WC8JLsJTEeFt4ZOxRN4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c3ca27f4c.mp4?token=lZvetoxQEqzS-sryvc8i33mLTS-1jq8bYa_tm2r36zwbDBi0iYtE_S5VZnSgk1vTdL8V0TFN_s7Wco6gQ73_m1-86pA1n6bsClC63pDE7RhzVcdW0LYlWMwHLRsXpV0wQw-wLZck7iFr_R8PBMFtpOYWxosLvDK2FAh37FHCuibJCpw322jOM8-GV-Qbsy_RaAO29SMnkMRTFDfXauQk-hI7qb9qVi9tIk852bIoBEC7QKKXezZcNpxSRWMZ2Oan5Naf5_9bEHdIL5qqaTXO6epOuUwBNlHAf7lHYTqNdL-Liz6e6Z1_qpK_1Sz_z-lX_8WC8JLsJTEeFt4ZOxRN4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
👤
علیرضا جهانبخش دیشب غیرمستقیم اعلام کرد که طرفدار استقلاله و اگر روزی به ایران بیاد برای آبی‌پوشان به میدان میره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/100936" target="_blank">📅 09:56 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100935">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de2d1332f8.mp4?token=idHYZzszAoUfCTUWFvo9nEKetvMpy6DkvifMoCbXF7aTfMIBoi24VyoYVDU0jeHcu9ZhzRZWre14Ni0RB9QvAXdYK5lgHBd3OcS8GP0ZVjVdt8nwjHHuYqgfaiKZj8uBsfKT_DVBTES_ka5I9Dd_cMk5Ed4WuQGHn8xYl5zA2owFGPapoGoGbZXqbzqkkZHJM5VTG78Jg6P5mAAHQHLnP9vz0IWBIFBxUeGjMO2BMcFqWR_jMgWQ1DpPQ4DxxdOcy6hOlxkyRrbcSRWXerNXgVr8bNG0xGHJrTmYCiItUkxZKhQJj4LruTEimU3PtifNM_fUaNEFbbbWrFqJqD4Z9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de2d1332f8.mp4?token=idHYZzszAoUfCTUWFvo9nEKetvMpy6DkvifMoCbXF7aTfMIBoi24VyoYVDU0jeHcu9ZhzRZWre14Ni0RB9QvAXdYK5lgHBd3OcS8GP0ZVjVdt8nwjHHuYqgfaiKZj8uBsfKT_DVBTES_ka5I9Dd_cMk5Ed4WuQGHn8xYl5zA2owFGPapoGoGbZXqbzqkkZHJM5VTG78Jg6P5mAAHQHLnP9vz0IWBIFBxUeGjMO2BMcFqWR_jMgWQ1DpPQ4DxxdOcy6hOlxkyRrbcSRWXerNXgVr8bNG0xGHJrTmYCiItUkxZKhQJj4LruTEimU3PtifNM_fUaNEFbbbWrFqJqD4Z9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
صحبت‌های گذشته بیرانوندی که بیشرمانه به اسطوره علی‌دایی حمله‌ور شد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/Futball180TV/100935" target="_blank">📅 09:42 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100934">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f5e2e3c171.mp4?token=bfQUW-L5gxF8_y3GR_M_EkVG07DMi-lFIfD1BuAj4YFi-UaVbIa9f2qa11YpccvHCjk3rFMc5CLFn7Bk6tTFnD4vUzZMTtkrW2Bx3zU2pjvvTR-R6PZHdlnyNs0qHGzi8HPKnoqX4gyllieyAuoTA6ikudEXk_RVX5CayDgeum1B7jEwmZND9_WTSxLCiq85tN5pWsBer1d6iGvJ9om-en3DiuTyLdblcUNzJOzRjXdUSotn0P8yO5JJ8fhjqqQLDzLbajSDtnsaxla1_B7gD1Qi-O7MN4skl_-USFphjgySOc3X1F2odO-jfx9ZXpbq1RZYNiQQ5-NIaKDZ6XIs6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f5e2e3c171.mp4?token=bfQUW-L5gxF8_y3GR_M_EkVG07DMi-lFIfD1BuAj4YFi-UaVbIa9f2qa11YpccvHCjk3rFMc5CLFn7Bk6tTFnD4vUzZMTtkrW2Bx3zU2pjvvTR-R6PZHdlnyNs0qHGzi8HPKnoqX4gyllieyAuoTA6ikudEXk_RVX5CayDgeum1B7jEwmZND9_WTSxLCiq85tN5pWsBer1d6iGvJ9om-en3DiuTyLdblcUNzJOzRjXdUSotn0P8yO5JJ8fhjqqQLDzLbajSDtnsaxla1_B7gD1Qi-O7MN4skl_-USFphjgySOc3X1F2odO-jfx9ZXpbq1RZYNiQQ5-NIaKDZ6XIs6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
صحبت‌های گذشته بیرانوندی که بیشرمانه به اسطوره علی‌دایی حمله‌ور شد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/Futball180TV/100934" target="_blank">📅 09:20 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100933">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff910de710.mp4?token=t0TR3AA0yBbkQWjckd1TLph9rrWS2TFgKBE0ogMY8iaEfJ-x_9SXQ0ZHChwT2azWKNqEaGa8dNasmqOsJj4LyGWgb8uhOlApVyB24Jt3uNqg0LiNgy06OCGTQpX-UoY88TCfdYLj-8WpPX06lOmatC0Ey6AP6EokgaGSupOOqHGb7gYsqFMG3MbyNJPvNX-Fam8LGl-2Zmq9Ctn6CS_FdUmSkWoXSRT9SGM9Alj2DzHUU5XCMkGIDZTnu9KbWOZqAUvIMqVyCk5le72ZrOBhRrCITibS5bybfUoTa77bA2maLPKLLiqJw4tKP_Wfo7xPM32xvDG9r3jS0N7q38Hkb2J9qL1_V0rjqtsNebJpfnOn8scFiNc_gQIv1MP4tWVQdJ2oqx9FEtxBn8Q2tzyBDIy1C9O9Y41wR0TwjrOievYxKiA8JLInQO_320-CCzolwQhk_tC0lUJVishVvbtnp4aveZzpKb1e34ebzbaf2tk4w3RfuFmHCK7qnrkbD995UefPIcEIfSbsiLNfDBr3kLNn-tZ-exoO4dT5frktso6UkSelLi_WyU-Ku7jvYDbX25aAiDNxmqlIxhqo_s1RIqS0LRAM1bN4QnnwPvl_hmp4_Idl2F5uASiOoG3ShyrgRO1odZeEkSuBUwpETweRQTykEtXZUeuPYfom8Uze-Bw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff910de710.mp4?token=t0TR3AA0yBbkQWjckd1TLph9rrWS2TFgKBE0ogMY8iaEfJ-x_9SXQ0ZHChwT2azWKNqEaGa8dNasmqOsJj4LyGWgb8uhOlApVyB24Jt3uNqg0LiNgy06OCGTQpX-UoY88TCfdYLj-8WpPX06lOmatC0Ey6AP6EokgaGSupOOqHGb7gYsqFMG3MbyNJPvNX-Fam8LGl-2Zmq9Ctn6CS_FdUmSkWoXSRT9SGM9Alj2DzHUU5XCMkGIDZTnu9KbWOZqAUvIMqVyCk5le72ZrOBhRrCITibS5bybfUoTa77bA2maLPKLLiqJw4tKP_Wfo7xPM32xvDG9r3jS0N7q38Hkb2J9qL1_V0rjqtsNebJpfnOn8scFiNc_gQIv1MP4tWVQdJ2oqx9FEtxBn8Q2tzyBDIy1C9O9Y41wR0TwjrOievYxKiA8JLInQO_320-CCzolwQhk_tC0lUJVishVvbtnp4aveZzpKb1e34ebzbaf2tk4w3RfuFmHCK7qnrkbD995UefPIcEIfSbsiLNfDBr3kLNn-tZ-exoO4dT5frktso6UkSelLi_WyU-Ku7jvYDbX25aAiDNxmqlIxhqo_s1RIqS0LRAM1bN4QnnwPvl_hmp4_Idl2F5uASiOoG3ShyrgRO1odZeEkSuBUwpETweRQTykEtXZUeuPYfom8Uze-Bw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🎙
پیروز قربانی: «هنوز هم می‌گویم با فجر نیوزیلند را می‌بردیم»
‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/Futball180TV/100933" target="_blank">📅 09:03 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100932">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vhf65D3pnFP-i7wKQfuvpKmIsJziHXI5Dg6UeACgk_SiNCq03_YsQxcHnXSsrZgzWnrv9tnoG3MINkLuYolVfXIRlUIkxygClXmkRf_-lV7Sj0HNEHIoFIQTCJrMWTd-XGHsM5jomQCR3y9cTWAHWiOO2LUpwS5nkLTTQm-qBe8sUHJZ76l0Zh63fjC-MKMxrVdidFrMmbHZwIttbrYppVhbsRkg112ETgXR0fyiy8OEoMG_3b-nRCBN2FbsdjyaYL7F_0ORJgLHMHIwUggO2Q8_x2YD4zlt4bg9wduOnZ5BuaBMtZEwBYxqvGEEPPSmhVNnhVl-cvjgv4Tbocbb6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🏆
پیام لیونل مسی، قبل از فینال جام جهانی:
🔺
زیباترین بخش از تمام این سال‌ها، هرگز جام‌ها نبودند، بلکه کل این مسیر بود. همراه بودن هر روز با این گروه، مبارزه با هم، ایستادگی در لحظات سخت و لذت بردن از هر قدم در این سفر.
🇦🇷
از تمام هم‌تیمی‌هایم، کادر فنی و از همه کسانی که هر روز تلاش می‌کنند تا تیم ملی آرژانتین را به یک خانواده تبدیل کنند، سپاسگزارم. مهم نیست در فینال چه اتفاقی بیفتد، این گروه از قبل یک فصل از تاریخ را رقم زده است که هرگز فراموش نخواهیم کرد و هیچ‌کس هرگز نمی‌تواند آن را پاک کند.
🇦🇷
سلام آرژانتین
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/Futball180TV/100932" target="_blank">📅 08:56 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100931">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d65552b958.mp4?token=L4xS1Hq7hNiAPfVCDjuiilabtzCktDKrGnbzccOoCiP2kDcefNy9DmS6UFn2VDcO9yz4JOQvOmBv7daYmQ7i42weMS17W8KU_b-rBsNzmWUAr3C8t6-vpSoQKhxc69ZW8KZaNSwfbakv3mblx7TEwh9GvpdOcTCWuSGZCqHfhYBFTuHZn7ZfUQjsivHZkxwBn97grVLAl6rIVP6p0H3mQn83Yb6guJbArQ85oN_Q-h4wiDH8Q7FLdicmfK4fetlMdr1N2f0PWK6T4RhdqifqWuCMQNgROUmqGyrtxTAa9mvM0hDd92vT3p3aoaNozPJy1B2G6DMGYamlxa5tUb3vJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d65552b958.mp4?token=L4xS1Hq7hNiAPfVCDjuiilabtzCktDKrGnbzccOoCiP2kDcefNy9DmS6UFn2VDcO9yz4JOQvOmBv7daYmQ7i42weMS17W8KU_b-rBsNzmWUAr3C8t6-vpSoQKhxc69ZW8KZaNSwfbakv3mblx7TEwh9GvpdOcTCWuSGZCqHfhYBFTuHZn7ZfUQjsivHZkxwBn97grVLAl6rIVP6p0H3mQn83Yb6guJbArQ85oN_Q-h4wiDH8Q7FLdicmfK4fetlMdr1N2f0PWK6T4RhdqifqWuCMQNgROUmqGyrtxTAa9mvM0hDd92vT3p3aoaNozPJy1B2G6DMGYamlxa5tUb3vJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📈
🧠
صحبت‌های زیبای هادی عقیلی درباره جنبه‌های دیگر بازی لئو مسی؛ تعریف متفاوت فوتبال در دنیای مسی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/Futball180TV/100931" target="_blank">📅 08:40 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100930">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pZlHjM1Ut_RKEvjOLdoI3qwPNeupuhkHujqqyunTKNq0GAhpM_PK6_k5vSNgDaQD-ukGxzLsu2s6knFlPnbMq9GdvANv2_9fHrVXGT1LD3Cqs48GOYlVwgw0Z6wSPYD99c9610qu4xVydv1JCaKocRIkv8cUr7GRE5G9_1JY4a1RhKo5n6xN9vQ_geXZngorzu0h-66sFK3cjR5MKzlYTMAo2h1AaUf7Yd9lBP6NpqF6z7fGTMokY-zARZq3LUK5s1DPDQxEzslfRNBDNVr-AmhZvOY7EMsP4uR2kyyyAwCuDG4lhxhs0QdN6F8CTD28MQc4AWs2NuBwMMXqipp5XA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
#فوریییییی
:
✅
⚽️
خاویر تباس رئیس لیگا، تأکید کرد که بارسلونا اکنون تونسته به قانون ۱/۱ برسه. این یعنی آزادی نقل و انتقالاتی بیشتر برای باشگاه بارسلونا در نقل و انتقالات
‼️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/Futball180TV/100930" target="_blank">📅 08:11 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100929">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1802a702ca.mp4?token=lk1Fd0I_hz9uRyhCLVP1dEj6bnX_s1oKBViclmUf2161yY-JoyWSGEVCpGRDmk2Zsc1zW_iQGtWFcgV8fUr7HJgv7gfhL0ytHtuEObu8No5jcMuP7EwDyINOLAdcxpTPYrfAQHrYvyzf5UFs5M7VUKIGaKkF0gGEoMiVUMJMcubzqXklU6aL6keyAANo8L9GCJXBNSHMBq12U11FKPg1fOZO5HWoPKl5vpN8GI_7MbpuMFj_fRPl1GpSFh1SOhhM2sSB5qkN1KCHyeEep9FXEo-Qrv9BBG8aDUkbnKzj0Y3FJtD1bi-rPtx5AtuPhlFrcKiHKEa8FxEmJm25YDXBkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1802a702ca.mp4?token=lk1Fd0I_hz9uRyhCLVP1dEj6bnX_s1oKBViclmUf2161yY-JoyWSGEVCpGRDmk2Zsc1zW_iQGtWFcgV8fUr7HJgv7gfhL0ytHtuEObu8No5jcMuP7EwDyINOLAdcxpTPYrfAQHrYvyzf5UFs5M7VUKIGaKkF0gGEoMiVUMJMcubzqXklU6aL6keyAANo8L9GCJXBNSHMBq12U11FKPg1fOZO5HWoPKl5vpN8GI_7MbpuMFj_fRPl1GpSFh1SOhhM2sSB5qkN1KCHyeEep9FXEo-Qrv9BBG8aDUkbnKzj0Y3FJtD1bi-rPtx5AtuPhlFrcKiHKEa8FxEmJm25YDXBkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رائفی پور ایز دت یو؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/Futball180TV/100929" target="_blank">📅 07:24 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100928">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🚨
🚨
#فوری ؛ زلزله‌ ۵ ریشتری شهر سالند-خوزستان را در عمق ۱۲ کیلومتری زمین لرزاند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/Futball180TV/100928" target="_blank">📅 07:12 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100927">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🚨
🚨
#فوری
؛ زلزله‌ ۵ ریشتری شهر سالند-خوزستان را در عمق ۱۲ کیلومتری زمین لرزاند
.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/Futball180TV/100927" target="_blank">📅 07:07 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100926">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/472dab2e65.mp4?token=Hs1hYvK5mU42nI0mW8DnHQ4h7Pqk-6g8oHXbL6fkHV7OgTV2RIqcnebjZbOEdP_qsiWhZJfYcEs0As80rvll7NEF6XKmG4SHgRNxThH101FX_RmtrkVHg_SYwHRyGeZCaV4JuzdpIdw9k-wpH91G9lCXUkX80IUhjqepM2aNvndjohnfC_uJxcWj-yTWSqTLEq-OzOJGVoSWmtXzcGGzjcXCSQlIJs-wjHeeyiipiMcoGxeEnGbf0ehiYgfkMf4cbcVedZC-MhpBRH18sFTAxocWhuRb03ngOi_eLCoLY-_diambv_8eYBN9PxG4F-KUIrmQ_RujDOMq9gmOOLQGKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/472dab2e65.mp4?token=Hs1hYvK5mU42nI0mW8DnHQ4h7Pqk-6g8oHXbL6fkHV7OgTV2RIqcnebjZbOEdP_qsiWhZJfYcEs0As80rvll7NEF6XKmG4SHgRNxThH101FX_RmtrkVHg_SYwHRyGeZCaV4JuzdpIdw9k-wpH91G9lCXUkX80IUhjqepM2aNvndjohnfC_uJxcWj-yTWSqTLEq-OzOJGVoSWmtXzcGGzjcXCSQlIJs-wjHeeyiipiMcoGxeEnGbf0ehiYgfkMf4cbcVedZC-MhpBRH18sFTAxocWhuRb03ngOi_eLCoLY-_diambv_8eYBN9PxG4F-KUIrmQ_RujDOMq9gmOOLQGKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🛑
گاهی بزرگ‌ترین ها آن‌هایی نیستند که بیشتر از همه دیده می‌شوند؛ بلکه آن‌هایی هستند که بی‌سروصدا همه‌چیز را برای تیم‌شان فدا می‌کنند.
🔺
انگولو کانته‌‌ی با تواضع با دوندگی بی‌پایان و لبخند همیشگی‌اش به یکی از دوست‌داشتنی‌ترین هافبک‌های تاریخ فوتبال تبدیل شد. او از بولون و کان تا لسترسیتی، چلسی و الاتحاد مسیر پرافتخاری را ساخت و با فرانسه قهرمان جام‌جهانی ۲۰۱۸ شد.
🔺
امشب، آخرین حضور کانته در جام‌جهانی به پایان رسید؛ نه آن‌طور که خودش و هوادارانش آرزو داشتند، اما با همان وقار و جنگندگی همیشگی.
🔺
خداحافظ، کانته؛ فوتبال هنوز هافبک‌های بزرگی خواهد دید، اما بازیکنی شبیه تو، به این زودی‌ها نه..
🔥
👍
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/Futball180TV/100926" target="_blank">📅 05:52 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100925">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4cd61ad475.mp4?token=MlMRTnzZfmRcEzb816kUSPA7uowGf9fKBgNAJvk8niS90FQJNyyuzI2oMO9VUh1bHJ4WcCt01xFESwDEK_57rWQ6qAeaGevp08j_tFXyzDpHqu244CIMyL3l3XB1lIgucZpJjc2Fd1W6xRRkzrOCr8Wgvl3gBQ4uSJaypIWqPgwo8TyFsMnQQVUw8BRgD6nrUHt78cqr0T1T-2b8OOI3AhUeCLSaLx2lqYfTxg7apTSWlXFPjUTMW8cXFNXfmw1itfyXbPaNvJI7KvGcFdZ3dPLJLTyraWZqdVG-gJSs0IXA1RK1ie6ofG8qh97sMXvQ1Btc3Zcct0zZFM11oKHWmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4cd61ad475.mp4?token=MlMRTnzZfmRcEzb816kUSPA7uowGf9fKBgNAJvk8niS90FQJNyyuzI2oMO9VUh1bHJ4WcCt01xFESwDEK_57rWQ6qAeaGevp08j_tFXyzDpHqu244CIMyL3l3XB1lIgucZpJjc2Fd1W6xRRkzrOCr8Wgvl3gBQ4uSJaypIWqPgwo8TyFsMnQQVUw8BRgD6nrUHt78cqr0T1T-2b8OOI3AhUeCLSaLx2lqYfTxg7apTSWlXFPjUTMW8cXFNXfmw1itfyXbPaNvJI7KvGcFdZ3dPLJLTyraWZqdVG-gJSs0IXA1RK1ie6ofG8qh97sMXvQ1Btc3Zcct0zZFM11oKHWmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وقتی بین دو نیمه بازی فینال منتظر شکیرایی ولی با این شاهکار روبرو میشی:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/Futball180TV/100925" target="_blank">📅 05:12 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100923">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YB8JmMfNhcRVger-PDf-ZCg5RYop6TmBCo8dnHgbCL0cmMs6E9G5YwEf3oG2l5OgLlCl1fYhtKKWdomx85mfk25ojHn5ctfnwYovuCRJhdBu74F6bb4PYcGCLMUv6CSKAktEJyJim3iSG5DGL-f8p2Iv3VpmWogp2mqJ6f690En78PifZ6QGC2nb2yU8YJm470BK87o8m0wlaSVt9NB-gPWE06e_BQ3jFMhWcjiJ0WPEl-J8M3tt-bkH1GNzriDcYlQHalni-R_6PNETR9lQ9VX3HWVswW9PdoOKqoi-VMvv5vvEZygWeqmSZhhBot7Xx9H2y1EudADtqKtofIazbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WrZpsxrBSSAeb3hoIbqOqnCa9cYJyV5nGjGt-7cgLY8DZHIbcFFt0KRcTUqbcuJl6LlRN2fMIyrE1pCBQNdQ-Z6oTP63N2G49Q9MhBjeVwWMlgjsk-BKkd69ucXvNqfIOfhxJ6MLCpbDFeasdtq0t0nsyHrDOop25oL75xuXztqbIEPEObomRiW71r6gA4n9_zKcDOaT8nEnSAS862pYyDUmD4Z7rZ-GGN0iuXQEoYThzlezYRhXg4dRmNznrn0MZK3tXQoZwOhJlkVIpF4s12kmAOri9CoYw83eXMFvuwXooTvIVdPFaCgY_XhRq_eEOkPAjzLrNSoJAIsVtbK-zA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
📊
🇫🇷
اگر کیلیان امباپه در جام جهانی 2026 برنده جایزه بهترین گلزن مسابقات شود، به اولین بازیکنی در تاریخ تبدیل خواهد شد که توانسته در یک فصل به افتخارات زیر دست پیدا کند:
•
جایزه بهترین گلزن لیگ اسپانیا
•
جایزه بهترین گلزن لیگ قهرمانان اروپا
• جایزه بهترین گلزن جام جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/Futball180TV/100923" target="_blank">📅 04:36 · 28 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
