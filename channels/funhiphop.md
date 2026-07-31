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
<img src="https://cdn4.telesco.pe/file/FwMbNfb0YRK5Kkw3STtzOUI1UI0qPGYSPc0YFo35a4GV0d15W1TRHU3huPKx5RS6TOW8j79_nvfmcIOr1kOHY2FOfgZEGm3esyOn3OgH784j3D5C8g_VgtrELnOwkzQPjqIoJAEBsWFUzIlfjiJGR-zka4bYktWgq_CPDiOQG9ZBWXOhFMeWnaaq64zbvwSTjLEz965Vfh87TUjQnrDMpnGhfGp3abHnfKzQQVyU3s4GJQBZEUHrUC_cJaE1xlzF-ubH9Qgaebgo4b15clP5D06b49dEn2wujftBBhscnljvA_b1OEv4RDYM_20icnU38osiYlB1aXPAWeUXDTlsKA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 226K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡صاحب سبک🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-09 12:12:47</div>
<hr>

<div class="tg-post" id="msg-81568">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bs2sN9GkFekfSMmkBuYa0sOKgEEIvGWwtxRrlsx2rHK-e-6vHDyfJDFvtOB7ndLoAKRlE2Wsh3yqxRrzNQ-dimWkoAzye__JvYjLhyZKBFqOFCkzowsNl-0bod-_ClVjWDtCIoXNKq4VDwhc1ltI4EEWYyDP_-9aQTMfT1D50JJ6Z4XBYCF3CGdVjPYjpE7WNvTq5TwKSnKg5gVQ6w2PLv5Fgu_EU9WbfDMhY84-PmfcCaDC0IrZhtUdN-p95SolEIQJrYwroQGDTYnSYzfmy6S1nziIzhz4cjTZ0Dr4onNsTGcr1qoYyhOU53IxVrhMZmati-vyORwOdp7vNzcMow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 3.49K · <a href="https://t.me/funhiphop/81568" target="_blank">📅 11:31 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81567">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">یتیم گیر اوردن کصکشا  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 4.57K · <a href="https://t.me/funhiphop/81567" target="_blank">📅 11:20 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81566">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf580585ef.mp4?token=o9gOj2eLRvhsR7qmxJ3xfZQcYchlEDXVu6XAm-tToRp0fPCJP46qfgBXdtpOnfQAdCpmM4ux8qF_jCzzT2wi8LDu64u9ssfrTzl7Aq_uqmpkFlRK-BBp_B7U76sMAHduJbo4gpPsx4SN4ueb869vFEqdjcB4x2WSsYkuYpYyznAK1uBIBcqL3TZerZp6kAMp532MD-ua6fGBLF3M7CjQ_9maVz7hX1OKHHGpkvapAMMPASkfo7SOyy_ign3i9Dud9UOdIeJBnDHqJsOtbB7wcZbDw6kl--nW7hR02XAwQVacIQndL7UzPT0aIuvlDFbbvnCt5yJSHp2nkYohbW9mJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf580585ef.mp4?token=o9gOj2eLRvhsR7qmxJ3xfZQcYchlEDXVu6XAm-tToRp0fPCJP46qfgBXdtpOnfQAdCpmM4ux8qF_jCzzT2wi8LDu64u9ssfrTzl7Aq_uqmpkFlRK-BBp_B7U76sMAHduJbo4gpPsx4SN4ueb869vFEqdjcB4x2WSsYkuYpYyznAK1uBIBcqL3TZerZp6kAMp532MD-ua6fGBLF3M7CjQ_9maVz7hX1OKHHGpkvapAMMPASkfo7SOyy_ign3i9Dud9UOdIeJBnDHqJsOtbB7wcZbDw6kl--nW7hR02XAwQVacIQndL7UzPT0aIuvlDFbbvnCt5yJSHp2nkYohbW9mJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شعار مسلمانان مراکشی بعد از نفوذ غیرقانونی و حمله به اسپانیا: الله و اکبر، ما اروپا را اشغال خواهیم کرد، زنان و کودکانتان مال ما خواهد شد.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 7.27K · <a href="https://t.me/funhiphop/81566" target="_blank">📅 10:23 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81565">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r4FYUBirA2gUbb1su0pI5-FVSnN-klhg4yxr6Nwxm5dm1tbw_O7McDCgqn3_iMyHNxhhqBNOX17LY2XoCEYfWg6sqRfcxqaLmH9HD7T_IF2O7sTKvqNl8wqjPy-fR2ipeONhFLuEaVZ7HEDvHJ0_7Q6-WguozNGYF8B_4GEVqBzEiteufnAEgmwWWMMUiXDX1L2UUfsVkG2cSO-yrcgzA_iBwvNPNWKZ0gOBxSCWCTysnmzSojarFE8TlBWQ6PuvDeRjCYIXrn_BzG5tgke2fbcEzP6ePZpFloPvO3bppH8kwiKqt3w9IySMgJWRvZDAVQs1-fo27FpQq90tdymZRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد از این تحلیل کارشناسی شده‌ی رائفی‌پور، خبر اومده که عربستان داره برای حمله زمینی به یمن آماده میشه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 8.07K · <a href="https://t.me/funhiphop/81565" target="_blank">📅 09:47 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81564">
<div class="tg-post-header">📌 پیام #96</div>
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
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/funhiphop/81564" target="_blank">📅 06:02 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81563">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">اسپانیا داره شبیه سوریه میشه.  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/81563" target="_blank">📅 03:29 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81562">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">اسپانیا داره شبیه سوریه میشه.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/81562" target="_blank">📅 03:15 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81561">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">حماس خلع سلاح می شود   ترامپ: شورای صلح امروز به توافقی تاریخی برای خلع سلاح کامل حماس و سایر گروه‌های مسلح در غزه دست یافت. این گامی عظیم به سوی صلح و امنیت پایدار است.  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/81561" target="_blank">📅 02:19 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81560">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">حماس خلع سلاح می شود
ترامپ: شورای صلح امروز به توافقی تاریخی برای خلع سلاح کامل حماس و سایر گروه‌های مسلح در غزه دست یافت. این گامی عظیم به سوی صلح و امنیت پایدار است.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/funhiphop/81560" target="_blank">📅 01:59 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81559">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">شب جمعه خود را چگونه گذراندید؟  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/funhiphop/81559" target="_blank">📅 01:39 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81558">
<div class="tg-post-header">📌 پیام #90</div>
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
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/funhiphop/81558" target="_blank">📅 01:14 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81557">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">این پست مربوط به رپ فارسی است  @FunHipHop | Taymaz</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/funhiphop/81557" target="_blank">📅 00:57 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81556">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XUgFj8joE6-IMK-LRhtf8_iU7PTPU8KGl-xM_152IrcIr6j5hRyIYm6CZL0PRW6nL0IbJKOCQbLpaXe0SkbuUTpfxrrY7swMPfd31KymP36pHTQvIeivW51kt8Of9Sm9chTaFXhlG7C9FZX_JZDneF-ZpfUAmO5ZeMqekNrHEzxZ63oMVCiVZzdoxXSJhyj6ISMjXw9MLbZLjyg1pV87qSVjxdyrLIPVgn2dnszCuFk3jDlYvAUEn5yNtqXdU4YsJZd4mRKt4GO1BV6S_wJ2HA9BVAQNmcOWoh6Dw3T1etAUHYa4-G-7_rN61jDUqU6TnBaYTPbVhzARV2E5pDJDKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این پست مربوط به رپ فارسی است
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/funhiphop/81556" target="_blank">📅 00:06 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81555">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">دادستانی تهران علیه افراد حامی محکومین اعدام دی‌ ۱۴۰۴ اعلام جرم کرد.
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/funhiphop/81555" target="_blank">📅 23:34 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81554">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nUhcErCkargL9ass_OaizvASC-Q6CJn9l4OiC7N34pOUPrLDxosQuup2zaTiaJTb7p3BhY5SDh9e0KFT5coqWmoZm0JEDcqa7NBGKz_sbdthed535hnGCsFqhXHsadr5ia9GFy7650A9dVqAzmgnfWgf8auxgq4lEOoKZ-_OcwhAx_UfOkMx_22rTjrbXWLhZKdWG7mV16BiBx3yMCQX11B_gH7CvuTJ1GGgITyK5oWEu47sxNaD1NpzrYnADzcNMI8fNplD1m33-Aqmo77TF7AzmUjc2j2GnpvmimH1OHJ5ofaRBmDttbtQ04xsf95kN0cfMVU14stw7Ow5BilbEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بچه ها ده سال تحمل کنید تمومه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/funhiphop/81554" target="_blank">📅 23:14 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81553">
<div class="tg-post-header">📌 پیام #85</div>
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
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/funhiphop/81553" target="_blank">📅 22:37 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81552">
<div class="tg-post-header">📌 پیام #84</div>
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
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/funhiphop/81552" target="_blank">📅 22:27 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81551">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">ترک جدید مهیاد به اسم چشات میگاد ۲  ریلیز شد    SoundCloud  @FuunHipHop | Mmd</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/funhiphop/81551" target="_blank">📅 22:14 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81550">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WWnYZ3Zvr6g-E9WT7DkdxVB_hzLcR2Gkuy71_PD9FGkPITDfKo0bo8RFiAQpn1XktablRIBv0IZFccl7aPPQKQJN6BjMOll2rIQhjzwLr1R6-fu7S4Fvo3nQ5XBxv1UlR5qt-k7Ffg4jd-G4GsN0Yf43hKlJZOBx4flP4FKqMF5hjHw-zMbBYPvi9AhBte7juI7Jc8OqOAXFD5mgcF7HKbEe923J79XsyrRiD-RkY055w89mUBJ3-FbW1-CD_qW1Wq3Yk_ktqJ9zOLd9n3RJ7J-1KeeKS1-y_cpHUhYsv0H84Peh6cP-Z8NsFuF4roBTMhyP9fT1KZ37VtbO7nIfrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید
مهیاد
به اسم
چشات میگاد ۲
ریلیز شد
SoundCloud
@FuunHipHop
| Mmd</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/funhiphop/81550" target="_blank">📅 22:13 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81549">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RZ-Z4N3REbo9xE8VKTc1xZ5akvPD_jf3vWYnAx0iS753r_u2A1BCEf4lVzutMJS3Qp3CSY__pyR4Bfh8WGiTH8YGkuMZ6DNanzzZXQ81ZYz0xOMNNPAt-vHTVup1DhmCThn-PC-aPPquKu7s22LmHDrvCuypagKWAcyYSj4V1HzeSJkcZ193cZtYN7ZHABArNWHMxkehPtKcO_yqIrRuxxpEn4psIYclKUbz27yUeHmNTgLQq8o-9la3eLI9zeEvs1NWCdCPExMCttrl4WcV65zqYSidWvkpm21182qB0Y8z0sN7DtyjHeF6klDgvo-ZPHzcppsy647D52DNVw7uRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یتیم گیر اوردن کصکشا  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/funhiphop/81549" target="_blank">📅 20:59 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81548">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">پیج اصلی سروش ولی زاده برگشت
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/funhiphop/81548" target="_blank">📅 20:14 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81547">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GNrecDBjt9hlR2Hwb8-3B-aeSGnmFESMKgJ-IFq9tF7MDTHN8b1LEw2_LAr7tF7yMULM2KOcTiw_95C-GRgncArIv-zqut_wl3R08Hr-2ZZZpNeAwverVAYAqUG45Cph9McV0nFJxPfG2MMEr0ilxk2f4I_Wk-cbvr7Kl_RCIBcAn8_JnR2t9mO8c_StdFknAaEHLodmyGwychJ7oFEF3pA_tOrDNccjfIvwelWaixv-8BX0Vew0ZinoDWbGl3qPSF5doyT6sRhmS3TMeF1R-7YaeTGZhq46ky007jeHaQIG7gMugYDBnCuZfsbmHUs2c04j0zWgD4ja2ZeyEk8TUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پروفایل پاول تو تلگرام:  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/funhiphop/81547" target="_blank">📅 19:57 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81546">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t-JjDpRMl3Ur8HlQxY85zQqmykni1qkjffldUd5qBDqdnHLwqwmkG6h5_7oxjBSMvUkt4e8DRsoaD4Q4EONm8sjragAUN4rqYC45RqG3-oCtBG11iF_NwfVNbGFdkhRGG5bWkU6Ds-GQsKK8QjcLro5bu0iFOYaX3km7oe5NxOr7ZjVx71S5FHp2WXzLbPs_h8WXhLj6Kh-FumEklnTnmQ3_lFdpxmcBzWXKukwJ5DHgj0FrH5RYzmeEGQv-YDBEpKC0oIwP41x5wKW4PyNPJtlbsUxgKdxRs7Er43F5KfFbOuz30nozOuhSoQT0mY8NE55qF2JxwmhGi3HXQ48dOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این بازی شاهکار رو از دست ندید‌  @FunHipHop | Jenayi</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/81546" target="_blank">📅 19:52 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81545">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PA1KdzsiuB7jphOv-MF4GzR0ya3Dof2S9QYix_JHkQQTPtVKxwTQKSObsfC2sg-AXebnLkXFGrP-pkUJrUByl0nopFcJEud72ZNdGI4t1onB6g5Yw9JaE0pp5SfXG0Gfk5z_Z7-Bitwn1Mt4AcWC20y5vQKlKw8YRFlQ0C8JKnBW4m6RHhPhp1GDjMVr2qkOCc4_lGxoHa8UiSEMhw7LAoLwUG3L3GkylGBDpr4jnQx_8ngxmcYPiyhLzOMAwElrRWF6sD93WnCErCFhR1h65PNzM83oGwkBjWpK9UInz0MxIyTAlEkUVCSc1xWio9k2FfVy2thZF-WatnOe0m2hrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این بازی شاهکار رو از دست ندید‌
@FunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/81545" target="_blank">📅 19:45 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81544">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZPFQwyXdDuOWa5vS7K3cTuO9POXpwMGqUAe_ChBtNsWICdJleQ6KAHcpZLE77fQc8v6AgMF-Os1WF3K1Z-fNNcDkDRLm5Ut4_fKYbxs0ghpMDegueT9mAtaoHidBc4A3hl99D_07sGtBfsH9qY9w7Zvva-_cu3c76LSLkqjuc5E4y0GxH9LqqI6qvEa3refX1vIu_mZ9BK3iFewRROYJEChsaeqIM66Bdgc1HmfePPC5o8jwxAmU2w594pMKt3Qc7Koe-cA2ZmWpXuEY8Wl_FVGO-lpXlxJT0m43JBl2QVlM8x3E_L7jhHEnCfSy67m3XFvFWjlouUkh27x_ZnzpeQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/81544" target="_blank">📅 19:45 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81543">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rfht-Tzh6Z22RE609Hd8O0vAX-9begRmJCLT92qHwK81Qmi8t8x6vKLM82-vbSpfp3JNS5nDUgmSmjPs17xpDPj25qL5DgxWj_ALpFMAfs6du3n8780ymxyXY8G_yA1Ignmd1q1Fy_am-Q1y73Y0hm6Aj8CuxANqfRS5r9BcmwMxjFqXHlBOgu2ydtoaa7BAXIIks_YYgJBMvLglpnKXkiEgLqYJ8zeWtjz0EeFodrB4mY2q0_kdIfBX5hDApj5n0XAMYFvRm2dSJVSAvdRqSinA8uaG9aFDXsLT5ZgpLdZHOsFIpvskF3Twkv_dVYU8pe8gYpYRw6hE7DENoV5hDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایران:
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/81543" target="_blank">📅 19:06 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81542">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FMfzzhz4kePMoDl639qoLgenvD673_1g95372tPyy8ol3i_UZ7j_dr5el4N1raglyDiwur7OBBGegouXaFSicoTjBF9TV4sPQG8_W0tTPigoMW7M3drIjMS6a5GDIApcueg0qMncl2Ezc99Ox7hqtUaLz4GBPmHs6c6Ysd2ndG4SKLA-A1GEyiP3a5mBLdU-BK7w7OAYh9Q99O8tVSmNmutx2g1XWaapBYeR4B_8_u3_fW-vHU4EASHlchs4PHTM6OKJ-3nPdXjx4bRk6JPm89wp8ly9pH8PbrlDv-c9LOt7N9eAVymtuNUoin9kwpoLpgBjg-33nsdIqoYKxv79JA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گلشیفته چقد ترسناک شده
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/funhiphop/81542" target="_blank">📅 18:01 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81541">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kmNHXQY0Lpip2-aVns8BI7shnNhAo0Uxe3DlJnfC1wf97saMHZg7tylUuNUFuiYT27IE_cjLNYa1FzSE2ea525u2npaCQ-0rxaUjarvHeAUwDqncIn14xh6GdWhtxP001UN5zglT0F4evEdIQJmXXXJrdM_i_J24WHFJIQbvHanq3lrPdqmbhOizq32eu4xTSm1npTUVK1Qrle81I58rJxFBjcZoevb5ongn-KuUNI4PK5mrhAOq-izDrsyfFcekE1drOJO1B9N-yYLySW5AXKJCX8SwzYDDN-AaHdMl_eXSRHVGislv_bUL8hxk2Wrl7bsC0F6gsjVr5KYpnMcXYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حکم اعدام بنیامین نقدی، جوون 26 ساله و از معترضین دی ماه صادر شد.‌
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/funhiphop/81541" target="_blank">📅 16:56 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81540">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uFtCHJ59fRsM9zPuzE1unNxXKKuaBv4zHNtRFUYl8NqfZSNyyAqSQV1rZZzWRnK-NOayMjr41nzq_kSi-8a9GT45qtV7mAAfcILJmK-FH7AZSFYENyGZ-iK1_DDlaPDrm696gjxc6d3NHuDlEdmHrnXUxm8_51UxW38-jwcfl5J89oJMt_MoJTWXmrNtvN0eAqUM-cbAyYgMMZwt8R_WBmcNgP8Ltk3I8QsCfZkBv9_yxNakxZkOE8-eCvtn1DLvYpGZ26arheB2oMHrTPHiei_x9MFO2Tlh3E3c7jE0zOm4j7Y1RmA3CovgIaTQvxor4hCcMLcthRTpQMyx6730sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیج افشین فدا بلاگر مازنی بخاطر استوری که برای سه جاوید نام اعدام شده تو اصفهان گذاشته بود بسته شد.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/funhiphop/81540" target="_blank">📅 16:44 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81539">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">از نیرو های مسلح درخواست دارم کره‌ی زمین رو منهدم کنن دیگه زندگی کافیه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/funhiphop/81539" target="_blank">📅 16:30 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81537">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hQTXbL4Xo7ALsL7qUZthOavI3AfkGa6NbRVdiDNB1U3-lEcNxKq6Vn39qDfTxTYJSwCcxhXsS93QuMrUTbNoOO32xNYWyO_iNqDFRW1lgK3AB1hBr1XO7-5HNT5yNNnfX6nBTIrsE371vEjVfQyGtw0D0benqj6xyZNrmmsGtJ0h3Izky0AT_rKHZYCQUfR-n62UA8viF1gRze4lClTk7WQT7RVcLq-OJ1dqMfrIuUe9qBee1fGLsPTEtawRv7MPkB07cpp3sZLql7F1Lqccivj8U2TxVml7IEThaST2j8iHmDUL-bRonRNIBVeJTwYcEJhcoHkkis_tNGlZQFmjJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آفرود سواری در کشور ممنوع شد
تصویرم از وضعیت یه پیج آفرود که این تصمیم دولت رو به تمسخر گرفته بود
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/funhiphop/81537" target="_blank">📅 16:00 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81536">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">اشکال نداره چین میاد بهترشو میسازه
🔴
چین گزارش‌های منتشرشده درباره برنامه‌ پکن برای تجهیز ایران به سامانه‌های پدافند هوایی را رد کرد و نادرست دانست.
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/funhiphop/81536" target="_blank">📅 15:47 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81535">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S9A08qGFM4a_T_a2pr2LVcxU4rFi-DagZI3G606faoILOaH1pPXpmlIzfeRVyTXDdu12-JIvNjG9xKIE1157tYru_nfkjXLfgPUbbfwK0tzdLCbzccu8YKslaHRwzIugcuu3wKssoUls5adBLEwigVCJJjGE3nsI6bCVn4Ju17VE_3TOzSytDp3O6Me7dTM6DHqGD7ix1c-E9WnKjC4_Zj_kN1EzMpIZg1r9payrA5oLyxzR6rmzk5KevcwZtKRAH-JQlBOd4XhAgmGqj0VODZWRKzzuFiuuAxy0yzlM64kFWcT4kC_27wj7ckYmMcmZAHO9_W-3Td53IZyb3ck4FQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آماده اید؟
صداوسیما: امروز صبح در پاسخ به حملات آمریکا به ایران، 6 تا جنگنده F-35 رو زدیم 3 تاشون کامل منهدم شدن، 3 تاشون هم خسارت دیدن چند تا از خلبانان جنگنده هم کشته شده.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/funhiphop/81535" target="_blank">📅 14:42 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81534">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MKk1TEJYWgVSny44wkuOSt4LEbnlNfy-wNd2-eE083jLO7wF0JWPnsW-0grTH2rlaU7pUhetjgm6HvkHGg_Q1NO3yn7O7EdiIZDInP3cImpFD3xWJ4dkr6nrVlWpYAypW_TfEzISSiUjdFu4jdwmWOty1Fb8spTmRJx_7zfG-OLdqHDuVypg8yDe0Im8TvpgGre3NLyXCCDeuLs2kodn8ExNFmrfC94y__D7-TV_iNQR857mviUCAAvMp4JPydfvrsIGTPBtA--QS3wZS8XCSLTEX6JNErSugD2QWEawtoOLtsCoI-wesL1LLEDdh-qCddpnlUxUe-EwweaSptUVFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دایرکت یه وکیل دادگستری.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/funhiphop/81534" target="_blank">📅 14:05 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81533">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/533f3ca2cf.mp4?token=jZ0_qAOp7j_dn39p13M9Mh4GIN4OM6uz29xX1mrXtmKmg3gHO-aRR2TKpEj3K5Se2krsEoPHnrd0jxevw6zoaJqw9vWdcdPM5IhqckBKes4GaXI0J9r5RgzkTHXoKrQqUi3U6z2QFenlT7DH07_no2WA-pn6cpVULkkh4DLNqEvaXSIS1yFRKKmedAHT8SIhbcn2-8KcdNmCicBzdKkXt3JgcL5UXr4DIqk_xjRiHvK9rB8jh9yI9SWo1cYaR_VdkNAkIneOZDGNxltIhvXl6uHlJi_HOAe2Q0lty_ehNmWcnp1EeAco0P3QxtcA7N6C0yUPywwhWHKYjhrot979X3BEUhcDDhxaNWP8C1KZF3QUubMvvgatA_SSn475AKFvnEX6u9JxbfjKqI2YDw9ACCVMy0um-IYAIbM5HPYaSLzGUKlEMYmE7kIbs0l_z35fguDLjKp0x_VUJ2xOsiBlWA8pUmVb6wKJ6uaaSfgwYkK4h22M5jna5eZmD6LYCBZRXE0IRbSIK8uPmBROBh_LBnwY6_9fyx6mPFZvwtra3vUU8yWT6tC_JoONxjClXEdwpWX1tP_lgYs-b7sXHJdMRY1hJpYcAa0h8vbjh0yYzzyUxsaZqJHGMd3E2aS7x3EHOnotp9q7I6Ft4mH3CeQNILZ9yuN5b_Kvq_dlNEupntM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/533f3ca2cf.mp4?token=jZ0_qAOp7j_dn39p13M9Mh4GIN4OM6uz29xX1mrXtmKmg3gHO-aRR2TKpEj3K5Se2krsEoPHnrd0jxevw6zoaJqw9vWdcdPM5IhqckBKes4GaXI0J9r5RgzkTHXoKrQqUi3U6z2QFenlT7DH07_no2WA-pn6cpVULkkh4DLNqEvaXSIS1yFRKKmedAHT8SIhbcn2-8KcdNmCicBzdKkXt3JgcL5UXr4DIqk_xjRiHvK9rB8jh9yI9SWo1cYaR_VdkNAkIneOZDGNxltIhvXl6uHlJi_HOAe2Q0lty_ehNmWcnp1EeAco0P3QxtcA7N6C0yUPywwhWHKYjhrot979X3BEUhcDDhxaNWP8C1KZF3QUubMvvgatA_SSn475AKFvnEX6u9JxbfjKqI2YDw9ACCVMy0um-IYAIbM5HPYaSLzGUKlEMYmE7kIbs0l_z35fguDLjKp0x_VUJ2xOsiBlWA8pUmVb6wKJ6uaaSfgwYkK4h22M5jna5eZmD6LYCBZRXE0IRbSIK8uPmBROBh_LBnwY6_9fyx6mPFZvwtra3vUU8yWT6tC_JoONxjClXEdwpWX1tP_lgYs-b7sXHJdMRY1hJpYcAa0h8vbjh0yYzzyUxsaZqJHGMd3E2aS7x3EHOnotp9q7I6Ft4mH3CeQNILZ9yuN5b_Kvq_dlNEupntM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
دیشب مامورها ردِ نوید زیادخان، همون فردی که خانم‌ها رو‌ تو لایو کتک میزد رو تو خیابون خرمشهرِ تهران زدن؛ بعد که رفتن دستگیرش کنن، این مادرقحبه با قمه به سمت پلیس‌ها هم حمله کرده! مامورها هم اول شلیک هوایی کردن ولی دیدن تاثیری نداره؛ به پای چپ ، پای راست و…</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/funhiphop/81533" target="_blank">📅 12:55 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81532">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vSWUJOi-fwaWCZLomb2hcwAhETFZ-mjtRTBZt9vurc56V36NuXxqy5RUlitbV_8rxkmGs7vdF8Zsoo5m7URwAQiEJPceTfAtQXHjkoUFWBFhD_2IYf9wI8VLdKFq6RxSwjlLzBT8n5xC8ZNmXx0DF6FzOjtmoaduFyinYXCiLgTBuFL1mQ64F4wcfAHaZKKTaErWvhhafpvPXuFNwHhEMZutSqjarKXfmLogd0WF8FpGHzkNGElnV3-laly-Yk65H6Pt8_owf2IGnuvKxiOVX2QYgP20kws0hba7gEp2WJyUzxzAmr2peqX8w3tgdN14odlnOXtApOdCLBgwZzB-4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
دیشب مامورها ردِ نوید زیادخان، همون فردی که خانم‌ها رو‌ تو لایو کتک میزد رو تو خیابون خرمشهرِ تهران زدن؛
بعد که رفتن دستگیرش کنن، این مادرقحبه با قمه به سمت پلیس‌ها هم حمله کرده!
مامورها هم اول شلیک هوایی کردن ولی دیدن تاثیری نداره؛ به پای چپ ، پای راست و دست چپ نوید زیادخان شلیک کردن و این گراز بالاخره زمین‌گیر شد.
این مادرقحبهِ 36 ساله، قبلا به اتهامِ "ایجاد مزاحمت، دعوا و درگیری، سرقت، ضرب و جرح، مزاحمت از طریق فضای مجازی و تهدید به قتل" زندانی شده بود.
@FunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/funhiphop/81532" target="_blank">📅 12:53 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81531">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QYSGMjJHO660SKtRcvcl6ST5gh2JT3CLiC8Nkl_W2Q3dYAto5d7JhVOeXLW3ZkMkXCRCW1MnLP75Wn0k8iEoA-Jm2AHxwroOqgxwxL_mdfz73aH6Lnh_jA4TSpNqO_0jCplKir7u3mnklnuNXZVbA_AnRsQNdUb9gnO-Bip7TccyRNc75JxPb8dKEPSLN0RwCUFqBerMhK0SETvOOSeSBrIYmt48nNP3B3JKkIvdRoBAQPEYp3GltPK2KVCisZz3nbupCkd0LfEBUuBMOBaA9DBwe8rdcwxk9WlznYWM4AO6P-lHnYZ9FqpYyqZB_xO1qAUYJS7XUE1ihndbsO7n2g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/funhiphop/81531" target="_blank">📅 12:53 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81529">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">یک منبع آمریکایی به شبکه "i24NEWS" گفت:
حمله شب گذشته گسترده بود و تأثیر قابل توجهی داشت. این حمله تقریباً دو برابر قوی‌تر و گسترده‌تر از عملیات‌های قبلی بود.
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/funhiphop/81529" target="_blank">📅 10:27 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81528">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">خلسه از زنش نیلو جدا شد   @FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/funhiphop/81528" target="_blank">📅 10:20 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81527">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">خلسه از زنش نیلو جدا شد   @FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/funhiphop/81527" target="_blank">📅 10:16 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81526">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">خلسه از زنش نیلو جدا شد
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/funhiphop/81526" target="_blank">📅 10:15 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81525">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fkbqmrf9pZB1-r6lyJxgr5cpnLICT5lhCHD0jESRHUrrBQtxksAN_HuQ47p8rQ5gV3BLejqYzNC8wnGoLVHEyB0uZOxkNLNlWC4Iqu_9idrOQIZenwr15ikcT6C-ZrztVC7hxguMLX8p4bQuvVMPOSSdw6G7s3WGqgbzruenh54utXG6BiPpdEWdX-BAiQQ-ayEKK6aggKWyk9B2X12FduvZ6Mf_llLh_uMYQ4g25i1fwS47yEJUxzEBh4BaGm2mAWdeskZ8Ag0t5Um4zsNFKa6Slt2EWGggH7WvC7aPXFuhbsaWQ3d_2xbBYTN5IXOvCb0mIKE7j4aukU1SZ4ZLGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ای کیرم تو این اکسپلورم
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/funhiphop/81525" target="_blank">📅 08:46 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81524">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">اینکه شب گذشته آمریکا مسکونی زده احتمال داره یه پیامی باشه برای ایران واسه جنگ های بعدی که احتمال داره رخ بده، که امیدوارم کصشر باشه و این برداشت صحت نداشته باشه. (اگرم انقدر اورانگوتانید که فکر میکنید آمریکا کصدسته و مختصات اشتباه به بمب و موشک داده و صرفا اسرائیل نقطه زنه نظر ندید کلا)
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/funhiphop/81524" target="_blank">📅 08:17 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81523">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b757b219d.mp4?token=F1FsXbeow7VNKQd6ZkGG9O_9MnvnzBMSXovlOkbOyScX-U510aLsEcEIEsTIOEdYHqIq5UPu3fm04wlAzaBAFYwzoEsR2Wty_w5-ZOATm8wknyn_NqH_ABi3fau132UHV8mF9JApPurNODG9ZaC4MzpqX1EUYxRWEgxEOU2WhJ52O7g85Ntnw3GnayUlLVHkzaBGCB3p_ARzi1EfFv2Ppm0TnFw5-d1OWRGiy2lRy_sOd5mEoJXBbmmtuFItw4s80jSsB1ILzZDiiF95b_klwU-5pIFgCDwGxKFt5OI8vkeisVGuBmv-9yzsUdIKtX4XJQtu1MfP-_C3XRjKyvacMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b757b219d.mp4?token=F1FsXbeow7VNKQd6ZkGG9O_9MnvnzBMSXovlOkbOyScX-U510aLsEcEIEsTIOEdYHqIq5UPu3fm04wlAzaBAFYwzoEsR2Wty_w5-ZOATm8wknyn_NqH_ABi3fau132UHV8mF9JApPurNODG9ZaC4MzpqX1EUYxRWEgxEOU2WhJ52O7g85Ntnw3GnayUlLVHkzaBGCB3p_ARzi1EfFv2Ppm0TnFw5-d1OWRGiy2lRy_sOd5mEoJXBbmmtuFItw4s80jSsB1ILzZDiiF95b_klwU-5pIFgCDwGxKFt5OI8vkeisVGuBmv-9yzsUdIKtX4XJQtu1MfP-_C3XRjKyvacMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">متاسفانه شب گذشته هم:
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/funhiphop/81523" target="_blank">📅 06:51 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81522">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">نتانیاهو:
نمیدونم دیپلماسی چقدر ممکنه اتفاق بیفته، اما نسبت به شیوه رفتار ایران بدبین هستم.
اونا همیشه دروغ میگن، همیشه تقلب میکنن و همیشه برای خریدن زمان بازی میکنن.
آیا ممکنه این رفتار با اعمال فشار کافی، از جمله فشار دیپلماتیک و اقتصادی، تغییر کنه؟ باید این رو امتحان کرد.
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/funhiphop/81522" target="_blank">📅 06:41 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81521">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">تسنیم:
برق برخی نقاط اهواز قطع شده.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/funhiphop/81521" target="_blank">📅 05:05 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81519">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">انفجار های پی در پی قشم و بوشهر و بندرعباس
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/funhiphop/81519" target="_blank">📅 03:57 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81518">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">بوشهر آبادان کیش
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/funhiphop/81518" target="_blank">📅 03:42 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81516">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a76739cd9.mp4?token=bYmWSa2RG6eTHZLHhduHy8SN9dRlVui0Xp1hVFjdvQC74CZacxE9RiV4g-09xybY0f_YPbM-zx3wt2KR5abPqK8tZb47MZ68g3biconpHMxQZBTEg6enkEkH1LHVbLM1f_okYNuLQMt2krUOZ5GyS0ALNoHeTRyMcsNeOx84vji5nu5sueGFWtOrHEbwug3cIh1mui6gENnFu700YMLB5-V3X6YwVQa9cw1uyoiEdBEJWpqQwl3yK0NAc5_JTriz21aHsgsdr-0V28J6-hkv8wMALoVHnsxTeKDP8o15N2HYdfzyzthoKrbTG4GQzvLKGUPENFwfH5XVr3vTJGb1Ug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a76739cd9.mp4?token=bYmWSa2RG6eTHZLHhduHy8SN9dRlVui0Xp1hVFjdvQC74CZacxE9RiV4g-09xybY0f_YPbM-zx3wt2KR5abPqK8tZb47MZ68g3biconpHMxQZBTEg6enkEkH1LHVbLM1f_okYNuLQMt2krUOZ5GyS0ALNoHeTRyMcsNeOx84vji5nu5sueGFWtOrHEbwug3cIh1mui6gENnFu700YMLB5-V3X6YwVQa9cw1uyoiEdBEJWpqQwl3yK0NAc5_JTriz21aHsgsdr-0V28J6-hkv8wMALoVHnsxTeKDP8o15N2HYdfzyzthoKrbTG4GQzvLKGUPENFwfH5XVr3vTJGb1Ug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در جریان مراسم اکبر عبدی، عادل فردوسی‌پور در کنار عباس صالحی وزیر فرهنگ و ارشاد جمهوری اسلامی نشسته بود میخواست دستشو ببوسه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/funhiphop/81516" target="_blank">📅 03:01 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81515">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">Game started</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/funhiphop/81515" target="_blank">📅 02:54 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81514">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">Game started</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/funhiphop/81514" target="_blank">📅 02:52 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81513">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">بابا کصخل بمب افکن نیست که رادار خاموش کنه، سوخت رسانه</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/funhiphop/81513" target="_blank">📅 02:29 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81512">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">بخواد بزنه ردیاب سوخت رسانا رو روشن میزاره که مهدی ادمین فان هیپ هاپ بفهمه؟</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/funhiphop/81512" target="_blank">📅 02:28 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81511">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">حاج زدن حاج
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/funhiphop/81511" target="_blank">📅 02:28 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81510">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">تلگرام کانال روابط عمومی سپاهو بست  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/funhiphop/81510" target="_blank">📅 02:14 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81509">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">کصخل سوخت رسانا بلند نشدن که باهم بندازن، بالاخره میزنه دیگه</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/funhiphop/81509" target="_blank">📅 02:10 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81508">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">ترامپ مادرجنده ساعت دو شد چیشد پس؟  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/funhiphop/81508" target="_blank">📅 02:09 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81507">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">ترامپ مادرجنده ساعت دو شد چیشد پس؟
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/funhiphop/81507" target="_blank">📅 02:07 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81506">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">فعلا چیزی جز صدای پدافند شنیده نشده به فیک نیوزا توجه نکنید.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/funhiphop/81506" target="_blank">📅 01:28 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81505">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">پست آدرویت تو چنلش: این روزا انقدر اتفاقای بد و عجیب میوفته تو ایران آدم نمید‌ونه از کدوم ناراحت باشه
🤧
🤐
🫤
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/funhiphop/81505" target="_blank">📅 01:09 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81504">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">تلگرام کانال روابط عمومی سپاهو بست  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/funhiphop/81504" target="_blank">📅 00:43 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81503">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">تنها اپی که سپاه و نیروهای نیابتیش میتونن آزادانه توش کار کنن تلگرامه</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/funhiphop/81503" target="_blank">📅 00:03 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81502">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">ترامپ این جواب سخت ما چیشد خوابمون میاد</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/funhiphop/81502" target="_blank">📅 22:46 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81501">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hlPdk-fObVjXY1M3iRhLUmCkEbSSM-_nIZyFw8f05JDkZ8umZh8PmXPTw7WqSnr1tfrHOgAMGbguLZIaFYfM71yv1jIWNp9u1l6DOsBsGL0LcaaQ2C0Ji44en4K3cSKeilgIRLYule0PRtF6UxXUE_VPl-vir_f8_mai3RiSum22Os0lvuA3hxm8gE4yE-0PFxs4v40_eCsv-EiGRLNTk3Bp0uvYgJn7Gg3HbGDwJJDg0WjPINPssh40mQkzRo23MIXhEBGPTxindqrYZTPuGfgvbjwBzydxpndGbXXKkhlc1QwhAvJbBJnIIaFq31adaJ1PccWQyMXeBx6B314nEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برا دزد شدنم ۲۵۰ میلیون سرمایه اولیه نیازه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/funhiphop/81501" target="_blank">📅 22:16 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81499">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">نتانیاهو امروز با رضا پهلوی دیدار داشته
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/funhiphop/81499" target="_blank">📅 21:16 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81497">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lyTTS7HXcU_QdLoUUiQ3xiyaT4WTgOvS4qXRpR88XcGRWgDP7M0P9eCWOvyp4GYMFoCAu7rorEgV6fdQt0WKuNO7QSJY_llzc6kLFio3CZwbxeaZP6tseMQGDfANWefCGPZ5cIV_pVkQESn3IpVBBsbJLqcSs00dt0-ymJ_MwK_eOxFQ5heWsdknImNEqY0WK1MUT_alwKO-_Z_k6kbxaGFnMlE5Mfjdb5_A_K4QgUMQR3XQ-4mZgTgxW3KVymNCDHm02iaFVgAkx6JcVF8t2GPmHNaOwnm6QyO4RBWQnUINrXmxfFXoX5tCckUzn93psDOgxMrTBZ3wSbWlJ0mQsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پشمام چه بامزس
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/funhiphop/81497" target="_blank">📅 20:46 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81495">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OZtksENiuKvZATCwXK4RCHuY7S3B9UEuzFzKkSZygWbK1sS832x67ZwlS5UfIG0BElSpqyNSbnvqRNReutC_NDUErzORgqmDgF6nqz74LOXNrdUv080t0QsMnqrtfNXxpTRONUoQBeFA7suvYYDk71COQwPdwi9g6vk40QRPc1jCt71yeS9vIvrUZRRK5SiQ1Ad8d_Q4u4JgBhuGURmSP4jiXMwUktic3VDeLnbE-ArYH7d5RbpWM9r4E9ULIdokztj07aRwCRZsok1dG7qOnR71Tpz-5YKxrNsJSsZtWJbibKMw87PJizvdwMb-6-01UsMmtAAc9h_k731blVwS9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی بچه اش رو دوماه زودتر بدنیا اورده با عمل که فقط تاریخ تولدش روز رند بخوره.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/funhiphop/81495" target="_blank">📅 20:34 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81494">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VvyF7GGMPZItDgLbkV8RJaXHVhWKB2kb0PX7S-GMtTeHSP9SKUXYGi6jFU3E2gNZ9yRyzqMUvf2Y1aF9X3W3p3g_vO4aiMawm8o05hMR380YDt17y1EulQnxHdeCTEnE2mhF8yN_J98ite_ba7YX51B-xbSZpmnEPK9g2jfCO04DXjcRzgtxASpncvuJf-8wRuFFGWadI6YZ66g3963JXGk0DGs0iPPx9wiveo4VtM0KiUmFwRKizVXvi-vCKe4P3CW9DE2cW0Cn2FkFbwILu8hvtYNyKsXgF4kOz6wwCR-fqDvTjoSfkZbsReF-kXXX5qNRlenHXV3swaAIBHcOaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اوتیسم پسر کوکوریا عود کرده، بخاطر همین دیکه موی بلند جواب نیست و باید ببافه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/funhiphop/81494" target="_blank">📅 20:21 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81493">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">پرایم هیچ بازیکنی اندازه رافینیا ۲۰۲۴ بهم نچسبید</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/funhiphop/81493" target="_blank">📅 20:11 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81491">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">از وقتی تلاش نکردم برا باز کردن پیچ خوردگیا هندزفری سیمی کیر رفت تو زندگیم
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/funhiphop/81491" target="_blank">📅 20:04 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81490">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">پول ایرپاد نداره؟</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/funhiphop/81490" target="_blank">📅 20:02 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81488">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/r4fF_eXsOPymwQqhzQWrfD3ndlyF_39lnynrr7nnsus21W--NTfSEr_M3C_V64FpM3WsCB2kkrcRaCw-BzHcB5xcWUHoyRCMZXgSn8m7pPyrZCfKtlx7tG3gYEORXUPsR7LbtLLOrm45tlwaRyqzAp8VJ2VRc0sXA9vGrwoeB-_dOg3GjKTrsZuNp1du5Tr-A0p_fXaKNWIvUmde3mz4A92YYYG5mlK6aEdtxNOXZ4t971CJfklQ5d_zSERWUtBE2dJzSLnr04CFidH9X0LWn44jtY36by9Z9UbATaOnwNQ62cUIts3FpOISxngrT29CsMvPKq1FvDC3AtP_-myh9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/b9OkxKYLCqJ3P4NGtu2Fn-OZj3E6pz6wjFQerB1gE8TPCcJNp3WB5xNWeWuZK8-JUPZbzKKDn-XKegXzkgoZXFNRq5BKW8hz_XvO6ROlbRCo0vc1VuBEh0j0qBT4alpnwQEHVuOBoYVishNwe6GEwF-ka5UF0fj-IvWNdVUXEzYuvxr6zhuaNTAsGxgayb9M9JY0pkYbOXbee4cyAGP1ICxqcHG0oAVko5yRXnhhQY6NQuSJLgHc4UJ_60JjKvjggDbEHmCbXwwe8xZZ-uDlY5LnLdFy-eb5kKotfFmnT-xnY6ITRYAeMzZAs7-P5cCyfuBC_HcKyjClzubZngmt0w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">رافینیا شبیه زن جنده ها شده
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/funhiphop/81488" target="_blank">📅 19:58 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81486">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jWcsTV5o1R-PQwW_FIYP7kKx3ELX7Csa2n6MlxUSMxuqg-56SIoiPoLx2n9fHR_mv4MEFufQ_UauedhxOFhar9Ng1qlChJ1DF8_tKqKW_75MGASuVq6cwd7Iq6JXeJwrX9m2S5J6Ith7PQjsuC-tMWs6gNS9Ob8mMTG3LkUKSz3ZFbo6OqhAfbrArri5SMntcWSVTP3AaZQnfWxV7EtGi_4hY16fQ1rGvh9tVCEhuMm81oSICPhYXRIhS9Ij7Jc-PwKsvBUrT1u7okGbAfrnY5vhkXcFIdtQ2QoJG_J778WapLXcDFa60qmapk3D43tVOUibyy0B-nSwJySafSz_0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CEOyGa_i3RspF2WV39eibXoANUOUW62Oq0-S4EIbbYiOkCAwu3Ih7zFmBWn0rp6YQgpKiKekQX0zrwpZfEVNZKJSKduwkS6bisFNfni2MnAIGYqx4xYVCIhn-0u-H5XuMq_nNv9BfKSVg_Z9wWAWoOslHoyjLK64iSIi2U87YiiyCyK_OwLrEwFz2ylUfoPlZg-JjMQ2PIv-itOpNvZjslEKlcNbyzJkNWWNyTIRJWq8YpekJqVLgRtqiJNKE76c--ZGWEPRDdwMuzanaab7bWlh6qc3W7dzsJ-PSvXS7SuHg6VKnn8I-zZxrAIfMnPSJJnv0QJIPWeWiwv7khKJuw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">هرکاری میکنم نمیتونم با قیافه جدید وینیسیوس کنار بیام.
@FunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/81486" target="_blank">📅 19:22 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81485">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l5ebyWxE8d_0hjOPq8hI5VMJsIMXLk1I3sfg1-sXDeDv6sH17rMdL_5xXzY2P2o6HXFJ2PNEKRgH6I8kXZHlO4J_vv8I9i4iciRZpSNp6XHx7oGlTaqXs4dccukfFc2oGw2EDgp7PHZBv4L2dw5UmAAdRnoTLyYSihnJEHn75bqtUW0yEn4pAYnA8CG7vG7MpvJORANODIA-FaljdyGnxnZeFxTF8o-hDQQcE90xlSUIgZNETRsacAryjf5F2vcL9EQXJiMGvyXKQGKEY9UscO34js6BFBV2NiATxBjq37bKumjPV7sEx3mPQ4WFGxf1sMS2ioWoV8coXTxGNrvjxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چی بگم والا.
@FunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/81485" target="_blank">📅 19:19 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81484">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QdJD3dv3OTg-QVkCHwchjEazf79tW81VokcocEElmbXB43PwRYdCJfyZnkLoNfu4fHkjjJIoLVs8wguBdEUzFUynKrFl4Hw9TfK4j7FjCTmlyEbZfzssohzDTxa8mBW_iIGbJvBJeFuW532tDerZN_pkSaLDRUtdmJUFssaSMsW1ehwVDaktlzClwtNxGbS0jL27J8lX2HJlFFlnQdO2TRE3mBoIeTEfGvdmB1Rx533S7v6nZVWb1R5HxPbfySejSFfUM-nGTLgwiaXgYd9B9fsiU2MGprAsV6ZmxOfN_ypra8W_fHFj3tp71sahAIjm5lP4_9T9Wzl_8ijVYaGewQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/funhiphop/81484" target="_blank">📅 19:19 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81483">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hLuCnzNkN-O_hmeajSE7fjEeq6ydTMJcCPscigJ4ncaxpZq9g61J5omgO5zi-9w7dl3y5w3AxPTgdlcLJMcO849qdIdaGMlL-uWiYqKLNKPeaskNZBhW0sw7yOKziNyLlWzxehKmVFMsS-SvzpO1QJ4PQKNQ5FClTc3mH8BmyPvsHvzrs12-AMQLsEJyDcxvqGiNRTw0O_EhbWXEO2fM-p_vf3_BcwTSikDuVGBZgF6d3Pref9zgC-aPBJ3U84Li-ubuBvnQ1oQNY8s7KJhrKeDdpj6TbAkQqe_vFZ8JGzrM6z7GLRNuYck3yAZTNmXWwvhuCW8roDH0zK_hwbNwCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عکس جدید صابر‌ ابر و دوست پسرش.
@FunHipHop
| artin</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/funhiphop/81483" target="_blank">📅 18:29 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81482">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dvD0SJ-VMPJJTUOWgGEHMV45iJvfe6Y9IjZ5kQLr-lGiHvr5EzMKQi-Em3aXhrCh5Eb046tIGSWwvPAnwnzxzu-Y5TSB7vA2BAkuieARUdO8VtUHYIPo87Uqh26cwpWwUPpEEpzjR4SgRWF0FNSJ7he4zhmdwCtz9B4t_n4xwdtN74aL2Sz5SMFClCWjl5aIX6GU0QUyXe2csdV8_JMT8dmv3q8JHVq058pnw-G7oZ9RQj_2l0zFfbs-5co4r9UBJo_-X7u4Q3TNCxa_0am4fz6OLE8gZG-K7NmEj1RAE-R1UDdOtv8I1Fw2jH-1D87YpCLWhC1lMhcirY3h59k2zA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پروفایل پاول تو تلگرام:  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/funhiphop/81482" target="_blank">📅 18:10 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81481">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vrp8ZJMgKD4UobIt4kw1ED2wT_gv_jbT7dwRmYXorUznjaH_PwOMsjWZgc0-GkKZg9TYpDiH6WNxUWL1TxWZCad10HV1GSXI-Ea67S_DoQHGKgodwa-N-cFEvtMLML57F67xlvrcLzs9UaOJSyx97bQgiz39JFSdr6OtBKhaEQqDO9Q76xJQ1fkwQsBTrnCLXauxSMJFMxla_uz2nN1i3AWlYFLhazT5PVr_x_7Tu4y7wVjToQYGmG5Ku75ZCWMSoSBzYVwUA52MY92KUaMynYxs-gAYW85ZNGwo8yHAKxTalfaI8xt40RYAvFtN7emqFnkzJ7qIaymQCrU_tbPB9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">واکنش دورف:  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/funhiphop/81481" target="_blank">📅 17:39 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81480">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">عاشقانه‌ی جدید عرفان پایدار و شاهین نجفی به نام "داشی" ریلیز شد.
🎵
Spatifay  @FuunHipHop | Nima</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/funhiphop/81480" target="_blank">📅 17:04 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81479">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s0CTOOgsFw2jIlg4hYQJk-Bv9aDKC-DhanlFhtoL6QlGp6xVPzSlnD97Yk3fHs-p2Tb6-jZ-DD_KfWl7NbX8lWEJHRgbKngxoaVf_fq3XPj8CYo9BwycsN5BQyJMJgf8KiD98Av3jTV_gHGTdHlhTg_9ChsBzsvgQHYDq0GIWBG98nJ-RIcCx1amXfOPNveRE9ZhOJz1O-U0PoFuTrL4qT1WIlKVFNcBHjuOtRPIq_ovtULWzGOR9y9Bse-M9Iy1McKuyfzNULwQOYaeYMuvj-PzICcXOLl60HqjCZ4T9DgKR5rhSX8FAoE9XTTSKOdCJET1Ztp2Soy9q7pNdRVKng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عاشقانه‌ی جدید عرفان پایدار و شاهین نجفی به نام "داشی" ریلیز شد.
🎵
Spatifay
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/funhiphop/81479" target="_blank">📅 17:01 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81478">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VbtR1RXvBcLtwoJKoqW7sBv5OM3YVGfd_En3_gWsUhHW03KueN-SjczNdOwgL6tU5bXTVG53hc0rQ7ZroOE8Um4lXh28uMEIVYt8u6JJQ4j6oDMZBe6tgykSKhsgWXYI8xATJA_1wQBhZSQ4ZB46r4y-oQBHao31ete-d1N-Q_AseQPuS5XpunJ1OeCzqQYcJuDxMKcoqhYIkzIDvx8LCPHRkT9k_tc0goH14hoYc5dQRFwbNp19upkTNhOK9kV3rK8gWsOMrIJ4Fq_Pmu2UW7WdQzPzkLcZsi9-OMSc6QW7ctYklatIAGt4y-cQXMA1t_urGPfc31vLNUFlkO5bTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پاول دورف داداشم، به اتهام تسهیل فعالیت‌های تروریستی، از طرف سرویس امنیت روسیه تحت تعقیب بین المللی قرار گرفته.  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/funhiphop/81478" target="_blank">📅 16:26 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81477">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">ترامپ: ضربه سختی به ایران خواهیم زد‌‌.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/funhiphop/81477" target="_blank">📅 16:03 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81476">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">منابع نزدیک به سپاه میگن در نتیجه حملات دیشب عربستان و آمریکا در عراق، تا این لحظه دست کم ۵نیروی ارشد حفاظت اطلاعات سپاه کشته شدند
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/funhiphop/81476" target="_blank">📅 15:53 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81475">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">اسپانیا با پخش اذان از مساجد تو بخش هایی از کشورش موافقت کرده.  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/funhiphop/81475" target="_blank">📅 15:42 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81474">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">اسپانیا با پخش اذان از مساجد تو بخش هایی از کشورش موافقت کرده.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/funhiphop/81474" target="_blank">📅 15:36 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81472">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u4s2rx4aNXQF-P5XfDetEcHEmvRqjV2lRnXB8BAN9495nxT86IRCuUyWPSunCoGaykANpE1XgqBOTrYmnZK1ELRGcYbqWmakBhjzh2JxmS04ondc00NeseV-HaJbIUdLUX_46Jm7h26T5WEjUOe4q416I8qJJ0_6Utr19lQn0c0PpZvR4IgpWom3xBrCGA1SHYnfpmRpkwbNmaoTBvYH5yHpwkz566j2PUH9iWBLnf2xE_1w0PiWwcbXMjlYHJL6grfJt3nGHceog-XBJmv_59Q96MWzlkYYC54_h9lE6rp-JgddFh102C89rOnvrE-Z-jq-dxKg5yNhF4yotMgfoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هیچکس نمیدونه چرا این پست انقدر ری اکشن "
🤣
" میگیره.  @FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/funhiphop/81472" target="_blank">📅 14:57 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81470">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/N-6YnpR8BckRv3u3kV41YOwQ2TtZ5Vc1jX-qwMSGKzKM74Ky-sSh2eHu-2mwRaKABZ98_0OhHeDdXs-JnmDAXhfaVNKOUZQMw65kw6QksmOvmSpmxlUywtb40gjIUEnaAeNJdA37Fuz-RsnIoeVf7TUzSRTEq9cJHPuubCOdanXC9K3OmhomMFaWXvDtohA2h98qJUKagnAiKlu9tVQjrwpUsbv6ljfi1x7cYTTunOADIdBEEveOp3NWqDz4yolanUIH0ev8H2AuisDSdhpPBaUvnyDtkjQN79ZNXsJCIVa3PKqFzNjC0VIWcGawf-vO5sEcOm9X0HBqByRKWHxfnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KrDsAa_kjE_8M_jkfbbTZzIhmMp9Ns2czFh-yikdVC-m0EF85ToTlb9Dg6GqXOqd4YCeIhq9dBn5SIVoAuCW2BgaIebD1Wopvb2LlRUNJjemixaka9gtApIu-trlWCH00kjj1p7ejQj1akGaA0d-JYgB3kCLCI7V_DtjCtVL_sb0EXnmuWsjEZw3FqoDSE9bAYajVDnXzZgfIp9qQmr8LXcCiLRvZWJAC-nSOzzRbVCv-whqNKu2uh2WcChL2kdeXYOcDkwb2d2ehcbRwUZe0Q2WsTMLFzBXDOfLxiM4wciukMwUdyaWztO99RBlGOHXSOUiZvGlY04L_7lotuyVwA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پینترست چرا تبدیل به کرج شده
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/funhiphop/81470" target="_blank">📅 14:35 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81465">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">اگه این با سپاه همکاری میکرد که الان همه تو صف اعدام بودیم</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/funhiphop/81465" target="_blank">📅 13:41 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81464">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">پاول دورف داداشم، به اتهام تسهیل فعالیت‌های تروریستی، از طرف سرویس امنیت روسیه تحت تعقیب بین المللی قرار گرفته.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/funhiphop/81464" target="_blank">📅 13:26 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81463">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">دلار 193
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/funhiphop/81463" target="_blank">📅 13:08 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81462">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NLTv1WfnZL29SqVnAp9epTwqNpMdN23EUC_xOQWIdokwlEmxgHM0SgP2UnlUGzal7-dw5Q6s8DW9CULn5GK8sM5EaLdP6H5VjNDdS8eQeIvaB48sc4qoVwkBcUj5vDqwcaRPkyiKvyiTcPdZJoGsOjh-Nu8cluLKBdPE_b35qNroyxEQP_HnVfMAPDX9byHVhKVDWuQhqPKSHMN-zfPU5sZVO8mm7swM5vN27SHDwu4n3COdEheHN9amRD4YJ1UV4E7BbM2edGJsb8VlFCCZ0PkKsOdOdrUz87ebKtomNj0egPVhWxbQWQF0nVHmm0byKWSwhjaFXCgG3mL2rwnuFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استوری پیشرو
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/funhiphop/81462" target="_blank">📅 12:27 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81461">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DK0ueS4Yw55G83gU5jqgZ94kRrlSlu8SDGfUreAAHiFwXkm-mSr6pch2-kX_glzGch_7sqIBiA_rBwhXy_Vdl8G1Af0eKmTdsGcWXbIkQnoMGTPVGrUb6q19DnhsJ1sY-kBEGeWmodE7RFpP62H2rRmkQHFjxSGsfrOF2yfPHcAe4gBvFKloCBaUiDfVQuOW6C91tf7Qwh1ULctACC_hXAGVpEzWFDbw58TqiZaq66AjZT1Od0FlASkKq4W3Gw6lsQGbPZQlVDh4EKF0ZulYaWKMpRjxkPisYBpBbsyAd7CbttkvzMJyxiTmvGZIH5_ZjEEHHw_z0lvR_CRLsKSAgw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/funhiphop/81461" target="_blank">📅 12:27 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81460">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">از الان تا ۶ سال آینده هر اتفاقی بیوفته ربطش میدیم به جلد مجله اکونومیست
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/funhiphop/81460" target="_blank">📅 12:18 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81458">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">هدف یدونه پایگاه آمریکا تو اردن بود فقط
💔
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/funhiphop/81458" target="_blank">📅 01:23 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81457">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">تروخدا اسرائیل باشه تروخدا این یهودا خیلی راحت نابود می‌‌شن بوم بوم تلاویو اسرائیلی‌ها مجبور می‌شن از دریا فرار کنن تروخدا پدافنداشون ته کشیده ۸۵۸۷۴۳۹۹۴۴ نفر ازشون مفقود می‌شه کلا اندازه یه استان ایرانن ۹ میلیون جمعیت دارن کلا تروخدا تروخدا اسرائیلو بزن سردار
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/funhiphop/81457" target="_blank">📅 01:18 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81456">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">ببینیم از لپ لپ اسم کدوم کشور درمیاد
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/funhiphop/81456" target="_blank">📅 01:15 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81454">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tM7e-M3sK_Ezt-RulBrgZklOVB9sj_FCsyhNGAbSHnR-hotkVSgxqFa94zkOw9-myCOZGCQzLfHnkTerpzm6lfBHO3q-bHDBwgwnOLzPNgF8Wf1jnvZzk9jroBHZZ3Mo0gCZ8c1hHqaqJaLGzTVUYNy8xNLyKDThH166p9CLNDn6XMCQasJOdcx0lKatZKDxCeS_UU50UU76VPk3Du1iJMBXFYYWaSJY-9zy03L5NC60Gq2JRXGjjU0htRxElNzNcjlKF10frjej5y-iNYAx1JhkCVIFv5gU9Gl4BdMv0lmV5Z6QhzwO5c3iIgiQKp02MJ--ZxXkEYWIeMRVznA_RA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😂
😂
😂
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/funhiphop/81454" target="_blank">📅 00:45 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81453">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GUAtRQvrGRs_hQraN4cZCl8lf2ksU36PKPZiJb3cuJ4bNjuvQmih9cGNp0tl5_nM_XoKk54gbSy-iNq6nqFu84KgsXAJyli0vwSyTUGnZ6antmr3ukPLXr606o96J75Qai7lTEtAxbDB6YWNq0uVo1jEAASyGQ6q3Rx_YT8w9qmvlCr3vtAqP6I3H-TOoM357RszSu4DbuIrufY0oqNRpfD5M1O7nOaBr90hTV-rrLvJ-bEzzgr98_oAx7cnMHdgFaRCfJcJCT58nN6lSez9WRcbqFNIMLrVPichg-61kRQtjjTEcbRTCUNDfACmC0A7ur-r8cMgrdTfnFeWhDae8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هرچیزی برای تعریف ساده کلمه نیاز به یک توصیف ساده و فراگیرتر داره، مثلا خارجیا وقتی میخوان بگن بی طرفن میگن "من سوئیسم" تو ایرانم هرکی میخواد به یکی بگه "جنده" دیگه این کلمه زشتو استفاده نمیکنه، میگه "شیما کاتوزیان"  @FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/funhiphop/81453" target="_blank">📅 00:39 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81452">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nOqH80N44rnWVHwkluTQN2-93_fSO066Fmb4Kv9ogup1uD2hxGomNf5hXQDBrq20P65KQYe-32QxYlgugMqHG2S_oYc7e396AHoiTwEjNAJsgy7GaDx6b7gMeglp-5xaD7_hiLjhXVrwr00BG9HJrwuBcMcIJU8H41j4IZKJywKZ22anWzcJEqv32KpNQCJS-V1yNZ_H38_HJ7VqofcMvUcypgjsPdx1LMvsgxXe5k91UwTSqDstmn648O7B41IOKmLfx4ly2y92RxjyquAEr5ixxxujVvjHV_VS-XDEgl1XDbxLBDzN5_H6Ms2eRfwtOlETV4CQEyWk-tQpGAF-5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هرچیزی برای تعریف ساده کلمه نیاز به یک توصیف ساده و فراگیرتر داره، مثلا خارجیا وقتی میخوان بگن بی طرفن میگن "من سوئیسم"
تو ایرانم هرکی میخواد به یکی بگه "جنده" دیگه این کلمه زشتو استفاده نمیکنه، میگه "شیما کاتوزیان"
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/funhiphop/81452" target="_blank">📅 00:32 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81451">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">#رسمی
داریوش ترک کردهههه
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/funhiphop/81451" target="_blank">📅 00:20 · 07 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
