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
<img src="https://cdn4.telesco.pe/file/Een9M89h075l2uT2fEb4VfdGRLFTwopz-4TyYCNJh3rKeN_NK87iucyNujJ7NqWjhdAewBAuF_BeaM9DYMGeVMSvOzgg8RdTl3USe8T-yieHOGGFGQ6YezKM-F3vgQPG7w5i25PA86Yavt3dJOgcCo0BmGey_XNEd-DO1rhcCau8J9Qty6aoR98MArrDptD0NXWDtplXFAXaCTc3LNE-Q5v5F2DkLJfU4WHeXv_4GIq91hcxuWFT5rBx3yInBrrK46v-gp9t4dc5uNvOPZj18KXcr4w7XuclLrfAhRS-BrXkV2mgpo7oLM31yoBwl4QPjTugIS9gLooqtzXB2gKyVw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فوتبال 180</h1>
<p>@Futball180TV • 👥 133K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-29 03:27:44</div>
<hr>

<div class="tg-post" id="msg-90060">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">تو چنل بتمون هرشب داریم به سایتا تجاوز میکنیم
😄
ما هیچ فروش فرمی نداریم و نخواهیم داشت و کاملا رایگان فعالیت میکنیم که کنار هم به سود برسیم
🤑
🤑
🤑
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 564 · <a href="https://t.me/Futball180TV/90060" target="_blank">📅 02:08 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90059">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/AEb19xAMEueVsMXICRTQhuleuJkzEClEIqGBrCYNV790KPZTvKXfDwJOQuR6jKr96JzMO62DgPbRaHLKY5T4DOrWOBGAfJEjrFg8qh6sIojDY1clZxdxXgHxIYljG_3oGOvcp90rmxGYFU2Pqe4aRhr0GpaPD9ozZlk5zqUcSKlsVtfh1959HsrB8K6cNNTZpkoYoZQTQz_q6eBOeVLPterk_w0OcCOyoa1ve74-l8oCLjGwZr3f37ciWV3q4EfV5jk9_Qqp000KmyIlZHvW7p09sPsQALrzfL3u6qW3G6zRjFj5oXv-ES2J2lfgjt7niFnGk2OKEUpU5g-O-mqc1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تو چنل بتمون هرشب داریم به سایتا تجاوز میکنیم
😄
ما هیچ فروش فرمی نداریم و نخواهیم داشت و کاملا رایگان فعالیت میکنیم که کنار هم به سود برسیم
🤑
🤑
🤑
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 568 · <a href="https://t.me/Futball180TV/90059" target="_blank">📅 02:08 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90058">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de7e2f01eb.mp4?token=ZGDl7daw3kowTGyQMnyx7BKg1rLPt4df287pi9ipduIoFf46oqtWQrdPoXREQLSXGDxMuE651x6nglsywHtSa6T7SiVW_5G2uQRcgzLzZqUjFMLBBxpHLuk9598nv5-PptzpSs_DqguH6-81MJYgHWesBdxw7d9NPAcuZ7L1YtBDXtc6q7yjSg5pcGSr198QunuMtJyD9WQPPp7gcJg0OKmbtu8VFVlIBiLMBF_2cNkBLn94BXLn1lrUi-z37Q-z8SRaKrBpBRzOAN11MJJsGmSLKwGrUq6uRKnI2OKGatD9Ef8LbhkkKsXUUxeVXv_c44OL07R8RyK7-Rzi3t0ZVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de7e2f01eb.mp4?token=ZGDl7daw3kowTGyQMnyx7BKg1rLPt4df287pi9ipduIoFf46oqtWQrdPoXREQLSXGDxMuE651x6nglsywHtSa6T7SiVW_5G2uQRcgzLzZqUjFMLBBxpHLuk9598nv5-PptzpSs_DqguH6-81MJYgHWesBdxw7d9NPAcuZ7L1YtBDXtc6q7yjSg5pcGSr198QunuMtJyD9WQPPp7gcJg0OKmbtu8VFVlIBiLMBF_2cNkBLn94BXLn1lrUi-z37Q-z8SRaKrBpBRzOAN11MJJsGmSLKwGrUq6uRKnI2OKGatD9Ef8LbhkkKsXUUxeVXv_c44OL07R8RyK7-Rzi3t0ZVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😍
خوشحالی مارسلو برای نیمار
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1.45K · <a href="https://t.me/Futball180TV/90058" target="_blank">📅 00:49 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90057">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wco2AxFqA-v38KFFTyR4-gPXUx53vvYrxLh8x4qC4xPCDbQcN9BU8SikmBjKReQckoPusw-1WvcEHQg0ZisTGtGcUO_aVekNNxx7_fY9pVQF1s4FEm_oqBUdmvpL_qXw_0CfIRC7c-xX4eFoc_ib9XvORSo2sDibIasOQWOhyPNfNdBLDvIsNU7ybszPFcPI4SoDsQPZP-dr0WMYhwnel9gialQxvz7pFiWhwtgwxjlFUp9Nge5okqiU_XKyan7IdldpzfWIIqsYwHeygYjEnpBB7rBIM6oIi1BbgDfGUpu1jXCTvqRvnlPvn-8vQVHc0F9PvKjGwbtI-2XmY1PfpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدول لیگ‌برتر انگلیس پس از برد امشب آرسنال
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1.58K · <a href="https://t.me/Futball180TV/90057" target="_blank">📅 00:40 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90056">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EteriKruBiH7ric3fJcPNAwytiQzf--zPlf1_wZHry04i2Fm00DeV9lGGXdC9n1S0JYjykob0M4IUlwMwrCPr3KT5tH9eyEzaiHim3hmtdkta0TXROI-s5vWzi6yCeATur9wxDiKAB-t2zmbHXckR4uTrvaZwDjZBGGzEx5VTBrPVYRKVqXmixoIiPboTjLDlddJV1za0nrZSA57s9Lm491cMbgsZPCEZ7Q_qS-CZMr6QeC5Bub3d6MKr49vRbacwUGoOwmYySHyVm0WoVkY9gtFGYe6Azp7I1_wt-kPvY8ujKX5lNixuddloHGodyElqufOxXMAPaLWlc60YPnB5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇧🇷
لیست‌نهایی تیم‌ملی برزیل برای جام‌جهانی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1.68K · <a href="https://t.me/Futball180TV/90056" target="_blank">📅 00:37 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90055">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D5A3TwBXIsOtkQuVSMbuIgPyn1Kz9qch2lwWJohg0MrSqobjBO1NVFwbnsHFraJ_ZkX-4a_1Hr01hzC5aCnLCIpQjMQczzjBC7COs1A2FGNlYvgsdgeHqmFWN31e_Pn9OpN9xJ8vD7jINVxeUQl4Yp-kvtA2KnE7QtMln40xz5c85Mh-fNjbhXg_RvHVKkcM61tU4FVDcyAEjGVEuZx9UEAL7emJxSGmeY36pJ_jd5Jx1ZNhHJ69LxzESyUqHem_srAcPynCF15Ov4qo1lKDpVPG79N4OJJarmCBdb3Y2nE6lkwO9wSaaw2_w4B2LGSPmRSaEwXk4eW-t7Aujf5ASw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
نیمار بیو خودش رو به پرچم برزیل تغییر داد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1.72K · <a href="https://t.me/Futball180TV/90055" target="_blank">📅 00:35 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90054">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6072fc8645.mp4?token=WnPu3gQIyxWz9YrCXULkxG2c9OEiL4QjuB-8wSm9p2iYe13ts0ePM6DzXEVuR6Lp2YHzBF8W2w82Cjkjx0FGKG0E8SoambH8tt94POPpfW4nzGm6UlvmYxshl_FYjZU4did5XQhxuPKrsgwOfS8fNbJzKi8YxPpCKxdrrWo4444xSi_QrQRwR9VNvNgdO1i3x2ST_tIMIqNr32VXR-Ktkk90Ff1H5yKChBoK7iqC_z6D6ho5RQOIY37bULd-vobWweupMUiN0NII-X3E3flm7cLKGAaSccdKZ8h96NRKYfZUBgImkkcc8pBeaZdfNu5CK2YbsB5z5CwEBlathEi0yA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6072fc8645.mp4?token=WnPu3gQIyxWz9YrCXULkxG2c9OEiL4QjuB-8wSm9p2iYe13ts0ePM6DzXEVuR6Lp2YHzBF8W2w82Cjkjx0FGKG0E8SoambH8tt94POPpfW4nzGm6UlvmYxshl_FYjZU4did5XQhxuPKrsgwOfS8fNbJzKi8YxPpCKxdrrWo4444xSi_QrQRwR9VNvNgdO1i3x2ST_tIMIqNr32VXR-Ktkk90Ff1H5yKChBoK7iqC_z6D6ho5RQOIY37bULd-vobWweupMUiN0NII-X3E3flm7cLKGAaSccdKZ8h96NRKYfZUBgImkkcc8pBeaZdfNu5CK2YbsB5z5CwEBlathEi0yA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😂
🙂
شکار لحظه‌ای صداوسیما از بازی امشب آرسنال که با برتری یک‌گله این تیم همراه شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1.96K · <a href="https://t.me/Futball180TV/90054" target="_blank">📅 00:28 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90053">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E_S8wsfzAKBxX7X0XcEWZ--ODnvrDWGeobah9fEsJHL49-hiUt1JIRAKrolrpfeYzYAQKqjg9GBFoZk9V2gRHoh3m-0pKfyTIyfEVh6I7bn1emZhlqjHezEaLThPydcTSiDYzcA3tl9Mlciy8xgf3CVAW3ZvQGaLiJ9IrxQyugR-8nYJBYN5ON3RcnKBvostOVcshq5HDmvPZWb8JOZSK-R0aO0X8d--CptFjtyFrHFv19gKjxNKWd52x39u3aSkAGMAhC_G-ziDTxijFBZVHbWZ_FtBUmQ_R8wAVlBJQ3ir1YLfBMwNoQUzN2k43Sxd70pn4IaTJmqk9EB4p4hlng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
نیمار بیو خودش رو به پرچم برزیل تغییر داد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.08K · <a href="https://t.me/Futball180TV/90053" target="_blank">📅 00:19 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90052">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🚨
🔵
🟡
🔴
با اعلام سخنگوی فدراسیون فوتبال، سه نماینده قطعی ایران در آسیا در صورت کسب مجوز حرفه‌ای، استقلال، تراکتور و سپاهان خواهند بود
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.86K · <a href="https://t.me/Futball180TV/90052" target="_blank">📅 23:40 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90051">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🚨
لیست‌نهایی تیم‌ملی برزیل تا دقایقی دیگه توسط آنجلوتی در نشست خبری اعلام میشه
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.85K · <a href="https://t.me/Futball180TV/90051" target="_blank">📅 23:38 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90048">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
❌
پپ‌گواردیولا سرمربی اسپانیایی و پرافتخار تاریخ فوتبال از منچسترسیتی جدا شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.97K · <a href="https://t.me/Futball180TV/90048" target="_blank">📅 23:32 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90047">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fqkninX3ZT5_t0jr0ob_S3eoEydF1TPU6RuHfmSdIpN0ZId19qY9N9fY5kvCzbIdlSwarGcIy-M-cJ0w4SiUSKcvUKA0V6SP1opBvZrg1KKlMIPOdoxAEmbBuGAsSj4U93sTYQehouCxRvPlPw6ukrOB4rlRBWJTiezW2HKLMnwl_5GxzT6hOtBOzm5JM0nIziNhI4eR15CeNiuH_a2RsmuxdZS70QI9U5d7Rb-ztK28fEs4cOHMpKYHaD_fAGr7SbkDishsnjjw4tXbhTOv5cPZeK_XMPyO2XZnHRHuQl_UVcFd6VQ7ReHncN08Loaai8JeJXWuoSuYksMp2nev4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
❌
پپ‌گواردیولا سرمربی اسپانیایی و پرافتخار تاریخ فوتبال از منچسترسیتی جدا شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.08K · <a href="https://t.me/Futball180TV/90047" target="_blank">📅 23:25 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90046">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🚨
🇺🇸
‼️
فوری از ترامپ: امیر قطر، ولیعهد عربستان و رئیس جمهور امارات از من خواستند که حمله نظامی برنامه‌ریزی‌شده ما به جمهوری اسلامی را که قرار بود فردا انجام شود متوقف کنیم، زیرا اکنون مذاکرات جدی در جریان است و بنظر آنها، بعنوان رهبران بزرگ و متحدان، یک توافق حاصل خواهد شد که برای آمریکا و تمام کشورهای خاورمیانه قابل قبول خواهد بود.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.45K · <a href="https://t.me/Futball180TV/90046" target="_blank">📅 22:38 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90045">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c28244d9b4.mp4?token=oAsUbCfWadZwW-l9A7iCibDyBLJFH1CbkTJWaY6NnBivsskVgjxpxweUEMdgCmuRjCYH7p7jGiGyH1HJE1ejWbWxAudAwRnncWN3k4N201SWhiSdQoCw2OFVA387iu8YHY9gpYN8lTKGhyeisChJhsNg1gLONxj07nv7PJX2ippRVFzgWVa4bk1WzHAprWb33Z1sh5_zGEIw_DGNEkFoHjIpwVl8aSAUsvHKSPV3qZba9sf3Ym3BNTLvH5f1cpN43XoCn6dRFS1MMQKzfUvczNfz5sFulVY2MunVaY4vTkVeCtgPlOtKt_fS5-ymAtxF4FYa83k-4rlMEZ7PF3v60g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c28244d9b4.mp4?token=oAsUbCfWadZwW-l9A7iCibDyBLJFH1CbkTJWaY6NnBivsskVgjxpxweUEMdgCmuRjCYH7p7jGiGyH1HJE1ejWbWxAudAwRnncWN3k4N201SWhiSdQoCw2OFVA387iu8YHY9gpYN8lTKGhyeisChJhsNg1gLONxj07nv7PJX2ippRVFzgWVa4bk1WzHAprWb33Z1sh5_zGEIw_DGNEkFoHjIpwVl8aSAUsvHKSPV3qZba9sf3Ym3BNTLvH5f1cpN43XoCn6dRFS1MMQKzfUvczNfz5sFulVY2MunVaY4vTkVeCtgPlOtKt_fS5-ymAtxF4FYa83k-4rlMEZ7PF3v60g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
لحظات احساسی لواندوفسکی در رختکن بارسا
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.73K · <a href="https://t.me/Futball180TV/90045" target="_blank">📅 20:12 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90044">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j0VdbEFWm05zo9luwtcu7neptdsXcvXUw7DGxTQdtXs10ymVNRzQlhy-vTClpZ-jX9l5YT-_4TjmyRt93KlNlaXi8WdA5E8FkLSXsI5X1dhn0GYHEyhVmQUUUFfI6Aj75YIoBpd9xoLZM3uR9oZm_5NBbsJSQPIT0kKNJGYJBFlB1cjisksDx5DoQAwMuMoovN84fX6fUH2VZ5fsBhcCkLbvYi31TX154OYQ6GKA69ammCm2nGk0M5H1TYA0FEkgQpDTtb2cATVwT1cbFnu0dT5SofhMeY6GHzmPQDFU-KDbh3Y703Z8qPK9riVF2f7RcCn8wKyfrz4SG5fA2Mp2Dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🔥
عملکرد ژوزه مورینیو در رئال‌مادرید
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.41K · <a href="https://t.me/Futball180TV/90044" target="_blank">📅 19:57 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90043">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">51.9 MB</div>
</div>
<a href="https://t.me/Futball180TV/90043" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 3.09K · <a href="https://t.me/Futball180TV/90043" target="_blank">📅 19:57 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90042">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f4KgiqTCVidTCBAmWNK8h2xWj0nv_dNMDpr5f2pfpM2KMsOL7caW4nlUMSDKV30M-BklLiFRa3fbWOp0CEB1-7X5VWOmI1jur3SJX2SbSYvmGKRJNsnX31ixKqxNjoum9k0jNXh-SFP9us8V0hk-OBfh1Ck9PNHm3p7ccm4it190td9RiOBrt8b_thyPzDCwr3yh044nNHea3T4KhqEIS_4lAhDuzBO5NVtUXt5oTsrGpB5ZAcA7SCSBsmJ3JjRy03BmONIf4SKLEifRw-A6-XijpzYiLLNXxL7Kbv-cy0ezl4OW5es8N4gy5JLib5OH2ak-JQzqVGtS9gHsgrASyg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 3.09K · <a href="https://t.me/Futball180TV/90042" target="_blank">📅 19:57 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90041">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fo_BXyBo2bJ3LByr1r-OZc6pTQ3iyYG_3_VTgf-K7BWQgO9phDK_trW1BtovJd912rvZLNO1P6fVxAUVFS5Y55K_OWOcDfhjBiM6NkA1sKuvd7iiXuBXulwehXBJmK8inIVHmt7TWx_r9tBsrlpyMQYB0oy5gwh4grlyebRVvTq1mefndymQnqeD5iY7m_w2bJY6pLDlVRVFBEvuf7tmtPTc_IkTPkB9OoWnL0FGOu0H3d2DaXEXxVGlwLdACJ-tVx6LhxlQN0La6AqjXhbmn3UWjMTEdcIyJnHDVM8kLYiLEILSfgel3HqqQ4spbYKykFe43v2OrBMHYxLJOEX3yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
تیم‌هایی که تا الان سهمیه حضور در فاز لیگی لیگ قهرمانان اروپا 27-2026 را کسب کرده‌اند.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.93K · <a href="https://t.me/Futball180TV/90041" target="_blank">📅 19:46 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90040">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/HuzcXzdnmqGrOZ78bWf6bDRMY00fxfLCc1EbWu78rzFtW2bywvo8FSLAEiRV13iC7eR6Wjlngm4sfAUozPnOnfVIkj2KWGfHECVcyYNxt-lQLwc5pLwrbpz0N8Rz5nwJcxShuQ3D5oNX8-JyiQI7t-deQJXQdXgRhCvw9RH-jLFam2N2LslZDP1Ang0pzF8YtfJmAqG8e3pPeBMawr3VTydH8N0HkQmsVanqrEs-2t_HzP88bJ7SNRHW-6_3uDgOiI8sgPQyjhP6XHJ41Vug8ye28ygdN7u7shmi0WylQ3WBcoutOpTGV4NCYgkUU75G3wcGMJHWKPA-lE69eUR_PQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تخفیف فوق‌العاده - ظرفیت محدود
سرویس اقتصادی با کیفیت موجود شد
💥
10 گیگ فقط =>> 1,700,000 ت
20 گیگ  فقط =>> 3,100,000 ت
40 گیگ فقط =>> 5,600,000 ت
سرور ها  v2ray هستن کاملا با کیفیت بدون قعطی
خرید
@amoadmins_bot
@amoadmins_bot</div>
<div class="tg-footer">👁️ 2.87K · <a href="https://t.me/Futball180TV/90040" target="_blank">📅 19:36 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90039">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y8MoObGq9MKvi3fQlaBt8vRQjjojVJ1auP2a-6Z_8zg3W2GqrBDAKWuohXqA28-Z3bFPn1kunU2ocGBWLsHkJRdQo2VDkshiNfW7V26Ezf-SfLuKHPX11fQvYbOvtKdS210eQ6Ue8lKzAxYUKIKvY8QT8Ub886cU5nLk1uBVHVT7fm8GrPAjKFsPXmdpe8oTZLQ8dFtTLMmslEcvpsyTlKRzqkpgqU4U86VefttEZ7ArcmARBDB-t4uWWfCjQhBNIq26PW3eX4P4f0JKHVzNrdS_y2wu6iNS87ame0gdL0GE1X9t-T7nqZFyNoU46-bsgZaRWpgrmmd3mKN7qZ2jXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇭🇷
لیست تیم ملی کرواسی برای جام جهانی 2026 و پنجمین حضور متوالی لوکا مودریچ در جام های جهانی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.25K · <a href="https://t.me/Futball180TV/90039" target="_blank">📅 16:21 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90038">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZUo-HomXzjbnxHWjPHIqlEDUC-TumDdaKIOj2Ku2W1-b7SxEOhLKoxyIunFMHGW9kgBxC2NIc7-XgLcvfK56qkfSWngkGTApmJl-YID3D80oUw_mCuGsN6qT9UBNB4ocLyUwea-BfyCb_UB5bBqtQS5jgixnF6p7Uplw-qBgulzWyhQ6ZyWO5VMIAoju1ZVRhvVd0E7kZR6RCHXmR6-duOFFvWnGyHZwu01bxAPlX6TJ0vT9eg39gAJW_9Wsh9YtnV_-pNWjN-a9nDeZKuw5I70wjIcx_mIYPyCYL8S1xm4xZJ9LQ0nQ3aKZSyZVcBjJiDHy1yYpPgyhn9TNgxY63g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
رسمی: هانسی فلیک تا ۲۰۲۸ تمدید کرد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.06K · <a href="https://t.me/Futball180TV/90038" target="_blank">📅 16:20 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90037">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/b5E64H_YE_QolnQINmNyqlCEImP5zN46qPC2IMCayerN-XtyOPTfIM-0X_RbPLSPLJgR7pk4nooVym3scgyMX2cbKyAJhOiTJmSmqdPx5A9vlHarPJhkCQ_3d3kQX-yjDhwOZ9A0yja5_q100z2gPZHpYVUyKsTJGcZK8E1bOIw5_QfuqYe0tjCM2n9zWxlZj5voDhZdxAh-JDcEx4L9qDl6B_A-iiEKQPvXCVwOEMMPPTLC_ifDxF_YaUBzOQfm6_QoQUWptNPO8ye2tSqLV38UEjPVAr-qOJoQEqOkaf74th9mlFOB0w-aQHi-klvkEaAV5GwG3j7abrsKny812Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
رسمی: کارواخال از رئال مادرید خداحافظی کرد.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.01K · <a href="https://t.me/Futball180TV/90037" target="_blank">📅 16:18 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90036">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ryPaqB1dj8KtuqUko16nj2IkcwBH98cHe8W1uBFLDwDHWG9ZzprqcgeSLvJXHxG3KMjMzz9enBuq87EPjEXLkNRgzfHDaB1p5CkGOYDc978pO_E4E8MCy38MrTYalrFYe4d23h16d6WKXaG_D9EhN2MELqCoGzJwMX_91tZmwyPVfeSMjeOq_B3ox-3Jk83sVlnkHrwruhKiOH4owYmVn3OIM4zqZMc7GL0n_FA-KvIViQVuYWefDqdAioBP1vS9foqlAv2HHfbPUo1Fexgw7smvRoc6YWmfHN9_bgX6VT41iZN-vYKcUNM4RD8y-Oz0RC2ETmRYnb8oOKbqNkQxXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
هدایای ویژه و شگفت انگیز چیتابت
🎁
۵ درصد شارژ اضافه قطعی
⚽️
بونوس خوش آمد گویی ورزشی تا ۳۰۰ درصد
💹
صدرصد پاداش خوش آمد گویی انفجار و کراش
✅
ورود به سایت و دریافت هدایای ویژه
📱
@cheetabet</div>
<div class="tg-footer">👁️ 2.98K · <a href="https://t.me/Futball180TV/90036" target="_blank">📅 16:18 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90035">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CMgRTLqGKXHnb2SfK5rhxWfzvYhPeQ_bP98tsgVGqeUOYSaWR5MPZ637LisEgwD3kAFOWWqiC9lodv00MyoNxQJD_kmCAE7I4xa0HGi9shbi2zopcvw379C-CRp3JMUs14h2Zm9l4vtPbaDH-FMXrQ1a6G7zJubuPHdd37exZxK2eewtPyifVQtQAPlP_pePpkMOShPGe44tuvsvCU6_aXDxxDp6MqtZ0Cxm5kozKRpLLy0jWevzGSFNPkzqIYcbG3yYo1sOBN7cQY1G8dPeW5I_PBxOeDbmEUJkw0B1yg7Fh7ikKwbGbDxuTiXObj5ahb1S52LwAxwGitbgHYjwXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
رکوردداران بیشترین بازی در تاریخ جام‌جهانی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.17K · <a href="https://t.me/Futball180TV/90035" target="_blank">📅 14:14 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90034">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8afcf96866.mp4?token=HplyAZstOvwhOuKxEKNNIMQ3FsSeTB7rh7LBCjpC82DHfaouI9nK8IqJcPJM1Y-pQulLIQdxz5QmhY9pSA3T0L2oUuGyZ0TYYgsybsyokoCKJ-CfpF3cHQCaoRkZGFxneIfPhDX_dJJlzZq_Tgul-vAbvSXwQxgppk8HBomXdmtTZp3jvZG1XqHkQk1pShwcnuIpFqIx3lJkbUV8fJVIU3OJzplo8llUBe_O3J-3YIip4cz29aa4VjA4vvPynHPprGT7tCA6sSErIC7vgQC3kJMDgIjSJnET9xtj_kU_gqWoOShEI8rSKbkW3KrwyfAAkXy0zSpPgl9thbi7Jx5BKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8afcf96866.mp4?token=HplyAZstOvwhOuKxEKNNIMQ3FsSeTB7rh7LBCjpC82DHfaouI9nK8IqJcPJM1Y-pQulLIQdxz5QmhY9pSA3T0L2oUuGyZ0TYYgsybsyokoCKJ-CfpF3cHQCaoRkZGFxneIfPhDX_dJJlzZq_Tgul-vAbvSXwQxgppk8HBomXdmtTZp3jvZG1XqHkQk1pShwcnuIpFqIx3lJkbUV8fJVIU3OJzplo8llUBe_O3J-3YIip4cz29aa4VjA4vvPynHPprGT7tCA6sSErIC7vgQC3kJMDgIjSJnET9xtj_kU_gqWoOShEI8rSKbkW3KrwyfAAkXy0zSpPgl9thbi7Jx5BKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
📍
Tehran
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.17K · <a href="https://t.me/Futball180TV/90034" target="_blank">📅 13:30 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90033">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TOhv3fvRYrIDf9dBvhiQbgp2DHnG30551dWt6oaL3OD6Wlf4ftOblC6xboi98LeQdSC-S2fIanGbozBu_h5dsnFqIAmVm7eyLoF-V8qt5Ymk34xX2VMDfNu3xnEjqaDnU9vVRlqxbfmvhP_OJTrDo8glS87lQQN-6FeTi_9bOWqSBs_a-IMPl406kKA1iyFlohlHsy2IfCO6V1maf14YKrT2hdI5WuoTnRyGcvcI9O3LnCD-gcLZAv-yne8Z3_5fseOB26wjn0bcrRCgK3OtOcV6wlKV6ko4mwvLEKekEAuykfVLC5Acuy3rrmZzk8Sg4A-DoqOagHOrlhNt_HJ6kQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
روبرت لواندوفسکی بعد از آخرین مسابقه‌ خود در ورزشگاه نیوکمپ، عکس نمادین اینیستا را بازسازی کرد.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.06K · <a href="https://t.me/Futball180TV/90033" target="_blank">📅 13:14 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90032">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">51.9 MB</div>
</div>
<a href="https://t.me/Futball180TV/90032" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 3K · <a href="https://t.me/Futball180TV/90032" target="_blank">📅 13:13 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90031">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BiuWtIcWI0HZ38KVg9YGjzw-LULvy4V5li7E5uT_wZHKFWw-en6xOBqbpfN3SsrjIhKrtAxqg4dLzC0zcTYRByaUqoAcZX2j_Y2YvHojupXYEepBntuJkFA5_Sb4Kh0rZGCIEq2Ydk_o1n2eKkbac1NwR9vxUKmqFl3MvxhIosgaz00uGtYhnsa5MPtzyuZAHjG398SSXQF_cD0rUlaKtpT763TPqqvDMhAiLwgIp01yB4fHGheCgmOeBFpup5PLn1jnc_xFC-z9OYAJfsxl01fiNYwYdM8O9-J-Q1VFM8BQGLbnzJnT6DtkGywoXnnsj7yJY2DdVpIywVDM9n6gzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازی جذاب
🔵
بارسلونا - رئال بتیس
🔴
🔴
🔵
به Barça 1xFamily ملحق شو و با هر پیش بینی درآمد داشته باش!
🏆
فقط این جوایز رو ببین:
📱
آیفون 17 پرو مکس
🎮
پلی‌استیشن 5 پرو
💵
4,000€ نقد
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
<div class="tg-footer">👁️ 3.24K · <a href="https://t.me/Futball180TV/90031" target="_blank">📅 13:13 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90030">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c9bd4b703.mp4?token=S73_LN59Apb6pTNztVqXO_fiFC1y0Lf1fBHS0UjnPX3kiK7BnDgc0KBnNDBEXK4X72zx95i3KeuqFnxjqYtcHkCQ1LC9Zd9XB-3qx-ygAbLMuULOllyfDMg0J2B7vVLl4oFG9NPHNk-W6acqq97ixClGrrfso_NXz-FzIwTDhtLTkBHX4v_09UOKuMoJJSuGaqsklY5V6XQrcaV9UBeMvRpvjMvOCv-94BdmZrIGscMQbudrmwGT12sm3EBOC-vdQpl8FJZxvlcZExoazG4q6FsU6oL1z91v9um771MTA0GXGD-qmlxRLMjhzusqkYy88seHtj1bIesjDxJkvlmPJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c9bd4b703.mp4?token=S73_LN59Apb6pTNztVqXO_fiFC1y0Lf1fBHS0UjnPX3kiK7BnDgc0KBnNDBEXK4X72zx95i3KeuqFnxjqYtcHkCQ1LC9Zd9XB-3qx-ygAbLMuULOllyfDMg0J2B7vVLl4oFG9NPHNk-W6acqq97ixClGrrfso_NXz-FzIwTDhtLTkBHX4v_09UOKuMoJJSuGaqsklY5V6XQrcaV9UBeMvRpvjMvOCv-94BdmZrIGscMQbudrmwGT12sm3EBOC-vdQpl8FJZxvlcZExoazG4q6FsU6oL1z91v9um771MTA0GXGD-qmlxRLMjhzusqkYy88seHtj1bIesjDxJkvlmPJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">استایل متفاوت جورجینا، همسر کریستیانو رونالدو، با موهای بلوند شده، در مهمانی جشنواره فیلم کن
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.52K · <a href="https://t.me/Futball180TV/90030" target="_blank">📅 11:47 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90029">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Da8_u83xAAeiIW7AhA6Zg3h7sB5HK6riWomOhZ_HPwlfmJko5PYJXkXlKlnSgz1C_vE-X14_iasNnEIOfpiXsfuy1FXwHEyCo4MuZ44_RwaudNYqS1jV1UTQ481xLliKZv7Wr_hnJ73sIzc4WUdkiWA-eK4w-20xNiLlqq0_eh3kgnEyAMiNr0cLL2U4JSloF5I3utKpI4UTUZ5ezD_c6qxq3TVpw9Ui4NrozqxVensT45O3lqcByr4NPlL5dxTDJOu_Aq5bScMVUqVvX2uZ9-g6lcvT6PNuInOA3Tg0UgCQFdeLNVMpgB0EpXKZDTvoy14QB544vThj1_zEJeagkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⁉️
سرنوشت تورنمنت‌های رونالدو با النصر
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.9K · <a href="https://t.me/Futball180TV/90029" target="_blank">📅 09:35 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90028">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/441c980280.mp4?token=QlPoSOf49TS56lt7vvvL67icQtDHwyoKHmi95OSYoeTJnBgl6tZH8bxIv57VurlUqyH1zGxysND4DY9e7exqQfJHgGurfC1VtUYqrBJ846cGMrPSDx5V4MUFbvGLij24vWu58A4DYLtAzBMDkvJqx_KGgf0SNRN4YnSQwP7eVQblnxz_aYA86pvSCSCgMS0s6DqpHam7p1Ph_mLuYSqKt_CaSgC9MT7m0R54xwdX2vI3GSWXKRCvhqejaZaTCPejZFpiFmDOjYqw1Y1CZgLc7I31P9DTub2Yf4k3Y98__DfYOlrFoNOGyR90NQZxZ9gC1kYtjeM6me9TU7riOBz2ow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/441c980280.mp4?token=QlPoSOf49TS56lt7vvvL67icQtDHwyoKHmi95OSYoeTJnBgl6tZH8bxIv57VurlUqyH1zGxysND4DY9e7exqQfJHgGurfC1VtUYqrBJ846cGMrPSDx5V4MUFbvGLij24vWu58A4DYLtAzBMDkvJqx_KGgf0SNRN4YnSQwP7eVQblnxz_aYA86pvSCSCgMS0s6DqpHam7p1Ph_mLuYSqKt_CaSgC9MT7m0R54xwdX2vI3GSWXKRCvhqejaZaTCPejZFpiFmDOjYqw1Y1CZgLc7I31P9DTub2Yf4k3Y98__DfYOlrFoNOGyR90NQZxZ9gC1kYtjeM6me9TU7riOBz2ow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤯
جادوگری بامداد امروز لیونل‌مسی در آمریکا
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.11K · <a href="https://t.me/Futball180TV/90028" target="_blank">📅 07:41 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90027">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">تو چنل بتمون هرشب داریم به سایتا تجاوز میکنیم
😄
ما هیچ فروش فرمی نداریم و نخواهیم داشت و کاملا رایگان فعالیت میکنیم که کنار هم به سود برسیم
🤑
🤑
🤑
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 4.4K · <a href="https://t.me/Futball180TV/90027" target="_blank">📅 00:30 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90026">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/FPli8tzQjWpJ4pMeZiG-8FTAhci0UROnnaAd6YWRS1vME7135Su3-jp1ssSV3aA4-n3hOcV6uFLswjXl41gLr5BkpW6C7EDADpxvD-vYZj4REeBOA32QIGZJseST81j5OWy2UIGdppVzj0pbA_JOcHvz_T88-quP8IsMU9n-GPkp4lkzhCb4E1CX2WUUntVlLF1pWuK_xX_pjPtpmyS4rZDmqAcnsa_MRqAlc9tgybWO7JDg4pRDZqkP6uNvjamzUoMB_xbedl6g8wpHjzSWqaU-BiLK2OmMiWyjXC9LcL4Bz6zL0xZztFBovXcTE-WXLS5g4XVJZMLp66EySwzpXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تو چنل بتمون هرشب داریم به سایتا تجاوز میکنیم
😄
ما هیچ فروش فرمی نداریم و نخواهیم داشت و کاملا رایگان فعالیت میکنیم که کنار هم به سود برسیم
🤑
🤑
🤑
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 4.54K · <a href="https://t.me/Futball180TV/90026" target="_blank">📅 00:30 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90025">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QrYf4SaQlgTWpu9gwcUgv2_uOJRZY0KpAntdnNNYI3YsUsMEcdMEd3g3CWTchzGkdeUtrTPbIx3c0vMwURN0QsRvydxhOrfOmYlq1wIQnqyE-2x-FiDJw4U3xvswhtQM8y9S5VaqWrhA_y1_uYhzLIfpnDUWDTLPPytFTgHafVvII2BtDkvXJcgTGGpjx5awqU_BItXMQSQrmGy1WGV6pJxMc55b_igHRDEEJRF0631RaEgrKK9Ex1UQcb2VlSj0XKegXoXFtUZFMyHdSktHU2rdl0jz-gLEXXC-p2YwIhNbGF_C-Zd1gnL4hQJ1KzJjaPu8Wsq2xuSN_VU7GmEr-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🫪🫪🫪
🤯
برای فهم‌اینکه لیونل‌مسی چه اعجوبه‌ای هست کافیه بدونید که این بازیکن سال ۲۰۱۲ موفق به زدن ۹۱ گل شد و تیم وحشی هانسی‌فلیک پس از ۳۶ بازی لالیگا این فصل موفق به ثبت ۹۱ گل شده
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.66K · <a href="https://t.me/Futball180TV/90025" target="_blank">📅 19:27 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90024">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1af6bf0b38.mp4?token=sgcAXEbqz0Dux4OcnrCndmIThPshZ4cJRypOLCtjIkdMK297SCp0XqoDqyUpwaWYXpcsSLyJCz67jnx9EOG4oZt9QJYau7JWHAlIKoX9md8hrPGknOcINEGCgBj7PB-bPzsE22Q0iOxq_ElxaD52W8i1aCJgEEjZyY3qhDdwBZ76fGL4tnH2Xzx54Bvl2cs6h_dUbkiWEQoKy2OezbW4RHCTI8GyzMygKERDR__eoFKfM3-2X6qHdH18NR3oHmr1FRTAt4kfhJU9jrpSaNGgnYTYLzax5tfugtaWK9TOFJRfxNCzC3eMWYBX5MpIDIAoLmq6e_FSMpwZOXV1AvWZTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1af6bf0b38.mp4?token=sgcAXEbqz0Dux4OcnrCndmIThPshZ4cJRypOLCtjIkdMK297SCp0XqoDqyUpwaWYXpcsSLyJCz67jnx9EOG4oZt9QJYau7JWHAlIKoX9md8hrPGknOcINEGCgBj7PB-bPzsE22Q0iOxq_ElxaD52W8i1aCJgEEjZyY3qhDdwBZ76fGL4tnH2Xzx54Bvl2cs6h_dUbkiWEQoKy2OezbW4RHCTI8GyzMygKERDR__eoFKfM3-2X6qHdH18NR3oHmr1FRTAt4kfhJU9jrpSaNGgnYTYLzax5tfugtaWK9TOFJRfxNCzC3eMWYBX5MpIDIAoLmq6e_FSMpwZOXV1AvWZTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👋🏻
پایان عصر کاسمیرو در منچستریونایتد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.78K · <a href="https://t.me/Futball180TV/90024" target="_blank">📅 17:35 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90023">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/109fc9f803.mp4?token=GHWF-am99wfArkI1ejlskA4w4vmG0g_FqM-50oP-vAUcYxgBZcpAYyQJDg1rb9cKgWM3_SB1amjF_vJqI4Y-Du8I66a14OlWM6FuaxIOUI1RNnEwcxsM31nujUm5huicyA3ct3ACJmKgUl6YtxIe2uf7pAE9pNUxngmUJsTC1ZKOBVzLWzWN3e4sl2XnEhOyPN63XE8MaSaS2XSq9HH1_T0lRYYPLtZ2tXxRz1K_JyjcJWfkgT-P5fxQ9skdn1Xo5esn07VEMCYZHTyHx8kIXUIdquBalk6h8vwNGSGqfgb9ofMPvbFNbHksFGTr-awy85aQHMrsT2T6X66mjclPzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/109fc9f803.mp4?token=GHWF-am99wfArkI1ejlskA4w4vmG0g_FqM-50oP-vAUcYxgBZcpAYyQJDg1rb9cKgWM3_SB1amjF_vJqI4Y-Du8I66a14OlWM6FuaxIOUI1RNnEwcxsM31nujUm5huicyA3ct3ACJmKgUl6YtxIe2uf7pAE9pNUxngmUJsTC1ZKOBVzLWzWN3e4sl2XnEhOyPN63XE8MaSaS2XSq9HH1_T0lRYYPLtZ2tXxRz1K_JyjcJWfkgT-P5fxQ9skdn1Xo5esn07VEMCYZHTyHx8kIXUIdquBalk6h8vwNGSGqfgb9ofMPvbFNbHksFGTr-awy85aQHMrsT2T6X66mjclPzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">◀️
لحظه شکسته شدن رکورد دوضرب دسته ۱۱۰+ کیلوگرم دنیا توسط علیرضا یوسفی با مهار وزنه ۲۶۱ کیلوگرمی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.72K · <a href="https://t.me/Futball180TV/90023" target="_blank">📅 16:46 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90022">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🚨
جزئیاتی از درخواست‌های آمریکا از
جمهوری اسلامی
عدم پرداخت هرگونه غرامت و خسارت از سوی آمریکا
خروج و تحویل ۴۰۰ کیلوگرم اورانیوم از ایران به آمریکا
فعال ماندن تنها یک مجموعه از تأسیسات هسته‌ای ایران
عدم پرداخت حتی ۲۵ درصد از دارایی‌های بلوکه‌شدهٔ ایران
منوط‌شدن توقف جنگ در همه ساحتها به انجام مذاکره
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.07K · <a href="https://t.me/Futball180TV/90022" target="_blank">📅 12:54 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90021">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uTTvUZbgUL4hAPpMldq03IPjJMqXiojYj1FluWz4ajijr2Z8nV0s5OzBK3vgI4kzwut1pSz_EI8bl5xSG4fw0lYGAcSbWweCtKH-Rx4nXTScIe-o2Luc60PAGKghRnh19uGX6n89_k3drADBjVQzeQBW7nKqqlmz_tX91a6ueZm8Zj9SBRqjR6ERTe5qd30aB8_SUakbqdWe8wDWGkOrOsZrEKI3hXMRm9zrINF2hqBmlqsyAjTnHTe5QrJgLSahQL6RcwKqt2sRCPdFr3OsyVyJM34_rXk_A5GCb3Q9pY4HpT7amu6Igt0ZcoAPeaNbeoufCo0OWYA9YXXlwfXfbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
لیونل‌مسی از سال ۲۰۲۱ کسب ۱۱ جام
👤
کریس‌رونالدو از سال ۲۰۲۱ کسب ۲ جام
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.84K · <a href="https://t.me/Futball180TV/90021" target="_blank">📅 12:52 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90020">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">51.9 MB</div>
</div>
<a href="https://t.me/Futball180TV/90020" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 4.5K · <a href="https://t.me/Futball180TV/90020" target="_blank">📅 12:52 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90019">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ikCgWDD4lK8sbF7Gsmz9mZAq2CrB3jRbKGEJgck-97roWU_gm4VViZjTzhCtqFC_nydwZ0Rl0bYSJkdQEdQHRhx_4ZhOfRQ2yHOlbDPy0CbhPVaayc30j7l0jj0z0hO5iAv2zElVJNZSmQeawX4iDjjatNw_rXIb6mMrTInTT0j4sFhCEfYk9Jk8qNs5teDWQN-7D3zlMe-ituxjuKCwL8s4ON5azE1tUGcWz9pA9Uq28ZETdeIpOOhMNrL9iM0sJ98nlUThjHhU34Pn4hHiYWO5Gx4xyuv634dYSKgabFTbhE3k8nDNVtINlrwkEBaIRL3Ek_fwr5XslVBVZLRh3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازی جذاب
🔵
بارسلونا - رئال بتیس
🔴
🔴
🔵
به Barça 1xFamily ملحق شو و با هر پیش بینی درآمد داشته باش!
🏆
فقط این جوایز رو ببین:
📱
آیفون 17 پرو مکس
🎮
پلی‌استیشن 5 پرو
💵
4,000€ نقد
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
<div class="tg-footer">👁️ 4.68K · <a href="https://t.me/Futball180TV/90019" target="_blank">📅 12:52 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90018">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🚨
ژابی‌آلونسو: ما می‌خواهیم تیمی بسازیم که قادر باشد به طور مداوم در بالاترین سطح رقابت کند و برای کسب عناوین بجنگد. چلسی یکی از بزرگ‌ترین باشگاه‌های فوتبال جهان است و من بسیار مفتخرم که سرمربی این باشگاه بزرگ شوم.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.41K · <a href="https://t.me/Futball180TV/90018" target="_blank">📅 11:50 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90017">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D98T9mUB_TAX3Z1p6HDHOCSbjZ0LcnwHAYyJcNuNnlvOklRoPxgRr6euNexgiUpH5ApWGOJp83QictezUtqkPijXcB_vYLgAmxKxKK6f7kuBiNUudeYTIjD8GG9PiMRqHtEeq3lXm4kHasgp4LuaitQQD3oBaXJorhHAfBYnWfqXIiUeDiHIqFF7g3aKjsscRd-NFNlRA9hp1w3T8necHeJzUOdVtu2018qnFI2fwDCxt9hUH_f15os-G_zMj8g7txKHAlgBMyu4H6YQq_cTTBUUG3Ou4w0WOunS13vo_Xg84YkIosRk80oKYVwlbwyouPdQ5R2jbaWOlQMCjNF-oQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
ژابی‌آلونسو: ما می‌خواهیم تیمی بسازیم که قادر باشد به طور مداوم در بالاترین سطح رقابت کند و برای کسب عناوین بجنگد. چلسی یکی از بزرگ‌ترین باشگاه‌های فوتبال جهان است و من بسیار مفتخرم که سرمربی این باشگاه بزرگ شوم.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.59K · <a href="https://t.me/Futball180TV/90017" target="_blank">📅 11:46 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90016">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pRZ-W-z9BNJo4SXU8LKmCtld20x9UGBR61Swhf6vLTSRtr1JWzYtyvRlWEHQR5KdLeC7ymRZiEIHxFvnF0NdDpvQHFL8c6ukkO1tEvS8XM3o235pyKYULnknQ-c9qk6xtt1FFBn2C1hTfzwSQT8eI3Yqt21Q-50p2vIU0P7RDIeS4_365r7VxkhFppDqk1F6XJ0VPbf9z5NdfROyI7ViQyfqSzS510U2m6PXFacFfrtSycq8Dzmi9w55hvdm3aQHil89pgoK9Icf9Qzu5qu2j82c37v9S6NgjctGot-zQ0yjXwIaveAo6yVt7eu2SrjPlhNfPXfwRY68HkVUPsc9qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🚨
#رسمی
؛ ژابی‌آلونسو با قراردادی چهارساله سرمربی تیم‌فوتبال چلسی شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.45K · <a href="https://t.me/Futball180TV/90016" target="_blank">📅 11:45 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90015">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">❌
⚽️
تیم‌فوتبال البطائح به سرمربیگری فرهاد مجیدی در لیگ‌‌برتر امارات به لیگ‌دسته‌یک سقوط کرد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.19K · <a href="https://t.me/Futball180TV/90015" target="_blank">📅 11:30 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90014">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/553b8556ba.mp4?token=VVIxaqT1HsncqMXPw_r5tJzspAye3JRSmHTp5lz4WI8eQkLqGI6rfkS1Kv3I3zSc_a5RS5Pz-9JxqXG_nxwKtqYi95RUSllJFVxJTpO4mZTPH1iYIAYafuMk1bWigVwc_CITxm2sea8_m04ol7JlS5xmHwSzwYlLTQUGsFHWwolnPg2PJ8_S19Gsz4vD3tudX5xNeuyhljWHsZ0pfBMVAsL19eSxu304AIHyywVNZl-S2bYwZndCarTt76yDGEMZURDaNGW9jNvqe-KpoL_LB9lik_OYNbb-q_ObLeyb5jzHu2ZITr7k0AUcQfWrP94sLG9ii6wokhGzPbdYEMpQTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/553b8556ba.mp4?token=VVIxaqT1HsncqMXPw_r5tJzspAye3JRSmHTp5lz4WI8eQkLqGI6rfkS1Kv3I3zSc_a5RS5Pz-9JxqXG_nxwKtqYi95RUSllJFVxJTpO4mZTPH1iYIAYafuMk1bWigVwc_CITxm2sea8_m04ol7JlS5xmHwSzwYlLTQUGsFHWwolnPg2PJ8_S19Gsz4vD3tudX5xNeuyhljWHsZ0pfBMVAsL19eSxu304AIHyywVNZl-S2bYwZndCarTt76yDGEMZURDaNGW9jNvqe-KpoL_LB9lik_OYNbb-q_ObLeyb5jzHu2ZITr7k0AUcQfWrP94sLG9ii6wokhGzPbdYEMpQTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❗️
علیرضا بیرانوند: سرود جمهوری اسلامی رو با صدای بلند میخونم و مخالفا هم هیچ کاری نمیتونن بکنن.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.53K · <a href="https://t.me/Futball180TV/90014" target="_blank">📅 10:27 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90013">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c75de85542.mp4?token=bb1SscTNuZ1hflp9QyeyJ7Hx9BK3YmefQ-OlEFYhBkRMxJLoi_Js92A45JPMSvg8jPL-6BhmR37B7pmzzj5XxrnvqZo76zcYEA0i5pmHPNSSUKAmIoHJ8VD3O0NEFIGVA0siM-S9BXqLSQX3bMKZPmaXAQ4g7lwnKHlO0YyqbQThLvI-xuNhTvkYIb2Pcka6U0t1-RdaOgzX8ybrEp9enl9e03M9V3ieye9ijLX8YIBG-9iVAxzJyj5mrbGajYDC5l94hM983e5VP0K0BQ43Sn40ITUlHm8w_YKprwfYHctxCeRleVPpHxXof4B3LP9Y70cIr8Won47__dcL4qB2TKEhogIVB51BJ1efKBnsNgeaoRVCwgssLJdThEmE-j-gALSum-hA767C7fIVGarNptTs1nn2ZMjzsdhwJPP-o1YvaYOPaKm0f7JLrFrEuoDbqTyB0--DxAhxRmSGYHACPnmViYaNQlBeH6xq9nNchyOQCm-eXTt2tT0YuIHedrm_GN5N7i23zVDTRjp_II2mQmlth4vIoXIrbUT1UTtB1nk-QI1ra3-YIv82c2JdmQKIihgiNeltZBB0DSb0JO5vqZHWbMwATHWd7a86ZvTE3_PMCYmRGJ5RMng_WKaH4sRSvOjxKBhfV8EtgCCMr90bUwQc5XWhYEvG7Cp5dOY_IIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c75de85542.mp4?token=bb1SscTNuZ1hflp9QyeyJ7Hx9BK3YmefQ-OlEFYhBkRMxJLoi_Js92A45JPMSvg8jPL-6BhmR37B7pmzzj5XxrnvqZo76zcYEA0i5pmHPNSSUKAmIoHJ8VD3O0NEFIGVA0siM-S9BXqLSQX3bMKZPmaXAQ4g7lwnKHlO0YyqbQThLvI-xuNhTvkYIb2Pcka6U0t1-RdaOgzX8ybrEp9enl9e03M9V3ieye9ijLX8YIBG-9iVAxzJyj5mrbGajYDC5l94hM983e5VP0K0BQ43Sn40ITUlHm8w_YKprwfYHctxCeRleVPpHxXof4B3LP9Y70cIr8Won47__dcL4qB2TKEhogIVB51BJ1efKBnsNgeaoRVCwgssLJdThEmE-j-gALSum-hA767C7fIVGarNptTs1nn2ZMjzsdhwJPP-o1YvaYOPaKm0f7JLrFrEuoDbqTyB0--DxAhxRmSGYHACPnmViYaNQlBeH6xq9nNchyOQCm-eXTt2tT0YuIHedrm_GN5N7i23zVDTRjp_II2mQmlth4vIoXIrbUT1UTtB1nk-QI1ra3-YIv82c2JdmQKIihgiNeltZBB0DSb0JO5vqZHWbMwATHWd7a86ZvTE3_PMCYmRGJ5RMng_WKaH4sRSvOjxKBhfV8EtgCCMr90bUwQc5XWhYEvG7Cp5dOY_IIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
عملکرد رونالدو در بازی دیشب النصر
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.73K · <a href="https://t.me/Futball180TV/90013" target="_blank">📅 09:34 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90012">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sP2Xp7JYZgRS_ZDcmceTAtsJ5gocxEWS3xqgeHqxFGYin_RxuMUlfaotInQY0EE7vTmzfYN3tsL5ukYSxk1z9biNXlu8lr4N0sD9zcfKz4bK134N6W2JfglvrwPQLTiRdczEs3UCcnarkWROKsiMId5DeA5_G6xTkmoqDmY-SdoCLOqSqerctaWg7TseQBrjI-5RDKPJiRM45su-1G_LE_j6mILa7cjtRJl3zbT1G8DgQ0hCwPTNErUnJ7oE2H2PpvtrJx9aDbeRtjcjuik8IjDIdyVxFUu0urgLCwVd_RBzzg5noPWnF2z1nSXYAgxONQ4PbkxaJj1QLbqVzT_CDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">واکنش رضا غندی‌پور به عدم دعوتش به اردو تیم ملی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.53K · <a href="https://t.me/Futball180TV/90012" target="_blank">📅 09:12 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90009">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d4fe02d07.mp4?token=EQY3494CjcQBo-l97M5d32XuButPB4t1GZINL7jMLVW8wwWI1NW78eX6XgB5_0L_15FuiBR4InKgjjC2C-p_Qx6zVhslTgNSDsiNUupRYmZbT4UTnVuhaQ0bS4huRAIOIYQTVOFvP522gjH8_0LbFfy_b9-GzsXwi921oX6ZGyXNBUwa0Jnd4G7vKU70pFT7fJjaidNEB80raD8MBaW2LmZl81hvIPvuTtHiepe32Hx__QmXOisOjUNo01AJ70UcN4qM2RWqhfVfy6ADwsNqTBlVaxmBSM4Lbn68vrFvpghc4IF-GQJjZor5MY_2_88RRBctuIMZQXV5EtyrOrRP2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d4fe02d07.mp4?token=EQY3494CjcQBo-l97M5d32XuButPB4t1GZINL7jMLVW8wwWI1NW78eX6XgB5_0L_15FuiBR4InKgjjC2C-p_Qx6zVhslTgNSDsiNUupRYmZbT4UTnVuhaQ0bS4huRAIOIYQTVOFvP522gjH8_0LbFfy_b9-GzsXwi921oX6ZGyXNBUwa0Jnd4G7vKU70pFT7fJjaidNEB80raD8MBaW2LmZl81hvIPvuTtHiepe32Hx__QmXOisOjUNo01AJ70UcN4qM2RWqhfVfy6ADwsNqTBlVaxmBSM4Lbn68vrFvpghc4IF-GQJjZor5MY_2_88RRBctuIMZQXV5EtyrOrRP2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اوضاع اصلا به نفع رونالدو پیش نمیره.
🙁
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.64K · <a href="https://t.me/Futball180TV/90009" target="_blank">📅 00:44 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90008">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GaWM5qhz5rEztHdqK699MQzr0s-A_KFOHteNOpeCGLoC4CKVoY83ymqNIARM5tg6ZlnNMTm6iiyhT0W7SONf6znbT_OmhLqCOn5w3o38p48KLOC5K5Gsd4wGlOXFo9w6vHXODe7gu9ai2BVFXIHjCbDHDIlg9Vw0p7uIm5D8_f6hCQzezok4fSdkE4jo4HF2AYDnsCUzhIGW0xauUJOxnn2lJUtwYuj6XO6xLBjd8gv45SDE0IsKgMDpEUGk1bc43rWH4_hpsynD5jP-AOfO8_2HdEvEASiDUMeItBo2CVe3h6puGyGIObA60dsi77FETyXVmFv6lLwtkJjADTbjag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
توییت‌جدید ترامپ: آرامش قبل از توفان
!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.94K · <a href="https://t.me/Futball180TV/90008" target="_blank">📅 23:40 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90007">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mbxzmO-zajAquu-qRR2knPh5vRaK9MSjywjehLh53PPbzR-91iEccsAAtQxRpT7lxyE5t75NnIN4m-iFJOkvHTQja_pqFXuXGA1q_CWFprH8olXhorMhZs_VQnaLGvNMTFf_f-P88is_FH4WslRf1BDugBYI0xdHkVDVBnVR5fSSn-phIR8hyJce9-aIlsC4Kx6-QF1muB30mMBvhXB1J9G7Q2FG7rrMIfs_3udXjvMJJn-fwYCQqFY_N4Q75dE693m4XjydT1iivflfxaGmygmfUBBlBYky7Z-b9uHYnTCNCzOHvSqJe_0JzS2_4stlDsTWG0s8bT3XXv142lUpNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
🔵
النصر در فینال لیگ‌قهرمانان سطح دو آسیا مقابل گامبا‌اوزاکا شکست خورد و رونالدو بازهم نتونست با این تیم قهرمان بشه
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.85K · <a href="https://t.me/Futball180TV/90007" target="_blank">📅 23:22 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90006">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IfYXESSHrg5_C793-2E32FYyPzE18aMkZQUkZPJxnj99S7_MlXMxDOabgJhW7nD4goSrU8i03k2w7duGUCcVVfKNRARUnLvdOfdiMlLzqWSpB0NT841wc-Re_h1eVTlE9vj2Wie1roo1Y6p_mZ4SEqKPlqJC_Xsmk1Thx412zMGsZzfnHYUNnMfKuhFW5vaZLGIOmlfL6QhWHVdVKizmKKhG9QZJdX6rZtMWaZqZTsVGuuchl2ogOBJspwfOeVi88PPDcVJhIALE-Px1NO1wxqwd1QtFmeK5TmI_LVOw0T6phxgAG1PcWHD19qfMPJiIggecqY7AZU3nxey_WqjdNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
به نقل از منابع انگلیسی، توافق‌اولیه چلسی و ژابی‌آلونسو حاصل شده است. قرارداد این سرمربی دوساله است
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.73K · <a href="https://t.me/Futball180TV/90006" target="_blank">📅 21:05 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90005">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">💥
اسامی ٣٠ بازیکن دعوت‌شده به اردوی نهایی تیم ملی در ترکیه
علیرضا بیرانوند، حسین حسینی، پیام نیازمند، محمد خلیفه
احسان حاج صفی، میلاد محمدی، امید نورافکن، شجاع خلیل زاده، علی نعمتی، حسین کنعانی، دانیال ایری، رامین رضاییان، صالح حردانی
سامان قدوس، روزبه چشمی، امیرمحمد رزاق نیا، سعید عزت‌اللهی، محمد قربانی، علیرضا جهانبخش، آریا یوسفی، محمد محبی، مهدی قائدی، مهدی ترابی
مهدی طارمی، هادی حبیبی‌نژاد، امیرحسین حسین‌زاده، امیرحسین محمودی، دنیس درگاهی، کسری طاهری و علی علیپور
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.58K · <a href="https://t.me/Futball180TV/90005" target="_blank">📅 21:01 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90004">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HO-8kowslL2K4UMj7GslEdXuUS2v0YJ0QDv28vkiGNkEW3dMNP6eEajFF_yBhc2l23Ff6z_GyD1cvfwOkEn0Yjw5sRPG8fk2UuYwPylKuo1Lwn8WtgGo16Vd91RJcYDUZbLXD5ybeLZqUaQTr32ApqKskCElHHKh5GdyQKCFtZlD702potb5sZLOrnDAoQuwTbjvcSAeiansdToGDJeEBt5xsUDJg4yh2Cp_Jy8HiUABQiJmdB9fr9-mnmhQZjVOT5w2BFf6tYTS8KBzyQHgqYOJoVZ-9kfS5H9cA5mFTxHEOhxIuW8m-Pa4Kp5f1SqFbgMRZOi7yHq1ofqktljFFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
به نقل از منابع انگلیسی، توافق‌اولیه چلسی و ژابی‌آلونسو حاصل شده است. قرارداد این سرمربی دوساله است
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.49K · <a href="https://t.me/Futball180TV/90004" target="_blank">📅 20:11 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90003">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C2zgFFFdrzi3cDy2BlF9HeYFVL9yzIz1D1_EcQGileOjhwkjC_P06XGSHDsWHnp1G9BxC0cRgBw6v9ZWBF76g8arZIB5zSYzqZfvIliihdw6uiqjPAXmsTEQvMgVWMEqjFSDHVIl_uM6zXCrrTFUlKMN5B1hTR1Fkqu_2dYoSkFzqugaazaaWnCHhBy2fY7Jsow9kMuP97xQkrl1MuEe75eA-vGwpAxiRu3Ynd5fvnW3RUBNY_Lsj4saCr7KQF0Yg-_1vszh1lnBnlyPKnyWQOsWE6X4SP_eCY3ge9ZKs8I-xySCY1HTHepHxNWsMmJqO5fa8pWSqENFPfqgJcswiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
پپ‌گواردیولا طی ۱۹ سال ۴۱ جام کسب کرده است
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.25K · <a href="https://t.me/Futball180TV/90003" target="_blank">📅 19:56 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90002">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cjashk6UthLnf-Umn3WrQfDTugPM5O0EytnZGYYuDTkyP21BJDcwly_B2DNNpUvu7nhQ5HoWTjRnp5pFZygcm96sCKq5q7XCXCnRoyJiOeR9VvsIAkeVDqURwqGlGoislQ_vp7BC8cK2QMihuZAT-K2tRapDCR7I6AvLysweC4lvMfNwqMkh9esH08ZdDtkyaEaTvaHuvSzJcL6I5ThLkT2HHbTGDr7d9FW6zWB7tbAw9U6Fn3YDrmXCdD4FxMrj-FFWa1MNISjPj__0xG5SurpytgGvAK_dmUXudPpo9NBcIKnVbTD2y93IPNsPBWFjUu2Cr_tOa1-hzZFINx_ffQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
منچسترسیتی با برتری مقابل چلسی قهرمان شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.99K · <a href="https://t.me/Futball180TV/90002" target="_blank">📅 19:53 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89999">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Waqumvmqy4u2SVMFKrU1rWhSKNJclXFALs9HdqhtZ9xSIgTJedkyeCMOhg7kziFfAs_SDH7fSjx-DmrCCbwWDE4C3-J7eXqUWWr1KyBtjquvJMavPgyRkTlIt_25Et9fkWBZ5FHHfC4r-08CopssR5GFy6gnSEVgmRzy89jAUBsJtbDdoEWzORx9_8JTIjS3aSlJterKDSkvbj-vlexB_OGoCUuKxiBinwJceOVVLNBFa1ARJL1-DHfpDs7NYCc5T9gW9L4K-snCCJQIp454Cmu2leupZ6SaxIbnR45vaMMZZJZqHVrsSezXL2UsSeyH9rojGmIJDs1jEzdDVmPphQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فینال جام‌حذفی انگلیس؛ ترکیب سیتی و چلسی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.01K · <a href="https://t.me/Futball180TV/89999" target="_blank">📅 16:34 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89998">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Py2SVrxdDPhT6_eSUHHM4MK7AM7m1UvHWKMUlQBCeLtVjKkWqpoRv8gzd2qeAn7mkeYA445eUsGQJF4hwVs6iNdeHunKBI4WGu9ia-p9ZvpTmG9X3apbPxHHQMeXkMu06dsvlUa-vMYZW2J8r7Rdc2dEjvhQAoqbjdHZ8AJE35oOX3DomO-RmIrRcL6hvCtW7-muo69cHjkFivJVTOEQXBiluWV99oh9bXfLd15XpqZoExUHX3EKNn-SEEvUTiKaLyd4Nw2PCg70pqNMVSrc2AeGDUneqXqC8HJR85V9xlaLoZVX6AmJzolsd6k_qi0010jM1byg3HJieMj7gYzMsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇨🇩
فهرست نهایی تیم‌ملی کنگو برای جام‌جهانی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.03K · <a href="https://t.me/Futball180TV/89998" target="_blank">📅 16:25 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89997">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jWRl88-W88MYuDJaXI6DZ2SQeTYbu4BLb_g5CH1Yni2-i_ptitvOZElrAQYKkaz2wBJBc9GySWXOwKmZ_yiftm6YeKJeIss-pW33NJjHD_XM1-JtVZK9t_tPHEXSeJqiYXvUmk53zrw5kv-Jtq-yBIFi73seBh1BN0wtcJjArI0UU7bp5LsaEDu6vTKiD3qJVrIsSoFzU0lb8o_XQz55j-tqQtqJk-pJwrM7wt5Lt9l8dh65wwQFSo-Ki1zkEy-ZugMlSmq2UBnf9k059g2Skqqymv3Hw0Q_lnLiOpA4UzBpJ-pAl2iIVryG-0AdkJtjEhJJXs4GVTqbmJq4rM33mQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پپ‌گواردیولا: فصل بعد نیز سرمربی سیتی هستم
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.02K · <a href="https://t.me/Futball180TV/89997" target="_blank">📅 15:37 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89996">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e01b819c41.mp4?token=Gix2jZCngEVkSo9-VQAZCR5D234SnP6hzgMBDc04fVTK5SGWS3goIlbhIEaIvsvrqd5EoON43Evd8HA_Ii3PbVfTBbIT31ZD-rbUIRXL6PGKDdS1swswXRdrveOxhDp3H_clqVvJJN4f8QByrpajOaC1yf-fMP32ETD4uf4232tQ8Eae4FAY1Vag00UOFRzbQYS0YLpGOX35ApSddg-oDqdPjEPM_M0eYh6DRj-gS9nqTs15pIJkc2QAQs9bvu-4Eg6xMkvfYccJpWnokr0l7pa9aBxa7sqpgl-TvwMjc9XL5ZHH0gDcZgrNS9onuwFsaFqIL6cmvzQ0eTt9CJpOHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e01b819c41.mp4?token=Gix2jZCngEVkSo9-VQAZCR5D234SnP6hzgMBDc04fVTK5SGWS3goIlbhIEaIvsvrqd5EoON43Evd8HA_Ii3PbVfTBbIT31ZD-rbUIRXL6PGKDdS1swswXRdrveOxhDp3H_clqVvJJN4f8QByrpajOaC1yf-fMP32ETD4uf4232tQ8Eae4FAY1Vag00UOFRzbQYS0YLpGOX35ApSddg-oDqdPjEPM_M0eYh6DRj-gS9nqTs15pIJkc2QAQs9bvu-4Eg6xMkvfYccJpWnokr0l7pa9aBxa7sqpgl-TvwMjc9XL5ZHH0gDcZgrNS9onuwFsaFqIL6cmvzQ0eTt9CJpOHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
📲
پست جدید لواندوفسکی:
بعد از چهار سال چالش‌برانگیز و سخت، وقت رفتنه. من با این احساس اینجا را ترک می‌کنم که ماموریتم کامل شده. چهار فصل و سه عنوان قهرمانی!
هرگز عشقی را که از همان روزهای اول از هواداران دریافت کردم فراموش نخواهم کرد. کاتالونیا خانه من است.
از همه کسانی که در این چهار سال فوق‌العاده ملاقات کردم متشکرم. یک تشکر ویژه از رئیس لاپورتا برای اینکه به من فرصت تجربه باورنکردنی‌ترین فصل دوران حرفه‌ای‌ام را داد.
بارسلونا به جایی که به آن تعلق دارد، برگشته است. ویسکا بارسا. ویسکا کاتالونیا
💙
❤️
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.22K · <a href="https://t.me/Futball180TV/89996" target="_blank">📅 15:32 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89995">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HDYdv3pq7RjBJUa58Sv9Lzmnws2juDEI1SHlI8QNvreJrLa53BktDdJ7V05dUgW8gmvyt8tPXBJJSL0wc9Ex-8ilQl1OykGXjOxQ_q2bVfv0IkugxSs3_SrXQu5X3BUnUCGEE5yipFhe9wXo014TsvMgqxZEombu45oE-HdG5m-Y8IGjBGkBTfHl_TpF2Tpm8L2ADTjsA8lsXxooCYEI5k__8wzqJXtBW0EdrMj6HAFjrc4ChFp3q-wh_wUvUQQyyEAjbTkCRWRURwwGPTBQ2nRF2VbcteMO12DJdjlkeB9xCvX0abjGh-QfrnAOLdZwQxEL5ySKdH6ErRswJWcy7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌐
نت‌بلاکس اعلام کرد خاموشی دیجیتال در ایران وارد دوازدهمین هفته خود شده و اکنون به هفتاد و هشتمین روز رسیده است که در سطح جهانی بی‌سابقه به حساب می‌آید
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.06K · <a href="https://t.me/Futball180TV/89995" target="_blank">📅 13:07 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89992">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZG4qfVoFfa1iQ2jc1KHbeaNNP7EOM0BZAR54fV2akYGr5_QL1Rj7R7A3Y3cjgEJx4sRo1AvY6pBtbDQljS6w0KrNpmj1oFMrZBMaZUiaQm9XUCPj0qcGQ37qApj-NghusWivFQMTzGPqZz5jnztvo-LSQO5bBnZ4HmxGZ26GiZ8PqwRBMkOGjbz0p_PLIHpcIVYaaCPVISgHdk8uEdAEbVZKBCLdEIYYKXfRxpKISP24-xqQvYkq2wvTTVvR3-pybapF6hDToYHJahYqkk_BJC0q85J-img2CRUtnEQ4Pqkufk3JT9PLjwgVZTFrjrR3tP11UgjX2IXrEsFRz-ssDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
⚽️
تا اواسط هفته‌جاری انتقال ژوزه مورینیو به رئال‌مادرید رسمی خواهد شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.88K · <a href="https://t.me/Futball180TV/89992" target="_blank">📅 12:57 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89991">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dcdd85ad92.mp4?token=bzXPXX-XAR_mKaDRvQPnZOrKbRegRW8bGuRX5bhvVKzSddTC8_Wfu4X_KDYeMATGBYQ_mCiuFDkOTGhhgDq1zwpwRH4or_aLPFciX6y_Iwik487j02odNCs1uvMMy5SqoI8wSEV6CWiX_9N-Piin-_ciM6jGXaMZbEAw9oEnYVdrFYuiZq4F5SAtjATTuqs9KN8-xJCLqIpm6EHTCFUCVyQzJuAS6ZZznnUj4Th-zSvsoNxBan5TRt51KURQUEakY8etr8VWVnyB5sWgPKu5sKz86fW8SlhlyvqDJwZuxDStIlzVME31VZNlReyk_qM92wOD6HwQ_mQfbRBX7Ip63A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dcdd85ad92.mp4?token=bzXPXX-XAR_mKaDRvQPnZOrKbRegRW8bGuRX5bhvVKzSddTC8_Wfu4X_KDYeMATGBYQ_mCiuFDkOTGhhgDq1zwpwRH4or_aLPFciX6y_Iwik487j02odNCs1uvMMy5SqoI8wSEV6CWiX_9N-Piin-_ciM6jGXaMZbEAw9oEnYVdrFYuiZq4F5SAtjATTuqs9KN8-xJCLqIpm6EHTCFUCVyQzJuAS6ZZznnUj4Th-zSvsoNxBan5TRt51KURQUEakY8etr8VWVnyB5sWgPKu5sKz86fW8SlhlyvqDJwZuxDStIlzVME31VZNlReyk_qM92wOD6HwQ_mQfbRBX7Ip63A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
آموزش‌مسلح کردن اسلحه و شلیک در آنتن‌زنده!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.65K · <a href="https://t.me/Futball180TV/89991" target="_blank">📅 12:53 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89990">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jPBM0OiwD1nZQeeUoNZLdmfTxVMAWWu0Y5Rx-zncFe5IA6StpuaegZ47-GXX6aEJawWCWKtQJ7aN_QRrTZ3_FrHYg0884Xl3ZGvMIeL2YfPxdn5m_RsnADX0I0IDZdKMp5q3uGcAAucB6yL5hbBVLurIiGWUJdaQQN4pNfwFLW_mm2_X4Bc9qx6SEBa3o6_0i2pAuOfQ08lactU9uypmWJ9N3_sjPs-XarKqPL2ndasebfGKE6xy2MDgCZ3mLkw9NIulRaRsYUlNBTQU1UpvCitlah6-gY5h_B2GxytfViJhpwlnCHVu-JWThKQcv46SRDrtDHZqHZJxhJq8119Rww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
هانسی‌فلیک با ماندن رشفورد موافقت کرد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.9K · <a href="https://t.me/Futball180TV/89990" target="_blank">📅 12:02 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89989">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sZA4a7IUL6NaSCIbzpHOdrvAtm88LNyHlWu1R101qcRy3qMUsJjyVOJUuEDGESZp6EhNyFVjahS7B0d5tgEjA-NOqLjw-Dvkz2WMgsKWhBX_JVgx0NT-goErefcKKEWcjo5aq9F6TcFdt5eGdnhJd6tZxJV0B4TJHlOHsMIg5ocfr3R_SzUt-xm0V7ErUqFu3_aCaI7g6uxf6lDdJNkig5w8lbwkfTao9k0vPSAZdIPlGCXKTHxV1OxeM3IivqcJ4xHiSmX30qcmrwno9wNB2lnqw0vwW0J4dDVqNjrr-7n73OkSACF2rWLtYyPcB9vmql_8M-5LsgH29UOFBxDKcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇰🇷
لیست کره‌جنوبی برای جام‌جهانی ۲۰۲۶
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.93K · <a href="https://t.me/Futball180TV/89989" target="_blank">📅 11:47 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89988">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SuKbicQ5vDYzyS3S6JWM7ct3SbIRau2xhASJ9bCfg80oKOfSDh7v0rWSZdKAjSJRvUplPmgjk-TE5k60-WLm8vyqBjO4FEyZfmLDbewKT5I8EGVp-jyC1eu_0clf-thwcDtp9nQEeI2yzvNim2HxaJcIl6tPkguxQk5ixXzkkZT3_pZk_BN4BOR8Km_UijfvnIPYeVAeMAEIVnDxEttJI3JQmiAeqh6VFQ7dgaNFWriEtsEBqGFvxfVb2BfxHvKigB831hxeQuzcMMb381E1NN43NWTUDD6YDQrSEOaGHMs-asCnXofP-CgL0pvI6at2haQgUmB2CKCfNlRxNp13NQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
وزارت خارجه آمریکا: ونزوئلا 7340 کیلوگرم اورانیوم غنی‌شدهش رو به آمریکا منتقل کرد!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4K · <a href="https://t.me/Futball180TV/89988" target="_blank">📅 10:14 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89987">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">فوت پدرم باعث شد از آلمان برگردم/ کخ سخت‌ترین دوره فوتبالم را رقم زد
مهدی پاشازاده، پیشکسوت باشگاه استقلال: در اوج بودم اما به دلیل مصدومیت‌های پیاپی‌ای که داشتم، وقتی خواستم به استقلال برگردم، آقای کُخ گفت که باید تست بدهی و این برایم خیلی سخت بود.
به ترکیب استقلال برگشتم اما دوباره با دو بار پارگی رباط صلیبی لژیونر شدم.
کخ مربی بادانشی بود اما اطرافیانش خوب چیده نشده بودند.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.65K · <a href="https://t.me/Futball180TV/89987" target="_blank">📅 10:12 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89985">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s5QeCiItdu3cftDKMEeVzL0_EboI0JMq5ual-yaXSFHfUmiu74xCLj6EN2cKxYXJIZ9bAMQ9ZPGnme-4c2YRWGC-BKVbv6puulDGQ4dCql8F3o-F9mZvQifMnneWN28BvLqxCMJah2ltOfd2huAutoNF6KHoYCIYMI8wA_zvj92nsrIz35C6j1Nd3_nkzKLjvgAyMaZQ8SU6dVLZDWqEbOYM7o9kVLa8vSmBVh9pYM8uqz_TA1t5pSCasEdqgPU6A7wtl3on9brQgVxFzfCWXQ4BwRCfEP8wFg4bewDmy9rW8spiBMEw4C5ABEBfwi9pjTbmwoT7OpCH2g8xbm9u9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
ژوزه‌مورینیو اعلام کرده که پس از پایان دوران حضور در رئال از سرمربیگری خداحافظی می‌کند
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.67K · <a href="https://t.me/Futball180TV/89985" target="_blank">📅 09:47 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89984">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">💥
🇹🇷
جشن‌ویژه باشگاه گالاتاسرای برای ایکاردی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.14K · <a href="https://t.me/Futball180TV/89984" target="_blank">📅 09:19 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89983">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TY4fHyRr6Rb67G8V3v5lvWUzGTyKoSdWkVfBkFheOnny8q64T9S2DJz-7PtQ2y0JMdt9W6QRlM25XRrsGzEDLVzIJY9Xj-X9LYPpR_D6yZarxRUP0Zu9t7bJ-ACRh71do8TEOFigxRFacvWJjALZCGG_HcGJ_E2AdTDWZwe4fKLaUtApQsgqDpG2R1O7L07NFEiLaH_383FgYdgxPKlAuyQnJBP9Z8lA2lX-dfovjLNedczZ8_uBC5ebsBC5on6zuOHBcvJyNh2_ycSNOAOtXE3Zrt4ufxw_O9votTfbs-1ofW4mGKm9B3MpIosLomqKj3gQ2onj39sf5dCmZAsl7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
مایکل‌کریک سرمربی فصل‌آینده تیم فوتبال منچستریونایتد خواهد بود
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4K · <a href="https://t.me/Futball180TV/89983" target="_blank">📅 09:03 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89980">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rzFpqgAExztETh7cAMjVYCnqg2OcNaxny8u7NPVElLUN2lKUXYiOb7iu3NhCfo9_M8EQqKV0gcmp_bW7nk0Pg8LQM_bzrh3PWIW6eUccqp5hfQom7y2CtWE-GwAJeROOowQEW2TyugejUo5z-yjUu8hs5ixHFdZ4KUFY4exhaxpCeTKyHDaGGP1llu7zTedrvDvRydOsZHMUC5-UkAuSXpsI-bfL3R8zSul4GQJ2ftp_hOOdsNd4NEc1jI2kW0izNcnEJe06KsfGcrCR4bKbrkZH6yS8n-EZGxnvo250lYuJk881UVkv4NwTmJrMhCP4Ogc44NzT1ZJdMMYfNqjA8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🏴󠁧󠁢󠁥󠁮󠁧󠁿
استون‌ویلا با برتری قاطع مقابل لیورپول سهمیه لیگ‌قهرمانان اروپا را کسب کرد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.18K · <a href="https://t.me/Futball180TV/89980" target="_blank">📅 00:28 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89979">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I_baZozZtemseUF1Wz9pPX2Zel9wFbu4YA7yAMTs1eJrufUz8YB2GOVxVwWU5MYGUeLEh3zAXDFcEjoAtJDazfGXMccoO3IwQggayDRiYVHpEp16SHFj41QeyfpCLZo6VIwrHGIJyIDBRvLyNeGGMprDsAw4srsJrsCjn_1qMYe1LMYSTqiCpvao3eVxCy-x7nKsxbYQlRHs7ELH4QTFq4LV6e8AFY94sOmXN0BUInJJDmRHsi6Aokjx5XjDd9Lx0uukiy7ZDNpC6wSoPJ0HDsEwoE7lsGGl_720Sdy2Moy6nD2jYnZ1gEFTxKibVnYH6aKcsXgZiVnyJkFnk-PI1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
#فوری؛ رسانه‌کوپه‌نزدیک به پرز: ژوزه مورینیو با قراردادی سه‌ساله سرمربی رئال‌مادرید شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.49K · <a href="https://t.me/Futball180TV/89979" target="_blank">📅 00:17 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89978">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🚨
‼️
سازمان برنامه‌بودجه به دولت جمهوری اسلامی اعلام کرده که با وجود تورم شدید اخیر، منابع لازم برای افزایش رقم کالابرگ را ندارد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.44K · <a href="https://t.me/Futball180TV/89978" target="_blank">📅 00:15 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89977">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aPdbb9xOoFTGJTv9VVluAcq0z8daslN1-pwlOPgT-dWQlqyv6BGWibpd_HM-9LMYFou9-2aQnLKMGIUHLpAVS0WRphIyH5WOqXRlHxd8YM9qogn10SAJGs163pxzQz8aohtBQlvnoB-kdqAiZcgdmmtIlf91n3iGbsGklc1_Z7NNTUxWaGd0zFP3jLHVFvDIG7hr2q1ZR7ugRmHnEt-LZVZTst3_pmpkoNDqfscJPFNHcpIwVXJhTZnOjg8hukB64cv4eRrX7SElAtu1n__HLljNXNlZJ4mchwlo32JQgry0NHH1oGB4ZYMCcFNO7Z5VbHT65N_wSwHdl_OhDKZw_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇵🇱
تیم‌ملی لهستان از برگزاری دیدار تدارکاتی با تیم فوتبال جمهوری اسلامی انصراف داد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.63K · <a href="https://t.me/Futball180TV/89977" target="_blank">📅 00:02 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89976">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rG1jIVHa39CkmNBx45dD0D0XWFCVkLHf65sY4RCQa7zggLDkDvc1xrHQlukHf6jZHKchDjO4L_qaZXCUiymzgDlZCTMbOxlxPHFGO2Uy6GIzxNIJy4gUZ-iqwXISn8H479yRHwMKtDOUJmy3OdPlEZDVIWoOrfkhLyt50nVRJuq37DMJWX-9W9dunItUqJXg8bf8InUC2iqkMf-_u-C-S7xYmXmXqEhUobOPj_1DJyorzzj6-FIgCVOL08Z1z1m_2KQKOi-Ir6C78jg5zPc6W0wUZHi2aiDbd5B5TghT7wg1ailUf0Q03qXY_prP60VbnorQGHqmWh3kHeYl4yub-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇭🇹
لیست‌تیم‌ملی هائیتی برای جام‌جهانی با حضور داکنز نازون مهاجم تیم‌فوتبال استقلال
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.56K · <a href="https://t.me/Futball180TV/89976" target="_blank">📅 19:46 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89975">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DYC8ohVdN2V7DlMwrn_NhHW3zFI7Uj8FuQHarAKr0F1AIsr_tIZ_eUvmzCp4_hadQ4C1DyoDxCTzGxhJPgRBMeLsUhDxzIAGjmadJshdOJg-zZYxkmG911zUCnO6tiJZeSnRfozsP94Kr9Z5Qgv_V6tZWoxZCn_-ddMpCRjWQ4BUrNq3U3chqKimZatTTjx6fgjiTsV6WiFO6HMYyx86Q79Why0JjLH6ODkUgixSRVef0md-KlCKVqOi5RAhbTPi_csE-E5QFYn0Kvei-oqdxfvWx7_Y-ZCZ1BRBIOMZ9drBmDgEeRgJ_BRy5ltzT-TFaaO3oSE-wMJQywcnyvzLIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بهترین گلزنان تاریخ جام‌جهانی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.31K · <a href="https://t.me/Futball180TV/89975" target="_blank">📅 19:45 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89972">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/myFvDEve9L0qmt3IvwHcR2Dkai8ZbWHmpj2Al1azgS7dFqlVXJSxWDSdY5oVDOx1ArABsocHxoJd5RCNhSTK7Y8WF7y-OeLOdQlr3R13Ya4Pr81zHInOunhivi08LYq_gZkMynFJaSYhu9Kj7dViHankp4mpqU1X_Mr1ckgKB3AC2kBVS_dUmiS9q9Y-XQQH3IbaEqvc3rfWD7PtHnc2G8SdBTsc4vrDKHok50ctQFU5P0RTVTZAJCVV6XrHxK3ZqJpjP6wYF-ASN5Itmwh_70pFnoofLJKXLwLetWwIBvwCc5aI4z2ZyjcxKhiBLfWh4iAY2vSyRayGdKxuLvLCCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇨🇮
لیست‌تیم‌ملی ساحل‌عاج برای جام‌جهانی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.56K · <a href="https://t.me/Futball180TV/89972" target="_blank">📅 17:01 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89971">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JKy6oZCAP4QfNMaPYmo3doiZMjJeMgojj-b4Qxbwb0aHYffm_j5A2lLgBQE40GBZuS5KzObq1UWVuDSw61leEVzduw4utDNZMICZoOO9jOyY_Uak0TKsW-xqEJmLsz9aKMkumZSb_fVKMhV9KOlmF9lNmL1lZoHRlJLxXG5yD_5GgULVVAVr4F6Cz5JZPfSmbipOfZCfmGDLul_UU5WZAiWMHMUHF5VFbzs-_5QZDY6OJj65NjrXC69Bqu1KAkDc7f7IvOsImY5NcAUYYNwen67zetWG_kaDhHiZwRnvAwCNUDzZmVcL8iexVdZCgXwodcU2k4nMAMedpzPbPsll2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇧🇪
اعلام‌ لیست نهایی بلژیک در جام‌جهانی2026
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.51K · <a href="https://t.me/Futball180TV/89971" target="_blank">📅 16:51 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89970">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🚨
🇺🇸
فوری/ترامپ: من با تعلیق برنامه هسته‌ای ایران به مدت ۲۰ سال مشکلی ندارم اما باید یک تعهد «واقعی» باشد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.74K · <a href="https://t.me/Futball180TV/89970" target="_blank">📅 14:31 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89969">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c8OGfzHPOApn_Rj3WQvhOKHl4y1tYu6NxyyAECtJSLDmwDhmfnWdGJoEuCvrtgxs1NyhZVIYKZbqUX7fZjpEAB4AV8R6jr6zStdQNn8qQszBPpmVTAvH0VW_5NXxrOsOPsGlUIstrYQN2fe3i7NtswVWmxDyDZx7SkW8AUY9U-fDY9qs2eNqP7ComkMArlD3UvcVWuNuZzrW1kRS9o77V0eStnp7TIgpSyCYf6IygXntP-u-D4BTMrrlY8Zk35miDvNMgETDNgp6qw_9oBhd-YecvpGS2Rcuypmc21mSXp1TGAve67HabQglqT7VpKyGhgdgFX_buyeaEoTUPafj2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
نامزدهای بهترین سرمربی فصل پرمیر لیگ
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.95K · <a href="https://t.me/Futball180TV/89969" target="_blank">📅 14:13 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89966">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QhhNRREnPXxjRJYyIp9gLvXaIX09eRyjaQPTON6kqg4eTT-pIhjX2UGCjuMABh5VAGHZ3A_Gal0BWQ1QSeDa4VMX8nANo-zzUkpO344aiuBJeeV_uGQOcw-sPm7WTMP6TiNR2QJBdeTKe9yMZi1cBKDnPhqumeTJ5U8f-aM_oColh6zyxYejIbmQFUh-1s7VyRmzXbH3rZlfOFZiw4clLj9iQ5_p10Xwql0MzEW4N5c0BtsY5nNeuhbBwu8oy8cm5_U__8GcAhn3PYKqYzL51_XDpefvAgE_JRhy-zweR9NZPLCWtXF0PFSGCRJ7_BFF0mNd5H-Kvx0ABuEdTPAUlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇨🇺
کوبا اعلام کرد رئیس سازمان سیا به این کشور سفر کرده است
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/Futball180TV/89966" target="_blank">📅 12:09 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89965">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZTweV1xqNyOZI9RxeUjNvHc9zg02pEmnvmhWNWAZcEUz6FSlOilUkXoZwmvKXyFRw7hFVKq4WeEJ7E4oxsrs9SCN4-F102EiYfo7O9JDm2P8HEVqOMiDOgaoZZA9o86L2JlYqEnbTrSJXgd15hM8K8IVP6WPGzQCmNS65SY62diG5GChLNexPCCZZLjs45wKsqmhk59NBnFcd52oagZOdBb71rwW8h8-8huTlmmBUOWMEzPO1-wNJhZgmKNoVYc0evkdesG2bG4NU19PWifvpO-6h1atIngDNn7nVDdKeyHKViBG1juUxRH13o7q8C-H5ELGHRkz23K-nHPijkUd5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇯🇵
فهرست تیم‌ملی ژاپن برای جام‌جهانی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.85K · <a href="https://t.me/Futball180TV/89965" target="_blank">📅 11:27 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89964">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CwOcayuyly_ZuGtoBgYLfvDYmwJzH3u7BCiTSgJF37TFGQpeP7mTf4X4UT--1hw-O8DqQC4f4-0RWYFmd7ItXB22DLynYwkRKE30IRZqRqZ0KuOzPeMZU1lRDjHxDHoRyye9z5hR7Akrkokm45SKNBkFIO7vUQlgvGRD5cXo0I0oFMn8HdWIecldzXdY-5fKEgQW03NC-b35a0R_8XSHbX0xtwBi7q0Vgir84TamXYxndqzZmcK3zuza3NsbBjBrv1j4TSEKyxd4AgOXjpEi4ZkeRiXbgN3QXoyP79V59v1ciobHeKS2wpwbOL-fv9L0Z1gfbfiDL07IGdIppFfRzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
‼️
امباپه: سوت‌های اعتراضی علیه بازیکن مشهوری مثل‌من عادیه. آربلوآ بهم گفته که مهاجم چهارم تیمم هستی درحالی که همیشه آماده بازی کردن بودم!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.66K · <a href="https://t.me/Futball180TV/89964" target="_blank">📅 09:32 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89963">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🚨
وزارت آموزش‌وپرورش: امتحانات پایه‌های هفتم تا دهم با نظر استانداران با توجه به شرایط هر استان به صورت حضوری یا مجازی برگزار خواهد شد
امتحانات پایه‌یازدهم و دوازدهم تا تیرماه برگزار نخواهد شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.72K · <a href="https://t.me/Futball180TV/89963" target="_blank">📅 09:28 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89962">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kLo0DiMhT_iKTgIse_Au9m8KMFIpjxE_hEct0RT8Y8mgm2EXcapzADmQLCS_hfaZvy4tzNTbQm_K_P5BcP6fGO5yJECPA5icGZvptdl9Lm1AmYH9AxJYBeET4BqaFktNabYssTcnaDk2O6jSyEKCAs5-1DWVlerdlYkOzeaoD0UE7JWQogh6l8pEH8M75d6PvuqWi1cdnXM5tKKa7tzt4Mz_yEuoQRvqlTB2GaHzWAa8E9MSY6BdkRfvCOQcxhvxfRVNbk4Tsb5_82xtd3b7wP6IHksnRFhhcwxPnZGFCLZNjAdBYX8qiLu85fEeUJNSvA5YmNJ5Up2V4qJN3D164w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
بازیکنانی که بیشترین قهرمانی در رقابت‌های لیگ در ۵ لیگ برتر اروپایی را بدست آورده‌اند
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.83K · <a href="https://t.me/Futball180TV/89962" target="_blank">📅 09:12 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89958">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🚨
🇨🇺
دولت‌کوبا با هشدار تمام شدن مخازن سوختی خود اعلام کرد که برق در سراسر این کشور تا مدتی نامشخص قطع خواهد بود و مردم این کشور در آستانه شورش قرار دارند
+کوبا کشوری‌ست که اخیرا ترامپ اعلام کرده بود سقوط سیستم حاکمیت‌ش بزودی رخ خواهد داد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/Futball180TV/89958" target="_blank">📅 23:55 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89957">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6579d2e780.mp4?token=XzLK-why-wDJb8bulZN9DwknnK5gaRVu4jUGLqQalQXdUToWzVNiWCRxNA98dnmUs8qAxqGd4PhemzZpmb6C2DAtQYQ3vf30P-E3EuF_2j5-FSwfa5ywxN2068X71FIjCTfsr5kucA447j_E3oYIGym2-YH5u5wPO9_yhFcjgYmnkRaN2ply8hXrsl3pk0w347zYzqToXw4Zt7Dn_hgIoo4frd80qc5wUtU-JkqpyG9rt3eHqOmomAvQNXT9gEN2JwPaO9QDv1RVWOXkt06VPAvUCMb2ia9kNHrhQ20VwWVZw0dzevvsWw0ZpDLPWeuIltmWW0m369NCJ03cQpcjh0mNmIBnhZr3vc4OIFQkI1xI4joUDpkb5w5FI_-mYMZe1oyfP2-y_DrKAsAbUgHN8yjzRrhnGk0CyyhXdr34zZG171xkBh6iUiXEIXkWwkVBluQMBoWa70qaBIfphzzFgxYeCesiNWt1GfbL_SlIuzVPTL-wfQiiDzLYFKfnheEmEa-BWUIKHGsX5e1QMzqZVay6HcHE9yf7JeVefm4Fy2N2Bv2n2rWP29se72UuhN67231WI7xSX4ENvV_47XlCy-FFg8gSdLShkuBpL1sYv1l3Zpj_xau2ousQTUWNxUfLux9OeEzCH5ta5f3esc79pruwFW4cRFvTkEMhjd6zovM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6579d2e780.mp4?token=XzLK-why-wDJb8bulZN9DwknnK5gaRVu4jUGLqQalQXdUToWzVNiWCRxNA98dnmUs8qAxqGd4PhemzZpmb6C2DAtQYQ3vf30P-E3EuF_2j5-FSwfa5ywxN2068X71FIjCTfsr5kucA447j_E3oYIGym2-YH5u5wPO9_yhFcjgYmnkRaN2ply8hXrsl3pk0w347zYzqToXw4Zt7Dn_hgIoo4frd80qc5wUtU-JkqpyG9rt3eHqOmomAvQNXT9gEN2JwPaO9QDv1RVWOXkt06VPAvUCMb2ia9kNHrhQ20VwWVZw0dzevvsWw0ZpDLPWeuIltmWW0m369NCJ03cQpcjh0mNmIBnhZr3vc4OIFQkI1xI4joUDpkb5w5FI_-mYMZe1oyfP2-y_DrKAsAbUgHN8yjzRrhnGk0CyyhXdr34zZG171xkBh6iUiXEIXkWwkVBluQMBoWa70qaBIfphzzFgxYeCesiNWt1GfbL_SlIuzVPTL-wfQiiDzLYFKfnheEmEa-BWUIKHGsX5e1QMzqZVay6HcHE9yf7JeVefm4Fy2N2Bv2n2rWP29se72UuhN67231WI7xSX4ENvV_47XlCy-FFg8gSdLShkuBpL1sYv1l3Zpj_xau2ousQTUWNxUfLux9OeEzCH5ta5f3esc79pruwFW4cRFvTkEMhjd6zovM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
روایت تلخ یک تولیدکننده در نشست ستاد تسهیل منطقه کاشان
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.04K · <a href="https://t.me/Futball180TV/89957" target="_blank">📅 23:36 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89956">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qkFZ04aycaVLwjFfA30-sRGZNqwVbazxjFPDoXqdE5tlIQJBnnSSjpaLTuRHgqMoRZUaJc2NVZIXWbIj0qSZnJ9mCzfPWJu2nb4RjCKVJgqrJSUo5rJf3vAJLd0nt8BHyD6a-MTcouRq8W_3jgpP4_71a4GdZZF0sQHqw1w9dcX0jH-fiEA6kzYcWFpUcG0UPZ8E3L3M94rNoVuZE5GU_76OZva0XDk2UarLFXzM6ugOwsLW9Kc8ufkcOENxX-rrgJnT7EQ4UchH4uhr9MO4dzjc7N6j71-CUXcdYp6HU0L2dlypu-d2z02ViADNL_zV3JXDP_Eket0Ic_AtiP2yRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇸🇪
فهرست تیم‌ملی سوئد برای جام‌جهانی ۲۰۲۶
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.67K · <a href="https://t.me/Futball180TV/89956" target="_blank">📅 23:13 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89955">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CMATXIOem9BBuAL85fE3aNXA0da21Ip5Yb2R8mNaxre-MGxfEXoskfQ9I32aloIywNBtt_f6weLktisiEfxKXem6VKQd0ar1793p4rbYG6_xxGeELlBfNXZOeX7HMbjh-lZ4F7O1ul6Cwa5qshn1AxcLdwtA3DnfDsw8voGY32ihVvBWx32mzLSzFoRNxtNbkMm9JTBnZ2ysKzvfi71wlf04OHEmIYlqo-VcH1wRc6SdrzXHEVmGaFyufrF0kvSPHHFbMCQc2XnHWt4VdWoPYhX_ybQzTHJ4qOEPulwEELuMUzEgIIUx7PUaHOC4KoEQrGgyujTP3HAD3NmTzJ9lOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
لیست فرانسه برای جام جهانی بدون حضور کاماوینگا
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.77K · <a href="https://t.me/Futball180TV/89955" target="_blank">📅 23:08 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89954">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7cda28878.mp4?token=MSQ1YXK4h5Mcvl-2YKJSzAiQLrceOY4CKr_44zHJ16pDTo5v8vfWlFkOG1exNJOCZxBJZzgEKE7tedrQ6t3ynRikt0gThbkc2IHrWZi2eLjffyf6Z9Uf1b2I192_Llsr1zqYe9yHHKFh7U5rEeB_oETQVJSSkaCY2__XKH1OUdEHVRYd4YsY3Bkk-uXYokYt6L9VbMyJ8c4Im2aCgarBpL25kmrFtynZDHbQDuOhk1vcOZRuZiLLxL-j6HhIn5JNetVAleYqhSWjgEbdDZN-BaY4b12rR_eJ0vJc7Sv5rFVQ9N99T2OG6lPs-ADF8ObZ5Z9wp9uGJOsRGxLkCb0zpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7cda28878.mp4?token=MSQ1YXK4h5Mcvl-2YKJSzAiQLrceOY4CKr_44zHJ16pDTo5v8vfWlFkOG1exNJOCZxBJZzgEKE7tedrQ6t3ynRikt0gThbkc2IHrWZi2eLjffyf6Z9Uf1b2I192_Llsr1zqYe9yHHKFh7U5rEeB_oETQVJSSkaCY2__XKH1OUdEHVRYd4YsY3Bkk-uXYokYt6L9VbMyJ8c4Im2aCgarBpL25kmrFtynZDHbQDuOhk1vcOZRuZiLLxL-j6HhIn5JNetVAleYqhSWjgEbdDZN-BaY4b12rR_eJ0vJc7Sv5rFVQ9N99T2OG6lPs-ADF8ObZ5Z9wp9uGJOsRGxLkCb0zpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
کاتس وزیر دفاع اسرائیل  :
ماموریت ما کامل نشده است.
ما برای احتمال اینکه ممکن است مجبور به اقدام دوباره شویم - شاید حتی به زودی - آماده‌ایم.
اگر اهداف تأمین نشوند، دوباره اقدام خواهیم کرد.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.58K · <a href="https://t.me/Futball180TV/89954" target="_blank">📅 22:43 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89951">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nf9HKpp7T1Xei3MbhuvEz8CJN1SjbYI9KlyFSSar0NueOwNm4ezoozM08l5xbtDyV3nkxgF4L2uiKn9CjNGTWPd-pz9CzwPSZN6tcWd17g1SF0A_gLUI_XCQS4Tw60z_RdddkKfxNbnggwmv_LfQwHU3EZ6wznidIMVJMIA9vP_qbr2MW9nDb7Mb9JwWKnhHXyHVTTTJ_5lzBruC_5B1I79qkSyVlM30aCFJQcQ9lB8UjLM3wjNlaE6CqF5FlVK8E_p1FUfNJ7g9cYyIkhv2nFgfBM7wUsEL4fyyB-VBD-6Uk1NYGj-PA7aOB_ftP30xjk-D7YtnqC9yz6Cnlr-LXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇧🇷
قرارداد آنجلوتی با برزیل تا 2030 تمدید شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.68K · <a href="https://t.me/Futball180TV/89951" target="_blank">📅 20:01 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89950">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lxiDbXuyB7js38TrqAxMVnQqV1eh2px4xF79nee9ySfXDJEzOZveroAfsZGplI0g8po7Gqx26pbkOYLS2a40CWW9gbwyQitlqIfM4eY22QDu0fxdcUuYPS3jEpPPO2KYoYaaUkb19lsiIX2uTKNkiw77N_rlBxNxlI_iGmTarsCt6bRr4iWrS3TVlRyebiNK0bThV5Z97oRdOMp3_3In_At-K1tdahdDXuNHB3vz6qd7CC_Zin7Nh823VkH0rew6fP9kiEIDuw4hRNqKENPMFQxiADGiA82S2xSQo1_mgoYJoNhuDBn07OEU2GfsXnsQlK59MT7YRJ3yK3LP3C2eIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇨🇴
فهرست‌ابتدایی کلمبیا برای جام‌جهانی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.84K · <a href="https://t.me/Futball180TV/89950" target="_blank">📅 19:57 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89949">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🚨
🔵
یاسر‌آسانی در گفتگو با مدیران استقلال اعلام کرده که بلافاصله پس از پایان جنگ به ایران برمی‌گردد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.7K · <a href="https://t.me/Futball180TV/89949" target="_blank">📅 19:14 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89948">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pVzhrnQCetsx1qhhZMcHY0wgJhI9An4MEO6u65cP2Oal_B_vPyjE8I4did2H0oqduWBcRGKHrW8bEJiM2w4YSRbud8lV5Ub7AAMV9ck9ZGansRpLZVtIi2b1vZs6ck-CtZtT-cCrGTIRKZMijCCcP9aRTEdGOuDGGkGGPG6p9NYEsZJQiIeYnjnRy8wKAEHnqcD-953GsqUVyE5T2qPdklpGLQC4su2LEiUd_pn-m47CweSJq3yJAzey1CEcEzT4je6nw7azHY09YlQb2W37zTznIWDVuXaPGHoUTdzCXEzBLuPrCJOxapFUVnf0nwsIQIRl4XF9GicKszdXuFPmpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
ژائو پدرو ستاره تیم فوتبال چلسی هدف‌بعدی نقل‌وانتقالات بارسلونا در صورت عدم جذب آلوارز است
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.91K · <a href="https://t.me/Futball180TV/89948" target="_blank">📅 19:05 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89947">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/173bf1e753.mp4?token=INs65be6pg5VB3Ji1IWxosSoCQ3B7Uq6OY36Tn7JHq1JrFa1GncRG_CQh97Z_RM_coN-UIq_1PzlIv1qtsnCY_26LZVvfTUdX6JQdLhzr8NEVHPjT0JL8xNApJDj6KkyNGmZlsV-8RJl7gk0q6vqT1V9K8SX1-tT7HcOGRc-HjhHG_jrn-weN8g9EowAwlX6m3wX3z3Qc5ok7izfkvKkSt5tPZFUHe4TWL3zV0q4BwCh1Q5yuDEJa-_0i1nVOun8iCIu378UmhPw4II3J8PChrMue9s5jLlpBMEEnT6e4tn2L1s6sV-Yf62Q-0rRnqa1_BwO06Q_RzBOxsXD4TWrnwLygciXHb-AIqBEkQBz1cO5PevnXkywEEkQ-71GS7VDlSLWSvwDR0xMhqYqgOjvJ4fOjEgqCc4hdKgEIzoyzuSjJhWStU-lsJQerGLOj_KNAZ6z6TG4RNeHLrc-Ft7Y9m74KVsxfcnCAktRYJLQXPj2Rl6G5v4fYScMGKesNWDWyvAkJ46ohTOlaITrUf0F8kDfJe_4hGnjQ42iI-mnkuySu_QHLjreVD9uoimrrUyOi53usKvS2qz3wHLItl1Pz8iMfSZL0mQWcNkQjW30HT9frLVOM0bCiiG9faBR6DheKU1pLT0vlfMZZunh3ZGp3ns4kB4c68PbTcRrCmSCiAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/173bf1e753.mp4?token=INs65be6pg5VB3Ji1IWxosSoCQ3B7Uq6OY36Tn7JHq1JrFa1GncRG_CQh97Z_RM_coN-UIq_1PzlIv1qtsnCY_26LZVvfTUdX6JQdLhzr8NEVHPjT0JL8xNApJDj6KkyNGmZlsV-8RJl7gk0q6vqT1V9K8SX1-tT7HcOGRc-HjhHG_jrn-weN8g9EowAwlX6m3wX3z3Qc5ok7izfkvKkSt5tPZFUHe4TWL3zV0q4BwCh1Q5yuDEJa-_0i1nVOun8iCIu378UmhPw4II3J8PChrMue9s5jLlpBMEEnT6e4tn2L1s6sV-Yf62Q-0rRnqa1_BwO06Q_RzBOxsXD4TWrnwLygciXHb-AIqBEkQBz1cO5PevnXkywEEkQ-71GS7VDlSLWSvwDR0xMhqYqgOjvJ4fOjEgqCc4hdKgEIzoyzuSjJhWStU-lsJQerGLOj_KNAZ6z6TG4RNeHLrc-Ft7Y9m74KVsxfcnCAktRYJLQXPj2Rl6G5v4fYScMGKesNWDWyvAkJ46ohTOlaITrUf0F8kDfJe_4hGnjQ42iI-mnkuySu_QHLjreVD9uoimrrUyOi53usKvS2qz3wHLItl1Pz8iMfSZL0mQWcNkQjW30HT9frLVOM0bCiiG9faBR6DheKU1pLT0vlfMZZunh3ZGp3ns4kB4c68PbTcRrCmSCiAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ستاره روی لوگو فقط برای قهرمانی آسیاست؛
تاجرنیا: لیگ برگزار نشود، قهرمانی حق استقلال است
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.83K · <a href="https://t.me/Futball180TV/89947" target="_blank">📅 17:20 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89946">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NH9jefXfrKttUQIo8aHPuidpvDs7bIzLgRrTP24anuxMfj6nihIaXKq52oFCiMhU1lgCjzfgNWV4uiowZO9vb7QqZ7xs6ZvdiEmF6pOfc5cbM94jW0lyZrwaC_G9_8UocrfLH9zkNd175Hb4eBRQpsS9KzXBJd-7cN5hjq5Kp1DRaBc6qcYAwlhXxDbhqtz9jO-YsbKjnpjv_Zwd3QKo43Gs8DIhSwuozx0slLTrL4mpOcdYF5j3fs6zxdaW7Eyq9pmg06-6WpiciTprM0wpbRrhsp5POoKIkrdR-k-7-m0GVyE_7SIE0QbIi8c-YaQk1ySBffgWPzyMLzFcdHuG7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
نامزدهای کسب‌عنوان بهترین بازیکن فصل لیگ‌برتر انگلیس
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.08K · <a href="https://t.me/Futball180TV/89946" target="_blank">📅 13:44 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89943">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e925e8e321.mp4?token=IzCPS69WfLXrKzZ_nmhSzX3iagn44vrEYnZNPvC_11qfE20FANF2H9W4VkJClqFz8iA_aKYR0u7gRk0B1U87BCFmUCVqdwO93_BrBcI-o49pnEd2D1KYMEt0Ar7ydWVACFbTT_xC19KLN0OJ5XuxRvhFtrN3GXpPpawn03_j3-sCyVFD6RQ6mZtXaNKSTDgXgxXAQTBAb-FlMC9xmcd9MpKpf1SPeXV6aH2vz3JSEjG2iMP2X3nGhTAVZAFe9NOjcyNjghWNki2w9t2yuXR6ZQoC7evaKNVZxFkHm20qYt-TNLOBXjhrBb7O9_ucwDWMVeBvuAEWnZ4bHuE8ezg6TA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e925e8e321.mp4?token=IzCPS69WfLXrKzZ_nmhSzX3iagn44vrEYnZNPvC_11qfE20FANF2H9W4VkJClqFz8iA_aKYR0u7gRk0B1U87BCFmUCVqdwO93_BrBcI-o49pnEd2D1KYMEt0Ar7ydWVACFbTT_xC19KLN0OJ5XuxRvhFtrN3GXpPpawn03_j3-sCyVFD6RQ6mZtXaNKSTDgXgxXAQTBAb-FlMC9xmcd9MpKpf1SPeXV6aH2vz3JSEjG2iMP2X3nGhTAVZAFe9NOjcyNjghWNki2w9t2yuXR6ZQoC7evaKNVZxFkHm20qYt-TNLOBXjhrBb7O9_ucwDWMVeBvuAEWnZ4bHuE8ezg6TA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
تاج: AFC چون زمان نداشت با پیشنهاد ایران برای اعلام سهمیه‌ها موافقت نکرد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.45K · <a href="https://t.me/Futball180TV/89943" target="_blank">📅 12:52 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89942">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fKwEeYqxK65Lwvn7ZiOxUpsBhZDjtg8o-fMEN9VkG2p6ALA4qbrlgGJlq-oKuyo_EO8eza7U_oMXbyKZS3D30opxhwUfC2IzKbksZes0QIe7123z7Ioi_zab9A-tueg6yuyrp62X0uUkLBaTCFLtLfy7Nr3cEZfcz6Q95n-duT-j87gueTCfNCLs6Y_QybxotXA5TO303lgpgb2pZTYBarXV5LUkWJWayGLMtUPPva9NyUgZMyeO8t7kpKa4HmIC7fcnCzfyMJVdf-LGHQodJhRpdjyQ5RP1oyuBiXvOluNQXTfUrcm2Ojf6J-tVWBxh_Nbt-AtQPwCDMxZm-ec4ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
ژابی‌آلونسو به چلسی
🔜
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.74K · <a href="https://t.me/Futball180TV/89942" target="_blank">📅 12:13 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89941">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TQ5ICF_tmY0xdZc_v6Jez9vFWugOkCwAcvmpySyhrVwouIiMIjeQ0NCK20A3kttXsgs6aSAp4steQJgme3jc-fZL2gZHAhtxMqAsBp0N31tKFJIoiH0jwUQPEIHFNr7o9F5ovRtP6DQVAnndarNXUs5Bw3-ntCf4AjSwR8NJvhiqmSG582ZWbWJqvXOr71tEAG7r9v0GgWGx2ddCUZjgGQOLr0J92L2unUAFAv0urTD2bXdVr4pHCE28F8pALWqsTClcwBc9BoB6pPP7NWJMhQVm8JN4BBeq9Sj91K74qcf9W-1_9O_8ZrBwUEeDl0PcUgjJ19jzfLAOTRhgOUc2rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
رونمایی از کیت اول فصل‌آینده منچستریونایتد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.36K · <a href="https://t.me/Futball180TV/89941" target="_blank">📅 12:11 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89940">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZWzUj_xhkHo_Sg141dfuEsWPcMaqm8cmD8jDfdwEUNE3uWpS7Nx8uiF4xw6Y2LJPkpngr_A20Gldheun7DqdVBKCcSQyZDQcDKA4pJUcIBKsRl4vI49aWwdUk2toZUlpBtS2LEmY9GSooqOBISUQogPfoyfd-hDMZvcDveeVY9bPhSNts86TFABP1n1FxaziBSNT4NifRcUykVKIVZmbYfoxciGqmQJHEAvFYNdonu4UDzoT1jWRY26deTOlAtUO76auVxqAzDpWTuxqlUAwUKcIXDcLUDMaMKjMMONRE9cpDErA1e_8274T7_ROYB5oFv3GSNGEFRfn0E6b_yRLrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
با اعلام فیفا، در بین نیمه بازی فینال جام‌جهانی، شکیرا، مادونا و گروه BTS اجرا خواهند کرد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.77K · <a href="https://t.me/Futball180TV/89940" target="_blank">📅 11:28 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89939">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TdmHVoyxpubudSiQg0b8tPE8I6zVEWv-kRedFKhQhp911DvfEalopLZACJ713w7I32LnU2EppTWjORqgTzlVNZ-Wa_J1Pf91v8BuBmq8_-kWmBrOmX2boi6OdlrSP5f1I-YDZmGdlIKkYiV0UHePpIBnHHkJNbKV7PqhE0wksO0lapimGbyRO2ymLcR_P1zDg1GZFevoSwF62VBruptPN4FN8U9wdaA79WmkhcKoq4rNv5lHb_heaF0BQa17l9DtEJYkvX5NvrI8USxht7QQlkDxCE6FqmCo1VLzzytNnHqFsnM0A6Y5j9XIyAUQuEB4a3TrCEFa_6Vp71H6hqp-9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
اعلام لیست نهایی بازیکنان تیم ملی نیوزیلند، یکی از رقبای ایران برای جام جهانی 2026
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.9K · <a href="https://t.me/Futball180TV/89939" target="_blank">📅 11:23 · 24 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
