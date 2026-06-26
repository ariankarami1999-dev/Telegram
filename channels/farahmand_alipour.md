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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-05 22:44:31</div>
<hr>

<div class="tg-post" id="msg-5742">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac9a1f1d75.mp4?token=nYdQIN6CTGG3-vJk6i8C67cN-mG626L1zv6-_dg6IAYINt-G6BfKl7UF-jSswsxgUXOS5C1F1MCcZ6pq5yDsVIBPPjlAatIANMQc_ifnmwd7OlF3eALwZja_vp08RbCuGYzcZpIaVv_svCtgwI3P_qvVE0DKspIJfItacKmGzWi0XtL73FR6GBmy1TL05-7b8jvPcNZO1AuCK58_u1lA-qmb7Hih9eoQ1b6e3HVx0ZzDT6_Njhn1PpjfzHvbOpDkN4LxQ7UBfB5MzRv1eVlFGzPrOC6eBQLh9ZYzUZK9ZcVHWdTveuqNnWfSuAxAwW12BpTrGv13-BXMh-gyIsv50r1K1vGBRQ8EvKOnTrvzX7oGwbMu0GWYuPY0MMMq7JRNSy7SaBce1HaK76u9hRde_GCH3YxRaoMMG9QHaXckdzdbY5A0CqGEHjXfALIMi9BtQFIFJwbeyxvP1lO6mKGkN_oc_fzgV4r6Z8DcSGOFppFopOtw6ewJ1lmsJl9WfLrUwFK9WmTRjhTh2qqtscpgL_IdnkAxU78X8P4lz-U2iB8B45bWuh0iLnMDEVHFS3AnM09OYchBKVInhEMRu9wfBdjRlnYb_aacH9pX9iftxgB3mBHjXWfCG0OkTIEufOSWpIK9ubE1CwfaqbYv4iL0gpp_ChdasJ45UTUcRFT73SA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac9a1f1d75.mp4?token=nYdQIN6CTGG3-vJk6i8C67cN-mG626L1zv6-_dg6IAYINt-G6BfKl7UF-jSswsxgUXOS5C1F1MCcZ6pq5yDsVIBPPjlAatIANMQc_ifnmwd7OlF3eALwZja_vp08RbCuGYzcZpIaVv_svCtgwI3P_qvVE0DKspIJfItacKmGzWi0XtL73FR6GBmy1TL05-7b8jvPcNZO1AuCK58_u1lA-qmb7Hih9eoQ1b6e3HVx0ZzDT6_Njhn1PpjfzHvbOpDkN4LxQ7UBfB5MzRv1eVlFGzPrOC6eBQLh9ZYzUZK9ZcVHWdTveuqNnWfSuAxAwW12BpTrGv13-BXMh-gyIsv50r1K1vGBRQ8EvKOnTrvzX7oGwbMu0GWYuPY0MMMq7JRNSy7SaBce1HaK76u9hRde_GCH3YxRaoMMG9QHaXckdzdbY5A0CqGEHjXfALIMi9BtQFIFJwbeyxvP1lO6mKGkN_oc_fzgV4r6Z8DcSGOFppFopOtw6ewJ1lmsJl9WfLrUwFK9WmTRjhTh2qqtscpgL_IdnkAxU78X8P4lz-U2iB8B45bWuh0iLnMDEVHFS3AnM09OYchBKVInhEMRu9wfBdjRlnYb_aacH9pX9iftxgB3mBHjXWfCG0OkTIEufOSWpIK9ubE1CwfaqbYv4iL0gpp_ChdasJ45UTUcRFT73SA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اگه خورده گرفتن که چرا میگید سگ هستید …</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/farahmand_alipour/5742" target="_blank">📅 19:53 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5741">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fad365bb7a.mp4?token=ZDr-STvQFPYHiROFw6OPE7okjr7IEHAwGcDfqUYyBg4k0-Dvk9qRQIKcE5xG2aewUJ912dVo_83a_jiYAwUcvSQphHICVJSnFHRCEsILiVyq2xA7qkuZr3bk5_ki9cNSYAuQW9RXOvqhjOSU2zL83IZYkxIZ15AIiPW56JRm1EuZ3RUKct9SeWjS-LFiZfgVlvHezTVkjslzw-S6Ybnjf4E8HQGRf9U2lczcyRXgE_g6QFYzHZV-PLIL5FT8yd0mL40Sp7E4N3lG-LybSPWDd_qpdQBnRXlbNlM4oOGZPr3XikHkTMJCVShwXA1Nnrb6TaFoTfgoL74RMT_P6d5E654wd_8E1jngQZqDbIcfh4AdSiQ_EDnb2WxAuS690KXSFcodRupdFggYwdKyArw0o8pGzZl47VWfX0zcB9MMZDQx_ybsm9a9TYVNbTkjwdFiDzkmtteDTZBsZpge8Yqrlfd38cfUSnn_XLOGgVAtwUs_G0j4wCialaTYYc8QLyT5qyOKtUagLBnyjykmehW9M48AYPaMXLJYbP1_aSUillMhLmu5Z7b4L9SA_H5l6xRzv5wn0rRrQElZwXcLXXb8sNwoJlDZqmak1lnJxHYuYLUnO4pBFG1rSyKICJLZMIOleuhrOmwPDO6BABjWg4UyATSItRoedZ4BGPS0uTxqWv8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fad365bb7a.mp4?token=ZDr-STvQFPYHiROFw6OPE7okjr7IEHAwGcDfqUYyBg4k0-Dvk9qRQIKcE5xG2aewUJ912dVo_83a_jiYAwUcvSQphHICVJSnFHRCEsILiVyq2xA7qkuZr3bk5_ki9cNSYAuQW9RXOvqhjOSU2zL83IZYkxIZ15AIiPW56JRm1EuZ3RUKct9SeWjS-LFiZfgVlvHezTVkjslzw-S6Ybnjf4E8HQGRf9U2lczcyRXgE_g6QFYzHZV-PLIL5FT8yd0mL40Sp7E4N3lG-LybSPWDd_qpdQBnRXlbNlM4oOGZPr3XikHkTMJCVShwXA1Nnrb6TaFoTfgoL74RMT_P6d5E654wd_8E1jngQZqDbIcfh4AdSiQ_EDnb2WxAuS690KXSFcodRupdFggYwdKyArw0o8pGzZl47VWfX0zcB9MMZDQx_ybsm9a9TYVNbTkjwdFiDzkmtteDTZBsZpge8Yqrlfd38cfUSnn_XLOGgVAtwUs_G0j4wCialaTYYc8QLyT5qyOKtUagLBnyjykmehW9M48AYPaMXLJYbP1_aSUillMhLmu5Z7b4L9SA_H5l6xRzv5wn0rRrQElZwXcLXXb8sNwoJlDZqmak1lnJxHYuYLUnO4pBFG1rSyKICJLZMIOleuhrOmwPDO6BABjWg4UyATSItRoedZ4BGPS0uTxqWv8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همین‌ها رو یک تلویزیون غربی پخش کنه، سریع میگن این برای اسلام هراسیه!</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/farahmand_alipour/5741" target="_blank">📅 19:50 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5740">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">ترامپ در شبکه «تروث سوشال»: «جمهوری اسلامی ایران دست‌کم چهار پهپاد انتحاری یک‌طرفه را به‌سوی کشتی‌هایی که از تنگه هرمز عبور می‌کردند، شلیک کرد. یکی از این پهپادها مستقیماً به عرشه بالایی یک کشتی باری بزرگ و بسیار گران‌قیمت برخورد کرد. کشتی آسیب دید، اما توانست به مسیر خود ادامه دهد.
ما سه پهپاد دیگر را سرنگون کردیم.
روشن است که این اقدام، نقض احمقانه توافق آتش‌بس ماست.»</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farahmand_alipour/5740" target="_blank">📅 19:23 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5739">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/726fb491ae.mp4?token=Ez3NPON3BjUJQ0jrp96WZVY2iuSaUrdH7i5j2ZcM5OMDVRM8bmV5V5Z3LBadf7ptEpL-YxxhRcRrcTfnYyqVCnuakovZ-TFaKTPraD9DOOxzE7Lq03aXMpEokoygcgV5m75QELXbESB-loS2zQMnC8A6PUUJ9ujDU38LaIRUKWkGf_49-Ut0Ty6MpKZSG7xQh76xwE_LdVPBnyAlvDr77JeavqnECnXqx5szvsu0MPVUwUVDSZxKg-XMujLdLGPp8O4ebhL1wIlONmDBn6n-koUUq2_4CWbpBRu5Ook4jtuEwjWq3YNVBJlCZvvP3pIfPGUe6MJgFCV3yHECuke0kIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/726fb491ae.mp4?token=Ez3NPON3BjUJQ0jrp96WZVY2iuSaUrdH7i5j2ZcM5OMDVRM8bmV5V5Z3LBadf7ptEpL-YxxhRcRrcTfnYyqVCnuakovZ-TFaKTPraD9DOOxzE7Lq03aXMpEokoygcgV5m75QELXbESB-loS2zQMnC8A6PUUJ9ujDU38LaIRUKWkGf_49-Ut0Ty6MpKZSG7xQh76xwE_LdVPBnyAlvDr77JeavqnECnXqx5szvsu0MPVUwUVDSZxKg-XMujLdLGPp8O4ebhL1wIlONmDBn6n-koUUq2_4CWbpBRu5Ook4jtuEwjWq3YNVBJlCZvvP3pIfPGUe6MJgFCV3yHECuke0kIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قمه زنان امام حسین رو چرا می‌برید بیمارستان؟  بگید خودش شفا بده!</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farahmand_alipour/5739" target="_blank">📅 19:16 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5738">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e184bbb012.mp4?token=WFZheY4bJthLfTsEnmlPwfkN3539xqkwoto4MSCzSkL-z1-xJXH78RVGxCdcRClgTvGYp3DF_Dg1ScWZshArOB40XwR947Di1K_26DbHusR1ACZG1_vTWyFgf7gv0KVqauI_LuVFw7aO-N79lL-dOmucPHrEI180l3MDtWBag-qKhcXgqvbiKZ7nDt_OdAWnSCotaJeey9kDCbIqEWIltToCJNTomthDY9CZX_AjJN1I4RCws5AkseQTI2B9hdfRkb0prAHTe0ehFQSCJ6oS3ZT2WGUAV3tkUSQMZgoZD7aB1JIt8_N_ddi9JcE9UFwAoXEc74C8mgGTBs9TPyGLpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e184bbb012.mp4?token=WFZheY4bJthLfTsEnmlPwfkN3539xqkwoto4MSCzSkL-z1-xJXH78RVGxCdcRClgTvGYp3DF_Dg1ScWZshArOB40XwR947Di1K_26DbHusR1ACZG1_vTWyFgf7gv0KVqauI_LuVFw7aO-N79lL-dOmucPHrEI180l3MDtWBag-qKhcXgqvbiKZ7nDt_OdAWnSCotaJeey9kDCbIqEWIltToCJNTomthDY9CZX_AjJN1I4RCws5AkseQTI2B9hdfRkb0prAHTe0ehFQSCJ6oS3ZT2WGUAV3tkUSQMZgoZD7aB1JIt8_N_ddi9JcE9UFwAoXEc74C8mgGTBs9TPyGLpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قمه زنان امام حسین رو چرا می‌برید بیمارستان؟
بگید خودش شفا بده!</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farahmand_alipour/5738" target="_blank">📅 19:09 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5737">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K86q9Pgkmf-I0BvRjkhFAAeLnuBPT4wEALZQG9gRi2mIKotW_LU9oUFhz13Yg9wjUD67gGD-bXHrZ9cuLM6r9RUd6Y7wGSq-te_T0nixa-QyAPkCcQnARSM9irxQBQGR0k4FyxXamoTIpHDdvIQwI7TSLMxTnjCzTEVFe1sjW1hlJH2tTuCuTp4eMvr8cIcE1FjDF9VNNoQua8vcNToDKWvH0ZZihpe0AZZeIiuhwEmS94oNE9zYOBCIXPrGwMgWRqA9mGOtG-6_rRhUtwlRXQrmqPlC-lcGRDJdW9d4XU6oJ1oYKI7RJZ17n35LbMzsA5c5YIlrNzYacJ9dN4m9tQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیام فارسی وزیر دفاع اسرائیل خطاب به قاآنی فرمانده سپاه قدس
آماده‌ایم کار را به پایان برسانیم.</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/farahmand_alipour/5737" target="_blank">📅 17:53 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5736">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">نحوه اعلام خبر کشته شدن خامنه‌ای
و عدم تعطیلی مدارس</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farahmand_alipour/5736" target="_blank">📅 16:55 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5735">
<div class="tg-post-header">📌 پیام #93</div>
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
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/farahmand_alipour/5735" target="_blank">📅 11:38 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5734">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vTlxXodelZAAUKeGl_CSolqihwb9i2RTgfHoj5F0PULg6_R1ps2Z55DfHD3yEQ6dQaqc0lEzOUmFLC_gejZzbBX7U4vITdlBcuWiLkhyA3AVQb7N_0PwToznCNI6AFDwsGHg53SHI8bekdkBXHoheGV_CU6H16uIPmJvJpvw8wjzwWwaqkBQgnGEKdHB9Rm-_KeYxmk1blfd14DROqikmnQOpwM1DRHXqAYR4NnowRwCsDkZZsMVS48SvsjAy7Xrued8ABhjjPFXm2lttdmCz1-gtqGqDa0QgeWVArkK_Z5ZQOkB7sT4ytXUjnHDdAxXtlqHqlZt5lzixl69-2pyQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر علوم جمهوری اسلامی  در ترکیه،
خامنه‌ای را از اولاد حسین عنوان کرد.</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/5734" target="_blank">📅 22:29 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5733">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YCbooH_h5rMr1jsmM99DYAG-HBv-xaw2c_9FRrELw__GaqzJrc1YnkKG5VuDUm6P5ChZ-V9zIiklEDwImH_QQbDB0rlw3WwCpHBb4woLC7E3eyxIVfFRJS_tWqzJvrv8FBpoCuMxZmQywnPuKU3fUju_LNRmDslASKsde8z1slhFXxNS_QkBFUCiFl84J36JOXFXAKsKYQiqGXF_GqfhTjmRlBUPze-DN_Tmkkn0KOWLBtimGXpJcd9_nPqyyf2qXD5UC_mlWyIgqHGnnmgQ1OKHxJiMZXUwPSTtC1ofldrgb5yRhwgswZafE6Y0Ag9mnWkZltelSh3rDEUgroy1Mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسرائیل به یک خودرو در نبطیه در جنوب لبنان حمله کرد و در نتیجه ۳ تن کشته شدند. مشخص نیست سرنشینان خودرو چه افرادی بودند.
صبح امروز هم در جنوب لبنان یک سرباز اسرائیلی در جریان حملات
حزب الله کشته شد.</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/5733" target="_blank">📅 18:23 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5732">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WM4D2xqXw920j5I9-sKCvfDDKU6t5AhNKkYatnKcd7tyoYkmaeUhgO78sK7G85vU6MyfGE8BOIsXHDeg42fETgvtpANYSdeRfsCn8aIjovbtBuQR8HtHxM5dEojSpN1o7PitmBb4xcOCJXXvNqO9m7jeLwjdONM4vhunTUzrmb6AVzRy2LWWYluO7LsaHMTdPz0fo0KwC2S7WOUqEFZNdTS8J3oEZ7hivBhokMESqW5Cw--Hs8IzErse1J7aHJv56ywILUBFGPnDBXQdh2voFwCwnuB3rB2gKAA97q3tdMur7CkOT-kNgipH2PJCECq_RYmAuZaTgShqZ2Cq1OP1Bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صد رحمت به اهل کوفه!
لااقل به دینارهای طلا فروختند!</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/5732" target="_blank">📅 15:21 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5731">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIran International ایران اینترنشنال</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6715f87786.mp4?token=U0XYFEb8RKWLLwsMhqzQx6C2Y7QrZ3ewrFzFFqywQgi0fYG7bXsWKw3zACAka8z4of3-tU5fwa3K1tR9Gr_OKhusDRcRPhvW5MwMJY20V8EjSYM0M0BCw6fhZhwCkesv2mkE5ax1NEBkKjYY6qzgh_NxnSEUWwlWzcgT9yDaLXFxAEwuDaTin_TvtN2KIHZUDi7WwLu_yJ806xe9pdEWejsuEMTMN8ayhEUs_cPspEP6cwiibW6Oo5EnwXOsldvHr4e34CM-VER78ixik3sv_v1OFhiilCvGuZs6L7-t2q1MLbz3EOi8BTaR51karFkNREqWVfvndE1mNzrtukpsYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6715f87786.mp4?token=U0XYFEb8RKWLLwsMhqzQx6C2Y7QrZ3ewrFzFFqywQgi0fYG7bXsWKw3zACAka8z4of3-tU5fwa3K1tR9Gr_OKhusDRcRPhvW5MwMJY20V8EjSYM0M0BCw6fhZhwCkesv2mkE5ax1NEBkKjYY6qzgh_NxnSEUWwlWzcgT9yDaLXFxAEwuDaTin_TvtN2KIHZUDi7WwLu_yJ806xe9pdEWejsuEMTMN8ayhEUs_cPspEP6cwiibW6Oo5EnwXOsldvHr4e34CM-VER78ixik3sv_v1OFhiilCvGuZs6L7-t2q1MLbz3EOi8BTaR51karFkNREqWVfvndE1mNzrtukpsYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیوی ارسالی به ایران اینترنشنال نشان می‌دهد که صبح چهارم تیرماه در همایونشهر اصفهان پرچمی با نام‌ها و چهره‌های جاویدنامان انقلاب ملی ایرانیان برافراشته شد. بر اساس روایت رسیده، این اقدام «بدون ترس و با قدرت» در جریان مراسم مذهبی «عاشورا» انجام گرفت.</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/5731" target="_blank">📅 15:20 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5730">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/afaf9624af.mp4?token=iF2srjxcL4ZBsJCQ_7iGRxyRMVNN1_PZd42nPcbn3iJFyxQRyIxU3xYnN8x9-e9mSE3cJuw-KHn0cM6qoaoCDYByTpW6NRc1Btl0vsdKkfkmMGQpb_-E7uAd0Ct5cI7FFJfrJi8-FCCyoxVf6HJlV801rqZZp5-HvFRbJpDWnN_JW_HRz7uTkaOE9OfqYw3NyKF3Qi0CeG13GG1OE2X7fiXIGQ11U8VDptU7jtSOWweN0YD6rU-CmeYha0wop3LY6Ue91FitP_jZw9ULFwsS1BgaM6Yl1V8aIgLPqhRhGlZFtD6eXTOc90CaJwQmwX_ojzzvUWuiEjw7WJacY0YSGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/afaf9624af.mp4?token=iF2srjxcL4ZBsJCQ_7iGRxyRMVNN1_PZd42nPcbn3iJFyxQRyIxU3xYnN8x9-e9mSE3cJuw-KHn0cM6qoaoCDYByTpW6NRc1Btl0vsdKkfkmMGQpb_-E7uAd0Ct5cI7FFJfrJi8-FCCyoxVf6HJlV801rqZZp5-HvFRbJpDWnN_JW_HRz7uTkaOE9OfqYw3NyKF3Qi0CeG13GG1OE2X7fiXIGQ11U8VDptU7jtSOWweN0YD6rU-CmeYha0wop3LY6Ue91FitP_jZw9ULFwsS1BgaM6Yl1V8aIgLPqhRhGlZFtD6eXTOc90CaJwQmwX_ojzzvUWuiEjw7WJacY0YSGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گوشه‌ای از جنایت‌های دیماه جمهوری اسلامی</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/5730" target="_blank">📅 12:24 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5729">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">اینفلونسرهای عقب‌‌افتاده‌شون‌ میگردن توی دنیا تا سطل آشغال کشورهای دیگه رو نشون بدن  و بگن ببینید اینجا هم آشغال وجود داره! پس اگه کشور ما رو کلا آشغال گرفته و به زباله‌‌ دانی تبدیل شده، عالیه! عادیه! معمولیه!   مثل همین حمید معصومی نژاد  که دیروز براش نوشتم،…</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/5729" target="_blank">📅 12:00 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5728">
<div class="tg-post-header">📌 پیام #86</div>
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
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/5728" target="_blank">📅 12:00 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5727">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🚨
یک سرباز اسرائیلی در جنوب لبنان کشته شد.</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/5727" target="_blank">📅 10:30 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5726">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/budDXemWSIQ7SkoDFzao16aXe1hInTtqIATa672agPsa9WF8EDsKLaGZV3l2WyzcdOnzy7lD-3AEzDARLU5DylmTGzy0xod2cYQUoVyaiEDygWz-aP4E3vtWkqMWNxQJMjnLh4M8a8tQhjNAa4Bv1ahYqY2UsYIJXOyQRJwyJ-kc9iYNaeAxPHkEf-9b9jhSA_aFjFd_9BNpDx0NOyB7h1peFf_j3XVoUfJM6YCCcfUQgKQ6TLuUAshceY4M24WeK_XLFURecglGtzjYh-FhsWLTeO-BGHNOc3_FHV_ke3Aq8JfdVy4vhfqBQWEuwqtDN5V_HvOy3tYY31T2d7gnSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرمانده گروه هکری «حنظله» که در جنگ ۴۰ روزه کشته شد، ولی خبرش الان منتشر شده.</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5726" target="_blank">📅 09:39 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5725">
<div class="tg-post-header">📌 پیام #83</div>
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
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5725" target="_blank">📅 22:56 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5724">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">وحید اشتری، فعال رسانه‌ای حکومتی :
تنگه هرمز شبیه یک بومرنگ برگشت به صورت خود ما، در ۴۰ روز گذشته حتی یک بشکه نفت نفروختیم. از لحاظ نظامی توان شکست این محاصره را نداشتیم.
گقتم تنگه هرمز میشه تنگه احد براتون!
به هوای غنیمت گرفتید، ولی فهمیدید باید دو دستی خودتون پس بدید!</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/5724" target="_blank">📅 22:23 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5723">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/171eba79df.mp4?token=ow6l9ksUoGYZxnwQlVeafEhcH8479ExBpzIW7qUM2TIrMAybIWU3tUK6MnXctg1RksF3XHaZ8D7pkgpqvrKNCY8OqHepUU8zwNpAaABO6QkPCbfCLQV3yqv-W17RM9gN3NypC4rVeod5sn_e9qENYBrWWglah_VORY7RLQBHVwBf2uXKLbbb-Crgd4vfP6vbR7fPRS1aXwOV1GHZjMZl0XDlsrnAWyyexQqU3vyjYi8phBRJI54YM43XiWi0A0V_HwYz3CMBKlVULO1Z4RSERIWCRxkAJNEGiQiBvnA_yDY_drf9RSJ7WctWGdl3r1d4fRIaHpbgnJ2yDyC4Q4j0JA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/171eba79df.mp4?token=ow6l9ksUoGYZxnwQlVeafEhcH8479ExBpzIW7qUM2TIrMAybIWU3tUK6MnXctg1RksF3XHaZ8D7pkgpqvrKNCY8OqHepUU8zwNpAaABO6QkPCbfCLQV3yqv-W17RM9gN3NypC4rVeod5sn_e9qENYBrWWglah_VORY7RLQBHVwBf2uXKLbbb-Crgd4vfP6vbR7fPRS1aXwOV1GHZjMZl0XDlsrnAWyyexQqU3vyjYi8phBRJI54YM43XiWi0A0V_HwYz3CMBKlVULO1Z4RSERIWCRxkAJNEGiQiBvnA_yDY_drf9RSJ7WctWGdl3r1d4fRIaHpbgnJ2yDyC4Q4j0JA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قمه زنی گروه بزرگی از شیعیان در کربلا</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/5723" target="_blank">📅 21:46 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5721">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jli0x8Uba9R9ryS_L9mD5KhqBLbTThFDO_I-iwvSrqt8Km41qL9N45oANx7c9YoE74z014uH28jhrirbn6kYxPJXinJAaAggQnO9SZPOErskbVK2CE3F5CGG1xUBl2393QYM7Y4jw49jvL4UNFF-BSrSfUmPImERYlqIZrCp0T1mgW8XjqmqFLjV7sfWzyZxLRex9Zyd5ooQ_updFz7-FDZNskFelPBxPbWT_S_YEpAqDldju6JpNb7JIEKqGVlMFzIXL9MNRgOZoZ5jgKBVi_R74uWNnZqhEp113xe6nZktmT9wFI0TyHPU1T5B7Lr0k2ltnnZ4RP5hhpqg4RWGFA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5721" target="_blank">📅 15:52 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5719">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SPL-slQDGyTqKrdL8cVYM0YZWmNHvgrDTvAom5gWlDH4ETbN11Ckb1LQrZJ5FpoaGLbXFWooMMyfNQWNqT0aZKghJIuHHDuw1KJgj9gaBXVDGTe9jFfiRQqI_tNFnL7y4Bx-Iieye8zggap-7XwIeHP8iY6zmnLxFMVRR-DLntiBYTamyLFSIohf6iUoeYQQWTTN7joHTee6Iz_Wb3CxGolypTnxE4FaCR6HGMyZ2-xDzYkyeN9D0cLPXwo9GbwCMzOD0afsZ4bDJAEvDDdkpgKBtTm__OvNoAZdLXifcSlxHfEQXGsZux7ImK41XrgO8rL60Tu5MGafFenwhuqvTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PAgBEqRjCAk0SdahIQMTrQtckAnfRmmYBmGumdCQqqY_SIM2LIGZRvZVzht9r3vCM6GP0yQfslXYlgdpVXZzQ8G21OtfCNS3Te4JBOu7BLqQ9mgRJxgp9HtDkA8TgNSqFvBqObnKT2L-fWcBBR30jezWZ8x680dkwLozdu9vyhAUMlMS6TC9oP7foxKUW5an_ijOy97rUCaE2yABmVWWa63-7R3lBY_tKN8w4yEhNiYtqXUtkFQ6JLK8pGcfC_G8-2wFLQNmAIILry1otDT5a4PvtKU7UvFUWw9OVRINmcaRFqIpJfNyErfi5o4fQfEzwF5UlD0UeMpo3e-dvwa9Vg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دیروز تولد «آیدا عقیلی» بود
آیدا ۳۴ ساله بود که به دست جمهوری اسلامی و در جریان کشتار ۱۸-۱۹ دیماه به قتل رسید.</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5719" target="_blank">📅 14:39 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5718">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">‏خبرنگار : اونا می‌گن هیچ بازدید برنامه‌ریزی‌شده‌ای برای بازرسان آژانس وجود نداره؟
‏ترامپ :
بلوف میزنن ، ۱۰۰٪ بازرسی رو ثبت و قطعی کردیم.
‏اگر راست می‌گفتن، همین الان مذاکرات رو لغو می‌کردم.</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5718" target="_blank">📅 23:27 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5717">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/975d16374b.mp4?token=LVvxy8WMW7w3lFvL-q2ZEKvADeLj4-tufpvfihw2Rbav926G9ZrZ2dSwMlMiXbKcV76Arn1gCffn-0GOrpbs9k2TfZyH91hMM6jTklvcowLHEYZGKY374WsFMcTwhDns2C3z_DWwMBAcFyCjNRDEeQzLTklBfashcEKc8yuUK9Rj2wbbltC-DzhfxOOqfuLkP3vAMo3usAOL_Dxlypif5uCfdansOxANnAA-CmSeePNRi3rFDXRWXGpNWalgA0ZEjDRfDkmhjijOELXi-HVtH9_w3Yo8yCBQim1S9UZL-Ls14UTIyFYy06CRMfVDPQbd5KN8Gz0LnEIEUii8uYmbpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/975d16374b.mp4?token=LVvxy8WMW7w3lFvL-q2ZEKvADeLj4-tufpvfihw2Rbav926G9ZrZ2dSwMlMiXbKcV76Arn1gCffn-0GOrpbs9k2TfZyH91hMM6jTklvcowLHEYZGKY374WsFMcTwhDns2C3z_DWwMBAcFyCjNRDEeQzLTklBfashcEKc8yuUK9Rj2wbbltC-DzhfxOOqfuLkP3vAMo3usAOL_Dxlypif5uCfdansOxANnAA-CmSeePNRi3rFDXRWXGpNWalgA0ZEjDRfDkmhjijOELXi-HVtH9_w3Yo8yCBQim1S9UZL-Ls14UTIyFYy06CRMfVDPQbd5KN8Gz0LnEIEUii8uYmbpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سیرک‌های جمهوری اسلامی</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/5717" target="_blank">📅 23:26 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5716">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Omq-kKYnUp1JzTnS7tRLtKO-d4cYzokGyeb3lfodamLwlTe--yFOS2kVqociJmDMxwkUaYX0iprXd6OfwELYOnGn83XtMm_or72JvLf_YfKwtbr6ExqPqKp6CfWb-VRgK9SyskDnx1s21XvTMVI3eubrHVEdZ-_TDlt22jBKDrQ7FKqLjnd8BoLsjk4J0M8SCywjWnPu3hD-1qOxdKL7nG4gigssCP3lq6rk0rRlImeLL3YFIDfnmMDicTJM4q1fJZmxowoCC03A43oUj4zgnyyeBfdCQZRneBBPOUW07wHWwjL8aSrR7BVaQFYTOaY2YRiT5VpJ7LE6cp-8YURNUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
شهباز شریف نخست‌وزیر پاکستان:
‏«مذاکرات شامل برنامه موشکی ایران نیز هست و آمریکا و جمهوری اسلامی ظرف ۶۰ روز آینده درباره برنامه موشک بالستیک و موضوع هسته‌ای گفتگو خواهند کرد»</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/5716" target="_blank">📅 19:00 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5715">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZDmGQUsjdnuee8oxmmcPzIE1iqeq0nHk5yAPdN3B8ZxXPQU13ALP2vu_DHzQcEaEZzjic9BpAIBGYXIrzWZXvdkBFLVBifkE1da0fVtRrkdwqAt6u8QnxZXd7P4XzalUwx2YBFzS5Tem-tm7MvamE5OBxFDdep9edF_Shaqc3cKeilT40LTBsxnXfZfw1C_dR43lJBAymPQBvFojFdgWnlYWgZLw-quZ6VjcGxR4iidfy2Y967BQtWjzYPeM_5fIJuLc_UCxUGEJI3XTsu7DyGE_8bse5zzg3eK6wiFVBmv0aJtVbuuAXLZRUkqxwtmIlz8u1DVZeQFDOJthJMLzoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/5715" target="_blank">📅 16:50 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5714">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">فکر کن رهبرت رو بدی و سویا و ذرت بگیری.</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/5714" target="_blank">📅 15:27 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5713">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mNEE6P8zoudCtdxLD1kFEsEzIecpjuzrfPvQsHJwgfDKipgSZarZxgxqVPb6BSob_wa6bZRE1hlflJfW8w9EA2aC2Qwn0S13_MKAvuPBDUirWXfK7CnKm3p1j3ZbQRwpqmDDQsBw_x2yBnk796QwwKsh5w044oLkHzm8-K-JO6lhNoqYBARIsbPfGJVJe7NKJKrjxbt_MiUIhkiZhxo8h4XHRHdGQ4p8-cSnG8-EjYeUe1Z-KCyfXQiSjtFXiOh72FBpIgoWuMmGIaoX0yxlgg9YWmxetyaGgBCd0-hpSO-q8b_a24QB3CXI523v6sD_sF-cAgGitJmv0QWx-gXVcA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5713" target="_blank">📅 15:12 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5712">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">ترامپ :  با وجود اعتراض‌ها و ادعاهای خلاف واقع آن‌ها، ایران به‌طور کامل و قطعی پذیرفته است که در آینده‌ای بسیار طولانی ــ عملاً برای همیشه ــ تحت بالاترین سطح بازرسی‌های هسته‌ای قرار بگیرد.  این موضوع «صداقت هسته‌ای» را تضمین خواهد کرد. اگر آن‌ها با این شرط…</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/5712" target="_blank">📅 14:59 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5711">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jmmccHlP0zwM74Jl3PAAERjOQgAx2AmUSkml6yQpudMtIoYU0c5ktpBgcwy_yFFQ09BonKZ7065fSE-n-RnbGwJTmwb62zsUxXp3hUvoYVosq14fTmmYpyvB7uCsxAYqFNhT285hCsquPhsH9Ry0iR-1_HlnmgMtuQxdZlnrEbfD6wmhWBEMBF_hKu57liZPxc_vBMFq_nhQfJfKHYJe1LCYFbjVa4QKU_pSLP9OKAujJD0cO6k-KcRTU616ff3bqLWUNFjd_AccJuXC5_DnhBzcN1jtypMubusEsBESd7d8zN1Kdgo06toOb4cL_pWYcyCJ0faBGcFvtSImmhQM6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ :
با وجود اعتراض‌ها و ادعاهای خلاف واقع آن‌ها،
ایران به‌طور کامل و قطعی پذیرفته است که در آینده‌ای بسیار طولانی ــ عملاً برای همیشه ــ تحت بالاترین سطح بازرسی‌های هسته‌ای قرار بگیرد.
این موضوع «صداقت هسته‌ای» را تضمین خواهد کرد. اگر آن‌ها با این شرط موافقت نمی‌کردند، دیگر هیچ مذاکره‌ای ادامه پیدا نمی‌کرد.
بر اساس این توافق و دیگر امتیازات بزرگی که ایران داده است، من موافقت کرده‌ام که تنگه هرمز باز بماند و محاصره دریایی دیگری اعمال نشود. با این حال، تمام کشتی‌های نظامی همچنان در محل باقی خواهند ماند تا در صورت لزوم، محاصره دوباره برقرار شود.</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/5711" target="_blank">📅 14:59 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5710">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c4fa249d98.mp4?token=KKOtkilSvufZAq8Iu0AANbG2r5wnZB9UC8HwUuFcJdUOHdIHdl9_GK-bQSI7e4aa0fKDR7ORtlbMJE4H32yXrt5fzHpWLtCeJI8jcNL_zCk3bIAlZvYfUdY-qTZdVpXCwoV0FNTYabcJBIiyhjA6uxeWeUmw7ktl-mpMD9rHGGye5ZGJSEIjA8lAfcWjtJg1LT5cD98lz_2d20eWlbjDneqVTHuOHUmBM-GnCkOfyUJAmFN0RY2IBh9khfMwmI0oFJQ7G0RiAUoDsBaNzjsZ2_zhQ3uMvQCmkzSGFXPAlQbFx6xx4bjTz8Pg3Ydhb6TK21TcjKAF5sJ3hDnn6ttWgg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c4fa249d98.mp4?token=KKOtkilSvufZAq8Iu0AANbG2r5wnZB9UC8HwUuFcJdUOHdIHdl9_GK-bQSI7e4aa0fKDR7ORtlbMJE4H32yXrt5fzHpWLtCeJI8jcNL_zCk3bIAlZvYfUdY-qTZdVpXCwoV0FNTYabcJBIiyhjA6uxeWeUmw7ktl-mpMD9rHGGye5ZGJSEIjA8lAfcWjtJg1LT5cD98lz_2d20eWlbjDneqVTHuOHUmBM-GnCkOfyUJAmFN0RY2IBh9khfMwmI0oFJQ7G0RiAUoDsBaNzjsZ2_zhQ3uMvQCmkzSGFXPAlQbFx6xx4bjTz8Pg3Ydhb6TK21TcjKAF5sJ3hDnn6ttWgg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار  شبکه «الجزیره» ، احمد ویشا
که دو روز پیش توسط  اسرائیل کشته شد</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/5710" target="_blank">📅 12:15 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5709">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q1jhVboDPuwSnEfjMeDu2okTOq9t0O-5uzKbw92fEsqsG-NgGR_dj7Bqa2rk3DXX9f-hC4gvu00bxxih268NWwKs87YWf378u-650dnsOXY2Dskyf9Rp8TTKn4y6aLBk4g-iDG9FJ5P8mjgdBE-fCxhKqeAsTNPaxLzKriZyW6Ci1UXl1oKE4MSPReDLkl3iUtQ_V9QcVAHMibz7pWPXnpfIyXPbE_vedzZgIm77WumSOgRNZQVEdkAt2wWI2nxlXe_tA2r1Y05E2EQUVi7wWAO7z3cRTBbdeHdZXdJnk29FtFhLWwCzakJamdexgEgy8b8kAAwR8DkA9fQNOLCPzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حالا هم‌دیر نشده.
«شیخ نعیم قاسم» می‌تونه از اندوه پیجر‌ها و کشته شدن نصرالله و کشته شدن خامنه‌ای و کشته شدن ۴ هزار لبنانی در جریان خون‌خواهی خامنه‌ای، برای همه یک جا از غصه و اندوه بمیره!</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/5709" target="_blank">📅 12:12 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5708">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L_hglFd5ul6QHZvTTouVtwx67bmt_OfDf3fuya_wu63YTeYt9-rM7jX-Yp-G2wBPk-I7-2NA64_9fGuZumUs_FcRjr0QcGhhfi07RleJFyjTxVbHLy1qRM4Yt-kVqu2IZqsVM4OHiYJUA3A1Ee_0yx8dScL3C3t3X6FvfXjPHggY5s-YP3zrWOFSb1O4B_IZT95Wi7fhLv2TwsEtJOJ4tBSVtpVwiAt4M-qzbRy9b-ytU7Il-iHL7f7vx9Rt6zAF1oVTHYPF4sK6ernRDnXCuca7rB2edtwDsMdgbpjYDUv-qhp2G7cN3GpgVPm-XdCWTkuNv5ZLxrKxKwwYBJ4Kdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فکر میکنید شیعیان افراطی فرقه جمهوری اسلامی  فقط با سنی‌ها دشمنی دارند؟  با یهودیان؟ با مسیحیان؟  حتی با شیعیان مذهبی که از فرقه خودشون نیستن هم مشکل دارند! تحملشون نمیکنن.  توی کربلا و نجف وقتی اونها رو می‌بینن دست به انواع کارها میزنن، تا براشون ایجاد مزاحمت…</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/5708" target="_blank">📅 11:43 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5706">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WEjJXq1y-XPsVAsM4v0BGvunzKLDiGirFycTiEyLGIfMBxC3h1REpmsH6QX2ofEFQ8_a8dSC9WoqPdTax3IYdGvT63_AA7bHehRtpP00jSCaLOEaNWNm9jPxP7MVlJNzAXhoQDX0Ve1lrnimFA7r2o-d_3h9GasxZojh_VHKIvrMMyos8Tc5s6z9vk_YCdpzjefi9ZhWOQOfMz1XwV8UJEdbzzzHU2lLxPHlXuTc2h6sRBhcU2IYp4Q_1cFPc9Gw6LQa7BFzOCmoqqmwgSP2frNMn1gpQX1SL1fEi8pZPN4MohrYy-YUkxAX8FA-Z0vkIvzUzGgdphxpCqRNcAKSvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فکر میکنید شیعیان افراطی فرقه جمهوری اسلامی
فقط با سنی‌ها دشمنی دارند؟
با یهودیان؟ با مسیحیان؟
حتی با شیعیان مذهبی که از فرقه خودشون نیستن هم مشکل دارند! تحملشون نمیکنن.
توی کربلا و نجف وقتی اونها رو می‌بینن
دست به انواع کارها میزنن، تا براشون ایجاد مزاحمت کنن. با افتخار هم میگن
بیرونشون کردیم! انحصار طلب‌تر و افراطی‌تر
از این فرقه که با پول نفت و با پول مردم ایران
فربه و وقیح شدند، وجود نداره.</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/5706" target="_blank">📅 11:26 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5705">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c656e44d19.mp4?token=COhDjrwsxyBgDBWkjqTGr-Tz16AaQm5LSMaNVcoeZT7kp01av7nrHaXchR61_dkjYeuw6SjADjNy1tsGlIirKWN43xBT84vBWQozH0Lz4h9BtN2qECmGDSoYpG6_TaUhC5VmeNIwCbLZmrp1sRxUTMLwYRlTQ5F7Vr2UwpVj6t2bS7pqdYdBouAxZ-TP_TymOfxr_KhWrSm34Qtp00oI250YlAs0UF-QyngyKH36MWCCS4m2tuoNussY45x6WAgJJBtN57BFTou7xih4dYLZyxD9yZOqsYU9hWxGimvqAKWU3ypfkk7Z8inf6jC-vXgfftxeWOeRKZydHoUddTdKaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c656e44d19.mp4?token=COhDjrwsxyBgDBWkjqTGr-Tz16AaQm5LSMaNVcoeZT7kp01av7nrHaXchR61_dkjYeuw6SjADjNy1tsGlIirKWN43xBT84vBWQozH0Lz4h9BtN2qECmGDSoYpG6_TaUhC5VmeNIwCbLZmrp1sRxUTMLwYRlTQ5F7Vr2UwpVj6t2bS7pqdYdBouAxZ-TP_TymOfxr_KhWrSm34Qtp00oI250YlAs0UF-QyngyKH36MWCCS4m2tuoNussY45x6WAgJJBtN57BFTou7xih4dYLZyxD9yZOqsYU9hWxGimvqAKWU3ypfkk7Z8inf6jC-vXgfftxeWOeRKZydHoUddTdKaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تنگه مفتی مفتی گشاد شد</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/5705" target="_blank">📅 10:37 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5704">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa6e1aeb6b.mp4?token=bc4BeKevi2i_ojAYKl_N09bQ9wsXWM0VPP5w6iRzZZW9lW6RWBeWSckhd_zZrCHZBhCnK2kz9G3bf4BqotY7tYwJBKz0LrMMqs902mnDDEUpaBBbEllxJWRLGh3jsL4xHjKrUUvgMhY1wN8Sdm5sXD7VmW8qszghDLhXpnyi9Xv33HIBDl_UEYw8hOmT8pLC3Vbd_JnWCqFj8gv6klqvECB68Wc19xx3RlheG_g1ovpKX40VSCmEpudFxAdedFSU3mzHzA8Pcc3UYI5XTQaWKtd7fV6A7TI0K5QzeKvVxWUP2NGgO1ekm7BfVhu9zoxvD1dAiQ-6ALvyu-s_683NsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa6e1aeb6b.mp4?token=bc4BeKevi2i_ojAYKl_N09bQ9wsXWM0VPP5w6iRzZZW9lW6RWBeWSckhd_zZrCHZBhCnK2kz9G3bf4BqotY7tYwJBKz0LrMMqs902mnDDEUpaBBbEllxJWRLGh3jsL4xHjKrUUvgMhY1wN8Sdm5sXD7VmW8qszghDLhXpnyi9Xv33HIBDl_UEYw8hOmT8pLC3Vbd_JnWCqFj8gv6klqvECB68Wc19xx3RlheG_g1ovpKX40VSCmEpudFxAdedFSU3mzHzA8Pcc3UYI5XTQaWKtd7fV6A7TI0K5QzeKvVxWUP2NGgO1ekm7BfVhu9zoxvD1dAiQ-6ALvyu-s_683NsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏ترامپ:
‏اگر ایران به توافق خود پایبند نباشد یا رفتار مناسبی نداشته باشد، من کاری را که لازم باشد انجام خواهم داد.</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5704" target="_blank">📅 23:51 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5703">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">بیانیه مشترک نتانیاهو (نخست وزیر)، وزیر دفاع و رئیس ستاد ارتش اسراییل:
در لبنان خواهیم ماند و زیرساخت‌های تروریست‌ها را نابود خواهیم کرد.
🔺
از مهم‌ترین خواست‌های جمهوری اسلامی موضوع لبنان است و خروج ارتش اسرائیل و بازگشت شیعیان به جنوب لبنان.
🔺
وجود بیش از یک میلیون آواره شیعه، فشار سنگین اقتصادی و روانی بر جمهوری اسلامی در لبنان ایجاد کرده.</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5703" target="_blank">📅 23:42 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5702">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d53a76b465.mp4?token=vSJpEBCplukKo2ApGhoEg4bhfQA7E03dKTFlDGQfp8XQAC2FsYYqlH8ps-X_YJZ2n0TSK9fqXr7l30i6hEUbcoFkqivtU3fsmqRzl8e0Q7A390rWfsE7ZWvrsF4D6WDWqN-t3u7rMDT-Gwtyd-BcuDqFK64NylxAjv4f_dpnwczhwucGZGJzgVYauWWQ6gbVkLt9SIIVXPsWvaisl9QdVAU1KwSgdVCbuK1xEUa1v4nj9wD4-3RkQpv7V1uKyoxGsJ2TL9SR-vo0QgK7vs9iZ1ZnhuNtILUXoG3nd-ggjCYMJ0vxuW-g3eECQMoVPPEYvURDS8OXpZ_rQc9KGDSDWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d53a76b465.mp4?token=vSJpEBCplukKo2ApGhoEg4bhfQA7E03dKTFlDGQfp8XQAC2FsYYqlH8ps-X_YJZ2n0TSK9fqXr7l30i6hEUbcoFkqivtU3fsmqRzl8e0Q7A390rWfsE7ZWvrsF4D6WDWqN-t3u7rMDT-Gwtyd-BcuDqFK64NylxAjv4f_dpnwczhwucGZGJzgVYauWWQ6gbVkLt9SIIVXPsWvaisl9QdVAU1KwSgdVCbuK1xEUa1v4nj9wD4-3RkQpv7V1uKyoxGsJ2TL9SR-vo0QgK7vs9iZ1ZnhuNtILUXoG3nd-ggjCYMJ0vxuW-g3eECQMoVPPEYvURDS8OXpZ_rQc9KGDSDWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ : پولهای ایران  که قراره آزاد بشه
باید برای خرید مواد غذایی باشه
و فقط هم باید از محصولات کشاورزی
آمریکا باشه از کشاورزان آمریکا.</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5702" target="_blank">📅 23:39 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5701">
<div class="tg-post-header">📌 پیام #62</div>
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
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/5701" target="_blank">📅 20:57 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5700">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MesigbOwqbKIbGsEDcbpj5toSir6SesbE4khLhvsjb-P6PaaHDM7MOUz1n1Tb1UMTD2L1EUcm23h3q76OyxmwNmwbofnErfs8DnHpeo1HLrmXfsOSQE_xckbc-OTI7VefX4cLRaW-zoRkOKOvmxQ28Ynz0FZnmAohbfrOZJOyAODzE7uQRIPC5YpdFhorzkhR6I8myQff9QuCNnHuUYqnKeZmr7dxub5S-jvkK1LraF5jV88Us05bGIoNiGrZ2oJx-B-TT7tDLMxCq1PYDh0dcRq89agpWIj31i2l6Wckqj-QXJfLAI2kULpHD-UIntfDm-KFOoxCfhpv0dIbCh2AA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این درآمدها هیچ وقت برای مردم ایران نبوده
هر جا پولی رد بشه، خودشون اونجا
قرارگاهی زدن و پول رو میزنن به جیب خودشون.</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/5700" target="_blank">📅 20:49 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5699">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gB5yA06DAnMUdQtdy0LrLGSz6kjiG9nazT32K50peJQqytYyut3d7WhGGe9iyfC1didkcLtrWq1HuHSF6pXwYk0EOFf4fNDtB4cYPVNMGJKvQrhMupeKn0tnov7MXoeVxuu6_FiUfoGbOGx6P9AxWbYRv4FR-sytZGmgT_XEJNeZmNpsBsBMhPuQsztY2HafGQGWa_JoaBEyQWs8Y0bJD4NpGyT9Xcw-vOz483H6YK5za-boqm_vjYI8eAHjgfUgnKEMW-ulLZiDaZpphdnZGbEexqqSXJvo2QjAOHdOOjerY2-TwQErFIcHxJuLi0lALMfxGmSod1zoJu4Zm2DHzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
ترامپ  گفته برای راستی آزمایی
«صداقت هسته‌ای» ، جمهوری اسلامی
علاوه بر پذیرش بازرسان آژانس اتمی
باید با «بازرسی‌های تسلیحاتی»
هم موافقت کنه!
«همه کاملاً می‌دونن که جمهوری اسلامی با انجام بازرسی‌های گسترده تسلیحاتی موافقت خواهد کرد تا برای سال‌های طولانی از «صداقت هسته‌ای» اطمینان حاصل بشه.»</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/5699" target="_blank">📅 20:45 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5694">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Xe5QK_trT256BmO43MG6sz2g8fTSQ0LF6Ni0Vb0dbC1bNTgZ28ZeLaS2hckybJVWpqaWQvQdFtpHBaMPG_ot9Ykt4OIL_cuVTPVcSDUHz3dnE6nwpm32mbbRQsB3xU2cNuOxZIKaYkC8BBwSp7NqkTdl74x7erF1yUqtJLmzbrfce7tPUQhGZPRJofJogpWQXeET4j-_wyGT0hY-x3MthoGMP8J5RpqHhDQuHnCxHFAMgevqAnBK7za9dbbav0EUxly1Ka9Jr37wrigPKrvF3EuQ728tvTes7_WE2nLigYtktq-4uKsD9tLvopZFiFy8kagGmrdrkTnyefDbreLVUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/L9fUrDaTWi3gcVHEIrE4jjcD_JCioaft3vYfmLVpKutEwyEi_VbLX233LDSXe_ix2H9iOm9BNAqAvMleHk7uUv9sYSkH4_zUnnTiBLJWP-Jaf8JnKs_oY4zaEZH23_UTl16zvJQvEaLGwgP9T0yZ-zU094Fwmj5Ug6qcM6BjnbNMxYsqyec7a2K2V_H7Ut1hhnafQimar9JGsV02NzCVUYi8TwfSzw1Ak6ph9vR71EOSjN6KGAamrJMDfChsfDa4m86t1Sne6J30CY4H1qlux6SJFkk6BLMyVsBP-rZtIVOV6TVbfIb4yL16aLBM3Qmlez0pjeWK8JZkQS7aEx4PZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cLRemZQnnLAr_0MXdJNUaQvjx_lvlYRhYN9oB-ryfTPh2k3wOuHxC4ylYQBr1Qd-je4c3Dfo71us5badlcOHi6cVV51giOn1eC_AQKugQv_V-IGLK3dXRNl8ZovGG3Qymum4Mvn5k4GbKJb8cWWoJqeBIOSSG7ZkiaNwEncRztdFfzPDaEkC8TymxZhIWMi3cC9S2B4YoUlbxyId3PGiwsLrJpjcrMQG4lxFhsFOg_-WgY0u0eY5zsU8NrAq-zqK_0c4nBVMB7m6OsDgwpPJEV-PpVHLb6v6elU7YXznO95o8CleTIqQncdpMGGZQTmmmoagWFPwEUAiGRZ7kV_VRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Q2SGENP3Ye9dn74UxpOvqZtUrtjLKF2IiGCL8yMlXuTZD7MgNBNfHD3r-56wX2dBx1g_jsNK0oH8J8vI5QMtnqK2O57LQr2H7Mj1wb7sTAFfAw2AJmZlpeb_icfhIAaXD6gOHtIxE2kk5QiSsPmfr0DEjLcpUdpf7lnRwJYcwEWwrw6lkPoX0vUOn7iCcYD8LAJ6SdFBQLot36TJDFeNL8AgM2_SMJXBsxyPipdGfb2Y11viuJC9cPUs8OYZAvjPLXp3s9AulNvJNnyLXr54YciWIJ707dBZP1NCXT_vJmJneQLDX3ByIw4H9nfCPsZVFZHJyTnyAI4KUqLrfbrCjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Udm-ZRjCQq2v_bT5LFTyNfYDpZqM5IaAJkK7tbB1ev5LXfF81X-rDR236eN7nEZgJptnfxO5fcjRL-b0SPVd5oLVmu1YZvUqucWJFqvNLr9Pb70jUWxFRoZiTH8OQmFh8AbpCAQ-ZxlDRjXZBuao50pXIXhsd3pJaH2RMjmjAPVNYYYKIvivkqaGhL4Iq8wO4GxVoMT6ly8u1f2QUhwzdFVMf3bsEzStmZHMDayzlrMgmf7POZNwsybRg-Br8DAXsG7N-_Xu41nrcVA3FSgTc1YDaK_DyLUslrZn-8Bp6FE8pv7l5EBFCqNed7xDn-29WHwMslGqfZQYteD3hD8kLA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">روایت یک جراح از سلاخی بی‌صدای سیستم درمان در روزهای جنگ</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5694" target="_blank">📅 20:03 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5693">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">‏بیانیه وزارت امور خارجه ج‌ا درباره نتایج مذاکرات با جی‌دی ونس:
‏ما یک واحد کنترل درگیری‌ها برای تثبیت خطوط جبهه در خاورمیانه، از جمله لبنان، ایجاد کرده‌ایم.
‏یک کانال ارتباطی اضطراری (هات‌لاین) ایجاد شده است که از طریق آن در صورت بروز مشکل در تنگه هرمز می‌توان با ایران تماس گرفت.
‏یک کارگروه درباره پرونده هسته‌ای تشکیل شده است که بلافاصله پس از اجرای کامل بند ۱۳ توافق توسط ایالات متحده، کار خود را آغاز خواهد کرد.
‏ما با قطر توافقی درباره آزادسازی دارایی‌های بلوکه‌شده ایران امضا کرده‌ایم.
‏ما اسنادی از ایالات متحده دریافت کرده‌ایم که به ما اجازه می‌دهد به مدت ۶۰ روز نفت، گاز و محصولات پتروشیمی را بدون تحریم به فروش برسانیم.»</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5693" target="_blank">📅 15:00 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5692">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">‏نورالدین الدغیر خبرنگار الجزیره در تهران درمورد نتایج مذاکرات سوئیس:
‏ایجاد سازوکاری نظارتی درباره لبنان با نام «واحد نظارت بر درگیری» با حضور لبنان، واشنگتن، قطر و ایران
‏· به‌منظور تضمین بازگشایی تدریجی تنگهٔ هرمز، مقرر شد خط ارتباطی مستقیم (خط داغ) برای مواقع بروز هرگونه مشکل ایجاد شود.
‏امضای یادداشت تفاهم میان ایران و قطر دربارهٔ اجرای آزادسازی دارایی‌های بلوکه‌شدهٔ ایران
‏· وزارت خزانه‌داری آمریکا (OFAC) معافیت‌های ۶۰ روزه برای نفت و پتروشیمی صادر کرد
‏· تشکیل سه کمیته (هسته‌ای، تحریم‌ها و نظارت) برای مذاکرات ۶۰ روزه/انتخاب</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5692" target="_blank">📅 12:38 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5691">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ax2rA8MSRUHlKBK243AfP-_VPyd1RlMuGMdWHxHvgFBPulegbk9Zv1Wnn6O8zJ5YT9ikD3qfOecEBNrT2GklxBAZTsScmrdiQHN4U1mJVlRlZO_Yw-073lwI1P6qkzy-m8b1ZNkKsiXIzKauT3XbS02RCBN_XH0qtvAfko28bs851aeAwlHob5zJNcw_3CGCnH9AhVfREoK7nAqn24-rwDd-uBMd6sZumZTplJ-uFsMTpeecD2UEf4Ndku2eurqbydv-7aaecHzAVC2cAS-DQImmAV62w8Y5k9WRDBccV_n04mTgYYWJalq2-ENVZCuQY0ynWWVRGGzz6z4QUroKeA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/5691" target="_blank">📅 00:01 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5690">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nmZqGqABac-Rcy0EeBmH7NVwKYTF6QVL3EDilG-B3aqU4hbtB-p0RYNExhQZ9V-fEFjsrSWk04osNDZm79lEd76K2-bYuhHiqzgghhvr44tWylTCkN-VSRojF8GtgJCl0_Hnqb8a6vST3E0Ni3afHC2TBjFFZ9lqiiOK-70OVBamFY_NfXjrv9UmlFPDiB7ZkUQolvG33Aq3jtnaCOO57Zls_oXux7or1ZfTcfEYgGGYPGFVVcrEMDpPPKQs___FkND3FMpGujonZE0BBjNi-ZBHPY9HaDYzF33PXT29sOww5oLQY6Xj2k1nL5bvro_jgdne29vU6F3DIGIncmXWpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
گزارشی از شنیده شدن صدای یک انفجار قدرتمند در دوحه پایتخت قطر</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5690" target="_blank">📅 23:31 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5689">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🚨
گزارشی از شنیده شدن صدای یک انفجار قدرتمند در دوحه پایتخت قطر</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5689" target="_blank">📅 23:21 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5688">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X8O-dW1TgrEfNwrDHpveOfHP2ZyIVWrCtyr29NUFiREnHboZXMsQHuChaCPR8jQRxhRS_1ASvyPrGUp6OIYyS6Hg3rn6f4MkLZke-dRWq07LBcWEDTfzb3ece1gSJDabyxQVvKKQXnEwDMYMEt-0tkk00F_z0tB1JgZ1kDOoaCnKw-LbwLYDMbc4xtM1DdYnM5SOUT0wwtK91RrCGPrxZglgt_O3RPs2Npfr5DfWwDEg_jokCDqFObBxRMG1IDExjxcdHxO7Ww4KWRg29lHefj5yatrwj3gujvpk-VlGAKUAV-hiW4v81HzhzTm1kDKO9GRDQAGLpbUAJm2VTeUy-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ورزشگاه لس‌آنجلس</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/5688" target="_blank">📅 22:55 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5687">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tGpF8P_6tBLSRrqYWkCNq1epXgwBxLqFYrKhfZnbOyuWuTyXoE9ZfpTNK6t31tfQhf8WXqvBdJQhj0K4T__yuS2hf4Wj6ABo9tdTIB3UMaw8xUtJZIJK7vhWM4yEQqx2VIk4Ta2AlepBRoYmq-_BnTwN7rOJX81IXcfbWCFgGCCYf_NXhist2RcE1K5u0i9C-zXKjIRAVEFInhiZlf0UyWMzNOawm7RCauT8iv-_Q1OSrP_i5FbAXHnf5JDaNTYAnEsxKtE3dnDSmxuX0YvPUzpD93xlr_jKHWQosMgq6QhGJk4t1b6OEBQrpIZZzXojXKwtcmAOWPaYkYXa7oWADA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پاکستان و قطر از ترامپ خواستن
یک توییت بزنه تا دل شغال طرقبه راضی بشه.</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/5687" target="_blank">📅 22:43 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5686">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UapI1IhEQtXEVaCR2bysAOuWAwmsjObKDhDF-Bto9oVN3AlmYoWSVTL4i5-GozMQ4N0L9gNZMoKFgnNO5elmT-u117WRNrNe8zw5qE9VWenppTJwmp2YT5-BNUZk7l7ZrHlYiAxRov6nEgqDoeUqAJ8ARkkcT3-iv_JyESA5F1KhfBvZouV7zeLTN2lu_cq0jLQiIcP_y0d5S9XXlTh2VFLklFLg_bEkY932kVVr-agvOxuavpFH1aNwnAcs8w5wR_MlmqHtEqz6vNvE0550rOo22iq9DIxEwi82t-7LM921-K9E6a5McyHI7bX_lrTMP5yrhkgz4j7REaqIMQ4AjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جی دی ونس و امام قالیباف</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5686" target="_blank">📅 22:38 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5685">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XH3G3cRaevxSNQKJRNs54_LPY1YzmGmcq1fRq5hNslmw7ZW-2UIjjN12YhS5ZeDnmt07VrzHDUwTXrUi-zXGedWR3wB1yXHX3qGNSgD6I_fL1ao0DiNhi8tou9E6kfBy2JAHXwBweX0gIz26Ov7hNsp0ytcKDoTAMrqC_rK3QNIvIzaisUrpIYuASvnCuM0Xtpjwci4Jd3zcoBPfc9tFtBLNjoZvv5JTsUmP-rh-6ir3aUDfVUvjBGHdsuoWnnInevhG17_g5xqSBtta0XcfpB3S1zrJtlznYYwZzRvr-B5c3jdzPBdjkNIdimdmobhoEMfOmD29saIoG3ze61glbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش اسرائیل از حذف «زکی یوسف محمود ابومصطفی» از اعضای تروریست حماس خبر داد.
او در ۷ اکتبر به اسرائیل حمله کرد و از جمله «یاگیل یعقوب» ۱۲ ساله را ربود.</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5685" target="_blank">📅 21:50 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5684">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TznVxKKIz_nR-TSboXjkxy7yoRH79lCexoAfuOA8T15NKiCXSc014fS7TWbDl5gRrbgt0XppckQoMNtYLTEhg5n4hUfoZ4LpPWM-IGs8S4E2O3QEmBPplpeQKmAr_kGfUG4q5Evtm45ycDnkAdcag-HCTv03s0ILWvFZ_0e-HBY84tEoRr5y5FFQJMQDOLOBbcqd4PtVHvkuz1SpQTkhtAAzECBiYjalIYmX3kPTpJBRxAlMnY6erwOrR2oPSF1GLQSrWajpePKdK2yFvVd9ua5O-jZku3ItzhQSweOkB4ZfEs_axXW8nJK1ST1FWDldNC6oo7F-1EA6DXic6rjWkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فعلا درخواست یک توییت از ترامپ دادن</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/5684" target="_blank">📅 21:19 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5683">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🚨
برخلاف ادعای شبکه الجزیره ، هیئت جمهوری اسلامی محل مذاکرات رو ترک نکرده!
پس از آنکه ترامپ  مطلبی در تروث سوشال منتشر کرد و به سران جمهوری اسلامی گفت که باید دست از حمایت از گروه تروریستی حزب‌الله بردارند و گرنه شدیدا بمباران خواهید شد،
هئیت جمهوری اسلامی ناراحت شد و پاسخ داد و…. و شایعه شد که مذاکرات رو ترک کردن، ولی ترک نکردن!</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/5683" target="_blank">📅 20:54 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5682">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EoaLpB8R0gqSmBlQZuQzMZdgb8sKDdVd2_wgRh9LlGR967WiW8fu14-73NRHwhIVn9VrqEBo9jVwzvoKMOpz1rmlv0NJ6tag1iL5bhso4btlU8Ih3UQ5wfFmte6NZ8BVlawR_8QGu-fQnTnRv7bWev9G1C9axp_7ylVvoIu73m6l0p-ob7TgCIeIG-qAFGwxRIdxTq3_j39qcbI_tgeBGsL4VQxpQyCePkZlmV46NlSLWpjkWTqj5RH3jUc2tYs-OhNiWRMYrBdnjYCudIITjbqdKfx5wKQ4Pp91mRfx7N9wnJVg0Mj6hZeeOD_BCkyrsBpXVTvtd46qQyPFbiMQJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس ستاد کل ارتش اسرائیل امروز به جنوب لبنان رفت و دیداری با فرماندهان نیروهای اسرائیلی در جنوب لبنان داشت.
جنوب لبنان تا همین ۴ ماه پیش در کنترل نظامی اسرائیل نبود!
حزب‌الله برای انتقام خون خامنه‌ای ، دست به جنگ زد، ۴ هزار کشته داد، ۲۰٪ خاک لبنان را داد و حدود یک میلیون شیعه لبنانی، بیش از ۳ ماه است که آواره محلات مسیحی و سنی و… هستند.</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5682" target="_blank">📅 20:50 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5680">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca65ce2ecf.mp4?token=OzEFT7Nupa9FanbUS-iEelE8AbmkaJpJUIT9tKSDk4rFx8u_2S6sOAVXhqt8E6HtyAjpDZukz5c2gdRE7Cj1C-ViNBZ6CUWKrTN06yV4WwzXACICmj5O86mOdRO7ElzGeHchG6OTIO72_Q72unqhGF87DtnXC0Myfcl5OpJCwEH81ffs1I4EehyTmONIneHw1vHAyc9UOzqzc-Mwam2pIWPP_LemmXwjo32bO6Yv2tsnaEtojxGv4JC2IQVSPl2nXjbJvprHmqmM88soXlBLjaPdYhf9AlOxGkOn56uVGmasuPeGNpvIfVgVYiVr_ff0gfUaC5yLCo6Oun3LyZPNLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca65ce2ecf.mp4?token=OzEFT7Nupa9FanbUS-iEelE8AbmkaJpJUIT9tKSDk4rFx8u_2S6sOAVXhqt8E6HtyAjpDZukz5c2gdRE7Cj1C-ViNBZ6CUWKrTN06yV4WwzXACICmj5O86mOdRO7ElzGeHchG6OTIO72_Q72unqhGF87DtnXC0Myfcl5OpJCwEH81ffs1I4EehyTmONIneHw1vHAyc9UOzqzc-Mwam2pIWPP_LemmXwjo32bO6Yv2tsnaEtojxGv4JC2IQVSPl2nXjbJvprHmqmM88soXlBLjaPdYhf9AlOxGkOn56uVGmasuPeGNpvIfVgVYiVr_ff0gfUaC5yLCo6Oun3LyZPNLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همین شب‌ها:
یک مراسم عزاداری در‌جمهوری اسلامی
و یک عروسی در غزه</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/5680" target="_blank">📅 20:42 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5679">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dGpS8Ctpni3GDnpvhM7iMhjRG98_xbuo4efcRx1_OmumsTUZui3ULlzsMZrVL4ogcXpOq563z4zF0R4OTgXShLMEJJqWbc99H5bOdrz4JvpRlw1QlGa1ngyyvbTRiwRIzevBFANo3wyf6wdnFaDVWp1tFy7ShYZVmlSYi9oAgygf3TlsDA2TmoWAWdKRqyS6wIcl5Md7M8YFP4cz8xt83rNn5vFckGv15nlJJTMV8a-HuYu8lCavllAtFAn62FXSa7xbUYQE5wvF6E6JYGqbyaGWqY3DecTNTReBeeR_iRYf1OBCNsqAgnd3tA0FqEJHtmyUcTnUKoUMejRrLTnCXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینها رفته بودند مذاکره برای حل مشکل :)
در حالی که تا جمهوری اسلامی جمهوری اسلامی است، مشکلی حل نمیشه.</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/5679" target="_blank">📅 19:42 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5678">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd078eea01.mp4?token=N95_5ejjOiDTwHv8nP32QUGxDcPKGjrGOfBSAGaHzS2HYDxjKR3n15RpT3KUWBFPJEKIYpNwGQaSX_EGhZHv8JJjJ8R8QLnT-Xt9kg9uyAeqXO-FAbcFN7mN_G--AvvMKF-hj-MNREWLjbiIpi3lLpqi0z6KdYtvZ2jQNiEc1PgT2a0UOjcIhu0AVPY9YSa29DyOIjAa34VVlfKn7kwliCU7f-o__Z6dRxe9WhntdwlaCyS2QJSMnpJdoHTMM5BfoiGYdKzkg4W1U1Wj9v70F9nVkHgIpyrYgCE4mplbYvo6DyYgMuLhc_pPmywCVX53fTCMbbrYuP0An_2uAs-Drg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd078eea01.mp4?token=N95_5ejjOiDTwHv8nP32QUGxDcPKGjrGOfBSAGaHzS2HYDxjKR3n15RpT3KUWBFPJEKIYpNwGQaSX_EGhZHv8JJjJ8R8QLnT-Xt9kg9uyAeqXO-FAbcFN7mN_G--AvvMKF-hj-MNREWLjbiIpi3lLpqi0z6KdYtvZ2jQNiEc1PgT2a0UOjcIhu0AVPY9YSa29DyOIjAa34VVlfKn7kwliCU7f-o__Z6dRxe9WhntdwlaCyS2QJSMnpJdoHTMM5BfoiGYdKzkg4W1U1Wj9v70F9nVkHgIpyrYgCE4mplbYvo6DyYgMuLhc_pPmywCVX53fTCMbbrYuP0An_2uAs-Drg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b2464c582e.mp4?token=Yl5EplAcCX7xb3R1FncUJbrm5FQlx0p_yZmdsaoDB3j5lo89CPmWkNq1nRXqNCd3uylnGpyFvj2HpoHbMQIFLOD1QYQsQRkjKfXD6Q8oryVvs7MOxCrVg719GavnDpAmeMD96pJixyH2mhJjMG8KjYb36JS2Brh4Nup-gO-yU4glRoV_AgjN7L5zMvAd4nD0axUksPf-1lsQIDJkMwO26KkwGacWEiprIXmAb18TlSzeKmkkWkG1Vi7J8tuAWFsweNoSgfBreETyXZyO50OKUhc2mMJ5Wm5hI5G11IcHgu6AhUfD2gTqeLrhkgOCjuJEKPnyEvrhdvuq7Rb9FeRhsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b2464c582e.mp4?token=Yl5EplAcCX7xb3R1FncUJbrm5FQlx0p_yZmdsaoDB3j5lo89CPmWkNq1nRXqNCd3uylnGpyFvj2HpoHbMQIFLOD1QYQsQRkjKfXD6Q8oryVvs7MOxCrVg719GavnDpAmeMD96pJixyH2mhJjMG8KjYb36JS2Brh4Nup-gO-yU4glRoV_AgjN7L5zMvAd4nD0axUksPf-1lsQIDJkMwO26KkwGacWEiprIXmAb18TlSzeKmkkWkG1Vi7J8tuAWFsweNoSgfBreETyXZyO50OKUhc2mMJ5Wm5hI5G11IcHgu6AhUfD2gTqeLrhkgOCjuJEKPnyEvrhdvuq7Rb9FeRhsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دور اول مذاکرات به پایان رسید
شهباز شریف نخست وزیر پاکستان یه میز برای کنفرانس خبری و نشست آماده کرده بود که ج‌ا، آمریکا، پاکستان و قطر اونجا باشن،
وبی عراقچی گفت نمی‌تونیم اینجا باشیم!
و ننشست و رفت!</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/5677" target="_blank">📅 18:56 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5676">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WaFKcKqkez6zyLsOz5wozIZ7aOB2tfASOkbXzEsO9RymkcaGUBRriuT3lFLDdvNGNd8cfDpcOFK4E6NYHi2QHadpID3EizfGZA-2_oTsiaPJKjJaQ-_LJqQI8Df1cImt_p9T_xxQMYXRKm2oBedNoGNLV4D0SMYKxzvb6SLCYCxX1RYeeF_wwlGeeolHhPpNfiDMWWSgxz8pHh3tX9LQVP5Fjdcqm2QnQh6TaMNQjp6PLleZ9JaRBsTSmZzAEOi-luciSYj_8bMqnFactQl2ZSXagurMfaKCU6YSpcvncjEjT84R3wF44xi9wt0uIML4urcWWv6ugmcLXSoVkshgVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/5676" target="_blank">📅 17:07 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5675">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7b14c3d6d.mp4?token=QIczHKPwTnY6way0G4MJjw4DxksuCh4aeRgO9QqyKr2EslkzaFAq4hbf8FzPJ6EgZme7865ctG2rUqD_F1mE8dzLR-wDLPrLk8hLUQap6zBixEYW-7rmDk7ExHDZMIn6_-oxIassh7jpj210qqz4KOTD-javyu0ntZoPvlgRYa99_naZfD1F_AgPFkwaYLgWiIo5gVm_7Z4qfgDp1mtykbEIYUQRdd1ebsnRMMgME11wEJmAUCCxXTdTygApLX_kyC4ykm-EgmIAridNU3Qyq21m5DZFRDWfD7OZ-L2T-RgelTS-o5mKZVb6V2QkqdQZzTOPl0NXXBQHFkVvmTJMWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7b14c3d6d.mp4?token=QIczHKPwTnY6way0G4MJjw4DxksuCh4aeRgO9QqyKr2EslkzaFAq4hbf8FzPJ6EgZme7865ctG2rUqD_F1mE8dzLR-wDLPrLk8hLUQap6zBixEYW-7rmDk7ExHDZMIn6_-oxIassh7jpj210qqz4KOTD-javyu0ntZoPvlgRYa99_naZfD1F_AgPFkwaYLgWiIo5gVm_7Z4qfgDp1mtykbEIYUQRdd1ebsnRMMgME11wEJmAUCCxXTdTygApLX_kyC4ykm-EgmIAridNU3Qyq21m5DZFRDWfD7OZ-L2T-RgelTS-o5mKZVb6V2QkqdQZzTOPl0NXXBQHFkVvmTJMWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جنایت‌های جمهوری اسلامی علیه مردم ایران</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5675" target="_blank">📅 16:58 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5674">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A4wVDZ48O40VTMvswYyqt_tmAyJG69Pf-VWUq4lwqEkBRgNdag98no4T8RqRYb_Cwi-BjhWxCLEMgwPlwgZbPjM5SNitbW7GTXoWcDsUiAUqlZGxLuErpHJeLNuPNkYmfpfUnopML5nNdoARpBLaWPVtdCXviQeODkci5wXhzpbZMGX5mjVcMO5A5OM3gbiSzAzszjQVZhRJ67CVabiRJ1OaPpHiE-EKViAvoqvHBMozgAc_FxU4ogJbBtNxFDTDf0nxNnXq69hhu1xVoXP9cyetOCmm5Yqb0ZVD4rhsXmC47fOdW036dPbbs7sVsv2GN_IMtzXPoTMiOP-DkdAf2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپِ کیسه دوز به فاکس‌نیوز:
«آمریکا می‌تونه به فرشته نگهبان تنگه هرمز تبدیل بشه و ۲۰ درصد از نفت عبوری رو برداره!!
اگه لازم باشه، ممکنه کنترل تنگه رو به دست بگیریم. آن‌ها رو به‌شدت بمباران و نابود می‌کنم.
اگه توافق نکنن، از کشتی‌های عبوری عوارض می‌گیریم.»</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/5674" target="_blank">📅 16:53 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5673">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HdFUk1EClWFxKQL4yR0Z9UFkB5aXaWSfKHXTo2nQwAKF8rz0UcW_GAFyujAiw64N69vpVbJNB-lDep-EfJRPcxSE2yxNK-FOiuGuJ2Z5_Zh-N-aHf60gkAO6nNRrjmrwUer1IsJOvp9nTdHVazd2-hdTJWER2_5WhlEFQkn7jJpEWCIh769S3SZm6Qa-X4mXsE1MVpRlsh55wZtfv4c7OgPpd9s6Mt2sk6k4LKHB_soqDRq1dcAUGl0qe61VRhsRfje61F8qtvGddEiZG9HId974yMJOreLWzacnYCfLZO1gLVCFpAPWZstIQZRFraei7o8FdrS3VcSCB2LrsOvalg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">جمهوری اسلامی سالی حدود یک میلیارد دلار به حزب‌الله پول میده،  در حالی که  بودجه استان خوزستان  امسال  ۱۴۲ میلیون دلار  بودجه استان سیستان و بلوچستان  ۱۲۶ میلیون دلار  و بودجه آذربایجان شرقی  ۸۴ میلیون دلاره.</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5672" target="_blank">📅 12:46 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5671">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/euEXeDkfNBabLgchQ6-FSwv2zEtvaKnfQW8CEF2ywgp3oRVk2sRgatKdLGF2rN1cHRvoVEXwNu9ujRuosc4kDmQ_rEl-koHaOAkEcgPe9d1btfv0rel6FEjI7aScC82Rx59D9NZs5DXJkTeRECw6HHdoXYVrWHdVFng1zT-twoRzZKXA_t45veJ8pG98BzHzMX1bntgg9pddS4B2mYv4f-vZcmHT4cekbIld0ttAj8V38CB-mPiWTAe072x1Z-mEgHp9dRfabTw_xinVSsfoE7ZfFNXAsBDxa9lAZAA4oFVJycdeHF3pZtHj95aNqY_SnJ71cVPjbczq16m3aT2y6A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/idjuJK7rE5QZyVqch7kL9B-sOX4lAnh6cSKYYSunO5830-ttixi-lHi7qP-r-YwDevzZAb4ziNPuf6mNj95fQbYyLMFM_xF-MWe_jLRLCD9PelJNBfMafUqvM5GGrTNO0_rlyY8SsbLQnZBXU5bVAjn80zNvT-zWf2pXZMqpn0dAdRq94LXhMCxKje14vOkIMUh0x119Kc_jXehRfXIJuPNRQ0tcAIDN-7MCzSv2GlxGy7oLDBaLx51z5nGpnb8E-Se4tcXEDIQUucoQOgVFFmTd5_XiJNtSSqWPOc8FhhOVXbh52WsuJc5NTG2c1cwzws_yhWd3u1Cq_4d4Yu7d8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امروز - جاده منتهی به فرودگاه بیروت و تشکر از جمهوری اسلامی برای آتش‌بس در لبنان.
دولت لبنان و اسرائیل درست ۳ هفته پیش
یعنی در ۴ ژوئن به یک آتش بس رسیدند،
سپاه و حزب‌الله سریعا بیانیه دادند و مخالفت کردن! چون نمیخواستند دستاورد
دولت لبنان به حساب بیاد.
در این ۳ هفته ۵۴۱ لبنانی دیگر کشته شدند
و بالاخره پذیرفتند!
حزب الله پول و سلاحش رو از جمهوری اسلامی میگیره، نه از دولت لبنان، برای همین این دستاورد هم باید میرفت برای صاحب کارش!
به قیمت کشته شدن ۵۴۱ نفر بیشتر!</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/5670" target="_blank">📅 11:24 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5669">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/228de5708d.mp4?token=cDi2Y0Gpjjv7vTYPsUVe46-fxxlo2B-47dlB_s389f42dXOXfjKUuSrLfvz1rbpxzyX5RAJY7REO2dRuzp0qcCd1Yraaej7guUVHHEEfBRnX7vRLfQODr9iMTnSh_GmruDHqghJerZ8sYXELB3zjNsFoWgfjDkwYx4BUy8GTnjkQnXq8B1oq5Ex5M8J4KJSFXJQFdEDUham8cZ2GG6k7kflAHz_e--5PgQ5FP0qiYoZ84NPlqwRMCA-se3w1HOSqfhPjQtXicixmeoBxKXJXAgW9uCZd0wg5bAr0CVEyfg7eUtPKkMudWrz7pXZZCm1zJ7RxqutHVHTXYgBsTtQhGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/228de5708d.mp4?token=cDi2Y0Gpjjv7vTYPsUVe46-fxxlo2B-47dlB_s389f42dXOXfjKUuSrLfvz1rbpxzyX5RAJY7REO2dRuzp0qcCd1Yraaej7guUVHHEEfBRnX7vRLfQODr9iMTnSh_GmruDHqghJerZ8sYXELB3zjNsFoWgfjDkwYx4BUy8GTnjkQnXq8B1oq5Ex5M8J4KJSFXJQFdEDUham8cZ2GG6k7kflAHz_e--5PgQ5FP0qiYoZ84NPlqwRMCA-se3w1HOSqfhPjQtXicixmeoBxKXJXAgW9uCZd0wg5bAr0CVEyfg7eUtPKkMudWrz7pXZZCm1zJ7RxqutHVHTXYgBsTtQhGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در مظلومیت شیعه …</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/5669" target="_blank">📅 11:07 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5668">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd9d936798.mp4?token=vEvtBkeiU321j1zgqhOdPLnP9IbSefnyK3DGcyhbMC1sm0Y_d53dWetIKwN9Oi8WJQiYqfT8QOOlIRG3HikwJu_TjTeVE6H2sKi2uPRmKR3un3C8Rayv23xujN_qu75I76oR5mNd-xOpgciELiP5WOyeRmV1r2v3zR6BEoOYxpmfoxSP5DJ0EsElZjN2HGp6fMXllesvG6oLPqkhiJn1I3dqyGeDfcMF6N0JGPX9s2AU8OOqHyngOg0AilQ4ns4NW8sN8-pPgmZGNi3qqk-HhCcOC4kHUC8xtWB4dCtkXI3tYhczIUNC7FRoFFyShi85Ud_iVhJnDTlEnXBEG6v1-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd9d936798.mp4?token=vEvtBkeiU321j1zgqhOdPLnP9IbSefnyK3DGcyhbMC1sm0Y_d53dWetIKwN9Oi8WJQiYqfT8QOOlIRG3HikwJu_TjTeVE6H2sKi2uPRmKR3un3C8Rayv23xujN_qu75I76oR5mNd-xOpgciELiP5WOyeRmV1r2v3zR6BEoOYxpmfoxSP5DJ0EsElZjN2HGp6fMXllesvG6oLPqkhiJn1I3dqyGeDfcMF6N0JGPX9s2AU8OOqHyngOg0AilQ4ns4NW8sN8-pPgmZGNi3qqk-HhCcOC4kHUC8xtWB4dCtkXI3tYhczIUNC7FRoFFyShi85Ud_iVhJnDTlEnXBEG6v1-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عاخی … رهبرشون تنها و مظلومه!
یه چیزی درخواست داده که هیچ کدوم از سران ج‌ا، جز جلیلی! بهش رای نداده!</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/5668" target="_blank">📅 10:32 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5667">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ff3016eb3.mp4?token=bQAWGID21Jy4qpzAVwIs69_gfkbF8WTet_lO-IopV0MgvaF1A0jXzkH6eAei854hG0EejAtR6g-E4d1UOg6uogGdwR6AFa6ti1u1Etbvh2JmPlyFjaM3RYB607eUvIQFPgufYX-w-jtUnbQh7cmSeBAPpJMhXrEu7MZTSMY7nqYzvI-8Nex2YJfTB0RA2ooIm_oOFL1-3F9Ldso2-qnjISNbnzExqHtvHHizTXRwDRosEVO6KUEc85KtUEH4nW0yzJtMDJ6CC1HMgaYhPUD2UnLqlALRqfu8cjIdqykmltxgvRpxvmC3ZipEVmN6IJinv2y5TS88IbYUNcKJYlK7Aw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ff3016eb3.mp4?token=bQAWGID21Jy4qpzAVwIs69_gfkbF8WTet_lO-IopV0MgvaF1A0jXzkH6eAei854hG0EejAtR6g-E4d1UOg6uogGdwR6AFa6ti1u1Etbvh2JmPlyFjaM3RYB607eUvIQFPgufYX-w-jtUnbQh7cmSeBAPpJMhXrEu7MZTSMY7nqYzvI-8Nex2YJfTB0RA2ooIm_oOFL1-3F9Ldso2-qnjISNbnzExqHtvHHizTXRwDRosEVO6KUEc85KtUEH4nW0yzJtMDJ6CC1HMgaYhPUD2UnLqlALRqfu8cjIdqykmltxgvRpxvmC3ZipEVmN6IJinv2y5TS88IbYUNcKJYlK7Aw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd300c19c9.mp4?token=pv538EZdGJQR-Wbqzavduzo3RavZebcngSFp4AbwR4kooxzHxvPOzwfJTRe0AL--YfTM8GoXW-oJBrkZaccELvt27BEW0wzxyzo2lSKluSlpmo0YpyihzofdqHq2W1uQRhMa0FCJIdSMdeKPIH4hx4bC2u5Zk9hXLBruz6f6ECifmk46PTZa_m9TmBBYZqQGMXSW52HBluxxcknXpSUUZGp01r5zws7ug1maJMGyTB-xuXW2uDacQSg13CXRdmPdSUSRyYK0GyT9GJVLr5Mp-aaHRZCzUnXjwGPPYID0qLps08zBQ6Ous0LQ7Yf0VAwuUCYEKX7f4I2-9cfCBF4ozD8ikR4lyZTspZi3QYQIayUD7M_cA_wjeuN2yciX0lci9ewsDb4GM5sHfzLmNS3PsRkOJq_lJj-XETqfoHAfauqebUinAyk_4_5AgA2C9XRG2JY3OpBIvt3kUOCqNk_S29x-zjvR_k3vDHgemiQDACo2oziw3Me1o-XoW1pEeNrtvsKgoIjegJHiQQxuVaWnZDRbpp2a8tSjreIbcsE82W5XBOj7uNbRmwFN2ayDR4PxCj18SBilOJQPYrTv95RGS-R3mLO3MUi0A_BYALIAZh-PallRWc5v47hlI-eX7cmeym8RGx1Q3Gpk8K9J7gHk0cKOCNpd17nWM3H4POn37Sc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd300c19c9.mp4?token=pv538EZdGJQR-Wbqzavduzo3RavZebcngSFp4AbwR4kooxzHxvPOzwfJTRe0AL--YfTM8GoXW-oJBrkZaccELvt27BEW0wzxyzo2lSKluSlpmo0YpyihzofdqHq2W1uQRhMa0FCJIdSMdeKPIH4hx4bC2u5Zk9hXLBruz6f6ECifmk46PTZa_m9TmBBYZqQGMXSW52HBluxxcknXpSUUZGp01r5zws7ug1maJMGyTB-xuXW2uDacQSg13CXRdmPdSUSRyYK0GyT9GJVLr5Mp-aaHRZCzUnXjwGPPYID0qLps08zBQ6Ous0LQ7Yf0VAwuUCYEKX7f4I2-9cfCBF4ozD8ikR4lyZTspZi3QYQIayUD7M_cA_wjeuN2yciX0lci9ewsDb4GM5sHfzLmNS3PsRkOJq_lJj-XETqfoHAfauqebUinAyk_4_5AgA2C9XRG2JY3OpBIvt3kUOCqNk_S29x-zjvR_k3vDHgemiQDACo2oziw3Me1o-XoW1pEeNrtvsKgoIjegJHiQQxuVaWnZDRbpp2a8tSjreIbcsE82W5XBOj7uNbRmwFN2ayDR4PxCj18SBilOJQPYrTv95RGS-R3mLO3MUi0A_BYALIAZh-PallRWc5v47hlI-eX7cmeym8RGx1Q3Gpk8K9J7gHk0cKOCNpd17nWM3H4POn37Sc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از دوربین جنایتکاران جمهوری اسلامی
قتل‌عام مردم ایران در شب‌های خونین ۱۸-۱۹ دیماه</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5664" target="_blank">📅 10:05 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5663">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/845f6aff27.mp4?token=B8mxi7_0GplMvdJQS3phbYaw8QZGWcBrzt2MraneEDdrWwO0c4M4iaIB9JAbCZEuhUIAurjAIp4Ib1A3D8HKcPuZYNT03sX1AhmbYdvxGbgY9pk8IX6ZMFFzCtnU8o0TqJIk0vAGoTp39jJefZG3BKPdvehgKr2J9hNl8wiFWBRBO6FdMSMKdLblb54io0fFlKBTll_LSKYg0-8y3StY8NDFe2dw9hfBBmuHvWA4d5LV-jURg_fSu6h0UKKq-iWQoyKR_aQKleasgDYVqI7hLX5LrnNy54QuELyt3rtrey-9W9gz-r1iNuq_74hdZyqs0ecohbuC4DnCzNBfp77xjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/845f6aff27.mp4?token=B8mxi7_0GplMvdJQS3phbYaw8QZGWcBrzt2MraneEDdrWwO0c4M4iaIB9JAbCZEuhUIAurjAIp4Ib1A3D8HKcPuZYNT03sX1AhmbYdvxGbgY9pk8IX6ZMFFzCtnU8o0TqJIk0vAGoTp39jJefZG3BKPdvehgKr2J9hNl8wiFWBRBO6FdMSMKdLblb54io0fFlKBTll_LSKYg0-8y3StY8NDFe2dw9hfBBmuHvWA4d5LV-jURg_fSu6h0UKKq-iWQoyKR_aQKleasgDYVqI7hLX5LrnNy54QuELyt3rtrey-9W9gz-r1iNuq_74hdZyqs0ecohbuC4DnCzNBfp77xjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمزه صفوی
فرزند مشاور ارشد خامنه‌ای :
در ۴۰ سال گذشته جمهوری اسلامی همواره سودای ساخت بمب هسته‌ای رو داشته و تمام تلاشش رو کرده. اما برنامه‌هاش لو رفتن!
جمهوری اسلامی پنهانی دو سایت «فردو» و «نطنز» رو پنهانی داشت جلو می‌برد که «لو» رفتن!</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5663" target="_blank">📅 09:51 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5661">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f28d8f2fab.mp4?token=oS4AEld2KObnjzJIBK1uyZFeTLBNMfuJzkvBkTPX2kcqCEGvBpDkNBBZbrFUftWaDjQxkkmjjjPry1N_dZXb0pFrAolRve31V588-2STOQ9je3OaMNQEMuHuZpbJP4uQXhswCOCE0Xbg0YbHvTjJUQd788RNXGf5etstbN-aq6YhPJk0v9GkxVc46Qq5uZDm9pxZa-MooO9a6lK-y2IW02H1iWpAR4EV1fbgQqyO8g_iUwWyXSw7PH7i38BA5WfBfR6sHqJmI0Qi-x58Q1LKjhI9_yeHEQIz2q3Ea4WZtqzdU5j4Lk9uHDvWLTL10y6W5NPjM9lG0yiu4Sa1FQZHVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f28d8f2fab.mp4?token=oS4AEld2KObnjzJIBK1uyZFeTLBNMfuJzkvBkTPX2kcqCEGvBpDkNBBZbrFUftWaDjQxkkmjjjPry1N_dZXb0pFrAolRve31V588-2STOQ9je3OaMNQEMuHuZpbJP4uQXhswCOCE0Xbg0YbHvTjJUQd788RNXGf5etstbN-aq6YhPJk0v9GkxVc46Qq5uZDm9pxZa-MooO9a6lK-y2IW02H1iWpAR4EV1fbgQqyO8g_iUwWyXSw7PH7i38BA5WfBfR6sHqJmI0Qi-x58Q1LKjhI9_yeHEQIz2q3Ea4WZtqzdU5j4Lk9uHDvWLTL10y6W5NPjM9lG0yiu4Sa1FQZHVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5661" target="_blank">📅 23:07 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5660">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W36gobT7i9NnWMMk4gUm62SEcjBGjkxrpltNBeHO3NqUSN_MQsqerU8em7TteBlgWg86EYxlhAXYQxrmOXAE52Y_alvmhDhBlWzYMiFv7mU2upeln1hS9i3kB_PzMmv-Xx3UW_EUsuDdkIbERPYGBnwJB-JdiRs49hg1IjwfzONwZanNt49BVDJ27Nwawqe2IJEDwdFhlAUVsKtvpRVpqWGi2lomYc5kRH_c3VLLteq_JzQ5qTDXIIevAl2dhMJIjZaUYfRha7zNAb69yItuTSbEXurjWbCxzR0FEQHW3v7tEAwFXZI0UdbxQvMq5eMLKUIATiEnb-UQQgFsPV0MKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/5660" target="_blank">📅 23:07 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5659">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9adbaa46b5.mp4?token=CEqndezT6k-W3rNhVrfRYv0NCqGEqNBrzP1SlC-lkHs_Up2i-Xi2xlOZe_Smao-lXbQ6fpy7Xmov-552rDyv-qITRbyNhXyvwBx2ALfxYahJSp1rcawe2Us_F8QiDZOZB_mM7acnR-28MxiOmOJgwNCV27NcZpkHVZ4J3lvCGwMIZUQBQlPQvsU65FONYwaC6OEq-W8BQLMrCvPFz9L2cBPPufktSAi_gdUMa1gPSFraahbKlMlKHxbvg9BsILICjZOdOyIsdm7Cq9llsxBQJ6siBDCIzw4gCmMjFGGCvuu8T-kDkjuiMXmrLAYq_3G16-MvvwlEqbuBkixlaInMfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9adbaa46b5.mp4?token=CEqndezT6k-W3rNhVrfRYv0NCqGEqNBrzP1SlC-lkHs_Up2i-Xi2xlOZe_Smao-lXbQ6fpy7Xmov-552rDyv-qITRbyNhXyvwBx2ALfxYahJSp1rcawe2Us_F8QiDZOZB_mM7acnR-28MxiOmOJgwNCV27NcZpkHVZ4J3lvCGwMIZUQBQlPQvsU65FONYwaC6OEq-W8BQLMrCvPFz9L2cBPPufktSAi_gdUMa1gPSFraahbKlMlKHxbvg9BsILICjZOdOyIsdm7Cq9llsxBQJ6siBDCIzw4gCmMjFGGCvuu8T-kDkjuiMXmrLAYq_3G16-MvvwlEqbuBkixlaInMfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">غزه</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5659" target="_blank">📅 22:34 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5658">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kuzEDOZ0aPOp0TGtBqTsXpiYSBhVsPxu2PipkKUP78ugmII79UThh9OMR2WhuI8145E2pekQlE0kJLFsRELSByWa4j7_aAPaqOMYKkZjHFMVggQUMHEmJZdUXx72nkk-m62XYpPO-4ZCwmpJje-pnu4-BXC6fs0k2DjI3iydK8kLEwgc18JkVUHRcxS1aAiWWYxq9Thc2sVBYoMvPYiqIrAG3IWPUdt0RTzt19a6DpCFiewGO1wJu4Qw0zjQ9x37MUObBRbg6UBMx-NfqBCb6I3pMMwGQHnB6QjMX80B5VxT2QSXi-UtGW3M2yhk8PFoNlGhZSFxlool-WBqkd4f6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش اسرائیل حملات را متوقف کرد
ولی اعلام کرد از مناطق تحت کنترلش در جنوب  لبنان بیرون نخواهد رفت.</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5658" target="_blank">📅 18:43 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5657">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZK7SbKACqoxDIlEwnN0DWWPTEeDwVTJxlPOeL-MWbZtAWbaff8zXLVyyDmV10JoyUa46ooOhwUCG3ElaBY-OCpHadk06d_DIqw5H-vrDphH9na8nUqVEN5CMlHqcDbHnpWMK5wiEh5Ar2ZgIjfKTo9UujDht8pdzy4aMNjN-oBji_NBC56k-A91OL6eBHchq4_AA6iAeBDoqehKaazSXXi7aGmAnC_RMRK-LETwf7ZS8PZXQ7oKpUcnf6TGjgo9rfAseaCKl-Fi9UJ-rvGFkk3TpDw9WXT-Nrjwb3dSk9gPXMf_anVZzlkIflUalt7g9QebLhu22AvqrWtIK_gQdeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در واکنش به جمهوری اسلامی :
فرماندهی مرکزی آمریکا، سنتکام،   بسته‌شدن تنگه هرمز را رد کرد.
سنتکام : تا الان ۵۵ کشتی تجاری با محموله‌ای معادل ۱۷ میلیون بشکه نفت از تنگه عبور کرده‌اند و نیروی دریایی آمریکا هم در منطقه حضور دارد تا مطمئن شود این مسیر همچنان باز می‌ماند.</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5657" target="_blank">📅 18:14 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5656">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">جی‌دی ونس در خصوص لبنان:
من فقط می‌خوام به مسیحیان لبنان بگم: ایمان‌تون به عیسی مسیح رو حفظ کنید و بدونید که در دولت ایالات متحده دوستان خوب زیادی دارید که برای برقراری صلح در منطقه تلاش می‌کنن.
مشکل اساسی مسیحیان لبنان، یا دلیل خشونتی که باهاش روبه‌رو هستن، اینه که حزب‌الله، به‌عنوان یک سازمان تروریستی، عملاً در لبنان مستقر شده و اونجا رو پایگاه خودش کرده. گاهی از خاک لبنان به اسرائیل حمله می‌کنه و طبیعتاً اسرائیل هم در دفاع از خودش پاسخ می‌ده. به همین دلیل، یک درگیری دائمی و فرسایشی ادامه پیدا می‌کنه</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5656" target="_blank">📅 17:19 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5655">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🚨
🚨
🚨
جمهوری اسلامی در حمایت از تروریست‌های حزب‌الله لبنان، تنگه هرمز را بست.
اینها دیگه راه گردنه گیری و گروگانگیری رو یاد گرفتن.</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/5655" target="_blank">📅 16:42 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5654">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/11b10561df.mp4?token=gIUxZb6icyz8ouydAQB4aMyXemStmkfLjh_0WUWD9DCMtqlbbBa7-Z5OP_QH1fdvDQCbWy199JFthZbUl7kiBMPnuWmCn8j1I9MF70G917W_C7eg_wL1DuLOXsC3_BNBNdj8QsQbBFTSNxhM4PT-RyBCUIgmmzL1JIdJiysO44y6h2x34Af4QPp3_rxsJKqCg-CqZaFuYb0e1hfOybHxZx7ooeaWFxr6zRWh0390eQADbc24ynBJoCTo2i1Nbq7Y22WTtomrJKtZLxnKv_y_dEzwLU4zWYOxDq7DiKw__bLygrEYs8wExMsCszh8UAahmS8KMA_DTGyXzwuFI7yitg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/11b10561df.mp4?token=gIUxZb6icyz8ouydAQB4aMyXemStmkfLjh_0WUWD9DCMtqlbbBa7-Z5OP_QH1fdvDQCbWy199JFthZbUl7kiBMPnuWmCn8j1I9MF70G917W_C7eg_wL1DuLOXsC3_BNBNdj8QsQbBFTSNxhM4PT-RyBCUIgmmzL1JIdJiysO44y6h2x34Af4QPp3_rxsJKqCg-CqZaFuYb0e1hfOybHxZx7ooeaWFxr6zRWh0390eQADbc24ynBJoCTo2i1Nbq7Y22WTtomrJKtZLxnKv_y_dEzwLU4zWYOxDq7DiKw__bLygrEYs8wExMsCszh8UAahmS8KMA_DTGyXzwuFI7yitg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اوه ا‌وه خیلی دارند بدجور میزنن!</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5654" target="_blank">📅 16:13 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5653">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5130bbfc36.mp4?token=e8vCtFBJHKPlimKKYzbyyTV6iw99YEUjNvwGiVUnIFtGHpUmaHIbYFooMgNF6-AApQsI_EgiXF-kosdFCTeh6CdRig0aN5LfPMkOALqQFTIYE-bnlHMWca2lDw5H2AhHgKemPk5YnB3qpWHQQ2veMVhmlOtxi97xciN4fonZXBK24ekAG0YOzB6IRTVrb0WL4hz4y0MGLoN9PJdBgMWkTyrHCBipTd6TL1iTTfFijrItIq5HIYKI3kY7xnuQU0eUsFi-t-2IqF1bshBCpoT_H7OzQ1JoQDFQaYEYfLZUyLB_DUU449z6DAv5orubBAuY_4xFbyu0pilNUmesH5B0oQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5130bbfc36.mp4?token=e8vCtFBJHKPlimKKYzbyyTV6iw99YEUjNvwGiVUnIFtGHpUmaHIbYFooMgNF6-AApQsI_EgiXF-kosdFCTeh6CdRig0aN5LfPMkOALqQFTIYE-bnlHMWca2lDw5H2AhHgKemPk5YnB3qpWHQQ2veMVhmlOtxi97xciN4fonZXBK24ekAG0YOzB6IRTVrb0WL4hz4y0MGLoN9PJdBgMWkTyrHCBipTd6TL1iTTfFijrItIq5HIYKI3kY7xnuQU0eUsFi-t-2IqF1bshBCpoT_H7OzQ1JoQDFQaYEYfLZUyLB_DUU449z6DAv5orubBAuY_4xFbyu0pilNUmesH5B0oQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a19f9c1ecb.mp4?token=sfMPIiZ0LksuS9UuNyjCQbZNKRk-ADUpfROknWKEHX7GSW80VRLqFRfDt7htq2171zmfeosNr3u0c6SGTrOraj_PZT3W7q2Yhr_i4bNLAS2tWnl0wRgY-CG0i9Ob8H9N9E029xOlHJ-xw6RmrndfCR6KdIdpOJxVuuAkTg8b9QZ4KpXPQc_xj0J94Jm5jxqTQSY1ol6QgLe0AuPGpq4JDaWZsV2ddXsISXBe4wbxEvWG3fYHVGnbP_Q1KQzHNGeK1gf7vtY-6P0bj4Cf1QATW5Oop7aiUwGGTVXFJT78pMumL9vRhJx5mFsLbxlSNIGcbY1yY8U0G52HBv7kQWzE3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a19f9c1ecb.mp4?token=sfMPIiZ0LksuS9UuNyjCQbZNKRk-ADUpfROknWKEHX7GSW80VRLqFRfDt7htq2171zmfeosNr3u0c6SGTrOraj_PZT3W7q2Yhr_i4bNLAS2tWnl0wRgY-CG0i9Ob8H9N9E029xOlHJ-xw6RmrndfCR6KdIdpOJxVuuAkTg8b9QZ4KpXPQc_xj0J94Jm5jxqTQSY1ol6QgLe0AuPGpq4JDaWZsV2ddXsISXBe4wbxEvWG3fYHVGnbP_Q1KQzHNGeK1gf7vtY-6P0bj4Cf1QATW5Oop7aiUwGGTVXFJT78pMumL9vRhJx5mFsLbxlSNIGcbY1yY8U0G52HBv7kQWzE3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اورانگوتان رو!
هر مسجد یک شعبه حزب جمهوری اسلامی
قاتلان فرزندان ایران بین همین‌ها هستن</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5652" target="_blank">📅 15:42 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5651">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s-q76xhi-uLV4HD6STOPmusUVc2tLtfufaWp6uQGlzoEXiqa77WjdqYiTPfudMuXZLzBwTq4yyTLaKk_Zhmn9y7Gzu7KCFGh4sJnN5qyzDRnQPyKJhXaDH4XISa_V2CKer8LtxTiIBtQc0NxRPa4E1ZArV_FZnVTSGn7ONyxM9gwPvIIIrVCs4l6C3Wc_7EMRMRbhNAuJqhObX5z9e2Jm2A8gX6s0L2zAeDDpnJhm-otSQU0GhDKXpBlAYwn4z6sr5I2HJbz6qdEqCqIMVWg0PJsrDL9LfGOU0KLITP_G_rHsU_gmmbGOFEQ5zvb8Rx172oNp8-WGGvfcpGEALIphw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس
قاب‌هایی جمع‌آوری کرده از جنوب لبنان
گفته بودید یک معادله تازه ایجاد کردید!
همون موقع که پتروشیمی ماهشهر رو هم قربانی کردید!</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/5651" target="_blank">📅 15:11 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5650">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ecdbcd4679.mp4?token=mwaUT6bRddyMTbX9pA96MCkfidx6Dep4xhqRyOgPbctdSLTr__CjzDnS-JC20-Sg-MG1W-me_8w0ImGZ9-dkxECfbMRQh_v3gPgorxJEFhTPp7lgBu7MP6iF-8qabcxah7rBtlTU_ih4I1WaXcQlj40KVUKW2E-fsyZOa-G3d7KeGPeHZBqTYV6LBcqqTucz1xqsORlqZOU8gFAUiM0DWWdEwL-4Y0oFRgdvncBtUYgiG3emMK8YmPPdmQVBBAPeJ1lEE0_O5ZiBCQ4UM55Sn6fVCQ3dMptU9_rUOCS8QwJplKMRLgdSxyGyvoTpcQJVoDaWMSIPDfdUwGWv1BrbbQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ecdbcd4679.mp4?token=mwaUT6bRddyMTbX9pA96MCkfidx6Dep4xhqRyOgPbctdSLTr__CjzDnS-JC20-Sg-MG1W-me_8w0ImGZ9-dkxECfbMRQh_v3gPgorxJEFhTPp7lgBu7MP6iF-8qabcxah7rBtlTU_ih4I1WaXcQlj40KVUKW2E-fsyZOa-G3d7KeGPeHZBqTYV6LBcqqTucz1xqsORlqZOU8gFAUiM0DWWdEwL-4Y0oFRgdvncBtUYgiG3emMK8YmPPdmQVBBAPeJ1lEE0_O5ZiBCQ4UM55Sn6fVCQ3dMptU9_rUOCS8QwJplKMRLgdSxyGyvoTpcQJVoDaWMSIPDfdUwGWv1BrbbQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نمیخواید بخشی از مراسم تشیع جنازه خامنه‌ای رو در لبنان برگزار کنید؟</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/5650" target="_blank">📅 14:29 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5649">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c5aba790b1.mp4?token=NXs2H_62CceSBEn4SmDB-NIuEZdV5XO-dymQESU4gHbpXxPAL2X7vMCF6-XQsYTa8dcsE7GFa7IX7VGslEWWERbbvNtcIzqodm5-5PK1hJdjlJgo6jSQMc0X9GZdilc7cr4g2AoDBx5xpy8NCmga8h3daxl3K7wE1bji2EpDYsTOVNets3QdXGURhrsgMQN6LXVPr1Xf2nVotfJr3l5FZFnnAV6xSUz1zMXgco3mKzlDlKEZbqMwv20KnUNRmyJECGdFcPEvY_SbZbt74-FbkDvf4TF0xuWh-B59Z9f4bsiA8MorCKhDW3kzTtD-pc7I598ZDoKi3F-w3yqXMAE6hQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c5aba790b1.mp4?token=NXs2H_62CceSBEn4SmDB-NIuEZdV5XO-dymQESU4gHbpXxPAL2X7vMCF6-XQsYTa8dcsE7GFa7IX7VGslEWWERbbvNtcIzqodm5-5PK1hJdjlJgo6jSQMc0X9GZdilc7cr4g2AoDBx5xpy8NCmga8h3daxl3K7wE1bji2EpDYsTOVNets3QdXGURhrsgMQN6LXVPr1Xf2nVotfJr3l5FZFnnAV6xSUz1zMXgco3mKzlDlKEZbqMwv20KnUNRmyJECGdFcPEvY_SbZbt74-FbkDvf4TF0xuWh-B59Z9f4bsiA8MorCKhDW3kzTtD-pc7I598ZDoKi3F-w3yqXMAE6hQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نمیخواید بخشی از مراسم تشیع جنازه خامنه‌ای رو در لبنان برگزار کنید؟</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/5649" target="_blank">📅 14:29 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5648">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9eec8cc86d.mp4?token=FED8REq5zILebuF88jMMd0Hv7pUi5N0GeA4gLp495GXSuOWGU0NtEYAiMD3-aEKndVhZTYoqontEiyNC3hek4uUf6hbPa7LjKNyDyD-Cu_P2V62MqbsYdUs48gMNmbhVVg-YMSmLpd-ltBhacRj1GRAGS08xJRJBLHCC2vx1q0O3Eu-VgIVBasRlucc8LABUJJd3r08iahSHHpiFPR71UC4fP5aiidyAJO1ZvrNjV20w3-wT1Cgd9U2oEnUB0i9X3h6F2l_La0In-cpkYuZisl9M9LYcsrQJkEelS3NZqkNC73M4Y4pNEz2EtAdi1HSziY_5bKJ_Gllm5gjR34VBiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9eec8cc86d.mp4?token=FED8REq5zILebuF88jMMd0Hv7pUi5N0GeA4gLp495GXSuOWGU0NtEYAiMD3-aEKndVhZTYoqontEiyNC3hek4uUf6hbPa7LjKNyDyD-Cu_P2V62MqbsYdUs48gMNmbhVVg-YMSmLpd-ltBhacRj1GRAGS08xJRJBLHCC2vx1q0O3Eu-VgIVBasRlucc8LABUJJd3r08iahSHHpiFPR71UC4fP5aiidyAJO1ZvrNjV20w3-wT1Cgd9U2oEnUB0i9X3h6F2l_La0In-cpkYuZisl9M9LYcsrQJkEelS3NZqkNC73M4Y4pNEz2EtAdi1HSziY_5bKJ_Gllm5gjR34VBiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جنوب لبنان - حومه نبطیه
از مراکز اصلی شیعه‌نشین در جنوب لبنان
و از مقرهای گروه تروریستی حزب‌الله</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/5648" target="_blank">📅 10:58 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5646">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m_2gLsKi9sdveO57E31bQ-4xWtc_1DyNgvKG-wMTNbREzA5G5TJtQ_uYCuLGBj526Alil2-CijKkO_iiWlTYvlsDpATGa0syw1re6k6gV1yhcfgkOil7LTJ8V3pAiNSTVaf0rVHISFKlbMA-VUrHxm0k0cOqULzTZ1QWPCkB8HDFNfTJ_0r9PLghEGI8sWvzHKJOlXF20hmCWQiBjKWqPGLSPw93-idIUCtfeNjrfz7bIJIkDaaewlbybWKvcevg2f69kjoBzUn7owH2PIREpzwmAfzvl_SlslufzDPZu_xWjoIYlWH2JTYrfGMuf4x5Wk9hMJi5bTC4tVTe9PxTAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/21669172c8.mp4?token=t9duI1KlET6cLGs0XQrZT3XCj3OOYVH7EWVgbGbc9F7sT7eVuTD5J8KnxVcxCo7BElRzELp6cDiy9-pRVKnmM61zHn4HqvRHhZyNVv2hP2AMOTwA8SBsP9gobkt7QhNqmN3rAJ95CJZtHIPncjE7Y28p9ycJEse95zYlTo41D7eTHe9nOoXYknuMp0_X9J5J4Hg3cqAREzrtCICZ-T0Ppe0sF0zVXCXSWijK2254XG456baqlqQH3oazvrJYagjJhg7ETIiZE8cPX0rF9n4Mxw6Lg836hsis-cVvVHrp9cnZ7l9HZ8HA9SaZdTL2Go4o3lkH5YxPTHAvWlV3kWknNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/21669172c8.mp4?token=t9duI1KlET6cLGs0XQrZT3XCj3OOYVH7EWVgbGbc9F7sT7eVuTD5J8KnxVcxCo7BElRzELp6cDiy9-pRVKnmM61zHn4HqvRHhZyNVv2hP2AMOTwA8SBsP9gobkt7QhNqmN3rAJ95CJZtHIPncjE7Y28p9ycJEse95zYlTo41D7eTHe9nOoXYknuMp0_X9J5J4Hg3cqAREzrtCICZ-T0Ppe0sF0zVXCXSWijK2254XG456baqlqQH3oazvrJYagjJhg7ETIiZE8cPX0rF9n4Mxw6Lg836hsis-cVvVHrp9cnZ7l9HZ8HA9SaZdTL2Go4o3lkH5YxPTHAvWlV3kWknNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ETK-UgYeSI2qKwiBIS3PG9_aOWsh413OJZh7PECYyxlTXRHkW1YBCrvWbC_mhkoQOXIkbcCsAzln0ZA4qRsUNF0xy83Q5V9ZWQRNED8DjlozQZBG56N71oj75DrFZk45cfcFxfnzKv-wPzB3UXnL_ZNrsEsLnVzC4a97oLw96TG3Jq_WFSgch-U1QWbFBMbWwhxBT-fw6-OEP1UDwLjd35bjWEBsR3u4QJWtKLyVgtWny5-S7fwCdgoRKiVHwQwN1wSWqzprRR11AribllWV2heURmhctACZlGagQq8BughUcvcEpH1SSBFqALooC-H3vyqnyhb3Wkj6rbEtOb_BOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e75af7dcb.mp4?token=cp3NvnRm8uGDQPh8nvgTmGOKN32c6nIKMtxhzSyGrSi9tQcFb9smDaw3L-rKpYx6qv97GCaIzLPxP9zliP3ZTkQum-5nIo9HMG5XcLFEe_rp1Zyxd9kAaNoaIHxf_h73NoiI3Sg7Cm4GCR_nLrHMcgoEZogq30-FfZ-o4mGHMkcmdE57Sih0LlbYCF1ezSsPGdOTlh_2p2l3Mz2ao3FiWhxiRiFe6SdXeZlWLnGxLDMruvWK9lpYIlSlmDxZit9B57NJz_MLxWkewFmQhuVd0effFyfsR8k3wNZwzmH9FJLo0bt4YrbPnKNTD8_C-p-U9mg2iMs8bl9KmJ-_hEVdVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e75af7dcb.mp4?token=cp3NvnRm8uGDQPh8nvgTmGOKN32c6nIKMtxhzSyGrSi9tQcFb9smDaw3L-rKpYx6qv97GCaIzLPxP9zliP3ZTkQum-5nIo9HMG5XcLFEe_rp1Zyxd9kAaNoaIHxf_h73NoiI3Sg7Cm4GCR_nLrHMcgoEZogq30-FfZ-o4mGHMkcmdE57Sih0LlbYCF1ezSsPGdOTlh_2p2l3Mz2ao3FiWhxiRiFe6SdXeZlWLnGxLDMruvWK9lpYIlSlmDxZit9B57NJz_MLxWkewFmQhuVd0effFyfsR8k3wNZwzmH9FJLo0bt4YrbPnKNTD8_C-p-U9mg2iMs8bl9KmJ-_hEVdVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صبح در جنوب لبنان
و بند اول پیش شرط جمهوری اسلامی</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/5644" target="_blank">📅 09:52 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5643">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SNSs49lqHo_j9bDk9qxC8cpi9CImqaCNEglFG7OG6rEZf7wj4_BOvf72m7uPOFYCvAtYHspDmxaw97mVm3wOz2vbYGkwSm4Fe4kVi5lAI_LGiWk5p645adgjWMcu4aR02dazydColQJFhdw8FQz6Km8o_xRAeATqunfUhtu3trinjAMpckCWplWSbZEVIquYHvDNXF8Ro0eNSlY3JEfKwKSjCtwmpHdQPoEaGo1Bd3SvWM8mfUgwwLB3N26Y94yfxQ_k-kiwgxU0JCBZfxyOce2xr-EgASQKgkKHqv_9uk50YTk41bc4hB25OX-qdSfVhUuMM4D0dS8GjWgNw384kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حکومت یزید هیچ کدام از اسرای کربلا را محاکمه و اعدام نکرد!
حتی به بازماندگان کمک مالی هم کرد.
جمهوری اسلامی هزاران نفر جوان معترض رو قتل عام کرد و بعد هر روز دست
به اعدام هم میزنه.
۸۰٪ از آمار اعدام جهان به دست جمهوری اسلامیه و قربانیانش مردم ایران هستن.
کربلا به دست مسلمانان افراطی رخ داد، که برای ثواب بردن و مقابله با فتنه، در این جنگ شرکت کردند. ۹۰٪ شون هم هیچ پولی نگرفتند! انگیزه‌شون فقط ثواب بود! محرک اصلی اونها هم روحانیون مسلمان بود که سخنرانی کرده بودند براشون و توجیه‌شون کرده بودن و ریختن خون حسین رو حلال
اعلام کرده بودند و حتی ثواب برای مسلمانان.
اسرائیل هیچ زندانی فلسطینی رو اعدام نکرده تا کنون! هرگز!
هیچ حکومتی پلیدتر از جمهوری اسلامی و حامیانش نیست!</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/5643" target="_blank">📅 07:48 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5642">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d81ee77286.mp4?token=r_T3m5byJNG2vgLJvGywdU3W1aCzZhQ1VHzT3-1dtI4Fm7YvVLaEkAY4hTFNCXmk9YtPRXTLXwCL-ELb8omMVOkfE2Jqikyzx0OZF4BSm13l6EzbIeeuuZvCWJvoZ2UMDUUW8gRPsUWqjCcZGFzyD5mazSCNpM2sFVQl9vK86tA9xa1Jx0Y7ituvmEN1Wdn_bISWI4YQtaiDh864OLK1VDeVljy1BtDeFBMvqm636rDP7S1sVE7kuigtIuXWFLRYOeIyIOBz4JIeh9nDwstMVPW62n2UUI1lwF6MGmP_FmVILJ2s6XnbecFbNuqK87WkPmOCNTzVwQHJ0E2GHN2weA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d81ee77286.mp4?token=r_T3m5byJNG2vgLJvGywdU3W1aCzZhQ1VHzT3-1dtI4Fm7YvVLaEkAY4hTFNCXmk9YtPRXTLXwCL-ELb8omMVOkfE2Jqikyzx0OZF4BSm13l6EzbIeeuuZvCWJvoZ2UMDUUW8gRPsUWqjCcZGFzyD5mazSCNpM2sFVQl9vK86tA9xa1Jx0Y7ituvmEN1Wdn_bISWI4YQtaiDh864OLK1VDeVljy1BtDeFBMvqm636rDP7S1sVE7kuigtIuXWFLRYOeIyIOBz4JIeh9nDwstMVPW62n2UUI1lwF6MGmP_FmVILJ2s6XnbecFbNuqK87WkPmOCNTzVwQHJ0E2GHN2weA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملات اسرائیل به جنوب لبنان  بدون توقف ادامه دارد.</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5642" target="_blank">📅 00:21 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5640">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/B4M6HpxuD_I12g7zUfczCI5HhtxvX5kKAuo1s9EO5tpDXfWlpxa1nv8OANi-YnODa23_Bfm6WZxFPDvUOlMrStuYdA5L5Zh3lxeMFI3MNH5KjXPOnZn729fh6y0c7X3naguT-SyVOqTstCPqgf9LYB4w41YGdovJwq8zF2DbHkd4PPwlimHHAO8CADpBCYEeKJ1XNpHk3ptuQgfnc30wsw5m3vxY6qR6oMyRawluosbbRJEzmiDxT1tAzKY0hMRTKyRt5o95vQmBOrqRO4v3IvGENLfzSq224fqPfSXrX_hsVgEmGBeK0BIukwxfb1xbNTB5w1i_vwvjYq5QS_ribQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TYxZ104qpx5JfoP6S6lxLaTeRWNEHi9LPVwkAD398B5-6X_ZUxsxGeUtRzeF2x0KnZM5AXHTitL1nhvn4qfv816xTsAIRWJNFRQu-z0WmENop8iaTe8Y2OfLGSq8WuMzLqyDKl_VJfXkWn3TYL0yHeY7bWAe5rfTr0UZZgl9xPykH-7mK1e7Ztl6MaqNRFFg-sCCN1UwB2IZFjC1pTGqGkwkRURB34RCxKMZhFgl9LEsteAyCb-LYwyHMosh_APRh_UD4d8Au5uw4LFkJX6nNRbF8l74vfR4kt73ny0gmc9eURMOqW0DVYbXodTxdZ67bMOavE7BTkpmebCDFE4iPw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">فرار گسترده کسانی که میخواستن انتقام خون خامنه‌ای رو بگیرن!
تا اینجا ۴ هزار کشته دادن و ۲۰٪
خاک لبنان رو هم دادن به اسرائیل!
قالیباف دیشب در تلویزیون جمهوری اسلامی گفت : لبنان ۴ هزار شهید تقدیم جمهوری اسلامی کرده.</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/5640" target="_blank">📅 21:35 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5639">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f791b65d03.mp4?token=RZiFA2Kx4lIav04Yj5eDUdFpnBjoIGEDt9jYgtYcTfjuWVO4lXxnRYj9b0k7pANIJYp-tSzvmj9ipWZ2xheAURZNrvYeB-4-vu97GY9FB7bgzsHLbDr96l9_9o7ilNLUIYRj3UZzeU4ZGwPJ-k2kLQNMDMORKYWY6WhOj69Yw9e_8soKd11ZbFKSlG7hOw17qFJ0T7Z300lhf0Kf4D8lESwHPUN4OSB7q6rrWd1mEIC0MfBu43EBwipCpk6OHZKYjCfVnjELvYM0xFDFEYUlZ9yQAGuTpFmksA7rxIaPfPfykGTwm29BM43xw4qSFClZNKsMBrLDxZziUIMcIKOMDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f791b65d03.mp4?token=RZiFA2Kx4lIav04Yj5eDUdFpnBjoIGEDt9jYgtYcTfjuWVO4lXxnRYj9b0k7pANIJYp-tSzvmj9ipWZ2xheAURZNrvYeB-4-vu97GY9FB7bgzsHLbDr96l9_9o7ilNLUIYRj3UZzeU4ZGwPJ-k2kLQNMDMORKYWY6WhOj69Yw9e_8soKd11ZbFKSlG7hOw17qFJ0T7Z300lhf0Kf4D8lESwHPUN4OSB7q6rrWd1mEIC0MfBu43EBwipCpk6OHZKYjCfVnjELvYM0xFDFEYUlZ9yQAGuTpFmksA7rxIaPfPfykGTwm29BM43xw4qSFClZNKsMBrLDxZziUIMcIKOMDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جی‌دی ونس به جمهوری اسلامی:
گزینه اول:
به رفتار خود مثل یک رژیم تروریستی ادامه بدید؛ در این صورت، به معنای واقعی کلمه هیچ چیزی نصیبتون نمی‌شه.
گزینه دوم:
مثل یک حکومت عادی رفتار کنید؛ آن‌وقت آمریکا، برای مثال، به قطری‌ها یا اماراتی‌ها اجازه می‌ده در کشورتون سرمایه‌گذاری کنند، البته اگه خودشون مایل به این کار باشند</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5639" target="_blank">📅 21:14 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5638">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jun_vrr4q0RqgyBjWkcfWs8yGGwNGA5egoGue4p0l9LLqE71SV4GHvCfDDFgHZn6Uhl-6tBual3ploGabHEZNb1bg7ky9aNizMXAlFZQWCfE0JKYcJAwNc7VlQj-Pba-1bjLsDp_QwXRc94RTmocK9VPk45ByqSknymeSRnIiaXB3_FGF4TEwmwBd-mP4p243FGlwoP2CObdqI4-JnXFk5hY3Fm5Nn_S0TRFP00i8bC4xwcUP8lQWShq-AwdvSDiAGQeTnXbYcNZ8XHQm3EYbWPEhM_8aTS2_RmPRr_hphtcRhaMA2KqXbPMFQPPCXMfKrMLlCihstMpDpFeu_ne8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنان دقایقی پیش رهبر گروه تروریستی حزب‌اله نشون میده که این گروه عامدانه شب گذشته آتش‌بس را به شکست کشانده تا اسرائیل را وادار به واکنش کند.
نعیم قاسم :«تا زمانی که قادر به ایستادگی و مقاومت هستیم، چرا باید تسلیم شویم؟
ما تصمیمی حسینی و کربلایی گرفته‌ایم که هیچ سقف و محدودیتی برای آن وجود ندارد و این تصمیم کربلایی همچنان پابرجاست.»</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5638" target="_blank">📅 20:02 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5637">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pzVkR6npZdbV9Df7YFurGdY9U-yDHeu_zWwhkhqOwhnWZoLry42HaJhIKxLQ85qgz14KGkCtmqO9Bw7kh1x9oTrbqJNYbE3gbHps0PTIU9JVJyt5WoHjH9jfhce-SXop8tsqvfnFFXPUxOJwF_dlBAR-akZyvtBneYXGqz2ix8sqvNuXU126urPgR0dhcuqPC_NJJuzEFaNZi2O6AsaJ64-CkbAIrYUxJmxePLpz5xyYtJGmaWs8HFGVHJkRnrSMMK-G-gsPpvURuNCzC4XaZAhU0dKPzMeifLBvtiS6d1lwVfXGYOkBYfx_Dz_-InSuspEE61ftU7vPFwhNJQTksg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/farahmandalipur/status/2067993854494622141?s=46</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/5637" target="_blank">📅 19:02 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5636">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g3W2IxLs-xvDBrKG6E-FwgAG0hpGdXp3a5s6QZjIKDdGrWC9qamYASSV5b4EC9Q2ilZncXgLD56R46VRH67B1wWNA-wdSZ-fr2ZFCniQoMx_wgK2YARudInDeA7FcMjqF864AE7DN-ZrrHfWcxbV5yECMjEacXpsMrQL8S2pXN9mpO3x4TGyDheUqfdUPGaq8n-JETas4kFW_UL0BqmeTkvQnsnUirV2-KEqfI_9bJNONxqvoFR1_K_p3Z2akbKCkiY-2Uf4QoPPpsTX9w8X5mYMgM9gzvSVve5GicbFCuQkiXqhACOgonqYe76zVtBQV_y3rAV3JQQMQkoFCeNmMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت بهداشت لبنان : از نیمه شب تاکنون ۴۷ تن در حملات اسرائیل کشته شده‌اند.
پس از انتشار خبر کشته شدن ۴ سرباز اسرائیلی در شب گذشته، اسرائیل دست به حملات گسترده به لبنان زد.</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/5636" target="_blank">📅 18:56 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5635">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UcJb6z4nJuMtja25-OUmWNJMadThRvU2VTyIaKpHz4SxzlOKogysDXyAYz-wAEMUf-BZT6cGbv8fVLAJyMQOBGvitRa2sDFHPvydi5fiztj_hOxiFRpi9uG_aisyGt7cnLGK53McyeOcNqRk8CnNAhqMC5wmqt4cS_QhMUDAmydmVmbAsoOiwtmWwjq2fQAOTenh7HeeUkQdo8IodgbuN9BBwiGI8HY1-SLKsA-r_GrJPgzibZnbJDXrVivfrkUnwyturFWllUSj1XUad71qaPWHC-3KLd_jQgZyzSDylwB8va1vPj4XfDwz3d530gNKz2Zge1I99wqJyCuz0DSLAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نگذارید</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/5635" target="_blank">📅 18:39 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5634">
<div class="tg-post-header">📌 پیام #6</div>
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
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m6w9EegAd63__msYMq8WhGbaVoCIKcrZWgRK0naXHyDGqki0PuxHw3CIddLWbq8ttcWVEMyP2v4YvQ5JY26bf71n5YcK2oLEYHtGEntVQnf1cSmPgbuXl6me77_0WARGmi8ZDQEShmXqRlVYN1ttNve8D6SmzYghyeDbuinLARELD0cdeaEAgVG-DLaqfjrJRMtQ4lp45ZN5TWrbPNwN6ZF6d4WLpJUOKfNgnyhVPdeGjqgrxtToMuNih1J-tDKan5AOHtWbkEgCSWezs2CYbUCORUY-cvQdzcVIIXhpvOFpO2AZYKTi5M8OZwcX3g7t-YbasE9XyJ55YAw31zzElQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نتانیاهو : به بیش از ۱۵۰ هدف در لبنان حمله کردیم</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/5633" target="_blank">📅 18:30 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5632">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/392eac3002.mp4?token=ldNjUsrw8DEUMxvLA2q6ZmwSvXO_v7NQRMWhftYC3802LdAI9qFFrxxePlfNFk_FN9NZBOsKROyvM1vjC6sMQsYM5UIyqRg-Te6UnULWPUyYnznyCHp5pPmsO4J1NrWX0LsFr17lDKS4K-YNjotXjfrMF5sEPwuXLTgCqAFFaTEKNzF60wruZ3SzLjUcjlVjP_mqCVV9zmn-Y-XcmVeNQtfWXdeQHeOmAAwUNoYkJxcIaAdLYMfsNK7VyzX70oU7tLgXcz3W5iJVCqNFumgPuxlBvuMuQL6zdfNQOWiIipRpkYtekuyvufcwAYkQYCyAm2KILRhBYSxI9poVScNNng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/392eac3002.mp4?token=ldNjUsrw8DEUMxvLA2q6ZmwSvXO_v7NQRMWhftYC3802LdAI9qFFrxxePlfNFk_FN9NZBOsKROyvM1vjC6sMQsYM5UIyqRg-Te6UnULWPUyYnznyCHp5pPmsO4J1NrWX0LsFr17lDKS4K-YNjotXjfrMF5sEPwuXLTgCqAFFaTEKNzF60wruZ3SzLjUcjlVjP_mqCVV9zmn-Y-XcmVeNQtfWXdeQHeOmAAwUNoYkJxcIaAdLYMfsNK7VyzX70oU7tLgXcz3W5iJVCqNFumgPuxlBvuMuQL6zdfNQOWiIipRpkYtekuyvufcwAYkQYCyAm2KILRhBYSxI9poVScNNng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سخنگوی ارتش اسرائیل :
توافق  برای آتش‌بسی هم اگر بوده در سطح سیاسی بوده، در بخش نظامی هیچ دستور جدیدی به ما داده نشده و ما همچنان
به حملات خود ادامه می‌دهیم.</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/5632" target="_blank">📅 18:26 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5631">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc70f2404f.mp4?token=gIraD-2Dz4vjZCw37cagF7SbyGw6ZW_kMCOllIyCC5_l3138DG6wanoQPQNH6mKZK9ic8sX3eERGcNr7Ddo6wRJvoDumXyQxlI5FRFkgKK8QvcdDaK2cWuVsRbbafqlHB26ie8JiHnRYkwR3xzWhijlugntGfE1nZ1Bbv0mINrOTZRE0RSw9P0P9IMVM3HIrsboMfWwkxRYvhYKYNWOUxkQcL7Rad6OO_yJMQvMpXJosmPgL33WZ6MhUn0jKXNuw9bwx057P_qmKE4XDpx4KAjrGw_tGMrhnllqzA3o9hKU2Pb4MObbPXojKmQYkWzutH0-ZxVGwpWpFz39E07WSbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc70f2404f.mp4?token=gIraD-2Dz4vjZCw37cagF7SbyGw6ZW_kMCOllIyCC5_l3138DG6wanoQPQNH6mKZK9ic8sX3eERGcNr7Ddo6wRJvoDumXyQxlI5FRFkgKK8QvcdDaK2cWuVsRbbafqlHB26ie8JiHnRYkwR3xzWhijlugntGfE1nZ1Bbv0mINrOTZRE0RSw9P0P9IMVM3HIrsboMfWwkxRYvhYKYNWOUxkQcL7Rad6OO_yJMQvMpXJosmPgL33WZ6MhUn0jKXNuw9bwx057P_qmKE4XDpx4KAjrGw_tGMrhnllqzA3o9hKU2Pb4MObbPXojKmQYkWzutH0-ZxVGwpWpFz39E07WSbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پخش حملات اسرائیل به جنوب لبنان
به طور زنده از شبکه خبر</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/5631" target="_blank">📅 18:20 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5630">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aab675b39e.mp4?token=UgskuNfrrRo9p2NRhCQJIYmjJamSxed2XsKvi8wGpvhJI8jB05QZXj7l4kdKIy9Tg0DEDiIUvi6eXkeDY29h1MpSwcnoV9D2iSa_HFjKwZw3qWJLAaDNWk9O27FmUFizZZNLoJR3aM3FRvGpTjD-sXZr7eqpnVcdT3dU17NTGp2PuF75cWbXhPv3xhcSI0QWI4onG-szpjoWxVr1jBU7pLXvqSOsGUqxVrGlVRdTsZfV05-QhPyIXQ4r6QtxaRkGysLqh1jhyb1zsHNdusXeLfso0LHwFMEeYagw_PAN06GviFRK1LCROmvOcwogOdIncms9jJ1rzJ7NJ4GQFRdTlw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aab675b39e.mp4?token=UgskuNfrrRo9p2NRhCQJIYmjJamSxed2XsKvi8wGpvhJI8jB05QZXj7l4kdKIy9Tg0DEDiIUvi6eXkeDY29h1MpSwcnoV9D2iSa_HFjKwZw3qWJLAaDNWk9O27FmUFizZZNLoJR3aM3FRvGpTjD-sXZr7eqpnVcdT3dU17NTGp2PuF75cWbXhPv3xhcSI0QWI4onG-szpjoWxVr1jBU7pLXvqSOsGUqxVrGlVRdTsZfV05-QhPyIXQ4r6QtxaRkGysLqh1jhyb1zsHNdusXeLfso0LHwFMEeYagw_PAN06GviFRK1LCROmvOcwogOdIncms9jJ1rzJ7NJ4GQFRdTlw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گریز دسته جمعی مردم نبطیه
در جنوب لبنان،
صدا و سیمای جمهوری اسلامی
حملات اسرائیل را به طول زنده پخش می‌کند.</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/5630" target="_blank">📅 18:14 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5629">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/73e57c3fdf.mp4?token=vbemQ8MuJgta-ayeTCg8Mve8wmlOZL-xhV2Paq34JPQmmMRwUMGQwPz25xvh6gVRIjuScedEx-LRjCD3QOC-ewBW5UieYCGn6XlxYgQ-8tjxYJS5henINprit-GAHosi4slagPW6mSN0DoMYTa12XtKZe283AdGaDz9khAa2VkVTG-w2c5POwMZUlr6RVzZx-j20Dx0xISQI2F00WgvsBNOteCifZ551OgBJhCwWtI7LPxaxQVyrGVPD0_HelfWuBIN7Kdw36PEiNXhdWfv9IoIKBKi7hwGqj54ZdjUYD2ow4cUr0DNc08YtyaiYJqdqf0UK9lHOMxHa1g6kkE3SZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/73e57c3fdf.mp4?token=vbemQ8MuJgta-ayeTCg8Mve8wmlOZL-xhV2Paq34JPQmmMRwUMGQwPz25xvh6gVRIjuScedEx-LRjCD3QOC-ewBW5UieYCGn6XlxYgQ-8tjxYJS5henINprit-GAHosi4slagPW6mSN0DoMYTa12XtKZe283AdGaDz9khAa2VkVTG-w2c5POwMZUlr6RVzZx-j20Dx0xISQI2F00WgvsBNOteCifZ551OgBJhCwWtI7LPxaxQVyrGVPD0_HelfWuBIN7Kdw36PEiNXhdWfv9IoIKBKi7hwGqj54ZdjUYD2ow4cUr0DNc08YtyaiYJqdqf0UK9lHOMxHa1g6kkE3SZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به رغم ادعای رسانه‌های آمریکایی، در اعمال آتش‌بس، رسانه‌های اسرائیلی از تداوم حملات و عدم توقف بمباران‌ها خبر می‌دهند.</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/5629" target="_blank">📅 17:42 · 29 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
