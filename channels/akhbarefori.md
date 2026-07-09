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
<img src="https://cdn4.telesco.pe/file/oS3HjtFqTy3dSLsVhC3-wZ0nyoCK7nzk6d5KvLIaAUzgFTRETWuetsMVllhAGVkhPZ4Xmqsf_aKtDA26CpxsEVbm0m4ImNgnqlDdGOSubgyY_jtQlLU0PSoVEINeB-ss6-5lNGNcHcqe0SqGpMgKFwb9l4wvjrlqq0Po-ayclVoe2Kjnj0BVumncU1zR7VLwWe2c3QInj8IEQehpl0AmLOpD0ass51qLrQ9TG7c6ggp1fwqq_2f0tGU0o4J5A2K6jNvI7fBLj8ndpHzSH7lk_0yJg3he8VyU7jQlsTmZFhpwnA5mqvyg96hsLfTV_G00mXzgod2vfbP2CNm1g0HSQQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.49M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-18 18:03:59</div>
<hr>

<div class="tg-post" id="msg-669141">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d2e1a3e20.mp4?token=F61qtNQ4oDi01bVumiFel_FwmViTQi9dBrd3j_PWrH0uJbBnb0XfuyfuZZH2M63hiPidPLu2JfrzlrpqORPzIZURcBwDBScNrOHvcHR00fZrkfYLo-AKLREXH6HVgMHl8_AM9HL1wACn4UAQD8tIG_47BGAKdeWC3-9humEvbH0ynUEl578yaO2N4hjg8nMbISbjjke6S50I3GLZSK1LDq_UiTeTAUItFf8cmUNp9XqHDRihf5Rp1ra8i_oXaImc6Ahil4UXlkOTILiOciPhmC1CN53LBVE2bmV5keCt1Ol6Kcp65lIa03eVILlLvk73FCpnDxguDv2gkffOAIHqVRlrg6Y2E5vHrPysjyT63s65G5Gu73K8EMSP45Jbgux4Ppxs1yDvyd3FtWRTBGhel_6FRpc8wP6eEaXvjGZV4S2fQZCbSGJVXe5_jzRbr11EXAcdgDW0N3YqQ27G26xlquZL9oZt0AO9f_6MiHHTGh-yHCa2HAxtvybZnlEHCQ3JMoGf416b5pXMOg1H2TPuPhSLUFJmBAW4f_pVjtNmsx3KFGk5ky9iQdJngbIdBxKDXCdCwZKnvFnbDBBxwauHRIfhm2U0LKh4LQYo1jkWb9TI0n-YAKBVKO-LuY4pDEfMPsOoFLvIscDsXheYKhTYV_H3q_oal_ncS-ZLpNcttCY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d2e1a3e20.mp4?token=F61qtNQ4oDi01bVumiFel_FwmViTQi9dBrd3j_PWrH0uJbBnb0XfuyfuZZH2M63hiPidPLu2JfrzlrpqORPzIZURcBwDBScNrOHvcHR00fZrkfYLo-AKLREXH6HVgMHl8_AM9HL1wACn4UAQD8tIG_47BGAKdeWC3-9humEvbH0ynUEl578yaO2N4hjg8nMbISbjjke6S50I3GLZSK1LDq_UiTeTAUItFf8cmUNp9XqHDRihf5Rp1ra8i_oXaImc6Ahil4UXlkOTILiOciPhmC1CN53LBVE2bmV5keCt1Ol6Kcp65lIa03eVILlLvk73FCpnDxguDv2gkffOAIHqVRlrg6Y2E5vHrPysjyT63s65G5Gu73K8EMSP45Jbgux4Ppxs1yDvyd3FtWRTBGhel_6FRpc8wP6eEaXvjGZV4S2fQZCbSGJVXe5_jzRbr11EXAcdgDW0N3YqQ27G26xlquZL9oZt0AO9f_6MiHHTGh-yHCa2HAxtvybZnlEHCQ3JMoGf416b5pXMOg1H2TPuPhSLUFJmBAW4f_pVjtNmsx3KFGk5ky9iQdJngbIdBxKDXCdCwZKnvFnbDBBxwauHRIfhm2U0LKh4LQYo1jkWb9TI0n-YAKBVKO-LuY4pDEfMPsOoFLvIscDsXheYKhTYV_H3q_oal_ncS-ZLpNcttCY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هر پرچم سرخ؛ نشانی از عهد انتقام
#خونخواهی
#تقاص_خواهید_داد
#WillPayThePrice
⁩
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 6 · <a href="https://t.me/akhbarefori/669141" target="_blank">📅 18:03 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669140">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">♦️
نمایی از پیکر رهبر ابرمرد شهید تاریخ و خانواده ایشان در آغوش مردم در خیابان امام رضای مشهد
#بدرقه_یار
#اخبار_مشهد
در فضای مجازی
👇
@AkhbarMashhad</div>
<div class="tg-footer">👁️ 3.05K · <a href="https://t.me/akhbarefori/669140" target="_blank">📅 18:00 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669139">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">♦️
در آغوش ابدی خورشید/ مروری کوتاه بر تشرفات این خادم آستان مقدس رضوی به حرم مطهر
🔹
داستان زندگی دنیوی سراسر مبارزه و جهاد و لطافت رهبر امت اسلامی حضرت سیدعلی خامنه‌ای از مشهد الرضا علیه‌السلام شروع شد و تا ساعاتی دیگر در جوار مضجع مطهر امامش، حضرت شمس‌الشموس علیه‌السلام به سرانجام می‌رسد.
🔹
برخی تصاویر این نماهنگ برای اولین بار منتشر می‌شود.
🇮🇷
✊
@AkhbareFori
|
Link
‎</div>
<div class="tg-footer">👁️ 4.08K · <a href="https://t.me/akhbarefori/669139" target="_blank">📅 17:58 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669138">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f3b602415c.mp4?token=QWrDGXDCEGCRTzjyJ5dmvHF0tj-uLzU1SpesBFRrd5nWky2nrS9XbOueLikAaQ0zFGE3n6j9y3rOfQjK40QQRLGErtGEsRJcj36aX4ayrHZD_sW4907sUVHId-Lr_ThecxEJmTCOj0FSsFeqkUvkf_nIZxY1fWOxS9kwcgqFVg75Hsx7LX3M5JTG65084ScE39pIv_nnU96zH08Ys1nAdnjkQHLBmWaXJzxP5pQR5CvZn-KdymmbW5nk5KIfBwZQs05MntC_fCorzXm_QylTbj5G9TBgVhdumvOUM4SJT8bhwPvnvNXPo3FxB_osPxh2rfwWanNQNwNRsIqltADhHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f3b602415c.mp4?token=QWrDGXDCEGCRTzjyJ5dmvHF0tj-uLzU1SpesBFRrd5nWky2nrS9XbOueLikAaQ0zFGE3n6j9y3rOfQjK40QQRLGErtGEsRJcj36aX4ayrHZD_sW4907sUVHId-Lr_ThecxEJmTCOj0FSsFeqkUvkf_nIZxY1fWOxS9kwcgqFVg75Hsx7LX3M5JTG65084ScE39pIv_nnU96zH08Ys1nAdnjkQHLBmWaXJzxP5pQR5CvZn-KdymmbW5nk5KIfBwZQs05MntC_fCorzXm_QylTbj5G9TBgVhdumvOUM4SJT8bhwPvnvNXPo3FxB_osPxh2rfwWanNQNwNRsIqltADhHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خوک نجس بدون هیچ توضیحی کلیپی را از بمب افکن‌های B2 پست کرد
🇮🇷
✊
@AkhbareFori
|
Link
‎</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/akhbarefori/669138" target="_blank">📅 17:57 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669135">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/STAMg8hs55-5Vi9b907XEG8orRcMaBS27Bm4jwww4KikepFALB-B08NjV0vwjKpAkZH0QcttMMhJc-qZ8ty3ZUx9DF1sqMawIyAHgyL08VyCDMCg3zvfbOBHu3JvQGZ68P7HyYTQG6wCIMNOuDvbj4Gw5_A41wri4lgHPJBOuj3DzsHiCoKwtdJbEBk6g0rorFfQd1T9ws1ZYdZ4sMSPtDpPhjLgE1hIMU928b34x4k7ul2rbHT4mnehLDkriMxeUpNLjMOQM7mxsCSvZrBHkZyasP4i_fmLeL3JAYWRpKhrawdeFYEw0wF93AxLdk3hJU2KqE1--hl9VmWYjepa2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SI40CnLoryCBxDitz6BShn16H6HVEVBc4ZVsP7JlXKAIoDI-UWVrCZJzb32mlkY-5yNttCppR0Ml0KYYwWQRjIUR-oQgc_wWKDx1PYrH8CKtiYKpS-a1MCI7OoxEUYZdBUqzhfqgmarla_nzQpPvwNQDUk_Vld1r7Z5PD1ECT_cUFV7I6wPm2pZ_M6cprEiDRYIfji4ADQ3IMIczP6_GGbGSU_58x6PwHvfnPGaWyUcc5PYCph-ISgnVaXKcgs7cGlJmql_rdzDyza3386rB7hB5BuaGRN0FWst8sHntuTj9_s_Mo7Bnp-Hxb39yCIe6L34u4ckdMWgRzPo_rQICeg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d47984cca.mp4?token=p95OxNLguPv2z1LtjDQaeZ1EVVKz53On1-cHR5CzL1LB3dT5yTcAqsP9BWrXdXcyC07InrF9C06lgbfqAVBBfTuN2IlngaeeFPxSK9wTAh6PtyFaIe0KLjwo1XA3VhRZOj4RHFoljYJCTx_vdGsvKpRC6ELS-WzDmnmaqER1ElS5ACnsjiFPw-iD8K6CL-186r8whtMOesHRHeoPd1Y2_i3a1U1LlzTBTGZ_hCkWvSn4kOatSA3CUNVtCrJRvSn0krxuRYZKq-pFYuR8Sl_j8bZAEzYcgEntcy2I_mMBWbzRHsIrh0lXN0RH1LnqaabUF3KZcmYFhhAgmBcxYd2CeQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d47984cca.mp4?token=p95OxNLguPv2z1LtjDQaeZ1EVVKz53On1-cHR5CzL1LB3dT5yTcAqsP9BWrXdXcyC07InrF9C06lgbfqAVBBfTuN2IlngaeeFPxSK9wTAh6PtyFaIe0KLjwo1XA3VhRZOj4RHFoljYJCTx_vdGsvKpRC6ELS-WzDmnmaqER1ElS5ACnsjiFPw-iD8K6CL-186r8whtMOesHRHeoPd1Y2_i3a1U1LlzTBTGZ_hCkWvSn4kOatSA3CUNVtCrJRvSn0krxuRYZKq-pFYuR8Sl_j8bZAEzYcgEntcy2I_mMBWbzRHsIrh0lXN0RH1LnqaabUF3KZcmYFhhAgmBcxYd2CeQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏
♦️
حمله به قایق‌های ماهیگیری مردم در عسلویه توسط خوک نجس
./ صابرین‌نیوز
🇮🇷
✊
@AkhbareFori
|
Link
‎</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/akhbarefori/669135" target="_blank">📅 17:56 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669134">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vcYUDbKmFtadaNJPl_9euHn46K9tAk4MFXtU3Le9AgTWEixIB6-5trswMvE1d0rYbPxvAd3CVio571I-L3Xh3bOkAbQU7tUslIh4YmXzYkDnZ8FtQhbVSa-6AHW_h9Ys_lLl4C5T_si55rYrH278BOnTnQsCzXZ0F_TW8OUj5vncQWCPLhcBXgkHCguwNGRNWighW8Gif9fuwu1bBAXcgpFJUbdPosG7DqnvKudE3LmZTOlNIuoH1dk6QskvHr2JcA8w8b4MU6xlL-Qwsq4_3VGLKwiCWYCyKkPA3lsEEuz-oQ6PgNfKIoeoMsXGSRf3N-RlKstaXV8gUASFAqo0tA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
هفت تیر اردوغان موجب دردسر نخست‌وزیر بلژیک شد!
🔹
اردوغان در حاشیه نشست ناتو یک هفت‌تیر به نخست‌وزیر بلژیک هدیه داده است.
🔹
این هدیه تا زمانی که هیئت بلژیکی در بلژیک فرود آمد، باز نشده بود. پس از باز کردن بسته، آن‌ها متوجه شدند که داخل آن یک اسلحه به‌همراه مهمات قرار دارد.
🔹
این سلاح بلافاصله به پلیس فرودگاه تحویل داده شده و هنوز تصمیمی درباره سرنوشت آن گرفته نشده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 7.1K · <a href="https://t.me/akhbarefori/669134" target="_blank">📅 17:52 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669124">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromسوگواره بدرقه یار</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iNWrrdhfY9r_1IlmJPQwVHFSXkkKe5bfGyPyKtCliFvgGq0NazWoxMVvkhfIBNbVwKKTxrIgZRbD0gHosaSkdUilzWQY2TR0RoJOZAx2wmcmNpIbu5K-yjH45GN7omRkaImoIBzeDBg-VUlSLYHpaDPPXWvGcgBNMkV8cXXsqzLE2_sk2uFrUibFjTrAHVwDg7tPjdic2_829oS5ig_HVjwqliCCRQ3OzJRY0pXG9QqZ_NK_MCVCwNjfTMxGU4VRUlCT1raOWnEiewvs48nMHyVCFwURbhbsvr2WYe_mV1GSh_JwrNKTC9s137VLxi_O_7IawVi8Y0bAWRZJ-8m9Vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dfbaaxpJVS8a3cL_P-KXNE9sazTLbMqDsH17Hgp0f82AGpksrj5qhYV1LLspnnfjGQ5O0biH_q5AYunswtnZvZmwMRZ1BYYHxXCoXdx9yQEJIbk_O4d6Zh5JPlNpucPlgcQwe-U577-oR1jXDGzKbI0r363Ax_NN5nG1IgGpB_vqXsCsjQ3_T8cRD954DqEki56Vt0bjLqXud9bzC5RyfmIyypOiE1PXFOeeJM8uZ0JdggSgzdgC8GpY3Zx8oDM3Yvsazw8G583APMlMum1LZ4yJQNy4zczVU5xOcRc0i4wyOuVf3vxqsvg9z5_qQ-3_RabzNgo-wZAyrnh1FVZo1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cBOS5R9EOUfgI8fNi6FmFk1q3VA3ybVp2ekU37Mmi-jEA5FCwH73dawdmXBmuv4ORurjbZXOUb_toKOeikV99Lfv8nZpKXkW0DK0Q8Pj5YkITNEeXYf2rNeB1MWYpKncEEM6pOEGMGDKeQ4vNs2tDdiU2TtQ51oWKDs6t2Va8RnVmTtUAxr2jFTtgzZmyf80SyM1pNSL5iOVB8nsNMfeiYf5h5uahNZY7QsXdYpT-J5wNr6o_OyA38ToxvM-UIYD6x4fqQdE4gsyDxYE2Y3pnGorEYOZ_HYtkx7Ua8m1MDx0MMt18vM_mRlOk4oNsoWz1SnNWRluEo_u2p1jMVXFGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/K8kY7lAyVTpEJO04JGROakMa5eIOB1knOuN7gsoUC4TKGWGfXIhdtAy1pa7Y8ab9I2-1lp8rb8RMQnOp4wGrqIsNVxwMqljdyR6G5IHhcoyqlBRkoGUTS2vWkGgN2MR9mnc3uVDxwsVOutuhtbeGBHHlZTvzddGBNpZjAYgON69dABI-Uha13u6LJ6wfmimZ_9Q6mq_g9lw7aT-n1ZPBLxLGL1P06hnrd5IXnjd4E80RKGm0xjm-EBh_F4OfL6dqT5o2LhPl7znbpK9OwozEy01cGPvEJrif2iq0VsceoniL1BgDeMDAof15G7BFeuZQl5jPGiaqmrmzUpR1qOgn5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/d2Ur3CsPt5uiibvqOcFji-HVUwioRK7zRwG1NWrIGEkP4Cnlhmw6Wm6JI88SArQN8ryvF5IJaZ3wdzlyu-Z28ZV2JrHhq4fM6cHZQkcpmI75tIEBcuDiHL0yiDfr_Pp4gjz-Isuvrzx_EV-3qvAWP2V0MyEAxVsLoFXFkSXj6WT0_EixkJJYB8Pf-DRqt8rO9L9ngAnjoNHJUyIQiNLSY2EBKM4NoZ356ojg4nnFtWLOYUziRHPVAZuTl_gBkgLuDXJR3QMQriuRCcrXkoj4kAoGwhio-xX2GGcBpWhYUrSi6Hy3xlCKKgTN2OkhhgO92GOWfGGTExx1zMgYlYQwuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/c3iiZi_kKe_mWO2Vt8t4U5_PeurbHvdbQOa-bvAAUy2zekIMm0A4WvIVw8XJyfW57ew7u_edjrBDjN29UmQDUeQHFG09BtcnF9HyLlbqxpUDO-DVNaevwln77ohuu5swjeu1AujB2j-_5WkR8pH7DrOAf7WBI5CiRZuCMK6HfhpJGNFKWJg5O-CFnD9yMTJxqrqT9JMzyDSN0PNx5bceQ8D8ZkhRFTvEPaeZ8KvRUZwC1Xj2TzHTZapV_gh1iW58gCun05VcLgAqebTxoIiJ6FCiNc61IsAog0Gtv0viqcx6cgaKRWRPd3F7thf-p55ZIrXfI7nq48qUSPhAbvRqIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nSwSispwCXHGeqeDJwhylEd60T4Z9fNHFs91f44s9T6Mv2e0TRhYQOQWbKJkJsgy9oNOKIRJ4jl6iG5DQXxy1347k11wMi0PFZ7RhxQnTxcPOl0ZwyQjaYZ-pqaRbBxxMGbnKy_WH3AFZAAyAJny0awtzYvWKEKQKEzcE839LTXYUK85F_qAknMmxdrfT7mcXiwUdNAakaY2dLF8cViefDkfIKIgFByctiUphL-Sw6sIHGqwQnsbc0nYIm-FzfNsDFKuU9MhGYdl_3U8XIv_tfhKtnK9i1e8kOZLbjI3_7a0XuPcmng-Z1n4VrnwVrq12HX4pdnzHUKKseWZ3Q_c8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hpXJ8hM2xDIxQXQjVH7M-AZk0dR8ZbfO3j_GFUXJjk9ZF6TzB5QBhMGYqBbev2HpgW8EdHvvgSt04YTk4JX2KhnFsaKL2JoKjzTn78CPcjMi670mu85speBVz80pNeCud55XaSxXifA8VrK_ZkVbJAg10YvzUnMD_uifCqgyHTQGEDoa8g8nXg3ITu7F3u1ZuMd_7qsbk_G1xejtWS7D-wB-5kQDTSXZDHZsLvrzQfWYhMbecXfaZWVw6xfzjPyBIch1mNQNq9csPKbIIAWalrvzz6Xe696fIqQkEfbmSnv8Q6gJmJuzYvVOxIglz5MJDKjo_EcSnlIqQaeR00EEwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uYIQ-Me1Lxhw-NvjE-2xNU4jSFlnnfXBYm3hHsh9EzOK15fuyG7t9z8O9K3CpfbhIMlU9zx5LxwKqRc3V9n-N-PFoezqe-k5MNcGbj5i-rRMucPs9yqq7KgaiBhQaVsPNlY9yQLHpNK8qI_T6MJH1orddmJnn83IFzSSaMFw4NppwPFepq-2Mh0bHxG16OaGS6l3vdMJWUJCriQNbo8aESFx3LhEdG6NNVKensyf_oIzM8LurKm8V0iDuSJcsMRpAAye1w10BtDr2oCKnYvd5YEB93_-wNNJhxQjydBRF9ZxDvQ-V-1GJIzmfBNWGxdjaL6_eZv4nfPNKocGKh8TIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fXmQo7kR2En5vor-Ncc_w9oydVnNof9qH2aw5fYPIydnKX36P0UYpV1XgRPADyDWJI-cKxj47Zkk2YpieTLNHiylvvZVb9tVdEI4bIcJ83DFMlJ8I9DjZlfdcLvYssHjs6vow0C0_Wd1nSA4H0VlGKB9Y5vMDh19qW3BTD1stnwAVd_sR-Kv_G-s3XnNdiLpLdrl5lISqL05ciHYfs2JE9EoJEcMUzu86zYzX_XP0l6znxfW1NtedriqPQczdaTx0ne2XrIDQQhrH0ouVHx8ap0Hrc40nT6zxiG094NoMQkxSlY2zqEah5DS17QxEz35wsdwx7c2VjNSw2S2V32rEA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">◾️
روایت تصویری مخاطبان خبرفوری از لحظات بدرقه و وداع با رهبر شهید
▪
️شما هم روایت تصویری خود را به شناسه زیر ارسال کنید
👇
#بدرقه_یار
@badraghe_yar
@Badragheyar</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/akhbarefori/669124" target="_blank">📅 17:43 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669123">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">♦️
دریادار سیاری: حضور نیروهای مسلح کنار مردم، نمایش اقتدار و آمادگی ایران است
🔹
رییس ستاد و معاون هماهنگ‌کننده ارتش با تأکید بر اینکه حضور گسترده و میلیونی مردم در مراسم وداع و تشییع پیکر مطهر رهبری، جلوه‌ای کم‌نظیر از قدرت نرم جمهوری اسلامی ایران است، گفت: این سرمایه عظیم مردمی، همراه با پشتیبانی ملت از نیروهای مسلح، مهم‌ترین عامل اقتدار کشور و ناکامی دشمنان در تحقق اهداف‌شان است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/akhbarefori/669123" target="_blank">📅 17:43 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669122">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dca6861c19.mp4?token=XWgMBfzFCnOOYjNLfIXO_PDPoOikVVQcCKsmTnHSf2kJCfphbYi629FnNjCuiFTqyr-IfWDXdNDyZcktXP1i2-BibJNlvmkUwFYzJA9k9AF6oKQa0mrgQhCPowcI_65VTKIVjQT4vB1nXNer03DvnSab0AdbXwWsCu6EUnqF2ZBcWTTHD9SsZemjFeveVZ2H50rpThKy4tbqvpe6bZC3N39tqtSxNs7IsbqGnyU3obBcdHPlsP4t3w9PwP2CT4PpHmMFmqITA_f8-cqKut44W1BU78xHWaz-fK7PdEKTavrFxfd2qq70NofmBvaRC0k28BIDaG2IRv3mnkuNLeuKHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dca6861c19.mp4?token=XWgMBfzFCnOOYjNLfIXO_PDPoOikVVQcCKsmTnHSf2kJCfphbYi629FnNjCuiFTqyr-IfWDXdNDyZcktXP1i2-BibJNlvmkUwFYzJA9k9AF6oKQa0mrgQhCPowcI_65VTKIVjQT4vB1nXNer03DvnSab0AdbXwWsCu6EUnqF2ZBcWTTHD9SsZemjFeveVZ2H50rpThKy4tbqvpe6bZC3N39tqtSxNs7IsbqGnyU3obBcdHPlsP4t3w9PwP2CT4PpHmMFmqITA_f8-cqKut44W1BU78xHWaz-fK7PdEKTavrFxfd2qq70NofmBvaRC0k28BIDaG2IRv3mnkuNLeuKHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
برافراشته شدن پرچم‌های انتقام در تشییع  ۸ میلیون نفری امام شهید در مشهد
#خونخواهی
#تقاص_خواهید_داد
#WillPayThePrice
⁩
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/akhbarefori/669122" target="_blank">📅 17:42 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669121">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">♦️
عراقچی در گفت‌وگو با وزرای خارجه عمان و ترکیه، آخرین تحولات منطقه به‌ویژه تنگه هرمز را بررسی کرد و بر تداوم رایزنی‌های دیپلماتیک برای جلوگیری از تشدید تنش‌ها تأکید شد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/akhbarefori/669121" target="_blank">📅 17:41 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669117">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bHmw7thPk9yFZK1vG7YTy1XUaSW-_i13lrQzxzk_iNiOnXWGNYfwiCr5ku_AHGIX87zkldH4uAsHI5enuNSDdeF8Ydl8Dkvnxeu7tKeCnEVLz4U6Dbgh6FmyuaS0O-0SE4NIkR4n921zqExAVnNN_IWD6Hxt0ARTkUXuULjKKsHeYaeMMKqf-KW7OVzoGJjItshq29pOI6gl_9qOEIjhZsZd58bXJO_XcuDo4U99ykYiJ_MVRQrNKRq6tfZOf8pxfU4hVKBZyiq4djefQuh9Hal40arM8zn4JwxS0UdR9l0rndcQ-mjj03LjlvEw4V1URmozMzqMDsstrhxcfvgW6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vA6aPqIGiewOJWA4qme-vuyoNZU7LzSsCm9hUD1k_24ln97VBPU7E-wbsM45O4H04brhD99VwKEmKS1uoIZazKqXxcpTS_xvc4VyjgNqenZFYFUKMQ33MGUbTK1hmzws2uqUe0UeehthpHSlQiCSgUA_oxKf9xwV_0j9crBg2rQo3VIr1zLy33qomoqG986g0NrWzJ9CVaTHpA4bR55rn5NYh-Q-WnTji89eo4ipnUDPIiNUrc2Ho9xHBmLRA1fnjICQV-VWESqNyBZMnEByrG0QhPBaP9FiO1cSbUmJNXysWzXIe6NmjOvtkEm1OUyVIlV9ja-FMhsQAnGKR8Ybgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rBV3qTFEXooJWgayO1z0ouuzf6gdoNBqNaV-nPboSqzhxSaufD6p0JrR6TgzU_Vqlg0Dv2crmf9kBAY4Ma26tDBnbZqwbyOSpQvJtRhLMSAoqJy92RBBF7CB5D1nF4IkxdzyZV09XuQ0LHgtQ82FeQpIijaOL1OOKpfJ5rECqDM6DAYMf5EtQymEvgbLmA0UetfUROUzDuRLk8-YORXybcLpIK9fU-d-MMs0ootyGz75SV11dd955lwt-fGNNyVfE60HZPFvrO-FtpFwrtNKOoDqq1RyxWqZPyvcxqYtLHanY-U-Wt2jMjueypGAzDxrJtv7XEsqoWxERT-86kzgUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nlj_ZwR4PVoVhyzINUcuKSzh16TDJDn_hPSLeuc_stB-XF3HZYcuiBm7zsTc16bOxgz3Yq9EOcTjdVrfHEuxVTnwOkSCsXBMiT3FrQMyqnv8va5XUCrEsGPwgqhplt0kmW_1KLmN4WVMTPrq_m0x6UY4Wiul_SHf5dynqgbMLupwwNkQ8XCNCUmCgkwCLQRKniZ60r5CBx__sAbUgEJ_qvcC3sg5eobXrmVqXDNuvsplBNRMLizJ-0n2XKotvFdj9jVAhSMQBVAjik7wOhdjlwoYFTufMXJjFepUaqZr9L3Hg3ExqHbce5zV8KfTi2NoBlUeM3GGWEUzCbPPQZ-dGA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
معاونت محیط زیست و خدمات شهری شهرداری مشهد: از اکران همزمان و یکپارچه ی مراسم تشییع به صورت پخش زنده در کل مناطق شهری با استفاده از ظرفیت تلویزیونهای جدید شهری و کیوسکهای هوشمند شهری در شهر مشهد مقدس خبر داد.
Samesh.mashhad.ir
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/akhbarefori/669117" target="_blank">📅 17:40 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669116">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9e6f04bbe3.mp4?token=sZseQmVo4SM6N_M82_wd5y2uOqnBJPPD3DDWtusMyRfVZRTRRVjCFSrC-p7EPEil9z_zFyDomberG9q4OfpsQKC3AEESeT2J64Hcx8eqVaKz22x4KUaN-DAE88raql5rXuz-zCFz2l5h6_qkO8YXUc83GzqkKG54Qh6bfCLBX8L5TJIy9I4cp19FWXfZmwYvorz2Rxntnp2aOYI9d069ykjdt44SclbRWpoT7jlcIDt3s5NHZRZLNd_mca2QSkdwdw9DavZiEX2IUTLFQ-PdcIwJl6tneU-w6_26r4tv6JeldZYMSTqBCVI2yM5yO8v6hszKJm3jtQLiBN6n1BYCyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9e6f04bbe3.mp4?token=sZseQmVo4SM6N_M82_wd5y2uOqnBJPPD3DDWtusMyRfVZRTRRVjCFSrC-p7EPEil9z_zFyDomberG9q4OfpsQKC3AEESeT2J64Hcx8eqVaKz22x4KUaN-DAE88raql5rXuz-zCFz2l5h6_qkO8YXUc83GzqkKG54Qh6bfCLBX8L5TJIy9I4cp19FWXfZmwYvorz2Rxntnp2aOYI9d069ykjdt44SclbRWpoT7jlcIDt3s5NHZRZLNd_mca2QSkdwdw9DavZiEX2IUTLFQ-PdcIwJl6tneU-w6_26r4tv6JeldZYMSTqBCVI2yM5yO8v6hszKJm3jtQLiBN6n1BYCyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خبرنگار صداوسیما: تا ۲ ساعت آینده پیکر رهبر شهید و خانواده ایشان به حرم مطهر رضوی می رسد و مراسم نماز به امامت آیت الله نوری همدانی برگزار می شود
#بدرقه_یار
#اخبار_مشهد
در فضای مجازی
👇
@AkhbarMashhad</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/akhbarefori/669116" target="_blank">📅 17:33 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669115">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">♦️
فرانسه و آلمان خطاب به تهران و واشنگتن: به مذاکره برگردید؛ آنهم مستقیم
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/akhbarefori/669115" target="_blank">📅 17:32 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669114">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">♦️
روایت زائر عراقی از حضور در تشییع رهبر شهید در مشهد
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/akhbarefori/669114" target="_blank">📅 17:31 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669113">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf3692b8c6.mp4?token=gz7_H0GZVbbr1r0Q3X_IjqUXUvzRT8uc8bxgrra_n6th6TpIF0U0fDQOVf7uRlaPPG9NueMJpaX84DwHazqex8DUJBfHfO3ouYdxL0tuueePUkCaKhFsRR5Khomjb190GbuzuDn1TMMA7HJVig5B6u7gDds5E7uTd0Xeu0jFeKayx8EWhzkJpw6L9cFsiZS2R-MEwyJSTeQjiPHPUpdxNMWghhrOfmUWPJhygLKqYG_9ko4u1UwMYW0O8FQ6_Jh6bnsoA1ed32ikqqT7U3BSD18cNmGwDHZm8CGYi-VdrRDXCeywtCK6z0MQq_iPLg7aFRRH2IeoYGKfut5cSMYlGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf3692b8c6.mp4?token=gz7_H0GZVbbr1r0Q3X_IjqUXUvzRT8uc8bxgrra_n6th6TpIF0U0fDQOVf7uRlaPPG9NueMJpaX84DwHazqex8DUJBfHfO3ouYdxL0tuueePUkCaKhFsRR5Khomjb190GbuzuDn1TMMA7HJVig5B6u7gDds5E7uTd0Xeu0jFeKayx8EWhzkJpw6L9cFsiZS2R-MEwyJSTeQjiPHPUpdxNMWghhrOfmUWPJhygLKqYG_9ko4u1UwMYW0O8FQ6_Jh6bnsoA1ed32ikqqT7U3BSD18cNmGwDHZm8CGYi-VdrRDXCeywtCK6z0MQq_iPLg7aFRRH2IeoYGKfut5cSMYlGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دریایی از انسان؛ اعتراف سنگین مجری سابق CNN به سیل خروشان جمعیت در مراسم تشییع
این یکی از بزرگترین خاکسپاری‌های تاریخ است؛ رسانه‌های غربی دیگر نمی‌توانند این جمعیت عظیم را نادیده بگیرند
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/akhbarefori/669113" target="_blank">📅 17:24 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669112">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c7a7390bb.mp4?token=CFomYaf4ILP2ZL8X4Ek__mNi-qz_DsoPFdBSSqp8FcCXVBC3XsEM6FYfUdp_ehqimvXK7N7Hm0UAcP14ddpRywK3pCVlwuG5-c3fXjjl9AL8TgduqvPh6pCGo3H_7tChPg7ZlJ2EJnSnIoTjBIWoglZ1RyJYY8hfquqSiFvPWz14UzDzfB_d67Mad3tWFHU5kzT8OGfA4jaVXLxHZ9VyciaPcM1UuMzIElwI64onY7jh1O5s_4736odAiJEiM22p_6II-ASKz-6Mt2rZTpm_4CQR6pipNmhNzlEUqCz2lkie01yrLY3W83P-OAukJ_SyoUPVffXfYqjMegq95AYmaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c7a7390bb.mp4?token=CFomYaf4ILP2ZL8X4Ek__mNi-qz_DsoPFdBSSqp8FcCXVBC3XsEM6FYfUdp_ehqimvXK7N7Hm0UAcP14ddpRywK3pCVlwuG5-c3fXjjl9AL8TgduqvPh6pCGo3H_7tChPg7ZlJ2EJnSnIoTjBIWoglZ1RyJYY8hfquqSiFvPWz14UzDzfB_d67Mad3tWFHU5kzT8OGfA4jaVXLxHZ9VyciaPcM1UuMzIElwI64onY7jh1O5s_4736odAiJEiM22p_6II-ASKz-6Mt2rZTpm_4CQR6pipNmhNzlEUqCz2lkie01yrLY3W83P-OAukJ_SyoUPVffXfYqjMegq95AYmaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
صحن پیامبر اعظم(ص) پیش‌از رسیدن پیکر رهبر شهید مملو از جمعیت شد
#بدرقه_یار
#اخبار_مشهد
در فضای مجازی
👇
@AkhbarMashhad</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/akhbarefori/669112" target="_blank">📅 17:20 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669111">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2154c194c3.mp4?token=NI70pPT5A1XaXwDM1dyYkUShhApzXneIgUab54gSTcicsDuE3mTNPKpRb3IEmOLppkIZly9dkWL14Aa_wee0CjjLJAcKT8-7TPoe_JkQFeMlg2CbRlzD9Elwy2WXPUnMsdK7S7KFJYa8knHG3h9oIWzIEY3cZpwej1BUCjssoZg6xdhP1R41GLykQq0wW4kuqQ5tg2W6FzFJbW1eV1tWH4C5gNEN_66C2RXqbFk5TVbqtu8luj2-FS_uyjkOMO1csjLRTjhzo__mhSA4bbSoaR3JG6mzjV4SxjAG2xAx6exS7qr7tGMfMhLtZeU3-XH4r-HpBnca6WjHcmSwn2th6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2154c194c3.mp4?token=NI70pPT5A1XaXwDM1dyYkUShhApzXneIgUab54gSTcicsDuE3mTNPKpRb3IEmOLppkIZly9dkWL14Aa_wee0CjjLJAcKT8-7TPoe_JkQFeMlg2CbRlzD9Elwy2WXPUnMsdK7S7KFJYa8knHG3h9oIWzIEY3cZpwej1BUCjssoZg6xdhP1R41GLykQq0wW4kuqQ5tg2W6FzFJbW1eV1tWH4C5gNEN_66C2RXqbFk5TVbqtu8luj2-FS_uyjkOMO1csjLRTjhzo__mhSA4bbSoaR3JG6mzjV4SxjAG2xAx6exS7qr7tGMfMhLtZeU3-XH4r-HpBnca6WjHcmSwn2th6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
زائر رهبر شهید: مردم ایران اجازه نمی‌دهند حتی یک وجب از خاک کشور از دست برود، تا پای جان برای دفاع از ایران ایستاده‌ایم
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/akhbarefori/669111" target="_blank">📅 17:17 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669110">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/961d949833.mp4?token=kruGgAnelbjXInxQFQOgX48h60WYJT36EgGCWcvILE1SLUwcRRJ_2DQZ6izB5B6hxASdzP9KcuFrJw1LcIkNcWwwkKwdKs7CVz9Z03KWDorxH84CWS3ktj9JU2PutDMzaa9AVAmdR_Q1lwrheU-duQJ9pC2Fw1cGU6yrgQEiXIyL4IDVjDCf8A5yI97xR2EqY74BQYq6BjTqwVGc0j523pXPEuO3anKsWi7f0AWDB2JuYiPqhCnZCJvbrhifBHLONNvW_D33PwmP8KTHk3RJGm4hmcuxHyh4qwS9zBcutbUTH2kkVfMXdhzRDB_ypsHo-7aNh71gNDRVGC-DtUFR1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/961d949833.mp4?token=kruGgAnelbjXInxQFQOgX48h60WYJT36EgGCWcvILE1SLUwcRRJ_2DQZ6izB5B6hxASdzP9KcuFrJw1LcIkNcWwwkKwdKs7CVz9Z03KWDorxH84CWS3ktj9JU2PutDMzaa9AVAmdR_Q1lwrheU-duQJ9pC2Fw1cGU6yrgQEiXIyL4IDVjDCf8A5yI97xR2EqY74BQYq6BjTqwVGc0j523pXPEuO3anKsWi7f0AWDB2JuYiPqhCnZCJvbrhifBHLONNvW_D33PwmP8KTHk3RJGm4hmcuxHyh4qwS9zBcutbUTH2kkVfMXdhzRDB_ypsHo-7aNh71gNDRVGC-DtUFR1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پرواز جنگندهای ارتش جمهوری اسلامی ایران بر فراز آسمان مشهد همزمان با مراسم تشییع پیکر رهبر شهید انقلاب
#بدرقه_یار
#اخبار_مشهد
در فضای مجازی
👇
@AkhbarMashhad</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/akhbarefori/669110" target="_blank">📅 17:16 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669109">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f98c78bc00.mp4?token=ooDrQ7S94C8022hZOXtFXr_QZGKTyS7fT7Gt_3b2Al2cFhWjhXMfwtOmd-tfVDBrzGGp_W4tGANAHKJl5pQheI1zcAJLaHeUNGobjteQBKCHvMbrUzrD8EldI6KUNzWv7e73ywKmpL7UBHr9PhboVm_yq7zRvL1U-nludbF3g1aWq_YodsCff5K7otcmfYbs1z2aVqwoLgAqz-z7Ifl3ZfMpV_lGBU3PtM3BEsCEArkDj2j8Kdzw3FdTSvjCMlD5cRNUHnfBjkPHPk-vx6x-colZRktZ9000FuqoB5ixxqgNXVFFFoQWYMD7taHZAVneghzB9PYLgwouxZsL5twm44WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f98c78bc00.mp4?token=ooDrQ7S94C8022hZOXtFXr_QZGKTyS7fT7Gt_3b2Al2cFhWjhXMfwtOmd-tfVDBrzGGp_W4tGANAHKJl5pQheI1zcAJLaHeUNGobjteQBKCHvMbrUzrD8EldI6KUNzWv7e73ywKmpL7UBHr9PhboVm_yq7zRvL1U-nludbF3g1aWq_YodsCff5K7otcmfYbs1z2aVqwoLgAqz-z7Ifl3ZfMpV_lGBU3PtM3BEsCEArkDj2j8Kdzw3FdTSvjCMlD5cRNUHnfBjkPHPk-vx6x-colZRktZ9000FuqoB5ixxqgNXVFFFoQWYMD7taHZAVneghzB9PYLgwouxZsL5twm44WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📷
تصاویر از ضبط پول‌های جاسازی شده در ظروف آب در منزل مقام عراقی
🔹
نیروهای امنیتی عراق، ۱۱ ظرف بزرگ آب را که در منزل متعلق به عدنان الجمیلی معاون بازداشت شده وزارت نفت در شهرک تکریت(زادگاه صدام معدوم) در استان صلاح الدین جاسازی شده بود، کشف و ضبط کردند.
📲
🇮🇷
…</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/akhbarefori/669109" target="_blank">📅 17:13 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669108">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/81e74e2b8f.mp4?token=HL4Xh9oK287thdhm9STsSfy1ENomQ5jBziLMLd5UpEUAi0VMW2oKsTBxkgj3daMPrTQJhpxaTgDaL5bltnVmP3JBza1JcrGHbdluvqcgiQ8dfnyIA5SsSWb8luc6TiDtNE4Unuhbwmr6D59DLlahiL5PF4WkVd_Mnyko4KSHoyO-RA-0HxbAdgUpDNzcIDwtZUD7K-OFUyVBM23Yktv4TVD7wGRjEzN-JMFZnWw2xKrxssK2Tat6oUy9GB2wKefNXpobgLf_tR01rt7JmD_V_L88GzPZDAgzuAg3y9FZpxtFB24F2RzBKP9MHS36RKu_xWl7cZcbsSw0b3DhqUIN0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/81e74e2b8f.mp4?token=HL4Xh9oK287thdhm9STsSfy1ENomQ5jBziLMLd5UpEUAi0VMW2oKsTBxkgj3daMPrTQJhpxaTgDaL5bltnVmP3JBza1JcrGHbdluvqcgiQ8dfnyIA5SsSWb8luc6TiDtNE4Unuhbwmr6D59DLlahiL5PF4WkVd_Mnyko4KSHoyO-RA-0HxbAdgUpDNzcIDwtZUD7K-OFUyVBM23Yktv4TVD7wGRjEzN-JMFZnWw2xKrxssK2Tat6oUy9GB2wKefNXpobgLf_tR01rt7JmD_V_L88GzPZDAgzuAg3y9FZpxtFB24F2RzBKP9MHS36RKu_xWl7cZcbsSw0b3DhqUIN0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عزاداری زائران در کنار خودرو حامل پیکر رهبر شهید انقلاب
#بدرقه_یار
#اخبار_مشهد
در فضای مجازی
👇
@AkhbarMashhad</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/akhbarefori/669108" target="_blank">📅 17:06 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669107">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3134345d79.mp4?token=X-sDFlX5Kfz2EjC6-7eOUXdMbbC4xs-aHlud7yo3KmlTGyceQX1tYihZcyR6mTw3EicfWuootqeLpVIcC4qzBjcatJYBb78pvc4GlwvIYSe6kd8REfdvkl9mxkgoMN-6HhpVd0ZtxBGNYIahPJhURz1FCF8U3F_ZgfQLRyVHR5rBAprcOcE0B3js6krRfNP2wce200hh62CwivJracwzwgl4RUcMs7OFSOJ8Xp_M_0iBYopO7UYNErcT6hGL496IRdCK1Sa88wm4iGag-9GHDltQhnbau-XKGNNNAo2NujmyXs7Ez3J4arlKzCuPTEiwcXsARwL8bAApHvS9B1RTYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3134345d79.mp4?token=X-sDFlX5Kfz2EjC6-7eOUXdMbbC4xs-aHlud7yo3KmlTGyceQX1tYihZcyR6mTw3EicfWuootqeLpVIcC4qzBjcatJYBb78pvc4GlwvIYSe6kd8REfdvkl9mxkgoMN-6HhpVd0ZtxBGNYIahPJhURz1FCF8U3F_ZgfQLRyVHR5rBAprcOcE0B3js6krRfNP2wce200hh62CwivJracwzwgl4RUcMs7OFSOJ8Xp_M_0iBYopO7UYNErcT6hGL496IRdCK1Sa88wm4iGag-9GHDltQhnbau-XKGNNNAo2NujmyXs7Ez3J4arlKzCuPTEiwcXsARwL8bAApHvS9B1RTYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پرچم متفاوت خون‌خواهی مردم: ترامپ را خواهیم کشت
#خونخواهی
#تقاص_خواهید_داد
#WillPayThePrice
⁩
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/akhbarefori/669107" target="_blank">📅 17:05 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669106">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c89b01cb4.mp4?token=Q3xAvNxM1Y-cZE2l-BcavhUOmKbowHV2jPxk-h2DfXNtdxXY_PgUtfgTX9RCaq9tKQFQirq7z3AGk6nKOvfDjCXRzR2TILCAtChYFascPmF9TEjdlp1bobyvpv4Pl0R0fH6pcc3QwbTyYvnxO6i8jHOpnuhDEgFfp-eFYNgnhUuUAy793dy-8L8CDBwP1B3cD3zMCKRhQXNQr1kjUZP2KOMcHgLAA47zhnd0d89nx2jluODGRqWOu71M5FxS2CaBdDMq6HDh9eIEoeogn09xtVgeT6K8ChCawuIGLzQuPCFVQc9mv2QmXupOifr-JOwpnBVpf44vNIEPinWVe7lRdoPu4dnuZDnpp3ImISto4Aq-78PWNsDbVboMYWBGzS2HsjZXhe8kkuWzexC66lGySegFAzKeNjthZzKpwoe6nQ7KhNgo2A88XptHVRO5AgiPsC5GPMqVnUOMTj10ehSBB0M1YtZzVG5xLxgBis6v5YBEmqj1mhOOKb7_DlwGgc1Re3bjQ4zcfJgcsLxLDXL1-ZLtD5pvUEuu4blLVrAkPcXwAFZ8AuErCBNAx-cg36GwiedakxIBgybsEvM1vFHG9w6ZDtvHljhAKGmVJ_kz9FaQHUyMmQ7CPMC3abnU-l2a9Mseun8KnGqIp1ca2zPeRxJyLxTbG6QEO2gPLBWRDcU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c89b01cb4.mp4?token=Q3xAvNxM1Y-cZE2l-BcavhUOmKbowHV2jPxk-h2DfXNtdxXY_PgUtfgTX9RCaq9tKQFQirq7z3AGk6nKOvfDjCXRzR2TILCAtChYFascPmF9TEjdlp1bobyvpv4Pl0R0fH6pcc3QwbTyYvnxO6i8jHOpnuhDEgFfp-eFYNgnhUuUAy793dy-8L8CDBwP1B3cD3zMCKRhQXNQr1kjUZP2KOMcHgLAA47zhnd0d89nx2jluODGRqWOu71M5FxS2CaBdDMq6HDh9eIEoeogn09xtVgeT6K8ChCawuIGLzQuPCFVQc9mv2QmXupOifr-JOwpnBVpf44vNIEPinWVe7lRdoPu4dnuZDnpp3ImISto4Aq-78PWNsDbVboMYWBGzS2HsjZXhe8kkuWzexC66lGySegFAzKeNjthZzKpwoe6nQ7KhNgo2A88XptHVRO5AgiPsC5GPMqVnUOMTj10ehSBB0M1YtZzVG5xLxgBis6v5YBEmqj1mhOOKb7_DlwGgc1Re3bjQ4zcfJgcsLxLDXL1-ZLtD5pvUEuu4blLVrAkPcXwAFZ8AuErCBNAx-cg36GwiedakxIBgybsEvM1vFHG9w6ZDtvHljhAKGmVJ_kz9FaQHUyMmQ7CPMC3abnU-l2a9Mseun8KnGqIp1ca2zPeRxJyLxTbG6QEO2gPLBWRDcU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
«تفنگ پدری» با صدای پرواز همای منتشر شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/akhbarefori/669106" target="_blank">📅 17:05 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669105">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromموسسه نیکوکاری مهرآفرین پناه عصر</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b4ec89bdd6.mp4?token=hRjpZ6ihu7N3bbTZ-OvxjqYTrD7IoGcSkOguciLemmkQOnzlzoLtWzQHlLyQmBvjr56o-6PNbCMWh188HvulcgmcI2u8OaQWCLkTWn7kFeExY604ytVZafPzGN0mx3H2Ax2F_tMcK-CryxYjs4ocGwQyB4ffXwN0ylgmGaIPbsbs399W8umH76-Bf4v5qI4j2_eFBTwG3aGJSrF83BrlT7TfHW7KXhpFCH-IaEZIOmW70AoTtD01D7fljXp5BxXFIhBhhzvJhKnuDc15TocZ1epHw24D0cD5zRRa83RV7FZMdqAmWoxR3TppFlrml4UZljVJog6CeYg7SuxXwX3TL7Jo-3oTaPAL_uIgx9ZxjnVyxLQ-cICGrPsfNelwOasCqf7FkHp8KU6TSVbqcnQLJQ6G7NqhJPf42TeQ0xZHTySWa7TqMv4q-o1df7iWpyO0uwXnP3IG7ZljiNKFN_HJCX1C8OZMkwGlqR_YPNEHTet2i7E9B5wd6rS4rhv_FeBpUchXH2wmZu5iAqO-EbTb3lzK8oZyzJ8IeaQFv-alJqGW1BlIn1ci_pwC7chq-LLviUOigHmIGcH8-VHU2OZ2Beeu3AeAg3FVIuOztwxwLXDEpBIaXH2qQTI1K3FIE_rtLQW5j41jezLodrRmCIgoa5Sg4Z4vR82spUrt54ykV1U" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b4ec89bdd6.mp4?token=hRjpZ6ihu7N3bbTZ-OvxjqYTrD7IoGcSkOguciLemmkQOnzlzoLtWzQHlLyQmBvjr56o-6PNbCMWh188HvulcgmcI2u8OaQWCLkTWn7kFeExY604ytVZafPzGN0mx3H2Ax2F_tMcK-CryxYjs4ocGwQyB4ffXwN0ylgmGaIPbsbs399W8umH76-Bf4v5qI4j2_eFBTwG3aGJSrF83BrlT7TfHW7KXhpFCH-IaEZIOmW70AoTtD01D7fljXp5BxXFIhBhhzvJhKnuDc15TocZ1epHw24D0cD5zRRa83RV7FZMdqAmWoxR3TppFlrml4UZljVJog6CeYg7SuxXwX3TL7Jo-3oTaPAL_uIgx9ZxjnVyxLQ-cICGrPsfNelwOasCqf7FkHp8KU6TSVbqcnQLJQ6G7NqhJPf42TeQ0xZHTySWa7TqMv4q-o1df7iWpyO0uwXnP3IG7ZljiNKFN_HJCX1C8OZMkwGlqR_YPNEHTet2i7E9B5wd6rS4rhv_FeBpUchXH2wmZu5iAqO-EbTb3lzK8oZyzJ8IeaQFv-alJqGW1BlIn1ci_pwC7chq-LLviUOigHmIGcH8-VHU2OZ2Beeu3AeAg3FVIuOztwxwLXDEpBIaXH2qQTI1K3FIE_rtLQW5j41jezLodrRmCIgoa5Sg4Z4vR82spUrt54ykV1U" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این مادر، همسر و فرزندش را از دست داده، روزهای تلخ تنهایی و افسردگی را پشت سر گذاشته و امروز آرزویش، حفظ سرپناه دو دخترش است
پنجشنبه مهرورزی این هفته، برای تأمین ودیعه مسکن مادران سرپرست خانواری است که در معرض بی‌خانمانی‌اند.
🌿
نگذاریم هیچ مادری، سرپناه فرزندانش را از دست بدهد .
💳
6104337737614782
💳
6037707000289144
💳
6037707000426027
🔖
IR 180120000000001264298063
📞
*780*35260#
🔻
پرداخت مستقیم
Mehrafarincharity.com
🤍
🤍
عزیزانی که مایل‌اند به‌صورت مستقیم به این مادر کمک کنند، در واتساپ یا تلگرام به شماره زیر پیام بگذارند:
📲
+989101785282
⭐️
مهرآفرین باشیم
|
اینستاگرام
|
وب سایت
|
پرداخت آنلاین
|
❤️
@mehrafarincharity</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/akhbarefori/669105" target="_blank">📅 17:05 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669104">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">♦️
عمان با دریافت عوارض عبور از کشتی‌ها در تنگه هرمز مخالفت کرد
🔹
عمان در نشست سازمان بین‌المللی دریانوردی (IMO) اعلام کرد حق عبور ترانزیتی از تنگه هرمز بر اساس قوانین بین‌المللی تضمین شده و این کشور از وضع عوارض برای کشتی‌های عبوری حمایت نمی‌کند. این موضع در شرایطی مطرح شده که ایران در پی تعیین هزینه برای عبور کشتی‌ها از این آبراه راهبردی است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/akhbarefori/669104" target="_blank">📅 17:04 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669103">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d31dbfab06.mov?token=bIrwLdM2jJlgiv1nSnRFLtLnOxMXsuDDKwKg9rsKAYUd2XwBD9XdQCLTRQenWONIwfoskLhX68B9VwU6KMN8tgMl0B9sLkM0XwLBMmRkyj2_E73Ei2_r1W9rRJ-z4ce0ht2XsOy8h3kRwoZuSurhRnlHjDgn-ugnR5bnXCuZIRqsDd0wW7TO3SeVUObujv3nhBzmt26L5ivFMR9Rny09LYyBu9nj7Fctkgd8RtPMzF8WD9SODdC5hBhzQUVDE0QlhCOqM_Gaq6kmTufU2lIUz-B_8TzU0wjdE9At3epN-7ZQNsZAO1oTXdhDv_PIuduOTURJvIXcOuRfsjvgU88MCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d31dbfab06.mov?token=bIrwLdM2jJlgiv1nSnRFLtLnOxMXsuDDKwKg9rsKAYUd2XwBD9XdQCLTRQenWONIwfoskLhX68B9VwU6KMN8tgMl0B9sLkM0XwLBMmRkyj2_E73Ei2_r1W9rRJ-z4ce0ht2XsOy8h3kRwoZuSurhRnlHjDgn-ugnR5bnXCuZIRqsDd0wW7TO3SeVUObujv3nhBzmt26L5ivFMR9Rny09LYyBu9nj7Fctkgd8RtPMzF8WD9SODdC5hBhzQUVDE0QlhCOqM_Gaq6kmTufU2lIUz-B_8TzU0wjdE9At3epN-7ZQNsZAO1oTXdhDv_PIuduOTURJvIXcOuRfsjvgU88MCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شعارهای «انتقام انتقام» مردم از کنار خودروی تشییع پیکر آقای شهید ایران در مشهد
#خونخواهی
#تقاص_خواهید_داد
#WillPayThePrice
⁩
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/akhbarefori/669103" target="_blank">📅 17:01 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669102">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">♦️
بدرقۀ آقای شهید از قاب آسمان #بدرقه_یار  #اخبار_مشهد در فضای مجازی
👇
@AkhbarMashhad</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/akhbarefori/669102" target="_blank">📅 16:58 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669101">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sJswMeftjPzRCRG5yTDLDUl59LGRsX1MHhHttYeFmReQR-w8rBI7pegvXviwPVYmIGloTyiqwBoUJwXRV3WpdCcU-uFcdVIUMF81hErOujbybM03QmxUVgZ19_uTaPwjfRcgrs7RDzNFsgS0jUbfe8dNYo2Osabw5aXzuk4601fbzCk9m7nEHtCkclmyLezTLjueq5pBnv8Wzx_J3rjAAL1IJ2-xcdv4nlhv74yeJo-uedvP7oE6AiP2H6RMhjw5rG-apTR7KxMtXMsKUYsweT-psjKRZs6Ed1gR3M6EfjTceBmBnCByhjn5roaJC71B8jrSa2ltkp8OYMH5mPPqSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اجتماع بزرگ مردم مشهد در مراسم عزاداری شام غریبان قائد امت و شب شهادت امام سجاد(ع)
▪️
با کلام : حجت الاسلام برمایی
▪️
با حضور : دکتر سعید عزیزی
▪️
با شعرخوانی : محمد رسولی
▪️
با نوای: حاج سید رضا نریمانی و کربلایی علی اکبر حائری
▪️
با اجرای :  امیر مهدی باقری
📅
پنجشنبه ۱۸ تیرماه
⏰
ساعت ۲۲:۳۰
📍
مشهد مقدس، چهارراه احمدآباد
@AkhbareFori</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/akhbarefori/669101" target="_blank">📅 16:55 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669100">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d55b592dae.mp4?token=vU7O-5-xaG-q8gGF0OJWlJapk6EAHiLvzaspi25o9xMeINfaLchLQMyUAIsq47pS4Cnv1HUpA8GYoULrRlnxtO78LksGvnZ8q1Xa-YvmdewHQ3vIxlpKIfEkvltAsUc9QhTBL98rzaL6pKEBM0F2v5UIYHTP-q_Zr4P6oHzdDsIoyFH9CrMPU795RXG_RGe6ZEeF57JX8SfahM7LMc2_MeEuLw9BxOY1rIHnT5aiuoYrVm6X8XHwvS8ksYEzzHq1igbXKrBYny-tRviFjkMnhIr-XFZ_tiRPZUHD_72yqwuz7oNWhoTJ3oocAZv02uDzdF0hj6mBM7FgWvmr-W0j4xngFMMmklETumFSZOnRx-7ufayhYoii_-3juMu3OyyJF-027yiZN9ASyihHI2C6ElIGcT9oGHkrv0kbunHzhWknH65u1DyWG0xyTDFBNCZOc61elQMpkvY7KnnSY5UkIfrqL3Ze65-w4KxMtw8WM-ZBlT5MjjWz9ojWls4hbm-6w3PMKkidZiv8up_FoQ3-iilyvXeiA2NP8uPj4Cox-ZjJHV4Ugv-WMZljsAwnjKrP_D8pmDp_XQOWsHPzYMjQ237luN7rW7zNYXIeAweLFjTei0h4TPMjd6pguo1tDq-A_e1iYCe6tOjB7O_3-HPjKDHTqqvGiwIfDeKx6UicgWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d55b592dae.mp4?token=vU7O-5-xaG-q8gGF0OJWlJapk6EAHiLvzaspi25o9xMeINfaLchLQMyUAIsq47pS4Cnv1HUpA8GYoULrRlnxtO78LksGvnZ8q1Xa-YvmdewHQ3vIxlpKIfEkvltAsUc9QhTBL98rzaL6pKEBM0F2v5UIYHTP-q_Zr4P6oHzdDsIoyFH9CrMPU795RXG_RGe6ZEeF57JX8SfahM7LMc2_MeEuLw9BxOY1rIHnT5aiuoYrVm6X8XHwvS8ksYEzzHq1igbXKrBYny-tRviFjkMnhIr-XFZ_tiRPZUHD_72yqwuz7oNWhoTJ3oocAZv02uDzdF0hj6mBM7FgWvmr-W0j4xngFMMmklETumFSZOnRx-7ufayhYoii_-3juMu3OyyJF-027yiZN9ASyihHI2C6ElIGcT9oGHkrv0kbunHzhWknH65u1DyWG0xyTDFBNCZOc61elQMpkvY7KnnSY5UkIfrqL3Ze65-w4KxMtw8WM-ZBlT5MjjWz9ojWls4hbm-6w3PMKkidZiv8up_FoQ3-iilyvXeiA2NP8uPj4Cox-ZjJHV4Ugv-WMZljsAwnjKrP_D8pmDp_XQOWsHPzYMjQ237luN7rW7zNYXIeAweLFjTei0h4TPMjd6pguo1tDq-A_e1iYCe6tOjB7O_3-HPjKDHTqqvGiwIfDeKx6UicgWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بدرقۀ آقای شهید از قاب آسمان
#بدرقه_یار
#اخبار_مشهد
در فضای مجازی
👇
@AkhbarMashhad</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/akhbarefori/669100" target="_blank">📅 16:54 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669099">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c1ba311d91.mp4?token=heJsK2sh7mYg5fLHaO0xCoiyApPeEgzHwB0Zrbt1nMFr2iWHFMgq_P7U9To9wf2Kb8pUYaO2aOyulp3vDT_-ok7sCu8q4SXO2VoaluOTZTDZ0hCzTIQl-h9vi11RfaCYH3knHIUT7cj5sVwm3YM4H5YJTo6dpfwu8SCLWKs5Pg_V2IMp6AzWxFB6vL5VmyNrDnx1QOqpxqh_RK66NpEM41YgzrE8S66Io3mofXaZsVzAIgnZQpU7gNYv0TOztDp6A-huTIex-YaBU7TGV8s7G7CPVNz4Mf7fdK1C3lX8ZvqWhfMAyHX9YoL0iMEhNwQs5F88zqZDxGAUv3GxvCs1CQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c1ba311d91.mp4?token=heJsK2sh7mYg5fLHaO0xCoiyApPeEgzHwB0Zrbt1nMFr2iWHFMgq_P7U9To9wf2Kb8pUYaO2aOyulp3vDT_-ok7sCu8q4SXO2VoaluOTZTDZ0hCzTIQl-h9vi11RfaCYH3knHIUT7cj5sVwm3YM4H5YJTo6dpfwu8SCLWKs5Pg_V2IMp6AzWxFB6vL5VmyNrDnx1QOqpxqh_RK66NpEM41YgzrE8S66Io3mofXaZsVzAIgnZQpU7gNYv0TOztDp6A-huTIex-YaBU7TGV8s7G7CPVNz4Mf7fdK1C3lX8ZvqWhfMAyHX9YoL0iMEhNwQs5F88zqZDxGAUv3GxvCs1CQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حجت الاسلام هاشم‌زروندی: از تمام کشور موکب‌ها برای خدمت به زائران در مشهد مستقر شده‌اند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/akhbarefori/669099" target="_blank">📅 16:53 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669098">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7dfc6e9330.mp4?token=m2bAu2oxAvOdLiR8p1AXMextCRT2MSIbiNpGj-IFc-yGX90V1NEtdLeBRJu1a3cPywgDa9CAkY7gUccsjJapSqHjqznDME5RrnQDdqzh8tPyYCb2l5ko0P4ikQk7-7qoRsn_wvSTiMoiEwS4Kw82JKT9RyfHnnMgp0m1OCMg3OJIb_SFqDAcPNkRpUaZVlAzorKcH28lvee1aRC7CCyJnHSlunFt4AAvyFMec2w767LA7Tnd0rH_gFBF8ccQMaYHR9QDmL3QWGiu49c85cJW2a9fpIoMyaMEq_AwqG2B5aSo07JwGblmkvqMK6E3-Bk--s-OJ_nTNpthN9lLC8yzQLLDmAa7MrvzCKCuCHSUE-wa7xDvtAnSisIshSpOdT2rtD0Wm61JqDGwhbXeBdBiLOwN5lDhKrUEH2yHYPWeMzHIHkeeiFTROhPcK4JsqJF-lQ_x05vgGbJQG0amdrQQLvnk_sjYi0hZlmnP6AJWW2nCLVEBYbZFCNFE3vz9pmYWFTw0auRiX_KOqk3zvvSOqS6hl4_4FFS_0OV4rmv_vRMdGbKq_v5MvVCn1ihBw5hl4I3IWqNWg2I1k-B2_LJWxrLWfM81oy1K3-OIydlozmHFEsn0PSEQqspK9YUwqkcGi5bHR1I6TRm9eEuGVQQwR-x2Plpx7VMCaFkM6DoOUPY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7dfc6e9330.mp4?token=m2bAu2oxAvOdLiR8p1AXMextCRT2MSIbiNpGj-IFc-yGX90V1NEtdLeBRJu1a3cPywgDa9CAkY7gUccsjJapSqHjqznDME5RrnQDdqzh8tPyYCb2l5ko0P4ikQk7-7qoRsn_wvSTiMoiEwS4Kw82JKT9RyfHnnMgp0m1OCMg3OJIb_SFqDAcPNkRpUaZVlAzorKcH28lvee1aRC7CCyJnHSlunFt4AAvyFMec2w767LA7Tnd0rH_gFBF8ccQMaYHR9QDmL3QWGiu49c85cJW2a9fpIoMyaMEq_AwqG2B5aSo07JwGblmkvqMK6E3-Bk--s-OJ_nTNpthN9lLC8yzQLLDmAa7MrvzCKCuCHSUE-wa7xDvtAnSisIshSpOdT2rtD0Wm61JqDGwhbXeBdBiLOwN5lDhKrUEH2yHYPWeMzHIHkeeiFTROhPcK4JsqJF-lQ_x05vgGbJQG0amdrQQLvnk_sjYi0hZlmnP6AJWW2nCLVEBYbZFCNFE3vz9pmYWFTw0auRiX_KOqk3zvvSOqS6hl4_4FFS_0OV4rmv_vRMdGbKq_v5MvVCn1ihBw5hl4I3IWqNWg2I1k-B2_LJWxrLWfM81oy1K3-OIydlozmHFEsn0PSEQqspK9YUwqkcGi5bHR1I6TRm9eEuGVQQwR-x2Plpx7VMCaFkM6DoOUPY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جایی برای سوزن انداختن نیست؛ روایت خبرنگار خبرفوری از خیابان امام‌رضا(ع) مشهد در مراسم باشکوه تشییع پیکر مطهر رهبر مسلمانان جهان
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/akhbarefori/669098" target="_blank">📅 16:52 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669097">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6551db78e9.mp4?token=P73HDmjYyTx7AhTB0ksdjuW3zmfnjebGmsLPVHUaMnAdGzEqTHaXlQ90UmILY6-9rBipN5Ilgd6c6vd9Y4CDhodmvwgNfmuw6rv-g07AU5R6jfhAukERFquUTTqaN_GGavLQb-NvSuALAzUwJ5RKPyFLLBZ8csja0XJEZjQ04PoZ-6PeVZQjEkouVLkAvYk3vj9Z70qctsG2FYFqwNckpAPht00wtqjCvzX4d9K1av60ZXMCRV5LaVKFC5yJON6N4QTGsbJv10kvpa0fQzbJVNCUnPFDZo1DT0BrER7FsXK4T15yIycHLEEskeF_NZJw5FsLcaXvgVkxF2Bg7k5Xyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6551db78e9.mp4?token=P73HDmjYyTx7AhTB0ksdjuW3zmfnjebGmsLPVHUaMnAdGzEqTHaXlQ90UmILY6-9rBipN5Ilgd6c6vd9Y4CDhodmvwgNfmuw6rv-g07AU5R6jfhAukERFquUTTqaN_GGavLQb-NvSuALAzUwJ5RKPyFLLBZ8csja0XJEZjQ04PoZ-6PeVZQjEkouVLkAvYk3vj9Z70qctsG2FYFqwNckpAPht00wtqjCvzX4d9K1av60ZXMCRV5LaVKFC5yJON6N4QTGsbJv10kvpa0fQzbJVNCUnPFDZo1DT0BrER7FsXK4T15yIycHLEEskeF_NZJw5FsLcaXvgVkxF2Bg7k5Xyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پیکر مطهر رهبر شهید انقلاب در آغوش ملت عزادار ایران، وارد میدان ۱۵ خرداد مشهد شد
#بدرقه_یار
#اخبار_مشهد
در فضای مجازی
👇
@AkhbarMashhad</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/akhbarefori/669097" target="_blank">📅 16:49 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669096">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aZSkD0MRq3rNX-n_E6sMjgtesbmYyhPVvGH94OZuqDlnBmlKcRgENEPnsrUSZrHZTxvjV0UyksCLr66-KpIuwTPGYm_dDvPhTXFQTJnyV5WCCRWufv_L4g16EQ-1o1VeebJ_d_X2oW5wSZZGQ9GjfTWmOfX9jJRg8wswKrWToBAmgl3vo5N68-SJTqfsMyp8URoL_07VJgFftNqqiK9XuOg-AU-mc8OxZCUEBu3kk8_mTnk-XeJbZLVM8P_aOkYCLFapDKLAFR8blWhmFGXgSY2YnQKHp5RmEDz0d60G3Y2KGY-D6MyaeMPzTA0ZW7PGa_AXV62DLxvK3jXG5Kl6tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
«مسئولان عزیز! چیزی که باید از ترامپ بگیرید امتیاز نیست، جانش است»؛
تصویری از پلاکارد یکی از شرکت‌کنندگان در مراسم تشییع رهبر شهید
#خونخواهی
#تقاص_خواهید_داد
#WillPayThePrice
⁩
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/akhbarefori/669096" target="_blank">📅 16:48 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669095">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a19f17395f.mp4?token=K2JGOiU7MMZQjeyHHc3o0H-5COVel5LHoLN0k3Rw4jtAPD2Ei-pvF1ibNlr9-doXDgvX44YLBFnYFBaGI6pe2hIxz4PQSKie058axC9x0Jnak6acaarH0JSkmwkRQubcdqOdA7F83zFdmUHTRkKWzWVRlhW0PoIvPq3jWZnWdw18nXd1N4E4l2B4X2AhuCqHrnjIZpGFURsXAERmGg9J8IzAjdpXhrpR5qNA5oaZ_9b0AVs4eW9N-OW0T_d7bOW9bCjCfV_nDVxUd9BzKj53TjlzDpz4cV2OPWZc7tvGjm9FRicPuE4dqTgmZLUWm2iEjQPI78agW6jEeRTC-5T6YjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a19f17395f.mp4?token=K2JGOiU7MMZQjeyHHc3o0H-5COVel5LHoLN0k3Rw4jtAPD2Ei-pvF1ibNlr9-doXDgvX44YLBFnYFBaGI6pe2hIxz4PQSKie058axC9x0Jnak6acaarH0JSkmwkRQubcdqOdA7F83zFdmUHTRkKWzWVRlhW0PoIvPq3jWZnWdw18nXd1N4E4l2B4X2AhuCqHrnjIZpGFURsXAERmGg9J8IzAjdpXhrpR5qNA5oaZ_9b0AVs4eW9N-OW0T_d7bOW9bCjCfV_nDVxUd9BzKj53TjlzDpz4cV2OPWZc7tvGjm9FRicPuE4dqTgmZLUWm2iEjQPI78agW6jEeRTC-5T6YjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کثیری، کارشناس برنامه پرچمدار: اگر پیکر رهبر شهید در سایر کشورهای همسایه مثل ترکیه و پاکستان یا هند هم تشییع می‌شد، آن‌جا هم شاهد جمعیت عظیمی ‌بودیم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/akhbarefori/669095" target="_blank">📅 16:45 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669094">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pri1E1zpdk41_QWKNlvgQGNc3603qQy3Banz_GNeU2KVh-5Mm61P10bq8O3FFvVZwuvwjU9prJok2uce9NdSHZNJhyJe7Sx2Dy8k6v7I-tAhviBLSTFzg9iFaDtKa2O74-91qhawbqV80HvmZaP80Rb6m1IxxrnZGsvlx8tLJT5jpKMSWXI-gnu4uH78v5i0eOMHPJo9MVNoQfGtSXQqvfiWugQQzS_zBzJOg3F-CIKWcP5-TJMv-AQEII8LmucIVnSfXhgBTlgi1I2PWPuItfe-TsgCHs17qbUcsi1_wvRw_2BONYcF5cs_SU8DK1zgVnNa8J0zNuNexiob7Da-Wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصویری از خیل عظیم عاشقان رهبر شهید در کنار خودروی حامل شهدا
#بدرقه_یار
#اخبار_مشهد
در فضای مجازی
👇
@AkhbarMashhad</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/akhbarefori/669094" target="_blank">📅 16:44 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669093">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4fb44dcb20.mp4?token=kYUi00THqmATZLPKWjnVECqrPmDq_6-_5GBZd2byMqT9-sA24MBlpYq4kTo7XsuuLtXWP9oSiTI9yi9ftHXIkwwkSk3HToyofn02RcazwK4uWB-zGPaF6BuMlGCOXgUe24lQ6P5gc2Hajw2Dhnt9DW67O9-sG_u0L2Cs8Rgl3CdB3Es4RqhDYdTwI3n2mK8X-PV0ECXwM-upnB4f4hlWcvc2Khn4hreqlfk34mknD_zzN7JxgVmLsPHf2SjXsOyxRwt0dC4QqUfSeZFO11kqoH_i6JaDJTxs4S0k6YTNv0n2z3JyabmIWHzim77qINtFlKGX4iVzY1rAoaHyk7-B8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4fb44dcb20.mp4?token=kYUi00THqmATZLPKWjnVECqrPmDq_6-_5GBZd2byMqT9-sA24MBlpYq4kTo7XsuuLtXWP9oSiTI9yi9ftHXIkwwkSk3HToyofn02RcazwK4uWB-zGPaF6BuMlGCOXgUe24lQ6P5gc2Hajw2Dhnt9DW67O9-sG_u0L2Cs8Rgl3CdB3Es4RqhDYdTwI3n2mK8X-PV0ECXwM-upnB4f4hlWcvc2Khn4hreqlfk34mknD_zzN7JxgVmLsPHf2SjXsOyxRwt0dC4QqUfSeZFO11kqoH_i6JaDJTxs4S0k6YTNv0n2z3JyabmIWHzim77qINtFlKGX4iVzY1rAoaHyk7-B8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویر اختصاصی خبرگزاری ریانووستی روسیه از تشییع رهبر شهید در مشهد
#بدرقه_یار
#اخبار_مشهد
در فضای مجازی
👇
@AkhbarMashhad</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/akhbarefori/669093" target="_blank">📅 16:42 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669092">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f6mWqAYtETjZQ5Zk8YU839XAcmojWLUgg5-bwMWB7kdWDZbEBGYzthUtWfT_uxF0cMJVBiA0H-D675iL3Bkmp57kRprUCn5k6b5Hh4FyhPN8-O9dMYbQpLsmIoZLBszxw_vikG5Uf-DLeJmXhilQMAQbGt62kYGifl5WrQkAWI4pCRTQGK1I0Ckch51UYYu8_e_Rl3duRP6t1zL4qC1t_OkMY2FB2-xPzQKsuEUAmmQwFiAGQPRrFjc_r7Vj3orrvVXiRLe_u_7gyJwSMoh09qCaygrirrc9dl_iInbcn3cIXfIWxdA48qGRYZDIN4RZCfKh59iYNZD9iswkSSU0fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سفر آیت‌الله سید حسن خمینی به مشهد مقدس برای شرکت در مراسم تشییع و تدفین رهبر شهید
🔹
به گزارش خبرنگار جماران، یادگار امام آیت الله سید حسن خمینی برای شرکت در مراسم تشییع و تدفین رهبر شهید حضرت آیت‌الله العظمی خامنه‌ای، وارد مشهد مقدس شد. / جماران
#بدرقه_یار
#اخبار_مشهد
در فضای مجازی
👇
@AkhbarMashhad</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/akhbarefori/669092" target="_blank">📅 16:40 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669087">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WlQvzBGKWFi74XH0EpnUWljuRWR12fd99pMOZjaHC0wtpzQ3gXIiLQZdt7uks_040dVIqOXHCQk25l7DlAAJUGGmhxkvqQl-_JGWvLIZ7UZu8Gl8X-2q2FVIoy5wrtoXB7MLZDQjhK65iUpKwDCoQADbbdju-xoxKjbeToYVB0PlmGD-34clpohG5oZaRlW5aXVzDi_KAaGGxZnJxtSvg54G2QKyntK2UjY6GeTdL3u2H56Rf5IzRbQv7ZveCKPXCsA6AExSuEO7d-r4RO6bUpez3BeQ_2_FclcbzQB4F6OJOrcG8ccASekRJ5zwtklUW34JLYT34nG7L1FjizLWYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/J3u1BkpvYIWh3oXNwNmiuBNmaSTiWLoXRyVuj-nFpvlDaBUEEl9U2oHs8nNwGCB0hwSXKtZWs0aoVuDr1NEEK-LUGLi4Eo_l7powtnaGMsLJMGlcQl1XTruOiqGkaWMpsF8Dy1TDQCWhK3_YmAUoylpxIoWSXC_p6zle-Cy7Jg8Ris6MJLJWbr2EzH9o57vsunORs_qmtHcY3JNaGBePw7rcIkWxXr9k-TIFg1slF7kqXTNGM4C6-GbgZyVKFhOHza6nUn9SWunHFULiZupSb2uUR3Fg4NgPYEBT6Jnu5M-5eTrALW5Kpzp1mP--XmZcjy25GpOiBRyIKCHLQZvjaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PcuwBkrrBCtW--GhYFZQK7hGkU041oDUuufB-iASp9Irsg-s_JW8FH1GvWiF55ai6dySjORMMjSto1B_L80XzeQTCS5Dell6klEte39Sx-e8oQb6Ib5voHlEry8Zvxph52QCNhd-lZjnJ9z_e7SaWlwVwhWO3IJZCl_GEqv3WpFeac8WRSJs0bv9luSnTNifPTkC6DUaSoZMyLbSK7yigFw5zTYcRqqGSDycZAztYyY4WQpfZlhvPJ0PtNotqSOfI8OgFrRBSs0jUjzB7VQfe7W7eFOxzOogOYi-RDt-xz1oyHgcFSakcq6h6fuUdaWqIlw-G1mUdMQn3VJMUgiiTw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4806ae948e.mp4?token=Kfp6q3pekJQxNJq6BB4uTwVMyOk7bTUUMfEMjkQJgjA3tqvQUCfrCLckovY29NH-c_wegu8adBnPI1oGGQgG6lqqrPKn1kSd8EAs8DXdRpqRy9lZmbAiJBM-XkMEAoRd0H_hnsJUXADEar1ILDkdjb4tGIKIC1NkHFNl0aD_1HFrC1i7kZJB71dD1P4EskoJQSS9sCmTaOU4BFmcQhghhNx0No3FINWSQ5yeyY-FfFHGQt9iWC8Z6vv1xnLR2yi4D4IMA6EbuGCGhG1qMIxEcAvXNmJUuMNTNE97TBMVF8bo5ANLuR-alWYPBXGDlS4EPPgtZwEj2mXe94r3t5ZUa2HfOFDumUJWfoQ_WeA26MDU7DQzGxWiT_8vjBACmrGp-BWrQBSuxBB8WrFkB1gcRkbXed2YxRdx5EBF-v4vaL-TQRcwDVX94a-CI9jZnWi4nQBvINsjIElSeag0A0coHSh7dMecpYXwkBaYYL6sHdo3yNoaygktMcSdIqrSKsf2aVLFwmGzKb2hVFY8bVDYhU_QgfVX1kIJ5868DAQvWorRiidi4sUBlUKd-WbRi_qmoVY6VcXgaY0P5dknDbJOxKiXjA0Ux8i_5ZaHK-LhkVA7Ycwa0luqqPfOSgWa9E0i36CZ1mWJpO1atIKuvnUpJa1oFrNjT3-HF2UN9qgCe6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4806ae948e.mp4?token=Kfp6q3pekJQxNJq6BB4uTwVMyOk7bTUUMfEMjkQJgjA3tqvQUCfrCLckovY29NH-c_wegu8adBnPI1oGGQgG6lqqrPKn1kSd8EAs8DXdRpqRy9lZmbAiJBM-XkMEAoRd0H_hnsJUXADEar1ILDkdjb4tGIKIC1NkHFNl0aD_1HFrC1i7kZJB71dD1P4EskoJQSS9sCmTaOU4BFmcQhghhNx0No3FINWSQ5yeyY-FfFHGQt9iWC8Z6vv1xnLR2yi4D4IMA6EbuGCGhG1qMIxEcAvXNmJUuMNTNE97TBMVF8bo5ANLuR-alWYPBXGDlS4EPPgtZwEj2mXe94r3t5ZUa2HfOFDumUJWfoQ_WeA26MDU7DQzGxWiT_8vjBACmrGp-BWrQBSuxBB8WrFkB1gcRkbXed2YxRdx5EBF-v4vaL-TQRcwDVX94a-CI9jZnWi4nQBvINsjIElSeag0A0coHSh7dMecpYXwkBaYYL6sHdo3yNoaygktMcSdIqrSKsf2aVLFwmGzKb2hVFY8bVDYhU_QgfVX1kIJ5868DAQvWorRiidi4sUBlUKd-WbRi_qmoVY6VcXgaY0P5dknDbJOxKiXjA0Ux8i_5ZaHK-LhkVA7Ycwa0luqqPfOSgWa9E0i36CZ1mWJpO1atIKuvnUpJa1oFrNjT3-HF2UN9qgCe6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نماهای نزدیک خبرفوری از خودروی حامل پیکر مطهر رهبر شهید
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/akhbarefori/669087" target="_blank">📅 16:39 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669086">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">♦️
سپاه: مرکز فرماندهی کنترل دشمن در غرب آسیا و پایگاه هوایی الازرق اردن با ۱۰ فروند موشک بالستیک در هم کوبیده شد
🔹
سپاه پاسداران انقلاب اسلامی با صدور بیانیه ای ضمن اعلام در هم کوبیده شدن مرکز فرماندهی کنترل دشمن در غرب آسیا و پایگاه هوایی دشمن در الازرق اردن را با ۱۰ فروند موشک بالستیک هشدار داد: در صورت تکرار تجاوز ارتش تروریستی آمریکا سایر پایگاه‌های آمریکا در منطقه از آتش سنگین ما در امان نخواهد بود.
بسم الله قاصم الجبارین
فَمَنِ اعْتَدَىٰ عَلَيْكُمْ فَاعْتَدُوا عَلَيْهِ بِمِثْلِ مَا اعْتَدَىٰ عَلَيْكُمْ ۚ
🔹
در بیانیه قبل گفته بودیم تکرار تجاوز پاسخ ما را به سایر پایگاه‌های دشمن در منطقه توسعه خواهد داد و در مرحله دوم از پاسخ به تجاوزات ارتش کودک‌کش آمریکا این تهدید را عملی کردیم.
🔹
رزمندگان هوافضای سپاه ساعت ۱۴:۲۰ بعد از ظهر امروز مرکز فرماندهی کنترل دشمن در غرب آسیا و پایگاه هوایی دشمن در الازرق اردن را با ۱۰ فروند موشک بالستیک در هم کوبیدند.
🔹
در صورت تکرار تجاوز ارتش تروریستی آمریکا سایر پایگاه‌های آمریکا در منطقه از آتش سنگین ما در امان نخواهد بود.
وما النصر الا من عندالله العزیز الحکیم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/akhbarefori/669086" target="_blank">📅 16:39 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669085">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EpmgDxfvQyom8dbjgX8qW0URp4BGw4SKTuPx5BiTEcrc3RMNiqAjjCkod0xl7-hquz4IVOQfPcwzRYyFQlUg7tSP__8AQIoXoxcJ4nfECNSR0SAXyY7vr0ANgZAPsyOhaTahc1mq579Ru1pDZEgSGjKtcIavvcCMlqGtG3Mv9kKnZNomr82nLPX2XqmtMxzSwCooSfbSX3brbKS7VQlqcDMhJ49pmHD1a5RzxLAJGLzmempaUZXBX0QOP8ob9lgQa81qBBhcoRAKbYfS9LmY8GwHj5yceJlS35pSDfXd6MRbW3zJHRmXFQpFnLZW8snPlulSmrCnAoKhZNsRWqPTjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
لارنس نورمن خبرنگار وال استریت ژورنال: علیرغم صحبت‌های دونالد ترامپ مبنی بر پایان مذاکرات، این احتمال وجود دارد که به زودی به آن بازگردیم
🔹
بیش از هر چیز، تمایل به عدم تشدید تنش وجود دارد و من گمان می‌کنم که این موضوع در واشنگتن شدیدتر از تهران احساس می‌شود، هرچند که در هر دو خواهان آن هستند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/akhbarefori/669085" target="_blank">📅 16:33 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669084">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">♦️
خبرگزاری رسمی عراق: مراسم تشییع پیکر شهید آیت‌الله العظمی سید علی خامنه‌ای در کربلا پایان یافت
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/akhbarefori/669084" target="_blank">📅 16:31 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669075">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hujm9r-FyMvheuAoMQCOG9juINzSA6vNMSlnjAklvJ6iNL7Pj8CNYo66F7Z-ulYdMPOyk2nw4yIpNSqjWgq9uThZE2bLeK5SbltEYUM4GaY4jQ6iP8odS90rfZCQ3jDuKQFWWpXV0a5bvmifd-rtEOS9d_vE09-qjsvMdWeI47EURxid4G1_atgGYq1UH5I96-boFci0KDp3CmJQNycPzCEtTRg9G9xsojx0rd6qisPlOgOGIQri2nfnai-lqsiiEG9HdpupjHxIo1fC35Ecf2rSxSqiPAojafRSJKXFDVmNbMp1SlVANpkRW09y0TjAy_DPZG0RDW-sFkAEuxLUbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QDNBA4HayU-OskuB1NY8309V-SgXLeh--v2dP4jGZEP07I89FBW4XuXU4qAl1_5ov06LzywqzaL9EO4TI0FFAg0hfsA6YbGu42nNgUTICOCAcOJfB6qKpRaIFqsJYo1ZMEQlY4M5uHs7NZXdhaNNY9HHJ1JRVDXI5NZvIkUMJMtWzMNfrRgyVzRlHCj8ujYkqMY0HQD3fV5trCDABCqF8E0GR0I42KnU2r3mL-dI3-WfoZToT_bT0WFG_IbXaW00NXLnZbZ_xZBO5VoCIxiU7TI9EiyR3A0zYuxGGZ-l4ckSmKYL4RdPJv226umWj8HPxHoCV96XTqA1aMm_Qo9E_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/u4zhL1rypJMON7HJcDn2JtLTMqRZf8GMwwDqpOn7D7heb4uwkqVHvfbBE9Qc7c_iNS2jyfdeFzAGNrDnTt_0wPeaEeZundP6mZh0bkJTmVjfeoroTTV0HZljpWLRnsLyUpy3jO6fYLKv7BhDUkm4LmwEKs5y87-XRVvzbeihChqcilVWavP-DSBOwXlTV5y-oTT0tEclTIy77BIQZaGQGapKdshRUQU9eFSD_T_wfPMHE54SB-TEdhwC1X4pI2j1ZFu5jYsvsdpBkg1n-e4usF_o-6yfRWZmLeQTvvPvc3OEIf_PjFDNAQOrqs3oDyni8-Ve4a36toQOQ1kVC1aCIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Xyo4Q3ZECY1MG9nVNV4X3DJziRo83xFc3cARbyLaZoFzvkL7wmtUwYGP7QYgeGuYbmKqM-dY69jNM1NQtfUDyH8SRDiO4aaZoPQV13mKBpPro-ISRSPYjWKWLy6d7H4EIxXs6VQlIWIXD1pSjyrwckmkss7L_IWLct68SkwvTYvy67EyYJ-eM7NITsLRoPEQFj7esX3c5B-rVHqjpopxQOvGTduFcdFqRtDg8uS6CJBwZg5DueAYeBbjx72U2z355-jiJ9msSMGWuCrrBHZw7GZzTO6lghm_-BvEMOdgiUQG_FltcQeLTmOTQWFWiDyZzWugiymFbUe0P24OUGV-2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EyAWkbh2fp2OJIKYcBTtKs_Ny4OJf3nzwsWrfHRCodFYdH29YfZfqz-nYmpLEDChn_L1NL7gO2y3n1RphQZt-0Y6pmrNtMu_auEYiAHoBP-71BG0fCFlFFKroVLLcCVABfXuc59CuDbSK1gxWbqQ1a6K2LR6dre8sJlP93ldsZAD4hANT-2aD-051E7RdgUWXSgwY0WLG-2mH-DtT-w3RCjHgItIGpePKVT7eQs_S9PJcySML2hGOm8Qt6-aRIs0Abd8n9-XxB6PxBOujNiQZUFUg5l6D7lCAgXfDPnwij68Nk0D9xQZnFoRG2UI4mYP69juayz6W4L5ES_kvJcuaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RAImy4UrTk3Ain4hj0tnU1qHiqelG7O_roZ_Qge506fBqU6E1P8bnjaGe9SRMNMZbLGvoPqjkafudmYhI1kQer83UHwb7_5ZimwtOy_kj00MIO0x4S-qRr4XqiRZGI4mDKwK1HpQDOR844gYTVH4OtJ5zeoKUNsnq2MozNc9uOlm6fGUEfGoTDUKq5VfwSQqcNubAbT0aT_dwaCmcWWgreLCKB8wcIa2RzVVACCFyKvTzGlhTUux0LT8434YOpZToEd52jKl5080EkSlCTq8oIAzn8YERTnTgbyI1444ozuDDulGMjTSACkA9XTKhJaxgzxLfXIbm6os6zPXO7UVVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Q5Yvaoshe_-Ow8b8Hst1cVcV6iQH1d9jcjq64OQpzpLj8iFciu556iu4myLYiRUB97KQ2rq71Tv5qUmJfLCuFY2XXuLzfxT7QBx7Tem44wXTfuUOW2myufkhtdxsPedHIYW1CSUZYu6RY_ycnpKQ3UAc7Hlo_KdT_0LQhMYkhs07hzI5080i4FL2r5anzluRyOm65JF3IAlspirdXwJWDffBRUjUc9MFHJRgHt8uYrNIH1tZ4aEdHS9HgKq-e5-VwbUA2VcNXYliHnstBrtW7_N5qlR6w7k3Jhq-1yVlJrO3GSPOon5tovoCxoVdcOWcJBXvdI-e9Zfw_g4mtpWt2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OIg4K72XR_T91YVAgFvFFhAws6fxIhD9x86T2Q1aYr7e1fiG85xWJ4kWxBr0eL9Y7XC_-BiTkVxewZx33uoRr6Q3-QsM0fiPAlQ2Cdkfck4H6hPZkiKbtQvWNo2Px-bd_fi-poFo9GSWzJbbClSZxeXfWyZBaWOApOiySXhtUB1tBiWDMx31lX4qN3O8TrTjsr7B8ao6fXH42gh30aezPj1AHmIb8rQ2kUNwbxVe8VS2UGoHxAnaKWonmUkzSmwLOwBbnIcVIrvjPjTVVHNiKAXh_9YTm-gbr_HZ_0zggm50C6OQ7CkWnMkyIm-R7ABPkm4fspp_HYskrTnJ-Rnu3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/i-fCDUwreWgjrAZuYVSuxi6VoKGRdD8BZ-B6GRnZbG7eR0E58akR_lKRmTbD-X07c72hvV4Ba02JsG2LuNJJhnga38xe_A_6hYuKbxNQdtL75C_r17JFgQxc-3TPblvkp6ZVd7VDB6_2lRJ4DDfeT2REP2iRjeyiIeun84Lz3EC_01wN2hdtwd5dlQuh0yTwdu3AjyKB5t3HlmzmOr607NpSoUg7kgbefYKJ0VgpLstCRXcj5ayOY0lBcBLyMCc_z1-Le08kCtCpzfwN0CSbeu44dtw630BgJj9WSbzbU-lyl0Tsmf0NDf78882zw9TIyqOrF2AW_uB6wjcD7N9Vdw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
پویش مچ‌بند سرخ
🔹
حضور مردم با مچ‌بندهای سرخ در مراسم تشییع رهبر شهید؛ تصویری از پاسداشت راه شهیدان، ایستادگی و خونخواهی رهبر شهید است.
🔹
شما هم بخشی از این روایت باشید...
🔸
تصاویر خود از حضور با مچ‌بند سرخ را برای ما ارسال کنید
👇
@Ertebat_baforii
@Alo_fori</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/akhbarefori/669075" target="_blank">📅 16:27 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669074">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/abb4108a03.mp4?token=IB0FTjkVRJ5Bp3rzgLz4mxj4h-U0LTDuhWocVa8VKAzAebbhsUINkK8HaZ1zkZgKhgpXD9bttfWNHEqJvQfQeVUReeGl-zLwIpHhB1Cn_dFwqk548epnXns8iAseWvDQGjp1XG3Od-P14dPu0__wlBM6N4dq4rLsX31ZPVVnnMQz61ZB6EDM0Ubk_sotfJzwtQaH1AdM6zQMkpRKcIl1vNKqgO7_gIYOvhX3g5i5MpwORJe4Wu10S17ajNnhvE3cUUL1Ed86lDE_CPi315frLWZlR5UoGPYWdjV2OT0wJZD5t5v9Qu58uuDsC290fc0_ZARr5KMwurXnbm7QhbIHmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/abb4108a03.mp4?token=IB0FTjkVRJ5Bp3rzgLz4mxj4h-U0LTDuhWocVa8VKAzAebbhsUINkK8HaZ1zkZgKhgpXD9bttfWNHEqJvQfQeVUReeGl-zLwIpHhB1Cn_dFwqk548epnXns8iAseWvDQGjp1XG3Od-P14dPu0__wlBM6N4dq4rLsX31ZPVVnnMQz61ZB6EDM0Ubk_sotfJzwtQaH1AdM6zQMkpRKcIl1vNKqgO7_gIYOvhX3g5i5MpwORJe4Wu10S17ajNnhvE3cUUL1Ed86lDE_CPi315frLWZlR5UoGPYWdjV2OT0wJZD5t5v9Qu58uuDsC290fc0_ZARr5KMwurXnbm7QhbIHmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خروش جمعیت در مشهد برای وداع با رهبر شهید
#بدرقه_یار
#اخبار_مشهد
در فضای مجازی
👇
@AkhbarMashhad</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/akhbarefori/669074" target="_blank">📅 16:27 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669073">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">♦️
در پی حمله اخیر به نفتکش‌ها در تنگه هرمز و افزایش تنش‌های منطقه‌ای، دولت قطر اعلام کرد که برنامه‌های خود برای افزایش ظرفیت تولید گاز طبیعی مایع (LNG) را تا اطلاع ثانوی به حالت تعلیق درآورده است
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/akhbarefori/669073" target="_blank">📅 16:25 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669072">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">♦️
تصاویر ماندگار از تشییع پیکر مطهر رهبر آزادگان جهان در مشهد
#بدرقه_یار
#اخبار_مشهد
در فضای مجازی
👇
@AkhbarMashhad</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/akhbarefori/669072" target="_blank">📅 16:24 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669071">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/02c3bb1ce8.mp4?token=MR3EcmBvLWbs3x0-TIx_qkt9-ckN182OF_iPaz13r8Izkqi7L4wWFPPYbevWoBEOeH0rCIZ58bjEchd2nVavajnVew00Yk45poMd9C8z26SoKDKSTvKDZZsId4XP7rQWeP2yQ_XhLieyUz0qj_CjQUsSLo88zTyYieq3ZS8PkvvTW3GfktjNEJCvEVJNyeZO_Y-zTiDH14cVjXhnDuhXSoQ4E7FZtNrlDMm_VDM__2hFT-ppva9Jb5E695ZiUOJk0rg92wl2ITUbTayPPnaFQ_c5RJTShhFHm2G2S22AX0b033LEzeIEabcizDjG8ezCq55cjRwOaMZqhwd5gDmWUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/02c3bb1ce8.mp4?token=MR3EcmBvLWbs3x0-TIx_qkt9-ckN182OF_iPaz13r8Izkqi7L4wWFPPYbevWoBEOeH0rCIZ58bjEchd2nVavajnVew00Yk45poMd9C8z26SoKDKSTvKDZZsId4XP7rQWeP2yQ_XhLieyUz0qj_CjQUsSLo88zTyYieq3ZS8PkvvTW3GfktjNEJCvEVJNyeZO_Y-zTiDH14cVjXhnDuhXSoQ4E7FZtNrlDMm_VDM__2hFT-ppva9Jb5E695ZiUOJk0rg92wl2ITUbTayPPnaFQ_c5RJTShhFHm2G2S22AX0b033LEzeIEabcizDjG8ezCq55cjRwOaMZqhwd5gDmWUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویر حملات موشکی بامداد امروز سپاه به زیرساخت‌ها و تأسیسات مهم پایگاه‌های آمریکایی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/akhbarefori/669071" target="_blank">📅 16:21 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669070">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e0b685053.mp4?token=g4lnz8Odc7mGZLfJwRamsOMkiy57yX2YgMCN__jBIowcRCfZHxqN4xDArDcsMSrWB115mUqDAfy2TiLzJxZh7tqKvjK1pyNS7Ds1P44Ae8aJmc_MlzdvNRzlZ9XeLUTCv8Ct9bqsfuWiNBJzWKp4O4BEXkmQVe8K3PN04YtNTi9H_h_QFq9GLZ5QWwLOzsIxcTFO5XGDFdh086nLSABkD7kmhurq29vZ1xxdwbjr0uLT8tqoyASY02Jsn9Qlw10BL2U26HRrdRKRnSeaSKqzWuJNHpU4GYWOSR3TyDEDmXlCMy2lJv9-DFdXCuGGFBs47RovTgLYjKgOSGTKvYGpUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e0b685053.mp4?token=g4lnz8Odc7mGZLfJwRamsOMkiy57yX2YgMCN__jBIowcRCfZHxqN4xDArDcsMSrWB115mUqDAfy2TiLzJxZh7tqKvjK1pyNS7Ds1P44Ae8aJmc_MlzdvNRzlZ9XeLUTCv8Ct9bqsfuWiNBJzWKp4O4BEXkmQVe8K3PN04YtNTi9H_h_QFq9GLZ5QWwLOzsIxcTFO5XGDFdh086nLSABkD7kmhurq29vZ1xxdwbjr0uLT8tqoyASY02Jsn9Qlw10BL2U26HRrdRKRnSeaSKqzWuJNHpU4GYWOSR3TyDEDmXlCMy2lJv9-DFdXCuGGFBs47RovTgLYjKgOSGTKvYGpUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پرواز جنگنده‌های خودی بر فراز آسمان مشهد
🔹
صدای پرواز هواپیماهای نظامی در شهر مشهد شنیده می‌شود؛ این پروازها جهت تأمین امنیت مراسم تشییع پیکر رهبر شهید و پوشش هوایی محدوده حرم رضوی انجام شده و جزئیات رسمی آن هنوز اعلام نشده است./ مهر #بدرقه_یار  #اخبار_مشهد…</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/akhbarefori/669070" target="_blank">📅 16:20 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669069">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">♦️
منابع پاکستانی: میانجیگران روز پنجشنبه، برای جلوگیری از حملات بیشتر، تماس‌های جدیدی با آمریکا و ایران برقرار کردند
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/akhbarefori/669069" target="_blank">📅 16:18 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669068">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Aza_7XMkeG4mIRUwpDnljEObygINI7S__T6T7EFl33Axe4XQTPUJIhHgb_PcnjtQ_PhiCb-uXvY6rkGXXTTGituCAXxiagBxOe7O3WYr2gW0n-cDITFDQa2zz_Ccdhfdfb2hYRWo1GqYiTa463rndW_CmYimE_71uqIyt5BYXPsD6BusYsixHNNujoGNDwG3prmWreNBMLJ8qfW9bU9rmtcUHSeLTRBf8Ekjzmp-3m_b1LVycuBQd8a4IfQJ8rgR16LbW7waX6d5elbkba2GbsddhdTIgZ4Vh0sRYBYY8EvjxJu9aU8PU6ZB9_2zOpzL5l15C3xvQgdmTBiIH2bxLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📉
📈
بازار می‌ریزد؛ اما
آربیتراژ
متوقف نمی‌شود
وقتی معامله‌گران از ریزش بازار ضرر می‌کنند، ربات هوشمند اطلس اختلاف قیمت بین صرافی‌ها را به فرصت سود تبدیل می‌کند.
✅
برداشت سود روزانه
✅
گزارش لحظه ای معاملات آربیتراژ
✅
شروع سرمایه‌گذاری از ۵ دلار
✅
بدون نیاز به دانش ترید
🚀
مشاهده عملکرد اطلس:
@AtlasSmartBot
اطلاعات بیشتر در کانال تلگرام</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/akhbarefori/669068" target="_blank">📅 16:17 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669067">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">♦️
تکذیب شایعه حمله هوایی به کرمانشاه
🔹
منابع آگاه با رد شایعات منتشرشده در فضای مجازی، اعلام کردند هیچ‌گونه حمله هوایی، انفجار یا حادثه امنیتی در استان کرمانشاه رخ نداده و امنیت در سراسر استان برقرار است./ مهر
#اخبار_کرمانشاه
در فضای مجازی
👇
@akhbare_kermanshah</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/akhbarefori/669067" target="_blank">📅 16:17 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669066">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">♦️
منابع پاکستانی: میانجیگران روز پنجشنبه، برای جلوگیری از حملات بیشتر، تماس‌های جدیدی با آمریکا و ایران برقرار کردند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/akhbarefori/669066" target="_blank">📅 16:12 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669065">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">♦️
سرلشکر عبداللهی: قاتلان قائد شهید را دیر یا زود قصاص خواهیم کرد
🔹
فرمانده قرارگاه مرکزی خاتم‌الانبیا با قدردانی از حضور گسترده مردم ایران، عراق و مسلمانان جهان در مراسم تشییع، این حضور را نماد وحدت و شکست نقشه‌های دشمنان دانست و تأکید کرد نیروهای مسلح با پشتیبانی ملت، عاملان این جنایت تروریستی را دیر یا زود به سزای اعمالشان خواهند رساند.
#خونخواهی
#تقاص_خواهید_داد
#WillPayThePrice
⁩
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/akhbarefori/669065" target="_blank">📅 16:11 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669064">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/09c41fdc23.mp4?token=pGV3t1GrRG33n8M8FfnoKH0f7ijCf1y0KU63yZRkO8oC7ZDOboBATfz8Oz5FGg8x_v-8YjWfTwWYt2UyVADLLn-kFLpbMxcc-Jp7rQpGWLTKvOjLwPEJ7qNxRUB7dWGnNFZZ1hWGb2-U0Y-HfP64KKsabS5Ic-DKWjK7w0wz4qnwPavCykMJV1H5N3Me7pnuzocmj3_EKhswL6W9d9E8eLSpCL-TekXt4AYsaGzxj_9OXjpyZvRHOzW6UjUojWZlgoEfn7SqNFBD1JPOG5bh8zwGsIMmY-9x_kYyBrQSM-Z6WU3P3eYLaHlGQgFPi7NZEPd6QHEGy-_SbolbB_ip7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/09c41fdc23.mp4?token=pGV3t1GrRG33n8M8FfnoKH0f7ijCf1y0KU63yZRkO8oC7ZDOboBATfz8Oz5FGg8x_v-8YjWfTwWYt2UyVADLLn-kFLpbMxcc-Jp7rQpGWLTKvOjLwPEJ7qNxRUB7dWGnNFZZ1hWGb2-U0Y-HfP64KKsabS5Ic-DKWjK7w0wz4qnwPavCykMJV1H5N3Me7pnuzocmj3_EKhswL6W9d9E8eLSpCL-TekXt4AYsaGzxj_9OXjpyZvRHOzW6UjUojWZlgoEfn7SqNFBD1JPOG5bh8zwGsIMmY-9x_kYyBrQSM-Z6WU3P3eYLaHlGQgFPi7NZEPd6QHEGy-_SbolbB_ip7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویر هوایی از خودرو حامل پیکر رهبر شهید انقلاب در میان انبوه جمعیت عزاداران
#بدرقه_یار
#اخبار_مشهد
در فضای مجازی
👇
@AkhbarMashhad</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/akhbarefori/669064" target="_blank">📅 16:08 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669063">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B9Zl_2mEuAfU2uQCOGmdNCfJVMG_6Xra0_JQLXabzdmN-FUKnNWNORO0rQXMqZcP3iU1m5onyxCuFeHhQAayDypFf3jLJCpi8egmKSVOyvtNBEIH-t7U6a8dyk7OXKn4_xefMrLL1Xut88sfd5QkZ5Ss86dfLqan17XR-9ZqKowmZ0pvDdgpQpjMxtn0F9ukhQk6RWyODZyb_ZLYqkxYUQ1V8Yegay_KBFeWZqeKuEK3Ai7LN1v0y9QQmebuvns9RdHR4okYPpjrNJNNrMH2MU_3xIBMXiYnUFgMebC_eoC7Z9cVDL6Jxww2zn1vMeOlJkNfnWzkA5NtH2DmMTde9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
شاه پناهم بده...
#بدرقه_یار
#اخبار_مشهد
در فضای مجازی
👇
@AkhbarMashhad</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/akhbarefori/669063" target="_blank">📅 16:07 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669056">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Pf8HbyLMLnB3blXRhHMkydp4UKEdCxnPNEwAa9IIjKwZBOxwbrHvDQUMDHzE2VMapFI1tH8ICLa_03pV7rElJxcrRF1v9EIKfnX0U2C1bivRPR7wQHZVFwArens0F96i47FNjOUv7vAFsUZ6aJsl4WY-TN0GHcGoiliv4caIy5pBpzSBq_0khkQW_8rZ4NVcf_1L9etzYHEojY5rbjrn1Qnho88O-5WmBn6uoXg23BgMvpz1owC1IY4sKRoPFLmqS2b6LOvh9EPfAw1GsNmwGAd93CVgEYrknLqmKp7LJPTanE3LR2XCuDXkyiXQXvuagwrDsgX1acJsRVZIVNrLUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/T4YL91jEuW1ZG7W-0-AazK6daef-ejkQn8HlJH51BBR4nw3DRFyaboETykievZ3Xx_A9IKk7dr2plc8Lio-N9tSV2TkbZBH--jWeDHS-ZR6Ey85H6Gg3EPCzInAbk2gz-9WyvX70GVWfw2zfFn_p9VnNeq_DnSZzGAAjwCytuIMs5G7FG4kUACHGuk401emqnqzHBU03prpO1xT4noaNynJ1bG01WJa9e5M5we4Gs11RqMzkWw7JAmgdnSQUgPlh9put6CE93mKJcxuKKaml8A14m86o4iKetw4M6fnfz3t84jKlww7a4QC8hvqbhR37EkOFXGwRirQuGWRhe0srmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/D-uNNwT0PRa4p97iufhLtHtDkyqw_O-UMwVPb7swfLuLDNFfBrhaRA5KRBDkvRUbB7uFXZVCo5dYabwl8c0RXv84uSF7bN3ofsDcJgj-Fbs8LqOQNNZfOpls47J7SLQG74bANtUmdCFITGI_Y4tTiHpYLNVWAtml1i-DsRJVHUoFUTINj3J4OJu8jbDtp_1xs7da3ut9hQwAq6SMm1thBV57OT-Xl_cY3-HsBSX_UfZIHKP_qYyGjgBwN-aDXGMSVFg_MJpdhSW7508Uqub2k1OkMJ0mYdodm8idnid0kYS8Rh0FEQXGyvevh-4w2qKuoB6WQ6Jq-u8jJs_bvgnQrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bf2CoP88dkGVpzg2ejbBOdZd775FcnU7Fo9DDJzC39_rHxtywCQ2Pt4ndK5y6uP-4V2fjrei0tR3Udy-NNZ4zcMOfQPujVRnuFpSZ6wy4mHmdYQrtGsX_rlkdNNRze2fuAWmRD77s4qa12lSFhcihakK532zU9O4isLxqRVlDmWoYPGFWHsXwc6aXRYjJw4X4qpb6BDwHxz2fiXxESTs5YW0fsf_-wR4dJtdIlDRlVaFqfIX1cmFVkAtgf8I_W4jQdD1Uv5x1DSBJ7NzRKdwaxbF51DwDEtWNnnFjD5Pq4REw_EVreBMLdr0aYYkfOSLw1so47IsMVNCpP4Ei5a1ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aAxWPY4dt6GNEFfCcZ3RkOqS5TO05EfkkKsFvZkpkSolT5fJ8R8hJQEbkrCJsn8hNdeTq5lF9JXrEJAr2g022xYSUouXyS6kPSzAj_h-F3CwL9ahqN6FQxw7QeG1zK3-Y9V3UR342mmjFVp1xDOAml5L_w2j6R-j6HkJOCsTGeFl6ToubifP2zQOLFHDdZjDB4f23geWF39C60x3m-QUeY3sy6j9jGtfZyrzkTflLLqITOH9j9qeNyNn1iV94ERA6dpSaB2A5lmtn31ijJuWsHjCdGAc_88q-vQMzBSk1pIswSp7q61ysafV0V5KITjebm6gQ0eNfWCLsvk-g8DmtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HMter8L_Wri4lS4Sol1NCcSgWwvNES8m1QzhlzamGFJf4murNwHT9JeWMgQpIUQXNia5PDCVHWYyYq0-0c0G6KmkwMfJMUp7gWHbpixV0Yrm7XvNh78gPq2z2JM0gNm9n2ykafAFdHDnbYCBSeapVkCjgWNhjH-h82YhI1IWp_IEOx-Cnkhu6A8IjtP5P9p56-cY636xBrGrKdqPZrSrr8BwD85Btmsvu6MiJwY0dEWqwRmJzxDQFQ7coTncn_jG9p9k3uxcmUJZvURKxpeRTOoo2JSWShS3X7UN1iTOSrUjeBY7hSbBzrtV7EIOtAiI6D8Zg4rgbjGy84pCqlRpcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ih3A_it-_dOF6JnFrkUVJI4VpQ04FLunb0-XUelUUVOn9rHZNqsQJJE24nY1NRcJ1LI9XraK5SBlxtNEzNH2DnE-9tWVlkljnCSNdqui18WTyEUGw91u1CjLh2PuIj04-Rym4Rk4X-4Y3U7hZ7Fztr1-q-o11IDJMTkVox7_r5fZLxzpgLNh8W16FRkFpF0aUq55tXJgLVGtvT_LBnp87-qAIvgywX9IsceXjRNINy4jzg6tTwJ8StegftPG4Tx2PAyQ3ghGPKlRw9Sab6WHsfSZF_H5NEn1nMzKZM5gYns5UUVx_HQM2HzLfZjHW3zoGCu_7dPW_uCjmqOImQVkxw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
اشک، دلتنگی و وداع؛ مشهد میزبان آخرین بدرقه رهبر آزادی‌خواهان جهان
🔹
تصاویر خبرفوری از بدرقه پیکر رهبر شهید و خانواده شهیدشان در مشهد
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/akhbarefori/669056" target="_blank">📅 16:04 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669052">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VjAgzC6mqySH1qnVL8AiQwrSwD1athUYKEC1Oq3IxoVQdWQmP0OWdC8EHUChamf0_NOFPfdcxLQKcFKPD2gwyCrqV0EQ3CE5WxXGZMdj7bnb_e_b2ml11XHbTeLy52iRONBXd2-4WGMcfQMSV5QJOBbOrEeVnjwcjryFcsi0xCQU-BP232GZa7k2CGAACs0sxvwnZNzuvRiudz7wrKxNg4iE0dTJmOvBf3mk9usosyH198L0V67PR2nzBNCs8VaPGdNlTB1EcveXMyM4FVXiAzU8Wj6NNaSDXevDzujcXibt8RhuIqNFwdBvnEASCYy4gSCa6j2NHbZ2gveYS4EPDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HFAVXHLscJJApxWT1vHZLP1GdOKtNfouQaPjH6yO_4wCpUQ-Aw7JIdtPZ2QdW3AISxuO-T5pLS9z9GpXpJUhUFpSUrg2QjGL1dpRvRQ5S7TVIjVxn6afHZYWspykDjkJcUbIokgOx6VpEWDr_q_lAz8IC0ykmKgWQ0NpJa2M14zxC4Pm9Nr3EecRAF-qUDPTc1VLFrgFkNziEfnF9wJFTJ_IOo9U4HybH5x40yyKxK1LjkXUzeDclXCtX3tJUANI7ju4TKIjQMeRNtVFUu2rxxTdP4B0fy4ZHYH_Bsqqg5kvHwWZ-kkusO4DcG1Dynbn5j1sLx_Kt-OIEKwIVReqGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vJ3Q1kD8TIjUe-tHxcc2xqCDNp7H1ZhKKOnkAaqclka917GMuR1rWsXQR9ItL_wFHSxiIK7o-3ZpQk9fUY_tRo7wM9cv2iiMAOCQUzw2pnSdx-XiR-o0gZYOk-vboPVIVvp72A95rTeZzWZcYBUD7zwufL10gyHKkX1dT_o6a-x1AUKtx2iaVIygtV0_RuWl9SCXFeImfXFkvIoxr90ENe_SSjgGs-8zW_5jfy5uhcQGO9gKkxCtpomlwWb2wlfI2tj78GE1-WKqyns9A0c-BAX2y-DQxcykxL9ufE6frF-B8NcS2qMNlAL7jGRdKQNqhPBVzOfcdxON47mFZBuTrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OExFdVOTx9KRjnv26kYLGEQWPEh79K_WDP90BkYaFioGRYsMKbqRHA3H1MdHisxCVGcz2R3s1HG2YBwFEdhfo52fVySgILyJc5yAFaR0gtOLn1YC6t3sN9bjeOF7c3N17dACXql_Y9hnOsTyjzDIrOJSaJEM1cX7SzKgtQpkFzXsQm7tOGdhU2M8GUOjRtDq_D2C5k0E4NVE-TSpLzPNvnzbIZfUQddnYEw5c0dZMBAtdNszPQurkipN8Ce3w63z356y9aQSU2G6kSBMq24FdQsmPkNGgLCAd61BpaVE1PyeANS1g0yPDG5FnmprVXTG24rPsquAwGhCPpZnLxW9Lg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">#باید_برخاست
ارائه خدمات مطلوب در گرمای هوا با استقرار مه‌پاش در مسیر خیابان امام رضا(ع)
مهدی یعقوبی، معاون محیط زیست و خدمات شهری شهرداری مشهد:
🔹
با توجه به افزایش دمای هوا و به‌منظور حفظ سلامت و رفاه زائران و عزاداران،  دستگاه مه‌پاش متعدد در مسیر خیابان امام رضا(ع) و محورهای اصلی برگزاری مراسم به کار گرفته شده است.
🔹
علاوه بر نصب مه پاش های ثابت با سیستم لوله کشی در ارتفاع مسیر تشییع در خیابان امام رضا (ع) حدفاصل میدان بسیج تا میدان بیت المقدس، بالغ بر ۵۴ دستگاه خودروهای مه‌پاش هم به‌صورت مستمر در طول مسیر فعال بوده و با ایجاد فضایی خنک‌تر، شرایط مناسبی را برای حضور عزاداران فراهم می‌کنند.
🔹
تمامی ظرفیت‌های معاونت محیط زیست و خدمات شهری شهرداری مشهد برای خدمت‌رسانی هرچه بهتر در این مراسم بزرگ به کار گرفته شده تا زائران و مجاوران بتوانند در فضایی ایمن، آرام و با آسایش بیشتر در آیین تشییع پیکر مطهر قائد شهید امت حضور یابند.
🔹
عملیات خنک‌سازی تا پایان مراسم به‌صورت مستمر ادامه خواهد داشت و نیروهای خدمات شهری در کنار سایر دستگاه‌های اجرایی، با تمام توان در خدمت عزاداران خواهند بود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/akhbarefori/669052" target="_blank">📅 16:02 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669051">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JDPOSax3o3bdfEt0a6IHIeuC7q8oDpNeJsn-YZ18V8XycAkKPdEe57tvJoBb-2DnMRbj2_AzNWKfjgPwKF8lz2knRjFcWcEJYwucHSxRk76ILZ_46QxzKKpFZfJmiXqjPHiovCcf9MOJdQ4jaWiwWsESCzm6Aw0ldZ4JIpt94cQ1-yxQ9CKrY6M7osfQDhoWSgoK2HUyerQT0-xBTeybbnMv3hrPcIBl5g3l_yBoN-X0cPJ9UcC_B914HQSfm-0a1tpj3qzH8neTTHAbAnaqr72J9urGPCNsHEzX10t5V_tqJd2cgQn-L-FLU66_jXnrwdrDPyTTg-Nx1kTW8oSaAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پیام مهمی که امروز از مشهد مخابره شد
#خونخواهی
#تقاص_خواهید_داد
#WillPayThePrice
⁩
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/akhbarefori/669051" target="_blank">📅 15:56 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669050">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/djhX2EtG9W0fGNqbGWIGr-_Zg92HsV0a9TW3pmNwGYkoTA8KjuNKgc26zTUyonjlPY9ggFpiCySMSxeW2z_C0-hvVsxt7ZXPwRDtce4JoprOBqWjvMAc_ZtnIKrXgYLKUiLytaRFDxlPW6UCIJNpivWPYPGYxz-LI1v8eWGatYOAjEZFyKvdfYku2X_7skP_ru--K5EKKn-H_4agRD_OM_h6g-sXXwcUQA0YbxIf3UFmFpzsSth92ytsCCYERxefPpApKitY-Kms7-2VMIgRSfj-jYzY54gwTa53LjzsCBKtuND9kIaI-P21H2lOv1k70MymrJ2x0HHXh7nFjcqpCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
تیم ‌منتخب جام جهانی ۲۰۲۶ تا پایان مرحله ۱/۸ نهایی از نگاه هواسکورد
🔹
علیرضا بیرانوند با نمره ۷.۶۶ در سایت هواسکورد، تا این مرحله بهترین دروازه‌بان جام جهانی ۲۰۲۶ بوده است.
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/akhbarefori/669050" target="_blank">📅 15:55 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669049">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2fa16352e1.mp4?token=KF_UniFXzJJ9R8SCIydrZLMQp3lgjtO_87CdW7Xk9b0IqSzdNvt3HCWq9UHePzmpGiaXITkYYkD-oGBZ_LeI_Q985_xhPTE737zlSXurK1DXZ73ibW4Zgd3lxnmOktKoRlNhnsMrHHBERR240qafkrez4Uf_cqDLh_UABHZwazQ9L5803GJSLi7q8K6zg2VBzNO5rc15CKo15hxdH01S91mNtDFEV956s1J7tc4mHoFKU0KvPrRWvFTyu_d3G-yv2j3cOMPbe0gE6F7gxzeqCyAyrtqZdCvxcOPNUr1E6zSI_U7-EJhPTpMeKmchX70EK8wWhV0v7r0CDavkMuzUJ4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2fa16352e1.mp4?token=KF_UniFXzJJ9R8SCIydrZLMQp3lgjtO_87CdW7Xk9b0IqSzdNvt3HCWq9UHePzmpGiaXITkYYkD-oGBZ_LeI_Q985_xhPTE737zlSXurK1DXZ73ibW4Zgd3lxnmOktKoRlNhnsMrHHBERR240qafkrez4Uf_cqDLh_UABHZwazQ9L5803GJSLi7q8K6zg2VBzNO5rc15CKo15hxdH01S91mNtDFEV956s1J7tc4mHoFKU0KvPrRWvFTyu_d3G-yv2j3cOMPbe0gE6F7gxzeqCyAyrtqZdCvxcOPNUr1E6zSI_U7-EJhPTpMeKmchX70EK8wWhV0v7r0CDavkMuzUJ4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جمعیت خیره‌کننده مردم در تشییع آقای شهید ایران در مشهد
#بدرقه_یار
#اخبار_مشهد
در فضای مجازی
👇
@AkhbarMashhad</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/akhbarefori/669049" target="_blank">📅 15:54 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669048">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b933c66a8b.mp4?token=MOnkTRULNJ7YbBbXPg8I_vvH31wGC3ePxF9dq2KBcsTHgFuH_MneyCa98wPgPCHaM5VAKnKICFBzHENt9fM27bNAOo4cSZMs_wSeOnbjYH0PA0-LBurmoCiF1nbHpiyg3NSCUwgeKCpRYxwnCJCDahvfOBqVS3DrZYrcusWltLcFqXropEX31LNUUS0nuQHcmP5xaCSLhRZrH9xnZWpS38jUTESFfDzKv3f9q_RZiTXE9AYxvsmCJQCSdD0Td_rWcJ-iFutNQTnTuor1UeuhgLrShoRFcHwQRcL9QDQmkjwgbDNHjhRgK14m0bI3SbtxlNQ5XWQILLqvv5Cq-JRdSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b933c66a8b.mp4?token=MOnkTRULNJ7YbBbXPg8I_vvH31wGC3ePxF9dq2KBcsTHgFuH_MneyCa98wPgPCHaM5VAKnKICFBzHENt9fM27bNAOo4cSZMs_wSeOnbjYH0PA0-LBurmoCiF1nbHpiyg3NSCUwgeKCpRYxwnCJCDahvfOBqVS3DrZYrcusWltLcFqXropEX31LNUUS0nuQHcmP5xaCSLhRZrH9xnZWpS38jUTESFfDzKv3f9q_RZiTXE9AYxvsmCJQCSdD0Td_rWcJ-iFutNQTnTuor1UeuhgLrShoRFcHwQRcL9QDQmkjwgbDNHjhRgK14m0bI3SbtxlNQ5XWQILLqvv5Cq-JRdSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویر هوایی از حضور جمعیت عزادار در صحن‌های حرم امام رضا (ع)
#بدرقه_یار
#اخبار_مشهد
در فضای مجازی
👇
@AkhbarMashhad</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/akhbarefori/669048" target="_blank">📅 15:53 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669047">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">♦️
بیانیه سازمان تروریستی سنتکام درباره تجاوزات اخیر به ایران
🔹
سازمان تروریستی سنتکام گزارش داد که در جریان تجاوزات دو روز گذشته، بیش از ۱۷۰ هدف در خاک ایران را مورد حملات وحشیانه هوایی خود  قرار داده است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/akhbarefori/669047" target="_blank">📅 15:48 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669046">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eaabcb679d.mp4?token=uxkyyXtChhFbPBrFrBRqCS_S8pmj5rwv5qtsMqs3awrcxHNmjmjqVCaOLCZB5fk8dslFhaCIGd6Zfw7c4M0npAKeOvdqik5RnrTU40GY-df-WgmKIhyJj2E__akOvxdo7c7lOc5euTdFD-AVvhuw-ses-QijYUTscL806EFFE1WjpT7MyndW-mIkp9mztQsZUPxCKBAJ6qraFnlP1mVrkTKSRNnMZe-S7BfXevt0L9llsCnk0RuESJ8q6F536ODGCvk0pvLaKlEsqm49WdTuDj7VwnymQIULwcZ6P5JAxk6irXp9ANg2ESj1PmIPuyI9Z9asFgymt6idY-UmE4ytKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eaabcb679d.mp4?token=uxkyyXtChhFbPBrFrBRqCS_S8pmj5rwv5qtsMqs3awrcxHNmjmjqVCaOLCZB5fk8dslFhaCIGd6Zfw7c4M0npAKeOvdqik5RnrTU40GY-df-WgmKIhyJj2E__akOvxdo7c7lOc5euTdFD-AVvhuw-ses-QijYUTscL806EFFE1WjpT7MyndW-mIkp9mztQsZUPxCKBAJ6qraFnlP1mVrkTKSRNnMZe-S7BfXevt0L9llsCnk0RuESJ8q6F536ODGCvk0pvLaKlEsqm49WdTuDj7VwnymQIULwcZ6P5JAxk6irXp9ANg2ESj1PmIPuyI9Z9asFgymt6idY-UmE4ytKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پاسخ قاطع دکتر مرندی به ادعاهای پیرس مورگان درباره جمعیت تشییع رهبر شهید ایران
دکتر سید محمد مرندی، استاد دانشگاه و تحلیلگر سیاسی: صدها هزار نفر نبودند. جمعیت چندین میلیون نفر بود و مسیر بسیار طولانی‌تر از ده کیلومتر بود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/akhbarefori/669046" target="_blank">📅 15:46 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669045">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
انفجارها بار دیگر پایگاه هوایی «موفق سلطی» در شهر زرقا اردن را به لرزه درآوردند
.
🔹
واشنگتن: چین در حال خرید دانه‌های سویا از آمریکا است
🔹
در پی شلیک موشک و پهپاد، همه فرودگاه‌های رژیم صهیونیستی تعطیل شد.
🔹
پوتین، مذاکرات صلح را رد کرد و برای تشدید جنگ در اوکراین در ماه های آینده آماده می شود.
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/akhbarefori/669045" target="_blank">📅 15:44 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669044">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromسازمان راهداری و حمل و نقل جاده ای</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a4b393ea9f.mp4?token=TgshpG1TjybX5W6U4mI-KeYQLTE6NE4RvBXT8X5xeWM9UbhRbSIt3hqnhGFAatN9cBAykMhFgyrdOsWbPsJaVaWK71ChItnV7MSOXyXhmJc1BBleVNy8TJFfqJdWLa0df3vkOWreZxrLfOhHqUdqB8BlBncx25ycHHTl9j2ISal6BMAgMb71x7eZmNeXfX_k7QpGOrI5UiEuKnfQVVQjmxmn53j5Hwb2dM1sYLSkgtkBTh_weyfLmgNFHKO2XBPij2SOvzCi2GOUWiR_CHI5r-PXIpim4Va7WwWnrFMAKAQeyoM0Jk0kDesEFBU5wvtM-yq0OpleP8rIJE7X2aNTYz0SG-_a2V96eNRyohtTjHcxufcKswPnFEjckxpUZu3LZNpBh6vSPL1GcBJef7VD2gWCcHjwWdiQI2-JTG3O-yXdF0ntvjzEW5g28CMQmH2jtc2dJBgbR_ld7kBaX6NLE0MoWuNqxlDIYzODnIulv6M6Omo6Nx110Zg2rlwO98Vad7dUYiE_A2268-xPGmOC70ylerBhQlYdt7cPM6c0Ba0jdLqkV-bqDRhYIPFPz-C9qVU49Qi96nExgh8DRZllNSoJpGAgdrSrzFhlQ1QDTKeTsf_PaIpqiCNL1UY9CE8tNUR2FomUyeOCngerO5jSESa6Zw8MhUzyMDZBrIEG_VU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a4b393ea9f.mp4?token=TgshpG1TjybX5W6U4mI-KeYQLTE6NE4RvBXT8X5xeWM9UbhRbSIt3hqnhGFAatN9cBAykMhFgyrdOsWbPsJaVaWK71ChItnV7MSOXyXhmJc1BBleVNy8TJFfqJdWLa0df3vkOWreZxrLfOhHqUdqB8BlBncx25ycHHTl9j2ISal6BMAgMb71x7eZmNeXfX_k7QpGOrI5UiEuKnfQVVQjmxmn53j5Hwb2dM1sYLSkgtkBTh_weyfLmgNFHKO2XBPij2SOvzCi2GOUWiR_CHI5r-PXIpim4Va7WwWnrFMAKAQeyoM0Jk0kDesEFBU5wvtM-yq0OpleP8rIJE7X2aNTYz0SG-_a2V96eNRyohtTjHcxufcKswPnFEjckxpUZu3LZNpBh6vSPL1GcBJef7VD2gWCcHjwWdiQI2-JTG3O-yXdF0ntvjzEW5g28CMQmH2jtc2dJBgbR_ld7kBaX6NLE0MoWuNqxlDIYzODnIulv6M6Omo6Nx110Zg2rlwO98Vad7dUYiE_A2268-xPGmOC70ylerBhQlYdt7cPM6c0Ba0jdLqkV-bqDRhYIPFPz-C9qVU49Qi96nExgh8DRZllNSoJpGAgdrSrzFhlQ1QDTKeTsf_PaIpqiCNL1UY9CE8tNUR2FomUyeOCngerO5jSESa6Zw8MhUzyMDZBrIEG_VU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
هر سفر جاده‌ای سه ضلع دارد: راننده، ماشین و جاده
‌
🔹
قبل از سفر این نکات رو بدانید و رعایت کنید
‌
#باید_برخاست
#بدرقه_آقای_شهید_ایران
#چشم_به_راهیم
#سازمان_راهداری_و_حمل_و_نقل_جاده_ای
‌
🌐
@cheshm_be_rahim
🌐
rmto.ir
🌐
141.ir
🌐
https://ble.ir/141_bot</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/akhbarefori/669044" target="_blank">📅 15:42 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669043">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/473d44b5db.mp4?token=DHfGNGmRtwI2fqmZfu4C77WYuqMema8-dt6wy4wQjB4a-UnoWFm_7rhKGbEl57dEUd6nUIrc4KMFRY7pZUy6K4M_TzUob4hSpiWrMPD7yb70Fk4gpBWvWMYKu72cd8xmt94bAhSjA1kgWgzz0RzCUCRBfjndtT74cJeN0uqBbv-2BABKVNQZ3E2sKTn1t2DX_VbhQCSJxE5HtEVfhAhbWpaWbOjwfoBPBnH91C10_EW1CteUnKGSXp_mkFdb-Wav2EzVQzSmyQVi-RCOPivm6TRgPv-03zEdgKbIUcEWhUypJ9hWttqmTbikKi2nI8LNNA7Y6ODQk6XHCFbg4dsNnrHMXySylc5xlYkwKIXpfiBbfYIVDVUq_EcbbxaXbLB44IkNnJYjv2PynwklEVc1N6SIdVZ9cpLcxEFFHdlyThNn0FWe6w6NDb_g4PQbBim0Yf6t6-pikq2nARaMLg3VT0AQWMC9sn1gkcuOViSfUf1K5lqRueeI3Bl4aaCYM6ca7rcoe91oInJh8H4HCcbYfUTXGrQrtb9CXcPK4yDP99MewfIBprGcFylZqQe5uTXbXaNabqKZVEWGAopzyz09fJbJqVBxVNeIHCtyPXyR-o_Ri_RAlfeSz4d8-Nx4WmgIwPiGctPeXECbDNLe8uTWfWx_FOhOxa8VPLg3AHk1gFE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/473d44b5db.mp4?token=DHfGNGmRtwI2fqmZfu4C77WYuqMema8-dt6wy4wQjB4a-UnoWFm_7rhKGbEl57dEUd6nUIrc4KMFRY7pZUy6K4M_TzUob4hSpiWrMPD7yb70Fk4gpBWvWMYKu72cd8xmt94bAhSjA1kgWgzz0RzCUCRBfjndtT74cJeN0uqBbv-2BABKVNQZ3E2sKTn1t2DX_VbhQCSJxE5HtEVfhAhbWpaWbOjwfoBPBnH91C10_EW1CteUnKGSXp_mkFdb-Wav2EzVQzSmyQVi-RCOPivm6TRgPv-03zEdgKbIUcEWhUypJ9hWttqmTbikKi2nI8LNNA7Y6ODQk6XHCFbg4dsNnrHMXySylc5xlYkwKIXpfiBbfYIVDVUq_EcbbxaXbLB44IkNnJYjv2PynwklEVc1N6SIdVZ9cpLcxEFFHdlyThNn0FWe6w6NDb_g4PQbBim0Yf6t6-pikq2nARaMLg3VT0AQWMC9sn1gkcuOViSfUf1K5lqRueeI3Bl4aaCYM6ca7rcoe91oInJh8H4HCcbYfUTXGrQrtb9CXcPK4yDP99MewfIBprGcFylZqQe5uTXbXaNabqKZVEWGAopzyz09fJbJqVBxVNeIHCtyPXyR-o_Ri_RAlfeSz4d8-Nx4WmgIwPiGctPeXECbDNLe8uTWfWx_FOhOxa8VPLg3AHk1gFE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
توجه رسانه‌ها به حضور میلیونی مردم در مشهد با وجود تجاوزات آمریکا
🔹
شبکه های خبری نظیر الجزیره و المیادین به این موضوع اشاره کردند که هدف قرار گرفتن بخشی از خطوط ریلی توسط آمریکا طی تجاوزات شب گذشته مانع حضور گسترده مردم در مراسم تشییع و تدفین رهبر شهید در مشهد مقدس نشده است.
#بدرقه_یار
#اخبار_مشهد
در فضای مجازی
👇
@AkhbarMashhad</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/akhbarefori/669043" target="_blank">📅 15:41 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669038">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PkQ4RuvYenYWtqXjKfSpvbs8pdwT760J9r22QhpGDYk1GrLGTcr0ioCGfoqPWSPVI_Zr2xjnxbKV_STeMDt7hLla3oMKG_9SoV3pjLMT37pt3MVTkken_oJV9WsZF2izksD4Secyk8vb0NuvqfF_3MZbCO8_7F6IcLBkjgusyuuYG9vMF3Pu0qLZJIBQBUHxE1MXydjtOrY81_2vfbe67HMOtVtv4tkeV_-5RdvHas42Ie0P5A1xJ6SCy4QiZTYO8xg94YMXoiMAiFSBD7qeKBPOxaJwViq79gpiBpGAmnzlzb-mw0JZBz9g4ooV7JTr55kEEZR6hrz0JctQeLOUVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uRwL5_Trak867FKoODVa-VTtCmLwxqBV_lRnKxf-Iw7kbs5AUccNBIH7YKEUdPrYmuBFVJyu7dPOplD4ilcBui9XNu1vKSOIoljLxCqB8LndowFaa3sGyo40mq6IsGzMWupffMUEflpBZyYidTeUi_AwtdSRKrQjGRB678SuqySAl9E8mVsgDtWkdSIlE8mm4qAcnR0ChbvI4c_8ZoPMphRM4Udj0WNlmiXiGj236OeWIiH17GjQCG5CY93H47KctcsOUzs6woriFVsCDxKblFfvXkt65ro68DO93KuoTGag4VjP8XfgC6e96gEDnfTODu6t_X-G36lxskJV-GEH7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/btulMBjpmgyM06gWRHMmbF235yd2qJi1wGdEELi4FoA473_qUDUKzkUWUVZRHwt2Ow1ueRMam9vsLMGOjv8YNdsBiLSHLtXzyUpWOBbbNWaHiaS9PN2NZ1ola8usUQnhZXdHWtaxDtiR8fuwzFuarmudmuOfe01C-rmaDD9m0t8v1CJjWxQ8FRL4dwagx12II0ZKM6Ird37BYq7srveuFV9_ie8ktLBy4aGwIuJNpVqAXC5VjX-CQJaW7TAicKIJfjt5TA_qSJ1emgxckS5c2B3zJYBOlAIj3YUOkvEEgPNOjCWyVHmCQIjOiLkNC6TYifvld61unWCPhcTUAG4qQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZpXf1rlF-YhM8STj9Rq0WKQ66CBwj7X_3PtcASUqm0DA1S2GU62MFKkJUbM_RfiUOa5NHciaMNcpuWIItoaYxukLQbsPeq5xOqtQSDHB2LNiADaYKDQf4lclMSoZGRtKEwPuB5rKDfZQlTpDGa4LQlh-mU4hX_Rzz8m_4zcoeJ6ZQN2OzdsedPMINsjYFPXQXuIrw-Wha-kvbc3RIEwhSBK2-CYyHf2gdgnUwQSXEeOe7kR_l5ZXoGh3BqnEFHaM5xb3-qa-PwRHg0EGSKKlL_NssBI22ZpNSmTjZQ9nqPaV6F06WcU8Q5xrVpXa0d-OEEGxnectvdcTLuYvQg4zTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EtFerBlLyD4Vu5_LrLX3LLOUZta0Z3Rxc-UhUolcL3TNn8pGKqrBp4xh_M7ipWg3SLcJ9heeqgIh9mr1SGwzhH8hkk692dslf7C-hPuuPAnxtGEzCNxERBysieMvEmHpRcqagWQiJE-DsbLt25eMGuUQMTnFMgg9yqiiaLK6lk7vRbykgWfSZCk4aK_u77hTM5wItVVBxIrYLE-UcNCn68rV3gGFnKyTsc7zH3aBezv8R_NUhGX3OHNKZieDb32p8A039dl6oBpjFdBH4APgIUud0a-MAN-OHDSB1fhJT1hDmatPnNRKBqi3VxH3V7kNKpWfC0-rq67bP-3kTQFsdg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">#باید_برخاست
روایتی متفاوت از ادای احترام شهر؛ نخستین المان‌های ویژه رهبر شهید در مشهد نصب شد
🔹
معاونت محیط زیست و خدمات شهری شهرداری مشهد، برای نخستین‌بار با طراحی، گل‌آرایی و نصب چهار المان ویژه از تصویر رهبر شهید در چهار نقطه شاخص شهر، روایتی متفاوت از ادای احترام و ارادت مردم مشهد را به نمایش گذاشت.
🔹
این اقدام تنها یک فضاسازی شهری نیست؛ بلکه نمادی از عشق، وفاداری و عهدی است که خادمان شهر به نمایندگی از مردم، در روزهای وداع با رهبر شهید به تصویر کشیدند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/akhbarefori/669038" target="_blank">📅 15:39 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669037">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/868f73e40c.mp4?token=sFp2VTfKzFu2mnr-UM6Ftl_gj5XwB_6nGNDYMBE6gbdhvUtJ0urHBXdtnSWuC8mRBCX3lvzjZ2dNjDzJm_i27i9ZxAavhsb15P69Q_p8oMeThAbOUqGOxvtDeg8AdyQJLXRcKPXGL9UX997EFtehkHKJbX0HehOgye4txB_pvFWiLhJ8Fd8NXaB9f1YE0kN3Sxvvr3q9r9KFc1Cje2IKkgYFIeqQVfa_3EgIyGuwvnbt-aBEDX-lPAryJjCcKc-dnyvoBVlHPVSIwJb2tB7S9dGRh1X2WkpzOY0kt7BVhmROTIc9e9D_R7nd1GLNuGWrID4Y1H82QOZ6hlqSMxyE8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/868f73e40c.mp4?token=sFp2VTfKzFu2mnr-UM6Ftl_gj5XwB_6nGNDYMBE6gbdhvUtJ0urHBXdtnSWuC8mRBCX3lvzjZ2dNjDzJm_i27i9ZxAavhsb15P69Q_p8oMeThAbOUqGOxvtDeg8AdyQJLXRcKPXGL9UX997EFtehkHKJbX0HehOgye4txB_pvFWiLhJ8Fd8NXaB9f1YE0kN3Sxvvr3q9r9KFc1Cje2IKkgYFIeqQVfa_3EgIyGuwvnbt-aBEDX-lPAryJjCcKc-dnyvoBVlHPVSIwJb2tB7S9dGRh1X2WkpzOY0kt7BVhmROTIc9e9D_R7nd1GLNuGWrID4Y1H82QOZ6hlqSMxyE8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پیکر مطهر رهبر شهید انقلاب و شهدای خانواده ایشان در میان خیل عزاداران راهی حرم مطهر رضوی شد
./ خبرفوری
#بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/akhbarefori/669037" target="_blank">📅 15:38 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669036">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e625359bc0.mp4?token=abKfrdr2GoiUJ-xX4qYKHtWjX0PQFZBxs35tiIDHziHHECBSCMHXvO9MzCJEcUFk54akmszd-QQ7acwZ2YeCF_t-PhFGrw07gFzTIlSfqVdSvgIidM_rMlV7tEV1FM-bJulL5r-qIKm_GblQOzrz-ah7MxdA9tSg18Z08EjityrzWY5A0LVTHUvwjiiz3tmeBcnfBYQjQ9M9z6IzhD3PeqTSUfRBUUenLESt0Uc_BZwbKM-qvEh1UYPxpk8wsONTC23eyE1OaN7zsaFtsTWATBQoReJX3xfq0B7paPid4bip3GF-2pDAiEfMt3Hf_1OX4-MQ7CChqlUvZINWWlUMTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e625359bc0.mp4?token=abKfrdr2GoiUJ-xX4qYKHtWjX0PQFZBxs35tiIDHziHHECBSCMHXvO9MzCJEcUFk54akmszd-QQ7acwZ2YeCF_t-PhFGrw07gFzTIlSfqVdSvgIidM_rMlV7tEV1FM-bJulL5r-qIKm_GblQOzrz-ah7MxdA9tSg18Z08EjityrzWY5A0LVTHUvwjiiz3tmeBcnfBYQjQ9M9z6IzhD3PeqTSUfRBUUenLESt0Uc_BZwbKM-qvEh1UYPxpk8wsONTC23eyE1OaN7zsaFtsTWATBQoReJX3xfq0B7paPid4bip3GF-2pDAiEfMt3Hf_1OX4-MQ7CChqlUvZINWWlUMTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شعار «
یالثارات الحسین علیه‌السلام
» ملت غیور ایران در لحظات ابتدایی تشییع پیکر مطهر «آقای شهید ایران» در مشهد مقدس. ۱۴۰۵/۰۴/۱۸
#بدرقه_یار
#اخبار_مشهد
در فضای مجازی
👇
@AkhbarMashhad</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/akhbarefori/669036" target="_blank">📅 15:36 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669035">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">♦️
در حال حاضر هیچ گونه حادثه، اصابت یا برخوردی در شیراز گزارش نشده و وضعیت کاملاً عادی است./ مهر
#اخبار_فارس
در فضای مجازی
👇
@akhbarfars</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/akhbarefori/669035" target="_blank">📅 15:35 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669034">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c0370ff21.mp4?token=q5Km8gxeW31lweI8TfwAG-ZdDMPg5ThQzOgTdSNDnOXISM5rc-YF3FILUNhDUCMy1rJBz2-xhryBkVLwkdHYh9J1NhpF1CebjW_hxrMNF18euIJ_YJ6wvQWJuS0zaKHEIj_HVc_uO6JkyEGdI0-W069FQ7HSIcPZlYANCXUX_uBBonBpn75xhgtCzk55C91rJuK8j5VWOhX-8CalixriiYwpXJhaSzMYirnxby07ilqyf3nyKUPePT_MXyzlPK_i0A7bo0lqzcZP_DSMkwdgUE2sRhqKOBBzjl7R4at1svSaEYdhY2jrhooLrtm4uqTZlWXDOTaKoAmXRSFChHEsuDQNUvDcgJmM7NTrdrO7R5GZwWLdu57lstUunoRVMM33A9rmllVWFgK_aTDZ5uEL79wdImmzfKnkKYJ63sQet7OGwpcaKkw0yVKZEvpnq5I5KnUilpg7iKix7faK0V-NafpfpdAoRPJlSo8kXiupzqY-7nUS3E7Tmov2hsivi7jOR5QcQrtvrVwiMyllMitBi2yDij68B1o3vtVjH78n0L7ervVhXQsGo-YtruYHIsUpH4fMLIRTll49mmU8lW4QNPDz8s5BZlKH4LA0JMRD3qh3VXwcp3aWWPoZrQJvL8Li46bp89C8PwDZIqYNrqWckWAIZEcDRXMHMihAzSCmT5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c0370ff21.mp4?token=q5Km8gxeW31lweI8TfwAG-ZdDMPg5ThQzOgTdSNDnOXISM5rc-YF3FILUNhDUCMy1rJBz2-xhryBkVLwkdHYh9J1NhpF1CebjW_hxrMNF18euIJ_YJ6wvQWJuS0zaKHEIj_HVc_uO6JkyEGdI0-W069FQ7HSIcPZlYANCXUX_uBBonBpn75xhgtCzk55C91rJuK8j5VWOhX-8CalixriiYwpXJhaSzMYirnxby07ilqyf3nyKUPePT_MXyzlPK_i0A7bo0lqzcZP_DSMkwdgUE2sRhqKOBBzjl7R4at1svSaEYdhY2jrhooLrtm4uqTZlWXDOTaKoAmXRSFChHEsuDQNUvDcgJmM7NTrdrO7R5GZwWLdu57lstUunoRVMM33A9rmllVWFgK_aTDZ5uEL79wdImmzfKnkKYJ63sQet7OGwpcaKkw0yVKZEvpnq5I5KnUilpg7iKix7faK0V-NafpfpdAoRPJlSo8kXiupzqY-7nUS3E7Tmov2hsivi7jOR5QcQrtvrVwiMyllMitBi2yDij68B1o3vtVjH78n0L7ervVhXQsGo-YtruYHIsUpH4fMLIRTll49mmU8lW4QNPDz8s5BZlKH4LA0JMRD3qh3VXwcp3aWWPoZrQJvL8Li46bp89C8PwDZIqYNrqWckWAIZEcDRXMHMihAzSCmT5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خیل عظیم عزاداران در تشییع پیکر رهبر مسلمانان جهان؛ تصاویر خبرفوری از مشهد
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/akhbarefori/669034" target="_blank">📅 15:34 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669033">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d8abb63988.mp4?token=V27XnitAhx2iMddNXuVS42Q1LzhQkpY7vcI-oBbFqFM__UbIDfSmxXMgas7u8lpDmzbyUwTbgSM6fUy8PR0yi4L_0h-MhwoZU3K3oduKQe1U8n-ZVKASWFwwTG_Ti_E4KqYlCQnF0DZVlfPEZ06DFj_0pIyVsZN0rjeRst1HVcui4177QT5vP8xuCwfQz2HWDDbO5z0Zu7P03Iz0CrNToxeOELEu85F2Wms9ZoaVkcRPCpJlTuru-WHdzta0MJq216G2WeTpkqyKmyOHEOIDghfJf6mGc8zqtz66NbmN5e3Sh--sMxPttHxCeqYDnZH27cpaP6HvfGJLSJ7Rlp244Y1_Q2JBeZY3eup9eUtB1tfyFgb7LpTT117_7kNEqa0alVNUq6tNJWwbkEjYJI8HIdpG_8jPRRGH3mthyOpFtCLqO3QFJ0_Rbzj5Nuu8GCvEye71gMLJFKJDSfKZobb38w_WTVBXgleAmoSKPadsgR4zO8VtYFJZAzjJnepftw7P-c_JbewnxUgocYgxYqaeuRsSOYUIsVZwwGRQQk40IHgwfMZjpZAO3BACo-3bfkTdPxgvJw0AjAri9YbLzWcE-Qxpx2EgkAxQO6HTldnW3TCEkjtZtmpMvdehSKIzhGBglAI4J0UbF4Uoona574oFhynnhtHiC7wWhj_B2BojIBs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d8abb63988.mp4?token=V27XnitAhx2iMddNXuVS42Q1LzhQkpY7vcI-oBbFqFM__UbIDfSmxXMgas7u8lpDmzbyUwTbgSM6fUy8PR0yi4L_0h-MhwoZU3K3oduKQe1U8n-ZVKASWFwwTG_Ti_E4KqYlCQnF0DZVlfPEZ06DFj_0pIyVsZN0rjeRst1HVcui4177QT5vP8xuCwfQz2HWDDbO5z0Zu7P03Iz0CrNToxeOELEu85F2Wms9ZoaVkcRPCpJlTuru-WHdzta0MJq216G2WeTpkqyKmyOHEOIDghfJf6mGc8zqtz66NbmN5e3Sh--sMxPttHxCeqYDnZH27cpaP6HvfGJLSJ7Rlp244Y1_Q2JBeZY3eup9eUtB1tfyFgb7LpTT117_7kNEqa0alVNUq6tNJWwbkEjYJI8HIdpG_8jPRRGH3mthyOpFtCLqO3QFJ0_Rbzj5Nuu8GCvEye71gMLJFKJDSfKZobb38w_WTVBXgleAmoSKPadsgR4zO8VtYFJZAzjJnepftw7P-c_JbewnxUgocYgxYqaeuRsSOYUIsVZwwGRQQk40IHgwfMZjpZAO3BACo-3bfkTdPxgvJw0AjAri9YbLzWcE-Qxpx2EgkAxQO6HTldnW3TCEkjtZtmpMvdehSKIzhGBglAI4J0UbF4Uoona574oFhynnhtHiC7wWhj_B2BojIBs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویری از ورود پیکر رهبر شهید به خیابان امام رضا(ع)
#بدرقه_یار
#اخبار_مشهد
در فضای مجازی
👇
@AkhbarMashhad</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/akhbarefori/669033" target="_blank">📅 15:31 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669031">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">♦️
رسانه‌ها از شنیده شدن صدای انفجار در اربیل خبر دادند
🔹
رسانه‌ها از شنیده شدن صدای انفجار در شمال اربیل در اقلیم کردستان عراق خبر دادند و همزمان فعال شدن آژیر خطر در پایگاه «حریر» آمریکا در این منطقه گزارش شده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/akhbarefori/669031" target="_blank">📅 15:30 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669030">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">♦️
محل خاکسپاری رهبر شهید انقلاب در نزدیکی روضه منوره است
رئیس اداره اطلاع‌رسانی و رسانه حرم مطهر رضوی:
🔹
پیکر مطهر رهبر شهیدمان و خانواده گران‌قدر ایشان پس از آیین تشییع و اقامه نماز به یکی از رواق‌های نزدیک به روضه منوره منتقل خواهد شد و مراسم تدفین در آن مکان با حضور خانواده و بیت رهبر شهید انقلاب انجام خواهد شد.
#بدرقه_یار
#اخبار_مشهد
در فضای مجازی
👇
@AkhbarMashhad</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/akhbarefori/669030" target="_blank">📅 15:29 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669029">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Z6Sx0blvfv1ooe88lblzMzbusbAXuO2YTS0HNlv65ZYmSs0MNq33HHERPOpkC9n6yblUtElU53myKChroNnFE-_GxT7DWcnQ3SQldaXEw_vgh-c-SmrxW_YNNuIQ0JLubd1usfRATS2Esfza5AVN_dj-CHnhFg4Mz6qmJS64TrIEVymDssK58fWmQ8nmf-GWGzn060MOxHCEhtam9lZLbM2Y4Oq0l6nZfWMJgBQjLirE5t9kWS9VgTNZshPRQSrKQ8Yt0XJN3rfuO4gMwNHXdDcWTvOPaIRB02XyVk6tXTuomI6vkJFPC-iqz_7wf6ysMJdYWaFbsK9Q1rWHwVUs4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصویری از محل استقرار پیکر مطهر آقای شهید ایران در صحن پیامبر اعظم (ص) حرم مطهر رضوی که پس از پایان مراسم تشییع به آنجا منتقل‌ خواهد شد
#بدرقه_یار
#اخبار_مشهد
در فضای مجازی
👇
@AkhbarMashhad</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/akhbarefori/669029" target="_blank">📅 15:27 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669028">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fWXsRU8oBgr4J7jAeQ5J1kZev1SV9JZAyN6C_obnvDHsL5oWNIt3oL8H0qDcoFSHw4N9uZPfvlq2aCx9IZGDva1LUkVHNR65DKAKUvSMp_EEaWN3NMeu3B2UwINIkb8EZiV_3cgvGsRQjvGPawWopI1OOl2QDGJqB9lJRCeaTF2VTTR0mZU00gUv14CuivaEfGQTZJ_33t9sFW7AoHDEyDrxBzcIFfcYKf4Y3w_wMhDEtPGxQRKb2kWSTUc3gnyotMHcWEbvN4aFcxSLbxaAF_amKx2x8t0liH-vC8y13-emOFrp7JAioEh47Fm0rFIEY_flizzYBVl23l_1rQ-Bvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
شهادت یکی از نیروهای مرزبانی هرمزگان در حمله آمریکا
🔹
ستوان‌سوم حمید زارعی حاجی‌آبادی، از نیروهای مرزبانی هرمزگان، بامداد هفدهم تیرماه در جریان حملات هوایی آمریکا و رژیم صهیونیستی در محدوده بندر کوهستک به شهادت رسید.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/akhbarefori/669028" target="_blank">📅 15:23 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669027">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s6gKBn_C8hdg9AEEHVSxn5OQp4WWRXuBJM2cW-d6BKyTu6jtBuL0uVnepwxHx3CLk08V98qaxJ_xIhG3SPRu9eIIfqduwFZR2EBnCRObTb7JfaFxnLQ1EQ1Rhbm7tAV2G-SBWpg2xBimzTNRgZLxMjzXUj9rVB19kRZRIhuwLVVcwOO7DWgJ2dXAoqpzIYyW1RKmRoRL8mNuZebJ5V-jVN6hRGu9sBe71Y2-8pcrn0TkR0Fff51XGz0LzfAjvHBy-K0iSmwVhuHGoZkVIuYwOqY_YKunuyYQ5g4ClK3YZ_gbz5vxgNyuvNojpv4k4rfLMMT9tloyCJvrQ_SILBiHEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نیروی دریایی سپاه: ماجراجویی‌های ارتش تروریستی آمریکا پاسخ کوبنده ما را به دنبال خواهد داشت و روند بازگشایی تنگه هرمز را با اختلال مواجه می‌کند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/akhbarefori/669027" target="_blank">📅 15:20 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669026">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">♦️
تکذیب شایعه تهاجم نظامی به کرمان
🔹
معاون امنیتی استاندار کرمان ضمن رد شایعات، اعلام کرد هیچ‌گونه تهاجم یا تهدیدی علیه این استان رخ نداده و وضعیت در سراسر کرمان کاملاً عادی و تحت کنترل است.
#اخبار_کرمان
در فضای مجازی
👇
@kerman_news</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/akhbarefori/669026" target="_blank">📅 15:19 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669025">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/89acbaa58b.mp4?token=QfUiWUqnsL_Dl9LifssRbLzmWWt6SO8joodU12YPniNjGJXa7DsYlwxK5wtFHpnvd9pG3w0B1VvczVN0EOCkxfyexWpW3GOKpKlm_7RX0HxEpwM-Kt2AdatRl5dvNySr_FS9YPp4gSMLnUomL1r3w9A4WybIvi9iJfjIhfm5qs3jg-DLNrFd0VCnzirXFGXT46WoWzMN2E3_0b_cEi3DKgSXZC8IFczvpkNjOiY7RCWjoL7PKveA-GZKxcyGPfRjiClwTXSU0Pu8a3HE4LUJ3ghUOUfvvdysVzf7HeaaaktnI7U9X0KusHUIY1pcvc0-5fgRZ6-mdIUTXtdvCooAAlZWSvP0mEg057-MiTGIAze6eUaipTUffEIu1Y2V7KsACzL-zNucC2E_WT4noEL598ytgfsZkzGdSaoxhV9Jw_ivVrm3FtcSuTh7mIV0y2nJumvgbEd5xVMyaEA9jVVYuk0zMPP7cfitAoFsYRhkUlrZaVbluMoQ3bzXmNhSh83Hf6Bg1Bh0LDtF-6mRaB8WMWTUo8BcmOx7uZuLaaLvupz9M97y-h9aOdThPfpS4zhAnozzs0thvZpul6oZTdRg__MYQ5L_uXTxa3iqCkStQd4ka7eIZMdKTo8ZEWfdB8SArmjjwyGEZKIumyPjcMPVgayIHmpJefpLXraxe9tOYnI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/89acbaa58b.mp4?token=QfUiWUqnsL_Dl9LifssRbLzmWWt6SO8joodU12YPniNjGJXa7DsYlwxK5wtFHpnvd9pG3w0B1VvczVN0EOCkxfyexWpW3GOKpKlm_7RX0HxEpwM-Kt2AdatRl5dvNySr_FS9YPp4gSMLnUomL1r3w9A4WybIvi9iJfjIhfm5qs3jg-DLNrFd0VCnzirXFGXT46WoWzMN2E3_0b_cEi3DKgSXZC8IFczvpkNjOiY7RCWjoL7PKveA-GZKxcyGPfRjiClwTXSU0Pu8a3HE4LUJ3ghUOUfvvdysVzf7HeaaaktnI7U9X0KusHUIY1pcvc0-5fgRZ6-mdIUTXtdvCooAAlZWSvP0mEg057-MiTGIAze6eUaipTUffEIu1Y2V7KsACzL-zNucC2E_WT4noEL598ytgfsZkzGdSaoxhV9Jw_ivVrm3FtcSuTh7mIV0y2nJumvgbEd5xVMyaEA9jVVYuk0zMPP7cfitAoFsYRhkUlrZaVbluMoQ3bzXmNhSh83Hf6Bg1Bh0LDtF-6mRaB8WMWTUo8BcmOx7uZuLaaLvupz9M97y-h9aOdThPfpS4zhAnozzs0thvZpul6oZTdRg__MYQ5L_uXTxa3iqCkStQd4ka7eIZMdKTo8ZEWfdB8SArmjjwyGEZKIumyPjcMPVgayIHmpJefpLXraxe9tOYnI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آتش‌سوزی یک جنگنده F-16 نیروی هوایی یونان پس از فرود اضطراری در فرودگاه زاکینتوس
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/akhbarefori/669025" target="_blank">📅 15:17 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669020">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NMU0toam_JCYoOFTUjMQGgahDkCMxfjYtU1KiM1DkKd4SYppjMkwdlswc0H2nIiK0ko7x4_sWAKUVYn-P5B0ZmaxyrMWDRIFI9S5sygzMV_Z2g_dWAvVCeco6KtrMjafcjZpJEmqUC5qTv8pNRwRFxd2C2sZOOBcDTuBrKRxWNNBZswpTzbL-MgdjbNjz1vjdbaB_Yi-CDCsyRfx7mT7VGs_J7qIkre4MbsMbI2itsNTiioyY7DbD7BOW2nukxpv6C6O-WyLyMlp27gj7KhaCA35YB7AyDZjDIfr33bKJUbbMkBxNgYazh_28XP9XsSvozd2QYs8u5eORH3fp5Rwug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/v834gohJnYFWMCC0_qbMKjfdbqGhq9Mr1rQJbIquGHPyKzekXDVtoNeUJc0U7HXoz_pw5Lp9ut91psbjLArM_CE0Refr9sLjSv8qC2tCJ0G70kkHmLttHqZeDPwFWaVDsV5cYJGO55JNrIMyF6lOZF5nUvF5V3VxYiNNFupiCUjJwgYUAPdFE0NyXb7kZbFAgzqpWYurLh7McSEtjHLvymF6MJsjK_zRH7uJpKpmProN5j70j9M2zewnC0JopG7gkHToZQc1Ebrg28kXq458R0o6QCQpZJEAM-G3E8IQHmNuHDpQ162gIky-jF5AGqztBpOsHUr7I2do2S4UQeyocw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UHcMkPSPJE2yF74vdioXYu4A14vttp9VuF_tKbl1ZgJV8du258QxlCFuVKS7m8TTZ5j0LHl29YP2Aye5ZzVwjshfxGxmyNSe5-2SLwEFwp5lhxEkX4l_5oBP1m818Yu6D0vH4_xU0tK4zagS49kzLDEJx7jdxkmcUoTpqKwnyyCXPHywzFzsXGtagVBmvgf2Ku4Fjj3Myk-E_LDPeBIb80ufpsjwB7hxm612cji7fL_ghEckR9SwunU0Kaw7HL7XMsp_FYPsJvgZlGNrvbP_rw7EIrqnOJbJJKeET1l-KpNK7lnTz_Z-QVPZjxakoef5gZL01Z-ZKJ1KhBKJVXaUDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BPjc4fniBb0jUg0ZGEk-HycWgSMIsBvc332dqeOXF9OZ5PPfP4iP6bmqpqCGSDh1avTPxTXWsh-YpG9i6LvKlAslq7hdaBHjGFi9KoKt1x-91LbHuhMEt8WBY9yiGUbRZJiOCxOd0zs-kIxrqGTFjZ2YmmsVF6qIDh3N2oyA9MqFe_KpyUiLTmbX0SbS-g5H2vG0dWkqWg-6P4Xc6qLYZ9lyxqnQvjBjktmxt7WkkelqZ6yRsvBq2LThjMfJEOF5apwF6SwedTph7pdLkpoXXvtFNxmmTIZ8Z2t9lFsHPBsE-4X77zC2ML8RwruJRx4XGTwPYjc2DRc7QuHnlcuIJw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
تصاویر خبرفوری از ورود پیکر رهبر شهید انقلاب به مراسم تشییع
#بدرقه_یار
#اخبار_مشهد
در فضای مجازی
👇
@Akhbarmashhad</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/akhbarefori/669020" target="_blank">📅 15:17 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669019">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a6cbce3695.mp4?token=i_xpFZK0zi18ccyCZAKB3zcoBtrSATNs9EdjyHx6p9k5vCDPrA0KOePo6zC_wxYHkcBt51rcoyACyXXS4rtZBf4lKjPQ7KGD0NY8J0Z9BLZAQR8BAQ5QzFADk5D2MDd6SrtmyeAT_4lR5s9Ly8QTRaGU2MIDZlG0ZgT4XCkYMNSrYi_AE_ITNCWGk4nnW5eJ_78p9XmHqQsPHVtBeDu1t9F7b7UO1dLpMknUuDIdlci1EMUbb-G4kdTnCmbCJpRKkMzxODMfc3kMjdT8m0lc_uoiV3zk9wFkarG-xqPSQSFIEKvnhBIBxIHTFf050uYhPCajCXpefTtCWMyTnVPNg6SaL2DJP3n87-8eYDp5HeAeCCwTuNF0G3Lsp-24m7b6uyF6gqjMFG5-NvuNjRyWK9r9Abs3m7jLwdBKKPfqSYq2fUlqJ9GFJ9omyE__32Ymo-Tdsv3Pef1-U-mND39wfsZ7UlFcgywtR84jdwf3chL5tpltPb9qOs3HvaK9sO0XzFC2vpUxYsoZiaGKar4OpPW9nEP2j6vZQ2LnhyB0SK4ORzLikS1j6kJNuPhwAUjQo6Plxz7HiEKDTm9QlZdycK7c8Okp6HUYDoYzBDO9N3R1vy6lR7bNMGjwzC2nJwJEt04Kjgn0Jj7bCdsv80e20vfFF4OUGLlie2h1aUMvWd4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a6cbce3695.mp4?token=i_xpFZK0zi18ccyCZAKB3zcoBtrSATNs9EdjyHx6p9k5vCDPrA0KOePo6zC_wxYHkcBt51rcoyACyXXS4rtZBf4lKjPQ7KGD0NY8J0Z9BLZAQR8BAQ5QzFADk5D2MDd6SrtmyeAT_4lR5s9Ly8QTRaGU2MIDZlG0ZgT4XCkYMNSrYi_AE_ITNCWGk4nnW5eJ_78p9XmHqQsPHVtBeDu1t9F7b7UO1dLpMknUuDIdlci1EMUbb-G4kdTnCmbCJpRKkMzxODMfc3kMjdT8m0lc_uoiV3zk9wFkarG-xqPSQSFIEKvnhBIBxIHTFf050uYhPCajCXpefTtCWMyTnVPNg6SaL2DJP3n87-8eYDp5HeAeCCwTuNF0G3Lsp-24m7b6uyF6gqjMFG5-NvuNjRyWK9r9Abs3m7jLwdBKKPfqSYq2fUlqJ9GFJ9omyE__32Ymo-Tdsv3Pef1-U-mND39wfsZ7UlFcgywtR84jdwf3chL5tpltPb9qOs3HvaK9sO0XzFC2vpUxYsoZiaGKar4OpPW9nEP2j6vZQ2LnhyB0SK4ORzLikS1j6kJNuPhwAUjQo6Plxz7HiEKDTm9QlZdycK7c8Okp6HUYDoYzBDO9N3R1vy6lR7bNMGjwzC2nJwJEt04Kjgn0Jj7bCdsv80e20vfFF4OUGLlie2h1aUMvWd4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویری از ورود پیکر رهبر شهید انقلاب به مراسم تشییع
#بدرقه_یار
#اخبار_مشهد
در فضای مجازی
👇
@Akhbarmashhad</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/akhbarefori/669019" target="_blank">📅 15:11 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669018">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">♦️
هشدار سفارت آمریکا در اردن به اتباع خود؛ فوراً به دنبال سرپناه باشید   سفارت آمریکا در اردن:
🔹
گزارش‌ها حاکی از آن است که چندین موشک‌، پهپاد یا راکت‌ در حریم هوایی اردن هستند. فوراً به دنبال سرپناه باشید و در محل خود پناه بگیرید. در داخل خانه بمانید و به…</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/akhbarefori/669018" target="_blank">📅 15:10 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669016">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">♦️
پیکر رهبر شهید و خانواده شهید ایشان در میان عزاداران عاشق مشهد
#بدرقه_یار
#اخبار_مشهد
در فضای مجازی
👇
@Akhbarmashhad</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/akhbarefori/669016" target="_blank">📅 15:08 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669015">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PJUEM3aoN8Yt4AqrpsoxvqLzUDvWojpEQW5WX_UumZsFBpkp_La-zzWiQvCCOUwJG6Y8txxiXNxwrEi9kbQ3IMQ0G3R523Cfydstvsvf4ExOgjLP8cT2kjAX3qTuwI6jkEizhNAaydmXRpjRKuWXps_be3fosDt9iqGwAdfp-zc-WBjDtj9yggkyQs_82Ppp1z4FkvMEaG0gj8UVh4AW1B8VhjrAHIpvx9opIC9dENDihxegpKJXy2BKttm75k37Hvs3P7QeA-DVMRDHNTV4BLtSe_y-F_DySzrby1KzfYAHKDgwruJfXMbr1FR_TO74M25PZ9dwpL7Dp-4mkHJ01Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اجتماع بزرگ مردم مشهد در مراسم عزاداری شام غریبان قائد امت و شب شهادت امام سجاد(ع)
▪️
با کلام : حجت الاسلام برمایی
▪️
با حضور : دکتر سعید عزیزی
▪️
با شعرخوانی : محمد رسولی
▪️
با نوای: حاج سید رضا نریمانی و کربلایی علی اکبر حائری
▪️
با اجرای :  امیر مهدی باقری
📅
پنجشنبه ۱۸ تیرماه
⏰
ساعت ۲۲:۳۰
📍
مشهد مقدس، چهارراه احمدآباد
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/akhbarefori/669015" target="_blank">📅 15:05 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669014">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd16554b7c.mp4?token=Z6JGzvvtr-3z813Xd_Vlv1py0qxagHbhnjsrlJFgpiHQyJJs1clvcvDlPIjd95hqjBJ-WhNqKdQQWVlUSRLI68zXMUSBddxdZR1-jYS5ZDIvNyLnKqYq4mzq_PFscJp94XlPVTr1pzV02oJf8JtAzGssxVSfRYpCHtGLFRPqapjdr_AZ7g2E6K-qt62vGzWSqmyvFprMtjEobXuBIRHLHysccfabg2icU0H8iRjTEPpt1ZGmkHUsC1pK9jmjxfcCLtr6SzX06ixcL2VWGLq1fcKD_sawormF8rehL34XAazCfjkCu8C83-96rvBClwyM8fyXBWzcOnY2fx4_iq5RVVpjQ6S5_3mz2kTz9YttAPJGTVV162ZKsp8lfyW-FWB1cpP3l5zr77Bdp1U0C1pjJ2sxXecC7jmN9_Ml3GUix-LiDrb-dBYBT2_zjysO-HMzJ_1PD7NJ1A7RTNqHcyu5LzLflj5QLenHndrH0k6OdI0heLaoWgMdhi6k4gzzTf42JY67b378izh9j8F55LHTNcdF5v-2tUDg6aJQnQTp4d0GHEItdDfmOeIqqw-C8nGNfZfLlpkOsiB8xpeO6ADwQxS0zyqX9vtz9m5LS0ES4IMCOoeOuh1dmIQqRRw0KwlgB6XJHKoOqzkAdtoR6eL7W1EALV9Nvd8xm4l6F0ctj1s" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd16554b7c.mp4?token=Z6JGzvvtr-3z813Xd_Vlv1py0qxagHbhnjsrlJFgpiHQyJJs1clvcvDlPIjd95hqjBJ-WhNqKdQQWVlUSRLI68zXMUSBddxdZR1-jYS5ZDIvNyLnKqYq4mzq_PFscJp94XlPVTr1pzV02oJf8JtAzGssxVSfRYpCHtGLFRPqapjdr_AZ7g2E6K-qt62vGzWSqmyvFprMtjEobXuBIRHLHysccfabg2icU0H8iRjTEPpt1ZGmkHUsC1pK9jmjxfcCLtr6SzX06ixcL2VWGLq1fcKD_sawormF8rehL34XAazCfjkCu8C83-96rvBClwyM8fyXBWzcOnY2fx4_iq5RVVpjQ6S5_3mz2kTz9YttAPJGTVV162ZKsp8lfyW-FWB1cpP3l5zr77Bdp1U0C1pjJ2sxXecC7jmN9_Ml3GUix-LiDrb-dBYBT2_zjysO-HMzJ_1PD7NJ1A7RTNqHcyu5LzLflj5QLenHndrH0k6OdI0heLaoWgMdhi6k4gzzTf42JY67b378izh9j8F55LHTNcdF5v-2tUDg6aJQnQTp4d0GHEItdDfmOeIqqw-C8nGNfZfLlpkOsiB8xpeO6ADwQxS0zyqX9vtz9m5LS0ES4IMCOoeOuh1dmIQqRRw0KwlgB6XJHKoOqzkAdtoR6eL7W1EALV9Nvd8xm4l6F0ctj1s" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پاسخ موشکی و پهپادی ایران به پایگاه‌های آمریکا
🔹
سپاه و ارتش در اولین مرحله از پاسخ تنبیهی خود، زیرساخت‌های نظامی آمریکا در کویت، بحرین و قطر را هدف حملات موشکی و پهپادی قرار دادند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/akhbarefori/669014" target="_blank">📅 15:04 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669013">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa41a940a5.mp4?token=VGGOXlmTTtijWSkiZ0jq5988P8JH71cLHrUAVp1_j8F2GfZ_pQwKdE0G9BnPciiPXl3_VCQ3fRGjE0-aYir9zcuCcIf398VTpxs1ig05olJRj-Jt5Nqkw0zYXLveOKxBLztbhrCCJ0LvqH-lEsGUAl3k1qDBQfbV9Q78_WbSE0ZUgVFCtqpgfjrbqqrjIGmgoUsdxoHPsxJmQEyVd65kFrgg7qjzDs_PgJ2_X-V9uNtJBdkwvoe-D6tgnaRmHMnBDj5A9QEIoWy91n4zsXhkxgkwCvc9ZVyuledCNmdITP63JvAjBlgj0z-DyJ0qJOFs2QU_8uaeVmBjdukgPFriDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa41a940a5.mp4?token=VGGOXlmTTtijWSkiZ0jq5988P8JH71cLHrUAVp1_j8F2GfZ_pQwKdE0G9BnPciiPXl3_VCQ3fRGjE0-aYir9zcuCcIf398VTpxs1ig05olJRj-Jt5Nqkw0zYXLveOKxBLztbhrCCJ0LvqH-lEsGUAl3k1qDBQfbV9Q78_WbSE0ZUgVFCtqpgfjrbqqrjIGmgoUsdxoHPsxJmQEyVd65kFrgg7qjzDs_PgJ2_X-V9uNtJBdkwvoe-D6tgnaRmHMnBDj5A9QEIoWy91n4zsXhkxgkwCvc9ZVyuledCNmdITP63JvAjBlgj0z-DyJ0qJOFs2QU_8uaeVmBjdukgPFriDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
صداوسیما: همه کشتی‌ها از سراسر جهان برای اینکه از خلیج فارس و تنگه هرمز بگذرند حتماً باید از مسیر ایرانی عبور کنند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/akhbarefori/669013" target="_blank">📅 15:02 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669012">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rlBjoPNOnFlAn7erE-b5emUPxs1PlShWUIK_PwNbpT-ZtL3fRWSrQjIsaDrXhzKUzQEi1W-N1DpsDdyATO8M3wyZVXfvvDsHpiU6m37PGX8x6PLIv6GtXeYDI8k7tx7QBiuVtEGVXXkZyv8_OWB9acNgvvC5ifdHjSpBCM3_Oz4Tw3wt4xREfCsj8CKFw2ofw7iD146tYTaopN8LGJrTodxSikMDv8pig6BlnDIkJ_Gp8hzs-uDG3w5-7IkazfCHrWzwpxefjhk5HGDLr6drS5sBnqKKEGhe5_4wFlgrR8Dqw6krYT7rbrV2S41Z_fDS_oireRaIAgCpXMHnLgp2ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پویش مچ‌بند و پرچم سرخ
🔹
مخاطبان عزیز خبرفوری، برای شرکت در این فراخوان کافی است با مچ‌بند سرخ و پرچم سرخ در مراسم تشییع حاضر شوید و تصویری از حضور خود را با ما به اشتراک بگذارید.
🔹
مچ‌بند سرخ و پرچم سرخ، نماد عهد، وفاداری و خون‌خواهی امام شهید است.
🔸
تصاویر خود را برای ما ارسال کنید
👇
@Ertebat_baforii
@Alo_fori</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/akhbarefori/669012" target="_blank">📅 14:57 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669004">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sGPwxEJMq1hycyc4fEkzwJJjADe8rnH5kL5PG-OGRJ66mLGpeXzielPy6mBNoHYqefZZfxqdF9Muo8lAjhCpm-pLNXFW5Wn4UMKtMN4Dg4qYktOLBqbscyZsQi6zBCspBwrohqNuaTlsB5XjyBEGozn29HDAzjqURvVXB3nsexbO74gFLRXvgQ4jUGHGPooLwGXWMvhfaqCB6xUjR3f-bMp6CJLoL5E71zwGKEB4SwSeRVh3TKrjj65ZC3gV3o3dudQ9qHBb9qpUwkqbQ4qMO-b5h5hNEkHkzc2sCJGJxfPazXt0IImGbeqD2clPudAMDE0CfHulOyh1Wylpv51QVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XMdCSUwCoQWemtxzntzeWLDNC6FkJV_mBZqY-OYpJfYygidSnIoWqeiXawZKrFhn3yFfek80KYmCbKKa6XDgdwX-eEosowDoOlzN83VZ_-gRsr_3nSZuVS_KAMbUfF6Gc3Mga5a9Mk0qh0l0v1Hr6hVO4sjl0j2IV5YGAokIcawuHOeAtIuSn6P-PJON6iBY0jlJrBOQ7D-8tLf3lVlj0spA8dL02RIwUixY0tYgGMcNWyWE18yuKR4Idy1zmRRQWEtJ5uOf0cJBFfxK4FEldQCBUvaQJNsHMMQslVeg3nuRfB_Hg-jZYaOWymUgTDji_wtcQDo9cHFRTe7CKknPcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GQIDHq6a2vI5jHh2Az1W_QSUv82VZCBvLMWaAAgNC0bEAnhx8H4b8xG13mbqRy9_9MBsm_yLKNKD2uhMKsFaqVYYyAunY_4WgaSGM5Egd2h8_De3Rz6YDajlcUfvFIzezy0gFghDZd42addlgKhItMDCqGazpEvAKjN1NZthgu0_DVdaiF7fdJes9eH7uhc0IJsszDA_JE7N_Y8Z60i-wdv7lOWb27z5ypFsMtDD-5751XTHi-LHBY8D_Yab4D7zEVZUKJLEu5M6Aw0dLc1pPcMcWH3WRDHunl-eIu5SVozdT7Qs5-p9LHEBPvaMO-KP2l5AV-gWg8DlwN84rBkp8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rzaCy6q5NLGzET9lduITzlxVX6_SGFJ2xhPyVyrv3yVtfX0EAKd34C2wMF1eUK5t0-RKCyl9MXsUt40CNPBOY_LQXy0wWvESn3BeXOz82WBO9AKjJZ_Bp3J0OOxXvfTMgD8EHJczmU3cYrKCnNFn0J8JMj8MNdXPSisYXUZgacC1tT2MZ0wjgrj5G7U6v0fRnuSkFJKvtbQ6b4C6h29YaOt9lhsMnB30ebjAnhDpUlZQdCqduoG8AXy9RIxdWHtzXjozdVPMLhwMgWdigdCGsxK6PJoJXkaFD3zrn-nJo3sJKUUzJozWSpBDeIUSIAF0DGC3WMEJc-xSRt36CENu6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/phhDwor3KW9SxyM0QBu1PY6Znp4U5b--tJ_b-XyW2HuF6eIqkHxyS8RNpZgQG9TGalUXPoRknAHxApHP1S_EnMtreVd94SfT1ow2fvfg2_ATxL94vj34QbhbF0K8H02e-No1Bs_0rFezV9bddTGELOLdERDKsE0LheVk72lZLTX-Ib0VxrZ12GVnH3qkYpE3h5Yy59Ih1Vxu2rhVzJwc_KFBKjvpkJXjepBNb7T5dNznXF0wu4lpOK7NfRhDZZIcsIaDr2pOg6waaQO7dwrYZ5pGHnVlGPbIOI2_csKy7pD5RouuXZSPE0Pga0EYCm0d-a7fDPkyWbsiFUOHFwbJDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LT8CLd6ewJIdxphuC6YKpAJjGosmJ4-yi273ICBIhqj6tSYMT3tKXWp07bfXMIjlw5J33abgFzCPkwRC8v7IhVCGSLMWw_2rpcJ1t2PUPf4JF00Q6QP7ZxI-AVvs_G6IwCRx-x_6N0yLF9d_-XXfKulgXvYsh0VtHKGAUf38FpIAGMKvd-cVJIIZfVFP3IfSGo1QRzkUDURHrcp4P0bUcwkVCw2W3H8lZ-v77w6Vq19EJSxanNfgxKqHoSM7nHswTzxVn59-RA-NYeH4qfitU245b0dftu6wafiSoGAd8_Migv4KQVRveI01Y5w0cX60_M8tT10lluhtGYQoyBCXHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/i6aA6wY7cyIiiEj3zwMMf-habpCV9TJNB40rk_q9GM8pfotN332cRcC87St6DKPE3AjnmW1f1NJahsn3I4aMeAphL35rXK7_gvwdy_3PN3xObEosAY0YB_mnYgQiCNLbPmC0e6o8O8FbUYOspTB8y2bg810tWcZowtEBFjZptKTihguidrZXVxca8A9qIePH_OVTzfJ4aJVlPL_4L_snG7pCAyfdb5hol8wxOY5S2xLhCd6HFt1lROlpby3f--pwpIZhYi-4hXf6epRE-_hJqL_IgI8u0jwGCPNBbe8CPlDdKfwJf91Wdmm4Z4adwOXVuc7_FiyV0YVHiSPi9R4CKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/c_Yej8EA77fybJP28q6lRX-8A29PpMgGYxnyGDfuqnHSQn69vnkkWXK7GRTGR1e-OwC5_c1i7layZ_Iz88Gda8tZyHfldWiyRmE4bh7sr-1pFRYyP8flhEYZ1sm86vDDXfQguzR1enzH_ywzmGQi3FN71J5-C3AsQqxbHGrDMM3DZqrK2MYBPcKHPRj5u7O_42py_j44rmEK-yOrXq3BBuSKh7anFJg6lg0ydJQC0rRfDWxhqeA4MTc88sUQEV6-XCoK6jy2rPmqny9Xfl8Bq3IoChyIzg_FTn_xj9IK5rP3SUxuDAH2yFqsJzY9k9XKPJPI4ZSIaiiTluNzCVo1YQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
توزیع هشتصدوپنجمین روزنامه خبرفوری با تیتر
#بدرقه_یار
در میان تشییع کنندگان پیکر مطهر ابر مرد تاریخ
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/akhbarefori/669004" target="_blank">📅 14:56 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669003">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">♦️
صدای انفجار در خلیج فارس
🔹
حوالی ساعت ۱۴ امروز، صدای چندین انفجار در مناطق دریایی و غربی بندرعباس شنیده شد که احتمالاً ناشی از تبادل آتش در خلیج فارس است.
🔹
برخی منابع از فعالیت پدافند خبر داده‌اند، اما مقامات رسمی هنوز جزئیاتی از ماهیت حادثه یا خسارات آن اعلام نکرده‌اند./ مهر
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/akhbarefori/669003" target="_blank">📅 14:53 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669002">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">♦️
مدیر بنادر و دریانوردی شهید باهنر: به شناورها و تجهیزات بندر سیریک بر اثر اصابت‌های بامداد گذشته آسیب وارد شده است. یکی از اسکله‌های شناور بندر سیریک دچار آسیب جدی شده
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/akhbarefori/669002" target="_blank">📅 14:51 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669001">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">♦️
رسانه‌های عراقی: صدای آژیر خطر در پایگاه ویکتوریا در نزدیکی فرودگاه بغداد به صدا درآمد/ خبرفوری
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/akhbarefori/669001" target="_blank">📅 14:49 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669000">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">♦️
پرواز جنگنده‌های خودی بر فراز آسمان مشهد
🔹
صدای پرواز هواپیماهای نظامی در شهر مشهد شنیده می‌شود؛ این پروازها جهت تأمین امنیت مراسم تشییع پیکر رهبر شهید و پوشش هوایی محدوده حرم رضوی انجام شده و جزئیات رسمی آن هنوز اعلام نشده است./ مهر
#بدرقه_یار
#اخبار_مشهد
در فضای مجازی
👇
@Akhbarmashhad</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/akhbarefori/669000" target="_blank">📅 14:46 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668999">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e7b7b47f69.mp4?token=XeliRu9tVfdueLaWRGNEPHt5x111k5_E6EXhqb5UPSz4c_G4OKPMF8aQLDB9_XWa6bdgkpZYzZ8FsTJg0WtveHdtO9v4ZmE5ud3xTwJTPFl-tPDTi5koHEHVxBko3RbiggwTDB-bbKIrXEHvzr5iSE9SIn9YDWYKkRcurp0z_tvL87kgq5Fu6BxlxA7RVE0xaDaVQsLjgbl7u4tb438RYcLc1ufKPc1QkTOk_9sXKlOlyKoU_QFX8gJtkNSqekO_WgGTYNAJrDREySNS9TDgP_8wMXZp34N8QrhHbKjTcEifxBnANWWRWj_G2Gj0RcwdI4zEiKKl0cwCp4P5pBzTdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e7b7b47f69.mp4?token=XeliRu9tVfdueLaWRGNEPHt5x111k5_E6EXhqb5UPSz4c_G4OKPMF8aQLDB9_XWa6bdgkpZYzZ8FsTJg0WtveHdtO9v4ZmE5ud3xTwJTPFl-tPDTi5koHEHVxBko3RbiggwTDB-bbKIrXEHvzr5iSE9SIn9YDWYKkRcurp0z_tvL87kgq5Fu6BxlxA7RVE0xaDaVQsLjgbl7u4tb438RYcLc1ufKPc1QkTOk_9sXKlOlyKoU_QFX8gJtkNSqekO_WgGTYNAJrDREySNS9TDgP_8wMXZp34N8QrhHbKjTcEifxBnANWWRWj_G2Gj0RcwdI4zEiKKl0cwCp4P5pBzTdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویر هوایی از جمعیت حاضر در مسیر تشییع پیکر رهبر شهید انقلاب در مشهد
#بدرقه_یار
#اخبار_مشهد
در فضای مجازی
👇
@Akhbarmashhad</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/akhbarefori/668999" target="_blank">📅 14:43 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668998">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H7mmSPoFQ6sApgFBK2rlxo2oozvQ8oW0KZX-_FhxXoSA65FgYL6aSZPk4rZW5NFYfLQ3p6cQCSFiE3DImSmw9wjvaTqtTWWOzndp969PCjyVzITnjl25NGrN05zDigyNuiyZ78hTpb0l85nntiEkzw2AnoHyznvPt-n9ILf329dpwVOj8WBfQF3xcUjsqfmB_K1AYG06ibrHH1kCzcOoq69Nj3X3az8j0sjPNo_DA8lKqrP9JA9VR8QwUmiIncZGlDN22pb9r_IQkLa4H8evicjmgGjT45km1xDBuhLww28Qtn91TJZ8--qap8VH7Y2ud56J3kNQ7eXkB1ILgMKd3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ادعای تانکر ترکرز: خروج ۱۰ میلیون بشکه نفت ایران از تنگه هرمز
وب‌سایت تانکر ترکرز:
🔹
تهران به دلیل احتمال ازسرگیری محاصره دریایی توسط آمریکا، شب گذشته دست‌کم ۱۰ میلیون بشکه نفت خام و نفت کوره را از تنگه خارج کرده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/akhbarefori/668998" target="_blank">📅 14:36 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668997">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">♦️
منابع رسانه‌ای: آژیرهای خطر در پایگاه آمریکایی «حریر» در استان اربیل در شمال عراق به صدا درآمد/ فارس
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/akhbarefori/668997" target="_blank">📅 14:35 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668996">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">♦️
موشک‌های ایران در آسمان اردن
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/akhbarefori/668996" target="_blank">📅 14:32 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668995">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2dcc65c428.mp4?token=Y3FORRdxiHe_ohwZHRe2gltKqEeGWs46PeplOlHe4ol_FqQpd78SvZ0VjL6xaCsvtNJaew-Hz9mTk-BMx6-nw-lEwWiKaJzTSYTWdxwMUrhtg8xk8bHTBCmBrocDGP4TUpyVGzmMiK-OVvuH4BTt42bFrjeE6LAVLJE_zW563NTOHoRWrvqXuMbVMbdmMdyHvS8kXCAmcQFXSlmoBi6-pNts7-B8OxRAMKR8_SbCiDUiWufmB8ffj_Y06C2Jv5sugC4Mg7bomJDvYuZoe3AMTRjAn862M6p-sRMGxMP6ATy_un4f89jUwuVcztDoWmsh9ECS1d5BHB4tnS1tm9bw9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2dcc65c428.mp4?token=Y3FORRdxiHe_ohwZHRe2gltKqEeGWs46PeplOlHe4ol_FqQpd78SvZ0VjL6xaCsvtNJaew-Hz9mTk-BMx6-nw-lEwWiKaJzTSYTWdxwMUrhtg8xk8bHTBCmBrocDGP4TUpyVGzmMiK-OVvuH4BTt42bFrjeE6LAVLJE_zW563NTOHoRWrvqXuMbVMbdmMdyHvS8kXCAmcQFXSlmoBi6-pNts7-B8OxRAMKR8_SbCiDUiWufmB8ffj_Y06C2Jv5sugC4Mg7bomJDvYuZoe3AMTRjAn862M6p-sRMGxMP6ATy_un4f89jUwuVcztDoWmsh9ECS1d5BHB4tnS1tm9bw9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خبرنگار الجزیره: آژیرهای خطر در چندین منطقه اردن به صدا درآمدند
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/akhbarefori/668995" target="_blank">📅 14:30 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668994">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd2fb8a1ce.mp4?token=tmP68fDBHSdr2Z9LkWQQVax3FzueGTuFFoWVIQtgrj0dGVEONrVpzY7d0F26_3tQqgRmJAUXKsSMdM_yrLli1u8I130eIwtQGlNAM-K4IyJ-SLv0ZeH3G_Ris9niILNwQiV8TOVP1MjGCWFyxCmnBjbbAjgOLANsfvQALrR4Jq4snUeJurXTb_hWCHmoQe5noCsnuGDcsL_0sn0jOVtWz2XYDCYz7laox2rI1W-Z2FweZBsvjbCiky4oinNF2AN_r9XnyAd9wxjRi_Mlaxr6ZRBnn-Efb1ysmoo4dw8NxsuG-1KlkYbgsLlCV5CGao4QXozCbIPX0M6fRCBGbd5tOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd2fb8a1ce.mp4?token=tmP68fDBHSdr2Z9LkWQQVax3FzueGTuFFoWVIQtgrj0dGVEONrVpzY7d0F26_3tQqgRmJAUXKsSMdM_yrLli1u8I130eIwtQGlNAM-K4IyJ-SLv0ZeH3G_Ris9niILNwQiV8TOVP1MjGCWFyxCmnBjbbAjgOLANsfvQALrR4Jq4snUeJurXTb_hWCHmoQe5noCsnuGDcsL_0sn0jOVtWz2XYDCYz7laox2rI1W-Z2FweZBsvjbCiky4oinNF2AN_r9XnyAd9wxjRi_Mlaxr6ZRBnn-Efb1ysmoo4dw8NxsuG-1KlkYbgsLlCV5CGao4QXozCbIPX0M6fRCBGbd5tOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تاحالا مهمون ناخونده براتون اومده؟
🔹
شما تو همچین موقعیتی چیکار میکردین؟!
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/akhbarefori/668994" target="_blank">📅 14:29 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668993">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/96cd2cf2b2.mp4?token=QjAU2mJSoKu-PY8p-OzCzEChsQJ6DFNYHUb2IrrLPkYJno0b0ujyMmr8JKlXO5KAgluOgqBGsIdmIzeJmDHbu65QCICdk6Bog7EE-oPssqHzcghq7Xd-5LGfWZXV7kCVR8oEmAdXWIpESs4AaMJqCx0nScCSQ7YyRKYlUfMgbhjV1MYWB_dQ1HZ5uwxH7EwHvxkXufRwk17k1u-fb39XNHLdJB3liEg0RQyoJWHPfbN3qezz0-6s6xMu1zWS1tGHwBBWQSZmjBbkNBfsSHNFfCxYHDLxRWVXDONe_QMxy6rDkPabosFZsDtTyCLOfeNz3IEMrSeWAIBoKOkH4haoiw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/96cd2cf2b2.mp4?token=QjAU2mJSoKu-PY8p-OzCzEChsQJ6DFNYHUb2IrrLPkYJno0b0ujyMmr8JKlXO5KAgluOgqBGsIdmIzeJmDHbu65QCICdk6Bog7EE-oPssqHzcghq7Xd-5LGfWZXV7kCVR8oEmAdXWIpESs4AaMJqCx0nScCSQ7YyRKYlUfMgbhjV1MYWB_dQ1HZ5uwxH7EwHvxkXufRwk17k1u-fb39XNHLdJB3liEg0RQyoJWHPfbN3qezz0-6s6xMu1zWS1tGHwBBWQSZmjBbkNBfsSHNFfCxYHDLxRWVXDONe_QMxy6rDkPabosFZsDtTyCLOfeNz3IEMrSeWAIBoKOkH4haoiw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بعد از تو همه فرزند شهیدیم ای پدر امت
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/akhbarefori/668993" target="_blank">📅 14:24 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668992">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">♦️
شنیده‌شدن صدای چند انفجار در چغادک بوشهر
🔹
دقایقی پیش مردم شهر چغادک استان بوشهر صدای چند انفجار شنیدند؛ هنوز خبر رسمی در خصوص محل دقیق انفجارها مخابره نشده است./ فارس  #اخبار_بوشهر در فضای مجازی
👇
@Akhbarboushehr</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/akhbarefori/668992" target="_blank">📅 14:22 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668991">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">♦️
توقف موقت خدمات ۵ ایستگاه مترو در مشهد
شرکت بهره‌برداری قطارشهری مشهد:
🔹
به دلیل ازدحام جمعیت در مراسم تشییع، خدمات‌رسانی در ایستگاه‌های غدیر، پروین اعتصامی، هفده شهریور، بسیج و امام خمینی (ره) موقتاً متوقف شده است و پس از کاهش تراکم جمعیت، از سر گرفته خواهد شد.
#بدرقه_یار
#اخبار_مشهد
در فضای مجازی
👇
@Akhbarmashhad</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/akhbarefori/668991" target="_blank">📅 14:21 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668990">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">♦️
از هر رنگ و هر ملت؛ همه به اشتیاق و انتظار برای سلام آخر آمده‌اند
#بدرقه_یار
#اخبار_مشهد
در فضای مجازی
👇
@Akhbarmashhad</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/akhbarefori/668990" target="_blank">📅 14:20 · 18 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
