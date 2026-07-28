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
<img src="https://cdn5.telesco.pe/file/E8_LYLo-hCQryOrexXvw3KDvoPxcmP3YV9muPtyQ3U0fJywo3m848TXcePVBZUoZa3GSQeF9NbqOxV79NawiaoFphVQ26FdmVky-SrhnMi5-29KgDtf_rv3Okqk5qclU0sk67pc-5QQl-9mEVEHgweL91BFcqx-vDsEdHCTISe7LbYRfhUDjv0aUuCoFzdRDo3U0vxz6UIfqFfEXdhsbaiEvum07yVhpza0HARGh_JA3iCxutFjMw8_umTT3DvizO69MuHvyCKRg4UL9BO3MuhU3Gq7QUlJ-aCOxhPaRCHSutPoqyQfeGQFNn-qXwB9T222Yz71ohE8DtvGCsMunrw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فوتبال 180</h1>
<p>@Futball180TV • 👥 520K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-06 11:27:23</div>
<hr>

<div class="tg-post" id="msg-102123">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aeee92fd86.mp4?token=mp95XPR_ahKJ9gZ9r4e5ELCid6cT6k-5lMgWC8knhFOxS-EBKVb4ZAfN7fa_iPMorrawEZEPr7eSmgeCzPYzkeqQPIKxC93paomEsmtMeZ-vWpUdR-ljNJHc9lJWSO8jXeIS-zcLv9ODlzBwP11EoujtWm8f7Zw8BwRWQ4jKBf2K0Oc32XK9JAT5fTOGB02o7rdHWf1MXbW0a0VoBiANssdWMT4YZbuM-tBnYcT2sHVEv6NQsqBHbGJ3C8H-oppNUOn-0FASjinOJCbRNS96u09fchXHb-M0ii-RLiiARkMEJMv8BUh07dYAKV6i2AWS6MIVB0zBRb6-UPsoqjkv1B7X2q4T24MyhWDiWtFze9GYnArArbLgJzGWkCYZzJEUF042N3v8QOuykIdxcxxOtr6fUg-Xh807He2FjtFFOgKsUOz7hXNe7hqjItrri3u820Xak6tqzaDoB_ueTIoFxDoxUNIQ_8hkUFHsYrCVH4EMKpYd5t7W2T8X4a0u3j0SlTrqjhCC9q3ZhmRe8u6RPfrbx_eOlivdTTrriVrhJ2PB7XyrTGN4hZRNMDTRU5Mb1p8C-Qgp-1hfnHIlpbKD6BeoNnMHXKGRQhUWCZ2yxO7ompbaHhmiMk1tE7vuD3Xoj3aVnNyxcAh68FUldwRfdL2F7E6o_y0rKxCouZHKLWU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aeee92fd86.mp4?token=mp95XPR_ahKJ9gZ9r4e5ELCid6cT6k-5lMgWC8knhFOxS-EBKVb4ZAfN7fa_iPMorrawEZEPr7eSmgeCzPYzkeqQPIKxC93paomEsmtMeZ-vWpUdR-ljNJHc9lJWSO8jXeIS-zcLv9ODlzBwP11EoujtWm8f7Zw8BwRWQ4jKBf2K0Oc32XK9JAT5fTOGB02o7rdHWf1MXbW0a0VoBiANssdWMT4YZbuM-tBnYcT2sHVEv6NQsqBHbGJ3C8H-oppNUOn-0FASjinOJCbRNS96u09fchXHb-M0ii-RLiiARkMEJMv8BUh07dYAKV6i2AWS6MIVB0zBRb6-UPsoqjkv1B7X2q4T24MyhWDiWtFze9GYnArArbLgJzGWkCYZzJEUF042N3v8QOuykIdxcxxOtr6fUg-Xh807He2FjtFFOgKsUOz7hXNe7hqjItrri3u820Xak6tqzaDoB_ueTIoFxDoxUNIQ_8hkUFHsYrCVH4EMKpYd5t7W2T8X4a0u3j0SlTrqjhCC9q3ZhmRe8u6RPfrbx_eOlivdTTrriVrhJ2PB7XyrTGN4hZRNMDTRU5Mb1p8C-Qgp-1hfnHIlpbKD6BeoNnMHXKGRQhUWCZ2yxO7ompbaHhmiMk1tE7vuD3Xoj3aVnNyxcAh68FUldwRfdL2F7E6o_y0rKxCouZHKLWU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
🔵
نوستالژی خاطره‌انگیز از دربی دلامادونینا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1.47K · <a href="https://t.me/Futball180TV/102123" target="_blank">📅 11:20 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102122">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7aafdb5637.mp4?token=WZrIMPGD7w6GIRtTmvX5o1OYNsMEPEZ1NJJ5dQ9w36-btM_DcHNZ1cpMielkyZKeo83J9_QW1XSN6NPcoTU3HLFxl4MEZfotZ7cbHlkW0_UFrO3SLoS_auDMb8qngJn3sh09Zrq6emBpoWfmPZj7VWMZqnMbeImgtG-EGY9r5EfKGH4mFXU7JWaVyKO5zb1B78ozJtuYo9fA0qIfqCZhM3C3gvBb79r0Y171ZYYxy38WMGHqIAr1vWV2Khk0eaJITdYSejMG13SoUEcSKkNOCkYXzVL4WmuOBRhz04uQiue_wQRzX6OaAL12Bgt1mStFCgZmbzmLuxZ-aspwcd9a9oi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7aafdb5637.mp4?token=WZrIMPGD7w6GIRtTmvX5o1OYNsMEPEZ1NJJ5dQ9w36-btM_DcHNZ1cpMielkyZKeo83J9_QW1XSN6NPcoTU3HLFxl4MEZfotZ7cbHlkW0_UFrO3SLoS_auDMb8qngJn3sh09Zrq6emBpoWfmPZj7VWMZqnMbeImgtG-EGY9r5EfKGH4mFXU7JWaVyKO5zb1B78ozJtuYo9fA0qIfqCZhM3C3gvBb79r0Y171ZYYxy38WMGHqIAr1vWV2Khk0eaJITdYSejMG13SoUEcSKkNOCkYXzVL4WmuOBRhz04uQiue_wQRzX6OaAL12Bgt1mStFCgZmbzmLuxZ-aspwcd9a9oi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
۱۰ گل خوشکل زده شده از مدافعین فوتبال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.21K · <a href="https://t.me/Futball180TV/102122" target="_blank">📅 11:04 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102121">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd7bc32139.mp4?token=usPwbeBJAJpl98QpXz5Ww80jG5pEIjd46LVcLWc9AxfF5f1ZbwV2DatN-3dCJNwc5j61Y-K0a45HE5hfw42RB7WR1Lk8iXtCNRzD8ZP2WlF0_-9LhPk67jwjQpLpXUyersjbiMsp7clrTd8Ha4pK96ur3pUxFtA0f7coFhWuJyNAuKvzQv8sL27GWR2mF4bIw9y6jXmrpMOCFleYmCNdOtHQqcNfyns9z4gnU_Hfk4lNwk9yeRkTmX52PBVEL99_q3za0Y2-W74_8Ce3uOg91jVWRFTqsqbFj9X-RELv1c3lfy5yFrNQiJjZGM-4brSpPLdA3d7cEaEq8gE-AuQfPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd7bc32139.mp4?token=usPwbeBJAJpl98QpXz5Ww80jG5pEIjd46LVcLWc9AxfF5f1ZbwV2DatN-3dCJNwc5j61Y-K0a45HE5hfw42RB7WR1Lk8iXtCNRzD8ZP2WlF0_-9LhPk67jwjQpLpXUyersjbiMsp7clrTd8Ha4pK96ur3pUxFtA0f7coFhWuJyNAuKvzQv8sL27GWR2mF4bIw9y6jXmrpMOCFleYmCNdOtHQqcNfyns9z4gnU_Hfk4lNwk9yeRkTmX52PBVEL99_q3za0Y2-W74_8Ce3uOg91jVWRFTqsqbFj9X-RELv1c3lfy5yFrNQiJjZGM-4brSpPLdA3d7cEaEq8gE-AuQfPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
خوشحالی‌گل‌های عجیب در لیگ‌های‌فوتبال ایران
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.25K · <a href="https://t.me/Futball180TV/102121" target="_blank">📅 10:40 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102120">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">▶️
رضا نوروزی؛ یک فصل طوفانی، یک عمر سکوت!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.11K · <a href="https://t.me/Futball180TV/102120" target="_blank">📅 10:20 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102119">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/krmyyWtDOz7K2ain209BM225RtRZK_pNlD8-RpV-yAMcIZpO05KPwuFB7Cy0mqysmhrXPZYuoUsonlKmGql5ud006Bz4zsg6kobs_DEVO1jA1xB5Tgqrub-hbrczF3njuG-TPX-6VPtyBq8Iekd4oFaGneThvR3PZaG309sisx7_5cF3FHNeL0P_t1gOU8eKrOjpK3sYUjRtjflrLP_uGXFiVQCGmdtgcmkEIH9IA2me8xt1QSoqR-THE0xhidzh-zu9g0rDzI--qy62GbxyCVl4at1gNKCxEBNgWyy6MMmjqf1h-D4ttRzYI0fMfVCMce9afuXbeLkwcRzEgwSIpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇹
😟
اینتر میلان به توافقی با تاتنهام برای جذب کریستین رومرو به مبلغ تقریبی 40 میلیون یورو رسیده است.
✅
⭕️
🇪🇸
اما این بازیکن منتظر بارسلونا است!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.33K · <a href="https://t.me/Futball180TV/102119" target="_blank">📅 10:06 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102118">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad2348e726.mp4?token=J44Z_q51vcX-qJvFRCHwiUJ6mtYqzqiVMxGUz949h9BDomRby5DLCPN5XFI3hMwcz8BhFO5mVem1UpgNkAXd28AYX49AFmKNsrozzdyr1hwje7Swsu9SvNlh-wL377ftyJcQMfaRMjyaCQiNnlHEEpPZCYeNNEAOu-2A7-lIgizLAJrm8W7pEpcHhx8-A7YzJqAhUptlkyh_Lcnydf5hzenljkqvOKPmH_ZZbeUm_pDzWQfSPfEuEKs9FvtEzhXgtWld3E6xF_RQM_TpsKjliYz5pwiTeFwq7iwNTvpjHKBRQxonvNHMSz9lDspYtZRWCE_4wCR9R-nFzRzM3L7zqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad2348e726.mp4?token=J44Z_q51vcX-qJvFRCHwiUJ6mtYqzqiVMxGUz949h9BDomRby5DLCPN5XFI3hMwcz8BhFO5mVem1UpgNkAXd28AYX49AFmKNsrozzdyr1hwje7Swsu9SvNlh-wL377ftyJcQMfaRMjyaCQiNnlHEEpPZCYeNNEAOu-2A7-lIgizLAJrm8W7pEpcHhx8-A7YzJqAhUptlkyh_Lcnydf5hzenljkqvOKPmH_ZZbeUm_pDzWQfSPfEuEKs9FvtEzhXgtWld3E6xF_RQM_TpsKjliYz5pwiTeFwq7iwNTvpjHKBRQxonvNHMSz9lDspYtZRWCE_4wCR9R-nFzRzM3L7zqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
یادی‌کنیم از تقابل نوستالژی نیمار و ریورپلاته
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.32K · <a href="https://t.me/Futball180TV/102118" target="_blank">📅 10:02 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102117">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3115e0e757.mp4?token=PUR13cSKw4p1bnXaacQ7vsKlcPa71yULQXVoMVqVNPwWkrc9_4BsxYCxZl-6GvmLJZNM4ZcgOQol18x0GVD9aT1kTrMOjHbbTrF5XJqukmMwp5QTzL0yNrwc3SfG8StZM3kMtqaq0tZ9Sm6wpEW7nG4YcWG_Kua-BBG6mN7ywMzdjkodXbB9VNr2UwOmiP1cJ8WvdWv2FlOlZxhI4pwIzL4O-R13IhAIbsCXQdfpJnJdcq5Q_gHjCR1ilRAPi-74ec-Ispr75XF1bkCEi4GVRUnnducRbGzM_RvooDQEyoxA_KRJANK9aCR5ooV7HdMFnU3EZyvobw8Wc7-wLuesDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3115e0e757.mp4?token=PUR13cSKw4p1bnXaacQ7vsKlcPa71yULQXVoMVqVNPwWkrc9_4BsxYCxZl-6GvmLJZNM4ZcgOQol18x0GVD9aT1kTrMOjHbbTrF5XJqukmMwp5QTzL0yNrwc3SfG8StZM3kMtqaq0tZ9Sm6wpEW7nG4YcWG_Kua-BBG6mN7ywMzdjkodXbB9VNr2UwOmiP1cJ8WvdWv2FlOlZxhI4pwIzL4O-R13IhAIbsCXQdfpJnJdcq5Q_gHjCR1ilRAPi-74ec-Ispr75XF1bkCEi4GVRUnnducRbGzM_RvooDQEyoxA_KRJANK9aCR5ooV7HdMFnU3EZyvobw8Wc7-wLuesDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
⚠️
▶️
این فیلم مربوط به سال ۱۸۹۴ هست و رنگی و اصلاح شده. حتما ببینید واقعا جالبه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.4K · <a href="https://t.me/Futball180TV/102117" target="_blank">📅 09:40 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102116">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/52dd0bc973.mp4?token=bj92_FWcgl_fd5dQoXihTBCSxMAVXRN4-eGE7sd04tNMm4fRExn3F-31__ogymY14QwWhURYKXfwm-5tHCH9R2q_dzTCLedV_267JnbCsXceW7B7065xHHPrwdiQLD2lcTmkuZleLug7ivUsLEHbyKyXmqN5-f19My_zKFKJw1ef51i-X0GR4jVxO0GqEe17Zdd4nDX5WxELv8sHwkL2QR3jZTTV5ZRwil_hXQgk9zxZ_IX27HcYlsXFH9CgmHXsMAEUbDg8ec9k_rjN-2quex8kxWb4oOK12jK1na29p7Iush0IEVyi4MNHRspJzK39i-O6YJqafvn4kQWkrihLFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/52dd0bc973.mp4?token=bj92_FWcgl_fd5dQoXihTBCSxMAVXRN4-eGE7sd04tNMm4fRExn3F-31__ogymY14QwWhURYKXfwm-5tHCH9R2q_dzTCLedV_267JnbCsXceW7B7065xHHPrwdiQLD2lcTmkuZleLug7ivUsLEHbyKyXmqN5-f19My_zKFKJw1ef51i-X0GR4jVxO0GqEe17Zdd4nDX5WxELv8sHwkL2QR3jZTTV5ZRwil_hXQgk9zxZ_IX27HcYlsXFH9CgmHXsMAEUbDg8ec9k_rjN-2quex8kxWb4oOK12jK1na29p7Iush0IEVyi4MNHRspJzK39i-O6YJqafvn4kQWkrihLFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اون ذهنیت برنده بودنه که آدم رو به همه چی میرسونه
🔥
🐐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/Futball180TV/102116" target="_blank">📅 09:20 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102115">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ffacd8024c.mp4?token=LLNYilczuRZ4G8MOWZDdYGLrdZoGwzUaY4M_X1lvvP2JTDXG_6N56lFzgS3kxUygueeGDtc1KlbUUx6MWDd_1HasXsK7h7DOv7ChT_GN02FWsDXQBgDMq0fJKxtaQgiLXVJ2AmFqV1I2pcLjoFl4MEwLBh-3XyzwZkCGIUAeKqJBh5XICAwYgmXk5NJGRt9TKif__-34JAgVKkOgHxKC5jGZfNF59ve-cbog8aji6BtlNiEZUybh_r0lyyoWk0Us5KTuNRP3pFgA_JDOoKRYx5N4jTEgayZQD1aNe2Nxy3Zsd2UBKvfyNf2XUeY_0c7efOPxsGildv7MDMaQPNSUKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ffacd8024c.mp4?token=LLNYilczuRZ4G8MOWZDdYGLrdZoGwzUaY4M_X1lvvP2JTDXG_6N56lFzgS3kxUygueeGDtc1KlbUUx6MWDd_1HasXsK7h7DOv7ChT_GN02FWsDXQBgDMq0fJKxtaQgiLXVJ2AmFqV1I2pcLjoFl4MEwLBh-3XyzwZkCGIUAeKqJBh5XICAwYgmXk5NJGRt9TKif__-34JAgVKkOgHxKC5jGZfNF59ve-cbog8aji6BtlNiEZUybh_r0lyyoWk0Us5KTuNRP3pFgA_JDOoKRYx5N4jTEgayZQD1aNe2Nxy3Zsd2UBKvfyNf2XUeY_0c7efOPxsGildv7MDMaQPNSUKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
مایلی کهن و پروین و کفاشیان در خنده‌بازار
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/Futball180TV/102115" target="_blank">📅 09:04 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102114">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d7e0420a2b.mp4?token=fME_CHYD78urNRcBBp5OeGFNiHPmJOgKC7VrOPxNQZG5500odYAO0AOKNRd6RvvFAe8E94NU3nZQY0W2_SUKv7CERAEYgBSkstW-CY3L0uLEvTyWHJKr9HyEy1tgYiS4X3aELpR2VnijqrC0rRIZ5Wjln1vdGVrhkdvX0boGIcc7WA4hoStpn7kpYEY5IAE24pKhud_yhPQV6XUnwkjHaq2VS2xYHdR83icu1i_2SX5A0kPfQ2NKcJAzCQvfaNRo7Oub0odRXW5ZpkQavQ9j6puQmi-NO32JQ8vXBtcOj3TwakRqVacrWdhlKJ-HOmgsV-XTxc5jo4xjL3W9P14QMUeJB8S9_oFL05Q3dPi7Ecmi4zZpZouhWnnXDoeM0HFxPYAxfti7GA59vyAppUJA4PCYCRfA5vI-lK8rvhFgCIAeQ4RWb--nJQScsplXL_tyWVU5Mgce3jXxk8k5Ww1n_0pECBEk0tERLvlTWsVJYoCaDJebChKiVbxQ_0bF0Z1AGSC4o34fDRZ-SNZR2B0homo67avcN3zlLOT4vgEYQkxUJCKYx3LhfYALJVnDBe5fnW1lUYURzYiiDRPeSuR2pTRst9xTnb6DRIA1OgwdXasMxJetCW5vS51KFDRnKEVmYKIKr6gRk8fbkpf1GKvvYY9-I-wL-U8_WfBckiyQWG8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7e0420a2b.mp4?token=fME_CHYD78urNRcBBp5OeGFNiHPmJOgKC7VrOPxNQZG5500odYAO0AOKNRd6RvvFAe8E94NU3nZQY0W2_SUKv7CERAEYgBSkstW-CY3L0uLEvTyWHJKr9HyEy1tgYiS4X3aELpR2VnijqrC0rRIZ5Wjln1vdGVrhkdvX0boGIcc7WA4hoStpn7kpYEY5IAE24pKhud_yhPQV6XUnwkjHaq2VS2xYHdR83icu1i_2SX5A0kPfQ2NKcJAzCQvfaNRo7Oub0odRXW5ZpkQavQ9j6puQmi-NO32JQ8vXBtcOj3TwakRqVacrWdhlKJ-HOmgsV-XTxc5jo4xjL3W9P14QMUeJB8S9_oFL05Q3dPi7Ecmi4zZpZouhWnnXDoeM0HFxPYAxfti7GA59vyAppUJA4PCYCRfA5vI-lK8rvhFgCIAeQ4RWb--nJQScsplXL_tyWVU5Mgce3jXxk8k5Ww1n_0pECBEk0tERLvlTWsVJYoCaDJebChKiVbxQ_0bF0Z1AGSC4o34fDRZ-SNZR2B0homo67avcN3zlLOT4vgEYQkxUJCKYx3LhfYALJVnDBe5fnW1lUYURzYiiDRPeSuR2pTRst9xTnb6DRIA1OgwdXasMxJetCW5vS51KFDRnKEVmYKIKr6gRk8fbkpf1GKvvYY9-I-wL-U8_WfBckiyQWG8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
⚠️
ویدئویی که صداوسیما جمهوری اسلامی تحت عنوان مستند شوک از پرونده خیابون علیخانی منتشر کرده که ساعاتی‌پیش به سبب اون سه جوون مملکت اعدام شدن!!
+ اتهام‌هایی که به این جوون‌ها زده شده:
- بستن مامورها با طناب به تابلو
- سنگ زدن به مامورها
- آتیش زدن مامورها با بنزین
- روی زمین کشیدن مامورها
-  تیکه تیکه کردن مامورها با چاقو
- فرستادن فیلم از اون لحظه به رسانه‌های معاند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/102114" target="_blank">📅 08:15 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102113">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/508992e992.mp4?token=tMQSiHT3KNdQf2usKYuYbU44bHaWnTIBe-ZCei-mViHOXlx45acu4Mp_ztI4PGHpZPhhQuPoou1LpGddX5t7s8ZxieS8NLPJAStyvoyPGi7OiM-vlkPYvRoHWZjL4QNzIQ3EePzstQVOMwqrv-ThqIvQM6CxeRH-6DzRmU0beFmqU70_lYHENq-vQwBOWKRtK2_yrOXLZwsJnUOkBk11UigJ8UX3Uw1Yr6sef1jJ0x7qymFF9Ua76wb94DobiZgyvHmyFuoTIv_zMjxx02o49jMiz5yl7FIixOkl4RjCg8J-iGOnQwB-c46FssJVhYHJl0-fovFr5NTfSM-j0E1yFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/508992e992.mp4?token=tMQSiHT3KNdQf2usKYuYbU44bHaWnTIBe-ZCei-mViHOXlx45acu4Mp_ztI4PGHpZPhhQuPoou1LpGddX5t7s8ZxieS8NLPJAStyvoyPGi7OiM-vlkPYvRoHWZjL4QNzIQ3EePzstQVOMwqrv-ThqIvQM6CxeRH-6DzRmU0beFmqU70_lYHENq-vQwBOWKRtK2_yrOXLZwsJnUOkBk11UigJ8UX3Uw1Yr6sef1jJ0x7qymFF9Ua76wb94DobiZgyvHmyFuoTIv_zMjxx02o49jMiz5yl7FIixOkl4RjCg8J-iGOnQwB-c46FssJVhYHJl0-fovFr5NTfSM-j0E1yFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سپیده دمید، اما روشنی نیاورد؛ گویی خودِ آسمان هم داغدار بود.. صبح آمد، اما هیچ‌کس از آمدنش شاد نشد؛ انگار خودِ سحر هم به سوگ نشسته بود.. ای صبحِ غم، مخند که امشب هزار شمع، در ماتمِ عزیزانِ خود اشکبار شدند...
⚽️
@Futball180TV
| Quf</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/102113" target="_blank">📅 06:52 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102112">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gKgKfgjjf72kUuTdiL2qkES6Vo6NsJghQZ_UqxpWzqAfIKa9gMv9bnz4SMwr5mdPorlquVrxEgEP9C0TNkBz4BSW3hWkS01bfVRtpQFWtipFOD0GezoMKgCsf3dSRFbQwnn2JnuPsrEh_hQAZ-4pavRWJ0h35lQ5p-hCDj43_i8BnQzKbnCWSDT_ZbUXsLJPBpkutcACWBSz1zUp-WeZ6NbD5NQz8SgXiCGfL3m3RiZiiPgGezMXfpph8yJPF10JLlCqs1LH0XkeXD8kTfBcK1mTwRXYOI6jrY3jQAnbxOxQTvXi_ieAK8u4uqVuPNHGQcc5PskquYhuZ0BkuVk26g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🇪🇸
#فوووووری
از رومانو: پرز مجوز مذاکره و عقد قرارداد با رودری رو تا امروز صادر نکرده!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/Futball180TV/102112" target="_blank">📅 02:01 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102111">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N02JxZEPcBmz5_mtfLPLOTZ4_45hzww0zn0_V01eBrLW0_zdNxPpK_T9aOuhdI8ausEe2cYt9EeE13AUCi0RHN_GX8rr_jaO2SF1qOqwFmWs1WbpBOOX0HCVoFn7h0wmcPw6iw4BLYuIxTBqsqvBYl0IZBeU7gAmq8rzG1mo9gTz3tIMZPsj-xBS_a-ue9m3EcW5e1guLdo51nFDg6mvN0GdMZhk8C9Rg0EBknhQ2JlQnHy012Sx4buUlvyOCGEldUGTTx6OJwR7exJfV3SNEC7o2oBPFHJZV-uMdD_PjMpBhqtLwcC0pGZx5naryTPV2LWlaz4UpIMsyxT08vCuig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
🇮🇹
افشاگری پائولو مالدینی از وضعیت وخیم فوتبال ایتالیا و دلایل استعفایش:
یکی از بزرگترین اشتباهاتم این بود که اصلاً این سمت را قبول کردم. سطح فوتبال ایتالیا به این حد سقوط کرده است، و دلیل آن فدراسیون است!
وقتی منصوب شدیم، فهرستی از سه نامزد برای تصدی سمت سرمربی تیم‌ملی تهیه کردیم. پپ گواردیولا بدون شک گزینه اول ما بود، در حالی که آندره‌آ پی‌رلو گزینه سوم ما بود.
ما مذاکرات خوبی با پپ داشتیم و به توافقی با او رسیدیم. با این حال، وقتی به فدراسیون اطلاع دادیم که به توافق رسیده‌ایم، به ما گفتند که نمی‌توانند هزینه دستمزد او را بپردازند و گفتند که باید گزینه‌ای ارزان‌تر پیدا کنیم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/Futball180TV/102111" target="_blank">📅 01:59 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102110">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c83412a5e5.mp4?token=CQCB61MtC2nAzGKWMNF9ajYK_pyaTyh9WFIGr6aENZtL-Tk3aX7c43GqmJAe6f9B3mPn8Nq23rC-NFr9D0KJTNgVsoNecl12-yZaDVuA-8RkFXKcSFmsWjVmVDxHBabAH_uBgUEdXctd4mVJcHorjkcb_aIKi_xBtzC96mHX2ySVZDLQnIcdMiECv9GHvEhVfrq8hLX-Z6DLbKal0_BZ1O7Zoeq7DaMuSwYMAqG-kIExqIsLTnAEJzw_xg0plMklTz3BhVWgn_Sbaj-0F6HKc6w9F6XLXNkLVduX59PP68WEgz1LvyISJoawUNp9CHSykf8lcMMhEVs-EpPc3IyAQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c83412a5e5.mp4?token=CQCB61MtC2nAzGKWMNF9ajYK_pyaTyh9WFIGr6aENZtL-Tk3aX7c43GqmJAe6f9B3mPn8Nq23rC-NFr9D0KJTNgVsoNecl12-yZaDVuA-8RkFXKcSFmsWjVmVDxHBabAH_uBgUEdXctd4mVJcHorjkcb_aIKi_xBtzC96mHX2ySVZDLQnIcdMiECv9GHvEhVfrq8hLX-Z6DLbKal0_BZ1O7Zoeq7DaMuSwYMAqG-kIExqIsLTnAEJzw_xg0plMklTz3BhVWgn_Sbaj-0F6HKc6w9F6XLXNkLVduX59PP68WEgz1LvyISJoawUNp9CHSykf8lcMMhEVs-EpPc3IyAQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
✨
روزی روزگاری ایوان زایتسف بزرگ و افسانه ای در خط سرویس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/102110" target="_blank">📅 01:45 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102109">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ybq1YgKOGHULljLy9Qek0vILtHE98QARS4DjLwh7gm0cwh7q9jw7zKTiqanvTIKyIcQgg4z6NC_1YVcsXAZb8LaUPfjaG9WhaLewRFyClATUp46DUbghb8w9LJgB721redL5mX1JnH-E3nEt4mBxWw_XZ1rb_tRx-CX_GPz0AiQbNW0NQHaYyIsKz1EtAlfjbu2deCzbvGoeYYhvEc_SYUy240SHK5kLoeWk4yaSMjS_cFrE-mC7cBts-kVQ9zoWCzbDom4o0J1z1HCxEN0RMi2zzAymLW8E6oou4skMt6hF4ZYDz1dl2AhCgUoO_5MYfFazCKIeVCTVKtSCtz4k-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔥
‼️
لیست گران‌قیمت‌ترین نقل‌وانتقالات تاریخ که ۵ موردش مربوط به امسال هست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/102109" target="_blank">📅 01:02 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102108">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uox_YV19fAFDhI2049w9ibmGW1jnmNoY8ZivgNdSZ-sXojkWYFd7yXNc3vqm81j6b3-nSp4E4HrCQU_ORkuGVulZEbtrzJuMAEoOlpJEwXGlx600LZ0MLM2ZSQetoSylTD6VyjTJcaYGDgcWlccFN8locHJlgMTW353vavOeFwjLRWujwYaExtEPA3Fex1lz9dzMCLavy6Ut8vDbXbb9YjhJIINkDoKmIj8kulKypQXcniMe-DpLQhzPWHPUSbX9v7My60ZZfUaTBdJvsjca0dwhboMALIIO3Qliih8ZG6vFU4hTVv8vG1a9OWBEg68vsJf7toiK9nbFwAANUf7CFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
پینی زهاوی ایجنت لواندوفسکی:
لوا برای اینکه بتونه برای بارسا بازی کنه قید 200 میلیون یورو رو زد، اون پیشنهاد سالانه 100 میلیون یورویی از عربستان داشت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/102108" target="_blank">📅 01:01 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102107">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/316f36114d.mp4?token=JmQVm31Mn6nNGGASoVcxjRhtLdy6w8G2zd0zQVJPxvMYy9EMKPybxQd8FFDcxd0406tkCp_qya0yKLJHOCVYSXfSkxkkec92aTA-ndga5iEoITJCSL99oOeNj6trQk7Cy3RhLTWe0T4IIQiOZ7Oek5hGKfgMO7WAvHfVvSDHKstNfRguupfQWAzzJr_373ubvN-kdYBSIykTPopM53KPeONeGbe7xWvhwNSClHLkJBc-4a9TulkrL7or7LNtx-uC2wwoEBjJafMXEL3kqAOLWCL72K83TekmkOg_7l43N4AXScu_7EZPKYpqdPQ3LAVb8BNkSlhyMDhX6s5Uf8W5sw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/316f36114d.mp4?token=JmQVm31Mn6nNGGASoVcxjRhtLdy6w8G2zd0zQVJPxvMYy9EMKPybxQd8FFDcxd0406tkCp_qya0yKLJHOCVYSXfSkxkkec92aTA-ndga5iEoITJCSL99oOeNj6trQk7Cy3RhLTWe0T4IIQiOZ7Oek5hGKfgMO7WAvHfVvSDHKstNfRguupfQWAzzJr_373ubvN-kdYBSIykTPopM53KPeONeGbe7xWvhwNSClHLkJBc-4a9TulkrL7or7LNtx-uC2wwoEBjJafMXEL3kqAOLWCL72K83TekmkOg_7l43N4AXScu_7EZPKYpqdPQ3LAVb8BNkSlhyMDhX6s5Uf8W5sw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از آمار تا پیش‌بینی
https://t.me/+L5I8ulM6jEc2YmE0</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/102107" target="_blank">📅 01:01 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102106">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bQ5PHv0NJ8x-JaOtIAdjT9RSDzY7WNb77cBAF1dMjyETgfYC92feMGQpOxMS_lXKYsihec4QaRvJ-TkWyu_UcZFhm0sadnayH9115ncPDhohaVoCuxxliutGvWtDfdS0G6b9zknSY-WroGjNEOmvUPDQfzYb6qQLQ_rV43PJbSFAXKMv77CEauwv0jf1dX8fCfmRCMtlLeFH-XEX0GPKF2CFGuJKHx5CdKziXXYvr_wa6tl5JjwdP_D8h4uwd7Y8-POrPXyLyezcVFbhHUZOkbyEepypdHhrDzjUq8QQronXn1wVWRCzL-fLXuiUYfFstB7XtAmjoZVnWKYdPn3l_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🤍
🏴󠁧󠁢󠁥󠁮󠁧󠁿
فلوریان‌پلتنبرگ: رئال‌مادرید از علاقه آرسنال به وینیسیوس مطلع شده و اولین پیشنهاد رسمی خودش برای تمدید قرارداد رو تقدیم ستاره برزیلی خودش کرده. از طرفی آرسنال هم آماده ارائه اولین پیشنهاد خودش به رئال برای جذب وینیسیوس هست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/102106" target="_blank">📅 00:49 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102105">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JvvtkGU0_NXASOWuTkYJIuuD0qA64xd6-Go08A6GmGpUtL_RLEn9Bec8IUtSVSCNUz9iTZdldWzGZzwqdoWV25jcZj0eko70uKXz4khNfLs3wgovEp1Yqc_J7Tt4Bp9uCngUii5QiJY5yOVseL6WDUDRTPnyaKC8WN9f6hnIcS0L3c3vyPX2KlybTnO9uxzNqpdc9ims-jG9QiOgBNBp_QEUzIrgraFgrMjyn1OYZyWTKVvAjIlHiQD5QsgkOSNE4qVoCAH_53UIaKe6BAAK_mNtIIQl-qbX1PM9jfEPhL5cGrwKMLvgXPj4L2pgtqzt3HMrnuE4lqC63usrrYKIDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🗞
رومانو: باشگاه چلسی موفق به توافق شخصی با جردن هندرسون و دنی‌ولبک شده و بزودی باید شاهد عقد قرارداد با این دو بازیکن باتجربه باشیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/102105" target="_blank">📅 00:43 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102104">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/CHsMGu-BDLirHCGNBhJWcPLF2TQ_QYd3JR0Kx8bRKRve_NlkWq_22wnrR-9Hd-9ek6LMgfDhUZCsFfsv9HSyIyZHbj38Jf6UdADa_dzvrgemF9GFpVPQ15vVQPzeYAsN7lksBmmRoY3e7iByk5vS9S_r9Alau4zi6OWK7XHzVtrsBKjdpiVRK7HeGnhQPoVJKZWVocgoDtRoGk0_d5BH_wt5MGPQAyxb7hdG5w7CtB54L9bbUc8ISpWH6c7ecZqDB6ep0g0JK4hp6a_LfbFGAVelluEQXMjUDIRoB9H2S9ptaogy7Cn32lYpfwFlyEnqyQ0PsBb8XHQ1GYvLT9pBuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
🇩🇪
فلوریان پلتنبرگ: هیچ توافقی تا این لحظه بین رئال‌مادرید و لایپزیگ درباره دیومانده صورت نگرفته اما مذاکرات به صورت فشرده از فردا ادامه پیدا میکنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/102104" target="_blank">📅 00:35 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102103">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pFQKwf0uF94f8BBXeH1L2g2iyl8xPKQYn77uLysDb6a5XCCQlFV2XUeqqwQc_aqmPC50iKC7LggCdujJj1nqu7aBvYfo1H9mAeZ_PZzx6AmHodZ2t93uS9j_6NZeiunxB8jVqDpVto5BzQGkaRtX6IqID2umHOQJd02dqNtZm5cTfUbqOShIDILLS9PqXonpc_imtDykQ5eZX3KcGbKFN-YGbE4fFjLX2kghyeR7MzpJ_13v21mzsyUHZMsF0uS7bfMcaPnlb1VjjLcBaQnwYyjfr7kM02o7a2iwqRQ2U9WplxkHGGDEh4P2WUm8AivnO8f5DAIAvM3UmP6GsC2ZDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
⚽️
مارکا: مورینیو درحال تلاش برای قانع کردن گونزالو گارسیا برای موندن در رئاله. مورینیو به این بازیکن قول داده که با وجود امباپه،‌ دقایق بازی مناسبی بهش میرسه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/102103" target="_blank">📅 00:30 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102102">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n1pBgSJc-uJ-Gd65vg0tlWcvXcHeLlaA2WItRT6_5ASqnmpNjPs68k2z60zuJ9v-CQdpWhH60SoOf0awZMDQyhk7v0j1t8y6AO3HaZpn6Fd_4vBH7kTfhNbHUe33CvsxBroCKNlsBh9r7vZjmU9j8I6qb623djEvxajbC_hxhBv1HrwT7YVuzrwaPn5rXGKVbOl3N4nU7yPumY1Y-MK_qOGuiPVRICyzEAtEpQB16FUr2OoX3pNvoLwOMRdPVo9Esp9bqxF1QfmqHp4xBqkoZCeVdvINKm2fwcE47QinbVAw8dWIw_50WCIy2VDmJKG27dmm_8f7xChyruiouJ0cKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
✅
لباس سوم فصل‌آینده رئال‌مادرید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/102102" target="_blank">📅 00:24 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102101">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/52dfeed19b.mp4?token=OSbmreKVuYIq341Bi_KdNRIt1afzru83MHVJFys9njlTfai6s9a0pqnOAiBY4Jdv73tiXy8bnil-9UUZsTyxncKeQqAc13g4Ef0r0A8BFvcx0-eYbSKMl8LxeVNv165wckmn79Wa_zO7FhbUuHkpSUaNq8dU_59wyO7tNox_ybXf-B3ZS9L1dq_V4kO-7ARrTB42GZxZtn6JnV2SyTzA1muZOOEVc3onPhXKxZv4fjfaH3bFMUpLaoY7O9j3lqYNKVCu-IW17HmC6g2du__03p1naux3wL8V3Qsmn03BSuCoa-Y4BdumQsE6uC0CQEiDpGjXwW3w6MC-z6ZKYpF-0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/52dfeed19b.mp4?token=OSbmreKVuYIq341Bi_KdNRIt1afzru83MHVJFys9njlTfai6s9a0pqnOAiBY4Jdv73tiXy8bnil-9UUZsTyxncKeQqAc13g4Ef0r0A8BFvcx0-eYbSKMl8LxeVNv165wckmn79Wa_zO7FhbUuHkpSUaNq8dU_59wyO7tNox_ybXf-B3ZS9L1dq_V4kO-7ARrTB42GZxZtn6JnV2SyTzA1muZOOEVc3onPhXKxZv4fjfaH3bFMUpLaoY7O9j3lqYNKVCu-IW17HmC6g2du__03p1naux3wL8V3Qsmn03BSuCoa-Y4BdumQsE6uC0CQEiDpGjXwW3w6MC-z6ZKYpF-0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تو تموم فینال هایی که بود
میرفت تو نسخه (پرایم) خودش
و تو اون نسخه دو تا وینسیوس و یامال رو میخورد.
شاید یکی از دلایل نتیجه نگرفتن آرژانتین مقابل اسپانیا هم نبود آنخل دیماریا بود..
🥃
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/102101" target="_blank">📅 00:03 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102100">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6f39b79d0a.mp4?token=J7qlKtS6GAwiirgo-nMbE8PIO2VszLFWNyIHRc1kML4-X3qCEd2zMD_c6YLnqz0oWZVSq3ugEGQFD4p-8dzjOGFLYX9by8s6bbrU4FTQrK0TlIuAyS8aiEgcpjrOXoaFVCkgdCu62dbTwedZ32Pwk_3sB25YddAJZu-JRucrIImzvs_nWJTRYDSnPv9OY6Use6Mvu9wkZtQKgB8G2sEDIJXzLPTJT4rm-o3DiqC5GcUGVJ_dJz79AREa3FEgTmpozUYMyNutKfH5I9ppWB8JOVSo6T49ZIZEIhISpgU3RVYqPIQ2D3kkAVK5xZsLMLh17NIiMYA9lC27z0fZNEE_rA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6f39b79d0a.mp4?token=J7qlKtS6GAwiirgo-nMbE8PIO2VszLFWNyIHRc1kML4-X3qCEd2zMD_c6YLnqz0oWZVSq3ugEGQFD4p-8dzjOGFLYX9by8s6bbrU4FTQrK0TlIuAyS8aiEgcpjrOXoaFVCkgdCu62dbTwedZ32Pwk_3sB25YddAJZu-JRucrIImzvs_nWJTRYDSnPv9OY6Use6Mvu9wkZtQKgB8G2sEDIJXzLPTJT4rm-o3DiqC5GcUGVJ_dJz79AREa3FEgTmpozUYMyNutKfH5I9ppWB8JOVSo6T49ZIZEIhISpgU3RVYqPIQ2D3kkAVK5xZsLMLh17NIiMYA9lC27z0fZNEE_rA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
گل سیدنی لوپز به آرژانتین به عنوان بهترین گل جام جهانی انتخاب شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/102100" target="_blank">📅 23:46 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102099">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RihQhs__3R7GtCRLZ3b7oMPC9lINxhNQhMF9mJMnLABW0L8mfatevxnZdMIKlvDk17YvIWyR2K9DaVerkxnkmynesqvuwL9j-_UF1Qg4AFgfDyPLxYG921XZ3ncMaYYqCYEQI1P78JXATLTz_I2dLCJGptwez5MK_upgy2Jr-a8z46pXRYlk2T6UcMNyQq2Ef6M_kdHrBWZGr9WJ5lnXVpvJraM4u_YVi1C9O-1xLcSIo9v0o8Jw3E2ycmFxS_JliIIuPDJmGotmF24QXWDISkCtnVI5Ub-A-wIoe9RNq_pZb0wXE-lysb0V-XQTgpY1Qc678CXCvwr4vCZcyGvpFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
رومانو:
جان استونز به اینترمیلان
HERE WE Go
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/102099" target="_blank">📅 23:00 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102098">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aLyqK6id4V-t-IWovRQDl42kjBRwU1XpkhRMwZ1K3lbuAOyUvdMLPd98yL0yCGr_DaC-vsbuEn_asR-HsBBBk38C35sRlvjz5Sn0KOgLXrdcdxotBJZBloUhFZscDGY4dSyHglg2VRBbJovTwJx7h7RthOKljyurVw9phyCMD-NW05Su9-TCcQ3d20Z-dR-SLGy8fG7lZ67yN51OP61OByyG5IhRijqLXwtclV2i-1QjN_1D-wkXyA3hcpV09Zv0mopNHlV2T_kTt9wIRTfBf2EFrRnepQM01Ho5wWM5yJX_qOQaKaajwiCZLL_ArBqOK6By6jKPjK8UDqyaUwJtEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اندریک و خانومی و بچه‌شون.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/102098" target="_blank">📅 22:57 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102097">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hN06sHYEIyvX7zHRHmfwtJfEmU3RfRew_6wPaNpMMs_5skr2gfJY4HUPlUmSAHty_nz5WAFyb-7AEDhxteypKbfNtzeihjL_58SR__TciOK5TV-S_7vTsqxZ4TXcB7avD3R63UJQwiOLJrF05Vmf7bvCGdhuFrARcWaD8Lr72ISZ5W6uLm3ja7SQcqm6Q0Qo4Zk9osOjvqrRib8a3qHetWXHyKZt-M4HElV7wgR-BIXSom8E5Yqzy8Gvp5eBscEWxscBheNjxYYDtAGpDfY7DVPTRN8w78JyWvJUBUUiIrccTl2QvKahiNLmnfH_EYKbBABqklu5YmhRrr2XNZ7jEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فابریزیو رومانو:
جیمز ترافورد از منچسترسیتی به لیدز یونایتد پیوست. جقی 3 بار ادیت زد تا تونست درست بنویسه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/102097" target="_blank">📅 22:55 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102096">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tFjHyL3o3KwPCH1T4bsYHOQV9i1tpLyLApv0IoLToo9Z5FCj00aKFxHK-43mcAsUNJOHU_9hAsEYCmIWu6L8mUjKphi7j3-SoBn4e5sxaAYyJqQWCwLLM0Lnq3ANvHxz4H0PVKNyM0A3j--GrRex2DP_rinBNXKbmieF1g8l6iNPQCaEvvUj20ZsBwX6O1IOpXiCjHORBn9rzI8wuf3SzbEKpSYjWUTO6aJ_9cllc7z2HiOgaiIrgssQnAc_orR0LmFybj1M3Ihr7-Fvodig6vlFlSwZ5AeKyqqUqZy3X08eVFVBihDa3T6n0rTi3-WOhQFefoojuHWBFEwH84qOTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
👀
تیم منتخب بازیکنان آزاد در تابستان 2026
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/102096" target="_blank">📅 22:05 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102095">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🚨
🔵
متئو مورتو: جان استونز در آستانه پیوستن به اینترمیلان است. دو باشگاه در حال نهایی کردن جزئیات این انتقال هستند تا آن را به طور رسمی اعلام کنند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/102095" target="_blank">📅 21:58 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102094">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qW_cJnSrzYqdDbtD-fWJ-snZhQyYvQ7aYhm3IrigwJdcJg8O9pSK_x3UbXdLhxPbt9g90EMujuXWrPiWC5-BKigjPxpb9pfGePUyPCi-OJVgjxttWgsWtNID_M6l7m8NBkgkcij5bcZqdQk2gvTD8mJbuPEhvbUb47NCXBjuCvCtf4RaDq5B2vGLGUgxHY0Z5467vo_DY07Nbc2WIdLZhEOUbb_UEyZ4rpIEr4sJo7si_FafT-FELyLTKcHrs0tY1p0he9IJezkAoAamUJPJwYwtknQY1_fOO4LphkM2AHWzZcnoFyE5mOvcZSneLC1u_K_p88m8KFSmB0QsUHpgdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
فلوریان پلتنبرگ:
لیورپول گفتگوهایی را با مدیر برنامه‌های برادلی بارکولا و باشگاه پاری سن ژرمن آغاز کرده است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/102094" target="_blank">📅 21:20 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102093">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oQjs40IEYNXOK3vqVKyY0z3wsF8XCgxcxR2q0v0k-L-E5bVLa4J222RZJb30DyWo2fm8LaT9khDp93gAMl9IM2OWJV1OVyM95gUUeY0uqu7Z4_Tb0MR2sspmjkhDvmbrPTpIRifNKe1xahExr3eXyIwbdNGXeIcLQwhX90YMBHZfbkkB7WbjPk6pM3IjuIUAWFnk_uJM2xQOeDYFYfXNDf4TwfXIBj9CNVk7Ctd9zqFKqwu2y21RuU7X3by06BBycdE2gAbqswbKccUzKPAdQPY7-PjPwtFG7WwsW6AO43McBFm79eyio8fWNsiTBa7yTauRLAmeMiEPMWUWdmB7EQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
رومانو: چلسی قصد داره جردن هندرسون 36 ساله رو به صورت آزاد جذب کنه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/102093" target="_blank">📅 20:57 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102091">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WStUYKK0En3ksbIjhCgrgoQq7-BGaEuokyvALCSPVXoaUm2IIE6SwGndwc4buv0L7QbALWXwyiG6kOI29qa-sDkYC8XHAOdFElJ5OtN_kIrjcPDWLuA4RV25j9Jm9JexIveqmVbakj3jdYjKuAIt83zGW_W6kS29BlJaPRMBheOV2nN0sGEiK7BUOZa5tbcInivhNYb_L8t7EzFIjNvdg1nYDhHiZNCsuBW5TGjePiL0KsUWSzagMpFRv_E7fq-PFu5seRwDZltuPCyEdK7U9f9sUhgsDaGwYkj-faQ-ptg7GNXD6T7LVDZrnlrRejrm_KWi0WjdtYQXJ-ZBMNdZdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🗞
🇮🇹
فابریزیو رومانو: پائولو مالدینی و لئوناردو از سمت‌های خود به عنوان مدیر فنی و مشاور در فدراسیون فوتبال ایتالیا استعفا دادند.
❌
❌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/102091" target="_blank">📅 20:42 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102087">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/r80ZxSZzjKnCOkgoyiisHvXI9R6ZxDtFfAsPHmqwToJ1zqYMDro63YVOdshaPkCfdcXCNhSrJSRdcNmaZpZcUUSUu89XwMrkkFj1hUH1sxMcMQcqV9_QypIgE-SIkdeSSsU7-MYJhP6pcIgnH_C7-yztak8ttk3_oDak0vkpU07t7NNPsiSz5BdppJzoyShMX6Z2W9uS2OYdiGyKTwZFNm5oaMBsARsj_-eSUv3h3WO0pODVkvgWLzYVoCvNkWFmycHJj6weo7R6eDO3xDBwKqnj8vHVEnYIWEDV3vwuNv7gVrlf2jv3K7132wxbd-Erz_BKPIyXBTAS5i055sLSLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ge-7miqgMqC8x7xxKS7qszyxA5hZqRm9QDL_HrxIjkU0gV8ucComtzwAbfX3Tcbym6s5BATM9w1rRtPpgZA46DqvvoxCbKdnTfc7Y3qaAK_WlS9tHnbYUJJuwcsl8GsPQohY1GvMYpPbmWxW4Sgvh0K-7oMzmfwK8qppSHJba4TXTa89-iwXZE6N7Ej-DJ-Sbhs3S3q3Ppi4_OF2eqWxStQaIAnQvQRGuqu8A2BJjjJFGeW3V_WLoULM2fPgU7fYKsazuz4D91qHkMBeb-fm-x7JWgR6vwJR65mvmCb9ae0tgDdJBSBc2UhzhufxfFMnm6jYSIv6ctITeaRwjuzdcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PXmSZHBCZWMttxc0zIM-WD2cec2QSg8yQXWgVH9aWYbEbLXhICAHOBP2X1dXsbB1K_giG7_zmCc996HvamXuRHu_xMWpqEjO-R9tRhFPqZDZKMMr1tVHHnzfij2nTTIoUlNXuRGtIRsPOQdzqLgQkXQgqoSXJvANAQTeVrk5AYxJkKy1kA494wHk0T4g7Tt3naSNM2-MXaGSWvhJvF0IRI8TbfkdxcD0yVUUTx060rdzVCJrSS7HLlEHiWFoY8UAblb-KUdXkKMeAPx0kYhyZ8OT0_5-sadD2u-kzXMgAlH4odejHXmUhtYdqeRd-MZGyEZ4gVR3Q03VAMoiy0B7gQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/L7jdd1ddRYVjKQdSPKxg6ADtlzxA3Ooe-7roMtN6YlM8HRjOicT0DmbiCCAmMdv6QKFxtUm0qWKk-x8W6TUE377ldgmOzt1CWhsQaWb0joVw8gKy48TGKa0Hzcv5ymyzqeKPhHNJAdE43axJ83jypj4x8Q74cYXk0JzQvSXwALdIkuKSLaOHrRDwSZ9WMpQCp-tKLH8SPLUCp4WRGu2FvhQP3tTaT0DkqVDPL8STsSBjmpxDlGsoZBe8GFw-sqZOf335JA4Ncjhww29cPz1XEugQGXh9DFNHQqzlErsv0WCoB1eCZoXmD950aPetVkZsOss8Bi5gXERiFh4pM44DpA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">عشق و‌ حال وینیسیوس تو‌ جامائیکا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/102087" target="_blank">📅 20:31 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102086">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lWZKqXWVTD1fiN2_1mVRFiD8lxIJHUhlfZJi0wYvuFqzfISdUB6dUrjrJ8GqkJhfufcsz7pvuGAOdPbYyJaWIpFO7p1Md7vmc_AFaBPm2gP-ur-RzWrJo_EX7yXlkmzeTao2aDIc5B7Yv6jA9BztPlZtHyz6FOC5UgGcKfRFX8sb2JCOYwe16VGuZg1Z5WuxgLxfGp2fCyJ18qkph92Uus9LyJ62yRN8WlTtCDlAFC2SEbUIegrK6nopEuMgaVZ8gjjIunC-BpzGH33lH8LWppYca2dhYiBNVHH-dsLgA37F-q2xzI1SvC-dhyW-qvH8qgVjZRelTzxAK7TflmOG5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇧🇷
گلوبو برزیل:
سانتوس قصدی برای تمدید قرارداد با نیمار نداره و این بازیکن در دسامبر جدا میشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/102086" target="_blank">📅 20:29 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102084">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SjADTKszDl3gXxCbf68CtbL7JYdqjZG3IQfxqDezVC3mjFCvJy96juZ7rtYaYw-CvRI7raMdcZqhQjooT052HNpgi7AiwwKH7mL1uFC1-FnO_KIzOU5PoL5EzGxevejE4znFPt5bXQogkpJ5VFQW8p0jeQ2qhPH-wFq-OL9uPOSq5U_ZlRres6mQdqI8mDpR5Y6p-j-Wro4KhJAv58CXs3jAVi67Npkub7JmtvQ9blPC_IsQnUuOKU69ENTLBTXGHoBgGiskJ4gnuv-ahl-_2VwTAs0Pn1wdlsAtQ_V5o901ShBxQClR_CguSd1ZklIzLOFdFGnw9DA8R73axBb5yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uvi2w7lmVsAn1zGCbX2ZiDHcU9HXHAQ7DIlto1xC1FmrS-XbNeMRr4MK7bUK3K3pEyo7djyW5cFP8QloC8CTOiPMF87GeJDlURSMgZwqKSB1UTkg_rdD0W6XksQVfbm94F7z_L4APwKj9QrFZY8AQKYwXA1corYbKVPw5CDLAnPrNlAZtzcQVOwhlPQcJNx478oVh_3Q4ieGNJaGxsgXV8ePIe3yzLqBCmz6mZFBhLtV7aTGxxdtLov3ET6h7PN0E_cjoskECZauLgmKPb772aEn3jyTGGk9AT4-oWbDyhExMH_gpBSy3vuzN8vuw-O30QYPyYcZ1yGMPTygBE1TpA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎙
اشرف حکیمی درباره شایعه معروف طلاقش گفت:
اینکه همه اموالم به اسم مادرم بود، هیچ ربطی به ازدواجم نداشت. از ۱۸ سالگی که فوتبالیست شدم، مادرم همیشه مسئول مدیریت پول‌ها و دارایی‌هایم بوده، چون کاملاً به او اعتماد داشتم. حتی الان هم قبل از هر خرید یا تصمیم مالی مهم با او مشورت می‌کنم و این روند از همان اول همین‌طور بوده، نه اینکه بعد از ازدواج یا برای فرار از تقسیم اموال اتفاق افتاده باشد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/102084" target="_blank">📅 20:13 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102083">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bCmynetlTkO5R2m-AcYO6PyfYuN8lCooyxtti0aMrYnx2lE34oP6UEld-EQhpG0PyD9CHYPTId4fwEfsUHzJCngJx21pIqgnoIugGXhsQ7h348oZa4kcVuaGd42JbOebVHA0l1YJFc2YsXH7qp8dabbcWWJanKpa0eZ3UV2Rt2xQ7uf5TlzhLglKo9pI8-Y8pKfuGyOFTwKLOzM7Vv59Z6iqpCZeq5Zjx7HOlO8B4N4ZDETNXo202VlHDKH00U_xau6-WRueKxD4fWePMVRldMvdcMp-lnaudlzOhfd25OqLg57h1q3icCzPNe0GyrMv-onGIZQCJxvFVGBn1dacgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
⚽️
امار سه فصل اخیر جونیور کروپی که ظاهرا گزینه دوم بارسلونا در پست مهاجمه
جونیور کروپی ۲۰ ساله متولد فرانسه ، پا راست . پست اصلی پشت مهاجم ، مهاجم نوک هم میتونه بازی کنه.
💸
ارزش ترنسفرمارکت ۵۰ میلیون یورو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/102083" target="_blank">📅 19:56 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102082">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G8PN2EclfgcpcerOhAK3R8tH9X9ytUXkGMKSn2JNdXshg5jTwnshS_twi-mk4GiILk-KcXiuHL-8jrjFxHG-2UsQQVtlyVKmyav45WOtyejgGH4SyG2BUEdQkBZRGPdLx8GCpHw4-7g5fikwkS1ie9i9DOi4_9i39wDvkJ-gq4q3UFqQnCoD1SsgSQo0SV_JWz-yJWgj9YaEBenUhaGKWjJ6D-0pPTittxkwjG3TRcZrvCEjjyXRwBlzVkKiB00tYX4WPzcftDO2Wc6TPWQBJS_7cqTwQLgkVWREBhMpkotO09LpyPs3vtzeYe1FxouiMey1DsTDWD0uzJBK_sHNNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
قدرتمندترین باشگاه های جهان از نگاه اوپتا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/102082" target="_blank">📅 19:44 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102081">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e948c535d5.mp4?token=jYL4LwZ0ymLUop9rtcqnFaACx7C7XZb9GymTFhRdIBwltmVKSMywY3yrrHB-gRwLinrUUvCahSfvIBz_IqtMizE7vUioZS07we_tdb9W5LXor-5pLXUUDqHzBTN0Era9vhSlK4yn-09Aw3WKy2CnbXnzEzJRhRLETZfpjYQnhGBBt94LyLvQ50sqWAvBlUp7df2DjmAbkHejveQG7DYsBK3eFq8vwm89KhWdIN52yXoA_bVgTpH3SoWKuyFSRz4Btl4ZkpLr0mZtyhK7BD1oSviZikV_pleiueFxjYo8tZEgNWsbRhANHgTTh_aE5W8f9_V2OukM0VRm98DVn9pBYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e948c535d5.mp4?token=jYL4LwZ0ymLUop9rtcqnFaACx7C7XZb9GymTFhRdIBwltmVKSMywY3yrrHB-gRwLinrUUvCahSfvIBz_IqtMizE7vUioZS07we_tdb9W5LXor-5pLXUUDqHzBTN0Era9vhSlK4yn-09Aw3WKy2CnbXnzEzJRhRLETZfpjYQnhGBBt94LyLvQ50sqWAvBlUp7df2DjmAbkHejveQG7DYsBK3eFq8vwm89KhWdIN52yXoA_bVgTpH3SoWKuyFSRz4Btl4ZkpLr0mZtyhK7BD1oSviZikV_pleiueFxjYo8tZEgNWsbRhANHgTTh_aE5W8f9_V2OukM0VRm98DVn9pBYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">داستان کریر سرمربیگری دلافوئنته
از اخراج تو تیم دسته سومی‌ تا قهرمانی جهان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/Futball180TV/102081" target="_blank">📅 19:14 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102080">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🚨
فوری ترامپ: به درخواست واسطه‌ها ما در حال انجام مذاکرات فشرده‌ای هستیم. اگر این مذاکرات موفقیت‌آمیز نباشند، به اقدامات نظامی قوی بازخواهیم گشت. ایران فرصت کمی برای توافق دارد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/102080" target="_blank">📅 18:49 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102079">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dk9q41RxsWFjm2tacs9ioJb8MpafqiaMG9FhdfWcoYy0-NMLoQ7LOxwiLY08h4zBeOFxvbbpC3Mf5EaYVnPTIgwJ2vHy6qjLjSdVmkyZPsDp8BxvZrIsEDmh_7ok5BHtJBAYpZ2aIliKs3vAnDXWXDDEXHjxjQ9ufjPDlRb66T35zfm4tgfEsfR28bvxzdFqMmbu1rZ0VC-YCFCDqJn7O078liCq5VFbe4G8JyWS3rxbrbFV0LYQ1-nd0j2GHSJazasHNm0n5dofCWcBGLPbbZfEH2rA7R8KH8JJoABTjtytyItcsacHdlaE1p0emeHo0O46f1zktjrpQ5ZcAjMXKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
👀
چند ماه پیش الچیرینگیتو توییت زده بود بارسا به بازیکن های بالا نیاز داره، و حالا همه این بازیکنا رفتن رئال!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/102079" target="_blank">📅 18:19 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102078">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IB2enFBosGOIHwQCPkwayzTIyylusPHMKMB-07U9RxQZz-UlGWHq887KQ8sAq_h8acu4dbspMF1vUyxmvOCNdAhDnIx1sxuV6KMrg-d6uhyi8if9dXG-Q9i1w5wa-sj2hEAeN5Hi0iqqpedicLpDfLTAIUyyWwsJgjiIiyBfTc85ZtvS93jYwN1uGA77odRiPVZ3IcM2AGXCIJk_Jq9X-9T9a0fe1V7cyPaJIgSS-azXzPyaoCcjPz8aQ_k2MqZBCkX_MgasVai4Sou43eC1norrV-DH8eFsW7eR6XofJ6jPOhdp7rmPKuWc702pmBi7pzY-nRClTsUz7MHc_4lnmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
امباپه:
ازم میپرسن ممکنه یه روز سرمربی شم؟ نه فکر نکنم، من تو تجارت مهارت بالایی دارم و میخوام که تاجر بشم البته بچه‌های تیم میگن تو میتونی برای ریاست جمهوری کاندید بشی ولی باید بهش فکر کنم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/102078" target="_blank">📅 18:13 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102077">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kmwNr_vEixjvNb5VuGeDEmHE3d0SvK_Pv7ohzjppgit1FetVV6n9I7fl9F0leO-UbPPLOFGHngpFhs0Md3yFC-6HnWRe3svTtIBYz4FsTg3FHknp-wxElGXQ6JdCBTqcAcbOVbkhunZw5jTtYzv5OhSOkDbCmPQBgZqIsnAWs7AGK-MCDr8e7Rt8CfvbeeVMP0LFdN8B65WLN5zQfMrRWnNKyX5oU-WWUjNxVeF1RC9OYC7MSZ3Rh3KKygJMq_mapJ6O5C6CdUcTmqrlFf6_kqDQtJ7M3-rg1m3NaEwbGXZTycLOuMEBSy6VfRu4ep4SY4NLnATEUIQ7q4AQgpC2vQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🏴󠁧󠁢󠁥󠁮󠁧󠁿
بی‌بی‌سی اسپورت
:
یک قانون جدید در فوتبال انگلیس در مورد مصدومیت‌های دروازه‌بان‌ها اعمال خواهد شد.
اگر داور اجازه دهد که کادر پزشکی وارد زمین بازی شود تا به دروازه‌بان مصدوم رسیدگی کند، مربی تیم 10 ثانیه فرصت خواهد داشت تا یک بازیکن از بازیکنان حاضر در زمین را انتخاب کند تا به مدت یک دقیقه از زمین خارج شود.
در صورتی که هیچ بازیکنی در طول 10 ثانیه انتخاب نشود، به طور خودکار کاپیتان تیم به مدت یک دقیقه (خروج موقت از زمین) انتخاب خواهد شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/102077" target="_blank">📅 18:07 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102076">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gAg4nvjxn4gBWuvC6L19vQ8sEjerYTIE0gLyUrrFgw0zQLCyrVkrCqdpZzB7zwcJkWqeVLvdPvbUSTlVPkAISg0h_LnYj1DTHV61CMMXROElBsAJCHfFW5gldS_vfUJMjPp1vO3vyuMlz_YVMBfUf1gML2VWDzcGBvHntxJYGK7THoA7nYOz172w8IzxxJaBtg_f3FAIv5FOaNdmKvGUDxI0efoSrb87ALr14Ou99t-WthdJsWS49xTZX5BBsvV_Tspr1DpTmOKRaMrM6OcM0EH_wGMrjVwwjvbL8PhnUeIOghpeDi7iMOQKGqbB_SCmLu8ZRqs47jHxH2vbwbkcUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
🗞
فابریزیو رومانو:
‼️
بارسلونا با افراد نزدیک به کروپی وارد مذاکره شده.
⚠️
بارسلونا با بورنموث تماس گرفته تا درباره امکان جذب کروپی پرس‌وجو کنه. بارسا یه سری اطلاعات درباره شرایط بازیکن جمع کرده و چند تماس هم داشته تا وضعیتش رو بهتر بررسی کنه. کروپی بازیکنیه که داخل باشگاه بارسلونا خیلی مورد توجه قرار گرفته.
❌
البته این انتقال خیلی پیچیده‌ست؛ چون بورنموث نمی‌خواد تابستون امسال بازیکن رو بفروشه و منچسترسیتی هم بهش علاقه نشون داده. بنابراین، این معامله اصلا آسون نیست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/102076" target="_blank">📅 17:50 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102075">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xu_CZlEhuGoZtHlNrqrlYQ6us2bU1SRC-V2WaiQE81qYUUplrC1_0Ogj6ClNC6PHMv5aCaV6Tl1li-EC8Wao9bxmjQuspHoTQ6_VlIZnUjXmK_Da9G_GxdbzTjegvZa9YbH58K2Ir1hULtdMKhhheU5dx5n8pJ0FzSnRhtw5hqGczqAKEUfQI0uqG-hTSYU1L-06hoQlzgJ9eibLBq8JYSAcgsKrzMBK2BE-19zJ2y3QYJXRCZfDWzSvf2AI4P-2t0x5K10uMfPuhQyUT0r582T3FuE6uXdiTIS8Mf-szqAMvlJ4yRyR6EBDZbYDrFuxKdiXd53nPesKCNvLH2468w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
فرانس فوتبال اعلام کرده که بردن توپ طلا حتی بدون کسب یک جام بزرگ تیمی هم امکان‌پذیره.
📊
این اتفاق برای این بازیکنان افتاده:
🔺
جورج وه‌آ در سال ۱۹۹۵
🔥
🔺
لوئیس فیگو در سال ۲۰۰۰
🔥
🔺
کریستیانو رونالدو در سال ۲۰۱۳
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/102075" target="_blank">📅 17:34 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102074">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/czCXJ5f93YtMacoNjSm-GhMLzXLbzFewc8I0jdf4mkFTQxxgFycrXrj6KoqnqRYBE7SPsOQAECgY5-wEI39DY4iwMIhYCWPqrCK8TNqbx5QtJnvdZ1tCH6jF95p2xEwn6W17-PM8S-z7ZZd6RbUaMJepjdLqodPx8pygbz-WHhGTpttLNZaffrc-OvsMtY6VuZSLL_U53CGJ6VAYpapbkdWXDKlw9cZkL549WEjz7tOcZeOcmP0BzE6cG8khjnVTrI_T0PdOu4sCoJWN98j5zPJWWexiB5a3gBf5QR0ZDe1Ph9aN9by37kvRqZg_dgzWXCm3JeCmUXWDm9VTMK6moA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
فابریزیو رومانو:
یوونتوس و پاری سن ژرمن در حال مذاکره با سوزوکی دروازه بان ژاپن هستند.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/102074" target="_blank">📅 17:07 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102072">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nm6Igoe33qI_V3q03ogwEOWM5hwbKN6mSFLe4pvbYhYf4aiCEuJ9GzB6sAHojQ3U-QHy0ZuVfiGjLY-C1izF6AUuui6DIFjkNtjODxHZO0R9RC-eyR6m2alrUJ26mON6pRYdc8ytsJ4kK_jQd5wvAP17CcExk_MaW434dsWEMxAmPG_HxkJjlVqnKr90UlyL_A_7NBZZ86v-HR9SxJuSEyfKiXxvPDNxnf-KRPvK4niviJBGM85Hg6ZqgvSHdxifUiPQqD_lOYw-oAIql0P18_dbRu0RogJKW81Hf4-o1FRa0GPhH6ODAKyVuSiL3u3DKhUM-7LwzGSH3mlCqtqR2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/O7RXkJh8F0PYx5oVV2sO0lE7E-6CoVx3r1BDuoXuBT3DoQFuCtVbC9J6DZd1BLJM0O432ypH1Wu7P5chB_wimAQSmstefdK2W7VkZeeOCjk-BMmjOlAHGUwITMffGgdvnQfnRsmYB2q194pZjESXJuLQw5IUre1EKH_pEbej-K8pb23VsQkmsmiqgRRk5DZVa3osn2ENoeeV8yUuGaTNafXQrG6ZWOkR_PVDrUdBCeJQ8rFSUXaYTXAZh0F1Zduo7anY5CJmmFIL6jxbj4jakfijfjx4qxu4c7c4bGg1t6CX6MrnjcVwz2VplQXECsRXqmZJu5X4zpLeolOunH2tAg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎙
اشرف حکیمی درباره بهترین خاطره دوران کودکی‌اش:
روزی که رئال مادرید با من تماس گرفت و من را برای تست دعوت کرد. آن روز بهترین خاطره دوران کودکی‌ام بود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/102072" target="_blank">📅 17:01 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102071">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WJIvq5vXvYp2OzepgRCOnjoSmXBefsc-k0iuZ2EneUbSf3vYL4MhpvHoiYnlxDj2OagBMtvNWMyS3cEGoO93sFBpn2a7wpZWexLyLv6eWxg82mQl0xlFkFOiKh1fFFkHIo2log9wyYdJsycYKgh_D0vOTYO7V6Yphv4t2WnK_LEAKIPjuaV22jhNU_eiJJ6KuYYUGMMfWi86z4N3VV8fUzc9wcmX4HyuAwwQtVONd9VS8jyK7ARwX-XlI-fZfpuDpKI5P6nfeEjPqFuJPCoqVE0XOi-oTPdYInA_Br7jlp0XX505Go3s_bXhmf8pc8rVFx7b0NbKQoOMUVe_NeB0VQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
حضور دیومانده در تمرینات لایپزیش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/102071" target="_blank">📅 16:26 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102070">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d3120e668b.mp4?token=P27mNDQk1-8Thk0rLTlT-90hG7hAahB6Spm85n1DE3WSAPZe6hzMLu1bgH_u70nFILpJBNB_ECZNiCDiPmAxBWn6VxxrEOQ1afItLYoM2-ZoMDZvkYR6IIq7UnOY6hyl72Te2LoTBKnXlr_9YMRKT-IOvHccQXfWTzlTUmX7Edm5xLsDJ-0nWwgKOY4FbArtNodUrRo95DVf284p_TSIbWxR0aX7ZqldIQYHf__EbG6YWTprgtI9CxPEh4DmBgtniwbIt9pUbffa_C8gArf3tvu8YPO4hoRd2ubMOvQR-E8NdwMUzbnfVeM3KzFzi6R1pVY1jfExwObyst0HbPzSTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d3120e668b.mp4?token=P27mNDQk1-8Thk0rLTlT-90hG7hAahB6Spm85n1DE3WSAPZe6hzMLu1bgH_u70nFILpJBNB_ECZNiCDiPmAxBWn6VxxrEOQ1afItLYoM2-ZoMDZvkYR6IIq7UnOY6hyl72Te2LoTBKnXlr_9YMRKT-IOvHccQXfWTzlTUmX7Edm5xLsDJ-0nWwgKOY4FbArtNodUrRo95DVf284p_TSIbWxR0aX7ZqldIQYHf__EbG6YWTprgtI9CxPEh4DmBgtniwbIt9pUbffa_C8gArf3tvu8YPO4hoRd2ubMOvQR-E8NdwMUzbnfVeM3KzFzi6R1pVY1jfExwObyst0HbPzSTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
عاشقانه‌های رونالدو و زیدش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/Futball180TV/102070" target="_blank">📅 16:01 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102067">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OlWk0iuqsfNFsgWzMFJU9HZAQ2rggnc-BHgol6wrXFpI08Y5Lt4XuZyTJMhbnsCVfoH_TqAiUHjXVir41VEStkIeeSEhxkzPIMSuUGvYHXKccETgCkRZsqwRo1Kjw-vNtkvHxaRtp88tB3nKatz1rLwaqsGJU8lLJ8CjxnDhjSKQtqW2T0ECpbn8aQ-lKWmsw4ZSj6ROqWwIIjdiefhGtgsZbthy8NOFEB3OFGJ9vkrrUoa_rAcF89O2_Ki-3oM7votNn-Y8ODIx3O938JARQUDWBpbfTLmlYcWBi6QqgExrtArprIAlcd8BOsYV7CGjZKMYGU2Xwaey3FWolUzCXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QP4AhNU4KyzZoGmncVi1Oz6huYS4j_Ge_hM9q-51ZQO896MbC7u_b6cLMee7UhHfR2g-WB3cq6-EdYLhOHIOLSHv1aWVMOo5IAbnjVBt7mcQq2PKVMAO60zMr02luWfLeZSitS1iK1PpJIdhFUBqn7hoxfSPoNpZMlz6wPdqjy5PYe41IashPO6N_9u2Yz1SHRAa0KCWjFG5_lwVrH0t_SfqBWfCI_WxJCfhl6XpC683v8F36orJSqnW3Mh0d1d1xfZtSU87C0skLG6zz5YjeRgnjnin91qeX-Ssu89guYgSoHzdsDHFRyxxSfEXLTKm8158uuP8VwSUwWtbZAXhgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cXBUkFDKlrS1FhaDNmsw-uyDok7wlHG51YB6G7cV11TBXycTOF4E-mI9TbSmk5_LxkLvAidAjAt_hjYZXC5MIvuE2oEW21IgoqQE2WS77EWxDJ_eQzF3EbQkUl8UygvHBS3Xy_zClQQwIVSDHpo7idD-AtHx4E0n8Djz8D5koALN6o2SpDG9QUd7cJWvFoMAsMFr95Q0XrQvchXT8pjQF2vNObhqGPedZ2_GpzeKIuZGUiOEYKuMMgkyU8fN61Zm9P4V4gcDCEdsjx7U92MrdVEWgCWnOuSJQi_41jBxga3QnwrT_7E1RpEI-UPJzt3EutCwj9cgG3u8uuIFPk2c2A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ایشون که تو تصویر میبینید مارتینا گونزالس دفاع 18 ساله بارسلونا هستن؛ حالا هی برید پیگیر یامال و رافینیا باشید درحالیکه اصل داستان جای دیگست..
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/Futball180TV/102067" target="_blank">📅 15:20 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102066">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🚨
‼️
انتقاد شدید امیرحسین صادقی از مجری خانم شبکه دو سیما بابت انتقاد از قلعه‌نویی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/Futball180TV/102066" target="_blank">📅 15:04 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102065">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f32263398.mp4?token=VF7Iwjl6swVyriHsBWX2rMOvxqpgXVc7VhB2eRRMlv1_8Q2vvPkjYXfC9N2KYUN_8OlsbjGejztgYfDAajFM-lxPZ-EBLAKE7Kw_mqmrdDG8_svyGFCXbgtElYQGO7ETHJ4Q6_hhiKMvK12qoKxeH8UUpL4wsQOw7CjwFUHvQJWJUYXuxDwgdqqpI2WUbTKiFAn2VOikFm-TysmUB8DMoYzqTUF9TIQJNRcPA9NwfTMxSOX_MtFc8jOV-DsdGm594wq8EqSTWxncBtNSkPyv7lEZgPa8vsNyobVzhRmN4PHU_Gx4T-EWQftq3PTTfw42-wP_9iACmdF7522u3-EfAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f32263398.mp4?token=VF7Iwjl6swVyriHsBWX2rMOvxqpgXVc7VhB2eRRMlv1_8Q2vvPkjYXfC9N2KYUN_8OlsbjGejztgYfDAajFM-lxPZ-EBLAKE7Kw_mqmrdDG8_svyGFCXbgtElYQGO7ETHJ4Q6_hhiKMvK12qoKxeH8UUpL4wsQOw7CjwFUHvQJWJUYXuxDwgdqqpI2WUbTKiFAn2VOikFm-TysmUB8DMoYzqTUF9TIQJNRcPA9NwfTMxSOX_MtFc8jOV-DsdGm594wq8EqSTWxncBtNSkPyv7lEZgPa8vsNyobVzhRmN4PHU_Gx4T-EWQftq3PTTfw42-wP_9iACmdF7522u3-EfAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">غزاله اکرمی بازیگر: رضا عنایتی کراش دوران نوجوانی‌ام بود
🤣
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/Futball180TV/102065" target="_blank">📅 14:50 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102064">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f2-KYSQ8GRHDUFdgEEzQpMtU2lc2S8-iwShlBpBlwqWZ1BogU77DCa8UoN_F-19LGK5o4KoF1t0smNfsUs37zOFs0n8SNM9AqWoEgsLB8eE6COc1_7bgO5JUxGj4mIfk1kwNpv08zMXxvziDw-17Pn8UwQRcC9T1WJjyLV3rVksWtUViyLDnEYvhnRUj0lrKacC99aTX0ISL5H-Gg1gudUa6yPnoqFgGD_OlTDvbI4UzjKrsD_xLA8j3YoioPM1ZGmiUSdhTKWtsEcHiWQ2tYpTkBzCNGRt8Bp_lisHIAqo6l8M5jZFR_VGRGI9nQW8XDvlTs1F0EznhbdW9a3kj5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚪️
فوری از رودرا (ESPN): رئال مادرید نسبت به احتمال جذب رودری خوش‌بین‌تر شده است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/Futball180TV/102064" target="_blank">📅 14:47 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102063">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BZVP0HlPHxVbV_hF-8gnFpqvWIU9MBaSPBXYHCfDSl5tf-yWqY5ttQGRujFsOrHcOqExserS51jZWISP_ZL6gp0G0JDoHpIBDTU1eyj-I6XJv0GmYVnsaYKR4e1y7b8JkmLEiojda9PV4_ErjwSVYPuFCjzdqBk048sKwpe6B31io3kLBXLqM50M01UMws8UTlsIqlV3Bg1iLUQlJ9wUYq7IAwhjEUlGc1JBwCYfogS05edWJDjFn2zo1GaFg_CH_43DO-r9EIOSGj-AnQtioHaNJccGlPUebwa1il8V-vI9s_TLRKHA6jUoQ4HB6iPcBxs8M_beRZk44Klrslutnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
اسم کوکوریا تو لیست رئال  برای لالیگا ثبت شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/102063" target="_blank">📅 14:45 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102062">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FP7xpDPmS2Ozjh8xodaHjIl0bVeLPWz867zlRaVH40mXaj20lfpm094R1s_NHzzwg0laR5FkC6keAsjm3bYXKt6WVaSzfxKX9ehkERBChpDO5G8n96WL4NNsPfO3D-W4BXExIcOxMHXE3Ot_brK8-kRYdt6l6-3kRBlDeTC9tLbLiXqYDktpJQhrkJzaJ0YaCFEgQipDlj4U1eX4Pb4gvnTCDflFtDZggCBtsYGvdWUkHqQ11FJ6_u0kN8qUjKY6ggu8nOBVXcwHATSjH2Z13jTt6Q8TH2Gu2ppZcqEhKVg20ef5er1qYctsdGtR2QR-rU_kcNYFPsubiOzhmsFgPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
👀
مقایسه عملکرد نیمار و امباپه و هری‌کین در بازی‌های ملی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/Futball180TV/102062" target="_blank">📅 14:03 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102061">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2084d796e5.mp4?token=nQwCyJgdDyDTUnH5Aoe4ZUsUDcR8U59viZSRu1lUzuy75ZlY-E7u5FhP3iO8V-tJHBP8tZFaMFezRoFZ4eZHtuMPHNkpCwlm9q_TlS8q41QjXAclBvKD5w4oRnAcQquL28b7djQzUaSsqn1htnlOryxUaxsrwaUtAqKjNHLGp6d8v6Y4agRa9eapXD6_kN1Cc1IA_sxE0Ae333jMRadAPV94v2VYYYZH5eK_wfiC1e3rxcti8N2LqR2svkLjYEAQYnaRnwFfRlPabr_bccUkkEut7gNkHEh0RCq7_HMtNOcAdz329O6r4mD8XMydr4b_yYYRFzycZfzLk68OVW1euHFjtAZBJPZ20lDCo3VyJDvM-RA_Pg0jODRjX2AWj8bjxgr5OlNZiJkEQjKho5O5eZ8l5JRRhDVWtUq94Yvy1e79IN3KaZ2MneHpo1o2wdNYH8mxOtDGNojA65lNOqq-MMZyQvGSER3OX1NdQs6BUpNK_snPujViHQv9KBr-Pz2r4RKGOsCPE-N8Gfd2ZqF1utZtQXmw6-9wvuVqRWXEEd7fN8HWR4RDA0ubE5YxpgRVm1VGITvXWXylwp2Y7rhO2-19Zla_52tHFRoeev9LSD5zOLjUafxlnYrruE56Y45gOrFJgFOtiYtCeFfhKaEbiYObtIj8-VU1AXousoz1B9U" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2084d796e5.mp4?token=nQwCyJgdDyDTUnH5Aoe4ZUsUDcR8U59viZSRu1lUzuy75ZlY-E7u5FhP3iO8V-tJHBP8tZFaMFezRoFZ4eZHtuMPHNkpCwlm9q_TlS8q41QjXAclBvKD5w4oRnAcQquL28b7djQzUaSsqn1htnlOryxUaxsrwaUtAqKjNHLGp6d8v6Y4agRa9eapXD6_kN1Cc1IA_sxE0Ae333jMRadAPV94v2VYYYZH5eK_wfiC1e3rxcti8N2LqR2svkLjYEAQYnaRnwFfRlPabr_bccUkkEut7gNkHEh0RCq7_HMtNOcAdz329O6r4mD8XMydr4b_yYYRFzycZfzLk68OVW1euHFjtAZBJPZ20lDCo3VyJDvM-RA_Pg0jODRjX2AWj8bjxgr5OlNZiJkEQjKho5O5eZ8l5JRRhDVWtUq94Yvy1e79IN3KaZ2MneHpo1o2wdNYH8mxOtDGNojA65lNOqq-MMZyQvGSER3OX1NdQs6BUpNK_snPujViHQv9KBr-Pz2r4RKGOsCPE-N8Gfd2ZqF1utZtQXmw6-9wvuVqRWXEEd7fN8HWR4RDA0ubE5YxpgRVm1VGITvXWXylwp2Y7rhO2-19Zla_52tHFRoeev9LSD5zOLjUafxlnYrruE56Y45gOrFJgFOtiYtCeFfhKaEbiYObtIj8-VU1AXousoz1B9U" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
درخشش‌های فصل‌گذشته لامین‌یامال در بارسا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/102061" target="_blank">📅 14:03 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102060">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g5PYPFL0MAbXlBpPRD53_HO5lNkCIUNtMWbOboB14ir7XOjzngAqwwfqrGOReOAyTlo2QwR94rnJ6W0K4QAFUESRN3M6oVKOMUXj7I1rJHvZ3zhV7b4Dz34mJyqx24Ka-4k0nK8llGqWzbbGLraQnv5xzrIhKMVsGZagd30UoJ9Wko3hg72HrM78kzDsn1ncbMW1NxZH4iMU81mcmZAWFqpZ0PjdMRdhFKm_aD4a5ZINvWgrzhNDAtGWolLDh2rc7U9gHVL_vzTEn2sMDcpxz0Heso3gYSPA7p6qZqzlx28uR6ziW4kyNP9wOo1LyaeLu0pwGbhu54839qgjH323Qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚽
لیست بارسلونا برای سفر به انگلیس برای پیش فصل با حضور ترشتگن و دیونگ.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/102060" target="_blank">📅 13:38 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102058">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/p7X5qUcWFXlMH9Z6y_ysL7mRMY__DGNpMsjmnAjjmTlRnDu7VdFXefcUydx6UUMLEUo6gcFE69e5bH7HTVxebdoWZgEhrV65A_8oC9UbFtum47CBvTkfU6wXJx4s4SZMz8Wi1YP8vABLLpYX9aCgK4D7u-6vkd0jLeLIM2m77IN7OSvyaVjQ4nHGARIokDecr7ICh5Y2BwW80CVamBSqzUj56kCi3AfcZfW-tl44Av2GSVJ8WoQEIwhz7TUGxhyriaol2U559bP0_YEZJqX387kRKG8oQ_R0RgnoVcrkv0cGLRNOhHrpszhMGQM6gL0KPaD7NYOidICLOpYebEmvxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bobCB9FMNtrPyyrn4s48RDf0OkvjeIFVGUFpDgRbrvcK8EHI4mfF2LaKACBnyDS79WeYYbq_GRMM5YRPO_UVtfGTL1W02XNppQC9VyL0fmsEMt7nKdthGuZK-sjt0DlW91nwQUs08IXSuzgstpum3XV60XOBBanqa9xgDYDzzniei23dpPpRIfpK_J3ODbkbijRiXOXYUyD5Bq3S5oUXlDPkHLtgW_300UZURDZYvFzi3BsDU8Yzx5snBdbRtqNpXsu7pUpIpLWCC73fydubFlC_ASo-2BCFzNzsTjI_DxG3_XdBMXgmovZfpwzdx0wC2-5OLqSV9Bs0M5nm-53SSw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎙
نیمار:
وقتی در پاری‌سن‌ژرمن بودیم، از مسی خواستم پنالتی‌ها را بزند، اما او گفت: "نه، من برای این کار اینجا نیستم. یا خودت بزن یا بده به امباپه." او حتی برای هیچ‌چیز هم بحث و جدل نمی‌کند. آدمی فوق‌العاده آرام و صلح‌طلب است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/Futball180TV/102058" target="_blank">📅 13:17 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102057">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/772e430691.mp4?token=t02w8t54kEvec6lkUAYgBc8HmrvHWKeHSTEr1qpskd3frcCR4uDtJPK1yTkXWgwOZkivVFCUs2dk80sVXFXZB-m_G2yIZIfu3W9E4gPkm7MRNoEp5-k1YCOBBZVU-rr-ZOl0PB-d8JO_eASsd35gd3L_sLCJIWoQbzosu3a9zVOXzsHPjmlPKTtUepo16YEg7JMC6oJ48BI7S4fxwI-rxUUvygnDUKidScfeQHciiMfpoaj8TrVaFxTKTv8o-aXR8ZLTq8K9rCW-1afRfYzqxaezQM8Wj5TMPqCrOoc58SuF4qJ5726hdApNJibUeQ50UnD8JGDTdLiHDp4d1vMqrg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/772e430691.mp4?token=t02w8t54kEvec6lkUAYgBc8HmrvHWKeHSTEr1qpskd3frcCR4uDtJPK1yTkXWgwOZkivVFCUs2dk80sVXFXZB-m_G2yIZIfu3W9E4gPkm7MRNoEp5-k1YCOBBZVU-rr-ZOl0PB-d8JO_eASsd35gd3L_sLCJIWoQbzosu3a9zVOXzsHPjmlPKTtUepo16YEg7JMC6oJ48BI7S4fxwI-rxUUvygnDUKidScfeQHciiMfpoaj8TrVaFxTKTv8o-aXR8ZLTq8K9rCW-1afRfYzqxaezQM8Wj5TMPqCrOoc58SuF4qJ5726hdApNJibUeQ50UnD8JGDTdLiHDp4d1vMqrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این جامی که داری میرینی توش آرزوی خیلیاس پسر جان نکن
🌟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/Futball180TV/102057" target="_blank">📅 12:52 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102056">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/urGjWmEa80Z11yKLllz024Z1d_cZX2oLVVwDJel0rkD2QOZuEnlGBnBumaEVu18BsuPTSjJoPiXY2uPpD_snUF9UkNiCRliA5ytU7TDezbe8X_BsVwWI1gkczWhLjBCpdnR0jk5mkhVh2kKu1aaUF4TAeOY-0YHR06fLdZj3PkHBeigw-v5zymlHbHKqDjRJTiV7IzwyhgAkFFMUlNVU3R8tIyOD6mgzIA2-zwbu9CHiT1DHIy1JqwKv1akmGAKX6V1mqTzcdCoDF_KewJO_3RYDYrKKbkvWda-rmb4qTHas_0eb-Uc4qbWcAIU6qZJP9t8jD12dqBSnvCWMiFCLXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
🇦🇷
بنر هوادارای بوکاجونیورز برای تیم ملی آرژانتین:
ممنون بابت تمام این شادی‌ ها
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/102056" target="_blank">📅 12:43 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102055">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🚨
🚨
فابریزیو رومانو:
🇮🇹
✅
پائولو مالدینی، به عنوان مدیر فنی جدید تیم ملی ایتالیا انتخاب شد.  HEREEE WEEE GO
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/Futball180TV/102055" target="_blank">📅 12:38 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102054">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WJSLLPqjHFUv7xl0u7sd_v7xn371o0Rz3hktpSevvjy4TZVyPqeOgWUheUkFRUm0k9Mr_UJQNEOO5nHPb7n3NK-6ZOJvOXVcXUzhdtnvih-W9Ie_FtVTRSvqQDi1Qv5s8bo0kFYthIdRxEQ1V3hphHRyynIV5juLb-eWvs9WETjJCE_h4MNfawiiUQ8UquK_TqTkxO9EB_9YTV9cIwTkeLPjUOwXAL846gnfxdQ1RbxifCjxScsGEFdwvOzI3Btz7-2IeIO5_RLqmq4P16rMXMJzPtUmrPy0BMxt6cQ0hamp0ZBijvLJOy54KgjK-GJwECmqm3TMsoYY5ZBjGa_FSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
الهلال به کریم بنزما پیشنهاد داده بود که به هر باشگاهی در لیگ عربستان که میخواهد برود. اما بنزما این پیشنهاد را رد کرد. این مهاجم کاملا روشن کرده که هیچ قصدی برای ترک باشگاه ندارد و این خود الهلال است که می‌خواهد او را کنار بگذارد. در واکنش به این شرایط، بنزما خواستار نامه فسخ قراردادش و همچنین پرداخت کامل ۱۰۰٪ حقوق باقی‌مانده‌اش طبق قرارداد شده است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/Futball180TV/102054" target="_blank">📅 12:00 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102053">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tUfDioJfx95CBe9iSvjK5J9HUlHO87gvQA4J_WdmPMNSBEcd8p6agDNfs7vE5kVIH07WX-SOnv8XgmmGGBTSa8g4BrzOcGDvilW0rcrC590dMeDrEA0j5Lauq_qNKDc8SbBoQiq1BkLITt2FSaDbnRVTPnVKQYg-b6aoSP0tPEzRFRexHUG3mhz3odBdKvfVBt8HTvh11bt_IZFv71fWEJXRqYbK2RtePotoA5r67GfDa6P-tw8xGNa56HVu5-E_spz4LiXgqhFXIS-uYw0OQI0Q4CPg2meoWETrdcz7OSsveT308YU9Jeu74OgE6E3s1tb8u4jwNRfpj8Xeuh08Zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
جورجینا رودریگز درباره اولین دیدارش با کریستیانو رونالدو:
قد بلندش، بدنش و زیبایی‌اش توجه من را جلب کرد. جلوی او می‌لرزیدم، اما یک جرقه بین ما شکل گرفت.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/Futball180TV/102053" target="_blank">📅 11:40 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102052">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MbAvEjg16i28l3cFOmWsQDbloWwRG0IdzhaPUjMPaMmTMDxsY3xCCkBI0fsKrqjRMQCK6myuhpm3cff1yNN-7Y3dCUiu_Ipmm6ZBET7iNlCWYylIUYaco9bM6iFHXIc8wjX-H0Z1HCYb_zCAfu8VYN7wljkPEQmnWYKf9oWex8AgPw0yZO-e4vh-D9BQNRQJ8FV0mhzsUuL9eGispTrY_DieAXC5dTiuCQ4psQb0C50ayUaWmqdJ0V2UpQvrvfrvtu1HbOlEEDm3MC_UQLt_2CSvRg-Sl7Vs1GHE92nnlrzLkEwi-zzzzQJkfH0O8sJaF_vhqZLuwRiqOTB1PJZY6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برناردو سیلوا و ژائو نوس به همراه زیدیاشون تو مراسم عروسی گونزالو راموس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/Futball180TV/102052" target="_blank">📅 11:20 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102051">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/809e9f523f.mp4?token=BEMER8csKPmKShzFKfe-JG7dtJmv-o1CT_JT7us_nUdhdR4PIbT-q3ZcMHKloPUAzIqyu7bzSmc-ketRLji9usjPua_Nk-2k_1R20rZKC2r2iDQKzDGRbSr7KOJ6iVfwmfHKErwi4fECRJRjP3ICBIyHzPLyjSABTVmci20LRfFoZKMlTLhHqzsnY2eX2EILNsBPZUZYJyC2cQUBFdDh0_Hp-axVv95jjlBHxEaTVVzxxs44Iqj3uepNT8BUOVve0nslgLAKdJv9QXgTnPQLWdekRjA8oZ7KaaQQBVrI-kWrplt5Sva_xP6lHIG45GV06zhc84CgM0UUjgDt-GGGig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/809e9f523f.mp4?token=BEMER8csKPmKShzFKfe-JG7dtJmv-o1CT_JT7us_nUdhdR4PIbT-q3ZcMHKloPUAzIqyu7bzSmc-ketRLji9usjPua_Nk-2k_1R20rZKC2r2iDQKzDGRbSr7KOJ6iVfwmfHKErwi4fECRJRjP3ICBIyHzPLyjSABTVmci20LRfFoZKMlTLhHqzsnY2eX2EILNsBPZUZYJyC2cQUBFdDh0_Hp-axVv95jjlBHxEaTVVzxxs44Iqj3uepNT8BUOVve0nslgLAKdJv9QXgTnPQLWdekRjA8oZ7KaaQQBVrI-kWrplt5Sva_xP6lHIG45GV06zhc84CgM0UUjgDt-GGGig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📆
🇧🇷
۱۵ سال از روزی که نیمار این گلو زد و پوشکاش گرفت گذشت:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/Futball180TV/102051" target="_blank">📅 11:00 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102050">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ijqk6_iwSgHRED4I6FK_deSLCJKMhVpBX4jL3k899LiEnB-YS6ztzxC1cmtfVkDaNPDzx2v8RPd5zMHdqT7S66uWzSxqdcx-eU0DSVKXD1Fyl3XB6VoJqaZQZp5xY5tft2WJSM9FoaZBZsQhkZ00NtcGTOtMMoUAv_nvjcrLZNQL711YuQsbUi7CNOdmPtqJ9PmeoTGrTCRmyBhPb0_dFZvlU4ggxQsEaJCL7vNT7_uMtIunYy8MRB_HlGf4JnMeyp7IFTmqVs2BzOZe4l-DqIK6bA_9O0ev3dS8D3whAhIidG9wbs7k3a-JHw36ojfp_UlKFJjUXdGWE-epU0AvwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
فابریزیو رومانو:
منچسترسیتی مذاکراتشو با باشگاه لیل برای جذب ایوب بوعدی ادامه میده. مذاکرات با باشگاه و بازیکن همچنان ادامه داره و تصمیم‌گیری در مورد انتقال او، یا در حال حاضر یا در تابستان سال 2027 انجام میشه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/Futball180TV/102050" target="_blank">📅 10:50 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102048">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sDwy6gucHIXrcG-uK_fiioCI-2ZbaBlzCB2trC41xh-tpWBtAZUyFmkrJHGV32FLNYwOtJYPhV2AByygKdHl2K0OE2Tlb0AdpvfQM__kHvlxWu7o_9cKZZHsxalcX7kN_cIjczDwk4_lS5YW4NytuZlQuBPY0w_ySXFBtVS7eeiLo8nV_seTQ4p6d7OTTSDc00utE3wQwchFoXZu24WvHEz9ntPG4UlM3z6YhNFMMnE8gUxz7ku4kRwBhsTRyD8qWNmTZdH87JMukIPNFWElA8Se4hSHziy1NFptf881M1-O0m8Z7Jm7cPzAOq63hMyQgMUozUgkHT_HjvPyDkBsLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lMu5NAuRxyz5k3403rtylY1_EmwVd7mT7g2NOgwMAlmiDwtXyU1wkl0IdxgpV12p8VkGN9cXe-oP6Y4kRfUu9sLZU9jHNgzQwpnCYHl1cNxLZzTpKhifeL9VyYrarcFY1FPIRrcFspGH0tQ9w5lQ-cbk7dGrRmXm9h2XJ5wQKcuHZ0vkf0Oa5BCp7S84wg5LJYp1xpH5GxoqTQR9wPMfDdgc98J-geu2ipJ00dTVSm9sGkRTolDqi7jT_YrGRCehDQAjPzVKF3hXT7-dTF5wWWuPAF98sTboqsmhSMSoyvusjtj31Q1zZ-QEeCZrGadW_ZlOdU7lEgrurmF6dWvjAg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">جورجینا و پسرخونده‌ش که حسابی باهم گلف بازی میکنن.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/Futball180TV/102048" target="_blank">📅 10:40 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102047">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZRqZu747wHxONCXDhRag0bGMgaAoh7c0NAODAckQXucRnSEPXiLF9Ay8pqkcpxCGwqQ_6Os5RSuiGI89VLhABZhizrVFu9L6xS4MF3bzfP3buKmk3gkAZNOI4kuAy1HrejfLN7E1SmC4KoE_PuqrPYhS0QDKJZwLchMi3-NJSA9xnZKmu58rw2nhCoXjr9KbIu60g-k2syLjfghpFFfr6DynAzPXcvjhPAGQdM_Pz93FX6pJ-hHHyEZlHs3QpQMYBGIAUpcJm109eHv1AVXEP4e4y_bFURlMTKiLfGRMxA8P4Vj4QpG_qm8wpWeAp7OlAqlsdok6HMgYq0RqtDBNfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
الیور کان در مورد کلوپ و تیم ملی آلمان:
شخصا فکر نمیکنم کار در تیم ملی به آن سادگی که خیلی‌ها تصور می‌کنند باشد. من معتقدم مشکلات خیلی عمیق‌تر هستند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/Futball180TV/102047" target="_blank">📅 10:20 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102046">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TSGXjuMshZ1vS110YBZ3BbPaPESIbd4t5JxlYzj6OoFerO7Go5vr1AziZQ48QWHICpym0x1SHuXMibtCBchABokW2oKjgxej56An39dNosnf3sstVEMCwe4yGQi2uuTODRtrRONvW6drvJrxe3N-N_DmyC2X1_ZO53S3NFXulaWJzTMpal3ErIyhTCLnyBHO7K0A1kOj4kZDWjZ7BLtKONPCCy0QdrYV5bwGY7-bgGVoJ3eHSvdZwhpXqbDDhT9taRTqqhCikEascj88UJghNvoarQDS0qGtV3dgiMa9c-8DDaX3_i9ajUwwlX470Oa9CjVn4Tm-WQ_sVWgHL1cHxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
🔴
وینیسیوس جونیور فصل گذشته ۱۴ گل و پاس گل بیشتر از هر مهاجم آرسنال ثبت کرد. او می‌تواند خط حمله قهرمان پریمیرلیگ را فورا یک سطح بالاتر ببرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/Futball180TV/102046" target="_blank">📅 10:00 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102045">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mO7mSxkSN7szteP5eK_1R5j_hXnGbPuqDWuQcfkvrPnUGPLtsK4lMv3gQOka7vEoEuecOwHuGSaMrM32V6IzPqhhE3ovTGY0ARoJx3qtWW38ygV1yccU21eAUKT8TjBUsM-iTks9bgOO1HGw8lTvDiqzgJhVEzSyWa0I1Vk-2CMiqvMZn7_k8mhMNhMo97TVwXz0CuPz7p9ML_8Cdu0VXw8BpH_PLxV2u7Xbdxj9ELWZ5XDicqxXBZ5b9y01yHOwQtpsUuICpB1IU4kLTrj7dsMQpCMn7CVgjrvEnyJlZWE2QOgeQys58UwhSBzzNekxa6Q6wE8jOUVDayVsYwQ7pA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
فابریزیو رومانو: پاریسن ژرمن تلاش میکنه بین رودری و رئال مادرید مشکل به وجود بیاره
‼️
🔺
🔻
پاریس از هایجک شدن دیومانده بسیار عصبانیه برا همین با رودری تماس گرفته تا اوضاع رو برای رئال مادرید سخت تر کنه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/Futball180TV/102045" target="_blank">📅 09:43 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102043">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sAxBF-MEcQrn-5S9c2BMneu8_Dx-oLy3SUX65goJrLp_iO41U3pRtaxUo2URbS0Szm2K-uw2jFqB9CLM0lWroLTfJ3kOlcmOhi5ggEmVheo_OEZ48vQjP0E1dBWYQwn4lpmF94dPL_eYEg9HovxelMrWunKR8mBogPmbBCsO3YvskSJlRKvaB06rmBzLl2d8oLdQJJfvL8vVyezZIplBI0pLZXKuIoWe3qEzoiFAc1ephaowoP29IB4iXGDJtleL8IyecaptqsqwI4CprDr-3aVQY3wnlqkcaTcjQGzDpOqjboGLGB2obJ5AO0eIt2j2O7E4ZL3LvaORsPv14ZbTgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tNG9NZiWDqVOjxWeeYr49xdCQgnKfsBKzWIPtTaEtwpnoEprAN-mTTniXRLNYAesRLk7dCU5zPSU9NdzFoxEytX1T4x_8uxOfwH9dtcpAlnc8uYQko59sHoqtq46gMZO-1_UT4nXmNPQYk40WLhUrZP6F_OFylnMIar5OHd1ss_2jd83NFI-kluEBat7mVYd-89XXDU1a2kAePR58sMpoeB-HNhXheWmxTIGFFwedZveFbz0vog6Lua-j1q7t8w6B-_YEbE-4R0bwZhdBBA-O99ubfUxJXKLJXI-2UcphP8tqFPjOpIvWEI7qVlpVWqpjAmY6rHoWkgKDyRYn6Lo2w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
👀
طبق گزارش رسانه‌های برزیلی؛ نیمار بدون اجازه، کمپ تمرینی سانتوس را ترک کرد و بعد از برگشت هم در تمرینات تیم شرکت نکرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/Futball180TV/102043" target="_blank">📅 09:31 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102042">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/upYwmERni-nnsDz-cJF75i15d4cQfc4JyB7pKXNqYgdFvDDp-WkNQLOiDzeZq6ku7FWOZ3cH1hIQjhVQBtzI3iKx7Assy0PYBOv6pG8Z01_Tuf5XJjIy22rFnOXJFSWUJRhFQXAAmJKwp4U2RHXTv2BQBrqanjOcLbYHL-xo_eaPYculFZGjfKosOMVq_NNxZA0WS_STyfzm_25n-0r5ULV9vQqjy6GuH26gV2_2QSoA_7HLNAvXlcvdDcdqV4tN1mU21axp-mMg4sdveK55XiHjEc8ZwRytJI64-YCwSndGL9tH35L36qcOQQe6uuZjt3h2lWxEMDEgwKEBp6N6KQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
نیکولا شیرا:
رئال مادرید آماده ارائه اولین پیشنهاد به منچسترسیتی برای جذب رودری است.  ارزش اولیه پیشنهاد بین ۵۰ تا ۶۰ میلیون یورو.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/Futball180TV/102042" target="_blank">📅 09:11 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102041">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HFBoG05dsrW8HAbFD6AYgms19S1fd35FVLIZE5FgEWJei19K2WMhvme8TS4R_hs8wAOA__IhbE1ypqSkIjCiwgjZ5XtPgoXxToxOnnG8zPghdior-IVPDq1a0DHIz0kofH1TBFqm0W_OZ-CSs5Te8Obk-AY1o6TjSVbG2Y7xvDDeFjWlNS0SyGUnTQ-USGFHxP6mTipOKbWaucBrVLAj7IxulTvGrRiIxJZgTGuOY8TQIbWF5Mg7mtJu75rscnMpx7Vb9vYyD9mt2uASeutjZlbquubOoqq9sTOntpSEqLYB8t9etvHWVXSsZdryn1rNhe5PITawKkcQWmp-4z07Zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
⚠️
اوه‌اوه یکی جلو فلوریان پلتنبرگ رو بگیره که ریده به سر تا پای رومانو:  حالا که ما را "دروغگو" نامیدید، شما خط قرمز را رد کردید. شما فقط یک روز پس از آن، انتقال رسمی لوزانو به آینتراخت فرانکفورت را اعلام کردید، و با این فرض که هواداران شما احمق هستند،…</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/Futball180TV/102041" target="_blank">📅 04:53 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102040">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oN0p1tz9Hyu3IxCJgjnHvP-QB2u5T4gE6GEBzzelx6SByMEijuX-pe85tjZlaSjNbshu4VRtSNXQyZNNuH1nMN4D36iKwmBIUkn0gVINJN0as7WbJDpcEO_DjigAGzoz5UF-yeeWq_GOtDIEin3LoUBMpCKZVM2qemJluFCMtCBqwwaMwz8F5xE-u0igJqOACd9MLUHtaF63mNRCW7Ye4jbQdlzDaR7jAR-2jvsuLD2FUhRCckHjEij-t_yWy8gqbUoFXAdCp3pSfYfkXQDizyDRUBiMjuy4gCc7efCe-aJld_k89e-HFNRap_oHf5EnMSJorfmGzAkqiW-0pmYSHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
❌
🇮🇹
#فوووووری؛ حضور پیرلو به عنوان سرمربی تیم‌ملی ایتالیا بدلیل فعالیت‌های شرط‌بندی وی منتفی شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/Futball180TV/102040" target="_blank">📅 02:10 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102039">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I2__hN3wfyRst2fwLmtnn0eNNTtISLky5-iMOrnV9G2a31Sz0jeM6Y8JryK2ChhcW--LgPDFvbuexa2kMDK13bTSvKWmSpfDvliatc3GldYCyvuWov9TDcLIMAre4aQWgG8YioxrDsOm0zo7trKvZBn-zRe237olaoTEZVSSPOFd0QFEh3-xEhU60SP9Y9ivdAuOZLTHZbYtFJF1v4NyXTQR-0nNmhExyNOluL1hgkp8x89SYuEq8217oDXySIORA9s-bSF56VjwOgeYPuGxB1rG0TuUnTOm3QFdxu1EV8_rC3v59_X4TEWwp9rEGfiGQb4HgOHwi4ckTbeH13XlRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
❌
🇮🇹
#فوووووری
؛ حضور پیرلو به عنوان سرمربی تیم‌ملی ایتالیا بدلیل فعالیت‌های شرط‌بندی وی منتفی شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/Futball180TV/102039" target="_blank">📅 02:03 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102038">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ulbkCSbJC6Ot_J9hRBOUVz8h1-Z5IklQ-rvKYsNcuiUTGKCAffWqFRjxyjiT5sS3qf5XDUD8W9vW6ejzOAsRkqKYNaa9EEvbmXewbaAO9UlZ3yPTRUHGzDXm704EXbGZNr3GDJ8GFUvspTBCM-6dmdd5RTZXO1p23zTlq8yZHczOcjxZCT0YQLN6zngLfuuboZuIs1tIIroAsdmTtbpeo7S728KwL3P2dnCDh2_Su_lQSB1ROHu0Wjb__3TqpWHk6RlTm_DknUTUyhdRTHHGfwTwaOlJwjDvd8RoZXhGYht02GOSybgUU5__cda_UKkiKEOZtgD0i72uVOEFwp2xcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇵🇹
ماستانتاتو بازیکن آرژانتینی رئال‌مادرید قراره به صورت قرضی راهی بنفیکا بشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/Futball180TV/102038" target="_blank">📅 02:02 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102037">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QcM17A8Pn-VgTjrs8z5-WS9aTeAx8of2tMHkzkXP2g0HAv8XdDPDP6PYAMa1x0ar3Oaor7_N0pLwPuaZbze0m51i6Hs61ApDMAEamptOCQlnlEvElLHXV2_S2Pg1X4TKF07ioZW1jpGPOCqYEwAHf2TBIft8DQicUXjgNka2BBu0TU4n114REUB0uDrfbCRWttHhqxxJRU-oU3cqt60Cqmey0z9c0q4uKuXsArjvRDkV7Y5xOkiwFieKLF6uzEWe0a6aQtDclMdt_HEAktIP07am9NXse9NHe1Q7_lddt8m39ZLZ5q_Mhas8zzxL2uD-Z8-DTX5THqWVFIaA504EGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🇪🇸
جنگ بین خبرنگاران مطرح فوتبال اروپا بالا گرفته به طوری که دیوید اورنشتین گفته پیشنهاد رئال‌مادرید هنوز مورد موافقت لایپزیگ قرار نگرفته و نیاز به زمان داره و به نوعی گفته رومانو فعلا زر مفت زده!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/Futball180TV/102037" target="_blank">📅 01:19 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102036">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/iqPzJmc1eiOf1j8wZ-qwNABOHmTAyVd3F618eMua6rFEjwOo2fCqgUwV2CsJLqR286HBalva-MAuUtrQ9fRMul0JjjSrzOBOdVlwRYZ7fPyXJXx3IwNBvq4vWLDqdAQYugjskvHJyBmg6PtNM9x28_7qzFI0KCbwNBez7TGgq7grzCmUqCujuhGZCBHKAV0PavfVWgK9guDs1FzsLNxf3PHfeUXn1YZkwrk5jXCKRCB6zCvMwB4ae-IEFoeYjAi1XBm1xgb8UqPDwGAM95BMGcBw4qfPOr7vA_7NZjRAVcg3atV0GAD89FuFGCYfMhJqJ7d6yRfUnRsV6qtJprioFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
سرخیو والنتین خبرنگار فوتبال اروپا: ژوزه مورینیو به کاماوینگا گفته که فرصت بازی زیادی در فصل‌آینده نداره و بهتره به فکر تیم دیگه‌ای باشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/Futball180TV/102036" target="_blank">📅 01:16 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102035">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YApX24Sj-pZL0-gIRT6lzm-lH8XrBRiJPMG67QSDuqOR1BVnT2mF4uYjJgRS-X1hjslNufx6V-xHiBkDRnrOcpI3PxI-6wyGS1_9MjdWdx8DiMQTcYElNmBxfqNoBTJjHmpg8qeTsZ_zoxbaynFOsGTAYbyv08XJ6lonC0YDdjsZf4TPHPj1_6rHsdwp7UPgv5vR1Uuq9FAKeBZyzQH9CfyhQu3_pik5pXmTdtbKBBTtecIIMe8DNj6sRCW4RXM-pmmsy1IM0eetvpdqEGVYZvLTTFcydtHgryKGX3b5UOwPLUBehuZFpgRC2YEYFEmFYwuollOEPvnIm_fVXECBhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
💣
💣
#فوریییییی از رومانو:
🇨🇮
⚪️
یان دیومانده از لایپزیگ به رئال مادرید پیوست. 𝑯𝑬𝑹𝑬 𝑾𝑬 𝑮𝑶!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/Futball180TV/102035" target="_blank">📅 01:05 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102034">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KVN1DzyOcSPhNos3y-Wco_XjVbdxd7ptINy3TOnLrt2XxIfveSAOBq3H6QPRBlNg_1zIN2CibUu9jDdLY4ixVt0vwLeNHxtAS2rwvVr-7IA_2rH8-frxI_URdSH9NYy-odYWgsxki9z2XdgDVxHR74hIfoJTH4uM7x4KqxnJwrF1phDZsC7mXGDOYiCvDoPkCHuDnJRjrt2fwFyPT7mFa4e_KI6ruUZbX7vFjmlkG47DLo02_0hfWFV-J9cPz4vEGusDLWBLxb7bmb4q7XY5V0pjLjOm5gIB9XgGeR8mNQewYa_0cUR5mw3R48hw4D-FJZASOCbiWS32uI4uk8wskw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
تلگراف:
مدیرای آرسنال معتقدن وینیسیوس جونیور همون بازیکنیه که میتونن باهاش چمپیونزلیگ بگیرن و هرچی واسش خرج کنن ارزش داره.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/Futball180TV/102034" target="_blank">📅 00:14 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102033">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6fda4a57b7.mp4?token=Yg108ab6fUwhJayZunmukimGS4jpaj1ZxFfBtOqgmgAt0DZigqHOe4GbYktFUDkzB2nEMkxpZvjjnY0hwoInjncC_vt5b200AYz3SDV0dc1t0aGOkpN-guoqkf3IXbAdYLgQQjVWJAZU5NnUVWlFZi5ydyGufsygG8Zb5b84DZOeVyG8Es8i1-nxmNejSzIEnVthAUocoZiQTIH-BhSk8xs4NGLurqlVtUhGiG0Ju0RVvBAezi4xSvzV7VaEd-6KEjKgSM5nsHXBYW6Cs180Me64J7pZFABgHMpwCq1mc4U_anT-M-TpUKas3ymjIHvK9r5hfymWGK3tcCTveQkCbQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6fda4a57b7.mp4?token=Yg108ab6fUwhJayZunmukimGS4jpaj1ZxFfBtOqgmgAt0DZigqHOe4GbYktFUDkzB2nEMkxpZvjjnY0hwoInjncC_vt5b200AYz3SDV0dc1t0aGOkpN-guoqkf3IXbAdYLgQQjVWJAZU5NnUVWlFZi5ydyGufsygG8Zb5b84DZOeVyG8Es8i1-nxmNejSzIEnVthAUocoZiQTIH-BhSk8xs4NGLurqlVtUhGiG0Ju0RVvBAezi4xSvzV7VaEd-6KEjKgSM5nsHXBYW6Cs180Me64J7pZFABgHMpwCq1mc4U_anT-M-TpUKas3ymjIHvK9r5hfymWGK3tcCTveQkCbQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😆
وضعیت این‌روزهای لیونل‌مسی در تعطیلات:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/Futball180TV/102033" target="_blank">📅 23:40 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102032">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ksdZj1ExvhHOYdWH5UyZB0C__M01920QnKZMM5dcuAcW_drvy-SQqdjdITmkHKBQ47CC-rFAxnQrH76HZ83BKJ9sLlfq9Q-Rsh_X_I-RaDJ1qU5IDOQ41muRWU94N-XAeGZaB-FBvxsRdztU4YBVmmsbBbFJPR8QftJks86nIoYzt-lUQzDlv02lM0KYKgtKPoxx_J0YY8wWiCbXsYf7pHaVhW69NTACeRCLjmEyCdpgYdZFillqH5Ck81NdFyCTGDRgfb6vlkqJYvvKrjVaVBoLqicy_MAYIV_vP7op66LOPb-5rjPUtDBZ22OVuOT42oeZ9EnM1V8nRWs5C90uBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📮
🇮🇹
دیس فلوریان پلتنبرگ به رومانو: بعضیا همیشه میخوان اول باشن.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/Futball180TV/102032" target="_blank">📅 23:36 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102031">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v4K44CFWY5_AHdTE3jrgu51i_Yf1d2JzvSPJEARbmfZBwx7JItxetFsu1lj-5zPUfabcyYfMst7SAQJ-ZwEPNbwmDBRumpw8tEDWpAkxuJHUbiTJus3dSAf6ZjDIPifH7kB1KacBjevA9NsAfSwLHS2GfuhT7ZF7vLD79m7mk5-J7kk0TtiT8ZGaAhjNT9F-tpo12JMu3pT0Eb0CFwaCnJk-48rl6YPatxF1TPu9odzObBCyEKW9LJwyFlGovO12qFg30VR9YpAo9Zapp3xfMsuPK5dQeOY-bx-TrUfIff0hzFNizH3SDLe7XH60CRLGoD2bgOD8MEJhDp3fg-Qbjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
😐
فلوریان پلتنبرگ اصرار داره که هنوز هیچ توافقی (حتی توافقی اولیه) بین لایپزیگ و رئال مادرید حاصل نشده
‼️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/Futball180TV/102031" target="_blank">📅 23:08 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102030">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🚨
🚨
💣
💣
#فوریییییی از رومانو:
🇨🇮
⚪️
یان دیومانده از لایپزیگ به رئال مادرید پیوست. 𝑯𝑬𝑹𝑬 𝑾𝑬 𝑮𝑶!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/Futball180TV/102030" target="_blank">📅 23:06 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102029">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e020f6fb8a.mp4?token=ndHT_gVmCQOmkuUiIBQ67y6jy4g2ZCrL6xyrVKvk4EZK7dsbvML7njMJVvJZdy8dAt4WJuFhfSYSdq1jYbtdNhP3g1nEjrvHQ1_0k-REU1hW_9J6mcjBNgHV9S6tmrnMoWTw8BT94Wl0-BXG5Utw0WjIdZ_bAgU4aOfBGxGBefznjryIDOgwbsLZ7RurfZOCbgws7ChrhVpkG-1gqmdb1s9qNmJ5sVXQtHJ-5Ilz5wJCt5eqR_Tu9e--9O4LgPrDNpMSa-RUmAhbZArsRUyJIugfmOD8-mKGHW_MfPgsMqI607edR6sHiQIz7cUBt5qd2kxyVWMeA4DjMIQ3AcHUxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e020f6fb8a.mp4?token=ndHT_gVmCQOmkuUiIBQ67y6jy4g2ZCrL6xyrVKvk4EZK7dsbvML7njMJVvJZdy8dAt4WJuFhfSYSdq1jYbtdNhP3g1nEjrvHQ1_0k-REU1hW_9J6mcjBNgHV9S6tmrnMoWTw8BT94Wl0-BXG5Utw0WjIdZ_bAgU4aOfBGxGBefznjryIDOgwbsLZ7RurfZOCbgws7ChrhVpkG-1gqmdb1s9qNmJ5sVXQtHJ-5Ilz5wJCt5eqR_Tu9e--9O4LgPrDNpMSa-RUmAhbZArsRUyJIugfmOD8-mKGHW_MfPgsMqI607edR6sHiQIz7cUBt5qd2kxyVWMeA4DjMIQ3AcHUxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسطوره فوتبال مملکت علی‌آقا دایی
❤️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/Futball180TV/102029" target="_blank">📅 23:03 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102028">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZSsD3_Ciit1F7qSBo9i9HK-WG1V46Kohx_0K8xaO_4beaqaaBXsSBoS8O1Zq9bqHQXJ3_j-vf7ctfMxgOTDFbaJFL72bMoSuYfTuLfXxjQtuTybH4TQdeitB7mUcfcB9vQToyKlUakDSOEiAOlkqBPyl0QP_Sd5L6z8-icmnQgcHvY0-r_XTBewS9jdJKVdVUpoHRKavqEpvkNPIbPwu4Io53XGriiaMu-rhF4VgBTks_IdnpcXTcDxbPY1nJx_hIX8tdtz39GzirOHtAaTm4iBpWmgOySIxc3df29m_ZNeGr0JxMp1THPI076rRswbYX7otOi-UWh14Iz0DFrrDCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
👀
رومانو:
🔺
خرید دیومانده بیش از 100 میلیون یورو برای رئال مادرید آب خورد.
🔺
مدت قراردادش هم تا سال 2031 هست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/Futball180TV/102028" target="_blank">📅 22:48 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102027">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H-jZHS_-FEF-W2V-Cc75octQ4wmKzAefcI9SyCXcES5E1zr0LnFDrhJEXZVg7dbmzCcdgCny5IjySlt9-lQlNYvTGERxYhmZ-Mm0OU_lZ5CZctHCTaA9JFekMsFZNLA5ntdRQHnNRZojzaxf7tdRFJKDpdO6Eb2RTp4Q68vc9SnuSaXR7pm1VeFLfVu6XR0Fj-9sDQwSVClN_m4WJp4FkPSaAwTrG7HL6L9Fd6SqO4pX-qhEXPGdyXp5CFJBRltf8p13D00nz9Yyi2LsNhAIM_5zw6O2_1P9C-rYjgIwcJyQfZZO9puAa0Z90yQ2rLbnxHmn3N_hbO-09jke8AzHdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شاهکار پرز:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/Futball180TV/102027" target="_blank">📅 22:35 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102026">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🚨
🚨
💣
💣
#فوریییییی از رومانو:
🇨🇮
⚪️
یان دیومانده از لایپزیگ به رئال مادرید پیوست. 𝑯𝑬𝑹𝑬 𝑾𝑬 𝑮𝑶!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/Futball180TV/102026" target="_blank">📅 22:33 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102025">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H6Jnjb_qE3DegNQiW2c5ZpQfglJcIXsYJ29SVnZ16Wgd484cSvcFfqC218x_Nv2ae8Fo0XTIGiDDiXOYU2tYII8-rmg2KJfTi3z5Oa_Ypj11ng6s4-IhM96XpYS1ekW_i70Z0tw4c9Y230__bv3j-FgGp3PjX4IHQeJvtQrFUW8ytmRMnIeYi0--3cTOWoxt01RtsSt5yLw4dvtefNDRehnMP3f-halRVmdzb1v91pPjC9RpuiRN6naHOJK_e3afR-j7Qf69TFYQy_ywxidhNAXrfC8avO38oJjregMPr2yhZ9g8RMGViRLn1x17sW8YQruKm6j8OrhkvAGXgTVsbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇪🇸
اسپورت: خولیان الوارز گفته میخواد یه قدم دیگه برای پیوستن به بارسا برداره و بزودی انجامش میده . نهایت تا ۱۰ روز اینده.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/Futball180TV/102025" target="_blank">📅 22:32 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102024">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rLsjO3TthUzQ2LLzCaiKPkoRfB1jWMK4kepWE2NEDfwgv70k3uCev4XwQwyc1u1UUlF2EBvjzYgsBsh9v-ad_HtDWiOrwTReOu5ZDIN6gRGUzzZtAyXl29m5AdOIBoA6RpW_tRSftQo4ZKOUjuiF-2dCeeJe-7DktmeG86hvKeedK7yVzmYrtXvjGZTN_NGYvQt2MCc_A0OR7U2Z0rk51AhtQGOdwmNs6BQz7DE7zcJHPUeRIXf9sYPdFBqHccLh3_8s9tA21-vm9gtvjX0xqg6InFhLT1DHiVQe6tUBj1hhj2SXV9mVe-_PGRHtjPGCJC-_1VBrajHUBPT-OwpkVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
💣
💣
#فوریییییی
از رومانو:
🇨🇮
⚪️
یان دیومانده از لایپزیگ به رئال مادرید پیوست.
𝑯𝑬𝑹𝑬 𝑾𝑬 𝑮𝑶!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/Futball180TV/102024" target="_blank">📅 22:29 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102023">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9274ecf947.mp4?token=QTn1rTz6Rt7hUlAeWFRXidMZKYnyeqc6dLyAjAvaH2zzXSQkmaNfZjOqZ3UXBYIUGuT7WC8a3vV7PJ2vB1vpa_9j06r7sjqFYzmRmife_iL9TqIw9p9dj1c_1EfJSkTCejyhSKD8IlohxX-nrFocC-bVx-Enoz3p7Ekh5wFm4l0VSZsqtydYEtjhYK4mvivfMivQAinSzyaq4t949rPIFNCAHUjpviNUcMrvSH8VGDlj9v_qrnlZZ6p27nErwkemoilxaVSB3Po8DgTart1KdJlj4dfJYREB223A33VKM4CD1aY16IimLaziwuSOLJJ04DB1EHod2gLNkyInbrJRI4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9274ecf947.mp4?token=QTn1rTz6Rt7hUlAeWFRXidMZKYnyeqc6dLyAjAvaH2zzXSQkmaNfZjOqZ3UXBYIUGuT7WC8a3vV7PJ2vB1vpa_9j06r7sjqFYzmRmife_iL9TqIw9p9dj1c_1EfJSkTCejyhSKD8IlohxX-nrFocC-bVx-Enoz3p7Ekh5wFm4l0VSZsqtydYEtjhYK4mvivfMivQAinSzyaq4t949rPIFNCAHUjpviNUcMrvSH8VGDlj9v_qrnlZZ6p27nErwkemoilxaVSB3Po8DgTart1KdJlj4dfJYREB223A33VKM4CD1aY16IimLaziwuSOLJJ04DB1EHod2gLNkyInbrJRI4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
آنخل دی‌ماریا: مسی نشون داد که یکی از بهترین‌های تاریخه و تا وقتی که خودش بخواد میتونه همچنان ادامه بده.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/Futball180TV/102023" target="_blank">📅 22:02 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102022">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mZZio0LnUkx_ywQoBMNf9KFMqBavbeQfXLuHCjsM6DXhRXjNG6Xz-rujNHbUsekp29imKHn-ItmdOMkV_zgoTH0wMhlkTzGS4CUE5bYPpPmcCQKDbn58DOhw1tjQkDYUYN_FMPEjz9_KekRIgjWTwT57K5xGt4XTnbWOOEbiKyaG6BX2OQv7zPvyDLPBBXO_SOLBbLLvkFDxasEdGzJGdASfe7zz6_tdiLkSix54MLP_6AOXnKSZRk3eMQfsGyPvCUrUFyP4pBKxTcpCX9nlOyezT2jUitSK_dcVSu2MhNmGgAGvzizoJ_PwqIxG9cRLTcpL1Ei5DQrdQy7bygj7fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
⚪️
عمق اسکواد رئال مادرید برای فصل آینده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/Futball180TV/102022" target="_blank">📅 21:33 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102021">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e76692a40.mp4?token=joDSwv7XweHfsH3poL_bUo1BRbFi8ysrlWRHu8nWMf8E_Sdd0TPrt_NDW-tkqUviEKd3SEzG4a3iEhaugWQid-tYm6560WMLQpUXpAp5clRHJqvQSJTTvTgShs5K3ick14nHYzYWmKp1yBYsktJZ8lZ-Zd906pgp2SpT-J6HLniqH6uuST2bouZbd73E4SQFqO9GYINZBR3aITKOV89UBMQZMIm3bDTI9_NoLjYOAQMSa-ZuWgCfrZ7SLUnGlZpa7QxjxEHvqkl43FpzOs0jItsr4hPrTqX-BL-c62Dc-f1TAQ70m9_wsfdXNwUyvd47Jl_xvIOYGzQ-BzSH57c7KGGBnwqctn9EvRBVJ-8OEUC6LuxxyHCdE4D3XcamUuXHIEU5kXtDt41d_eSeeWTi-sdh6eX8h30yGTbN61ZI1FCTTk-xIrcVOyBeFpuKoEIueomTwWFIwCqEpVM76xNBNdiSfK49W3E5VCiK1KGakkBOr2zBsREGPadY8TC1Y1fQ1Sx4Du8w8Ovl3ADNt6Leqg7ZjARD1mGanEckFNpZKL6xXbsZfGTg-t5bVIEpdvZuvXy0OKXrn-bX4JxVSUcCweTHYrMrivIYTeQCTCQ6IWqK7NhsUW8vkISLic3A9b9SNxcEUSkqYV5ASstfrnJ9-2FRL9z2fZpX8uMYZmPLQIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e76692a40.mp4?token=joDSwv7XweHfsH3poL_bUo1BRbFi8ysrlWRHu8nWMf8E_Sdd0TPrt_NDW-tkqUviEKd3SEzG4a3iEhaugWQid-tYm6560WMLQpUXpAp5clRHJqvQSJTTvTgShs5K3ick14nHYzYWmKp1yBYsktJZ8lZ-Zd906pgp2SpT-J6HLniqH6uuST2bouZbd73E4SQFqO9GYINZBR3aITKOV89UBMQZMIm3bDTI9_NoLjYOAQMSa-ZuWgCfrZ7SLUnGlZpa7QxjxEHvqkl43FpzOs0jItsr4hPrTqX-BL-c62Dc-f1TAQ70m9_wsfdXNwUyvd47Jl_xvIOYGzQ-BzSH57c7KGGBnwqctn9EvRBVJ-8OEUC6LuxxyHCdE4D3XcamUuXHIEU5kXtDt41d_eSeeWTi-sdh6eX8h30yGTbN61ZI1FCTTk-xIrcVOyBeFpuKoEIueomTwWFIwCqEpVM76xNBNdiSfK49W3E5VCiK1KGakkBOr2zBsREGPadY8TC1Y1fQ1Sx4Du8w8Ovl3ADNt6Leqg7ZjARD1mGanEckFNpZKL6xXbsZfGTg-t5bVIEpdvZuvXy0OKXrn-bX4JxVSUcCweTHYrMrivIYTeQCTCQ6IWqK7NhsUW8vkISLic3A9b9SNxcEUSkqYV5ASstfrnJ9-2FRL9z2fZpX8uMYZmPLQIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🔵
امیرحسین صادقی: وحید مرادی من و فرزاد را در هتل المپیک آشتی داد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/Futball180TV/102021" target="_blank">📅 21:03 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102020">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qm0HGA70W7u9EnzI7dY5CGrngqs-CVDrPOUWIcs-l-SukvMlftKng5C_AIZ8zMARIDqSpTKNLHmzssqe0nT9tXf04fhWG-H-N21jSLLqm5LT7s-mQ9nj8u8BifQ3t95kl9Y40IPHSNTUvJnLMxmNOFiED26NGolSj6M0jHnygpO0JZ1bftFuXPLGX92KUudo1Oi_HNy5lYWjhyj_lPU96qkuha7YkDFbwzDET9jKrQFAVV6KVSzxCGpwB50tSeE3HLOgA8sPmdj7Wh86UY8sVqW4RqwwdIYA9aqxD4ZTteha_W5dvDiVdgcJeSmrVzxA0k2rAMu9dwZl4Y4VuP_awA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
🚨
پژمان جمشیدی که به تجاوز متهم شده بود، در رای نهایی دادگاه از این اتهام تبرئه شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/Futball180TV/102020" target="_blank">📅 20:57 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102019">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SVxdIWy8M-yrsqODg4Tfc11o_pbzHyjGAYkGDfcNXhd3_0tRV5ZLu9OeKeeCrgdzFraK2IQpOjFciwd8cbjYEicGL_AQpKUs1ySdwbua3tLgWRB3x1BmOglAlTaAxrkha6amIoa_nLIEPPfjwsp2T74OnkbUhKwzlHvDJrrUpygSkH1XAmRS6v0SOyTAEfPfXly5oUwRF_vvn8Ygy3a4zsB8IGESTiykdLMeRncworijfBegWPtqLk_0W8mfmzd0ecuXlhyZJkUCgHE3b__6VqLqZDv7jpi3EjFLO1rmFc1lhpWGoLSC5CLQHn3yV-zY0GmEERCYUgsoXXwHxyalRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
💣
آرانچا رودریگز: انتظار میرود که یان دیوماندی این هفته به تمرینات رئال مادرید بپیوندد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/Futball180TV/102019" target="_blank">📅 20:43 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102018">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/260d53f1d3.mp4?token=O72gAn2RjfWYhG2M3dj7t2ecKmlz7nBypTsvLfzPmyB7-wZLda1x-_zjJksLc5otzl8FLbXLYV5vZ-1eslf6Xb7Egw-yI1aFOjg4YmZE5EBiyR2v1momHunw4ZsTMiVvcLcufZexvrnWM_hzo_KJIz-46F97INcUBn5QVeOLiMRblr_fGAD0M0OoArlDPNj2Ufd9pLAEOac2TOhOgNXZ054mI-MnjqFamXNz96ORCp78U09ONnCyWk3nCblpeDhtrNhuHizNn1r1hco1gm2LpOYIxg7ZK_WbFNDNSM4NkGI-CJkoEjj7Gchr5jyFn-cb9SOgizJcQ3Ab4CewacaHbxv7Yd9a6iq3cI-jb-90O6Hqvk0TdpJ5pMz9HjjNekcGPoQ73DGJPhFgzan8w-4ZpjCnWRsbJ_-AMtW2icEsawsBWpYS6c3RzA2J1oe_rY3NS9Wr5vX09NsHJRKS3PZ3N2J4owdDOFNHpI-X3jhJ38eQlRKUlt-bnpX5Da3eCXck2SZK26th1665qQrn_A4Pv_ruNRpMj-3Hk_dM58eyWPZjwwPSitmb0w1ECb6J0Mg1dPgJflQApdFb6qHhhBeeDp3-6YBDXa1jRg-mYUCnk8c-ASoL0pZEfmGyMxA06nuVdh3B92HPSMmm1VnPr9oGqecrimcAt_KfLf9NV9WLaA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/260d53f1d3.mp4?token=O72gAn2RjfWYhG2M3dj7t2ecKmlz7nBypTsvLfzPmyB7-wZLda1x-_zjJksLc5otzl8FLbXLYV5vZ-1eslf6Xb7Egw-yI1aFOjg4YmZE5EBiyR2v1momHunw4ZsTMiVvcLcufZexvrnWM_hzo_KJIz-46F97INcUBn5QVeOLiMRblr_fGAD0M0OoArlDPNj2Ufd9pLAEOac2TOhOgNXZ054mI-MnjqFamXNz96ORCp78U09ONnCyWk3nCblpeDhtrNhuHizNn1r1hco1gm2LpOYIxg7ZK_WbFNDNSM4NkGI-CJkoEjj7Gchr5jyFn-cb9SOgizJcQ3Ab4CewacaHbxv7Yd9a6iq3cI-jb-90O6Hqvk0TdpJ5pMz9HjjNekcGPoQ73DGJPhFgzan8w-4ZpjCnWRsbJ_-AMtW2icEsawsBWpYS6c3RzA2J1oe_rY3NS9Wr5vX09NsHJRKS3PZ3N2J4owdDOFNHpI-X3jhJ38eQlRKUlt-bnpX5Da3eCXck2SZK26th1665qQrn_A4Pv_ruNRpMj-3Hk_dM58eyWPZjwwPSitmb0w1ECb6J0Mg1dPgJflQApdFb6qHhhBeeDp3-6YBDXa1jRg-mYUCnk8c-ASoL0pZEfmGyMxA06nuVdh3B92HPSMmm1VnPr9oGqecrimcAt_KfLf9NV9WLaA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چنتا سوپرگل قیچی‌برگردون ببینیم تا روحمون ارضا بشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/Futball180TV/102018" target="_blank">📅 20:05 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102016">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/g4h1LrQd6p7fZFM6FO8wJib4NetlUEanKKT4qhMBQg04978XiHBcOG47EXS7GfLA5-YZMTfGeXZW61lqqhAUKSM7yfUG4c62nFZTxPq-nNX9Xoo813wQr7H9JOeiDDxogb7PvoeShOJ2F_6LZlN_-QhE_zZEDhKl_4RcmUvyOvK503JEbEWPPbej5esrMptjCF4E4sCnKRzYmsr-oQoXwhpgp730wWCxz5Yb0Amu8hLxKK0b9i51RpKBOT-q0tJx6k8NzW20MGgeNux71d9hWSYR2vi7zfVZTYzWUusw5yV_VIvt3amAKHeOYlSPOyXOYempTamkeAjQS6jSsfXLcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NM9p233dVw60VwWINcroAYHkLUp7vqEa7IcyNEtBzSPHu307XCW_S_mNoxjgSW8yVOJfRVFXbtpsUgTCw7NhyMEqqmuFojY3ZKr5DONtJPyjkrhJVj1bsgCWVVCoJUKx4yUh_0fgwRdHhcWBQIt5JqPB7D-w6zMppdx0KBoAon_u3007VfEiTUer7iW0-wZHTzSk1stmfONy9KK1HOH4hfI7Qy0PMObX2rMcC8ua2C0izTZircLc6hCESe7Uh_NQefmkkWKUYnpWkl10173xK1fAEUp1i0uIqlD55d2f0m3clxyBSLCkvEMiNGqDnxmcmeR-ZDkBlQglS1oID-C7hw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎙
لواندوفسکی:
شاید مجبور باشیم ۱۰۰ یا ۲۰۰ سال دیگه صبر کنیم و منتظر بمونیم تا دوباره بازیکنی مثل مسی ببینیم.
🐐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/102016" target="_blank">📅 19:58 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102015">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o8n1mozVXYGFyaOAEHkAyHNRXvGGCQ_8yPa3u4xdzvCvN0TJRa0VvbqllaCiCBVaShndLemgTXJdY1f0U51NBQa-QhUouwpPskrYk5qdgFfufmisHgK8GlH7PmyrLUouqUEt_MqJqsIwiQwz_nNG2g4gxAQRfm09i2YB_GBnrssM4UOG7gOblzhjO58Y_xqnSTYmFTT_hMZhiJYgZ50_QGC_uFrvR8P8rxd3nvBtOLmqukMbHdRGUtuMhSVbL30Adsq1zd_XzPaBIfD3g1NHm_zTxaRfLbM-6VDHDEhMKK9mxPV9_HO6trqAD_VoiPOnIJNt6OUa3Ee5jq2Hvq9aqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💰
گران‌ترین انتقال‌های تاریخ فوتبال با در نظر گرفتن تورم:
🥇
رونالدو: ۸۰ میلیون پوند → ۲۹۲ میلیون پوند
🥈
ادن هازارد: ۱۵۰ میلیون پوند → ۲۴۵ میلیون پوند
🥉
آلن شیرر: ۱۵ میلیون پوند → ۲۳۸ میلیون پوند
نیکولا آنلکا: ۲۳.۵ میلیون پوند → ۲۲۶ میلیون پوند
فیلیپه کوتینیو: ۱۴۲ میلیون پوند → ۲۱۷ میلیون پوند
پل گاسکوئین: ۵.۵ میلیون پوند → ۱۹۷ میلیون پوند
مارک اوورمارس: ۲۵ میلیون پوند → ۱۹۶ میلیون پوند
گرت بیل: ۸۶ میلیون پوند → ۱۹۲ میلیون پوند
استن کولیمور: ۸.۵ میلیون پوند → ۱۷۹ میلیون پوند
ریو فردیناند: ۳۰ میلیون پوند → ۱۷۵ میلیون پوند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/102015" target="_blank">📅 19:49 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102014">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb3e14eaaf.mp4?token=ULWZyZuWDdZUafvyOrSvIS3WG7kut1aMD4CtIboosEoRShK4NGa1FkAJDngDiwQQAc5o9gifZX0sm-VufZFzcENVO3y5PqZvJBiJP3uTruEpX4LBPsIj8-2Med_5ht1I8JRrZHE_OnJWvrTcTc2Oyup0AA712PnWbPK1wHEkXwpxRuqHiH19GZb4g6JzrPyKNasoiMiFvd4c2rYBmZX8szHXpYniyly6f4KYH1NjJpzGC3aH4JVvDeaOMsRuYQISdVBuF3qRmx1fFWJ1BSVppHIr8YKL0fmv5hxm7-MGm8xkXmt2fhinJOAw8rtIOJDoDlhcJNc_0xSyq78Cu79Q7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb3e14eaaf.mp4?token=ULWZyZuWDdZUafvyOrSvIS3WG7kut1aMD4CtIboosEoRShK4NGa1FkAJDngDiwQQAc5o9gifZX0sm-VufZFzcENVO3y5PqZvJBiJP3uTruEpX4LBPsIj8-2Med_5ht1I8JRrZHE_OnJWvrTcTc2Oyup0AA712PnWbPK1wHEkXwpxRuqHiH19GZb4g6JzrPyKNasoiMiFvd4c2rYBmZX8szHXpYniyly6f4KYH1NjJpzGC3aH4JVvDeaOMsRuYQISdVBuF3qRmx1fFWJ1BSVppHIr8YKL0fmv5hxm7-MGm8xkXmt2fhinJOAw8rtIOJDoDlhcJNc_0xSyq78Cu79Q7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الگوت کیه؟
دیومانده: رونالدو
رونالدو یا مسی؟ مسی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/102014" target="_blank">📅 19:39 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102013">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromچِشم به راهیم</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8c1d6e560e.mp4?token=JRLvFQPUuh9txrXLE9AXmBh6BOHZ09DAYHYDBldL2wa4ytCC8wTJAnpTxZjNjrn7fuuAg-Y3KLGykeoZTdPbGxJ_E1ZkKYQqA-6BXVYC8bDIwTxDGQa9xZg56lC60Le5rHt1Iuc0eOiFgqxVsEG0znu1ic_icnXxkUm5F-bgUL8veVPBTwbP0TkG2_0WOcUYvKzYxLvsFhvbphyVIM3RZbXC5VzIQjKB41T_8MKsKmWI3Ed-0qSlkt5l5IF6DZ_zOixq1OHKSCrPjjYyk00GzzbguUVFIOrnYI0sEeAElq18uCM3KOs5x8aEuz8oPlFq-m4GdWhzpKIK1HJY86tnbBLSDDZYWKmXQUveblrCaZ6l5qbZDlhu6LINuA7z-j6LcOS0xgd865Y7LLL4SpRywdKpTFUC1OuGjJcJWetR8leaPKsCVEgIKyK9shA3UpUIs0NcH8M8H860jCPitnrpu2hMUeQyTGdpyYDdpKq-AKHr1J-yHWcJpWQOiq0x3sZoznhPBBaDiry-LAgDM_xfqXPmfjBb9Nepp0fMiPfEYK-z8TcT2Ah-0G6s_oaT0xmtZ8tnYxz8Jqtx51Z05qJnh485mClI7jjTmD6bh4Cw5KO8VD3kihN85V0TJUGuyhej_RqAH-uuWrntJa7-9BXBkiZfurCdwmRytkT6-M0nqr8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8c1d6e560e.mp4?token=JRLvFQPUuh9txrXLE9AXmBh6BOHZ09DAYHYDBldL2wa4ytCC8wTJAnpTxZjNjrn7fuuAg-Y3KLGykeoZTdPbGxJ_E1ZkKYQqA-6BXVYC8bDIwTxDGQa9xZg56lC60Le5rHt1Iuc0eOiFgqxVsEG0znu1ic_icnXxkUm5F-bgUL8veVPBTwbP0TkG2_0WOcUYvKzYxLvsFhvbphyVIM3RZbXC5VzIQjKB41T_8MKsKmWI3Ed-0qSlkt5l5IF6DZ_zOixq1OHKSCrPjjYyk00GzzbguUVFIOrnYI0sEeAElq18uCM3KOs5x8aEuz8oPlFq-m4GdWhzpKIK1HJY86tnbBLSDDZYWKmXQUveblrCaZ6l5qbZDlhu6LINuA7z-j6LcOS0xgd865Y7LLL4SpRywdKpTFUC1OuGjJcJWetR8leaPKsCVEgIKyK9shA3UpUIs0NcH8M8H860jCPitnrpu2hMUeQyTGdpyYDdpKq-AKHr1J-yHWcJpWQOiq0x3sZoznhPBBaDiry-LAgDM_xfqXPmfjBb9Nepp0fMiPfEYK-z8TcT2Ah-0G6s_oaT0xmtZ8tnYxz8Jqtx51Z05qJnh485mClI7jjTmD6bh4Cw5KO8VD3kihN85V0TJUGuyhej_RqAH-uuWrntJa7-9BXBkiZfurCdwmRytkT6-M0nqr8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
اگر قصد دارید سفر اربعین را با اتوبوس راهی مرز شوید، پیدا کردن بلیت را به سپاس بسپارید
🔹
سامانه پایش آنلاین سفر (سپاس) با اتصال به همه درگاه‌های رسمی فروش اینترنتی بلیت اتوبوس امکان مشاهده و مقایسه ظرفیت‌ها را در یک سامانه فراهم کرده است تا سریع‌تر و آسان‌تر بلیت مناسب سفر خود را پیدا کنید.
🔹
از ۲۷ تیر پیش‌فروش بلیت سفرهای اربعین آغاز شده است. برای برنامه‌ریزی آسان‌تر سفر به سامانه سپاس مراجعه کنید:
🔗
sepas.rmto.ir
#چشم_به_راهیم
#اربعین_حسینی
#سازمان_راهداری_و_حمل_و_نقل_جاده_ای
🌐
rmto.ir
🌐
141.ir
@Cheshm_Be_Rahim</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/102013" target="_blank">📅 19:39 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102012">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🚨
⚪️
فوووووری از خوزه فلیکس دیاز: انتقال دیومانده به رئال مادرید نهایی شده و بیانیه رسمی فردا منتشر میشه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/102012" target="_blank">📅 19:27 · 04 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
