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
<img src="https://cdn4.telesco.pe/file/n9iJPeezaSCVqPqH72PRo_RSHDKX6w9IhrFcY2Pr2yLf3GmMYpBjtIcUTtUYnfUJOGVPs7Lw8F4Zk8Utn-vXKLmgZr84bTP1CgsTeYK9IztmZI0a_ffAJyIUOpP-5tIhbzSj6gMsYWAtT8JX9F-5mqyvDU02mbtIx1ehzrQ94mPho09S24qWjZKS-3vg-CYeAcI3qzm3F2c7UnWR_JaWYuq-P3UCalT9X7V2u9WYe2C7GaR86f_yCFHP9RDyCJ4v4monxygSP5CC5XZ7SahfQYadFXxTZU1JWT1ut74_N5JhbIPqvGW2X_FuRN81m47YD3SV4Y34vrEWmbKYkxd2VA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 226K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡صاحب سبک🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-09 06:17:17</div>
<hr>

<div class="tg-post" id="msg-81564">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/76336c1936.mp4?token=M--dgxEGlEzWSHaVlx3MQNyctmrmsHl41JFEO0b0cLcqPuOCgTaGaAfZIAibyK2sA6JL53RgJPNMkZA5pwSpeTHhiieNMVoWXFrNFeBP6EWS7X80fCbfUfN_L_fP7pYOm7KJnuyqjqGmeP8Z1Y7IgDn-ls6XqIVLrtU6FmjCHXv5iMghMQqSiywz9bCjdWgPsH3JygxGaHorBFB09032yRWN-rAOtLmGrlFUzaZsiQoxOLBFYcP7peDFEFB1BZ41x0xx83DQ42ua6nHyfjv4s_8B3TuxzX9lXdb-DVdMZ8Qtb6Oc-2w8_MHgsjYHB33jCYtbopPG8FqWp8z8D-TPzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/76336c1936.mp4?token=M--dgxEGlEzWSHaVlx3MQNyctmrmsHl41JFEO0b0cLcqPuOCgTaGaAfZIAibyK2sA6JL53RgJPNMkZA5pwSpeTHhiieNMVoWXFrNFeBP6EWS7X80fCbfUfN_L_fP7pYOm7KJnuyqjqGmeP8Z1Y7IgDn-ls6XqIVLrtU6FmjCHXv5iMghMQqSiywz9bCjdWgPsH3JygxGaHorBFB09032yRWN-rAOtLmGrlFUzaZsiQoxOLBFYcP7peDFEFB1BZ41x0xx83DQ42ua6nHyfjv4s_8B3TuxzX9lXdb-DVdMZ8Qtb6Oc-2w8_MHgsjYHB33jCYtbopPG8FqWp8z8D-TPzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خودشون سر شوخیو باز می‌کنن بعد تا ما چیزی می‌گیم میان می‌برنمون.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 858 · <a href="https://t.me/funhiphop/81564" target="_blank">📅 06:02 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81563">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">اسپانیا داره شبیه سوریه میشه.  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 5.59K · <a href="https://t.me/funhiphop/81563" target="_blank">📅 03:29 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81562">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">اسپانیا داره شبیه سوریه میشه.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 6.47K · <a href="https://t.me/funhiphop/81562" target="_blank">📅 03:15 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81561">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">حماس خلع سلاح می شود   ترامپ: شورای صلح امروز به توافقی تاریخی برای خلع سلاح کامل حماس و سایر گروه‌های مسلح در غزه دست یافت. این گامی عظیم به سوی صلح و امنیت پایدار است.  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 9.33K · <a href="https://t.me/funhiphop/81561" target="_blank">📅 02:19 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81560">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">حماس خلع سلاح می شود
ترامپ: شورای صلح امروز به توافقی تاریخی برای خلع سلاح کامل حماس و سایر گروه‌های مسلح در غزه دست یافت. این گامی عظیم به سوی صلح و امنیت پایدار است.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/funhiphop/81560" target="_blank">📅 01:59 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81559">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">شب جمعه خود را چگونه گذراندید؟  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/funhiphop/81559" target="_blank">📅 01:39 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81558">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/06fc3e48dc.mp4?token=mITDb8SwWgSpgAlvi8fkcUGQ8-pUsvopp7D0GauRPY-9DQAcB1-rm-OWA_qmHY56oiqM5fprLqSS8x9-OHsBPBARmf5BGKR6sPIKG_h0InnGMxL0FnWkqQUr5nsVDJg3DlnzOLZOC1_KTSJYRF5qOV3iyKzJwalu1Uz5D7rv1HvMBsPyb9MwesKfhgssKv1JJaNLGkRZTfXNdw6ArwgZVbZLhSyz_9PC9bJPJoJ7iDMnxPf0iZ5OkTufS6_FJCGbL19_8uibt8gyAUqUjT_09_beevxj7F6Lf-4lgvGO5n19MJVF8UEwoexvBfF8jk6q9TaxGpCIPrJzc_bfi0feLzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/06fc3e48dc.mp4?token=mITDb8SwWgSpgAlvi8fkcUGQ8-pUsvopp7D0GauRPY-9DQAcB1-rm-OWA_qmHY56oiqM5fprLqSS8x9-OHsBPBARmf5BGKR6sPIKG_h0InnGMxL0FnWkqQUr5nsVDJg3DlnzOLZOC1_KTSJYRF5qOV3iyKzJwalu1Uz5D7rv1HvMBsPyb9MwesKfhgssKv1JJaNLGkRZTfXNdw6ArwgZVbZLhSyz_9PC9bJPJoJ7iDMnxPf0iZ5OkTufS6_FJCGbL19_8uibt8gyAUqUjT_09_beevxj7F6Lf-4lgvGO5n19MJVF8UEwoexvBfF8jk6q9TaxGpCIPrJzc_bfi0feLzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صحبت‌های جالب پژمان جمشیدی درمورد شایعه‌ی جنجالی
بوسیدن دست وزیر ارشاد توسط ایشان:
آقا حالا ما نشسته بودیم یهو رندوم خیلی اتفاقی وزیر ارشاد اومد کنار ما نشست منم یکم چیز شده بودم با هم گرم گرفتیم و داشتیم می‌خندیدیم درحالی که دستم تو دست ایشون بود یه ذره خسته هم بودم یهو سرم خم شد ایشونم تیک عصبی داشتن دستشون یه ذره تکون خورد یهو دیدم رسانه‌ها دارن تیتر می‌زنن من دست این بزرگوار رو بوسیدم.
😐
این تیترای زرد و سخیف و مشمئز کننده چیه می‌زنید.
😐
چجوری می‌تونید نبینید من همیشه در کنار مردم بودم و برا همینه یک هفته‌ست باید با فیلترشکن وارد سایتم بشید دیگه مشکلتون چیه؟
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/funhiphop/81558" target="_blank">📅 01:14 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81557">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">این پست مربوط به رپ فارسی است  @FunHipHop | Taymaz</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/funhiphop/81557" target="_blank">📅 00:57 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81556">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XUgFj8joE6-IMK-LRhtf8_iU7PTPU8KGl-xM_152IrcIr6j5hRyIYm6CZL0PRW6nL0IbJKOCQbLpaXe0SkbuUTpfxrrY7swMPfd31KymP36pHTQvIeivW51kt8Of9Sm9chTaFXhlG7C9FZX_JZDneF-ZpfUAmO5ZeMqekNrHEzxZ63oMVCiVZzdoxXSJhyj6ISMjXw9MLbZLjyg1pV87qSVjxdyrLIPVgn2dnszCuFk3jDlYvAUEn5yNtqXdU4YsJZd4mRKt4GO1BV6S_wJ2HA9BVAQNmcOWoh6Dw3T1etAUHYa4-G-7_rN61jDUqU6TnBaYTPbVhzARV2E5pDJDKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این پست مربوط به رپ فارسی است
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/81556" target="_blank">📅 00:06 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81555">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">دادستانی تهران علیه افراد حامی محکومین اعدام دی‌ ۱۴۰۴ اعلام جرم کرد.
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/81555" target="_blank">📅 23:34 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81554">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nUhcErCkargL9ass_OaizvASC-Q6CJn9l4OiC7N34pOUPrLDxosQuup2zaTiaJTb7p3BhY5SDh9e0KFT5coqWmoZm0JEDcqa7NBGKz_sbdthed535hnGCsFqhXHsadr5ia9GFy7650A9dVqAzmgnfWgf8auxgq4lEOoKZ-_OcwhAx_UfOkMx_22rTjrbXWLhZKdWG7mV16BiBx3yMCQX11B_gH7CvuTJ1GGgITyK5oWEu47sxNaD1NpzrYnADzcNMI8fNplD1m33-Aqmo77TF7AzmUjc2j2GnpvmimH1OHJ5ofaRBmDttbtQ04xsf95kN0cfMVU14stw7Ow5BilbEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بچه ها ده سال تحمل کنید تمومه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/81554" target="_blank">📅 23:14 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81553">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/37370edf56.mp4?token=qHW3rm5FpAbDPOG4gqzAqxs3YeWTI-mFvall1TPPOZZtG5NAUjKDKo7LloC_f6i3t9D86ZnWzHExg2RxkMoTEwsCWliqCNb5Cw5pcx598wPxl5HZHeXCwJUEGX9qKq2u1fnq_LpJqOrS3NqgKxjE39SVxvbiF5zS0zzRp135tCCPtnOMFb32W3LzOp4l7eO0qMB3vvcaq2PCfunEsWyfSpWCw_3sVDqH5JpsyfBE-o1XLOY4rArvPiw7Bw-hc31UoAw2PAfLP77V2e2jbZKJtusvhYi3E9uH6vwsmikzq4mbWK0Hn6A3na1gKf1loAYr1_RFAPUtny4H6THvg6N2qgt2ZhiHEyOs1NwaigMTvTmyNLzltlFYHKmZemapwBRZ7xCFhW1NA3KHJZezivWcRBPDeVvsXsBROQPveAfX7wAsgNh33ajVGEKaU9FWPfJ7lOmYQris5eejbcmOjb7_uAXBJ6BN529b0X7S3iQAh8T4KL8ITmDzUX3qioO6OfipX6j1xBTpje96CNFad9ulC61BTHfkSAGHYCgpMDhdbivv9TEsRioka_uWbfc-a_YrkATaw_y8mo0MbozoW2tsuo9wZxe529J0giQtjQIX8Pk1x1M-vIQMIR9N_0SqtbP7QepjhfT_7g2yd_Fm4SUylDVgD19spImBdnNdh3ZnM8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/37370edf56.mp4?token=qHW3rm5FpAbDPOG4gqzAqxs3YeWTI-mFvall1TPPOZZtG5NAUjKDKo7LloC_f6i3t9D86ZnWzHExg2RxkMoTEwsCWliqCNb5Cw5pcx598wPxl5HZHeXCwJUEGX9qKq2u1fnq_LpJqOrS3NqgKxjE39SVxvbiF5zS0zzRp135tCCPtnOMFb32W3LzOp4l7eO0qMB3vvcaq2PCfunEsWyfSpWCw_3sVDqH5JpsyfBE-o1XLOY4rArvPiw7Bw-hc31UoAw2PAfLP77V2e2jbZKJtusvhYi3E9uH6vwsmikzq4mbWK0Hn6A3na1gKf1loAYr1_RFAPUtny4H6THvg6N2qgt2ZhiHEyOs1NwaigMTvTmyNLzltlFYHKmZemapwBRZ7xCFhW1NA3KHJZezivWcRBPDeVvsXsBROQPveAfX7wAsgNh33ajVGEKaU9FWPfJ7lOmYQris5eejbcmOjb7_uAXBJ6BN529b0X7S3iQAh8T4KL8ITmDzUX3qioO6OfipX6j1xBTpje96CNFad9ulC61BTHfkSAGHYCgpMDhdbivv9TEsRioka_uWbfc-a_YrkATaw_y8mo0MbozoW2tsuo9wZxe529J0giQtjQIX8Pk1x1M-vIQMIR9N_0SqtbP7QepjhfT_7g2yd_Fm4SUylDVgD19spImBdnNdh3ZnM8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شعار مسلمانان مراکشی بعد از نفوذ غیرقانونی و حمله به اسپانیا: الله و اکبر، ما اروپا را اشغال خواهیم کرد، زنان و کودکانتان مال ما خواهد شد.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/funhiphop/81553" target="_blank">📅 22:37 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81552">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/POKkwEjWbdV9edM8Mhx6cF4ms722x0JUsennuOunuF4--uts_D6Px-szabRn24AKuhY4HA6wMDsnHLVDXwonjwjlltH03_sC7ASMW68mUKxo7eKxgSuUYqQZdDy41HGK6t1uH_wrrUwmDdxLYM19EPhxB2m4h_YFXsNXEuiisolUpkZTzLraGgozbH0uSlBFQ-_CDzjpBDcyd1f8GYf8slw7OrG7QJP1CarjdY6Bok4EbfYC8oLxu-PTelNCOyKYgPgcNB_qxbKfGMcl0tdcuzt9yRmVuG2Nmv1XkK_vZgLz9e4K4dGQ3Il7-rhDLZG6_Xl5nm9ZXHNReK87MS_rRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
😐
پشمامممممممممممم
نیکی نیکول دوست دختر سابق لامین یامال پورن استار بوده ، فک کنم یامال وقتی فهمیده ازش جدا شده 4 تا از فیلم هاشو پیدا کردم براتون گذاشتم ربات چه
کصی
هم میده لامصب
چه ناز و خوشگلهههه این دختر
😍
مشاهده فیلم:
https://t.me/Footballi_Dark_bot?start=get_tbcbmlqhfqdjyaew</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/81552" target="_blank">📅 22:27 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81551">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">ترک جدید مهیاد به اسم چشات میگاد ۲  ریلیز شد    SoundCloud  @FuunHipHop | Mmd</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/81551" target="_blank">📅 22:14 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81550">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WWnYZ3Zvr6g-E9WT7DkdxVB_hzLcR2Gkuy71_PD9FGkPITDfKo0bo8RFiAQpn1XktablRIBv0IZFccl7aPPQKQJN6BjMOll2rIQhjzwLr1R6-fu7S4Fvo3nQ5XBxv1UlR5qt-k7Ffg4jd-G4GsN0Yf43hKlJZOBx4flP4FKqMF5hjHw-zMbBYPvi9AhBte7juI7Jc8OqOAXFD5mgcF7HKbEe923J79XsyrRiD-RkY055w89mUBJ3-FbW1-CD_qW1Wq3Yk_ktqJ9zOLd9n3RJ7J-1KeeKS1-y_cpHUhYsv0H84Peh6cP-Z8NsFuF4roBTMhyP9fT1KZ37VtbO7nIfrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید
مهیاد
به اسم
چشات میگاد ۲
ریلیز شد
SoundCloud
@FuunHipHop
| Mmd</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/81550" target="_blank">📅 22:13 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81549">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RZ-Z4N3REbo9xE8VKTc1xZ5akvPD_jf3vWYnAx0iS753r_u2A1BCEf4lVzutMJS3Qp3CSY__pyR4Bfh8WGiTH8YGkuMZ6DNanzzZXQ81ZYz0xOMNNPAt-vHTVup1DhmCThn-PC-aPPquKu7s22LmHDrvCuypagKWAcyYSj4V1HzeSJkcZ193cZtYN7ZHABArNWHMxkehPtKcO_yqIrRuxxpEn4psIYclKUbz27yUeHmNTgLQq8o-9la3eLI9zeEvs1NWCdCPExMCttrl4WcV65zqYSidWvkpm21182qB0Y8z0sN7DtyjHeF6klDgvo-ZPHzcppsy647D52DNVw7uRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یتیم گیر اوردن کصکشا  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/81549" target="_blank">📅 20:59 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81548">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">پیج اصلی سروش ولی زاده برگشت
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/81548" target="_blank">📅 20:14 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81547">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GNrecDBjt9hlR2Hwb8-3B-aeSGnmFESMKgJ-IFq9tF7MDTHN8b1LEw2_LAr7tF7yMULM2KOcTiw_95C-GRgncArIv-zqut_wl3R08Hr-2ZZZpNeAwverVAYAqUG45Cph9McV0nFJxPfG2MMEr0ilxk2f4I_Wk-cbvr7Kl_RCIBcAn8_JnR2t9mO8c_StdFknAaEHLodmyGwychJ7oFEF3pA_tOrDNccjfIvwelWaixv-8BX0Vew0ZinoDWbGl3qPSF5doyT6sRhmS3TMeF1R-7YaeTGZhq46ky007jeHaQIG7gMugYDBnCuZfsbmHUs2c04j0zWgD4ja2ZeyEk8TUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پروفایل پاول تو تلگرام:  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/81547" target="_blank">📅 19:57 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81546">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t-JjDpRMl3Ur8HlQxY85zQqmykni1qkjffldUd5qBDqdnHLwqwmkG6h5_7oxjBSMvUkt4e8DRsoaD4Q4EONm8sjragAUN4rqYC45RqG3-oCtBG11iF_NwfVNbGFdkhRGG5bWkU6Ds-GQsKK8QjcLro5bu0iFOYaX3km7oe5NxOr7ZjVx71S5FHp2WXzLbPs_h8WXhLj6Kh-FumEklnTnmQ3_lFdpxmcBzWXKukwJ5DHgj0FrH5RYzmeEGQv-YDBEpKC0oIwP41x5wKW4PyNPJtlbsUxgKdxRs7Er43F5KfFbOuz30nozOuhSoQT0mY8NE55qF2JxwmhGi3HXQ48dOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این بازی شاهکار رو از دست ندید‌  @FunHipHop | Jenayi</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/funhiphop/81546" target="_blank">📅 19:52 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81545">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PA1KdzsiuB7jphOv-MF4GzR0ya3Dof2S9QYix_JHkQQTPtVKxwTQKSObsfC2sg-AXebnLkXFGrP-pkUJrUByl0nopFcJEud72ZNdGI4t1onB6g5Yw9JaE0pp5SfXG0Gfk5z_Z7-Bitwn1Mt4AcWC20y5vQKlKw8YRFlQ0C8JKnBW4m6RHhPhp1GDjMVr2qkOCc4_lGxoHa8UiSEMhw7LAoLwUG3L3GkylGBDpr4jnQx_8ngxmcYPiyhLzOMAwElrRWF6sD93WnCErCFhR1h65PNzM83oGwkBjWpK9UInz0MxIyTAlEkUVCSc1xWio9k2FfVy2thZF-WatnOe0m2hrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این بازی شاهکار رو از دست ندید‌
@FunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/81545" target="_blank">📅 19:45 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81544">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DYpRvI9xc-GtD15fX_xAaRIwDbkbRsO1zhNw1Ba9xw2bffrFl80q516tmZr3g8uDXt1ROqPk3mlwB8FV8iu3gqODUsBMFu87OHbWpv-FF0TTVSY0KvyWvYbGwZBnBBSavDJwxQjmPXAM5gM71FNW1XuEtbuTCJWtxHe36W5jb0hvXQv0HmvUUq4XYoDmkx_aYkJScx-wbGYTKHazNHEY_KhMboeckFA4ydsuwH2BLc2cLqsaCbVvewYKf0x36n0AvJCpomspKI0hmNBKWBsNCJWYUAeW-R5qWh8soPpcGviKesSLK1mcS2l8TxjhobHpaZjyWby_D3iEXWLbdMyDCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽
بنفیکا
🇵🇹
-
🇨🇭
سنت گالن
🏆
مرحله مقدماتی لیگ اروپا‌
🇪🇺
‌
🕔
پنجشنبه ساعت ۲۲:۳۰
🏟
ورزشگاه استادیو دا لوز
🎲
با بیش از ۳۵۰ نوع آپشن پیش‌بینی
👆
ضرایب شگفت‌انگیز
📊
نگاهی به آمار دو تیم:
✅
بنفیکا در ۵ بازی اخیر خود مساوی نکرده است.
✅
سنت گالن در ۷ بازی اخیر خود مساوی نکرده است.
📈
میانگین گل در ۱۰ دیدار اخیر اتلتیکو مادرید ۳.۶ گل در هر بازی بوده است.
‌‏
⚽️
نکاتی در مورد بازی‌های رودررو:
در دیدار رفت، نماینده سوئیس موفق شد با نتیجه دو بر یک بنفیکا پرتغال را شکست دهد.
🧠
بودجه‌ی تفریح از بودجه ضروریات زندگی جداست.
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن رایگان
🅰
r8
💻
@BetForward</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/81544" target="_blank">📅 19:45 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81543">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ehoX6TkFOJj0kgPXVq5vGONfy4mPg7bD_FTxJfeY2cd-IeWJhDpmWyu7JH60lVxEZ8QLZ-yfPe-NHNxJWnJugjDEepwK51DOT2QStHk4v8nWh_IbKzbduN0Ko0CTVeqm_AbUWOm_nz3tHXXY8l_KLUnu3NK4yVs3B8aPmwH5ng1C8E_l5S5UsN7BOjF0ScSOxSudvYJFwoRiDjQZyUf_XiLrd_5iMAhNugte_jgijdwxK-QmAIRXDN_Kc8iQdkAn85DhDAV3hSnx9f-2xtomFf0gf2E_bU2JT-JsxGvfC1dSRUt7UiZk12O5kBOY8aSZtqzqt7M18kXNidxLeDS81A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایران:
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/81543" target="_blank">📅 19:06 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81542">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AxOykL7OLvvKfb1fzms3DnDCwKA3Az2yiMfANyv6mAeJi-OwcQUUNoIrIQHOUc-wMb-mpuH--BU7HrFwMObc7k3-639VwmZuVaxy1aJ_5e3VzLPpx7Oanh3FlERLz7dUBX022z0nDp5m1kRaIItfMo0cAKSz6_NYgPOGjbmaXZbEeFHI55FqUnR7xC2WkNSGYN7bT_Ct3KrSucoDJ6e_FoM3H6fXTXV33NDp5Eg09uFkZsRz0MUH22oH55tTDG3NXk3BMQqPqx3h0PfxpLP2aULzv_bQ1fskM8nV48uOpgKB6nPcckr13xeoVqD49ZdLUm8qqOxfOHpqdADpxQnC2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گلشیفته چقد ترسناک شده
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/funhiphop/81542" target="_blank">📅 18:01 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81541">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QoxJ5dgQjyU2GO26NJBYcF0rv2Fcf_mwNLFpMwgIreoCMi-55hXbJ9B8-OA8Hehz8t0MPHZdlF4zcx7Y2zieLIWf7q2jhB7srS-DtmNemX8T_2KPXetxu3vGPOvc865vZC26GZ5gf6_1zUVqv3quLiCw3HHp0ai_GChP6HCQjg2DqbyaJe_RekTJzmo3NTkMaoqLukEsemobEmQifGrnMa2V6sdhFLNwt1PI4_uZzS3ZEFKvUneJ_X_ZQHF6kN6X5NxC1z1qN0dYi-6QPN8WCT_EBQTwDgaY0zio86zwRfU4TKzmbbm0tdWLN3yfvMLZt25ja_6zWhcL23RcbDgYdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حکم اعدام بنیامین نقدی، جوون 26 ساله و از معترضین دی ماه صادر شد.‌
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/funhiphop/81541" target="_blank">📅 16:56 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81540">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jVFBkxKrpDsLyLOCty1yvQyv_bL08uCj3hvmv67Bv_xoEJUBJhF42xgcbLcdYzi4UYMWgMT_RWO6QvVQ1EMNM1zXeLsaKIgBqyBuahmeNK1ekOeg-ndvkUmfuVpy6_M0GQf4xlZF_kvllLlwrXxghqRuXkyAj_GhDt4COCEkZ0N3qyPyk3DUfGLwtm9QJWWxP7jhXMk5EXDmkaCiXTB7bd3FNNBij7E5L8r6u3AzrHIRZwGw2T4n3K7t6LT5gLnhQKsDRtek4a51u3wxl5e2CK4R6pLJiNxjKXfIiC09pYjwvT2G8LAngoBqP7SFzledTIMOELCkV6iA1XKtB_PqOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیج افشین فدا بلاگر مازنی بخاطر استوری که برای سه جاوید نام اعدام شده تو اصفهان گذاشته بود بسته شد.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/funhiphop/81540" target="_blank">📅 16:44 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81539">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">از نیرو های مسلح درخواست دارم کره‌ی زمین رو منهدم کنن دیگه زندگی کافیه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/funhiphop/81539" target="_blank">📅 16:30 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81537">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AGuidskOVLpNpUWDu5JMxRfhjt9loDq22EC44GwUkBfPi3v5GMBRU9na38y_vGSVaj8t2eCcfPzQY1jeZDrscToKgcYNLwnNfAbYbyl4x86D4ILW4OsfF8DJVmaQ3a-c-92NvnNozqX8OeGd8XV37ee3P5xe_49_mZ6nNHmS7151a-pqFsYG3KjqqBE3qfzYjReVbz1aeeeXhWx630j9qd1_4EB3qj0XEoAy22bA8T-rfVAYngWlpigqb42yMuzwvoVmUpLRsk1QH_TvvmkdCRaPfHqxnC1fy-jKu_QmAUFBiH4C5coK96555WMN4VXCy3SR-LPe4uwnbnT6UCMSRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آفرود سواری در کشور ممنوع شد
تصویرم از وضعیت یه پیج آفرود که این تصمیم دولت رو به تمسخر گرفته بود
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/funhiphop/81537" target="_blank">📅 16:00 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81536">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">اشکال نداره چین میاد بهترشو میسازه
🔴
چین گزارش‌های منتشرشده درباره برنامه‌ پکن برای تجهیز ایران به سامانه‌های پدافند هوایی را رد کرد و نادرست دانست.
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/funhiphop/81536" target="_blank">📅 15:47 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81535">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n5fM9rimHdxAqtbnSnNR_79kBahvGmp79HscuyxvlZ-g6uNjJaaPDNNpb1Oq68FDFSNi-DQNxkXT-d1qk6eu46_m7XZiCBInX78rGapnyPflMoXulA42uiWbR-W_bUmsJIVrkFq6UIbNjmzKr53aZP8cgMdIZMtwSnmMFmrJZe0INDMwt6ObgSBbnXWYP6Cv43GoidIf0csW-ka6SHPnS9Bct61hNMbA5-RF6ucpvCPp4RaO2oiWh3i6RNmmXIVtv0QufeNBpNaUQw0YZLeN-7xN2V39BTxUQutWE-5vmhkKNaqhMjHjw701CKsS_-tla5NtGacYn4UgdtwV9PXjRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آماده اید؟
صداوسیما: امروز صبح در پاسخ به حملات آمریکا به ایران، 6 تا جنگنده F-35 رو زدیم 3 تاشون کامل منهدم شدن، 3 تاشون هم خسارت دیدن چند تا از خلبانان جنگنده هم کشته شده.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/funhiphop/81535" target="_blank">📅 14:42 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81534">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qS1t23kUxwAsMK8wwApqJymzPYLmUKK_XCky0FJyr_6FWe2wdwCBsm8GKQnBdBatXYuH6OfkhcsEgionMa7aw0kIpSIPejZwhFuoeDNYfcSkLVWPVOpvXiedNpFC9Lrpl3LitlvBYD2EvaobpYcQH7dFUD-DPgzMpRHVqwg95A4ll54add8bNLn_OzcqqkmTo7NvObnJcLk1VEJyIb8srqCEdcTBKxA7WiMiHlogls-8akrC6FJjjBAsY5XhXwaERW9ZtjQbSaEEVjjs6vNhTgxYHYMulKuTiD1Cs6xb6pj0ny11lhPkymF5RQUwHj9-GaWEs1-7P6F6ePu3Bwffzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دایرکت یه وکیل دادگستری.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/funhiphop/81534" target="_blank">📅 14:05 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81533">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/533f3ca2cf.mp4?token=iRn7TOYLpr2q7MDQG3FYEpVAZFPnP1oxfBoC8CEkGM2Ux_LEo1OSoHBP_d-F3mi6cckl3RktDhOWseJI1bpdvJsOH-_M5xh_PS_6336xTB1lrWtrnNByw2uJ40GnwG5m_e0yZfMKt_37kFiLWTDoJ7e05tbjaD9EfESzvIrK7V6pF6RRgcGSv2UPG4tL7nudMGcKI48AXX1LYedlPx46eGZyWZlpPDyt-R37GaEsJ2VMu_aX22eriw6eG5ZFbqBXMtQMOPNx6Pg4uQ-h8fhjRfh7PneIRe-3TfB7m_4EifrschvKbNPicFBtF4_ZZAKYEMxjqehFE1MVPrmA-mGpnBgYajAonkkN8mZRaTckxncTVbfA6z1H259RHoS-VnDidMA-ZbmTLFnjb0BHYuYoGShrjODF1renEfx7JZLEYgWW45ssOQzY_zccZCagCQB5jyNzRm0VNIABJMJn505B4Kdo-iXCKtFPWVGWuv53qeqtEFgwjBD2ZU6tqNcRXrEF6raBEIhltBDaItk9ajKDSaXQ6llXF3LDtc3WMHBmQH0MEHBofYxHB6Qr3w82xfk86dIrNUqBmdrJ70OJcFu-RrrvFsL_brsNqJy7QkHr4Cwm5P55W8sdQ5ezJpJGjN7wtow0g9BZ3ovZHcNyl6whx97nRRfUfoPw7cIO8Crk6Yg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/533f3ca2cf.mp4?token=iRn7TOYLpr2q7MDQG3FYEpVAZFPnP1oxfBoC8CEkGM2Ux_LEo1OSoHBP_d-F3mi6cckl3RktDhOWseJI1bpdvJsOH-_M5xh_PS_6336xTB1lrWtrnNByw2uJ40GnwG5m_e0yZfMKt_37kFiLWTDoJ7e05tbjaD9EfESzvIrK7V6pF6RRgcGSv2UPG4tL7nudMGcKI48AXX1LYedlPx46eGZyWZlpPDyt-R37GaEsJ2VMu_aX22eriw6eG5ZFbqBXMtQMOPNx6Pg4uQ-h8fhjRfh7PneIRe-3TfB7m_4EifrschvKbNPicFBtF4_ZZAKYEMxjqehFE1MVPrmA-mGpnBgYajAonkkN8mZRaTckxncTVbfA6z1H259RHoS-VnDidMA-ZbmTLFnjb0BHYuYoGShrjODF1renEfx7JZLEYgWW45ssOQzY_zccZCagCQB5jyNzRm0VNIABJMJn505B4Kdo-iXCKtFPWVGWuv53qeqtEFgwjBD2ZU6tqNcRXrEF6raBEIhltBDaItk9ajKDSaXQ6llXF3LDtc3WMHBmQH0MEHBofYxHB6Qr3w82xfk86dIrNUqBmdrJ70OJcFu-RrrvFsL_brsNqJy7QkHr4Cwm5P55W8sdQ5ezJpJGjN7wtow0g9BZ3ovZHcNyl6whx97nRRfUfoPw7cIO8Crk6Yg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
دیشب مامورها ردِ نوید زیادخان، همون فردی که خانم‌ها رو‌ تو لایو کتک میزد رو تو خیابون خرمشهرِ تهران زدن؛ بعد که رفتن دستگیرش کنن، این مادرقحبه با قمه به سمت پلیس‌ها هم حمله کرده! مامورها هم اول شلیک هوایی کردن ولی دیدن تاثیری نداره؛ به پای چپ ، پای راست و…</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/funhiphop/81533" target="_blank">📅 12:55 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81532">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D7XthsLGAbueYTke__O6EqA1OfNJX7qRRxRkneRRLeQd_t-Hmg_-8Fbvq5VUU-2cOHTmdWd0weaAvTBhOGM-p56BL8po1f93TN1Z0NbSmAC2EYoAUB7eOrFfGYwTyZ_q9FzNJhLkH_zZxqnq6TstEvrohjg3V_WUqHJDApDjuAmTNKucJCykPIQzCbC35ukmowrgCXTIkVehNoOcnrVpBdRzRiyYyFwQhYq_8K7jNsOMeHtZECvJsfPc6AyiZ_nCPszZCpVyeXBCasmjEpT6wTSwTK8quH4zzeHo23n7Ish3D4zPoP0Spvw9or1j1rHCKjrYSHJNYB07sS_9QubGBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
دیشب مامورها ردِ نوید زیادخان، همون فردی که خانم‌ها رو‌ تو لایو کتک میزد رو تو خیابون خرمشهرِ تهران زدن؛
بعد که رفتن دستگیرش کنن، این مادرقحبه با قمه به سمت پلیس‌ها هم حمله کرده!
مامورها هم اول شلیک هوایی کردن ولی دیدن تاثیری نداره؛ به پای چپ ، پای راست و دست چپ نوید زیادخان شلیک کردن و این گراز بالاخره زمین‌گیر شد.
این مادرقحبهِ 36 ساله، قبلا به اتهامِ "ایجاد مزاحمت، دعوا و درگیری، سرقت، ضرب و جرح، مزاحمت از طریق فضای مجازی و تهدید به قتل" زندانی شده بود.
@FunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/funhiphop/81532" target="_blank">📅 12:53 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81531">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Osg5xQD1CUgmAaLIdxA6z9FS70X0uWbmIkvAsdLf8X2jgSGT3bFlHywEzi8PQ-5BH5gce-N6n-c-C_PFbWHRwpzD9d546SLCkKI3shaYusYBDbL9KrInioyqdHviOWlNyreAD4ifxDY3cOAIIM4ZTk77XXpD7m2oLaIBgYdoumvWP9czjaB4yjqIL2h0MdmxibPfstuFqszN3yGZXGbrs5lEoFzBGi3PxSEtujBgnsMzbuTMflZutwdKaR1dbJjtkFa-YuL5OIgTZoZRixN8j_OQDRrEPwDgKhqlAB3BIDpew1wWs4tufSCnqBE_9Z_qw80njngXOeD-EfmuYgnbeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽
بنفیکا
🇵🇹
-
🇨🇭
سنت گالن
🏆
مرحله مقدماتی لیگ اروپا‌
🇪🇺
‌
🕔
پنجشنبه ساعت ۲۲:۳۰
🏟
ورزشگاه استادیو دا لوز
🎲
با بیش از ۳۵۰ نوع آپشن پیش‌بینی
👆
ضرایب شگفت‌انگیز
📊
نگاهی به آمار دو تیم:
✅
بنفیکا در ۵ بازی اخیر خود مساوی نکرده است.
✅
سنت گالن در ۷ بازی اخیر خود مساوی نکرده است.
📈
میانگین گل در ۱۰ دیدار اخیر اتلتیکو مادرید ۳.۶ گل در هر بازی بوده است.
‌‏
⚽️
نکاتی در مورد بازی‌های رودررو:
در دیدار رفت، نماینده سوئیس موفق شد با نتیجه دو بر یک بنفیکا پرتغال را شکست دهد.
🧠
بودجه‌ی تفریح از بودجه ضروریات زندگی جداست.
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن رایگان
🅰
r8
💻
@BetForward</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/funhiphop/81531" target="_blank">📅 12:53 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81529">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">یک منبع آمریکایی به شبکه "i24NEWS" گفت:
حمله شب گذشته گسترده بود و تأثیر قابل توجهی داشت. این حمله تقریباً دو برابر قوی‌تر و گسترده‌تر از عملیات‌های قبلی بود.
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/funhiphop/81529" target="_blank">📅 10:27 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81528">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">خلسه از زنش نیلو جدا شد   @FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/funhiphop/81528" target="_blank">📅 10:20 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81527">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">خلسه از زنش نیلو جدا شد   @FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/funhiphop/81527" target="_blank">📅 10:16 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81526">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">خلسه از زنش نیلو جدا شد
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/funhiphop/81526" target="_blank">📅 10:15 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81525">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WnAJovXw7p8fhqCwAXxSQx2eP3HUx3QGVxDuCo97TLQdihNm5EHtyJLJXmOnlCrzY-BQ3vL4X8i78HUhbA2x2YqlErO5gXrpHJEa2eJ_-rz3001iMgTJp5HiR16hsIAaJbp5XKmeALtGHRlXid5TnWht_jXtPYzrQrmY_FtUsUYSV7eAuHqUT705auVKv34jPlRvCw1vAz_72pkl9bvUxYu4gd-0hmrY-A-t4RsVEHorHpu3duyF51esBGvDUlZFWABtrdgeF-358DCJYoDPmgXh6qwH6R0QyX0pWCA3F2lv4PBzp_9nsUNOJFZrMw18hM2652ekgY4ZEbs5BKLBhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ای کیرم تو این اکسپلورم
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/funhiphop/81525" target="_blank">📅 08:46 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81524">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">اینکه شب گذشته آمریکا مسکونی زده احتمال داره یه پیامی باشه برای ایران واسه جنگ های بعدی که احتمال داره رخ بده، که امیدوارم کصشر باشه و این برداشت صحت نداشته باشه. (اگرم انقدر اورانگوتانید که فکر میکنید آمریکا کصدسته و مختصات اشتباه به بمب و موشک داده و صرفا اسرائیل نقطه زنه نظر ندید کلا)
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/funhiphop/81524" target="_blank">📅 08:17 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81523">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b757b219d.mp4?token=G360l9NnA7kOt7mjmSCdMQS4fh9Py5TukuhVCHfkyhs3kF4VfuZzH1ssnJn20gE-xCT3ZUVvYm6bCXHOLlDdfMWpoQk0SQ7GW6V_Otg6_GVih__V_hNW3Ks1Aiy9iJ4gRFcOL-71pt1viVjYO3qtg53HCttzGvG1kitpxX2WJYLoGsH7rLojHLm5KBoPG5O37JdOWXcJxxkoQDeuMkf--865QrGq_n9mJB2kwol_e7vq5dOPT2CKd1wsEg836m86cnlBH3Iq66n7DFah-4DheM7BGIN5xKiQD2kqaX5rSPGfOPkVo2OESbw5M8jMjmaBTGRbUP7TYrXmKeSxIZNiNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b757b219d.mp4?token=G360l9NnA7kOt7mjmSCdMQS4fh9Py5TukuhVCHfkyhs3kF4VfuZzH1ssnJn20gE-xCT3ZUVvYm6bCXHOLlDdfMWpoQk0SQ7GW6V_Otg6_GVih__V_hNW3Ks1Aiy9iJ4gRFcOL-71pt1viVjYO3qtg53HCttzGvG1kitpxX2WJYLoGsH7rLojHLm5KBoPG5O37JdOWXcJxxkoQDeuMkf--865QrGq_n9mJB2kwol_e7vq5dOPT2CKd1wsEg836m86cnlBH3Iq66n7DFah-4DheM7BGIN5xKiQD2kqaX5rSPGfOPkVo2OESbw5M8jMjmaBTGRbUP7TYrXmKeSxIZNiNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">متاسفانه شب گذشته هم:
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/funhiphop/81523" target="_blank">📅 06:51 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81522">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">نتانیاهو:
نمیدونم دیپلماسی چقدر ممکنه اتفاق بیفته، اما نسبت به شیوه رفتار ایران بدبین هستم.
اونا همیشه دروغ میگن، همیشه تقلب میکنن و همیشه برای خریدن زمان بازی میکنن.
آیا ممکنه این رفتار با اعمال فشار کافی، از جمله فشار دیپلماتیک و اقتصادی، تغییر کنه؟ باید این رو امتحان کرد.
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/funhiphop/81522" target="_blank">📅 06:41 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81521">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">تسنیم:
برق برخی نقاط اهواز قطع شده.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/funhiphop/81521" target="_blank">📅 05:05 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81519">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">انفجار های پی در پی قشم و بوشهر و بندرعباس
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/funhiphop/81519" target="_blank">📅 03:57 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81518">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">بوشهر آبادان کیش
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/funhiphop/81518" target="_blank">📅 03:42 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81516">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a76739cd9.mp4?token=iZJhU2WN2IKP-Lm_1GdZIKoO43g8LXmLmTWmI1Xf45JrFOechf5n0EF2UFL9PCk2Asa7k0_2i6ms_-uoJJXAvi5pWJop6oB0IW4rnGGDUJlbmU0v8xnO0bYSf-BgB4otaqrBgDCIUTJgBwiM4dZrXvIZhYV9pmmGqapAAGh4V-OAS4dGn4q0wHJo4YyR9dyK08aV04XVlpok6TNUTyKqcEj0_ki56HxFpJEEZXAnSLpaZ9j8cS9bCtfkwC_0JCpR94eERuGEYryYWV41JVhn5wDWF7buyn3lgLp772yAUCHUoNdpsKRWtuCVndscsEtmbe4blo11hmRhHYdWeoPhFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a76739cd9.mp4?token=iZJhU2WN2IKP-Lm_1GdZIKoO43g8LXmLmTWmI1Xf45JrFOechf5n0EF2UFL9PCk2Asa7k0_2i6ms_-uoJJXAvi5pWJop6oB0IW4rnGGDUJlbmU0v8xnO0bYSf-BgB4otaqrBgDCIUTJgBwiM4dZrXvIZhYV9pmmGqapAAGh4V-OAS4dGn4q0wHJo4YyR9dyK08aV04XVlpok6TNUTyKqcEj0_ki56HxFpJEEZXAnSLpaZ9j8cS9bCtfkwC_0JCpR94eERuGEYryYWV41JVhn5wDWF7buyn3lgLp772yAUCHUoNdpsKRWtuCVndscsEtmbe4blo11hmRhHYdWeoPhFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در جریان مراسم اکبر عبدی، عادل فردوسی‌پور در کنار عباس صالحی وزیر فرهنگ و ارشاد جمهوری اسلامی نشسته بود میخواست دستشو ببوسه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/funhiphop/81516" target="_blank">📅 03:01 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81515">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">Game started</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/funhiphop/81515" target="_blank">📅 02:54 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81514">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">Game started</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/funhiphop/81514" target="_blank">📅 02:52 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81513">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">بابا کصخل بمب افکن نیست که رادار خاموش کنه، سوخت رسانه</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/funhiphop/81513" target="_blank">📅 02:29 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81512">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">بخواد بزنه ردیاب سوخت رسانا رو روشن میزاره که مهدی ادمین فان هیپ هاپ بفهمه؟</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/funhiphop/81512" target="_blank">📅 02:28 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81511">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">حاج زدن حاج
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/funhiphop/81511" target="_blank">📅 02:28 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81510">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">تلگرام کانال روابط عمومی سپاهو بست  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/funhiphop/81510" target="_blank">📅 02:14 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81509">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">کصخل سوخت رسانا بلند نشدن که باهم بندازن، بالاخره میزنه دیگه</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/funhiphop/81509" target="_blank">📅 02:10 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81508">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">ترامپ مادرجنده ساعت دو شد چیشد پس؟  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/funhiphop/81508" target="_blank">📅 02:09 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81507">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">ترامپ مادرجنده ساعت دو شد چیشد پس؟
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/funhiphop/81507" target="_blank">📅 02:07 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81506">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">فعلا چیزی جز صدای پدافند شنیده نشده به فیک نیوزا توجه نکنید.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/funhiphop/81506" target="_blank">📅 01:28 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81505">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">پست آدرویت تو چنلش: این روزا انقدر اتفاقای بد و عجیب میوفته تو ایران آدم نمید‌ونه از کدوم ناراحت باشه
🤧
🤐
🫤
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/funhiphop/81505" target="_blank">📅 01:09 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81504">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">تلگرام کانال روابط عمومی سپاهو بست  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/funhiphop/81504" target="_blank">📅 00:43 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81503">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">تنها اپی که سپاه و نیروهای نیابتیش میتونن آزادانه توش کار کنن تلگرامه</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/funhiphop/81503" target="_blank">📅 00:03 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81502">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">ترامپ این جواب سخت ما چیشد خوابمون میاد</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/funhiphop/81502" target="_blank">📅 22:46 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81501">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IB24OS_RZuL4bZGJyK2QoIKzRr9-mh_HKHoWLMuRnj28qnJmBhRvpgO1N3uZodLUdFsKcYxvWnt3AHwj7ZFa6C8LBcwGEkiML_PaAzayXZLAtme_GrtGZ0IsdgUSEKgcFZQbtx1oBOPFCi1zWt5bOgqOlg0wSLifmH3RERg9UG_k_XT4cUd_JOGmPnI8pM1ljjnqSdigqVGTgujThDGeNKNaKmL58u3XF7leLBzDO5Jpo1ZRL4ruPzVtmGZI6aQo5U8qRB9wgIofZmIiYQky8UIx0GpYWSUz4L71tvz7LMAo0HlvyNwd-uKLKpASDSLwHquiI4K7TWsdOt5g8ZqqiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برا دزد شدنم ۲۵۰ میلیون سرمایه اولیه نیازه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/funhiphop/81501" target="_blank">📅 22:16 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81499">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">نتانیاهو امروز با رضا پهلوی دیدار داشته
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/funhiphop/81499" target="_blank">📅 21:16 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81497">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S1uP3jedB3M8W2sahAAT41S_PL_R6HZTlTiSDV_EeeqMK54g1qbLXQRhO-6hsTT4lA0QHs0Tu3zkn3L-sirJmj6r1qk1Wd4oeK5ILWY0GXY9lJGnI9JaZL3wQG6C3KobRa6Z97qR-9ZcWooUM0iExVKY8XmXmHXO0pCQh4268NQ4DdEL0SYYSlw5fQwv7MrkYwXDzpFPguoeHNArXX0lO6pXSqZEVUI_Pl1KnAKXbhqtX2ApshwdBJ7TO6JFbHt0ImCGWrXWHm9EIOfZNCelbk3-mfr41uyMxUV0xhF1Zw32HiTKKq52ZP2U5CeKi36-G78PmojWofH5il1oPwHGZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پشمام چه بامزس
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/funhiphop/81497" target="_blank">📅 20:46 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81495">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y1m08W9e-hbA8u6hzuc4UGcfPCVIevY6b-J9R8cdQhp11rjP8awYOD4G8T27POR-iuXuFZQYVmSKu6Ut2FI94DfBhuwae8onH5zDa2gZml5t8wFKkLEAwJaI1LYLH9Y-YBaqBxAUI5LYQX31S_1bgAGdl7aXQCuQgyM5yvGcLjwetGezgU8wIwgVhGgPtViPF7EdbnqeZCZFLUXlr2_guz8_n0-0ubDoz-YSlp1jA_CjjpvOqeVPzte1ThVK3bzvbWwcYlQP3f2QT54a28ikJXKVVsssxgEZCFgKreyT_x54Ui-DrmMPAd0Np1QNdN0sHOJNUnnLK87EFVfnnvrapA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی بچه اش رو دوماه زودتر بدنیا اورده با عمل که فقط تاریخ تولدش روز رند بخوره.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/funhiphop/81495" target="_blank">📅 20:34 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81494">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gGWSYUwycwG-VKfiYxUMG7DejsTx_IyaI54QKHbbPq6ZIMRCx0CsnVuTIqRS9D0TNrIuxvLGw7y7tIo5hMoNSb3FLfG2csxG5JPW2MbGXQ8cq1Y4W5dS6c6TUS28aYmnXlxygs6D-eTO-J5PWWMVrQHpcFSXjuXckIb26wTtVpriiGGNMe2_pc6cFOS025MX5cqk3vSd6OnF_v1U2f1ZXBHcvmcOdUmCTyHmeGQ53mOlv0AcnGJ0EfNopeWmziEH-qvErUR32ty2FwksjLyIir4CZWeR-W4xU1V9V0goK5XwbusnLFN_FQGO2ChDnShcO3S48P0Z4yX6Ha19gmvu4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اوتیسم پسر کوکوریا عود کرده، بخاطر همین دیکه موی بلند جواب نیست و باید ببافه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/funhiphop/81494" target="_blank">📅 20:21 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81493">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">پرایم هیچ بازیکنی اندازه رافینیا ۲۰۲۴ بهم نچسبید</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/funhiphop/81493" target="_blank">📅 20:11 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81491">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">از وقتی تلاش نکردم برا باز کردن پیچ خوردگیا هندزفری سیمی کیر رفت تو زندگیم
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/funhiphop/81491" target="_blank">📅 20:04 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81490">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">پول ایرپاد نداره؟</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/funhiphop/81490" target="_blank">📅 20:02 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81488">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mVSxsTN6NceuG8b-i-uTCb-BtrEQUJ5cc8IFtESUMk-ZUl_7jpTzWpXe7JFJ4Ob95vS10s8z89wf5FlZR9ip9ynIvFieECp6a_plWd09tnGCfKNB7nOAHeq4QLP2sUimxDQ9eIJGLEz0haV8QxcJsc5CnTR1QL6OZJQTfUIBf1zwAGfvWpShVb7bvl1n7XJiykLYD3ZjZkk0qQzuq1TOLsohi63HPEMr4IcYlcZrgB2Qd8PjMKSDxeEN2GC_dkOz89Ydb9veWVoqRZmWVAUAGl_U6xfAU1pYPpJz7Dklj5nWWwF7LvKaNo_it4eT4n3_lV-sLyzwtFss2407LlYCxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jrw_aUXBM8NbRsa4nMGDs8lRksuF99toMkWd7YvIVFGU4gIeauhD0LeIIyTVN4eIAGvYlJsaqjiQjaWv2cnivYUJHVlA0_DkERBFjM-mcW4IgLjPED2QohGtUD4ik3bwsLSWl0fzf0Mx4BsotBtQC2NFrE28bZ4HJWXUpqi_i-_iuM8VFGXm_TTp9a2N3W5Y04-XhSSMf44M__ruma-5XqgLZLLK0uDfxiq7afPuNX9wfNHLOdtBaiVR4M3QCFqJ84kJs6JQ13MpJtr_nRVnejEM6LPYLlhg2m03DDO5m-4z91F9jdslRyoCtvAfgiciFgmxSpCNIycG1WLQOjngTA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">رافینیا شبیه زن جنده ها شده
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/funhiphop/81488" target="_blank">📅 19:58 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81486">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/d97nKlN67cfFz-OXnnGrg-oJERR3d_H8xYnf_9asw0swZQfvjx7eSd5Xs01Xfor19J8iEKlQYl-uNz9VhvOif8k3InkpWQ026Hc-aEGuE1dMsgdz_w6RjHgRb_zLsIwzOgOoZuWsZLbtbbOg_HwdpMcYhVeMy5MTbq1AM56b9MKExxYB5peTyuAH7CgOQYmhOb0_nKDwU86E__OjfnpXteDlK4MtpGMcLQiJLmg300UDNdj2rqBQhC8-YZZEz6sjPxXmKwce9KUAAy-xoCgzN78kNrYvlNq0meczJvN3-gHpmJcr-juz8Wi0ixXwP_6LKadkedraBkno9OGkWzoCUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/j00kh5Bo224bleMzMpViQjazPx5INnFEG8WGI9Cywq9C4RQ4yjNoqtnPFq2zCQaNbETlKBmcBGIjimUnOIX0iEWzLYQdTw4BsiFOPy8tt6OnXK2Tz9-BvqpkneIe9XBn-LpytivnZijpIfaTkCc6ujpobwU7ivy8qk8yHQc7eLk9M_yhn3yTV2BU98l4YoTsAI9cVyxORo_5DQv895pe7AOiuQbhPTT8y4lDOZWjyBFYoMNA1HavylJu-XHsgWqsyr8i7JtXeUzBiHKNrirU_xAQdh8gUNgrvqc4kmKkGhQJzljlC3-DA8hK1ODG7uuNv1sxEg_jlYhUClIStj8vJw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">هرکاری میکنم نمیتونم با قیافه جدید وینیسیوس کنار بیام.
@FunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/81486" target="_blank">📅 19:22 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81485">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rDRCDPvXUyxFzTsdm--cO6Pu9sZHVcg79uMa5vLT80TG_bDy4EG7WxDB9HstnjtgKaf96s6nIiLzyI1-L1w_eVpO2QW7q0q4bPSk0sAvxRatf8sGiKSNI-yGO2Eph1Y0r9XNCQ90uKFOCfDio4gB7r_Zn4gbg2j96r1hOHbyFVaiV0_g51yoquXTXImH0m_tfIVRwbxV66Ns7b57bKiC-MjNBV1tbMHwtPF5e740-E5mO_s6kjELZoxGemlai5eH-_cCTX_SU-GRPwbxyLyVq2nSlXwI7kciTzcjhXk8Ag7Fvd-iMchFrChH2oyKQOL8_ES8EP1jZtki8tQp3bPRMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چی بگم والا.
@FunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/funhiphop/81485" target="_blank">📅 19:19 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81484">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MullVJBf_edjSkUTzT5DuzACuBMMtlb3EKY7gda3iKzx1RwmtNgi-D56JIiDt0OhzW_OzVWkJ5mARpKGIzgGtj4PRsQSZtYcOFVMF241--ybqsM5n1PjV_qgipxFLLvv7hBcXEDq6ve71jmraPoJV8gYqTeBuoSKGGGK2KBdRCeAnU9kUaBy8WchXL4y7X7WB3UhWeg1Q7E5x3JXtYRAhZ6Ojm1C2MYZXhAYImMTmdegNWdJ-ysT5rYQq9wfXlTpUivDCpV1MAqn1GYWiqDJxlqknGi_YsML7tpztkw3A5uPxOuxY1uhMJRukREcqg8qeYvk1iPwsdLB6zgaixSmAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽
اتلتیکو مادرید
🇪🇸
-
🇪🇸
ختافه
🏆
رقابت‌های دوستانه باشگاهی‌
🌍
🕔
چهارشنبه ساعت ۱۹:۰۰
🏟
ورزشگاه سرو دل اسپینو
🎲
با بیش از ۲۵۰ نوع آپشن پیش‌بینی
👆
ضرایب شگفت‌انگیز
📊
نگاهی به آمار دو تیم:
✅
اتلتیکو مادرید در ۶ بازی اخیر خود مساوی نکرده است.
✅
ختافه در ۴ بازی اخیر خود شکست نخورده است.
📈
میانگین گل در ۱۰ دیدار اخیر اتلتیکو مادرید ۳ گل در هر بازی بوده است.
🧠
تحلیل خوب، آغاز خوش‌شانسی است.
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن رایگان
🅰
r7
💻
@BetForward</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/81484" target="_blank">📅 19:19 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81483">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UrJ44RfRA7LxytjBXN9XpTG_44SXUj28WDfoZ1VLdcFYo_8rTN-eGqaa5ez6SGp4h22_j7zLk51LjYz56qC-DL5HNxqgdSpJAu-zDzRip0I-9rYExF0qQfr_nF84lf6QXZbo8LNY7vI3KJzY9Th1q32aZ3TcO1GfAd4kV43-626yl303qX2MYq04op3mFGOaKIbHMUEeGDHaBBVK8o9CSMaUsckZgRJX59Yea6Lu9Xb_dcDKdGsqMOUb2oBpipfw1ZAL5v0jKqFF1t88StKUMPIviKV4dZSXHzrgmHuubqNfCaPnENYou3zCMNHT0XvzO1qoPYzmEfPGpVoZPx4Pkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عکس جدید صابر‌ ابر و دوست پسرش.
@FunHipHop
| artin</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/funhiphop/81483" target="_blank">📅 18:29 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81482">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n8bdeasUkFCI_0H6HvgqjrI8Kq7V5i9tLtydHv_ZSY_7jdcFOBjZviFhwv1am03jseYDZm7yScgRK3A6hB--lpbCeoSDU1f-OwSTNGlXhRAatHfpeULUeYshU7oJZjw42OMqYseePMEKlmpGUSXnMzHPNS4JHdJTZcW6ku_G5B-6llZ6j5fgUJ0s47qpvpzt2njPQbEu4Tx6XdVpZQ_6S9S8Lq27wQYUjtsuvF8OjwZukdmCWdzqFXrtEorKeer1RFwkEPv4dZs-g6SIbNRedCKAgvHtIt_59a068BBqGajxx9sYPWQa3W3s2agrhzmL_H95k2o07tPn2fBfZ7PiWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پروفایل پاول تو تلگرام:  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/funhiphop/81482" target="_blank">📅 18:10 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81481">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hpidAJQMRi7nTLoSxP2XWN6DtJitzfGpq7JynvuogR7c5Al7nBSfKE1WnuTdRTrEQljkrUmBjm7dTE5g4GyusULIWJDHfj4tbDyTVTHhbFrU3QGSFo05RKWm4dq3EiR3syz4XJlZTnd-v5nfeC4EvzK4hLu5nD_DZhESmQoC001cIVvTjAAdU3YNt3pJ-CpjvpP7_oCPb-lrU9aCqKN_qj8hVmIH-KeKeO6QEmICBpK2Btt3ofbyf5EPZ7kbvXdEptIxy3OD0Y_Z2YO1uyn0tz4ooTobbO6IGSLkqqEaBhn1R384nJcoZj1hESihSdfniom10pDNDwe_Ca5gx0iFkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">واکنش دورف:  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/funhiphop/81481" target="_blank">📅 17:39 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81480">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">عاشقانه‌ی جدید عرفان پایدار و شاهین نجفی به نام "داشی" ریلیز شد.
🎵
Spatifay  @FuunHipHop | Nima</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/funhiphop/81480" target="_blank">📅 17:04 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81479">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FSAxT_xY1TLCTEVCQSW5dy4sooUXcev4phKtVM7TDbGY7KD_tjHKF1qocn0aOH0laJ_TDMcUSyujGcG9CwplAJnCQbcJZrgNgRPLGyuABxOgGL-PwnBMTnPfaVt9Ae5SG8arOTffixkBPjzLJ_ez6KRNapsjvEqum3HqQjWyHhChkDHNAgz-x0SBug02cxGTl_4caIo1ra5wJXUNT0mOlHcAa4pfKXV4bvOtzwMFxF1Hk090tLnoXPasG5La_hmg1kn8ptHHgdM1qvXlSYw5vtKsA7fjLKI6iBRGwV6YU6mfj6eKe-SmBFCeUazjARLH34bG_IyvBuS0I6k5XREIJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عاشقانه‌ی جدید عرفان پایدار و شاهین نجفی به نام "داشی" ریلیز شد.
🎵
Spatifay
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/funhiphop/81479" target="_blank">📅 17:01 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81478">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v-36AbRMF6YL3O2OMVlNTxrzFjm-OSJOeMGG-XZLVFKLL4emKWKvZxBK8D-Zw7AKHzqk4oQH8Gi8mtyXn_8wlx7NUc_JXIle5TZK6ZLRM44GAqA8nJw6mweI2YOQe_40XlvHREoS5EeEpUe3UrY6BP5SmCtK4Oo3noO1vgRK_Ghkhtv9LyET0TXqApduQ4HJz7Q71vRmlxLytX0NmPw4hZ-R6yADXrUlNMEdinu6c1ibott3YsIC9CtAQgfAXympsV2Zxl1rsrioJ9BIxqlZk5g6KMGDm114uuMxp2-bo_JZi1wPBybu7buOHhp570vyW5iWLBpqNxTkT2LPhvfpPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پاول دورف داداشم، به اتهام تسهیل فعالیت‌های تروریستی، از طرف سرویس امنیت روسیه تحت تعقیب بین المللی قرار گرفته.  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/funhiphop/81478" target="_blank">📅 16:26 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81477">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">ترامپ: ضربه سختی به ایران خواهیم زد‌‌.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/funhiphop/81477" target="_blank">📅 16:03 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81476">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">منابع نزدیک به سپاه میگن در نتیجه حملات دیشب عربستان و آمریکا در عراق، تا این لحظه دست کم ۵نیروی ارشد حفاظت اطلاعات سپاه کشته شدند
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/funhiphop/81476" target="_blank">📅 15:53 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81475">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">اسپانیا با پخش اذان از مساجد تو بخش هایی از کشورش موافقت کرده.  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/funhiphop/81475" target="_blank">📅 15:42 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81474">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">اسپانیا با پخش اذان از مساجد تو بخش هایی از کشورش موافقت کرده.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/funhiphop/81474" target="_blank">📅 15:36 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81472">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B2_e-ZE9JeNAiuBKfPQIkLGbP8KL-7Hf-1vdso2LRLbCC80KmUOEJurzy7jqTalLzPZKP_aWqwjslktl0BGRpvYIQUYydATHn4RqtClbHX3AwLRR91_hYyu9tgt7Iu4gzAMVdeWfXvuWdkbdgqJcaiXN7KcxkklH0i2Ag_JrulPOz64Ca3GQPgpjJpVEuOehimLgK1POFPNIN4e7H7mbDuSMmnCUJDWdeT44-NLdvQnNew5ztWEgkbxwrMMCMAFypSsaFXZJ7Y9XFlghvc60rPX3ACbzMl0SteRVca_YI3o1wfLPfobHLJCKqESld09b5cneOjMnN0iMcLqbNvXa_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هیچکس نمیدونه چرا این پست انقدر ری اکشن "
🤣
" میگیره.  @FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/funhiphop/81472" target="_blank">📅 14:57 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81470">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jytC-YyYeRNKSosmpbP6VpdNRba1BXX0TpF31oepnCY3uQmGQch0M9cvN0Spq6cciat7wKfirjY4FFIxmJ8UQyp3voL0giRh1Qn-Lank_TVbuY1qNCO7cUrB1FZpFia9w8G8gDCmjVH6Nf6Oc-zS8HhuGYrKOlzRXVI3YP-6gzQ2sRNyCsNGNfoJ2aRqVTjq1iKReFZTEiz_hfbiE2xPexYLb6pHDWH8NzqmFVQPC6c6iGC2XCzm-KxgaT3JQXiv4x0Ez4D9WaqeiCs_i23JH4eAhSYnQoC4zWeXXEMJkNYf3UZe03p9DBlqH9k8SlM09ebNSR-rdUxxw3R8wg4g_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ma9C4wviAc8gPaS-Sv2kmnI8v0n_q_yvv_g5yt9_I6QUe58u3SjI2ZpZyE9exoK9fim80i3pvkzQSzyHQaijXQlfRZboA2nu1pRpb__MM7UqFqlbM-2-BuDbAl7UUF9Alu7LL0cPx1h3TObbUaHIUoeTrUrOXEP1VZyz4FK91zYcl0fikmm4p9BNra-VLw9yN7-4yFzXdzfJXW4xcj6P2_efgPWPbTeah6auEDGHpdtJycvLM19DjuJ_GJDiOUonyKid2H_PLHTOmS_T_6eCDQ9EirWL9m2CN6JyklulcsCq-JL1R05x8563hOF3xpu3HPE7A3mTMvzpdKRsejatCA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پینترست چرا تبدیل به کرج شده
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/funhiphop/81470" target="_blank">📅 14:35 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81465">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">اگه این با سپاه همکاری میکرد که الان همه تو صف اعدام بودیم</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/funhiphop/81465" target="_blank">📅 13:41 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81464">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">پاول دورف داداشم، به اتهام تسهیل فعالیت‌های تروریستی، از طرف سرویس امنیت روسیه تحت تعقیب بین المللی قرار گرفته.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/funhiphop/81464" target="_blank">📅 13:26 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81463">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">دلار 193
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/funhiphop/81463" target="_blank">📅 13:08 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81462">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EPeh-4kzIU0sLYheSA6q8IYCZYioTELGC0c51WH-m2BoJGQdVRGDyVXVhsIdcK5zlLrNlbdBELOMYCVGUWcAgAhXIb_AzpuWA9Gm_C3-RtsOeqar5UA9IEgghAUOejNPDWi898BZOD8khzUDeyzOH8JiCgRzHSMFd2UljhknDGX_wTs5kp-q_EpXGFFH3GwY2Z_7bXqUQadlRdPUDNSA2kxxfBrcySmGcIUnBdNSe2HrGCg5raWgxOnebh3Hk_5xpRpoT69KkJM-znwjVQg2jY-qNeKF14QKOWcD5S6Z-45NhjGwIqrq-DX8__dz8GxbF9udQ65aL-00uAC9S-h9EQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استوری پیشرو
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/funhiphop/81462" target="_blank">📅 12:27 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81461">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NrUVTMcazHm0K8xh8JveEaga-_CnKVeKc5p6MNQi-MmiNx6InEWMlpBV2PXZxnTvFwp8UFStq2mzCAXKnSLiVEhDr4vsDziFTsXx0L5lGeZQKl-KtFmWatBhoUNNI1m0s6N-Un8sWBS_rAY5XhHx7SzPD8jqt6a5EszL62YavzkZSdxmRKTjHg41UDio8nMe5ELz8LbbDl4v6NxnBR5xsGq3xcFwYiFN-SnuF6n0TPW0NwGthAzEORbRD2k9RmTYC6bOTdEyVqLbTbj6U3ZjfT0HdfdOhZhPaGfCdGfABhkbnRZShGs-OR2gfO3feNgRf9NwUkcQ7ZNi4y0a-V6Axg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽
اتلتیکو مادرید
🇪🇸
-
🇪🇸
ختافه
🏆
رقابت‌های دوستانه باشگاهی‌
🌍
🕔
چهارشنبه ساعت ۱۹:۰۰
🏟
ورزشگاه سرو دل اسپینو
🎲
با بیش از ۲۵۰ نوع آپشن پیش‌بینی
👆
ضرایب شگفت‌انگیز
📊
نگاهی به آمار دو تیم:
✅
اتلتیکو مادرید در ۶ بازی اخیر خود مساوی نکرده است.
✅
ختافه در ۴ بازی اخیر خود شکست نخورده است.
📈
میانگین گل در ۱۰ دیدار اخیر اتلتیکو مادرید ۳ گل در هر بازی بوده است.
🧠
تحلیل خوب، آغاز خوش‌شانسی است.
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن رایگان
🅰
r7
💻
@BetForward</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/funhiphop/81461" target="_blank">📅 12:27 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81460">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">از الان تا ۶ سال آینده هر اتفاقی بیوفته ربطش میدیم به جلد مجله اکونومیست
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/funhiphop/81460" target="_blank">📅 12:18 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81458">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">هدف یدونه پایگاه آمریکا تو اردن بود فقط
💔
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/funhiphop/81458" target="_blank">📅 01:23 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81457">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">تروخدا اسرائیل باشه تروخدا این یهودا خیلی راحت نابود می‌‌شن بوم بوم تلاویو اسرائیلی‌ها مجبور می‌شن از دریا فرار کنن تروخدا پدافنداشون ته کشیده ۸۵۸۷۴۳۹۹۴۴ نفر ازشون مفقود می‌شه کلا اندازه یه استان ایرانن ۹ میلیون جمعیت دارن کلا تروخدا تروخدا اسرائیلو بزن سردار
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/funhiphop/81457" target="_blank">📅 01:18 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81456">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">ببینیم از لپ لپ اسم کدوم کشور درمیاد
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/funhiphop/81456" target="_blank">📅 01:15 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81454">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q8Js3l7D1FsE3CN7TFG1NeegoBo39koG4jaXVin8164ey6Fid3DhZuTq9M2RJAhA41odCvdai3buwwBtjnl6GKSL8HOSOhB48wcNVsVcv_eQ1gTMSpacrJWe4PSI52SpijUTf-cxZiy8lSs1vSqeipNUpxspnN_Ou46rCmoOEJFWoyr8E-b5lzNSzXpQCYv81eXWtp24uox-CZ3005vLjPUZ9AlpbD75MYIjRiccaryIPlmj5IgVV59sC3zKQ29BVeH3m9EPYWnOUFuMP2pNCEryx1-zqR5akHQGv95PL-3DlCQOHy469DJ4UwivhcmEXffiVvbF3W3-V0Q8i8DdXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😂
😂
😂
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/funhiphop/81454" target="_blank">📅 00:45 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81453">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uSOULTtDkhfEZs_YcgVl8n13R9pJvv4FtaCUrKShvdGs0-8TXSjuUBy-8zdedmqolrJQP6mi8wgChqyDQnVfIWVMkJZuK4cqKAtql2TzuvW4YvpsA-fY2yoSvCqIOSN78xLEC-XwHkBbI7gKYe8-Os3ATmfQZuheyX9s3qHB85KtqQId9PGFfb_is8geL21R4CayReeSwFhbXnxR6kfE1Zz0S8sEJvUT1rql5BtP8g0v8o2rRxIHWZQfAAjWY_4LWDfxSS4XUBXqoBI078xWovf7ATWJPJBXbWG4wzS11Em15XmAKjWI9nGDYe6TFbvLG_Wlwo3nRFxHzszAIk8OPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هرچیزی برای تعریف ساده کلمه نیاز به یک توصیف ساده و فراگیرتر داره، مثلا خارجیا وقتی میخوان بگن بی طرفن میگن "من سوئیسم" تو ایرانم هرکی میخواد به یکی بگه "جنده" دیگه این کلمه زشتو استفاده نمیکنه، میگه "شیما کاتوزیان"  @FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/funhiphop/81453" target="_blank">📅 00:39 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81452">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vPkpnWjpa1jY09mP9S7Fijj1Hx49AhYub2rMkomjttNiKOnDzLj0zyE5CBks93yksh9Z-dUOQn9ga8zPHmcwrwSS99uNeLiBdCpF9Y_0RxmfRM2lQSjUAX3Eom_XM46t5lWzyZZWPV4tuW4MQLKMLxd283ZWd3o9Sm5DMVpy2dogQmN9e4IBaSMf1Iromkclqa53bT86nDqrdLU5BDIDL-6WujA-6PKtnRjD84simD9gZIB9GWaknTtC56Pg_uTEb__nxaSRwELenYH3SaoLVETxHpb7j_fzUFdw4moryGG0IIsiFeAz7LxuVyy-WPT3EfiVSWGDfCknSw3GvMDs3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هرچیزی برای تعریف ساده کلمه نیاز به یک توصیف ساده و فراگیرتر داره، مثلا خارجیا وقتی میخوان بگن بی طرفن میگن "من سوئیسم"
تو ایرانم هرکی میخواد به یکی بگه "جنده" دیگه این کلمه زشتو استفاده نمیکنه، میگه "شیما کاتوزیان"
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/funhiphop/81452" target="_blank">📅 00:32 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81451">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">#رسمی
داریوش ترک کردهههه
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/funhiphop/81451" target="_blank">📅 00:20 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81450">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IaPHHHQaZYDJwr-hpAtaW7V0M5bit2sa-B0ovdLUcSQhrtqRRMG3H8bHSanUEGpCGbAN1f1Aw3PMO5ntF_RPDD1TYIEinxuPKf_UXgicBPY8ayaN5xVYHAhvZ_0lsVLcywFiH6a0docjCvdaO-oROvZkKtWhNNHE_xTkb0K-UbclKAIGfHrfoK3rDBSE2gXzwtoWhQvzU58yJFZlVtjd0ME9ZQAk4Y9nqoRanmLwpCBNVCNpuZMRSIL86B5aQ9Qn_diEnqmFLxlXHY-oz3opoWTIyJKEYdSPfk0ObnKxEuwKemgn03wmc9vZ6uXB0oWu97AZ8IJuWZQw9J_OKDkWyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حضور شاهزاده رضا پهلوی در مراسم یادبود لیندزی گراهام
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/funhiphop/81450" target="_blank">📅 00:08 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81449">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">یعنی جدی عملکرد ترامپ رو تو اوردن نفت از ۱۲۰ دلار به ۷۵ دلار تو دوماه ببینی و باز از گرونی نفت بعنوان یه موفقیت حرف بزنی نیازمند خیلی کصخل بودنه  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/funhiphop/81449" target="_blank">📅 23:13 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81448">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E9RR5D6_FbxDSLicdXlr20CT6z1pQ6Byt11W8y6mIcr4PUm1cNrMmuuXzyg6IQoPRY1FTqGvsRUitwuoiHJJqoG0BVFVc-UOT_v30DCabryZA81JTn_rCtIuPqpuUiXwCOR2I4sdiHQVJuAh-tKubdoQCVacLJpa515DkmiksG-gdCh16Q4vSmPtBXg-k4-RxedL6e7B97qzsSc7YmoxrDredB4WVmPGFFQVUyFBI0aQCHfPSKzZlZxHbCC1ACnQTSfvWVWGRN7bEpBUNnqqCRcWDEFYgwhLfzznacb2R2Ertay_m9pqiXaNXVmpLHUODvkKpRR-TqM9Iwr3f4Kklg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لاپورتا سکته کرده، اما اعلام کرده که حالش خوبه.
@FunHipHop
| artin</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/funhiphop/81448" target="_blank">📅 23:08 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81447">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">قالیباف: دنبال بهتر کردن
زندگی
مردم هستیم.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/funhiphop/81447" target="_blank">📅 22:48 · 06 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
