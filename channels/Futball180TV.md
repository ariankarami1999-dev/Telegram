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
<img src="https://cdn5.telesco.pe/file/Cma3ZbAAk513kQ8tQvaGzZrD5R_o1snNfZmEamQr3sXUGZ2vLuDMoE8xUp7II6gDfjdlvOp5k5nJkKImFx_vOR8OcEsxKYL1Pe4x123V3KKawuueCwfwLBJ3yicHXLqQLpn7Yv5mZvxL4coOTxBnzX1SBzNVMmKujf7Wcoud4Iqwbbo_Dh0p7CaJUnrMhBMrAuL1_4aAKUVvTExF_YEgjhcbN_n_GAj73bM751lMxTifE6mf0lITj9BjM2gjzpQ8aURY3SS-WY46UNRACeM8OqK9Fgoeqr1HgpI1XPBFji3mZnn1EzcPM0qIhMw6MjXpqDR3SCndDVbsFHSWhOZ2Aw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 جام جهانی 2026 | فوتبال 180</h1>
<p>@Futball180TV • 👥 481K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-23 11:49:06</div>
<hr>

<div class="tg-post" id="msg-92552">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r-CONLyU5hMS5Z10ZYicOCE8rwOCqXSiHoSJMSH3QjyHjfw1Mx5kup1T3F7JFcEq-d5HbiaZSWq93iGbRBqq0Bs0lkeTG9rjXAChGi5wt8IHQbZNtVtFKl8ENQNmHLTY3QBweoQmiyCInE1aaImuWxC2WTUW8xypWtxxohvn-p9l9PSzt-X2sbuzFdWe-ML7xEqNaPB8m0glvZmrpmdtagcmlaeKj-PBPpk6gQmZ6McbVcAetjheHwCsXdwPqDzIslvShMf8uPSZnBxKr7QDdvoG0nldIUFt0OL-Bc7DhHjtx4Yv6X3iWDLD01cpDT5CrX3Ta0SOdghPi89m2_yKBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
📊
مقایسه میزان ویو‌ بازی فینال فوتبال آمریکایی و افتتاحیه جام‌جهانی؛ خلاصه‌که هیچی فوتبال نمیشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.58K · <a href="https://t.me/Futball180TV/92552" target="_blank">📅 11:40 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92551">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nOUo0m4i0eCY9MxoIwIZorPnUJgVjgTZHvYmJWbU3e7Pm71QOWwp5kr-sfLy5L0Tu3acp32XRrqpDMLEXJSCIf8EroUgATT0xdC-Ih7BxGMz0HwMBmCO58vAnOjL9ZWEP6rXsQxGvJVVrDyoAFIaOm26l2vRTf5UDB6l66UcmTfnQqeL84ldwKixmqO67zqZthgn1aUIFWRfrgPwHMqTW04TFKxssmJSVo7qssD7r7qBQ3kEMHoaXDJ6y025hAQr-r_F3RwstIFW5HGwx06B2BwQ50WZeI6DJbmCfCXTLDMVACHISjVIOkypK18QQ2A1yOoJhlCBNQNncY-r2tUCJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
رندی‌اورتون و جان‌سینا در بازی افتتاحیه جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.64K · <a href="https://t.me/Futball180TV/92551" target="_blank">📅 11:20 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92550">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/06db464749.mp4?token=hwJZGJaVcg2sB-VBzRdh1v05Cg9iW1cxiuCGLEMHeEr32taVA8Q1ZGL_kRHLixeV9QD2FlakTidLqOu8xlkEmy1uvM814JP91p17SDfFq_Vs-YE4UTBECuy-0gbhyPeAZXJjAraK0k9WaSJaFSGBpcI4lj1iKTzPfMvSgxyDxL7JWFuuquwi7WrnXlgnykb7KUMHm4L9-Ip2_r_kH2PKg9-TYbSvNMkZ2kRLabmwsO9Rf3wKHZzjaz8-ywYLoLpHB1O7hEl1rZ_IqVa4gXezTCr3jPqEv9RWEKXrabx0I9hUpN1-RnCRANJgHg4f2St8p--D2HsRJJ8kYjOJVU9TZCfgKp7bRWfMEYOUJ_4s10sQCJKXyCHdJae-4ZPgnqePbOocB0dZ0EgYyYwvhPvfV0fpKzvFUlcLIqWknMuc279iB43F30sBG6IL4oZo0k8JiRbTyUKDVi2XfSZsFJwj1oKnp7KkG2PisTOpWBALQtYXuIVR8nE-6QnwsXCxYJbTLsRq0DeWFqi3qFtepElhnQ3zcQOdsHRD9rQbGT3B7nfJe1E7NjxLbIuJKGB6AFduEykAop5WTy_7kBqSlq9ymc_FsDZr7_0FBAeIiCY2wV50Cq2IX93Xb3Jci4bFcEmjzwQFrc4I-0VTku15baTGd84ON8nP9RB6769BW5N77sE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/06db464749.mp4?token=hwJZGJaVcg2sB-VBzRdh1v05Cg9iW1cxiuCGLEMHeEr32taVA8Q1ZGL_kRHLixeV9QD2FlakTidLqOu8xlkEmy1uvM814JP91p17SDfFq_Vs-YE4UTBECuy-0gbhyPeAZXJjAraK0k9WaSJaFSGBpcI4lj1iKTzPfMvSgxyDxL7JWFuuquwi7WrnXlgnykb7KUMHm4L9-Ip2_r_kH2PKg9-TYbSvNMkZ2kRLabmwsO9Rf3wKHZzjaz8-ywYLoLpHB1O7hEl1rZ_IqVa4gXezTCr3jPqEv9RWEKXrabx0I9hUpN1-RnCRANJgHg4f2St8p--D2HsRJJ8kYjOJVU9TZCfgKp7bRWfMEYOUJ_4s10sQCJKXyCHdJae-4ZPgnqePbOocB0dZ0EgYyYwvhPvfV0fpKzvFUlcLIqWknMuc279iB43F30sBG6IL4oZo0k8JiRbTyUKDVi2XfSZsFJwj1oKnp7KkG2PisTOpWBALQtYXuIVR8nE-6QnwsXCxYJbTLsRq0DeWFqi3qFtepElhnQ3zcQOdsHRD9rQbGT3B7nfJe1E7NjxLbIuJKGB6AFduEykAop5WTy_7kBqSlq9ymc_FsDZr7_0FBAeIiCY2wV50Cq2IX93Xb3Jci4bFcEmjzwQFrc4I-0VTku15baTGd84ON8nP9RB6769BW5N77sE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
لب‌گرفتن مردای کره‌ای با زنان مکزیکی‌ در حاشیه جام‌جهانی
😐
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/Futball180TV/92550" target="_blank">📅 11:03 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92549">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🚨
🏅
یاسر آسانی به باشگاه استقلال نوتیس داد که اگه تا ۷ روز دیگر مطالباتش پرداخت نشود فسخ میکند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/Futball180TV/92549" target="_blank">📅 10:42 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92548">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/92ec45dc61.mp4?token=RpaQZNTuR25bDlhsLkwCYuFByv7ZVinW3hJ2xrgI2hd0ZOEb4y05HdWNca_CFbD49dQGcP8jczc_2CYaC_kr2l-G-tWhDSLE9mBheGadT6WoYvrlPRN4BIxFnb4JBDN92quFwIQb6PJfY94QHtGOk1ooGbSz8GuQZsnAUafDX2KW8723MFlH16-98BCKYb-N2eRDPLThhBiBlGtEwJkcjAZg7BXQxSWZn56-Z3XZ4vglz5R8A877wEBSnB_sg2uzReMNlm1nMDjZbbl0DW9x98DgR_ZjKJfmi8eHDuQSqVY_Utvdpq06sESAt6OF0aPZCTwtY0WA82OeAGLh_RjtLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/92ec45dc61.mp4?token=RpaQZNTuR25bDlhsLkwCYuFByv7ZVinW3hJ2xrgI2hd0ZOEb4y05HdWNca_CFbD49dQGcP8jczc_2CYaC_kr2l-G-tWhDSLE9mBheGadT6WoYvrlPRN4BIxFnb4JBDN92quFwIQb6PJfY94QHtGOk1ooGbSz8GuQZsnAUafDX2KW8723MFlH16-98BCKYb-N2eRDPLThhBiBlGtEwJkcjAZg7BXQxSWZn56-Z3XZ4vglz5R8A877wEBSnB_sg2uzReMNlm1nMDjZbbl0DW9x98DgR_ZjKJfmi8eHDuQSqVY_Utvdpq06sESAt6OF0aPZCTwtY0WA82OeAGLh_RjtLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
ادای احترام ابوطالب و قیاسی به جانباختگان اخیر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/Futball180TV/92548" target="_blank">📅 10:37 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92547">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f5e274533.mp4?token=WBTAEeRwct_nJBrbws52ogl8OGPdlbnHp-y_50uSO58BqeagIjj6j8n3hNSMGCrYYsX1xxYFAn9cvjmXeWz6bYZFi_PeLX8iJ-6HWLhSPq-PcaUFW9DxJk6DX1guaHGZ8w6vauCrRLUlNw2BICrWPcoccCNZa46o6fbxSOSl6e7RznHiQdpVdLjErHf8Dy66xkxtkKUS8xlYt2QO3TBUz3a0MTBQXvO5j1K10spELGfTs4CRVjb_VE2Qyn6hJUFF6QVxAj1wn0Qidlc0Urj6VJvWaun-JpT0NKTkOjY_M7n1BTft-y_Wq25hXufETjjt7468Nw-HwAgNubaREDRtJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f5e274533.mp4?token=WBTAEeRwct_nJBrbws52ogl8OGPdlbnHp-y_50uSO58BqeagIjj6j8n3hNSMGCrYYsX1xxYFAn9cvjmXeWz6bYZFi_PeLX8iJ-6HWLhSPq-PcaUFW9DxJk6DX1guaHGZ8w6vauCrRLUlNw2BICrWPcoccCNZa46o6fbxSOSl6e7RznHiQdpVdLjErHf8Dy66xkxtkKUS8xlYt2QO3TBUz3a0MTBQXvO5j1K10spELGfTs4CRVjb_VE2Qyn6hJUFF6QVxAj1wn0Qidlc0Urj6VJvWaun-JpT0NKTkOjY_M7n1BTft-y_Wq25hXufETjjt7468Nw-HwAgNubaREDRtJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🇺🇸
نیروهای سنتکام هم دیشب اینجوری بازی تیمشون رو درحالت آماده‌باش تماشا کردن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/92547" target="_blank">📅 10:19 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92546">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aa-23H2AFZsmFaZmcDRvH0SwJij6d1dtAIToBB5gZmt3QKoyqCjlihQ0PZVPzs7hac1CEjHwBTmB_lHRHz6MzNLWTKKRx3tTWN_8BPmJhE1anj4Y-ypfZDnwWo816CMXf9NRxCMkckga5dwpTckYiUONY_ku8QYABh4PW325m7T-QfjhfZNyaYBQOtc_o5BByu9p8_6XDUCo5iva-bXbO7hukdGLd3X6Tzz16Sxa-90iEVAyLWufGjxZ8oTrdwOy5crmhwwXC9S7XVLn9RHCTQwB_aO5UmeAsRxxpJhWH1UNx6HCzg_hUIwNDt7d0D1Yft7zAZ9FUXlVTNVUZkaroA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇹
فابریتزیو رومانو:
میلان هنوز با اولیور گلاسنر به توافق نرسیده. در کنار اون، روبن آموریم و ماتیاس یایسله هم همچنان جزو گزینه‌های هدایت میلان هستن.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/92546" target="_blank">📅 10:12 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92544">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d707ba521d.mp4?token=FKnQO62LeulurD5drZbRB3-1f27uIwXSn2-18sR1UhNteoZcWf3vgNRvDsv68ZNL-SUvrip1YQkeN-nO8k-wvVJgZKB9wH91Rz3Xxa-LWSEwafbNFMFPNCaF2qp70Go4ZLzMIqKwozpwpcXHrxK4ppE6zT7RWC_C7zt9aDmQ211q9FOMKwNN_HrMWI8dnjDdLZHG31UldZj2zbhJmGtn7clSmBguoazFQMv_tUH4wyttCTPSvKKUckH68SC0FoRCxvk5aB5vbrBjg34JNxsKK1eySEPueMBPaDUOhY42BBeNq1g1Yi6i7dAfvp3YWEL7ltgxoHphRlWBB0HuhN-m0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d707ba521d.mp4?token=FKnQO62LeulurD5drZbRB3-1f27uIwXSn2-18sR1UhNteoZcWf3vgNRvDsv68ZNL-SUvrip1YQkeN-nO8k-wvVJgZKB9wH91Rz3Xxa-LWSEwafbNFMFPNCaF2qp70Go4ZLzMIqKwozpwpcXHrxK4ppE6zT7RWC_C7zt9aDmQ211q9FOMKwNN_HrMWI8dnjDdLZHG31UldZj2zbhJmGtn7clSmBguoazFQMv_tUH4wyttCTPSvKKUckH68SC0FoRCxvk5aB5vbrBjg34JNxsKK1eySEPueMBPaDUOhY42BBeNq1g1Yi6i7dAfvp3YWEL7ltgxoHphRlWBB0HuhN-m0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سم امروز تامین شددددد؛ تقابل بلوک‌شرق‌ و غرب در زمین فوتبال
🤣
🤣
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/Futball180TV/92544" target="_blank">📅 09:58 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92543">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RAAMcjebaRXuo0FDueSecjuopYJH9wcB3V4HTPV-kuDHcJ7MatE336EEdBLe43WCbxV1yZ4zGWvnWFpzfSAPxpsRvckgSVoR0Dc2IkyYwP7AfuJhdFwadQTkmvpFmYrb2N6R1sPlgiOXCiXWy38NmjGn_LcYPM9Tzg_MQK1lX7kb8Pe-MYNRc4s-adny9viV9U5tljTO3Gxu2sRFyoe7hcwFBDXGkP5lI3Z7wSUPHcXTOFRwQrI5mzpqn3ljybENmH60pAVMeuonTmQFPcBAG42ir62SedfXJnmI3y1mJQbW09l1fcGSZslomk_zL1ZcN4Vm7czOfiPn6rhhdXC3Tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤣
بورس ممکلت با صحبتای دیشب عباس عراقچی از سبز هم سبز تر شده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/Futball180TV/92543" target="_blank">📅 09:58 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92542">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/Futball180TV/92542" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/Futball180TV/92542" target="_blank">📅 09:58 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92541">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17bdf5f245.mp4?token=dzp8DDlIp81axCRoociaXHViwa4ItDMAowzzZ1KsINWbgCwdH3OIjlWirJaS6o7zSxqza__5dt9e0hG0fmHfT8bkkCkTcJR2oFiMXfP8KAO5kIUSZDEmb6WWZHttIjn4IPsDivs-3WDANSpVyYerok0Z_y8SXOAbndSfQ1ZbzBCzM-8sisoKAirCYRZo0JaFORoqtHCiR_PwrbcCII087MFsRgqEDJ1yF378CWAx-B9qJvKQ-N_NlZKFjS3m6eRgBm9FCk4iWLl47B7h6_Y9jdZ8ajVOPKgDmYJ8LjFMsvDCuDdjRrU5dbFNtqugWFMFC7hp6wUYL9vy2oVnuYhJkAGhTuu0UzeRiiSH5-Pi9zn9jxbTVhFOej0Ij-SkrpmCMtXIoBhUrWIJk6NbbP114hvgrz7tM7Qs17NLw5LcLQ7MuVd5bYW52_1knIfZyw4gGn74AC-xhRh_UCivb_hAiTBUxNU7gNzlZl0TCTpMmsdIL3IMzSks8beoFUBHgAIFHstSuRvB9lwGxjf9ch0_opIzKo9MMfAeUNAXA1_-KFDPgCpj2IWEx63dbR1Gb3OyqtQxvzST3cnEobVOuFMcaI7zS-PDXze0v7k5AmNYiEAhMOMVJ1wYxApE7IlU05GBkIubQ2w-Bw-1qRIvHxezOsnC-Nha_sCa635zUkq3Xh0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17bdf5f245.mp4?token=dzp8DDlIp81axCRoociaXHViwa4ItDMAowzzZ1KsINWbgCwdH3OIjlWirJaS6o7zSxqza__5dt9e0hG0fmHfT8bkkCkTcJR2oFiMXfP8KAO5kIUSZDEmb6WWZHttIjn4IPsDivs-3WDANSpVyYerok0Z_y8SXOAbndSfQ1ZbzBCzM-8sisoKAirCYRZo0JaFORoqtHCiR_PwrbcCII087MFsRgqEDJ1yF378CWAx-B9qJvKQ-N_NlZKFjS3m6eRgBm9FCk4iWLl47B7h6_Y9jdZ8ajVOPKgDmYJ8LjFMsvDCuDdjRrU5dbFNtqugWFMFC7hp6wUYL9vy2oVnuYhJkAGhTuu0UzeRiiSH5-Pi9zn9jxbTVhFOej0Ij-SkrpmCMtXIoBhUrWIJk6NbbP114hvgrz7tM7Qs17NLw5LcLQ7MuVd5bYW52_1knIfZyw4gGn74AC-xhRh_UCivb_hAiTBUxNU7gNzlZl0TCTpMmsdIL3IMzSks8beoFUBHgAIFHstSuRvB9lwGxjf9ch0_opIzKo9MMfAeUNAXA1_-KFDPgCpj2IWEx63dbR1Gb3OyqtQxvzST3cnEobVOuFMcaI7zS-PDXze0v7k5AmNYiEAhMOMVJ1wYxApE7IlU05GBkIubQ2w-Bw-1qRIvHxezOsnC-Nha_sCa635zUkq3Xh0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
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
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/Futball180TV/92541" target="_blank">📅 09:58 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92540">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cyi2JMjvxufXzBT-0BSwZYokn_1ZCc92LpZIpkCJ-KAUsTWP8Sshn905mgTHA1ByCPnEyBOL4NW54bH1RMf42RaceHCbpQVQsyAEJzAHbY72jLHRz6cvPYyvDnl0YSzyS5eq9Tde3-JEWUwHN_orTUSYHlHOtzgU-oaU0tWdCfT3oQ__qI3PnTA_osR8nqqyF2tKK0Xn1DlSrjAqdzjNoIBXDAeLxKh-8e61Q65ueXiRnXEAuYFlFqWVq7tyMPGbCREB-UqSeVIi2QMm1tl97ZSMPU1ynPWc9bVzEw69AMwMKBXsmWvKBCqFU9GgSAveiR5v4JGHb-gifN-XEcrXRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
دیشب اسطوره‌های واقعی هم تو ورزشگاه حضور داشتن :)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/Futball180TV/92540" target="_blank">📅 09:42 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92539">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0641f25512.mp4?token=c-3oeZGJ51WevCwD-gKBRnUOSkufraVJ0tv6rb2-iD4bLG1_jeMYcBuA4_2Qmt5wJLKysjo5uBP70_kkcZzhOC1jo_8I7lKQt2vKjHPaLDoOVqkdYQ_QL96HdyX6uhvMCX7f22_dnFW8v7742xi39bmwllOpO8m-wX5-f728zkVXH003MQLec6O6kHtHDxm7UmGxEWvd7ou-m4S-WPkd8w70vPriGFMLp94xjjxu6P5P6hfqOyWt4t0hUPq1oiFD3L5loJt_t10tn9lQbE42_FWOe5Y_Z8fnD9SZ7-r-MeM8uRkXWQ0Bg933V1tbV8FeqrFqw0MAIkZTtZ5eBIhwOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0641f25512.mp4?token=c-3oeZGJ51WevCwD-gKBRnUOSkufraVJ0tv6rb2-iD4bLG1_jeMYcBuA4_2Qmt5wJLKysjo5uBP70_kkcZzhOC1jo_8I7lKQt2vKjHPaLDoOVqkdYQ_QL96HdyX6uhvMCX7f22_dnFW8v7742xi39bmwllOpO8m-wX5-f728zkVXH003MQLec6O6kHtHDxm7UmGxEWvd7ou-m4S-WPkd8w70vPriGFMLp94xjjxu6P5P6hfqOyWt4t0hUPq1oiFD3L5loJt_t10tn9lQbE42_FWOe5Y_Z8fnD9SZ7-r-MeM8uRkXWQ0Bg933V1tbV8FeqrFqw0MAIkZTtZ5eBIhwOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
دیروز خیابونای کانادا در تسخیر هواداران بوسنی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/92539" target="_blank">📅 09:40 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92538">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pTr-F2gFfy6BHk7sQHNI88Dp0M5fBPmAc4JWnOvZQg_zNZlvIlMYuAALsPLNTlQBNfEsLLlpoDa0VFBWeMwPIyIIcOM4Onf46Y9B8olDtlrJZgRdotwR-_pvFEE2SPgaork7pHHUsme9iwe-SpCtnC8tKlkAmo-Hc-iYFVwcE5gvt0uHsKKR2bVIZGmsv4mJKDWK9cUlCzSw-MYas9oulul7xfNA8fvmdycTMC7CJpm-uQAjaAZyL231L0C_SzZUpTzbeTVlDRp5uDXYvwfdAxmUtCxW8k3-Cmh2eqPy5wmkC3RhxeRrRHzYZLMgJFqVMCu87VxkmAdzU-7dH-UNMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
نیکولو شیرا:
لوکا مودریچ پس از جام جهانی از فوتبال خداحافظی میکنه. همچنین این احتمال وجود داره که بعد از بازنشستگی به رئال مادرید برگرده و سمتی در باشگاه بر عهده بگیره.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/92538" target="_blank">📅 09:22 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92537">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1f6db524ee.mp4?token=LmdtiDKMPyYd30bC95Ghg7EipGdJVU7H6HTfP1yEKa5lgwa0HLy5NU_9OJJlicxkf5RyHK6LvOohi8KVBobefeB2OW_6V273q2kIK1lrc1hYAeMtr8IOaY4uOvV7xxKFd-WxINOAsEs0D8mrCJ5DWXyQGqVdEW4oYm3Xw6qd5P-9YDgsgHVLeO_vx1E3aFNNOEB_cGDlMYwcuEk6aVt4qnTfU5eSxBf0w0s6NXBJ1R38SzkESOY7ooa0z1MnAnT8IdyhZnsTR32uTe38lOTQaVLIwwRcWfrgGQR4P4kwT8561RICbcwO3JXZwI8XqJPsiXXYG-cssJgxSdl6aU28XqGrqKNuDYiVlpgjBw8R3BONJ73Ln50adr5MbnjVQ7L66vWcMxXIeEnVzyNdpKIEyqBOeiBYA5RUN6878BJ6zWzyzF7YNilFInWtN2-72R3c62F9pXsL2jASgrn2ar1WgIT18Gx1kiIbz58pr2CVm_jWpQxsQYU2Eu8YmIipcDpfZ-lu7DHC1zYcYgufkxa5_OF1gtcgq-aFHqrIBVB1X8F0uTxsAhjqFlmvRvz4bEy_G0C0T2SNlul8ss5Yjc4Ru-98Ai5NASJOxO6CZek3IfVSaoHM44pG-J-LU1jhdMcD-16INeFSo3zlC_iBXtw67Ya6racHu5sqA9UVjwamvPU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1f6db524ee.mp4?token=LmdtiDKMPyYd30bC95Ghg7EipGdJVU7H6HTfP1yEKa5lgwa0HLy5NU_9OJJlicxkf5RyHK6LvOohi8KVBobefeB2OW_6V273q2kIK1lrc1hYAeMtr8IOaY4uOvV7xxKFd-WxINOAsEs0D8mrCJ5DWXyQGqVdEW4oYm3Xw6qd5P-9YDgsgHVLeO_vx1E3aFNNOEB_cGDlMYwcuEk6aVt4qnTfU5eSxBf0w0s6NXBJ1R38SzkESOY7ooa0z1MnAnT8IdyhZnsTR32uTe38lOTQaVLIwwRcWfrgGQR4P4kwT8561RICbcwO3JXZwI8XqJPsiXXYG-cssJgxSdl6aU28XqGrqKNuDYiVlpgjBw8R3BONJ73Ln50adr5MbnjVQ7L66vWcMxXIeEnVzyNdpKIEyqBOeiBYA5RUN6878BJ6zWzyzF7YNilFInWtN2-72R3c62F9pXsL2jASgrn2ar1WgIT18Gx1kiIbz58pr2CVm_jWpQxsQYU2Eu8YmIipcDpfZ-lu7DHC1zYcYgufkxa5_OF1gtcgq-aFHqrIBVB1X8F0uTxsAhjqFlmvRvz4bEy_G0C0T2SNlul8ss5Yjc4Ru-98Ai5NASJOxO6CZek3IfVSaoHM44pG-J-LU1jhdMcD-16INeFSo3zlC_iBXtw67Ya6racHu5sqA9UVjwamvPU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
رامبد جوان: والا من کاره‌ای نیستم. زنم گفت بچم تو کانادا بدنیا بیاد منم گفتم چشم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/Futball180TV/92537" target="_blank">📅 09:20 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92536">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a625bd5f87.mp4?token=Coe_5T_GJnS5jRoyfxq_kgTvx-EnTGRauEA3XJ_ZL8-7VQuW4739m_NMNIoiKl6s9UHges0r22lbt_r-n9PIMd2NSO1fWloSVJ7yy3voU3B1OzzXSz2hfr4Q3lBjaeqrhi4PT2qoOOTJNjBCHuJnxEFARGcGjAHzo5p4eaGUV4we7o3EeQCW8ADaMMCZ9pD2GR1GR5k6-BLc-0l1y21YaHl_n_XkAqPtET5NAOJZltqn0pPiZ89Gx_sQwuuHmH_Avze5hMnpdjZjUZsXl5rUOaAD_wSu4MeWLMWiwhRlg6-YGPvEYUS3UZ1ieBamYL90aKQyN5_g4jmlxSFrIGusSiJLPvgrZe7S8n-3jNlxDXjUPZ-AmfRF3vTQiGqo7_-FX92vk75PqaKfb3mZtTQy2YcV46ByGH1GtWKM5J97NVfN3EfkmO139Nfbq3kDaDpKnbN0UZQZ-qLWXTt45dkkBQHywg9Z-ZEGw8EkNgcPf2t3Zd119AFMJU0yLAWnVlYjAKrd6Ln90NHFQWkkvt6cfeKsGVo3stcUtt8yfp2IOWmmXuvM8S8vFZCTscdX4mdFZwvd3UeHjQCtRoxYP-3IGaWmHU3o4TirjJdo2Y6uH_8XI5CqvTkFR3n9Po5xgKtN2PlSQVHtYOjObXldsHj5taD7Pm-T8UFYaX0oSMZzX6k" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a625bd5f87.mp4?token=Coe_5T_GJnS5jRoyfxq_kgTvx-EnTGRauEA3XJ_ZL8-7VQuW4739m_NMNIoiKl6s9UHges0r22lbt_r-n9PIMd2NSO1fWloSVJ7yy3voU3B1OzzXSz2hfr4Q3lBjaeqrhi4PT2qoOOTJNjBCHuJnxEFARGcGjAHzo5p4eaGUV4we7o3EeQCW8ADaMMCZ9pD2GR1GR5k6-BLc-0l1y21YaHl_n_XkAqPtET5NAOJZltqn0pPiZ89Gx_sQwuuHmH_Avze5hMnpdjZjUZsXl5rUOaAD_wSu4MeWLMWiwhRlg6-YGPvEYUS3UZ1ieBamYL90aKQyN5_g4jmlxSFrIGusSiJLPvgrZe7S8n-3jNlxDXjUPZ-AmfRF3vTQiGqo7_-FX92vk75PqaKfb3mZtTQy2YcV46ByGH1GtWKM5J97NVfN3EfkmO139Nfbq3kDaDpKnbN0UZQZ-qLWXTt45dkkBQHywg9Z-ZEGw8EkNgcPf2t3Zd119AFMJU0yLAWnVlYjAKrd6Ln90NHFQWkkvt6cfeKsGVo3stcUtt8yfp2IOWmmXuvM8S8vFZCTscdX4mdFZwvd3UeHjQCtRoxYP-3IGaWmHU3o4TirjJdo2Y6uH_8XI5CqvTkFR3n9Po5xgKtN2PlSQVHtYOjObXldsHj5taD7Pm-T8UFYaX0oSMZzX6k" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🏴󠁧󠁢󠁳󠁣󠁴󠁿
استقبال مردم آمریکا از هوادار اسکاتلندی که ۳۵۰۰ مایل پیاده‌روی کرده تا برای بازی‌های کشورش در استادیوم حضور داشته باشه
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/92536" target="_blank">📅 09:02 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92535">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FX-EEMZRzfHvGTnNtdUiTjMguSkuYHg97-WkxV15g1a2iBBfxqp5X9P3kHqoavKlUJleg9eCWYFJNThLzOBnP-GMUdFpuc2u2nIA8xJ8r4gx5BAEgesTAy8S5eRG1dW6YlQAdfju-g45r49QgsiNg3lTBQ7UqDlLnAHuSCeTHraPEENV2JY4wwMYE7KwQye8XUy4UbG9qOtDkOLC5QvjwHFNJ0xdExgaW6-KzrMFyGlLCkwrF3aWrhCqKztKIzVxqtNNfhC9UyzB2jSajqPgZW4BlkMu_HnYQsOaMxTL3q6ixTJDyYq6VcyK5YSvqbTZRL31L5PmXkgLncx4Kh76hA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا قطعا لایق برد بود
😅
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/92535" target="_blank">📅 08:02 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92534">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QBU6bRezDAALOtxPFaUq-iCCpPXoWSkO0sQ3SZmzNklvRuCx4OdgazD7oYp1BmbUlfO9bdm0_El0CsxR4cm0U0iUDvD5udMJMVnYwMAGjJ57y6ZjD5j7GbtWqxFYD1PTdq2nJH6eJ0xxQQwWO7mYHblqeVWkGWMEoulu0QpO3a7-_IEaFWK4yU_1tzfxTkAskFguB9c-JZ1a2aGXVx2e9vgwCt0UfBHXyu26jctjZq1uj3hUoKfbKLSEuC4M42mp3XyBdB3ve-d5g3SZT9HygSDwVFf7sRuDZZR4_ZM4HBJ9O7q6Hcj3xWV-yBKz_i-M45WEG76-wYYMD05D_Q_8fQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🇺🇸
عملکرد تیم‌ملی فوتبال آمریکا به سرمربیگری مائوریتسیو پوچتینو
✅
16 برد
🧮
یک مساوی
❌
10 شکست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/92534" target="_blank">📅 07:45 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92533">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pzWyvVsBaIQOkWViEP5iYod5bYJQ0rO1dou0CGNI1wakUDFPlHk3SupGxvSpAbFhWKofM4WoFdvSLKA3YNbtRC5PiMsENJ7SOV9tJfiwi_cu-V-4CbH8mvZAtIKXY00X82Ygux9TPS-3jQ22PbRnAL2pieGA3Nbm9ODTlsGqlMKVlw1bGTQboLJPvNZ82Yu5e4ugOPr3c2XMi9HjZyDvmyBTAR1Pdp1hC4R-7Tz8Gug-BBbtoRAC02o5mk6bD0k4uFurH0c7sw-v3sufyo-7KHlUkXN-UrIiRr0ac3nS6I6QHBbG8kavVtskOe9ZcPT7S7Y3PRuyFNPGcElzxowSgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
📊
| تیم‌های آمریکای شمالی با بیشترین پیروزی در جام‌جهانی
18 برد —
🇲🇽
مکزیک
10 برد —
🇺🇸
امريكا
6 برد —
🇨🇷
کاستاریکا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/92533" target="_blank">📅 07:30 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92532">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rMTqGJkiVYwYI1KjOWw6639YJkeMzw65iWmcXlWXCononnHX43go8UHsaH-5MBVhNDVjTnGqzCjqS16h9-7Sp32XGHx8DZknLJ3vxGG6-myCaHL9mjPzcjNV0UXH9lYHbG9_6bxZddbSw-8DDv6_jcv6izedvxGnyxQwwuHQk0XfPmMp_F2eCh18yAlc6B5pMielydqg4oFWhjI_pszn73YVMYtybXnirb3NWlGTccsoqBk4uJ53DsqjigWWwsvwIhPoHGh88vpJKbO-rB3kmSe7GuDR8odjvigau9ddtSWp0m7MQCg81cd_chT3RC615urpWi47q3XYqfONM-s-cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
رومانو: بارسلونا همچنان به جولیان آلوارز فکر می کند و این بازیکن نیز به ایده بارسلونا علاقه مند است اما باید منتظر باشیم تا ببینیم چه اتفاقی می افتد.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/92532" target="_blank">📅 07:25 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92531">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HBsO0rtCTEvGdcGVIPKvCVKgk98q2d4GWllHtAAJluNMsCOYzrgjr-nif80T4nC3S5IX9phrtxCjPe_sEHB_5G4ZA1Bh6Su6LxeQAiOboeojOcxfCXkv9E7-4xz1hgprD5_cDCm_e8kKeYJ0F-RDho0gBfVpRbFm-nXRlGjAmc3BZghlMM0x5RJWeBZh0gFfxB4aI9bk6PZVPw_0i-xbFD1921MUdusoC44EahmtvU5sSMGNvajRSc6llGv1fhR9Cm0dwnnwiao3Nvulxa2vjrSDu7ZZjI0Qb4cgZLWgjvXRnJi-TDfKtN8BEzYjWeSoeaeL8kUTCH9X4AiEJao7fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
شکست‌ناپذیری میزبان‌های جام جهانی 2026 در خط استارت
✔️
مکزیک
2 _ 0 آفریقای جنوبی
✔️
کانادا
1 _ 1 بوسنی و هرزگوین
✔️
آمریکا
4 _ 1 پاراگوئه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/92531" target="_blank">📅 07:18 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92530">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rTqH9rDuTnG2oAeJFsosj0R1Qg-BbKaA90GZadmIKUUuGEWg0F2Mk50xV5pB-tOth-NSbzPqI7UncuthynzI1bJUq45retyjafP-3IBwDe2Lnxh_NGbemTqGzA8Mh4QHTKHAq3Hou-yClTsx8JMahp83A6hSO3rzIAVL-cdo7B3hi1spr3XIqO6UFguHlldvYMzePSn014em7wtiVfFxfnT6Mvle_t-5KF6iyMt46l-eYdDfF7hF-EJNDfTKlHbmjUhlKWD-WPejiTNf8ilIOOJY7-xcYV_rRCgXYlDil-a876eu1QZX3z-6MSdLvwsl5jf01_22rcJRJwIfjg__yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
🏆
بالوگان بهترین بازیکن دیدار آمریکا - پاراگوئه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/92530" target="_blank">📅 07:00 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92528">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Wx4oqSitHLAlsAgRahwUz5n48qolUAsu2ABFu0HLog5VV9tBeLBRu8kQ5NHDasHRIvEAoiKDHkG8KFdCJDL_ixEiRQtLVL9Ma1nJEHwD3KfhJThz-rJPbjOOWaVi9VuxGrQt0PCmptHKsqM4R5eHPaMWjw49QhXC-Yk3H3_KLiEDbX46NPOOOBPutdUcu7y7yTbS7patTzWychK6S1mvPhgn-ntFW6Hp_aExWsc-1EYCSlUO6exZUQEKnKDY9s9AgmHk8nbS4gGejdxxc6bmGGeCWjrqo3zQsLeIESqo7VpmWbp_mDfRnWjmhtJ3NRbMyihsmr7Rmk7PKxBFVEnVkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/B_V9yMmX2861qtiEbTR6PPi0108LRfigOLFv1KFDCf2sDRjogcSd_hLgwBBM65mXmRjpYlTjiYwOX16b9lALFi-jbDKTiEHJFvsRloRRZv20hU2z62t0CeJUr7JMR74o2iXD0A7Agwf_aN_JQs60-_A2kj1oY6-_uH1fh2ChsP8_zlcuZnY6p3m1ZmRRN5l5m8HoI-En1JCie6M5ohceYUCeRgSXAQjLm-5s8KyNPXVE27O98pRbyszEJDLqOwICiwofT8jv1gs9U6dKtjOtNlp6Mzo-0K4cC5p9T5EteeK27bc6Bm9sy5sLksB-jssDBTYNlZ8UXm3WdADy7rJreA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📸
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/92528" target="_blank">📅 06:57 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92527">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F79uXakMUnXECWoL3qw-RnRpA9niST5OfqTJYHaqaoEdKz6UtyEtZLGWXiaFJ5cKmLNJzAAqKO2lRXVrhf2LIzqQX5SWwv4piUPES2U6-ZG76ZQ5sYeD6-ZRPaoKJUJnk6kpFMwliQsDdL2dbVYHuC6p_2MJhvIXKF9V7LOLSdXo585qybpzOEGTRgYHzN5RHQVbjXWAj1hpMK_4gDT_zDBwwDOh3Epep29yR6CXIAmATtrfxi4Qndw2jV-N-HE3W7Iq4ZtSIuCgSql03tLcwtxbqwRP7kI8x7DvJQ_4k7WcFkLovNtRfsMryni3CqOyG80AMYitZob7RB0hcmzm1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
آمریکا برای اولین بار در تاریخ خود، در یک بازی در جام جهانی ۴ گل به ثمر رساند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/92527" target="_blank">📅 06:46 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92526">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DwW3p1sWk59ZN4klPfUpKdCqER5z-PwaKkfWSypjPE-HRrXT1TJfKHC4lBGcJZqCXtZJjXxCm5GOaGYm_oHva6_ocufdeyCIal7VqL0P6BmNiX3uh7cb41iI0vp9T1et5T8iUnkujgl3koPBtQSWE4Tf3ylsPKHIX4Ofx76wbRoNl4PKG72YhnkDvMgD-Qf_qzocJ8VyjqBD8pQ4s328q2IB9KUHYaFqEG5PGUO-fmtbjKMxuCPnbmP8FpJQRJ4ssG8Zotrq03MK0jWnb1M4UQFmgWPpEyIzviFzAj05SLtYcQUZEU2MSbkvm0oIaTNiCaPWtkjLRgmiiYG4hEsh9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
✔️
پایان بازی |  نمایش درخشان شاگردان پوچتینو در خانه
🔺
آمریکا
4️⃣
-
1️⃣
پاراگوئه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/92526" target="_blank">📅 06:40 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92525">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K4aSjp-w-m8tJ1En4auwDpponE2zdkrPFMFb2GLHdh9T6zQmPQD3Qr0D-nm4QPTfCY5VR6G5fzUbeaXG17Kw7YfGNdvhpCmWGN_QB5HhEaeHZLi79Sh4IYk15w8vBcC9k4VHs1SbkkxQ0n2gdsIjds3mbBVb-axxsbAyIJyh7j2RMUaeV6Ipvk8hhjgbz7Oc1NjleEVAasiyi6OLPJXc5q98iYkKU_r0R4ddDkA6T5yMvPqbGVhZhErjV9JxpBB1qgLr1ECIpsxHLX74exurzkwhZvgSeHJc9nfGQsYmQV5jGq2C14qe9uZXVtMfFWctVDpibPgzb_XRkv5H9XV5hQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
✔️
پایان بازی |  نمایش درخشان شاگردان پوچتینو در خانه
🔺
آمریکا
4️⃣
-
1️⃣
پاراگوئه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/92525" target="_blank">📅 06:37 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92524">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e217c2352a.mp4?token=px7jnXbMaw_PiwpSk0j4EbR1GdL-MAEl1jfN8Ykxvn0TAdV8joUm22NYLTMzPCWY-mizvFG8PumCAKxoWjI6ql67uBm8J_Al-IDTurGa6vhunThTuTPIn_ZGxREXzE3skQaPUf9Jfzqifegd3BTk2JoJMxJlkam578zR5M45Ujyzp3Rr_BJlp5b96YcH_84rdUko1jRDcHpQB_zt_7jytKYI5Jd_kNCiXA9XgogTX0dGP6L3DWJN_RnuGaqo7_qxFuJJ9lEhaaVjF1KGOYg34BywZxFFqC-tBKEyOKbptqZoV5p2vrv1OPb8bxU1T6NZ6oLyMXfo_L9CaTuYZS0Y_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e217c2352a.mp4?token=px7jnXbMaw_PiwpSk0j4EbR1GdL-MAEl1jfN8Ykxvn0TAdV8joUm22NYLTMzPCWY-mizvFG8PumCAKxoWjI6ql67uBm8J_Al-IDTurGa6vhunThTuTPIn_ZGxREXzE3skQaPUf9Jfzqifegd3BTk2JoJMxJlkam578zR5M45Ujyzp3Rr_BJlp5b96YcH_84rdUko1jRDcHpQB_zt_7jytKYI5Jd_kNCiXA9XgogTX0dGP6L3DWJN_RnuGaqo7_qxFuJJ9lEhaaVjF1KGOYg34BywZxFFqC-tBKEyOKbptqZoV5p2vrv1OPb8bxU1T6NZ6oLyMXfo_L9CaTuYZS0Y_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بیرون پای سکسی رینا به پاراگوئه رو ببینید و لذت ببرید
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/92524" target="_blank">📅 06:34 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92522">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">عجب سوپر گلی زد رینا</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/92522" target="_blank">📅 06:32 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92521">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">گللللل چهارم آمریکا
🔥
🔥</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/92521" target="_blank">📅 06:32 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92520">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eY7K7p1SfX7fJtT3VKN6Q8vgoS2oq2Aix6eR0gG7_oTX2oK2DF0cfJn0T4R45DBn1vk1jsjooXjQLOPiRq6GHnTroD7E1A-rm0fQiAjWVzZg8oUj8AADdnaflRYWSF65-hT5CyIl4sWbqyNcG8l2HSkxKYTJOGS2P6giBlNa03sWhM0cK4M5LRiLAlhy0Tspt4iw4KuIvqRGx6Gqe_cel_zsELumt30n_kubwrsoQv-KCfM71cvPrqMZdB4jq_JgSKrAEcbNCB_CakTrWMlWsz2x3ugTzFdoUQxmf8HCFwzNDHfgu6LSYkYDImG7BoTwZlf50st5dp99M4ldv7-RIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
🇵🇾
70492 نفر از نزدیک بازی آمریکا و پاراگوئه رو تماشا کردن.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/92520" target="_blank">📅 06:31 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92519">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f_2YzvhaqYVkMzJkxUl3SoWEmMb3lSjV7XhFA1lslVzL0FlWqkyjm2K4bD6ckSm1GtCWHQ-nVqJUGdEedGtJ2d3_qEN7jUJhaxlnkFikJJn8cx_HQ3AI4E575hJVOBYZGHYJvKHEc9vcYqKtArfQOjzNDcCWw3i7piPvmJG3pgubn5XRFuhMMJaIF9uxtyp0GPi7mKlXO10Ax4L4rfI3rV29t33frig-1zfuiiEBQ8vjrkivU4bMjWzx1OKUs1jkP9RXocUevdL9IM_KmSPHBykU9tdvKcHlIo_H3jPbUz84b9ZTbNpz-vEQo-GsU8fY0F0PCMdseF2s6KU-aWsENA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
📊
#فکت
نامحبوب:
🔺
پاس‌گل های پولیشیچ در جام‌جهانی: 3 پاس گل
🔹
پاس‌گل رونالدو در جام‌جهانی: 2 پاس گل
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/92519" target="_blank">📅 06:28 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92518">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XQH8naEJ6HRgxHlatdbcvu01Z-UqoVGp8tgBr-I-5L0TqqMSe_L8Sk6aQIK9xjEZTeKWFnKL2m6wwe2a5kUQKdCxeMZg3WUQzV18pj8y9_xD00cyg8NVtSdBTq2DZaywq8d2SI3VkQ7R2fxB8IGqg0xviqNxs3OylWGoCe11cgSJLZ6AHNQjQeAtAub5WwqRniBrSM6C5ApZQ_GC3I19DgW978HEg7IUNVsDQRyRywrRQBQonr_lwKFRXx0EjYKk1Ug3gCB31LlPSx5YRSYXHBJWJ0Cpgo3nb7gQs8UuhAAWXbvOZhcHZBGqQtpJ29ZtFyWgNZDdIwf8n-JXM1LDNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
🔺
اسپید به زلاتان: تو فیفا خیلی کُندی
🔻
زلاتان: شاید تو سرعتت زیادتر از من باشه ولی مهم اینه که من سریع‌تر فکر میکنم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/92518" target="_blank">📅 06:22 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92516">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iaehdFShpwWKMsYXQ3jObxVGYP87HeAR-m5dVnZ7QxhlRSxf8KhoxFICgpso2pzOqZkZ8Pj5fGvmqoZnjGMaPCZQFlV9ln3j9ITy8mGqadB1bP7VzKoNXrx4ycs-Y2cd-9eHTCDIznwjY_n2RVqXqBDARdOGMppWf2bw6PGHGM05Yf4DYhT-ZwhBLdRVdp1MUBkLflEF8KA0MhoN9bdFpUSfKSKSi5hXCIcM2bMLMPKSh9aq5Sk_k52ZYB4FK7WArEk3I99t7AQovUFWPRt2aHeZ3pdIvDyPDBkbt5a9yIaqISs-7BKaJlqjHDcaUsP18gZXUiNjyPCpD7aEJ2OMWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oOu6ZbPUbJzpYEiwuPb7p0eu4D1BxgZKu8o102TNdaqq49TSGhzUy_nRy5NAK05IaMXKpKGRU2H1gYGv9xucGE_8Vye3hFrzjThMBU5wrgItUsNK8GgedNrh8A443AYG9vyYtV8WmhZqubqkaaYr9OI_kvP2kxoyrB9ATBi1bJMs8w18LbY9qMgE32ZwMr2OmQJ5dib4Npqsuq02JJR7hRtWfBkJxENbXKqBilzDkzjoU-PeqrYvTE2WPSUtx5Ekx4IRN6Ui0Us2Uuu_JFROWE5w3kNTUDVL6qoPeF1rkIiTsO0kj3P9_kKrEf_hC47jJNXW2ly1nwonkng6QPeHgQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">فکر کن چقدر باید سوپر باشی که تو اولین بازیت تو جام‌جهانی همچین شاهکاری رو خلق کنی
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/92516" target="_blank">📅 06:14 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92515">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/51d2169a1a.mp4?token=VAqSdqc8YCr-u0i3-eFkhBTFbVdJeghE08JJuCLZTwBT4h_DlYAjFvEGu4TkYgueAc1ZdsdDNFlKjE4tTIRty4AdTQc2_JQ6t7IpP1SXlwEhI-JnIfn3TRH_iefbytGzWFCeyYglgwi1HZ8RuZYzBlFbaJc7wA-G_7ZJNsRyVtRkL1tvByW-RHQqAfDPQgLgvgLWovu56BdQMqigCqDes_Jl7geH3gR0RBvWe2wp1APGhsV0OPER8sgD2a_ld90PzyazRJf5Kr9uMicx3y6R68sbSx5Y-8Ld2tg9v8u6-Fp5VpxzPH84KClDJn93op37_FsGDS4BAIcQIYyJSqshQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/51d2169a1a.mp4?token=VAqSdqc8YCr-u0i3-eFkhBTFbVdJeghE08JJuCLZTwBT4h_DlYAjFvEGu4TkYgueAc1ZdsdDNFlKjE4tTIRty4AdTQc2_JQ6t7IpP1SXlwEhI-JnIfn3TRH_iefbytGzWFCeyYglgwi1HZ8RuZYzBlFbaJc7wA-G_7ZJNsRyVtRkL1tvByW-RHQqAfDPQgLgvgLWovu56BdQMqigCqDes_Jl7geH3gR0RBvWe2wp1APGhsV0OPER8sgD2a_ld90PzyazRJf5Kr9uMicx3y6R68sbSx5Y-8Ld2tg9v8u6-Fp5VpxzPH84KClDJn93op37_FsGDS4BAIcQIYyJSqshQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇾
گل اول پاراگوئه به آمریکا توسط مائوریسیو در دقیقه 73
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/92515" target="_blank">📅 06:10 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92514">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">گللللل
پاراگوئه اولیو به آمریکا زد.</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/92514" target="_blank">📅 06:07 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92513">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/927bbb478c.mp4?token=AkpA_z8vmU3EBrV-nHzDRb_2M0kko2vhK-pq6SXF6UqVgj9Ime6nVU4Mh3P3T3RNRAvqLtGRzyi1MLms6s7VDC5FTjak_i3AHoQPs0iHvDdGEq0N8Nfu5GtD7jnxt4g3mP8OjJXMEkU5xHctlyzkGZDxokbEG9pQWmz54sYtMbq6vJCunuraOq751YTizxW1caysSOrOzEsK_5khBM0Ue9yFo1sKMMxrcA1zEWqE-xi7duDIYSU-vYFtMghw-VgxBdrk6eNxaPMZzjP2HRT5odexYU7mDvMvAahL50Pivf1RcT9lmkm4a3NBCmPhoWjNsAPZJ4BMHGiZHFCoSCEXtQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/927bbb478c.mp4?token=AkpA_z8vmU3EBrV-nHzDRb_2M0kko2vhK-pq6SXF6UqVgj9Ime6nVU4Mh3P3T3RNRAvqLtGRzyi1MLms6s7VDC5FTjak_i3AHoQPs0iHvDdGEq0N8Nfu5GtD7jnxt4g3mP8OjJXMEkU5xHctlyzkGZDxokbEG9pQWmz54sYtMbq6vJCunuraOq751YTizxW1caysSOrOzEsK_5khBM0Ue9yFo1sKMMxrcA1zEWqE-xi7duDIYSU-vYFtMghw-VgxBdrk6eNxaPMZzjP2HRT5odexYU7mDvMvAahL50Pivf1RcT9lmkm4a3NBCmPhoWjNsAPZJ4BMHGiZHFCoSCEXtQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
رونمایی از قانون جدید تشخیص هویت در جام جهانی:
🔻
در حالیکه داور با اعلام ضربه ایستگاهی به نفع پاراگوئه به بازیکن آمریکا کارت زرد داده بود با دخالت VAR، داور به دلیل شبیه‌سازی کارت زرد رام کنسل و به آلمیرون بازیکن پاراگوئه کارت زرد داد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/92513" target="_blank">📅 05:55 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92512">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2f73fbe3dd.mp4?token=AClaGiwcnOkUvMJBOTAMvLUQ1G92nzgaY-KBCyRgDsKxl3TRLyPz9Zs-MwQ4JgXkO4lGKj8elm9x7l0wsqtAyCEXD_L7yQ7G2TsiE1rrd4F7UOATLMGC_4oOCJdGgrhKLWJva4F8Vi-gEh4oOGPqcH2Aj2u7lS1VYNvPOKRvPTXXCO-y-WyDe4sP_E4DcZe3Ru2qFUlVvyWGmhp5yr1X99KFc6GyW_BnX4D5_rRkBlhPo90BAEdzNn6qT-8QlxuYjsxuJ8an9yo8EzGGiNp9AbSmQhtATMOvjrSOXbb6SjvH-ijBt2_Jp5Q-BAupmQ90fJNrbflVp93S4D24zVEvrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2f73fbe3dd.mp4?token=AClaGiwcnOkUvMJBOTAMvLUQ1G92nzgaY-KBCyRgDsKxl3TRLyPz9Zs-MwQ4JgXkO4lGKj8elm9x7l0wsqtAyCEXD_L7yQ7G2TsiE1rrd4F7UOATLMGC_4oOCJdGgrhKLWJva4F8Vi-gEh4oOGPqcH2Aj2u7lS1VYNvPOKRvPTXXCO-y-WyDe4sP_E4DcZe3Ru2qFUlVvyWGmhp5yr1X99KFc6GyW_BnX4D5_rRkBlhPo90BAEdzNn6qT-8QlxuYjsxuJ8an9yo8EzGGiNp9AbSmQhtATMOvjrSOXbb6SjvH-ijBt2_Jp5Q-BAupmQ90fJNrbflVp93S4D24zVEvrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بازیکنای آمریکا تو بازی امشب:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/92512" target="_blank">📅 05:51 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92511">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ef7c3eda2.mp4?token=msdYGsO3MMIGEy4WmqUWy4M_XIV4Ms4bj_bKDG207DFHsHtqxLKuSW3PS6_bicgya03z5swh7cuAdPJQJCecHQToRqiTaIXuOcULLAdoQolnohAYGVFcTZjqUS2bypQ8lv3dvBLhvka_yTaCA_nVXOigDijNPSWwSD6-hiyGbvLgSlNv24Rgy4SevC9NHjgVtKNWLShqUdVn7zerhGl4MiB5NHZmJ67338TOHQGidaiyW1MnO-zxWtCvv_WrL5ETJTBMrvlYnr8VA8hIOvUSEU5ViKdt_l5ZZz3iTrfJEQ5AEsGu0iaAwmQpb7Ynkd0HorMKAiaOSc-qAvPk2rtz2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ef7c3eda2.mp4?token=msdYGsO3MMIGEy4WmqUWy4M_XIV4Ms4bj_bKDG207DFHsHtqxLKuSW3PS6_bicgya03z5swh7cuAdPJQJCecHQToRqiTaIXuOcULLAdoQolnohAYGVFcTZjqUS2bypQ8lv3dvBLhvka_yTaCA_nVXOigDijNPSWwSD6-hiyGbvLgSlNv24Rgy4SevC9NHjgVtKNWLShqUdVn7zerhGl4MiB5NHZmJ67338TOHQGidaiyW1MnO-zxWtCvv_WrL5ETJTBMrvlYnr8VA8hIOvUSEU5ViKdt_l5ZZz3iTrfJEQ5AEsGu0iaAwmQpb7Ynkd0HorMKAiaOSc-qAvPk2rtz2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
جاذبه گردشگری استادیوم های آمریکا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/92511" target="_blank">📅 05:45 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92510">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">پولیشیچ تعویض شد تا برای بازی بعدی استراحت کنه.</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/92510" target="_blank">📅 05:41 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92509">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t8xD7nimupwuAKpCIJMgWkdBRnc7Wr4oHcFZ2uQJZ-rQfb0ygWayDJNkHM7E0ruth8GMTXSCS2MV1MUJV3nsKdMuKLGhYzvRXv7_KhoCIAdT0_s-fTAcgT0_PctoitC1aUGHPuXv6sJeetZCETbiktOi_vF5N4KIA4AsCAIcbrURcPLSXMoDH5RJOHahpCdyNsHCqeDnxc1c6ux5LjNtpiB8bhwwN3AuCeRWAiw6knLX8n2yWT6ciN5X7YIqvK_JI_hHoizi9c8We0PBZFePJV7NHZT7Tx4A6j2c5pw4l3pa4cdRGQMFNXdYt9-0_cJEJMPSJdXNNKlpzPYU3OBe5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آمار پولیشیچ در جام جهانی با آمریکا:
✅
5 بازی
🔝
4 پاس گل
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/92509" target="_blank">📅 05:36 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92508">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tTs8K-O2RU3TLiEcfcx4RSpN6xYOPFPmWY-e5LrMfS7k1E0HERcIasCdU8wbPt3CqPnVbV5dD87e8wqRMVDit9B1MctbleRRtate1UqTf5fEVIAjBrKxi3TL-NBvhJNOXv7rwnUYtS970EV4uh5-rtjzwVgSFk4WS-iMns4-Tt9V-AfEv3KRCyoZQSbeJT1nMA2FAAMJsmLWtplK9Kb1c_IWRGKoRPpbGewmQ9YiyhOlpsZvRKshwg5jPI5JsKsKUwMsrvNpZRo-J9nHR88c6PkWpl9iBeobsnElMmqPWf0hDrXFMyJUN2lVL_Lhm2ZS3MBaHY20pMxGWXkD7e9AQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
الان حال این طرف که روی باخت آمریکا 1 میلیون و 800 هزار دلار شرط بسته بود دیدنیه
🤣
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/92508" target="_blank">📅 05:32 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92507">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">پایان نیمه اول بازی
با اختلاف زیبا ترین بازی جام‌جهانی تا اینجا بوده.</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/92507" target="_blank">📅 05:24 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92506">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/1368a8262a.mp4?token=noAwFLUJDm_AurxdCdA4VUc-asOPMqC50pHmKTbMOJfnjcChL8L7EBm4WWTv5KhvaZf-DMY22QLTGH-ImgY_1pgEBUOuBE-SgBDkbY_5aMHL7PyNPCsInvAdFli19W2pvdXFHFQ1uoXrDUXivKHsxgTTPjwgcNKAHJnhUgZS89X89SBh3yd3Y4zxzTKglotl-ZIWG5TvplR6HQVemyBc-iUizqExUAJ2Lfb-uOkdpYdRc6qAQYoNTUW07T--zDfovf0RdT3LXNKcLGdSolrOOO7VjnwJP4oUvi3nczxM1-vZU6Tr82QbiN-Xu-3xmyevHxIcx2slmWnELizxn5Fdeg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/1368a8262a.mp4?token=noAwFLUJDm_AurxdCdA4VUc-asOPMqC50pHmKTbMOJfnjcChL8L7EBm4WWTv5KhvaZf-DMY22QLTGH-ImgY_1pgEBUOuBE-SgBDkbY_5aMHL7PyNPCsInvAdFli19W2pvdXFHFQ1uoXrDUXivKHsxgTTPjwgcNKAHJnhUgZS89X89SBh3yd3Y4zxzTKglotl-ZIWG5TvplR6HQVemyBc-iUizqExUAJ2Lfb-uOkdpYdRc6qAQYoNTUW07T--zDfovf0RdT3LXNKcLGdSolrOOO7VjnwJP4oUvi3nczxM1-vZU6Tr82QbiN-Xu-3xmyevHxIcx2slmWnELizxn5Fdeg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
دبل بالوگان مقابل پاراگوئه
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/92506" target="_blank">📅 05:22 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92505">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">بالوگانننن
🔥
🔥
🔥</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/92505" target="_blank">📅 05:22 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92504">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">پشمامممم آمریکااااا سومیو زد.</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/92504" target="_blank">📅 05:21 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92503">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/enJLF4W1y1eqbVWLiNuxryyedBEvS6eIBfQTbBSM44MOCn0NbwXvOpCZQT7-L0WOV-ZgN80536AxFhgs6BVJQVzrz1duJ9Dq3MVDHWg8SVfDymQvO0PylsUzj_S_jNhNPj51YJois51gsInvwvsS1Ox73ZZp58fIeokeSGcbxJ6hCdJrhjpopAlczKv19Im7dgIlMCt2dn_aKRzpBs5sj-KpqQOY3mUjfYjEFV-PojwdLZnOCbIBAbrn01nnntkMOG9JypTshkN0yyT5LOGAvuC_5K-cZmhjsUKXJn_Ljz88VKf-PLx91SdlsGqljIXHwYDJbHkTSjf-Ws-ZUh6Q9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ویو رو ببین
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/92503" target="_blank">📅 05:15 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92502">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VGP8DfiQnCHfHq3yaT7e2fUgMWYdYJmyEVnc4GLbufnsE21XRaJ_qWI5E9QNw9d_lB5NA-OCsADPfe0KlB4ju9VBXix7_c7kM3sB8RI7TR58wvxd1-nkD20bh365kuQVGiWp9r50O5xPEZLhvr36kG3ie6RBVkyjjqgXeFtgRxvefCRF6b8Zntf5VvRYgZ5pdf9scWm69XWe7qcsEqsaEj5cUn9utDPRUBUOwelyqySIIGOkhCe6RGIQ7HZ1KZf-mXllIo1yMv6vD9ownBS-kdmm_b8GElnpTcVhxPz5JFJ6gpNvY8hkEs8OnzsmGGsSEtWHj64EXNhkrpEKRv84lQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مارکو روبیو هم تو ورزشگاهه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/92502" target="_blank">📅 05:13 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92499">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Oj-FeHV9cGQZ4GQV3yGCM9USBKreW1zOCg796VP62HH1Gnwl2WEzZwzp1hng3IasUMS_uFZ0WyqWvRJpQxrC16pHo8yDwhucJOlZrKci8OdoyPNjgkxlul4AFjV9lM1lAl50WV9gsTM3YkWm8_L_lAa6FXYuCOThCKDS0Taxhra5b5-cEUKHfmlkK7WKbwuKlugyVEQEFCkJm2dx6SWL_UKWFah2Ec3flHkLeZP2iv5j4zxOssG20ylilFZWxtkMAWR_yc9-Yyje3bnzc_Ly8LzF7ttM7EB1PS4KV97bHBvDiCF192U1uXWm9NSldo2j0pqu81oBqygc9Xfx4YChLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UjyabN9MU_XRe7jamsFC1QLd6zXbpuP49jGyIK4sqNLL9zZLEMkBqmL7PZRCkL9nxpZa_3Mkm8c1hYRb_2yadw6GBd_UXCZKP_xSDua6WWKbf7a-rtq_WPqliCws7XOIhcR16hfCtJ3jwK2cSHNaO4rFDuqN0U5IhAEd6wmOx53Wpsoj_VjikhhquVyqBX1-AXVI3qP_i3S9ooUnk9skEO5YG_RzD58SLAXv5lq1v3bY4wMvwMtzKr4-j_Ej2vmvRvlJTrNA9Zw3YUpYYoytJ5HN36qKKyevsrFA-vsvZnDW6H8ZjEqlBBilAxohexA64KSRTIk2UQGr_DYUhHOZqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iN1enZFm7bOfxbYn1sAdto9CxJusFCN5W0zs3vovpvX92ymZUJoQTqAEBT16NipqQCRpA02ct-tZlBcIKcQu4agJcjGYsRNvuJPWbXooVYnxInSe5-iuhoDn_KAU5xtriCelO0T70uEfbT7txAJrE0UZQ-rf72xX5btG4cnChSMTUMdySK33XSsnvFsI74KO1U22zH8Gh_pKnemXg5NpiEcEgvXO7xyReglxnoW9FcZ4tMYNzFMrxKvtxADWlElzOxOP0_2YrEBSxGJ6P3UjtXw9DI_BJKw1BmuVZXZM3bu0HJo3dergF8vq52rg4rUtbnStUMOKmDT-Xe9jm8RC9g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">وینیسیوس لاشی چجوری دلت اومد به این بانو خیانت کنی اصن؟
💔
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/92499" target="_blank">📅 05:13 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92498">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">پولیشیچ دفاع پاراگوئه رو اتوبان کرده.</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/92498" target="_blank">📅 05:07 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92497">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/cceeec25f1.mp4?token=U1muvQmtNP7_mYh9i966JLln7Y_hk4Y3A3O8P_SI-Dg5qVagX3ZCuHJtd3PAThh7vDML9Mctf9a6amOKTjlRVGBaKFpT24su0FLKGhQLJkHgy5h89XSTNN8goLBnxDDjujh_U4bZkQU-K64x7mcxndCMqRMEiRgKRFR4wdPRJZyD9GG0qu7qBBYF_oyfTa1uWF15k1dcp9BxzYFGjvYwi3EtDBhDhXL4lJaKZJ2VVgkgYN-6mt5kWxRkFM0MjUZIeOSew2z00mqbgBkXGVe4NgJY_rvWIgjyuryhJGPpLfsIEwglepihNg2PzVwJcYlZSJ1oOCnu5OGKDfVi6C4Isg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/cceeec25f1.mp4?token=U1muvQmtNP7_mYh9i966JLln7Y_hk4Y3A3O8P_SI-Dg5qVagX3ZCuHJtd3PAThh7vDML9Mctf9a6amOKTjlRVGBaKFpT24su0FLKGhQLJkHgy5h89XSTNN8goLBnxDDjujh_U4bZkQU-K64x7mcxndCMqRMEiRgKRFR4wdPRJZyD9GG0qu7qBBYF_oyfTa1uWF15k1dcp9BxzYFGjvYwi3EtDBhDhXL4lJaKZJ2VVgkgYN-6mt5kWxRkFM0MjUZIeOSew2z00mqbgBkXGVe4NgJY_rvWIgjyuryhJGPpLfsIEwglepihNg2PzVwJcYlZSJ1oOCnu5OGKDfVi6C4Isg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
گل دوم آمریکا به پاراگوئه توسط فلوریان بالوگان در دقیقه 31
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/92497" target="_blank">📅 05:04 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92496">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">و بلههههه گل دوم
این بار تاییده
🔥
🔥</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/92496" target="_blank">📅 05:03 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92495">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">گللللل اول آمریکاااااا
⬛️
⬛️
⬛️
🇺🇸</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/92495" target="_blank">📅 05:00 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92493">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/i5qVPea5HAmU_FuPe7NSRilC9cvEt2hapTqSuKquL8FzvDidXyfdAVS0gwkEKdzKbkE6mHr3hg-IcRrDswa-gejBs-FuO3k6fMyQPDAfyFL8fhcdJNA2yPAMMiFH5x0Zn-XQzH-4sRiZz_PTH5SIio6xlGoaBUWfP5WDWFBBlinZSG4__uVqXP4U9kWeiUAFBsWl0pEw8bkS5_Bd52-Nvd3rojaqucLBiRTUGBTcxCUAZ70LXIDqh03E-DvuOtHxaWarS4kBfXgHziq3j_CIxu4Qi7wCnl-XRlwWmgbgixcTXxVPAfTV9o1vRQxk5taQ93AaQKam7ZAPibuvIdlBpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pjju7Q-GQ6pGz_I750ScjPVPYAf1NWL9d-1DXF4ju3ZXsWJg2qCF1zfbeNBL__WXzQHBHdNzHpRipDhbjvGYROABqU5WqPO4eC72KiVBvyb8_C0mXkwO3JHsF2E7HGXXJOfaBagbtY5hjODUGOdESIS-arBLIJwDbJ3QNpwhVWzZ-L51Uth_3idlCTLGlel32om8riwrxCpeYO0uSylCfcaaslIdfPRvwVsALF11gKCAlUk3aPuTfhePH8jwls0DTa5SUwdBPkhX8O6YOjfyKCi-CXC5v6HwnlGWrer7w8GXWDV25asoaTjUxmMCm9VWGXiY4FSGyZEPGIduYAl-7A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👀
‼️
این وسط وینیسیوس هم یه دسته گل برا ویرجینیا فرستاده و دوباره با هم وارد رابطه شدن.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/92493" target="_blank">📅 04:59 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92492">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b2fae2f7a.mp4?token=NJMu6FkUdptpO1fdYAwxPFdnELKpcXJBCleAgsdRxY9OrsOfbfd4lKH-B9cnhZ0LGRGnv18jqyyc0UT1B7wSwTtk1iWz2aRdfrESX2k62K3hJWKj7sIVHbdJDWib0oNVA4TYcXqHbxLkIOJecGWhSO6fxxxkKZAxrWlq6pCHFJECwDWmY9qsU9TiRSLr3CCHbwm6-kkVg-KVVjLqX-A2JG0jQNTHFhfgVzYtE3qutrLDrpaw-UGZ6IlhvWr9QLwf7jE4SgPYk8Yv61VXmh8oYAj96UYy__DQA1-AdTSBlVIxVbjbnsIcMbpqdpVqqo1Ngd825UjoHApwlLV4bw6Z5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b2fae2f7a.mp4?token=NJMu6FkUdptpO1fdYAwxPFdnELKpcXJBCleAgsdRxY9OrsOfbfd4lKH-B9cnhZ0LGRGnv18jqyyc0UT1B7wSwTtk1iWz2aRdfrESX2k62K3hJWKj7sIVHbdJDWib0oNVA4TYcXqHbxLkIOJecGWhSO6fxxxkKZAxrWlq6pCHFJECwDWmY9qsU9TiRSLr3CCHbwm6-kkVg-KVVjLqX-A2JG0jQNTHFhfgVzYtE3qutrLDrpaw-UGZ6IlhvWr9QLwf7jE4SgPYk8Yv61VXmh8oYAj96UYy__DQA1-AdTSBlVIxVbjbnsIcMbpqdpVqqo1Ngd825UjoHApwlLV4bw6Z5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">واکنش اسپید به گل آمریکا خداست
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/92492" target="_blank">📅 04:52 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92491">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">آمریکا ول کن پاراگوئه نیست و داره فشار میاره.</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/92491" target="_blank">📅 04:44 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92490">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a08dc037d6.mp4?token=UQZScxMgAMAHC78bfcgi_xUZQK-lS1NU0bfbXXjelYdYnChXGQHZcSBSpOC9ZskgnqQE_AGo21CdoNM08jf86JK3AKc4eN3lMTGKqHO61UmaRcniIs16K6yu7q3NUu6xpGdOHts0ZP2CRlm5dKynycj2a023fO5dU-rzYTdsIKIZzMH49rjlVF6uw6kXENGKpw6wRCrraCk9jJjwgW-RHxW4tY8D8FLrnoDl16LvRiEQ-WMv_Q-_mbH-8_z2UZ-r4zuoorVOibyzvHDWStuKns2EnBBHEeK3l2IC7krhvRF9QN7iamAqXF-Y5xxNr0AbvzGMFa5mwnZeKePZ6cLpuw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a08dc037d6.mp4?token=UQZScxMgAMAHC78bfcgi_xUZQK-lS1NU0bfbXXjelYdYnChXGQHZcSBSpOC9ZskgnqQE_AGo21CdoNM08jf86JK3AKc4eN3lMTGKqHO61UmaRcniIs16K6yu7q3NUu6xpGdOHts0ZP2CRlm5dKynycj2a023fO5dU-rzYTdsIKIZzMH49rjlVF6uw6kXENGKpw6wRCrraCk9jJjwgW-RHxW4tY8D8FLrnoDl16LvRiEQ-WMv_Q-_mbH-8_z2UZ-r4zuoorVOibyzvHDWStuKns2EnBBHEeK3l2IC7krhvRF9QN7iamAqXF-Y5xxNr0AbvzGMFa5mwnZeKePZ6cLpuw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
گل اول آمریکا به پاراگوئه در دقیقه 7
حرکت سکسی پولیشیچ
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/92490" target="_blank">📅 04:43 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92489">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">گل بخودی زدن
😂
😂</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/92489" target="_blank">📅 04:40 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92488">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">گللللل اول آمریکاااااا
⬛️
⬛️
⬛️
🇺🇸</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/92488" target="_blank">📅 04:40 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92487">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">خب بریم برا شروع بازی آمریکا - پاراگوئه
🔥</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/92487" target="_blank">📅 04:31 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92486">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/Y9z2DiQR6zr4UN0o4d0Xgl0TnALDpHkII-v11Laba6s92cmZaoygpaC0Y89h5EHRX37b8LnfNKDn12E8jX_jgF06cR6Y_dOv68Fg49Y6xJygKf9Iks1rwy-yKCf4TAgnLAqoBeZX_Tv2nk6hZkaF_DHpuB2z4Ra3ohyyHrwO9rkGlyuCEQHsKG4FZgc5uC6AOSkSBBT-PpoQW2udLi2noDZRGk2WPY1C3L2pyzf3oz1iNAdeU-5bIzPzfbK6NBQuznHd06A06-jX1idx-iAlkjIFfuGfvXg2nObZbGmkP4suWzQ5rBzyOFo3QhARma8LCYwsTsufmSO7W1momiio9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🏆
🔥
🔥
🔥
🔥
🔥
🔥
🔥
🔥
🏆
🏆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/92486" target="_blank">📅 04:31 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92485">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kZ-h_s5fw27tj4DhbpN_bPNCT_mGeGFxhhvE_B8Lt698vc6oWWJHEIZFSsvsh0IXuP3iz6-hR06eHmoZhPgMoa7ngu7s9mAttz0REhIxFBNh8kH6I8Z8y0z8UGYbXHqcpiJpwSxoe7Fz3rcJsluSZmoitBY6LV2RgXyznFdNWOrGwbBv36tp-rVkl-GzJp145YYYANxgtWWQl2cwo0q-zH5UIUuIpkU9OGgGBUNg4qe1mX5KxbkyjlsHEpUfY9KyIDUW6bOmnKLhukjeh1bsOIHCiH-tqQ-D5_P6pl1FJkkIhRlvdxR2stJMVBtZX9DQnnhe52TvCZn_apRjs-H-tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بکهام و تام‌کروز هم اومدن
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/92485" target="_blank">📅 04:25 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92484">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/otirbYn0Bn0NSv3AkTdXKtfsnpk7r5YrA415h_LtasEQfkctFlHBCYBNc3jgodk68fetuqW_kYO2kvXKUeb2v4fVC-TLZ_LxVa0nYqQvAEYyzzOotGIfgOm7xn9JqFQohbZrDe6RY-MBWn9lawIngdsCWmkTVcaLB5qb9oE5FNEeCT8XkVtPS-uNtRAmudOHwymk2o86J-ow1QXg6VtxFqQJtMgGIPg2oZ2I-d8RXKU8c1grXxlpIypgaCIDhb8fb_3APcmZztfR6EfEnstZ31Y_bh6BDeJUDWwDkpAliPtC5umwfoPnLCoEOu9AOQ7DyHTC3oYTh4Nn-Zz-A7K9_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
🇮🇷
حمل پرچم جمهوری‌اسلامی حین مراسم افتتاحیه امشب در آمریکا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/92484" target="_blank">📅 04:18 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92483">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🚨
🚨
🏆
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#فووووووری؛ فدراسیون فوتبال انگلیس به فیفا هشدار داده که اگر تا ۲۴ ساعت آینده اقلام دزدیده شده پیدا نشه، از حضور‌ در جام‌جهانی انصراف میده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/Futball180TV/92483" target="_blank">📅 04:15 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92482">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PRU3_Z4a0s4J9gQjIXNhL9Mv4RX83iFQNdy323hPowBEfcLYD2f3YsnOSCH40yOwfQ75wBCeChTXmdTh19pAgp9wcD1h7BE1lvqvmtVcSUdlSKeDRLUgwQrfHLcCVac7KLTxdXcSVN2RxHogmnbRd9YeSqxWLe6IWb9kJdejFcFd3w9ofCtVA08GwpRXQ9KnCfa4m2MnoAT3Uc59dk6FlgSpx0DMDTXoW0AWC6F4WorgZIUcypKfPop4vkHYldvvF2emFp6vg8H4zHEIRMG_e4G-Czevno_eJKf-AOkfxJTAv6gLsdws3SeQQLK8noOCxoQNLQ-NRYvtotGnvSBZ1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لیگ ملت‌های والیبال/ پایان ست دوم به سود ایران  ایران ۲ - ۰ آرژانتین
🇮🇷
۲۵ | ۲۵
🇦🇷
۲۳ | ۱۹
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/92482" target="_blank">📅 04:14 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92481">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🚨
🚨
🚨
‼️
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#فووووری؛ تجهیزات ضروری اعضای تیم‌ملی انگلیس شامل کفش و دارو و ... در محل‌ کمپ این تیم در آمریکا دزدیده شده
😐
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/92481" target="_blank">📅 04:12 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92480">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🚨
🚨
🚨
‼️
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#فووووری
؛ تجهیزات ضروری اعضای تیم‌ملی انگلیس شامل کفش و دارو و ... در محل‌ کمپ این تیم در آمریکا دزدیده شده
😐
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/92480" target="_blank">📅 04:09 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92479">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OCic5k_aOyrhUiFZQO7qgOuvA8unJybmEpgkAHk-aG9PRM1xoFsrXCrO0bIq8iBpfntsyvWuiaW1eaVZyJ1ORyzAjAmWVzSSyXAmLJullDlR9aiJSwcgldwmtl3pw_9epSfDVxfAoEdckXIcaa0LckcJdefjjZ_lPM8HWItUDWoWn3AiLh1698SK2SuJ-JFPQathcDZurWDHNZQgdTsRPNT6ruqzie-7WDVhfwf8G14MZpyWUITV7i4PLBoDvTqr5QMXWThYTGTjMyz37qxSk6mkmPH1R4kNk1c7kZBZ9PzV2GKJhlBUX2UAW991QkquhXbjjrrTkOlgMmgqBMRGmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
🏆
🇩🇪
مجریان تلویزیون آلمان در جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/92479" target="_blank">📅 04:01 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92478">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UyJTAf7b4gUH2RO6pu8ppltCGniGmQKs-p2AfFCoAuBhqq7H55HzqZpQP9DSJ6krmvEwRPMsVWB14_bEYF7ry_1cdpZFccCuWIyw97j4eXr6LGzBGn8tXXJo-JDeqZv0026nqjtqhkvqz_9hTWju3lmIRjFSm5_wrYmhSqRImByrpklqomHonnPRXbGtrCepdAbWubf8y9z9CBXqUaUUW06v68TyCMW_EX84RNEypCNn4I9vXyYNJHDtO6Iq0aUIy4zc8YcOhdarzQcBlGihHi2r7i65RfoUtcrE0dRsMFMFg2H_e1sDACQXnrJjGsfEq6Z6z15uhQUEBs3xYugCLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
اسطوره کارلوس پویول در ورزشگاه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/92478" target="_blank">📅 03:50 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92477">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JfpJunK1y_LTR2rQ9bfmf2q4y-rYTgq5ZqljYaWpc0MaL-P_G6C6TdTJhyxSMucI-3_QjnjIXVtAoVzFblt_cWEv9zYvfz445KNRG48_V3pINBnS9VENg_tEh8k9YkdsVAfq7eFjWWCR68wAtuf4ezXYfqyUnB8otTusjSOFHJyRhfyLbGU5zBdVkcOxCvwvEvEtT0hLVplrBSetYKm7MUgFHSnUdOzAbOH9pUdndPXyOlkAEBIM0UQT4VFIHb2cGfHpFkWHGhptUFEv3zyefTh0X46EONsOs7BZYyHkpv06LkwwexUENIatS8HU1A4GTsz4SN8zjA3xh-hJRTePzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاپیتان‌آمریکا هم به استادیوم اومده
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/92477" target="_blank">📅 03:45 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92476">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b291ed502d.mp4?token=eyd_C45yTXO5vYfjv6_IUzhLHBeSKDohMFnFc3EySBlzqjPb7m3av_qHDn_HvUQcTlcKl7oYTpBPLP2opQ8gbkpjHaDGcTEKYuvnojcKGUmizxMiZVCi6emQ3t_jZI_mp0As6uXy-3YJmBCpjRQbRa32EL3Ojq9zGTYtTiZ_1j2WrMGRr5KVozEvUc4sYDLHhkxPMcsGwsqWDnfgg_wLYG1XaCfjy61afJOAwOw7mby1FO6jE4Bh8ST5XWP6-bG-Oj281PpKd88xNtRvGqKuVAfcDYNdxRY2Qq-6q_HBCTBlkw_AaF8oUkiZ9qHLtaiUaup877HteICOucFJB9v9CA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b291ed502d.mp4?token=eyd_C45yTXO5vYfjv6_IUzhLHBeSKDohMFnFc3EySBlzqjPb7m3av_qHDn_HvUQcTlcKl7oYTpBPLP2opQ8gbkpjHaDGcTEKYuvnojcKGUmizxMiZVCi6emQ3t_jZI_mp0As6uXy-3YJmBCpjRQbRa32EL3Ojq9zGTYtTiZ_1j2WrMGRr5KVozEvUc4sYDLHhkxPMcsGwsqWDnfgg_wLYG1XaCfjy61afJOAwOw7mby1FO6jE4Bh8ST5XWP6-bG-Oj281PpKd88xNtRvGqKuVAfcDYNdxRY2Qq-6q_HBCTBlkw_AaF8oUkiZ9qHLtaiUaup877HteICOucFJB9v9CA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🏆
اجرای دو نفره بانو لیسا با آنیتا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/92476" target="_blank">📅 03:40 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92473">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AqCMx1XD5fREt6t_0ddYQz_leQNA_PiT4X9qjh6bx0DdbDXK-Oij9lrAfdH2wNPRJiSJfCrDSzUD-4-pj9146_1G5Lof30NMU45BNt4JeXhKMPXZExLZ-PjRzLrdVB9vyEStXaha8YyGx38VTZsnE_4uOpoOvEupO-EPOuvYAFE0aJXuj9VxC3TWSSG1RiFN8XyqRkSuTCm7L2IlpL7MocWFvTESdRXKKh0ZdexiRQkbPZQ4BhFChM4Pvvb_aMENe3-u_RRU_olKOzuFosK7QyBcrgpq2Ix2itOkonS66tFWil5HUinjVD8ni3yqZ_Svix_dnz-J5Uy2p_RnRUsHMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rAgdLV_w93lRzNnvOW6wd1DLyvdW2EmdYi6ZVWMtnXJ7WQ1uk5CKs--jG_Qwatrk02lEubO4cvLqClgc17uTsHDoeJbqaj_sUnZHKCNK6ZywhiloXPTblY3axMr5GW_vUsLVzNsdcpBO3FMksmQlPrlecspVD2WVxJWtKkVUuh8IpIoQ6rdiCbyt53NDY4asGCoMGq6MlULHWazPj0qYygOR372AXyaXbTGSydcUT-7zRcBqJohEXkN2vSS1WNuzQXO95U1h9sRHtQwv-kDrRH6nfKpJZzqK6Ng_WnmKct1RC4BjlVcWMLcZpeW6TQheyQDgYkp3xH6dhaVkHx5ehA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sCn-Lair0JG2JXAXOVM21mv9nnAm7SxECO6vr3XSm6DO6lxWjbLSErYrLCRHAy-cHfejrGds0c0rs4mfmDBtWh2kV_8-KItMneps-tg_1qrJGrCBH70UNYxiRsgA-_Ho8dt42KQTnvSytzEjdQsQdjr8qNdkBSCecaQNaOK__YwIytzQD4N4pz7Cbj-Gr8MnKm3r5BXkS0x8BxEsTWp1pzxf7T24uczOQQUNHoaByeoJ-4MzXR4UdprrBpIHK9BcVfggW12mrL0fNJiC3Ex3lfq6DXmnYCkE_gQWFvAvK3fwHeXir9D54HM9Ww9A54Kb5MR6-ajdOE9bdBek9rGbdQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🏆
تصاويري ‌زیبا از مراسم افتتاحیه جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/92473" target="_blank">📅 03:38 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92472">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">لیگ ملت‌های والیبال/ پایان ست اول به سود ایران  ایران ۱ - ۰ آرژانتین
🇮🇷
۲۵
🇦🇷
۲۳
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/92472" target="_blank">📅 03:32 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92471">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🚨
🔥
🏆
🇺🇸
اجرای کامل بانو لیسا برای افتتاحیه جام‌ جهانی 2026 آمریکا.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/92471" target="_blank">📅 03:30 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92470">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">بخشی از اجرای بانو لیزا تو مراسم افتتاحیه امشب
😍
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/92470" target="_blank">📅 03:28 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92469">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0252ecab75.mp4?token=BOk9rw1OhP5N3pdPz_hSfOig8hDmMjYz5GtQww-fU7ILk8ibdOzqc40Sqpu7Pp7fxH3NWnMXw7O9OxbR9mdANJtv1SW15XJybf13AyLEI5B-9QSLTMZZSAW2p1UbmYIGjMQKu_1J3rpIKP6_7V4M0w-dBAhvghdERCzS8aEA0n65JHrZw0u78XdhsIuHp36pXlhOWxgIsoxeXopMIwqRGh1V3Lr0pxK_ihKBCKVpZXXC1u1fqitYADLLJQfqojSzUHEmXhiw6bTtlwfn_C7sC_hYTpcBnjWlWMKkP2TCJoLMBf7RLnjh6ImepaqR_b6_Zqrw8uhBpftFS5zmuG-QoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0252ecab75.mp4?token=BOk9rw1OhP5N3pdPz_hSfOig8hDmMjYz5GtQww-fU7ILk8ibdOzqc40Sqpu7Pp7fxH3NWnMXw7O9OxbR9mdANJtv1SW15XJybf13AyLEI5B-9QSLTMZZSAW2p1UbmYIGjMQKu_1J3rpIKP6_7V4M0w-dBAhvghdERCzS8aEA0n65JHrZw0u78XdhsIuHp36pXlhOWxgIsoxeXopMIwqRGh1V3Lr0pxK_ihKBCKVpZXXC1u1fqitYADLLJQfqojSzUHEmXhiw6bTtlwfn_C7sC_hYTpcBnjWlWMKkP2TCJoLMBf7RLnjh6ImepaqR_b6_Zqrw8uhBpftFS5zmuG-QoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بخشی از اجرای بانو لیزا تو مراسم افتتاحیه امشب
😍
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/92469" target="_blank">📅 03:24 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92468">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vkzygK9GThNJ_JV8FkltBA9DrPxmB5efcOteGX53XXSZY96De7bT1kvDXTxYMbNBMMPrkNrvAaM2OFyXYtDxYHo8XmtBjZD-UgWdaUY7cGV9gYS8uh_yukMQoMxFCBzRTd3C6PR5AdeY2q1XdIbphwqiW8wJ27E6cJxpdHmERppMrjJHh2Cw3RPvWiHIS5CkvpxDLX123R_m2o1fx7m8jVST5oy9FbtSeOFmWAKcJtuPGpIvbvGzchckQdmL_WnZUWYBrcBJED3j9Y4RBXfwgkjOT-KcUfL20xI8WmDAriRl5KdjezHtP1VrqlefmPy4vACjtMUrBpQIjrwElAhoAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ورزشگاه کیپ‌کیپههههههه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/92468" target="_blank">📅 03:24 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92466">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mE8bc5FaRlzuLV1Vobp2pwZR_KZ7dwTkagsoz5LY5dTcZQ45TbgNT5CnMrp2lW2OkA8NsmqNaSKBy3idwcv_gbPa_FeVnYvZW3M_nW-BbkETf5m7IHNCbDlWv9W_P8HDAZD-DM8CMeLoG8V7-yA98LVAM7ACKeNnwAJJu-VczdEAkX-zCxCt5ZwRAQ39cBRVUtgn9b8oPb9icy0-4eV2YMpQjNl0UP-HasVDh1lXQ2vKo1yqgXGeIb8L8Ugvq84E-ngztOCKtmUYOELrocas9WXq5t2b_mVAom0UI5mNRYWcqi1N2nCNs5Y7TYe3GgcGzSWPiuAQzcdLEFRVxn7pvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
🔥
بانو لیزا درحال اجرا در مراسم امشب
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/92466" target="_blank">📅 03:21 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92465">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b_l8eASAgqLWv7wp_k2EvpxQASbEIFN87Poq6ZJpyxmXeBtKuIUuOjeHS534yhhGq399QlYJ77vgK1s67uN-VaAOPLVxhSWoB0Ge4egV3PtNjEWtuFFbOq6J5f5KWMYCQ9-YPAM9ld2yjLY6pHcZcJRzyokYjsfOQ7kmerXmDU3VaZti9-Ekkr1NWlNbMdoSkyr8PonYlhwu7cGt7QVJ8ddpyn7NnexK3peSE3cG8xZHyoSjRfGvWXZKefVDCpqCsrecBSv4FHcfGRWrJo8ukSSSjUE4a7ol-aEFbTbKBPOworuxAM_e3K_LGEMT5N5qYyqxXO7Ru3jttEUBssKvHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
🇺🇸
ترکیب آمریکا مقابل پاراگوئه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/92465" target="_blank">📅 03:16 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92464">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a643a87a13.mp4?token=QXkz_VEqRaq59yQQ_oz7gh-wGw0El_8Ca1N5H3Kk9X5j2yj8kFC4dxs_nVR0JpIhosnWrEYgMJF2EUzWPhjblp1LLe5hrkD0I9eNipOLjGBFPE3nFU7jlio0aX17zGMEpZ8LPUfp-XUbB_U4mPj08bJn_GOn3YKoDS_tTAcHGPjmzFmGg3-Ub0XvCXzJkms_GjdyMXdyY0Wwvm5uGR2oAxZgWHH535eU6cHE-NhobHnMUh5FqAuifZCj2nYIM86pmUzO9tK-0fSVKPRCLy5bY47x7fTdX6E-wOLRTLlnXu1mE7-RQJWflX043UQbB35zkxpGee1Q1ar64Hoi_S_Me0YNn6BuU1W-hmTpM3zFs5Z_O5n-2oD6RzXpTzyKVmZFUjOG8OyWmtN0ZETtvOSoy5waBYCHTAK-gAhgFiBcwMKonMRX00pus9rkwZAM6r3oOUK38w2mNy6gHHVM_Z3LBRLRNPFPGd-FlCuMkTEP1Nka9lSXjUGYXzZCDHskrE6U5i6gSwbJh3pn_MdpAFMomv9dF6TNFdRRSRE9GSj3181unQLbmiGcsHcnCouYbbZxr8Y6e3ejoQpm9xwf0tuhsSQAcboS7Hbhxg3T5X-gT9H9S6t62Zj-hLxRpjWt9Kel_zO556PhULp1WdkjNnDNh8pgUhtASrtShKwn3AH0Fng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a643a87a13.mp4?token=QXkz_VEqRaq59yQQ_oz7gh-wGw0El_8Ca1N5H3Kk9X5j2yj8kFC4dxs_nVR0JpIhosnWrEYgMJF2EUzWPhjblp1LLe5hrkD0I9eNipOLjGBFPE3nFU7jlio0aX17zGMEpZ8LPUfp-XUbB_U4mPj08bJn_GOn3YKoDS_tTAcHGPjmzFmGg3-Ub0XvCXzJkms_GjdyMXdyY0Wwvm5uGR2oAxZgWHH535eU6cHE-NhobHnMUh5FqAuifZCj2nYIM86pmUzO9tK-0fSVKPRCLy5bY47x7fTdX6E-wOLRTLlnXu1mE7-RQJWflX043UQbB35zkxpGee1Q1ar64Hoi_S_Me0YNn6BuU1W-hmTpM3zFs5Z_O5n-2oD6RzXpTzyKVmZFUjOG8OyWmtN0ZETtvOSoy5waBYCHTAK-gAhgFiBcwMKonMRX00pus9rkwZAM6r3oOUK38w2mNy6gHHVM_Z3LBRLRNPFPGd-FlCuMkTEP1Nka9lSXjUGYXzZCDHskrE6U5i6gSwbJh3pn_MdpAFMomv9dF6TNFdRRSRE9GSj3181unQLbmiGcsHcnCouYbbZxr8Y6e3ejoQpm9xwf0tuhsSQAcboS7Hbhxg3T5X-gT9H9S6t62Zj-hLxRpjWt9Kel_zO556PhULp1WdkjNnDNh8pgUhtASrtShKwn3AH0Fng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
جو هالیوودی اطراف استادیوم محل‌برگزاری
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/92464" target="_blank">📅 03:14 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92463">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JfJzUTHzvj31OTxiHeCKgbBNFw-vEUTiQidEIvERyMiuq6q9-zp8X_HkrEOaZ9qsmYCSEjVJxNeXfFo4G3DTKbRVGyc9ObBMaBdfLv6m0EkPb2NPC6EQjwD_zizaBdrsLb7PvZ39qUwit4pZU9W0tyMvEYF544p1b86a3I9uvjlzoWT9lOWFHk75R0bZIh4iCmzK0LBOGtAHhzk6KCbOdEpbwXiu0gOMujq8kHHot3hxgkCCP_1Dr0i23rBRz6vNrzqHIFRyE2N0G-ENkW0p0Ccrm0GFJN0wkDpu3AX4PXIyOJ5CUOamukyDx3k83isi7il5HJ0h1aJkUMfj0lIQSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
🇺🇸
ترکیب آمریکا مقابل پاراگوئه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/92463" target="_blank">📅 03:13 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92462">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dd835b923e.mp4?token=l0Kx548jTr4G--D0iY3kcpB8Mr6jAbY_V_IqfX89U4dhKaH21Iw51B7evQ9d8ulCppEwCxEnhGWrv05jSbcAAMzDdiupmOr-py8xEjVvDGzB4WoGv3_7wR7BMq-2m83ig83QJ5YMXTkCcGGTXMhpO2fsrcJtYgC9sueD7i7T3YD-OQBDGEQwfVqO9f6MHvvBgl3NmmRbNSGcbWnwaukXnyVZ02dukD_H94P-VSlulHcGMTCd1u4H2WqpZ03Q9hLFJVmcH4evQcpaW94N8UGCPMvUHs6WBpR-w89js9Ks04J5C9e-aAZw4xLGe27bkQaY0MUKyjIjqPp_pwNSuA3A-jp1pYmgtdnUjVRCu84RYbFr9YKpcPUrHKRGunHvl7wovtLr1cM3S1tgFADFR2rrZhThLW5DNm0RfjN-XFm_INUjkgbFsdQSZKJw1AhmLrUfvWZ-yTkPePXSGq71W41xdtpNKr6tHAHXcD62LGCiEXUEg7jSy2sw0RwA__wnYbXhaq9MZuogcYY_bt--s0wDpOOaubs4vAavcvvjhtlBbT0sFh4bJaWlvh78R9_QuBc8IHi8vVa3T79PdBvCvrzWHC0G8p6tRlCP3QxMTPIMkPVyWXjPlgn6Wx2gImFotl7N22D4KTkZE3Hx3mJoGSJtMKEOD1XzfJtHLFlkdjTV8LE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dd835b923e.mp4?token=l0Kx548jTr4G--D0iY3kcpB8Mr6jAbY_V_IqfX89U4dhKaH21Iw51B7evQ9d8ulCppEwCxEnhGWrv05jSbcAAMzDdiupmOr-py8xEjVvDGzB4WoGv3_7wR7BMq-2m83ig83QJ5YMXTkCcGGTXMhpO2fsrcJtYgC9sueD7i7T3YD-OQBDGEQwfVqO9f6MHvvBgl3NmmRbNSGcbWnwaukXnyVZ02dukD_H94P-VSlulHcGMTCd1u4H2WqpZ03Q9hLFJVmcH4evQcpaW94N8UGCPMvUHs6WBpR-w89js9Ks04J5C9e-aAZw4xLGe27bkQaY0MUKyjIjqPp_pwNSuA3A-jp1pYmgtdnUjVRCu84RYbFr9YKpcPUrHKRGunHvl7wovtLr1cM3S1tgFADFR2rrZhThLW5DNm0RfjN-XFm_INUjkgbFsdQSZKJw1AhmLrUfvWZ-yTkPePXSGq71W41xdtpNKr6tHAHXcD62LGCiEXUEg7jSy2sw0RwA__wnYbXhaq9MZuogcYY_bt--s0wDpOOaubs4vAavcvvjhtlBbT0sFh4bJaWlvh78R9_QuBc8IHi8vVa3T79PdBvCvrzWHC0G8p6tRlCP3QxMTPIMkPVyWXjPlgn6Wx2gImFotl7N22D4KTkZE3Hx3mJoGSJtMKEOD1XzfJtHLFlkdjTV8LE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🏆
هم‌اکنون از اطراف استادیوم دیدار امشب
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/92462" target="_blank">📅 03:11 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92461">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bBm7jkU_SPEKUuEf3R4xIaHPZC10EgTaWEVgfE7vbPwfXTLyyHNoIUJAJ_hbPZA40xFYCQyRqv59lAbGYRmRGkR9MdNbsYDr7EmaZsiEnkiageVTIDr7S9RReRLEb-0-0_wuQO23dhyEOw7Osezz4zIn1IZKu0LVcbsipQkeOlLmteKxvyvmiBK5KKKcmrwWDJuYPWM_jCDUcNgXVghJr2jc9PTeNQN7iVp4O-bVJCYevEC6Cx0Zt6f4vNUgLY7lVEIvHSyZcleuapKQHEc1mrBFkZEp4gZDbZFp1VqfVRuTOtrFaP9wfBzThNiABqGttuIt06B_1eUMtXd8UjhfdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
هم‌اکنون استادیوم محل دیدار آمریکا و پاراگوئه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/92461" target="_blank">📅 03:09 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92459">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">لیگ ملت‌های والیبال/ پایان ست اول به سود ایران
ایران ۱ - ۰ آرژانتین
🇮🇷
۲۵
🇦🇷
۲۳
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/92459" target="_blank">📅 03:02 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92458">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hb3PB6Y_CiiTNIdiR-QYy9m3icI3F4niiL1h6G2XAAwEr6ZX4klU2MBjZ8OWU9kqfJnmbBCW6DmarikHLY4P4t4oeZU5YAIMxO7LUKeDLfPoJwz9YoQFqQf9eNJdvQOEPqY78gUoKPA223UDoBnMbl8_HSZPAitawIuZyJxAnoR9wPbUQ0oKKly845h8wnBWVgwbyH0los2rtn3zVfCCXzi6QF7s8anwCOO0ZsC94Wiz_Yrtrz6jY3ikxCHsCOTWemEylCq0Rw2wlAElI0Lxmw4gtwBRIoOMRtr8mcAit-gvRwitI78yP6ammnWP2NnfP_mJmuOYvIxIFPA2I15ZbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🇧🇷
ترکیب احتمالی برزیل مقابل مراکش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/92458" target="_blank">📅 02:58 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92457">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SJZGwMK-VLuSAvmOoDro_R1TDYnl8jyZSNUWSQY7FuRFlcE43iwc4ec3lJ4tdQ24XUba5XNkbBVoLhKYbqNSZgSeYOFZgFmiRKit3iRHSVlm7lVkhwbLSOMywH2xfKTTUr0GW8ank1EUpiG9nQ3MT6FYh3SWnkkxF_1HkU_5cxqU0RvqLVp8kCEojFd7CLIe8VsMCQmuBSA8j_R2Xd7KHmTdWls9brt3UME_MLIz0qo9Zk72CXlrki3y5x4iayEGlVibSNMLwx8Q03VUCkVOSwqwvVUVW-N3MTdO1m57tSbvYPWkN2mBG1FFpp6wbanNPfgOuoY4kqKKa4hUjQrcWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤣
🤣
رسانه‌های خارجی از قلعه‌نویی چی ساختن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/92457" target="_blank">📅 02:50 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92456">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bea6577b63.mp4?token=nmk9L7GeXZRForGMGykzlMRioWhID6tQAhDydkrr9oaMoUTEpdE51kEn1fd_vT6JjK3O_4p00KGNb9yal6tSyAtkZ-MLC90Rz8ktWJvkLBm1NbEqpMUYKgXibRlQPDIcblfVxeNmiu_I_dtUP9BcwJNC7fePAKIxB9dFIfoBPBtVKHWzskU0D3JF7Mvx0VGlsweNoyI9E5ee-A2h-LNOEtIRT7nOFyk7LtWwR20ZsToVnuwfV5jfke6tV_oW618BcqJd3uFkaPEbOEHTiBwJCuJWR1yfjH2bo-9Sl3_p_Ih0Zs4ZW8XMFn0Buls9pNH-pak2sUjzGBS-ZYDcq3NUZYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bea6577b63.mp4?token=nmk9L7GeXZRForGMGykzlMRioWhID6tQAhDydkrr9oaMoUTEpdE51kEn1fd_vT6JjK3O_4p00KGNb9yal6tSyAtkZ-MLC90Rz8ktWJvkLBm1NbEqpMUYKgXibRlQPDIcblfVxeNmiu_I_dtUP9BcwJNC7fePAKIxB9dFIfoBPBtVKHWzskU0D3JF7Mvx0VGlsweNoyI9E5ee-A2h-LNOEtIRT7nOFyk7LtWwR20ZsToVnuwfV5jfke6tV_oW618BcqJd3uFkaPEbOEHTiBwJCuJWR1yfjH2bo-9Sl3_p_Ih0Zs4ZW8XMFn0Buls9pNH-pak2sUjzGBS-ZYDcq3NUZYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🏆
#فووووووری
؛ خبرگزاری‌های مکزیک: امروز نزدیک محل کمپ تیم‌ فوتبال جمهوری اسلامی یه جسد پیدا شده و پلیس درحال تحقیق درباره دلایل این قتل هست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/Futball180TV/92456" target="_blank">📅 02:32 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92455">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🚨
🚨
🚨
#فوریییی از رومانو:  نیمار بازی اول برزیل مقابل مراکش رو از دست داد
‼️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/92455" target="_blank">📅 02:26 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92454">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W5flXrhGj1FZ3FxgE8ds9QLSR6boRKOHKVrTF0gHsbKMfdeHcw5i45jnp49g4ZWG3Jjx-DFXJcneBw_ukY9XjC-NgxEUZPxbGBmdUKX55a2D0QlD8ksePcRXx2IGYlaeOqq9xnUFmnXGekK02oFSrGyxqk6N9c66Z7dUX4FKQpJhSYBXW9W8X-IU9KtIYFBPwkakxPaSprygcWW3noTzHsaOliKqCD2mnCA1SMJ212aum7jOmh5SZUVtpLs6M3-xbnsP6UxMTug4_VwbBxunDQQRTHjR0dtSYKBnxywZ-533V_-anRn_ENWyar8aHTk8d-OGqNfubMAUrow9-UtM7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
مادر دختر پاراگوئه‌ای آماده بازی افتتاحیه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/Futball180TV/92454" target="_blank">📅 02:26 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92453">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🚨
از طرف اتحادیه پسرا به دختران مملکت:
دخترخانومای ناز و کیوت
🎀
ما نوکر شما هم هستیم ولی باتوجه به فرا رسیدن جام جهانی و لیگ ملت‌های والیبال، از شما عزیزان تقاضا میشه در راستای حفظ آرامش روانی، حفظ تمرکز این حقیر و جلوگیری از هرگونه دعوا و قطع‌رابطه نهایت همکاری رو به‌ عمل آورید و از انجام موارد زیر خودداری نمایید:
🙏🏻
🙏🏻
❗️
پرسیدن سوالِ «من یا فوتبال؟»
❗️
شروعِ غیبت با پیامِ «اون خرابه رو
یادته؟؟»
❗️
ارسال پیام «بهم زنگ بزن» از دقیقه 60 به بعد بازی
❗️
قهرهای ناگهانی همزمان با ضربات پنالتی
❗️
درخواست بیرون رفتن دقیقا ۲ دقیقه قبل از شروع بازی
❗️
بلاک کردن به‌دلیل« دیر سین زدن» در وسط بازی
❗️
ارسال هرگونه عکس« مدل‌مو،مدل ناخن» و انتظار ذوق در وسط بازی
بدیهی است پس از پایان تورنمنت، تمامی ما مجدداً به چرخه عاطفی عادی کشور و بوجی‌موجی کردن شما بازخواهیم گشت.
#کپی
شما هم میتونید به همسران و دوستانتون این متنو کپی کنید بفرستید یا فوروارد کنید من که کردم تموم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/Futball180TV/92453" target="_blank">📅 02:15 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92452">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lemfKIYM4gM-k4rx59oq-K__djboogNINLHV7skQMX19v7jqrFb8g0AAxqLSt6WVbZNZVXkVqoJSkSCfXs5ZdUwco3hVHLeU6YeVrQI48HVnyU7MyE73hbE-ry8yzqBGbgaw9uwHd8qZ7p7M3WMUTb7eyMD2EgtG0OeDvJyCClQ3JlFCmLwIIbBMCx0YZsPmbN36UsPKH83PMKYSWoCv7NGTlkiGf5uJ75no-Nvqbd5__rw_tLNa0hcgbhtNVE5_MuNhwwiZvlhy_S7rrCU-r3AL0qX8SUfvpZvsuArNx0U5jAYpTNWGqZTzE0IHa3Wr3B9h94nb4BkaruOrGWhMtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😀
پست‌جدید نیمار درحال عشق‌بازی با زنش تو آمریکا با کپشن: خیلی دوست‌دارم بیب
😊
😍
همینکارو میکنه که نصف سال مصدومه
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/Futball180TV/92452" target="_blank">📅 02:02 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92451">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cOSRbWc0FyTzAbUArx4HF-EEua9MjjXJlQB9BGHKcC5_Vc82tJL8hV2dki9LwOzbss-M00jLB4u_Iik6HidnHDg_Cm27Hvo4Z5FbP1XeM4h2zT1WUhZYadm28ZfDt4Z1HZQja603txkKj1MYxT5MXG6cu1vJAg5ESM0Gt-BsT1ovt9G0gvRs69KFw3mDcgTbXhj80eN4Kn_iu43c4xGdPc_ngC2PEDnfh2D7XK_XKGD8FFIau-_J38lPFHa-Wqdd8K8qKx199Gc3AZTTk5vYHNEWqBIXoiRIx0bdI9qcVaYP1MhtcuI9EmFcJ615kGpWEcgDjN2aa7NC-0sDWxkeQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
#فوریییی
از رومانو:
نیمار بازی اول برزیل مقابل مراکش رو از دست داد
‼️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/Futball180TV/92451" target="_blank">📅 01:50 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92450">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BGZpa4b-2U4GjKoED3ziFrcspMIDx9Vk6d5ktUFg43pO9js2K9V9dmxwKP07Z_vZmTW4t1Mcq7LQC9RQZvIDRlYZ3blDx_VkCbjZBvoBJ31ifE3NiWTtpe3X1CPAt0CybMgDZnEw7lpOsQJ85Oc_avQq-Xew38ChfCtuCWhIZPnooQiVUnJtHKdB5p5bJ-KBORCAuhuFBVGnMVxt3YSYZhlEWKJEAc_XcyheroD7RpY2YA_LcNpgG4Q4wwKYue-GvMjMMdsTCBnyMXFEYh_AvnrEJSVOUhRdIC_yvN-LO9RGan5yfX8U2dX8TBbZAhGz105lHJ2_5QxL6fIaQejTVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
زنده از ورزشگاه بازی آمریکا و پاراگوئه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/Futball180TV/92450" target="_blank">📅 01:49 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92449">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SC0aoB_-t72hHtX4ZGlaGFO8pVbkSIOLxKCpxTiQbcjF1YJFYZZMMoYD-sw4WI7C469oeTb9csQTF2-2byyg77nN7GZ9fydMPNwWxtFS0TyWY0f-yspcQlYFKsksCTvSzj3xXWe-moT4H_kcQK2UkrUZ8ReSLCDy68Bv5TrhOH-B9-5sMvayZ8mU1PcDUpD47M1nkwQodledpGkjlmBPNQ_GV5bhJ0w-9C-gNOM1rVBOFtPcnoxkF7SIfughwL99Jv_s0iHC0F8Ulx_HrYhowxE-Uosy92jX6CMV8naS49TmGs8Bfifo-bHZN3f5_RWO_nJcDD_cMzEZPbC2dliGCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
ترکیب تیم‌ملی والیبال مقابل آرژانتین؛ ساعت ۲:۳۰
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/Futball180TV/92449" target="_blank">📅 01:46 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92448">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ru_ROlI68Ommx85Kr9cM32RoRI_5W161m4kUWmAkkQ2RJp2KmqUk1KgSjSIzxjQ1DPUz1DY8S3LRrqb2nEopEuTUWBpq5w3huszZ09HKoEps5S8N0UQ-HiAaaqkENOZdPtlJ1baUKpFKN1JIe_ePCpJ5B34MO3iKHLY0bx_S5_vTSzxi-XVrr3w8Sj0CSBWnZvESFBbA_-25kX8ILTEoSr0YaOw4r_1EyeWawJBK2o1ruNzl6gnCEwilldBHxPgk648nVoNw0EVBuaveHJfTeISgKiidZrIOOh7Leu27GZsGmCW9pTi07jSK3_LimIgAlXlMn_TozsEA6oLsoPh3EQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇷🇺
🇷🇺
#فووووووری
؛ رسانه‌های روسیه گزارش دادند که پوتین به مسئولان فوتبالی کشورش دستور داده که تورنمت جدیدی با حضور برخی از تیم‌های حذف شده از جام‌جهانی و تیم‌هایی که شرایط سیاسی خوبی در جهان ندارن طراحی کنه تا به نوعی تحریم فیفا و اروپا علیه روسیه در بخش ورزش به نوعی خنثی بشه!!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/Futball180TV/92448" target="_blank">📅 01:40 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92447">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OFWG_uagNvfCJR7dLoJ3e7hVz6NSufoLsQTay4KEwWXlENaKF0M39n2Xdl_9otnKXa1tv0-g3t6JvufUjtXxeFfjSHrsOAwkdoHBAFzSWjaE5iVPVqGfVKKRL8I_FRRjUhxiPRF8BAa2yiuq8N-QfCqEU5LTue2hwjRZsYOC22GYyAvOtageN0wahEVZFPQyOJXec5bfnXUIT_gXSQ8iR2cmA6vEQlcDM7y6ARtawtnPSnPOgw56sSIIV6s_O_YfGRTh4Yl8LWs93wHwyosZMP-JBrOvPwbnnRFzjmo3H6Vt7W-5NPtRN7jquOjBaK4SOP59aFYjIhz8oP74MqQxHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
هواداران پاراگوئه در آستانه بازی با آمریکا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/Futball180TV/92447" target="_blank">📅 01:35 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92446">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y0m2MGf2g_hvN111-DBTE-3zv6vR3v9bZm_gWEsuF8_XXBxU3ycjLuA_i4qfmUJXkSvEkyhwSkOT9dIlkPGMR_F_BW89D5f8onafhaB4tf6MQ4agMSo20pgm25khnIw3XuT17nHFun3dy_vTbwss7UDKT6KgrkhUc18KeznENPhS8AGxZ7VF_Fp6ssu9s0cliPCM3gXNBlsNmjBfsPIfoB4QI6sQFCfQmWx7ttBQhIdS0KEDlCNBbYCBekbFOXC1HBlUzXb7bCzUNgNi5V658lNZivDu5yt4VN46yLQxdlYvsT2k33VdE9XuqajOgixzaU64hAmmTtPzolg57nQBhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇫🇷
#فوووووری
؛ دیمارزیو خبرنگار ایتالیایی: پاری‌سن‌ژرمن قصد داره در صورت درخشش فران‌تورس در جام‌جهانی، برای جذبش اقدام کنه. ظاهرا انریکه از سبک بازی هموطنش شدیدا راضیه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/Futball180TV/92446" target="_blank">📅 01:21 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92445">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/G0cdY06e1HYPaRsdnqEBspRwqqVcVJYqU2PIkSrCi-j7jJkJMuzBb_EyMu4Uac4jMTeTmQM3mKg07ijOYY3FHO2biHCFlsPx-xZX4kuF_XBtZUINLFvKykppDP8y51uM4qLbxYJNx8f8-nRAGSla_jrRYoEQlwOko8mIIEVpZhLnhk3xpbJCFoTf7cHJaJyutplNZsuzxET41xOGi2SjuEmc4Ids9NCsWnEBhjwtm56gFVRVtXxTNWI1bpbUUAY3uTijpkP7zkTmgu_oaeJmFrrfsgeLVDnulsJhS8okZLOIvdEb748WYMvMjkI2Qa7YmnhgGDDjlW64v80hCl4yRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کونی خان بهترین بازیکن بازی افتتاحیه کانادا شد
این چه اسمیه تو داری مرد
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/Futball180TV/92445" target="_blank">📅 01:19 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92444">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a9dd472ef5.mp4?token=hhByJDqNQNYeden1ss_0vCKbotlXx1KRFT5Aw_o2uSr3HvLcv90DOIHyD-LXMgxsaTc5VGy1D1EfwhPd3y-Wfq2ioGA8RboFhNGZOdppRF5MC70g3BYsORihqYx-F2aTbq5VAwLiMd9Ayx4CM7RIcZbfg1Lg9bT06i605iexPtAi7rAnpzUYgsBsGMX3vUS7J5HU5hRAw1iY6Ivb91nhdvmyHL_f3N9aFQHTfJ1Gi2Tec7aH505ZquRTa4C89GKIxNnz62Iy6l8S5XldFs8OHzr7BsrtyEOkvNyjEMHBOIgZhuDX7PgFdnmzdCbMubeMdX1siNXiXU8fmPJ3aOYX1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a9dd472ef5.mp4?token=hhByJDqNQNYeden1ss_0vCKbotlXx1KRFT5Aw_o2uSr3HvLcv90DOIHyD-LXMgxsaTc5VGy1D1EfwhPd3y-Wfq2ioGA8RboFhNGZOdppRF5MC70g3BYsORihqYx-F2aTbq5VAwLiMd9Ayx4CM7RIcZbfg1Lg9bT06i605iexPtAi7rAnpzUYgsBsGMX3vUS7J5HU5hRAw1iY6Ivb91nhdvmyHL_f3N9aFQHTfJ1Gi2Tec7aH505ZquRTa4C89GKIxNnz62Iy6l8S5XldFs8OHzr7BsrtyEOkvNyjEMHBOIgZhuDX7PgFdnmzdCbMubeMdX1siNXiXU8fmPJ3aOYX1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چرکی : شب اول تو امریکا یه دهه برام طول کشید تا صبح شه
ساعت 6، 6:20، 6:30، 6:40، 7، 8 و 9 از خواب بیدار شدم
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/Futball180TV/92444" target="_blank">📅 01:15 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92443">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9fa48a9b18.mp4?token=qGGIkZV0id9Xb6eh74cm2aWjkgsq-c7vvc8mr4hvB77x4RPDMhH8n9vgzQZzaQOhzPK_lON9b5ixTq1_yzrzQZlXJek03ALjc9jfJemuGhmH1FATtmOlIB49wViIB1ePJlyoDfw_GUT6BHZd14Z6kGTMosXSuBqrYy1HZ9tsBTXfJPrm8PY-ELPeWqrgMDp-G16zB2wJWuQzpoWAUyC2hjtBQVqcgtU9CUlOSq_Wt74mO3ihJZqAiGiArfPeAhhuNiMd0VCVcijmPzgrgGs2H9OFU8ksqoUF4kEaS_U_9dUfiyrufazZnPVHClCBLVuhLHnXwMOH-EMpiDNewzysCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9fa48a9b18.mp4?token=qGGIkZV0id9Xb6eh74cm2aWjkgsq-c7vvc8mr4hvB77x4RPDMhH8n9vgzQZzaQOhzPK_lON9b5ixTq1_yzrzQZlXJek03ALjc9jfJemuGhmH1FATtmOlIB49wViIB1ePJlyoDfw_GUT6BHZd14Z6kGTMosXSuBqrYy1HZ9tsBTXfJPrm8PY-ELPeWqrgMDp-G16zB2wJWuQzpoWAUyC2hjtBQVqcgtU9CUlOSq_Wt74mO3ihJZqAiGiArfPeAhhuNiMd0VCVcijmPzgrgGs2H9OFU8ksqoUF4kEaS_U_9dUfiyrufazZnPVHClCBLVuhLHnXwMOH-EMpiDNewzysCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
زندان هم زندانای قدیم؛ یکی از اعضای تیم تتلو یه ویدیو منتشر کرده و گفته که آقا امیر(
😂
) از پشت میله‌های زندان باهام تماس میگرفته تا موزیکشو براش تنظیم کنم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/Futball180TV/92443" target="_blank">📅 01:13 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92442">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ed2c6f597.mp4?token=Mxfzqb61bkfZgyrh3NYIg_yjpzBgR6tjoB8Iq8sXhPQvKIXgOJJfWbYS7i-Svoun2bpHs_ErSP5Q2l0dh44hH5LDAKVb1lhVEnOfUO6ExP1epGxBR_ReyEbSqwYPzYkCXKEWPJHqqgFiUQvLCJpNQ7IE_inL3xpSER2XsJAZSbNf7z-ZuZNaCFVrmbcoFJdR3vDxieNsUMUqDubtsq0UMz2s7tUfreJfltAuiSA3XrKrxs_FzgM9SHuGdvjzHPL-CtcEjrw5uI1iVkSxdzsU6vG4y7OyiwtJxPcu_itnBKYAVjr-6IDR5V7B5yzRSmsVQH7naHBxcBoK97NsdGlXuzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ed2c6f597.mp4?token=Mxfzqb61bkfZgyrh3NYIg_yjpzBgR6tjoB8Iq8sXhPQvKIXgOJJfWbYS7i-Svoun2bpHs_ErSP5Q2l0dh44hH5LDAKVb1lhVEnOfUO6ExP1epGxBR_ReyEbSqwYPzYkCXKEWPJHqqgFiUQvLCJpNQ7IE_inL3xpSER2XsJAZSbNf7z-ZuZNaCFVrmbcoFJdR3vDxieNsUMUqDubtsq0UMz2s7tUfreJfltAuiSA3XrKrxs_FzgM9SHuGdvjzHPL-CtcEjrw5uI1iVkSxdzsU6vG4y7OyiwtJxPcu_itnBKYAVjr-6IDR5V7B5yzRSmsVQH7naHBxcBoK97NsdGlXuzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
دیدار رونالدو با یک اینفلوئنسر که طرفدارشه
دختره زده زیر گریه رونالدو بهش میگه اشکاتو پاک کن تو خیلی خوشگلی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/Futball180TV/92442" target="_blank">📅 01:04 · 23 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
