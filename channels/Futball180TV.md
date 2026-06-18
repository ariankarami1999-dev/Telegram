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
<img src="https://cdn5.telesco.pe/file/XlSyKenPPXmNxR2dMCPJzt-Efpbs88W-pHjrRzoHx7BHOklkPwBAwUzYcfW5OiUHuOa_ELyxHzadS94V3TbB9VQZV761JlUaXZqUSWXqtAR72rCIpBkfLQoFVTr_a_uB3d9wrZYz-VpT2OMrtsvLYnTphAAj0-fPHKJ_QOublKqsL3vvhjKnTp9K08u0ACbPhXVS5CLNkxlh8FT2wenB1JV3cr2K3uV0uqv5SFsaCEchBVMnV2HoB5MDFTOu1B7_XeXWlFAUCFinVwQrSVgM6UJpbq9dslaZPaDCrajWIzNyUejQmg_gyeI9yKroKSEp9lA4CdewoP7iYo0GPCXKXA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 جام جهانی 2026 | فوتبال 180</h1>
<p>@Futball180TV • 👥 670K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-28 23:42:23</div>
<hr>

<div class="tg-post" id="msg-94267">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">بازی سوئیس و بوسنی چنگی به دل نمیزنه</div>
<div class="tg-footer">👁️ 619 · <a href="https://t.me/Futball180TV/94267" target="_blank">📅 23:42 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94266">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57a9674b76.mp4?token=dteM39J1eSA_zUGR-x1UiZOL0iCIwsb4vqpmIDlAqB8veL2Do3hri_yqx7FqTsI06wbu_7wwbRpFkOZ2En9qHoWDc1zmPffyKY6vX7qC_-ypn4orkO-LrO9lxGDAUp2uQl6b9U9fYotBLwX_6Xo5YBR3xfLk31sVTWESleK7UKP_Nf0efowgKVSNQLPb1--dtaAPXk1HcYwgPjouz1-PJzAaxLPbk7mlDmG9pUWk-1ISTu9OKWiu3HYDb0245Qo__H7y3PeS3t0Gp2TR9Ck2F-SdHDOwOL1vJ-wT7ku46cO6CiIJ907NDILBwXNMPSRCWqQ_0228FIl1RtmdrWAYig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57a9674b76.mp4?token=dteM39J1eSA_zUGR-x1UiZOL0iCIwsb4vqpmIDlAqB8veL2Do3hri_yqx7FqTsI06wbu_7wwbRpFkOZ2En9qHoWDc1zmPffyKY6vX7qC_-ypn4orkO-LrO9lxGDAUp2uQl6b9U9fYotBLwX_6Xo5YBR3xfLk31sVTWESleK7UKP_Nf0efowgKVSNQLPb1--dtaAPXk1HcYwgPjouz1-PJzAaxLPbk7mlDmG9pUWk-1ISTu9OKWiu3HYDb0245Qo__H7y3PeS3t0Gp2TR9Ck2F-SdHDOwOL1vJ-wT7ku46cO6CiIJ907NDILBwXNMPSRCWqQ_0228FIl1RtmdrWAYig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">واکنش نیمار وقتی آنجلوتی‌ گفت بره انفرادی تمرین کنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.67K · <a href="https://t.me/Futball180TV/94266" target="_blank">📅 23:36 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94265">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uWRxWgj2pfrDkT5mPtSp224gPZWGMBeKTE-exKaQ9CpfFJD6cP5jMkMfTGDp7Ysg4-OgNL-Fbeay_5xIMFcRqN8wDkkAo56-xb_M0lZaZ4PE99gvcfbUc7Umfb2ywhkJCnXrkzVCNNLhhAj0CTeir_Tb9NznKlu5q8vXXcJdsrX73mP_XmiT4GtMIRbjWnipn3EsyaiM9yJjJ-yajSlswvQlaLAE1gt19a30gP_JfkQckZhqu3Zlt_nuIrAGDh9iq2YkFhwc7xcyTfsVB9akRHk4eoMAmUDlPTGF8XVrfPSrwfcMdqgGuRpJz6RPSJ0qd7oFyahJFt_Vgslir662bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚪️
فابریزیو رومانو:
فعلا خبر پیوستن انزو فرناندز به رئال فیکه و باور نکنید، خودم روزهای آینده دربارش صحبت میکنم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.67K · <a href="https://t.me/Futball180TV/94265" target="_blank">📅 23:36 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94264">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HdOj6fA38SeMHnVPp9b8lncrdWn7ioUjprbvt1ZwDptzVHGyIavWlk7lMqNm8zB3_XMCPrDCuxOzgVtraCyTsUUtFdAErZDJalFHRtYFZbc-KTqYcu6EmYFfIkQRY1zVb2bzKwaNnYMv1rJPuGv_WbG17gAagDqq2yWkCbleSCgEnK529ynNwzNFYld9S6kOuBOXThvszl9pS7SCL-NZICvrgriYLJ7V0kQtlZURs64DoCwlbh_eTWu3kroWweL13R4c_JyKIQ4p-IKIXUcbtxljrQnfKjmuDqr19X8HOhsWfRn7haz1z8psnnByeDgNKHjzZa6mjHp1elfwTTd1vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فیفا پروتکل جام جهانی را تغییر داد و به درخواست توماس توخل، به عکاسان اجازه داده نمی‌شود که هنگام سرود ملی جلوی مربیان و کادر فنی آن‌ها بایستند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.94K · <a href="https://t.me/Futball180TV/94264" target="_blank">📅 23:23 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94263">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NwPUzL52tjADM7nm2FpEXBJbSaT2fD5E4ntt-Y6Btmq7vYrgJlMCKtf3-4BKDTSzSBNMj2fQ9dnnhv9bWARNCnDhtGLhNn01qzgaFdOA2XCiBElUZR_fsK7H5ljC7K8kHd7F2nuVVFbXl-6TmqBfW2M_d8LWOaoxYkqFPUWejuNQ-J9FT-j0o0ochaNIA6i3WzFe9EGGxFFP4R1g8hFLolvtu0SbBcebMBzhNbnMQpIAfRHOeB8QN25IbekN0EA8Dh4ljckFrBKhCGRaRZnVn4jMYlGQ-37tV7EQ9RnQpe5K08E9bCw-71s3HcruyWjVfjM57GudhNuKHNARwOTg9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#فووووووری
از تلگراف: بارسلونا و لیورپول به میکی فن د فن ستاره تیم‌ملی هلند علاقه‌مند هستند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/94263" target="_blank">📅 22:47 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94262">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ss3pZurxBrl2zCLXec2IkbLO1UOEe5WKwGMkh3xgYV-QlqTke9tyPuheAmjKMKhGW1-16Smp6PyFObU40PC7z7C8PoHtoEGUtKvrwDrlwF4itKGRFFQDP4ASIC1dfG_0LhpciIx-LO11HrP2K7kj0Pupsqi0Bh-Lf9JMguCG-4HEooknwHTe6oRr4NiOeC94GYoZspyIFh6N0mhY-GXZ34ctrUsWIaVYqBrKUDWRKvODayDmYuqV1N_92px2CLJGYvA9jbQcpdhmR9K90987hPpOFlduREHIE4JGfhrrirBJJiu1iaY0j0sv9MHhRzxb9M-adj6z2UdjJo4Ip7vYiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
بهترین بازیکنان ۲۴ بازی اول جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/94262" target="_blank">📅 22:44 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94261">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c29742102b.mp4?token=BChAHa96AAFxT8pbk_3pCBbwpFKASbBEIr2dAr5nZTjsJNW_laCMkpMYSsI_P94DFPtyKjsd-X3rcT_57WWiBJ58APZsLzZAfyJq2p5RHg-pUH_nAP_2Q3qoudJjKG2-3iuKlobR0HCvY8vpzip7EtmSe83jKUZidZpDYhuiqeYooiiJNQ1IT_M01wGeywRPA4VXKhYgMNOCLdgwI-S60cXE_iE2SSiFKw9XXRDAioj1DSxczYCJFts4GwCzqR82Iy0MFKeG21G3H3Q8eQyR5VwEXoNRwfbvTFhRJw3Xu9qwQ0jdcsVSBxAkV7hWAEV-7PngL_NEdh2BytC2LHlh_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c29742102b.mp4?token=BChAHa96AAFxT8pbk_3pCBbwpFKASbBEIr2dAr5nZTjsJNW_laCMkpMYSsI_P94DFPtyKjsd-X3rcT_57WWiBJ58APZsLzZAfyJq2p5RHg-pUH_nAP_2Q3qoudJjKG2-3iuKlobR0HCvY8vpzip7EtmSe83jKUZidZpDYhuiqeYooiiJNQ1IT_M01wGeywRPA4VXKhYgMNOCLdgwI-S60cXE_iE2SSiFKw9XXRDAioj1DSxczYCJFts4GwCzqR82Iy0MFKeG21G3H3Q8eQyR5VwEXoNRwfbvTFhRJw3Xu9qwQ0jdcsVSBxAkV7hWAEV-7PngL_NEdh2BytC2LHlh_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚡
انگری‌بردز ۲۰۲۶
🏆
بازی کن درجا و بدون قرعه‌کشی تا ۱ گرم طلا ببر!
💰
اگه تو هم طرفدار سرسخت بازی انگری‌بردز بودی، اصلا نباید
انگری‌گلد میلی
رو از دست بدی!
👇
کافیه وارد بازی بشی و
تا ۱ گرم طلا ببری!
📎
انگری‌گلد با جایزه طلایی</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/94261" target="_blank">📅 22:44 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94260">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n-Fy2Teo_Fo7MrL0jSW13OTm8zRB5M-0ukNKcTI9ZfICttneu18n1fRscyk0kwFCw5NkNLrQmoI-Xwj2nIgMXt0coU1BXpck7loXfkPizmrxtNEwUmrddf7mQq-vLSG_eZT2E_ULUXqeRwYU0Inb4BJolW2M19ViFZfIstIsCYCHV2wnO4fYXCOBhmZKDAPpqa1_reetNeqndG7xCSWxeGwFRz6u8fvN6hvdqSmAfS9u3stIKYVCert42PXvAnas8L_-X6pU2bWstEtBZTmZfoSqMg0ElzYbzmazN8-vQIGscT6gu7z1vkU2C3ViFt3_py91ceCfTVR3Czvm5CIoPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
ژوائو نوس:
همه می‌دونیم کریستیانو رونالدو چه کارهای بزرگی برای پرتغال و دنیای فوتبال انجام داده، اما اینجا همه برابرن؛ کریستیانو هم مثل بقیه فقط یه بازیکنه که اومده به تیم کمک کنه و کنار ما برای موفقیت بجنگه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/94260" target="_blank">📅 22:28 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94259">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W8RdT6peF7tGLd7ktAHXdhSpmgcxCUwrT2kQellEvf_NwM6tsxbx5lxq4sUbz8Qzy5LWMqB9UkX75hkbv1-LrN2CzCL3AGP8k4BfhP1cemVWiaRkJJemRmnLD7iNx11xXTHpy7AmUWDAgwCsIeW7tS7DSV0-bQzzmw_UiuoAiLROIskJlx5ecJVUDuE7s3c2kRXjQpl9m_zLdagIs1oNHzWhu4xCU28Fn_gETjFzxGwNyGnQwHXi38ljqUQALb4lzpE3kyBD1KP0dA-GAKfXtlcnLOjP913HXI0gDQe4FRJeZEHpx8OH1Q3v2Rrajj9-sFdG-3cyjC3Vn33D-TxbBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
رسمی فیفا ؛ رامین رضاییان به‌عنوان خلاق ترین بازیکن دور اول گروهی جام‌جهانی شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/94259" target="_blank">📅 22:22 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94258">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f6kgHgSANpfof8E5VrSCptpfYcwfqH-znMokmmw_ksVUBxTeER0sqIbhzm2gn_nNXae-FfJZf1BEPG9UUysjqhSZCYsATDiCCMoYNLcKJqlLRf3XF4u-wBXNU8_AUzryhLm6fO_DMpTLo2U3_GD_D_EMcuNtQGZzQCFAbnMrR6lnFybLSLfkwXCm5KKyOB9rlevahTx-xEdsr2pkGeXr5m4X5UjETtMypz8c00CVjO87MdaoBrwzZaU8BN5c1CzejL1F99w0prz8-xRBt9NTmiVg6W5z3OwIhtt4nGlPzW2jXZkmOIXd8d4K1ln-qGME294IkMdZA1nvverXZFf7LQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
رسمی فیفا ؛ رامین رضاییان به‌عنوان خلاق ترین بازیکن دور اول گروهی جام‌جهانی شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/94258" target="_blank">📅 22:17 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94257">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BjQNzvEV-RcUMsLCS9laJEwy4kdxsqAQHNn4ZIJxtPEo5F31bYQUZGTrTZGuP1cvtlvJ7pzoPfJI3pMVwdOHGVfFCLhihs_n3QGsn1eYDsnWjQOMQk8lN1OupZtNHqd-7lFyXYgl0gbsLW8ATJGnCiMUop0EzKQCQ715mDngQpUCJN5v-HL5Uy6nQbr9JCM1tIVX9ydvUujPvBiyh6MRKcr8MQ1mH-ImR2emMQR6MjQif3ySGTfXqzvf9K2mzHTp1K_JyKswVGHe4SMkiDIxtP3UIirjbs9AEgDeCrUJqS46oCC6Tj_2VxfofuGgu2M2_B2nlgSQ9OsnTJ6sieFfgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚪️
فوری و رسمی |
جان پائول فن هکه، مدافع هلندی برایتون به تاتنهام پیوست.
✅
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/94257" target="_blank">📅 22:08 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94256">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZxeIF6ovyHWoiSDBPR911Ruyo1oMG2I1fxHpm6mYQchg3EcwfdiTSY7J8shfrJxflLZlcUhPnWs0cOwax5QYPXNZef4zT2_iQLwJwpbF2BEn6Vltxk64LE-d9ivloeQfm7WcK8cWXrv_hO2RFHwq8J5L8unvUUKXUXpu6dGLUSxyPFej5y2ujmXUMKHJubPIPjytm-Pa8G97QEPaUC_mAJvD35AGUDe5hhgdIfRgjyg_4MkofH0MyHpOPhxPjmynpBClbcMS0-xDFBsMKQ72Mwf7qVrcYdJt2gdSYCJRYd8jQsNP8TWYeQBQDa24GIp-qOQg-Urvq_cGXYpAAJU2cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇯🇵
#فووووووری
؛ کوبو ستاره تیم‌ملی ژاپن بدلیل مصدومیت دیدار با تونس را از دست داد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/94256" target="_blank">📅 21:58 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94255">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EFlE6iqo8rYkDgc4FhfsIR8w4CsiqIkmT_yQyCkwI44P-BiA8GgW-2OuliqzpSmvhAT21NOJqUX8y00i8UyliUluz8NGuePgtriwvxpzMqVdIrKYf5z3n_5EH8udt7Y_VuV9nbxgM7Hy5DpiovpmbDHNqfV029S0FPhQGRGueHhvdeXCuhh39tsnLafGHZNkCvm6d5VbxolSFI0HE1qt2RtUbjyTOzgZ1GzRUB5dHxkLbcvGmPOx_6tpUlBSbMMAIC-OnEK0YMJFYdZHXxJRtepC21FA1P6WGJ_61z7XJsFaBVvNueZNSENa4eykDL4TSdYO5mjEzWvlnN1LswaTMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
فیفا، لیونل مسی را به‌عنوان صاحب بهترین عملکرد هجومی هفته اول جام جهانی انتخاب کرد.
👑
✅
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/94255" target="_blank">📅 21:58 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94254">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LPYrLFVCv_VVqEePuYnIcWrUMAcDI_brb9YhGZuoBYPUkraYFgRlVVYfrlkDUIzKPIYrjPROZE9VVb5eq8wWAB395Or5upRov7ZRE6cfrmUjml_132QrVZ7tIKY_x199Rd-lgcTYUpPKbHlz3BSsWDPngWM9NGVVwWl1rk9JQNxgrI0tAUFR-Y7mjv9IcX3BeBM9D9Uu43dlrYwUqLb2Jsd41MBGzIcr5KkZBj3VeQwk3NPD0HakPu70l9nQoRlynbGS5r5wARzxi1j0TicWSTFUU4Yvxs7otklph6wwxl7NGRWrm3mBKk5PuFDAiFsoHO6-kKBWHoUgmUcBLdLCCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
اینترمیلان از تمدید قرارداد مربی خود کریستین چیوو برای دو فصل خبر داد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/94254" target="_blank">📅 21:35 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94253">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u6ZckzrDP5u3PssI5NueHTJ6qOqNFjlhwj-k6kGwtkCvnXxuQlnvax2OhHaRr-m8TnULRxy4albFcm5sOhzsigpXrHfNG-prKpkmhummy1ey4BdTJtKLgehzpqkQlj3DayYszyMqQ9l8yucd1V0ybZWU20rrrZ3jfB5QfKcUKcVbSQ_4n6Os7ShSwVZPXNrdR5fxq9OrKLtmhKwVPfi_KQ-tIS-oz6FOiMS1_ZhJuwDKuXTH35jgA8D3RT6zXwZV4wANA61M5AwlcnrJepMX9TN9g8cn-tMRaCJ2aPXdOkwLAxM9MGa50XxfO5RCdsGPioVwC29TYaEkv2jy0CvsXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
#
فوریییییی
؛ ویکتور مونیوز به لیورپول پیوست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/94253" target="_blank">📅 21:33 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94252">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🏆
گل‌اول آفریقای جنوبی به جمهوری چک
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/94252" target="_blank">📅 21:17 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94251">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">زددددددد</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/94251" target="_blank">📅 21:14 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94250">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">آفریقای جنوبیییییق</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/94250" target="_blank">📅 21:14 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94249">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">گلگلگگلگل</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/94249" target="_blank">📅 21:14 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94248">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PtBX2r79azNhkU3XoQNdD7eyDQ6Vip52_F1xuGlbdFe7Mq6DjPS3XFx62B9R42bnThdR85hninPayiXpfLIusvM5l1S80Z6DMVFgA_EQ9Fuuw1nwp4HYjUmqazfA8d8yhF2MM-FubKp3PVQfSHwiKC49-hWrbXO_cZSGfiVdeuWzDg50ZMem3J5_iTDg68FspxtHi4GjYJPSkuVSUrzWmukOsz0gJtGG0dIHhTmFrPTCxcrxb7rqqXV_5Fxt-1VSoZSIpRWn7Ua3SlbzSuFR3stYRF-_lMtz1S5UCX5O8k9HmCbkMlc0qjv7p67qpdSgigsAM7nu8w60gUk4ExUS6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#فووووووری
؛ مجتبی خامنه‌ای: بنده مخالف توافق بودم اما بدلیل درخواست پزشکیان به عنوان رئیس شعام، با این موضوع موافقت کردم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/94248" target="_blank">📅 21:13 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94247">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">پنالتی برای آفریقا</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/94247" target="_blank">📅 21:13 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94246">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kazfHTtuQnMrGtO729QglGAk-bLbVMWjIn6Xzt8OKPFnWsOLSmW9Z1kTU5WhIBkzbL-RgZ1y15eG_bmCPloAlujZp3hcXK0nAh77Kk9OvyXdvVzPAz_htMgXSvD9GU7nddBS-RVCROR__0oGHCzSSnZgDeC2NSoV3XIPdDeLMAFm88s6Ia5YNkXOpr1hnUmBb-pDnXTSqexDdhlER4W9rHZkguRaBZPHkSFoxPy-vQnh6AwB-35hAq_hMFmTVL03uR3nrhtdZJQMQZC663fsD3wXT_k-GJgx0pqY3SBR95PVfRU14egucdhmPciIRJEMzpOzKdZTATo4d8BocSKOJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇦
🇨🇭
ترکیب رسمی بوسنی و سوئیس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/94246" target="_blank">📅 21:09 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94245">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VZl4pZF_grmQ6_08AZ4n_WRsc53hJ5bsg3dkv620rnNr7mntSNE2Fho5aG3Abr12iT0LW4I2g76GDVqMxzuG6zrIhe5I2Pv0Od6E53HDcOcEqNOz77_1MUENSh3sLKfDO591aog0vfGtttzAemNCwqSWqHMgBGW3AWvlMbiWERM4oYPGYIOmTxS0gUJJhWSjBlZ5fha3qJ8QDl1LFFzXGmj1CDx-BzpdZDBNQSMdtxARvI8DbzAmhAYdTyvymNKVUmQ6ZeIhtWIOylUMKzzAu17VAH38CdGV0Qz0RHhLBtJkRIGl6kYlyOz65l2XsD3mAqpLZ59SMQcZ7a2oY9Oi-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
مارک کوکوریا درباره انتقال به رئال‌مادرید:
فکر می‌کنم هم من و هم اطرافیانم، خانواده‌ام، واضح بود که این فرصتی است که نمی‌توانستیم رد کنیم و من از تصمیمی که گرفتیم خیلی خوشحالم.من مجبور شدم تصمیم مهمی بگیرم و هیچ شکی ندارم؛ فکر می‌کنم این یک قدم بزرگ برای من است. وقتی بچه بودی، رویای بازی برای تیم‌های بزرگ را داشتی و فکر می‌کنم رئال مادرید یکی از آن‌هاست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/94245" target="_blank">📅 21:00 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94244">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f0717ffb37.mp4?token=dWjOXzdecUPiF75d8y40TdeFWlbsu8EC3MPP4JL5B-cFeQ4blRGIns28I4EDB8RMKNd7-q3in4ajABWDs5oD5THP-udHfk5gVoqCE5WfvYomBaGBvquqbkvp_XYiHZmtGR4CkmTLekZrBtL9-notDU16aL33j8Sg_9i7VX0OmbEYA6UQUrOTu2QAi6b_2pojoYJLc3b07HZTi4Drnf1rme_PBxoQfGVzdKBF_QzCJd-Hp-ZOAsHZ8XvUs2Pp9z6QpW8ziUKiVHSqZak9UYJnI5B8MfRGKikOM2FaZ-mL1473QZq37d1fnEjIXxKnDOEnhWeD3zqhdigKHaKFTZeFlA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f0717ffb37.mp4?token=dWjOXzdecUPiF75d8y40TdeFWlbsu8EC3MPP4JL5B-cFeQ4blRGIns28I4EDB8RMKNd7-q3in4ajABWDs5oD5THP-udHfk5gVoqCE5WfvYomBaGBvquqbkvp_XYiHZmtGR4CkmTLekZrBtL9-notDU16aL33j8Sg_9i7VX0OmbEYA6UQUrOTu2QAi6b_2pojoYJLc3b07HZTi4Drnf1rme_PBxoQfGVzdKBF_QzCJd-Hp-ZOAsHZ8XvUs2Pp9z6QpW8ziUKiVHSqZak9UYJnI5B8MfRGKikOM2FaZ-mL1473QZq37d1fnEjIXxKnDOEnhWeD3zqhdigKHaKFTZeFlA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
رونالدو نازاریو: به نظرم اگه یه نفر باشه که لیاقت اینو داشته باشه که جلو بزنه و عنوان بهترین گلزن تاریخ جام جهانی رو مال خود کنه، اون آدم کسی نیست جز مسی؛ مسی بهترین گزینه برای داشتن این جایگاهه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/94244" target="_blank">📅 20:34 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94243">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oeuYPrgNbTTld4qmiXTn5TKaHrANGHVBwIDV5uIxdmQqzdIuZ7kRBuExeJdYlOHBraDA-qmQW284oFRqSOcj05IE_GhXK_oXzxNCbILplUWIcfHBfqnD4_09x0M1PdkGsxngT_RIRDYnAMoVGBgFl3QFHO2Qgops3aEA5ojwMcGfrffcvL58Uo-KRBE6Dv9CVMxxZsRsV2EofhyF8G6nWHGfxhLUXF1xVkG18ffleFVsY-vOcCrJUCOiEOflLacFpUo7trOVPI9hfX5CCjldjM6VQVeFMkoU-f7NG_2IGeqLMWNulBuV8aXqUevInUGHW_LfUEAAIXUp63D1OkD4mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
بلینگهام : مودریچ بی نظیره، اون بهترینه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/94243" target="_blank">📅 20:28 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94242">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nPUqdMn2xY5p3KivYf6kKQ-jfN4stZ4MWYFw33c9ehAdEN8j47l8poz4AvI1a8O8f_xDaZotKtA5A38DhPQC_6CX5GTYX89gGr_8ztVzeOM1Tb-FunqeXeO6uD1FrnRBTUyxz4PnPidN7kJ439yRAyG59qNmUWNCY_mqeHqL3zfA4q8HHRRwTLpyzk41ge1GwO50jj4VGgr27zkGe1bYSxQMBC17Q3s25F_ZemjebVz9gzLWcOIc-OzrGjnfDe9SFQNJjF5_vnZrPTlZusml9JVk7wM9cSZN5Dlhe_BwKZ41GxxdyME3LbA-HDZ1H7xyLNpwQwgFYG3dY1MbPlbvKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇰🇷
بازیکنان کره جنوبی امروز دو پهباد رو تو تمرین سرنگون کردن، فدراسیون فوتبال کره جنوبی رسماً فیفا را از این حادثه مطلع کرد و خواستار تحقیقات فوری و اقدامات امنیتی سختگیرانه‌تر شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/94242" target="_blank">📅 20:25 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94241">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">شایعه شده ایلان ماسک قبل اینکه میلیاردر بشه تو فاک بت جوین داده بوده
🔥
با آنالیز حرفه ای ادمین های فاک بت ، بصورت رایگان از فوتبال دیدن پول در بیارید  با فاک بت ، حرفه ای تر شرطبندی کنید
❤️
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/94241" target="_blank">📅 20:25 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94240">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bbFniDHZHGSvG0htsn1VdOGtZyffcUH3Zg3SP85wH_w0CQf0bwoqmZB2PdwehlZc4yPzYFoIQYJs34my_r9OzNFMXSYxDtxUDSFvoe6ssVg82HNbK-mMXRQsJ4Fgf81UfW56Fxqgv1hMLNr9C5CuPwEkTcHLRABMs8friSw6buE_7UJlgILnHCIO5C8IuxkFkNCjwvjQbHojoG466Hzd-MsSpdqAxJvM_28QXtczslbQpjuEOs3c6jbicETRwTxzRbdlGVDz-NltSS2vDUvWsjw4NVv0AF9AzVGHRwWWiaLjPd-izs9ejOew0jYHHyR51LwzDiPC0JygTJVwlWmsFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شایعه شده ایلان ماسک قبل اینکه میلیاردر بشه تو فاک بت جوین داده بوده
🔥
با آنالیز حرفه ای ادمین های فاک بت ، بصورت رایگان از فوتبال دیدن پول در بیارید
با فاک بت ، حرفه ای تر شرطبندی کنید
❤️
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/94240" target="_blank">📅 20:25 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94239">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">پایان نیمه اول
😀
جمهوری چک 1 -
🇿🇦
آفریقای جنوبی 0
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/94239" target="_blank">📅 20:21 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94233">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZywLXbY1fQ_Zjf2wfXCPqWGYnl_sv74U1Zn5aEdIz5sqJ0k0TYelRPx59z7z_3_thf-NfwsYTcwOFW8BLmSWM4LrM-_-qQyTrE2eoQlb-dRvK47J-kQIZ6gcArhc10ro3NeZgE_VQ3W5VkzXxOu00bFEX5jazXVlEKtJXJk3hUsIx0PEofYlY5TIHpGY8TU6uTpNPyuEiEOaBtRP-90vFbdVChL9wn0beYg_9Yjpm-3F2l_hrXeGrSLvTe9LJNR4pNRVQEKbv8QNa52dw7GuIjAP1gBEzflqPba3zzCtB0pNeTq8yNdfhMbXaiQssbi6KIltJNIjM7MqT_b8cobiTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MVK7SXyY8a5YvRd3iTtEB7sO-nJCRRedDYb-YPYGf1RVfC4bEJfJ9RhMlTYz1F0I-P4VXI1U6FNhDww8GDywVUleSMBhujtSA0Wo37GrEZ5KJVkKSJAqX4rhqmmhPYL2ClaxEalBb7JK-9KCE4nVuAuhF5V1M6jYFPZke9AYZs-fLHKpeG8krf4bK8VFetu6R5nBbaPgyfHcHqD7NkZINgHbtb6NmLaRcR_g_r23Ey9rQ1xCySihsWGVz1W8HKzy3k0bxj3Avs9FBP1hMUUJwV9-Ph4rXY1dMr6W_CeWhQb6dOemCcwrKeNFzdRA_qBP9jn1BIO_Za-VcRFmoiv8rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GNM6GN57c1KGMAMsoW1pihCbxqla_Ys-AGTkqVmr5eBz3xWRGLEeO0DCxdpmNVpvy6LKPFjKhFoHbwOA76_CJnmWrvbzjLT1rPhHn3ibDLxa67434zFPSWzcCOKQvIG9KU4_kggIkx0MSmk_XIDsOjGcUYxONOXF9pZUptxX8fnSTDzFLTjaahol5tOVtqOzUV_tNfCYDwdWnska7lSWaYgJWJAs7YsERYkPGRnexHixmewHhJGX3OX_BTYnWJzpWV7s2OF_F2kgRhNb_lQcZQmP-j07C6DG-RcYrdTLBZwp33DJ5GiDGil-hIxUr0zXtGF3-9zS2MfikQRav1bBxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uijAKwamhwVPFmajJlDHLvJPYgACKAFQabvuoHVQM7E4RzQACsOYMBboC3ymI3ERD7ktAyeO9X8fA4YE8Dyx1X49ah6j0VH2r3zFyG2sGCIYSUuP4IkepGPwhxdqSzcDjBXdo-kdvglzGWfBvTQx2f2CqHCCaT9oEgLQ-Mn-8H475ho0m-JOt8EDvXl6RVgfWgSmvdlooCzx76OU37TFoJs8gVhlvJ062ZtdbJ7cA0us3XGHphMX-duK67rLtr9qgA-V9UFPqhSLtSp4ALtBqa-DubV3to4cVHP7-oAXv_12Ww9kKxeRCe33kvdFtHqTuVwQeT4E91_82vBymp6Cdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iqZLbaXTKH9SU7DmbgRadJQ0qeTiQ6Ncnf94O2LNad5AcQIYa3XKwidKuHrGcYcbuicpO1xXM8CvvBKc809Q0tZyq3YTOhKQTc2gPCgAe2dJYpFpV3EY06dlMR47Wd06rGT1ha3Ow5JLPilIbQeQXD5_Igs5zSE1vLbygC937HoYqlpt6ICk-IGzpIFF8_orlbnzOOTjPLPoyGAcqT2hrpZLNrtGUdfqdDGHN4mmRnqBtM_VVopbnkwujB1c_r_kqBkxMdWUbbz_CD4f6xLtQIRpznq6To93jbOg642h5iv_KDKj2POJeqadlVwZ2n2v4NkQpnm-9FSFIqYhmXMS4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/i91slw946d26Ji0vNF-6mJOlMxXq79Ts9i9UV5Pho0Qq9AlbZRi68sc-TrH5KnscB3WYquHR88sXxsBUPR8Y9pTSTNt1egDPWN6xVXhiTzWIsp9oeo5yiW3PKL7FjrgaTWJAk4_sPP-TeK9qnBlVL7DHwD0_o6amVt7TQ_EGwvloTT_SMy9j7wJsxHyuEB3oReGI-opXikTc0VfVwO1k1pMA-tCOiAaikUt1xptcONVJMVm0kqY3ulSZ0HFpknGeOXhWuBbpe_7Z1ZzyeEWKDcSMLwqhE15mMJOufz3Xo1yWNrBXVengqyRghHUk8PjUJwwrO5VLnfbpAg3jrND9aQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👀
🔥
بازیکنای اسپانیا و زیدیاشون هستن.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/94233" target="_blank">📅 20:17 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94232">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TiWw9IAzbclTc4MOyCMcRorN4n2W9KLAdiTBp1p3o94CEKdAU_WvBBmY2TF_AZXB0IESqDPOO5pGb0kYPhfZAsWTAK4SqhxDrZaCA7UD8d6vmGJkHY16WBl8cdYlX5F4cPIJvORIruR0WGW07SiX4DvIxF0XNFgcjVciT-zaWWmOdNQPlBCpfBbqVrH10hCoVu-Fxk9_kmjLbUhwfxUNARqy0JxZps_8RmR3KEegQRbhgBs0a7q-t9VL6nhqYS19L9rtnuwHR5KBVKPigN47DUgkXUHdNHnYAmN99B3Hd5952BQjBqIKFcPPKbCEmy8BEpOhmbgRxlxndG9gImJg7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
3 گل در جام جهانی 2026 پس از پرتاب اوت به ثمر رسید که چک 2 گل آن را به ثمر رساند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/94232" target="_blank">📅 19:57 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94231">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/562bcb149d.mp4?token=qZ7CkEHCza7hCUvPPPwIH4X00bmdcZjfIWFwAi-ZjTPqGvo0UknMlzekJD0uMItp6W1aFPqHuJ9gUExQQVu1y5v2K-zcflRe94aKmLnjt95Zv53Mcta0U9EjHxnUcenM9Tj_vpujyARwKTJaJYro2FfTWA2lLQgAudepk9N2FeRcaOtZrKbEyj6I4QcTSq2wbFEpOKtsqQX8hHsODNlsfNe9oMtUwyVkQJqtaHbh7o-f_d--mAGfV9nK05yqd7rjIPIaUm6bl2SdK0vZe09si5pQQEMLBDcfiomx7s_p36owXorUfXv9pM8YXo5aFkj9QGfMj0mpfq9gnHA6LYfZkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/562bcb149d.mp4?token=qZ7CkEHCza7hCUvPPPwIH4X00bmdcZjfIWFwAi-ZjTPqGvo0UknMlzekJD0uMItp6W1aFPqHuJ9gUExQQVu1y5v2K-zcflRe94aKmLnjt95Zv53Mcta0U9EjHxnUcenM9Tj_vpujyARwKTJaJYro2FfTWA2lLQgAudepk9N2FeRcaOtZrKbEyj6I4QcTSq2wbFEpOKtsqQX8hHsODNlsfNe9oMtUwyVkQJqtaHbh7o-f_d--mAGfV9nK05yqd7rjIPIaUm6bl2SdK0vZe09si5pQQEMLBDcfiomx7s_p36owXorUfXv9pM8YXo5aFkj9QGfMj0mpfq9gnHA6LYfZkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رفیقم: داداش قمارباز اگه برد و باخت به تخمشم نباشه قمارباز میشه.
همچنین رفیقم بعد شروع بازی:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/94231" target="_blank">📅 19:55 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94230">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🚨
❌
🤩
#فوری
#اختصاصی_فوتبال‌180
🔻
اگر اتفاق خاصی رخ‌ندهد، اوسمار ویرا سرمربی پرسپولیس طی یک‌هفته تا ده روز آینده از هدایت سرخپوشان جدا خواهد شد. اوسمار بدلیل مشکلات خانوادگی و البته درخواست حقوق بیشتر نسبت به فصل‌قبل، موانع مهمی در مسیر تمدید قراردادش گذاشته که بانک‌شهر مخالفت جدی خود را با افزایش رقم دستمزدش اعلام کرده
🔻
دراگان اسکوچیچ درحال حاضر جدی ترین گزینه هدایت پرسپولیس شده که البته فعلا بابت مسائل کشور دچار تردید شده. از مهدی مهدوی‌کیا و علی‌دایی نیز گزینه‌های بعدی سرخپوشان هستند که بعید است این دو در شرایط فعلی قصد حضور در ایران و فعالیت را داشته باشند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/94230" target="_blank">📅 19:55 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94229">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9605daa245.mp4?token=q60429f_1q_uhvRhSzkFkMyP-3tFrF8UcLoW_om2BmCOJNKcypB6mUANQyzpwJ7C-pE-17IChoPZ83snFaaslpL1gUKlTvhxLpjAHURLWosABBUXw572mzIfhEic7tR_-55jmd0xengOYWCGImM7Bav6c8PiEepVzAEH3figC7Y03AMfrY3lXia7dQseZE6ONpCGuNuqrkQq14vEGTEMDmpUK9Hh-ToR5voho53O7YjXHovQancwHkr-yKQrDY3fZsGL7r7emhGHE7IjeD4VwOScwDCpAforjrI1BkYU5g9NyM8-GSJW2UU4n4SpfoDyytnlcwNriC9bYXrM2Wf18Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9605daa245.mp4?token=q60429f_1q_uhvRhSzkFkMyP-3tFrF8UcLoW_om2BmCOJNKcypB6mUANQyzpwJ7C-pE-17IChoPZ83snFaaslpL1gUKlTvhxLpjAHURLWosABBUXw572mzIfhEic7tR_-55jmd0xengOYWCGImM7Bav6c8PiEepVzAEH3figC7Y03AMfrY3lXia7dQseZE6ONpCGuNuqrkQq14vEGTEMDmpUK9Hh-ToR5voho53O7YjXHovQancwHkr-yKQrDY3fZsGL7r7emhGHE7IjeD4VwOScwDCpAforjrI1BkYU5g9NyM8-GSJW2UU4n4SpfoDyytnlcwNriC9bYXrM2Wf18Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">واکنش های مربی ژاپن تو بازی با هلند که به شدت وایرال شده و به انیمه ها تشبیه شده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/94229" target="_blank">📅 19:51 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94228">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f0LKlcZyJs9fzzjRQ11irbEXfywasHeFy0q-Fjxq4R6hV-0gyhi9bXGx2R0qFd3Y9vBTEFq0NvDJuFe4Y_7Qm5bbn9GFFRrigZbt3TWvr3sqwYup4rQOfeDvU2j9Mzxc0g6V-GdeY7MTuL8xI5cJEgvJQ-72F2LEGMvvOjD27XNs7jBGt9mCJZ1acv4WYt4l_4Ob8gQFPT1KFuqvmX0H0PuQkjWUAN8RDi2E9DvRcnneNlxfPJ6oVjZtqpn8zAL9IJa52MQlkgtUt7SSo78UCH0lkhqZsJYau5C5MkHrj4KvdbRjXKnOyKT8ik3mNCap2lTUvrQejX_OIWrdDNnOiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
پیش فروش GTA VI از هفته بعد شروع میشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/94228" target="_blank">📅 19:40 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94227">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JLai6v-1SHgITncts2CjdLs08Mx5ZmIn9NHRt8-vmf_QmM2LqCI23aG2Qc0SCGryRBIZU0OghrOUjvYDgOG4lJuzAPVJANCeKiwJFhOCuqHJ8aVLGGXrxvuCES7UOFP9AAiBbJdIWRvI8GSHIDWRUrXKCcD9roKwaWSDQWuwE8eXBpu0Wqduf8n8w9NqeJ0cgChX-SPPD2CmdVPuc0pOn8m5ksSf-4J0qE8v0rs7MGN9qHuKWIcENjB-7WVEOeUCAl8AqgtFFGxUq3QhDoKtA8h7mN5sOb7OCPoimblZiqbsGEDpW5B2P9KNFcXfLshgCnb-TWlPQXwXuvNYxThVdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آماد دیالو بیش از هر بازیکن دیگری در هفته اول دریبل های موفق ثبت کرد
🔹
او فقط 34 دقیقه بازی کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/94227" target="_blank">📅 19:39 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94226">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o2opAb0x44Xf1FyCWdrkfyNApL92GjkDoyTdGiLVJ4nU4MHBqKLqctKV4G8v4faOxULL05QhhCplV_fCmvLoDDCaOz_bzV2aJ2hOHoP9GoTXTvIm3j-qt4LBgpjy5vTsuPSdrBHVPUYJLfdbBwMMuqeC8xMsXQdg95kIgpgQLLXME1okfu2mWNW6BbGk5t-loagu7HwE8Vod0RDIikCOrbFpwXL7_Am9auX_VN8r1kj2_RuSE5RRQuxhDlG8AaalYIm4UJOrtqjGFjD7ADYaJW8lD4VRtmDvxzj7UJbXsMz-K5F-7G0DNlG-GoK_U0bhzxP4deeFajG1QB2x5C_j4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇿🇦
🆚
🇨🇿
۲۸ خرداد
🗓️
۱۹:۳۰
⏰
چک
🆚
آفریقای جنوبی
📌
📌
تقابل یکی از نمایندگان فوتبال آفریقا با تیمی منسجم و ساختارمند از اروپا
؛
جایی که قدرت فیزیکی و انگیزه در برابر نظم تاکتیکی و فوتبال تیمی قرار می‌گیرد.
⚽
🔥
جمهوری چک، تیمی منسجم و یکدست از قاره اروپا با ساختار دفاعی منظم و بازی گروهی حساب‌شده که همیشه حریفی سخت برای رقباست
در مقابل
آفریقای جنوبی، یکی از نمایندگان فوتبال آفریقا با بازیکنانی پرانرژی، سرعتی و جنگنده که به دنبال اثبات توانایی خود در سطح جهانی است.
🚀
⚡️
آیا جمهوری چک می‌تواند با نظم و تجربه خود بازی را کنترل کند؟
یا آفریقای جنوبی با انرژی و انگیزه بالا، شگفتی‌ساز خواهد شد؟
👀
🏆
🚀
بتگرام در تمام مسابقات جام جهانی ۲۰۲۶ همراه شماست؛
با پوشش کامل بازی‌ها، آپشن‌های متنوع و هیجان لحظه‌به‌لحظه رقابت‌ها
👉
🌐
🚀
betegram.com/affiliates?btag=3_l7
🔥
⚽</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/94226" target="_blank">📅 19:39 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94224">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/ffc86a865e.mp4?token=J7sYhyHDgloaxP9bkPWMMoSa-HacNFDU-kxOPW9ah25RO2tsppFMujFiOitEQ2w2bxuCVT_Ubz9ZiQXt1Z0HJnQjFVFs7msy7hLBKbZ-mYjWl6uNaUJCNao3loks1yxYkKxb6_LLUGk0I6nKNizr79Tp0RIDf5fH75GZgmjhgm4TQycDaxIXZwx5gHKCIfLEYpGbpyj_MjLRrfb7KPwaXnvQqpmzVmyAJmeW2-s_zs2zFvx1T0yzdyrhqCdJwxidutpAWUaCh8WnXKHHedcgm1lLgZLQjgTVEh8P5FqSnRTo8GTclKR34vzjBdSF5H1JXsm0WmyGVTfmsOkpbx6cOw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/ffc86a865e.mp4?token=J7sYhyHDgloaxP9bkPWMMoSa-HacNFDU-kxOPW9ah25RO2tsppFMujFiOitEQ2w2bxuCVT_Ubz9ZiQXt1Z0HJnQjFVFs7msy7hLBKbZ-mYjWl6uNaUJCNao3loks1yxYkKxb6_LLUGk0I6nKNizr79Tp0RIDf5fH75GZgmjhgm4TQycDaxIXZwx5gHKCIfLEYpGbpyj_MjLRrfb7KPwaXnvQqpmzVmyAJmeW2-s_zs2zFvx1T0yzdyrhqCdJwxidutpAWUaCh8WnXKHHedcgm1lLgZLQjgTVEh8P5FqSnRTo8GTclKR34vzjBdSF5H1JXsm0WmyGVTfmsOkpbx6cOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل اول چک به آفریقای جنوبی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/Futball180TV/94224" target="_blank">📅 19:39 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94223">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">چک گل اول رو زددددد</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/94223" target="_blank">📅 19:35 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94222">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🚨
ترامپ:
اینکه کشورای همسایه ایران اورانیوم داشته باشن و غنی سازی کنن ولی به ایران اجازه داده نشه بی انصافیه! ایران باید برای تولید برق و مسائل مسالمت آمیز اورانیوم داشته باشه. ترامپ دیروز هم گفته بود همه موشک بالستیک دارن ایرانم داشته باشه چیزی نمیشه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/94222" target="_blank">📅 19:34 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94221">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eL-9lZTsTgUiFiRc_lbk-2jnGfdy7JU6AS1i-nwREtRKMpSTXVLKE19rEu_91TAY-DIKunUfHn7pfCF0gNF048qCDu6OQ32deYf-FS8YCRtTRfIxB1mbZVMmxWwyO80T-0p13FdVpMqwfG7Ia9C-mIFTDAg4qo1tnEwb00zk_MRDTuEywErvBqsMf9x_th7m9dgN91bhQkslo32StwNjscnwC23wTkey-mJSMNUPhmrOwiwYTrR2hu0DtH_146p8IkF6cCuWMqxsTu_PQ3CDIp1XOGABCKiCOKWwpUDuW90kEay3ot3eK6oZ4pwNn8k1X04yJdn6KUAjkeqkosUPDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌎
مسابقه جمهوری چک و آفریقای جنوبی اولین مسابقه در تاریخ جام جهانی خواهد بود که توسط دو مربی بالای ۷۰ سال هدایت می‌شود.
🇨🇿
• میروسلاو کوبیک (۷۴ سال و ۲۹۰ روز)
🇿🇦
• هوگو بروس (۷۴ سال و ۶۹ روز)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/94221" target="_blank">📅 19:25 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94220">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f5b4f88afb.mp4?token=K_ppf5lLMZnu61k3dGeDEl0pWQ8WjJfsbdUbJWMcBfe1K-3w9C_UdLZ1mDvF3AVypv485WgnlmuL6usebOjlU4QwkWBVAsnRwt-rLW4IxljFeTv3hxrWr1SSu-ZNp7KsVgzM23YaSYnmLFN5L6ll2nWHhFHtKzW5fhHnrJjxYDf2G9o5E2xol2J9_x1AMVs5zG-Lk0mm1Abo20oLj5TZ3OdL7co_ACnc_oXd5nAbE86K0dO_aRXxVWpKJlx8TfuvMtm4pWgMAQaLXVHXqC5SAWEJxzMhzHoQj3L3VZQN44DIh4YyJ88o8YrQioqtZ42LbysNUuvpVEQJcQib0-b81w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f5b4f88afb.mp4?token=K_ppf5lLMZnu61k3dGeDEl0pWQ8WjJfsbdUbJWMcBfe1K-3w9C_UdLZ1mDvF3AVypv485WgnlmuL6usebOjlU4QwkWBVAsnRwt-rLW4IxljFeTv3hxrWr1SSu-ZNp7KsVgzM23YaSYnmLFN5L6ll2nWHhFHtKzW5fhHnrJjxYDf2G9o5E2xol2J9_x1AMVs5zG-Lk0mm1Abo20oLj5TZ3OdL7co_ACnc_oXd5nAbE86K0dO_aRXxVWpKJlx8TfuvMtm4pWgMAQaLXVHXqC5SAWEJxzMhzHoQj3L3VZQN44DIh4YyJ88o8YrQioqtZ42LbysNUuvpVEQJcQib0-b81w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
‼️
وضعیت فیلمبردار بازی امروز صبح کلمبیا که بعد تکل خشن خوسانوف اینجوری مصدوم شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/94220" target="_blank">📅 19:00 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94219">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c4N_UhXUNI72ahrNjTQWrJVMP7BGoAM3bZHBVxAouL3VOSYTzwi7WqpcuVXNE4ApDmNGb8RF9POTKTiGHh_COZqSukgS_xE33GjCuUNB1zKDUIwHl_icBLWiJG9WgxjMydQG6-C26bUMRNLg2NvJs0ygEtDTWva-45pAjV7GwyqYAIGqvLvxE8GQJnCiqOgbGHwYbZ6BaDXLZhdNotaj7D9Nc4qYtIOpZGRo3KqoFw2HAqpdDumCv6deO4y1tEe4lkwMgDQ-KyLu4Dpysb90UjC0arrYu3A8nToMMY9v_bKepfPsCDgGcXLpzHxPTyhmZWwe_kc-zO21t15pAALBSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شاهکار معماری ورزشگاه آتلانتا آماده بازی
🇿🇦
🆚
🇨🇿
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/94219" target="_blank">📅 18:43 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94218">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78462604bf.mp4?token=soRxlamw9GTngkFach18Q5Z3qylXCikdgFTUNMXBHtvv75kQz1EvLY73SvAosw0uCrkJcvY-GT2MxGQwO6j6x5du7xwuk0V9tw9IjJtUgtEiUxLk9xBn9gu-6GBYtCBSi_LtDRkXb-pK6tPDv-NPmpPLGYz10DjklMyVXf53we5AphchwFseZ5VZWLPXiFWBQvSkAix_tWcEJEE-noSB4l738JhOwGa8SR9iK32bMM92xYwqoO7XYZXnl4L8XVaQ3uj9THluXaXUPo922Q8lEU6dirZjNxj9ju0mvTmeUAEEVcQRmNVXDwH2HnwDVWU4oKd1i9YwIB1Wbaw_diq8sw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78462604bf.mp4?token=soRxlamw9GTngkFach18Q5Z3qylXCikdgFTUNMXBHtvv75kQz1EvLY73SvAosw0uCrkJcvY-GT2MxGQwO6j6x5du7xwuk0V9tw9IjJtUgtEiUxLk9xBn9gu-6GBYtCBSi_LtDRkXb-pK6tPDv-NPmpPLGYz10DjklMyVXf53we5AphchwFseZ5VZWLPXiFWBQvSkAix_tWcEJEE-noSB4l738JhOwGa8SR9iK32bMM92xYwqoO7XYZXnl4L8XVaQ3uj9THluXaXUPo922Q8lEU6dirZjNxj9ju0mvTmeUAEEVcQRmNVXDwH2HnwDVWU4oKd1i9YwIB1Wbaw_diq8sw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇧🇷
برزیل از نمای نزدیک چقدر زیباست. بیخود نیست دوست دارم این تیم قهرمان بشه.
👀
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/94218" target="_blank">📅 18:33 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94217">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gg8rHqVoe4d8TnrHQWl0mdy2NhcPS4fJmtTVbvS6E30KuM-Oyyp17LokVYq-QkyJLYq7D3aCqWynMpGOP2E8b5vUheXqRa2W9KkJUNFf6habqf5OaSbhAOpyYsquI8_FRLNGPF_B1Dsr1qPzk8EnmDgB-M-I7r10IBwrLyE2cBZj_Zl5eQ_FEcOE7Pjvz1Le4X9V0fDk8TkRWbLJnOZ-6hp5ELCyEYCrvASGTWsYs1IO034UDIcmO0LB-lfpJ28034mBO4mbGiNEijF_ScB3aew7MhyQLPaWfV3zhEN_IiyU16CmeIPboOi5Z3ac_IEM5gZdOB2JkUqa2PxzrijWEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
نیمار به همراه اعضای تیم برزیل برای رویارویی با هائیتی به فیلادلفیا نمی رود.
او در کمپ برزیل در نیوجرسی خواهد ماند تا مرحله نهایی برنامه ریکاوری خود را تکمیل کند.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/94217" target="_blank">📅 18:25 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94215">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LfagJDu820A3SLg9JesQlJyq7AZRsWSJUpzaYxp8uBynxGL2nm1xFzpwq0_v5B6OFgw8tgQm2MDYdN6yVuXS7KoXMT8jCIX33cOs5w8W9hVknM_BBX-lhdH8tn5IkngTTnrSmUTujz7WCibkE7YwqQz3dlnyFFI8XfCjUWMtt_cKzkuJixdTKjAJl_LEIGPs_OyVMJ7s4KFDUFRp1_zmsYts7TI_xrJGh5U68FPvTvsapdnLEMrHz_9c7F5q7yUgVoO1vwpKhISLfA-Uueuean5FP64zNyxu34dy9-mR6B_dj1KpVfoFeFS05zUqe4ny_B7W0qnp1vwY6Dj1QIDxzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YYrdPPb7Qnk2CKEZvEWTS4DAWk5lpBPoO0UjFc7OgBsYJ0OGyuXJjkYLNdjZUOsORRukCwrcwxa23-jeHWB5q_hSGQmLtTQkEpcG5SMjFbJWF9dTa90hCSo1Qsj1C79aoaGme6de_KBkm3WZTqih5QvuxCcMPLqrIYHlCmpIKC5_yIystTNVDEY2L3kMdyNNZ-T3TiI9Az0-nPuFa6IEm5PvES53lA22NelY4wkp3DXOG0pzOZ73MMSmn1Wnbb9nZHFBttFM8rl834yuGMnTkVzeCk8yJuZvzZGbkqpxeEBDcP1iw8Pn7Y5zdpMczoUx6x_7dTJ0-lJbX2ahEdKxeA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🇿🇦
🇨🇿
ترکیب رسمی آفریقای‌جنوبی
⚽️
جمهوری‌چک
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/94215" target="_blank">📅 18:24 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94214">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/723f2bef75.mp4?token=aREAajqpciB2jLKIKMNGAeHjRuWTf4gUZRojuAhdLQHsG7uyh_BdixX2rHHhT2sIetLUKOgeJL_zIaGOwDJBJv2MFZuprlBYl1wK2dtFATvrKDpEBvL7InotC2KXbSBP-hJIHBLk7-v7gzXEHOiew6vJ7cNEcKG0vkzb_swp4Jm9jeCC45r0mwel5DQVPVAYS-64Z0BdVjEWcXgC3E_OzRynJexKDcdEgjuy6-WC3PGZry0cv_B9sGl70TPVwjzTB8gDczY6X6YUs1zxpWpHqiaBTFCyeYlnOH_zX4oF2puqTbJlSnjCYD9VfI_utjz0cjv3LDvsn-40wjeaYDlnKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/723f2bef75.mp4?token=aREAajqpciB2jLKIKMNGAeHjRuWTf4gUZRojuAhdLQHsG7uyh_BdixX2rHHhT2sIetLUKOgeJL_zIaGOwDJBJv2MFZuprlBYl1wK2dtFATvrKDpEBvL7InotC2KXbSBP-hJIHBLk7-v7gzXEHOiew6vJ7cNEcKG0vkzb_swp4Jm9jeCC45r0mwel5DQVPVAYS-64Z0BdVjEWcXgC3E_OzRynJexKDcdEgjuy6-WC3PGZry0cv_B9sGl70TPVwjzTB8gDczY6X6YUs1zxpWpHqiaBTFCyeYlnOH_zX4oF2puqTbJlSnjCYD9VfI_utjz0cjv3LDvsn-40wjeaYDlnKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
تیکه سنگین امروز فتح‌الله زاده به میثاقی:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/94214" target="_blank">📅 18:22 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94213">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🔥
💥
🏆
آفریقایی‌های خلاق این‌شکلی با موزیک رسمی جام‌جهانی ویدیو گرفتن. انصافا‌ خیلی خوشکل بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/94213" target="_blank">📅 18:20 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94212">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/80aa310d96.mp4?token=fgNxCpClDgPOVM_rkhyCE27PlneXjCoPTxWGGacHr5LtzZnka0H9nV1yBrfWW2qNAIdDoCWZePPMtS5z_Yrz3muWuAICC6rpKJ3gPQZTWibbn5dumC-NS5qEWVuthcpqJOHcZ7ulP0NGl2U4Go5MGHW_o_mwsE9I8BPLFqCBbk2mkjy989ee4TfxjZrm9bNeuFYJkcBw3sOWbAJ5T75vBA88glB19h4Kzs2yGcfxK4FD9sz8JgfNCPzP32LyneZWOqWLXuuJHtIGhWzTdIui4wytTxvLXU8XQC9D56RSmf1rmbtL3WkW7GioedoXEOJ9JxoPuMbdYt48H1cqBnAnhF3r0WbgJqz00ul24krPbEN0-R9dJAV7vlIm4INcqDIr_x-l0mlcXX8ZyZmxUhjJwS5FWMzhxOCoAyLmI3hXcftlzr14qB6zgpGC7xxs77U9IU-K6Fm2dGJEbNCJXcpjdyq7nr6a7GoQJWvPv2X4aPnVkhMkw6j1AsWQ2EzjbohyowqL6Y2epz5ET63ocjRMHcNxdXccvoGe95vi6bbtXMNXNditGOar32pvgblquDrM9WM8vCcQg3REzkNvAValuIYT2QKNaR-OcoT46kuiSGZ_35NeumkQZinqoGPFIHQwiBc0qThmHyo2bA3x_57Jv7OfAw4EWYgOVXTOWpTzJ28" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/80aa310d96.mp4?token=fgNxCpClDgPOVM_rkhyCE27PlneXjCoPTxWGGacHr5LtzZnka0H9nV1yBrfWW2qNAIdDoCWZePPMtS5z_Yrz3muWuAICC6rpKJ3gPQZTWibbn5dumC-NS5qEWVuthcpqJOHcZ7ulP0NGl2U4Go5MGHW_o_mwsE9I8BPLFqCBbk2mkjy989ee4TfxjZrm9bNeuFYJkcBw3sOWbAJ5T75vBA88glB19h4Kzs2yGcfxK4FD9sz8JgfNCPzP32LyneZWOqWLXuuJHtIGhWzTdIui4wytTxvLXU8XQC9D56RSmf1rmbtL3WkW7GioedoXEOJ9JxoPuMbdYt48H1cqBnAnhF3r0WbgJqz00ul24krPbEN0-R9dJAV7vlIm4INcqDIr_x-l0mlcXX8ZyZmxUhjJwS5FWMzhxOCoAyLmI3hXcftlzr14qB6zgpGC7xxs77U9IU-K6Fm2dGJEbNCJXcpjdyq7nr6a7GoQJWvPv2X4aPnVkhMkw6j1AsWQ2EzjbohyowqL6Y2epz5ET63ocjRMHcNxdXccvoGe95vi6bbtXMNXNditGOar32pvgblquDrM9WM8vCcQg3REzkNvAValuIYT2QKNaR-OcoT46kuiSGZ_35NeumkQZinqoGPFIHQwiBc0qThmHyo2bA3x_57Jv7OfAw4EWYgOVXTOWpTzJ28" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🇩🇿
🇦🇷
مراسم خواستگاری وسط بازی آرژانتین و الجزایر. داماد چه ذوقی داره
😍
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/94212" target="_blank">📅 18:03 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94210">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FccbTx7bfMXcnIuE_38POxPCKhgA2nknpxwEIvcDD8Zk-chzEF6XrZVm0cNVcykmOizOpcV9ilxKfZ0UVb00TmQBAUhVKSI8c2rPQXf5o4MaQgY0dGlmJBfeWXRkJyyEuaITLGRZ3wTPzsmGp9DMICWYs5xaZF-3Jq_O38xDVxW5ccwP5_OA_LcdsDVylQe-l-R9-OnnFwjpC9iw5SyepDj7EY3jZ6yZo9gREEEUKpIpkCUDuKfpgOUm-Mg4lzn73ou49kuh4IINGdDdYDE5LHFs10h-5lcn3Fz8sVYnOTBb7qsmv4awC4bIYo2ZZaq1hT-SlYQ9GnOwYr91HdR2cA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/B38LmOjwomvgBl88-Fv9cCF80OSXqrHBsaMVRdUvwr7zH2-93vM6cy2jdgkzYjKsNElDKQRUYSYhiHx_if1pVyp9tTSl4MDL6iLxmksblM-PFTfM1w7PvJQgChie3q5Y-u3SjtTVe2dU45vVbiTjh7Z32Iu37chCJEWETfW95g8QtFeyRRg4CN4159now6CIl7kwZYdQ5KA1Ohpo1hyodrSkx0vfRXUZFY1xvIDf4JHwKCDr0JuwwrPlbvPBK43q92u2eOxkc4qQt1LYMjUhqjhHMe_LqSvS0R0NIpksuqtt9QyMnDeo8HNf_pOzieDIrxpi3EkcBWu-0tJVE4pNfg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
⚪️
#فووووووری
از مارکا:
رئال مادرید در حال بررسی ارسال پیشنهادی رسمی به مبلغ ۲۲۰ میلیون یورو برای جذب مایکل اولیسه است. رئال مادرید همچنین میخواهد این تابستان هر دو بازیکن انزو فرناندز و مایکل اولیسه را جذب کند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/94210" target="_blank">📅 17:52 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94209">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/916898ff1e.mp4?token=n6YILFhyUhlnECE0sAKiz598Uk92QqWfH4vRNSdukF7YpFhRBW09BwMy0Ln010USehkD_YyODI5xZAh9TIW2JT_g4XmkyF5Yt5ArFiQD3WRQ5m-CaGzWDe3w-Whu1KhJixqgQLnH5AB9xaN4wEqoJM_LZzD9a65SnYqBCdZQmMnJ9I5PaGLDfLGxXSWKEUE3wrjhy3Jz6zQePZ8JSlY9Ti968kJnOM8J4OweivqGakL4sPMneHuBfGiyChb7hMhIPz2kcFRCeX8s1ZYSxB0ia6Y2YlWQZ__ZrKnNkp0YGCXOQajbzSUMI8ppGG-tP67RSvBYkcJatVg5b_WJp-NSow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/916898ff1e.mp4?token=n6YILFhyUhlnECE0sAKiz598Uk92QqWfH4vRNSdukF7YpFhRBW09BwMy0Ln010USehkD_YyODI5xZAh9TIW2JT_g4XmkyF5Yt5ArFiQD3WRQ5m-CaGzWDe3w-Whu1KhJixqgQLnH5AB9xaN4wEqoJM_LZzD9a65SnYqBCdZQmMnJ9I5PaGLDfLGxXSWKEUE3wrjhy3Jz6zQePZ8JSlY9Ti968kJnOM8J4OweivqGakL4sPMneHuBfGiyChb7hMhIPz2kcFRCeX8s1ZYSxB0ia6Y2YlWQZ__ZrKnNkp0YGCXOQajbzSUMI8ppGG-tP67RSvBYkcJatVg5b_WJp-NSow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤣
🏆
خلاصه هفته‌اول مرحله‌گروهی جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/94209" target="_blank">📅 17:40 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94208">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/37dc9fa1fc.mp4?token=K6c3WpMtJqtXgjI6lqOd-lG_NPb_PkscUnXXY7EpMgPg-IPF2IICJ7Bmt4WfAYnjui9P0jMVQX1PUp-pl6TlkvapI9XHRRJXj9stUxsxiHgDydAjAkqYbnSafrZReJlYCS8JcdfK-DETgDhYnPXO_91UEB-RpEoJQ158qkVE0CIKt1FoGd13mFoqJwexnFbU3_scrGjiEd9QQvVcEt2k54cybr1izQqmAasCYAxA2v3miRhLaQqSNbEX0DOT7VNHq8s8NC6INES5qPjyoWDtjklkHJITsMSDTq4Iv8S4ghzdpXW_rC4m4LEMNeuplYvsUthNz6hHdDgQB7ITLa0YZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/37dc9fa1fc.mp4?token=K6c3WpMtJqtXgjI6lqOd-lG_NPb_PkscUnXXY7EpMgPg-IPF2IICJ7Bmt4WfAYnjui9P0jMVQX1PUp-pl6TlkvapI9XHRRJXj9stUxsxiHgDydAjAkqYbnSafrZReJlYCS8JcdfK-DETgDhYnPXO_91UEB-RpEoJQ158qkVE0CIKt1FoGd13mFoqJwexnFbU3_scrGjiEd9QQvVcEt2k54cybr1izQqmAasCYAxA2v3miRhLaQqSNbEX0DOT7VNHq8s8NC6INES5qPjyoWDtjklkHJITsMSDTq4Iv8S4ghzdpXW_rC4m4LEMNeuplYvsUthNz6hHdDgQB7ITLa0YZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
👀
🎙
روایت مرتضی پورعلی‌گنجی از مرام و خاکی بودن ژاوی هرناندز
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/94208" target="_blank">📅 17:20 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94207">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/182af5a6db.mp4?token=i_kDuL2vTmT4ZKJxymFttjubani8-hMU3VBqmtAfA_p1iD72msvLGuGWZbUdyyrLZC9D0orKY4RuhDl4R7FjdMtm06of6b2ed4lEvFiYTuyEg9LG-MBbv76rtn0Uuc3nPP0808AI1qNJVRI6MW95lnB7geL64jPlRzmJ7jFHlK_fLsCzE6ZQjj7Cdf45R86mqRfwOJ2QglMl8pgneIy-FGCIR2AzcAKd2dh9gVawBxNYw9e2X5A-cMv0GjLJ1cUZUEYJMo7rrpLxLGWpg4GTnaHT5wPFgzPokcV4pLcCjckb0plKaQbsMadXB9WxYAmKChgUb2MplcsHeUgZCBbZ7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/182af5a6db.mp4?token=i_kDuL2vTmT4ZKJxymFttjubani8-hMU3VBqmtAfA_p1iD72msvLGuGWZbUdyyrLZC9D0orKY4RuhDl4R7FjdMtm06of6b2ed4lEvFiYTuyEg9LG-MBbv76rtn0Uuc3nPP0808AI1qNJVRI6MW95lnB7geL64jPlRzmJ7jFHlK_fLsCzE6ZQjj7Cdf45R86mqRfwOJ2QglMl8pgneIy-FGCIR2AzcAKd2dh9gVawBxNYw9e2X5A-cMv0GjLJ1cUZUEYJMo7rrpLxLGWpg4GTnaHT5wPFgzPokcV4pLcCjckb0plKaQbsMadXB9WxYAmKChgUb2MplcsHeUgZCBbZ7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
رونالدو نازاریو:
به نظرم اگه یه نفر باشه که لیاقت اینو داشته باشه که جلو بزنه و عنوان بهترین گلزن تاریخ جام جهانی رو مال خود کند، اون آدم کسی نیست جز مسی؛ مسی بهترین گزینه برای داشتن این جایگاهه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/94207" target="_blank">📅 17:16 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94206">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c565269871.mp4?token=rh6XiEIZWljBCu4ljfezMAfVqQFTcJCI0IAeal4hMar4jYqqvR6mL4ppQ15OZsMlJ-_8slxbYflKHDocQfw9hc3mH3WG1QZRzJg8TwkMKgxJcd9yyiLpGuhIHYlAYeOeJXATY3vXBAlO0KMpAljdTTbQNyDFFe_2My2wrALZVicAVg_hWcqr4oEhcbs2T7d-P4IyLI3WLL_TvI_cqEY9jRNqdcISMk2jK9HAAaMxfet_J9cdj1CmDNs0ubXWZN1L2EK8gaW96oF9tMWKZHb5Df28VfwNjHXXCveEW2OljttBR7bpCzcmsLPh9ZY5ybK2yM4MUwxsc2VLgbMloS9vYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c565269871.mp4?token=rh6XiEIZWljBCu4ljfezMAfVqQFTcJCI0IAeal4hMar4jYqqvR6mL4ppQ15OZsMlJ-_8slxbYflKHDocQfw9hc3mH3WG1QZRzJg8TwkMKgxJcd9yyiLpGuhIHYlAYeOeJXATY3vXBAlO0KMpAljdTTbQNyDFFe_2My2wrALZVicAVg_hWcqr4oEhcbs2T7d-P4IyLI3WLL_TvI_cqEY9jRNqdcISMk2jK9HAAaMxfet_J9cdj1CmDNs0ubXWZN1L2EK8gaW96oF9tMWKZHb5Df28VfwNjHXXCveEW2OljttBR7bpCzcmsLPh9ZY5ybK2yM4MUwxsc2VLgbMloS9vYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
حسرت یه موتور روندن اینجوری کف خیابونای ایران رو دلمون مونده
😢
👅
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/94206" target="_blank">📅 17:04 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94205">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tvnw5eyJ1pRGKqDkwllOMNLJIettzcBnoEfSfqoUIWFCEHe78clMdxn647U5rKs3VzVCfvapQL4q1HImA_Bx994k7KL8JaocjXAXAK9LBTeCUqNSip2_EY67ZK60oFiunp8_ZmFxcqaD-dhHfNuXStnQ3kqQzvyrTHuT6y7kj1pOVchAsj-BrfqLLjibjNn9zPrQj8mRF1UEvZLBTDJFRRsRYXDbwXILsUPl25U5S9WKVVHR_AV-3ptmflnyRN_ZZ_M2KY41VZQ_2iuozE5vz_2chzfC8i-oHDkO3nz5ZWVq7F-mBbr9FOYmWSyPSeHwFhWzPBl9B4146cl0GcDVEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
پیتر اشمایکل:
روبرتو مارتینز، بدترین مربی تاریخ جام جهانی، نسل طلایی بلژیک را نابود کرد و این برای او کافی نبود. حالا او میخواهد این کار را با پرتغال انجام دهد. آنها نباید اجازه دهند او حتی یک بازی بیشتر روی نیمکت پرتغال بنشیند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/94205" target="_blank">📅 17:03 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94204">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cUeSnnMeWOyrHtPXjcMTus8yqPYN8Bh4KP2wxk5RE0VTemXdxURcYhm2ZPM7oykfQqJ1g8rL7sk4QfHCRzlluyjJNOJXt7fDX59j3dv9CzXlp4kTG7dwvCbNLBksAF5vrq0iEf3PUjA_-e3cvf0FQ0RNNUQKBBd_8tolfP-q6-arCwF_TlUI2qzf3onY-XyA6_pBYaPqfJ5Jb6AMrHRj2XcA52u2rkt2XRG5kNPk1YO034ERdRIUfWu0F9NeL4N2CNYDeInv41drIq9IEARov1gAbsZY4TdJ9k98PNawttLKDMmqETO-BxMmtP85B7UYItocAAtAIEh9QYH5RqGxZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
فابیو کاناوارو چهارمین بازیکن تاریخ است که برنده توپ طلا شده و به عنوان بازیکن و مربی در جام جهانی شرکت می کند.
فابیو کاناوارو
فرانتس بکن باوئر
اولگ بلوخین
مارکو فن باستن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/94204" target="_blank">📅 16:57 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94203">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/83f7bc36d5.mp4?token=mRXtv-BoidrqaP0Mx6HrsmbnzXkNwvdC2tNxObjPc-oElPerE7AVBeOrSCQWHrJSowTUXvmW9OblsIqmY6FMo_A2Cwf3z0TkdoddreCV3A8QY8okXdRUvxQzIyfU78ktG268oIB5A5GzlzgJWNHM6feuFOqY9_ik7rkECGt0--8AgRR_g5-FFo8qt1eRb6OkglWkL6gErGPYHL9T0gdKChypi5gWfY7Y8TAONZcEOEcBDMrKKx_bK1qPzmAstDbLA_xfFt-TryhSPNxqgKVX18dzSI_ZxADQGmCc61NI-wkd_HVXeWYPNZaZYLxOX6YgEw1Dq307D_IJT37W_MG8Vw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/83f7bc36d5.mp4?token=mRXtv-BoidrqaP0Mx6HrsmbnzXkNwvdC2tNxObjPc-oElPerE7AVBeOrSCQWHrJSowTUXvmW9OblsIqmY6FMo_A2Cwf3z0TkdoddreCV3A8QY8okXdRUvxQzIyfU78ktG268oIB5A5GzlzgJWNHM6feuFOqY9_ik7rkECGt0--8AgRR_g5-FFo8qt1eRb6OkglWkL6gErGPYHL9T0gdKChypi5gWfY7Y8TAONZcEOEcBDMrKKx_bK1qPzmAstDbLA_xfFt-TryhSPNxqgKVX18dzSI_ZxADQGmCc61NI-wkd_HVXeWYPNZaZYLxOX6YgEw1Dq307D_IJT37W_MG8Vw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
🏆
یه ماه دیگه میفهمی به بختت لگد زدی مردد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/94203" target="_blank">📅 16:40 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94202">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vi-gbulRr-J65gd8Jr5FM321N9_-vkTL-x8u_uQguSlF7i6Yuvg4MBdyYBJVFhmGNbuyBKetDSiRaiO40MgphFNgNdq5ESbVSb5qo7qnKdYMPrUwdbmvD5vLrM1zwNWBuHiGQNnIznWf9liQj4YCYwBEPTqCd7ieBA1KOIH1gZ-huTbt6-6FNj6X8Zu5QeyMcv6ub4y4vqWXF53rNNB1IQ7mJahHm8sCOTq4Qm7XsuP-mGY-RbHMbk0UPUYUqGC1L5dw5kUTSWte6Ez2__1yiczeC4xYVp2kgdfsngZixU696wNEaNv3NbCcNzYI1uUc_CqONCrB_LUXliBOuuzNkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
توماس توخل تو رختکن خطاب به بازیکنای انگلیس:
دلیل اینکه این پست رو قبول کردم خود شما هستید. هدف کاملا مشخصه: قهرمان شدن در جام جهانی. باید از همون اول درباره‌اش حرف بزنیم. میخوام به جایی برسیم که قوی‌ترین تیم دنیا باشیم؛ تیمی که هیچ‌کس دلش نخواد مقابلش قرار بگیره.
🏆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/94202" target="_blank">📅 16:39 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94201">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PxEUbJGjxkEf7F40QVvcV70OT19wqLtaytFALEjc3HCgQ6BkIcRnJ4U_R0rgkuB7MnIs7bEY7Zitvkhhl1c3hDfudbgv88-mtNePK8zBJiqo2KbVnzlULKPOsRjjdCRsnm4C7XjWsDF354uMNWOrkTMsYPnaklD_0j07qh0UGe70h92rKFbmPwqw_8UutouMtO4_VT68A-wRfcRJgv8kX2vCv9Im_4NtXtWDrKcqM8ZqKXcEwfvYEqXdw1HkfiGHiaG3bgHeqp4IDBFQDWotR26qNa8YHW-XhfdF0brG-NMvvyU79Tgu23jDaeFsPSed9seSHSVpO8wK1CegSC_nEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
خواهر کریستیانو رونالدو:
بازیکنا انگار یه‌دفعه یادشون رفت چطور باید پاس بدن، توپ‌گیری کنن و حمله بسازن! تمام بازی رو به عقب و کناره‌ها پاس میدادن، ولی اشکالی نداره؛ شروع بدی داشتیم، امیدوارم آخرش خوب تموم بشه.
🙏
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/Futball180TV/94201" target="_blank">📅 16:28 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94200">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YTQaSUaSR-XPYofidNaVmZ02O1by8surcdsii_dfVsjDOGeMahXkBS5Rfd9A1IrvlhAohoGjCEFCUCgjbSxHuMbpeCZnjYeN1-MgkyVWSXYUPz4P96YpmvP6J64lKcMc_yEhzkvs2oLBoS5jZpPdcRBCQY253xtpe9OjvLnQwc9Jy6giUeKMfz7BmGADvQR6fkoMjlaKHAZsTRbMmHgUKRWotmWM91LmY4tov7vfZTp1asG3_gt-Sv_4b4xM958NuJW5cpHUjh61NnESy--HPwVDez9aJIsrt0HyYDiKY9uM3ruTb7n7VoVxWEyXVi69VjU3__iLkrFQVciIWOy6VA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
حمله
جیمی کراگر به رونالدو:
مسی مشکلات تیم رو حل میکنه، اما رونالدو ممکنه گاهی خودش تبدیل به بخشی از مشکل بشه! مسی سطح بازیکن‌های اطرافش رو بالا میبره، ولی رونالدو دیگه اون تأثیر رو مثل قبل نداره. بازیکن‌ها رو باید بر اساس چیزی که الان ارائه میدن قضاوت کرد، نه افتخارات ۱۰ سال پیش! فوتبال بعد از سوت پایان، به گذشته کاری نداره؛ فقط عملکرد امروز مهمه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/Futball180TV/94200" target="_blank">📅 16:23 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94199">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7b65f43b16.mp4?token=us_RapEE4cYsU0szxaGyrrtEhjzfJ1HpjLO5_nCQmpm3z8LAATNlWHC9WqLjqB_4DDKvGggEuJ2G15vXP6CzojGdFgYSjlwWj4MufEB0dTptZRuqY8XhS2G3vABN_8kTU79WWNj5FKfQvr9UGrGqpy9ivQd1cQ2oVCwKTcVMJWyYuR3xe3eGDAHgVlZOViBK6xLdnLnZ3y89Y6DxaNRlZUVNzV4iShwFeOBYhjHx1K1dCzimo5Zat1PtqktgftyY99c-1sib4Z5NZNY6jaT3LQtN6YK_FkhuJhb8n6M98vQswEjkbAWLqatMSeIvGxuXnGS9FU_MKNGrVan4hT78hg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7b65f43b16.mp4?token=us_RapEE4cYsU0szxaGyrrtEhjzfJ1HpjLO5_nCQmpm3z8LAATNlWHC9WqLjqB_4DDKvGggEuJ2G15vXP6CzojGdFgYSjlwWj4MufEB0dTptZRuqY8XhS2G3vABN_8kTU79WWNj5FKfQvr9UGrGqpy9ivQd1cQ2oVCwKTcVMJWyYuR3xe3eGDAHgVlZOViBK6xLdnLnZ3y89Y6DxaNRlZUVNzV4iShwFeOBYhjHx1K1dCzimo5Zat1PtqktgftyY99c-1sib4Z5NZNY6jaT3LQtN6YK_FkhuJhb8n6M98vQswEjkbAWLqatMSeIvGxuXnGS9FU_MKNGrVan4hT78hg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
🏆
خبرنگار: «ولی تو در کنار کلوزه، بیشترین گل رو تو تاریخ جام‌های جهانی زدی؛ این عدد و رقم‌ها برات مهم هستن؟»
🇦🇷
🎙
لیونل مسی: «نه، راستش نه. واقعیتش اینه که خب باعث افتخاره که اونجا باشی، چون نشون‌دهنده ارزش کاره؛ اینکه اسمم کنار کلوزه باشه یا اون بالاها باشم.»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/94199" target="_blank">📅 16:20 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94198">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d2d6b9ef8.mp4?token=aDW4qf-euuz9llkwIFwB0ep0HZ3zPqnJyFs27NIL5cBAcFmMtFhwOwcqEQx8gRIysW81usrpjBy5lkrXa-Mh_IxJOo57IL1snCriLSgSePceiPtoSisG8IHndKxD_5YLqS_K8y_YFr93jbkbQJmWUVB49fc65ciWKMbTy0kr-uR_S1geeQFeKqhQ_2FyhTMUv9LH_JZszhjflFzUCtddtxCEvwm_UrFy3NHvUfNfz9A36g11oYNNJH3evLuw5_nju7wD5E6gotOXvTYXaUiYsxpC5z7gQLqRfy4FgvIMUO4TqL-B_KC5H_qUgSu2ZyclUAMkDoze9UfYdpD1q33uL2yrrW8E_AVmDuiJqYXNJKiYZ6vKM1Zmk6VJl8zAAoBKNX1N2dWPEVp_MeqWOIseEYOwEXcC7hhjOJi_HWyCMWbrkD0yeJxALDEaGN-FInw5cft0boAAD_L1ztUpciti3OVnryYKgW6m1AEjSWcpJmD3JqneVxUyuL92csBYgET5-hVF-b8iGl05NKmZt2Q76Y5_Ib6XMuXbJv_zzSL9MtrGFTOrJjnelO-TlYW9Ay6xgnUKoD47xgZ9_EInMePXHmNEBczeXGKV4qOOVDl6nbsKjuqoY-LE1ZzLVZAC78Ow-C_BnCMif17wk20TeLkrcEDWQ1m8bAzsh5VwksUMD9s" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d2d6b9ef8.mp4?token=aDW4qf-euuz9llkwIFwB0ep0HZ3zPqnJyFs27NIL5cBAcFmMtFhwOwcqEQx8gRIysW81usrpjBy5lkrXa-Mh_IxJOo57IL1snCriLSgSePceiPtoSisG8IHndKxD_5YLqS_K8y_YFr93jbkbQJmWUVB49fc65ciWKMbTy0kr-uR_S1geeQFeKqhQ_2FyhTMUv9LH_JZszhjflFzUCtddtxCEvwm_UrFy3NHvUfNfz9A36g11oYNNJH3evLuw5_nju7wD5E6gotOXvTYXaUiYsxpC5z7gQLqRfy4FgvIMUO4TqL-B_KC5H_qUgSu2ZyclUAMkDoze9UfYdpD1q33uL2yrrW8E_AVmDuiJqYXNJKiYZ6vKM1Zmk6VJl8zAAoBKNX1N2dWPEVp_MeqWOIseEYOwEXcC7hhjOJi_HWyCMWbrkD0yeJxALDEaGN-FInw5cft0boAAD_L1ztUpciti3OVnryYKgW6m1AEjSWcpJmD3JqneVxUyuL92csBYgET5-hVF-b8iGl05NKmZt2Q76Y5_Ib6XMuXbJv_zzSL9MtrGFTOrJjnelO-TlYW9Ay6xgnUKoD47xgZ9_EInMePXHmNEBczeXGKV4qOOVDl6nbsKjuqoY-LE1ZzLVZAC78Ow-C_BnCMif17wk20TeLkrcEDWQ1m8bAzsh5VwksUMD9s" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
💥
🏆
🇦🇷
حاجی جو ورزشگاه بازی آرژانتین رو‌ ببینید. ناموسا چه‌حالی میکردن با لیونل‌مسی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/Futball180TV/94198" target="_blank">📅 16:02 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94197">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb2cdbc7c6.mp4?token=UVEhOSlevnIYxKozqRpexFc3V2wzMwFq0zl0BEaUPBZyr5tXAkRzAzttTqQJ9ou875ac2mGPOgSHZCWAvvXOkCD2wQVDAz8Zw9NRyyTjwqdgfv4PE1K1vW775F0qMOXVSEvBU_agp6-1JyhGPIi_nC-s0cdgiEIBrFr2cdgw_VpC1TKr8LJBRm_zmjPrRhLyt4cgHxGrezD2hTMneY2dOT94H84Tu5PlAI7evfiv3Y9hMqnQo0b5LQSaVJNp53s323el84oLmnayxLVc19fBxx4hguezEdLLF4dHo_JgBO04df-8u9gI3FycFxfJRFQXSFGLl0ryxM4H9HE_vjbEKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb2cdbc7c6.mp4?token=UVEhOSlevnIYxKozqRpexFc3V2wzMwFq0zl0BEaUPBZyr5tXAkRzAzttTqQJ9ou875ac2mGPOgSHZCWAvvXOkCD2wQVDAz8Zw9NRyyTjwqdgfv4PE1K1vW775F0qMOXVSEvBU_agp6-1JyhGPIi_nC-s0cdgiEIBrFr2cdgw_VpC1TKr8LJBRm_zmjPrRhLyt4cgHxGrezD2hTMneY2dOT94H84Tu5PlAI7evfiv3Y9hMqnQo0b5LQSaVJNp53s323el84oLmnayxLVc19fBxx4hguezEdLLF4dHo_JgBO04df-8u9gI3FycFxfJRFQXSFGLl0ryxM4H9HE_vjbEKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کلمبیا با این هواداراش واقعا شایسته برد و درخشش بود و هست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/Futball180TV/94197" target="_blank">📅 15:46 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94196">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U7zzqnUQ_Lah1IH9dsFfXvBx_iidVZtFvrle-ZIqx5B5lY39ur5ccgNXdjM8b78srptD9y42-07FoqnEwvT7N0JSgbXgVlGgjOk32I0ulImojmzdRZZ6j90xmCNE0jaHVQxdJlYKqyNDcWjNpGiy0_b_culWBgmz381RLEOMpeg3lyQvz3Et5Ci8zuuCIlRN1gaNvjuKvHfi2m9d-kmgE5yooXCOUyrOhpfEmF57gjiAhhgPC0ymfJ2B0RFBAdNBP5NY4HpAUQc-ks_EfY00nwW4GIE_AhtOzNuHE838FJCG1l2GYCLJSlYTgpJBUKJpgHh5aQfBDeTjfU1P_xHS7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
به گزارش موندو دپورتیوو، مارک آندره ترشتگن و ایناکی پنیا جایی در برنامه‌های هانسی فلیک برای فصل آینده ندارند.
❌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/Futball180TV/94196" target="_blank">📅 15:34 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94195">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65efc6e80c.mp4?token=NQ2DaTHsuSLyKAYIUQJ6bvIjxvYaVHqyQdeiIGuwgAmIBPkV-GFTUMKDUJREMKCKCn4A5fBHC7OkMmzGOjPlezp7z0_tEtkBxE3LV6lqqeLd1eyVTko5RupD1P5w_RiAhnyIZEzs-5-FnycWZVeHe6IgY4D5v6SxdEV2UuVHk3ALFjADrDW1YGrYQQMPHTrfQY2_XKf2OZCKWMnfzzc-3tpFyjuAGE2fLtsfvJmLds1vMcUA3XcrcCmTKFx9fR3uCpUJMZYz92Dwr2ZVi3Awkoh6nglKvza74bDN_PlQdw5xpyP00I7htR0mqk19-BWiIi-Xzqk-uIPMdQWPLtEomQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65efc6e80c.mp4?token=NQ2DaTHsuSLyKAYIUQJ6bvIjxvYaVHqyQdeiIGuwgAmIBPkV-GFTUMKDUJREMKCKCn4A5fBHC7OkMmzGOjPlezp7z0_tEtkBxE3LV6lqqeLd1eyVTko5RupD1P5w_RiAhnyIZEzs-5-FnycWZVeHe6IgY4D5v6SxdEV2UuVHk3ALFjADrDW1YGrYQQMPHTrfQY2_XKf2OZCKWMnfzzc-3tpFyjuAGE2fLtsfvJmLds1vMcUA3XcrcCmTKFx9fR3uCpUJMZYz92Dwr2ZVi3Awkoh6nglKvza74bDN_PlQdw5xpyP00I7htR0mqk19-BWiIi-Xzqk-uIPMdQWPLtEomQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🔥
کف خیابونای بوئنوس‌آیرس این نقاشی و بنر درخشان از لیونل‌مسی رو نصب کردند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/Futball180TV/94195" target="_blank">📅 15:30 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94194">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JuzXgoPGwWq17PTyZV56_csMUTWYJX1OWhM7s4_iLmQNk6jCv9RpsCvN3oc8frNosVwQq7GDrw3r882bvnvYpnd7RfPV9qfV4A8vX1cB6t9b6g1QvLWJ84arOPzKSWKqhAZOp-t0Ebryq-FX9W1NWb8QncZAK5VRKkMMcTiKt6tqdOf_CnfPsuxjvzsHqqKtKa2ECFRm0KuA0kzVpDt1Eb2bWhPkcMDrTY-zqc2QTf1EtqbuXCmIquWmDSm11NFSKqOKLACk-PTkw89Zt-OTQ8kxTYjI35jNympmpHoT-kwaInL54sspGV36RXVX3L2tq3UgTIGKJNk_RO-q4_Hfpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚪️
خوزه فلیکس دیاز: ادواردو کاماوینگا اصلی‌ترین گزینه خروج از رئال مادریده؛ هافبک فرانسوی مورد توجه چند باشگاه پریمیرلیگ و همچنین پاری‌سن‌ژرمن قرار گرفته. البته خود کاماوینگا به هیچ وجه حاضر به جدایی نیست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/94194" target="_blank">📅 15:29 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94193">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/Futball180TV/94193" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/94193" target="_blank">📅 15:29 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94192">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jinlcn4xetDLA6nEkKH8Ssr95CpnUjZ3A66Y_OdTHUBUumfw54R-Yp-wjLpYfEdnpvAkK8LXySlGAl4UQ3C2WWTEZc5wthCSY3r1QJk1PjtMZJofaKF43mxuOpICr1baS354PhmsAxo--6hNj0E25coJinPuzKhxbLsfWkVHxjnpVzma7SV0uNu0AGmkI4TYngbsLkakiQkPL3v7gNp9z7p6cIegTokr8oGCHAtzgZNndijRMkECYFvvZ0TT2TfkPfqx2KdWECKzP1rva6Vks16lk6_KAvj-OcI7NSm1LYFPVej-umNFrZ5v27ogcwuDSxpW7yp7SN1C_vHJbOcP7Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/94192" target="_blank">📅 15:29 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94191">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/naGbiiEN2bJLK9ElHmzOOPXU2KBbyDcLffIsBXUbaA4vMBhsd6a19sXcclnAXHP0yd2iElOhbxq2E_flVJS2LHa-db8GifvKjlpCPfqIMweq4Or_gpRxAoT3jYIAogH_65vnpQLZxxIT89GjSWuTPI1z9YFMj0RdpZZKnM6ktGsWSdsv2rqLtuULUCB-aYyH5N07cO6P5yptHJooybZJbe4Shek4qs9vTqQXTDSZKuT8cJXRBh-03YrM1GQr2BYNrw2O92w2bnnHqcQv_c6M8lR0BLcCeao3lu7um_bI6NxM83bCBH9K8U4Y23Ifi_lvXMohNpG7KMpiCJyTJfGJgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚪️
خوزه فلیکس دیاز:
ادواردو کاماوینگا اصلی‌ترین گزینه خروج از رئال مادریده؛ هافبک فرانسوی مورد توجه چند باشگاه پریمیرلیگ و همچنین پاری‌سن‌ژرمن قرار گرفته. البته خود کاماوینگا به هیچ وجه حاضر به جدایی نیست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/94191" target="_blank">📅 15:25 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94190">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nU-KzesHOnfpzocVdrQbZk28M74g2ptrBS6AS-UcrejEcZMKPEbZR4-mEoJkBcof5TuRipy44bcOwakWn2BxuQ1UXnEcRCdBi69IePV4mlb1tIS9YEIxQgPoXrQwd73DbEubV4-sxeXa2rSj6JERfaLa1k1kZX8xDh4vnlF72FkrrTCEHoOFhExohGg5d5-gPWT1eNJ1GCJVsCPMdLyL1FTLYGt1leEUWv8NbYeWoe8O-xC2GPvWCuqR4bLrfEDpBy0GlI4uxjJlYzZ5IxjK7UbwHwBUNZHTJpUSNyrHWaVIFi6NvKWHjXLBbfpr7DmOm_G3zl7JP1fuPBDnaIu3_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
🚨
#فوووووری
از رادیو مارکا:
فلورنتینو پرز در حال آماده‌سازی یک حرکت بزرگ در بازار نقل‌وانتقالات است. گفته میشود رئیس رئال مادرید روی یک انتقال بسیار بزرگ و جنجالی کار میکند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/Futball180TV/94190" target="_blank">📅 15:13 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94189">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XW4yTA4h350fAycq9UVNVtf2PQUaoYh4Ah7BUkjH1c4VTJxlXQi3iIf9jvsA2Bft-hsPgiuSuaWXCC8xCW9x37E5-FfA3BIJstuGtEonzjEHkN7d039S9NUMWuR1K2N0DPmgn2aznn-1EffkYIiCKu3rWwGaMmEc-bP4PGro59KoqvHURYiPQAjEC43EKVwbiQGfmalGYUbFYQ1CAxLTVDx95abB9OcI0hgNudGbinM009X-CeAnVi2VZH5VzNPRWQWJGk48zvZCTiSOpkYhVixbfkgWN_LFBuhv4n0-g3JUz0aSiP4RS_cDAVnAT9daELqT4lrc7LjhOUI-i4ZuAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
🔵
بارسلونا از ادکلن 75 دلاری خودش رونمایی کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/Futball180TV/94189" target="_blank">📅 15:07 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94188">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jxd-L0DaP3jpKFKMZhtmYVDH72xn6GIphLg3CBQkTaR1zAuxclW6ZnXk4t4oHxR-7ClBoH5mH71i8GQhTWhtn6lQE8Xs5OZ8JdSMcWNcsB1QtxzaXQYIIK6YRWmw2W5IHKUKgckhMssuAhX4St-pyGGI1tUIx6J9RzyXXnALpgQSo3FAQOu4848SclwIBVNsDBA2aSJn_1Q2xMe6gtxYD8PXKy1KC85u3AAoARs2q1Q41eciTgy2Ohu81XGC9-r8SSfZXBINiEfjStHhde7UJxPaBf69u2hB9ry-SedxjUJkr-2b6gK8WAjkplNQy0MtoG9WzDrAtulCZpSJO77pPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💥
🇦🇷
زوج آرژانتینی بعد برد فوق‌العاده کشورشون
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/Futball180TV/94188" target="_blank">📅 15:04 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94187">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XUqlO_DvcdhUjF_LZBOpS5xlgsRjbWSWaDTnWxaqoC3gYijRdKwya6LzlT5HpUOUHEz3z940PKhcI_oqkdagt-Pi2ievx0QlJm_XBoDEwZwwkR8p1I0kBJAPtClMiTHVeYM7740pVgx0ff4iJoX3sMn2fJ0GZTW0MeGc7sNLGZgAEYaIuEgfoRVkaZ0ZsQfDNiGYHaqYhElUGP0RX-mebVH-okMyDjm-HYeLPsLJ93n5gx21LlKGwl_-hxthTfizOfj_YHz9BYHIbSWWme1vtKBjyCaLkxKgXMxqTkyxbRZv1IyOaMmx2c-eycjvEONGjkF-OhXiy_ZAfOwQZ9gKjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚪️
آاس
: رئال مادرید استعداد مراکشی ایوب بوادی را زیر نظر دارد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/Futball180TV/94187" target="_blank">📅 14:55 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94185">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fupqNz_aPFbAAP7Ifr89Gf2gvdSl2r4YbxbTAROPuK1Xs_2vms1_xXX-WmW6Jf9hftF4WQCBSSO4lR2Wbl7RyRGySqa8o65BK-KrqaYaLTIljDFzZDHEc5RPvGYUd97IjzPOvqe6SDB9xvyrXeoYCMrdKQv-Os0wNrlC0veHLFi1iRwG0E96_N8wtqKUWgKULK9icCz_BSiGldDBOuAiHYUI0bbQAhKp9ntkO8-ZpFkhnxV3oEKQrtSD0ald10qqQXbhAn_q4mztsjupG7fgBYH4kT2Erw8hE-gOmLyN-SI-OKor1iWp5jEcb6lXHQoJYbR2NnGvivDmgXFOJzfEbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hbn0QgO5Hv3kw8cFTmVC81S27vlYAG-eli8UK-PGDSbxvx9VPR6wzhyz14_6kokbQcHuixDmwyuMIcJ9457eY7iDPXWkJSVhCX3ki2zD-yV5QpAR9gp6CCwIIP-mWXAkI_1_Ce06xzx_o9YpU26RYCK55BdFNxzcaZlPIvv6E8V1h4Gim-mXV_zDIUsepgJqS0bzogMyyav0evsjjc3q7IzjDd_unPLLgea_pmj3_oPcgbtvgp6QnDkEO0IJewuG-oRN4MLNQ8QcOU_D8TBW-sC6hSFT-M788CB4Mty3DxPyI4a5JixeIAVNeIQqi8jlqqUf3LbwWqRXZzdqRcFISQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‏
🚨
فوووووری از آبولا پرتغال:
⚽️
روبرتو مارتینز رسماً سرمربی باشگاه النصر شد.
🇵🇹
ژرژ ژسوس رسماً سرمربی تیم ملی پرتغال شد. اعلام رسمی از سوی النصر و پرتغال پس از جام جهانی
✔️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/Futball180TV/94185" target="_blank">📅 14:50 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94184">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c54bbd91a7.mp4?token=qeMVI6tztZGE8PhtDN5BcgSF7zPI-mwdFy12CNHUa8byyfFLkVvXy4JLZKe_UKFDaBBV5vYOamSLt3bBm8AwUlSa4TwvIA7gXVDlpQrt8znRnbbxz7KwVhG_6-_YpQ5zsHsPu9WFwV4gRmUGA5rnDlRUVApxXHKSzN_4FFhKjTKgj6jIiBbfy1x7MMlCxNcMTgoeZmboMN8QnjDmeM0IcGnP2DP03N0DGW--NQWmao8bnu8N0FSuOOm-0ykCwZxREjQec263oipoE34bnWv2txalUHwGXe1EvYSVj2qTMNjTiQOfu_5_vT97v60y-_GWjd_9RVSDHE40XI1oLqKmMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c54bbd91a7.mp4?token=qeMVI6tztZGE8PhtDN5BcgSF7zPI-mwdFy12CNHUa8byyfFLkVvXy4JLZKe_UKFDaBBV5vYOamSLt3bBm8AwUlSa4TwvIA7gXVDlpQrt8znRnbbxz7KwVhG_6-_YpQ5zsHsPu9WFwV4gRmUGA5rnDlRUVApxXHKSzN_4FFhKjTKgj6jIiBbfy1x7MMlCxNcMTgoeZmboMN8QnjDmeM0IcGnP2DP03N0DGW--NQWmao8bnu8N0FSuOOm-0ykCwZxREjQec263oipoE34bnWv2txalUHwGXe1EvYSVj2qTMNjTiQOfu_5_vT97v60y-_GWjd_9RVSDHE40XI1oLqKmMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سباستین ورون، اسطوره فوتبال آرژانتین: تیم ملی ایران خیلی متحول شده است/ فوتبال ایران ظرفیت پیشرفت زیادی دارد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/Futball180TV/94184" target="_blank">📅 14:46 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94183">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f86cfb3e2d.mp4?token=IsjJv3sgXwri_QSQisev2Y1KtSZhFQohyG-HDaYmpYuwNAMeMHY2pAU0jTUpEl82gPMNVRzO7M9dz8LJhY5eid81-KvvU6mvU4U0oRHnUgp1Eq-Lf_a8aTGQ2fi2G-Ec8JUtRvWwNdyiutHfA0XkNGEyn_NbbiTxll4cnCmro6s3qDiuZpp98s1eda7s7w3wvYegcIKJHTTOTpS3gnKKxeLz6OStFm1OJAcJjb_A3JtGTGqfdgWmh4vn-8T91wWtKxuE_IP2a2okiT0sCwpeZu6UkMrb-Z5MTmKSCPSSCxb_dlYbuH99YTYaHTXjb1pYVLqlGprrczboqehqjKKGjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f86cfb3e2d.mp4?token=IsjJv3sgXwri_QSQisev2Y1KtSZhFQohyG-HDaYmpYuwNAMeMHY2pAU0jTUpEl82gPMNVRzO7M9dz8LJhY5eid81-KvvU6mvU4U0oRHnUgp1Eq-Lf_a8aTGQ2fi2G-Ec8JUtRvWwNdyiutHfA0XkNGEyn_NbbiTxll4cnCmro6s3qDiuZpp98s1eda7s7w3wvYegcIKJHTTOTpS3gnKKxeLz6OStFm1OJAcJjb_A3JtGTGqfdgWmh4vn-8T91wWtKxuE_IP2a2okiT0sCwpeZu6UkMrb-Z5MTmKSCPSSCxb_dlYbuH99YTYaHTXjb1pYVLqlGprrczboqehqjKKGjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
‼️
⚠️
پیروز‌قربانی: با تیم خودم فجرسپاسی از این تیم داغون نیوزیلند می‌بردم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/Futball180TV/94183" target="_blank">📅 14:40 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94182">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g3uo2mUervhACs1F5qWLiQ98AWhi1JM3rjaXaIIq--9D362NAQ0a0NGKIFCP2aB-j46KpahOwvaSw6AwUtSCxUMZvVdDdDReIQWTm3AH4bcWA-itIlZgj5TeXQ5yWkdgx2ikvbW-izlMwlcVtf9FkJdUp2oHoVgVKn6uMR8zgN4chRIXcDJ3kiOE7JAsJmytoRg7KBLgZM3hOHphjNVfBEGbt3zLd_VvydOhoocktsYnGprzlz-5FciNjx8l75CsIK71xRtHDE15V2nuDg2EXxZhsbC5I6HHtNOuioxHKi7_kqezVjr5zAw3zZsdlh-48N5aR-9GcauCuAY8oIwGuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚪️
فوووووری نیکولو شیرا:
رئال مادرید آماده‌ست یک پیشنهاد بزرگ به چلسی برای جذب انزو فرناندز ارائه کنه. بازیکن موردنظر هم علاقه‌منده چلسی رو ترک کنه و به رئال مادرید بپیونده.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/Futball180TV/94182" target="_blank">📅 14:34 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94181">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mdNO_2ul8hf7iN9kl0cctWtAbV7qxwD_D5eOy46GLBf-Md0-CsDIzMtk3qRQW56_-6Ozd6pvz4uz0L1BhYwPmWiJRNJdd3JpLXnZtqwzMV6Pu240yQ2NsextZd0ERRu-JekLhnt28oHE3q-Hd9yDLttOFreexmB_RbHTf65BvtgbOp-Z6m5w82MrAeUH8-pKMZxYefw_SQrsbtDGclghSHzlgKaEFg6YyI_1ncHBOsNWttyRNCc_Djsha5i3_SlQYk_I2jM6if_ffa_5aPxXfWPb53t3xaRreSOpHrqOVtSqzTiHW6eVm6v6yzRiCQ_1WXpUaDovR_g3uhAsDRAaow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
🇳🇴
📊
عملکرد ارلینگ‌هالند در کریر فوتبالی خودش بعد درخشش در اولین‌بازی جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/Futball180TV/94181" target="_blank">📅 14:20 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94180">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9087c58782.mp4?token=cfQwlXGKgR182gG7bu7QLsbeekxqmjDOron2lruKVPwj-1S54fuBCYmXmsZPsdEagZ5aIzzGc3H2Soev-ZM9lu3XHPMZ4FanQNzYdKja9BruhBgBBPhMxVzLU9WXoX5ypjoJu-6A_dlsSmS8WAZEcxN1dhXKJ-mvW3J4Wcl9mo3tLQAAah-A-IHHpeI3jOCjquhHYwXDJ5TDESXTAb3odHduPsU_FuqCVzP9cdoOkRgMQOfJcRA5ziBqLt_BY8EpWfsfH9kE_L2HaP3Tkvj4Sttev29QecQXscyCtGT9aooBNkze0x_7tXuRixV39_xAjHNQVxgDd0GxhKHw1q8W0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9087c58782.mp4?token=cfQwlXGKgR182gG7bu7QLsbeekxqmjDOron2lruKVPwj-1S54fuBCYmXmsZPsdEagZ5aIzzGc3H2Soev-ZM9lu3XHPMZ4FanQNzYdKja9BruhBgBBPhMxVzLU9WXoX5ypjoJu-6A_dlsSmS8WAZEcxN1dhXKJ-mvW3J4Wcl9mo3tLQAAah-A-IHHpeI3jOCjquhHYwXDJ5TDESXTAb3odHduPsU_FuqCVzP9cdoOkRgMQOfJcRA5ziBqLt_BY8EpWfsfH9kE_L2HaP3Tkvj4Sttev29QecQXscyCtGT9aooBNkze0x_7tXuRixV39_xAjHNQVxgDd0GxhKHw1q8W0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
صحبت‌های زیبای دکتر انوشه: فوتبال و زندگی مثل هم هستن و شاید دلیلش همین باشه که ما اینقدر فوتبال رو دوست داریم..
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/Futball180TV/94180" target="_blank">📅 14:16 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94179">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SDImmPBsXEzlwJKSj-6CyyX0Gf3krbCGd4kUympjqA1tPj-6WB7LCPVZEBpqMWHsvM_fmY35_Z36yCmQmTlzprCQIIM2KBRKF4Gw2Q_GorOIe3NaGGQoxaSHvDxrc3mL_Ij6WZdP9YqEy60NREHkUXWZpRtHbLrEoNWnkQNdyKn0SVL4Lw6MdxLtgUCG2CGUneUElB1bK7DnzqUOHmzkUoQh9btsVmoyHoB6JqrWG5Tg5mMrsIrplFyukAUG5bcfquh09HvUFSl5tYhLEdXS4Kt3pxachPHG2JUwMpKP4KNZW_RDJv3u9Wir96v54cVShZO3-HR4UxvvSJTutbGgcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
پستی که رونالدو تو اینستاگرام لایک کرده.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/Futball180TV/94179" target="_blank">📅 14:04 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94178">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/39843c046d.mp4?token=OmidZAQIWaU_nNCk00_NliT1C0oA0lTUUop9nal7_Jt1kx8kkwggPSytHortpSo6akFsUvgCfqjNCkmJx6VzVL0Y4_p3PBe4z7s0O9-qZp7QN01LQuZnmCsjyNZJG8QOdYSUg6fH7l1hPuHaWB9iDpDnZ12YDP_OqUpszUToxT2AKqpDfRQZD65AfJfCbWOZ90rqlZYW_kkkKITunibMcaY4oU-aiRThBHRhrKxapWEzSPEs6d2qoU1u0HdFWEIw_AHZbJbGZYvGNceQiipafCgHHuzTQuVQnG_wPANN121QHHJkxhTQtlRMOq1A1WPjI9d1qdz0_llQqaYo8OJStA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/39843c046d.mp4?token=OmidZAQIWaU_nNCk00_NliT1C0oA0lTUUop9nal7_Jt1kx8kkwggPSytHortpSo6akFsUvgCfqjNCkmJx6VzVL0Y4_p3PBe4z7s0O9-qZp7QN01LQuZnmCsjyNZJG8QOdYSUg6fH7l1hPuHaWB9iDpDnZ12YDP_OqUpszUToxT2AKqpDfRQZD65AfJfCbWOZ90rqlZYW_kkkKITunibMcaY4oU-aiRThBHRhrKxapWEzSPEs6d2qoU1u0HdFWEIw_AHZbJbGZYvGNceQiipafCgHHuzTQuVQnG_wPANN121QHHJkxhTQtlRMOq1A1WPjI9d1qdz0_llQqaYo8OJStA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🇨🇻
خیابونای کیپ‌ورد بعد درخشش گلرشون جلو اسپانیا یه نقاشی غول‌پیکر ازش ساختن و فوق‌العاده شده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/Futball180TV/94178" target="_blank">📅 14:04 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94177">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">امضای پزشکیان از نزدیک
😂
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/Futball180TV/94177" target="_blank">📅 13:57 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94176">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZL7C8t3q-uFztWP9-BKXaqdBEfCgFzxyhuqBXfHHNL1u2qYHTwRq3nePEu8ZFAL3ID_lQMfJLi97I0h2YLtq64oF0Se_ZQ17vGgaylApQjfk5TecJReRXODuHIH8YLi9JF31kzd4fGbUWVM5jUUWng6x0C9IaRqYw449_CGurannzz3-uHopzg6TraVAtzIeG_X5vms9Fhf7sauTqhB-MDU_Xtt_t3kdQovDzTqvPoqUasUC45tz6o4xpmpcazYbfOzf9poo7idkXrP9QlDDfxrtStuuH3uHR52bS7_kUCG3yDUTSArEzemoJm36yCA27QWrJv56L0o8_MSMfc3FZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
🔥
سه‌گانه ترسناک بایرن‌مونیخ:
🔺
‏اولیسه: پاس گل
➕
بهترین بازیکن زمین
🔺
‏هری کین: 2 گل
➕
بهترین بازیکن زمین
🔺
لوئیز دیاز: گل و پاس گل
➕
بهترین بازیکن زمین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/Futball180TV/94176" target="_blank">📅 13:43 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94175">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f6df6576c1.mp4?token=rQRO_OORkozM7zaZ2yNTJ2vXqCpM_YlDTY81vPzNOPe2utp5T7mPuaM652lHTC96B2Gy15jdE-6GQNRdztIlh_hD1XgJgg5jH7_9HhJ3NfS78kNJ4rgA6XjxE4OSkx_i0MV675tt83pGdPu3Iq0DSR1jjSg6LVNV7Iw46LiHmiBudflicNZqEG4bL4208uc4jSPL3NmZyXzMXtknV5bCyxbjtQZwXV9tg_15pFgNthAIZazRjXH4QZZVufumdCn3GBexKpQWdFetdpxIw0jF4t-IID6M2dQplqf1SybKPCeB99XSwtV7tLw828_LOqLqodQBw9UIxWCGt7dBEhXD0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f6df6576c1.mp4?token=rQRO_OORkozM7zaZ2yNTJ2vXqCpM_YlDTY81vPzNOPe2utp5T7mPuaM652lHTC96B2Gy15jdE-6GQNRdztIlh_hD1XgJgg5jH7_9HhJ3NfS78kNJ4rgA6XjxE4OSkx_i0MV675tt83pGdPu3Iq0DSR1jjSg6LVNV7Iw46LiHmiBudflicNZqEG4bL4208uc4jSPL3NmZyXzMXtknV5bCyxbjtQZwXV9tg_15pFgNthAIZazRjXH4QZZVufumdCn3GBexKpQWdFetdpxIw0jF4t-IID6M2dQplqf1SybKPCeB99XSwtV7tLw828_LOqLqodQBw9UIxWCGt7dBEhXD0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سباستین ورون، اسطوره فوتبال آرژانتین: اگر مسی مصدوم شود، آرژانتین با چالش‌های زیادی برای ادامه جام جهانی مواجه می‌شود/ در ۲۰ سال گذشته مسی نماد آرژانتین بوده است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/Futball180TV/94175" target="_blank">📅 13:42 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94173">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/33819b4cf6.mp4?token=UmZxo3CJt4t0iI0r0wqzetWqnvRdAzhR5IDUyzFxrfWMMG1fRT76O3720fmNdxYWs_vLnpY13SDj0PnmvaPJRoHlSn1M6w9IYZNNWzn85GsPD8TKlz4WtT0_jsZnHOkWPHlLOcmVj2FEky83fuDUduPBYE_DCb5_JO35DkFJdAwmJEHebWlLXW3IUWZqfVvso0j_WYMQX_Cu6N-Q0xpYUcniYZt2mJRLVUdkENh2iBjaWHxD6obe1tJCDP3wkuxDtuHAL3WJlsSn6niWy0GIhHEPqNqq1ZqkTnRM9-qV9LEMZDo14QcWg69Y0A5glm0niGu-1nyrGyDhmcwNx6-2Kl3vIihIl2dYVqBlOoTR22pT211Jcs_uw9WDSz6o_d7l7RiP3X0CmE4aZP1CyPZ8eeEDdMiQL-0sQ98hxLL9NXQhefbUUAVJhyzFParMK8-hIx3wx2OW8mEMj9Gjxz4AT9VC5gW9OV84iB9qhXLfeDs4m1Q5qWjqSVtfiJ6v0vxy0wbRMbnh3KGCVmUUw-BdooWq9BJnnOx-FFxv0PHpZiGJBCUQ3yf9YuP-uyrc_OThawDQLeiHoTyktNYTTFmgHwc7p6sP2deEj2dOrrF_DrCCF3zCx4-Hz673dfzSikH3KTWVqEwjtx6dFlvso6CKPz-MZNvU82UzMvhqEFPcI94" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/33819b4cf6.mp4?token=UmZxo3CJt4t0iI0r0wqzetWqnvRdAzhR5IDUyzFxrfWMMG1fRT76O3720fmNdxYWs_vLnpY13SDj0PnmvaPJRoHlSn1M6w9IYZNNWzn85GsPD8TKlz4WtT0_jsZnHOkWPHlLOcmVj2FEky83fuDUduPBYE_DCb5_JO35DkFJdAwmJEHebWlLXW3IUWZqfVvso0j_WYMQX_Cu6N-Q0xpYUcniYZt2mJRLVUdkENh2iBjaWHxD6obe1tJCDP3wkuxDtuHAL3WJlsSn6niWy0GIhHEPqNqq1ZqkTnRM9-qV9LEMZDo14QcWg69Y0A5glm0niGu-1nyrGyDhmcwNx6-2Kl3vIihIl2dYVqBlOoTR22pT211Jcs_uw9WDSz6o_d7l7RiP3X0CmE4aZP1CyPZ8eeEDdMiQL-0sQ98hxLL9NXQhefbUUAVJhyzFParMK8-hIx3wx2OW8mEMj9Gjxz4AT9VC5gW9OV84iB9qhXLfeDs4m1Q5qWjqSVtfiJ6v0vxy0wbRMbnh3KGCVmUUw-BdooWq9BJnnOx-FFxv0PHpZiGJBCUQ3yf9YuP-uyrc_OThawDQLeiHoTyktNYTTFmgHwc7p6sP2deEj2dOrrF_DrCCF3zCx4-Hz673dfzSikH3KTWVqEwjtx6dFlvso6CKPz-MZNvU82UzMvhqEFPcI94" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
▶️
انتقادات تند پیروز قربانی به امیر قلعه‌نویی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/Futball180TV/94173" target="_blank">📅 13:42 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94172">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WEcCmU3IH7PdLuvvt0GIzAJb_FougNZN7I5yTlW--W6fQd2Epatkua3Nzgnk6DU-BWPcWk9nUqsgKYnygUelHltHSCQKo8MUTjIcaLOpRkOL33skaWGNUKiZ38Rpcg8skjZyq_2u_4T4f532jR6smCXdFN_oYFNkHpKtVcZo4VoC-lrlIO9aFSCyC0o6PGmFw_LnY2_BJCCWemejcbEYwv-fgKvmjYvens0k6mHa6M2_YoqlChqoEEqh8c-R4YCJQsqpbqVQyZTv2x0-9D9PGQ13dKtLZNd7liKhC1R9T3dcgLU_j783U8b8n7P1f8z_9N_iuc6UhvQkG5vW8Y_2fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
خانواده لیونل‌مسی WC2022
🆚
WC 2026
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/Futball180TV/94172" target="_blank">📅 13:20 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94171">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eeb6168a2a.mp4?token=ZPl79URE3EedovZTslLxBD0xqz03xcfshm4CWPC6TKk-2bRicWjZ-ellA2O5yt3LtW9oH2dWznCb1Ah3fQ5gTUxSe0DxcbpyMpU6B8oenPNsjBz1U5c6rOMThD8vmeaXaSKbS_puuvd9hbGeHJv4hYb0pkAvp7d7OGQAA3Q2B59Mz3hta0F-zGEzJBXePkWRa9TAGsujjkCQzFmeDflj2nyGE90Ij5KqcGEQ7pQVxBwWxBmawSirCszHL_o6D-j9VrSSqFimJbEhIvtb73_9Gv-0cq8w0zv8u458F2oxly8TWytI1zyihipGdBF-pgXTN-FPPFhMApflcJJ_aCQNwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eeb6168a2a.mp4?token=ZPl79URE3EedovZTslLxBD0xqz03xcfshm4CWPC6TKk-2bRicWjZ-ellA2O5yt3LtW9oH2dWznCb1Ah3fQ5gTUxSe0DxcbpyMpU6B8oenPNsjBz1U5c6rOMThD8vmeaXaSKbS_puuvd9hbGeHJv4hYb0pkAvp7d7OGQAA3Q2B59Mz3hta0F-zGEzJBXePkWRa9TAGsujjkCQzFmeDflj2nyGE90Ij5KqcGEQ7pQVxBwWxBmawSirCszHL_o6D-j9VrSSqFimJbEhIvtb73_9Gv-0cq8w0zv8u458F2oxly8TWytI1zyihipGdBF-pgXTN-FPPFhMApflcJJ_aCQNwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
🇦🇷
🇵🇹
صحبت‌های محرم‌نویدکیا درباره تفاوت حضور لیونل‌مسی و‌ رونالدو در جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/Futball180TV/94171" target="_blank">📅 13:12 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94170">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3720508738.mp4?token=T_9nTUiZYHXz6V2o1PZ7bv6s34GTJiQxI9MHax7kENze-Lmrg_DVL9fsfddAlrKjKD7ku_IW3XBRGlaOI0TvoGc5gxfe09C9Q3XXUE7T1Q0R-sk5BIUPZM_ExTbd_J5r3K1cXTVp8lPyqVV5zYSUEyra9M-khdmGgWrgtW1nE_8F4lUtMHmU0FK6lZyIKgFjNZBePr7UGtKC_lTrUxSSKg090-VeJ-aHV9tvCmFu_yDqSeJBnqE70OtNSaWkH0z52wTuW7ULIcGETf6Dl-G4cnAc2hJvgTO5fA-6RzW3t7Ro3GqbGobMIfnkjPdhpO6ZhwJfSQ7rag_d_MXzw6FJCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3720508738.mp4?token=T_9nTUiZYHXz6V2o1PZ7bv6s34GTJiQxI9MHax7kENze-Lmrg_DVL9fsfddAlrKjKD7ku_IW3XBRGlaOI0TvoGc5gxfe09C9Q3XXUE7T1Q0R-sk5BIUPZM_ExTbd_J5r3K1cXTVp8lPyqVV5zYSUEyra9M-khdmGgWrgtW1nE_8F4lUtMHmU0FK6lZyIKgFjNZBePr7UGtKC_lTrUxSSKg090-VeJ-aHV9tvCmFu_yDqSeJBnqE70OtNSaWkH0z52wTuW7ULIcGETf6Dl-G4cnAc2hJvgTO5fA-6RzW3t7Ro3GqbGobMIfnkjPdhpO6ZhwJfSQ7rag_d_MXzw6FJCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اظهار نظر جنجالی سباستین ورون, اسطوره فوتبال آرژانتین: مارادونا از لیونل مسی بازیکن بهتری بود/ او در زمانه‌ای فوتبال بازی می‌کرد که حتی زمین‌ها صاف نبودند ولی او رویایی بازی می‌کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/Futball180TV/94170" target="_blank">📅 13:11 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94169">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C5yGACTEbSaEtii-0P-b7Mr4xW1VqqZIM5s1oW640KT-4_2LxfOE8YviRLxj1JFPDdgjz7Dtm4hICrBal50HUFhsFRL4MOO5Ceql_4cFV5TZogZKiKVuzonPVq4rUcLuPygARuAnhv1tdMFNA97qLPS1tuhIG-kWlwh2FlRE8FiVu2-i-8wIYQ_ckSxK66K0peyIKs6I2cmix7-jKCQGJMYrVR8mGX2KqFraiwhL2p0vFnR3bkq-my3cCh36q6lTPLRaoz10979Rr1BExdRlejGAme2sBKG73PuPS7qJfvl1cNDCG6J6nMnUgaG9CRtizH--a03V4RHY6f8243AnKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
🏆
بیشترین پاس‌گل تا پایان هفته‌اول مرحله گروهی جام‌جهانی فوتبال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/Futball180TV/94169" target="_blank">📅 12:51 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94168">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de8bc47b42.mp4?token=WXa0zQHSTpnoK7BV1Bjk-VSluY43XKDYahkukqGq00zAFzwLLBVe44-HimZCYWuhncAvr7iNVo7nXuIyCEBVe8id81ELEXNPfUKMvA6k26necUS8Gy6nMhTJcSarOmAN2QAwTNvdRUqVeu1qh0aFDz_d27_tTZZra2G9bvxI5mwaBILAgw_51JQCEW0MLG87XsNPeRvjo6zpw_eNEt_45GoyOX6Bfgsbfhq8NnHUieHa2I4iwZdGGipda06j_yNUd8qv8x5rDZ3jovPINnSSUor63OxEu6CfHQQgp8n8Q9AQvgsT-ryVsYvGHalkxpDjHhDL0PZsS7ov1EmMGU27ww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de8bc47b42.mp4?token=WXa0zQHSTpnoK7BV1Bjk-VSluY43XKDYahkukqGq00zAFzwLLBVe44-HimZCYWuhncAvr7iNVo7nXuIyCEBVe8id81ELEXNPfUKMvA6k26necUS8Gy6nMhTJcSarOmAN2QAwTNvdRUqVeu1qh0aFDz_d27_tTZZra2G9bvxI5mwaBILAgw_51JQCEW0MLG87XsNPeRvjo6zpw_eNEt_45GoyOX6Bfgsbfhq8NnHUieHa2I4iwZdGGipda06j_yNUd8qv8x5rDZ3jovPINnSSUor63OxEu6CfHQQgp8n8Q9AQvgsT-ryVsYvGHalkxpDjHhDL0PZsS7ov1EmMGU27ww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فراتر از سم
😂
؛
🤣
چالش بازخوانی نام بازیکنان تیم ملی ایران
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/Futball180TV/94168" target="_blank">📅 12:47 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94167">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3cb354f20c.mp4?token=M3C9tiaWRxdv7fOCNSSvtjgYQwN9KMsRfMunNYQNFsaRiBQwDqpPnlw2lmpDuhL4rSKYmank4kCkbvdO9zOaE9CR63CIJ51fJjxkbTIdwLc_egV_cI1Nhwd1X94vYiCTWfVWBUEF5wTg3xi9Y1ZfqCFfv2l9SKl9G9sdPLZinS8YlUnn6I2TXY1O6lFDIwq5Z6E9pgJkieURSAlmDLFB2jF1Y5ttR9D1WhniQo7Xv8GTFAyjHKMEPVYBHikpe1KXz4lRn1OoBiQ_Jg9Qm0ma6-K0mw3P5bHQXPXjwwWo6SoQWmWyYfsImwc30OuGfAmOXTYGYQfWRt3yaKjCYURrqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3cb354f20c.mp4?token=M3C9tiaWRxdv7fOCNSSvtjgYQwN9KMsRfMunNYQNFsaRiBQwDqpPnlw2lmpDuhL4rSKYmank4kCkbvdO9zOaE9CR63CIJ51fJjxkbTIdwLc_egV_cI1Nhwd1X94vYiCTWfVWBUEF5wTg3xi9Y1ZfqCFfv2l9SKl9G9sdPLZinS8YlUnn6I2TXY1O6lFDIwq5Z6E9pgJkieURSAlmDLFB2jF1Y5ttR9D1WhniQo7Xv8GTFAyjHKMEPVYBHikpe1KXz4lRn1OoBiQ_Jg9Qm0ma6-K0mw3P5bHQXPXjwwWo6SoQWmWyYfsImwc30OuGfAmOXTYGYQfWRt3yaKjCYURrqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اظهار نظر جنجالی سباستین ورون, اسطوره فوتبال آرژانتین: مارادونا از لیونل مسی بازیکن بهتری بود/ او در زمانه‌ای فوتبال بازی می‌کرد که حتی زمین‌ها صاف نبودند ولی او رویایی بازی می‌کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/Futball180TV/94167" target="_blank">📅 12:41 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94165">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G1CpK8M6ukQNQ_kOxcLmlO3b019V8lhdffv3vqHtsSiuu4zJjoQkYB6G2ADsdBUY-3BdsRJSlSWKp4FOgPRV09o8B2VJcDGeZBMR2Vo6anlmbXkbTIcPlPiwxH2jMwnCsRwUnXPhTFhlZY_4_uMUNWGDLtyCBhyNl2WPP6H7_a9JxKZNwoNCgavszd7rZGJakf56V7RiJk1qucTouQAkkkmPdsr21IQC2BPd3bzVevsGoipCKJTrU2bdFFtQ9ArjgOfvyhHeTwjvbhbXPPlAjuUXEHO9NNMh7nMLR2amQcix-0XfP255vJOZkZ-9ls9-N0MKfEuieU_g0s7T8lT97g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
🤣
تو ورزشگاه‌های مکزیک یه پیرمرد فوت‌فتیش بجای تماشای بازی درحال عکس گرفتن از پاهای خانوما بوده که توسط تیم امنیتی و اخلاقی فیفا از حضور در مابقی مسابقات محروم شده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/Futball180TV/94165" target="_blank">📅 12:36 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94164">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mFVcfWZCoprSfrjOdjwNENoVQ7_F-U8234m24-TikXsIBNo1K8HW8WAlZb7X0FG5nbk5Y46gd6o5WGygPTehiuvtoO-OyOdjHHCt-EiPKc2d15nKfFYabacInojVStg00AXR_VB9iJrK0KVaQcunwRYTB3gJOrkxA-9cK2ugh5eG4orlCeBUYMtdtTOJycgztxNrIKmkBohjjUcCJcTbbhcmtfH7zgwrd2lRagFkWFttFp7PU_6OTIcwHZVONIWCq6Z_VjLtTFrBfEK2QSW8xxcRZ0IcD29V4R1kV1643Sn5G33ZedFQEA3ImvEb48JwfNlIoGSs-dWUpEpDkoXDrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
فوووووری و رسمی ابراهیما کوناته با قراردادی تا سال 2030 به رئال مادرید پیوست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/Futball180TV/94164" target="_blank">📅 12:35 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94162">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OjQ8UuRqck7FlS6RKQFRg08DpD3JKxn5AmRULDn0TQamWjai-cqrIaODN0X61bbrjSLwY7RBEj2aah1iuVM9EK1qZJNeA9OtOay2eydbBMPnpTa4YtlS6MOr2cokxJE9fU1gmzI26zwOLZJg0vaMo-zN36Wxszj1tfS4KPQVHC6wH9-bTVCWp0AYMsEBu_B5dc1b2EzplOnKLjmXi39cNMXr7GyYZRJxpfAh_VfUHOIHwMGhB-OPrexWPB4mG9wn73dySztQ8QJzMAXwfQzlPcXQQjUMMYSRe9zYyQgRnnaYaVgzce9CsP0du4K6N8oAO_gY-mT0RsMlYax0vV-faw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
🎙
مارک کوکوریا:
رئال مادرید یه ابهت خاصی داره، واقعا سخته توضیحش بدی. هیچ‌وقت نمیدونی چی قراره اتفاق بیفته. خیلی کم پیش میاد کسی بتونه درک کنه چطور رئال درست وقتی همه فکر میکنن کارش تموم شده، برمیگرده و بازی رو میبره.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/94162" target="_blank">📅 12:26 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94161">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5767fe2278.mp4?token=VQ9U_W1ZkRa7dGMSqY-0zlGaX7GUFYOZnX1YI3x7sJebaZcXfHnxSHT0YJgP7qyUTosVTHt89gF6gABWB1lM4HOfYH6QO0-lIvWyE3gn-DpAYed9DRgsAhZBBeJ_gXGen9Qacg3Y9hPtfvbrI2rpgoqGFGgxtBPdR4d2CaTG-fvLKiIQZjpYE4STvXY8FICx0IRptIy7lo3KCXEHRlCd9Tr-Qmz6gHPIUM3Xs-ir1SDv4MPtbqTUNzF6xL-Ccfiu8LWQjgDdC_XHP6EE5fmzx6bV0T3rk180vG1qe4M9pRp2bN_CIiqZN8XYE08e8yiEp61WLEbQeOK3T87U5EYa4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5767fe2278.mp4?token=VQ9U_W1ZkRa7dGMSqY-0zlGaX7GUFYOZnX1YI3x7sJebaZcXfHnxSHT0YJgP7qyUTosVTHt89gF6gABWB1lM4HOfYH6QO0-lIvWyE3gn-DpAYed9DRgsAhZBBeJ_gXGen9Qacg3Y9hPtfvbrI2rpgoqGFGgxtBPdR4d2CaTG-fvLKiIQZjpYE4STvXY8FICx0IRptIy7lo3KCXEHRlCd9Tr-Qmz6gHPIUM3Xs-ir1SDv4MPtbqTUNzF6xL-Ccfiu8LWQjgDdC_XHP6EE5fmzx6bV0T3rk180vG1qe4M9pRp2bN_CIiqZN8XYE08e8yiEp61WLEbQeOK3T87U5EYa4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🏆
🇬🇭
رسانه‌های خارجی با انتشار این ویدیو نوشتن که غنا دیشب به کمک سحر و جادو هواداراش تونسته دقیقه آخر پاناما رو ببره
😐
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/Futball180TV/94161" target="_blank">📅 12:19 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94160">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5190506dcf.mp4?token=tARs22CelhTIQSBQBB3Uw1lMwoXBBvrZKt2vmhc8YMB8ueGQRHdRB75xE48gGwV-R8vVqPD_vc71jJkOD2BVd_x_Buj6U-dUqRML91n7hs6Jps7_KwsJhRPToJtJnhWVnSaZbmIrTlr4_DupMrYLJojISL65U049vbcEIKKzlcSDipB4h47fS_iDAMu5o8tWKuJVfM1W-gXGk-uMjZgg4EJ2ZCIj4SgmfeW5tGRdKcZdxTOpyBDNzBjq15OU4g6FFrhLpW5vWKgoBImJ2ThgReGSvpV4Aq6bd6ZIroCD4TlfzSgIeUju4tD8adpLRmfXVcVyjuwPGp_CJaN-ncLbZDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5190506dcf.mp4?token=tARs22CelhTIQSBQBB3Uw1lMwoXBBvrZKt2vmhc8YMB8ueGQRHdRB75xE48gGwV-R8vVqPD_vc71jJkOD2BVd_x_Buj6U-dUqRML91n7hs6Jps7_KwsJhRPToJtJnhWVnSaZbmIrTlr4_DupMrYLJojISL65U049vbcEIKKzlcSDipB4h47fS_iDAMu5o8tWKuJVfM1W-gXGk-uMjZgg4EJ2ZCIj4SgmfeW5tGRdKcZdxTOpyBDNzBjq15OU4g6FFrhLpW5vWKgoBImJ2ThgReGSvpV4Aq6bd6ZIroCD4TlfzSgIeUju4tD8adpLRmfXVcVyjuwPGp_CJaN-ncLbZDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🔺
حمله نویدکیا به قلعه نویی: وقتی حسین‌نژاد رو دعوت نمیکنی حتما باید از لحاظ ذهنی به خودت سر بزنی
‼️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/Futball180TV/94160" target="_blank">📅 12:19 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94159">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lasH0P2OZwgr-wJno2M1qyLPDZ-Gt_Vly2C2jqwfy71nGQYtWsOgGg2JPtuw4-qzr-bNlstGa1kwPNtihweKtDwMY5wb5kueIuntC_jWWjFyBB2LfeY6lJUaWIMuJ3v1ylbs6Ue3HyBHJCVxxSlyNtF9i967jPxEMgJVONTFuT8RCyLzVJOChZSr-V_2yII7jX9Vu_cGMFxTEMiUj7UpkF5rvHhJc3X33oHU6e443B8joXL8-JhiTnJhfOHf4UYjXOZBJ1Yq-eKwo8zlZn-ZPpg0_RY5xlK0eB5rzOvd3i7vbgh-AJqT-Dei5JuagIZWgpz3dwFmqr6sTYjLPHLpmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
📊
جام جهانی ۲۰۲۶ در پایان هفته اول به میانگین ۳.۱۳ گل در هر بازی رسیده؛ آماری که از شروعی پرگل و جذاب در این تورنمنت خبر میده.
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/94159" target="_blank">📅 12:16 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94158">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/Ac_WLBrVeqb-9rpL8ePgeaefuTpmRpy_9Vd8J2_a6Z2kgKQaaLOVBnb3WGzM20yKL8ZSyZnkMwXaDFv5NLpBYXgkME5qgaRWJF1kKoOuVWknvFkhYOst8uP57L9hOmwv0sMxCL1GcVHKZfnXeZD3DVFn2pRZS3XxSiotOJQsDX1_WsL2wp2QoVRZWBBC4ObyTMzKs4SIM7S7KBaaSj9uv1JbTrJ4c9uOG7A8zZK5bQ1hcPqP7IOoMU1NppO3GpAO73xTAMKMzzoSYX_e1bDz8gfrPRK9ZWewmOlqNet4dL5s7CArLtlLAsehsVRgC4uoqStUTX8xH3z0BKXBPqVhjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نابغه خودتی پسر بقیه اداتو درمیارن
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/Futball180TV/94158" target="_blank">📅 12:14 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94157">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R8mR1a12y8o4MRbzkL55vmLZQhfe5ZsHefIhW6oZOaGJwoKIj2F9z35ZXpiJAG0Tq_icxsDbhRwOOpvaP9o5i94L9q8PJprQwjFlpSZiTZvRwRv-BlOuDRGvCX37I0POICw9uH8d8UpFc5OcZzxqDnemIvuZxNOhXn2U9NXgBf78YDcYBjYP6NltGysJYM9AlGFpBPyESYlTQSlbNJZxyKOwf_oPOCnz2MvNycK81_4-6ANm7reEI1d6g75i8EjCTJgEdRene4c293mM_RGGQT-Np9IKxudiQ4d4oWoiyQ7v86ys7xRoRfQNTyC4c1yWFQlKQQGoIktVYx47HvZbwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
🏆
رامین‌رضاییان در تیم‌منتخب هفته‌اول مرحله گروهی جام‌جهانی فوتبال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/Futball180TV/94157" target="_blank">📅 12:12 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94156">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qt-r9ugzl7nDAgidZxRov56TnvrEJcvyMFL8KlhWYEUgc6eIpSgRWB3W-7dMJuTsyeIuq8248y6tchDKxzC7ucJv0VNjK9Bs_NBIpEICsuld0_VbItSgecmgkhfFAG4XDvEtGzQlS5TCY3HVEwQC0pnqtUibR1xW3Vz7b1MJ0hg77or3OAM2dkKu7XL7kqSKtSOADatc_BZxZ7iDyTRi5x2DklFumgRkQ5gdd4sChpHh9p_mHcJ9oY6322Eaf6vCY6ejQ4_gRFp_swiS_1aVFQGQmoaYxSaXJ92c0GLHDqN2r3EB2hJHVVcXjO9xeF_U9CA69ByQEaHBR6Aknp_wCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💥
🏆
🏴󠁧󠁢󠁥󠁮󠁧󠁿
جود‌بلینگهام ستاره تیم‌ملی انگلیس بعد درخشش دیشب مقابل کرواسی با دوس‌دخترش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/94156" target="_blank">📅 12:05 · 28 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
