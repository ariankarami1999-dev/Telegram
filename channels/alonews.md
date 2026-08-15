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
<img src="https://cdn4.telesco.pe/file/LXXJysPkfnr6ohUwwySTf_PLF1oj5fiy1NAp47WWeQrAWGddwEtwj3eNK5YwIALbs7BoLCSmD1bJmTPfxI42DsY_satgGzeZdVmBikov0lglnS2KyWOhsNScdJhTzhROVqcjuluSloIvWe_CyNrqTsxx3GL2hbA7GC3sXTZmu19eD8pP4ii5VTyLbo2FgzAaWVSCnX03CbuO607R14eWaBVCBxNy0aFFbQJ_UC097_t7zX-5tLnm_g62CqAo_J_3JtdOeDBqyQLMMIBtk167HLBHfe3BAs2jAV8oAGNLP6tDDStik_H1RtujevZxAwFCMw0kIO0ZKgeMWaJJhHnzGA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 966K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directمالک کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-24 23:42:12</div>
<hr>

<div class="tg-post" id="msg-141938">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/pgIIRpRTQ7_rJbA3Nbr75xuvtUfS9AY9bhQUOWOLHrvzgIKqlG5BJPjMUfY1yk6HP_KN8v1zXmvoy7Ue6vJoOkypTonZMe29pvy2pb1B04Iy1pU7hn33dlgYm_QlieKAgU0Y3saZF1sH_W97q-5mLgjrRwL7bpBE76JI-67BINrHee1NIQmheJq8tkVfmxatxcGaaWjqkc1rb-VAU0dX-zj1AQEIyTVIXgPXtR9nRPsdoMYtFGmygmvtT-MsrP836wA3ZcrnXbksAsMQfzFtptJne_uJazVA7dnx0W3jZ4TvS03Pz_WBL_D8Lp189bcEHL5PglW7AWH1aKjRRdbAAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
فرمانده ستاد ارتش اسرائیل: آماده بازگشت فوری به جنگ تمام‌ عیار هستیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/alonews/141938" target="_blank">📅 23:37 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141937">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q4yAXefOdcT6W10NbCEFirL1c7s2ExXfwme3ASeFDXdq3Kmzc-xFLLXo7ZmW8ETp0whAkkpzoec7IhGqS4zmT22wsgKvKz2lyibVcXbfkYonBo9EoJc4bf1hpmHw0W95CQDTHurYKvp82RmhmAQaQxzxRnHdkLogHMj7aRKNqxUqNwo-wCsRmoWfGFT3H0Q_xlCN_rLjcTGcjMZU5VMlJnnLr8KTGqhwbLKoXEGPFiPgii5ixY7cJVMiKLhzsJ1-Qk4B-DNB4ZenpElBKd2-aoFEp3A__8bOxTEgX0dEl6yyHwAza7d67Ct3b5Tf3JKENIuPg_PaURKSZ4me_UQjpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
همچنان جی دی ونس شانس اول برنده شدن در انتخابات ریاست جمهوری آمریکا در سال ۲۰۲۸ است
✅
@AloNews</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/alonews/141937" target="_blank">📅 23:32 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141936">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b1aa363cc6.mp4?token=sBGuQkjbB_JE9IPIOwIOFnjrCR9XfN7Jyh8nUKNdcpVbC34EXNpuqkLeOFLJBjprJYWY1CQCuv8O0k-V_LqiA95DLJo9U5YeVwrvPZDTKQjoUifzjfn2hqFLjoTtx3NoXtO694psfE4LR_b6D5SCf-7850zK_7K0Rzhw5ZwDG0EqYcMf6xCKzN8Y_68fZry5DzbQG2hT5bi1THHP-qJaedn4vqcPIy0c9Mpnojnf6lm5BlEz8r71iG1RW-JD1f4ZudffNVuTtjDX-WJlGZe3ZwpReau04LcAO3zwtVHgfgh8umOwpEyZlX_S2u82DoG5IIJXXCt6_GsufnQtCg5pWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b1aa363cc6.mp4?token=sBGuQkjbB_JE9IPIOwIOFnjrCR9XfN7Jyh8nUKNdcpVbC34EXNpuqkLeOFLJBjprJYWY1CQCuv8O0k-V_LqiA95DLJo9U5YeVwrvPZDTKQjoUifzjfn2hqFLjoTtx3NoXtO694psfE4LR_b6D5SCf-7850zK_7K0Rzhw5ZwDG0EqYcMf6xCKzN8Y_68fZry5DzbQG2hT5bi1THHP-qJaedn4vqcPIy0c9Mpnojnf6lm5BlEz8r71iG1RW-JD1f4ZudffNVuTtjDX-WJlGZe3ZwpReau04LcAO3zwtVHgfgh8umOwpEyZlX_S2u82DoG5IIJXXCt6_GsufnQtCg5pWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سقاب اصفهانی
:
پولی که برای خرید اتوبوس داشتیم را در جیب قاچاقچیان سوخت ریختیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/alonews/141936" target="_blank">📅 23:29 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141935">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/580f35cabe.mp4?token=e5raVNd3gnMLClbXkpDeU0O6drhEWwNInCITtrH3cuty4n0ZKeJ8oS4QWgfXpTlVzOb_WzD-JTPvSGkLTgGYxOt79jl04A_uirZQOg7j98bvZ9gsjvgNyulF_QogZIxpyoEEvb1JoCYqjO_osjV7ZbLa-vDe6GIEvDKvCkTL0-WKhCAjofI6jhSCaY0KfZ6LN7J7Bv9C1xTfT9X4p01qw9Xi8Za7Tkd5GR4rg4VvLGqbMpPTJ8KMuNgwqunM1FVEF013bzHVUtGTG4-74DO5gguDJy2C8hzxRIt7FY4I75tS6sjs9YDYk07Nsy0ncF2ZyT7nrCR6V_lWRHW3c5KrxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/580f35cabe.mp4?token=e5raVNd3gnMLClbXkpDeU0O6drhEWwNInCITtrH3cuty4n0ZKeJ8oS4QWgfXpTlVzOb_WzD-JTPvSGkLTgGYxOt79jl04A_uirZQOg7j98bvZ9gsjvgNyulF_QogZIxpyoEEvb1JoCYqjO_osjV7ZbLa-vDe6GIEvDKvCkTL0-WKhCAjofI6jhSCaY0KfZ6LN7J7Bv9C1xTfT9X4p01qw9Xi8Za7Tkd5GR4rg4VvLGqbMpPTJ8KMuNgwqunM1FVEF013bzHVUtGTG4-74DO5gguDJy2C8hzxRIt7FY4I75tS6sjs9YDYk07Nsy0ncF2ZyT7nrCR6V_lWRHW3c5KrxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سقاب اصفهانی:
هیچ شگفتانه ای برای مردم در بنزین ایجاد نخواهیم کرد
🔴
در صورت انتخاب سناریو، چند هفته با مردم مشورت می کنیم و اصلاحاتی در صورت لزوم انجام خواهیم داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/alonews/141935" target="_blank">📅 23:29 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141934">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">👈
در پی حمله‌ای موشکی از سوی حوثی‌ها به نیروهای مورد حمایت عربستان سعودی در شهر مأرب، یمن، طی کمتر از یک ساعت، ۵ انفجار رخ داد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/alonews/141934" target="_blank">📅 23:27 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141933">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👈
سقاب اصفهانی: امکان ایجاد بازار صحیح برای فروش سهمیه افراد نیز می توان اجرا کرد/قیمت این بازار ها نباید توسط دولت یا رانت کنترل شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/alonews/141933" target="_blank">📅 23:23 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141932">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/da4e44162a.mp4?token=lSOWqaqaryxzhZ34KwXP-pdAItrN7QMKnQvQqYpqoUBf0ZyDKqb-bGmXfngNXRJCUNDLE9dK_KveIYRor4HslzMeSn7997WgU6GlPrjGJ9lnngozSqQkhVzEN731Ou-JSkPcocDdlzvPK1n5FrhDGjoFYt17Ci_8l-y9t4azQ44WS297y0_7LRgZCcoxjKF6SVfeSM2LAFa8SgTzp4AV2PvY0tzY3a3D1zeYxIoILn7kBY3hoKy6082aRAuSky3NxrsaHRRwc-UNJL2_VQxn8WG8WEkZvzoHrey52WhQwob7E0K3lbIrqW5p1yZdxsO2JxF3niiRZOubSzpEPBU-pA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/da4e44162a.mp4?token=lSOWqaqaryxzhZ34KwXP-pdAItrN7QMKnQvQqYpqoUBf0ZyDKqb-bGmXfngNXRJCUNDLE9dK_KveIYRor4HslzMeSn7997WgU6GlPrjGJ9lnngozSqQkhVzEN731Ou-JSkPcocDdlzvPK1n5FrhDGjoFYt17Ci_8l-y9t4azQ44WS297y0_7LRgZCcoxjKF6SVfeSM2LAFa8SgTzp4AV2PvY0tzY3a3D1zeYxIoILn7kBY3hoKy6082aRAuSky3NxrsaHRRwc-UNJL2_VQxn8WG8WEkZvzoHrey52WhQwob7E0K3lbIrqW5p1yZdxsO2JxF3niiRZOubSzpEPBU-pA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
هدف قرار گرفتن نیروگاه برق الزاویه در لیبی با یک پهپاد و قطع برق
✅
@AloNews</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/alonews/141932" target="_blank">📅 23:22 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141931">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a2f7915012.mp4?token=jR34psS6IZ0rjEXnu9YpL4chKZq92cj7Th0ow6OMJs5uIxhrfyike2mnTFuN2ba1bLIpnE3AHhd5auE829ma7iFom58ICE-2PeMZWDwBJJqKsdyee3BZEoLQOH6tZKxAusXVZxFSy_LwBWCksrOUDsb0AAGdNwYoq1n9aGyVGXmPrfcgxfKxx8Px7-i08fygRyYROMDldl_GWQC0Hay87vXp9KR94LIfmQXVzvZXn2FDh8daClAtTOJ4dJ-Mv4nBpeCaO859Lxl6UU6mh1XtBiLskZaVwxTMbTp_odRJCa_zowlm6IdM7fj_Ah6NKRKirTYEu6PI0r9pPIOwi5rRhg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a2f7915012.mp4?token=jR34psS6IZ0rjEXnu9YpL4chKZq92cj7Th0ow6OMJs5uIxhrfyike2mnTFuN2ba1bLIpnE3AHhd5auE829ma7iFom58ICE-2PeMZWDwBJJqKsdyee3BZEoLQOH6tZKxAusXVZxFSy_LwBWCksrOUDsb0AAGdNwYoq1n9aGyVGXmPrfcgxfKxx8Px7-i08fygRyYROMDldl_GWQC0Hay87vXp9KR94LIfmQXVzvZXn2FDh8daClAtTOJ4dJ-Mv4nBpeCaO859Lxl6UU6mh1XtBiLskZaVwxTMbTp_odRJCa_zowlm6IdM7fj_Ah6NKRKirTYEu6PI0r9pPIOwi5rRhg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سقاب اصفهانی: امکان ایجاد بازار صحیح برای فروش سهمیه افراد نیز می توان اجرا کرد/قیمت این بازار ها نباید توسط دولت یا رانت کنترل شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/alonews/141931" target="_blank">📅 23:14 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141930">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">👈
رئیس سازمان بهینه‌سازی و مدیریت راهبردی انرژی در گفتگو ویژه خبری: حدودا به هر عضو خانوار ماهی 30 لیتر تعلق می‌گیرد حتی اگر صاحب خودرو نباشد.
🔴
قابلیت انتقال آن به هر فردی که بخواهید وجود دارد. دولت مدیریت سهمیه را به افراد می سپارد.
🔴
قیمت دوم و سوم در این…</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/alonews/141930" target="_blank">📅 23:14 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141929">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f05284b9d0.mp4?token=R3oYp6INMw0REIM_dFkVXiv-s4zVhiNO_iwHLuVMU5Tmk4SsTCtcMwBe643UBU2oDBUIA5TWmPrUA7ZjwKYpPSZ4-b4O4TFPvtaw9ecRDDkggGJMkq93gXo7coKPRYiWfSdvRb4ESswM5lkoq9N4_S9BKzssbbZ_3HM7pW9OMCnbAnmrUxng9fwLuD69nL0kinML_daEoc5Bs468wZzOMrydyYXIq41rSJHIUP0N9wmhZrUocnzQk_UnmwcrY9GwwmF6YooVm4gl960hcyDG0SlKc4mMdkzKKKjgx6nA-GwE6wwJY0hMgOR1tP_TFme84ZuWdnolpfz95kgEjBF8SR3aepEzFsbsy-8ncdq2tc41kane23Tsx5XYYNIC6hlDjrPg-RWIablIWZUuMVs9AVUTVSWV0POAeLQxHJYm2iek1lmLTWORfUW6sEFA6950fLhr4ZfIvhEUzMJZ0pBZ4WzdMV4yiV1lTx4SW1IlZEIhggS5yIll4HycEQ6FucygmOUAK_lutr-mtRkgfamDVd-6PZVsp2fZf76zQiT8s-Nhisr0dUiB3HzQ1sWKQ0XCVihAGBS9MVtB5HZFLJ95EQqTeIq8BI9SHzW7pObXkiRB8uMUyz9FyuKbTRxbY7qJCpPR-wkPWPGza0rDwaPkhv16t0ov-vcvpADfTKbLP-8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f05284b9d0.mp4?token=R3oYp6INMw0REIM_dFkVXiv-s4zVhiNO_iwHLuVMU5Tmk4SsTCtcMwBe643UBU2oDBUIA5TWmPrUA7ZjwKYpPSZ4-b4O4TFPvtaw9ecRDDkggGJMkq93gXo7coKPRYiWfSdvRb4ESswM5lkoq9N4_S9BKzssbbZ_3HM7pW9OMCnbAnmrUxng9fwLuD69nL0kinML_daEoc5Bs468wZzOMrydyYXIq41rSJHIUP0N9wmhZrUocnzQk_UnmwcrY9GwwmF6YooVm4gl960hcyDG0SlKc4mMdkzKKKjgx6nA-GwE6wwJY0hMgOR1tP_TFme84ZuWdnolpfz95kgEjBF8SR3aepEzFsbsy-8ncdq2tc41kane23Tsx5XYYNIC6hlDjrPg-RWIablIWZUuMVs9AVUTVSWV0POAeLQxHJYm2iek1lmLTWORfUW6sEFA6950fLhr4ZfIvhEUzMJZ0pBZ4WzdMV4yiV1lTx4SW1IlZEIhggS5yIll4HycEQ6FucygmOUAK_lutr-mtRkgfamDVd-6PZVsp2fZf76zQiT8s-Nhisr0dUiB3HzQ1sWKQ0XCVihAGBS9MVtB5HZFLJ95EQqTeIq8BI9SHzW7pObXkiRB8uMUyz9FyuKbTRxbY7qJCpPR-wkPWPGza0rDwaPkhv16t0ov-vcvpADfTKbLP-8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
رئیس سازمان بهینه‌سازی و مدیریت راهبردی انرژی در گفتگو ویژه خبری: حدودا به هر عضو خانوار ماهی 30 لیتر تعلق می‌گیرد حتی اگر صاحب خودرو نباشد.
🔴
قابلیت انتقال آن به هر فردی که بخواهید وجود دارد. دولت مدیریت سهمیه را به افراد می سپارد.
🔴
قیمت دوم و سوم در این طرح وجود ندارد و سهمیه در کارت بانکی افراد شارژ می شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/alonews/141929" target="_blank">📅 23:09 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141928">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c66d62c3d.mp4?token=O1OOfEkcSxLjdZKpfxOjlWXZi4ywY8SCkPrs6ZDbOjb3KHnJ_iiqO4nNLpVfxVs8kFAq2MdS4Bh3B6crkTgWOm28BMZuOG5AoQkiDNlibQcrLEgrtsqITGEdThisUHMnhpzDTLyG6mz-ERm2z7m-siJTxYomLlviDxD6aoLAFrZ8Z8DvkCUODHSdkaqMrqhcWrtHkqUc472io2WLz6O1KIL2A3KhFArxVLrRV0IcmLhBKEBa_B_0hPfs-LICzc-10lE9ecjVVQ6ubHmBN4JbYrGuI7LeChQfeqnqd74rlvs8UAkEX2B2vqaNMd_lTy04JsatszQ1pdc8r9EIF3X3oA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c66d62c3d.mp4?token=O1OOfEkcSxLjdZKpfxOjlWXZi4ywY8SCkPrs6ZDbOjb3KHnJ_iiqO4nNLpVfxVs8kFAq2MdS4Bh3B6crkTgWOm28BMZuOG5AoQkiDNlibQcrLEgrtsqITGEdThisUHMnhpzDTLyG6mz-ERm2z7m-siJTxYomLlviDxD6aoLAFrZ8Z8DvkCUODHSdkaqMrqhcWrtHkqUc472io2WLz6O1KIL2A3KhFArxVLrRV0IcmLhBKEBa_B_0hPfs-LICzc-10lE9ecjVVQ6ubHmBN4JbYrGuI7LeChQfeqnqd74rlvs8UAkEX2B2vqaNMd_lTy04JsatszQ1pdc8r9EIF3X3oA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ویدئویی از شلیک اخیر موشک‌های "فلامینگو" اوکراین، به سمت روسیه
✅
@AloNews</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/alonews/141928" target="_blank">📅 23:05 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141927">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">👈
سقاب اصفهانی: بنزین در ایران لنگر اسمی تورم است/ مردم بلافاصله بعد از افزایش قیمت بنزین انتظار گرانی همه چیز را دارند
🔴
پ.ن : همیشه بعد گرونی بنزین همه چی گرونتر شده
✅
@AloNews</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/alonews/141927" target="_blank">📅 23:02 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141926">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LS5If3yrfbs8UD07X1Y6D59YBDkx78nri3vmlPk2LLVygfMNuQifGASQA1XBSaqhWCtE5b6TwjaTk6LWJbz2EvEB3GP9SeWUDG6iuaUy8k37WznB_BFYKoaCaKwZZvJ6N5oWRoCFX6SAzEDHScm45iUA66drDsd9mYzo74KjJ1mGsTvcKq6Gi0aj0JUvP5hX7OgCc3_OEGSSSy8hSGZMikcne-xauZp5EBj8gdQFGAq1DZrWEcJnmhnf0HViiayWNp-edri62hVlyTn4MfbUyzMYfkMVaTDsgNM0us6Ue04FodMEs_JOPvPBaYxinkgi_yU7ZrSvl5-uE3b5_bTLjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قیمت اقتصادی ترین مدل گوشی سامسونگ از ۵۰ میلیون تومن عبور کرد.
یعنی شما اگه ۵۰ میلیون تومن نداشته باشی؛ یه گوشی خیلی متوسط هم نمیتونی بخری.
✅
@AloNews</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/alonews/141926" target="_blank">📅 23:02 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141925">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jp8KV0EgiP74DwqOPUGRtEJkSbUMJST1yc7foH8LX1Jq2VQdDEbtV488p30Ff5Y5GQK8Lf7vK_qANpFbUrAmUEi7Sw6lZrBYU3F1xc4mtULJiUcko470VLctP1F1dtpp56E_5M5OBBNBL14-18SzUDg_-1to7sJf7WPKLg4YWra-9zY3h-8GaLTWqpoF8naEBUIH-gd31vS2R5l1p9sXsAUfkNfufmdJGWNO8xRkV_zV5tsfBtXgXDonRyxo6U_d4GTegPJbaGNKpNfMy1QjVsC5tHLbxPqkARzrxvca5e3BTleBJkOeYtcNwpu3st3gJ_PiZb4KCit3P7s4yDAR9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
کاهش سلامت روان در میان اعضای خدمه ایالات متحده فراتر از ناوچه آبراهام لینکلن به سایر کشتی‌های مستقر در منطقه برای حمایت از عملیات علیه ایران، از جمله ناوچه باکسر گزارش می‌شود.
یک مادر گفت پسرش از ماه مارس در ناوچه باکسر بوده و اگرچه شرایط «به بدی ناوچه لینکلن نیست»، اما این کشتی چندین ماه بدون توقف در بندر سپری کرده و سلامت روان به یک نگرانی جدی تبدیل شده است.
او گفت این کشتی پیر در ابتدا برای یک استقرار متفاوت برنامه‌ریزی شده بود اما به دلیل کمبودها به خاورمیانه تغییر مسیر داده شد، با وجود اینکه انتظار می‌رفت پس از استقرار دیگر بازنشسته شود، و با چندین مشکل مواجه شده است.
اعضای خانواده همچنین می‌گویند ملوانان زن در ناوچه باکسر به دلیل تمدیدهای طولانی‌مدت استقرار، از دست دادن تماس‌های بندری و عدم تأمین مجدد، از محصولات بهداشتی زنانه بی‌برگ مانده‌اند. ملوانان از بستگان خواستند پدها و تامپون‌های اضافی بفرستند تا بتوانند آن‌ها را بین خدمه توزیع کنند، اما بسته‌های کمک‌رسانی هرگز تحویل داده نشدند.
منبع:
آرون
پارناس
✅
@AloNews</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/alonews/141925" target="_blank">📅 23:01 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141924">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8252e0d0e6.mp4?token=SoR8ZbeNNfIVvTEqj2MuueFcmGlgMLINA-lNK8Y8GGRv1275skrYVRdGwyzQt-nQg351maNIVLL5zQDlxTmTXwBODMXaFVAxOBZgW8_v3yfPB6sxDscDFPrILH-O3lLd_CrZLyt4Z8_tp-BuTMJqRLXEMi0seB767VMD83TjaTcC_6whFFlMU7qfvd1ymTgRXykkpiQ0kk5shl1McYgiiQmNYIRG5yO5H9cZ8VLQYJQKFnURM92QBi-TnPf4amImViuC6weJgMX1Fcd5qcglUJkZ1wlUg_yoiqzNnGuLLCgSpw7MGMd1YxuIxkV4DkMv_V0IAzQ_nPRRz125VBYTWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8252e0d0e6.mp4?token=SoR8ZbeNNfIVvTEqj2MuueFcmGlgMLINA-lNK8Y8GGRv1275skrYVRdGwyzQt-nQg351maNIVLL5zQDlxTmTXwBODMXaFVAxOBZgW8_v3yfPB6sxDscDFPrILH-O3lLd_CrZLyt4Z8_tp-BuTMJqRLXEMi0seB767VMD83TjaTcC_6whFFlMU7qfvd1ymTgRXykkpiQ0kk5shl1McYgiiQmNYIRG5yO5H9cZ8VLQYJQKFnURM92QBi-TnPf4amImViuC6weJgMX1Fcd5qcglUJkZ1wlUg_yoiqzNnGuLLCgSpw7MGMd1YxuIxkV4DkMv_V0IAzQ_nPRRz125VBYTWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
احمد آریایی نژاد نماینده چفیه به گردن مجلس:
مهسا امینی به درک واصل شد!
✅
@AloNews</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/alonews/141924" target="_blank">📅 22:58 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141923">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bpv-K7SRi2I8t8lK3oWUB2HYfcOjM9RGDt01rSgsod-fHWDcJIAu5bkWDWTb7e-E8X49OqZzM319kt8dNYCv1opGdjmmAE3sKx2-gYhU4yUsI7SRjKvUiT3asOnjZbQM8ZkoEzsmobuQYr9Dl3JFQwQ97EwVfLEmKjWtYKFLqx0QRrxqiRTLuzKYNGIdRopAz_uR8EN8trYjBj1Nvixj6NNM9m75dJI6h186iOKmnu2KY_ZbughpAUvDCAdnhFeQZyRNyKjR_bPNchydpE6uwFGO1eBICkh2vhRP8JcQL0IdHAyKW1_oFQYTmwN9Po4xAZgw7laQuhakPrQkhRIyZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ایرانی‌ها درمیان ۱۰ کشور پرکار جهان
🔴
مقایسه آمارهای سال ۲۰۲۴ نشان می‌دهد ایرانی‌ها به طور متوسط هفته‌ای ۴۶.۳ ساعت کار می‌کنند؛ رقمی که ایران را در میان ۱۷۰ کشور جهان در رتبه دهم قرار داده و افسانه کم‌کاری ایرانی‌ها را رد می‌کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/alonews/141923" target="_blank">📅 22:57 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141919">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TO6qct8arNK8fvxqKq25A86npfTRmYX7MbWMwgz0c7HxZTI4luR_rBZkmyT1XDPYMH5q9v7wBlvPN2HH1ZMJP4iI1c5w_Ri8Dc3KeM4XcHzWBkx0fxKGrlCUFAfDG0rPOj0M7f-0iCNfCm4c54ZgiSxnIgZ3xa-ZLRjYaLc-SlduVYmR-yu3n2InjwdpSsdQoAq5a39fXdZ6YJxz-HZ4MTiL-19CYlphK7YHExJ8VCmzcVMR01BdvlHwGYgeqnlwJOCOez4BETg_DedXF5LGW-QEXE2LOtxLGC-FduaYLLI8-elytWB4N4QUH9mhrRMcGmmndAqdl-Qg6THFB4GGlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RrlOA3CF3TaZvCIXM2Ta3nALc2LDSh3mqYHYoz7u6qsadewL81jyIZnafB20On_brhr-mh07aPyV0q_Ji7joa6OEE75VvVZkH1713hWFr1W8gzbwhRsxyLTv3kFPDs4Vp1u_7BR-b9iOYdhWpwEzV8nLdqGdY8urnulKL-Unj-jSwFxNPzvLIM4MUK5FcHcmsRBP825n0qdDZbsrldznR8jIWbvGm3JZnXTjkTx71fZ5UJ7vNg7bK1-D2EjhYAMKcvSMVrMXhOY9zD6pHuEVVOH5KxPMgNYj4U-57bPBgm1KSF5TvGE4PRcrS6baHTdNiCc7eS_eaguR7qGVZlRWkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NM8dey-KYXoo_jyqd2XxbzQLaD86zbnsrke22dqcrqovGM11wZVP0O2bmJmg_XZklAyRCHbs5Du_9ekrF4hGJVZgM3fKynGoKfofB1Ttb6PGECQMemeCmTzuWIy7_7jgWLfVLUvSBMKpt4ATw9LD1tcJB8i4LmLMO_yw0QU9JX8PW5msOH6uOXqJzXxAMFV9UPQS5INsB3izEuAE0zBTCeVqnF9omYpz00hjb59yjMxeX3AtGBILafTy-Y1naLIiWqPs252fz3XQ6EEoZWp4z28v3Uey1YF6kue4VEVDpclBM-P1-OuqkUvhrOiDpmuGhUdEO-9VYDjfcwU4xj_D8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cNBod1ZueQ9rmQtIR3inlGZi_OE-TS7vtJKvnm8UxDQb_OGl7xsQIGgCCTNXCewkWO5UED1aCxcoF-SCQcHynCx1HUxdD4ugVTc_gtangoAmKgtjhMk76CPVnDVOz4VdDzEULDXai6aB1yPqME6DzQkQOABNEilHrAvd2q3CjjleONbHv0PLqEhjJY8S1PiZenP55UMx6RaYkC1ql78rBi5I_2hh4HUE1vPdctYuI5wNVhL-y33VA2BpbiO_JUutSl68qzKS6fOjR6RwISitM97maUTY2d_lwCbx3Vd6293m1OZCSalOUWTuChWbB8mT--6usV1NuiBmaVEjGX9yIw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">گوشی‌های جدید سامسونگ با قیمتای فضایی وارد ایران شدن؛
⬆️
گلکسی زد فولد ۸ اولترا (Galaxy Z Fold 8 Ultra) با حافظه 256 گیگابایت و رم 12 گیگابایت که جزو گرونترین‌ها به حساب میاد، حدود 437 میلیون تومنه.
⬇️
ارزون‌ترین سری هم، گلکسی زد فلیپ ۸ (Galaxy Z Flip 8) با رم 12 گیگ و حافظه 256 گیگ، از حدودا 300 میلیون تومن شروع میشه.
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/alonews/141919" target="_blank">📅 22:56 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141918">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e21c271cbb.mp4?token=QjczxxvMLaXAiaKh-skkwBpkpJQbzQHIJQSH9bk5Q3mfJdWewEkUNNSwCZfuLtOiWUtXWIdxxanL3deylq610c0Zymo-Y2fWHtlQN9yB-_zqv2F8YhRSSYdMToY75q5iGuYhuTCntb5RKjMhk5bH8azKZVMuWu_BuKu5FfD5VoUSmWiv-MMQpB8vFRKWOzqV0uxuttMTHx5pKJiji-dQBWJl4Jqfgyzo6QfZFM7Sq1sWvsO4u1zJpwFrNzeajvRKSB-iWWVPuQk89oEO3cOIib-2iLz2apoJ1lidgqbZk9UscweaHT2XYrEgBGt-SBJxpVabiVKL_cM5RP7SPpQENISZmUa43PSL63wj8EMFL4RzeJvLMd-Poevf1Z-N9sJhFV1FNCD7JJpAGWJzVaFnsuvmaQIaRutV9mZ3n7Q8g4Yz6xAT5AZqr1L8Fd0Ch9JgfnRNLS3gl0GR5DaABZ551uAughYk18A8RwqJ16G3vqJ9RHBXbuL_KN14EO2Wp7alokZJSkqPFiOcnttA7tAInl9DxatEQFX97f8F9G2DgIbgfZmwjqG9m-NaY5Nu5DFA8J8Nlule8pUIn9Ir81mT72To-upBcny4pblPu1zioULQq0Qcs5Vh4TDS6C-szs4TYHC47zPHm1NBwt2gLgoTvG3Q1eKNLprMXXelGYmKHS8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e21c271cbb.mp4?token=QjczxxvMLaXAiaKh-skkwBpkpJQbzQHIJQSH9bk5Q3mfJdWewEkUNNSwCZfuLtOiWUtXWIdxxanL3deylq610c0Zymo-Y2fWHtlQN9yB-_zqv2F8YhRSSYdMToY75q5iGuYhuTCntb5RKjMhk5bH8azKZVMuWu_BuKu5FfD5VoUSmWiv-MMQpB8vFRKWOzqV0uxuttMTHx5pKJiji-dQBWJl4Jqfgyzo6QfZFM7Sq1sWvsO4u1zJpwFrNzeajvRKSB-iWWVPuQk89oEO3cOIib-2iLz2apoJ1lidgqbZk9UscweaHT2XYrEgBGt-SBJxpVabiVKL_cM5RP7SPpQENISZmUa43PSL63wj8EMFL4RzeJvLMd-Poevf1Z-N9sJhFV1FNCD7JJpAGWJzVaFnsuvmaQIaRutV9mZ3n7Q8g4Yz6xAT5AZqr1L8Fd0Ch9JgfnRNLS3gl0GR5DaABZ551uAughYk18A8RwqJ16G3vqJ9RHBXbuL_KN14EO2Wp7alokZJSkqPFiOcnttA7tAInl9DxatEQFX97f8F9G2DgIbgfZmwjqG9m-NaY5Nu5DFA8J8Nlule8pUIn9Ir81mT72To-upBcny4pblPu1zioULQq0Qcs5Vh4TDS6C-szs4TYHC47zPHm1NBwt2gLgoTvG3Q1eKNLprMXXelGYmKHS8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
حرام زاده بودن رژیم جمهوری اسلامی و طرفدارهاش رو بصورت ساده توضیح میده
✅
@AloNews</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/alonews/141918" target="_blank">📅 22:56 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141917">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ugSOr5DlKxo_wOV6O_ueffSDZTsa3ByERBdpIUX_s6dudYIGo3eHrceyZ2ADxe-VEUWIvZ-WOzhh65xu4VQM_eCCOp5dXUCxjtNkzEZElcTG8lMzZxQFVwUvOVFTyF0unOV2UBy2ecN3592-PkKG8zqjur_ohUk1OfwzypQ14D2wdK3O84Cl-X0gmh6fbhC7Z-BRp0lRktrLm-xOTL0Ig4xpnhdOpY2ygRSWPQje7WBDBP1Yyjpks1PPaGHHagiuvqfdXPCpXeSZueuS6e-6p1m_SmbqrXAFgxHkDT20gdFRKZxeHgYnLkh3-NN_l8ybsKx0VpKHlI6U831FO4PWzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مدام از مصرف بنزین و صرفه جویی میگن ولی کسی اشاره نمیکنه چند ماهه شبانه تو کل کشور هر شب ،کاروان های موتوری و ماشینی تو خیابون ها دارن بنزین دود میکنن
✅
@AloNews</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/alonews/141917" target="_blank">📅 22:54 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141916">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C4ZghKHLDR8hw2Myj6mis-E5K5Q4r83FTnjjkM_bdGGq0YQbDyE1JvEFnLPoS8B1jGhVvgd4QONQmymVNEb_ngldDh5lveDVl0-hahWZUOA2mjUClW6GYB7o5yG3YZ1ThOX9YoahijpC5jf3RCpZYmD6ToHkHXbFst2VyzpiMVfxqoPvBAe0PUZJruKvf0UOupN_0lthkaDDm71TyzN-HbX4owcB1cUF0G8d560dc29jqisN7hdX67pr1j4SvNknoHEkGiscqfAy5R4TCIsCgPUDVIIgIvuEUWJ0IJZAt88kjBaf0yo5gEprt-8GGa6-HAR3Mu_iaEdttiGXkmFtpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
یک ملوان در ناوچه یو اس اس آبراهام لینکلن تصویری از غذای سرو شده در ناو به یکی از اعضای خانواده خود فرستاد و گفت که وعده غذایی شامل «یک قاشق از همه چیز» موجود بوده است، نه آیتم‌هایی که به صورت شخصی انتخاب کرده‌اند.
ملوان گفت که به خدمه گفته شده غذا «با هم مخلوط شده» است و اضافه کرد که لوبیاها از بدترین چیزهایی بودند که تا به حال چشیده‌اند.
منبع:
آرون پارناس
✅
@AloNews</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/alonews/141916" target="_blank">📅 22:51 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141915">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/114b809380.mp4?token=NBdpQ5ocb3inIRMFIBYqjldaKiVSGyQZELuTorWE2ktSaLflz21cZVyd5265CWjE8h8St7A25Qw3KkX2jh8FKqoWG8TYd-788VjWP83RNzP8XoCzihhNEq4bTJ9COSY6KbU4CYSm9xQ17xTJPLkoWqOVKGQprYrJZepPVBl9IsAC2GE8_0AGQ_LXtCKx3E90cCamikmc_m4bWsihrEiOWKaOFD0iZ-L507PkNfseOwpTG8zXZzEK0onYuha5taOmp7GqZ67T5KnXTXD_R3p_-rff5wrKulq8gC3Gm20ObsTn9FIPtBxxkLFD152hjWgLfKDfvdZ944DvIjSMcaDk4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/114b809380.mp4?token=NBdpQ5ocb3inIRMFIBYqjldaKiVSGyQZELuTorWE2ktSaLflz21cZVyd5265CWjE8h8St7A25Qw3KkX2jh8FKqoWG8TYd-788VjWP83RNzP8XoCzihhNEq4bTJ9COSY6KbU4CYSm9xQ17xTJPLkoWqOVKGQprYrJZepPVBl9IsAC2GE8_0AGQ_LXtCKx3E90cCamikmc_m4bWsihrEiOWKaOFD0iZ-L507PkNfseOwpTG8zXZzEK0onYuha5taOmp7GqZ67T5KnXTXD_R3p_-rff5wrKulq8gC3Gm20ObsTn9FIPtBxxkLFD152hjWgLfKDfvdZ944DvIjSMcaDk4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
رئیس سازمان بهینه‌سازی: اگر به‌جای خودروهای بی‌کیفیت و مونتاژی چینی، کل یک خودروی ژاپنی را وارد کنیم ارزان‌تر درمی‌آید
✅
@AloNews</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/alonews/141915" target="_blank">📅 22:51 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141913">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlo Sport الو اسپورت</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EXgv2KZiQCpvh5kLPSguX0DrsP9-hPPhe93aWtDI6nRZ__psjummyKoCOeLlg9YrqxHZ7qA3eucRCPxK86ZKLMLjYCRPkJI5S4ec39c4hIA9UUMT18vAMi4LmfXvIro51uQUkM5jBd3yZSAbHzjtuKG7A8TiB_GiDqI9uOcBqtj1JjMZPUtFqRhtVTFZ2S3DcKJZbWzCdlW1prcWx3nvwZXvCoq4f5ke3a7TgDqzFeTpfbbgjEUNtJlp5G94K4ngTasVDYSUpvztu_g6QeA2ZeSs3SVvUM03fjjXt1NmLymsTk3orv_QtfzEi-xlH35vxhpK5TXl2pBLQpPMJv5-8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MCHZFyn7Jc44SoBKN2B6-XaathlypH5HaD3lyVIKSD-vMV4HpcbGA18TINebP8lKca7arRnLWDvaj-Ph34MSm7QfMGVVtZcJjy6vvLQkSGmp5IbMnkConpkF3pc2J-XuHMvIZLF4O_B2UiHbhMXle0r8iLIHY_kIoOkPhwLLGutMdJ7oy5CBXgk80PIza721Sdzw2i6ALBHGRi32LnlYhthi4siSWcMHOGq4gGIML1re_QzbE0OdVsWeTH8txRtIEXIXFuK2hqMCOthiWn9c_SM9GwbudTNK1gua-saZ4s29eE0tj5QsiUGn4EffUn3clYmy9LexzPINlVnC9lVBBA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔵
حرکت قشنگ هوادار خانوم استقلال بعداز بازی دیشب
👐
@AloSport</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/alonews/141913" target="_blank">📅 22:49 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141912">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9f363f7c8.mp4?token=bK-2rkVMdIs-gtmBEEPwnASgg_inX7_xfkdKU6ZmWfpiDkXTL3mMaKlV5WlwHG2gxEt3XKtZ9J7WMF0ov1IzS8yc6Ve6CclSvUaLHC_cG9BfZ1beNeCvUPFb7gJXT_bDdXOBIRu-vWT0An69KtoBwJPEi3ZCVnLAie3lG8uCPv6ZALTYjeD5Hm7XnBkdZ1xyHi99U6ZWbyn7uRhiK-1n0mRYLXyewNrTX7klbF7lC-9xwF1CtJSZZ6TmYMXPTma6NyqWNCv-HWKIitMW6VtkfAoU7Kiny_HF8FrlezACaEOrYrbtAmDrCyJlEDhdN63JyVq_9wTsrvTQQmGa-kG2WQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9f363f7c8.mp4?token=bK-2rkVMdIs-gtmBEEPwnASgg_inX7_xfkdKU6ZmWfpiDkXTL3mMaKlV5WlwHG2gxEt3XKtZ9J7WMF0ov1IzS8yc6Ve6CclSvUaLHC_cG9BfZ1beNeCvUPFb7gJXT_bDdXOBIRu-vWT0An69KtoBwJPEi3ZCVnLAie3lG8uCPv6ZALTYjeD5Hm7XnBkdZ1xyHi99U6ZWbyn7uRhiK-1n0mRYLXyewNrTX7klbF7lC-9xwF1CtJSZZ6TmYMXPTma6NyqWNCv-HWKIitMW6VtkfAoU7Kiny_HF8FrlezACaEOrYrbtAmDrCyJlEDhdN63JyVq_9wTsrvTQQmGa-kG2WQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
رئیس سازمان بهینه‌سازی: اگر میزان مصرف بنزین خودروهای داخلی مشابه خودروهای روز دنیا بود الان شاهد ناترازی در تولید و مصرف بنزین نبودیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/alonews/141912" target="_blank">📅 22:49 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141911">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6aabb4acf7.mp4?token=FfTk-1Wn2MTJ7rnVgbpdLrM-LVNxGp2j5mwirTbkQMhV6M0P1a64u-1fL1Z4IlRPMmBxwCkhM-uRXEQqJOAf_TzOp2xp61gXl8j-e4glJjsDX6d5chzT2pt2QhCDZMPLAsG8u9pz0953JMFDN0RUuFUoOF1ldzGnHSsXR7Tz8DoK45Ej_dd8NAOMi1tTNuCJDXvDfxL-nBI9LQ9PenhhiSotH707E1oh2vGCavOI_Sl2tqgBePdpz9WPZL1XCBNJjBnCqaizzOxAG9Zu4un35Ug2e0MgwMHCTwBoHSw9UlYiqwGEElP7dJBd_OULNxdtCTKOxctqgyQnQ6pL-kxaJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6aabb4acf7.mp4?token=FfTk-1Wn2MTJ7rnVgbpdLrM-LVNxGp2j5mwirTbkQMhV6M0P1a64u-1fL1Z4IlRPMmBxwCkhM-uRXEQqJOAf_TzOp2xp61gXl8j-e4glJjsDX6d5chzT2pt2QhCDZMPLAsG8u9pz0953JMFDN0RUuFUoOF1ldzGnHSsXR7Tz8DoK45Ej_dd8NAOMi1tTNuCJDXvDfxL-nBI9LQ9PenhhiSotH707E1oh2vGCavOI_Sl2tqgBePdpz9WPZL1XCBNJjBnCqaizzOxAG9Zu4un35Ug2e0MgwMHCTwBoHSw9UlYiqwGEElP7dJBd_OULNxdtCTKOxctqgyQnQ6pL-kxaJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سقاب اصفهانی، معاون رئیس‌جمهور و رئیس سازمان بهینه‌سازی و مدیریت راهبردی انرژی: نرخ مرگ و میر جاده‌ای ما ۳ برابر کشور همسایه ما ترکیه است، با اینکه جمعیت و تعداد خودروهایمان شبیه است.
🔴
در تصادفات هیچ‌وقت نمی‌گوییم خودرو بی‌کیفیت بود و هزینه‌ای برای خسارت او قائل نیستیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/alonews/141911" target="_blank">📅 22:48 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141910">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👈
واشنگتن‌پست: متحدان آمریکا در خلیج فارس درباره اینکه آیا واشنگتن می‌تواند به یک پایان دیپلماتیک برای درگیری دست یابد یا نه، تردید دارند
🔴
مقام‌هایی از عربستان، امارات، قطر، کویت و بحرین پس از ماه‌ها حملات ایران در نارضایتی خود اتفاق‌نظر دارند؛ برخی از آنها درباره ارزش ادامه میزبانی از تأسیسات نظامی بزرگ آمریکا نیز بحث می‌کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/alonews/141910" target="_blank">📅 22:46 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141909">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
طرح اول پیشنهادی دولت برای بنزین چه مزایا و معایبی دارد؟
🔴
در این روش قیمت بنزین تغییر نمی‌کند اما بنزین تا میزان تولید ۱۲۱ میلیون لیتری در پمپ‌بنزین‌ها توزیع شود و وقتی تمام شد، نازل‌ها خاموش می‌شود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/alonews/141909" target="_blank">📅 22:46 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141908">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-poll">
<h4>📊 🔴تو شهر شما هم عرزشی های حرام زاده موتور سوار، زن و بچه مردم رو بخاطر حجاب و پِت اذیت میکنن؟</h4>
<ul>
<li>✓ 👍بله</li>
<li>✓ 👎خیر</li>
</ul>
</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/alonews/141908" target="_blank">📅 22:44 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141907">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
رئیس سازمان بهینه‌سازی: باید کلید اصلاح تولید خودرو را محکم بزنیم؛ نباید هزینۀ مصرف اضافی بنزین را از غیر از خودروساز بگیریم
🔴
باید شماره‌گذاری خودروها و واردات خودرو تعیین‌تکلیف شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/alonews/141907" target="_blank">📅 22:43 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141906">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👈
سقاب اصفهانی، معاون پزشکیان: تو خودرو سازی از اول انقلاب اشتباه راه رو رفتیم
🔴
پ.ن: تو ۹۵درصد زمینه‌ها اشتباه رفتید
✅
@AloNews</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/alonews/141906" target="_blank">📅 22:43 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141905">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
گزارش صدای انفجار در سیریک
✅
@AloNews</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/alonews/141905" target="_blank">📅 22:35 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141904">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
گزارش صدای انفجار در سیریک
✅
@AloNews</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/alonews/141904" target="_blank">📅 22:29 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141903">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
سید عباس : آتش‌بسی وجود ندارد که بخواهیم آن را تمدید کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/alonews/141903" target="_blank">📅 22:27 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141902">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">👈
سردار باقرزاده: 3 خلبان ایرانی پس از سقوط جنگنده‌های سوخو-۲۴ در جریان حملات اسفندماه، زنده توسط نیروهای قطری اسیر شده‌اند!
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/alonews/141902" target="_blank">📅 22:19 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141901">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
آنیتا آناند وزیر امورخارجه کانادا اعلام کرد ابراهیم عزیزی، رئیس کمیسیون امنیت ملی ایران به دلیل نقش داشتن در فعالیت های تنگه هرمز را در لیست تحریم های خود قرار داده‌اند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/alonews/141901" target="_blank">📅 22:18 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141900">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">‏
👈
الجزیره: کمتر از ۳۰ ساعت تا پایان صلح ۶۰ روزه بین ایران و آمریکا باقی مونده
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/alonews/141900" target="_blank">📅 22:16 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141898">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/aGUrS6G9jOmswtB-hsBBRKLdriiZKvRmhB7d2EtrAHXqF5KNT92A6gaGBh8lzBQmUW74TJ2QEGj2h-0e3zKzIHaIld5YPZeZ4fZyrlNljg1WTFHHWHpaMUgJOePeEp-LJy7NXtCVowZuNYT-AciJAnnhp8hVwCzHZxR9uGr2UP1130LVjwC_vVAhVP43ixnsBeNZ1ggbr3qmcVroSTBLvEEYVxOpBudpHg3TW-NslaYZDleaym_wQjjYa3fMojjF83Y6FOWPF06OEivxhmvgN9CVS8oVqa3o5K0h_--Qw8yzCO-RqeP8V9VfTLnU3SDS8UqkRUGWUPli5dobFFvS2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/vaO9BZuvA9PqmZbQAGrJH1eR04IJUodvRfTCpVvI0--qovcKuSPbiKRfB10xWLFUIxfSFWdcQ_r1zaGutySbiM56cpB6HgQwjzYcpiQgTlC2YyBTLwbFdkinPdqClKlwmLFKvgbpgI0a3m6XGmeIVQZFk_b4VJhe40rMhnuir3dfsLtVbWW5kSLQqy1rClNzyME_g5y1T6_et97PCW5tqbXy6ZQn56P081aepaI_msJ_aMW6YtCRh1F16o7J9U2y5SBNWZApGUmwxkXFi8gcGNKkJD5_6jDzTyiIlzB2JuWsy2BAkcIEgD-6F4RXpMCF3nFLOxAlT0cn7vdBwcekzg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔴
در زمان قاجار دخترارو بر اساس سن طبقه بندی کرده بودن:
دختر بین ۹ تا ۱۰ سال : خانمچه
۱۲ تا ۱۳ ساله : نوچه
۱۳ تا ۱۵ : غنچه
۱۶ تا ۱۷ : گنده
دختر ۱۷ تا ۱۸ ساله:ترشیده
+بعد ۲۰ سال رو "پیردختر" حساب میکردن. و فقط مردای بالای ۶۰ سال به خواستگاریشون میرفن
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/alonews/141898" target="_blank">📅 22:15 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141897">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🔴
این هم وطن
انزلی چی
ما حرف دل یه ایران رو زد.
🤔
قهرمان های ما همین مردمی هستن که با این رژیم سازش نکردن.
✅
@AloNews</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/alonews/141897" target="_blank">📅 22:14 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141896">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8994c2f3c6.mp4?token=oEDumC6KS6Gn-VVS0hLAE80Xn0TN0cm4_89r1PDAy7JNjljm-wNhT5GF4Rr1f61AIDQWpCyeYe7XM-5uMAjfXQAnvEKtCGoc1I59wJm5_UD9BZoSm-Tr92KaaPIfhTiul_KjX3D-wl15ub9CGy3yYLJtg28KTaXdqKFudsP7BhxWy_DOkesqBbu1kYXf1AbX8pyTxC9HaR3ewZUCDPtbghHsVSlgbpgvm4G_6F0v0QUUUz8JvchTQRsiBbm5GEPl4OBsGyM0lim7LMB19vfCZ7XG_4C98OdMo480wLWhrRhi6VYEYczbCQsxacYY7nRigO1Od2IL_6oW5BUgVksyJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8994c2f3c6.mp4?token=oEDumC6KS6Gn-VVS0hLAE80Xn0TN0cm4_89r1PDAy7JNjljm-wNhT5GF4Rr1f61AIDQWpCyeYe7XM-5uMAjfXQAnvEKtCGoc1I59wJm5_UD9BZoSm-Tr92KaaPIfhTiul_KjX3D-wl15ub9CGy3yYLJtg28KTaXdqKFudsP7BhxWy_DOkesqBbu1kYXf1AbX8pyTxC9HaR3ewZUCDPtbghHsVSlgbpgvm4G_6F0v0QUUUz8JvchTQRsiBbm5GEPl4OBsGyM0lim7LMB19vfCZ7XG_4C98OdMo480wLWhrRhi6VYEYczbCQsxacYY7nRigO1Od2IL_6oW5BUgVksyJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
زندگی یک ایرانی در ۲۲ثانیه
✅
@AloNews</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/alonews/141896" target="_blank">📅 22:09 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141895">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">👈
طالبان هم فهمید برای پیشرفت باید دنبال رابطه با دنیا باشه و جهاد رو بزاره کنار اما جمهوری اسلامی نفهمید
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/alonews/141895" target="_blank">📅 21:54 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141894">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/19a93bd565.mp4?token=IBtCPvuzRVLtKd-j8GqIBf9dkv2wmhk6uqTfi67ea4JOp5Eks_uS8XJ3Rp4DLYbWmpxf8BlT0MwG-q04kCszAzZN89AU-SyEE9OCTrecR3sGW2FSbWbITa7E6g6_T9gCKQgnQijAeSh5-AVw6QAxP9XzqBeN_UMJmjqcK-SGVwX9z9rmkzIQS8I20haIknKGiBZOaRM_GBUdzJi3K58zWtsD1TCHcVWxCLi14XUjYWBnFG51oildI3CMNrqOqNOjMQHKQnXLy96m5KaDahC0RjdKso5TiDC2Gfei-NRlkWW77ZOAJ6hAwJS-YswXEPm_-VhoL9Ar66QrLvJXMVheTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/19a93bd565.mp4?token=IBtCPvuzRVLtKd-j8GqIBf9dkv2wmhk6uqTfi67ea4JOp5Eks_uS8XJ3Rp4DLYbWmpxf8BlT0MwG-q04kCszAzZN89AU-SyEE9OCTrecR3sGW2FSbWbITa7E6g6_T9gCKQgnQijAeSh5-AVw6QAxP9XzqBeN_UMJmjqcK-SGVwX9z9rmkzIQS8I20haIknKGiBZOaRM_GBUdzJi3K58zWtsD1TCHcVWxCLi14XUjYWBnFG51oildI3CMNrqOqNOjMQHKQnXLy96m5KaDahC0RjdKso5TiDC2Gfei-NRlkWW77ZOAJ6hAwJS-YswXEPm_-VhoL9Ar66QrLvJXMVheTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نیروهای یمنی مورد حمایت عربستان سعودی از یک پهپاد انتحاری (FPV) برای حمله به یک خودروی متعلق به گروه انصارالله/حوثی در خط مقدم جبهه استفاده کردند
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/alonews/141894" target="_blank">📅 21:51 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141893">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e32c238411.mp4?token=gQgdcSkDKMK1OxAkCpKDX7lL0behGXyUREODHKamZp3Pk12CBOCS4u39Zprj998nBs4gihTlxdQ3QOn3WiqO7Ce3CtRqC_xH6eyHIgFRk1oKs06WFBhXzkd4Id80dAu9WETW4YYskK58rb3p9WP-mWAF76e3-pa2XrHGo_IV1pM38tJ-ghd0CCMK8_NLfteSfxg1eV8xPJ9pBx-HG0nGg2JBGThFqfqqPpEfg8Tbs9C0SwxKcSI7MPbhQwOzNC7Stt8H-OjaDfboCGwenML5INg_o6cI2Sy15iDvwPmRcDd0q-ANIvkWB1DsFKoIhRrMEibzJHzXZp2vOLdPoH4QJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e32c238411.mp4?token=gQgdcSkDKMK1OxAkCpKDX7lL0behGXyUREODHKamZp3Pk12CBOCS4u39Zprj998nBs4gihTlxdQ3QOn3WiqO7Ce3CtRqC_xH6eyHIgFRk1oKs06WFBhXzkd4Id80dAu9WETW4YYskK58rb3p9WP-mWAF76e3-pa2XrHGo_IV1pM38tJ-ghd0CCMK8_NLfteSfxg1eV8xPJ9pBx-HG0nGg2JBGThFqfqqPpEfg8Tbs9C0SwxKcSI7MPbhQwOzNC7Stt8H-OjaDfboCGwenML5INg_o6cI2Sy15iDvwPmRcDd0q-ANIvkWB1DsFKoIhRrMEibzJHzXZp2vOLdPoH4QJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
شهردار ایندیاناپولیس در آمریکا از ساکنان خواست که از راونزوود، راکی ریپل و سایر مناطق  به دلیل سیل شدید که بدترین مورد در حداقل ۳۰ سال گذشته است، تخلیه کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/alonews/141893" target="_blank">📅 21:37 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141892">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">👈
پس از حدود پنج ماه توقف، پروازهای مسافری فرودگاه بین‌المللی لارستان با برقراری مسیر تهران–لار–تهران از سر گرفته شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/alonews/141892" target="_blank">📅 21:30 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141891">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gg7DPs158zvpCY9eAvEgN_ZL-VdUREFyel35ZjqPBgqlaR7pBEC9HWIlqZ7BnX7dQlQL3-EURjg2h0Egvrm5r8wbDWIBlLIRsjg83F-s94n85NXhZ5eKlPal3_bhp1uKZM8sh29lCVIP9-PtGaQeVl8JvA123XdEfZMJeqB63CInr88iiB6fNYAxFxIlgON0ogxNLCPubH3HFd3bmHNbYwQVgmx7GZD4mmYLC1pRkb0JjC4AEiUrVevVQI0mmAJCNbmGSa1wvNM_6bhrgpuk_GVCXUEXVnRmmwecZDxMnToZaFPeDDkRJe-4mRobd7y-4_Mv1ASWamMUmT1-ydiMLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رئیس‌جمهور کلمبیا، اِس‌پریِلا
:
کلمبیا با اسرائیل، همیشه دوست و متحد بوده‌
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/alonews/141891" target="_blank">📅 21:27 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141890">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XtaiXTvA8qmnqSPqrnqZSlEQFvDJtnlTRuNJmoASmbDrwSJWqB6QOFvdYWDdgUEgrR0kHse7lZEZblEdGWeXBxylny2GUZn0xIQKAJkhlFbaBXcT3yeiFCfEumw_3eImg1-1DzWzhgSMN7L-hXl2m4V3K9yCkUV_JVVd17As7yRc9EO4e2ZZqg7JP6fOBebxlxPjEO1W0q-Ba56SocK8iji45EnkT9dWiFLH7C4TxbQqCrTNi9Rv6-Mo-ch8kEa0-0c_gzCGyIQeDE38r3WUSdM87sBrlvwscwcxKkt7FVD6g7m9BCIvl_Q58F0goZFnP2pKHk7BAR_oYNz7LDP_xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نبیه بری ، رئیس پارلمان لبنان : اسرائیل هیچ ارزشی برای هیچ‌گونه توافق یا قانونی قائل نیست
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/alonews/141890" target="_blank">📅 21:17 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141889">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Eoyr4n37iOlNvUZq6TXtBbxZiQcKvLbnpbi_xzeG5mgYQNzVv85M6fOk7Fc4l8X3xdDPpWgBrJS4quccU6q7P6MyBj_xEOkJRmAAzhxcOYcjuQ_RCykPq7gkvC-vTOunhyp2pOQqWOQyGuNaaUoBGXKojXWHMZNmDAVYso7bdQZbeBeDV9H2BVAZYXdF2_xmPao_QQHC8MvHj4gp-T_BoKrAjBunz95V8AzNdHlu-06tYC-blbgZMo3prQ52EbpTdh3dHyt5V0Cd_rI8FaUBdycnF-P4x0KnJdfgUH2WAUXqjiLI1GO5cfmv8pDeQV68cbYgm9BN_15R3xLpJj5QbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
در ساعات اخیر انصارالله یمن حملاتی به دو پایگاه نظامی صحن الجن و تداوین در استان مارب انجام داده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/alonews/141889" target="_blank">📅 21:12 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141888">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">بچه‌ها این گردونه صراف رو چک کنید، من الان شانسی زدم ۵ دلار بهم داد
😐
😂
انگار اصلاً پوچ نداره و به همه یه چیزی میده.
برید بچرخونید ببینید شانس شما چیه
👇
https://r.saraf.app/s/agrd309</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/alonews/141888" target="_blank">📅 21:08 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141887">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GPt3O48LMG2-u5-iKjyU1C995miQCGVc_lHlkJ4QuxnxAwFK0Hbaqo5n2HNLw9Jdd0cHcIZVZjDwxyk0tRoUbjqgAbXwEq32k1eWLQbg07TtSb2D7miMyOlSnQilrqBwuQITAiXDxIFQgEhf_S6ivI9UaWH1xUyEo4MfrHyWL2Erv9Nhr6lvw8-jZq0A5nfD0tuCrY0yR2c5HQ0kHip-ObichFnON_yXAllo0QQqxKyQwpP62k5oUsGtDj88py7e4HxD8IdaG1sI5w53P4YuIm2zIHH390njByzvnYhzN8M_gVIFpCBIZx94o69PTLIKGPxqoLjgaFXOUhBaP4wBtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
👈
اندی بیکر، مشاور ارشد امنیت ملی کاخ سفید و از افراد نزدیک به ونس از سمت خود کنار می‌رود
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/alonews/141887" target="_blank">📅 21:07 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141886">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">👈
آتشبار توپخانه اسرائیل به شهر عیترون در جنوب لبنان هدف قرار گرفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/alonews/141886" target="_blank">📅 21:03 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141885">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I40bByWKOF2fdlMkOXtX56jpvDa6T7tntzr5HUtX6F4o1uWLpZnY5ONPJG5RYv_D8L6DbomjwCoqQDqyL4weOKIcwbLidShB5xVCuG_68JLRW3Gh2ZVv_bAQfo8bY15T57jo_STsWNrIJida9ZTCH_-9KeNQ7zPZoFboWU4VmbARGe8UEpFt0DC8kmws9JeRCCrub_ghcqcZJutY0jPDsEXML2Iv7GwHWiiBvLPN1ra2XgcLkhXOPAOene7U2GyOpllO41XbFLaiQHGGiP0bXvFH9F9pwh1ZZYpRRmBM9_5QIIWdrSNZfDohwFAebSaTxPAndV1SwtkEvbCoonWfgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
انفجاری در طلوسه، جنوب لبنان، به دنبال فعالیت‌های تخریبی اسرائیل مشاهده شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/alonews/141885" target="_blank">📅 20:59 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141884">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
زلزله‌ای به بزرگی 6 درجه در مقیاس ریشتر جزیره «میناهاسا» در اندونزی را لرزاند. این سومین زلزله بزرگ است که ظرف 24 ساعت گذشته در این کشور رخ داده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/alonews/141884" target="_blank">📅 20:55 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141883">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DS7qvOWA5y9gslBzDyf-XK7ZQy_IRBcnH6ZDHBD5GbL_bzU5Njp5Kngb0gpH3iTQXL2ul1Xpf_9U9diHBq-Ttbh2eH5WOHgAWqAaKTtvLR-7WfY3JgsBRyxxFgSyV6In7frVHpB6AHejfoFSNjcR0uIaZuJRwBTE-AzmThVBPjkkbhtAPPovPJJUGbvyCdhbjoG5zlfBBO23T5h7LWA2lAaNd-B4nU__YcQNGRSA61V1mxUxSma1j2gH5QJHBgCMFHVVTitVnIC506NYa88Ke4mOixRHN70KJNLnrrvaGXVaYL-wxsjIkeX7M3B7p-SZI3VB4oypTBu9hvQERl5zTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نورنیوز: ۲۶ خرداد، تفاهم تهران و واشنگتن شکل گرفت؛ ۲۷ خرداد، در منامه مقاماتی از آمریکا، اسرائیل و امارات دور یک میز نشستند
‏
🔴
موضوع فقط تنگه هرمز نبود؛ مسئله، جلوگیری از تثبیت تفاهم بود.چراغ «اتاق تخریب» درست یک روز پس از «میز تفاهم» روشن شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/alonews/141883" target="_blank">📅 20:51 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141882">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/txT31zW3PMDX5b3S-4sF3hDryXa0bNBQo4uGlyX-zRHMKtiZBRczSsoyTD3kQfsJ7g6MSEBF0jOawcq9R6EmKh-M_BmIBpvjrsleArh2sx5UiPF8IYJuEqK951FVon4DFpKRm2q_nNj_iK-wPHQWjEM-f2UxMS7jCpM01HR1yhyqYn1S685aInCfyQ1YdVo3UgWaJARX8aBuN2DARRCC8wLayv93uLmTQzTaUSgs57vwwKPFXXH3hALrPFjxBT4kB1PzG9OCtk2CGoyqBcdnFTCuDa1AeAliFyvShRYnZf1TIsvbk2LlH22wuPqHmJdHQSdOrKdZXhhIMfxKcImmpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حماس اعلام کرد دفاتر خود را از قطر به ترکیه منتقل می کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/alonews/141882" target="_blank">📅 20:47 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141881">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9091137d97.mp4?token=uy32GdfhMJjeszCzwN0JbXTKNJHEB9j6SCkAXCUjvDU2C_abbwUk9U-tAdIQEvOt4S_REWa2kzLzgMeJyl6vtPwFKHwHaT_Or-d8gx1SIEGP3RJshU5PBZx-Vwid04jVRwD35vHRMr85FVYnk2DDlbQPPsTIRxwdT1koFZ7RlTsVDSZduQtJNr1ho-6H3B9AxY9LTB3P4ZYs2xzQxl36F3xI-ZkJaGiVlxl3btHctkf0VC_ltzMpdsjMQtA3hGJp6eitgvHLIKBPbZCtqoELySpqPnsVckplz40YWhmsdgnV2boe_KtG5jGyfHGCNV1l0DUQmPVOL5n1blnoVejXXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9091137d97.mp4?token=uy32GdfhMJjeszCzwN0JbXTKNJHEB9j6SCkAXCUjvDU2C_abbwUk9U-tAdIQEvOt4S_REWa2kzLzgMeJyl6vtPwFKHwHaT_Or-d8gx1SIEGP3RJshU5PBZx-Vwid04jVRwD35vHRMr85FVYnk2DDlbQPPsTIRxwdT1koFZ7RlTsVDSZduQtJNr1ho-6H3B9AxY9LTB3P4ZYs2xzQxl36F3xI-ZkJaGiVlxl3btHctkf0VC_ltzMpdsjMQtA3hGJp6eitgvHLIKBPbZCtqoELySpqPnsVckplz40YWhmsdgnV2boe_KtG5jGyfHGCNV1l0DUQmPVOL5n1blnoVejXXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
کمین جالب FPV روس علیه نیروهای اوکراینی
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/alonews/141881" target="_blank">📅 20:33 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141880">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👈
نیویورک‌تایمز: اروپا که نگران است ترامپ بدون حضور کشورهای عضو این اتحادیه درباره جنگ اوکراین مذاکره کند، در تلاش است تا جایگاهی را پای میز مذاکرات کسب کند
🔴
فرانسه، آلمان و بریتانیا در حال تدوین موضعی مشترک هستند و انتظار می‌رود که کشورهای دیگری نیز در این روند مشارکت داشته باشند
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/alonews/141880" target="_blank">📅 20:28 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141879">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K-vD86uJR_YaJVVqrh6Eor2l2JrpijxLLOiQEeDebFOsNhh2H_pAYaDIcWmICjviNPuLus1f1wT3ga6I9c_SlKy4ugR84OzYcrot-bATvx2nHZ3oxn-2_FDrY_NbBC44H2dD55ogGKVhUqV9X7gyYPSCJI-Fa48xPO2BPC-TtJR3ZMgR64YN0kAf57AbTBuAz7J9Z_0xqVMNhMDJAKLug1HYc_SwHQV_nSvPKp2hGGS0mOmUdMKlXbmzlH4_iqQvZtt35kyzeGrGRH5OnDAXK6fklrT1x-vTke5UKX8F7R7MGwBJzYWgJ_jvxKjMuevGE8UEtICOF_mPZ0tk_T19mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مایک هاکبی، سفیر آمریکا در اسرائیل:
نیروهای نیابتی حکومت ایران شرارت محض هستند. حزب الله کودکان را جمع آوری می کند و به مناطق نظامی می فرستد. آنها نظامیان اسرائیل را می کشمد با اینکه می دانند این کار ها بی پاسخ نمی ماند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/141879" target="_blank">📅 20:22 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141878">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HJJ2e6bwbb5_2bdBAOs9PJxdQTJp8Ns3wMtTKtJP9Dn2taY38j0IJPb0SUmn1UJdP9hfdBxLnpJ2nsavSFxOwX1RrG40IPeaqmmdWL1PZos2QBe-rPT-weeU2_s0OYVUl7GmT2L-AUYzP08m-PhZdG32tpQXo9z9Ui0JuDe1SCteFs_ozGifzMjIyIFgZ0Ku5Ba18AdGr04mPDz5pXrDDrhJJl8qyRYtoh6kaZ1w_-1Vo3ej2hF6coOexXalWmWx5JYcxiSD88J-MUM50vXATWWBPzEl2N4pDocWTxFyhTzEjt2FcI85c5m1tqmIcwLe_vSb9Ntxh0hycFYI8UoMRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نظرسنجی جدید شبکه CNN: محبوبیت ممدانی در شهر نیویورک در ۲ ماه اخیر ۱۱ درصد افزایش داشته و به ۶۹ درصد رسیده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/141878" target="_blank">📅 20:19 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141877">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">👈
شبکه ۱۲ اسرائیل: بر اساس اکثریت قریب به اتفاق نظرسنجی‌های فعلی، نتانیاهو در این انتخابات پیروز نخواهد شد، و آقای ترامپ و مشاورانش از این موضوع آگاه هستند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/141877" target="_blank">📅 20:15 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141876">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
سوپر اپلیکیشن "بله" از پلتفرم های ایرانی بازار و مایکت و... حذف شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/141876" target="_blank">📅 20:10 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141875">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">خبر عجیبی که دقایقی قبل اومد
😐
👇
https://t.me/+nCexQYLuuONhYzg0
https://t.me/+nCexQYLuuONhYzg0
دلار و طلا میریزه
⁉️</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/alonews/141875" target="_blank">📅 20:08 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141874">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M7k3DY2SSDE9bVz2ppjYefy3CkEtCAZJghaDtX7VgkkgYGVZOZmzqm1_8lcCCUkAIUyonhng9QCE_Hs9yAHdCq3VJGLQwO-7R_IpZJqt4gExYWokAcsYidr8nYn1Hfp9vwK-bJBzT-6HBNwlaDDgYxencB7kaX7WIZT5bYTs85EDg9gt39IAskW4V_VGIcuCOvm6QAvIgcAdKkhXlmNQbIaU5L5K6aPb3TaIMRk-QyW5EKWKHV18zZKYasF-POnrBBwsk0wLyFPr3bxonEjVpNOaMvMtW9XAfOJ_4fOJOx31M7A65XgOfqtzFe9nO-b5EG5hfc6mgC_HGLcFp15Kpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
خبرگزاری تابناک، سال ۱۳۸۷: خیز دلار برای گذر از ۱۰۰۰ تومان
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/141874" target="_blank">📅 20:02 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141873">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">👈
وال استریت ژورنال: کاخ سفید در هفته‌های اخیر بیش از پیش نسبت به دستیابی به یک توافق نهایی هسته‌ای با تهران بدبین شده
🔴
دستیاران ترامپ با ارائه داده‌های خسارات تحریم‌ها، او را مجاب به تشدید فشار اقتصادی به جای جنگ کرده‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/alonews/141873" target="_blank">📅 19:49 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141872">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WuYFUPTFISadT7MG_99X2sseMIBDaJQwebp5pP6A82X2baZk_8nLfih422sk9DVzVwK-F0QhybmZi4EhA-2C77i27U_2PVOXi_llTUeyfl080hc9mySyweXHegB3aevbYd6JPb8woZJtSmySXgVUiEiyFc1Z5MOqRbM5IO7OSmz8MeMdsenFhhSSlQlTvloc0OKIJI4Arjn1w9DbPB8tEG2Y1XICkJxaiA4NnXULx4oCB8tqbbN60a7ZgDnYWxLV5vJQh1uulxtTJcGi9N3wBGg8GjDbSFectTxr53_Wgq20P30G5aBVfOX_su3yN4W6j7PqmOi5q6oKr1OaXkAY2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ: من و کیم جونگ اون خیلی خوب با هم کنار می‌آییم!
🔴
‏دونالد ترامپ درباره تصویری از خود و رهبر کره شمالی نوشت: با وجود نگاه غیردوستانه در این عکس خاص، عکس‌های زیادی هست که در آنها لبخند می‌زنیم؛ من و کیم جونگ اون خیلی خوب با هم کنار می‌آییم!
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/141872" target="_blank">📅 19:32 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141871">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/okBkzBDNN-JsajLPk3sBBR_bHxZV49mG-owWy7J8lGLIykQVMwD8LnlCMvOVSXGNLEGwiTFgR_a4eSMjrt5_DP0TZJdA8qLrjz59Wf6gUChHXUWhpxMdZawIIwkjUXmdlbo0tajkRPq7Ao1PGNWsOc3kRvCaMtYr3laHdU6PQGRbNIWCKyN39m9eRNP6p_nbuL8nDeNg5S7O-cK9o9ctAq7z9HmoZl-TmkkSYO2VeyiLfC3rVwycw-NSkDiog9iiZdhndYgsY2LOvwLaITh08QYXIoZeia6DU0KP566f5GzfcOQsznw9sK2M8PWsW1LoNXUVrbpCDx1BeE2Hnou7UA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حزب الله لبنان در بیانیه‌ای اعلام کرد پاسخ حملات سنگین اسرائیل به جنوب لبنان را خواهد داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/alonews/141871" target="_blank">📅 19:21 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141870">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/136da7e3a1.mp4?token=hHX4p2vnKwhnScbRRWnUNaboxS_7oUbbh_QIxzW2UDp8B5Kd3vJ6huHmj8lEUO3CEiya0b9la7X2Ngq_Epets6pQWlH1LfPtsqdmPx3U-b9Tso-_uiR_QEf6Sb5Ox0FZ76h5CdDChM1w3Ee3fv0qQtHheSXbH3lA0gmpx2AccQyg27fcZve6_6VN4vpgm0I_QNe3X-ub1YWHgdEICTV9epLIQYecB6ZGpgqtvCe-iqgz6WISajNHASWyGSjBSgC3_7QIHaU6xMY2MFj3M7XPc7Q8r-6-fkQCTtEcyMRrvtE2Jd5j03bkrK5KFB5ofx_Ge9qIjjyg8TxGgijm2JCMxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/136da7e3a1.mp4?token=hHX4p2vnKwhnScbRRWnUNaboxS_7oUbbh_QIxzW2UDp8B5Kd3vJ6huHmj8lEUO3CEiya0b9la7X2Ngq_Epets6pQWlH1LfPtsqdmPx3U-b9Tso-_uiR_QEf6Sb5Ox0FZ76h5CdDChM1w3Ee3fv0qQtHheSXbH3lA0gmpx2AccQyg27fcZve6_6VN4vpgm0I_QNe3X-ub1YWHgdEICTV9epLIQYecB6ZGpgqtvCe-iqgz6WISajNHASWyGSjBSgC3_7QIHaU6xMY2MFj3M7XPc7Q8r-6-fkQCTtEcyMRrvtE2Jd5j03bkrK5KFB5ofx_Ge9qIjjyg8TxGgijm2JCMxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سربازان گردان موتورزرهی 64، که بخشی از گروه نیروهای "وُستوک" هستند، به شناسایی و هدف قرار دادن نیروهای اوکراینی در منطقه زاپوریژیا ادامه می‌دهند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/141870" target="_blank">📅 19:12 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141869">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👈
شجاع خلیل‌زاده: گل من به مصر درست بود؛ شاید ترامپ گل را دستکاری کرده باشد!
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/141869" target="_blank">📅 19:05 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141868">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
سازمان تبلیغات اسلامی: تجمعات تا هر موقع رهبر بخواد ادامه داره
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/alonews/141868" target="_blank">📅 19:01 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141867">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">👈
به گزارش ان‌بی‌سی نیوز، دونالد ترامپ نگرانی خانواده‌های نظامیان درباره شرایط دشوار زندگی و خدمت در ناو هواپیمابر «یواس‌اس آبراهام لینکلن» را رد کرد.
🔴
مأموریت این ناو در خاورمیانه به دلیل جنگ با ایران بیش از زمان برنامه‌ریزی‌شده ادامه یافته و همین موضوع نگرانی‌هایی درباره وضعیت خدمه و فشار عملیاتی واردشده بر آنان ایجاد کرده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/141867" target="_blank">📅 18:55 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141866">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TkHQaR2iIPwLXz4aB5sYrKzJyFgckeizZeRg3NIYDb7_KA1euHQ1_nZigdLNdz-QcX0kdjHTBDRqtz34Z2UTDquSs_T4g6TKBXLt3fDR64ZfJNI8XDoJW5SUw8qf1TIBirdweLaIb90LBBpe3v51ZKZ6yJw7QAb9gGj4OyUwK0E8hEVdMFykeUvTW0hW7qP2HxlxljnCNSnNozx8fMPfMKe2zfoplCiuzeywRqcw-BU61nrJ-YjoSw6afCRfJ0890ylDYd24KfYb6x7BHw9OOf8qz-ArPCFCh1L-dp4S5USPcRV-w9v6YVYlx3NsTdPGOBcsxzUlgntvo3Cy2l0QmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ارتش اسرائیل از ترور حاج علی سمیر حاج حسن، یکی از مسئولان نیروهای رضوان، در حمله به انصار جنوب لبنان خبر داد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/141866" target="_blank">📅 18:51 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141865">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e77374a26.mp4?token=OgrTlYcHEzziZUp7EYcXc38nmpSRtmiyrZuKkyBV4IyTGYurKLcgQ-GikrEn6Xvy2plxRtqjR6wEa-5TV0gHqs64iO6A-vb6yubi1adirnxTWcCz4M3RXUnO3DQ4psla-hJI3Noh3rZ7dj9oAWHvU2mtOFk4Y_XmYam9cAautIWARlvUl-EcBM5ew74Nji87gbN7798JA3htmISKgurqueTaMs5NVindpCD3jT4hqzeMwZ1QLPW1QhSD7A6wj0xo2oyppSwvX0wSPAAmQN9JHbAggvPbWmpNsQzlQ63bIlRM5X_eg6FcaO768J_O5VOChIpTdNFX1vyjGbz2f_lumg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e77374a26.mp4?token=OgrTlYcHEzziZUp7EYcXc38nmpSRtmiyrZuKkyBV4IyTGYurKLcgQ-GikrEn6Xvy2plxRtqjR6wEa-5TV0gHqs64iO6A-vb6yubi1adirnxTWcCz4M3RXUnO3DQ4psla-hJI3Noh3rZ7dj9oAWHvU2mtOFk4Y_XmYam9cAautIWARlvUl-EcBM5ew74Nji87gbN7798JA3htmISKgurqueTaMs5NVindpCD3jT4hqzeMwZ1QLPW1QhSD7A6wj0xo2oyppSwvX0wSPAAmQN9JHbAggvPbWmpNsQzlQ63bIlRM5X_eg6FcaO768J_O5VOChIpTdNFX1vyjGbz2f_lumg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
گوشه‌ای از جشن استقلال پاکستانی ها که دیشب گرفتند!
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/alonews/141865" target="_blank">📅 18:42 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141864">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
رئیس‌جمهور ترکیه : ترکیه نمی‌تونه غزه رو تنها بذاره و هر کاری که لازم باشه برای حمایت از مردم غزه انجام می‌دیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/141864" target="_blank">📅 18:40 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141863">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v8AqIMPfdkVbDPvNYGlE8KyKrJXPooc0sXbwMcswUbOkjulDfukZlfnPYXI5cpOsqfr7sfF4hDrefisZGQcfrBR_-Tr2ro33Sz9ZxmfRANkeGtQ5iqqXs92l9GJVrEw3TBFHIPgpAjIUtKRGMrEJ_Wy2-k-8uHvWtoxcGLxPqrxdvga-GI4061KpozvmZW7UTiioft8JZ9Hd7XJeoyku2f8f-CyK8W9EeuvrI24y3jiwtIaJEyfCTaITpRVYqoflXtkjOp_lsBmmQNSAsGScjaxJfG7SdLcawrGtocO3hAePospF0Xd-dNnnqMe5GNfVGpFMtqlGMKkxkITJE9cN7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هیاتی از وزرای تاجیکستانی با عراقچی دیدار کردند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/alonews/141863" target="_blank">📅 18:40 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141862">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
رئیس جمهور ترکیه : در آینده نزدیک به سوریه سفر می‌کنم
🔴
سوریه رو تنها نمی‌ذاریم و برای حمایت از ثبات این کشور هر کاری از دستمون بربیاد انجام می‌دیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/141862" target="_blank">📅 18:28 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141861">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
رئیس جمهور ترکیه : در آینده نزدیک به سوریه سفر می‌کنم
🔴
سوریه رو تنها نمی‌ذاریم و برای حمایت از ثبات این کشور هر کاری از دستمون بربیاد انجام می‌دیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/alonews/141861" target="_blank">📅 18:27 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141860">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oespFjSlW5cxlGNlB5FE1_AX5dTnOi8OPMrN8Ei3I86KEAng861byBgAFdb8PJhtb1MDNYWga_q96hTnpVMDZDuNWSluS3a08mfySbSg_yDmSYlLR-SkNg2NK22MgTnv1wdJjrqaLLK2_4uODxf88Vxi3j7mocwpPVfvMgcbPKar7lFP2KT71FwbC89GyrhalCSf4FLByQNPflQztDiZIn_bScqB7NRU2GqaiIEcgN6kzzuEV2p6kNIXQ01x6QupR-cok6PbuGo0w2-D4f8hu3HCZoK7-qIXtprvmwA7P4NDM6tJGrkI_0EIDmAvxFply_ChC6g0ejUVrV_RCclbqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
واکنش احدیان، دستیار قالیباف، به تأیید تفاهم‌نامه از سوی شیخ نعیم قاسم؛ خطاب به تندروها: بیدار می‌شوید یا خودتان را به خواب زده‌اید؟
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/141860" target="_blank">📅 18:20 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141859">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">👈
وزیر انرژی ترکیه: شرکت های تکنولوژی سعودی قرار است در ترکیه نیروگاه های انرژی بادی و خورشیدی بسازند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/141859" target="_blank">📅 18:15 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141858">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mx2n-Z7iJ-MRp9FvI7Pmis3sSzp3CpAMJXiXpmDLdTjJ7cYPU1ATJHtu8bKxfl6MInRK0zqlnqvWjidZ2_vAmsQUGOeiD5gs48tW_5am8A51_0LjrzN-ScyyepOsGIKlZlpUC2IlcpeLK0NxsCrMbvyL3CXJPI7n4senp4zD4fW7B1qBKc6du6rwir9FlnBygLV6JNY9cFT2uA3YuKKMKCUdqXAb_6PnkfNxF_lNaPRlX1k3IHs0YvM07LMj6lwAJshzKQ3QVBvN0FMNpjysCIuMWC5izmp1mEhH5Ccnh4Y53GFIM8vuYwZPtx3rLiJX2e-yMHFa55mabEPasHk28A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وزیر انرژی ترکیه: شرکت های تکنولوژی سعودی قرار است در ترکیه نیروگاه های انرژی بادی و خورشیدی بسازند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/alonews/141858" target="_blank">📅 18:14 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141857">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
واشنگتن پست: مقامات می‌گویند ناامیدی از ترامپ در میان متحدان ایالات متحده در خلیج فارس رو به افزایش است
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/141857" target="_blank">📅 18:09 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141856">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HOmt3Yivoyi8nGwDzfrR95pLMCB4kg8KVYmMMFQN9z9nYNkxs18JbujHfRNjXj4syuGY6cCa1hBxprVdhfvYwbEK79vvbw7ksh0huCbe_QIMOWt7zEdNjzkSQfldCP40EhBcgxhVtkodw3I3gg6XIHoAf4HSXo1r9BVzJOak6x1JcBaEO5P0ZmS3-7kfEWmxt2qjKHszrH8nSaxIaFBbfqYRSGyzLQZM-kUZvPftBQG9Hos0DwOUy8C-cVJ60uXZdR59ugaruW1a1OFAXgoF9k4-lYf-P9zj6Snadueiy1X3kEl5Q-t4WsRR2yUXIMy062RDa2ZdZD2KWDheLmu0cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پست اینستاگرام نوید محمدزاده با لباسی با طرح پرچم فلسطین
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/141856" target="_blank">📅 18:05 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141855">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">💢
زود بیایید اینجا خبر خیلی مهم
👇
https://t.me/+nCexQYLuuONhYzg0
https://t.me/+nCexQYLuuONhYzg0</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/141855" target="_blank">📅 18:01 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141854">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
کارشناس صدا و سیما:
70درصد مردم تو تجمعات شبانه شرکت داشتن
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/141854" target="_blank">📅 17:48 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141853">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aOoXhswhJjZ2zL3-5Tis4927vQK6uuSboKzR60q2qTnaDYXURxyz62IyJxeLfk5uGdgQoPcO4z90L0qWUy1ft_5mTc0jyi4WT4URFtfKxcTSnBxK7-ruHqxRgPJ4oVi7gAsWzAIaDEyd3Mb4a5bxYA_VqGNdJBc9bg4_iMUbLS3WflhfUiQOqSALCiVgXdp2-NwcDrnxvyQIKlCzBcK5D6dleZ-z4VkbMwih_d0UtEc85YVDLHeZFI2FANJs1X1J3VYVyza9etdkxYeKzbYoynp9J6vVNIhmhl4ObAs_zLk205B4LgqgisJ1FY5ld0XcCRUstaJNvBsCzz49hH1ZwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
واشنگتن پست: هیچ توافق خوب و قابل‌قبولی با ایران نمی‌توان منعقد کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/141853" target="_blank">📅 17:44 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141852">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/358cc4c68c.mp4?token=hUMEQsK5lEYrxwLAxyDGOnxqUm1LoChN444HmL8RorDBmxRIAf-Ss1tdP7nPIR4hYuVMG8klrZ6FgP_2m3xHfRixuiFS8_2pscK9F2EnkOu3sZjYNvK6jJFiK01CdTWM8g2K3-26PcfgfdiASTDqf1fXfDAc7l8ZwLVUk76aPyxtaj1PUTmulPXaqIeXz5Dv97E5AsJE3doJrGxzvg7ti0JPmuxmDqFxvJ6JCUFue26YSSEvMUUn07eM16z4Ezro6U1D2rPzWtkng5mc1zRNZI0ixDnJR40HXQIFN0IXCTTexDWKnBj958AR1MMuDWMtgcUF01sGgH49r_Alm0rKKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/358cc4c68c.mp4?token=hUMEQsK5lEYrxwLAxyDGOnxqUm1LoChN444HmL8RorDBmxRIAf-Ss1tdP7nPIR4hYuVMG8klrZ6FgP_2m3xHfRixuiFS8_2pscK9F2EnkOu3sZjYNvK6jJFiK01CdTWM8g2K3-26PcfgfdiASTDqf1fXfDAc7l8ZwLVUk76aPyxtaj1PUTmulPXaqIeXz5Dv97E5AsJE3doJrGxzvg7ti0JPmuxmDqFxvJ6JCUFue26YSSEvMUUn07eM16z4Ezro6U1D2rPzWtkng5mc1zRNZI0ixDnJR40HXQIFN0IXCTTexDWKnBj958AR1MMuDWMtgcUF01sGgH49r_Alm0rKKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ویدئویی از حمله نیروهای انصارالله به نیروهای وابسته به عربستان تو بندر المخا
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/141852" target="_blank">📅 17:35 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141851">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4894cf0030.mp4?token=dgqKIIW-v_MnWuI3zwxCtYt-nB2BwJEEWJB_3yIuKJ8-ZRng13VyrleNyd2O7qsd4JSB9InMtNVSuk74-HhBs-8k0ra_01qonFhkgFsQYNrZ7_m7IYvUmAjhqVwZVLx3-srDnX5c6AxkEUomvmVmQIYCbifMp9n_7L_w62jfLl7WZzIF2DfwJCuBh61VUq1__rA54XFnzfkO7FSbl1cZovwT0tjx_rRAp9wT9ChhanluI2fbjMr0oDThVdww_db6tRgPR6ZsoYecQwrTDDnmhNXtntgAbxWew-p60wiYc1EOj1E6hUwUvig3h1F_sby3yTH5VAzPgAP97I0XKOu1jmEWB5iyUPQDhv2LD0Z2Gvtys0aElaxFMGCs_mDwUfrvkpkTEVINQxtoEQb4uCyq-v3mdSmN_cHtSwJkFf0yiQwyQ2d6j1jK4CKDtLc-r_ITLiQybYI0Qvy9mrXYTLZNO8-wjdTY16H0ONwsTjZRcfZan3_PaNgxm0qbu2fWK0czpkM2sTgHe2UpeykcPLtZ8ZGOesjc8QPfqEkTikxPEwF-1AMKLV7aaWyc90KUlBhGjyDRbeHuuW5p-Nwg1s96VpxtYqFtsXCICIVl1mEc12_l_8UEvaQdcpprTvn_7Ei4Z0h-JiHK_4-iTJTX6OX-UphwiOPzKSKV5bkz9kpBppI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4894cf0030.mp4?token=dgqKIIW-v_MnWuI3zwxCtYt-nB2BwJEEWJB_3yIuKJ8-ZRng13VyrleNyd2O7qsd4JSB9InMtNVSuk74-HhBs-8k0ra_01qonFhkgFsQYNrZ7_m7IYvUmAjhqVwZVLx3-srDnX5c6AxkEUomvmVmQIYCbifMp9n_7L_w62jfLl7WZzIF2DfwJCuBh61VUq1__rA54XFnzfkO7FSbl1cZovwT0tjx_rRAp9wT9ChhanluI2fbjMr0oDThVdww_db6tRgPR6ZsoYecQwrTDDnmhNXtntgAbxWew-p60wiYc1EOj1E6hUwUvig3h1F_sby3yTH5VAzPgAP97I0XKOu1jmEWB5iyUPQDhv2LD0Z2Gvtys0aElaxFMGCs_mDwUfrvkpkTEVINQxtoEQb4uCyq-v3mdSmN_cHtSwJkFf0yiQwyQ2d6j1jK4CKDtLc-r_ITLiQybYI0Qvy9mrXYTLZNO8-wjdTY16H0ONwsTjZRcfZan3_PaNgxm0qbu2fWK0czpkM2sTgHe2UpeykcPLtZ8ZGOesjc8QPfqEkTikxPEwF-1AMKLV7aaWyc90KUlBhGjyDRbeHuuW5p-Nwg1s96VpxtYqFtsXCICIVl1mEc12_l_8UEvaQdcpprTvn_7Ei4Z0h-JiHK_4-iTJTX6OX-UphwiOPzKSKV5bkz9kpBppI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
اسماعیل بقایی، سخنگوی وزارت امور خارجه ایران، اعلام کرد که ایران و عمان به توافقی در مورد طرح ترانزیت دریایی در تنگه هرمز رسیده‌اند. این توافق پس از پیشرفت‌های مثبت در مذاکرات صورت گرفته است، «با وجود موانع ایجاد شده توسط ایالات متحده».
🔴
بقایی افزود که این توافق حاصل تلاش‌های هماهنگ بین‌سازمانی به رهبری وزارت امور خارجه ایران، با مشارکت مقامات دفاعی، امنیتی و محیط زیستی کشور بوده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/alonews/141851" target="_blank">📅 17:16 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141850">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JRN9tVxncLf7x0mNQGNkbyZc_w10IhqtBi1FZ09bqmBs8k6EBpd6osjcJgF_sDg7eSiIYMKO5PfZQartIaXmNZWA0MhQGpTeQzeGJH6NHRpQhwY5brDkyOSWtV528DMttM2DfQNaX-SbeTrentItPMTHSsiscspzZcdlEIfQ-jJg2HezaZkwR0YZp3NP6F38A3fsTXrLlnAN57C6Izb6uPhR5fho9FnQfPYNbetKp4nZH-IbPmOl_paZjganTEF5C7OAv4wNzhJM39tWLnQWGboZcBD2L9SGYhC-7pNGhaQMb8fXWv3y3KqHHy9Pg7y-jE_T6oI5rJA7Lfu8kw3c_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اسرائیل دو حمله هوایی به لبنان انجام داد و ۹ نفر کُشته، و زخمی شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/141850" target="_blank">📅 17:01 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141849">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
ژنرال کین، رئیس ستاد ارتش آمریکا :رژیم ایران یک ساختار ایدئولوژیک است و اکنون خود را پیروز جنگ می‌داند؛ جز قدرت نظامی، هیچ ترکیب جدیدی از تحریم و فشار اقتصادی، تنگه هرمز را به وضعیت عادی برنمی‌گرداند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/141849" target="_blank">📅 16:44 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141848">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/skn4QOWBX87GEws-Sp8N-A2jvglTPGheaZTTqn53ZzN461o1v58mTyQyCqK2dU42v9XX341AiIJJE2vzXN82oRTjQ8zJaUYN98ResQHCu3121zxmxlfhmQWaVTiPvQo7LaGeEI2BN7xTEGS3ZpZNNCwv1FQh3Lcc6dPTl2qVQNA9qJa7aOe0lvdfVDMlOzD96AzONpta9IJfCFO0p-7GCfi5saKOpGEvvxcdcJ2YFAYMVDgdtZfWy6tzSw-wquvMp-e1WqBkrjXsz5w6-1TS-qWPB-BsYOtfg-hYLvF1buh9KrOHztCy-Crel0aFECSp3rM-aTNOMpkhRVnXsnzNWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
جزئیات توافق میلیاردی رونالدو و جورجینا برای روز جدایی
🔴
در صورت جدایی، جورجینا ماهانه ۱۰۰ هزار یورو تا پایان عمر دریافت می‌کند و مالکیت خانه‌شان در مادرید، به ارزش تقریبی ۶ میلیون یورو نیز به او واگذار خواهد شد
🔴
این توافق همچنین از سرمایه‌ گذاری‌های شخصی رونالدو محافظت می‌کند و در عین حال، نقش جورجینا در تربیت فرزندان و مدیریت خانواده را به رسمیت می‌شناسد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/141848" target="_blank">📅 16:37 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141847">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cxr_4zUCpDPz5S32fbZOjCYZABKnVALJ7Xzt_i0TzANO-46iS9gdLaB1Zub8ymP2yyFTTfuKYzMxeyA8Pk5ln8TRdCnSFzGrEQH9yN3wrK1T7_XkhFQO9mBy1-Bzu80lmRzo7Qt_uQO8ZlkroN8i7c45BuAHWf-DN9NCMpjaeQzA56ukdmBLI4X0JZ9BMsVHLrHG5KpI18AvYsdwIdVNd1w6nFl5VNLz8xcAUkUilLtbHWTqo7mwx1i-SIHJoeyPzOdRq1qNRmEZcPz9zM6oYw8BNM_eZ8SnRidZqGQ24eW2Y_6lo6At-ttGFTt8Ka0dDvFHH0oefS3SDS6vYulQPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
👈
عراقچی: با عمان بر سر نقشه مسیرهای عبور از تنگه هرمز توافق داریم
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/alonews/141847" target="_blank">📅 16:29 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141846">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/82b35919d9.mp4?token=qjDdGNtZSwK-jvUyoPCmd6SC-RmnRylERUxrXktcFDsLEVLCdz_lJt2pC5rcFhxU9NlUgl5cpqlgPC1ViWcVTgGtfqXTFqkEYjPs8msoz-Uj5sA2ywseZGGgMR-S0VcTVdi81lW5v68DmlzPEgYG2Lrv78hVI33fkdhHYJButLHOLkNqlEVMKu1StK6efjKgHaGrG7ciS0702fwCXbkIPSu37aQFmbDZzOK54SgVAF8LPhhBfWANlp2tSGeg8BpAolVZjiTaCcfKpHyAZIATsA2V0zF1lsGtOg1QmSGbGJKA7NoSjBICOljErpHYZ14YS7Anl4xinzoLVViOg2wEdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/82b35919d9.mp4?token=qjDdGNtZSwK-jvUyoPCmd6SC-RmnRylERUxrXktcFDsLEVLCdz_lJt2pC5rcFhxU9NlUgl5cpqlgPC1ViWcVTgGtfqXTFqkEYjPs8msoz-Uj5sA2ywseZGGgMR-S0VcTVdi81lW5v68DmlzPEgYG2Lrv78hVI33fkdhHYJButLHOLkNqlEVMKu1StK6efjKgHaGrG7ciS0702fwCXbkIPSu37aQFmbDZzOK54SgVAF8LPhhBfWANlp2tSGeg8BpAolVZjiTaCcfKpHyAZIATsA2V0zF1lsGtOg1QmSGbGJKA7NoSjBICOljErpHYZ14YS7Anl4xinzoLVViOg2wEdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
طرف داره وانمود میکنه که داره به پیرزنه کمک میکنه؛ همون لحظه کل طلاهاشو از دستش در میاره و‌ فرار میکنه.
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/141846" target="_blank">📅 16:18 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141845">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
آتش‌نشانی مهاباد: انفجار بنزین ذخیره شده در یک واحد مسکونی، ۸ نفر را روانه بیمارستان کرد
🔴
۳ تن از نیرو‌های آتش‌نشانی، ۱ نفر از افراد حاضر در منزل و ۴ نفر از همسایگان، دچار سوختگی سطحی شدند
✅
@AloNews</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/alonews/141845" target="_blank">📅 16:02 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141844">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/daf8b9dc48.mp4?token=dF0J9MJrXePB06jCI6iN3RppgYwbD274GIqn-_hRM-u_SNvLc5Y12oGsA1NM0usHZN7xQV4qSgSfLjCui9VEPX0QhZV7lY-ZSm0rBVqkdoNOqadzUDY9c3lhJmyMmW-Quihx4qH34g3a4Zxq8AbNc9QVYdF-FfDU2WWq0mAY7LSxSvEchKD6IpvihZBdKsidBUIVjkqKXbIioW7_KeOm_2HcK-F-FIWz0--TqPXQHfJwaUtJYn09dWER-gbGcB7T1p3hFYQGzDyooY69FdUtHdf6Il7uW8hc7p9uoTCJMuLIRTcB4C-I5PsdNGnhnkAKs15bl-oIzbe9AFNZLJfLFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/daf8b9dc48.mp4?token=dF0J9MJrXePB06jCI6iN3RppgYwbD274GIqn-_hRM-u_SNvLc5Y12oGsA1NM0usHZN7xQV4qSgSfLjCui9VEPX0QhZV7lY-ZSm0rBVqkdoNOqadzUDY9c3lhJmyMmW-Quihx4qH34g3a4Zxq8AbNc9QVYdF-FfDU2WWq0mAY7LSxSvEchKD6IpvihZBdKsidBUIVjkqKXbIioW7_KeOm_2HcK-F-FIWz0--TqPXQHfJwaUtJYn09dWER-gbGcB7T1p3hFYQGzDyooY69FdUtHdf6Il7uW8hc7p9uoTCJMuLIRTcB4C-I5PsdNGnhnkAKs15bl-oIzbe9AFNZLJfLFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
لهستان بزرگ‌ترین رژه نظامی تاریخ خود را برگزار کرد؛ دونالد توسک هشدار داد: «فقط قدرتمندان از جنگ دور می‌مانند.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/141844" target="_blank">📅 15:53 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141843">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">👈
میخائیل اولیانوف، نماینده دائم روسیه در سازمان‌های بین‌المللی در وین، اتریش در ایکس نوشت: «دونالد ترامپ رئیس جمهور آمریکا تهدید کرد که تنگه هرمز را قلمروی ایالات متحده اعلام می‌کند. این یک شوخی بیش نیست.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/141843" target="_blank">📅 15:47 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141842">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">👈
رویترز: امارات متحده عربی اعلام کرد که ایران به یک کشتی شرکت ملی نفت ابوظبی (ADNOC) حمله کرد در حالی که این کشتی در تنگه هرمز در حال عبور بود؛ این سومین حادثه از این دست در کمتر از یک هفته است که یک کشتی ADNOC درگیر آن شده است.
🔴
هیچ آسیبدیدهای گزارش نشده و شرکت ADNOC اعلام کرد که وضعیت تحت کنترل است. امارات متحده عربی ایران را متهم به انجام حملات بدون دلیل کرد و خواستار بازگشایی کامل تنگه هرمز شد. ایران تاکنون در مورد این ادعا اظهارنظری نکرده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/141842" target="_blank">📅 15:43 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141841">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">👈
زاکانی: مترو تهران تا پایان جنگ رایگان است
🔴
‏مترو تهران در حال حاضر رایگان است و شهردار تهران گفت که تا پایان جنگ هم مترو رایگان خواهد بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/alonews/141841" target="_blank">📅 15:38 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141840">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ic3JCD62OfefLOvHYkl5xV7rRvWItNDJ_QQ8O_Zi76Br25DMT9I8Cw9wymcn8iOlCbtsR9PAPmhyo6wswsZ4L1icfcp2BU-dfLr2339jYY67PGm_ZasXsaQV1RMBu59kaxaIauiGpau8KnBk24uL1AuNdCZDU7UOper21GQyHew8n5C2npJ4w5BHe2BgUy5iiXpZWS37IQwXVXz0nRdS5MULm6dwM0x6QzsS06iX1AdFdLf4_8WTyq-qZVXd2H1nYV8T-Dxje4A5R_EWVarBxuZJAhJOo1fXlTlid5Ecr8SjEKIYIgNG5JuwjCiAihxPXMaVcRf1sO7aDwExM_4fgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
طی گزارشی در رسانه ایتالیایی، قطر ده ها میلیون دلار به اعضای اخوان المسلمین در ایتالیا کمک کرده تا مسجد بسازند و به گسترش تفکر اسلامگرایی و حکومت اسلامی در ایتالیا کمک کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/141840" target="_blank">📅 15:34 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141839">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/41653dd3a0.mp4?token=a9PI1wRr4iMuuFwCEZ7BAGqP27Iv4WDjkBjwtTBhNsU0x94gZYnAYTCPCDHCWJO08ORdYmv10IMHihsLN-tbUoYwvm6W6e8b-B8UJzNUKh3fSaENnS5aAXwNDm1Gy8awRq4xLf8SletlXcjemSFStHr7L_MFx0SXrq37C08Ja2GZrMFZUR_--UdWrzcPPtwiZtb7hITJjJu01kn2fyibAgILyYLXzBWpo7ELPXjeIvyFDCLR743_g7jBxZroR8XMa0NIL1DKJdC1BPct0oRkR4qOyaWpqy_so1NYrUXNh24Lbswf5qS8yIZEmoYuuVt9vXcFvQ3hat7ybRYa-lMPYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/41653dd3a0.mp4?token=a9PI1wRr4iMuuFwCEZ7BAGqP27Iv4WDjkBjwtTBhNsU0x94gZYnAYTCPCDHCWJO08ORdYmv10IMHihsLN-tbUoYwvm6W6e8b-B8UJzNUKh3fSaENnS5aAXwNDm1Gy8awRq4xLf8SletlXcjemSFStHr7L_MFx0SXrq37C08Ja2GZrMFZUR_--UdWrzcPPtwiZtb7hITJjJu01kn2fyibAgILyYLXzBWpo7ELPXjeIvyFDCLR743_g7jBxZroR8XMa0NIL1DKJdC1BPct0oRkR4qOyaWpqy_so1NYrUXNh24Lbswf5qS8yIZEmoYuuVt9vXcFvQ3hat7ybRYa-lMPYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
آمار اولیه کشته شدگان حمله هوایی اسرائیل به دیرالزهرانی دو کشته و ۹ زخمی است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/141839" target="_blank">📅 15:27 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141836">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MuYYJ86roG3YHDT5KTwBC7Zi7GSwj1PTz_zqN94Mru3UnesoKNRWubOjoBUsVSQIpwUcjX6J8-YQk1jZjsotniakXSQJHi2u86lWk1qYtMSpv_q3fMMuBIvax5fsEf0rmose18TV6VyzsR06zSTxSf42XzfE9i579CkiP_5R7fnU1ON8Nn4KXmxvU7gSDDe5u8BRe8FAr6u2mHK7FCh8KxJzP4kdzdMAPcKbIize6xVcb1xannOtI51Wi3ZTQLK7UfNX5Ydg2MYlSEHyjYEUfFBHXcAsuCDz5oXVgNAbq202qzMKQF-vEudpqOUCznUrHB3desmz9PdrgZhom0mmbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff856ea1ed.mp4?token=KvIvE7mCv0QsjCoiiQPnBw7RV0JZusj3GMExeVqA0tWf6VbfbAk7TxcOI5wQ7eiKJ1tytMZyBnCAkiAFUoHpzy4G16yjME0xjsb3H97Dfdx50g56BZx5Y2FLl6Y-q64LDD-l3N-1x0WSjqQQbE2KZO5qdPmH0qSIG7-_oDKYXXwWOp9YOom7j85JcuSchagVuUwaobz0xaVBSsIRc9jAr9TrpwRsztwoOxVqLJt-BWp7CaHgbPD_X7OX7OV_92WGxpYp1eVSKquGSU4hShXoApeGtdBVkytMCNJm7Kxucgoe4Ia4B4cwk1iWM1ooS_RADu27DPC9Syx8zHWOAxACiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff856ea1ed.mp4?token=KvIvE7mCv0QsjCoiiQPnBw7RV0JZusj3GMExeVqA0tWf6VbfbAk7TxcOI5wQ7eiKJ1tytMZyBnCAkiAFUoHpzy4G16yjME0xjsb3H97Dfdx50g56BZx5Y2FLl6Y-q64LDD-l3N-1x0WSjqQQbE2KZO5qdPmH0qSIG7-_oDKYXXwWOp9YOom7j85JcuSchagVuUwaobz0xaVBSsIRc9jAr9TrpwRsztwoOxVqLJt-BWp7CaHgbPD_X7OX7OV_92WGxpYp1eVSKquGSU4hShXoApeGtdBVkytMCNJm7Kxucgoe4Ia4B4cwk1iWM1ooS_RADu27DPC9Syx8zHWOAxACiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
لحظاتی پیش یک حمله هوایی اسرائیل دیرالزهرانی را در جنوب لبنان هدف قرار داد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/141836" target="_blank">📅 15:27 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141835">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
کانال ۱۲ اسرائیل: طبق اکثریت قریب به اتفاق نظرسنجی‌های فعلی، نتانیاهو در انتخابات پیروز نخواهد شد و رئیس‌جمهور ترامپ و مشاورانش این را می‌دانند
✅
@AloNews</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/141835" target="_blank">📅 15:14 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141834">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
معاون دریایی بنادر هرمزگان: تاکنون بخش عمده‌ای از آلودگی نفتی سواحل قشم مهار شد
🔴
عملیات جمع‌آوری پس‌مانده‌های نفتی تا رفع کامل آثار آلودگی، ادامه خواهد داشت
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/141834" target="_blank">📅 15:09 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141833">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/358cc4c68c.mp4?token=WmU6oiwOYuB9DoaaHdbJy65qcXkqPKdKiFZrRWU5YcakkuhPjRqLg8ix80WHrfOtvzON51YGU24ecM-R21spZXElhplAYE4Mhfo5MPzOOyE3CFwswgMLtwAT9ANsAGDvd7M9z2PhVk4OFShyex0E6rijsS_733E35GeGU2v3DGj719sPB2PDzuryjptGC8w4TS26CBrMg6HUN-2VL0orPWy5fMsIgnCTJOwNIcUxr7EoBIuHEkkuukpNQvZrM45uRa4ZFytRTuNCBMBf9kB_OI5MflbgX43-3AObjrmVJ0tQbfPap6kXaxq-_i8ctaH7_dRaHts185iAXRuxCuD2dA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/358cc4c68c.mp4?token=WmU6oiwOYuB9DoaaHdbJy65qcXkqPKdKiFZrRWU5YcakkuhPjRqLg8ix80WHrfOtvzON51YGU24ecM-R21spZXElhplAYE4Mhfo5MPzOOyE3CFwswgMLtwAT9ANsAGDvd7M9z2PhVk4OFShyex0E6rijsS_733E35GeGU2v3DGj719sPB2PDzuryjptGC8w4TS26CBrMg6HUN-2VL0orPWy5fMsIgnCTJOwNIcUxr7EoBIuHEkkuukpNQvZrM45uRa4ZFytRTuNCBMBf9kB_OI5MflbgX43-3AObjrmVJ0tQbfPap6kXaxq-_i8ctaH7_dRaHts185iAXRuxCuD2dA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ویدئویی از حمله نیروهای انصارالله به نیروهای وابسته به عربستان تو بندر المخا
✅
@AloNews</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/141833" target="_blank">📅 15:05 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141832">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VpwpbipO45pTb1ob2HLh2_SXjKGAp8uQ2Pa7PTF9awepoLQfLQtOUg1_-ND9PMZfgRV0W3ajvEbNJBiNg2vYansiqRlEJpXRiZpTi2LnbyqEuWNN9vpDPyJmv0eRILabLl3ReC2GC7R0frt8wbv15Jg8Hnm5RPoDBuq_hEmemvWfzaikNew6qOk7_UaL1Azt26e6-AZWMe9B2zcSEdzklaIgcSqSEajz2voUlFnN56JXY2C6D29MxkAnqKccEuggcULBvPEaZegwQXYd-ImRll1YO-5vmjFSWk7M1Y9MJt6Nk-HGSP8pQOYyffL84OPlo4C9qwAAmw3A7XZCSaGL4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سردار باقرزاده: 3 خلبان ایرانی پس از سقوط جنگنده‌های سوخو-۲۴ در جریان حملات اسفندماه، زنده توسط نیروهای قطری اسیر شده‌اند!
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/141832" target="_blank">📅 15:01 · 24 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
