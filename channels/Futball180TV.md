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
<img src="https://cdn4.telesco.pe/file/hQhajDmEeCBbEXLyUHM3soVJujc3Cz53kC_00iEpsN7MCQ5TcLsBfhMnBYHOaTf_dFCC19baWL6__XCy8_DI656WBrfyN5A_5AVMXUkCPAxKsMVivrG-FuQATBKsoQYi-cXRKymO28m76YNKNMWT1mEVR2ra65FNvIT_IFVfZCyXakWWmSK0f8L0quXkBVzoko0FV5dgq7gnlnBmcXKu6Qj1z3glTd7NiLZ67sjM7NbCL7d0T17CSqgou6GPn4TwA8WxRPFLiKvwajUnE_8Qgt0fSzowrkv6R49ksAGJ80IbkBsC_fFU0DsMvvxo8Q-JMwSnZgU9UvNtUMnbT_UF_w.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فوتبال 180</h1>
<p>@Futball180TV • 👥 122K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-07 18:01:13</div>
<hr>

<div class="tg-post" id="msg-90352">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">نیمار سه هفته به دلیل مصدویت غایب خواهد بود
!!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 397 · <a href="https://t.me/Futball180TV/90352" target="_blank">📅 17:59 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90351">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/abw7k5_0fNfeXl1mySAdkaBWAW_bzxx6F1rTK_2RHZt8b3WioATKjrZ0cxOR1-g5h4a_kAl0EOTN8ITpQ8pThZN05t5mx9UL5wCw-T_tihb2fokNW13Hpezo4km-LfKn78KvF0o3KRJ3vpio7-iqfjlg5Yl_F5obGcvPU4NEaEJZUT3s22oJuH78L8ldrEJk_gcvx3KOM4eBrTcgR1WXXWHhCh0gIu_9AyYvMfybxHGc4UF51_HvSMEEAAE66_654r_HEmwRJeoKXgavMhhQbrL59wZ6F4SILvVUaP6U6LhLMewCWF3qnWqNtwCxJSffA9-na4aL8qEyLZrQMUM20A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
اتلتیکومادرید به بارسلونا اعلام کرده که هیچ رقمی کمتر از ۱۵۰ میلیون یورو برای فروش آلوارز قبول نخواهد کرد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.26K · <a href="https://t.me/Futball180TV/90351" target="_blank">📅 17:37 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90350">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DoOzrntmgG5Gllm1wYErK3o7Rw04l5KN1EOI7si4gllSc8Z1e6pC-7i1bVCHFafqsaKsPWn9gXZoWfDKX_1mI-7EWsfLWFcP2anmMgoYzK6tuYlBWHBwonYCCEdKu4Zf04UQ9WNk7HhEhmFjgpxNfsmdhS9NFCo9dYs4hfH30BsBiV0cQfJpphkpOhTXHBnSB1t8m5EwbUMkj-IoiyqO7HaY6pJ9cKEGON7rQq7t6Wh7Ngw4orvociPUNrgINIVdfle9hgxj_J1y8zZaJ2y5namvq7CPLgudVoYpd2_s_JjE6ytfjoQldpxjd741iu9TGyDI-VuGNN23rJ_18hKgwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حضور گوردون ستاره جدید بارسلونا برای عقد قرارداد و انجام تست‌های پزشکی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.91K · <a href="https://t.me/Futball180TV/90350" target="_blank">📅 17:25 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90349">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o2FF1v2sQdK4dq_N4Hd02LOaclRUowr9HiZDK0XVi5WzRDwOU5zAFeKCgvUCu_21S9wKZjZN4h_6F10OOQBbPObKijrzJA4MTnV3bXhpr7-mYY_EyWCWkPXr9ay5B8Gax-9ihPwH25WbsHjJtnli0I_hsYw8i4_j2sDQuTXtrIlwk95QVqLYdQVyazrTFkhJLX-7y9kDcgTT0BycT7LN0HvxiFXVzN5BJCynnLLUzwEAek5jSJqx3Wp3NDxA78em-HPpVwgtdBFCy5q-qJQ5Lhgeb7zuHDYuUjyiBa8tGpGcbY7uhAg-6mH-X_Y1t6iPa5xSYdmZIvzNGjbh1FICAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
مراسم اهدای توپ‌طلا ۲۰۲۶ روز ۲۶ اکتبر یا به عبارتی ۴ آبان‌ماه در شهر لندن برگزار خواهد شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.51K · <a href="https://t.me/Futball180TV/90349" target="_blank">📅 16:39 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90348">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ae9wSRQ3C4p61SmL8RvjG7SaAhrUFVv2XX5py6qHjxtEuyLW30NgNSyQY1srxAx52NITMLlz_l2vIRF1YlonEGLPejtP2eLkVLWnyeG3UEj3vih-MoIzPzihkTIEof7C5SfTr9CQd7HBAobYwVvGNYiX9YQB-9lcX-77dEHMnbJZQewUHfPPZJCEt_Etjc1Qwms2U6OzQUgDKt7I93IZw5rVH6rHLAAiIRL3yaG7eSBVSbD9Eosl_idDAAMb2M0IMtKDvn-EJzyqcN_tlI8-exCF4YqpsMKf9iY26UHh9Q6e3no_ZCvL1y3VxeqKuzgA4dvKWwsfC7pDtjAgnxdiSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
مارکا: اتلتیکومادرید می‌خواد خولیان آلوارز را با قیمت ۱۵۰ میلیون یورو به بارسلونا بفروشه
💸
‼️
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5K · <a href="https://t.me/Futball180TV/90348" target="_blank">📅 16:28 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90347">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IUXcb-o6MalQJpnNpufQCo3-jP81_s6IWPMPwG_9J_DuYGooLkIRCGZjQNDVD_XV0zm9Z7zoquwfYHxmmId5iqw6rmW8G8ncTGULcgxHSI1YuJDs0lEEJI1v-8KSML9knEj3PRpykSEQpjVzDlK8plCb6RT6jTx7hI84zBm4Aj6KMj8MOHqwTK_P1-zkCOKo4wFkC-nlU0Tt_tYLw4lgQfDU27PBcvoF_h-sRPlNCbCYK466drou7As7qC1bIOPkWH8QmpdPsMF0brIp0h7DXYX0HyDwOGTqsVc2G9OiPJ4rTiBiXd8uFfT43zMCz0PfIX5J-gwk9U-NOTSN8RHPjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقایسه عملکرد دیگو مارادونا و لیونل‌مسی در دو دوره جام‌جهانی که قهرمان رقابت‌ها شدند
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.58K · <a href="https://t.me/Futball180TV/90347" target="_blank">📅 15:48 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90346">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb77f6f337.mp4?token=p7464886x3NBXcaRx-TRACgDHvZfDA9_AWjiqGbYqNvroM5a3k_VthxzUs5izUwgxxdo-_EOzBfkV9ZiHiiA5GHcgLk9aorkw5hVG0QaVc38iv8LdZ7XwLRJPgPOzmdyTIvrgpipp3IXzHIFYTWpiUdVaqTKR6OpuvQ8yFB5_ktvdJHTVmPUB83WYmAmeCD3FrMyd2IpjUYtqWXopOMMncNf5h5CaspHV1A9taWuYu1dbNVgvCx6iFht6twmECqhzfFZfZgv4Q5DDl2_7DGP4__qk8RNQNskyVoHjkqUugPDyquxBXvD624Q3aaxdQrM__pXemKL0xMhzu8mQipElm0PIi4GaePrgPh_gJoa0rfGZBBI2UFq8nV5rEmmPCL-iNHCwx2k18pzxm3LYXPoD24OitqZSmWdJlcnzuf2qK9R6RYpr_PQxwQuMTRZnevmUxqIXkGjsjnJNceE5WRnqtnJz3yxyu5wkGdQ-lLJjoMAgSrpAmKkU73lKMAh-y-dobS_zXVnbCKuZMUsG3HAFE_g-lu4nQr1t_yHHiJSU_a4j5gzWDDyWcXWFc5XKDseOibREQ2To6kQl07pDiInS3Z93d4QwyVbh3-9Qgw44Cksx-qxQV2t0N_x2f35n8DfiIxqzRRbWngYtiBDu-rRpSKuZu1vuqPZFee7krNEgBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb77f6f337.mp4?token=p7464886x3NBXcaRx-TRACgDHvZfDA9_AWjiqGbYqNvroM5a3k_VthxzUs5izUwgxxdo-_EOzBfkV9ZiHiiA5GHcgLk9aorkw5hVG0QaVc38iv8LdZ7XwLRJPgPOzmdyTIvrgpipp3IXzHIFYTWpiUdVaqTKR6OpuvQ8yFB5_ktvdJHTVmPUB83WYmAmeCD3FrMyd2IpjUYtqWXopOMMncNf5h5CaspHV1A9taWuYu1dbNVgvCx6iFht6twmECqhzfFZfZgv4Q5DDl2_7DGP4__qk8RNQNskyVoHjkqUugPDyquxBXvD624Q3aaxdQrM__pXemKL0xMhzu8mQipElm0PIi4GaePrgPh_gJoa0rfGZBBI2UFq8nV5rEmmPCL-iNHCwx2k18pzxm3LYXPoD24OitqZSmWdJlcnzuf2qK9R6RYpr_PQxwQuMTRZnevmUxqIXkGjsjnJNceE5WRnqtnJz3yxyu5wkGdQ-lLJjoMAgSrpAmKkU73lKMAh-y-dobS_zXVnbCKuZMUsG3HAFE_g-lu4nQr1t_yHHiJSU_a4j5gzWDDyWcXWFc5XKDseOibREQ2To6kQl07pDiInS3Z93d4QwyVbh3-9Qgw44Cksx-qxQV2t0N_x2f35n8DfiIxqzRRbWngYtiBDu-rRpSKuZu1vuqPZFee7krNEgBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هواداران جذاب الجزایر آماده جام‌جهانی فوتبال
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.03K · <a href="https://t.me/Futball180TV/90346" target="_blank">📅 15:19 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90345">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W5SH_2ycOLMiEDQGtv8ehB1IG17boO9YwiCkbR8vuLMvOQoB4BiJfEhfjE6O7hAx9KNKGqr4cEV_S3DVgzNxGn05oCfpulC8nTYQnpUZ2o6jymo4yUs3vrnw39vZXX57ml-KuD8tgwIOYRLHtn16x-S-DO-ml9q1k5B7P0SMJWuBFJXm6vZXroidQmMbDRJ8cfM37_g9BBsNAsR-4MNki2ENIUNEuHSubQIIJcWtLNvCJfh1_gDRIBprCISl_yMDYF11zHEyXRfVp29hpzkDwQLtsLUCAxypURPeDRC2t6geyuA_TJEwFtWyZ8PbbcdBBA3lOBW3HVbz2M93fob7Zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😍
🎤
امروز دور جدیدی از رأی‌گیری برای عنوان جذاب‌ترین مجری فوتبال را آغاز می‌کنیم.
❤️
عکس‌های جذاب ۸ دختر از دنیای رسانه‌های فوتبالی را تماشا کنید.
1️⃣
و هر چه سریع‌تر در کانال ما به گزینه موردعلاقه‌تان در نخستین تقابل رأی دهید</div>
<div class="tg-footer">👁️ 5.61K · <a href="https://t.me/Futball180TV/90345" target="_blank">📅 15:19 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90344">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pSVPWnnB2ho_J8wH5wyx0KYp1AU2WB6i7gVozrQLph2kvjLFm20DD1tizhyHTCjt5R6o2URI5o5--5pD0spjUcavoFt03A7vQowlHtzOK9C0Z-Pbg9ZJLDQM2-LbmscPjeTl1GVFnrSAzM6lYDTWHxVEu0V2mlLFCLpR8ggLYe-VfqPACN3zsg7nzLKUrVOiPJnN0oKSLTlAWhKEjIt-lhe2Ni8MxtVbN-bCL3EubqU9lG5ZVd2kzuwE4sVkiOdcjTzzUam_prKAMifk3k2ygE_NpvbKgk72GNUs2kxR-wxeh4sTecrG5RMfIhIzqy9Ym3NCsffAX1252AsuLr3Ymg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقایسه جالب نیمار و لیونل‌مسی در بازی‌های ملی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.43K · <a href="https://t.me/Futball180TV/90344" target="_blank">📅 15:17 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90342">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dOyHWDlVHlvhh0Uov-uneb5f3A9rnUJ34DFWK_bdx69gBN6oY0Ovwm2Mx0RDYeRZ9HeF5frqafNMCxAf2XA-a8onW_ZLlJiNn28LM97766K00qhkVM_3l4g6fW1RBrnysv14N2cs8OoO0WL46KBf2HVPBAcKLpZf4ASMTbchsEzyWG5LyddMugkmxlCQm1WriV6eGqah_dEwDCLoVmGqYVbjvlG8qVGHEnR-183wn8sRLODvlB7pPMqkj3uCStxZ8h0yJ9wqY8s8jn6V3kTedPRnVtCVEuj9GcEYOAiPuaISFUXDDxyGD6Nzz_hbKs8SVUZHGPEGCf5Ago7ClYbXdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بهترین ترکیب آکادمی تاریخ بارسلونا
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.58K · <a href="https://t.me/Futball180TV/90342" target="_blank">📅 15:10 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90341">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bdadf29b0c.mp4?token=Xy1SPUU2ytJzoBbjeCvjg9c08Z5lQSD1feQiLdyaPJQa664TuA49zjJOf8IcVUHG5GI_aqMf7BC5urijRCdu8mKu9QCdq1Et7f1-sFpQlkfnBGw8lgZwJLDKFWHpnqioXWb688C_uhJHAAQW1XZ9wepFMHWISPAvN0qvfMXQfzkP-PQShB1TRYr6Wte5skkD6sSg65bmR2NAXd1bHpVrQOUPFVHw30bkwXe65XWcqLEar5ubVoPqRiNy3EcdPvJlYUSKDmuslVdvZo7e4hioVCwxnQ2eq6j2P7ZcIoQj33vRdnZ5nLcEx1p12lpsg_uboQ1dbAvxx_sXzYFKCNeL6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bdadf29b0c.mp4?token=Xy1SPUU2ytJzoBbjeCvjg9c08Z5lQSD1feQiLdyaPJQa664TuA49zjJOf8IcVUHG5GI_aqMf7BC5urijRCdu8mKu9QCdq1Et7f1-sFpQlkfnBGw8lgZwJLDKFWHpnqioXWb688C_uhJHAAQW1XZ9wepFMHWISPAvN0qvfMXQfzkP-PQShB1TRYr6Wte5skkD6sSg65bmR2NAXd1bHpVrQOUPFVHw30bkwXe65XWcqLEar5ubVoPqRiNy3EcdPvJlYUSKDmuslVdvZo7e4hioVCwxnQ2eq6j2P7ZcIoQj33vRdnZ5nLcEx1p12lpsg_uboQ1dbAvxx_sXzYFKCNeL6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">استقبال گرم‌ و صمیمی از نیمار در اردوی برزیل
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.06K · <a href="https://t.me/Futball180TV/90341" target="_blank">📅 14:45 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90340">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc9f0d340d.mp4?token=O4r1MeWrNBZQUTHGNyj6OpvRwjJcWCHidmM27M-_nqKWnnnfoTj1a0lSvSHUu-7vBZH4cBZir5fCMF627NaDKYuKMxHc_i7gpip-WMUEfHbNKMffGnj_KZJ6wnwu73UWrSREWAjbmljjP2cNT22UA_K4nGOn5OTzFHATUvdYW0wtqR5-B08WMlr76cHBdBL_jcqQzqdrow7YpABRgmm5eQL7SRCc9vS-_22S0eptdaAcDzsy6enXlTEH-wikE9E--6jmes65Ob_70fz5P7gLJFsCBMO4JXp9KZIBA_D8Wu72innws825ahR3ClbGKjRoZnXToZqxF6cd5DOtvY0Ixg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc9f0d340d.mp4?token=O4r1MeWrNBZQUTHGNyj6OpvRwjJcWCHidmM27M-_nqKWnnnfoTj1a0lSvSHUu-7vBZH4cBZir5fCMF627NaDKYuKMxHc_i7gpip-WMUEfHbNKMffGnj_KZJ6wnwu73UWrSREWAjbmljjP2cNT22UA_K4nGOn5OTzFHATUvdYW0wtqR5-B08WMlr76cHBdBL_jcqQzqdrow7YpABRgmm5eQL7SRCc9vS-_22S0eptdaAcDzsy6enXlTEH-wikE9E--6jmes65Ob_70fz5P7gLJFsCBMO4JXp9KZIBA_D8Wu72innws825ahR3ClbGKjRoZnXToZqxF6cd5DOtvY0Ixg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انتقاد جالب و شنیدنی هیوا یوسفی از وزیر ورزش و جوانان که هیچ نظری درباره قطعی اینترنت در ایام اخیر نداشت...
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.61K · <a href="https://t.me/Futball180TV/90340" target="_blank">📅 14:20 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90339">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/18e2b0b1c0.mp4?token=TL5aL77GD2dozUAD3Pp-Q_TkUQSKKcZuaDdBbEG11Z_3CZ0RLaG8dlc_kCDOIcF2yNCRuIDUYlqaAWehCTktxi71LAH_jB9CIz88Y4XLpzdzw0vHM36Y7qkT1LQHAM7uYsWN07-wvGwE42V6SKhDJHT3K1EzrgofIbaxVG_sYEKlRZLxyt2OzVxKFV-JFcJnUr3UXKNEAqGlBsALYGR1Y2iqPwxNmihbHEi4-cA16bxIHu5sEMeHrYSeH-mrOoy315SjvnA3tix2pWcWu6Wklcvf5-HAnQsd17Q1MfoBqweTeTdHAXudCx6YYShgR_vrHa8mfAMQ3wr_i4iHSgwzPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/18e2b0b1c0.mp4?token=TL5aL77GD2dozUAD3Pp-Q_TkUQSKKcZuaDdBbEG11Z_3CZ0RLaG8dlc_kCDOIcF2yNCRuIDUYlqaAWehCTktxi71LAH_jB9CIz88Y4XLpzdzw0vHM36Y7qkT1LQHAM7uYsWN07-wvGwE42V6SKhDJHT3K1EzrgofIbaxVG_sYEKlRZLxyt2OzVxKFV-JFcJnUr3UXKNEAqGlBsALYGR1Y2iqPwxNmihbHEi4-cA16bxIHu5sEMeHrYSeH-mrOoy315SjvnA3tix2pWcWu6Wklcvf5-HAnQsd17Q1MfoBqweTeTdHAXudCx6YYShgR_vrHa8mfAMQ3wr_i4iHSgwzPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پيش بينى فرزاد آشوبى از عملكرد تيم ملى ايران
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.91K · <a href="https://t.me/Futball180TV/90339" target="_blank">📅 13:55 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90338">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bFyxN4Y3aGoJYAG0ITXVGRjItb97GXNAURJpOX52zI6qXXWiPO-jRQzrKref1IS4HtQ-q4Eyzv8NBF6ABSKbEaxQi-ALHsz8XwtVZfPuDvlVtrDlrD14ODyXzOTHXcLrB5smw6fwFZsjDxLUPXpAhFTpMx_yeS7VWnRxyDGUGnjQIqMBVMYWr582TRiYmu6A_Q_hj-14sWZLsTwouaCp_68p2FJxesIlP7GCG0E8lJ_SlvVkH4B5qZkboO8segrllMtEz6YxVeK1N7ffzdUIe406ZLiKsI4u53YX0PhWuSv-tUp7Bevp9qVrCIvxMD21QF5wsT40ze8LFgyrmkAJww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در ۱۱ ژوئیه، ممکن است شاهد پرتماشاگرترین بازی در تاریخ جهانی باشیم.
🌍
اگر هر دو تیم آرژانتین و پرتغال صدرنشین گروه‌های خود شوند و تا مراحل پایانی ادامه دهند، طرفداران شاهد رویارویی نهایی بین کریستیانو رونالدو و لیونل مسی در مرحله یک‌چهارم نهایی جام جهانی خواهند بود.
🤯
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.52K · <a href="https://t.me/Futball180TV/90338" target="_blank">📅 13:32 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90337">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jkq23cUzjqdR9w6Eir9XLOiCsfZeHQnjFZPmC4KlxqyUIP9Ig8x_ET63QuEVtau4x1P61tFhjIaXbKEmAyQyiG8zqEA9NgY69Uxobvk7jwhP5jMhp0kA6pdg-wH9piugNtKOo1kd3za3Q66l49YfwHukCRMnJWhaQWOihY-f1hppQ7Mg84kNSZTh1uhLVTkXEAR8Y33_xf6i5MN5kOXMYFGYWH5GBMnRuFGKmBAdtp--nQgWdR9w0d0xP9AVjQ89q7kWrVE9cjw9GQgsDni87C5QnKkcm8ZJ5XOacHUhMfP2_zFDBA9JLwrpqRwWV27SpAcp8cmXI4X_KEvrU4nO6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شماره ده‌های تاریخ تیم‌ملی برزیل در جام‌جهانی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.2K · <a href="https://t.me/Futball180TV/90337" target="_blank">📅 13:31 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90336">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/31f588b63d.mp4?token=gdNwZFMgf8Rg1TRTTMKuHXe-sKnWK-IBahAHZxf1YQ6g318S_bfs31jKskMpls3tuqZtfFRziZeHBphK0VKxfQkkrtafaTZBdUBvLWmrHRcRa5wJn8H_sC2uJlTdK0HPsbtK-EZtLglJk5CxHnEJ7E8nPHLTNEMx4Z2WrPBK8ZuB-UfjJcp55zwYmWyGf52zMYKMEHeXCs6-rsILaUqJZ7eB6lAJ7PnhpNlWf1Ye4DJ6Q3D6Va3w-5bVnsNqmiCJBXA26yRPOVhAUpfvfjo5TRcG32EnfjSuonWjdp-keX56_9bD11BrI4ERlM5H0ciszks3OlTihzgkBNJdzIHa9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/31f588b63d.mp4?token=gdNwZFMgf8Rg1TRTTMKuHXe-sKnWK-IBahAHZxf1YQ6g318S_bfs31jKskMpls3tuqZtfFRziZeHBphK0VKxfQkkrtafaTZBdUBvLWmrHRcRa5wJn8H_sC2uJlTdK0HPsbtK-EZtLglJk5CxHnEJ7E8nPHLTNEMx4Z2WrPBK8ZuB-UfjJcp55zwYmWyGf52zMYKMEHeXCs6-rsILaUqJZ7eB6lAJ7PnhpNlWf1Ye4DJ6Q3D6Va3w-5bVnsNqmiCJBXA26yRPOVhAUpfvfjo5TRcG32EnfjSuonWjdp-keX56_9bD11BrI4ERlM5H0ciszks3OlTihzgkBNJdzIHa9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترکیب منتخب سهراب برای حضور در جام جهانی
👀
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.37K · <a href="https://t.me/Futball180TV/90336" target="_blank">📅 13:21 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90334">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🚨
🚨
🚨
🚨
اولین پیشنهاد بارسلونا برای جذب آلوارز رقم ۹۰ میلیون یورو به علاوه آپشن‌ها خواهد بود. لاپورتا قصد داره قبل جام‌جهانی این بازیکن رو جذب کنه
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.56K · <a href="https://t.me/Futball180TV/90334" target="_blank">📅 13:04 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90333">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
#فوری از فابریزیو رومانو :  بارسلونا در حال آماده‌سازی اولین پیشنهاد رسمی برای خولیان آلوارز است که به زودی ارسال خواهد شد؛ هیچ بازیکنی در آن گنجانده نشده است.  خولیان پس از رد قرارداد جدید ماه‌ها پیش، به اتلتیکو اطلاع داد که تمایل به ترک این تیم دارد.…</div>
<div class="tg-footer">👁️ 8.76K · <a href="https://t.me/Futball180TV/90333" target="_blank">📅 13:00 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90332">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aqrSVKr5CWjynmOFt7cgyKTaPYREaS9XI57grwShCWyeRKiC6cYUQCL8o3P_slgw-n4c5-yCiS1ONi7EPRGFHrQ3fQAgflS-XFDGhm-r0SgLG7qfgrw1eyzkFx9S3XdUYB5uhkzuQbOzqTOcOoKzy8wj0fJdM6MBhntC7D7bVPRyLAeTx76EG_rFf2aTYMgof8aN5wOWWJNfmtIjgmnsI1QOBj5Z-gt2mZIFsX2NvvVBKOrIzOXEyw2XMxE6lW5NAKZGrtNhJ46uUUL3LkvEhH4vxPYzrSyn0y9AQQjMExhsWFX2XzZIL-oUJ2DyK5YWyX12b6DUC6Yu9IWQ2MEm_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
#فوری
از فابریزیو رومانو :
بارسلونا در حال آماده‌سازی اولین پیشنهاد رسمی برای خولیان آلوارز است که به زودی ارسال خواهد شد؛ هیچ بازیکنی در آن گنجانده نشده است.
خولیان پس از رد قرارداد جدید ماه‌ها پیش، به اتلتیکو اطلاع داد که تمایل به ترک این تیم دارد.
پس از ملاقات مستقیم با مدیربرنامه‌ها و واسطه‌ها، بارسا پیشنهادی ارسال خواهد کرد.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.17K · <a href="https://t.me/Futball180TV/90332" target="_blank">📅 12:52 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90331">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/858ae0e82d.mp4?token=pM21OkO-wqPlGyoKl276A-B7A9EOgpoqOM7SCOZ_3ZzO2wexyxm4BzQhITQ0c-cL6Ofw8o2q-qhghvUbdo0CHqtE127pTNCBz6z9ZBkhrtGqe4Ktf-CwMlXGzdmqJT07TtMv5gP76ODgOzulU8yRNVK0XfaNyX3Rspy9UhfYP0i3AX7FXg16uV35uXOULaTJjMGjA9rPzhBRpuGPeJNU7DmTiwNrRiw0zpPm0HTpAnIjIet0aBnNrX1xdBVkKdur3-X56CEtPGnO1_GYHx0I5-VjzDp35BL4xH4Kac3rc5KAp0SK44ZHpVSZv7F63PnNHpP0hkOH8XkUDHxz0vldaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/858ae0e82d.mp4?token=pM21OkO-wqPlGyoKl276A-B7A9EOgpoqOM7SCOZ_3ZzO2wexyxm4BzQhITQ0c-cL6Ofw8o2q-qhghvUbdo0CHqtE127pTNCBz6z9ZBkhrtGqe4Ktf-CwMlXGzdmqJT07TtMv5gP76ODgOzulU8yRNVK0XfaNyX3Rspy9UhfYP0i3AX7FXg16uV35uXOULaTJjMGjA9rPzhBRpuGPeJNU7DmTiwNrRiw0zpPm0HTpAnIjIet0aBnNrX1xdBVkKdur3-X56CEtPGnO1_GYHx0I5-VjzDp35BL4xH4Kac3rc5KAp0SK44ZHpVSZv7F63PnNHpP0hkOH8XkUDHxz0vldaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینترنت بین الملل وصل شد!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.73K · <a href="https://t.me/Futball180TV/90331" target="_blank">📅 12:35 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90330">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👍
👍
#اختصاصی #وینرو :
✅
ثبت نام کن
🤩
🤩
🤩
هزارتومان شارژ بی قیدوشرط بگیر!
💵
💬
به مدت محدود
📣
😮
تنها سایتی که با عضویت بدون  واریز 500,000 تومان شارژ بی قیدو شرط میده #وینرو هست
💰
👑
#معتبرترین سایت ایرانی
⬇️
🌐
Winro.io
🌐
Winro.io
📱
کانال اخبار و هدایا r7…</div>
<div class="tg-footer">👁️ 8.44K · <a href="https://t.me/Futball180TV/90330" target="_blank">📅 12:35 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90329">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pdDXXFMpB3twd6F9qcISJUgV2YOkIIh90sy9CyG9vehkL0n4GKYU0VwLCZBuR_EKjEOX9S_1xSgXEDRRudUxfXNuII6WzxQN7tWNSbVaulXf9grVf-05CmJFHCpZCOG5KPx6ajCkr5B6-1hCEkqgVcOfjpPEVz5YuXlR1AGMWEppWQZrvl1FHi76CpQszRnTsLWEaMqUhuMgYBSP9kqvVOlJrj60Kfvnm8A2pBNyfHWnF_n3JWyyc_NvxKl_WJA_AnsvFVFYzMcpA-8CNY9s-Kah26AWqYz89I0UsMZx363YaE5ut2BW5rkOgvt58nWdAqI3pDoM2Hgxz100rflP9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👍
👍
#اختصاصی
#وینرو
:
✅
ثبت نام کن
🤩
🤩
🤩
هزارتومان شارژ بی قیدوشرط بگیر!
💵
💬
به مدت محدود
📣
😮
تنها سایتی که با عضویت بدو
ن
واریز
500,000 تومان شارژ
بی قیدو شرط
میده
#وینرو
هست
💰
👑
#معتبرترین
سایت ایرانی
⬇️
🌐
Winro.io
🌐
Winro.io
📱
کانال اخبار و هدایا r7
🎁
📱
@winro_io</div>
<div class="tg-footer">👁️ 8.49K · <a href="https://t.me/Futball180TV/90329" target="_blank">📅 12:35 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90328">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/97ac0d5890.mp4?token=YTYJrEv7cZNJG5VcnnumcRcbB12Zs1GuK8jbAmLnDSVMMYolpJ49wd0HhhdJTKEbjMEG85ySkHdTJaNIy401ZQP1vkameL5nM1keFFwUZI7zwyN-7p8_cDF4ZyeAXfonb5Mm0PV0G7078s1N4JjPSbMjxSN_jvoffszzR7nUqT4_hp73wHAZ6rqumbbwNiMYI9mmfKmg_DgSPjTkc41FeV2d8P4yXYoFP8uz8FGled8yXiWBySEnYFSlwc9SvbfdLQYWUKFGeN4iuosAHW__KU3bpfENCJMs9QX63jYA1L1LvHAY99Nc2aaVoQku1sEfqrWzk8NmtfOzSBNJh3ft3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/97ac0d5890.mp4?token=YTYJrEv7cZNJG5VcnnumcRcbB12Zs1GuK8jbAmLnDSVMMYolpJ49wd0HhhdJTKEbjMEG85ySkHdTJaNIy401ZQP1vkameL5nM1keFFwUZI7zwyN-7p8_cDF4ZyeAXfonb5Mm0PV0G7078s1N4JjPSbMjxSN_jvoffszzR7nUqT4_hp73wHAZ6rqumbbwNiMYI9mmfKmg_DgSPjTkc41FeV2d8P4yXYoFP8uz8FGled8yXiWBySEnYFSlwc9SvbfdLQYWUKFGeN4iuosAHW__KU3bpfENCJMs9QX63jYA1L1LvHAY99Nc2aaVoQku1sEfqrWzk8NmtfOzSBNJh3ft3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بازگشت لامین‌یامال به تمرینات اسپانیا برای حضور در جام‌جهانی فوتبال
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.15K · <a href="https://t.me/Futball180TV/90328" target="_blank">📅 12:15 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90327">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WJhSaAb7ziiEHhfw2_YdMHkHG1bFR56vECrch6UGYrKX2oNeAjmy3MhHVU1_pwPjcjSS583NO3APUpHnWR3D6R5vE3lIDbHKDOt4G468iGkvHvqQZ5cwrLOa9-R5yUZY7a49iqacY76UOP-s7GwNHbItlLdDNT0isZcqN6s61joFemtBWKsdlV0eyM1dEE3Wibq3ExfdDdOUtxKkwnxioomPOlpncU_-wYCGuJhtP0Lp4ns_Vg6502UN19HdwFlcBDKs6AEYe4d_W9TPnb24Q8hJsmKyK-ePbC3U_1kafOWmCJ70nvercz_cUKACV9YGUkI_gPPDIsPixkm3s1AVbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیشترین حضور توی سطح اول فوتبال انگلیس
آرسنال تنها تیم بدون سقوط
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.99K · <a href="https://t.me/Futball180TV/90327" target="_blank">📅 11:50 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90326">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e24e703cf.mp4?token=WZ0s0fTzoO7gFKD1eLIlI_XFxN4VyLWs5wpyZEEd3H869l2-dveo_NV5YXMny6J17DiPP_amCKIsxZ-VgnlPZfYSgrvQlx4fQ_4HztsKhZi8nZgy-Q1Joh5YSFCaubHzFJswbsBW6TbefcCjnR6znlUgVluWYkTuVYP0_40VmzjqZChi-kOM6tdB60J8bHK-N7ZrZmdj1HMPyUOBpglpPgPZxvoSGKf6jcawAho4pDJnmGMbwv1sp7UIZmpwEEsTQJCvFN83AvdX9fI-m_xQTDlXNMt76kfgG55Bai1gUyh5wE3MrYMroG_k0oiAV0oP_qn9KBeoZ-KcyB-2NiTMyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e24e703cf.mp4?token=WZ0s0fTzoO7gFKD1eLIlI_XFxN4VyLWs5wpyZEEd3H869l2-dveo_NV5YXMny6J17DiPP_amCKIsxZ-VgnlPZfYSgrvQlx4fQ_4HztsKhZi8nZgy-Q1Joh5YSFCaubHzFJswbsBW6TbefcCjnR6znlUgVluWYkTuVYP0_40VmzjqZChi-kOM6tdB60J8bHK-N7ZrZmdj1HMPyUOBpglpPgPZxvoSGKf6jcawAho4pDJnmGMbwv1sp7UIZmpwEEsTQJCvFN83AvdX9fI-m_xQTDlXNMt76kfgG55Bai1gUyh5wE3MrYMroG_k0oiAV0oP_qn9KBeoZ-KcyB-2NiTMyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">«تازه خارجیش رو بهتر بلده ..»
😂
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.14K · <a href="https://t.me/Futball180TV/90326" target="_blank">📅 11:25 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90325">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🔷
#اختصاصی_فوتبال‌180
؛ مونیرالحدادی و یاسر‌آسانی دو ستاره خارجی استقلال برای ادامه حضور در آبی‌پوشان خواستار افزایش دستمزد و پرداخت به موقع حقوق خود شده‌اند. سیاست مدیریت فعلی استقلال بر حفظ این دو بازیکن است زیرا پیدا کردن نفرات جایگزین در شرایط بسته‌بودن پنجره نقل‌وانتقالات عملا سخت و غیرممکن است. قرار است پس از جام‌جهانی و مشخص شدن تکلیف لیگ‌برتر، جلسات ویژه‌ای با نمایندگان این دوبازیکن برای ادامه حضور در جمع آبی‌پوشان برگزار شود
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.88K · <a href="https://t.me/Futball180TV/90325" target="_blank">📅 11:24 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90324">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rxaaxEk3p82le40iFMOx9ISLAUyMl5khaYWR5icNZ2adCSOCJDFNwMYF1CF89BDK-eN54cEDNDxc12atVzwuf7eHNxAR2th3ZIM4YEIMHVhSF49sp-op_nDeOOK4XfgfFqgj8DdILMiUM2LamwYsekRYBuyC-AomjAQJr32Ilo6RkL20D1TKszXCPV-kmDJB9nGVRMRoy5g4H9R6eWXoFUI2jcPgxt43XuYh5YRdkV-xl9RgPo5ku-94XWPQbqcYF3tulxN4tso4YeEdgdr9pKLV7Myev9P_dJidd1dcKPxdZhf3hipGAUesA6Lc4JPK7yhrAudleYWwZUQkajMqiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
شب‌گذشته دیدار مهمی بین سران باشگاه بارسلونا و وکلای خولیان آلوارز برگزار شده است. این بازیکن شدیدا خواهان خروج از اتلتیکومادرید و پیوستن به بارسلونا است
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.28K · <a href="https://t.me/Futball180TV/90324" target="_blank">📅 11:20 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90323">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZNnM7zZpL-vXBHwMB8jHMbKgKJUtm7fS-s9S5tCYys95-Q9SAXisnaO-b12mcsxMtJDdTM-f-wzBjBw0NX88s7tIbYPlmbYM0XiVw9elRtyE3APKXLuS0KG3aaQUqNVduWLRujzQ6b5O9Ajj8VxOrfq3DV3rwZ4ljLv34rcSqriy0zlt94AxW4jUwcnZHEb7L7h0G72Sq52RluD5K0Nb1bJXoT_7ZOT_hPg4c5lurowLO4yMplnJlb_mls3MX7tYLZM-s0e7Cxuk1HsH1nXkIp9MZ7cSbzKkljwB1hWg-autxDlN98-3qG3rSc6cBUdRWHe5n4kcC3J20eZXqubRlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بهترین گلزنان تاریخ‌فوتبال برزیل
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.14K · <a href="https://t.me/Futball180TV/90323" target="_blank">📅 11:04 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90322">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40f4a1291c.mp4?token=t37iWqIwhsBtLPoNznfCpx0n1uu39gqDuQbAilsNzSpO0yCg0Naf-Y31r55629mtd75KqdX5DJjDVB5KVKr3l9aoSfPh3-EoDIRzOWQFLgKa0JUWDAY6VZWFlawjTBja6zy8weN53kF8c9o6NS2ATT750z2Y_0jwhFGCuT_wO3F8FuWjTRK0C-aKNeYS9xqjszWhmODDurYhSbkLkf3aUraSEoYlGgMLM8JGHaJd-wZ9laE0ZhuiKNPp7AvlbnInD6Wq7Jh7Bt6xoprJbW05iUxHoDto1dSHMNlH8R2yi7SPuaOi7H3Q_rN4MWs0-6T3_8qEuxSyEMQ51a2_ERVuRS-NftlkCPQKqs0adIH9-R6nx5D5aT4zkCqnFneKBqJuWcTx9LBbtUEYRBZynIBc5hnvkC_aohF4gmPumZQgQRkPH4sOfVCJ7CF_rt9EUacoSwmDJrr6o6754l5CvhgVhdIAk62eS9JhDqp2_7_uokymxOoATy8I6l5OwrlCdrH218Gd69Ha7k_Yj6ZnoNojbj_YQquBhTUktA3Z7pcqTaeCU5mdPDZJqjPC9XcY2TfjhtzG3Lz5NMwGkW8KmeYPa3KqrW45kyK38m87JKEBG8k-8yfJ9fjaw-WzjBMyD2HgJq3veI5bfFJuqKc-Ocq3AlYBUb4FbVBIsCJRLNLntQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40f4a1291c.mp4?token=t37iWqIwhsBtLPoNznfCpx0n1uu39gqDuQbAilsNzSpO0yCg0Naf-Y31r55629mtd75KqdX5DJjDVB5KVKr3l9aoSfPh3-EoDIRzOWQFLgKa0JUWDAY6VZWFlawjTBja6zy8weN53kF8c9o6NS2ATT750z2Y_0jwhFGCuT_wO3F8FuWjTRK0C-aKNeYS9xqjszWhmODDurYhSbkLkf3aUraSEoYlGgMLM8JGHaJd-wZ9laE0ZhuiKNPp7AvlbnInD6Wq7Jh7Bt6xoprJbW05iUxHoDto1dSHMNlH8R2yi7SPuaOi7H3Q_rN4MWs0-6T3_8qEuxSyEMQ51a2_ERVuRS-NftlkCPQKqs0adIH9-R6nx5D5aT4zkCqnFneKBqJuWcTx9LBbtUEYRBZynIBc5hnvkC_aohF4gmPumZQgQRkPH4sOfVCJ7CF_rt9EUacoSwmDJrr6o6754l5CvhgVhdIAk62eS9JhDqp2_7_uokymxOoATy8I6l5OwrlCdrH218Gd69Ha7k_Yj6ZnoNojbj_YQquBhTUktA3Z7pcqTaeCU5mdPDZJqjPC9XcY2TfjhtzG3Lz5NMwGkW8KmeYPa3KqrW45kyK38m87JKEBG8k-8yfJ9fjaw-WzjBMyD2HgJq3veI5bfFJuqKc-Ocq3AlYBUb4FbVBIsCJRLNLntQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یکی از عجیب‌ترین وقت‌کشی‌های تاریخ
😂
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.21K · <a href="https://t.me/Futball180TV/90322" target="_blank">📅 10:35 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90321">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/txN6JiZEyrhxUdR3jplFCLHxGpwDWsqkWyB4xJrVO1o9RjgFpgDR8KVjJhf_C9WA7jxgyzoh9_cS-j0tFo-jJD21XYyw-ivZa1YsY8FeWwWsvOizWjKo3QyytYt_eyf94tARuFDP0Kc9ENK037VamdXuZKMGJ7xNhSpSIQg0QY02CsRmFg7eY5GMvcsJ4y5ZAWdq4_wTsla3_1A0oPEqwAlykibmAhaqjlMGYOEykocuqyXeew6oqzgKGQesOz47bMhwhewlukIbvLylqaE969RvgAA7bCVZdW6H_xlc1QOqST7AsvWse3LAxoi-WWZcaEtgeeRymYW-z3dUrk-KnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فیلیپه‌لوئیز سرمربی جوان برزیلی هدایت تیم فوتبال موناکو را برعهده گرفت
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.6K · <a href="https://t.me/Futball180TV/90321" target="_blank">📅 10:21 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90320">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/njm0193h0GBAWTL_w-wMhf8VeXspC7k4EqIxWnAiSlsju-h5mK_0ti8jAy5zFOnR_2ezGbAV0drrit16X-qXc6TrVpUeAKlZmx5hEcke2d0k3xESTm4-BY6VkogffYvxxpMCThQNL6IooYSNZGQNPlya0xmDg_dF28_cr102aqaVzpZYq5MUx7L5PEXHTVd6fxBhS7lHJTmXfSStcVv5aV4GkUMRLvJHyTU7UhQz3POOc6qTghf74BNeWZnejbR5Bu8gLHK4WxPCyuzKD1Jq3FORJDVhLO8jV2B0iHJp1iMMt980TBGdL74VSKmvEhjGcAPw6SiQ1txL3euUapdeOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسپانسرهای پیراهن تیم‌های حاضر در جام‌جهانی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.46K · <a href="https://t.me/Futball180TV/90320" target="_blank">📅 10:10 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90319">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/49f9845215.mp4?token=Higc6-I9oXt4iG-YOSWS2k777yB9yfoUG3sIZ5w8nQdhqkUZsVrkBuisx1RvMI5XHj68YmzJQw3FoX_7FtFyk5D855A7HLbqYqmuYZx1MrwX8Em2mQ3qAJ17wtNDrFm3JtJGPpFWnMlXmKjg_58KECg36krKmLD6kX5b2xOwzpRBof_N_w78fZld36TlT9n2EYBOV5O8iaiBHAEZoSHbNa9k4Wc0MD7grQOnVsfvmF5_TM8fw_rBoHyjRliU-K1QRqz-Gic1HsPnyG9Ckv7eQlVBXluls0b-p2sTgGXqSquj37c33yHYpf79YHOfXbeaFYpNrXLa76yZzLLkj17MKXlt71BvPbsGPPRsboiCnoHHWcUGsEAxl8VC76wOCeWJdbdy-hVSrhM920QGSbkFrKahw4HSp5SarsFb2y8pAP2-Not0icf4QkSLqp-UBPyOlI0mqguCMoraLCytULpeiShj5OOnbA5QQAZUb_1d3k9Ff1qBJrS9jbL_yp0dFGPTQ8O3XqvBW7wRzh5PVwpN3n0nkjL7qtKmp6JHf3W1CZ2nTs30_1lMIzO7f0Osqu2OaK9erZHGV9m-O2D1Z2FcWTgtl074xFwplaHe_uxiDKAnEk6I7Y6RuPDBkTT7VUOt8aA9EDwYBQ1qoN6yMGFK-n1mAUfeKQQ61jFlGZ8CdZY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/49f9845215.mp4?token=Higc6-I9oXt4iG-YOSWS2k777yB9yfoUG3sIZ5w8nQdhqkUZsVrkBuisx1RvMI5XHj68YmzJQw3FoX_7FtFyk5D855A7HLbqYqmuYZx1MrwX8Em2mQ3qAJ17wtNDrFm3JtJGPpFWnMlXmKjg_58KECg36krKmLD6kX5b2xOwzpRBof_N_w78fZld36TlT9n2EYBOV5O8iaiBHAEZoSHbNa9k4Wc0MD7grQOnVsfvmF5_TM8fw_rBoHyjRliU-K1QRqz-Gic1HsPnyG9Ckv7eQlVBXluls0b-p2sTgGXqSquj37c33yHYpf79YHOfXbeaFYpNrXLa76yZzLLkj17MKXlt71BvPbsGPPRsboiCnoHHWcUGsEAxl8VC76wOCeWJdbdy-hVSrhM920QGSbkFrKahw4HSp5SarsFb2y8pAP2-Not0icf4QkSLqp-UBPyOlI0mqguCMoraLCytULpeiShj5OOnbA5QQAZUb_1d3k9Ff1qBJrS9jbL_yp0dFGPTQ8O3XqvBW7wRzh5PVwpN3n0nkjL7qtKmp6JHf3W1CZ2nTs30_1lMIzO7f0Osqu2OaK9erZHGV9m-O2D1Z2FcWTgtl074xFwplaHe_uxiDKAnEk6I7Y6RuPDBkTT7VUOt8aA9EDwYBQ1qoN6yMGFK-n1mAUfeKQQ61jFlGZ8CdZY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">برزیل و هواداران جذابش در جام‌جهانی
🔥
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.59K · <a href="https://t.me/Futball180TV/90319" target="_blank">📅 09:45 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90318">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T-tzbO_IFHf8u1dVRjHKjudaQuxOU2a-H13RtimPxThje6QPN3XX7Azeg2FeBemdtwutdqDFiqcEBkDTMJd2o2sVQNDWwxLlIxk7lFRztXDsrgmXI_51KlYVR2YsA2YHg4xv3tIw-bIZLekUYC4Z8xjsqSZBU4vbiqa-15KSjl6yBQvmbbwlju8GHYUAjUz-fJedPe9h1bAG7QDWlKkbnEUlqulqjFLj0QF22Hfo9o7-jO5722a_sab-j-z0wJUM17y8ynArmEwQCWFqPJnLnF-OCBv01c4hIoYmFA12TgZyuGaoZuxxxM_Kb-8dWhqf0n1lgya-cimOGHfDmL6SSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پرافتخارترین تیم‌های ملی تاریخ فوتبال جهان
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.72K · <a href="https://t.me/Futball180TV/90318" target="_blank">📅 09:20 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90317">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e84afd40a9.mp4?token=GY0lauXs2WMFWTnrDGtuU1OPEjBhASnx1ibgDVNQbuX2wij32q7B8lpcbqJRmyyKYb0cVAICA7oDO0g1LK6tnl9orAoHevKFk3R1BHCxZPFcCVgc0MY0WVIpbwRuJtMfh8A0MqW6NqRLJfSnvME_Jc_eVesbStEaliQzx7IxYm1LhxuQBJEtKp1CX0Fuz_3ubwD8OFRdqtWGhW4RYYUGiIX3ePjIZ39kl1KVmIBtR0Oen4_WOMS30AhrkZ9x7n4Y-IcSVfFgtXww00Dr621dyM8aadsCVweuMJLATCWHqr50dXeMFL8xDLcMUJ5y3GCjjRGHryeNyPATYjIK-mPDDj7nd05y64eqSQK4_RxY549vRF1dTxN-j_uXyTSMWroRBcH3Aew_qcso4UTIZcRZXIDvcnP_Wzu1KA2NFX3jE43WTBmUHyivzibEQJDX-0-HMY9P5UTbUs51aUJ_tHw9jrENPDwbFT4c3fZJOj01XbhXikNMagUc907F47pHJF0WubuuEYJh_Qbp7wqNB90eAarlyx_ohgiw6dPOAW-NQV8XNGoq4QuJyIiHMY68xoukRKGLnhyxNV5elE_2fOX7j7QoSkRVIteGmHCDkTHbNsGgKc52B5Jj5jX5wEwDz5Yh_U_xWz5XsSrcW-htm86a3Ivh8I3dLJspj9k0ppe9blo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e84afd40a9.mp4?token=GY0lauXs2WMFWTnrDGtuU1OPEjBhASnx1ibgDVNQbuX2wij32q7B8lpcbqJRmyyKYb0cVAICA7oDO0g1LK6tnl9orAoHevKFk3R1BHCxZPFcCVgc0MY0WVIpbwRuJtMfh8A0MqW6NqRLJfSnvME_Jc_eVesbStEaliQzx7IxYm1LhxuQBJEtKp1CX0Fuz_3ubwD8OFRdqtWGhW4RYYUGiIX3ePjIZ39kl1KVmIBtR0Oen4_WOMS30AhrkZ9x7n4Y-IcSVfFgtXww00Dr621dyM8aadsCVweuMJLATCWHqr50dXeMFL8xDLcMUJ5y3GCjjRGHryeNyPATYjIK-mPDDj7nd05y64eqSQK4_RxY549vRF1dTxN-j_uXyTSMWroRBcH3Aew_qcso4UTIZcRZXIDvcnP_Wzu1KA2NFX3jE43WTBmUHyivzibEQJDX-0-HMY9P5UTbUs51aUJ_tHw9jrENPDwbFT4c3fZJOj01XbhXikNMagUc907F47pHJF0WubuuEYJh_Qbp7wqNB90eAarlyx_ohgiw6dPOAW-NQV8XNGoq4QuJyIiHMY68xoukRKGLnhyxNV5elE_2fOX7j7QoSkRVIteGmHCDkTHbNsGgKc52B5Jj5jX5wEwDz5Yh_U_xWz5XsSrcW-htm86a3Ivh8I3dLJspj9k0ppe9blo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از جذاب‌ترین هواداران کشورهای حاضر در جام‌جهانی بدون شک کلمبیا هستن
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.31K · <a href="https://t.me/Futball180TV/90317" target="_blank">📅 08:55 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90316">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c6e129bd0.mp4?token=qjEb2kOkszOTTtktXJ_fsv8dbVjrXeI59r8U_eUbkJYIEsHzHwCQ27kA_03bpEkbQcyupBLlw2275oFlZf_uGwxEq3ZGmnkCxiPNpG4hyyl5iSInMFM5IuDg9TRUe2iJN862olIAQN3WTqi2q-lo1HIKsiBMwAeifHC6ddN-K33Mb2Q1JhS8PUd1BhC-4Y8gvJt_KUeBqJ0L8goZCll0JhDolD3ZW4a43vmrsMCIRMK5eoV6wzLcAIr-ex_iS5yiOGkKNi9ySuPFA58654NWHV6GRPCQuHbX8TE7uz0RqpfCYZDp9dKXlLcPnbibqF9ILCU5gQaPpUJkBYLfASdKPgfzDkBDorv0emIKEMFqu_Azgl01XcVj0cyfLNGvjOWauZZLpLsMyP1Z3R14SkMMf3Kd82fjF1tsAxnbuJpLu5Dp5KKroJv2fgfxoNAZXJi6QPOtqQePExWK0yKyH4bW_8nvSfURNIUnmZR1-0c1KXjLBLWaPt1SEZgx5l8AulZMx2vB28p1MbWnyTELH0l7xHzi_RZD43Jwj3h5FTEVfFAusAQJmCCp_roPhzmAiTahkXcfkbeQECFI7QglV4B31JMqhW2WxN9rK-R8j-PwM9SxVw5upsVZpfW3dY-MPMHW7lS04Xx0c2GS1ZVQZyxj1n7PDQgkMCKpMOQt7JhtN2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c6e129bd0.mp4?token=qjEb2kOkszOTTtktXJ_fsv8dbVjrXeI59r8U_eUbkJYIEsHzHwCQ27kA_03bpEkbQcyupBLlw2275oFlZf_uGwxEq3ZGmnkCxiPNpG4hyyl5iSInMFM5IuDg9TRUe2iJN862olIAQN3WTqi2q-lo1HIKsiBMwAeifHC6ddN-K33Mb2Q1JhS8PUd1BhC-4Y8gvJt_KUeBqJ0L8goZCll0JhDolD3ZW4a43vmrsMCIRMK5eoV6wzLcAIr-ex_iS5yiOGkKNi9ySuPFA58654NWHV6GRPCQuHbX8TE7uz0RqpfCYZDp9dKXlLcPnbibqF9ILCU5gQaPpUJkBYLfASdKPgfzDkBDorv0emIKEMFqu_Azgl01XcVj0cyfLNGvjOWauZZLpLsMyP1Z3R14SkMMf3Kd82fjF1tsAxnbuJpLu5Dp5KKroJv2fgfxoNAZXJi6QPOtqQePExWK0yKyH4bW_8nvSfURNIUnmZR1-0c1KXjLBLWaPt1SEZgx5l8AulZMx2vB28p1MbWnyTELH0l7xHzi_RZD43Jwj3h5FTEVfFAusAQJmCCp_roPhzmAiTahkXcfkbeQECFI7QglV4B31JMqhW2WxN9rK-R8j-PwM9SxVw5upsVZpfW3dY-MPMHW7lS04Xx0c2GS1ZVQZyxj1n7PDQgkMCKpMOQt7JhtN2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">علی لطیفی پیشکسوت فوتبال: کی روش شارلاتان بود، پول می گرفت و بازیکن دعوت می کرد!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.22K · <a href="https://t.me/Futball180TV/90316" target="_blank">📅 08:31 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90315">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🎯
شانستو #رایگان امتحان کن
⚠️
🤔
میدونستی توی #وینرو میتونی  رایگان شرط ببندی؟
👍
تنها کاری که باید بکنی اینه که عضو سایتش بشید و
🤩
🤩
🤩
هزارتومان جایزه بگیرید بدون نیاز به واریز
💖
تنها سایت مورد اعتماد ما با بونوس های کاملا واقعی و رویایی:
🌐
Winro.io
🌐
Winro.io…</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/Futball180TV/90315" target="_blank">📅 01:14 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90313">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QFBGWfbsmH2X--9Tf6XXoZFCJ2ixvTQ_ez9TxGmZV_ifilpwNOwcqD6ULGJsdWZk9-_taUXpPGl5_PcMYyHrYfulQUmlKz8dox8JtCsiND6lCRSX6cDPy5b3ExjwMBuE5y-tnnEdG_DU7-pdQjfHz1t9GE6p_5SGcHcqPSwraEw1BJxS1zEh52LQO_lOkCFF4CEwwqxF-RCa_XNazkx4qABedBQykNZJAdglIuRfbuMv0bE0ggdXZXx4gEvsZiSbbCu-iwtq8H6myq4RPSQKZaaEQzHQGCL70DIidr1ODFeIyBKxclEWbmBUNpduMzlCjukLR_q9ERUAMy3mSz8btQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎯
شانستو
#رایگان
امتحان کن
⚠️
🤔
میدونستی توی
#وینرو
میتونی  رایگان شرط ببندی؟
👍
تنها کاری که باید بکنی اینه که عضو سایتش بشید و
🤩
🤩
🤩
هزارتومان جایزه بگیرید بدون نیاز به واریز
💖
تنها سایت مورد اعتماد ما با بونوس های کاملا واقعی و رویایی:
🌐
Winro.io
🌐
Winro.io
کانال بونوس های رایگان
a6
📱
@winro_io</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/Futball180TV/90313" target="_blank">📅 01:13 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90312">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qRzMJReUmk8hwMRfWCy8xSvYXoZ6KaSGxdiQwN5cRaAKq4Sqvt9jZPk_n1atP-ncz7s_ScO6Xvp8atB14bZ8GgmDkpUCieR5ZEZs_TI0hwqO8JtI1imWZ-Ur3j45Iub9Oj1ypEbrOymUaTvfjoNboNNEOejz38pJqxgvnLe4uJiKwM79kAeyNkmzvDN8t9pWormPb4AQsgTQ2UskFFXii_efGyU5s47gOeeNEyGFJN_bA8AM7T_dddP9V4EdgiXdMRWuEVgaDsrCPrYG5mzUL0il5mE_KO8W63Sva12upOexZ9GZxwrcldJfr8V2Tt-6wYLabqE1L1pB9jBN53XWsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تیم‌فوتبال کریستال‌پالاس قهرمان لیگ‌کنفرانس شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.85K · <a href="https://t.me/Futball180TV/90312" target="_blank">📅 01:12 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90311">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aAc81RRyjuVoidZHMTmEXwJXhRd6SICxPzzINra_MBHHT58BQ-vC6kPoKGdyRtbD97LUSureFU2PGsxdlvjRFA8EggUQThW1JEj26nXRdAxqvDHrcfAVucATn8f9pwSenTZ6dqKBbpRsRrxEPc_1sPRyQXfbl_tB4n_ST_gS8G49GCnObt9vWwUiEtcZHhUFXutq1z7LaIsO9dQZLI8xZpUz-bhEDfEoQx066Vmf3u80qIWIPJMt5i2n6f3SJ7clqxirF4L2RN0il1vs3m5vtnVes62PUUCyFQ5DTeM_PsTHoqU0XkPVMiBussZSTKpD7-Rc2rImjf8iRb6hpjlxnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کافو تنها بازیکن تاریخ فوتبال است که توانسته سه دوره به فینال جام‌جهانی دست‌یابد. حالا لیونل‌مسی و امباپه این فرصت را دارند که در کنار کافو تاریخ‌ساز شوند
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/Futball180TV/90311" target="_blank">📅 23:55 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90310">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🚨
🚨
برخی اخبار کاربران گویا این است که سرویس گوگل‌پلی درحال‌حاضر رفع فیلتر شده است
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/Futball180TV/90310" target="_blank">📅 23:30 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90309">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l4BuwOmX5Q5hXdTzQJWh-J_RJgAf5JTQy7dw4YIepMpum9XXgOQw3HD0o67z5ILG-DzWoPYfrdBGbH0b8k8B9_u8U41zDh3qkTE4p_onJ5LoWlQVsTfqcg0uj8rITQC6oP1_1QWfo7c28dzx5GsHH66_HPyMDPHuQx_FWmmVZQwZd2ci6-IRvsI2M-AU_TmNhx_M1YbSvT9Htt8vBnWSA-xFUaof9Wc5bEhm_3dlctlM5lUuKFYb-vqp6Jw3rna2pO7gBNo2ER_xoE1q_mqCULdccTeIUqPeKxCPYchLAkw9_9mmI7gVzTNFCJsc-ez0Y3pBRCLMS0LXGvxVIQBv-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عملکرد تاریخی اسطوره فوتبال مردان و زنان بارسا
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/Futball180TV/90309" target="_blank">📅 23:25 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90308">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W3evZK2281CBnBTeIzi5ZTiv3wdHSp5MH1pFnlFuLelmBDa1gjJvtt5IoMwpfsT-yp74Zd1ejUvmDG_mE6s_C7Gh_shh02lDwWur0W4vBH7yCcPjojVxqRygOxjBWTATMec8Ouhf78WTWW12yp6EEvPiupHR4Y0TQxnmUj7ohbm06P_zmxkX-JClgVzfkGfX-uGcM2l-ZPody6NGGmpFjfnCa-nyK9QtIq47QlyF8Z7HAeQuJLjb2XFuz4N6gpXRlCVpPadSa-O3UDWR1gFfcaixDR-e-fBRUFSbWUpV5Barnu3bZR3MosHP9LDRAyWgwL4gNfUA4U-6QZPxkTpxtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
گردونه شگفت‌انگیز جام جهانی
🏆
⏩
با پیش‌بینی رقابت‌های ورزشی و بازی‌های کازینویی، مراحل هفتگی «گردونه شگفت‌انگیز» ویژه جام جهانی را تکمیل کرده و هر هفته تا دو چرخش دریافت کنید.
اطلاعات بیش‌تر و قوانین:
🔗
bfrd.link/WCW
🌐
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
💻
@BetForward</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/Futball180TV/90308" target="_blank">📅 23:25 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90307">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/84204a485b.mp4?token=FNiHnsJ9tejIJH450uUiGl_vn409uzHytbHYk0qgqTjyX5jIO5QqmNVT5k-nQ2VK7dedbh0skW7xB9bcu2QB73QsRJC9hnb5ZLxgMusDjMsZP3gSKnJsMdvqOnbtGyjgTuoZwZTA53sGOO3DmpATbU98Pg-tkJM4UE4EzJENJN-rg-3TDZ-wvRvYfYuGNFxwErXbStcGTVfBwGbrpvFV3WPdZrfW0AmAyiud-Ma4qpnJHMlBo-wzhuTA2GD0fHUZvEmomT6Uy6D2i2thpyPW1C5o1GSq1w64z0Dvk39CztF4_RpDe8NpnDPb01JVGTh-Ayl2sM7XtZpntjpsz-KdDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/84204a485b.mp4?token=FNiHnsJ9tejIJH450uUiGl_vn409uzHytbHYk0qgqTjyX5jIO5QqmNVT5k-nQ2VK7dedbh0skW7xB9bcu2QB73QsRJC9hnb5ZLxgMusDjMsZP3gSKnJsMdvqOnbtGyjgTuoZwZTA53sGOO3DmpATbU98Pg-tkJM4UE4EzJENJN-rg-3TDZ-wvRvYfYuGNFxwErXbStcGTVfBwGbrpvFV3WPdZrfW0AmAyiud-Ma4qpnJHMlBo-wzhuTA2GD0fHUZvEmomT6Uy6D2i2thpyPW1C5o1GSq1w64z0Dvk39CztF4_RpDe8NpnDPb01JVGTh-Ayl2sM7XtZpntjpsz-KdDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">امیر قلعه‌نویی به سبک لوئیز انریکه درحال هدایت شاگردانش برای جام‌جهانی فوتبال!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/Futball180TV/90307" target="_blank">📅 23:05 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90306">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fa7TUkEfvWd3apo-jfpcfv5fovppJLiM8nRVN8bJW5JGowgQHYCHeAP8JfP4UOWqAFGE-EZa9RB-45SOUGnbTZjI1SA0qWUwhT7VnD9SQ2JovCoc7BBV46N7nFEEVguFx0h_cFet_wh_g2Qmdv605plb6aBnJsVDJKSZH0Q7rz9OAdzuxTxnxpkrues-OwdALcR7gqmnnjEqGB849543FRvUtqsI7zQGmsYm6EUfx2_qnv0qw8au7i_h37ehUIcngLBADc6A3LloJhiPfCPtxcA_n8NG3Po_UmS3PO_TtzxZimocEw8RU8wVMskPyxuZWitCjAuMA87YwwGFi34A3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اندی رابرتسون ستاره خط‌دفاعی لیورپول با عقد قراردادی به عنوان بازیکن آزاد به تاتنهام پیوست
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.75K · <a href="https://t.me/Futball180TV/90306" target="_blank">📅 22:58 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90305">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/80080a6ded.mp4?token=hEuIBkcw_KhUmWPz7qRaLsyXfrT5OEsUdGRu54Yjr0b7rMu2x90GrPHAiIY4TFfdx5ELdsnrrXY_qtXWkOlZN7lhyDVvWPwObVY1mSy-00yMUW3LnZaKZXLYNVFB5g20XtWoTyflqSYcENLO3PuJvyYLSQPMRV1yEOmCLe1FSmkJ9xUqhkoVPG9h5OZo4mN_Kbl1BK6MX9Oxvg5o9K40w4RGc8KjKoLnBeiK-d9rMVJISpGstOf6AXbOoAHpFxR0P8BGaWL7UdnqTYjBwyNGzu0XQ8imHkABBVK_yNBgQ_P3XgS3KetgHyMPpilYdRlwqx9f0xk1hWjUtHMI2Hy3zA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/80080a6ded.mp4?token=hEuIBkcw_KhUmWPz7qRaLsyXfrT5OEsUdGRu54Yjr0b7rMu2x90GrPHAiIY4TFfdx5ELdsnrrXY_qtXWkOlZN7lhyDVvWPwObVY1mSy-00yMUW3LnZaKZXLYNVFB5g20XtWoTyflqSYcENLO3PuJvyYLSQPMRV1yEOmCLe1FSmkJ9xUqhkoVPG9h5OZo4mN_Kbl1BK6MX9Oxvg5o9K40w4RGc8KjKoLnBeiK-d9rMVJISpGstOf6AXbOoAHpFxR0P8BGaWL7UdnqTYjBwyNGzu0XQ8imHkABBVK_yNBgQ_P3XgS3KetgHyMPpilYdRlwqx9f0xk1hWjUtHMI2Hy3zA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جنگ هادی‌چوپان با رقبایش برای عکس گرفتن با آرنولد در رقابت‌های اوهایو!!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.74K · <a href="https://t.me/Futball180TV/90305" target="_blank">📅 22:40 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90304">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/35b0dae947.mp4?token=uSKvF1pAkWivot-Bq5-2hpjxtpgGnWhnn7FPgmz7-CiMxx6IzpO0Lo3qDBz0IYjmidLZHifeAXq9MHhdUF9hb3eTAIAd7iRnWsrsryWlaj78eszSYJtPAbQeAfMPWRnO5HDXvsFNuUAqz3L-oGiAVoNvrs15SpuvAkIFAOJYYrW6m_kvjdp_MkU9ZQDw0XUE1LEGGPo-RkjLWIrIimgkLVj1ZpL0Qg_kLZqgGzqVwg-ALon2zToeXuXg1GU71jpZCxE3DtqtRrZzm9tC8bJ4_LOM-yvx7jRU96D2fB426E9ZZf5J7F8BvcWtQzl4a5wQBa-4RF_Reie8-XPSN1mJuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/35b0dae947.mp4?token=uSKvF1pAkWivot-Bq5-2hpjxtpgGnWhnn7FPgmz7-CiMxx6IzpO0Lo3qDBz0IYjmidLZHifeAXq9MHhdUF9hb3eTAIAd7iRnWsrsryWlaj78eszSYJtPAbQeAfMPWRnO5HDXvsFNuUAqz3L-oGiAVoNvrs15SpuvAkIFAOJYYrW6m_kvjdp_MkU9ZQDw0XUE1LEGGPo-RkjLWIrIimgkLVj1ZpL0Qg_kLZqgGzqVwg-ALon2zToeXuXg1GU71jpZCxE3DtqtRrZzm9tC8bJ4_LOM-yvx7jRU96D2fB426E9ZZf5J7F8BvcWtQzl4a5wQBa-4RF_Reie8-XPSN1mJuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حق‌ترین جمله‌ای که درباره وضعیت فعلی میشه گفت:
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/Futball180TV/90304" target="_blank">📅 22:15 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90303">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/05aa244672.mp4?token=S5Bs8B989P8yOojO8GbbWbghTAEu4aaZzoJD6ra8K01MTocVPRfR5GNriR_skic3uhwocElBE1EqqOYYnz3_GdGpMVz4EdUKmDlSdd-ZM8ydPrBXV4K59ZkG0f-4WGJf6QSEVpAAoTUQaNW31H9VlYQsdQ6Mtm6gwvln6S9SMhyx1zdFjwqYXV9OnQYtIhzDKp5vI6j4WiTY3TiVykxj2JesRO6qvbmD57_AIseQ9cxdpuQs4z0j7OqdSNjXqfonY2viXSdclueiwQVJxHsVp2hJkFi_qnt3IJ2vZzCd1eaIXJ8UTkYtBpMdzzMADcfdsWqDQHyDfeGxDKlSKhGHMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/05aa244672.mp4?token=S5Bs8B989P8yOojO8GbbWbghTAEu4aaZzoJD6ra8K01MTocVPRfR5GNriR_skic3uhwocElBE1EqqOYYnz3_GdGpMVz4EdUKmDlSdd-ZM8ydPrBXV4K59ZkG0f-4WGJf6QSEVpAAoTUQaNW31H9VlYQsdQ6Mtm6gwvln6S9SMhyx1zdFjwqYXV9OnQYtIhzDKp5vI6j4WiTY3TiVykxj2JesRO6qvbmD57_AIseQ9cxdpuQs4z0j7OqdSNjXqfonY2viXSdclueiwQVJxHsVp2hJkFi_qnt3IJ2vZzCd1eaIXJ8UTkYtBpMdzzMADcfdsWqDQHyDfeGxDKlSKhGHMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دنیا برای آخرین جام جهانی شما آماده نیست.
💔
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/Futball180TV/90303" target="_blank">📅 21:50 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90302">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NthtgRDn9nWUDg6MyoVPh6chkWF7NAZ7NEvhnemShEhzp5eE-pGL7dDmiPCZZ3rvxkc89H5y-dwt7tzYHWnrSVuEwaL47BX7lIbeaPQye519qYfEf6oSjxVZ87PfdhZZ8G0a0StRSG9Wdpwf2pdQp1QjYyAStrgHTW1iAiL_uI_I1zn0cD1bWS7h6ZSAWwrcWTQoyI5DAoWsZ6ZfuGjq-Ab3QxU8BcpcUFax5BuYKHNulNugRGcptvgIVtCdIXqgmT1CCFxzjxSi7Q7hudozickn7Owk7ngAxR7iuK_gPYivvugLt9EfLBkH2pwMy3sOy9Fd-7b5EAPvxqfhVH7bxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#غیررسمی
؛ آنتونی گوردون با عقد قراردادی به ارزش ۷۰ میلیون یورو از نیوکاسل به بارسلونا پیوست
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/Futball180TV/90302" target="_blank">📅 21:28 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90301">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b45e4bbf26.mp4?token=aJlbmzh7TI7Fi5QDcaeo4kDJFWn5YxOOD2Wmt_sOfYprhHsGsi_lJhElp_2Aeeg-V02zOzCHSw0hPw80pTaIdcVru0oVKHzQa2k7S33ppp3DbmJE0_Yl2spt24KbLTZID2AfXZ_I8obLPmAd89wL0ihuk3IA0RdpUnSNyJN2gUqEM7OdIY9tPCo_dDQFwtVK21_g87zfjlznMeGQ8f7afJixKBUS628xpDgsgloZMD24veK0Jf2_cY25Ze-IdgH-gK0FCcVTwReD3VEbSiglnAJc8f43htnM6kJOKu__tLktHs5TiKfjU3SufmwJgnM6boiVZ5bCPds9PR_R1zob_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b45e4bbf26.mp4?token=aJlbmzh7TI7Fi5QDcaeo4kDJFWn5YxOOD2Wmt_sOfYprhHsGsi_lJhElp_2Aeeg-V02zOzCHSw0hPw80pTaIdcVru0oVKHzQa2k7S33ppp3DbmJE0_Yl2spt24KbLTZID2AfXZ_I8obLPmAd89wL0ihuk3IA0RdpUnSNyJN2gUqEM7OdIY9tPCo_dDQFwtVK21_g87zfjlznMeGQ8f7afJixKBUS628xpDgsgloZMD24veK0Jf2_cY25Ze-IdgH-gK0FCcVTwReD3VEbSiglnAJc8f43htnM6kJOKu__tLktHs5TiKfjU3SufmwJgnM6boiVZ5bCPds9PR_R1zob_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چالش جنجالى و جالب مجری با محمد نوری پيشكسوت باشگاه استقلال
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/Futball180TV/90301" target="_blank">📅 21:25 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90300">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KInlT9wEkb3vaIuEqlinV4EzZw_Hq53bRXbwjQ4-uiVjx0xxQkqplT2cvI9ULRBd0l-vxMhaoea-A0OWeL_iwFH2gZ7rCRdWk9SPZx6NLloWAp_dCOUAJyaj_keM0Lzh5q7HuFODt_Rgu5_lpapQHymSSoxptu-hHePMIaZDA2n03jiu9_9z7QD9gL5745wyaehpS_ZLgkHZDctw7kDE_T1IXbSeDjVKquHUYiW0veP__StD2Wp7lOD33S5mQtewaHkz_hT59EIRfyYGd1MkYOm3K26AKRD3goHqdK1FFGf8x7Gh6yYdu26GGKUl__BzfEbERiZXQVjOozBClsaH8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شات‌تاریخی از مراسم جدایی الکس‌پوتیاس ستاره تاریخ فوتبال زنان بارسلونا
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/Futball180TV/90300" target="_blank">📅 21:02 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90299">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gVUM-Jy9VWJgzw1Fr7Bdv8bWjBGjkbPAYS_zczT9Wh0cNOevmqx-5CZnO8Pq0p8F-O3pleb7JG8_ftwhbGLxxoyOdmEYK2bPdGcM_4XEvkKZxu1-vEphuFYSsXhbmGNo7_sMLPW_wY4gWpECaFbsRCvLQdBpejQoyhUzaMAyWO1_6rx-tkxQu9Xc5TRCSNBDxhGRg4yfR4rF7jd8D9_2Io2xE7fgCI5W2ldq8xcjqdYo3gQiKjZjU8UfuoQBfii_BVwhsjoNaL4dwfF3u6_oE7Wu8NVBZPxhPGH29sXe3LfTv1SbWFJMfeBBVXh46mIdB7VxVbrTM9sv_TWtU3_OCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قهرمانان تاریخ لیگ‌کنفرانس اروپا به مناسبت فینال امشب این‌فصل از رقابت‌ها
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/Futball180TV/90299" target="_blank">📅 20:35 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90298">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57a28e2aed.mp4?token=pVF1O8YNWNx5oGtz249NF-_wpSku1kW4dPFXp4WTYoIVkyk1sru5KktfV6bSwPwmaGx7ng8IYot8J2JHpVoxDk5e1IZcW5a1Z1w390n_p2FEI8HaKhqvQ-u7DVn3_4OTuoEXvXWtl19BiROn_alqAbrK9PEmtGD3sTjyaGeJ0rnwqDWKW9elSm1tA6Bb9u6rw5AAY0z8SfPLT02zupw1q5bChMntp4Miyf7jfwsZ2NEyP_3ihHEsnYPnkTDRfKlt4qoC9ucszt3ulz2X_WWRTH-g4qVlg9KMTyplj1CEEHlz3lvj-pGM2k6BQJ_C3dbXQYh_PR7bwJXdVunGp1slnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57a28e2aed.mp4?token=pVF1O8YNWNx5oGtz249NF-_wpSku1kW4dPFXp4WTYoIVkyk1sru5KktfV6bSwPwmaGx7ng8IYot8J2JHpVoxDk5e1IZcW5a1Z1w390n_p2FEI8HaKhqvQ-u7DVn3_4OTuoEXvXWtl19BiROn_alqAbrK9PEmtGD3sTjyaGeJ0rnwqDWKW9elSm1tA6Bb9u6rw5AAY0z8SfPLT02zupw1q5bChMntp4Miyf7jfwsZ2NEyP_3ihHEsnYPnkTDRfKlt4qoC9ucszt3ulz2X_WWRTH-g4qVlg9KMTyplj1CEEHlz3lvj-pGM2k6BQJ_C3dbXQYh_PR7bwJXdVunGp1slnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمله عجیب مجری پرسپولیس صداوسیما به سروش رفیعی: پرسپولیس باید یقه بازیکنی را بگیرد که حال نداشت بازی کند
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/Futball180TV/90298" target="_blank">📅 20:10 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90297">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ac28b3311.mp4?token=tLIN2-KIzc7z12ZQb0uoxK9aGOuApf9JRddMMx_edPO1CBwnRx18lCbMaeswiOeRkcCppGjD7aWlEWDq_fgWXQtp2C8kLfrr2U_spJTtBLZEDls6bzJ9coQrcBBuYPeIQbbFzY5paKUaMkG8rJheZE9ntxyCeI3QZC4wMtYnmp8VsEMp_AGheKWKcdpYgVacvMnwDZW1gATl4GfeMOp582tdNr7r4-PNpA4vtOfKbqZSllCrPtoIHTZXgqN3qoDJzpAvHgBrDrpR2s6JAfENqbBR9wVMlR2CgnEqAluIj9Ganqj8D0WzRZtgDlau8Ou96gdeLYQF4Ovu0HZv2ZB3aA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ac28b3311.mp4?token=tLIN2-KIzc7z12ZQb0uoxK9aGOuApf9JRddMMx_edPO1CBwnRx18lCbMaeswiOeRkcCppGjD7aWlEWDq_fgWXQtp2C8kLfrr2U_spJTtBLZEDls6bzJ9coQrcBBuYPeIQbbFzY5paKUaMkG8rJheZE9ntxyCeI3QZC4wMtYnmp8VsEMp_AGheKWKcdpYgVacvMnwDZW1gATl4GfeMOp582tdNr7r4-PNpA4vtOfKbqZSllCrPtoIHTZXgqN3qoDJzpAvHgBrDrpR2s6JAfENqbBR9wVMlR2CgnEqAluIj9Ganqj8D0WzRZtgDlau8Ou96gdeLYQF4Ovu0HZv2ZB3aA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">استقبال شیک نمایندگان آمریکا از تیم‌ملی عربستان در بدو ورود به این کشور برای جام‌جهانی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/Futball180TV/90297" target="_blank">📅 19:35 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90296">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e4496fe5fe.mp4?token=OCoLVxE1kFCLVhEDIonDcm5Wyurqc82uMLd1l-WGuBbcWWNVUt-zZGpSCAOJKd6MWbKHPbpvtMX2YlRZiuJ0_8USV1qxsKv9tXo1e3luXRweHOuCo9_p92nPwOodQYX5zVxA2nHk55ZhE1Rz0hGjK-Fp5mJQErGsYX42QCOUXtq17yHRxGbz6O3EpSlKpAdOfkqd-QC9BshK0O2sbm0b8Bll76w-i0DltK92n_qOtN0X89JmdrT3mGww26Yvzvte507u5mPyK6AI-RlE8OuZRW2jmSWBigDAkIZfjk9HKcfP0FtSH_8MY6YuWMdfmyE92NHpHbdhStxeimpTVCdMzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e4496fe5fe.mp4?token=OCoLVxE1kFCLVhEDIonDcm5Wyurqc82uMLd1l-WGuBbcWWNVUt-zZGpSCAOJKd6MWbKHPbpvtMX2YlRZiuJ0_8USV1qxsKv9tXo1e3luXRweHOuCo9_p92nPwOodQYX5zVxA2nHk55ZhE1Rz0hGjK-Fp5mJQErGsYX42QCOUXtq17yHRxGbz6O3EpSlKpAdOfkqd-QC9BshK0O2sbm0b8Bll76w-i0DltK92n_qOtN0X89JmdrT3mGww26Yvzvte507u5mPyK6AI-RlE8OuZRW2jmSWBigDAkIZfjk9HKcfP0FtSH_8MY6YuWMdfmyE92NHpHbdhStxeimpTVCdMzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حضور نیمار در اردوی‌تیم‌ملی برزیل با بالگرد شخصی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/Futball180TV/90296" target="_blank">📅 19:23 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90295">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aFKqbup26FCEMHhtNHLFItxy8ExxXhmfrMcln3jTN4_4RS1Q7nDH3C2EWQNpqHgA9mYLe22lN09uf89PPIyGOouBvHYYB2fzSdqcQkzR1aY3o2baErX0t64NYBgWXHvfM6bX8ks7C5g38Zv-umLB1uSEzQcxHp2raifuG2nuPQPfkoDmDflk1IV2pB9he92PYdUwubtjAwcGsLmXnBJDT_wjq37V5-OoYD2eXsoksb0l1tKQZBFflbqttJrB1nemOfDaMLQLybXzBclPQUY0WRryoFMI1ru6hKv6EYtFLdALTsvRkVFNN6TgH0lu2Ms8lpsOdg8lH0cIIjQRpScOXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
جیکوبز خبرنگار مطرح اروپایی: چلسی برای فروش انزو فرناندز درخواست ۱۲۰ میلیون یورو از رئال‌مادرید که جدی‌ترین مشتری وی است، داشته!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.62K · <a href="https://t.me/Futball180TV/90295" target="_blank">📅 19:15 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90294">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c0fba26b8.mp4?token=vrb9jf-euJTJmMdkV-W2Icv_G5X274ea1ttQZIQVvcHVFldY9-IT3JGOHoWsHnr1T0EfL3kkTfFjBr5aCa6y631GFDHRyc2pbR5IAhloHlQ8vzb_KSQSOiPUydEFCnlV_gTnXKspEBbScjFiqKlVXtom7EahVwOA69b1NifNEP9sm3_mchE2KuSVmMK-UJQopZegTnvZOs3_YnVqlkWOKcJtqIEaylPwFpzEtqPR0H83C7e1koUAWxj4ZoUczP-zO8PCuXv15VNbHrYWk0R-WFS2fha4yFMwDCvC4UGe0k4niVMz1OhA1jHm1lX74mM_-deA7uS0TgMSSzDxULBrs1gZtWtZ8nDHuuYwIHWjXkXeEKcCIhpf6x7JPZaoy4C9JGM4uoRUVeZoMM_WG0z1L7vUxGa4gU1Fu1FM-QLLxzEonI76swZv2KLtf13TeWXc1Hq2oufS2Ls7hBCs2_XsA69KCBE02FSjJI4xjn3U3EZAtLP3Y8cerAyLKEeiK4PsNg_Fgdv-PPLIkmyO_3W_ltlohb91PCpalX7R8BBIT5WMkEmMb2iztj22sykcLUPdDMYJzlwRej0ESHmvAFr6_iNzS8JBZEvqOgYRq9BomicIA4JwRJQsJZN4R7fMBcswWaVYRUyH8NaWxtQ415UEdDHwDus5CuW3nQoW56vewYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c0fba26b8.mp4?token=vrb9jf-euJTJmMdkV-W2Icv_G5X274ea1ttQZIQVvcHVFldY9-IT3JGOHoWsHnr1T0EfL3kkTfFjBr5aCa6y631GFDHRyc2pbR5IAhloHlQ8vzb_KSQSOiPUydEFCnlV_gTnXKspEBbScjFiqKlVXtom7EahVwOA69b1NifNEP9sm3_mchE2KuSVmMK-UJQopZegTnvZOs3_YnVqlkWOKcJtqIEaylPwFpzEtqPR0H83C7e1koUAWxj4ZoUczP-zO8PCuXv15VNbHrYWk0R-WFS2fha4yFMwDCvC4UGe0k4niVMz1OhA1jHm1lX74mM_-deA7uS0TgMSSzDxULBrs1gZtWtZ8nDHuuYwIHWjXkXeEKcCIhpf6x7JPZaoy4C9JGM4uoRUVeZoMM_WG0z1L7vUxGa4gU1Fu1FM-QLLxzEonI76swZv2KLtf13TeWXc1Hq2oufS2Ls7hBCs2_XsA69KCBE02FSjJI4xjn3U3EZAtLP3Y8cerAyLKEeiK4PsNg_Fgdv-PPLIkmyO_3W_ltlohb91PCpalX7R8BBIT5WMkEmMb2iztj22sykcLUPdDMYJzlwRej0ESHmvAFr6_iNzS8JBZEvqOgYRq9BomicIA4JwRJQsJZN4R7fMBcswWaVYRUyH8NaWxtQ415UEdDHwDus5CuW3nQoW56vewYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ماجرای بازداشت نیکبخت در پارتی شبانه؛ این همه آدم معروف آن‌شب آن‌جا بودند چرا فقط چسبیدید به علی نیکبخت؟ گفتم نفرینت می‌کنم یک روز جای من زندگی کنی ببینی جنبه‌اش را داری!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.51K · <a href="https://t.me/Futball180TV/90294" target="_blank">📅 18:55 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90293">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t0SSMvhZhbDB5Y8hGGqKYfaw-yOoL5cEk806J1CQYsZZcZyZ26Q7g_x7TYW1igkQALMXOES2XWWCsGixSL9aBsqKEnA2XkFgUsGY-75vcvxT02O8PsETQv1m5HzIPHqQd4D3QYXzVD7teN-7aNCg8jlzBzfwmWSpU_F25M14n3CRca70BKYQ2cRtMVy2dFtjRlybZdZQhN4lqy7PVV_MZApQrj-iEtn6se_JAaRhcSfNEW9jU9rVp47iDMhO9BXNgN_4hsAQMHnsBeDIIys4E42dkEVwYaTbLIIpmgqXHdR6_8gkNtF89I2MTDH3QJP1Hg-x1liN_3lPD4sG22k1SQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بهترین هتریک‌های تاریخ ستارگان فوتبال
😂
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.36K · <a href="https://t.me/Futball180TV/90293" target="_blank">📅 18:28 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90292">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">⭕️
تا حالا بدون واریزی روی فوتبال ها شرط بستی؟!
🎉
500 هزارتومن بونوس رایگان فقط با ثبت نام بدون هیچگونه واریزی!
💳
شارژ سریع و امن با درگاه ریالی ، تتر یا ترون فقط با یک کلیک!
⌛
پشتیبانی 24 ساعته
💖
تنها سایت مورد اعتماد ما با بونوس های کاملا واقعی و رویایی:…</div>
<div class="tg-footer">👁️ 8.93K · <a href="https://t.me/Futball180TV/90292" target="_blank">📅 18:28 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90291">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fBMN4k15SFfLweXvwG9RYaJpfHf3kmxyFLWt5cA6LlerM9ySF4SbfXHTN_78R6QiTAtWgw19zk-Uxc4m07J6XQU4OhZevCT_rmLX6567bjDw7Pl28zuAughMhDfUyvPl_1YMEg9E8fK9eVcXrxvdBaSTv43F0ppGo4FlB6XYxDI1G9Ve7TqMovzN8NfnLg4KrCWulUMbdISn5PoYKzlLrSt6WYXd1dabOmB5eKaDboG2w-73cC-HCwWsxQ-MNCOsuHZbQnGgEhWu8vz9RwW84N3pyB9gF6sWS-gdbtNpqsNuzy5j2Lijl5nIgf_CckMAYkvPKQE1Fu-UEBd7zyu39A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
تا حالا بدون واریزی روی فوتبال ها شرط بستی؟!
🎉
500 هزارتومن بونوس رایگان فقط با ثبت نام بدون هیچگونه واریزی!
💳
شارژ سریع و امن با درگاه ریالی ، تتر یا ترون فقط با یک کلیک!
⌛
پشتیبانی 24 ساعته
💖
تنها سایت مورد اعتماد ما با بونوس های کاملا واقعی و رویایی:
🌐
Winro.io
🌐
Winro.io
کانال بونوس های رایگان
g6
📱
@winro_io</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/Futball180TV/90291" target="_blank">📅 18:28 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90290">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pvole0AeioHUM2VFs_H-93hf79pwW7dpwti0HVoV543tYFGJ7s7uxgflfjmUepbspFPIoHU30Qi1J--CnlLFgtXl9QknFW4wwB5CUzG59IFayK9b4RvElzGAVgfgyAf0dgXHUNslYSa95LpO86XNPTwAhaZNIT6nJPAJ9Q9Va711hGbt9deppjyGqgL89D0u0m7h6m1FemLLsdw3mrkS6t4tSOPl0TS_mucsaGQCJVpuWNb_K_NjsXkG1sGEwL1ZxCjG0X-_lWjmfjdhtCkEnp_y1NsSlUCFaQ2-t5EJEbTNEyJAijXfJSYK3nWZe7NY5GQzTXSRxVSGDRgfjMiXZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تمامی قهرمانان جام‌جهانی در یک نگاه
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.28K · <a href="https://t.me/Futball180TV/90290" target="_blank">📅 18:05 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90289">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mfKfgqlvssxfrSbVdEELt49SczFcHh0fkoZgByIiQY2UpgoVA1kieEvwu2CzHI_Ph5EIjxkEi5f1JyIk289uwAB6ATxhmEUx5ZKq10qzjWsbmSWXI9y_vamUp20NYg50aWOpNA-E0askcoYZizlfJyryrhRkPoLuXeL9HtOFarDTxFcZLvP1n0Y18NRzuDjxB0WKp-Pl79XK1-xSXhALoDq3-6CgyiBdNXV69s9Mv1btjk3_nKyG117MmxwIbr2aCtvCg5TL0TlO32-VObsnygkQOA-UsqQAJOqCbjMCj23kGaqWCCV0nBka9tsuoDiAlXBd4x8mbO0xk-B2XUeaqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
به گفته اکثر منابع خبری، قرارداد آنتونی گوردون با بارسلونا تا ساعاتی دیگر نهایی خواهد شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.81K · <a href="https://t.me/Futball180TV/90289" target="_blank">📅 17:36 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90288">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rA5KIbrSEb7CAJAAJokutGxCE8QjdGoiXf_XKZlm5AVK05JdncnQAweIVXqOSP-SDo88sZCuPn7mTI73RrjRznNB3j6JGUuDVEAmCHpICT9XucQD_nUXJD6z-u8FuXrOTPjPtOYxbyTjj8PjeliJZwsYa0LtNkZbrQZROzPexBFjK_iaSQ0xjB21SelEJzI50-NzFkGUzTSWUeb16buE7GaGTfarxMzvRKnqHaaPny1JEwH-WIoyssxeUAnuoOS1CC0hxTZZ9F5S7SItsVR5CCD5zo_dZm4i9L_GUbv-CQ5iROELcTqthSiWZJ5wM4nMOKkQdoM__cseZGy_ID0xIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقایسه میزان بازدید پست معروف جام‌جهانی با پست اخیر نیمار در صفحه شخصی‌اش
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.64K · <a href="https://t.me/Futball180TV/90288" target="_blank">📅 17:15 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90287">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Va-PmgHHGSZGWBCEtzn-KeQBpLR9GQeCWRE6BS-GprvebhNf24VzRR_vjCuaLCAtaauHk4zu9HvQzNW12LZmVMMHEDhc5jafv6zVGOAvbPmyg55IwLS8bMq3ZnXF6T24yG-FM_dnatSjmy1n93hATgpJWHbtTQEhEQrzgkU6o9PTtAFnmbdc_g3Ltgm75sU7-WX8H7lnUmigrJHnBOlp5hrO3aHGlEuxMfW10Drwkcv-wmEwEYOVS0XZi_pjVFCckwAzDOm8dla1W8KX5HEdWYRUpwEzeWXj2eJFMnAEqsmz_AE6MxfHlSpdkZ6RpAC9VVjunjTeI82EnHsrLbrekA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
جرارد رومرو: بارسلونا قصد داره قبل از جام‌جهانی قرارداد گوردون رو نهایی کنه و سپس به آرامی در طول تابستان مذاکرات با آلوارز و اتلتیکومادرید رو جلو ببره
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.84K · <a href="https://t.me/Futball180TV/90287" target="_blank">📅 16:54 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90286">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/30945cae67.mp4?token=GbUPOz9wuooEsWsMkf3jQJ_PiyPVEA3jzUb9sOmNOfD8c0llqL6mzTcffhiGV8-ItErmkTf7SM7vbFB1zG2ZA9hdKXf5irPZwb_qaOy4GVubKjF6je-PI-U1U8_FBHmy0eEJ05vs-O9YsSaE2sqEIlbOT90zmrpu1cJP3Onb5qLFJfCNiebZC3bZn5Ysv34mdfS5W7B2EW63dhA6Y7QH-a-NphWNGGNdcDEyOXEB71JL6EGzb7NshcgcgRXebDkI-6Fj6E9a45rkhsg4eJcS8n30CnKnIpiwtREXBxDTG2DPC9KRaMAvUTwMoz4sCWODJz8Rez7nt7QO5FLAWUqV_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/30945cae67.mp4?token=GbUPOz9wuooEsWsMkf3jQJ_PiyPVEA3jzUb9sOmNOfD8c0llqL6mzTcffhiGV8-ItErmkTf7SM7vbFB1zG2ZA9hdKXf5irPZwb_qaOy4GVubKjF6je-PI-U1U8_FBHmy0eEJ05vs-O9YsSaE2sqEIlbOT90zmrpu1cJP3Onb5qLFJfCNiebZC3bZn5Ysv34mdfS5W7B2EW63dhA6Y7QH-a-NphWNGGNdcDEyOXEB71JL6EGzb7NshcgcgRXebDkI-6Fj6E9a45rkhsg4eJcS8n30CnKnIpiwtREXBxDTG2DPC9KRaMAvUTwMoz4sCWODJz8Rez7nt7QO5FLAWUqV_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از حواشی بامزه مراسم خداحافظی باشکوه پپ با سیتیزن‌ها
😂
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.75K · <a href="https://t.me/Futball180TV/90286" target="_blank">📅 16:50 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90285">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c42b3ba26.mp4?token=YcRGzW3kIpSaayVRHoVGdD2QGttu0cN4pRufxi3AqkBUZfvxCk0bIhiKTESCQCZ3WT-Q2CZOdoznXN9nMYnfFGx4mBphn7GW3dp81X6ocfsVWvVv4bJlFwMILNxWQKVFPh7qZ8fAhrNfRkkWocNF7hewzMKVp15RGnsBzOsX9V32g7SW40zH7E8oJ4ox8fVe1V1SW7W1nk2E0t-2M11tGKjCzfEkMTwN00WdrSAv1pzVSOWGivrW9eDb7nTepqOMJ21a8r9Q54vXk4rZ98Pnz5MedJoNO2nOc7i2p74zNxF1-yoKoDmOPrgxnIj6YdBzlUMhGGS_1ti5iQMi-H_lKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c42b3ba26.mp4?token=YcRGzW3kIpSaayVRHoVGdD2QGttu0cN4pRufxi3AqkBUZfvxCk0bIhiKTESCQCZ3WT-Q2CZOdoznXN9nMYnfFGx4mBphn7GW3dp81X6ocfsVWvVv4bJlFwMILNxWQKVFPh7qZ8fAhrNfRkkWocNF7hewzMKVp15RGnsBzOsX9V32g7SW40zH7E8oJ4ox8fVe1V1SW7W1nk2E0t-2M11tGKjCzfEkMTwN00WdrSAv1pzVSOWGivrW9eDb7nTepqOMJ21a8r9Q54vXk4rZ98Pnz5MedJoNO2nOc7i2p74zNxF1-yoKoDmOPrgxnIj6YdBzlUMhGGS_1ti5iQMi-H_lKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آرتتا و همسرش در جشن قهرمانی آرسنال
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.53K · <a href="https://t.me/Futball180TV/90285" target="_blank">📅 16:25 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90284">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cmopcfy2z_W9NwQ35C0IqzQu0sE3GKuILoD2OaYPkRRppWfiH9aMVMeFGMk6M5uq8VT5YtqjpOuWToC93AtGpwqvja156p8WEaA5E7sEhgv00VvjInvl7WQ6GzGFS0-WkzLcKquyauKTlh-qf977MHkXnUYzDgE5l0488RS5esBjkDOurUVqmQWTS0VIvPneuxfmg7-lT03EAOpZHk7ob9tHa3AV_zQyCLMrX8mGvgZJN3molwmuiGAOSU_nZJ-_x8bY0e_H4u_ry1MjDauiPyrDow4PghnWcU3AiEc0NHOJuz-zqdvRRxZZkxkipEGN46RuiFZOn-H0zidKOnYIeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
لیست تیم‌ملی هلند برای جام‌جهانی ۲۰۲۶
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.6K · <a href="https://t.me/Futball180TV/90284" target="_blank">📅 15:42 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90283">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bmw1lNhlyHoxSYNA8zl41erepmwXjKVABZH5NjjKvgwmZrUtlfHIC02l6h2bUAJrlQaxih5IphriUd1vjBxiw5N11exnAYxNkMWCACG7WcBAZF0B4zE-q3-F-fxWX50jw1yOWPZad1ojl5EKfxS8RU1iUixCJKbrDG3-pNstFxi8Z7V7U2gnRgpIaz7WOBVp0H8D0G6nSCUwcmPFZbYjhFSiPPWRZ5de8pMBBQBkrFmqU1fruUcU3yvFtpJ3jnYfmSY9eSczuYOMsBZq6DAfXxnuCwH_ElZ0nhWVYEjVNUof2lrIGLszYW44Wc8MPh7Pk9SadI1M6gzgCWDQGqbc4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پنج سال گذشته: کریستیانو رونالدو ۵ عنوان کسب کرده است، در حالی که لیونل مسی به طور چشمگیری ۱۳ عنوان به دست آورده است.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.01K · <a href="https://t.me/Futball180TV/90283" target="_blank">📅 15:37 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90282">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SBfpe9D6iSoWTRBslIJwWa3ZgW4_M-aNJh0K_iCdmJjpj2Hlz-kxs6Glw2v0ulmHX1VKyxRTtGF8Lxni9gxRWwqmMuMNWHeOdxec9YUmsIt6V5_jn0kFqco0NOeXMiqRb-O65CmjMVm6XV7yBD6jJlwoJIw97A-Gx8o7UYRN_yQS8b1b9Opdqu2vjHBacacSXFvLkLNA8sLS4-hpiTPHXCMcCUCHVU9A_B2zzokPG6UnVItw6k6oUEKyE5zt3RCPSst2vHz8CMPkczDkqMUL1NE8O8TM28RGcFwZEfB3cEsBGyewz23MTjCe83E8fp3HlNLcB63h57rC2cB2EJ4uvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">180TV
🤩
🌐
دوست‌دختر جدید دوگلاس لوییس در عرض چند روز به ستاره اینستاگرام فوتبالی تبدیل شد.
👙
طرفداران نه تنها درباره رابطه عاشقانه این فوتبالیست‌، بلکه درباره عکس‌های نیمه‌برهنه این مدل ۱۹ ساله با مایو بحث می‌کنند.
1️⃣
جذاب‌ترین عکس‌های دوست‌دختر جدید این فوتبالیست در کانال ما قراردارد</div>
<div class="tg-footer">👁️ 8.72K · <a href="https://t.me/Futball180TV/90282" target="_blank">📅 15:37 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90281">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">آخرین وضعیت بازسازی ورزشگاه آزادی؛ 3.2 هزار میلیارد تومان دیگر بودجه نیاز است
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.93K · <a href="https://t.me/Futball180TV/90281" target="_blank">📅 15:35 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90280">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bbe3da6710.mp4?token=PyY4CFc5hOP5Jm2klbwah4LaQnsctRsXZNi5qAvB-QyjgFhcPx1FUFJWUWwq-FZ47CYViU_1U3vz9PxZqxR3JGsSdcjcTOM8u-FsyP20slkobce4b6R3RGuzJHP1ysSQjXPTW1PWnG1qJBCvOzqLbZ6jlUsB5QdW4zbZYDiX5xesbJwO3madtPj7AgN5wVPLWWYoN98flyTwX6OW5ejd9T5rYwOp4tpV4htgunCggjZ7OWEYN0DMNbTSvuGzp3-BG7QTMtce_EyFC8Gpuz1-5v1alHctItZSu1TL5yd3msOSiuoACumqk0HNvf1HuE5XinYyzsLd7JdJv8i17MKiAB5olTTcJ8jkjtnGwLNDDe2OQ4f3ZOF4liWNhf2XaMpumO6akoeCXcMnb6cbKo4aTuHWlj6ua5X75g6Vj1RW0pKvbd36q4NeU7DWM1bYCbfOXHgNeLYIIl6GVKILXL9yjyKPlShYL0vD2TFuFediBhmXzMz8HHn6-cyJfE31pcw39PgWC6qOCUNP6LHIQppLloBbvp9Xg2pw7WYRvyVBsRujx1GP5fO5JTGnEdgR6dncUuyrn6Sh6FzjjAxWXudJBbSwRqaTP7ca-HJkRc2650O8-gZaulk_b2SiizyxOx18OdVCvpAZB__nbcQDXG5-Dwt5NZxU0ylxRIiJM7oBRKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bbe3da6710.mp4?token=PyY4CFc5hOP5Jm2klbwah4LaQnsctRsXZNi5qAvB-QyjgFhcPx1FUFJWUWwq-FZ47CYViU_1U3vz9PxZqxR3JGsSdcjcTOM8u-FsyP20slkobce4b6R3RGuzJHP1ysSQjXPTW1PWnG1qJBCvOzqLbZ6jlUsB5QdW4zbZYDiX5xesbJwO3madtPj7AgN5wVPLWWYoN98flyTwX6OW5ejd9T5rYwOp4tpV4htgunCggjZ7OWEYN0DMNbTSvuGzp3-BG7QTMtce_EyFC8Gpuz1-5v1alHctItZSu1TL5yd3msOSiuoACumqk0HNvf1HuE5XinYyzsLd7JdJv8i17MKiAB5olTTcJ8jkjtnGwLNDDe2OQ4f3ZOF4liWNhf2XaMpumO6akoeCXcMnb6cbKo4aTuHWlj6ua5X75g6Vj1RW0pKvbd36q4NeU7DWM1bYCbfOXHgNeLYIIl6GVKILXL9yjyKPlShYL0vD2TFuFediBhmXzMz8HHn6-cyJfE31pcw39PgWC6qOCUNP6LHIQppLloBbvp9Xg2pw7WYRvyVBsRujx1GP5fO5JTGnEdgR6dncUuyrn6Sh6FzjjAxWXudJBbSwRqaTP7ca-HJkRc2650O8-gZaulk_b2SiizyxOx18OdVCvpAZB__nbcQDXG5-Dwt5NZxU0ylxRIiJM7oBRKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رمزگشایی سامان آقازمانی بازیکن سابق پرسپولیس از علت اختلاف با قدیمی‌ترهای باشگاه: جوان بودم و خوب بازی می‌کردم برای همین از من خوششان نمی‌آمد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.94K · <a href="https://t.me/Futball180TV/90280" target="_blank">📅 15:35 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90279">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kNpSGk4BWGsS7Pk3V3eUKTbQHNuN_zO8W2jPVbqG_PEMmazCIblg0jignzwbY8IZszfZlq9ROGYKVvkO2NAqZET_kpt7eGr3yxlpiykcaJAeQD5GAD7QHgX4oPP_cuEEZ-FLgaYSZ3JlJVO9MuqOY-KepD8SILjslv91O_18lBGiAPgv0JshvciEr_Z98Ud-cv5JCjOz4gVxLyUzgqUsSryyH4yPxCmda7ulI-RpJ-m9yx-RGKNQNSkZinnUyeKe9RgeS0e93GZiDJXrwQIpitcjB-WTwVFSsUmZ7N-2r2SWUBfAT24rPLEinrEAmitTQNOWbU8yIfwE6bSTD_zqBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تیم‌های ملی که توانسته‌اند دو بار پیاپی قهرمان رقابت‌های جام‌جهانی شوند؛ تاریخ برای آرژانتین رقم خواهد خورد؟!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.99K · <a href="https://t.me/Futball180TV/90279" target="_blank">📅 15:10 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90278">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2cbec1c58c.mp4?token=SQvk9eQGyCncIj12aRAT2iTzFukg00i8L-FvIp76-WCrVHbEnUIGRTLzMv5ucAC9k80wV6YP-fRlUoAx0TPPhTY_GOjrbKC3b7FlCcotzRxtJGJPu4SGl8oL7hQuKwi_zySYqcUT8kszcHMKbJnZ-ohgSy-m2ubsKxJTjedRnZ6GDIXzL4xG-8dFwFASN-4cZo2-ZbdpTv1sUZjZ9LCM_-ylQUfyEzYH-04hyaYTtJpkwz4h_X-aXpciaKK3CZ2qooQva2W9iqODomcgWnJdyyIJPNco2x9qObVfjrMfU-4_OMQUfOQyBHNfYyIoaC_DamKSTVRM9ACR7qRUIUitnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2cbec1c58c.mp4?token=SQvk9eQGyCncIj12aRAT2iTzFukg00i8L-FvIp76-WCrVHbEnUIGRTLzMv5ucAC9k80wV6YP-fRlUoAx0TPPhTY_GOjrbKC3b7FlCcotzRxtJGJPu4SGl8oL7hQuKwi_zySYqcUT8kszcHMKbJnZ-ohgSy-m2ubsKxJTjedRnZ6GDIXzL4xG-8dFwFASN-4cZo2-ZbdpTv1sUZjZ9LCM_-ylQUfyEzYH-04hyaYTtJpkwz4h_X-aXpciaKK3CZ2qooQva2W9iqODomcgWnJdyyIJPNco2x9qObVfjrMfU-4_OMQUfOQyBHNfYyIoaC_DamKSTVRM9ACR7qRUIUitnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انتقاد شدید صداوسیما از دستور پزشکیان برای اتصال اینترنت بین‌الملل!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.5K · <a href="https://t.me/Futball180TV/90278" target="_blank">📅 14:45 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90277">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/083cb252a0.mp4?token=dYpNHU132rEBmL_3jPfM6hPDhgofh-5yl4MI59PYmO2_2GiopfOSAh03DxmB83b-TAGBMl03vSDf-dlZW25mIQpBuzNe0r-Y0qhw9fJPO562G5MrxG75BlYdZNyvpVJ1AWWygXBI5kLbWwq4b8tseSEqUP_Ukys06l-1Aobj9g8LJoy11xZbUUbJExjdrKIIzOf5KteiO5FO5RLaKDfawCSNXoDoO2NSpUza1P_WnATqehoeEbgYI4BtDanYn6lL-i4qAAMSDjr2MKRNmBnByBEE4wr0okwVpin3zleZfg9pbjkhEot-x0T4xTrxi9RNvJUL84xi6A2H4gtj_tuSkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/083cb252a0.mp4?token=dYpNHU132rEBmL_3jPfM6hPDhgofh-5yl4MI59PYmO2_2GiopfOSAh03DxmB83b-TAGBMl03vSDf-dlZW25mIQpBuzNe0r-Y0qhw9fJPO562G5MrxG75BlYdZNyvpVJ1AWWygXBI5kLbWwq4b8tseSEqUP_Ukys06l-1Aobj9g8LJoy11xZbUUbJExjdrKIIzOf5KteiO5FO5RLaKDfawCSNXoDoO2NSpUza1P_WnATqehoeEbgYI4BtDanYn6lL-i4qAAMSDjr2MKRNmBnByBEE4wr0okwVpin3zleZfg9pbjkhEot-x0T4xTrxi9RNvJUL84xi6A2H4gtj_tuSkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محمد نوری پیشکسوت فوتبال: سردار آزمون را ببخشيد. اشتباه كرده و عذرخواهى ميكنه
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.71K · <a href="https://t.me/Futball180TV/90277" target="_blank">📅 14:20 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90276">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ej2EalEB60K3BsHpYQu0RQL_oSLmBHzcafxO5qbYHaS_B8ZQqn-lswlnOEiGay2SFdMhedqve1Wbttcyyx7H7GqipeiKXatNG2jbeBgm0S_NJSRcDaSFxWjMxPM4gEr429KQE3-Jb9EfFyj9Vd6ckRRzv-sPQBiN14_dyLGVL2S1mLKJQpVUFbS4h4lA55BxnPVM0OlnaY_1NO4XoQv0mjXaFXVAqT_BD6gCP1--0yunDfDoVl4lMfqH6oxY6FKX4ogaoDpFIUDuKnMPAK5zKAUnMJEgesedJz0L6zOO3NDImqq9WAAi9Lf62ozHSoqNRFmRuBCzzT8XN84ADDMQbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آخرین باری که باشگاه بارسلونا ۸ بازیکن در تیم‌ملی اسپانیا داشت، این کشور قهرمان جام‌جهانی شد و حالا پس از گذشت ۱۶ سال بار دیگر ممکن است تاریخ تکرار شود
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.58K · <a href="https://t.me/Futball180TV/90276" target="_blank">📅 13:55 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90275">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be02e7f18e.mp4?token=BlmiReRVtveEJqgNpLIg6Ccf0Sbo8uKH6qLQhWHcfhONFCym6HJRDw_iVFK5tOkGn0dLdzHVpt4qhEZ43Xmto9GpAmwcikyfSANeobOn05Et87Z9flhcO1PfZzFqyzKXYuvKePxE8vbsppc7DJs-7e2gdSOCIV2EfPf4mWIlfGT6NhxGz1BOOxnBIcLMPUJUab7jbaYS8VNwddpdTDs3_TeyYpPnBLPS1N_2KiQl93RCnSq9kXNSGF20nk-F-4TaNRegvVyzJTXbgoqofM3zrLo2usfcYmJiDmR29lX7SL-F2OkUCyRmgYjsSMwVgLk9kMKn_IaifxzzWMhyQXHXuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be02e7f18e.mp4?token=BlmiReRVtveEJqgNpLIg6Ccf0Sbo8uKH6qLQhWHcfhONFCym6HJRDw_iVFK5tOkGn0dLdzHVpt4qhEZ43Xmto9GpAmwcikyfSANeobOn05Et87Z9flhcO1PfZzFqyzKXYuvKePxE8vbsppc7DJs-7e2gdSOCIV2EfPf4mWIlfGT6NhxGz1BOOxnBIcLMPUJUab7jbaYS8VNwddpdTDs3_TeyYpPnBLPS1N_2KiQl93RCnSq9kXNSGF20nk-F-4TaNRegvVyzJTXbgoqofM3zrLo2usfcYmJiDmR29lX7SL-F2OkUCyRmgYjsSMwVgLk9kMKn_IaifxzzWMhyQXHXuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از عجایب فوتبال بانوان در آمریکا؛ بازیکنی باردار درحال انجام بازی🫪
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.71K · <a href="https://t.me/Futball180TV/90275" target="_blank">📅 13:36 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90274">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/coydkT9EvaNakW44HtH9heco_TphhLoZAycoOk2EjTPVc2Ubct4RZxPrml-5ut1AMSU1PsYBIoGb2D12dpWbJFSCg-pwClgpbzsEh5O6pKCQgMRzz2PKxXw4p1yeqLX92D6-aNLmsqYFtoDanXMIXFgGJGNiQtvECGIqCxHDFVtxeXsxaY5CJ12_6unvg9hVcy1ekKF2SkoydkfuyKl5N-M_e1xO3_Iw_M9ISS_wWwg-SrQuzm7Ovoqn9p3YeJgyagGQyT4UZfFiQ_3A4w-5Xz7xDRK0xZxuXmDO4u76ds-QTCNOd-e7xyJ_IaLCKnqEEGaMOenXdYsr3o_49yoPig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
متئو مورتو:
مذاکرات بین بارسلونا و نیوکاسل برای جذب آنتونی گوردون در حال انجام است. با وجود علاقه باشگاه‌های لیگ برتری و بایرن مونیخ، گوردون اولویت خود را به بارسا داده است. نیوکاسل برای جدایی او آماده است.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.43K · <a href="https://t.me/Futball180TV/90274" target="_blank">📅 13:25 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90273">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lF-LmFb22P50wXonhdUYzu7P2j__JzRhC3qUgOJjPRfaliYc734gd2bmoes2H0YkitjJKoEJa7j2xPTgPcKruntuOuYVKczhQoKMfa4et3y-Hvihxi4LCdjJtRmkaOC2ETtyy9ppCTU7LNIxaI7tc6F7Ui2bgaKI1LnaeR-kVzL8-T0PFZQE9pKvWBpAm5IJ84o_SG-PkbT2iJbVi4kSorapzPSUhqEIe2Qq_mhVpNtB8GufXNQQl6_szddB2Zqbc37CeZD9w3shulu3yTk3Kj6P7IK896LNs2n-IQzVfml4NIDbNCjnz-DwgirQX6SnPac6s4F1vz9Ad0maZ2y2qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بهترین گلزنان فصول اخیر لیگ‌قهرمانان اروپا
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.44K · <a href="https://t.me/Futball180TV/90273" target="_blank">📅 12:50 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90272">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">⭕️
تنها جایی که در لحظه عضویت بهت 500 هزارتومان موجودی میده اینجاس
❌
🎉
کافیه فقط عضو بشی تا #وینرو  بهت
🤩
🤩
🤩
هزارتومان جایزه بده ، نیازی هم به واریز نیست.
⌛
پشتیبانی 24 ساعته
🍆
تنها سایت مورد اعتماد ما با بونوس های کاملا واقعی و رویایی:
🌐
Winro.io
🌐
Winro.io…</div>
<div class="tg-footer">👁️ 9.2K · <a href="https://t.me/Futball180TV/90272" target="_blank">📅 12:50 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90269">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/keKm5iCZAbQPMYIIfXVIRtxzE3ar45CQpBdlsqx1mPHN8hkRFQFmO_xvOi9Up7154pgKrz6LR9pSZ96pqT3TJw59shDtL9fQK4d1o8rg-EssiTQiUsHuTHFMRIk8S0MD1EdWvIO3I8_QOoxJhmsjxxwt0g3DGMBXGaXjQ7SioEfMOmI99ZriRCXakPBva8kFb6qJ86OG6WB_W90CyW3eT3YkGbQwrtFNXlGW_Z4aPfQUCi-Zqvbrbb9-C96OrtQSSo5Vxo91A1qVohJG8kKTG_heXMDf1zC4nYvwLEcYsVR8IL9Vl-h3CSInS6f9-MF5N777DkIw26elAk9lM-fnKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
تنها جایی که در لحظه عضویت بهت 500 هزارتومان موجودی میده اینجاس
❌
🎉
کافیه فقط عضو بشی تا
#وینرو
بهت
🤩
🤩
🤩
هزارتومان جایزه بده ، نیازی هم به واریز نیست.
⌛
پشتیبانی 24 ساعته
🍆
تنها سایت مورد اعتماد ما با بونوس های کاملا واقعی و رویایی:
🌐
Winro.io
🌐
Winro.io
کانال بونوس های رایگان
r6
📱
@winro_io</div>
<div class="tg-footer">👁️ 9.6K · <a href="https://t.me/Futball180TV/90269" target="_blank">📅 12:49 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90268">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4cf55f690d.mp4?token=cIdiQlnIqHvougqvdCDcm6RFp2s_7Wity5yrhceDMgufgFjEWa5ODlx_w-DBSSllUbGSD1HMc_4xx-wlBL1P4FBUFhmkqomJsdgnk5ZJYer2FgE7Wjy4JNvlawojoEQ8yIDi4Xd8aBdDvX5UmoPqN5NIB5Ko518dym9cGb0h-SntU2LuMIn91ikAkdcbcRym0AR6tFSuTkrau9OnRkxSrAb0fZ2dGhi48zbvWddxgHVUf_8Qvip1sHkCHEtbeffDDgxh5waPQsbbWNXYNuKMjgtz9BHbpMjGtz6fKJXcgpzq3TKYQ7a8UUKqSSV_AiZMG3IYetGGc_mvLJBX8imf5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4cf55f690d.mp4?token=cIdiQlnIqHvougqvdCDcm6RFp2s_7Wity5yrhceDMgufgFjEWa5ODlx_w-DBSSllUbGSD1HMc_4xx-wlBL1P4FBUFhmkqomJsdgnk5ZJYer2FgE7Wjy4JNvlawojoEQ8yIDi4Xd8aBdDvX5UmoPqN5NIB5Ko518dym9cGb0h-SntU2LuMIn91ikAkdcbcRym0AR6tFSuTkrau9OnRkxSrAb0fZ2dGhi48zbvWddxgHVUf_8Qvip1sHkCHEtbeffDDgxh5waPQsbbWNXYNuKMjgtz9BHbpMjGtz6fKJXcgpzq3TKYQ7a8UUKqSSV_AiZMG3IYetGGc_mvLJBX8imf5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اظهارات تند نیکبخت واحدی: افشین قطبی کاره‌ای نبود. چرا در تیم ملی نتیجه نگرفت؟ قطبی ذات قشنگی نداشت
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.94K · <a href="https://t.me/Futball180TV/90268" target="_blank">📅 12:40 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90267">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/98d2b87299.mp4?token=PLiG0W1HQUqv9cXM7UWa9K2fMtNWs1nClPrl6X5lNssFSKpvkB0ZMW8TV8Ln7ieroZDmpgQqQzhEm9yMgESmV8fWzMeR-IK0KfCreqG68YJsNDzTfCEl1q4pF33DZVezF1H1C4bQUYLlMlaltJZIRDxqg9mMvvlVnAJ08aCyrDrQH4sOyUAnIw__V4U3svfCV6uwnQP3ONMjoLm86VKPRt5pDjurufIf8e-UB_9DDre7W6LMRj5oq_22M6nl1YtKyEQxTA-WNEHfcppsBsznLjNtyxSAVSu_02uUlHRRTyRWgcuKiJQOngyq-Jv9Z4H4x_OBZIKQfU6cLjz25KzJtA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/98d2b87299.mp4?token=PLiG0W1HQUqv9cXM7UWa9K2fMtNWs1nClPrl6X5lNssFSKpvkB0ZMW8TV8Ln7ieroZDmpgQqQzhEm9yMgESmV8fWzMeR-IK0KfCreqG68YJsNDzTfCEl1q4pF33DZVezF1H1C4bQUYLlMlaltJZIRDxqg9mMvvlVnAJ08aCyrDrQH4sOyUAnIw__V4U3svfCV6uwnQP3ONMjoLm86VKPRt5pDjurufIf8e-UB_9DDre7W6LMRj5oq_22M6nl1YtKyEQxTA-WNEHfcppsBsznLjNtyxSAVSu_02uUlHRRTyRWgcuKiJQOngyq-Jv9Z4H4x_OBZIKQfU6cLjz25KzJtA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
اسپویلِ بازی آرسنال و پی اس جی.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.12K · <a href="https://t.me/Futball180TV/90267" target="_blank">📅 12:15 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90266">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/99be172cd9.mp4?token=RtdPc9TGXv8oKsJYPIluBFvgJTbp8KNYIFdEq_gV7b5xabl5qPHSMjE0rlt_TDE24ei_-I03aRH_rU0Q0wERrRbGAoRzkKXAgmXk8SvENElBdadkLwOdnnetwlMbHkLIrJOfuGHNSE5m-28o8R0J2uGlHISi41VIb7aJEYyxI0BatgatlUxt5fTo2L955c454h2zgp4wGljKmXwkF8HVj-UhvO6SEGygcr4namVO9ydo3NQmntofvHqQ71K4wy1Cklv-GSt-idG5X9Y17_XoyFAfltunkOV7EaRFksF7YQtDgMh7ZhwmlyjlIvm9aQLM1AI7uO59TSUQYGf1jVdc2oHogy1gWZ90HdFo81UDox_zQA_2GQcqj1l64T-66XBUqRFVc41MzJbXOlKC9QJj5E0FUqgVrgzufOdN0F1cNWiQXV1e-7Beef1oGlXZtvJNOsQnWvD0LITeka3M7Vfs5U58LxDBYF57T1rjk3eRdGEo_5rUYauTFX_oXk_qoBN51x7iBpaVSzm9WdsM0RhzmH5Icu04ldvf1ctjSkMhP5h6TUZkQ1R3ab0qj8-uqhuZvqF76gs3j7p0mwt_82uaLoYiSgOqMRJMcmCLadsawnrvCi15-nED3cBuGpCPX8l3TZMBI6GR9cp5RVrhEYqHSUeeXkTJf8adfHj2SkKwR0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/99be172cd9.mp4?token=RtdPc9TGXv8oKsJYPIluBFvgJTbp8KNYIFdEq_gV7b5xabl5qPHSMjE0rlt_TDE24ei_-I03aRH_rU0Q0wERrRbGAoRzkKXAgmXk8SvENElBdadkLwOdnnetwlMbHkLIrJOfuGHNSE5m-28o8R0J2uGlHISi41VIb7aJEYyxI0BatgatlUxt5fTo2L955c454h2zgp4wGljKmXwkF8HVj-UhvO6SEGygcr4namVO9ydo3NQmntofvHqQ71K4wy1Cklv-GSt-idG5X9Y17_XoyFAfltunkOV7EaRFksF7YQtDgMh7ZhwmlyjlIvm9aQLM1AI7uO59TSUQYGf1jVdc2oHogy1gWZ90HdFo81UDox_zQA_2GQcqj1l64T-66XBUqRFVc41MzJbXOlKC9QJj5E0FUqgVrgzufOdN0F1cNWiQXV1e-7Beef1oGlXZtvJNOsQnWvD0LITeka3M7Vfs5U58LxDBYF57T1rjk3eRdGEo_5rUYauTFX_oXk_qoBN51x7iBpaVSzm9WdsM0RhzmH5Icu04ldvf1ctjSkMhP5h6TUZkQ1R3ab0qj8-uqhuZvqF76gs3j7p0mwt_82uaLoYiSgOqMRJMcmCLadsawnrvCi15-nED3cBuGpCPX8l3TZMBI6GR9cp5RVrhEYqHSUeeXkTJf8adfHj2SkKwR0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پاسخ شفاف سهراب بختیاری‌زاده سرمربی استقلال به پرسپولیسی‌ها: فاسد نیستم!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.75K · <a href="https://t.me/Futball180TV/90266" target="_blank">📅 11:50 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90265">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/suVHVkpBJJwwyJ6PNGDS5G_0egaqkfn43litE1zzZMSUW1RBtFRp9mXHZ5Gj1-Q9hIaPFZp9JF2QZlQibg5zkNDgUgE7KBAyEQh9qWnkLOa_9bqGpToJr7kbdlGEDQa0bQCqvW6CV1LyDPykutTNVkE5PtFQx0Q0wjkyiPCkR6Es8spj5LZSB59-Zoo66iLCekeVniccHYK0GxfQhHYSfmqEL_FG2e1x6yDDx6mCze5jf-Q8nXckW9whye0HYhPQCkbqfS5jN7PuAHM1x-JOJHxgs_xrwc0-D8Yod4FjFYlTaK0UFQeFDP7w5_3JENsJusgHP0n_XsYl_NvFtLEzyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
به گزارش رومانو، باشگاه بارسلونا بدنبال عقد قرارداد با آنتونی گوردون ستاره نیوکاسل است
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.71K · <a href="https://t.me/Futball180TV/90265" target="_blank">📅 11:25 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90264">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/426e74bc07.mp4?token=Q7uYVi99tkh9OezohyyQYEYpFrJyffpCyOaoQ4DsE-f3UbTwDVOkpS-jzpv3Sctjia1ck8DgoEizfG0EXJJp9vLtLCXODljf8x6OAtTciau9uGgj_A7D-B1tnkuIOHCVhpND4XMMK_nivd1t3qeziVeKwgLYcoY_IBAaBXV_9JqWvRY-7JmBTo1Bu-PetBVclxA-uhxfLUgFkUUWT20nQcL1cWt6Y2Z3OaZYmOgRoaJ-fCL-SmXa4K_5plS_l2wT9T0t7Txp9YYA96jqaJapXBNk8jmgNhwu9GbHsFR8_ltufSnnlGQhExZsJ4IbNE6RV-NFgzvaGKNKkwhXIPS434WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/426e74bc07.mp4?token=Q7uYVi99tkh9OezohyyQYEYpFrJyffpCyOaoQ4DsE-f3UbTwDVOkpS-jzpv3Sctjia1ck8DgoEizfG0EXJJp9vLtLCXODljf8x6OAtTciau9uGgj_A7D-B1tnkuIOHCVhpND4XMMK_nivd1t3qeziVeKwgLYcoY_IBAaBXV_9JqWvRY-7JmBTo1Bu-PetBVclxA-uhxfLUgFkUUWT20nQcL1cWt6Y2Z3OaZYmOgRoaJ-fCL-SmXa4K_5plS_l2wT9T0t7Txp9YYA96jqaJapXBNk8jmgNhwu9GbHsFR8_ltufSnnlGQhExZsJ4IbNE6RV-NFgzvaGKNKkwhXIPS434WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیو وایرال شده از اظهارات عجیب شیدا یوسفی بازیگر گمنام سینمای خانگی: در کارخانه پدرم، روی شمش‌های طلا راه می‌رفتم!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.65K · <a href="https://t.me/Futball180TV/90264" target="_blank">📅 11:00 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90263">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6b5959b18a.mp4?token=PuZpETXnwi__DPFJyVC98nunKeuQdZVlIzoNvOdHR9tXFVOkxKQS-bY8-oT5C9IEar4Bolf-w4AXSLqWtF61X_xx6F4mHyaXB6Vql1XY56kB-8mgyTfWePHDDn-Rn3Xm3N_1wgos3x-0CZ_j6Q6P8n01JDi5wkQZWxVZWvGI8vvxmlv44gyoFuS0WHUZbiZnTferPyftHm3zqsE7OxuhQzKzLtczmdroupDX8s_6x6qT3ygKcu8vxVA5yDb_ATMCNHxfTYADaDWn78T-lEtvdNVKoLXz7sZvm2Rf6kPhXugGzHIUE4WViDbAvuUqAO-9tyRg32tF5_gvci7dFFL8Nw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6b5959b18a.mp4?token=PuZpETXnwi__DPFJyVC98nunKeuQdZVlIzoNvOdHR9tXFVOkxKQS-bY8-oT5C9IEar4Bolf-w4AXSLqWtF61X_xx6F4mHyaXB6Vql1XY56kB-8mgyTfWePHDDn-Rn3Xm3N_1wgos3x-0CZ_j6Q6P8n01JDi5wkQZWxVZWvGI8vvxmlv44gyoFuS0WHUZbiZnTferPyftHm3zqsE7OxuhQzKzLtczmdroupDX8s_6x6qT3ygKcu8vxVA5yDb_ATMCNHxfTYADaDWn78T-lEtvdNVKoLXz7sZvm2Rf6kPhXugGzHIUE4WViDbAvuUqAO-9tyRg32tF5_gvci7dFFL8Nw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وقتی صحبت از مهارت و دقت میشه
🔥
🔥
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.61K · <a href="https://t.me/Futball180TV/90263" target="_blank">📅 10:35 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90262">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o_we7MJtkJ1sMrBVKjPqNgWO3WnXpihXm9sQ0ezWOhkrCwV1DZmk1BHj8IRl7T0AKAA-ScwiqijaRbrjHgiqSpHcvCEChkgIql0ZzafCz_MmCslluGFi51utU2J62E3pxL-DUux8MNKYvBND_h55BJupJHwThAVSmJcaSl2ny4I6useo-vr7ITsnwYLwMGmuHme6707Uuq3_aBS01Hm0Vpn1PwO0sdm1xs68maHj-s7UIDT1quWXt_xJMtgUedJzZ56KtyyHSzjflW0VqS3F7rO83QlcLPqZCjYNb6yN3BO1O5xdUQZyCO1TD1inbk80bCqVtv_sM0tMKzDgZY2c9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در ترکیب اصلی رئال‌مادرید در فصل گذشته هیچ بازیکنی از اسپانیا فیکس نبود و بنظر عدم حضور بازیکنی از این تیم در تیم‌ملی اسپانیا برخلاف بارسلونا طبیعی است
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.74K · <a href="https://t.me/Futball180TV/90262" target="_blank">📅 10:10 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90261">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8d64b58d74.mp4?token=hOpyIKXyAdJQQFy2fzuGAOavCYwcwJGGtgSElxuQKyq1admyvm_SyOFV8aSyYn_tufo0ljQPlbFCe-fbLyWqDj4fVU7gBJqQXl-njPpeK1WD-Sq2zChaGUAr376k7wbGNVV_qx_0DaQOegBoTJcedyLq8fXKjbW7DG9hNqBXtuapLSWnNJpJW9pJK7U46ubldL0c_OthKlDJBuB17vlYoMbpAJiEsTDNxQQsdALhwNIo3qLLz1dtH_s4xkDTICOKj2iR-bEcyMlcokQ1DPk982w45lkQEhE3NKU3TH3ZVeHAALS2UfzOLoh1zE8Eo-d-Uccz3MFWSowHcQoKWkvpboWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8d64b58d74.mp4?token=hOpyIKXyAdJQQFy2fzuGAOavCYwcwJGGtgSElxuQKyq1admyvm_SyOFV8aSyYn_tufo0ljQPlbFCe-fbLyWqDj4fVU7gBJqQXl-njPpeK1WD-Sq2zChaGUAr376k7wbGNVV_qx_0DaQOegBoTJcedyLq8fXKjbW7DG9hNqBXtuapLSWnNJpJW9pJK7U46ubldL0c_OthKlDJBuB17vlYoMbpAJiEsTDNxQQsdALhwNIo3qLLz1dtH_s4xkDTICOKj2iR-bEcyMlcokQ1DPk982w45lkQEhE3NKU3TH3ZVeHAALS2UfzOLoh1zE8Eo-d-Uccz3MFWSowHcQoKWkvpboWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بهترین گل‌های فعلی در سال ۲۰۲۶ فوتبال
🔥
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.74K · <a href="https://t.me/Futball180TV/90261" target="_blank">📅 09:45 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90260">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/26b4bc8543.mp4?token=HqwR4q9dJX-UBP09RW4tvYpVevQIV7DI_9UBEr9NeuII3jOnPxuUZESvX7SpK_PvcOkAC5SehWtKRaFaVZYdZjECqWSKxYBn_4P_Tjh_3EGrRInQa-A2QCeNGcKwQYMOAHpbEXLT8XjxaNvVd32eymVps2pklV_Ere1YFr5iZEtX4lMLWTTLwSSWzMsrVCg6f0fBkL2gqYM6XisEaHRz_LbrsVy0dyhE6Iwxyrw6FC2gOzNQPaagWKiGV5yKqGUcLW2jkquZ3Vu_RwEY4wAac6bCA0UMbKVQ9p1pjNBEkPGu0jZyXwNMPhQXQyzvFCW8SgLKAp-Z0tq3T3DvOWWjaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/26b4bc8543.mp4?token=HqwR4q9dJX-UBP09RW4tvYpVevQIV7DI_9UBEr9NeuII3jOnPxuUZESvX7SpK_PvcOkAC5SehWtKRaFaVZYdZjECqWSKxYBn_4P_Tjh_3EGrRInQa-A2QCeNGcKwQYMOAHpbEXLT8XjxaNvVd32eymVps2pklV_Ere1YFr5iZEtX4lMLWTTLwSSWzMsrVCg6f0fBkL2gqYM6XisEaHRz_LbrsVy0dyhE6Iwxyrw6FC2gOzNQPaagWKiGV5yKqGUcLW2jkquZ3Vu_RwEY4wAac6bCA0UMbKVQ9p1pjNBEkPGu0jZyXwNMPhQXQyzvFCW8SgLKAp-Z0tq3T3DvOWWjaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وحید قلیچ برا خودش عالمی داره
😂
😂
😐
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.76K · <a href="https://t.me/Futball180TV/90260" target="_blank">📅 09:20 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90259">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c4b0e0df75.mp4?token=iL4vqTkVzY-8tr7r5ueEPa7L3ts5gFY11QazaGI0M0H9SiqsEJVOorrg32-cNtLHRWhyi7_5NXW648JUbxNGHKst9nWgikBfA2PvKKTPzxyzt7sv2bR1wIqbjEWyac0svhytRviX_A8AhxYs4mndNRNLjdAUFtlA8iWXIBGcKAGE8qbpcO20JDRpnXVvf9b2RgRxNzIVTl2pAgVGM7J5Ux5WDKyefi1KKmYKrve7R5t4B59aRrq-AZIvwmyHmut9rv6pYr8uSmELcSbaRap0pEA4dkNhV3VZIQI-5nRnkaH_Lw-LWzc99eVI-5wBaM67upUDNrjmMD7r91LC3uI5Qw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c4b0e0df75.mp4?token=iL4vqTkVzY-8tr7r5ueEPa7L3ts5gFY11QazaGI0M0H9SiqsEJVOorrg32-cNtLHRWhyi7_5NXW648JUbxNGHKst9nWgikBfA2PvKKTPzxyzt7sv2bR1wIqbjEWyac0svhytRviX_A8AhxYs4mndNRNLjdAUFtlA8iWXIBGcKAGE8qbpcO20JDRpnXVvf9b2RgRxNzIVTl2pAgVGM7J5Ux5WDKyefi1KKmYKrve7R5t4B59aRrq-AZIvwmyHmut9rv6pYr8uSmELcSbaRap0pEA4dkNhV3VZIQI-5nRnkaH_Lw-LWzc99eVI-5wBaM67upUDNrjmMD7r91LC3uI5Qw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
همسر ناصر حجازی: به او یک میلیون تومان پیشنهاد دادند تا گل بخورد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/Futball180TV/90259" target="_blank">📅 08:55 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90258">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">روایت قرارداد نجومی فرزاد آشوبی با راه‌آهن در ایام مالکیت بابک زنجانی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/Futball180TV/90258" target="_blank">📅 08:32 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90257">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">Soren-VPN.apk</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/Futball180TV/90257" target="_blank">📅 01:45 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90256">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Soren-VPN.apk</div>
  <div class="tg-doc-extra">62.2 MB</div>
