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
<img src="https://cdn5.telesco.pe/file/fSsmYNny0YvDsYuPTvA9evFABbDAKoMe0NNYiteGpzD4vzJ2WtJZHB2ijmL0rsudSE8z7bdM865l7teX2WoYorq3mo5zhOFYQu_D3gh4rD3yL5n4nmuW3CCHsLYZiCyddUC4GvExwwI1fmRVxXCPg6pw6xh5f7xOVc_iwmyAs3ZGtqPyWDdGYG021WH7Wqj4uzqAB43CFtvLYN5vN3slkyscJrBMChMGAI-krAD3Wjqn4Itvyh42WT2QKya7w1QozpKZGEZozHzRfZEGv8LJg_KqUJRdDvnFvfiLOHvv6zJw-loQCqMMD6Kv_UnWQ2GjxwnAWkPS3ibE1un0i1wenQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 جام جهانی 2026 | فوتبال 180</h1>
<p>@Futball180TV • 👥 636K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-14 14:06:16</div>
<hr>

<div class="tg-post" id="msg-98295">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/meBBpRcmlraLoE7jh8AaLjdnO-sBowvrVs4NWpuDYho5DHiInRklFvUDEqMQjhjtclKEYcFSrDpGSaj1-jw7zuElQx08BpQ-x9k5QCQ0YWc4R76CYf3LtjmyfDaFNa8ogD6ccEY-qDnTOH5xiR9YwUQgrsLWX9H9JdOhqRaWAkKYMdu9BArDBNkJu2eXWzkI_YdCqSCHsBqRu7AcsFQ2Jd77FBF0_1FUGAGAL_0YUKjcdnl_BX2hn32A7BXGKNT0a8DnoL7bwpqxCIso7aB1-fIAjHV1xV6nHLuP5_kYAcfDYeF9_kgBdAsTFHPHpEfQCPy08vRwuROhR02w5xsrQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
گریه‌های علیرضا دبیر در مراسم علی خامنه‌ای
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.75K · <a href="https://t.me/Futball180TV/98295" target="_blank">📅 14:01 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98294">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hqWP_FYf3MAJVSzpaTwskltNVFU0PytGzXGDrnq6XzXTr2icrLn6cc-2enUDWJndpEc_8pL7S6_4SiZkIobLoFGQ54fJHhvThe3k7YtbH4tuMOCwblhsMcUuQzLdqAnmBRRB5On9QGibB5eJ9CNdTJ-SyO6S1ufukH6b1GTbVme-VK8QHOxwP0WZ6d0340xvmqeuNG_lns2SbW7Q_XSR09RSnDh9gkZLxwwBRoE0nTqsQPsnDvAbvVpkH46tLY_FKaR19oGXO8i9416mN40p1jf2OC-HYswu0JVw2VR9qVv0IOsPwDiratOQuQHEpKB3joLzBAt-kL1FG39t8MuJ3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#رسمیییییی
؛ دومفریس مدافع تیم‌ملی هلند با عقد قراردادی به رئال‌مادرید پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.62K · <a href="https://t.me/Futball180TV/98294" target="_blank">📅 13:38 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98293">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dde65c4bdf.mp4?token=DvY_1OV_ulaSPfjkSzuBQn2cc42CHGyIIuzXyW5uihFl4llunMBmtxGeMiODA-fVW2Uumre7TIE_QYohfKPXbYERx1FwCc274dhQI3TJPpY-WybOYSXvZPQntvQMtOovuMszrFKdLFEDgKwc3jwZey4ECKYMHy6MqwDMViaBeaISJykTYyQGbs8XHAcMl9h0ERvKqq_9V3buhiggvXoXjHj2qgdRIM8FXLgLVuKWqCTF6w1L4wOsn2I2H1P-LB0DU-ZbPqd9gqgKSI60zzm0Jn0khki5r1cdrDN3WqCdOJGO_S0aizkdbPsQ21a2lram1L_OGHGNrjX0uGKwYosTeQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dde65c4bdf.mp4?token=DvY_1OV_ulaSPfjkSzuBQn2cc42CHGyIIuzXyW5uihFl4llunMBmtxGeMiODA-fVW2Uumre7TIE_QYohfKPXbYERx1FwCc274dhQI3TJPpY-WybOYSXvZPQntvQMtOovuMszrFKdLFEDgKwc3jwZey4ECKYMHy6MqwDMViaBeaISJykTYyQGbs8XHAcMl9h0ERvKqq_9V3buhiggvXoXjHj2qgdRIM8FXLgLVuKWqCTF6w1L4wOsn2I2H1P-LB0DU-ZbPqd9gqgKSI60zzm0Jn0khki5r1cdrDN3WqCdOJGO_S0aizkdbPsQ21a2lram1L_OGHGNrjX0uGKwYosTeQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
ماجرای درگیری معروف علی فتح‌الله‌زاده و مجتبی جباری را یکبار از زبان خود فتح‌الله‌زاده بشنویم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/Futball180TV/98293" target="_blank">📅 13:20 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98292">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fP5MOl29kAnpu1nvU9Lgqa7iXwDMgEawYVEXuTSJ2IL46-gT41rSTIJFE9mNMgf7o_4J5iNQvKuwu0k4fpQsIVgnZx14ONaXXnw45O5eBVXYeey73106AkMTN30HI3jj90jVpFCyj0BpShKjtt1xNblecCnjJpbRhQg60Gp5fwiGleCbpGIiDUuXTq7YitjwiQX8FPiIBx8DalBBOH9oB8RlM2WC9twXNQyp_c5cmsxA9mcy_FxJoeOfRkcYJ1qhmmcOR3HnFviONseN0_7Hib-_g7r6m2aLeBs2AziJMUGRLjaJ8oBkFLkxBUNdFp0ItMnOFemrRMNUT2n11MeWAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
فابریزیو رومانو:
کلوپ به عنوان سرمربی جدید تیم ملی آلمان انتخاب شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/Futball180TV/98292" target="_blank">📅 13:18 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98291">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e63e17f963.mp4?token=dGb_l8K4h9qFqKjnuIXo5mM_8_DC6iRMZP_5Ea2H8yTAIEWq7LNYRChBukQWyw_xv-_ZQPRkr85BTf_xIXD85JhZrn1Y1LUO---Is5ENxX-0-lXT0q-6kgbGvl80pastowN5mgykc5_ffCrKnAxcoO6rwwTnBr37DpjM020ZOKCv4mZIK_IgHtGuA_i6l4JHs9-d5hjH6L2WhVQtaf2ks6RWHMGv42MxrKFl0NISZdInK3SkY58pnmezhUPSnfwHOtrDTnc-MZIvHRf4Rv46Dh0_vWwdyjSGFCkQ2ez6Ofr4P77Z53_X_hg6p4OmzkQCvKW71TEDvK7rnCCSPkbBBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e63e17f963.mp4?token=dGb_l8K4h9qFqKjnuIXo5mM_8_DC6iRMZP_5Ea2H8yTAIEWq7LNYRChBukQWyw_xv-_ZQPRkr85BTf_xIXD85JhZrn1Y1LUO---Is5ENxX-0-lXT0q-6kgbGvl80pastowN5mgykc5_ffCrKnAxcoO6rwwTnBr37DpjM020ZOKCv4mZIK_IgHtGuA_i6l4JHs9-d5hjH6L2WhVQtaf2ks6RWHMGv42MxrKFl0NISZdInK3SkY58pnmezhUPSnfwHOtrDTnc-MZIvHRf4Rv46Dh0_vWwdyjSGFCkQ2ez6Ofr4P77Z53_X_hg6p4OmzkQCvKW71TEDvK7rnCCSPkbBBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یادی‌کنیم از حماسه تاریخی محمد مایلی‌کهن در گفتگو با عادل فردوسی‌پور
😂
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/Futball180TV/98291" target="_blank">📅 13:04 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98290">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a4ade1cc7.mp4?token=jteLqQgyGPiXw5U7_8vfakquLMZYIx86CKAhv5YcIQMe4FgukMhMMwn1ErP9pnUvK_tpJDzEBb4zXrCcr2MsZulfwpjR-MMNeGqVBnERy0ZDE2WmEIGTxFFcu8c_PCSwA9yqwImGeixWTGRmEYJkCtForSeaQLG-dAtpvGO3yYYYp1M4aEzeEjTcigGeulKzVBf_CxOdUj3ozWQpMlOnpmB4J1vJ1GZaf7EpKg9sosrJVQEpyZczk-oYDGaUHn4h3rszOGDiuezLYYVE8ul5W8ECVqJ6fYbQ-Ir7qaRWHdo_W1RIxMD7u-y9FR0k92IC_DJ9BTdRAIeOuGpdYTNdNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a4ade1cc7.mp4?token=jteLqQgyGPiXw5U7_8vfakquLMZYIx86CKAhv5YcIQMe4FgukMhMMwn1ErP9pnUvK_tpJDzEBb4zXrCcr2MsZulfwpjR-MMNeGqVBnERy0ZDE2WmEIGTxFFcu8c_PCSwA9yqwImGeixWTGRmEYJkCtForSeaQLG-dAtpvGO3yYYYp1M4aEzeEjTcigGeulKzVBf_CxOdUj3ozWQpMlOnpmB4J1vJ1GZaf7EpKg9sosrJVQEpyZczk-oYDGaUHn4h3rszOGDiuezLYYVE8ul5W8ECVqJ6fYbQ-Ir7qaRWHdo_W1RIxMD7u-y9FR0k92IC_DJ9BTdRAIeOuGpdYTNdNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
هوادار کیپ‌ورد: «ووزینیا شوهر آینده‌مه»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/Futball180TV/98290" target="_blank">📅 12:40 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98289">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0306de1296.mp4?token=fKcRWip9bp6FvIheC11QC3aMr2ski-IKf_80CDGqPpycSWI5cqTAdDYP1kUO1UbIrhdp6QoKL4qjYlnRzCw8wWgQQLJUKoPv46frgD3b5qYyQtElpx-woxvpvqbPWC5pQaiYUntGMYiyhw7aj-DqNQLTVuUr5J-MMiNbgg_nQUzNqzhbIHO8B-zAM6h-6rjqmyelvbiFhS3_Vxc0ej2dam_DPpZOwnS0AH2FLSlw642WSICqtoW08Choav9ECBnMj0ghjlNdMMqTjaIy24HcVJ5wnt8ahcBREdNB0uXolVduWUVrojRUz4cStF3CrV66SFGgxpZ7ugl9Cv-_nx25sw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0306de1296.mp4?token=fKcRWip9bp6FvIheC11QC3aMr2ski-IKf_80CDGqPpycSWI5cqTAdDYP1kUO1UbIrhdp6QoKL4qjYlnRzCw8wWgQQLJUKoPv46frgD3b5qYyQtElpx-woxvpvqbPWC5pQaiYUntGMYiyhw7aj-DqNQLTVuUr5J-MMiNbgg_nQUzNqzhbIHO8B-zAM6h-6rjqmyelvbiFhS3_Vxc0ej2dam_DPpZOwnS0AH2FLSlw642WSICqtoW08Choav9ECBnMj0ghjlNdMMqTjaIy24HcVJ5wnt8ahcBREdNB0uXolVduWUVrojRUz4cStF3CrV66SFGgxpZ7ugl9Cv-_nx25sw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
🇨🇻
نام ووزینیا تا ابد در تاریخ جام جهانی خواهد درخشید.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/98289" target="_blank">📅 12:20 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98288">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">شادی فوق‌العاده سمی هوادار کلمبیا بعد بازی با غنا
😂
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/98288" target="_blank">📅 12:04 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98287">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🚨
🔴
#فوری‌#اختصاصی_فوتبال‌180
🔴
تا این لحظه و با تصمیم اعضای مدیریتی سرخپوشان، سرمربی آینده باشگاه پرسپولیس به احتمال بسیار زیاد گزینه‌ای داخلی خواهد بود و خبری از سرمربی خارجی برای فصل‌آینده نیست.
🔴
در بین گزینه‌های اصلی همان نفرات همیشگی یعنی یحیی گل‌محمدی…</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/98287" target="_blank">📅 11:57 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98286">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n7kWIz8YqysUp_tfgpKdGZH8_iOd2taTJm885NgdE6Z_y3N6zJ9vYIkQ8lOKIA1wTNBgAyytHspCHEuiILyj8nEmH8VKy1sHX6WOdb433EQCCUHAjgv7IshUE4a7xQg7_t5q-mkSlHkhLWxlmz4F6vbLtBO5QpHU7SS1llrHng-ougD0WN7nw8Rmf3HLRl8qmM9L7BAWli16_J2iUzm4uRiDctPIozQtdhhYL7RYENCEIqdutEo7--i8pOcTu1g7gplFJbto3ByQODeoEBNCwy4unXQsqkXT0WsvEOl-Z8FreVl9rdcBibU0SZeAqoh1O99Ixeb0fQ9uxhhW3VB_Aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🎙
🇵🇹
🇪🇸
گاوی‌قبل از بازی با پرتغال:
برخلاف اخبار و شایعات، بنظرم بازیکنان پرتغال با احترام فراوانی با کریس‌رونالدو برخورد می‌کنند. اینکه می‌گویند رونالدو در رختکن محبوبیت ندارد اصلا درست نیست. همواره واقعیت‌های یک‌تیم در رسانه‌ها بازتاب داده نمی‌شود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/98286" target="_blank">📅 11:46 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98285">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6bf2d4a738.mp4?token=AVo7HaQzSv6Xgc-twizTpu2MwxnL2PvxhPwq6ISYmXB0K-yXRmi2hlZMGlaLiBv1jA3owNucY-6Q_9uX7sJVl_yq2EPv5iyP3DMxfJ-z7tKxSkbniPMo6m6Ug9yZrlG-UZvGCvZAohS4rXtC9dbeF0Fj5ZZr2lhyyavNERngME7jRK3fzdIFI67GwPcunehj6UfPRzxnCjfVxW3Re2dSn56iDxMkaRuimMUqGS4RKPvb3c2g0NYwEL-D6hQ8KuTbd08PPAehJs2EUBXJ7spzTB8NNvIWSmHo2LUbgNFBybMKkEKMLFeBpn84QJDyHJIP8I1Or09nugM9pymW1gh6HA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6bf2d4a738.mp4?token=AVo7HaQzSv6Xgc-twizTpu2MwxnL2PvxhPwq6ISYmXB0K-yXRmi2hlZMGlaLiBv1jA3owNucY-6Q_9uX7sJVl_yq2EPv5iyP3DMxfJ-z7tKxSkbniPMo6m6Ug9yZrlG-UZvGCvZAohS4rXtC9dbeF0Fj5ZZr2lhyyavNERngME7jRK3fzdIFI67GwPcunehj6UfPRzxnCjfVxW3Re2dSn56iDxMkaRuimMUqGS4RKPvb3c2g0NYwEL-D6hQ8KuTbd08PPAehJs2EUBXJ7spzTB8NNvIWSmHo2LUbgNFBybMKkEKMLFeBpn84QJDyHJIP8I1Or09nugM9pymW1gh6HA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇬🇭
جادوگر غنایی در بازی با کلمبیا!
😐
😐
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/98285" target="_blank">📅 11:40 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98284">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GffH_tjK31GGdCRUXpjb9g76eGU0VmzSsUprV2ENK0jkhDVBNwjVWcSm94RsjDFETRmoE_dSwn-8vqViUQ29fRqoxb5Wfot6Xh6jFfX_JLV8zcLBbnB7AAxJ0FqJslLWOhdmzWoa2QQbvMn8skP_u3osWErE_BGt4NoXk2eeZdNv1z1KuhjJUfHjlSTz7OHbbMBxk3ZmDCv0Z2p1eMqKh9li0F0SM1cCHLtIAddVHVMogiysDgx78FmX-vA7ZRsqi8vQ8cMkemwo7KfSQB6tSdoPWL_N4IzLpTRpuIMET08hw-PQDgI569oT9Q_dQXuklYPbdms5vad-3K3QZJHSrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🇫🇷
دیدیه‌دشان
:
من خیلی حال میکنم وقتی مردم به امباپه میگن دیکتاتور. دیکتاتور همیشه کلمه منفی نیست و وقتی راجب امباپه اینجوری صحبت میشه، ذوق میکنم و بهش افتخار میکنم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/98284" target="_blank">📅 11:20 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98283">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a015c896ae.mp4?token=CtTB1kKXxsf7xh_Cj7GQY7m0pUNVgEkIxWINnUKbXaNX4ZUVfjnBFCl7wkc-DEut1NMarLqqJzLQ6uLIX3yMS8Cm80k4JeEONtkg1jqf1ziIpxK_qEjvPdAtpbb1JZKa58aIXahU5eKNCjJgn2hr6Zu2gPPqwWglf3Hx5QmmOpWxKpZnlVuqLyguoHgs3OfOLDZx2C6bjAnlOVEiEDDq8397qWsGhNbgLfkWpU4h7ZoywgVZ1ZTuMdd_qz4ZwP0eiwnWwG3IOwT1_fqss3FZzFb1D5ushZ92375v2xiy-dNFmBPwkl7kcBVIcPPE95peRYWZilMF4HbmIzYtNR35_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a015c896ae.mp4?token=CtTB1kKXxsf7xh_Cj7GQY7m0pUNVgEkIxWINnUKbXaNX4ZUVfjnBFCl7wkc-DEut1NMarLqqJzLQ6uLIX3yMS8Cm80k4JeEONtkg1jqf1ziIpxK_qEjvPdAtpbb1JZKa58aIXahU5eKNCjJgn2hr6Zu2gPPqwWglf3Hx5QmmOpWxKpZnlVuqLyguoHgs3OfOLDZx2C6bjAnlOVEiEDDq8397qWsGhNbgLfkWpU4h7ZoywgVZ1ZTuMdd_qz4ZwP0eiwnWwG3IOwT1_fqss3FZzFb1D5ushZ92375v2xiy-dNFmBPwkl7kcBVIcPPE95peRYWZilMF4HbmIzYtNR35_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
ژوزه مورینیو: بعضی از بازیا دقیقه ۱۰ تلویزیون رو خاموش میکنم  و در این مرحله از زندگیم تا ساعت ۳ نصف شب بیدار نمیمونم که بازیای بدرد نخور رو ببینم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/98283" target="_blank">📅 11:00 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98282">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BfO9wEecFZT1TICqOUb3iezoSCExIhrVOFt7uyt4BOFA6JHjWbfHOBHOYaN43_NnhOHtivN6uZofmQNEbCpxtmPEca7IimuA9ONLVxO2ygqYtu2e0BvaKHkPFE7j9OuPK2YqB9psngMCA0LNGdQ97BDSXn9Jw4LI3EiLrUg_AbJufeibpVtQbs55SSgkL8DS3F4VBp1gJDRpH4YbmQ9eHARjeGmYRgvABI7ZJr6YQzTbnjepoTQR9fUXDIvbZYzC20eSEUypmkMFl5pOw4S-RQpA3c22VxjNa6BXzyILPZsA_zOOImd__g9OAoX4fTWxqMPxjPP9uAvWgE9f-2P4uQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚠️
📊
گلر کیپ‌ورد در جام‌جهانی از حیث دریبل موفق از رونالدو کاپیتان پرتغال پیش است!!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/98282" target="_blank">📅 10:40 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98281">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/68476dda6f.mp4?token=qFFFn2f7xS024kCjBXE_IqsloKlebRuDXJAvACef-htIIaAZ3WZtZzyVs3z-eJCiQS6gA_AgwnM0TyvNOv28q07uwJUzCAaXBAlD3X22d0lGtwOciq8n3zvt2wvhUKUhHCAd6qyzFrDHhXUKr3gNGBT-WFjIoSoEle1DPDaf4Y1xwrApAL0KwahLzo86C6vaDhKTUrkW3Y2JXC9E4ynMZMpxWEXNGYUNZMHGjQUoMjcMhutuwjeIfCYKSVAKASWACf_i97kBeKlUNQlbbofG2-L7E4Z03L-ySxRe8G12jG9_WSyvwZN9EmKwxLHLlFVBC5hgjDQe4XPI5TYwEOPR0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/68476dda6f.mp4?token=qFFFn2f7xS024kCjBXE_IqsloKlebRuDXJAvACef-htIIaAZ3WZtZzyVs3z-eJCiQS6gA_AgwnM0TyvNOv28q07uwJUzCAaXBAlD3X22d0lGtwOciq8n3zvt2wvhUKUhHCAd6qyzFrDHhXUKr3gNGBT-WFjIoSoEle1DPDaf4Y1xwrApAL0KwahLzo86C6vaDhKTUrkW3Y2JXC9E4ynMZMpxWEXNGYUNZMHGjQUoMjcMhutuwjeIfCYKSVAKASWACf_i97kBeKlUNQlbbofG2-L7E4Z03L-ySxRe8G12jG9_WSyvwZN9EmKwxLHLlFVBC5hgjDQe4XPI5TYwEOPR0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
🎙
خاطره مهرداد صدیقیان از تماشای بازی لیورپول و چلسی در استادیوم استانبول
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/98281" target="_blank">📅 10:20 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98280">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/597dbbddec.mp4?token=aTnNDf6xwrJHDIIQlaiOYtTuFKuEC-3nsDdtunZNKDd0ILigxRRPy4lHSUsBRfvmoYDCDYSQw2xX8xnxYmW_DPAPeMcZEGza8s8pW8lb_Bf1PwmU_zvZ866abKskpIP4Gzxnu0X-g89rFwFV7exU6rhPdhMCbRH9NYnvt8o9I4Se8ramV3kUS4OLl4uW8eke-T1W64RN2nfWBa62JxfrFZKFUtOnXvRs5l1x-2b5N28jZ4W6jbGSfmMkDnFqCvXYcjZI8MIXWhTXR3NJYaojZA3-0iCAPeU3cWR4F25FlClyzekw32wUTeX7uH_ilkRuKloeZz6aIXc308mOC7YDzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/597dbbddec.mp4?token=aTnNDf6xwrJHDIIQlaiOYtTuFKuEC-3nsDdtunZNKDd0ILigxRRPy4lHSUsBRfvmoYDCDYSQw2xX8xnxYmW_DPAPeMcZEGza8s8pW8lb_Bf1PwmU_zvZ866abKskpIP4Gzxnu0X-g89rFwFV7exU6rhPdhMCbRH9NYnvt8o9I4Se8ramV3kUS4OLl4uW8eke-T1W64RN2nfWBa62JxfrFZKFUtOnXvRs5l1x-2b5N28jZ4W6jbGSfmMkDnFqCvXYcjZI8MIXWhTXR3NJYaojZA3-0iCAPeU3cWR4F25FlClyzekw32wUTeX7uH_ilkRuKloeZz6aIXc308mOC7YDzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇲🇽
گارد ملی مکزیک درحال تامین امنیت هتل محل استقرار بازیکنان انگلیس پیش از بازی امشب
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/98280" target="_blank">📅 10:04 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98279">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/522d669236.mp4?token=aLgZkvza-zmsjdOdi1ZXB0wkLDKa0plazI71F5tMC7B4xusJG_u-6tdbANj-4iGQzA0bxaGX1wwF2EMs7b6GTxFs-0YSQaM7F8DJi-1ppigcJhku0G4SKyN-wMFODN4jtVdLChuOEFyfHcdlkhDlDZzyJVwzMQfgEUF6XJYs3UnMXto-FWiL32P-k6UfWkB_iszj3xh8jw38_iFXbF2kYtL_peHNzHFxC-aaOZmeCzznd41VoWvshS7s2o2SIi_oMxsI8AltuHD1tD5C_aExILzxf28_sIxfavTai4hAi4wBxlXhITQnBg8wazHB3X25lCHASnBo526fV5XIKS44LbgOH2S73rCIa8W9v_fHuIdhu8O4G8EdG3T78LJcELPNXpuD0zmqgNlNuExFw9g1gqtgeRjK2ous0aEF19MICnGfsxVYvFZJfuf-wCO0dn5RL06uIQh3NzuDuADo5RweE10JMGL9NXlpddiUE6Eys2U1YG4A3hdx7LKuFghLrROQsUlNc03Qi0_8CAiZJX20DlZlVVmDzHwDPk09bFp2WJV5W3mq8ENVjapwJe7wQgPLYW0xhG_jd2N_EomzkGanswlowiWykyT6Zn5C8bYKRabELBRO964_T3pHfkQemDnlJc2yZPQ4M6xTQqPbjfc1BpxLZ97o6OPXjv1rV1XqdNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/522d669236.mp4?token=aLgZkvza-zmsjdOdi1ZXB0wkLDKa0plazI71F5tMC7B4xusJG_u-6tdbANj-4iGQzA0bxaGX1wwF2EMs7b6GTxFs-0YSQaM7F8DJi-1ppigcJhku0G4SKyN-wMFODN4jtVdLChuOEFyfHcdlkhDlDZzyJVwzMQfgEUF6XJYs3UnMXto-FWiL32P-k6UfWkB_iszj3xh8jw38_iFXbF2kYtL_peHNzHFxC-aaOZmeCzznd41VoWvshS7s2o2SIi_oMxsI8AltuHD1tD5C_aExILzxf28_sIxfavTai4hAi4wBxlXhITQnBg8wazHB3X25lCHASnBo526fV5XIKS44LbgOH2S73rCIa8W9v_fHuIdhu8O4G8EdG3T78LJcELPNXpuD0zmqgNlNuExFw9g1gqtgeRjK2ous0aEF19MICnGfsxVYvFZJfuf-wCO0dn5RL06uIQh3NzuDuADo5RweE10JMGL9NXlpddiUE6Eys2U1YG4A3hdx7LKuFghLrROQsUlNc03Qi0_8CAiZJX20DlZlVVmDzHwDPk09bFp2WJV5W3mq8ENVjapwJe7wQgPLYW0xhG_jd2N_EomzkGanswlowiWykyT6Zn5C8bYKRabELBRO964_T3pHfkQemDnlJc2yZPQ4M6xTQqPbjfc1BpxLZ97o6OPXjv1rV1XqdNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
غیرضروری‌ترین بحث تاریخ:
خداداد: گزارشتو بکن
خیابانی: توام فوتبالتو بازی کن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/98279" target="_blank">📅 09:43 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98278">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/34e9e6fe8f.mp4?token=Zd7R7X8KBqYYnSdHYi0VpWvbK2W7p-eQtR_7ou--o4Pcz4Jo23zgxJuSbeBWZabROPIGJHFMS-NwB2HxJxL00rf0F7-xkJvpJGddzYb87A562Fefm4DfPObhaOu0V7C28Qxu0Zf3jpzJlGpymDMvfkjXaJwfggAa_AYF81vACaRi6pUfzzZPl1UzAZnvtNCRUklV-QxdKfq0RrDoV6M03_UTFAu11szgMVy0QesMj8Tk6UJ6ilm6UXFKU0lhHvclG8Zkjrstzmfa_73jFDl3RmmpXIaqdsBY0SB-VFmU3kQLKmgp6l9blKmvBY7OcW5FpHQdnO9b1wpKkjXdn_6I0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/34e9e6fe8f.mp4?token=Zd7R7X8KBqYYnSdHYi0VpWvbK2W7p-eQtR_7ou--o4Pcz4Jo23zgxJuSbeBWZabROPIGJHFMS-NwB2HxJxL00rf0F7-xkJvpJGddzYb87A562Fefm4DfPObhaOu0V7C28Qxu0Zf3jpzJlGpymDMvfkjXaJwfggAa_AYF81vACaRi6pUfzzZPl1UzAZnvtNCRUklV-QxdKfq0RrDoV6M03_UTFAu11szgMVy0QesMj8Tk6UJ6ilm6UXFKU0lhHvclG8Zkjrstzmfa_73jFDl3RmmpXIaqdsBY0SB-VFmU3kQLKmgp6l9blKmvBY7OcW5FpHQdnO9b1wpKkjXdn_6I0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صحنه فوق جنجالی از بی‌توجهی کیلیان امباپه به گلر پاراگوئه در پایان بازی دیشب
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/98278" target="_blank">📅 09:40 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98277">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">❌
بازی چرک و کثیف فوق‌العاده زشت پاراگوئه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/98277" target="_blank">📅 09:20 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98276">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/897a264b10.mp4?token=rHLLvOitQFlsqqlGcnhzHmQCEtZS8jlIFMAeA3u8LisWhBzLSYuLNCSCzp6EhZfX3D1TtMmAT49AIh2JZYZBY1CjG5oYCUyGNS1vb_BHhOO_P6mJpiFrDmZeZ9QQns-BnefsaC4fw7zBqMynpKl8CNgWzPNMLIj8EP2uR8V5mvoZb0isU46hoUQbrjXwKYyKViOIvPw4pyL7vDDoE7axwetQm8O3vQiqnNZ4522LBLVJEMvmzldQyD94ySBePq5JkobEHEmoUAFR-zXsmaBUmB3ueZIwrE4GfZp9IEc-2pFcjOlNyyDbAI2-EBm2_SansVNQlYXJAYlr73K942J9Jg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/897a264b10.mp4?token=rHLLvOitQFlsqqlGcnhzHmQCEtZS8jlIFMAeA3u8LisWhBzLSYuLNCSCzp6EhZfX3D1TtMmAT49AIh2JZYZBY1CjG5oYCUyGNS1vb_BHhOO_P6mJpiFrDmZeZ9QQns-BnefsaC4fw7zBqMynpKl8CNgWzPNMLIj8EP2uR8V5mvoZb0isU46hoUQbrjXwKYyKViOIvPw4pyL7vDDoE7axwetQm8O3vQiqnNZ4522LBLVJEMvmzldQyD94ySBePq5JkobEHEmoUAFR-zXsmaBUmB3ueZIwrE4GfZp9IEc-2pFcjOlNyyDbAI2-EBm2_SansVNQlYXJAYlr73K942J9Jg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🙂
در پایانِ مسابقه، امباپه بسیار شاد بود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/Futball180TV/98276" target="_blank">📅 09:04 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98275">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c3b324ff50.mp4?token=kgPvcwMo5HkdoN4oj2pJOhZs89IWwxZjik_fCGdkzxckjWlh2RMF_O6o1aIBYR3HO70M8jmbsIJUkFRVQU5fYD7fzzZwAghc7WDga4FrJE54aja6kimljJ1WHZqD6D6AFGmYz43fU-Nd6KDP6IaZdmk71uiToKrTOs9ZVBMRQISlD1ycj1DznJN0M3jQkmOYF9btnHx31er4OdYSPeHKCzmdXhGmdMx8Cq1ys_2KbReA1YDZHnDu1XQLIufG-UeE2Y7J-uhXFbxqq6QlzjgO7fdKy80Z5Jm5SEerQ0xRZUJw-V4AFKdJ5BQcvVHvNklLM3IopIUFsOWaw0z1-NniBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c3b324ff50.mp4?token=kgPvcwMo5HkdoN4oj2pJOhZs89IWwxZjik_fCGdkzxckjWlh2RMF_O6o1aIBYR3HO70M8jmbsIJUkFRVQU5fYD7fzzZwAghc7WDga4FrJE54aja6kimljJ1WHZqD6D6AFGmYz43fU-Nd6KDP6IaZdmk71uiToKrTOs9ZVBMRQISlD1ycj1DznJN0M3jQkmOYF9btnHx31er4OdYSPeHKCzmdXhGmdMx8Cq1ys_2KbReA1YDZHnDu1XQLIufG-UeE2Y7J-uhXFbxqq6QlzjgO7fdKy80Z5Jm5SEerQ0xRZUJw-V4AFKdJ5BQcvVHvNklLM3IopIUFsOWaw0z1-NniBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تنها استفاده من از خونه خالی:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/Futball180TV/98275" target="_blank">📅 06:57 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98273">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aRCDxs5jjiXtko0q9SXbsdq31O6kOKQwgXq4DmtptIxh_5ZedbuARIhGJFWlRhV0haSo-ojQ5YcQe0CVqOVmSal-56nUdSEGCLJ_19za7S7U-ho5yW4wlAy_XYt8McGw1GyhWJRyPUN92X6lKr98sms8OEZ-kfusLxnMS6FFh5pYg83HCnlMF2TkKI7wSEZqsYhM5WmVxh9Di-y2xhvPZHudF9inNNiruksLWkZsoiOQ9Edkc4qoBprA_HWQkey04IreomPRm60moi0fDDVBvpFCBJzMkuo8Lv5lqivCu0ga_morlVSTVLsuZPL91IyYofgXYd4rCkbe8SjNyfiqCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JAFQPryxVkkaV9tTigZeBHDOfqUGuNqnZj0lHDdPGxN8USorCSgyyJCiQhz9YoksxmgRzdRcF6XqcF0mUQZpt7L7k9aTCoUYBtgKW2WtNOH8h6NgbwQyJW5iFXbHTNw94yetreKa_xtwG8eWvo3w-ePFnsV0p2gUNkaLa8QqBmivPeWtmP61WVjif2T7j5VoovF7W71v8HwR_TQpSEt9Oeky-cannno4q7F6KHeU9ZMsMLYFGlRZvdS-Pqi1gLiW59nQKYqh_TbG2VU2e7Z_kjEA5wrbRgKmUREudGw7moRKcs9fVQymvm7zgvK4Y-ATYApBQNw6ha2ws6tTVbi55g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎙
👀
پشماتون بریزه که مهرداد صدیقیان رو دختر مایکل اوون بازیکن سابق لیورپول کراش زده بوده و با مخ کردنش کیت امضا شده باباشو ازش گرفته:)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/Futball180TV/98273" target="_blank">📅 05:04 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98272">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb9f230059.mp4?token=LE-v4BxHSgZChjOsbKz-8rdU0X3ZX5tvH0lQFOEub51PEaNx1hw5rcilP1a0XVBMYFM3-wnXxVVGhSBkURHvhF6C7Nynt7LuPKs14n5BSjDHH6kh24XJaIfDiKfGT49yicnFgOlBVLlHLSOWqr6Oxa_Ebomf3GtOWrWE-vJEQDIHvd4S8DnEK5rdGI1XKVkdR9ZXrRPF1mWEGgkRW4iDZA2NgSd2BmGJdSfWY3aJy2r55nYp0X-D5Hn5sUgY42VcF92e5zl9C-nr4jfN6UYltCOytQt9XwS_AeJrf7Tv2RlEkz7BU13QSXcWHkTAnxwdWC41V1SXR384n7nWwlFtBE90w4mcrN_x4pzlTpG1RtewuQ20nvltLYYuUh7Af8oUlRh8Dh2hDHB7UpPTAT5XcIBr_4llIT2NNM50rJwYkxQYaN3-5MiX0XIicUqM_vifi-duhL_nrOHIGQ-vmMHH_gqUysF3mNWSTk6qjppeeLmEf4qUf1LTtUpzL-uGNplJaF6ccbAyO1YiDXd7naPkMdIavBR2Vx1rZihXUwO28P2Mkjxijbc-DRggsIGPlg1eza62ctD_SDWeTnOS_HDFkuR-YoMY-I8eT5-PWel9gAimbqI4F4nIsxeyJA8WoF8_8PlrgJRefZFYhvA_1jWr3exoRoOzfbD3n3Hye1Ux7Aw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb9f230059.mp4?token=LE-v4BxHSgZChjOsbKz-8rdU0X3ZX5tvH0lQFOEub51PEaNx1hw5rcilP1a0XVBMYFM3-wnXxVVGhSBkURHvhF6C7Nynt7LuPKs14n5BSjDHH6kh24XJaIfDiKfGT49yicnFgOlBVLlHLSOWqr6Oxa_Ebomf3GtOWrWE-vJEQDIHvd4S8DnEK5rdGI1XKVkdR9ZXrRPF1mWEGgkRW4iDZA2NgSd2BmGJdSfWY3aJy2r55nYp0X-D5Hn5sUgY42VcF92e5zl9C-nr4jfN6UYltCOytQt9XwS_AeJrf7Tv2RlEkz7BU13QSXcWHkTAnxwdWC41V1SXR384n7nWwlFtBE90w4mcrN_x4pzlTpG1RtewuQ20nvltLYYuUh7Af8oUlRh8Dh2hDHB7UpPTAT5XcIBr_4llIT2NNM50rJwYkxQYaN3-5MiX0XIicUqM_vifi-duhL_nrOHIGQ-vmMHH_gqUysF3mNWSTk6qjppeeLmEf4qUf1LTtUpzL-uGNplJaF6ccbAyO1YiDXd7naPkMdIavBR2Vx1rZihXUwO28P2Mkjxijbc-DRggsIGPlg1eza62ctD_SDWeTnOS_HDFkuR-YoMY-I8eT5-PWel9gAimbqI4F4nIsxeyJA8WoF8_8PlrgJRefZFYhvA_1jWr3exoRoOzfbD3n3Hye1Ux7Aw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
👀
پشماتون بریزه که مهرداد صدیقیان رو دختر مایکل اوون بازیکن سابق لیورپول کراش زده بوده و با مخ کردنش کیت امضا شده باباشو ازش گرفته:)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/Futball180TV/98272" target="_blank">📅 04:59 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98271">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/efwdKA5DsSxMOFPuA3uA3_zyp_Hi9dRQpuXnVABTWZgRbQcK_nQr3lk4glQcRfAgYocrxQ1gtWQvMeC6MR5BZEuyqDsy0BDVkqm_GUnaRxe0gKt6L4jcCxlwsYx3zCJO-cHIcIUCqwQaVCoELnbMhfJHBgt_Q8va6wMRbUTkb-C8212KHwnRNk-ReqaeZuUKx8oeqSLDzJMAdwIzCPYSeXYTi9BidLosBY5Ur2BwdZeCqUL2WlOU-w8RSakJSXkt4L3r3d_h4K0KVjh5gDaB_i9udhH9iIX7jPazkYkzBs1X-dd_NOZP1ptw2XYHdGVspIUGcqfbuF-SO-4jimdteg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔺
از سال 2018، کیلیان امباپه با 11 گل بیشتر از تیم‌های زیر در مرحله حذفی جام‌جهانی گلزنی کرده است:
🇧🇷
برزیل (10 گل)
🏴󠁧󠁢󠁥󠁮󠁧󠁿
انگلیس (10 گل)
🇵🇹
پرتغال (9 گل)
🇪🇸
اسپانیا (4 گل)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/Futball180TV/98271" target="_blank">📅 04:17 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98270">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nrP0KP8bI5XfS_CyCMe5nK-sq1yYZCdg34bSqlaJpKAuJzTfdbLGPmbyIoHDX4DVZ6Iy41G_Bh_dtKKXUa174wCJtGHXLxHqj6Abvx2FnAv5R-J5SDFqkBcrrUtOiy3T1a818fm5fLnNgbSG9sMGuklj-Hjc5vmJEeUGjXFsUa5e15J0G1zJhMRthCg7e87BgEWwsJh-Km6zhvVwQzmSGT61yiJkA4QXp4SOtnZQwk6KpnKjPZy1t1kWorzgPumRRmcA7kCO2VHZZgk_HdQu2XCYAPr9NRAX67x_k2afRgpXdFKwdciYc_R3xuYdcD3Df-gmhlsYjRsEQ0cfzRzKMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
زلاتان: اگه من امشب بازی می‌کردم، ۴-۵ تا کارت قرمز می‌گرفتم. فرانسه خیلی خونسرد بود، آروم موندن و حتی بهشون لبخند زدن. بهترین واکنش همینه که وارد بازی روانی اونا نشی.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/Futball180TV/98270" target="_blank">📅 03:33 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98269">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b2b1ac9904.mp4?token=N7akzHYnQ8HpiGLI5gvkJrIB-ex8izeAgkxYJoEH-r0r0txAHSbuL8pDcujSwFfr6aOBTnd0kRHCdB5vTLbsYuNvRCJCB8AvTMCaf3WKmYcetB38sKAPSTG6sAc4BrhJc30Dw_iMqhmE4SMDKa2qN8ngnrPcTheRY6kblFtEadlafQzWs22ipsUOw_oGs1iO7hlR9jwvzgU3zWpZpteIwV5WMr4Y1R0fG80XTxOLRVFZst3eTXEwMlpZT0pAXxB7oR0xS46KlegDKusHJzPuOBNjn8HS1MlJ2y7YrMYPN6CzLuLdn01FAhqcwwpDzAwT0c65N45ovuXlpfVGMyjFfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b2b1ac9904.mp4?token=N7akzHYnQ8HpiGLI5gvkJrIB-ex8izeAgkxYJoEH-r0r0txAHSbuL8pDcujSwFfr6aOBTnd0kRHCdB5vTLbsYuNvRCJCB8AvTMCaf3WKmYcetB38sKAPSTG6sAc4BrhJc30Dw_iMqhmE4SMDKa2qN8ngnrPcTheRY6kblFtEadlafQzWs22ipsUOw_oGs1iO7hlR9jwvzgU3zWpZpteIwV5WMr4Y1R0fG80XTxOLRVFZst3eTXEwMlpZT0pAXxB7oR0xS46KlegDKusHJzPuOBNjn8HS1MlJ2y7YrMYPN6CzLuLdn01FAhqcwwpDzAwT0c65N45ovuXlpfVGMyjFfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قشنگ ترین صحنه بازی همینجا بود
😂
😂
بازیکنای پاراگوئه با تنه زدن و فحش دادن همه کاری کردن تا امباپه رو فشاری کنن ولی دیکتاتور با خنده‌هاش بازیکنای پاراگوئه‌ رو حسابی فشاری کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/Futball180TV/98269" target="_blank">📅 03:31 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98268">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T1wbEydqJJ3J3ChwWlMAA8o5H8lrwE5lCCwOAgWETRKmIr23tgmGReVaFltGDuDTZkZ-AOIXFtARAnhIJ6TJZuiUMIdAQW9pJoPprUnFzEXYNerx9SDiWRJBoUMeWjMu6wx6iYxhVpIwJshi-u4HbKhgTnhL_m6unMduFHQFTdSGhlqURUtHrup6LGWOsHctjFTC-lzLQmRTPoZT_MP_ALvc3wXI1598Qs2gC5xRQ8lIGMObUVqS7mb-9Ti5NJGpHiPC8KoBCmJ56obbuX21O-QZUIZw4FSj-Acl9rpMouL4v2LmrTHe1Bes4PpIqG8uDOgzaBN3C2MjyYhp5usgzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرنگار :" کیلیان امباپه گفت اگه لازم باشه دستامونو کثیف میکنیم. نظر تو چیه؟"
رایان چرکی :" دستامونو کثیف میکنیم؟ ما لازم باشه تو خود گوه شیرجه میزنیم"
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/Futball180TV/98268" target="_blank">📅 03:04 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98267">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KUQgbwUbB6_83TDEUElC3k450HHRppv56eWYxi6yWz0VaEu0pI0Hd8Smvh03jcGhMkNwgIipwlqUwGSKb97pQooakAn-tKFl_T-gAOwBco_IKhXCJTQe5oAylbnB3PlPTD1BQ4YruhfmIOo-hBt-syuTxXyKQruDaqYH9GkCN2OTXrCn-Vh0rRY9k5-0SQlBIJ2amk1RDJgVP4LFLZ4pABr__RLpyoI0Qnwgu-mKpPoya-VisFJrdwntxCHGRn3y5UjpT1OKxbiW_APMjfDsCENTpjBFOys0FxmaFJ7lqbI6Pcukw0CAd9FSJqNihPcsFldBwDxvfPPY26Pn6kaubA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
کیلیان امباپه : ماهم بلدیم مث خودشون کثیف بازی کنیم. ما نشون دادیم تیمی نیستیم که فقط برای هجومی بازی کردن به زمین بیایم.
🔺
اونا فک کردن ما میایم با لباس مهمونی بازی کنیم اما ما هم بلدیم کثیف بازی کنیم. حتی تو کثیف بازی کردنم ما بهتریم. فک کردن میتونن مارو غافلگیر کنن ولی ما غافلگیرشون کردیم.
🔺
اگه اونا بهمون بگن برو به جهنم ماهم به اونا میگیم برو به جهنم. اونا نمیخواستن فوتبال بازی کنن.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/Futball180TV/98267" target="_blank">📅 03:00 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98266">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VIA_X5Pb3Hll4BPS9yBquyeKixhZXZkgGjxJ7qd-HtwbPwqPpuhiocZX9xMsyQgPdJ83bPbBRJMonvFLpDxGzNCfarTPFKVJtaugdvQF_t-CfcNeef3d_cFvzn5UlDHJhUFJIvfPAymrhCELZiz-Q_qfSApF094CJu-mihG5LQzAS3GpgQxaHNzshTKcFPDITH_yvueHwn-rL9tAqwuoh1ZhkNFM0t1ZmlGp7jTgqFkniDRrTiOYPJJEM4XchSnic69st_1nolUynMvnC_UQfswnAuXDPswk1oNbHsSOkS2nSLBLUYHqSLX2z9k4RdbjG5Uf5TC6Bb3DtDasUYoiIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه تحقیقی هم در مورد این آقای تانتاشف باید بکنن تو این بازی. هیچکدوم از کرم‌ریختنای پاراگوئه‌ای‌ها رو ندید
😂
چندتا خطای خطرناک ازشون نگرفت و در عین ناباوری یه دونه کارت نداد بهشون و سه تا کارت داد به فرانسه. خیلی عجیب قضاوت کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/Futball180TV/98266" target="_blank">📅 02:58 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98265">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z2KLyuThRYnNqoUwjenJBOclYzA3NAlfkpyO0BemSegRDgNazJhEkhiVUjLjKsuhkUEG4I_rCbY7gwGO68jF5T7-0VHouelgjgEjP8NbEv_zw9wDXq76_bCNKbenYoC9OT8LylLNd2Tw6zwXadC1lFtD697WbplPg5wH6G4vUU7N1GHaSzYUhErb4krBGwyGcOpAS22kEoZWxZa2vXMyt39zKUqJ5T-Y1VfhWyxfIbdT1b4ekkjwLv2KT8iEcFYK2nMKxH0O3SfiyFONsmjpS9Yi9RR4N8gUOU7NJHlBLCKuMau6V-lGbG3ESBL8cHaPjvMBIp08c_9vMwaqOkj2Qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امباپه خطاب به یه بازیکن پاراگوئه تو بازی امشب: مادرت خرابه
🤣
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/Futball180TV/98265" target="_blank">📅 02:54 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98264">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZBiKEu8PHllL7zOPfpRWVnzuhuhI-m5_0uTqNxckwfaiuICBjDxDE7c7A0SC0o22VtgV5HSL_QuMXtqlZtl5aGtp2UGWOF2aUr6vzR-M01Cvund3_0gUYw_by-FXh_6iozBjZfe6_IcxxUMOZcwX6OFAEpOFgeLNecFvxEooA4BfG-ZslqO1flGAt4GKKESVlKpcLRFTEjUOmM7PtmOG01q-_eMZVRCVAifhiv0eHEHiZCqV-i6RjYJjESkWVhry4fb_FLZeXkqRTfU2392mCfZSxfrHS4AsRwkYvXTgj71CEhkTqA_l8jJEczY2e82Iqham_shnundZKVmA6_E83w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
📊
|| عملکرد پشم‌ریزون کیلیان امباپه در جام جهانی:
🏟️
19 بازی
⚽️
19 گل
🪄
4 پاس گل
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/Futball180TV/98264" target="_blank">📅 02:50 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98263">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VxTLRXRVArKWiN0mtN2XsDrRmqRvIadihgDyiumINFVQInUZwLlrDqouzUgMBkeODVx2PWeV75f1Nn8_0zaUvs4tEFh-tAu-Uuy8xaoQfShCQetM2K0c2Wy8ii5PVClnf4qpEK6AbP8Eo4GVSTh1JqOv9q_XfxBecJUXrcfDp77XiUQRFKtIzrjdetjAwJOsg4VwcnzwoDp0meX2maOJGigl-BSI734wcvNbNEcDWHSuFGEjQ3L2ya_330qTSnbKJXMuHaCJXVTsy0v-leqMqGSg5hc2K8Vs1qlnlu5D1q8JPxTVvRMRpJ2jwPkEEN5V3SnGE5C_VLs71gMa_mhTDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‏
🇫🇷
|
کیلیان امباپه به همراه مسی، رکورددار بیشترین مشارکت در گلزنی در مرحله حذفی جام جهانی شد.
🤩
لیونل مسی - 12 مشارکت در گلزنی
‏
🇫🇷
کیلیان امباپه - 12 مشارکت در کلزنی
🇧🇷
پله - 11 مشارکت در گلزنی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/Futball180TV/98263" target="_blank">📅 02:47 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98262">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SDATdFfoK4bUHhB1CMnwXK4NCmphtiP8VNZcnuLuMjcpuXs3eNi8PV4O3FwdcIrSbZe2VeE4RPRs42H0smVxYdGjKh3VBaMic-vhprGGxKfwlucVe-k0Iktj5hyN2akULUId8mUCgZfZHnKuRrbTyrH49EDlRnjyiPt3nYh70QuVsOMDZCTj5H0Z2Yi0x518MY8j7F6Lq-yfCNaolKMDYJuXxkq0kPqTCG6Cq2KPh_WiQcktvd11VOambA_kVQiBdYOzx2RQKwNMDsHWgp5pLqbSfe1QuLX1rgBCQbBgc4ds44I7asBbsdTtT3OcRH150ZOYOQhrG5U7V0PgEUmTLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اورلاندو خیل، گلر پاراگوئه با ثبت 4 سیو مقابل فرانسه به عنوان بهترین بازیکن زمین انتخاب شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/Futball180TV/98262" target="_blank">📅 02:46 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98261">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bP2PzxJE6NY42U1ocHU8T1bjS8eBc96OdyZgVwSVsM5_MjYcKlVl-gGFkdy-iZuYUciXtx6onojYcy7FR5BR_XTjN-6EkRcIkr2zPXSgZp2H1Jxm4xgQVNK79RKQTRLY-YSVxmdj-LPP1f6AICvhcGZDQaWO559-y6ZPYCDwQt86E4fyqLFopTqTCUmWdaz-ad8U1nlkptDLTs5XiS0e02kbvg7NqZURJPfE1C6Kf5wgpsUu95_tx39DWTYHmBQFc6m98G1xZirHXfUF8lIhl_eRh60XTAUuBxkXIc5BeRhOCIT4RvCYSxv-j2E_E9fCKhC6uTc61nNqtea8soGKuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گلر پاراگوئه اومد به امباپه دست بده امباپه دست نداد
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/Futball180TV/98261" target="_blank">📅 02:42 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98260">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/Futball180TV/98260" target="_blank">📅 02:42 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98259">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/PX5D2eNDu3JUsshuhQ6qG2S0Hm0w4XXYICebi9CQLYgtCZBn32q-_try4yKloIhBg_hZzoFU6JD_dLips-UOXPIsLUUyLqNbliMW5-fKOnXpkLTz_Zj8kUso8NJ8dQPvkUC4zerGB7sIVR36syjegcDnzBPbHoMCmkNbFc7bdXH91FQPd-OWrrp8d--ZNMrcYtSVTCXWulbZt3WAURtHc5d_9cBNxrg3cmQ990h1drtTJQ_3hQH9ADP42bwSwznS-SYA4YFGCW8IJakqDJ5UE0Klm0Ej4ckVdeFrer30b8HB-VWKFOu9ehNwSLPjbhp4I8A4J_VHQfPjN9TRG72BeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet
@FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/Futball180TV/98259" target="_blank">📅 02:42 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98257">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qcQxZ0p4L3rW8nCSnRCwBoJ0gz-cuR3WnRhgTsOu3WdzqRGO0g2r8dERoBRBta_cZpA_4Tc-Y_rfI56lBDivj6J1UujnkndH7ZyUCimR9pg-abOidzhKwzYThRUHAbEDSnvnHoGofRtsnOkWTYObDD53XMBfeuSHITCsVVadRqfkGbsxeyFTKTZls2U2GIp3X_mcJojM354RZxsCELqCPL4Nzf58gWhg1TdHa6lGcx2VWHWQzb663_gR_KqomTVoJ_U_qvcIHjubhYKv5alKe-uh6C1ZI9ZkcRFifsxDvN_de3fYdbSgREeDYS4GEl--3TfgtiZWEnf4ADedxk0iSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UwnS_yr0tTWQwrZWn4F7ZpooAqZMgHjlf1HMULYoAAAlLPTYzHoNlN6kO4C6huaeKUYdnSzMndK_A8fewmv9YXz3ODr7u_GqaXDpd4POkQPzTAp6mt6Rp6eTqta-rO32H1YvFcrjCjaYl-bBxj76SUJIEm48csBQQwSSVaYZ0wXP7lnDnlsF7AbAMe5DvNSqzCL6OPoPF_cL1cXUnDYrQaeckWD60rqRqaClplvcFra8CkY3qwJilaJmCXctr1bxj-4qaZGlmqTBN6Xi0kjC9mO2uh9jBYTVf7tJGIqoIVcqJ4tw0Jbue6NowSUKw8T0KeCIig_JCPfyTAGsf7xv3Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">وضعیت رایان چرکی بعد بازی
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/Futball180TV/98257" target="_blank">📅 02:40 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98256">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lKg6lEoMEXiXjd2rp_oliuFt8PyoMXCD6yA_Km3GExPnNU5HntOtbhNIIsFBeyPPLPhvadX5HAGRsEq1zTBVgodc_3kbTR346D5B5oadeDsS6In3cAoUtAfeF2DlmIUR2n_m-j9T1JDVedG1AG6Poso391yo_ieobtd3kA8vXdw4Z01fE0TcEit-mcqZeeaFuXdDjSq3NIXJWuYWboJtJsXCd2vCsWdvLLrYAREEHujOpIKbSbNPZAVNEcwk84A-_4z_yZbxbbgLXoRxqEfbmFsCe3u1SAb8GhIv5U2iKtEx_EbKbx-WyjdG6XUj3-VnToAbIoQKdRELOKnjItRTlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
🏆
آپدیت نمودار مراحل حذفی جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/Futball180TV/98256" target="_blank">📅 02:39 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98255">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XFKfZmp3U50RXITh7KP46uourlmoe68kL9dspzgUswiJoy7FI1LiEwXk3kBHAqk116TWMkiCay0JOJWehuUdgc6aEi1sOtZzBSgBQnfrKGjIHelL8VN_yrAJNgqxJBp81L6Svma8aWsxWwasAm6xcY0DvzvMvr2Q4iQOC1LFrS3GmrbVGreUf2-VKdxdqQ3b8qAX1XlEU_2REsLl1CgDjgQgZj5W7sX07mM2RZ3PPH4eMr8PGEaGyyB17-ewe5IoZOgmag04oMY75FXlLcc8BYeO16FQnzfpKbJQgQMdZWPYqNNAPrRZhMMUURFOW91_w2KFOhBgEhJybJDrd0711w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
مرحله یک چهارم نهایی جام جهانی
🇫🇷
فرانسه - مراکش
🇲🇦
📆
پنجشنبه 18 تیر ساعت 23:30
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/Futball180TV/98255" target="_blank">📅 02:38 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98254">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h_O9lBFcc-pUrH7035w92qiEZtKSl_MK10EgM1PccnFpbmzG08iQxlFY92YIG7c7fj9N9mU-AjzD8eSVuu1cTv_2Od4wXB9a8JJIUiPEUsmFQZ-jW0wAzgwm7Cs0FbTpd8YFt0bX5hdIe7lZnIPNNgtDNax8g-bpssyF7E9rJg20NQ5owcTStMZdyFIeqQtifoaRGwOYr7NPRY8zuJoJnRSKny4VY1UIKmasV1gf_O5heFK8qWlyRtLV5kpxiwZkDyH2RF4Q3qzuwa5J2vzhuwRBqp5d2dxjb4amiOssiQ_cK1wZpJKFi9HvX7lxO9nX4vmGF2QlJXhVbJKWEGF0qA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
پایان بازی | صعود دشوار خروس‌ها با تک گل دیکتاتور
🇫🇷
فرانسه
1️⃣
-
0️⃣
پاراگوئه
🇵🇾
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/Futball180TV/98254" target="_blank">📅 02:38 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98253">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sFbDDx2vKT2NfF51Ddul0fCH7SPyia356kBP-t743TP4e8Lp04RzbphbXpGkE0v6jtg4jZmIpo7K2RvFm3pUNGcV2H5Su3WaB4SJCYmrgWYTW2pVygQ-LffHssN2SIyphKBSNB5mo4k8WaCLx69-H5SVu03toRnjXh7F561y2MfGrkBnK7F8i5zU5su9FhigCT7BkyTixAGUPkVn4ijj__6JavJ8u1nDFrFW7JpXoqTFB0Cy_5mOMzJmmD3hXsAWc5uWpMmPatPh2Bm-dZUKzilUO23H1PyLKgoKL8lF3HJCbzt0gD-AyWjO7uIqvnMLuiUHIgC8T5B2pitAsgn1Iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امباپه قشنگ با خنده‌هاش دفاع‌های پاراگوئه رو فشاری میکنه
😂
😂</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/Futball180TV/98253" target="_blank">📅 02:35 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98252">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">امباپه قشنگ با خنده‌هاش دفاع‌های پاراگوئه رو فشاری میکنه
😂
😂</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/Futball180TV/98252" target="_blank">📅 02:34 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98251">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/26acefe7a4.mp4?token=IfFB-Ap0zlpUmTJKOg9cFP2oSM1xjz8zYRz3zNsMRm-RV7bF4kebPhkMxvWgTyGYHnBcR1cji3740XnpiXaNTGwymh20XaXpmvxvRVtGejdsyVTORm2KaTCDxn0vrZxecwKzgqoXcK2myiSil3cmvsHVgr-ujXsEcO3X1p89lPOMu0dY7bWZ_f_HZ0FYqZZ8QR9j-PBx1_ebfKLIbvxhvQw6ISuk9VkX9MnV5dSpuSTghPM3KvL_D-ke9hkriprFu3rfVEUnfOh5SeAJKvPoFM18Zv2wFXhPK1psde2G74-xwnTlpRHBc19y1vNlNFOYRSCT-_KfN6p7ZE2qXdfx4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/26acefe7a4.mp4?token=IfFB-Ap0zlpUmTJKOg9cFP2oSM1xjz8zYRz3zNsMRm-RV7bF4kebPhkMxvWgTyGYHnBcR1cji3740XnpiXaNTGwymh20XaXpmvxvRVtGejdsyVTORm2KaTCDxn0vrZxecwKzgqoXcK2myiSil3cmvsHVgr-ujXsEcO3X1p89lPOMu0dY7bWZ_f_HZ0FYqZZ8QR9j-PBx1_ebfKLIbvxhvQw6ISuk9VkX9MnV5dSpuSTghPM3KvL_D-ke9hkriprFu3rfVEUnfOh5SeAJKvPoFM18Zv2wFXhPK1psde2G74-xwnTlpRHBc19y1vNlNFOYRSCT-_KfN6p7ZE2qXdfx4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
🇦🇷
تشکر خبرنگار آرژانتینی از لیونل مسی: "تو پناهگاه و دلیل شادی میلیون‌ها بچه بودی؛ از همون روزی که به دنیا اومدن، تا اون پیرمردی که داره از این دنیا میره.
🔺
بگذریم... این دستبند رو آوردم تا تو تمام کارها و مسیر زندگیت حافظ و نگهدارت باشه. برای خودت و خانواده‌ت آرزوی سلامتی فراوان دارم و از طرف همه مردم آرژانتین ازت ممنونم."
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/Futball180TV/98251" target="_blank">📅 02:32 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98250">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">اوه اوه ده دقیقه وقت اضافه گرفت‌</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/98250" target="_blank">📅 02:25 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98249">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HJpANK-LJclw1xliaGxDotT1k6JJGChDBYSU_p5kDiRjCYK7UAbsQRFj3lEUMNVityZ8z5CLpecagfAl8nWbrs-jplF3icy82-LynLby9kPpGvgmC8hRQiC8s6XfwRIPCZI7WAMjzYJ3cwLsC-855hXEL7n_n8UJlkoAE02frSn9F1H25I9PUKL3gvSnv9SQY9uYh-VyqigsnvQZE3PKLp_WDm0EXAcobtvd1rScm44uYSIumedg6eBXBP9PJ1juJyzASc3MBKiKgWAIvXFNUyYqrPtxBpRf3IaKV5SPAsU35BMoCl7UIbBb2AgfdU7LrDTzJFAIm2VeXSn3hZ6BOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امباپه به آمار 19 گل زده تو جام‌جهانی رسید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/Futball180TV/98249" target="_blank">📅 02:07 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98248">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/8668e7ec94.mp4?token=fymwZ7AhfZnm8sAZMKxLSUbsmeloSk_ftqq2oHFNYqCaRUysc-uK93MNsB58_NdO4FnMZoHyJxr9AQszgY9CTTKm0EKqaHRt2nxTMjM7cK2jLFlWOGh_TNwbx2Pwp7BqapX-09a49KUJ7ke3AbTuPPqqCCSXT2ZJY0W5cacThYD9n2j23mNS92KrA4s_-6GT1crhaLdv9RGQTUV_lb85HM39MJdLYRgvPX7DISuZLeaIvJ8QjZhKDr9iIqRf-9cNKus0kVP1QWhze3Fs9BRqlVWiHS3EGCM2ic-anyHb5OZjdzaq2Z37ojlbg1bo4v8TXkvYfMc2E0XhprjW8KtprQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/8668e7ec94.mp4?token=fymwZ7AhfZnm8sAZMKxLSUbsmeloSk_ftqq2oHFNYqCaRUysc-uK93MNsB58_NdO4FnMZoHyJxr9AQszgY9CTTKm0EKqaHRt2nxTMjM7cK2jLFlWOGh_TNwbx2Pwp7BqapX-09a49KUJ7ke3AbTuPPqqCCSXT2ZJY0W5cacThYD9n2j23mNS92KrA4s_-6GT1crhaLdv9RGQTUV_lb85HM39MJdLYRgvPX7DISuZLeaIvJ8QjZhKDr9iIqRf-9cNKus0kVP1QWhze3Fs9BRqlVWiHS3EGCM2ic-anyHb5OZjdzaq2Z37ojlbg1bo4v8TXkvYfMc2E0XhprjW8KtprQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل اول فرانسه به پاراگوئه توسط امباپه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/Futball180TV/98248" target="_blank">📅 02:04 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98247">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">پنالتی برای فرانسه</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/Futball180TV/98247" target="_blank">📅 02:03 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98246">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">پنالتی برای فرانسه</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/Futball180TV/98246" target="_blank">📅 02:01 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98245">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">صحنه مشکوک به پنالتی برای فرانسه</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/Futball180TV/98245" target="_blank">📅 02:00 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98244">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">پشمام چی گرفت گلر پاراگوئه</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/Futball180TV/98244" target="_blank">📅 01:48 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98243">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🇫🇷
🏆
🇵🇾
بریم سراغ نیمه‌دوم بازی</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/Futball180TV/98243" target="_blank">📅 01:38 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98241">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/mTRRgk2jH0efk7GncaC1xZd_fucMANBiFvsSeEWflQwY9B4JqJFUrez8wsimOSi4cAP4yYd10xntIK0WrqOpURJ53wAwJZ_KvPHuE7uX8gAWEc-UVpHq98hlACtUhjtOsXu0nqzJ0xbKFAg5GeGeuWpypwUq681DeR0dgdzLGbD25mBf5gdaKdE4-iWyy6DoyeOeLCuVIWtyaaAQPPOGxA8XSns0WBuN83Po5Iyw_vLdgQgllXB5SijrsTqjAPNY8aFmbcdLyQ_OO30HHxmMJudPQ6TWaFsB9iKQx-r5cz_8Mmw3IVVSvVHMO-On9WXarddUoDJap4cphdU9fnIAYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/f5OyJrVRUgYJC_63Mqgtn57ZOBsvbmQNeQS-WkxahuV5Wz7I4VIEjmUiRLQVoUQectoPtWlJdhMgBnEKhHXbC9cOYaP-tGBYQRydlRW1l45EHTsr8vtMU4UcXeG8c729E3Urz9c4KzGU_cs6jv7WvSNfZR9sLj5NyBuBNOG0KZrbpSsoRGz7uK7XrHgNWLt6xdpY46N80pdlTYdPBpxTh_k9aJSEHEUNFmq1XWiFmzT_FlPeNjKb1pFj_KhhBTBukLV3g-vqsKMs3jjHnAhtNe9fq0s3WWG0T1HO8wK3iYUVDqWXQQFmTsHgmoaAIXuRVDQbX36zlEjDkvuJqdt_0g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇺🇸
مراسم سالگرد استقلال کشور آمریکا که در بازی امشب پاراگوئه و فرانسه برگزار شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/Futball180TV/98241" target="_blank">📅 01:30 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98240">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QrIDAtCd6Si9RakYFBQLI9xSy14CerNqj7pQQzbMyshVNZI6Y6lUZD7BtvmMZ38jJRgD2ceUwIRCV8C1G--TEqz5vOapDqaax0b1Dpn6NJN9sSPGHNGuENBUuVxIBDmrs921cjvs9zQN4ckWDuqMT35feTsK7zoQy-TgXLsVhUjH0fmM9DK2sCzcI3B7Qye2ZwG11KkcCWB1IH1jt4KpM06ZJ6opodUI0g6LsBEPyPg2tK7exG7-R5L-p_1Un-SHqC0NDb8_OciDe9obwArCuNyFHxgIsp4iahzhhuJpLUh1JwVjcASVwy-H8_TUIfE1hhkIxWfw7McmtZkICmMF_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
حرام‌بال پاراگوئه از XG بازی مشخصه.
🇵🇾
: 0.05.
🇫🇷
: 0.15.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/Futball180TV/98240" target="_blank">📅 01:27 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98239">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">پایان نیمه‌اول؛
🇫🇷
فرانسه
😏
😏
پاراگوئه
🇵🇾</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/Futball180TV/98239" target="_blank">📅 01:23 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98238">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">پایان نیمه‌اول؛
🇫🇷
فرانسه
😏
😏
پاراگوئه
🇵🇾</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/Futball180TV/98238" target="_blank">📅 01:22 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98237">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/la4M7ws8IhKec7bkdi3WYibrYkzyOYo4ixsS0T9dPmQRcIZOVBngf__l8reiidhz6KZmW5it4-4AsiHr1U_ae_uMj5P12QEUr4AWhri4OEgSSFE33l_P9HHG81BJoG4ol9rXLbZGVwwJbVD2zFkHVvPSV4YtdfX1w8yV4meuPvcnspr843P_zfHeuPIFGRTjP7KPXa64X2taaCDNjEa3puREHHY4b3-TwydlXhy7eOrMDDPEccjzy82ePfqKsy3Jn-rd98zC-6HMJOzERaWEOTdL9C4HyeP5KPGfaDshJLInr71AV7XDglGxoGIpCrrh0mbo7EYHc549k6m4Hk8p7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">درگیری دیکتاتور با بازیکنای پاراگوئه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/Futball180TV/98237" target="_blank">📅 01:10 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98236">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N789aSamK-7GN0y0suaBgINOUqcyZau_csmlYpWeaJbhL-iEKA_jWT7nZbrQOSsl0RrEcrNBrH63j4Ujzwszdwk1__bfUQzRGfQ8tyXwFd4phTdFeq1YtJhuY3qy7DnHNMyXXNOu03tX2sSQEwpJSycdgQ_VZGenG3p08GrXAY_Ov3EKwX2StauCgZ873Er2Nv7faCvom6lgobtrINKLHBdLexLRIVbKKcZnie6vU-eKG0ub1wj_4G_2Dt-lMuDHcW_62Boh6er18IrnlK4i1wK54SksGx3nlsbUCEWrVKnJxVHaV5lvaZNbLTwCfwM2xfJQFAAJZarmuoYXIJdVfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حرامبال واقعی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/Futball180TV/98236" target="_blank">📅 01:01 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98235">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">پاراگوئه اتوبوس پارک کرده</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/Futball180TV/98235" target="_blank">📅 00:47 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98234">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bdh6Ly-BxH3Ggo6m21FR7C7LrN_ECNQsO1l_QkYrDNBi_3mrFOBiIRczP0-KTENUHaVGIa2qOqGrKXcpFzGpXyLc0W6uw0HSkS2KTg4I0-BcINtvie9x0EWbmp0c3vvG2nVdNEJx81ha1Xmn1wzc0S22Lc7qZZjCFpHfpuLiramaNuhaeCPAYoh3y0BgSyCkolcxtL06_e2fRggs1GB414N8gbQSjlK5qDiPvRxqghh6cxJVnhLFPBr1agMqO1dSlM38q0pH8HphVTg_XhO-L1a0H-dU-7yjasa2w9TNpA6h_w3gbumhncPCbsJjMDT6U2UnmcdgMvFUxxjYdkiVig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مراکش شایسته صعود بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/Futball180TV/98234" target="_blank">📅 00:35 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98233">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/Futball180TV/98233" target="_blank">📅 00:35 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98232">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/MoX9n6Umlzc5lgrh5cOc-cVAB6ZENU-YmgV5XXvrH4SMnpLykP6D0qzZcJ03EMqCOomkEnep1Y1-OIEqzhMQeM61veSdJdjtZlTcbnod-nUgYEck_vMFTySzVNGl_cFgVCnW2faxj71364c-3CmTpZV7JQOwNs3C4LTqMC1cpf1xIbvIDt-wSe_9y_dcyl45fgEvfNh_58C0UMI808QbWNntWzVJTPuVG12L3mCurQ56nnpMUIkEjhux6YleupyyCApfngECIgWXQGafAphUwso19wq33lNcBrjTOStEP0zFhGZ2cTknchRoE1MzJ91Haz0zf-9Q5kChB6-vVK6Wow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet
@FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/Futball180TV/98232" target="_blank">📅 00:35 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98231">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">بریم سراغ فرانسه و پاراگوئه</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/Futball180TV/98231" target="_blank">📅 00:31 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98229">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/px-sNnHYNQOe7IgeedHFfY9dVvR4WX55yyjb-UwvmdLAGxUykjHLPlZvT1xdmykmuYoDMGJi0VYULSwZBbL4hxeE7uG3rp0uGGhJL_dR1YYJzP2H5Kly2HDWqDmGJWlHIUH62ZTZufCe-va8Pr8WD89qbWd3uPb-DXEwndxjUNcmsuOqK3XMX35L-NTHuyLU6eoVFxBiaTURC88QYtFUqygftOlPBv4dQ0CZuH24G_J2IZvdsmt8-_nMXlyq1YSJ-RkhwBnkbG7bBHeSE3AyBFKpGiZ-B6PWHAkPm6up8yXobWjc8IUel48ilSZBNKCppSncpiaPBc4xHLr5V_NODA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/o0fENN8bzoFSkuUKRWMFYpjrokZDu_hKKsmyxzWTH2GlpUIoUDOSVFfj1eVy3r3DqDcr8f_-NDrQKfcEh6WX9tPWsspWJH10Dc2XtzfnMXDn1jFrOBj67rj4Pxp-kbKnRngo2xZgQC1uN8Ao_ED-S4Iarp4hHxtCrlndjqjnQptiQzoENYJOj9InUSnd3q-NMjVw5lVgK7VQjWCVZ3ovVl1OoLoCUpuuGLPCKX5B5O1SVhvQu-pgD22ENa77Fh9KLRSSa0hCSGd9SL1u9p_JW97DRAGD1coHHZMUq2Cxgi-Rjqwq7JSYebIM9EJcvkWvx4s7XJl5myalmTta8VzEdw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">مراسمی قبل از شروع مسابقه به مناسبت سالگرد استقلال آمریکا‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/Futball180TV/98229" target="_blank">📅 00:25 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98228">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QydzFA6HFTwJ5qjhHwEApYucKRpMCONDYlH_uV67i_-HOSvhOzUFGN2xzgpRVjrFbQKUG3yOvmba5qzso4zBrSLwY1MwYiXDxSVyFgdJTd1uDnFPAKE9e0D7tlceKmc6lSASwOKkcI7W36whPgIvfDdx954LHV8_Gp_H2hgrgNipq5zHb2dDlKDNaIalAjAuTo8yCR7ZzL0Hsxdfdg5fARaNnSQQOTi-4ww68ZtvhUeTePl0qiNrPqcKKITlthG_pqb3Rdrr9nm2zL_iWooAW8-CWW1g0Mu3w1z5ijSsJOzBXsyM68GNMzPDM-GYq-d5zf7-BwDgZY55j7USZV_y6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زلاتان امشب با این استایل رفته برنامه فاکس اسپورت؛ کارگردان لاشیم یه دیس قوی بهش داده و تو زیر‌نویس برنامه نوشته: زلاتان ابراهیموویچ - 0 گل زده در جام جهانی
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/Futball180TV/98228" target="_blank">📅 00:17 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98227">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QQ8fFwHWS_Ewd3BUUWqnM6MJhmRQczz7_fU21lLtMoFRukzmDTXLqSKGqm1n2UjuhtnnZgtqaaLOqsOr9eLW43d7agxTZXFtiOJdqtC3_qN99nTjNjFjHUIbezizkrVdDw488jr4aALUpIB5-WBRMLsDGXT4T787ea3pi3f1aMpHc82A8XJ2osrrcF_dtB1Z1XJZ2wjLTHWf4BgLvVKL_0ITgSUTOsfl61Ay7mx96e7WY3K3__F9U6-G0Ji-AW76itVFNJQQjxDIf-B8hrBjbD9un1Kb8du1sOmFJCQEe0fWBiVsIBBNw-ToAiqIMEelUQ0cHRDSe29NBxBlNYuu_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دماسنج‌های داخل استادیوم محل بازی فرانسه و پاراگوئه عدد 140 درجه فارنهایت رو نشون میدن که معادل 60 درجه سانتی‌گراده!
‼️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/Futball180TV/98227" target="_blank">📅 00:11 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98226">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/wB1eSDl4km9Pl0C3ISrOrGcdPX0u1XiCeGT-Ww5st1JVSFBTOfEjCjCwSpuzICaEtg8NXfhWKQ4QHbvBjvl9CBh5YA0JND2MfwHeFQ0ZvHoDg_1i-ivwqzTLDaMRq_Z1PgcoiARaVIoYCXxH9mhfdm8hcHwDYMpQjOECTQZ1bVcLr-c9UqVUFxHYYxCmiy8Kjq0u8j4s9M-TOttaOvPgbpnTODs7cQ2Q-l7UJpTbtpravn-IAYE-v_srXHj3sokd7aro0yFrVVBZ2T5I5gptBeBaGxybRQ9biTBJKBg_cDSem0MVwsaJWkgduElJsKmkYOCUycLYOha04j68bBoU7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دماسنج‌های داخل استادیوم محل بازی فرانسه و پاراگوئه عدد 140 درجه فارنهایت رو نشون میدن که معادل 60 درجه سانتی‌گراده!
‼️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/Futball180TV/98226" target="_blank">📅 23:52 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98224">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F2nFWIXnXotSx1sWNK8IYJONGF55OAEyO5E2KZNTpJA7aj8jNIt8cQsvwNpWXMeDXA2oS0BNimzmAnYgjRycFNuTWAs-gGQG_8YJZaPMluLJseVFwLUxZQpG_-QM9lvJ5zfh-m4yCOW40rybH-orpyh9Ez5zfnMbXNEcWszZb8yQNHqp2CGuNe5_GTYMwQHsci39iPLEwdR5F15xtqqdJFMUbLZCMdPOcO_d93HUddjvjrqvPedH9JBRGOjX6hh12-NAD4XvORkgNa9yw5Kg3W1eX8jBBmNp_l92fajBe9SwmDWI9yGPwhPV0FxRSW8QRKCw5hJtZo-vi_c200nJIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اولیسه به این شکل وارد استادیوم شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/Futball180TV/98224" target="_blank">📅 23:28 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98222">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RySmkad5Rd9L0OvQ2fBtEb79YIAGUCzUHO2jDmQkoqX96-0fEXj1pQ8jCgzGS5x4VPNAxcrBrBge6zwwf7DLDWMemTaZsgzU9uMSWdDS62XX_PcJW4zlhFG46PT-1biX3iROqJFzLVO7tVFvkbUskSNopiO4zBh-9xai-JL2nQh4yzJqoqUuYVzFQu1oK_dQPDKVY4YAnKSj_Z_LjfAFwNcp9Ube_wamHptz4nQZMnwPXslsf6eHRtlIdQb1TsB4iV8sqFohaMXHx6CeUsiZP3yPF5lPr_VVbtM3Bzp8tzUvysdKahDmVtpoWK1BZo2FShjhuAYVDq5vSpmSR7vqyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jAbsUzVLJY9UWd0kXBP8EHfQXuhu9CXxBNRvb0r5HyX3PYbvhOOvm1KihowQa1Uf1q7j28WgTB29_O-5Cg9YMrfF0J6YaMWKQT7FcxOs7Cf__XFLKkTm-2nvMliPB8WmRyfN2GZdruROx4u0BcEAeOuOYXsCyzcYXQwZlJ8X7DzVwM0lr0C-DAWXDT3YCWb0eqovToJijkZVneFtXsgp1CXqpCudtj_w0eRWEpc80n4cQ2IuMVjv2BfgC3NBsxgnW3h72v6NzSmFnFGuZCgpROwKq2Ze9gi7b9jPBxvbqsz6OpJNviOxLzHcyjROiq0ZnneLB5unIgYcbm2e1-4IMw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🇵🇾
🇫🇷
ترکیب دو تیم فرانسه و پاراگوئه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/Futball180TV/98222" target="_blank">📅 23:05 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98221">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HdiofBv-4CtyLRZk-WFr8_gUb_9gqe0e7jAi65NjqChohMrYlAQCrChsabWg4GfLqGDs5jp5R94yZEd9v_FmnWTR-vP5aosE9vpPE9p5VwIbTIKHlp8SV6Y-oAOCOws3FZwMKpSuJ_PPaDMr98HTdQCBTEorM7c5M-U7nUojgy1AxRGgxxCG86ktbHfGWE9BJqSoVsXSfnVOScuQl0MPgt8KVofsGhebGGQ1skV5bYMjcZvKPzCksDqrjJXlHZSsQ0D4nBUb08isDaaDpp36HON7Q8Jgs_aEsqPxIL5devgUKHLkM2PMnbsWv_rtevU2O6eqjdzHvuiwicnQAMnccg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🚨
🏆
اشرف حکیمی با ۳ پاس گل و ایجاد ۱۵ موقعیت، بیشترین تعداد پاس گل و موقعیت ایجاد شده را در بین تمام مدافعان در جام جهانی تا به امروز داشته است.
🇲🇦
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/Futball180TV/98221" target="_blank">📅 23:00 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98220">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s3CVZWIn1MKWtHkNOyIwoK45xced4uy7Ncq2OnNtOvXWCZdOueq3KwQDKe9LNNw1ulUFoVnirudJmAg070oDrly0XcNW04AvbUFRmqfViURXxTISc99Yr9wHwEPjW0F83fKcER2oy9karLJez5UUtsv6kwQlR7CYdvkTnPn0GX4vwAz4qSYhkqbB3g3_Ypze2mMizWFhkpQdIN4quCqr9do4c3W1u6AXSPZ0-6CoXJthpelwifnNOIfysHEoEs_5o4XbGxkKgO2kYeuEL6OyRaJwLajrWINtTx4uFX3pLA-hyQ_q5MpKyNbmo-nKVDkg4-GMeeKj3aCQwIaWYJVZlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
بردن مراکش کار هر تیمی نیست.
😏
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/Futball180TV/98220" target="_blank">📅 22:59 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98219">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d6GbuCZj31vTutel4CJ53dVv9Qoof99s5opkUMjq2IYTMnNPgSU7K1wQ-cxBrXbDB6q3zR3F-Bq8nmYGOAuV5pZKd3Qntjd1GHFpAqhiPg3VZNS0vE3EmwlqS-Z7IFRO4k0WgNVVGH3lt3sRhONgd10WBpzwnlTgcwfDTxEu1wFJyKrmKAMLAdbr-ini8O37Fd16jeBfahQl0sayFh5LPPInpsAKiumKxddrCuB7fT_N_a0dvmtCmEwYJNEsvaMSDTLeWG4b_b9BPBnF2_tApwWtV1GMQtuW86-CXUWN9MFlVxo_Ox8LivxPzgcPamwB6_ZFr6bpFXAhoOCcW15aaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇲🇦
یاسین بونو، نخستین دروازه‌بان عرب در تاریخ جام جهانی است که در 5 بازی متوالی دروازه‌اش را بسته نگه داشته است.
‏
🧤
بدون گل مقابل کرواسی
‏
🧤
بدون گل مقابل اسپانیا
‏
🧤
بدون گل مقابل پرتغال
‏
🧤
بدون گل مقابل اسکاتلند
‏
🧤
بدون گل مقابل کانادا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/Futball180TV/98219" target="_blank">📅 22:57 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98218">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🚨
📊
|| بیشترین پاس‌گل در جام جهانی 2026:  ‏5 پاس گل -
🇫🇷
مایکل اولیسه ‏4 پاس گل -
🇧🇷
برونو گیمارش ‏4 پاس گل —
🇲🇦
براهیم دیاز
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/Futball180TV/98218" target="_blank">📅 22:50 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98217">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aGZnPFwbYMUJ5ZTMBEIzKRNrvEMcDxosKUy3jYW58kMAbf2tkXgsiDiFfDqNEQCvH6uIhZ1C2iY59e9NeG-iCCf18p2x_n8gefLVlfIpq7XesX1jMWZFq16Fv3bHzbcq7irQ0W1or8fQq16YCMdlicH32cc7I5X_g6k-TPxGiWpfuDv4LeIYzsd_POJgaH2xFgyMcrUv-RX8YS4UOrm5YfaGkyfZ0E8GniyMACrVbsYcIRV2a-6t9ym_FwQGIHBsv6Er0gt_NARE5BiiU3dZTVmwyJRZ8dajaxrlMz7YUO9yGnL7hNaZslQvQ6iIK8ZYusQjcTWh7TQ7OCWdQkKxXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇲🇦
عزالدین اوناحی:
ما تمام تلاش خود را برای رسیدن به مرحله یک‌چهارم نهایی انجام دادیم. هواداران مراکشی در اینجا اقلیت بودند، اما به ما قدرت دادند. این پیروزی را به کشورم تقدیم میکنم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/Futball180TV/98217" target="_blank">📅 22:49 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98216">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fCoqqsyq43FgzokfGRa31k5f6Jvd_vfVKtFVbVq1ytDlfnxTP0V3hcCpc8C6cUNxbuG6AklXRq4JOOo7Cs-wyrmMvC6cqmVQu1QqpDBFS-0tl5h662jO755TUo6267QZmPz3FQr5Fevg4WmAY-Rb1EtbPLTisGU4uVIQ63iS2VwOp15v1GW1WClWFkbowHBh-xU-Y1_c9P964M0p3aGomHfMVcVBeaTH3TjcTpK1ve89f0Qxw5mHAe6xEBWw_8WlD6dMb1UjBfKVHU5mg84D59wPx3aMoZpoUH83eYbaiyLKjqudEW7EfnQTCmC7nIyUA8yMxRK_PJTqKobaAV4UTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
|
| بیشترین پاس‌گل در جام جهانی 2026:
‏5 پاس گل -
🇫🇷
مایکل اولیسه
‏4 پاس گل -
🇧🇷
برونو گیمارش
‏4 پاس گل —
🇲🇦
براهیم دیاز
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/98216" target="_blank">📅 22:49 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98215">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J9vY0TwmJCjjmPJcRrqms-oEeDUcLzN6WSPryD4clNCtL4OPcMzctcoZ8pcgoJlq0jU6MBRBXR-VAfyQFuOChVu3Deh8n7ZL9m_4UvgLca3dMeLE35vAEBnIczgV7BktTyOpZnk2lYMQ3cNc2vDCcN9LRv-LDfbqFjCtPsBQr6aOeE5pd-VipnHYSdBozjYyozKGfirdqYKi62wAft6htw2vcXO7ist5vAf7WdFL--2iPKDkjkUoRSoO4O7YzyQExABktgFUUMIlzi5E9pcxeYVsKgYeeh7WL4YlNs3OeHY9t3iC_xRGyJjJc3-f-ksuVoEZInmKjtqMYzOEbMUFSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
بیشترین تعداد گل‌های زده توسط تیم‌های عربی در جام جهانی:
30 گل —
🇲🇦
مراکش
💎
18 گل —
🇩🇿
الجزایر
16 گل —
🇹🇳
تونس
16 گل —
🇸🇦
عربستان سعودی
11 گل —
🇪🇬
مصر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/98215" target="_blank">📅 22:45 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98214">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dn8dI_ZRNwtKGk_nY8ksXGuYHN5ryHG4uCpLngdW0UbMCWq0MvF8xip80EKOFfIFw6dRWcXdgmfkQ7SHRPUk4jfe43C_FDAqLHHdUXCdE5a4Oc5tA4imHkbiDfv5Q7Dy23Klhs4KGJebSwG3cVbm8WBFwjzke5f4O9ixY80z77OYqgS0XlqAo-1dQ4JOAJD-Pdjx4B5QwDBPSXcnaQ1hzCss3fnDIFz9NZLJarqaJeEnExEzT-2pRSow3EpP8btR8_nk0wXUbTCY3va5n3DuURZfFJIpi_8WzQP3WZbyuM70BDgJ_z4_y6pzwR7sxiqYsepzXnBksMNmJhNHq_rpcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇲🇦
تیم ملی مراکش، نخستین تیم آفریقایی و عربی در تاریخ است که در دو دوره مختلف از جام جهانی، به مرحله یک‌چهارم نهایی صعود کرده است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/98214" target="_blank">📅 22:43 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98213">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ibwV_KUNtKpYvP8ZRKZ9GLAMoPDHGf40ILEvry9Z4v7ZHkEDFyGYoFSw20Aqd6fDQPt1jdyB6U5GfiWOGwORjvzofBiU8uLbew97m9snD2SzF4omMoEX7XgbnA-561mWaLZhzaVO9Sb89lsbuykxDQiN2lkSFfPNCcdj4WuTnee0m4yYaf07t3FT9FY-2N7mATkxYBIgwrRJnSt0825ucp9vqhA0Jtisn5Q3mqdfLu2m8epQQZ8rVvbA6jjMhIyJdBCf2cPYsOG-Cdl7997NTV9LFxoNyxigpcovGp-orsr1xQFmuxZBOS36tNmEQMOsR-L72gTtXzwz2N7VAeFu2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇲🇦
عزالدین اوناهی مقابل کانادا:
۲ گل
۱ موقعیت عالی ایجاد شده
۱ پاس کلیدی
۲ شوت
۲/۳ دریبل موفق
۳ مشارکت دفاعی
۳ دفع توپ
۶/۱۰ دوئل زمینی برنده شده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/Futball180TV/98213" target="_blank">📅 22:42 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98212">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🚨
🏆
پایان بازی | صعود مقتدرانه مراکش؛ شیرهای اطلس همچنان در مسیر تاریخ‌سازی!
🇲🇦
مراکش
😆
-
😏
کانادا
🇨🇦
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/98212" target="_blank">📅 22:39 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98211">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l8zBFyd5ph5DjpYNUg7S5OdQCqh5AzagUWE-AheUKfIgYD5QT3p1UAIiTNN1T1mWb6HuhspWKh0Kp9thxsSvzm51MMNz5yuQZ0olzd3Vewpg9rq_iT-6teF5whRdLvo1eZDiU0yecLtAc7v07nQ3CTcdOg3vQmGO5BEM27Ko9zdItXPnO3Gw80GbIIoDcdU0k0HtyyXHugraE9EskO2XSLiC5Py6LLXTnbXHCHioscokzBj2ZHbTs0rn1B2JkH0Tjs1jPfuxrZiefOcOCeP2t9dNRlRMQGP5_S_Ohy8CF4k4ER95ued5xOoag10P3izTeUYY8cex81GJm0OWLLEdXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
پایان بازی | صعود مقتدرانه مراکش؛ شیرهای اطلس همچنان در مسیر تاریخ‌سازی!
🇲🇦
مراکش
😆
-
😏
کانادا
🇨🇦
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/Futball180TV/98211" target="_blank">📅 22:35 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98210">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/2d14181bcb.mp4?token=XOn_HB3f1296tH2cyw_zf--yZkFxIYiRqACNaUMNnruM4N2xM2-BdSlaHWMj1Ad9_nPFwjVDDfPpLj1upZIULZYC73rQkBYEdNUcAlvXCQhlMign6ysuPt0vS3SrihSfILNqmh01mTVyHr9SYVsTpCYxM5y5x3pBYjYmsArUK8YAfTga_g1jDZYST07uFhkiTPQJraZb03AH3Q0ENzpY5pp0VrAycxvvImWOyuFjyGLPRLU7mnZz1-Addj2ZhGBDFYeB4N2BdyPX5bqIous9rsdw9eic8n5fMrVIvgm_VjtOR7os_dyyd8BRWjBG_i83rjQZNwhKTI5t2U9HHFF7dg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/2d14181bcb.mp4?token=XOn_HB3f1296tH2cyw_zf--yZkFxIYiRqACNaUMNnruM4N2xM2-BdSlaHWMj1Ad9_nPFwjVDDfPpLj1upZIULZYC73rQkBYEdNUcAlvXCQhlMign6ysuPt0vS3SrihSfILNqmh01mTVyHr9SYVsTpCYxM5y5x3pBYjYmsArUK8YAfTga_g1jDZYST07uFhkiTPQJraZb03AH3Q0ENzpY5pp0VrAycxvvImWOyuFjyGLPRLU7mnZz1-Addj2ZhGBDFYeB4N2BdyPX5bqIous9rsdw9eic8n5fMrVIvgm_VjtOR7os_dyyd8BRWjBG_i83rjQZNwhKTI5t2U9HHFF7dg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇲🇦
گل سوم مراکش توسط صوفیان رحیمی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/98210" target="_blank">📅 22:33 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98209">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">گلللللللللللل سوم مراکشش صوفیان رحیمیی</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/98209" target="_blank">📅 22:32 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98208">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HhlrClX37z2ju-R8a4GH1-kIaMzjPZ5g_AgXSegoUVmNLUZCHkR8JI8EQzrW2AS0mXDfF6btgewbX8taA5nrj393wqlqGlc3DHSBn1ruZDfYtO8lnYZOenxfDv937gyCVx0CatzClFKIah1oka749CeM3ilqW_EqR_fJ4KuKmQxmDXs0qsA0qBeuzRfIrMgeI-b0psQvNZV1aIaEeZk-NyDzJ-ZDfkHWukDiHBFCc8uwfq7qfVs8HMittwE-xcJYSi8mxx4XYMMK-6P97a_jd1lae-0iXqHtJ8Eb3ihjaDtMBRqdkCfITchpzfwB7JkBkGP-EbIekjfLTfI5ZtzwBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بانوان عزیز مراکشی خوشحالن منم خوشحالم
😍
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/Futball180TV/98208" target="_blank">📅 22:20 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98207">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/9a15c420ea.mp4?token=UbXrRvDFY5vaYW2w54HRs2O7wTKdVPPO3VB_NumYipXevcsi64gdweeM_bkGeY3p8nxZ8l7AT5gwSD6_D-Q2S4jOtIupmxBJ8bamZqKaKpbSMJBiwOXOa3pq-qdoeyMm2eeZgf157sexHRvcSiWwDoIGlm5HEVIkwTniWJamAPRyFa1h7DaG-UR__p8DhTRfeWcAaaVGukKsPQL6EpLpjeTsOPSknhj6N0u9mR-YFFPfTDsYKTa2qOCbyS_VAVsuvNq-fPUCORbfPg1Ps_zaJIS8fdMpIPw1LTVwufhrx8bZzMqixNIfxTGnJB0-fOcxBYoYcE22YGjYPR-crPTmsw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/9a15c420ea.mp4?token=UbXrRvDFY5vaYW2w54HRs2O7wTKdVPPO3VB_NumYipXevcsi64gdweeM_bkGeY3p8nxZ8l7AT5gwSD6_D-Q2S4jOtIupmxBJ8bamZqKaKpbSMJBiwOXOa3pq-qdoeyMm2eeZgf157sexHRvcSiWwDoIGlm5HEVIkwTniWJamAPRyFa1h7DaG-UR__p8DhTRfeWcAaaVGukKsPQL6EpLpjeTsOPSknhj6N0u9mR-YFFPfTDsYKTa2qOCbyS_VAVsuvNq-fPUCORbfPg1Ps_zaJIS8fdMpIPw1LTVwufhrx8bZzMqixNIfxTGnJB0-fOcxBYoYcE22YGjYPR-crPTmsw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇲🇦
گل دوم مراکش دبل اوناحی با پاس دیاز
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/Futball180TV/98207" target="_blank">📅 22:18 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98206">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">گلللللللللللل دوم مراکش اوناحیییی</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/Futball180TV/98206" target="_blank">📅 22:15 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98205">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cipswXVJmF9rdawj8wFYmNLv8ScYP-nZlCriISyT80XVG0x5g54C5gQJVb59suRPn4dxNnyJ-kygGOPTRygRoLL6oV1iUmuZUAEsqv5N2KzXI3sDVkEojxFILjRa9dKKG-t2lvk4AqyfoqaYmydeTOgITJei7I-C4PB-bsk_9ybFhpdMO_CeyV7aMCPxeZ08ZEZZZHOC21Q9T5_5P7gjbSfEF0_cZTIAze89Ifl6oXadWzt47PKSB_7R2a1mMZ8LCE7_57SPdc9cPuZg9L_iw11CZyQNT2W6sPj3wMORS3aeEc4dppl6eoe2XAHEvdaGfrTaP10p_tJnU1LGH2cChw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدل موی جدید رافینیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/Futball180TV/98205" target="_blank">📅 22:13 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98204">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/98204" target="_blank">📅 22:13 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98203">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/SG-kcDTgslKCQ0oA45UI4vA07N-joLjTVJdlzgBwnwQh9dDtD2MWMfdzmFpaQCu-0Qw7a_XTmpijW1kdpPh70JRNdJHoy0iQ9SYTv9Eri6dbT-ccxclxO-QoV8-lZTcH6KJomb34vHXjMvte8RLWKLszrmtGGUvMACuWf0IgqbEEmlyuyqEOTxNrAIl1QhUN6H5ZK_B7mSSmJAsP-8-SJy9X-Kllbbv0qCc9obkOyyVRBimK3s8KFZe6rf07q362RsXLevpIAJ2qABu4gnbUiMNnfGOc8yKGfG1CiQhJ4eFn0NVUwwjJkrqs3jywXUFmGKKLIEJwk-ryRoDQ5_S1Lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet
@FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/Futball180TV/98203" target="_blank">📅 22:13 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98202">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/79bed95c4a.mp4?token=adNXQME964BpKXz9sOQeRYJ7mdauoS66HsfH3X7e_rJ368yMx0uL3fVS92WMLBJIW7Xcj6oRsqN1vGGWOv5x-sdCznbDZYlZ5kZI_Gf8405dP4wXbtGM40wTsHpF6QduGIxK5sRdVmiNKnLejmjJ7XhkLlZyTHvEJafTNeOfsLR_pcpABn8cT-iaBjQsA1EPHTxB40G_OEakgsVwATVaaBvQPDq2EUFyt2OC2bo2SQJ_UT3SV9TFd6T2QuvNdEEycuzUdfkj1c1AmVg3hFsPbVVKPWeoLYFcCDpggDZX2CkhlYhsFluOmg1RdT7tq3ixttZfTiOVFxkDoQ8G9206CQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/79bed95c4a.mp4?token=adNXQME964BpKXz9sOQeRYJ7mdauoS66HsfH3X7e_rJ368yMx0uL3fVS92WMLBJIW7Xcj6oRsqN1vGGWOv5x-sdCznbDZYlZ5kZI_Gf8405dP4wXbtGM40wTsHpF6QduGIxK5sRdVmiNKnLejmjJ7XhkLlZyTHvEJafTNeOfsLR_pcpABn8cT-iaBjQsA1EPHTxB40G_OEakgsVwATVaaBvQPDq2EUFyt2OC2bo2SQJ_UT3SV9TFd6T2QuvNdEEycuzUdfkj1c1AmVg3hFsPbVVKPWeoLYFcCDpggDZX2CkhlYhsFluOmg1RdT7tq3ixttZfTiOVFxkDoQ8G9206CQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل اول مراکش به کانادا توسط اوناحی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/98202" target="_blank">📅 21:50 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98200">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">مراکش اولی رو زددد</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/98200" target="_blank">📅 21:43 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98199">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">گلللل</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/Futball180TV/98199" target="_blank">📅 21:43 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98198">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">بریم سراغ نیمه دوم</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/Futball180TV/98198" target="_blank">📅 21:40 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98197">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CPLHVszTeeh1fNDsDaRT-or3XflJU7l77MqAjjzyLdjsC2VhGQa-o_HriWrH5ix1z6t3wqHHth4ugKVWdVcIqBsREYJzzxBFfpgKJkCR73A5OeFArEI5xmU6jgmCqOruDa_-hnSq-BDNygNgv_JSCtXvkFNstbCuFOyYGHSZC7t-7okOzSJBNapeiUdMV4mMTPWthaC1X5F4g-0x1C0LoUmHJDnhurfW_I4tOzKGaF8fJsaOp9gdg4-1-FMOjODeLMWGp0Hue0F7Db2EPHb2rkuMomh4sKevkS94_zhv61jO9Bwihs1VyHBQI0Cc9uNRoC0xTCP8VqPR5eSEeBKTZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آمار نیمه اول بازی مراکش-کانادا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/Futball180TV/98197" target="_blank">📅 21:30 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98196">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aQpELOTGgPQrcKFRaXDR-RoQK2ckX9DLxj1z2GrhI7054BiHID59mVmEGg7rMH9vQylV8k2HSQmzj3nrKNLA8puk9TaRob5ycYY3WtXyTRgk92eC-iq7WUbWrIZ7cNGipV0Z2yNGEIzedyUUkRLLj-7XJVhkfmco_OBc64XbFMMFQJrx603TjZQ8gN-TKjL_nOUd2evB6WSeXhMu50glP2dJuYVDz_QJ_D8U5ADvTjxXfaNscAOiGYp5bwmKZgu_cuE0nJlzaBM1tUbPDrk-WUaCcWLkSFruHK5c5kVs-IfxiDjLAVtPJjt8o2-6KMQ9W6iPyeIv4XiU-eq6L2LExA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حتی اینفانتینو هم دیگه خسته شده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/Futball180TV/98196" target="_blank">📅 21:28 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98195">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">پایان نیمه اول؛ کانادا 0 مراکش 0
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/Futball180TV/98195" target="_blank">📅 21:23 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98194">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wo2VfMAoeHukLgn6z9_buUHIsqsLtjNhaEjs0g1S9ihQ8RlbAxY8QZxiaSZPpLZ8JXTHw9PUlxPwe0MskwKVWEZhypUDlsH9aqSBq8yWeJASNLF0tqNZpkKqYquaXjheAn0E5I6XjXchAca91ecoEeeOy56x9fMvETynusK7zZ9v-Z8L_HoZ7o0jJs0kmESOOpVODvpI3apSf2k3xBMPyVSMv0lfow0y88xWbBRO2n8rH1Tn8Ua92x8_yezEq7aRntff61QfO5g-VbT9ykpzTLG8oW2uFf-2GWt2LdbXdL3FVrplpmWSP8lBe3zsbUmeMdeRs7FoHGAIyXjvhKwluQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سایباری مصدوم شد، صوفیان رحیمی جاش اومد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/Futball180TV/98194" target="_blank">📅 20:54 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98193">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hZNrTFDgMhW5CX1aGyFjskGSeyROgnAIWZI2JspYYLhvMvc9JPslvNNBWwG9sytD_Oo6rUjAiibZLQMvgIiFfKhuZolXAJvzH5zv-LP8bd4dIgONgTPD7IdyN9XFdWifinLUiEFVVWO0k2ERRv47AZeANW2W3G-9mvHHpkm_oisLeDDtS0K0BuBk2LIGGcnp-GP0Gi-rVtWPovPdu_oO6hoD-XQ2miuWr3TURcF1Ed6KqC1zSQVZ_BP3KjbJ56s2qikDVYXWlQsgRQa8hSXEPvj8soV_V-_5iMvfMkblAM1j3EVSrMSJMmbDCFPPdjZJcTrdVmDrc-VOXviiePEqVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همون همیشگی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/Futball180TV/98193" target="_blank">📅 20:47 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98192">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z-s-iPlWasP7bXmtE0V29AvOuMywl5T1HMksHm9g84WZE6Gv6Gb-Aij4BbA9HT7E4wA52hvPH-ANjTEvkeE1w7y47FVs8ocDpYCYzT5jbkmx2b6VVe3eACmO7v_TF2wq73DlqY2MIqx28wSVbM5MXgcbKxprbh5-_7GNZYIYakBFrmdvlSKkvozBxlNvirG6N2uEXmEWQB3Sz241hc0x4anC_iUBkTsRFGb3lnHfwDV0rd26XoFL5kTmoX1ckPE3LIUmnStdgfLDwdsewfoxymMvgsFgQfSJnh16io-McRlrFv6P2PMdDPEDvHP5NX6FIU-Sof2jrmun9Jc6cOAU8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عجب گلریه این یاسین بونو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/Futball180TV/98192" target="_blank">📅 20:44 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98191">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">سوپپپر سیو‌ بونو</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/Futball180TV/98191" target="_blank">📅 20:41 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98190">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">شروع بازی کانادا و مراکش</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/Futball180TV/98190" target="_blank">📅 20:31 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98189">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🚨
🇹🇳
فدراسیون فوتبال تونس از انتصاب هروه رنار به عنوان سرمربی این کشور تا پایان جام جهانی خبر داد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/Futball180TV/98189" target="_blank">📅 20:22 · 13 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
