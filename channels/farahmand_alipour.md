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
<img src="https://cdn4.telesco.pe/file/uUxJ9gGeZ6LX1HvvPAm-cTD4AeK0qKxyah096SCivWFYVswq2vylJd3BaXnSxD7GAEMn1hGbzsLnj8FriXrpdSOpGpIkMeB_cXchHZG3WXrLb7loe7dfy_dg5KLVmkGcyHI-vq65mBnuTeDkdupxdaL19x0PqA-EFiTHnfsYNwOIywaqCcb3EwUY67p97iBulgTQ8zTKuSgy3VKS3-EPn4vBfzyZ1ZPenPKn4EstVQ-Xwuh-oaZK4bQmPlJYHtFcq36x3Tkn1fw6kRePIM_mz7U2nasa9SIrOn99mmEVtKe7Ygtzy2vC5IQBz_6jhUXGcYfkAtBfTV-lTW732rpryQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 62.7K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-06 00:32:49</div>
<hr>

<div class="tg-post" id="msg-5744">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BeNWpm9bbFk38cO1lTGgXNOYQ_QOviSlPty4SZU6QS2g0b8fvcXha_E-bagq0NJRe0FI2I2L2XAqBnaYxD0sjwdLZTzQ6xoxQ6GIj0nPXDS5Pz9jcKZvSiCWiXRRz2_M5NldE_bLKSrCrvBLj7KlVBTmv4y71_n1DHpYcceXA4rFMLNzdbGTgcCZyFrmdEcSMLTtNRujnAxxP99hv0LL_qgaaTQ2NkCfsofdFoTjz60xTt9eHirOhbc16hI6HW_IQ-rVVklh2l_IXLvtc0PH6nOfghiQPaDm1Jg8YdGRTJapcn20OYIjnp8cngz3D-uMMVDDuFPd7VSbX7P8aOp2wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 1.34K · <a href="https://t.me/farahmand_alipour/5744" target="_blank">📅 00:31 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5743">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FUkW-Dgj0r1t_OwcMzQ83GZ7OnbvrYhqXl8Q75bai4Trzc2vgBMuxqNi-Q9xkeLKKqDT3L7svJgTgeRiDLQBSsli3BZFHf7eV_qXvp0GKCuqnIZ5dwYQFZ7irqZk1R76t7Pqolvi31b_SWBThTcIYqSOoRIpx5j_AgVUK0cXRB30enQwTej-Q7tHykRLX-uEV76ePZJi9LnLxt88TBE4IcRi819HkLVPV73-K3JxHi7XFimbNkRx5lJUhWks1vPbQ5BKNAmPdtOR9oPNIZqCz31tABiosk9ouosCg00q-6ytYXTkHYDBMBapEcLeJR1xFvFcAOSUkMfEhbi_tiQj-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
حمله ارتش آمریکا به اطراف تنگه هرمز
‏فرماندهی مرکزی ایالات متحده (CENTCOM) اکنون تأیید کرده است که هواپیماها در اوایل امروز، 26 ژوئن، به تلافی حمله پهپادی دیروز ایران به یک کشتی تجاری در تنگه هرمز، حملاتی را علیه انبارهای موشک و پهپاد ایران و همچنین سایت‌های رادار ساحلی انجام داده‌اند.</div>
<div class="tg-footer">👁️ 3.01K · <a href="https://t.me/farahmand_alipour/5743" target="_blank">📅 00:27 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5742">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac9a1f1d75.mp4?token=nYdQIN6CTGG3-vJk6i8C67cN-mG626L1zv6-_dg6IAYINt-G6BfKl7UF-jSswsxgUXOS5C1F1MCcZ6pq5yDsVIBPPjlAatIANMQc_ifnmwd7OlF3eALwZja_vp08RbCuGYzcZpIaVv_svCtgwI3P_qvVE0DKspIJfItacKmGzWi0XtL73FR6GBmy1TL05-7b8jvPcNZO1AuCK58_u1lA-qmb7Hih9eoQ1b6e3HVx0ZzDT6_Njhn1PpjfzHvbOpDkN4LxQ7UBfB5MzRv1eVlFGzPrOC6eBQLh9ZYzUZK9ZcVHWdTveuqNnWfSuAxAwW12BpTrGv13-BXMh-gyIsv50r1K1vGBRQ8EvKOnTrvzX7oGwbMu0GWYuPY0MMMq7JRNSy7SaBce1HaK76u9hRde_GCH3YxRaoMMG9QHaXckdzdbY5A0CqGEHjXfALIMi9BtQFIFJwbeyxvP1lO6mKGkN_oc_fzgV4r6Z8DcSGOFppFopOtw6ewJ1lmsJl9WfLrUwFK9WmTRjhTh2qqtscpgL_IdnkAxU78X8P4lz-U2iB8B45bWuh0iLnMDEVHFS3AnM09OYchBKVInhEMRu9wfBdjRlnYb_aacH9pX9iftxgB3mBHjXWfCG0OkTIEufOSWpIK9ubE1CwfaqbYv4iL0gpp_ChdasJ45UTUcRFT73SA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac9a1f1d75.mp4?token=nYdQIN6CTGG3-vJk6i8C67cN-mG626L1zv6-_dg6IAYINt-G6BfKl7UF-jSswsxgUXOS5C1F1MCcZ6pq5yDsVIBPPjlAatIANMQc_ifnmwd7OlF3eALwZja_vp08RbCuGYzcZpIaVv_svCtgwI3P_qvVE0DKspIJfItacKmGzWi0XtL73FR6GBmy1TL05-7b8jvPcNZO1AuCK58_u1lA-qmb7Hih9eoQ1b6e3HVx0ZzDT6_Njhn1PpjfzHvbOpDkN4LxQ7UBfB5MzRv1eVlFGzPrOC6eBQLh9ZYzUZK9ZcVHWdTveuqNnWfSuAxAwW12BpTrGv13-BXMh-gyIsv50r1K1vGBRQ8EvKOnTrvzX7oGwbMu0GWYuPY0MMMq7JRNSy7SaBce1HaK76u9hRde_GCH3YxRaoMMG9QHaXckdzdbY5A0CqGEHjXfALIMi9BtQFIFJwbeyxvP1lO6mKGkN_oc_fzgV4r6Z8DcSGOFppFopOtw6ewJ1lmsJl9WfLrUwFK9WmTRjhTh2qqtscpgL_IdnkAxU78X8P4lz-U2iB8B45bWuh0iLnMDEVHFS3AnM09OYchBKVInhEMRu9wfBdjRlnYb_aacH9pX9iftxgB3mBHjXWfCG0OkTIEufOSWpIK9ubE1CwfaqbYv4iL0gpp_ChdasJ45UTUcRFT73SA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اگه خورده گرفتن که چرا میگید سگ هستید …</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/farahmand_alipour/5742" target="_blank">📅 19:53 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5741">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fad365bb7a.mp4?token=ZDr-STvQFPYHiROFw6OPE7okjr7IEHAwGcDfqUYyBg4k0-Dvk9qRQIKcE5xG2aewUJ912dVo_83a_jiYAwUcvSQphHICVJSnFHRCEsILiVyq2xA7qkuZr3bk5_ki9cNSYAuQW9RXOvqhjOSU2zL83IZYkxIZ15AIiPW56JRm1EuZ3RUKct9SeWjS-LFiZfgVlvHezTVkjslzw-S6Ybnjf4E8HQGRf9U2lczcyRXgE_g6QFYzHZV-PLIL5FT8yd0mL40Sp7E4N3lG-LybSPWDd_qpdQBnRXlbNlM4oOGZPr3XikHkTMJCVShwXA1Nnrb6TaFoTfgoL74RMT_P6d5E654wd_8E1jngQZqDbIcfh4AdSiQ_EDnb2WxAuS690KXSFcodRupdFggYwdKyArw0o8pGzZl47VWfX0zcB9MMZDQx_ybsm9a9TYVNbTkjwdFiDzkmtteDTZBsZpge8Yqrlfd38cfUSnn_XLOGgVAtwUs_G0j4wCialaTYYc8QLyT5qyOKtUagLBnyjykmehW9M48AYPaMXLJYbP1_aSUillMhLmu5Z7b4L9SA_H5l6xRzv5wn0rRrQElZwXcLXXb8sNwoJlDZqmak1lnJxHYuYLUnO4pBFG1rSyKICJLZMIOleuhrOmwPDO6BABjWg4UyATSItRoedZ4BGPS0uTxqWv8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fad365bb7a.mp4?token=ZDr-STvQFPYHiROFw6OPE7okjr7IEHAwGcDfqUYyBg4k0-Dvk9qRQIKcE5xG2aewUJ912dVo_83a_jiYAwUcvSQphHICVJSnFHRCEsILiVyq2xA7qkuZr3bk5_ki9cNSYAuQW9RXOvqhjOSU2zL83IZYkxIZ15AIiPW56JRm1EuZ3RUKct9SeWjS-LFiZfgVlvHezTVkjslzw-S6Ybnjf4E8HQGRf9U2lczcyRXgE_g6QFYzHZV-PLIL5FT8yd0mL40Sp7E4N3lG-LybSPWDd_qpdQBnRXlbNlM4oOGZPr3XikHkTMJCVShwXA1Nnrb6TaFoTfgoL74RMT_P6d5E654wd_8E1jngQZqDbIcfh4AdSiQ_EDnb2WxAuS690KXSFcodRupdFggYwdKyArw0o8pGzZl47VWfX0zcB9MMZDQx_ybsm9a9TYVNbTkjwdFiDzkmtteDTZBsZpge8Yqrlfd38cfUSnn_XLOGgVAtwUs_G0j4wCialaTYYc8QLyT5qyOKtUagLBnyjykmehW9M48AYPaMXLJYbP1_aSUillMhLmu5Z7b4L9SA_H5l6xRzv5wn0rRrQElZwXcLXXb8sNwoJlDZqmak1lnJxHYuYLUnO4pBFG1rSyKICJLZMIOleuhrOmwPDO6BABjWg4UyATSItRoedZ4BGPS0uTxqWv8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همین‌ها رو یک تلویزیون غربی پخش کنه، سریع میگن این برای اسلام هراسیه!</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/farahmand_alipour/5741" target="_blank">📅 19:50 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5740">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">ترامپ در شبکه «تروث سوشال»: «جمهوری اسلامی ایران دست‌کم چهار پهپاد انتحاری یک‌طرفه را به‌سوی کشتی‌هایی که از تنگه هرمز عبور می‌کردند، شلیک کرد. یکی از این پهپادها مستقیماً به عرشه بالایی یک کشتی باری بزرگ و بسیار گران‌قیمت برخورد کرد. کشتی آسیب دید، اما توانست به مسیر خود ادامه دهد.
ما سه پهپاد دیگر را سرنگون کردیم.
روشن است که این اقدام، نقض احمقانه توافق آتش‌بس ماست.»</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/farahmand_alipour/5740" target="_blank">📅 19:23 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5739">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/726fb491ae.mp4?token=Ez3NPON3BjUJQ0jrp96WZVY2iuSaUrdH7i5j2ZcM5OMDVRM8bmV5V5Z3LBadf7ptEpL-YxxhRcRrcTfnYyqVCnuakovZ-TFaKTPraD9DOOxzE7Lq03aXMpEokoygcgV5m75QELXbESB-loS2zQMnC8A6PUUJ9ujDU38LaIRUKWkGf_49-Ut0Ty6MpKZSG7xQh76xwE_LdVPBnyAlvDr77JeavqnECnXqx5szvsu0MPVUwUVDSZxKg-XMujLdLGPp8O4ebhL1wIlONmDBn6n-koUUq2_4CWbpBRu5Ook4jtuEwjWq3YNVBJlCZvvP3pIfPGUe6MJgFCV3yHECuke0kIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/726fb491ae.mp4?token=Ez3NPON3BjUJQ0jrp96WZVY2iuSaUrdH7i5j2ZcM5OMDVRM8bmV5V5Z3LBadf7ptEpL-YxxhRcRrcTfnYyqVCnuakovZ-TFaKTPraD9DOOxzE7Lq03aXMpEokoygcgV5m75QELXbESB-loS2zQMnC8A6PUUJ9ujDU38LaIRUKWkGf_49-Ut0Ty6MpKZSG7xQh76xwE_LdVPBnyAlvDr77JeavqnECnXqx5szvsu0MPVUwUVDSZxKg-XMujLdLGPp8O4ebhL1wIlONmDBn6n-koUUq2_4CWbpBRu5Ook4jtuEwjWq3YNVBJlCZvvP3pIfPGUe6MJgFCV3yHECuke0kIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قمه زنان امام حسین رو چرا می‌برید بیمارستان؟  بگید خودش شفا بده!</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/farahmand_alipour/5739" target="_blank">📅 19:16 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5738">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e184bbb012.mp4?token=WFZheY4bJthLfTsEnmlPwfkN3539xqkwoto4MSCzSkL-z1-xJXH78RVGxCdcRClgTvGYp3DF_Dg1ScWZshArOB40XwR947Di1K_26DbHusR1ACZG1_vTWyFgf7gv0KVqauI_LuVFw7aO-N79lL-dOmucPHrEI180l3MDtWBag-qKhcXgqvbiKZ7nDt_OdAWnSCotaJeey9kDCbIqEWIltToCJNTomthDY9CZX_AjJN1I4RCws5AkseQTI2B9hdfRkb0prAHTe0ehFQSCJ6oS3ZT2WGUAV3tkUSQMZgoZD7aB1JIt8_N_ddi9JcE9UFwAoXEc74C8mgGTBs9TPyGLpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e184bbb012.mp4?token=WFZheY4bJthLfTsEnmlPwfkN3539xqkwoto4MSCzSkL-z1-xJXH78RVGxCdcRClgTvGYp3DF_Dg1ScWZshArOB40XwR947Di1K_26DbHusR1ACZG1_vTWyFgf7gv0KVqauI_LuVFw7aO-N79lL-dOmucPHrEI180l3MDtWBag-qKhcXgqvbiKZ7nDt_OdAWnSCotaJeey9kDCbIqEWIltToCJNTomthDY9CZX_AjJN1I4RCws5AkseQTI2B9hdfRkb0prAHTe0ehFQSCJ6oS3ZT2WGUAV3tkUSQMZgoZD7aB1JIt8_N_ddi9JcE9UFwAoXEc74C8mgGTBs9TPyGLpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قمه زنان امام حسین رو چرا می‌برید بیمارستان؟
بگید خودش شفا بده!</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/farahmand_alipour/5738" target="_blank">📅 19:09 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5737">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K86q9Pgkmf-I0BvRjkhFAAeLnuBPT4wEALZQG9gRi2mIKotW_LU9oUFhz13Yg9wjUD67gGD-bXHrZ9cuLM6r9RUd6Y7wGSq-te_T0nixa-QyAPkCcQnARSM9irxQBQGR0k4FyxXamoTIpHDdvIQwI7TSLMxTnjCzTEVFe1sjW1hlJH2tTuCuTp4eMvr8cIcE1FjDF9VNNoQua8vcNToDKWvH0ZZihpe0AZZeIiuhwEmS94oNE9zYOBCIXPrGwMgWRqA9mGOtG-6_rRhUtwlRXQrmqPlC-lcGRDJdW9d4XU6oJ1oYKI7RJZ17n35LbMzsA5c5YIlrNzYacJ9dN4m9tQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیام فارسی وزیر دفاع اسرائیل خطاب به قاآنی فرمانده سپاه قدس
آماده‌ایم کار را به پایان برسانیم.</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/farahmand_alipour/5737" target="_blank">📅 17:53 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5736">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">نحوه اعلام خبر کشته شدن خامنه‌ای
و عدم تعطیلی مدارس</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/5736" target="_blank">📅 16:55 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5735">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qvv0oNieOKpjDD__S1oAM2RVzTuTnqVUIA5s65IBoptVQW67DBJvE-LvZSPzcaDgfLTor8bTn8HnzG46jbxuwYDjW73OcSgno5soLgqYPMW1xwYtmfn-NUEnsMpgjIa27LCJGSOA2guHFl-vxZy_nN-S6MpIQ3m_L8Pn4FcJi5Z5HpyVTNwQjJnMzDr6wYGutaPpcGLntFhJedDiyAgjZ7RN10K-2L8BIJSTb29K1a-vfjTfZ_mKlwKQAFqWOS9E5uup5Mt05_j25GTQiajTTRwODucgPumxji87EupCR-5GsZ02xisFy0zb18_stGn_oG6-H7wKT-N5-UsvP6hGMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آتش‌بسی که دولت لبنان و دولت آمریکا
به دست آورده بودند رو رد کردند،
اول ۳ پ در یک بیانیه و بعد حز‌بالله،
۳ هفته آتش‌بس رو انداختن عقب،
۵۰۹ نفر دیگه کشته شدن، از جمله ده‌ها کودک،
تا بگن «جمهوری اسلامی» این آتش‌بس
رو آورد! جمهوری اسلامی و زاده‌هاش،
اینطوری با خون مردم بازی میکنن!
اساسا چرا این جنگ رو شروع کردید که بعد رفتید دنبال آتش بس؟ برای خوانخواهی خامنه‌ای بود دیگه؟!
چرا بعدش افتادید به گدایی آتش‌بس؟؟
ادامه میدادید تا شکست و اخراج دشمن از خاک لبنان!
مگه الان ۲۰٪ خاک لبنان رو ندادید اسرائیل،
آتش بس چرا؟؟  آشغالا!</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farahmand_alipour/5735" target="_blank">📅 11:38 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5734">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vTlxXodelZAAUKeGl_CSolqihwb9i2RTgfHoj5F0PULg6_R1ps2Z55DfHD3yEQ6dQaqc0lEzOUmFLC_gejZzbBX7U4vITdlBcuWiLkhyA3AVQb7N_0PwToznCNI6AFDwsGHg53SHI8bekdkBXHoheGV_CU6H16uIPmJvJpvw8wjzwWwaqkBQgnGEKdHB9Rm-_KeYxmk1blfd14DROqikmnQOpwM1DRHXqAYR4NnowRwCsDkZZsMVS48SvsjAy7Xrued8ABhjjPFXm2lttdmCz1-gtqGqDa0QgeWVArkK_Z5ZQOkB7sT4ytXUjnHDdAxXtlqHqlZt5lzixl69-2pyQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر علوم جمهوری اسلامی  در ترکیه،
خامنه‌ای را از اولاد حسین عنوان کرد.</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/5734" target="_blank">📅 22:29 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5733">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YCbooH_h5rMr1jsmM99DYAG-HBv-xaw2c_9FRrELw__GaqzJrc1YnkKG5VuDUm6P5ChZ-V9zIiklEDwImH_QQbDB0rlw3WwCpHBb4woLC7E3eyxIVfFRJS_tWqzJvrv8FBpoCuMxZmQywnPuKU3fUju_LNRmDslASKsde8z1slhFXxNS_QkBFUCiFl84J36JOXFXAKsKYQiqGXF_GqfhTjmRlBUPze-DN_Tmkkn0KOWLBtimGXpJcd9_nPqyyf2qXD5UC_mlWyIgqHGnnmgQ1OKHxJiMZXUwPSTtC1ofldrgb5yRhwgswZafE6Y0Ag9mnWkZltelSh3rDEUgroy1Mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسرائیل به یک خودرو در نبطیه در جنوب لبنان حمله کرد و در نتیجه ۳ تن کشته شدند. مشخص نیست سرنشینان خودرو چه افرادی بودند.
صبح امروز هم در جنوب لبنان یک سرباز اسرائیلی در جریان حملات
حزب الله کشته شد.</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/5733" target="_blank">📅 18:23 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5732">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WM4D2xqXw920j5I9-sKCvfDDKU6t5AhNKkYatnKcd7tyoYkmaeUhgO78sK7G85vU6MyfGE8BOIsXHDeg42fETgvtpANYSdeRfsCn8aIjovbtBuQR8HtHxM5dEojSpN1o7PitmBb4xcOCJXXvNqO9m7jeLwjdONM4vhunTUzrmb6AVzRy2LWWYluO7LsaHMTdPz0fo0KwC2S7WOUqEFZNdTS8J3oEZ7hivBhokMESqW5Cw--Hs8IzErse1J7aHJv56ywILUBFGPnDBXQdh2voFwCwnuB3rB2gKAA97q3tdMur7CkOT-kNgipH2PJCECq_RYmAuZaTgShqZ2Cq1OP1Bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صد رحمت به اهل کوفه!
لااقل به دینارهای طلا فروختند!</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5732" target="_blank">📅 15:21 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5731">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIran International ایران اینترنشنال</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6715f87786.mp4?token=U0XYFEb8RKWLLwsMhqzQx6C2Y7QrZ3ewrFzFFqywQgi0fYG7bXsWKw3zACAka8z4of3-tU5fwa3K1tR9Gr_OKhusDRcRPhvW5MwMJY20V8EjSYM0M0BCw6fhZhwCkesv2mkE5ax1NEBkKjYY6qzgh_NxnSEUWwlWzcgT9yDaLXFxAEwuDaTin_TvtN2KIHZUDi7WwLu_yJ806xe9pdEWejsuEMTMN8ayhEUs_cPspEP6cwiibW6Oo5EnwXOsldvHr4e34CM-VER78ixik3sv_v1OFhiilCvGuZs6L7-t2q1MLbz3EOi8BTaR51karFkNREqWVfvndE1mNzrtukpsYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6715f87786.mp4?token=U0XYFEb8RKWLLwsMhqzQx6C2Y7QrZ3ewrFzFFqywQgi0fYG7bXsWKw3zACAka8z4of3-tU5fwa3K1tR9Gr_OKhusDRcRPhvW5MwMJY20V8EjSYM0M0BCw6fhZhwCkesv2mkE5ax1NEBkKjYY6qzgh_NxnSEUWwlWzcgT9yDaLXFxAEwuDaTin_TvtN2KIHZUDi7WwLu_yJ806xe9pdEWejsuEMTMN8ayhEUs_cPspEP6cwiibW6Oo5EnwXOsldvHr4e34CM-VER78ixik3sv_v1OFhiilCvGuZs6L7-t2q1MLbz3EOi8BTaR51karFkNREqWVfvndE1mNzrtukpsYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیوی ارسالی به ایران اینترنشنال نشان می‌دهد که صبح چهارم تیرماه در همایونشهر اصفهان پرچمی با نام‌ها و چهره‌های جاویدنامان انقلاب ملی ایرانیان برافراشته شد. بر اساس روایت رسیده، این اقدام «بدون ترس و با قدرت» در جریان مراسم مذهبی «عاشورا» انجام گرفت.</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/5731" target="_blank">📅 15:20 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5730">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/afaf9624af.mp4?token=iF2srjxcL4ZBsJCQ_7iGRxyRMVNN1_PZd42nPcbn3iJFyxQRyIxU3xYnN8x9-e9mSE3cJuw-KHn0cM6qoaoCDYByTpW6NRc1Btl0vsdKkfkmMGQpb_-E7uAd0Ct5cI7FFJfrJi8-FCCyoxVf6HJlV801rqZZp5-HvFRbJpDWnN_JW_HRz7uTkaOE9OfqYw3NyKF3Qi0CeG13GG1OE2X7fiXIGQ11U8VDptU7jtSOWweN0YD6rU-CmeYha0wop3LY6Ue91FitP_jZw9ULFwsS1BgaM6Yl1V8aIgLPqhRhGlZFtD6eXTOc90CaJwQmwX_ojzzvUWuiEjw7WJacY0YSGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/afaf9624af.mp4?token=iF2srjxcL4ZBsJCQ_7iGRxyRMVNN1_PZd42nPcbn3iJFyxQRyIxU3xYnN8x9-e9mSE3cJuw-KHn0cM6qoaoCDYByTpW6NRc1Btl0vsdKkfkmMGQpb_-E7uAd0Ct5cI7FFJfrJi8-FCCyoxVf6HJlV801rqZZp5-HvFRbJpDWnN_JW_HRz7uTkaOE9OfqYw3NyKF3Qi0CeG13GG1OE2X7fiXIGQ11U8VDptU7jtSOWweN0YD6rU-CmeYha0wop3LY6Ue91FitP_jZw9ULFwsS1BgaM6Yl1V8aIgLPqhRhGlZFtD6eXTOc90CaJwQmwX_ojzzvUWuiEjw7WJacY0YSGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گوشه‌ای از جنایت‌های دیماه جمهوری اسلامی</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/5730" target="_blank">📅 12:24 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5729">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">اینفلونسرهای عقب‌‌افتاده‌شون‌ میگردن توی دنیا تا سطل آشغال کشورهای دیگه رو نشون بدن  و بگن ببینید اینجا هم آشغال وجود داره! پس اگه کشور ما رو کلا آشغال گرفته و به زباله‌‌ دانی تبدیل شده، عالیه! عادیه! معمولیه!   مثل همین حمید معصومی نژاد  که دیروز براش نوشتم،…</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/5729" target="_blank">📅 12:00 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5728">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qf2U9OciURkkQQ4zhMA1HRxOYDfxslMk65LuYdzQ7-vVQIZOFyrZSIIiWgawnK9Vke5r2sGIEgwqsApX195Z0L70wc8L8AOfDfkbGQP1cVGAemytizh-yFFAv85cdw6d4vAo0jTtdMwfCbYgJA6Dkq_bwj6cwPIyCR2ww8zc34h6ZPg_zt-f4Et9rG-q6zlo6N4py_EuGkVhIjesN1DXbR1S5pvCujsm27167NF11oTjoUnhL0l2x-23kOQolPMqucMug1jvuILZmz_6Qvohpl68WCbepyk3ypttZns1xwPBvBWg7gvHiAjdB9LW5PZTy7rzAHLcgm_8MCaZqHOt_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینفلونسرهای عقب‌‌افتاده‌شون‌
میگردن توی دنیا تا سطل آشغال کشورهای دیگه رو نشون بدن  و بگن ببینید اینجا هم آشغال وجود داره!
پس اگه کشور ما رو کلا آشغال گرفته
و به زباله‌‌ دانی تبدیل شده، عالیه! عادیه! معمولیه!
مثل همین حمید معصومی نژاد
که دیروز براش نوشتم، میگه فلان مراسم
عزداری، توی چند روستا در جنوب ایتالیا انجام میشه! هر سال هم این موضوع رو یادآوری می‌کنه!  خب اهمیت این چند روستا چیه؟
پارلمان و حکومت و بودجه کشور و قوه قضاییه  نیروی انتظامی و قضات ایتالیا رو از این مجموعه و از این ‌افکار انتخاب میکنن؟
آموزش و دروس و دانشگاه و رسانه‌ها، دست اینهاست؟
از افکار این عده است که صنایع مد و فشن و خوردروی لوکس و ….. ایتالیا در اومده؟
یا از مناطق دیگه کشوره؟
توی اون مناطقی که موجب شدن ایتالیا قدرت‌ هفتم صنعتی جهان بشه و از مراکز مد و فشن،
اصلا این‌ افراد رو راه میدن؟ چی کاره‌ان؟
یه مشت عقب افتاده در حاشیه کشورن! هیچ کاره!</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/5728" target="_blank">📅 12:00 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5727">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🚨
یک سرباز اسرائیلی در جنوب لبنان کشته شد.</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/5727" target="_blank">📅 10:30 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5726">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/budDXemWSIQ7SkoDFzao16aXe1hInTtqIATa672agPsa9WF8EDsKLaGZV3l2WyzcdOnzy7lD-3AEzDARLU5DylmTGzy0xod2cYQUoVyaiEDygWz-aP4E3vtWkqMWNxQJMjnLh4M8a8tQhjNAa4Bv1ahYqY2UsYIJXOyQRJwyJ-kc9iYNaeAxPHkEf-9b9jhSA_aFjFd_9BNpDx0NOyB7h1peFf_j3XVoUfJM6YCCcfUQgKQ6TLuUAshceY4M24WeK_XLFURecglGtzjYh-FhsWLTeO-BGHNOc3_FHV_ke3Aq8JfdVy4vhfqBQWEuwqtDN5V_HvOy3tYY31T2d7gnSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرمانده گروه هکری «حنظله» که در جنگ ۴۰ روزه کشته شد، ولی خبرش الان منتشر شده.</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5726" target="_blank">📅 09:39 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5725">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/86c17f6d3c.mp4?token=bxCGtDSw4LewGVTwENXuEFF-CQJFAlEfeuZt5QtvpXsPXcxBIlXy6Fu-z4Tmj4DdJK9TFSfG7TXZB3xbV_PGWxdK6LSTQ8i_P-0J0xwI351dMFT2uZBK4JPqiJddq6X3C0FE3KHnynoWXPYE0bnb55dekzsA5wAmFlC-qy5Eeibgci4VGzoCyTQOnwTyeQruAkT2aYTdT9AS6FW9Bc7gyN1921-Cf9zqUhC1GzPVXw52gZ5zXmgGDy78t9mkAHvXvwyFuO9RHDqzCXgaUZLVllkIxHvLgCysIcj7ncJwjB8itQ-5Aryhn8GeMLagnmvM6_YriB4zz03EVc-D9TAzFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/86c17f6d3c.mp4?token=bxCGtDSw4LewGVTwENXuEFF-CQJFAlEfeuZt5QtvpXsPXcxBIlXy6Fu-z4Tmj4DdJK9TFSfG7TXZB3xbV_PGWxdK6LSTQ8i_P-0J0xwI351dMFT2uZBK4JPqiJddq6X3C0FE3KHnynoWXPYE0bnb55dekzsA5wAmFlC-qy5Eeibgci4VGzoCyTQOnwTyeQruAkT2aYTdT9AS6FW9Bc7gyN1921-Cf9zqUhC1GzPVXw52gZ5zXmgGDy78t9mkAHvXvwyFuO9RHDqzCXgaUZLVllkIxHvLgCysIcj7ncJwjB8itQ-5Aryhn8GeMLagnmvM6_YriB4zz03EVc-D9TAzFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ میگه جمهوری اسلامی خیلی رفتار خوبی داره با هر چیزی که من میخواستم موافقت کردن!
باید هم موافقت کنن و گرنه دوباره
برمیگردیم سراغشون!</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5725" target="_blank">📅 22:56 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5724">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">وحید اشتری، فعال رسانه‌ای حکومتی :
تنگه هرمز شبیه یک بومرنگ برگشت به صورت خود ما، در ۴۰ روز گذشته حتی یک بشکه نفت نفروختیم. از لحاظ نظامی توان شکست این محاصره را نداشتیم.
گقتم تنگه هرمز میشه تنگه احد براتون!
به هوای غنیمت گرفتید، ولی فهمیدید باید دو دستی خودتون پس بدید!</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/5724" target="_blank">📅 22:23 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5723">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/171eba79df.mp4?token=ow6l9ksUoGYZxnwQlVeafEhcH8479ExBpzIW7qUM2TIrMAybIWU3tUK6MnXctg1RksF3XHaZ8D7pkgpqvrKNCY8OqHepUU8zwNpAaABO6QkPCbfCLQV3yqv-W17RM9gN3NypC4rVeod5sn_e9qENYBrWWglah_VORY7RLQBHVwBf2uXKLbbb-Crgd4vfP6vbR7fPRS1aXwOV1GHZjMZl0XDlsrnAWyyexQqU3vyjYi8phBRJI54YM43XiWi0A0V_HwYz3CMBKlVULO1Z4RSERIWCRxkAJNEGiQiBvnA_yDY_drf9RSJ7WctWGdl3r1d4fRIaHpbgnJ2yDyC4Q4j0JA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/171eba79df.mp4?token=ow6l9ksUoGYZxnwQlVeafEhcH8479ExBpzIW7qUM2TIrMAybIWU3tUK6MnXctg1RksF3XHaZ8D7pkgpqvrKNCY8OqHepUU8zwNpAaABO6QkPCbfCLQV3yqv-W17RM9gN3NypC4rVeod5sn_e9qENYBrWWglah_VORY7RLQBHVwBf2uXKLbbb-Crgd4vfP6vbR7fPRS1aXwOV1GHZjMZl0XDlsrnAWyyexQqU3vyjYi8phBRJI54YM43XiWi0A0V_HwYz3CMBKlVULO1Z4RSERIWCRxkAJNEGiQiBvnA_yDY_drf9RSJ7WctWGdl3r1d4fRIaHpbgnJ2yDyC4Q4j0JA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قمه زنی گروه بزرگی از شیعیان در کربلا</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/5723" target="_blank">📅 21:46 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5721">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GsoFj93vZMXdyaGkA8Qc3isiCZafG3nKpjYOd-5sN9f1YVQz8n4sSeK0SKnSiARy5B_gOuxjpdts7Ja6OVtDqXFKOL31EdSZMbEbuUqdOE1clbnaNiziNv8toEglBzn2YGfllQY_xxJK15HHMtAI18CMpzUeXbz05BA9CLloGbC_WmKKiGRy4he9rWif_GVdAwB-ioS23OorHrjcuFPRe_c_JSlrXtK2_7-Ty319ps6Vc3HfuRxSeHBDJBGZOieGQjkYD8iZtGg5zgMFEvD3BqI_bqcIKk_qm5g_4XrMLmtHWYFc0KhyMJOGyrtUfKIUdUYOrzrSEfv3oxERyAyANQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تاکید مجدد ترامپ بر ذرت و سویای آمریکایی
و اینکه ج‌ا حق دریافت هیچ درآمدی از تنگه را ندارد.
ترامپ : ایران به ایالات متحده اطلاع داده است که برخلاف گزارش‌های دروغین و جنجال‌آفرین رسانه‌های جعلی، ایران نه از کشتی‌های عبوری از تنگه هرمز عوارضی مطالبه یا دریافت می‌کند،
نه هزینه بیمه‌ای و نه هیچ‌گونه مبلغ دیگری.
اگر این اطلاعات نادرست باشد،
مذاکرات فوراً متوقف خواهد شد!
🔺
همچنین، ایالات متحده هیچ پولی به ایران نداده و هیچ‌یک از دارایی‌های ایران را نیز برای در اختیار گذاشتن به آن‌ها آزاد نکرده است.
🔺
ما بخشی از پول‌های ایران را که کاملاً تحت کنترل ماست، در اختیار کشاورزان و دامداران آمریکایی قرار خواهیم داد تا با آن برای ایران ذرت، گندم،
سویا و محصولات دیگر خریداری شود.
🔺
ایران به‌شدت به مواد غذایی نیاز دارد و ما این مواد غذایی را برای آن‌ها،
منحصراً از ایالات متحده خریداری خواهیم کرد.</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5721" target="_blank">📅 15:52 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5719">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jcfzcMK7mDXhsHd_UDZpyo3xlEGuPC1iHSuO9BpG33lW2WfCLnrj_Sbj5CnXLeNWhM2KNqzPcikhezqmK7CO52-TPOxIbUt-jbuqT5GXtPMKsfkvDl0RvQ7VC06xgDf3VIo75UWWAZyKhp8a6My_ubuon-3Re7P93DAeJSBLnQieAlZRZ3RqTh5h54zWSx8vBXI6P_T3aLVhhOwFygWKRfsSzLWEPR_HnUDjFLJR6ru3XDBJKYVukUvDhfuMXwYnTsVYVnZtHSIxwUDIiRQfI2mFQ8i9DDGetOTv6_AK6ivX5QzACvqbRvAamDI-Zx45qNnZvSnDzszRqAdKCs23sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/W7X_h5eKAkMBTLRJ49vnXYGN2Rwwe2NLCOkY0m_kJ1DXVCord4aMVBrS5ERcakL0j3TlUBxUV0Acw-t_lxYDkKj1wZeP1Kh6i19bfqojGnaqamk7bJRESYQZGkJt4u-coPBZ1Ru4J1zAqFr7jEIVX1Ovz_sUo3nc6oEE3gByruaaKxI0FDGe2ckr48NgLQg5pIC257BPcYlRsj8gNNeoDt2dwuodiGwpqxLY3OK-QFuKPKJ4yoSnKg6dfmy0c1i6MJj2x9Enup1NP-nCkpxBiDpNH4NVksGmshHU7iUM7jUpgCbUtXwBYq-cBjHhVwo72ZtCKzMYS49kRDUwgGIX2A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دیروز تولد «آیدا عقیلی» بود
آیدا ۳۴ ساله بود که به دست جمهوری اسلامی و در جریان کشتار ۱۸-۱۹ دیماه به قتل رسید.</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/5719" target="_blank">📅 14:39 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5718">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">‏خبرنگار : اونا می‌گن هیچ بازدید برنامه‌ریزی‌شده‌ای برای بازرسان آژانس وجود نداره؟
‏ترامپ :
بلوف میزنن ، ۱۰۰٪ بازرسی رو ثبت و قطعی کردیم.
‏اگر راست می‌گفتن، همین الان مذاکرات رو لغو می‌کردم.</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5718" target="_blank">📅 23:27 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5717">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/975d16374b.mp4?token=ins0p_hRfkePiGy9acwVbkZd_rFqzc0tTMOTRo1U43Tb-IcwMQ3fAeP9kP230zfZH96whdGZgofXkyroUS0Yv-8vU7FaLu0Zp6danaujRLBtTyhXv-nMmfnV-O_ngB7NcWMhdQIUUJoN9h_iKY6D6HkC_GMPBYgAZIHzyxP8EdLPfv_UEN4oglO99VU-QqGBygO2vcd49lxPGmpve-mWhsZodsBJz3iTVyI9-K0fESH5fBDs6aQZ36eB4ggeEIyjaHctkOX2vQ5FJDFkksQqDkRbkPfoxPeTa6nUyq8ldQwyp63qfWNdiGNvkzObA2s8H4Ws-dfKeu59V-nBmh4ojA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/975d16374b.mp4?token=ins0p_hRfkePiGy9acwVbkZd_rFqzc0tTMOTRo1U43Tb-IcwMQ3fAeP9kP230zfZH96whdGZgofXkyroUS0Yv-8vU7FaLu0Zp6danaujRLBtTyhXv-nMmfnV-O_ngB7NcWMhdQIUUJoN9h_iKY6D6HkC_GMPBYgAZIHzyxP8EdLPfv_UEN4oglO99VU-QqGBygO2vcd49lxPGmpve-mWhsZodsBJz3iTVyI9-K0fESH5fBDs6aQZ36eB4ggeEIyjaHctkOX2vQ5FJDFkksQqDkRbkPfoxPeTa6nUyq8ldQwyp63qfWNdiGNvkzObA2s8H4Ws-dfKeu59V-nBmh4ojA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سیرک‌های جمهوری اسلامی</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/5717" target="_blank">📅 23:26 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5716">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xxqm79ep8VTQpqdsr2yZP6Z5P9_CsUN3IXPA2EB2sALV_XK2UjVzDJnAYtv0M5kUkptjNwfS_lkb57pEhvfkEVpKEY_cWDtjgxYmUQTJUIgrfY9V_Km5fzFMDKOjEseUDE6DGkXY9PqC8RfQEjQOAX_mpFe8MSiwmW_d2LLsZWfzxog3VW9RiwSMG4imYikHlQTf8Uv16I975t6Q65p21mgsayKzPWDMZ7jZcun8ry7aymOTUwuRlYd2jTJuyYkfdMFXCXoO27a11BQRoQk0rKK2n20yYtbxXku7qeT0vz8vi8D5bjRyQjIRl6TatmwsmNyH6RtdXiOja07riBs5oA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
شهباز شریف نخست‌وزیر پاکستان:
‏«مذاکرات شامل برنامه موشکی ایران نیز هست و آمریکا و جمهوری اسلامی ظرف ۶۰ روز آینده درباره برنامه موشک بالستیک و موضوع هسته‌ای گفتگو خواهند کرد»</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/5716" target="_blank">📅 19:00 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5715">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZDmGQUsjdnuee8oxmmcPzIE1iqeq0nHk5yAPdN3B8ZxXPQU13ALP2vu_DHzQcEaEZzjic9BpAIBGYXIrzWZXvdkBFLVBifkE1da0fVtRrkdwqAt6u8QnxZXd7P4XzalUwx2YBFzS5Tem-tm7MvamE5OBxFDdep9edF_Shaqc3cKeilT40LTBsxnXfZfw1C_dR43lJBAymPQBvFojFdgWnlYWgZLw-quZ6VjcGxR4iidfy2Y967BQtWjzYPeM_5fIJuLc_UCxUGEJI3XTsu7DyGE_8bse5zzg3eK6wiFVBmv0aJtVbuuAXLZRUkqxwtmIlz8u1DVZeQFDOJthJMLzoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/5715" target="_blank">📅 16:50 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5714">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">فکر کن رهبرت رو بدی و سویا و ذرت بگیری.</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/5714" target="_blank">📅 15:27 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5713">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nk4Fgnbd0evljIk3sLuW0XOzesvmpoe-mdWgZlnYpAGDdkb3qZ8zmpWlSf-47RaN2NZzxlbJN0Gu97re5WNprBZsu60S8aQqwIH7x9ngG2wDbsWXdmDVaYSlbAWcqkj1vFsqNSQ_WGXkncnTKGhXCstsk1LNrhlBAOmZ3u6a-c5zFiHr6SiqXVpMx58bPfOuNhujivrulEXXC19p0zl0grHBmCQMynn3DliKs0fR0FqRqKM0niTS4uT8-0YqOp3-uCg00CIR2RdKpHH7ZNhfduhKVHnOJaReEKFyF-JkvLQibCoPfEAaF5lA4uG5zf_rMKJQjBXzOAvpWf4EjGlGGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان ملل گزارش داده که در عملیات خون‌خواهی خامنه‌ای، توسط تروریست‌های حزب‌الله ،
۱۱ هزار ساختمان،  که میشه
۱۸ هزار واحد مسکونی کاملا ویران شده!
بیش از ۵ هزار واحد مسکونی
هم بالای ۵۰٪ آسیب دیدن!
هزینه‌ این عملیات قهرمانانه!  ۱.۳۸ میلیارد دلار بود
که قاعدتا باید از جیب مردم ایران
پرداخته بشه!
بیش از ۴ هزار نفر رو هم به کشتن دادن
از حمله حدود ۸۰۰ کودک! بیش از ۲۰٪ خاک لبنان رو هم دادند دست اسرائیل!
🔺
آمارهای این گزارش سازمان ملل، شامل ساختمان‌های ویران شده در یک ماه اخیر نمی‌شود!</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5713" target="_blank">📅 15:12 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5712">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">ترامپ :  با وجود اعتراض‌ها و ادعاهای خلاف واقع آن‌ها، ایران به‌طور کامل و قطعی پذیرفته است که در آینده‌ای بسیار طولانی ــ عملاً برای همیشه ــ تحت بالاترین سطح بازرسی‌های هسته‌ای قرار بگیرد.  این موضوع «صداقت هسته‌ای» را تضمین خواهد کرد. اگر آن‌ها با این شرط…</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/5712" target="_blank">📅 14:59 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5711">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MI_4CsDsFkn4f2M4SRQSKTRqGX6wM4yySvPKyIKl1rOg1G-ah9i0YRjSR2JiE6DQ36vdjqpO0g110J7pSatvNiyZJyHM5PtSI552xrmYbpGqnE_J8WUVJ7QsOQ9xI0XnlAHdXgSqZ0vMq5lgODCIupX14WyQv6bso_tgCv55v8K0t0K8oYZ6Z3vSB5EsOdNSSIyR09dOeF3On5XaLUkVOe3Oz6WXvnXIwiQRatOmQvamGGb4SrJyxDTXJ-HYD-wqFi0vysjKfSfGumlsBmUzg04Ftia_mVnUZyoGrldlNCrsMK1ajvN21-RJtfK3k1NFH-aDqTkxlctgfU_ubDhfZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ :
با وجود اعتراض‌ها و ادعاهای خلاف واقع آن‌ها،
ایران به‌طور کامل و قطعی پذیرفته است که در آینده‌ای بسیار طولانی ــ عملاً برای همیشه ــ تحت بالاترین سطح بازرسی‌های هسته‌ای قرار بگیرد.
این موضوع «صداقت هسته‌ای» را تضمین خواهد کرد. اگر آن‌ها با این شرط موافقت نمی‌کردند، دیگر هیچ مذاکره‌ای ادامه پیدا نمی‌کرد.
بر اساس این توافق و دیگر امتیازات بزرگی که ایران داده است، من موافقت کرده‌ام که تنگه هرمز باز بماند و محاصره دریایی دیگری اعمال نشود. با این حال، تمام کشتی‌های نظامی همچنان در محل باقی خواهند ماند تا در صورت لزوم، محاصره دوباره برقرار شود.</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/5711" target="_blank">📅 14:59 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5710">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c4fa249d98.mp4?token=U4CPlgGVFASMLSmFdrZayBV-wvNlylqAI9yI99h7GCRsh-2X8ieH1_JTWb5Rg7NRde7sdmRHNJqVXgunj9K4xxbBokPVUEwzqwfiGg0WPM_VgD9kS5dhb3USqcDiGGmF11A-Bf0s-vBJCiLawMvjtftmQQ-oj7jvZ1m072Lca6ACwt1GLEIK9JCraRrnLA2Uq-3vgUZtTKSLJY0u8Ko0Ul-uyrtbuF3Z7soke8_dfcnM6xW0yZM5h-Afc_DmHFIRIiLg_IhbwOjHWbImAS0gjgpMag1XOYDuwr6bKRPhtBY6F1XMPU8PGNYFJvOedjplqWw3I60T7DhPeSBAfIkWDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c4fa249d98.mp4?token=U4CPlgGVFASMLSmFdrZayBV-wvNlylqAI9yI99h7GCRsh-2X8ieH1_JTWb5Rg7NRde7sdmRHNJqVXgunj9K4xxbBokPVUEwzqwfiGg0WPM_VgD9kS5dhb3USqcDiGGmF11A-Bf0s-vBJCiLawMvjtftmQQ-oj7jvZ1m072Lca6ACwt1GLEIK9JCraRrnLA2Uq-3vgUZtTKSLJY0u8Ko0Ul-uyrtbuF3Z7soke8_dfcnM6xW0yZM5h-Afc_DmHFIRIiLg_IhbwOjHWbImAS0gjgpMag1XOYDuwr6bKRPhtBY6F1XMPU8PGNYFJvOedjplqWw3I60T7DhPeSBAfIkWDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار  شبکه «الجزیره» ، احمد ویشا
که دو روز پیش توسط  اسرائیل کشته شد</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/5710" target="_blank">📅 12:15 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5709">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UmjCk8rt3hIZMcIHFlhR74OqGX4Q9oTv0b01AeUB0au8kSV9C0sQsqdp4ndK6ta4-faphi6j8JiJtqUBolUGYWNeTs7mR02dUTocOLhvK0A2ZsRJrliy26CY5GNvxgH3ufvXHbWcDmkAYh0f3o-tPqvn4JLRsi-O_oBuxyiSG5IBqNuywKZFXGmlpl-ZnW2Su2NvibJTRrwThqDSE-tYXXMN_cjuMtGXDQ0hhGYqz5CKCeJdcynlSMYnOJics5ayF7qmhWVaG5EB4UCZmKzooAOAwjH-WCUO4JD62hKOZ3VeD5H6UI10zcpvuJl2UL_glgODS2g-RbB2OQnNWzJoiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حالا هم‌دیر نشده.
«شیخ نعیم قاسم» می‌تونه از اندوه پیجر‌ها و کشته شدن نصرالله و کشته شدن خامنه‌ای و کشته شدن ۴ هزار لبنانی در جریان خون‌خواهی خامنه‌ای، برای همه یک جا از غصه و اندوه بمیره!</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/5709" target="_blank">📅 12:12 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5708">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/siXDEWpQvAJfqp7-kSDtr9z0RkYvdN3KsTACXSAUm1wNzkZJaIh83sBVEX9Q9Lw0dk253VuUBpRPYEtaFOzatcPyiDSTzEQRMHL0AD5Aad2zvfmvBuaf01ALz2bK7iPmMFWRW3EHCu3MSKYmmpOLV0B6DbzrrNAyX3MFr3pBfljWpMuiozvU-V73khyoHKMLM3wqOoOSRxS61wkw7Vi2W_mZcyjmY5ZjDdo1_tx_X3hXyRIu9KzdY5TzycIKCOxQLDCp_kgfsBoO_rGZVj8A4WfbwuxMhbKhSvzm4xAAHvJtk_6BG5dlLn61XM7Qh0RGHyFCOE6LMV40R_C_jXmtiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فکر میکنید شیعیان افراطی فرقه جمهوری اسلامی  فقط با سنی‌ها دشمنی دارند؟  با یهودیان؟ با مسیحیان؟  حتی با شیعیان مذهبی که از فرقه خودشون نیستن هم مشکل دارند! تحملشون نمیکنن.  توی کربلا و نجف وقتی اونها رو می‌بینن دست به انواع کارها میزنن، تا براشون ایجاد مزاحمت…</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/5708" target="_blank">📅 11:43 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5706">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BkGQUUdlvywZvYXlWjtedRA1HWvzyBRI6GdP7lhBNTFyi5syaMpFEPAgNCWJYKV_qgnhg6hLgS3m1ajb4npHlTBJWOyJFcTLA0uwseqbeIfainZkbjgCR0yZ5fPT0DX8EYIEDNcL3kN41b9iQlJSW4aiaryhOxmtiF5oppN18F77XuhHMSthz-9GfOmfx8coZZQ7RyWxGx7C1c3SI-DBLYsbnOfHYs9mkB0Kr-FdxK8D5piO9Rv3nCv2F3DBtOe6hyMDsyYTysg_juLSRBJRo4_BHNmEIo1UvutefKBoCDkW7fVnGTCc-NHpM9BvJMV7e6Z4UDMmmbG4NT_e8Xm-rQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فکر میکنید شیعیان افراطی فرقه جمهوری اسلامی
فقط با سنی‌ها دشمنی دارند؟
با یهودیان؟ با مسیحیان؟
حتی با شیعیان مذهبی که از فرقه خودشون نیستن هم مشکل دارند! تحملشون نمیکنن.
توی کربلا و نجف وقتی اونها رو می‌بینن
دست به انواع کارها میزنن، تا براشون ایجاد مزاحمت کنن. با افتخار هم میگن
بیرونشون کردیم! انحصار طلب‌تر و افراطی‌تر
از این فرقه که با پول نفت و با پول مردم ایران
فربه و وقیح شدند، وجود نداره.</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/5706" target="_blank">📅 11:26 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5705">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c656e44d19.mp4?token=ZmKZjIZNNfQxA04lW2vF_IVdjoWQUtwJeA8n7OfHh9nXiEEft2wzEWY1dhIBidcvKKEjXQPeT7g3aYgTsDjV3DYJteUMaS1mSDGTEgEdMjBHIKsmz624ipq9Gu_mQLwWTrjfuV02eBjmCxwhwUGKlfHKlfV9uB3lO6jd4GtvJph1RIUG1I4JfC_ncDbNNobLZwa-X0Slj4t36el23aP7m0Ni1ov9Zwlx85o322vWGv2fHC1R6K7FxGeYHuL1PBjpCySkWswJnr4Fo71ZdhPKBjJ-yvCTrtqiqP5UVz9Jbii-C6kW1ThOCjHcBNefvnjhDPN-dfZ1g5mpqIhGyt5V2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c656e44d19.mp4?token=ZmKZjIZNNfQxA04lW2vF_IVdjoWQUtwJeA8n7OfHh9nXiEEft2wzEWY1dhIBidcvKKEjXQPeT7g3aYgTsDjV3DYJteUMaS1mSDGTEgEdMjBHIKsmz624ipq9Gu_mQLwWTrjfuV02eBjmCxwhwUGKlfHKlfV9uB3lO6jd4GtvJph1RIUG1I4JfC_ncDbNNobLZwa-X0Slj4t36el23aP7m0Ni1ov9Zwlx85o322vWGv2fHC1R6K7FxGeYHuL1PBjpCySkWswJnr4Fo71ZdhPKBjJ-yvCTrtqiqP5UVz9Jbii-C6kW1ThOCjHcBNefvnjhDPN-dfZ1g5mpqIhGyt5V2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تنگه مفتی مفتی گشاد شد</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/5705" target="_blank">📅 10:37 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5704">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa6e1aeb6b.mp4?token=GidVkojducuPEjkRIn_rV3gpPuVTpHRk5sDtzkv18ouZD1J39OP0LdODb_b6fFkrdvVUNAMpg1__V1liHvGjtNuDIYkQVZih94vtJbYOhUuuh8mIR03DNUM6MEBGFNaCMJsxYJ0StsEq_cpeZhBUANIaWSc7YYPRuBiANuk3r12YHsvGxEaKz8UFzRS75wjObrcyfeV2SDS04-s3LygtD091sXv_dGlzbhrOdP0fSIApPyx7sOZs2VRWg3CewZBQbthNToQZk_lw3MCEN9Rdwe6PqU8BGmlTEKRnLkdUNYf_JZpcifs2n8gq3J91CE95YgOIZNEntkzadJ8yfb7OvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa6e1aeb6b.mp4?token=GidVkojducuPEjkRIn_rV3gpPuVTpHRk5sDtzkv18ouZD1J39OP0LdODb_b6fFkrdvVUNAMpg1__V1liHvGjtNuDIYkQVZih94vtJbYOhUuuh8mIR03DNUM6MEBGFNaCMJsxYJ0StsEq_cpeZhBUANIaWSc7YYPRuBiANuk3r12YHsvGxEaKz8UFzRS75wjObrcyfeV2SDS04-s3LygtD091sXv_dGlzbhrOdP0fSIApPyx7sOZs2VRWg3CewZBQbthNToQZk_lw3MCEN9Rdwe6PqU8BGmlTEKRnLkdUNYf_JZpcifs2n8gq3J91CE95YgOIZNEntkzadJ8yfb7OvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏ترامپ:
‏اگر ایران به توافق خود پایبند نباشد یا رفتار مناسبی نداشته باشد، من کاری را که لازم باشد انجام خواهم داد.</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5704" target="_blank">📅 23:51 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5703">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">بیانیه مشترک نتانیاهو (نخست وزیر)، وزیر دفاع و رئیس ستاد ارتش اسراییل:
در لبنان خواهیم ماند و زیرساخت‌های تروریست‌ها را نابود خواهیم کرد.
🔺
از مهم‌ترین خواست‌های جمهوری اسلامی موضوع لبنان است و خروج ارتش اسرائیل و بازگشت شیعیان به جنوب لبنان.
🔺
وجود بیش از یک میلیون آواره شیعه، فشار سنگین اقتصادی و روانی بر جمهوری اسلامی در لبنان ایجاد کرده.</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5703" target="_blank">📅 23:42 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5702">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d53a76b465.mp4?token=BAEzjkmf0pyZy87M40frttsxKj8fMKPMVxjuXQSRsMbzgi_1KMfSB_5nZLX12mAr1QJNakwU86khlpmnN_ppbuTvTcGWBwI7H5M6bWIS09nV8RDH_lo1tddmSBrFH8ZkhXxvf3c9jygbg16K82gPhG0XippY7ScqXnoNLaHof7OfZm1u4BOjUKJ4NNDe5pLHIsmURDG0Lgc-gd4FCOs-isSn8QlYCADMN1JBGMDQ80CIsVGQ3BCR0TbdorHpZ0LgQLqH4MTCUM6I0VyGqMYUdn_gBK_WPavVtYM5MvBhd2UClDf-tvAg0ZGEaTckvT3JbJejeUAZgTZObukYnALNZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d53a76b465.mp4?token=BAEzjkmf0pyZy87M40frttsxKj8fMKPMVxjuXQSRsMbzgi_1KMfSB_5nZLX12mAr1QJNakwU86khlpmnN_ppbuTvTcGWBwI7H5M6bWIS09nV8RDH_lo1tddmSBrFH8ZkhXxvf3c9jygbg16K82gPhG0XippY7ScqXnoNLaHof7OfZm1u4BOjUKJ4NNDe5pLHIsmURDG0Lgc-gd4FCOs-isSn8QlYCADMN1JBGMDQ80CIsVGQ3BCR0TbdorHpZ0LgQLqH4MTCUM6I0VyGqMYUdn_gBK_WPavVtYM5MvBhd2UClDf-tvAg0ZGEaTckvT3JbJejeUAZgTZObukYnALNZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ : پولهای ایران  که قراره آزاد بشه
باید برای خرید مواد غذایی باشه
و فقط هم باید از محصولات کشاورزی
آمریکا باشه از کشاورزان آمریکا.</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5702" target="_blank">📅 23:39 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5701">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromRadioFarda</strong></div>
<div class="tg-text">🔸
گفته شده این آموزگار زن به جرم تدریس آنلاین به دختران و زنان که از آموزش محروم مانده‌اند، این‌گونه مجازات شده
🔸
براساس گزارش یوناما طالبان تنها در سه ماه نخست سال ۲۰۲۶ دست‌کم ۳۱۲ نفر، از جمله ۳۹ زن، را در ملأعام شلاق زده‌اند.
🔸
با آغاز سال تعلیمی جدید، ممنوعیت آموزش دختران بالاتر از صنف ششم وارد پنجمین سال متوالی شد.
🔸
آمار یونسکو اشاره می‌کند که حدود ۲.۲ میلیون دختر افغان از آموزش متوسطه و عالی محروم مانده‌اند.
🔸
زنان در افغانستان با محدودیت های چون اشتغال، سفر بدون محرم، پوشش، فعالیت‌های فرهنگی و ورزشی و غیره روبرو اند.
🔸
در پی بازداشت ده‌ها زن و دختر در هرات به اتهام رعایت نکردن پوشش مورد نظر طالبان، اعتراضاتی در ولسوالی انجیل شکل گرفت که به گفته یوناما با سرکوب خشونت‌آمیز مواجه شد و دست‌کم دو نفر کشته و بیش از ۲۰ نفر زخمی شدند.
@RadioFarda</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/5701" target="_blank">📅 20:57 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5700">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ns_2VDIG0rKObc3i74okN6vs2nCk21hsssvc-m6vdnfC3W3XlHAGTeQ66JBetU8W_Z9isNqlmh9_7qOtOFDI8KClUIFHO2QD02Ee2qUSSq34Q2AvSSgijg0Hssb0GOe3TUDIwzw8PRfZV_Fv0r9gpBloDXa5d32O3QvvfJw19J9EStPCjVo6hZLG7nztfrt4OUHdkYQMV0kB9xPJohJ0oaiBJyYtDNR8XjiYb6y48YEqsmXFXEToWvPcMsu39mr5TwNTQqzVAdghIhQGfW-zYWsJwWqMdUjjZtl_PgUNmSEixBtsVFaWQfbCY-LuEeJASPlOjB3s-nDd-K2C13zVXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این درآمدها هیچ وقت برای مردم ایران نبوده
هر جا پولی رد بشه، خودشون اونجا
قرارگاهی زدن و پول رو میزنن به جیب خودشون.</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/5700" target="_blank">📅 20:49 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5699">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rO_yeSp9thr-ZvX02vCLz6_3aT_m7wC_kvNB7P6Twe0luj4qgRCP3Z3pJRCnbytfMhOBGaYf1Gqwm5l1TuOHtuZ_06vxrXlKmbJCTPxHxl09TpJ9IzbGVeTxuqhW6WYdGnov41HIQHTx0cEkRefziwxbIc25Q7nRC9_HVf3mMx2w4bKSDOeUpYH4CsATMmdWjstYJDXuP7RoTskuVK9AMTmSpacJienJpBiav9DZnQd9pUfzZ9dWKAPdmdXX4Qr0WbpGDb245iy2rzzE-rOfgDVDEaLCJLP0jTEP0HW9dOxoXcd8SMuhI_R1hBeRK65c47W5ZKUm0dvVSR6J83_XhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
ترامپ  گفته برای راستی آزمایی
«صداقت هسته‌ای» ، جمهوری اسلامی
علاوه بر پذیرش بازرسان آژانس اتمی
باید با «بازرسی‌های تسلیحاتی»
هم موافقت کنه!
«همه کاملاً می‌دونن که جمهوری اسلامی با انجام بازرسی‌های گسترده تسلیحاتی موافقت خواهد کرد تا برای سال‌های طولانی از «صداقت هسته‌ای» اطمینان حاصل بشه.»</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/5699" target="_blank">📅 20:45 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5694">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dZ45V13WbGuPzzo1o8F9DqmbIv7jWKsFKU2YinqQF3g9ejq5VtZsiUFnM78ksx7VJm7wGwC5pPuKpRopqvySWNrS6T284GFOlRmeuyyO62tCeayhnxQrAz8ymaGltiok3zS2ToZDpH9X-ydEPe6AeoTYrcqG0N08H_ZZuA-snhx1Ztxm-aIoMZiUVmomk7ssjBB27GeXPltJaOSsqHuC7sOP50O0OFIRKN_kErnYM9fdkxvY5WMObZ1qExPF4uiggxr0Jaq-cCWcUN1q8MnWZVO1rAJHvnQmyrPf6PCKk30PWfb8wLaoBLuhdmFtBwWEzo1vA1z82_wAUh84An4Wng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Mm8o7a4-Laep0NT-mxWnbX6jIC0FIKvDwULgIGVqL62Azso8zTtR6tBrsUIe5ucbZiWg4m6W_ZtzSwaODXTsUaLdLSO3PwIyXU5Dls2xafX3oKMgWEhFxnDrHAbKRvlD6a-qutwPfuliEiyLNOMwPo3xSqtPqJI6faCUwGjI3yivtiVR0CqO9_VGMMoPh3gbW9rE-CIahUeIm39E1ZQujiJprUwmtwADqnbY3F2r3-92vdeKJbtqK9Anwu4v2jkyOocnfZaqAK-y4_5aLH4CI1shuh5BXUhChSuNKde5wvmS_TeyJmawb2b799xfnJ6IZvGWnu7xY4B3-w085TplaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ROkWNmG1sSf3RVCo-sfZPkh7NAB5wR1DtlYQ7nRJzcctgSKiweHBprDaRmXibrFE2g7XkkWcnuL0GDCDF9muhI5qgBYox2fjeEGlbBjiOP1huLCAHWIFOLF_kPsTQaHrl0JIgfF-uksDk5j1vrzdAgrCBco8Y_M3f0nKN1JMAjGoL2FuwpKV8PZMzcywRFjJ8ac8XjSfZbJE3ZLz_NMIoVFIayKeCKQvAow7oa_N7q9res5BmDoMlFg09aGTu-4WUJcIZ9iZgx48GpRTGb8flHX1Jy4Xoz6kbmekodFe3gGBSzK5-x5A8gIcgd1xsm_NHfu2fGCtvEdiu4fNLpz5Qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lMac-y3jkJ3UUxXEAp6vqmF-wqaHl78pLS8PMjqvHZI1omajcwT_TPbU8wTPJZgKX53MQ8rMDQq3pHi1UiDMHAA9NtjbcDAjU7EqBI53AAo7s9CFP0SBUn4Eoq9o474p0u5DFnOL7GocZ2NCL9tFTdvp1_AJetuUhFQGqVddBvC06nydP_Ra4wo2kneF6i0GfGhB4V6QR36a7SxDykgvhODgwIuZilossHY_WhdTNtDBggO080DsSB59jQhcQnnOCL2nEyjCWvvifLc2X_uTiZq2ib-VXcTpouGtDcK90BE9oYaCdp0fQPNjnH8HP7qs0qDkc4jcIdeODGPZmH4tuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vDhBFfnW8c255wCxXgTNv8aOFTytd3XKKN9FjSvfrd8XdpHJgIt_JPTWaGMGqXprGOJoUuoZndD2QWpeHQWn0d2fACW-6RfW738S7mKDMYprGxpDvW4gO9qio8lXrC1QIc6ClGWfZzKBPCYOepx9kYou5FccD9WQA62kAwmbSe6wIHLejxDEmQVeGWHYiVZmF6lqyR4aszf4gqZQM6pQEKdz6unoVI3xKanC0rN0Vmk1WU3o5awvhrhPoKEoxeO9i6aFpkYODXAzyCdidIToejZP_Z57li1UWnmWAhy1-ANm_PLQbDl9431pRqrL2ezVA3PCP85t5inGLgqmPCQ-ag.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">روایت یک جراح از سلاخی بی‌صدای سیستم درمان در روزهای جنگ</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5694" target="_blank">📅 20:03 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5693">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">‏بیانیه وزارت امور خارجه ج‌ا درباره نتایج مذاکرات با جی‌دی ونس:
‏ما یک واحد کنترل درگیری‌ها برای تثبیت خطوط جبهه در خاورمیانه، از جمله لبنان، ایجاد کرده‌ایم.
‏یک کانال ارتباطی اضطراری (هات‌لاین) ایجاد شده است که از طریق آن در صورت بروز مشکل در تنگه هرمز می‌توان با ایران تماس گرفت.
‏یک کارگروه درباره پرونده هسته‌ای تشکیل شده است که بلافاصله پس از اجرای کامل بند ۱۳ توافق توسط ایالات متحده، کار خود را آغاز خواهد کرد.
‏ما با قطر توافقی درباره آزادسازی دارایی‌های بلوکه‌شده ایران امضا کرده‌ایم.
‏ما اسنادی از ایالات متحده دریافت کرده‌ایم که به ما اجازه می‌دهد به مدت ۶۰ روز نفت، گاز و محصولات پتروشیمی را بدون تحریم به فروش برسانیم.»</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5693" target="_blank">📅 15:00 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5692">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">‏نورالدین الدغیر خبرنگار الجزیره در تهران درمورد نتایج مذاکرات سوئیس:
‏ایجاد سازوکاری نظارتی درباره لبنان با نام «واحد نظارت بر درگیری» با حضور لبنان، واشنگتن، قطر و ایران
‏· به‌منظور تضمین بازگشایی تدریجی تنگهٔ هرمز، مقرر شد خط ارتباطی مستقیم (خط داغ) برای مواقع بروز هرگونه مشکل ایجاد شود.
‏امضای یادداشت تفاهم میان ایران و قطر دربارهٔ اجرای آزادسازی دارایی‌های بلوکه‌شدهٔ ایران
‏· وزارت خزانه‌داری آمریکا (OFAC) معافیت‌های ۶۰ روزه برای نفت و پتروشیمی صادر کرد
‏· تشکیل سه کمیته (هسته‌ای، تحریم‌ها و نظارت) برای مذاکرات ۶۰ روزه/انتخاب</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5692" target="_blank">📅 12:38 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5691">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G4WS9WLjd_KNgJZDC708X4_wpwW785o34rTmquYOSYRLkQIcEVnPmFxN3Q8z3gQSQf5qxonbAYrLgfIPAmUEYNLfQM6-lE-XQrgIaPkrtaHhdaWyO7Xayajlg6dwKJGceVd0rQVRFI16ocC-8e1cFOoRfaLxx1yKiwqpdeVlWjreSh_oXle8CIBFD_vW8MuVCDthYLd8AN-5xX0pwJ6EI5puateLCVBeHNN07nTTnY1lbKWg67KsCFK6GF2iNKKqmIDPTEnAcOYo7rBNtdanq-gqI4a-JKzepLyLZFPcf6_LMKgE9XOKHuyjUD2w48p-ryYy5qDjHR-d-dkSgergqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ دوباره از ایتالیا انتقاد کرده
که چرا علیه حکومت جمهوری اسلامی
کنار ما نبودید.
این انتقادها و حرف‌ها  شاید ۲ ماه پیش،
۳ ماه پیش یک معنایی داشت!
حالا با اسرائیل که کنارت بود چی کار کردی؟
خودت که «ناوگان بزرگی» داریم!
و بزرگ‌ترین ارتش دنیا دستت بود
چی کار کردی؟ مارکو روبیو وزیر خارجه‌ات حتی صحبت هم نمیکنه!
که توی بازی‌ای که تو درست کردی آلوده نشه!
بی‌آبرو نشه!</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/5691" target="_blank">📅 00:01 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5690">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kor94COM7jCPmkvpQxIefDXSbwPzaZUEvoSS1Ap-UsliZObcit8myyk5yziXkK3FigMT2gD0vSEGV3CCs_-k3YAmIbcW_mM453-xwE9ASpE9sj3o3kcBlUGDV7VPgh-az7DnyT5Am1yWHUvrRqtya7fsydXiXUX7kCQf0-nvGlu95-B2l2mgfx-vOMH7FN-8mLZRiGyb9ggcDV6XtaujnvxDT7gKUKha5NW30ujGljzvS_GgpyHXzBFPkKyzRvxJkMaG9OCpptcCWRh6ACZMK4Qyj2UQ1JbJNQY2u6eKvdXT5XT00LgSj4vWbsCCsaSBA6GEYnPDHKISvMguObH_vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
گزارشی از شنیده شدن صدای یک انفجار قدرتمند در دوحه پایتخت قطر</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5690" target="_blank">📅 23:31 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5689">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🚨
گزارشی از شنیده شدن صدای یک انفجار قدرتمند در دوحه پایتخت قطر</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5689" target="_blank">📅 23:21 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5688">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DHPsUfZOedQwlrU6QFQ2tdPRrfEWjvfKAgWfE91VnldSaj7RvYW4_LRCwHtflUIgKacphoLm_IHCQqDjykDDrTIBpRsROG8F9GIKO858yWAbTJ4ndWlEAWIMi7AUgRpWRRN8RHA84cKgNOewRETMCDpczkIzLZ0_C5IRvy87IL7YW7njxOKW4PQBPEw8FceAGKIj4hsH3afEX6PYt-onRurSeCsAGMMzJFSoj4m9fzDdHxkqMtHCsWHtIpGyQIugGhSWVgWgjkGPA9JjgOW4SgEH16QLxCzgyV1dkjl7KzDdzOo-Tjz2UO7aYFXT5hFFTpqHfIXGDL-4qDAONNBOdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ورزشگاه لس‌آنجلس</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/5688" target="_blank">📅 22:55 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5687">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CiPZwCumoA1-F_udzKw-KW6cZeNUQxgrt01qzAoIEAAm65uwAbz0X6fg59qlnIUKkstL3h8YIH9svufgGIZzFL2clFsLo1rUpDniDczZX9EFgYJMkRnozLNYhl9rOeQVKHphpU5VH54MCofXwfZE3ack82G7JnIro0AkJHxC_5WiIXB4ZhibA-ziNeKV52jaU8kh89yp8NcX92YyFZ9Hk6WwWCK3ts12sSDUX8bDMIPJznRgMQYQdGRHLJyJZzOMdsV776eD6uBfRoqKtbhPbRBazicXkbjEfAEjnM29GivO9XQvhJFkfZU9k2kboPhXhUBVpMZj5lcm4pcKg6CvNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پاکستان و قطر از ترامپ خواستن
یک توییت بزنه تا دل شغال طرقبه راضی بشه.</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/5687" target="_blank">📅 22:43 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5686">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h5OrJo0fesEyo6wtf6fbsNnZXbuPqol5hKqBD0b9Y3RQTRBgB4nflbjuMH_o3Y4Vk7ghdnxx0stphnUvrtpMcKUyjygYSljhK2i1DOY1cy2gK128OW73aagUfkJ3GHlbUAbnb_lo2SNdtJbN14wN1HvorkJR_5Bt1gOLe9TnJI2OYJC56SmqDPR5MX3MAL-WIjGGxsz1SpGyYz17dpHXGphwqUZhmILk661qSIXLg4-iqVjZrhRdP_I_iziTU63F8JQdU3QxHhDq1LD35vYhfvzy4XC8FiCzUVOpgB_MtrHdfjnDoP8Mv_rzn-A5b9cy2LQdTGlj-13gEU2mFpQBjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جی دی ونس و امام قالیباف</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5686" target="_blank">📅 22:38 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5685">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cz9L3lejYCJAuVSOiBxEeWndGwa7Po7NDev8nXuoSL9W0qoLvU8xMRnIGtS8FitTmuWjz5wt4V0CAOhXgh-JC0rBKIWCiUZ2yJovL2J-1Jj6LB3_urozuduxBc_-qIrkNewtZLQwNuFhbSdQ9UAr4GaJokjhwIhTM5c-MVcq6NabTh6-OMmpHfX_-fZOuCtEns7ACbENumYuYMCrN9d-d2paMGNRz4cAz73VxbODndMjVQk2u9xTM72Nd-bCIO-ixGhDDyGwFj80KoofORf6J78gA1Ck1PDZu6exMkOU_JX98Nb6_25785RTz8tPH6S88790Fke7wtduWitYl9Vg9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش اسرائیل از حذف «زکی یوسف محمود ابومصطفی» از اعضای تروریست حماس خبر داد.
او در ۷ اکتبر به اسرائیل حمله کرد و از جمله «یاگیل یعقوب» ۱۲ ساله را ربود.</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5685" target="_blank">📅 21:50 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5684">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RN_LH4kPAvXQgu8Uxa8n7yW8XI7aJtm81owNvTG8CaS-CrLUjZvrjqnBTt_ItMef2WZTyeWTiCG1ZmH6Wew0wKb7yFrT_IrNU4kLqyLSWDfDF-iM_ibLsutGgGR7z2cpAMfbLKsENolgoejtlYPrqfGB-xEjfh55Xw_4WdNRuXaQ1RKS0kYzWhaEYIGf8iFDKGfZIwFw-joY7Rih7NOucKza_EaIT9d8X3JOwzP4PjUfDwrQNj9WXZiY7lXropB_0YULL6N2fkpfZs6ez0SUfN5fcO1Ghp7zGoy3wzx2YtkUgp-nuR76jkzdLsKl1NYC63aGI_g0IMURsXHLKJt2Lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فعلا درخواست یک توییت از ترامپ دادن</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/5684" target="_blank">📅 21:19 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5683">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🚨
برخلاف ادعای شبکه الجزیره ، هیئت جمهوری اسلامی محل مذاکرات رو ترک نکرده!
پس از آنکه ترامپ  مطلبی در تروث سوشال منتشر کرد و به سران جمهوری اسلامی گفت که باید دست از حمایت از گروه تروریستی حزب‌الله بردارند و گرنه شدیدا بمباران خواهید شد،
هئیت جمهوری اسلامی ناراحت شد و پاسخ داد و…. و شایعه شد که مذاکرات رو ترک کردن، ولی ترک نکردن!</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/5683" target="_blank">📅 20:54 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5682">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Eqz56kK_aXEJY955a3CtwuJ_GrPWCqdzlMBMXrOaG-9WYNuDFeA5Y7kv5nKKUp55KoQgACaLcboadLSSWR1G1f9IAT8X1gA1nu6JoWFlmPKEMlOF-PpoZsAgrVH6OrHmocUyrqAaUQtfdJolLOxo86c3CT3aQT4ZIFcMh2NcvhOGmr_FqdNqRNTS5zSE75O6uW2wO9UdGPZ-UU-eMq2vxZq9Fw_9C8ZRnV0eL3eFHdE4nhG94djlL6nXh8IxnJWEb9j4ehht8ETX5WIzuIX-C-5yrpBDmS95yLFpmeD9Y97dq1wchjs5oLdqGhp8IzO2r0oAjHvxxdNpKXGzhirE7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس ستاد کل ارتش اسرائیل امروز به جنوب لبنان رفت و دیداری با فرماندهان نیروهای اسرائیلی در جنوب لبنان داشت.
جنوب لبنان تا همین ۴ ماه پیش در کنترل نظامی اسرائیل نبود!
حزب‌الله برای انتقام خون خامنه‌ای ، دست به جنگ زد، ۴ هزار کشته داد، ۲۰٪ خاک لبنان را داد و حدود یک میلیون شیعه لبنانی، بیش از ۳ ماه است که آواره محلات مسیحی و سنی و… هستند.</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5682" target="_blank">📅 20:50 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5680">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca65ce2ecf.mp4?token=LQfO8fLxKgaXekxIMb3ChINPnZjsumQxEgeuLOcBpxgeqJdvc1BNS3uubaY_UjoYO6dRGqMyNdT-bsSTqTIUB0XTsZjdxYjxJgCikOJwIkhzMzBwDtAsbl_VOycjvYXxYYjIDWkcKXbso-0sMUqNLMz7zTTu5-wBaOzmsfAXUccvvh0k5_EfGjIAu8opKYXLFVyFqoPaOhskcEytIDfxgJ6x5AS2AeTmwkxxMvZ9TEmf9cxzL0v72I_QTCPLCzMOaTTCtXfZNgHPK7v1bV7YBF_UooWvWDfTIPRB1J66Vvidx6gt1L4CWq6i4Ak_F2FVdkGV7f6urs_m9RVxm4mY8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca65ce2ecf.mp4?token=LQfO8fLxKgaXekxIMb3ChINPnZjsumQxEgeuLOcBpxgeqJdvc1BNS3uubaY_UjoYO6dRGqMyNdT-bsSTqTIUB0XTsZjdxYjxJgCikOJwIkhzMzBwDtAsbl_VOycjvYXxYYjIDWkcKXbso-0sMUqNLMz7zTTu5-wBaOzmsfAXUccvvh0k5_EfGjIAu8opKYXLFVyFqoPaOhskcEytIDfxgJ6x5AS2AeTmwkxxMvZ9TEmf9cxzL0v72I_QTCPLCzMOaTTCtXfZNgHPK7v1bV7YBF_UooWvWDfTIPRB1J66Vvidx6gt1L4CWq6i4Ak_F2FVdkGV7f6urs_m9RVxm4mY8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همین شب‌ها:
یک مراسم عزاداری در‌جمهوری اسلامی
و یک عروسی در غزه</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/5680" target="_blank">📅 20:42 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5679">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZPRROlzHeLITNRKNuOHEsxeb6sWRBhe2bIbZuZ5nPn6JPEl9XGaVCnvw_QNJ5_gVA6S8Ca2GchoZYTIWEGBHS0cUwk9VjURt3TaXB5tbs_9qeRT1eVdAhybia5BlewFDbGoI-T6WNgiZsmKB49V69aa3lvr4aiiFJjOIq7mgPXyPPOkhlAS2qOjIQS15Wvs7KydmqtpjB1PPo9t5T9lUCJzDv5V2nrZF4o_TbH7W7KZH4bdboTmMGmX6TmOyEUfJFt3hrAExaBudWDrdNFkPxWJRlZ_xFDN1HvqVVUTpKHC10g6hZXDegDAA4uPJ9wsp0kGvRB9_8134jsc3-U3nww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینها رفته بودند مذاکره برای حل مشکل :)
در حالی که تا جمهوری اسلامی جمهوری اسلامی است، مشکلی حل نمیشه.</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/5679" target="_blank">📅 19:42 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5678">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd078eea01.mp4?token=fBGkS3omdQCmH0zgSMZ5B9C2J_icNtP6u2h_YUKJbUBUygd57xOoNo2MUBD84EmKE9MB5oB_pOAHvT0iaO4TMuq0V0x6VUsHlvkotfXauEUje2y56kFGuPF8vhSPCZp3dkpgGXkzRdO1iXxapP82xxVAgjZWlUQTovJC1JAiP7IYxzdqXC2xNa_h2nwRvLsUUkz_HVk8jGJ7QIkLhDCTLk3rXdRHLu_NGcX08xX0K2P3uOGaLDRV89BKyjwJZyT-5upfnkc7KCaZ1ZMGOuNr7rVocEKDQgYQ8MB24bGEo5LDIJboX_YsXKx9NfHjcyEd0KFQiKqeaQ2UrXTUaHqH9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd078eea01.mp4?token=fBGkS3omdQCmH0zgSMZ5B9C2J_icNtP6u2h_YUKJbUBUygd57xOoNo2MUBD84EmKE9MB5oB_pOAHvT0iaO4TMuq0V0x6VUsHlvkotfXauEUje2y56kFGuPF8vhSPCZp3dkpgGXkzRdO1iXxapP82xxVAgjZWlUQTovJC1JAiP7IYxzdqXC2xNa_h2nwRvLsUUkz_HVk8jGJ7QIkLhDCTLk3rXdRHLu_NGcX08xX0K2P3uOGaLDRV89BKyjwJZyT-5upfnkc7KCaZ1ZMGOuNr7rVocEKDQgYQ8MB24bGEo5LDIJboX_YsXKx9NfHjcyEd0KFQiKqeaQ2UrXTUaHqH9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">معاون رئیس جمهور  آمریکا،
نخست وزیر پاکستان و نخست وزیر قطر،
و خبرنگارها داخل سالن نشسته بودن، قالیباف و عراقچی گفته بودن
اول خبرنگارها رو بیرون کنید تا بعد ما بریم
کنار آمریکایی‌ها بشینیم!
مگه آمریکا چه نمایشی میخواست سرتون بیاره که گفتید اول خبرنگارها برن بیرون بعد سرمون بیارن؟؟</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/5678" target="_blank">📅 19:28 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5677">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b2464c582e.mp4?token=bZhajfFBTPkEGcLBh3-F_xQYu6CwasYSh-YChkaRJwTWU1jqJv5QcqtDf_bjfQDxGDXDXSC80L-tCCx3EX0ZXEjmvql2r-X2k59ttt3Z-tbRVmUHGwUhcJvxbTIeUH-7rIwOFZ8D0UnXCxe-BrAeh6NpngCJZkNTWHRvyIH6KgLMxwaSUEXBI4Pftdba0Wj5Cv31UE-fBBh7WZB6aykgjEGwmJm7B8bREX8_2nMXHz2WjAQ-Cijs4PfIhhIUUHC6IYzHmlpm-soq4105AsNpc3ZYAq5DsUN5VGtsxGOKJm9e2lcqB3D99H3DoYE1bjhYPoEXNK_Iz0xr9ldDcLs5tw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b2464c582e.mp4?token=bZhajfFBTPkEGcLBh3-F_xQYu6CwasYSh-YChkaRJwTWU1jqJv5QcqtDf_bjfQDxGDXDXSC80L-tCCx3EX0ZXEjmvql2r-X2k59ttt3Z-tbRVmUHGwUhcJvxbTIeUH-7rIwOFZ8D0UnXCxe-BrAeh6NpngCJZkNTWHRvyIH6KgLMxwaSUEXBI4Pftdba0Wj5Cv31UE-fBBh7WZB6aykgjEGwmJm7B8bREX8_2nMXHz2WjAQ-Cijs4PfIhhIUUHC6IYzHmlpm-soq4105AsNpc3ZYAq5DsUN5VGtsxGOKJm9e2lcqB3D99H3DoYE1bjhYPoEXNK_Iz0xr9ldDcLs5tw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دور اول مذاکرات به پایان رسید
شهباز شریف نخست وزیر پاکستان یه میز برای کنفرانس خبری و نشست آماده کرده بود که ج‌ا، آمریکا، پاکستان و قطر اونجا باشن،
وبی عراقچی گفت نمی‌تونیم اینجا باشیم!
و ننشست و رفت!</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/5677" target="_blank">📅 18:56 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5676">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nm1Wo-gu-JdVQAZN8wCNx-Dou7K1FeUuFVqw2uOIx13Dw3eqiMX-H2_inVxNRr5CMYVFYljAzH3hc9KwNbTmeJX3dD-NZnZ1doVDixbSszhB2REL09T5tV3ZOXSS0PiFuMgcDWbgMnJzIep6H8-As-Z2R4Yb7Jn84a_RMbIGac3eIy38YdPDu-UoPpie5d4M5C9h0HN6FI85SFmLXFjzKFXkhm0woo_ewQNXCgJJXVoRoEn3iTulaY2gVcfbDktU8b8KnTXyjLZrAGqeh1RmSW_7Jt-Aad2oo_zMGuJDHOr_dCBf3EHLFZgr8svR3dBWaVAP0pp8gBWyg8M8Z1X9-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/5676" target="_blank">📅 17:07 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5675">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7b14c3d6d.mp4?token=jSyKQt8V4kQb-TpEVM7SZi7DFvfcSqHrc3HoXKTRhgoYRvxU5gxqh1rNHtEbt6Ssb8WPiTGprLDSvMT6OViU-c8B7j7zPT9Md4p8etnyDF-Ty01REBYpZ2SY3h78MaDlSBhC50Bcs3zO6eOHdnxqq_HgVbepO9LRf_5DCSi2swvO5tK0P8cvlhVfg2VilvaFP_8JyK_lROGr-5JjBTxqWrElOeIsdfhQ6j8eDg-orML9Vvwk800UDblGsGVjEv9magsM45XZekWyab6voQ0aPJkBcjbpUaszuk73A27odYa2q7RCul-AnkYaRAd_eg5nJvI5n6OzmShocB-EnqAGMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7b14c3d6d.mp4?token=jSyKQt8V4kQb-TpEVM7SZi7DFvfcSqHrc3HoXKTRhgoYRvxU5gxqh1rNHtEbt6Ssb8WPiTGprLDSvMT6OViU-c8B7j7zPT9Md4p8etnyDF-Ty01REBYpZ2SY3h78MaDlSBhC50Bcs3zO6eOHdnxqq_HgVbepO9LRf_5DCSi2swvO5tK0P8cvlhVfg2VilvaFP_8JyK_lROGr-5JjBTxqWrElOeIsdfhQ6j8eDg-orML9Vvwk800UDblGsGVjEv9magsM45XZekWyab6voQ0aPJkBcjbpUaszuk73A27odYa2q7RCul-AnkYaRAd_eg5nJvI5n6OzmShocB-EnqAGMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جنایت‌های جمهوری اسلامی علیه مردم ایران</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5675" target="_blank">📅 16:58 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5674">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OqMM3JIqvW_2F8tkeqEECuTAhlcJMQzLB-LXRO489mZDJT2W6yBTIgIPZfJVquW04jjveAJgtafiMOgUrccXlKswoqkiJZPE87mQ7AJFEmXA3ch_LH8L82wHScZ2uABqWV-2Fdna-PKLo7PbO_CXYI8XgWJOx7v31p5Kj_VgqBthOlTNvrGz5nkNLpwK2x-Y3WEoE4KSys56g3FdGSvZYMAWrZmqUSH1QM6hxLowWWb1xR-r-DONrgujUuO3fyFbjxXnE8acDfqG2B_R3Ecr1aAcya2TNdvr-wUfQ4p750Faa09zA4oLf3j21jPuVWAcAhIAPqzH12uZJ8DbvZNBEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپِ کیسه دوز به فاکس‌نیوز:
«آمریکا می‌تونه به فرشته نگهبان تنگه هرمز تبدیل بشه و ۲۰ درصد از نفت عبوری رو برداره!!
اگه لازم باشه، ممکنه کنترل تنگه رو به دست بگیریم. آن‌ها رو به‌شدت بمباران و نابود می‌کنم.
اگه توافق نکنن، از کشتی‌های عبوری عوارض می‌گیریم.»</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/5674" target="_blank">📅 16:53 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5673">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jFe7obCVQO7MFSr7R5aNYAq-ONMmcdpdTC2NTXvGFftaOFQK-h7dPrOlwYmaG39sHVuDk7YhWm4TFwtGG8_GrUQLrxqJht2yXmL7fHHfh8RYZGWPhwhOJwZQKB3Y1WNh5_9rO4-ha98eERaeVdKY6Bex0l5V5QtZ0gUr6SZ6MtJA88YyuTnX09N8YOQaIa9ZCiRqXjgLSHm_omyQlT8D-1HnWSCTVNgCZN2WJChXLz5P2aJ5OwoLkuzh3atWFHlh2JL1KnKqoBJXuUMqkH6-UarEeG6qd5wtSQOq7DJHfOrXMamZ_zo4Hpgm57Gl1itHA87km91eIeVXe8VItZA92A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حامیان جمهوری اسلامی میگن همونطور که آمریکا به اسرائیل سالانه کمک میکنه،
ما هم به حزب‌الله کمک میکنیم.
امریکا سالانه ۳.۷ میلیارد دلار به اسرائیل کمک میکنه. این مبلغ میشه ۱.۴ درصد از بودجه ایالت نیویورک!!
بودجه ایالت نیویورک ۲۵۴ میلیارد دلاره!
میزان کمک آمریکا به اسرائیل میشه اندازه
۱.۱ درصد بودجه کالیفرنیا!
ولی حجم کمک جمهوری اسلامی به حزب الله میشه ۷ برابر بودجه استان خوزستان!
۱۲ برابر بودجه آذربایجان شرقی!</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5673" target="_blank">📅 12:55 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5672">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">جمهوری اسلامی سالی حدود یک میلیارد دلار به حزب‌الله پول میده،  در حالی که  بودجه استان خوزستان  امسال  ۱۴۲ میلیون دلار  بودجه استان سیستان و بلوچستان  ۱۲۶ میلیون دلار  و بودجه آذربایجان شرقی  ۸۴ میلیون دلاره.</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5672" target="_blank">📅 12:46 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5671">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qu6zsotdWKjrJ1OsdoJRZtC2Bdbe5PYwHr_DdnkdbwgggZ_qA8wtktT6aDxMAjLY85UT2_6Is0psthYU2hVNc9FBKoTiwNXf96EjEKdQ3rGRfS4pnmc4p5xj9MiEFaKZFA4AYfGOQlN7I15gXBFjPMkC44r9wb4OIfpTRndmVfTyhi-ntn65WapCksGBRJoEl3UMv5orQtKiLdVmwaiYo-QA4indFTgh9y23n4C7P16d6ibkrGmSOr1XQdmRfjDIVtcAXQ9rfz2CdbD_5CeU-8wPLFVyfIsmDMr8NEIESom1Mqfx0R_a1LkdY-vIlMWd50Q6AiW1avq5w7E9oHTZKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی سالی حدود یک میلیارد دلار به حزب‌الله پول میده،
در حالی که
بودجه استان خوزستان
امسال  ۱۴۲ میلیون دلار
بودجه استان سیستان و بلوچستان  ۱۲۶ میلیون دلار
و بودجه آذربایجان شرقی
۸۴ میلیون دلاره.</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5671" target="_blank">📅 12:42 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5670">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kx70xAloI9prr7qkvUZvwtcj2bsvJveKDl3ZhauDGM_tjVV9vW-ZCAri-ZOz6tg9GQkHNl3vGZDEPxxik2z-Ix5H_BQ0zjyo4uxAcwjiyMpnZKPVUmc72zL_rYWc_Kx0D2fFc8xRRmXSI5yrxDpio9RuLvpWHiBOfbRClXs1D_5-0VaiwILkSBM_s-_1fCJYB-3Ff2A7seRmSe5h7MycXbj6uZtzdhVGDiJpDKR7hUXJgdaubwqb7qgP3lLVRaDi1Af7M-RfHikU_mmN0LcM_DmdabqB1HhW_xQDMnb5zC_Z1WdWn3hEEkt74k2p95Cm7PNRGINBV9fFCVgN4VWxwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امروز - جاده منتهی به فرودگاه بیروت و تشکر از جمهوری اسلامی برای آتش‌بس در لبنان.
دولت لبنان و اسرائیل درست ۳ هفته پیش
یعنی در ۴ ژوئن به یک آتش بس رسیدند،
سپاه و حزب‌الله سریعا بیانیه دادند و مخالفت کردن! چون نمیخواستند دستاورد
دولت لبنان به حساب بیاد.
در این ۳ هفته ۵۴۱ لبنانی دیگر کشته شدند
و بالاخره پذیرفتند!
حزب الله پول و سلاحش رو از جمهوری اسلامی میگیره، نه از دولت لبنان، برای همین این دستاورد هم باید میرفت برای صاحب کارش!
به قیمت کشته شدن ۵۴۱ نفر بیشتر!</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/5670" target="_blank">📅 11:24 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5669">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/228de5708d.mp4?token=blbTtw9RR3eygEcLJ8psIlDayiSANwbU0pgdo7XsyYCFfEN8o14kUq42GvVP-usqiR1toTKeJmKnU-bldoZ1Z5L9_dTz17uFtABsvoXjAaFZgTSTizL1mcx6wewnHsa4Dm_RsfXUtb7b-ey3m8tHT9OHt9uIGcliXcXMnEfebw8eQ0NwCIxbvgu72Qfc6gqhSXHZBkSdS-6xSLHn9JDxx0PG-8EGmvBKXh1biHxfoELZild_dXRvNvglk44qHvIP66Bo7Vlsvq7Z9_6zahsVuZweD9YiRzzqSYx2WQAOjgUr3uj5u-W6rGvghbn32dJ1FMvGJL_mGtGBcuhcCMsIZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/228de5708d.mp4?token=blbTtw9RR3eygEcLJ8psIlDayiSANwbU0pgdo7XsyYCFfEN8o14kUq42GvVP-usqiR1toTKeJmKnU-bldoZ1Z5L9_dTz17uFtABsvoXjAaFZgTSTizL1mcx6wewnHsa4Dm_RsfXUtb7b-ey3m8tHT9OHt9uIGcliXcXMnEfebw8eQ0NwCIxbvgu72Qfc6gqhSXHZBkSdS-6xSLHn9JDxx0PG-8EGmvBKXh1biHxfoELZild_dXRvNvglk44qHvIP66Bo7Vlsvq7Z9_6zahsVuZweD9YiRzzqSYx2WQAOjgUr3uj5u-W6rGvghbn32dJ1FMvGJL_mGtGBcuhcCMsIZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در مظلومیت شیعه …</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/5669" target="_blank">📅 11:07 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5668">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd9d936798.mp4?token=eecpduPIF_A023LjjHNZsXh-ELXvGAugh8Bz9UqTMO6lU59LmiMUmajUGmBiALooUfHmlcpCgJ6qgtz2GpFoBXv1UJzOnYS61CQF_pHOjgZDetqDNAwuPYyd1ikJ53Gvl4Sinmr9_S95FpRW4Cp4itdQ3ScgO8Lp5B_rlNOc4GpQFQGlmhlDbfwrtyQdlQfrl_I-Y68FKLWG_OhjTRkjhe0sPFLX3--rfMPaJx36Yd4lQupw_NqcygpVe_yshDeR_TfuGAYxpBbi9_tT5N7-l8h7fxHTJZwFWdOChvnNKoOQcS3kD1JYakJ6r17nNawEczwOWZOZh_VAXMqO9bYOoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd9d936798.mp4?token=eecpduPIF_A023LjjHNZsXh-ELXvGAugh8Bz9UqTMO6lU59LmiMUmajUGmBiALooUfHmlcpCgJ6qgtz2GpFoBXv1UJzOnYS61CQF_pHOjgZDetqDNAwuPYyd1ikJ53Gvl4Sinmr9_S95FpRW4Cp4itdQ3ScgO8Lp5B_rlNOc4GpQFQGlmhlDbfwrtyQdlQfrl_I-Y68FKLWG_OhjTRkjhe0sPFLX3--rfMPaJx36Yd4lQupw_NqcygpVe_yshDeR_TfuGAYxpBbi9_tT5N7-l8h7fxHTJZwFWdOChvnNKoOQcS3kD1JYakJ6r17nNawEczwOWZOZh_VAXMqO9bYOoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عاخی … رهبرشون تنها و مظلومه!
یه چیزی درخواست داده که هیچ کدوم از سران ج‌ا، جز جلیلی! بهش رای نداده!</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/5668" target="_blank">📅 10:32 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5667">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ff3016eb3.mp4?token=gur8awAoENPHpsFNYiFAQBfShYeKXOndNmHb5cKXGuDwbQaX903mYP60EpTttHrNWnpX9WkVc7_QkCorLoNPFvgGOttquHZN9zegTel2RlqWNfjX31sSpmEhnqTRSgU8bLQkJafvoeL2wXAdH14InremYiwCxqfLgIfVIqT7jMhuKemZF6tkarEFdB9yrJHzvnBe7s-Er-ar5cBNnBeg2rbOJghSiAp8zJayD-mfV9nVU2VbPLQL1KtcdVthih4YpoSycVX0hqMGPaKdznwNfHLEZTa82tsOAG0_3xGqyhlkRKcUh_d4D1KafTcZ391aEASmSCkHtCPAdHUOMdNr5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ff3016eb3.mp4?token=gur8awAoENPHpsFNYiFAQBfShYeKXOndNmHb5cKXGuDwbQaX903mYP60EpTttHrNWnpX9WkVc7_QkCorLoNPFvgGOttquHZN9zegTel2RlqWNfjX31sSpmEhnqTRSgU8bLQkJafvoeL2wXAdH14InremYiwCxqfLgIfVIqT7jMhuKemZF6tkarEFdB9yrJHzvnBe7s-Er-ar5cBNnBeg2rbOJghSiAp8zJayD-mfV9nVU2VbPLQL1KtcdVthih4YpoSycVX0hqMGPaKdznwNfHLEZTa82tsOAG0_3xGqyhlkRKcUh_d4D1KafTcZ391aEASmSCkHtCPAdHUOMdNr5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به رغم آتش‌بس دیروز
شب گذشته ارتش اسرائیل توانست
کوه «علی‌ طاهر» در اطراف  «نبطیه»
را تحت تسلط خود در بیاورد.
در زیر این کوه جمهوری اسلامی شبکه‌ای گسترده از تونل‌ها ایجاد کرده بود، هم برای انبار کردن موشک و اسلحه، هم برای حمله
به شمال اسرائیل و هم اینکه یک مقر فرماندهی و پناهگاه امن برای نیروهای تروریست‌های حزب‌الله بود.
ارتش اسرائیل تخمین میزند که هم اینک در این تونل‌ها، ده‌ها، با شاید صدها نیروی حزب‌الله گیر افتاده باشند.</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/5667" target="_blank">📅 10:30 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5664">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd300c19c9.mp4?token=p19QG5NYlBB1P5exWWxvVcuRmj7JfvM1EhkFfP8WjUGkh4-mWz4J3kAn0QsFfELXi_pdQImq9Zh1W1qlR5NbxYjQrBNJmDeSPqeA2rWFT5OgQjGQsOIuc7ABu8cltM4NjUz6m3q0ncugbQ0jpomHDnzqb0UiRu1z8H0ji7Cc1DuxnlyZHaS8Q95y6vUtDHHhmAUiG_rDG_PpGwRdYaEuyF8_zSYHi67w6SkiPa6OqSvnake1sJqRvnz4hVjteBQ3jVlvATGsCgRSJIsES6xkSUDmO7I0mXRqWLv5PukNuu1KbbegI1E6Z9hHQ0H3A_pr6OFTBZtS_TFD8xmKiSAC4X-OhzBtornTwY6LOGf6Xtg_bmRV-w6NkZcvTB6QqsAkD5jNznNAG5_Mdxsd6WvTLWbAu72XRkQEjCkHZ1z-utVNwhK-6riuLRNDlJP-SCrEDWpGqmuWpB4em_OccD9hfT0uoesDZQiziI93ZmUkBxb1JDycgwwPYan_bJEn-DR-yK3Z0B5vCs0nirJUTkow_nrYfceo8mjZXObQxtcDQtmbGyyWitzmA9XnnfO4blcrw15i2GnozPIbsvHDFSup4I549geaUdMLSMSwM_F6eY_hvN7zmmDKA0sY824Wa27-WOEGrJiQ9L6OdFX0JAkStYU6vnYut5bQiw98HQuIgZk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd300c19c9.mp4?token=p19QG5NYlBB1P5exWWxvVcuRmj7JfvM1EhkFfP8WjUGkh4-mWz4J3kAn0QsFfELXi_pdQImq9Zh1W1qlR5NbxYjQrBNJmDeSPqeA2rWFT5OgQjGQsOIuc7ABu8cltM4NjUz6m3q0ncugbQ0jpomHDnzqb0UiRu1z8H0ji7Cc1DuxnlyZHaS8Q95y6vUtDHHhmAUiG_rDG_PpGwRdYaEuyF8_zSYHi67w6SkiPa6OqSvnake1sJqRvnz4hVjteBQ3jVlvATGsCgRSJIsES6xkSUDmO7I0mXRqWLv5PukNuu1KbbegI1E6Z9hHQ0H3A_pr6OFTBZtS_TFD8xmKiSAC4X-OhzBtornTwY6LOGf6Xtg_bmRV-w6NkZcvTB6QqsAkD5jNznNAG5_Mdxsd6WvTLWbAu72XRkQEjCkHZ1z-utVNwhK-6riuLRNDlJP-SCrEDWpGqmuWpB4em_OccD9hfT0uoesDZQiziI93ZmUkBxb1JDycgwwPYan_bJEn-DR-yK3Z0B5vCs0nirJUTkow_nrYfceo8mjZXObQxtcDQtmbGyyWitzmA9XnnfO4blcrw15i2GnozPIbsvHDFSup4I549geaUdMLSMSwM_F6eY_hvN7zmmDKA0sY824Wa27-WOEGrJiQ9L6OdFX0JAkStYU6vnYut5bQiw98HQuIgZk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از دوربین جنایتکاران جمهوری اسلامی
قتل‌عام مردم ایران در شب‌های خونین ۱۸-۱۹ دیماه</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5664" target="_blank">📅 10:05 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5663">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/845f6aff27.mp4?token=W-SWEJWZNoUCp5kU2CBUO2XuGn_NyK1tSmtFeE7gLc8Mqk4czDZAz9CC6bvOeCZnC3iHnPqf4DSJKLepsCRbIdppE18MIYN4qTucV6jRNp8W-qDCEFmhsHhoixHPQaH0sEc54Of_Dh6lZhk_N9ID2nv885YiQ7f6D9P7db4e5Xcsj9riSYqw0aBp_PN34Xa6_QJfvROiheCqIB_LKnOwXNgQyjWHaus9gOAlg_eQob16BJsQhtxZw9xFKYUW_5J5bGFY0zEOp-Dv2rHr0DuEOclcdj3E7Yu_NwI59JmFxM6mLhFhmwu1jOiaQajUew51A1L3A4MKjAlzqPQzvJRQkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/845f6aff27.mp4?token=W-SWEJWZNoUCp5kU2CBUO2XuGn_NyK1tSmtFeE7gLc8Mqk4czDZAz9CC6bvOeCZnC3iHnPqf4DSJKLepsCRbIdppE18MIYN4qTucV6jRNp8W-qDCEFmhsHhoixHPQaH0sEc54Of_Dh6lZhk_N9ID2nv885YiQ7f6D9P7db4e5Xcsj9riSYqw0aBp_PN34Xa6_QJfvROiheCqIB_LKnOwXNgQyjWHaus9gOAlg_eQob16BJsQhtxZw9xFKYUW_5J5bGFY0zEOp-Dv2rHr0DuEOclcdj3E7Yu_NwI59JmFxM6mLhFhmwu1jOiaQajUew51A1L3A4MKjAlzqPQzvJRQkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمزه صفوی
فرزند مشاور ارشد خامنه‌ای :
در ۴۰ سال گذشته جمهوری اسلامی همواره سودای ساخت بمب هسته‌ای رو داشته و تمام تلاشش رو کرده. اما برنامه‌هاش لو رفتن!
جمهوری اسلامی پنهانی دو سایت «فردو» و «نطنز» رو پنهانی داشت جلو می‌برد که «لو» رفتن!</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5663" target="_blank">📅 09:51 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5661">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f28d8f2fab.mp4?token=T54aOLSmZk5qy4e1ZGAZa18l7ZdwJZGpzHEvYtXPRx-7QF7-tC06OghUr2sj_2Z809xn58z0cyM2sD1pvtMpc9HYBm32Qx93ONyOStqJS68fdvxds7qWC2cXpjkL3S9pG_Ixqdizp6j2VEUMPYI4ubp3tdB23LtHkwb2eTzWNlmiDdunqz7fi5khS_OWcY6Cwwzq16K1fqiFXBRUTiysg68oXLNsL3_0a1cF2s9DepCxsZoj5JQKpQGJ7u8vDyy3V7r1SEuUdVZx8GlaYqLaGXcsrG9uuepu4lBmB-6dYDXUWNJyiR4SE5AX5X7mR8zkMP3RKJK69qB41KQRrHHUKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f28d8f2fab.mp4?token=T54aOLSmZk5qy4e1ZGAZa18l7ZdwJZGpzHEvYtXPRx-7QF7-tC06OghUr2sj_2Z809xn58z0cyM2sD1pvtMpc9HYBm32Qx93ONyOStqJS68fdvxds7qWC2cXpjkL3S9pG_Ixqdizp6j2VEUMPYI4ubp3tdB23LtHkwb2eTzWNlmiDdunqz7fi5khS_OWcY6Cwwzq16K1fqiFXBRUTiysg68oXLNsL3_0a1cF2s9DepCxsZoj5JQKpQGJ7u8vDyy3V7r1SEuUdVZx8GlaYqLaGXcsrG9uuepu4lBmB-6dYDXUWNJyiR4SE5AX5X7mR8zkMP3RKJK69qB41KQRrHHUKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5661" target="_blank">📅 23:07 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5660">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eBJtqqF31dzl_dJ_iQw67gYEKWzdVLe8oVm4INdyPCCVSWUvH32XscWPBGzkRfp1DIIM1-Rut4Mi1q0Cep0OtcDEsXRABh23RpCGc-03rtNgMPiL0a62qvyUw7cKcMY1J1awjJsdg6BvqgLgazTUSvZYua8bQMJNJjvHdbGtMeB9zx2Fcd0Jnd_ovrsAH7HeMdi05eqyr8Kgn20AXRcuVCzKlA9plosKLIlYg2uKfXJaiRC4Nez3QZjKTNw729adgL5UiREaEoYL6Nnv1KpQoO-X7D1eI_j4HSj0XGc8jH7yfe_fSN0uBTFD-GjzrfxX-prnlzYm_5y8Af1xiuuymg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/5660" target="_blank">📅 23:07 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5659">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9adbaa46b5.mp4?token=SapNbazB0an5En6VK53Vercjm3xNEcJWYyj7tlu68bZ1yXtrk2aWhSpw74A_-0R5XqH1bMj_OtnZAwhII77IJlH1yZVhhlB1Eh0GX3up6H75ormpDqGzoqIemR5ZRoFUVKNN2RZEe18puJpBmTeNY95OTKQDuhZi81cqElLGVTEQOwnT42FuXm0HPIHd07uqbcr-i2IbHyxAm1MCUrIeIqR6-lWBtA-DbTiMa8Rje1XXygHi0s--fL6AJYnyPQGEKGfa2l1BLBFvqS5ag0mZJ0ibvwoiJQQj_T7quX3h5PlSKisRaTaEMUN3gaPk9R_Ne4I8CRovDpTKRjmlppk2BQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9adbaa46b5.mp4?token=SapNbazB0an5En6VK53Vercjm3xNEcJWYyj7tlu68bZ1yXtrk2aWhSpw74A_-0R5XqH1bMj_OtnZAwhII77IJlH1yZVhhlB1Eh0GX3up6H75ormpDqGzoqIemR5ZRoFUVKNN2RZEe18puJpBmTeNY95OTKQDuhZi81cqElLGVTEQOwnT42FuXm0HPIHd07uqbcr-i2IbHyxAm1MCUrIeIqR6-lWBtA-DbTiMa8Rje1XXygHi0s--fL6AJYnyPQGEKGfa2l1BLBFvqS5ag0mZJ0ibvwoiJQQj_T7quX3h5PlSKisRaTaEMUN3gaPk9R_Ne4I8CRovDpTKRjmlppk2BQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">غزه</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5659" target="_blank">📅 22:34 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5658">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/goxuXE9T6o_N10nhckBhICqdsKKJXczDu3RlX7OytoTxd3Sk3RUKVMvIRJ1fmSAYBbJ-E1bNUHsjxJGynAbj35irGbwVBdMZmf0sH2DsX86uBxXAkxwqNs4HLZu_W04fs4AaGye23a2eTCIKYkFPUt_EqCIexc1QX3YATRS2Sx2t0XhDof6WkYX_1zXw0sm7cx-vcqj4MnMpu34i3OkB8N4hvQag7K2OaCxcCeCeXziKEKKiIGR6m9GBjT7-I9jjQSx8HuYnx1MjgzNgiF8M-Jxxx-EU_KCkbNt5AMvH10bFoq0TpvvRuGuCp4mXw1EZnmjU-AqJ3d9RBxP_nn6UKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش اسرائیل حملات را متوقف کرد
ولی اعلام کرد از مناطق تحت کنترلش در جنوب  لبنان بیرون نخواهد رفت.</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5658" target="_blank">📅 18:43 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5657">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZA7F3WJdAiQWWzznZsp--VM7Q3048SXZBZbknmJY1U6VFjcn97GakO1dxu-ANZUk6zGJQc77MD3yuYJlMc0jhgsqyHDExBRTHBnwsTOfwIIIqygNS-cktqw2nUrcBB1zRa53apdmQLCjfeNHn9LNveGWm0CSMv2ovfX6bvOeU3CmzM5sRNdUFN0cHrJqo35F3dPqFBPWPfQ_h28oN0q__lQFXoSOVFZBeE03AS_BaIiA1ach-Chygut1C0_FXsY2JR6ulXjzlTm2zCQakdHSrFidOBvyTSAZoKo7wZ576UQih84n79b9Qr_VrGEMbowzVyZbwpNTxVOPTuN_M9uyZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در واکنش به جمهوری اسلامی :
فرماندهی مرکزی آمریکا، سنتکام،   بسته‌شدن تنگه هرمز را رد کرد.
سنتکام : تا الان ۵۵ کشتی تجاری با محموله‌ای معادل ۱۷ میلیون بشکه نفت از تنگه عبور کرده‌اند و نیروی دریایی آمریکا هم در منطقه حضور دارد تا مطمئن شود این مسیر همچنان باز می‌ماند.</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5657" target="_blank">📅 18:14 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5656">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">جی‌دی ونس در خصوص لبنان:
من فقط می‌خوام به مسیحیان لبنان بگم: ایمان‌تون به عیسی مسیح رو حفظ کنید و بدونید که در دولت ایالات متحده دوستان خوب زیادی دارید که برای برقراری صلح در منطقه تلاش می‌کنن.
مشکل اساسی مسیحیان لبنان، یا دلیل خشونتی که باهاش روبه‌رو هستن، اینه که حزب‌الله، به‌عنوان یک سازمان تروریستی، عملاً در لبنان مستقر شده و اونجا رو پایگاه خودش کرده. گاهی از خاک لبنان به اسرائیل حمله می‌کنه و طبیعتاً اسرائیل هم در دفاع از خودش پاسخ می‌ده. به همین دلیل، یک درگیری دائمی و فرسایشی ادامه پیدا می‌کنه</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5656" target="_blank">📅 17:19 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5655">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🚨
🚨
🚨
جمهوری اسلامی در حمایت از تروریست‌های حزب‌الله لبنان، تنگه هرمز را بست.
اینها دیگه راه گردنه گیری و گروگانگیری رو یاد گرفتن.</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/5655" target="_blank">📅 16:42 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5654">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/11b10561df.mp4?token=iw6-d2-W5arIckTwlv_-VJwAOW2Yt9h5RvGM526UxJtdWw1l-2yUx1JNX7Mv74qZe32oRFxSpN-tNp9sp5S65m4PkPKquIp4wHtJNbm8Yb3eb_y0BNyPmzTJ4w5kuYrSjTxFEt1aYgNa-Bt4pnSAK0P4y4K0jKTQEycO7BwvmL45newce0bnvb549hvV9s3gidotjy9OCC-nTRw6MrpZN1QPUmh-pnYSrBUEqNkHmb8X__GBHh8cO-NK_IB2uFvR9ZhQogBXqAtIY-OKVGlzdUoFkDT3gCrYovBjzTY68vRdxrNSo2toVP6dIiA9WbmYeoI1hL2aY6frbYEnDdcUkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/11b10561df.mp4?token=iw6-d2-W5arIckTwlv_-VJwAOW2Yt9h5RvGM526UxJtdWw1l-2yUx1JNX7Mv74qZe32oRFxSpN-tNp9sp5S65m4PkPKquIp4wHtJNbm8Yb3eb_y0BNyPmzTJ4w5kuYrSjTxFEt1aYgNa-Bt4pnSAK0P4y4K0jKTQEycO7BwvmL45newce0bnvb549hvV9s3gidotjy9OCC-nTRw6MrpZN1QPUmh-pnYSrBUEqNkHmb8X__GBHh8cO-NK_IB2uFvR9ZhQogBXqAtIY-OKVGlzdUoFkDT3gCrYovBjzTY68vRdxrNSo2toVP6dIiA9WbmYeoI1hL2aY6frbYEnDdcUkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اوه ا‌وه خیلی دارند بدجور میزنن!</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5654" target="_blank">📅 16:13 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5653">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5130bbfc36.mp4?token=VhqkXlhmF8HY2gstUPljAtEGYtssLEba1a75gJHERXBlxVUXxEgYPS2MWKwRQYxISS7O7DGxuGYIM51193lbdjSGeccCa9O3tlpBVfTnqKD1YH-_OWu6k8WAFS8SNdg8bsPwktknpbGcbBLEBC7IfBVqpUkk_zYukQURwSPUcawZ0bKSQ1ZIv4TNM9m-Iu2ANz21MohdNgPMkvsNOajqbxUXxTTnepvqGXYTyPxzfGCzL-LqnslbCaCNTyVcFF4oQ_BJOD5fgrPDtGrwwGibJUBnrEuuBrd2wxjyU7G0LwsPMW5Rawt2LJdxSQHBnSx2aU3JDl8kCSDUnK4xN_cdbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5130bbfc36.mp4?token=VhqkXlhmF8HY2gstUPljAtEGYtssLEba1a75gJHERXBlxVUXxEgYPS2MWKwRQYxISS7O7DGxuGYIM51193lbdjSGeccCa9O3tlpBVfTnqKD1YH-_OWu6k8WAFS8SNdg8bsPwktknpbGcbBLEBC7IfBVqpUkk_zYukQURwSPUcawZ0bKSQ1ZIv4TNM9m-Iu2ANz21MohdNgPMkvsNOajqbxUXxTTnepvqGXYTyPxzfGCzL-LqnslbCaCNTyVcFF4oQ_BJOD5fgrPDtGrwwGibJUBnrEuuBrd2wxjyU7G0LwsPMW5Rawt2LJdxSQHBnSx2aU3JDl8kCSDUnK4xN_cdbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مجتبی، فرمانده کل قوا ۱۲۰ روزه قایم شده :))
خودش هم در جنگ ۱۲ روزه رفته بود «کمین» کرده بود برای دشمن!
که در جنگ ۴۰ روزه غافلگیرش کردن!
«ما اینجوری نیستیم!
خود ما پیشاپیش لباس رزم می‌پوشیم»!
مجتبی کجاست؟  :)</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5653" target="_blank">📅 15:50 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5652">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a19f9c1ecb.mp4?token=OyA5qFcMefxDhjei9uLCfZ9Fg5iihERzPHvLu6Rhp-4eHPj6fEiK_EZa8Zfdl9dpzFRcI6vf04VsF7m9OAtE4jEil8XVHi_5fw6VkdVPaItP1QL0evYfVkuy61hSd0GmAAL6AdsvLj-Gju66NUX64Qk1ru7oKeLoHenJcZgzgjU78PHPf5ygcUWhcSzudPXJa0VY2hBGLXqax8XmRHOc_vo2Aj7hdFN2ulTRf75n8BtMB2D0ZtUukagBbB-4euZ_iwSFu5ZhXMlI38bwofXPgXpBhUwDMWjrNzZKnLpHBGUCcrpYxfLMcmmLdMZIBzFHFoNetWBNtBslzJWW9ZEcMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a19f9c1ecb.mp4?token=OyA5qFcMefxDhjei9uLCfZ9Fg5iihERzPHvLu6Rhp-4eHPj6fEiK_EZa8Zfdl9dpzFRcI6vf04VsF7m9OAtE4jEil8XVHi_5fw6VkdVPaItP1QL0evYfVkuy61hSd0GmAAL6AdsvLj-Gju66NUX64Qk1ru7oKeLoHenJcZgzgjU78PHPf5ygcUWhcSzudPXJa0VY2hBGLXqax8XmRHOc_vo2Aj7hdFN2ulTRf75n8BtMB2D0ZtUukagBbB-4euZ_iwSFu5ZhXMlI38bwofXPgXpBhUwDMWjrNzZKnLpHBGUCcrpYxfLMcmmLdMZIBzFHFoNetWBNtBslzJWW9ZEcMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اورانگوتان رو!
هر مسجد یک شعبه حزب جمهوری اسلامی
قاتلان فرزندان ایران بین همین‌ها هستن</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5652" target="_blank">📅 15:42 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5651">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E80YZ8UiAlLPLJvO4794OlK2sz0Nf-boxn-cW94nqA5UJYhx1FXVDl437RuQmBhnYLtbT0mZTBBGQv7tGm7soXfs2PoylT4RA2pgpKW7fCkaSre-4vObUT50SRvrwP5XO-bGdXAojXX9VyW9j4OAahTC867LZKIZ8PHie7L17iQNtyi4aYshDZmH5GYKJxgb_7y0mvlaaYsRzFX8KRQx8MGR3pYrUxk7EeI4sqQKfDsYl6Douhk6sFnSBTgI4jHQ06rGNYvfaGR_-sTaJJJL7MYyYlcCVnIMPDxAFQn7oJ5063ZgS2_fDfki9kHETTelD7fZSQBVlX4DlKb7kR81aQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس
قاب‌هایی جمع‌آوری کرده از جنوب لبنان
گفته بودید یک معادله تازه ایجاد کردید!
همون موقع که پتروشیمی ماهشهر رو هم قربانی کردید!</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/5651" target="_blank">📅 15:11 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5650">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ecdbcd4679.mp4?token=hwmhu7iZn0vHg5WWuDppiITLs2cPiMy0X_Os9hbuYq-jJosZ4O5uISy8fl-ywNE6_aSYmkZc1N8VDR_v2ENqjijgDBsB9A3Es_x1erzzdIqNdFcTcQ_42n69GI8DI7K0WjKpIWmnX9UWLo-7I7BCk9Dd8WZDQO45RDCdTA2um50IZgqjh8Hpq791Y-kR4DicmB5i_E-v5EnFErsN3SBxrhuCIT0bGTqDQXneUlmtonhd6V6DoFWU8xBTgeqNVLuqhUz48BiU5OFvfisoc9zoADwKzf4Y8b3ePbWPBrDs4yOok2DYUZsoWkiYMWCLa_BvfCOHpg7ikmZSR4x6PMdxBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ecdbcd4679.mp4?token=hwmhu7iZn0vHg5WWuDppiITLs2cPiMy0X_Os9hbuYq-jJosZ4O5uISy8fl-ywNE6_aSYmkZc1N8VDR_v2ENqjijgDBsB9A3Es_x1erzzdIqNdFcTcQ_42n69GI8DI7K0WjKpIWmnX9UWLo-7I7BCk9Dd8WZDQO45RDCdTA2um50IZgqjh8Hpq791Y-kR4DicmB5i_E-v5EnFErsN3SBxrhuCIT0bGTqDQXneUlmtonhd6V6DoFWU8xBTgeqNVLuqhUz48BiU5OFvfisoc9zoADwKzf4Y8b3ePbWPBrDs4yOok2DYUZsoWkiYMWCLa_BvfCOHpg7ikmZSR4x6PMdxBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نمیخواید بخشی از مراسم تشیع جنازه خامنه‌ای رو در لبنان برگزار کنید؟</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/5650" target="_blank">📅 14:29 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5649">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c5aba790b1.mp4?token=uiXJzPS1VIKe8PNqO0KQkze8S34Pw5uplFZz7o8_5zTUmCfEjhj8p6YjHom2kqZey3BfcmLrppVBwdmyd0xm8j5r7lPRK8s00-73gVk-9sIGdzn-lM71Omg0mAbVJkpI_zmCboBlVaJqyTAfCBe6KojhA68rT_pbsy8EVxPUupxb0bJ0gBIsQxl8A69t5VO8Xw3PCUYvzefiPMYq7uEbYJWYmicyQpLc5pTlwJmDMcAr6SxFPBwFgW8INQuEvDiibz-RIumCV-EyUU7BFr1e9ZxlAQsb_fL7fYFRn6WawJj9wkj1_Hmdpw1dDh-zxQ_VpIDhI12kIu4mUmtsH_oLAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c5aba790b1.mp4?token=uiXJzPS1VIKe8PNqO0KQkze8S34Pw5uplFZz7o8_5zTUmCfEjhj8p6YjHom2kqZey3BfcmLrppVBwdmyd0xm8j5r7lPRK8s00-73gVk-9sIGdzn-lM71Omg0mAbVJkpI_zmCboBlVaJqyTAfCBe6KojhA68rT_pbsy8EVxPUupxb0bJ0gBIsQxl8A69t5VO8Xw3PCUYvzefiPMYq7uEbYJWYmicyQpLc5pTlwJmDMcAr6SxFPBwFgW8INQuEvDiibz-RIumCV-EyUU7BFr1e9ZxlAQsb_fL7fYFRn6WawJj9wkj1_Hmdpw1dDh-zxQ_VpIDhI12kIu4mUmtsH_oLAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نمیخواید بخشی از مراسم تشیع جنازه خامنه‌ای رو در لبنان برگزار کنید؟</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/5649" target="_blank">📅 14:29 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5648">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9eec8cc86d.mp4?token=JXpOS50PdTOOCtrk_eHTw9up0IH-4YC8-6jAwTm_3PqPE9PQzd0QxVqNpekt04pRIW7bRSzrJBQftT683npb16M1iOG8Pgjf6Se1Mk3OLYQKv8Eah0W-XZJ1yVMtMVhT2EAgd4UNdMFn3WfivNzRYcqObE0pu_UvuSaxLjbGr_sLE5mw3nCorFMQw7N5GjCNXZK4dOn82L_JP21YunV9v9HhhDfW6xBzPQ4bpIZ2c3reIM1vlzq9LaiqeCYl24jNQXy8hjaDgExg66FKBUHLU4wy1QL7gVmSru4xgpXMfl5ZBYjm8LvuIZp5xTvuB7BwUWQbmjB6KVa2U4bWbQAH3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9eec8cc86d.mp4?token=JXpOS50PdTOOCtrk_eHTw9up0IH-4YC8-6jAwTm_3PqPE9PQzd0QxVqNpekt04pRIW7bRSzrJBQftT683npb16M1iOG8Pgjf6Se1Mk3OLYQKv8Eah0W-XZJ1yVMtMVhT2EAgd4UNdMFn3WfivNzRYcqObE0pu_UvuSaxLjbGr_sLE5mw3nCorFMQw7N5GjCNXZK4dOn82L_JP21YunV9v9HhhDfW6xBzPQ4bpIZ2c3reIM1vlzq9LaiqeCYl24jNQXy8hjaDgExg66FKBUHLU4wy1QL7gVmSru4xgpXMfl5ZBYjm8LvuIZp5xTvuB7BwUWQbmjB6KVa2U4bWbQAH3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جنوب لبنان - حومه نبطیه
از مراکز اصلی شیعه‌نشین در جنوب لبنان
و از مقرهای گروه تروریستی حزب‌الله</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/5648" target="_blank">📅 10:58 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5646">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YE4aPAYCvpuDtzLPFpundPmJ78KIaT3lTQzf6K6jc2-lfZS7AsNWILO0D2pC7e9PStiO1sEWmI7UldWpJWk41hrNTUWI_wEJOHIBFtVRWzN5MpR0-0A5fK2sdYjP6z5mERWABRaL05cLfXt_gslgzSvqf2mTOwJZj0QU7dtunjfj5m1XQBkFTIcmAtgmF_K0W94CHnBsK1-vMM4DJOcmzIXE-ygAEzwdg_bonzo4S-TfEbaQ6nYVtDOoicwRzKyu68wbn6k60NJwg9itNaeBQq1GEhd7bzdB19doWt1kRICgLxI3YNFUeQCaRdsdbU7l4MIm1nA2BW5ucOkezxZvPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/21669172c8.mp4?token=jNSFxMIq6Do5zyplQQH9YQXtKdvZZO-Fx3YYtvLXgx5wM5G-tLxHBz6AorNCD-soV-PrvFrEZe_DXwyidu3nTWOmy_N1ADO_adk3skaX-jVc4HSL_6vyXkMWvyQ-6mvAcQsv32tw1tIKGRNTUeMKeKAXFLBgSDbbT7aZFClybGISKxiREEkpe2adrJffqZomr3IIK2jD2CcuAXxP9X8nVp1wuZtcMZ4z_SBQfmH1Jli47elwRAclN6UKjQ1GOMITkH5rAQJSqP9NeUH-IjjEHcy4c3Z4fBnSafUOiTU9HUkEkTatx77gylniAK0FpiYiZ0N9IX-tGMBRBNxJfo1cTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/21669172c8.mp4?token=jNSFxMIq6Do5zyplQQH9YQXtKdvZZO-Fx3YYtvLXgx5wM5G-tLxHBz6AorNCD-soV-PrvFrEZe_DXwyidu3nTWOmy_N1ADO_adk3skaX-jVc4HSL_6vyXkMWvyQ-6mvAcQsv32tw1tIKGRNTUeMKeKAXFLBgSDbbT7aZFClybGISKxiREEkpe2adrJffqZomr3IIK2jD2CcuAXxP9X8nVp1wuZtcMZ4z_SBQfmH1Jli47elwRAclN6UKjQ1GOMITkH5rAQJSqP9NeUH-IjjEHcy4c3Z4fBnSafUOiTU9HUkEkTatx77gylniAK0FpiYiZ0N9IX-tGMBRBNxJfo1cTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاویر امروز شبکه المیادین
(شبکه خبری عربی زبان شیعیان لبنان
که با پول مردم ایران کار میکنه)
در حالی که حدود ۱۲۰ روزه «انتقام گیرندگان خون خامنه‌ای» در جنوب لبنان
زیر گلوله و آتش هستن،
تامین کنندگان پول و سلاح‌شون در ایران
مشغول صیغه و همسریابی و غذا و….
سوار جیپ صورتی شدن و….. بودن.</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5646" target="_blank">📅 10:44 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5644">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rmVcNLeSk--aGSokmJmGt5FZrLkjTeOD5GMDRMWVow5SoGodMgKMgCUDfa_mYdp8Yi0roZBxUUp3EtUjNsW1NOpeHwhER1FYFX_epFFVexp7yVxpmCdo2D8FJ3W9MPy0y-SfvCLCgfEdfKvEIZ7RdY6jw072mp9G5DrUQdASlksDUVJTzKXueHq63_FaN0p7SV2hM1dh17j7EGTg0FwFMN5RQxHq8cLhQ_BNRkwjslJxmVC5pS2wpjkqtBt8LZPRCHNNVgG5VhH5o3wR1WP0sbLAZf0UxhwIMLe5v4Ehlo16sBPWSE22q2TDfAGR5AP9B2Cg6xZGHVgbfNIVEofwgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e75af7dcb.mp4?token=hbc8S2wNRRMqcLvh7roGXbreGwn-kL6i8sTKPcLdpBqQBM_LnOdEbsnYmCHJMWdCt-4rukL_BV7v6kev4G6hVV1uu3heLFF0s7np8gJsz0NQggOo4SaHS9QswiJCrlt3zdiizeuocbqDE1_KYNPSvJZafFOtmBmfSoelEoi_tMx_FcbferWspq6UfDBIuMsT2uNatbR8ihx6d_enYbz2UWIhGUdyQ0TbMBLLw7EFh4yZT4SwkIfGOmRcNInxeS2llh8dRpsq2G9RxZZ-iU2OdQfg5hh-kUj-Sh5ETkWwRQvGH0P1b7Ld2UYid2td6Cd-jL_phuTK8I7qiHX5Pe3D8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e75af7dcb.mp4?token=hbc8S2wNRRMqcLvh7roGXbreGwn-kL6i8sTKPcLdpBqQBM_LnOdEbsnYmCHJMWdCt-4rukL_BV7v6kev4G6hVV1uu3heLFF0s7np8gJsz0NQggOo4SaHS9QswiJCrlt3zdiizeuocbqDE1_KYNPSvJZafFOtmBmfSoelEoi_tMx_FcbferWspq6UfDBIuMsT2uNatbR8ihx6d_enYbz2UWIhGUdyQ0TbMBLLw7EFh4yZT4SwkIfGOmRcNInxeS2llh8dRpsq2G9RxZZ-iU2OdQfg5hh-kUj-Sh5ETkWwRQvGH0P1b7Ld2UYid2td6Cd-jL_phuTK8I7qiHX5Pe3D8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صبح در جنوب لبنان
و بند اول پیش شرط جمهوری اسلامی</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/5644" target="_blank">📅 09:52 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5643">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/okr4OuE3wsLh5IEWLP7p2cq4p5Da1bWxZoPu6OEvP0H0bXmQwve94dul4S8vYvERCS67IAAoLVEcLgDlzzoSaI9tovkEYqY-1yBU-n_g4LfzfdC4Up2P7nd4KKCtsUm6tB5Ll3qAQO4rVqBD6TaNHNv4a9g8zc1WptZYM-FUP0L86Sj0jr0Q86Q1lz4xahgDIXD8t5mpcYl-gFyyjZpBeBGQC_9K6j66jEt0PdrgPArrqmyDOVdsZRDEjTreyy_qQ5wYiL7vqGHumpYxYl1LewCR0d7F_wJWKIH5baoXyDtvuZ3zfcBG9An2-ZJzms7rGBRyiEKJyQlq9pxmuPGC_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حکومت یزید هیچ کدام از اسرای کربلا را محاکمه و اعدام نکرد!
حتی به بازماندگان کمک مالی هم کرد.
جمهوری اسلامی هزاران نفر جوان معترض رو قتل عام کرد و بعد هر روز دست
به اعدام هم میزنه.
۸۰٪ از آمار اعدام جهان به دست جمهوری اسلامیه و قربانیانش مردم ایران هستن.
کربلا به دست مسلمانان افراطی رخ داد، که برای ثواب بردن و مقابله با فتنه، در این جنگ شرکت کردند. ۹۰٪ شون هم هیچ پولی نگرفتند! انگیزه‌شون فقط ثواب بود! محرک اصلی اونها هم روحانیون مسلمان بود که سخنرانی کرده بودند براشون و توجیه‌شون کرده بودن و ریختن خون حسین رو حلال
اعلام کرده بودند و حتی ثواب برای مسلمانان.
اسرائیل هیچ زندانی فلسطینی رو اعدام نکرده تا کنون! هرگز!
هیچ حکومتی پلیدتر از جمهوری اسلامی و حامیانش نیست!</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/5643" target="_blank">📅 07:48 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5642">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d81ee77286.mp4?token=gK0xmYje-SjmVOViQS22yXfbS-vf4yui3O7gK1eJEOCcaJlm6x0vgPX6QPKyIuWWefSsLdkyTd9rWlqhrefhlnz0RbZYis8Uvmepq87-gNnuCEB_84qbC1RYqQPR9VrM2Q5ogcJfej1Y6fRLlzd0dHy6jeM6KpSdmWL6JUPyOPnQzJVOYn_tUbXNJL25wmBmx7616l4rkbMnU-T7INXOZe62M3jjOD3Cq9fbqAbuNZO8viSrRUeJXMkwlhVf8ZuWkUahlizQ1aAU7G9Yd4xG57z49q_bZ89vrO6wKM-YZKJpQ4_WQkLUmzs3BV8ALem-8Tqgw7a_tEueRMeYyHKzzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d81ee77286.mp4?token=gK0xmYje-SjmVOViQS22yXfbS-vf4yui3O7gK1eJEOCcaJlm6x0vgPX6QPKyIuWWefSsLdkyTd9rWlqhrefhlnz0RbZYis8Uvmepq87-gNnuCEB_84qbC1RYqQPR9VrM2Q5ogcJfej1Y6fRLlzd0dHy6jeM6KpSdmWL6JUPyOPnQzJVOYn_tUbXNJL25wmBmx7616l4rkbMnU-T7INXOZe62M3jjOD3Cq9fbqAbuNZO8viSrRUeJXMkwlhVf8ZuWkUahlizQ1aAU7G9Yd4xG57z49q_bZ89vrO6wKM-YZKJpQ4_WQkLUmzs3BV8ALem-8Tqgw7a_tEueRMeYyHKzzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملات اسرائیل به جنوب لبنان  بدون توقف ادامه دارد.</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5642" target="_blank">📅 00:21 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5640">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/B24ddpPWrB_2S_8Efa3z6FCz8pkKxff-Az1pvW9RybV4C29ot5CPSEwPV4AIheT2-JE4qTnJaFiCYKLOoLtB8f5zUKrIZxvZK4LgSngEswBYKtC3qURwPJ_qtOHTh1lYA6PSvFa7GxCJAHsQJyzZyM0Hd6ebBDyZZr9Z8xXfuyE6jQWW1LIqqA3-RJCH8_w82ZfiT4l7yT-hehoX_Nw9_GPOkXTkfC3w2zUvjk1Htpotxeb8YyttROeUPAjGaH7WSfk9l8EkAaS1qPh8W9EGNKcve3qn1G5qcTMC0snlCNTgiW32zZqYV5wx9uN1bDwhwTKde7W_4oy5TXl1eVJwEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JcYPc6Z6QmxR_hLI-MIXSJt2JUObaQkK4Wt_QxFCSy8GJtcAH_WUaDyvGhZVw89V47836m6-XpHYiGfwP1i6wuXpdsFTkRJsHTrjWbXUs9X_IICNJ5SMws9yRwAZLMVf5xgpcYdxIWxuDq6Zq3UiPNhPT2vdz5sYwx__wC163d1ynuhwO_OblsJ_xeB-3WUBNhdCWDaCWY2EVq6FXK7RX_SMi-J7FP9ZT8snHpsBDH0Nq6LtIgl9c_419JaNCNFDGYlsFkLIHbrLj84PvLZd9U_9pEh7AUo05k04Y3OSFMqrSoZBcjkwHkq5JTS50x4IdKzWAfL8RV3ckpHEuMBi0w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">فرار گسترده کسانی که میخواستن انتقام خون خامنه‌ای رو بگیرن!
تا اینجا ۴ هزار کشته دادن و ۲۰٪
خاک لبنان رو هم دادن به اسرائیل!
قالیباف دیشب در تلویزیون جمهوری اسلامی گفت : لبنان ۴ هزار شهید تقدیم جمهوری اسلامی کرده.</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/5640" target="_blank">📅 21:35 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5639">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f791b65d03.mp4?token=Ah1i22KNF8BOlIkAqkDTQl4IDzVUv57RQ2RgQRmb4iCfiiN1cUtop2qqB9DM3GtScVFjZsmP87wjUVzvBGo74YTBfnPrprzNTZvJPmEDdJFdFGW5Jn7d_D3GqhlpPORGyATXo1BQ_tw7viOLO_Qrz7ntStY5-M_e64fCzlW5cA1YNo82QGAj7GH6N1lj7xtCi2XR1MSyxRklqCR-z-BDk0fvH85afeqbQVEbOc71vUbH0XIyx5Zn5VzO1LlLh8MHkY_XPl903aS_o6zwg1vQdnP9TWHtpra6JIkgl3_djiKusm8Ef_zdgPAQZPh852IIvq6kShWhM2u_pVTYpcl75Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f791b65d03.mp4?token=Ah1i22KNF8BOlIkAqkDTQl4IDzVUv57RQ2RgQRmb4iCfiiN1cUtop2qqB9DM3GtScVFjZsmP87wjUVzvBGo74YTBfnPrprzNTZvJPmEDdJFdFGW5Jn7d_D3GqhlpPORGyATXo1BQ_tw7viOLO_Qrz7ntStY5-M_e64fCzlW5cA1YNo82QGAj7GH6N1lj7xtCi2XR1MSyxRklqCR-z-BDk0fvH85afeqbQVEbOc71vUbH0XIyx5Zn5VzO1LlLh8MHkY_XPl903aS_o6zwg1vQdnP9TWHtpra6JIkgl3_djiKusm8Ef_zdgPAQZPh852IIvq6kShWhM2u_pVTYpcl75Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جی‌دی ونس به جمهوری اسلامی:
گزینه اول:
به رفتار خود مثل یک رژیم تروریستی ادامه بدید؛ در این صورت، به معنای واقعی کلمه هیچ چیزی نصیبتون نمی‌شه.
گزینه دوم:
مثل یک حکومت عادی رفتار کنید؛ آن‌وقت آمریکا، برای مثال، به قطری‌ها یا اماراتی‌ها اجازه می‌ده در کشورتون سرمایه‌گذاری کنند، البته اگه خودشون مایل به این کار باشند</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5639" target="_blank">📅 21:14 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5638">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ir6rVMLNc58WW3VFQE1vC_ABjATdz02O46CKMwhTx29kkJFeAv772A5WSMiVDLOYxhG4b6PJ2IjI7Tw9WMFaww4N_s-HrmBzUY8Vu5s-voVBMT2gLb_QBW7JQPyrykdxgBJeCku-LbPQpuL-cQNg2HnHGV-2lfEEQDKwIbp1SM12DKkaMQLvCnwfsvLJdb-F6h4vlYz385k92mvUDlRMigvMcVB2-yYXq6qFho8tSLaAALYUa4HTDJ40Ziv3Nw8mm74hoGND8jMM4-jDA7ipT1upW2BRyF3flhCdmQVcYpEgRWIlcmdQtivQQPw65usC7T7lyes2kC--4e_qqIhR9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنان دقایقی پیش رهبر گروه تروریستی حزب‌اله نشون میده که این گروه عامدانه شب گذشته آتش‌بس را به شکست کشانده تا اسرائیل را وادار به واکنش کند.
نعیم قاسم :«تا زمانی که قادر به ایستادگی و مقاومت هستیم، چرا باید تسلیم شویم؟
ما تصمیمی حسینی و کربلایی گرفته‌ایم که هیچ سقف و محدودیتی برای آن وجود ندارد و این تصمیم کربلایی همچنان پابرجاست.»</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5638" target="_blank">📅 20:02 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5637">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OKXy4eDuUFprWtipBLQaAEF6mywYCEzWnGRwG7fghqswFAZDk8qadMhmH6CVJwFNc0WZJZ5qkZ-AxLQc_4kKTtcdkG1FWIt4Bs5UqUmf_fpy_MK6ZBtAHGTmX2LAEyaHN0c3Aspcf8HQqM4_HByUpKUzdFjbgdh1tD-cSZimBcRxX6gXHdJPugT-DnXEH7PndQNLQZQ0YRDwdgRbM9UfzxCAbUw_FDabcTv2DgvIwcQlFjb-3gJZWSd32M8CP-sOoZPPgWhv0Zllsij4SaO0QmJKKGrw4le1T0wa6CvFWk-g-cG2xFtngfoH_AGxxf64YGzzgRhaK0q5qLcml6wB4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/farahmandalipur/status/2067993854494622141?s=46</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/5637" target="_blank">📅 19:02 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5636">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V10zEtutUrwpk6iRLxWt3FP6lM5z_D50BjO_l57kn6Ejj4aaDJkMIVxpRRy1lZt8dkp3tZxCzTBWFGsbu2cyL6rQUcyFXMTyWLbjWPU4SQnAfApbLB8QxIoZ-XwiG3K-DBK5_sSKRVSt4luQZgxnVc1Wyo6HSsiDXILDIL-YSwjAAEVBYcYmQQ22uEcZ2-pc6-mCsfc3Yhzv61IDyfmvx7wJkO-t0cpGKCFFV-Dp4qaJDAHopo-9ruSZ462rstJkT71sGziNlxv-2P3omVYo24mYQeukZsqOHliK0N3Y3G2NOiwQczAL8XBZHyeGyGiNVRgjjgy3fJrPUwU6AIU_-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت بهداشت لبنان : از نیمه شب تاکنون ۴۷ تن در حملات اسرائیل کشته شده‌اند.
پس از انتشار خبر کشته شدن ۴ سرباز اسرائیلی در شب گذشته، اسرائیل دست به حملات گسترده به لبنان زد.</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/5636" target="_blank">📅 18:56 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5635">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B6HbX6YppLd_hoZnW5jUTdd-6LVLhppauBX5Pzhd2MxuiBNLeg2RPGJK_xUZ0jCwg_oKpd3-3JWI70U5678aepR2d8LTXSF8a6qJWb2HCVPmeVYGyJeAjPcYJGjQ_MAh0hJFWiyNyTn6qeqK0rR6xsNEllOHFvKJ0PGET5G6Fh-AjfQ0vcpRQG8wBnkQSlAJfEdD-N5NFhIaARona8ofg9Y3nqAuxxZZU8Mh5CK4DXDX7wduKD5-vMdLUOEtLk9rXUUKcsKcokgEAAODX3DMovb0B3S9kvih331dJACGyGuATivZb3FiwXhtYPkkYlJoQialwowXkW7KMSFbMc1Dpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نگذارید</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/5635" target="_blank">📅 18:39 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5634">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🚨
عراقچی : مذاکرات برای دستیابی به یک توافق دائمی با آمریکا، پیش از اجرای این بندهای تفاهم‌نامه آغاز نخواهد شد:
🔺
پایان جنگ در لبنان
🔺
رفع محاصره آمریکا
🔺
صدور معافیت‌های تحریمی از سوی آمریکا برای فروش نفت ایران
🔺
آزادسازی تمام دارایی‌های مسدودشده ایران</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/5634" target="_blank">📅 18:36 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5633">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N9tiZrrFUVm5rdDwhwCRt8AS9nl98bsuSgmClUrKw9EceEA2USa09bxjradGRvnwmxl5q2PqUBUpD5188A7G5NvWsJct0PGWUKQFTeafuZmgH3kRKkiQXslxeJRRwV3qQyO9mq1EWH6KabMW42Zyok6becSSvfINA8hWjqFi7bu2URqtjmI8HyMoPZlEA_GGFRSERHIGWoQYEiEhNR_rDyQMUIfA7phKn3-2GJ1sqyKTOKVfQLbZ2YtLIeSLXZO5oneMEYhzLCamxRCyqGpA5jf6Ei-KFqB8bDqI5JCKBh01hPcHuq684BXWGcbLAbt6NL3YjilfUO5g94nswIogDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نتانیاهو : به بیش از ۱۵۰ هدف در لبنان حمله کردیم</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/5633" target="_blank">📅 18:30 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5632">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/392eac3002.mp4?token=cR3uCLa7yUaulTEPI7IsJHyQ2uC-LnKjmyNBLxjq_S0kYR092kcrDjvql3W2CAbp0MJB1TWxbTIA285LIzWuNKJFiKmFB_FZIWCH3knu-USX4kytQSO40oRuEWuE_VY7rWRF1fsY_bP7-SrokxaNNlZqt2XFWYwTMIDRcu9i_g0StutgrwqBqA2PzGIjj2VtozgBrcMRYDvWJsyI24-dQVGF8njs_Rji90pRHwURCYyP7rPLvmAA6akFmZLVvAHKY41qfEn7qKUp0dkVsmdmJgMFLsLr380lAxhc3b1gNPyICej6Pe2e6SHo0n1eFG66vMQkKvbXLAcP8AznAeRwCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/392eac3002.mp4?token=cR3uCLa7yUaulTEPI7IsJHyQ2uC-LnKjmyNBLxjq_S0kYR092kcrDjvql3W2CAbp0MJB1TWxbTIA285LIzWuNKJFiKmFB_FZIWCH3knu-USX4kytQSO40oRuEWuE_VY7rWRF1fsY_bP7-SrokxaNNlZqt2XFWYwTMIDRcu9i_g0StutgrwqBqA2PzGIjj2VtozgBrcMRYDvWJsyI24-dQVGF8njs_Rji90pRHwURCYyP7rPLvmAA6akFmZLVvAHKY41qfEn7qKUp0dkVsmdmJgMFLsLr380lAxhc3b1gNPyICej6Pe2e6SHo0n1eFG66vMQkKvbXLAcP8AznAeRwCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سخنگوی ارتش اسرائیل :
توافق  برای آتش‌بسی هم اگر بوده در سطح سیاسی بوده، در بخش نظامی هیچ دستور جدیدی به ما داده نشده و ما همچنان
به حملات خود ادامه می‌دهیم.</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/5632" target="_blank">📅 18:26 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5631">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc70f2404f.mp4?token=egvK4RPGQzvNUDb-u8e5wrTU4htOecjqWbznKIh0Yx2PsUY5Q4JH9MBLuQ5pkrZZRDPban2Q22hHdFmpUT389uNDHhnvD-HqxCVDd7BzxFguu4XHP7a4uUjO2OxeL4Rq4v-DsrDnAhApD0l0HfjewX03c-dqVXPJpAmt1Px0twncwxG7FxWKgdnba23XROGFbPMfQSVxCugbrWNBhUBx-jTkX7gQk-IMQ9-_9etvcPlJcKgTwMNq5fOu9H-5Yc516R8WSdxYn0bYsHjh1vt8XTyhj8YxxyqCe8I96CMVL0x9QmycWbegvrARL3DARwo6JgQzGb1DoofH_IH6f5w7Qw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc70f2404f.mp4?token=egvK4RPGQzvNUDb-u8e5wrTU4htOecjqWbznKIh0Yx2PsUY5Q4JH9MBLuQ5pkrZZRDPban2Q22hHdFmpUT389uNDHhnvD-HqxCVDd7BzxFguu4XHP7a4uUjO2OxeL4Rq4v-DsrDnAhApD0l0HfjewX03c-dqVXPJpAmt1Px0twncwxG7FxWKgdnba23XROGFbPMfQSVxCugbrWNBhUBx-jTkX7gQk-IMQ9-_9etvcPlJcKgTwMNq5fOu9H-5Yc516R8WSdxYn0bYsHjh1vt8XTyhj8YxxyqCe8I96CMVL0x9QmycWbegvrARL3DARwo6JgQzGb1DoofH_IH6f5w7Qw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پخش حملات اسرائیل به جنوب لبنان
به طور زنده از شبکه خبر</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/5631" target="_blank">📅 18:20 · 29 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