</div>
<a href="https://t.me/Futball180TV/90256" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔵
فیلترشکن سورن (اندروید)
• نسخه 2.1
برای اینترنت ملی و بین‌الملل، عملکرد خوبی داره.
وصل نشد، مجدداً برای اتصال تلاش کنید.</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/Futball180TV/90256" target="_blank">📅 01:45 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90255">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D1L6ZBUHEOXfbgJrrSLPOMISQj5iNBu7kYIXVBUMVZ8v19qvPQZ4V-wJvmcmEBxaP4jVDRCadd9vCIiSst1-_hXQYC2uynVF8yqOrovJhpzrL_KHcXD51hzvLqyEoq7V6icjyczVh4D_JcGfQBDeRbUJoJAvQhtIm0b4DCVpmCYrdNpquo3RGzZYIAcnZ3fEzI-bTgiQAXow9iIYIvSbjLL1wSivh7b0cKW6DtP6HHqT0gxqmo09ywjSWqn7IPxzU0wkOCNdqKMUZ7RWT6GRRZ2aprQDP5uX2yPv8-ZW--OjOdb-olc-RAg9fQxE58pusWmcZq_ue_DSPEpaCYpeOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">میکل آرتتا بهترین سرمربی فصل لیگ‌برتر شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/Futball180TV/90255" target="_blank">📅 00:56 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90254">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🔥
برترین گل‌های این فصل سوبوسلای در لیورپول
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/Futball180TV/90254" target="_blank">📅 00:54 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90253">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CY52_tJaD9EaB6QnVzzkWJxo1blCVa_HfQokBgcZos1MkDzNXlPkbznkF5IR5e0cc6UN2A11XD1ZWbnGP9loagybOzgvMROidKMoTLNMxKhFHxcMs58Z08IfSasw1aF9qEps3pl_lfWnc4Zfw8D59pQlCoyesmMLkLk1f7FaHVUG8D0Q1hn8rBYzoi4g3VN_E_gdgGis52NFiBGElJESYwyHDIVthEgh76TfM0W5OXnqxrrPK3waYbz8EhgCDMg9zAclDvWZ6KQkiHIC7INcqJAzm5qsdwSsLx_gvFizM07iGkF9eKx_aLrqsYno2TwQqdauzYIHPRboOicCKFcSoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الکسیا پوتیاس بعد از ۱۴ سال از بارسا جدا شد.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/Futball180TV/90253" target="_blank">📅 21:34 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90252">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea61c87680.mp4?token=G4f-QpXXmk0rkdnAiixDOAdqQPNUVqABYktC7SrtNc-a9ItW4I7G0yLXmL3eo2FXoztdjoxjJZjJnQZaBRcJgnASww4imk74OW6iDc83-NPsNt8eCqZ3wy-Gb7PnzaR6y2-1sMFXHcLDQCZWL4c3gNbbCMjSJ71NRfYIt5qKdWof6DF-DwxwlJd-QFRLI-NYtLupw7PNhZQcHXBZ68lgeJj49_befU2YauXjXjUyLrjp11mvpPXCNNeITytnWsBAJXAyWXek4vnecoZ43afTQWGZDYAqoPafL2QJXRJPlqXlYkilwMt5pcK5SpQqU_GlMUe1U81naU510c5THXWjqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea61c87680.mp4?token=G4f-QpXXmk0rkdnAiixDOAdqQPNUVqABYktC7SrtNc-a9ItW4I7G0yLXmL3eo2FXoztdjoxjJZjJnQZaBRcJgnASww4imk74OW6iDc83-NPsNt8eCqZ3wy-Gb7PnzaR6y2-1sMFXHcLDQCZWL4c3gNbbCMjSJ71NRfYIt5qKdWof6DF-DwxwlJd-QFRLI-NYtLupw7PNhZQcHXBZ68lgeJj49_befU2YauXjXjUyLrjp11mvpPXCNNeITytnWsBAJXAyWXek4vnecoZ43afTQWGZDYAqoPafL2QJXRJPlqXlYkilwMt5pcK5SpQqU_GlMUe1U81naU510c5THXWjqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">واکنش ناصر حجازی به پیشنهاد گرین کارت؛ آمریکایی ها باید به دستبوس ما بیایند!
همسر مرحوم حجازی: وقتی بهش پیشنهاد گرین کارت آمریکا رو دادم چنان فریادهایی میزد که ستون خونه می‌لرزید!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.84K · <a href="https://t.me/Futball180TV/90252" target="_blank">📅 21:15 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90251">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">51.9 MB</div>
</div>
<a href="https://t.me/Futball180TV/90251" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 8.85K · <a href="https://t.me/Futball180TV/90251" target="_blank">📅 21:14 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90250">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cAhQ2zZjo4XscL7o3z7mpzWSVhl54J02n1jwrVfymSV34ncHqI2B3n7fsgfN7zFKC1QN1TIyN9yb1L-jsAWAw_dOFqQ33l6Cbe-aXdcI5avmTNTozRYqSiX93_LX3w3XSywWA0hnKfBovuTd1xZUfePQoDKpfb8U_DmCXqZ8Nu1Gy78jaF-jJa_rSrGDM1P_pVPb8H-6UywUh5ByT0X2U9KpnzU2qtGTgAa2SnzlOxekSPixLG8i7AbwggDUi4BZ2qO0iMMqU7iEnkCvCtCP1mG-V18lw-WR50ys0bYs8tX16pcwXsOrOU4lPM9zl7zuepYYKvATMjmb9fX-Sh_DkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤑
پروموی Crypto Freebet
🤑
💠
حداقل 5$ با ارز دیجیتال واریز کن (حداقل 5 بار در هفته، در 3 روز متفاوت)
💠
هر دوشنبه
💎
یه پروموکد می‌گیری برای 30% بازگشت وجه از میانگین واریزت
💠
سقف بازگشت:
💸
تا 300$ در هفته!
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
<div class="tg-footer">👁️ 9.29K · <a href="https://t.me/Futball180TV/90250" target="_blank">📅 21:14 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90249">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/baad93a3a8.mp4?token=JqJ6wkr8eosX_T2KVFfxgvXvA-iBLB9Fj07VvhyC-LtpGgLYeM7SHXHkvp2NITQL0FC1ckzgRn2cuNDHOyRfPcS1bnPcaQCBd8flolS01IHXfy9l2bqVaGhm4gUe3uxIbrz16ngOTKKcSu3yKmRa8FxiJCXE9XyQMAVKCjdagDwsdvHBUK_2IUrlL4Wk_W7pF7lyVhvW4wU6iZJcr6MPSla6MIYkTmDXWTQ5Be8TfF2ezDmrUXcXnE6w8iLKqOeOuPWGtv0eEU_7_QGZ2gxpEzkVvW8lwvBqlrAv1jy2p9Mo5Vpxdgr9dXIinqzps7dK0QatlVjLxPqNy4WsHa24pg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/baad93a3a8.mp4?token=JqJ6wkr8eosX_T2KVFfxgvXvA-iBLB9Fj07VvhyC-LtpGgLYeM7SHXHkvp2NITQL0FC1ckzgRn2cuNDHOyRfPcS1bnPcaQCBd8flolS01IHXfy9l2bqVaGhm4gUe3uxIbrz16ngOTKKcSu3yKmRa8FxiJCXE9XyQMAVKCjdagDwsdvHBUK_2IUrlL4Wk_W7pF7lyVhvW4wU6iZJcr6MPSla6MIYkTmDXWTQ5Be8TfF2ezDmrUXcXnE6w8iLKqOeOuPWGtv0eEU_7_QGZ2gxpEzkVvW8lwvBqlrAv1jy2p9Mo5Vpxdgr9dXIinqzps7dK0QatlVjLxPqNy4WsHa24pg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ازبک‌ها آماده حضور در جام‌جهانی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.88K · <a href="https://t.me/Futball180TV/90249" target="_blank">📅 20:28 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90248">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QE-t-g87jHGTwO3bPNNglFULIwRn5wYN1-JvaaR3PBtlrwe6BoGV8gV9S0t6P_5N5woQLGTssKlpnNgmdqgDDvvdMwff85YrsgosbPlPtWvWh_8UzJyj2iqj7gcs-f9-G-JwpJJXo8VEck8SG-owjuxwPRVRsgRumTFav1VazhudOW4uTyo9LDkfSi5E5ZHU5oyy3W5CrfRwVKcyMOFbM2FO-UtzR7HoU_-iuAU9uizzuxJLVgZK6DFF1gRo3rM0mSzh7bLQ2dO4y9_t4DbFC4MUceK6YhdBliacMpPQzL7OGDq6XfCM8q-Im0ur9iE_LzkGHuLaoJKz_POWc7WfPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">با اعلام رومانو، قرارداد آنتونی رودیگر با رئال‌مادرید یکسال دیگر تمدید شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.21K · <a href="https://t.me/Futball180TV/90248" target="_blank">📅 20:03 · 05 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
