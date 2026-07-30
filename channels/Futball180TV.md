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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-08 16:59:30</div>
<hr>

<div class="tg-post" id="msg-102353">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T-o5CHhYbX86xGweWLc5_XPwJLDzWf80wYqf_nDu-2wk9tzdIrdiF2Mb2IUnAfQudD6KaNsH8QQisUkmBhoqKLoLqxPmWD0Rb-Lg0sr9-bNvSQjhFKzLeUL7hmnhUsdunBpp6_l67K9Fd1pY6MOhcuofY5uf9TUkQhXwpwejVHCoKVSqWJ7LKB-DMcmqPfl5JCJQGRxvPZIpU0js7M7xhGO-szB43SEXaqWncOTqadCNr2i1v0blNzHtDY4OCbQNrsHWf19FfKwP4rXfUmM2JmrUrX6NKdaf5uneTOry7OM7NKydOpw6Dm4XTV_XJlSgAj2-1f2UOKG6wBrO4tErKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
🗞
رئال مادرید، پیشنهاد رسمی ۵۱ میلیون پوند برای جذب رودری از منچسترسیتی ارائه کرده است.
❌
🏴󠁧󠁢󠁥󠁮󠁧󠁿
منچسترسیتی قصد فروش او را ندارد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 614 · <a href="https://t.me/Futball180TV/102353" target="_blank">📅 16:58 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102352">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17f25fd06c.mp4?token=q5p3FiAVMmCOzxCiwwP8Z4aTw5ouBR0IXV14IRMcN8h0gaBUfRcosZMteVBs6X50db4CeHJe8gdAbFTLeW3jTkWdXVWMY6KMG4QPxh_1tf3r-JastFqNvvjL0T15UCGGS5LOYXDsxvkZ31eINA_3iTjiMtI7JZAIW-5ATXptS2ZZU3tXLWVW9yZGKz22M4iElZdGs_L7JQgVPAJN9Aedc6-hNpB0khAKsGePIpDX3j_sfOfrqL_CH8NoNrhnnajtZAb1d2DVguEBMqbmLp8MZkZ6Xwm72Mye1js5RAUxv-Y5vz55uU4yJX7iR0oxDrj5t53DrTh7hcnQtVfwNmlQV07ztEMWgYs9LuCW-Uh_bJn_RR7TrGbuUPPQji4Ci-2QvemPrMXBN3b4m_aZjY_n-NTlGhvd_BI3_UIzLUaVpftCcwjBVW_bW4dsbUX1DEKD733autYBxbIi4PUzE-etg7ZDCuXgy3HmQM9QR3ujvt5qs-5j1gMxHRbzTvAgavbuaVEl-Stp1-jq7txPYxERbbVtyiOEgy4ctiKq5HR5GxO5UJPg-sxmAENOAydc0GtDcwMyX-Gs7m7vcaO8dEtABKFLMLvIKBmPBnQl_mShCCssG3o_nkId-JoCYKBq9d76v3LwRvHU2i97eODbl3ea_l-pepMqZ4LafdHLBbKtScc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17f25fd06c.mp4?token=q5p3FiAVMmCOzxCiwwP8Z4aTw5ouBR0IXV14IRMcN8h0gaBUfRcosZMteVBs6X50db4CeHJe8gdAbFTLeW3jTkWdXVWMY6KMG4QPxh_1tf3r-JastFqNvvjL0T15UCGGS5LOYXDsxvkZ31eINA_3iTjiMtI7JZAIW-5ATXptS2ZZU3tXLWVW9yZGKz22M4iElZdGs_L7JQgVPAJN9Aedc6-hNpB0khAKsGePIpDX3j_sfOfrqL_CH8NoNrhnnajtZAb1d2DVguEBMqbmLp8MZkZ6Xwm72Mye1js5RAUxv-Y5vz55uU4yJX7iR0oxDrj5t53DrTh7hcnQtVfwNmlQV07ztEMWgYs9LuCW-Uh_bJn_RR7TrGbuUPPQji4Ci-2QvemPrMXBN3b4m_aZjY_n-NTlGhvd_BI3_UIzLUaVpftCcwjBVW_bW4dsbUX1DEKD733autYBxbIi4PUzE-etg7ZDCuXgy3HmQM9QR3ujvt5qs-5j1gMxHRbzTvAgavbuaVEl-Stp1-jq7txPYxERbbVtyiOEgy4ctiKq5HR5GxO5UJPg-sxmAENOAydc0GtDcwMyX-Gs7m7vcaO8dEtABKFLMLvIKBmPBnQl_mShCCssG3o_nkId-JoCYKBq9d76v3LwRvHU2i97eODbl3ea_l-pepMqZ4LafdHLBbKtScc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
مملکت به شدت عجیب و غریبی داریم
😐
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/Futball180TV/102352" target="_blank">📅 16:39 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102351">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/138f735fee.mp4?token=YVATD0qsXa0hmheDqFYmB1fNlV8VaHW4WkHxXLBiYBO6D7EYnciE8MV56kJdo-Q5QFcf3YbYJBWnh0CxmBJihII8RwFSR1CIYqUdKE5hvbMfboCeSHR4yLXcVCISnk-iLeEcpmx-VxG8SKUnS9vPSCxWIvmqcYvya4IksLx-fjbkymYnyfdA3GiXf9eTPW2V50bqkKT2E29hVhhA3ibpDGx3NYNH86hWV44-ESD3usr0Hgr-rxm8RKEnR6Mv1xxwPNr6R_-Z5OLy1mCGSZh5bjKKSs6CWHR7FlbsR0nyWxwy_ST-RPzJnIZ-MBNVMUFQfVn6dHkLIVUiEi8asA6MoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/138f735fee.mp4?token=YVATD0qsXa0hmheDqFYmB1fNlV8VaHW4WkHxXLBiYBO6D7EYnciE8MV56kJdo-Q5QFcf3YbYJBWnh0CxmBJihII8RwFSR1CIYqUdKE5hvbMfboCeSHR4yLXcVCISnk-iLeEcpmx-VxG8SKUnS9vPSCxWIvmqcYvya4IksLx-fjbkymYnyfdA3GiXf9eTPW2V50bqkKT2E29hVhhA3ibpDGx3NYNH86hWV44-ESD3usr0Hgr-rxm8RKEnR6Mv1xxwPNr6R_-Z5OLy1mCGSZh5bjKKSs6CWHR7FlbsR0nyWxwy_ST-RPzJnIZ-MBNVMUFQfVn6dHkLIVUiEi8asA6MoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🎙
برترین‌های تاریخ از زبان رودری ستاره اسپانیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.21K · <a href="https://t.me/Futball180TV/102351" target="_blank">📅 16:20 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102350">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🇪🇺
🇪🇸
یادی‌کنیم از آخرین قهرمانی بارسلونا در اروپا با مثلث تاریخی کاتالان‌ها در خط‌حمله
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.43K · <a href="https://t.me/Futball180TV/102350" target="_blank">📅 16:00 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102349">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RNkBcnpsFMIWA8M8sxuxU-sDFMIxL8K1pqZx-qj5wSNNIeEVG--aLzvtSbVWk3SFOHjmbF2Sm_KJP8gp0Ed0SNEtMcg3HO54Lgew67ZPfuQG_QrQQtSBu0M2kFrjtzTlY47_sxt6f9XpFQywg7Se7UfdRiFDe53S62OxL7qkg-93KCuPgFOdxVTOxDdFmas2dwpIXSAWSaXSMF09lI8xvO57yUJPyGoaAhz-ktv76xjLwozHpeqJsrIUkI80g2lbqGg_XeBj_J4wnqm0O3IXRafDchrhylvMfE59NtB2867yWC2TtiWipcvL8ARZm_6Gse2NneWymnM34WMWGNAj4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
گونزالو گارسیا به فولام پیوست
۴۰ میلیون یورو
۲ میلیون بند پاداشی
۳۰٪ از فروش بعدی به رئال مادرید میرسد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.47K · <a href="https://t.me/Futball180TV/102349" target="_blank">📅 15:45 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102348">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d88e7b9804.mp4?token=Cdv6_kGuapdAjf9Co-I74z5T5UG_9guMcBmF4Ph9bc7HCMHxtdSr2FotNaKaPuki0IVeWJekTeWKuXI7zD-dTt6toPOXL4qSMD9Z-jbIbZPfvKZUdF9Qa-A6GroW1TIPgxeOzGi0EiK1RTjEjouFTs4-DpMKjNUyA1lc5FBLataS4K2T-tycZ_VFuuggWrnmBOVm-RZHT9nOEZgpZkiLH-8k0HqEkP9NECGHmpK5yKSYJW2SPK_4ogaKDP385SCjWzAphwEwl373qkOYUmamLpxuNYqF7Q_s3LW4yYc1Tpq-XcyG-bEuDPuiq4MG4m1pCHja3s9SvmbXm8FOC-n7AQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d88e7b9804.mp4?token=Cdv6_kGuapdAjf9Co-I74z5T5UG_9guMcBmF4Ph9bc7HCMHxtdSr2FotNaKaPuki0IVeWJekTeWKuXI7zD-dTt6toPOXL4qSMD9Z-jbIbZPfvKZUdF9Qa-A6GroW1TIPgxeOzGi0EiK1RTjEjouFTs4-DpMKjNUyA1lc5FBLataS4K2T-tycZ_VFuuggWrnmBOVm-RZHT9nOEZgpZkiLH-8k0HqEkP9NECGHmpK5yKSYJW2SPK_4ogaKDP385SCjWzAphwEwl373qkOYUmamLpxuNYqF7Q_s3LW4yYc1Tpq-XcyG-bEuDPuiq4MG4m1pCHja3s9SvmbXm8FOC-n7AQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
💥
حالا که بحث تیم‌ملی داغ شده، این تیم‌ملی و بازیکنانش بنظر از همه سر تر بودن :)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.5K · <a href="https://t.me/Futball180TV/102348" target="_blank">📅 15:40 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102347">
<div class="tg-post-header">📌 پیام #94</div>
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
<div class="tg-footer">👁️ 9.36K · <a href="https://t.me/Futball180TV/102347" target="_blank">📅 15:20 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102346">
<div class="tg-post-header">📌 پیام #93</div>
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
<div class="tg-footer">👁️ 9.82K · <a href="https://t.me/Futball180TV/102346" target="_blank">📅 15:04 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102345">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🇪🇸
🔥
۵ گل زیبا در تاریخ باشگاه بارسلونا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/Futball180TV/102345" target="_blank">📅 14:40 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102344">
<div class="tg-post-header">📌 پیام #91</div>
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
<div class="tg-footer">👁️ 12K · <a href="https://t.me/Futball180TV/102344" target="_blank">📅 14:20 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102343">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ufPyxDRehTWkskIZi-vuvgp_uVzAK04wEKPnR2E_L1GsjmXvLly894zm22CLFJkCcIgCjrTaZ-EIF-vaEFi_Y6QWS_QcRFthw7nVc4dYYpaorBIHYDs-7X3jbv7lLpp-o5VPvN98WDcgIlAwnDJHdtDEK6DmzB0LRZxiEjR7QE3MQ9uyxpTWnfYXRz7H5FvzDrhRJbS1FBV3rIebEpGGcQTZL_tuXaQPM0MDprDYV2WW7EM8YEisb8f5gvtnPICc2lTp7tG6O_5mpCk-jLy6eJLPrtIhz9nwTe2plYGlfN5IFLaL8teoPZnyxMBPhhixTSHZ_iERR2UXDNq8TCXDTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
🔹
رسمی؛ نیو راموس مصدوم شد و حدودا یه ماه و نیم از میادین دوره‌.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/Futball180TV/102343" target="_blank">📅 14:16 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102342">
<div class="tg-post-header">📌 پیام #89</div>
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
<div class="tg-footer">👁️ 12K · <a href="https://t.me/Futball180TV/102342" target="_blank">📅 14:00 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102341">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PyKRIwdr2sShXhBdRDTwUtEig1VQ-vzN73ARztTpI7g7Rv3o_nTiMuSF-RTCmnSKqmi88yev-NQ_VtgSTHL15grsrzvqXCsJNmiGbUGFaVOg2CcnRxlDgM5PMUZ80y7ufSblaYBujeV1dfsyF2kYtKIxUZkACI29TpSZPFHjOjKorWKkrf3l55cKUyfcq5tgJaHSJXVYp5nVe9Zo1Xu3BA9z7iGHFAeA2zsTXDY3x24pIzqz2LnV4U5AyfA-zaMC2maJ36gY05LbCutwtw52Kp9b9-gvilNIV7vbFVCfEEkcGIlUPSeLRzir07RlQmqkdQOec6QnAhO4sD2qzhZVGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#فوووووری از کوپه: رئال‌مادرید و فولام بر سر انتقال گونزالو گارسیا به مبلغ ۷۰ میلیون یورو به توافق نهایی دست‌یافتند تا این بازیکن شاگرد آربلوآ شود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/Futball180TV/102341" target="_blank">📅 13:42 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102336">
<div class="tg-post-header">📌 پیام #87</div>
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
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/Futball180TV/102336" target="_blank">📅 13:40 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102335">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/efgdUFLb99sJDYMT-ESXqw4MRH6PDfJeZeYhQ90rQuURg-U9F43XQc3edOvVpH5Euwp-27kgWVjQIe3S2YjASIFcHO7ObR1d_hsGMd2vcpCfz5GlRrSSPpCwldT1AofRZeOVCW80MWVMUAj1G9fBshGG5Ltq1LzZrgdWZovjqb1qF8BqYVI0BO5MjJuw1NMPDHBeLjb2RDi6z4culoxJXXmA-uS2_D0TEK2yxveMYV2008y5OtxyxU_VEly0Mw_9dTfM5p-3-KIN3rvd2TFAETMnXppStjuHVPF8m7gHq8zWQIWczgw5LpT-gYz1x5J0J8HBPGR9pjCjkqIi0Mbehw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
💙
#رسمیییییی
؛ روزبه چشمی قراردادش را برای یک فصل دیگر با استقلال تمدید کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/Futball180TV/102335" target="_blank">📅 13:35 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102334">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pYYg47D9f_gWTOscWY922tkYnOoEiuoqY-ld3mJIUFytfsTx53J3FgAanX8rfKsi5JxcKbZWOZ2bbPkhwC6LpaiKFl-A89davgrdzrY_jFZDT2JTBMJ7YvGvVhEWw9FrbkNIlx8_zOsB0VfrIz7ERv6Qq95dgqWvA6KgVjqaG0cyqGSe68AG-F4tey57EmWcz6AtqRkOJJTGsf1WCClenn3pcUSB7aNuwdlSc0oBIK-HJStdoyuOY5dN2WmI2vL5wVZ4PvbEnqKNs2cqc1VkL46ZN83guhd2Igilsd3TMeIgAstN-w-kGauyaDmrdPPaaN5IDslAAbVozbJffzP9gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇹
⭐
فوری از فابریزیو رومانو:
⚽️
ماکسین لاکرو از کریستال پالاس به چلسی پیوست. 𝙃𝙀𝙍𝙀 𝙒𝙀 𝙂𝙊!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/Futball180TV/102334" target="_blank">📅 13:33 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102331">
<div class="tg-post-header">📌 پیام #84</div>
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
<div class="tg-footer">👁️ 13K · <a href="https://t.me/Futball180TV/102331" target="_blank">📅 13:33 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102330">
<div class="tg-post-header">📌 پیام #83</div>
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
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/Futball180TV/102330" target="_blank">📅 13:16 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102329">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AO9rfLsecNDs1bF2pI9YNg3DjGyWdfodgK4EMJrjZOt1X1AHva2fmVZxfoXonNLxRG5JsgoxpvQ_vZw7twtVr_5LHviAWZiINEh4NlxgJYOM91FtJNnJz0r18Lu0Ho0zI3bZ6q8K5rsXdN1GjfuWfG4nv7lNaI1wwnmFWZYpS-o_kLEwxsWr_PEWXtWjrYZteoElQD5ZwMATGEVaHTs41YpeaQZrs4g1DdL6eAYOYWLYz7mtK2ncdB8v7eS7XZwra27MkoZoKuRAabMOTOr02Om2PLXJpTRgiI05aI7nuOSBLjWWxwZMW6rwXd4uZeaS97xxuHTOcFE_3TKGAaUFrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
‼️
✅
توییت مجتبی پوربخش مجری سابق صداوسیما علیه عادل فردوسی‌پور.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/102329" target="_blank">📅 13:14 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102328">
<div class="tg-post-header">📌 پیام #81</div>
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
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/Futball180TV/102328" target="_blank">📅 13:01 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102327">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qRZodgNJULNP-7Qdfjgzz9-2eiZqO4p6x3H8KIu1xiwOjjBXMobLeqhSh23E6t7sF8zudf4zm1vYgd--raDTA5M4Rhozdn1OatCwIQdkE04KPMDmoUwvttsYHZOU3wNzFQeGpUE3ceK1PzVXv-mCaVpHgsIj1PkkLzFiq8sfqU4uHYIkeent6_S2z8ELLoMF02uNBRPnu7Sq9n7N2oUbnnkxUOjNl3y5fhBuTjKugAt8uV-_SFpMkABvCOrXYXr9SbqnZu4SphXO_TLtIlHlS3hOs8EtfSXVwrFwiYsSfoZ5SM9s6wExgOlF6JNPryJAXn1-s3qxB_ZPHdizcyBHYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✅
🟢
صندوق سرمایه‌گذاری عربستان سعودی ضمن تقدیر از یاسیله پس از کسب دو عنوان قهرمانی متوالی در آسیا برای الاهلی، با جدایی این سرمربی به مقصد نیوکاسل موافقت کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/Futball180TV/102327" target="_blank">📅 12:48 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102326">
<div class="tg-post-header">📌 پیام #79</div>
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
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/102326" target="_blank">📅 12:40 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102325">
<div class="tg-post-header">📌 پیام #78</div>
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
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/102325" target="_blank">📅 12:20 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102324">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xp52jHaL-tItnLiudaspfSI0RLn81FyHidO6YRvxewx9GYdzQpnWrlNck3vRg6PDcFibzL3QXoAtf6IArTY1b4D_TiLCSa5e3BpCVamdowlSWuJlLCQBgQEliaXFyXHeRL4jpT6xxawAV7LUWLEBj5TxDckWWgM-pjQhhoW69GfeP4TL6vCiWFmf7kAIV53QonSLA1XTDaZqAH6-FPotOscL-DyzoYrv0_4m4SfXSEbLJm5_tYAnWsnQskShaJegn1WIgjpC4jeVsAQdjRWSKY1qvCvvPxQ_rlYqOjrbqu_-Mbmwxuqtxvz6_fYZzOcbbsSwY4JbyeP37HC37bKfkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🗞
🏴󠁧󠁢󠁥󠁮󠁧󠁿
ماتیاس‌یاسیله سرمربی الاهلی عربستان در آستانه هدایت نیوکاسل قرار دارد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/Futball180TV/102324" target="_blank">📅 12:08 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102323">
<div class="tg-post-header">📌 پیام #76</div>
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
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/102323" target="_blank">📅 12:03 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102322">
<div class="tg-post-header">📌 پیام #75</div>
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
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/102322" target="_blank">📅 11:40 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102321">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UfUZUV4WD3eypy4er16uF9FukTFMnxT0fODnLF-gcLsxkbegS4ndj0DmzBMHd8jjVGyoGjOqR38gCUDxYtdxUj3Y6PgbwUa811PQIDiOepzuvM-fGRB-4GDv-veDhL-lXU0RsDV1itlRMmXcDOARbRDv0pFFM4g9R3ZPOm0EABs86pEtMesF4MvXxBeHEQFJ_biOW-IIoHTEXB03JwrLNZP64jQXaY2gNjc1N8xt5P07nzIlQ8UEFNY_KVm_AET22ZwxkaojBMX1ag-aLbvYGMYXqOYxF_wCViVWF6npu6oHl0BPSG7IP8um-opdtzX7uc2oQtRJbltx3pRLZ_RVXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
⚽️
رونمایی از کیت اصلی النصر برای فصل بعد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/Futball180TV/102321" target="_blank">📅 11:37 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102320">
<div class="tg-post-header">📌 پیام #73</div>
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
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/102320" target="_blank">📅 11:26 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102319">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UQcDfqLVoH_HwKLZtXFo_8PbAGmFE2TghnHCnJfUCSQdCKzfftaMSGi1CXQmBdUtWtYaZ9UDwnV0-zb0ehrKf7u2c6Jz1GzGP_kaSk9icpBou25fWpXwrV5xv3UudA0ZhlJBOD2Xp6FnoXs6aVaR6qsvUnstp7e7A4zpFtJeSHlDgmXn8r9EPxox0tTMDiAtGZMpJAWfanQL7uU5bkhpgIHfXB2NdedbvOdxQxRb57UEIuA737mpeSaduCZ1VaiGpngWUPIhK4-CbsuIhu1CWSE96rnMlp8MEoqgyo3xScchyucFePRcO86M_KnVYBhB5ajkxp8ql_KCjud9gzwEjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🗞
🏴󠁧󠁢󠁥󠁮󠁧󠁿
ماتیاس‌یاسیله سرمربی الاهلی عربستان در آستانه هدایت نیوکاسل قرار دارد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/102319" target="_blank">📅 11:21 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102318">
<div class="tg-post-header">📌 پیام #71</div>
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
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/102318" target="_blank">📅 11:16 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102317">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🚨
‼️
🗞
🇪🇸
رومانو: رئال‌مادرید و لایپزیگ بر سر انتقال دیومانده به توافق نهایی رسیدن اما دلیل اعلام نشدن خبر اینه که لایپزیگ ابتدا باید بازیکن جایگزین جذب کنه و سپس خبر رسمی اعلام میشه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/102317" target="_blank">📅 11:08 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102316">
<div class="tg-post-header">📌 پیام #69</div>
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
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/102316" target="_blank">📅 11:04 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102315">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LEJWuDtemdI1MmV-arsWxdozGKeT7mLFcGUzvGA_Cfi04wvRd6NB2H2-r5jwcgrVttMFdSzICR2Crxfv6A2ileQ8NU-1lLZsbIRerUV4kDJB7m_UB0JtNrdqTWVCnaqCIF9MCwTDqPM0tFRwnmsIvmlnxGGHR5DIMyx7X0hzVJrZJY6TbjMtHpOUgeN5HWfthkR_YlpcGRWNKr5miSU919CP2NMmU42BaqXO0MgVLbEqovfcYQ92GqvZ1B8aM0DUV_sHbfI1AJ51JX9Am1k9i7BExl4Z3jBK9q2ifEqfmo3pj5ujCDoJYxeS-8TT_7Fqr_nhY7rB7mzCjalCP6ar_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇸🇦
🔵
با اعلام رسمی AFC، مراحل حذفی سه فصل‌آینده لیگ‌نخبگان آسیا به صورت متمرکز در کشور عربستان‌سعودی برگزار میشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/102315" target="_blank">📅 10:42 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102313">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IB8VFnNrszajPacXstSh9A8UjUVhBQMMvodOfpFvsY9cBOhLDWn5ASKGkqIImmd-sixWcYzcaKoZANgKW7EXhMmU8OcsnXRwH8qn_HLZp-f_dk4WtFNGpCZiO6IPqd1ENcvUbKbqGIAmg_GoVeUwmJTxitZY1h_NGHfq4fXLo4P9jVffm6mb1xM_3B1olF6xP18KVs_zH2SAGkDdh7e1n4Xh0H7N7w-3mT3GYLhnuZacoGmgTxRliKeV5srPgHM-3iR7gHAlzNzfaEjTXsQKFUUv5U0lauayWiJgiJFrTbE8j1s70RtW7FrR9yjuXdEFgClSeBTtgHNgsVkvuPd6ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✔️
🏴󠁧󠁢󠁥󠁮󠁧󠁿
ایوب‌بوعدی ستاره جوان و مراکشی باشگاه لیل در آستانه عقد قرارداد با منچسترسیتی قرار داره و بزودی جانشین رودری میشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/102313" target="_blank">📅 10:39 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102312">
<div class="tg-post-header">📌 پیام #66</div>
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
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/102312" target="_blank">📅 10:20 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102311">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZX-t7F1mfiTFNx5cIufMXR5g5DQQbw0J0oDVARzJmaKuoSU4vHBDEUCcy8jxyA4c8h2OkkEqZp1W6TKTusPauRJPkiCV5RJwQwO_ee168Efi8I2uk_3bmXy4_c6ycQcnZfkakiwpBfoOw3gj5_vkRz4MTCC82l84eRxaTdlJc6KmG3R6y7x60rCV3HiM3Pbl2c6Rcp5fZXBBOWV66zLs7TmizSCUonTKeY83BnGYqIJQ7dGIpq9r9626OQOtkU64ggNpSn6fyZJblRSLYBAbGpEm7MS8_6GEMmmED5_DVtc921yICGAvU4b0So6QePnw6WXjOa4-mp4LizWLBM2dCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🙂
تمام‌نیازمندی پسران فوتبالی سرزمینم :)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/102311" target="_blank">📅 10:02 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102310">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gY18BWVibkRFkbMHplkbnpKPAbNP4RnKIOPFK66vDlYUXoEpWUM80y2U5oyJ-ssMxjlEucI1E7rDsbwgtuqke5Ovr32uXiYVqufUVRxHX4L5T3I0mVGD035o5lOi6m4lW6PlswKPPP8T_ZgTsd65qsd8KqQEwcgYOr-90VTUFGumJ9aBEozbHpiduMAgQFf07KK4U66cG8QXp03yt4FDnzRmQGmvHUseK_QA-sGuUCV0CkjZStHJLkP8CEeFF2JCAQpH22L3wrniqhv_QFmaDU38hNbG6xbaQ9L9Fnz_IndDQwb4FtbCtrXGHyUrxCCSqcVgDYf7fG8EVv6TcgdOzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇹
🔵
فابریزیو رومانو:
پاریسن ژرمن و موناکو برای انتقال مگنس آکلیوش پیشرفت زیادی داشتن و معامله در قسنت نهایی خودش قرار داره.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/102310" target="_blank">📅 09:35 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102309">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kf5sSrQpzFjq6s7rJJegEMwBk7UEIFxeCSWjFHV1fDh6bzF0YGmSeTORcQtqWsKgZ8ZywzW0kdKJG_nB6jLnr1cckMnQ1ZZBTdHBmdWLxYg0pM21D_sT7w86mUs04yvMeeLFH-IRDheHDf7HwcwPpS6wzWeFbmsbKppoEwMFbCY1-yASdcP9UGOo7lLQFHIaIBqYGVMznIS_F30V78gMmwj4wRtiH3hG6rZDHEgq832PStL6MLpRrPDN6iWXYjQDlD9pGP9dSePGjxC9v9nFpu3xHEYTXeGrJ2LMyOqF_5oJkSNKVBeLGMwOSxiO2zpmAijjkqGh66FVLPdP3QKJng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😳
بلینگهام برا زیدش تو تعطیلات عجب پایی میخوره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/102309" target="_blank">📅 09:20 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102308">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tl1aXHvTWqQoecVsnLSjxuFBn2JHvAVubUcWpRL8sIYy-2fLxw3rQwuNO0mX1ni9TpptFYs3nfq8vtrTOjAacWAuDe6OCoeU3Vp_kelfsfGqHRDaZLrUDHPTJ41ZFiK9J2SJGx_pRRyWi0T4pzpWqOjD-M6zbvToPcY8cA6BuV4S3Oa23dCIrC748N2x2392cHm-A7yExHxyuiNlTJzWSketWLelZgHu8udvUgnxxXkoDfEocXmdzQRgB7NsI4r26uagqmuWot9Cu7wUgmtzhlN1yaxc-XOYHFXHdT7Htv-Ut3qIkmsnt9tpe3mAMytUstNucHnUXbzjm9s71Do8hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❗️
عکس پروفایل فرمین لوپز، در حالی که تمام هم‌تیمی‌هایش در تیم ملی اسپانیا عکس‌هایی با جام جهانی دارند.
😭
🇪🇸
لوپز در بازی آخر بارسلونا قبل از مسابقات جام‌جهانی، دچار آسیب‌دیدگی در پا شد، که عملاً شانس او را برای حضور در جام جهانی از بین برد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/102308" target="_blank">📅 09:00 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102307">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/31f0971b6a.mp4?token=VjZ6NR1Af3b97GzeCK6x2v7_y1sniMynCeDB7kclXiCgURvjwswJC4ZKVQQegyslBTj--hyFVqF8GebuGR5BXczD7ZeSWQYJ_uLDy8gvRYbDEsn_ldZR0xYz5VvFsivWTct1eZZH4LW14DBAEumk7NIBLlVGBuTBaxA-oKczgrIkZrthIPTO7Rw-X77njmGWtTK8g5xipez_-Rr1wgRF9ZRlIfOSu0_TK_8t2LFokyqxSVdVWxKx-qlIwlSx_yJpeP0AAao_OgkchWMTCGe4TwG8PahUmo8ewdKSeH0VeRlm1ZctSWi-9i97H41QH3I5XtgRK2u_QD3931CbqEqw1A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/31f0971b6a.mp4?token=VjZ6NR1Af3b97GzeCK6x2v7_y1sniMynCeDB7kclXiCgURvjwswJC4ZKVQQegyslBTj--hyFVqF8GebuGR5BXczD7ZeSWQYJ_uLDy8gvRYbDEsn_ldZR0xYz5VvFsivWTct1eZZH4LW14DBAEumk7NIBLlVGBuTBaxA-oKczgrIkZrthIPTO7Rw-X77njmGWtTK8g5xipez_-Rr1wgRF9ZRlIfOSu0_TK_8t2LFokyqxSVdVWxKx-qlIwlSx_yJpeP0AAao_OgkchWMTCGe4TwG8PahUmo8ewdKSeH0VeRlm1ZctSWi-9i97H41QH3I5XtgRK2u_QD3931CbqEqw1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ویدیوی سنتکام از حملات بامداد به ایران
.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/102307" target="_blank">📅 08:18 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102306">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">‼️
👀
اسطوره‌علی‌دایی امروز رفته بود مراسم ختم اکبر عبدی که مردم این‌شکلی ولش نمیدادن و دنبال سلفی گرفتن بودن!!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/Futball180TV/102306" target="_blank">📅 02:34 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102305">
<div class="tg-post-header">📌 پیام #59</div>
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
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/Futball180TV/102305" target="_blank">📅 02:17 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102304">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X7Ci0H5CSDKe19Oym76Al9nSEOoAmSdK6A-8bG3sLTqAIMF_2jEsJ8cHpBnaitUQPEOqcNRUOoc_4i8IPiFbiT_CfNZkx6TLBuQ2TXRJeSiYnqiuP58frmzG39L7YYiNhfO5QBNwxOd-6AGMMU6GIZ2KSqnHD6B_fPkLZW898PDhOgNkyOz-j-z31qJqB3HOkbQaeygNn8XoXeypPbSVTj2YDmEWIhdmws3VMFpgdWQrabX2oy8xK0wxorYcDHf75bcXCnPvLx6_UQorg44PsubdYlJMEoMQd_lCTPhEkuZIHdQOB_aVf7E-KD9NJn_5EH-4bC4BM7rnp8dIF7KisA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇺🇸
🇮🇷
وال استریت ژورنال گزارش می‌دهد که دریاسالار برد کوپر، فرمانده سنتکام، طرح‌هایی را برای یک کمپین هوایی ۱۰ تا ۱۴ روزه با هدف قرار دادن زرادخانه موشکی ایران به ترامپ ارائه کرده است. ترامپ هنوز تصمیم نگرفته است که آیا مجوز عملیات کامل را صادر کند یا حمله محدودتری را انتخاب کند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/Futball180TV/102304" target="_blank">📅 02:14 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102303">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6afbb43876.mp4?token=vr3bwRc7pr8eFyda_3gtk40QUW_zlOMCMpMC7k35xQI1CYKEDGawNJtP6g5HQBxu5CX7E341XH2IL9zXQghXiXTAWUhA8WWOEpLBLs2MvmWsjfQuOvsgsswZztI-IWq-KJesAmBgnoNc8ws8EHgWgi_JIF0vxKXDsQOpk-cOtrxhG62MXmw36qXB-A7zZwfKV74IPlojHt5qWYuaMsLoqA1m3WuwLzTyFJYwJuZiQiJ2MatRb7QUXeqTVyS1R31ieMEkz0NaV_JrpVE9RKDa6iVQ-G7UAnNpTshLriSbr0mP9vNBs7zMclECFhn2Ltnt1G6h1JzwYHMH7Zq-R34owg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6afbb43876.mp4?token=vr3bwRc7pr8eFyda_3gtk40QUW_zlOMCMpMC7k35xQI1CYKEDGawNJtP6g5HQBxu5CX7E341XH2IL9zXQghXiXTAWUhA8WWOEpLBLs2MvmWsjfQuOvsgsswZztI-IWq-KJesAmBgnoNc8ws8EHgWgi_JIF0vxKXDsQOpk-cOtrxhG62MXmw36qXB-A7zZwfKV74IPlojHt5qWYuaMsLoqA1m3WuwLzTyFJYwJuZiQiJ2MatRb7QUXeqTVyS1R31ieMEkz0NaV_JrpVE9RKDa6iVQ-G7UAnNpTshLriSbr0mP9vNBs7zMclECFhn2Ltnt1G6h1JzwYHMH7Zq-R34owg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
⚠️
عصبانیت شدید آزیتا حاجیان خطاب به مردم در حاشیه مراسم ختم اکبر عبدی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/Futball180TV/102303" target="_blank">📅 01:55 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102302">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kIK0t6jW3W_MFNzwa602Fj8JRpdziqDQ2xCIPXNzyJN7LU_Ey91kAHxdR3F8sdSoic1sJymGLPiAbx5p5LtmtdOdjPHmK5eI5IdVRww9o7YVYq1sVCXMDFUJQN-T6e6W3TOmkIM3Eq4Ramh5ooF02bRtP5TuCscpffY9eKizFD0FG0kLphYNuZGpqBvdXLISu2sXHAwMTf7boDk9X6V_sWCvkQemChtWtTSKzEWN40O5WguJMIhwErXq4rxLP8CWMVOyxHvcV9UBtUgXL97-H9T0DKdcHDON_WXZr8zKYfhgQvcSf6J9NZFupPpx0n48n4ZJcSqY9Rx3K9J6A9kaTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
🟣
بازگشت لیونل‌مسی به تمرینات اینترمیامی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/Futball180TV/102302" target="_blank">📅 01:33 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102301">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a4e2122bef.mp4?token=ukx8VS9GOt3xb1TV1rz0lj-EgTRzrw8JYe-aCO6xGzYzGuywCJ6zYeUZcApZhHROyU0uzDrIPSQdAko3y-6WNrCBVBzYfvNNGMLo8nXevflXixDc3dMdpoQUIp4olOlL0OIjsaoc42s514j5M3eWvsOtlHbw9ZaDj6JQPvU513S4ureazb1lATha9ppRBL4sR1XLQRkOohfomQrpSZjd3efy_4jcne4Oi_WxWrxCDYvnwELWhXddBE6puDDBbrlQjkwb-5rYlWzU6KUYXs2ohyVUcxqZN1MFLeFip1VFFNLM50t880VNAhSGw6N2KGIQtdkSVrJ1Xtd3QMwitv3n7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a4e2122bef.mp4?token=ukx8VS9GOt3xb1TV1rz0lj-EgTRzrw8JYe-aCO6xGzYzGuywCJ6zYeUZcApZhHROyU0uzDrIPSQdAko3y-6WNrCBVBzYfvNNGMLo8nXevflXixDc3dMdpoQUIp4olOlL0OIjsaoc42s514j5M3eWvsOtlHbw9ZaDj6JQPvU513S4ureazb1lATha9ppRBL4sR1XLQRkOohfomQrpSZjd3efy_4jcne4Oi_WxWrxCDYvnwELWhXddBE6puDDBbrlQjkwb-5rYlWzU6KUYXs2ohyVUcxqZN1MFLeFip1VFFNLM50t880VNAhSGw6N2KGIQtdkSVrJ1Xtd3QMwitv3n7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🟡
افشاگری مدیرعامل کارخانه فولاد مبارکه: دشمن با بیش از ۵۰ موشک مارا هدف قرار دارد و بزرگترین دستاوردش در جنگ همین بود!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/Futball180TV/102301" target="_blank">📅 01:23 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102300">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IU2PDdhiSQZbEZLg76BffyiE70Nn9AG7RqNDSxQIsGbrE0F-XNi77WyRb1ofAqYELkOqLnSTC3kmIsJp5OEUUCN5wc5NsOOTHQktXfriD0W-KSS_liFMW43_9RlbdjieXJhqhW9Z601uu_FFdgJ7ma2J6n6PGL-HTEDLJqLQdRwWK4jjT9CQIbwt5in4pfnXw5iV3B3H7LQZlMJDptA_af4deG9BxnJ1et6cFTlS-YE_p0o8BaAGoTOnrbLNagBZ5VDND3BZTRatyJeBy_J8srNGODlPpRyQNrdm89LBFdpjQr_yUSerBADMaYiLkqkpMxo_Hf4Mr0cxPa2uzbxJnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📱
📰
به دستور ایلان‌ماسک، صفحه خبرگزاری تسنیم در اپلیکیشن ایکس(توییتر) مسدود شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/Futball180TV/102300" target="_blank">📅 00:58 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102299">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/07fe21feda.mp4?token=NAO9XDgka1mZFOhm_aaxQhlj8JdFetXmOyWbugApozpx3In-vgOxPRr90GlKSOEzaP_up-f5AcTuEgRiLPtbsJYPb75tEz5w7hjb6P-zdgTousNGhKOTiEYjdPRbZ4PL-N7OfDNuDKYMlJHOSPMtlNS10rNgZUea3UYMXyZxicV_1fkLxumeR40bvBQCK5EmbzEXc2bwnd10ygDg1_OWe0nvsP7IaARaYO3y2xpFYncVR0FZjIwar246nq6-4OS75LgCCjbsyTskE9W7JLgNdVJLmk4yk5_f3LVc2xOkSoG_vqdrIKJCfGrZXs7BZatj6nFOjW5KbbwThlhrgkQrjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/07fe21feda.mp4?token=NAO9XDgka1mZFOhm_aaxQhlj8JdFetXmOyWbugApozpx3In-vgOxPRr90GlKSOEzaP_up-f5AcTuEgRiLPtbsJYPb75tEz5w7hjb6P-zdgTousNGhKOTiEYjdPRbZ4PL-N7OfDNuDKYMlJHOSPMtlNS10rNgZUea3UYMXyZxicV_1fkLxumeR40bvBQCK5EmbzEXc2bwnd10ygDg1_OWe0nvsP7IaARaYO3y2xpFYncVR0FZjIwar246nq6-4OS75LgCCjbsyTskE9W7JLgNdVJLmk4yk5_f3LVc2xOkSoG_vqdrIKJCfGrZXs7BZatj6nFOjW5KbbwThlhrgkQrjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❤️
پلن آخر بارسا استفاده از ترشتگن تو خط حمله
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/Futball180TV/102299" target="_blank">📅 00:55 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102298">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XTK-pJL8MpHbIab6d_l53Fa-J4zOCYuNnxZAZQmO_CtrEhO9rqxi-FilRc0ipsHnKwdcZDlhOz5SwxQcyuv6rcmayS2VJw2uzaZQbYG0hI9_s-eDC6B03XNZ6wRozOBa0vhT_hRE9vVU7U7mUSD6h40Uy9htwuExzaviiz9CrEv7-dnqNf1DXK4fFbaeaR1kNBJuilW1qbY-hj0QArIqH2W93s9dewRmJFSpNMZIRs2d3zxwyxICMsvTMUX-b9O6xMpKvzoieEOQqkUQaaBJMxJQmIKOVZCCaIIG5JTR3lKYBQ4TUqcb_M4CqRZB654eZ6m0VDKYmOzszkTWfIretw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/Futball180TV/102298" target="_blank">📅 00:46 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102297">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Np4vRSQAcPfB1nSHRgtWYluqSb9Df1Gsyjq1FlI5jwrxwzuZF87FgWYgbuRyQjLB8IGeLApLI95jPuSYYYobqtcveU7mU_on2_LxZ9e0TLtVlPw_XpXUvJM1fdlaaL4XTvDrHN6g_aATPPgtP1HX2do4VUL9ibmtGryXGb-uG17DToCqbWNx46kMJ3mND0ygyo_9wjXIi4qs074fDAcjDIsxm81arMGEeXKMuePI6t2OW7QXgLeQADn2P9VLlsrIKHObXw7TAB-K7mkn1C4Z2F062Jq1g6cKdr4Szb9WWo8C2PBv6zDzFKsZjzYIEikNeyreV0m8FR6YQOqNKFRoTQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/Futball180TV/102297" target="_blank">📅 00:37 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102296">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a93d51cbc.mp4?token=EmUUhD4w84y-XVe2StsyqkKtNyiYS08auske9sA7yW3MmoLEv6cg5EzNusQGtaiqbJGiNuvMlARg98OdRudZ2yR3A56uKO1yQRS6Yd9Y_jelTXQPbq_ZS8hYkyYklEBx-RP3_XTUA0njhqFh76jddZf0QZSTuiQ7Ps-PHyIUNiOkD-muQBUPR_aOx0xUN3_wy4R0utNgKzEZ-GmuXfIzztQCtKIrdYSYgEhIhi_vUW9QU6rkhCv22vQrV-eXq839whyCzMZGV_x4O5OzqlF67C9TLKr5NmerfZ4989rf2GTsMVBOicUBZYcg4QpJDr_YESIcwWHYf4yNXXAby4c5eIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a93d51cbc.mp4?token=EmUUhD4w84y-XVe2StsyqkKtNyiYS08auske9sA7yW3MmoLEv6cg5EzNusQGtaiqbJGiNuvMlARg98OdRudZ2yR3A56uKO1yQRS6Yd9Y_jelTXQPbq_ZS8hYkyYklEBx-RP3_XTUA0njhqFh76jddZf0QZSTuiQ7Ps-PHyIUNiOkD-muQBUPR_aOx0xUN3_wy4R0utNgKzEZ-GmuXfIzztQCtKIrdYSYgEhIhi_vUW9QU6rkhCv22vQrV-eXq839whyCzMZGV_x4O5OzqlF67C9TLKr5NmerfZ4989rf2GTsMVBOicUBZYcg4QpJDr_YESIcwWHYf4yNXXAby4c5eIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پشمای اورانگوتان از بدن کوارشما ریخته
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/Futball180TV/102296" target="_blank">📅 00:32 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102295">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd4b353d1e.mp4?token=bznoPNHYhpPzyFY1JyDgEhcywK1EO6AZQHDMFJRbnp4q_BlGz7kwJBfMoJv1-pqKzROqCZspgb8bXmD-9ijGI09XGf_9nJ7NcG8UHyrIhDnGeLd-NjdW3nAx6svnFQYYtKCNpiemu9trPJmZiaw91LK3CxTbiv_iKKeMdpA9uP0YTXK4aC6eZgyXkcxYLEWqEkEyA2Vquwfdrit2Wx4qtgyYNmyDZNxhlDEuUt8U-xidUjGAEScU29E56zGyS42y-zBK3LNX4zhBxdA9o9w99ZVEio9WvWbGj5Fh4BWGsPc01gk_m8ifhyoLFXdnzK6_g_wcJ2NSFaSXRRytp_Idzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd4b353d1e.mp4?token=bznoPNHYhpPzyFY1JyDgEhcywK1EO6AZQHDMFJRbnp4q_BlGz7kwJBfMoJv1-pqKzROqCZspgb8bXmD-9ijGI09XGf_9nJ7NcG8UHyrIhDnGeLd-NjdW3nAx6svnFQYYtKCNpiemu9trPJmZiaw91LK3CxTbiv_iKKeMdpA9uP0YTXK4aC6eZgyXkcxYLEWqEkEyA2Vquwfdrit2Wx4qtgyYNmyDZNxhlDEuUt8U-xidUjGAEScU29E56zGyS42y-zBK3LNX4zhBxdA9o9w99ZVEio9WvWbGj5Fh4BWGsPc01gk_m8ifhyoLFXdnzK6_g_wcJ2NSFaSXRRytp_Idzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یامال تو تیک تاک : دوست دخترم خوشگل ترین دختر دنیا با من آماده میشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/Futball180TV/102295" target="_blank">📅 00:16 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102294">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🔴
چالش ۳۰ روزه: از صفر تا سود مستمر با فوتبال!  ما یک چالش ۳۰ روزه رو شروع کردیم که توش با تحلیل‌های روزانه و مدیریت ریسک، موجودی حسابمون رو چند برابر کنیم. تمام تحلیل‌ها و فرم‌ها کاملاً رایگان در کانال قرار می‌گیره تا خودت روند سوددهی رو ببینی.
➕
پیش‌بینی…</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/102294" target="_blank">📅 00:16 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102293">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/316f36114d.mp4?token=iC1_FRY8HvWRt7G3nxe7ml0_wyuwZ3G4UpMJFTWH9wIP_FZBHVopsVrb_eSwJI-Yz0GKyEyJCXo6_0J-U5qsrsTjl9GR-8kG6xMRkhVQVl7kAyqPemieaguVUlRlPNCRXHMYf2vGlawA2ClRM-Sdm0pDAbLUe_6wif9H6LDmbkvcg23m0vzXHaHpa25z1Ka1Eg-zc3ZDKjin4ZvUNEkuMhu4SRsk3bnECcC8HvH5E7Mf5ISsWqwFVu07LJ4jCjnIlRQflpGDmUHEd__034KpBesN6NWJrcf8yMbPx1z2Ce87J2YE8MO1Wz9Ju0FgzHyZn3XlF6KzmhvOE69XFx_iqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/316f36114d.mp4?token=iC1_FRY8HvWRt7G3nxe7ml0_wyuwZ3G4UpMJFTWH9wIP_FZBHVopsVrb_eSwJI-Yz0GKyEyJCXo6_0J-U5qsrsTjl9GR-8kG6xMRkhVQVl7kAyqPemieaguVUlRlPNCRXHMYf2vGlawA2ClRM-Sdm0pDAbLUe_6wif9H6LDmbkvcg23m0vzXHaHpa25z1Ka1Eg-zc3ZDKjin4ZvUNEkuMhu4SRsk3bnECcC8HvH5E7Mf5ISsWqwFVu07LJ4jCjnIlRQflpGDmUHEd__034KpBesN6NWJrcf8yMbPx1z2Ce87J2YE8MO1Wz9Ju0FgzHyZn3XlF6KzmhvOE69XFx_iqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/Futball180TV/102293" target="_blank">📅 00:16 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102292">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/opzSZfpB66Mh3KEGAs_qQ93bMTdbkIapfcLBAyuuH0bzLVW_y9uXruR_0wAyV8Mpoujw4QRmmOWD1ZdlfjYeDthIK-OB_Cbo-ocEG7Kk7p9LG81o3MaBDOHKKVV82eB6RPaSB7jdS_gOIp5mClx_FfhXnsK2ByPMffB_M10C9C04245uVkN93ibJO2ENtRjYV4BV_YuYk3v-_qunSnTmhdXP_0jHz67FgbP0WlsN1a8DfFjoWmHqiAUs_moemDRrEhP7uI7TI_IX1ZwJCRoiIxkGFcyjVzxbWjMYV9Km1SSbWNdYTJf1gFuPICqlNkhqeaVMzSi_m_AiHpHI8p4OBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚪️
فوووووری از پپه آلوارز: مارک بلینگهام (پدر جود بلینگهام) در پایان فصل گذشته با باشگاه رئال مادرید در مورد جدایی پسرش صحبت کرد او دلیل این صحبت رو اختلاف نظر در مسائل ورزشی اعلام کرده بود.
باشگاه اعلام کرده است که جدایی او امکان‌پذیر نیست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/Futball180TV/102292" target="_blank">📅 00:13 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102291">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hvLQEFhz_nr90HdsVEm3v6MSS-kARlHq6OU3IUjtnEpsSpySeB05D-RKSd3ltx7iPXAmfjguDL9SEBzufEXo5nwaU80Q0636176IvzNGk1u1AIDYk0ejivhTp0SFElOQWW2v-QpiD_Ai8yLqX7GI87RCZmKMGjPq4DZlNNOQvMxQ0jwe5OtEsBhO8yloFxf9BmHud3agAMXUw1SnXAnmfwCEiI0kkLeg8_fOOQBdEhvVnU2pNnNafC8ypJS9784f94uwixufw6k7FKMpWmqDTDouiZuwIrPpxKCFxMSx0NjXWIgZMZwRHvMV_AH-1bLjxW7A6xgOhMwnNgFS0jTzqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
🇮🇹
فوری از شبکه DAZN ایتالیا:
استراماچونی از ایران برای هدایت تیم ملی این کشور تا پایان جام جهانی ۲۰۳۰ پیشنهاد رسمی دریافت کرد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/Futball180TV/102291" target="_blank">📅 23:40 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102290">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UxJJIw4zpWQRLYDEXQlFeX1wwLsJogGvEoa3ko4xzZyN7wOE1wXPEIVdm0NEmjq4VK91TIrIdw-XTLDsM9L4NaHiGBBCpjmGZ9i_9q9os-eplhkgsd0p3VEWlbKPgClntMw6KyGpe3G0_dpTZisFj-XIVsl_OYKG20BCUPs8RfIqXCcJtp29Xr4f_IsatX5BUNaOskPD5fqnTpcBJeN9LvTjFw-GKriVH0n1RbwNEZ7Uc9Uf1aQQQ_6hkGg54jmQUXXsSi0skeJXJoJv2GF5tJpRmdpKMQB7IEMKrBlHf-tl7CMxQWnEikMAPUbR-BGfBii0sShQwTIcdP947Q5kAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
فرمین:
این بدترین تابستون زندگیم بود! همه چیز داشت خوب پیش میرفت که مصدوم شدم، اوایل جام جهانی نمیتونستم بازی هارو ببینم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/Futball180TV/102290" target="_blank">📅 23:01 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102289">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ylbw1MOE6tPy7qZeog-zxhhIxgLHIwIbAOWAilxZI8zioR1fFRkJOeEQhOfBhJC4odvzORV2RO1B_TqhcCzFW9VwwtBu6K9G2Myaq800ZFhywH2joRwiHXJq78laF6R81yBNNNxIh7Psj70VSltiCQLYGrofmIq6D0dPyu7Px0wkgO5ge2-_ANgnpsZYDownV7yb3_McqSvJQULQS3kOJr2sUY3Mdp1IF_6J-p1XE9SqwRhoppsWW4Vked8c0qyiwTPyGOKbUmqUo1ayvuNDUSwWK_vBm7EnNPEQ0caCXVoZYF23OeoauvYlUXkLge6QuqhjCL_hbQClqj8rSMAyhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
کیت سوم دورتموند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/Futball180TV/102289" target="_blank">📅 22:34 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102288">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qrzvb3rmJMGxD4g2UYvDJnNfAaBI0U6epwnPfiHD38qdF9ecvcS97RQHEmeWnqSa2oK_I4R64toyUuCSbSlGz4Ps_Y8J9CyGLq1Bsi4sqX_rbkLtRAqHbeJUPBaedNXInfxTzh7Tbx7XmAELXqZTyvA8xvUh_wR5bKoGJS9g0m3Nogyphs41-18Ov3XXgNRbJrcZfftyapwT461ptIMyw3sKLF41V9HCb2IbYknb1gJanjL8quiMFgzyy76MAg3a3aNOjOLiSFfTUeagwiQh0vI0PSjup8_gr9xsXULrOfUFScLJW7gJpcOiNZ4qSjS_8EAWkBEuZciL9a4fHCZMtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست جدید رونالدو چه سیسی گرفته
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/Futball180TV/102288" target="_blank">📅 22:19 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102287">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f5b210f5e9.mp4?token=KC6taoj9N_zo9qt8GYSJbkue9Y3Fra5K8JlFtly_PBygrZXorugBzuAokATGPoR6GVfAZeMjkuuYtEahDtpb7Te3H9tAmDY8xTTacXnxKGSddXvx4KJVvoCRGllrHUHap3cu_JIxzg2MCM0cfPw87TcIQleZSciqixBYtB2oFKXbS_-cM3hxqXmhODjp7w47q1kbz-zfHTsTnBvbl3JwR1nqPF4niOazNsaBXkK5WAwTThpj2AQEowPMCd_Y12Z4oppEuwf44-2jYCfrocnyPNmQ1dsaFv15Erpyxic0m8pfZNRayzYVZnT0gyG1xtH2YqiE8mg0MRTPnd7DC3qJgg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f5b210f5e9.mp4?token=KC6taoj9N_zo9qt8GYSJbkue9Y3Fra5K8JlFtly_PBygrZXorugBzuAokATGPoR6GVfAZeMjkuuYtEahDtpb7Te3H9tAmDY8xTTacXnxKGSddXvx4KJVvoCRGllrHUHap3cu_JIxzg2MCM0cfPw87TcIQleZSciqixBYtB2oFKXbS_-cM3hxqXmhODjp7w47q1kbz-zfHTsTnBvbl3JwR1nqPF4niOazNsaBXkK5WAwTThpj2AQEowPMCd_Y12Z4oppEuwf44-2jYCfrocnyPNmQ1dsaFv15Erpyxic0m8pfZNRayzYVZnT0gyG1xtH2YqiE8mg0MRTPnd7DC3qJgg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
ادعای نادر فریادشیران درباره بیرانوند:
اگر بیرانوند همان متنی را که علیه علی دایی نوشته بود، جلوی من نوشت. نامرد باشم، یک ماشین به او ندهم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/Futball180TV/102287" target="_blank">📅 22:15 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102286">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/COeAP_LxthPJTNEMPFda-dXhERp0QyWQ5mJFmQbSiHLn1OCKIp8tmUB6IciW-oLb41BTigAY6YKGi-ugiqe3zTbcYpg5qpbccCIHNZHz3kap0ASC1GhEuzhhEgNWkgLj_z4pjp3nepRzL6aLKdNSibeET9hkp0rDB03Dp4jlIMo9TKM1xZ5iEu1pS0JOdDuloKMeoubQ0khQ-vafG_rDAHjA-T7ZTvSz6VmDEFUgJnc5qfnO6n5QpNJHBewJPpiTkmku1UJdtuWJSpD6GGipIww-ksySzHbNOLP6JFJBd3f8lJojk9UktFQpUBUgOcWZ3sUY_2ju9iNMRap7HMVpZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇦🇷
فیفا بدلیل نمایش بنر فالکلند در جام جهانی 2026، پرونده انضباطی علیه آرژانتین باز کرده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/Futball180TV/102286" target="_blank">📅 21:50 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102285">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb35f99ea4.mp4?token=L-nYR8LLCcOCf0RBnxbXg7A8Ai6MdT8LL3eX7KsPTcThGYBH_bg93_Gdz2vZHP9-xSzQ71N9kQ_8-L8fKb11DZKsZ_kQKaPyBydlj8RZ4Vv2KQDQh1Co_Snci0zfLYiaW7ehP_ZkkU8zudG17y7NW4Cqj6o8MSMis6RTwmEFGhcZ9UTMgeQgITU2mIw7I-hA_m-CfkwC8Mx8WolNCsauAEs0H4Ntbf0CaZCeXo0fgTC0As2d9tFvoVqWwg0mh1v9WHNjXVb2NJAwGnN6DeLvGFMRnbIDuL8Oh5viTLzILDug9hGC0i_wr_JkZ1czIm-rW5gHbEOW__E6gNv70qTdig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb35f99ea4.mp4?token=L-nYR8LLCcOCf0RBnxbXg7A8Ai6MdT8LL3eX7KsPTcThGYBH_bg93_Gdz2vZHP9-xSzQ71N9kQ_8-L8fKb11DZKsZ_kQKaPyBydlj8RZ4Vv2KQDQh1Co_Snci0zfLYiaW7ehP_ZkkU8zudG17y7NW4Cqj6o8MSMis6RTwmEFGhcZ9UTMgeQgITU2mIw7I-hA_m-CfkwC8Mx8WolNCsauAEs0H4Ntbf0CaZCeXo0fgTC0As2d9tFvoVqWwg0mh1v9WHNjXVb2NJAwGnN6DeLvGFMRnbIDuL8Oh5viTLzILDug9hGC0i_wr_JkZ1czIm-rW5gHbEOW__E6gNv70qTdig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یادی کنیم از روزی که نیمار باعث شد کرک و پر امباپه بریزه:) خودش هم اصلا براش مهم نبود ضربه رو زد بیخیال رفت. امباپه اون پشت داشت جون میداد
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/102285" target="_blank">📅 21:42 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102284">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromچِشم به راهیم</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8732bd386a.mp4?token=WG8lrcR0Wdv5bjfZe5ty9slnbn8UDMiRaKZB2jxPdjJDKvndF5YrerlbrJJPRndr13HEav8oVGu6UZTdkJua3yyasFg9rtvkLRTJLRQt3CPqEDDA9Goq1f2Mm4QjWdHsMdZnAXjGkEFz73eiDjJiSvCbwCRxYrs7FjR6a7k6S9DZUk7RzQKMNAcRToWmAYY7-7DE0Hrt4ehfTBptQ97GH6Cn0m2rfKZnoXofP0aiaZvnLuZrokrjVpgIGd_M_Ig7nHJUkC9miJFzStflgaTABi22M1OLcPBlxrjQFovrGhJo6KZ_SrkBqOJlUXx9-7IAfW7YakSvacP9DPJbhH5sKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8732bd386a.mp4?token=WG8lrcR0Wdv5bjfZe5ty9slnbn8UDMiRaKZB2jxPdjJDKvndF5YrerlbrJJPRndr13HEav8oVGu6UZTdkJua3yyasFg9rtvkLRTJLRQt3CPqEDDA9Goq1f2Mm4QjWdHsMdZnAXjGkEFz73eiDjJiSvCbwCRxYrs7FjR6a7k6S9DZUk7RzQKMNAcRToWmAYY7-7DE0Hrt4ehfTBptQ97GH6Cn0m2rfKZnoXofP0aiaZvnLuZrokrjVpgIGd_M_Ig7nHJUkC9miJFzStflgaTABi22M1OLcPBlxrjQFovrGhJo6KZ_SrkBqOJlUXx9-7IAfW7YakSvacP9DPJbhH5sKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/102284" target="_blank">📅 21:42 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102283">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HyaRYvVaIgRy5rIR3mwuZyL81x1nBpPuSyjFLoPxccRTgQ-mdmMmYsRJVU7mYIsMCbQ99y2OLiQLMuYR4z7SapnTZv-l_RmrVWCR0JTXYN8gx6XuE01X0sXA10enijBbSZkkLGIyr1jTZixXsjLG2i0rPXJKvvF85wI3Wzjh4nVHYaLk2w_-OW9d1B2R-1IS_1sBkDuNH9z4AlZK7kMkFi3yA5G8fAH3o9HQSs_kNEHf2vl1IcnaNPiGnPI0K3LaMpLit34CTr1YXYhsWehSK618aKW6tyJLgwLIaGAm7-KdlsUsRG4qyeR68MOwcs8H75IcPUhVKcRR5YJ_uH6KPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست جدید جورجینا که بسیار هم پرمحتواست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/102283" target="_blank">📅 21:40 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102282">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L_zgGU7I4-D4eM_PIFQIyCkmK6iP5AOhhZrcXVfgGxrNwP4rXcWoE4zY39vI4nH1W4p6PmNizRcGx2ev-yUU6s5LVwRRuDCoggcTe4J8hptOwJGdFH801DFQw0s1AOO8NCKBVWneYFJkvPzaLoViAJL95NAzqmVjCbuxKD4nnXy_PIAcjqFBjOaFEbU8LmM6IDxht_6anwpFFaFgW8gbUTEnBmA6VSgRH01vwFR3dnAYTCd1Td80iEjy9iZ7sj5a6HPdgOObNoiRLOkZVNzMY6ecVwZSz0hlTlmNQgwHKoUPvNaNK2tOlnV8AKz7HyPse2MpVFSeH6yj6Rr0suH9nw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/102282" target="_blank">📅 21:20 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102281">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1795b5f8ad.mp4?token=K9Gg-IMobVBukAn4sRf84_2UmX8zZK-E7pndlmJfAT8a1T9m56Z6dFhnHZtKPVjxTbRQ_XUmK6PB167ZTQiWapY-GRFwDqjQflKq79lr5cYgiGClJbZ6nLTJf8lqAuYL3THATjOHYUhM_ur6WnuvSeZ36Ik8mNlgpv-qZfyja4s0vz5XipyB8SZLC83DYXor2XUY34Jj051tPxBqZrMoc5Ge6eAaGvH6wIxIAHBe8iDaFM6ZsSWJhle21lZv6xISbEwsvT3XxlH6eCXSGabBuvDz1x4iZoIqOLIQjtMewlVceKTcVgkq86qW9j3azI-V2ddNYqfUl5BSfKGP2uG2DQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1795b5f8ad.mp4?token=K9Gg-IMobVBukAn4sRf84_2UmX8zZK-E7pndlmJfAT8a1T9m56Z6dFhnHZtKPVjxTbRQ_XUmK6PB167ZTQiWapY-GRFwDqjQflKq79lr5cYgiGClJbZ6nLTJf8lqAuYL3THATjOHYUhM_ur6WnuvSeZ36Ik8mNlgpv-qZfyja4s0vz5XipyB8SZLC83DYXor2XUY34Jj051tPxBqZrMoc5Ge6eAaGvH6wIxIAHBe8iDaFM6ZsSWJhle21lZv6xISbEwsvT3XxlH6eCXSGabBuvDz1x4iZoIqOLIQjtMewlVceKTcVgkq86qW9j3azI-V2ddNYqfUl5BSfKGP2uG2DQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/102281" target="_blank">📅 21:01 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102280">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TL3UWP_Q_-UOillI6dOGBdtTCSk9ftwzNM8Qb7spgzBchcDpgxE0oDDmh41VSTLTdY6zDdkiMCrq8AlJGMHkPU2HbxpFD0YQBB98MDX2g1wdEV6U63f_pqx5nq9DugOBREeFAaacDcdVTqhUJ2fd63iHN7Li_D6mXvWn81ews2iHvEvPNevEmj47MJA8FsGid2BjOvHR4mlm9ziJ_NTnbWsH6SExg-cw3VyuDC0NfsHpYpoIEKSAbs1JKVQM41jPedEf4g56sNL8zO4lZhVFyYfucC8vK63OS7UGdHbJw1KaQJZatuHA-7noaJud5sDjEcatKw3mXuCWadMJehETUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
🏴󠁧󠁢󠁥󠁮󠁧󠁿
اووووووف کیت‌جدید منچسترسیتی رو ببینید که قراره دو سه روز دیگه رسما رونمایی بشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/102280" target="_blank">📅 21:01 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102279">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t_U0mfmo6XTOOq4zo2nCg-F71q1d-6Qbpe5dDmWGANNdDEduaMyQ-PvE6SXen4TjQpHauI42AD1mcdYayJbFlIovuaMrZZsN6DJnag-r7Q2xner46pDWTrp9Ha0VJ3c5-zSZsuGQge1qTjqc2puI0X6SIfFqxyTtgr_Hx4EnL-MhFOAg-o2oh3-7C7-VV7DznTqMFqEw4tzOnYA43B9bqyIX9MTm_dLjHMkV3lMQvB0dqfEorwkhnfXyLZsNMhFnIUsnPsfU5RNGuRYDVEKf2faZQhvdcIk4gwQt4AFcRd3eJlzN9l-t_1HGlWpho6O9ZBSDM46rCCwhkqvo3I9J5w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/102279" target="_blank">📅 20:42 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102277">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/n8aGItYsGq7FBAxozAHhhW0YF8_uGvxpZKlnp5eR6QicrB6u0MxALRG6xmiLrp6AeRRoPsrGHrCIHBfY3SJByS-rACXQgx4b1EiCqevJVulOGTuXrlcEl2VsoxhvrNA6FsI9eGgOsZ7-FdJsr7IdLQprvkZKw57wEQEqYzc9sUw0TbBrQO9BKltTcxPWQvUiuzy7p48Rb1Jd9Ogw_098C84c4CqL3qv0lpipLn4quOneBRtGlUBgql2cVOzhQsF-65mVeApKYvKOvcsyV04rhn_7iEVhNM23Pzeh8SbU5pNMSlqgtrs_pSH6OpeZPqD8xZtfujflIkSIkvQLQwwvxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oI3QkuDUrq1-89QECj5Xk1aUwj7xGq-98yNvHn87m_7d_aaGTRCRNlMa-efDMadQl_d80__pi-fX3iIk_7kgLkNv5bOo5a_TGP9WT5H1BoXyFBC2i-Aegb2yUR1VxrDcwTqPLxSvNQ_WtiTUEE6mTgvrCumMrFZx3x5ALVpIB0aY0F9DmDJax-ckZMqshxNpTdUZg0i3Mb3UqGQnQzBpOpDxfm9yUj0tvLsXGDYREmCK6kMKXIn79Poos1IAQVwvx96-aAZAcYxEchg1bC36kheo9_NJdg9oRuqdFxXQcFQlSuCfMrz8rnKcfrLi4gNlyEHscdgsJSO8fFYvpLwZmA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👀
طبق گزارش‌ها، ویکتور گیوکرش، مهاجم آرسنال، ظاهرا سر یک ماجرای ۳۰ هزار دلاری گول خورده؛ گفته میشه به یه مدل اینستاگرامی پول داده بود تا برای دیدنش به لندن بیاد، اما اون به‌جای انگلیس با پول رفته یونان و حتی یه عکس فیک فرستاده تا نشون بده تو راهه. گیوکرش میخواسته این قضیه بی‌سروصدا بمونه، ولی ظاهرا اون مدل برای دوستاش تعریف کرده و ماجرا لو رفته. این اولین بار نیست که زندگی شخصی گیوکرش حاشیه‌ساز میشه؛ قبل‌تر هم شایعاتی درباره ارتباطش با اینفلوئنسر سوفی رین مطرح شده بود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/102277" target="_blank">📅 20:40 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102275">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TaKP2uRUu0ABgFzzgORDv9pQd9R1PFaVtYikMv5Nx1-87cu16VNgJ1MP41QFRcIAWLH04rHVaK7LnVvgyeghzEPVfoZONeD-bBLdD9fow6QOA0tEC-QQ-Vjf3e9L-PZDBRMXYxumkJhpdlH78ebQNQBIfbS12tBOSY2Ou6ZzzTwzrNb7tDbyOTfRLenXvp-lNfrEMo0o20mo_zqVH6VtUxDWELfidnh7d2Db2fHKqwg-bzFC2J96iL8bDoWggwdse2GRpcGIQvKrA1ZExEGkPPluvUyHOMOiFMn2xggEzkwbm5OY2kTYkqNvv7Al_Je0SZG9msNW_MXrgIRLVSBtKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pKUDPlLgg2SCI7P3Wvywp-XMCazJ80EEN2OmP_7n1C_DC9p9wddp3KY-6XyxBYF5zmlqBu_94TCvb5sLZCmMdKcCWzBT0mwAzNbxWfpHFKMxfQ2FO_6LNtmTnGnKC7cWjqLr7SUmxnJDG-XsUZJHKG9FezxiuUTO290JbM6lZmZZewYJaCUM0jaiI3kVRIAuzk_5bsLBpJQTmg7si2mKeiyLL0g2SdMtfFr3Ehbdh0Kt4sMiyWROlgjha72OVdv4_Rg_N9u-aKNTm7oLe-YY_XoaDG-gOZf3o2SWVohIvqlvxL-phEgpjzKOQdUgYATUYVK6e0f4uj5NJAIFeaMGkg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎙
پپ گواردیولا درباره لیونل مسی:
من جام‌ها، رکوردها و جوایز زیادی بردم، اما شگفت‌انگیزترین چیزی که تا حالا در زمین فوتبال دیدم، لیونل مسی با توپ زیر پاش بود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/102275" target="_blank">📅 20:20 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102274">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H222EhZADuD-ByEZjiwrP4b5oGQCSMv4vNs9_SYzUM4uvukFdAGzZDYWET6gueIgaKq63e4RSA6DQSSa4LzUq2k8xYhiNH-j4lxNdcyKbgBC_duDs7M2JGBHFVMb-yJeInP2cdRMr4WeeqnKyVkGugkkN5_8UPAcBBqXecMGEYtlZuv1W_o55ghM4bCxmDa0guSrG-YriuqWVzrsZIYLPYKGh_thkX2zgBxcn7d-POIsA6WsMHWIAC-hwdzP2omRJ5v2PkV99vlXUum23aPMOCZRZbkQ99uxq-QFNHNY9OcXpgxUS5Z_CljjG9JdSem_6mxhcLdpNq73bjQ5d8X3kA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇪🇸
🗞
#فوووووری
از رومانو: بارسلونا به طور قطع نظرش راجب فران‌تورس تغییر کرده و هرجور شده میخوان نگهش دارن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/102274" target="_blank">📅 20:11 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102273">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V33jNZGF-7wmmqo-PgBlSfZreh1d6qeWf_kVdUrpD4MWqrBOfurVi2xzmuhEWOqgfDS6BQqWOtqFJ3sMAs4JCusb7rxqpJpyjFaEpM8e7NXhlaM17o-Y2w0z0-o2DvbIFhT5X0VMg-hVgPLfQ6Q0oCWbJ-A_Uxdz60zFU9Q4mxT3jUGqc-AM2zLU53EU19iukZ36gK9d-AM4REl_6LttmcxVB7E7p_PMKILqgW83rf3R6brbC3mcNgjzsyhIPkGOmGMCxCQb7WKUxOi8gnPlyFt0gRmqZknymFqxRyjUk8RYkz2PrWR0WS7SwjoMHbd4SUMyZV83Vmu99iEITWeHGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیوفیس کوکوریا مدافع رئال‌مادرید
😐
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/102273" target="_blank">📅 20:05 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102272">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/84ff90fced.mp4?token=S8pyNJmXw4TUR98405aQfevN8reuPs6aC8Lk_89B6hsBNwLvca8VgNWFffaq88DsHpJIkDopgTbLPWL4WPBwvPIQuKjeU-D95-pa02emb6X7SfP4EoaShjlikRHPbC5Ix9sdO9BsaRBQW6mCtaabyvDZVt--Y4hy51uajSbLyUBPzxKG0iXjM9qQ5x5MEW6p3AkOe96RVSpx4viY_7rQOL4Lh_fiOsrq9TMHKGPtHNMYXVCNRuQtp4mXb38op-5_DYABXUafQ6foM2meNlK59qo4kV31fptgn8nj8V6lXDz4w64fbqsh4hzkxOVxvuw8ISHArMzGOs-NAHsfHulw0kf3wHJh5kSj7enU7dqtg7YN7j8RLXQ4Y-oQW2RN6Oha5KJFdWDAgcojnEt6gBvUXP9QLCGcp-2hUq2S5JXO1ehh6_taVNvUlkg6-UzPYYgimlSBp3BLR3ZIGfUpj38tj7Zm7euna9pv0Upw77VxfkKpZv14S0kCJLZ4Uiec7B48BDnUt8Zy4YIjCkoRqKgHC5xdlw-ms1ODoTYydHr_Vl3pzbjOVqR-3vU6uIZIcS5F6geBqJlOzcCeIXwJtTJyr3hsvRLaKvdyPX6ex98nWHdA9TTqHT2vLXlQ_kzVnFvb-KNV4kZf4-3URBW0QXvkspv5MAVIqHKis0O4jqid1Ko" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/84ff90fced.mp4?token=S8pyNJmXw4TUR98405aQfevN8reuPs6aC8Lk_89B6hsBNwLvca8VgNWFffaq88DsHpJIkDopgTbLPWL4WPBwvPIQuKjeU-D95-pa02emb6X7SfP4EoaShjlikRHPbC5Ix9sdO9BsaRBQW6mCtaabyvDZVt--Y4hy51uajSbLyUBPzxKG0iXjM9qQ5x5MEW6p3AkOe96RVSpx4viY_7rQOL4Lh_fiOsrq9TMHKGPtHNMYXVCNRuQtp4mXb38op-5_DYABXUafQ6foM2meNlK59qo4kV31fptgn8nj8V6lXDz4w64fbqsh4hzkxOVxvuw8ISHArMzGOs-NAHsfHulw0kf3wHJh5kSj7enU7dqtg7YN7j8RLXQ4Y-oQW2RN6Oha5KJFdWDAgcojnEt6gBvUXP9QLCGcp-2hUq2S5JXO1ehh6_taVNvUlkg6-UzPYYgimlSBp3BLR3ZIGfUpj38tj7Zm7euna9pv0Upw77VxfkKpZv14S0kCJLZ4Uiec7B48BDnUt8Zy4YIjCkoRqKgHC5xdlw-ms1ODoTYydHr_Vl3pzbjOVqR-3vU6uIZIcS5F6geBqJlOzcCeIXwJtTJyr3hsvRLaKvdyPX6ex98nWHdA9TTqHT2vLXlQ_kzVnFvb-KNV4kZf4-3URBW0QXvkspv5MAVIqHKis0O4jqid1Ko" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
لیونل مسی:
آنتونلا اجازه نمیده داخل خونه با پسرام با توپ بازی کنم. تناقض‌های زندگی همینه دیگه! من از فوتبال پول درمیارم، ولی حتی نمیتونم داخل خونه فوتبال بازی کنم.
👀
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/102272" target="_blank">📅 20:02 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102271">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v8XiVhEZejjrejA1QCYndazM2oDaB_Ev69chI21QnSrW6vMigH7cV-wXBfM2rhYx35pMxKy6S6a1SEVA5LG4o9F8weokLgd1OU5cAY1GpKYFQfWo7yHEbE09C0HihmpHwp6IWQqJ4XbOOYJ-450JH1E7KMsQ2jERiNqIrXnjJi3uVTkwstMRQ5bm2xsMjp-rmP_454X6Gw8BbadG1hOF6gZi85Wpc1nZumrmjHcfYMokfwOsy0drWDO1t3GJba6vrJRLij9eTjvaDGuYf8dsyJxmBug2P19i6Y7E6Bs4foxYTN0TFiwfaEUNhnBvi4SmDKEoM2ubaF-FEDoobyhSPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
✔️
⚽️
نگاهی به اسکوربوردها
.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/102271" target="_blank">📅 19:51 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102270">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f57a7d2d3f.mp4?token=fuc9SL3wYViICbT2bGATOeHt7YZsKStG_YNd5L_tYSMKnlsFJ26R2mbGEYwfX7cbfXhoG1VIlwfyOrZsrtZ4uma3mn_OqZaIuRZsHx24KMAA0Eo5oS0OqVOYvK5OJ72dM0sofeCSkxC0yt02l9K5t2uK4_8LQrWaUOHRvFYf5lADyLXv-8XQHhH596VElnOw-2inRbotDTzzo-O6Gb28ZRRTTHtBHieEVBqCeFIbjY14RquRwfVmknaU5SQrfL6LTFoSaQPDGimRZDXxrT79vqIouifLyZuGMm943fT-0e4DPY7F0qSTUuBlObkeqIgqrwHWlYGCS5T28UBXhifjmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f57a7d2d3f.mp4?token=fuc9SL3wYViICbT2bGATOeHt7YZsKStG_YNd5L_tYSMKnlsFJ26R2mbGEYwfX7cbfXhoG1VIlwfyOrZsrtZ4uma3mn_OqZaIuRZsHx24KMAA0Eo5oS0OqVOYvK5OJ72dM0sofeCSkxC0yt02l9K5t2uK4_8LQrWaUOHRvFYf5lADyLXv-8XQHhH596VElnOw-2inRbotDTzzo-O6Gb28ZRRTTHtBHieEVBqCeFIbjY14RquRwfVmknaU5SQrfL6LTFoSaQPDGimRZDXxrT79vqIouifLyZuGMm943fT-0e4DPY7F0qSTUuBlObkeqIgqrwHWlYGCS5T28UBXhifjmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
⚽️
دریبل‌زنی در حالت عدم تعادل (Off-Balance Dribbling) در FC 27
.
این ویژگی آن‌قدر اعصاب‌خردکن خواهد بود که ممکن است وادارتان کند بازی را وسط مسابقه ترک کنید!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/102270" target="_blank">📅 19:48 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102269">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7495121486.mp4?token=MreooI1rPikiS7xY8GiwUKYwC7uQhvs4MSwJLP_HRlJHVXp9yJEmTxHp1dAZvotzLHwo7c2xpksHRokzGcWHRRXA77WrEb2cgqKSdFz7Gk2HXMSe5oHZnYNXsCeJ9Va_rmkPS2jEjYsplDTnA0quW_waqKcXHXhVKQJ5kXNHFEJdPFKMP_u5Z66yaGk_7mM0VNyZCmZDuzBpwBQ9a2RUgKQ9GbUs50VAoGHFPanI7VH5fu9ThcGYNwdimmyuASI7e6G8ET5m2khPePp1dFKgfNsPXTN-QNxEjCslPLwmNdQIXMlv9cLeB6NTQIY6Ab21vcQwRs6MuqhlnNpd1Ijqdw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7495121486.mp4?token=MreooI1rPikiS7xY8GiwUKYwC7uQhvs4MSwJLP_HRlJHVXp9yJEmTxHp1dAZvotzLHwo7c2xpksHRokzGcWHRRXA77WrEb2cgqKSdFz7Gk2HXMSe5oHZnYNXsCeJ9Va_rmkPS2jEjYsplDTnA0quW_waqKcXHXhVKQJ5kXNHFEJdPFKMP_u5Z66yaGk_7mM0VNyZCmZDuzBpwBQ9a2RUgKQ9GbUs50VAoGHFPanI7VH5fu9ThcGYNwdimmyuASI7e6G8ET5m2khPePp1dFKgfNsPXTN-QNxEjCslPLwmNdQIXMlv9cLeB6NTQIY6Ab21vcQwRs6MuqhlnNpd1Ijqdw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/90a87aed54.mp4?token=IRcWun3sFlWeudWjyvckgtNUJTvPofLcc_DW1WMc4jDPYFMGFWkKyIb7ilDj_DB8b4qk-gzZDRezMuaK_tHpyt9bglydTVnj-GJtpVAa83CS6SdZ8gsHv-g1btD2UQr21kjURFhcNexEKluFZHvhjg3E1fB6CfkjYdmeKlPXihwRUxnhS7ZKc5DrmmpX6rSvNSVv8IOmd1lTi4X2yKQy8xmeQBYQwBvnQd6LH40L8365UsDUSHk5uobRMibwwd3QsMwriN-yRGsPYVZaZpWPo5aoJOpnHSXl9huKzQl8NTlQBvlFHxYWAuPoJcks_H45HDza6uARwXG0vGJFVtGy_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/90a87aed54.mp4?token=IRcWun3sFlWeudWjyvckgtNUJTvPofLcc_DW1WMc4jDPYFMGFWkKyIb7ilDj_DB8b4qk-gzZDRezMuaK_tHpyt9bglydTVnj-GJtpVAa83CS6SdZ8gsHv-g1btD2UQr21kjURFhcNexEKluFZHvhjg3E1fB6CfkjYdmeKlPXihwRUxnhS7ZKc5DrmmpX6rSvNSVv8IOmd1lTi4X2yKQy8xmeQBYQwBvnQd6LH40L8365UsDUSHk5uobRMibwwd3QsMwriN-yRGsPYVZaZpWPo5aoJOpnHSXl9huKzQl8NTlQBvlFHxYWAuPoJcks_H45HDza6uARwXG0vGJFVtGy_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/102268" target="_blank">📅 19:41 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102267">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5128380014.mp4?token=Au-416WlcFuHDGubOY6rt_Lz4fOxuIDTTN86n-5O--T95MapJSrQqMpB5_cPugex4RDRpMTbyMdy5ajVkVuIKmIeCWdobbzhCmrm1LBPdkbumpsWp5p_I6vCoJJv0WoiZXDGKUcigZ7pBJ0DE8Y2JIYdxPjedOT8AT1eHLztF0Xd3oFt06SjSqmt5sFI0q7cpMSpX4ytw2iuIHMmYfYs0sZFgWN0sKbY11ZZuBycgXuuyr_YHpAzU0esd1DhwC6mEZ357YAJ2-ShagD2sCtznM3LT2-ZwggeCMyWCBOt_n0uAxZpQ71WzYLQ5TLxWKkX7WwiKEM0-2UGwMc0vpKSLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5128380014.mp4?token=Au-416WlcFuHDGubOY6rt_Lz4fOxuIDTTN86n-5O--T95MapJSrQqMpB5_cPugex4RDRpMTbyMdy5ajVkVuIKmIeCWdobbzhCmrm1LBPdkbumpsWp5p_I6vCoJJv0WoiZXDGKUcigZ7pBJ0DE8Y2JIYdxPjedOT8AT1eHLztF0Xd3oFt06SjSqmt5sFI0q7cpMSpX4ytw2iuIHMmYfYs0sZFgWN0sKbY11ZZuBycgXuuyr_YHpAzU0esd1DhwC6mEZ357YAJ2-ShagD2sCtznM3LT2-ZwggeCMyWCBOt_n0uAxZpQ71WzYLQ5TLxWKkX7WwiKEM0-2UGwMc0vpKSLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/102267" target="_blank">📅 19:40 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102266">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a8d0459b3.mp4?token=seJiYeBWiCk3mUbJqAaplKHgjlUn74QR1XmJFrKU9vHdavZbg4STgJGXcTVSRTLjXzsNc4rsBME2WA-rwZHw0TLO668vOPdYpCJIMu6oxUi7DrY29729p1chwxfXHYqCsLEWwmrKyjDE4sogE_SY3XGR7jHcg0xySNzWtWqw6Gqg_gKAGkaM52XP3i7W6w-bU29EUqhvyPgUUBqNFcKCm8VKmIiBpre8_NEkC6Tb9nMk-q8ow4LejZ9vxdynLQ5T2q-WlKF9p0zIceVhxZ9h0I6hfOBumMvAQEdzFM9Hi4V_2AzoX4Tj-EfqDDfH_7itpzsKjeQQVIWdq4KNzHwGzIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a8d0459b3.mp4?token=seJiYeBWiCk3mUbJqAaplKHgjlUn74QR1XmJFrKU9vHdavZbg4STgJGXcTVSRTLjXzsNc4rsBME2WA-rwZHw0TLO668vOPdYpCJIMu6oxUi7DrY29729p1chwxfXHYqCsLEWwmrKyjDE4sogE_SY3XGR7jHcg0xySNzWtWqw6Gqg_gKAGkaM52XP3i7W6w-bU29EUqhvyPgUUBqNFcKCm8VKmIiBpre8_NEkC6Tb9nMk-q8ow4LejZ9vxdynLQ5T2q-WlKF9p0zIceVhxZ9h0I6hfOBumMvAQEdzFM9Hi4V_2AzoX4Tj-EfqDDfH_7itpzsKjeQQVIWdq4KNzHwGzIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
روایت جالب مجید «قصه‌های مجید»:
وقتی ۱۵ ساله که بودم، تنها از اصفهان به تهران می‌رفتم تا بازی‌های آسیایی تنها تیم دو ستاره فوتبال ایران (استقلال) را ببینم. در ورزشگاه یک سرود می‌خواندیم که آن زمان غیرمجاز بود و البته خیلی کیف می‌داد؛ آهنگ تنگ غروب سیاوش قمیشی…
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/102266" target="_blank">📅 19:20 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102265">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V0vacz0OIE3sofCAuqGg33L_P3yoZwFu6AFI-tQt5N--TvB61MBd2T6frnYLAeSmMAkHZmMtvypM9EzhY6v22rcM9WSGU_K5Kl--DpJH83g3taApPXKJyqYyZ_joQyNnIWE0DOTUILgdsx7x7r6GyijFKi4Dp3XRtIwzSa9C5K8NYud4J0Jsjo7_5VIySf_5idqVDuKTcJIvvJeLLdYJu7pKM8gSREu46_EMJ4KsV5VqH3D3c0Y6GLM4oD85ovmvpw7aBF04OGLRyaOcmkeOTIy2baZp-IGT_ukw99KALdZY5HJPy4ZU0eunEoMdiRUDDtaDxdkSGoCJ_g-6ZFLCpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
🟢
تلاش‌های علیرضا دبیر برای حضور نکونام در پیکان هم جواب نداد و ساکت‌الهامی سرمربی این تیم شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/102265" target="_blank">📅 19:18 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102264">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6bcb41b861.mp4?token=uQ6rbAsjtdDSxCfy3HlWek5Z84T_JW3YjiqHmUtU8s5miT3_pDSuAvyjaEESdayOKq2sL7nYSjwI7-qJ4wlJnMoX2qUQK5kRm6g-Yhxx4tyTtIWf9eW1P56MQT8QPn5X17B6JbpY-Tq8LYaXDVasWdLBI-fWqbXpmn8SPx2u641Us7TTTtiL-Oa8jDgCC28vnAV5g2xm75C7Dj3MJSP7-7a49Zoo6ScSTsJv5RQVL_g4cVijn_3G5gE4e6Wqe69yh12w1go64vPigIvLIUwR5aSFKY8bo6BePJWfrX6U-wr_dLrOXBvTfPqdlJH8x0z8_PfhdREhTvHu4JPMSaoDgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6bcb41b861.mp4?token=uQ6rbAsjtdDSxCfy3HlWek5Z84T_JW3YjiqHmUtU8s5miT3_pDSuAvyjaEESdayOKq2sL7nYSjwI7-qJ4wlJnMoX2qUQK5kRm6g-Yhxx4tyTtIWf9eW1P56MQT8QPn5X17B6JbpY-Tq8LYaXDVasWdLBI-fWqbXpmn8SPx2u641Us7TTTtiL-Oa8jDgCC28vnAV5g2xm75C7Dj3MJSP7-7a49Zoo6ScSTsJv5RQVL_g4cVijn_3G5gE4e6Wqe69yh12w1go64vPigIvLIUwR5aSFKY8bo6BePJWfrX6U-wr_dLrOXBvTfPqdlJH8x0z8_PfhdREhTvHu4JPMSaoDgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/102264" target="_blank">📅 19:03 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102259">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d7OgMvNtx4Da5s3xQkBGyHjWbwEVuOoLdJZvwlSXTiXNxVomKs0KWvVEQQUf7RIR1m27D7XMAWJYYHlE4fvSngIFUw4Tf9sJw3-jL1Lt05TPn8-8CphEa9BtHG2HJxEtU9lsd02Ye1irBSS_MaeTCNPM1z3gM9nZWKMSGBF9V-RH_QewJCwcyR97u_OLBQD1Ak1jJKkH9pH096N22kkFdc0f7uBlXlllDiLrZCtkPKXauHFMgISKSCFfICvhTOfahGwszhKPC6NyyFdjF0IBjL1I45eL0fVQVtv5fXB0lCX3cWgZjHefNVZHvTMW1a0WRr2p924UJaZMXiupQHDqZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
🔵
می‌دونستید؟
چلسی در سال ۲۰۱۴ با ژوزه مورینیو به جذب لیونل مسی نزدیک شده بود. گفته میشه آبی‌ها آماده پرداخت ۲۵۰ میلیون یورو بودن و حتی با اطرافیان و وکلای مسی مذاکره کردن تا او رو به لیگ برتر بیارن.
اما مسی و خانواده‌اش تصمیم گرفتن در بارسلونا بمونن، چون این باشگاه برای او چیزی فراتر از فوتبال بود. تلاش رومن آبراموویچ هم در نهایت بی‌نتیجه موند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/102259" target="_blank">📅 18:20 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102258">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/18b74b82c7.mp4?token=QgRdHYno7hs9AX4RybZCDW4LQWL1daXHoChFjv8Y0gL5myw6W9PgqX6UXu4oRS-sTeUh6UAvhLibNc7z-b4P7M0wQ7F5dRDmOU_-NRr6mj8CO53vduMlZ70gjfNegDowfqUgLefw4L9KnFCYn3UzGyzWRoecI5N7qV8hOBqp9KVF1ZliwuL01Ke95fOfnZ9vYM0_q8cVLdxu0J7NR4YGkbCxFXKDSir4o_lmCrYhs5FpXv8YSZZVzLNDfOxcxLd-0RRguy4DSl64-idxfIOrjKxXZvpHlfFLw4gHf3lzpKUSLPUgpTYJtCWX50pwPf8wuNxhWm-xdilp9x-TsLXEQVT__L8EvA3cHtVztozTRoNjNdshAhVDfB4MCqNjEpnQiVvtOsA57ZJDwqIybhHVv2FkUm4hhFD6C4IRw-J04iI3F20HuSK1E9djIYmJLQi4ADGHLT6GdoNWMRI6qTlLwup717C6-AR45wa6IguKK_T3n-soWWe2_EIroHOBLTBABdBIdiWdHS0ylbTqxh9tBfXrHmayNPHQMvm209AJiafS0oZGVPzIy7pkZOd31sILqZpSsnIfUfcPOT45-jqozCqQ24xM45mrjdxyL5_Sdp8byGW4p-auRBwPxTWa7vdCH2FM-6p5MadcyAxgx9ROcu7Tb3_kCLyQkzxYujg6A1o" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/18b74b82c7.mp4?token=QgRdHYno7hs9AX4RybZCDW4LQWL1daXHoChFjv8Y0gL5myw6W9PgqX6UXu4oRS-sTeUh6UAvhLibNc7z-b4P7M0wQ7F5dRDmOU_-NRr6mj8CO53vduMlZ70gjfNegDowfqUgLefw4L9KnFCYn3UzGyzWRoecI5N7qV8hOBqp9KVF1ZliwuL01Ke95fOfnZ9vYM0_q8cVLdxu0J7NR4YGkbCxFXKDSir4o_lmCrYhs5FpXv8YSZZVzLNDfOxcxLd-0RRguy4DSl64-idxfIOrjKxXZvpHlfFLw4gHf3lzpKUSLPUgpTYJtCWX50pwPf8wuNxhWm-xdilp9x-TsLXEQVT__L8EvA3cHtVztozTRoNjNdshAhVDfB4MCqNjEpnQiVvtOsA57ZJDwqIybhHVv2FkUm4hhFD6C4IRw-J04iI3F20HuSK1E9djIYmJLQi4ADGHLT6GdoNWMRI6qTlLwup717C6-AR45wa6IguKK_T3n-soWWe2_EIroHOBLTBABdBIdiWdHS0ylbTqxh9tBfXrHmayNPHQMvm209AJiafS0oZGVPzIy7pkZOd31sILqZpSsnIfUfcPOT45-jqozCqQ24xM45mrjdxyL5_Sdp8byGW4p-auRBwPxTWa7vdCH2FM-6p5MadcyAxgx9ROcu7Tb3_kCLyQkzxYujg6A1o" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
🔴
۱۰ گل منتخب تاریخ تیم منچستریونایتد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/102258" target="_blank">📅 18:01 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102257">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a9oa82ggxjhJE67kspLKLnW4M3HSEuHCZoYAV3KJlT1PbOgGEKJzyUyZBMW1fI9AkWfm6f4tpgVehiUFcoAVGfAZpqNFUtFq1EpJML4bFLEY6M6g7gFGZa1J_TgxH9mYFRk-XKtvrfahvQFDbdwu9LCW9SFZ1RnCbntRF8jBVeRerSiLzXp-fxOSUDYVoQY-ErPEvQWtPYPr5rcaWi_dyPOWPxRz-uOjggL01pwk6jEM6uODW5FddPKRzxYQMoXuNHfIfBzYTpgUraeJkvFJIUoU3sXphu-XeAnLqPg_X6D4letVOdm6PPmFpPH3AZqi-FSYrVNBLzRa5uu5EsIGXw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nl45VlNXAj0JZb4ybp6MaAxFaHdBnzxIH8an9YdNMMyJ5tLp3DM5jOcgU-Lg4YbFd3NGB5jIMT4dD1w1t_eTyYEHxsND8YrhxuWGN1DhPI8G1TluhDVY3bVqbss4GjYCAdSTTLFRghNqZn0YyG57zspZkNkP5GEvPSAFqkvHMgS8T7qYMJKxhqkf01xbcL17MUU9zBWhmtJudgh0nAUNIvGdJBdsueJD9Fm1Hw44-p6R3dPOgmyCyAMGTiOi447eDs55ZtLop7rd6z0YVRl_-DdZA1tYnSWDFKE37g5mSQw5kklGEJEOybiD6CzV_wpUoHsXBkVxxNkHzuDql9kZ5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇫🇷
رونمایی‌رسمی از لوگوی جدید فرانسه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/102256" target="_blank">📅 17:39 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102255">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eD1-jafAUwbqt8xd5ST2FeYyMYiK9zWkgRjWISJl-MoqC5SvDQ1x1HBYETetXwMbGfKHquUQc9QEyvqQ1ZH-1dXmOgSbafcH8gbNhK0tGcaWtDba0ntkloCHN8gK0XQrdodJyzEZbGBsE-YvzfI15eiQUsnJBCQ0B10FHsMuGFWulsL-l7JBvSN-Tw3ddvrp_9Ou-p2bK0M2rteC9ZvKlNbweuwKcICzvBv2Uz5Do9a5UxK-AZms2AzgawJHnbNVCSkYFnoEbMqm3tp_Fd6Rgc2xUi2O9FYAnVHShOGTjQxoi22TR_cI9p_heEG0Ci3r_rUUlhg7sKdsRf0LFkcJMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
⚽️
مارتن زیگلر - تایمز اسپورت
🔻
جیانی اینفانتینو، رئیس فدراسیون بین‌المللی فوتبال (فیفا)، قصد دارد بخشی از حقوق مسابقات جام جهانی را به سرمایه‌گذاران بخش خصوصی بفروشد.
🔻
مذاکرات با سرمایه‌گذاران و چهره‌های نزدیک به دولت رئیس‌جمهور آمریکا، دونالد ترامپ،…</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/102255" target="_blank">📅 17:31 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102254">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f4d715de39.mp4?token=u09rJruljSEHI2rsRrUPsCfLxHW-59mhrG9nLL4dwhBSs47fx9X0Z3sil2QhjFoq6TwipJjgJdlDSbQ993fzoQQtQuvgaDtOyqVx1KSjzWZZ5Ay8ZErwLosYruLb1iR7Detdl0oz7pWDMDcyHvRaGt88eXpO-HOl4Im4b1A2iZap2XYcxCoN3l-8B24mb7sf9VmySHQIzKnpAVFZub5fP4s7FrIvLMoOtMpTzmG51Y04gY0CeXDFOe_u-Y8x3CkuOB44kKJ-ZfKrFqc4bMDNBr24uC6hceDjVQ6KoBfqbnM-rzS-itjKva2xIUwZ3P4oVqZqWwQKVMHjSDfFvKStkhl2ATtS3x0-phSqtrvWVMuOCjshARRYBslvEBBdj3gkW72fPVieuUa3WsacYqOGGBlc4-tFZLqbohyPsmH14ffj-V5uNynDvxS__8jfrlXJLai95649hy0wo-TltQd_N2mKDyhx_6BpBMw3IfNhe-PZpzzUOcWtpvnJQPGtQ9x0hM4tC1pMFd0Ww4Lt5gsy7KKMntHb70yaCCHAPTrRsWaRFtcqSwZSQaRv-Z9MTMD0wcyBJQD5NNspO8pLViyF_0jWa9S_GHgXvWYzx64QkBSN41aIyOhJwXCDihnp38DljQJPBTwmQPLGipumr47rDE3zVazgOMN7y2RkUeLJLdE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f4d715de39.mp4?token=u09rJruljSEHI2rsRrUPsCfLxHW-59mhrG9nLL4dwhBSs47fx9X0Z3sil2QhjFoq6TwipJjgJdlDSbQ993fzoQQtQuvgaDtOyqVx1KSjzWZZ5Ay8ZErwLosYruLb1iR7Detdl0oz7pWDMDcyHvRaGt88eXpO-HOl4Im4b1A2iZap2XYcxCoN3l-8B24mb7sf9VmySHQIzKnpAVFZub5fP4s7FrIvLMoOtMpTzmG51Y04gY0CeXDFOe_u-Y8x3CkuOB44kKJ-ZfKrFqc4bMDNBr24uC6hceDjVQ6KoBfqbnM-rzS-itjKva2xIUwZ3P4oVqZqWwQKVMHjSDfFvKStkhl2ATtS3x0-phSqtrvWVMuOCjshARRYBslvEBBdj3gkW72fPVieuUa3WsacYqOGGBlc4-tFZLqbohyPsmH14ffj-V5uNynDvxS__8jfrlXJLai95649hy0wo-TltQd_N2mKDyhx_6BpBMw3IfNhe-PZpzzUOcWtpvnJQPGtQ9x0hM4tC1pMFd0Ww4Lt5gsy7KKMntHb70yaCCHAPTrRsWaRFtcqSwZSQaRv-Z9MTMD0wcyBJQD5NNspO8pLViyF_0jWa9S_GHgXvWYzx64QkBSN41aIyOhJwXCDihnp38DljQJPBTwmQPLGipumr47rDE3zVazgOMN7y2RkUeLJLdE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⛔️
تعریف ژیلا صادقی مجری صداوسیما از بازی پژمان در عشق ابدی !
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/102254" target="_blank">📅 17:20 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102253">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PAhRpjQSQsHjFHA3RMBbK74CiimuW8BlqLoQ2AyZSAULtyBDqyvhe9z7-1xZwqwAT6oFznsz-b9ayBdUocv2WElkdOhOtx2IIGngRsPTDvaakyuwkyArzEKl20_oQSe0qoWlO2W4pN-m8DdrYmj4GajGAAJibKhAcMBBbVMn6QLaNfr3en79o9R92Y6ejQTDl62T_LgvBiNv2ErtZdMwNlj--SMXYuTdogQLW1yCrzsxYdYFBXiU11FrKaZNi2gc0VWU_MukCkflyLk5dGpLez_IA8Q7vHxUojjO0pBxNf6HRwa32O7XXqxDrdyjmir7wDPE6QLwvC85jLTC3BxUAw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DN09iPYflE17vPLSSfvyzGTrN1ZBaFJhz9UFjAAO5Zm0-nB1hP83gkSZuH-ECfLUhfgDAb3YPBGKD8ekDNvP_UNxu3fSoYwXJibVQE6z-UO9RB3PvW8DHGzl7Qy9BMUgRavsFZ0rW_4dDSxq0as_fYkQe0YVFzhtGAT_t-eozvSfm1iUs5Art-PseEaBQQLNSPfmWcXTMkqieHo89a4S2o6WU-3eWUUdjsK6ilivW18ly-9zt7nenF_P8Gi2muQzxQSdHC_8Jd1IEkolvgdZjWeHVkUIlZ0Jh6gAYSZ9KzFrkoXF5mHR_w4Tn7AzzKB2GNlAoq77W0v0AmaYpYzDvw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/102252" target="_blank">📅 17:05 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102251">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jOUyAnHcfFa3h3chXLhzD7eh7ZtO16WD3fTpAqfKBoszFBujJ5b2J7ko2L_lwEqX3eI9qH9xYAKO0eiDu8fkpezVhE_qUTO6dXEpRdt9c4xTAhUzZTtTMhgdR3UXDN1h6edP3m8u0m_IDCB_1nN55GE3EiLIpKzRddGexlU6qu2Am9bg1Rw6vWYEXPN32F1_MKa1KsE37KDXAdVjHupF-3uI9owh-HT3i0RoU0tHMfSaGcW9p9mTA5iFtgzHfiYNXSM7htamPUvJ-W1q4kq2j2y4Q1VbT9X28v47RabJYb4NbAXsVOCn9ebVUq7NXxX0HYo91gom1HiRCjRGkjdzEQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/102251" target="_blank">📅 17:01 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102250">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4eb71ce498.mp4?token=K_cy3Ht80HcWyEZfhHTB1HghpkOg7paUvQQgyUU_WwxyCTMMSRtcD1Vsp09UtXryItkjrNn9J32ka-YB6xLju5iv0MHvPOETTv-Y4baAJd0qS_iS1OCU7_bOwIKvpKMidGKOoK8178U8TsZFLGBlvohV0Y6c0LZ3bfgd_jWubokkof9uav3UganBMzw5iDX8ncoPp56pDm_HQue6QYtTA92APJulEZ5OAYh9FAF390qRiGmPCtp6CBmAQBGmsq0mniImgXPhGLfyz_NbWPKkmhz9zpZ-tY-c69dKMXd_waQXtucw5BebPr6P0o06ciUEbrRzEaUVXUiIc_jyGSju1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4eb71ce498.mp4?token=K_cy3Ht80HcWyEZfhHTB1HghpkOg7paUvQQgyUU_WwxyCTMMSRtcD1Vsp09UtXryItkjrNn9J32ka-YB6xLju5iv0MHvPOETTv-Y4baAJd0qS_iS1OCU7_bOwIKvpKMidGKOoK8178U8TsZFLGBlvohV0Y6c0LZ3bfgd_jWubokkof9uav3UganBMzw5iDX8ncoPp56pDm_HQue6QYtTA92APJulEZ5OAYh9FAF390qRiGmPCtp6CBmAQBGmsq0mniImgXPhGLfyz_NbWPKkmhz9zpZ-tY-c69dKMXd_waQXtucw5BebPr6P0o06ciUEbrRzEaUVXUiIc_jyGSju1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🔥
لامین‌یامال و زیدش در تعطیلات
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/102250" target="_blank">📅 16:40 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102249">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/32ebe18939.mp4?token=kZVkmVgMxFJgKdgeUeLFKNLi4LPdEHTOA6VeaepID9M3F484fWKwCVYTSrUWOVBLqRqlJznUT2gJjLESosWr0E329QGADnpVIPCSqgWM6piLif-PQrIbystUqCjRckElpgo6OO62NunvKcE-NBZ8l4D2mWsRfdgoaXttri0LafywP-r6o-4N2BirT98xOGoxnN_G4RbQZGtJa84r-FF-07g7Gn8yM_fo_9vGztz9MaaNaSsDT6uEvdTP4CF08PI2zKI2p098A-qpxuJQeDt_YQdSTP9kq-wM0M7YrCkVJZvFd4ek4qxY-OBdkH8pSYsOBTVv7-oDO7iA1RjxG4-wtQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/32ebe18939.mp4?token=kZVkmVgMxFJgKdgeUeLFKNLi4LPdEHTOA6VeaepID9M3F484fWKwCVYTSrUWOVBLqRqlJznUT2gJjLESosWr0E329QGADnpVIPCSqgWM6piLif-PQrIbystUqCjRckElpgo6OO62NunvKcE-NBZ8l4D2mWsRfdgoaXttri0LafywP-r6o-4N2BirT98xOGoxnN_G4RbQZGtJa84r-FF-07g7Gn8yM_fo_9vGztz9MaaNaSsDT6uEvdTP4CF08PI2zKI2p098A-qpxuJQeDt_YQdSTP9kq-wM0M7YrCkVJZvFd4ek4qxY-OBdkH8pSYsOBTVv7-oDO7iA1RjxG4-wtQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ترامپ نادان وسط مراسم ختم گراهام آدامس در میاره به بغل دستیاش تعارف میزنه
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/102249" target="_blank">📅 16:20 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102248">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pm5RepBmAUnP-GJ726CpT8dFKYOl2gNOztqFcbnHZgDefBN8eYGKsSvxm3-Djyxmj5JYKF6x_AbjurzVdTa_d86TrCjm0KKgkdJlgLC74MPMnhC7TxxAErXv31S-nHQpqrR2cD0QNE5VPYoHAs0rHoCy9mn8lmmaJfjHOEAelPLdZFQYPJCMBaRE6y6WHQlUUoUMVkB8_aJx0lofGEEuLMCRBWWvBb18veedIYVw8TH7BzOVRYPKmJuh-kfjENxnE5U1qiH6sm7uZYn0FSeycauUUsug4VFbYgsnpgQ3dDoRPdoNySdZdWJ_NOJVmL_ZDnmDJWV-AtA8s__65ChCrA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🚨
ترامپ در مورد حمله ایران به اردن: حملات شدیدی به ایران انجام خواهد شد، آنها شکست خواهند خورد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/102247" target="_blank">📅 15:57 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102246">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e2de7978a2.mp4?token=g_r421Yezuz8X0o00rv5YQ_V_zWRJJ-VzjgU0HQzAX-vxNdgPYat4vNiwgewL1mAm6RidrNsn1mWa-PaQrUOspcNGKoewTVNOoMEyLlBYJw51PMZSYxUvWLLNnexFTzvlKC1X2v6CavHAETpOJ4BQM7z7nWZjPJGPYQsZn2U1q_X265Xg1ZgMYb3xK_j8OPUOxdAGGmWovgwLnMnPJ4HO7PVpp0YFBowVq8UAkHJvyfnaLbvlxJvxjg2W_MRIaEhdo9PlxpSdpUt5sapp7eDbrIpUh8Cl_rYitanZEDKi_gF51REWkLwJ1nUUz3LvnewHqT3SKCN1Dubn0DnFop3JQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e2de7978a2.mp4?token=g_r421Yezuz8X0o00rv5YQ_V_zWRJJ-VzjgU0HQzAX-vxNdgPYat4vNiwgewL1mAm6RidrNsn1mWa-PaQrUOspcNGKoewTVNOoMEyLlBYJw51PMZSYxUvWLLNnexFTzvlKC1X2v6CavHAETpOJ4BQM7z7nWZjPJGPYQsZn2U1q_X265Xg1ZgMYb3xK_j8OPUOxdAGGmWovgwLnMnPJ4HO7PVpp0YFBowVq8UAkHJvyfnaLbvlxJvxjg2W_MRIaEhdo9PlxpSdpUt5sapp7eDbrIpUh8Cl_rYitanZEDKi_gF51REWkLwJ1nUUz3LvnewHqT3SKCN1Dubn0DnFop3JQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/33130fd550.mp4?token=QPG19AOf23FWaq3QuEd0JfzdtiDhcDzl3FsjQrhSynBhl0TJYoQTRe6Cg98bq9SyXgaac1NzjXIl-KYO2YmhCbzogXn9rDDyQ5htetEfmVqxBojTMENc1bGWvtghrUb8cfkn1fRUsYGyoiOvqB4CCbuILbGdUwJBx6DEOguyNbqwrCDhOTo0H91QpVvDh57d0B0J9FJ2u9Mot2rxZ2eBW-xMC2VtTk5geFGEbiRd4PCas2FjeMrD6g66z1qbSEg7Pp5hLKIuas6wMmDhvmGv378gR4KIiEuE1BPaxGPUfVxxcc0nx6woy5p9HN1En13YsvZKUltDBp97rzz8xjToFwlEvLF8QqhkGPV_KQyYfJ9gmaWydYa0PJ_zpI0i8XakqaurSw_BuIOJFPMLx1yL1LtICUxfZGR3Y4yb8vVPrP67HiZEbhYJKaqFQVj4x04qE1pTmXzNNvqjwEYdbeORnsf4CfZ8VoGhZBVRBCflwnWWE0MKx4PeSsT6ELicykz9FhNOE5d42IjdU7RnKB20tVWzWFqDRWLDOD4l6t9zoVk8ff6MJkyFmWm5LfEnQNB1rDH9C6pCgp9BbRR04sW2ta2xtMFeODB5OnQrgLOrBCpD647uZHodRBI6Nyo40cTDJk2ytfi89fYisEXD3JT-nMP41D9FLPa8iqkLLuGUhlg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/33130fd550.mp4?token=QPG19AOf23FWaq3QuEd0JfzdtiDhcDzl3FsjQrhSynBhl0TJYoQTRe6Cg98bq9SyXgaac1NzjXIl-KYO2YmhCbzogXn9rDDyQ5htetEfmVqxBojTMENc1bGWvtghrUb8cfkn1fRUsYGyoiOvqB4CCbuILbGdUwJBx6DEOguyNbqwrCDhOTo0H91QpVvDh57d0B0J9FJ2u9Mot2rxZ2eBW-xMC2VtTk5geFGEbiRd4PCas2FjeMrD6g66z1qbSEg7Pp5hLKIuas6wMmDhvmGv378gR4KIiEuE1BPaxGPUfVxxcc0nx6woy5p9HN1En13YsvZKUltDBp97rzz8xjToFwlEvLF8QqhkGPV_KQyYfJ9gmaWydYa0PJ_zpI0i8XakqaurSw_BuIOJFPMLx1yL1LtICUxfZGR3Y4yb8vVPrP67HiZEbhYJKaqFQVj4x04qE1pTmXzNNvqjwEYdbeORnsf4CfZ8VoGhZBVRBCflwnWWE0MKx4PeSsT6ELicykz9FhNOE5d42IjdU7RnKB20tVWzWFqDRWLDOD4l6t9zoVk8ff6MJkyFmWm5LfEnQNB1rDH9C6pCgp9BbRR04sW2ta2xtMFeODB5OnQrgLOrBCpD647uZHodRBI6Nyo40cTDJk2ytfi89fYisEXD3JT-nMP41D9FLPa8iqkLLuGUhlg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
احترام به هواداران به سبک لبرون جیمز
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/Futball180TV/102245" target="_blank">📅 15:20 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102244">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/34dd03fd29.mp4?token=ipqHLL8Nddcn-_zjDogaKBeJiuaRFkzG2t8TQ7-7Wt8I73jv1FZU_e3CTviyowfFNEzyeAWNsFw4YRw2U07EI39O26Vk4DL4Rdt4CpNgk6943EI1JSEFeQFFYTqyldPjpxGFcyRXkWjB5TP0KG0D68HIEUo8gyiUAuqTN1NzZWvcR7Z5XiiXps58LpX9OxIekF4XkrYKHlagK-49UKqrsFtl4z17rFotwRBbtTUbf69-HtGDhJ8YifnOYvB8hGt5EmXLXGecNOars98JMwfMhEo9Bbn0VHa9UDgsbHVm-TLhpGad34acdcWIPkRPqO5zG0gQk8BQ1G3saIzP18-ADA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/34dd03fd29.mp4?token=ipqHLL8Nddcn-_zjDogaKBeJiuaRFkzG2t8TQ7-7Wt8I73jv1FZU_e3CTviyowfFNEzyeAWNsFw4YRw2U07EI39O26Vk4DL4Rdt4CpNgk6943EI1JSEFeQFFYTqyldPjpxGFcyRXkWjB5TP0KG0D68HIEUo8gyiUAuqTN1NzZWvcR7Z5XiiXps58LpX9OxIekF4XkrYKHlagK-49UKqrsFtl4z17rFotwRBbtTUbf69-HtGDhJ8YifnOYvB8hGt5EmXLXGecNOars98JMwfMhEo9Bbn0VHa9UDgsbHVm-TLhpGad34acdcWIPkRPqO5zG0gQk8BQ1G3saIzP18-ADA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
یادی‌کنیم از تیزر تبلیغاتی با مسابقه رونالدو و‌ بوگاتی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/102244" target="_blank">📅 15:02 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102243">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9a4c493f3d.mp4?token=aqm1_QQfbQKOK6FZCQT6PtLj_PAFTGIq7s--CmRTEyF1h_foTFY4p8LNhkTdpPb-LZSaI3vBnlSgApgmqTfRdtQGro4sLtu3k2v0ZAmun6m2QmTFC5APM49MLc5E8h1yRYHzYjS3EgpB2ixkfHOixuCYRgGWmnsm3FQbncuwGmZFrbzAvRqBxFSwZCwuc-Drq6_uNQ9m-LOIawAaKd9Oc6yP7oG0w80N_OCNjovh9MdWePMl1NKvmCn72nLKZeHDgBXl80raElXcbs7IoxjbedPDJcLiY2t45-zQ-MmMl1aQfg58z8H6rwjPdliRinzJ5WoTDLfP98MVVnRQGBvObw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9a4c493f3d.mp4?token=aqm1_QQfbQKOK6FZCQT6PtLj_PAFTGIq7s--CmRTEyF1h_foTFY4p8LNhkTdpPb-LZSaI3vBnlSgApgmqTfRdtQGro4sLtu3k2v0ZAmun6m2QmTFC5APM49MLc5E8h1yRYHzYjS3EgpB2ixkfHOixuCYRgGWmnsm3FQbncuwGmZFrbzAvRqBxFSwZCwuc-Drq6_uNQ9m-LOIawAaKd9Oc6yP7oG0w80N_OCNjovh9MdWePMl1NKvmCn72nLKZeHDgBXl80raElXcbs7IoxjbedPDJcLiY2t45-zQ-MmMl1aQfg58z8H6rwjPdliRinzJ5WoTDLfP98MVVnRQGBvObw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
▶️
یادی‌کنیم از مصاحبه سمی محمود فکری
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/102243" target="_blank">📅 14:40 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102242">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/45ed8d40d9.mp4?token=bBX4NPFc29eN1Xfc-gIDRgEUKU29rxJNUBCOeU_6ep9_PPu8R3ifeofxUnAlj7O9gezJtZMgNbn2NzeiJ5qnfQoflZqPsfvGXvptgwT3NzrxFBjmZD-VQmsvhC5mO33WktFO3uctIMQiSvoMS7spZ0liT5ldbVP15UGhqbKGcMmjQh2j4AsYQgaKb5u2wEnIKhHGMEsVgFHKz2UmZFhIgLXKZOeuWZZL9ki0WTd9qblwIj6697uACbDYZ02aonGmeLjjntP9ZAKZheV07KBOgHo-q6TLT-cZQwUZ9BohXX__oal70V3s6eXzj4KG9yv64ou_1cdf1BE6JMwVuvzHM4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/45ed8d40d9.mp4?token=bBX4NPFc29eN1Xfc-gIDRgEUKU29rxJNUBCOeU_6ep9_PPu8R3ifeofxUnAlj7O9gezJtZMgNbn2NzeiJ5qnfQoflZqPsfvGXvptgwT3NzrxFBjmZD-VQmsvhC5mO33WktFO3uctIMQiSvoMS7spZ0liT5ldbVP15UGhqbKGcMmjQh2j4AsYQgaKb5u2wEnIKhHGMEsVgFHKz2UmZFhIgLXKZOeuWZZL9ki0WTd9qblwIj6697uACbDYZ02aonGmeLjjntP9ZAKZheV07KBOgHo-q6TLT-cZQwUZ9BohXX__oal70V3s6eXzj4KG9yv64ou_1cdf1BE6JMwVuvzHM4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
🏴󠁧󠁢󠁥󠁮󠁧󠁿
دوازده‌سال پیش در چنین روزی اوریگی زننده گل تاریخی لیورپول به بارسلونا، به جمع لک‌لک ها پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/102242" target="_blank">📅 14:20 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102241">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e9073a1aea.mp4?token=aoU8hN6RdID1Rizy2Qk9uY_I-OJqOeYA9q__ZU3NFwEefDyxwdBPOUTP_8JsLgImPm6F7PNA_8gCPix8wnYspIqkNXhs9F5IGMkLhUtniE_3GEgeK2qwCsl1MTvwoPkJRGj-pN96n20LImUySNUV4zCeIB0C2YY9Tdt07jRMZOE6XqzqfKyx-1wQsn7Q-y7aLC29iv7Rznym4Spb3ScS8bT7naeeiQM8ou3wJZFZgdjIpLbusGfLzn1in7J4RF1PvAax9966CIFLwrahRj9XT_SlrNPXW2km_wpFOpqkFVXGe7aAlyuUHHovO8iC-Iw7o_5joYrHXQt-EjyvYjNi8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e9073a1aea.mp4?token=aoU8hN6RdID1Rizy2Qk9uY_I-OJqOeYA9q__ZU3NFwEefDyxwdBPOUTP_8JsLgImPm6F7PNA_8gCPix8wnYspIqkNXhs9F5IGMkLhUtniE_3GEgeK2qwCsl1MTvwoPkJRGj-pN96n20LImUySNUV4zCeIB0C2YY9Tdt07jRMZOE6XqzqfKyx-1wQsn7Q-y7aLC29iv7Rznym4Spb3ScS8bT7naeeiQM8ou3wJZFZgdjIpLbusGfLzn1in7J4RF1PvAax9966CIFLwrahRj9XT_SlrNPXW2km_wpFOpqkFVXGe7aAlyuUHHovO8iC-Iw7o_5joYrHXQt-EjyvYjNi8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیو انگیزشی با روایتی‌از زندگی مایکل جردن
💚
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/102241" target="_blank">📅 14:01 · 07 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
