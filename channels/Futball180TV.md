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
<img src="https://cdn5.telesco.pe/file/DBUGyP9XCfgTskyw8EO2l4-RpnBK0_ZTVJWRtCI5E91WaIR6xpo2WHurdDurbgmH6xqcmllNw-UjnxmcpsO0d1oe-1Uv_yAmQrWuBOdtwPYAJWXva-WTUxitvYs0kQIZINNLH44h-RgFA8sccEI-2Ny-1zNJW6tXAbmlcBXP4gcDJqHGpolqv1_Yg051_vs4Jk95oaTlPCPveQkVazjw6hv1rsWx2bZXGe8TVociXohw8qF4np_vMxbtuyb8oyEO4EgAY87W5l98c6uyVxzLceXbO2eltfrEWo9rT9-s1wI87MTfZAZr42z_vwEj994isPXn70fnvwK6ZJIIXmt-Fg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 جام جهانی 2026 | فوتبال 180</h1>
<p>@Futball180TV • 👥 624K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-16 03:39:09</div>
<hr>

<div class="tg-post" id="msg-98732">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">گللللللللللللل بلژیک
🔥
🔥</div>
<div class="tg-footer">👁️ 1 · <a href="https://t.me/Futball180TV/98732" target="_blank">📅 03:39 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98731">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">بریم برا بازی آمریکا - بلژیک</div>
<div class="tg-footer">👁️ 610 · <a href="https://t.me/Futball180TV/98731" target="_blank">📅 03:36 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98730">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HDiMAboBWIrXZpTn76zTQltUvXmSDM5z4-TXat077flw_BZTQVyiYSYpEDKbFr2xZAz-_SCJTGzO6rwbJ5kAr12idKs43UkbCvA8eFCosmFTKdR2AzCASV3mrd2OqsUZm0Hu2zuZ-bXAvDXNrMszwGTg-oA4SLxf7sSbQarepnZo1HeAcUK7Vc1IUnXccfPTdI_kCT0kzML4zm-xjUloxZsiVg-bZYrBQOR0Enyjqmz6hfohZTI_vedkh4UHwF5nKNN9vE3yXWC_Ry9ygDuPMLqheULQEM_ogalXUlyN5xClYbWwhbxnSltrWvd45LdMylmmg0Rlj2nw6m7ZFMxqkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🤯
مقایسه عملکرد هالند و امباپه در تیم‌ملی!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1.21K · <a href="https://t.me/Futball180TV/98730" target="_blank">📅 03:32 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98729">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FuckBet @FuckBet @FuckBet @FuckBet @FuckBet @FuckBet</div>
<div class="tg-footer">👁️ 1.21K · <a href="https://t.me/Futball180TV/98729" target="_blank">📅 03:31 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98727">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mANrtYm_nNXXz-LPpqonBs5-GfpcGKX57nFsXnoHbwIiKF2snsLlP1ypYykKOiuKiFn381mEL0jJ7J22vBD01fLCyGypKqlSTD8sw50T5AZwzz4erXKGRIAJCtl2eFqmynqkV4d-IQM0Mc0j_IvXpGSUh4icyd5w0nRH2EHd8YgghaFkzkW3pcK1W2ttcshaB02Tw9j9QehEpK8Ncqpq5jl5GcrUQ5i2BJbRiEqfRnc5eN6Pvy-S3cyRy41TztCgrTohg8bn8Caz97ndcEteWtNNNSJATdRkHuehkzx_8JxYzi2lDX2aZ9KPslfDORb5rZm2JvfGDp0eTgbkmprIoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FuckBet
@FuckBet
@FuckBet
@FuckBet
@FuckBet
@FuckBet</div>
<div class="tg-footer">👁️ 1.21K · <a href="https://t.me/Futball180TV/98727" target="_blank">📅 03:31 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98726">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4ce0afd819.mp4?token=IRAKIRyzxtvoItmKN6bSnxyEfC3QJGDBV5ycmkTp5Y4LR-rDKxO3vsmvF9JXV0nKAN74mzLq6pZmu4BWx06iR71ewzTBqIZSN2ngJNMuNua48DuXDFpsokhi6oTijaqZedufFrS-sQCIn3Fivct5lpZ9mlgn9Xyyxy1K0zdH5dy8l1a5QfD7G1Lbg8e0mxrzpJUvwgHH9fq0M4GZA_5KtyskKyI2Cu_WhlIrZdgIWVFnkGN2amVnky-GnqOdfdJ8FSypaqqxet3Y3sfOk4Mmr11U8jw48fUxfG4BwDrY47QI55syCUfiCFBJgI5cCmFYHSQ2ZggbFjSPeNDKTeQkyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4ce0afd819.mp4?token=IRAKIRyzxtvoItmKN6bSnxyEfC3QJGDBV5ycmkTp5Y4LR-rDKxO3vsmvF9JXV0nKAN74mzLq6pZmu4BWx06iR71ewzTBqIZSN2ngJNMuNua48DuXDFpsokhi6oTijaqZedufFrS-sQCIn3Fivct5lpZ9mlgn9Xyyxy1K0zdH5dy8l1a5QfD7G1Lbg8e0mxrzpJUvwgHH9fq0M4GZA_5KtyskKyI2Cu_WhlIrZdgIWVFnkGN2amVnky-GnqOdfdJ8FSypaqqxet3Y3sfOk4Mmr11U8jw48fUxfG4BwDrY47QI55syCUfiCFBJgI5cCmFYHSQ2ZggbFjSPeNDKTeQkyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گریه های اسپید بعد حذف پرتغال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.43K · <a href="https://t.me/Futball180TV/98726" target="_blank">📅 02:33 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98724">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AuIOTmTgbIW65pfgADkF-jLohcpVo55bmc4bBtCIeQkj630krXd6H9C4RHtMcq4OSNW0YXLttuAuo_HEZs290KzVL73IfqiSV3ggzEO6OKK9haxlBydhVqYn9GlKH0Xpx36eCO0ZAzRiMkVyQY9IWsv10YVZB2wCgScH03gqk-Rfvb5IT5p3vDc098MULSa853PfYnp_AQUtUW_Mlshk7K69V430Ydl-nCT-6tARyumuaMGauK6KY1jTRcxNbtS9Fu7m7JSkqZlIopC0_8f2kyl97M_6ZsVZlYB8QCGOZBj84kBfW4OpqV3PdG1dxmCNocVXkn78JZbnPxd52qXyEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Kn5bXCM2HLxteAfILY9fIRqe7nl37FoZYlY_uNBhKS6T_wzPh-HPaNu2Zo_rJOHn8ka5H7yoPL6YE1w0xmFukIlalDlnTZdatmlfAk9EgviWeNoTjBfeh9Mn9K8I6G5dlaZevJ-MQ1e8Zd1rJvkSi84WB9nJeCsyfSxCIlB_mU4SP5qWbjrtTVnPZKK5DMlz0_FoCz9MRU__KAAN4zO7gHCjt0JJ7kZbe9D_R6jQE7HJ5GYjDN44bMgcAgiS36YUA6UjJkEJSvIeaGIHaioU5LB6pf5J_VL64D9ZFQv126tVEIEykUaNcQJqK5sA71cbuZwlAmuMUUPzfiDGBrn7bw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">-
First dance.
🫣
- Last dance.
🤕
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.73K · <a href="https://t.me/Futball180TV/98724" target="_blank">📅 02:16 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98723">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🚨
🚨
رونالدو: از فردا در آغوش جورجینا خواهم بود و با فرزندانمان تعطیلات را با لذت و آرامش پیگیری خواهیم کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.88K · <a href="https://t.me/Futball180TV/98723" target="_blank">📅 02:11 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98722">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🚨
🔥
👀
#فوووووری از جورجینا بعد از بازی:   برای امشب و تعطیلات تابستانی برنامه ویژه‌ای برای ریکاوری ذهنی و جسمی همسرم کریستیانو دارم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/Futball180TV/98722" target="_blank">📅 02:08 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98721">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🚨
🚨
🚨
🚨
اسطوره، کریستیانو رونالدو:  ‏"من ناراحت هستم، اما تمام تلاشم را کردم. من با آرامش خداحافظی می‌کنم؛ این آخرین جام جهانی من بود و حالا باید فکر کنم، با خانواده‌ام باشم و به زندگی‌ام ادامه دهم."  "زندگی ادامه دارد، و فردا یک روز جدید است. بزرگترین پیروزی…</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/Futball180TV/98721" target="_blank">📅 02:06 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98718">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IoG1XxNRATTLPPEqz3ZcULpK1eJR24v9t_Atb-PS-e5_kXR2xRY1wkYN-p6FouaEtl473dFQ-KT8IFc5iMf-YD7Rdibxjl0ZdMNYCISRIpGPk_LMdinnhDhf5zJVJdIF0bF9N59MyjUE88sIpmLjnvRQiXNsEOcpSI4JqA790KMHI7cQ1WMi19_j1JwyzO2R8wj-CLpwVOlFhgeFm8Q9XhByyjQ31T6gHbQ6-jOE0hqUsObGgVEszJykFqbZBe8iDDk0zUvFTAIIT2gV64mgOVTMpBaM-VFV9sTZnJI9XCJVvaa0YVP3w2zLb2tP4P0zvN_De_uS3kcubPWo6ILNFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
🇧🇪
ترکیب تیم‌های بلژیک و آمریکا با حضور ثابت بالوگون بازیکن جنجالی آمریکایی‌ها
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/Futball180TV/98718" target="_blank">📅 02:05 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98717">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🚨
🚨
🚨
🚨
اسطوره، کریستیانو رونالدو:  ‏"من ناراحت هستم، اما تمام تلاشم را کردم. من با آرامش خداحافظی می‌کنم؛ این آخرین جام جهانی من بود و حالا باید فکر کنم، با خانواده‌ام باشم و به زندگی‌ام ادامه دهم."  "زندگی ادامه دارد، و فردا یک روز جدید است. بزرگترین پیروزی…</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/Futball180TV/98717" target="_blank">📅 02:03 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98716">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🚨
🚨
🚨
🚨
اسطوره، کریستیانو رونالدو:  ‏"من ناراحت هستم، اما تمام تلاشم را کردم. من با آرامش خداحافظی می‌کنم؛ این آخرین جام جهانی من بود و حالا باید فکر کنم، با خانواده‌ام باشم و به زندگی‌ام ادامه دهم."  "زندگی ادامه دارد، و فردا یک روز جدید است. بزرگترین پیروزی…</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/Futball180TV/98716" target="_blank">📅 02:03 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98715">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dSpktMT07h4euxg5eWez5xoUQNp4hEUemaXjcaIw8nHAd7j2ZV8c8zZ3L2cuR7-1M7JSb5La1PtOTkOKk44_hXDazYygbJbSI0ZoOCKrpPuBEiYt219HwfeSZs3mh7vNHWuCAfVGk8CiWQrEIpqACZy42mdDjtTVW-rYGUgXMa4goiKyH-W0SZYYGDPQsmMMHYm14IQH51R8J7fXvE94mL7A6xBkTjfm2tLMBfnoOBfde6CNj3LOj3TQSvK7tUCNUTiA8bsRBU_8RP7gDd40PW-2JRJHuXpk7okG-jhAJFNiu_xqBMY2sjkk3qzsm06b4v2soi0st-JgKC9QdU0vPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
اسطوره، کریستیانو رونالدو:
‏"من ناراحت هستم، اما تمام تلاشم را کردم. من با آرامش خداحافظی می‌کنم؛ این آخرین جام جهانی من بود و حالا باید فکر کنم، با خانواده‌ام باشم و به زندگی‌ام ادامه دهم."
"زندگی ادامه دارد، و فردا یک روز جدید است. بزرگترین پیروزی من با تیم ملی در سال 2016، با قهرمانی در یورو بود. برای من، این مساوی جام جهانی بود."
🥶
🥶
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/Futball180TV/98715" target="_blank">📅 01:59 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98714">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H1tsTqAW0Hncl2p9ohYF-OGPRxOPqZEK2VQ2kWC6e6DhliZZ3dFbJemXz0cWyIxNA34t5JxwXrwPkmiQpxdz31fPczxYaH2eoWxzCkY90Ef9o2rjRtpRPr7AdH40On4TerR9fytQWvsCZpU0Ztt9Q37YHILbQmEJhv0C9fQM3nYmulzpcsK3Zzho61igLkPnmj3Nt6jnS7MGved3cWa4K9SqrSPRStE_myO3p0OdArMOm2BupoAtRP76O1n9qlSaa5-Lh23ZhtsN2CeZCPdFKwF8QCr5uXBDVKuXVG3iF4zMyI0XpmOlqAAlcba57NxE8QpWONFMD99-RMgvM2x6bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
خورخه ژسوس گزینه اصلی جانشینی روبرتو مارتینز در تیم ملی پرتغال است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/Futball180TV/98714" target="_blank">📅 01:58 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98713">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jhz1-QMAS4YilNnn51xvHdETJT4_GKxpFJc7KsCSvffnFVsNkL95m8Oc3_pTI3iTXYbUkaraQbiKT4x_DO5aKc_ab8lRdra6jWQRqbssxm1b2UFnbA6pW_5erAvVvzrbR28h9jo_RLS_FYyGxFb-p6seTKhH1W4AP7nyYreXTSEAFSRaWerM7CsYjKLU60gg2cUAIzKeaNruiuYA3la8SR9pPw5ksW5h3quWp0pbxQwU5dEcMlgwnRYRRhKXeUWKYGN7jCzHSKq-StWEiGpaO1K7dlRo5cUn18AUsONX9Vq37VMckZZxd8DHwN8DUPKFjDrLK8sP8gsqB0f2Se-rOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😀
کسشر و خیانت‌کار اگه قاب بود:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/98713" target="_blank">📅 01:43 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98712">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tgnLgC8Iwc5h8RMcHSHIndYkBxNsx_MvIjV-_1mJfFhlHXM7_HIoOYHs05Jt8k-Pbgmx8fWpqpyXaIVyX8jE7nuxhlEXuY6zCBGGM4iTmZ80ucsBrDCIllj9906SW5ndqgTxxY9UtowrUPNBVzvn_0WsjCWdfRKFbFudC76kvaVtKH9QHP7QCQMBow0jumPztgoR32asNTIhyPavJZX9-ja2lEhc7U0mHlVZTacnCprSdw653JJZHCM0CO_kfBRXR9ENcptwetBVlinZkY5Z8UqtfY3kXOZbVLc3aCXpUzzzoC_2fjND7DcpmZmrW3hyesThmrT9Xa-jK9nBO9xIPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
👀
🙂
ژست لامین‌یامال در رختکن اسپانیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/Futball180TV/98712" target="_blank">📅 01:41 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98711">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dmIo-10Dw-vksksFuyaoowN_f1SXQcnJsgFK49OLrwnfVUUdAZhTexkCTjnjytE2J7_3tb0l7_RlB7gbyGVnPxWimdVz6SDqOsrnu4Fhwr5EoeB1KhB6cp_6lEj-a5fa4BgxkChTps0WMybb2flE8W4Zg1c6j2QaO13xHxVQcG0PfELFEW8TEmJh-BQVyoMJnvZJkeikFBZrVaUCl-C9-vrC1oLy2rX82KTfLKNiKzIq5tYfML5mmdYtd0TewC2EBT5QFjv1GtT9Qt4HMsfXrvDGwZICxCckoMa-wrI5wv5-Kl_P-CaCyD_yK5dSZ56smFzQvQ-ax0gcvHHgGVXvlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
🏆
نمودار مراحل حذفی جام‌جهانی؛ حریف اسپانیا تا ساعاتی دیگر مشخص خواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/98711" target="_blank">📅 01:37 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98710">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ejgppp6awqSCnew2O3XaZf-FZ3-1F1XkHYpMpOzEo7LV2nMilYNltTDw-P-TS22WHUO8MuGBvzHdRecTDOgNi4T0rz4ejAsQdNMnM_ZnrRhRzjwDuOQevSWBvpsUWy0WZtzxGbuzvrG68p1XX_zbXlMnh-PXeTO44cpiVt1bhLE72YDc80zDo3XDgIak4OcsWUyf706dGMQN4SR6BKEJHKAhP6vZOrJajfBk3M5GA5ho5KLNaQOLAslRR6eHg56PGDBlKFe-aVIdcuUVt1WiHdHTBJ05OwYsUpciaCBWpFs31Pkbnpid4EyDVcq50ICgDm3ZkxpQg8Z_tR-pW-znAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
پرتغال قبل کریستیانو
🇵🇹
:
❌
در 3 دوره از 17 جام جهانی شرکت کرده است.
❌
در 3 دوره از 11 مسابقات یورو شرکت کرده است.
❌
0 قهرمانی.
📊
• پرتغال با کریستیانو
🇵🇹
:
✅
در 6 دوره از 6 جام جهانی شرکت کرده است.
✅
در 6 دوره از 6 مسابقات یورو شرکت کرده است.
✅
قهرمان یورو
🏆
.
✅
قهرمان لیگ ملت‌های اروپا
🏆
✅
قهرمان لیگ ملت‌های اروپا
🏆
— پرتغال بدون کریستیانو، هیچ چیز نیست
🐐
.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/98710" target="_blank">📅 01:33 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98709">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🚨
❌
🏆
واقعیتی که دنیای فوتبال دیدند اما بازیکنان بی‌غیرت پرتغال تکذیب کردند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/98709" target="_blank">📅 01:29 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98708">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uR-mPah6zuwrDUQl86QpjBBmxHXx7vxmHXSSZYe2UeUXb44KqT1k7nDCtCcc_x6CLQmn_mCHHjHPd5RZf9GEqkWUlF2YoMla8BJuyDzdNs8HqH49Q9VT5vvcNviAp07EUMlDt84N7ektbd57IYUPOhRc8ORkYxvf7srCUeWB9ia7gjIku1zM1kCQ3BOtvqzh82pESq-Gb23B8wWn_kpHTwX12z-79Y9mnPQWbueKfDNEwaL81K4VqMRu_jCutX_2RhjFGvcpiidF7k_4YADGVM2HFQOFu8bVV1NIlY-WHKcQS1g0lssEWDKqyAohAAVawHdYfnPlD7ql4D3LAK9fPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
🏆
واقعیتی که دنیای فوتبال دیدند اما بازیکنان بی‌غیرت پرتغال تکذیب کردند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/98708" target="_blank">📅 01:25 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98707">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cxT85dFW5gi6UQwAeKIeiBgsAUeBPvZ48IKe7kKyL6UcseQ4IzVmWjZnpUXEIHoKH5NV5uCEoNPaWT02qEdcCONZLZSsEWFlBDAtNQK7YJnU5pU0zqkNaxpYH-Bol6OF-alA2PiO7q5hBhhfaopIIsOA9WR87onKmouRh_mRH00xxqCsfHE1sUylOFSYEYwx5JmgFpvyDpKd5TjpCunz6r3ehPYfxtJzE8roTtfrsWyMqgEx5fb0ps6wKRvvO6uSnpYOv7saAFw_i189I-XCT7_e-gofrTwru0j4YL1AuOQa4v29TQ_3ehVXqte-F1Pa1a-IoI2xw1aeZnc0UTc43g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
بیانیه فرانس‌فوتبال برای رونالدو: - از شما برای خاطرات بی‌نهایتی که به ما دادید، سپاسگزاریم. میراث شما و پنج جایزه توپ طلایی‌تان، ابدی هستند.
👍
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/98707" target="_blank">📅 01:22 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98706">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/imx07KqH1QX-qUnODQbFE6E3EVw0MJXVswER2Ww6jyhFTpR0f3wDpXiF7i5G_EPHOTKvx1FsbUKLRAxuyzP4izf8v5tGg-Cym8wZjNzJHU8E7Xlxv2XbMlmVWUzQ-DJteEtr0Y1wcvuM9Ro37GoYliZMefCE_ZmOl6JV0KxlvAUsRpESE9WL4r6lcerg_fU09XwJIP7QGYPq2YKpM3AHMDnbhkhq1ZFypkEO4AjI5fWcvNq4PZux1lEd5Xo0_JMHZbzLBi21d_0ig2BtJBspawq7QicHcPkj1JV_liMkCiKZPoWRSWy1YRv0rstLU1hcRADh6235WzWkcn5cCyUVNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
روبرتو مارتینز از تیم ملی پرتغال جدا شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/98706" target="_blank">📅 01:21 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98705">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/153aac5990.mp4?token=lEeUeKPT3EluBk0dl-Y-ac8aZvxGRqKQHxRzPhggcmR7A3UlMUsi5Zz3HMbtHo8YAP1sLy0UXLm80RKFCwAzOBWi34RMiD1LGeCV3GrHmOJWhZTi87LPonrwPyKq_-iiLcP84xcMfELDSW32JELC1jxSnLoV4R4g8ikL4Vgz5UCMzBnApmsdqEmlQ-KxOzCufUCdEen7gmK3ygswkuzO26pCzJskK-SCun3Aj_hB_aRWrg0dFmFlRZcKIvY3MvCTYLCN29EseIGb4sOf9nIuSZWxSVDuJHqwM3NVjw67C9b4iaey7c4R5iQG6h7JDh6rb1QquzKKl5Q4rCeBrNt5Ug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/153aac5990.mp4?token=lEeUeKPT3EluBk0dl-Y-ac8aZvxGRqKQHxRzPhggcmR7A3UlMUsi5Zz3HMbtHo8YAP1sLy0UXLm80RKFCwAzOBWi34RMiD1LGeCV3GrHmOJWhZTi87LPonrwPyKq_-iiLcP84xcMfELDSW32JELC1jxSnLoV4R4g8ikL4Vgz5UCMzBnApmsdqEmlQ-KxOzCufUCdEen7gmK3ygswkuzO26pCzJskK-SCun3Aj_hB_aRWrg0dFmFlRZcKIvY3MvCTYLCN29EseIGb4sOf9nIuSZWxSVDuJHqwM3NVjw67C9b4iaey7c4R5iQG6h7JDh6rb1QquzKKl5Q4rCeBrNt5Ug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💔
💔
💔
▶️
عادل فردوسی‌پور کاری کرد که امشب هر فوتبال دوستی بابت رونالدو اشک بریزه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/98705" target="_blank">📅 01:18 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98704">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2cc0463de5.mp4?token=mCM2KwaPxYo88mqAgWdYVf59XK9mZraVbvIoT1ozCfTyTZO2oEIHYjkSnj2LFzr8JYTxu1LumkCOz_9yLhWhvj_aHtslO8_HU5w8s2MGNpjRs1h8lIe_0kidT68Ax2b1dait6D-4BOguey8Dq1jDinGZCGaCwlbZDqbMqY7CiVawi8pibgnhl57Tr016IC9LT7-jP6dBlu1U9sA0n_tfc5L_LYQwS4BCG7eOqobjhtFSpmLrcx1g966xGl1O91X5Yb6Ovu7bHUB86LXBCS1lzsdsWy0tzKm_4TINgv7YkvX0Uw7qy4Uz79X5Cup57zxag-RyF9noB7eP8NV4mK2A4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2cc0463de5.mp4?token=mCM2KwaPxYo88mqAgWdYVf59XK9mZraVbvIoT1ozCfTyTZO2oEIHYjkSnj2LFzr8JYTxu1LumkCOz_9yLhWhvj_aHtslO8_HU5w8s2MGNpjRs1h8lIe_0kidT68Ax2b1dait6D-4BOguey8Dq1jDinGZCGaCwlbZDqbMqY7CiVawi8pibgnhl57Tr016IC9LT7-jP6dBlu1U9sA0n_tfc5L_LYQwS4BCG7eOqobjhtFSpmLrcx1g966xGl1O91X5Yb6Ovu7bHUB86LXBCS1lzsdsWy0tzKm_4TINgv7YkvX0Uw7qy4Uz79X5Cup57zxag-RyF9noB7eP8NV4mK2A4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
حرف‌های رونالدو قبل بازی: شاید این آخرین جام جهانی‌ام باشد، اما امیدوارم این‌طور نشود
💔
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/98704" target="_blank">📅 01:16 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98703">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TP_horxXCm0KiecFA2XhEAgxJMdf0SKITJazx8452uLgOUZ7X-ZUVK_dntUewcxnc9MDobddpUmjn8C7ozKyYPw6ricm0gqwoQIU63Walg5IItJ5qkgmtJfFfmHQodBjmbaQtCjzOb6fx8Q_6_0eUem-r6TJhF31HWCsgf0z1Fe1NI-mVH19iTqatf-CIorOJjM6Fek8H-AqwXmiiXLIhQ-LLtbiTPbgGbNx6eSEskk8CUs7vkYNrJYZp8OeREI_DFHPhIf2Mag1wDLZ6LRXLRYUiBq3M6SCwrIIzCn1cLSlhAM6Au9dV1Bijv1tPbU_xnWvJE1qJxjS0l8rUau-Ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
گل میکل مرینو به پرتغال ، اولین گل اسپانیا در مرحله یک هشتم نهایی جام جهانی پس از گل داوید ویا به پرتغال در سال 2010 است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/98703" target="_blank">📅 01:12 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98702">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BXke7RINXvofivbJm2MfHMvKyJThLelxHvmgr6Gyf2SsBWmR9CK9Hke8P_sXaiUPyYFQAVIn0ptoNFLwMEwY4IWhOmcHQB-76ZNVMyvtGaUwsXMth_BhTXIUidcQGGfAIg2JfwrfYqDMWBBLEiVuleb0EiFBgjou9p0wOOvG3_SzdxEuK9SLXaM2lyX1_3nTVLT8rFfUl5xzCh11EUJeHuoaIal6DcoR7uasTK0yKxk9rxsfQCuOISkEFcKjvGCRLONWnHLxUQOY572DAK7QPw1yvKDq2-Cgw5g7RJeJgdeRCMo4DiFI9GRe3swBwYKctXkEN8_itzyeJdhuC_ajeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
♥️
کاتیا آویرو (خواهر کریستیانو):
سر بلند بدار، برادرم.
تاج تو هرگز نخواهد افتاد.
تو یک غول هستی، تو سرنوشت‌مند و انتخاب شده‌ای.
تو فوق‌العاده هستی.
از تو برای همه چیز سپاسگزارم.
از تو برای خیلی چیزها سپاسگزارم.
از تو برای رویاها سپاسگزارم.
از تو برای شادی‌ها سپاسگزارم.
از تو میلیون‌ها بار سپاسگزارم.
تا ابد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/98702" target="_blank">📅 01:11 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98701">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/QVrb4utUuoJi-yg5PksgmumG9izerz9Hr2H45YKgpOHuYfl8mXoW4icRDlJEGiCYVLGt3ZTgxvpoSzVtClPjgGYF1pAyJlz0To3sS9o1JgRNzOJgMo3QPfNcx9SyZRsrl2wtLd6vGnNJIDM5jYwtEqeWqfcXRfSMF7XvU1chUUhOBaWta_uCtUMWyKG-w1dd6PyncE-smMHasibY1wiEerqr0pUA5Lx92U7MEiE-I6gpGW_p3HLHiQoBMa-Pwy5NriqO7XFzDkDdm_hvbq5wSj6N8JPnoUKUNKllTaRXUqq6zQ6AfWpVvBnWOaPsxf-zP4TWav3GGLevAKZANdCdrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پنج بازی پنج کلین‌شیت
✅
خانم ها و آقایان معرفی میکنم بهترین مدافع فعلی جهان پا پا پائو کوبارسی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/98701" target="_blank">📅 01:08 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98700">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A-LbhvZDciNgsAToff6jQojYabO_S7rwgzMj8E8RKymO-wh49-r_wEMoHdINcbHY2d-GhKbK4kyO5rXKuYunL18_XuQYiTsemU-VJ1xosjmFGHQHzH-QPmnU7tULZVZIKwgBFafN1ZtilgbPxdb7Lbaq-sDeHxjbQ9HjdWxs3EDCmiXKpdjRTScYDB4llXtVTv_cQ56yrWaoxJhONBmsX4-HQrLepigaomGL5PMssX_Cc6FD5lZ0hG8E2thFZo08I75BKE9IiIwTPCeC3o4vW7PUfve3ZYhIQYkScgDw8Sx6g0G3OokD7mKec9rbWXqixJSCzLQPfKdkhUa-A5MDGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✔️
🎙️
رودری [
🇪🇸
] :
"از برناردو سیلوا بابت تمسخر کردنش به خاطر از دست دادن فرصت در آخر بازی، عذرخواهی می‌کنم. اشتباه من بود."
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/98700" target="_blank">📅 01:08 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98699">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a3q78jOtK05kvV6hw-QHyRFkgPMmgFbNlLpAIfRSiKDtQjOuKPIpHxCuebaebTbn9v8M7U_5EUlJwFvcwOx9vbmmq3TkX-L2yQpcwrUOHbykw7s0Z_1K_oViaIIptieK9WP7BvBnC0sGKSzUUwpA5MMXYxbOrbz1eIUTJV64gcEfri44PlnN1XObQS8GymTnbgiURjeE8Hv-nyyti9rdYR9UB2uyzcA6agMFxBzirn3xc8xFtpJAaDWnRVidTzzbcj4cVfdxfoDMcq8Ufr-tzCdBTPBNUFTW-IMGOiR2VoDV6_H8-sVsmdCNNj1zohBbsnIvnvHbbK5PrAUZVktEVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
⁉️
و تنها یک‌اسطوره همچنان باقی‌مانده؛ آیا تاریخ را رقم خواهد زد؟ برای گرفتن پاسخ کمتر از ۲۴ ساعت صبوری میکنیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/98699" target="_blank">📅 01:06 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98698">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">این جام هم مثل جام جهانی ۲۰۲۲ به کام بارسایی هاست
😉
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/98698" target="_blank">📅 01:05 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98697">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🚨
🚨
🚨
🚨
ادامه گریه‌های رونالدو در مسیر رختکن پرتغال؛ واقعا غم انگیزه
😞
😞
😞
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/98697" target="_blank">📅 01:03 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98696">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DehmeVW2dCprC_UoNKmwfI5MzgJOoQA9bJsJaZ0f9v_ZcIcTjUvKxK9qHRspnTwkieXCIxJYVMhCGoyWdVi62zwZ5WlejNCWvZkDPM3Wv1jzunowU5DmnMw8Uuiqko3f6EkyhVs-HL5-NXwf42oA4valgOtPcHveuSX-EZhuqXNdsyiOn_qC7oPpKLGVrKpyC3IQBMwTglIRoSi69j5T_4MvQjUHCqxSMSdEMwohWmUFXRY_2mkKNzzvsdEkp3G0P4IouVySsbncVyTx91PMcZ-RB7MeOM6TUOyKqD3yPU-mh_KflKPM_JINW_bh2pCsYYOwU1wCqy195-2BqfrMYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🇵🇹
سجده شکر مدافع پرتغالی‌ها پس از حذف شدن از مسابقات جام‌جهانی
😐
😐
😐
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/Futball180TV/98696" target="_blank">📅 01:00 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98695">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EuJOPfT8wL4KKcPws2gWSt8C56xRmFrBLyDLAJ9peA0eQr3zDgBijCAb6_OGC9V40xhS7TMAaFbw2IPg8gM0jNK-yfZtaI855kxO-D23F6wS6uT7YFhIkS4WI09hnhm0tBGiOkhtcjEGSidTQA6Kji7eb0-yRge6D7HyNc3GymHEkm5QEoXahVmgrIUyWUjZsrHlJZdkowGFJRrC6KhvqK_alPpxqwbLdd6mb-N58hOvTWBFMbjzaQbfZZT9BiHdn1_Yh9rmc_wDRW6n0lVRrESxTAI3MvJgGmHuHVsebubSTYdp4JGQrbrOy-L9tyr9e7hpHZgGqtxizMTeqOHoTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🤯
تمسخر پرتغالی‌ها توسط مرینو
🇪🇸
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/Futball180TV/98695" target="_blank">📅 00:59 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98694">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QChcG5baO44W1O1SE3k7tvePlEjsyApsVcfYfDEoiq4xX7SSF87abnUAVRnQndXQ4lyW1UxBuL9fiK49yR05pwPpDPd0qK-TsfMtj_BNnV6mNdYMqS8we_pawCUnS9IRXi2FhDxWo04IAv5EsYHaYfwqKmEM-ohXGe-2tQQN7qfYwPOp_PlOOijrTdM0s6SJK8anKkku_i2WlEmGGUxvNsq_x4RptMDgLl17CNo79e35kEm5gBa5SsGEcgBu6KEy6fnytSgJyn6UVibmYF0ZFyFMv79_1vWFffsQJCkKEBwbCV97GnjrHuLAbgDQo4N3IyTNTrHKNuNigSX11MYa1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔥
🇪🇸
تیم ملی اسپانیا، اولین تیمی در تاریخ جام جهانی است که ۶ بازی متوالی را بدون گل خورده به پایان رسانده است:
🇲🇦
مقابل مراکش.
🇨🇻
مقابل کیپ ورد.
🇸🇦
مقابل عربستان سعودی.
🇵🇾
مقابل اروگوئه.
🇦🇹
مقابل اتریش.
🇵🇹
مقابل پرتغال.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/Futball180TV/98694" target="_blank">📅 00:58 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98693">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ba77c1d49.mp4?token=W8G5bofXE6Vv1fS4UDDbOnck3qiRbw5HoCfMK3rgoay1K8vmH9mJtit3qz_yGDQL2tk4CY3jt4QAk4zbq9qgpCyEkE1Wvw0me9nkAdVEw382wLEHDWqDsywrn56PL0DnqXwGDp2QLHMUrKfDHfznyAaWv_RuypGuv2eTPT3-Rr_gauu63sGzl_NAQKcEtOOUCvPmFp8LxffpfpF0qMZSVmz8JDQinEFPYc4MFlDVTqddTWIYB2yhq-1r-Sm5Wpu-vEzBa0RFBRoXIxAROAmzCuyNwD7SBEDlayiEVJ_AZ6zslvrmx3YFuk4yOOwbRqXqmylMcr-JeEoSjgMVK0OUgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ba77c1d49.mp4?token=W8G5bofXE6Vv1fS4UDDbOnck3qiRbw5HoCfMK3rgoay1K8vmH9mJtit3qz_yGDQL2tk4CY3jt4QAk4zbq9qgpCyEkE1Wvw0me9nkAdVEw382wLEHDWqDsywrn56PL0DnqXwGDp2QLHMUrKfDHfznyAaWv_RuypGuv2eTPT3-Rr_gauu63sGzl_NAQKcEtOOUCvPmFp8LxffpfpF0qMZSVmz8JDQinEFPYc4MFlDVTqddTWIYB2yhq-1r-Sm5Wpu-vEzBa0RFBRoXIxAROAmzCuyNwD7SBEDlayiEVJ_AZ6zslvrmx3YFuk4yOOwbRqXqmylMcr-JeEoSjgMVK0OUgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🚨
ادامه گریه‌های رونالدو در مسیر رختکن پرتغال
؛ واقعا غم انگیزه
😞
😞
😞
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/Futball180TV/98693" target="_blank">📅 00:55 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98692">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kMJyUw8WvaUuQiNvIW3em80duOPOU028847ydNf3idJe0Ryn_5NXriyn6S5izmvTx72Xt-9OlVRIDz-wtpnKVs6VHyFDUAclQfe0gbveaKZSiTHH6XFENXhkP9f3_ThL0_jNuHfgKdDcdZ2YLDskXt9hRs_E3gu-25AUGobRTjA3BRy7A8vG_F3eTWg58q0bXdxmWE5FdCygZG-sjjM1Enz9ApNobtQWDBJFfnFJPKS1bkuRfhKo8qq_Uci-elQLcSMLuhBoozJM1qVw4poLNSZIamP8Ujoepi12gL400bFvBjCByKzsGJWE1jCFTnE7EJFv2k0JhQ21Ft7GcCfHwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسپید هم یه گوشه کز کرده و فقط گریه میکنه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/Futball180TV/98692" target="_blank">📅 00:55 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98691">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/axhYK7mqg7qoGocoRj3w7FyEuEJX0X_ZKVkFXiT0LbGUlr2eCsLdo7sBPcAwNTvUuQ-PAjY5Kdq1zEQl8tzaNiog3czXhABQpgZ330yni6nHKbzu7bRlpCadRTkQFEsUw3_pmnbtb0f8oFCn4UbBRIIaIa7HJCwDhLzVjGvZu7zPvjuhqT8Iz9sgJv11SxN0NDIGs8f2YNQYw7shG2acSOYmwHhBjVfZFp5nbF53SFUKZI97lTcRys77A7j99GTN3zgh5dQg1_jozFrqGvl5JoZgeePGgWELw9tOY7qmK7ZjndPhiC1MIFz7fCR91EzzdAEtLyE5NVXQsSq7k-zJaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
‼️
📊
🇵🇹
مسیر اسطوره، کریستیانو رونالدو در تاریخ جام‌های جهانی:
‏•
2006: حذف از نیمه‌نهایی.
❌
‏• 2010: حذف از مرحله یک‌هشتم نهایی.
❌
‏• 2014: حذف از مرحله گروهی.
❌
‏• 2018: حذف از مرحله یک‌هشتم نهایی.
❌
‏• 2022: حذف از مرحله یک‌چهارم نهایی.
❌
‏• 2026: حذف از مرحله یک‌هشتم نهایی.
❌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/Futball180TV/98691" target="_blank">📅 00:53 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98690">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🚨
🚨
‼️
⚠️
🇵🇹
روبرتو مارتینز سرمربی کسخل پرتغال: این بهترین بازی تیمم در جام‌جهانی بود و اگر بدشانس نبودیم به راحتی برنده می‌شدیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/Futball180TV/98690" target="_blank">📅 00:52 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98689">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">💔
😞
سپاس‌بابت خلق تمام لحظات بی‌نظیر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/Futball180TV/98689" target="_blank">📅 00:51 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98688">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6a9ae9f6e2.mp4?token=QP-6G0zbVV0-ut3pjm0xWjJ9Yxg5tErU_nnakqAUbfCE82IgAEH1qucSKCJhAIspt4tRx7nVlt8_7DNPfmI4vE_pKmdXDge2dZoyr6wbJHIo1BbYeGHFEsLC2oLpTvPJeVfJ4CRFpuwxFDGihRKp4hzzXTDqLSbBR_seZ8jD7eS6xwIazUKh09X7qqszh1-sHKNHPf5iTPjJanSwhYfR1yP5zYIsaiwLV87Q-ANi2Tx4cnNYEojtTxH2lY4oi3Td1nDfGO0-hMF7s_syVgjVtigUnbNW9UpSARhFwXG4lcAOCR7tu-PLONADi7mzYJdLPqLHU8YxtCoWNmca2wivdTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a9ae9f6e2.mp4?token=QP-6G0zbVV0-ut3pjm0xWjJ9Yxg5tErU_nnakqAUbfCE82IgAEH1qucSKCJhAIspt4tRx7nVlt8_7DNPfmI4vE_pKmdXDge2dZoyr6wbJHIo1BbYeGHFEsLC2oLpTvPJeVfJ4CRFpuwxFDGihRKp4hzzXTDqLSbBR_seZ8jD7eS6xwIazUKh09X7qqszh1-sHKNHPf5iTPjJanSwhYfR1yP5zYIsaiwLV87Q-ANi2Tx4cnNYEojtTxH2lY4oi3Td1nDfGO0-hMF7s_syVgjVtigUnbNW9UpSARhFwXG4lcAOCR7tu-PLONADi7mzYJdLPqLHU8YxtCoWNmca2wivdTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💔
😞
سپاس‌بابت خلق تمام لحظات بی‌نظیر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/Futball180TV/98688" target="_blank">📅 00:48 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98687">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GUGVXU4W-xXbfpKKWGVwgCKHZVy3yB26HBzjwNaS5IVAJh0jxgigTYx5ZhQYwXRjJ6AtWBXQsh7_n8Mkfrcnm6Vrg8S8lkuoDgPwagV4dFVdV_B3zPQkw-k18NrclWPj-I-A9zmIaV78t46TcyRDSp3wx1V8eHaoJh0-qifbS8gOq2VFpQyOpZhQPkmSXXRwwx9RIeXg307e2HxpqCQQZgH1sQsHj1A6t73cqstSTTDROM-_OaMTLs5SsXAFteWP66UE51OuHrNHlqZ-rXZDW7YkI8VGKcjZuLvXS-3y4eWTKEXYnQNptsL3W6hZMRkPgb3F3xI8atXwhjohBL4_Vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔥
🏆
خلاصه جام‌جهانی ۲۰۲۶ در یک‌نگاه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/Futball180TV/98687" target="_blank">📅 00:46 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98686">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Awf4_NdZr1sZ1ZXI4ia4GrCqhpt8ausZvYcOieQe6OdMcm5gh0bERZDf3w2jGSee4ABqLjiu9aAs4a6JLL6faR0qBEn6D969wrIPH4SG9q4JE8PA0dieBAP5wdZp0AtFKUZPsaqVWREjNu7PciXDavU3h_8Fxp6JXil8CThH1hvYFU_Qr3W-kMJen0RGZR1KBQCUvmdk2M8UiPdPHgjbJyt3WK4ApT0zXw-2IwEwXoXisZmzUOn1_kwAYeMZ39vcvk3myAZcmW7JRyQm2scU5IVkjCU49cPWbicID_bF4ud2jcq-B2w4vkXqY25hbqSLyZB6RfLPI9cQV3QZxWRkww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👑
👑
👑
🔥
🔥
🔥
۱۸ سالگی و اولین حضور در ¼نهایی جام‌جهانی در اولین تجربه جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/Futball180TV/98686" target="_blank">📅 00:45 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98685">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">👍
🇵🇹
تواضع اسطوره و عذرخواهی از پرتغالی‌ها
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/Futball180TV/98685" target="_blank">📅 00:44 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98684">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XMGcSwmYX1GMsZpK0uzFpTdMQ4MZKNRF7SpitjrQFXW2fjriYOvaEuIY3fSiivRepYZtVG8DUa-7BYW756PIlq46AyHINXXoE90ThssgEpWHyNSIXGCb2uRkPltroG0Ktt6zq7ku1fINBQmQPZEwMyYJz1HOPyoOOrQjYd0ZMj-0UyBFBkdlv3HMfLBvyHn3J3_LNyD3fOVRsKGltT5_oaEmo8l0Wejt82SYhlUTXiUdWXiETwMK9UGmuveleblA-_WDCMt5Zeacmt1jV_ANO9axuGSYe0E8uh2oZG-QJ9Ts4PLt1bEZFKRXWjWBKZHVcW8vad33FbU1-mC7rqVBZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👍
🇵🇹
تواضع اسطوره و عذرخواهی از پرتغالی‌ها
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/Futball180TV/98684" target="_blank">📅 00:42 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98683">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uMkKECs5QzBK97s5E_yDD0VrWHwDhtRNBjUEowJRVirjgy7giK_c0rPRj-QHH01ogJ0RchoQvHzCyuAzbKLC69IDfhshHXPZHs73Dg-bnSOQpEX_C0MYOmslFRxIPQGYp52UoLdNw1YOI2x6vtOSj7SO9aMG_ZroppBW_ncgeCe-oH1POtDFjDiT9eUnTuaiEgH4QD5lfXVS-nmrN-NHSqzoPXco9ObYfsGmnm3F4XzYAGf-2f55K-kMC4TfQLgV7LC0Y6v0CMH3x7OLa02fvD0etumzBkRkzmeZTMnXmXP1fYlx3C3LyNq1XwhhwVwo-SjJSm64fgiyOjfDbPNW1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💔
💔
💔
💔
بدرود کریس؛ تاریخ فوتبال پرتغال بعدها حسرت داشتن چنین بازیکنی رو خواهد خورد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/Futball180TV/98683" target="_blank">📅 00:41 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98682">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FuckBet @FuckBet @FuckBet @FuckBet @FuckBet @FuckBet</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/98682" target="_blank">📅 00:41 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98681">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/grjUEnsQWQ3ufb_vhW6fNJbpKtKVBfwmNE6-Cwhnp4M4LawdvKvCtPy5wGkkK30EZBq1mYpjQLy__levDd5XJevINIEFvyJ1ssy17ek1uQ-67SpSiWjUlADBTPjtnNF4TOowxVGlfifJshQlPsZ5cI3AX9JmznvEx-1snTt1SppSfdFMY99IkDh71paOzMD3Rh02U7cmvn8DBVfSfHzHPYG9-obPcxCsXxq7-CVNJ5vkGIRr9HQjAR4sZD8BQ_7SNJj9nAmfMbqgYdN316HJY8rhzMv5Z6e5ILgdw453UeKhoYbRzLBjZyYcg7_rTSj1j5M8KCkc-zuje9QYHqRM-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FuckBet
@FuckBet
@FuckBet
@FuckBet
@FuckBet
@FuckBet</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/98681" target="_blank">📅 00:41 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98680">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N3_joGhIt8pWZrKNU7HavdIGbe3IHxLMRH475OSiTj2orTMSjdyld6ltmKHWjUzmATO19vZYlW2SB6GJCjQdTaA90zuCM1-_Wp6tqpOenQPdfoQrn1DHjTW9Gsd87ww_jAjp7AsINMAXTU290S39wiRv31l9HIofnlTR5MIT9LqGw3CoX9Dg9pSmSjVlraQE_ZYtfbSsqlBeEziRy-0xiodug_qx7KQAk2EntWn_1z73EIUpVzbUXzjVTzOzasoRk8FXWtiROojNNds6WqWuDdHouCliwZq4HguBLV2y4XtcEKXcpmlk2sOBDbell7zTyapU0WAmm0flShfI_A9JZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">و فوتبالی که همینقدر میتونه بی رحم باشه.
😞
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/Futball180TV/98680" target="_blank">📅 00:41 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98679">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mzwlzLB-WsWH-BCKjBPzkRykOisUlj8U8Xa2YYNvVl4L8ds_BQbF1M_Zeg2p_QaLpGgmrBxWqZLYoNZwmAiypByJxdc2k7_JQyRfezdZ8pOz8sJ2_YPBmTGrIM-4G0G_SlLrHbGnbMHqOB3tzCk50nULFw6IYw2SstLj79_0ZRPWlQq4gkoeqkqXcXaWPFKHF-WeD_r-CUG1cdhLhXJfv-6taoq_XKg6KGeveTSGE8gkQ_pNszcIj4ZEvTiyzZfYXErsYAfC6goaQnAOG6q6QCoRzCr7YlXsrPOf1_4trJPwaKG6BH9mmzCyS_jfdyiZqxDdW61KakBUDfCdI-nZZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
😔
اشک های رونالدو بعد از حذف پرتغال در مقابل اسپانیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/Futball180TV/98679" target="_blank">📅 00:39 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98678">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b45fc1c41.mp4?token=Hg84RZPK6FJYca7xlv5-VYai0eJHOu-vOn_6ovtvGGFDB_EUzHd3QkXYf0ACV-bi2WMoVWgCIVlJciI9aUiaPUDos5CZdX40JfqisGAz8CQhSnlPyy3OEg4jgtLjZT87kdC5JpPmo1IgLmuyqPFIjTiJwBloXKEgkSWR-YxGqIfywQFRt6N_ITSz-fICbasoa5RlUaCk5I3-7zo4_ZMvvKuEopfr6qxzrcaFzp7FamR1X3ausBc0SKaPltgRY8XdrdrrVEHhkh7mRnjTeZwhX0dROOJ0HoSV6CKTuVmtwhxS1x583eBZU4b0vdNgQPKjgq-NFo1GQVrx-epaaGouIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b45fc1c41.mp4?token=Hg84RZPK6FJYca7xlv5-VYai0eJHOu-vOn_6ovtvGGFDB_EUzHd3QkXYf0ACV-bi2WMoVWgCIVlJciI9aUiaPUDos5CZdX40JfqisGAz8CQhSnlPyy3OEg4jgtLjZT87kdC5JpPmo1IgLmuyqPFIjTiJwBloXKEgkSWR-YxGqIfywQFRt6N_ITSz-fICbasoa5RlUaCk5I3-7zo4_ZMvvKuEopfr6qxzrcaFzp7FamR1X3ausBc0SKaPltgRY8XdrdrrVEHhkh7mRnjTeZwhX0dROOJ0HoSV6CKTuVmtwhxS1x583eBZU4b0vdNgQPKjgq-NFo1GQVrx-epaaGouIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🚨
😔
اشک های رونالدو بعد از حذف پرتغال در مقابل اسپانیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/Futball180TV/98678" target="_blank">📅 00:38 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98677">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X8x28MmLKUB4lYwFAUH6AxMqo42mNyqUJRYnpbV7nxvZUQSgyXS8UtTQ5RSZkHEbKtNExfYiooOIH-RZEOpVPagLC9m5_QQtHD0mwup568QNx03SooSv8XgBnzE_B_1P3CHuCFdu01jyoK5CVNbyjk9eyel23PEWG3aZn2AuM_lh-cGUppIB0gaDf2pEiVLPfcPJgHnMdPP_ppPYB5wOqUsAId5TAWhuOi49sYkp3k8ci75eUniY92vOFWluNHzAgGtivOHBqdXKHHI_lpTRpEf2jgz2U9NKVuMT7Xk6lLWj1z70Qyr00GMyItpshCDPsORORVyjA-rT45VsLYK-Ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
دوتا کچل اما تفاوت زمین تا آسمون؛ یکی با تعویض بازیکناش ورقو برگردوند اون یکی با تاکتیک کیری باعث شد ۹۰ دقیقه رونالدو تو زمین راه بره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/Futball180TV/98677" target="_blank">📅 00:37 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98676">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ehpw2llk9LmA2HAsQna2f1V6L1NBGRE7ZKOLGb2vJxRejJS_4OjVySWpchNqdYE5CvSGW8FOl952V8xhKV0oO3L5L4bcPRdEdjZaPNrQ5wU30C9szX0cMbbaEHkvjnUMqguF77XLyjMqmEZuM3A5iD0kN6UBrrQqh1_Rti3H1sF_IyU0k3VduVXWnR_deON5WUx_R2OJqO39mwYKQ1ulVMa-GP1u8eUDMkX_NnBAR1Wn7yYCJWiT5O4aGGvrEYWQUJuxMYCjF8U9R5cBpvcCMXrqCWh0R0CwmXTXGFNebSKbuBNHQTBYf9v3iMEFLOzVf6r8dsp0H5umbZgZr9EyEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🔥
رودری بهترین بازیکن زمین شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/Futball180TV/98676" target="_blank">📅 00:36 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98674">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/O-XHOvMiJFyYmvxdBDTWvLM1G0sAySbPxcwW7Dzn0eI6FXFhvLyou_5069sCoJTqHDOoWoomVh3bZdLxGqwvrnXoNjBkI9saHgdVaS_v4huQwt9TqG-cww4Ru6SwyzA-E2-zLhR_ywIUtjgLaKiqfhsUjm-hB5lhGNrvRFGRqNM5YpydopdcWpW39D61uMH-hj3USQjENEsakZo4SAExvz75miVMsn4Py0tCFH5_eSPe6IcQEE83UxJVcMSqJ2fWmf73EKNFVukHjT38yG1rS1imcyvC16rgjGktx-lMfrpL5RLEOBaws5Ks7TFrOn3ra1vFk-I2l2T1dAjSbdt0KA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fJbHdMzHyONkINyI6BDBaShVc41rl-an6Fxhu2xHw1rIN554D2owylDRn3LUJRlJe2j6PHMyao7o4zGZOoeHDWZWj-nX3B9aFi-dguZMO-Amz6H4hFa62Ojkn6ppgLQIGk9uI6IdOWfy527rJM3MufqcXBhLcU2saU-PpPHeNIEYjadbsmr9M8qGVd8RWPKbfWYvt864DvE-JvJ9vv1lyTVpiK03lqcUyMHbwtI5UPH9JAFPkRWXXcNyxsR7p4hwnxDUR_KSnrGAXgDo9AfPuGav-9g_ccXCiqXcClGMoJ0Mu5T5GAWOuI0L4OP-Vw31qWL4UlQ4PSXH8MA-LeuO5A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
❌
و رویای رسیدن به قهرمانی جام جهانی که برای همیشه به پایان رسید..
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/98674" target="_blank">📅 00:35 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98673">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fJ1W2WjhmyyYDFgrThL_fMJLmMBwgYBPURBnD9qa57EIpFok9sfkfw-h8ThLpSsCwuLt3TEYScRlAUaKs_YeMyPvVv9rRZlVGFXvA4NGj_G2OC1bJHe5rUJxfNEGIj_JKR5nEQiYEzY8yuMOdTs1IR5f662lHjlvekZZsH6sDbbv7Prkten5YP9W41vmAqcUvJ7y9H0Veu6F7OQvbMQYP-rj8SWnHW_f8ozOJphsD1AnojQDiG_hItRwo5IdWhryRg6G4Yc76_CXanz6t-QLeZQlLy7XRDgBujoKvakEwxvb8aEtPsMEFACojJNbRri_iTfR-4aXN-sUYYstn6Oh2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
آغوش لامین‌یامال و کریستیانو رونالدو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/98673" target="_blank">📅 00:35 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98672">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SQ0OmdjZ2hqYSJNdMPbZfj98PGr_Kt4FRC72A1HJ0gl17pcAH5iRkDHr8MJLH8SUfbn6XybUSKITO5X5XmzzGysE1Dmy_myi2smCXP-HmNHytmKtdMn3SrpwtM5mkOxVmWgoQFwRs0DUnklmRO7hODrfOSs-Zb_owArLpLYpvkVSSBXj20HrrHfJv-xmia1JA4Tt24OEkK-V6QLb8829u-ztMullu4pMqcVl51Zx6MvPKs_4RNXr-EdkGkUCGGpXqp_YvjFOzcGEyRkvf7fwY1O4KSbMma28hQC3fXbYh7LRdB77HpHBpiGYmwUDyQm57fW-qmFO539ykMG-HbU3Qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😔
🚨
🚨
🚨
🚨
پایان عصر یک اسطوره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/98672" target="_blank">📅 00:34 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98671">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dceoi0JbzYqv58TAAhAfzo2jYay6mCvIXPYBGg1nkhXWPMcfIZl6hdLekYf5tpyIZ_PZ_qwzaJ_e2_PrvAQ1o5v5vH4zoN4EKgGJEv8YT8hAEHYxcbpoSj5N-EGIfHhAiXAjJLVkztfRFh2gzHkUvZCDcK63XQUBHz1N0DwN6RSO1D4ZbK36BRc4tPmaXZ5pSYeWxhQ54e1kTF7ZEC-iWigUe6leFUsJxVssUjoaR4UyZtFFRIwssT1EURvg7OZIBrM5vG2PXZ7qw7H8LQ95W00zzm_H_dhKSmVYg8QtZdepm7t8hTuK_oujsHxtLBngYxhhJGdzQpbQxS9ufWnLKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🏆
پایان‌بازی؛ رویای قهرمانی جهان برای CR7 نابود شد! بازیکنان ذخیره اسپانیا شاهکار کردند! پرتغال و ستاره‌هایش با جام‌جهانی خداحافظی کردند!
🇵🇹
پرتغال
😏
-
😃
اسپانیا
🇪🇸
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/98671" target="_blank">📅 00:31 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98670">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">وااااای</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/98670" target="_blank">📅 00:31 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98669">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">کاستا جلو اومده</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/98669" target="_blank">📅 00:31 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98668">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">فرصت آخر پرتغال</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/98668" target="_blank">📅 00:31 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98666">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">۱ دقیقه تا اشک ریختن های تکراری رونالدو در جام جهانی</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/Futball180TV/98666" target="_blank">📅 00:28 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98664">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Tv7X5vY7rGqthRf5RlN7CIn9JLbruIDQkR1Yr-tG9b-G-zO-D_E04gbnMA5J0XPpEhtZw1Ltcn1IlU5htcdRjUGKVKhERp6i8OPmhmTULXrDq27K8vGKyPF952Eq1-ZRN_r15H2fS-0hNDsb1YRNFyV4tSWCY2PloTlXuyC5kIuD5rwyM1WNrFPkzu3NfxZtfJmK4ZUQ0ic72e9BaS556jXN79zlw9UTzwYwFc_KHD7K-8YBsR08XyYcuafqfrk6Lwf1ojEJ-15XVe5dyF17mutT92vMJz3mezzBwVcxbbnLWnFLpgEO8xy_c4rHB5ni7TQkTJkttySZQUCa0RKMhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/R4Fd12bJ3AIC1hGjcKKhfSYl0Dt6ktLZArCiTIIbUwpdPUNmow9yyTfRAk3UYGTWGXifXh5UZeoqeiQKM-Z6IdWTtlRAf7u7FLMD1MQN36mA9l4AM51aq99Zd4elk1yMXdEUoge8CoP92YbrYLSdHPSeBgW0dm6vYG239pH4ldxzqygzY0xTy3hxQpFlkrwwhGIwhyCPE5F-tl9vmkctFJdgbHS1zNe90304ZJGr04axxvK0jkqsp0pgDdXD8VTArU2neBIya1jC_FPgI10Lmac3PFImN9TPYMDJ8WGT38NowebxoSjrcL-g326i63l9th_u1t7h3XpDgihysCjC4Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">لست دنس و این حرفا؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/Futball180TV/98664" target="_blank">📅 00:25 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98663">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/32526464ce.mp4?token=tl8PDAxdqwAUm5UuaBGxePHxf3uKcgNE3aB3XK_TvKJ3s6efzgm2U_GdUXWFZ5_HbyxfFGkbniXvQUdZJgi2S31klUxMPCXVUoWlAZdbunjlMpk3MR7PH0JTvCurienERraxsu_toAeWOYM0DjPWFgcPlhwrfH428UjeVFjyvK4UiLKA8U4fF76Gm5TmNK1E4sjgzajKPc7NZfSoubyKn4YGZYxMHvu-z9VgAqdDbyVfzk2CfomnpdjVsSO3jSxU3pJjymhI7tEEyB3H76OLRYY4sXbu6OPO7wF2FH0yx23fqlRe6XPVj84-33opcBuatYU_DFaXyVHlm2izKxB4rTdEh2ZLky46J12DTo9xLRdm3xUi_gxdyPZ4n0CKnSCse636yDj5_uW99S3SUY3Jatmbh34ed0RxNh78sUDPV_tqbiqZB-07febTIWmIhFhl5ClvQl970zhPhyrrdywsmEXH5Edtb7GIQ0bOe98ZCXn4wlC4ksZXItqLHhqFQXs0B2cckj_yoHPxKks6ijFxj3_GLiFAN0fnB-osymL_7F7TiB0p0baiFq1oOeV6zVR53fgZ4CjHLXoRFPx5ip2XBHLjzEpHdzlGnLRYh4aZO-PphcROn6YnU_JTZrk8t8pCWyGBBPdrm78CK2ems8L_5HFDHXLFYDyh1HAaB8wnygw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/32526464ce.mp4?token=tl8PDAxdqwAUm5UuaBGxePHxf3uKcgNE3aB3XK_TvKJ3s6efzgm2U_GdUXWFZ5_HbyxfFGkbniXvQUdZJgi2S31klUxMPCXVUoWlAZdbunjlMpk3MR7PH0JTvCurienERraxsu_toAeWOYM0DjPWFgcPlhwrfH428UjeVFjyvK4UiLKA8U4fF76Gm5TmNK1E4sjgzajKPc7NZfSoubyKn4YGZYxMHvu-z9VgAqdDbyVfzk2CfomnpdjVsSO3jSxU3pJjymhI7tEEyB3H76OLRYY4sXbu6OPO7wF2FH0yx23fqlRe6XPVj84-33opcBuatYU_DFaXyVHlm2izKxB4rTdEh2ZLky46J12DTo9xLRdm3xUi_gxdyPZ4n0CKnSCse636yDj5_uW99S3SUY3Jatmbh34ed0RxNh78sUDPV_tqbiqZB-07febTIWmIhFhl5ClvQl970zhPhyrrdywsmEXH5Edtb7GIQ0bOe98ZCXn4wlC4ksZXItqLHhqFQXs0B2cckj_yoHPxKks6ijFxj3_GLiFAN0fnB-osymL_7F7TiB0p0baiFq1oOeV6zVR53fgZ4CjHLXoRFPx5ip2XBHLjzEpHdzlGnLRYh4aZO-PphcROn6YnU_JTZrk8t8pCWyGBBPdrm78CK2ems8L_5HFDHXLFYDyh1HAaB8wnygw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
گل اول اسپانیا به پرتغال توسط مرینو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/98663" target="_blank">📅 00:24 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98662">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">پرتگالللللللل پرررررررررررررررررر</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/98662" target="_blank">📅 00:23 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98661">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">پرتگاللللل پرررررررررررررر</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/98661" target="_blank">📅 00:23 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98660">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">مرینوووووو</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/98660" target="_blank">📅 00:23 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98659">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">گلللللللللللل اسپانیاااااا</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/98659" target="_blank">📅 00:23 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98658">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">تورس چیکار میکنههه</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/98658" target="_blank">📅 00:20 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98657">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">برناردو و کونسیسائو وارد زمین شدن</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/98657" target="_blank">📅 00:13 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98656">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">تورررررس خرررررر ریدههههه</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/98656" target="_blank">📅 00:12 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98655">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">اسپانیا فشااارر آوردددددده</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/98655" target="_blank">📅 00:11 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98654">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">واااااای</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/98654" target="_blank">📅 00:11 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98653">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">وااااای</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/98653" target="_blank">📅 00:11 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98652">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">بازی این دقایق جذاب شده</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/98652" target="_blank">📅 00:11 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98651">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">فران کوسه ریدددددد</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/98651" target="_blank">📅 00:10 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98650">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">برونو داشت میزدددد</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/98650" target="_blank">📅 00:08 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98649">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">واااااااای</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/98649" target="_blank">📅 00:08 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98648">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">اسطوره فران تورس داره میاد زمین</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/98648" target="_blank">📅 00:07 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98647">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">لیائو و دالوت برای پرتغال وارد زمین شدن</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/98647" target="_blank">📅 00:04 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98646">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🚨
🚨
🚨
عصام الشوالی:
تیم ملی پرتغال به صورت دفاعی بازی می‌کند و وقتی شکست می‌خورند، می‌گویند رونالدو هیچ کاری نکرده است. چطور می‌تواند کاری انجام دهد وقتی کسی به او کمک نمی‌کند؟</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/98646" target="_blank">📅 00:03 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98645">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromتلوبیون اسپرت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OdbZZXD44G6gzDFfM0PXNoFr2xYseARkFIooVmKmnelXmJtgUp7YFjAiyAAn2edpUdiTj3EEYB3GluzEVcPC4fW4UNQDI0g2oUGB21WGjjsi6qMHtbskyb8bYVLfeT4TOPnYeQ030KEJG-wwA4zBW58ZbhFlL0ixgou4U9DJfcNdJWZxA5_2B5LzWXJOfB6M3pP2hkws4XBE5VCB2XXdim_UtYBwrEr16kU1lSLteePWXMz9BM92khC51NxKTP7ybzQJdM_PDnu9n1OL6JGFvaC9ojINW1D8NJfTefqtF9-ca0fmKdHiX03DMTDbct1IcBZLJ-pC8kQvUJ3lM0Bn3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎮
اسپانیا یا پرتغال؟ انتخاب با توئه؛ تا از رقیب عقب نیافتادی از تیمت حمایت کن و پلی‌استیشن ببر!
🏆
👇
👇
👇
👇
🔗
همین حالا حمایتت رو از رونالدو یا یامال در لینک زیر اعلام کن و با بازی کردن پلی استیشن برنده شو!
👉
Https://tcup26.com
👉
Https://tcup26.com
📢
این پیام رو برای دوستات بفرست و به این چالش بزرگ دعوتشون کن!
🤩
@telewebionsport</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/98645" target="_blank">📅 00:03 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98644">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">مندز تعویض شد سمدو اومد</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/98644" target="_blank">📅 23:48 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98643">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">نونومندزو گایییییید یامال
🤣
🤣
🤣</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/98643" target="_blank">📅 23:46 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98642">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/MAhubVCTQtFylU83HKjZ24kFQPF6iq0ob3ddBgGHXLBVUkwYgcT56NJEVr8WQ2a-xOKU5rAMQBVUkKzk9wrkekQvULtUtHrMGW4f3nFUWuR-t-oLqNfyHF30-xv5rUgAc7rzE9uwyKbG40aNOUngDMy5cu0iKTr2RsoviIk9AAYhMdKQMmSAdPPThTfvAiikQJAh94H-j97aJKCzJHsq_PFn8Hv_sJaPh0ZgymoIONfw_bLN4RmMD0fhwfvb7YwzNAjl0pONbEb3Lx58LER2mbqRxAI5GgKh4G55fOwc9YvD-pzzGVEAgsk4cip6szXyYItWf2FY6yfdQnyxFEKGSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اقا سطح اینارو نگاه
سه تا از بهترین هافبک های دنیا توی ترکیبشونه ولی دوتا مهاجم درست حسابی ندارن باهاشون بازی کنن بعد بجای انتقاد از مهاجما از هافبک ها انتقاد میکنن در حالیکه دوتاشون چمپیونز زدن و یکیشون توی این فصل رکورد بیشترین پاسگل تاریخ انگلیس رو شکست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/98642" target="_blank">📅 23:38 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98641">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🚨
🇵🇹
🇪🇸
آغاز نیمه‌دوم بازی اسپانیا و پرتغال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/98641" target="_blank">📅 23:37 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98640">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M7cYEInv0bzu5hGNauXqY_EscsH16pw6geL2_STwMUSnY1VuRHR8uaL-S9CnOF8Rp1meEE2qTidm0QV6yW6LEk_evALr8hNECGDlskua5CpbmX07a4mbd9mlxrUiNF-9QPhFFfx8GEpX_Hm_-tNjQ1Yqgq3kx2t8jCuG9-Mo5d8Q5sp3Iewt0DlDY1UnooHvJERxZRL3TsLQSnUjLk6aoU3tV03ogeIDm4itf5Mk66YHaiUtJHUwMniS5niF44e9tHWUuMxl2nFG3XYoMSe_4UshYhAks0aGCdEhzBosvuxy5IkzLQzlzK26_Iesn65tYcAsSNXREscFpmw-YRRHgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
🏆
| تا پایان نیمه اول، اونای سیمون دروازه خود را به مدت 564 دقیقه متوالی در جام‌جهانی بدون گل‌خورده بسته نگه داشته است
🔐
🔐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/98640" target="_blank">📅 23:30 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98639">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WaW9KeS9h6OIuroqKfzkdps1PX1fjx9L4H7j9K-tUYLdEJPdKeJzYxZP2s43kWBIkfrniFImzKZWVmhAxYgZhwZrQFZnSgH0v7LiWqmrJ9UlsyIdbPNh4yIBX328Iv8Yjs78ajRFl5esuWBEu0A778utWjQUyXVqsPB3YZOviqC5qw5mv7STOyQmrvZYER9b43iu_6Rre7fmxprxe-Etn2CHtdUwQKXRDU4rPf0Qs7ZLUDdbJpWZFbjC-7DDna2A4k9t4hRIPqXXTFl7pplsrNw30nlqPV0KK1zLUVub2cK4lD30R-tTXCr7uWNDaf8DjutX-bTpDRqdq0-OA620RA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گاهی وقتا هم کلا دو نفر هستن که عکسو خراب نمیکنن.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/98639" target="_blank">📅 23:25 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98638">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mei5dt0BqZgSIeVUUdAdI2Lru3x43n-UfqcTHsNGI4LVW4TmUsqimqxSMMButw0kU95UxYklpco842GO1_0nNdvXFZXszsknpZ5SPvB2eI8WouNmqmq_cdTpMfHspGvTIRJQTxPzpHljtYGJeX0fuvToZ9GgQOJTE_W9V5tvMF1SVKQZ85muTmSP5uOJznyrFgj4nQckEfdIw64m9jKLjqwY3tF_LtqtKPI6qrKL_AOudGzilH56xmTNjOXheui-W6U-GEja8ncf9SH6_c2NRjZNfagrVUAeJD1sR89mAerz6O17_P0L0iHT8ToP6nhOrMGWZ_8Ox3yTdmbk2lcCWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
🔥
🔥
🔥
🔥
🔥
🔥
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/98638" target="_blank">📅 23:24 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98637">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HgZliLKuN6mPtJZQoXABlgvWlop3Tn89fvLjxhjtm8hNbp1gwajBy7HotHTnO8D4ltMRDUTT7-SeDHIP_bgDWV_BG1hxN0ThAp3j7FCKLDxZ57xYz3bQHUyOKlXtsBfAjj78jayeRmObKFeqh_EoflHWlJjRflRtL35QbOT3yBkom52bek9X9fUH4vOdTtSZMOSAxWMTMfR_r1_ALjy9qh5D3_QShzTxAYwKaqlN6G0PWptk0wVR3N58jxA04uhpd129T8ou6bPA_emce-MPfzsjbdx0YXhmpU4b1zf54EexOOIMamASXn2cTK1_lhWWacNS1bjYnnw1n1uTY3rSsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
آمار نیمه‌اول بازی اسپانیا و پرتغال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/98637" target="_blank">📅 23:23 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98635">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🚨
پایان نیمه‌اول با تساوی بدون‌گل
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/98635" target="_blank">📅 23:21 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98634">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/257e1f3178.mp4?token=r_wX9-gdvCDiiYTx6XAQujjOrJnLycGD80kcw7fiGaol7aPNmIr1CEA49Q2t80aT8iv2xFxpuiCA-0nKQ0WlU0lW0DWYR4C6tqOGt1LqmzhMiK0l1nPUpTcX2rBAjQQjtNTef5ObAAnyzW8nkwMnRwnPB6YYCV1kykI0iQb7z6bYn8IiQaIGDaLKSXRpKYMBNxJ9JZdOD8f-618oDoVhg6zwvjfgaPEHraGupKSIKCcSnntuXVSbrnILC2c1rg8Q20OGT7e-3aIa2WF2l1xu5j253FpUcc687aCAJKZB7uShPaG0u9NsSiIva8iIvl4A_OiMKCPAt8bYgEGyTrQqdIuk3tdD1M5OvZ1zeoEBWnmC6zkbQezY1IfHidop5lxWrZUXnLmWjDUo-Caxw8XxrUIW7dhQBXdRWqVDSA_jp618MUeVpLmXmAbA_QeH8zyBG4v_l_A_j_Yh8WwGe_G0WWXTmnfgyt5JQKTeBaJxD90WzGkFAH56y6SqVClWqWAmNyNXpp04FNTJZDp3KOkrRG_BTOAGmidsJHYWvlOiPzRceh9IMEdpTeFK4zVQzrzn21gzdPo9G2fIeIDS_yXhu_qpUv8pJoejXSKkZhV7Up8P6zvA5L7WujkohFL9aJDAXhROTB5G5mmaYB-x8lZtzufzq5yONuT1r7J5eabcVQI" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/257e1f3178.mp4?token=r_wX9-gdvCDiiYTx6XAQujjOrJnLycGD80kcw7fiGaol7aPNmIr1CEA49Q2t80aT8iv2xFxpuiCA-0nKQ0WlU0lW0DWYR4C6tqOGt1LqmzhMiK0l1nPUpTcX2rBAjQQjtNTef5ObAAnyzW8nkwMnRwnPB6YYCV1kykI0iQb7z6bYn8IiQaIGDaLKSXRpKYMBNxJ9JZdOD8f-618oDoVhg6zwvjfgaPEHraGupKSIKCcSnntuXVSbrnILC2c1rg8Q20OGT7e-3aIa2WF2l1xu5j253FpUcc687aCAJKZB7uShPaG0u9NsSiIva8iIvl4A_OiMKCPAt8bYgEGyTrQqdIuk3tdD1M5OvZ1zeoEBWnmC6zkbQezY1IfHidop5lxWrZUXnLmWjDUo-Caxw8XxrUIW7dhQBXdRWqVDSA_jp618MUeVpLmXmAbA_QeH8zyBG4v_l_A_j_Yh8WwGe_G0WWXTmnfgyt5JQKTeBaJxD90WzGkFAH56y6SqVClWqWAmNyNXpp04FNTJZDp3KOkrRG_BTOAGmidsJHYWvlOiPzRceh9IMEdpTeFK4zVQzrzn21gzdPo9G2fIeIDS_yXhu_qpUv8pJoejXSKkZhV7Up8P6zvA5L7WujkohFL9aJDAXhROTB5G5mmaYB-x8lZtzufzq5yONuT1r7J5eabcVQI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😆
😆
😆
😆
😆
سطح یامال عالیه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/98634" target="_blank">📅 23:19 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98633">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">رودری به آسمون کوبید</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/98633" target="_blank">📅 23:15 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98632">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">پرتغال خوب موقعیت ساختههههه</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/98632" target="_blank">📅 23:11 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98631">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">وااااای</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/98631" target="_blank">📅 23:11 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98630">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">واااااای تیییییرک</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/98630" target="_blank">📅 23:11 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98629">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">چیووووووو نزد پرتغال</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/98629" target="_blank">📅 23:07 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98628">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">واااااااای</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/98628" target="_blank">📅 23:07 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98627">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">اسپانیا خیلی موقعیت خراب کرده</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/98627" target="_blank">📅 23:04 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98626">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">چیوووو نزد اسپانیا</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/98626" target="_blank">📅 23:00 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98625">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SW5IpSpB6c_FTy6UP1ZhKKMIEuTLN-3sn970B0XCVYouSjlrWzVXg2aC3iI0XszTS47Rq5Yk4PeYH-7HL74zQDy60DIh7ePpwJCL9We79BxGFBQNA6vUKvebpQ8YonFqRfZRaGxiGoJf3cx6lgLCs6dFCxXinS8rM-hnsDu1xMAhggaT6HoDiSeQ6HQKkHA_PpM0MZXPLPNz_hpDLLJ1nZeOXfFGSccASPKGcLtfwHE9cQ9ibdc4D9wIZ8bHamuSuCk6ZZGmo4r8X1w0UlxTTPpnOW_giWK_-jJ6GpWnKoaOHrknpD2i0x5KTlyB5GV463le1PX6iKk8VzxuvkLuqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بدین شکل
🤝
🤝
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/98625" target="_blank">📅 22:58 · 15 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
