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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-05 20:43:45</div>
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
<div class="tg-footer">👁️ 5.33K · <a href="https://t.me/farahmand_alipour/5742" target="_blank">📅 19:53 · 05 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 5.55K · <a href="https://t.me/farahmand_alipour/5741" target="_blank">📅 19:50 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5740">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">ترامپ در شبکه «تروث سوشال»: «جمهوری اسلامی ایران دست‌کم چهار پهپاد انتحاری یک‌طرفه را به‌سوی کشتی‌هایی که از تنگه هرمز عبور می‌کردند، شلیک کرد. یکی از این پهپادها مستقیماً به عرشه بالایی یک کشتی باری بزرگ و بسیار گران‌قیمت برخورد کرد. کشتی آسیب دید، اما توانست به مسیر خود ادامه دهد.
ما سه پهپاد دیگر را سرنگون کردیم.
روشن است که این اقدام، نقض احمقانه توافق آتش‌بس ماست.»</div>
<div class="tg-footer">👁️ 7.55K · <a href="https://t.me/farahmand_alipour/5740" target="_blank">📅 19:23 · 05 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 7.8K · <a href="https://t.me/farahmand_alipour/5739" target="_blank">📅 19:16 · 05 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 8.31K · <a href="https://t.me/farahmand_alipour/5738" target="_blank">📅 19:09 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5737">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K86q9Pgkmf-I0BvRjkhFAAeLnuBPT4wEALZQG9gRi2mIKotW_LU9oUFhz13Yg9wjUD67gGD-bXHrZ9cuLM6r9RUd6Y7wGSq-te_T0nixa-QyAPkCcQnARSM9irxQBQGR0k4FyxXamoTIpHDdvIQwI7TSLMxTnjCzTEVFe1sjW1hlJH2tTuCuTp4eMvr8cIcE1FjDF9VNNoQua8vcNToDKWvH0ZZihpe0AZZeIiuhwEmS94oNE9zYOBCIXPrGwMgWRqA9mGOtG-6_rRhUtwlRXQrmqPlC-lcGRDJdW9d4XU6oJ1oYKI7RJZ17n35LbMzsA5c5YIlrNzYacJ9dN4m9tQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیام فارسی وزیر دفاع اسرائیل خطاب به قاآنی فرمانده سپاه قدس
آماده‌ایم کار را به پایان برسانیم.</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farahmand_alipour/5737" target="_blank">📅 17:53 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5736">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">نحوه اعلام خبر کشته شدن خامنه‌ای
و عدم تعطیلی مدارس</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/farahmand_alipour/5736" target="_blank">📅 16:55 · 05 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/farahmand_alipour/5735" target="_blank">📅 11:38 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5734">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p9J2WgJ5JE4bNwwdz7q3V2IrUVuUtOyCbKQMhCWopxKc1s6gix1hOSQOB24hmiOoqWoB5x08HGAydJYskEYx9uJ9fB7VnZeWF5pJJpDrJVOMnu_47qlJsqCRfP-HOpzs2qb0DYgznXUdQcIv9l1fZfBnSuOa2GGqlnj7f10NIymfektHzHhIgN_j39xmwWiE4ZQufHxDVJBCArVKFr2knX3wNxadbTNZDzc9agKT5UKobteysFOWA7d5CnI2vyGz9gYz5v9JuSejqwGuFbqIzFAPUn6061WK260Wq5q8Ifk9YPDRe2giW4GzW9wG7cma7pXSGwOOuYbHyQbhN_p5vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر علوم جمهوری اسلامی  در ترکیه،
خامنه‌ای را از اولاد حسین عنوان کرد.</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/5734" target="_blank">📅 22:29 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5733">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YCbooH_h5rMr1jsmM99DYAG-HBv-xaw2c_9FRrELw__GaqzJrc1YnkKG5VuDUm6P5ChZ-V9zIiklEDwImH_QQbDB0rlw3WwCpHBb4woLC7E3eyxIVfFRJS_tWqzJvrv8FBpoCuMxZmQywnPuKU3fUju_LNRmDslASKsde8z1slhFXxNS_QkBFUCiFl84J36JOXFXAKsKYQiqGXF_GqfhTjmRlBUPze-DN_Tmkkn0KOWLBtimGXpJcd9_nPqyyf2qXD5UC_mlWyIgqHGnnmgQ1OKHxJiMZXUwPSTtC1ofldrgb5yRhwgswZafE6Y0Ag9mnWkZltelSh3rDEUgroy1Mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسرائیل به یک خودرو در نبطیه در جنوب لبنان حمله کرد و در نتیجه ۳ تن کشته شدند. مشخص نیست سرنشینان خودرو چه افرادی بودند.
صبح امروز هم در جنوب لبنان یک سرباز اسرائیلی در جریان حملات
حزب الله کشته شد.</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/5733" target="_blank">📅 18:23 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5732">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WM4D2xqXw920j5I9-sKCvfDDKU6t5AhNKkYatnKcd7tyoYkmaeUhgO78sK7G85vU6MyfGE8BOIsXHDeg42fETgvtpANYSdeRfsCn8aIjovbtBuQR8HtHxM5dEojSpN1o7PitmBb4xcOCJXXvNqO9m7jeLwjdONM4vhunTUzrmb6AVzRy2LWWYluO7LsaHMTdPz0fo0KwC2S7WOUqEFZNdTS8J3oEZ7hivBhokMESqW5Cw--Hs8IzErse1J7aHJv56ywILUBFGPnDBXQdh2voFwCwnuB3rB2gKAA97q3tdMur7CkOT-kNgipH2PJCECq_RYmAuZaTgShqZ2Cq1OP1Bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صد رحمت به اهل کوفه!
لااقل به دینارهای طلا فروختند!</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/5732" target="_blank">📅 15:21 · 04 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/5731" target="_blank">📅 15:20 · 04 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/5730" target="_blank">📅 12:24 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5729">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">اینفلونسرهای عقب‌‌افتاده‌شون‌ میگردن توی دنیا تا سطل آشغال کشورهای دیگه رو نشون بدن  و بگن ببینید اینجا هم آشغال وجود داره! پس اگه کشور ما رو کلا آشغال گرفته و به زباله‌‌ دانی تبدیل شده، عالیه! عادیه! معمولیه!   مثل همین حمید معصومی نژاد  که دیروز براش نوشتم،…</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/5729" target="_blank">📅 12:00 · 04 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/5728" target="_blank">📅 12:00 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5727">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🚨
یک سرباز اسرائیلی در جنوب لبنان کشته شد.</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/5727" target="_blank">📅 10:30 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5726">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/budDXemWSIQ7SkoDFzao16aXe1hInTtqIATa672agPsa9WF8EDsKLaGZV3l2WyzcdOnzy7lD-3AEzDARLU5DylmTGzy0xod2cYQUoVyaiEDygWz-aP4E3vtWkqMWNxQJMjnLh4M8a8tQhjNAa4Bv1ahYqY2UsYIJXOyQRJwyJ-kc9iYNaeAxPHkEf-9b9jhSA_aFjFd_9BNpDx0NOyB7h1peFf_j3XVoUfJM6YCCcfUQgKQ6TLuUAshceY4M24WeK_XLFURecglGtzjYh-FhsWLTeO-BGHNOc3_FHV_ke3Aq8JfdVy4vhfqBQWEuwqtDN5V_HvOy3tYY31T2d7gnSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرمانده گروه هکری «حنظله» که در جنگ ۴۰ روزه کشته شد، ولی خبرش الان منتشر شده.</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/5726" target="_blank">📅 09:39 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5725">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/86c17f6d3c.mp4?token=c0tT7NJILZpPvsY9Qa_MG0_zT8zZvgFkUhOG4DHutGP_Fx04jwA1XvhCAzzfrXbA1WPCkVG-bhBDhplXaxoVWsHR3amGwXtlul4FVaWKh0xwTKj8dfhZJqajiwl0Bv8zFpSg9npH8C-BQBY8RWdCG0aMiwK1jTVLlc2TtxxqDRGk3PANTHcaVL0X3OpmDAy2TFUnuhH9FJRDGM0yL1xEYouTP0KKWAQIrrOcLtcKeLpbbIoT_4S8W1mrjP9HRfkaPv27oBCckaXIBFkGVemRBXiYK40lvgrPltQ0WZ1ncfr9OfeFEx3x8iCR_skQNb1dKmNfbNA_54gZ_VTFYSJixg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/86c17f6d3c.mp4?token=c0tT7NJILZpPvsY9Qa_MG0_zT8zZvgFkUhOG4DHutGP_Fx04jwA1XvhCAzzfrXbA1WPCkVG-bhBDhplXaxoVWsHR3amGwXtlul4FVaWKh0xwTKj8dfhZJqajiwl0Bv8zFpSg9npH8C-BQBY8RWdCG0aMiwK1jTVLlc2TtxxqDRGk3PANTHcaVL0X3OpmDAy2TFUnuhH9FJRDGM0yL1xEYouTP0KKWAQIrrOcLtcKeLpbbIoT_4S8W1mrjP9HRfkaPv27oBCckaXIBFkGVemRBXiYK40lvgrPltQ0WZ1ncfr9OfeFEx3x8iCR_skQNb1dKmNfbNA_54gZ_VTFYSJixg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ میگه جمهوری اسلامی خیلی رفتار خوبی داره با هر چیزی که من میخواستم موافقت کردن!
باید هم موافقت کنن و گرنه دوباره
برمیگردیم سراغشون!</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/5725" target="_blank">📅 22:56 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5724">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">وحید اشتری، فعال رسانه‌ای حکومتی :
تنگه هرمز شبیه یک بومرنگ برگشت به صورت خود ما، در ۴۰ روز گذشته حتی یک بشکه نفت نفروختیم. از لحاظ نظامی توان شکست این محاصره را نداشتیم.
گقتم تنگه هرمز میشه تنگه احد براتون!
به هوای غنیمت گرفتید، ولی فهمیدید باید دو دستی خودتون پس بدید!</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/5724" target="_blank">📅 22:23 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5723">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/171eba79df.mp4?token=OPq3cR3Qo6hhZnA544SqRW1zTB4Nc7i-pxNq6PjN4uhFo-_0wZTHtg-dfM7qan4ntEVLD1WuLx7zl4RzsQBcqfOHiF03_1QHFlLKvVzGwPIJVwi-p6qQ8NIutEXCXPBBndmLWEekyj8ld8uhibLR3TEV92LFVBtzuvjteIA4wDhXKduMmbu4RAkeDixWC4Dva9fREoYIASDk2qsAbgq2ENcoNCsfwTedn__GB8i-9KpYglj2M6TwHWX6IdeDs1plcYTF3Mdghowt-a_liRTVvPHYxlNV8nUTOXWf1Tk3cjlhqvaufI1ZzvR4HSrURn57Pm-0gBleuhi_atNz3OtzRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/171eba79df.mp4?token=OPq3cR3Qo6hhZnA544SqRW1zTB4Nc7i-pxNq6PjN4uhFo-_0wZTHtg-dfM7qan4ntEVLD1WuLx7zl4RzsQBcqfOHiF03_1QHFlLKvVzGwPIJVwi-p6qQ8NIutEXCXPBBndmLWEekyj8ld8uhibLR3TEV92LFVBtzuvjteIA4wDhXKduMmbu4RAkeDixWC4Dva9fREoYIASDk2qsAbgq2ENcoNCsfwTedn__GB8i-9KpYglj2M6TwHWX6IdeDs1plcYTF3Mdghowt-a_liRTVvPHYxlNV8nUTOXWf1Tk3cjlhqvaufI1ZzvR4HSrURn57Pm-0gBleuhi_atNz3OtzRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قمه زنی گروه بزرگی از شیعیان در کربلا</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/5723" target="_blank">📅 21:46 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5721">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nfxsnffrikp7UJJzega4j6SPWStfbcHHDUAnr4yFp3-taheqCZ4bgTlr9I3V3fiEq6MTPUlehPko9K7LSvFf2TFGc_Vl2EfNlRop78ui2eOLTGn5Z55D5DUpTySlpSMoluNkaHSWpvxBamWBbjsFrNePpVlCINd4JkgNtmQRZs-6AWy5ZLL6IdRV94EUJ2nCTGkTZTV7-e-gsJGOuM3r7q6iE2N0erWlvkfJJYOsNiwn7G1SbjuCwP9cNnBVCb7DwSb1-hcmYwHEJDJzjQZzjldIRWHVKiS1EvHEpQXAWl8Y8hUqvE38QxsBjWDYLyr316o1g6bU7kiwjnVTPMadNA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5721" target="_blank">📅 15:52 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5719">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CcWC1osg0H6kYI9L-mplmOcb2gHOPoYrHBorLvFI_F6NzGmUGHOIbQJwpue_fHeoUSNOM3pjxtn7J4AlzPIe_tBacjr86W-MW8YBhhF8Y2iJEiUNzYoXvfIedYcxk9HO1pZt5qRj_aOSfigwxDN1FXSyaIwtcuB6uvOmMMSD15PfLttCo5hgvbcd1hyQIMhSleSETkVqp2dO6rU9D6m714wib7NIAvKM_PMDqCQ79W8JewAWKeqaEByLVSBTTTgo5Wikevz5eGcUJuynjIIr4N6DZxRUzo0Liaa1WFdlDmyyOVRa6N_PLpeM5taY6Fvd8P7u1OJogHQ_ONn_f09L2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JoBwKgdwKgCt-1KRnLShK_ijQ9e1Ug3sTEkE2ts_AxqTwBmMir_BiQVqZNobBg6CIVexpQ7mFXY4WJTjWi1RCSTsIMJMhEkk40kN59yhDegAS7TlwTUcCXSrJXhoIW1WCMeT8v4lz0ZmWicBYodpVcAbLLhwfnOwS401818eTBehg8R9nDKUOuOq7cZYs3wv7ZRrUG6E7Hj6NcrSYL_GPz4sMY5pVDFD9uen2kgpTwsQrHcH9AAa-j8-nvbKvhbLcQ19zsMgfcw7SW59HtsvxeIXU8Au_NTk1l_pEkYXJ1AwFUFi-fhDPeAgvIcrZDS95LMhf7rPvL3X8PYgWZ2QtQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دیروز تولد «آیدا عقیلی» بود
آیدا ۳۴ ساله بود که به دست جمهوری اسلامی و در جریان کشتار ۱۸-۱۹ دیماه به قتل رسید.</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5719" target="_blank">📅 14:39 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5718">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">‏خبرنگار : اونا می‌گن هیچ بازدید برنامه‌ریزی‌شده‌ای برای بازرسان آژانس وجود نداره؟
‏ترامپ :
بلوف میزنن ، ۱۰۰٪ بازرسی رو ثبت و قطعی کردیم.
‏اگر راست می‌گفتن، همین الان مذاکرات رو لغو می‌کردم.</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5718" target="_blank">📅 23:27 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5717">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/975d16374b.mp4?token=hI2sJ2p12Y09Ggai92CC9h-Kt0-gk5ViF_ZKIdc19AsMhA5qJcXEZ4OgjbZFUpa3JtZIt8ZP_YFIDrLI8aTUNQa1AlcshTr8eMIa8wKYzetRyeRcFxkir7kKzutavR3X_zlTVPimpOpv9ZQTc9NrOFSEpzko2ry5Tpok-s-czkqERAEurRAQGgpygA-U4r_LqIw9xgclLpfUF1FjSDjNK4JYHzGLoKEzNQQZpQPMOhWaa5ymja_hgqdpJjbPyOlieS3aYuaM-SrAn3mwINTNUbOKDF9ge5D8w1EWpH4Is8kiC5FnOtsMmWaUMzBkkDqSwPJHpSqrSJNZGoDnerB05A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/975d16374b.mp4?token=hI2sJ2p12Y09Ggai92CC9h-Kt0-gk5ViF_ZKIdc19AsMhA5qJcXEZ4OgjbZFUpa3JtZIt8ZP_YFIDrLI8aTUNQa1AlcshTr8eMIa8wKYzetRyeRcFxkir7kKzutavR3X_zlTVPimpOpv9ZQTc9NrOFSEpzko2ry5Tpok-s-czkqERAEurRAQGgpygA-U4r_LqIw9xgclLpfUF1FjSDjNK4JYHzGLoKEzNQQZpQPMOhWaa5ymja_hgqdpJjbPyOlieS3aYuaM-SrAn3mwINTNUbOKDF9ge5D8w1EWpH4Is8kiC5FnOtsMmWaUMzBkkDqSwPJHpSqrSJNZGoDnerB05A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سیرک‌های جمهوری اسلامی</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/5717" target="_blank">📅 23:26 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5716">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D2kJUGHz-2RWNgFy-b9XF9WuSVy2gVNUNwbQX0wU5UU2Vxsy6iAYOyZtLULYVXgY5rUsqcB-KscxZEQ_f_WvDqIw1QcWDAjQ0sL-o2gF5j1SGTnMe_Qer7QSqZV861k2Ymt7wlWkGJogZY77BmWHdDCXb6PEpkbSUbxYGXSGKgM4ZdXTYg__JgKzVsoEntri2O9Ls0RrgiA9p96RPBJh8e_MRGb5KPEeWI2qwH58yPnlhG2jgLHNQ-a2kt69ivtMmQcsPMd8iUYUEEZkxGAHZU9ZbX0jRFMU9JDqVCW4EhceY2dVF2u4TFHl0kvmdbl-m3Ry_tBqQZwiqRuPEJCacg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
شهباز شریف نخست‌وزیر پاکستان:
‏«مذاکرات شامل برنامه موشکی ایران نیز هست و آمریکا و جمهوری اسلامی ظرف ۶۰ روز آینده درباره برنامه موشک بالستیک و موضوع هسته‌ای گفتگو خواهند کرد»</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/5716" target="_blank">📅 19:00 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5715">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZDmGQUsjdnuee8oxmmcPzIE1iqeq0nHk5yAPdN3B8ZxXPQU13ALP2vu_DHzQcEaEZzjic9BpAIBGYXIrzWZXvdkBFLVBifkE1da0fVtRrkdwqAt6u8QnxZXd7P4XzalUwx2YBFzS5Tem-tm7MvamE5OBxFDdep9edF_Shaqc3cKeilT40LTBsxnXfZfw1C_dR43lJBAymPQBvFojFdgWnlYWgZLw-quZ6VjcGxR4iidfy2Y967BQtWjzYPeM_5fIJuLc_UCxUGEJI3XTsu7DyGE_8bse5zzg3eK6wiFVBmv0aJtVbuuAXLZRUkqxwtmIlz8u1DVZeQFDOJthJMLzoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/5715" target="_blank">📅 16:50 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5714">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">فکر کن رهبرت رو بدی و سویا و ذرت بگیری.</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/5714" target="_blank">📅 15:27 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5713">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JAycoIgh9_gqYxsUYUo_EMaHlxu_sudPAjgf8d49XzpKkOyJU-8s6iycy7XhGSCujFFaNreLwh-NqbxpuFm4R9BtAK0jJnTsdvDZlkULQtr1C-K9r7_Pcal45atY8CMNBT_UKyGgpyBArd9O9WmuZIlGDXi2PeccBDnlHcW_Q2FtPqhJYbzTC_MXLOrdJFhKhKvf8yeZbdUhyq1Xyl_BfUIujuMgLq83tnzpV6jR1-hqefQPmQD9HRrMXsMSjG3hKi1JGOeifU_kKtLCqHxgZ80urDyR13y9GvLuDiQdER54-wfW8cwfQnm5a8h7URwvk2uWr7wndQQYGbn4BjPN9w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5713" target="_blank">📅 15:12 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5712">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">ترامپ :  با وجود اعتراض‌ها و ادعاهای خلاف واقع آن‌ها، ایران به‌طور کامل و قطعی پذیرفته است که در آینده‌ای بسیار طولانی ــ عملاً برای همیشه ــ تحت بالاترین سطح بازرسی‌های هسته‌ای قرار بگیرد.  این موضوع «صداقت هسته‌ای» را تضمین خواهد کرد. اگر آن‌ها با این شرط…</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/5712" target="_blank">📅 14:59 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5711">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l4AOSzNY0scbvWeXF2BVhB31xhvfNd9v6CwkX0F-WlW1O1Q1Nh6A_g8NNOyVyeR9O5FN8jwfH7uMfhcGz-oD08ph0LaT0CA0dfAumJQigY0jlqyvx0fY94X43PO7l0DVyjV3dL2DsDgK3UhK6Jeu-C5idF43hQXqgxVaFplPFt0o0f5l6c-yskR7RMRRmAiQANSMbrVbJijgNL-mv1vAA5JLd3cJZpuMsf4GBGimbqzHwFOWupB4lC5VOHmo129RdlGkkAF2nBHm0zVuE87fEshcG2AHdVRiPttI56t9VI8Hl8XBFcsNY0GvybSN0xXvhSUD9_ztyRuDvXMzyJGRMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ :
با وجود اعتراض‌ها و ادعاهای خلاف واقع آن‌ها،
ایران به‌طور کامل و قطعی پذیرفته است که در آینده‌ای بسیار طولانی ــ عملاً برای همیشه ــ تحت بالاترین سطح بازرسی‌های هسته‌ای قرار بگیرد.
این موضوع «صداقت هسته‌ای» را تضمین خواهد کرد. اگر آن‌ها با این شرط موافقت نمی‌کردند، دیگر هیچ مذاکره‌ای ادامه پیدا نمی‌کرد.
بر اساس این توافق و دیگر امتیازات بزرگی که ایران داده است، من موافقت کرده‌ام که تنگه هرمز باز بماند و محاصره دریایی دیگری اعمال نشود. با این حال، تمام کشتی‌های نظامی همچنان در محل باقی خواهند ماند تا در صورت لزوم، محاصره دوباره برقرار شود.</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/5711" target="_blank">📅 14:59 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5710">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c4fa249d98.mp4?token=Gu2utYP8anLLvXR2xqfgH-75CU-Rl7c19vmHH4iAOf6Tp0rzp6qigyK8ok4GPJ3v5gF9775kXHVUZSGxh-WpYorfI6ulA57H0ES7fwvX0JlFnt94p9-Tjj-mEDoYclUzevKIZYWkBmRLQa3Cm252MRHrs9RBW-m61zAkfRA4s_sLN_yjwCi26Lelhr_tVuonwh7eLFLGzS_mZh3b1ZiLiYmYoTX6a9o7xQBeI77oTU1jKnT5DZ0j_mhcpwmCDj4J7eZ_bciJp0IY-iYwt2BTxbD_qYCsvmWrdKu4CLp3v4mAADkJLWwJbqJwR9LUvHlaDwZiLm1mNjx1HTj4axQiDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c4fa249d98.mp4?token=Gu2utYP8anLLvXR2xqfgH-75CU-Rl7c19vmHH4iAOf6Tp0rzp6qigyK8ok4GPJ3v5gF9775kXHVUZSGxh-WpYorfI6ulA57H0ES7fwvX0JlFnt94p9-Tjj-mEDoYclUzevKIZYWkBmRLQa3Cm252MRHrs9RBW-m61zAkfRA4s_sLN_yjwCi26Lelhr_tVuonwh7eLFLGzS_mZh3b1ZiLiYmYoTX6a9o7xQBeI77oTU1jKnT5DZ0j_mhcpwmCDj4J7eZ_bciJp0IY-iYwt2BTxbD_qYCsvmWrdKu4CLp3v4mAADkJLWwJbqJwR9LUvHlaDwZiLm1mNjx1HTj4axQiDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار  شبکه «الجزیره» ، احمد ویشا
که دو روز پیش توسط  اسرائیل کشته شد</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/5710" target="_blank">📅 12:15 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5709">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v501M-PzVdUY2sa7PS4COAsCcFxrOKI4kg0NNeFMsJWxOjF0gf6Rprv_e55cdWkUev0RbJXmOyNsSNnwn2m-6W_G_hPzvalaW87P90K_l5Q6HWGUMgaVJMDogwxkHQLGFfA_H5gcQBJi0TFwThR_IBbRprIaqLHXqhkss-JD9h2inJdq97zZitpTgIBTHIUpjN3R8O2kYcBRw5xglN9ftVlj2o4vS1A76oAxzti4x3Ilg2uuT3emFp_g4hvMZbmIDtRmpGxT-r783bM6-g2av-ZIjrlfS1e1dnXpSbPzVn6sX_WyZMG5ZQUqn8VuerCqr3p86oyXNcCkI_Nwfmk_gA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حالا هم‌دیر نشده.
«شیخ نعیم قاسم» می‌تونه از اندوه پیجر‌ها و کشته شدن نصرالله و کشته شدن خامنه‌ای و کشته شدن ۴ هزار لبنانی در جریان خون‌خواهی خامنه‌ای، برای همه یک جا از غصه و اندوه بمیره!</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/5709" target="_blank">📅 12:12 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5708">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mddHZURYXByyeqv0zaJN7lQ5ohowcDjG7mvAmT-jePCHCb6NbUhX7e--TzaICP0X5WZkyLcSk9w_H80ivOs3CSIO53TukCCn-n-TJARa1W6G13FWXz58w-i5iZ5V7OgcV9eZM6DG-0A0LVJ88iYP9Zc2Lo2R3h4J5ca4zbz8kPwsHnT3oFdSteUXEYXbVCHKJ_qbc4ukG2yhrV7pfPJEUCxmmT5dwm-AYe0vuDJoApcUPd4RJRuONBgSeEVgTjVAiUPQ7wJPKm-B863vcQhVVbSCkYW6ypTcWfc84YAdkgDiheo15VtW4o7GC2RfmxcPxczsWoHaXuztmxTp0LQ_aQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فکر میکنید شیعیان افراطی فرقه جمهوری اسلامی  فقط با سنی‌ها دشمنی دارند؟  با یهودیان؟ با مسیحیان؟  حتی با شیعیان مذهبی که از فرقه خودشون نیستن هم مشکل دارند! تحملشون نمیکنن.  توی کربلا و نجف وقتی اونها رو می‌بینن دست به انواع کارها میزنن، تا براشون ایجاد مزاحمت…</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/5708" target="_blank">📅 11:43 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5706">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u0cxi3cN1C_5-Xj235YmV1XIGTZngQwhA2iF_2AQ1d4-V2Nc4WZS5AIV3zni2-_2Gw7C9wrQCPriV5NowFPMX2aVaaDiWOvH81aJW2lDAufrBEDmWftb0q63kySarLi0T6iJwgpPpre0NY4YFE9UdHVT0SmTInoSCJpNyCa42nEUQMguH4VNRub7rNH1zMZzYdQiTtIpngO7nnmUJG5EMsU3r8hgjPzwg-2DHg0X87SL3lTHlQKwNX_BUlWDOVGSmHqzrP0IFBwMQxkRqwUxLTuZN0PTtHx_INTKzlnE_8ny8UNM4r-bO2o16H_sePOGdOjJe-W2o7qR5PGnqlVf8Q.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/c656e44d19.mp4?token=Nn0wW2VERqqMIGtlBCdaFak7dvjXsa7gU59TwIHZZvs425Tm4M6Q1bV2Sd1jN2ylgsN0KiPG-C0GETuMEePvT3JxosDt1TFkkXWkHtN2iY9ipVEaoQvdtwVgSKEnXCMu9AHl4cQzxeg4f0qBS6xcyheQ6xo1MJHTpjywWDcaIA28bxOB-WG9ADOvVuli4ORnHRDuj6C8Smd6T9UvcMKkRX5WrTJJtpKj_ZTJ0UudA2ww0RzIM6PrmmKXvc5x-VP_y3aByTJboShGVMXDaKqnxcnXCQC2SUu5yDcEAUEu_toxXdDIKboACUHSlt5LGZCvgAbNZPAKh5laTbUXxu_7sg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c656e44d19.mp4?token=Nn0wW2VERqqMIGtlBCdaFak7dvjXsa7gU59TwIHZZvs425Tm4M6Q1bV2Sd1jN2ylgsN0KiPG-C0GETuMEePvT3JxosDt1TFkkXWkHtN2iY9ipVEaoQvdtwVgSKEnXCMu9AHl4cQzxeg4f0qBS6xcyheQ6xo1MJHTpjywWDcaIA28bxOB-WG9ADOvVuli4ORnHRDuj6C8Smd6T9UvcMKkRX5WrTJJtpKj_ZTJ0UudA2ww0RzIM6PrmmKXvc5x-VP_y3aByTJboShGVMXDaKqnxcnXCQC2SUu5yDcEAUEu_toxXdDIKboACUHSlt5LGZCvgAbNZPAKh5laTbUXxu_7sg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تنگه مفتی مفتی گشاد شد</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/5705" target="_blank">📅 10:37 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5704">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa6e1aeb6b.mp4?token=BjovtnactKmtxx3n1txsl4FRq3ovKjlNU3xe-JKgIe3doFrCcVP6-LxNb0PuPVS7sM8GIVept5hxhxlMsxso2hRMMRGsS_dQgw7odEcG3VJ5PryRaPgFmFCDpOgvXYZ5yrGVt-WMxZHbq0jFGlH1m0gFZUbMT3SYJitAttMQuaGYcIT1YpYM8o1sssoISUQvNrMGztiPnYXokCEjVrsqBF8tP1peFIaXJsh2aAtuiMOvjcNq7NUYb0O4tmATCPVbfmgFHWniVzf8FIrxrYf29WH0NhRsTorzzqE5JxUy11bRl-Qy5UGD1p-1QzIakGKK3aHHbb330zR7TGbVEG8tEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa6e1aeb6b.mp4?token=BjovtnactKmtxx3n1txsl4FRq3ovKjlNU3xe-JKgIe3doFrCcVP6-LxNb0PuPVS7sM8GIVept5hxhxlMsxso2hRMMRGsS_dQgw7odEcG3VJ5PryRaPgFmFCDpOgvXYZ5yrGVt-WMxZHbq0jFGlH1m0gFZUbMT3SYJitAttMQuaGYcIT1YpYM8o1sssoISUQvNrMGztiPnYXokCEjVrsqBF8tP1peFIaXJsh2aAtuiMOvjcNq7NUYb0O4tmATCPVbfmgFHWniVzf8FIrxrYf29WH0NhRsTorzzqE5JxUy11bRl-Qy5UGD1p-1QzIakGKK3aHHbb330zR7TGbVEG8tEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏ترامپ:
‏اگر ایران به توافق خود پایبند نباشد یا رفتار مناسبی نداشته باشد، من کاری را که لازم باشد انجام خواهم داد.</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5704" target="_blank">📅 23:51 · 01 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5702" target="_blank">📅 23:39 · 01 Tir 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PmKlOLfK2HH_vokRhZ0LsNMp-ur9Xfmp9GLHLWYjmeh_6hB4conunb8IYz67Godr8YdMkqV_x1XurTFcp2YnAJYRLSztAtthDwRaM9M9KKcZRjfdqLCQXSIqGDpfgAerWGRrg_XP-HJc9HlQ5YkQ0Sq_Iz9uGBbz0TyilsDD3u6Ef9cqVsOmPHLeb9yp4lFQ05yAeCxa0Ma8wgb6w5MHZNUo_NnTOUjhYp_V9SlFO7gP93KYMR8IoQ-RZeUI6lhu5pKvdI_dg6m58tACjGlxHYG2V_9Gt3uoN4MthP39vw6pbhfb1FZ0JrbXAYhhXYSZir3BZ7TjsV79W7I5YsWVKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این درآمدها هیچ وقت برای مردم ایران نبوده
هر جا پولی رد بشه، خودشون اونجا
قرارگاهی زدن و پول رو میزنن به جیب خودشون.</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/5700" target="_blank">📅 20:49 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5699">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pBACAkVSNVGv_X6Hh1apqZ_MoWrPCNYVpF2dSS2jNK4RuTmzE13SehhtnqyAxVKK1LTAz4UqBAAM-aqkBm9Pp9jLY7BZ-xFb7OImFsdmJIVF8dom8zDsqAKpX13ILPuIyTDkdKg_oKR34DJGHFThCBhj7jluB4-098b1OGkKsqwXxXSCSI-_LggQBMSOOqtVmFapIO7pn0ikmxxouM7-DcXnEoE2dcR3lSIoGveWz0QBGDs7mC67lhsamCBClTwbWgFbYod1xVMdIoY4V4JwVXDdzXPqEvxUjn3w-TOnGOKy2ONLsl5p94kn0E6bP0SWYTkKEhG9uRdz4XN6ldvG1w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/o5C_U4SSYTR_kKicMpEKRdKkrf6gOnYWUcrSjsEc3ugE85rbvv_8637uf4lBeRqHWFc7r6RnHjTaD0ZX-dPOmNpEduUAeh1XFwI9BRvXtwn5bpIAczgD3F_4JigClyWLt2-3Qe0jJbKn8M2qZCdQ9ku0kAYXxRsYgNNYicN9WnqD3D9arxEiYaRmoYuj9kScGSqaJDzRZMUDqVp7ukbzdI4QkW1cmUkshepOX7_C6A9JfZykxSX7NvReOtFkt3DOIwioph38uH4lxGIr3TXAhwPqxOjYkjNCtw4k8TbCjKUH0_KEztbo5LyBhe42EfG0Cqre0L3mI1vA0roHIE-kWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/B1ce1EEx1SlUgYpcN4ExarADVEtGZo_ZQqHSVXVUIldge-BQxtuzi8iEzc3ovBi9xw7o1RcEycBc3J_uGKOIfbDdFuhVWtMbrWESbRB2XqUOkCGvUe_PZZDe3ES6s19u89s1h-XcyPPCsw23DKl2zkQ1dQ0Pnz-BtOVMl0niA4LkRfyJSXHX0WZnrjxjsW-8ihKoh12SsYWKFAiU7iS5TfvbawHeKJTx0uXVgjTvXzHwhyY6E08jdX6dqbIQ5gUZNlCSj33hr12aRF2VHw1xTr_dhPn4OzThF_3EMsKVmm7xFHkZQq8BkV4N_wx8dWilQ2haOvptLfl5COjSBs2F_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ruage2xMytLMAoNMLEhBdkEXVFVHoqJZ0SSz98aMVINTLCVl8rLRjDKtfK45xYfVjVXAHTJcsKSFzNWsmSQL0TFClAL5RN-FLd5lyTk1bgvWudoaKLOWtX0_IuqtdS4k1yzT6VpxONj538aFaOUSFT9dlMhav11cUfoALl75RM70tNTDqe5WMdwWOMoSoZTsthBtId3SlOhFqgWcxsqtUSOayl18XFEo4mTTeSHvSVVTXjAzpuGqm8tXumATylnN60e-_vAEfb1X1FCE8JKHgWISY2rP7AVaLdyFFeGecAL0NM6EBuEw_YAhzMuKYg8Be95PG5SKQ1i6L183NCM2OQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Eo5zAbvzId4BPjuPvQfZG8TPCuMvVp4FmWguyx4E0t6FaQZObI_RAzxEIar27KX0n_l7lJLlajjrJ1l5tGb6sy4v0fc1QyDK0Q68KGKtGoCiOSg4l3hTV0_C_eDnTpS8kl66iqeIVXFFmliWE5ubHqwtP5uuBPuenSmFrGqZ2Y2-yutKu8cqMGU1jkw823y9_6wMbQjWr2CnZ2nWyaTS43pXQTsRJO4ZaTfh9JdAzXIN40Si5J8XLoCHxCOWQ_EeVs0XUGjIHwxCs_Bj1xereoeh2U7nmCO9v4tCCKbJ9TWPWrT370uEhcfeAF21q5GJ41osq9BOBCHaz5gZE7t24A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IYZbaoz6YOL6VeOnQWcLDrfZZNyUB_eF5ZlChYlCVgTIS01BJ4G4UoscHjUMdh0vf9IySAbUnXv0giXj_ci9PSuMbA0OuYRLIytFw03jZxyxU-KBIEgf7VB54_O5VGiis_Kmq2u0hkVnPllPEfW-gPbWWFIqToK7yIiYhuISKRtZOI6T9mfe032TTE-2PmM85TaMHywm5r34rdy1HbWvgrJoOXZWKEZJtv20-2cGhWeqsBBot0BA14WtFHCHLQwT2XI_ZZbxocy2x0CHxOGTedcwojSg9veB0CSPS98CfDC8F_zHklbbtkVWrjgWAjUqnF6BxFvECSqOBPZCMmAFhg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PGPqqsHk6G2aY9gCkT2AgVfbVjKh-l1nb8pQEINWyJ8oBU3uRcTHAla4HET3uUrYQ8fz8TdurhDWGDW04istZTZha5eZ9I1_zSHdHc2R998TbKMflmjcL_3WuIvTUsc2U68R3JuBx15N8t820hssyIAPT5yKjWRR1f3fMCgLDCHEh18h6IR94-OkjiJYp5dOD1-g1dO8BuRd5lMNZQtz5jkuoUqTqWlZHSfFKXcS3yFn_4Ohs8eGcdup8_9kTAG6zF0E70CoQ94bYgxZu8aRxJuT3_zZhIeNP1vdeBQIziEjtqhmPB30SDm738Ty3epxOdmfghNY0nXCzX_21evOcA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u80qA4OIYdCTntZMVNhPNVrGYEnBp7w-ZKx5Ru2eVyUitacmlLeEl58KWTcutEU_0vxtK2EHgK_booMFv9jvOxoOFH7UqAFJOTlshbAM12bq42Cg4wtOOUOuIOL-TXVyZUHItog77habHJRO17jhf3QOr1TsqgJIBTXqza2e_8-KV9rNWSqArrapTYdNlsKZDjTLgKDYALPnKzqKkilE8AET2lIf2r_nzXa7eGbVEhBuvOIj6fdSVHVVT8JBocmdL0oeBFEDQIswWe9qCdeubu0Mz3MoubIFwksgKCE4cAHnWg-sHsvNRzm7jyiCzup76gtRBaeF98R2UH9-4CPQ5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
گزارشی از شنیده شدن صدای یک انفجار قدرتمند در دوحه پایتخت قطر</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5690" target="_blank">📅 23:31 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5689">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🚨
گزارشی از شنیده شدن صدای یک انفجار قدرتمند در دوحه پایتخت قطر</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5689" target="_blank">📅 23:21 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5688">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/myeLHpZdZl0Sj20eLYQAVOGF3CaDJ0eqDxMBtDdlMFKr7t32Iua1_Rgv-cU-dHRoRiTEysoV2BCQw5Qi-eUuF1D47VadLGwiV-akJUecElnzJDTwL76qFhAQhAj7s6FZUUGMq2ej9UAuNtCjDN1soQgEBBQrlQ0GOl1LD-nExsySCAnItUpweVqlrANA5Zc4U8mTWDLQtIhS0tbe1BKeYa_7wpCh9Ljh0aeXIBBme6bNrJ-hht3OXMWuoPp50wx9Ue-i7hEz3zBbvpBRr4XviwBeFSDIPlSfsIHjxIX52ZZUsMLL3DI22aJ-rtJaapV-FyLfa4452LHItyKSbFNezg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ورزشگاه لس‌آنجلس</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/5688" target="_blank">📅 22:55 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5687">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vluhS8IHW_s63oC7MK6BEj6xVLzuDRBG4Mv2-rMPe_OHm2gFM7c78e2BfGro44swqZRNgLj33AbC7X_W-QmpcqrnRRNT9XOMZmLGtbidXBa57vtLrGx80ocDdsWu7xILzU4NaboFQpuOX3lGzGbVoCP2YZJCx0aIH0HbN-jCzsYekMW0JJ1w5cyVkmQJB9L-uVgUgkpoLipb62l6Ayi3WoV2DbG2izctgSmYXWwlBgyeTzVgz4OHkSVhK9xayR5Dp2NhtaWkJWq5MWhAq4_OxLoY4whn0IobU4t9K1kwe6bK3jIWd89HJVC4sFo-chHmGdME_jwTvafI2ZGx7EjZMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پاکستان و قطر از ترامپ خواستن
یک توییت بزنه تا دل شغال طرقبه راضی بشه.</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5687" target="_blank">📅 22:43 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5686">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PUyz5PzPaF65SPO9l5-a0RcazJauYgCJTplBGcqSJC9JMSom5DyyNVfTizcPlv-STXppfcOruxcHKbgiK5H0Zxl6wDPTEu0CZ9rBYu8z3mBC91wwHa5gueLskrpZ3q3oAU0rDNQQpm-Ofas6BDJJPl0nsN9zz0vE5dvW3VN3VQ34pfIKv1HUBdBDAiTg3bruh35Ooi8tehGyeGcGqw7BFsDuUZFvp8zowNHTvVFLx72EBSJpBw9br9OmKzrZX57S-4szLhG95OYMVnIz_5wgM26nPUEZf9hBvONLuWYMM3rF69F_alwfaDV7S-G-VZ9V0Taw9tc_wvsqfJ-G0Gwklw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جی دی ونس و امام قالیباف</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5686" target="_blank">📅 22:38 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5685">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VpnI6j_pdYBeijCIkivDB3LZIPs_9E_DrJ0AUdSRg_DGKLUwlGM-R9g9y5YMbiKqG2J22ppmhzB17WZ3eIeB_9iW8pxBFaBuA3yypEB81xCEHFbjkKU8J288ZupzBvI2Cba-tXLf182-PRKlYGP4Md6kHKVx0vmrrzbKuLzeCOvN3Kob4U0ZNhB3bnEvCAinOU0V2QbBAlIPEyE2WhHNsIXDU7WVCzhuidIG0W4T6JBxO___dD60IUyfBLZcVbLsLfuYG_iz3D3KV0oNsiVadbzZcydaZ-27k_bxAix1Bx21GemzhYmvnbtSPcZxzVSE4Hddh1lcUT-xfBAxp6PiWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش اسرائیل از حذف «زکی یوسف محمود ابومصطفی» از اعضای تروریست حماس خبر داد.
او در ۷ اکتبر به اسرائیل حمله کرد و از جمله «یاگیل یعقوب» ۱۲ ساله را ربود.</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5685" target="_blank">📅 21:50 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5684">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LK4IBdibZaexZkxPMROtmOhULf21vKKv4trmeS_tnOzfuhloGZ22DHsQCy31-H0b2HWBzRlmk75bZjEUhScIMR9pBOBY2KXvEYZ7M4hB8xND5SExigQV1IMNDIqVfbHcQYl_7vsiL9ztMwYFx3kEUzsIQAkom6-VgrduqTjRvxgm8c7vtSE8JzNJIKxYIJnS7DI5PeAjiGBuj5W8AT5AOo68fcHLloVAxfxfA9c2oMDmmutsH-Qe8yam0oVOPjsPkn1Hx75GaSHY_kNNcVoRbSvLeKu750RDCl7hOtOJuTwszF_z2-9HXRp-WkRNmaYv_VZYQ-Qk0Q_sh90jL9A7zQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q1GF-dKrqGOev8ALjp0aGLgo9lnvvsIL5oYAlXQkxpETOioYlL_XC-IVFJzmr2qlkScSb9PD2zap-wbk3XHTQgSox1hdXNzDXdyt-BkZ-Atvm0uVJmKmRh9K27Zpu9OVqaF0Ii2E43acuUsAWrLRwmjuugroMbWHkRJ1HanWW2Bm9uw18GNV-S87g_omoZH31krlthOvzCC50IWhCLubW88NtxyXP9ypdDPrH5nQSkWPjwBKh9AqpLleJKKxdbfDAgNxboQIZmnbXcrmdUx3dHqqtRnrMPRbVUV5yaKeuBUm4d3kqtNZ5OaLbzlVK--4C9uD0DOxnPiI2CYZfZZ4HA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس ستاد کل ارتش اسرائیل امروز به جنوب لبنان رفت و دیداری با فرماندهان نیروهای اسرائیلی در جنوب لبنان داشت.
جنوب لبنان تا همین ۴ ماه پیش در کنترل نظامی اسرائیل نبود!
حزب‌الله برای انتقام خون خامنه‌ای ، دست به جنگ زد، ۴ هزار کشته داد، ۲۰٪ خاک لبنان را داد و حدود یک میلیون شیعه لبنانی، بیش از ۳ ماه است که آواره محلات مسیحی و سنی و… هستند.</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5682" target="_blank">📅 20:50 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5680">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca65ce2ecf.mp4?token=QdJltQ3KIn4eHMeeCn-vDi7Qs6ldt5UwwuLh8vDXhRnbzTVX6Krum6HWR91j0AAIY2JwaZtVR-CtRS3RvaNfeu51FrAKrLqy2RXsZK15AlL5S19Ib-hUX0rup_3mZURHsJqrQKTUOLVGnE298xquope7jKjCi7JtNvX98UtK9H1Stqop6kUOLAocN7hA5FPbpsErSEby607xm8dxxxfo_bRZ751l6XdGw4zuWhM_PozIR2ZyBWwuNy2GAV1LuG_vYJwnAXwOzmFeq5LN2gyuLsw1uA3lxIv32C_2pw7l56XyKjA0XxvnnxBYE_bq9dT4XA419PQbL8UtpyaYqik_BQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca65ce2ecf.mp4?token=QdJltQ3KIn4eHMeeCn-vDi7Qs6ldt5UwwuLh8vDXhRnbzTVX6Krum6HWR91j0AAIY2JwaZtVR-CtRS3RvaNfeu51FrAKrLqy2RXsZK15AlL5S19Ib-hUX0rup_3mZURHsJqrQKTUOLVGnE298xquope7jKjCi7JtNvX98UtK9H1Stqop6kUOLAocN7hA5FPbpsErSEby607xm8dxxxfo_bRZ751l6XdGw4zuWhM_PozIR2ZyBWwuNy2GAV1LuG_vYJwnAXwOzmFeq5LN2gyuLsw1uA3lxIv32C_2pw7l56XyKjA0XxvnnxBYE_bq9dT4XA419PQbL8UtpyaYqik_BQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همین شب‌ها:
یک مراسم عزاداری در‌جمهوری اسلامی
و یک عروسی در غزه</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/5680" target="_blank">📅 20:42 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5679">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A3-frucARm_l_GpsIjFBuOaM1gIzqPAEfKima974b3_eFaZTfXzablxE1pQ6YdpYmhhjQGjQwzObfbq2BKFsiE75p7s85vQVu1luoRL2XMH_BemcRr0GzZ_u4QgdB4CBo-Eg-JqukZRPpNMr7zniurw9ULxKSs2r6ySL8os2dpjyM8Kom4Y4rNIgnfC7RVbKxsW9nkpZgcHBfSt-4-LLM9gmwC_ZULulE57TDAtIgaLPojiLmaF4k0ixv4CyA6tM5yhKNl6tkp0Y9tiktD8UxqeNPZCYwhOrYSn79qsyN-3njgWzQaGEFlIs1TegunJ4nQjNS60xeCj-lvlA46aA4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینها رفته بودند مذاکره برای حل مشکل :)
در حالی که تا جمهوری اسلامی جمهوری اسلامی است، مشکلی حل نمیشه.</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/5679" target="_blank">📅 19:42 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5678">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd078eea01.mp4?token=bhFE0SEJCfgGLnLqc7OoTKYz_kxXcmUnW59R2N7CQmkMf_-jmwUrR8yGY5MQYYwDAlYfkmz8-ICzXNxsjqURVXzACW6YWP5zx3B_MuXu6ds9gp7GEg6e7n2Q9dgKUCTdc4ZZCwcKlKTbcC-0jzhsvxeKw6AqTqwir2AV2Hi6Uibz54lgurOhyFJQOCBqBEBjLi_mFbDuZpKtIhlfEWQycEX9xELQRi0fFcCEJtaaQpMhjdtPnfZQbKaevEw4Urc4nU7g-0lrDjHXz0soPgiYLx91oJQUeEjZRapFJdzsh1_B8naQwOKoaNimRLaIyP-6_EYnPmLG-s3-MuFau1EQ9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd078eea01.mp4?token=bhFE0SEJCfgGLnLqc7OoTKYz_kxXcmUnW59R2N7CQmkMf_-jmwUrR8yGY5MQYYwDAlYfkmz8-ICzXNxsjqURVXzACW6YWP5zx3B_MuXu6ds9gp7GEg6e7n2Q9dgKUCTdc4ZZCwcKlKTbcC-0jzhsvxeKw6AqTqwir2AV2Hi6Uibz54lgurOhyFJQOCBqBEBjLi_mFbDuZpKtIhlfEWQycEX9xELQRi0fFcCEJtaaQpMhjdtPnfZQbKaevEw4Urc4nU7g-0lrDjHXz0soPgiYLx91oJQUeEjZRapFJdzsh1_B8naQwOKoaNimRLaIyP-6_EYnPmLG-s3-MuFau1EQ9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/b2464c582e.mp4?token=BV45j1BS9l1db7BmjNRDnsIMQuQFbkCJAccbHfuNW_r5V7RLD1eoYOC4diBpNHUTzWjo4Bp3u9r-Zhgn_EVGyUM5W3zcCThTIUQt_EOkQXZCiEYNcPMzob2rwrv8y-lW4JXIGVx3du8v9N37M2EwcXWCQzkagcr-sl7c2YWP_EojxsoquvCBx2OLhtLl9n9BZKyDNuJIXvKKStdXrY3vd5nhKA4xZ366iNtLoG_NiElF1-4M0CyrlP-BCRyl7_GT7YSdcJZwxZmKlvd5fxFXrTvkazp54ErdaTRkXGptTRL6z27pVGNh3nuuQ3TDvHc0OoKUDL3vWPKZXEVnO2DMiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b2464c582e.mp4?token=BV45j1BS9l1db7BmjNRDnsIMQuQFbkCJAccbHfuNW_r5V7RLD1eoYOC4diBpNHUTzWjo4Bp3u9r-Zhgn_EVGyUM5W3zcCThTIUQt_EOkQXZCiEYNcPMzob2rwrv8y-lW4JXIGVx3du8v9N37M2EwcXWCQzkagcr-sl7c2YWP_EojxsoquvCBx2OLhtLl9n9BZKyDNuJIXvKKStdXrY3vd5nhKA4xZ366iNtLoG_NiElF1-4M0CyrlP-BCRyl7_GT7YSdcJZwxZmKlvd5fxFXrTvkazp54ErdaTRkXGptTRL6z27pVGNh3nuuQ3TDvHc0OoKUDL3vWPKZXEVnO2DMiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دور اول مذاکرات به پایان رسید
شهباز شریف نخست وزیر پاکستان یه میز برای کنفرانس خبری و نشست آماده کرده بود که ج‌ا، آمریکا، پاکستان و قطر اونجا باشن،
وبی عراقچی گفت نمی‌تونیم اینجا باشیم!
و ننشست و رفت!</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/5677" target="_blank">📅 18:56 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5676">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OiJvWzEgJK0SQkydT8OYvy_fdp3u3A_0irF5l6HObYd_abizcr5foisE2yVWqo3R76RGSk4e-_zNEKmg9qgjSGq_B6simCEWkqEC8zZoCMNdODOftAe6Qwxc8jS95007w3Van4j67M6hKp3ToBFIE4BPYPZh5VcvZ0Or8diqNbjA7pyijsLoO2rh8mtahXEA7p8SE0uc8OOr_L4-SwEgMwaZSNRtGkQhPWuPqi5x96GoknNPB800lotabzExD2ZSrz3zJrp4Pu148rUxtHqnqtgHI7vx_sf50IZM32azMYhtohdyIL8x0dSl6bWV03OSOmDwh4H_mnpTt9a9cWQsIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/5676" target="_blank">📅 17:07 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5675">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7b14c3d6d.mp4?token=Po6V1GNRrFdU7Tr86CFUF-iOgcFHbCqUQtuz8hq9FzUEG60ny6g6zy_S5E1WFpAYWJZ2360ARi3GyFZBC0vqb3CYBYvWTAFo2xWLBDPPh1sWllpicfHTMtZ-smMTiK-fDObpB5oABWw9HNkJcWObF74YpE6yy3N92sQHxILup6tR0EMr726GNXRWXMiAxHEkfCX0ItOQ7cRg1u0rEUaVPgBev28o6COP0NzMrvr9u6j3-W9W1qOf0RncmyIWF1X5vr-BrG2r8sWiOng2qZ8dlhqrI-iCGCi4t6AUgyhMn3SKHKzWXmhUMU9pAnKi-m84GJQuIWcFNK1BQnFopvOuIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7b14c3d6d.mp4?token=Po6V1GNRrFdU7Tr86CFUF-iOgcFHbCqUQtuz8hq9FzUEG60ny6g6zy_S5E1WFpAYWJZ2360ARi3GyFZBC0vqb3CYBYvWTAFo2xWLBDPPh1sWllpicfHTMtZ-smMTiK-fDObpB5oABWw9HNkJcWObF74YpE6yy3N92sQHxILup6tR0EMr726GNXRWXMiAxHEkfCX0ItOQ7cRg1u0rEUaVPgBev28o6COP0NzMrvr9u6j3-W9W1qOf0RncmyIWF1X5vr-BrG2r8sWiOng2qZ8dlhqrI-iCGCi4t6AUgyhMn3SKHKzWXmhUMU9pAnKi-m84GJQuIWcFNK1BQnFopvOuIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جنایت‌های جمهوری اسلامی علیه مردم ایران</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5675" target="_blank">📅 16:58 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5674">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L3X7_CpU4rK9wjV7lsTOngEMuOaMwZq5IgMqCJVmyti16GfoiNxrJpAsB9Ih0JmBrsVlU84aBISr-_5P2e23mBlp9xqMwTVcem8fAquqC8a0UIyjegr_oPknrv8mA_xzpH2Rpto5HeS1EoUzrxyzpRnNn19gpM-YcyHQDSYtd1NI65aTz3cjZBbiLwG_kr4AnyiWMbyYqU5riOPydLoSnwgqNHIvf_FmBSLgens0RZrRxlL4O0Qjx0NeXJY6qOKHyXbLVFhV3ZMUseV8SZtRNrnEW8C6KXQ6iLK3PkJAziN5MkxgVxy_FqOaxRvSrrswn-ZURGVzj2prY7eQrFBIZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپِ کیسه دوز به فاکس‌نیوز:
«آمریکا می‌تونه به فرشته نگهبان تنگه هرمز تبدیل بشه و ۲۰ درصد از نفت عبوری رو برداره!!
اگه لازم باشه، ممکنه کنترل تنگه رو به دست بگیریم. آن‌ها رو به‌شدت بمباران و نابود می‌کنم.
اگه توافق نکنن، از کشتی‌های عبوری عوارض می‌گیریم.»</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/5674" target="_blank">📅 16:53 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5673">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ol_nBzi0BcQUJ67nPm8wwda2ya57A7xssqm5YaxS-r6GNp5OxEA3djc0sOR8SnpiMiqcmk4MA3p_wIJZMEvIyDchNTP5HWDJQI4uCYQJabbQxJbBhcY4_EFS2flJeQPPOorr74AXzE_3WaE6GZlluZPR1Skmb-EQlqnSjklq586hD6b4glvqiAHZ7hu0ClbDnvIBP7GuW-NnkZnffvn0FwOM1pzTROyDi38ZYd8eva_z-8NZTeoHjtgdugh8pWMmBFd2TwHRE-5kcIo9p__xl8jFh_FqyEXRIqpnBXLsQWj4YlVix_TOvtpmcum8ZTkpL5iC2qs8lsww7nA5ulIgJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حامیان جمهوری اسلامی میگن همونطور که آمریکا به اسرائیل سالانه کمک میکنه،
ما هم به حزب‌الله کمک میکنیم.
امریکا سالانه ۳.۷ میلیارد دلار به اسرائیل کمک میکنه. این مبلغ میشه ۱.۴ درصد از بودجه ایالت نیویورک!!
بودجه ایالت نیویورک ۲۵۴ میلیارد دلاره!
میزان کمک آمریکا به اسرائیل میشه اندازه
۱.۱ درصد بودجه کالیفرنیا!
ولی حجم کمک جمهوری اسلامی به حزب الله میشه ۷ برابر بودجه استان خوزستان!
۱۲ برابر بودجه آذربایجان شرقی!</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5673" target="_blank">📅 12:55 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5672">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">جمهوری اسلامی سالی حدود یک میلیارد دلار به حزب‌الله پول میده،  در حالی که  بودجه استان خوزستان  امسال  ۱۴۲ میلیون دلار  بودجه استان سیستان و بلوچستان  ۱۲۶ میلیون دلار  و بودجه آذربایجان شرقی  ۸۴ میلیون دلاره.</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5672" target="_blank">📅 12:46 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5671">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a9qP5bxZuDHaLGAl9lZUsVxUh6kQZUSGvqDYteMggJUwygvwgb7W36GWyVGYRiPYuZVRUzJaTY8NU9rHF9JhA6GXn5myYj5IjT1hnVMUXM5cm787ah17BvFeysLjdcpHqOVLFAc20wk4dUQAjfLkNbOPKvUFFumLCTw2-O8XZ1iwfh_OlZQWE1UnrDdDi_jY4bZSgpQ5Rov47ne49Ttk7AKNEV9sMbkhuhSBUS2oGDbvtrLL-4p1KHE1kAqOMCaUezhurYy7UPnJmi0eHsoYJG05e6q7Z2HgkEHuQ234jDWtPZrGDsqg1sMWS0j0fGjIQT9oMKGL6LFyLgyN2-xEFQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BxeJUuQDW40qhSd5b0cynLgDeU-sXqjwc-cmwLOKmd3ktWYJ-V4PegXkANGq5V04oZhE-2Wl-4kUkZsdSYSlSgX8gYyVrLz0dItDONUDqWxDVyRBy_-eqUR4KeHXEZCen1DwRPrBJunTNVcn7E5rktXBiQrUqocaDA3mw-8MMLkiW3HillowBdakSu6KIzqhlAb9U14xwxytbg4rn4QuYHNpIGU9zWHQFmH8p78GjHISfyywZwZw-u4KY4Wn0mZ5DZuOnnbQ4YHWh-MEOeOYI9S8x_MGJok74Wto7SrRKp451ZyMgaPtGU8e0_lrz6Ty8dJLPgmCQQCjwUeTCnuSYA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/228de5708d.mp4?token=UB1I6i907KTLi3TuzSIfN02Exh7PkUWCAkdw8KnOp3K12b6q5dU_8PZ_tOAFBhsjhESBP9B1RijL_rgEMPYRsF7nxtPUoaBt8jJdrTEHIAnh1ST9Xi2tKLr-Nupr48KFGD7sQDoDijinb4sqCl2efEVSbtJqSf_kwBy_8mBcgs1BZJGRLbedWOHgS1NYN5qq0SgqZ2wAapu355U4PXmUnelsbQ4aY60XyUFrCoVzBZsLphrLBFeKkTHpMKvRLeh4539AHxZdJSgIV9TZVYAp3-ehT73kyW7FIP-JBgxH4p1KxNrvqQrqRcREiwlu22Jq7jd-U0uSlC85I60DZrbzrw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/228de5708d.mp4?token=UB1I6i907KTLi3TuzSIfN02Exh7PkUWCAkdw8KnOp3K12b6q5dU_8PZ_tOAFBhsjhESBP9B1RijL_rgEMPYRsF7nxtPUoaBt8jJdrTEHIAnh1ST9Xi2tKLr-Nupr48KFGD7sQDoDijinb4sqCl2efEVSbtJqSf_kwBy_8mBcgs1BZJGRLbedWOHgS1NYN5qq0SgqZ2wAapu355U4PXmUnelsbQ4aY60XyUFrCoVzBZsLphrLBFeKkTHpMKvRLeh4539AHxZdJSgIV9TZVYAp3-ehT73kyW7FIP-JBgxH4p1KxNrvqQrqRcREiwlu22Jq7jd-U0uSlC85I60DZrbzrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در مظلومیت شیعه …</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/5669" target="_blank">📅 11:07 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5668">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd9d936798.mp4?token=LjHewbWN0RMwe-znN_2SUwQAlj-q3zcDq3pCO2QcrJuCB-1iVMz5_Hr3SUDgs9b1jNYi4jF35VnnyqFJC23F5ioeaGgCP6Gx9ezrJnueQD32tLmHymiKe42H23NDM070zSPECLly_baG68eOtp43JlVsBXNDrA990fVV_N-66SxKQI573o48AWsIrLfzncvhwEgueC6-cv_4pDGKv01-QbNfMASLGjjAqblYwyUR4YfIJobguPfelV_-qKIDAv5v_zeuDMjVAK5fzguiSoTrjdfEV6vCYvoVjbWQSmVNHpxpnLCNhR6JYkXcIECjZA54n-QMzhfmt7yzmBD1C9Jd8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd9d936798.mp4?token=LjHewbWN0RMwe-znN_2SUwQAlj-q3zcDq3pCO2QcrJuCB-1iVMz5_Hr3SUDgs9b1jNYi4jF35VnnyqFJC23F5ioeaGgCP6Gx9ezrJnueQD32tLmHymiKe42H23NDM070zSPECLly_baG68eOtp43JlVsBXNDrA990fVV_N-66SxKQI573o48AWsIrLfzncvhwEgueC6-cv_4pDGKv01-QbNfMASLGjjAqblYwyUR4YfIJobguPfelV_-qKIDAv5v_zeuDMjVAK5fzguiSoTrjdfEV6vCYvoVjbWQSmVNHpxpnLCNhR6JYkXcIECjZA54n-QMzhfmt7yzmBD1C9Jd8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عاخی … رهبرشون تنها و مظلومه!
یه چیزی درخواست داده که هیچ کدوم از سران ج‌ا، جز جلیلی! بهش رای نداده!</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/5668" target="_blank">📅 10:32 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5667">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ff3016eb3.mp4?token=U5nkjVR6ntv9bmG77MgS4ooJT-98M06a3wa29yOP5tDJDwMFl8wHzj28HicRVofCn8agK5MumlcybB-Azc3gSi4vT9uhu4cjq6suog-Lv8SxxS-lHOWpaoYCvU9PIf_6EXtFON-Na-OLf-UlPehT11v5DooDOe6dt5ENVYyAfKtG6N0ioiFbhz8QlzQ1QSBLAc0NLGOqXzeFmLguN9w6GxU2aW7T6bCdZoE8balpszk1ZP2jW6FNO_IvZbSWwGYN3nQQQ-ykHB1AwmiHNRXKSHXAe6aLan-D6sfooG2m-DBuLOz-24AMad_7B5qLboAEGRAWrcQe4p1ELzhj09W3cg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ff3016eb3.mp4?token=U5nkjVR6ntv9bmG77MgS4ooJT-98M06a3wa29yOP5tDJDwMFl8wHzj28HicRVofCn8agK5MumlcybB-Azc3gSi4vT9uhu4cjq6suog-Lv8SxxS-lHOWpaoYCvU9PIf_6EXtFON-Na-OLf-UlPehT11v5DooDOe6dt5ENVYyAfKtG6N0ioiFbhz8QlzQ1QSBLAc0NLGOqXzeFmLguN9w6GxU2aW7T6bCdZoE8balpszk1ZP2jW6FNO_IvZbSWwGYN3nQQQ-ykHB1AwmiHNRXKSHXAe6aLan-D6sfooG2m-DBuLOz-24AMad_7B5qLboAEGRAWrcQe4p1ELzhj09W3cg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/cd300c19c9.mp4?token=VaLb_q6fYPSm43TAx7oixdL9DMKJYxP7IWfi04dytHuVPTYXcMEzSPEMSpXLJrMHja3K3ijBpWUBrJgH71qMonngRhBzpXk4m3aK6xlNLgVsuNt0Irf_Pmk4Q-iG_iQJksXvsmRSeYosmLi7yCfXIUCpos6mlSiS2uxz3fTf7Qm182m0LU_-PlZDKJ5MR0Qg3ElHL7QK5vR9dUmm9hLq7ItHpVfiLGWlYyoRbId5PNZjM0SDm1T_UDk_uf3983USuj8JL5X4HZxNY66Gscyp2Q9wCPDRpmtctZst56qTxPzjpEAKDbOFwMIVuVS_eTl91GUxT6VDWLoKAyAsS66ayYGOyFELDca0ZO4XjdniULgynHsVaufckQeFCkEXcJzR06UEMJ-hcaoHOQLryOrWw90doMdplTw_LMh5ftbh8iPfo7Z18eK1Q28wgFmPp48HzyeObpE68t42Ya0KtMrh9ILWiYmt3pyfeIcZWjgFbNNWij1SJl2AmosiE0mZl4RlDgudeKAVoIZG3gDwktp7wz03oXTzuypgsMEhZFAeFcEHiGNfxM1kE-pzfigWAuBmfws93dkA-HYt7V62Y1zhi0sKcuuEiqWkEEwgvN_dCRajvyHzkw_AusRoz48H9CTZPY4gb-aeSXU9lsUYsTCXV2uKVsGFMjDGWDPZ3TU--Zc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd300c19c9.mp4?token=VaLb_q6fYPSm43TAx7oixdL9DMKJYxP7IWfi04dytHuVPTYXcMEzSPEMSpXLJrMHja3K3ijBpWUBrJgH71qMonngRhBzpXk4m3aK6xlNLgVsuNt0Irf_Pmk4Q-iG_iQJksXvsmRSeYosmLi7yCfXIUCpos6mlSiS2uxz3fTf7Qm182m0LU_-PlZDKJ5MR0Qg3ElHL7QK5vR9dUmm9hLq7ItHpVfiLGWlYyoRbId5PNZjM0SDm1T_UDk_uf3983USuj8JL5X4HZxNY66Gscyp2Q9wCPDRpmtctZst56qTxPzjpEAKDbOFwMIVuVS_eTl91GUxT6VDWLoKAyAsS66ayYGOyFELDca0ZO4XjdniULgynHsVaufckQeFCkEXcJzR06UEMJ-hcaoHOQLryOrWw90doMdplTw_LMh5ftbh8iPfo7Z18eK1Q28wgFmPp48HzyeObpE68t42Ya0KtMrh9ILWiYmt3pyfeIcZWjgFbNNWij1SJl2AmosiE0mZl4RlDgudeKAVoIZG3gDwktp7wz03oXTzuypgsMEhZFAeFcEHiGNfxM1kE-pzfigWAuBmfws93dkA-HYt7V62Y1zhi0sKcuuEiqWkEEwgvN_dCRajvyHzkw_AusRoz48H9CTZPY4gb-aeSXU9lsUYsTCXV2uKVsGFMjDGWDPZ3TU--Zc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از دوربین جنایتکاران جمهوری اسلامی
قتل‌عام مردم ایران در شب‌های خونین ۱۸-۱۹ دیماه</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5664" target="_blank">📅 10:05 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5663">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/845f6aff27.mp4?token=v0rB57KFhYswTUXTBOxGR5Tm9LPIgTC06noPmeOXVqubj82aRC4K3GDO4JwmMmO-7DL0vzY2vbE90DVNiSGPmlf58ZtiemYfPXhn7M9v6ts-_ZWmDhJ1UrglutoMg0EGAbuF0NRfnHT6ZZqq1xa0hGHLBaUsH_4QbGmCzTST_aJ2L40ErUk1DDJm7CZuzbEnAZm8eOXE1mhK6yroR2_7WOxVoIbK_5cn-An3_FWd83-zg0jz2_BTy7CTdVglnsBLcLGuS5k7gHA5LtqvJHMfcCagjB2P88XtQIBZ7nvBPWxpmmlhIVY8ojh7G3PN18WhnlvVJCDTfaqAQxw3xwiZoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/845f6aff27.mp4?token=v0rB57KFhYswTUXTBOxGR5Tm9LPIgTC06noPmeOXVqubj82aRC4K3GDO4JwmMmO-7DL0vzY2vbE90DVNiSGPmlf58ZtiemYfPXhn7M9v6ts-_ZWmDhJ1UrglutoMg0EGAbuF0NRfnHT6ZZqq1xa0hGHLBaUsH_4QbGmCzTST_aJ2L40ErUk1DDJm7CZuzbEnAZm8eOXE1mhK6yroR2_7WOxVoIbK_5cn-An3_FWd83-zg0jz2_BTy7CTdVglnsBLcLGuS5k7gHA5LtqvJHMfcCagjB2P88XtQIBZ7nvBPWxpmmlhIVY8ojh7G3PN18WhnlvVJCDTfaqAQxw3xwiZoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/f28d8f2fab.mp4?token=m0Wb6xUJXwXz6Ro6Hhha0iXml0jk3eK4PY99GP_b5W3yf3rpaJ3lsHqHGhl54BH2cwnugiyU0zq1c5mRgcfNHbGjuNVinwCcwo4_2edP_DGzJJyKZ856xax-rhYUTQtY0vLeAN-N0WnkpcBDpTqpIfTQHfJ-Uc7H51hCTOenTPF3Y1IuhjPldBng-JIV7D8Gjr2YFfPtIk_XBjLEEQxbqmbvFKJHUSFNFgnXAyn9PAIZubRL9Wm52vbGvrRST3AgUZXTwygtwXRsC005svu3y2Ibs_JeZRNPZgsSmlYgO9WAnOCvbGCbNL0e-0VX6YmibqtCb8Al567TMioj8pCzfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f28d8f2fab.mp4?token=m0Wb6xUJXwXz6Ro6Hhha0iXml0jk3eK4PY99GP_b5W3yf3rpaJ3lsHqHGhl54BH2cwnugiyU0zq1c5mRgcfNHbGjuNVinwCcwo4_2edP_DGzJJyKZ856xax-rhYUTQtY0vLeAN-N0WnkpcBDpTqpIfTQHfJ-Uc7H51hCTOenTPF3Y1IuhjPldBng-JIV7D8Gjr2YFfPtIk_XBjLEEQxbqmbvFKJHUSFNFgnXAyn9PAIZubRL9Wm52vbGvrRST3AgUZXTwygtwXRsC005svu3y2Ibs_JeZRNPZgsSmlYgO9WAnOCvbGCbNL0e-0VX6YmibqtCb8Al567TMioj8pCzfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5661" target="_blank">📅 23:07 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5660">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mm_KO2XTasTMVtbX5puQx2maqhbyCU5UHKNbNbZGQxPEC4zx0R3Is7Z7GnUJVZXlJCNhRo-j8fDY23uUxb0-jaivmlfUiuzbDmakFolXYO8lyrvCvOu1WAvGEkXu9dnJ7UFyiSLrOftDaL_AIzx4ziBIQG_1o4_Zf7jokU45B_n6tuURS2cmfjZts8_C0bPZyAMd1H_Oel53-IcAcMYjh2RciH64nTGm8s_mYFeYInLOWUCxZt_DWwAvTkiCx654PviTwoMNKQXYTFeOTniN37_Ocs_E_DZW6-fGSIWFjvT3TpCpbNiHpeJIMl6UjoVKaKoUtFTCo0pyTbrcX3zAhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/5660" target="_blank">📅 23:07 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5659">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9adbaa46b5.mp4?token=N9fsyElcTLA8Dl4-7OBDUPlV01NC73XeSMxW2p5kGs5GQ1V56xXbWV1-7upbNN-ZdQFzgHPTYvK7pPh9yGKnhnkMeE4ZKnJ3kAq7YRSLtxkpVnJdFGW6YHe8THf5cPFU-RUkQKkYyfgbnxDI5p7I0XkEhaDIpJ-OoSHW6GYPclawZtP29NrARQsNOdsNoigoPLqARqHLzdRd4_bjYFmOA9yAzqquz2rbnElzoXK7xax0uFnpam2GcT2aFjvuBJesIcEEVhhynuuP9SvuWqtKIvjsVHZkOId9v4b138nvf_SRrHNKmeES-7DMu7oaJGL40U6JDA-l2EDes1WkVb3GzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9adbaa46b5.mp4?token=N9fsyElcTLA8Dl4-7OBDUPlV01NC73XeSMxW2p5kGs5GQ1V56xXbWV1-7upbNN-ZdQFzgHPTYvK7pPh9yGKnhnkMeE4ZKnJ3kAq7YRSLtxkpVnJdFGW6YHe8THf5cPFU-RUkQKkYyfgbnxDI5p7I0XkEhaDIpJ-OoSHW6GYPclawZtP29NrARQsNOdsNoigoPLqARqHLzdRd4_bjYFmOA9yAzqquz2rbnElzoXK7xax0uFnpam2GcT2aFjvuBJesIcEEVhhynuuP9SvuWqtKIvjsVHZkOId9v4b138nvf_SRrHNKmeES-7DMu7oaJGL40U6JDA-l2EDes1WkVb3GzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">غزه</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5659" target="_blank">📅 22:34 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5658">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SeQBwENiNqDzeslmKbKYJtdv_CWNzfHlvw261BftL9sKMN065mfLB0tw8iFPZPqZr0zd1hXIlPFKzhUP1WBLovgFBiEI6RzN6xdqJZSxKqF4KkVxRK8d3tVeFZggp1cjJDN3vy-0jFjmvPj91SoY81Tf93IJJA1-AWlQKE0Wh3FsFG2xuE9HTVrcHRNeKvY6oeyHABb2Ki3TUylqX9T-Yn9z3dZz4ubCDI7v64uIqKfTRz8LPsa0HIyT_XpF7VcufYsYFlaTfHV9kI92YaGRR2HUnfmzea_q0boJCUPJgyuza-QKp1GQgdmN20z9pb1bQNfBWHQNbW1oRJYZyTPYxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش اسرائیل حملات را متوقف کرد
ولی اعلام کرد از مناطق تحت کنترلش در جنوب  لبنان بیرون نخواهد رفت.</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5658" target="_blank">📅 18:43 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5657">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RPv6NTgA4WU4kwk_J2Bt2OELoBVwXeD0e-a6wm6jB1U6LkGkkTPlTES9WZ3YxkyU6dj0ncrDunvDyAnnKlq_cC6xSiZrinsw3bMsQ-kDLev6j4e-wTpiXhFmgpUNi0bux8do51-O3zqqNqo7pSXb834xOq-MhUrmgTfpkef-Qnl0vPzWdbSUvffIa9cEWRfRS5thD9f4Rg11CZkxgJUi7lOJWOMvup9cpaXVfSjrN8O02bhou-ynGa_4QdZl-5iWcrdUEVXWJZyoS3G74Tj98eDtRPGtA2Uiwnuc9chdsIYDhfjsfJpyqi5WNTqjBVsW-HYtwwoVzYF-zyMYuGHcPQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/11b10561df.mp4?token=vmS0a_8HPzy-J8vUTIj5s9e2JqeB290S15bTyFbOQnncv5aBIUnPjrP9Wcsth7a_-skXQKQ6oYpBiVpcT0MO1vNr-8Cay4LYxKMReAZudIi3t2wNwxtDmicWCTtNFghK1qRPI-ySecMhPJte6f-8dcDBdyxwz2S3QO0NLXbdWfbDVpN88WPUTt8U3DcvAWahapzCKHmvLTE61cY56Rd2ZtMfuW2PhkDwrUIrywIuyYPhY0UvsVFqtxVvcLcMiO9zbsC6hFvargMLtrWRctkHqWBz1ei9h8vAFbOTPxggJ1izzLSe_QkQC3XMMR0g_BA4UIMJQOb8S7RMSR_vBEp_eg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/11b10561df.mp4?token=vmS0a_8HPzy-J8vUTIj5s9e2JqeB290S15bTyFbOQnncv5aBIUnPjrP9Wcsth7a_-skXQKQ6oYpBiVpcT0MO1vNr-8Cay4LYxKMReAZudIi3t2wNwxtDmicWCTtNFghK1qRPI-ySecMhPJte6f-8dcDBdyxwz2S3QO0NLXbdWfbDVpN88WPUTt8U3DcvAWahapzCKHmvLTE61cY56Rd2ZtMfuW2PhkDwrUIrywIuyYPhY0UvsVFqtxVvcLcMiO9zbsC6hFvargMLtrWRctkHqWBz1ei9h8vAFbOTPxggJ1izzLSe_QkQC3XMMR0g_BA4UIMJQOb8S7RMSR_vBEp_eg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اوه ا‌وه خیلی دارند بدجور میزنن!</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5654" target="_blank">📅 16:13 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5653">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5130bbfc36.mp4?token=jOJkCjgeykeUytaHerjNIWe46ijwe-Re2QwJcGnUpesLOku_KUwhVkxuQSevByb0uJkykOPNnRGC4seZrpIjlV5QYF6TIpIhOZsnCNYli3il2ql0ODZ6wHu3m7_3q_50D099byu8hLOWQ1BoA_LX7FYYG3eoj7mv_GIcXNfxT4ofJgkHNQqYrK5e-CSDQHameHNETImYpRjBAGt6em3Juz7DqfziBc7FoVgjzd_Py8nE-hfOrn5piwvGQYBqhSHN4mLkxQuHFi-oeClScthVlZcmaYSxRNLizc8E14gM1-SIv1QSQYChRSu_kZKRl4h2QalPGRIcswab1_JJzGs2WQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5130bbfc36.mp4?token=jOJkCjgeykeUytaHerjNIWe46ijwe-Re2QwJcGnUpesLOku_KUwhVkxuQSevByb0uJkykOPNnRGC4seZrpIjlV5QYF6TIpIhOZsnCNYli3il2ql0ODZ6wHu3m7_3q_50D099byu8hLOWQ1BoA_LX7FYYG3eoj7mv_GIcXNfxT4ofJgkHNQqYrK5e-CSDQHameHNETImYpRjBAGt6em3Juz7DqfziBc7FoVgjzd_Py8nE-hfOrn5piwvGQYBqhSHN4mLkxQuHFi-oeClScthVlZcmaYSxRNLizc8E14gM1-SIv1QSQYChRSu_kZKRl4h2QalPGRIcswab1_JJzGs2WQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/a19f9c1ecb.mp4?token=H9HUoOgClfIgOfa3WxsrKCA67ZjTG2_ilJgRoZf_vm3hfIb_KQctHbUxk9U6IG2LtJ7hcDAOalMxiFqFD472zPO--l_t-rluWS9jRn3-FXgL1Lb8V9FZIi5l3J6QNc6_CCBwsU-L1NxO6BwnBn2zlslRfljMagj0Y5Pj79dlNx4v5jkMZGlAwPSsZCDh7xP_KBj9U7kbfvbZ5w_PQMYEYeovm5QbW2yiqsLz659C6bt9Ux-FpXIRbuxnjTe35EWiqnY-0vRXdfsL5i7BeEoe5Ve5SguxyfzmWMJPyJvkyYwwwl8yBJYkqrZpF8YvxJ16ljqnVd0wrG7txnFXiCP1EA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a19f9c1ecb.mp4?token=H9HUoOgClfIgOfa3WxsrKCA67ZjTG2_ilJgRoZf_vm3hfIb_KQctHbUxk9U6IG2LtJ7hcDAOalMxiFqFD472zPO--l_t-rluWS9jRn3-FXgL1Lb8V9FZIi5l3J6QNc6_CCBwsU-L1NxO6BwnBn2zlslRfljMagj0Y5Pj79dlNx4v5jkMZGlAwPSsZCDh7xP_KBj9U7kbfvbZ5w_PQMYEYeovm5QbW2yiqsLz659C6bt9Ux-FpXIRbuxnjTe35EWiqnY-0vRXdfsL5i7BeEoe5Ve5SguxyfzmWMJPyJvkyYwwwl8yBJYkqrZpF8YvxJ16ljqnVd0wrG7txnFXiCP1EA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اورانگوتان رو!
هر مسجد یک شعبه حزب جمهوری اسلامی
قاتلان فرزندان ایران بین همین‌ها هستن</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5652" target="_blank">📅 15:42 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5651">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UACOf-A8iMpUe_Ke-Eij2XH3BW4br1-ot7jVE1zOhzpUpXFDbAEpfIL-h94gTLlJ4UaD19MriVkPPtu1PwMFF5nsT4DqBCsliymRn97pmJ-Ha_FwgEh4DLZds0n7lTrei2LHWkt11jeqv-M4iymqaMHCWRl4AkJFpJU-6pRN_RWbNAtYu2vRwMI8SYP-7P166HVThrz3M-jvbs97PmjSZ0CBfBagCVoSgIWOjvANIX3w2bIp8FEtmWWGADHIOwQ86XfL4c1-1o2D9olio54sFjGr9HCi5ZAyLX7XesGI25fim1uayLKoDhOu_VFh3n9m7sJDXjZzjHFdI4fvje2zqg.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/ecdbcd4679.mp4?token=sGckozNbwZ5zsnLYOs0JsUBc7YC3GFVvMOf-cdSkMkCS3iYbSVnlfAbxMVupV8ry3JHJ0f7P79FlREKdKS8ZE7tJiNn7Nttpu83jARtSO0uGHmB7s09SLziOgfGhhjaDlZnmoPXUojRd2npEOMM23cpwPtUm7QiIgxawrmyL70-bi7_BChP2rAIItL-WYpDm7ER0JsXL8qqG5zna8vxVzeZFVfTfzLRrrCWtkMFfcjBy32BW5S6ETRafIR221VxFV_hzoMmQTjukQBP3FyHr-0ac_xJqh4HqomGtoyobhwAMcM3rSv2_71Gq1FfdA-hMcNXBjqwdX25GMkIyG_y4Cg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ecdbcd4679.mp4?token=sGckozNbwZ5zsnLYOs0JsUBc7YC3GFVvMOf-cdSkMkCS3iYbSVnlfAbxMVupV8ry3JHJ0f7P79FlREKdKS8ZE7tJiNn7Nttpu83jARtSO0uGHmB7s09SLziOgfGhhjaDlZnmoPXUojRd2npEOMM23cpwPtUm7QiIgxawrmyL70-bi7_BChP2rAIItL-WYpDm7ER0JsXL8qqG5zna8vxVzeZFVfTfzLRrrCWtkMFfcjBy32BW5S6ETRafIR221VxFV_hzoMmQTjukQBP3FyHr-0ac_xJqh4HqomGtoyobhwAMcM3rSv2_71Gq1FfdA-hMcNXBjqwdX25GMkIyG_y4Cg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نمیخواید بخشی از مراسم تشیع جنازه خامنه‌ای رو در لبنان برگزار کنید؟</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/5650" target="_blank">📅 14:29 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5649">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c5aba790b1.mp4?token=v0Ry6QUZQw4CMXTWSwq-897HxDTYSvztVqTuiSvgEVM9zqK3xoOys4kxwg8qgI5W6d-WgjX53amlCPK-vD8Yb7KlCIiXM8nqWCN1n7Ex25FImbc9oK7SXIrwbQ06xQ1tmJGaqTF7wu4Paqa56Pl2BRCGfLK2QBeWGr810A-IzHeLuw4EW3Ycs8I91PCtNTDffl5Rj4-_GgsrBnYOIfBx6G0lkGCo_ZFi-ZKKWPwbXxkbOjJrA-xFp76VlYYpBsptEBMniJzOZVHD7I2841BgBj0zftNVz1cKhqCY25nVvN7d1gqN2R4moup4sxk9AsDhUHHJuIwCzj3t6ScF5A9SiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c5aba790b1.mp4?token=v0Ry6QUZQw4CMXTWSwq-897HxDTYSvztVqTuiSvgEVM9zqK3xoOys4kxwg8qgI5W6d-WgjX53amlCPK-vD8Yb7KlCIiXM8nqWCN1n7Ex25FImbc9oK7SXIrwbQ06xQ1tmJGaqTF7wu4Paqa56Pl2BRCGfLK2QBeWGr810A-IzHeLuw4EW3Ycs8I91PCtNTDffl5Rj4-_GgsrBnYOIfBx6G0lkGCo_ZFi-ZKKWPwbXxkbOjJrA-xFp76VlYYpBsptEBMniJzOZVHD7I2841BgBj0zftNVz1cKhqCY25nVvN7d1gqN2R4moup4sxk9AsDhUHHJuIwCzj3t6ScF5A9SiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نمیخواید بخشی از مراسم تشیع جنازه خامنه‌ای رو در لبنان برگزار کنید؟</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/5649" target="_blank">📅 14:29 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5648">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9eec8cc86d.mp4?token=a-xj5sFSY4SGdTgudBQyEhWv3ObV1mkYGhOjWbIXSXZNG_pky3LMGT_CNNZQDbKCgUMCUInG-qsq-rK5IA8ZlrrNj0PeMxq6ukGatsXi99VCtsIyGrQ9s7o_W8X4OylbEDQ8XJe4TYfPxoa5ewSC65c6i3nD1P1jCQAqTxnwzbRRo-ZWcaJEzMSiWM8zNxtjvNC5HD36OsZM43ZFDmgmJIilLd-9oGR8T8IrzJDlUTTUtEUGYv3eu8c2a3V47PPBdOgzBSoPcQP0soTulkjmeAdHaPUEimk1aJQV8eKI28KkHboJbRMlLha96hqmHFdk-oWzMkWuPXAuXBIGe0SvZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9eec8cc86d.mp4?token=a-xj5sFSY4SGdTgudBQyEhWv3ObV1mkYGhOjWbIXSXZNG_pky3LMGT_CNNZQDbKCgUMCUInG-qsq-rK5IA8ZlrrNj0PeMxq6ukGatsXi99VCtsIyGrQ9s7o_W8X4OylbEDQ8XJe4TYfPxoa5ewSC65c6i3nD1P1jCQAqTxnwzbRRo-ZWcaJEzMSiWM8zNxtjvNC5HD36OsZM43ZFDmgmJIilLd-9oGR8T8IrzJDlUTTUtEUGYv3eu8c2a3V47PPBdOgzBSoPcQP0soTulkjmeAdHaPUEimk1aJQV8eKI28KkHboJbRMlLha96hqmHFdk-oWzMkWuPXAuXBIGe0SvZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جنوب لبنان - حومه نبطیه
از مراکز اصلی شیعه‌نشین در جنوب لبنان
و از مقرهای گروه تروریستی حزب‌الله</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/5648" target="_blank">📅 10:58 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5646">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EiCS_KQt9aRI61ZVLpDT5g1MJL2qlYziRgN2tfM5LOBhXA5g-kgtlDyu4BYf-VgWZA-ZqLY74AecBSA0E5bBCuWvH_1d1KXzMuACOXUrp_8O59hwvx3q27BUfVYiYP83rfKRhAVpxwhjbm9HRARZ0XrxqVLdFUUYWFJHS9eG8OF3rgrx3WLqesz9JXV_dRpGqftJkJr6bFVj3EIuu0PcDLr6ru_XmCM7wXJHn_uX02q3tW2BoI8dAOaI-io4bUnUNZMsnoY4n5jYMBNhDNprgLioywgqpf1ORn4KMeMsbyAaRjlj-rTjVc6BsDVc6pTICTrd8HSO1Hnxh_X109K6jA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/21669172c8.mp4?token=HJrA6YPfoRgqM0eFiON5xXNF9Epvv9n-oNMsPrIAYYjkbzvCtd3SqoWAr-T4xTMz8nUiBymXHOoW1DQQqYFkvwYLcYrw_2jG3gbKBv8QeX-aL84N9JlgihUMRYawQr6k7Z-FxrjwtFbuaqI7phEG-Iq2nDwaThTYdiUF-3KOnuQ0qxSp0tJTZ_kmYAZmx7x2dsLP3uKIbLjpPiswBvdAwJdazjeNuoHwlRYrxllhsQdT0uylF5XoYOVLTE_s-zw5-Ey7R0qiqww9WO4M-kZUFYZjjrsAduP9enAfntkfLoHBHpt1o9cl7e5kBc-1P4AYtBxb43EE4BlBTRTYlUz6uA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/21669172c8.mp4?token=HJrA6YPfoRgqM0eFiON5xXNF9Epvv9n-oNMsPrIAYYjkbzvCtd3SqoWAr-T4xTMz8nUiBymXHOoW1DQQqYFkvwYLcYrw_2jG3gbKBv8QeX-aL84N9JlgihUMRYawQr6k7Z-FxrjwtFbuaqI7phEG-Iq2nDwaThTYdiUF-3KOnuQ0qxSp0tJTZ_kmYAZmx7x2dsLP3uKIbLjpPiswBvdAwJdazjeNuoHwlRYrxllhsQdT0uylF5XoYOVLTE_s-zw5-Ey7R0qiqww9WO4M-kZUFYZjjrsAduP9enAfntkfLoHBHpt1o9cl7e5kBc-1P4AYtBxb43EE4BlBTRTYlUz6uA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RQDMaeoqkGezLCUdC3SKyK_4a7_eCVcblGB0gMNOZixeykNAMEy980Vn0Bp2d5IuNPawbqDGs392lGuzNz8xT2YfY7rcniagV3vtevCcY3JtuEooJqVSE5Tf8POqAJPCYGdkBIwzedTC9lqe8nf3lnc_nbtI8ytNLad47ERXr2QdrYlzWdhNVMueFPSTBsbi7hR3Oc9-2-1l78sNAeTjmq2ZrS2QwL9B78HfgI5ZxWsH9ojd3Yv32idzaRjGu6I7bWHk1M6FUJfM6WYqcIpSd9mFstjeImCvqsRiB---M9TzvFvuJ5L9wmx-lnbu43lLjB-CWNGvpP6-D3x9UF5OkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e75af7dcb.mp4?token=aJaa1eWKte0W4P_aYp4QHKjbe8TLqjNLnp8hxUvI2RNAKPFy8d7v-28lhCSPQWai_H_dTo7HrYBOw318L_teFzeeR6fcqofPAfXvZBgnZEXLr8p_5t97iIyLT4757VzBWb35paJhzEjIBMLGBZZ6R4Ih1By9szkcYjED8TmhuGx0mDzUCs-kBgo0wOx5ORkVXxNWVizUOPNj8rca-vYULfL4fZRqBFsdU75zSXuuOVkekCDadPH7O_014t3INfPJG5USaxBFpFdWXendGq3Xa5oKxfktUSYEdH0eoTpHGNYosuuOmsSK0Eq5CckxovANf8r_rCSMD7F0hR-4ZPx1xw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e75af7dcb.mp4?token=aJaa1eWKte0W4P_aYp4QHKjbe8TLqjNLnp8hxUvI2RNAKPFy8d7v-28lhCSPQWai_H_dTo7HrYBOw318L_teFzeeR6fcqofPAfXvZBgnZEXLr8p_5t97iIyLT4757VzBWb35paJhzEjIBMLGBZZ6R4Ih1By9szkcYjED8TmhuGx0mDzUCs-kBgo0wOx5ORkVXxNWVizUOPNj8rca-vYULfL4fZRqBFsdU75zSXuuOVkekCDadPH7O_014t3INfPJG5USaxBFpFdWXendGq3Xa5oKxfktUSYEdH0eoTpHGNYosuuOmsSK0Eq5CckxovANf8r_rCSMD7F0hR-4ZPx1xw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صبح در جنوب لبنان
و بند اول پیش شرط جمهوری اسلامی</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/5644" target="_blank">📅 09:52 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5643">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M2rHxtyAWnp9eGG83V5JJ70PlfZn47AQ4gFGnlMpGrW9ISzFxyAw47rdNT9GUhtwXF8nz2fNtiZLOI7YNRpa3F74mKTVIm4OECzlQHKiSiq4PV6agsrILWe-WnnjpkkeKkK5BMn0sIyq19BYl36I1lAgsXweSfwb-p1ALhGA8zw7lnaOnso5QekWaiTo7s-JtHqD5ylMqYnKEpCbSQ14xxCTkfEL8ZKKiYNme5-de7POepsqFB51s2wjMyEeCUzPqO16AEvujxIfkc5j7LzzFWFjEOd_pVBtyp2g2xCW6EP31FElRdE5ZasbvogZs5leYP7hw-2IKcb5lsjJZmIBNA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/d81ee77286.mp4?token=Mirhg-R4BQAXwKCHxs1I7Pr0iOucXrPJr675aJNw1QE4yCWWDpnvkPe65EaLg4Bp6fcVV9VsHSEIo3-0zdOLtJmy3TYjFdB0LdTC4xgBcSFLMr_uu7eFw46zX51rQJJ5ClNxgFv_53SFfx4SlkFNm28Q6DMvS6D7935Fri5qnILBj9GH9RmFy-I484o0WtPRVgtNmacGOzBfrAUobCsG63OIeAq-2PhvUZ7zV0wI8xPzhby_Z0VJCACC-YDjuolqE34WkinNzYKZldR3qL9YDQ_8u3pxErD7t8NqQlmWb-YQ0xWxcRnDLHFrK8wGxJMTIDr39nd-eLczluPh91AC8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d81ee77286.mp4?token=Mirhg-R4BQAXwKCHxs1I7Pr0iOucXrPJr675aJNw1QE4yCWWDpnvkPe65EaLg4Bp6fcVV9VsHSEIo3-0zdOLtJmy3TYjFdB0LdTC4xgBcSFLMr_uu7eFw46zX51rQJJ5ClNxgFv_53SFfx4SlkFNm28Q6DMvS6D7935Fri5qnILBj9GH9RmFy-I484o0WtPRVgtNmacGOzBfrAUobCsG63OIeAq-2PhvUZ7zV0wI8xPzhby_Z0VJCACC-YDjuolqE34WkinNzYKZldR3qL9YDQ_8u3pxErD7t8NqQlmWb-YQ0xWxcRnDLHFrK8wGxJMTIDr39nd-eLczluPh91AC8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملات اسرائیل به جنوب لبنان  بدون توقف ادامه دارد.</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5642" target="_blank">📅 00:21 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5640">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qqrRzsBadxjYfimxG0WeOW0730f8GHE6rDtqCZdZYU8jIPTYCaJlGr5iHRP_CNyLt5OXUNtjg1-Jp2b3zhmRCSy7Y7F_w-oCH0kdr1U8V5Xl-lWrLolWF2qolbxN5IhdaaPStzdi2OirFMOuQ8onSDlgRLU0HUIXdmo9rxRK16YzrePEt8MSWpH1aaiqVvwrqbqA6UUGyCm9EMvJacz3D-cTHB-zrfHN4kP2MyDnKBGfout_fD4d28nRqfjCqv_VW8zvz-3BsxnMP4WffyL8Lk8dDrETTVsRSoH1wZv-OkNA8BHVn2gWeffY4SvJLh_ww7LtorP84oks8c9lh3T-ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/s71_LnGbl92NY6_TkCO7qD7F4BA5SqvwU8-jisMAmIiQgcEb1h_1aKRmWwOe9Hlx5Z5SigBUDuvlLFTBkDPmtFMisPG_fb7kt7rFHM_e54oimSI7PIxPutm8GFQ0f9YzNh1sKVwj-_0Qha3gQbAKPu8ZpAIcBbStPuEN3qhcojZblZPs1hcl1SrCO-KVkUIe-lbmSxcHn-tBTZax64DSQfT46A-dc5q6Z-pCLAe37aEYj_ecNKD-IFwDxU5u4olk-v3tLXC55_GoUDumyoasi7hyWcScp0GrG_tHq1NBxhDJMBCK3Yc5mlKCzdfA85aqTYowUvPa8glnhoAeuR_R0g.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/f791b65d03.mp4?token=hikyGXuuhYmJqbyyi7fcRalwm5xqwFJKrKAEx6pW4dyUwCtP6Vl8QchhYHXKSxwiBuL9rt-u06HCR2qTXa6As8sJz8yuIAmAd50luNyz0p8q0y3A82jAyFPjsb1nVz6lzL-rSsYDud4V8K9xS50MyygthHBC4xCEig2ZSDob_k7fF5f8tPVAZR7U1qO7304TB4tMcn293a9gTTLJnnCS4gW0HbBmfmdDs2ZBtk-JQ2Ulone5niSLIXqtHLMlyfGx9B6KMcQwMNKgWmw45dhVB87UzKo53S_aaLhYxiP7VhLGzdN9Hsjm6U92oV9Ylug7oghLBZKoC8et9s1USxc0NA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f791b65d03.mp4?token=hikyGXuuhYmJqbyyi7fcRalwm5xqwFJKrKAEx6pW4dyUwCtP6Vl8QchhYHXKSxwiBuL9rt-u06HCR2qTXa6As8sJz8yuIAmAd50luNyz0p8q0y3A82jAyFPjsb1nVz6lzL-rSsYDud4V8K9xS50MyygthHBC4xCEig2ZSDob_k7fF5f8tPVAZR7U1qO7304TB4tMcn293a9gTTLJnnCS4gW0HbBmfmdDs2ZBtk-JQ2Ulone5niSLIXqtHLMlyfGx9B6KMcQwMNKgWmw45dhVB87UzKo53S_aaLhYxiP7VhLGzdN9Hsjm6U92oV9Ylug7oghLBZKoC8et9s1USxc0NA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c9oSSnkSm2QjsAjr8uvSxDNTiFImR5f-_By_YvL-msRjKiIKKLTbnYB55X1ZJTjkm-Qu62HN3D-57HjO-uNYm8ziNBlOv365q_SUk7DbvuzQDIxtpeLhmHWzn5RM2_uts0tmbdC8yf2LoWMdtkA08cW9ji2c0hZITExY3KRoKd9zS9F3fUGxIu6c4pzzduvS8w0UR9SXp0NxYbRkgBo-At83QbmLAPKT3ze-jzNzpYQ_ts0gfx23YwmfRkXCN_iDroHDMJWQc8EaMz3A2ujT5HO7OiebdM_zTh3cFUnrQE1cab6UjA05PtGgY14J2MAxBV_ubGat6NyWHxRNHBcfMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنان دقایقی پیش رهبر گروه تروریستی حزب‌اله نشون میده که این گروه عامدانه شب گذشته آتش‌بس را به شکست کشانده تا اسرائیل را وادار به واکنش کند.
نعیم قاسم :«تا زمانی که قادر به ایستادگی و مقاومت هستیم، چرا باید تسلیم شویم؟
ما تصمیمی حسینی و کربلایی گرفته‌ایم که هیچ سقف و محدودیتی برای آن وجود ندارد و این تصمیم کربلایی همچنان پابرجاست.»</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5638" target="_blank">📅 20:02 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5637">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gudL8jRYMT2oMQPuIU7xv6y6Uul26KBe30VEDiJOGOINQzTw7Ce3gmJeKajrDXff_bthPEo2RWqTrXtzakU2B3QI5ShA8mwCW0RV7AJFGH7qErgs1wuz8vRFGINZRjCNH8zaYEJXeOOeX2co7UiAZJL1Ne4xmj4WXdu1h2DS1RoI7kzucv7BH8c3xMvwv9bZ_QOpv3n3SQ4VbAojZXZq9DSee1dJ3GePBfw1b-oD7sDiAvhtKm5PAuoq4YPTtFrCBxVwyvmTSdoUhtEoIC1WtFpXP-RRcvM3EzpMuVpTGkfRpoJURV5yctbkOOmXPaz9Fwm4FE0IrRz3OD_K5cs2Ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/farahmandalipur/status/2067993854494622141?s=46</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/5637" target="_blank">📅 19:02 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5636">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mAgWwf5s5uck5ollRv3yNh50cTxBnBNp2kp5wLGLuH9G_Cxgpm98jQszRyxdkFgt4WRDlhUvkE_n5Ulkg6L2hREz6M3OMcMQn09Kyx6SKTZpBg4yoI49K0rwgGhctsXY7gwiBxuadEHev6qo8_saUP3_CDR0bhoFBp2Bt44JIlmmYhY9OksBhzdb3Z4VO1mURmsVo_u8a6b0HOKSO4r9naUbWISZ4qknIEoYBxDSv95o1XR7KoUyUFo_7l0af9ZtGeabH1Ej7AIaBhe19JZ5swnDjIqAmUoAdtQFdmlCy9sEIRDenHdMlV117YRE4nopNsOE49iNJM2vRVIpXISE_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت بهداشت لبنان : از نیمه شب تاکنون ۴۷ تن در حملات اسرائیل کشته شده‌اند.
پس از انتشار خبر کشته شدن ۴ سرباز اسرائیلی در شب گذشته، اسرائیل دست به حملات گسترده به لبنان زد.</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/5636" target="_blank">📅 18:56 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5635">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iey4hG_Dv40g5NkQEfpu2QfxWVZLjF-1j6CsDOT4qXqh7jiXOa1B-LIxTgWtu8EYsAP3EeostMFhWq6AL6GAm7uBN7lM5yWcXRURjrUaQwagP6XmPNfO3j333MYXW4R8fKfO6eIFQjwS7HgdIPOr1IHrehmoJKzQ3ywoxLN_T82E85Kr9DGWBkG8Etm7fuAa4DS2vMrX_C3zNyfTcnuqz8L8xBkHOq7y3V0yYqVhGOpwMlBlGoWC6qDwcBposIZhSmneHCq-NUsP0KtHnXaKSS_RNWbh_xKKbTPsMKTTl3NzPL0eqiIxptPtaOXfQZvvFMzJEmiQr0Fkp9vcMv-GJA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tvekuql_zG6QQrZFSuj65Ym2bnWtpUf0hfnfnwJb_JJBFUGvXHQUqe30YnD8qxCy8UFpi-FFMY4ckjKzkL4Ji3fqTP8KlauttvBpQiHl0QW_OSxynTCb9XLIS5HWOcRbEmLGOPl-Huo2c6OZob8bYnRQxsMO3raP7niohiE4tVPbMdCA6H1UuPYJD-EZCNlV7Aptq93fGwMGiHMN2QjLNiAod6l1-OoCQ0XzqLluTLsGxalgrI1eohx7fLj_LVyxwoYDHdhNKiGfkD7R00oVvjtXEJNgV42OO19wo0zuJctGhDWcx2Lk2xa9DsZ0lwCgqANTaRZG1ctrkxybjzd72Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نتانیاهو : به بیش از ۱۵۰ هدف در لبنان حمله کردیم</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/5633" target="_blank">📅 18:30 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5632">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/392eac3002.mp4?token=JqV9pGNFjva0SSNY0ttIfRfxkjRSirYv9Ur0qpJE-lYTOaT574jHa480gvPeket_LbO4h0U6Iok9v7f7KMZ2Ew3RYwXavZdSdzCSfwuZBxUmbxog-5xD3SHWXaSDaEm3pZRM3B4_ot5j7NPXSkEiks_wHO4u96luMp3MQGt_I-PFIOVW_0THXWfXgmdS6Pvzn9x7RtI6n4AHeRxutnpw41P1l6-CS6zybVdDvzzpn50jxrDcUdTWS77s4NPO6wLbCWw8_KIK_2vZvvL8sZuBmgntmdAK6i9tDp8rgKmSzlEYkdK7eMRvV_DQSk0h3KM4HG0CzCRKCzw1W0Ut0aMBiw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/392eac3002.mp4?token=JqV9pGNFjva0SSNY0ttIfRfxkjRSirYv9Ur0qpJE-lYTOaT574jHa480gvPeket_LbO4h0U6Iok9v7f7KMZ2Ew3RYwXavZdSdzCSfwuZBxUmbxog-5xD3SHWXaSDaEm3pZRM3B4_ot5j7NPXSkEiks_wHO4u96luMp3MQGt_I-PFIOVW_0THXWfXgmdS6Pvzn9x7RtI6n4AHeRxutnpw41P1l6-CS6zybVdDvzzpn50jxrDcUdTWS77s4NPO6wLbCWw8_KIK_2vZvvL8sZuBmgntmdAK6i9tDp8rgKmSzlEYkdK7eMRvV_DQSk0h3KM4HG0CzCRKCzw1W0Ut0aMBiw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/cc70f2404f.mp4?token=mPJcr5JYhomI3VhPjUAD8BJ-FUO0-k4OOS-8IoLHAnPlZiHUGv4N9WBEcGJdxhCIGrT-m71SkFNzk5LRkxanG22X_BP58v78IOCZAmdxxZDToTINTLKkF4K4NTi79oldtR2J-WHAR8aIX3ZaHqDKHTo9HkW-z8e6yudoYxiZPXTxrih5DvhfbWIz-wWPfy3-t1YDS9N72G-cPnVGbLS17k_UsmrNw7Dn054CHR-xa66wxdTLJjkL3pcosfLAvLxGgq9fuz0gh_3m4L6JEXl71T7YnSVGCoEvdbAhxeNmIZbWtGVijt5wA5OiiDPZp3sL20vN3te_hmu8RRfzwWAhaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc70f2404f.mp4?token=mPJcr5JYhomI3VhPjUAD8BJ-FUO0-k4OOS-8IoLHAnPlZiHUGv4N9WBEcGJdxhCIGrT-m71SkFNzk5LRkxanG22X_BP58v78IOCZAmdxxZDToTINTLKkF4K4NTi79oldtR2J-WHAR8aIX3ZaHqDKHTo9HkW-z8e6yudoYxiZPXTxrih5DvhfbWIz-wWPfy3-t1YDS9N72G-cPnVGbLS17k_UsmrNw7Dn054CHR-xa66wxdTLJjkL3pcosfLAvLxGgq9fuz0gh_3m4L6JEXl71T7YnSVGCoEvdbAhxeNmIZbWtGVijt5wA5OiiDPZp3sL20vN3te_hmu8RRfzwWAhaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پخش حملات اسرائیل به جنوب لبنان
به طور زنده از شبکه خبر</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/5631" target="_blank">📅 18:20 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5630">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aab675b39e.mp4?token=DcQHS601O08GMUp7UZpY1yqfFmq2mpcYhwYs2u-AiFJk3UoAuvTeXim5obU7UbH2F1ED-rOi970BgiZsjjiwt3EHYHckOhnxwftF9vahmQlH4nf42KVarHWo4Uxc2SU74uxEU2hMb9Lnx9oXy6m9TTyJmfJa2G8jOiD32XTdbctGb55zH5GnMsImMsxiv-pE2wxDpO1tZsRMZWDzO-ZE7NPmyfAXLRUpaHrvGCTqnrQ4u13sIKtr86QWbmoCdnD8e59BjECS-v0mD7lT1wFSFYF2snItnx2fnoma9VpqGz-AWpogbNW9tIcq6CxckNInDYURkbvj3apzReHPI1iIeA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aab675b39e.mp4?token=DcQHS601O08GMUp7UZpY1yqfFmq2mpcYhwYs2u-AiFJk3UoAuvTeXim5obU7UbH2F1ED-rOi970BgiZsjjiwt3EHYHckOhnxwftF9vahmQlH4nf42KVarHWo4Uxc2SU74uxEU2hMb9Lnx9oXy6m9TTyJmfJa2G8jOiD32XTdbctGb55zH5GnMsImMsxiv-pE2wxDpO1tZsRMZWDzO-ZE7NPmyfAXLRUpaHrvGCTqnrQ4u13sIKtr86QWbmoCdnD8e59BjECS-v0mD7lT1wFSFYF2snItnx2fnoma9VpqGz-AWpogbNW9tIcq6CxckNInDYURkbvj3apzReHPI1iIeA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/73e57c3fdf.mp4?token=rVLAkcoeFO9nFBnIBK5SW8RKbyI91KmkAlhIvMyMENR66SDR0kMJtlVmyPS_kCMLrzs4WAEvAwytBpbK_O7ruD5QOVMm1M71pZzIw51cbLvn7d4U1_fU9oRB5lmOwFfYSKy19aC36BEYp6WzE-33nDQfPNNNLCWf41YdIZ2An6ZrXhjP3u3IEM8xJDJWxM1TAAknYvkuwcbnm33e12nh6kZl3H3e1_SJz8jqf48jkDhOZmp6V4WONx0uKJLx_BT9k8zw2r-RriY9n10TCdK83aUfA25CX3-LT2DYLoP8TR1mu_CRSHicjDI942L4EUIPp5qk9tLVLuUjKrumEr4s9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/73e57c3fdf.mp4?token=rVLAkcoeFO9nFBnIBK5SW8RKbyI91KmkAlhIvMyMENR66SDR0kMJtlVmyPS_kCMLrzs4WAEvAwytBpbK_O7ruD5QOVMm1M71pZzIw51cbLvn7d4U1_fU9oRB5lmOwFfYSKy19aC36BEYp6WzE-33nDQfPNNNLCWf41YdIZ2An6ZrXhjP3u3IEM8xJDJWxM1TAAknYvkuwcbnm33e12nh6kZl3H3e1_SJz8jqf48jkDhOZmp6V4WONx0uKJLx_BT9k8zw2r-RriY9n10TCdK83aUfA25CX3-LT2DYLoP8TR1mu_CRSHicjDI942L4EUIPp5qk9tLVLuUjKrumEr4s9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به رغم ادعای رسانه‌های آمریکایی، در اعمال آتش‌بس، رسانه‌های اسرائیلی از تداوم حملات و عدم توقف بمباران‌ها خبر می‌دهند.</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/5629" target="_blank">📅 17:42 · 29 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
