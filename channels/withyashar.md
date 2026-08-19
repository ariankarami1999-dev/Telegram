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
<img src="https://cdn4.telesco.pe/file/JBI1vpWk4lI9OK7qJEO5fep_K-LMC1LVMePk59_GCNwbZJbThTAu6pSnU5Xnu-6ohHcWaJI25VjngSoqnw_3hYmmVPt5D9_ZjyGYt_CqavX1ksp3PZtpyAeKq2ri8n1TdWoz9Tz_VOyeOOgGcjGRHudiVl0vKhm4di7CTJYU4UXCXZPJrWciYLLaU4Qzjcd5iRYud8xjMRNrnaQB7zBZ25J_ZsW2S3ofr8n8rdlWeBXt61zExLsrqgbpG0ZVosynhMTjxSsUD7jTfmq_4tr390aR-8bNlpSZimdL7TqitmefcfaUxI5IpjX8UZla0Q7unjNd0rPm7vhdAo1yYXOHaw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 443K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیل📸instagram.com/yashar🐦x.com/yasharrapfa📺youtube.com/yasharrapfa⛑️paypal.com/paypalme/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-29 01:17:17</div>
<hr>

<div class="tg-post" id="msg-21229">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b17a03cc01.mp4?token=V97PMqM_N3hosT91z7Tvxg30V8S3pCvnSF1JF38sl2Xw5K-koIqEnraxjJjAjCF_6l47VLsE2GrNiyvT7hSudqhO1LK-sw2Mf6nzPSVcTsGugDub2IsoEDKYxSsu7gppOovcEaqsRFdnft52xl6CCAx7wCv1EtUyI-9IxhR0SJkWtnDzRnBfa9vfv3PoyS4BWqGzk-GiV0z78knlQYH5CQqBSWdYv8ePFsbXfE_TsOAeinVld96llnaZguaKvsYK3rqFe3Ju_H_gYjEqutaktbsFc0gpI8s9xSpIdVv6qfYBKlUfI14sKYyO0PZCD3BPZKDHgelGKMTi4qXUUUt1Cy6oPYmYpG6HWQUR20cnD0NmptJFoUdZSN8fS2c2ouveI6UhQTTOBnMCKXtzptpmign8OfU7k8m2Iwe4gBGn7ULApkC4BVNzhrrsb2OD1a_wZT7IxeGItENPHwfyQzRKj3Nv3Y__IFkT-VJ8bDQOo00x_gK-s1ddiwRnTs8xnw0F_rnc9MaNMV1Uc1hN2zzD1NKjCZ9I1ZIs_5KJ-ZO7E7vA7eapIigLyv4PccO1SF76W59eY-VzMhlN0WGw6d-qS-rm6jc2ZxwY6lrmP22Z_E1hlOypUrt4dMa9jbsN4FBTle1UEl18lnBej2pU2N1J8HI-QiJLd7XWb3G9EoCUP-E" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b17a03cc01.mp4?token=V97PMqM_N3hosT91z7Tvxg30V8S3pCvnSF1JF38sl2Xw5K-koIqEnraxjJjAjCF_6l47VLsE2GrNiyvT7hSudqhO1LK-sw2Mf6nzPSVcTsGugDub2IsoEDKYxSsu7gppOovcEaqsRFdnft52xl6CCAx7wCv1EtUyI-9IxhR0SJkWtnDzRnBfa9vfv3PoyS4BWqGzk-GiV0z78knlQYH5CQqBSWdYv8ePFsbXfE_TsOAeinVld96llnaZguaKvsYK3rqFe3Ju_H_gYjEqutaktbsFc0gpI8s9xSpIdVv6qfYBKlUfI14sKYyO0PZCD3BPZKDHgelGKMTi4qXUUUt1Cy6oPYmYpG6HWQUR20cnD0NmptJFoUdZSN8fS2c2ouveI6UhQTTOBnMCKXtzptpmign8OfU7k8m2Iwe4gBGn7ULApkC4BVNzhrrsb2OD1a_wZT7IxeGItENPHwfyQzRKj3Nv3Y__IFkT-VJ8bDQOo00x_gK-s1ddiwRnTs8xnw0F_rnc9MaNMV1Uc1hN2zzD1NKjCZ9I1ZIs_5KJ-ZO7E7vA7eapIigLyv4PccO1SF76W59eY-VzMhlN0WGw6d-qS-rm6jc2ZxwY6lrmP22Z_E1hlOypUrt4dMa9jbsN4FBTle1UEl18lnBej2pU2N1J8HI-QiJLd7XWb3G9EoCUP-E" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اتاق جنگ با یاشار : خونثانیاهو
@WarRoom</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/withyashar/21229" target="_blank">📅 00:15 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21227">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/C6sFeWtfYQXI82ZE_EF0baTOhgcYhn-TMrhNjg4k36DaL-h0jzPvlZc2EDci0HGqGk9YTHUf9XioekFkn2bpBJqfNmodxTOcHgErNSTVdvYhsVmsoLHlGA7FeMq-6rRadauqYx_lwwRPMFUTxxEu3tJ1wGyAaoQBq54P1sPZIK69mee4BEgBQt9U5xVFh7NPO5mc-_OcB5IdyxgQW-7hbKmRlEXeLSw1qmRm48hj1Z59YiHeIvLFNc5OaR1xYC61jHFTg1LZ-v4Z5q9O-mnyZGN81LjrUzZYYdLALBsf-FX8rkabDAsRjGqe_y1xkDzulsXBNf46Ptd1bhHN-n_P-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cKWWRlZa7-69bBHZKvAefSsNuwMY3jQ6YHaxr5x7pznAqVI2AqcCZ2p4wFGhRnzOUsJBqwgnfdkSdP9ghd9AxIRTlvksZ26z7DVbQCbYAI4VkVRTTMHmDIbuo_bgwiyuX7_gar8tWlcCvvlBNZOCbyjnijL8AXXo0YM5LsV7bf2la1SXCRLRanBB_ctBDGTA8W94iI3i3Y3TGOSsRHtj0PRNlIdZTq5Dpelrqcc4czMcSJ03pxDFQrqCUfLSFXH-Np4Fz4iFqRgQl7J7G7aB01wqfjFHmRZ8vCUvDnYUqS8C_U6FrIiHyTUTTV5nYbffZnPTHh3surzZ4tRYZLSioQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">تویت جدید مم باقر که با سرش تنگه هرمز رو بسته نگه داشته
🤣
@WarRoom
یاشار : خودش داره میگه تنها راش اینه سرم بره</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/withyashar/21227" target="_blank">📅 23:34 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21226">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f25637c93b.mp4?token=HiV6Jal7DlL8798TRI6JnF-yXJv_efliPhj0RexAtRSWEF6HxKrQ2nhWfR_jBO27fYtmGShENcVjIg98xjocjvzRxMLYYNoC7a0HelYS81hO_RQc6_FsAerldu1mnBVXuNwaHRKicnCMCZpdJnMpxHj6dCRJv6xDXouQnnVh0X0fufWi0i77xszieQ0kgIULnn86_mxKlZzLYQ4hoAosW-r0jmrXsyh333YvbhQF0AGINXMk6X7yV3N8vztY6yjZoYt48UxYNF_ApzCahkXsplxy0_GCKoA1DHJM8B6Zpl--pNQfve1hEsefVrH2cL2MpUUNLPGk5BIxegnZEMZSRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f25637c93b.mp4?token=HiV6Jal7DlL8798TRI6JnF-yXJv_efliPhj0RexAtRSWEF6HxKrQ2nhWfR_jBO27fYtmGShENcVjIg98xjocjvzRxMLYYNoC7a0HelYS81hO_RQc6_FsAerldu1mnBVXuNwaHRKicnCMCZpdJnMpxHj6dCRJv6xDXouQnnVh0X0fufWi0i77xszieQ0kgIULnn86_mxKlZzLYQ4hoAosW-r0jmrXsyh333YvbhQF0AGINXMk6X7yV3N8vztY6yjZoYt48UxYNF_ApzCahkXsplxy0_GCKoA1DHJM8B6Zpl--pNQfve1hEsefVrH2cL2MpUUNLPGk5BIxegnZEMZSRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ در مورد ایران:
ما چیزهایی داریم که می‌توانیم علیه ایران تحریم کنیم. ما تحریم‌های بسیار سختگیرانه‌ای داریم و خواهیم دید چه اتفاقی می‌افتد.
@WarRoom</div>
<div class="tg-footer">👁️ 66.2K · <a href="https://t.me/withyashar/21226" target="_blank">📅 23:22 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21225">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0003edd740.mp4?token=vVES2fALxOKdRJTho8e01gvpiBaH-Uv7QzfECQgCha1bNWH78C1RhdUuaY0gVBIuuskffiHWEW4hsAOr-gJwpd0PK8GAdqzyU4vcRbbRzodXWrex1Mi4EECQ0ItendKbDn-Juh7isHYp3KV6Qpbh-YjjnZVALfsHPuLD4HGB0vDGmOmdk6Ls0ypvZ2XDxxOTygUeSO3oGxiXTLvpXXbeElh_W9pF2QUOWth8ZdoPAUtJnp3tux0KXikdjUhdW4sk4TzwIj1aDaxGNjplVfUVt12l6plWk37uUKEyjmyaBsgxX3qT0lRk48qEXGj8qwXhsajCoIRb2v0rbHc8RrS3aw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0003edd740.mp4?token=vVES2fALxOKdRJTho8e01gvpiBaH-Uv7QzfECQgCha1bNWH78C1RhdUuaY0gVBIuuskffiHWEW4hsAOr-gJwpd0PK8GAdqzyU4vcRbbRzodXWrex1Mi4EECQ0ItendKbDn-Juh7isHYp3KV6Qpbh-YjjnZVALfsHPuLD4HGB0vDGmOmdk6Ls0ypvZ2XDxxOTygUeSO3oGxiXTLvpXXbeElh_W9pF2QUOWth8ZdoPAUtJnp3tux0KXikdjUhdW4sk4TzwIj1aDaxGNjplVfUVt12l6plWk37uUKEyjmyaBsgxX3qT0lRk48qEXGj8qwXhsajCoIRb2v0rbHc8RrS3aw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران:
خطوط لوله زیادی در حال ساخت هستند. من فکر می‌کنم تنگه هرمز به اندازه گذشته مهم نخواهد بود.
در حال حاضر، تنگه باز است. قایق‌های زیادی از آن عبور می‌کنند. مردم این را گزارش نمی‌کنند.
@WarRoom</div>
<div class="tg-footer">👁️ 68.5K · <a href="https://t.me/withyashar/21225" target="_blank">📅 23:11 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21224">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">ترامپ: در حال حاضر با ايران مذاکره نمی‌کنیم، زیرا مذاکره با آن‌ها اتلاف وقت است.
@WarRoom</div>
<div class="tg-footer">👁️ 67.6K · <a href="https://t.me/withyashar/21224" target="_blank">📅 23:08 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21223">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Oy0R7sVdYAritd2tcy02nEelMkM-T26Bbxg7o0ShfVLhSKw-wEpCpo0KTvZF3SbRvTMsF-MvVu4wqzINT2wRbokCnBKwsqmCVJkqKXuyYdVHnGMdCUrYujdBlqhq0zwQ3GqNQXYXxFkfRDcmsUhrGeXqIxjHk3yY1tZY6C5TKQRi9ZQmTnR2WogUIxUHsYKAlmszdTftZrSgcuF1pOzyapabqX0RtD0amKKZxPJYKF4zuVsz-YT68RnoQXQ97i9fpd-Cea8sQB6jGuzPfCw0LgS8fPAhhXOsYZXKj9TJAWbzaKEWvpjlIj0xGMoSLBFEuwhEAjdw7XtmETjbV8WxHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرانسه نیلوفر شادمهری، رایزن فرهنگی جمهوری اسلامی را از این کشور اخراج کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 77.7K · <a href="https://t.me/withyashar/21223" target="_blank">📅 22:34 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21222">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">زلزله ۴.۲ ریشتری حوالی گیلانغرب در استان کرمانشاه را لرزاند
@WarRoom</div>
<div class="tg-footer">👁️ 76.2K · <a href="https://t.me/withyashar/21222" target="_blank">📅 22:29 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21221">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">کانال 13 اسرائیل به نقل از یک منبع نظامی: آخرین چیزی که به آن نیاز داریم، یک جنگ تمام‌عیار با ترکیه است. ما از میدان‌های درگیری کافی در حال حاضر برخورداریم.
@WarRoom</div>
<div class="tg-footer">👁️ 81.7K · <a href="https://t.me/withyashar/21221" target="_blank">📅 22:06 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21220">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">نتانیاهو: ما توضیح دادیم که با حضور نظامی ترکیه در سوریه مخالفیم، و به نظر می‌رسد که آنها به خوبی به ما گوش ندادند، بنابراین تلاش کردیم تا آنها بهتر درک کنند.
@WarRoom
😁</div>
<div class="tg-footer">👁️ 87.6K · <a href="https://t.me/withyashar/21220" target="_blank">📅 21:34 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21219">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">ممرضا نقدی : ما باید به بازدارندگی دست پیدا کنیم. برای ما خوب نیست که کسی بتواند تصمیم بگیرد به ایران حمله کند، و سپس، در صورت شکست، عقب‌نشینی کند، خود را سازماندهی کند و شش ماه بعد دوباره بازگردد.
@WarRoom</div>
<div class="tg-footer">👁️ 91.1K · <a href="https://t.me/withyashar/21219" target="_blank">📅 20:57 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21218">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">مارک لوین : من با ویکتور دیویس هنسون (مورخ، نویسنده و تحلیلگر سیاسی آمریکایی) موافقم؛ او در برنامه من در فاکس نیوز استدلال کرد که ما باید از تشکیل یک دولت در تبعید ایران با رهبری شاهزاده رضا پهلوی حمایت کنیم. و اگر رژیم ایران فروبپاشد، او می‌تواند در دوران گذار، به‌عنوان یک رهبر موقت ایفای نقش کند.
به مردم ایران سلاح بدهید!
@WarRoom</div>
<div class="tg-footer">👁️ 93.5K · <a href="https://t.me/withyashar/21218" target="_blank">📅 20:24 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21217">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">رویترز: بریتانیا امروز ۷ فرد و نهاد جدید مرتبط با ایران را به فهرست تحریم‌های خود اضافه کرد. این تحریم‌ها در چارچوب تحریم‌های رژیم ایران اعمال شده
@WarRoom</div>
<div class="tg-footer">👁️ 92.4K · <a href="https://t.me/withyashar/21217" target="_blank">📅 20:06 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21216">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">ارتش اسرائیل: ما دیروز در منطقه ساحلی، یک فرمانده گردان و سه فرمانده گروه را از نیروهای نخبه در گردان بیت لاهیا وابسته به حماس به هلاکت رساندیم.
@WarRoom</div>
<div class="tg-footer">👁️ 91.3K · <a href="https://t.me/withyashar/21216" target="_blank">📅 20:00 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21215">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">ترامپ امروز در کاخ سفید با شماری از مدیران و چهره‌های بزرگ صنعت رمزارز دیدار می‌کند. در این نشست، مقررات جدید بازار کریپتو، قانون CLARITY و تعیین حدود اختیارات SEC و CFTC بررسی خواهد شد. رؤسای SEC و CFTC و مدیران شرکت‌هایی از جمله Coinbase و Ripple نیز در این نشست حضور خواهند داشت
@WarRoom</div>
<div class="tg-footer">👁️ 92.3K · <a href="https://t.me/withyashar/21215" target="_blank">📅 19:37 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21214">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ab2cd42e14.mp4?token=t3KoDq5oG_HJwny-Sp3u09mePnzVUVHmx5l5R8SMi5C8H-BC0dPZakFuOthnTCXT-wAdW50T30jQXIRbhzaK4_jUpeUhXfxQ_mI29FJV_I9xNWmneJp6zBWYUk3rEATaNnrCDAf2LuNnYu5i4JsaKuR72oWpejrPIv-IZv7wf7_6ENmBzxsbkupBjtXokSVdQ625TtA8GYjJYdEsLXIT9bhqZTH6gfDtV1oOr17yDc7VvcQ9_UUtILdVEopJABxYHoLJ_we5BIYxRBB257w8oDNfGgc9KgRIh3wY2f1X71mOLL-piY8yJ-HG6EviCX5rSNwkwCHJcPkjBMnwhh4dVEX652fQ82n-MaREtUmDN_swY1hMkoSI01cMi4gpt5vK-CjbM9IAhTJYcDbhP72cDgiqrhoXCduG3LDsNqAX1ZJByNDl6dBukPu27brpUSembfIq5edV3O6j-r1ZHUHTb5fitCZWx8VYroRFNox-qig4XPb9hK29RyOiueuf8XFxpgvcXog0PYrSy3iEbwTYNYBr9YRRnLY_Vm4UWUmGR_6xdrrsdLxTG1Mm9o5qVh9k6oemAZa5WwogJXms7H-xD525CyrXKjuBfFZcJi5xJwi2-hymyVRWFyVNSc7k8MD39txV_flaImjZt0TBwC06yEIV9UGcKJy9tTYC9TayA6o" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ab2cd42e14.mp4?token=t3KoDq5oG_HJwny-Sp3u09mePnzVUVHmx5l5R8SMi5C8H-BC0dPZakFuOthnTCXT-wAdW50T30jQXIRbhzaK4_jUpeUhXfxQ_mI29FJV_I9xNWmneJp6zBWYUk3rEATaNnrCDAf2LuNnYu5i4JsaKuR72oWpejrPIv-IZv7wf7_6ENmBzxsbkupBjtXokSVdQ625TtA8GYjJYdEsLXIT9bhqZTH6gfDtV1oOr17yDc7VvcQ9_UUtILdVEopJABxYHoLJ_we5BIYxRBB257w8oDNfGgc9KgRIh3wY2f1X71mOLL-piY8yJ-HG6EviCX5rSNwkwCHJcPkjBMnwhh4dVEX652fQ82n-MaREtUmDN_swY1hMkoSI01cMi4gpt5vK-CjbM9IAhTJYcDbhP72cDgiqrhoXCduG3LDsNqAX1ZJByNDl6dBukPu27brpUSembfIq5edV3O6j-r1ZHUHTb5fitCZWx8VYroRFNox-qig4XPb9hK29RyOiueuf8XFxpgvcXog0PYrSy3iEbwTYNYBr9YRRnLY_Vm4UWUmGR_6xdrrsdLxTG1Mm9o5qVh9k6oemAZa5WwogJXms7H-xD525CyrXKjuBfFZcJi5xJwi2-hymyVRWFyVNSc7k8MD39txV_flaImjZt0TBwC06yEIV9UGcKJy9tTYC9TayA6o" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ : مردم دارند جایگزینی برای تنگه هرمز پیدا می‌کنند. می‌دانید جایگزین‌ها چیست: تگزاس، آلاسکا، لوئیزیانا.
مردم برای نفت دارند به آمریکا می‌آیند.
@WarRoom</div>
<div class="tg-footer">👁️ 91.1K · <a href="https://t.me/withyashar/21214" target="_blank">📅 19:28 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21213">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cce66acfb3.mp4?token=RBsXllVCbLvarY4jn9lUtYZiS0eb23iluUq7D0_ADfBnhcivROn56JCoZredRsT7N9t8C41J5Dp3AdMq3ev1g2Zz6CGtkyQPGgPfOoNTDqDPhSpapUmcDTdN4krgmllIXAqFjiQbJ2JD6uXwSewa-Z1m5fm4L56mgqFDdKSSYUzVaBBhoeSud_RdBkK_Gux5xN3XaErWKdNeuzgV_PgJ9ZAuo84LDfV467RLYscHGaZz5el2hodDSVmASfg62TDr9Qtc9mdJCrcjcgufztIJWotikQjjtPXlfJHCIwwq0fT_btZkEDMrNL-gScj4kgCtOxtw60ON2i3j75FcnZmAAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cce66acfb3.mp4?token=RBsXllVCbLvarY4jn9lUtYZiS0eb23iluUq7D0_ADfBnhcivROn56JCoZredRsT7N9t8C41J5Dp3AdMq3ev1g2Zz6CGtkyQPGgPfOoNTDqDPhSpapUmcDTdN4krgmllIXAqFjiQbJ2JD6uXwSewa-Z1m5fm4L56mgqFDdKSSYUzVaBBhoeSud_RdBkK_Gux5xN3XaErWKdNeuzgV_PgJ9ZAuo84LDfV467RLYscHGaZz5el2hodDSVmASfg62TDr9Qtc9mdJCrcjcgufztIJWotikQjjtPXlfJHCIwwq0fT_btZkEDMrNL-gScj4kgCtOxtw60ON2i3j75FcnZmAAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: ما تنگه هرمز را کاملاً در اختیار داریم و کنترل آن را در دست داریم.
@WarRoom</div>
<div class="tg-footer">👁️ 88K · <a href="https://t.me/withyashar/21213" target="_blank">📅 19:13 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21212">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">ترامپ در مورد ایران:
ایران نمی‌تواند سلاح هسته‌ای داشته باشد. می‌دانید چرا؟ چون از آن استفاده خواهند کرد.
ما اجازه نمی‌دهیم از آن استفاده کنند.
@WarRoom</div>
<div class="tg-footer">👁️ 85.5K · <a href="https://t.me/withyashar/21212" target="_blank">📅 19:11 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21211">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/34d548b77d.mp4?token=X3pnvRuLwLA9DBzxf5kTu7iglFp9thp_KOrtQ1b_3i-s7Vq4MufGAjoVF31Dqt2qi-m_3MY4bbkWlcx7SoExJMGEKN3CEJm8Er_CuU6Fq8GJtraHNxjTqmoHnuU0n47JxfBq-6KGys-vUo5F5rFbGkc6VVgq386qrQYHLcZLfCwyZj2oVXFaF9NedojlmtzI9MC3h_SAAW5yWpw29AxLpMouRZ5cpDTUMqMvXunp5iB_Ep0rQR6SZn92raGMfZJURUbQ2F1iJz3tqhdqvsK-8RHVlBb-DO7Ab6aKovTPJNhzdH6iomBY2g5WRBKPfeZYQRcGsJQmxSB9OvXdh5Z7dQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/34d548b77d.mp4?token=X3pnvRuLwLA9DBzxf5kTu7iglFp9thp_KOrtQ1b_3i-s7Vq4MufGAjoVF31Dqt2qi-m_3MY4bbkWlcx7SoExJMGEKN3CEJm8Er_CuU6Fq8GJtraHNxjTqmoHnuU0n47JxfBq-6KGys-vUo5F5rFbGkc6VVgq386qrQYHLcZLfCwyZj2oVXFaF9NedojlmtzI9MC3h_SAAW5yWpw29AxLpMouRZ5cpDTUMqMvXunp5iB_Ep0rQR6SZn92raGMfZJURUbQ2F1iJz3tqhdqvsK-8RHVlBb-DO7Ab6aKovTPJNhzdH6iomBY2g5WRBKPfeZYQRcGsJQmxSB9OvXdh5Z7dQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار: آیا شما دوباره با ایران مذاکره خواهید کرد؟
ترامپ: شاید در مقطعی، اما الان به همین حالت اوضاع خیلی خوب است.
@WarRoom</div>
<div class="tg-footer">👁️ 85.6K · <a href="https://t.me/withyashar/21211" target="_blank">📅 19:10 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21210">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc2b72a973.mp4?token=UZ64IwM9UUUqE5uV627PKMUvF0C0EoPA-X8fTNYIm-mav-KNtdNc2sNy1qrVKsRBG-h5XMt4ZOV7QkVGV6jo-xU6IFIggsrGtOxjGBEy-BUDT4QfiIHVnYlTxLqZdCZXE7dLSCjJP3QsMwQaV-uIK-QRsiDMg-lPXgAkMZcTaWwc6ticmBSe4HjAhL7QquegsMZj7kIsCwWcB5tLERKk__037CbDDN65BWXxHYWkokSWkXXas4zEdwbSQhxqm5hI5gpcMQXfNhClw8kOEQZx25a27pVk8zj_sFeRQ7TAs0VB8huSygIzn0_sETPaWHHTBDCH44vjRjKzdrdRfjNKUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc2b72a973.mp4?token=UZ64IwM9UUUqE5uV627PKMUvF0C0EoPA-X8fTNYIm-mav-KNtdNc2sNy1qrVKsRBG-h5XMt4ZOV7QkVGV6jo-xU6IFIggsrGtOxjGBEy-BUDT4QfiIHVnYlTxLqZdCZXE7dLSCjJP3QsMwQaV-uIK-QRsiDMg-lPXgAkMZcTaWwc6ticmBSe4HjAhL7QquegsMZj7kIsCwWcB5tLERKk__037CbDDN65BWXxHYWkokSWkXXas4zEdwbSQhxqm5hI5gpcMQXfNhClw8kOEQZx25a27pVk8zj_sFeRQ7TAs0VB8huSygIzn0_sETPaWHHTBDCH44vjRjKzdrdRfjNKUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره تنگه هرمز:
قرار نیست کارمان بی‌نقص باشد، اما نفت زیادی از آن خارج می‌شود، خیلی زیاد.
مردم شگفت‌زده هستند.
@WarRoom</div>
<div class="tg-footer">👁️ 88.4K · <a href="https://t.me/withyashar/21210" target="_blank">📅 19:09 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21209">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca74a36348.mp4?token=X9BHlq8HBWmELlCL4fvcpn1e00Uwtzid8MzxUpzltPP6fqDpkFBoNnF_77POEHQVcTQqqEIqLOZSKrDxD9Itcv0nySOw4whdWFFpOXSxd2ITF08RQZUpc5r2tqk1Ke2lE-ImYa_viF9N_6N0OKuvI1UTXQ9XkcznoCF-kGnt8ReCRQJEfmF3SU91yTp-6iyNs2M85PJXAGhDGvNiYP9D5pfHkb_jb1sa1BM4Q_EMJk4Wxr7lqij4sRqLPzvcSl011iRCKECmzfGEhZxDNUS6UuURs9ykibhNj-M9wyx-Be6YEvptJCqkMAzNG32Wc1KA_TbBeFhKFzhgAoC0D8GDTzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca74a36348.mp4?token=X9BHlq8HBWmELlCL4fvcpn1e00Uwtzid8MzxUpzltPP6fqDpkFBoNnF_77POEHQVcTQqqEIqLOZSKrDxD9Itcv0nySOw4whdWFFpOXSxd2ITF08RQZUpc5r2tqk1Ke2lE-ImYa_viF9N_6N0OKuvI1UTXQ9XkcznoCF-kGnt8ReCRQJEfmF3SU91yTp-6iyNs2M85PJXAGhDGvNiYP9D5pfHkb_jb1sa1BM4Q_EMJk4Wxr7lqij4sRqLPzvcSl011iRCKECmzfGEhZxDNUS6UuURs9ykibhNj-M9wyx-Be6YEvptJCqkMAzNG32Wc1KA_TbBeFhKFzhgAoC0D8GDTzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ در مورد کیم جونگ اون:
این واقعیت که من با کیم جونگ اون خوب کنار می‌آیم چیز خوبی است.او ۵۷ سلاح هسته‌ای بسیار قدرتمند دارد. هرگز نباید اجازه می‌داد این اتفاق بیفتد، اما او آنها را دارد.من با او خیلی خوب کنار می‌آییم. من کیم جونگ اون را خیلی خوب می‌شناسم. او خوب خواهد بود.تا زمانی که یک رئیس جمهور باهوش داشته باشیم، او خوب خواهد بود. اگر یک رئیس جمهور احمق داشته باشیم، احتمالاً او خوب نخواهد بود.
@WarRoom</div>
<div class="tg-footer">👁️ 89.6K · <a href="https://t.me/withyashar/21209" target="_blank">📅 19:04 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21208">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">پولیتیکو : ایران و آمریکا وارد فاز صبر و انتظار شده‌اند؛ هر یک منتظرند تاب‌آوری دیگری زودتر تمام شود
@WarRoom</div>
<div class="tg-footer">👁️ 96.6K · <a href="https://t.me/withyashar/21208" target="_blank">📅 17:20 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21207">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eck6mfYcIUC-wO3Y38-CJ8Iut2wgLAn7VGLXULR6b_YGUVTAFXxoNnYKZrViV5Hu8kMOHPlvaxRiKqRCjBuLzCzbZ3QE4wg3VDB1HhqwQBFrhwvsAgF5E-fA-Jiwlf_Lg0ysP5gnGVviKFv9OX2c43NBSztFKyGi7jXeZXcTSnzHNdGOSgeOudOfJeLzsY2VB_ZWAp9CbbftFZy7rFyS0y1Xt6KiX8c8hcgJ7O4Z_-G2blS7esoVew-9EYg9Y6ezVwEcP6UPFNG68Cf69vwiDxqefAGIKw6RbvaxcNO6epXDfo61dGP-RE24GPBuBJ7Do0sFvzQj9XCKTm8ePr5gVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سنتکام: یک فروند جنگ الکترونیک EA-18G Growler نیروی دریایی آمریکا، هنگام انجام گشت‌زنی بر فراز خاورمیانه، از یک فروند KC-135 Stratotanker نیروی هوایی آمریکا سوخت‌گیری می‌کند
@WarRoom</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/21207" target="_blank">📅 16:00 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21206">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">مرندی مشاور تیم مذاکره کننده : دیروز، کاخ سفید گفت که مذاکراتِ وجود نداشته با ایران را «به حالت تعلیق درآورده» است؛ ظاهراً با این هدف که فشار اقتصادی را افزایش دهد. اما چیزی که کاخ سفید نمی‌گوید این است که آن‌ها تا همین امروز همچنان در حال ارسال پیام به تهران هستند.
@WarRoom</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/21206" target="_blank">📅 14:47 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21205">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">یک مقام ناتو در واکنش به گزارش‌ها درباره احتمال تهدید اهداف آمریکایی در اروپا از سوی ایران گفت:
ناتو آماده مقابله با هرگونه تهدید علیه کشورهای عضو است و برای دفاع از همه متحدان خود هر اقدام لازم را انجام خواهد داد.
این مقام تأکید کرد که وضعیت بازدارندگی و دفاعی ناتو «قوی و مؤثر» است و یادآوری کرد که سامانه‌های پدافند هوایی ناتو پیش‌تر نیز موشک‌های بالستیک شلیک‌شده از ایران به سمت ترکیه را در چهار مورد رهگیری کرده‌اند.
@WarRoom</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/21205" target="_blank">📅 14:41 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21204">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">ناو هواپیمابر یواس‌اس جورج واشنگتن به عنوان بخشی از عملیات خود در منطقه عملیاتی ناوگان هفتم ایالات متحده، از تنگه سنگاپور و تنگه مالاکا عبور می‌کند.
@WarRoom</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/21204" target="_blank">📅 14:19 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21203">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">وال استریت ژورنال: مقام‌های عرب می‌گویند ما «بین ایران و آمریکا گیر افتاده‌ایم»
آن‌ها معتقدند جمهوری اسلامی در نهایت به افزایش فشار اقتصادی، واکنش نظامی نشان خواهد داد، در نتیجه، جنگ دوباره می‌تواند شدت بگیرد
حملات اخیر جمهوری اسلامی در تنگه هرمز، روشی را که برای حفظ صادرات و تولید نفت به کار گرفته شده ، تهدید می‌کند , در این روش که «سفرهای شاتل» نامیده می‌شود، نفت خام و فرآورده‌های نفتی از داخل خلیج فارس به کشتی‌هایی منتقل می‌شوند که در خارج از منطقه منتظر هستند تا محموله را به بازارهای جهانی منتقل کنند
@WarRoom</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/21203" target="_blank">📅 14:12 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21202">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">ارتش اسرائیل : ما در چارچوب خنثی کردن شبکه تونل‌های سازمان‌های تروریستی، دو تونل زیرزمینی حماس در شرق خط زرد در نوار غزه را مسدود کردیم که در مجموع بیش از دو کیلومتر طول داشتند.
@WarRoom</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/21202" target="_blank">📅 12:57 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21201">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d47b2eca4.mp4?token=W5IMhzaIyNKU-NcHc6SD39jPgHkQM4kZQcOTGmRHVg7EYIMBOJo6WRIiJEEE9ieB_MCnHNGoo6LKKBRsMz8uL0HpyU6kmIN0Avvg6ZIPQtubHyGp8Vg-A466jIOYaC_e5ev4NZvwU5ju7aM_6FAdSF4RMvDURoYQkOHA-xhyjdAdj9ow3nrzB0ZDWQj04NgZOAvNk8VBa7ArPUs4SwrYk0Qyc84cqkIa5CGyB25mI19XfEos4EYLVuOpO5XEybWXBjVCpza4lFZoncbAlMzfr2RD7xYdAg7cYw6NyxPmQhXz3euEJxFC8BZmupsUcGMT8iiKAtC7QxoBNDKWmHGiaoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d47b2eca4.mp4?token=W5IMhzaIyNKU-NcHc6SD39jPgHkQM4kZQcOTGmRHVg7EYIMBOJo6WRIiJEEE9ieB_MCnHNGoo6LKKBRsMz8uL0HpyU6kmIN0Avvg6ZIPQtubHyGp8Vg-A466jIOYaC_e5ev4NZvwU5ju7aM_6FAdSF4RMvDURoYQkOHA-xhyjdAdj9ow3nrzB0ZDWQj04NgZOAvNk8VBa7ArPUs4SwrYk0Qyc84cqkIa5CGyB25mI19XfEos4EYLVuOpO5XEybWXBjVCpza4lFZoncbAlMzfr2RD7xYdAg7cYw6NyxPmQhXz3euEJxFC8BZmupsUcGMT8iiKAtC7QxoBNDKWmHGiaoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ممباقر در عراق…
@WarRoom</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/21201" target="_blank">📅 11:48 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21200">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">سی‌ان‌ان: ایران بخش قابل‌توجهی از کنترل خود بر تنگه هرمز را از دست داده است.
بر اساس داده‌های شرکت کپلر، در دو هفته گذشته
بیش از ۸۰ درصد کشتی‌های عبوری از مسیر تحت نظارت عمان
در بخش جنوبی تنگه عبور کرده‌اند؛ مسیری که ایران با آن مخالف است. برخی کشتی‌ها نیز با وجود تهدیدهای ایران، با اتکا به حضور نیروی دریایی آمریکا از این مسیر عبور کرده‌اند. یک تحلیلگر کپلر گفته است که به نظر می‌رسد ایران
دست‌کم بخشی از کنترل تنگه را از دست داده است
؛ هرچند ایران همچنان با تهدید حمله و ایجاد بازدارندگی، توان تأثیرگذاری بر رفت‌وآمد دریایی را حفظ کرده است.
@WarRoom</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/21200" target="_blank">📅 11:07 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21199">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">الجزیره : این ترامپ نیست که مانع عبور کشتی‌ها از تنگه هرمز می‌شود، بلکه شرکت‌های بیمه این کار را می کنند
تا زمانی که تهدید فیزیکی علیه تردد دریایی وجود داشته باشد، این شرکت‌ها از قدرت مالی خود برای جلوگیری از عبور کشتی‌ها استفاده خواهند کرد
بدون تضمین‌های قاطع مبنی بر اینکه کشتی‌ها از حملات ایران در امان خواهند بود، مالکان حاضر نمی‌شوند که در تنگه تردد کنند
@WarRoom</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/21199" target="_blank">📅 11:02 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21198">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">اورشلیم پست: تام باراک، نماینده ویژه آمریکا، هشدار داد که حمله اسرائیل به پایگاه هوایی ابو الظهور در نزدیکی ادلب در سوریه، می‌توانست منجر به تشدید تنش‌ها و یک رویارویی نظامی مستقیم، احتمالاً با ترکیه، شود.
@WarRoom</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/21198" target="_blank">📅 10:56 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21197">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">رویترز : آمریکا برای
بازسازی ذخایر تسلیحاتی و افزایش توان تولید مهمات
، بودجه‌ای بیش از یک تریلیون دلار پیشنهاد کرده است. پنتاگون قراردادهای تسلیحاتی را از پنج‌ساله به
هفت‌ساله
افزایش می‌دهد تا شرکت‌های دفاعی با اطمینان بیشتری کارخانه‌ها و ظرفیت تولید خود را گسترش دهند. هدف، افزایش شدید تولید
موشک‌های رهگیر پاتریوت و THAAD
و جبران ذخایری است که در جنگ ایران و دیگر درگیری‌ها کاهش یافته‌اند. همزمان، آمریکا تولید موشک‌های کروز را نیز افزایش می‌دهد؛ از جمله قرارداد
۲۲.۹ میلیارد دلاری هفت‌ساله با ریتیان برای افزایش تولید تام‌هاوک از حدود ۶۰ فروند به بیش از هزار فروند در سال
.
@WarRoom</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/21197" target="_blank">📅 10:45 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21196">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">فایننشال تایمز: ایران در صورت تشدید جنگ از سوی ترامپ، حمله به اهداف نظامی آمریکا در اروپا را بررسی می‌کند.
به گفته دو منبع نزدیک به حکومت ایران، نیروهای ایرانی گزینه حمله به دارایی‌های نظامی آمریکا در
بلغارستان و قبرس
را بررسی کرده‌اند. همچنین حمله به
کابل‌های فیبر نوری زیردریایی در تنگه هرمز
نیز از گزینه‌های مورد بررسی است. این منابع هشدار داده‌اند که در صورت حمله آمریکا به زیرساخت‌های ایران، تهران ممکن است دامنه درگیری را فراتر از خاورمیانه گسترش دهد.
@WarRoom</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/21196" target="_blank">📅 10:39 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21195">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BM_Y0fFBmGDkCOGtG4FGGvS72vZ-IrReGAK7vvcRdj5OxMQuM5LHT2TP4lbmE0e3fqBYmpGWFuBLNE6EJxpVY-cTsi1YynC_cq54MkyAGPxomPSF0AZSmqFLcIOzBpLolAACMJ-CaF04869jn-VJrJDASaDSWTuU34mMtPzlHrMaESrfRwSrrCisaolbXbCm6OwkHIXwGh31188oqUDAJrbiMJ3H-giVta6eBUQrs9-rVbFYjEpNuTExMX2E0tSpm32tUJFvRframvp6za9K5Ugeep6f0T4nynms9Mn8koDIPUxkYJsbBCCGCrftMSvD1iKSGveG_O_Uzr4X_i6VTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تا سقف ۱۰ میلیون دلار پاداش برای اطلاعات درباره هکرهای ایرانی
بهزاد مصری , کیوان فیاض ، مجتبی غاله‌کوهی ، آرمان کهزادیان ، صابر شهبازی
@WarRoom</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/21195" target="_blank">📅 10:31 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21194">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">یک مقام ارشد وزارت خارجه آمریکا می‌گوید:
«اهرم‌های متعددی وجود دارد که رئیس‌جمهور می‌تواند در هفته‌ها و ماه‌های آینده، در صورت انتخاب این مسیر از سوی ایران، فشار آن‌ها را افزایش دهد.»
@WarRoom</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/21194" target="_blank">📅 10:25 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21193">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/21193" target="_blank">📅 03:13 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21192">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/21192" target="_blank">📅 02:39 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21191">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/withyashar/21191" target="_blank">📅 02:26 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21190">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-footer">👁️ 131K · <a href="https://t.me/withyashar/21190" target="_blank">📅 02:12 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21189">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-footer">👁️ 134K · <a href="https://t.me/withyashar/21189" target="_blank">📅 01:18 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21188">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-footer">👁️ 134K · <a href="https://t.me/withyashar/21188" target="_blank">📅 01:10 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21187">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">الجزیره : ترامپ به تیم خود دستور داده تا زمانی که ایران آماده امضای توافق نیست، با این کشور دیگر مذاکره نکنند @WarRoom</div>
<div class="tg-footer">👁️ 137K · <a href="https://t.me/withyashar/21187" target="_blank">📅 00:46 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21186">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">اینترنت</div>
<div class="tg-footer">👁️ 134K · <a href="https://t.me/withyashar/21186" target="_blank">📅 00:38 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21185">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">خبرنگار شبکه ۱۲ اسرائیل:
نتانیاهو با یک رویکرد برنامه‌ریزی‌شده، در حال آماده‌سازی جنگ آینده علیه ترکیه است.
@WarRoom</div>
<div class="tg-footer">👁️ 136K · <a href="https://t.me/withyashar/21185" target="_blank">📅 00:09 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21184">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">ترامپ در فاکس‌نیوز هشدار داد که اگر عمان مانع منافع آمریکا شود، این کشور را بمباران خواهد کرد @WarRoom</div>
<div class="tg-footer">👁️ 135K · <a href="https://t.me/withyashar/21184" target="_blank">📅 00:02 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21183">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">خبرنگار اکسیوس: «مقام ارشد اسرائیلی ادعا می‌کند که حمله به پایگاه نیروی هوایی سوریه در منطقه ادلب با هدف جلوگیری از استقرار نظامی ترکیه در آنجا انجام شده است.» مقام ارشد ترکیه پاسخ می‌دهد: «هیچ حضور ترکیه‌ای در پایگاه هوایی وجود نداشت. اسرائیل در حال بهانه‌تراشی…</div>
<div class="tg-footer">👁️ 133K · <a href="https://t.me/withyashar/21183" target="_blank">📅 23:59 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21182">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">خبرگزاری الخلیج ،وزارت خارجه امارات :
در پی تشدید تنش‌های منطقه‌ای، تمامی فعالیت‌های تجاری، مبادلات تجاری و معاملات مالی با ایران تا اطلاع ثانوی متوقف شد.
@WarRoom</div>
<div class="tg-footer">👁️ 132K · <a href="https://t.me/withyashar/21182" target="_blank">📅 23:55 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21181">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">❤️‍🩹</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/21181" target="_blank">📅 23:43 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21180">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">سیریک موشک بلند شد
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/21180" target="_blank">📅 23:33 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21179">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">اتاق جنگ با یاشار : گزارشهای مردمی از وضعیت ایران بهم نشان میده که فقط یک جرقه لازمه تا این انبار باروت رو منفجر کنه
@WarRoom</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/withyashar/21179" target="_blank">📅 23:14 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21177">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/r0vk3uuCkbZtToMHVKyoGO8vSChW9AX31UQYIEYjflJNpVew_N0dW6TyJH79JkmIxjAA6YTjDoYt06pJWoaNsyX2zOwOS81Fb6X8wshpSZ1H7fp0roS0sbnKXDYkNravBcSmo8DyLTupt0Ck26yCRXAijcuIxU84nwpwaZ1dGSqLWqbszg6_6MaYLbJLmJYvV6YJU2ksmJ_5VtvCKDNK4Ux2gd6AO9tjyIgrovm1bz_Fs7OgJLY8HlzuTGpr5EW7lSv_nNhqeO6pzGt659vJfZHTLvQAGYEP6JlEXthdpL0FbZEyxsbA--VjQYT38Lm45-bNfzYAPoZx_KlE8my_3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cyOiPGFwrXxB3a8KBlpEDFcaWTp-sHKCNnrke3aoZEvw5KN2SQMbw04SMGiCjtaWVQBZO3vfT1-CZyfTept51nOWxVjEOqqZzFd0EQDxbX2qhdbsY0Hef6pGbm7N_l0jUe0MLmOEYjp8gGfmSwlaxQJO_bcvYsNpW4y_8bYWhvL2JKfI3IYe19HcET8qJzMlkVlCbCs0QOFtuIqXqcvtmmArvuetl2aCtB_B9qdyafqJGTIvA94ukuyIjkqvBFCiKe5EdrsbXfSUDQDwL1J0dxtlxdESAFLRlHglIxNMndVXQSI8YFZzBhWDws-uaDpmaLFayH8Mse4zE7LdeB9PUQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">برنامه کوروش بزرگ ۲ روز سالگرد مهسا امینی ، که شاهزاده در تورنتو صحبت میکنه و لیست قیمت های بلیت این برنامه
@WarRoom</div>
<div class="tg-footer">👁️ 133K · <a href="https://t.me/withyashar/21177" target="_blank">📅 23:09 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21176">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">سفیر جمهوری اسلامی در کویت امروز با ۴ نیرو سپاه پاسداران که از چند ماه قبل در این کشور بازداشت شده‌اند، دیدار کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/21176" target="_blank">📅 22:54 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21175">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">اورشلیم پست : پنتاگون از  ۳۰ دانشگاه خواسته بررسی کنند که با نهادهای علمی چین، روسیه و ایران چه نوع همکاری‌هایی دارند و آیا از طریق این همکاری‌ها ممکن است اطلاعات حساس پژوهشی آمریکا به خارج منتقل شود یا نه ،
یک مقام آمریکایی گفت دانشگاه‌های هاروارد، ام‌آی‌تی و دانشگاه برکلی کالیفرنیا هم جزو این ۳۰ دانشگاه هستند
@WarRoom</div>
<div class="tg-footer">👁️ 131K · <a href="https://t.me/withyashar/21175" target="_blank">📅 22:20 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21173">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/H38H1YvyXHRnFZ9SMKAtKYfULBp_Pls1Uu97hafanPuZpjwCfVg-8j1ndkveDG3rMZubvlzZioWtA1ZCBoqaAKsEf8zDFUT-9NXXROnntBXiAAqXh4Hzha3jpYbAd3Ts5dYnoQtoQyxKlWcJJvK7GkghvhQ2ZxDd14X38vu-woJjyW26nBRefeA5R9f-dAdIlvU03Pp3pQa9rJLdNbbWVI6TgHqiioEP--ortnDge9EErSen4bGxXRFjh6yU-PBXyeiZ5h-PWM9atX1Co2qRBSp9RLhOPeGH6-yOKZd2kZAWRpa_MDIg8ffBEDkh_LdWODk-ZStnPYgjlNrymPbFxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ch0pFGOp9azViVaj53OyOk6xjMGLtPuqxxbD2yf9K_CWCRCSDPRCAw9lf9XP1LVMbmwbL3Ddn_uMPS5hza7uSLHUJvldxRQXKC3u8qF8O4TeOyUS6rz9xM6ki29yBxp-tCTKkdt3uqeULMhpqt7FUDbM4NBEhEJ_9qLYOFStwvUPmKFoumTsLXBEcgTOJXjIIl8VDvQgOr6fg-TLlDUQFg7ZmBZHr1lkXa77LkJw0iTmuBP4qiugPU-ASis610ODtMe-xHz1LLrvdwDCYbxOMBlGPvrB3-TE4rxApEfVqGoYBgt7qvEVtaRw-cY9PVH_iynTUQSF18nfybLIIx7n5g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">تصاویر ماهواره‌ای دیروز حداقل ۲۲ هواپیمای سوخت‌رسانی آمریکایی را در فرودگاه رامون و تقریباً ۱۹ هواپیمای دیگر را در پایگاه هوایی عوودا در جنوب اسرائیل نشان می‌دهد
علاوه بر این، حدود ۲۰ هواپیمای سوخت‌رسانی دیگر در فرودگاه بن گوریون وجود دارد که تعداد کل هواپیماهای مستقر در اسرائیل را به تقریباً ۶۰ فروند می‌رساند.
@WarRoom</div>
<div class="tg-footer">👁️ 132K · <a href="https://t.me/withyashar/21173" target="_blank">📅 20:52 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21172">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">روبرتو کارلوس : مسلمان شدم.
@WarRoom</div>
<div class="tg-footer">👁️ 131K · <a href="https://t.me/withyashar/21172" target="_blank">📅 20:14 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21171">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">وزارت دفاع امارات : دو موشک بالستیک را که از سمت ایران در حال حرکت بودند، شناسایی و دفع کردیم. @WarRoom</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/21171" target="_blank">📅 20:11 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21170">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">وزارت دفاع امارات : دو موشک بالستیک را که از سمت ایران در حال حرکت بودند، شناسایی و دفع کردیم.
@WarRoom</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/21170" target="_blank">📅 20:09 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21169">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h2i0l-Aqph9cq7O49JBiGSS_fm2A8xj31eUFH1evRN-MT3NHWO8EEZOx9B8fcsF7Fx0T85YiUb_-bUoGcWdPKaVfHnsGI6kjpMJM98r4pPrOMJCGOUtChHnizm4W-R5zyZ9ZN3LO0FfttC_KauBL9J4sAsuMtgZH5H-lumZoTvEH-_5i1Q_eaDrtxFDeMLPYDvpf7KOVDP3gn_sKCkst99aOjtT-OzR35i0q2JDlIYyNOwHrYKDKMRiuQziF3i2oCp7DpXc5xFjyDTrbTqWS5xhLEvndEWwGF3Dk_ZFLcszrgpaL_OTYzlbKVD0drGk5crVylxIqj5QEqonyAPo0eA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏UKMTO با تأخیر گزارشی از حادثه‌ای در تنگه هرمز دریافت کرده است.
یک شخص ثالث گزارش داده است که یک کشتی فله‌بر هنگام عبور از تنگه هرمز مورد اصابت یک پرتابه ناشناخته قرار گرفته است. این برخورد باعث آسیب به سمت راست کشتی و تلفات خدمه شده است.
@WarRoom</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/21169" target="_blank">📅 20:05 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21168">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">خبرنگار اکسیوس: «مقام ارشد اسرائیلی ادعا می‌کند که حمله به پایگاه نیروی هوایی سوریه در منطقه ادلب با هدف جلوگیری از استقرار نظامی ترکیه در آنجا انجام شده است.» مقام ارشد ترکیه پاسخ می‌دهد: «هیچ حضور ترکیه‌ای در پایگاه هوایی وجود نداشت. اسرائیل در حال بهانه‌تراشی برای بمباران کشورهای همسایه و تضعیف ثبات در منطقه است.»
@WarRoom</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/21168" target="_blank">📅 19:58 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21167">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q-4URWa_TGmlVgEwbbrkRLY6_K0RuSYJ3FE186VLsR-INsvbzoDCDbCFfQ29DNszhGcGoPHqhh7-4yGMlCyQb_snX1EX6nYnNV4CB7AXBcrdffelPlMO5_sqC6dNS2_qdstcLBGRRDl0RnCcxXaBjweG_7L2WFTyGJQqErSus487aARPRvJo0F9jtgEJcC_ks76iSX4kwtZTC1-95WpiDbZxNni_nKPMyW2n9_RGIpsjB6Mmg5qXjK6tJTxgPxYtIxE-74akcbnlWBntvapDn5lqVrfjIKCsZNhcrUZat_sCEWZwy_E2ZjZqQG8Ucu880RjLsd0sv_O_F4RpYc4tJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت جنگ آمریکا با انتشار این عکس از ترامپ نوشت : ما پیروز خواهیم شد
@WarRoom</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/21167" target="_blank">📅 19:54 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21166">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">خبرگزاری رژیم تسنیم مدعی شد که
پرتابه‌های شلیک‌شده به سمت امارات از یمن شلیک شده‌اند.
این ادعا تاکنون
به‌طور رسمی تأیید نشده
و منابع مستقل نیز هنوز آن را تأیید یا رد نکرده‌اند.
@WarRoom</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/21166" target="_blank">📅 19:15 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21165">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">الجزیره : ترامپ به تیم خود دستور داده تا زمانی که ایران آماده امضای توافق نیست، با این کشور دیگر مذاکره نکنند
@WarRoom</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/21165" target="_blank">📅 19:04 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21164">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">آلارم حمله موشکی در‌امارات ممکنه باز اشتباه اومده باشه @WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/21164" target="_blank">📅 18:33 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21163">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">آلارم حمله موشکی در‌امارات
ممکنه باز اشتباه اومده باشه
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 134K · <a href="https://t.me/withyashar/21163" target="_blank">📅 18:24 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21162">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bpti22HvX3At7UG6tXusHY3Uf3GYphuUG5SisF6qDS5WSjHhmjFt61DCIKUuh-aGkNN29Ph4H5OsPNDytfeHeOp2fmkP5udR9D8q-QCKB40kUQmrR4_LaVM_YMn5b9UokbeNQoyZFz7rGEmvn2qKM78EW1CHoWT9XTQ_tu6Yi5umJj3w1srxs-2q0XWesV3sE2uFIuAosISf-VC4KUxVzDBTEy__gP2ubuvnG3D_hQUYuabDnmH9DcnDz9DFkkZhP7qkTu0gsi4vwrFrsDoZ-Uj6kj6plZgT4cHYOxr5rNZbQo_QOTmHnlYmKAliKSI8i3B5sci5T7qlExg0e6pLsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث : هیچ مذاکره یا گفتگویی با جمهوری اسلامی ایران در حال انجام یا برنامه‌ریزی نشده است. محاصره دریایی به قوت خود باقی است. تنگه هرمز باز و فعال است. تمام مین‌های آبی برداشته یا منفجر شده‌اند. از توجه شما به این موضوع متشکرم!
@WarRoom</div>
<div class="tg-footer">👁️ 137K · <a href="https://t.me/withyashar/21162" target="_blank">📅 17:10 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21161">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Eo4w8ihbRQ-mt6vXCKO0nwlq500WNIj9LfqDFq03UkFwzxGfD0w8kc-aFzdskC_CFTv_qAxhYMWn0DXo2KXp9OXb7bDu6vMF1UTHtAxce4x4id5Ho6yAtWwGVLQe-t3-7v4rm926QK95qq5MJ-Gr38rm_mEFc_WBpvZzTLiIzMI_hAPQ2PVSFmiVkhM6CH_PPwEiSkDIhAe_CNG9Yhga3j06AltaJDWea9V7UgFzZECZ3uXgRlnxmfRoaGFEmdchdvg7lVRiIbRXbrSd6Y9k3g48yZASRT3iDkz4sUKnL_j187svxeh02o4EYLtxGqVV5yo017UlGzdwWx_KCHKPqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث و سیگنال حمایت از تغییر رژیم در ایران : لیندسی همین چند هفته پیش داشت خوش می‌گذراند! کلاهش را ببین!
@WarRoom
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 132K · <a href="https://t.me/withyashar/21161" target="_blank">📅 16:49 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21160">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VUrkBwef4-z0JYH1FhkzKj6KkSc1sFADaaBvHy7HqUqBjGSt8VmtFe8sgd-S0zJZSOSiiyJjk-xI9EwpqPsUiYcf_MXQaqBJZNAtBNAH1n46S0RZps4zwmAB2Ueo2iTXBdN5hkhLLZsEEBVlwo3tsIcmlhfv7uCp9IaERGFY4ktS3xcD9UujrcDA9actANJaWL4lm3GPIgnfIN7bU-YWHleRyS6m_9wgekZ_M3u106xmTWmmd71tgtACYD_63RqjCLPHSYxVcPxgHj6jvu5ikFuuKsA7FxifCKYWCkMBjCI8Kxiq7bf_mkv0YV_xAAwfAHk1G1izL0HiEkaV4Gbb2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هواپیمای مخوف جنگ الکترونیک EA-37B کامپاس کال ، در حال کم کردن ارتفاع برای فرود در پایگاه آمریکا در جزیره خانیا یونان میباشد ، از این هوا پیما فقط ۵ دستگاه تا کنون تولید شده
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/21160" target="_blank">📅 16:21 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21159">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/77ba9d3c18.mp4?token=u86ymZr83KvzDodjJA8ft52HjqaiDgirIlG54-vErWMSY10UU74nBbIaYNrSVqttpgsjleXLcws_3HPylI__N7kE3FwMaOL5xAdSM6hH0qK2Px9pT6Z2z5DF1QuXo1cei0KTP3uAJ4WfSXG4zaTPIwCk2xz3szvp84p5m4RX8Xwa_3VOWHnOcph8Re3XNwpOCv_wKjE2Ixvpy2x8Dxr-iaAtJsioc1Y6z1iZfH13hY0XYTzXEM4BWjoK5caC0FZpEDk9yjFLFM0pt1RpHGVcAZ8bVd2FKIydAkJJ1-HaGeIRe3gyWBFXaRytJhrowcFITNUXC-MYw3Z2PKU8PqzvKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/77ba9d3c18.mp4?token=u86ymZr83KvzDodjJA8ft52HjqaiDgirIlG54-vErWMSY10UU74nBbIaYNrSVqttpgsjleXLcws_3HPylI__N7kE3FwMaOL5xAdSM6hH0qK2Px9pT6Z2z5DF1QuXo1cei0KTP3uAJ4WfSXG4zaTPIwCk2xz3szvp84p5m4RX8Xwa_3VOWHnOcph8Re3XNwpOCv_wKjE2Ixvpy2x8Dxr-iaAtJsioc1Y6z1iZfH13hY0XYTzXEM4BWjoK5caC0FZpEDk9yjFLFM0pt1RpHGVcAZ8bVd2FKIydAkJJ1-HaGeIRe3gyWBFXaRytJhrowcFITNUXC-MYw3Z2PKU8PqzvKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دارلین گراهام در مورد اسرائیل:
من با نتانیاهو و همسرش ملاقات کرده ام. آنها برای تشییع جنازه لیندزی در شهر بودند.
من یک چیز را به او اطمینان دادم که در کنار اسرائیل نیز خواهم بود
@WarRoom</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/21159" target="_blank">📅 15:32 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21158">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UQo7jtRuAEqKDIn5xEeRUWJMsDx3NDfktYBuMbgGMrBagQLIrK8l3V1OcGmpKTbKn16ua5je3vmrouh0g1iMz8VxsF45lZyPhl8qPHZQjVmQd6BmngGArDE5jxCK1zeXkPwvb9odRnpNxXmP4u3uV1xdUZtQC41gMrfWgY8-1_WmVtrTILbq9QdnNSih1nx1H3rX84eygvQrvRp7-ocwf1di3TdKHl1-DswQGVtAGDieYSeuYFsme1_33J65o6Ago9LtoEwsD79CWrcAJAwSXd7kNZQljIWymP2sSF6_yDOP0jIhyWjpCtQVCSm4qM6YaQg8Uosj-UWwJhpJclqkCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ :
منطقه جدید متعلق به آمریکا, تنگه هرمز
@WarRoom</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/21158" target="_blank">📅 15:04 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21157">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">سخنگوی وزارت امور خارجه قطر: ما نمی‌دانیم چه انگیزه‌ای باعث شده است که ايران پس از گذشت 6 ماه، موضوع خلبان‌ها را مطرح کند.
@WarRoom</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/21157" target="_blank">📅 14:38 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21156">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">رئیس اتاق مشترک ایران و عراق :
ایران حدود ۱۲ میلیارد دلار از عراق طلبکار است
@WarRoom</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/21156" target="_blank">📅 14:36 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21155">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/21155" target="_blank">📅 14:03 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21153">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lhO6RkIARHG8b95rfK3j7jYJFczkWaOMqMQkbGEqinmI6_ads9WKnT9CnuQo887OA1QYIQpbd0ZfyP-Kj4jCvGxnAngGyffyTsfJUBwzSkCdy0x93kdQZR0vt1c-48xoklvhj38E_RrjQyGLFK4Ky45tLjIi1wk6Z7L5aZuWr3dNljtQIFBaUBjdpRZekQGZ4Lk-nx-OfvcelI60Ou_-5QAvO5yGc8tv6Ip_P0D_xpqMoAxR87yZWdDvHnXkJ4s3NDBH93B2FSRiKpLgxNf2skf5FoSfrquvaAWX65a1qQn94mUCHlyuibkCdZpHeb1px-1oOHvg1MbRo5PaKnTGhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iZikWwkT2iGinF918Mf7lmKXywWfetfwYMgsa78tjHRQcSN1KUIgM6eg7K-TNmaHn_NYxMCVIY6Jc4dO8uu2rDnRVgLqJmAiQM-Wgbh_1Ertyb498Bmg80qlM1MMnJRhZPbHRVOETXns63yZ6EGWJAdmbTASArz_TOzv3RfbvGpnQf2ho5pROA2qS1yqZytefF9aYMOa7hcC2W_nF2qUjA3redr6fojdrQ8UUl75ZRyO8MVYAp8AtQUxxLajXVzN3f_xhLGEj3RErPz2g9C_hUHcLRx0Fa8-Oecc-SYw_TUa1CGiIOU2yHjUxSh92Bi2fxddwZ8xThmLBYO_txsuqg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">حقیقت یاب رپفا : عکس امیر تتلو در زندان که رسانه های سود جو بدون دقت پخش کردن  جعلی است! با  حتی کمی دقت فتوشاپ و کات ضعیف دست راست امیر و همچنین بی کیفیت کردن عکس برای پوشاندن خطا های سازنده آماتور آن مشخص است ، عکس اصلی رو هم قرار دادم که ببینید فرم دست ها هم یکسان است
@WarRoom
@RapFA
✅️</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/21153" target="_blank">📅 13:57 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21152">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">ان بی سی : روسیه از طریق دریای خزر قطعات پهپاد، مهمات و تی‌ان‌تی را برای کمک به بازسازی ذخایر ایران که در حملات آمریکا و اسرائیل آسیب دیده‌اند، به ایران ارسال می‌کند. مسیر خزر عملاً غیرقابل مسدود کردن است. نیروی دریایی کشورهای غربی بر اساس کنوانسیون سال ۲۰۱۸ دسترسی قانونی به این منطقه ندارند و کشتی‌ها نیز مرتب سامانه‌های ردیابی خود را خاموش می‌کنند
@WarRoom</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/21152" target="_blank">📅 13:39 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21151">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">رسانه های رژیم :  اسم فرودگاه مهرآباد به فرودگاه آیت الله خامنه‌ای تغییر خواهد کرد
@WarRoom</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/21151" target="_blank">📅 13:26 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21150">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">رویترز
:
دو شرکت بزرگ حمل و نقل چینی، ارسال نفتکش‌ها را از طریق تنگه‌های هرمز و باب‌المندب متوقف کردند.
@WarRoom</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/21150" target="_blank">📅 12:00 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21149">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">بوشهری های عزیز خنثی‌سازی هست اعلام شده
@WarRoom</div>
<div class="tg-footer">👁️ 131K · <a href="https://t.me/withyashar/21149" target="_blank">📅 11:27 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21148">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">بلومبرگ : با اعلام عدم تمایل دونالد ترامپ، رئیس جمهور آمریکا به تمدید توافق رو به پایان با ایران و تشدید تنش‌ها در تنگه هرمز، چشم‌انداز صلح در خاورمیانه با رکود تازه‌ای مواجه شد.
@WarRoom</div>
<div class="tg-footer">👁️ 131K · <a href="https://t.me/withyashar/21148" target="_blank">📅 10:23 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21147">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">العربیه : منابع ارشد کورد عراقی می‌گویند نیچروان بارزانی، رئیس اقلیم کردستان، طی دو ماه گذشته دو بار در بغداد با اسماعیل قاآنی، فرمانده نیروی قدس سپاه پاسداران، دیدار کرده و در چارچوب میانجی‌گری محرمانه میان آمریکا و ایران، پیام‌هایی را رد و بدل کرده است.
@WarRoom</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/21147" target="_blank">📅 10:21 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21146">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">عراقچی ، وزیر امور خارجه: اسرائیل تمام تلاش خود را برای جلوگیری از دستیابی به توافق‌نامه و عدم اجرای آن به کار بست و این تلاش‌ها همچنان ادامه دارد.
@WarRoom</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/21146" target="_blank">📅 10:16 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21145">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pcVPtCbdVYipmdE5efUus9x0kjtX3zYYr2D-uz4KNGjI2HSUplW7PyLP4rsPM-xxAehs0-s_MuajL9veeQ_oA7WRhMR3WTez9iMVq3j2AbQb_-aTZoR-RVdNNhSHMwVshyCZu2X3XKduwmcsiVmUh3iu3YQ19C0Lmftt6wIVu_sTmQif0SAcPc7-w9W8LUIr0pj9RlRBQWgshZbfTQ832i2xabPT2Ta3wK9gj15mk5STFJWguTgf0D048jl2DjktcEJBbq-TgrPjs5EUo_GbCqyJesPo9TrD_z5rSs8L61IAE4GyHvfLl8dmhtAJYCI0L3-jpPkYBKAWzy2wv1TQmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به گزارش UKMTO یک کشتی هنگام عبور از تنگه هرمز به سمت بیرون، توسط یک موشک/پهپاد مورد اصابت قرار گرفت.
برخورد باعث آسیب به موتورخانه و زخمی شدن یک عضو خدمه شد، در حالی که سایر اعضای خدمه توسط گارد ساحلی عمان کمک رسانی می‌شوند.
تاکنون هیچ تأثیر زیست‌محیطی گزارش نشده است.
@WarRoom</div>
<div class="tg-footer">👁️ 132K · <a href="https://t.me/withyashar/21145" target="_blank">📅 09:19 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21144">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">مایک جانسون، رئیس جمهوری‌خواه مجلس نمایندگان آمریکا امروز در گفت‌وگو با خبرنگاران گفت جنگ با جمهوری اسلامی یکی از عوامل افزایش قیمت بنزین بوده است، اما مردم قدردان این موضوع هستند که آمریکا با برخورداری از «بزرگ‌ترین نیروی نظامی» در تاریخ جهان، توانست
«سر مار را قطع کند.»
@WarRoom</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/21144" target="_blank">📅 04:47 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21142">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/withyashar/21142" target="_blank">📅 03:34 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21141">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I2cu_bVURXoyPdsgGPvNKR56JLTG4vXNPnGDKSo1QpO9HiYmZRqMaSb3WGHomNy5DoYcHKO3ZPb2gI6NMCpNQ7sujrjEAO151TPNUzCP9nwc2gtUbdrpWFJCovuNETGScLPy3jTZ-T9aE9cz2A6dchsOCmDol3TjtlqdMrRzBdgHgTJFo-RY0w8iMJy5bgxbJYP6iuRuP5o5wyfdo_ircNOUwDwBMgJqXAXlbpf6ve--vM_rtnQzPqPCGrWkyD5BoPXGPrMPHVF2_L3TbLeeNj2lP5QSVDUz2FqgRCLC2Jgk8f_6oLXlxjXFLv-8wBSoqRbH_yTj9yW5TEdp_cH7fA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@WarRoom
🕰️</div>
<div class="tg-footer">👁️ 133K · <a href="https://t.me/withyashar/21141" target="_blank">📅 02:52 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21140">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/withyashar/21140" target="_blank">📅 02:47 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21139">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromali</strong></div>
<div class="tg-text">اقا یاشار خسته شدیم بخدا بگو کی میزنن</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/21139" target="_blank">📅 02:46 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21138">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">العربیه: ممباقر قالیباف، رئیس مجلس ایران چهارشنبه آینده به بغداد سفر خواهد کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 132K · <a href="https://t.me/withyashar/21138" target="_blank">📅 01:51 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21137">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">دفتر ریاست جمهوری ترکیه: اردوغان در تماس تلفنی با ترامپ بر اهمیت ادامه گفت‌وگوها با ایران ابراز داشت و بر آمادگی ترکیه برای مشارکت تأکید کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 134K · <a href="https://t.me/withyashar/21137" target="_blank">📅 01:12 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21136">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">آتش‌سوزی میدان شهرداری گرگان
این حادثه ساعت ۱۹:۱۵ دقیقۀ شامگاه دوشنبه رخ داد که بالغ بر ۲۰ باب مغازه در این حادثه آسیب دیده و دچار آتش‌سوزی شدند.
@WarRoom</div>
<div class="tg-footer">👁️ 134K · <a href="https://t.me/withyashar/21136" target="_blank">📅 00:52 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21135">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">چند گزارش تایید نشده از پرواز یک اسکادران جنگنده از سمت مازندران به تهران مشابه با زمان جنگ @WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 135K · <a href="https://t.me/withyashar/21135" target="_blank">📅 00:48 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21134">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">چند گزارش تایید نشده از پرواز یک اسکادران جنگنده از سمت مازندران به تهران مشابه با زمان جنگ
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 136K · <a href="https://t.me/withyashar/21134" target="_blank">📅 00:37 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21133">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HCtn2AFUI2xnETx1mBwYuMK2-bYp1xwkZs4eSb0yabJwsUye5_6ZFeu0yBNa0ku4kPx3X5fUMJEolj7EE22b1GVz7FxBcQSTpopPdjFHKWdsbITpCgx0GvJhmlDdlq_G0qCKUoZk5OULRDv5KE1m7RM19i0AZVqOWaoUOkeMHlJhjB7bcbW9wu28sExNXjdt7_pgQz_jF6p3wGQG9CXlUaluMlAzIOGwaCHFWfh8l3C0SNCEt4vKN8-CqoaMmaQd34lsLiPMvQtImsDy-tihRrr7rxidqmYnwgzR9GyeRzTl6qYNvYb0H7qjUvDjlAxIsKeBmavbEVSb69n_MOxg-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در‌تروث شوخی با رهبر کره شمالی:
کیم : هی دونالد، با هم اوکی‌ایم… مگه نه؟
@WarRoom</div>
<div class="tg-footer">👁️ 136K · <a href="https://t.me/withyashar/21133" target="_blank">📅 00:32 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21132">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">مدیرعامل مخابرات : سرعت اینترنت بزودی با مهاجرت از کابل مسی به فیبر نوری تا 8 برابر زیاد میشه!
@WarRoom</div>
<div class="tg-footer">👁️ 135K · <a href="https://t.me/withyashar/21132" target="_blank">📅 00:01 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21131">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">اکسیوس به نقل از یک مسئول آمریکایی: کوشنر به نتانیاهو اطلاع داده است که واشنگتن می‌خواهد اسرائیل اقداماتی کوچک در غزه انجام دهد تا جدیت حماس را بسنجد.
@WarRoom</div>
<div class="tg-footer">👁️ 137K · <a href="https://t.me/withyashar/21131" target="_blank">📅 22:52 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21130">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">کوشنر به فاکس‌نیوز: اگر ایران حاضر باشد توافقی را که تاکنون با ما درباره آن مذاکره کرده‌ایم نهایی کند و توانایی ساخت سلاح‌های هسته‌ای را کنار بگذارد، طبیعتاً ترامپ هم آماده توافق است. اما در حال حاضر، ایران هیچ نشانه‌ای از تمایل به انجام کاری که از نظر ما منطقی باشد، نشان نمی‌دهد.
@WarRoom</div>
<div class="tg-footer">👁️ 136K · <a href="https://t.me/withyashar/21130" target="_blank">📅 22:51 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21129">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">کوشنر به فاکس نیوز: اسرائیل نگرانی‌های موجهی را ایجاد کرده بود که ما توانستیم به آنها رسیدگی کنیم و برخی از ابهامات مربوط به طرح را برطرف کنیم.
@WarRoom</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/21129" target="_blank">📅 22:19 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21128">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">کان نیوز اسرائیل : احتمال شروع مجدد جنگ بسیار بالاست
@WarRoom
🚨</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/21128" target="_blank">📅 22:05 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21127">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf2bdcb1f8.mp4?token=cttleMFx1fK-ST5dhU-v72zigJV1Cp3UHJGxfJ7biMwwHwwrVQ7C4pQ-Sf-RTJdaTX6_Ac1sVkPLIKwTGyff6PyKKMeATQ338AI9vH_PHAat7cNpZ56rIBGGBAkn3UVAJ48toV93hzqofP4VsuqzNmn5DH8IFPUQHoKfNXG6PrUMQYWSGHRDjdtL2LLwnEudKi8CWTEtyyfYbWz1xlWK1B1JHEmGEqf8-gkXtOtv1SNRr3WW4HPanUiYo52UrHTZBdErN-cq6SDXN_jKG2k1VWMsYtnd3CzRFYD40ljJBRX6g_zjYsPhf0ZXTw3zxYjoJFeq6M3VsloRhTeA5PD0hA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf2bdcb1f8.mp4?token=cttleMFx1fK-ST5dhU-v72zigJV1Cp3UHJGxfJ7biMwwHwwrVQ7C4pQ-Sf-RTJdaTX6_Ac1sVkPLIKwTGyff6PyKKMeATQ338AI9vH_PHAat7cNpZ56rIBGGBAkn3UVAJ48toV93hzqofP4VsuqzNmn5DH8IFPUQHoKfNXG6PrUMQYWSGHRDjdtL2LLwnEudKi8CWTEtyyfYbWz1xlWK1B1JHEmGEqf8-gkXtOtv1SNRr3WW4HPanUiYo52UrHTZBdErN-cq6SDXN_jKG2k1VWMsYtnd3CzRFYD40ljJBRX6g_zjYsPhf0ZXTw3zxYjoJFeq6M3VsloRhTeA5PD0hA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ : ایالات متحده به دنبال تمدید تفاهم‌نامه با ایران نیست
ایران در دردسر بزرگی افتاده است. کشورشان آشفته است.
ارتش آنها کاملاً شکست خورده است.
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/21127" target="_blank">📅 21:57 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21126">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">ترامپ در مورد ایران:
من ایده اعلام تنگه هرمز به عنوان قلمرو ایالات متحده را دوست دارم.
ما کنترل کامل بر تنگه داریم.
ما در حال خارج کردن میلیون‌ها بشکه نفت در هفته هستیم - شاید این متوقف شود، یا شاید حتی بیشتر باز شود.
تنگه باز است و قیمت نفت در حال کاهش است و این روند همچنان ادامه خواهد داشت مگر اینکه تصمیم بگیریم کاری بسیار شدیدتر از آنچه انجام می‌دهیم انجام دهیم.
@WarRoom</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/21126" target="_blank">📅 21:54 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21125">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa62990739.mp4?token=RjGsk8q5n0aykox8nFeaPJbxlKPxSM5JD40N4jR1nm3IScSngAAt7cbTTjjGu-qZdqvXlXYQAJ7d_mQWWURSURk5G56qB4Z0Dk_OMoRgQfYYMatUjdjubuhPvnpTAdFG-3o7AByD3IupJzXQlJLsDdx73RVIYXVlIWBJZqMiJN662Wp8wzn63eUPQCgwB8CYzU8-llIQXBm08rellwhUzHmle1gAPIsPCEMQRzoX4pRL91yVGtwuzSTs8-7c-YQPaBgvA4Pz5FX09a8iHwBuF5f2EpxTbv3X-nl2mw4cxvZEgVNdSE47ifSbzeb5RkUD-XxlQQBExPPYTIybgrJsJYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa62990739.mp4?token=RjGsk8q5n0aykox8nFeaPJbxlKPxSM5JD40N4jR1nm3IScSngAAt7cbTTjjGu-qZdqvXlXYQAJ7d_mQWWURSURk5G56qB4Z0Dk_OMoRgQfYYMatUjdjubuhPvnpTAdFG-3o7AByD3IupJzXQlJLsDdx73RVIYXVlIWBJZqMiJN662Wp8wzn63eUPQCgwB8CYzU8-llIQXBm08rellwhUzHmle1gAPIsPCEMQRzoX4pRL91yVGtwuzSTs8-7c-YQPaBgvA4Pz5FX09a8iHwBuF5f2EpxTbv3X-nl2mw4cxvZEgVNdSE47ifSbzeb5RkUD-XxlQQBExPPYTIybgrJsJYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار: آیا غذای کافی در ناو یو اس اس لینکلن وجود دارد؟
ترامپ: وجود دارد. آن یک گزارش جعلی سی ان ان بود.
در طول این سال‌ها، ما آنها را خیلی بیشتر آنجا نگه داشته‌ایم.
یک دریاسالار به من گفت: «من خیلی بیشتر از این روی کشتی‌ها بوده‌ام، قربان.» و افراد حاضر در ناو لینکلن می‌گویند که به خوبی از آن مراقبت می‌شود.
@WarRoom</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/21125" target="_blank">📅 21:46 · 26 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
