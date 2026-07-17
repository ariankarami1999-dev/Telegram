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
<img src="https://cdn5.telesco.pe/file/K6A6FklcQdvUyDXl4teUjVznMqMGXQmSQjOao1di-qatbIz8PTQdis-hhs-ZOrkoeELgBBHxrjA12DVbCS7bwC299Fn7mfxOtVSl1PkinekO5VmaEeaiT7ZkfqOsT8vkggulucVVNYL0fJ8xgr7eHlyRVTmmWEMGq4bFe_ATH39uCSmVveiqTZVQ5aY7sbpc647Kz8-Wz6AweHVdvGmzm8zvfIuP1Bi-CWeRvExajDXzA3GTsHJKWhMu2ul_FOBq3TEhhTrw35fG5VbUj617Lwa61gEaUx3r7QLzAV6CDU3FZ_Ug1CCMKTP7or7eDNH8Z582IK7C9fZXx5lS6TIEbA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 جام جهانی 2026 | فوتبال 180</h1>
<p>@Futball180TV • 👥 565K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-26 17:40:19</div>
<hr>

<div class="tg-post" id="msg-100634">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8c7ee59734.mp4?token=n3EwFBo4t91j6log9BB1DlqpTTErGkhyAcS99Jw57eH-NLIAKvHjmCrBcaemVmEav89dclrsLMfLeUYEhPVc-91mIk3k25SjUiIxeiAFEmcfcv8OfgTD_sOyRG3a0Jbsqy5ZfgROrIBygzwh7-UjqLmnq94nWYU6PkkDaHv_OGBs89RM7kWvykIK3yWJy69W6KHVKf493QoQClEeilVTBIwoI3z1hxLUMl7a_7K7D01vag4PZ0ZkezUdUUblh62Jkv9Stf_9yDMXM-Et7ZBzM8LE_XEna3xn2a-Tl2WIVAuhFbfvspar4aC9Jdd0h-qTlFLYlCmiWb45PvZlPjQCLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8c7ee59734.mp4?token=n3EwFBo4t91j6log9BB1DlqpTTErGkhyAcS99Jw57eH-NLIAKvHjmCrBcaemVmEav89dclrsLMfLeUYEhPVc-91mIk3k25SjUiIxeiAFEmcfcv8OfgTD_sOyRG3a0Jbsqy5ZfgROrIBygzwh7-UjqLmnq94nWYU6PkkDaHv_OGBs89RM7kWvykIK3yWJy69W6KHVKf493QoQClEeilVTBIwoI3z1hxLUMl7a_7K7D01vag4PZ0ZkezUdUUblh62Jkv9Stf_9yDMXM-Et7ZBzM8LE_XEna3xn2a-Tl2WIVAuhFbfvspar4aC9Jdd0h-qTlFLYlCmiWb45PvZlPjQCLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😆
صحبت‌های بامزه ابوطالب راجب سرمربی مصر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 606 · <a href="https://t.me/Futball180TV/100634" target="_blank">📅 17:40 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100633">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/giJ2srNG5khLszj7cp6H4VlfVV_HQxDoE9jz-oqUdXjiH05oXNhKFg486oFdwZIMJIFcefeT7LFOFtORcsUbzZ2FNyGLSbsSFignpNHxiRDG3wUGiDANg-TwT4q9RH69Tw9UeqPi5bMzJYvXfa7tNT_mTeES7IAp0k8v_G6gP_xK12RzIjTKmX61JId-HAf0GGa61tsu3So8enpcOWEhmdghnI_k7W7fqF6J92NmkyjYGqeOn-Q2p7MFL4rPiQCaqWjgR3I1FDPt1Vy_AZNvpyA-JTaC4M6LFG0PvJ_glSL7Xb_pGGY2RZpOriXft9WHvlLS2-Md0VXWN4Okul1uqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
لیورپول رسماً اعلام کرد که قرارداد دومینیک سوبوسلای را به مدت پنج سال تمدید کرده است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1.21K · <a href="https://t.me/Futball180TV/100633" target="_blank">📅 17:38 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100632">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/47857f07d9.mp4?token=QioU1fSsQ_qdozlMjXP4R0MztEJBt1a-BeqpU6iyEmZCoEH0ByhCzhGXUcU-phQ3n_Qr7aviNld9fcTynDOMPJw4Yrivu3to1gn2o2JVqgE0wwlBx6rpBOQWI_vuJNcnUSeqaM-5uVnrxDdMOWFi4l8HGlftbF9JBiDttVEwyVKX5oyl4CO8urPQMA8V9eXClS3qwQoZDiCl9XWj5J1BRLGQ_2KZWphw5YMYJDeB0BQbL6o96ve4HVbRMh6fVPj-k4J9joFayakuIG_C9Yn4pI_yze1DbGWxYgEjRnDaW1Mx6eHTcZOkjc1tyR9_yhpJT-sC1NMyp5G0KtA63gw-EQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/47857f07d9.mp4?token=QioU1fSsQ_qdozlMjXP4R0MztEJBt1a-BeqpU6iyEmZCoEH0ByhCzhGXUcU-phQ3n_Qr7aviNld9fcTynDOMPJw4Yrivu3to1gn2o2JVqgE0wwlBx6rpBOQWI_vuJNcnUSeqaM-5uVnrxDdMOWFi4l8HGlftbF9JBiDttVEwyVKX5oyl4CO8urPQMA8V9eXClS3qwQoZDiCl9XWj5J1BRLGQ_2KZWphw5YMYJDeB0BQbL6o96ve4HVbRMh6fVPj-k4J9joFayakuIG_C9Yn4pI_yze1DbGWxYgEjRnDaW1Mx6eHTcZOkjc1tyR9_yhpJT-sC1NMyp5G0KtA63gw-EQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
👍
به قول عادل فردوسی‌پور علیرضا فغانی متعلق به ایران بوده و خواهد بود...
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/Futball180TV/100632" target="_blank">📅 17:20 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100631">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fwqp658mOmx3EuKjwWc5B_II6O4445OMmr7UShV4pg1HsE4wDUMAtnV5ipWP8jZctv21wpyDqRIJZ7UvKBJ3HvvERXSkg_pJ0lY4tntHX0Atx_9nrvEmx9ZVTxBsfnsR1x4YLL7623f3weSDqW1aEPxZG_ajwPv-iDU0UCmTrunNNdCAwrT_N34VDAop9KWzGuWJ75JLLF0ncx6Z4avr0bFfNCMF3CmDBpr4PDqV2Zm6WgRkSmhe1w7d2vyXjHq_sIMZJNyn47WJTVgA36BZN47qUunIzZFuX6RY-o19Lc0yXmnlE_IdcDTLaV1L5aqMa43sA_Pm6_fNcq4M_0nsMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
👀
سجده شکر داور آمریکایی بعد از بازی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.63K · <a href="https://t.me/Futball180TV/100631" target="_blank">📅 17:02 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100630">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9beef7a15c.mp4?token=L-eN-43UF3r32AWvUUWAClrid8pWdyVfbEAAivxRitfPJ4a0dhnaigQr6MrEq42COMKzr4fLkjPrmMcob-OvUVhCQoa02_Rk7qS0XYeo_eXlgmrzql0fcnjaKjZyoUzTr2b9TxXZ1xHKJE08E3mXnjwUZ9kcWef5o5gmISL8jYDN8u4qhY16YmwlCAo6rAGib42mTt5pZNIyl0BDXYoeExtFbJO7euPGiwMR5tDi8YkPMy6kQa9_0tgT4WX4fgE6GQ7hjyi86BAV8Cbfelq7CWsRRguHlSkfzeLKdaxak0ReAkxwYx7VtIJ12QibwgR14S_rEe2uDZ8uLsIO1KIDAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9beef7a15c.mp4?token=L-eN-43UF3r32AWvUUWAClrid8pWdyVfbEAAivxRitfPJ4a0dhnaigQr6MrEq42COMKzr4fLkjPrmMcob-OvUVhCQoa02_Rk7qS0XYeo_eXlgmrzql0fcnjaKjZyoUzTr2b9TxXZ1xHKJE08E3mXnjwUZ9kcWef5o5gmISL8jYDN8u4qhY16YmwlCAo6rAGib42mTt5pZNIyl0BDXYoeExtFbJO7euPGiwMR5tDi8YkPMy6kQa9_0tgT4WX4fgE6GQ7hjyi86BAV8Cbfelq7CWsRRguHlSkfzeLKdaxak0ReAkxwYx7VtIJ12QibwgR14S_rEe2uDZ8uLsIO1KIDAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
گلاره ناظمی داور فوتبال: لیونل‌مسی صدردصد باید در بازی مرحله گروهی اخراج میشد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/Futball180TV/100630" target="_blank">📅 16:40 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100629">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e1929090be.mp4?token=ERhFnwgAlktYaoU3gTCPIkyEGG54jRwBZfyZMWdgyhJq3XYweiB3mH45IHPlWM9yY7HWWJm-lSeM6Ee8mXCh7VgfzmdAw_pnuSnlIymfYFFw6y12nLG7VeQVaS4CexBWo1cXXJBQEHszwNE06E_0bEF8EosG3rK-umqdTnB1BVJjOsfX-VH8xkwreYOsE4Oa0uTHnRM2tQNKU5zP8vg8DwjQpiREWlJTg_I3DDODBnTxLIRINpV5Xdo3s6VzNHfDBtaN6ouc83In919RaFwRy5SgvszjNEJLocH3Yzie7BMDdUSot-WhMDLvfX-IgMo-k8o0kOmvx6pveriG2gRPomVvFyG7dBonX5Er-hyu0HH5Z94uWRGSShFFiEO0_Auw3NHwYOYHKLV0Enb8DCogtbc3kehL-9EEgsEFSsD9YRZatSQSfeVnKKQvQe9Zw0PYomoeSZmdXlELAEA2ljXiijm25ISzqBplKayEcPxcGOBWITDL6FEESaAmg-M3tXkTZxiQqlQFDvq62S8CGKOHXc4rYvJwbIJKib3Dg0ihC0FvG6LFUatSrXlGG8BIJfaNkmNDj_eEapGLJ2IdyHWUAdWX_3d3u_aQd-DNSZ74FBZmIxO3lCDuz5ThkeCENTVaS50lLRg6bRC8VDwPpYcqEKWrJXpobdRA8VeV9B4C_LU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1929090be.mp4?token=ERhFnwgAlktYaoU3gTCPIkyEGG54jRwBZfyZMWdgyhJq3XYweiB3mH45IHPlWM9yY7HWWJm-lSeM6Ee8mXCh7VgfzmdAw_pnuSnlIymfYFFw6y12nLG7VeQVaS4CexBWo1cXXJBQEHszwNE06E_0bEF8EosG3rK-umqdTnB1BVJjOsfX-VH8xkwreYOsE4Oa0uTHnRM2tQNKU5zP8vg8DwjQpiREWlJTg_I3DDODBnTxLIRINpV5Xdo3s6VzNHfDBtaN6ouc83In919RaFwRy5SgvszjNEJLocH3Yzie7BMDdUSot-WhMDLvfX-IgMo-k8o0kOmvx6pveriG2gRPomVvFyG7dBonX5Er-hyu0HH5Z94uWRGSShFFiEO0_Auw3NHwYOYHKLV0Enb8DCogtbc3kehL-9EEgsEFSsD9YRZatSQSfeVnKKQvQe9Zw0PYomoeSZmdXlELAEA2ljXiijm25ISzqBplKayEcPxcGOBWITDL6FEESaAmg-M3tXkTZxiQqlQFDvq62S8CGKOHXc4rYvJwbIJKib3Dg0ihC0FvG6LFUatSrXlGG8BIJfaNkmNDj_eEapGLJ2IdyHWUAdWX_3d3u_aQd-DNSZ74FBZmIxO3lCDuz5ThkeCENTVaS50lLRg6bRC8VDwPpYcqEKWrJXpobdRA8VeV9B4C_LU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پشت‌پرده گلزنی تیم فیروز کریمی به پرسپولیس!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/Futball180TV/100629" target="_blank">📅 16:20 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100628">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d7422c46f.mp4?token=Nhy5dchRF2KSYAh2s8KHYMRzhk7mJ16utFR92TSK0A6ExmTitx1raV_vEHRvbm328bj_70Pksx7nvYOsbgU0FRn6ZlTBmBQeX8CKvO04awINgfTKu4Bsee3OmV0t9xZWXi99DeVUmgP1CK_02aMHcffLEMFEbdvYs6WrBi5RkOHiGafJhzUI-maw9QKC3j_J8iHOKQKWC0mo7vXdXvG6UM_5KKMyjaPKnWupfJk04AEZl5GBHDKUHgDvbWisATwCOq7k1SgCz0AAwfutANCcoc1Jzbt4KvFKvtCphLUIK6hfh_76IEfDt6JsNZ0VqW1rynxIk77UjT3YYVKiDE_Xgg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d7422c46f.mp4?token=Nhy5dchRF2KSYAh2s8KHYMRzhk7mJ16utFR92TSK0A6ExmTitx1raV_vEHRvbm328bj_70Pksx7nvYOsbgU0FRn6ZlTBmBQeX8CKvO04awINgfTKu4Bsee3OmV0t9xZWXi99DeVUmgP1CK_02aMHcffLEMFEbdvYs6WrBi5RkOHiGafJhzUI-maw9QKC3j_J8iHOKQKWC0mo7vXdXvG6UM_5KKMyjaPKnWupfJk04AEZl5GBHDKUHgDvbWisATwCOq7k1SgCz0AAwfutANCcoc1Jzbt4KvFKvtCphLUIK6hfh_76IEfDt6JsNZ0VqW1rynxIk77UjT3YYVKiDE_Xgg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
افشاگری کفاشیان از تیم ملی: علی دایی با دستور احمدی‌نژاد رفت!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/Futball180TV/100628" target="_blank">📅 16:04 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100627">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d8f98dd6ec.mp4?token=Ev6YUVd6roZ4Mw0bFFTgnhl2H9aUre05PmvDYmV1hvtqYK7JkrbB1MEJSTdzGMzVs4i8nj3A45m6e9c6x6THthFQV64rI4yHFEbWrqlqSPsPArbTo2z-Fn3gw6ItTsFF0vcATr5GsLcSMQ4G500Vrrfa9QJJSwSwy4gp1fTe9XwuVMxd-n5npA1pOYCpmrEVHQt9JUjj7tqr_QYtS0kWCtQH2eso12cpGUZaUIbmlCC63hfx5ZuILH_L145evP3c2hvUooVDzU7Er49QyetVZUE6h40gmL11IFQul1OMi7_Onob9Di241-g4dAWXpDVbg59TUgWyT6DkUev-KnPE3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d8f98dd6ec.mp4?token=Ev6YUVd6roZ4Mw0bFFTgnhl2H9aUre05PmvDYmV1hvtqYK7JkrbB1MEJSTdzGMzVs4i8nj3A45m6e9c6x6THthFQV64rI4yHFEbWrqlqSPsPArbTo2z-Fn3gw6ItTsFF0vcATr5GsLcSMQ4G500Vrrfa9QJJSwSwy4gp1fTe9XwuVMxd-n5npA1pOYCpmrEVHQt9JUjj7tqr_QYtS0kWCtQH2eso12cpGUZaUIbmlCC63hfx5ZuILH_L145evP3c2hvUooVDzU7Er49QyetVZUE6h40gmL11IFQul1OMi7_Onob9Di241-g4dAWXpDVbg59TUgWyT6DkUev-KnPE3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😆
پیشنهاد ابوطالب به مسی برای دوران بازنشستگی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/100627" target="_blank">📅 15:40 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100626">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🚨
🚨
⚠️
🇪🇸
مارک کوکوریا:
اگر قهرمان جام جهانی شویم، روز بعد با لوییس دلا فوئنته تماس می‌گیرم و به او می‌گویم که دیگر روی من حساب نکند و من با این قهرمانی خداحافظی می‌کنم! چون فکر می‌کنم که بعد از قهرمانی در یورو و جام جهانی، نمی‌توان بیشتر از این جام خواست
‼️
‼️
‼️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/100626" target="_blank">📅 15:30 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100625">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/soy14pmHj2kN3ctuPAj01dNLNL_tWoGgTO7AeM1YIV4FP23Nca4FKRTnQ1pSyvPjfYytF3KKr-IB4urKUTXAfEBuzxgVbzB04Cd9QgoydqFYnQ7H0bTMUac4iKEJ07_3kvHfwqhHEarjwVv1V_7MMhOLPnUm_CDC9fLU1PmhDrXKbS-iumMtLeI5PIP9HwcXJ__v0fUtsmIOGbVYvHbJVlYtg9dSluzcXBmGl2bjEKIFOLJOFr2uxT-W6nSyH9s498lIVX-Log6o5jYj7A_VposfOEUSGCwalwTk5MlzOlEkEH0bHAOHILWm_LH_8q_VsXKaQ9RItGyHxzxWszaWwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
🏆
آرشیو وار درباره انتصاب وینچیچ به عنوان داور فینال جام‌جهانی: فیفا تمام دنیا را مسخره می‌کند. این داور اسلوونیایی یک فصل فاجعه‌بار را در اروپا گذراند، جایی که در مسابقاتی که رقابت و تنش در آن‌ها بالا بود، کنترل خود را از دست می‌داد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/100625" target="_blank">📅 15:17 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100624">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T6FITRaplIQdo6MVg6mJ2e35wjh1PW7pSe6YpIgWpUBK1tQyRMTILvMSbPlJLIiuh_5TgcHiaS72KucPrT6gbprVGpvqKw6MtUnwjbd-LDZLWA_e0i4_zAEtYUXOUlLQdt9i-TboDghK-dU5Lh0iYGHbvjLnZu3J06sfuH91YMH-Iskznif2-9b0iaExdWZjyefzFQlopdhuendvK8tpYZnwfEAxGeAwfqFjVVc84M13VNZcRo5H38Sz-oixteWO02yIl2Cujhs3Lxl8efWzsJ4FV5aRzyYWUR2qm9qL53toGTPjfqLpDotJCjc530jisNn3kfCaJZcZGj8pcy8g8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🔥
تصویر جام‌قهرمانی جهان در شهر نیویورک
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/100624" target="_blank">📅 15:13 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100623">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HK4sy83Byr-6tiYwqZH2iOcR7GOQsEBJ5pJQK3G3f22_VEowqXgoAWU1-q97TpAWRviq-vmibwHJ43K8XSOg942NAkWb_p2oOrqk0etLaLUuL5DZQ5-MrDW5t1zAS3QAI_H1mUDdyb7lxCDj-47jSWKJjxFaorAAIZj0lu-tC7fU9g1VAp_Qced9gdusQq-BfvSQ4wuQU-3wk-F7aJvmbP7W8EkV7EBCS1HOErz1gBetZS0_f5zjgxEmZ3sXPnuK5dcXr06Egautd3YTlZKzEF28iihP0Ux87xNVU6ByzN8dLwG2z8NfHkNr2hFVKf2Imcqcd83B4uUAb6n9Zkc5WA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇶🇦
کشور قطر در آستانه کسب میزبانی سوپرکاپ اسپانیا در سال 2027 قرار دارد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/100623" target="_blank">📅 15:10 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100622">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c-cNLBk4rla9FMMzFPV1NpIPsIpqqIv7_NuDqcc3OQvesYAsjCqUR8TJJjZ5hhcPBCOWWElNFu9eE3235rAGmlNgHoTz0RNIrNAl3e3xyJbWErzgg-yzhD3rxUiEItovX-_9U59cg0BTKc5I0nqs9VPseo9WOMi_YuIAvXEUohKpWZo4Ffr0UQMAc9cuMPwBG1ubd8_PzT4BhyvFBIOxEVO0pXdWBMjtVa3Hoj155aYHgrK6JvfLyP-u_I0AzfZF2okdjyiIo9g2pRCLNHCAn1Q0Vokdqk7uWNah4GTSvEHCWuBx6Ks4Uy4ffxl4CVJprvYzY53osrVa3_pTyn4E9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🎙
رونالدو:
«کریستیانو رونالدو احتمالاً هنوز هم سطح کافی برای بازی در لیگ عربستان را دارد، اما شرکت در جام جهانی بسیار دشوارتر است.»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/100622" target="_blank">📅 15:09 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100621">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromYekbet Support</strong></div>
<div class="tg-text">🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
✅
تسویه فوری جوایز
💥
آپشن های متنوع پیشبینی
💥
کش‌ اوت تا دقیقه 90
🎡
یک فلک متفاوت، هیجانی فراتر از همیشه!
با هر چرخش، همیشه برنده‌ هستید!
🤑
یک‌ بت در صدر بیشترین درصد فریبت‌ ها
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
••••••••••••••••••••••••••••••••••
💠
لینک اخبار و هدایای سایت
👇
👇
🔸
https://t.me/+ioIBrQfqMLtmMmEy</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/100621" target="_blank">📅 15:09 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100620">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromYekbet Support</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EZlBJTHLvNMqZ60o_yous-NehCHxFMGfKaGXgKYxt_4RiKi515MsFRoN4jKtpGvdLtTlwC3kAyudv9h68u3iIQoO5qzc_IgDUbbXtpd1WTyb0KgX7QLCFVgBlAzh1X7UU1YdUaiDY7BuGO4luVvFtVBaQXF15ykycKptlZ8qZBVnAjq-Nh7fYPsE7NYs4NDA9H5hKjArtNuOF_RPRYXT1hEbPL5sqG8FKLbklD6I8bAr9ejByPBAJ8yqqADzla7PzjXxFlbKrf6bek-uupd-Yqwg41fRY7AerSuT90v4Io-zLEGCli-o_0tcqfA72GYDRtwuOTTtwu2ef53WMbBsHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💎
سایت پیشبینی
YekBet
💎
🎁
جمعه و‌ دوشنبه‌ های فوتبالی با بانس 100% میکس ورزشی تا سقف 30 میلیون ریال
🔒
واریز و برداشت با سریع ترین و امن‌ ترین درگاه مستقیم
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
📲
@yekbet</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/100620" target="_blank">📅 15:09 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100619">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/abc262a80e.mp4?token=rte2GJvYmCxLPAOQ9Jkg5Q1CZrII3qPAJuVRUxf7nBmSi-7VHtNCWqtymXsQ0SL00hMmdcs52-7DUCBVEHsPl6laap8YDYUtyibiB3HXejLOzzNGJJcQgNvJhQjFq9xpZ-OZ-kDudmlU5ZV3EH_Ma0dbmponOnMFaULgNjK7E5YrAlx075o2Du4qA7iWDEqQJgZ0hkZ1ArX4X8zQ5qOIkJrNbM1391HJBhoGmgCeViXud-oOVko5GMvzebnrvpcVQhzaeYytmAxWkJNjh-WrXmsY6kva2D-3S8KpZ6UHE7yirZZjbdBLr0FXoME_-Mqik-9kE89NrCsKg5LRPp71dg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/abc262a80e.mp4?token=rte2GJvYmCxLPAOQ9Jkg5Q1CZrII3qPAJuVRUxf7nBmSi-7VHtNCWqtymXsQ0SL00hMmdcs52-7DUCBVEHsPl6laap8YDYUtyibiB3HXejLOzzNGJJcQgNvJhQjFq9xpZ-OZ-kDudmlU5ZV3EH_Ma0dbmponOnMFaULgNjK7E5YrAlx075o2Du4qA7iWDEqQJgZ0hkZ1ArX4X8zQ5qOIkJrNbM1391HJBhoGmgCeViXud-oOVko5GMvzebnrvpcVQhzaeYytmAxWkJNjh-WrXmsY6kva2D-3S8KpZ6UHE7yirZZjbdBLr0FXoME_-Mqik-9kE89NrCsKg5LRPp71dg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این صحنه عالیه. عادل غیر مستقیم رید به پیروز قربانی و تهش داشت از خنده میمیرد
😂
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/100619" target="_blank">📅 14:46 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100618">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4d3da3a81c.mp4?token=FMxZuHb4LROtf-3eqKIGcg8drC2W1VieysMgqCXBJVwYxFhkm2Q-VD7KTLoiJbE7QB2ad9YPnvbZr-9XHtNXozjQJDT0nh8eQIOkB4kLeCdh4oRhf85m6vTYSWa3zov1z5u4eGuB5lU6QJwQfQZ_VDOIETpaK44rPNICpv_a7UTHtjts1Oly2iZT5sQqTLoTqRUwStIv2F4BgVoPjFscreFc8rpGTmSWmYucpxKo0TPB5qV4PWVOHmW54MoIEpr-m2X13qEL06Xw7Qus3HmN6c55F4oEVEZEpLfK4M_jra4pp5KY-Vq2FInZ1DmUXrPGA5r7stKgO0vosoe2biTM5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4d3da3a81c.mp4?token=FMxZuHb4LROtf-3eqKIGcg8drC2W1VieysMgqCXBJVwYxFhkm2Q-VD7KTLoiJbE7QB2ad9YPnvbZr-9XHtNXozjQJDT0nh8eQIOkB4kLeCdh4oRhf85m6vTYSWa3zov1z5u4eGuB5lU6QJwQfQZ_VDOIETpaK44rPNICpv_a7UTHtjts1Oly2iZT5sQqTLoTqRUwStIv2F4BgVoPjFscreFc8rpGTmSWmYucpxKo0TPB5qV4PWVOHmW54MoIEpr-m2X13qEL06Xw7Qus3HmN6c55F4oEVEZEpLfK4M_jra4pp5KY-Vq2FInZ1DmUXrPGA5r7stKgO0vosoe2biTM5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عادل فردوسی‌پور بنده‌خدا ذهنش هنوز تو برنامه ۹۰ گیر کرده
💔
❤️‍🩹
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/100618" target="_blank">📅 14:20 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100617">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5cfcde07f6.mp4?token=dMn1NDRAXZZND75Uz8KtzwtdLx8LICjtclBzdRj1aLe3gFmBKdT2SXKY9kEXCqTq_jOFvf8egyG7DAiRCodLy9WnoASJkcRFQ5vDuEIdqARgPm7kK56NyTJyg9nNZby9aLv7u0i3bJYQ_Luq6fh_Fgzky-y1W-aqjCgtylAYlCpmv-MnYa8_lkn6dsy3oToplPDHl1YP1dgwp7a22g5BYKLPBZ5xEtT3_v_khKOoA_NR3Vs34tK7wSjkNuNqtLXz4pJAdtDcqLTDbPChdU0oIBIf0QYFRKvo-QewORGiRiia7ruB69ry4aJ5bnQpE9sm5SPkpkZjXgbeaTOsWT4Azw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5cfcde07f6.mp4?token=dMn1NDRAXZZND75Uz8KtzwtdLx8LICjtclBzdRj1aLe3gFmBKdT2SXKY9kEXCqTq_jOFvf8egyG7DAiRCodLy9WnoASJkcRFQ5vDuEIdqARgPm7kK56NyTJyg9nNZby9aLv7u0i3bJYQ_Luq6fh_Fgzky-y1W-aqjCgtylAYlCpmv-MnYa8_lkn6dsy3oToplPDHl1YP1dgwp7a22g5BYKLPBZ5xEtT3_v_khKOoA_NR3Vs34tK7wSjkNuNqtLXz4pJAdtDcqLTDbPChdU0oIBIf0QYFRKvo-QewORGiRiia7ruB69ry4aJ5bnQpE9sm5SPkpkZjXgbeaTOsWT4Azw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
🇦🇷
خلوت اسکالونی با خودش در نخستین تمرین بعد برتری قاطع مقابل انگلیس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/100617" target="_blank">📅 14:02 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100616">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3127a14b81.mp4?token=J0AAh3VAm_UWCrBzRYpmBmgKS6NCeHmlXz-5g0wv3RrMwF1RImsyDN5dJLlA1_COdWms8N8F6vGuA3MFR3vRzFvEahlDNkuLfrU700mE0zQNDQhxCBL_wnH0PqFWyDDQxlCO4KRUT3HFcuq1XIEvWtKtKpljrgd8-A4wB8I7-2LZCURxsuU-9Ku0Rg5b0G5B5ttigOIoLf_xzkguG85kQsBcHmyjOXAgOs4XB4m5dK854uBcuWuBbMpeO8QnJXdO57L4_2Ef_8r8jacKSqijW3yZExA9ZvU6Sif9FkAjfmRfylqCE6aPiBqtjvtMkb5awkB-W_P4xoAjRAjwULdGwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3127a14b81.mp4?token=J0AAh3VAm_UWCrBzRYpmBmgKS6NCeHmlXz-5g0wv3RrMwF1RImsyDN5dJLlA1_COdWms8N8F6vGuA3MFR3vRzFvEahlDNkuLfrU700mE0zQNDQhxCBL_wnH0PqFWyDDQxlCO4KRUT3HFcuq1XIEvWtKtKpljrgd8-A4wB8I7-2LZCURxsuU-9Ku0Rg5b0G5B5ttigOIoLf_xzkguG85kQsBcHmyjOXAgOs4XB4m5dK854uBcuWuBbMpeO8QnJXdO57L4_2Ef_8r8jacKSqijW3yZExA9ZvU6Sif9FkAjfmRfylqCE6aPiBqtjvtMkb5awkB-W_P4xoAjRAjwULdGwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
🙂
خاطره خنده‌دار شیدا خلیق از خیابانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/100616" target="_blank">📅 13:40 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100615">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ef1022d87.mp4?token=pqQ6xC2Ek0RmgjONvqUomqy_9qAlvmLU4MDWlBifHKobo4keZt98PjWxgkQHrz-0z-uOlVEPXX2D3u9N4ljPe6hXZqcaFROF77oplY3Qj422B9BJ7DboVPLv_B9XYlkj03Huv1FeunvhA6Qr0iQqYo6QEFz5amjoV9B8T0CBuUZqAX5RHFVvUmoc6xt6sReqIesurd-ntztsrlWGEuKnLvlIY-S6_u0sGrmfSdXCVeP-DnB5RgVdC3Nbu9w7YDe_1ET-yFSEj4LW3uUoCCHL886q_sdMVQ3AX3Ozk6Ho7D9YdD2br6xM9LXKCyNY_6uCmsag-2JN6saGxi-XH6D6bQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ef1022d87.mp4?token=pqQ6xC2Ek0RmgjONvqUomqy_9qAlvmLU4MDWlBifHKobo4keZt98PjWxgkQHrz-0z-uOlVEPXX2D3u9N4ljPe6hXZqcaFROF77oplY3Qj422B9BJ7DboVPLv_B9XYlkj03Huv1FeunvhA6Qr0iQqYo6QEFz5amjoV9B8T0CBuUZqAX5RHFVvUmoc6xt6sReqIesurd-ntztsrlWGEuKnLvlIY-S6_u0sGrmfSdXCVeP-DnB5RgVdC3Nbu9w7YDe_1ET-yFSEj4LW3uUoCCHL886q_sdMVQ3AX3Ozk6Ho7D9YdD2br6xM9LXKCyNY_6uCmsag-2JN6saGxi-XH6D6bQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
لامین‌یامال و زیدی بعد از برد مقابل فرانسه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/100615" target="_blank">📅 13:40 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100614">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/206dd79518.mp4?token=qk602WPrfj_CEqo8rPScWIuqujRGXqg1Tfqook1_EZ4kCQ6Uf-73KZAkhDxZ9HjrObQKBYgVflDeZaJpEqForhnmRqLoBZZfHltIzSMEY5KjSS91NLxfAdg06yCYG4Pb0HPdFqqPIIstum641t5LItQclVuHuf_KSmOf2gMi5t7PMsN6xkAesvgrXRfemCs0p9jIvYuNEVjgeV2qfw4mjUvqK6BLVmRuBkd_eniwttkv0d0aqf4kJ_W4Uins2CchxQ6cbYtbPAyHrn2ODeuqcN8j6IWsm1lGd2_Nyq84-Bk7ymdQcfOOGrm6izVUEFhWTGF-5DGnkLpAVU5b0MhKtmNaWF1IH5jAOIRFDSq9U4PdYaKfNIfosPhfOw60e7sllKiwia5s9ni7YSSU0ePIza_wMhRjB1aQlLy9oB26Ckw5csWSFKSD-Zz_I3q9B4KFONz86i2xuTIt6zXyDFWTjVVXfd6wocu5xW1M5bj-r60UDYDvKS1Oxei3rUpZGKe4PBklKVdPK3krdLcpf9By2_t5M7Mid-qfzCIohEq1KhjEY4nwqLMSIgo48VqT8kD2HRzxUbQZyY9okv9UgA36PrH1SW-sNfeGJH6m3J-NI9dibdIeJ3ZGgC7rIgrVkeh_1XDUNin3lUkigmTcoIVcVi5ND54yBybE7mqQYKkHjDs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/206dd79518.mp4?token=qk602WPrfj_CEqo8rPScWIuqujRGXqg1Tfqook1_EZ4kCQ6Uf-73KZAkhDxZ9HjrObQKBYgVflDeZaJpEqForhnmRqLoBZZfHltIzSMEY5KjSS91NLxfAdg06yCYG4Pb0HPdFqqPIIstum641t5LItQclVuHuf_KSmOf2gMi5t7PMsN6xkAesvgrXRfemCs0p9jIvYuNEVjgeV2qfw4mjUvqK6BLVmRuBkd_eniwttkv0d0aqf4kJ_W4Uins2CchxQ6cbYtbPAyHrn2ODeuqcN8j6IWsm1lGd2_Nyq84-Bk7ymdQcfOOGrm6izVUEFhWTGF-5DGnkLpAVU5b0MhKtmNaWF1IH5jAOIRFDSq9U4PdYaKfNIfosPhfOw60e7sllKiwia5s9ni7YSSU0ePIza_wMhRjB1aQlLy9oB26Ckw5csWSFKSD-Zz_I3q9B4KFONz86i2xuTIt6zXyDFWTjVVXfd6wocu5xW1M5bj-r60UDYDvKS1Oxei3rUpZGKe4PBklKVdPK3krdLcpf9By2_t5M7Mid-qfzCIohEq1KhjEY4nwqLMSIgo48VqT8kD2HRzxUbQZyY9okv9UgA36PrH1SW-sNfeGJH6m3J-NI9dibdIeJ3ZGgC7rIgrVkeh_1XDUNin3lUkigmTcoIVcVi5ND54yBybE7mqQYKkHjDs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🏴󠁧󠁢󠁥󠁮󠁧󠁿
فراز و‌ نشیب لیونل‌مسی در بازی انگلیس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/100614" target="_blank">📅 13:20 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100613">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ae03b39787.mp4?token=Vs2CwBpSfuXqOk5qNy1cZFyB1DQ3YvAzxpiU-qPbphh5S1XSN8ZJ4z-bkX9Dc3turru1U0210E2CQMhgGfxyvhakRsGuaJhrJyEWJ6znOtYIK7UmgenRlMm11Z-bXsLV-PMZHKww1okCeqsseyiawxLKtT9s3fZ6siZD-T61FVn_IXpA0ZcbH1rAevvOQibVp33l3NjFFddbv0eeklKEE57kILRpZPc_Kzb2TRs0ez-5-HORGbtaOZFdSacYNwLVVCmNfvWRoAyZ2Fd0JYtJ9VbU-NoH-VDgHWCtZ8QrZMBd8Q5CFiWp9EL79UmFL0NyKDmVvfoRvZjy8ITS06ZQJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ae03b39787.mp4?token=Vs2CwBpSfuXqOk5qNy1cZFyB1DQ3YvAzxpiU-qPbphh5S1XSN8ZJ4z-bkX9Dc3turru1U0210E2CQMhgGfxyvhakRsGuaJhrJyEWJ6znOtYIK7UmgenRlMm11Z-bXsLV-PMZHKww1okCeqsseyiawxLKtT9s3fZ6siZD-T61FVn_IXpA0ZcbH1rAevvOQibVp33l3NjFFddbv0eeklKEE57kILRpZPc_Kzb2TRs0ez-5-HORGbtaOZFdSacYNwLVVCmNfvWRoAyZ2Fd0JYtJ9VbU-NoH-VDgHWCtZ8QrZMBd8Q5CFiWp9EL79UmFL0NyKDmVvfoRvZjy8ITS06ZQJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
پشت‌صحنه تصاویر پیج همسر لیونل‌مسی :)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/100613" target="_blank">📅 13:04 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100612">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a39dd16f5a.mp4?token=Q4IrIaIO_KhYG-YA-fdb6iJsQVW1EUm8k9gxgFodt16jg3d5UDtomITQIwn5DL9Qpgy97CJ4I-hBQhv06Xx_5tKUTJmbvNxhbVlkcEB4tS9fNmjXBvu1xjHU1oL3uQDgW5i2u8whtqU4DKfEfcLfVvkqEzRlUnFgCtl2q_UalXY_iPE0PGdE5GUu9WHp_gSizG65aFpZ6Iuh_4Co8uz44AyjP5HMfx9KztC7do1Om4N3We4E1JsL5QmdALR4xqlGn-joYhJ9NSPkzjfknZ14ipCDRZGIxQQQwbwVbYkavlnsXo3shLq2-KNOsPES83FUF9ggSpyUwpu3vQI7NKACXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a39dd16f5a.mp4?token=Q4IrIaIO_KhYG-YA-fdb6iJsQVW1EUm8k9gxgFodt16jg3d5UDtomITQIwn5DL9Qpgy97CJ4I-hBQhv06Xx_5tKUTJmbvNxhbVlkcEB4tS9fNmjXBvu1xjHU1oL3uQDgW5i2u8whtqU4DKfEfcLfVvkqEzRlUnFgCtl2q_UalXY_iPE0PGdE5GUu9WHp_gSizG65aFpZ6Iuh_4Co8uz44AyjP5HMfx9KztC7do1Om4N3We4E1JsL5QmdALR4xqlGn-joYhJ9NSPkzjfknZ14ipCDRZGIxQQQwbwVbYkavlnsXo3shLq2-KNOsPES83FUF9ggSpyUwpu3vQI7NKACXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
کنایه‌های سسک‌فابرگاس درباره سرمربیانی که پس از زدن یک‌گل وارد لاک دفاعی میشن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/100612" target="_blank">📅 13:03 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100611">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EbCZPPPjRYbyQ00KX-9_kC1BaoyJWvcF3eKxmTXpJCFhHIPOUM5j0nKuYCF2ctJhyQUkrE6iobAUNRum6ndGC4KEjGKpRlTWUiQlCje7hNeuYxLRNmHDLWahvQoohrsJzGy_pp9gwIqUC4bgx67C4wb-DmaTwUjuc_Yx4xCA6OlgCj9wPvTIA_RMCLQr3OGlc_ciq89IJ1mYgFZjuW8GeFDxm_Mx6MSR4acGMB34pEiMQklsqvQRmJErkNuufbzOHmv_4BGOZ7o-20hSaf3IqNyLS7PJN3-9bH49CkpSxizeXjh4oo-nkGb4J_s78Hp5syrWwBeCevTBiV4epNC78g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
با توجه به صعود انگلیس به نیمه‌نهایی جام‌جهانی، بند فسخ قرارداد فدراسیون این کشور درخصوص قطع همکاری با توماس توخل از بین رفته و اگر سه‌شیرها بخواهند توخل را برکنار کنند، باید کل مبلغ قرارداد وی را پرداخت کنند هرچند تصمیم بر این شده که توخل حداقل تا یورو ۲۰۲۸ ابقا شود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/100611" target="_blank">📅 12:50 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100610">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b380c91827.mp4?token=UZazAln6nHBj7hEw9_1r6VBJDKCBO95iFkyKKGZpECqQTLmCT766jvNqZm4PRxsFPdvI1H8JX8JaHCj0CFLfgy_dgrpnlp22cXotACk1lXRU7-is7RfTlG2HrJM7vWZD3KetDPp2yPSAotlu5XJpKciP44BaOOHsJHswXpIT_mNdZ6NK3ITl7SMZIKPuCUsBII4aVLtIP46zIcFYovcTD9Ahm5IFD_Qh0PBH5gYJjX_-UWHGu8WgFwD1TFbFqFR6G1koUG3XF74O24qQzbVkp8VnT2plYZxJClx6VWT1cNrlXspwL8AqSIHgducfc9yz3C8f4REYLie4T2WAN6968g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b380c91827.mp4?token=UZazAln6nHBj7hEw9_1r6VBJDKCBO95iFkyKKGZpECqQTLmCT766jvNqZm4PRxsFPdvI1H8JX8JaHCj0CFLfgy_dgrpnlp22cXotACk1lXRU7-is7RfTlG2HrJM7vWZD3KetDPp2yPSAotlu5XJpKciP44BaOOHsJHswXpIT_mNdZ6NK3ITl7SMZIKPuCUsBII4aVLtIP46zIcFYovcTD9Ahm5IFD_Qh0PBH5gYJjX_-UWHGu8WgFwD1TFbFqFR6G1koUG3XF74O24qQzbVkp8VnT2plYZxJClx6VWT1cNrlXspwL8AqSIHgducfc9yz3C8f4REYLie4T2WAN6968g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
شوان‌اشتایگر اسطوره آلمان بعد صعود آرژانتین رفته بین مردم شادی میکنه
😂
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/100610" target="_blank">📅 12:40 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100609">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c98bab1d3b.mp4?token=oFyledJKZEL9opCTqM-lrXJG1OH8jKaPqgaU9JT04RUnTKv3kUD1xeyLQelYCPQEyz-CBk3966TEfCASO6TVJ4BBkUE0KR2-HlrlUbv_fnF2c72F-K5ozPOQVaKdj_eFZUkGZ3kI4WhRm0aqJRDO6jyXCc6oiQyBLASp8GkfBQYvKTeC04Di5m-KdF8exJ06fcuD-hL1-OZjXmPGLAuWi11ruZ7Qg6VzMP3gdtj06Xhrke94Inn76y5FmTlewyxtTuhSsDlpMqoeful-sjis0whgrmhvgxtYho7UEX7hlOMw6SRI5jkK99eL8DQbQ81EsbtqE5yve-Es1npBLI4NZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c98bab1d3b.mp4?token=oFyledJKZEL9opCTqM-lrXJG1OH8jKaPqgaU9JT04RUnTKv3kUD1xeyLQelYCPQEyz-CBk3966TEfCASO6TVJ4BBkUE0KR2-HlrlUbv_fnF2c72F-K5ozPOQVaKdj_eFZUkGZ3kI4WhRm0aqJRDO6jyXCc6oiQyBLASp8GkfBQYvKTeC04Di5m-KdF8exJ06fcuD-hL1-OZjXmPGLAuWi11ruZ7Qg6VzMP3gdtj06Xhrke94Inn76y5FmTlewyxtTuhSsDlpMqoeful-sjis0whgrmhvgxtYho7UEX7hlOMw6SRI5jkK99eL8DQbQ81EsbtqE5yve-Es1npBLI4NZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
همسر لیونل‌مسی سرمست از برد کشورش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/100609" target="_blank">📅 12:20 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100608">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f788b2d6e.mp4?token=P1i8DYLRfI84-iGizxUAKqqVTbAvfFjM5xsKxm2bp0zY_HWdk1EomA-xlAGyTK8Q0HAyXeDpqnLb8aKl2nzvjvFGDBIbQtbSoHPWhSEyOYrjHWevUWgr1aTJLe3njNyyWcrXFSj3ypV4b_5UrKanC1r_Fco3Kl62IUpZosx2H_LdwB4MVFkLQlQd9q8HC-CkBCrQ3YiUvQgRmSC_G1zkPKHvBorXWFHVufH4c2ylyWvxDMnmcA3RZPC4stUGVFBtnpjXe7I5iWO_rC_kb1vTlOxNB9B0WqtMI06hTMbeBz4aNVyYvLzkOOMHEJmqWIgnGja1qmDpEZNNZ16t43lp2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f788b2d6e.mp4?token=P1i8DYLRfI84-iGizxUAKqqVTbAvfFjM5xsKxm2bp0zY_HWdk1EomA-xlAGyTK8Q0HAyXeDpqnLb8aKl2nzvjvFGDBIbQtbSoHPWhSEyOYrjHWevUWgr1aTJLe3njNyyWcrXFSj3ypV4b_5UrKanC1r_Fco3Kl62IUpZosx2H_LdwB4MVFkLQlQd9q8HC-CkBCrQ3YiUvQgRmSC_G1zkPKHvBorXWFHVufH4c2ylyWvxDMnmcA3RZPC4stUGVFBtnpjXe7I5iWO_rC_kb1vTlOxNB9B0WqtMI06hTMbeBz4aNVyYvLzkOOMHEJmqWIgnGja1qmDpEZNNZ16t43lp2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
نمایی از استادیوم محل برگزاری فینال جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/100608" target="_blank">📅 12:08 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100607">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a2249840ef.mp4?token=jp4ndBNqjS5cjUNjT21bNnjtb733JFLB8LMUW7ctQcE4okcEEA0-Bq1u6r4SkGBleJ_oMUTArGYHQqDai5KuS_9j_8lCeIcxB-g_zGgqYUEaijzp93ACW0ROplDlnFiK_p1aMYI5GyxuThgDpAYW83Ip59IDE9kH0HIV85v8uyOL0nQ24VTV-fybafM8nX1uFN3FblUgsyLTrc1phvnMMGKyHMvOE6evTz6k1bg468HfOmTydd4Gj8KaNaICe-8BcwDVlzpFk5Df0bHM5a2dMIy2lFUBN8AmHqOf8rpCM8YztrJAvB_ZZXGP0zkFoyxoRO84cQeu4Y1Nhye18u-aDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a2249840ef.mp4?token=jp4ndBNqjS5cjUNjT21bNnjtb733JFLB8LMUW7ctQcE4okcEEA0-Bq1u6r4SkGBleJ_oMUTArGYHQqDai5KuS_9j_8lCeIcxB-g_zGgqYUEaijzp93ACW0ROplDlnFiK_p1aMYI5GyxuThgDpAYW83Ip59IDE9kH0HIV85v8uyOL0nQ24VTV-fybafM8nX1uFN3FblUgsyLTrc1phvnMMGKyHMvOE6evTz6k1bg468HfOmTydd4Gj8KaNaICe-8BcwDVlzpFk5Df0bHM5a2dMIy2lFUBN8AmHqOf8rpCM8YztrJAvB_ZZXGP0zkFoyxoRO84cQeu4Y1Nhye18u-aDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
🏆
ویدیو وایرال شده از گزارش بازی آرژانتین و انگلیس توسط یک پدر ایرانی برای فرزند نابیناش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/100607" target="_blank">📅 12:00 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100606">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3961697c2d.mp4?token=ABigseJz6Ol9DRK_-QduetfvvmkIuw9w5PkwtWnceAU91SZTilDbceS06qOgEc7kn-SgBvm2QY4Po8tguTxZjdaNQyAD0cIpeo-q7ZHbtJmicNvtH_Fy8hgdOTECHedEYR4kr4j5grRvs0y-5t9f53wvMzfkpLVEUUVw8WKPeC58QWsokSLlJvV8o85ywunXTtk9MfudeLZqgtmyH0QqpzwagZ4O_ZmeczPh5pSFU1O233oidBzNiNs5eDHmahSqPiQAgxRb5UzdczuW933pFdHg1EsR7m8P_Sm-C221miJSwasL1rx6_Ewmc7uhqCj6Yk0vyaIsYIuh9XvH_8ODpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3961697c2d.mp4?token=ABigseJz6Ol9DRK_-QduetfvvmkIuw9w5PkwtWnceAU91SZTilDbceS06qOgEc7kn-SgBvm2QY4Po8tguTxZjdaNQyAD0cIpeo-q7ZHbtJmicNvtH_Fy8hgdOTECHedEYR4kr4j5grRvs0y-5t9f53wvMzfkpLVEUUVw8WKPeC58QWsokSLlJvV8o85ywunXTtk9MfudeLZqgtmyH0QqpzwagZ4O_ZmeczPh5pSFU1O233oidBzNiNs5eDHmahSqPiQAgxRb5UzdczuW933pFdHg1EsR7m8P_Sm-C221miJSwasL1rx6_Ewmc7uhqCj6Yk0vyaIsYIuh9XvH_8ODpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
⚠️
کرم ریزی بارکو بازیکن آرژانتین که باعث شد بلینگهام کلش کیری بشه یه پس گردنی بهش بزنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/100606" target="_blank">📅 11:40 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100605">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e7414ff88.mp4?token=B1-eFJVOhSdbENJ5lU2fvBiYU1_PU5uSIMirYjdvC8azjdnNk4zdIEawztaZBJQMZFMtLl_2xdVaq6edjYBYsxG3xRcnttakmSYx7UkAQvr0eZXEdwAOFuGj0fAxhj0cbJgMDsIfgprwvgnhejVWulDN0SnuB1OCdbLEmtUbODPLe7wiKxYoDaeVL8xN5HOEBSRp3qqqUtTqBU5Fh39VEgK3XjudxpNVKfHbXMX7DalX4ht96jF8FIE4Sck0DqQWkNA4KlV1ydA1uYD4GtTqG-FR70JxyL5p_1YYO1Mx14v8ATmmkZT9W4v5PpBkAWx0GTmGYcxOGiZlRsOU6kTtkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e7414ff88.mp4?token=B1-eFJVOhSdbENJ5lU2fvBiYU1_PU5uSIMirYjdvC8azjdnNk4zdIEawztaZBJQMZFMtLl_2xdVaq6edjYBYsxG3xRcnttakmSYx7UkAQvr0eZXEdwAOFuGj0fAxhj0cbJgMDsIfgprwvgnhejVWulDN0SnuB1OCdbLEmtUbODPLe7wiKxYoDaeVL8xN5HOEBSRp3qqqUtTqBU5Fh39VEgK3XjudxpNVKfHbXMX7DalX4ht96jF8FIE4Sck0DqQWkNA4KlV1ydA1uYD4GtTqG-FR70JxyL5p_1YYO1Mx14v8ATmmkZT9W4v5PpBkAWx0GTmGYcxOGiZlRsOU6kTtkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسلاوکو وینچیچ همون داوریه که امسال در بازی رئال بایرن یه کارت زرد سخت‌گیرانه به کاماوینگا داد و بعد فهمید کارت زرد دومشه و‌ اخراجش کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/100605" target="_blank">📅 11:33 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100604">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e3ceef1f3.mp4?token=WvgnGmG-Qe__TC2HwJnYsCYA-0SqS--CXvzzX_hl1WLk-2QEWAo8Km73HqsskS0HT5hbK9XcIlfDptT5oT0kDxykyzvgdyXuVbcp7-SF9ufP072Xf0s5wTE96RX_NyU-Z3cxgKf7gCh2q42ubbl2IOXMRUVcD3CI3_hzQdzL47tX5tMWBOfwltZtDe144obCm_9f2jVyzX22DbcYE3QuZ2atbb07Hq3aZbvISM_pWgwvUl8gknTxMSJmRLJWY2KPAYzS9M_ZtBuzt7l44eULZsqUJ4xqii4p7G8pF9f8Gy1WByBj5vcp-lGq5gwhB0baP2E5kMk_CcfCf98XCgiuy5f0a7BzLJ6-aI9e3N02KSLc0CSK61mds733iXC9y3jx_Vkz266p11iZzu61VnFMdytNz8vmps26JlgaSALzeKoc95MVq5X_KyaNM86m-3s_yJhR-sYkpJECWTue7UG8A4p77V16QpF9WECB49c7iqcu-2N04IbuG-y5i4478Uhb5wNDJ3cVvrQse8lGiWyl_1ZOBcQgDw_3ztK0j5kACNtXtM0sFsJwvqWec8C0-ay5vp9Xpt_JskDXWDCthm_5ODMr6cdz5hLgjqbvo6lKD-ZeM1P_WCCTxDn1R-cLTOqdkPt8lVQ_wWdXdGgPS3OH8MXuFAt7W_z00aE_ibZbTYY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e3ceef1f3.mp4?token=WvgnGmG-Qe__TC2HwJnYsCYA-0SqS--CXvzzX_hl1WLk-2QEWAo8Km73HqsskS0HT5hbK9XcIlfDptT5oT0kDxykyzvgdyXuVbcp7-SF9ufP072Xf0s5wTE96RX_NyU-Z3cxgKf7gCh2q42ubbl2IOXMRUVcD3CI3_hzQdzL47tX5tMWBOfwltZtDe144obCm_9f2jVyzX22DbcYE3QuZ2atbb07Hq3aZbvISM_pWgwvUl8gknTxMSJmRLJWY2KPAYzS9M_ZtBuzt7l44eULZsqUJ4xqii4p7G8pF9f8Gy1WByBj5vcp-lGq5gwhB0baP2E5kMk_CcfCf98XCgiuy5f0a7BzLJ6-aI9e3N02KSLc0CSK61mds733iXC9y3jx_Vkz266p11iZzu61VnFMdytNz8vmps26JlgaSALzeKoc95MVq5X_KyaNM86m-3s_yJhR-sYkpJECWTue7UG8A4p77V16QpF9WECB49c7iqcu-2N04IbuG-y5i4478Uhb5wNDJ3cVvrQse8lGiWyl_1ZOBcQgDw_3ztK0j5kACNtXtM0sFsJwvqWec8C0-ay5vp9Xpt_JskDXWDCthm_5ODMr6cdz5hLgjqbvo6lKD-ZeM1P_WCCTxDn1R-cLTOqdkPt8lVQ_wWdXdGgPS3OH8MXuFAt7W_z00aE_ibZbTYY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
❌
ویدیو ساعاتی‌پیش از ترافیک در مسیر لار به بندرعباس بدلیل تخریب شب‌گذشته پل ارتباطی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/Futball180TV/100604" target="_blank">📅 11:21 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100602">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/56ec89ae70.mp4?token=IsaV3mILGRbyGsFdyM8tzJy94CJpc8ao5POOklMrIRvaKz2PpfJJtNOQZkD0aDB6egbzBC6MBejgmH9DDq2hCHN95-GsTmfKADZLtTgdBrtp6Z1kH0PdukKIuIDFyeXJcosdDOPYa9BxDgRYiZYpNFLa5LfdLLQixG3cZ38fmhg9669hVk85_U88qIkZBr45UokTxd7HhvhsmYCRIy0BAPRx7F2W6ln2_WK0NvdAy8mT41dd_rar6k51t2DiTsWhV0JKRsb7mHOO79eUV6Hd6zjBaju4AIuc-jO9JYhuqmIo36H9g46RfvIQodUW-JjoEMvUI0s6hKJ0yZm_5CvFzihOkGxeBd0kbE2UAxntIpVPsQq5Q3szyNGgWnszMPWi6XW6DX__JjdVOhNL8M3R4nertVcf-z4SfTsXuOHqqJLdsg9Tw45ztLvGK8iKgKCAn3JGCFQew-Q8p7wiieP1AUct-d27d8uoGXWQGFaB_cRTp2eyf4zeJ9GIPgRYhxhtUBs1s4ut_ZTkYcWqO1eHLRObNQF5x5bl3Y_y6A26X_1gSg_VfifrGtCkAcqvKeyWv0EWboSgaRCNxaqE0gy0DzyZUQqj9ZXigcLdrADxxbZZvaiCVbDBiF4zUzY1bsgufQlBfAtqdpMc2s_DAKBE3qvhQCY8c9bUXa9MJhKtQA4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/56ec89ae70.mp4?token=IsaV3mILGRbyGsFdyM8tzJy94CJpc8ao5POOklMrIRvaKz2PpfJJtNOQZkD0aDB6egbzBC6MBejgmH9DDq2hCHN95-GsTmfKADZLtTgdBrtp6Z1kH0PdukKIuIDFyeXJcosdDOPYa9BxDgRYiZYpNFLa5LfdLLQixG3cZ38fmhg9669hVk85_U88qIkZBr45UokTxd7HhvhsmYCRIy0BAPRx7F2W6ln2_WK0NvdAy8mT41dd_rar6k51t2DiTsWhV0JKRsb7mHOO79eUV6Hd6zjBaju4AIuc-jO9JYhuqmIo36H9g46RfvIQodUW-JjoEMvUI0s6hKJ0yZm_5CvFzihOkGxeBd0kbE2UAxntIpVPsQq5Q3szyNGgWnszMPWi6XW6DX__JjdVOhNL8M3R4nertVcf-z4SfTsXuOHqqJLdsg9Tw45ztLvGK8iKgKCAn3JGCFQew-Q8p7wiieP1AUct-d27d8uoGXWQGFaB_cRTp2eyf4zeJ9GIPgRYhxhtUBs1s4ut_ZTkYcWqO1eHLRObNQF5x5bl3Y_y6A26X_1gSg_VfifrGtCkAcqvKeyWv0EWboSgaRCNxaqE0gy0DzyZUQqj9ZXigcLdrADxxbZZvaiCVbDBiF4zUzY1bsgufQlBfAtqdpMc2s_DAKBE3qvhQCY8c9bUXa9MJhKtQA4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
اشک‌شوق وینچیچ پس از اعلام قضاوت وی در فینال جام‌جهانی در میان تشویق سایر داوران
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/Futball180TV/100602" target="_blank">📅 10:59 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100601">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dh0w6D6bBcnkWxPPop5S59BVBqv7aJJ5bJoyVcKeVOCaAYRg7feQmPUz0HFacayvQZiqKkUh4e4NAjjeqIW_BeYPn6GtNpt2L5UytQ6R0zJmDPobBGVf2cI_gEwNIhpaUwYaShYgUWZEP80aIEUsAEwOkTtPYPnMYU5QZ6TzYrOK6HwnAOGmj04UNgU__wJf9_rYppyH6-4KI-Szdsr47REGD7MadLsB7y6vMhnj5KbbRkihxLgwwU4-olp83AANfy9mSF0tm-FpQ-dp7zj3ndqj6b7hATO4OLIJPKnb-Ely0COVMAe17FmqHUO_KEby0GCVoBOrXtRDYv2Yv4MxeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
👀
آخرین رده‌بندی توپ‌طلا جام‌جهانی ۲۰۲۶
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/Futball180TV/100601" target="_blank">📅 10:40 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100600">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bfcb128fd7.mp4?token=bj619vvq0IJeg8GqIcxb9aPTmcYjuWiqYfnLmmquRAgj2FHNW66Q1CgOM9v8EliYmgmnJr5Cbujbd8iFL13SiE4QRL_gy4z95s-xvp2gRDJsvdigrO11RXQ5JjyzPdQYFJo9gkd-Jo4g8jUfT9ZQQ9gGVgNjHxnNZXOOh6GL-McAQev8HMj2AO-FCj7Dqw6zorYbM0nAeYzudsJJr_L2d2iatocHn4OnypcekfdAn0qP_8j_itMhm9H5YFdipiYarel1__KPIaIYFgv7IXWdv2TwGsO9yJPd3aBbBR-b3Yyba5pbepKpLw9v8rUefw6ledOHs8rwMOgOoTHIYdCP5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bfcb128fd7.mp4?token=bj619vvq0IJeg8GqIcxb9aPTmcYjuWiqYfnLmmquRAgj2FHNW66Q1CgOM9v8EliYmgmnJr5Cbujbd8iFL13SiE4QRL_gy4z95s-xvp2gRDJsvdigrO11RXQ5JjyzPdQYFJo9gkd-Jo4g8jUfT9ZQQ9gGVgNjHxnNZXOOh6GL-McAQev8HMj2AO-FCj7Dqw6zorYbM0nAeYzudsJJr_L2d2iatocHn4OnypcekfdAn0qP_8j_itMhm9H5YFdipiYarel1__KPIaIYFgv7IXWdv2TwGsO9yJPd3aBbBR-b3Yyba5pbepKpLw9v8rUefw6ledOHs8rwMOgOoTHIYdCP5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
👍
تعریف و تمجید فوق‌العاده علی‌دایی از اسطوره داوری دنیا علیرضا فغانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/100600" target="_blank">📅 10:20 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100599">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L-hu-AgAKaqpGN6V4jOaGWnBgcEljykL7fxccrKp6VwGPO8RCmSDF9iJ6GrZAHbvUROg0J6BJnZlJQMDdmCUrNYxg_otgCyobXzyAmmBbOV2SyjW6BqsvcN6729j0lONnZNHW_HqCVE7x6LnJHkyHvEuu3cM_TVk9Gs1wbKSrnfRu-b5y9J2qEpAzOK5--0a21bcv6N2DRTDRkYImPg2G73he53gkCdyuDWHM2cmFO6of1I1QQrMpFHxLZbvBiXouaDFgGbN3Qwmxmvrc8waF89QuDyz4XfxD1P0aeZxmsNck2BLGIPuAwu27jhh-msje9Nkyw66KCUtAH8mTxt9aQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
🔥
سن بازیکنان اسپانیا در دو جام‌جهانی آینده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/100599" target="_blank">📅 10:02 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100595">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/clev_jEt-rpOi_WsmJ6uDCZVOl2anTf7Hy_nUVigH-hW61IZX4X6sQlUujw6h9yVJplAbemACvLa481dgVN83bD17UoS0DjfxTo0j8KVhZlU-e0BEXonnWJhAIPUxROmmWAaSDy3dLTQGy7EdYhw_aAUaxweEykd2IAOItE4Qlt3pfImcAynieveIS6p_o0mMNDi4qEvN21hWwTuXDHhCbDCGFS8QFfhzQ5LxZ6kAQAE72bYOQltWeYvcAdIlgusemvScFrUskuvpp1EbqQcx0Af5aDH3G4ppUce_kzm-1whOesAz-G_FhNpVlSBKPJyghAaTehKT3DX_LdbCEm0XQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kZuZRRrPqGJqT7GIJe7e2qy6bRhesgJkdyiteScLT1-dVo4flCk9AidamU3z1TS1F6m86vIyG6oyTHfZhz6jqCLsR2Q2yyRDlaeIMBYvz5jDzdeJ9Qf7CA9GIqm5eoS6gUhN6o1pgr8imLNY9y_XR-g6Bpq5J5C2nfg8b6BbLlYH8limEwdX0XI36o_y10EiJmMZ3nOuZmX5F7QfVmYOoXO6CP-mTsDLmB3RYr8ksAksLmgYSK5pfUTJuXeeLRJup6g2D2DZBYNBpwD4xsxuWrCXh0p0qODImbgU6-yUnBvRvKx0RqZoinEU5C9i18GqTN-tRa9tOhCpx7o80nwRnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/o7V64SVBTclIvsId_1yYdlXKGq1pBzlf7yzUOfUBIZaCGjeE7ZjFb8yzzJVBHHPQbJZHqK1gPd9GqK6INBlQP4x9l_FUrayED8jOO826PeRSNhgg-bKJsyhNC3mt_857S6UCpeSm2sb541rmMByyg3XOaeQ2_ccM6NxqFiC3jA5QVp_pcMqo434R_wyW-weAl9HM8mqUAYVppyQCgIxCvKLVBssBDxIVJQgsQbqPqH6VxicoXc-z2GaRTulvzTbvILogF8NRkRw4X95QfbkIlj-ke50KavIo7cc1ba-zZtkcykqmjeopMJHc2sM353HuoObNyLVSfZLYi7pH-xjGWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sA2l0LPH0MC659R2ooDQSER5ra-PTdpi6kvs0DGwsE7GFxQJ20MFg19VUYdw5ujiXS3eXtewNHe4RPhlPJdSzhgMBC08vOxuhGTQftvayFbXTJ1yEWC3Gvd5uMuk6L_oPHToJtEA6_Boc-x7wCx0tS-17GoriXZRnFW9zbCbvS8KQ-c_MhJiJMbjqTYGA0GzW9AGi_UivFkzrwxVdk9rENLEFWNgBmsILQr8DJIgiTUgUGMynLLBF426x4wlPf1_UXiMbBoktuWcbCt0MU2PERlj79s4FtkOFPNpOiR3lnzM7nTSHrBypi29KpJU-Xfl7pfUdFS2wUHbmAFk2EUzRA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔸
⚪️
12 سال پیش در چنین روزی، تونی کروس به رئال مادرید پیوست.
⚽️
465 بازی
⚽️
28 گل
✨
93 پاس گل
🪄
121 تاثیر مستقیم روی گل
🎖
34091 پاس
🎖
974 موقعیت ایجاد شده
🎖
94% دقت پاس
🔹
🎙
کروس: لازم نیست همیشه حرکات نمایشی انجام بدهی؛ اگر با دو لمس توپ بتوانی بازی را کنترل کنی، همان بهترین کار است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/100595" target="_blank">📅 09:45 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100594">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4324684be2.mp4?token=I7B4XZxlyobh0KpMs8Qugo6A1srBHnPx8hBjp-igkNuGj-9u8qHHwbneIZIsNLfe9TMfysfJQcD64FZ2m9IUZh7lchXEMEo_Lp8Ma8l80aWTxaIpZCA40IVBQIoOAWK2PvmlY4EuVUAg6yjSgmJTUAMJhvnbnqeRGfKfVEucViYGPZeVVn863f5mH-LzM10glUbgayKffzKVj2qBdGI-3fl8YAttLQyxYZVvHSkAOAmkIT9ey6SfB40xQX9Rr5FnsKeNfVFiQ6WhNy35RMRFN4hIXPrLZ-YECOElLNuHeoXsX_YfHtHZFQYWRPnRookOIalH97jR9Hd-R1LOd-D1ww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4324684be2.mp4?token=I7B4XZxlyobh0KpMs8Qugo6A1srBHnPx8hBjp-igkNuGj-9u8qHHwbneIZIsNLfe9TMfysfJQcD64FZ2m9IUZh7lchXEMEo_Lp8Ma8l80aWTxaIpZCA40IVBQIoOAWK2PvmlY4EuVUAg6yjSgmJTUAMJhvnbnqeRGfKfVEucViYGPZeVVn863f5mH-LzM10glUbgayKffzKVj2qBdGI-3fl8YAttLQyxYZVvHSkAOAmkIT9ey6SfB40xQX9Rr5FnsKeNfVFiQ6WhNy35RMRFN4hIXPrLZ-YECOElLNuHeoXsX_YfHtHZFQYWRPnRookOIalH97jR9Hd-R1LOd-D1ww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
🙂
تمسخر مجری شبکه ورزش توسط ابوطالب و سوژه شدن آن در رسانه‌ها.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/Futball180TV/100594" target="_blank">📅 09:40 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100589">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5a6e4da4f4.mp4?token=Pg7zIaCO1IDI_r0gti8aw7_uHL8GhU43V9E4LgsVnNxnEzKuZ2k0qMMOAOYO7CRVqSfJEu8xLFHs1Z9rk_LTtnadwQGG6B4GN8cMvzqoNXY_STt6K6Lu-f6dnSdVLIxoth3ZnpaFTnflS_MeJYgTF8LlT9XM0laH6tqIKum8yQZSRzV9dUjK31k70R4-upeoEKSXEhOotjAj2C2inluzDCl-SGr46n7jcDAkspYWsI9FSi8CgtoVHo-wxiaBCMheEZglaRPLayJK0NnbHJCH4iI9KPKDgIDq-mT5YLFWVg9BKgsNDuXYjfbijemklybhmwmReeEz4-XOYmOuZZ1Y_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5a6e4da4f4.mp4?token=Pg7zIaCO1IDI_r0gti8aw7_uHL8GhU43V9E4LgsVnNxnEzKuZ2k0qMMOAOYO7CRVqSfJEu8xLFHs1Z9rk_LTtnadwQGG6B4GN8cMvzqoNXY_STt6K6Lu-f6dnSdVLIxoth3ZnpaFTnflS_MeJYgTF8LlT9XM0laH6tqIKum8yQZSRzV9dUjK31k70R4-upeoEKSXEhOotjAj2C2inluzDCl-SGr46n7jcDAkspYWsI9FSi8CgtoVHo-wxiaBCMheEZglaRPLayJK0NnbHJCH4iI9KPKDgIDq-mT5YLFWVg9BKgsNDuXYjfbijemklybhmwmReeEz4-XOYmOuZZ1Y_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
خاطره بامزه خسرو حیدری از فتح‌الله‌زاده: روزی سه با گوشیشو میشوره
😂
😳
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/Futball180TV/100589" target="_blank">📅 09:20 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100588">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/84d54514e4.mp4?token=jVpQoonrLRj6NUz5L0Aktj1aumoT7-F7xOSVmskuZE1CyA8Pnn-3TnUOWwCQGFGJChRX_vI63V96DutjN7rM80boAEl2PxvXw1UkC_juTBGxpHpYymWmxdHR6y9-ZvOpmNVGchgL7w-N_QnsoDMGijLGiQp9cfXMWqCxZISzY5EQKl2yKJPthV3fNSTkx1Kao3wl7KOcLlZjf-BoeVUA8QgVHq7Ou6NQfYIX-Mxspp0i0rPZV_VEaw9XHwWEd6ELrUuMwX7r6jTO-xDAHSiWTGNBeH8PPXW-MwQj3WwYSyL17kIeZESwrmnk8Ef9pMq-icVSflGtLRvYaKuH5xn5ag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/84d54514e4.mp4?token=jVpQoonrLRj6NUz5L0Aktj1aumoT7-F7xOSVmskuZE1CyA8Pnn-3TnUOWwCQGFGJChRX_vI63V96DutjN7rM80boAEl2PxvXw1UkC_juTBGxpHpYymWmxdHR6y9-ZvOpmNVGchgL7w-N_QnsoDMGijLGiQp9cfXMWqCxZISzY5EQKl2yKJPthV3fNSTkx1Kao3wl7KOcLlZjf-BoeVUA8QgVHq7Ou6NQfYIX-Mxspp0i0rPZV_VEaw9XHwWEd6ELrUuMwX7r6jTO-xDAHSiWTGNBeH8PPXW-MwQj3WwYSyL17kIeZESwrmnk8Ef9pMq-icVSflGtLRvYaKuH5xn5ag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
🎙
علی دایی در دفاع از مهدوی‌کیا: با او چه کردیم که با دلش ملی بیاید؟ مگر او را دعوت کردید؟ انسان‌ها با ارزش‌هایشان بزرگ می‌شوند، نه با مجسمه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/Futball180TV/100588" target="_blank">📅 09:02 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100587">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OlyUUapLM3BCxH2QzkbBlzsSUtdIesNflqfPS9O7a71dIjiZIbFZ9YC-tLgPegJ1B9eXCRqJZJNZ0oW3AKa4SSeilncRQj2dwon40TDTo-Zc_hcJk6YKpvQBmz19lRBQuKjjYQC6JbicAfgKs2zdKHfpyOTnKK-qZi4Jnm7_HF6AGjJx_FZK8tu9nOGgeyE0qV-RSFr2Uof9ASPPRSiHkuaB3Un0Gn6CX-8CTjhU9Uyfih8zK57OGfHOa-zu8ujIeQ2VRqmtF-sPvFsICW9CFNvOCwtSz8HYpP97W_71KAwhhHT0d36sYJty8IM3PU73JPQZDidK8M3ZHge9xaYZRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
🚨
فیفا اعلام کرد که برای اولین بار در تاریخ جام جهانی، "نشان‌های قهرمانی" به همراه جام و مدال‌های طلا اهدا خواهند شد، مشابه آنچه در NBA انجام می‌شود.
🔻
2026 عدد نشان قهرمانی تولید خواهد شد. تیم قهرمان جام جهانی 30 عدد از این نشان‌ها را دریافت می‌کنند، در حالی که 1996 نشان باقی‌مانده برای فروش به هواداران در سراسر جهان عرضه خواهد شد.
‼️
‼️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/Futball180TV/100587" target="_blank">📅 08:23 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100586">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AfeWX4p-gozdJXxAUSEmIMN19aPflw0oXgsNuD734Egr-JCMec2_yY7mSnAiM4YNXX3qmXgPBDMTSDeACm0ZfWCyizI6_mrgokK0QUiavLoNl-UccUt39WVmkkWQ8kIPrKJoRucL7J7V1_dx5Cra5Vl9uuI3719-xJ5HLQT2mgoZkBGGOFcLZNzzy2innkctZCDwkGCF9Ex_5iWfC1Pp3s0TjRZCnB6fwynvZz1pbhzHBCaQpgTtf-a8nydaIfOc0eKxf3ouq9obo_xyPJRoL3x8LcRzrOyk_RK-jbFp_cfRZt9VVGgxX_lTHoA9iKGoKuCdh2SJUs05N89z8tIGFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#رسمی؛ با اعلام فیفا داورایی از کشورهای اسلوونی و ونزوئلایی برای قضاوت فینال جام جهانی بین آرژانتین و اسپانیا و دیدار رده بندی بین انگلیس و فرانسه انتخاب شدن و حضور فغانی تو این ۲ بازی عملا کنسل شد..
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/Futball180TV/100586" target="_blank">📅 05:47 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100584">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MNSIXIkBEnA_ZavuMhHkljJmz-9bsGkW54iZ7wGDh6CNQoZCnQu509gSo5Zqqpe8di0XX2bYqHn8q4S8DjntCOrvqlwnU5zB80f69TFFlYZUSNwNg575vdMXvdZMfMCAzSv0ZHBi2829VNYxfank8uPLHtxlq46dIm59HicXyhAfrGl-yxTn5JcsJJGea17HZ-0BES7m3izAfKJ2e7TKJgb5hrLlZMr0hFWKNOXwL7WZCoOzUeUXDm11tUbl2qETik1zLwEewZon5Bo7QpxoNQGeO1KXCeiaLZVyQdRfOAJZUiILBowmuMTuYZ_3RE0WWEK5UrTJdiZcTeela1jx-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/O0fUgZUekPUBx0LpJP5GtETZ0nYnAc7dY9DPZUmmK1J2Xz8qF5Q9cdm-DM3pETTjX4JLKLcNOXkZ54Ce8WmwdcEBtwnElH-VHPzxgq50s7gWupgZ8br0hNy7cRwIro2HTUumuonlb-W0fO2hR0aa3M0eWO3SfPTG_Lw99nI2jgLoLqbI94zG6hBJPYmpiMhMdv5G3yMd7r0Zo3PYS4MgJjqRxfCGFaxcllw0wuFzei18VwVPUqa0Ge4N7FFlJuZ1xQWixuD-3t1J8-FT-w6WuQH9N9NVFbIEw_uuwHEsO3Cju0CDwh3gJBUhx7I0-j9GcK6GpCsp0sOfzuvLk8dkQg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
لحظاتی پیش در پی حملات آمریکا، برج کنترل دریایی ۸۰ متری چابهار بطور کامل فرو ریخت!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/Futball180TV/100584" target="_blank">📅 05:28 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100582">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vJxmk-mBoCA6O0rImmG0cmeKU2lYb97HGcqub2_GGk8PfXdJ8iYX_Fk2gp5wCJlRUmlqFECrbS4X36OZKFYQXLccL-0XMD2e5fvVqJDuqjFl6xbu-0SAb2gnMc_WVt5ytLkQgHzIM_DSZYdAN2rEjrCzqrXrVLbbGsBB9miqm04h023P6-xhLR2tRIbRcKb5VlAABavDAqBBTTHesJcQ4ZcEfe55x1XsgBqP4paGuOR24mtnXQfI_Rv-Pvwz9KNDcNFyKgUl2ZgG-EktlOhtcG-8BdkGJFcei1mpXYmERfHFycTFsk4S4bXWM1RGpqFfeu16v1QAnzPlPXXi2_tWRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lIkhCoaWYC0qhxGAHQkTa6L8RA5lnA_iZXPi_7cwj6zyXGmcfygXpiriIVoFbs2fjL24csvt8yh7zAPtnJ6kVv0KfORTBG-pbFGNTk43qzUVwRJQV42JE2-53u3JKFstgOw8QgEMLcN7IXExqTH0XJ8Iu-mcWJGtCIiUQTM4bIpB7BJEu5iQiaQ34e93pIFwqcdZJ545BppHGmuWHM8qARXQd6BD2pEtDGWxDcru9en9Wx1SxA4nYzOQngtX2ajuFaAUdkkKMFmVy38Ju6GdKz7bcw0CpWzS1TbAWyuYwklNN9FEMLFA5URTM99bNw9EkDAw0CzEX4_EmmklonOFbg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
#رسمی
؛
با اعلام فیفا داورایی از کشورهای اسلوونی و ونزوئلایی برای قضاوت فینال جام جهانی بین آرژانتین و اسپانیا و دیدار رده بندی بین انگلیس و فرانسه انتخاب شدن و حضور فغانی تو این ۲ بازی عملا کنسل شد..
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/Futball180TV/100582" target="_blank">📅 05:27 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100581">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bKAg05403iQUBAzJgMVqfDZQQXrekJ1J8q0mi6fgIn7W_bTdlGnAaehTNyazS2xmIWBr4DjsHHSIq2vlrCtzatm3QE7xd6enBk8OUWEqpxwbvUq5jKSjEEFXjTSEclCMKNI9RAX9gAhUmJPnZk3giiB5vLcCaURVyLfiIXKInhHLayP-mBOp2wSSHerC1DqnnYf0-de7jY1OdRiIPUjQgVgP87KhZzNv8UpbGu5P7R5ksVgq1mC30cenhY-B9Xv9peJcSGaZ3b6Erf4rXwE26bCb1dYvZCAGow9q7qlvN8aiTQqJr5ppUWvsve6pHOh_3slB38bO9YmkPiHUuQjquA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لاپورتا: اگر داوری در فینال عادلانه باشد، اسپانیا 100٪ پیروز خواهد شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/Futball180TV/100581" target="_blank">📅 05:02 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100580">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hEQEcDZxftF4Mn5vCKjFunstb_XFpVMacbEs3P4EiBZAJOjj_7cvdMbsapFXGLKI7sKtG1Ew8luwqYA4JNJPMB0sOW1FdHjPyE2NGpZV94S2h5fyhOJ9tl8XwwICep9S5jKHDYw-fDVfpLxmJYhllZbhqnave-1PeWoV4K91XaPvw4GhHqd7AIrQ-YJEZ42OF26xz3XQOpyx0RMlPHJxWIPM4LFHgAIThGAnuux2TQqpwh1I2q64zpHc86-NKncP2y5x1_6HaIqyXKr8bTXHubDzZNxsYUqYYVRv0TL_-HBh3_H6nHpMxSqYC1KOQX6KddaLRIR8IMa7unkkDsI21g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
پپ گواردیولا:
یکی از بزرگترین پشیمونیام توی دوران مربیگریم اینه که نتونستم توی دوران اوج نیمار توی بارسلونا سرمربیش باشم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/Futball180TV/100580" target="_blank">📅 02:45 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100579">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tvGjH-HXDfU40EBIF7-Yt_7sZA2rM2tjeCW-hbEfh5i_gn9ck0zS0hgX7whobARwnQcZzwA3rFAmNrQAubEyR7wcTK8b4mMIzyIPv2uxv83XE2zKP8Ip-JdtyJ7JVKuObu5YKmFQmO7GBHHUk_pFzD2lZg5crq_k-0Dce3We_nLXP_k5CTACaz60EWks_Lh3JaDWH9ryXmHzCN7nSRyaHfQHe0_zBzSFWCIRV6tT0d5JANCFbchvEIfDvdTgM9rQdJSOnFrGjg9sdn8G75uNB4zG8SE281Sl99vqPt6a9SLV7lPpl1iGZ8K122K14vrEHEgam62H1XlQVWzR9xbPzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📰
🔻
مارکا:
مصر درخواست میزبانی سوپرجام اسپانیا در سال 2027 را ارائه کرده است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/Futball180TV/100579" target="_blank">📅 02:27 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100578">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🚨
🎙
🇪🇸
خوان لاپورتا:
- ما یک پیشنهاد ارائه دادیم و اکنون تصمیم با باشگاه اتلتیکو است.
- بازیکن(آلوارز) اعلام کرده که می‌خواهد جدا شود، اما پیشنهاد ما تا ابد باز نیست.
- در صورت تغییر موضع باشگاه اتلتیکو، ما یک مهلت نهایی تعیین خواهیم کرد.
- ما یک پیشنهاد بسیار خوب ارائه دادیم.
- این بازیکنی است که فلیک و دکو می‌خواهند.
- اما اگر این انتقال انجام نشود، باید روی گزینه‌های جایگزین دیگری کار کنیم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/Futball180TV/100578" target="_blank">📅 02:19 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100577">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MPXE9RUkO14mQANbusYisZ7eJozUlzZqI-fRVOXzp7aKXICpydLsgCzgCmUMUL8-DhQiYhHNK6zopT2Wi8DtIDcuw3qPivqv77sKTbN0Nz6jY3VyagEuToYgMg1ADH5ZWCNl2SJvhzKPbelpkZjgdjpXATfGyE5OQA9hNN49uX6rgc3bpGQz_tMISevurkChHnf2cyhBUtGtAbM1H970eEp8-hWBjL-hp064nTgiFaxXzgJIJ8fT1FMka7xfZYDxChWgvKvfbr1syj5bY8bycqazP7YwxXhVa7RyqLxkoVZqqR54l80YP2lUh_OAgT3DsVyVqwjH7XWSXvbDHXRAUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اولیسه کیه بابا.
همون همیشگیو بیارید بایرنیا یکم حالشون خوب بشه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/Futball180TV/100577" target="_blank">📅 02:03 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100576">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FuckBet @FuckBet @FuckBet @FuckBet @FuckBet @FuckBet</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/Futball180TV/100576" target="_blank">📅 02:03 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100575">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/RdxrkMZDBpLUy5ReRHCpUl_yYjPS-T_kh9iYJ45acCwUWPCjEhNnRYJuZm2jj9vv7PgEenDZvIFVcu7vuXboC6nU1zSbgDdhW45kLtXIgIJsAbybnG0Q0NKUJhoj7MrNR7jM0UCKG0dGjsoGuQLQPAp0iQAQIjK4izoLIuDEvXKnNFB0XUGIsF8VErlqplnIlAWwD_s2wqew7bAAYXKFupApEkdAzm6VGYZILA8kx85eLQxKx9H3x8Q8yE4KjtnSnwtA3Sg1U0e5cCyiZOxlU9uiXXD7BPLYDpZntlgBI3o-6iAt3_q5dhpU6j8llwPTZfvk7xvoUOa6Y4efDQU1IA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FuckBet
@FuckBet
@FuckBet
@FuckBet
@FuckBet
@FuckBet</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/Futball180TV/100575" target="_blank">📅 02:03 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100574">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🚨
🚨
‼️
لکیپ: مدیران بایرن‌مونیخ از طریق اوپامکانو درخواست تمدید قرارداد به اولیسه ارائه کردن اما این بازیکن رد کرده و گفته فقط میخوام به رئال‌مادرید برم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/Futball180TV/100574" target="_blank">📅 01:35 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100573">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fbNOuqJDqJo9CRFMZ33N6asN5--_cS26k4LyFlLwc7LJQ1Y39YuZnc2PqjW2bDKEiClez0jzl8vkJeG2V3yBcbujbG1qHJwF85gDLZI909aySCB0S8KzA2QhZBBZ_QpDr2iFKfw08dI7OdlOsbdvaFWIBQDh2uxV_HFqGHjkty6mhW__oeAGmzw-GHugaOTCkZ6ZGnzwb10Yr9LblCCyncp6b2_OFgGyinH6oReUUwAsGGPjrP5TL0Y7M_mZZhVO0acSrxFjghnyMwn9svreTn5HrErjXQllwUAnzHIjZL7s9Q2HuDE8aayPk4FTEzzVXYaQodA_P_HoYUsrxcO4mQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🗞
🇩🇪
🇪🇸
لکیپ‌فرانسه: برخلاف صحبت منابع خبری آلمان، اولیسه شدیدا دلش رئال‌مادرید رو میخواد و پرز بعد جام‌جهانی با پیشنهادی دیوانه وار برای جذب این بازیکن اقدام میکنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/Futball180TV/100573" target="_blank">📅 01:20 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100572">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cws82ff40fOmJ3NiNRFXSrTNvp3XC0dX3wdpZq8q_B0X-rmF-1StieNkw0ivmDkoYqi3kQ1pU_3FeeT2JIelGf80RlDn7bxKut63BFIHvXHh0UHQiwroPO5vV44-6SAZo1NssyIdQscQp9e9yhg8-JpnYw_hZPoooHpKnoBkJTBB6d-jvk9OfJVhH3TyCN2SpNDMDRg5Jw9ZZNTIh5bp9DWN73rnAekcZ6FD0gXi3h0tFInFpHSqtq8d4gs87Bi1hbi9UMJ1DZp2eWGSTmR_oNymsjDH-k96DdcY7cOMrQjIlHOy3FWAvKVF3NTUnTrEqTAA3cPAD0IZ_-39iNedTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🗞
🇩🇪
🇪🇸
لکیپ‌فرانسه: برخلاف صحبت منابع خبری آلمان، اولیسه شدیدا دلش رئال‌مادرید رو میخواد و پرز بعد جام‌جهانی با پیشنهادی دیوانه وار برای جذب این بازیکن اقدام میکنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/Futball180TV/100572" target="_blank">📅 00:58 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100571">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IZ-gmgk3n553zA80QDwOr5nRTaNNit9MedqAoITGlPDrzarIGPiB8pssh7AD9G72jm3jTrgPgrF_0HYVkzCVHnr4atv42iOtml8goAMfIgtt-T5BcGAallDGZArsU39b6EsziGSLpv_DPqnJ0Ik-UDoTqWQ_xUh3z16vmwDqpCQ86EZSxfo9f0fMGoraCqrc3fisMkL5oEDEyh2CfljeIFCdJfhh_yS8crTmpLxFuJQQaEgYswozTZgYXMrjz9to4Yf3pfo-Wn2czcsoV2naC-2E5MXLnDrsiKfvywJUC0rr1W7jza7wfdiJ_G1W93WL9voQ1VeCxcsJSdxAQ09JKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
رسانه‌های آمریکایی: مطابق صحبت‌های رئیس جمهور ترامپ، حملات به زیرساخت‌ها شروع شده
!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/Futball180TV/100571" target="_blank">📅 00:49 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100570">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hPcm09H5Ub4bIu2TuSAeAG2VJuFkv1o4tc9dszzrkBGO1UTAbldoDo6imtU9karim44UpptmT5OTrBsfyHMYHoUg8FGfmNd3ORMWW1KslG-x-w1trx7NDmV4LAWG5QMrVmHlj1T-MxfBSzni4djIqvUV95lGHIOFdMQ2ZrQuu48EW7exM-MCfv_bxvn7GuQ3T9tUckPxylooVo8DoeKLeH939KOcwBJCtqLlMnVxMVYCVZnehX4Cn2ol5UGABm7icQgfkkqTOwftEgODOtwG9TUpAt2y7TWqSoK4IYwZTsPVybvD9xFqqsEviAfjVkd-MWsD4mH882yXTcslL7SuVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
⭕️
ویدیو دیگر از پل مسیر شهر لار به بندرعباس که کاملا تخریب شده است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/Futball180TV/100570" target="_blank">📅 00:34 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100569">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pydc9a8_wfSATC1SETuvdGlJzWQm-7ZC7HqKuJ3a_5l1k00URn1u3XXTw4c8-4YV7hGCz4tFb6mn6vVuoq50XO5U95bewmqDoSTHK14pp1VejtDi2Q0gtVeHn-5TR-lUALpbRxWfn7CxVXQz_TODoLglz17YBKEW_lgYD-N3m_mJ22If1DPgt2uC7oPKuKac9_sgTvwKwgsvLVyb8C5xNTEO-JuISPANPCNBM1g6_shCBTUo8cFp5y2gjk51lBRGrlLuFTM3VJTDdzfdLWL8TcR_g9V8dTX9LSRMKMogcnFaCO5qoJoEBqbWjdTQAuUdKOlEp2acr3pDp8C-h-ojjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
تمامی پل هایی که بندر خمیر را به بندرعباس متصل می کرد توسط ارتش آمریکا مورد اصابت قرار گرفت.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/Futball180TV/100569" target="_blank">📅 00:33 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100568">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🚨
🚨
⭕️
ایستگاه راه‌آهن بندرعباس بمباران شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/Futball180TV/100568" target="_blank">📅 00:17 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100567">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fYpxEhJPtIfBcpF0o6fJyxwCeAkhHrkjLfGB7-mqI_K2L17xhqTnr3oTsk9QQajDUBWdS0EQW1sWHXvfKTJvEJCVvkbmzoT_dKJCWX9JCsTSpwIpZdqRr1iZuw8a83SBE_3DWN0lRSN7hOKreuPq0mjKw0qFIf5I_C9Jt0Ksw84ezdH1VH5SC7RuRcSEZUU5LF2Wbr9PsTpmJxMcYWBvcurKuY5t9EeyHXkfTFLJGh8TePYsksCNU3RnNH4SvjfY-I-wg_DuOcjMShNDpnroYnimOnK_FWZGA7Sf-1npBXs4Nf_2YzkSy1VzypNxp-zi3EScGwupa-uUV2v0FAY0HA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، تو فینال جام جهانی 2026 حضور داره و شخصاً جام رو به کاپیتان تیم برنده اهدا میکنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/Futball180TV/100567" target="_blank">📅 00:14 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100566">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OAqfhxiEpSAgqMcjdIjXrqSNII01bfBWUhAvmeUMQZoqB1zNY2gZssYHbVL0hXlGCIIGrO56TDFrm7X12k6RPf_1YHPdGNTIyFCNMqISBHojONvI6uAvM940Xo_ykOEzn4Z4xQZLXNteepTfPNTvMUV7Wz8uQDcrdrAKQtV_WnG_IXPsWrXYA6pjjjCPg_us_HNc-MTdgtWHwFOV2j5H0QfwcUcTiCw72VijkVdy1BlV_YIgoE8BQsG_LGaKDu-f84uT9TBH-64AKVLo8A39NUNn1sGDUSOtSruYuPuc4FoX1COvjG6R-36tUqT9W7K6AwtXK0kmqPBGIYpsJ8yfUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇹🇷
محمد صلاح قصد دارد در این تابستان با باشگاه بشیکتاش‌ ترکیه  قرارداد امضا کند. صلاح درخواست دستمزد ۱۵ میلیون یورویی داشته است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/Futball180TV/100566" target="_blank">📅 00:13 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100565">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🚨
🚨
🚨
⭕️
گزارشات حمله شدید به سیریک
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/Futball180TV/100565" target="_blank">📅 00:10 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100564">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/a4bc985b6e.mp4?token=oFLq37UzxeGvob5cRFbMtHJMLj-sBgNrj2YvKgUTkM8jIske1dGxUToFWs3bBsI_gRjOX4jmbvPWy5gdRKLV88-lg66oXU3b_r8VaPjDL3G9_MTD1qUYqz9Vlq2PNMJo7yWLDGQcnoEhUijlN1tzmZwbKQiOFXNKiSh1ROWZvUqkSj5g0Ic6D7mCRIU_PTGEsMxjQBSncGTNnBpilz4zOGc3c5bKYp7AEJxt-5MtB7P0JiMXuxdY5vXt3Je7rWts9783a0vq2mKncwq6zZ_tLAH62xKdkY6B5d5DoE6i2HEOm_P5QrD_7oKc2cfR1h3QgXUcY59_9NlCE6dIjBYiTw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/a4bc985b6e.mp4?token=oFLq37UzxeGvob5cRFbMtHJMLj-sBgNrj2YvKgUTkM8jIske1dGxUToFWs3bBsI_gRjOX4jmbvPWy5gdRKLV88-lg66oXU3b_r8VaPjDL3G9_MTD1qUYqz9Vlq2PNMJo7yWLDGQcnoEhUijlN1tzmZwbKQiOFXNKiSh1ROWZvUqkSj5g0Ic6D7mCRIU_PTGEsMxjQBSncGTNnBpilz4zOGc3c5bKYp7AEJxt-5MtB7P0JiMXuxdY5vXt3Je7rWts9783a0vq2mKncwq6zZ_tLAH62xKdkY6B5d5DoE6i2HEOm_P5QrD_7oKc2cfR1h3QgXUcY59_9NlCE6dIjBYiTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
صدای پرواز جنگنده‌ها در ایرانشهر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/Futball180TV/100564" target="_blank">📅 00:09 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100563">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🚨
🚨
🚨
⭕️
ویدیو دیگر از پل مسیر شهر لار به بندرعباس که کاملا تخریب شده است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/Futball180TV/100563" target="_blank">📅 00:04 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100561">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/110e253ea3.mp4?token=HuGD9h-UJT_Vm0YmmJ_bezkSexeWMh-oFQ1fv0uIgrXcIJnErVs3dAku_ysy4j8gXTW8rAPERlsvU4BZOSHEMhuGVZCOxBgmeePYWqnDYl9g8meatibg0e-L22wHHZUNOHPylUwpzYMpHEJ0xuxwy5NsdsmWzorPWyeXkbbPAbQZ6gg248EJK-p0xziQDM9CYs2k_VcoWCDZxN79OYaJXXLoFRIKo-dYpqQtCxMXHWVnNDM9PyJvJB9hCxL9JVzrOeUKGUm0Nyy18Oo4C5OaTDqL4c1qIE_qJho3EHqT5I_Tp_Sl_IAqQ0ictwC24JgR9S6g773RLZg3VMa6zn22NA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/110e253ea3.mp4?token=HuGD9h-UJT_Vm0YmmJ_bezkSexeWMh-oFQ1fv0uIgrXcIJnErVs3dAku_ysy4j8gXTW8rAPERlsvU4BZOSHEMhuGVZCOxBgmeePYWqnDYl9g8meatibg0e-L22wHHZUNOHPylUwpzYMpHEJ0xuxwy5NsdsmWzorPWyeXkbbPAbQZ6gg248EJK-p0xziQDM9CYs2k_VcoWCDZxN79OYaJXXLoFRIKo-dYpqQtCxMXHWVnNDM9PyJvJB9hCxL9JVzrOeUKGUm0Nyy18Oo4C5OaTDqL4c1qIE_qJho3EHqT5I_Tp_Sl_IAqQ0ictwC24JgR9S6g773RLZg3VMa6zn22NA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
⭕️
ویدیو دیگر از پل مسیر شهر لار به بندرعباس که کاملا تخریب شده است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/Futball180TV/100561" target="_blank">📅 23:57 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100560">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e073aa854.mp4?token=odlmyMl8x1Rcv38ZghUC5t6JfxzA5rZ5P7vDAUGk-uuI8rp6C24mxrm9w5SHTiffNn-W4M52wy60ybCVsHJKw_pPHrfsDsqSdt9qbmJuJDnyOxv-ABwUSxvPcloyU8GZzA759le1e5XpYoZfljxz9N-pEQ1dRzxEj_sJdc39bkpyY1BMHUTqGpmzNi_JSOS3Tn9sIL0w058SP0v5CPrDbjtWu7spOOM3g6rN1xwiHHgncPBKvKVAekooKuvK_dt3zTN44nk2AY1hXH5H7RV37Pd31trDD_7TbMWfM1uByNsq6nfMQ6VzvkMeuKLN3eTCBGlkgAgXlEWv6JZmQq09uw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e073aa854.mp4?token=odlmyMl8x1Rcv38ZghUC5t6JfxzA5rZ5P7vDAUGk-uuI8rp6C24mxrm9w5SHTiffNn-W4M52wy60ybCVsHJKw_pPHrfsDsqSdt9qbmJuJDnyOxv-ABwUSxvPcloyU8GZzA759le1e5XpYoZfljxz9N-pEQ1dRzxEj_sJdc39bkpyY1BMHUTqGpmzNi_JSOS3Tn9sIL0w058SP0v5CPrDbjtWu7spOOM3g6rN1xwiHHgncPBKvKVAekooKuvK_dt3zTN44nk2AY1hXH5H7RV37Pd31trDD_7TbMWfM1uByNsq6nfMQ6VzvkMeuKLN3eTCBGlkgAgXlEWv6JZmQq09uw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
⭕️
پل استراتژیک که شیراز را به بندرعباس متصل میکرد و مسیر اصلی حمل و نقل مرکز کشور به بندرعباس بود، مورد حمله آمریکا قرار گرفت.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/Futball180TV/100560" target="_blank">📅 23:55 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100559">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🚨
تسنیم: شدت حملات در بندر عباس به قدری زیاد است که برق برخی مناطق بندر عباس قطع شده است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/Futball180TV/100559" target="_blank">📅 23:52 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100558">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🚨
تسنیم: شدت حملات در بندر عباس به قدری زیاد است که برق برخی مناطق بندر عباس قطع شده است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/Futball180TV/100558" target="_blank">📅 23:17 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100557">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aqgpL15mYSNZljq5JwXK73n18zXnSQFU4VVERAOl6apxidpcQ9W6KsfrMJLxFFb0CSxko-AckeXmiH5V1aQI1zptCxynnrn0_JMH0EnCOAnKeI6rinwJEMllk_LSFaK1-cqwGqEeKM6b5PiIAu34BQZ8YkWiAg-rT39Mc7mLnNKIOgam7Lb0SEPqYw60QhpIis-gRudKxJwgaqd84iMVuPhdgMgETBhiKv4hcPrySE77_GF7IXuKbW2RKustzlLeKq0stMh_-mRfd_4Rp2_-czvV-qO-hu9CxCdsjl7mG8j6q07t0Z54FbK2rGjAJ-sR3gGS_uxv1kl6bzUPsZqRBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇫🇷
گزارش برگ ریزون RMC SPORT:
ویلیام سالیبا درحالی برای فرانسه 7 بازی انجام داد که دچار شکستگی در ناحیه کمر بود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/Futball180TV/100557" target="_blank">📅 23:11 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100556">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GMOSBfUXvwiAAxmAhgxIMNgGmoqKUu-YO-CmiNOLZRNU-0F5mchMsNFnj8vHkLf3PmKyIKTbvTp0wxi3G2fJtcpKHw0TrVdZ9575t9N1-ypYJD8NOIA6I894OdHqyNk7abwR-yChDksSUkpUXGDm08OGS8xRP1uc5kg4lKuVwMD30sVcagA8_qbcZjOvT4tS1Hfh7PEJgOBpVO3HdT7FA1LuIArWW8p6IEG9T6MjERyglT8d5DgcgwJxA3SmRx0P283W-1dOQAdqFhsyOehViud-h4RUTTGaI9_PR7SdKzEey_NscOHSonxqSqd-AlWlWJRaeZYVaVo8-lhUHGBn9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🎙
انریکه سرایزو، رئیس باشگاه اتلتیکو مادرید:
خوان لاپورتا از قبل میداند که خولیان آلوارز در فصل آینده در کدام تیم بازی خواهد کرد.
👀
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/Futball180TV/100556" target="_blank">📅 22:53 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100555">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e16fb64d04.mp4?token=g5ILZ1ftSziv4nsTztlGiP8A974I7Y2qrcva7XNLWC_2PeZE9xH3aV1r8Gd22ja-fJbMm1iF22jbC-HmCJnJNalfueNv3WAwfJjWRyuPcn6CLnOj8w-QkR7tz5wWFKWrwBDy3P3bJmAFcb7vzrJD_6_ZFkawaPuK0JgaWruls3osEuPxvoj9VSCIhDtfZhW3_guO8E8Xc0bnol1VaVJLN8_EliJusgpO6YWbaYh3OVqh0sbhsJy3VQpFyK-Qd9006O0Fp7e1F-O0NUgOW_daAi6h54nTkzwtmXlZsqbF1qaGMJPlnaOSrCLJ1_Vzi5_J6xvM6W7xV63zEZQD6gcdkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e16fb64d04.mp4?token=g5ILZ1ftSziv4nsTztlGiP8A974I7Y2qrcva7XNLWC_2PeZE9xH3aV1r8Gd22ja-fJbMm1iF22jbC-HmCJnJNalfueNv3WAwfJjWRyuPcn6CLnOj8w-QkR7tz5wWFKWrwBDy3P3bJmAFcb7vzrJD_6_ZFkawaPuK0JgaWruls3osEuPxvoj9VSCIhDtfZhW3_guO8E8Xc0bnol1VaVJLN8_EliJusgpO6YWbaYh3OVqh0sbhsJy3VQpFyK-Qd9006O0Fp7e1F-O0NUgOW_daAi6h54nTkzwtmXlZsqbF1qaGMJPlnaOSrCLJ1_Vzi5_J6xvM6W7xV63zEZQD6gcdkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مسی و یامال تو فینال
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/Futball180TV/100555" target="_blank">📅 22:15 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100554">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rKGQqJh2_2guM8X5EScBjqmZ0U063XQrmg6DWhT4_NYDyiSlrLukXqvOsWsf9quhmPofe6lpvasmVm32i4ZXDmtaTcwYm3IDC8Y_Yufsvyg-EMHU4iCwqKPjmsMxfpwbBIhs11ipN15gnaQZo1LiXYCzhS_e2Gz5jw3NcEMLbCSFOne0HHbbTx3yhzJuW5ROA1MxCBl4IyEN8ZWMDwUK3xwSCsFWpJDkYFot4Dcr4aNADdTvuBV5scOmRd-GJPSTT-gzLCkb55gzhxtu7aI3iIbBi8Fhy6qWaYYSdIoOeh5h18b0VansIkn8ZNkAiFNWGFmyzgHCFA7Ha4xQ_rJjpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇦🇷
برترین گلزنان تاریخ تیم ملی آرژانتین.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/Futball180TV/100554" target="_blank">📅 22:15 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100552">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ds4kTfKe81Ch4UUUJP9hwOL2zm-KEiiZLi4EupMmYed5FP_h3qQLpuxpNTZK-6yEo42m6glQE1AQLWdaniB3ifv4p4Lc_pAqdKYnj8h10HmSkafpIMc-HD_D6Vb98VcPU3vO_Cmx_zWWASZNK2O-F4EqyLn9GiTL73SJp4NRdgv5MH1dodXJ0SM5jM0Di9zHVW7EiZK9FN-T4yPNrbOdE6YMz4QUYs_twmXDOReF--gpFOWvpEiu_bEvcChRaqPLckIzrkgY4dImcBIpGW7IJha-XDXt3r336O_aKkRAdXybFC5_lZSuQPVFDcwWigtZXMTqaKunT2fKFc9NoaF3lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jmGY-DOKL8FidAOnOthORpO2I__Be6GVNhEws97i4ha6AbLl7flng3UIaOtlw-OLbiC84v-liT8dh8pPNC8Q6TOl7LN0dYMiyWHI9iatgV9uKDkfdE-MqTdBvNhtz0sy2aeUsrFsynMoUiPev4sLP86pYSRx8rHYd5rmFJtdM0xiXCW2i9_w6P3178xCI6xwVQ-xcvnMb00wPrqq-WSvnHDrbx9cYnMZJ1kbG-xwZplboPI3KAa3rn-mwt_5hxv1mk1ymspF3TMJuRTP3-iO-veQbiihzLlk3wLNsUQ_tuMkBlFYARmyl8jtYHw4CY6OBlLgr-ZRBGa2fjGH2fDLMg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
تنها 2 بازیکن در جام جهانی 2026 بیش از 20 دریبل موفق ثبت کردن:
🔺
25 : لیونل مسی
🔺
22 : لامین یامال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/100552" target="_blank">📅 22:13 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100551">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Iwv_FOb8jDRpyvo1ypaRG3FcEuhy29c_pbfg0sICz-L6asY_dey_XKmVrWqIRH5TOZDeuOUZZWeEAYI1R84Neuy9nNAA-7ew4MKXYlUozaQtA0XgmJf0yqC9a1ApGdlVj9Nio-DqFVTPqNL7hOYONgyUZ8fjjX4xPccXOX0rIx6XIoAF-giTbrlCy67ukX8kPuPpzspUUAVd0a4NtHA9wOOU3EJJk5fW3gAWK-7l8zwVzFfoLoVvI0p3jlvent_cMY4ccDEwVKDRIpYEAGvrBuY5HPRbpZ0P-iODD-5lW3iauCcw8ViEbHfEH3Sv8B7jyw6ZsUcmFeS3QlLXiI_U9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📣
اگه آنلاین‌شاپ‌ داری این خبر مخصوص خودته!
اگر فروشگاهت تو تلگرام، اینستاگرام یا بقیه‌ی شبکه‌های اجتماعی فعاله، حالا می‌تونی بدون نیاز به سایت درگاه پرداخت اسنپ‌پی را فعال کنی.
✨
امکان خرید ۴ قسطه برای مشتریات
✅
فعال‌سازی در کمتر از یک هفته
✅
افزایش اعتماد مشتری به پرداخت
✅
بدون نگرانی از فیش‌های واریزی نامعتبر
🔥
همین حالا ثبت‌نام کن ‌و درگاه پرداخت اسنپ‌پی رو به فروشگاهت اضافه کن:
👇🏻
https://l.snpy.ir/i1ekm</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/100551" target="_blank">📅 22:13 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100550">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ksf6XtIuY-PPC3RbzaRIXPpkD5yneib0PBY7HDr1jsXbSmZ_j7tDFs1w1nBub1jBg5H-wJwzERWUndF6vz8Mzn0g_RJdNlDCSwzoUX4YuMKrRhq2zCsJTgdkXUG_2D36wGd_cAKMdsC-yyaBd9k67DZhycBGVJXWXMHDJRmns5-hhvkrITXSyoG7qNZXU2qb538Tx8J1e0-ANdrnr7vymMKQ1ZxXKrFkPm6mbeZZRJ03M8PjEnWxgymDtLV42gHYrf5Wqd9tV-QNrrBl6afiEK2PxrSax9yeaVqVrORKKpOqSVsDCuqxTOFkdetl-WoN0Xo-uTVXR6l0-JJW5MbR3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
فابریزیو رومانو:
فابیان رویز با پاری‌سن‌ژرمن برای تمدید ۲ ساله قراردادش به توافق رسید.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/100550" target="_blank">📅 22:11 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100549">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f1EZC-5kvk2GBqPrteLLdsIUqokDflET-erB7NmgVIttRM68_PUtCC6bUfvk-U6ThxEMXQjTwpI6WcrkaqPk_W8eiwudto5TFh_RgJX3VaMAh-I7lDjyKIVXUXKWMFAIrFuKe0jzHcg1GItuZQNXmc1fQaEKqWB9kTaj_RccErAUKmfbu-4DZzXpDCCLgFUpbvqDwwTdbnvVIfl9nTcLQg8IJPWP5brzBr43dEBoi35GbzkgNAah6SH8NU781W8K5m5IaQOTzClVcwHvMS5asuFGsJQEK-oVLC-Az4j-1-OpzS3BDmHN2vT-kwBu_7U63TmHv4W3WLuPa1BZAKu-Lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
سنتکام: حملات ما به جنوب ایران شروع شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/Futball180TV/100549" target="_blank">📅 21:58 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100544">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MYQi-4toF9c_9OnvCNMJMUXlKoZ4p2-1IaLxDGfFsuQCu35GDl2HVsvvGmKZGBBlkoRKlf3rtevSIqIMqmDYFmIG0zIEoHCT-cDYyVbIN42QGWi5PS4wS3qMMgQajNZ8S1NqF63cOnon_Bo0aatZqVUMzvidbVjh2Geds2SgaJ5bbBKMsJCGyG2kN-SVW5jXjfkmJxVVzxaJze1mUDBi7RzSetEoRp9vGXly7avKRimzTcv2fIr6Q37O7rMdjpO3rk5zKzywfBPmXLMsncasXVcG3og0uGOOpnb0QtZirmc5L73JTpPFg_x39ty2_-LTZfzXbIJvoNivOJAVcAH8-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LI7ZVdCb3m_aYv7BwjRIt9HFllzPilcBR9gwnf-Ovh8IzNfBuCeLMKngZH94pJBrr8JhdiLBKO6lme778PA9eR_q_Ny_PoMP7lslKV4uqlKNdpSsDdgFminuBxk11VSY2Bi3SJuQ_DZQlkQqYvtlGLzsCCY0VjOYEHOeSNNyrs26fqqknog3R399nda_sP_ePsj_juDaE7Dxx2qiCGqg_4kUl83PIdz0Z109prNlKQVJoSgIJaY8uGTPwK7CQRXZxwKonSabHvVXpiNUFMtr-MOxMf-4Zr1w5cUuHFx61hTtZxt689eXOMYQ4mH8sKvrzcKNmmKOTcv-GwJ1uuxJ4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/J3zaUBVJc5IUE14c-um8l7ep_chySomkhugKLNiwTtBiSumlzgFABSMDp6T-E4hHwdP5u2HpEP27TcfgaACHR83ONndxnGw1DdoquUELOirJn8rjmEuooBTYbJguogsR-HZOq6SMFPYTrdsEEGOeC3Ye_wc6opDN3a1HyHDvNYK1GUpmAHMP4G6jqsHj55rcTentnd9mNjw-oBuwNfAWBB_Pn58vlSAY0G7yi7bXow9WrfjJMpTbU6BXAU9lV5PNRCPcomPDcrQ67h_9mMK5_WHKKgCB_14-SVmpmwNy7kbsLopJebwnptCFVhvIuvHVJDKyO0gVQKgyrbJ5HrTLCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gU_pZsw1j66bbIKLP3dcGZ3XlMeffS6AIPTyc6RHOFYP6LFkdQkL3H8Z92YawTkQ-C0MQg3upzdET8J36_mgb7WtrLMzRvFt3PkliSXRsOo8V7wLAqk-CGw1Ph_e5-aMnQTvaYJxfdIEn0lTmeqrpknh2VZQetxSa3Mxk15fEhRvsjdI0eKpUq53ziD6RVmFaRCHt-E21Wi2q0DARSA4jh7Ina94LHO9d8JOghsYOL0UYLSLe_46b6AGEsocg7OSoQfxWzXPZWFN0JAc3XXvT-zh2dkonC0Yu_9rcRUMm9HP4qp08JxGsk_ptwWvUfnt0eJkSQlCXgxJHo2a9IcxAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Cs-TCcFpZZELctJmc5OvTN789j90YEa1QZwbMsJEjUhzSjkgGfLT5R4QPZOxDmMm-MICFuNP8JqFTlgDp_UloHbYWqR5BxNKmQcVZiif1eAJqmsZhvHQqYEtBL73KbPvz5AIZuHT0eSWhv82vyGmPa9xsaVKTZEDXcWrDHgfcpwYIVQM_vNmWWVzmwesVVW4dsFwG5k9hOKHil6-4MpQ3Yw4HHT8RIx_vgS4Jt-Jfg7RHoqpGkwEp_97TUsPAlihL2vQmzaZDbJ-bpaPilJvGCX5RRLBsCq6IolBC3rJOePDZX7UH6yYiuqBAAXdOx-yPGGotVgfsgaI84GMyOEyPw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پدر و پسران
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/Futball180TV/100544" target="_blank">📅 21:55 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100543">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dK1NBMtzrC7xIIQk5j3fsN2bjIV4Am_ldUsEEh53cfga08UvmdDeXcSjJEhRmX0kf-BwTCGy39miFEnsnmwp78Pwipp_HKciv5S5dNrJPt2eXwHwkxfLq8oC6cH1i5t19m5wauUY-K0jnNtUfmfJ4mqnfEmwiQvUrjFBrUnLxdwrqoKn0oT5I6pbUXCtz7LtgGWhpCn7Y-bprV_wDhpbU3hFrQI_BkmaVGFdGRaBK-wvT8TJjn9K-CGKuS9BAcwFiIsdSqCT_N4WZjw5mtAYOcBULv8VjQfzoI2SVgNV435PBzQQQj1mQEOZPev-UTEcf_8ssBL2yPZjJ8fCmCJTxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇫🇷
اولین بازی‌های زین‌الدین زیدان به عنوان سرمربی تیم ملی فرانسه:
😀
ترکیه
🆚
🇫🇷
فرانسه — ۲۵ سپتامبر ۲۰۲۶
😀
بلژیک
🆚
🇫🇷
فرانسه — ۲۸ سپتامبر ۲۰۲۶
🇫🇷
فرانسه
🆚
🇮🇹
ایتالیا — ۲ اکتبر ۲۰۲۶
🇫🇷
فرانسه
🆚
🇧🇪
بلژیک — ۵ اکتبر ۲۰۲۶
🇮🇹
ایتالیا
🆚
🇫🇷
فرانسه — ۱۲ نوامبر ۲۰۲۶
🇫🇷
فرانسه
🆚
🇹🇷
ترکیه — ۱۵ نوامبر ۲۰۲۶
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/100543" target="_blank">📅 21:51 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100542">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MVL2lnURge9FO9j7GF92x3NGPeEI5GFr9HWo4gI6RZbBH_mOjfHt0B1dR9AkMt0DgTVmidYbGPacB6udinpbi_-8SIFr5gEfg00OtKgtwHAFLgzgRZjDt_Dtn64--AQra43tYdW8EUdAP__MQ0qfhGJJENXj8w8a_VkyS0vSi2xwFjGjXELLi-gg3osKgROZ_wSvnjfMfUaAyfP0Z_WDIH3oXivUV43IGpXrVENvA3CgaakZX918NaV2KPxEdcb-v-wIvVhyoXdRNEjIg8fr_yD-xygj6R-lTugISVB2XO3EvvaVccCNTgSe1z2CwqL6iQDE3aW57kmBt6mKqmLweA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
خبرنگار: چه تیمی قهرمان جام جهانی خواهد شد؟
🎙
گواردیولا: بنظرم آرژانتین قهرمان جام جهانی میشه چون حضور مسی در بالاترین سطح آمادگی، یک مزیت بزرگ برای اونا به حساب میاد؛ مسی همه چیز رو تغییر میده.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/100542" target="_blank">📅 21:33 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100541">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b0ffa0ac5.mp4?token=eQRSs-UGQTnQmmKspaAkeAdz_g9_PWkjzbXFbZ-EWClXxiywi5cjMEzOFC4YQ3QFDqF4unb9cWyvzq6xA6HrMXTl4ceABRBUrN_6UNvCVLhapFJ-YJxpIMp-0zsZd_PQGIbZ78q367VbYWTwkYmkti2b-oeuxXg4Hv90qwbAYoEzsOLnz7gtVFoFoHOrLB0s0w08Kzb8eEb4gMlClhdrLxVXJF1PBMFBsX_qL5sOEm-1-y6q4aTgPH_Yo9PwWxj_TEY8-GJ8HhS40qcbAoqGg3YX-JQKnd0-xoNVi1nNKE5yK_JfONkYF2iODerQVHjzv263tjM5prOxmYylG7e6iQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b0ffa0ac5.mp4?token=eQRSs-UGQTnQmmKspaAkeAdz_g9_PWkjzbXFbZ-EWClXxiywi5cjMEzOFC4YQ3QFDqF4unb9cWyvzq6xA6HrMXTl4ceABRBUrN_6UNvCVLhapFJ-YJxpIMp-0zsZd_PQGIbZ78q367VbYWTwkYmkti2b-oeuxXg4Hv90qwbAYoEzsOLnz7gtVFoFoHOrLB0s0w08Kzb8eEb4gMlClhdrLxVXJF1PBMFBsX_qL5sOEm-1-y6q4aTgPH_Yo9PwWxj_TEY8-GJ8HhS40qcbAoqGg3YX-JQKnd0-xoNVi1nNKE5yK_JfONkYF2iODerQVHjzv263tjM5prOxmYylG7e6iQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مرد شریف روزگار
👍
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/100541" target="_blank">📅 21:29 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100540">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">فرم هایی که چنل های دیگه با اسم vip ماهیانه 2-3 میلیون به ممبراشون میفروشن رو شما بصورت کاملا رایگان میتونید تو فاک بت دریافت کنید
💸
🫶
فقط کافیه ۲۰۰ هزارتومن اکانتت رو شارژ کنی و با مدیریت درست فرم های یک روز فاک بت رو استفاده کنی تا نتیجش رو ببینی  @FutballFuckBet…</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/100540" target="_blank">📅 21:29 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100539">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LaVX8W3IsYlb9hMNJ8wEypnqwU_6YGUCWW9CHQBm9Z0d04HaczD6cj2ah3ZgxKeOuYEVEg2TQP2cn0YmkbiPLnOh47XHcSc2Yc7Wk5QpV02xCM8rb8aUZ85gaVPEciXLrQR4eXU-3hFFmGRRXfaAIWO8Rxaeu-qyNimb03sOAMPRODo92JK941ya5Xnv1uYXm1d27aInAQfLA1TP59A19yJD3xLZpwJB2uv6wQO4dGA7KNk0wqFcFEGoawoNGji4vfNzX6IN2dKJh176u5tFIUESIK_CPdqYwf8ShiLQ1wkpdslV2ahU-SdfIt1U42_JbWTmpxr1vNwA7j7I6zY97Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرم هایی که چنل های دیگه با اسم vip ماهیانه 2-3 میلیون به ممبراشون میفروشن رو شما بصورت کاملا
رایگان
میتونید تو فاک بت دریافت کنید
💸
🫶
فقط کافیه ۲۰۰ هزارتومن اکانتت رو شارژ کنی و با مدیریت درست فرم های یک روز فاک بت رو استفاده کنی تا نتیجش رو ببینی
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/100539" target="_blank">📅 21:29 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100538">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QhST48KjFbo2No_aio2j2yq0JrUc0e2SYVQB6xKmlF5NxbKXN1tNS7wLWQrLMJdLfPOWCmkPPpTswSQ_S1hDyWiAdjBiCJO5EBnEQkv-nOJEBUZpi7QmvcGn9tLv7QIZTaMEf9f1uKhg75j9E9bLpcEu_icBbLl2KOZc88Smcb7MniNIV9ZVRgb-jkiOq3eJ6fwbuVuWyPhr0Vn7Hl_yy7vk5MsvkrtN7wk6RaTCQMRdvrLcnoX9SA3AmmUsqr6-d5Wu-XwB_AVTxuLrDDSSd9kh6VcX5AhHIGBnEv02u01JVNSWYZ0kSfUZLcAdjdr0S6zSlYI9IQd9Uk0xJiaFug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🗞
🇩🇪
#فوری
از اسکای‌اسپورت: اولیسه به بایرن‌مونیخ اطلاع داده که در این باشگاه قراره بمونه به رئال‌مادرید نمیره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/100538" target="_blank">📅 21:27 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100537">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RtavzO07FRDfm_pmsgqc_-gVpP1SsouPyEHK7aISiddicF062lbXgH9_6n-v60SDSSICuALxxJfoA_AUtczFB2W2vThUyVaCPFRAVFLvPDqAv-0veZsKdkCKGkAo_yngh8Dr0Cbzn6xfYnZI7hhvSBwmL_KYM2NgZZfipBkPf_nXDdiZj2bJMaXyJo7GcatPggNryX06pvPJCtrsI48Y4kBCFrcCw-h-4nGwNPoS3jI7V-I5FVYB5k6yX_735FoLsVIFJh28bVeOpE0Evg2xvKzxqqvlp6Vcie0XWvWaZteoIPhG2RYg0M1UId1n1mVJe1V-M2qi4ew5n-Cde1z1UA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😆
یه‌کم جمع و جور تر بشینید مهمون داریم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/100537" target="_blank">📅 21:27 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100536">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🚨
🏆
🇺🇸
سخنگوی کاخ‌سفید: دونالد ترامپ در فینال جام‌جهانی حضور دارد و به تیم قهرمان کاپ را اهدا می‌کند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/100536" target="_blank">📅 21:21 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100535">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/378abba176.mp4?token=RuGVi7Q42px-CYJVxblmYjapExe9agxwOS53pbvqmtviLSgPdrfSnAT53tNXxrEh0nrBUk-wUvjMF_wGNSYePS53iWqNAn5e7V3BpVxnnT7JInx5yDESNrMVsv9-ET-HqTbpzNgMK1oW6A7RxN4h70DKgmXXEgP5M499nFWUID9kMFGilefDF82PidOjLWV0S3kufUhu9fp7BmD6QCKbTlV8f4cwoZALNz8LOJK29-Ml4diy47m9FlOklRHUNqr9tZMzYcOSLb0gx5_bW7tQboaAR5QUzFKgZG2Sqj90roW5Fv809TFjM85zW5U0kM3Peg802nYwbqmatkvXffOaSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/378abba176.mp4?token=RuGVi7Q42px-CYJVxblmYjapExe9agxwOS53pbvqmtviLSgPdrfSnAT53tNXxrEh0nrBUk-wUvjMF_wGNSYePS53iWqNAn5e7V3BpVxnnT7JInx5yDESNrMVsv9-ET-HqTbpzNgMK1oW6A7RxN4h70DKgmXXEgP5M499nFWUID9kMFGilefDF82PidOjLWV0S3kufUhu9fp7BmD6QCKbTlV8f4cwoZALNz8LOJK29-Ml4diy47m9FlOklRHUNqr9tZMzYcOSLb0gx5_bW7tQboaAR5QUzFKgZG2Sqj90roW5Fv809TFjM85zW5U0kM3Peg802nYwbqmatkvXffOaSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😆
😆
فنونی زاده خطاب به جهانبخش: اگر تو ایران بودی یه تیم دسته چهارمی دنبالت میومد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/100535" target="_blank">📅 21:21 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100534">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/47fe3526bc.mp4?token=kHC78rqL__NsIsiTLKkjQUPeCRWEZfDrUqg9IlgcPPDBTOPHlRPwWC8A_xjpog9FZu-uPcx7WQ1CF1R1ImBNGVkhq7OGruMOIlpuKbbhPHZdILJ-f5Gs5d4WzM4sdcRENG3OtQdw5gDQp1RK_bNoxdjoHSJex-TIBr2f_k5fF59fx2w5jcPSDXQucu9jVWzjjtvI5ZIUccvTzQguv0Sl-FTNiak3cg5U2ROOI-Z3bSdVaOK2UZK3EKb3pCuxgsYoggdNedXrX12PLEkjwWWecFH_KCpILODG0tnzOHWzSbtJ_FEroqTArwGDakixwNxV9t5tjA_YiLCSauDsQAfvWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/47fe3526bc.mp4?token=kHC78rqL__NsIsiTLKkjQUPeCRWEZfDrUqg9IlgcPPDBTOPHlRPwWC8A_xjpog9FZu-uPcx7WQ1CF1R1ImBNGVkhq7OGruMOIlpuKbbhPHZdILJ-f5Gs5d4WzM4sdcRENG3OtQdw5gDQp1RK_bNoxdjoHSJex-TIBr2f_k5fF59fx2w5jcPSDXQucu9jVWzjjtvI5ZIUccvTzQguv0Sl-FTNiak3cg5U2ROOI-Z3bSdVaOK2UZK3EKb3pCuxgsYoggdNedXrX12PLEkjwWWecFH_KCpILODG0tnzOHWzSbtJ_FEroqTArwGDakixwNxV9t5tjA_YiLCSauDsQAfvWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
🏆
حضور تیم‌هایی از قاره‌های آمریکا جنوبی و اروپا، احتمال قضاوت علیرضا فغانی را در فینال افزایش می‌دهد؟!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/100534" target="_blank">📅 21:13 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100533">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromARAD GROUP |‎ سیگنال آکادمی اراد</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MEiaZea8YuzS-qxjsxegwfgARTReyvRrnvzeJ4mD_euS7nDGn-javsJJtXZF8agtafC5B1BwLQNpj__AmGQYySF0vVlAxX5WJAIr4EWBq6oibXXdKemm-IBSKYo4JlZJ3RFEhBPMCoY2Jdw-3TbVU-cpuSxH22v0IwcTxAHk3xMgr3lIOPLcJ2JZ7k8Ur1mWD6KfSdC5iRjp1DBiq7S-VM7uxLXmdG132_uV2tVFLC-LG2LiQk4JgM9CgYexTj424NhfRFGk5FCwV1JlvArWfJQ89_o8rVyUF7PSdL1GOfdJQ_u73iS4SAV9LDJhkZyAnSd0wH_FXGU49KXoR11W5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
کپی ترید خودکار
— فارکس و کریپتو
⚡
اجرای آنی
— بدون تاخیر، بدون دردسر
💎
رفرال
— با دعوت دوستان درآمد جداگانه داری
💻
پشتیبانی ۲۴/۷
— همیشه در دسترس
🎞
آموزش شارژ حساب</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/100533" target="_blank">📅 21:13 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100532">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/735694936e.mp4?token=ce_1X5D7Jthk8X2a4dGFcpKrJCpNr8-eT2IjNrMJEASaGN1ddTe6LiILZlaVtlYAbqOvng7xt6E4rbx3Iv0IVIjQbhXxWIyRez_sspbgveT3bG48oM0SHM_lVw60PLud_WxgDVRWfpV9SizL-kAM-lPn8jm08JUr7Ow1cI0BTMiMspe65yoM1vi_eERXMuPMyj1-RTQqgNfpztIxKuPY0eZeOBjPCOFNaCnaLufpiFkUHjDQ1wBrble1PaPyB1-ATg2IRCM48r1GsTuMXFVTyieTu20_SgAkv88MukQyXHmvOLiDq2ZJ5VDc_mNyDiDvlPuIDNMNamtpBSsf43R0nA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/735694936e.mp4?token=ce_1X5D7Jthk8X2a4dGFcpKrJCpNr8-eT2IjNrMJEASaGN1ddTe6LiILZlaVtlYAbqOvng7xt6E4rbx3Iv0IVIjQbhXxWIyRez_sspbgveT3bG48oM0SHM_lVw60PLud_WxgDVRWfpV9SizL-kAM-lPn8jm08JUr7Ow1cI0BTMiMspe65yoM1vi_eERXMuPMyj1-RTQqgNfpztIxKuPY0eZeOBjPCOFNaCnaLufpiFkUHjDQ1wBrble1PaPyB1-ATg2IRCM48r1GsTuMXFVTyieTu20_SgAkv88MukQyXHmvOLiDq2ZJ5VDc_mNyDiDvlPuIDNMNamtpBSsf43R0nA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خیلی وقته دنیا یه خوشحالی از ته دل مثل این صحنه به ما ایرانیا بدهکاره..
😞
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/100532" target="_blank">📅 21:10 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100531">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/L3dfIvvFyShlT8rhRMzS7uivT6_ZzKvGcPG_FDtzD4vRlRU_Yg7klY1m2g3UdYhnStOY9YejUUoPaQCruvBvOtrFEQO4WJEQp4niYlEAstWEyY1ZsaAAKOA1VCyXO4TS2wArNumWjF8aBuow_bE6ZWywdEQtT3Fnbwo5vO0l4PA3awSR8fBT7nhfeNH4wL_wlkcL72H31zQtREawAIkQewFncbeSKkpzcs34vBR0jOOWUBcQX6f5I53xDgQg0FJKo8DNmxwSjtX4hCh3ls3YOmlA98xImrjVyTqaebo85_5h-yhw2-fUJPgnBuV8CUpqDMgP9Cirx9z5Zt8Os5agEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
فابریزیو رومانو
🚨
🚨
🚨
🔴
کریستوس تزولیس از کلوب بروژ با مبلغ ۴۰ میلیون یورو به آرسنال پیوست.
𝙃𝙀𝙍𝙀𝙀𝙀𝙀 𝙒𝙀 𝙂𝙊!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/100531" target="_blank">📅 20:53 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100530">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aJfZv3OxRI7VRZSONcMqriaSTLniGYeXOJqbOBueoHaunpdxqtrioUhFY_XbCG-xlEIUbpzebiHZg8w4IbnI_3BCoaqADCj7M25vb_A-cYAU_ucnZxg0_0OagWpC0c3TRJvNjhbWfbC1FDzzweTSzGmyO9mdn8npxJhf5vA0SFXWKA9uyTm4Rr8a6Rcxb_nU9xo-wWkFNn1BdoTqFhlJF9hz4457v4ju0VoAgkaXBx-ZumpNcTe8vg2EG454F7n7InihSHK9bibIs7us7szuzr3IwMsqWL8QTk1jHSEJ3e_4Yg8wkcSOFnSgyFUHkbK9dnsp0eEWX1RGUtmelaXEGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🚨
🚨
لیتان، رئیس باشگاه لیل:
🔻
ایوب بوعدی باید برای یک فصل دیگر در تیم بماند چون باشگاه لیل در لیگ قهرمانان اروپا شرکت خواهد کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/100530" target="_blank">📅 20:39 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100529">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">لیگ ملت‌های والیبال
ایران
3⃣
➖
2⃣
آلمان
🇮🇷
25|26|18|25|15
🇩🇪
22|28|25|20|12
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/100529" target="_blank">📅 20:32 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100528">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ec19c4e50.mp4?token=LIIcB6Ty2_WekF_QO1fyABmApgRIXurfNv-M0S1dSLeFufba9i11GF-b-Bu7Gwv_PwYoVkmEHRSOw4gn4BQeWVNvfThebyRlbHbP5SbREra-nh8rTJLNWk22gcfi_x8QnxLU37gNXMzC6Kvj9gqyARx9TXszaX_ymagRMTpRlFSVI7urbC1xoBHJ6sqaiFAcvQrhO0gDQGpPw67pH2yaFOjhkHMazdrcAK7fd3o8hhAB3vbInTiQjp3F41fwVbEji116-jW8zKDq7RNcyGQohbITkLZ4UEhSel51lLx7KVkobLyOiFEcTJ86X7K-vtZcgDt6fzM3l0z578XuhsdOrg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ec19c4e50.mp4?token=LIIcB6Ty2_WekF_QO1fyABmApgRIXurfNv-M0S1dSLeFufba9i11GF-b-Bu7Gwv_PwYoVkmEHRSOw4gn4BQeWVNvfThebyRlbHbP5SbREra-nh8rTJLNWk22gcfi_x8QnxLU37gNXMzC6Kvj9gqyARx9TXszaX_ymagRMTpRlFSVI7urbC1xoBHJ6sqaiFAcvQrhO0gDQGpPw67pH2yaFOjhkHMazdrcAK7fd3o8hhAB3vbInTiQjp3F41fwVbEji116-jW8zKDq7RNcyGQohbITkLZ4UEhSel51lLx7KVkobLyOiFEcTJ86X7K-vtZcgDt6fzM3l0z578XuhsdOrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
بلینگام، درباره بحث با مسی:
هیچ مشکلی نبود فقط داشتیم درباره صحنه خطا صحبت میکردیم، خیلی شلوغش کردن! بازی کردن جلوی مسی واقعا افتخاره.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/Futball180TV/100528" target="_blank">📅 20:31 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100527">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63f42b6ddc.mp4?token=G5zIT3nfk9jtnu6KsXyVLUDLN50jQMNhOprP-CYbadA-4ov4qzWdVBTCSk10u-oRzBkJOk-gDHtObLfJjYOQTL51xicEkc_NAMkLkRtRgKmOyAO9WfHAq4fbxAKA4dPen24FMYxmZFP5w-1aFAluIHuXnN-_uRQXeIp-z26hfou6ClCtITLhx_SCCkGVUHy3yTEE4SpdrUTYMNDcGv2f9Vdocx5l7UFr0msf6jb13B4_abcRLkN7JSEKE-uepAFoV2qWoTOU8yB8LR8AnIXNgzkH0FA-ANsnD2WbjdyothVHBKU4InrUMvov-ffwbAm1IVugK2_Ct7VB0DEFY0RYW4RsmasKaBdyss8V10zA09vB7gaUH5Fgjc4A-Zer2qaUz9KLw3DykfkIMEp9_LJknQLLN2fEwa_srvXA8SODJ_DiFCLDwb5XECbfrZ3PpHRxK-s-L4vDMVsZAt04sPiJPy8mxjSMLeYRPACt-AgLcK_ceia8O8jmAETupUAWXNb1FSFmaSvlg2YEt2usXj-FG9hJtp5H73LxYV_6Y7usoG1cvkwLkFBxKitDhNe2BdnNXRm9M8wqcQ5s0lbOByMXRyWkbqFyMaSNrF72ErMFgu22yRK8o4TABcK5HS2bUIjLTM5jLzQ3b2usWG9IKdkn1L7PuLQ4WaOoJopiPfFZZ0s" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63f42b6ddc.mp4?token=G5zIT3nfk9jtnu6KsXyVLUDLN50jQMNhOprP-CYbadA-4ov4qzWdVBTCSk10u-oRzBkJOk-gDHtObLfJjYOQTL51xicEkc_NAMkLkRtRgKmOyAO9WfHAq4fbxAKA4dPen24FMYxmZFP5w-1aFAluIHuXnN-_uRQXeIp-z26hfou6ClCtITLhx_SCCkGVUHy3yTEE4SpdrUTYMNDcGv2f9Vdocx5l7UFr0msf6jb13B4_abcRLkN7JSEKE-uepAFoV2qWoTOU8yB8LR8AnIXNgzkH0FA-ANsnD2WbjdyothVHBKU4InrUMvov-ffwbAm1IVugK2_Ct7VB0DEFY0RYW4RsmasKaBdyss8V10zA09vB7gaUH5Fgjc4A-Zer2qaUz9KLw3DykfkIMEp9_LJknQLLN2fEwa_srvXA8SODJ_DiFCLDwb5XECbfrZ3PpHRxK-s-L4vDMVsZAt04sPiJPy8mxjSMLeYRPACt-AgLcK_ceia8O8jmAETupUAWXNb1FSFmaSvlg2YEt2usXj-FG9hJtp5H73LxYV_6Y7usoG1cvkwLkFBxKitDhNe2BdnNXRm9M8wqcQ5s0lbOByMXRyWkbqFyMaSNrF72ErMFgu22yRK8o4TABcK5HS2bUIjLTM5jLzQ3b2usWG9IKdkn1L7PuLQ4WaOoJopiPfFZZ0s" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">علی دایی: «ما شکست خوردیم، به چیزی که می‌خواستیم نرسیدیم.»
کریم باقری: «همه طلبکارانه صحبت می‌کنند، در حالی که هیچ دستاوردی نداشتند.»
عادل فردوسی‌پور: «چرا باید برایشان مجسمه بسازند؟ چرا باید درباره استقبال از تیم ملی، واقعیت را وارونه نشان بدهیم؟ ما هیچ دستاوردی نداشتیم.»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/100527" target="_blank">📅 20:22 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100526">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vTZBuPqhh9qy5_1CEwp4bRnpkKa7z4XLEOyqZPvkZvzVn9W0pCoMzX2z441OG0ZxXDxehRh90_z5KCgupzON6w19gP3BHfZ7oIVfz8myu-j4s03kfyTEVD9wTjrLuJJW3ink4HfOPDPEkCMl8rM5dWLcohsIfppR5OhH-wobbuGGSQN1rywzCa3-XDRB0Y0CKUL7MLytpF9G_I7ZXZ1Bb1LnJQrPJuLEPk383KgGXu3iFqxqQOpdOh9kusRR_Z478cBvc6ni0zaR7QNCWzRq3PCEso2ZPC4lzoLHDmwT2A9GjRjy94MkiwIZG6lEDAI232W4MyUdwuj1ZdrAx4-toQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">�
جدیدترین پیش‌بینی Polymarket برای قهرمان جام جهانی ۲۰۲۶
بعد از برد ارژانتين در برابر انگلستان
🇪🇸
اسپانیا:
۵۸.۱٪
🇦🇷
آرژانتین:
۴۱.۹٪
حالا نوبت توئه؛ از داده‌های بازار ایده بگیر و پیش‌بینی خودت رو در
Betegram
ثبت کن.
🎁
۱۰۰٪ بونوس رایگان اولین واریز
⚡
واریز و برداشت سریع
🏆
بهترین ضرایب بازار
👇
همین حالا ثبت‌نام کن:
http://betegram.com/affiliates?btag=3_l7</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/100526" target="_blank">📅 20:22 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100525">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aNz2Nj8JviZM6cSsizcEhJQtsBKHUu6kdmhSQPUFSE76ExsIcAs_gI1HnyPs9e_QCVRItEeUVwI0gXOAhssKQgcFwsCkZ5duzLnQL1E9SvmpmcNNJZZm6V-LYlj9kAmtMvlAlQP90exJPRRw9bHP5el-_GJBrSdqZwGt2vPJpIcpgMH5uVZ2BMroa-XN8bvYdXBVL5MMpWj5IqLttQh4qKXYWLI4ij2NiZhZzhc5vin0k_V319ku1N_FSeSmz-igAH_6h8i23U5mC1RwcFMjsqtm4rumI-bb1jcI28QeSlLqQ_xkHhIcnwgBlr91wymUN8fC8pt8BKXzlSv2xmf_MQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
عشقتون تو تمرین امروز تیم ملی آرژانتین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/100525" target="_blank">📅 20:19 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100524">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d68c789aa9.mp4?token=ftaY9pflbT9n0AdX0jDT8IgAsttsE3nsK3rZIHtOxXz2zzGqiaT8e2F-V8500hpNj-wzOFF6EXtCXhNzmANKHjnQyX1v-xN_6sxQ00Q767-dwPIbCeNAPX1ckzZi2-KGnUMjETBR70bwTlfZ8TTFmbcPkDeDYS7k7UMS40j7n37Y2XN1tb0kUMbz_xxrHpvyROfOTeybAdeEhMa8URhOro6McVncq2sPxDbp0k5ynVdrGWI5s1pf6VbYly0pARjNF627TqnLafeUWZvliqN3o5A0yfvsg0hHr_L5CcUzz9ag2dJu9-cCLA41J-IXxZ1HwPpTTAIxa2S0tg61dbYfLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d68c789aa9.mp4?token=ftaY9pflbT9n0AdX0jDT8IgAsttsE3nsK3rZIHtOxXz2zzGqiaT8e2F-V8500hpNj-wzOFF6EXtCXhNzmANKHjnQyX1v-xN_6sxQ00Q767-dwPIbCeNAPX1ckzZi2-KGnUMjETBR70bwTlfZ8TTFmbcPkDeDYS7k7UMS40j7n37Y2XN1tb0kUMbz_xxrHpvyROfOTeybAdeEhMa8URhOro6McVncq2sPxDbp0k5ynVdrGWI5s1pf6VbYly0pARjNF627TqnLafeUWZvliqN3o5A0yfvsg0hHr_L5CcUzz9ag2dJu9-cCLA41J-IXxZ1HwPpTTAIxa2S0tg61dbYfLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
👀
❌
لامین یامال در تمرین گروهی اسپانیا حاضر نشده و روی ران پای چپش بانداژ دیده می‌شود!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/100524" target="_blank">📅 20:06 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100523">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CNyoohntecKq9DdbFg1MJjG70rxIexRYpJueul-6P_1AkVx-5W1MfFE67k4Aq6eUi393cro7VYyd-RsA1y0_YSMpN6ej9PAGEJOUt3vQPZL1Jce1cPXn5al6CcDC8Yhu3ZpAjRkJCAvmuEt9mCpaXgJ5vyZ4YZxGgenvE01wrIA6w5u5CbiVs0Rlma2mQUpP6ww1eaZ1tNC6qV9J8mhBqu9zetcLlPm2k1lmasPxfr7j9TocmytO3SduHDhjDVgi84tk3M2hwQwSK3CXwpNwRHWj_B-0N0DWXwBbNVj6dXoa9yHA6CUfxliDLV0e4ITaEAwVxyjU5RY4cNSsGiG3NQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🏆
#فوووووری
– گل
:
رتبه‌بندی ۵ بازیکن برتر برای توپ طلا تا به امروز:
1 - هری کین.
2 - اسطوره مسی.
3 - لامین یامال.
4 - مایکل اولیسه.
5 - کیلیان امباپه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/100523" target="_blank">📅 20:01 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100522">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NbmhfdqEYsGmJ-tjXnwPFI0e_dCCL7w2QL3iS-LHsUGFLvzw-DRj_AEpa3VosRX-WCTbZn9Qrz9WSd_BnhyUDviEoyKMOqGydZSt944KRp_7a7yVqwjaPl5ZAkwF4o71MRsdag8_wG3uOnn6EeHFvg8vlrTAvgfyv7OOUy38-E5KYWAmYljxLCgNhWtj5Jy_agB18PFPVPVAp1d0mQG47thpDOWJYEaSiblu8lF5a7mldJrWlIa1r9DBPBAoXThPacAPx8H4sR3gGzT8FLr1KZBdyXCAME5OoOTBD0JRqevxgjHraVDsV05kyADUCdTkwXlRj6SBMtpHjciANEupXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
📊
🏆
| مقایسه آمار لیونل مسی در جام جهانی 2026 و 2022
غیرقابل توقف
🐐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/100522" target="_blank">📅 19:58 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100521">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/62c9ac7d18.mp4?token=W5WD_rMh2oTSG3_i0kJhMV0-igI0Psupc0XJOKdO51Zu5MWzjbykJ4eH2xM5ZLFpIpigspPhXRiIdwEKLaumCXPG46zhci5WfuOO3m2mq4IxQD7NAi6JHSaoKEOYUaeKx8UCb0ccukkmf3Zg-kJPwFaMxN_sIE5r5OlZYz3ZD7rmhQEeR7jRBjmQFHMkJTNJ2LseKtI9an3UvAppyT2s-wGwqoLhRcRYVIHZMgZQXkQsh4ec0ImHHaVDIpIydHm2_VOWnUtLsj2y0-FHBIKq9L6k4SUzOBGJEgL6mJND93hTOINB_Vil8EeJSloto3q30fiKoNFWM9roA04Z1L1NrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/62c9ac7d18.mp4?token=W5WD_rMh2oTSG3_i0kJhMV0-igI0Psupc0XJOKdO51Zu5MWzjbykJ4eH2xM5ZLFpIpigspPhXRiIdwEKLaumCXPG46zhci5WfuOO3m2mq4IxQD7NAi6JHSaoKEOYUaeKx8UCb0ccukkmf3Zg-kJPwFaMxN_sIE5r5OlZYz3ZD7rmhQEeR7jRBjmQFHMkJTNJ2LseKtI9an3UvAppyT2s-wGwqoLhRcRYVIHZMgZQXkQsh4ec0ImHHaVDIpIydHm2_VOWnUtLsj2y0-FHBIKq9L6k4SUzOBGJEgL6mJND93hTOINB_Vil8EeJSloto3q30fiKoNFWM9roA04Z1L1NrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😃
کل‌کل بامزه دیشب عادل فردوسی‌پور و علی‌آقا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/100521" target="_blank">📅 19:40 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100520">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UhdG05Fd6T9DzDv5_mfxR2egaIZJ1p5D3d_UwdHKfHJBt1u7UhF_E9_lJo7oVXjErnLyJLvKioShdIB8nhdqyGmyJ9SZ1t-x5I6XJjeauOnzxMxvzS6MisQ8JFLHjR9mafDGT7x-URYwWmVTY1_oWF175Wj4MFGOXhNjHUwzJfjfUonT6SX0bZbGPLU5npzoMQ2e6GCHrDFW6zG6JMYNpHzjkPrDVb2Xi2hQOYE2CzlDbZston_y6hz6d_q1bVpsUENIExUdOzcpwm5VmU8x9CUtROtLtv6atIRugg686aTErTBJuJoAM6FtzkNVjtlEAx3jTVjiN1JM2Gj5ueaAaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فابرگاس و خانواده قبل بازی دیشب
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/100520" target="_blank">📅 19:34 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100519">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qhZqJS7AwrahFQsggcCst2-vkCD9P5KEiAn3I07IJzTShEqek5PaB262bs_wtcbQo_OPDYJck3TGCFn_0o7Hl9uVZqwHaEv_P8DsjKPZ5LiP57OstDBDRl_v90fYNvoc1gRGW7T11Jaz3dTf9p-25DvIdE5e3rU3s9JcqRbIRfjTfAV23l5BANdQHdPHTXv9h60xMDk1nvFnAbTy-FCYOvoW6Idr5_54bCUIyWtS0y9WhF8EBIDLcfPJOyjUkcEQr4jg4u1aMyTgaoGZFPzdDCLXGydDvEkx4H4KomFe0JMnpq9NPj4XXpKQvdwB9FA52hUCWyS66mgJH7xsVCw9KQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کیت اول آتالانتا برای فصل بعد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/100519" target="_blank">📅 19:28 · 25 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
