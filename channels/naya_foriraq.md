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
<img src="https://cdn4.telesco.pe/file/VuNRm182_SE3FqdtRzN6ovJEHenxsEzhBvG6ryBiL9b1V5RvPTAxBdkY3IbJ9rfJduOsGUCHaizIbYZwEZIk7wU3w9_K8p9dZ6ihW6CyLP_Eet5PkSjQdeAG3mOzudE3kL2rgLhGbsASd0TawVloRrAT5VS_EezVKOi4M2GOI6ZzgNkzD15RqQMPsPqMbGIPOqgFxXmgASO00A_4akgNZc5Kh2bC1edMhbnUmzo7XioQRnmRXpg1qunsaaVbbeSN1FRa4AgJM2o6bL2aPPJRXu5Vdr2ug9XYe53NLUDeOW6uEuU5-XrUsNRYtZ8O37LK2e-0pkmALC1PGA7nlJmmQw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 265K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-21 15:51:52</div>
<hr>

<div class="tg-post" id="msg-93527">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">النظام السعودي مقلدا النظام الصهيوني: سنصدر بعد قليل انذار بإخلاء موقع بصنعاء بهدف تنفيذ عملية نوعية.</div>
<div class="tg-footer">👁️ 1.85K · <a href="https://t.me/naya_foriraq/93527" target="_blank">📅 15:42 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93526">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">‏مدير جهاز الاستخبارات الداخلية البريطاني: إيران تسعى لاستهداف مواقع كالمنشآت العسكرية ببريطانيا وخارجها</div>
<div class="tg-footer">👁️ 2.18K · <a href="https://t.me/naya_foriraq/93526" target="_blank">📅 15:40 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93525">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">النظام السعودي مقلدا النظام الصهيوني:
سنصدر بعد قليل انذار بإخلاء موقع بصنعاء بهدف تنفيذ عملية نوعية.</div>
<div class="tg-footer">👁️ 3.51K · <a href="https://t.me/naya_foriraq/93525" target="_blank">📅 15:31 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93524">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/148343f45b.mp4?token=UaPGgetxjpif6cADUbH0pxDUkvy1uEZ_CzR7gqSOAnI4f8YK31IY1M8ZjL-aMNkNN2GeVXVT54HXtQwIDcg_yFRzyzX_v_dZXWCJXwyqsEtUnIZZsnrC9-03OAroN0TFL3uUAkLa3tVnfYszSUEDN4jqDwIruDOvAyz3db0szq-mVUsThAeZ03mTM50eZLK7mk19n3W8Aas9FWCu3uGigomt-iRpZsaN7mkLhRkzl-Hnjja08aaz2sc0NGzEbc60M0CPbQLxmDoB9AnHb7aDI_ltHTwXGb3ixYvjMCtOT0xfC-tDsnYdcqeQGGkjnWxJPMLnnwtzIad2QSW1kW_VKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/148343f45b.mp4?token=UaPGgetxjpif6cADUbH0pxDUkvy1uEZ_CzR7gqSOAnI4f8YK31IY1M8ZjL-aMNkNN2GeVXVT54HXtQwIDcg_yFRzyzX_v_dZXWCJXwyqsEtUnIZZsnrC9-03OAroN0TFL3uUAkLa3tVnfYszSUEDN4jqDwIruDOvAyz3db0szq-mVUsThAeZ03mTM50eZLK7mk19n3W8Aas9FWCu3uGigomt-iRpZsaN7mkLhRkzl-Hnjja08aaz2sc0NGzEbc60M0CPbQLxmDoB9AnHb7aDI_ltHTwXGb3ixYvjMCtOT0xfC-tDsnYdcqeQGGkjnWxJPMLnnwtzIad2QSW1kW_VKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سماع دوي الانفجارات بوضوح في شمال الرياض</div>
<div class="tg-footer">👁️ 3.52K · <a href="https://t.me/naya_foriraq/93524" target="_blank">📅 15:31 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93523">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">في خبر غير مهم
🇪🇬
وزير الخارجية المصري بدر عبدالعاطي: كل ما ستطلبه السعودية سنلبيه.. ومستعدون لتقديم كل أشكال الدعم للمملكة بما في ذلك الدعم العسكري</div>
<div class="tg-footer">👁️ 4.39K · <a href="https://t.me/naya_foriraq/93523" target="_blank">📅 15:22 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93522">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">في خبر غير مهم
🇪🇬
وزير الخارجية المصري بدر عبدالعاطي: كل ما ستطلبه السعودية سنلبيه.. ومستعدون لتقديم كل أشكال الدعم للمملكة بما في ذلك الدعم العسكري</div>
<div class="tg-footer">👁️ 4.66K · <a href="https://t.me/naya_foriraq/93522" target="_blank">📅 15:20 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93521">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">هجوم بالمسيرات يستهدف الرياض</div>
<div class="tg-footer">👁️ 5.29K · <a href="https://t.me/naya_foriraq/93521" target="_blank">📅 15:12 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93520">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">انفجارات تهز الرياض</div>
<div class="tg-footer">👁️ 5.37K · <a href="https://t.me/naya_foriraq/93520" target="_blank">📅 15:12 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93519">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">انفجارات تهز الرياض</div>
<div class="tg-footer">👁️ 5.32K · <a href="https://t.me/naya_foriraq/93519" target="_blank">📅 15:12 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93518">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">مستشار الامن القومي العراقي:
400 سوري نُقلوا مع المعتقلين إلى العراق لم تَثبُت إدانتهم، وسلّمنا 50 منهم إلى بلادهم. البقية سيتم تسليمهم إلى سوريا على وجبات</div>
<div class="tg-footer">👁️ 8.26K · <a href="https://t.me/naya_foriraq/93518" target="_blank">📅 14:17 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93517">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c9852db7c9.mp4?token=sXM3SiWdPP1hhcNXPUX3PxqJbh3GXZ304vUW95zyKvADtqsiX17zNsC2TrKTCeVcX2N52JacI0hqMH2NiC3gDI9BtbC1Svzkj3Wa3yna5lOb4CD1zdSraJMIpfADJOncGMigvVZMI0dUvfCrxbkznqzCQ4rzt_1uB7cDT79QxO5V3l-7Z3QM1oOeShqGI9fbS5zTfAynz8jnfhQzTVa25D4k5Jp74-N113iQvx2lDOSY7ZrTxn9Uh-XxBlNFS7V5SEV5cwxewQW9kzi0ntQp5Cbol6lqT0ZtGFUAlnm51wShRYhgRKSyXdmnocJHizYA6lP4ORH4oDuPT4aLnECYhCtgD4ydR82CUtcirBVgs7_Ci_yjJwdJ1MtCn59HBFrCUMMy0gX9h4Vv-g6DvDPtGRhHe6CdDGbHsZgRorhSd7nfTU4jBOKdHeov-mmKZnCxKx9NxEJCaRikZ5jyOJ_QnGLYVFtvFyaI6WydvnMRemk_i4s5byverHcOpWV1Zqe0kpFuwOSA9mnj7tdacHOZiFkDxnfDXTv1wdRYh6Qfhe-gpQQwHb_sK2-bS7ez4q32J7D8H8yXWCKQVLoT5D3CY1miYdyX5Ucj6Pk4Bqu5SXTQEJjTE_ggkS29XsEHp8UBpyNpSQJ-FKSr5uUS5g7IhhiKBraxxLJR5c5VAYNjRiY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c9852db7c9.mp4?token=sXM3SiWdPP1hhcNXPUX3PxqJbh3GXZ304vUW95zyKvADtqsiX17zNsC2TrKTCeVcX2N52JacI0hqMH2NiC3gDI9BtbC1Svzkj3Wa3yna5lOb4CD1zdSraJMIpfADJOncGMigvVZMI0dUvfCrxbkznqzCQ4rzt_1uB7cDT79QxO5V3l-7Z3QM1oOeShqGI9fbS5zTfAynz8jnfhQzTVa25D4k5Jp74-N113iQvx2lDOSY7ZrTxn9Uh-XxBlNFS7V5SEV5cwxewQW9kzi0ntQp5Cbol6lqT0ZtGFUAlnm51wShRYhgRKSyXdmnocJHizYA6lP4ORH4oDuPT4aLnECYhCtgD4ydR82CUtcirBVgs7_Ci_yjJwdJ1MtCn59HBFrCUMMy0gX9h4Vv-g6DvDPtGRhHe6CdDGbHsZgRorhSd7nfTU4jBOKdHeov-mmKZnCxKx9NxEJCaRikZ5jyOJ_QnGLYVFtvFyaI6WydvnMRemk_i4s5byverHcOpWV1Zqe0kpFuwOSA9mnj7tdacHOZiFkDxnfDXTv1wdRYh6Qfhe-gpQQwHb_sK2-bS7ez4q32J7D8H8yXWCKQVLoT5D3CY1miYdyX5Ucj6Pk4Bqu5SXTQEJjTE_ggkS29XsEHp8UBpyNpSQJ-FKSr5uUS5g7IhhiKBraxxLJR5c5VAYNjRiY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">القوات المسلحة اليمنية تطل على مسقط رأس القيادي المرتزق حمدي شكري ومحمود الصبيحي ومسافات قصيرة تفصلها من البحر العربي وراس العارة</div>
<div class="tg-footer">👁️ 8.36K · <a href="https://t.me/naya_foriraq/93517" target="_blank">📅 14:13 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93513">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rLUoVA-gRAHus67GcJV9WzPI3xpHsucczFwncPM1unxU2RAZQ5CDvR6uytBeJ7scC8LYagziHepD6r3GLA20jfDvTnG5mzwiR5g-YRAobzyROmtFtS4_AmLLOC5eoWQTUWCccNgsr9rGmI42YKww8mn_onyKVwwK7Khg9_wJdpoBDzBr2QKJel40OuahkdKaclW_JK8D91j9VXrhhggC7sf7oGHy5gTBEX6teNyOEm_wlAvLygeynhorHRt1ZWrWWEMfAQQz-mOao6mY7MjN7bl1T9PcRoNkLWI2U0vFmgKZmsRWARHJS2qHRqN5l3Uq8qMkCUVaY-avPpkjG2NyFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eM1dpo1hbgt7C8Jpui0Slz6oFkCCErPx0bzQ2cUNWF776JxQ2-n0DvwWfhB9uFMfSQ8aCzTkmjOI9FYC3KrLBvQyHHEN4sAnN35I_k8qi6ThKmV7clDx0gKuxvaLfLtynjmkWnPNO65RXfKF-NSCYU4c2Z05k22UleAq2ema87V1zvb18QBN8yQ2U-7NBWZe1AoOryZzn2wMW5Hrm8jGVzu4tkG2FjDW1yjdxygI3nrccUMGuAOIcdzHJx8A_543XxtYBGDzAI_o8StZ5esUGdnsbwHCuP3iTw7sVhASX011Rfsuhf4Toxgc3DYBbxTWrc-ZkxadopFOKmaE5h5exg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dP_naNevYK18jLwSTF5n43okPHg-qV04cHKaAjqHXvgVb6u2OKkvaUPjsgEi-2-sJkIRyjXkNtt9VjxiR5pK7TbGIY7LZiu1MarOUzbZzgS5y850hvDkJ0ZrB0GoOQ1RfSu73XhGZkDEnmQBdNi6odjoaG4rE14OpxzfeoY4whFJLImOn87GfI20y5qPYwsE0Vdw6XgQmqber6OONcS_EY6ptKHM-WHwN4ELlxKtWu3Z7PnbgghvWb3ORKMvfIlPG616iLr87Norh0WQlyWEhexQvo13UseBBjOkDT9lYfHiaFto2SIJhT2yyZCLRvjhDPK3z6QAEuCVQcBBhHJy4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/o94CSXejfxaO23ccqG7RjXg-PMsFCHvDZiAvSYa3sDnRFigmUZI9SIdeVQ5ztq_1ByjV5dPWS0yH-m-XgHTSOYQRApf96NkZQCdpJD3tSVQPA4aUg2wt9ifl32Z5IlGfBvEe7Ju_EOOiJ0KCjWEdoPUk9p-MvvfPT65oKPgFJcBMeeQtqvott9nAjlQakMPdA4YAEgv_OSu1tNqGu791ANotTGiO1ri_1wXEnZeykf0Ilp0eGMzRoqZcuEdrSNTMFkmy6TlqCl1AxhcbPvv3fXw19Dg_KUaGIXWvajBQ_s4Fbwvx4Ak7weiPRclCKecveVbAElKmDabk6ltMMJfCDQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">النظام السعودي يغير صوت الانذار ويطلب من المواطنين تحديث هواتفهم
اريد الرنة مال مراد ترن ترن</div>
<div class="tg-footer">👁️ 9.1K · <a href="https://t.me/naya_foriraq/93513" target="_blank">📅 13:55 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93512">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromنایا به فارسی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d12152172.mp4?token=Av3dapeq7iUlKKVj04HeSaeJVxfm75Xq3rxO9ckSXyWKsxnWyzcB3xKtfMwaQFNMY3zI16M81dCyPAX7mCWMXVn61EeCyxRWNmZCF9kVwvMsTpzB2KAIOMVTvPaHSxfH8Wart-JdtYST6krWsrPDebFvRTaU1JG4O8YtbN9yvrcrav1Tv_rhlrucF76TQdWYvwUKTvLGXsEAceAUp0nGg7dWK24TwAnG2rFugjkqle3tyxU_iosv3VAG5ibQ_Ymm8YkVaLK0ANo5-i5SAjHwGJsRETBj2muZ9KM1ncaUpv9duUWXd73Kci4G5J2AyEOQ3Hu6tAIe5HvyKwqXov3qVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d12152172.mp4?token=Av3dapeq7iUlKKVj04HeSaeJVxfm75Xq3rxO9ckSXyWKsxnWyzcB3xKtfMwaQFNMY3zI16M81dCyPAX7mCWMXVn61EeCyxRWNmZCF9kVwvMsTpzB2KAIOMVTvPaHSxfH8Wart-JdtYST6krWsrPDebFvRTaU1JG4O8YtbN9yvrcrav1Tv_rhlrucF76TQdWYvwUKTvLGXsEAceAUp0nGg7dWK24TwAnG2rFugjkqle3tyxU_iosv3VAG5ibQ_Ymm8YkVaLK0ANo5-i5SAjHwGJsRETBj2muZ9KM1ncaUpv9duUWXd73Kci4G5J2AyEOQ3Hu6tAIe5HvyKwqXov3qVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴
یا علي مدد ..
@Naya_Press</div>
<div class="tg-footer">👁️ 8.38K · <a href="https://t.me/naya_foriraq/93512" target="_blank">📅 13:50 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93511">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">لحظة الهجوم الصاروخي اليمني يوم امس على العاصمة السعودية الرياض
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 8.18K · <a href="https://t.me/naya_foriraq/93511" target="_blank">📅 13:46 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93509">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PGgtgnFafiwsF-owbJ3tIwjtUSv2Q7a8E5iXQCzm20akiMETtQmigY6ESeP4LkrUaRLV0ZT9Ur17UiOduC2uVnbhMFm-jm93wO7FBf9GHp3NjgfOZfx54QwK3K6Hiuu6VdXOhExI-kC_9t61k9qY8AhFJYDNOiLXpUl0-zhGgQNE5nhfFvQgusti-Ka0VwPBq9BBde8kEGgeWVC5czQuYgheU8h1hUz_9zGfU-u9qVwY-qfBA7MDxfNf_-XnY6nmdyEnNUHOAjaWDB_8JHP0AhLAKloNWVq3B9A4wOA31FDF4_HoAMGMoRLcTZMBzCui01OEUQRzAcq1b6HanVOQXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YtVbbiE3Ve9_QdgCbIckJY3GA5uckjwlsOp9Cvl3UPBaDKcs0oPiIa47Q3D2oQ1yHEbB7oUuizYsL5_ouSroXAjPPmxx8o6FdyoPZQkgawWyg4YsxW01Pq1ENBIpgm-mu9b-V8tJnadil5h3vseZksWEWMVSO4j3f6kwSE_N7p5Bdb-o55TOfkN5SRYvL6L9am7fLCfWLv1meqBqGRVLbDJn5yTZqXqWzdYqcZaUJsr73XmdzqLxvn67RKfrc5hzUdRklBeUos3v2RB7p87SGSjLg0LLJ8Cc6Ts4sO4Ph2n5npdZm9xqCohZN_rEopLrdKz1QrpNSA3VlUVj8AO6Mg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اضطرابات في الرحلات الجوية فوق دبي  https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 8.28K · <a href="https://t.me/naya_foriraq/93509" target="_blank">📅 13:41 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93508">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">اضطرابات في الرحلات الجوية فوق دبي
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 7.87K · <a href="https://t.me/naya_foriraq/93508" target="_blank">📅 13:40 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93507">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0bf372211.mp4?token=FW4eJRc-h-hgfvuJoCgee9-SDt5MCtw5pbItIatb7pD6f7KtHoTRdi3sl6aUNl_zJVJAJL_oZ1Y2jpaF9ohuCUmRnmcjAbslTR9FrRMhOIYRCx2uvkjoJtRgCOZaIZQ3GQC1mnYz3RFzeOGNOMNKap-iIEIEMTPoqDD9dTlLZneAxsRMoUxqU9HpGSli-zdUDj4upUdqOL0P6FObPT69PEmU3h1t155lgpu6bC-D_oGFelsasps9MgmGR5fKwSfBR0xCeL-CB0o7lfUWOBzqDOEl1KoisV4LmBS6PZDS_v0PaDWTx53gVgdHrAO9OlRRnXGTz_BwdCEMKWBfyLvXC4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0bf372211.mp4?token=FW4eJRc-h-hgfvuJoCgee9-SDt5MCtw5pbItIatb7pD6f7KtHoTRdi3sl6aUNl_zJVJAJL_oZ1Y2jpaF9ohuCUmRnmcjAbslTR9FrRMhOIYRCx2uvkjoJtRgCOZaIZQ3GQC1mnYz3RFzeOGNOMNKap-iIEIEMTPoqDD9dTlLZneAxsRMoUxqU9HpGSli-zdUDj4upUdqOL0P6FObPT69PEmU3h1t155lgpu6bC-D_oGFelsasps9MgmGR5fKwSfBR0xCeL-CB0o7lfUWOBzqDOEl1KoisV4LmBS6PZDS_v0PaDWTx53gVgdHrAO9OlRRnXGTz_BwdCEMKWBfyLvXC4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تعطل الرحلات الجوية في مطار جدة السعودي بسبب ضربات القوات المسلحة اليمنية وضمن معادلة المطار بالمطار لحين فك الحصار
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 8.66K · <a href="https://t.me/naya_foriraq/93507" target="_blank">📅 13:32 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93506">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🇮🇷
الخارجية الإيرانية:
إيران وعمان توصلتا لتفاهم بشأن تحديد مسار مؤقت للملاحة والتفاصيل التنفيذية قيد المتابعة.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 9.01K · <a href="https://t.me/naya_foriraq/93506" target="_blank">📅 13:20 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93505">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🇷🇺
الكرملين:
العقوبات الأوروبية الجديدة على موارد الطاقة الروسية قد تعرقل التوصل إلى اتفاق بين موسكو وواشنطن.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 9.18K · <a href="https://t.me/naya_foriraq/93505" target="_blank">📅 13:18 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93504">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a154d4b9e6.mp4?token=D9KJ9OBcY_QCE-H3QzEWCnFEyQtCUwPP1tlBeQqFyfNNBqnRU0SKQUrn8_L1F-78Y7UZN6a01wh3izqiBLebTfsK2PaCFoxMYrY2CmRH40xdTSzY4050CfhVrmjLbQdHPirNCoku0YFn-t2_Pgk49tV_J9PeUR4HvDX_CgynMnT5vEhEitDsxZO-F74MkGvLOzU3W0naRi5wN73zB_LdOmiIVSnuWFQL1pzXiZfJz5DmrvVK4HZyXYUteafad1zXVgM5E6LQaNyt2vnjfdHbD2PLmn_pXNAFsHv94dBc0ij5jaAdmU2ukpp21BrUwbpH4h0dh_tw-SFdD4uobkQk4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a154d4b9e6.mp4?token=D9KJ9OBcY_QCE-H3QzEWCnFEyQtCUwPP1tlBeQqFyfNNBqnRU0SKQUrn8_L1F-78Y7UZN6a01wh3izqiBLebTfsK2PaCFoxMYrY2CmRH40xdTSzY4050CfhVrmjLbQdHPirNCoku0YFn-t2_Pgk49tV_J9PeUR4HvDX_CgynMnT5vEhEitDsxZO-F74MkGvLOzU3W0naRi5wN73zB_LdOmiIVSnuWFQL1pzXiZfJz5DmrvVK4HZyXYUteafad1zXVgM5E6LQaNyt2vnjfdHbD2PLmn_pXNAFsHv94dBc0ij5jaAdmU2ukpp21BrUwbpH4h0dh_tw-SFdD4uobkQk4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
وزارة الدفاع العراقية:
القوات الجوية نفذت ضربة استهدفت بقايا عصابات داعsh الإرهابية في قاطع عمليات ديالى.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 9.83K · <a href="https://t.me/naya_foriraq/93504" target="_blank">📅 13:03 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93503">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v-iWKOBkxtTZEaRedwUUbvIgYsz7RZqIeUxuitaIpIHEELJdCvAGkTtYCNvirFGXgGes4-wkuhuc_MS4Y4GPIpzcAJtZygI1TksTtYMwZJ4EbzDtuSlgOMG3WUkbUd4U1VT6-TmhpHVUgZ_Gufp5_uvI3qsNuh5vaQrB7xx3m_QClshFDZ6jhALWhxvlmoT5GznpPYDX2xHf1Fi5XoebYHAVLF9TImD8Vnf3SGdVupRMEvVgDDT_ZO4Sc3GGAQ2tFSy-k1aqdO10jxCMCTYrppZyZ6qFcK9KwqS8d3DL8SO1pG_H0cdcdpr4mPvQqPtqQ3q8jfplE4fWh8ovdoeQrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
مناشدة عبر بوت نايا
بعد أن أطلقت وزارة التربية العراقية التقديم الإلكتروني للإنتساب وأعلنت عن مبالغ أجور الإشتراك السنوي في المدرسة الإلكترونية، الطلبة يطالبون بأن يكون الإنتساب مجاني بظل الظروف الإقتصادية والمعيشية الصعبة للعوائل العراقية.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/naya_foriraq/93503" target="_blank">📅 12:35 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93502">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/olW9nFY3aJdycpyjRtFGoOuIl5VXPq_VE6g3qVq61OIZgNKpFMHU6ug_4DHEevk8cq8A3jM8Qk8XqC5uO6YUAXNL-ckEWuMFaTlGbWLJOwZz7nIt4GzTZozJASLtys7igZ4TUhbQdSsuFO8ZZEOhfcL5CV_ZV3T65g38D1OByUbfpOPpKedf14bmIKEQEvNvOIBUTZB9W6AHtuIgw21QVMzs0bRZZ20G4SR9H-PdNiN7Xa6Mb5X_NMPnW9PW9qVZi61S8bY6FNOZUnoJbnOEdPRl2SAb7gHWW_S6zQ8y8nvvT__jZjdS_hGuVxvj02ec9RICIcgtI8oo_QH4KhWu0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لا سيادة ومعتقلينا بالسجون
الحرية لابطال المقاومة ؛ ابناء الشهيد ابو مهدي المهندس
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/naya_foriraq/93502" target="_blank">📅 12:13 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93501">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/15614c3890.mp4?token=GW22stDJpTALnxTlqwPGdJ9a05QhL4Mno8ySfFfk11e33J07crFHYRzWttUeEoNwk2ZKgEnWeqH8gXaDpHGaCf9NWsgvwitKrYiwPhwiHcEB34dTFUvjIfSRCnauIx3TStNugI4ilE_IopcR8p4XaJiyEoRTg87P8ZMCb4y-60ZXJgMVarUrQN6gh_KgyK9DstQ6yNXGsLnDq_6o2asZSU7RBt84z9LrYL6S7ei2HBQ_I18p2zTJSqUXwCB9Up3HSjutjlBXue8_lm_egEWqrtcdtUWhtnFfzsIyA1Y14DcJqbLVXgfVPBP_wJXttbB4Mqwy90IB1BNTTwUKjweSkFb2wsKArcw1KECA9L9cIqXqn2NaXtQdb7pLi72nGoXUEOJanzWsJrZurX3yfbh9DU1SGEYfxZA-qKc2YPg24LKkhd_JHZFSt81Te_RfV0UbKMg5v_WnHm2OZtQL56UrPRs-c4f-uHuSMwCKqMZK0ZBW7Qgnm6f7zTk2XHcd55jSFwqfDvGZPUbyaTwQcyBCoavenw4hP4cZWIApZyqod84rf_2LYV7TMsVosMitocasq2zRlCvl7jtTifPyNMQaZkfhK-XpXbIwncih4pWUoQBPiymoAJznPQ8dfOWTYrsCd-bNsE8PPfEEZ3llhxtbTfKyGctCwF_V_4ojaiA8a4o" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/15614c3890.mp4?token=GW22stDJpTALnxTlqwPGdJ9a05QhL4Mno8ySfFfk11e33J07crFHYRzWttUeEoNwk2ZKgEnWeqH8gXaDpHGaCf9NWsgvwitKrYiwPhwiHcEB34dTFUvjIfSRCnauIx3TStNugI4ilE_IopcR8p4XaJiyEoRTg87P8ZMCb4y-60ZXJgMVarUrQN6gh_KgyK9DstQ6yNXGsLnDq_6o2asZSU7RBt84z9LrYL6S7ei2HBQ_I18p2zTJSqUXwCB9Up3HSjutjlBXue8_lm_egEWqrtcdtUWhtnFfzsIyA1Y14DcJqbLVXgfVPBP_wJXttbB4Mqwy90IB1BNTTwUKjweSkFb2wsKArcw1KECA9L9cIqXqn2NaXtQdb7pLi72nGoXUEOJanzWsJrZurX3yfbh9DU1SGEYfxZA-qKc2YPg24LKkhd_JHZFSt81Te_RfV0UbKMg5v_WnHm2OZtQL56UrPRs-c4f-uHuSMwCKqMZK0ZBW7Qgnm6f7zTk2XHcd55jSFwqfDvGZPUbyaTwQcyBCoavenw4hP4cZWIApZyqod84rf_2LYV7TMsVosMitocasq2zRlCvl7jtTifPyNMQaZkfhK-XpXbIwncih4pWUoQBPiymoAJznPQ8dfOWTYrsCd-bNsE8PPfEEZ3llhxtbTfKyGctCwF_V_4ojaiA8a4o" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇾🇪
🇸🇦
إستهداف مباشر من قبل القوات المسلحة اليمنية للمرتزقة في مديرية الوازعية بمحافظة تعز أثناء تواجد الإعلام السعودي، ماأدى الى فرارهم من المكان.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/naya_foriraq/93501" target="_blank">📅 11:48 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93500">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/711d7fd6a7.mp4?token=oDiITNpmhCEQp939ncNygRZlgrNrE5xl_rkQ71Q85QknOGCTq2tv1Enc_BmjQynN1hoZrvVNwC0LAC2JCe7BexuGtPYrY1Eg9CHQeGh5IvbNKRX56W44eZpK5eXjaeHj71ZwTGnxo3VlfuStiOOJCzYU83C6dVFF7FLA65Z0csodgpx-2ucpCvm8LGXnhWf9QHn5jqjZ8E6GO4Fzj-iDB6qqnlreGroqMswlgYX3KDsIzmEAZqpvyBInanLwBV9SKuo62DFkkjbBaKBldY7YOc70gARf_GNhWM4lqXV75DnrULM1rRvBVPau2YXojj4dqHUCFdIvz2NRmyx1i-g51Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/711d7fd6a7.mp4?token=oDiITNpmhCEQp939ncNygRZlgrNrE5xl_rkQ71Q85QknOGCTq2tv1Enc_BmjQynN1hoZrvVNwC0LAC2JCe7BexuGtPYrY1Eg9CHQeGh5IvbNKRX56W44eZpK5eXjaeHj71ZwTGnxo3VlfuStiOOJCzYU83C6dVFF7FLA65Z0csodgpx-2ucpCvm8LGXnhWf9QHn5jqjZ8E6GO4Fzj-iDB6qqnlreGroqMswlgYX3KDsIzmEAZqpvyBInanLwBV9SKuo62DFkkjbBaKBldY7YOc70gARf_GNhWM4lqXV75DnrULM1rRvBVPau2YXojj4dqHUCFdIvz2NRmyx1i-g51Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
القوات الأمنية تستخدم خراطيم المياه لتفريق المتظاهرين من جرحى الحشد الشعبي المطالبين بحقوقهم وسط العاصمة العراقية بغداد.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/naya_foriraq/93500" target="_blank">📅 11:37 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93499">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2f8ebaf541.mp4?token=sJaZ4TjI12ndUnzYbsJVxDdRJjmyIMbS6M4I8MAfpa3XwCYqitGkhW54fqKktxy7w99JBizz6CKmBYq2ekJbuKrEhH6LW-cxCXFOOVJB_sbxSzVNrSmYoOZuHzjhR6GgV9VaN4yx8S117bHrihw_axtWzuMJSj9qiFIk9xGmidnrUR71gn6jrmeclILBpqJZ_iMZiSl9ai8AJ4eX8M1xuRmCUhC4OWZ2H4SPAwAee18Ru9jqCbVcy2_G6EHndjALZnE5KmrPNFF9VgC1DDnLDwZwrb4t5C3B04xqAMODQAplo2G5h4GIAGKISunon_PKXZLBOFEI6UMCoEKW-vI6Gg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2f8ebaf541.mp4?token=sJaZ4TjI12ndUnzYbsJVxDdRJjmyIMbS6M4I8MAfpa3XwCYqitGkhW54fqKktxy7w99JBizz6CKmBYq2ekJbuKrEhH6LW-cxCXFOOVJB_sbxSzVNrSmYoOZuHzjhR6GgV9VaN4yx8S117bHrihw_axtWzuMJSj9qiFIk9xGmidnrUR71gn6jrmeclILBpqJZ_iMZiSl9ai8AJ4eX8M1xuRmCUhC4OWZ2H4SPAwAee18Ru9jqCbVcy2_G6EHndjALZnE5KmrPNFF9VgC1DDnLDwZwrb4t5C3B04xqAMODQAplo2G5h4GIAGKISunon_PKXZLBOFEI6UMCoEKW-vI6Gg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
لليوم الثالث على التوالي..
استمرار المناورات الصاروخية الإيرانية في عدة مدن.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/naya_foriraq/93499" target="_blank">📅 11:30 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93498">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🇮🇶
مصدر امني عراقي لنايا
تغير بحركة القطعات العسكرية بالعاصمة بغداد حيث سوف يتم نقل الفرقة 17 جيش عراقي إلى كركوك و توجه قيادة وألوية الشرطة الاتحادية من كركوك إلى بغداد ، قاطع عمليات الفرقة ١٧ هو حاليا جنوب العاصمة بغداد يشمل المحمودية واليوسفية و مقتربات الـ دورة .
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/naya_foriraq/93498" target="_blank">📅 11:16 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93496">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rDbmmKmg066Qr8CTE41q0d7IjZjW4rsP-YHTyaaLDRwcane-CPhPN1wsIFLzI-v-Drq4P3znomlzygHjPZentV9AJgAlhXe9oFTqgAtwNwqghmw5nbI13vZGPYoVNmT6c2zCMFXQ3V6V1BmRHiecbLitlpzPrZ5v8NA1sNE8itPRLbA0DkJfsXqIXo1NXN2OZRZLCusYw5ISMuRmlPoI-8C7E9sLQjEZv862fZBxxYbgrqRpVJTD9Uf6kiriCgOQniG5FEey5kNep5mRnaGwrOFlQWYfbyr_MLirBi6P1DtgSAmgMfEQg6so599Jog50pJKFKZfLtW10wKytYZ4kIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
السيد مقتدى الصدر مغرداً بخصوص منع إرتداء الحجاب والمظاهر الإسلامية في دولة أذربيجان.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/naya_foriraq/93496" target="_blank">📅 11:08 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93495">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🔻
🇮🇷
🇷🇺
🇰🇼
On July 20, Naya’s Telegram
channel published a warning about an existential threat posed by a potential Iranian military ground invasion of Kuwait. At the time, a pathetic and failed Russian English-language channel came out to respond to Naya, gclaiming that such a scenario was impossible because there is no land border between Iran and Kuwait.
Today, the American newspaper
The Wall Street Journal
published an article mentioning Iran’s threat to invade Gulf countries if aggression against Iran resumes.
Here at Naya, we do not write without reason. I am Naya, and I know all the secrets behind the scenes.</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/naya_foriraq/93495" target="_blank">📅 10:21 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93494">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🇮🇷
إشتباكات بين القوات الامنية الإيرانية وعناصر إرهابية في منطقة تفتان بمحافظة بلوشستان جنوب شرق إيران؛ مقتل عدد من الإرهابيين كحصيلة أولية.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/naya_foriraq/93494" target="_blank">📅 10:14 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93493">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e7a00c4573.mp4?token=c9fOR23pskatBZae10r0XOCM6_AQWGnVrWPx5XKFud0QLXX-j9E2EKtPdRMqkWZBGZsTFhxXS8hLTJPoe9DJqm8KX8EkUIFHVEq-yGod9DWbj0aKVPn0-0oEvEQqGX2Bd3_6L5VTosL0kaZN8crLcELAmhtNk9v2mbKcHbq7CZfxIv4yNgH0JcAdlA1lUuOMHPWA5fo1sALQmqUmKmxVUi6Pg4J3kZuKfVaOAcf9glEYjXqMkN_sQtc_pG5i0Gue9Zdxs9CFQN5waMUeIL0IpJeZ8jaPk4ZNEWbvTTJtbOhP7Tz8GzVdisMe6xR2RBgmZz9vn8deq7bg0bsPLNRFUmhyyKSKiYiIPRMa306BZeVoRtIuMzpodRudsWgqwPTRLvWrecKEzytNGJWAl5ReSC2lw0YCPPZ6TT4O3gbXq7u7wU6khQPeDnUYoLX2C7JxGvpX-nmJPRVqhO5Vsi92ESzS8d8hgAUsbl1txYP8rtYlSB4h8F2ed0L3zm3gO4HtQ9-jWD3kfUN2k8v7odsFWxIID04fljTmTiFGj5a8-nGYs1aiCLyKZVBIVarVeJ5JaVWq0yeIiXQDlPFzTrLPQocBe18H7nOPzlJQlWWM3qRfM4KBe18g87GMLbnYzrqbGn62FANwz5N0Eg7qzTDnJFsp0zlMtT1HFLu03b-KJPk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e7a00c4573.mp4?token=c9fOR23pskatBZae10r0XOCM6_AQWGnVrWPx5XKFud0QLXX-j9E2EKtPdRMqkWZBGZsTFhxXS8hLTJPoe9DJqm8KX8EkUIFHVEq-yGod9DWbj0aKVPn0-0oEvEQqGX2Bd3_6L5VTosL0kaZN8crLcELAmhtNk9v2mbKcHbq7CZfxIv4yNgH0JcAdlA1lUuOMHPWA5fo1sALQmqUmKmxVUi6Pg4J3kZuKfVaOAcf9glEYjXqMkN_sQtc_pG5i0Gue9Zdxs9CFQN5waMUeIL0IpJeZ8jaPk4ZNEWbvTTJtbOhP7Tz8GzVdisMe6xR2RBgmZz9vn8deq7bg0bsPLNRFUmhyyKSKiYiIPRMa306BZeVoRtIuMzpodRudsWgqwPTRLvWrecKEzytNGJWAl5ReSC2lw0YCPPZ6TT4O3gbXq7u7wU6khQPeDnUYoLX2C7JxGvpX-nmJPRVqhO5Vsi92ESzS8d8hgAUsbl1txYP8rtYlSB4h8F2ed0L3zm3gO4HtQ9-jWD3kfUN2k8v7odsFWxIID04fljTmTiFGj5a8-nGYs1aiCLyKZVBIVarVeJ5JaVWq0yeIiXQDlPFzTrLPQocBe18H7nOPzlJQlWWM3qRfM4KBe18g87GMLbnYzrqbGn62FANwz5N0Eg7qzTDnJFsp0zlMtT1HFLu03b-KJPk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇶🇦
أمير دولة قطر:
إغلاق مضيق هرمز والأضرار في راس لفان أديا إلى تعطل مهم من صادرات الدولة.
تؤمن قطر نحو خمس تجارة الغاز الطبيعي المسال في العالم وما يمسها ينعكس على الأسواق والمستهلكين.
قطر تعرضت لاعتداء على أراضيها من جانب إيران في انتهاك صارخ لسيادتها.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/naya_foriraq/93493" target="_blank">📅 09:46 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93492">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🇮🇱
إعلام العدو: تم توجيه طائرة إلى مسار جانبي في مطار بن غوريون بعد تلقي بلاغ مجهول المصدر حول شحنة مشبوهة على متنها.  https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/naya_foriraq/93492" target="_blank">📅 09:27 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93491">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/70999657f3.mp4?token=pUsuYves_wx4QdQdt_aV_6lFR-Hf6v1qAfTfQeh3QNJ4ln3NOc0XcpmqMYMXBXw5rKqhSEQgU5x-QVls_CCU4zRhHtWrs4bV8r0jrh7JmAJC-oL81vgEHtfpZaYBQ7rQhF46RTkOCcyrvxDer_wOa5RFfNCc4PHcy2skHGFBeelBagnOQ9dr2FORDOQUhHq3M3BJSN9WLM9W8hIGMKuloCupqQcnwWwJGaHV1MQTv90yugk7MR2SSQWcAXeunohkZ_LrjEz2zgP460c0iVSTOJfg6Xn63hSXE_wXmBouV_Q3O2kk3H88X1Lvee19o81H-n2KrBnb8Ai2hUtxbe152A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/70999657f3.mp4?token=pUsuYves_wx4QdQdt_aV_6lFR-Hf6v1qAfTfQeh3QNJ4ln3NOc0XcpmqMYMXBXw5rKqhSEQgU5x-QVls_CCU4zRhHtWrs4bV8r0jrh7JmAJC-oL81vgEHtfpZaYBQ7rQhF46RTkOCcyrvxDer_wOa5RFfNCc4PHcy2skHGFBeelBagnOQ9dr2FORDOQUhHq3M3BJSN9WLM9W8hIGMKuloCupqQcnwWwJGaHV1MQTv90yugk7MR2SSQWcAXeunohkZ_LrjEz2zgP460c0iVSTOJfg6Xn63hSXE_wXmBouV_Q3O2kk3H88X1Lvee19o81H-n2KrBnb8Ai2hUtxbe152A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇱
إعلام العدو:
تم توجيه طائرة إلى مسار جانبي في مطار بن غوريون بعد تلقي بلاغ مجهول المصدر حول شحنة مشبوهة على متنها.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/naya_foriraq/93491" target="_blank">📅 09:26 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93490">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🔻
رئيس الوزراء البلغاري:
سفينتين قبالة ساحل بلغاريا في البحر الأسود تعرضتا لهجمات بطائرات مسيرة، وأدى ذلك إلى غرق إحدى السفينتين.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/naya_foriraq/93490" target="_blank">📅 09:17 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93489">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🇸🇦
🇾🇪
عدوان سعودي على محافظة صعدة اليمنية.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/naya_foriraq/93489" target="_blank">📅 09:16 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93488">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🇮🇷
وول ستريت جورنال:
حذرت إيران الدول الإقليمية من أن قواتها المسلحة قد تشن عمليات اقتحام برية إلى الدول المجاورة في حال اندلاع حرب جديدة؛ كما حذرت إيران مسؤولين عرب من أن منشآت النفط السعودية قد تتعرض للهجوم، مما يزيد من الهجمات التي يشنها بالفعل الحوثيون (أنصار الله) ضد منشآت النفط السعودية.
وتخطط إيران أيضًا لشن هجمات متزايدة ضد القوات الأمريكية في حال اندلاع حرب جديدة، بما في ذلك محاولة إغراق سفن تابعة للبحرية الأمريكية في غرب آسيا وقتل البحارة على متنها.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/naya_foriraq/93488" target="_blank">📅 08:38 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93487">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🇾🇪
العميد يحيى سريع:
تمكنت قواتنا المسلحة بفضل الله من إسقاط طائرة استطلاع مسلح نوع "وينق لونق 2" (Wing Loong II) تابعة للعدو السعودي وذلك أثناء قيامها بمهام عدائية في أجواء  محافظة صعدة، وقد تم استهدافها بسلاح مناسب.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/naya_foriraq/93487" target="_blank">📅 06:28 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93486">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🇮🇷
دوي إنفجارات في مضيق هرمز وسط أنباء عن إستهداف سفينة مخالفة لقوانين المرور الإيرانية.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/naya_foriraq/93486" target="_blank">📅 04:09 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93485">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🇺🇸
‏ترامب عن إيران: ليس لديهم أسطول بحري؛ وليس لديهم سلاح جو. التضخم مرتفع للغاية.</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/naya_foriraq/93485" target="_blank">📅 03:51 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93484">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e2a6182b81.mp4?token=WvgBbs7qrWy3j-yGox__eVaSM_etDFu_6aE_8NxkGtvI1tZWWp16_HwIQBOyDd5Jwrjj7fNpIZ1qOsbvXMs1O6fvPQmZrImnL00x6Eoe3ygIQ8U-CfkYzXLJR--RUnJ0e1_qAXMzNbA_cE7wAEu-GCFtti7OpAoaktFamfeUut1VUCRSpXzgyKUIHsj3A-jiMKCCOV7m78IrgwwrVKpeMzq0KTBxUNdhHXXwuh4AALMvquXB00TPA2i4pylq4N6pqJfueccbZBQ-dplHsWn3BOf7sY2BJ_DPlu9qa5VCjghx5cpVkH5-15xfKXVWKzPqJbQL-BvVvkEMnf_f1AMn0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e2a6182b81.mp4?token=WvgBbs7qrWy3j-yGox__eVaSM_etDFu_6aE_8NxkGtvI1tZWWp16_HwIQBOyDd5Jwrjj7fNpIZ1qOsbvXMs1O6fvPQmZrImnL00x6Eoe3ygIQ8U-CfkYzXLJR--RUnJ0e1_qAXMzNbA_cE7wAEu-GCFtti7OpAoaktFamfeUut1VUCRSpXzgyKUIHsj3A-jiMKCCOV7m78IrgwwrVKpeMzq0KTBxUNdhHXXwuh4AALMvquXB00TPA2i4pylq4N6pqJfueccbZBQ-dplHsWn3BOf7sY2BJ_DPlu9qa5VCjghx5cpVkH5-15xfKXVWKzPqJbQL-BvVvkEMnf_f1AMn0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇾🇪
🇸🇦
مشاهد لاستهداف القوات اليمنية المسلحة مدينة الرياض وسط السعودية.</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/naya_foriraq/93484" target="_blank">📅 03:43 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93483">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🇾🇪
🇸🇦
مشاهد لاستهداف القوات اليمنية المسلحة مدينة الرياض وسط السعودية.</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/naya_foriraq/93483" target="_blank">📅 03:18 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93482">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🇶🇦
🇸🇦
‏أعلنت الخطوط الجوية القطرية تعليق رحلاتها من وإلى مطاري الرياض والدمام في السعودية.</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/naya_foriraq/93482" target="_blank">📅 02:24 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93481">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🔻
أنباء عن أصوات طائرات مسيرة تحلق في اربيل شمال العراق.</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/naya_foriraq/93481" target="_blank">📅 01:57 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93480">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🇺🇸
‏
ترامب عن إيران:
ليس لديهم أسطول بحري؛ وليس لديهم سلاح جو. التضخم مرتفع للغاية.</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/naya_foriraq/93480" target="_blank">📅 00:35 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93479">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">كوريا الشمالية: الأعلان عن تجربة إطلاق صاروخ باليستي تكتيكي</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/naya_foriraq/93479" target="_blank">📅 00:33 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93478">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a9bdc6dbff.mp4?token=fVFZ2r17KVkpgFdM-Y_uupRao5Y14V7nC-6wn1PqI7CT0jBLXiidcvZdR5gQEJDFf9zSV-LKXN-5FlLy72wp-h8e50rJHQfo5EwZj9FvlJYznYfdhiVgvHXb7569jMo6t7t1D8YX7hGp-McatgkGv2Eiibwjn2HRY_uXFDFX9Q-PYHqK4x--LnydFl_CnI854HJ__udEOkIKTyto6VFhG0el_0_B0kMb4xPLaGTVvdpbrslvyrKi1sypC1HECU7xHuoZ07e_WfHbiT9P1BTrvtFw-fg32dIfJOoxygFzKizsz-jf3l6vQ6exfEV0NVcZ9jtzGiXo10ADq1BFYOL6bg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a9bdc6dbff.mp4?token=fVFZ2r17KVkpgFdM-Y_uupRao5Y14V7nC-6wn1PqI7CT0jBLXiidcvZdR5gQEJDFf9zSV-LKXN-5FlLy72wp-h8e50rJHQfo5EwZj9FvlJYznYfdhiVgvHXb7569jMo6t7t1D8YX7hGp-McatgkGv2Eiibwjn2HRY_uXFDFX9Q-PYHqK4x--LnydFl_CnI854HJ__udEOkIKTyto6VFhG0el_0_B0kMb4xPLaGTVvdpbrslvyrKi1sypC1HECU7xHuoZ07e_WfHbiT9P1BTrvtFw-fg32dIfJOoxygFzKizsz-jf3l6vQ6exfEV0NVcZ9jtzGiXo10ADq1BFYOL6bg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏ترامب: الحوثيون يتصرفون بشكل سيء للغاية</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/naya_foriraq/93478" target="_blank">📅 00:30 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93477">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lEmzvzquqdkJBjxNQy_gNjkCUWmmMs3vmEPLZhiwefYVG0Ll735QcUlqjLm1cT9GJYN8UxDzD9o5IWUh3qtyMCBPtTcNBLabsu2QuD7H-dmwIzfS8Np_Q3GAGRuA6T7IowPyxzZ3u7e3DpgyYZHysztLZfDDFCBwxC31fjskXCuimG78X5px16p44th5wqRye92rryRLPYIjWizANj0Cv38p5_5y7T6mSyD8b65S3URFvgNs4QiPQVPs4_SGNWtZvwbdTK4xc7NqCjbAP4f5wILgD_i7_8GP9y09AUZRbUufByweAdwD0k7CJvUTmM7F-LJ5EGsQeaABVhOWuu0TKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏طالبة محجبة وصديقاتها في أذربيجان حُرمت من حقها في التعليم بسبب ارتدائها الحجاب بعد ان اصدر الرئيس الاذربيجاني إلهام علييف الموالي للصهاينة قرارا بمنع الحجاب في التعليم بسبب ما اسماه بـ"الحجاب ثقافة عربية وفارسية".</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/naya_foriraq/93477" target="_blank">📅 00:26 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93476">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">انفجارات تهز خميس مشيط</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/naya_foriraq/93476" target="_blank">📅 00:24 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93475">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">انفجارات تهز أطراف الرياض الان</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/naya_foriraq/93475" target="_blank">📅 00:16 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93474">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">سماع دوي انفجار في الدمام</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/naya_foriraq/93474" target="_blank">📅 00:12 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93473">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">سماع دوي انفجار في الدمام</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/naya_foriraq/93473" target="_blank">📅 00:11 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93472">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🇾🇪
انباء عن عدوان يستهدف العاصمة اليمنية صنعاء.</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/naya_foriraq/93472" target="_blank">📅 23:58 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93471">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mS_GwLCa0CB7J9iR8JdGwIztWDxT29fD92eSvYaY9A2JJHe_NIANG7a6sHnmGY3_frVkMyxioYW2rsUjaiCLF2tFMYnc_pvbCW6_ajjRf3OVr267Y2PNZlu0DnhUH3eUFrhZaV6utkylf0I6JY5qzNGx-4Va_-9OPckQZZtGtJeWJxKTReOujAosPW6EC2VUKJSEO1wzUGIEeGMjLh5bDCnVgcJfqcIE2ccwZ55ZAiWehocNFQm5hZD2j57WJ6pmrRFMRQrF4Nha7KJhse9-QkNmEj8Crlbuhg-rG4d3KxINBGLErCEIAd3r71Em0Tt9FDutCNAhta7c3IFQ2h0Qhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
🇸🇦
🇾🇪
جروك يرد على موظفي مركز اعتدال السعودي
🔻
حتى الذكاء الصناعي لدى إيلون ماسك بدأ يعاني من إفهام الذباب الإلكتروني السعودي</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/naya_foriraq/93471" target="_blank">📅 23:57 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93470">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">انفجارات تهز خميس مشيط</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/naya_foriraq/93470" target="_blank">📅 23:49 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93469">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">نايا - NAYA
pinned «
🔻
لمتابعة المشاهد الحصرية التي تحصل عليها نايا من داخل السعودية يُرجى متابعة حسابنا على منصة «إكس». اضغط هنا
🔻
To follow the exclusive footage NAYA obtains from inside Saudi Arabia, please follow our account on X. Click here
🔻
برای دنبال کردن تصاویر اختصاصی…
»</div>
<div class="tg-footer"><a href="https://t.me/naya_foriraq/93469" target="_blank">📅 23:33 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93468">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nOOr9ahKLE6bcfau55_d-b_lBPJ9ZqPcZ1e_JswN8eLq_dJ0MYw78AmIUwQc8_xhlKeS1Z6ec5mfA_n5BbueXDoOyB0JWEnjoJZ0ih5n6WAB90409qQVvt-c_6uEZtKdM_aVpenUzlSnkizLKcuOXfS6Xw031fqQU_VAi39qGJG1mEHdmLkz0HcjusiOFzeWbAdOOEOgZgZ-5zHY-WN16CixyFtesnZpLo-W129b_cNxo0o87RRrkaGXmBYMhUDAj6HHqS5jfnvNQUVqgftwWEVWssQoNvdIqZc1_N1XorKBSXX50ZDnIVEH859LQo9SxWA27agahR8i9O3BUhytrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇸🇦
السعودية مجددا تتوسل بالمواطنين للإبلاغ عن وصول المسيرات والصواريخ
😭
.
رابط التغريدة
ليلة هادئة جدا في الرياض
😆
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/naya_foriraq/93468" target="_blank">📅 23:30 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93467">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🔻
لمتابعة المشاهد الحصرية التي تحصل عليها نايا من داخل السعودية يُرجى متابعة حسابنا على منصة «إكس».
اضغط هنا
🔻
To follow the exclusive footage NAYA obtains from inside Saudi Arabia, please follow our account on X.
Click here
🔻
برای دنبال کردن تصاویر اختصاصی که نایا از داخل عربستان سعودی دریافت می‌کند، لطفاً حساب ما را در پلتفرم ایکس دنبال کنید.
اینجا کلیک کنید</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/naya_foriraq/93467" target="_blank">📅 23:22 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93465">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AZvrlk5hwxvfD4OBghhpgL6-Plq1ttZNHyacbYpQiH60175tMczO_I7D4LelmuPdsEBDSrJzKj1H9DmNHJQ5XGCTexHidkbjiq92zk1H1hFkZQlIwmCC-J7mBxPeVD8TjCUWH1HSIz2YWdwJqS-3GM5LnTPWlIKT624l6-GIthWVVnUBf1sUj1CRplB9uLtIZ3puKF5cX6-zHRcY9oQr0WfUiXNa8UBsekpl_gVq_-Rk9YRO00sP9JX2D4_oIveChZNlw32jxhwG8jGcWWlKvtT-swjjyEkELwtdzBUiG2hdOF9FQNK9wswuIHlFuZnTvnfw2sUoqDizP6UBmkRbTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الرياض فارغة بانتظار صواريخ انصار الله
رابط التغريدة</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/naya_foriraq/93465" target="_blank">📅 23:19 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93464">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ad0902f6a.mp4?token=M91QXFuWX5qPlz2XGTmHSoSXw7KfUgiZxz9KZIMU7DrvfZE-qWbMlAE0A5mO_eHvvJMIGkd96xR_8i6bEHVBCOaJzj3SGvKYG817uwg14tKYwcnaRQRx3ZU1sjC_qos2qnggNZ3kxL5w6IcULEI_QXd8VoOqOezl8BKuCrNLMwRC9aiegjSJNicL8a8KufAmOHujE0xxDCspgP8CsIrR2GtC863w4zUvxvZeniGaPcj8Pvdfp4eaC8xygRnEMeikNc_a1LOUy_rkQlXr1xQ7y_KVK5QPTlyXO9XZ2aIwgqtLO3IiVKHDl7I8AJOzThUnE3xDUMQXKW9J8eSA8JqGvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ad0902f6a.mp4?token=M91QXFuWX5qPlz2XGTmHSoSXw7KfUgiZxz9KZIMU7DrvfZE-qWbMlAE0A5mO_eHvvJMIGkd96xR_8i6bEHVBCOaJzj3SGvKYG817uwg14tKYwcnaRQRx3ZU1sjC_qos2qnggNZ3kxL5w6IcULEI_QXd8VoOqOezl8BKuCrNLMwRC9aiegjSJNicL8a8KufAmOHujE0xxDCspgP8CsIrR2GtC863w4zUvxvZeniGaPcj8Pvdfp4eaC8xygRnEMeikNc_a1LOUy_rkQlXr1xQ7y_KVK5QPTlyXO9XZ2aIwgqtLO3IiVKHDl7I8AJOzThUnE3xDUMQXKW9J8eSA8JqGvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
🇸🇦
مشاهد غير محدودة لنايا
😎
من الهجمات التي طالت الرياض قبل قليل.  https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/naya_foriraq/93464" target="_blank">📅 23:04 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93463">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57f2d20cb2.mp4?token=O-jyuGDrqPdbSqSy2FYznKeppzwxCeWgLxBnRBOVo52CtJ_XJc929Du-xzpydWRUP2DG5QShmRBuuuybkNVtIJD82LWpzJuUZEw-2M4CXXtdjRiLXqQAN4wyFXI_PsKcFSeLR7QYNXao2rhv7ezdzDnbTxQA8Ylks4N8e2QqUmo6PuLR-nLHTdQ27fUwpYQPtKlrORw3MYOv_MLZTD-d5HTl-XvKrNnxf-dRMy4IZIwPmkUD-8t0LtgCkYofsvdoRzH6oFQB07KVRKfatUnmmSmMeHM-FXQHbR08AVPd2hh4yvU219A7sT9TURRsAQQY5g08AkMIGtCcxZnzAENVrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57f2d20cb2.mp4?token=O-jyuGDrqPdbSqSy2FYznKeppzwxCeWgLxBnRBOVo52CtJ_XJc929Du-xzpydWRUP2DG5QShmRBuuuybkNVtIJD82LWpzJuUZEw-2M4CXXtdjRiLXqQAN4wyFXI_PsKcFSeLR7QYNXao2rhv7ezdzDnbTxQA8Ylks4N8e2QqUmo6PuLR-nLHTdQ27fUwpYQPtKlrORw3MYOv_MLZTD-d5HTl-XvKrNnxf-dRMy4IZIwPmkUD-8t0LtgCkYofsvdoRzH6oFQB07KVRKfatUnmmSmMeHM-FXQHbR08AVPd2hh4yvU219A7sT9TURRsAQQY5g08AkMIGtCcxZnzAENVrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇾🇪
🇸🇦
مشاهد حديثة قبل قليل لانطلاق الدفاعات الجوية من وسط الرياض.  الشكر لمراسلينا
😎
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/naya_foriraq/93463" target="_blank">📅 22:50 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93462">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🇷🇺
بالتزامن مع الهجوم على الرياض
موسكو تهاجم كييف الان بالصواريخ البالستية .
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/naya_foriraq/93462" target="_blank">📅 22:46 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93461">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">نايا - NAYA
pinned «
فجر ساخن جدا   https://t.me/naya_foriraq
»</div>
<div class="tg-footer"><a href="https://t.me/naya_foriraq/93461" target="_blank">📅 22:45 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93460">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🔻
الاعلام الاوروبي:
تبحث المملكة العربية السعودية عن أسباب فشل أنظمة الدفاع الجوي في إيقاف هجمات الطائرات المسيرة والصواريخ التي شنها الحوثيون على مطار الرياض، والتي أسفرت عن مقتل ما لا يقل عن 13 شخصًا وإصابة أكثر من 300 آخرين.
أظهرت التحقيقات الأولية أن الحوثيين استخدموا الطائرات المسيرة لتسهيل مهمة صواريخ كروز والصواريخ الباليستية.
تسعى الرياض إلى زيادة مشاركة الولايات المتحدة العسكرية ضد الحوثيين، بينما يدرس الرئيس ترامب إمكانية شن ضربات.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/naya_foriraq/93460" target="_blank">📅 22:41 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93459">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🇸🇦
🇾🇪
لاول مرة منذ اندلاع المواجهة مع الشعب اليمني
وزارة الدفاع السعودية تنشر تنويه بسبعة لغات تضمنت " الهندية ؛ الفلبينية ؛ الاوردو ، البنجابي ، البنغلاديش ، الإنكليزية " تدعو بها المقيمين عدم نشر الفديوهات اثناء القصف التي تظهر فشل منظومات الدفاع الجوي الحديثة لدى السعودية و فشلها بالتصدي لهجمات القوات المسلحة اليمنية .
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/naya_foriraq/93459" target="_blank">📅 22:39 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93458">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🇬🇧
🇺🇸
‏
وزيرا خارجية أميركا وبريطانيا:
يجب محاسبة إيران على أفعالها.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/naya_foriraq/93458" target="_blank">📅 22:39 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93457">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🇮🇱
الاعلام العبري:
يسعى نتنياهو إلى وساطة أمريكية لإقناع المملكة العربية السعودية بالسماح بمشاركة عسكرية إسرائيلية ضد الحوثيين في اليمن، على أمل تعزيز العلاقات وتهيئة الطريق نحو تطبيع العلاقات.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/naya_foriraq/93457" target="_blank">📅 22:38 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93456">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🇾🇪
العميد يحيى السريع:
بفضل الله وعونه تمكنت قواتنا المسلحة من استهداف مطار خالد الدولي في عاصمة العدو السعودي الرياض مساء اليوم بصاروخ باليستي وكانت الإصابة دقيقة.
نجدد تحذيرنا لكافة شركات الطيران العالمية وجميعِ الخبراء والموظفين والعاملين والمسافرينَ من كلِّ دولِ العالمِ من مغبةِ تسييرِ الرحلاتِ باتجاهِ المطاراتِ السعوديةِ فإنها غيرُ آمنةٍ باستثناءِ مطاراتِ وأجواءِ المناطقِ المقدسةِ في مكةَ المكرمةِ والمدينةِ المنورةِ.
وفي سياق متصل نفذت القوات المسلحة عملية استهداف لقاعدة خميس مشيط الجوية بطائرة مسيرة وكانت الإصابة مباشرة بفضل الله.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/naya_foriraq/93456" target="_blank">📅 22:32 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93455">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🔻
If you want to see our Video inside KSA join us in “ twitter “
🔻
https://x.com/nayaixa3/status/2109720131270275359?s=46</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/naya_foriraq/93455" target="_blank">📅 22:30 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93454">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b80ec7f71a.mp4?token=wBLOSdGTkxEto3oCK-IBSuI8HdzgxlccJCot2jdwPk8kZJdPo8F0HLvnWjepEHujENPF5OhMXELQhA4TC-Z32MVr0JwKQtJBCPHVqz9FA9f0g8BtZmAWx4ze-iqowJGGIAiHvB1LHzltXrViEN_LhnhYTsrRMam4k_zNnDwiAetvuVlPOJc-QrjBCr7PfDnJjPNCfIGFiWgToBXmo41dXGgT0InK50MG_UvEkyUnuEZ2MyGsHMiUw6D3ek_kyWYUyfOQYrz4wS2_SQOoruYdxzDVSUTaGNckH6V0wUlDKmaMylzuWiLl44uvc3H24RDloM77XnnPktJYtx7eQjWVzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b80ec7f71a.mp4?token=wBLOSdGTkxEto3oCK-IBSuI8HdzgxlccJCot2jdwPk8kZJdPo8F0HLvnWjepEHujENPF5OhMXELQhA4TC-Z32MVr0JwKQtJBCPHVqz9FA9f0g8BtZmAWx4ze-iqowJGGIAiHvB1LHzltXrViEN_LhnhYTsrRMam4k_zNnDwiAetvuVlPOJc-QrjBCr7PfDnJjPNCfIGFiWgToBXmo41dXGgT0InK50MG_UvEkyUnuEZ2MyGsHMiUw6D3ek_kyWYUyfOQYrz4wS2_SQOoruYdxzDVSUTaGNckH6V0wUlDKmaMylzuWiLl44uvc3H24RDloM77XnnPktJYtx7eQjWVzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">السعودية تفقد السيطرة على الهنود
😆
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/naya_foriraq/93454" target="_blank">📅 22:30 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93451">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/06004d882c.mp4?token=MWH_qVlExeQEVcPMPIbfxNLVOUXrPBaluE40QYhpUA6pVbAVJP9QBFLrVeyQoYGcSE7JjvoSu8XXI5UJAva2frwqMlEqsBLEAVRLOVB3l_-1QqeEYcyD8ZGkV07VJ1sIT09N7b-vWaM8zqt9AdD95jS2icdrqvOBHr9E0gWexaq15sYKMDJV1qFSj68wvWdELhDM5FarW-OUa_J5TSIkSS8KmtSSul-FFVWVGg4F9RE8JW97jZmrldDaU07d9jxJM44mUszdCnzqxtKaqUYfj-jRs2Gvw-xoWjb73XaSR06o2HLdaHeIi85Jccg5ZIT7rm1YJB55CIjyfKcDv6_uLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/06004d882c.mp4?token=MWH_qVlExeQEVcPMPIbfxNLVOUXrPBaluE40QYhpUA6pVbAVJP9QBFLrVeyQoYGcSE7JjvoSu8XXI5UJAva2frwqMlEqsBLEAVRLOVB3l_-1QqeEYcyD8ZGkV07VJ1sIT09N7b-vWaM8zqt9AdD95jS2icdrqvOBHr9E0gWexaq15sYKMDJV1qFSj68wvWdELhDM5FarW-OUa_J5TSIkSS8KmtSSul-FFVWVGg4F9RE8JW97jZmrldDaU07d9jxJM44mUszdCnzqxtKaqUYfj-jRs2Gvw-xoWjb73XaSR06o2HLdaHeIi85Jccg5ZIT7rm1YJB55CIjyfKcDv6_uLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇦
🇾🇪
مشاهد جديدة غير متداولة من استهدافات التي طالت الرياض ظهر اليوم.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/naya_foriraq/93451" target="_blank">📅 22:30 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93450">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">استهداف سفينة اخرى في مضيق هرمز  الله اكبر  https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/naya_foriraq/93450" target="_blank">📅 22:27 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93449">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">الله اكبر
▫️
استهداف سفينة ثانية في مضيق هرمز واندلاع حريق كبير فيها.  https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/naya_foriraq/93449" target="_blank">📅 22:25 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93448">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🇾🇪
جولة ميدانية من مركز مديرية المسراخ لمراسل الإعلام الحربي - 12 أكتوبر 2026م
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/naya_foriraq/93448" target="_blank">📅 22:25 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93447">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/53b0c970cd.mp4?token=T6SyQZ7_b9xHj4UOtj10_VRMWZ4FnqLkiZ-wXXfxMitXRISDou0PUu5Wx5-9zsSiT5YRsIjHrJp83OKsVjx4uel1EwgdCuQF0Ak1MLapznJIanY_mqTne_fIg5kyX2-gpHo7SOcgQdxNv0FeyHvAXf_MgxUGB4GK-z9c2DVCZX1GiSoxU50TFtNwEQs2xUSTsvJES9KFHFywwdvxA56bh-7-ZR0wZMlq4SM5S02YITt6m0CiSLSZRKDLT-EGfAS3X0JPKHLP5NBsLhZ0AbN_Z7YX-7pcABdAcOG9_KGzDXlr2HlqJAofeMIOqpNLTf8WN73zpp2fB7P5fZLB-tAGEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/53b0c970cd.mp4?token=T6SyQZ7_b9xHj4UOtj10_VRMWZ4FnqLkiZ-wXXfxMitXRISDou0PUu5Wx5-9zsSiT5YRsIjHrJp83OKsVjx4uel1EwgdCuQF0Ak1MLapznJIanY_mqTne_fIg5kyX2-gpHo7SOcgQdxNv0FeyHvAXf_MgxUGB4GK-z9c2DVCZX1GiSoxU50TFtNwEQs2xUSTsvJES9KFHFywwdvxA56bh-7-ZR0wZMlq4SM5S02YITt6m0CiSLSZRKDLT-EGfAS3X0JPKHLP5NBsLhZ0AbN_Z7YX-7pcABdAcOG9_KGzDXlr2HlqJAofeMIOqpNLTf8WN73zpp2fB7P5fZLB-tAGEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇦
🇾🇪
مشاهد اخرى من توثق لحظات اطلاق الدفاعات الجوية السعودية لمحاولة اعتراض الصواريخ اليمنية.  https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/naya_foriraq/93447" target="_blank">📅 22:23 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93446">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ecd4c20bdb.mp4?token=LCo-tI_BhsnBR6WNmpcCNpT6PVzeL9ouO22HZqD5DWmE6nHRxyE5A2f8eTzqFRpNvmQolZIwLJHxlqwW2mD8Q4vH0dTSPcWGqoL97FYmpFpjkRMH5U7N63-3ztRBx9dJdx4WbWEUZxg79J-0YsnP0ZB_GbVfZbFe9wxJPGgVnAe6yrBPdNDW0cYYes7YcJtL4Lam1srb5OO7R0CKJfFKvj6WZvW3kFVsJgQzhrxei1jb1dPU3rd5nQKZVUJ03PFm55INEmImFAVJjn00oZP7Ef9KNlUWhVOY8_wnUgWsqpPfdNh9unhYXy23zFIqJ95Z1FlHIKeB8OngCtpXMInKCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ecd4c20bdb.mp4?token=LCo-tI_BhsnBR6WNmpcCNpT6PVzeL9ouO22HZqD5DWmE6nHRxyE5A2f8eTzqFRpNvmQolZIwLJHxlqwW2mD8Q4vH0dTSPcWGqoL97FYmpFpjkRMH5U7N63-3ztRBx9dJdx4WbWEUZxg79J-0YsnP0ZB_GbVfZbFe9wxJPGgVnAe6yrBPdNDW0cYYes7YcJtL4Lam1srb5OO7R0CKJfFKvj6WZvW3kFVsJgQzhrxei1jb1dPU3rd5nQKZVUJ03PFm55INEmImFAVJjn00oZP7Ef9KNlUWhVOY8_wnUgWsqpPfdNh9unhYXy23zFIqJ95Z1FlHIKeB8OngCtpXMInKCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تم اعتراض جميع الصواريخ:  https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/naya_foriraq/93446" target="_blank">📅 22:22 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93445">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d2d642d2db.mp4?token=qqhLTUaFNR9twO_BOfSc0aCbwb-8bpYkow-wA4f_7bU4h2BmNuPIyxKnDodb1VDv1-SqVWvocTz0zXrQtpkE6_430L2mSkzwG-7f9U9DrasjBwhtk2GRpNFfV_CH09y0CsGa4dlxdkMYjywn__mE8DlnTCy0WGkkUv0j_YH2Wv25_-F9D3ZtBLtFpKLIyLr9vBkOK71Bv-KIR_LAJbJMEeQnP1M0h-i9CjJqYWEBw8FdBPQZXpRsvWD5nUq4j_kR8KA1_vCQa0ao_X3knxyFW2SJ3LDm5fKprMRnRPN6fcOGP-9r2mQ2ShmFTxW5RgGhPNg__dGNz0eBaGGKY4e8aQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d2d642d2db.mp4?token=qqhLTUaFNR9twO_BOfSc0aCbwb-8bpYkow-wA4f_7bU4h2BmNuPIyxKnDodb1VDv1-SqVWvocTz0zXrQtpkE6_430L2mSkzwG-7f9U9DrasjBwhtk2GRpNFfV_CH09y0CsGa4dlxdkMYjywn__mE8DlnTCy0WGkkUv0j_YH2Wv25_-F9D3ZtBLtFpKLIyLr9vBkOK71Bv-KIR_LAJbJMEeQnP1M0h-i9CjJqYWEBw8FdBPQZXpRsvWD5nUq4j_kR8KA1_vCQa0ao_X3knxyFW2SJ3LDm5fKprMRnRPN6fcOGP-9r2mQ2ShmFTxW5RgGhPNg__dGNz0eBaGGKY4e8aQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇦
🇾🇪
مشاهد حصرية لنايا توثق سماء العاصمة السعودية الرياض قبل قليل.  https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/naya_foriraq/93445" target="_blank">📅 22:19 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93444">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fee472b449.mp4?token=g5snT434LLDVLvE_21mecT5CZmtQQ1ZTa6ip64CcAKXDbfX9EY4e0cabVYtSQn8hasxWk0k9k2SQgBzNk-2Krnnlv-SszqUXuEyjCCHs6DlD1VrGt5fuCXWC81tCkhw8zWBDHh_h3gPWx0X3dcXyvAq3L7OkGJYendcEJiVtQ3v7oaAY9Voxv0cvfa1cE7KwkuOc62t_CfquWvJD4d3-F1KDLZ10XZTeRzcsjGhWOKIVMaGkgB8-2rXgBjv-mopZ42Yuezs2apCJtCXxIQkPNoQHmTk3W2gb1SkBqk-K9RnfKJJREH4pLAScc9hzJq7SggcDosJASCUe-OQ3tvYqhg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fee472b449.mp4?token=g5snT434LLDVLvE_21mecT5CZmtQQ1ZTa6ip64CcAKXDbfX9EY4e0cabVYtSQn8hasxWk0k9k2SQgBzNk-2Krnnlv-SszqUXuEyjCCHs6DlD1VrGt5fuCXWC81tCkhw8zWBDHh_h3gPWx0X3dcXyvAq3L7OkGJYendcEJiVtQ3v7oaAY9Voxv0cvfa1cE7KwkuOc62t_CfquWvJD4d3-F1KDLZ10XZTeRzcsjGhWOKIVMaGkgB8-2rXgBjv-mopZ42Yuezs2apCJtCXxIQkPNoQHmTk3W2gb1SkBqk-K9RnfKJJREH4pLAScc9hzJq7SggcDosJASCUe-OQ3tvYqhg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇦
🇾🇪
الصواريخ تصول في سماء الرياض متجه نحو هدفها  https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/naya_foriraq/93444" target="_blank">📅 22:15 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93443">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/230d30c017.mp4?token=u_bSRLvGpOsoyHyBxFEvKKq3m4rpZWjRuAtsg52ndvtovLU5qhfayoa8obgFOOefoE_oAi2Y_va0B7kZK3xIHmIT-HzUoSqMEuP91zT7ZWP_2EQ46F1Lo5-WzTBeDExEcTVDy3nxDgIFLQt5L8lquK0aoudvSmi_7kjRNFqgvM2VohCFgm7jJP_bqXWL11CRG08UkAS0sl-6D64h9mB08dGYWpe5bNAmxNO9wuRxQ662LhYiZ7_nwChtELkwZhGAWKiT6jkcoeiEQL9KDR-dMvmBElgIQRmMuolYbXvNL9GmdYjQZVFDRARq_kLOksDrKBJmI1uSG7iWXvVNdaPu5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/230d30c017.mp4?token=u_bSRLvGpOsoyHyBxFEvKKq3m4rpZWjRuAtsg52ndvtovLU5qhfayoa8obgFOOefoE_oAi2Y_va0B7kZK3xIHmIT-HzUoSqMEuP91zT7ZWP_2EQ46F1Lo5-WzTBeDExEcTVDy3nxDgIFLQt5L8lquK0aoudvSmi_7kjRNFqgvM2VohCFgm7jJP_bqXWL11CRG08UkAS0sl-6D64h9mB08dGYWpe5bNAmxNO9wuRxQ662LhYiZ7_nwChtELkwZhGAWKiT6jkcoeiEQL9KDR-dMvmBElgIQRmMuolYbXvNL9GmdYjQZVFDRARq_kLOksDrKBJmI1uSG7iWXvVNdaPu5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇦
🇾🇪
مشاهد حصرية لنايا توثق انطلاق الدفاعات الجوية السعودية قبل قليل في محاولة منها لاعتراض الصواريخ اليمنية.  https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/naya_foriraq/93443" target="_blank">📅 22:14 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93442">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Audio</div>
  <div class="tg-doc-extra"></div>
