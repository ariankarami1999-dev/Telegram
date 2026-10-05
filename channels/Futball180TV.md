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
<img src="https://cdn5.telesco.pe/file/GQGCdiZ2bZEoy6VL64pwvv3z5mhHDoYb87pC8Uh0NL1-_qY3F7yv_mTe4VM7BCRkn4VdZxly7ISchRKtj8u_4t5uZWN10rJq1q1Pt0qVFD-ZpJFHLy6-ZK4nsJ98gQh0oqQgAF0F8CK2QCC5BTucryJ2wKVKm0caDZ4c917yVj1SA4NZ4b-p6RgRObTf5eQeGABfDDcP8zvE_IMWP-QXMY68gSSuDw03ZMUc-7z7fExPGXAz7MKNnVjPZbZx2FVTQNqcdRCeSqun0NRNB9uqDQZ3t8jqLlwGFZ3lTMZNZzgk07c0yvsvoniyv7UlD8rQiZTleTIVt_SBPWmD_PExmg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فوتبال 180</h1>
<p>@Futball180TV • 👥 391K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-13 22:09:04</div>
<hr>

<div class="tg-post" id="msg-107879">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1743ee1f5a.mp4?token=O2E3tnn701r5kInk7SA7OBrPBdBaoFnSeJHMa5dYsJ2IV1aGxpQK8zJiOgLYNbl9WCHLFzqQ0j8q6gvM8OYgf149wz6MSOtuW_saSRLBPeUTqYgIVla8okrRK2fYMUNipGDIumvYbV1nGzYlDvU_wCgtY2TyujYks5vR6cTk3-g5bhETdjdHWg5yEkLRcXT4BSerH1mYWktjS2sNkW6n4kwdGOn7SoLz-CvCWfdLLJ_EQNrFvYBSf2CUgHZDx8nKo-IlK0eRwd42fnauGtcAwvG9JdGem1b4MnYFPsQNiNQVaVI_8-iq6LOv4xyhb0UEShZJjU-yRfjaKhUJ8-hmkFUmAhOS9FPUVaFTnxMKOJu28gI_yHtoVlHS-lf35S8uel_0Eo6-YknEZUlv5HbRIHvbIVtHDbaC9fwpW20-q7flCG99qNQqC9HNTNnoaGApBAGjePzScijyWutMxTjJN2geXhupv_8S8swStnLzx3CK1Hvr85IgKhlhR54UluBCgyZdULoB79vNsP_HXGeGoG0EmOqGVg-dTkgKvplcfoaSFYOELwnUyWI1ZCahDNF1O1BfgzUzWdAjM8bP2EAogfNEZDDXUhaMTwcwgP2h0pFQurXZg77_J0cGOOVfBylXBxL8GhJtUUgKj-NdbVzfMpMmE_zENOzqHh0ZxLXXprU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1743ee1f5a.mp4?token=O2E3tnn701r5kInk7SA7OBrPBdBaoFnSeJHMa5dYsJ2IV1aGxpQK8zJiOgLYNbl9WCHLFzqQ0j8q6gvM8OYgf149wz6MSOtuW_saSRLBPeUTqYgIVla8okrRK2fYMUNipGDIumvYbV1nGzYlDvU_wCgtY2TyujYks5vR6cTk3-g5bhETdjdHWg5yEkLRcXT4BSerH1mYWktjS2sNkW6n4kwdGOn7SoLz-CvCWfdLLJ_EQNrFvYBSf2CUgHZDx8nKo-IlK0eRwd42fnauGtcAwvG9JdGem1b4MnYFPsQNiNQVaVI_8-iq6LOv4xyhb0UEShZJjU-yRfjaKhUJ8-hmkFUmAhOS9FPUVaFTnxMKOJu28gI_yHtoVlHS-lf35S8uel_0Eo6-YknEZUlv5HbRIHvbIVtHDbaC9fwpW20-q7flCG99qNQqC9HNTNnoaGApBAGjePzScijyWutMxTjJN2geXhupv_8S8swStnLzx3CK1Hvr85IgKhlhR54UluBCgyZdULoB79vNsP_HXGeGoG0EmOqGVg-dTkgKvplcfoaSFYOELwnUyWI1ZCahDNF1O1BfgzUzWdAjM8bP2EAogfNEZDDXUhaMTwcwgP2h0pFQurXZg77_J0cGOOVfBylXBxL8GhJtUUgKj-NdbVzfMpMmE_zENOzqHh0ZxLXXprU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚽️
کلید واژه‌های تکراری قلعه‌نویی؛
همه مقصرند جز ژنرال!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/Futball180TV/107879" target="_blank">📅 21:59 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107878">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🚨
‼️
💵
عادل فردوسی‌پور: دیگر حوصله شوخی‌کردن با قیمت دلار را هم نداریم
روزگار سخت و تلخی که سپری می‌کنیم/ شروع فصل لیگ برتر، با دلار ۱۸۷ هزار تومانی، بازگشتش از فیفادی، با دلار ۲۷۰ هزار تومانی!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.55K · <a href="https://t.me/Futball180TV/107878" target="_blank">📅 21:23 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107877">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc2122fb81.mp4?token=p4-FFx9fVmqKCzR1jrtHNX2RDsaHyXIA5RROlHip97Hr3qJ5IFew65wDCt0qoAU2lfwl46RdF_O3kAj1_ZsiwsxdRpe499eZEvbR4Xl0x8XODp57TMMbV1NpRqL-dwHrdWDE7Zde3Cl5K8wrdOLkyeTJE_s3EQvnsLlxnXaHyDab6iU6kMneoZKjNg7yGpH-543QS7t-0sg5oDqD_HzcRwmgc4OPrigJ3TgwFwJFm4IAcpUFLNQrldPdiMRj04mzg2IEBDkGTm2boSFlP2CIc61Rr-c3-CUrck1fb-V7qJsnUkcH-UvEIEQjhfHa2QOwVFtDxlM8WGMN_QOy-i694gUyJWgBEtSNqmO1_Ur9BrUMjAwp9U0tidEt_8IzyrcONhm8wUkWgYZALTGCS34Rj_NXjGZlVpwg6C-cIX0NDq8pDoQk9lD97ECf4Lec-7ygeTPMsCODRIHA32_bKD_Aa9VtjzVx7aixxK1V9YOHt-XT3_DTVDGTooAbgDKs3A1SGI_gOG7KoLqeXeOhqGhGNEKemrotkabKDlN76CBigMwcFXZooEwCjUZmSNZPpg9wRXZ9GnHeburDsNR-GLbhxXc9-JSRYP2T9eUwxaSMEZVmXaku3xu88-jHGBHqMaWDSTtlKSnmWIRBN1w7UBgoZMViUXXnIkRbso4bEt1vHiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc2122fb81.mp4?token=p4-FFx9fVmqKCzR1jrtHNX2RDsaHyXIA5RROlHip97Hr3qJ5IFew65wDCt0qoAU2lfwl46RdF_O3kAj1_ZsiwsxdRpe499eZEvbR4Xl0x8XODp57TMMbV1NpRqL-dwHrdWDE7Zde3Cl5K8wrdOLkyeTJE_s3EQvnsLlxnXaHyDab6iU6kMneoZKjNg7yGpH-543QS7t-0sg5oDqD_HzcRwmgc4OPrigJ3TgwFwJFm4IAcpUFLNQrldPdiMRj04mzg2IEBDkGTm2boSFlP2CIc61Rr-c3-CUrck1fb-V7qJsnUkcH-UvEIEQjhfHa2QOwVFtDxlM8WGMN_QOy-i694gUyJWgBEtSNqmO1_Ur9BrUMjAwp9U0tidEt_8IzyrcONhm8wUkWgYZALTGCS34Rj_NXjGZlVpwg6C-cIX0NDq8pDoQk9lD97ECf4Lec-7ygeTPMsCODRIHA32_bKD_Aa9VtjzVx7aixxK1V9YOHt-XT3_DTVDGTooAbgDKs3A1SGI_gOG7KoLqeXeOhqGhGNEKemrotkabKDlN76CBigMwcFXZooEwCjUZmSNZPpg9wRXZ9GnHeburDsNR-GLbhxXc9-JSRYP2T9eUwxaSMEZVmXaku3xu88-jHGBHqMaWDSTtlKSnmWIRBN1w7UBgoZMViUXXnIkRbso4bEt1vHiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
تصویر تکراری تیم ملی
بازنده اما طلبکار و با اعتماد به نفس!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.57K · <a href="https://t.me/Futball180TV/107877" target="_blank">📅 21:22 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107876">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QFGbATYHCo-_k-JoTzkc-F9ZtG0wjyvcOiPR5X9gFv_wqcZDbqMeDFAzKvlr6wFALT73Y79fGk7BemrQtjhfCs2KL0yM9pCfBTtdN_UvqrpFiVtYwlLqMJ6ZY_2z6WSakxzQOIBRZjekVphteOVuhL4bw8vlYeJzcwzW8mPIBBz0-zMwTqmauL8Q14eMAiZRsMC6ilwBZqgt9kWigWpo2fUILF-Bpx8HX_x8ZcyI3Ewpk3B_xkuzxGpmw7-oiXEJj-DIQAxhXpXA6eFb0m_9CEnfjxthsJwOP2JhuO5Ry86HtLBP70UYGlrHHKw3fCBISZljEFADvJ-jF6fi84yMRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✔️
🇫🇷
ترکیب تیم‌ملی فرانسه مقابل بلژیک
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.73K · <a href="https://t.me/Futball180TV/107876" target="_blank">📅 20:41 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107875">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/71f2c09e35.mp4?token=Ewi7vtPdVU23cNtEPIYv-mdKzjKxlRkFsbtTmkZNpRUwtvmXEBxW2kOmRs99PbR4jNpwBq3vZExbOZRckhRSZlsRAfvnEaWVPsBT0nKkQz4I_X06Zl6QZU3dh5hhXML8Z8I4aaEP8k7kbYtctGk7IwpP9zjTcXZLtClKmj7BOC6VjeKpLJQFOS5WxVzuCCfzBnxIpVYjUP3ijrKtOrZ_VHGN9Ka3rzgsTSKZpBEa6OLRYVkWOnXe5xyLNAZ-DZ38RBt_5FLH2a51pMd8d6ej3SdGevxmFv-cgmHytxttqVFHTMu2YJl3F2AXxPioAbxV97ksoHy0SMEw0MIGLwl1pUEWLDd6VTC_b_7qlA91FySbVmL4U_q29J-tUOCw0xx1bmLnWdVSdriZEkANDhsz2xGPUf_GomtAZaruuliIOTsZoGjdw_a_jf3rhv7OIHrZ1m2tjdLOraMf2eNihANN2id5bg2vYG-FEyvcdhN3lAYaFvc6EcRf8wUSQm1VbCFYSXwfKnAlVY12OyeL3wZcSW3c5mHCdepXzvU5c4djEskqHaIX8XwqHjZsNh0Re9QBjtp-mg3eqewchs5A1RgaR2a7nE8BRfuzF5A-urHiCzZ6I4dCDIqIHInubMWEbRDK7JtSQXolb_cC9FewCb9K3fp1Qh4fdjx9Lcw_bOKxQHY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/71f2c09e35.mp4?token=Ewi7vtPdVU23cNtEPIYv-mdKzjKxlRkFsbtTmkZNpRUwtvmXEBxW2kOmRs99PbR4jNpwBq3vZExbOZRckhRSZlsRAfvnEaWVPsBT0nKkQz4I_X06Zl6QZU3dh5hhXML8Z8I4aaEP8k7kbYtctGk7IwpP9zjTcXZLtClKmj7BOC6VjeKpLJQFOS5WxVzuCCfzBnxIpVYjUP3ijrKtOrZ_VHGN9Ka3rzgsTSKZpBEa6OLRYVkWOnXe5xyLNAZ-DZ38RBt_5FLH2a51pMd8d6ej3SdGevxmFv-cgmHytxttqVFHTMu2YJl3F2AXxPioAbxV97ksoHy0SMEw0MIGLwl1pUEWLDd6VTC_b_7qlA91FySbVmL4U_q29J-tUOCw0xx1bmLnWdVSdriZEkANDhsz2xGPUf_GomtAZaruuliIOTsZoGjdw_a_jf3rhv7OIHrZ1m2tjdLOraMf2eNihANN2id5bg2vYG-FEyvcdhN3lAYaFvc6EcRf8wUSQm1VbCFYSXwfKnAlVY12OyeL3wZcSW3c5mHCdepXzvU5c4djEskqHaIX8XwqHjZsNh0Re9QBjtp-mg3eqewchs5A1RgaR2a7nE8BRfuzF5A-urHiCzZ6I4dCDIqIHInubMWEbRDK7JtSQXolb_cC9FewCb9K3fp1Qh4fdjx9Lcw_bOKxQHY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
▶️
بررسی ۵ نکته مهم در جدیدترین نسل‌آیفون
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.8K · <a href="https://t.me/Futball180TV/107875" target="_blank">📅 20:01 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107874">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dce1470830.mp4?token=d4siQusuQYbSkYkAbrr3i6lKEOx_J3f7KloYjJaYc49WR3Mclm4CIwBBDU2bbS2Rf_-uPwYpT83exbhpwSj7dlbxQdI24oLANqm_RIz5cu5cpyhOQYpm5xLMcL9iDF8GNVDSYGFhK_9OLIfyVgceX8n2hrV4X1PdVuT6L5miKGYXHZfI3fUr7vW4B_ZFmjRB_jJYFhAJ0xJPrVS52wjjfBSDd_WTDb6OqFHR6rT7XVmtpGLg1LKKIkVOTCGTHHCLrczaOMQihgiIHeJ7Wbvkbh5q8dgo_g-OyQspzC4GXx9hVxhT5BQQSW4nwhNov1LWbOOGgtErVo5uPRwSkewwMSKC7MrdttHiDQB7boi42ydJLHVgfE7m2eFQaQlmFTiKZOT-_7jaV_8OqJFvIeYR9gN4tAQicw7B_YBxlp3zu0qY1oJoFThAGOP9o0aiI4TLVKbxL-VadesvfjN72z8VPpIrkFmdH4eVoi9Wwpop0s6B916219QwtLiB_DnkFilmGYmRw1SGC84n6vU3oOil31qH6bS_uyxuzx-_jLs98FP9rPAdvwn1KL_A8JvjptVfOR3DueyPMFRVjW8oVJ-ylBIwsgAvBNIBrhRSuxEwCEQj2Brl9Rwvl7vmDo4lLMEtEL4w2-szoq2d2NoysglxWasenFKNY9NmzAOB7WWAi2E" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dce1470830.mp4?token=d4siQusuQYbSkYkAbrr3i6lKEOx_J3f7KloYjJaYc49WR3Mclm4CIwBBDU2bbS2Rf_-uPwYpT83exbhpwSj7dlbxQdI24oLANqm_RIz5cu5cpyhOQYpm5xLMcL9iDF8GNVDSYGFhK_9OLIfyVgceX8n2hrV4X1PdVuT6L5miKGYXHZfI3fUr7vW4B_ZFmjRB_jJYFhAJ0xJPrVS52wjjfBSDd_WTDb6OqFHR6rT7XVmtpGLg1LKKIkVOTCGTHHCLrczaOMQihgiIHeJ7Wbvkbh5q8dgo_g-OyQspzC4GXx9hVxhT5BQQSW4nwhNov1LWbOOGgtErVo5uPRwSkewwMSKC7MrdttHiDQB7boi42ydJLHVgfE7m2eFQaQlmFTiKZOT-_7jaV_8OqJFvIeYR9gN4tAQicw7B_YBxlp3zu0qY1oJoFThAGOP9o0aiI4TLVKbxL-VadesvfjN72z8VPpIrkFmdH4eVoi9Wwpop0s6B916219QwtLiB_DnkFilmGYmRw1SGC84n6vU3oOil31qH6bS_uyxuzx-_jLs98FP9rPAdvwn1KL_A8JvjptVfOR3DueyPMFRVjW8oVJ-ylBIwsgAvBNIBrhRSuxEwCEQj2Brl9Rwvl7vmDo4lLMEtEL4w2-szoq2d2NoysglxWasenFKNY9NmzAOB7WWAi2E" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
کنایه‌های ژوله به داستان سربازی دکتر بیرانوند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/Futball180TV/107874" target="_blank">📅 19:31 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107873">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8d2ddbc7f1.mp4?token=YL6SmoPT_gdrl-eNn-eV742zZ6-A2zipMyKrEiPvbGaEFVaRToUl58eaFB5DNcgTb1V5HiBCtSyTP4Q1qJwwA-7JQ7hYAhKbWVY4aWNLQcl-9n2rldjUGv_7jWlTGA-GqrlaESTtVl9QZPsz_3b3wFo_5e0YpeRPQoVGOjAYN2FBFBaPCxKPe4FKf0S3rsj9IWUhZ5H4Y6P38YEvn8Z-rp9ZQ7lX24I7TGv09sjI5efU1yNsi_Z7NbMhIOGfan4DFALUia8AYHy_kshp-rwRNFoCTuleE1rvCFB0LicfeO77Mo5SNFmoZmShpU6gea3cTCE1oJJIVwTwZqoAKniSTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8d2ddbc7f1.mp4?token=YL6SmoPT_gdrl-eNn-eV742zZ6-A2zipMyKrEiPvbGaEFVaRToUl58eaFB5DNcgTb1V5HiBCtSyTP4Q1qJwwA-7JQ7hYAhKbWVY4aWNLQcl-9n2rldjUGv_7jWlTGA-GqrlaESTtVl9QZPsz_3b3wFo_5e0YpeRPQoVGOjAYN2FBFBaPCxKPe4FKf0S3rsj9IWUhZ5H4Y6P38YEvn8Z-rp9ZQ7lX24I7TGv09sjI5efU1yNsi_Z7NbMhIOGfan4DFALUia8AYHy_kshp-rwRNFoCTuleE1rvCFB0LicfeO77Mo5SNFmoZmShpU6gea3cTCE1oJJIVwTwZqoAKniSTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ممکنه دفتر نُت موسیقی دیده باشید ولی ندونید چیه
این ویدیو کمک میکنه تا کشش زمانی نُت‌ها یا مدت زمانی که یک صدا یا نت ادامه می‌ یابد رو راحت متوجه شید
و به هر کدوم از این نت ها چنگ، دولاچنگ، سه‌لاچنگ و ... میگن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/Futball180TV/107873" target="_blank">📅 19:00 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107872">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd348ccf0b.mp4?token=WEq0wvdyMP1-e7PM6MvG30t_wQRHca5z-k4y8JwNONP1SvsBdr2TERP0YwplXpSu4FymoEYdrOJIIHgvNifhKveEz9Dk3nALd1KitcHiEbc3XCJ_Z1YHqNuUN8rOwyqFOYS1r0u2EnXOR4t7J9_KU9VzEy0CxYgTgaDWlNrbj_IBu-WWMEl4iV4epN8TU4AZBS34wrefCGtMrb8E4XktmX3EbW2DiGtb5ABVEKX4RrnqHnfAUQykld-gPQk2v_9FEILTNroGgcROThe-J3Am_IdvQVxHTtUBlYK7jETG37tmy4twruZw-eZPMqaNJAu8gDgHr33Bbp-xI8E8wBYYKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd348ccf0b.mp4?token=WEq0wvdyMP1-e7PM6MvG30t_wQRHca5z-k4y8JwNONP1SvsBdr2TERP0YwplXpSu4FymoEYdrOJIIHgvNifhKveEz9Dk3nALd1KitcHiEbc3XCJ_Z1YHqNuUN8rOwyqFOYS1r0u2EnXOR4t7J9_KU9VzEy0CxYgTgaDWlNrbj_IBu-WWMEl4iV4epN8TU4AZBS34wrefCGtMrb8E4XktmX3EbW2DiGtb5ABVEKX4RrnqHnfAUQykld-gPQk2v_9FEILTNroGgcROThe-J3Am_IdvQVxHTtUBlYK7jETG37tmy4twruZw-eZPMqaNJAu8gDgHr33Bbp-xI8E8wBYYKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
وضعیت پسران و دختران پس از نتایج کنکور:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/Futball180TV/107872" target="_blank">📅 18:30 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107871">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B38BX241Oz-6BJns7LSAEMW62d4S_WcGuzuxf8eXdLJIQfm2kJPQs5CSj7ApthJAatmGM9LaU-PbTnxcBicWzMW2rPwa_c08u6Dx19ksHWmOdBq59RmtZ3yWvATE0TcvBUvHe6hg6UYY9_32pHfQsEn4_Crg4vr3VFm_7Fu415Nve4hvdnesvgB3VMZYopjQG-DGPZlAz-gc3_dTCB843X55Zky-5GVLwFUlU3nYObmh3DlPpGFzB7Amhh5X0FeelJoh4bZ_DNk5l942N46kSD7CZtxk_mB3DbGAb86SlwdPoG6J4nN3i5E8NMChxAE_G1_3F1IOsFjgEUgIJE63tQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
فهرست نامزدهای جایزه گلدن بوی بعد از کاهش از ۱۰۰ به ۲۵ نامزد:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/Futball180TV/107871" target="_blank">📅 18:19 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107870">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6601bb6094.mp4?token=GAiI5zKVLWK5FfX_qeLU4gv0y766LE_pJI-LeAAP_tgQCB3uKWamMRs7qx-ez9vCCf4czE5LQ7Sxsu7QBJ_UG3HANQSM3j5NCbGHdWI_ZRIqJSJKplvQFcP46wThBU851Ae4iEAyyafx5QG1swfCOte2bzCaFTBQlVL1W8jouPLVfXLwT-tBFl5dK_fc9nQ3k8eAd1h3MaV5x3PD186kMMVktDHlDHMFdtCwyQOxTxYugLAmm_AGqwCwSvXfw7MnvAdMMtJ4lR-1VaL7ceefU3p351b_v2KxGzC3jgKnTiuZrAkg7FaLIXDriL8XEiyUw7liVfS4HySnxEaZxzCpQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6601bb6094.mp4?token=GAiI5zKVLWK5FfX_qeLU4gv0y766LE_pJI-LeAAP_tgQCB3uKWamMRs7qx-ez9vCCf4czE5LQ7Sxsu7QBJ_UG3HANQSM3j5NCbGHdWI_ZRIqJSJKplvQFcP46wThBU851Ae4iEAyyafx5QG1swfCOte2bzCaFTBQlVL1W8jouPLVfXLwT-tBFl5dK_fc9nQ3k8eAd1h3MaV5x3PD186kMMVktDHlDHMFdtCwyQOxTxYugLAmm_AGqwCwSvXfw7MnvAdMMtJ4lR-1VaL7ceefU3p351b_v2KxGzC3jgKnTiuZrAkg7FaLIXDriL8XEiyUw7liVfS4HySnxEaZxzCpQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
میگل آلبوکرکه، رئیس دولت منطقه‌ای مادیرا، زادگاه کریستیانو رونالدو:⁣ ۳۰ سال دیگه کسی یادش نمیاد کی سرمربی بوده، کی رئیس فدراسیون بوده یا کی کارشناس بازی‌های فوتبال بوده؛ اما همه می‌دونن رونالدو کیه.⁣ این تفاوت بزرگی و معمولی بودنه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/Futball180TV/107870" target="_blank">📅 18:12 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107869">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/107869" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 9.56K · <a href="https://t.me/Futball180TV/107869" target="_blank">📅 18:12 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107868">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MhkOob-Gfl3J-uxL1edo_smTU_-BfclnDyHvQEtWVGTYF_Vvx9x81AjrtunrA-JLI1Vqtf154082NsXBOhWtdIn8yY6_2Zlpo1jvFGFXVTWHeEn9VFJcrvDlfXDCytEUCRESl1PG0mUmUsuTn5VNATO5S9ru4CfDrWt0LDnHLDPSebCh0PgVLpxn112qI-hql5sC3Hd00hA5-6HO8BT5Jb3bv9upfBRx4HUtoh6bg9M7tpI5m67iPeNJj9ePOkdMfu0_IlvlvF9lxCVuCgK3HTmHxywuHGKPgmpCXs1KTYXbQBzWPYJiM3ugXRcBLsShEXwWtG4p9XCmWYEm6VzjVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤩
نبرد هیجان انگیز بلژیک
🆚
فرانسه را در
TrexBet
پیش بینی کنید!
📉
نگاهی به آمار ۵ بازی اخیر دو تیم:
بلژیک: ۳ برد، ۲ شکست و ۱۰ گل زده
فرانسه: ۲ برد، ۱ تساوی، ۲ شکست و ۷ گل زده
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 9.8K · <a href="https://t.me/Futball180TV/107868" target="_blank">📅 18:12 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107867">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hUloX3k-WGb-NkZUTKE7gz42Pqud-iRS3ge1tD4oC_WT4UaeqThOZtdYPjjlXnuOAj2bhDxlZaH_Agrz0m9A66UwhEk3LXMBd30sBupYJdlLd647wCVsq7V1lPjZjXLC18dR_CbWic7V5esdSOtHWqnytyyqe94YGGT2AzHOOzXE9ySX1E37eYpO-_-iH10iFppaFowLMN1V9yif8su1QlFOC978NQApAfZEZS1nuuR8-MChEepws3u0RGf8gwqSyE6LNq3XevRrORy9AUFN6VQ7cnRW6Qkh6Zk-jDe59tRjxareGxyUue_56DaWzLMT8Qoaamag44Ye_fnqgOyM5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🔥
گونزالو راموس در هر سه بازی اخیر خود با تیم ملی پرتغال که به عنوان بازیکن اصلی در آن حضور داشته، گلزنی کرده است.
🇵🇹
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.81K · <a href="https://t.me/Futball180TV/107867" target="_blank">📅 18:02 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107866">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c1c39a914.mp4?token=sseranLArIQVB4swkBMgC34SFsXToFIYleHiYiZRXZ9aXswQOY51qfFLzXRr9QtgXwwiq-tXCx-FnD-lWoa8BtZ-oY8GAHL16SAecO5HljXHbGDrtMxSUmaOallI9swps6BSfszh6DZ3pCVk9R_dt6Hty_eSW5jjI3S0NZKHgwQx8xlZprECfMq-x3QKxtzJIDmDn7-0vA8BCbn0er-goJomuK3ffVObX2NkmqB61bfHUPC6abVnoWxJGIobX-wVBCRDt_ik_PBlNeGvrEE2Q0d-uzMAZjt91hDkeYLkcNhMOt1TwqQ_Lh2cptAGv8ny50sVEvLRpyTnZDp4IwrA1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c1c39a914.mp4?token=sseranLArIQVB4swkBMgC34SFsXToFIYleHiYiZRXZ9aXswQOY51qfFLzXRr9QtgXwwiq-tXCx-FnD-lWoa8BtZ-oY8GAHL16SAecO5HljXHbGDrtMxSUmaOallI9swps6BSfszh6DZ3pCVk9R_dt6Hty_eSW5jjI3S0NZKHgwQx8xlZprECfMq-x3QKxtzJIDmDn7-0vA8BCbn0er-goJomuK3ffVObX2NkmqB61bfHUPC6abVnoWxJGIobX-wVBCRDt_ik_PBlNeGvrEE2Q0d-uzMAZjt91hDkeYLkcNhMOt1TwqQ_Lh2cptAGv8ny50sVEvLRpyTnZDp4IwrA1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤡
آخرشم نفهمیدیم بارسا چجوری تونست 8 تا بخوره.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/Futball180TV/107866" target="_blank">📅 17:20 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107865">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kI27Bbfeamg6YyRaYRuQgGtEK_DBTGp519vFvo6UGsdKcq8iUcigR3ShtREQgO0rpfJQI-lT3OtMQ7-JNdv0essbtslBg2pjmEO0LCwPL5adtUpJvyqtsrtamrHnpDiptk6shgPAhkKWWtgNK7L_JAbX21KGkzD1Ef_kO_o8zyPLwA-rnNMJ9b4uekGlBIafpgd4pXBdGty3JreOTZkrSjtlj_LipqjTIqr68ezAvU1yt_c4tZNjmKGsG1KvR4rdNlzYnuVuKW_hj7L07CUB7GDE1rKyRKJyP3UUYPYkIfuap8DgKDp4iKRG5BFDutds21bzmqiOJ9sBox2mPRv35Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
عکس جدید نیکی کریمی در 54 سالگی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/Futball180TV/107865" target="_blank">📅 16:55 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107864">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d579a3c3bc.mp4?token=jBiQ4EO9BAj2bAKG4qpN0bJByRRTpobwSxU5dA4hKzYAbkxHSYIGmA5e4K1k6tsL02beBoIADPdMkBNjzYA9azxCjvJjPYmowlUOfz-Ui8bjledfo7-vtaOmETsl9HjZMAwfTJtVAUdUb9BvLo8LSHRpJ07VfqoIW_vdcJyI2W0nBjKEXuy5j9GULrhVUv3zFJNeMsCkYGgQk9XOWLRV2iOPmGHlimQffMmIgChO_Ppy2TSBb3GEWB_aMeziFlcorJmblMAo49tS8o9gu4pMWgYVyhDPc1CR3Nct0np6Gy0uOOFpIIouNzgwr2aLqmC-WphSNpQZQtocwjZ3pqW08g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d579a3c3bc.mp4?token=jBiQ4EO9BAj2bAKG4qpN0bJByRRTpobwSxU5dA4hKzYAbkxHSYIGmA5e4K1k6tsL02beBoIADPdMkBNjzYA9azxCjvJjPYmowlUOfz-Ui8bjledfo7-vtaOmETsl9HjZMAwfTJtVAUdUb9BvLo8LSHRpJ07VfqoIW_vdcJyI2W0nBjKEXuy5j9GULrhVUv3zFJNeMsCkYGgQk9XOWLRV2iOPmGHlimQffMmIgChO_Ppy2TSBb3GEWB_aMeziFlcorJmblMAo49tS8o9gu4pMWgYVyhDPc1CR3Nct0np6Gy0uOOFpIIouNzgwr2aLqmC-WphSNpQZQtocwjZ3pqW08g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
🎙
صحبت‌های رسول‌مجیدی درباره سختی مربیان تیم‌های ملی بدلیل زمان کم آماده‌سازی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/Futball180TV/107864" target="_blank">📅 16:33 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107863">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/45ea1e2bc4.mp4?token=v9KiplPNl903XrT9SvjOGWSGf1hLjzJDu1f46YGgOWnvVIYCDBc2as4pSW9e8wRTvmBUwEHR3V0KD5NZRVMeZRxzigiL5XgfZNRDEjL7OLmXfpmkxpgtS0MAPAlLnUaj_RNUqfA57ABXYIzUVpbAnhV2LtzBRsTCQX3axXah-PCwV0qOP4Bz_0p1WRvlXvQL67fYKkB_bEL6P0GzOAgMJBy2Ax3mT4vxlCRTGksaY97jPoNlyYaBG-MagMLUoYhfsOuEP2JlnrKbfQktxjWtSbizZogqCL41XZvyFIDUjY7VsIq0oxGaomz1JfZc4mH8_C1V_R38ZhPTkV8eRGO6rQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/45ea1e2bc4.mp4?token=v9KiplPNl903XrT9SvjOGWSGf1hLjzJDu1f46YGgOWnvVIYCDBc2as4pSW9e8wRTvmBUwEHR3V0KD5NZRVMeZRxzigiL5XgfZNRDEjL7OLmXfpmkxpgtS0MAPAlLnUaj_RNUqfA57ABXYIzUVpbAnhV2LtzBRsTCQX3axXah-PCwV0qOP4Bz_0p1WRvlXvQL67fYKkB_bEL6P0GzOAgMJBy2Ax3mT4vxlCRTGksaY97jPoNlyYaBG-MagMLUoYhfsOuEP2JlnrKbfQktxjWtSbizZogqCL41XZvyFIDUjY7VsIq0oxGaomz1JfZc4mH8_C1V_R38ZhPTkV8eRGO6rQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🙂
بیرانوند تو سربازی اسلحه بازو بست کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/Futball180TV/107863" target="_blank">📅 16:05 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107862">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/367af750e7.mp4?token=E6VwkWaVV5VIEzhgBMntEJ1M-AIQdJvEuP47Q_Dd2CxAxkzKFr7bgP7WABr66MavfsGY4gCl8GinO5lz4gBlw72MU1ZI52q3Qlaw-9iLHN3wUvPG8dyV0SEoFYLzVSDSC2iXDczOvzr9zuF7bknx8pDcJ7SdA5Nln9FgjMXtAehsfM6m_ixZsIWfZnUq8G5SfAre_G63lrS0VkLnP4IfPfAH8aGTZugSstMVB4-SudiPbaaTasBoGWrgLGv9135fjGtASd-ZV0KsEp7dxGXX_oJfFK40hl7FNdFCrgwtU5yAIu__507nqLfOofNc82bff4FYkg1Io57s-HFyhmkx7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/367af750e7.mp4?token=E6VwkWaVV5VIEzhgBMntEJ1M-AIQdJvEuP47Q_Dd2CxAxkzKFr7bgP7WABr66MavfsGY4gCl8GinO5lz4gBlw72MU1ZI52q3Qlaw-9iLHN3wUvPG8dyV0SEoFYLzVSDSC2iXDczOvzr9zuF7bknx8pDcJ7SdA5Nln9FgjMXtAehsfM6m_ixZsIWfZnUq8G5SfAre_G63lrS0VkLnP4IfPfAH8aGTZugSstMVB4-SudiPbaaTasBoGWrgLGv9135fjGtASd-ZV0KsEp7dxGXX_oJfFK40hl7FNdFCrgwtU5yAIu__507nqLfOofNc82bff4FYkg1Io57s-HFyhmkx7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
▶️
با توصیه‌های هانی‌رامبد، اینجوری شانه های پهن تری میسازی؛ ذخیره کن و بفرست برای دوستت
❤️
👌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/Futball180TV/107862" target="_blank">📅 15:40 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107861">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/anIwa143B0VGe1_tZVmNxcsAY1HMcio8XSMUbdrUg6-dEvFptsvTSklWJbHDUlqCTVs_TTEAU5_4sHd3EHhneXpcZXs-36EhLnk8ZxoFCgt_WBA1xF4HvYpkLomsQJtresBH7qTy_XuxMEVCWQctjla41NI2jdBxE8DLiftMC5eFLscir8LuSnEqIQB86a8nCHhNr4N0N4T8MFMdpiv9MwQ3oaieh3In9I1iYC6kRgjN9RDv7TrDPTaiP6gJK2ONIuoOnY9YRFKpVGRWIkx3fW56Z0EsZam8RkSXrSGWEjmlaVt52lg4DcqNjwwoRDv4PUUvmLF0rAL_1s-sP7SRHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🇪🇸
اسپانیا اولین تیم ملی مردان در تاریخ فوتبال است که 41 بازی متوالی را بدون شکست به پایان رسانده است.
🤯
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/Futball180TV/107861" target="_blank">📅 15:15 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107860">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c6f99cc68.mp4?token=hDbncCkwPMRQAvhdpvIeEu7zzQLxeYuvpDEsWJCowjBl-fNb6EH1eO6QMvVtGxmsAGZU0rauDY-kcO4lT2HYaU1dhrcG2akS1QKUZf3IjbNUYYHpJcqbysaAD5eJ-9tykNFWrZBaWkQQ6z-s9CPDO9KTDnPeFWoiJYXs92znxgvaD50YC_GIm71-BPf183To9j3i43fFrUanX1fIaOZ751_-OFjx8Lh4v5N7cJiGIuiXKVU5t4vgxvvGqdcdUJyZiGW9m93wFAFUhhVLTApwepKEYPQzNEIFQuHu3_j8ta-397Q3SlAA5Pr-rZPImDeNCcYJJrEo5apB4jw_q4wuMwsQ3EIz7REpxFkuomzRq5OVlUH10hIHZ09G8A2_COMHFvdJk02RnvDajwCTv9cFV9Zx5QSQf-X1n4Rc64mKGr2IfDJaOHF2cEyNw1YgQdFZ6pSxLRmww2EqVfpuawCKYuuL5RWJ_Gq6N9cv7LUyDlLUjKavFBx_oq_uHAiV-xKuESeyEkRZ7FmNm2apJfdBbIE8hFJuBbKtrL01ZLZrNAbn4X3C18k7PaMXncMHtbAE24-EPIrR4DiEA3Ubg9PNZrovmknBO8B5yXmqJ-AFt64zKljvOAkOjnRrUoPLUNxS9nqVVLxgrtIZBB0EsT_qm_7GrCyF_LUhMrFzdqjXgTc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c6f99cc68.mp4?token=hDbncCkwPMRQAvhdpvIeEu7zzQLxeYuvpDEsWJCowjBl-fNb6EH1eO6QMvVtGxmsAGZU0rauDY-kcO4lT2HYaU1dhrcG2akS1QKUZf3IjbNUYYHpJcqbysaAD5eJ-9tykNFWrZBaWkQQ6z-s9CPDO9KTDnPeFWoiJYXs92znxgvaD50YC_GIm71-BPf183To9j3i43fFrUanX1fIaOZ751_-OFjx8Lh4v5N7cJiGIuiXKVU5t4vgxvvGqdcdUJyZiGW9m93wFAFUhhVLTApwepKEYPQzNEIFQuHu3_j8ta-397Q3SlAA5Pr-rZPImDeNCcYJJrEo5apB4jw_q4wuMwsQ3EIz7REpxFkuomzRq5OVlUH10hIHZ09G8A2_COMHFvdJk02RnvDajwCTv9cFV9Zx5QSQf-X1n4Rc64mKGr2IfDJaOHF2cEyNw1YgQdFZ6pSxLRmww2EqVfpuawCKYuuL5RWJ_Gq6N9cv7LUyDlLUjKavFBx_oq_uHAiV-xKuESeyEkRZ7FmNm2apJfdBbIE8hFJuBbKtrL01ZLZrNAbn4X3C18k7PaMXncMHtbAE24-EPIrR4DiEA3Ubg9PNZrovmknBO8B5yXmqJ-AFt64zKljvOAkOjnRrUoPLUNxS9nqVVLxgrtIZBB0EsT_qm_7GrCyF_LUhMrFzdqjXgTc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
💥
پیت هگست در سالن «کلون آرنا» در آکادمی نیروی هوایی آمریکا، در یک نوبت ۹ شوت از ۱۰ شوت سه‌امتیازی خود را به ثمر رسانده است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/Futball180TV/107860" target="_blank">📅 14:50 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107859">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/969710a175.mp4?token=EMl9a3iNCaZgedLMei2goxbQeEfR1K0MCcZd-wT0nHk51bt_CcqBCw1qHoxpHKpQ4P8Tf5KEnvPeKfv3iHkGUIsfU6VP4p0--B8gSzSJWDCZ2fIb2R57BmOzhJU1cRF_xSpvJJ2wImXRl5aAbbTeL8MB1CibK_nH9j1E_UGr8PEWrhVqIVc8iLHzaHZBCpyjQJVRpyR2VrQ_EEScZXPban1RkxZKRDaBh4nkjOqq-YbgsjrUBojhJJNyO3ffIqriAYm6gUpQWwVPard9CXYv9NVW-OQb9Xl6gMEeo59zrafoiVrlilFwHuRo0zF7cyeeVO2smIXUDPDxRitRSQP60JdNyeMpS1qeelva0pxOtMao28oxtqvtO0k7U7xF6hYO5jSDk1aR9XQsXhhI4sVZrEXjgSyLZqhysVr31Dqe5GSinCMPFXTx_ZdF95w5G2gMerdpgxi04bveY9Mf6vc403qLZBznwGxpR2LnVRc5ApTKdRBYFaqSPAWU9Ad78LRuX4ijcu9Sr1OEiTmoSzvs4LiZowEG9YmRn32TdvBd-nc0Zv3ay76ksasgETYqNDl-EZ2N2ZjlD03725V5usafi_2ISnQ36L8wnkdVgXC1NFrfY2JQnVviv3kXYm2yRX4bnL-jP8SuohVQJSfmVpiks22NACVz78rGE10M8jT38tI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/969710a175.mp4?token=EMl9a3iNCaZgedLMei2goxbQeEfR1K0MCcZd-wT0nHk51bt_CcqBCw1qHoxpHKpQ4P8Tf5KEnvPeKfv3iHkGUIsfU6VP4p0--B8gSzSJWDCZ2fIb2R57BmOzhJU1cRF_xSpvJJ2wImXRl5aAbbTeL8MB1CibK_nH9j1E_UGr8PEWrhVqIVc8iLHzaHZBCpyjQJVRpyR2VrQ_EEScZXPban1RkxZKRDaBh4nkjOqq-YbgsjrUBojhJJNyO3ffIqriAYm6gUpQWwVPard9CXYv9NVW-OQb9Xl6gMEeo59zrafoiVrlilFwHuRo0zF7cyeeVO2smIXUDPDxRitRSQP60JdNyeMpS1qeelva0pxOtMao28oxtqvtO0k7U7xF6hYO5jSDk1aR9XQsXhhI4sVZrEXjgSyLZqhysVr31Dqe5GSinCMPFXTx_ZdF95w5G2gMerdpgxi04bveY9Mf6vc403qLZBznwGxpR2LnVRc5ApTKdRBYFaqSPAWU9Ad78LRuX4ijcu9Sr1OEiTmoSzvs4LiZowEG9YmRn32TdvBd-nc0Zv3ay76ksasgETYqNDl-EZ2N2ZjlD03725V5usafi_2ISnQ36L8wnkdVgXC1NFrfY2JQnVviv3kXYm2yRX4bnL-jP8SuohVQJSfmVpiks22NACVz78rGE10M8jT38tI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فوتبال معلولان عجب صحنه‌های فوق‌العاده‌ای داره!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/Futball180TV/107859" target="_blank">📅 14:25 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107858">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/81e41c5067.mp4?token=g11Kxrto7YoMZUijxrs1rV0yzZYIVA_8fFtE4Ky6yqjOmQt9yBXQfjUNweSeMiR_aEWwo1ZNsmUdEo9FXAmxJq9WYRkYoaYhsCPBefKDgQBAHOANfhKcn819ZUtw1T_5AV0PYahTCb4T_p-xdB77V5fpO3fSiUbdAX4m_fEC0r8vkZQvcU0RqDgFeuba1Ua6DrfZ3veOg_EhZRA7o2qK1jxQnxA02hO0StVhSIPfwWMVFmb2np3QTlBFczeRcbLEEZuUuLWrf9VxEtvv0Rjlq9mJJ-YqNHaR3Iv0uHf_eYBRoOxJkwoLAmbVBEBzkivO-0c2yueny3oOAZ6RGGKDIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/81e41c5067.mp4?token=g11Kxrto7YoMZUijxrs1rV0yzZYIVA_8fFtE4Ky6yqjOmQt9yBXQfjUNweSeMiR_aEWwo1ZNsmUdEo9FXAmxJq9WYRkYoaYhsCPBefKDgQBAHOANfhKcn819ZUtw1T_5AV0PYahTCb4T_p-xdB77V5fpO3fSiUbdAX4m_fEC0r8vkZQvcU0RqDgFeuba1Ua6DrfZ3veOg_EhZRA7o2qK1jxQnxA02hO0StVhSIPfwWMVFmb2np3QTlBFczeRcbLEEZuUuLWrf9VxEtvv0Rjlq9mJJ-YqNHaR3Iv0uHf_eYBRoOxJkwoLAmbVBEBzkivO-0c2yueny3oOAZ6RGGKDIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سمفونی خیابانی!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/Futball180TV/107858" target="_blank">📅 14:00 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107857">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5554fbfbba.mp4?token=sFqT6b8aHNbWPhUBY7d5gAX4dhnK7tuB1N_vz1-3Lys3_ACUUnIHcWoOFN1eH-ebACxG2AGT7rITHRGie7Vd8Be9JLadWjaRksF9lXvOnIywAdJplc7UHM1EDT-O11nfHlpLtDihZ-E9bZqeI688zV_VpDUxTgSpe1LtQuD3uCIl_qvafQVR5HQBBRxO6pLoZMbXSATkfVAfhbJrszNrY8GOsqXfebHXGAGz5xkpDXBCVJP_byLq7ClB8mpGLkBxFsZVxhI1kzwRE3BSS1zfisLgke9FMMXOSwG1UXJ3G5_O_OAjqhJ8EPbpUjw7W2EmvgeL6ZZPqPkyNI_kYXrGwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5554fbfbba.mp4?token=sFqT6b8aHNbWPhUBY7d5gAX4dhnK7tuB1N_vz1-3Lys3_ACUUnIHcWoOFN1eH-ebACxG2AGT7rITHRGie7Vd8Be9JLadWjaRksF9lXvOnIywAdJplc7UHM1EDT-O11nfHlpLtDihZ-E9bZqeI688zV_VpDUxTgSpe1LtQuD3uCIl_qvafQVR5HQBBRxO6pLoZMbXSATkfVAfhbJrszNrY8GOsqXfebHXGAGz5xkpDXBCVJP_byLq7ClB8mpGLkBxFsZVxhI1kzwRE3BSS1zfisLgke9FMMXOSwG1UXJ3G5_O_OAjqhJ8EPbpUjw7W2EmvgeL6ZZPqPkyNI_kYXrGwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
👍
ویدیو جالب دو بانوی کاروان ایران در ناگویا و خوشحالی بابت کسب مدال در آسیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/Futball180TV/107857" target="_blank">📅 13:35 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107856">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cedf090cb4.mp4?token=e7-kDBHed1--bi8e4GFcrp7uhpQ17kTqdsS4up80RPUCSJAiNwIlImEpy7vdipr26I5u6qO9MA8Vn5soR-58995H073nhClGzk-LPVj_2FhFYZvyrpF4VKDJWra_0Sf_vG2xTUwOMcMll9Eo1YVXv7AYe2WCCDwDjjVwyuGs4dtBp9Pr9Bmdx_Z74ElOAzlOMIjwFWABtB1ajRuobVN1tw5NzaIjLWdgB4TFdv2s0km5teePDXRUpk2a-SqrEm7zMW-Ojbu65kQRQAFGADlSORdKQnC4UbBWX_MWvHDvdFY2v04cirpJhVNKTSqyztLWAG-aoL9JRfhI8KF0YS-Fzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cedf090cb4.mp4?token=e7-kDBHed1--bi8e4GFcrp7uhpQ17kTqdsS4up80RPUCSJAiNwIlImEpy7vdipr26I5u6qO9MA8Vn5soR-58995H073nhClGzk-LPVj_2FhFYZvyrpF4VKDJWra_0Sf_vG2xTUwOMcMll9Eo1YVXv7AYe2WCCDwDjjVwyuGs4dtBp9Pr9Bmdx_Z74ElOAzlOMIjwFWABtB1ajRuobVN1tw5NzaIjLWdgB4TFdv2s0km5teePDXRUpk2a-SqrEm7zMW-Ojbu65kQRQAFGADlSORdKQnC4UbBWX_MWvHDvdFY2v04cirpJhVNKTSqyztLWAG-aoL9JRfhI8KF0YS-Fzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
صحبت‌های متواضعانه اسطوره مهدی‌ مهدی‌کیا درباره اختلافات بهترین نسل فوتبال ایران
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/Futball180TV/107856" target="_blank">📅 13:10 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107855">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/54734be7bf.mp4?token=SUOrWlfaD20m6KtJG-rCWVz7lqwNHoePsRDg8Cesui2cP4Y5dVvImJkbuLRqmDOQBoWsEhBOUI9E8DZKuKI3IbfoU3wI1Fs1BJymKOwvEu4KV6_u9iHxBv0O0GZM7eeOFG7_Zhk1w_BR7r53NMbG12GUniyVV8iR9l6qhmvo67cBZn17nIUTyiIoargddAYZtlZ9dYmiIBGsAf3LeAoJMgyUjyQpbtC32tmNKYcQGj9ffDboduMVmTUm8oMabB1-POJ8jou7rj5FMe0OlcI2oQRy09eDx5XZ-sPBZ3TY3qNt_wbPVsN5nVh3JyNzL9fQYsqqF6kr070fqATq41fOxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54734be7bf.mp4?token=SUOrWlfaD20m6KtJG-rCWVz7lqwNHoePsRDg8Cesui2cP4Y5dVvImJkbuLRqmDOQBoWsEhBOUI9E8DZKuKI3IbfoU3wI1Fs1BJymKOwvEu4KV6_u9iHxBv0O0GZM7eeOFG7_Zhk1w_BR7r53NMbG12GUniyVV8iR9l6qhmvo67cBZn17nIUTyiIoargddAYZtlZ9dYmiIBGsAf3LeAoJMgyUjyQpbtC32tmNKYcQGj9ffDboduMVmTUm8oMabB1-POJ8jou7rj5FMe0OlcI2oQRy09eDx5XZ-sPBZ3TY3qNt_wbPVsN5nVh3JyNzL9fQYsqqF6kr070fqATq41fOxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
🇮🇷
خاطره بامزه علیرضا بیرانوند از شب پیروزی دراماتیک مقابل پرسپولیس در ضربات پنالتی …
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/Futball180TV/107855" target="_blank">📅 12:45 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107854">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u-nnFjcVNBWoDL05djS7sQ2VXNJ6ppY-bw4cCFUQinQLty0juMwpwI0dBnZHSXXwRbNWLRYZkj1-aCmJMFS8OtJ6XQsFDMHe7sBSLfNR1uAFHgSSraUDOXgWYAQ0oCCZsylHjCPoiTxqMtugKP-Wbeetx-VMSe4S4QxDu2lwmg0ZrmsbAz1o9WNOjyYHOY9zqP1wvxwr98KFEfRQ76fkNFw9yDLCphVtK7AHrXC8MezhgHPF00JVcw0cYhRnqL_UTF0bWMJrNlMJsWYyOsJ_CiEB-AiJfCoIWbUu9q6eFp2Kt_R-t9sQluVE1vinivPNA71vFydZMbZtDuWgujqQRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇮🇷
🇮🇷
استوری مدیررسانه‌ای استقلال در واکنش به مصاحبه شب‌گذشته مدیرعامل پرسپولیس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/Futball180TV/107854" target="_blank">📅 12:32 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107853">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AooO0Tdr-L8My6ZInB6T6CgziYMbBvj3mkKo7Q-hgbaF3_OAOl25d3R_QlA-ojwqDs5-z0w3NQ2-Ay6ukYEGsIE4wr6mP8iaCJ6Eb94I2JAmFJIaE6NBm31OJ_fnuFTb_4R7KDK8fscHvMUdNT1bKJXHLnYqqXp-zAho-RQfzDrDk27n_NCNgpIVtwZf59oOlRafxps2gF-1WptOoBNcpF3LDjpqUyVIXX4er0ZgmiG2JwZv5Hc65R_NSRlSxCX-AFniesis0mT5eEiVkyC4QZKGrOBlIfCiiMs42-eKulRgiQzsZkg-GfN52qRnL6bsuao-s0_Ii8I856qKoG9kEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⭕️
🇮🇷
هیئت‌رئیسه فدراسیون فوتبال اعلام کرد که جام‌قهرمانی فصل‌گذشته به استقلال داده نخواهد شد و پرونده این موضوع رسما مختومه شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/Futball180TV/107853" target="_blank">📅 12:25 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107852">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f754e7f64f.mp4?token=aJyo7BOPIahDdsJUAv6NTGt65n80gxqZbTPxgs9I-tvm-V7ZY0pbJXHl1YIxpzZR8Hu5ocO4uKJOgNTApHW1Qx6cl9vBcih_AQsx2ai7AcxPj66GkHiQzg0p-_-iQ5dIlB3Mktkz37H7Exg5_Mx7cFA22tcjHs2aCBEXXJP1LbM3nt70X0E_jZ_pz2DBybY2Ubk3wHMbphle3KzgGPA_ukMvkXsHJMYt4WKXM8ffxDfPyVw86Qd1P_YqHivEgnE-IOXybz54RZPpTbuxub-gqTLG7VOGrS1hM0QAbbf3nqSV18SgPXajpNfTo9gr1sLMPWaX-FkjxDXLPg5sGUoxcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f754e7f64f.mp4?token=aJyo7BOPIahDdsJUAv6NTGt65n80gxqZbTPxgs9I-tvm-V7ZY0pbJXHl1YIxpzZR8Hu5ocO4uKJOgNTApHW1Qx6cl9vBcih_AQsx2ai7AcxPj66GkHiQzg0p-_-iQ5dIlB3Mktkz37H7Exg5_Mx7cFA22tcjHs2aCBEXXJP1LbM3nt70X0E_jZ_pz2DBybY2Ubk3wHMbphle3KzgGPA_ukMvkXsHJMYt4WKXM8ffxDfPyVw86Qd1P_YqHivEgnE-IOXybz54RZPpTbuxub-gqTLG7VOGrS1hM0QAbbf3nqSV18SgPXajpNfTo9gr1sLMPWaX-FkjxDXLPg5sGUoxcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😆
😆
چالش فوتبالی با چهار اسطوره محبوب
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/Futball180TV/107852" target="_blank">📅 12:20 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107851">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/atmqeKrhVYIu2bCckIZEtkNACAZOkXbzuqYvn_wV72n6YJNEYsme6eoX9gZWkpL4cU8CJnI6Y_y_TTqea8oi3R1H4fmSOOkCub7wXVGiz2vNcpcseSIpsiA-XuRTIamNdDSZe3yfcQI2LyPcmy-KJHH6PsKimeMnrahJo0rMOmsWEg3k_NDW5YdwlnBBdYnU1q79zYtvNL4m96NoTamFeEkdLYAr2MmeHDdto4eTHAiKwXNbXz594UAhNgEY2bpx7K8E2e3QwD2TgagyhDv5UBLjJNJzjfvU1NzFW4aL0uGJIgDyDtkGSGZItqUuoVzdbC-Lx9Q62VBnaBi1eRTnSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🇪🇸
عملکرد مهاجمان بارسلونا در این‌فصل چه در بازی‌های باشگاهی و چه بازی‌های‌ملی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/Futball180TV/107851" target="_blank">📅 11:55 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107850">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6fd2204c7.mp4?token=JPE-f16qXeogq2iynClAcluTQBc0gib6HPFrgh130Jh1KliG01fMNvPIk30YqCka0ylpC_HB1kkPeSzD5aM7N-tXmZqjdLRSW7XnuJVhnoMNUZ4oZI16oQOz1S9xNIlD5UZFwbK20JXzLDFYnf27Ar7GhQX4tgrLJFkktyMeMIVUBwx-A1eFHwDyBH789c8pBtKx0HNZn5bPzIwdBz0LbKor2-oIajQJoG5kFI67yyOrlY6L-Oyhkw5WydvNKNPqMX0noOm6Y3afkw5sVdeqG9gZcJwi8IbzvVpDlVOFeH9i3KCOgLslbJ9xgySWT_GycChladrNCvC7UFf60GQkzDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6fd2204c7.mp4?token=JPE-f16qXeogq2iynClAcluTQBc0gib6HPFrgh130Jh1KliG01fMNvPIk30YqCka0ylpC_HB1kkPeSzD5aM7N-tXmZqjdLRSW7XnuJVhnoMNUZ4oZI16oQOz1S9xNIlD5UZFwbK20JXzLDFYnf27Ar7GhQX4tgrLJFkktyMeMIVUBwx-A1eFHwDyBH789c8pBtKx0HNZn5bPzIwdBz0LbKor2-oIajQJoG5kFI67yyOrlY6L-Oyhkw5WydvNKNPqMX0noOm6Y3afkw5sVdeqG9gZcJwi8IbzvVpDlVOFeH9i3KCOgLslbJ9xgySWT_GycChladrNCvC7UFf60GQkzDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
🇮🇷
خاطره عجیب حنیف عمران‌زاده از وسواس‌های فتح‌الله‌زاده: حاجی توی عربستان چمدونش رو زیر شیرآب شست می‌گفت با دستمال کاغذی کنترل تلویزیون را بردار
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/Futball180TV/107850" target="_blank">📅 11:34 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107849">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f8daf57827.mp4?token=HzCgT57ZTnCJ_xraI9aqCqwkgk8brtRf3RJ2STJcH5SNtZXgKc0yZSUJoAlturYTLhb9F6HcTA6OFMf5ZspSVPIjUtIz54dF58uZVNe8pTQmz4jF35zXoYZVJC0BkPoyDdW3GyIc2s_aUr7XKJuR0HpupCW_mZX4DiLL8nIVOl6Vo-jV81GFG9F9zomyoymbnQZWsWoUryhYtjbWbBK65K8WdS9NzxL-uYPp6g_b8YweWIBl--tWaNr_79g9oc0xpXGWqePE5MurZBigqLgyP1bPoTRKAoGrRcogZMT1OIc_9PmDuPxuFC1MhHi5oJdgRF1Js2mqH0GW2VcNwd7elQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f8daf57827.mp4?token=HzCgT57ZTnCJ_xraI9aqCqwkgk8brtRf3RJ2STJcH5SNtZXgKc0yZSUJoAlturYTLhb9F6HcTA6OFMf5ZspSVPIjUtIz54dF58uZVNe8pTQmz4jF35zXoYZVJC0BkPoyDdW3GyIc2s_aUr7XKJuR0HpupCW_mZX4DiLL8nIVOl6Vo-jV81GFG9F9zomyoymbnQZWsWoUryhYtjbWbBK65K8WdS9NzxL-uYPp6g_b8YweWIBl--tWaNr_79g9oc0xpXGWqePE5MurZBigqLgyP1bPoTRKAoGrRcogZMT1OIc_9PmDuPxuFC1MhHi5oJdgRF1Js2mqH0GW2VcNwd7elQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
👀
‼️
سردار آزمون به دو بانوی تکواندوکار ایران یعنی ساغر مرادی و فاطمه احمدی که در مسابقات آسیایی مدال کسب کرده بودند،‌ نفری یک میلیارد تومان پاداش هدیه داد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/107849" target="_blank">📅 11:22 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107848">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👀
‼️
🇮🇷
صحبت‌های شروین‌بزرگ درباره پیشنهادی که در فصول اخیر از پرسپولیس دریافت کرده بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/Futball180TV/107848" target="_blank">📅 11:11 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107847">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/107847" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/Futball180TV/107847" target="_blank">📅 11:11 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107846">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RRMOMtiCNAArsRAaCvPkZFncgIeWvGAwHJbQSRsMy9tpdeJIKTtv4bpPiVmaC5Da5-n-5nU_4F6lpzkWftwRoppt1ETySlQEIlqDcvtTyeTycl_4S6JrG_BpANpJrbMziscpatZ2Zy9sSd_DIAxfxNzEIiZrbONrZSnCOE4pRrs1P0MEDjH4KhpmmBiG3_XkefkiucC3uSUSouRR2FVw5BfxMIWnzsCMckNRlILwuAzmkzs2wTAVP3HEdAYJOcFwn7l2egsElRweOtVSFc-AYBS0Ouq9b4AVXVRQDeujLXLKB72Izigmlo7WzZa9MqQt6u9ozb3wL5JML8G04NWlHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
مچ‌های مهم امروز در سایت بین‌المللی
TrexBet
بلژیک
🆚
فرانسه
ترکیه
🆚
ایتالیا
لهستان
🆚
بوسنی
سوئد
🆚
رومانی
نیوزیلند
🆚
ژاپن
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
انتخابت رو انجام بده و آماده‌ی هیجان باش!
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
http://T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/107846" target="_blank">📅 11:11 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107845">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/294e1e1160.mp4?token=XXLMkEgDfQR7b_FxvJxWHdbCznT-JNS8rtEe7iLpbTl2I9ygV8ScJCYUTSQfr0mtUeztRDv6Gs2NykxkBSO11v-Qy8xCg6esZ_GcJygAgTW8VtMLD6oBdbOEwijyxWyY80r622Fuehl3Vk1td091dHbCPdFu4jnYxghuGQNk0k-gA2dtlbHWnw3HHVeh9i7MEgzKuDp9TdPeo-eYOYO82j2irNx_YDrZw5zCubHFk1rFZpdBqdZLWQfp18D2-4p84Dl1ZcL918PWSQtildPeJ1WNzGW1i4toa-TKd-mp_F1U7MWVKPg4OFpxeCJM7wv2oqLXf5y3nDV12y7650imlg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/294e1e1160.mp4?token=XXLMkEgDfQR7b_FxvJxWHdbCznT-JNS8rtEe7iLpbTl2I9ygV8ScJCYUTSQfr0mtUeztRDv6Gs2NykxkBSO11v-Qy8xCg6esZ_GcJygAgTW8VtMLD6oBdbOEwijyxWyY80r622Fuehl3Vk1td091dHbCPdFu4jnYxghuGQNk0k-gA2dtlbHWnw3HHVeh9i7MEgzKuDp9TdPeo-eYOYO82j2irNx_YDrZw5zCubHFk1rFZpdBqdZLWQfp18D2-4p84Dl1ZcL918PWSQtildPeJ1WNzGW1i4toa-TKd-mp_F1U7MWVKPg4OFpxeCJM7wv2oqLXf5y3nDV12y7650imlg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
⚪️
حاج‌صفی کاپیتان تیم قلعه‌نویی: امیدوارم در‌ جام ملت‌ها باشم اما قلعه‌نویی‌ دنبال تغییر نسله!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/Futball180TV/107845" target="_blank">📅 11:05 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107844">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">‼️
🎙
🇮🇷
🇮🇷
بی دلیل از استقلال تعریف نکردم؛حمید مطهری سرمربی فولاد خوزستان: کاش سهراب بختیاری‌زاده خارجی بود!
🔺
حمید مطهری می گوید اگر نتایج سهراب بختیاری زاده را یک مربی خارجی می گرفت، همه کار برایش می کردند!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/Futball180TV/107844" target="_blank">📅 10:40 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107843">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OZVxP3tVogRrY6Iz4Ucn5FAmedTtZaXNZqZCUzjcOdplY9yT8KuMH4sfTQALqsq5u--ngRU8-t_GaZ_EERwU8nWUB7Ukwy1AHEAI10zIp5HT_jCJR5wI9lZOvR6a7-GUlGQbOexf3n5QhZtq--1MAIvTJUCYN1m56an085vL3HHE7JdQLgYz5hyEqzhntLcoxoX4-p_45y5WIrNgchAceUR9faZecwf1G5mjrxG0UCFU1dJNVMb5pfmHOh2PbVmybcBqPgem7F4ZmFdQe4ZsmCzs4nlEz_CMsj9pM2Fx_rWIvS0VtmVc557R8CCTt4qDD6_HfoDFF15IqEzO3sCsjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
💸
گران قیمت ترین بازیکنان اروپا
⚡
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/Futball180TV/107843" target="_blank">📅 10:15 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107842">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75399136b6.mp4?token=Tz8JhZsFJJET9e_OG_C_OUhqAuQvfFxi90wBnHuvEm47Fj5J7nHwmOr8jTWwB6obCkY4X1cM3IP2E3ksuP6oBBhmKt6_rdZnsJsvu9Zn8JIMZB-PnPmRhAb5MxM72LBO-jUCpinJd247nksMO5i8WhdWyi-vZpylBTlTzcfsoKHh_cA9VghPaxSuZ47jIiX8h5WoywnOuXo8ZeiG7vGcN9mEwYpxtn3FwqF1Agwo9bNTZdRXp5DJntDltXxcYA7xGwpYujOE4dlYZ7AgIUWeNkRXJrfcav7Y0xCXMMKIoVo-cINPZu_JNNn-Vtth9dJVfNS5Y_orOTsFI8zGyyYDM7ioQdqTaazG1TToK9be1VPtJyNeG94u2pRUwmhS1kVvUMz8NeFnDg5cEtT4mFsXA5VdBa0mYDGKhZi5OJPg-oNrC3B64ml7pBB28sWjBr54FyoX-Cglh3ByC3wAF99c6Lid9DVma2edthye3hP5r9-R8mEAqy_m3_LZ6qxTr_SEhFLbGAWg6FQPh5qHcSKdwg1Waxyaiv-7MN3HUg2FHVnvksEybLqQpDr1f5lScRWtg1pAERb875zQqJmQNKSNezaui0tjRU1M4LCBUxGx-4gDe2f4VYRHZGS_TECpmFa0IlWrMOt7MPazv1sHJFbi6Zl-bhHOemjayvAdnxxWGDo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75399136b6.mp4?token=Tz8JhZsFJJET9e_OG_C_OUhqAuQvfFxi90wBnHuvEm47Fj5J7nHwmOr8jTWwB6obCkY4X1cM3IP2E3ksuP6oBBhmKt6_rdZnsJsvu9Zn8JIMZB-PnPmRhAb5MxM72LBO-jUCpinJd247nksMO5i8WhdWyi-vZpylBTlTzcfsoKHh_cA9VghPaxSuZ47jIiX8h5WoywnOuXo8ZeiG7vGcN9mEwYpxtn3FwqF1Agwo9bNTZdRXp5DJntDltXxcYA7xGwpYujOE4dlYZ7AgIUWeNkRXJrfcav7Y0xCXMMKIoVo-cINPZu_JNNn-Vtth9dJVfNS5Y_orOTsFI8zGyyYDM7ioQdqTaazG1TToK9be1VPtJyNeG94u2pRUwmhS1kVvUMz8NeFnDg5cEtT4mFsXA5VdBa0mYDGKhZi5OJPg-oNrC3B64ml7pBB28sWjBr54FyoX-Cglh3ByC3wAF99c6Lid9DVma2edthye3hP5r9-R8mEAqy_m3_LZ6qxTr_SEhFLbGAWg6FQPh5qHcSKdwg1Waxyaiv-7MN3HUg2FHVnvksEybLqQpDr1f5lScRWtg1pAERb875zQqJmQNKSNezaui0tjRU1M4LCBUxGx-4gDe2f4VYRHZGS_TECpmFa0IlWrMOt7MPazv1sHJFbi6Zl-bhHOemjayvAdnxxWGDo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
🇮🇹
آنالیز انقلاب تاکتیکی گاسپرینی در این فصل با تیم آاس‌رم که حریف سختی در اروپا خواهد بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/Futball180TV/107842" target="_blank">📅 09:50 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107841">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">‼️
🎙
محمود فکری: باید به قلعه‌نویی حق بدهیم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/Futball180TV/107841" target="_blank">📅 09:25 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107840">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75fb30e6b0.mp4?token=qgvLYcnk5mfCSooUfsfYVI4ZPufLkjRY0agBTX2LgGrktTBRhXbySws-9HU2RdNHZRj9j_2AelTVk7EX0OoBkxSiLf_8lrqS-iWOAfiKs3bNDM3MSkEtlgT1lL9jtKVJLBNkl7MhBn1qiVCW5aK9Pj769DzEXwnLHTGHaa_UF6TPqQMhdagTV-yXMNjYdsRKZcYYK6-7MDixojIN8hFeK63F2Pc1w99C_Z8k5CzlaADwDhNaBEKCKUEi2YdJAk_Kt0ntETURCK0zHBT4tw5OlhmwRS8mxZlGXSVw9izKDSxR3R1orarc1ouZruRibFjqJ3iFyXW7sF25EpmsJbhmCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75fb30e6b0.mp4?token=qgvLYcnk5mfCSooUfsfYVI4ZPufLkjRY0agBTX2LgGrktTBRhXbySws-9HU2RdNHZRj9j_2AelTVk7EX0OoBkxSiLf_8lrqS-iWOAfiKs3bNDM3MSkEtlgT1lL9jtKVJLBNkl7MhBn1qiVCW5aK9Pj769DzEXwnLHTGHaa_UF6TPqQMhdagTV-yXMNjYdsRKZcYYK6-7MDixojIN8hFeK63F2Pc1w99C_Z8k5CzlaADwDhNaBEKCKUEi2YdJAk_Kt0ntETURCK0zHBT4tw5OlhmwRS8mxZlGXSVw9izKDSxR3R1orarc1ouZruRibFjqJ3iFyXW7sF25EpmsJbhmCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❗️
🇮🇷
فوتبال جا مانده ایران از امارات، از زبان شهریار مغانلو؛ دانیال اسماعیلی‌فر و برشمردن مصائب هواداری در کشور ما
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/107840" target="_blank">📅 09:03 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107839">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e551facae3.mp4?token=MRk2nAqMLLtBzkb8Qme6RKN2r5iJYg4VZxFK4WB0aMTyFyzVU4a2tRX2kho56AgGrRS00Z7HvicSvf1ANHyrXLebEDpkoma-T9sdPZkP567mZbnaO4hM2m74NUA2b8SSnbvx-Z3OZ50bU8ksdY33C_gkWKdOPv4PtOQ21QAPgFRsstPjYqKZPJLdUxZf530z6DlhaVBTijpRmnZ5vR__PLnlNPgsNbapIV5sYHQl2UtYQG4z4pL6j8WvSiqozWQ47jTX8qKYOSJA8HEWYpXSDI7HZqqU-y2kNIc2OG-a6iGh16gFuYvwiqHtLk2ZUqtGLjTHawSyFhkivMXUHJUiNYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e551facae3.mp4?token=MRk2nAqMLLtBzkb8Qme6RKN2r5iJYg4VZxFK4WB0aMTyFyzVU4a2tRX2kho56AgGrRS00Z7HvicSvf1ANHyrXLebEDpkoma-T9sdPZkP567mZbnaO4hM2m74NUA2b8SSnbvx-Z3OZ50bU8ksdY33C_gkWKdOPv4PtOQ21QAPgFRsstPjYqKZPJLdUxZf530z6DlhaVBTijpRmnZ5vR__PLnlNPgsNbapIV5sYHQl2UtYQG4z4pL6j8WvSiqozWQ47jTX8qKYOSJA8HEWYpXSDI7HZqqU-y2kNIc2OG-a6iGh16gFuYvwiqHtLk2ZUqtGLjTHawSyFhkivMXUHJUiNYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🥶
🇪🇸
جدیدترین پدیده آکادمی لاماسیا بارسلونا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/107839" target="_blank">📅 08:03 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107838">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/107838" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/107838" target="_blank">📅 01:06 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107837">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fk4WVu0W4NC7656oYRRmKNOaVD6Gx_ataHhpmAL8lG3pGsA2xCz6zlnXbR3NP8Au9OwIorVK2_8FnMdcOT_Dz4JuzSgwYIlXULcj1e-w0wDxuRZO9XNdnOVyyuuLQpf65rh0yI5zU-_hI7yYn4HeyWeP8BVFlavSagW5g8Ltd7sy7MXsb-C3ikDkRoHJ8JLaye2KxKcBGRjmb7AWsVmbwHAqgItC6gOQ6AyRvXBl7Vgjm1L_2witnNlqlhnsEw_5y_0eWYkrmZLZmVcCUsxZY_oDDJ3wb3fFaLC3nHhmxbrcNd-k7nCkdVf2uwOmwZ53NlLCtPtU6GyjZ66hDC-NEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
با اولین واریز، بیشتر دریافت کن!  فقط در سایت جهانی
TrexBet
🦖
بسته خوش‌آمدگویی ویژه
TrexBet
تا ۱۰۰٪ بونوس واریز
🦖
تا ۱۵۰ چرخش رایگان در ۴ واریز اول
🥇
واریز اول: ۱۰۰٪ بونوس + ۳۰ چرخش رایگان
🥈
واریز دوم: ۵۰٪ بونوس + ۳۵ چرخش رایگان
🥉
واریز سوم: ۲۵٪ بونوس + ۴۰ چرخش رایگان
🏅
واریز چهارم: ۲۵٪ بونوس + ۴۵ چرخش رایگان
🦖
🦖
🦖
🦖
🦖
🦖
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/107837" target="_blank">📅 01:06 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107836">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/107836" target="_blank">📅 01:06 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107835">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hahHgRQmqv2WdRcnzbFd4UDPAcGzB-qq761i19jX9VjbwiXFOo7-SWaqPC0e0zlFXoQkE670wgv3gz71NVwSixrSyYYqG24vDraGrE2k9Ipb-OskdSHBOsEFhV33xbReKzpnlPvLcRhjgt2-Eh_UA88mIOQclCt5IPXyuyuWkVOQbhGTAuuKPKQEw7roFs9Y4xcJNmthzkwCK8svBnsY8ricHQPPiEz_H-5o4QpO0IDcGrPMjXK4_31qtKe9WOc-rdVpFyX4AehDiisnKzu6rBsS219pZTH0PAru97FNVhC2_RzdnQ74QoqiCJdIps60k_Tl2nZAQwfAFQBIsjWUMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🎙
🇵🇹
ژرژ ژسوس سرمربی پرتغال: آنچه بین من و رونالدو رخ داده یک سو تفاهم است که به آسانی حل می‌شود. البته این بستگی به تصمیم خود رونالدو دارد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/107835" target="_blank">📅 00:50 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107834">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tHoKyXtGJQ8_h338tcTS4rFg2NcJV47UydnCuixlPbufzLn48AyKWOl-QO5JChRygHHPG-1d5SBV9wuY-KDo2EVgSU7DzoTrSAuqGz1UqdD-z3J_bz47R0bZs5r5txewvrzxf2EkHA1HXXb_9vAAmtFmnaGbMXlzp3QS7eD2vXTavqta2HPKwpWju_dOPAweq31o2juFmuIzZACEtU80sobRzswwCERIti0C69_BNgwvqQOD3Ax3fcxoIBYK-4DD3MTRpR6d9Xxq-Te2UpfJxFdnn2I-wCLjOo0NfnZqbGNVuVU82U4ZN-enpxJ4QW9RaSPtl20u9GEOIEoOt_Lx2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇵🇹
تیم‌ملی پرتغال به مرحله ¼نهایی لیگ‌ ملت‌های اروپا صعود کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/107834" target="_blank">📅 00:14 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107833">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/e30d963cb6.mp4?token=d-Z3ACm3GiJKnSMfGsVgIJWl3kbqPWYp26MvFL-9IZwDcOqwURnu9BtFUHvbwuhXp_ST6j18RoH_8EQitj17UritUAM0EXsC5M5ghOvu3OvrxKk4c2NJ_pm5PszeoKgRg2Oeo8lHl026iJNZPvUlhNhGBgRHua-6oDK1wES5bHC-XF6p_gbVL-_lW2g7kgxCzXxHjJia0F985DgIWoFLxeAIplC1oPVy7KBKWVEYzV8EoYWDRf1-HMStAFQBol1EtMdJhM6m_8lKD2TqbVVP3LnmxzXLzlupg0QnHC4m8H5GtzF-Ebdu07ujEtwcCwgeaxqojNasgK3a0G3QpMi5c5Rad79sz9eL-QwzuXsZpIZ6KnPLczvnweI7JH3Z71M6xXMKOTXfdVedyh4kq04I54TB2S26asTYEl-xuEQgTFePfi54fa8Inoie2O1coGrTma3JrOArtlt38qLzjQg-G0wbStBaIbYcVykVh7YVSBxvvDtVUP52o03h2V_zzSbJ2Ea6DqW_uIWUgwpT45rwlISEo3YYnDvEbRogKulsYKnKLxI_vMirvggqienKEtCt8oE9a5aDwaJvTbCKh7v8LOij3TJixtZ72T6FZRiS8Ciszvgs4pACNmPqv9Pbyaa6w8_dZ6LfDBInM4vNVq0FCFDBKw-6JXdFOGUzMoxvz6Y" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/e30d963cb6.mp4?token=d-Z3ACm3GiJKnSMfGsVgIJWl3kbqPWYp26MvFL-9IZwDcOqwURnu9BtFUHvbwuhXp_ST6j18RoH_8EQitj17UritUAM0EXsC5M5ghOvu3OvrxKk4c2NJ_pm5PszeoKgRg2Oeo8lHl026iJNZPvUlhNhGBgRHua-6oDK1wES5bHC-XF6p_gbVL-_lW2g7kgxCzXxHjJia0F985DgIWoFLxeAIplC1oPVy7KBKWVEYzV8EoYWDRf1-HMStAFQBol1EtMdJhM6m_8lKD2TqbVVP3LnmxzXLzlupg0QnHC4m8H5GtzF-Ebdu07ujEtwcCwgeaxqojNasgK3a0G3QpMi5c5Rad79sz9eL-QwzuXsZpIZ6KnPLczvnweI7JH3Z71M6xXMKOTXfdVedyh4kq04I54TB2S26asTYEl-xuEQgTFePfi54fa8Inoie2O1coGrTma3JrOArtlt38qLzjQg-G0wbStBaIbYcVykVh7YVSBxvvDtVUP52o03h2V_zzSbJ2Ea6DqW_uIWUgwpT45rwlISEo3YYnDvEbRogKulsYKnKLxI_vMirvggqienKEtCt8oE9a5aDwaJvTbCKh7v8LOij3TJixtZ72T6FZRiS8Ciszvgs4pACNmPqv9Pbyaa6w8_dZ6LfDBInM4vNVq0FCFDBKw-6JXdFOGUzMoxvz6Y" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
گل‌دوم پرتغال به نروژ توسط گونزالو راموس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/107833" target="_blank">📅 00:01 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107832">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/e974e0edb0.mp4?token=OniMYnZBvp7jBYyxHFwAHr3tlR9dQ8jJ7jaz3cJWDr4C7UHatYwNUayexF0f9-7og4bmEDEFt7KHaDLYVHQ828uazec2tcrX6Z_-uKR0EoiBLCUopWAxid6eINW59jKs4bg3QJ9t2effLxjg5_T0h1JhL_8i3-E-M57_yhHP6kQiI5KVAXpc6mKpuCtYdKohp1ORhCWLt3VrJF37iTd88NLUGXrSDx-lh96sa59lXsvwvwq1J_xsortGZnd6cCkeCZqY1fMUAjW0afSr3asWvF_o-Dml7OLFlaJSUsovIs_6KSNOXmZsr_p6GrFIUBPvWn8oZveGs6MnJNlElATWfIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/e974e0edb0.mp4?token=OniMYnZBvp7jBYyxHFwAHr3tlR9dQ8jJ7jaz3cJWDr4C7UHatYwNUayexF0f9-7og4bmEDEFt7KHaDLYVHQ828uazec2tcrX6Z_-uKR0EoiBLCUopWAxid6eINW59jKs4bg3QJ9t2effLxjg5_T0h1JhL_8i3-E-M57_yhHP6kQiI5KVAXpc6mKpuCtYdKohp1ORhCWLt3VrJF37iTd88NLUGXrSDx-lh96sa59lXsvwvwq1J_xsortGZnd6cCkeCZqY1fMUAjW0afSr3asWvF_o-Dml7OLFlaJSUsovIs_6KSNOXmZsr_p6GrFIUBPvWn8oZveGs6MnJNlElATWfIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
سوپرگل‌تساوی پرتغال به نروژ توسط ژائو کانسلو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/107832" target="_blank">📅 23:12 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107831">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/2872cf61d0.mp4?token=SGBkPdESsdFsHN1M_q35_RuJ79D9eZ_wk8-harkc1r4BSE9Pgbiwuq441mGUU7LjoK_h5q8yHv_rN0X0DyCQdrZYYixGL18swwxHysNr-rkGtEEFcwZzLhT8hQg8RY3kyQ2a_Jf1cNe2Ta22LQuzO6s54jXrfoLo_W2JnddUHFH5iNtc65JSPEEv-Set38ZhFfh3embgZGI3ioTshwdG4hzk635K_0S510guuYJ6vAXaWpH2GWam2pL5el9lhSN7fK-zcLU5zpWregb8LIbRPqKtgAR101F1wWS0vYOwPfkwkNjTFtuhviFHfownJUPgeBPrRGIxkDBGtNsOwCVV14j7_PPm606ffeuYThqWjtNciaYT6bhi7iYHTaRoHaHy34FVk4u_Mt_AeeXFcfJxGndk6epsQyIvzcB2lLST-uhgUeEdyFIap_RNk92u-JCwK33QJKTlb3QivOXOh7D_CrLtILmF_qcmL1bfbKBwUP7Nm_TdeT2McY8exBY9wVuAxMEoCLqshX0YwkpajdK_V1VmkpclDBiv4dA9T5dlZkSgJvTm8QvRG9xpl4_vtX1snbdlDuTxVn3jxuot8hWGuaJ4nFZtZUsiv5QgFEtH3A130kzNwkwUP8MUlIHSLvxorM3UNsPW4xEAzZVfD-Suwb28vivmVSDHmFoUX1KyxVY" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/2872cf61d0.mp4?token=SGBkPdESsdFsHN1M_q35_RuJ79D9eZ_wk8-harkc1r4BSE9Pgbiwuq441mGUU7LjoK_h5q8yHv_rN0X0DyCQdrZYYixGL18swwxHysNr-rkGtEEFcwZzLhT8hQg8RY3kyQ2a_Jf1cNe2Ta22LQuzO6s54jXrfoLo_W2JnddUHFH5iNtc65JSPEEv-Set38ZhFfh3embgZGI3ioTshwdG4hzk635K_0S510guuYJ6vAXaWpH2GWam2pL5el9lhSN7fK-zcLU5zpWregb8LIbRPqKtgAR101F1wWS0vYOwPfkwkNjTFtuhviFHfownJUPgeBPrRGIxkDBGtNsOwCVV14j7_PPm606ffeuYThqWjtNciaYT6bhi7iYHTaRoHaHy34FVk4u_Mt_AeeXFcfJxGndk6epsQyIvzcB2lLST-uhgUeEdyFIap_RNk92u-JCwK33QJKTlb3QivOXOh7D_CrLtILmF_qcmL1bfbKBwUP7Nm_TdeT2McY8exBY9wVuAxMEoCLqshX0YwkpajdK_V1VmkpclDBiv4dA9T5dlZkSgJvTm8QvRG9xpl4_vtX1snbdlDuTxVn3jxuot8hWGuaJ4nFZtZUsiv5QgFEtH3A130kzNwkwUP8MUlIHSLvxorM3UNsPW4xEAzZVfD-Suwb28vivmVSDHmFoUX1KyxVY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
گل‌اول نروژ به پرتغال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/107831" target="_blank">📅 23:00 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107830">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a8d1f2465c.mp4?token=tdKINE_HGl_cZnDYhGj0-rYRqVHiEAkg8UEqhNvEE8OJszlA1amzy-nKyXD-Pns0qh60dUZ8z2eoD3j3VIjzuDhHGnY7YnfgFlVjUUoC-8aUFVxMO4uOg2_FrKHn5saRRxQEl8_0sBeE5iBUakF-CEyvi5jZY8gt99ku4IBKODikeiHX1RoAocYUAbSBIijUqSbH4I4vY1wl8W4QRwAfsKBYVGOaAGVcGqo5BNHCksm9E7FJFCvWOMJWBBac2ADWFYhA1Akt8Q8Jq-oGchF8U_TeqcqvH6dFPOKGZ6yPYreEXP4mehyKmEcQZSwf0tyiqDeNL25UE7kMt0IQdC95_mWeoDbReWtqe3pBFzfotvIfH-Lhszjazasck5UcI9Q9NVpe87xgyFE2jEVQCVJBrrzaBS5yZdVwQ0TuWz0ZR7tCg2kCNjJFlH_3NSQFRffCTVnTQp1gQn0acytS9Awq9IBJi9-bSxmhr00e9WQ_LQ6qqGeJEV21S5DX9dOC7ijyymDGzdjOmLFKWOFhocpc-iooH4VMcx6jiyAyYdXvbgWslFXC_1XxtVpziayTaGp3KMlsLUIgoA1azsrmSBfWlZ1eyNG8Cr-A_K5OisrVO2YwXMCpyJ_R5CVeWcxeQ--VcIcv1-v7zvigt4Vla4DwdB1MIwdj2ckXKZNotIVRM9c" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a8d1f2465c.mp4?token=tdKINE_HGl_cZnDYhGj0-rYRqVHiEAkg8UEqhNvEE8OJszlA1amzy-nKyXD-Pns0qh60dUZ8z2eoD3j3VIjzuDhHGnY7YnfgFlVjUUoC-8aUFVxMO4uOg2_FrKHn5saRRxQEl8_0sBeE5iBUakF-CEyvi5jZY8gt99ku4IBKODikeiHX1RoAocYUAbSBIijUqSbH4I4vY1wl8W4QRwAfsKBYVGOaAGVcGqo5BNHCksm9E7FJFCvWOMJWBBac2ADWFYhA1Akt8Q8Jq-oGchF8U_TeqcqvH6dFPOKGZ6yPYreEXP4mehyKmEcQZSwf0tyiqDeNL25UE7kMt0IQdC95_mWeoDbReWtqe3pBFzfotvIfH-Lhszjazasck5UcI9Q9NVpe87xgyFE2jEVQCVJBrrzaBS5yZdVwQ0TuWz0ZR7tCg2kCNjJFlH_3NSQFRffCTVnTQp1gQn0acytS9Awq9IBJi9-bSxmhr00e9WQ_LQ6qqGeJEV21S5DX9dOC7ijyymDGzdjOmLFKWOFhocpc-iooH4VMcx6jiyAyYdXvbgWslFXC_1XxtVpziayTaGp3KMlsLUIgoA1azsrmSBfWlZ1eyNG8Cr-A_K5OisrVO2YwXMCpyJ_R5CVeWcxeQ--VcIcv1-v7zvigt4Vla4DwdB1MIwdj2ckXKZNotIVRM9c" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
در مورد شکایت از یاسر آسانی؛
🎙
حدادی: چیزی که عوض داره گله نداره!
🟢
نامه فیفا به استقلال را خواستار شدیم
🟢
مدارکی داریم که بقیه باشگاه‌ها ندارند
🟢
آن سال هم هواداران استقلال قهرمانی آسیا را از ما گرفتند
🟢
رفتن کامنت گذاشتند عیسی محروم شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/107830" target="_blank">📅 21:41 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107829">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f2aee117f1.mp4?token=L4tU7Zl4ri1YxU2dluGIYRPyanGzSDyNC52oxC1u5NCV3jTMg9jdxZZ-dFBBeKFsHsea6EwH4mRHxmVxTIqc25HUD6FViCTM_Vx0hg9nxMReaHD2Kgp_inXav9TrqYvs9BzDNVFIm1EA0CQabD5N5wI0woyTi4VsMgGwB_6PgbfbeXIUIwRN0ToFcfiaPVRmoWU51-fMaHQTk5OahfJUsv0VPVFcsCdKiWoOjTH7lQdwgj2sJB4X8NGNQshLXv74j7w4ZYq3m7DAvxtGbAm93efXvdXsXsOte91lWdvEIaCsk6V8wE9jm0Fz48eodMkVP14k2YnUaWckQd-EiQNUuw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f2aee117f1.mp4?token=L4tU7Zl4ri1YxU2dluGIYRPyanGzSDyNC52oxC1u5NCV3jTMg9jdxZZ-dFBBeKFsHsea6EwH4mRHxmVxTIqc25HUD6FViCTM_Vx0hg9nxMReaHD2Kgp_inXav9TrqYvs9BzDNVFIm1EA0CQabD5N5wI0woyTi4VsMgGwB_6PgbfbeXIUIwRN0ToFcfiaPVRmoWU51-fMaHQTk5OahfJUsv0VPVFcsCdKiWoOjTH7lQdwgj2sJB4X8NGNQshLXv74j7w4ZYq3m7DAvxtGbAm93efXvdXsXsOte91lWdvEIaCsk6V8wE9jm0Fz48eodMkVP14k2YnUaWckQd-EiQNUuw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
👍
🎙
تمجید و حمایت زیدان از رونالدو:
"فکر می‌کنم اتفاقاً باید از کارنامه فوق‌العاده‌اش و کارای استثنایی که انجام داده تقدیر کنیم. اون باعث شد ما جام‌های بی‌نظیری رو ببریم، پس به احترامش کلاهم رو برمی‌دارم."
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/107829" target="_blank">📅 21:35 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107828">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5af8a71f26.mp4?token=K3yj69QzkArxQy-Wnls9TVEFXcFMEP56YepcCyeTatSDBVJVu1if_snsLW59z56l6EyXPq93z5Cq9JnEfuz1E5k0DJm0QLI27KcaaAYxAWpEIo2nt1v9PPzzVVwxfKKDRIbbwvCL2cyuj1Q6dZx3ktgAgqIU6LRd-mIu59znQH7h4FB0fOm5IKEfXknH-sQ55h0QcCJxlUTXBa81EAi_nNOXGvggyxMBZabOxgmckXXTIj2Q5PRkzIvQ3MjYahROmSbMuTeDFCjRf59BA1wGh7nyje8eoik9tFuARHvHQjA6nRn2UKkxFKjbPXiXfzsP780NKmGGC9y6bwY71cuhqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5af8a71f26.mp4?token=K3yj69QzkArxQy-Wnls9TVEFXcFMEP56YepcCyeTatSDBVJVu1if_snsLW59z56l6EyXPq93z5Cq9JnEfuz1E5k0DJm0QLI27KcaaAYxAWpEIo2nt1v9PPzzVVwxfKKDRIbbwvCL2cyuj1Q6dZx3ktgAgqIU6LRd-mIu59znQH7h4FB0fOm5IKEfXknH-sQ55h0QcCJxlUTXBa81EAi_nNOXGvggyxMBZabOxgmckXXTIj2Q5PRkzIvQ3MjYahROmSbMuTeDFCjRf59BA1wGh7nyje8eoik9tFuARHvHQjA6nRn2UKkxFKjbPXiXfzsP780NKmGGC9y6bwY71cuhqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
🎙
پاسخ علی چینی پیشکسوت استقلال به مالک تراکتور: ما از منیریه جام بخریم؟ بیا تهران از نزدیک جام‌ها را لمس کن!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/107828" target="_blank">📅 21:00 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107827">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/56554104cf.mp4?token=Ck8pJ_jdG9618ksKHdPNsx1TY1A2AtWglo9uNTDT6EIorJ7WHbcupR2fSJq0R7jL-u4Kd5fT6hGr6MshBKVteTLslknqsWGifIAkVBklMnPIHyBlOVgZ7fiL_SGiNuGeeyC6hrVMBEouUNsLdYqr7E1f6QtT6MXvI3qMg1sRJwCP8bTd_rvDahNOZxjBNRrgjF7cb0A9YC6kZt8qzYV3oZYvULCYkeJAHXfEZ-1fqHoeNuL-bszXG3-X1ZEPe8VgPSkZJRq-juzAkPVMuk4XJ-Td-cALuPbYUYP8TJ_iUatQOHni8p4WcDQG-ohEqCobFej-Z4P19k035-6IMUHXrQkvaX5TCoh0YDw-OGx60goL1dTzh_lApFVteAlgsZq68qScXbFIbwLRl9Sft2V81P-KZVXi2A4b2nHeRJVVhVUxZiWV-SMgN2Zhe9V0yKykgfxRTfHPN2cb5iWNrUaj4CsGQLCuzg_0ZiqnnOqpqrHPh5aksYBPR0WnWukDjvSMr3ZVHFidQh0LlQCXpz1imTWcMQVMnDpQdiryw6KqnSNSI1qVwoqAnin0R32Hse1pNKr-Yzj3EPNQkF9DbscZphnUsF2oxlqsWYCDQ4M_f0KU8DYv-pviCw4Ha1Gd4Z0nwkg587ltzKEMNoDYyLMqmu4u2rOjHfZNSgJHDSpDfCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/56554104cf.mp4?token=Ck8pJ_jdG9618ksKHdPNsx1TY1A2AtWglo9uNTDT6EIorJ7WHbcupR2fSJq0R7jL-u4Kd5fT6hGr6MshBKVteTLslknqsWGifIAkVBklMnPIHyBlOVgZ7fiL_SGiNuGeeyC6hrVMBEouUNsLdYqr7E1f6QtT6MXvI3qMg1sRJwCP8bTd_rvDahNOZxjBNRrgjF7cb0A9YC6kZt8qzYV3oZYvULCYkeJAHXfEZ-1fqHoeNuL-bszXG3-X1ZEPe8VgPSkZJRq-juzAkPVMuk4XJ-Td-cALuPbYUYP8TJ_iUatQOHni8p4WcDQG-ohEqCobFej-Z4P19k035-6IMUHXrQkvaX5TCoh0YDw-OGx60goL1dTzh_lApFVteAlgsZq68qScXbFIbwLRl9Sft2V81P-KZVXi2A4b2nHeRJVVhVUxZiWV-SMgN2Zhe9V0yKykgfxRTfHPN2cb5iWNrUaj4CsGQLCuzg_0ZiqnnOqpqrHPh5aksYBPR0WnWukDjvSMr3ZVHFidQh0LlQCXpz1imTWcMQVMnDpQdiryw6KqnSNSI1qVwoqAnin0R32Hse1pNKr-Yzj3EPNQkF9DbscZphnUsF2oxlqsWYCDQ4M_f0KU8DYv-pviCw4Ha1Gd4Z0nwkg587ltzKEMNoDYyLMqmu4u2rOjHfZNSgJHDSpDfCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
پیمان حدادی مدیرعامل پرسپولیس: ما زور داشتیم و تورنمنت سه‌جانبه برگزار کردیم. اینکه قهرمان فصل‌گذشته معرفی نشد کاملا منطقی بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/107827" target="_blank">📅 20:41 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107826">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🇮🇷
۸۱ سال گذشت؛ کلیپ ویژه سالروز تاسیس باشگاه استقلال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/107826" target="_blank">📅 20:31 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107825">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aEwz9jgmbvnlFh4V3z0PBDCuy81piVHSRtZ5MPCG7NydvsZTF2D5oON-eT_vn62LTHkUMkl-EryoQH_Hh9IpR7QJ10GDQxZTvo6mARnCwsc6HThfjWMNDpXPqqtEKV9y4jDytNjSgtcWcUnq43kUI_Gu2UBIwjvRYzy5HTUvuTaT-oYQUPPfmrVlplXJf8BZMJAVx1FxLEyCmqTWcYSm8xod9-XsJ--JTfzJICY2Wn2DoKhuSW5cfLDW6Xngc5_UHAy4kGCUiVJ4Bi01ZbCrUZk8E-fOtnPlEtgiSVc_JVEuiQHaAtZ4NnxgOdvSgMA2jTkLrzuYBM7S6bQhj6_BRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
‼️
پیمان‌حدادی: قرارداد اورونوف را تمدید کرده بودیم که بتوانیم بعد از درخشش احتمالی این بازیکن در جام‌جهانی این بازیکن را بفروشیم ولی برنامه‌ریزی موفقی نداشتیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/107825" target="_blank">📅 20:29 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107824">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">‼️
حمید مریخ مدیر برنامه یاسر آسانی و نزدیک به باشگاه استقلال قصد داره که شیرزاد آسانوف هافبک میانی 23 ساله تیم ملی ازبکستان رونیم‌فصل به تیم استقلال بیاره و منتظر تاییدیه بختیاری زاده‌ست.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/107824" target="_blank">📅 20:27 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107823">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50712b5d4b.mp4?token=lUTE04jSwkiCwxpwQZu-vctJbG6Brc_Qk2zN3O7R1sjUDdSu9A0OeM-bcA1B3tE9-7MrE1LC7U6-Qa0srx-RvwheDttavEPSPVZLjpsq83f43Y59o6rtjz5LRZTMynYV_07RAtlKhEHr3ThstEwBUSWzN-TcZkAgQmGkGMSF1QNXACmk1uU0ZRnOlMs84iteumC59m6mDVlikhBAJOeMcfvM3PRkObsYjYkd8hTNYjF6r0wtuyGQ8eG-ooote0RT5PxbCzlcesgqq2ptXjJw-HbHoSTJCg7v5nOd2H1jVTeEEvFY1Mk9T0EGnp9OPcnrS7ucPgwHcnaesBsWWM_kRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50712b5d4b.mp4?token=lUTE04jSwkiCwxpwQZu-vctJbG6Brc_Qk2zN3O7R1sjUDdSu9A0OeM-bcA1B3tE9-7MrE1LC7U6-Qa0srx-RvwheDttavEPSPVZLjpsq83f43Y59o6rtjz5LRZTMynYV_07RAtlKhEHr3ThstEwBUSWzN-TcZkAgQmGkGMSF1QNXACmk1uU0ZRnOlMs84iteumC59m6mDVlikhBAJOeMcfvM3PRkObsYjYkd8hTNYjF6r0wtuyGQ8eG-ooote0RT5PxbCzlcesgqq2ptXjJw-HbHoSTJCg7v5nOd2H1jVTeEEvFY1Mk9T0EGnp9OPcnrS7ucPgwHcnaesBsWWM_kRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
پیمان
حدادی مدیرعامل پرسپولیس: قرارداد 5 بازیکن خارجی ما 4 میلیون و 80 هزار دلار است
🔴
در نیم فصل و تابستان بعدی بازیکن خارجی نخواهیم گرفت. ابتدای فصل بخاطر همین کادر ایرانی گرفتیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/107823" target="_blank">📅 20:12 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107822">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65b6b0e4ee.mp4?token=VB6NEN8OLY4FEKIPtx9M9x2a9a8iMqViMcEHypFNI5ST5lphzl9QSDn5B1b1nXV8FEpBVA415vEiQb2Wm4gOl-kKhJZEBDhcMcuMk5l_1QppBnKPyjc_DRU06CIijNHTWOLN5wH8UAaGPAvLWW7St5FF_K_KWbq6N5AGKJ2YR-OdvyDbjXKr4fxgFnbGXX7k9SbI0D2yk_fYJ94mTnaRLUH8eNHc66mBNIc-4vF9WPjDnfC5xchAZS8JlhYfFf17UEQRYYMhgeJkqhT8heJgMKIgTtMr1kp54ePVW2hmUuBAs1B_zg-aKRT1QYlX8mgx8WhSzLxziVli7IuiBFCpMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65b6b0e4ee.mp4?token=VB6NEN8OLY4FEKIPtx9M9x2a9a8iMqViMcEHypFNI5ST5lphzl9QSDn5B1b1nXV8FEpBVA415vEiQb2Wm4gOl-kKhJZEBDhcMcuMk5l_1QppBnKPyjc_DRU06CIijNHTWOLN5wH8UAaGPAvLWW7St5FF_K_KWbq6N5AGKJ2YR-OdvyDbjXKr4fxgFnbGXX7k9SbI0D2yk_fYJ94mTnaRLUH8eNHc66mBNIc-4vF9WPjDnfC5xchAZS8JlhYfFf17UEQRYYMhgeJkqhT8heJgMKIgTtMr1kp54ePVW2hmUuBAs1B_zg-aKRT1QYlX8mgx8WhSzLxziVli7IuiBFCpMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
‏همسر
بیژن مرتضوی: تو مجازی به آقا بیژن فحش میدید ولی تو واقعیت دنبال عکس و امضا هستید!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/107822" target="_blank">📅 20:04 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107821">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fe589a60ed.mp4?token=PyrAH-JTqZq18jEvQKaBw80uiJ6Uk7_YX3ZgK8nFCFpeiT2MQu6CnkzIGClwO0omLlMNqAIIRMFrvf_DADYmqKYfEzrcd7Rf1XYiMLlFDwZgbk54bLRLB2p7q91lmVxYbQAXpwhJ7mf1E4xkDR1pOE4drc1pkjwP1NbCzcfg5VPGmTqC2G_vOiECDEWKEbCw_tY3GHlcNzbYR87ANFhDxFEigThhHtYRFpPx746DIBkafzbz2umxY8oh7pePymkJFvllpWk-jsLrqapXZ4r4oi-f1EGWIFWa0JBtIVGbg4y0fcfV1wCarifO3RLnUY_oNd7rdGQXu3tvEi2CET82lQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fe589a60ed.mp4?token=PyrAH-JTqZq18jEvQKaBw80uiJ6Uk7_YX3ZgK8nFCFpeiT2MQu6CnkzIGClwO0omLlMNqAIIRMFrvf_DADYmqKYfEzrcd7Rf1XYiMLlFDwZgbk54bLRLB2p7q91lmVxYbQAXpwhJ7mf1E4xkDR1pOE4drc1pkjwP1NbCzcfg5VPGmTqC2G_vOiECDEWKEbCw_tY3GHlcNzbYR87ANFhDxFEigThhHtYRFpPx746DIBkafzbz2umxY8oh7pePymkJFvllpWk-jsLrqapXZ4r4oi-f1EGWIFWa0JBtIVGbg4y0fcfV1wCarifO3RLnUY_oNd7rdGQXu3tvEi2CET82lQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
اقدام تلافی‌جویانه امید عالیشاه برابر خداداد
😆
😆
😆
😆
😆
😆
😆
😆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/107821" target="_blank">📅 19:33 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107820">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6340210c7d.mp4?token=qAxx7mpeWkA_hxQ695TV_N9cBoEj36b7pxKDLdmG9Bn8rtL0ox_IICQJDbqmyjDu05JlcDvD8rBEuydrpN9Yik6KkDlbe5PJnl_tPdmH77DG5GMtsulDDuKwLOPzgN0a9CPCrNd_ehkVUM9wq9_ZJsqTYNXL0IYMTpBldu0joy_kK8FvgMvdr85TcHdCpE2wKrcVfhsAG0-g2PQGo6riE4_teRAUGwHhdmJnUCTiLO7hsD4jUJg_IYLa39CkOJdLrOLw2mhVZdUpG_CzMHa446SzQ8lN9JCB-dFNa4i-VzoSp62PpMmQFguUuCniQB3PkxU2WbOYvSYQCs7s0eY67w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6340210c7d.mp4?token=qAxx7mpeWkA_hxQ695TV_N9cBoEj36b7pxKDLdmG9Bn8rtL0ox_IICQJDbqmyjDu05JlcDvD8rBEuydrpN9Yik6KkDlbe5PJnl_tPdmH77DG5GMtsulDDuKwLOPzgN0a9CPCrNd_ehkVUM9wq9_ZJsqTYNXL0IYMTpBldu0joy_kK8FvgMvdr85TcHdCpE2wKrcVfhsAG0-g2PQGo6riE4_teRAUGwHhdmJnUCTiLO7hsD4jUJg_IYLa39CkOJdLrOLw2mhVZdUpG_CzMHa446SzQ8lN9JCB-dFNa4i-VzoSp62PpMmQFguUuCniQB3PkxU2WbOYvSYQCs7s0eY67w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
👤
مهدی مهدوی‌کیا در واکنش به اتفاقی که برای کریستیانو رونالدو در تیم ملی پرتغال افتاد گفت:
🔹
«وقتی این خبر رو خوندم واقعاً ناراحت شدم؛ یک ابرستاره مثل رونالدو شایسته چنین رفتاری نیست. کسی که سال‌ها برای تیم ملی پرتغال همه‌چیزش رو گذاشت و یکی از مهم‌ترین چهره‌های تاریخ این تیم بود، حالا به جایی رسیده که اردو رو ترک می‌کنه. به نظرم باید احترام بیشتری برای بازیکنی با این سابقه و جایگاه قائل بود.»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/107820" target="_blank">📅 19:13 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107819">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ae14913e57.mp4?token=GGb-E33evMjekm79k38DXkfJNHfWJJ9nm69M6dQGLH7w5XhSwFfRHiFvGn7cNo9GzFnd-FaqlvULggJnB3vQACAs2qmNxhxSeLn3cRcrmbebIVOku-dvVDV2kJF9q4QR4U0RCmKf14aioVSr-0km6xbcVcC_mXjik0Tdk9J5J-H46QEwrB0i0Pci1u-4Po362XMT-eQdL98SNdJD2EVQbCw8yArhtqTkepl39KU2g9PDtk0ZIEgJ08kl5owsv1m8YMTW64rN-GqQSLMaUksJjIVWPFWeJdGMmmyyxeKSTnhNa5BTqKe04v6gM_NYgC8dRG-N861-3HzVp0BKge3LsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ae14913e57.mp4?token=GGb-E33evMjekm79k38DXkfJNHfWJJ9nm69M6dQGLH7w5XhSwFfRHiFvGn7cNo9GzFnd-FaqlvULggJnB3vQACAs2qmNxhxSeLn3cRcrmbebIVOku-dvVDV2kJF9q4QR4U0RCmKf14aioVSr-0km6xbcVcC_mXjik0Tdk9J5J-H46QEwrB0i0Pci1u-4Po362XMT-eQdL98SNdJD2EVQbCw8yArhtqTkepl39KU2g9PDtk0ZIEgJ08kl5owsv1m8YMTW64rN-GqQSLMaUksJjIVWPFWeJdGMmmyyxeKSTnhNa5BTqKe04v6gM_NYgC8dRG-N861-3HzVp0BKge3LsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇮🇷
💙
فتاحی رئیس سازمان فوتبال باشگاه استقلال: نمی دانم پرسپولیسی‌ها علیه یاسر آسانی چه مستندانی دارند/ وقتی باشگاه السد قطر با آن تیم حقوقی قوی که دارد از باشگاه استقلال شکایت نمی کند یعنی حضور یاسر آسانی هیچ مشکلی نداشته است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/107819" target="_blank">📅 19:02 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107818">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/70613f964d.mp4?token=Ouss_MTDeAi5zOxIE_spYlxBzltlpefQOTFIlBHme3tfgg-X176oBrD9QJx91PyZ7Y66kdpJ892VHezT2K38vksYOPbE0QKUTtyfy1QN2yFTQGymk9B6DnYiVpxv_XQ2YWIYcrrJbHfJOc2MbxsgPpgxK4pSGAxkgYGwwkg0OqDRs-vnsKfPH5MxscqX4IIgu1mnvEBVEq2t7rNl4VO5ys-7bRXuN6cc98FpNpg8eSj6jsKM7r99BD9t-bG9sgDNzpbEWV7pL7oK7eizKFYeBi0iMEzlZyPk5sxBweyyIanBFMXuqfRIvDzblatykzU8DtBazIQ9dAcMREF6xe1YNYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/70613f964d.mp4?token=Ouss_MTDeAi5zOxIE_spYlxBzltlpefQOTFIlBHme3tfgg-X176oBrD9QJx91PyZ7Y66kdpJ892VHezT2K38vksYOPbE0QKUTtyfy1QN2yFTQGymk9B6DnYiVpxv_XQ2YWIYcrrJbHfJOc2MbxsgPpgxK4pSGAxkgYGwwkg0OqDRs-vnsKfPH5MxscqX4IIgu1mnvEBVEq2t7rNl4VO5ys-7bRXuN6cc98FpNpg8eSj6jsKM7r99BD9t-bG9sgDNzpbEWV7pL7oK7eizKFYeBi0iMEzlZyPk5sxBweyyIanBFMXuqfRIvDzblatykzU8DtBazIQ9dAcMREF6xe1YNYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صحبت‌های امیرحسین صادقی بازیکن اسبق استقلال و تیم‌ملی درباره وضعیت وخیم اقتصادی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/107818" target="_blank">📅 18:34 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107817">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf836fb3bd.mp4?token=BtpuhD6dzMLpSBWsVAr9e3BO9YNEdN-h3jZYxXmiZfmkrCGD058LWMfRvowBnZJARp69mieF5E1PbBw92VQ-oqYqbI4rDOTnwYnh4fUCkgeEBgMijvyLY05lQPu9pDRAFQUlYVE8w_yIZGcbThvRcGcnnUEc38sP3Fi-ezJpzpyIiqPVbvUnJcvVMcxZ8muG1_fm9ZsHWzpMGG7GnGzHzlrIldGfkHcHWAKDlYd5G9y3E3Atwu8fCyrudmgxuqBIJRZuFOyl9jUx5xpASqxYNKgYa5ol7sclTPu0QrPF1aR5HtLNuznhVdYW3j8Z-tkJMdF79kqxBhp2vVTZotXr7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf836fb3bd.mp4?token=BtpuhD6dzMLpSBWsVAr9e3BO9YNEdN-h3jZYxXmiZfmkrCGD058LWMfRvowBnZJARp69mieF5E1PbBw92VQ-oqYqbI4rDOTnwYnh4fUCkgeEBgMijvyLY05lQPu9pDRAFQUlYVE8w_yIZGcbThvRcGcnnUEc38sP3Fi-ezJpzpyIiqPVbvUnJcvVMcxZ8muG1_fm9ZsHWzpMGG7GnGzHzlrIldGfkHcHWAKDlYd5G9y3E3Atwu8fCyrudmgxuqBIJRZuFOyl9jUx5xpASqxYNKgYa5ol7sclTPu0QrPF1aR5HtLNuznhVdYW3j8Z-tkJMdF79kqxBhp2vVTZotXr7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🔴
فریادهای عجیب یه نماینده مجلس جلو قالیباف به همتی رئیس بانک‌مرکزی: به والله میرم خودمو جلو بانک مرکزی آتیش میزنم
!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/107817" target="_blank">📅 18:20 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107816">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eAx4eMUnhUOSv87OUL4yBNYje-UrdRIOZD9-lpsNobozqotmM7bw2lTG3CcHpUPTIQ-L6pMqj0MCbddZR4gHy9OcfRhQ1mC2aBE6IJW2FzP39iOHr549195kvoYCQJU0lvXIgliX1YMHG4yvVIq20s32Xu535vG3lsjwJHQ6DUnGQ3kfHeED_266eq3Kmlu7x-WIGAC25wpAxFanxUj3ZOfDlLkBwps4Yyw8rr_ugQrmltnZQE6YhXaCyfYBJYTAIXutCT28YafTbeVCEkSQyjis0iX75F9jeE5EpVMuk4jUxsiBtMUewq71fVNjaMyRSBhJfIeLloQ2W6k4yrJy5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇵🇹
فدراسیون فوتبال پرتغال قصد داره برای فیفادی بعدی یک بازی ویژه خداحافظی با اسطوره کریس‌رونالدو مشابه اقدام آرژانتین برای لیونل‌مسی تدارک ببینه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/107816" target="_blank">📅 18:06 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107815">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d0576436f6.mp4?token=SviMOvnfht2ZFvwcMOex3AbyF0f9YXuf95AYS5q4ycf8BqcG3HKIMfplyfHV0ZfJLbdYa4thLLNRyrsFqxoG5vHwfgIi7zMIVaFHCsSaL1Y4Jti9QGRjrvc3W6g9fNdnfl-mYkB_lKELGzc1Phhhw4zXi-roZLFD5jmqGvLAXHYqcNjwSldQW-QzhhFfYFBHWf2_uEQPZHwGu1RSgLiVi8kOQNZ1b2Itf1itqQX-y-8s60n1Ti3NhhRqiihEeAsLiR224xXud8D2b0ucBes5AibzG6NJDGcO-BVgQE4PF5NCB2kXHHahv1Vpc1BIwHP_ZJmg09OZfzpoE1a5SyXdZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d0576436f6.mp4?token=SviMOvnfht2ZFvwcMOex3AbyF0f9YXuf95AYS5q4ycf8BqcG3HKIMfplyfHV0ZfJLbdYa4thLLNRyrsFqxoG5vHwfgIi7zMIVaFHCsSaL1Y4Jti9QGRjrvc3W6g9fNdnfl-mYkB_lKELGzc1Phhhw4zXi-roZLFD5jmqGvLAXHYqcNjwSldQW-QzhhFfYFBHWf2_uEQPZHwGu1RSgLiVi8kOQNZ1b2Itf1itqQX-y-8s60n1Ti3NhhRqiihEeAsLiR224xXud8D2b0ucBes5AibzG6NJDGcO-BVgQE4PF5NCB2kXHHahv1Vpc1BIwHP_ZJmg09OZfzpoE1a5SyXdZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
⚽️
مهدی مهدوی‌کیا اسطوره فوتبال ایران در حمایت از مهدی قایدی گفت:
🔹
هر بازیکنی حق داره بگه بهترین مربی‌ای که باهاش کار کرده چه کسی بوده. اینکه به خاطر چنین مسئله‌ای یک بازیکن رو به تیم ملی دعوت نکنیم، واقعاً نمی‌دونم چی بگم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/107815" target="_blank">📅 17:58 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107814">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/107814" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/107814" target="_blank">📅 17:58 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107813">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uXpl0Z7zG2cYdlZljeIsb4LtIdXwLw8d0MjcEpZOcaOa-1C3yy4eRC5sTChsdA43W4N_Tk04JmokkLh7QVaYEBdK14FYR70VFJ2-CKXHuDbGpTQyTfz5rdqJDMk0ZUk0fbkZm-BlHRft1gy0HKdVfdTH55tAPGZlOf-O0RGqNQ6cQLg5NZuKI7U3voJ3DsIYsB7kFgqXR08w5l9h79DRjtFgjRTpm9tjqdP4c8sK6Avvvo8wF_smMDOcm8v6ix52Q5joGiacvX1VN3-gzbafgk1nRawTt9VK4ieZF-wdgEot3jlBIuuLi7vg2uCeNkdP1QNj2r1c3wqsnKsXWpmSNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤩
نبرد هیجان انگیز نروژ
🆚
پرتغال را در
TrexBet
پیش بینی کنید!
📉
نگاهی به آمار ۵ بازی اخیر دو تیم:
نروژ: ۲ برد، ۳ شکست و ۸ گل زده
پرتغال: ۴ برد، ۱ شکست و ۹ گل زده
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/107813" target="_blank">📅 17:58 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107812">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZoYm9cciw4i34eromTVjBtphGqk8H904MnjXRDxdnXXr6lN3-6ucE1aM7EWYiIgNRUyHKxH5IxQR0l7LnhQyj-l22TumU1yCHnQediMuQtEDAfuKPFKa3mTQJKfelOBV7Urea7KhPVbK-IyutwKhazAX325HYFQ0dHT9XBmdpgVbVim73u0yLrBns6tbGwhM0ckJRfnvO0wy2aIBUlkDUdZeL9qimHq8SBGUUckcpqULkiLFo6UkMD2XYC3JD1DWKfdKMYnOhJkAs_i9A-4hpns4u96iO_HojeXUGPWcuywP73BGUcWRhRhJh_MLyxf_2itGyhGo_leYEpOIjBpqrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
⚽️
براساس گزارش منابع خبری، یحیی گل‌محمدی سرمربی فعلی دهوک عراق قرارداد خود را با این تیم فسخ کرده و در آستانه حضور روی نيمکت تیم‌ملی امید قرار دارد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/107812" target="_blank">📅 17:43 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107811">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OKeg4fYLtIRMCAx_yYCyKVtkEFg0PKonXQ0KD0Qy2HCZcTMJO3TdmuLDGULNVQvQDnzDHsZsm8l2C8cgXcGxtWL2WLanQh94eTPmEJhGBoWcnL3bO2JXaHwE1b5gZH2CC7AJHOSJvMhOrvLPmI8Nl8dw0m0J9mQADe_2S-oalWikUkAbz6GmdhNC_V0Sicx-ObWYZXQKKWuxuGirUp40gqJQWATIDjL77hBb4ARWElXT3EnuvvMKyAMejEie8uAYlHqaAtiJW2LfvQeTk4lCU0m8-ppkg9kkWEi7vFBj3bptbkmihkp1Kww2gLcZt3Leduerg8L4Ez2lw9NhKwV4Hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇪🇸
مارکا: اندریک از نیمکت‌نشینی‌های مداوم توسط مورینیو ناراحته و میخواد ژانویه مجددا به صورت قرضی از رئال‌مادرید جدا بشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/107811" target="_blank">📅 17:30 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107810">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">‼️
⚽️
لحظات تلخ احسان حاج‌صفی در تیم ملی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/107810" target="_blank">📅 17:20 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107809">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0177fa0248.mp4?token=WhWAShnEqecAf44R57IT-mQO1_R8yt0uXoqp4Y9ERbKHLq-72uJIHAq1w1ySdcuOGM_CPnGWqVMOfu7DcR4hQO_tCM9GGQIYZ6PNLBkNo1cGPjmr7iEBimfNy_dwBxBFPOMbyknbW54C_7o5ntADWzV0LnItc46d38HHxMvMii1VOzN3bGVtpAJPvZ2nkhuKBaItR9dgOmbPVkXFsorctGkh38f8eh9QsPg0nVW2Mi7MF5Nu1Ibp1Bn9oFxnHpKzdXNqPP-fM_Un_xDj3atVSspRqZkJkXNqRRViWnorTGNF-Q7wRSYeh6ESAv0dUCEMTtUvT7Qk3BY66dqQx_6MWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0177fa0248.mp4?token=WhWAShnEqecAf44R57IT-mQO1_R8yt0uXoqp4Y9ERbKHLq-72uJIHAq1w1ySdcuOGM_CPnGWqVMOfu7DcR4hQO_tCM9GGQIYZ6PNLBkNo1cGPjmr7iEBimfNy_dwBxBFPOMbyknbW54C_7o5ntADWzV0LnItc46d38HHxMvMii1VOzN3bGVtpAJPvZ2nkhuKBaItR9dgOmbPVkXFsorctGkh38f8eh9QsPg0nVW2Mi7MF5Nu1Ibp1Bn9oFxnHpKzdXNqPP-fM_Un_xDj3atVSspRqZkJkXNqRRViWnorTGNF-Q7wRSYeh6ESAv0dUCEMTtUvT7Qk3BY66dqQx_6MWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
🎙
⚽️
علی‌فتح‌الله‌زاده مدیرعامل سابق استقلال: قلعه‌نویی نتیجه نمی‌گیره؛ من بودم عوضش می‌کردم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/107809" target="_blank">📅 16:55 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107808">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e1845ed89.mp4?token=pob62bpGZ0IV71IkAMbQhswfcthBUsVhqRCJ8k_fOz5aXzn9N6PgS5VuRuKKw37dy5Ta-HaXsJ7ScBuCoS53ndKqUrHc5OrigaObynxRHHQdzwOHH5uhW1r5YVjNFtM3c4jCdnofmFmiPFSUAewEFqXdb8QEsiShP3FO9-LbE92twjiu-Ce11W8rY07TSqGm1O_KOwuo5KBPYBfkINyxSnDMp9grBuLwEx-OMDc44QGkOh0YF65NUFOxLub-gdKMft7akLHrs2Ib1D9X1cpPLvhLaC75qMrnt2YY-Nm0b0RhSWU1IpKHjC7TW6d_ufgCAoFgMGHziO2-9ZLZRm3SDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e1845ed89.mp4?token=pob62bpGZ0IV71IkAMbQhswfcthBUsVhqRCJ8k_fOz5aXzn9N6PgS5VuRuKKw37dy5Ta-HaXsJ7ScBuCoS53ndKqUrHc5OrigaObynxRHHQdzwOHH5uhW1r5YVjNFtM3c4jCdnofmFmiPFSUAewEFqXdb8QEsiShP3FO9-LbE92twjiu-Ce11W8rY07TSqGm1O_KOwuo5KBPYBfkINyxSnDMp9grBuLwEx-OMDc44QGkOh0YF65NUFOxLub-gdKMft7akLHrs2Ib1D9X1cpPLvhLaC75qMrnt2YY-Nm0b0RhSWU1IpKHjC7TW6d_ufgCAoFgMGHziO2-9ZLZRm3SDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
🇮🇷
میثاقی: فیفا دی سوم چیشد؟ اگر قرار نبود بازی کنید حداقل لیگ را برگزار می کردید!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/107808" target="_blank">📅 16:32 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107807">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63df69c40a.mp4?token=VDmZRICmmq2o_A_o7fdyQAyj_lVnnyR72-ioUtimF5vLoKxM_Aouzcv2744TRO_rqF-O4S292TiK3-1-JtvlyN4gOY7pKzlQ6KvxD6H21aRdTgFu2s2r1lW9VbLKuJfjriEXukyenpas4Cp6W8BbAAcTg2y1JR_fDxG0ArhFsFL22qn5L1lRVTMfwo4PF1WjzdIqketFuzdF0aZxaB8dspoq15srr2jEi3sxqs3PSMw9C1wjeJy_oMD7CnlYwdtQVe8Dkt1BEJKE2EhLCFmRSJa_b6SbrVtMRnETS3Xdqph4qpojwXSNCT0anM4-2Ir-lapy3i6fxYdNWBXm0r6M4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63df69c40a.mp4?token=VDmZRICmmq2o_A_o7fdyQAyj_lVnnyR72-ioUtimF5vLoKxM_Aouzcv2744TRO_rqF-O4S292TiK3-1-JtvlyN4gOY7pKzlQ6KvxD6H21aRdTgFu2s2r1lW9VbLKuJfjriEXukyenpas4Cp6W8BbAAcTg2y1JR_fDxG0ArhFsFL22qn5L1lRVTMfwo4PF1WjzdIqketFuzdF0aZxaB8dspoq15srr2jEi3sxqs3PSMw9C1wjeJy_oMD7CnlYwdtQVe8Dkt1BEJKE2EhLCFmRSJa_b6SbrVtMRnETS3Xdqph4qpojwXSNCT0anM4-2Ir-lapy3i6fxYdNWBXm0r6M4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
رسول‌مهربانی مجری دلقک و گزارشگر صداوسیما که با این الفاظ دیروز جنجالی شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/107807" target="_blank">📅 16:05 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107806">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3dc22c75d3.mp4?token=bgF2xxQSqqNmxB5acmHFe6u65ceBvP8rgtUI3pFc0V5kF-90N0ugZivwB0Bev1fCX_sd0im5LiglPrrqH4Ljd_2mNGXFOqlZ86_TdCVDudpNuT5VqMCEGu6eGHLkE7Ikb7GgFz65okUBAUzV9RCHitNX8lSo4XbF9Mx4x9KPwh7BFnr3KIOwGEo2JtS5im_ZJSBSiZl-haDUBFVm7SJU106mw1yOOK6tL_fr0xCv1wr_dEfutp80ZMg6Nm7aoF1ZJkc2q1xv3Yxy70Qyw4KobxNOxnaAp_ogoMHoGhkBLHjihsFhOndo6GDo1BHDys24bc-0jGjNnPuhjhEB94kIMw2rMJTURWDSMDsWEG4KS9jBZCfVcy99pU7ut4KpcrMOGDv68wRdSxSAJo8lf6EQnyZFcorSH1x7lkptsxxkMwG4fPyKRP79dflCiq3M6rvT5mgCw-AvGLRL_NpC9b2-vWYlqbKakCHjaS4n-wLQmmRFTzRLtg-fOH8AmoAEc_Xt1Y8TczHxNuJhnDBb2NcBkPN3Zx6dGzEF_csMHeZ8D6AR4hbOmCyGwu1NihriuyL26mlBcGDMhs7Oy4o4aHrJVaAOkbmwM4b_xYIw37enDN-hmowA0BGyrZvGspCMTj-9F7MczsiQcmPzpgpqHJPeoqfqvxQqPjRcAXc03bgF1k8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3dc22c75d3.mp4?token=bgF2xxQSqqNmxB5acmHFe6u65ceBvP8rgtUI3pFc0V5kF-90N0ugZivwB0Bev1fCX_sd0im5LiglPrrqH4Ljd_2mNGXFOqlZ86_TdCVDudpNuT5VqMCEGu6eGHLkE7Ikb7GgFz65okUBAUzV9RCHitNX8lSo4XbF9Mx4x9KPwh7BFnr3KIOwGEo2JtS5im_ZJSBSiZl-haDUBFVm7SJU106mw1yOOK6tL_fr0xCv1wr_dEfutp80ZMg6Nm7aoF1ZJkc2q1xv3Yxy70Qyw4KobxNOxnaAp_ogoMHoGhkBLHjihsFhOndo6GDo1BHDys24bc-0jGjNnPuhjhEB94kIMw2rMJTURWDSMDsWEG4KS9jBZCfVcy99pU7ut4KpcrMOGDv68wRdSxSAJo8lf6EQnyZFcorSH1x7lkptsxxkMwG4fPyKRP79dflCiq3M6rvT5mgCw-AvGLRL_NpC9b2-vWYlqbKakCHjaS4n-wLQmmRFTzRLtg-fOH8AmoAEc_Xt1Y8TczHxNuJhnDBb2NcBkPN3Zx6dGzEF_csMHeZ8D6AR4hbOmCyGwu1NihriuyL26mlBcGDMhs7Oy4o4aHrJVaAOkbmwM4b_xYIw37enDN-hmowA0BGyrZvGspCMTj-9F7MczsiQcmPzpgpqHJPeoqfqvxQqPjRcAXc03bgF1k8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
👀
🙂
بازگشت سردار آزمون به تیم ملی بعد از مدت‌ها با کمک متن هوش‌مصنوعی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/107806" target="_blank">📅 15:40 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107805">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ab5019276.mp4?token=XVjltgvgHLnWK1BbobaQZDovf_TJXS2VjSRhdlkQz-bDnxWfQ3yQmGVtUdNyzsTFvPbN0vB46PiNHbCBo-0bD9K8kuIcEfF_uBonSRjE39wmTnqsBBwrJZ_4C457iQCYfJOzTdQqKs59K3QTYpOZqai6LeqsgEpJ2b-xwy4u5N_UnmjUmVQPGadKSYobeXwZfRk16iV71JbacNQ__ylXp4NTagtEFMQ2nOfg7gVNczYwXWmFu8_zdEhCJf7EbGbS5c6HsV_8AFn8Nnp7Aj7A7vF0cCX8B9KcpaQBlEt9ddHbl6z6EVi8tsPCojXN37BsocbvOlvzR0dldoljhMHjaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ab5019276.mp4?token=XVjltgvgHLnWK1BbobaQZDovf_TJXS2VjSRhdlkQz-bDnxWfQ3yQmGVtUdNyzsTFvPbN0vB46PiNHbCBo-0bD9K8kuIcEfF_uBonSRjE39wmTnqsBBwrJZ_4C457iQCYfJOzTdQqKs59K3QTYpOZqai6LeqsgEpJ2b-xwy4u5N_UnmjUmVQPGadKSYobeXwZfRk16iV71JbacNQ__ylXp4NTagtEFMQ2nOfg7gVNczYwXWmFu8_zdEhCJf7EbGbS5c6HsV_8AFn8Nnp7Aj7A7vF0cCX8B9KcpaQBlEt9ddHbl6z6EVi8tsPCojXN37BsocbvOlvzR0dldoljhMHjaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
▶️
ویدیو وایرال شده از شادی رتبه ۲ و ۶ کنکور در حین اعلام نتایج کنکور سراسری
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/107805" target="_blank">📅 15:15 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107804">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/49b154fa09.mp4?token=WO3RyGuFVQPYOs9TKfZhIrdtuS4nFvo9F1QCvDNd9Y-hj3xHMSSwXM4hG0mxBuOIqXB96mngCYyihtLhLTiJBENhgRQQW3j7JPV2zOXYSiXDS87BVOgCWtQrLh0OaMSeUvuaK7x1iMqR42ZJsT0TuNZMwqEtyhLH3r0Hn7jPBzSfyvHnPRa-YIBjkKGPO3Telm41QUGYVqvpUW0Ykqqwsc_fvweIYgz3uwl_ibxHrajpziZKGdfp-5IQR_g1WkQAaf-5S_OFv2fOi_ra7ZYlz2P0_FKrdgD_BhkOQ8StCYfQ7hU7Fg037mRVQkA9EoKmzGzt1BuJQiPwO3BDZv5jPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/49b154fa09.mp4?token=WO3RyGuFVQPYOs9TKfZhIrdtuS4nFvo9F1QCvDNd9Y-hj3xHMSSwXM4hG0mxBuOIqXB96mngCYyihtLhLTiJBENhgRQQW3j7JPV2zOXYSiXDS87BVOgCWtQrLh0OaMSeUvuaK7x1iMqR42ZJsT0TuNZMwqEtyhLH3r0Hn7jPBzSfyvHnPRa-YIBjkKGPO3Telm41QUGYVqvpUW0Ykqqwsc_fvweIYgz3uwl_ibxHrajpziZKGdfp-5IQR_g1WkQAaf-5S_OFv2fOi_ra7ZYlz2P0_FKrdgD_BhkOQ8StCYfQ7hU7Fg037mRVQkA9EoKmzGzt1BuJQiPwO3BDZv5jPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
👤
👤
مشاور قالیباف رئیس مجلس:‌ تا به عادل فردوسی‌پور تذکر دادم، مطلب حمایت از علی کریمی را حذف کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/107804" target="_blank">📅 14:50 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107803">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HkZPpc4RqtUkXhsiJn3Ncb2um3NxfHJnvLR_T9z1JAajGpTSgyEw5qJ4NdpmAFyY4a2lQmUQsJdoqdnq5UrSaS4sP527M2-txXJVbhK7rRQREXzTud5NLGw-CHTy38SbkQlT0c_fN47h5M4WKmU-CpwRnapeOVDL7H1ftiBFhP3uSJAcHkco-QukNp8iwxK16qnJcwTsBJw7-msE_gsG3ZUWqbe8igPmljjWKkpVwHvDyG7VXW3WoRnwRo2cFwvmE1J-Zfml2IP8jj8eAju-AY0MdQlsIfaU04ApkTWC-HseTRB_wUjE4VTOUTny91NOGBryFVk5LJrTbpYmbh6kXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇹🇷
وضعیت وخیم ترکیه در لیگ‌ملت‌های اروپا؛ بازی بعدیشون جلو ایتالیا هست که آردا گولر بدلیل دریافت اخطار محرومه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/107803" target="_blank">📅 14:25 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107802">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e464e1d963.mp4?token=JuMJMubvmVS9TxdFxopleCwt6vBIhWs2CFhdNu02bGUlgQ8IIl9_r5Lkmj_PRbtLbcouh07FszIjvN-agnyF2CXieqLG79U2dXcW9QHjSEvZpQR4BwX2vzjutwkjchT4kNYGnTdsJSEyawvCgA7SZgiOCkZP-DM7Pv1VsY6YcFy8ghXltmu5YzO6JGDdDhSG9QuPXsjuI4sM9AgfR6IauIbos4n2a0179nTXBET3wf3A6x9NTF7C_ixIKXOxrJ-pHtbe0y0BoxiWQN8VKM1YQiAYogyfnHOkeXKRkCmQdCvdqVqZd10DybpdtY9tvK-fhYJTP2KM5lP2wDbBBBUwFXyNQMN-Y5dlmKQ7Vxq6egp-RnrQqHZERGCLmA2QMjzdIrxljn_EvfsgGYCl0grXv6FQGdk84r4WypaH0AZ-ZbctoTH1toPB1n2rMdVwi15vq4UF5TFNwSb5gnnK8zWCAsPu6HsqxCFPgoas0Rhh5wAz6XoKEMTcnpakuOr7myP_9YDNFGZXwiYYI9t9yNv_JATpg6MFaMB1XzDSyXQ9fU8SodP5YKv9zHX55MGwrwFhYDtNMMfCXLPJgQYpBr1kudvJO5WEtw-TYA8LoFGwnRS409t0OZ6wQTtv1PT8pvh10RLxBRnlWsapQXhjhXHU5_yP1UhvdKue5KfKLUAnn_o" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e464e1d963.mp4?token=JuMJMubvmVS9TxdFxopleCwt6vBIhWs2CFhdNu02bGUlgQ8IIl9_r5Lkmj_PRbtLbcouh07FszIjvN-agnyF2CXieqLG79U2dXcW9QHjSEvZpQR4BwX2vzjutwkjchT4kNYGnTdsJSEyawvCgA7SZgiOCkZP-DM7Pv1VsY6YcFy8ghXltmu5YzO6JGDdDhSG9QuPXsjuI4sM9AgfR6IauIbos4n2a0179nTXBET3wf3A6x9NTF7C_ixIKXOxrJ-pHtbe0y0BoxiWQN8VKM1YQiAYogyfnHOkeXKRkCmQdCvdqVqZd10DybpdtY9tvK-fhYJTP2KM5lP2wDbBBBUwFXyNQMN-Y5dlmKQ7Vxq6egp-RnrQqHZERGCLmA2QMjzdIrxljn_EvfsgGYCl0grXv6FQGdk84r4WypaH0AZ-ZbctoTH1toPB1n2rMdVwi15vq4UF5TFNwSb5gnnK8zWCAsPu6HsqxCFPgoas0Rhh5wAz6XoKEMTcnpakuOr7myP_9YDNFGZXwiYYI9t9yNv_JATpg6MFaMB1XzDSyXQ9fU8SodP5YKv9zHX55MGwrwFhYDtNMMfCXLPJgQYpBr1kudvJO5WEtw-TYA8LoFGwnRS409t0OZ6wQTtv1PT8pvh10RLxBRnlWsapQXhjhXHU5_yP1UhvdKue5KfKLUAnn_o" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
حضور بیژن مرتضوی و همسرش در دربند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/107802" target="_blank">📅 14:10 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107801">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/82e592cb76.mp4?token=qM1PHrco89ixWHvfQ-J0SS73eZnX1_QStGe6Q7K8bLPQwxW_TlblaxqPuFW17C7VDwL6SeREDVvOQwn4geDfI05Hf0nomQ7elukKBV1qvm7NcAuS1iEiDlGi-kXUGMt7ElxfGBD0PSSuCO0FEeNqj9xpJTsMHVdJnLdrXuRkQlH3VVd8aV9Y5LNvbtHiHfVgoI3e55ex4nOgQTdE2Nwbx8PaM4T7YTtFNLZeBguu_hZVjslRYhEFrnpcPxN_RY_CP6yPG8Sv4wQuRDUXq88wj8wdkEUVSL9KfoGAdPGVmeBQIZ6lQ_-efjbknkWAo_GyVH_Ciyt4i0r9Toj75RusGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/82e592cb76.mp4?token=qM1PHrco89ixWHvfQ-J0SS73eZnX1_QStGe6Q7K8bLPQwxW_TlblaxqPuFW17C7VDwL6SeREDVvOQwn4geDfI05Hf0nomQ7elukKBV1qvm7NcAuS1iEiDlGi-kXUGMt7ElxfGBD0PSSuCO0FEeNqj9xpJTsMHVdJnLdrXuRkQlH3VVd8aV9Y5LNvbtHiHfVgoI3e55ex4nOgQTdE2Nwbx8PaM4T7YTtFNLZeBguu_hZVjslRYhEFrnpcPxN_RY_CP6yPG8Sv4wQuRDUXq88wj8wdkEUVSL9KfoGAdPGVmeBQIZ6lQ_-efjbknkWAo_GyVH_Ciyt4i0r9Toj75RusGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🇮🇹
یک‌دقیقه با درخشش دوناروما مقابل فرانسه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/107801" target="_blank">📅 14:05 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107800">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5581b57d8f.mp4?token=Q8XfrjLgDaew550fwikBYRKRXwZ2dhaW1xrdOu-KxALQIdlQOMp4cei4S7P6ZIFsuoH1_luYntsyyZADAL9Ab-P32yRHYK17ywIIKUBj0nJK8KoKmmXQg47SO33x3VoE8y6s_mNjae_LV8jA8xJaM4yTcA-SbAI-S3OPj9jac3QeshYEgxP3-pvphOvFyHfoHMNvgw5_47wj7LYPWor_WHcn2Ch2L_UPhXJpSJTVenW7glRUnnRCgrSHyXwA8aZmDBXwg1hazXPO4Hw1HuDYY8YGo3M7tgeAX5arxs1Ju5SxwAsHvIwHyIcXhfuzZGbA-hsZCuprPXypis2-eC1OBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5581b57d8f.mp4?token=Q8XfrjLgDaew550fwikBYRKRXwZ2dhaW1xrdOu-KxALQIdlQOMp4cei4S7P6ZIFsuoH1_luYntsyyZADAL9Ab-P32yRHYK17ywIIKUBj0nJK8KoKmmXQg47SO33x3VoE8y6s_mNjae_LV8jA8xJaM4yTcA-SbAI-S3OPj9jac3QeshYEgxP3-pvphOvFyHfoHMNvgw5_47wj7LYPWor_WHcn2Ch2L_UPhXJpSJTVenW7glRUnnRCgrSHyXwA8aZmDBXwg1hazXPO4Hw1HuDYY8YGo3M7tgeAX5arxs1Ju5SxwAsHvIwHyIcXhfuzZGbA-hsZCuprPXypis2-eC1OBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
دزدی مسئولین از بانک‌ها سوژه جالب و وایرال شده مهران مدیری در مرد سه‌هزارچهره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/107800" target="_blank">📅 13:35 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107799">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🚨
‼️
⚠️
درگیری‌شدید و خونین در مسابقه‌ای از لیگ زیر ۱۸ سال کشور که در مشهد برگزار شد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/107799" target="_blank">📅 13:10 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107798">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46755fa2d0.mp4?token=HRTUhen7W_fWpUp9wue2GcOk4jrqqSssYpJ-l0o9m-_5bkFrsaYS5cI8DfHxm3yrup-DshYDXmVGU6W9h2Sw_TmW-gj-2t027_0iCfT45kEZwu4cn3lubg6qkJT__eNEQgNa3YrsjIwDuXec6TzEsdlB_QNj_KxCP5lcKFPoIPl3Uqx10WkqxnpTozcaMQTPseZEJU-W6ddKkuwKp6XxaKQVr09tQINbUUOvWFR8bmtC2rFyfVP_skUSPzzqgbYdyPKMT_oaLSL0hIIDvzRoLVwOx3izcFX45joF_T6vpJSHHJ7QVkmpWX1bX5rUpyXDSV8GgH7cnTnmdwjUIIs_pQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46755fa2d0.mp4?token=HRTUhen7W_fWpUp9wue2GcOk4jrqqSssYpJ-l0o9m-_5bkFrsaYS5cI8DfHxm3yrup-DshYDXmVGU6W9h2Sw_TmW-gj-2t027_0iCfT45kEZwu4cn3lubg6qkJT__eNEQgNa3YrsjIwDuXec6TzEsdlB_QNj_KxCP5lcKFPoIPl3Uqx10WkqxnpTozcaMQTPseZEJU-W6ddKkuwKp6XxaKQVr09tQINbUUOvWFR8bmtC2rFyfVP_skUSPzzqgbYdyPKMT_oaLSL0hIIDvzRoLVwOx3izcFX45joF_T6vpJSHHJ7QVkmpWX1bX5rUpyXDSV8GgH7cnTnmdwjUIIs_pQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
🐐
از توماس مولر پرسیدن: «مسی یا رونالدو؛ بهترین فوتبالیست تاریخ کیه؟»
جوابش؟
👀
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/107798" target="_blank">📅 12:45 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107797">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ad1675b1b.mp4?token=C1P45sS8Er6WnOWJdDO9NqQ1Fuk9LCgZStM_nOI48ciSxqUNCp5m34B36aZxgg9__5hOB1Mfx15MYrwZUIUXy0e3fpO3WL5uKOLXWPbUUL9oBUf5PK6xAS-MSEEW53OxmH6RV43R2ssM0toBB8L9zeym6aLGeOaJSzFoXwEA7w3Va9rYrXb1XaSq600T-KR0cdT26r_TQ7or4vb-9qmoHDqOYBD4jFeas7SZWZKw3UOctRkEYAyLrMExbxpiVubvsL4S-GPC3qKMlrIMwxzyTWLh_Fo8h4xG-iqS0E0v6Lbvk9xXMoJ8CRFt_XH6vwC8SsXIBhIJlkp4-fcl6I_Cpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ad1675b1b.mp4?token=C1P45sS8Er6WnOWJdDO9NqQ1Fuk9LCgZStM_nOI48ciSxqUNCp5m34B36aZxgg9__5hOB1Mfx15MYrwZUIUXy0e3fpO3WL5uKOLXWPbUUL9oBUf5PK6xAS-MSEEW53OxmH6RV43R2ssM0toBB8L9zeym6aLGeOaJSzFoXwEA7w3Va9rYrXb1XaSq600T-KR0cdT26r_TQ7or4vb-9qmoHDqOYBD4jFeas7SZWZKw3UOctRkEYAyLrMExbxpiVubvsL4S-GPC3qKMlrIMwxzyTWLh_Fo8h4xG-iqS0E0v6Lbvk9xXMoJ8CRFt_XH6vwC8SsXIBhIJlkp4-fcl6I_Cpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇵🇹
عدم‌پاسخگویی سرمربی پرتغال درباره رونالدو در نشست‌خبری پیش از بازی با نروژ!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/107797" target="_blank">📅 12:20 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107796">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a683578dd.mp4?token=f18YwemsowKZBJYLviFQKBTyHxkOzGWECTP6raOv0sO4OAWR_3cW5J_BhErGlE152l3Z1dzH-pd-eaLLmXZDfT5OhKcrzhsAZ8h7sQ6C9SmE1Ti-sqMmtM8G5HPAdH1nEZA0mdOVZlURUNb-X8Uo5GPsJI5d6-d0g6vH6ZDEnU801g9QodfTcwcl6I6qr5uonduSCti26LmIGfWEfNqcx5Bjv-ET1Yn9qtGYTo_e_EM3O7NX34dlkpAwZ_VWnUawdv0L4K3GDFm4e8SeakLf43XN0WJXUTTI33wm05VMaeLyJiYxd4_fXJOxxSNQC9-WE72RVe3RAVjd8UJAv0rGFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a683578dd.mp4?token=f18YwemsowKZBJYLviFQKBTyHxkOzGWECTP6raOv0sO4OAWR_3cW5J_BhErGlE152l3Z1dzH-pd-eaLLmXZDfT5OhKcrzhsAZ8h7sQ6C9SmE1Ti-sqMmtM8G5HPAdH1nEZA0mdOVZlURUNb-X8Uo5GPsJI5d6-d0g6vH6ZDEnU801g9QodfTcwcl6I6qr5uonduSCti26LmIGfWEfNqcx5Bjv-ET1Yn9qtGYTo_e_EM3O7NX34dlkpAwZ_VWnUawdv0L4K3GDFm4e8SeakLf43XN0WJXUTTI33wm05VMaeLyJiYxd4_fXJOxxSNQC9-WE72RVe3RAVjd8UJAv0rGFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
دهقانی، مسوول مسابقات بین‌المللی فدراسیون فوتبال: باید ورزشگاه آزادی را همانند نیوکمپ بارسلون مسقف کنیم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/107796" target="_blank">📅 12:07 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107795">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bfa3096b41.mp4?token=HwRWd66zqS_mxstFca5Yy5-P-wlIfOhwxF8t4-iGiBcBf2UagBrPd-52B2b_YvH4Acz5EpjlNlvP1QQvS5QQVBDGB7o78IZ6KKENa9uZLYQjuA6LGHQt2jOaf6pJrstzrLyAArwW4cWlUE6dETDuOb5W7u2QqsLgusyb-27z-c3CA--Jtr4k_vUbE_EH4KgO6M78eyw_ig2Qes6zZadaNzV_f6mcAJkbg1aaIC_k-o4acUqILPC4_Buhha0yJAG9YwiSAG5b0xVS57dmaqr_g9oxTmwgtFJyLwjzYEQLIVeepd3fMl5zURCsbEDwxgOXcyOXn3KIS8tL-7pg_vHYIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bfa3096b41.mp4?token=HwRWd66zqS_mxstFca5Yy5-P-wlIfOhwxF8t4-iGiBcBf2UagBrPd-52B2b_YvH4Acz5EpjlNlvP1QQvS5QQVBDGB7o78IZ6KKENa9uZLYQjuA6LGHQt2jOaf6pJrstzrLyAArwW4cWlUE6dETDuOb5W7u2QqsLgusyb-27z-c3CA--Jtr4k_vUbE_EH4KgO6M78eyw_ig2Qes6zZadaNzV_f6mcAJkbg1aaIC_k-o4acUqILPC4_Buhha0yJAG9YwiSAG5b0xVS57dmaqr_g9oxTmwgtFJyLwjzYEQLIVeepd3fMl5zURCsbEDwxgOXcyOXn3KIS8tL-7pg_vHYIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
🎙
ترس عجیب پیمان یوسفی مجری تلویزیون هنگام نام بردن از روحانی؛ یه وقت نیاید بالاسرمون
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/107795" target="_blank">📅 11:55 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107794">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6ce37f880.mp4?token=hnZq2YbdfqvZ_xcif7tQIt8bzGkgrsEOQOPOfUewjVPUCsPwCIcKORz9KaF9kPnMy7qkz4MNhaBqMlwLb1NWKxkZAUTeE7aDohMbuh-qHpsr-nct7TN9M7Lkw_pEiXnFT8y0bD4AxtVzq_xHQLEfODLenKnk_0ttnDMbmMGf6CadIctpUHrTUaf5mBRFn0PCvtviCJX5yt5ZAP76FVC6hXQ6-8UeW4c0b8KSKaNxbnSO5BNjL4653PEpHO6ymKFJcZbRog8hcCcnQq0k2jNzSlX5JYbwkLJfxhxBEux8PMlpir95RGCizoltxNqjkYm1fzpJ9royXXJ8pla1vFKkL6AmvK6aIk21lM-WfTaCbwcEW5s4TuJE4KTT3N6f6QE8TiuveNm_-IbLivN-Aqd6gvICJ8158onLAliF3tqrxAqvDxr27gUjmGZmdswaEbRAWdOwpibBrCmsUzVz6OVNEdIALj7zEJKleCJkJtxXk30y9gaNg-yrPNhJSovrmWipkowbit1BdtoxiG2ITRMe0MwiTF84JWpqrZE1vx24nkY-QOBk0rDKY3RxFKxsgoPCBPSY2jAzfL7pFCxAJTwRaxVKrt7bn1RdH2oG-61WvQo8iwSqBLkkaWJbaSO-cLkRNL8G1kb4kaINrC_gYXCydMT507hZz177-hRnNFYgQHo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6ce37f880.mp4?token=hnZq2YbdfqvZ_xcif7tQIt8bzGkgrsEOQOPOfUewjVPUCsPwCIcKORz9KaF9kPnMy7qkz4MNhaBqMlwLb1NWKxkZAUTeE7aDohMbuh-qHpsr-nct7TN9M7Lkw_pEiXnFT8y0bD4AxtVzq_xHQLEfODLenKnk_0ttnDMbmMGf6CadIctpUHrTUaf5mBRFn0PCvtviCJX5yt5ZAP76FVC6hXQ6-8UeW4c0b8KSKaNxbnSO5BNjL4653PEpHO6ymKFJcZbRog8hcCcnQq0k2jNzSlX5JYbwkLJfxhxBEux8PMlpir95RGCizoltxNqjkYm1fzpJ9royXXJ8pla1vFKkL6AmvK6aIk21lM-WfTaCbwcEW5s4TuJE4KTT3N6f6QE8TiuveNm_-IbLivN-Aqd6gvICJ8158onLAliF3tqrxAqvDxr27gUjmGZmdswaEbRAWdOwpibBrCmsUzVz6OVNEdIALj7zEJKleCJkJtxXk30y9gaNg-yrPNhJSovrmWipkowbit1BdtoxiG2ITRMe0MwiTF84JWpqrZE1vx24nkY-QOBk0rDKY3RxFKxsgoPCBPSY2jAzfL7pFCxAJTwRaxVKrt7bn1RdH2oG-61WvQo8iwSqBLkkaWJbaSO-cLkRNL8G1kb4kaINrC_gYXCydMT507hZz177-hRnNFYgQHo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
🎙
🇮🇷
بغض محمد عمری ستاره پرسپولیس ترکید: از روستا به تهران آمدم؛ شب‌ها با یک بربری می‌خوابیدم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/107794" target="_blank">📅 11:34 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107793">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9581683260.mp4?token=GERjjL98hsxDi2byDA8UYqjBNMK9nxSRYCawW9E53kE91BxvDHPIQYYV49VuqSUJDZ7hXJmz6QZ3T5i0xHOJ5MiIKl5DgeF1cOb5_Kt1ONSZHyfmCaa5ylBi5xm8TZBVhkd5kBgXO48XzTc-Tzfj3Jbrff-idxr1U-7aa5G6-eXsciS0lIjZyzymVEijpjB05gInO18qScnqQrhxzFer-sXf3lwoVtTbFHUvS4idUWfQL2mPCjmkGUToQfLrKYemiDiQoT4sP5v52IXnfhc90bu2eI01nCynnmVzbeNZWRyrFZ12icwbFC59Q-rfpAc6QnOitgSc2dccYmTXb6Z3Wg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9581683260.mp4?token=GERjjL98hsxDi2byDA8UYqjBNMK9nxSRYCawW9E53kE91BxvDHPIQYYV49VuqSUJDZ7hXJmz6QZ3T5i0xHOJ5MiIKl5DgeF1cOb5_Kt1ONSZHyfmCaa5ylBi5xm8TZBVhkd5kBgXO48XzTc-Tzfj3Jbrff-idxr1U-7aa5G6-eXsciS0lIjZyzymVEijpjB05gInO18qScnqQrhxzFer-sXf3lwoVtTbFHUvS4idUWfQL2mPCjmkGUToQfLrKYemiDiQoT4sP5v52IXnfhc90bu2eI01nCynnmVzbeNZWRyrFZ12icwbFC59Q-rfpAc6QnOitgSc2dccYmTXb6Z3Wg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نمایش های عجیب وینی مقابل هند هم ادامه داشت!
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/107793" target="_blank">📅 11:14 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107792">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/107792" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/107792" target="_blank">📅 11:13 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107791">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ST-CDpfNJpcqJYT9Upw8DhkpSWQvaeM5EkdmoHCLEFTi4p3ydc2CcOpyAS8TtG0HfvTLD6sCawZAd1pZ1n--oi6OzDM_Xa4ySGq36kScLBj76sWEDrOAC0njw0Krzs611U4UJQzk7ZwGM9lRtkNx-KBX0hN4Cf89UClRzYHm7T_ebGTvVz7zrxeGGz6SP2H763gayrfUIZvqNiNVf8rS3MPnSlpqIc4o3xfkLtowJLd7AO8thKVRrqEXeVJ0UcA7Ntf_Rggx4yzLga3H065JSIhn377j-Yx18b9X5S0cgnbhMIGKkm-jsy7mJd0AP4cHq5QzS6VZqnYvcqaLTyoi7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
مچ‌های مهم امروز در سایت بین‌المللی
TrexBet
آلمان
🆚
یونان
صربستان
🆚
هلند
نروژ
🆚
پرتغال
دانمارک
🆚
ولز
آفریقای جنوبی
🆚
مصر
مالی
🆚
مراکش
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
انتخابت رو انجام بده و آماده‌ی هیجان باش!
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/107791" target="_blank">📅 11:13 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107790">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6634bc99dd.mp4?token=ojmW6vDJFLenQhKyLogPBHZ2oUjwo92ZymAo8pOSOcB0iymFEKUqmlSF-DutSwVlaR-5FyC85tdNa8Zxph15tQuvIxMqyKG0FRK4vkhqx7a23Lm1AFrfJ4VXhlGoap5nmof3ExkUO8Bekxya_8qeTLLbXCsKydneg5ST8GBgLjU_F-CHPhgNzDIvR-bi2uLylKI4fCGV4JB2rwihpLzwNUbM7heEp6AdIqeK5eV06vaiAbmBu6B5vyGAagBeWJ9iJGfo2gKnFrjYvapeszZyNZKThp6hEn3ux2Oe2KE-zV-1Povb_Hutpm7V_BYtAO1bW05KKPtkd2bAtsEstCSyCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6634bc99dd.mp4?token=ojmW6vDJFLenQhKyLogPBHZ2oUjwo92ZymAo8pOSOcB0iymFEKUqmlSF-DutSwVlaR-5FyC85tdNa8Zxph15tQuvIxMqyKG0FRK4vkhqx7a23Lm1AFrfJ4VXhlGoap5nmof3ExkUO8Bekxya_8qeTLLbXCsKydneg5ST8GBgLjU_F-CHPhgNzDIvR-bi2uLylKI4fCGV4JB2rwihpLzwNUbM7heEp6AdIqeK5eV06vaiAbmBu6B5vyGAagBeWJ9iJGfo2gKnFrjYvapeszZyNZKThp6hEn3ux2Oe2KE-zV-1Povb_Hutpm7V_BYtAO1bW05KKPtkd2bAtsEstCSyCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حرکت‌جالب لامین‌یامال بعد از بازی دیشب
❤️
👌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/107790" target="_blank">📅 11:05 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107789">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/321c017aa1.mp4?token=VDNxygh2QIoiZasIJY_gK7kSeqfipQJDqzYDZveFShMF-4CfJ4z7VCsLMma2_T0oC9pvpRnbFV8vtjeW1GoSFzUQEJifZLLE0xQutm9MbsU31q7dkX0kex-Hh691X_F_aNyicyUW1DPOLdTCnFKHHmGEcQRb7S1EV9fSVcV9OY-NL0iviqXHaDQdprY25_47U-jIuetpJxoDg4iAOyOW5uysv9KlxYFOpgjIb1xgGGD45X3hIivaQ59tlooukIqxecge2drVHuljyjMacEUVLSph9iBDzwThEZgCnd4Se4SbWIUIXohnB8HODXHun499J8iPfU2-72RMbcfxBqnGng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/321c017aa1.mp4?token=VDNxygh2QIoiZasIJY_gK7kSeqfipQJDqzYDZveFShMF-4CfJ4z7VCsLMma2_T0oC9pvpRnbFV8vtjeW1GoSFzUQEJifZLLE0xQutm9MbsU31q7dkX0kex-Hh691X_F_aNyicyUW1DPOLdTCnFKHHmGEcQRb7S1EV9fSVcV9OY-NL0iviqXHaDQdprY25_47U-jIuetpJxoDg4iAOyOW5uysv9KlxYFOpgjIb1xgGGD45X3hIivaQ59tlooukIqxecge2drVHuljyjMacEUVLSph9iBDzwThEZgCnd4Se4SbWIUIXohnB8HODXHun499J8iPfU2-72RMbcfxBqnGng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
▶️
کنایه مهران مدیری به ماجرای نماینده مجلس و مامور راهور در مرد سه‌هزارچهره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/107789" target="_blank">📅 10:40 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107788">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8c7979edd7.mp4?token=vm0T39x6c0dQnByKhrEKo_D3airPZ1mslTIgjchO3GBimHaZtYYXdahk9zEcpbep5TWrez3SDuvNaWEZymcRIl0fDoPaaMm-rBmeVfZGUgkhqVnlenHN41IECTFfOQG6nj_1UTM5Ezm53kF6EjLYmvMi9MLbSqyjCcIEnGSEeJPursFRCn6zo0dI_Z2k_FaYVqaz2psgKJg_knW4Lpy0Sj7aBvKfrU8c6oN98RlT2ZCYUTfLyiQmSfKCQPMdUfUX_65FXx3fvwBVw4c14JKRkhxSjytaqRM3s7GNcZ5-DlTQ1WqxBKfH3ijwXNNoCUgOyUnpZZcWnOIU04q2sVlLpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8c7979edd7.mp4?token=vm0T39x6c0dQnByKhrEKo_D3airPZ1mslTIgjchO3GBimHaZtYYXdahk9zEcpbep5TWrez3SDuvNaWEZymcRIl0fDoPaaMm-rBmeVfZGUgkhqVnlenHN41IECTFfOQG6nj_1UTM5Ezm53kF6EjLYmvMi9MLbSqyjCcIEnGSEeJPursFRCn6zo0dI_Z2k_FaYVqaz2psgKJg_knW4Lpy0Sj7aBvKfrU8c6oN98RlT2ZCYUTfLyiQmSfKCQPMdUfUX_65FXx3fvwBVw4c14JKRkhxSjytaqRM3s7GNcZ5-DlTQ1WqxBKfH3ijwXNNoCUgOyUnpZZcWnOIU04q2sVlLpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🔥
🇮🇹
درخششِ دوناروما اجازه ی گرفتن انتقام رو به زیدان در بازی با ایتالیا نداد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/107788" target="_blank">📅 10:15 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107787">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/95502ba1a6.mp4?token=me3782vDIkGTVCf-ZBZMSqVCt1i-WbWVkD695-oQTTYbOV2vXsCMay6a97rohn4Yo8IvqUDbP1twqx1M_vkvD-ZSlF4aK9t7c7HRI_r-mGmMUa6QGEsl6PNXqBucFNTMUfSMDa6u-qM1S8Kk61k4CKU8nht05Cf25DQgU0uJtI0Ay0T5ZCBNhUkQ0yzcYCQ3hw-03vkHP_3m6js2Mts7xSM4JKNJX8wGWCFiRxQO82Zx7PKQhiDCCAVN9rLuTf2hlCbPvXNK6m50_Np_FcQDV4gFiwYMflUvtjtPdVm2DWQvKGjbNOD57lT12v651IIDkk3G3UJ7IcHAECPrPzxiNVlnfghemGAtR0W9rQiqv9yDYUSlm3WvcQvaRv5BG6HdkdnPrhy_5k-46x2pWxWl2IcZCd9ZiR_-DSRTwhkt6bhYLsUSQRAN-Bf8sjjkunjyjDk1vq3dyn8gTrpzQE6krdoNTtvm8_DZhLq4JfCD7qu5cNNB_1vZo1P1yXAoK-irI2nm3-o8AE-fsj88JiCnHWnJAwGTfr2HotB0dqLKNg1eSw40KMwq3D31BM-54obJS1pifMcuM3pnCslpOfPxZzZzNLHGpzivUNpmhnt6cLyz2bBNN8MiBUhK_UyLbvKv4wLiuVmbi4Z0K_CgdI8XXTQvimKEV1ur2Sd5BydpYkc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/95502ba1a6.mp4?token=me3782vDIkGTVCf-ZBZMSqVCt1i-WbWVkD695-oQTTYbOV2vXsCMay6a97rohn4Yo8IvqUDbP1twqx1M_vkvD-ZSlF4aK9t7c7HRI_r-mGmMUa6QGEsl6PNXqBucFNTMUfSMDa6u-qM1S8Kk61k4CKU8nht05Cf25DQgU0uJtI0Ay0T5ZCBNhUkQ0yzcYCQ3hw-03vkHP_3m6js2Mts7xSM4JKNJX8wGWCFiRxQO82Zx7PKQhiDCCAVN9rLuTf2hlCbPvXNK6m50_Np_FcQDV4gFiwYMflUvtjtPdVm2DWQvKGjbNOD57lT12v651IIDkk3G3UJ7IcHAECPrPzxiNVlnfghemGAtR0W9rQiqv9yDYUSlm3WvcQvaRv5BG6HdkdnPrhy_5k-46x2pWxWl2IcZCd9ZiR_-DSRTwhkt6bhYLsUSQRAN-Bf8sjjkunjyjDk1vq3dyn8gTrpzQE6krdoNTtvm8_DZhLq4JfCD7qu5cNNB_1vZo1P1yXAoK-irI2nm3-o8AE-fsj88JiCnHWnJAwGTfr2HotB0dqLKNg1eSw40KMwq3D31BM-54obJS1pifMcuM3pnCslpOfPxZzZzNLHGpzivUNpmhnt6cLyz2bBNN8MiBUhK_UyLbvKv4wLiuVmbi4Z0K_CgdI8XXTQvimKEV1ur2Sd5BydpYkc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
🇮🇷
نمای‌کامل از صحنه‌جنجالی بازی لیگ‌برتر بانوان میان استقلال و گل‌گهر سیرجان؛ فقط جیغ و داد داور و بازیکنان رو ببينيد
😁
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/107787" target="_blank">📅 09:50 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107786">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/363181b8d9.mp4?token=bb8KQ0nvXTJ92bdUY09At1kPExGf16XRp9z_NHazr00er0GJdq30EM-tMypX7XgB_njV1K-I3l0gqZzvIX-4eJxVZ5zO97o7p3E9ErARI9b_xC1jKTtBVDk8KJ0jkz18h4VBB5WUmPc9Bcr-AVl4NKOv45_JQTX09FDTyRvD9yvDD-5ustPjjiUgCg54OnsrbmyWbajynBuVUZLktgEq7lNA6SMrdt08Ir0HIIw_7o0N_GgUNCez4wzncHRmJIXxUvTivAvTm6C16UTYCt7IwEuiedr_yT0Y_TNR8lfEeSlHhngN6BqC8AXCJYt3DXuYX91uHHIGQHyYWJm7pZPK9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/363181b8d9.mp4?token=bb8KQ0nvXTJ92bdUY09At1kPExGf16XRp9z_NHazr00er0GJdq30EM-tMypX7XgB_njV1K-I3l0gqZzvIX-4eJxVZ5zO97o7p3E9ErARI9b_xC1jKTtBVDk8KJ0jkz18h4VBB5WUmPc9Bcr-AVl4NKOv45_JQTX09FDTyRvD9yvDD-5ustPjjiUgCg54OnsrbmyWbajynBuVUZLktgEq7lNA6SMrdt08Ir0HIIw_7o0N_GgUNCez4wzncHRmJIXxUvTivAvTm6C16UTYCt7IwEuiedr_yT0Y_TNR8lfEeSlHhngN6BqC8AXCJYt3DXuYX91uHHIGQHyYWJm7pZPK9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
▶️
‼️
علی فتح‌الله‌زاده:
🔺
فدراسیون با یه قانون من درآوردی سه جانبه برگزار کرد، میتونست با همون منطق بین ۴ تیم اول بازی بزاره قهرمان مشخص کنه.. به استقلال ظلم شد چون به احتمال ۹۰ درصد تو حذفی قهرمان بود و اون جام رو هم از دست داد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/107786" target="_blank">📅 09:25 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107785">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/708801c3df.mp4?token=Bs692ym-THGLs2mqE_f1RU2EOtHinilNScytiSFmGgzpnYymIMa0bYz5w7Q4JaQDUYl2E2b5ls0JxKjvDrY_AbQYP9LDwNxIke535leLCU0MUsgwfumAPqxjwFmfY9W03wQNTW3fxaRJE8Fof_mk_Rkb4qed4Gaz937aG2mL8aIr3LFdCgrJfY39cDgRRQjcnXKUYts6CxFTfk8xguMvtw3C4dF35YkAGFubwuLh6eHDqEjvGqCee80-lYmv7rHbGzVTreTj3xUx5DE7S0C90QMmDhELRsSJ8Z4bYT7OCj0TvvWYN06M_xWHdzzlyr3HlQ0zUhJoJeVV-lZh0dNiAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/708801c3df.mp4?token=Bs692ym-THGLs2mqE_f1RU2EOtHinilNScytiSFmGgzpnYymIMa0bYz5w7Q4JaQDUYl2E2b5ls0JxKjvDrY_AbQYP9LDwNxIke535leLCU0MUsgwfumAPqxjwFmfY9W03wQNTW3fxaRJE8Fof_mk_Rkb4qed4Gaz937aG2mL8aIr3LFdCgrJfY39cDgRRQjcnXKUYts6CxFTfk8xguMvtw3C4dF35YkAGFubwuLh6eHDqEjvGqCee80-lYmv7rHbGzVTreTj3xUx5DE7S0C90QMmDhELRsSJ8Z4bYT7OCj0TvvWYN06M_xWHdzzlyr3HlQ0zUhJoJeVV-lZh0dNiAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🥈
ایشون کیمیا زارعی ورزشکار رشته روئینگ هستن که تو مسابقان ناگویا یه مدال طلا و یه نقره به دست آوردن
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/107785" target="_blank">📅 09:01 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107784">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a540d193c.mp4?token=hC4U00S8hV0Dti-RZNLU4bImo6DgehLhtJWbUX1LqbDKnak-E7tAXR2Y1NiN99kLJkjeRq1ykR14qIbDrUbzL1qBvz23DERDnzKFjRa_JEZmYrOh93Bp6laHa47VMDEaxRMwKlZoFqhL10cwy10KRMmMylpggIxaW1ZIuk9euvoQaSgDL0U5o8Cuqk8LcH2j6Fhv3AbEdbeoLqmBl2LZ9vQVynit2Vw1WDqVVaS9hxgbq7RH6y5uOSIa2fAt4aMj5Yn02_AMEtNbBwkIfGzgqeKoEU94hxtuqC3tSPWOF7ZpW6awdrGOXWL_clxgMWRtdWHM1HMchPcmZ4LMSsCdfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a540d193c.mp4?token=hC4U00S8hV0Dti-RZNLU4bImo6DgehLhtJWbUX1LqbDKnak-E7tAXR2Y1NiN99kLJkjeRq1ykR14qIbDrUbzL1qBvz23DERDnzKFjRa_JEZmYrOh93Bp6laHa47VMDEaxRMwKlZoFqhL10cwy10KRMmMylpggIxaW1ZIuk9euvoQaSgDL0U5o8Cuqk8LcH2j6Fhv3AbEdbeoLqmBl2LZ9vQVynit2Vw1WDqVVaS9hxgbq7RH6y5uOSIa2fAt4aMj5Yn02_AMEtNbBwkIfGzgqeKoEU94hxtuqC3tSPWOF7ZpW6awdrGOXWL_clxgMWRtdWHM1HMchPcmZ4LMSsCdfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🎙
🐐
حمایت فیلیپه ملو از کریستیانو رونالدو:
"یه تفاوت خیلی فاحش بین رفتار بازیکنا با کریستیانو رونالدو و رفتار بازیکنای آرژانتینی با مسی وجود داره.‌ من می‌بینم وقتی بازیکنای حریف مقابل کریستیانو رونالدو بازی می‌کنن، خیلی بیشتر بهش احترام می‌ذارن. تو تیم ملی پرتغال، هیچ‌کس حتی به گرد پای کریستیانو رونالدو هم نمیرسه! تو نمی‌تونی بذاری بهترین بازیکن تاریخ همین‌جوری بذاره بره، انگار نه انگار که اتفاقی افتاده؛ اصلاً راه نداره!"
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/107784" target="_blank">📅 08:40 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107783">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d08431eb67.mp4?token=ME6NWsV_QHSO0U79avwpTSG0rucYsiTkYpcUt_cNVmSn8L0-0FfrhiyDGlBILYM-gPuj0K_BCUMUnveyYtV6WXzUs0VxQdiEjdlKqWPzgqS8IiVQ-T5b0RpKjE4WjgL39bjWMGfXI3MGZWFizlU_d5R-CWq24VXJKlBSRw2T3xS68ar95-QDN4bXUQmlmDurOt3XfriRdSlHsFPoKHimWy4QBGkgiWvBZ6jgdHopz0KYe_421OYq-92RTVV1E2kE-W7udb2RcKZuVVrYlqwsyz1J-Hd70k1t-7JclwBcmWIP4pIRDdi5mOBKtzn57D7EF8btSZQJllh_oJaSlfYXAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d08431eb67.mp4?token=ME6NWsV_QHSO0U79avwpTSG0rucYsiTkYpcUt_cNVmSn8L0-0FfrhiyDGlBILYM-gPuj0K_BCUMUnveyYtV6WXzUs0VxQdiEjdlKqWPzgqS8IiVQ-T5b0RpKjE4WjgL39bjWMGfXI3MGZWFizlU_d5R-CWq24VXJKlBSRw2T3xS68ar95-QDN4bXUQmlmDurOt3XfriRdSlHsFPoKHimWy4QBGkgiWvBZ6jgdHopz0KYe_421OYq-92RTVV1E2kE-W7udb2RcKZuVVrYlqwsyz1J-Hd70k1t-7JclwBcmWIP4pIRDdi5mOBKtzn57D7EF8btSZQJllh_oJaSlfYXAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🇪🇸
سوپرگل سکسی یامال در تمرینات اسپانیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/107783" target="_blank">📅 08:05 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107780">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df11e10418.mp4?token=Ge6SccqVOfnhI-mdCoPBqLCiGzDcZQHekrx-TsJkcUw95YQ5QQvVPVqdDIZC1hzOz5x08HZlhx42ggUuq_FFfWKDv8T32WareuR1I3ZZYJsqfIs5g4XWyVqfmu7OA74udaF5pJ5qY8j7bpALPsuoGIN_MJaDvxSvyt8_F6uSDACI-UmtUVVGlTicd8QcrHEeRi0vPRaL3LRaGKuviN8Qdh-Lbbw9WR6a7H0TMz4t0an397WC7IolUJZrp0tju4xtGX8fq6tgHc431ETZ4y1Ltq8W6EEIgefSCx11o4u79Wt2cbi4d9rpnxT0KjhIU_PD3Mxv-FNK6k4wjc1ubLxn3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df11e10418.mp4?token=Ge6SccqVOfnhI-mdCoPBqLCiGzDcZQHekrx-TsJkcUw95YQ5QQvVPVqdDIZC1hzOz5x08HZlhx42ggUuq_FFfWKDv8T32WareuR1I3ZZYJsqfIs5g4XWyVqfmu7OA74udaF5pJ5qY8j7bpALPsuoGIN_MJaDvxSvyt8_F6uSDACI-UmtUVVGlTicd8QcrHEeRi0vPRaL3LRaGKuviN8Qdh-Lbbw9WR6a7H0TMz4t0an397WC7IolUJZrp0tju4xtGX8fq6tgHc431ETZ4y1Ltq8W6EEIgefSCx11o4u79Wt2cbi4d9rpnxT0KjhIU_PD3Mxv-FNK6k4wjc1ubLxn3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎁
زلاتان ابراهیموویچ به مناسبت تولد ۴۵ سالگی‌اش، یک خودروی فراری مدل F80 کادو داده. قیمت این فراری، حدود ۳.۶ میلیون یورو تخمین زده می‌شود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/107780" target="_blank">📅 00:43 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107779">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f84ad4f46e.mp4?token=t56cyhmEyu_OIoKAWoESdJ_nH4iA6zXPWMH8TOxFSs3MNN_ScNLk3T1imNL08z39cFHsgWFIaQXCmowgiLXUvA0PrffPQZYMmk4Xv-uaWLKdlKYGzVvZ7QyUFOyeRGtm14-O7Z1AGnG5pLFBvdmkquzAFtryimNbcHG2uP8fgxpFyV2zQhsEF7E0AvBlPAVS31VypiX_G21eLXAe0eZohNn2zWmfeW70ezjpi_M1nCdQtpidH3dLH_aYdt1Cb8t4UTLK_JP0cE4XGv7Nz9sz7PO6VrMHOCNgBi-NA1mDAAfkK7B-6gk3QSkIxPMZBs_fEElEAM86Qu1KZRO-53FZbQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f84ad4f46e.mp4?token=t56cyhmEyu_OIoKAWoESdJ_nH4iA6zXPWMH8TOxFSs3MNN_ScNLk3T1imNL08z39cFHsgWFIaQXCmowgiLXUvA0PrffPQZYMmk4Xv-uaWLKdlKYGzVvZ7QyUFOyeRGtm14-O7Z1AGnG5pLFBvdmkquzAFtryimNbcHG2uP8fgxpFyV2zQhsEF7E0AvBlPAVS31VypiX_G21eLXAe0eZohNn2zWmfeW70ezjpi_M1nCdQtpidH3dLH_aYdt1Cb8t4UTLK_JP0cE4XGv7Nz9sz7PO6VrMHOCNgBi-NA1mDAAfkK7B-6gk3QSkIxPMZBs_fEElEAM86Qu1KZRO-53FZbQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
‏لحظه
اصابت صاعقه به برج میلاد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/107779" target="_blank">📅 00:17 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107778">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/suaMlC3H4SUQs1a0xCWy0sQBcBCSsh2EvEeLf5kcwg93TEIFMLhLv4QfQrBMy98llZJuHR1bJayHk0kERTDXDsOqfTGsepnUumiuklOsgoHqDx5p7tVa0muLp3C5UnW4qsIUj3hgxpMiFWxNph-ts62hVsr_yaiguR20a6BpzXtPuniKkKsCYSzbYcsQ59IFin59I5N0xLNb_zpGQiRKarEPCMNAgINWSHeUuZAUTk4M23UcAvJH1icvmTVB6PWQzvnU61B8oft-CYoWa5DrF_Ccj-kOjbTAEg-yIeCB9zluEbiM4BSfpXMuMCC2vjMKe6L-e6vixz0-usXMDq3r1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
لیگ ملت‌های اروپا| تیم اول و دوم ندارد؛ اسپانیا با هر ترکیبی برنده می‌شود
اسپانیا سه - ‌چک یک
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/107778" target="_blank">📅 00:12 · 12 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
