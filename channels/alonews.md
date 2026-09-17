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
<img src="https://cdn4.telesco.pe/file/CuxB3qD4xcgHGfh9il3yleb8r4qprPRdstAxFEKMFU6nUIdMaduQ_P0BOXdBsSUbhVjoxD7z28pMcZdibA4r8DkDVDqD_rLxBhk414aooVXjYx5n9ZyPtZnwI8pOwfn1qVmii215wahAXn3W23EExHrEFsxycs4E1fOyllr8u0K9zi-FhTULhZYXm2i9Z5ifN0gFVuPxPUeol_9gJYj9223brwghBx3Pis2a7nkOagIPAiNPlt4bTvB1S-4vG91zQnnSMucfiv6G8072OO7TrLQh7y_nop16VRj-ZzzYAx5hhexaU_5ICgclpHYKvJY1fT1FeVbENIxWd6dojW7GLw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 946K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directمالک کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-26 18:02:50</div>
<hr>

<div class="tg-post" id="msg-147897">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M3WTCAa8sNm1z8mZajqzvOm8702yU2uNOwBnvlsFq9aNTdUfFZFLOVwdSEMxfmSuDLQwsVB6zW_CBTUYbRfvBzJPMS98VFGooCBQ-lAJ2cV8p5xC2td3_k6gJLjb7LI37oYXBZmaEgBNjAu7Z2pLNCkHYeb5GKQYdUb5HKPHGjTVyqarC353vupB9ZdMgG5g3vrbQl_W5fepAvYHZQ-KISZO-J84A8BDaRFKD3FUSlGnGffQP5yqQkYTwVJSWBsWlVP-DyN1rOitM0aJq4ZaJNIecPMxMwqK-y2JqsfD7dfHK89OGn3JlD4Jm7_cwKWufpKCjwjcgoivJWikpC7n6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ولایتمدار: روحانی و برجام ما را ذلیل کردند؛ خدا ذلیلشان کند! حالا با اقتدار مذاکره می‌کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 1.24K · <a href="https://t.me/alonews/147897" target="_blank">📅 18:01 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147896">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p2SsEuk_Ba293ashT2RqIa6Ola2TvX5TXi_u8iFZWlOuC_aDdxAKEJlswB_OwruSGFh89N-VHdAcmQ2_cYKhlKjfFEsLIAeFRKmwISBuKDiE15ghWrBj3CVrxmjnr-aKlWcCWpF0YC9_Y-fQRma3BPJabVlgDoJ9zV3KKDSk7W7secGXsLEY4K7q_ZOioM25FlgAjQlDhoPUtRNco0VZZgyNg-PRgZpGXOc1OTKN4pstQ4BPRHDVr6Vjc8JAIRaiDf4fUxjAd2SIXd_fEEcCKaMqTtx1j4WrChoH8PVOwDySdJso69egtbAUbJyXDqtSQmECadpTjJRtOvPKQRT6Mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
جذاب ترین رهبران جهان با حضور رئیس‌جمهور پزشکیان تو رتبه ۱۱ام
✅
@AloNews</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/alonews/147896" target="_blank">📅 17:27 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147895">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wmz0m1MIkDsnVMT83ES5kHE7bynbXUHkUzBa2jsv-F8YPXH9RXgkh9IjqejATM7ule1zQSw0FKZsIL7dhhg4S7k0f48CYLvo1V395D8sYrbSghHW2GuAnoJt9o8saVTMVC8x-mR5_4trLkE-4WcmB1LPpFe255cCQChom5A-GmDrYMHs9Aie-ePYYDEV781fM9j1lP72BDwrm-k_OLmQ10btp_RLLXMx_6-ryxi8gPZLvaAfIHCjePcnj1xn0FxGovIJP202uLQ3aytqzCX1KkVMFm8izLsX31WefXV1ewYC-iVpT9Dalz80dYKUfsHZvefGi0_gpXRjddQT5-ekjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قیمت نفت برنت به ۱۰۲ دلار کاهش یافت
✅
@AloNews</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/alonews/147895" target="_blank">📅 17:10 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147894">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">👈
گویا کارت‌های سوخت جایگاه‌ها به‌ تدریج جمع‌آوری خواهند شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/alonews/147894" target="_blank">📅 17:04 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147893">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">👈
المیادین به نقل از یک منبع آگاه: ریاض از عمان درخواست کرده است که از انصارالله بخواهد یک آتش‌بس دو هفته‌ای برقرار کنند که طی آن، گفتگو برای بررسی راه‌حل ها صورت گیرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/alonews/147893" target="_blank">📅 16:44 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147892">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👈
نتانیاهو:
تمایل ایران و نیروهای نیابتی‌اش برای نابودی دولت اسرائیل از بین نرفته است، تضعیف شده، نظام ایران را سرنگون خواهیم کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/alonews/147892" target="_blank">📅 16:26 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147891">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👈
سپاه: پهپاد زدیم
🕺
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/alonews/147891" target="_blank">📅 16:21 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147890">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/16117ba246.mp4?token=J4mGKn3HV35c2g_ADg2Exxja3iU8Ztr0GcbNWCnvy-usxUCpWWIrgSMOE2gK0ZOCLI1YEUC8VsASgqGAuxZb45vM7R5P_VT37F2fG0QNpertOWnGocww-oCOPi_pUHfU4LlZoy4kFe0DWtiBwkkuvTpDIRDhMngaQ3Rw6-2JmdkjqD2tSiqFdZly_CLPi3tIrXhFsMM-rdgXWmAujxPdWeE5cvLz1FEeSMpIoMJ_vLlm0GOlst9wTiC_8Cp6iC7iKleglAaNbIqcJkny0EQWNllmT7G_6fA_A8YH7Q_OFf9d_nCwJbVJ5UOJej8zPdPLqpSyTmlFaS5tHGJwOmhO7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/16117ba246.mp4?token=J4mGKn3HV35c2g_ADg2Exxja3iU8Ztr0GcbNWCnvy-usxUCpWWIrgSMOE2gK0ZOCLI1YEUC8VsASgqGAuxZb45vM7R5P_VT37F2fG0QNpertOWnGocww-oCOPi_pUHfU4LlZoy4kFe0DWtiBwkkuvTpDIRDhMngaQ3Rw6-2JmdkjqD2tSiqFdZly_CLPi3tIrXhFsMM-rdgXWmAujxPdWeE5cvLz1FEeSMpIoMJ_vLlm0GOlst9wTiC_8Cp6iC7iKleglAaNbIqcJkny0EQWNllmT7G_6fA_A8YH7Q_OFf9d_nCwJbVJ5UOJej8zPdPLqpSyTmlFaS5tHGJwOmhO7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نخست‌وزیر کانادا: هیچ‌کس برای ما تعیین تکلیف نمی‌کند
🔴
مارک کارنی، نخست‌وزیر کانادا، با تأکید بر استقلال این کشور گفت: کانادایی‌ها متحد هستند؛ هیچ‌کس قرار نیست به ما بگوید به چه زبانی صحبت کنیم.
🔴
هیچ‌کس نمی‌تواند فرهنگ ما را تعیین کند یا به ما دیکته کند که در عرصه بین‌المللی با چه کشورهایی توافق و همکاری داشته باشیم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/alonews/147890" target="_blank">📅 16:19 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147889">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/obUYkxMwW3HN4xpT3Z83MJ4qSKrY4BXsKRMbJkpNtxpgghZTt2yIqGYI4BjHVaZt_tz5b_kXpj2nUn613-Rc81JhDrcNqkLdluo0fhjJ_7eLOi2rZFt303UNXCco4RPETy1EelxonlkNXBaBFPPcaPCezpUh6R2YSZCzDlkOB7bidTxemSHOvR-PzWIYEpcOp888gUsPzYFLJZvphkllUR3ImaYhlO4wp2qPh3kSNHLXOJUbjet64_pOqwgvjQ4wuPqeYSCyvdFQG5aoP2BsBUoWBupX7Nv9_twr7Yvl3EpUf1u1ZFYcDLl97pFR-9F5Uc_FU1Fvovqr3V6FIfUDzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پس از به صدا درآمدن آژیر خطر و شلیک موشک‌های دفاعی، آتش‌سوزی بزرگی در یک شهرک نزدیک به مرز لبنان رخ داد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/alonews/147889" target="_blank">📅 16:12 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147888">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
رویترز: شرکت پهپادسازی آمریکایی «پاوراس» خبر داده یادداشت‌ تفاهمی با ارتش پاکستان امضا کرده که شامل یک سفارش اولیه در حوزه پهپاد می‌شود
🔴
این شرکت قرار است با یک شرکت سهامی عام ادغام شود که تحت حمایت دو تن از پسران ترامپ قرار دارد
🔴
مدیرعامل «پاوراس» می‌گوید بخش دفاعی خصوصی پاکستان «در حال ظهور، اما هنوز نابالغ» است و این باعث می‌شود شرکت‌های آمریکایی سریع‌تر حرکت کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/alonews/147888" target="_blank">📅 16:06 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147887">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q1F2Ilns_3UYOgUsWsopCsCFELR3bD4gvgpE-SZHf0AxZ0_Ybs08E6M2yeFwTxFBkccZVDnMEqzbC2d6PGzf-ztlQ0WvVcidTxU3v01CUSTSFTsGq8IAAd8PlvpjlyqUwoHY6kQ7NbNKvKwYE3fN4zsUSzREHSALW56-KuFaneDbn_giz7xDIn-zPI6Y9qe5CSNxyHP4TuH1tJVFBFF7kBiv43XwwLYmshsj9Z14eKvlehUe-DJ-u3GBkYooUPw6aJ295QM9roteb_xQcEFjrYh1smZtw1ci78o_9lwa-Cb-AzhsLJ8xU6Hd3DouzPbVOwPtrbU2YvBexhD_HqkCog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قیمت آیفون ۱۸ پرو تو کشورهای مختلف چقدر خواهد بود؟
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/alonews/147887" target="_blank">📅 16:05 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147886">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I-BNqljuCJFz43024-wUGwbEgPjExxX-0JH86p9NMxffN41Kfaa_yfUZ5WSetK_ejPVXe2XKOOyESOQWJpqzEEdr5g-Sd7aSinfjIGUpAYI-jENihQuk_VUfXgQw1HNhIDkb5XGc4YO1hp9R208GoAfE0yl2jf64sXVykG8FVIKjYpunYcZGfu8p8WpwbTaBA0uL2NloMbw_d72XyBXsdCCCeBk5elLObk10l0Qp_P-uCFS74zcZODYY1dbWZawWOgDZCb2zWf6wyTu6zVGVGrJPXwEkSJG9dUgMUVdSXJTFNP-bjW6QdL9HVsZnufdX1TYesYt-BXO8zOY1zAH2Eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ساعتی قبل جسد پنج زن و مرد که گفته می‌شود قربانی یک قتل عام خانوادگی شده بودند، در بلوار سیمون بولیوار تهران کشف شد.
🔴
اجساد این افراد در گور دسته جمعی درون یک چاه عمیق دفن شده بود
🔴
عامل این جنایت دستگیر شده و پرونده برای رسیدگی قضایی در اختیار مراجع مربوط…</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/alonews/147886" target="_blank">📅 15:59 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147885">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">این تاریخ بیت کوین میاد رو 200هزار دلار
از این تاریخ پرواز میکنه تا 200هزارتا
👇
https://t.me/+4jOgodAq96dmYzY0
https://t.me/+4jOgodAq96dmYzY0</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/alonews/147885" target="_blank">📅 15:56 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147884">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m1qthQ0axTS4-eD0e5ul_LFseBB83lk6hP_bilz8xlnPHsyE1F1T3afLG9F8kuKZozZDEQ98ttSsFZjFl9I5NPT4rmmb0044fRDPxNU5ZnM6v5WGMigWyRVA79HKJxA7YcQaG_i-AFYKOKKYAjUROHdXXZG4Q5R9kBymV-VEQCNxTOWf0RM8R-a5u-G2jRyt0wA2ffkqEyLgxCPlwy4wFEBHYsHLC4FLGNS-lAeCfRB4SOpzx4yMqLHpczYP3r_Rpf8XK_7lQx1jX1VmwWWLHUlQdcZM77PEKjb5tIQCy6QtS4B-ywet79eydLWYVO2Rbs-OGc0zHanc1dDs51bjaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آخرین قیمت نفت: 103 دلار
🔴
امروز نفت برنت 2 درصد کاهش قیمت داشته و به 103 دلار رسیده است.
🔴
قیمت نفت آمریکا هم به 100 دلار کاهش یافته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/alonews/147884" target="_blank">📅 15:49 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147883">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">👈
سپاه: رهگیری و انهدام پنجاه و سومین پهپاد MQ-۹ ارتش امریکا در قشم
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/alonews/147883" target="_blank">📅 15:48 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147882">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">👈
وزیر دفاع اسرائیل: جنگ با ایران و سایر گروه های شبه نظامی ادامه دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/alonews/147882" target="_blank">📅 15:37 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147881">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/96265f0275.mp4?token=Zzs2UYwFITkG0dy8FxkbA_1f83029ES9XzNtmB6_VJY4c_-sl4DEX1jYF8XrXLruQwH135dl20NRdFn4r0kwlQCCmcyDXZU6vgmWiETz4yX2bFhkC1HKIklQl9d81jHDPfnij-8pKMwcmboKKRQYf3n1AzsDadhrG3IqOgQxdg-lIn6ZMLFVqu4ovoAuVoywoEhQ197K_tinkIpAtQ5BvOTeOMuxYhkyvXocmDh87THf_dRXeza6R-AAPu_SC71ZPk6d6eXIIdhP__khCnEhvMf_MgJymDGErtu5cBfQkE7NqPLWeAlg0KGtcpCouWEyTQXSaxdwm60LMF_nhqxlew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/96265f0275.mp4?token=Zzs2UYwFITkG0dy8FxkbA_1f83029ES9XzNtmB6_VJY4c_-sl4DEX1jYF8XrXLruQwH135dl20NRdFn4r0kwlQCCmcyDXZU6vgmWiETz4yX2bFhkC1HKIklQl9d81jHDPfnij-8pKMwcmboKKRQYf3n1AzsDadhrG3IqOgQxdg-lIn6ZMLFVqu4ovoAuVoywoEhQ197K_tinkIpAtQ5BvOTeOMuxYhkyvXocmDh87THf_dRXeza6R-AAPu_SC71ZPk6d6eXIIdhP__khCnEhvMf_MgJymDGErtu5cBfQkE7NqPLWeAlg0KGtcpCouWEyTQXSaxdwm60LMF_nhqxlew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نتانیاهو: تمایل ایران و نیروهای نیابتی‌اش برای نابودی دولت اسرائیل از بین نرفته است؛ فقط تضعیف شده است
🔴
توانایی آن‌ها برای عملی کردن این هدف، اساساً به‌شدت آسیب دیده است. ما وظیفه خود را انجام داده‌ایم، اما هنوز کارهای بیشتری برای تکمیل باقی مانده و آن‌ها را تکمیل خواهیم کرد.
🔴
ما حماس را از بین خواهیم برد. همچنین ابتدا رژیم ایران را شکست خواهیم داد. آن را سرنگون خواهیم کرد؛ سقوط خواهد کرد. با حزب‌الله نیز مقابله خواهیم کرد و آن هم سقوط خواهد کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/alonews/147881" target="_blank">📅 15:33 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147879">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DJPC9qbspNNQ4vEQNnpIsskgnsslft26J7ZH2d8mc2pvGUMLUTh4ofClTNNYmHOlBJaYXq-FXCeNt97ev2WJwJphOleDn-npOCYqLis0aeBMt5XVyuT-n640xZ32Ct7b_uL9RegzVTwpC9-RLFf1R8GCnaPTausKVx7gqhxqC3lMhI16XxhHp2Nb9YVgwd59I514hLtFJWg6xFUaKy-JP15A1E7DQPzhffjRjQEX937Mu_FXWMOKUzk1-SAu-zql4ZOfzWsuREykDJCgPQs03wATVJanjevZ20xK58d83vjd7Xo0KHYcS5g6OUGKS9Vv9vyGMfJxd3aIwpc0YkxWCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/auTJzssrBaw47hvV93YG2DOTcFf1RsXyUNX_WskEfNDeb_dZtkg89MjB3adYxsShzY60iLbiZERVOj-HzAvjX1c7-mpF9_-d1D2rCgE__wqwB4TpNRyOEuPrHVCx8JFF6D9pjvw_1FoRO_8v8GZVSawnBUDkNmfzVDSi57dVT6-WOzQFNIyo3szDUIvNcIFq7T3M16_bnRFLTli8PA32zgHcrFCMI7-2sNYzWxy7CVNYD-RGOJfhmGRJveAhXPep0PWC70O_eJ9Q6f-47xQyrbIsI4jUS_iq2n1dsJXBLjTGSkzC08EOy-Ox-_MToMrh4rP6uV6q-YEVDu8HQjPxiQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
فعال شدن پدافند در شمال کرانه باختری
✅
@AloNews</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/alonews/147879" target="_blank">📅 15:32 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147878">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VeTbUBES8pUamB1RA_Tncd_VkzZFTQp8_5dK1qOM_mIUWZTZoinMZM7FWFEE3GZrc8hHmASX50irPrzLkniA9eKofMqbLwM-IGBEWDo7EK1AeQyaUEDRyJcI3gfaoCUuf_0iEtPiMxA4WrBEJlC5tRPfB3ubIG1HAeXkA3bZRvxx4Tvm4UQYt668zY8r-I36DRNzMpboTeLThltm1awuckPzrImlGhw7qFgvzvjEqOp6THUb-13obac65F14wYuHjc3H-eDcM7VQQxFKdPDVGmjJBYiiLOaCgnueaY87U7QtdcIKy02deVisarO4O7Ch4iP-pH-aGYZJsJ5aVMaVSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سعید آجورلو، عضو کمیته رسانه‌ای مذاکرات: آمریکا برای کاهش فشار از مذاکره مجدد می‌گوید. سخن ایران مشخص است؛ به هفت شرط مورد نظر تهران عمل کنند تا تفاهم عمان- ایران درباره تنگه اجرایی شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/alonews/147878" target="_blank">📅 15:26 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147877">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NknBXN01aa45IWqlQ6Gd_XHDhy46FsQOMygA9KWxzRXPU4BhA8Ozv5bC3lZvc8AtHbfz3VxLxO6tQcrszziPAifycrJygd2n6Zoh-DGIweHynoysswuZyqi6Ri-a0QnPp-K5YULdGfO8f2zx0Xyn-AXpYPACNPfNcu3C3X-Gt1zyV1nhxKDzAZQzoiT8eBcgauNfrU3SbAe-46M6XDItC4iD_TogxMCR_ibx-M6y7O-n7YBRKzBcazZf11JOg0sl575kGZGfLiPehbipqzQPLZCxIUTUiaY-swlpC468j848x_Ga--1r4C76BJaRAAsVz89bCgtq5IglZ5nOSJznAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
گزارش ها از نفوذ پهپاد و فعالیت پدافند در شمال اسرائیل
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/alonews/147877" target="_blank">📅 15:16 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147876">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
آناتولی:
عاصم منیر از ایران خواسته تا انصارالله یمن را متقاعد کند که به تأسیسات انرژی عربستان حمله نکند
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/alonews/147876" target="_blank">📅 15:02 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147875">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
تسنیم: ممکنه خاموشی‌ها توی زمستون ادامه داشته باشه
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/147875" target="_blank">📅 14:50 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147874">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
دلار 227,000تومان
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/alonews/147874" target="_blank">📅 14:29 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147873">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kSGq2JoQ0J0ya_OSF9b96fhMwlD8Bb_urQYlNL8Sx9Pi0J42uH5Ch5QdicEHn4Ayb9AmbEtkkXg8LzkingpSNn-ILA4JN7MdCrfEf6vbE_Tj6PN3Xuesm15lrhBIFozIZbHHuU82LSRWY5G2hZ_ZtA7RSzuLLRaYE0okFUpo3HztrVrGtiwNmhjoC4lpaGFZF0ez3g0qjfbG9W2DjiNmlW3fWkx78zbw58wvoXXTN1y2kBA0NixBd-07fySmsqSgwNeJTonBWseEzil_OkYXI_8vE8ZScMsoDQyeE5FKOo5QqTtLTMIfhhz9_gHdl-f7DUhJqc4K_8qTlMuGN4KYGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
یک هواپیمای سوخت‌رسان سعودی از جده به سمت مرز یمن به پرواز در می‌آید تا پیش از بمباران یمن، به جنگنده‌های این کشور سوخت‌رسانی کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/alonews/147873" target="_blank">📅 14:13 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147872">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k-vVq33B_Wtchr163tl-Veidtj4Qz3eYEofngBRcPysCoVmGKzINSijwgLyj0pjn7XZBntPb008y50spLxUmCDEBRVSIa5aBA6FMsU6DEGulZ4CH9evdmludXFbwJcD85-Pmo2UFoAfWAZrbAaTcI1nKXyHrksaJRHfB8sSyu5gb-nzqJ6f1ZpuISytlF4_3Rf2Tr52wDoAJBOStuJuqaQNImZ0hMwvt--mMqjjVdA_FvLEjeadhoyDsGzr5m0m6eX2fMTnPFVyGLOhil-uK21kqtHvYRbmZcwLQs674LpFD7PKtvuvFw9bqI8hSCaurH4HDZ_pU9LMw__DtgOjnnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
امروز - توقیف تویوتا متخلف با راننده ۱۱ ساله در یزد
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/alonews/147872" target="_blank">📅 14:07 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147871">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
کرملین: تصویب لایحه تحریم‌های شدید آمریکا، تلاش‌ها برای دستیابی به راه‌حل مسالمت‌آمیز برای درگیری‌های اوکراین را پیچیده خواهد کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/alonews/147871" target="_blank">📅 14:00 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147870">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👈
ترامپ: اگر‌ کانادا بخواهد به اروپا نزدیک شود و اروپا به او کمک کند، اروپا هم تحریم خواهد شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/alonews/147870" target="_blank">📅 13:44 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147869">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HKtj8k_6P9xBq_dKYzX0wORC46wu4ByCAkPRUwNHOpOyWPn25leW4haHGy6zCWM-54g7WbOeG-02MkW6MB0zrEELjBS50IFPUaf2NEvytkA5VVsZW2lJUWbsoeSx2t_t5rzcftNchsiC-bw_X_J2acGjY68jCPnNM9fzH7ijJHslwcHy2qH5XPAZ-oyw76Q5e_6GM89v1LkM7Nutcct2D9Rz9EpPTgJD0ofINqXUoEAZvgtkwKg8H4OIjXO3RlIIv_gHz7ogdIU8X8HAfoODSW14te1u618MT7WyyBNs0mqYaJNsJ8wRjEoBJ4vXg5auvC4IKZO8Xff6J7Z6QcUqBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
۱۰ فروند جنگنده اف ۱۶ آمریکا به همراه تعدادی هواپیمای سوخت رسان، صبح امروز از پایگاه لاژیس در پرتغال به سمت خاورمیانه اعزام شدند
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/alonews/147869" target="_blank">📅 13:40 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147868">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👈
ارتش روسیه ویدیویی از هدف قرار دادن 1 قطار اوکراینی در استان دنیپروپتروفسک و 3 قطار دیگر در بندر یوژنی استان اودسا توسط نسخه هدایت شونده پهپاد گران 4 منتشر کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/147868" target="_blank">📅 13:32 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147867">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
رسانه The Nation: ترامپ علاقه خود را به جنگ با ایران از دست داده، اما جنگ همچنان به او علاقه‌مند است
🔴
اردوکشی او به ایران یک شکست تمام‌ عیار سیاستی بوده که اعتبار دیپلماتیک و نظامی آمریکا را تکه پاره کرده
🔴
جنگ برای ایالات متحده بسیار بدتر از آن چیزی پیش می‌رود که قابل تصور بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/alonews/147867" target="_blank">📅 13:28 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147865">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🚨
اتفاق وحشتناک برای طلا
‼️
‼️
👇
👇
👇
👇
https://t.me/+cs85WnZxgpM1NjRk
https://t.me/+cs85WnZxgpM1NjRk</div>
<div class="tg-footer">👁️ 54.7K · <a href="https://t.me/alonews/147865" target="_blank">📅 13:25 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147864">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
گاردین: عربستان سعودی از مصر، بریتانیا و پاکستان خواسته است به صورت فوری به جنگ با حوثی ها بپیوندند
✅
@AloNews</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/alonews/147864" target="_blank">📅 13:24 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147863">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">‏
👈
صرافی کوینکس رسماً اعلام ورشکستگی کرد تا پنج روز دیگر زمان دارید دارایی های خود را از این صرافی خارج کنید
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.5K · <a href="https://t.me/alonews/147863" target="_blank">📅 13:18 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147862">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db56a3dd02.mp4?token=nXXfTHWmSHEdJYT2AzSVLm8cF2UuK_zjCaHks3n82hXOIQE6gHCKyBoS-v2zEkqidY-YM1w-Lv09Ap9M_79l4BrC42dHmBt5FfY-h1nw9pLNctj3HvceK3mTee8_lLtQj3Rph6XxA7mcXAb2P-K9qjXMm_EgbtuEHCvbTkXM_LChgl2m1ctPcaza7vOHFEMTuQXVCgazIuMFub94yG_RDNUxXC4b1N-GI_nff28l6SNSjp_nIp2xPjx9pKLOZ4p7Snl8VuJXYo1M2QSYFdaixW66Bf2FS7VrkXUdX1cTIgvMHRxQaFdz3AtAx7qPJqnK1UHrosYh6wLfXrg9bPcZHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db56a3dd02.mp4?token=nXXfTHWmSHEdJYT2AzSVLm8cF2UuK_zjCaHks3n82hXOIQE6gHCKyBoS-v2zEkqidY-YM1w-Lv09Ap9M_79l4BrC42dHmBt5FfY-h1nw9pLNctj3HvceK3mTee8_lLtQj3Rph6XxA7mcXAb2P-K9qjXMm_EgbtuEHCvbTkXM_LChgl2m1ctPcaza7vOHFEMTuQXVCgazIuMFub94yG_RDNUxXC4b1N-GI_nff28l6SNSjp_nIp2xPjx9pKLOZ4p7Snl8VuJXYo1M2QSYFdaixW66Bf2FS7VrkXUdX1cTIgvMHRxQaFdz3AtAx7qPJqnK1UHrosYh6wLfXrg9bPcZHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
درگیری شدید در جنوب سوریه و کشته شدن ۳ نیروی امنیتی
🔴
الاخباریه: درگیری‌ها بین نیروهای امنیتی سوریه و یک گروه مسلح در شهر «صنمین» در حومه شمالی استان درعا، بامداد امروز پنجشنبه آغاز شد و گزارش‌هایی از تلفات مخابره شده است.
🔴
شبکه خبری العربیه گزارش داد سه نفر از نیروهای امنیت داخلی سوریه در درگیری با افراد تحت تعقیب در صنمین، کشته شدند
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/147862" target="_blank">📅 13:03 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147861">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">👈
ترامپ درباره اروپا: چرا باید بار مسئولیت این همه کشور در اروپا را به دوش بکشیم؟ ما بار مسئولیت کشورهای اروپایی را به دوش می‌کشیم
🔴
تنها کاری که باید انجام دهیم این است که بگوییم: می‌دانید؟ ما دیگر با شما تجارت نمی‌کنیم.
🔴
ما دیگر به هیچ چیز از آنها نیازی نداریم
✅
@AloNews</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/alonews/147861" target="_blank">📅 12:48 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147860">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">👈
پولیتیکو: پیشنهاد اورزولا فون در لاین برای تبدیل کانادا به نخستین «عضو وابسته» اتحادیه اروپا، پایتخت‌های اروپایی را غافلگیر کرده است.
🔴
دیپلمات‌ها می‌گویند این ایده پیش از طرح، با کشورهای عضو مشورت نشده و هنوز تعریف مشخصی از جایگاه «عضو وابسته» وجود ندارد.
🔴
کانادا نیز با احتیاط به این پیشنهاد واکنش نشان داده و مقام‌های این کشور گفته‌اند تمرکز آنها بر تعمیق همکاری‌ها است، نه جایگاه پیشنهادی جدید.
🔴
مارک کارنی، نخست‌وزیر کانادا، قرار است امروز در پارلمان اروپا سخنرانی کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/alonews/147860" target="_blank">📅 12:39 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147858">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
پکن: چین تحت فشار آمریکا همکاری‌هایش با سایر کشورها را تغییر نمی‌دهد
🔴
وزارت خارجه چین اعلام کرد: همکاری‌های تجاری و اقتصادی پکن با سایر کشورها بر پایه برابری و منافع متقابل است و تحت تأثیر مداخله یا فشار طرف‌های ثالث قرار نمی‌گیرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.6K · <a href="https://t.me/alonews/147858" target="_blank">📅 12:27 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147857">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">👈
الجزیره: شمار کشتی‌های عبوری از تنگه هرمز در روز گذشته به ۳ فروند کاهش یافت
🔴
داده‌های اولیه ردیابی شناورها که امروز پنجشنبه منتشر شد، نشان می‌دهد شمار کشتی‌های باری عبورکننده از تنگه هرمز در روز گذشته (چهارشنبه) به تنها ۳ فروند کاهش یافته است؛ رقمی که نسبت به ۱۲ فروند در روز پیش از آن و بسیار کمتر از میانگین ۱۰ روزه (حدود ۱۷ فروند) است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/alonews/147857" target="_blank">📅 12:24 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147856">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/445b3dec5a.mp4?token=h2C4rhHABPsAFCfR-XZlHrhAvGNow3TP9Fyq5_3BYTofAP7AjtnzsPetWPnS8I4QMrHu7BXieihjaqRHWvnbHdlmOgHwoHp4zULOGazHfGcLB7EhEY5fULBw50QmdBbCnW01_pxxMTkOEixmooMFLY_YvR_PYrEjKiDMLNCHOz1vlsGLQO2WU_DQM-dYlfd6stomgvvpfnepVzB-rOxcZqO3vMlpUwAxBky4QBJy7DJgtC3akUJ1nFjhQMgrhKJ33CP1dOgBkT1d4Y4LNZ4llyVF2dWT7BAUucpgI-cA9TMskWmBwAj9d-JXk3SOsatirWw1LVImsnt0v7Pj9aG9kQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/445b3dec5a.mp4?token=h2C4rhHABPsAFCfR-XZlHrhAvGNow3TP9Fyq5_3BYTofAP7AjtnzsPetWPnS8I4QMrHu7BXieihjaqRHWvnbHdlmOgHwoHp4zULOGazHfGcLB7EhEY5fULBw50QmdBbCnW01_pxxMTkOEixmooMFLY_YvR_PYrEjKiDMLNCHOz1vlsGLQO2WU_DQM-dYlfd6stomgvvpfnepVzB-rOxcZqO3vMlpUwAxBky4QBJy7DJgtC3akUJ1nFjhQMgrhKJ33CP1dOgBkT1d4Y4LNZ4llyVF2dWT7BAUucpgI-cA9TMskWmBwAj9d-JXk3SOsatirWw1LVImsnt0v7Pj9aG9kQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مرادویسی، تحلیلگر اینترنشنال :
بر اساس این 3 تا خبری که تو این هفته منتشر شده، بنظرم آمریکا داره خودشو برای یه حمله نظامی بزرگ به ایران آماده میکنه :
🔴
حرف ترامپ که گفت شاید قبل از انتخابات یا بعدش، کار رو با ایران تموم کنم.
🔴
صحبتای ونس که گفت شاید تو یک یا دو ماه آینده، درگیری با ایران وارد فاز جدید بشه.
🔴
جلسه بردکوپر، با فرماندهان نظامی اسرائیل و کشورهای مختلف.
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/alonews/147856" target="_blank">📅 12:13 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147855">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">به نظرتون کدوم بیشتر رشد میکنه؟</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/alonews/147855" target="_blank">📅 12:09 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147854">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">👈
پهپادهای اسرائیلی در ارتفاع بسیار پایین بر فراز منطقه بقاع شرقی و رشته‌کوه‌های شرقی لبنان در حال پرواز هستند.
🔴
پرواز پهپادها بر فراز روستاهای سرعین التحتا، سرعین الفوقا، نبی شیت، صفری، الخریبه، جنتا، یحفوُفا و الشعرا گزارش شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/alonews/147854" target="_blank">📅 12:01 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147853">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AjmssKPnFhRrJfhTohR5zfi3tIEI-d7_V_ONm0S_3-YlaXI7qq_fYct7VaOqOQ5kbGInaKUxas2QrpmizPu6AEr0S5ao1ae45EXEd0Hpetg8Q_GTfRGq9XBVZNaB5Mc_W0cg8j6ggJyIW-SPfCeu_1UngE7hYb00Tstwtn5Ilgi4T8fyiDsfuzIuYEopWW92bnfPz1lhyhHKJnz207UvwZ-Y0zddIaWF0NflM0vRIvcNdudQW2KLFS60aDmYk4BUL3X5ESdjIBUYQ0mld09ZPcwiSPypDrRbAd2JA6foBz8iVYqfaiHtVLaYk-8y2tH-ebO3o_v5p7f7WSQukNH1QQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصویری از حملات هوایی عربستان سعودی به مواضع حوثی‌های یمن
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/alonews/147853" target="_blank">📅 11:57 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147852">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
عربستان سعودی در ادامه حملات خود به حوثی های یمن، صبح امروز مناطقی از شمال و جنوب این کشور را هدف حملات هوایی خود قرار داد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/alonews/147852" target="_blank">📅 11:47 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147851">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dddM7GCUgzqIGxo4AJsfDAPveyy4y3lrVL18s2a_xJFVxKULSrfuD5xRIkVPR8hgA2zPGrzGdRDj0YIeQJEXViQcIHfsbF172CZDqnRQzUtcxcah9MqMPu_h5IMIBHXP9MPrwf_IDC3uCREhcq7L1CTGtFvqqyBRvcwbCN11A1gc0045oZNTN-75tswZ20CJRkB0jDRQybnraz5eXImzONsduRxNo-yMS3AmrtULvEkCW2xPbVgUqYTgnnydZcyptQFFMjyBtaPB82tM9ogJdVDFAC-V_FQOqOtxNfhDxZ_VR3nzR1DU31F1UuasH6wgzU9MHiN9-lrGUJ27_c3xFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قلعه‌نویی: اونایی که به من حمله میکنن مشکلشون من نیستم بلکه تیم ملی عزیزمونه، اونایی که حمله میکنن یه مشت وطن فروش خائن هستن
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/alonews/147851" target="_blank">📅 11:43 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147850">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">بیت کوین منفجر میشه
‼️
‼️
‼️
اگه توام نمیدونی بخری یا نه حتما ببین
👇
https://t.me/+4jOgodAq96dmYzY0
https://t.me/+4jOgodAq96dmYzY0</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/alonews/147850" target="_blank">📅 11:42 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147847">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Wiou6_74iBGRPYZjCPAjZwhdm7G67Ja_U65tUR1IEqkqzU6Qbb9HL4trElp-0aXRwLMez-_TqtUrBNJe-EV02hydibKhh0LV2MGPlYntM9ylsWVSOy0dI0Heqgv1N7J0sIMeMz5inpTTL0vUXOyjxJNdAiaKPoLD6Q8gljilC6XrtxhrtbTYYO4LPTqtLg4raoFEDS7Grhr6nxsinskw9Urde85snOV0B1kjiE8TTzVv16bZgU5TfZXF6jp_wsP7Yfyq_83XBH89Ew6V09xBwZhpPT25DAfjsBaZYh07WVXRBh6Q5x4iXoMEGXcTIwkCnaqMTNOIJ5KJoRWB7KeizA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HPbSOtKpwkD3iC0tNpU2FfzQ2jE9q1wzgRyIAHUBE-EC8_beqjK5d83HinouZqNxSRRtvJ0jXZNx6KGr30FwZ3AJY5iV9kFQ9frlAaBc2RB5RuTKNlFbzY1taLkjbc9w4P8Ke8MMb7ZdlvkgIp7yaY6yoKKU3Pk6DHULQ5TyWbOV1dMbuzQpX_mHscfrzSisPoicbuO8nQgGjWEXXn_aCtce8B2seCm7NEEeQn8eCzZqU3Rbb42V4AHBhKseoezw8U5ESWW8iwSlSpkYuyivfFBtjXyhynNWpab8puXoIWo3sqFXHLJ6njGoYrOkFOkRbvgpPZ8k0330h40HC7kPDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hJbFt8yWFjd7p31QD9WbCNcyBp4mHnGUlzMIx6aXwh8YJ9eJA_aeGRS9Wmo7Pox8ndJufPAO6QF9dsFTg70zSi3Jb0GNFD_WyGcvsNzQjCRzE8_-oqUxtbFaVNp2_Ho4DlO04Stb6ffkAKN3rJuIXuLOFIp--dO-WfmOAQZmhdFoTiYUV0szjJC-TpSZLcmcznCsSrXISsy760gS0esCK3kWT2ZOsmsNISiqEll8aGkHg47h3kvAKNH3yvJiBMZeQ_LKXWHLcgf027gqJqNwgj5eMbcl6n9Ov6iVHTlRZW5pFGS1YcwdEYOM5LbQgkMMs9r4XehLXKb0p10lhFD0rw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
هواپیمای هشدار زودهنگام آواکس E-3 آمریکایی پس از حدود هفت ماه مأموریت جنگی از خاورمیانه خارج شد
🔴
هرچند برخی، تغییر شکل انتهای این هواپیما را به برخورد پرتابهٔ پدافندی نسبت می‌دهند، اما دلیل اصلی این تغییر شکل، فرسودگی ناشی از مأموریت سنگین و به‌کارگیری مداوم آن است.
🔴
فرسودگی و استهلاک تجهیزات، بخش پنهان این جنگ بیهوده برای ارتش آمریکاست
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/alonews/147847" target="_blank">📅 11:40 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147846">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rpJ1Z-trZdQyUP-NsoKikxdr7DySEN3s5ks6O6vR36h0LZw9TIEIFNMJaDX3vfOhBcpSmvtGm-KqqNYK2Br9DsYZWnJzGmEkpq2BO_AllsKn-t_S9pnYkRHCYZF711AMLGtO_0_JTFgfePmvFI6Ai1BakMCvzK2fnxaDYo2iaKPO2cm87_AWetQCNDTyq10S8U_uUxbY8TbLatiuDOIe3E3VNHA4YVuNMNDjgn_2VMAfMQOWKQUzwjAmlK3kVpyrpJ20bFnnIvTmBBP_K3MsGHKDH0DyWx2wxW3l7J4Yp7Yx5S59hrtLj3ZQQtMKdTmcEdUSxr7_ArIen78opvIdLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وال‌استریت ژورنال: آمریکا در حمله اخیر ایران به اردن، در برابر حدود ۲۰ موشک بالستیک، ۶۰ تا ۷۰ موشک پاتریوت و بیش از ۱۲ موشک تاد شلیک کرد.
‏
🔴
‌برخی موشک‌های ایرانی از سامانه‌های دفاعی عبور کرده و به هواپیماهای آمریکایی در پایگاه موفق‌السلطی آسیب زده‌اند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.5K · <a href="https://t.me/alonews/147846" target="_blank">📅 11:37 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147845">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">👈
الجزیره: گزارش‌های مربوط به اینکه عربستان نفت خود را از طریق عمان عرضه می‌کند، قیمت نفت را کاهش داد
🔴
نرخ هر بشکه نفت با ۱.۲ درصد سقوط، به ۱۰۴.۵۹ دلار رسید
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/alonews/147845" target="_blank">📅 11:27 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147844">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
ساعتی قبل جسد پنج زن و مرد که گفته می‌شود قربانی یک قتل عام خانوادگی شده بودند، در بلوار سیمون بولیوار تهران کشف شد.
🔴
اجساد این افراد در گور دسته جمعی درون یک چاه عمیق دفن شده بود
🔴
عامل این جنایت دستگیر شده و پرونده برای رسیدگی قضایی در اختیار مراجع مربوط قرار گرفته است.
🔴
جزئیات بیشتر از کشف اجساد پنج زن و مرد در تهران
🔴
اجساد کشف شده مربوط به یک مادر، دو دختر و یک پسر خانواده می باشد
🔴
سال گذشته دو برادر خانواده که پس از سرقت طلاهای میلیاردی به پلیس مراجعه کرده بودند مورد ظن کارآگاهان قرار می گیرند
🔴
در ادامه تحقیقات، دو مرد به قتل پنج عضو خانواده اعتراف کردند و انگیزه خود را دست یافتن به ارثیه عنوان کردند.
🔴
آنها پس از قتل، چاهی حدود ۲۰ متر حفر کرده و اجساد را که داخل گونی قرار داده بودند، در آن دفن کرده بودند
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/alonews/147844" target="_blank">📅 11:12 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147843">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
رویترز: بحران اقتصادی ایران، مهاجران افغانستانی را به بازگشت به کشورشان واداشته است
🔴
افزایش شدید قیمت‌ها و کاهش ارزش ریال باعث شده پس‌انداز بسیاری از مهاجران افغانستانی در ایران از بین برود و درصدی از آن‌ها تصمیم بگیرند به کشورشان بازگردند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/alonews/147843" target="_blank">📅 11:04 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147842">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d0b6c3f846.mp4?token=S1ilPNepKRiG-4rQ43QYtrMJrMENTE19L5I4SdOByw46STDJm7tyVHQ9O43aBlQlLLXtKx-Rvr4I8W8Is2n-Lw076snZ-RZPZOcF7Glc-1XtfceYZ5kE2NmZQNp41K4RyLBa8xX4x9GWewEj3eUlr8l7T9QXH5FmddjMnR-nTDAfwu5Q2f84VJPXEDeevPrdP7jf5jHF-TKGq39lxg3PgY7APzMAfUtWNjNA6HBPfSPiiChI75U6uFoH2CheBRxAiMObSThjZMVarJU6cX2ehSvHZPAuFtq8_Lnq3GDtX5Dqzi4s6qrWYj67GP1K2roETPmmsOGNrQov0rbVDFht7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d0b6c3f846.mp4?token=S1ilPNepKRiG-4rQ43QYtrMJrMENTE19L5I4SdOByw46STDJm7tyVHQ9O43aBlQlLLXtKx-Rvr4I8W8Is2n-Lw076snZ-RZPZOcF7Glc-1XtfceYZ5kE2NmZQNp41K4RyLBa8xX4x9GWewEj3eUlr8l7T9QXH5FmddjMnR-nTDAfwu5Q2f84VJPXEDeevPrdP7jf5jHF-TKGq39lxg3PgY7APzMAfUtWNjNA6HBPfSPiiChI75U6uFoH2CheBRxAiMObSThjZMVarJU6cX2ehSvHZPAuFtq8_Lnq3GDtX5Dqzi4s6qrWYj67GP1K2roETPmmsOGNrQov0rbVDFht7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
عضو مجمع تشخیص مصلحت نظام: دیگر جنگ جدی نخواهیم داشت؛ یعنی دیگر تهران و اصفهان بمباران نمی‌شوند
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/alonews/147842" target="_blank">📅 11:00 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147841">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
ژاپن در واکنش به احتمال نقض حریم هوایی این کشور، در روز ۱۵ سپتامبر جنگنده‌های خود را بر فراز دریای ژاپن و دریای چین شرقی به پرواز درآورد
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/alonews/147841" target="_blank">📅 10:55 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147840">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Uor0vlLCbtsvd83ihLzMStUDUdEY2TohR2-Dv6-s0VQfSmGqMbPHSJDXDGWIXG-kc0gK5mXPk324XSGslR1Y8AzYNffOqmEfhsPgtNphIo9wpmgLFJ3cKyWAegB9Thl8dNm62Dx7IqrQo-BwvHRCX4kx5oduSrr2AqoksMFEXSLgOqw5gr_aY_mOYdV8iljxva73Gi37szsnKRd-F3KkO83XmRXAJyR8TSJPR09rCEhRL87SkylrYgl5nIreT6nKcWvTNWOM9kxyY1sdebh6Bx7kXbMJmqBO7JUBg5NuaHFM6YxSvnbrHIND656JbKIsdvvgZaHu7vkU3C8yhiqA5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
زکریایی، کارشناس حکومتی: امام علی تا آخرین لحظه بخاطر حکومت مخالفینش رو کشت، تو حکومتش هم فساد زیاد بود
🔴
حفظ جمهوری اسلامی از جون امامان هم واجبتره چون حکومت الهیه
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/alonews/147840" target="_blank">📅 10:49 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147839">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/957feeea93.mp4?token=WXxHpFN1bTwO_IQqllTgbWlrFaq1qOCCAL-P0cxAq_fMf5HYs3F8WJTk79olqS3DyNTIalpOOjLMIvFwmZR43mohN5Ae5vboO5A7_3dKchu5VtOR12ePPS90yh0CkhUz9fJHeOEQouBfHYxLwBlPPgZx7cSTl1nWFzOHi06LyWgAsDLhlApO9UzHJDXSyweQihU0oSD3tngXRGsuK5O8-zqOtDlGZ0uq0MiAOYnafKaweFRTI2K1ZHyBVU2IMc_GB2-xFKi6aTAtMupL5eCLxVPUaf_x6VUtActPKC4fnXazN8E4njlHEvEpXZxLsn8XjFdUfOLgxdwN8AzoEUxyeQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/957feeea93.mp4?token=WXxHpFN1bTwO_IQqllTgbWlrFaq1qOCCAL-P0cxAq_fMf5HYs3F8WJTk79olqS3DyNTIalpOOjLMIvFwmZR43mohN5Ae5vboO5A7_3dKchu5VtOR12ePPS90yh0CkhUz9fJHeOEQouBfHYxLwBlPPgZx7cSTl1nWFzOHi06LyWgAsDLhlApO9UzHJDXSyweQihU0oSD3tngXRGsuK5O8-zqOtDlGZ0uq0MiAOYnafKaweFRTI2K1ZHyBVU2IMc_GB2-xFKi6aTAtMupL5eCLxVPUaf_x6VUtActPKC4fnXazN8E4njlHEvEpXZxLsn8XjFdUfOLgxdwN8AzoEUxyeQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حمله به یکی از بزرگ‌ترین پالایشگاه‌های روسیه
🔴
پالایشگاه نفت «اسلاونفت-یانوس» در شهر یاروسلاول هدف حمله پهپادی قرار گرفت؛ تاسیساتی که از نظر ظرفیت پالایش، جزو پنج پالایشگاه بزرگ روسیه است
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/147839" target="_blank">📅 10:48 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147838">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a7347b9d41.mp4?token=lwa2NlWhsTgURT-DR2HFxkYj9SoufR0cspESprh9jV_KME9QQXph_ZtaRjTJUkd0LGdau09ORcKfRvVWBUSk6ImNyCueM8uyTbmwhaCJUHZaBg76KCcoRWGSRycMd790KYnGCpzys62nTF4CjQA850MvBeYJSsoEzfDkkeaTjPFvqRsFvvE-WCO_CFvUTfh9E5iUihjFkYWzVV020j4to2Fw2t-ntpqeu86HUGORTT-DPTY8u0lVOpEocGtR8E81NC037yIKXKf2_zA3AINCsT5VMCKQU8k6BB4hbtyxr8UEESrxzmRQhFkCFq7gW-vjREk_p3OPKJVGkKUbuVgqHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a7347b9d41.mp4?token=lwa2NlWhsTgURT-DR2HFxkYj9SoufR0cspESprh9jV_KME9QQXph_ZtaRjTJUkd0LGdau09ORcKfRvVWBUSk6ImNyCueM8uyTbmwhaCJUHZaBg76KCcoRWGSRycMd790KYnGCpzys62nTF4CjQA850MvBeYJSsoEzfDkkeaTjPFvqRsFvvE-WCO_CFvUTfh9E5iUihjFkYWzVV020j4to2Fw2t-ntpqeu86HUGORTT-DPTY8u0lVOpEocGtR8E81NC037yIKXKf2_zA3AINCsT5VMCKQU8k6BB4hbtyxr8UEESrxzmRQhFkCFq7gW-vjREk_p3OPKJVGkKUbuVgqHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
عارف: از مردم عذرخواهی می‌کنیم شرمنده‌ایم که امروز دخل و خرج مردم با هم نمی‌خواند
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/alonews/147838" target="_blank">📅 10:44 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147837">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
ترامپ: جنگ روسیه و اوکراین به‌زودی تمام می‌شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/alonews/147837" target="_blank">📅 10:38 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147836">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">این استوری یکی از اعضای کادر درمان در مورد زگیل تناسلی(HPV) هست که میگه: زگیل تناسلی به قدری تو کشور بین جوونا زیاد شده که وزارت بهداشت دستور داده فقط تایپ های خطرناک رو گزارش کنیم و بقیه رو منفی گزارش بدیم.  [@AloTweet]|</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/alonews/147836" target="_blank">📅 10:34 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147835">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ad31b0089.mp4?token=rhTqA_PZEbTzj3Ea3DA8pklCRh4lt0HKVNRMRyAjVK7TrwA8Sp_Bt5jJ8zdShR5ZAtPg-XL8vKY-HpuD-wLLkbWAqWbY0WViBacx24GvHUAkZkJgwSeOpxrYH3BXL2lkQn7IRc8-u2eul73iO19RKJnwK9HfRYStGxkvsKEto18C9IvUno6qR3x17NC6gtJlxJ4sZGgZLdjbdjy_7UpIunsKqrG-m8z5EDmbX9Gc6ghVELd8Gevd3PXAWp4l9Yh_WQoMDEQBmY5M8IV8LnqgirVfyeLkbYWu0-ziynU6eyu85eILcY1CywTGG_h4UsRe-boksUetjksuAH0R4oBQ8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ad31b0089.mp4?token=rhTqA_PZEbTzj3Ea3DA8pklCRh4lt0HKVNRMRyAjVK7TrwA8Sp_Bt5jJ8zdShR5ZAtPg-XL8vKY-HpuD-wLLkbWAqWbY0WViBacx24GvHUAkZkJgwSeOpxrYH3BXL2lkQn7IRc8-u2eul73iO19RKJnwK9HfRYStGxkvsKEto18C9IvUno6qR3x17NC6gtJlxJ4sZGgZLdjbdjy_7UpIunsKqrG-m8z5EDmbX9Gc6ghVELd8Gevd3PXAWp4l9Yh_WQoMDEQBmY5M8IV8LnqgirVfyeLkbYWu0-ziynU6eyu85eILcY1CywTGG_h4UsRe-boksUetjksuAH0R4oBQ8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
کنگره آمریکا تا پس از انتخابات میان‌دوره‌ای در ماه نوامبر تعطیل شده و چند هفته فعالیت خود را لغو کرده است؛ همچنین رأی‌گیری برنامه‌ریزی‌شده درباره استیضاح پیت هگست، وزیر جنگ آمریکا به تعویق افتاده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/alonews/147835" target="_blank">📅 10:34 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147834">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/712b365b48.mp4?token=ibsLt-l3ajxHgmaR5hsXYnFXKbk6kMxzOsrxzURYuAHPzU8UNHPRPYVZ4_s10e_xyy0TOOrUBt6g8KSMoFIJfycP3lV3PQcvjVE4gunpMgqIQ2zN_ZlUMaK73Omh7K3fsMuG_LMfQxhmyeGv0Ly-x69eZB-cv2JytBLrjCtFJp8ptNkWGJJsfS7DNIQXczP_ZmDLEpeYBu1uOtkuGv1V1Ovsw6oiNS1JYmP2AD6htscbWIJGR2gDhtVzTG539GznAjO6PIQLNEuAGI9dDLyWKj-fmXRmaiUAHB6U2qKqyEFtlhqef9AWlu836-i7QBoceyEgqUTV96a3t7AX-PJrjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/712b365b48.mp4?token=ibsLt-l3ajxHgmaR5hsXYnFXKbk6kMxzOsrxzURYuAHPzU8UNHPRPYVZ4_s10e_xyy0TOOrUBt6g8KSMoFIJfycP3lV3PQcvjVE4gunpMgqIQ2zN_ZlUMaK73Omh7K3fsMuG_LMfQxhmyeGv0Ly-x69eZB-cv2JytBLrjCtFJp8ptNkWGJJsfS7DNIQXczP_ZmDLEpeYBu1uOtkuGv1V1Ovsw6oiNS1JYmP2AD6htscbWIJGR2gDhtVzTG539GznAjO6PIQLNEuAGI9dDLyWKj-fmXRmaiUAHB6U2qKqyEFtlhqef9AWlu836-i7QBoceyEgqUTV96a3t7AX-PJrjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
فرماندهی جنوبی آمریکا (SOUTHCOM)
:
نیروهای «کارگروه مشترک نیمکره غربی» روز چهارشنبه یک
ایستگاه سوخت‌رسان شناور
در شرق اقیانوس آرام را رهگیری کردند که به گفته آمریکا، از عملیات قاچاق مواد مخدر دریایی پشتیبانی می‌کرد.
🔴
اطلاعات SOUTHCOM این شناور را به سازمان
«
لوس چونروس
»
مرتبط دانسته است.
🔴
نیروهای آمریکایی خدمه شناور را از آن خارج کرده و به مقام‌های اکوادور تحویل دادند و سپس شناور را غرق کردند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/alonews/147834" target="_blank">📅 10:30 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147830">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GJfXlndaZEwfga_HL8zMZ6OHbCkzTKfHNgahniuCEEKzfKzJbmvNOQrGsoWv-jR4f8ODHqXDz-2BjBjr50RGpm6AbVGoct1xZS86GpU9oTu3-mpRePyexw6rc6REJporv0sWthdjqEuhaw8_TlsfmdVc2J319hwC6kqF7cuadEP1pNqEJ8WhUjU1HGsy9uh1ECpX2crcd-PCHpWqAofPUeoQRCVA9wN1YZSzZHz_D2rrKsTbXcTum2eIcAE4dDV0dsNRANxGQprFyT2_b4ltDalRZ9mxoBHXd-oSyXBF7UV-mNqIIxRBeAusaS9kr2SUEAbGcZE6S3cy7s_bfhG8oA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DF9NTG-a2QgYu5L0WrwzLZq5apD8WGzRtWuOzjvbmltLHtjIc2AjEZyD7OCPWSx8OBZj-Z0aY_JAtfzcEdZ-D9ezYbMlh_nh0l10HNbCMAScMy6gbppkbXdfXHpyesfBRrLXhvlsmFYKxvG32xajc41lNqE1zGLyRdANRcbOPLyzd1AJzw60P5BTle95ZyXAZzLw_GJl6fWoxoY2oZc1_gJTaMy6H02eqzFjM7b5dEKilkuiZl_GDyK8dZSY3nJjPdLqABwYEVo9i6gqIM9LvS4CSwSy0I5eWUH68Oi5kQ2dR5yUH3B1buVSbcNS6dvMg_vgAB4ql0Hser4uxjNlpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IBd7EvVpZX-6g5sqnkubcEY0bPnCEFVPZlfJl5Aa_lqdvGyxUlSA9F91-2z_of-Q37YQRoSB3uQoEPq5WFNNJqOplzzlBtyePsj8srbkJeGQ9fgJWYjpBdh1IdfGKwGw9VKi09LEb1098Ms36Z1AmCfKSvYdHab4q62MIlHXzsJ8G2PZMy1W_qMq64qCxnUPcHu4if-Mdndldorkfa74rFhXDM1Q27qtDVnkYfjTt_rHG5QPB8okv41XLdsQXHJaYCnFeMJsEF3nE0DLk9vUNPKS2AwHTWABhuPuWZ9oSI02GVMuHptt6_y6WLA_XWgpcX6f1mRJ7dGibueByz9sPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GrE7838mOgEP5sVnQouf78-d4TO8Ql02wRAceUD-9v7n7COVtpLw7drWUx3rSyF-PvD6vgj6l-qlkLUDLlYTZMrNr_vrW5ZdwC-ujiluWKPYeNBvrq-lZnGCaGjzwSnIn9BKNGDinwGNEOnBLFkcoEwbnUMdExYOrNw12xugcElLskVHJxI92Bwj-2RIajGsvKhlI2ePSQoJMsxLdc60tSh2hbfAhhHTsE5ljlJjfI6LGGpTFsSxBbYjkb5dF50gHXRjpGG-aSATJom4RLtATvENXwmXfyyucdJ4LZDyGM2pUbKzpw1hayFZm4gZ-DBzf5KSkcLZKqHoD4IYymKLNA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
خسارت وارده در کیف بر اثر حملات موشکی/پهپادی بامداد امروز روس‌ها
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/alonews/147830" target="_blank">📅 10:23 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147829">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🔴
طلا به زودی گرمی 30 میلیون
‼️
🔴
سکه  به زودی 300 میلیون
‼️
🔴
دلار به زودی 250 هزار تومان
‼️
🤍
اگه میخوای بدونی کی وقت خرید طلاست
کی وقت فروشش، تو این کانال بهت میگن
@Tala v dolar
👈</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/alonews/147829" target="_blank">📅 10:19 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147828">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/33f4661bad.mp4?token=ET4nWhIDGxZuIQO-5zyVI6yYYN-_1dfmBmIbTKLWjrpvkWFyAyv7flRZRUGwRpGSE4LPu_BfIV-e_9WkvyjFcNdmEdRhe9-bzofpTUj-Wi0UgjoggnJOzZFZwU6jl9ih58U7iUmYWl0-MJSY48k9nMMTZEfbFCslvkGBtVhrYcTMmJPLhq7TvnFtgdwDTMlHm4QlkTLj2oMv53sqTt6XxG-pY8bDeztpi1xzbCyva_uPbk50oW9O1lfU1jVNC5pxUSFAp9VCOF8eOAsg28qY_aC8X7SXqKjCmoFessqC5-5psH2kOlFoBsEO8d7JUnmMiw7othazy0brSsZrHNojsYmT_EEIAdxF431l3Kg2pnGUeg8D9_M9t-cPB6xJrMPacl1xN5dGjvM1tDnX-YiRnRboiiTnCXs7Uqtoy-wrDy9NxeN7Ppwrr5nGXHJhJj228uqQ2XOWmxqCpijxyQLVU0LfJLgW3j6tfaOBOWm8SJfzTkXbKVwsT3fmvZNMa3CPgFSJHhRj1ibxaarM-Ik7qM1L_ymldQ4oVlJJ8v8eEizvK9BYSy-IXNkL1zFa4pYpvt3cQJhiNEsKRaZocsd9ndvJGqZh6CWavI7NaffPnkioM-bcxfB3PLjfzaKHXHyOjBYNdH3cs3-DQLd5v9KHnV9I1p2Qj7jR-0HLPqydbO0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/33f4661bad.mp4?token=ET4nWhIDGxZuIQO-5zyVI6yYYN-_1dfmBmIbTKLWjrpvkWFyAyv7flRZRUGwRpGSE4LPu_BfIV-e_9WkvyjFcNdmEdRhe9-bzofpTUj-Wi0UgjoggnJOzZFZwU6jl9ih58U7iUmYWl0-MJSY48k9nMMTZEfbFCslvkGBtVhrYcTMmJPLhq7TvnFtgdwDTMlHm4QlkTLj2oMv53sqTt6XxG-pY8bDeztpi1xzbCyva_uPbk50oW9O1lfU1jVNC5pxUSFAp9VCOF8eOAsg28qY_aC8X7SXqKjCmoFessqC5-5psH2kOlFoBsEO8d7JUnmMiw7othazy0brSsZrHNojsYmT_EEIAdxF431l3Kg2pnGUeg8D9_M9t-cPB6xJrMPacl1xN5dGjvM1tDnX-YiRnRboiiTnCXs7Uqtoy-wrDy9NxeN7Ppwrr5nGXHJhJj228uqQ2XOWmxqCpijxyQLVU0LfJLgW3j6tfaOBOWm8SJfzTkXbKVwsT3fmvZNMa3CPgFSJHhRj1ibxaarM-Ik7qM1L_ymldQ4oVlJJ8v8eEizvK9BYSy-IXNkL1zFa4pYpvt3cQJhiNEsKRaZocsd9ndvJGqZh6CWavI7NaffPnkioM-bcxfB3PLjfzaKHXHyOjBYNdH3cs3-DQLd5v9KHnV9I1p2Qj7jR-0HLPqydbO0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ
:
«اگر پیروز شویم، ۵ هزار دلار به شما می‌دهیم. همین، خیلی ساده است.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/alonews/147828" target="_blank">📅 10:06 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147827">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d9d7959037.mp4?token=EIxnYFv_0WDGKH2tncOgLcgqmhsDrv0A8uOqgjjEbbMTOufCTSVrpsHQdtG1B-788sOjFEnnBq906EVHNqI5giMeqaUeVsHERgVyY_RBPbKan2rob-Bs0xSsFO_hlm8UBo0dPj8iOOz2VjkmM1VWyB-aYuHIS30xNC5kDgeRyC9mTCw3XKwKfr5N0eHSPntuExDkN80P_A-WsA3FxSci3zlaU8DkvZjchoI_T2EBGQjPvUVVpZVaRmbpD2_DLp-YX6bdxpqAk2DNXWuTKye3bQxfQxMNhaY8xXt8a6UUChnAl7IUHR1E4atoaNiXKzt3plct1Bh16UyY7Guh-r1KUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d9d7959037.mp4?token=EIxnYFv_0WDGKH2tncOgLcgqmhsDrv0A8uOqgjjEbbMTOufCTSVrpsHQdtG1B-788sOjFEnnBq906EVHNqI5giMeqaUeVsHERgVyY_RBPbKan2rob-Bs0xSsFO_hlm8UBo0dPj8iOOz2VjkmM1VWyB-aYuHIS30xNC5kDgeRyC9mTCw3XKwKfr5N0eHSPntuExDkN80P_A-WsA3FxSci3zlaU8DkvZjchoI_T2EBGQjPvUVVpZVaRmbpD2_DLp-YX6bdxpqAk2DNXWuTKye3bQxfQxMNhaY8xXt8a6UUChnAl7IUHR1E4atoaNiXKzt3plct1Bh16UyY7Guh-r1KUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دونالد ترامپ: «بالاخره من آدمی باهوش و دارای ضریب هوشی بالا هستم.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/alonews/147827" target="_blank">📅 10:05 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147826">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/edf5f3fd3f.mp4?token=eMbuFBWEnqQQ4GCKW-1Jcl4lOkQl59jvzHtu0q2itGM-w0QqrqtOmY-riPkgpAGFAecvuiTWIuhXg9GUUS3aq0Donv38lH1jQR15qdTBzpSPtxinb5sVBuFf8liXnfXyHoPjK24Yc3iJlH_mRF1zeCW38JO1hHRQvYEZa3rfFlPrIXYP3C6OfKOyuK8PWHuWhcy3oXjMPMSu7Rm30Ogl_ciJTTUTlhdCi8vQno-61Q-XNCFp7HwlPXqF8JKNWbct-_C0q7F7hWnqfmxpw4jHMFbIy3Zr8GQiYdiVoUdT_uYv80PKMgMHAL6mt0fSzlHRR_ZYnk-vTcZ5m5Dbk0xrEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/edf5f3fd3f.mp4?token=eMbuFBWEnqQQ4GCKW-1Jcl4lOkQl59jvzHtu0q2itGM-w0QqrqtOmY-riPkgpAGFAecvuiTWIuhXg9GUUS3aq0Donv38lH1jQR15qdTBzpSPtxinb5sVBuFf8liXnfXyHoPjK24Yc3iJlH_mRF1zeCW38JO1hHRQvYEZa3rfFlPrIXYP3C6OfKOyuK8PWHuWhcy3oXjMPMSu7Rm30Ogl_ciJTTUTlhdCi8vQno-61Q-XNCFp7HwlPXqF8JKNWbct-_C0q7F7hWnqfmxpw4jHMFbIy3Zr8GQiYdiVoUdT_uYv80PKMgMHAL6mt0fSzlHRR_ZYnk-vTcZ5m5Dbk0xrEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دونالد ترامپ: «اگر دموکرات‌ها روی کار بیایند، این کشور وارد یک رکود اقتصادی بسیار شدید خواهد شد.
🔴
آنها اصلاً نمی‌دانند چه کار می‌کنند.
🔴
ما با رکودی مواجه خواهیم شد که تا به حال مانند آن را ندیده‌اید
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/alonews/147826" target="_blank">📅 10:04 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147825">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/177534508d.mp4?token=HhcSz2QdeRtr9z7O4bFkK8hyLloQ1BzwKzafsP1Y4d5J8G9qIFygZlkFyeHIqvW7favcOWfl44dQ8gTZA6NQh6tPQNksPoiyHtcBRht0xW5zBu0GHPSfqBP6HlP5EipQBehLamNcxDJU3_HqprEmHUFMgbVZjMeoOT8iZjDhWlHO0t9Do8mVfArXu5E6WHUTnLqaK2EyCevMVIx2KfTSqcKtnvQpQgfzavWSvdLzJBIelVvvLiNXRgZW9hnWmle22GIp07EETOuwz-xpZSbO5D3-u0QvU0-9V_xyJ_iRLqWmkRzSy51vgsd02uF4T8kxIexlOe3xRhi6eCbT_pqTDmJa2xJgvlaEuyojcJpKDBarF3ijyUUKXCG3wyaic32sTyOsiGYzpFsameo9h4Dveto5nJLtIyLCqKsPGGuea1s3geALW_UEZ5-y_4b5hbMMGkwdAjqZL0EQpmOzHIIlp8987Bdm5xk69JMq8QNyFG9ti9NdPUiyre_1BA7ttSLL4_oNcBTzBgF4Y_buScjiVcK3xaYIiiuBEoddIDrqs-CjoYKYgjEvidmPFsB1ikagdSXsmm5F9xvtW_eIxhWBhfbAZM2VIu6e7Xp0rLM4gu1HJR2dVByQkvqKIsgQX8eK2Vc-tqCQx90tuGBNLFZhhKeHsOZuR4GQcxre6tMVHQM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/177534508d.mp4?token=HhcSz2QdeRtr9z7O4bFkK8hyLloQ1BzwKzafsP1Y4d5J8G9qIFygZlkFyeHIqvW7favcOWfl44dQ8gTZA6NQh6tPQNksPoiyHtcBRht0xW5zBu0GHPSfqBP6HlP5EipQBehLamNcxDJU3_HqprEmHUFMgbVZjMeoOT8iZjDhWlHO0t9Do8mVfArXu5E6WHUTnLqaK2EyCevMVIx2KfTSqcKtnvQpQgfzavWSvdLzJBIelVvvLiNXRgZW9hnWmle22GIp07EETOuwz-xpZSbO5D3-u0QvU0-9V_xyJ_iRLqWmkRzSy51vgsd02uF4T8kxIexlOe3xRhi6eCbT_pqTDmJa2xJgvlaEuyojcJpKDBarF3ijyUUKXCG3wyaic32sTyOsiGYzpFsameo9h4Dveto5nJLtIyLCqKsPGGuea1s3geALW_UEZ5-y_4b5hbMMGkwdAjqZL0EQpmOzHIIlp8987Bdm5xk69JMq8QNyFG9ti9NdPUiyre_1BA7ttSLL4_oNcBTzBgF4Y_buScjiVcK3xaYIiiuBEoddIDrqs-CjoYKYgjEvidmPFsB1ikagdSXsmm5F9xvtW_eIxhWBhfbAZM2VIu6e7Xp0rLM4gu1HJR2dVByQkvqKIsgQX8eK2Vc-tqCQx90tuGBNLFZhhKeHsOZuR4GQcxre6tMVHQM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دونالد ترامپ: «اگر جمهوری‌خواهان در انتخابات مجلس نمایندگان و سنا پیروز شوند، من «سود سهام ترامپ» را اجرا می‌کنم؛ هر بزرگسال در آمریکا ۵ هزار دلار دریافت خواهد کرد، چون ما درآمد بسیار زیادی به دست می‌آوریم
🔴
ما می‌توانیم این کار را انجام دهیم؛ دموکرات‌ها نمی‌توانند چنین حرفی بزنند، چون آنها تعرفه‌ها را اجرا نمی‌کنند.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/alonews/147825" target="_blank">📅 10:04 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147824">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
ترامپ درباره ایران: «ببینید چه اتفاقی برای ایران خواهد افتاد. پایان خوبی خواهد داشت.
🔴
من می‌گویم این ماجرا کمی بعد از انتخابات تمام خواهد شد؛ اما شاید این‌طور نباشد و پیش از انتخابات به پایان برسد.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/alonews/147824" target="_blank">📅 09:50 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147823">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/920d4a383f.mp4?token=BNjYJ2bsaNHAWXgEYOf4ovwC9qr6Biam_qqxsAM2yoAoYnInLNdpSalRO5gs4dSF2zuVg6Hm5UdM9jgnZzF_Uwka0wvV4I_ZBqp0ZbPRvBwVjHni9IIBYMnEg5Amior7liAFMBOTkX-0rUES7U0vnH_rv22T5Z3tyhXxnp5I75ae1P2QQAfRTV6SL7NwjM4Uw960KlYPL3nJa-cdpH95Do0EEYi4K_ZadE4As2D-pqaXeEbfmHgs6tRi15oBJIoR4FjuhF3BabXSaTcoL4i89k4F9zN8Hu3o_f8pIzlEkjq73y8oLCHqBNIgV_INuJ4yPT-m0yYo9Mc7ZE6Fszb3QQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/920d4a383f.mp4?token=BNjYJ2bsaNHAWXgEYOf4ovwC9qr6Biam_qqxsAM2yoAoYnInLNdpSalRO5gs4dSF2zuVg6Hm5UdM9jgnZzF_Uwka0wvV4I_ZBqp0ZbPRvBwVjHni9IIBYMnEg5Amior7liAFMBOTkX-0rUES7U0vnH_rv22T5Z3tyhXxnp5I75ae1P2QQAfRTV6SL7NwjM4Uw960KlYPL3nJa-cdpH95Do0EEYi4K_ZadE4As2D-pqaXeEbfmHgs6tRi15oBJIoR4FjuhF3BabXSaTcoL4i89k4F9zN8Hu3o_f8pIzlEkjq73y8oLCHqBNIgV_INuJ4yPT-m0yYo9Mc7ZE6Fszb3QQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دونالد ترامپ درباره ونزوئلا: «ما میلیون‌ها بشکه نفت را از این کشور خارج می‌کنیم، اما نمی‌توانم رسانه‌ها را وادار کنم درباره آن صحبت کنند.
🔴
وقتی می‌گویند «غنیمت از آنِ پیروز است»، این یکی از بزرگ‌ترین نمونه‌هایی است که در تاریخ دیده شده است.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/alonews/147823" target="_blank">📅 09:46 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147822">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/34941eb79a.mp4?token=KlvXmZ59vXOgSOhqxsyxj28XQ4B-NG7jbrGalzw0dMozf86Y-jCdgp11nHzHHiOrZ4fuOBMFfhvSr2GYEcC1b1olTixblOuTCYT9XO9odd_r15m9KWr-Rp__BzJ_eiiyxPgWrxT6MlKlFvem_pomZKUVbXIY9xnD6_XsrsVzWwlkh7x4-MycZimQHD-6JvwOLckhQbSJGi90v3-Bxu0BkzeczfaPZvEM8jSx3Bx6NBeMGTZUat8L80ENJzAZQZrteksnwnJaFAL6aq8N-8745QzmrkjXQFixZJVbGZhgjEInK-N-86Nc9AVJrvf1AMlw2YMZ9vh1g2MXNxk1BBYwwUobYvWkHhSwkezvSVTI7RE3KHCj4s73oIRCE4wreE3Lby3QF_pkiCRuUhnde8ELa0Sb7d0WPI7bKThO7qOJKE9-KHqGHwMAwQ5DJqtWZBXUssYXBRZ_n3wipuJLepJKxiL8iHuFatZVL9NhVNSlyJnX0xD89IIPsXqBeysi0HZFtdwKAh593ODzkHsBLmaH-2AvbkTI9B4uyuEjTWKik7GpnmwO36S31sUsn5tu8OyQ9LOfhIvrygbWlPnKy6aklXMeLLeFDW-pnV-NlSpfVxgbDCkZ6wa0LmMEUPeKKNKAsJe1Gezv0VGo4YBbF-0em7zbOd4Q-6-cX-U2sbQMluE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/34941eb79a.mp4?token=KlvXmZ59vXOgSOhqxsyxj28XQ4B-NG7jbrGalzw0dMozf86Y-jCdgp11nHzHHiOrZ4fuOBMFfhvSr2GYEcC1b1olTixblOuTCYT9XO9odd_r15m9KWr-Rp__BzJ_eiiyxPgWrxT6MlKlFvem_pomZKUVbXIY9xnD6_XsrsVzWwlkh7x4-MycZimQHD-6JvwOLckhQbSJGi90v3-Bxu0BkzeczfaPZvEM8jSx3Bx6NBeMGTZUat8L80ENJzAZQZrteksnwnJaFAL6aq8N-8745QzmrkjXQFixZJVbGZhgjEInK-N-86Nc9AVJrvf1AMlw2YMZ9vh1g2MXNxk1BBYwwUobYvWkHhSwkezvSVTI7RE3KHCj4s73oIRCE4wreE3Lby3QF_pkiCRuUhnde8ELa0Sb7d0WPI7bKThO7qOJKE9-KHqGHwMAwQ5DJqtWZBXUssYXBRZ_n3wipuJLepJKxiL8iHuFatZVL9NhVNSlyJnX0xD89IIPsXqBeysi0HZFtdwKAh593ODzkHsBLmaH-2AvbkTI9B4uyuEjTWKik7GpnmwO36S31sUsn5tu8OyQ9LOfhIvrygbWlPnKy6aklXMeLLeFDW-pnV-NlSpfVxgbDCkZ6wa0LmMEUPeKKNKAsJe1Gezv0VGo4YBbF-0em7zbOd4Q-6-cX-U2sbQMluE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره ایران: «راستش، این جنگ به‌زودی تمام می‌شود، چون آنها دیگر نمی‌توانند ادامه دهند. کشورشان ویران شده است
🔴
قیمت بنزین کمی بالاتر رفته است؛ اما این بهای بسیار ناچیزی برای کاری است که ما انجام داده‌ایم
🔴
قیمت کمی بیشتر شده؛ حتی اگر خیلی بیشتر هم می‌شد، باز هم این افزایش به‌سرعت برطرف خواهد شد؛ مثل یک موشک که برعکس حرکت می‌کند.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/alonews/147822" target="_blank">📅 09:45 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147821">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
ترامپ: «من به هشت جنگ پایان دادم.
🔴
روسیه و اوکراین… دو رهبر آن‌قدر از یکدیگر متنفرند و نفرت چیز جالبی است. جنگ هم چیز جالبی است.
🔴
در واقع، همین جنگ باعث افزایش قیمت گازوئیل شده است. اما همه‌چیز خیلی زود تمام خواهد شد.»
🔴
ما تقریباً بار تمام کشورهای جهان را به دوش می‌کشیم و این وضعیت واقعاً نمی‌تواند خیلی بیشتر ادامه پیدا کند.
🔴
ما دیگر نمی‌توانیم این کار را انجام دهیم.
🔴
چرا باید هزینه کانادا یا مکزیک را ما بپردازیم؟ البته ما به توافقی بسیار خوب با مکزیک خیلی نزدیک هستیم.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/alonews/147821" target="_blank">📅 09:44 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147820">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f5ec161883.mp4?token=k5bCaai732Z88pA28PDl1j_a7OZI1SJklrAWBVTE2Vgp1SseQbL-ftZEhetGiRSGbOUk6HtNWnPELpnyLXo786S7ZrT3CmzAanBkOi1YiAD3HSA3gx3VzL1LS209jj3qSxI7_TCK6etyQNBDgkBTU4Uu7ZC-tEtg_z0_2QlSlWiJNpbZV8-HhIDlXp1ETLhM2CRUtPvnZwP3FaT2rNAWOAb8YJ7WKK20yl0UjZCucZthIVjwWBLu00GjdSfgprxclPde08dJSFfJ4UlOnflOlrCGXZJ1tIhdL-guLmHTBCFYsZIfwfmFDk1BojnBYuV-Fsq-VKQlRamR-NgmysVFA6g2r7V_q0wT08NiRsyJxUF5m7qSLe9e5CAUnzTOK2vEiJSij4j_mJ9rfTfWiAeGr_xw-hk9bAzNpVGgbmywJkPuBdfS-8yfU_rKYFRZK0wVdOBz1LFfEgGBSdJFYDqaruVjAedoQr63v5sCfgJ8ZVdYn-_ltoLuDWdXPL8dkOrsAQrW24Iq_RLzCtMRBly7mw5tObI5tiw0FKIf8ABvAdXOlxK4PKvSvDaYPwXFVswuFz7RN5yp-WIiBTZ06xiHhXlyZDC-9ITSvKdT9kzrbvoy6Rj20POmqbbS0MHHq5iivd8FG1GTHP-VG-OyH52Z_MzdZfsr7EVMi22U2ighGC4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f5ec161883.mp4?token=k5bCaai732Z88pA28PDl1j_a7OZI1SJklrAWBVTE2Vgp1SseQbL-ftZEhetGiRSGbOUk6HtNWnPELpnyLXo786S7ZrT3CmzAanBkOi1YiAD3HSA3gx3VzL1LS209jj3qSxI7_TCK6etyQNBDgkBTU4Uu7ZC-tEtg_z0_2QlSlWiJNpbZV8-HhIDlXp1ETLhM2CRUtPvnZwP3FaT2rNAWOAb8YJ7WKK20yl0UjZCucZthIVjwWBLu00GjdSfgprxclPde08dJSFfJ4UlOnflOlrCGXZJ1tIhdL-guLmHTBCFYsZIfwfmFDk1BojnBYuV-Fsq-VKQlRamR-NgmysVFA6g2r7V_q0wT08NiRsyJxUF5m7qSLe9e5CAUnzTOK2vEiJSij4j_mJ9rfTfWiAeGr_xw-hk9bAzNpVGgbmywJkPuBdfS-8yfU_rKYFRZK0wVdOBz1LFfEgGBSdJFYDqaruVjAedoQr63v5sCfgJ8ZVdYn-_ltoLuDWdXPL8dkOrsAQrW24Iq_RLzCtMRBly7mw5tObI5tiw0FKIf8ABvAdXOlxK4PKvSvDaYPwXFVswuFz7RN5yp-WIiBTZ06xiHhXlyZDC-9ITSvKdT9kzrbvoy6Rj20POmqbbS0MHHq5iivd8FG1GTHP-VG-OyH52Z_MzdZfsr7EVMi22U2ighGC4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دونالد ترامپ درباره اروپا: «چرا باید بار این همه کشور اروپایی را به دوش بکشیم؟ ما با کشورهای اروپایی
۲۰۰ میلیارد دلار کسری تجاری
داریم.
🔴
فقط کافی است بگوییم: «می‌دانید چیست؟ دیگر با شما تجارت نمی‌کنیم.»
🔴
ما به هیچ‌کدام از چیزهایی که آنها دارند نیازی نداریم.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/147820" target="_blank">📅 09:43 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147819">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8492b0e442.mp4?token=F1KwK4_tgc0V0LcHBp6s91Vkd7pph9X_JAnLg_YDFc4RCyDmOLBf3SIQKlh8RCffk_EZCiVyntvgEQYIWIhO7dXcFNBPwUB5Fyj-uge2zb4KpSOM1XanqDkL4z4fO_gzbc8CLX4Ju1eBB1Tlshb3ABytblShmBDP_Hb2vMANeUsMOT0zp2X8-0Z9nMEtXEF67_eD-fe2MEqogYyq2SCu-9mlvzFZP3TWuYnOwg4YTSVAjj5QVdfN6ZaJRk9npPvG6LCpny8QU4Uu_fFMnY2vfDFvboIoVgXra1rBmOyu-gXI8DakKAlJ0jjgTx_qxjflnfetmBoafZHc_smMElUYTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8492b0e442.mp4?token=F1KwK4_tgc0V0LcHBp6s91Vkd7pph9X_JAnLg_YDFc4RCyDmOLBf3SIQKlh8RCffk_EZCiVyntvgEQYIWIhO7dXcFNBPwUB5Fyj-uge2zb4KpSOM1XanqDkL4z4fO_gzbc8CLX4Ju1eBB1Tlshb3ABytblShmBDP_Hb2vMANeUsMOT0zp2X8-0Z9nMEtXEF67_eD-fe2MEqogYyq2SCu-9mlvzFZP3TWuYnOwg4YTSVAjj5QVdfN6ZaJRk9npPvG6LCpny8QU4Uu_fFMnY2vfDFvboIoVgXra1rBmOyu-gXI8DakKAlJ0jjgTx_qxjflnfetmBoafZHc_smMElUYTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ:
«اگر تجارت با تمام کشورهایی را که با آنها
کسری تجاری
داریم متوقف کنیم — که بیشتر کشورها را شامل می‌شود و انجام آن بسیار آسان است —
سالانه دست‌کم ۱.۵ تریلیون دلار درآمد
خواهیم داشت.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/alonews/147819" target="_blank">📅 09:43 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147818">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
دونالد ترامپ درباره ایران: «آنها به‌شدت در حال ضربه خوردن هستند. تماس می‌گیرند و می‌گویند: «می‌خواهیم توافق کنیم.» اما هنوز آماده نیستند.
🔴
ما هر زمان که بخواهیم می‌توانیم به توافق برسیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/alonews/147818" target="_blank">📅 09:29 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147817">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4fc4619f14.mp4?token=qgHxrgS393chBHKiZgKFBtz-OcrCj7-_LS06A2wDwHgAHr34vPe3S1PCH9qy_cxBlNTXoEwlby4J8Gv4a2kEgo-9UVMh_oIbWws-bu7Cs2RIsH4YQ6BM0Bx1xH2dq2pv2EKYP16aNvvstWfTkCOMI4Tg19At6f7uKk_thjduJtW3NEOB7RMgS13_keg8w53OHFWv8Bf2taDww6nMhwB16vy24gG5_FRqjlIFrWNjH2ROu4qDzlw2krCTX4rlN8NR8nGht4Kt4Gc0xiY59nrZKw2FeFrVlsGksCFVz-JuukV82zzxL6ZQPZtXVl4i0DfHARUsdUhIN9JjYA0RPqW1ew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4fc4619f14.mp4?token=qgHxrgS393chBHKiZgKFBtz-OcrCj7-_LS06A2wDwHgAHr34vPe3S1PCH9qy_cxBlNTXoEwlby4J8Gv4a2kEgo-9UVMh_oIbWws-bu7Cs2RIsH4YQ6BM0Bx1xH2dq2pv2EKYP16aNvvstWfTkCOMI4Tg19At6f7uKk_thjduJtW3NEOB7RMgS13_keg8w53OHFWv8Bf2taDww6nMhwB16vy24gG5_FRqjlIFrWNjH2ROu4qDzlw2krCTX4rlN8NR8nGht4Kt4Gc0xiY59nrZKw2FeFrVlsGksCFVz-JuukV82zzxL6ZQPZtXVl4i0DfHARUsdUhIN9JjYA0RPqW1ew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دونالد ترامپ درباره ایران: «دموکرات‌ها دوران تاریک آمریکا را به ما تحویل دادند و ما آن را به دوران طلایی آمریکا تبدیل کردیم.
🔴
و آن جنگ — آن جنگ خیلی زود تمام خواهد شد. ببینید، فقط تماشا کنید.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/alonews/147817" target="_blank">📅 09:29 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147816">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👈
تماس تلفنی عراقچی و فرمانده ارتش پاکستان
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/147816" target="_blank">📅 09:21 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147815">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r_F8AO3DFfXdd7OWu6zq03wvHWuE9pMhxU8JlyFCk1d-R1p_Yg3VrLh63fyCIDMf25VJBEJTLBIA-pa_GgeYUz8qJtsNjuPM0Q6ODW3lUPXy732-fG5MXIgYeCZXKVa-Q-NtIIUznyL6uogmMTM12gdTXdzpsBD9SDXs3rnpyl7RNB26kh7JTDSLEfciTrgAn4g1WkKYixElSDSR4b7XL_uL2mPecF2jXMVjcp3-FYB_dqfhQwjAWW4YZw41eY5kGBwAAztSbVgJ_MA47J8qMVJAOZU9sM722MjTewgSSR-SkN3XhEwKS1BkeQnW_jScJkowrrnUHunjnZ06oS8qxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
کیم یو جونگ، خواهر کیم جونگ اون: نشست آژانس بین‌المللی انرژی اتمی (IAEA) درباره خلع سلاح هسته‌ای کره شمالی را «حرف‌های بیهوده و تکراری» خواند.
🔴
او گفت جایگاه کره شمالی به‌عنوان یک کشور دارنده سلاح هسته‌ای، قطعی و غیرقابل تغییر است و «با هیچ چیزی نمی‌توان آن را تغییر داد»
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/alonews/147815" target="_blank">📅 09:09 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147814">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
واشنگتن پست:ذخایر موشک‌های پدافندی عربستان سعودی رو به اتمام است، که این امر باعث شده تا این کشور برای دریافت کمک از متحدان منطقه‌ای و غربی خود درخواست کند.در حال حاضر، مصر و عمان تلاش‌های میانجی‌گری با حوثی‌ها را بر عهده دارند، و این در حالی است که هدف فعلی، دادن فرصت به دیپلماسی است
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/alonews/147814" target="_blank">📅 09:05 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147813">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
اکسیوس به نقل از منابع آگاه گزارش داده دونالد ترامپ قرار است سه‌شنبه آینده در حاشیه مجمع عمومی سازمان ملل در نیویورک با رهبران یا وزیران خارجه شش کشور عضو شورای همکاری خلیج فارس دیدار کند. گزارش‌های منتشرشده نیز بر برنامه‌ریزی این نشست با محور جنگ ایران تأکید دارند.
🔴
انتظار می‌رود نمایندگان عربستان، امارات، قطر، بحرین، کویت و عمان در این نشست درباره مرحله بعدی جنگ و پیشنهادهای آمریکا برای شرایط پس از آن گفت‌وگو کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.8K · <a href="https://t.me/alonews/147813" target="_blank">📅 08:59 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147812">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tdMu8ABV77zVq0augbrI_ZhgE0326ojnj4HHTL8l5BxYCzs9XBcVaFJlCt_Fdjj6_def2HCk5MUva6vTKLrlbibkAn_qq_e88bMiZg_BidhTZrBPCevapfl-I5ykai3ciAWyFzuVijFxTIulxcYNFe0nXWDISn_bXPi3vAzB1ROYboyOYigHV_fbkmmxhl8lu2pMX0JwJgFK6a3pALDCrxs7n6v_hofAWvPiDacALQqX49DHtlSNgVBi4tfsRl18Sh08gIOgfmJYEKa3Cv5Gul1rHAd9trbvGv2Y_ZNkaIjvYHdhigGhKcAguAmLbkmIV98vM8VQXZE7vKdhpkJIIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
امروز ۲۶ شهریور، تولد کمبوجیه پسر کوروش بزرگ و روز پسره
🔴
روز پسر مبارک
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.1K · <a href="https://t.me/alonews/147812" target="_blank">📅 08:53 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147811">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">👈
مجلس نمایندگان آمریکا طرح تحریم‌ها علیه روسیه و ایران را تصویب کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.6K · <a href="https://t.me/alonews/147811" target="_blank">📅 08:47 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147810">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65c03c4e5b.mp4?token=Ba9MX_8MTaM5_sUNa2jh_c0apTlxzHYS9rsVXztSpIIRwq1zgeLnPnytdD8YZA0KVsTlw43XT9J-lxSGroypAddGYQuCQjDG9d-FhypT8TgJ530VK8Wsc8zfBkXIgyjvmkTzhRrddTEyi7w-z0uGTDeQU-ap7xQjORxUfGLUmAq5Xp0Xs7a47V9bvytbhF8dtCpXIutdSSxBUvElttNlF-7JYf7vguYuy4frKWqo8xgc5lyFZ6M1sgycbf-iIq3LCoBOJ8f-dUmpGnP_1ksKF8uxq5NO0cdZ4pjdlTRfxmL_cEPPAUkkhKnRnD5GCO_RDVM0cqi6m-_i_mTuMFZVSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65c03c4e5b.mp4?token=Ba9MX_8MTaM5_sUNa2jh_c0apTlxzHYS9rsVXztSpIIRwq1zgeLnPnytdD8YZA0KVsTlw43XT9J-lxSGroypAddGYQuCQjDG9d-FhypT8TgJ530VK8Wsc8zfBkXIgyjvmkTzhRrddTEyi7w-z0uGTDeQU-ap7xQjORxUfGLUmAq5Xp0Xs7a47V9bvytbhF8dtCpXIutdSSxBUvElttNlF-7JYf7vguYuy4frKWqo8xgc5lyFZ6M1sgycbf-iIq3LCoBOJ8f-dUmpGnP_1ksKF8uxq5NO0cdZ4pjdlTRfxmL_cEPPAUkkhKnRnD5GCO_RDVM0cqi6m-_i_mTuMFZVSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خبرنگار:
«آیا قبول دارید که آنها برای کاهش قیمت‌ها، به‌دلیل جنگ با ایران، نرخ بهره را افزایش می‌دهند؟»
🔴
دونالد ترامپ:
«نه، آنها نرخ بهره را افزایش می‌دهند تا شرایط برای ترامپ تا حد ممکن بد پیش برود. مشکل آنها این است که ما
بهترین اقتصاد تاریخ
را داریم.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.1K · <a href="https://t.me/alonews/147810" target="_blank">📅 02:12 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147809">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">👈
ترامپ:امیدواریم که به انتهای "جنگ" با ایران برسیم. ایران می‌خواهد یک توافق منعقد کند.
🔴
خبرنگار: آیا از طرف آن‌ها با شما هیچ تماس‌هایی برقرار شده است؟
🔴
ترامپ: بله.
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.4K · <a href="https://t.me/alonews/147809" target="_blank">📅 02:06 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147808">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c79e5a8106.mp4?token=d27ekee6sQuiBg8B7JQ_l13PktKhZX1Pznevu4OJfOBcPRkQ1mSP10eJuaX_7PUL1rtZcb2HoreFbFbYO14I7d4qqOF4vRpHNpIA6ye3a0PCAufD5UKiPH9r8Hak_caZskZSYJsx-iAhPsAIwL6ZIOhckMwHWZvksW6x_ynBzeLzrn2hTiWoUkHyL051fTzsKoXI6uaUexCdm_MVcGDUYDTUSp2qwmImc71rjtbQtT4Zx0ZsdQNJA3HLfQvVmUJNplpMXyfx6NGtDjl92-BWwDeYOdn-xA54INHLWuZ7sgbN4-fCwUPPPv1T3Bl3KkBnWzzB-TwdnOIDp_6WmudQjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c79e5a8106.mp4?token=d27ekee6sQuiBg8B7JQ_l13PktKhZX1Pznevu4OJfOBcPRkQ1mSP10eJuaX_7PUL1rtZcb2HoreFbFbYO14I7d4qqOF4vRpHNpIA6ye3a0PCAufD5UKiPH9r8Hak_caZskZSYJsx-iAhPsAIwL6ZIOhckMwHWZvksW6x_ynBzeLzrn2hTiWoUkHyL051fTzsKoXI6uaUexCdm_MVcGDUYDTUSp2qwmImc71rjtbQtT4Zx0ZsdQNJA3HLfQvVmUJNplpMXyfx6NGtDjl92-BWwDeYOdn-xA54INHLWuZ7sgbN4-fCwUPPPv1T3Bl3KkBnWzzB-TwdnOIDp_6WmudQjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ:امیدواریم که به انتهای "جنگ" با ایران برسیم. ایران می‌خواهد یک توافق منعقد کند.
🔴
خبرنگار: آیا از طرف آن‌ها با شما هیچ تماس‌هایی برقرار شده است؟
🔴
ترامپ: بله.
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.4K · <a href="https://t.me/alonews/147808" target="_blank">📅 02:06 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147807">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">👈
امادگی جانفداها و رزمایششون برای زدن جنگنده های امریکا و اسرائیل.
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.7K · <a href="https://t.me/alonews/147807" target="_blank">📅 01:57 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147806">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CUCygYvSrGTlrh2Pf6R2_QxOpqx4jNO31LacbJ9HiDyNTvvbocstdarRft_Qmp8GiUVevV6056pbQ60IHyXNAwByLlqFUqlB7uVvWtqfywC0eLf3qIHrJhAP4R5V_K3CjPpsp9K4-kK9N6lypyraHdQnScE_x15rCN9-1ju_vtinTUpRR4XT8v4Fw5B0u5yrzqamnCGT3Ges7sjeEmitrSc9L3w9gjTBC7xbmMd3bCGXKrOJMnvUhLd-OYk_NSS2IO-nOZGkdDjBUfDd54zT7kv7sOnVlDshMfqwY4UWFmSgYr_nCCsr5aOkVFlYnruHGo-eyXlfPZDaaqQQ0J4Ujg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حمید رسایی:
بنزین باید مثل کل دنیا لیتری 450هزار تومن بشه
✅
@AloNews</div>
<div class="tg-footer">👁️ 79.6K · <a href="https://t.me/alonews/147806" target="_blank">📅 01:29 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147805">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kCIXzm0jdZRNWx2CZf17wsFAdt1WYGhNcLy9xEsl2JnTdEwRL2RmMp23RITehqYzneFS2Ap5vqaolapzHs-Ol6ww4eRi-4ULiOle_Ty8FCIW0pmVVPRJl-gQvfWwZ602fS7eDgPc5wtQz2kybImVmy9now6EsyKLyOp3NmxriyBZMCf8_Lxb0VQC51N1M5sYUw8AqRT_9bbo7hsAIeuc2mcBDIk4XE4iSof0SqhofS-BgK57mjWyuHgNoFtZV2lI-2YpudfdjnWTub-rCfNnxZ178TbGCBWf6r_ngd9H_s2hD0My9mBbdNLTJYYLCvKRNALfJaB4zm_5IQ1dHbOffw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
یک فروند هواپیمای ترابری روسیه در تهران فرود آمد
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.1K · <a href="https://t.me/alonews/147805" target="_blank">📅 01:26 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147803">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RWPvgGnEeZBF97rWJgJ4a2CLlT14KPi83Wmu-sv8UH_gErnRIESaiIYE6FgrukFcy4BnlPdwsR2riZqZz7QKfgdvmOG7KjYuTRgKqefDTV-Ces53srYwotulwSmqRNo1CVYHS903e1JdVKY8jNGjSH8EIuLgR6uQ-viDzc37Sn7cdRfAVj3CdpcrcMs4vFG2WCVODnTMWmBmGvNGuyg4IXokmOkhC6ZFKj35rrN0qWnMaaVfZqHN8Pe2yr9jpF7HHkKFm3gw5CN8qYJ0f96K_K2mELvTdksjfJ2eoxjVf6HH7l8ds2Q9wZy3gjbELPNhOgW-giZxC4RsCKAiw7dLZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SzHe0HQFOH1QG7KxLLKwhIJY9F7whWp6diBfoZQ8pxx03FjdUhlCCzNbhvZo75ezBDwNYXLuQJ_fbHBT_b_L-f08-gCLNr3Sj60bJw_KxEeFG1Obu5M0ZJ3GLcejs9iNY3r8AOiogsjz5ILztzA_5fwT-lCd1jK1a8Cb_2T9eNyzoE_tjLirOq8CRriMmoliduVkqV1HF9lfvoEi3p-cIx1k-BSEaZn4l_TelpssfPw5naIWa_7-K4XJk2J3nIUJkChqtkvpSi15ucQjA7TO988IYT5QhZGGFe3pbwkwccTbWKM7FLrl-1fgk3I7SDy-lHX3QYk3cS6BsbMo9PXnvw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
علی ضیا، مجری معروف با دوست دخترش رفته ایتالیا و عکساش حسابی وایرال شده:
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.6K · <a href="https://t.me/alonews/147803" target="_blank">📅 01:00 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147802">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">👈
توپخانه اسرائیل شهر سربین در جنوب لبنان را هدف قرار داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 77K · <a href="https://t.me/alonews/147802" target="_blank">📅 00:56 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147801">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O9PtXEfaUs4A4XLWfFlMCTaF-bVpwNrt0-berfwJVmkRNzYplDJsPqQXYDAwPbN9i0rgu148Ifoi9BPaa5QLy_y5-p_JvqIN_U2SBsXXhPmXKFZOFb310zJOSR6ab3NnBz6YgJtSqCnTt3J7At3Wwv0zqwcPSnYhowj6mMJFfZitUGj_qTXM4egygRjZ45iWgXQ55v-8p765P0sjLjM2tXzWTPD_rMVw9-zGH0c8rD-YctgKVFuHhhZvluk08qzjvN1MgySsnt16CP9SZZsZuTGdwwtEJmLDlNEkeQ2szRHVkCSaJy4cMH4p3o7Y-Y9i8VndxgrMSGubh94fNAq5UQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
استوری جدید هادی چوپان
🔴
زنده باد جمهوری اسلامی
✅
@AloNews</div>
<div class="tg-footer">👁️ 84.6K · <a href="https://t.me/alonews/147801" target="_blank">📅 00:44 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147800">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sU4vnrTT1Aoff_gFOgf4MmD8G_2qkrua8NoqSMrIL4_wJY3WxkWOCqC3me6Q0uLSQTTyftfkWUa9gT4vAHxzycRSm0OLl_GiAob7psYVtW3gjDoI1h1WkoBApLgGxHHef3N4-g0eDjeoWVKzyKcf0rY28Lc7TRLJFza4YEZo6RmbWmlGgonWizL8I03bzF7PfvxR95Ku-l14TS9J6gpG3nJpe4PI1eF1YiKKqbvUHmGj0UjGekVtdI7ae9sZq2H6QFuYSZEZz0ZYQlK3q2mAJvVU88BFLq6O6k-5xoy04-cRSV0ZzibntCQg5954JsNPjfsGvTypeD_yg85x_47SNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ به فدرال‌رزرو: نرخ بهره را به یک درصد یا کمتر برسانید
🔴
ترامپ گفت نرخ بهره در آمریکا باید به یک درصد یا کمتر برسد و مدعی شد آمریکا «بهترین اعتبار جهان» را دارد و با ورود سرمایه‌گذاری‌های جدید در حال رونق است.
🔴
او همچنین گفت اگر آمریکا تجارت با کشورهایی را که در برابر آن‌ها کسری تجاری دارد متوقف کند، سالانه دست‌کم ۱.۵ تریلیون دلار به دست خواهد آورد.
🔴
ترامپ کسری تجاری را معادل «زیان» دانست و بار دیگر خواستار کاهش سریع نرخ بهره در آمریکا شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 81.1K · <a href="https://t.me/alonews/147800" target="_blank">📅 00:19 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147799">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WzSQiOKc38hiX2Obu98BKHhJZCBiTq52wwXhxJo5m7JLiJgekoELXxafkch_xbh8jFNOlNhRHAPBwboT_fTVEPKhkvXvqdxn5M8URVbIxoh-HfsIKDTk9DJBUxzzN5efMmGX6mOJ0RzuQm8i6mRcybH867uTBPLLC244MkzPS0qOWJj_lVHU3I6r-04o1uk4LDGvb28PcOEVD2D6ifbJVs0YBItt8VHj1Z1jien34wYiUR6GOW91XJEBy3N-46CBBqmSDtOl0uo7a0LVqJw1rJGLZvBLVITVKr94J8-oavum0NBGios7chxxwPN1GGHoPtQ_NYG3uoaFC0UcRFTiGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سه حمله هوایی اسرائیل شهر المنصوری در جنوب لبنان را هدف قرار داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 81.5K · <a href="https://t.me/alonews/147799" target="_blank">📅 00:07 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147798">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H_Hr3cRB-cZ_CtDNL77NPc_aRjS4cL9uP72RQLEKl7A314veLKCF00B1b_GyZA-U8nT7ii_-L_Xh611I_-qyUgSH0jioBgRkFWg3WQfrEExbJR21hh8sA23qg32XJtNIge6G0je9vpUy1yrg62TU7lI-mlqujHf9TMLGcrynTeeUUp9T6CNUaxLdRFJK9p9T6qOA9wFLhQTSVSnVXfPgipbvGS13u9N4rM8CpD8D15xFObNdLSXZUqpuDQ7Dq7gx-A33hI_0XQrVHquW2_Mq-iCnp7_1t0tpVSVhqnA3cNVVnt4cNkj6oOc-0CY3uvc-JGn1o55xgk-5p1NDD-ShZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
علی قلهکی: یکی از پیشنهاداتی که اخیرا «عاصم منیر» در سفری که به تهران داشت، مطرح کرده بود پیوستن ایران به «پیمان مکه» بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 80.8K · <a href="https://t.me/alonews/147798" target="_blank">📅 23:57 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147797">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d3bf42cd99.mp4?token=ocg8Hg3iWbK4Dh8F1fOMAkC5eicbbnn1dukGSqy59vxKIhqpPGlMNRtAngEPZLLrFygaL1G3tJmjTgon1p31k-N67m49wvrGJ-kCK4NXLo4D9eo330wYc3eByeWNqbdlhk_Sl8N26G-5CSNrRwAmn1gS7e4BKQRyxtM59ItlfqCJrnStAiFU-mcDJ0a4lP0ejEUuB_wcoVX2Tur2ri6wKYd8Fo6CPG-0SXT-J6WaR53HGWOwPNzDBhaB6ufmz2Bs6NLR1LuG56M2RS3CP8siP2UVA8Fz_jM-ou6HkPxl7LjdL23yGCXEWfaIVaYt_EqlFL01vNl9PUKbNO0DVX765Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d3bf42cd99.mp4?token=ocg8Hg3iWbK4Dh8F1fOMAkC5eicbbnn1dukGSqy59vxKIhqpPGlMNRtAngEPZLLrFygaL1G3tJmjTgon1p31k-N67m49wvrGJ-kCK4NXLo4D9eo330wYc3eByeWNqbdlhk_Sl8N26G-5CSNrRwAmn1gS7e4BKQRyxtM59ItlfqCJrnStAiFU-mcDJ0a4lP0ejEUuB_wcoVX2Tur2ri6wKYd8Fo6CPG-0SXT-J6WaR53HGWOwPNzDBhaB6ufmz2Bs6NLR1LuG56M2RS3CP8siP2UVA8Fz_jM-ou6HkPxl7LjdL23yGCXEWfaIVaYt_EqlFL01vNl9PUKbNO0DVX765Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویری از لحظه سقوط جنگنده سعودی مدل F-15 در نزدیکی استان مأرب در یمن، صبح امروز
✅
@AloNews</div>
<div class="tg-footer">👁️ 80.8K · <a href="https://t.me/alonews/147797" target="_blank">📅 23:47 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147796">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z8zJAC_iw3IVneA5SDpRj4bBevMPQm4wd8vrKbR7xxmc73Hb2S9MbfjcZ_OKSduMy37mAziCtcAk1DtBSYXnEZBfS2Ov0CBdVudlA7zHKWz7vUAEtr6jp2YKwAiTupBRyaqA5QrowU8etI_1c-SEEdl3uX6EcnrbBqvIivkHFysxUohg2fdSkepKLNZgeB56RA--qLlfH2C9WIBbukmm5ITQrESel6q-4UP7cSg2R4HcHSMoAlhc4gGBp4G-7EobS5ytyhm75RxYlByiy8S5kyqJJBI03pt6jWOaxAbjC9kV9-aDVcvboCJwOFUWnXSN8Pzb9EVYB2ua6l6bwdzs8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
باراک راوید خبرنگار آکسیوس: یک منبع منطقه‌ای مطلع تأیید کرد که دیپلمات‌های آمریکایی آخر هفته با نمایندگان حوثی‌ها در سفارت آمریکا در عمان دیدار کردند.
🔴
در این دیدار، دو طرف درباره تنش‌ها در دریای سرخ گفت‌وگو کردند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.6K · <a href="https://t.me/alonews/147796" target="_blank">📅 23:41 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147795">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">👈
فیلد مارشال محسن رضایی: به هیچ وجه به آمریکا اعتماد نداریم و واشینگتن برای جلب اطمینان جمهوری اسلامی باید اقدام عملی انجام بده
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.2K · <a href="https://t.me/alonews/147795" target="_blank">📅 23:37 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147794">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5a7085b819.mp4?token=M57KygaiER-JkMBZ4Dkby8prQ2Nvg2eYfRFWq4VT2T1HvGrcpDfsoSJpt1AgoJAP1sE8_ItDPa16U4116TgFaIbEGDJy8HTtxUrFy814IuCltZ2vGbUqs8xlszW6w2FfjAhn_CF0RCFmyI3XqTEIs3a0g1l4JIeP9t_9r2YqTqi3WyHway0qoqQ1BrG16UJGT6ZYWD7qOklZVJPxvBP4PoE-DanZcxM4nstWXXuiOndtDqrrHZT5HIIZiG_k1UL5r8nhDt-2sqwhGFylyFOo9HqEiOIPmwH4uIQQ6wF6OVLG6gfinSFO4w9zZ6DRLmQ-As23jv8I42hrk3nygUPkjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5a7085b819.mp4?token=M57KygaiER-JkMBZ4Dkby8prQ2Nvg2eYfRFWq4VT2T1HvGrcpDfsoSJpt1AgoJAP1sE8_ItDPa16U4116TgFaIbEGDJy8HTtxUrFy814IuCltZ2vGbUqs8xlszW6w2FfjAhn_CF0RCFmyI3XqTEIs3a0g1l4JIeP9t_9r2YqTqi3WyHway0qoqQ1BrG16UJGT6ZYWD7qOklZVJPxvBP4PoE-DanZcxM4nstWXXuiOndtDqrrHZT5HIIZiG_k1UL5r8nhDt-2sqwhGFylyFOo9HqEiOIPmwH4uIQQ6wF6OVLG6gfinSFO4w9zZ6DRLmQ-As23jv8I42hrk3nygUPkjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وقوع آتش‌سوزی مهیب در تأسیسات نفتی کرکوک عراق
🔴
گزارش‌های میدانی از وقوع یک آتش‌سوزی گسترده در یک انبار مواد نفتی در شمال عراق خبر می‌دهند که تیم‌های امدادی در حال تلاش برای مهار آن هستند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 81K · <a href="https://t.me/alonews/147794" target="_blank">📅 23:32 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147793">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U_qQ42pP57LUATAN56nU8nuQL6ATU4VFCAGi88f7G_egyYY85BZpVNgsXXfczuE_CGKth-ecZSt8D_U--Xl3o15Rozi5wCXrEZgm42SjEPrUuyOHVLzrdPZjZYZ5O-X7TVvcQFvkHdifeGYa1Kz7yDFeEeXHKaeFwA2g3CCNHUaszDupjP4CoNI7nF54yczMeNDaiIlhHpdQKS0z7x2cXhgX-T0W14zvyLwhauPorhmaSQ3QowWBn4Y0hckPgP-SDJrPu6JWS_mxela5kS7oGqzpCJWrZDcuzWr3j9pMGxz9_kS87jU7yCZtSpnTvaRTXlnNnHPKRGzn1TRlhpc5bA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
شغل جدید تو ایران آنلاک شد: فروختن نوبت تو پمپ بنزین
✅
@AloNews</div>
<div class="tg-footer">👁️ 79.1K · <a href="https://t.me/alonews/147793" target="_blank">📅 23:18 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147792">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
تعدادی از هواپیماهای تانکر سوخت که از بریتانیا برخاسته‌اند، امروز در فرودگاه رامون در ایلات،اسرائیل‌ فرود آمدند
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.5K · <a href="https://t.me/alonews/147792" target="_blank">📅 23:13 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147791">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6138b0dabd.mp4?token=RiWhvvRPz0aLMKYXQIvuVS_VzB6LGRw2Y7B232n6UDA1L_ko_zCHFI-pU-xcse2G9amFBkEJrg4e3Ge8SY16QWD0ApAh5PMYdzqHgTZ8zIIn1HRHJp2FlgncI5DW2biqe6O7UnW4Wkh-nVSbajVHWIkZJZY7qTwuRA-B09f0GuxDTbmX6XemIDD6Qzi9eU5zhGK1cmRiRwDNn7l5SxsVjgkrXWda5qurigzFR7Vv5KdybedHKNdFdF0mKD2sMLQRqMh6JvZBLXWneh_ckPHTCgTbrv3sM0nRZr0PJUZ_nw6iRay5s7rbSrntpK9H1lDtDkCTmKtiHQoaSPwu8oTOxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6138b0dabd.mp4?token=RiWhvvRPz0aLMKYXQIvuVS_VzB6LGRw2Y7B232n6UDA1L_ko_zCHFI-pU-xcse2G9amFBkEJrg4e3Ge8SY16QWD0ApAh5PMYdzqHgTZ8zIIn1HRHJp2FlgncI5DW2biqe6O7UnW4Wkh-nVSbajVHWIkZJZY7qTwuRA-B09f0GuxDTbmX6XemIDD6Qzi9eU5zhGK1cmRiRwDNn7l5SxsVjgkrXWda5qurigzFR7Vv5KdybedHKNdFdF0mKD2sMLQRqMh6JvZBLXWneh_ckPHTCgTbrv3sM0nRZr0PJUZ_nw6iRay5s7rbSrntpK9H1lDtDkCTmKtiHQoaSPwu8oTOxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
شورای رهبری ریاست‌جمهوری یمن (PLC): تصاویری از حملات به مواضع و تجهیزات حوثی‌ها در المخا و چندین موضع در خطوط مقدم در محور تعز منتشر کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.8K · <a href="https://t.me/alonews/147791" target="_blank">📅 23:10 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147790">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e2dea2d9fa.mp4?token=orjzk7DBuZbmO4UxXLZuy30m6xB_0h4dUrGlkfR5iJmVPWH8O498tzJlBgO1C0rvZ7BEbyLpDgl9JGVeHnYyg-zMaUhHE2Jbcwqfcv7gtJLmgK_6Nk19rxqyN2woQToZsUvYXzr53Vb7E4zGAWWGzZUWxTwCSq4KZb5nEtyw0sAvuig0KdVWx4nzGo6qhQjLNtUImEar7R9ZbHYt5n4TbqZHbXDM13ktsd6kxcH3AJZJBzZLzLK7XmYN-ZKoxHQqkGqvWLcec7cvwCpp8_6-QjBldqiwUVdLA1yeB9iCuXNx20fr5CmQzO5EUK8cWOyGMRTQMFWicrWZW8JA-1GR7YWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e2dea2d9fa.mp4?token=orjzk7DBuZbmO4UxXLZuy30m6xB_0h4dUrGlkfR5iJmVPWH8O498tzJlBgO1C0rvZ7BEbyLpDgl9JGVeHnYyg-zMaUhHE2Jbcwqfcv7gtJLmgK_6Nk19rxqyN2woQToZsUvYXzr53Vb7E4zGAWWGzZUWxTwCSq4KZb5nEtyw0sAvuig0KdVWx4nzGo6qhQjLNtUImEar7R9ZbHYt5n4TbqZHbXDM13ktsd6kxcH3AJZJBzZLzLK7XmYN-ZKoxHQqkGqvWLcec7cvwCpp8_6-QjBldqiwUVdLA1yeB9iCuXNx20fr5CmQzO5EUK8cWOyGMRTQMFWicrWZW8JA-1GR7YWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
احمد الشرع، رئیس‌جمهور سوریه:
این نگرانی وجود داشت که تحولات به سمت انتقام‌گیری و موارد مشابه کشیده شود.
🔴
یکی از اهداف این بود که به مردم توصیه کنیم اجازه ندهند شور و سرمستی ناشی از شادی آن‌ها را به سمت انتقام‌گیری سوق دهد؛ به‌ویژه در مناطقی که آسیب‌های زیادی دیده بودند، مانند شهر حماه و مناطق دیگر.
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.7K · <a href="https://t.me/alonews/147790" target="_blank">📅 23:03 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147789">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64f5f39d29.mp4?token=lcVe5es1IfJqLVOIOIOGfs24Pg8pUkt_acD2V4PBeQT04DU7-rbCXKbiiWVxUrV7pfvGU5EFv6fFLOvIT7fyysP9fIVUp7C6fQsIsLC-huZvl1uM2XadrSEL5SK3BMbA5HU6Q1XDwIT55RlO_a_NRY4ulCL8Y-ZReLROTnU3xGPAGomSZ7VeMS5iWJMAFP9cOaI_zJT1cphZHz7Re8y81p9UWXnNdFYeTYcLXPdayglJ-rDxTpsZLkmfex2tgs2D0cEBFnHg8tVNjAwW39sq40Cbb06I5FkME9BfrPJRsa8nwrK7GdOgjKWKpdOXWOGc7z8cCrDTu8Bc8ywr4z4Ntw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64f5f39d29.mp4?token=lcVe5es1IfJqLVOIOIOGfs24Pg8pUkt_acD2V4PBeQT04DU7-rbCXKbiiWVxUrV7pfvGU5EFv6fFLOvIT7fyysP9fIVUp7C6fQsIsLC-huZvl1uM2XadrSEL5SK3BMbA5HU6Q1XDwIT55RlO_a_NRY4ulCL8Y-ZReLROTnU3xGPAGomSZ7VeMS5iWJMAFP9cOaI_zJT1cphZHz7Re8y81p9UWXnNdFYeTYcLXPdayglJ-rDxTpsZLkmfex2tgs2D0cEBFnHg8tVNjAwW39sq40Cbb06I5FkME9BfrPJRsa8nwrK7GdOgjKWKpdOXWOGc7z8cCrDTu8Bc8ywr4z4Ntw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خبرنگار: «پیام شما به ترامپ که بارها خواستار کاهش نرخ بهره شده، نه افزایش آن، چیست؟»
🔴
کوین وارش، رئیس فدرال رزرو: می‌خندد «چیزی برای گفتن ندارم.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.2K · <a href="https://t.me/alonews/147789" target="_blank">📅 22:58 · 25 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
