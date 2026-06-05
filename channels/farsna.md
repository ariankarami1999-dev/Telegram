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
<img src="https://cdn4.telesco.pe/file/agAWrVwb3WwMWFHpC5VYGzGUTzPgMHhLzzM2ZoPWhKvwb6YRes-r_4-KFXKC6XPWVJiFXeg7SL22FJnvw1NLOp9c3ueiZ9sulDMSrJaRSK3vNNKvfejItGg-rq3jH2r4C84wWOjAaK42GY3m0B2jcCD0QnZeMKhysxi1UQTiew2qm9w46lUfrnwdfJfhlGxGyb_l7WdS3IKoq_zeyRcDSo7juhL69SGDxc_tpzJPbNuYLAdBNW-0tV_QXfBOleLjIxfm8V5h1m6WI5_joCXYchrhLa-qk9hrZ4eEJSU4LARxledpuM1jYT15wafmvE5IFgJMQgx0IA8T338E01ioVw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.82M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-15 20:29:14</div>
<hr>

<div class="tg-post" id="msg-440100">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JOLIKpNynMvfPB7TD0HnxuNMFPT5tIAWKLa-OCrm4ABLv7eS6WJLQtw-2S9ASe3lh8m75ISnUFs8IhFQWcV7vLGAjRa_Rm0PmPA1ZJmKGammSW3rnP5lsrAz53IhXwy_90E3teA8Tq-sKf4HOZ767Ne1zW1wE5yWbR6pWfu270_hnVz8PYUbUijCjEtCLvuH_t54wj7tlMFiiYASny65D6L32nP5vtGdlXrsmrWVIkq6IjMi3qUR9Wfn6kwbxyvDSRh0iPALhTcEj8BUnY-4P9cO1oxiBLvOtqhFCPRLNML8FQvmDhTAf3nwokYOLSBeiq2H6u02QEJchbNyr79hFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پوتین: ایران به‌دنبال سلاح هسته‌ای نیست
🔹
رئیس‌جمهور روسیه: ما از تصمیم توقف اقدامات نظامی در ایران حمایت می‌کنیم و معتقدیم این تصمیمی عاقلانه است که می‌تواند به صلحی پایدار منجر شود.
🔹
من هیچ تحریکی از سوی ایران نمی‌بینم. ما معتقد نیستیم ایران به‌دنبال دستیابی به سلاح هسته‌ای است.
@Farsna</div>
<div class="tg-footer">👁️ 595 · <a href="https://t.me/farsna/440100" target="_blank">📅 20:28 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440099">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d046ae554b.mp4?token=SZHCveHlD0xQfTfhiHVCfBPVCPXmPqcUuQEaeGOeK3KwMOJNLwCTbKOdlKiD5UWxyMgKpLdLm6xBb0D0cBeer4hF-7Zv6L9t34_9pPJug9T0ChX3InmkwXbkvtnTOlX7drEORgLBZ_hzAGJIpw20tvTiEPMILQRPpDXxJAlgY1HSYX8m933z1Z0o0lebapGe_Jsq596v7Uhdqg0dZ_ED9X_JsrNbbnK5EdJrxmSk_3rnScW32wF1HYPPl_bweBB32yT4ZLpP_z1tsE9_5mWSqaToDs-AcKjCBz0Vse-flpXCJQvMgXiIBtHkbpuTO7EwbQ0IHmd8meohAKt0GG3zcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d046ae554b.mp4?token=SZHCveHlD0xQfTfhiHVCfBPVCPXmPqcUuQEaeGOeK3KwMOJNLwCTbKOdlKiD5UWxyMgKpLdLm6xBb0D0cBeer4hF-7Zv6L9t34_9pPJug9T0ChX3InmkwXbkvtnTOlX7drEORgLBZ_hzAGJIpw20tvTiEPMILQRPpDXxJAlgY1HSYX8m933z1Z0o0lebapGe_Jsq596v7Uhdqg0dZ_ED9X_JsrNbbnK5EdJrxmSk_3rnScW32wF1HYPPl_bweBB32yT4ZLpP_z1tsE9_5mWSqaToDs-AcKjCBz0Vse-flpXCJQvMgXiIBtHkbpuTO7EwbQ0IHmd8meohAKt0GG3zcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
جنگل‌های ارسباران در آذربایجان‌شرقی، بهشت سبز طبیعت‌گردان
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 2.53K · <a href="https://t.me/farsna/440099" target="_blank">📅 20:06 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440098">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HnpYgysWyH2AyYSDjstZIfJ6d6yWJYSedYi30YBuzsBMQ1Pmq2g6imeMseUmX7nlu7thDy0ELcizjilLGxVfr3RQHFck88xSuVMkY7VJeEvjM-2z9lbijLhKM3dtqNwolpmkwqbhxSNmthLIbFM5FNuzuNSjj665Lj5DqiuZCzjCBlH1oAg0cQi1eqKSXhVqqPGv8ts6aJ6GTRsfOBOOwF330WYG2ktwnYnj7YcAWsmo0MZj-JVwC38KyAPgI7-cq_yg7ub2sPvANROF2JODg45_z3ZSYC-smj_pU4WJcIxBHQj3UmDbrEQeZmdEYC0VLr8_B9SXTxQTcDH7L81MdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
پزشکیان با انتشار تصویری از پرچم ایران نوشت: سرو می‌ماند ولی طوفان به‌پایان می‌رسد.
@Farsna</div>
<div class="tg-footer">👁️ 4.96K · <a href="https://t.me/farsna/440098" target="_blank">📅 19:40 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440097">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">زمین‌لرزهٔ ۴.۸ ریشتری در عمق ۸ کیلومتری زمین، حوالی منطقهٔ بالاده در مرز استان‌های فارس و بوشهر را لرزاند.
@Farsna</div>
<div class="tg-footer">👁️ 5.69K · <a href="https://t.me/farsna/440097" target="_blank">📅 19:28 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440096">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/384f94b258.mp4?token=GmpQDUpBLoiDGdkapQ8zqxoVNALaVlZPmP2Ny0Uy8vn6w4L20tGAnRQUxanFImAkzhKKN0c13GcHd6ilSxsqhd1Lspm6AEywcagH1rp3TE6w-ljfr5zANIRhAk-kwQkfHjI1gWoXboBMZnuOqhswd-TYe7xcKwyU8gFejtgzIyWsUK83p7ikMJTYdbETMDphSvOOQ-9VOyOlNhKJtIgTusugxJi9DbcLUFbuvKKoJQ-b9s48rPTvY_2wcbLMB281zR1-HH8qHU-A08Z0nwA-VqC5BkX9YQ6FGZSLufpPeD5a91pGCaxLO3iAXgg7RjVb8cO6t4dNZdPi8xFkYepFKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/384f94b258.mp4?token=GmpQDUpBLoiDGdkapQ8zqxoVNALaVlZPmP2Ny0Uy8vn6w4L20tGAnRQUxanFImAkzhKKN0c13GcHd6ilSxsqhd1Lspm6AEywcagH1rp3TE6w-ljfr5zANIRhAk-kwQkfHjI1gWoXboBMZnuOqhswd-TYe7xcKwyU8gFejtgzIyWsUK83p7ikMJTYdbETMDphSvOOQ-9VOyOlNhKJtIgTusugxJi9DbcLUFbuvKKoJQ-b9s48rPTvY_2wcbLMB281zR1-HH8qHU-A08Z0nwA-VqC5BkX9YQ6FGZSLufpPeD5a91pGCaxLO3iAXgg7RjVb8cO6t4dNZdPi8xFkYepFKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پوتین زلنسکی را مسخره کرد
🔹
ولادیمیر پوتین گفت: «همه دیدند که دونالد ترامپ چطور داشت زلنسکی را ادب می‌کرد.»
@FarsNewsInt</div>
<div class="tg-footer">👁️ 5.56K · <a href="https://t.me/farsna/440096" target="_blank">📅 19:25 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440095">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">خزانه‌داری آمریکا از اعمال تحریم‌های جدید علیه ایران خبر داد.
@Farsna</div>
<div class="tg-footer">👁️ 5.7K · <a href="https://t.me/farsna/440095" target="_blank">📅 19:21 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440094">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">بسته خط ۵۷.pdf</div>
  <div class="tg-doc-extra">6.2 MB</div>
