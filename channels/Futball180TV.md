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
<img src="https://cdn5.telesco.pe/file/XWdUxjxwYKIg4RFVkyYlUj3sCnNrEcsn58GmpP-kbe8jqG5snBCmsJHIHLsK9c3i8c4EPYE_a_aJpwzOU-MkdAkYoxCy-jWwa98Gj62waDPXNZwUJ_xhhSlLTgSEQoIRYjfIUEvCaokvMVUZ8w83gFqgpXiBBFZ865sY88d7CA0dL9c_jctT9y0n_bHRWn4j9iruK_ib3gnZxMXYha8BNEbZacwDo1IwcS4fG20gBWo5ZFWSpYHgRzPYifEsV41R6xWKBkHmxAQ1yw8ueMQ01dQjk3N_zTiNq266KgjtFSpoAc33vHeAZeJeDG1tzv9_e7ZBIpB2VOge9spQTdXANw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فوتبال 180</h1>
<p>@Futball180TV • 👥 512K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-08 15:21:00</div>
<hr>

<div class="tg-post" id="msg-102347">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0063915b2d.mp4?token=htdxodQ7Ond_EhzaDNJef6_MXNhT5Ckk-5z7lGtmuL1rSrLnHD2pnIjAw67nXPPpA0bTkQrTPDrhZEaRlmp3PK-T7MBJY59MY3tH1ef9mATYFUGuUxib3byzvFaGB5eWPL8sHAnfaDweC8tvTbz-YHf81ronh8c03iA0u5O3yXzd4M1hAf1DLm5I98d6Ub3ti7g9MoZMn-9QbgI7MFiZcgIloFiXx-gYJDMeMQPGKtMYsU7ya7n5_D5niviKbxUkHqoYNaYBImwM-6IFymXqasfyo00RxWUyUzJIaM_AY5WXL_JTd3eGevYiIL65sXvTy_boucEfobxW1XTXpCYC_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0063915b2d.mp4?token=htdxodQ7Ond_EhzaDNJef6_MXNhT5Ckk-5z7lGtmuL1rSrLnHD2pnIjAw67nXPPpA0bTkQrTPDrhZEaRlmp3PK-T7MBJY59MY3tH1ef9mATYFUGuUxib3byzvFaGB5eWPL8sHAnfaDweC8tvTbz-YHf81ronh8c03iA0u5O3yXzd4M1hAf1DLm5I98d6Ub3ti7g9MoZMn-9QbgI7MFiZcgIloFiXx-gYJDMeMQPGKtMYsU7ya7n5_D5niviKbxUkHqoYNaYBImwM-6IFymXqasfyo00RxWUyUzJIaM_AY5WXL_JTd3eGevYiIL65sXvTy_boucEfobxW1XTXpCYC_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خاطره‌بامزه از زبان فیروز کریمی
😂
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 572 · <a href="https://t.me/Futball180TV/102347" target="_blank">📅 15:20 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102346">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2314f18179.mp4?token=Y0l1LHU_5B-KrqgK-krqoohGFbjINvSw9c1PW7LXoLfZNv_ahe0gdQIhBOrBbldMXxmXngQ_fje7xb1NATKhLe8HgeM4vO2PeknmFI-NShqj2Kz8-s30ftZa8-2QMwFb80raV2bgXmmp1g6gFlSl_kqN5v9otrs6ZJv4D0cBNwZQYKVavrG9cLnGFuNDLusz_o-Cf4jXwAmbOJeQLmnq5X3f9cyYcapvqC93wkZ-VLjrIF6WWedRc9YbiaQFvmed2O8sydZHmm1G2ue1iTCFb2aROwLGBNUbM8N98KY94_J047_08ByGPUu2AtIOdzZJUA2FC7d-J16LcS7OvfQkdw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2314f18179.mp4?token=Y0l1LHU_5B-KrqgK-krqoohGFbjINvSw9c1PW7LXoLfZNv_ahe0gdQIhBOrBbldMXxmXngQ_fje7xb1NATKhLe8HgeM4vO2PeknmFI-NShqj2Kz8-s30ftZa8-2QMwFb80raV2bgXmmp1g6gFlSl_kqN5v9otrs6ZJv4D0cBNwZQYKVavrG9cLnGFuNDLusz_o-Cf4jXwAmbOJeQLmnq5X3f9cyYcapvqC93wkZ-VLjrIF6WWedRc9YbiaQFvmed2O8sydZHmm1G2ue1iTCFb2aROwLGBNUbM8N98KY94_J047_08ByGPUu2AtIOdzZJUA2FC7d-J16LcS7OvfQkdw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
⚠️
تمرینات پیش‌فصل بادیگارد لیونل‌مسی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.77K · <a href="https://t.me/Futball180TV/102346" target="_blank">📅 15:04 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102345">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🇪🇸
🔥
۵ گل زیبا در تاریخ باشگاه بارسلونا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.17K · <a href="https://t.me/Futball180TV/102345" target="_blank">📅 14:40 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102344">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1e80cceff6.mp4?token=VXdTNGR-QbuOIeXwd_XjfpTSNSFtTzBN-ardi1DLLY_TeTa4a4b2kDcEPt15dzm4bb0ARvfMAiye4ygHtFUpnXkARCyunlCcSf0k84uEuXqPY3eZbdbHrC-CI6mGacZ5IJAXLWUCCXlZI73J55P1oyvzSdErry-ProPNou5D9BnKt3E5m0mIw4ycsGR57d70vPnp18hKO4WGeqQXf0cojas1iPmFJWk9jvcHdtGcK-VL2pJyY-tB4dxmnv92VAKeDlmAPvi8ALY0l92ZuU5yYfL02cXq88DddENSQakNvj2vlYZIqPqsCclEjgH_6QDoFiCEHiPjcPk8yartDcFueW8-vG9kPhogkeElvU-wQp0kbmYdiNYthPwYxFp1gq9NhNbQ-OvxRdAOgUMvnvWvDsL2WHOglmi-br-HTixXxvF4NMqEQU5Xbc17fA58mcsv7KKm75oL7DCwt-9CH-SXimip94koWIWlHe95tREPqbYO4IAzMbbEEsYP_GwLNUSAOop_wPv6v_6PFLLuVUPxG5wTIIz6vLwRFKERT32Y-JTTexQiZP5Rm1xmtnXvTT77CHiAI9FdAXGEL38E18uGB4Y5UGOfuYevmUqMBLi0JA_XsFSKfoLsGasHgQU-TGXHPKiZeoYiBHuMnRdrm9X6iAW2yomG7NOSG_KAVI0JNPk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1e80cceff6.mp4?token=VXdTNGR-QbuOIeXwd_XjfpTSNSFtTzBN-ardi1DLLY_TeTa4a4b2kDcEPt15dzm4bb0ARvfMAiye4ygHtFUpnXkARCyunlCcSf0k84uEuXqPY3eZbdbHrC-CI6mGacZ5IJAXLWUCCXlZI73J55P1oyvzSdErry-ProPNou5D9BnKt3E5m0mIw4ycsGR57d70vPnp18hKO4WGeqQXf0cojas1iPmFJWk9jvcHdtGcK-VL2pJyY-tB4dxmnv92VAKeDlmAPvi8ALY0l92ZuU5yYfL02cXq88DddENSQakNvj2vlYZIqPqsCclEjgH_6QDoFiCEHiPjcPk8yartDcFueW8-vG9kPhogkeElvU-wQp0kbmYdiNYthPwYxFp1gq9NhNbQ-OvxRdAOgUMvnvWvDsL2WHOglmi-br-HTixXxvF4NMqEQU5Xbc17fA58mcsv7KKm75oL7DCwt-9CH-SXimip94koWIWlHe95tREPqbYO4IAzMbbEEsYP_GwLNUSAOop_wPv6v_6PFLLuVUPxG5wTIIz6vLwRFKERT32Y-JTTexQiZP5Rm1xmtnXvTT77CHiAI9FdAXGEL38E18uGB4Y5UGOfuYevmUqMBLi0JA_XsFSKfoLsGasHgQU-TGXHPKiZeoYiBHuMnRdrm9X6iAW2yomG7NOSG_KAVI0JNPk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
فرشاد محمدی‌مرام درتست گزارشگری سال ۱۳۹۴
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.32K · <a href="https://t.me/Futball180TV/102344" target="_blank">📅 14:20 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102343">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ufPyxDRehTWkskIZi-vuvgp_uVzAK04wEKPnR2E_L1GsjmXvLly894zm22CLFJkCcIgCjrTaZ-EIF-vaEFi_Y6QWS_QcRFthw7nVc4dYYpaorBIHYDs-7X3jbv7lLpp-o5VPvN98WDcgIlAwnDJHdtDEK6DmzB0LRZxiEjR7QE3MQ9uyxpTWnfYXRz7H5FvzDrhRJbS1FBV3rIebEpGGcQTZL_tuXaQPM0MDprDYV2WW7EM8YEisb8f5gvtnPICc2lTp7tG6O_5mpCk-jLy6eJLPrtIhz9nwTe2plYGlfN5IFLaL8teoPZnyxMBPhhixTSHZ_iERR2UXDNq8TCXDTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
🔹
رسمی؛ نیو راموس مصدوم شد و حدودا یه ماه و نیم از میادین دوره‌.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.64K · <a href="https://t.me/Futball180TV/102343" target="_blank">📅 14:16 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102342">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3336c43202.mp4?token=tedZgQiw5LaANkpOd3dMX2fDv2seWXHOZMq_Uf6-K82M1NeIKXdjXlSxsEmBOCY-V89okzBLgNrHJlKyIs_zz4MRNaBiLMKpP7WEf0jVlmtNeyb1dRSh7CoDeAmRHW-ZNVoWAvMXp-79LXHvNLdO_fptQrvjy2e0lMWevolWFKSqQTdRSI31sHK8hpLb33qfC61U-wEC-gRJ5vrtACJQCD0_aMt-WWZiqPOnThMV4HNDSbCNJaHSfN5oO-tE5HzYtFGioMRb2Yby_6vaf62phGe0TChjH0OzE8Wbg9eig9RfgKsKriSibo94B2h_PKduisdoUPQh95E4knheMZV-uA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3336c43202.mp4?token=tedZgQiw5LaANkpOd3dMX2fDv2seWXHOZMq_Uf6-K82M1NeIKXdjXlSxsEmBOCY-V89okzBLgNrHJlKyIs_zz4MRNaBiLMKpP7WEf0jVlmtNeyb1dRSh7CoDeAmRHW-ZNVoWAvMXp-79LXHvNLdO_fptQrvjy2e0lMWevolWFKSqQTdRSI31sHK8hpLb33qfC61U-wEC-gRJ5vrtACJQCD0_aMt-WWZiqPOnThMV4HNDSbCNJaHSfN5oO-tE5HzYtFGioMRb2Yby_6vaf62phGe0TChjH0OzE8Wbg9eig9RfgKsKriSibo94B2h_PKduisdoUPQh95E4knheMZV-uA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
💥
رتبه بندی سوپر گل های فرناندو تورس ستاره سابق باشگاه لیورپول و تیم ملی اسپانیا، توسط خودش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.34K · <a href="https://t.me/Futball180TV/102342" target="_blank">📅 14:00 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102341">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PyKRIwdr2sShXhBdRDTwUtEig1VQ-vzN73ARztTpI7g7Rv3o_nTiMuSF-RTCmnSKqmi88yev-NQ_VtgSTHL15grsrzvqXCsJNmiGbUGFaVOg2CcnRxlDgM5PMUZ80y7ufSblaYBujeV1dfsyF2kYtKIxUZkACI29TpSZPFHjOjKorWKkrf3l55cKUyfcq5tgJaHSJXVYp5nVe9Zo1Xu3BA9z7iGHFAeA2zsTXDY3x24pIzqz2LnV4U5AyfA-zaMC2maJ36gY05LbCutwtw52Kp9b9-gvilNIV7vbFVCfEEkcGIlUPSeLRzir07RlQmqkdQOec6QnAhO4sD2qzhZVGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#فوووووری از کوپه: رئال‌مادرید و فولام بر سر انتقال گونزالو گارسیا به مبلغ ۷۰ میلیون یورو به توافق نهایی دست‌یافتند تا این بازیکن شاگرد آربلوآ شود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/Futball180TV/102341" target="_blank">📅 13:42 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102336">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/r-qqbeyNqxg_HIIYyvcpzlL0_n1QRp4Iom2arBvqgTgwnNkk8gIsapvq-FOAHrDV0I4rxcqfuVaH34kF-6XNijyhJuZ4MCnkG4KklV0_M_HtkmqNxxTWJOf61ym_Dbn99NH3588PrtZHUmJ0wTk8NY_POzYr4dcGnHAYviSEVn_zXXMP0V4b4GVNa48KJRrhkhVZ0YF0kzjva0bpmWgwQY6ekZebHI7NPema7PrPaoh55QzSfm-nDhbCHgs7CxYq6ILtnB3xLPPTbvVNGsjTObJP1AVjgEBbnQPhDirVqo0nTge5H_njcLO7fzzExgx39LDi6Ux4vchVD17NMYXHAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dppjneVktDDpR2cyxdSJAFFkrzOekl0N-xq4izvS6FF9Ig0RNCIeE_D-CoTNjtIpIkn5PmV95qv3u87ziLuJ9g2JsxGfsbxUk9HDgTOkPsrU1C6YfYpgESShapqz3FM2wLu5BcOOkh6CzkzYSs84d_Ykp4huctvtLGXAaoKj6hfoHYT5h1QRbgL33LQ1L9HAAyw2m5rtbeFvnSSZ2LMktSO2PlOI7N4z91qaJ1FS1oJ_5etCkOtwLshIR7vD9jibiE9qeGsrfiz8oznGu_NFSRpHBAKk-tRePaup498Mc3iUBEOPeNhzOag9jF5niOTm0D19UeqEs4IuD102VGtrSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/N4XcB-5eGsEJrW23Zvi22eQ_cp66mWxIuxPoxRkv9e-3d8DPWfCZRXSUgIkW86dN44ZhF_shxMzlNaU3voyh8o7x32Z_tsOrP1wk9Qem5C-ZgsR9vNVoKy5ZroBrxGLycZra8OyUJhPUTctbx_q3xUJdSsA40BOSfgwEfDhVIXgUqYQQyRKA7key6BihngzTaEn9XfebcG9SlTkvNEXnEVhsb02ObK3x9cOInlAvEoPpLXKcJhGnuMkTVkMKgN6HmgXpnBVNCFmkRQ3rqfAR71pL-Bii6vK4-gytX9yu57bSw-1Sk95mjsHerQwdaQhBFJXYh26rQv1Xx69Ui4SVkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nrtKuxGYc_m7Z4xEmisPLY-dFWsHjhPkSZ5zOJBgkafv3BbHAbD1_GZfTsVroPmGyMxGFHA1-Ok23mAF59vKHRFXm-OJjMFUQnFfBFsfJPkKrA3I2DYSf-TMeNLyyH6YXcYEoMP6Xg1w9ct5ViNQOALRHFFcyFpdxR-xCXHwoIok-clEWXEGLo4oQeQQRJcp-IR8L7jdUJlEOL6TD-zpEPKPBLikfKNbdJrFuH_cWxYTWOHSRsNgmVrlhmdC_MMG1qCqLvuoAUJAhr1y22Xam1SLphqthWN81ikbVvuA4wBxqg8FpAhfUXM0UOopHPer3T5JRdhIo9HhvTfy-QWOAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CjK3baZWCnURaRnm-1HDGWhkptyamps7k-evjrBPQgHduqjmbgHB1Szgd5Nl8msEh-tzfYxCtS2q8EvvXSAbBpYVnoQFFCq_fNFUfIQmOLx0De6_wqO2TtaZNyb6l6GzVwTR5nfhAVnwWJxxYNz7nc9YoSMAa0V4M6S2zb9mTTFoBnhdkHcjJ_GnI8sNosIuTahlGKzhlgOu8iNebFzmyjpd2wm4eH66uYLu7Yi1reUhLEvyBlAXkUf6F6-VFEbK0gGuwXILEN98JzdYOaWFRf1Bz943NIWis4l7dx78WJDUQEykjsA7mqVxU55iHSDvO47lFEpxae8DSGnKW9YC8Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">+ قدرت تورم :
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.78K · <a href="https://t.me/Futball180TV/102336" target="_blank">📅 13:40 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102335">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/efgdUFLb99sJDYMT-ESXqw4MRH6PDfJeZeYhQ90rQuURg-U9F43XQc3edOvVpH5Euwp-27kgWVjQIe3S2YjASIFcHO7ObR1d_hsGMd2vcpCfz5GlRrSSPpCwldT1AofRZeOVCW80MWVMUAj1G9fBshGG5Ltq1LzZrgdWZovjqb1qF8BqYVI0BO5MjJuw1NMPDHBeLjb2RDi6z4culoxJXXmA-uS2_D0TEK2yxveMYV2008y5OtxyxU_VEly0Mw_9dTfM5p-3-KIN3rvd2TFAETMnXppStjuHVPF8m7gHq8zWQIWczgw5LpT-gYz1x5J0J8HBPGR9pjCjkqIi0Mbehw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
💙
#رسمیییییی
؛ روزبه چشمی قراردادش را برای یک فصل دیگر با استقلال تمدید کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/Futball180TV/102335" target="_blank">📅 13:35 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102334">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pYYg47D9f_gWTOscWY922tkYnOoEiuoqY-ld3mJIUFytfsTx53J3FgAanX8rfKsi5JxcKbZWOZ2bbPkhwC6LpaiKFl-A89davgrdzrY_jFZDT2JTBMJ7YvGvVhEWw9FrbkNIlx8_zOsB0VfrIz7ERv6Qq95dgqWvA6KgVjqaG0cyqGSe68AG-F4tey57EmWcz6AtqRkOJJTGsf1WCClenn3pcUSB7aNuwdlSc0oBIK-HJStdoyuOY5dN2WmI2vL5wVZ4PvbEnqKNs2cqc1VkL46ZN83guhd2Igilsd3TMeIgAstN-w-kGauyaDmrdPPaaN5IDslAAbVozbJffzP9gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇹
⭐
فوری از فابریزیو رومانو:
⚽️
ماکسین لاکرو از کریستال پالاس به چلسی پیوست. 𝙃𝙀𝙍𝙀 𝙒𝙀 𝙂𝙊!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/Futball180TV/102334" target="_blank">📅 13:33 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102331">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dW8CLmSKKrU2PzwE1vr7WY7vGT_tscPxVb2xtDGnva_x9sgHPCY7VhARio_EZ7crgvDjTwe4kkX1p2v4R2q3bVpRG0YlcCBg7D9fj1azETpEle-iXscFS9EuA-9lVJX_Emes_l-CBTyiIJfDudS_D1Z8Tjk-tcR26jmEsdirL9BLeFXOJexRmLH-iK9bRqFrMnk3rfz0u9drefLdQngGk2as50oGg6T6mTGDi1C0gdyE-tfFTcrWP9_7JznISp4n11Rpoa2iRA1rUbHrrL4thfug-T_Mbq5kYVyGvQ4MIryN4gLsw7EPtVhcioqSZjldPY3FAUHNrw-XydTFqfUd2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VDccYwmzMB_hdgdtGkUYJmXUY4zvL1p_x6P25bz1wsBgq97zHRMbuRwxJMC3fboVEHyoT4q68UwEK_rgkGRGcxLAlgZM1k2S94Onho5k2HFdB4dLcJaOX8rctxZUj0Kx6zUlBxNZi3-YJ44oOPwKjTEE6_ClmhwathlFwCfD-N-S1TOhdjIZs1UZ6dZLde_iszvo4q2AKwnR2gP5Gpim7qG3h0cJOlRhDdIgvQ_z6fGVffxi64tsRN0v4dLlza1JPB4g8iT60Zv-dYUi5e-ijgHNxoeAlq9FhWF6bg3oPCEy5LzIwQYQ-1aT1IDPWaSUrWO_jjiFhquoJhj26f-0_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uO9wWl8mU180nOAQQDqmJiuwg8shpKpq8dVV2RPW_Z_2E2-DUEzxf0on-FdUKZ4Ba4_pW2Y1W6BHM8jVgPs5pV0fc0lcJaz4It9TQRHCbDP9tdQEYNZCAYjkaWPkoByO-6Dj-kcfxSOsjWhExZ-HI6JwVk4_M_pebP9hFH56RKL4xfzYJRE_gIbN6zD2l3JuzGdomj5O-Uf9VpCBHFRArjNuzaEIw1OtkxdDI2ANKU1CAFagbt4xrP4vZ2WgZ775H6CbQwTGzS2qs0Wc-S0bkJW7i3ashfr6IMysJq-XhBOwWX8JAyE_ScKYq68elv-C7aWbCZbdKqIojYc6HXA2jQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🚨
🚨
🗓
🔹
اعلام برنامه مسابقات سه هفته ابتدایی پریمیر لیگ ایران
⚪️
هفته‌اول لیگ‌برتر
🔵
استقلال - مس‌شهربابک جمعه ۲۳ مرداد
🔴
شمس‌آذر - پرسپولیس شنبه ۲۴ مرداد
⚪️
هفته‌دوم لیگ‌برتر
🔵
استقلال - نساجی سه‌شنبه ۲۷ مرداد
🔴
پرسپولیس - اس‌خوزستان چهارشنبه ۲۸ مرداد
⚪️
هفته‌سوم لیگ‌برتر
🔵
استقلال - سپاهان یکشنبه ۱ شهریور
🔴
پرسپولیس - تراکتور دوشنبه ۲ شهریور
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/Futball180TV/102331" target="_blank">📅 13:33 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102330">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SAEn909jin1xduxJ_8gLY_Z5cP6ez5UZTiIpxBMsp7V69bKmVj1cFmoZfhelBFg2Zx41ScWxGgGIF1TMFStq76MB3a_pBwy_zXX1CM0wJT6ap8nR6h10H4ro5cpwEZuVf5tSx9IOVYLPrOXutJgJDGnaUwPdmylKY3ri9USZWleEk3YGa69ogyaBCsPwKFxr0sthuQvtv4h3orGDFDx6jXpW51HlyIGf5efi0IXm87jkdtAVGtXRLWFh1NttT1ZflHOHXt7h-Iev6TuquZMEdkX_67A0QbsgjCjynJzDXpThzFCn-pNkX9sSd-tqQbwKqJIRmJbfJDFgOvawe-Dqzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#فوووووری
از کوپه: رئال‌مادرید و فولام بر سر انتقال گونزالو گارسیا به مبلغ ۷۰ میلیون یورو به توافق نهایی دست‌یافتند تا این بازیکن شاگرد آربلوآ شود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/Futball180TV/102330" target="_blank">📅 13:16 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102329">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AO9rfLsecNDs1bF2pI9YNg3DjGyWdfodgK4EMJrjZOt1X1AHva2fmVZxfoXonNLxRG5JsgoxpvQ_vZw7twtVr_5LHviAWZiINEh4NlxgJYOM91FtJNnJz0r18Lu0Ho0zI3bZ6q8K5rsXdN1GjfuWfG4nv7lNaI1wwnmFWZYpS-o_kLEwxsWr_PEWXtWjrYZteoElQD5ZwMATGEVaHTs41YpeaQZrs4g1DdL6eAYOYWLYz7mtK2ncdB8v7eS7XZwra27MkoZoKuRAabMOTOr02Om2PLXJpTRgiI05aI7nuOSBLjWWxwZMW6rwXd4uZeaS97xxuHTOcFE_3TKGAaUFrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
‼️
✅
توییت مجتبی پوربخش مجری سابق صداوسیما علیه عادل فردوسی‌پور.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/Futball180TV/102329" target="_blank">📅 13:14 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102328">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee8b739e27.mp4?token=FcdU_PPMQEug4FGYwnUu61LGtKG-0n86drr9wnmeHKBFeeQQPJ5vGpDqzK_gPz0SCL9lik8J7BDnb4u0Tfpe1HDGbalaAB-V6Lj9F_aEr16hcNzmr8HbOqKJFpKm7IcO7GA6PknOqPNBWmqnKgIy42-hz78uOgLOm4s52-zGQe4cjWaRe4WQ_vgY3L6VH0dbbSaflTqvEg4veUbvBQvaZZKlQAB8olpvXL0ey6e89fpkn7uF8bXHw9wNktmW62xzIkjeJaxvxXmfJbf3wRFN0Qbp2XVag3GZJ3JSXQZ_VD4U2Ox49lGU9lP0C7Rzl3Q3Tk3CryJ21BzGvOG0qPgjVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee8b739e27.mp4?token=FcdU_PPMQEug4FGYwnUu61LGtKG-0n86drr9wnmeHKBFeeQQPJ5vGpDqzK_gPz0SCL9lik8J7BDnb4u0Tfpe1HDGbalaAB-V6Lj9F_aEr16hcNzmr8HbOqKJFpKm7IcO7GA6PknOqPNBWmqnKgIy42-hz78uOgLOm4s52-zGQe4cjWaRe4WQ_vgY3L6VH0dbbSaflTqvEg4veUbvBQvaZZKlQAB8olpvXL0ey6e89fpkn7uF8bXHw9wNktmW62xzIkjeJaxvxXmfJbf3wRFN0Qbp2XVag3GZJ3JSXQZ_VD4U2Ox49lGU9lP0C7Rzl3Q3Tk3CryJ21BzGvOG0qPgjVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
روزی که مسی به برونو فرناندز درس فوتبال داد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/Futball180TV/102328" target="_blank">📅 13:01 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102327">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qRZodgNJULNP-7Qdfjgzz9-2eiZqO4p6x3H8KIu1xiwOjjBXMobLeqhSh23E6t7sF8zudf4zm1vYgd--raDTA5M4Rhozdn1OatCwIQdkE04KPMDmoUwvttsYHZOU3wNzFQeGpUE3ceK1PzVXv-mCaVpHgsIj1PkkLzFiq8sfqU4uHYIkeent6_S2z8ELLoMF02uNBRPnu7Sq9n7N2oUbnnkxUOjNl3y5fhBuTjKugAt8uV-_SFpMkABvCOrXYXr9SbqnZu4SphXO_TLtIlHlS3hOs8EtfSXVwrFwiYsSfoZ5SM9s6wExgOlF6JNPryJAXn1-s3qxB_ZPHdizcyBHYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✅
🟢
صندوق سرمایه‌گذاری عربستان سعودی ضمن تقدیر از یاسیله پس از کسب دو عنوان قهرمانی متوالی در آسیا برای الاهلی، با جدایی این سرمربی به مقصد نیوکاسل موافقت کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/Futball180TV/102327" target="_blank">📅 12:48 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102326">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa8a1ce74f.mp4?token=G-73f51DmccXCW77AUTfXo8pQDDNZuz3xJ32oRpcvlb_Kdy3H76241yApZLINwe08GC7r9oUES6wsLOGIXEBtRqwB7A0vPS5HWB2kiMigEvzdJaRWkuT79p8mSdaP51uoCG2M33gzW1ZYZSmnetZ1BAv6Clkd9YuXoPfhh6PrhM0A1-GZfa0APVlokt9uwMIi92OINVr-31YyramgQxdIC2bqox346Wy-sWAbvIRDE5JI20_avYcEz0ceo68j2T_X4oqq7NmzdYnpYttCI5AVgF2k2HmE4qrL96dhxKPHtJNS4eqM3Ffphp2cUnqRCr5G-vc3L5OLG4ezAPykxoVWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa8a1ce74f.mp4?token=G-73f51DmccXCW77AUTfXo8pQDDNZuz3xJ32oRpcvlb_Kdy3H76241yApZLINwe08GC7r9oUES6wsLOGIXEBtRqwB7A0vPS5HWB2kiMigEvzdJaRWkuT79p8mSdaP51uoCG2M33gzW1ZYZSmnetZ1BAv6Clkd9YuXoPfhh6PrhM0A1-GZfa0APVlokt9uwMIi92OINVr-31YyramgQxdIC2bqox346Wy-sWAbvIRDE5JI20_avYcEz0ceo68j2T_X4oqq7NmzdYnpYttCI5AVgF2k2HmE4qrL96dhxKPHtJNS4eqM3Ffphp2cUnqRCr5G-vc3L5OLG4ezAPykxoVWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🙂
یه فلش بک بزنیم به زمانیکه داور زن بازی رو متوقف کرد تا به کاکا کارت زرد بده و باهاش سلفی بگیره.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/Futball180TV/102326" target="_blank">📅 12:40 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102325">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/49420aa7fc.mp4?token=D5c7yeXENS-SGTrkdmU5oabRcoCKUtjRvyjixnbBW1KIBy9Edex01q1gSyBNiwvafL68H1Nmov95JjnR1DzhVU3VLdxuebJ-bZ8Gj46JA_3DJOlAr4IhGTjtR_JF-twyQ2GH3Owv3M24AtH-CkzuYrQ3RodHRehwXSyv6BYuiiesfs8msiRZUeXWtLwD6FA5rGSXLbxOyYgOI4F3FQtP9woxLkaxxG-JgZ5hgakZxUJru9s75YHuQngjMs9GkETN9FrhDygOsBvgN2qGUShoQX72d1AkslYHhVGciU9Y0-ShLSdeticG-q3kIc8_LkvECRDhlgWCHHD-7CGZaNvmxIHVziSre9dX6Jqy-rTMVbYndZeCCu45ITtj6lTgAbmM-tAqwJpGquEZfYtYDgIBnQPtCZfvlCyLipEYvFIeEXZARuJAi7FpNdA1rtPzzf6uAWr1RK-ca60INU5n4ATbeI6OcOxQlWg2Ya-HvKKRoZ2fXOKMpGDw-ccwVPoH7VT0jrBtrGrL489-r2o0mQ4IouS8YYbT2ih4srJbKMokvZI2fxQykrs63-1ULiT5IR2PPkb-QXA5m__BZNpRDliyrD5_dkEQ5OL3hLtFqBsKVyJtScayPGLYX7ra5t0QLB2gl8HfXUAX_cePFEEATLEGkJn2mzCSiE5cOwm8XuvRrfk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/49420aa7fc.mp4?token=D5c7yeXENS-SGTrkdmU5oabRcoCKUtjRvyjixnbBW1KIBy9Edex01q1gSyBNiwvafL68H1Nmov95JjnR1DzhVU3VLdxuebJ-bZ8Gj46JA_3DJOlAr4IhGTjtR_JF-twyQ2GH3Owv3M24AtH-CkzuYrQ3RodHRehwXSyv6BYuiiesfs8msiRZUeXWtLwD6FA5rGSXLbxOyYgOI4F3FQtP9woxLkaxxG-JgZ5hgakZxUJru9s75YHuQngjMs9GkETN9FrhDygOsBvgN2qGUShoQX72d1AkslYHhVGciU9Y0-ShLSdeticG-q3kIc8_LkvECRDhlgWCHHD-7CGZaNvmxIHVziSre9dX6Jqy-rTMVbYndZeCCu45ITtj6lTgAbmM-tAqwJpGquEZfYtYDgIBnQPtCZfvlCyLipEYvFIeEXZARuJAi7FpNdA1rtPzzf6uAWr1RK-ca60INU5n4ATbeI6OcOxQlWg2Ya-HvKKRoZ2fXOKMpGDw-ccwVPoH7VT0jrBtrGrL489-r2o0mQ4IouS8YYbT2ih4srJbKMokvZI2fxQykrs63-1ULiT5IR2PPkb-QXA5m__BZNpRDliyrD5_dkEQ5OL3hLtFqBsKVyJtScayPGLYX7ra5t0QLB2gl8HfXUAX_cePFEEATLEGkJn2mzCSiE5cOwm8XuvRrfk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در هرجای دنیا همواره فوتبال آبستن حوادث است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/Futball180TV/102325" target="_blank">📅 12:20 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102324">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xp52jHaL-tItnLiudaspfSI0RLn81FyHidO6YRvxewx9GYdzQpnWrlNck3vRg6PDcFibzL3QXoAtf6IArTY1b4D_TiLCSa5e3BpCVamdowlSWuJlLCQBgQEliaXFyXHeRL4jpT6xxawAV7LUWLEBj5TxDckWWgM-pjQhhoW69GfeP4TL6vCiWFmf7kAIV53QonSLA1XTDaZqAH6-FPotOscL-DyzoYrv0_4m4SfXSEbLJm5_tYAnWsnQskShaJegn1WIgjpC4jeVsAQdjRWSKY1qvCvvPxQ_rlYqOjrbqu_-Mbmwxuqtxvz6_fYZzOcbbsSwY4JbyeP37HC37bKfkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🗞
🏴󠁧󠁢󠁥󠁮󠁧󠁿
ماتیاس‌یاسیله سرمربی الاهلی عربستان در آستانه هدایت نیوکاسل قرار دارد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/Futball180TV/102324" target="_blank">📅 12:08 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102323">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9305c345ee.mp4?token=LEJhivmdzV6DJtOikt2ClMb2vxYJ3qRN8-gsmeWC2dYOfn6c9C6-g98LdUWzA0hNDWSB8GaHH8ZnsrizCoD32esVIs406EpDGbY_GRrHBW6SgunaTIhRdCV7N4FYCOCvu9yUf9S155Q3EPOKvpVpmw2kczs4V7pU5KRThn7ypZZ5I-Gpxs2eNV5kJDSLS9e6emSowDGtklZ6VB2oqr-uTNNA5cQcAN_A1RJQFXcuD6AWLKhQLgMMQ1EkECYvNhdJWWYlqOMxveEMMv-TmpNl4QJyWsVLyZzqQHfqxF61xvbUXMQggSyKGrcaym7chfCAsbafkYfPkj4KydSGlA_LaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9305c345ee.mp4?token=LEJhivmdzV6DJtOikt2ClMb2vxYJ3qRN8-gsmeWC2dYOfn6c9C6-g98LdUWzA0hNDWSB8GaHH8ZnsrizCoD32esVIs406EpDGbY_GRrHBW6SgunaTIhRdCV7N4FYCOCvu9yUf9S155Q3EPOKvpVpmw2kczs4V7pU5KRThn7ypZZ5I-Gpxs2eNV5kJDSLS9e6emSowDGtklZ6VB2oqr-uTNNA5cQcAN_A1RJQFXcuD6AWLKhQLgMMQ1EkECYvNhdJWWYlqOMxveEMMv-TmpNl4QJyWsVLyZzqQHfqxF61xvbUXMQggSyKGrcaym7chfCAsbafkYfPkj4KydSGlA_LaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
🇧🇷
فالکائو برزیلی بهترین فوتسالیست تاریخ
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/Futball180TV/102323" target="_blank">📅 12:03 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102322">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc1c528fcb.mp4?token=eudO8BNZiT8wHCmGAOOoBNC2-AjVjBZtkHAHlPLgGuovWVjd51nQXRrDUFFPciX-sY1uUiQ3mIbNRzWaSES7RkTfn6ROGYEpyvDwstN4xFXVJGjY45WtHTzjOEhqz_Nl3G0v8SsT7t3bdkjVPNjG0DM-HIrEWhpHFpGHG-7rLXKSEq2plMHLufddzqYEhzmvmU6qWolvCYhH3lrAhgWwPnTaRudLxl5NPhqb87yLlDKEaUUuErmbkOmlgUfPMj9FfJkx8vxQzrDmHjTfApaSbduvfp0EN3usnFAHSTHPIhdqcJecUJ2nmTiLTFIgqzUKMaVhsc-kSqNH068rhb03Kw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc1c528fcb.mp4?token=eudO8BNZiT8wHCmGAOOoBNC2-AjVjBZtkHAHlPLgGuovWVjd51nQXRrDUFFPciX-sY1uUiQ3mIbNRzWaSES7RkTfn6ROGYEpyvDwstN4xFXVJGjY45WtHTzjOEhqz_Nl3G0v8SsT7t3bdkjVPNjG0DM-HIrEWhpHFpGHG-7rLXKSEq2plMHLufddzqYEhzmvmU6qWolvCYhH3lrAhgWwPnTaRudLxl5NPhqb87yLlDKEaUUuErmbkOmlgUfPMj9FfJkx8vxQzrDmHjTfApaSbduvfp0EN3usnFAHSTHPIhdqcJecUJ2nmTiLTFIgqzUKMaVhsc-kSqNH068rhb03Kw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❗️
❌
الکساندر پاتو؛ ستاره‌ای که قدر خودشو ندونست و خیلی زود از فوتبال محو شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/Futball180TV/102322" target="_blank">📅 11:40 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102321">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UfUZUV4WD3eypy4er16uF9FukTFMnxT0fODnLF-gcLsxkbegS4ndj0DmzBMHd8jjVGyoGjOqR38gCUDxYtdxUj3Y6PgbwUa811PQIDiOepzuvM-fGRB-4GDv-veDhL-lXU0RsDV1itlRMmXcDOARbRDv0pFFM4g9R3ZPOm0EABs86pEtMesF4MvXxBeHEQFJ_biOW-IIoHTEXB03JwrLNZP64jQXaY2gNjc1N8xt5P07nzIlQ8UEFNY_KVm_AET22ZwxkaojBMX1ag-aLbvYGMYXqOYxF_wCViVWF6npu6oHl0BPSG7IP8um-opdtzX7uc2oQtRJbltx3pRLZ_RVXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
⚽️
رونمایی از کیت اصلی النصر برای فصل بعد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/Futball180TV/102321" target="_blank">📅 11:37 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102320">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">✔️
🔹
بازیکنان خارجی ، 4 مدعی لیگ برتر
:
🔵
استقلال:
🔵
آشورماتوف، ماشاریپوف، آسانی
🔴
تراکتور:
🟠
خامروبکوف، هلیلوویچ، ایگور پوستونسکی، اشترکالی
🟡
سپاهان:
🟡
ریکاردو آلوز
🔴
پرسپولیس:
🔴
دنیل گرا، اوستون اورونوف، مارکو باکیچ، ایگور سرگیف، تیوی بیفوما
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/Futball180TV/102320" target="_blank">📅 11:26 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102319">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UQcDfqLVoH_HwKLZtXFo_8PbAGmFE2TghnHCnJfUCSQdCKzfftaMSGi1CXQmBdUtWtYaZ9UDwnV0-zb0ehrKf7u2c6Jz1GzGP_kaSk9icpBou25fWpXwrV5xv3UudA0ZhlJBOD2Xp6FnoXs6aVaR6qsvUnstp7e7A4zpFtJeSHlDgmXn8r9EPxox0tTMDiAtGZMpJAWfanQL7uU5bkhpgIHfXB2NdedbvOdxQxRb57UEIuA737mpeSaduCZ1VaiGpngWUPIhK4-CbsuIhu1CWSE96rnMlp8MEoqgyo3xScchyucFePRcO86M_KnVYBhB5ajkxp8ql_KCjud9gzwEjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🗞
🏴󠁧󠁢󠁥󠁮󠁧󠁿
ماتیاس‌یاسیله سرمربی الاهلی عربستان در آستانه هدایت نیوکاسل قرار دارد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/Futball180TV/102319" target="_blank">📅 11:21 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102318">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b07d2f0b1a.mp4?token=qSXQSJO89G-05cziXmYc1uEtzoM1t-Y-GFjuJk7SWm4u3SJLhjVIng5f2Aw5zBPYE-yDb78GtfwH3kDcokeJGMQk5OxwnTvrlN3dZoYNdzwxgHUShWx2wZLaUxyr32bboWOZXqVuVButyMH0l2R_iTxfmloAh7adlsGM5aLyNnxZnzmfHxvRN-E8AIH3Vg6T054xvoFy8D2ZNMA1EE-B9E4A--NM6yBSJg_CtJzWEWBxVUlTYj35h03CiVUgY5pgt3qEMKzuDul-U4V6S_17KE07aZvkQgX1mJxTSqmaU8buIHtQFTDOvCwLPHuocaSJ_Fn_DsSGtJMO56IfKbpViQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b07d2f0b1a.mp4?token=qSXQSJO89G-05cziXmYc1uEtzoM1t-Y-GFjuJk7SWm4u3SJLhjVIng5f2Aw5zBPYE-yDb78GtfwH3kDcokeJGMQk5OxwnTvrlN3dZoYNdzwxgHUShWx2wZLaUxyr32bboWOZXqVuVButyMH0l2R_iTxfmloAh7adlsGM5aLyNnxZnzmfHxvRN-E8AIH3Vg6T054xvoFy8D2ZNMA1EE-B9E4A--NM6yBSJg_CtJzWEWBxVUlTYj35h03CiVUgY5pgt3qEMKzuDul-U4V6S_17KE07aZvkQgX1mJxTSqmaU8buIHtQFTDOvCwLPHuocaSJ_Fn_DsSGtJMO56IfKbpViQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
با اعلام خبرگزاری رکنا، نوید زیادخان قره‌داغی همون حیوون کثیفی که دخترارو تو خونش کتک می‌زد و لایو می‌ذاشت، بازداشت شده
⚠️
‌‌ ‌ ‌
یه ویدیوی وحشتناک ۱۰ دقیقه‌ای از
این حرومزاده منتشر شده
🔗
🔞
مشاهده ویدیوی کامل
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/Futball180TV/102318" target="_blank">📅 11:16 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102317">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🚨
‼️
🗞
🇪🇸
رومانو: رئال‌مادرید و لایپزیگ بر سر انتقال دیومانده به توافق نهایی رسیدن اما دلیل اعلام نشدن خبر اینه که لایپزیگ ابتدا باید بازیکن جایگزین جذب کنه و سپس خبر رسمی اعلام میشه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/102317" target="_blank">📅 11:08 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102316">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a432ebcf02.mp4?token=gLFiVhlKzG7FJ0YQi4dqbYp8j0FXmmDpndzcSL5oQDoKa8N4UXSVD-mIVRZAC7_FGHYdl3P5WVw18461NJzqPhz84Sj5ojL6CgpECmFZ4OF7yDEueum7hj8XQ1_OkZ_A_IrFl-6raPUKIdYkmrRasKQWs2ZZHwmxiQOL3al9W4I-xAeEQO5iCCEP2pyLlQDpkU5LC_1cnidbjX1v_oF4ZzewIKRg69WJoK8_xR9KwdS40gIa3j2D1vSOqSDeWFUx8Ko9RpxKRK7A9-4yR7IuOmFLpqRB2K5AwhLBTD733sZcbiCT8u8uXQ4ZFo2LJxNz5T6aonaa8ggamxlsqfbXIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a432ebcf02.mp4?token=gLFiVhlKzG7FJ0YQi4dqbYp8j0FXmmDpndzcSL5oQDoKa8N4UXSVD-mIVRZAC7_FGHYdl3P5WVw18461NJzqPhz84Sj5ojL6CgpECmFZ4OF7yDEueum7hj8XQ1_OkZ_A_IrFl-6raPUKIdYkmrRasKQWs2ZZHwmxiQOL3al9W4I-xAeEQO5iCCEP2pyLlQDpkU5LC_1cnidbjX1v_oF4ZzewIKRg69WJoK8_xR9KwdS40gIa3j2D1vSOqSDeWFUx8Ko9RpxKRK7A9-4yR7IuOmFLpqRB2K5AwhLBTD733sZcbiCT8u8uXQ4ZFo2LJxNz5T6aonaa8ggamxlsqfbXIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
از دعا کردن تا بزرگ کردن لامین؛ چند کلمه درباره یامال از زبون مادربزرگش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/102316" target="_blank">📅 11:04 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102315">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LEJWuDtemdI1MmV-arsWxdozGKeT7mLFcGUzvGA_Cfi04wvRd6NB2H2-r5jwcgrVttMFdSzICR2Crxfv6A2ileQ8NU-1lLZsbIRerUV4kDJB7m_UB0JtNrdqTWVCnaqCIF9MCwTDqPM0tFRwnmsIvmlnxGGHR5DIMyx7X0hzVJrZJY6TbjMtHpOUgeN5HWfthkR_YlpcGRWNKr5miSU919CP2NMmU42BaqXO0MgVLbEqovfcYQ92GqvZ1B8aM0DUV_sHbfI1AJ51JX9Am1k9i7BExl4Z3jBK9q2ifEqfmo3pj5ujCDoJYxeS-8TT_7Fqr_nhY7rB7mzCjalCP6ar_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇸🇦
🔵
با اعلام رسمی AFC، مراحل حذفی سه فصل‌آینده لیگ‌نخبگان آسیا به صورت متمرکز در کشور عربستان‌سعودی برگزار میشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/102315" target="_blank">📅 10:42 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102313">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IB8VFnNrszajPacXstSh9A8UjUVhBQMMvodOfpFvsY9cBOhLDWn5ASKGkqIImmd-sixWcYzcaKoZANgKW7EXhMmU8OcsnXRwH8qn_HLZp-f_dk4WtFNGpCZiO6IPqd1ENcvUbKbqGIAmg_GoVeUwmJTxitZY1h_NGHfq4fXLo4P9jVffm6mb1xM_3B1olF6xP18KVs_zH2SAGkDdh7e1n4Xh0H7N7w-3mT3GYLhnuZacoGmgTxRliKeV5srPgHM-3iR7gHAlzNzfaEjTXsQKFUUv5U0lauayWiJgiJFrTbE8j1s70RtW7FrR9yjuXdEFgClSeBTtgHNgsVkvuPd6ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✔️
🏴󠁧󠁢󠁥󠁮󠁧󠁿
ایوب‌بوعدی ستاره جوان و مراکشی باشگاه لیل در آستانه عقد قرارداد با منچسترسیتی قرار داره و بزودی جانشین رودری میشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/102313" target="_blank">📅 10:39 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102312">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fac4341594.mp4?token=qBVBxdS3BWZ-5yNFsrCw7AB9GA2hyRnzsknf20OwLusZpmtI2ReEjM2kFmzrA7IVykJSguJmtg4c0ygMbQVMf1rzO3ULNBwdxf-JAqoSczuBdQNH5s-bZZZO9iipZnIuPslANDiDx1HUE3xdWOIF2R01-yVKpoNVuGOLMkAPVuWmKBxNHJd3NXtIFAlG5bt1RL81P6qd9ouMQTYvwgFbKQCN0JgE5oHtDWFthV07MeuoWgOGb1qhyLyH9Y_gkNefYU5sVi9lo42gK9uw3q4URZJVnCD1IlUMooUmCinn4n5o1ZhpNQa0tVWe0oyHo9KIjlugkYNG8IjWbv6cJKSQVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fac4341594.mp4?token=qBVBxdS3BWZ-5yNFsrCw7AB9GA2hyRnzsknf20OwLusZpmtI2ReEjM2kFmzrA7IVykJSguJmtg4c0ygMbQVMf1rzO3ULNBwdxf-JAqoSczuBdQNH5s-bZZZO9iipZnIuPslANDiDx1HUE3xdWOIF2R01-yVKpoNVuGOLMkAPVuWmKBxNHJd3NXtIFAlG5bt1RL81P6qd9ouMQTYvwgFbKQCN0JgE5oHtDWFthV07MeuoWgOGb1qhyLyH9Y_gkNefYU5sVi9lo42gK9uw3q4URZJVnCD1IlUMooUmCinn4n5o1ZhpNQa0tVWe0oyHo9KIjlugkYNG8IjWbv6cJKSQVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">Auraboat kids
💀
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/102312" target="_blank">📅 10:20 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102311">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZX-t7F1mfiTFNx5cIufMXR5g5DQQbw0J0oDVARzJmaKuoSU4vHBDEUCcy8jxyA4c8h2OkkEqZp1W6TKTusPauRJPkiCV5RJwQwO_ee168Efi8I2uk_3bmXy4_c6ycQcnZfkakiwpBfoOw3gj5_vkRz4MTCC82l84eRxaTdlJc6KmG3R6y7x60rCV3HiM3Pbl2c6Rcp5fZXBBOWV66zLs7TmizSCUonTKeY83BnGYqIJQ7dGIpq9r9626OQOtkU64ggNpSn6fyZJblRSLYBAbGpEm7MS8_6GEMmmED5_DVtc921yICGAvU4b0So6QePnw6WXjOa4-mp4LizWLBM2dCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🙂
تمام‌نیازمندی پسران فوتبالی سرزمینم :)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/102311" target="_blank">📅 10:02 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102310">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gY18BWVibkRFkbMHplkbnpKPAbNP4RnKIOPFK66vDlYUXoEpWUM80y2U5oyJ-ssMxjlEucI1E7rDsbwgtuqke5Ovr32uXiYVqufUVRxHX4L5T3I0mVGD035o5lOi6m4lW6PlswKPPP8T_ZgTsd65qsd8KqQEwcgYOr-90VTUFGumJ9aBEozbHpiduMAgQFf07KK4U66cG8QXp03yt4FDnzRmQGmvHUseK_QA-sGuUCV0CkjZStHJLkP8CEeFF2JCAQpH22L3wrniqhv_QFmaDU38hNbG6xbaQ9L9Fnz_IndDQwb4FtbCtrXGHyUrxCCSqcVgDYf7fG8EVv6TcgdOzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇹
🔵
فابریزیو رومانو:
پاریسن ژرمن و موناکو برای انتقال مگنس آکلیوش پیشرفت زیادی داشتن و معامله در قسنت نهایی خودش قرار داره.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/102310" target="_blank">📅 09:35 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102309">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mc3rKHmEU9oGz-PmCOUBes-fpd9cv79OoEg1kHp8SoyUs7ct2zogIJ2cRFSnr_VpDOM4hDU9FPAk13Yi6Ua2tYlO8evgIBARSg3rPMThnwzoopum0_Nk1HZJdJtPn7hafl6rPFTx1r0MGuGgi-bUcXmkrTIKpqTyQ-m86XGtWxJ79U7t9dx3RV_EC7K30QA3Qyuol2nTY-bgFQ0D69HsgT5KKossLuXtaM7KzlAd-t8yyMhujc90rDPN1cm3pp-fPoN7Kawo7Q7gikhqzQ6q1yp6zx0L_WsqZ5IJra495f89HilUW0rCZhxpyOftTdzP79AmTm_tpJjvYKNwQJ8V5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😳
بلینگهام برا زیدش تو تعطیلات عجب پایی میخوره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/102309" target="_blank">📅 09:20 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102308">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tkANkSLzxIIB6wCqJiwrudKA6DVs-b6SJnrPYQsUZcP5u5nTsL1EAec1741q3lCI-UM5qChSHeQkX-DIMBivP0VG4JNkysrctYo1nVExjmVfyTNku2tfp7407_On_F8w2ZyVFGEdi45PNvYehROj6qd0q3PsVoyV19NItoK4E_TReDZQtTp7N9-7lyDFW3sAqvASdmr4pl5L22fs1j-i0EVmlHjnkoFIs8ahk65Oh3YgxNP80UaLFEvBJlFz--g2a1ihSYnWqJCN6hVkk3t69hZlLaJO4qRO-8UYcAXYke3cfuIvK8VOjyK16Fl79VIdCBfn3LVdj-2g-LVEikZAfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❗️
عکس پروفایل فرمین لوپز، در حالی که تمام هم‌تیمی‌هایش در تیم ملی اسپانیا عکس‌هایی با جام جهانی دارند.
😭
🇪🇸
لوپز در بازی آخر بارسلونا قبل از مسابقات جام‌جهانی، دچار آسیب‌دیدگی در پا شد، که عملاً شانس او را برای حضور در جام جهانی از بین برد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/102308" target="_blank">📅 09:00 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102307">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/31f0971b6a.mp4?token=L4oR3A3-0t5E1D8qHdGHEnEarYhu5QoZXM9v5RjPe4EjGBiQTUEXduUr8L_qRQNL5aJeUe08RJ7RiEDjMKVyiKkWoERAfrbWHdpKFROgVntpn5TsS_5z2cJTr5vb3LIquZdWd56zKyGEY32wIf61kQEMnslEPwH7LZe9sIsV9nfSaU7QECsvXmOM8SI0C8QyABaWTnywXmY8j0gxcLYGU5MxGA55dDGNotYjVMaXrWaRY0d9N932nUkLjCRQePlIOIs0aBWlrI5eb9pe2nmtKLrPuqvUtTLZ3ZLmpL45kbTIgWFm9AKs-e-iNrRQ2g4VTbaTs_vH6G5tQvk-RvSTVA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/31f0971b6a.mp4?token=L4oR3A3-0t5E1D8qHdGHEnEarYhu5QoZXM9v5RjPe4EjGBiQTUEXduUr8L_qRQNL5aJeUe08RJ7RiEDjMKVyiKkWoERAfrbWHdpKFROgVntpn5TsS_5z2cJTr5vb3LIquZdWd56zKyGEY32wIf61kQEMnslEPwH7LZe9sIsV9nfSaU7QECsvXmOM8SI0C8QyABaWTnywXmY8j0gxcLYGU5MxGA55dDGNotYjVMaXrWaRY0d9N932nUkLjCRQePlIOIs0aBWlrI5eb9pe2nmtKLrPuqvUtTLZ3ZLmpL45kbTIgWFm9AKs-e-iNrRQ2g4VTbaTs_vH6G5tQvk-RvSTVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ویدیوی سنتکام از حملات بامداد به ایران
.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/102307" target="_blank">📅 08:18 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102306">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">‼️
👀
اسطوره‌علی‌دایی امروز رفته بود مراسم ختم اکبر عبدی که مردم این‌شکلی ولش نمیدادن و دنبال سلفی گرفتن بودن!!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/Futball180TV/102306" target="_blank">📅 02:34 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102305">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HiGRLnGkH-vYsSQstItgbbnMIRJoQ7CFVGTKYotSWtUiz9wRma-4drwdSS0FsPShE5HSRm2oa_3zNQP2AJTKAdRMpwpetixjMR-99YuNHYnOzGpLAFIBn8QTBMYQbhoI-qFZBNW3K2O_n50QbFhTzhtzEewK33d7WgaOkvQ1k-F2IGYUGyoSAgkCaCAUudX5Z4zgEiAizrm3eTPBfLH7rnyYN69CNATC-BxojAuNSZhaC3IvrBqWKA8NE8-669koQv4A-sRoTFNTZHbEMWeuBvKog_KoqkWEzwwFGtni8hou3jgaY1Tz3_IOsz9O2lDrVPU2MRf8m4H0Y3W0R5gG4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#فوووووری
از Cope: اولین پیشنهاد رئال‌مادرید برای جذب رودری به ارزش ۵۰ میلیون یورو تقدیم منچسترسیتی شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/Futball180TV/102305" target="_blank">📅 02:17 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102304">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q9kjejOc8yYSY0z2G3b3_Cd1aAZS64_YkrN7hBT2ExGvGf2-ff-FnBegpCy6r9a5Yhn8ewpkUV0Ipnq6AGfnugV6MhCD1B3ToQfmtgyXRLSuZniErvpfaA65NX2FENTZWIFIzzj2MmuRRcv9Dv4Y2W9EgD1zkHLsZ0kJjnyLgKWAxP7j2C8UWjxT50XZrkJ93lh2DqDrmgGn4ZOGC_iihj-yM5Hp6K1hT8aq7nlSRx9_skRoHN4_OgwP8NQbwHYwEPcQPSbkJy6EYNQLwUxDUlTKm9fwzvQqr_Uqu7tNEPDuZseGWT1cU_F-SqNYMPtlhAZDUanUvQa3moH2J6YVfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇺🇸
🇮🇷
وال استریت ژورنال گزارش می‌دهد که دریاسالار برد کوپر، فرمانده سنتکام، طرح‌هایی را برای یک کمپین هوایی ۱۰ تا ۱۴ روزه با هدف قرار دادن زرادخانه موشکی ایران به ترامپ ارائه کرده است. ترامپ هنوز تصمیم نگرفته است که آیا مجوز عملیات کامل را صادر کند یا حمله محدودتری را انتخاب کند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/Futball180TV/102304" target="_blank">📅 02:14 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102303">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6afbb43876.mp4?token=pYEud3Ay4wrCoLu_OqrKY7pLUjCW64BfaQ3UCpFpK50NpJiOI8Q7V9jJKxDFatYdJnT9n0VYiZle_xh1-aeKdAWHzja4icCXJtWM74KtWXDbtcMUXH8GdCWkAwXLCsDsukcoIxBesJ_AvaxT2N_3oH_tVftNRUTEoeVkEmfaYqelt46FnI0r2ohmDK_w8K2upkr-ZLJNMlI5mhG7bswC3BAyAMzUK9ORPB6qjmiqfiik8Mek6rjMMUcJV-QPd6e0JyyyI1VuZDoMB2EERyLkzLvx6HIvB5yHRwHyBMxKeqpxZM0KQ_-wmQtUfc5p8gocAo7mfrj4bXcuFRlawHY0jw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6afbb43876.mp4?token=pYEud3Ay4wrCoLu_OqrKY7pLUjCW64BfaQ3UCpFpK50NpJiOI8Q7V9jJKxDFatYdJnT9n0VYiZle_xh1-aeKdAWHzja4icCXJtWM74KtWXDbtcMUXH8GdCWkAwXLCsDsukcoIxBesJ_AvaxT2N_3oH_tVftNRUTEoeVkEmfaYqelt46FnI0r2ohmDK_w8K2upkr-ZLJNMlI5mhG7bswC3BAyAMzUK9ORPB6qjmiqfiik8Mek6rjMMUcJV-QPd6e0JyyyI1VuZDoMB2EERyLkzLvx6HIvB5yHRwHyBMxKeqpxZM0KQ_-wmQtUfc5p8gocAo7mfrj4bXcuFRlawHY0jw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
⚠️
عصبانیت شدید آزیتا حاجیان خطاب به مردم در حاشیه مراسم ختم اکبر عبدی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/Futball180TV/102303" target="_blank">📅 01:55 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102302">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d-ULDr2bO23KF1n2QecL3EVvh6rn4e0jSxb_2FX6W73GJvkY9e_zl7-Ff6NNyjYzUfKc05t-9JKkWQ-1F8QGmYtgJk5r0B8mJjNp1QSkOgcGp0_rOpYJ86KMneOWp361DzzH7eKCqCknEg3XxDGm4hOkvvYjBsNT3L-fnZ1z5rPCvzc6p-xpRvhzhmWDElC60IM5cvV8ZRFanN9FvJ2ShAnsvisvLO9VrFrffQxXsL0BV8w1EoAGWKZ136ua399U58jgShsB2DCvcl0L1z4x5N-p-ycYs4pm6_v_6tnreG-bfT_n3bI1BXfPL7kZD1E76jg8SfpbAhRxALZ43iFQnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
🟣
بازگشت لیونل‌مسی به تمرینات اینترمیامی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/Futball180TV/102302" target="_blank">📅 01:33 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102301">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a4e2122bef.mp4?token=HgvShlLPDCGku7wXfOI72StERNE4stu8pjsUfG5Bb9en3qSvZXF1CShP5l-jSKdjKfQxKUxbqox2PVY5bCoRN-zkCTaFQ0GB-juuGWFQkt7X6Ah-UlST0SMdnWjyjSE21ciGwV9Jiw9fIswK-aGWFu_B9Wg3id2cZQumPvHPUvPYxfocDek4icDWGdla6PwQ9Uai8GIhLYLXbbOHAm4vbEBIvuq9Mu8_47l5b8vRjT4G8iTcKN5_n-C6gATgWASpcrH_gL1xhE0_iEwQMyGI2vUjTv4NLLW-5sfeOrIi4hyjSH-cnzQaznvSuKuHNepWqFrtdFHH9piIJu52fnpA1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a4e2122bef.mp4?token=HgvShlLPDCGku7wXfOI72StERNE4stu8pjsUfG5Bb9en3qSvZXF1CShP5l-jSKdjKfQxKUxbqox2PVY5bCoRN-zkCTaFQ0GB-juuGWFQkt7X6Ah-UlST0SMdnWjyjSE21ciGwV9Jiw9fIswK-aGWFu_B9Wg3id2cZQumPvHPUvPYxfocDek4icDWGdla6PwQ9Uai8GIhLYLXbbOHAm4vbEBIvuq9Mu8_47l5b8vRjT4G8iTcKN5_n-C6gATgWASpcrH_gL1xhE0_iEwQMyGI2vUjTv4NLLW-5sfeOrIi4hyjSH-cnzQaznvSuKuHNepWqFrtdFHH9piIJu52fnpA1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🟡
افشاگری مدیرعامل کارخانه فولاد مبارکه: دشمن با بیش از ۵۰ موشک مارا هدف قرار دارد و بزرگترین دستاوردش در جنگ همین بود!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/Futball180TV/102301" target="_blank">📅 01:23 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102300">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ku26Kz1zt-ibXTm5TXRKhyrB0Hrjrb_N4ilpCVT-aDjt6JJ1owlgff_Bhx8bNPhe9L2h0SW5cujmYPDsW2ke2sbBewBp8MwTwq6wkgf6-X6gUUPomLQmz66EKjRWB1_WFSv_FZpDzgQD-7XkQCl6O-MfR_YlpM7KrprOHdovmVppAiT73jQFTerz30-g4ltjSG1Gl-e6z8pP_6lrRhuQXTRlsH7raCdHBvUgFLjDdN8_7JvuIu5pqbEanMQWL2PtCnHTWLjZZ_SFM0dbbkY-TXJuGfe8iumZYKNzaQ_P_UIYa2JNnQZzhr9_0v12NCDUE_Ymznym33iaLdXRFIsMOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📱
📰
به دستور ایلان‌ماسک، صفحه خبرگزاری تسنیم در اپلیکیشن ایکس(توییتر) مسدود شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/Futball180TV/102300" target="_blank">📅 00:58 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102299">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/07fe21feda.mp4?token=PA0IUl90Z5AolRm5AGCp12dFeakgWBMA8cpQXeEY4Mus8V9qz9ALsoDhF4lZN-wRlXz0Ty6wKyOzUtX242OVGRMmIbwnYXe0GdXbVJaH7Ni26_fPa82FxH-xKZ2SFduE2rmOW_Q5wCDhhKpa-QaA3Xwp6-7Xz9mmweG8Jc5E_vwWWWZ0QK2iUrzytqHpCrRB4S-Gu5gSfqLJHoVoD1a21jeXppeYQtn-gYngdj4Swx9Br0vb3pW6tOGYtHIvoSVncKz5GfBzg1WQSulMFqJHjoCnJZsy6Hy_UvGHcOm2WeqG-_fKsEOkkFBXQIhI6CG4BYNkzCyO4merQUQfyI-BVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/07fe21feda.mp4?token=PA0IUl90Z5AolRm5AGCp12dFeakgWBMA8cpQXeEY4Mus8V9qz9ALsoDhF4lZN-wRlXz0Ty6wKyOzUtX242OVGRMmIbwnYXe0GdXbVJaH7Ni26_fPa82FxH-xKZ2SFduE2rmOW_Q5wCDhhKpa-QaA3Xwp6-7Xz9mmweG8Jc5E_vwWWWZ0QK2iUrzytqHpCrRB4S-Gu5gSfqLJHoVoD1a21jeXppeYQtn-gYngdj4Swx9Br0vb3pW6tOGYtHIvoSVncKz5GfBzg1WQSulMFqJHjoCnJZsy6Hy_UvGHcOm2WeqG-_fKsEOkkFBXQIhI6CG4BYNkzCyO4merQUQfyI-BVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❤️
پلن آخر بارسا استفاده از ترشتگن تو خط حمله
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/Futball180TV/102299" target="_blank">📅 00:55 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102298">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f5jYXvmYBev8jGw9xYWNtdXlQ520UQIUhNK_qHGwPDWqdpH3c-XCPpiy3x9Fw0koA8HV1A6Ii7jDLPveikglq7WqPr0Wv44jR7BCyoYfyAOS5OKHtGfcRve2R_XFwLMT2tEEBG7ou-buBlLwg_Etm6Tncyk0nbAngfth0T7y1sIjacSJCfqFEJyRsZ34xw3GPZ5EsYukSY9znpTMHKi8m0xggr0BpYHXqOuaS8X7BfgDRhR_Af4bS3M9S2VhrULwwBBSUcFYHX5-Hgg6nzFaN4lxTi1QkW8ixniW9oc-fv6fjJmdl_CD9EhIRjP9_l0Jxl8i__GBI4nkxoycPOZqKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🇪🇸
په‌په‌آلوارز
:
🔻
مورینیو، وینیسیوس را به عنوان یک عنصر ضروری در رئال مادرید نمی‌داند.
🔻
باشگاه، این بازیکن را مجبور به ترک نخواهد کرد، اما در عین حال، درهای خود را به روی یک پیشنهاد "مناسب" بسته نخواهد کرد.
🔻
همچنین، باشگاه قادر به پرداخت پاداش قرارداد به مبلغ 80 میلیون یورو یا اعطای 80 درصد از حقوق تصویر (حقوق بهره‌برداری تجاری از تصویر) به او نیست.
🏴󠁧󠁢󠁥󠁮󠁧󠁿
از طرفی نمایندگان آرسنال پیشنهاد خود را به‌وکیل وینیسیوس ارائه کرده‌اند و حالا همه‌چیز تحت نظر وینیسیوس برای پذیرش یا رد قرارداد با تیم لندنی است!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/Futball180TV/102298" target="_blank">📅 00:46 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102297">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vOh7TKKAdpYcsHC11BjZy1TVaekyqeMBeT_XIzjGzX1h1YiY2xGK8aTpAXusztt6AM5TTcx9D38aio_54DmWTYmNEkl35NkfBCg217vx8FB1ivu9f-foK4JmUWrYsz796hyBdysL5LZhtSvMQKUL5zQKu2i1D8cb9MO9t0uOJ6-hUlendT32aOPTy7m6RRmWVhdCoiTlNire276wdJv3ZfNumvo9nvx5xtMhDcvX4mJjlBGo2QPiYlelz7K_EiDH9Djjh8H7rjDYOC_MfY4VDduWAvc1dfnZPXz0a7HgJxAfubN7lEdyi_smwgqeoaZgGMl6PPpPfGfD6SeBF95szw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
‼️
🇪🇸
🇩🇪
فلوریان پلتنبرگ: امروز هم توافق میان رئال‌مادرید و لایپزیگ بر سر دیومانده حاصل نشد و مذاکرات به فردا موکول شده!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/Futball180TV/102297" target="_blank">📅 00:37 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102296">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a93d51cbc.mp4?token=GxWJ6s2duIeI8d0HKLQnSoy-GXpKRSXGwgzxRyMBnfbom12YTZPP1X0i-O6-_QKjTaqPZoCqn65VlDgHND_OoE-LAoOB2WexUltSQ8bpN4jKUgGWH3EUR9tsCa8BmppF4B3FtJNhcqRKWR-8WzF_XAVre05jPjE2db3WOM5teQ-9byiuVt93ZUoUYbFp_tXYAO5FenIK6D2ZQSeetHHvNE4o3NYvOD6pN5RiLYU6crGO8vrcoUN8RlXQhbiqypHIm1DpNgNeTNk4KpJ06Rt3_5w9_HptGqnAuqfHuhU8DB_Q1M9i9sNOO2X7VWnm7fgIjpnvHo5THgdJiK61gDV8vDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a93d51cbc.mp4?token=GxWJ6s2duIeI8d0HKLQnSoy-GXpKRSXGwgzxRyMBnfbom12YTZPP1X0i-O6-_QKjTaqPZoCqn65VlDgHND_OoE-LAoOB2WexUltSQ8bpN4jKUgGWH3EUR9tsCa8BmppF4B3FtJNhcqRKWR-8WzF_XAVre05jPjE2db3WOM5teQ-9byiuVt93ZUoUYbFp_tXYAO5FenIK6D2ZQSeetHHvNE4o3NYvOD6pN5RiLYU6crGO8vrcoUN8RlXQhbiqypHIm1DpNgNeTNk4KpJ06Rt3_5w9_HptGqnAuqfHuhU8DB_Q1M9i9sNOO2X7VWnm7fgIjpnvHo5THgdJiK61gDV8vDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پشمای اورانگوتان از بدن کوارشما ریخته
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/Futball180TV/102296" target="_blank">📅 00:32 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102295">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd4b353d1e.mp4?token=tKzJ1SD-CXBpAal60aum2G3iHKYT9QzcspMXfRCJPwLv7nolZcLfaD2sNuIO9lj5J2hkKj1UpwEl1PIttkVyM_0c6he7bkD-f50IGlahHcg1av8I5legaTbZqVOJ4KpynaBC0tvF4Er65ZC7Jf4lAPE_rCi3m-a_ND2VqBHkzzxTXBRJSn4z_fBU7uT3Lo-D24nHRi_98xz9hmaoFPq_3jEzT3-YH2fdZcHXOILtzdct3JKAUjsyMio2TXe3zf-wG-zwuru6vzw2i_7Tj7zk-4mS0_an-OOaA-330qGf1wxon8RYGR6NdIxzqWJP3CNNCXwgS3rrhdfO5tDuXu4rGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd4b353d1e.mp4?token=tKzJ1SD-CXBpAal60aum2G3iHKYT9QzcspMXfRCJPwLv7nolZcLfaD2sNuIO9lj5J2hkKj1UpwEl1PIttkVyM_0c6he7bkD-f50IGlahHcg1av8I5legaTbZqVOJ4KpynaBC0tvF4Er65ZC7Jf4lAPE_rCi3m-a_ND2VqBHkzzxTXBRJSn4z_fBU7uT3Lo-D24nHRi_98xz9hmaoFPq_3jEzT3-YH2fdZcHXOILtzdct3JKAUjsyMio2TXe3zf-wG-zwuru6vzw2i_7Tj7zk-4mS0_an-OOaA-330qGf1wxon8RYGR6NdIxzqWJP3CNNCXwgS3rrhdfO5tDuXu4rGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یامال تو تیک تاک : دوست دخترم خوشگل ترین دختر دنیا با من آماده میشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/Futball180TV/102295" target="_blank">📅 00:16 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102294">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🔴
چالش ۳۰ روزه: از صفر تا سود مستمر با فوتبال!  ما یک چالش ۳۰ روزه رو شروع کردیم که توش با تحلیل‌های روزانه و مدیریت ریسک، موجودی حسابمون رو چند برابر کنیم. تمام تحلیل‌ها و فرم‌ها کاملاً رایگان در کانال قرار می‌گیره تا خودت روند سوددهی رو ببینی.
➕
پیش‌بینی…</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/102294" target="_blank">📅 00:16 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102293">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/316f36114d.mp4?token=hra5PyE_C46H2aGMpANdpP0SqbyX8n4mTLtQBUOcG8uA9VZVm9yVenBrtETVyE0fj4DvsaIE7YZM-cAGZm_UjompVuabHGqZZdPmQ_ipI7lIyejJULPepg8M4KwxLMkcNRFpnEhtuv9Hf7XfrJP2vpXT89HJrWegJmGZ8UftCLxvizmNJgmDyPjzvz5tw1zfSYaszsrmb1xhmLbHAaTt9PF3jV2-LfarBSPkhpPS7ApUxLWbDHFV4nwGHTKOE0wRBhTkhDWiee_u3PPELK-GxmonCR6GmjJmJddFYsPU0_33bh3kIBDUlXI1ROqifbg9hOKhHG1NVU-g2z-b7P920g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/316f36114d.mp4?token=hra5PyE_C46H2aGMpANdpP0SqbyX8n4mTLtQBUOcG8uA9VZVm9yVenBrtETVyE0fj4DvsaIE7YZM-cAGZm_UjompVuabHGqZZdPmQ_ipI7lIyejJULPepg8M4KwxLMkcNRFpnEhtuv9Hf7XfrJP2vpXT89HJrWegJmGZ8UftCLxvizmNJgmDyPjzvz5tw1zfSYaszsrmb1xhmLbHAaTt9PF3jV2-LfarBSPkhpPS7ApUxLWbDHFV4nwGHTKOE0wRBhTkhDWiee_u3PPELK-GxmonCR6GmjJmJddFYsPU0_33bh3kIBDUlXI1ROqifbg9hOKhHG1NVU-g2z-b7P920g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
چالش ۳۰ روزه: از صفر تا سود مستمر با فوتبال!
ما یک چالش ۳۰ روزه رو شروع کردیم که توش با تحلیل‌های روزانه و مدیریت ریسک، موجودی حسابمون رو چند برابر کنیم. تمام تحلیل‌ها و فرم‌ها کاملاً رایگان در کانال قرار می‌گیره تا خودت روند سوددهی رو ببینی.
➕
پیش‌بینی تخصصی بازی‌های دوستانه باشگاهی و تورنمنت‌های معتبر
➕
فرم‌های گلزنی (بله/خیر) و گل بالا/پایین با تحلیل آماری
اگر می‌خوای از روز اول چالش همراه ما باشی، همین الان وارد شو:
🔗
https://t.me/+L5I8ulM6jEc2YmE0</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/Futball180TV/102293" target="_blank">📅 00:16 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102292">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VRoQUekpev5A2rNCB0epsMpBhrIGzke-kvppxDhLL8XV1ObfYuvUYdFy_HsfztU9ox8B60sj6p3vk3U9pKbho0sMcCUFQtwWcDmM3qadaxXMl-nz8mXFTiQXJkMYhGn1JcybhEFO57hxyLHvz_neOBZhQMD1tT8YsbxAwZPMuqP2tKmtU0dxo2zpa_l933XDXjTZfR7kdvRyFnFCttMyrnkJl9L9Y5_hM9QmAHDEOZ70cq7Spim4g4-82TTrszr9JOXk9XZSMo7mL_7fYWvSI7unoh6IGAYcDGijU6gevuFyfgRKHtM3WHpvCZqmunNjrzPBGtfq8skol1bOLG3t0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚪️
فوووووری از پپه آلوارز: مارک بلینگهام (پدر جود بلینگهام) در پایان فصل گذشته با باشگاه رئال مادرید در مورد جدایی پسرش صحبت کرد او دلیل این صحبت رو اختلاف نظر در مسائل ورزشی اعلام کرده بود.
باشگاه اعلام کرده است که جدایی او امکان‌پذیر نیست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/Futball180TV/102292" target="_blank">📅 00:13 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102291">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZINZyUHgsBqzSzRXrHZ1PanicYvnn4g51zX47haKL8TzveBVvX8AFvzxcXgLTyxAlbP91MVDMcnXyAq7k8wSm5Jsuy87cGJ4y4lOmGrUie9lpv1x8XtLZOfdn4dMactj0c2h-9mDZUWlyAiCln8eOpwbrQ0zv17ewsNKyWN9UviiO0GE3y_h5__QWbkEUm_AXb6vbI3-xAi9s7Mo-HjBPbqLf0jSa-Gt1JxoXKPuFyjnwZC7Vpp1QEMysxd73xPlmyB2sB1unN5iG3RM0geSPVbW3nRv5taFyEiBLfHHaubT5ZjeNHapX3CTYbOOuEjriRx8HfRdc4xviLoSDFIc9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
🇮🇹
فوری از شبکه DAZN ایتالیا:
استراماچونی از ایران برای هدایت تیم ملی این کشور تا پایان جام جهانی ۲۰۳۰ پیشنهاد رسمی دریافت کرد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/Futball180TV/102291" target="_blank">📅 23:40 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102290">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pDRCss4P9qqoKw5JxZTwm3MMwBUH9UOlW9iOxfDYCPuHPdu8zWMGpl48ib-UapJJ_tzinytYxKZ-KAii3qoXfV50Jn9GPrauGbbiP3nPDN-kn913h63nGitmX6pmFJimAq16Q9lo3sHWHDh4ldq5GpkCGFwIGdk-45AcVwpJOX4X6UndWmctT_zMI1_860zpBkQvvhCNQw4QiksvP-FDUsnjIkIJuVSBEEanZfnoOOn6c8QYHZ-T2HN_CKx4oGoXhZT5RN4Idu0iI-e5b7J9-mhn7zD9tzTpMyj47bX_dgl0-S9ks5kmeP25BfoH_HTB9yZ0_WQhwEPYVSfTDipdjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
فرمین:
این بدترین تابستون زندگیم بود! همه چیز داشت خوب پیش میرفت که مصدوم شدم، اوایل جام جهانی نمیتونستم بازی هارو ببینم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/Futball180TV/102290" target="_blank">📅 23:01 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102289">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rV4AhkDlgPiOXGh0RpyFFn4TYJU3GRa310afhTpKgDtVHovi4P6rtL_vXKxJr3Wr-6auLugwyLSz5BNMIIXOADqzXTnwOo7aulEOeJ8klXsOOpVMCVoIt9nrPTQaYrpkGvJV1_oJkqFz4vY_wtMdy4l55a9O9Gb4veZ3uenprnnn3zsg-kxsBh7XZ2rmI__71bu5JNURnC0ja5oNpy488MtXVLEC6pcwVnu8Qj_h1peEk08ZlFbcThMLFeOzmS0oV4IQj8ewN6AemPFYjlPH1JXX6fOSzbhFOZEBT9imRLUHBrMpWMdppWltTVOqp7G6NSJU5WmC0t8V702uN2P9HQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
کیت سوم دورتموند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/Futball180TV/102289" target="_blank">📅 22:34 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102288">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OL6lEeDifwXpbVxItewGz3g37sIywaawxVEqmjAAgTncGKy_zJgzmNL1d7z4a2e7KlIBuvGR2Bt-5_EtaBoU8VXPq-owbsskC-4ukwbYdOLgI1_Y87F_-Yp_y_pg6pFNfxuO6f5u5Dw9c26tLCxJg_sAaO-AsbXGjbPK-eJioZx_4Qi3YH1SDJkrrQ3GJKyxS66SVEJ4nuU58PC7CUXOLpJLtXJCsA4LzGdS8f5O0inqLVyAl9qAnuc74CnfgalDrFAEpEjwShXSkJNTrHFlFQCNT0oqGSEcs5swJABeYebAyiXXvIHA1YBC5zQ89NmF9NFjEfLoo_q3rxbW3SCZIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست جدید رونالدو چه سیسی گرفته
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/Futball180TV/102288" target="_blank">📅 22:19 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102287">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f5b210f5e9.mp4?token=BSrstAeX9_OxuEpt3GtVAbYVh0AScp_pq-C3X8tjLMMz7x_aQt2lyeqY1rP3vtKfbbxkXGD5b7VzPoHI023A9UVMeeuAdTccjvbHQtqOsFrdxNX8DrE76SgEeT2Y0_1TSNkox21fEfuIkVUZtt_O19Lk7kVcs_WZctskiWJP0ZDtjZWpJjGSQjzVj3ccup5NDNVLs0tfl68Fk5KmVthEZATrSPDRPpyl75Dfpc64c-msGa6UUouX9x5yzSaM3Bm93YWlwyI7_0PPKfB-r_FRDBU8qlkOodxh9_oHW7PMM81DecHjUfnd42rN_Ch_K9EUOwtO-v3C-RaRTfOtBsAljg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f5b210f5e9.mp4?token=BSrstAeX9_OxuEpt3GtVAbYVh0AScp_pq-C3X8tjLMMz7x_aQt2lyeqY1rP3vtKfbbxkXGD5b7VzPoHI023A9UVMeeuAdTccjvbHQtqOsFrdxNX8DrE76SgEeT2Y0_1TSNkox21fEfuIkVUZtt_O19Lk7kVcs_WZctskiWJP0ZDtjZWpJjGSQjzVj3ccup5NDNVLs0tfl68Fk5KmVthEZATrSPDRPpyl75Dfpc64c-msGa6UUouX9x5yzSaM3Bm93YWlwyI7_0PPKfB-r_FRDBU8qlkOodxh9_oHW7PMM81DecHjUfnd42rN_Ch_K9EUOwtO-v3C-RaRTfOtBsAljg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
ادعای نادر فریادشیران درباره بیرانوند:
اگر بیرانوند همان متنی را که علیه علی دایی نوشته بود، جلوی من نوشت. نامرد باشم، یک ماشین به او ندهم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/Futball180TV/102287" target="_blank">📅 22:15 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102286">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vaU59IX1nwOdmzjysRtNLV8HW7yc09R04xuAC0tl7FqXKNVL4E4wx5JxfB1vn1f2HdGcdk2w1RDLdB3GsXjjjT19lnmy-tiL4VIPrppiwSL5Oxu4Fd9I_f17SsWXFdpcAysbJKXI7aKttLNPfhMycL9HuXOgdVnbqE_cVYUfjgPwyBMaUQARiBg19x8hxx6ExwHGCdXvNrd0J2ApYhgcxanxKugKr8bSUzKX2weeFFUCVlVlMX04fTs1hwCNJi-0Deq4RelAmIvxmsRbFOXnDman9OOrzpIOHMtRZCsJnFEGqSge2Ht4v6tGJy6zVs3fbhle1ejG4GmXnVnlFbcKvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇦🇷
فیفا بدلیل نمایش بنر فالکلند در جام جهانی 2026، پرونده انضباطی علیه آرژانتین باز کرده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/Futball180TV/102286" target="_blank">📅 21:50 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102285">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb35f99ea4.mp4?token=NLyx2B6TyhuZz6iYK1Evm3j_pczjddA2sWckVRuPe5OFhotMAUv3G4kfmgzQKRvMl_SeRoit9iMgAlGsqyHHcjTVdyL711FBTd2XrD2zqhs5Pnncofidv-5ZcYhevzDsQ69wyUuuJld2C_a54GuJmwNmQdLPhMPNu_V2xugHgT4ribnfgndDOV7UOoevBA35vGJX7VQzF-sIDrXJonrZX8W_HwfTj1PavC9wYC4jD1Cfp70Kz1TRboS64svPZA8mmZGTMipt8nWx00-OlRQIhnTpX_gw3FzXDSNzpl-kqbQ70wb9AcNmOWaA7F3S5m_hvzIJviVT780B7rFS8e59dw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb35f99ea4.mp4?token=NLyx2B6TyhuZz6iYK1Evm3j_pczjddA2sWckVRuPe5OFhotMAUv3G4kfmgzQKRvMl_SeRoit9iMgAlGsqyHHcjTVdyL711FBTd2XrD2zqhs5Pnncofidv-5ZcYhevzDsQ69wyUuuJld2C_a54GuJmwNmQdLPhMPNu_V2xugHgT4ribnfgndDOV7UOoevBA35vGJX7VQzF-sIDrXJonrZX8W_HwfTj1PavC9wYC4jD1Cfp70Kz1TRboS64svPZA8mmZGTMipt8nWx00-OlRQIhnTpX_gw3FzXDSNzpl-kqbQ70wb9AcNmOWaA7F3S5m_hvzIJviVT780B7rFS8e59dw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یادی کنیم از روزی که نیمار باعث شد کرک و پر امباپه بریزه:) خودش هم اصلا براش مهم نبود ضربه رو زد بیخیال رفت. امباپه اون پشت داشت جون میداد
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/102285" target="_blank">📅 21:42 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102284">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromچِشم به راهیم</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8732bd386a.mp4?token=s-_aLebEhJB75a0C1LFEVk8UsIGWfzKmfYEN7VulUSeRtErwDGr8A-RchSsuCLzADkYdLa5bq-TSl5dclglO4-MWnddmznpAL-CoUcpi-xPYnpxMG_rJGWM0MnClgoDdSz8YddqmH6xbVjKcQFYgZc3ZIyFftzslHRVlUPUIEcax1STD_mdJ9bhHtTv37cEbWmfVnAFRFUxbycJf6QxasaJJQCcGktBXiqQd9Ikc8LPtNH56vdT2PKTf2Ln5SYDGsdELOFgW-yqlpdO5fQBRnR9XyShcJi60aplCMVeJnIcv3nnH91ZupuKBkqm3haL2PoMIVUNXK_er6lGRL4e9uQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8732bd386a.mp4?token=s-_aLebEhJB75a0C1LFEVk8UsIGWfzKmfYEN7VulUSeRtErwDGr8A-RchSsuCLzADkYdLa5bq-TSl5dclglO4-MWnddmznpAL-CoUcpi-xPYnpxMG_rJGWM0MnClgoDdSz8YddqmH6xbVjKcQFYgZc3ZIyFftzslHRVlUPUIEcax1STD_mdJ9bhHtTv37cEbWmfVnAFRFUxbycJf6QxasaJJQCcGktBXiqQd9Ikc8LPtNH56vdT2PKTf2Ln5SYDGsdELOFgW-yqlpdO5fQBRnR9XyShcJi60aplCMVeJnIcv3nnH91ZupuKBkqm3haL2PoMIVUNXK_er6lGRL4e9uQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎦
نذر سفر؛ سهمی کوچک، اثری بزرگ
🔹
در سفر اربعین، اگر صندلی خالی در خودروی شما هست، آن را نذر یک همسفر کنید.
🔹
هم‌سفر شدن با خانواده، دوستان یا هم‌مسیرها، علاوه بر کاهش هزینه‌ها، به روان‌تر شدن تردد و کاهش تعداد خودروها در جاده‌ها کمک می‌کند.
🔹
اربعین، سفر همدلی است؛ و همدلی از همین انتخاب‌های ساده آغاز می‌شود.
#چشم_به_راهیم
#اربعین
#نذر_سفر
#هم_سفری
#سفر_ایمن
#فرهنگ_رانندگی
#سازمان_راهداری_و_حمل_ونقل_جاده_ای
#حمل_ونقل_جاده_ای
🌐
rmto.ir
🌐
141.ir
@Cheshm_Be_Rahim</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/102284" target="_blank">📅 21:42 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102283">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p1ZK4M0_j8F-q_gSwlmllLtRdRGYJJLyXXqjRetMMoPEsiPpqM3bHXjow2pvClrZ6Ykg9RNbcPxT0PrRMUH1cAmy-JEphyzGQRTm-UJpI3ILC7hIZGOS89CUdRIw0tYKXctLb72Wb_rMu8Ww2vWsd3nzuyk_xesT_SOyeiX8X98JMh4HbpP1atodKOOxJoRuAp8GhLy9xQHlJzqMqbWMvPcB4izc0LuVTlRHxE1-8LAlEv5neH2yWyRIZICdwcDEkGgWQTeT0mD2-2H-zWH7Luz1CG6TB1fANm53GyRMpt6EzflWImm7ic53YateeBBfu5h5l0iTbf-OFta1YZkC4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست جدید جورجینا که بسیار هم پرمحتواست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/102283" target="_blank">📅 21:40 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102282">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AM2yKOKWYKgbZdr2sMyHoii3Nvw_rK7h29P_kcJltlEGfAIiuByR4Sey0evjNZFExlbPaqeMiiIWdnT3Lozh2DX1Lxx1i6o1b6nmUxisskpDi6iY1Q3S5CClHY6eiKFZsmLugfXa5wY64cKuf8mt2GcKl9az_jth1-eTTMkdi60cUTwNgTF1_-JlTME8P8sENRM6USQwEIakHk5lohqKMOmiDt8ryfODFxcD1c8_X0lKEOASLppOiGIa_G7t1F0eyyAwkHMeMVPGqVcwdtwXBZTGGN9VyKblUSQLmxCLif8KxPUvnVFaxY5oAuelH2QxxhaTBL_89Nqrcl6UHxy02Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
🔹
کریستیانو رونالدو از زمان پیوستن به النصر تا الان حدود ۶۲۵ میلیون یورو دستمزد و پاداش گرفته!
❗️
در کمتر از ۴ سال، قرارداد رونالدو به یکی از بزرگ‌ترین قراردادهای تاریخ فوتبال تبدیل شده:
✅
حقوق پایه (۳.۵ سال): ۵۹۵ میلیون یورو
✅
پاداش ۱۲۹ گل: ۱۱ میلیون یورو
✅
پاداش ۲۳ پاس گل: ۱ میلیون یورو
✅
دو کفش طلا: ۸.۵ میلیون یورو
✅
پاداش قهرمانی لیگ عربستان: ۸.۵ میلیون یورو
💰
مجموع درآمد:
حدود ۶۲۵ میلیون یورو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/102282" target="_blank">📅 21:20 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102281">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1795b5f8ad.mp4?token=tWU3uYCB5zZRy2iE3r2d5AhZ8QEPwRAac_57p9zXBq6Hi88FoOevANPbQhp11TyDERf7yqc-tr20uRwqw70DzQHUVWhexBIbwVRQ8YTjjev6fXasyvXE1UWejNj_UitJxc_wto2XnpACzTWwFg_7GmkK-LmU_wgnfmkp7sYaaWREyROTIs3mvSZhil9fF5pmhIBiWTqmquhE2XOWEt8w2sYnWQF6eZJf5DoNbJuwC5x7UgyiSxx71Md7cn7RoWzXfnmcQm41iXTZOdslbG8r4vgzPO9QJIhJrHvYT-oL-PQ8uOcb99sFA695CX30UL-ESPy_LMoFrLmoovptz55QZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1795b5f8ad.mp4?token=tWU3uYCB5zZRy2iE3r2d5AhZ8QEPwRAac_57p9zXBq6Hi88FoOevANPbQhp11TyDERf7yqc-tr20uRwqw70DzQHUVWhexBIbwVRQ8YTjjev6fXasyvXE1UWejNj_UitJxc_wto2XnpACzTWwFg_7GmkK-LmU_wgnfmkp7sYaaWREyROTIs3mvSZhil9fF5pmhIBiWTqmquhE2XOWEt8w2sYnWQF6eZJf5DoNbJuwC5x7UgyiSxx71Md7cn7RoWzXfnmcQm41iXTZOdslbG8r4vgzPO9QJIhJrHvYT-oL-PQ8uOcb99sFA695CX30UL-ESPy_LMoFrLmoovptz55QZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ریوالدو، نابغه‌ی تمام‌عیار
🇧🇷
🔺
پای چپش چوب جادو بود
• هت‌تریک تاریخی به والنسیا؛ قیچی از بیرون محوطه
🔺
جام‌جهانی ۲۰۰۲: معمار خاموشِ قهرمانی برزیل
🔺
وقتی رونالدو و رونالدینیو تیتر می‌شدن، اون بازی رو می‌چرخوند
🔺
توپ طلا، قهرمان اروپا و جهان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/102281" target="_blank">📅 21:01 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102280">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r85FWcNxR_WfNxM7pxyNYWwDpZHV78133jhrHS9-TrXicyDU6M-QtfmFq7QN3TzpH5GOpcgahyUgA06z4Xb0AXKNFgbzYAnpwe7dYiPkgvizdN5cI_PpsGsSPcJZw5eyS7sNTFOTR6F0fGajPOJkdVDABLv7orkbLq-XmMY-GLbj2zguFyK0THbW5aOfMZIfk_ZZennntQr-HgZOqXTPEtepYoF_fA2KWXWac6Rs4vPMIiaDnDqzpntzbpiR7ZqNvHzu_Y5qSTdXivqJZxpnr9dQY8cGHpLfL6YWRg1fni99d0nPijlBRCjJLZsDbyhgPdRDzb7EQ1t0YNwh4urf6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
🏴󠁧󠁢󠁥󠁮󠁧󠁿
اووووووف کیت‌جدید منچسترسیتی رو ببینید که قراره دو سه روز دیگه رسما رونمایی بشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/102280" target="_blank">📅 21:01 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102279">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tWlZE5xyYyudWw8ers7E6XP8O37i-xRWMuM2Xeb3xgoNA-GI3H7Bl-pZO6KISbPGTiY9Fg3o41GGf3TMxeW6-fQRI727cdpbnXivdz9rhfgRQU34J5hNXJDvaBDI1m1_fEpNkUsGhhnDpb1eywHnwK1PbgDJhcRnwJFy95DCkslIIJWyUK3LPFLJZ813SZvr-c2wODZletjUQgPqeo2CCVocfDqfuGjG2GGS7Tz51xOkimQMfIwvsZ4DN-RtyiOLPvWjocvGOKjc8hf3yu5yF_J-gfjL3qDcZdfy6QiEPBXB1CmXnMOsFvvdo6jfaw2XEtiPjP63z_edEUpAqKgOhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
⚠️
🇪🇸
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#
فوووری
: رسمی: الی جونیور کروپی گزینه خط حمله بارسا پس از شکستگی استخوان متاتارس پنجم پا تحت عمل جراحی قرار گرفت. مهاجم بورنموث طبق برنامه زمان‌بندی ریکاوری، انتظار میره ۳ تا ۴ ماه از میادین دور باشه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/102279" target="_blank">📅 20:42 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102277">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qNKI8CDu1H52BOuyiKiDnFDTKYHOpB5wQlC5XyS0r1ZCFIc3di-In_FyqmL-pt8giJghLDTQl98QkhT2CNb9ndxybYGszHLRvvf9SVkd-dMN8lmSlEs6l5aEt54F5SlxTv-J1lK86Y6zBtaydWsoVN9i2NaLcukhiBsWhO4I8lSXpXWapO2NrIXk6WFyVda1cpmSeWNFH5T_ihYArJGChHERMOnVR_Mt83MkIyF0E1EVE1JvVN3Lxu9VBJQGSg4XCCviVWvVCF9wBkvsJ8Xcxuu3d362u06WRMwZk6BJn0h-O1kwE5darkIf25GVWQ1-JNr2DqrykVp61685SPyM7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mEvuHkToqVmRf2QuN3VV23d5jegrongJ3O6UQKTXaJJ66GHORlodhnnmrND5ggZ1BUcV0nwOkpbd9vGT9hR-BwgclA9Y_PDlK7oB4BQuHjM6Cgc5-kYUU4BgeYluKrMZQ9TcG2-OANfu5rNwczrfCHAu16Q7wjSTr-cAJtdp2DNhwpTTQp36SZ9ELMLHyx_IcXooccaaWmDWmk5iZA27h71AztKx_5O_DhP78VZRTaHQUjImOHVyWHXpB_T3VKEee8rP465f2pbjf1LALOKPvaqdW11LbsZ-8J4BsSrzF1GkQDJXEjspPmzgGhrlAuAJklU9Sy4VUNTbbWQcPafQpA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👀
طبق گزارش‌ها، ویکتور گیوکرش، مهاجم آرسنال، ظاهرا سر یک ماجرای ۳۰ هزار دلاری گول خورده؛ گفته میشه به یه مدل اینستاگرامی پول داده بود تا برای دیدنش به لندن بیاد، اما اون به‌جای انگلیس با پول رفته یونان و حتی یه عکس فیک فرستاده تا نشون بده تو راهه. گیوکرش میخواسته این قضیه بی‌سروصدا بمونه، ولی ظاهرا اون مدل برای دوستاش تعریف کرده و ماجرا لو رفته. این اولین بار نیست که زندگی شخصی گیوکرش حاشیه‌ساز میشه؛ قبل‌تر هم شایعاتی درباره ارتباطش با اینفلوئنسر سوفی رین مطرح شده بود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/102277" target="_blank">📅 20:40 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102275">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZqEPJV-_NIoNfMenYud2_Hvgniyq373h8aBmqC4bktZtYWb2g_fvJtirpwD7serN-gpF4qUbWqayQym9wCunTnD85knjM1_NBApJAoajbwB2jeaVEYZFpNi1H9jAyrKHVCaWHJSvetl5Q0CWYLRQVK4oktNc9eiAd47Hz944W_AARoXekwE9G6ByHxDBRNmKOLgqvtXGM5wiVYgbyFaTXBBtsgOW36s0e1AWXfZP1yn5TFzX9OdiPF8ssVYenqXK41Mla9URR1VtJh6yfZUXcPOX00JMV_6y5qyKf0p4LQrRzcXvmmaEL06xPpyeQuacHdRO4PIsgraiLS2snPIakw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cOnG2m38amjIrHR6HZYQ_o2Ep3-DmP27RgefFOdXpYhQpX0R4XcZiyKryCONY_18nHfKgaeUS9x4hMlSpzn9Thtc6rEMTJ8DqBdMztaoLf3yeiXhQhQQ9NStuDvurSrDc6D5I-LgTd6rY381lVmnNAxRR5GaV2SvDc8LCZtTe64dJ9src_BNpaFTQa5aWNeA_FTUZ72K2BdPkYzmAyKG9bde8mgsOl08YnengafWCCVxqd9jGxHCDSDkNsqaTES9fq33QtNqqoh7OwloNwaBy92aHqegfZX0wJCKWqVD5SXIrVesso6GBGu2aCbQrgjJIqr2d2pi5_ukk2vnwl8K_A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎙
پپ گواردیولا درباره لیونل مسی:
من جام‌ها، رکوردها و جوایز زیادی بردم، اما شگفت‌انگیزترین چیزی که تا حالا در زمین فوتبال دیدم، لیونل مسی با توپ زیر پاش بود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/102275" target="_blank">📅 20:20 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102274">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sZUPT47E1JJcmdImmJnPCYK2dfWeiUP1ULsvj0uXKr5S4aWfi30BkkElEUIRJGweqG9vp22fcwH5NGXZBInUyKo79Ty6hgLTe9Dwx1vQFkRJst0eNTnFWDyyNn5CGUAKLrac8FYA1WH1tJoQReXWc23wFkecc-y4aXMarVBItDvRDOUq543PcJRExX1eO4Ox13b7y9Hp898-Wu0WZZrciJ3Y-g6S7Kj-umo8jSOKy72gmLmJ1deJ1M3UVM7lJQV-otsfGJ5TWFevSPbTiBXImnX5thJ3MKMXWoXIGXmrrVohKQRVBFPOGMXgeYYYaI1wgQJyZvmHa7mTQszaVuiaLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇪🇸
🗞
#فوووووری
از رومانو: بارسلونا به طور قطع نظرش راجب فران‌تورس تغییر کرده و هرجور شده میخوان نگهش دارن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/102274" target="_blank">📅 20:11 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102273">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qDWUh_ouVywZLK4kI90Hp1ESD2xsv76d-XLroSBpqVebjP0OoNvwSRmUR5-u5Zgp7Nn3HImKuU4W97oxPeKbSWAuQTTRsFgKXt9-jLKrErx3PbYI_r1T1qMd0h9XvlWEiR4GXRapv6k9GIR6Hpplspku_CRHc3OjgT9Ylf8z__DlZ-v4noOgS4ZiabCBkpPTPts3I7Xin3v8KVeg-sRVvQiGubSHVsZqDFSRDzx_oEJ6Q9L_EoQe3SUIG6cJZoQJQd-kk9BnUH16oZNyraRgdFlUZWW1MTU4ubxa5wlL3Cyesl7h7mlFFm0S8JP4RRFJ2N2qFvbiDFl9botyxLhk5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیوفیس کوکوریا مدافع رئال‌مادرید
😐
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/102273" target="_blank">📅 20:05 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102272">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/84ff90fced.mp4?token=KVwNq6RIuijTkC2uH-oR40RsYuDn-xKYOLas4BKfh-SnnKBoTzK9VhR_xK2BvFj-8Cc8Vn-odckGJlOck_rNQP-m34YRGr4WowJNKtT_ZFpxfYnac7K3GXW5JrkmFmQnCJ-5bqZ-R7MZhjl0zA4VlQhKsQUo8abkQoPqoUYRtw_2fQaQdRa-BcWlNL0AkmLzVHTPBaD8MulZF2Lp7uJvFFKIxZ9yjENWwTaK8Brzgat6tfVV_8LsJC4TFJaMP3FB2yydQ0TqvV41RIT0frmutJSa3mJV9n-JYnYUyeRDesKE1TjGndJSHmVH1_fLNgKFp2gv7YxWOGA_6zScfoPEQ66cHgK2Tzgop8HMFHkIaPuX0tCyZX7rRIzMmAOX7r_q98liiiPXcT-gRRc6g2crQhDZtZ2LkZWSXWs9RoTIV1SmIllMvufQ1Qqp9VdSst769cID2Fd7SbRrfsUKm6R1TAGoo6BXgqqIAojOh-x2Ha2NZd4nXCLFUEvTHVHfgETiCKJNXzwRKWItyi64oxP4qWEbBtVGH2_U5ldtYnGVO6DCp9auHmBcI-FzzAjq-O2vK6VcD4irNHDrdqjzexuHLJiqL5FXzzfFzlNvuwiau99lNrLJa_I6UUX5YCkdh2OYIjN-qUtb6EOuMKoE_zP1JmXvVbTCxUmC9jl249kB5iQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/84ff90fced.mp4?token=KVwNq6RIuijTkC2uH-oR40RsYuDn-xKYOLas4BKfh-SnnKBoTzK9VhR_xK2BvFj-8Cc8Vn-odckGJlOck_rNQP-m34YRGr4WowJNKtT_ZFpxfYnac7K3GXW5JrkmFmQnCJ-5bqZ-R7MZhjl0zA4VlQhKsQUo8abkQoPqoUYRtw_2fQaQdRa-BcWlNL0AkmLzVHTPBaD8MulZF2Lp7uJvFFKIxZ9yjENWwTaK8Brzgat6tfVV_8LsJC4TFJaMP3FB2yydQ0TqvV41RIT0frmutJSa3mJV9n-JYnYUyeRDesKE1TjGndJSHmVH1_fLNgKFp2gv7YxWOGA_6zScfoPEQ66cHgK2Tzgop8HMFHkIaPuX0tCyZX7rRIzMmAOX7r_q98liiiPXcT-gRRc6g2crQhDZtZ2LkZWSXWs9RoTIV1SmIllMvufQ1Qqp9VdSst769cID2Fd7SbRrfsUKm6R1TAGoo6BXgqqIAojOh-x2Ha2NZd4nXCLFUEvTHVHfgETiCKJNXzwRKWItyi64oxP4qWEbBtVGH2_U5ldtYnGVO6DCp9auHmBcI-FzzAjq-O2vK6VcD4irNHDrdqjzexuHLJiqL5FXzzfFzlNvuwiau99lNrLJa_I6UUX5YCkdh2OYIjN-qUtb6EOuMKoE_zP1JmXvVbTCxUmC9jl249kB5iQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
لیونل مسی:
آنتونلا اجازه نمیده داخل خونه با پسرام با توپ بازی کنم. تناقض‌های زندگی همینه دیگه! من از فوتبال پول درمیارم، ولی حتی نمیتونم داخل خونه فوتبال بازی کنم.
👀
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/102272" target="_blank">📅 20:02 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102271">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XCjDiD5Uut7ZMSGfC77Gakbxca_6jRxXBWt8ZMfZv85f3Ci7SSn-uNkwVXr-quSKf9SC9A1_QANWqc4tmjoVl2fMJatZycrbVxVD5cuBzrtlWoIEuK56aH51JD0SCvV8VbvZ7OITzSiOKHeqmNiXxgjq5yAsExWm0oM34I1batvFxLPf2HxwRwCWTxTvqg_DKJmjWP3oRDsT2E-VDy0wJ8XvE5e7FVg0f-T4PNVucLzfbzmmoUrXE0moSb9w65dp3y0eoApBdvqpWCPXAjcpoIKc5SnkiutW_kNJyUsUaoFSdbUH3q8sH0hoBaNewqvTJ67vIjNgUeJGXAJsu324jA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
✔️
⚽️
نگاهی به اسکوربوردها
.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/102271" target="_blank">📅 19:51 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102270">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f57a7d2d3f.mp4?token=CR_HsUwxfUUmJMwscuDJQR0OTPUWKeBMEN7ImyO4YIA-oq90EG6CBIqvUSNPh5mYWzfvFtBw0qWrfHSJkTt_hBmS5Jog8vlxBEoPdZNB7C8AVJTeo6exfqxZ97zFn4uGjqb-ghiIbq13tVDtvK2V6f0yQGCF13GnYmOldYb1j0VMuoxmth1Fh1J_gM88GtW58vdJE7n63xEEMVHiT8A1b4xozuS-x8gpWbEt-Us5PH8VqG5b0VFzo-SUosA41FI6ZSSb3VJ0OpUlq-SRCp3dOfaTi9pqEDBH8E92oAX1plZV3zBro5AhBcHF8VUji5QEoSlwjCHvEkNuk9yMaijn8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f57a7d2d3f.mp4?token=CR_HsUwxfUUmJMwscuDJQR0OTPUWKeBMEN7ImyO4YIA-oq90EG6CBIqvUSNPh5mYWzfvFtBw0qWrfHSJkTt_hBmS5Jog8vlxBEoPdZNB7C8AVJTeo6exfqxZ97zFn4uGjqb-ghiIbq13tVDtvK2V6f0yQGCF13GnYmOldYb1j0VMuoxmth1Fh1J_gM88GtW58vdJE7n63xEEMVHiT8A1b4xozuS-x8gpWbEt-Us5PH8VqG5b0VFzo-SUosA41FI6ZSSb3VJ0OpUlq-SRCp3dOfaTi9pqEDBH8E92oAX1plZV3zBro5AhBcHF8VUji5QEoSlwjCHvEkNuk9yMaijn8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
⚽️
دریبل‌زنی در حالت عدم تعادل (Off-Balance Dribbling) در FC 27
.
این ویژگی آن‌قدر اعصاب‌خردکن خواهد بود که ممکن است وادارتان کند بازی را وسط مسابقه ترک کنید!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/102270" target="_blank">📅 19:48 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102269">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7495121486.mp4?token=KGMWH5dsHLu5QaWG_ZplH-D8jt1GME9YGQSxY2J7iz-xXjAFcOs56pt-HJFV30MS2NfOrYA_smOGQZ_FW9KbiI_M-R_VQU7_QHAVt5vJEYLe7DB1kNF_yDVpH6sphkzZ12zLmj8XcaNRfAOrWJP3Y1EL4gwP6pI70WgSRq-u_Ox0CLVQGHMVCEy4bwpYVmpPwh1YZiDoSQcxTD_Qfzx8ldBdEuqLDSOBFDcp-Q0IejZboJE5noMbAPeEOIR0VX-08AMyQ0LVpZQzhxQvhRrqfND_Oin0NjEVaeSQ5KNX65L68rbCYDJoO90mfUwS6ZYTuxvpVR4gP3Hx6aV4Y7NMoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7495121486.mp4?token=KGMWH5dsHLu5QaWG_ZplH-D8jt1GME9YGQSxY2J7iz-xXjAFcOs56pt-HJFV30MS2NfOrYA_smOGQZ_FW9KbiI_M-R_VQU7_QHAVt5vJEYLe7DB1kNF_yDVpH6sphkzZ12zLmj8XcaNRfAOrWJP3Y1EL4gwP6pI70WgSRq-u_Ox0CLVQGHMVCEy4bwpYVmpPwh1YZiDoSQcxTD_Qfzx8ldBdEuqLDSOBFDcp-Q0IejZboJE5noMbAPeEOIR0VX-08AMyQ0LVpZQzhxQvhRrqfND_Oin0NjEVaeSQ5KNX65L68rbCYDJoO90mfUwS6ZYTuxvpVR4gP3Hx6aV4Y7NMoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
⚽️
کرنر ها در FC 27
!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/102269" target="_blank">📅 19:45 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102268">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/90a87aed54.mp4?token=pieWiksco1TRtJwG9c0awhiUKoCpgXKV6zIVv5qQEc6K6WKr4uYZAugwG415oodJd4dtdGhj3KVdN8vQ53oCDOiwiOiTqmi7YRGlJDs9qyxLRCOKBn2ECc7x1Lks10nu1TLZmN5KVIVGEAv_1sOVQtsM8B5HbRnN7c23L792_BxcB2p_X3ZpYu6PoUXAH6Q_0N-q7pVsdoF54dCmzMkfRvpzU4v-IIepQoUUoLrebBPv9FdPXb7-5dxeSM5rfU-wK_R312nLHUwJhzQoBkAWcEPaxgdmQGX-R8oR1lfOvJLlLHLui2mJ0eXUzUObuXWaNIg8am5mDOXXbz-2hRCXhQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/90a87aed54.mp4?token=pieWiksco1TRtJwG9c0awhiUKoCpgXKV6zIVv5qQEc6K6WKr4uYZAugwG415oodJd4dtdGhj3KVdN8vQ53oCDOiwiOiTqmi7YRGlJDs9qyxLRCOKBn2ECc7x1Lks10nu1TLZmN5KVIVGEAv_1sOVQtsM8B5HbRnN7c23L792_BxcB2p_X3ZpYu6PoUXAH6Q_0N-q7pVsdoF54dCmzMkfRvpzU4v-IIepQoUUoLrebBPv9FdPXb7-5dxeSM5rfU-wK_R312nLHUwJhzQoBkAWcEPaxgdmQGX-R8oR1lfOvJLlLHLui2mJ0eXUzUObuXWaNIg8am5mDOXXbz-2hRCXhQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
⚽️
دفاع دستی در FC 27 دوباره به اوج برگشته است!
✅
‌   رهگیری‌های دستی (Manual Interceptions) بهبود یافته‌اند.
✅
‌   دفاع سایه‌ای دستی (Manual Jockey) بهبود یافته است.
✅
‌ در مقابل، قدرت تکل‌های خودکار (Auto Tackles) کاهش یافته است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/102268" target="_blank">📅 19:41 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102267">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5128380014.mp4?token=C053QzNDgXJBbuIB86EETBx9ceHHhMBP2CgYlTzbkDecvEKtvHPdvDk1Ns5JE7Qb6AvE5ViN8uBiiUETv2iHLgqmK-XnFcWmIqDb3ckAx55FZs1AEkUlWquHGCV2U-5nKrPTqEfneTsCE0y7n2qDP2jpK2_SVEwBT-0pXNYb5n8VVq9izvgzvTJJq_eI1brUR1GhII-Wfth5A61r4ytVNkkUIK2zcJzPAoKxGvIOO5gbrFhjMVKBq3cJcSFibz4uXKfT_DKKET2wzzo3zlo-LbCk79ZBkb3O-efXeQaglF4BmA11o8EU56aipEaDBtHzXI12XUr9AA87sC-FQt6pzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5128380014.mp4?token=C053QzNDgXJBbuIB86EETBx9ceHHhMBP2CgYlTzbkDecvEKtvHPdvDk1Ns5JE7Qb6AvE5ViN8uBiiUETv2iHLgqmK-XnFcWmIqDb3ckAx55FZs1AEkUlWquHGCV2U-5nKrPTqEfneTsCE0y7n2qDP2jpK2_SVEwBT-0pXNYb5n8VVq9izvgzvTJJq_eI1brUR1GhII-Wfth5A61r4ytVNkkUIK2zcJzPAoKxGvIOO5gbrFhjMVKBq3cJcSFibz4uXKfT_DKKET2wzzo3zlo-LbCk79ZBkb3O-efXeQaglF4BmA11o8EU56aipEaDBtHzXI12XUr9AA87sC-FQt6pzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🔥
⚽️
#
فوووووووووری
و
#رسسسسسمی
: تررریلرررر گیم پلی FC 27 منتششششر شدددددد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/102267" target="_blank">📅 19:40 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102266">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a8d0459b3.mp4?token=GmhwEcjL89ffrelrxvvOYYYuir8QfamSfNTy3fzKNzi1MxJvNJpKiawqjxQtqq92RbDOkrwtqVbDc3Qtf_TpZfJpQ-aqJdCeGQNYT1iCsKqs3EgukKI_A6yNqw_JCgzgzvpXKLkq2MO2KBETabAdnAIxYMOkAiUY32Tpoi1gjZnSo_m3fweErj7u_DGHqCIYgAEYY7Ae5SzSImYGG4Q9_EhrF1d3vzQst8Sy0t0vjJo9A9nNrqTOUJ38vymLQ0YHEkiBBVnXnsPHXWGj84Z7zgwxssoSsRhAZlqgRIDINQyzLkgFRNXBzYr237EoOLXavzNkbnfx-dWeEZAeMX_PY4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a8d0459b3.mp4?token=GmhwEcjL89ffrelrxvvOYYYuir8QfamSfNTy3fzKNzi1MxJvNJpKiawqjxQtqq92RbDOkrwtqVbDc3Qtf_TpZfJpQ-aqJdCeGQNYT1iCsKqs3EgukKI_A6yNqw_JCgzgzvpXKLkq2MO2KBETabAdnAIxYMOkAiUY32Tpoi1gjZnSo_m3fweErj7u_DGHqCIYgAEYY7Ae5SzSImYGG4Q9_EhrF1d3vzQst8Sy0t0vjJo9A9nNrqTOUJ38vymLQ0YHEkiBBVnXnsPHXWGj84Z7zgwxssoSsRhAZlqgRIDINQyzLkgFRNXBzYr237EoOLXavzNkbnfx-dWeEZAeMX_PY4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
روایت جالب مجید «قصه‌های مجید»:
وقتی ۱۵ ساله که بودم، تنها از اصفهان به تهران می‌رفتم تا بازی‌های آسیایی تنها تیم دو ستاره فوتبال ایران (استقلال) را ببینم. در ورزشگاه یک سرود می‌خواندیم که آن زمان غیرمجاز بود و البته خیلی کیف می‌داد؛ آهنگ تنگ غروب سیاوش قمیشی…
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/102266" target="_blank">📅 19:20 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102265">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p6n9z8zJBTMLIF0ZwPDa4TkNEGCszzbYihnkWoPKh8hh65BU6a7yPbyOeMBatlXsrZbl2SaUNvTXFZyV7Z6IKDTlgQqQ9TOWTa2T8yirY-eRoFBcksa22nPeSLsZRSzFPHJFlRyTNhvp6tXXCmcClgm8vVhVfNV-l-B9mvwd61X9Pu4LrlJN8Pq9maJToaYHU9JHbaFPkK8riHe273kEC3dHiOWEVrXxOuoQ3NmduwoSCAZppxa3sZIWJopv9lA1pHEkWRwMPx6iETLrNj_Ogx6czG2pNQJTcOXPEUUU_BFeokbs9p9CZzfx4yqbGVRqf1son9r67vtrDNmWd8h7Fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
🟢
تلاش‌های علیرضا دبیر برای حضور نکونام در پیکان هم جواب نداد و ساکت‌الهامی سرمربی این تیم شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/102265" target="_blank">📅 19:18 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102264">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6bcb41b861.mp4?token=OXfgPSrMP5rXUvGi1yQPrnBVfOeBfjJXKWy8vKwk7JbLL96OQcn3UKsfaeUz7pRnhlLxy7HqvPK6vlqsqDR786dFUdfAJDC8-X_ttTLtrAjLfwKl951Be9ojpSn-CLcCwVu3SZwDnVOqmAfK0OSPTUHtlO0qLTOSbZ1KjW3AvExY_9GlAngAvrQqN_FLes2NZhPubINuC7gENuvS-d_QEH720XWcChy820xv0UIUgNqjROE44ExF6CyGUNn0RMxpVr4SJ_skkkAwZiOpt5mjYw_d0S4zBkSZCQLQ7Q_FvkFCGGzW9A6WGapnzopeIiqlnT9hNw3O0nbg5WE6g-Zfjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6bcb41b861.mp4?token=OXfgPSrMP5rXUvGi1yQPrnBVfOeBfjJXKWy8vKwk7JbLL96OQcn3UKsfaeUz7pRnhlLxy7HqvPK6vlqsqDR786dFUdfAJDC8-X_ttTLtrAjLfwKl951Be9ojpSn-CLcCwVu3SZwDnVOqmAfK0OSPTUHtlO0qLTOSbZ1KjW3AvExY_9GlAngAvrQqN_FLes2NZhPubINuC7gENuvS-d_QEH720XWcChy820xv0UIUgNqjROE44ExF6CyGUNn0RMxpVr4SJ_skkkAwZiOpt5mjYw_d0S4zBkSZCQLQ7Q_FvkFCGGzW9A6WGapnzopeIiqlnT9hNw3O0nbg5WE6g-Zfjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
🔻
داستان پسری که دنیا او را به حال خود رها کرد، تراژدی تلخ زندگی ماریو بالوتلی
🔺
ماریو بالوتلی در ۳ سالگی به دلیل مشکلات مالی از خانواده بیولوژیکی‌اش جدا شد و توسط یک خانواده ایتالیایی بزرگ شد. اما کودکی سختی داشت و به خاطر رنگ پوستش در مدرسه مورد تمسخر قرار می‌گرفت؛ حتی مدتی فکر می‌کرد با شستن دست‌هایش می‌تواند رنگ پوستش را تغییر دهد.
🔺
سال‌ها بعد همان کودک تبدیل به ستاره‌ای بزرگ شد و به اینتر میلان رسید. اما وقتی مشهور شد، خانواده بیولوژیکی‌اش دوباره سراغش آمدند و ادعا کردند می‌خواهند رابطه‌شان را شروع کنند.
🔺
بالوتلی با ناراحتی گفت: «وقتی هیچ‌کس نبودم، کجا بودید؟ حالا که معروف شده‌ام، همه یادشان افتاده من پسرشان هستم.» داستان او، روایت پسری است که با طرد شدن و تبعیض جنگید و دردهایش را به انگیزه‌ای برای موفقیت تبدیل کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/102264" target="_blank">📅 19:03 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102259">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q6DQy5fmXN5bKg2pUVNQ_92cSS7OBkQ6xWejxYp_IwfmfpHkWfRhjxfxtstS1eHNID8X6Ir89Do2gC51PVC9Lx7ThXClfy0lGU6NaOW_2FkDpQ9XLrUqFRjf3KjdGwqMMb3NobbK_ESjfAz9WMJlZytHynm0fWcr7R_9rP0YN5_3d2DzyMQ6xBvBRzqBr1Lujmp3r_omxeth934SbbnTj6ttUw-BqWoiNHqS6WMcQIAgeERAPG5E9uZYt1ZSlyqfK2_1Fa7S33hlLMxxLsdGSMBzNE25lHOChoPwZRRNR1Lc2FcHgKlD9vfKnYSbTz2nM2P-xI84b71wRs3DEMjTLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
🔵
می‌دونستید؟
چلسی در سال ۲۰۱۴ با ژوزه مورینیو به جذب لیونل مسی نزدیک شده بود. گفته میشه آبی‌ها آماده پرداخت ۲۵۰ میلیون یورو بودن و حتی با اطرافیان و وکلای مسی مذاکره کردن تا او رو به لیگ برتر بیارن.
اما مسی و خانواده‌اش تصمیم گرفتن در بارسلونا بمونن، چون این باشگاه برای او چیزی فراتر از فوتبال بود. تلاش رومن آبراموویچ هم در نهایت بی‌نتیجه موند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/102259" target="_blank">📅 18:20 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102258">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/18b74b82c7.mp4?token=fIrpkV2vVm_N2Dzbqnvz5oBzVKB1yzBJ3vca1R3WKdgyzCpFE01lT3GffZFJiKanXrTKMPkGTeZQ255X7XKpETFQGw6I6NE_484mWA9xEVfeQwAU0wRMiQ4gMdAlWWcL4x2mPeB-5rpHKgpKWU0DHk77oTzjSZLfesT5o5JnBEgEzVIZTceDuZOWZfqGxLrt_W00hx4ZZypGDzPV_KflVY1AOY5hBMPBc_BvNjYd1uQUqSKBtwXp0gwHQHhEKR9vjLJxhI5rRK7LGt2XhAfsuiiAYtB6Jpesw7RtMCa6t0Dsf8NJU-tZC5XpV_DJINnSuajIw9YogV84K4P4hMW_uT5pZiNSX1J3G-a1tRGRtqI7MRZ71SM_H59rChqk4ykFy_bZp1EVzBL5wxa8emIPpArNOYR0BXdc3WZRZANWl1u7sIiIzuCjKcHQGE4ct5s_5jRWI9z4FDXPZCGt21MrbdclutZfaeJehMzadkkVeqOshTfy4L-1cOoFYEf_NGYJuthbLtC_z-JpS_bRLmQWNYLDbIRNm-EZiwBXQZIUU9SFCuS3AwuSjez1LIX9absk8EdqkJ7MNoSehciiMlPUVCa9U2cQ-KgY6Xl-TiNr3hNhWEQKXLVf9Z0KBJhQTM5nhI8rOB5mGWELivYU2EsViUgMdgu6xqTpsI8S6fjN7WM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/18b74b82c7.mp4?token=fIrpkV2vVm_N2Dzbqnvz5oBzVKB1yzBJ3vca1R3WKdgyzCpFE01lT3GffZFJiKanXrTKMPkGTeZQ255X7XKpETFQGw6I6NE_484mWA9xEVfeQwAU0wRMiQ4gMdAlWWcL4x2mPeB-5rpHKgpKWU0DHk77oTzjSZLfesT5o5JnBEgEzVIZTceDuZOWZfqGxLrt_W00hx4ZZypGDzPV_KflVY1AOY5hBMPBc_BvNjYd1uQUqSKBtwXp0gwHQHhEKR9vjLJxhI5rRK7LGt2XhAfsuiiAYtB6Jpesw7RtMCa6t0Dsf8NJU-tZC5XpV_DJINnSuajIw9YogV84K4P4hMW_uT5pZiNSX1J3G-a1tRGRtqI7MRZ71SM_H59rChqk4ykFy_bZp1EVzBL5wxa8emIPpArNOYR0BXdc3WZRZANWl1u7sIiIzuCjKcHQGE4ct5s_5jRWI9z4FDXPZCGt21MrbdclutZfaeJehMzadkkVeqOshTfy4L-1cOoFYEf_NGYJuthbLtC_z-JpS_bRLmQWNYLDbIRNm-EZiwBXQZIUU9SFCuS3AwuSjez1LIX9absk8EdqkJ7MNoSehciiMlPUVCa9U2cQ-KgY6Xl-TiNr3hNhWEQKXLVf9Z0KBJhQTM5nhI8rOB5mGWELivYU2EsViUgMdgu6xqTpsI8S6fjN7WM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
🔴
۱۰ گل منتخب تاریخ تیم منچستریونایتد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/102258" target="_blank">📅 18:01 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102257">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tiwZUAI9hMiqb5aJjpduBSXXnECpRh6gvZeLzhKqRr4k8Jg9F03_u7U5iEEi4vOjkiGLX3ZflxkijhFQFM5CMBv4AwP0BC75Q4QGOYk7lKcgbT_StmvgHwEdyl2xiNRcY-vYWrFohlcTv1tnlan-n6Loh7tkosA97lfIIvDP8ImLCgDFqIDUOjb8b7ADi0wdLXKR48pQelC-pEyxBPWJ_1MwB5A-5kbWVY9fbn4M68Z_wiyYdpOdtvwc0h_HiusDqZIRsSavVljH9Oms1OQeYtzpK2BY3wzML49RvvBt91Idwv1ZRvJkd-SKEAfXlYbZRDVS3ihIy5gZPVz5w8uujA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
⚫️
#فوووووری
؛ فلوریان پلتنبرگ: کریم آلبگوویچ ستاره تیم بایرلورکوزن با عقد قراردادی به ارزش ۳۳ میلیون یورو راهی یوونتوس شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/102257" target="_blank">📅 17:58 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102256">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZqW4Crx0KkegGja5_FhqRMERguIQWASJU1h3f7yHpM3Afns_FEHpnE754hqedb81PKn0rHxIH7lb6KV5SiRenGD5x_AMGS988nzT8MI7y5mdX9U2wi-1UDjsf3KXWso41ZsPM3SdROKWkhPujlcPvf8fvOQSe8vCq2Bk6uUaHghmi8ZfhnEG1yT4Muzrgq4Zkyd6M9F_tAbydpyHse_sUN1trvGyrwwh5vtvdLSViVK_dZnXWUPTFxUPEDge2Y0gWNPN0NkDl5RiZU-iH62bQ48G3ib0fb7kr15jS1-TQUelPLfc3ve78sVMg9vRmfDuFNopgj7AMIJ_kx0QW4smeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇫🇷
رونمایی‌رسمی از لوگوی جدید فرانسه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/102256" target="_blank">📅 17:39 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102255">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iojdT98bkvWcsWAOs6ZAUmAUBLHbaV3Gk-Vg9d1QtRFiH2wy15OzIlgxJDbHfn3CDwAGaBH86qKd7TOWhqEffEOmUvrugtn46e6MAOE3Ox9S-8OQ7tO5x65gP_-YhCmYktAuHy0XxSxFCSqe3cilqkrRq006KqR67UstlJ7etxjF96XihzYotrORQnASM-Qywy9hIuWS0ov3cLKccfbQqkPHZTKCa-rLOo3ZRqd6lXwimZDVZOIf-j8Fw6m4dELfw98J9gC1DX3K0ngEzhGtMBBrsRBHJ1NMEktIPh4mbbF05nPOQrWcWP7LnDMZPqpIVgHO9xeqvcsJKfuqKpX4-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
⚽️
مارتن زیگلر - تایمز اسپورت
🔻
جیانی اینفانتینو، رئیس فدراسیون بین‌المللی فوتبال (فیفا)، قصد دارد بخشی از حقوق مسابقات جام جهانی را به سرمایه‌گذاران بخش خصوصی بفروشد.
🔻
مذاکرات با سرمایه‌گذاران و چهره‌های نزدیک به دولت رئیس‌جمهور آمریکا، دونالد ترامپ،…</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/102255" target="_blank">📅 17:31 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102254">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f4d715de39.mp4?token=qD6w5pSTrVTgDO5_dnLKLbCiSzb-vBGIpiK2cSbBxOC8ix4DPZRDOLP9csjqYaeY1G1xsDXd-0uXgFZCoUImotXEk0OrOf3vEctCcKF2iuo9klxhS2MxKj0XFno6gVm6EsE47BcJWv6i3wOAhpXro6O_uaB3OVw-ObMFoH-rIxfBMtEwWpgbAtHHljAEGPZT_rnrhY1DdV11GtkubUYo6Q2RCTA2zrhFweWVFYitEi9Na7g_auVHEZJf2V1LF_JRpJj23aQeutTEL_M9zeUWqGK7PFp8_uyL1E7p4NCAxaKwzPlOCYyM0wk4EFDSWEysIeWN9DANNVjr1hoJreaHQhvBwtASySys0VPdZsgzI8asiE2IF59t0Ox8t2zARLwj2xFtyZ2od4ISB6MrhtOTpRhKzVw5auMBnLa2Ba2ibDLWkxelpwvsQKl6t2hJmMvKlPexrYcfIzROmGVKnIDI8F41nnrHzHVigh5HLMwlPmrX3_srI8Yz0hFpuxGfJQVfGkilwbAEULpuUZBUhoqfIF0_CxwtuZ5Kkr-wU9fLG4o_bazkaNMjfiKIKd4pMawfiCbCZJ1gM6dxaVDCHEWwmrLuQN8R2RocXmFYwTc4kTmRa1QoEHVvgkZ5YUasy5NWXXiJYNUyAbZEO8yZqU8PabK_muhY9Rt6BRNoAVtmkPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f4d715de39.mp4?token=qD6w5pSTrVTgDO5_dnLKLbCiSzb-vBGIpiK2cSbBxOC8ix4DPZRDOLP9csjqYaeY1G1xsDXd-0uXgFZCoUImotXEk0OrOf3vEctCcKF2iuo9klxhS2MxKj0XFno6gVm6EsE47BcJWv6i3wOAhpXro6O_uaB3OVw-ObMFoH-rIxfBMtEwWpgbAtHHljAEGPZT_rnrhY1DdV11GtkubUYo6Q2RCTA2zrhFweWVFYitEi9Na7g_auVHEZJf2V1LF_JRpJj23aQeutTEL_M9zeUWqGK7PFp8_uyL1E7p4NCAxaKwzPlOCYyM0wk4EFDSWEysIeWN9DANNVjr1hoJreaHQhvBwtASySys0VPdZsgzI8asiE2IF59t0Ox8t2zARLwj2xFtyZ2od4ISB6MrhtOTpRhKzVw5auMBnLa2Ba2ibDLWkxelpwvsQKl6t2hJmMvKlPexrYcfIzROmGVKnIDI8F41nnrHzHVigh5HLMwlPmrX3_srI8Yz0hFpuxGfJQVfGkilwbAEULpuUZBUhoqfIF0_CxwtuZ5Kkr-wU9fLG4o_bazkaNMjfiKIKd4pMawfiCbCZJ1gM6dxaVDCHEWwmrLuQN8R2RocXmFYwTc4kTmRa1QoEHVvgkZ5YUasy5NWXXiJYNUyAbZEO8yZqU8PabK_muhY9Rt6BRNoAVtmkPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⛔️
تعریف ژیلا صادقی مجری صداوسیما از بازی پژمان در عشق ابدی !
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/102254" target="_blank">📅 17:20 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102253">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hy__tcxapJz3qEzSRx9O1dOX4VrwAtM6qOIcRva_pndkqd_gwykQmZTl8dOsdrisqxpI_TISVw9CsvxuQ6CjQC9-oPdXmrNnvUYa9d1ojuC_7K_6qWiiMmgFH5S6w621PsoXkVqiGB-oTHsgYinORvEOlfh25seRKYrJGxl6egsftV6J-EZkSD401ZrWaFPohAmpZ1Cmq1FowgCslhTrqGtdzbm-6B4F22zatnFwWS4Srm4HDnLaE9zMndrk1KAKwVRT0HiR0i2dIz9dFHdD41EPGdmO628rtqosfnjT7dCcjtXQb13srLGQxSDR9ehURl8wi7oqgFQ0NUjXeTWS5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
#فوووووری
از فلیکس‌دیاز: رئال‌مادرید به احتمال فراوان معامله رودری رو فردا نهایی میکنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/102253" target="_blank">📅 17:10 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102252">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jBJKSE_mI4HN64ea2ypEffC9FwlkHaVfK5nlj-g3u3EmGTFG89uV0SxL_I8LOqW6XgtTkV1ydopjJ535ZmXhCtz8_PRS-b54N5AvRZ39CWdIQQ8MLDCvdmDrufReLS36ZUdlb_o2ofQXZsc0448DcagRr_ViImOUCfjxC6ouKM_sRIIqvl_-BRDJDUFkEUrPdg1ceZEdKVy0cTBFqoT6-5ODTZIg0tX6PdsHQP4msGBtFwAMZeqoU2_rxoF2qDLMTThDMz42vCv6E8gR53wVAukcIADd00Jv3QNkvmonSV4lxFJgy3KtjpOfzVozJ3kYXWp3NTh8KWFP_cF7Uxk8SA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
ساسا تافولیری:
بوعدی با منچستر سیتی به توافق رسیده است و قراردادی تا سال 2031 امضا خواهد کرد.
🏴󠁧󠁢󠁥󠁮󠁧󠁿
✅
🇫🇷
لیل امیدوار است که 100 میلیون یورو از این انتقال به دست آورد، در حالی که منچستر سیتی می‌خواهد این انتقال را با 90 میلیون یورو به پایان برساند.
💰
👀
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/102252" target="_blank">📅 17:05 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102251">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f9EqaS2N8uRMTjRBNvxXqrsE3YGt7YPi8LNrUAFFCcODJzd3qWTeNzgvOmxtR4aQ4sFT5yjI2dzoBAWF6g-iC-hXhx1cvMhcFNfUmGVLcefKfPf5oqpJnEtaSww95QhzfOCmMgEQXdigDdTewvSAR-MX2fG4OcI-UsTU9S4ZdIsuS46tmxWmwqXsWbFXxQmQRbA2mMbeN0L2j18jaHrv9fHLDfAfBl7JjWqEOhGwEdFhJMgO_IeHEDiIBL0swlVnVB_vRgStzN1NUNM0HNlKivG3mpn-y0olhSuBMle6OywNW81EPS4-rp4UNvyQy8yeAAw6vQTxT0kmtec9g9wmQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🗞
رومانو: جردن هندرسون با عقد قراردادی به مدت دو فصل راهی چلسی میشه
HERE WE GO
🔥
🔥
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/102251" target="_blank">📅 17:01 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102250">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4eb71ce498.mp4?token=vact8fXSyVfo9QiKqDB_i2WNnzPEqRPuOxKJpMugOge1FxEZKdrvkfVQX6RH1dJ2P2-O9LteoOXpJYJz-6db5iIr2zIbya_DSohcLol6IcRHI3FANpN5617pzPWhDmZ-JyDXBCjyeJN-bHIB-kEFzh9a8L5HIBD5HQXr_OLT0uHTRkkPs9wiLkxgXrlHeEuj1-vPo3HKb2v5EBZ3St705b3VO54hupgnu19oTWh_v-WwmM992s9q7G2-Vms89QqkExyoId3nM3KaJITQylQ1xwhR_FO7qYfr1W7BUqMG13LvirnSIhHYHl5MXCY5DFCz97vAtG6WI5ULmqEk7hPMpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4eb71ce498.mp4?token=vact8fXSyVfo9QiKqDB_i2WNnzPEqRPuOxKJpMugOge1FxEZKdrvkfVQX6RH1dJ2P2-O9LteoOXpJYJz-6db5iIr2zIbya_DSohcLol6IcRHI3FANpN5617pzPWhDmZ-JyDXBCjyeJN-bHIB-kEFzh9a8L5HIBD5HQXr_OLT0uHTRkkPs9wiLkxgXrlHeEuj1-vPo3HKb2v5EBZ3St705b3VO54hupgnu19oTWh_v-WwmM992s9q7G2-Vms89QqkExyoId3nM3KaJITQylQ1xwhR_FO7qYfr1W7BUqMG13LvirnSIhHYHl5MXCY5DFCz97vAtG6WI5ULmqEk7hPMpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🔥
لامین‌یامال و زیدش در تعطیلات
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/102250" target="_blank">📅 16:40 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102249">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/32ebe18939.mp4?token=TxfSo1m-Ehwswn9-W9noXdZFnH3x_r8pZ6U5Saauh5WknTMPCNdTQ9pTxyUvxUuQxMXJXm4UtIsTWqcqVmEki8h8EsLd36RK2L0vZYEEp96bZSdLM_X_bLQJyv400vIeHeJlvssbmUOZymg3YqMJQzKjbaaAp0cc5a1Cjiw0aqhqk0KlY65n1pP4gx95FP2Ds0nYf1MvDVfCY2pSKNXoNEXwxZ3aAxV6-4VM2QJAU593WQosO_oaPCXP9iK_w8fWvdsXZQBcBwgdpe_E_JdzgGFXuf0XQmHGuLU_xefWnQBCSnOWNo18JfONZeo7BMqqSNuI5M0wMCoNNtdpPJ1VQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/32ebe18939.mp4?token=TxfSo1m-Ehwswn9-W9noXdZFnH3x_r8pZ6U5Saauh5WknTMPCNdTQ9pTxyUvxUuQxMXJXm4UtIsTWqcqVmEki8h8EsLd36RK2L0vZYEEp96bZSdLM_X_bLQJyv400vIeHeJlvssbmUOZymg3YqMJQzKjbaaAp0cc5a1Cjiw0aqhqk0KlY65n1pP4gx95FP2Ds0nYf1MvDVfCY2pSKNXoNEXwxZ3aAxV6-4VM2QJAU593WQosO_oaPCXP9iK_w8fWvdsXZQBcBwgdpe_E_JdzgGFXuf0XQmHGuLU_xefWnQBCSnOWNo18JfONZeo7BMqqSNuI5M0wMCoNNtdpPJ1VQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ترامپ نادان وسط مراسم ختم گراهام آدامس در میاره به بغل دستیاش تعارف میزنه
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/102249" target="_blank">📅 16:20 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102248">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hP_FPD_n-leAZlyqswOzjB730sIwmNOECgwdjVcKYoOtGjvLIvWI6rpMKZR2fQvj86pImvb_bMqUL8oR1QkEibUr0jdHEyA3gb6bdhAUDjHkQIAdFFITqv9jLx42xbWNpPinIENTT_UXoDT93VXuZjuzU2VBmQPQkBoPiTu8aRUYKJ6dsiAv1UIauRSAahiEtQjymqj4rn4HkOC_jbcyr-AS7Du8xIu4xjCcFU2ZZCgBURhMekbrAWUutELCRgmh0Y4Kh3WLB-DvPd-Zhna3Kob1j27sNelu0HNqrBZ524sV_RJTpW1rTkiTP05LRSgpvsfuYBl0q0q_Sc-mEoE5LQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
🔹
رئیس باشگاه الاتحاد فاش کرد که بعد از جدایی لیونل مسی از پاری‌سن‌ژرمن، این باشگاه یک پیشنهاد تاریخی به او داده بود:
ما ۱.۵ میلیارد یورو به مسی پیشنهاد دادیم، اما او این پیشنهاد را رد کرد چون خانواده‌اش می‌خواستند در میامی زندگی کنند.
چیزی که بیشتر از همه ما را غافلگیر کرد این بود که حتی یک لحظه هم برای تصمیمش تردید نکرد. میتوانست خانواده‌اش را راضی کند، اما خانواده‌اش را به پول ترجیح داد. ما کاملا به تصمیمش احترام می‌گذاریم. خانواده همیشه از هر مبلغی مهم‌تر است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/102248" target="_blank">📅 16:04 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102247">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🚨
ترامپ در مورد حمله ایران به اردن: حملات شدیدی به ایران انجام خواهد شد، آنها شکست خواهند خورد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/102247" target="_blank">📅 15:57 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102246">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e2de7978a2.mp4?token=SgitAxnxWIge30PcyIXrQ4k3X5nvRnRCWgZa5ZFBEaD8KVJ4n6I0LqVO6iyP9OdJOua8mX4eVjaEIlmC5EyGg1jL53OJ6-JNHwuv5XBKEHccvc144IHhcIHW_WYgUr90YxgUa86MljHE_XW6OzWxRSaI_K6IJlfKn_Jf6pODmKyvtLaZb0CCBM_gc-FRVjcGSrnwgGgQQUSQVNBiG-wooLWXaOa28Sh6l7oe_rmBFCbnwkJk62GM8r2qQqGfEg4uOlxqG_aCKeMPtmomNzZcxerFP7n221C8frOpD6jHVhZYBeX02a4wkac-cf_nRjkQ91PnBFtV8v4yD4cfjifdOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e2de7978a2.mp4?token=SgitAxnxWIge30PcyIXrQ4k3X5nvRnRCWgZa5ZFBEaD8KVJ4n6I0LqVO6iyP9OdJOua8mX4eVjaEIlmC5EyGg1jL53OJ6-JNHwuv5XBKEHccvc144IHhcIHW_WYgUr90YxgUa86MljHE_XW6OzWxRSaI_K6IJlfKn_Jf6pODmKyvtLaZb0CCBM_gc-FRVjcGSrnwgGgQQUSQVNBiG-wooLWXaOa28Sh6l7oe_rmBFCbnwkJk62GM8r2qQqGfEg4uOlxqG_aCKeMPtmomNzZcxerFP7n221C8frOpD6jHVhZYBeX02a4wkac-cf_nRjkQ91PnBFtV8v4yD4cfjifdOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
✔️
🔥
هادی ساعی در المپیک 2004
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/102246" target="_blank">📅 15:40 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102245">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/33130fd550.mp4?token=lj4piHFQbWPgt3McvzSVO5tYsl0TYKAqxgHtqAApUadQUYk9aVjkkJla489tTS0jTAgL4nvh2K_BHQg_TxPeQRLoNLpdgU5VT3nbgxtOzffwSbn61lQX4ABK_sDomA_AlNE6n9ekfi9Aj-APtftkbvf5A5PNVjBbB5h5lnDUR1NuEjRq7e89Ngi8kAzDHkXkk2kZfXc286DWz0naS7ygp_49GZ4pKHxU64RwLZ7NcQLJC3xvrrfZ7a_vTAxS6CK6ZqduCOMqTHwsZONLguP2V4OHVgqRI-1wr7tiipGC2Jj7o0Kcq2fZfx0xof94lsWrXT8-Z573s7ZkjaV4mFOIcnUHSMaX8wlyJj25GOUCOMACtp_4f4Pm2RORMLvpDf154BbLWxWxU8ockvIKCpr-Q4kLADmRxFlJ5Sg8COf6_0jfiW29OzA_rCErMb5mr3SYxee7gbmFgS2_lDxaN6AR9imiRHzrQP7FdBErFJXbq9Yfmfh5qPPSqG-MMLTSAtlNswA1hvKo0GAHGKeCHmDvbgP-NlB5TtcD0Lob49F3nVnFNWSTO2HWTX86IBoJ1wvHK-MBYda8fivEZA9bc8MB5JC6-A279HlOeHKWg2QzANKoqcWNKr7XWmnZt2Nos-KexW8E5shB1vg-OR6HtXCYRzPaSc-HM_HmtbVg-vzNFkE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/33130fd550.mp4?token=lj4piHFQbWPgt3McvzSVO5tYsl0TYKAqxgHtqAApUadQUYk9aVjkkJla489tTS0jTAgL4nvh2K_BHQg_TxPeQRLoNLpdgU5VT3nbgxtOzffwSbn61lQX4ABK_sDomA_AlNE6n9ekfi9Aj-APtftkbvf5A5PNVjBbB5h5lnDUR1NuEjRq7e89Ngi8kAzDHkXkk2kZfXc286DWz0naS7ygp_49GZ4pKHxU64RwLZ7NcQLJC3xvrrfZ7a_vTAxS6CK6ZqduCOMqTHwsZONLguP2V4OHVgqRI-1wr7tiipGC2Jj7o0Kcq2fZfx0xof94lsWrXT8-Z573s7ZkjaV4mFOIcnUHSMaX8wlyJj25GOUCOMACtp_4f4Pm2RORMLvpDf154BbLWxWxU8ockvIKCpr-Q4kLADmRxFlJ5Sg8COf6_0jfiW29OzA_rCErMb5mr3SYxee7gbmFgS2_lDxaN6AR9imiRHzrQP7FdBErFJXbq9Yfmfh5qPPSqG-MMLTSAtlNswA1hvKo0GAHGKeCHmDvbgP-NlB5TtcD0Lob49F3nVnFNWSTO2HWTX86IBoJ1wvHK-MBYda8fivEZA9bc8MB5JC6-A279HlOeHKWg2QzANKoqcWNKr7XWmnZt2Nos-KexW8E5shB1vg-OR6HtXCYRzPaSc-HM_HmtbVg-vzNFkE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
احترام به هواداران به سبک لبرون جیمز
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/Futball180TV/102245" target="_blank">📅 15:20 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102244">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/34dd03fd29.mp4?token=SuJjQh5DFQ8WW0c0POJ0LRkRnkXehCix6q-IkJyHr3aGl0TWTfXtN4L1a6rpEn1Qn5AsHrx7b47ksmgAnmP8Xu8lYCMU3IJw0oDpyONrJy3gMZCW2gHp8Z1XPCxXurB7MjMoIngsoxXAtFOS_DApQwPVo2wDsS5RgTJT_exPi1G2sgxsWsXoEkgLQokYyczVeU_er1ry8G4_4rwpXydogNk4LSr9KlnbbZzXDrRkGw6W4vZZjxQYQDGfk8lvGqtNjWeNySPfbX2NqxCrLsmd5Vc2R3AsHoNjVJe5RO4aSjyktpm0Lb89cIisOlDOh7RzG2BnwQVfqvwh6Mg-otaOYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/34dd03fd29.mp4?token=SuJjQh5DFQ8WW0c0POJ0LRkRnkXehCix6q-IkJyHr3aGl0TWTfXtN4L1a6rpEn1Qn5AsHrx7b47ksmgAnmP8Xu8lYCMU3IJw0oDpyONrJy3gMZCW2gHp8Z1XPCxXurB7MjMoIngsoxXAtFOS_DApQwPVo2wDsS5RgTJT_exPi1G2sgxsWsXoEkgLQokYyczVeU_er1ry8G4_4rwpXydogNk4LSr9KlnbbZzXDrRkGw6W4vZZjxQYQDGfk8lvGqtNjWeNySPfbX2NqxCrLsmd5Vc2R3AsHoNjVJe5RO4aSjyktpm0Lb89cIisOlDOh7RzG2BnwQVfqvwh6Mg-otaOYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
یادی‌کنیم از تیزر تبلیغاتی با مسابقه رونالدو و‌ بوگاتی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/102244" target="_blank">📅 15:02 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102243">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9a4c493f3d.mp4?token=K_eiA2JNoehxtuhjUhSsuvGuC6wNcwVT94oxq3uRBctY6GWPhqDzXRiJ1y7FmMVvruKFUv_smLPSLfDS5nqXm86uM4dpY7-OFKLrWsvmDea1GLwyFdJ8qrrv83bUUufVRqqrSnxOOdnYH0BNGsiDJ0RcDRbxJYZvpxOZ_usYOicGbrLfwaBceH3FaAetZjLkAk5hRxB7FA_2ymjuG0qtj9_eUOIbkypO1AMWlBnc8vavr77L-OimQ9tQU47X8D6RQ5aQuVjN8wz7M76PYdev_M1j5wcDMnSWSxGWtkguH8jyWGxmGai2NkIPd2w9vEk8fiCBNMOpOf7nflkojXe8xQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9a4c493f3d.mp4?token=K_eiA2JNoehxtuhjUhSsuvGuC6wNcwVT94oxq3uRBctY6GWPhqDzXRiJ1y7FmMVvruKFUv_smLPSLfDS5nqXm86uM4dpY7-OFKLrWsvmDea1GLwyFdJ8qrrv83bUUufVRqqrSnxOOdnYH0BNGsiDJ0RcDRbxJYZvpxOZ_usYOicGbrLfwaBceH3FaAetZjLkAk5hRxB7FA_2ymjuG0qtj9_eUOIbkypO1AMWlBnc8vavr77L-OimQ9tQU47X8D6RQ5aQuVjN8wz7M76PYdev_M1j5wcDMnSWSxGWtkguH8jyWGxmGai2NkIPd2w9vEk8fiCBNMOpOf7nflkojXe8xQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
▶️
یادی‌کنیم از مصاحبه سمی محمود فکری
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/102243" target="_blank">📅 14:40 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102242">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/45ed8d40d9.mp4?token=A0hUrFuG_CStsTLJ236GV_jIGYh5UgAU-ForxmPlm2_-BqOReN8NBh5WX3PI9Lh_gwhDe8nmF27EG2XdrqqFPFGgxT1RAcliTtpDd8Xg8eEWLwx8j1JB6pu86Vi7_9xbhpHOJFwHNQco8-suJBVCYbESA1m3MHZAj0s79F5LrcgvgNaIfvZP35WH0d9s539b6kiD2Yc53cDnv-U97-J-7VIt6DJMH2hAPrt55LUAC0Z9yU9IZEWfzPNGzuCY5MJ9ExI5OBfc8sbQvW81I-Wr2XXIvlqrODu56hTtYKj4QX0zPFO543GkMEJ5xUw0NmtncZAX_ETRk8NelBZjOYFbOzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/45ed8d40d9.mp4?token=A0hUrFuG_CStsTLJ236GV_jIGYh5UgAU-ForxmPlm2_-BqOReN8NBh5WX3PI9Lh_gwhDe8nmF27EG2XdrqqFPFGgxT1RAcliTtpDd8Xg8eEWLwx8j1JB6pu86Vi7_9xbhpHOJFwHNQco8-suJBVCYbESA1m3MHZAj0s79F5LrcgvgNaIfvZP35WH0d9s539b6kiD2Yc53cDnv-U97-J-7VIt6DJMH2hAPrt55LUAC0Z9yU9IZEWfzPNGzuCY5MJ9ExI5OBfc8sbQvW81I-Wr2XXIvlqrODu56hTtYKj4QX0zPFO543GkMEJ5xUw0NmtncZAX_ETRk8NelBZjOYFbOzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
🏴󠁧󠁢󠁥󠁮󠁧󠁿
دوازده‌سال پیش در چنین روزی اوریگی زننده گل تاریخی لیورپول به بارسلونا، به جمع لک‌لک ها پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/102242" target="_blank">📅 14:20 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102241">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e9073a1aea.mp4?token=GCzfeF6M7j5wOEF5-z7KLVV858z1AaYAITphLyhH2JfTY0Dr-SYqKQ_4rwWGE9fr5sWC9Ax1qHQfuLDioS4wHpAbdO7cOHOKXkwsTZTJGgAxNny-42LLZzrQq1l-Yi3p7Z9WAJ682rmspZsWe0e3h_OvrrjriXJAvtmdcSZKwopN9EkzexgEJaDk1ycPP4R4O7wH2hh6QpZeccVd60QiAuZNiU3GrA9_T4GSrHCPn22hVhkvchayK57AaoJayvNILWRoacYzcmgmlIkaQILoWAFG0sy5n3tcO3BGtji0P1KhrwIVOxpDxmzUJS7cp91WbajDrR6Mk3HM3ir1P7Px6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e9073a1aea.mp4?token=GCzfeF6M7j5wOEF5-z7KLVV858z1AaYAITphLyhH2JfTY0Dr-SYqKQ_4rwWGE9fr5sWC9Ax1qHQfuLDioS4wHpAbdO7cOHOKXkwsTZTJGgAxNny-42LLZzrQq1l-Yi3p7Z9WAJ682rmspZsWe0e3h_OvrrjriXJAvtmdcSZKwopN9EkzexgEJaDk1ycPP4R4O7wH2hh6QpZeccVd60QiAuZNiU3GrA9_T4GSrHCPn22hVhkvchayK57AaoJayvNILWRoacYzcmgmlIkaQILoWAFG0sy5n3tcO3BGtji0P1KhrwIVOxpDxmzUJS7cp91WbajDrR6Mk3HM3ir1P7Px6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیو انگیزشی با روایتی‌از زندگی مایکل جردن
💚
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/102241" target="_blank">📅 14:01 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102240">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d5MRX4ddFue0Lz9Q8c90P0QMEqH0UeCS9vZabKRoybQiey50SKH7qdsrlfUpQdQ40qGEFxxz2K-20lC06ekaMs0sb_MvzF5KIeMWO3l2PLbG7IMYtcAnt4YyvNqh6jsRv9b7uBRDfOfWEtd4KXJ4YhZt9pN-beJwxnls9186XCpJfsKpDEXCxKazrUCiHZn_o0QwrelF9fMp0gr33VXoGFcmt9ogY-rnZ4LTRjg-aQeakFkjIAkEkkXQQ1YHUz5Vt62dz7NYSS2KrIITNPY5I7m7mgz3yQR8p6DgBYhRSNXNW_eFNLAP_OIOSWOaqZh3lrGRGlSd_tgpSYuc0x7a8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
🚨
‼️
پاول دورف مدیر تلگرام، به اتهام تسهیل فعالیت‌های تروریستی، از طرف سرویس امنیت روسیه تحت تعقیب بین المللی قرار گرفت!
و اما واکنش اکانت رسمی تلگرام توی توییتر:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/102240" target="_blank">📅 13:55 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102239">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🏴󠁧󠁢󠁷󠁬󠁳󠁿
همراه باشیم با بهترین نسخه گرت‌بیل در رئال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/102239" target="_blank">📅 13:40 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102237">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/O8r-hSCows4CJJFVJAOI-RLwO-iMhCA7VTCd8X-dFvPOOFVLC8HtV_O9bha10DMIWPgfnwhNb9e1UkVmuXNuJz-qV4bJjU_jgsvQ71vDzpYzeLxOEVqM5vQifPoYMQJUs6Aamzf1Rj2YDHGBidqKoqyuNr08gGG-NFshPYi-1DSW-xjgci6KwRRheLWPADUTtFu-w1XLOXRibH-BQQUfAfHLdttk1-ntexdmu6ZQOVFO_qeKpk3ffPgd1QRCA1_ZYd0WS8GXvbkKmGcmLdCLWQ-bk1IQfz15jPm8xdGQmKDokeyRIbkrBHu66PsdQ93PfLv5Elkk5ODfnOO-9UPvvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lkTJCNmq_G4fv6SrI1Ju_hzTrxpKGqqEwnDkRIdFb6-2ysIBQg6Y7dJwcQtp5t3PyHUcW7pZkDt7Pzb20fhgx9oi3jw5NH3R9HKI8dysh6or5IQ3llSgMh5IoV2z0SRGODX8A6y6IXfSHJ3_ftwbPhXY1BAP_vooL6fhYw8UcnQwgZxkH3vvUTWNfGrfjZSLLy9LWHTTriBEmeKl_-5CqG4iK26doSCGlKuieZxLmD5ucOQDDIM_u5jvuvkn7e6DjWMRmqflH0zvuD8sueJNnX8Ss6W68raL-hPjnR7FuW_nidR7Jy1HxyhwiTEG3-eB9WroP3wSgusUUequHeCXDw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">گابریل مارتینلی هم ازدواج کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/102237" target="_blank">📅 13:31 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102236">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BCge2J5DH0yJgHoLRD4evV8eKUpZQlSnaQYNzq0yQLn47Ls8SImSLCLvyjMu9-thDkOQJUXGn-RflXhwI2GQ39K6z3tQxWOrPDKP6cZotayh8MF8UjWOqC7So8EeLVHbJRqztEvcV2gtuPFPrRjfFx9sGegAhD36pCReAkAMrF-TMaHjB62mFPTVttbwAryTaOvapzKkLTBqvJcCBkfCY5PgU6S_MokBe3lZc1oWSwH2yvSpPQrbpzO4B59nch_zZSLX_v1ha0Ylb-hUfffnQC7cmZnwH4XOIr-elpHdyZVEp7PZo0sW6VRL2IdduGOM3WQNdSl8nI3-4BCeorW0Eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
‼️
⚽️
#فوووووری
🔺
اینفانتینو به فدراسیون‌های فوتبال اعلام کرده است که در صورت موافقت آن‌ها با فروش سهام جام جهانی، هر فدراسیون 40 میلیون دلار دریافت خواهد کرد.
🔺
در صورتی که فروش سهام رد شود، هر فدراسیون 10 میلیون دلار دریافت خواهد کرد. یکی از منابع گفت که…</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/102236" target="_blank">📅 13:29 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102235">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S9sdFiRNSSNfASv1mnq2lLKSvMtrRYZnyP9eStW0Oku57t1eiDOaWrO-EvfrOLcPch4rgIkakWz8nuu27YjqrW1dVDQY-hKLSjdPDlwh0xQOjvtXRo84T5hHLg4tYyQ2iYyT622Rz5EWd6wYRgiuR1pPSM6ramJiK7f6xOT3hmZVKrXgq9dU4YqH9MPSThw9QnPI6Q5b6-KBQv3lCz7qEjoFLhBA3c_DrydPXRT1qVcUqmM8DffyNcb-fq92PgPz0C4VxlRI_-xCHmabtOBPKW6jZtaoLBW0-6mlVRCi16-DyDHQ0g1DXdViMD0IIUbIyEg28i6JvRKmswk68_-x_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🗞
موندو: باشگاه تاتنهام انگلیس رویای جذب کونده مدافع بارسلونا رو داره اما کاتالان‌ها فقط با پیشنهاد بالای ۵۰ میلیون یورو امکان فروش این بازیکن رو بررسی می‌کنند!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/102235" target="_blank">📅 13:25 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102234">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JM41qn0yFc7ouNP7Uh8sfXCYtv4cVg65ZKv3zCyI8zUP5vXR09GwG91MROA3EnAzJUQ4Fv-UnEz0IH7TC_d0RKvwl63tfm_nW8xSLB_UB0FqPULy0OBEgUjgbzR7P9gQkWOkMz2hHaMAUfyytabvUZ90IOt-daRiAq2MYeapyG0nHZqKU6AfFxoCrfkAqhXpY0CF4LayBNb1yqNfvt-j81tK-fsGysoMxe4owWqZmrhf_OBwAYv4clUQAwP-h4mOiqTpe5_HTNxftWrtucgDjYFXR1ZCC3BdRnXoCoeJM4WauN9WeSkiUOYscvCxOZRNkxIa3_mZxe-4kjX1MZuAtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🗞
#فوووووری از اسکای اسپورت:
🔺
🇪🇺
یوفا به کشورهای عضو این اتحادیه در اروپا اعلام آماده‌باش کرده که اگر اینفانتینو بخواهد جام‌جهانی را به سرمایه‌گذاران خصوصی بفروشد، از حضور در دوره‌های آتی این‌رقابت‌ها انصراف دهند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/102234" target="_blank">📅 13:19 · 07 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