</div>
<a href="https://t.me/naya_foriraq/93442" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">قولو له الرياض اقرب</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/naya_foriraq/93442" target="_blank">📅 22:13 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93441">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cfbac31622.mp4?token=p9wOU4V8reOD0HHKouP_4whLz7YhCS4OIOyta8CxjKG0EV4MXIlScos6cjyN7-PugQynqTVxb1K42SulJqmX4mCS1RuyIMj4vtNcxW1wHPSLElMS4idhFTFIJn3I4Xh0cXsLH7K6VtUSfDCQ1QcSumfUCJWC6c5bo-7aZRWKMsAmRAt_GFUQR32dOsIkGDQF85NliCgLCcW-72ZyeQDjlq0ins6gFK65yPjOuRl_j9chsh8K-toF5fNipwaVaimSVFFBoOolrx-C_CJ-ZahffQdxj_m_F-ToN1477llCt6mlaM4ak5mT6yQ6iba6DInl6UV9BEwPCd3QOXMy9sMavQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cfbac31622.mp4?token=p9wOU4V8reOD0HHKouP_4whLz7YhCS4OIOyta8CxjKG0EV4MXIlScos6cjyN7-PugQynqTVxb1K42SulJqmX4mCS1RuyIMj4vtNcxW1wHPSLElMS4idhFTFIJn3I4Xh0cXsLH7K6VtUSfDCQ1QcSumfUCJWC6c5bo-7aZRWKMsAmRAt_GFUQR32dOsIkGDQF85NliCgLCcW-72ZyeQDjlq0ins6gFK65yPjOuRl_j9chsh8K-toF5fNipwaVaimSVFFBoOolrx-C_CJ-ZahffQdxj_m_F-ToN1477llCt6mlaM4ak5mT6yQ6iba6DInl6UV9BEwPCd3QOXMy9sMavQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇦
🇾🇪
مشاهد حديثة من سماء العاصمة السعودية الرياض بالتزامن مع انطلاق الدفاعات الجوية.  https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/naya_foriraq/93441" target="_blank">📅 22:10 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93440">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/efbd8766f2.mp4?token=R5xu1pDCY13auRPb3UYoeDdqLlMqgmATGxlW8rLZ1asT9dbW8HYxLovIvVx0d7kpVyudSdILRJ2wHV5rf-Qpge-yAJVMbfPE5glU5fqc1_JOlI9R9bE621kZsTG6_g0cxVI4cBNUXEvBZg3_zH6oy2_L6Idx2Qb2xZJLEhhMajHZGYsiwC_CNVScPnKEmH4RxXnrFqehTeUQxp6R37r3lMqEUf2D9RnliRjuI7RX4h_JIqLW4QqW7sZ4bktLXlPbt5g_bm8HFR5w80QDhl_aHft_0p8oq2g7F0zjNTxj2TwcxYVB2pqglg__ojeCEahtVOT7gsRw-5RRGmektF8VUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/efbd8766f2.mp4?token=R5xu1pDCY13auRPb3UYoeDdqLlMqgmATGxlW8rLZ1asT9dbW8HYxLovIvVx0d7kpVyudSdILRJ2wHV5rf-Qpge-yAJVMbfPE5glU5fqc1_JOlI9R9bE621kZsTG6_g0cxVI4cBNUXEvBZg3_zH6oy2_L6Idx2Qb2xZJLEhhMajHZGYsiwC_CNVScPnKEmH4RxXnrFqehTeUQxp6R37r3lMqEUf2D9RnliRjuI7RX4h_JIqLW4QqW7sZ4bktLXlPbt5g_bm8HFR5w80QDhl_aHft_0p8oq2g7F0zjNTxj2TwcxYVB2pqglg__ojeCEahtVOT7gsRw-5RRGmektF8VUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇾🇪
🇸🇦
صاروخ باليستي يمني يطلق نحو الرياض</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/naya_foriraq/93440" target="_blank">📅 22:07 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93439">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/21384b098a.mp4?token=ssi-zfzRH9CPLX0lVSbgKH_mpV3RL8P-JV-J_KbCQlTJLBPTZY2jT9FyG350S7XE25eTqYW7Z2Zfk1Ju7UpZZq-sJsSrAhz0YfdF-wJQocLkQkcXwUyukwGHIrvTvHRAIyBNjJ8w9I3czXUALdJsOhUwKIuPi2COwerrx5SiBm3HHYT5k-YguKxt75hKPwfl6aCm3XEX0Ew9e_AFQS28-aR6ir76tB-xwD_yeMu7gCIYCmEPfB-IoHJfNSOoRs3ImVh41CCVqQ5r_2TmNmFHgOIo5sgaoS-X8FesyvaodL5B0WD63Sqn6orSZ71qobHMmja1827BwqHH87mnm2IKnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/21384b098a.mp4?token=ssi-zfzRH9CPLX0lVSbgKH_mpV3RL8P-JV-J_KbCQlTJLBPTZY2jT9FyG350S7XE25eTqYW7Z2Zfk1Ju7UpZZq-sJsSrAhz0YfdF-wJQocLkQkcXwUyukwGHIrvTvHRAIyBNjJ8w9I3czXUALdJsOhUwKIuPi2COwerrx5SiBm3HHYT5k-YguKxt75hKPwfl6aCm3XEX0Ew9e_AFQS28-aR6ir76tB-xwD_yeMu7gCIYCmEPfB-IoHJfNSOoRs3ImVh41CCVqQ5r_2TmNmFHgOIo5sgaoS-X8FesyvaodL5B0WD63Sqn6orSZ71qobHMmja1827BwqHH87mnm2IKnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇦
🇾🇪
تأجيل مباراة النصر أمام نيفتشي في الرياض إثر القصف الصاروخي اليمني.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/naya_foriraq/93439" target="_blank">📅 21:59 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93437">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🇸🇦
🇾🇪
مشاهد من التدمير الذي لحق بالمباني المدنية في العاصمة رياض اثر سقوط صواريخ الدفاع الجوي التابع للسعودية.  https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/naya_foriraq/93437" target="_blank">📅 21:55 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93436">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AEhA1PFamsWhlFpvRfaPJT0XHTp3N64cn7-pBMEl57drOgU0ctispYiLfa_HpZO3Ac51AzjEPbBgDV5kK7I-yJZRtQhAe6WctAELr-heJce9fwG_sjZN7yBWRkDu25fUghO4NGo70-C-9cL8hlz9eGRr0pB_BC_tH6i9fUtkdffeiNQ4N6_G3lMGIm6QXe-xixS3K1Rs2nL01yro2n8fzyvZlO-qL6Ysu3hlBpwsafT0kkmE0Nb1dYiuGaTVnSRYsMFCr2n2aCKIAC2VoSaXSbknjso-IK0a1lhPDujWm-dZE92kPtLU0d9K44pItrgpjel8fPG_QsR81LeLLJD5vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▫️
انفجار سفينة في مضيق هرمز اثر تعرضها لصاروخ مجهول.  https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/naya_foriraq/93436" target="_blank">📅 21:55 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93435">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f2S140rf7Zq4FUpNII5RXb8kEUvSB7P52EkFhIEAPXGk77CmTIPYAKAEk4Z5xyDi7E_9VIIhrklcNExaBmW7Rin6oP0bNJnfn6ZCX1q5I3HV0m0cmmici_ybF32F_lHiTsCQQQmfmidnW9CBU_WiLojFZYDCEvCB4Tz6eGC60SxKkNwW7S8XXXZslN-2kPPLqKWnuzV8x7crjU9e8uJ36SSS5YO7clVCl6129F8SooO6uFWcKBu-qDq_VgiRqbdV6p1uKpnY_6mXTGQPWZJektrjkAyJZKyeGP9eZeWQ8TgT9qIMmkzcADzUwGSbHawPjzMJwoz6RgJ5lqQPp3qhlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▫️
انفجار سفينة في مضيق هرمز اثر تعرضها لصاروخ مجهول.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/naya_foriraq/93435" target="_blank">📅 21:51 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93434">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ASfxHSXgPBvqpNWJ2NwNAT3sMRKtkEpEUcxUouCF5fhEMN57AR56StinjKabHt6xapCrCCXmtl7ZOu_nzZFFvxiwVAzU_E_VNj7wcEJ2Px9-A2A42fzvxCTM4Fs9EGiTityQQoua50SI4wkKNZzqlulo0Di-qsyMIhIWYvpI4CARRZ7CKurtq2oepw0IWGp7Mw8DN9jNe1sFHeZBZ5iezNLB7_INXK62I_s_MfVjKtZCVFrHCDl0TdJGyTg5haivFTFTIE3rlF2ylUzBMELSKKpQUjjwdPoRXF60QaPtFXeRdu6kD67uDe4bEeOXfGUiURgm0UyNV7f71e5Vh-AB4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📈
قفزة في أسعار النفط لتقترب من 107 دولارات للبرميل الواحد.</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/naya_foriraq/93434" target="_blank">📅 21:49 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93433">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🇸🇦
تفعيل الدفاعات الجوية في العاصمة السعودية رياض.</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/naya_foriraq/93433" target="_blank">📅 21:43 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93432">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8575d2165e.mp4?token=AR9tCO9DiGPSDq8o6NixYIsxSGDUGynD2RmfBwgNDP5vm0zfOHI9bT11Bn_Mg8YSc6eUv0UBQzhzQnHB4fO9mGf2qX99SFDkHl8ZwYlUzf1VPuMAWLSGB3Ge4klLwIdyBA91RQIZixgskuR4MEe6e2WAYXtzEQZqImEgOtN9NgbVSNiEV4i4vmbpt8IX4ypysZhC1DGE5XwVXuX739HW93sKe_J6MxkEiW2ul-IjgPvOSSsksXQ_YkxYsQrw2nn3YnJYA_W31B6zu1HmYltYg4W_x2sEbN5jBUzeuQVKyXdoKePj5Ccp62P2JNTQCvo0f4WgVl5-d0cH7IxPo8nnUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8575d2165e.mp4?token=AR9tCO9DiGPSDq8o6NixYIsxSGDUGynD2RmfBwgNDP5vm0zfOHI9bT11Bn_Mg8YSc6eUv0UBQzhzQnHB4fO9mGf2qX99SFDkHl8ZwYlUzf1VPuMAWLSGB3Ge4klLwIdyBA91RQIZixgskuR4MEe6e2WAYXtzEQZqImEgOtN9NgbVSNiEV4i4vmbpt8IX4ypysZhC1DGE5XwVXuX739HW93sKe_J6MxkEiW2ul-IjgPvOSSsksXQ_YkxYsQrw2nn3YnJYA_W31B6zu1HmYltYg4W_x2sEbN5jBUzeuQVKyXdoKePj5Ccp62P2JNTQCvo0f4WgVl5-d0cH7IxPo8nnUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇦
🇾🇪
مشاهد من التدمير الذي لحق بالمباني المدنية في العاصمة رياض اثر سقوط صواريخ الدفاع الجوي التابع للسعودية.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/naya_foriraq/93432" target="_blank">📅 21:43 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93431">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🇸🇦
تفعيل الدفاعات الجوية في العاصمة السعودية رياض.</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/naya_foriraq/93431" target="_blank">📅 21:35 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93430">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v7lmUP0XyfEyoPlqp9mKlJ3Qx7rOdPlsR4vJHGriiogMcqaruRM8kqHXhj9ArgbrbKDcwqpeo3V_wlSV_wh0sjfVBT9UgfGsfHWggtG_8gQ1I_NrCh241Ed0kdCsH1cLpIHsliS77wkrnCRqs_DFZWaiMV5tXC8kf_JGYmv1pXDw-3Z1vuEoXRBFv4izHu-H_iK6rIxrH__2-kTCrD2F3AnahJyvYVVdzxG3bBoN65zz_ykSuBPsDdelbb6hFbClSxg3Avvbqj1dZ8DQj5Z7uL4tJiFiKFU8HFSLjmpBWIbLdtgqFA1D2qNMLSHCFU8mIvslqDh21wCSnEXD7qzP1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
الرصد اليومي لطلعات العدو الجوية التي يخرق بها السيادة العراقية.
يستمر العدو في انتهاكه الصارخ لسيادتنا الجوية، انطلاقا من قواعدهم في الأردن والاراضي المحتلة.
- طائرات (KC-135) عدد
2
.
- طائرة (F35) عدد
1
.
- طائرة (E-11) عدد 1.</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/naya_foriraq/93430" target="_blank">📅 21:33 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93429">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">انفجارات تهز الرياض</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/naya_foriraq/93429" target="_blank">📅 21:31 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93428">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">مشاهد تطهير وتأمين مديرية جبل حبشي ومثلث البيرين ومفرق يفرس بمحافظة تعز وطرد تحشيدات العدو السعودي منها - 12 أكتوبر 2026م</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/naya_foriraq/93428" target="_blank">📅 21:31 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93427">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">انفجارات تهز الرياض</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/naya_foriraq/93427" target="_blank">📅 21:30 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93425">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a503742f5c.mp4?token=nSA3xqHlZymA8JOBb20fU6Vha0xcCaP3C9N75XOyLp8Uq2cmr6H4eeHu5Eg4S3ag5nv1qSXdsTTHcLKsdGYa-eiYRaiJAJBYRWTj-7KZl0_szbk4_VlojzcGPzNMf4m_cMpXuAajGI54CqpaItTCeVUo_zSGAZF7DN01hKjf15K7zXUenQa4jrqFGDwAi5_Jq1QiVz56vcjYAUg9svg3zCFr24dqeRgmdsyZI3Fgay5jzPqZEtKF-u-uJCA1VVd-6gCWqoaATAyMty_vli9GCznus7aBaelS5p38ffQmperyvNMWuTz7wd8q5HdGRfuXLiDorOGbd5mFiwBMgIsJFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a503742f5c.mp4?token=nSA3xqHlZymA8JOBb20fU6Vha0xcCaP3C9N75XOyLp8Uq2cmr6H4eeHu5Eg4S3ag5nv1qSXdsTTHcLKsdGYa-eiYRaiJAJBYRWTj-7KZl0_szbk4_VlojzcGPzNMf4m_cMpXuAajGI54CqpaItTCeVUo_zSGAZF7DN01hKjf15K7zXUenQa4jrqFGDwAi5_Jq1QiVz56vcjYAUg9svg3zCFr24dqeRgmdsyZI3Fgay5jzPqZEtKF-u-uJCA1VVd-6gCWqoaATAyMty_vli9GCznus7aBaelS5p38ffQmperyvNMWuTz7wd8q5HdGRfuXLiDorOGbd5mFiwBMgIsJFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇦
مشاهد من الهجمة الصاروخية الأخيرة للقوات المسلحة اليمنية التي استهدفت مدينة أبها في السعودية.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/naya_foriraq/93425" target="_blank">📅 21:15 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93424">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🇸🇦
تجدد اضطرابات الرحلات الجوية فوق جدة والدمام ومكة المكرمة والمنطقة الشرقية في المملكة العربية السعودية.</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/naya_foriraq/93424" target="_blank">📅 21:05 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93423">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">‏وزراء أوبك
: أدى الانقطاع الحالي في تدفقات الطاقة إلى وصول تكاليف الشحن والتأمين إلى مستويات غير مسبوقة.</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/naya_foriraq/93423" target="_blank">📅 20:56 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93422">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac48e4e35b.mp4?token=LxELMdGIhvM9Wlxxf6rPqClbIjjcrbXR_cV8tJGawwxy5GoHWHZFoK-d16n4O7aC9V1ELlx-BUdvNRE5b5wx84HxA9HX5rWsa659T0q5NGRCcnj5mg9fZ70KpHNEN3bORPg5eDNQRhIoPq8YEtg4ajyqI_uEhuOgr3dIram0oaCuHNklfIZ9ej21W1fN25zVeZwEIvasGpDsbQdqyJ8NESYIUYbDz8d0SiEkj7QzFr9uW5G9RNvDPToKvl2kJO7PpeOc7AQot66F_qznO6tVVcnoAG572riHxLBh5vLEoUoqO6L-kT43EOrXRPjk5CFtBhQhs99iVu6h7_E4ylw0oA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac48e4e35b.mp4?token=LxELMdGIhvM9Wlxxf6rPqClbIjjcrbXR_cV8tJGawwxy5GoHWHZFoK-d16n4O7aC9V1ELlx-BUdvNRE5b5wx84HxA9HX5rWsa659T0q5NGRCcnj5mg9fZ70KpHNEN3bORPg5eDNQRhIoPq8YEtg4ajyqI_uEhuOgr3dIram0oaCuHNklfIZ9ej21W1fN25zVeZwEIvasGpDsbQdqyJ8NESYIUYbDz8d0SiEkj7QzFr9uW5G9RNvDPToKvl2kJO7PpeOc7AQot66F_qznO6tVVcnoAG572riHxLBh5vLEoUoqO6L-kT43EOrXRPjk5CFtBhQhs99iVu6h7_E4ylw0oA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
‏رئيس إقليم كردستان العراق: أبلغت حكومة إقليم كردستان أحزاب المعارضة للجمهورية الإسلامية الإيرانية أنها لن تسمح بأي هجمات مسلحة ضد إيران.</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/naya_foriraq/93422" target="_blank">📅 20:42 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93421">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🇮🇶
‏رئيس إقليم كردستان العراق:
أبلغت حكومة إقليم كردستان أحزاب المعارضة للجمهورية الإسلامية الإيرانية أنها لن تسمح بأي هجمات مسلحة ضد إيران.</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/naya_foriraq/93421" target="_blank">📅 20:35 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93420">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🇺🇸
🇸🇦
السفارة الأميركية في الرياض: توقيف أميركيين في السعودية بسبب "التقاط صور لأحداث وقعت مؤخراً" شملت تعرض مطار الرياض لهجمات.</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/naya_foriraq/93420" target="_blank">📅 20:34 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93419">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🇺🇸
🇸🇦
السفارة الأميركية في الرياض:
توقيف أميركيين في السعودية بسبب "التقاط صور لأحداث وقعت مؤخراً" شملت تعرض مطار الرياض لهجمات.</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/naya_foriraq/93419" target="_blank">📅 20:32 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93418">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🇾🇪
العميد يحيى السريع:
شن الطيران الحربي السعودي خلال الـ24 ساعة الماضية 119 غارةً جويةً وصاروخاً استهدف بها الأعيان المدنية في العاصمة صنعاء ومحافظات الجوف وتعز وصعدة ومأرب ولحج والبيضاء وإب من خلال طائرات "F-15" و "تايفون" أقلعت من قاعدتي خميس مشيط والطائف والعدوان الصاروخي من نجران وجيزان وخلفت شهداء وجرحى من المدنيين بينهم نساء وأطفال.
ليبلغ إجمالي غارات العدوان السعودي منذ بدء التصعيد على بلدِنا 2177 غارةً جويةً وصاروخاً.</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/naya_foriraq/93418" target="_blank">📅 20:28 · 20 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