</div>
<a href="https://t.me/farsna/440094" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">بسته خط ۵۶.pdf</div>
<div class="tg-footer">👁️ 5.71K · <a href="https://t.me/farsna/440094" target="_blank">📅 19:17 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440093">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a3bb2538f7.mp4?token=iAPoYLBDOLqz5sjVMTC1OJyQ4a7I3PE3cAeR7rNEYrsHws_n6-6bTZYb_WpXneWDllnFb6xTgDoDP9gfDj_br1gdHpzVsqtEd5aJFTC-nj50IXtU81VOjFN1YxxOC-_FUgscnT63fzJjyJsBCzqJpeYW2e-XIR-bYMwhF-niQG788aSORykmLV1Q-w6B1djSP83tM-G6PQusYiY2h_O6OB3iQURbNFcut2fkIG1Fd17lTm2lEQK1nodO6of46LQ69lXSlQn6bhzyKafMrHwWF1HkWpyQJbTKEf1pjEUdjaicCySCiXCnmkeRZWgzsiEfABJQriSbUH6osXWCF4t8JA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a3bb2538f7.mp4?token=iAPoYLBDOLqz5sjVMTC1OJyQ4a7I3PE3cAeR7rNEYrsHws_n6-6bTZYb_WpXneWDllnFb6xTgDoDP9gfDj_br1gdHpzVsqtEd5aJFTC-nj50IXtU81VOjFN1YxxOC-_FUgscnT63fzJjyJsBCzqJpeYW2e-XIR-bYMwhF-niQG788aSORykmLV1Q-w6B1djSP83tM-G6PQusYiY2h_O6OB3iQURbNFcut2fkIG1Fd17lTm2lEQK1nodO6of46LQ69lXSlQn6bhzyKafMrHwWF1HkWpyQJbTKEf1pjEUdjaicCySCiXCnmkeRZWgzsiEfABJQriSbUH6osXWCF4t8JA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تشیع پیکر شهید «قدرت زرنگاری» در جزیره هرمز
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.99K · <a href="https://t.me/farsna/440093" target="_blank">📅 18:38 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440092">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2023097cbf.mp4?token=VwSPG_wUyH1kD6MK209eOr6THnTkHCk2eKH-akvlox5VjJEqEFPi7IVbEOeWvsmCE5hHAIVejAb4sQa1He-eTlh2_zLIqsIzCKL2_dRJMSY0IMpVLE4NYoOcVJo6E2EEFK3MwtUhgW9VuL0pW0Zzf5q-u_QrfNkpMos8yBUcMoiOfr3aM_TZWCFbFvK3HU3ClI1c9uhSH79C9Wqq3Gsff4k_omah-kz9iyCgeVqVlzFI0gZo40r4lssTkuG4Q9NEFwxlRqtybS-HXzRV6b6rPvV8VkZCbNs40k-Tw6M8FMOOFKXNP1C1pPnLX0jMcrjoM900AUMIby9U1z0OxqBv0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2023097cbf.mp4?token=VwSPG_wUyH1kD6MK209eOr6THnTkHCk2eKH-akvlox5VjJEqEFPi7IVbEOeWvsmCE5hHAIVejAb4sQa1He-eTlh2_zLIqsIzCKL2_dRJMSY0IMpVLE4NYoOcVJo6E2EEFK3MwtUhgW9VuL0pW0Zzf5q-u_QrfNkpMos8yBUcMoiOfr3aM_TZWCFbFvK3HU3ClI1c9uhSH79C9Wqq3Gsff4k_omah-kz9iyCgeVqVlzFI0gZo40r4lssTkuG4Q9NEFwxlRqtybS-HXzRV6b6rPvV8VkZCbNs40k-Tw6M8FMOOFKXNP1C1pPnLX0jMcrjoM900AUMIby9U1z0OxqBv0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">با راه‌اندازی خدمات شبانه‌روزی برای مشترکان
نخستین فروشگاه دیجیتال همراه اول در تهران افتتاح شد
همراه اول از نخستین فروشگاه دیجیتال خود در تهران رونمایی کرد، مرکزی که برای نخستین بار امکان دریافت بخشی از خدمات اپراتوری را به‌صورت ۲۴ ساعته و هفت روز هفته فراهم می‌کند.
این مرکز که در محدوده ونک راه‌اندازی شده، با بهره‌گیری از کیوسک‌های هوشمند خدمات مشترکان، مراجعه حضوری را سریع‌تر و ساده‌تر کرده است. توسعه این مراکز بخشی از برنامه حرکت به سمت خدمات هوشمند، منعطف و مشتری‌محور است؛ مسیری که می‌تواند شکل دریافت خدمات اپراتوری را برای مشترکان تغییر دهد.
@Farsna</div>
<div class="tg-footer">👁️ 6.53K · <a href="https://t.me/farsna/440092" target="_blank">📅 18:33 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440091">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LVq6WdXsaSQOt6YQ_WnEHWi8gDg7DmitPSfr7ANjR7-Ln0suLVwD1EYudwFBT1pjCw3qGfTtcO6VgN9PTY6YAbBWsJJK4gXAj-O5cWOvSvwkC4U8ub_dfOJ0qTfJkQrTVVB_rdmsa2bw2aM7ItiIwarEYasKBeC8PPr8vkiavH3bfXkaJiSQMMJhEqOb1R2rpaY2_wOVEMnmP6Lm-K1feuZPVz6_k7s6xqZVOqJI-3_9L7Xl8GOrA8BTHaJ6MT2J0dEq3SwxGC6GIXCVgjHWKb6WmvXLamgEK_wQS9AnU51MN_CXPUhQBgy7ycxpLG0ldSTMIH3BZtIlkzfN9quSBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای همراهی و شرکت در پویش هنر برای زندگی
لازم نیست هنرمند باشید.
هرچی دلت می‌خواد بفرست:
نقاشی، دل‌نوشته، عکس… حتی یه خط ساده.
چون هنر راهی برای آروم شدن دل
و کم کردن اضطراب و
خستگی‌هاست.
آثارت رو به پویش هنر برای زندگی بفرست
تا با هم، با هنر،
از سختی‌های زندگی عبور کنیم
شما می‌توانید آثار خود را
اینجا
ارسال کنید</div>
<div class="tg-footer">👁️ 5.88K · <a href="https://t.me/farsna/440091" target="_blank">📅 18:31 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440090">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-footer">👁️ 5.23K · <a href="https://t.me/farsna/440090" target="_blank">📅 18:31 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440089">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f6ef468147.mp4?token=jAAoEqBFQT_0hVSxrjPzEWLwp3cgegvx1abjMvdqIm0xEvrocYNsbqei4ATp08mkl0M_XRQVuT7xRP54j4xAAIX6NKaw8p819K62jzwvBPwtnaG9L1rfYh3GrEg7Wbux5RSRu7i2HjpwczCYsbXsLhFBxbbSONXye0jwFcwvdJQwcvzTzmF0Zs53jYtEY6TnyqvUYlvEO_K3jZ9J6J7jVmp8ri_DBBt7iDeSX194VGCxbk7-cbmtVCgvE5qDQWUWGnv0zJ7DQ5Q6ywYKKsuVVmyew1IBllWoh4XkVvKOVg8d1O1CjDXeVMkxDZQBgO6Xp0279pfIkhmjcd6ZEmsoPYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f6ef468147.mp4?token=jAAoEqBFQT_0hVSxrjPzEWLwp3cgegvx1abjMvdqIm0xEvrocYNsbqei4ATp08mkl0M_XRQVuT7xRP54j4xAAIX6NKaw8p819K62jzwvBPwtnaG9L1rfYh3GrEg7Wbux5RSRu7i2HjpwczCYsbXsLhFBxbbSONXye0jwFcwvdJQwcvzTzmF0Zs53jYtEY6TnyqvUYlvEO_K3jZ9J6J7jVmp8ri_DBBt7iDeSX194VGCxbk7-cbmtVCgvE5qDQWUWGnv0zJ7DQ5Q6ywYKKsuVVmyew1IBllWoh4XkVvKOVg8d1O1CjDXeVMkxDZQBgO6Xp0279pfIkhmjcd6ZEmsoPYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سیداحمد خمینی: دلتنگ حضور رهبر شهید در مراسم سالگرد رحلت امام‌خمینی هستیم.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.1K · <a href="https://t.me/farsna/440089" target="_blank">📅 18:12 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440088">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🎥
حضور تاریخی رهبر شهید انقلاب در مراسم شب عاشورای پس‌از جنگ ۱۲ روزه
🔸
بخشی از مستند «روزی که با تو بودم»، روایتی از دلدادگی مردم به رهبر شهید انقلاب @Farsna</div>
<div class="tg-footer">👁️ 7.9K · <a href="https://t.me/farsna/440088" target="_blank">📅 17:49 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440087">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🎥
گوشه‌هایی از قدرت موشکی و پهپادی ایران که در بازدید سال ۱۴۰۲ رهبر شهید انقلاب از نیروی هوافضای سپاه به‌نمایش درآمد
🔸
بخشی از مستند «روزی که با تو بودم»، روایتی از دلدادگی مردم به رهبر شهید انقلاب @Farsna</div>
<div class="tg-footer">👁️ 7.81K · <a href="https://t.me/farsna/440087" target="_blank">📅 17:43 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440086">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb64ae0c52.mp4?token=Z5efArzxU5MacjR6ESXDZBf115nqaSX7MNqKCIwSsVbrmn_TC2RhBNL1Idt5g3Gl6SZHPVdjGAw8PnldTLxQi8V3XMJTla52-yU9Adqy81Ro5e38XZtAFEN1Gdt-E-U9dHFdxu1kVh5cCpHf-LkjPZQz9HJi6uZRCSfSdz9jYYnKZXz4svi-ap-ltB2MgL3lneVAbwxxsHKnszFr6QDdYkIxOBvnAbNQQ0ICOiFuUBZANp1LskByper-MTuHFRmzluitkaJpZ0V7nkDHkbGFQ4vGId7OOgfpsdD0ghLYPZideU3uekeYsSCiNDdByM34BGrDcEopjVpDJFt9U6ojwDuIICeHIWxvPfI30GISBLDbUtWcUtlGaTgTa0kPipak7Z8jy1LiVZgUMWlysziUxIwcq6vmEE5_cjD0oWyC2jJPNC6S5dKQvhHsvTaCbcLrOUSMUNGGQesf5Lmp2wF-9J6JHUvvWwHgL0VzifrB3lwscxqBxf4xQJXweUPQDMqfjsAFDIfiVV6jFEl88WaNdCO7FoPxlZUaXJ-bD0dAeJQPyNtcbXvfi2BaKDV8wqQSJiz7UrJeDAMU9lLMJj75nXTfVN5iFiKnG7BQhc0tC_kdpGS2y47tW0BekzEMmg5KjWLPYrr7rjDqRyhaFPiU_ii0jR-uYLE286HP3P9hr20" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb64ae0c52.mp4?token=Z5efArzxU5MacjR6ESXDZBf115nqaSX7MNqKCIwSsVbrmn_TC2RhBNL1Idt5g3Gl6SZHPVdjGAw8PnldTLxQi8V3XMJTla52-yU9Adqy81Ro5e38XZtAFEN1Gdt-E-U9dHFdxu1kVh5cCpHf-LkjPZQz9HJi6uZRCSfSdz9jYYnKZXz4svi-ap-ltB2MgL3lneVAbwxxsHKnszFr6QDdYkIxOBvnAbNQQ0ICOiFuUBZANp1LskByper-MTuHFRmzluitkaJpZ0V7nkDHkbGFQ4vGId7OOgfpsdD0ghLYPZideU3uekeYsSCiNDdByM34BGrDcEopjVpDJFt9U6ojwDuIICeHIWxvPfI30GISBLDbUtWcUtlGaTgTa0kPipak7Z8jy1LiVZgUMWlysziUxIwcq6vmEE5_cjD0oWyC2jJPNC6S5dKQvhHsvTaCbcLrOUSMUNGGQesf5Lmp2wF-9J6JHUvvWwHgL0VzifrB3lwscxqBxf4xQJXweUPQDMqfjsAFDIfiVV6jFEl88WaNdCO7FoPxlZUaXJ-bD0dAeJQPyNtcbXvfi2BaKDV8wqQSJiz7UrJeDAMU9lLMJj75nXTfVN5iFiKnG7BQhc0tC_kdpGS2y47tW0BekzEMmg5KjWLPYrr7rjDqRyhaFPiU_ii0jR-uYLE286HP3P9hr20" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دعای شهادت توسط رهبر شهید انقلاب برای حاج‌قاسم سلیمانی هنگام اعطای نشان ذوالفقار
🔸
بخشی از مستند «روزی که با تو بودم»، روایتی از دلدادگی مردم به رهبر شهید انقلاب @Farsna</div>
<div class="tg-footer">👁️ 7.46K · <a href="https://t.me/farsna/440086" target="_blank">📅 17:40 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440085">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🎥
نوشتم «تقدیم به خانواده شهید عزیز، آقای سیّدعلی خامنه‌ای!»
🔹
لحظاتی از دیدارهای صمیمانهٔ رهبر شهید انقلاب با خانواده شهدا در سفر سال ۱۳۸۴ به کرمان با همراهی شهید سلیمانی
🔸
بخشی از مستند «روزی که با تو بودم»، روایتی از دلدادگی مردم به رهبر شهید انقلاب @Farsna</div>
<div class="tg-footer">👁️ 6.89K · <a href="https://t.me/farsna/440085" target="_blank">📅 17:37 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440084">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🎥
«صدها مثل علی خامنه‌ای در راه این آبرو جانشان را میدهند»
🔹
روایتی از علاقه و محبت رهبر شهید انقلاب نسبت به امام خمینی(ره)
🔸
بخشی از مستند «روزی که با تو بودم»، روایتی از دلدادگی مردم به رهبر شهید انقلاب @Farsna</div>
<div class="tg-footer">👁️ 6.63K · <a href="https://t.me/farsna/440084" target="_blank">📅 17:32 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440083">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/afbac845cb.mp4?token=JUWYirO6XSFHedNCOKZ6zKNW3iOBqONOvSAb-Sx02ZKmR21Xsfm8QmKRF3AKO7Jav3Nd66obnSYYqM1V4ld4Zb02sbSrj5dtsgOXjF_uZuuMl-cn2Y_6cxCdTPH_D-yFuzHnPumBMwhQhhW4Vexzb5cm4i_qMEWkgCOubO1jhCo7y-iLmJYiJG-CN2cUIxNYBNpPbBHG3NIGYkodEIgs6JUA1QHamywVPr85Y2bKvegqQvjLUncOUhDjZzg8_e5XWNZgO0-PRhCw_1B0_iXnlu9Xf5unTP92vUoqzpcPxbPva8wMH9xBYpI34Od2bY-t_qSZTg7MKxl_MnSS8Lku8Tm5ipegwH7sRhKCbIxTDdFaU2rbCb78A1yvqVnDJMEITS-r85GyyTw-ZHdzkbKCGHOmgJgN-RYxG3XTGOhBVEefxwZt57cha1mvgpi7ByH24MSbyEObxFVky0-KsRAchI2M3hjIR1RCgDPll9xLmOy9mBX4Zx55gxonIu-8GaWdDCLWdC32PN0DTIxbmNrqGgGw-Cb1KgYs1wYexF9mAUNCxRL6tgqvK-BbdV2BPByZU9P377_OT1Z0TYVGvSAJDnMCWhclq2KBEQaj6HZVe-HW5yd_3qYe3Z6A55UufyUH1uJHO_YZ7cn8XU4HQA3CI2DcbyMMye8uIfz7GbqBlGI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/afbac845cb.mp4?token=JUWYirO6XSFHedNCOKZ6zKNW3iOBqONOvSAb-Sx02ZKmR21Xsfm8QmKRF3AKO7Jav3Nd66obnSYYqM1V4ld4Zb02sbSrj5dtsgOXjF_uZuuMl-cn2Y_6cxCdTPH_D-yFuzHnPumBMwhQhhW4Vexzb5cm4i_qMEWkgCOubO1jhCo7y-iLmJYiJG-CN2cUIxNYBNpPbBHG3NIGYkodEIgs6JUA1QHamywVPr85Y2bKvegqQvjLUncOUhDjZzg8_e5XWNZgO0-PRhCw_1B0_iXnlu9Xf5unTP92vUoqzpcPxbPva8wMH9xBYpI34Od2bY-t_qSZTg7MKxl_MnSS8Lku8Tm5ipegwH7sRhKCbIxTDdFaU2rbCb78A1yvqVnDJMEITS-r85GyyTw-ZHdzkbKCGHOmgJgN-RYxG3XTGOhBVEefxwZt57cha1mvgpi7ByH24MSbyEObxFVky0-KsRAchI2M3hjIR1RCgDPll9xLmOy9mBX4Zx55gxonIu-8GaWdDCLWdC32PN0DTIxbmNrqGgGw-Cb1KgYs1wYexF9mAUNCxRL6tgqvK-BbdV2BPByZU9P377_OT1Z0TYVGvSAJDnMCWhclq2KBEQaj6HZVe-HW5yd_3qYe3Z6A55UufyUH1uJHO_YZ7cn8XU4HQA3CI2DcbyMMye8uIfz7GbqBlGI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قوت قلب رزمندگان
🔹
لحظاتی از حضور رهبر شهید انقلاب با لباس سربازی در جبهه‌ها و ماجرای جمله‌ای که ایشان به امام خمینی(ره) گفتند و رضایتشان را برای حضور مجدد در جبهه‌ها گرفتند.
🔸
بخشی از مستند «روزی که با تو بودم»، روایتی از دلدادگی مردم به رهبر شهید انقلاب…</div>
<div class="tg-footer">👁️ 6.58K · <a href="https://t.me/farsna/440083" target="_blank">📅 17:22 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440082">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🎥
پزشک معالجم گفت: این دختربچه دست مجروح تو را خوب خواهد کرد!
🔹
اشاره رهبر شهید انقلاب به انس ایشان با شهید سیده‌بشری خامنه‌ای هنگام حضور نوروزی در منزل شهید آشوری در فروردین ۱۳۸۰
🔸
بخشی از مستند «روزی که با تو بودم»؛ روایتی از دلدادگی مردم به رهبر شهید انقلاب…</div>
<div class="tg-footer">👁️ 6.36K · <a href="https://t.me/farsna/440082" target="_blank">📅 17:20 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440081">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/42002b2f8a.mp4?token=EaJRL61g3iYnU8zqvyOLmArlgzwvAyMZCcugcEKyJE9wOqnJVDtplRtOttzdrH0aEB___mplBg6U4DkCbn301QcS3mxz-DGwJtLweaXLqoBOntDyDXe2M4mHciox-0g1jd2D8ClGZXhpzpKhojMApPyhI6cTHp1eZxlhQMAgp8VaoiCsJ6YBZncxe4Iej8VoSqK4UlekI9KPHDaCDaCFrZvDRDVYyJc9K0nDFQ5KDI8vzc6C0kJpNfdDn-WyG3rHgb_T6NRsod2C0FOShXjCknoVN-d5gCGiCM2X4t5YoMra8o34G6EAHZV-Do3KQveU1h9T2uxDkt_2qY0DxH_3m6sz8GInlxWp7locUwAHcqS2KeTnOb0LEUf8ZUOUzlW4Uz_r5RiMl_aQ5Ko4TBRQqJwMGscY1d_5i46YTiZQqdJh7qYAN8wvbOOmWMP3afq8RzCllCu28d7n8Usz2FA5lmjRTY9Ogqxtz5gWF8jReo-FOUpOxJUhL23yx1WAn4TaR7X95mR__Ay12wItP0brU5u71lgVnIUBMP9clOIN4-CLhuOzyu2WLjVYgBwSRLEc8C2IeqPJPiQKJXgSrCLAhPKxjeYDtWBeVaH9sDHgibYHDVAHN2xY8PpMrwqip5YWRfNs9k1mVJpTCgfp-3pvLBnEYcw8-FNMMnGapQkBK2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/42002b2f8a.mp4?token=EaJRL61g3iYnU8zqvyOLmArlgzwvAyMZCcugcEKyJE9wOqnJVDtplRtOttzdrH0aEB___mplBg6U4DkCbn301QcS3mxz-DGwJtLweaXLqoBOntDyDXe2M4mHciox-0g1jd2D8ClGZXhpzpKhojMApPyhI6cTHp1eZxlhQMAgp8VaoiCsJ6YBZncxe4Iej8VoSqK4UlekI9KPHDaCDaCFrZvDRDVYyJc9K0nDFQ5KDI8vzc6C0kJpNfdDn-WyG3rHgb_T6NRsod2C0FOShXjCknoVN-d5gCGiCM2X4t5YoMra8o34G6EAHZV-Do3KQveU1h9T2uxDkt_2qY0DxH_3m6sz8GInlxWp7locUwAHcqS2KeTnOb0LEUf8ZUOUzlW4Uz_r5RiMl_aQ5Ko4TBRQqJwMGscY1d_5i46YTiZQqdJh7qYAN8wvbOOmWMP3afq8RzCllCu28d7n8Usz2FA5lmjRTY9Ogqxtz5gWF8jReo-FOUpOxJUhL23yx1WAn4TaR7X95mR__Ay12wItP0brU5u71lgVnIUBMP9clOIN4-CLhuOzyu2WLjVYgBwSRLEc8C2IeqPJPiQKJXgSrCLAhPKxjeYDtWBeVaH9sDHgibYHDVAHN2xY8PpMrwqip5YWRfNs9k1mVJpTCgfp-3pvLBnEYcw8-FNMMnGapQkBK2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گوشه‌هایی از مراسم جشن تکلیف دختران در حضور رهبر شهید انقلاب
🔸
بخشی از مستند «روزی که با تو بودم»؛ روایتی از دلدادگی مردم به رهبر شهید انقلاب @Farsna</div>
<div class="tg-footer">👁️ 5.99K · <a href="https://t.me/farsna/440081" target="_blank">📅 17:17 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440080">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🎥
صل علی محمد بوی خمینی آمد...
🔸
بخشی از مستند «روزی که با تو بودم»، روایتی از دلدادگی مردم به رهبر شهید انقلاب @Farsna</div>
<div class="tg-footer">👁️ 5.86K · <a href="https://t.me/farsna/440080" target="_blank">📅 17:12 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440079">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6a2cb50bea.mp4?token=cTutA_I-OyEmOwrkIG2G9shoCsN_MUGRUN8NdcIXE4XDNR6ddvOKa1Hhxa8vPSDvPP8jBX5-GTWv5v3LleX5zK3EIlJoZvXsKbNA4lHtOXZwbGPm_MvyLYSYLZrNmm6FGxfHfBxWrA8-N8XTq37ApmhHDCntthJcnGjU-bRTr2zkPLyuuXDVpwiFIu0wVFHJKE1ezMNXQGJxyGmkIPPKwxtpbRZtOM8vk94EHO9cMkyg784hcnLtRFht9qNZQn_a4Ljhn2mCy-rABjZWfDQzgrmJPzhnvbSet6An4cJU9rao27Qhq8_dXYFea-mM-4w-zGqT8phdEGguE_z6MM5N7hUxTeSdQfvxAF7nQ7Zy4Muxa3q2tlOXJAikDMYki5g1HUpkTlwq8xNOvk6vyIeswht334LPWj_MFok4YkCVFsVzuR7QYpeMIaAsib4qys_cPWeoUub_ofAVnqdukMYitUqrKpAMAMiWTCEBQTf8itACa1EqOOoI3_8yJKVqsMkFbhC_dSc9KfnhZlNE1PhAGMEnvh3t4rR3qle029UQoXWLG0uji3utov6tD47yhkyeGBJd6gsY1nnjQ4agnTeqplVGCFW-gYnezIClp-GH1vCA9GAYqXvxRx6duXa7vV67WGzfqnw8rCwNC1LoU4M7VJDnXoG4BGcVNUimxeYdhmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a2cb50bea.mp4?token=cTutA_I-OyEmOwrkIG2G9shoCsN_MUGRUN8NdcIXE4XDNR6ddvOKa1Hhxa8vPSDvPP8jBX5-GTWv5v3LleX5zK3EIlJoZvXsKbNA4lHtOXZwbGPm_MvyLYSYLZrNmm6FGxfHfBxWrA8-N8XTq37ApmhHDCntthJcnGjU-bRTr2zkPLyuuXDVpwiFIu0wVFHJKE1ezMNXQGJxyGmkIPPKwxtpbRZtOM8vk94EHO9cMkyg784hcnLtRFht9qNZQn_a4Ljhn2mCy-rABjZWfDQzgrmJPzhnvbSet6An4cJU9rao27Qhq8_dXYFea-mM-4w-zGqT8phdEGguE_z6MM5N7hUxTeSdQfvxAF7nQ7Zy4Muxa3q2tlOXJAikDMYki5g1HUpkTlwq8xNOvk6vyIeswht334LPWj_MFok4YkCVFsVzuR7QYpeMIaAsib4qys_cPWeoUub_ofAVnqdukMYitUqrKpAMAMiWTCEBQTf8itACa1EqOOoI3_8yJKVqsMkFbhC_dSc9KfnhZlNE1PhAGMEnvh3t4rR3qle029UQoXWLG0uji3utov6tD47yhkyeGBJd6gsY1nnjQ4agnTeqplVGCFW-gYnezIClp-GH1vCA9GAYqXvxRx6duXa7vV67WGzfqnw8rCwNC1LoU4M7VJDnXoG4BGcVNUimxeYdhmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
به چادر ما نور آوردید...
🔹
گفت‌وگوی صمیمانهٔ رهبر شهید انقلاب با مردم زلزله‌زدهٔ سرپل‌ذهاب و تذکر ایشان به عکاسان و فیلمبردارانی که با کفش وارد چادر زلزله‌زدگان شده بودند.
🔸
بخشی از مستند «روزی که با تو بودم»، روایتی از دلدادگی مردم به رهبر شهید انقلاب @Farsna</div>
<div class="tg-footer">👁️ 6.01K · <a href="https://t.me/farsna/440079" target="_blank">📅 17:09 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440078">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🎥
لحظاتی از حضور رهبر شهید انقلاب در منطقه زلزله‌زدهٔ سرپل‌ذهاب با همراهی آیت‌آلله سیدمجتبی خامنه‌ای
🔸
بخشی از مستند «روزی که با تو بودم»، روایتی از دلدادگی مردم به رهبر شهید انقلاب @Farsna</div>
<div class="tg-footer">👁️ 6.23K · <a href="https://t.me/farsna/440078" target="_blank">📅 17:08 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440077">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/37ffa4d20a.mp4?token=P5d0UEEIf5p_244DR3S0uzShAsM3bWKW-sUfWNaiuJH3IYLyuZePCVm7kRsm7heQGQGNnSTuibCAfmsx4AlVuUM2dK_xuaHFW8k3x7H9nvjaWyf73FtSxwFpIwRplnmGJFmgEOGEzwJOQiq5XGuwACSPsa_pkxv7s9KYbv0ZS6ZXh9i-YKOwg1a5hL4BtKKTzFAs_3Cf6tJGfnS-0-JGW3N6VpgqYy7KhRun4NKsZteW0Co3ANq3BsYgLsWk5xjLc3TchytjK43N1wJMdTbubTsBS93xhydZ1E1uqfqD3Dvbd6NmNNm0IC0WAyKbPaOgeiZxGmz3W9PtSvjVDnWG-ozwdzjio0zHzYbiKSR6rnb8DeJwJv3RFWiz4t1JW9J9H8GbbPJEpOv5zts4OC-rlGVSHr20Fy3LVw3IfTt5X46FEjhg9b2gQtN8GUSvae90PgnKP27r7YAHD4TGnNtZC2CA0Z5hplSA8KkdpDvwXCATIr3MmuAoUfCVVIRVN3O19rX7zBcOj59kCmZSJjuII_BPxEVMQD-WaDhMHN-sBhe8f8FosUh8CNWqTHQVz8Npv-HyrHaePxSyaZGOfRZIW3QxJrQPEZMINzgfvI3fS8O79L9fEQEDXwRyWSRW2OcbBsKP_HIndBQrwQK8ULKUuwUjV3OmX_BrzsunF4iBPk8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/37ffa4d20a.mp4?token=P5d0UEEIf5p_244DR3S0uzShAsM3bWKW-sUfWNaiuJH3IYLyuZePCVm7kRsm7heQGQGNnSTuibCAfmsx4AlVuUM2dK_xuaHFW8k3x7H9nvjaWyf73FtSxwFpIwRplnmGJFmgEOGEzwJOQiq5XGuwACSPsa_pkxv7s9KYbv0ZS6ZXh9i-YKOwg1a5hL4BtKKTzFAs_3Cf6tJGfnS-0-JGW3N6VpgqYy7KhRun4NKsZteW0Co3ANq3BsYgLsWk5xjLc3TchytjK43N1wJMdTbubTsBS93xhydZ1E1uqfqD3Dvbd6NmNNm0IC0WAyKbPaOgeiZxGmz3W9PtSvjVDnWG-ozwdzjio0zHzYbiKSR6rnb8DeJwJv3RFWiz4t1JW9J9H8GbbPJEpOv5zts4OC-rlGVSHr20Fy3LVw3IfTt5X46FEjhg9b2gQtN8GUSvae90PgnKP27r7YAHD4TGnNtZC2CA0Z5hplSA8KkdpDvwXCATIr3MmuAoUfCVVIRVN3O19rX7zBcOj59kCmZSJjuII_BPxEVMQD-WaDhMHN-sBhe8f8FosUh8CNWqTHQVz8Npv-HyrHaePxSyaZGOfRZIW3QxJrQPEZMINzgfvI3fS8O79L9fEQEDXwRyWSRW2OcbBsKP_HIndBQrwQK8ULKUuwUjV3OmX_BrzsunF4iBPk8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
لحظاتی از حضور رهبر شهید انقلاب در منطقه زلزله‌زدهٔ سرپل‌ذهاب با همراهی آیت‌آلله سیدمجتبی خامنه‌ای
🔸
بخشی از مستند «روزی که با تو بودم»، روایتی از دلدادگی مردم به رهبر شهید انقلاب
@Farsna</div>
<div class="tg-footer">👁️ 6.27K · <a href="https://t.me/farsna/440077" target="_blank">📅 17:03 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440076">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c972cadd0.mp4?token=sMaonv01NVCfs_fwdIrFm7ILMChfLIC9WNU-eI4Uhop-R8Wk5WMS9LNLUacvoYevZzZdw8LC3_ZGmO2nirJpyidse5RegXlAHyr0yOWDAEOtKiSXHjZgIbg7PBbGti_klW3mJ6slYNI0_-c6p3yHA0R8r5GkLOySOFU3f9-P9W3ySISQKQ_cPJseyzU6iAr8S9EEn7f-WlU4zdNZTPEN4z7yyDbxEl6k88YD0qHn-G7FVKOxzN8lFdRgu99uSm-cSIvWFAlNQMDkGR-NAMKlApUfTvzg_vFTpaBG9tK9CxivWM9TkjWrCo3Y_-yc4Ml17gJBsDbXLGi6evKEcYUwug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c972cadd0.mp4?token=sMaonv01NVCfs_fwdIrFm7ILMChfLIC9WNU-eI4Uhop-R8Wk5WMS9LNLUacvoYevZzZdw8LC3_ZGmO2nirJpyidse5RegXlAHyr0yOWDAEOtKiSXHjZgIbg7PBbGti_klW3mJ6slYNI0_-c6p3yHA0R8r5GkLOySOFU3f9-P9W3ySISQKQ_cPJseyzU6iAr8S9EEn7f-WlU4zdNZTPEN4z7yyDbxEl6k88YD0qHn-G7FVKOxzN8lFdRgu99uSm-cSIvWFAlNQMDkGR-NAMKlApUfTvzg_vFTpaBG9tK9CxivWM9TkjWrCo3Y_-yc4Ml17gJBsDbXLGi6evKEcYUwug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
لیلاز، اقتصاددان اصلاح‌طلب: تا زنده هستم قلبم در غم ازدست‌دادن رهبر شهید مجروح است.
@Farsna</div>
<div class="tg-footer">👁️ 6.53K · <a href="https://t.me/farsna/440076" target="_blank">📅 16:58 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440075">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b4ac7e16c0.mp4?token=a7eEz2sLP23euBnWhJuSE0CrwARYyKHcgZC7DmNOglFbFwafC5kXkWcB2Ipnb1PEGs6Omqow0sRO0VSSu7h5Hv4w_V0bxr6_aZPQ-dqYyauNYEvKuvbH3Cva8pMm3RjZ5TQwlKeO6JLXnwWDfkrPtnrHJvEbTZPyxluPhPCWJgNMpRi3E-vbCYpV8ID2Si69HlDWqV5fZQAWR05yyJXW4jcYstbgeG2C69J8F7lB52MWMoA-dkQEz_RWIyQzRNef5lP7NoR7kX3KfCA64JsRWZjIHhjQTupEFYu4N5rRd_icrqhVztSOkM0HM_ToBbACF4sYxtwdF4F4UI0DMh8PxiHplxIbJ0LeUpEXoAB2dpaWtQFo2-ioo7bolRp7F1laluhXaPay_azDF79km_WMtG0LDEX4ucK0KNa0c_EvVj6Z8PYl3tIu_nIDlZtXKmMZN63f86xy8R2CJSVg1g3rEr_TWLMlvuIXWP0ZmHXPIGeOM9TFIr75W2pJdXR-89QzdnR9ybsep_3OulO80CV37_kfoxx8n3wlEbT6V1UoUBEnx0l-qB1S6fJckT62ovw6icrSPIzGPYroPvSVm2lqD0-jOwX8z764USFaL_x6mxzDTlTpxDa51ov9no8dFX1ISu-FUOC2fpL29Old03RhExFLVZUVrSCToVl5dUxc4wk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b4ac7e16c0.mp4?token=a7eEz2sLP23euBnWhJuSE0CrwARYyKHcgZC7DmNOglFbFwafC5kXkWcB2Ipnb1PEGs6Omqow0sRO0VSSu7h5Hv4w_V0bxr6_aZPQ-dqYyauNYEvKuvbH3Cva8pMm3RjZ5TQwlKeO6JLXnwWDfkrPtnrHJvEbTZPyxluPhPCWJgNMpRi3E-vbCYpV8ID2Si69HlDWqV5fZQAWR05yyJXW4jcYstbgeG2C69J8F7lB52MWMoA-dkQEz_RWIyQzRNef5lP7NoR7kX3KfCA64JsRWZjIHhjQTupEFYu4N5rRd_icrqhVztSOkM0HM_ToBbACF4sYxtwdF4F4UI0DMh8PxiHplxIbJ0LeUpEXoAB2dpaWtQFo2-ioo7bolRp7F1laluhXaPay_azDF79km_WMtG0LDEX4ucK0KNa0c_EvVj6Z8PYl3tIu_nIDlZtXKmMZN63f86xy8R2CJSVg1g3rEr_TWLMlvuIXWP0ZmHXPIGeOM9TFIr75W2pJdXR-89QzdnR9ybsep_3OulO80CV37_kfoxx8n3wlEbT6V1UoUBEnx0l-qB1S6fJckT62ovw6icrSPIzGPYroPvSVm2lqD0-jOwX8z764USFaL_x6mxzDTlTpxDa51ov9no8dFX1ISu-FUOC2fpL29Old03RhExFLVZUVrSCToVl5dUxc4wk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
استاد دانشگاه: هزینه‌های تأمین امنیت تنگه هرمز باید جبران شود
🔹
عسکر اسماعیلیان عضو هیئت علمی دانشگاه: ایران به دلیل مسئولیت در تأمین امنیت، ایمنی و مدیریت تردد دریایی در تنگه هرمز، ناچار به اجرای تدابیر کنترلی و صرف هزینه‌های مختلف است.
🔹
منطقی است که…</div>
<div class="tg-footer">👁️ 7.67K · <a href="https://t.me/farsna/440075" target="_blank">📅 16:48 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440074">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromسیاسی خبرگزاری فارس</strong></div>
<div class="tg-text">🎥
استاد دانشگاه: هزینه‌های تأمین امنیت تنگه هرمز باید جبران شود
🔹
عسکر اسماعیلیان عضو هیئت علمی دانشگاه: ایران به دلیل مسئولیت در تأمین امنیت، ایمنی و مدیریت تردد دریایی در تنگه هرمز، ناچار به اجرای تدابیر کنترلی و صرف هزینه‌های مختلف است.
🔹
منطقی است که برای جبران این هزینه‌ها سازوکارهایی مانند دریافت عوارض یا ارائه خدمات تخصصی دریایی به کشتی‌های عبوری در نظر گرفته شود.
🔹
اجرای چنین طرحی نیازمند تدوین چارچوب‌های حقوقی شفاف، قواعد اجرایی مشخص و ارائه خدمات مناسب در قبال دریافت هزینه‌ها است.
🔹
هدف نهایی از این اقدامات، افزایش امنیت و ایمنی تردد دریایی در تنگه هرمز عنوان شده است.
@Farspolitics</div>
<div class="tg-footer">👁️ 6.72K · <a href="https://t.me/farsna/440074" target="_blank">📅 16:44 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440073">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f5c520b46.mp4?token=FTHB5ERbJTcsZIpw7DkqxBIh-WpDN8_tSSjaNpnyZpL59INHTga1BhG8tySf-8UcwzSIQJmSWrKkmuUoe_9_xTDVscRCpNocBLX2MMEStDUc22DJAWp7e_9MNF04DaFOYyYGvQk9mFRGg8KZzkvVVp754xz8kENMtsFxuQKCSWOqVG1HIOgmRrbbmTNaUaOoIYn9AVvWJl-NArlRJQXPMlE3S5KnezawrJ1J7wVT0XRK-hLZb9-iygiNIJbmsnq8G6lF2TZtYFg4KGAlCa1948bHWNFUePb3_vUAfEEs6JhBCea7oXGsHHJVbMXfoqdxk0WAdI7DfbFAYWWHLheXHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f5c520b46.mp4?token=FTHB5ERbJTcsZIpw7DkqxBIh-WpDN8_tSSjaNpnyZpL59INHTga1BhG8tySf-8UcwzSIQJmSWrKkmuUoe_9_xTDVscRCpNocBLX2MMEStDUc22DJAWp7e_9MNF04DaFOYyYGvQk9mFRGg8KZzkvVVp754xz8kENMtsFxuQKCSWOqVG1HIOgmRrbbmTNaUaOoIYn9AVvWJl-NArlRJQXPMlE3S5KnezawrJ1J7wVT0XRK-hLZb9-iygiNIJbmsnq8G6lF2TZtYFg4KGAlCa1948bHWNFUePb3_vUAfEEs6JhBCea7oXGsHHJVbMXfoqdxk0WAdI7DfbFAYWWHLheXHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تانک‌های صهیونیست‌ها همچنان شکار ابابیل حزب‌الله است
@Farsna</div>
<div class="tg-footer">👁️ 7.41K · <a href="https://t.me/farsna/440073" target="_blank">📅 16:27 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440072">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4d40dbeba5.mp4?token=vvzqxuo4lsKLdfVBVxH738xMV5F5hbwKItp4nIXRTl5-6U-mBDXY-Hr2mhjl7ptk2Q-IRskmAqxfp591j-Fkp6L12C7WHdk68YaFGHHJkwkcVxC-HaNC6CKoXg87wS4e6I1r4KY8ogCn1fCK-oWUHM-CUBltuIZfy4lXdi9hXec-r6-4Xd2Alx7GqSxKMuTuSXLonzPvKxKx8z0J9MWyZQnFvFhlbVS-gM9OVjHlwfTz9l2yocnRJu37kR74Fq3f2GONj775n_1NTMT0gH6OgZwzeVeYSQEmh2-duNdHXE9DZzXHVY24xjYGXSo0lBI-hal9qFQatzvGfm_sAoKo3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4d40dbeba5.mp4?token=vvzqxuo4lsKLdfVBVxH738xMV5F5hbwKItp4nIXRTl5-6U-mBDXY-Hr2mhjl7ptk2Q-IRskmAqxfp591j-Fkp6L12C7WHdk68YaFGHHJkwkcVxC-HaNC6CKoXg87wS4e6I1r4KY8ogCn1fCK-oWUHM-CUBltuIZfy4lXdi9hXec-r6-4Xd2Alx7GqSxKMuTuSXLonzPvKxKx8z0J9MWyZQnFvFhlbVS-gM9OVjHlwfTz9l2yocnRJu37kR74Fq3f2GONj775n_1NTMT0gH6OgZwzeVeYSQEmh2-duNdHXE9DZzXHVY24xjYGXSo0lBI-hal9qFQatzvGfm_sAoKo3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نصب کتیبه‌های ولادت امام موسی‌بن‌جعفر(ع) در حرم رضوی
@Farsna</div>
<div class="tg-footer">👁️ 8.4K · <a href="https://t.me/farsna/440072" target="_blank">📅 15:54 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440071">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7b40f8bd30.mp4?token=bW96bQZepqYJyFoGJfux2acOzrBl14JOL0zbMEFrTaWN3dtUJZSU3GNwk-GrX5H6t7lCIyQBMZbDFXmEBF5AbeYzmHID1g29J93l2rX6dly6EQX_wJxwpsgV0yvcUiR8HMryllqkQQYOlAA0iZ5GALVc_pfPNy2Fky6LqcgKqG8on5b1jbumfhYBatW2Vj_sZZaeHZJfXgK351sB6anmoi9JBvwMdmTAoR5W1H9lCxMfRzxmzLF7ryprrv1zWYSLLTzWdy87mLgunLB6kx4OAN2VLdFyq21GXYg33xhtvR5ktuE5F96X0oVQ-P-3zHnA2X3MJYDJn7Okb0OqHdKXoBIjnOJ1CeBlOlBT_NVaRaLOtm8b8z49qLFRpjAAbZEtT45HF_alvi2oaeWH1x05PJmuhzzqEsIqAEiXtlDVVmIyszLMzJE1o163rhDBafqZsyYXlGNEj1jeWIZ-rpSWuBRQWaCUS5FljEQZVZMwNcd_kUkqFTD0f4Mvn_HSzH8-aRn_HCe-U_iYoU7zeA-DnQH1desw8OaQndgyI2ZCUezisufF0GFW2wpl-MExLtjqcu4VE0_bSI6qisY6vMeLsL_bq8tfJ5XPJKZtZO3TjHFZ6DIF28jF6hBASQK-wO8p_04PMA2vMfS7Jw5J4YzDQmvyl2roTPjZyc8in61oPoo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7b40f8bd30.mp4?token=bW96bQZepqYJyFoGJfux2acOzrBl14JOL0zbMEFrTaWN3dtUJZSU3GNwk-GrX5H6t7lCIyQBMZbDFXmEBF5AbeYzmHID1g29J93l2rX6dly6EQX_wJxwpsgV0yvcUiR8HMryllqkQQYOlAA0iZ5GALVc_pfPNy2Fky6LqcgKqG8on5b1jbumfhYBatW2Vj_sZZaeHZJfXgK351sB6anmoi9JBvwMdmTAoR5W1H9lCxMfRzxmzLF7ryprrv1zWYSLLTzWdy87mLgunLB6kx4OAN2VLdFyq21GXYg33xhtvR5ktuE5F96X0oVQ-P-3zHnA2X3MJYDJn7Okb0OqHdKXoBIjnOJ1CeBlOlBT_NVaRaLOtm8b8z49qLFRpjAAbZEtT45HF_alvi2oaeWH1x05PJmuhzzqEsIqAEiXtlDVVmIyszLMzJE1o163rhDBafqZsyYXlGNEj1jeWIZ-rpSWuBRQWaCUS5FljEQZVZMwNcd_kUkqFTD0f4Mvn_HSzH8-aRn_HCe-U_iYoU7zeA-DnQH1desw8OaQndgyI2ZCUezisufF0GFW2wpl-MExLtjqcu4VE0_bSI6qisY6vMeLsL_bq8tfJ5XPJKZtZO3TjHFZ6DIF28jF6hBASQK-wO8p_04PMA2vMfS7Jw5J4YzDQmvyl2roTPjZyc8in61oPoo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
شلیک اخطار موشکی-پهپادی نداجا به‌سمت ناوشکن‌های متجاوز و مزاحم آمریکایی
🔹
روابط‌عمومی ارتش: در ادامه عملیات مقابله با شرارت ها و مزاحمت‌های دریایی و ربایش شناورهای تجاری و نفت کش توسط نیروی دریایی ارتش تروریستی آمریکا،  پس از شلیک‌های اخطارِ موشک قدیر و…</div>
<div class="tg-footer">👁️ 8.89K · <a href="https://t.me/farsna/440071" target="_blank">📅 15:22 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440070">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f396a4ff6.mp4?token=f28htpfm12LseqFLT3s78SDvOH0Zj0o4k_YlMKMi4IJIFd4lzbFr5oc4oWlSkdiLuZsBJWmQEme24YbaZUP3MVk53UJlbu2l3BBbwCIn-ORaiu4OooI8i9NZPRoG2iergT1Bpn2RblVRRMCI1sEsjskemMXGOLe5RcyzeD4k4mJHNgxVAIDZV2tmX0sxcKRHC_AzlQEHIv6W0CK996JksTRh6kE3TcuqvAUM_4qZRkHeeEBozMbBn7qR-ppScfAcGbylCDwmqydggmnTW_mZ6hfWkn--qR9dYlRongGprbInmblqb_hB6BEesltPQg6jqO-D2WrgjxVAYilwvIQK1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f396a4ff6.mp4?token=f28htpfm12LseqFLT3s78SDvOH0Zj0o4k_YlMKMi4IJIFd4lzbFr5oc4oWlSkdiLuZsBJWmQEme24YbaZUP3MVk53UJlbu2l3BBbwCIn-ORaiu4OooI8i9NZPRoG2iergT1Bpn2RblVRRMCI1sEsjskemMXGOLe5RcyzeD4k4mJHNgxVAIDZV2tmX0sxcKRHC_AzlQEHIv6W0CK996JksTRh6kE3TcuqvAUM_4qZRkHeeEBozMbBn7qR-ppScfAcGbylCDwmqydggmnTW_mZ6hfWkn--qR9dYlRongGprbInmblqb_hB6BEesltPQg6jqO-D2WrgjxVAYilwvIQK1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
شلیک اخطار موشکی-پهپادی نداجا به‌سمت ناوشکن‌های متجاوز و مزاحم آمریکایی
🔹
روابط‌عمومی ارتش: در ادامه عملیات مقابله با شرارت ها و مزاحمت‌های دریایی و ربایش شناورهای تجاری و نفت کش توسط نیروی دریایی ارتش تروریستی آمریکا،  پس از شلیک‌های اخطارِ موشک قدیر و پهپادهای تهاجمی جدید شهید دانای نیروی دریایی ارتش جمهوری اسلامی ایران، ناوشکن‌های متجاوز DDG_103 و DDG_87 ،دریای عمان را به‌سمت اقیانوس هند ترک کردند.
🔹
به‌دنبال این عملیات و عملیات‌های روزهای گذشته، علاوه‌بر ناوشکن‌های دشمن آمریکایی صهیونی که در قالب ناوگروه جرج دبلیو بوش و مرکز فرماندهی نیروی دریایی تروریستی این کشور به‌عنوان عامل مزاحمت‌ها و اختلال در تجارت و امنیت دریایی منطقه بودند، ناوبالگرد بر  ِتهاجمی آبخاکیِ تریپولی نیز مجبور به ترک دریای عمان شده است.
🔹
مرکز فرماندهی و کنترل عملیات نیروی دریایی ارتش ضمن تاکید بر لزوم دست برداشتن دشمن آمریکایی صهیونی از دزدی و شرارت دریایی، تاکید کرد: با وجود گسترش و دور شدن ناوهای دشمن از تیررس موشک‌های استفاده‌شده، در صورت نیاز، موشک‌های این نیرو با برد بیشتر مورد استفاده قرار خواهد گرفت.
@Farsna</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/440070" target="_blank">📅 15:10 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440062">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JA8rB4Q7sGG7rvGNDzsn4FPzJeQS8ly8xCQ5IDKKB6IXIDbgOrlXvEzyAlqyfBnNFV1BZNzHpYoiQ5W78SKpoXRN5m1fFt-h8vO2xwkWNPW4swA5QicOzXBsgFP_kJptzfvYs6CGfDojxjFscTNHac20xf6JvnQ9lRbikhc8FeiypGMf46tkLLjUa2Q8wB8BEbX0PPsrcfVLS4HgSeppZwdRK5qamYqnBmnw8Sw3cr0MooI-1ywuedp0V1gMultt2Rdeul_T7BzQ2iC6Nt9DZPFQNtbFeM07vf15jdexycDnrId1W2Ddg_wg-aOsYQIfSPvfyzT7wp7rk_ym3rZpFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/s6e1VtOwxYcGhcq7ewhrMqhmJ4PO2Azt0m_XCYOfxgNZpRZfttQaTAzfWvPTYIKqqpQ3PUnscM6D7mccue7DfrFTEUBFp1wLfHUGywxyhfmJH4Eb4cY-cqk3klzG28-47scsgY_zLSzTjk6aBoFbybbjydhxgxQev6gBK_Hdy-H4dqgNgQ5lfnpFVvURj2al9rUyi3XRAwGbD9IwBbHnC2riT8eJcRUMQqDe5amrI2E3_JvBBF22fFKCUOabc3Z77h9TJe-bl1lOrr0bo81uANBrPe5YN4k8LDnOl1BmJC_jJUNmS-duulCbRM2Q-tOzpMprElSatLNd5HSPzNsnuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RJAOkGQHq2Hpwwodk9E7jnh6qElXTwetzLq5CURApXMtzUBsaI4iNgScE6aKKa2e2eNt6DpcCtI2TEdMhv_Mpw8z9Pj--3aaCqcNFijCx8tp-HiUgasd1nD3h4CrThoa9vg5uhppAy-KOKz89gI3i5vspQGyKMOi2yrou5spNVZ8GwBaPnTO0Jz5Ym4If56O_Tv-PfrHH_aXj3xr1HfF5VVLQ1kqVtdqiRx3TIM1npdDtMHhR4gflD-Spq9yRAlpsYfB8r9houds6ZlYJA3Dnik_cyCU-mVFpUBIdg7J-HrFc2Zvaow8uXUaO6vrZ5U-yjbc2MIxU6FHEfdhKYGLtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cOLE8gsr_hgfRJoXArFJf0DoElGFwRlc1xL7Sd2q81vYbXnb4gVZgVAQPvOvtrT_QunZ0jMOc8UvG5Oz9s9UaSwUk9lsdAS2TuHtz9tdb5f5ewyvNYLcPifFaJTzz5Df34siEihR6roLt-u6c8B_wcSNrIikjUB-VBNz8zKKnsF_RLItrFykz98qTRfJVxjZ-OTqEOFMU5q1RF6FHgBSfhKsZIGH0otYJgtKaO7E-SzYSJ6TNHoWZIS9ODc7VX001HQrodZEA1_Fo5liJqIJcfZViUKtUh2zpTel74BmwVCU9VTYcmEk7UPsHRMnfE2kwwXtc2gP87dTlHo5WMtOvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tDS5ujLRDFYzBXijKkjLL_vxu1S3aU0iBswqpEJnvdnaVyi4GI6wEP6mrXsgSnCvtoGHYB4ey_eVJutpwXpW-GnC6AqNOw8yhADc0Bieoz23eS5QvzfO0t5578pZPC16peIB4TMkC18SLEsyq4HyyABAyQ6U0uD0vKIT80Qt_oSk1NB_6u14r106GOt06VmYYf0s0OtS8mNInX-hSbHJuHzr12ACVnMfpbHpUwiR6E8UnCE4DKoh8aQO22eoZhEkG2Nr70iKJVc045qnHVBt64F-wasaJhRKTczwFb7ev3j-ZHXmspQ2h6SU3BCD4YoFX22vmfTOgC8ntX61tQEiVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JN6CV65cA0BvpJK9NPIodSMwpRQccZFSyK5d-46CzPAgtGPCG2HAVnnlVnftPnfBmlHXozaQLtsOcxLeu9x1ZWbmQPC61nPewMRzXAW4sRX2wWqfmf8dkQ1oAFMbDgXzAvTCmhrWEKVWmG06zTbFrwFpyN_632KiFi8Y74BUWb9yk0f31Zh5Iy80IY2cuFdf40nUqSQBhB1MZWbbDlf1-f9f9jeUegL5vAgVzofzqaYIJ_Sb_VJ6Lsmb6JZ0xV_z7C9invgkZMgd0oZ0xlA75DeVg60IShBkDdFc7t4yvru3fGIz9QHCmbwQgUEtYcJHOPvtAMiDmXbJTPzNURtlCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/G4xdD34AaTn8A-B6_bxG90gA2HMGGrEn5RBjtuRlS8GPZIkr0QWl9sYkzh7pEl2otCl9T-o2e3RP0EH7oO5H-DNDisbgb_lAxIVf6qABcWUKCjJpEqOav_LfxVcUR3k37Z7gywixt42MnOzwJA9mlzn8mPLmMJ1UweQrMr2s-s2CTi9u4WLDW3lUb3OECq96oFY6p9HTAM9dcsVbS8Uifgaer9FeFWpoCufSgeU-X33Rd73yIuRLw6BtVTEIYR1KNUkoxDEFMsXnhrWq7Qqp5ibgcDJsAHzL4Y8g7-vg0YAi_-4xPdhGktfzXCM47RGR5AqRa-tzfhvgvlTAJvc2Sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PlzKBPTd6FgZMuWBMlDKoRE9GGhYOF3HAPV7KapuQqII5pl1C7HNCtB_oDV2Cce92opkjY9ap0f9uOTWjgdtcOhqtQ38yRUFm841nHAo8E56-8sG4IIY7P04rYjHtEQCoDFGR6JuFnqooKkGWa5277V0kUGZrppibNx6GXVdin_nYppYkFRjW02Skx5FcKP7cxyMY0hPo2FldtuynLwyUNy4T2Sn1oYwyLDgjGlstVTaTSycxf4TaFInuZRg9WhtLK44cGpSbVWVkDcKXf0UT8X8CBA6zKklfkfBr3d3AovaKjWsfKcmbemKXCvrZ_y3MoOAdQBnf9-Yv5hhxV--9g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
دیدار حدادعادل با خانواده شهیدان خاجی و صاحبدل از همراهان دیرین رهبر شهید انقلاب
🔹
غلامعلی حدادعادل، حسن خجسته، اعضای دفتر حفظ و نشر آثار رهبر شهید انقلاب همراه با جمعی از اهالی و اصحاب رسانه با حضور در منزل شهیدان سعید صاحبدل و اکبر خاجی یاران و همراهان دیرین رهبر شهید انقلاب به مقام این شهیدان والا مقام و خانواده معزز ایشان ادای احترام کردند.
🔸
شهیدان سعید صاحبدل و اکبرخاجی همراه با رهبر شهید انقلاب، در اولین روز جنگ رمضان در اثر حمله آمریکایی صهیونیستی به شهادت رسیدند.
🔸
پویش «اول خانواده شهدا» به دعوت رهبر انقلاب، حضرت آیت‌الله سیدمجتبی خامنه‌ای، با هدف دیدار و تکریم خانواده‌های معظم شهدا شکل گرفته است. ایشان در پیام نوروزی سال ۱۴۰۵ تأکید کردند: «مردم هر محله، دیدارهای سال نو خود را با تکریم شهدای همان محل آغاز کنند.»
@Farsna</div>
<div class="tg-footer">👁️ 9.49K · <a href="https://t.me/farsna/440062" target="_blank">📅 15:09 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440060">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🔴
منبع ایرانی: ادعای العربیه دربارهٔ موافقت تهران با انتقال ذخایر اورانیوم به کشور ثالث صحت ندارد
🔹
یک منبع آگاه نزدیک به تیم مذاکره‌کنندهٔ ایران روز جمعه گزارش رسانهٔ‌ سعودی مبنی‌بر موافقت تهران با انتقال بخشی از ذخایر اورانیوم غنی‌شده خود به یک کشور ثالث را رد کرد و آن را نادرست خواند.
🔹
شبکهٔ العربیه پیش‌تر گزارش داده بود که ایران به‌طور رسمی با انتقال بخشی از ذخایر اورانیوم خود به کشوری ثالث که مورد توافق طرفین باشد، موافقت کرده است.
🔹
این منبع به خبرنگار سیاسی خبرگزاری فارس گفت: موضوعات مرتبط با پروندهٔ هسته‌ای در مرحلهٔ کنونی مذاکرات مطرح نیست و بررسی آنها به مراحل بعدی گفت‌وگوها موکول شده است.
🔹
وی افزود: «موضوع انتقال ذخایر اورانیوم در دستور کار فعلی مذاکرات قرار ندارد و ابتدا باید طرف آمریکایی اقدامات مشخص و قطعی خود را انجام دهد و دربارهٔ برخی مسائل اساسی به توافق‌های روشن و نهایی دست یابیم.»
🔹
این منبع تأکید کرد که گزارش منتشرشده دربارهٔ موافقت ایران با انتقال بخشی از ذخایر اورانیوم به یک کشور ثالث «نادرست» است.
🔸
مذاکرات میان ایران و آمریکا با هدف رسیدن به یک تفاهمنامهٔ ترک تخاصم و آغاز مذاکرات ۶۰ روزه، پس از حملات آمریکا به چند کشتی‌ تجاری در جنوب ایران و تهاجم ارتش رژیم صهیونیستی به جنوب لبنان متوقف شده است.
@Farsna</div>
<div class="tg-footer">👁️ 9.79K · <a href="https://t.me/farsna/440060" target="_blank">📅 14:54 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440059">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd0679961e.mp4?token=GUf9Mrif8SHpqIyieS0Pfdpucb-ez8HH88Ug7rL0PovCV_aMGtdOvhmfasXoeSOthFes85SDLO51T0ViPXyGzQ00pr9lewg6gxnQNSyManeqg3VajXiY_XjrMOvEH3CyWr6Z8je-Mpn20c4StHdbl03vhcqQ1qA4pFb82DKneMEimWrhURwhmCtltwJE96jZYXwRBTpGZXwczgyWdFnXGJguOfL5xw2GSVT36mf2tZj9YKPKZiXGlBEj3G3kKyXpFuj7oG3rAcWxzYo4AoFjRADzygPmxSaOC14HQmFdm27quoukuHRxmKTU9QSWNaif2SBN38MxZLCYwEsF8sz1-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd0679961e.mp4?token=GUf9Mrif8SHpqIyieS0Pfdpucb-ez8HH88Ug7rL0PovCV_aMGtdOvhmfasXoeSOthFes85SDLO51T0ViPXyGzQ00pr9lewg6gxnQNSyManeqg3VajXiY_XjrMOvEH3CyWr6Z8je-Mpn20c4StHdbl03vhcqQ1qA4pFb82DKneMEimWrhURwhmCtltwJE96jZYXwRBTpGZXwczgyWdFnXGJguOfL5xw2GSVT36mf2tZj9YKPKZiXGlBEj3G3kKyXpFuj7oG3rAcWxzYo4AoFjRADzygPmxSaOC14HQmFdm27quoukuHRxmKTU9QSWNaif2SBN38MxZLCYwEsF8sz1-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بارش باران و وزش باد شدید در تهران
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.42K · <a href="https://t.me/farsna/440059" target="_blank">📅 14:47 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440058">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c1e0870945.mp4?token=Lf9viECH-hhSRh2-shWdH3tzKT-53Q92CvxC88s0F13099CiBrDXMgeqPDvgJlAbiZMlSxrO7kgfh8mL_zeTyidVZuP_Wdp5CuFnSEGcudojnwTUWE2n5_iCu_Ar-OPNKfZAPumKVH-bDAZ6HaQXSSLBTKfjn4DnfBwqI8MmuvkwNLYVt-mdoS_VCmrFai6_Mnex2oYqwDfLZxjBeYlefJn8c2D8irSNxDhMt-0g3cHGjNZ59iSP3ywvVDgjxeHnSGNnAJLw8UizicEsFhyB3AGE4FHev6Jp4Eljo_J-uRvTvw5g9Z8jWKkJOpf3ZZWFAASGLmvu3S3Fo3KDO5j4Dg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c1e0870945.mp4?token=Lf9viECH-hhSRh2-shWdH3tzKT-53Q92CvxC88s0F13099CiBrDXMgeqPDvgJlAbiZMlSxrO7kgfh8mL_zeTyidVZuP_Wdp5CuFnSEGcudojnwTUWE2n5_iCu_Ar-OPNKfZAPumKVH-bDAZ6HaQXSSLBTKfjn4DnfBwqI8MmuvkwNLYVt-mdoS_VCmrFai6_Mnex2oYqwDfLZxjBeYlefJn8c2D8irSNxDhMt-0g3cHGjNZ59iSP3ywvVDgjxeHnSGNnAJLw8UizicEsFhyB3AGE4FHev6Jp4Eljo_J-uRvTvw5g9Z8jWKkJOpf3ZZWFAASGLmvu3S3Fo3KDO5j4Dg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تجمع خودروهای نظامی رژیم صهیونی هدف حملات حزب‌الله شد
@Farsna</div>
<div class="tg-footer">👁️ 9.01K · <a href="https://t.me/farsna/440058" target="_blank">📅 14:40 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440057">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rMMeymvs4vBzFcG8DXBBhS_M4K0TGBvUmnv_WUgU1OGGwpb90EB-6bkJezdLO04CZ46teYBDHgb1h19_Ut5vqAHSig642MEcrFYofiPkggRoGtsUOlVSsUCjzFDcxlM8W6S7QvrhUITICjUy3iy9umS6erwO1K_-LOMj2uGDZGwKUzYtdAYkjtqXBoh0d9-RmTqkoc3geCxKn7w9mcU9-Shm_j6CyX0SjOs5xvbdwzc6Ngfy6n4JwR5a37Hs4DrtX-4zlq__VXWCXVjjICsdyXbZ2AD_Ow0iWAahd8ORnTStZ6rIhCjJfF3lyUIAA-_eHBWGpOhDHKF5h0pdjWpv3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان ملل: جنگ علیه ایران میلیون‌ها نفر را در
معرض گرسنگی حاد قرار داده است
🔹
برنامه جهانی غذا: پیامدهای جنگ علیه ایران بر امنیت غذایی جهان در حال نمایان‌شدن است و میلیون‌ها نفر در کشورهای آسیب‌پذیر برای تأمین نیازهای اولیه غذایی خود با مشکل روبه‌رو شده‌اند.
🔹
در صورت ادامهٔ درگیری‌ها در خاورمیانه و افزایش قیمت نفت درپی وضعیت تنگهٔ هرمز، ۴۵ میلیون نفر ممکن است با ناامنی حاد غذایی روبه‌رو شوند.
🔹
پیش‌بینی می‌شود حتی اگر بحران در خاورمیانه فروکش کند، پیامدهای مخرب و زنجیره‌ای جنگ در ماه‌های آینده تشدید شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.56K · <a href="https://t.me/farsna/440057" target="_blank">📅 14:31 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440056">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mi9mP-zaGx95Kze7Y0c5-iwIF1X4205crZfkpBRjmMeaRNQVaGvtZ4NYdp01za0NcuVeA7XHKWixE03x0_Yudd_qkXlTPFrv6lC_NHRlI1YtfpKZxK1hThULYZdT41P-xAl-i20oMeZO8QKSDth5_DqkIKg_tXtN3I2Bpzx_uCNhea3ilbTPC7-IFzRrxA50FyNMbzNe188auXMWTi2_jRSP_igp2Rd8me6H-mN4_fSiqS-Ak5p6Z529egLAP2VznOx71bYDP2tfiTWpMn32MSVs6Xo6UlF8q2ijh5tYcnmlHysxoj4dYuRQjr720_Fl6XtV1-y14ma1LGC_jTREeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نخست‌وزیر پیشین رژیم صهیونی: نتانیاهو ما را به‌سمت شکست مطلق در لبنان می‌برد
🔹
باراک: هیچ نشانه‌ای از فروپاشی حزب‌الله دیده نمی‌شود؛ آنها همچنان قادر هستند به اسرائیل آسیب برسانند.
🔹
بنیامین نتانیاهو ما را به‌سمت شکست مطلق در لبنان می‌برد.
🔹
دلخوش‌کردن به راهکار نظامی صِرف در لبنان، توهمی خطرناک است؛ هرگونه پیشرفت در گروی برکناری نتانیاهو از قدرت است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.31K · <a href="https://t.me/farsna/440056" target="_blank">📅 14:15 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440055">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PHmhBVO2phuz5K5CHQvzyojOlRf6Hz1bvz3-p15w2aeQJlYdfIoWg2XYw3f9JviMoxrJ-GuC-d_o9hc4W1rkrrgkRd9ECwxqN2DCLlf9GxxcyVF-qdc__F0pbBoB5ulpPUfraEzTLGQ0xQC9M2X1nkE0rIAbYsCckwnBCPfbEufxd2OXRgY5pIfw6tr1lQJKyFNB8wQXJ16bDo9DKJA20JvSK-TyRNzqTyvEE9Divmn-obqgoSuYlk1WDrc_wafOPHCRrSej7FJKmifJ9m5b3grqN1yV5Ts0XyBvUwkwRw3D-ioioSaZm22z50EFqGd_TjFx1wUfZcxLIQph4FtRrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خطیب جمعه تهران: هیمنهٔ روانی دشمن فرو ریخته است
🔹
بررسی‌های میدانی نشان می‌دهد که ایران در یک موقعیت ممتاز و کم‌نظیر قرار گرفته است.
🔹
امروز نشانه‌های یک فتح مبین دیگر را مشاهده می‌کنیم و خداوند متعال آثار این پیروزی را در عرصه‌های مختلف به ملت ایران نشان داده است.
🔹
یکی از مهم‌ترین جلوه‌های این شرایط، فروپاشی هیمنهٔ روانی دشمن است؛ وضعیتی که از لرزش بازارهای مالی دشمنان تا اضطراب و نگرانی رژیم صهیونیستی قابل مشاهده است.
🔹
در گذشته گاهی با یک تهدید، یک جابه‌جایی نظامی یا حتی یک موضع‌گیری از سوی دشمنان، نگرانی‌هایی در جامعه ایجاد می‌شد و آثار آن در شاخص‌های اقتصادی نمایان بود؛ اما امروز معادلات تغییر کرده است.
🔹
اکنون در شرایطی قرار داریم که حتی بدون استفاده از قدرت سخت و توان موشکی، صرف صدور یک بیانیه از سوی نیروهای مسلح جمهوری اسلامی ایران می‌تواند لرزه بر اندام دشمنان بیندازد و آنان را دچار نگرانی و آشفتگی کند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.95K · <a href="https://t.me/farsna/440055" target="_blank">📅 14:05 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440054">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78cb1a827f.mp4?token=sntqds-sDs3cUVVsKDrHhZ-5TP0PUZ6BoQdc-Qt0B0oYmD6VnbJfeLOdtLhLQF8yfYG1R3dwmVWB4KVpPCdgxXZAI0MKfWHFSGDoKaMa8VZRShllSPvAtf7M6C_LHglCyORF-nSEAP1aVbTpVqHNaFFZGzvUSiMivBLsHXS1L2CU7-yKWYKqyT1Dj6U0cJZgijihzQmO3f25NJNnC7cC9TP674liUhu52NV9cYTSv54XBc0-64XP3_h621eGxf4xwcLw0tTz4OvWdGqGeymI4evgvsVHLoiyYP263_-a5towY3veevYxhc6j5lVvkOm9mo74ydprXdNWZHZ-XUIGkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78cb1a827f.mp4?token=sntqds-sDs3cUVVsKDrHhZ-5TP0PUZ6BoQdc-Qt0B0oYmD6VnbJfeLOdtLhLQF8yfYG1R3dwmVWB4KVpPCdgxXZAI0MKfWHFSGDoKaMa8VZRShllSPvAtf7M6C_LHglCyORF-nSEAP1aVbTpVqHNaFFZGzvUSiMivBLsHXS1L2CU7-yKWYKqyT1Dj6U0cJZgijihzQmO3f25NJNnC7cC9TP674liUhu52NV9cYTSv54XBc0-64XP3_h621eGxf4xwcLw0tTz4OvWdGqGeymI4evgvsVHLoiyYP263_-a5towY3veevYxhc6j5lVvkOm9mo74ydprXdNWZHZ-XUIGkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
هندوانه‌ها سوار پهپاد شدند
🔹
در تازه‌ترین نمونه از کاربرد فناوری پهپاد در بخش کشاورزی، استان گوئی‌ژو در جنوب غربی چین از پهپادها برای حمل هندوانه در مناطق کوهستانی استفاده کرده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.81K · <a href="https://t.me/farsna/440054" target="_blank">📅 13:57 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440053">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aNhCGM6PFndc6LUhcVo-HxkXsataQ7PzoG1i-ERN-B1n8JvZqj8aypkSU_AHNwaTgWZPcXaLHwawRnTBoTuh_LrTAc374xltdExmx_tdGniTsbMn5Q9W3P1OwBgYvXLHUsgN6I43JkO93Hn9Sutl_nT72WTqB00zypripkj5jNO_uHcxYWaiZZRjV6yluxPlx0jG2UleSMFSa1BMSjaMU85dDxH-iv2dV4CdNdjEQ0a5FRq690pUTIcPo-7s95c0XURktHAde648djLX_GR-eNjaP7tRecDaIHNjGtMERu8VFuhT6A3cKNotHIg9_M0E9njaZtTZdb9aFIRmhy67UQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
کشتکار به‌دلیل مصدومیت مدال نقره گرفت
🔹
محمدمهدی کشتکار در وزن ۶۳ کیلوگرم رقابت‌های کشتی فرنگی رنکینگ جهانی مغولستان، در دیدار فینال به‌علت مصدومیت انصراف داد و به نقره رسید. @Farsna</div>
<div class="tg-footer">👁️ 7.73K · <a href="https://t.me/farsna/440053" target="_blank">📅 13:55 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440052">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M8zn1u8PzWSWIBKvVdIOtiJQHtz5JftdBqpEKwUf7936BRRR5jpLZ4Vs1Yg2nR0gRsbr50DnHFMtkHwlM45n1Qv8Cov580_xukX83bNDb9xaXAkN3wh6vfR1OwJW61BjZZ8hqlENJpPcNEeoTHBLLEZqbqvy-JQBm1bkYfPpm815TwEQ3KL75v0pmQgtyA24KnxUyAABDYqPmi_OGznJ_p8gNM2QQy3aS4qpYQwK2iDcEdzJ4SYBgqBARnfiwl2rPzj-syu5TVKLXpf3UZ3euaIK8k10Wd9LPxuHkLo-14glhiRU-vAiY3UAY6GTUBz4CYIH_Q470hhgAU3qQGJoeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۵ شهروند جمهوری آذربایجان در حمله پهپادی کشته شدند
🔹
براساس گزارشات منتشر شده، شب گذشته دو کشتی باری با مجموع ۲۵ شهروند آذربایجانی در معرض حملات پهپادی قرار گرفتند. این کشتی‌ها خارجی بوده و به جمهوری آذربایجان تعلق نداشته‌اند.
🔹
به گفتهٔ وزارت خارجهٔ جمهوری آذربایجان، در این حمله ۵ نفر کشته و ۳ تن دیگر مجروح شده‌اند.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 7.87K · <a href="https://t.me/farsna/440052" target="_blank">📅 13:48 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440051">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cfd067f409.mp4?token=HzZgY-39z-fQnuV4v7ft1pS7UM7Df2uBFvJqGKuvgn931X5B22dFnPKw2BGEd6AvU3lG2cV7OKmQk7RHLaqeiNVFuygu49fEEkTTyAI1VfSB4dxbhaReDib9-Z0zCs5GxYHTtIXv5ZHSPfWuYIGy25S1jnaXIy9iuEEF_11lzqinWVsrJKDnxexAOcIZ105QM6uIruAEaJ2GqPNYWlR-G25rMy7Lwxz_4fB7sJ0F_p0XQa-61oKKbJrRYWTazjl89i5_1C8x_r74-JMpL4E12fqzNOHle-p2IukZnz_3x3Px_t7-B1DBEKYryzyrUZ9mxOpEIsgbwjDrM2jmg8B10Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cfd067f409.mp4?token=HzZgY-39z-fQnuV4v7ft1pS7UM7Df2uBFvJqGKuvgn931X5B22dFnPKw2BGEd6AvU3lG2cV7OKmQk7RHLaqeiNVFuygu49fEEkTTyAI1VfSB4dxbhaReDib9-Z0zCs5GxYHTtIXv5ZHSPfWuYIGy25S1jnaXIy9iuEEF_11lzqinWVsrJKDnxexAOcIZ105QM6uIruAEaJ2GqPNYWlR-G25rMy7Lwxz_4fB7sJ0F_p0XQa-61oKKbJrRYWTazjl89i5_1C8x_r74-JMpL4E12fqzNOHle-p2IukZnz_3x3Px_t7-B1DBEKYryzyrUZ9mxOpEIsgbwjDrM2jmg8B10Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
احمدی‌وفا طلایی شد
🔹
در وزن ۶۰ کیلوگرم مسابقات رنکینگ جهانی کشتی فرنگی در مغولستان، علی احمدی‌وفا در دیدار نهایی با نتیجهٔ ۱۰ بر صفر یو چول رو از کره‌شمالی را مغلوب کرد و صاحب  مدال طلا شد.  @Farsna</div>
<div class="tg-footer">👁️ 8.09K · <a href="https://t.me/farsna/440051" target="_blank">📅 13:36 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440050">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/alF6_wldyHMvPkYH6l9USr6cmqeXDXoFFa8v06wfi64HLvIp67bwbAhMa4dalOQw3jdgFNC4uQMBrypbFfjLfGpwAgbGyiln8N1GDNoMQc7IzBEuxE2NHP6B_ARjO0KAlfhib0aPdblkXLT0dHqoUgxFyGxW7TscBH4LDr9-pekDnER8oD2061k-Ak1BYW9reQWtoiyZyrn7BDjx7PTyeBW8XEB-J-w6DX_hzlwgjiLVGrvqXRWQb1klNT85leVcs8Joq0yuOSyfwXmRtf1S7XeeHQWpWc2xCkvddoEXK4IiQYesDIZe8YjB9GQpOhekdCDzCFE7SqnQ02MaO3LV3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سرنوشت دارایی‌های مسدودشدهٔ ایران همچنان در هاله‌ای از ابهام
🔹
درحالی‌که یکی از اصلی‌ترین خواسته‌های ایران در مذاکرات، آزادسازی دارایی‌های این کشور است، شبکهٔ العربیه مدعی شده است که ایالات متحده همچنان با درخواست ایران برای آزادسازی دارایی‌های بلوکه‌شده مخالفت می‌کند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.25K · <a href="https://t.me/farsna/440050" target="_blank">📅 13:29 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440049">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">موافقت رهبر انقلاب با عفو یا تخفیف و تبدیل مجازات بیش از ۲ هزار نفر از محکومان قضایی
🔹
حضرت آیت‌الله سیدمجتبی حسینی خامنه‌ای، رهبر انقلاب اسلامی، با درخواست رئیس قوه‌‌قضاییه برای عفو یا تخفیف و تبدیل مجازات ۲ هزار نفر از محکومان محاکم به‌مناسبت عید سعید غدیر…</div>
<div class="tg-footer">👁️ 8.62K · <a href="https://t.me/farsna/440049" target="_blank">📅 13:17 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440048">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0ae75fd3e.mp4?token=nwadS3BRyNSXcF4izGo2Mv84TJykltIb0jjtktay0lLayM5DzYN2dKXkwcAsdLF_vEBUn7dEbq4fhaBsHm1dk--xH1UYHa6jsBGBqadwS-lIv0s_eKBKGenspySEKpst4y-R9Vo5bx2GknOHkWZnSNY3VEoGq-BtbHHVRs4mdon9ooz78DC7c6SpQztihYX5p9yl6pmnG4Wmy84teDTQXUMjJfimrgd4jlmhxVPnqjZOaxrHP4cjbjyfihvHXQ1-KuFWg2v6HwQjcDwkG4GNMqXnPCrAgZrMIipVPdk6se6OG0te2uSF-i-AVv5vOwb0Xrk91OfsCZXN_VA8EWDtoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0ae75fd3e.mp4?token=nwadS3BRyNSXcF4izGo2Mv84TJykltIb0jjtktay0lLayM5DzYN2dKXkwcAsdLF_vEBUn7dEbq4fhaBsHm1dk--xH1UYHa6jsBGBqadwS-lIv0s_eKBKGenspySEKpst4y-R9Vo5bx2GknOHkWZnSNY3VEoGq-BtbHHVRs4mdon9ooz78DC7c6SpQztihYX5p9yl6pmnG4Wmy84teDTQXUMjJfimrgd4jlmhxVPnqjZOaxrHP4cjbjyfihvHXQ1-KuFWg2v6HwQjcDwkG4GNMqXnPCrAgZrMIipVPdk6se6OG0te2uSF-i-AVv5vOwb0Xrk91OfsCZXN_VA8EWDtoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
احمدی‌وفا طلایی شد
🔹
در وزن ۶۰ کیلوگرم مسابقات رنکینگ جهانی کشتی فرنگی در مغولستان، علی احمدی‌وفا در دیدار نهایی با نتیجهٔ ۱۰ بر صفر یو چول رو از کره‌شمالی را مغلوب کرد و صاحب  مدال طلا شد.
@Farsna</div>
<div class="tg-footer">👁️ 8.21K · <a href="https://t.me/farsna/440048" target="_blank">📅 13:10 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440047">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">حملهٔ رژیم صهیونی به یک خودرو در لبنان
🔹
خبرگزاری ملی لبنان: در حملهٔ هوایی رژیم صهیونیستی خودرویی در منطقهٔ کفررمان در جنوب لبنان هدف قرار گرفت که این حمله یک شهید برجای گذاشت.
@Farsna</div>
<div class="tg-footer">👁️ 8.39K · <a href="https://t.me/farsna/440047" target="_blank">📅 13:00 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440046">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">حزب‌الله: تجمع ادوات و نظامیان ارتش دشمن اسرائیلی را در مناطق البالوع و وادی‌ الحجیر هدف قرار دادیم.
@Farsna</div>
<div class="tg-footer">👁️ 8.52K · <a href="https://t.me/farsna/440046" target="_blank">📅 12:59 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440045">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🎥
رئیس فدراسیون فوتبال: تا زمان مشخص‌نشدن تکلیف ویزای آمریکا به مکزیک نمی‌رویم
🔹
تمام ویزاهای مربوط به مکزیک و مجموعه‌ای که باید در تیخوانا حاضر شوند، صادر شده و هیچ مشکلی بابت هیچ فردی وجود ندارد.
🔹
تیم ملی ما باید فردا با پاسپورت‌هایش به تیخوانا مکزیک برود‌. هر اتفاقی می‌ا‌فتد باید امروز معلوم شود‌.
🔹
به فیفا گفتیم اگر ویزای بازیکنان یا عوامل کادرفنی و سایر افراد را صادر نکنند، ممکن است تصمیم‌های دیگری بگیریم‌.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.52K · <a href="https://t.me/farsna/440045" target="_blank">📅 12:50 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440044">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">موافقت رهبر انقلاب با عفو یا تخفیف و تبدیل مجازات بیش از ۲ هزار نفر از محکومان قضایی
🔹
حضرت آیت‌الله سیدمجتبی حسینی خامنه‌ای، رهبر انقلاب اسلامی، با درخواست رئیس قوه‌‌قضاییه برای عفو یا تخفیف و تبدیل مجازات ۲ هزار نفر از محکومان محاکم به‌مناسبت عید سعید غدیر خم موافقت کردند.
@Farsna</div>
<div class="tg-footer">👁️ 8.33K · <a href="https://t.me/farsna/440044" target="_blank">📅 12:48 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440043">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/abae735a11.mp4?token=fFr4kAyfabeXwtl0pcVLWJJ9IP3RkFAw3AOOXU5uS8Wn1w7B_lmqJ3P2NmgEYiuorHePD_c_8m9kawnhP8RgVrPUV8MAPaUe-Qc8mjGC97JKdYAJhNrzEShTKukersSssd2NaMDAT9Db9tQh5_jJxzis3K4zO8fKu9SOfykX-_KEw2gIN8k_8n1H5jhgfHOgIXsYNM5xReEVoRkWV4LlxxxkQVOE_zAl5Y4w1qE9SF3jPxx6W7IEwl9bC0niq5q0OM72un3nImYb3JZu_Fus0zJdiDh9IEtEEq7tSrywZSWZEww42qqGrhFeL0WdPIfzodWb4omSunREx5ZXjJMrCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/abae735a11.mp4?token=fFr4kAyfabeXwtl0pcVLWJJ9IP3RkFAw3AOOXU5uS8Wn1w7B_lmqJ3P2NmgEYiuorHePD_c_8m9kawnhP8RgVrPUV8MAPaUe-Qc8mjGC97JKdYAJhNrzEShTKukersSssd2NaMDAT9Db9tQh5_jJxzis3K4zO8fKu9SOfykX-_KEw2gIN8k_8n1H5jhgfHOgIXsYNM5xReEVoRkWV4LlxxxkQVOE_zAl5Y4w1qE9SF3jPxx6W7IEwl9bC0niq5q0OM72un3nImYb3JZu_Fus0zJdiDh9IEtEEq7tSrywZSWZEww42qqGrhFeL0WdPIfzodWb4omSunREx5ZXjJMrCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
انفجار مهیب تانکر حامل سوخت قاچاق در مکزیک
🔹
انفجار یک تانکر حامل سوخت در شهر «تپئاکا» مکزیک آتش‌سوزی گسترده‌ای ایجاد کرد و ستونی عظیم از آتش و دود را به آسمان فرستاد. این حادثه موجب تخلیه اضطراری حدود ۲ هزار نفر از ساکنان مناطق اطراف شد.
🔹
به گفته مقامات، در این حادثه تاکنون هیچ تلفاتی گزارش نشده است، اما دست‌کم سه نفر زخمی شده و برای درمان به بیمارستان منتقل شده‌اند.
🔹
بر اساس گزارش رسانه‌های محلی، گفته می‌شود این تانکر در لحظه انفجار حامل بنزین قاچاق بوده است.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 8.94K · <a href="https://t.me/farsna/440043" target="_blank">📅 12:38 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440042">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DuhBaPXRH2OgtB4kpQPmAqjR2DGHz9LrqrenAMisBg1cmPusjpWTNnESxVtkI6n5ENAWQ8qqZMnbta5mYbgSmtTWDvU13aF7iAL1N0V5bEUCOxq-4-jxr1E47vIq0nt2xal3pxeBHvn5kSKtqiktA4w_SRoDjIJ9WzyCq_6Z3PAPQOANSrL5Ue4B8j4Q8LkXkslhfQCMubBWV2DhGcwWPgN6U2OF4qxyAKr8uNLSu4S7m3H6SdLXx1Vxz4UHE-6QXhOfprmYF7wbCanrTE34ABfHU5p4Veh9F3_6URk5djmPuevPBjfkCUc-vTTT0EX9joORByT9cHn-5MV219QdNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیدار سه‌جانبهٔ ایران، روسیه و چین با گروسی پیش از نشست شورای حکام
🔹
در آستانهٔ برگزاری نشست فصلی شورای حکام آژانس که دوشنبه آغاز خواهد شد، سفرا و نمایندگان دائم ایران، روسیه و چین در وین با مدیرکل آژانس بین‌المللی انرژی اتمی گفت‌وگو و تبادل‌نظر کردند.
🔸
نشست شورای حکام آژانس بین‌المللی انرژی اتمی از هشتم تا ۱۲ ژوئن ۲۰۲۶ (۱۸ تا ۲۲ خرداد) در وین برگزار خواهد شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.68K · <a href="https://t.me/farsna/440042" target="_blank">📅 12:24 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440041">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0335b58aa6.mp4?token=D8j5hN1ejCSJhsKeNfCciqdZSLx8aD3L9BErY8_26NV4mmAk1KNblWXnA-5QGrxvImMD6oFzzQzanqshAFY5tfOIENym08WtsJ3IHyN7vposej7gYeUNgV83i9Fi-q6QVWk5Hw72P-lEgayte10ufwYUFMulTy2_tKJTUhbpNwvTjvb-gMJn_S3ZP3TaxX6QiG-eaW99_MJd2IJFpEl4OIChh6dX572WZ1fuJbCL9WO2-0_DAcb3FU-p_M0TwzVOlLro5q18JXN78Zvj8WcRjnLV8gBtbcdGERKSGuEuDZ6HMwYVZ8kc-QwgeSi4YxePvgRoMJLCiB9YQPTD8GqEkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0335b58aa6.mp4?token=D8j5hN1ejCSJhsKeNfCciqdZSLx8aD3L9BErY8_26NV4mmAk1KNblWXnA-5QGrxvImMD6oFzzQzanqshAFY5tfOIENym08WtsJ3IHyN7vposej7gYeUNgV83i9Fi-q6QVWk5Hw72P-lEgayte10ufwYUFMulTy2_tKJTUhbpNwvTjvb-gMJn_S3ZP3TaxX6QiG-eaW99_MJd2IJFpEl4OIChh6dX572WZ1fuJbCL9WO2-0_DAcb3FU-p_M0TwzVOlLro5q18JXN78Zvj8WcRjnLV8gBtbcdGERKSGuEuDZ6HMwYVZ8kc-QwgeSi4YxePvgRoMJLCiB9YQPTD8GqEkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بزرگ‌ترین رژهٔ موتورهای سنگین در مشهد
@Farsna</div>
<div class="tg-footer">👁️ 9.08K · <a href="https://t.me/farsna/440041" target="_blank">📅 12:15 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440040">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🎥
ایران بر چه مبنایی از حق حاکمیت خود بر تنگهٔ هرمز دفاع می‌کند؟
🔹
رئیس انجمن حقوق بین‌الملل ایران: تنگهٔ هرمز میان ایران و عمان قرار دارد و بخش مهمی از آن در آب‌های سرزمینی ۲ کشور واقع شده است؛ بنابراین ایران و عمان بر این محدوده اعمال حاکمیت می‌کنند و دولت‌های دیگر باید این واقعیت حقوقی را مدنظر قرار دهند.
🔹
ایران در چارچوب حقوق بین‌الملل حق دارد بر عبور شناورها نظارت کند و با توجه به شرایط امنیتی موجود و حق دفاع مشروع مندرج در مادهٔ ۵۱ منشور ملل متحد، اقدامات لازم را برای حفظ امنیت و حاکمیت سرزمینی خود انجام دهد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.06K · <a href="https://t.me/farsna/440040" target="_blank">📅 12:01 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440038">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">اسرائیل برای ۳ منطقه در جنوب لبنان دستور تخلیه صادر کرد
🔹
با وجود آتش‌بس جدید در لبنان که از سوی رئیس‌جمهور آمریکا اعلام شد، ارتش رژیم صهیونیستی برای ۳ شهر و روستا در جنوب لبنان هشدار تخلیهٔ فوری صادر کرد. @Farsna - Link</div>
<div class="tg-footer">👁️ 9.24K · <a href="https://t.me/farsna/440038" target="_blank">📅 11:39 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440037">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hqTZy9FvSRy5dF_kV0fRULYFOgS_lNxBcGsTHkFcmP2PEf-VvNfh-nNbzAq7Sdlxiirs2uaHn_CGUl49EeZ5jX6qRKb1FYzN5wEkU7BGZRiVb_TNkcr-xw1TpAcOu6MZCdWqDL2SBzDxorn_lgkksGCT7Ju3aWza-Va5Bh8UO8PsXvJMNXLSDrmOhhmmOX0csz1Xd6dwYHDNVKJbm9Vm8f8hyNnfaLP_So6wtIOZdmukOUK59lNt1bMzE7xPIPGB_qyD9aQBHxUfAIKOIDFW6vLTt-PPKgV5cklnm401HXpm-tlTbDPgjVD5aZEZdBNn3-lP3Kzvolpf6mo-EOM4eQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مجروحیت ۱۰ صهیونیست در روز گذشته
🔹
وزارت بهداشت رژیم صهیونیستی با بیان اینکه ۱۰ صهیونیست روز گذشته در حملات حزب‌الله مجروح شدند، تصریح کرد که تعداد مجروحان این رژیم در جبهه شمالی فلسطین اشغالی از زمان جنگ علیه ایران به ۱۱۰۴ تن رسیده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.29K · <a href="https://t.me/farsna/440037" target="_blank">📅 11:35 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440036">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">اسرائیل برای ۳ منطقه در جنوب لبنان دستور تخلیه صادر کرد
🔹
با وجود آتش‌بس جدید در لبنان که از سوی رئیس‌جمهور آمریکا اعلام شد، ارتش رژیم صهیونیستی برای ۳ شهر و روستا در جنوب لبنان هشدار تخلیهٔ فوری صادر کرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.21K · <a href="https://t.me/farsna/440036" target="_blank">📅 11:26 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440035">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F9o227wqGpzrX1a5yUObmTjzYcomwl2_HrjW7rXsNUD_YGeX47xVc8zsA3Uz_A7WV-KB2cXcAMrnnpnHwp94XQYiXuMwcfUnwPl10RC_9YWyBC_6pRcVpHTR9WpcbHmV4-N2OH68K3tJfQ7dxwlShpxqepbKMQpMl0kXCJDiLQOy3VYIqfq35m7gXhRRxQrM5UHimn5fhK_y3S3KmBrfQgEYAC3kep-lKsfyEopPK-QMYfif0x_fc6EeB4zm62VXxrodptUCuoZdbMHKK-7_xXSTemt7uu01DVuortuemrMbbfFVtHT4K7NYGHvcBUKBcYpP5JptuPloOtY9iC7Z0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مسکو: نظامیان اسرائیلی باید از لبنان خارج شوند
🔹
سخنگوی وزارت خارجه روسیه: ما هیچ تعهدی [از جانب اسرائیل] به آتش‌بس در لبنان نمی‌بینیم و نقض آتش‌بس توسط طرف اسرائیلی سیستماتیک شده است.
🔹
ارتش اسرائیل به عملیات نظامی خود ادامه می‌دهد و به تدریج منطقهٔ اشغالی در جنوب لبنان را گسترش می‌دهد.
🔹
هم‌اکنون خواستار آتش‌بس فوری در لبنان هستیم؛ نظامیان اسرائیل باید هرچه سریعتر از خاک لبنان خارج شوند.
🔹
ما هم مانند یونسکو نگران حملات اسرائیل به قلعهٔ الشقیف و شهر صور، به‌عنوان یک میراث جهانی هستیم؛ هدف قرار دادن عمدی یا تخریب وحشیانهٔ اماکن فرهنگی غیرقانونی و غیرقابل قبول است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.51K · <a href="https://t.me/farsna/440035" target="_blank">📅 11:22 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440034">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TmMJBKpspJioDGGHqYby10AYEXBjKQrxdoCmvFIyHyof5p0zSoWmxpgZN_F5y5ExU7HKybrzVErC_Hl4ondySgkkfZJHtezegpVqwvwcM9F2IcKSo3bHYRafZk4h9XCVyL0rHtIgM4Nbg-dC0D_VxLVpw-39RVIF4SD2W8WZazhcUoLcDFTTVY5EXpX5D4HwJrTwieV6iFm0ocQMyDANgTFX259Xf1crmMpWxEkTIAwRnJJeMQ617yXmh_qzohGNwlPnQhU6kQH1-ek48kkZG53QtaqD9l6hSo8H0NEEjdVOsDhL21MJGNsEOeN2ggCTr0CaktzuyBMlqGBT3tPV1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مجلس نمایندگان آمریکا باز هم برخلاف نظر ترامپ رای داد
🔹
بعد از تصویب قطعنامه محدودیت اختیارات جنگی ترامپ علیه ایران، مجلس نمایندگان آمریکا با رای اعضای جمهوری‌خواه طرح کمک تسلیحاتی به اوکراین را برخلاف نظر ترامپ مورد تصویب قرار داد.
🔹
مایک جانسون، رئیس مجلس نمایندگان، پیش از رأی‌گیری از اعضای حزب خود خواسته بود با این طرح مخالفت کنند و استدلال کرده بود که باید به ترامپ فرصت داده شود تا مذاکرات خود با روسیه را پیش ببرد. با این حال، ۱۸ نماینده جمهوری‌خواه به همراه یک نماینده مستقل که معمولاً با جمهوری‌خواهان رأی می‌دهد، در حمایت از این لایحه به دموکرات‌ها پیوستند.
🔹
این طرح شامل تحریم‌های گسترده علیه مقام‌ها و نهادهای روسیه، از جمله بانک‌های بزرگ، شرکت‌های نفتی و معدنی است. همچنین تعرفه ۵۰۰ درصدی بر تمامی کالاهای وارداتی روسیه به آمریکا اعمال می‌کند و واردات نفت خام روسیه را ممنوع می‌سازد.
🔹
در بخش حمایت از اوکراین نیز فروش تسلیحات به ارزش ۸ میلیارد دلار مجاز شده و برنامه «لند-لیز» دوران جو بایدن برای تأمین تجهیزات نظامی کی‌یف تمدید می‌شود.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 7.56K · <a href="https://t.me/farsna/440034" target="_blank">📅 11:14 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440033">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LYZJeEACoio5p30ylLXLrGkw2GFb1RSQkqWa5o-i4i12fyU-cIhMIZ6gTweV2Qomsohxct_LntTdXXvuH-vPPgFJUFSCcdjOr2RL-vWQgMt7TiJodyrTPB9L2KS_-gBrct7s5nPLPjOB8TFTVra1uWl9UfngrC78gPYGjLKjp7gmp0CYsNxJp5_yHZSDFAl7jq84Y4CIrJQqrsmP_9svS47W2OPR8f-tJ8eAqW7l6jz9lM3QbuQTUnCZinGcWYBbTdBLTMCk5xavhPxEXTZKCP_1lGKgx7Ii1RxR8SvtIlxg7y-g19lAWOx_apwyzcTmQWqkfZ_eZ5FT65hZDQtR5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دلایل ناکامی آلمان برای عضویت غیردائم در شورای امنیت از زبان بقائی
🔹
سخنگوی وزارت خارجه امروز در واکنش به ناکامی آلمان در کسب حداقل آرای لازم در مجمع عمومی سازمان ملل برای انتخاب به‌عنوان یکی از ۱۰ عضو غیردائم شورای امنیت سازمان ملل متحد: ناکامی آلمان در کسب کرسی شورای امنیت سازمان ملل، آن هم برای نخستین بار پس از دهه‌ها، نشانه روشنی از اعتراض جامعه جهانی نسبت به رویکرد غیرمسئولانه و ریاکارانه هیئت حاکمه این کشور در قبال نسل‌کشی فلسطینی‌ها و نیز تجاوز نظامی رژیم صهیونیستی علیه ایران است.
🔹
به یاد داشته باشیم که آلمان یکی از بزرگترین فروشندگان تسلیحات مرگبار به رژیم صهیونیستی است، نسل‌کشی فلسطینیان را توجیه می‌کرد و به هنگام تجاوز نظامی رژیم صهیونیستی به ایران به جای تعهد به هنجارهای بین‌المللی و محکوم کردن این تجاوز، آن را این‌گونه توصیف کرد: «کار کثیفی که اسرائیل برای همه ما انجام می‌دهد».
🔹
این کشور حتی در قبال جنایت جنگی قتل عام ۱۷۰ دانش‌آموز در شهر میناب توسط موشک‌های آمریکایی سکوت کرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.53K · <a href="https://t.me/farsna/440033" target="_blank">📅 11:12 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440032">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">وزرای کشور ایران و پاکستان
گفت‌وگو کردند
🔹
طبق گزارش الجزیره،‌ وزیر کشور پاکستان در حاشیهٔ نشست وزرای کشور سازمان همکاری شانگهای در بیشکک قرقیزستان، با همتای ایرانی دیدار و دربارهٔ روابط دوجانبه، امنیت مرزی و ثبات منطقه‌ای گفت‌وگو کرد.
🔹
وزارت کشور پاکستان هم اعلام کرد ۲ وزیر بر ضرورت تداوم مستمر تلاش‌های دیپلماتیک برای تحقق صلح پایدار در منطقه تأکید کردند.
@Farsna</div>
<div class="tg-footer">👁️ 7.6K · <a href="https://t.me/farsna/440032" target="_blank">📅 11:07 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440031">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c0d4f4bdd9.mp4?token=YCypbLIE1rppcieaKXynS2uTf2S6A6u0Ozlw5M2B7GSLF6IdGxxe12YzIlQG6eGCY2lDRpoqPe3LtAKBmZsO88oP2BIzFGY0pyc4p6iQA9iOtxCtgr14ChfElIP7jrffxiU62Pzu9uqSi5-yYHP7fq5DJb3xfuMeTePXJcyrBmyHLc1IXgMIF6EF4n9FGHgZMsGeEdbt_5hSWJ4NH0jfr1sSF0FSxpG73Sp8y6coVevKX6USHUhg9S8zBaQKcl0l0msflzVut9W7XkW2xse-cR-E8vn9_sDCTx7XPXWKsPIRquLGOQE32vaKecCG3VC8UsJ-2ZJtQ-6b71L-_wkhkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c0d4f4bdd9.mp4?token=YCypbLIE1rppcieaKXynS2uTf2S6A6u0Ozlw5M2B7GSLF6IdGxxe12YzIlQG6eGCY2lDRpoqPe3LtAKBmZsO88oP2BIzFGY0pyc4p6iQA9iOtxCtgr14ChfElIP7jrffxiU62Pzu9uqSi5-yYHP7fq5DJb3xfuMeTePXJcyrBmyHLc1IXgMIF6EF4n9FGHgZMsGeEdbt_5hSWJ4NH0jfr1sSF0FSxpG73Sp8y6coVevKX6USHUhg9S8zBaQKcl0l0msflzVut9W7XkW2xse-cR-E8vn9_sDCTx7XPXWKsPIRquLGOQE32vaKecCG3VC8UsJ-2ZJtQ-6b71L-_wkhkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مشاور اقتصادی ترامپ: ایران عامل تورم در آمریکا است
🔹
جمهوری اسلامی ایران با بستن تنگهٔ هرمز باعث تورم در آمریکا شده است.
🔹
دموکرات‌ها سعی می‌کنند ما را با این کار به دردسر بیاندازند؛ رسانه‌های سنتی سعی می‌کنند به آنها در انجام این کار کمک کنند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.32K · <a href="https://t.me/farsna/440031" target="_blank">📅 10:55 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440030">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NwANBkznpTY8QfvJuhNja8xto0U3RwpuEN_5ebdhQYL7m6Z5gNBMLS7Awre5oULq7yDMBiXmXtWEIO8TNXZ1-Yr1yefYoeo3Z0AQJnfpDvIETT5wT7esFUi4aFPUeco0n6CvXLW4nvnz3qa9THzUP4xbwbZLjDDxio7oU2fJzrSFwmrOS9zXOCjnwe6QJrKQA3MeMcKpZkSdDPJPb6ZYHl-Uq9r_f4ArBRWMtTbsIfcE6dW_7bxKIWI5RMpM4N-sHdoaptXd8fya7aEwB-H3wu7GAdfTgaCo65PPYX1Jf9tMV-dCCIOC-Hz4o0L6SFHnirpdfbw1oyduaHyRAc_iIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توقف بارگیری نفت در یکی از بنادر عمان
🔹
منابع مطلع امروز از توقف بارگیری نفت در یکی از بنادر عمان خبر دادند.
🔹
خبرگزاری «رویترز» به نقل از این منابع که نامشان را فاش نکرد، گزارش داد که بر اثر وقوع انفجار در تأسیسات نفتی در «بندر الفحل»، بارگیری نفت عمان متوقف…</div>
<div class="tg-footer">👁️ 8.65K · <a href="https://t.me/farsna/440030" target="_blank">📅 10:43 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440029">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fc7CCPRBmuTgeflj2Ow4YazIfdJUy-7uoS6u5PAV7844o2FW8qkc3ZVqqI3dqUwTERDzU3TlLxQqq1rcHVSdR1fYa2xpffLuGFidlqLu7xB_9pCX90l-rGBl_VPsthZ1LVcMWiWO6FtfL0y70bA0aboDaUsvClQEieHDHU7cnYayo6ZUf8LW7F4USy-dG2tYo3FsD6aK9ENpwqSe_cbdIop2206Rs56kX5E68Z9bkvr9ERaE5nv-3DvY86CFBOBqy8f257mdvXFkF4TcJKGBUHQ5UHL1Fu7VGrpqydsp0gNBFYQnXzWYXIPTRu40mmMTwgrW6Rnil6ARLrSK4G3S6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر خارجه روسیه: آمریکا و ایران باید گفت
‌
وگوها را ادامه دهند
🔹
ما قویاً از گفت‌وگویی که چه خوب و چه بد، بین واشنگتن و تهران با میانجی‌گری پاکستانی‌ها درحال انجام است، حمایت می‌کنیم. سعودی‌ها و مصری‌ها نیز مشتاق کمک هستند.
🔹
بسیار مهم است که این گفت‌وگو ادامه یابد. توافقی که حاصل می‌شود باید منافع ایران و کشورهای همسایه‌اش را در نظر بگیرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.93K · <a href="https://t.me/farsna/440029" target="_blank">📅 10:31 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440028">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q2n0dKH8vUR1BURVUOk1E7OYR1Pb_ZMp9LR5NOu8P50TXJPZxPiGIg9tEH_jqwgHvlllB1SUc0Fj5BI-dATAdodJbwypG_RMrL6k8lX2WuTKSqp8nd66T8etWmhKzCYq1Zkpi7w-PGeZP4CjvhkhTViNdwPLiNs5LzljTW-glDdmtgQO6j4nEjMI7mZqHA_8VuE8-dM6LMpTrFMvmhHrhgRAMxHTrEFIDEoDABGdeA1LpPIDvzeu2BHv4ESPrHIe-iPfyNibmcVeHLulyXR2I3U9RSV6tHxjAGwVyQTPDJWL8FEm71TyFBWvM2qeeIM73FR-6-tR00_6gF7S7oowEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">احتمال لغو ارسال موشک‌های تاماهاک به آلمان
🔹
پالتیکو: واشنگتن به‌دلیل نگرانی از واکنش روسیه، ارسال موشک‌های تاماهاک به آلمان را احتمالا لغو می‌کند.
🔹
این تصمیم احتمالاً با کاهش زرادخانهٔ تسلیحات آمریکا در بحبوحهٔ درگیری با ایران نیز مرتبط است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.87K · <a href="https://t.me/farsna/440028" target="_blank">📅 10:26 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440027">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🎥
پرتاب کفش و زباله روی سر کاپیتان اسرائیل
🔹
تیم فوتبال رژیم صهیونیستی در یک بازی دوستانه مهمان آلبانی بود که تماشاگران این کشور در جریان بازی با پرتاب کفش و زباله روی سر کاپیتان اسرائیل از صهیونیست‌ها پذیرایی کردند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.56K · <a href="https://t.me/farsna/440027" target="_blank">📅 10:05 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440026">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QbLYHFdfzElMKxpgGr9fR1q0UvzpADJwimN-Bqt30ncip5SbSQ70_ec4lgS--_zAC4ThSiprowBEHkVmccbljWG8M0G0mRg9hciG9-S4XaR_Eeyn6WJoBbuPakfxBmALCK2dfbBHQd0ZOs572Mn0hcSc4WxsQKhOqtecQLlwquQekbhY69NB8fhA6LJQDGEO8m9ZWQLNESmn8PhBHHkfF1V_vyI9ZMaZ3GsaOsNlUJC5mF6w_XyLRnT3M_2il4rLnIOCJcIpynYwzGv03Qqd-_UcUTWu7FUob8kuNj3oZZr9E5hWKRa0HWAFzCEvpp3NIaQKFrIQI-AA1hWQ5DtqHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس‌جمهور چین بعد از ۷ سال به کره‌شمالی می‌رود
🔹
دولت کره‌شمالی اعلام کرد که رئیس‌جمهور چین به دعوت کیم جونگ اون، رهبر این کشور در روزهای ۸ تا ۹ ژوئن (۱۸ و ۱۹ خرداد) به پیونگ یانگ سفر خواهد کرد.
🔹
این سفر در شصت‌وپنجمین سالگرد معاهدۀ همکاری‌های چین و کره‌شمالی انجام خواهد شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.82K · <a href="https://t.me/farsna/440026" target="_blank">📅 09:54 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440024">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WZVI59YVZ9FG8Hp2KQ9iiAZbeL6hsw_HUbmO0NixguNqTnFhvWSstBlxQl6RKS-yxgiUwz2pW9X2t-IbfJ_l3yJV-KUClLGJbKNFb723VD-uQWNmfwVSUSQrPJdSIcSHSuaHzPBPLrBEu6kcYXLu1QbZRyvHKxa1a6Q-P6hxWWb4VPdXmenUNd3Z_4_3tGgcD05HO2d445X6x-kparoNEFEidRZAiXvqwZA3B0zvsIHTrARavPbqwRJUO7wmKI_bLqV6yFLwWKzekY3EnKkeDMS82UKuIZmcov-wfvIp3zbbv-ZbMMjpdknNCV0w7lQexKDVl0B-TvNLjlgImTLeMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توقف بارگیری نفت در یکی از بنادر عمان
🔹
منابع مطلع امروز از توقف بارگیری نفت در یکی از بنادر عمان خبر دادند.
🔹
خبرگزاری «رویترز» به نقل از این منابع که نامشان را فاش نکرد، گزارش داد که بر اثر وقوع انفجار در تأسیسات نفتی در «بندر الفحل»، بارگیری نفت عمان متوقف شده است.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/farsna/440024" target="_blank">📅 09:18 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440023">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be0b06c1a4.mp4?token=aqp6XvsMP0XvciFpt31ycStrepWvLtFql1TIE04HEyOWrAN8IVjQ25Qn7wAeNw0Tw8m0M2ts0Aym_hGZMcfg9vqlaxL1nkKICtQ3VLtA0uU8p8Bx5f2IKEnW55Hq90V_aOFReMbb61ThqWHBw38YvvLY1WdAPLOg4IVcCm1RvK3Mg5JXBCrmL9rFNLyBgQK3raKyOwTCDiaPiFiKkRcXvoqAdFvCn9vhaEK3KccP5skUrUrLyQBMLQek_Vlwaf9fsibKDnp_PlEuYbaUtvJD7VVzPXI4rxrPlX7-M2OYKtk6u9v2R9zRG7QjFhUIS_kSTsuYUlSFaoRUS5PmCG3rGkMVh8mRo0whDUc-2tBkb8XPhF_65JtbsKzDxMX1yH4BzYJe6t-na8pnFmsfuZSLTdksa7-sx5v9CVmZJY3gIpZWgPF1hUdGGdeSMlGlYQjx30cmt2itVnxTf5K2TVM-wULNY6sjgsnk5TJWINtEIe5SyJv3WM4Dmo6jZ5_Iamen7lGG0ng12EcSEHYrvYsYh9NnDMCVUqTpf_BeSESCueJyhcpRYR6MJq4O3jvGgta7r9_9uz_Yc5ralJkbSlArskM3FmQgOXDoo7-A8U2WHiPrDocSX-87_XD1g8Kr_qGD5etSMMgTsVOm9PIkq9zIfH9C5V2L9BNwy6K44X2Q9ck" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be0b06c1a4.mp4?token=aqp6XvsMP0XvciFpt31ycStrepWvLtFql1TIE04HEyOWrAN8IVjQ25Qn7wAeNw0Tw8m0M2ts0Aym_hGZMcfg9vqlaxL1nkKICtQ3VLtA0uU8p8Bx5f2IKEnW55Hq90V_aOFReMbb61ThqWHBw38YvvLY1WdAPLOg4IVcCm1RvK3Mg5JXBCrmL9rFNLyBgQK3raKyOwTCDiaPiFiKkRcXvoqAdFvCn9vhaEK3KccP5skUrUrLyQBMLQek_Vlwaf9fsibKDnp_PlEuYbaUtvJD7VVzPXI4rxrPlX7-M2OYKtk6u9v2R9zRG7QjFhUIS_kSTsuYUlSFaoRUS5PmCG3rGkMVh8mRo0whDUc-2tBkb8XPhF_65JtbsKzDxMX1yH4BzYJe6t-na8pnFmsfuZSLTdksa7-sx5v9CVmZJY3gIpZWgPF1hUdGGdeSMlGlYQjx30cmt2itVnxTf5K2TVM-wULNY6sjgsnk5TJWINtEIe5SyJv3WM4Dmo6jZ5_Iamen7lGG0ng12EcSEHYrvYsYh9NnDMCVUqTpf_BeSESCueJyhcpRYR6MJq4O3jvGgta7r9_9uz_Yc5ralJkbSlArskM3FmQgOXDoo7-A8U2WHiPrDocSX-87_XD1g8Kr_qGD5etSMMgTsVOm9PIkq9zIfH9C5V2L9BNwy6K44X2Q9ck" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
چرا اسرائیل به‌دنبال اشغال بخشی از جنوب لبنان است؟
🔹
امانی، سفیر سابق ایران در لبنان: رژیم صهیونیستی توانایی ادامه اشغال بلندمدت مناطق جنوب لبنان را ندارد. در گذشته نیز با وجود اشغال بخش‌هایی از جنوب لبنان، در نهایت به‌دلایل مختلف ناچار به عقب‌نشینی و ترک این مناطق شد.
🔹
نتانیاهو تلاش می‌کند با اشغال برخی نقاط و روستاهای مرزی، این اقدامات را به‌عنوان تضمین امنیت شهرک‌های شمال فلسطین اشغالی و نشانه‌ای از موفقیت خود به افکار عمومی ارائه دهد.
🔹
اشغال چند روستای خالی از سکنه دستاورد نظامی محسوب نمی‌شود و بیشتر ناشی از نیاز سیاسی نخست‌وزیر اسرائیل به نمایش پیروزی است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.81K · <a href="https://t.me/farsna/440023" target="_blank">📅 09:15 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440022">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">کالابرگ دارندگان کدملی با رقم پایانی ۰، ۱ و ۲ شارژ شد
🔹
وزارت تعاون: مرحلهٔ یازدهم کالابرگ الکترونیکی از امروز آغاز شده و حساب سرپرستان خانوارهایی که رقم پایانی کد ملی آن‌ها ۰، ۱ و ۲ است، در این مرحله شارژ شده است.
🔹
همچنین خانوارهای تحت پوشش نهادهای حمایتی و نیروهای مسلح نیز در همین مرحله امکان استفاده از اعتبار خود را دارند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farsna/440022" target="_blank">📅 09:03 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440021">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7dc1a27bab.mp4?token=da5sB3IdYlsKVH03XEAF_gLUwp9s8DMjYGSFASi-X8tWCDFWQNCcxm87jICKLepvwfS5HsaTExHZiWqfXGrjkhABGBcHkQzINt5v7lhSpvWhKw8h0Ot7v7hAsDRbxWb_BTyZWzDLtYMoTpOqqKEIABV0PAlGYmnY49Ut0mTbJN40FS434-ib3uxsL55UAwT4l3PHs4Czo1v1_wAcXi3SLCqrQ7zBOnfbYk9T8tHZiYsMi3JJvEK_9ZJkE__FgM8HeRL6L0s2tCu_sJcAsV1v4gMTF1r3vBq7Q3GR7R4ogEom9beXVVt2zkpyG8Msr7CJ8c6B01hBI-QuMKNBGu95UYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7dc1a27bab.mp4?token=da5sB3IdYlsKVH03XEAF_gLUwp9s8DMjYGSFASi-X8tWCDFWQNCcxm87jICKLepvwfS5HsaTExHZiWqfXGrjkhABGBcHkQzINt5v7lhSpvWhKw8h0Ot7v7hAsDRbxWb_BTyZWzDLtYMoTpOqqKEIABV0PAlGYmnY49Ut0mTbJN40FS434-ib3uxsL55UAwT4l3PHs4Czo1v1_wAcXi3SLCqrQ7zBOnfbYk9T8tHZiYsMi3JJvEK_9ZJkE__FgM8HeRL6L0s2tCu_sJcAsV1v4gMTF1r3vBq7Q3GR7R4ogEom9beXVVt2zkpyG8Msr7CJ8c6B01hBI-QuMKNBGu95UYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روزنامه‌نگار آمریکایی: این سطح از بی‌عرضگی در دستگاه سیاست خارجی آمریکا خیره‌کننده است
🔹
راگین: ترامپ نه می‌داند هدف نهایی‌اش چیست، نه راهبرد رسیدن به آن را می‌فهمد و نه خط قرمزهای ایران را می‌شناسد.
🔹
این جنگ بر پایهٔ دروغ راه افتاده و هیچ نقطهٔ پایان روشنی ندارد؛ این یک ننگ تمام‌عیار برای نیروهای ماست.
🔹
ترامپ تازه پس از سه ماه یاد می‌گیرد که دنیا آن‌طور که او دستور می‌دهد، کار نمی‌کند.
@Farsna</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/440021" target="_blank">📅 08:49 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440020">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lKZ5YiM7XNDaQ0sVH6B16TjRITaYNGoqCrodn7MhQ5K6XhAiF_BXAnJCnO5rXnurAdbXspqluc40a30rNggS3YDURkualzQy3-5RxqimLQ0Pt8WZ0kj5hReYMMopIX_wqbvsuPp5-T6gEPIWLsMtZgfy5ECYZXtz5kkNMtdG_3um5qmnMZnUn-D5QFbOjiZDHmTNtjH_JqfUtce801ojGDTtrivNUjE1PKsuUaha2gTXR-NNj920z3zaY3b8SdSLJKnEG0CFocd2lyQ8yKKHRc9gZhu6gEG7M4VQB1anmXVAA1NiGB8UbGFW-r9Ptn8hos-xRwJwVqIJ0yhaWC9Gaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عراق در سوگ آیت‌الله فیاض ۳ روز عزای عمومی اعلام کرد
🔹
در پی درگذشت مرجع تشیع آیت‌الله شیخ محمد اسحاق فیاض در عراق، دولت این کشور، سه روز عزای عمومی اعلام کرد.
🔹
در پی این ضایعه، «نزار آمیدی» رئیس‌جمهور و علی الزیدی نخست‌وزیر عراق  با صدور پیامهایی جداگانه،…</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/440020" target="_blank">📅 08:23 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440015">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/flRZFTcU27O_QmNyN_vdCpZM0E6KaCRQ1fjhbThaMKQxWs7lfqmz62iDD3ZcDQduljutllW9SjQSpt8K2ROREk6RbmKJhHp4lSr0cUxIcUp5Da1ht2DKr0zZtPq_7_xRtqWW-s356on9VOtvmp_eaEhYmyLEq12r9OFz5hFf6kY_xNVZQVEyVnrjjy0LWzg0rJGXLj0LMSwil_jjFjl31C3z4g6MPU6tH0dfsZ-mt4DlERN-ngXLIVeg3Ps-vTVswFVkrhUBkq3zJNmkKWVQYh6mZ229tkmBCGwkaOGfdg6kkZdoHVWaXhfvcylHWBiU7ToGJgb1UrC7ZwVcFiiz_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BINtwWlWVfIMj9pC-5SWqW8jDjC_5mPXvJmi4TZwt_l_Tc1jQ4fCYy2dWV5qQt-OwcTrKkjvbzeJGK_chIrHjtHMJ3DLphVRBBivm6Yfz_8oVulDmg9IVTiXe7aRGsKJMrj6kZJ4oIX2MV1F-a623g39QkV1q_34O1Ae-X1YiYCANDXa9RXU4S6QFuVPDuYv9GPXdsEvjMgFc2Qd4GN31a9VVor74hsRxJR6txq-zWUFexmJfqW9zdl7RsVaj_0C_T0s_qPap3xZJXYV7MbBettxlYM6c7tJg-zEBseYffcmEGNGLKO9S0dgfFcHUf5NbvNIUsyr5SglSUxe-W5YUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RH1QY6_Wp-7JKkC_4_KLF2WCyd-jsck1OkEMA9Yr6eG64OP2GF4-B5BGAP9IGeTvf0l_ZqQ537Zm6GkzeY0-bMT4gim2Q-WG9SXo490oH2xzncTD18BapynGYzGNP3Wsud28izKe-q__w5eoTSV4Bju7wCZgHHPWwz81hVBJqvZvjBagzV9_QP-QeP3-RtXMk8TXeN1u70OtuIWGkHSM-2AxJeyo_AfcbcULMQHZ6Lun5yrkhvTMHzaJ2s1sfKfd38y3HdB3Xq-hp5ALsdj013sw8rffiMpo8Jmk7rfcr4YizEjiakT84STK_6JYMsUrieSTcICGpjqtko1GsEDYGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PMjzRkLhUbEri3TgLO1RE4vTIJwPN-fcxhtAPhCI-beGWh201UfGA6quw_4nByCTePnEMBHQtMjwnwXsSli7zbIBYF5prnGvUJHdZzMcNAy8sXhvJcmh6pAWgmyIVXRlY5pcHxLRfeI92KsBQy6PAnXXQmH49lgMmFemfKK3_E0bUS88GiTEb6X3h8pg41-9sJopLWQ8Rync3-4Nem4RG7yyE2qPlN_33cVNEkPUsz0MU6okfJaDRn7gknhPN0e-Nv3a5QihAPWKTocEY3sJrMDwgjMafVsAauaLdj7cesV0hk-chhOyh7GyjFQ-4JZw0ejlBjKRCuu1Kd-e11qiWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/m8ai8dR9LPiUWDP0xpRJSCc4uzfSKu3lwPxp2nEKVbJQ5l1HU-D55HXhdufAYkl55asWQJq3OcuXWGFm5tFgNlueqvTTSOxYKgMWa-TB-6Hs_5hr1k-dIldiFYQnLcWSs3GAFsDFpQ29txb47yh05JI-cTq50f2PeP2MCHUXNCcTuCJyuIsBFPe4qcTa2CtpKnhQvSGAOSF7FRs2b9TN3Jrv9h_TWR8xHsfIXyV487ohqw2nFq50EtNPRaVdSB9G3r6whsIfjeDyr6QfVznPt0D-yskMdLym05Ns4SkqWsbZTsub2cC00aseSZpcZcsruyW12z1KsQlcmHRTXOFrAA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
حمله دشمن آمریکایی-صهیونی به حسینیه اعظم زنجان  عکس: عرفان تقی بیگلو  @Farsna</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/440015" target="_blank">📅 08:01 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440014">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u2NsBAOUp1qofqO58t0gGfzA0QVwPHxRPDIpzjp2YFVZ5J2zvbIUZXA8SKPB9yPYMWU1EgdnXt59ENi3V0MuKiFFq7rNGuwVw8Gjsv2PzrL4doImwjaiJbbfJvq0kmYvGJt2TiVpy49d8Erpev8QnUW5_xQkx25MExaP_hcXYH-MrDq_NjXt6HdArqDZ_MscNwZuom2jetfctRGGn9IOXd-if4ZrqbA3dfuMsFuAhQBUFa5jDOZ_7Pto63wZaN0INHDtasKiKcFty7IV2JQBJYYQNrBLVTMzo4YHl3iid0CtsXG64-nKkNokpSdleRrPUsJANydGTIgcR1EbeHgX2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امارات نیم‌میلیون صندلی هواپیما را حذف کرد
🔹
در تازه‌ترین نشانه از عمق تأثیر جنگ رمضان بر اقتصاد منطقه، شرکت هواپیمایی امارات مجبور شده نزدیک به نیم‌میلیون صندلی را از برنامۀ پروازی این ماه خود حذف کند؛ رقمی که معادل ۱۶ درصد ظرفیت پروازی این شرکت است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/440014" target="_blank">📅 07:47 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440013">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vsgpTPgbDf4BQcJjJmNoY_023LnwOe6GS2lgYON4DH4HYXMwlJwABwXzHcoCH-QhTQqBCHn78lfYgDCzPP_b0xTjHubvhX-ign-mTPxPn0n2ZRdmWoqcAaqcy1ADAaktF-FxpV90os6USPDwslhEzzkrfoJC5YBJD4IcHmkAG5OrVZSRZx4_J6NeZG_-zVKn0TziG3u1hW-JttDEfJn_d5cCNc5EbNbLZCB3iIyVm9G1rjeIz8PLyMoGT934RrOZc-u7sSIo6kN-8HYtcs53Y4CKfrKMJe-gzaeyfRUAbxcpzPhwsOQQoyiW59Q75UL7merhLsYs2xDCYvMY7QXYTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">راهبرد تدریجی حزب‌الله برای از رده خارج‌کردن گنبد آهنین
🔹
در حالی‌که طی سال‌های گذشته سامانۀ گنبد آهنین به نماد توان پدافندی ارتش اشغالگر در برابر راکت‌ها و پهپادها تبدیل شده بود، شواهد موجود نشان می‌دهد حزب‌الله راهبردی تدریجی و هدفمند را برای تضعیف این سامانه درپیش گرفته است.
🔹
برآوردها حاکی از آن است که تنها در ماه گذشته، بین چهار تا پنج واحد از سامانه‌های گنبد آهنین هدف قرار گرفته و از چرخۀ عملیاتی خارج شده‌اند. با توجه به اینکه اسرائیل در مجموع حدود ۳۰ تا ۴۰ واحد از این سامانه را در اختیار دارد، چنین میزان خسارتی قابل توجه است.
🔹
همچنین یکی از مشکلات ساختاری گنبد آهنین، هزینۀ بسیار بالای رهگیری در مقایسه با هزینۀ حمله است. هزینۀ شلیک یک موشک رهگیر چندین برابر هزینۀ ساخت و پرتاب یک راکت یا پهپاد حزب‌الله است.
🔹
همین مسئله سبب شده تا اسرائیل به سمت نابودی زیرساخت‌های پرتاب موشک و پهپاد حزب‌الله برود تا به زعم خود به جای ره‌گیری مدام پرتابه‌های حزب‌الله، اساسا مانع شلیک آن‌ها شود، اما این راهکار نیز در عمل جواب نداده است؛ چراکه حزب‌الله طی دو دهۀ گذشته شبکۀ گسترده‌ای از تونل‌ها، پناهگاه‌ها و مواضع زیرزمینی ایجاد کرده که امکان پنهان‌سازی و حفاظت از سامانه‌های موشکی را فراهم می‌کند.
🔗
شرح گزارش کامل را
اینجا
بخوانید.
@Farsna</div>
<div class="tg-footer">👁️ 9.94K · <a href="https://t.me/farsna/440013" target="_blank">📅 07:28 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440008">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EJZ6ub2UaFYPrbmTVk2XJXFmU3T6_OSV1N1OtUSSUVckagIXL6bLCFCA_jq5RQ7sAGPBvRrWSHbGL4BEXK2gLarVDa-1c31w9CSle8Gw7OC_B_K_oQTzUM4PrAMVsXPTUEIBp1VJwuECAzzpuEYTEy2I2Ek6hwiZrROJ3IcevBt6dtUtqciCyRWVGuqBWi3R3Vz9-wWBMdba0Jy9D8R0eOKODsj0Gz3M0tE0z68a_4qc8S6mBvhujGn2tVAEyq9XQX04BnGLpaUtlBmSpB4zR0geWOWlc0Inzsu-03OEE9XVIegQiwNTHOlcrkrvnjmw6slv_tS1B2w3NTlW4BcjzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Yf3i2jX5HC9o1l35eWCuvznYmg114ZWgquUCgvQIYqbvmb8t8ptfSiTUHMmib2zIHSuT_1enrABq9B8mpIf3hCaaYKhvZRlO0ZUC3Hq1pnjpyql54mOatakNvO87ykPr7jtlLIpIwV7_GupntpU3Q6QH1qnXQYH9yZb8sv9C4IXaHVBx0PUAppGCnjpbUGgCp2iFfxexnFSVV7TCioySJO-fLoCxTw2lvVW74yOdxX7CzNyi8hREtUESy1ua_fE1HJ3-6JM1Lh-p8oaF9MeW7aG6OVKnuo06_wz12662E-zzjYjB8hobSSVCqwrOWWd02YYsIEOangiPIUKeNKUfmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tQKZ67LBKk8Vpq6b6bvXdOBSwWzyQvMcB2aMjUISkKdYVsfC1w7A5_tZkE8vuMYBAxF3LpJDTzN807egw6vYrlmw8w5rNIQbCVj0CTkOYL90cxu65cRU783vE-LN9c5gtfDx2vTFNb-J5BwO5a063Z7CcQvRZS1S4M-XxOHg2jHblYJ7MMr-gRnYNB9FasdwP-mDAMDrtdvFDwXIZx5pUvV5O23_yzCkaYeHyLrwSsMuEmuBg29ALvL-0HTd8im2YduSjbG-Jo3kGjI7VxIkaIRllmoJ5Iu7HUv9hJdWY0uEDuSppa7l6CcCQjDhw6kc4tqUQxaxZnmVgp854WbWMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/i_Wf8YTpns7Hvx3LTZ4bZyMqoo2zH7q9-yqGuBpt-2XEDXWSaxnZ91tq6Vu3cgFFtNLGeM1CtRnz_q61QnZSYrXfTNg9vsYKualXG0fdsNir4spMkMOtjclanickOZfs2lp3qTJvUHVr8tcdJxA1Np4btSRWfRJ6kpNlEAEoLN3kXX7FIfJqUnYBN-OVCKkVqe0cXZBT3kwITwmUkuHl7LzLM7a4FmQVNLSyf-i2zxhWL7DhsHaFyGR8o3EoYVR1iGGs2SPpt9hgXzdWiq-39SXTJZ1mHmLsYlokGTIc1S-9RnMDqG5SjlRLTA6VELkVIKxk18UzNp7j716HVYmXew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sScpu9wre2q3oPI2Vr-gZ4QxUouZUGpcgwMGtGMXcJsMvZ47vOZtLgBv0ecNgR4_m_faszX1sMWPiOHn5D-5ytPcNxd1FPRe5epp_u3eeL0cuc7ym-i2iAnJUvwVkXCJ7d9xRaHeewz1eIzQfjxUT7xrfpJu6nIDwuN3TcMMoX0Rm3vm445jkCFoiGrCHQa_DDrpFfL86Qz_Gqv7FXss4vedGavYNab8TVapbnS3bC7wwoZNSd4-ouHv4kq9C-4P02qJYHCgZIPCLKH5dCcexH-6oa-Wue_yZ7DikXP69iCo4nnVUhJtzJvqaoFk5NYUtxmTBG0hOkUDMtimb3744A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
راهپیمایی بزرگ عید غدیر در زنجان
عکس:
عرفان تقی بیگلو
@Farsna</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/440008" target="_blank">📅 05:25 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440007">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس هنر</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KLhUQnV1ifzzTSvjxUYFdhSHfbtzQZO3LrQNTq1lHReU7UiPKSfL0ogF8sI2aUxXY1bAn3G6pm8B1GrwKP-jfb1S_XUPoZPCVVQET_TiSMuE-3906-jTIr9YTYV9Hu0Sx1zyPIZKEzIzoHo_-AK6rWrJg5yTqDHABPgE4cd_ikEXeVSt1cno8a31CwXHdmKq4cMsFx4l6rpCL0VuEOV8i3HKD0oXAGBZ3N5t7xYfgf3eFKjhPaD8fcUlExjltd9WdS9qFduFe_i2gUAnod8I7HKmcSKLLVREmdQRvmtqGBZ1_I0pDScC8QC4KssOpMs8m6uua8BuHUoifwSgkBvl_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روایت رسانه‌های غرب از مردی که شاه را سرنگون کرد
🔹
رحلت امام خمینی(ره) برای بسیاری از رسانه‌های غربی تنها یک رویداد خبری نبود؛ بلکه فرصتی بود تا بار دیگر روایت مطلوب خود از انقلاب اسلامی و رهبر آن را بازتولید کنند.
🔹
این روایت‌ها با تعابیری مثل «کشیش سیاسی» و «چسب افراط‌گرایی» تلاش کرد انقلابی را که با مشارکت گستردهٔ مردم به پیروزی رسیده بود، به عنوان حرکتی افراطی و بی‌ثبات‌کننده معرفی کند.
🔹
مرور گزارش‌های رسانه‌های غربی دربارهٔ رحلت امام خمینی(ره) و انتقال رهبری در ایران نشان می‌دهد بخش قابل توجهی از این روایت‌ها از زاویه‌ای سیاسی و جهت‌دار شکل گرفته‌اند.
🔹
استفاده از واژگان ارزش‌گذار، انتخاب گزینشی رویدادها و حذف بخش‌هایی از زمینهٔ تاریخی، از جمله ویژگی‌های مشترک این بازتاب‌هاست.
🔗
گزارش کامل را
اینجا
بخوانید.
@Farsnart
-
Link</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/440007" target="_blank">📅 04:15 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440006">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">حملات گستردۀ حزب‌الله به مواضع و خودروهای زرهی رژیم‌صهیونیستی در جنوب لبنان
🔹
به گزارش المیادین، حزب‌الله اعلام کرد شب گذشته یک تجمع از خودروهای زرهی و نظامیان ارتش اسرائیل در منطقۀ «الغندوریه» را هدف قرار داده‌ و با انفجار خودروهای زرهی، تلفات قطعی به دشمن وارد کرده‌اند.
🔹
حزب‌الله همچنین اعلام کرد که یک تجمع دیگر از خودروهای زرهی و نظامیان اسرائیلی در محوطۀ قلعۀ تاریخی «الشقيف» را با یک موشک نقطه‌زن هدف قرار داده است.
🔹
در بیانیۀ دیگری، حزب‌الله از حملۀ موشکی به یک تجمع از نظامیان اسرائیل در منطقۀ «القنطره» نیز خبر داده است.
@Farsna</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/440006" target="_blank">📅 03:58 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440005">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس معارف</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e370b5f25.mp4?token=TJA6Svz1QXbm8bZIKTmY-gt_jlRj0ASHVP7eSPITlbNXJi2VmeYTVBGMKeicMSg8cV-CYMACoXbNPAUfCQw8oeyqmTttkpUn9vPNvs9S1Ki6CQQokb3y7VeRqFkRojVK5mtTALGHji-MXJ8Gs_ZnY3XK0Zydc3kzGjDL4ESnNgx65B8bdK_QS0tU7hqazrIpf_GaaU-s1OvCljGgKaZQRJ8PrMvH_WSM_HBZSIgKAgNzB07HDGMjzw_YkQ7XUFyR9Ox2aRzqR-CdQxEPokDbfRHpS8dOvvpyCWcmwwEfOh2KRLK4w9eyPRNrb_mgmf9YqVao22jjUxINNnhV0wXBX0DJP9_UNhUZq5g3BSlVWEzLr0ciesUAbfy-nPQqUvjVzCRFM8cPI_YlAljLSD0dDGpd9sYuQ_0Fov5mFLcGpV-RHlG8GRYz9caEkn2fMRy5RP4larjV_AHLFcIY2BgLhjFfi4tS3LbaMw-5mmJbU8uxAUh-3JDHoV8iV_-7dN9LjeovEjEvjv0aPEfPMzNCWB37qZyt3ONiii0PkQ33Sw5cSy3al8MqyXZdIoWuAa4LRqqYpOo7ZEcQFwYPO9gTfpAMtmxIMpH3BR3YYXsfrS89VQJpp8OCmTwW4HSuPRNBjSx3Ac_5Z6o63JmIqIXOZTNs72GnTZSNTMd5MybOJt8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e370b5f25.mp4?token=TJA6Svz1QXbm8bZIKTmY-gt_jlRj0ASHVP7eSPITlbNXJi2VmeYTVBGMKeicMSg8cV-CYMACoXbNPAUfCQw8oeyqmTttkpUn9vPNvs9S1Ki6CQQokb3y7VeRqFkRojVK5mtTALGHji-MXJ8Gs_ZnY3XK0Zydc3kzGjDL4ESnNgx65B8bdK_QS0tU7hqazrIpf_GaaU-s1OvCljGgKaZQRJ8PrMvH_WSM_HBZSIgKAgNzB07HDGMjzw_YkQ7XUFyR9Ox2aRzqR-CdQxEPokDbfRHpS8dOvvpyCWcmwwEfOh2KRLK4w9eyPRNrb_mgmf9YqVao22jjUxINNnhV0wXBX0DJP9_UNhUZq5g3BSlVWEzLr0ciesUAbfy-nPQqUvjVzCRFM8cPI_YlAljLSD0dDGpd9sYuQ_0Fov5mFLcGpV-RHlG8GRYz9caEkn2fMRy5RP4larjV_AHLFcIY2BgLhjFfi4tS3LbaMw-5mmJbU8uxAUh-3JDHoV8iV_-7dN9LjeovEjEvjv0aPEfPMzNCWB37qZyt3ONiii0PkQ33Sw5cSy3al8MqyXZdIoWuAa4LRqqYpOo7ZEcQFwYPO9gTfpAMtmxIMpH3BR3YYXsfrS89VQJpp8OCmTwW4HSuPRNBjSx3Ac_5Z6o63JmIqIXOZTNs72GnTZSNTMd5MybOJt8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ماموریت مردم ایران در آخرالزمان چیست؟
@FarsMaaref
💠</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/440005" target="_blank">📅 03:36 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440004">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uVUoEteBxwrDFNVCNBdWVY40VuHprAySncEdWlZdaUeRoa_SXU4PJRbiU0c-dYCMvzTE8hxI8nYRnBkMOZ4lwUFEmhd15FOJdtDGmmfYyXdxYGSnAPTkaTSau8eK2NqrxuCld6m7ftHqHp-uy6Ckd64uJ2aM7mm_SJtfIxsxm9hbQixFx8qaiMpeZ1bzfkoRHPt1QHN718JmVX4Pu22yAdvqsvarshyWFL2HnzGH8Dz5Da0Q-nULxNoNl3fKzUUuBdNgstLXMGFmfa4dVPR5xz4AHgua4nVv_fmOc2tMCpCvub88Ifn_TwTcocdsAYseqIkd2xl0bcqxbKrL8OkYCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طرح ناکام ترامپ برای تسلیح کردها در جریان جنگ رمضان
🔹
در حالی که رئیس‌جمهور آمریکا دونالد ترامپ به تسلیح کُرد‌ها به منظور اقدام علیه ایران اعتراف کرده، رسانه صهیونیستی روز پنجشنبه گزارش داد که موساد نقش عمده‌ای در این طرح بی‌ثمر داشته است.
🔸
جروزالم‌پست به نقل از مقامات اسبق موساد گزارش داد که واشنگتن با توجه به تجربه جنگ عراق در جریان تجاوز نظامی اخیر در ایران به دنبال طرحی بود تا نیازی به اعزام نظامیان آمریکایی به ایران نداشته باشد و از این رو، قصد حمایت نظامی از کُرد‌ها و تشویق آن‌ها برای حمله زمینی به ایران را داشت، طرحی که در نطفه شکست خورد.
@FarsNewsInt
- Link</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/440004" target="_blank">📅 02:49 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440003">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/07c3f17a4b.mp4?token=BmIjwf94gWTVPMktwNVQR2yxzvUBTqrHpH22Bp87n0u-Z-BIVOAdUaIWg7p15t9qjlBrq23vsOm5-JSUS-nrNP7-Z8FaO8wdPJM_Sf7yGpC_eXa8YNANkQOlr1oBOZujpkEwuXOQaE7y9w3SYXq-wHDWeiylhUhMedcDtpIU-zuYTTZm4rztUE127YUBCCkr1BpUBihI_FEq_G3iOa4ITBstsCsaZJQ22MlQ3HTChHCMv7QluzoPyTgBLFcdubQ_l-OGwG6Vrmi-AzQWDEZTQSIW01yyhWR_6JA_Z4pfNcbHNS355Yqj0idqyFutlJiOcooUgdPX1PGiKPLwAmEV9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/07c3f17a4b.mp4?token=BmIjwf94gWTVPMktwNVQR2yxzvUBTqrHpH22Bp87n0u-Z-BIVOAdUaIWg7p15t9qjlBrq23vsOm5-JSUS-nrNP7-Z8FaO8wdPJM_Sf7yGpC_eXa8YNANkQOlr1oBOZujpkEwuXOQaE7y9w3SYXq-wHDWeiylhUhMedcDtpIU-zuYTTZm4rztUE127YUBCCkr1BpUBihI_FEq_G3iOa4ITBstsCsaZJQ22MlQ3HTChHCMv7QluzoPyTgBLFcdubQ_l-OGwG6Vrmi-AzQWDEZTQSIW01yyhWR_6JA_Z4pfNcbHNS355Yqj0idqyFutlJiOcooUgdPX1PGiKPLwAmEV9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تصاویر جدید سی‌ان‌ان از آتش‌سوزی در ناو جرالد فورد؛ پنتاگون پنهان‌کاری کرده است
🔹
تصاویر جدیدی که سی‌ان‌ان به آنها دست یافته نشان می‌دهد ابعاد آتش‌سوزی دوماه پیش در ناو هواپیمابر «یو‌اس‌اس جرالد آر. فورد» به‌مراتب گسترده‌تر و بحرانی‌تر از روایات رسمی پنتاگون بوده و عملاً توان عملیاتی این ابرسازۀ نظامی را در اوج درگیری با ایران مختل کرده است.
🔹
درحالی که نیروی دریایی آمریکا در زمان حادثه با صدور بیانیه‌ای کوتاه مدعی شده بود آتش‌سوزی به‌سرعت مهار شده و ناو «کاملاً عملیاتی» است، اسناد جدید فاش می‌کند که این حریق توازن عملیاتی ناو را به‌هم زده و سیستم‌های دفاعی و اطفای حریق داخلی آن کاملاً از کار افتاده بودند.
🔸
تصاویر به‌دست آمده توسط سی‌ان‌ان، ویرانی مطلق بخش آسایشگاه و تخت‌های استراحت ملوانان را نشان می‌دهد.
🔸
سیم‌های آویزان از سقف‌های فروریخته، اسکلت‌های فلزی سوخته و تغییر شکل‌یافته تخت‌ها در میان تلی از خاکستر، تصویری از یک جهنم واقعی را در داخل این ناو ۱۳ میلیارد دلاری به نمایش گذاشته است.
@Farsna</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/440003" target="_blank">📅 02:19 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440002">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">مشارکت استارلینک در کشتار مردم ایران
🔹
رویترز به‌تازگی افشا کرد که ارتش آمریکا برای هدایت پهپادهای انتحاری لوکاس به شبکۀ استارلینک متکی بوده است. این درحالیست که آمریکا و رسانه‌های مختلف، مدت‌هاست بر روی ارائۀ استارلینک به مردم به‌عنوان ابزاری برای ارائه دسترسی…</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farsna/440002" target="_blank">📅 02:03 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440001">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🎥
موکبی با ۱۱۰ هزار پرس چلوکباب
🔹
موکب مائدۀ غدیر ۷ سال است که در روز عید غدیر ۱۱۰ هزار پرس غذا توزیع می‌کند. تمام هزینۀ این غذاها توسط مردم تأمین می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farsna/440001" target="_blank">📅 01:37 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440000">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">حزب‌الله دیروز چه ضرباتی به صهیونیست‌ها زد
شکار پهپادها
🔹
مقابله با ۴ پهپاد پیشرفته هرمس-۴۵۰ ارتش اسرائیل در آسمان نبطیه، وادی الحجیر، بخش غربی و کفرملکی-جباع و فراری دادن آن‌ها.
انهدام زره‌پوش‌ها
🔸
انهدام کامل ۶ دستگاه تانک مرکاوا در محوطه قلعه تاریخی شقيف به وسیله موشک‌های هدایت‌شونده و کوادکوپترهای انتحاری «ابابیل».
حملات پهپادی و موشکی
🔹
هدف‌قراردادن پایگاه‌ها، مقرهای فرماندهی و مراکز پشتیبانی جدید اسرائیل در مناطق «قلعه شقيف»، «یحمر الشقیف» و «تله العویضه» با چندین فروند پهپاد انتحاری و موشک‌های کیفی.
هدف‌گیری تجمعات صهیونیست‌ها
🔸
موشک‌باران و حملات توپخانه‌ای سنگین علیه تجمعات نظامیان و خودروهای زرهی اسرائیل در مناطق مرزی از جمله القنطره، رشاف، الخیام و یحمر الشقیف.
@Farsna</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farsna/440000" target="_blank">📅 01:12 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439998">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">هلاکت یکی از اشرارِ جنوب سیستان‌وبلوچستان
🔹
به‌دنبال رصدهای اطلاعاتی و کشف محل اختفای یکی از سرکردگان اشرار مطرح منطقه در حوزه جنوب سیستان‌وبلوچستان توسط حافظان امنیت، یکی از اشرار با سابقهٔ این منطقه به هلاکت رسید.
🔹
در این اقدام عملیات مقادیری سلاح و مهمات مربوط به شرور مذکور کشف و ضبط شد. شرور معدوم دارای سوابق متعدد ضدامنیتی بوده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farsna/439998" target="_blank">📅 00:46 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439997">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XrCtCeoyxTqD6z_hAOpT4hANBJjtbhOt09Mzb1ipy4dcEDNd7vjuhM5kNkRu2gYhUPDOCxiOabHtypaDQPyJ3SLpW0w05vXhjqU3kNKrN7rdZDriYyN_ADy9d6CHsqndR39RGHycxydyZiP-yfX9JdiTYjgdjftvE50_ET7QmzLOZsbJ6iISyyZ_jY881jBt0i2LpXSoqVPbig1u9q68jTEquV9zvQ3f2zcFaFqQPZApOgvuiQV0uVmRLsrod9UIWngeJTMumOFFw3KbXAjmIHGiIRzgYE5COGH_j0QNxa8uy5hFK1r-mnEHzsD6yVymQ72LngDIr4PVIELD5oVJFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این دیپلمات کوبایی گفت: جنگ اقتصادی که بیش از ۶ دهه پیش تحمیل گردید، در ماه‌های اخیر به طرز بی‌سابقه‌ای تشدید شده است.</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farsna/439997" target="_blank">📅 00:37 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439996">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-text">اعتراف ترامپ به شکست طرح ربودن اورانیوم از ایران
🔹
رئیس‌جمهور آمریکا دونالد ترامپ درباره طرحی که آمریکایی‌ها برای ربودن اورانیوم غنی‌شده از ایران داشتند گفته که جابجا کردن مواد هسته‌ای مستلزم حضور در مناطق درگیری به مدت یک تا دو هفته بوده است.
🔹
او گفته که ایالات متحده به همین دلیل آن طرح را پیش نبرده است.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/farsna/439996" target="_blank">📅 00:19 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439995">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aac8ba4aaf.mp4?token=hH2ERSDnNv4Vf_22CJpNDC0bc6K4_RkIm5czLnDgtBn99DiBNhGK3g_yITU8CFFBcrienqVa5VGE4VHhMTlVSV4cmG_hb88c4nrNZKH4VoXmlXlYGGA30wxLtwh24IgjdnZ-9R9ZXDe0KE8KLWIDizDjsYYsNFPRuGnQPbtQ7jq7CAQ5FOesdT7tH64XPv3x9eh-y_qSxXvyFKZjO_rO45aij2C5PXPtTzT4t8ZMIJWVIRaDJbJqqeK5bUS0oOu7bbpN8odEpro6aOqf72QrW_Y4T75HoOOh5QnRpmflEM38NR1c-jIhPvHpO5l5spyjRMZO-UqbJ46okeTU_btn-SLLNb6ZJqXPODiANpUYN4mZT6KixpLFVO6xeY-6pPGftLRJN51pF2yeXY1EJpKgujY_WLp7XTSgSzd1QUGWp3rQBB3zEucDHQmWAYiuO07DyxhK18IxtpCcsTPu0iuwnT0iMEKCWpAkNUen0n52SbrR2coebHoQMl3x9sthgP0KPlGm_pB8GigaUQ31W9hh3KJdELTHwzsBchCG8tSsQ51GCbodSBYY5pXX3e94QMpF8SxXaWj14e2jrtXLLJIMRIO_Xr7Qw_jNv2kF8EgE6CLxXRtj2ZPzNVEgpHAvIvWTpk6JcybRN64MSCDK62UANCOXHyvC30figsChdt3tWNI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aac8ba4aaf.mp4?token=hH2ERSDnNv4Vf_22CJpNDC0bc6K4_RkIm5czLnDgtBn99DiBNhGK3g_yITU8CFFBcrienqVa5VGE4VHhMTlVSV4cmG_hb88c4nrNZKH4VoXmlXlYGGA30wxLtwh24IgjdnZ-9R9ZXDe0KE8KLWIDizDjsYYsNFPRuGnQPbtQ7jq7CAQ5FOesdT7tH64XPv3x9eh-y_qSxXvyFKZjO_rO45aij2C5PXPtTzT4t8ZMIJWVIRaDJbJqqeK5bUS0oOu7bbpN8odEpro6aOqf72QrW_Y4T75HoOOh5QnRpmflEM38NR1c-jIhPvHpO5l5spyjRMZO-UqbJ46okeTU_btn-SLLNb6ZJqXPODiANpUYN4mZT6KixpLFVO6xeY-6pPGftLRJN51pF2yeXY1EJpKgujY_WLp7XTSgSzd1QUGWp3rQBB3zEucDHQmWAYiuO07DyxhK18IxtpCcsTPu0iuwnT0iMEKCWpAkNUen0n52SbrR2coebHoQMl3x9sthgP0KPlGm_pB8GigaUQ31W9hh3KJdELTHwzsBchCG8tSsQ51GCbodSBYY5pXX3e94QMpF8SxXaWj14e2jrtXLLJIMRIO_Xr7Qw_jNv2kF8EgE6CLxXRtj2ZPzNVEgpHAvIvWTpk6JcybRN64MSCDK62UANCOXHyvC30figsChdt3tWNI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قاب‌هایی از مراسم سی‌وهفتمین سالگرد ارتحال امام خمینی(ره)
@Farsna</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/farsna/439995" target="_blank">📅 00:14 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439994">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">۸ شهید و ۱۵ زخمی در حملات رژیم‌صهیونیستی به جنوب و شرق لبنان
🔹
وزارت بهداشت لبنان خبر داد که طی حملات هوایی رژیم اشغالگر به شهرک‌هایی در جنوب و شرق لبنان، تاکنون ۸ نفر شهید و ۱۵ تن دیگر زخمی شده‌اند.
@Farsna</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/farsna/439994" target="_blank">📅 00:12 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439993">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8cc273f3a3.mp4?token=q2fah2bV52Hc9MNxXxxOcr84qsiLC1Anw8UYfNBcE1EQNuG9DmwkJXjixAKTWnm_r-WeEcsY-4mfDf0-lXDRhrjk9sgiFrXlnBZBTx7Iz4XijedrbwGNRgbnasLNIMLVMP2VE8_20iY_ydrOULPR0WG0mWw1-JTz3JUk-jmB5DESfSTkZ0OKTN4Dgj0nLhufeBzmJCH-JS4Og0UWZFofKaELDUc5d_OORwZt5iXrTOtnYkh8jAXGV-TiTR-as0izfNMJyXxiBY1P-LOaICyhzfABMJFcJ63t9JXTHuR1tYPouFHL7VXhpvs1hi3Y56wlMwxlBkeauPqWLB8tf8pAoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8cc273f3a3.mp4?token=q2fah2bV52Hc9MNxXxxOcr84qsiLC1Anw8UYfNBcE1EQNuG9DmwkJXjixAKTWnm_r-WeEcsY-4mfDf0-lXDRhrjk9sgiFrXlnBZBTx7Iz4XijedrbwGNRgbnasLNIMLVMP2VE8_20iY_ydrOULPR0WG0mWw1-JTz3JUk-jmB5DESfSTkZ0OKTN4Dgj0nLhufeBzmJCH-JS4Og0UWZFofKaELDUc5d_OORwZt5iXrTOtnYkh8jAXGV-TiTR-as0izfNMJyXxiBY1P-LOaICyhzfABMJFcJ63t9JXTHuR1tYPouFHL7VXhpvs1hi3Y56wlMwxlBkeauPqWLB8tf8pAoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سرلشکر رضایی: اگر امارات و کویت با صهیونیست‌ها همراه هستند باید ابوظبی و بوبیان را به عربستان و عراق بدهند.  @Farsna</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farsna/439993" target="_blank">📅 00:02 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439992">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5d5ac33ac2.mp4?token=U2NyX-NaxERSN9az-xjcTzFxG4AxvoT_yaicgThgpHPyf2B8bFVQowXdwMp5mjJUXRe7BmGZ0vPtLfMFYwWUWkm2geFEG9s7Qd6fEeKjNHTFeJSVDm5jLxWKlan9-A-QDzmrzu5UcKXb4IBpgjWOdlwtiqIdvZ_7jxqV93mGn-eWN2vEmP19V0cPreqrTDotfd7CKepCEjAjDPbENDL4b7ohKo5v0w2JIsLHzhwOtADfnIKX-WWKJqpV3vTSGHI_qicmL4T_FCBgFhZD8EClbMqWegOrKTznCR2byqMP3KoYwVQrYjY_J5VUODE1byHC-bvX5AKaSmEkq5YBborJWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5d5ac33ac2.mp4?token=U2NyX-NaxERSN9az-xjcTzFxG4AxvoT_yaicgThgpHPyf2B8bFVQowXdwMp5mjJUXRe7BmGZ0vPtLfMFYwWUWkm2geFEG9s7Qd6fEeKjNHTFeJSVDm5jLxWKlan9-A-QDzmrzu5UcKXb4IBpgjWOdlwtiqIdvZ_7jxqV93mGn-eWN2vEmP19V0cPreqrTDotfd7CKepCEjAjDPbENDL4b7ohKo5v0w2JIsLHzhwOtADfnIKX-WWKJqpV3vTSGHI_qicmL4T_FCBgFhZD8EClbMqWegOrKTznCR2byqMP3KoYwVQrYjY_J5VUODE1byHC-bvX5AKaSmEkq5YBborJWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سرلشکر رضایی: امیر قطر و ولی‌عهد عربستان دارند خودشان را با واقعیات تنظیم می‌کنند
🔹
اما امارات، بحرین و کویت همچنان فکر می‌کنند قدرت آمریکا مثل قبل خواهد بود. این‌ها فکر نکنند که اگر این روش را ادامه دهند ما بعد از جنگ رهایشان خواهیم کرد.  @Farsna</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/farsna/439992" target="_blank">📅 23:53 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439991">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8c4bba7fa3.mp4?token=S9M1sZVMVl2Hx6OjmmXhIOiwYDqhrZ4y3tRYM62_HypiSRC-FXo5Pl__ylXz-_e8jfguSJmDSbad3dRCULi8aJliz6Dzp29r2Ej6Zxah8QS919B-1_PAJfiH-v_c6GqnpAbkQzi6E_c8IIF32zmFpklOTw9Db3ZyEnYG_TlE79GtbhiWMEWr_K5N-AMx9Y641fhchamP4bzH1IoKWfM9HbuffAyQUZ1NiwreeLGmtGiqycLhfy8G3wq-3i590Ee2oLo-QCTmPr4oOl1d3vku4ZHpjeFzvqH_GFyG0JmqKLxhlGePtpmILYAQbnSqVkwaS8xpvDvag4qs5uidQvyLHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8c4bba7fa3.mp4?token=S9M1sZVMVl2Hx6OjmmXhIOiwYDqhrZ4y3tRYM62_HypiSRC-FXo5Pl__ylXz-_e8jfguSJmDSbad3dRCULi8aJliz6Dzp29r2Ej6Zxah8QS919B-1_PAJfiH-v_c6GqnpAbkQzi6E_c8IIF32zmFpklOTw9Db3ZyEnYG_TlE79GtbhiWMEWr_K5N-AMx9Y641fhchamP4bzH1IoKWfM9HbuffAyQUZ1NiwreeLGmtGiqycLhfy8G3wq-3i590Ee2oLo-QCTmPr4oOl1d3vku4ZHpjeFzvqH_GFyG0JmqKLxhlGePtpmILYAQbnSqVkwaS8xpvDvag4qs5uidQvyLHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سرلشکر رضایی: اگر صهیونیست‌ها به ضاحیه بیروت حمله می‌کردند، با قدرتی چندبرابر جنگ ۴۰ روزه شمال اراضی اشغالی را موشک‌باران می‌کردیم
🔹
اگر امروز از متحدان‌مان دفاع نکنیم، هیچ‌کسی فردا به کمک‌مان نمی‌آید. دست ما روی ماشه است. @Farsna</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/farsna/439991" target="_blank">📅 23:47 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439990">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/53fe498cc2.mp4?token=Ag7J4cg4ne7UaXH-s0WA3y1_35lpe8InDuJ1cePF1gdthdyl6H9ZPn-moBxHXkw40pEHIbid8cFMug8L8a3TLCx4502bGJ_pXl2SVhrpzhawRyM3CLGMxIlQyb0COCDlIIZRZSAVsdmk7v4R1ZS6hvUw-SHDpB7JXYjCUd6ecO7-WNMBN-7tKOUivfD0nahs1Wiz5wgdOllxopoTZk0zjj2OnQVz__huTB9mqUYlzDI-mxWsIp62MY051JDBrB4XOg_ynzKUzVFg_OnR0l1GQtA6M-UBAYAVu0IHRPs-gl5ZrALdlE7LTASFUfDMoBqiUtFyXhmzFX_YIaAbypzBmg5Ny0ko8sHKDX13BrMaYv4D1vdQOzg2DKi3Le4qpLbFWauu8YNHvqVBkKAXacUtzdBO0xVVA0kp0EX-DzwGybt2dhFyOzBI45klxNNqTe056IpHM1NusVL5YibxdDoxxOr2mxCrfikABsJbdFdAxcRh1cRdHPMuo3Ao3jtLWyIl_-ERJ_nuP4V15YjrtFZNwlvpxHfSlnLXKWip-XW9PReYyM5XZhspungLEHbVVuZhWG7EWgiyn_6HpgVFU6mxm0IssQR9F4svzPH0iVkVEwkKRpcr9hhglmCA62Qn2Wn7MYtOXT3De5WDMgW2dBKZIhlgVubTYJUOiftONZh0stg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/53fe498cc2.mp4?token=Ag7J4cg4ne7UaXH-s0WA3y1_35lpe8InDuJ1cePF1gdthdyl6H9ZPn-moBxHXkw40pEHIbid8cFMug8L8a3TLCx4502bGJ_pXl2SVhrpzhawRyM3CLGMxIlQyb0COCDlIIZRZSAVsdmk7v4R1ZS6hvUw-SHDpB7JXYjCUd6ecO7-WNMBN-7tKOUivfD0nahs1Wiz5wgdOllxopoTZk0zjj2OnQVz__huTB9mqUYlzDI-mxWsIp62MY051JDBrB4XOg_ynzKUzVFg_OnR0l1GQtA6M-UBAYAVu0IHRPs-gl5ZrALdlE7LTASFUfDMoBqiUtFyXhmzFX_YIaAbypzBmg5Ny0ko8sHKDX13BrMaYv4D1vdQOzg2DKi3Le4qpLbFWauu8YNHvqVBkKAXacUtzdBO0xVVA0kp0EX-DzwGybt2dhFyOzBI45klxNNqTe056IpHM1NusVL5YibxdDoxxOr2mxCrfikABsJbdFdAxcRh1cRdHPMuo3Ao3jtLWyIl_-ERJ_nuP4V15YjrtFZNwlvpxHfSlnLXKWip-XW9PReYyM5XZhspungLEHbVVuZhWG7EWgiyn_6HpgVFU6mxm0IssQR9F4svzPH0iVkVEwkKRpcr9hhglmCA62Qn2Wn7MYtOXT3De5WDMgW2dBKZIhlgVubTYJUOiftONZh0stg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سرلشکر رضایی: از نظر من محاصرهٔ دریایی، مثل جنگ است
🔹
ترامپ هرچند وقت آتش‌‌بازی می‌کند تا ایران را تحت فشار بگذارد اما ما پاسخ می‌دهیم. @Farsna</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/farsna/439990" target="_blank">📅 23:40 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439989">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/41e8dac35d.mp4?token=nFic5WyQdXFG2sHQdm5HHCLBnWb3y-G3queZQHI7w6pS3dD7oCd7bbGigmrMZl3n3m1R7P86v5ZoitdhXL6b5QnVTfW8ppQTaKyJBaPHUaFq1PXRsYChfvnfiYoUcIxmLI6EktAx6ihzsMeYjQE6zWJ03A8pc7YIcosxcfDwk2V_fr0FefpaC1WzBzq1lI7rLcCc_Q-03ePvj1IG6hsEigORfOzM9kTf4WJXr5qp5dPFfmOYA217M6v3ftGTk31UKz7OoJP-gVXIfgrnuaV_DsxuhM3reZk1M1CXe8qKXR7Vh5n9-kjtURqYWRiL7GpxGv2VykoFn4CjyVXZHHCH83SHqmR_e6S-3d9VNO3bgKrqeoxDgiXNDQ5Ef93-IXAOIZU24nNr2g48eTyTvSKdLZO_gw8Fpk2fCEfB3kbZFnUrZjZWq7vV7FyKb5Z2nKWhPg1CoRYaHdzdf089lokRUKDTsn0SIUX6Ttx9v_oQiDLyh8baFKGB2Az904VqacRBr4qMAb8nPuBbs2qdkDEcp84Q-uE7HULrQ4343nQ6TvM3dmgeY_WPwC58ALs0KYPE3Kbys8tIXwakz4BeKb2kbT8ero77H3bzYBP4ekC8GsCvPpLcyxipZ3hIR1kJz1KTb4-PEoY0n4QKeQR9iIWcd0qjoGFCapTj6kY8JjfZdN0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/41e8dac35d.mp4?token=nFic5WyQdXFG2sHQdm5HHCLBnWb3y-G3queZQHI7w6pS3dD7oCd7bbGigmrMZl3n3m1R7P86v5ZoitdhXL6b5QnVTfW8ppQTaKyJBaPHUaFq1PXRsYChfvnfiYoUcIxmLI6EktAx6ihzsMeYjQE6zWJ03A8pc7YIcosxcfDwk2V_fr0FefpaC1WzBzq1lI7rLcCc_Q-03ePvj1IG6hsEigORfOzM9kTf4WJXr5qp5dPFfmOYA217M6v3ftGTk31UKz7OoJP-gVXIfgrnuaV_DsxuhM3reZk1M1CXe8qKXR7Vh5n9-kjtURqYWRiL7GpxGv2VykoFn4CjyVXZHHCH83SHqmR_e6S-3d9VNO3bgKrqeoxDgiXNDQ5Ef93-IXAOIZU24nNr2g48eTyTvSKdLZO_gw8Fpk2fCEfB3kbZFnUrZjZWq7vV7FyKb5Z2nKWhPg1CoRYaHdzdf089lokRUKDTsn0SIUX6Ttx9v_oQiDLyh8baFKGB2Az904VqacRBr4qMAb8nPuBbs2qdkDEcp84Q-uE7HULrQ4343nQ6TvM3dmgeY_WPwC58ALs0KYPE3Kbys8tIXwakz4BeKb2kbT8ero77H3bzYBP4ekC8GsCvPpLcyxipZ3hIR1kJz1KTb4-PEoY0n4QKeQR9iIWcd0qjoGFCapTj6kY8JjfZdN0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سرلشکر رضایی: از نظر من محاصرهٔ دریایی،
مثل جنگ است
🔹
ترامپ هرچند وقت آتش‌‌بازی می‌کند تا ایران را تحت فشار بگذارد اما ما پاسخ می‌دهیم.
@Farsna</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/farsna/439989" target="_blank">📅 23:34 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439988">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fbcf6abb0f.mp4?token=UtHVsTb2Xiis3c7rYd8GnYAHEr4yEAcWjuup1uqsbJ-6KbaTVTBjS3Yl-N6AoR2oi1eF6tdf2ihjnajMEeQyB2WMoTosssn95v0qJKVcvIRcmpGuNvhns4ZkSWUSfWn4TeSs3EnV9CJlQcLh71sq3mgjegfHkO44tdRunq8d3jkOFbsOannle7niXBxu5b4Sx9gaiKa_H9UMrx_S1ZRZtLT-ym05Qt0rLTdl5ZRgpOVuDap1pc-e6bH3sHP-gnK1XUeqqAEmCZLBLCB6N7v2iKoGVlSZ8ExYlSBgCGmjf3h-bk5eKV0fUloctvGTfTBZj2S6RvBVjxMMiKWLJYzylA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fbcf6abb0f.mp4?token=UtHVsTb2Xiis3c7rYd8GnYAHEr4yEAcWjuup1uqsbJ-6KbaTVTBjS3Yl-N6AoR2oi1eF6tdf2ihjnajMEeQyB2WMoTosssn95v0qJKVcvIRcmpGuNvhns4ZkSWUSfWn4TeSs3EnV9CJlQcLh71sq3mgjegfHkO44tdRunq8d3jkOFbsOannle7niXBxu5b4Sx9gaiKa_H9UMrx_S1ZRZtLT-ym05Qt0rLTdl5ZRgpOVuDap1pc-e6bH3sHP-gnK1XUeqqAEmCZLBLCB6N7v2iKoGVlSZ8ExYlSBgCGmjf3h-bk5eKV0fUloctvGTfTBZj2S6RvBVjxMMiKWLJYzylA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حضور محمود کریمی، وحید شمسایی و سالار آقاپور، مرد فوتسال آسیا، امشب در تجمع مردم در میدان انقلاب
@Farsna</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/farsna/439988" target="_blank">📅 23:27 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439987">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af31942098.mp4?token=gh58CyH2ol00tRBDZ4wwqg2OZXikVBZ-MTNktLkgl5tQdHfYgnniPvFeWxTUQgtsm3_D803fyc8iPtGVGdHewsZJjS_owQ30-jUZob0w5-gGbcJOsx_CjgSqsM-1d1gSJQ0A7cSXup0ciEKR4UJKgFWULbfkXsZ8KXxWEiov671ku10IMFSzP5DtsJPuhGohaC1iQI0wtHm444YzoZlZWGR00HXnVmrhKEIz3r0fnWlb8_9rMq3764teiyP1QhF-c3Zz-ffHwb7qLlQQwNe94esaNsCL-OtbBswKFLknmiZQl1veRDnv-CyBZ7iL1dORyZ4BwASyqI_kfd5hHt_fuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af31942098.mp4?token=gh58CyH2ol00tRBDZ4wwqg2OZXikVBZ-MTNktLkgl5tQdHfYgnniPvFeWxTUQgtsm3_D803fyc8iPtGVGdHewsZJjS_owQ30-jUZob0w5-gGbcJOsx_CjgSqsM-1d1gSJQ0A7cSXup0ciEKR4UJKgFWULbfkXsZ8KXxWEiov671ku10IMFSzP5DtsJPuhGohaC1iQI0wtHm444YzoZlZWGR00HXnVmrhKEIz3r0fnWlb8_9rMq3764teiyP1QhF-c3Zz-ffHwb7qLlQQwNe94esaNsCL-OtbBswKFLknmiZQl1veRDnv-CyBZ7iL1dORyZ4BwASyqI_kfd5hHt_fuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قابی تماشایی از بازی کودکان در جشن ۱۰ کیلومتری غدیر
@Farsna</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/439987" target="_blank">📅 23:24 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439986">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">‌
🔴
سخنگوی ارتش رژیم صهیونیستی: دقایقی پیش پهپادهای حزب‌الله به منطقه‌ٔ محل فعالیت نیروهای ارتش اسرائیل در جنوب لبنان اصابت کردند‌. @Farsna</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/439986" target="_blank">📅 23:12 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439979">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vOP9eonz1LQCEloOBVkXM9bcULt_lph4PGZXVNVked0m3CIuQTppszcl9kefLDuIRwDY1o-FDy-bK6FVD08gwag-ZBXMfzsnklHuwhHfeyjpkJ-p2O79PVqIAmWUYvg2HYM7emAlntnEwdlulOsgpAAN1T4XZ7bQQubt5EmNOI-lITlwG28joGm9Wx4o5nNPRXRPOpoYsnTT07HdWzS6rlVcRuML57kUiBj9v68kDQfl18h6LLe62cliMzVDQqQZ7-_ebYZeRWg4dEJIEKKRPtcjFgZLRema3pAhwEBa5zGe6MhVenhPihNiJPKSMX9t4dy2DK-3vJHd9kSARFheDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oOrDHZzJC0098HxgrbRK5okJ8KXD8UQdBIn4U03rQ_Rhk6IFeiwlqVHI9pAg6zol2ZtFyujei3oFzlgZ15_WLnz-RM8R7yINZpIcgRH3QGV4v_97D95UWnhhc-NP0ajNhSSu2kEgeGUQxhIfx5pnEME0gITEcWXGASv-lJuW9g2LIHe8WKhTxK554jWpZyFYPJWUw90K0XJGNk13sEgdEtM8H8LThv06dPvm1ggy2nSy858ZzcfYoKmkZKS5nqXGuoJHiyUtohq2RqKrRIT_B3tqKM2-ysw3FSgP8kp4AbMhC7JP0t8TnGsxP9KWqVPpvfsMYK14lzASWKqvo6cB4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BXyTHbWS5k4ik9lkTOMnPdlx1sl2q1qfldZ0ZRz-oVwHFXRqA9K94KyXytdS6mzqPCPp3zG1ptpifHOwOMurB8sKDnwutB35fNPUqThdvz7V_NzjvJZehN2_6_k-We99vgAOnJ-SZFy8Ep8y5XVxOy3Y5v-1W2iXVtqoYxo_PGjTNV7OUv6EgPMYKTnuYihsh3Pg4dmc9tUaDkuCxHyaOpr_Z5Sv2pWlhNmGUcRPkitE2b9FKRcXXOJOK1HjMYT2teITS36iC66boTENygX6RjfZ_jWB-qI2cHNBhglO8NZyuQtXbSJj5reEnLULAeuQyaoFlf2Ql7idFGA4_y4YPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dLer-pW2J9DENCXyBvb-4UNHSoGUQo_7Jc9XoeOfZlt_TEvhI7xRx8Fi582QUj_cbvWaMtB-BqI5kpLk-KXAZDeqdkWx4aoVR6gO5myAdoF2W0mOWgujZOZK_Gxx1DZ5Wb0ecu88N6-Lwt7ujpPsamLFvfayQ6ef6XFHgxhBpCgfrDtkFVsYiYgpG2TJo0tBD-500k3WEGDUuKisSgv25UdzuFOh7gqTNGwrpZBEHpb64SMJ0HDFaOqfHnhhpC-XeEXKR4hvxyQyNSKZnl2GWXaYMqV-uRR9tGK7sWfajQoMUT57ou3D5Obya7MFO48omJ4Uaj44ejwOE04l9_mHpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pDIfUcujPIS6V3Z7FICEP4iE6ZyU2Nkoob1ptOpLBZFz7LWXk0iFI9vob4xaysmuqMUES9g3jMd-vYp9mET4EKzD-AEVzd4aJtWWkOwF2Z-cCTBBpdHJLG5qlwCyIdNj4zPRltI-LhJvN7TtzloMLNomhYFPb2PFBjNcoH01-KNDmtqzUzAHCP3yDMZqDrGNZZlcygklp_gqFm_keJ9oMcbq6dtxOycjqsLwl9zg2QnVF-hG9XRvlUiqwt-p5dBDz0QRJmFZ03qa_UAM867wXAVwBW1vlRhDp-sfEYf54eHGt3g7f5ZgsWRKTy2omBc7caGyyGdtD4jVtlqZ4En7kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Hghsyg_v_DYAfRGSQ-zzFNI2nnnqp8KQTikUzZJ0D-r8yJc911S_2qQ-THTlx7mL-KWXWJ9g5P-q7Efj6-NE9zv_w4ioc-VqPJ9HR9xNm03zOv2nhh659Gaoxuq37d0XhxSHxLDZteGvHksRVf03phnbCqFpX1aN03MdgE4l-asq_VjMaPlSv0hm1DsAf2bCu9GziUhJAdASuQKK3St-FMfNrzwV3cXfo_MgQMVOjvkehSvtFRSsWBsunL2erzkY0dXihx5ouBR339QnFYLbyk0iSK7vQzF8EJ31mRtFLUYbVTS3rnDwj1RMl-faZyfebe38CIuRRs1LKraLChnaig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dh9OV9wLwIWoWnOkDltenffDdkj2Sh-PD3e3LcZva4gRgEAnPi9v4dWNEjuavUHlALBgv9324FWW02NdOo8LdghIahvKCRtY2tl9Mj1rnpJE5tR_HQfoJ6dpdn6zX-kQ-rJi_dMB1SF6ni76M6DZ4l05QZZHvNNqUZVI1Jo6Y4Hq2BzpNbeBifQqqP7eeN9rAfa42H2t72eMeh-1fTdvznF_ChLIGmMQPWj3JXty3t8z_2vNmA1cNqA1C3kX0F6nyFbyNyKRNix0hM6vzehJqU2kENwiXiDJB2eOyuhHFgSYjP5WTnzDw14lRNOGoY2nhuxgYVJanzEOE1CpzL3-Og.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
غدیر از قاب خیابان‌های بیرجند
عکاس:
حسین توحیدی فرد
@Farsna</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/439979" target="_blank">📅 23:08 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439978">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b22c0e31dd.mp4?token=geXk8EoRNrjJZW6TvTqkj-7AibB-_dDJBuyuU6e7Nfxt1DoE609ijyi_nUgGDSXYm9i6t2MdyNciIPVNURI87kLAV49oB_UqUMKp7hYLKK5rU8UHCczPJwSlDbNu9nSxx8-0kjy0qmA7PMPJQz4LYGJGYgA662MtPMfQJ0Hum3QPSmcAQvSNy-iVtCGZKVOGU_IbIGyAZS23E_BOa57zzms__iUpCSc9ZI5ZI0Qgt60xBJPPKfFXIyGl_fFIHFiud5Pf2ElOIk53Q3YTzv8_A0IJzahf5WapPNVNUERM_lHr8hz7BbLX5Cn0tjgm88lF9OtCZ8xNBh_roRrFGGkAzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b22c0e31dd.mp4?token=geXk8EoRNrjJZW6TvTqkj-7AibB-_dDJBuyuU6e7Nfxt1DoE609ijyi_nUgGDSXYm9i6t2MdyNciIPVNURI87kLAV49oB_UqUMKp7hYLKK5rU8UHCczPJwSlDbNu9nSxx8-0kjy0qmA7PMPJQz4LYGJGYgA662MtPMfQJ0Hum3QPSmcAQvSNy-iVtCGZKVOGU_IbIGyAZS23E_BOa57zzms__iUpCSc9ZI5ZI0Qgt60xBJPPKfFXIyGl_fFIHFiud5Pf2ElOIk53Q3YTzv8_A0IJzahf5WapPNVNUERM_lHr8hz7BbLX5Cn0tjgm88lF9OtCZ8xNBh_roRrFGGkAzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حضور خانواده فرماندهان شهید موشکی ایران در میدان انقلاب
🔹
تجلیل از خانواده سرداران شهید طهرانی‌مقدم، حاجی‌زاده و محمود باقری
@Farsna</div>
<div class="tg-footer">👁️ 9.83K · <a href="https://t.me/farsna/439978" target="_blank">📅 23:05 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439977">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1186b0acc2.mp4?token=QC9ptFIlPiYYBaquGuL7ctwxSZxna7rtYMBJvqmkbvgm0BCAe3A11ac5V3e0gJ0t1YUn2IQtkHsVRAoRCnQ2vDfKP6j31vpFDLY4Ky683r-AjHtoVOT38LlpdZzmOp7HSLle2BtqlRk6cZ76rts2hhaSGyOkyD0scNa8Ij8JJ6KZxfehN_SbI7uqhkAB9WS18EbFDuWIjwO1J896o9EDGqWzWgFt1_6nuUt94L65rQsMhcjtvwnqdI3Nn_YM4w_OYRMACBIhaR6Ewx-uqOg3wC8SNOnLbkt-nOw7EfXnPXfGavVPUx7pYeNX040PL4ch1JVgPTySPiINrgCGI1nsKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1186b0acc2.mp4?token=QC9ptFIlPiYYBaquGuL7ctwxSZxna7rtYMBJvqmkbvgm0BCAe3A11ac5V3e0gJ0t1YUn2IQtkHsVRAoRCnQ2vDfKP6j31vpFDLY4Ky683r-AjHtoVOT38LlpdZzmOp7HSLle2BtqlRk6cZ76rts2hhaSGyOkyD0scNa8Ij8JJ6KZxfehN_SbI7uqhkAB9WS18EbFDuWIjwO1J896o9EDGqWzWgFt1_6nuUt94L65rQsMhcjtvwnqdI3Nn_YM4w_OYRMACBIhaR6Ewx-uqOg3wC8SNOnLbkt-nOw7EfXnPXfGavVPUx7pYeNX040PL4ch1JVgPTySPiINrgCGI1nsKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
واکنش بچه‌های تهران به بزرگ‌ترین شهربازی ایران
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.84K · <a href="https://t.me/farsna/439977" target="_blank">📅 22:59 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439976">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dde69484bb.mp4?token=sNoDBp9jZBOtrpATMBVd2BEgCiEKnhGACMMP4IFMoTmJUDaKHq0ouAhJHnn6VHDRK52KjCTiwIiG4pg_d1SLQ3lyM-XsEoar1tZTQ3n2PEfhZOysJm1nrsJolOJ8cqEplhL-lRCTt0NtqEZPvcdsk5um5-6-VgHbGMNGwx4rWk-sC-jHw6J7cMFqAZWIJsnZcvt-66lpqm5i63tKJmPPE9JiIOSsv2ggVuuy-l9OxFEQ43N85kTjH_wmA0Oy6sLk6iJEHMmrHhEeeVY-nhpuc30iaDE6NvWDGLd_OoENbCAHZAbFLRtruxd31rv_hNRSdx7SSOfRwHFpO_m-YyjdeQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dde69484bb.mp4?token=sNoDBp9jZBOtrpATMBVd2BEgCiEKnhGACMMP4IFMoTmJUDaKHq0ouAhJHnn6VHDRK52KjCTiwIiG4pg_d1SLQ3lyM-XsEoar1tZTQ3n2PEfhZOysJm1nrsJolOJ8cqEplhL-lRCTt0NtqEZPvcdsk5um5-6-VgHbGMNGwx4rWk-sC-jHw6J7cMFqAZWIJsnZcvt-66lpqm5i63tKJmPPE9JiIOSsv2ggVuuy-l9OxFEQ43N85kTjH_wmA0Oy6sLk6iJEHMmrHhEeeVY-nhpuc30iaDE6NvWDGLd_OoENbCAHZAbFLRtruxd31rv_hNRSdx7SSOfRwHFpO_m-YyjdeQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
لحظاتی از اجتماع غدیری‌ها در مسجد جمکران
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.72K · <a href="https://t.me/farsna/439976" target="_blank">📅 22:55 · 14 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
