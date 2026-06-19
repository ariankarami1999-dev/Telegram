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
<img src="https://cdn5.telesco.pe/file/KPm2JpNcySCLoD792yKLp5hFKu9bjs53jR6nvetrIXqnvFBi03zUAEYu-HrE9Msxl-bmuepnmKE1W5P-CL_Mg3-L-EqH_O7W-bs2-A4rLf0EKQm3ivnftoDWvurjF80Xu8oGeKfN9z9ktzXilYBJR2QZsllciy3capovzqFXXFsBmdX-ESTQfwpG21nn5QXOIsOZv8jqhc9fWS2BIA2XL0L1Cq2ELmpM_D7MEn9Sl8zRsaQhhOj-WXfoxp4mUx6YVnWSPs7E5aYJRuCu_9PzQKa7vF9S-7YAsBvA73am8GbeqqvAexA8cGGoKvwlultsbwn8DFBi6Pk7BpM1g9v4hw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 جام جهانی 2026 | فوتبال 180</h1>
<p>@Futball180TV • 👥 674K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-30 02:15:05</div>
<hr>

<div class="tg-post" id="msg-94552">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/25cfcc20c6.mp4?token=tvdjaTjvIGXe3ljRYFLCuoEcsRLttFqHcuXgYKGC-bAGIL0M8bgLgcbayWL1Mh68FInOJrdmJpU0hZ-UyfaUP7wWzZS3ZU2EQ7ec-fGUHpndgI21QgzI5ASw_VW7y_fXlVmCN532ZngHrP0fhxIg_daMrefwOyolGFutXc8u7RsAmmKkQnpgMtLBrc0vSrhM0-smd3KJQXwZim93-2JSAkwuF8YZf6u65muRqdErwW1PwNVqMbh1Nz2xcIULS4XAu3rm8RUkH74W7JfqE45y3XbDXTbTrHdPFaWG_nwNwWXdC4o1XHTLMkt4etgMj-oU5qjIdJBYaZ20jIvRrJSv05GdXgr7qGRfYLXM84JoRPbtWCdArXIMcv-sqTYcj175lUFgvsXqZaN-qoJPLEmNTFf-OPZenpanh1_PcVFosYiwaUIvHm4pU6-cMdVQdQe5DJX90VTBA8ZwZ8Ck_s6FAUMu-cAC_kBoYPAsQA3ukNdpkQlCSLCSp_rz3e5VwMFo6obOxTQAgTpCVH0GgHC799sYgGlVgCWNIgLgDJWkykv9-KlAIt75BJW0hXViHHRl902ANwIdlt1ZJ67LEQPpA-tvyfYvtoHU4v5euXE96b8wJKNV1tlA8L7NAwUkyjIwYfSBFiHbdcmso0uWlkA8IadDHJKk6d03Ycmpjk-emtc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/25cfcc20c6.mp4?token=tvdjaTjvIGXe3ljRYFLCuoEcsRLttFqHcuXgYKGC-bAGIL0M8bgLgcbayWL1Mh68FInOJrdmJpU0hZ-UyfaUP7wWzZS3ZU2EQ7ec-fGUHpndgI21QgzI5ASw_VW7y_fXlVmCN532ZngHrP0fhxIg_daMrefwOyolGFutXc8u7RsAmmKkQnpgMtLBrc0vSrhM0-smd3KJQXwZim93-2JSAkwuF8YZf6u65muRqdErwW1PwNVqMbh1Nz2xcIULS4XAu3rm8RUkH74W7JfqE45y3XbDXTbTrHdPFaWG_nwNwWXdC4o1XHTLMkt4etgMj-oU5qjIdJBYaZ20jIvRrJSv05GdXgr7qGRfYLXM84JoRPbtWCdArXIMcv-sqTYcj175lUFgvsXqZaN-qoJPLEmNTFf-OPZenpanh1_PcVFosYiwaUIvHm4pU6-cMdVQdQe5DJX90VTBA8ZwZ8Ck_s6FAUMu-cAC_kBoYPAsQA3ukNdpkQlCSLCSp_rz3e5VwMFo6obOxTQAgTpCVH0GgHC799sYgGlVgCWNIgLgDJWkykv9-KlAIt75BJW0hXViHHRl902ANwIdlt1ZJ67LEQPpA-tvyfYvtoHU4v5euXE96b8wJKNV1tlA8L7NAwUkyjIwYfSBFiHbdcmso0uWlkA8IadDHJKk6d03Ycmpjk-emtc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
واکنش یه هوادار مراکشی بعد گلزنی کشورش به اسکاتلند مقابل دوتا در و داف طرفدار رقیب
😂
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.12K · <a href="https://t.me/Futball180TV/94552" target="_blank">📅 01:58 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94551">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/15f84c4794.mp4?token=iD2522yOudHoz2xerDrBSfWLhycLdzDKRm2Zo7cY2ioFblAwSDTifcvr5EK-_B2fl888dvtl3xhINivKR6h0koNtDXdlkgp8me4i4oN_a5_YdKJJbZGO1cwaJ5yrI06HI15ZyV6Y7HbzSKwjx5jI7TkvXNuzaeocx6OE8hSpKwcRY2-6w4Vx18Bny5NKXb7WCj1xgNd07EDfXnIKkrycuTrk8Tw2Xe66vAi__vZgk2dIKunvjQYpVzIrOJzT3BhR7nsmrnNZb5jlQ8Z7BaFMO5Gm9XXSNx8LNFqz1AVVdHu9Avdbol9l3HsZnqeB95_aO_dnZSzMjlPKMtNuohoGr684F1Fc-Qy5OgpEr_DrdNDKPnqJZuiZtQOgYZYhzYPd0M2O7ZHt3kaprg8W2TWiKVHSP2OOXHdQNeyQRIJdQ_udPVf9-EqzmhtIFIR2o6xq9QRi9Xd3xcVrnranCNiHzPZoM1EtfKuSav3hBFEHfcYqUaUVbB0HO1Fxtwqpp76CVGJTOD72tsT6zKSlPXwVKI7Q9RkEA33DLZ1gY56nSudfwnBOQKtARMabN8Yi4fBYs2TMXZF64Yx-6JfT4EqgAvLgwCnqr5KcfIt63CSsaPYARBVe2t-jWJtMLlniGn3ZJvubQTGWDKGrJVSLu1e-dlRV3kMivx7R0lsdjKkWkv0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/15f84c4794.mp4?token=iD2522yOudHoz2xerDrBSfWLhycLdzDKRm2Zo7cY2ioFblAwSDTifcvr5EK-_B2fl888dvtl3xhINivKR6h0koNtDXdlkgp8me4i4oN_a5_YdKJJbZGO1cwaJ5yrI06HI15ZyV6Y7HbzSKwjx5jI7TkvXNuzaeocx6OE8hSpKwcRY2-6w4Vx18Bny5NKXb7WCj1xgNd07EDfXnIKkrycuTrk8Tw2Xe66vAi__vZgk2dIKunvjQYpVzIrOJzT3BhR7nsmrnNZb5jlQ8Z7BaFMO5Gm9XXSNx8LNFqz1AVVdHu9Avdbol9l3HsZnqeB95_aO_dnZSzMjlPKMtNuohoGr684F1Fc-Qy5OgpEr_DrdNDKPnqJZuiZtQOgYZYhzYPd0M2O7ZHt3kaprg8W2TWiKVHSP2OOXHdQNeyQRIJdQ_udPVf9-EqzmhtIFIR2o6xq9QRi9Xd3xcVrnranCNiHzPZoM1EtfKuSav3hBFEHfcYqUaUVbB0HO1Fxtwqpp76CVGJTOD72tsT6zKSlPXwVKI7Q9RkEA33DLZ1gY56nSudfwnBOQKtARMabN8Yi4fBYs2TMXZF64Yx-6JfT4EqgAvLgwCnqr5KcfIt63CSsaPYARBVe2t-jWJtMLlniGn3ZJvubQTGWDKGrJVSLu1e-dlRV3kMivx7R0lsdjKkWkv0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
💥
🇺🇸
پرواز بالگردهای نظامی آمریکا حین بازی امشب با استرالیا و ذوق‌زدگی جالب تماشاگران
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.16K · <a href="https://t.me/Futball180TV/94551" target="_blank">📅 01:50 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94550">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ONS3NTY08FSOOv1LxfTTj-r0z1R2oG3u-vbQ_jomTF-VWlm9wiJzyelzaHRs2U-JwRB6c5B7CG4GOVtvv0WwlgdT_QWTtOEMB_aSV4HvittaU5g0xG-PoWYRsjeADabq94UTOflzW7mdeV9EwNEhlZ8VNaPpn2CNGTxru2bSKsVykL15js8xKSEV6_hu9tQzz-QEiVlk2US5ccns28Tvu8ycYK7Ys0XKdpwe2Vzkm6T_4RK-T3TULq2NHt5HD-69TjzgOOr-jP97uXwGGwh93dZIrdAdMJy8KhVM7MMpkeLfBZ4I64hdxA3lPQBhkDwmIVNkT2n_twlwUUqEKKSDyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گل‌اسماعیل سایباری سریعترین گل جام‌جهانی ۲۰۲۶
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.19K · <a href="https://t.me/Futball180TV/94550" target="_blank">📅 01:40 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94549">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/2ceedb0fae.mp4?token=rJsFOEQlbhP1TiMUccP0e3lDJO0bcw3jGIknzdk-NPlx-UWaA1xRkDI7ioo92AwfrAFUoTa7zujJp2DVW9grx0yrrESpP1kUG73-e-plnHXP0H-ou-x5OGGU9C090GanPVSLfCt-2zcP2rp7vj2B1ZuIDM-HEKTrLEodPnrvNe-5w1PFmDThC575vHSiBRRHqQz5QBQ3sDBWD1Q0VDoi012Qdu-Mgh508s5yW386gPeyrbXahvo02YwX7hmVSWKRtW_6vyWc3-Pz0MmchwLohoSrApv-Sl-mZdPSd6lJpx4bmKuZIKUPVXeCsUGtYW3ziFpy-NgoJIZMSBoFhFttcYwJ_GmknMNKkvg_pVVg82j5Y-CBGHUjdap-C5dLj6EhsOD_hQM4VoKP7Ftdxg1MujwgXszDQzsX6T7xvVLNGOnf-H9LxjX9NDfgxKSYWyOFy1obNiYlmtoBqDCgu-oPEwnZxCOdxbzWJpyI0GpWeOz5BeE2_OP4memZQBLzeYPn2fonwgtbjUs6PENTToeBsTj_Wpl9CWicQXOHoru-Arpauo9mLyp8c4CwLKHlcGczVgT5xPazURJu4UPk7ohFU5VcCb7Px0wr4g-2LXiwI85Q2CS_EMxuB0rpfaq1CIyD1RRCNzfK3dh5uVc25hctFkCdTbGFf2_zOW0VdGX7bAM" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/2ceedb0fae.mp4?token=rJsFOEQlbhP1TiMUccP0e3lDJO0bcw3jGIknzdk-NPlx-UWaA1xRkDI7ioo92AwfrAFUoTa7zujJp2DVW9grx0yrrESpP1kUG73-e-plnHXP0H-ou-x5OGGU9C090GanPVSLfCt-2zcP2rp7vj2B1ZuIDM-HEKTrLEodPnrvNe-5w1PFmDThC575vHSiBRRHqQz5QBQ3sDBWD1Q0VDoi012Qdu-Mgh508s5yW386gPeyrbXahvo02YwX7hmVSWKRtW_6vyWc3-Pz0MmchwLohoSrApv-Sl-mZdPSd6lJpx4bmKuZIKUPVXeCsUGtYW3ziFpy-NgoJIZMSBoFhFttcYwJ_GmknMNKkvg_pVVg82j5Y-CBGHUjdap-C5dLj6EhsOD_hQM4VoKP7Ftdxg1MujwgXszDQzsX6T7xvVLNGOnf-H9LxjX9NDfgxKSYWyOFy1obNiYlmtoBqDCgu-oPEwnZxCOdxbzWJpyI0GpWeOz5BeE2_OP4memZQBLzeYPn2fonwgtbjUs6PENTToeBsTj_Wpl9CWicQXOHoru-Arpauo9mLyp8c4CwLKHlcGczVgT5xPazURJu4UPk7ohFU5VcCb7Px0wr4g-2LXiwI85Q2CS_EMxuB0rpfaq1CIyD1RRCNzfK3dh5uVc25hctFkCdTbGFf2_zOW0VdGX7bAM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
🇲🇦
گل‌اول مراکش به اسکاتلند توسط سایباری
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.19K · <a href="https://t.me/Futball180TV/94549" target="_blank">📅 01:37 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94548">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">مراکش همین اول کارییییی زددددد</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/Futball180TV/94548" target="_blank">📅 01:32 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94547">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">گلگلگلگلگل</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/Futball180TV/94547" target="_blank">📅 01:32 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94546">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">کم کم بریم سراغ بازی حساس امشب</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/94546" target="_blank">📅 01:27 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94545">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E0yAJ-zjknesTwnHXVGJW_Ei-Z1VtW2IMRHykNmdaLVnZ-u_tzqsUeSq8llab5G8_nusefQ_l8_4AcNuF6wdI9Tq4MdD0Eae8Be2Pc1VSt8fE50_y7Ri-ySXX5a1MlYkOq71huOEAOQ_Oz_BNDUyrsIC9s7cyJlQ4mZuuTZbm1UVnRcf92IAFWi7F_cEN76zpZlu1NJFYUl8GSL1jL975SXgi46WndfmxA5uCuBcBIe50onUiz9SkK0aStL-XDDs5J4vFrZWuqKuWSlRad2ZQVvfzIylPRovbhK_OMh0sAhubWMaUkqyZf6wk7LiynzqhBg_Wq3m_bDOT_XzWGPHng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇸🇳
تیم ملی سنگال از مشکلات متعددی رنج می‌برد: پرداخت نشدن حقوق بازیکنان، انتخاب نامناسب هتل، برخی از بازیکنان به دلیل کیفیت پایین غذا مجبور به سفارش غذا از خارج از هتل می‌شوند و سرمربی این تیم چند ماه است که بدون قرارداد و دستمزد کار میکند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/94545" target="_blank">📅 01:11 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94544">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🚨
🇮🇹
👀
یه‌سری منابع خبری مدعی شدن که رونالدینیو تصمیم گرفته به فوتبال برگرده و‌ میخواد تو تیمی از لیگ‌سه ایتالیا فوتبال بازی کنه. باید دید رنگ‌و‌بوی واقعیت میگیره این خبر یا نه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/94544" target="_blank">📅 01:07 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94543">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NBH6qplBE_SwC_pKCHP38BwquzMPzfxFHmCRB4ubPQI782zeAS9KqTz95njPzL4LAnqggwwoKTxposC5WH0rec7oVreyQxTzI0Ac4EsZGBslog8-dGvVw8EL6RJlOjb6fzuiaw6qMRvgOGUzcn2QJE41AqokLJ3CMveJsNED3o5_wIcIpli_U4SwFEgJqghR2Mo9MUcwlrsl3Wcf26B5rDpQJegM1u5VKKrSfPO-4zw20wBXR1WsyXk0iROjrAuvYjVdjo2ds_yN9xbHvRCJPa0dRhLJXsIPuC3aju8LVf5Om2u6aX5jBr0px-QIwz2T-AvQkBjOUvaD4MZsANCXcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🗞
#فوووری
از فابریزیو رومانو؛ کانگ‌لی بازیکن پاری‌سن‌ژرمن مورد توجه اتلتیکومادرید قرار گرفته. بازیکن با باشگاه به توافق شخصی رسیده ولی مذاکرات بین دو باشگاه در روزهای آینده آغاز میشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/94543" target="_blank">📅 00:59 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94542">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N2dilgsR6cZaUkeBzA7hD-n9qgCoOEv_bwe5YJbcS50MQvzmHcKOOwAtkevSBSSE_R95RHqssXBtZWKVKID0qAR-14oCYItWRgy8J-GxKrbTXhzKump8wjag6KS4GcQJGScZknXBau4ziDONmeb77vBxFppuLFT1Vkhps2HLWvyP7t2SS9F5KWYCr2FVzKDA526QB8q4-U_WLlz902sfz8fZC_O6C1qFmvhSrP4BK5iDJJTz1rC1gUNO81qTyEnqxsrfQpNR6fPOZHtM2exAXzT_bH6Wgc6ksfBR09_BZXReaSM8tCnjw3VeXIwqxBjLZRZx_JWfMc_MP9_GD3f09g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
طبق گفته رسانه های انگلیسی مارکوس رشفورد از ناحیه کون مصدوم شده
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/94542" target="_blank">📅 00:52 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94541">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jysNcZ-cwrQBgZnHQX1NDbvQ-vKkNP77BYtgdQySA2VnNLKCMNUDShwvmBFfmxPioIxyucnMtz5vnSm_81-JZ7bIEtkqCmgqnuLH2AEdaDEXqfJky1q_4GvuQlDq6413v3frQMNGgR_hQx3HPwAt_IWLxoc66aUiotkiqFe_Q8ClDw9FrfK-MXi0Vjb7PMurzWCH34R7VVaXrNNIMOfeMNYX8vcLd4cIyitmOjvQXM-DdxWKUwVI6dVHyjTttYx2xEKFz03y7u1-MLFm9179eBOUcoIvJez-F6MjqvFDSzaEmknPB2s23BSvvhBKmrevHs8DaQMtwtEeREEkmNyATQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
📊
تیم ملی آمریکا تنها یک بازی از ۱۱ بازی آخر خود در مرحله گروهی جام جهانی رو باخته و اون هم مقابل آلمان در نسخه ۲۰۱۴ با نتیجه ۱-۰ بود.
✔️
۵ پیروزی
🤝
۵ تساوی
❌
۱ شکست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/94541" target="_blank">📅 00:49 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94540">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LGN3sB8DrekrrvJt0VUXtwnNqOVAfp4oiYHJC6GnPI10CkX01zKkzKGVuAO0A1XxBWhSHrNj_DZOQPCyVlw9HbKibyYSKt9DKbl0wuDBX1sjNtnzU_PnvApkoMmGCbcy89OkzRE6gxNzP6EuVS0yG9AUMC2ncjCxJfPnlrxYUKBfkZNkDorswJ8XJNEKgt77oROUcd09H-xwVR5PI03YCq9fDyNM2_lL3LBXZr9KzrrPM2gJfdg_P-q_j7bV0mgkyQWkq2rpxCqpIQx7r_-u6tdwBcfCbovcqursXRFvdzdXyql03XMA7HMZpeuZZiGklAJhQeNnYIxL25bBxIQ4Tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
بالوگون مهاجم تیم ملی آمریکا به عنوان بهترین بازیکن زمین انتخاب شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/94540" target="_blank">📅 00:47 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94539">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">✅
🔴
فقط نظاره گر فوتبال نباش پیش بینی کن و پول دربیار
💵
@palang_bet @palang_bet
@palang_bet @palang_bet</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/Futball180TV/94539" target="_blank">📅 00:47 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94538">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IXRUVZ2zZcDMpcKRXuxkgDIKmeus7u7awUxfkfiSi3mx2Plmp-okBmeJ4IUXnCXXL5bkkAEzgXpc1lG-e-6bJBZGg_5KPTdN6k1Ki3GRO-QCVNhMcvFSq8AFqTT2wa7T3NgGqQTzye7EIUbAkRBxBu9f-UqSEjOHgBzWslSusDN5dLTBo4SunX8Tw4G0KEBguJ-3qiTiqkoW7ldCtHnIPqKaNuREzNx3G5OjQV2deiWi6JgVgiS2V6_xhN63xvkO1eADF3YOuYJsj_nZoL2NkL6hZbNEgEeEbBuC2qxqAm7ysJx6SOz9RE_s-weN_9gEqpP_vqbsQ05-hi5UWjAOPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این آمار فقط مال روز اول
جام جهانیه
🔥
😤
میخوای از پیش بینی فوتبال پول در بیاری؟!
⚠️
تو
پلنگ بت
جویین شو
بهت آموزش میدم چطور پول دربیاری و تا اخر
جام جهانی
سود تپلی بکنی
❗️
اینجا میتونی روزانه درامد داشته باشی
💵
🔥
@palang_bet @palang_bet
@palang_bet @palang_bet</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/94538" target="_blank">📅 00:47 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94537">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ufIoHf2VunsTUa0sOLX-sOCv0mdFsxLusRTKcWtN7FK39deTSpkL1XCeCZyuTF7cG77YUQPuMLhNe-QQSNTZBaB5nzj2h4ysdk1PzlcYT4IHD6-Bw-dWDuNvs6fthJt0AXRDWihrCtyrvyiaLonirR9jRzrXTUFR3f9VlMar9IaPbRpu0JFAtMEk5V8B6MIzENHvh6x2LC_Q16xrbc_q-5PRxIxAgXxwB__FmXJhpJRw-9spbj-uoB8PKqJTBjSRrXmDoBjkCAT6Q1yEokIfNzudWekYdiKBpV_rkghGWW_xmL3n0y23xtk29l8FGIB8GB2CYquMPID4ERtSFJ7zGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدول رده‌بندی گروه D جام جهانی.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/Futball180TV/94537" target="_blank">📅 00:43 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94536">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C3DhzNwPayzhkHz7L2ioz4aOLAPTtYTXcwFm9QxUCDo3g8d5sSni5RhE14pNh5_3f0WuvlqnQMBWnGx3QwhXoTihss7PRdQ-FB90HbrEozSAO45PVkH8xsXiCWkiN7dWmAYXLBG6ZDnFtJEGFVK8ry61FHtTr6Y4XdvSo8PoEhxP1rUavEgZ7ZZy1HDzhEMiqQiHwDL67yl3ipCUt_bDXVDZqkhBhDqgVYAngViCCzPnRgKKfN_3KWOv1P9Zzn-kEuafBiqfMO6P9VB0VUiP196LhRNDn0SIlpTY2Z2-PKfW1wBeEH94tPNOiSH0ZC6DGsoZuLQ_Jmk3sGbfIoxhFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">داور مصدوم شد</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/Futball180TV/94536" target="_blank">📅 00:41 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94535">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZyCexYe4ZuySSjd6a1BhRmCidWQk3XJ5BzD4rYEZNxMedYvmuguJyhzNf7079fY83vCq9H-rZ82YTfYYIw0lpaZ5tZmx7N4eqC3SdVnl3eqMdQf-WcZlnhPQAXzeNqKV5XyicyEyZIfqkIwlzbs78ilovbUYFhEFTyuxu9q1Vz1NxITW2iAcOfE63kTPdB0YCvIB242jLGkbCNMH2WvSekq7LJSrR5siNlYssvsvlY6riRaPH_qanDuiQEkxBZF4zKLLMMHpjRABD_UGdYHMARGLDRjiX79vW6eUh7aylxBH_zSEurHXKi4fokGlFb0LVOyI3fhzNUDKV6D6qb3Liw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
🚨
تیم ملی آمریکا هم به عنوان دومین تیم به مرحله حذفی جام جهانی ۲۰۲۶ صعود کرد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/94535" target="_blank">📅 00:35 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94534">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/onNpMsyhsRcvqggbEACZ9QVXAZNFF0klDPW14nckKyWRTFvEKowpE2hrEBoYyyv74AG-1gMoO0-ea-q5n4dbCjihdobfiYOfAKga3YeCtAOaSdN3w6__ezYUuOzp4dlbdNXZKcqqjb9kPjC4gd95FEL18-XoiU6s7EmXU_chReHiI5u3--Kpg6Rc4KcSUQrZSpTSPo-UxkaiPMnsTvfA2QwAbvJ-MPw_CQjD8dofJGGG5pb5iBlgxPJKNebqSkXr0tOm2fDindUWQHc-ArGluOh5R4nbi8S-x8eorW9CTTv_mUFLj6DjqFH0FS5ZNN1ekT-agvoCDvyPrR4bTTHKvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
پایان‌بازی|نمایش برتر آمریکا؛ کانگوروها دست خالی زمین را ترک کردند.
🇺🇸
آمریکا
😀
-
😏
ا
سترالیا
🇦🇺
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/94534" target="_blank">📅 00:34 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94533">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">داور مصدوم شد</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/94533" target="_blank">📅 00:29 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94532">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">۶ دقیقه وقت اضافه</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/94532" target="_blank">📅 00:26 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94531">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">این دقایق برخوردا وسط زمین زیاده</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/94531" target="_blank">📅 00:24 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94530">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">استرالیا همش دنبال پنالتیه</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/94530" target="_blank">📅 00:19 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94529">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kdru-RJNCiOH_9Opx6mj0ModDLK6-VM55EmzrfpsQ2n5RxIN0qb1axVlN2l39gJcTXOT9Dn5Vbxjpz1MIM-G8SEk2t7JJQVSPQPd-a_UtQJBBRJzeushrk_R5alYRBSX_YWUxXIROP6aivh9Hjwev421ooY_s7pQ5mM9ERq3wFG1o4MQ-J_N1hJUUO8lnup5KhrwJP2j4ADp0gNZQBXUkVT1bjMDlA2p4gH-OOKLPDlX5eqNevBQwph0ejXDDwEsZLf6TKM9hzvGz0WgTEHFDjLlgc7dz6ZBJxjPLYaEdx_NjFCveI-xcsj8Dtap1bm7FUbMLnEa4MCOYMZQOTd37w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینو تو استادیومای آمریکا میدن 13 دلار
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/94529" target="_blank">📅 00:15 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94527">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uZQ0AgFCOE669tbgQ4_NnYNA-dEoxZEmoaEtYqqBCN3hqfJurOm_Wbcjy-fve9VDgvNxWhdoY0d9uzLKJZb1szTthvjIxEbO7H29GEneGNJMn-8ny_O0W056Qw2msCYEJI5gNEzZWSKJP1gm4-0FWAckbWDW1TGVARq0zHRDqIDuW8lawjGBoWhC5LJJWpsYpTTyNOFe1FtEzb1Q2V8tNc2MHm1IEAiUDUwGmuVTImm7BEwwDTTthfEggf-XnOiEtuJG2TIGYtLTly_J9rMLXDVIZAkFFBGregamkHeuxR2WvzadR_Y1d_0W5skbGzZ8deNUlPFSsp90T8mhQQHtXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uDATl8TtdobuvabhLo9KLYjoJqWm3Ds4YXKDkx2kJGZXIGiXUxgXCY-pB2ybqdWMjjCb-btVOIPiYfhi0E6tZIcaNBgKSv-jFR2M4cHdwccsb3eYJ-Q2CpHOkKy8Cc8Kf5E2clJweR0jWxMhEl9sZve_6LVdlDMMuaO813YckAQajOF4BJ2o8XaeThM2Dq7eWE0LNp_FL8SkPOdH0Ttg8E23aqm0pofpoOyxKoYiChmq0rnnu_YLdFlTClh1KWprIQ6twlUcDPp-fe9zp2uUimFIQW5DP9DlYgRbKqFHVHwQdL_vzyYD6XYbgHt8WFXgdO0yrvZFZlGaF6AwA2oijg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏴󠁧󠁢󠁳󠁣󠁴󠁿
🇲🇦
ترکیب اسکاتلند و مراکش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/94527" target="_blank">📅 00:13 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94526">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e3c41e3b9a.mp4?token=CryN75g9zRPSJ-KRsUVKt5yYJbvkJTh0JJlZqfZ3MJt9YgLf-KHNgswZFSaC_iGHEZ5XLWaFrO6glKkjKrsU7G4gU2mXFgIXl6Xv_plmiaobU9QQyQWiJJuWQGmmpvVR1qQ_M9A4mo1DqQsGCk8cs4DuFBrj0w8GqwB-mmjdEVj-hwpl6bU5zcPy19o6EjtrrK04KHkURdATz6moWDMxgN2K8xD4emJllyeEC5N7KGq7JSPumrzT_NwJsxtAlf_0vd09FZptnymAEkz50vI8_9JxPxiuedG0AhrrDnDpY36TS_ZLVAGe9zfV_InbEhXgyT6xtajTRSUZUNXzMz2OEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e3c41e3b9a.mp4?token=CryN75g9zRPSJ-KRsUVKt5yYJbvkJTh0JJlZqfZ3MJt9YgLf-KHNgswZFSaC_iGHEZ5XLWaFrO6glKkjKrsU7G4gU2mXFgIXl6Xv_plmiaobU9QQyQWiJJuWQGmmpvVR1qQ_M9A4mo1DqQsGCk8cs4DuFBrj0w8GqwB-mmjdEVj-hwpl6bU5zcPy19o6EjtrrK04KHkURdATz6moWDMxgN2K8xD4emJllyeEC5N7KGq7JSPumrzT_NwJsxtAlf_0vd09FZptnymAEkz50vI8_9JxPxiuedG0AhrrDnDpY36TS_ZLVAGe9zfV_InbEhXgyT6xtajTRSUZUNXzMz2OEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">میثاقی: باتوجه به اخبار به‌نظر می‌رسد ۵ تیر برای سهمیه آسیایی یک بازی بین پرسپولیس با چادرملو برگزار شود و برنده باید با گل‌گهر بازی کند/ گل‌گهر و چادرملو هنوز تمرینات خود را شروع نکرده‌اند/پرسپولیسی‌ها چیزی را می‌دانستند که بقیه از آن اطلاع نداشتند و تمرینات خود را خیلی زودتر شروع کردند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/94526" target="_blank">📅 00:13 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94525">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">استرالیا داره فشار میاره</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/94525" target="_blank">📅 00:12 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94522">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I0GruEcymKEIYLLN5_KbGd3vCl0rPAu-Nsp6pFpxFj8gM2XTW-mY-LbCih94vZHd8aMt6wIvQSHySJ6nxM2p-FPcqphNjgHRX_Ea3P__P5epLU-tSJ4Jp1j3BIz6KRM5o-VpXwJLljwOFKVs-CLbB0ETYfHg0FuIkgZSrYSQylDKqjqHHvTPSVvg3ezx6TxnW6qNTCKcqC2JELvB6VA2uBk20D299Lnyjp-putdy4CGEflHwG6nETDn65AwVGQ_FdDqF0BPOJDQLOIN-mWSNpyzXAw0LxLr0gyyZ3YX5UF6BfUm5h8IRn8cH-Lw99rd1X4L9kA2XTwsFGFUgLRJayA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
👀
پست جدید رونالدو تو اینستاگرام: مثل همیشه متحد
🇵🇹
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/94522" target="_blank">📅 00:01 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94521">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">وااااااای چه ضدحمله ای زد استرالیا خرابش کردن</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/94521" target="_blank">📅 23:57 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94519">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/puaAhdAagJAgi5bjdPKTpZYV3rnBsI7D8zuvvdqjjIVhw65H2EetmC7ukn68UhUrIMiIgvBABYqHuFdwC_TOfOQrhUj8CzBA2cr3obMNJaWSCp3Yl4XeRYcB8Gb5FRXKQdc5_OpnryHehCtONMjvUblOVbCVJZvAGCwFZ8Dau2uh4rqWpBgIvECkBLATKcRcvlaklyiQG3_yn_NiXx1WKlTR_E1O8fGBSnYReplxFV7vfZ8ZIBTJcqIsMdSTiV1yJkq_QcsPEssx_efB_mSCUvtF4vMM5QbNzHr2nujUD0H_Cm8x4P9rFfkoi5SYrGUs01gg9wPP-_L-RU6rXlmGfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Bh3XiYuD9eUd5j1A_PPNFkMV3y4SiY1RajhpGSMvT3zzW8LT9tYbjGdDEoNbngTOWB5FMSa1qQK_o40v_cpC-asABBkwjzhN8lYJZW7FcWarfupcWnw-fDSS50ismglUFBbL6cyCcaMYAWkXZ294l4ReWl3a_7BJ3073xoXoPebMzF8OsTeYoCcUvWn4PcPNcJa1nmb3SC8Wb3CuBgEk4jNYlyR805UHfgsHGrXdma6zaz6aPmcBPtZbcFvGc7ggL3ipF863yr9t8KcvPX0idYDl8svqNLdpCtLMZbREJj7W4yJU3YM5Cz3kBE86RSF8qJsU64OUBdUBbNVCqGNDKQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">تینتی رادمن بازیکن تیم ملی بانوان آمریکا قبل بازی‌ توپو آورد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/94519" target="_blank">📅 23:50 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94518">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">واااااااای چیووووو خراب کرد بالوگان</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/94518" target="_blank">📅 23:47 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94517">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">بریم واسه شروع نیمه دوم</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/94517" target="_blank">📅 23:40 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94516">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0663a525c5.mp4?token=ibJXBHExPofR2D1EWZLWM0vqTscxjxC6CcguuBx5Rxj_oH_khP-C4vGor0_Y_Zrj2vrX1KDx9pYRngTFr4mBJvhSuIj8fWmi42ubZ7TWrszQrl3OaP9qWaWlIaErHj9k2yz2xicyvjE4__PSMaTTIYH1NNBi5wMVASrkQP1MDZCZmzGQszWz4x3sed1ki69ISnM2MhZPHyXr2j9kYmC4x5WuonNv1qm2nsIEjj_W4sFCUBVu-Y5ClQwoqWWW2Pf67WVZ4BBnZqxxACbXF7l2bmv2EQWDddYukJ_pQUxK7pBHJF9iLHMJUkKIeRlFIgP9dRoFLuPdqwjtf9B8WSuRQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0663a525c5.mp4?token=ibJXBHExPofR2D1EWZLWM0vqTscxjxC6CcguuBx5Rxj_oH_khP-C4vGor0_Y_Zrj2vrX1KDx9pYRngTFr4mBJvhSuIj8fWmi42ubZ7TWrszQrl3OaP9qWaWlIaErHj9k2yz2xicyvjE4__PSMaTTIYH1NNBi5wMVASrkQP1MDZCZmzGQszWz4x3sed1ki69ISnM2MhZPHyXr2j9kYmC4x5WuonNv1qm2nsIEjj_W4sFCUBVu-Y5ClQwoqWWW2Pf67WVZ4BBnZqxxACbXF7l2bmv2EQWDddYukJ_pQUxK7pBHJF9iLHMJUkKIeRlFIgP9dRoFLuPdqwjtf9B8WSuRQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جدول‌ گلزنان جام جهانی:
گل بخودی - 7 گل
لیونل مسی - 3 گل
جاناتان دیوید - 3 گل
کیلیان امباپه - 2 گل
ارلینگ هالند - 2 گل
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/94516" target="_blank">📅 23:29 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94515">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/58175e8427.mp4?token=SqHrXbu5wg4tW_lLGAaYNH5MzFkGMKvfAnbFg6I8NpXiq1EahJVdv6YTx65OwmrcUa07_nyasrF8EcSOWvKjrQyyyYn7JRZW66PiXMM_zGh1dzIODA_Uey1PelVFNpS2xhyXH70k6uXZ9qE_qLFKjNt4kl6dVd8v7bIOyb5m_czBvCSp9Ir53HoetmUFQtLY2jDotuMdHBRLHFRc2A7QbFljwvCwFL3sqP08UdehmV7Xw9yjQ4I-pyTnClijT-55CzhLDIb4l9aTBK99YeVyFI_quP2fDetI2vJowGBZ5vi_cdUDG0ozXvuJSWWfTW80f7qAIfDgrtWdGY6YZrupSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/58175e8427.mp4?token=SqHrXbu5wg4tW_lLGAaYNH5MzFkGMKvfAnbFg6I8NpXiq1EahJVdv6YTx65OwmrcUa07_nyasrF8EcSOWvKjrQyyyYn7JRZW66PiXMM_zGh1dzIODA_Uey1PelVFNpS2xhyXH70k6uXZ9qE_qLFKjNt4kl6dVd8v7bIOyb5m_czBvCSp9Ir53HoetmUFQtLY2jDotuMdHBRLHFRc2A7QbFljwvCwFL3sqP08UdehmV7Xw9yjQ4I-pyTnClijT-55CzhLDIb4l9aTBK99YeVyFI_quP2fDetI2vJowGBZ5vi_cdUDG0ozXvuJSWWfTW80f7qAIfDgrtWdGY6YZrupSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زلاتان و تیری هانری به یاد قدیما اینجوری براتون دلبری کردن
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/94515" target="_blank">📅 23:24 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94514">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa27036b6c.mp4?token=RfbuqvYZlS2Z-1xHesKNITJwoq5D5uH7crF2DuARUvwJ-55OnugqGbMBr5-WSGAoKUMedoFBdvKBu3_edO2Me-SYJ2uBIIXT7jIWqx-Vna9kGWA4u9NkV1dRF9iZbJ7pEIQuoQxD3d2ITVvaSxHdpkLyzHMSF0XFKGoZu74IwtTbV3GzpHm6WAXIn099trKUsC2Fgay-mk3lPcErkOGp_FuVbGnFRy_WxHQA-gHPKfarEG6ML1b-7iqOvNUJ8kw9_4AQ_8UfC-UPCfAyOhuRqQJ_Ehivd47Nf-zFfyhnwmYcTtDEXFOTCh9qIDEfgMaT0K5nGjt8RC5EU0YkVRY0Bg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa27036b6c.mp4?token=RfbuqvYZlS2Z-1xHesKNITJwoq5D5uH7crF2DuARUvwJ-55OnugqGbMBr5-WSGAoKUMedoFBdvKBu3_edO2Me-SYJ2uBIIXT7jIWqx-Vna9kGWA4u9NkV1dRF9iZbJ7pEIQuoQxD3d2ITVvaSxHdpkLyzHMSF0XFKGoZu74IwtTbV3GzpHm6WAXIn099trKUsC2Fgay-mk3lPcErkOGp_FuVbGnFRy_WxHQA-gHPKfarEG6ML1b-7iqOvNUJ8kw9_4AQ_8UfC-UPCfAyOhuRqQJ_Ehivd47Nf-zFfyhnwmYcTtDEXFOTCh9qIDEfgMaT0K5nGjt8RC5EU0YkVRY0Bg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">میثاقی: به‌زودی جلسه مهم کمیته استیناف برای یک سهمیه آسیایی برگزار می‌شود/پرسپولیسی‌ها خیلی محکم درحال تمرین هستند و به‌نظر چیزی را می‌دانند که بقیه از آن اطلاع ندارند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/94514" target="_blank">📅 23:24 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94513">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">پایان نیمه اول؛
🇺🇸
آمریکا 2 - 0 استرالیا
🇦🇺
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/94513" target="_blank">📅 23:23 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94512">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🇺🇸
گل دوم آمریکا به استرالیا توسط فریمن.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/94512" target="_blank">📅 23:16 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94511">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">رفت وار</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/94511" target="_blank">📅 23:15 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94510">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">آفساید اعلام شد</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/94510" target="_blank">📅 23:14 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94509">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">گلللللللل دوم آمریکا</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/94509" target="_blank">📅 23:14 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94506">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">گلللللللل دوم آمریکا</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/94506" target="_blank">📅 23:13 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94505">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v229UU66wbl0w_E4YdOvyz5wAk45Cag-5-0-KlMg57AEpGBj4PHNg9AzhVOuS0kkENpCcS8SrftiIGi469ZiTDUXsYGdVJvmRMu8SyIwDx-iszcOgIXMIJsTW5tZxXSSckOlu9jbxbtx8VKO_B9kgXVS4EIUxLduKJSCs0QSInGOqGKTh_sEqB2kSY4541cX_mVRudN1hoKEXGbbMHkHLP3R8csFumWtMJzb3eUY7qxLEGAA65MUUpdvEIOw4AUuI2yoEinIS6JIFFDbRbjP2fnhTuOIjyo1w2t4I3vFf7CFP3m7lpAxXFKLHbbKsoxdQ7QTrdp4wBtS-3XKKTmd8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇺
خطای مشابه خطای مسی توسط بازیکن استرالیا که این بازیکن هم اخراج نشد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/94505" target="_blank">📅 23:10 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94504">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h3R56SRpjO11urdfYSI1GwZjD3MDAZuvt9I6pMMRK29LnQQ_uk7BRLJ4BjKRkYmpdgBjSeQWPwzWFOI-XMqNZyYOwZ8g8LPpDXa_GUEwTseVExCxDQ5e5qvErSWn3QGk9b2JMHkoKZkmBHh6spMYSgaOZxAouu85d3fF5VBe4nR9ur8WiAquSvnkRdKk7UknkBw7YU68ZdOX6yho_WtUe4-E3JwxceNwpJ3tDru4VAKG_iBQHL9ppY2JNLrJe3tYC0XsfZOFkXwbgD5g8O9PIsxpFJAPEnvKFuwiX3jMvrmH8WpEXlLBT6qdVuuA1K4nYRhj1y7UKV4ateG6cOuTHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🇲🇽
🔺
تقریباً پونصد هزار هوادار دیشب در خیابان‌های مکزیکوسیتی جمع شدند تا پیروزی مکزیک در جام جهانی مقابل کره جنوبی را جشن بگیرند و این معادل هست با:
🔹
بیش از 5 بار پر کردن ورزشگاه ومبلی
🔹
تقریباً کل جمعیت منچستر
🔹
نصف جمعیت آمستردام
🔹
تقریباً ۳ برابر جمعیت کوراسائو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/94504" target="_blank">📅 23:06 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94503">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cm66oGUkWsxiFY_57Ix4JKaUJPhZgZ1f67FvpfiLfR1gqWdgCWUO0EkTX4-CbftZcptN8eyFBXaZjSBMIZdJX33hkD8wu5n1RTrFI1z_FontsTXlWzGREHHCfDUu5kfZjEdgSfmr9IQ9w24HSSqeT6hlaxBF8shXZuIGbrybg_o9zXPzSBNN6j00T2XDZnY7jsjbMSeBcBW3mULVtAQxN8Q4yzBIPQgBt9DJfZlV2Uyb8wmnvQj_bxGeUoNmAxNcVSVFM90NbHKwh8iJ7n-FDBixgqLBqeZtHOzYJNMq2gG22whdGuf_NiJXs6J7rJs54UgzQOA-7j-f5KU4NEnqHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
جوایز ویژه قهرمانان جام همراه من
در «جام همراه من» هر پیش‌بینی درست، شما را یک قدم به جوایز ویژه نزدیک‌تر می‌کند. در پایان این رقابت، سه نفر برتر جدول امتیازات برنده جوایزی کم‌نظیر و ارزشمند خواهند شد.
🥇
نفر اول یک سیم‌کارت ۰۹۱۲ کد ۱ همراه اول دریافت می‌کند.
🥈
🥉
نفرات دوم و سوم نیز به ترتیب برنده سیم‌کارت‌های ۰۹۱۲ با کدهای ۲ و ۳ خواهند شد.
علاوه بر این، هر سه نفر برتر یک گوشی پرچمدار Samsung Galaxy S26 Ultra نیز به عنوان جایزه دریافت می‌کنند.
سیم‌کارت‌های ۰۹۱۲ از ارزشمندترین و پرطرفدارترین شماره‌های همراه اول به شمار می‌روند. حالا باید منتظر ماند و دید در پایان «
جام همراه من
» این جوایز ویژه به چه کسانی می‌رسد.</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/94503" target="_blank">📅 23:06 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94502">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🇺🇸
گل اول آمریکا به استرالیا روی گل بخودی برجس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/94502" target="_blank">📅 22:43 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94501">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">گل بخودی
😂</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/94501" target="_blank">📅 22:41 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94500">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">گلگلگگلگلگلگلگ</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/94500" target="_blank">📅 22:41 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94499">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">گللللللللل آمریکااا</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/94499" target="_blank">📅 22:41 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94498">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dd6Nx-ybf5GDA7ZzINjnNhmoC7vWImWzqMlMEU7mhjzNU8xj6OxYMaEEfIZ5PYiTmEAbDwSgHZMinpiFEw1DY9QnDgnaWDriGG9Ahl1Q8EQK-956U8a_WGzdcEqKacoUfB3bUzRACE_1bO3SbkscZ-nk7IjQ_ms3nVhyhYdSYe6FzgHGIKtlqqFQ2Nb9R3wE1oP1zH7DbD5MGUHg2KbEg0jd1k-f4D3esyL_o22bqc-FdUDpmYAQkriTTIhOZsL1kUrCBN1CEgybQ2ykJHf47ocZlzSMSLU2yjn0GWDE-ImbP-aKhTBX2PqOGgSXDGBoch0i1NEXWiweWDcAAiYz2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ ببین کاراتو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/94498" target="_blank">📅 22:32 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94497">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">بریم سراغ بازی استرالیا و آمریکا</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/94497" target="_blank">📅 22:30 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94496">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q6JFsOaDbJinXpUSQvrAVprvi3z4kdO82ciVPmIgjoKUSUfBfNtutHfHNbdCP1ZFqC46O5fPWmE7aE3uKrxSF2_pos9QuA0KhwRxRd6ntt5-4XsKIrM3k1rFnmoEm8mAG4NcFBwB8wqUy4VJSMd7pK3nGrs3jT4l6YCFceQxMvuH5i4sMduf2zRWULQd9lNwZzQi6lxSzdAAYT0VC5nIbA1xNVrdzr5CPP44gARPTNMzTx9_8s4MvBjh1an4z9bSiPifFRAu8Aeg_ydjLMi0ILUIbZXvCHFfK_Z3nfG1tFjE5fjGsBjRn4GclQN3YQgXMktHIXaUq05EX_-t-sbFDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ژائو نوس 240 کا فحش خورد سر یه مصاحبه
😆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/94496" target="_blank">📅 22:21 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94495">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UR9nc7VI-woK8N8H3A9yjlXakYuvbQ0VgSxQjSfyc5q2u2g9UHiHWI3DLXH4EFJBoc7RUuRVKvaK4aNeS8XVd5ulrOutKaJGl4gUNs2Ek9dKVdan5YrpDFCW10sJaa6NfabZ2eTXvlr8jqHuxhGBLmSYCkyEpwtXSlRC-T_Nxjv88So26yKqC7cn95ziA6bY1u_Hb2ZYGVIEUB_5K1VHUAuj8aLqdujQp2rQS30LpAI-l-Txoi-WBiL7CvKT5Lt-dMzXX34SDLk8mfiS7k56d69vuCBx6SOARKBThELNqMze6E4RY35agpRamzsyJZqRwjmrX3q23TDejvyeRqVjgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زیبایی ببینیم از بازی امشب
💗
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/94495" target="_blank">📅 21:59 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94494">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mtIuPbSrIhZlaeEOhoYQTJQniBpVKt5BEbzsFDT3P_kdvmWuJdc4blOVw-6jd8yF8hgeBiYYoO1igvA5iEuIolZOsAdcLhgBDMpA7dEGH3syyP-VhR6QA_DP2aTQimP0QruX6tJHZj3SKH5cK4U0svg0arlc4u4Z9gYtBS39Fp9kfO7UuvkA7ULySr6PSfxqr0qb6Q30hioAzYTSgKHzIq-eDcoD25pawZPrtCzhGGlfbC5gykft-BEhB91WiI0A3w1xEXulJWMaUegIPEk0L3ESv44qITU7EUNnnihzGUOFsDPqCpXM4GDTbl6eJuDBahuH32q9McY22K5p_9S0OQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
‼️
تونی کروس خطاب به ژائو نوس:
اگه ژائو نوس واقعا خودشو با رونالدو برابر دونسته فکر کنم یه توضیح به رونالدو و دنیای فوتبال بدهکاره. رونالدو 20 سال از زندگیشو مقابل بهترین‌ها جنگید تا خودشو ثابت کنه اون با 21 سال سن خودشو با رونالدو مقایسه میکنه؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/Futball180TV/94494" target="_blank">📅 21:55 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94493">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CVajkJ15pmqxarrhAYkGe-uVA5brNIsjLGGNG9NfbEnq4hhrNZctpxMVml92pN40w-VTcpEIe4t_sq1jhmAZOcSuRbSwd1GmrAAgPezsS-oSJmmxQIiKNMpQSx0kE3CY813FDRkuAMJ2f_2R_ySsLwqJEIh-uVmirynZKFUhXmDIWNpY1HgBTiS5gyiXkI5p2Rf0aXXldhM1Blvk7J5CEQKXgqVnYJzgVpxum0GhYXhEXqzwp3yDKKSJAyjm-rDEsC7c7-LVCP-ZxlsQbJy3VBcEz7gjKZ6nSScseIMwvpqend6nNKC5SKI5t6IQX0niS8XCkKpkoiZbFyB0cYjhsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
🇫🇷
🐐
تیری‌آنری: لیونل مسی اجازه می‌دهد پای چپش به جای او صحبت کند. هرگز نخواهی شنید که لئو بگوید: «من بهترینم» یا اینطور درباره خودش صحبت کند. هرگز
❌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/94493" target="_blank">📅 21:40 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94492">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OqDovFnwK2IUrF4ULPlutS21qw-LrTNo6TlOZM4T7iSeT2U8pAsF0zNkE0mnzLQu5Iru9wdT4upB_iLuog7DLBH1rGqBZzVzFwLApmGo1worbLJFhi3Fvm4fEmcUCrJbN0AN7U2yHW9A8cU0F1pFOiEzxoT8jfK2cPqzZOpZj1qP00HqwmoZoGBrRh9j2nwufar_UpqifQeAuvWp5pQnbnLXF1NT5uO3myH0W8FHy9I7tutT2Ma8axvIU87_aYFUZPhRHuSoz75NvJBbwYRk3T7sNZCMYOFsSAfcPVbRf24iWH34GybvOzs_WTWQVs834oZCSu7OT1-W7SDAtaZLYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
وضعیت پای کونه بازیکن کانادا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/94492" target="_blank">📅 21:29 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94491">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ppdiLQSQMKszmkSn4jx-09UKyJpR_aOLuWTzKNrQUAU9gP_7T8s9R8MXOFVyL82nAdHxP6DMYyIKw3SDc5804shnHNnS50HR2UYi7ZVHoVd1Rvi92s3dj8xR1boqKkPxQ8sjiVsKSQJSoiH_aWQppO24YRM3iVUcDtZrozMhsVwNckkTGmNU-AyC8qw4gJqQpllby1VTUwAnVkW4Na-7wdSJq1In8nfgjr9MMGex-Dj_Rfxr-FCJ7QF082QZg09fF1fbYBhEPG2yQuWFKLNkcLbe5u9MmLF8dtTsh9KhR7UOR9TAgWuVV6tuBsoHtGaVdJNVAlyBhErL141es_4dVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇺
🆚
🇺🇸
۲۹ خرداد
🗓️
۲۲:۳۰
⏰
آمریکا
🆚
استرالیا
📌
نبرد دو تیم پیروز هفته نخست برای صدرنشینی گروه
؛
جایی که هر دو تیم با کسب سه امتیاز در بازی اول، حالا برای نزدیک‌تر شدن به صعود و تثبیت جایگاه خود در صدر جدول به میدان می‌آیند.
⚽
🔥
آمریکا، میزبان رقابت‌ها که پس از پیروزی پرگل مقابل پاراگوئه، حالا به دنبال قطعی کردن صعود و ادامه روند درخشان خود در حضور هوادارانش است در مقابل استرالیا، تیمی منظم و جنگنده که با پیروزی ارزشمند برابر ترکیه نشان داد برای حضور در مرحله بعدی برنامه‌های بزرگی دارد.
🚀
⚡️
آیا آمریکا می‌تواند با دومین پیروزی متوالی، صعودی زودهنگام را جشن بگیرد؟
یا استرالیا با متوقف کردن میزبان، گام بلندی به سوی صدرنشینی گروه برمی‌دارد؟
👀
🏆
🚀
بتگرام در تمام مسابقات جام جهانی ۲۰۲۶ همراه شماست؛
با پوشش کامل بازی‌ها، آپشن‌های متنوع و هیجان لحظه‌به‌لحظه رقابت‌ها.
👉
🌐
🚀
betegram.com/affiliates?btag=3_l7
🔥
⚽</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/94491" target="_blank">📅 21:29 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94490">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RzlCa2SDQdWvesf4BvimIVhJ7GvIfD9SEMkIe_EZxXL7y_F0Xen5i47sj9-raNbWolfHmUu1JZCqCgJMWSN3_hxbBc2ASEl_vaQMJNreyKrCNcRV_6-N3974u0R8UVhdQc9_qZGB5nbPW2CGhToU_QC2PUiWNHn2gkse2no009Un9ShG9OQ0kLHyTyGV_uimQJXGdFQHm_8sJIES-caYC93mM9pmCy8ogSo8chlw4OQuAuCu0moqAnC3HKLC4J8Nrvl633Yy66XOuIMjPNISV0iDEJDT2emf0w-k1_K29y30nmRBM3SmkUxVDQ-tR7qBZpA-ZcneiGkfkbzrfrXfBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
رومانو:
بارسلونا برای جذب خوزه کایسدو، وینگر متولد ۲۰۰۷ از تیم کیتو به توافق کامل رسید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/94490" target="_blank">📅 21:22 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94485">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NVV9pP-TeGNZosy5aroaoRTWXBz-MQzrrXpJsqKqWPBkGSt3u3o7fvERTObApypF2FTxVy1xuIENTzwLxWiNywqY6l9JjhfmQMmyMmqv8JcU8OM0oe3mrJUjCI4DYY2aM0X2N2Sto6x4gywzDFwNBx0lqkIdXVPwH2c3eQyVg2gwGipDW_Q2WloYpzYQUUx5eFJJB9vPajcSYxm-YHnsgoAanMe855rKmQbPRIEMr3RMBVWLcWeAY-1Zk7mppBI2XbOsYgOVHDt8z0iG8iHioQs9-fXaaEN0P9_qwUZQNQknGkvakLUeBdbrGM6-cJUyVaiWkmQEcrza7rTk7ewtow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pmpJCuwGGMRVt0NO7kqBWvPPyf5mwTe11QqLMt7EUada7Pmv6F_DeARiI00pr1ywcJh7fUS3GeYiI95qf3xNnVXIkK0gohzEuhe0BsWbXwodw_IwWSPISysMrDNelSgDTlzYHtvLSF7gJ2zT5bpC6wc3aw1FzJIeZWB-AJmpTeKmH_xjv-CtIHlaaQyVm6FT0_J8XNUymmBzwkjkYuu6ABuI0KbPO22G6Xbl2uKHa7RfjHNdeU_eVcrGgMOVfJ673BzbZlT4EegzFkSObt42rWtEJj1XmDZ_8aFHB7qtdfG8w5fW2iPnNikqrZ1WwfA_uhCvbqlQ4ZzPJTZxvyCEfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IhtAq70MjMkkNjmHMwXBbSV8LbFBBhdXN-uyA1myRRP9SJv-t5cxjkKjcokRVCD7hDuxy_9hwhXW1FEbM-n9D9hPMWfGcHg22c4vJmDQnjrhSm2zybPmtwp5H34mXex16OQw4U2FcUEDwUP2JrPSVDKttzuLds5aa-KaD6gimnmJMfZjPINH11bfL5Lbnt0rUauZhfII5prCNgQs9SoMQypWdeauI72pEhey-jGFDC-dUZXC8ePK0HnRIOBi4WuLhnpRsAG8ALW9zsjuJY8VP0Yqb1B80adhReEm4syhgxkb3eAbD-yGd0Dmmct7LrbLUnIfN2fjhmipspx5s5sfrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/idgKXevsM4pot1he727j1czLQVZ-AzX8qj0BZd9x5li3dRbcMfcphsItN-nhvVLI674KkKD6ov0rN7B6U6EWrS1UFqN5wQasYJ4FU_9xlOUU6v1WHBA4aMCgWoEDzXzh3a1vJgcXjSNewJQzDaMnh9DKgF97bwupgm_pHqO9lP490t_6jCFnXGwaOyfVDSdCPG4T2LwjPOwotsIUENzZzJkLUljeMHq5p_GfP07oYOI8glyOefP_CUrfxGm2AhSzlv3HqtHBR8al8ZNewYcS9JzAYT-bp4JsuiJlkynb-aimJOyDpX1quv0sDA-jB-1D_tfliIlVO0Zzt_WbMSIYGA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">همچنان با فنای زیبای مکزیک که تموم شدنی نیستن
😍
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/94485" target="_blank">📅 21:08 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94483">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/D8GE41jp51LnXJqItV4xRThnwKY7C-sXWUYvhb9vwJ1fS5wPlkGgqTgspsa3j-MsCV2YwkAhCmfu7zGEhNIlReQQNJG_NgdSbw_Wt-GF-KXEZpT7tVAhQVC52gLVzf6MDSLrLltz67OntwpDd0IoGECqzQ2fAjmsAMap3OsL9i4H8v3oASsMDoKWJnUU2M7tzb443_r8RSg2d45Fkt-T3zjK_RCwMKMUwp6HLvL0T-8tkkGmcLkSKI5mToFgCSxDXzzmLjbmSbRmZJ4yxnH_wYOwC5CN7JlkOGD07m-PKTjgg08vj8bMhmWdSA46hes3CUBH3AmVrAi-zN-uKcI6bQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZSmnTAs90CFEsHr-TIShlltxR8UysNM05KoCPeNQkTU53pFTbQRlRj_iFMzg0iocCPI9MowQDsA00Ae4M5QpD6ngh5ot0TOhGNqqNR4u7py7y8dryXg3u_HB7VTQqtEq7Avp5X3K8qHikini5tfQHtGXXTzekIVZLJ-gAZJFVBlVPm01LOE8MNtKSpwDYbBSXmX_pMNV5SQBeRU-TpRAgnmYyg8t03Atoxjs-Zj9LI30wTGOPLKye-U8d-9jBqVQL-BUHu51NW-IBXf5KxGyidQ6DCxwpjrHB9OGj9GPKAG8tVJF5_xflCeYqSC1LL-jqcPqnHX8W53c2TCQBqMHJw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇺🇸
🇦🇺
ترکیب رسمی آمریکا و استرالیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/94483" target="_blank">📅 21:08 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94482">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ck2nd3DWqu3RhaN6X3jW7Zf3q51K4raUfoKHf3A8RzD3cTscWjuldWm_HWfgzndYqAVWcVYOnQsa_4njsMC5dglVadq7o-_I9XvRuoiazVqMU7iqYOO1bdZFx3R4OS9DGpnLfJYlVHS4IloJIB0V8sC2IvprT8G2Y-rYhbPpO43tKW-kj0XgCCDJs7bWyS9rYvjC7dcKvh3YTUbzwta4OYJT0U4FZnRcLovC1HdrbIYFrHonFgSH54YEbkwbKIsr__mndEh0IGKnB3iNfj8_ob6hjNZzwrVjedH1AXI8QS1kgd52F10AT60J0aI5E5VOlpLo298-XGaSD7gKJHqs_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
🚨
کریستین پولیشیچ به دلیل مصدومیت در ساق پا مقابل استرالیا بازی نخواهد کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/94482" target="_blank">📅 21:06 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94481">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nR8u0O-ACESjzLvk3nZ9HAbWpzxv7Qy47cvc1ZZt0lupf7l8O88WLRQ2ndCz8mZPzdiXu-F2iUK0tB-oKAUtjxtVhK29L6vCaARRXj9_t_OSwI05ac20wHZ2sQsK51OAu3kbOBqZiRyNadMPW_9LTr-IkYwBzl8iWC2H-WSss_xc3vdDOWi0Ec_S87ObWLexGrGQsYRM4QQoQki16JYhKGBxzOQcIBeaHVcbt-IR63X44Dx-wXvNFUoPDx97BvStTjFNJdNYt5LbCLQX524eaxakbNjiB7V-poKtW3pNWb81GZ0ZQgwAmaXMuVciPudVSDqFyg2oCcKh0KCDaY5UMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📰
🔻
رومانو:
کریستنسن دائم المصدوم یه فصل دیگه با بارسلونا تمدید کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/94481" target="_blank">📅 20:50 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94480">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f52919070b.mp4?token=H7UcvNUcmPtVlPaDOsTAM-Pnayk8oYYhHtseGSbdMyE31xuiCauSAWPK-oYPH9onmprUo5hzyZy6RouC55h_fEuASPAMDT2CsNp89w1cqKYt3sGhbCIAU9JcfI5VOnvLGieguBlJDzWXDuvQXEQn8HUC_WEeh6-G6ssrb8oZD28zHn3G-8moCjjvA9vYxEV3VLDTon8oOjw2pgnVRX13tlEEfGF2SPJM_B2DoWiLb6SvvwxVlrKknQqyCxlG_TQPuYQAW0zaACqQp-PTmF_4HM5CyFI7cMjeAJehxNhCb2cU4IxqPq5vCwTTh5LjQ_cGQ7uIhscjfSTYMqQuB6oJew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f52919070b.mp4?token=H7UcvNUcmPtVlPaDOsTAM-Pnayk8oYYhHtseGSbdMyE31xuiCauSAWPK-oYPH9onmprUo5hzyZy6RouC55h_fEuASPAMDT2CsNp89w1cqKYt3sGhbCIAU9JcfI5VOnvLGieguBlJDzWXDuvQXEQn8HUC_WEeh6-G6ssrb8oZD28zHn3G-8moCjjvA9vYxEV3VLDTon8oOjw2pgnVRX13tlEEfGF2SPJM_B2DoWiLb6SvvwxVlrKknQqyCxlG_TQPuYQAW0zaACqQp-PTmF_4HM5CyFI7cMjeAJehxNhCb2cU4IxqPq5vCwTTh5LjQ_cGQ7uIhscjfSTYMqQuB6oJew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جوری که بازیکنای آرژانتین تو زمین مسی رو پیدا میکنن
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/94480" target="_blank">📅 20:42 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94479">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m_ohwurHb4fRq0m64qwrpYQcRDdADuPArkR1HDRTawNRMYt0WP9S-NjAnoYj0LQE_Jb1bdZYQ9ImMq2Vvlcam2c9OSDhURRWrhPwgXHjoB-otwgrca_6J-UwNVztmPscs9EeBX3-Nb53GzEsRikD_ICz0dKHgy9LuwRTmIJJ-Z_-bRyVI0rY-wWSjCRJ5h1QJHAkz46yvmqp8e5xdFshBdRaLnSJmNWwBalpXdS1txtD34CWFX7kGFDBJXboMf-XwRzQzaT0ug7Qqa7EOb9Fvzcr2sXr_5jA5lyK-B21W1DAFE7Rpu3oPrs1nq4enAmSbuekGbVJX1_6TYNJH3OPzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
رومانو: اتلتیکو مادرید با الخاندرو گریمالدو به توافق شخصی رسیده است و انتظار می‌رود این قرارداد به زودی تکمیل شود.
🔹
ارزش این قرارداد 12 میلیون یورو است.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/94479" target="_blank">📅 20:42 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94478">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o1gARa2EGmCFbpRQ9sggosYWPDQZpntWFIBaGW5ChjLP-um3V2e3HPwALpsuGS_MtMchJ8jesVez3RXEwiGNWWj1YaOGgcC33fK0Je8UlHrKdariafIlaPNb3hrWnZiRiHde_y8A6LEH8s4SZrcL2Ff0MyZfC2eL34YPgd1RfQKrI48W3pTddFQGh8Jta_78ErTEggce4fyHO9iJM4QubuG-XMhT12u1C2XYBti-XXn1EOb_8QacEl6UkcFFhqPULTjzj54MfAJtiXehIuylm90bt8XwsJuslEK6W8w1ISwKFLJC99ASUuh9Jf87OnTV8e_T74XUhSYfxytbtXCxOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🚨
🚨
🚨
🔺
#فوریییییی
:
‏فدراسیون فوتبال الجزایر رسما از داور بازی الجزایر - آرژانتین به دلیل تصمیمات جنجالیش شکایت کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/94478" target="_blank">📅 20:34 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94477">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e-VeH5_qyvA9Lpa5CmA8ipfj08vrFGkoC4kGn-0T3G87yjdPb3i5PaDTRELGg-ae3OuaPbepV6v8m7p3czCQMKV6knmcYdNyLz83SA2srReat6eVD0ern6JenS0YhSJmxRNBk8Ax7P2MlaTcXI6cfVbgTkjx1CaZlpmNJYWWX8kbWhZtP6dNEdVqj5R5kFjDdmLkEBclm4TNYZV1b_Bvb0pnFzxlBhFJtIVZY2uLDEo_YkG5eQ-TV_b5-BKgK8nAD47b2Kv4IgqNUgkPg2cp1oANZ4IQmU3exgbrKYrSqejq6_b6l6OJMKXt3G4m1NwS_iQ_S_Dors6ZjWSJ0eGzuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
متئو مورتو (معتبر):
⚪️
انزو فرناندز دیوانه ایده انتقال به رئال مادرید است اما رئال مادرید هنوز در حال فکر کردن و بررسی گزینه‌های خود است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/94477" target="_blank">📅 20:18 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94475">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aRBn2Of52Xy_bWmXUYaQ11nUtZ6kzhDCS9UnRYQrZ_EsUkpfAqC9ZqsawMmmUe1aYFF_4Cd6rvnujU2vXFN7dGLyAPVLli3ym1p-lwamr6qlCk_cEoyoL0zfA08A6XFCAtqUvh3jR3XL_VGUzkDTdKPuwANnqLRfMN7xVJqGNuCESI22UvMXs6dy8wUeKnFVLFXKj5L9EqFK-pLh_99LZYftz7zW826I16y5ocgrnfxABgad7AvnFE0uoSMsmw44nMHiPgNtO8QwTsC0lYctxwlaeWFpZTXfZ2Tkr3TZktlxJXwaOse_yhafOpx1smUg61EQcbY4MPBq3EZoYe2M8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IW3f6Vr5HNIWJ6YiDWwpsBqrM9Ja3fpZv-g8wP042RoWMW5mqqPNRsK_ZLT97rqNcZKhd2k6rECOLaulwXZsOChCYUWkP9QEKvv7XwGl_iJnebtfjWLGyLDlNEK6OI1lg85t4_CvTWyLf3aLMHfj03J-p6SYZ1_bRXWta1Lr_8rWfTMiLYjfA2v5aLDqfS1Bu4HpypuxUhsLd-dbXq-m2Mar0pKtRvEgCjIecS2AehqXD39ZrNb6SoQ8Tsu75qp4DGqr8YuXPxa7lypAOXMt2fl9KTnLg5iXqJvVAFh2vYtmNejDxsqTdHNsWcqxn1L9CGPcZl7RQ6UYXEpkAHASxw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇺🇸
🇦🇺
ورزشگاه محل بازی آمریکا و استرالیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/94475" target="_blank">📅 20:12 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94474">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v7V2J6bkg2-SjQhe2pZyOn2Xoe51BkUfxX4bZoH9rq12mm4Tp2qI2l2Go7eS-W4RAHKknX0mVyfj9qYiBqA-ey-6syerDJ-EZ4af9LQjxQ-5H4_xKb51S5dQrNBACILW8RN1HEbaWcPVaY7PHwnCG4aygMfGRKJYmnSRYxPcSGtiSdj_4qtF7whBngaaLyxIYfmmhmRzGc_UHLdgYcodm-T8t1mNOXqUHONZsA6VQOJEelT3hDPMf1RMd7YSzXR-9crgCLD7ZjxLNtAheypSudYDnmtZ5_GQ3XyQGR-ya4qT1_-XIrcjz3ZjIsSfEeC3aySiJRRnH7lSC7OSwgm-Aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
دکلان رایس برای دومین بار متوالی بهترین بازیکن فصل آرسنال برای فصل 2025/2026 شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/Futball180TV/94474" target="_blank">📅 20:02 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94473">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea022c974b.mp4?token=JNHwu6G9aCxmHHxJlCu2iU4jNBGlBkvl0Rmou5b8apLuVy46qXqMJY7koJ0Xs1BX6D7z-I_2UdUBq6r1IyxfJKYiRf-NdDoG3OCUA9JeStsQFdUbGkQaKRPc7MzYi71geazSUG78jMNH_3k2Wc-LfZLiSjMB9rCK2PZzbhzAjJ6v6Qwtr50oMkb9OFABwVz2Yjw1JpsFmZ6FtR9SA8n6yA5FK2DqKvF3Y_mZZozsYyoCaJgMhY5pUsW_1iMdZ9AShzvEW69ZeoBPkIndXvtIeFvsbIufGYJJlMuJJHPk1dG0SlnyOyrcgMPakB1DHcu3OMXG92GMnglEQG0E3soG6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea022c974b.mp4?token=JNHwu6G9aCxmHHxJlCu2iU4jNBGlBkvl0Rmou5b8apLuVy46qXqMJY7koJ0Xs1BX6D7z-I_2UdUBq6r1IyxfJKYiRf-NdDoG3OCUA9JeStsQFdUbGkQaKRPc7MzYi71geazSUG78jMNH_3k2Wc-LfZLiSjMB9rCK2PZzbhzAjJ6v6Qwtr50oMkb9OFABwVz2Yjw1JpsFmZ6FtR9SA8n6yA5FK2DqKvF3Y_mZZozsYyoCaJgMhY5pUsW_1iMdZ9AShzvEW69ZeoBPkIndXvtIeFvsbIufGYJJlMuJJHPk1dG0SlnyOyrcgMPakB1DHcu3OMXG92GMnglEQG0E3soG6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
هوادارای مسی تو بنگلادش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/94473" target="_blank">📅 19:58 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94472">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/Futball180TV/94472" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/94472" target="_blank">📅 19:58 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94471">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🏆
جام جهانی ۲۰۲۶ فقط یک تورنمنت نیست؛
جاییه که رویاها ساخته می‌شن، ستاره‌ها متولد می‌شن و تاریخ دوباره نوشته می‌شه…
🌍
⚽️
از نبرد غول‌های فوتبال تا شگفتی تیم‌های کوچک،
دنیا دوباره برای بزرگ‌ترین جشن فوتبال آماده می‌شه
🔥
┅━━━━━━━━━━━━┅
🟦
آدرس وان‌ایکس‌بت:
🌐
bitly.uk/connect1xbet
🌐
bitly.uk/connect1xbet
🔓
برای ورود به سایت از فیلترشکن کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
فایل نصب اندروید 1XBET
⬇️</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/94471" target="_blank">📅 19:58 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94470">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pHX7aPTWhj7geL42SkyNTVUtQIw7sOlTyhLRFdTe_1843d3kD9pHstf6P6u9uxB0O60ln-D2Kmf0qdFa8IUsdHJ2RI3awL05GAK8QPnUuBdkGPyC0kxk6uSfudO8j-CKNwc86tUabRixjuuxF-DyiFS2KqeaBB35MzkYsfnS3gWPjS1aSCnVS5-NAn2Whiou5Px1MpQagQvuFi3iNdreUK6BsvIfh7X5QMSzl1gqztzItkvyzItPSvBGtvOdlYJ3XpbARRoejk7cfXM-uqOFe5-csiY7ZXH7zQkTWHubilzduWxdBrOiAnyoWaQKCyxHGvin2YSLViE1e5ZrfaJoFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇪🇸
#فوووووری
؛ روزنامه SER: قرارداد کریستنسن با باشگاه بارسلونا به مدت یک فصل دیگر تمدید شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/Futball180TV/94470" target="_blank">📅 19:45 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94469">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eVTxGMuqmmBZlhlPCQJ2Ar2aEt7pwUfRJ-Axp9IERHCa2nMzXWDf5_t-poWwgXcyH8T2BKUxuNADnOoPZk1UlkoLZ0JoGOc9DyPe_W0Gvnm302lnkJWauWf4Q2mAl7IKH95qOLRszjeM-gep06i3PK497jldcP5YyjizqpkmNFlVeTdoR3zfmBdCmPmXubeA72E2Zn0fllDBIvrR9G6RiENJ6exe0_h7EQzOrb8cmcAk7pwvIWVhvEh2bzGc-RgeZnW26eeNfPskMbFoQqOlAa5sJ0gKu0UApJCZaQhLPqgrZqdKL1dCRwEeiJHkO9XH-9eI_OaF-SO43QlcIM96fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
اکیپ:
بزودی دادگاه اشرف حکیمی به جرم تجاوز قراره تشکیل بشه و وضعیت نهایی اشرف بعد از دادگاه مشخص میشه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/Futball180TV/94469" target="_blank">📅 19:34 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94468">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12f9169375.mp4?token=O-dr-lDu5JzoNE0bo1upXzG5xk3bXGfG9ez4CbXqKRBA32Oua6mGQ70PGk32HLXB26E_p8blx1W0lcdIvTkEnqGixd3Fs0BvULsYlnJtYeIdsldbYe2zb3FR9YAWheeaP4AbIltZOTssR7uzCZlfvaXu6N53KJ21QU7c5FWL4J1mJIWw15OrsuzqhQxdb8Kyq_RZzcrJ0bUxBRn2AF6teKpsEreG3mTUb4CFsA7U8so95vDOzBEd5Eh0VjQFIOiRccgznzkI51z2-jzD-MRAmexcqb2CGRFhI2KLjEDZOMZ8k3jvA-TfowIbxlXtimopLWMqRCUaUfO6GSH65914gA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12f9169375.mp4?token=O-dr-lDu5JzoNE0bo1upXzG5xk3bXGfG9ez4CbXqKRBA32Oua6mGQ70PGk32HLXB26E_p8blx1W0lcdIvTkEnqGixd3Fs0BvULsYlnJtYeIdsldbYe2zb3FR9YAWheeaP4AbIltZOTssR7uzCZlfvaXu6N53KJ21QU7c5FWL4J1mJIWw15OrsuzqhQxdb8Kyq_RZzcrJ0bUxBRn2AF6teKpsEreG3mTUb4CFsA7U8so95vDOzBEd5Eh0VjQFIOiRccgznzkI51z2-jzD-MRAmexcqb2CGRFhI2KLjEDZOMZ8k3jvA-TfowIbxlXtimopLWMqRCUaUfO6GSH65914gA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
⭐
صحبت‌های الهام‌بخش مارک کارنی نخست‌وزیر کانادا، در رختکن این تیم پس از پیروزی قاطع 6 بر 0 در برابر قطر و در سایه مصدومیت شدید اسماعیل‌کونه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/Futball180TV/94468" target="_blank">📅 19:23 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94467">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/49d44fd743.mp4?token=j7xdUQTPY6v92lXTxTSfD9phig_ozTzS1izY9DnTgmDQACxZkgm_-oNt8_qmwylutVh56009lb6mVndih5STPBwaF9smOULZH6ty_w7nyVwj9vCV5LAkpImlG8xb0zXnZZo9157RskTiwfQra1_x6BvTOFf0_jaE7Gf_o-gDeL6l-IZxO_lqITcqz4t_glE3ZLM94kn5eMn9wJqfVjL-T2B7RguD0kJ127_Dv63IJ2gpSqmOhnJegmiz3NBfhCqkqt-QcXi9f90Wp9MHmQnQISbKtbR2X66vP5QCgAlqZK9rzN_uAl1ZGWGHnfqFd9E4DKOEoskQHX0rHTWOrIrhHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/49d44fd743.mp4?token=j7xdUQTPY6v92lXTxTSfD9phig_ozTzS1izY9DnTgmDQACxZkgm_-oNt8_qmwylutVh56009lb6mVndih5STPBwaF9smOULZH6ty_w7nyVwj9vCV5LAkpImlG8xb0zXnZZo9157RskTiwfQra1_x6BvTOFf0_jaE7Gf_o-gDeL6l-IZxO_lqITcqz4t_glE3ZLM94kn5eMn9wJqfVjL-T2B7RguD0kJ127_Dv63IJ2gpSqmOhnJegmiz3NBfhCqkqt-QcXi9f90Wp9MHmQnQISbKtbR2X66vP5QCgAlqZK9rzN_uAl1ZGWGHnfqFd9E4DKOEoskQHX0rHTWOrIrhHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
آرژانتین امسال از شانس های اصلیه
😍
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/Futball180TV/94467" target="_blank">📅 19:07 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94466">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jr6jncnXQSrVJDSMlTQkgbrk2L-7vG2vr31ZWogcOlA3-Lt7Idq_jErMG4dk20uJ1FljSnHSOYxPQtA-dMNaBTGpRKCTWDvy0dXMxYTHxNLthiaxAgN3dxXRzgc_J9AhIA8XhSpXZLLIBxGmhdv1EbWfQoeE21xu0brxluWK8N23NTl22bOcEWTuGiN57uJgGBqsZ1hmIGrut5-kIS1opnM57mM-PNKp1PTrAiv3kPjm6zwIUtaUWxnNUB_K1Y45SP_0p1-rrzy6mreJWO5ClhjcOUGzAQyDx8exQWFaDbOMnAUkAIgghgiDiRHPK2dIkuSk2lyCnHIoIr0kvRnCtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
پاسخ تباس به شکایت بارسلونا علیه پرز:
"این اظهارات غیرقابل قبول است زیرا بر اساس شواهد اثبات شده نیست."
"لالیگا قبلاً چندین بار مخالفت خود را با رفتارهای رئال مادرید و عملکردهای معمول آن از طریق رسانه‌های رسمی خود، از جمله کانال تلویزیونی‌اش، اعلام کرده است."
"لالیگا به احترام روندهای قضایی ادامه خواهد داد تا حقایق روشن شود، اما بدون تردید در دستگاه داوری."
"لالیگا علیه هر نهادی که بخواهد به اعتبار مسابقه آسیب برساند، اقدام خواهد کرد."
﻿
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/Futball180TV/94466" target="_blank">📅 19:05 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94465">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QnI2eLZN3pCmHNi6JE-ILce9h7XzReG2UkBJBxko8Hm8IpnGhRr_r9GU8qU0881kCsjrPSzGGLJhIlkGog3DulXOitj_1Y8afoFAPoB3OjHURVf3oOuCTvQTlNRWdkGSlRkkiZrBNF-Xq8U0cdM0YZAYDp53QbtOj-ys8FaC2_UL47X71YX_QHqibr_NVx5SWPPHJWqpgldGD9lENylLP-e-np5bkTzUW7HCmDmwEG9tGI8k3UhL9cWMlGwhAKko2e5eJMLYL_SWrlHP5jCmo7QJEu6Ro6cAruDRXtjt4hUSSFHzf5_vOjGGw14g9-d0OM4Q0719u8BGa6aOOGvUnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
از شور فوتبال تا شوق زیارت
با فرارسیدن ماه محرم، حال‌وهوای معنوی این روزها برای بسیاری از مردم با آرزوی زیارت کربلا گره می‌خورد. در همین حال، کمپین پیش‌بینی جام جهانی در اپلیکیشن «
همراه من
» فرصتی فراهم کرده تا این شوق، به سفر عتبات عالیات تبدیل شود.
🎁
بر اساس اعلام این کمپین، در هر مسابقه تیم ملی ایران ۳ نفر به قید قرعه برنده کمک‌هزینه سفر به عتبات عالیات خواهند شد؛ جایزه‌ای متفاوت که در کنار هیجان پیش‌بینی مسابقات در نظر گرفته شده است.
فرصت همچنان باقی است؛ تیم ملی ایران در دور مقدماتی همچنان دو دیدار دیگر برابر بلژیک در ۳۱ خرداد و مصر در ۶ تیر پیش‌رو دارد. در صورت صعود به مراحل بعدی نیز این جایزه ویژه برای هر مسابقه تیم ملی کشورمان ادامه خواهد داشت.
💫
به این ترتیب، حداقل ۶ فرصت برای برنده شدن این سفر وجود دارد؛ فرصتی که شاید برای برخی کاربران، از یک
پیش‌بینی ساده و دقیق
آغاز شود و به مسیر کربلا ختم شود.</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/94465" target="_blank">📅 19:05 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94464">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8bd2371280.mp4?token=JtsoYxlzLJ_hUnEHnJHc6TbVM-adt9CJJbKA0wDZnBAMtS0j5mVD-tdyVnGGVwCEOVF-iYfrHzsRMH-L5HqjX-3fuBIGlF3MFiuUFJ6UadXx8TdVh2-Ky3K5tBaThMjeee-XXCboMNgZLIDRrEIfgQlqg-_HJboHfrJYz6XbcvBJ4qHSQfYm0j0lqeAAQXmvaqbJlpRlh7npq20-4klObNkMmNrI7V56g8mpYwfz6Eq1XDbnxHB2AOEpQNmroYYnmx5u7XACnd9waQTEJEwYoxtp2fJidF_g9g8A6tW9B3X-6fsVFn_Cm-STEkuUaW2tsu06aJdasHnsabuUrZn43Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8bd2371280.mp4?token=JtsoYxlzLJ_hUnEHnJHc6TbVM-adt9CJJbKA0wDZnBAMtS0j5mVD-tdyVnGGVwCEOVF-iYfrHzsRMH-L5HqjX-3fuBIGlF3MFiuUFJ6UadXx8TdVh2-Ky3K5tBaThMjeee-XXCboMNgZLIDRrEIfgQlqg-_HJboHfrJYz6XbcvBJ4qHSQfYm0j0lqeAAQXmvaqbJlpRlh7npq20-4klObNkMmNrI7V56g8mpYwfz6Eq1XDbnxHB2AOEpQNmroYYnmx5u7XACnd9waQTEJEwYoxtp2fJidF_g9g8A6tW9B3X-6fsVFn_Cm-STEkuUaW2tsu06aJdasHnsabuUrZn43Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جوری‌که جام‌جهانی داره پیش میره:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/94464" target="_blank">📅 19:04 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94463">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uTxBlJ80nCjbFig9PRvLMOHucyZOXmcCtSleYKDYzgXRqU7hWcKWY7C3MMzuRGXeD7swXg8PUpWX9p295iwx7E0f0mBoZZVlwNTlZ_bp2cB7DMLZ4N-AFNbN4EJsq3FgADkecKh7sJx2WHS3EQLDAdHaKSTv60uaaxNraFr2PKaURaZNfqK-nAN1kcPLLU7nDHofkJ8BZ46eiL4im-r9FUk6n97VjCm8zObvWNamLbM3hIMmFplvYuYzeECaC2zv7aV6LYEJc9Md0ojEjddMEUQtHxq2lFXk2lRBQiWBeBi16F61mcUip5TEV9LK5-OzF_UQHg7p68ss9mUbVqMR1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
🗣️
دیس ماتزاری به زلاتان:
🔻
ابراهیموویچ به دلیل عملکرد ریدمانش تو میلان بزرگ‌ترین طرفدار اینتر در تاریخه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/Futball180TV/94463" target="_blank">📅 18:48 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94462">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m8dggc1NTeQHFUuVjcVRhiIo7eaDFNUu3PIKtyoMDKlCsL595evVCv3yRFAyHgHpc6L0p5KYBC3Eqrar9UhOxbn38JYq9MhvuYxrydMWtvS0VxtkmjWW5S8vN3QnG-iDrJ49TRrz2nJKoFRshbSjwTfoioPJWdzfMR6fFR1sAjfqpBOhjNBpEM2c4cuMIVZQa3_ImQQ58akiMJKwc9SCAzOEIFTqUeBO2MYdmqBEjo9SHeJXrJEkFkdYI1fi7eC9UuZ8C7j0Xo2L5sbF1hQrk_X1AyLpmqOZG6peMamJXdmB-u3OQAf8dHEDAXkJFlhRgS9v46BY2zu9ughafvuVeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
رومانو:
رئال بتیس برای گارسیا به رئال مادرید پیشنهاد خود را ارسال کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/Futball180TV/94462" target="_blank">📅 18:24 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94461">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MxfJ-i11sNYJqSFP0kOYii-rtB0ak2B1Q-iBEVlI--XDT5HtKMavWgsZG48tQdLW_0b_dRPc35DWot6BXg_RWtXEWPpJv6Muvg_IOF1EDP13wUljm_o2gbOgBp_3KJDidi3fs3BdLM-rhMst-yZZdgKFZE_5HRLb6YlV7fjAFoS_EScFoNCfPgX0yc5pbgwb1WqOjxW9FAKCZRk8fSBbFvMJ_lG49xaUeN5K5EuwZDwHu3SvhJ8BbXooQAB5W3w02seKG8dIUF-UC8_V9EnxKRRTHPZhXHUpeRJaqeIUUlefYDM2ngZma8fNO430HsM0svM75cwn4PRnNMBuIlJlsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚪️
فووووری آاس:
مورینیو به جذب الساندرو باستونی علاقه‌منده اما اینتر برای فروش مدافع ایتالیایی خودش حدود ۷۰ میلیون یورو قیمت گذاشته و کمتر از این عدد وارد مذاکره نمیشه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/Futball180TV/94461" target="_blank">📅 18:10 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94460">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BHq9D3Pp9n15cXdxgiBIE_Tb-RURkRzEvrXJaX_Ifiq-UwvV4OBHJ61G7EDTI1ndjUhyNBy2tGuFcvdunRfbaxSE8_vYdIaFaDeZm2UIZicrYPLDFOh0KG-gE1FbJomanKpOHAbAutum8jE7eM3brUNoCH48Jp17Uj_0kIorvXwq1Cxgp2fzau_Vbq9FObXUX_yxPua5HFpQMFSxUHiavCXtWnWSnTZL8TrS_VR3qGs61xhgRMaybvpRbr8_hiLRDE9mdCJaCZ8QsP3CAeIdA2cYvuus-PJU_oXJ-8r6r4V5Qf3qERJT4aHFimI6owoqIiyjt0cassSxGJee5dYwwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
پیشبینی‌ هوش مصنوعی از مرحله حذفی جام جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/Futball180TV/94460" target="_blank">📅 18:07 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94459">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/126dd65d76.mp4?token=JTCYX6UsIqSo2imi7VtBIzA3DOH86AaGFJZcvKqIaTb-6OwG4uKpRhx00ujYdERLxhP3Xk5Byzz5cspvfeqgiyZ93oekZlzF7fZfMXLal56NIw3hJ214lQtpjfx_CWWOd2Qb_8v9Fl2DuLfj9Fh5JHD2yJiZqJ467aED70APIEvE-UBXplxQ-k0m_rRum5NPjNuJ9dSL3nUvWILxzyzQs_LU19CxRP0wKGrg02IgavFTAFl8fYem8AqGTlyWgEerPH37zwLB5QgEQMAt-D2pnb4DJIYOmW_TdcfOH8-kAZj3zMXKSLaJJdej60cJI-UvGTRSJBLUPx6AHxr5tsk1nKSIbTUAjfp84UPR1K_iUV1ziLtuw4s-5CijBXJ0dtgH8RJVYjZybGZODoaWqgUnR3C2azH6GYqVkPMq_MN8GJ04anYyauMdNAvH-qS0FqV8bN_tN3HPSAuZKAARVaogOjUFJSOlFJYHrf2Th3QEaauIJ7JbFh4CGLNhCNdj-XFpbh5iLWdrvBlCEOlFwsyGL5HbCi2cbYTdv8AEh_vtXhyIVxB1o5f_ToZAJZY8AMTy7Qz757DBpmODwrcPYFJ3dlPGJo2-0z9WDCywuBaunBexKxYWmSCO8soJ2X2R1FeMzeQ-Ef7I9uFurOx2ZsfC4qp5im58im8m-K58NtcXdzM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/126dd65d76.mp4?token=JTCYX6UsIqSo2imi7VtBIzA3DOH86AaGFJZcvKqIaTb-6OwG4uKpRhx00ujYdERLxhP3Xk5Byzz5cspvfeqgiyZ93oekZlzF7fZfMXLal56NIw3hJ214lQtpjfx_CWWOd2Qb_8v9Fl2DuLfj9Fh5JHD2yJiZqJ467aED70APIEvE-UBXplxQ-k0m_rRum5NPjNuJ9dSL3nUvWILxzyzQs_LU19CxRP0wKGrg02IgavFTAFl8fYem8AqGTlyWgEerPH37zwLB5QgEQMAt-D2pnb4DJIYOmW_TdcfOH8-kAZj3zMXKSLaJJdej60cJI-UvGTRSJBLUPx6AHxr5tsk1nKSIbTUAjfp84UPR1K_iUV1ziLtuw4s-5CijBXJ0dtgH8RJVYjZybGZODoaWqgUnR3C2azH6GYqVkPMq_MN8GJ04anYyauMdNAvH-qS0FqV8bN_tN3HPSAuZKAARVaogOjUFJSOlFJYHrf2Th3QEaauIJ7JbFh4CGLNhCNdj-XFpbh5iLWdrvBlCEOlFwsyGL5HbCi2cbYTdv8AEh_vtXhyIVxB1o5f_ToZAJZY8AMTy7Qz757DBpmODwrcPYFJ3dlPGJo2-0z9WDCywuBaunBexKxYWmSCO8soJ2X2R1FeMzeQ-Ef7I9uFurOx2ZsfC4qp5im58im8m-K58NtcXdzM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
🏆
صداشو کم‌کنیددددد. ویدیو جنجالی وایرال شده در خارج که قبل بازی ایران رو نشون میده و ایرانیا همو فوش‌کش میکنن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/Futball180TV/94459" target="_blank">📅 18:02 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94458">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VHhObrxJxVqzhG0pjds9nt6MJuUbEgGxesdjpxjxbbWhFbJrNk9uzBONILES1Zm5suMJcpWCMXJFY5k4O-WUWuOHJDwz1poGjtBB8KOvidrXMwkRdvT-f5saxAA-LNz7KbCsF2C6llgTIO4yBENyqOmJriH7rKWKo2W-VwTbCJp3S12JS07XOQ_5vCOpPCKrOXsibdkgXATpWiniS-VnBxH63IfOqOgrRFJiQaaKF48X4Ib85myGZBb1j9q15V6w-hycQtHvNOcAYGo2j5fmtfbOgBucSk4sbofAmp3ZaR3TAFaOK3KoGn6s6f6nQxhFqBA6QlZ5PYJAq4UfYGyRaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نظرت در مورد هتریک مسی ؟
یامال : مسی هر بازی بیشتر ثابت میکنه که اون بهترین بازیکن تاریخه دیگه حرفی برای گفتن نمیمونه، نیمار الگوی منه، ولی مسی بهترینه تمام دورانه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/Futball180TV/94458" target="_blank">📅 17:59 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94457">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a748cd76e.mp4?token=XOTwxFy_Y6-oeMiHsylfqDN0xLy4HdigfaEbgmZcRxyEfO6ZL8Lm3PPbE-Y9q67ge0BqoSJrl2ySCZpIqOdsRLVTjXR2GKFat1iUDqGzCInqjgZrp6WykTCBxJ4-rBVtcHNC1y2geDKGEmU4YCoX2hy1SZZLi-72vmXI9cFgAlmeYnP5ZTvQZStnKHvkzVyaYWKCBZLxtU5MbgBAG72wrsdfJGf0v-ArcQupWqBuBlGqzrQFIS9azHBCUBxAfIUBCkLjDyJT_wCVIalypvRHfN0K8WEt1WmJuDm46kZdh9wvu5v1X61GC85o-Joe39WVzZHybR5rlOeEbzZDnQM85A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a748cd76e.mp4?token=XOTwxFy_Y6-oeMiHsylfqDN0xLy4HdigfaEbgmZcRxyEfO6ZL8Lm3PPbE-Y9q67ge0BqoSJrl2ySCZpIqOdsRLVTjXR2GKFat1iUDqGzCInqjgZrp6WykTCBxJ4-rBVtcHNC1y2geDKGEmU4YCoX2hy1SZZLi-72vmXI9cFgAlmeYnP5ZTvQZStnKHvkzVyaYWKCBZLxtU5MbgBAG72wrsdfJGf0v-ArcQupWqBuBlGqzrQFIS9azHBCUBxAfIUBCkLjDyJT_wCVIalypvRHfN0K8WEt1WmJuDm46kZdh9wvu5v1X61GC85o-Joe39WVzZHybR5rlOeEbzZDnQM85A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رامین رضائیان: خوشحالی من وقتی است که مردم ایران خوشحال شوند/همه تلاش خود را می‌کنیم که در جام‌جهانی اتفاقی را رقم بزنیم که دل مردم ایران شاد شود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/94457" target="_blank">📅 17:59 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94456">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/001a9bf699.mp4?token=FV_p3hlx8i72mMqxTKq28-BVzmNbEpc-5d_h2wQJAnGBKQRfDzZMCOskbfgiYmVfzOLOuZ6Sofy_kjvC25xSzKQoU_X9Qgop6k4YIkDe-tm39i5hfoq4yFAFtmBMNk4oWbeYZehrx02nTshBlM5zcR0MsxB4TgBzqFmZAsfJ-aVMJSYIAUY3IXpgpM9pczAbDe1b4qDxjAxFVkPV1XhYWsCgUdQ1mKsflMI9DbgNmY86Jnjx0qu1zxlkmcgcsJbxc0SEMs6QuGG0tw1hY55T3OhDIJC6nbRbmkOC7_gKuqHqGLR402BzFY5qWdGVUBzGgM6ZieUhsHe07MELSzlrpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/001a9bf699.mp4?token=FV_p3hlx8i72mMqxTKq28-BVzmNbEpc-5d_h2wQJAnGBKQRfDzZMCOskbfgiYmVfzOLOuZ6Sofy_kjvC25xSzKQoU_X9Qgop6k4YIkDe-tm39i5hfoq4yFAFtmBMNk4oWbeYZehrx02nTshBlM5zcR0MsxB4TgBzqFmZAsfJ-aVMJSYIAUY3IXpgpM9pczAbDe1b4qDxjAxFVkPV1XhYWsCgUdQ1mKsflMI9DbgNmY86Jnjx0qu1zxlkmcgcsJbxc0SEMs6QuGG0tw1hY55T3OhDIJC6nbRbmkOC7_gKuqHqGLR402BzFY5qWdGVUBzGgM6ZieUhsHe07MELSzlrpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
🇨🇴
🏆
هواداران دوس‌داشتنی کلمبیا کف آمریکا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/94456" target="_blank">📅 17:40 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94455">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LuF89wA1046k38-CY6dtwjyUXjEeuf1fEAE-nk7mn_T3vF83rgU8R9DL08EWcZ6f-bjd6UQvQ-W9kpkhcoFmWgSFrBJDm1xMejVSbuyFzQAvxcW5MUiqkQ04ZcahlPGygTLKAWxFClvLZBCSN3v8OB4VJ-8MqdTfhp0cUD9_dabcC3uHVTJTezxOhvi_3W1xPPadbOko5tGUNu2_peqBVgSUsH1iWioQotfNqT6DDchOnjZHZFpJI9-Y9X3529nTdTplmL_VRqglAw3Z33S9HL_kiolgnMzFlOmCoTD8NKQYoRkIq8W4rMQDyN9hO5yvQLUl7c4WSlleRe5uU7oYvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🚨
دیوید اورنشتین:
منچسترسیتی به‌دنبال یک خرید بزرگ در خط هافبکه و میخواد همزمان برای جذب ساندرو تونالی و الیوت اندرسون اقدام کنه.
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/94455" target="_blank">📅 17:38 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94454">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bb9tsiGgNMg5G6F9zDplrYzZd6n_jLPNLXH2dJ7_xI9Hg9mCWQ9L30coI3-MbMExFw9ekdvLYsNieCeDanyjUnSMKyv4cJWRw2bPLpn1Wfl9vlbM9he0fSbGCcNQlQQf5Xt0d8NmwtQmyQkBI9aftJO8Dt59I3yO7YO_nzoRovZisSp4EPlNT0PyjF9lCqzy6VuU5eg9eAb-wbxLMnmx-Z7KyAF9N_PIi_AmFe9nm9O_i9AwDc0DNhxAjheBrAoHeWROJFaEOUk4iYP0BmMDZ74HK3awHlTnhYgWpIGMVkMMP0NjF5lfzga5Z4Ev-BRS2l73gdyzqLWJHcK4wOEuLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
رومانو:
اتلتیکو مادرید با الخاندرو گریمالدو به توافق شخصی رسیده است و انتظار می‌رود این قرارداد به زودی تکمیل شود.
🔹
ارزش این قرارداد 12 میلیون یورو است.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/94454" target="_blank">📅 17:38 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94453">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/ijJG-TF9TuffLYGGSypPNNHOrN0KAo5dElQ7lBjlhFzNDbPlcEW1YsQOVlaQBXKFRdw46Bbpny09qNGU2znfrIF6C71HAQMYagi0HH72O4cQuPu8bsC5IJZVUB78kHqLY70uDOiyNye-Hq5wtzfa9zN1rLA36Kr5RTcDyCSKed1mZD9_4tL89nkYx9hVBSlSD5vQYx9nii81Wmo4Zjzuim6iy6LjIPqgRR4K5i_ko_wpv9BI-Kxh7uVfE4eFfJroJ-jWPDfvhVCBUMsSUzFnFy7ZJw5700YXf9o6ryUI9nxVr71ViAjXwmvjFuZ_sO54YBhw9i_HbmxXCu90xFEzXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
تا ۷۰٪ تخفیف ویژه آخر هفته روی کالاهای منتخب
💳
خرید در ۴ قسط و بدون کارمزد با اسنپ‌پی
✨
مشاهده محصولات و خرید با تخفیف ویژه
🔗
https://jwir.ir/ir1</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/94453" target="_blank">📅 17:38 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94452">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c628dc86c.mp4?token=MVVrAbWPYNHULsWXB7QJOkd_kIbB_vLv5F4mW2Pk9kvHVl1APNKAeljfP0hxibTpRsJj-MqeCrzsrm4wyb5UEdCeCrR3IUbqZbRCbBbtOYEoP2e54Bl3DX3zE1zzOsNtyR_uj_ohhvs1VuGHjle0b58H8PAeRpkwSClPWSnCYvokf-iJV96bokhsiprUXl-iGNWNlq9P6zEwGGShIkTJjAnhAA9BdDYZWDZCvSo9qJjm4oXSao7OJn1mWt5q4OiTcunVHvySoTk_zACfdW2DRyLamaCj4MFvuyIp1CXyEnsiMa5TvZPMIK6QGq1uW20NZDDuSYdn2ZIOkfrqUu4SDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c628dc86c.mp4?token=MVVrAbWPYNHULsWXB7QJOkd_kIbB_vLv5F4mW2Pk9kvHVl1APNKAeljfP0hxibTpRsJj-MqeCrzsrm4wyb5UEdCeCrR3IUbqZbRCbBbtOYEoP2e54Bl3DX3zE1zzOsNtyR_uj_ohhvs1VuGHjle0b58H8PAeRpkwSClPWSnCYvokf-iJV96bokhsiprUXl-iGNWNlq9P6zEwGGShIkTJjAnhAA9BdDYZWDZCvSo9qJjm4oXSao7OJn1mWt5q4OiTcunVHvySoTk_zACfdW2DRyLamaCj4MFvuyIp1CXyEnsiMa5TvZPMIK6QGq1uW20NZDDuSYdn2ZIOkfrqUu4SDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤡
🏆
این ویدیو خود خودشه :)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/Futball180TV/94452" target="_blank">📅 17:20 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94451">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yl_j9jQRjYPf5QnUd3TuaAjtCj5Yv8iP2biB5Rdmk6Cu8hknSCoMtgkQf0JTpZUsM5VaKyd3KkTlLgWUQBK7_O8oXnNPbt79Zt1IlogOUtnnb7Lc2nl8zztdn9wvpMB9rWpOaiAXKN2vo3mGdArcb0lWoHDwLm533PSoKnoO8fHMV6SlhpXgyp6pAH0cPHQyaVotntbQUdzHu0Sv3Df5llb-aZfBngrdVlFgH-T-IA7HsSMChWnKUZTVn7bYCikqsyjeTDbE9TvwXdNX0UiNLa288VjPccA8TrFwtb7to14FiJaaG0v6vGtz74AtokAc3txYqUtlk_L2NT2xwo83dA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
تعداد کارت های قرمز تو جام جهانی‌ های اخیر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/94451" target="_blank">📅 17:20 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94450">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jQfu8rb0LkPPVK8KxBjPa0-MlAEiPfa5_1wF6i5niX4tD1TUw5FnVixVbD_1Ly6e4WvbIYFDgWu--d5HepgbPiFUcskB3CZTU6B4EJ0MWxDRTw5xgH1QUo81MzG1JqGV6xjNAPoiO2JeOp3etwRrEeKbR-lWFvf4xLqpoRN2JZzYecssmBzsQ1mpjCcaLzGmX3CxYNowP9lg2Kjg9vU7DtNHSbe3IRSgJ0mqWJDoTT9OS-0K8cCDX6CKFdB6KXD8s47Q9NuakNzZ_QCMF2jnAeUN_bduB1OTFXKOdxdRwXNeiq3_1datEZBoXNzVpnR6au6ufE6KIG0xkxdGlTi8uA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دلافوئنته :
رودری بهترین بازیکن دنیاس، وقتی ازش انتقاد میکنن عصبی میشم، چون اون از تمام هافبک های اروپا بهتره اون حتی اگه 50% آمادگی جسمانی هم داشته باشه بازم جزو بهتریناس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/94450" target="_blank">📅 17:17 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94449">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4d969ad7b3.mp4?token=SJDKfFtB42ASULIdyJ4Xy9NvEuFssx42GZZhR-wFe5wFyIdMX5QJ7J3BeXNVdY2gZlTFALCX8CUkYwUl0s1oZYeU8bnNCs3aQCsVNL9_Zcdq9ovbsAzH_c6fQ9RXm4kfAp5Pkc6fgmhspW6ZszVqSv0kcdvq0VSXk6H3uow7YATBkAT-zXEDNcWh-CiTojWMcyQ_VOa_cTsUgdt4Afu-6OW2uxnMQC_uwFghk7nfI9wkhNmFpOIkjvA5TeafL05fhdPYKUVsYsHqD__diozkLUkF1DRYGh7xVX8M_BBqDSe86fzweyDFWf5sD-qtdlE0pO0cJkltpDiDcOgL3I_QAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4d969ad7b3.mp4?token=SJDKfFtB42ASULIdyJ4Xy9NvEuFssx42GZZhR-wFe5wFyIdMX5QJ7J3BeXNVdY2gZlTFALCX8CUkYwUl0s1oZYeU8bnNCs3aQCsVNL9_Zcdq9ovbsAzH_c6fQ9RXm4kfAp5Pkc6fgmhspW6ZszVqSv0kcdvq0VSXk6H3uow7YATBkAT-zXEDNcWh-CiTojWMcyQ_VOa_cTsUgdt4Afu-6OW2uxnMQC_uwFghk7nfI9wkhNmFpOIkjvA5TeafL05fhdPYKUVsYsHqD__diozkLUkF1DRYGh7xVX8M_BBqDSe86fzweyDFWf5sD-qtdlE0pO0cJkltpDiDcOgL3I_QAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مهمونای جام‌جهانی ابوطالب‌حسینی عالین
😂
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/94449" target="_blank">📅 17:16 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94448">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">Live Tennis</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/94448" target="_blank">📅 17:16 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94447">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PQOJmUN9uWxQpYrYwE0GMvN-EFY6SjSYW07bysfhcOlL77EsOBlhUPdM8-lz5KbAq0HJ0h8PkXSvTvs6dqtRwE1Dwd-ISu2RbWIWTUuJLHEzNU1-KVFk1jCgnnv3chIzAdbsDfq9h-eg7Jw6oX7KYsPZXTpfostnWUYV5YeP1dTSIb257sTiE-chERJnLGWj31vJaMzJy9ufNXOkZoBxeKixGx5tDS35XRCdbNMdhgAFHa453Q4vtvLrDGI1ca18UME2hIJOgj7LoFEXJQshe1vpX6oN0NcuZ5Vi7nh8_ll02kljHbz1iHkHMv1VQtIVa-Vq67GGPbqYYIrlDMSRPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوست دختر ژائو نوس بعد هجوم هوادارای رونالدو به کامنت هاش، کامنت های پیجشو بست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/Futball180TV/94447" target="_blank">📅 17:15 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94446">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c99fa3193a.mp4?token=SyI-iX3ZzHcSsh6hw4vAFKeKdVeNKBx-xUCcfXmzRmAvsS2Wef-N8qoICB8GEeidPuIs_NdJ1fAULrS9jzx9n000GPdAes_hZ_OmZc1QA4v6q6weNRXwnHYcmpf5s2jbpfygpznlbR1jofeBKUru6umYPPybwz859WvAEC38qn8zCQ9_4DF01cgb9PMn_XH2XFqz3Zu6syBf8iC_N7eZaUFG0vukxbUaGkDVivUu__6gGTLE-Hg7r_f1Yk83AfWEFuIA_Gu9Dsuxe_jGiT6JrW0meoE7rKiNLVXiAtkh_AhOKR4HoPZiAywqjKLVx7hiTiZRbWV8okGWn0nEh8lwNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c99fa3193a.mp4?token=SyI-iX3ZzHcSsh6hw4vAFKeKdVeNKBx-xUCcfXmzRmAvsS2Wef-N8qoICB8GEeidPuIs_NdJ1fAULrS9jzx9n000GPdAes_hZ_OmZc1QA4v6q6weNRXwnHYcmpf5s2jbpfygpznlbR1jofeBKUru6umYPPybwz859WvAEC38qn8zCQ9_4DF01cgb9PMn_XH2XFqz3Zu6syBf8iC_N7eZaUFG0vukxbUaGkDVivUu__6gGTLE-Hg7r_f1Yk83AfWEFuIA_Gu9Dsuxe_jGiT6JrW0meoE7rKiNLVXiAtkh_AhOKR4HoPZiAywqjKLVx7hiTiZRbWV8okGWn0nEh8lwNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دختر فوتبالیش خوبه
😍
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/94446" target="_blank">📅 17:14 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94444">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hcYh4b7wlSakAY8jTxGYtX05HKbXSlyZ-P7UwMjB9kdG0zo0nzxKfBhejRg8eE7XAbQ8JXNmZA5r1GQ9AR554-XG4FCUkIoAKpvub4cuHfdK5c8-RH_M52qA-6S5BcvDnbDiqWA2_NfAwDy4366v40kMB_VCnliNpbiMThGPlH8nCkKAXvj0AQUeek0FfAFw8bMDmy04l6TscTJM0eEpVwAI3x5kiJVO3oDKp2B5PWZRq1N5nYgJDTcDQop0i8rKCj-s_oT_-L-lGCl_Jx6kcwdZag1czWp2aFBP2yvNEG6pcTeHJ76OeLjqcNy9egqCSbk4fbtZSJmJuT6fpGTPLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
لوئیس فیگو:
ما جام جهانی را خواهیم برد [پرتغال]، چون بهترین تیم را داریم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/94444" target="_blank">📅 17:12 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94443">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U0dh-bdUHfmkVDoNrsDPx4fIE62GXNbgBl4pV99NJ5DNMFbt1FDKHXjyNTii2_-2w9WHP4wz8yHi_xd89WBmD9oPd3DCxMrXYGjzAxm0RGN4KB55D4gMdE5TznkiEZTanD33AR1Pe89bHZaYDKNsWFR74lSS7qnSqp_P3uAFhd_XkqOMxzNrD9AzPS5r2u09C_217CLGzn3tzM9Lbse3Xn59a-5VKP1s373wzbzaGvwKBm-7TqGnWGp2WPh9UKpDyz-5RWNkhw3tOaMNxIZDUdcLGHSdI-eI8-izYc0j4QCBeANyscFSXUOlFoF_PMZXldijT6p7sDwHE5Pstph5iA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔺
اینفوگرافی خدمات فعال‌شده پس از رفع اختلال فنی</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/94443" target="_blank">📅 17:12 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94442">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a1c32ce413.mp4?token=UOMGhcy0SEOMPaKWrdbIauf3A-o5k_HsRwqtOkU9pyCosBujJFtEfjTMEPsLfdlPWAh85scDlbA3hL1LtwtkT6hFmsxOhKSjjwys8JjDmGXEOyatRyOgcb6cMSXZ77Tw0D-y6a9-mV236k9gHrKh6-1qhcmFEyv97n5_5s5GXZOwub1JvPhe3JAS70dHxqln-9m05Fr1bHZ6Y1n_sUhFYslVfTRwCKsAVpo3Z9vpDXl6wEWwabIybcIhM1Zv1HwN-ULWgNOadw-R7EwCJglwRh4y1KYA9xXXZGAkLavyKXdMx_pz0UjjOWe7rGaoKxEVv4C8gNRw2kLjgVhQ30i4Aw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a1c32ce413.mp4?token=UOMGhcy0SEOMPaKWrdbIauf3A-o5k_HsRwqtOkU9pyCosBujJFtEfjTMEPsLfdlPWAh85scDlbA3hL1LtwtkT6hFmsxOhKSjjwys8JjDmGXEOyatRyOgcb6cMSXZ77Tw0D-y6a9-mV236k9gHrKh6-1qhcmFEyv97n5_5s5GXZOwub1JvPhe3JAS70dHxqln-9m05Fr1bHZ6Y1n_sUhFYslVfTRwCKsAVpo3Z9vpDXl6wEWwabIybcIhM1Zv1HwN-ULWgNOadw-R7EwCJglwRh4y1KYA9xXXZGAkLavyKXdMx_pz0UjjOWe7rGaoKxEVv4C8gNRw2kLjgVhQ30i4Aw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
▶️
خاطره حنیف عمران‌زاده از هتریک ایمون زاید و شکست مقابل پرسپولیس در دربی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/94442" target="_blank">📅 17:02 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94441">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e669850176.mp4?token=PTwMJKKoQKnyyb2-ZtyQhZSi8T5chfgESLfQVGuDz3QkTWkdYRs5GJa2MEEAdsSfSk8YkfvdWRkSStw3iuhrIynq0qbLfC-N7XYVylf6kbH2hf9GUNGA_FvzK2cSUS7UkuC9N751AgHQBYTpgE-LdjzLLTSWMWhHqO6rg9_IaXyoWvNynX7_QB1xmoPwRn14cGL9qxWS-OTUbY028qgKRWk1B7SbWTDxGgmr5CSyeHiUR94rA6lj7IMjlwWMpnzOiZSNQGnuJbVapDieuBcUaw5dzVAOQh7H2Lo3CyyqDnLV0Yv9w9a84hSfANnfUPAdwfQrVIxfg-LO-M6xPm9hEbkCzchNyUSSmc4QDhlZhTXwzqNOqNFk86FdyMKAyEWPrmpqDuTgff-ZMDiIKWpB6pBLQ9NjgTV-aK2u8Zq0GbGrzdXEu--BvdEmM3zlLJDomw7KQ5SLsv_KafJm3WzB3_bTR-OKpjsC-rLQ2JBMcXH3d4q7PuFnWddDQrTVXjAyB_pG5VHb_sYF2I1eTnr35kBdpkYbzEaPCqM76JSzWzuCsg_I8BJldJwtUljaKN9jBG1rATnbVEFMKzDnnGaTgoKBZ7w0yiizGBaf-81fYQTf5cstbrlmBpGH_Il4otLMNK1Ci-ZWVQJ9K7nH758Ttw1LZ1Mq2oLVN5m_EnviVqM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e669850176.mp4?token=PTwMJKKoQKnyyb2-ZtyQhZSi8T5chfgESLfQVGuDz3QkTWkdYRs5GJa2MEEAdsSfSk8YkfvdWRkSStw3iuhrIynq0qbLfC-N7XYVylf6kbH2hf9GUNGA_FvzK2cSUS7UkuC9N751AgHQBYTpgE-LdjzLLTSWMWhHqO6rg9_IaXyoWvNynX7_QB1xmoPwRn14cGL9qxWS-OTUbY028qgKRWk1B7SbWTDxGgmr5CSyeHiUR94rA6lj7IMjlwWMpnzOiZSNQGnuJbVapDieuBcUaw5dzVAOQh7H2Lo3CyyqDnLV0Yv9w9a84hSfANnfUPAdwfQrVIxfg-LO-M6xPm9hEbkCzchNyUSSmc4QDhlZhTXwzqNOqNFk86FdyMKAyEWPrmpqDuTgff-ZMDiIKWpB6pBLQ9NjgTV-aK2u8Zq0GbGrzdXEu--BvdEmM3zlLJDomw7KQ5SLsv_KafJm3WzB3_bTR-OKpjsC-rLQ2JBMcXH3d4q7PuFnWddDQrTVXjAyB_pG5VHb_sYF2I1eTnr35kBdpkYbzEaPCqM76JSzWzuCsg_I8BJldJwtUljaKN9jBG1rATnbVEFMKzDnnGaTgoKBZ7w0yiizGBaf-81fYQTf5cstbrlmBpGH_Il4otLMNK1Ci-ZWVQJ9K7nH758Ttw1LZ1Mq2oLVN5m_EnviVqM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
▶️
پسردکتر حسابی در گفتگو با ابوطالب: منم میتونستم برم دختر بازی ولی ترجیح دادم راه پدرم رو برم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/Futball180TV/94441" target="_blank">📅 16:40 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94440">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AjdEel_-yTQeUKkJv0ffwKhmbYwRWj9JlRNpn3D-8LDd0Mt0KtkbdBrKbPxSn7-JGrWink0p-yoW3nO4V856y1PMxPkTC9KXKKKMSuX4qJDbdrwvms-dqiFvQZhxmAHWhltJd_ow17i2KnFh4b199nMzbySzaJdubgEgb2f7-bzCfN0cbMUHCR-Y6OTHvRxGsYNMMvcxFMiX8K-qF_y05ma0F94W9TlVFuXjbISiiTS7KKY5iNgooSP5uUfnKYrFQGla8TX6zKyllaXm7Zw9RBIzRXV2LUpm32gPBd6Q96tqloJlQsBgZCTTA5PFKrtEeVMKuIAZ7mp0m20MXtKN1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🇪🇸
🎙
گاوی درباره انتقال کوکوریا به رئال مادرید:
خب... رئال مادرید اخیراً تغییرات زیادی در دفاع کناری‌هایش داده است! این نتیجه داشتن لامین یامال در بارسلوناست. یامال بهترین است و حالا آن‌ها کوکوریا را برای متوقف کردن لامین جذب کردند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/Futball180TV/94440" target="_blank">📅 16:36 · 29 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
