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
<img src="https://cdn4.telesco.pe/file/PKIxG6ZM3HudFY182CK-sG05fmF2EnsNv-12DWwwi3CWr6F9EajkSo7ou64ycKjfQ89TURVlkn_2adoyimoZZ_04TtXUNQvl4kp2CbPiW6TvsDQInbzHRu4aJAd6JGDOquK6cUdOQxJPswBKaA_41cMVhheekAoJJGtsQN787l6O3-ItqjyAemEF-PYM_FH9BidStDs13d1MVq7iJuWKTgBjs9I7xSWCgTIXQZ6hRGPvgmZXF1LdXE-F4YzT_LvUeR6QMr6IJBsc-Lrh09jScd-XDNvvr8NqD3moti6aqDO3nL-g5GW2L6nPPn4d5VYT6rqD4J9lively7k5fqd47Q.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 255K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-14 09:00:04</div>
<hr>

<div class="tg-post" id="msg-81039">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">قوات تابعة مكافحة إرهاب كردستان العراق تعتقل عدد من أبناء عشيرة الهركي في محافظة أربيل.</div>
<div class="tg-footer">👁️ 678 · <a href="https://t.me/naya_foriraq/81039" target="_blank">📅 08:55 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81038">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">⭐️
إعتقال "خورشيد هركي" من قبل قوات تابعة لمسعود البارزاني في محافظة أربيل شمالي العراق.</div>
<div class="tg-footer">👁️ 934 · <a href="https://t.me/naya_foriraq/81038" target="_blank">📅 08:53 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81037">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">⭐️
إعتقال "خورشيد هركي" من قبل قوات تابعة لمسعود البارزاني في محافظة أربيل شمالي العراق.</div>
<div class="tg-footer">👁️ 1.39K · <a href="https://t.me/naya_foriraq/81037" target="_blank">📅 08:47 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81036">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a710a25bde.mp4?token=In7Ykcug0Y_CYCMlsakhg1UmyDDLEYcM_cB_XHg1X1qygWfn5lhC-nrEVbA5_5B9b9Pt8YtMjSws2yBqVrGP1k5_JI2CT94BP6VIsLazoz-Na1ZgzH4WBFoRRtDOprDbPOKqW5ml5F05c_x4vL2taNLyvzfvlyMH4BlT72Zk4fmxrme2VROpQ6kxwI39-5k_QwRBzvFdtc7NLQd2_1cPsmK3zFxXj9zxDdZxONj0hFOiRzTMpso5XykUohb9CVYn5H0JUeXSkMk3tDMRQAfMigesy2YXSRhzw2XgVzVnYbiBA16vHIKC66QEdBENm75NJCaXfCCEbB0Vhw4bE59Omw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a710a25bde.mp4?token=In7Ykcug0Y_CYCMlsakhg1UmyDDLEYcM_cB_XHg1X1qygWfn5lhC-nrEVbA5_5B9b9Pt8YtMjSws2yBqVrGP1k5_JI2CT94BP6VIsLazoz-Na1ZgzH4WBFoRRtDOprDbPOKqW5ml5F05c_x4vL2taNLyvzfvlyMH4BlT72Zk4fmxrme2VROpQ6kxwI39-5k_QwRBzvFdtc7NLQd2_1cPsmK3zFxXj9zxDdZxONj0hFOiRzTMpso5XykUohb9CVYn5H0JUeXSkMk3tDMRQAfMigesy2YXSRhzw2XgVzVnYbiBA16vHIKC66QEdBENm75NJCaXfCCEbB0Vhw4bE59Omw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مصلى الإمام الخميني بعد إقامة صلاة الجنازة على الجثمان الطاهر لقائد الثورة الشهيد.</div>
<div class="tg-footer">👁️ 2.93K · <a href="https://t.me/naya_foriraq/81036" target="_blank">📅 08:19 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81035">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc9f781ff5.mp4?token=g8vObci7yTj9x8iTgKJKv5863J5JmImJOC_b2C2BYk8HQD1z12_Ma4CO90nDgdxH_jfMjQm3Z8B541gOVbFFBiJfGMdsmBDlnoH-FIu0gBDQ5FDY1574vE3_p0TFm6powmeAEkXNj1Pj9SUnbUEkzGUlhgK4Z4bK8ESbc_KMABAECEzgRRoQdDEPYx5i5c5aZtqnV0ePzdSN-JFXNkU_J-IQaeC5XXf7b3o4vn2wHEWJN74P-za1HLlRnTSprVuJkdw3Rva7XWqXWNQNUMO1L0_tJy8cVPfoN9FPTpLghXZ1I4b1svczY1HasJ4hRhZPE-_Eeh-_6zQ9BpRNxVRx4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc9f781ff5.mp4?token=g8vObci7yTj9x8iTgKJKv5863J5JmImJOC_b2C2BYk8HQD1z12_Ma4CO90nDgdxH_jfMjQm3Z8B541gOVbFFBiJfGMdsmBDlnoH-FIu0gBDQ5FDY1574vE3_p0TFm6powmeAEkXNj1Pj9SUnbUEkzGUlhgK4Z4bK8ESbc_KMABAECEzgRRoQdDEPYx5i5c5aZtqnV0ePzdSN-JFXNkU_J-IQaeC5XXf7b3o4vn2wHEWJN74P-za1HLlRnTSprVuJkdw3Rva7XWqXWNQNUMO1L0_tJy8cVPfoN9FPTpLghXZ1I4b1svczY1HasJ4hRhZPE-_Eeh-_6zQ9BpRNxVRx4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ای پسر فاطمه، تسلیت تسلیت.</div>
<div class="tg-footer">👁️ 3.02K · <a href="https://t.me/naya_foriraq/81035" target="_blank">📅 08:18 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81034">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hf4gYCIHda8ArRu3bGHfPS_o72RRVEj3g4cwt-HJhQvhHYAvMmEYHFK97zgcTRXpI693ZFNS65eyzvGF8vrTja5R2HzN3ddtKmLjSduM_2HmtI29zgEMg07wbtBCsFecdGdB2dn_yFErr10JNNN8DtP_uxQylfZwryn_WGu0jXs0X7J9AVoUrOP_gA_YCEiOz7aQNF83-GXRgZbizecCytJBKoBwhIhrrNma8f8oxFuQBhOeiVxSTRCblkgNjnEvm_gzIdp8XLqUJP3Rup-jcz22LTGUT1Y_4sEMzdQTXnw2somOatuRU10xJw0FnBhmbPwsAJ6DnnO_vZ2AD4KaZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">يالثارات الحسين</div>
<div class="tg-footer">👁️ 3.14K · <a href="https://t.me/naya_foriraq/81034" target="_blank">📅 08:16 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81033">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f10526db91.mp4?token=bJHRpggm1fDkd_EEE2TJr0Gho7DQbX5Lp1Xx5eNLn1V0WsrMD8n36xPzTzunFePfd8AbMF-QMkPsw288-24ilZhLgEYBZVa4K8boHtvgGcgnxEM7K5Y3buvsdJS_aGixz2PDxLvERue0pidhdVw8CM3L8kMqER1l1kz6hFTiHgiPIJrHSsMkY0zuEAAtHzoKvkNAnrSrIAMgHL3Q7FFxgJJMtP1hKk8rj25iHwqzwFfptVYhCCFySctvL68vWFgU4ilVTxti8pVfh-wJcAWzJv9AaZxFhNFETI1YfgLJeQSt_MvXowKO7kDpMqTfiDGcpyU1q-jDlmUQlqxWp69hpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f10526db91.mp4?token=bJHRpggm1fDkd_EEE2TJr0Gho7DQbX5Lp1Xx5eNLn1V0WsrMD8n36xPzTzunFePfd8AbMF-QMkPsw288-24ilZhLgEYBZVa4K8boHtvgGcgnxEM7K5Y3buvsdJS_aGixz2PDxLvERue0pidhdVw8CM3L8kMqER1l1kz6hFTiHgiPIJrHSsMkY0zuEAAtHzoKvkNAnrSrIAMgHL3Q7FFxgJJMtP1hKk8rj25iHwqzwFfptVYhCCFySctvL68vWFgU4ilVTxti8pVfh-wJcAWzJv9AaZxFhNFETI1YfgLJeQSt_MvXowKO7kDpMqTfiDGcpyU1q-jDlmUQlqxWp69hpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اللواء وحيدي في صفوف المصلين على الجثامين الطاهرة</div>
<div class="tg-footer">👁️ 2.98K · <a href="https://t.me/naya_foriraq/81033" target="_blank">📅 08:14 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81032">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">مقطع فيديو كامل لإقامة صلاة الجنازة على جثمان الإمام المجاهد الشهيد، آية الله العظمى السيد علي الخامنئي، وذلك بواسطة آية الله جعفر سبحاني.</div>
<div class="tg-footer">👁️ 2.98K · <a href="https://t.me/naya_foriraq/81032" target="_blank">📅 08:14 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81031">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">مقطع فيديو كامل لإقامة صلاة الجنازة على جثمان الإمام المجاهد الشهيد، آية الله العظمى السيد علي الخامنئي، وذلك بواسطة آية الله جعفر سبحاني.</div>
<div class="tg-footer">👁️ 3K · <a href="https://t.me/naya_foriraq/81031" target="_blank">📅 08:13 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81030">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b2eeb37e5f.mp4?token=SmNtJwSmoS-QOpidlbz0IpraUIf9JN2h9fSqw2UD6waQoxdw5uaj71VATnDawuiQXDbApg46LwrvhZUlOZ0wC0d7DMrV4xxOWM3UgUYz9xOR0eQbW82E3SoLv3FqFwlT7dRd8KSXYe6iuNdI6yY-Xd54KzwfNOwTpYJ-1r-e8jL1wP05Z5JFZbiUPEpj3ae71EJ8ZoNdKye_Z56ip20_uIYMnXs_jPU9tHZhRCj-xInGdSFD_PMTn0_UK5pxKhp_RRcsNVMv_Eqjj8vhLA34sIFCo7vX87oYfluVAc1NfEwZTh0qouoz_gP5qVnt6CTFEqVAHeNpk8dk6ftVC2rYSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b2eeb37e5f.mp4?token=SmNtJwSmoS-QOpidlbz0IpraUIf9JN2h9fSqw2UD6waQoxdw5uaj71VATnDawuiQXDbApg46LwrvhZUlOZ0wC0d7DMrV4xxOWM3UgUYz9xOR0eQbW82E3SoLv3FqFwlT7dRd8KSXYe6iuNdI6yY-Xd54KzwfNOwTpYJ-1r-e8jL1wP05Z5JFZbiUPEpj3ae71EJ8ZoNdKye_Z56ip20_uIYMnXs_jPU9tHZhRCj-xInGdSFD_PMTn0_UK5pxKhp_RRcsNVMv_Eqjj8vhLA34sIFCo7vX87oYfluVAc1NfEwZTh0qouoz_gP5qVnt6CTFEqVAHeNpk8dk6ftVC2rYSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انتهاء الصلاة على الجثامين الطاهرة</div>
<div class="tg-footer">👁️ 2.82K · <a href="https://t.me/naya_foriraq/81030" target="_blank">📅 08:13 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81029">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">انتهاء الصلاة على الجثامين الطاهرة</div>
<div class="tg-footer">👁️ 2.62K · <a href="https://t.me/naya_foriraq/81029" target="_blank">📅 08:12 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81028">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">أقامة الصلاة على جثمان حفيدة القائد الشهيد</div>
<div class="tg-footer">👁️ 2.69K · <a href="https://t.me/naya_foriraq/81028" target="_blank">📅 08:10 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81027">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df0b8e849c.mp4?token=Ic-ZCAWVVxImvTBLy-4XIeZKj9F280ac9mlEkL9aWRdopvmZIOWCsgGDhzBme9iOrylqsVJYTAOlZOr6wTh7vOJf_CJWn8Ecf4cFAOBfv6phf1AzCU_wm6Lv3Q9tH0JPEzWfQCzRGAWmLS7sdvHzz_Ik_0Lfh6STe3WNAblO-3hEqRbnokPxXASA6tJ_jOhGfiwb90aWs5SdQGRTWN6_HNt7AFCZq9bD3Y70XghuWu-AtGoMQN0g5Xr8sGovG7oLvZZ1MGGvj14SjyrmWAJiDAbZZV-oiMPIamCaLi3jLknNjvkWHbXC6x4pTJxROywI5iHaUp8gXDk_8MIbm9GkOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df0b8e849c.mp4?token=Ic-ZCAWVVxImvTBLy-4XIeZKj9F280ac9mlEkL9aWRdopvmZIOWCsgGDhzBme9iOrylqsVJYTAOlZOr6wTh7vOJf_CJWn8Ecf4cFAOBfv6phf1AzCU_wm6Lv3Q9tH0JPEzWfQCzRGAWmLS7sdvHzz_Ik_0Lfh6STe3WNAblO-3hEqRbnokPxXASA6tJ_jOhGfiwb90aWs5SdQGRTWN6_HNt7AFCZq9bD3Y70XghuWu-AtGoMQN0g5Xr8sGovG7oLvZZ1MGGvj14SjyrmWAJiDAbZZV-oiMPIamCaLi3jLknNjvkWHbXC6x4pTJxROywI5iHaUp8gXDk_8MIbm9GkOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">أقامة الصلاة على جثمان حفيدة القائد الشهيد</div>
<div class="tg-footer">👁️ 2.75K · <a href="https://t.me/naya_foriraq/81027" target="_blank">📅 08:10 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81026">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a6dc481a81.mp4?token=Gh5YkoopXC2msEz-3Ixkq086-uU5qdd7Al_LSnWlD69JkjPDCqbezSAkzek9g2Mumr_0fr6eOUcaoAjSAy-y6zcn_ClgSiz_RenWSWvjvrvT-UgjDSs2mRau1kEJ6vy1KPaHYjoxA1dd75M27EmvdVqjdhBprfwbpDoo-42OvwLv4_gAMgHs9JxnipCiUwiHV4xolr4Ou0KFU3zzMx78LePgzQfoeWXHyu35uJRnes4GiyXs6C7jTRJLUyZRIBUGwYUiTgGbebmgsCUKuvpwbJ_wC9A6_jm2ED19kIAWonvYQHTcwNlti1MtQ3SQMDP1hWF3qs35Tb-wMuLNpWl9RA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a6dc481a81.mp4?token=Gh5YkoopXC2msEz-3Ixkq086-uU5qdd7Al_LSnWlD69JkjPDCqbezSAkzek9g2Mumr_0fr6eOUcaoAjSAy-y6zcn_ClgSiz_RenWSWvjvrvT-UgjDSs2mRau1kEJ6vy1KPaHYjoxA1dd75M27EmvdVqjdhBprfwbpDoo-42OvwLv4_gAMgHs9JxnipCiUwiHV4xolr4Ou0KFU3zzMx78LePgzQfoeWXHyu35uJRnes4GiyXs6C7jTRJLUyZRIBUGwYUiTgGbebmgsCUKuvpwbJ_wC9A6_jm2ED19kIAWonvYQHTcwNlti1MtQ3SQMDP1hWF3qs35Tb-wMuLNpWl9RA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">أداء صلاة الجنازة على جثامين عائلة القائد الشهيد</div>
<div class="tg-footer">👁️ 2.77K · <a href="https://t.me/naya_foriraq/81026" target="_blank">📅 08:08 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81025">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6bac6feba4.mp4?token=VJEQQ0EuK59lVCAtk2WjO6MIvKyuhIzfgnfdhhVd1V4uTWLtUh7-f0UTfXXt6PUrrnc8XYo8CgZ0zp5vywiI8jVKuBDencLcng6QhK7U32aSHmtzrrSJHJDYgSVSr8YWiGKW_qrWjFQZ3CKbT7gOgKDxDJfYVbeY12L0wJBkj0LR2uk2M_nWWB_n9GufdjCp_uL1bJLC_XYgnw5W96oqmJFi0PpiPYUGh2A7jZdFPPts_o5Lm_eHmi6vPLH-dexs4SYZ4KoTonJVfXhUg6ifxADo-GV1m10Vcip6abOP5xf6ZPUlEOvGTY03BSIJW4ELxTTO6Vu4qJoTmONSiZceKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6bac6feba4.mp4?token=VJEQQ0EuK59lVCAtk2WjO6MIvKyuhIzfgnfdhhVd1V4uTWLtUh7-f0UTfXXt6PUrrnc8XYo8CgZ0zp5vywiI8jVKuBDencLcng6QhK7U32aSHmtzrrSJHJDYgSVSr8YWiGKW_qrWjFQZ3CKbT7gOgKDxDJfYVbeY12L0wJBkj0LR2uk2M_nWWB_n9GufdjCp_uL1bJLC_XYgnw5W96oqmJFi0PpiPYUGh2A7jZdFPPts_o5Lm_eHmi6vPLH-dexs4SYZ4KoTonJVfXhUg6ifxADo-GV1m10Vcip6abOP5xf6ZPUlEOvGTY03BSIJW4ELxTTO6Vu4qJoTmONSiZceKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الآلاف يقيمون الصلاة على الجثامين الطاهرة في مصلى طهران</div>
<div class="tg-footer">👁️ 2.76K · <a href="https://t.me/naya_foriraq/81025" target="_blank">📅 08:07 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81024">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rc9uZ_Oyu8PKRHxn72uxHkFj6oOKX_NbWNP8dCy71JIUyF73g4uAP8PEJ7Vn89IV3ddHp-ThGc6OLH8Bc2V-WfRTCHU7ZZvfEwDgE37fkRsWax1VpUXkJ6eEnaVfVvwvs48qfEVCVY9RfaWih0nzzYdnPtSNSrcAfxvUAy2-10aDiDZU-GqWtzx5Kjw5YwyhdiBisVEvH_mdzjNn4kFMJkktdbf4BNtGMDVSqPGASY38DkO1fOXbNABtodroXzFPb4qDaIIolMcBSkahn0W3j2hOb6pY8rzMyiSR56ks5IdzOKQ0oWVRqJhQ5vZ6vvhT5F_oBs17K90gHKL5hw-ITg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الصلاة على جثامين شهداء عائلة الإمام الشهيد</div>
<div class="tg-footer">👁️ 2.73K · <a href="https://t.me/naya_foriraq/81024" target="_blank">📅 08:06 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81023">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">الصلاة على قائد الثورة الشهيد</div>
<div class="tg-footer">👁️ 2.64K · <a href="https://t.me/naya_foriraq/81023" target="_blank">📅 08:06 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81022">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d2b942b32.mp4?token=rrQZB2sXSXjqj56uzyLfBc2vgS_sbH-ezBisFJuyZ6-DU6AR4geuiHAqy76ZE-73CbJpMh78tuYQ0e5RkBfDaNEG2Bt9G2tbAVxQib4d3nbTMw8xNSYKWuobsz-TyQypm8VtuNBxNvK2uC96Cl23uYsg-0N6nbiGngUYhspPgmfNTDdvbWA-HV2KRXzO8-N2s6H0SwA1BXHZIMxDLI9ljO5nyEFLim7jBl9REx0pIMjP3HEJOAqRkzl1E6NTo2zN3Y7wxILcLvT_KaxkQgOnp1M6p92JqbyUyE-hkUIhCXs3aFuoIiiD_tet04ZI7n6lZsuybPlHRQX8FRhMutt31A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d2b942b32.mp4?token=rrQZB2sXSXjqj56uzyLfBc2vgS_sbH-ezBisFJuyZ6-DU6AR4geuiHAqy76ZE-73CbJpMh78tuYQ0e5RkBfDaNEG2Bt9G2tbAVxQib4d3nbTMw8xNSYKWuobsz-TyQypm8VtuNBxNvK2uC96Cl23uYsg-0N6nbiGngUYhspPgmfNTDdvbWA-HV2KRXzO8-N2s6H0SwA1BXHZIMxDLI9ljO5nyEFLim7jBl9REx0pIMjP3HEJOAqRkzl1E6NTo2zN3Y7wxILcLvT_KaxkQgOnp1M6p92JqbyUyE-hkUIhCXs3aFuoIiiD_tet04ZI7n6lZsuybPlHRQX8FRhMutt31A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الصلاة على قائد الثورة الشهيد</div>
<div class="tg-footer">👁️ 2.65K · <a href="https://t.me/naya_foriraq/81022" target="_blank">📅 08:04 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81021">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/466cfde4ec.mp4?token=U-4nTOD1MPTef4CFQMnARcx1SYmgfM_Fx5PqmI_6Kemu0XE7n1gB2Fe_nSQFUGdp89u9t7dJZf8Op6dAgklCUQEXd9TnYA_act6MOtS0yYjklWYG9hCAN1rDFoTvYhQvCfOLk6mxoWbHjGmofiBPCZbOlL560D4TnOt0P5FkddpIN4tU6DdRs2nzf7OI12jNwK2YTmAVlye2h0OcgWbT0mVBktmndLK-4kj_xNf5JgBt_5wwoD1KEm7z_gOlJAwU2vYNqSylGLQjXY5gGw_nESptLHMTpKi0CKS2Znfe91AVU48prjzY8zBFfNMSXom9EUEUWu3Tf1vzYC0xlaya9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/466cfde4ec.mp4?token=U-4nTOD1MPTef4CFQMnARcx1SYmgfM_Fx5PqmI_6Kemu0XE7n1gB2Fe_nSQFUGdp89u9t7dJZf8Op6dAgklCUQEXd9TnYA_act6MOtS0yYjklWYG9hCAN1rDFoTvYhQvCfOLk6mxoWbHjGmofiBPCZbOlL560D4TnOt0P5FkddpIN4tU6DdRs2nzf7OI12jNwK2YTmAVlye2h0OcgWbT0mVBktmndLK-4kj_xNf5JgBt_5wwoD1KEm7z_gOlJAwU2vYNqSylGLQjXY5gGw_nESptLHMTpKi0CKS2Znfe91AVU48prjzY8zBFfNMSXom9EUEUWu3Tf1vzYC0xlaya9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">من الصلاة على جثمان الشهيد القائد</div>
<div class="tg-footer">👁️ 2.68K · <a href="https://t.me/naya_foriraq/81021" target="_blank">📅 08:04 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81020">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v0JxJ7RqvZ50V-eyGaxw_Z98cRgTdMhOUnjQuL9uUkZSfGsUecifR2wk4m5iQDp3GJ7UJDYa_Qx5rULQUxY5t_ylTCfAPeJK84RIxT349kiqG76_dIQkO-WhyIYsUIGFGek7qonGcJk07xV504pX99EvU-90uMYhzysfhI_SmtavPk6SXV6xUmWSrFOJ9H_3HpnsoqgMF64GmMvAVgO28qNhUA7UU_b6xx1e5x2cg7hB5aaVvIgStpd8gVNAcImVLZlNKMtu26oT1GF4fqZJQ_D5qTdo5AHOwYSfm7Gg5jsUhzdyhYhrFsrNyS7VFc9hfkgu6NQgHcL-2eqvju2tIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بدء الصلاة على جثمان الإمام الشهيد</div>
<div class="tg-footer">👁️ 2.59K · <a href="https://t.me/naya_foriraq/81020" target="_blank">📅 08:03 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81019">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">رفع نداء "الصلاة الصلاة" على جثمان الشهيد القائد</div>
<div class="tg-footer">👁️ 2.65K · <a href="https://t.me/naya_foriraq/81019" target="_blank">📅 08:01 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81018">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b29f1eb22.mp4?token=Q7LcdIo4Jr2jlbachFuxVPA420bvK5fsFzyZmcmUJ9yw7CuKsLWXQ5tJdgeiDx7nueCooWjDbkmq0bjIL-S3u3SUXnOaXGQ5vfNAyXP5zbHZ2seuiNpMhXzVAGV4A7SnTZtlLI_qOvbDnEZwT3wLg-mMLJLX9sIFb9J4AczyWoaeRc1NHTSp59v_XMLc02oVLrLv08u1gsA_CE8efn4G4vRw3IRXdKlE-87IXiC3R6aBbVW3UFkrZQfAUzpKO3a_GcmAseAhqQoWU5MVQ9gxLAg2ej6vlhHcH4fmvbsmxvhvDAts7rukKQ_85Ak5RXMY3MU6Wxu0RHVnhacKwxpW6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b29f1eb22.mp4?token=Q7LcdIo4Jr2jlbachFuxVPA420bvK5fsFzyZmcmUJ9yw7CuKsLWXQ5tJdgeiDx7nueCooWjDbkmq0bjIL-S3u3SUXnOaXGQ5vfNAyXP5zbHZ2seuiNpMhXzVAGV4A7SnTZtlLI_qOvbDnEZwT3wLg-mMLJLX9sIFb9J4AczyWoaeRc1NHTSp59v_XMLc02oVLrLv08u1gsA_CE8efn4G4vRw3IRXdKlE-87IXiC3R6aBbVW3UFkrZQfAUzpKO3a_GcmAseAhqQoWU5MVQ9gxLAg2ej6vlhHcH4fmvbsmxvhvDAts7rukKQ_85Ak5RXMY3MU6Wxu0RHVnhacKwxpW6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بأي ذنب قتلت</div>
<div class="tg-footer">👁️ 2.69K · <a href="https://t.me/naya_foriraq/81018" target="_blank">📅 08:00 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81017">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">العلماء والقيادات الإيرانية حاضرة لإقامة الصلاة</div>
<div class="tg-footer">👁️ 2.66K · <a href="https://t.me/naya_foriraq/81017" target="_blank">📅 07:59 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81016">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b85d4a8db8.mp4?token=kMqatPIaoOv22HoUi37kIVzZuVSrMyFmkssaAKJX-FC2phnY3pTU9s0CZxaNh5KD6JKJlC2qHvF1OMom_30O7zTDn2w2Pz2JfLXVl7K7kkrhi1Sq96Dfo1BRjL2W_V4ZittXMh4v82euAw5t7YvxGrlyoK23Tdxs5RVLQzgumVO84pv3de6rh9pZnQG-LXHjsRj58LJbwXs5mJg1WpEH3JYnSOYgpwNa4SNtfypQwaTC4Yiv6-emoUkgvNuB151cWkZkCrzriQvIXF3HWNTR_VgZtEeqrIiYTVqnLmgQyLKkorBUalVQu04hrKsV4PgabyxqX5SdW_Jl_fXHk2uqPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b85d4a8db8.mp4?token=kMqatPIaoOv22HoUi37kIVzZuVSrMyFmkssaAKJX-FC2phnY3pTU9s0CZxaNh5KD6JKJlC2qHvF1OMom_30O7zTDn2w2Pz2JfLXVl7K7kkrhi1Sq96Dfo1BRjL2W_V4ZittXMh4v82euAw5t7YvxGrlyoK23Tdxs5RVLQzgumVO84pv3de6rh9pZnQG-LXHjsRj58LJbwXs5mJg1WpEH3JYnSOYgpwNa4SNtfypQwaTC4Yiv6-emoUkgvNuB151cWkZkCrzriQvIXF3HWNTR_VgZtEeqrIiYTVqnLmgQyLKkorBUalVQu04hrKsV4PgabyxqX5SdW_Jl_fXHk2uqPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">العلماء والقيادات الإيرانية حاضرة لإقامة الصلاة</div>
<div class="tg-footer">👁️ 2.73K · <a href="https://t.me/naya_foriraq/81016" target="_blank">📅 07:57 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81015">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/746ceaf248.mp4?token=NPVWWNecNe8zCp9HtmhLk-_4oYRmhU0YYHXDaVmdMA6hdlDrup6r-BBc-nJ3gIPyU1dLf5e7XeqWzPFbDb-QPrJhIIPO30hOokxtOmPOuaGNdFiruxb5oOlgtG_cXNwztWQECpgk5qyGxCCbvK32LVIuRwpE9lKnv1jAG2TO_zEpsIgnhQHyfL8PhInxxne4XJEHGtO7rMgSSy2nfmEb0NisU_l1GqJirddASAsA7Fl5mBspxuY9icfHrkpIowHusmGFgLlVlFi6kxh1FFzy1mI0U17Ce6m2zz3P0RxQQCPJiKxN22eqhUWEAJSVYCqVcFdxPseNsyIOqDKNQBUkGDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/746ceaf248.mp4?token=NPVWWNecNe8zCp9HtmhLk-_4oYRmhU0YYHXDaVmdMA6hdlDrup6r-BBc-nJ3gIPyU1dLf5e7XeqWzPFbDb-QPrJhIIPO30hOokxtOmPOuaGNdFiruxb5oOlgtG_cXNwztWQECpgk5qyGxCCbvK32LVIuRwpE9lKnv1jAG2TO_zEpsIgnhQHyfL8PhInxxne4XJEHGtO7rMgSSy2nfmEb0NisU_l1GqJirddASAsA7Fl5mBspxuY9icfHrkpIowHusmGFgLlVlFi6kxh1FFzy1mI0U17Ce6m2zz3P0RxQQCPJiKxN22eqhUWEAJSVYCqVcFdxPseNsyIOqDKNQBUkGDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
وصول أبناء قائد الثورة الشهيد والقيادات الإيرانية إلى مصلى الإمام الخميني لإقامة صلاة الجنازة على جثمان الإمام الخامنئي.</div>
<div class="tg-footer">👁️ 2.86K · <a href="https://t.me/naya_foriraq/81015" target="_blank">📅 07:54 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81014">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/96e3bc9a09.mp4?token=KK0aiBy_o_dqGsEkVdzSNa-J6S8xocN5N-5vQeIRHQHQPcteIJK18gbMZkbcMYgqClNJBs-__pVelLKUtqVt67n_DIHnxfE97zhtaxNf6IYN_LDOs7TC1pQtGx3YnYrdjQfwzbhN0JbZph9EIOLdbah-D8zUN1u5NbhwliN2xWteMzwgXrfsleF3tJAd8GAXl6cPmnVFJv0uSZGC7nh-Oy0cSuY8wclxNeBPQsciVEv98EtBPo0YrulwY4iK3tPppDbFmTVMjGRcC8JTf5VOsmHmh7EO_DeTF0i2o1r6rRvomh0raxJzpdDWM5SpCce1pIwnbtsu8IZDodVOXWBKOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/96e3bc9a09.mp4?token=KK0aiBy_o_dqGsEkVdzSNa-J6S8xocN5N-5vQeIRHQHQPcteIJK18gbMZkbcMYgqClNJBs-__pVelLKUtqVt67n_DIHnxfE97zhtaxNf6IYN_LDOs7TC1pQtGx3YnYrdjQfwzbhN0JbZph9EIOLdbah-D8zUN1u5NbhwliN2xWteMzwgXrfsleF3tJAd8GAXl6cPmnVFJv0uSZGC7nh-Oy0cSuY8wclxNeBPQsciVEv98EtBPo0YrulwY4iK3tPppDbFmTVMjGRcC8JTf5VOsmHmh7EO_DeTF0i2o1r6rRvomh0raxJzpdDWM5SpCce1pIwnbtsu8IZDodVOXWBKOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
رجال أبوجبريل يدخلون إلى مصلى الإمام الخميني في العاصمة طهران.</div>
<div class="tg-footer">👁️ 2.93K · <a href="https://t.me/naya_foriraq/81014" target="_blank">📅 07:50 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81013">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/21cc6541ca.mp4?token=Wt_633Da42OXzgGFuI8zE9K_k13uee3n_IgkrQrXzwZJvhtmFXyNFM5qENqMwTWkH1QJhqg0Kk6NWkoeAl-8NGpJU-YfCKXu7FpDHhZYdB8FfgyXx9_RLijftPNkeInyAnmTHrMy6Y5G3mK5iJ2ucAf-PymF4V8e5K16S3kOOwEPzbXsGkDiGdYYV2V2o6NoNTudjuZc-j5xdG4tlwbfNt5LPY14uE53EUXIrK04uqBP2xmluhei3452c6KXAFxtag9w2d3qwKMfyKaWgK9oGs11vA3jybVy0ysGTOvfHafnWefPDNtST1bzw46ZPijnvKpebgbBW8ug0E_egR59mw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/21cc6541ca.mp4?token=Wt_633Da42OXzgGFuI8zE9K_k13uee3n_IgkrQrXzwZJvhtmFXyNFM5qENqMwTWkH1QJhqg0Kk6NWkoeAl-8NGpJU-YfCKXu7FpDHhZYdB8FfgyXx9_RLijftPNkeInyAnmTHrMy6Y5G3mK5iJ2ucAf-PymF4V8e5K16S3kOOwEPzbXsGkDiGdYYV2V2o6NoNTudjuZc-j5xdG4tlwbfNt5LPY14uE53EUXIrK04uqBP2xmluhei3452c6KXAFxtag9w2d3qwKMfyKaWgK9oGs11vA3jybVy0ysGTOvfHafnWefPDNtST1bzw46ZPijnvKpebgbBW8ug0E_egR59mw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
عزف النشيد الوطني الإيراني في مصلى الإمام الخميني.</div>
<div class="tg-footer">👁️ 3.27K · <a href="https://t.me/naya_foriraq/81013" target="_blank">📅 07:41 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81012">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d62994becf.mp4?token=octFfi7WEZj4MfoNf0gUfvmJnbEOE3nWB9HSL_Q6JBR288aFl0HKVQUx1-Dd_pCYMvilxbMMtMV06fP0H_PpdzG3cZXmauDzIcXANO0bBpdXW49wGS7vqwRReo07Igo0Yz0sB7BkG62jmBaqARlxSoEGpOOZp3cvPw7YwoIN6G1fXzV03sz1p5FgiklFuprp-WON4azT4psrt61WsKdljF06d4WvEByjb5JYwowISg2wcQMKkLrUlNqCaOVz8WLWEp5C41lDnNEN9dAA9z8RVYggQwGh-mHC0BC7XlTJlsdUj1F9z8wRycSxEl8AjhO_FIGFUbBchlffNWVc6V1gV3eYJm6JR7YpRHXpSu7vVcipFqQWkc_wNVK9TqJA2ejHnCydKOs089AdWTYDzNp2ZDSxbVUN80LNcz4lC4MFQcbDwYij4sZtK6yG3-sOPFFmXt1DDcIE-wiT5T6jIk5zikqfjT4XIJd1swp0RaMc117Fo27bxV0Y-1MZxcB2EwWCtzMkamuyQvVCm_6owhy6ejc2cBEmQyPoA0t5myFpCnO3OWAhHt5O5RKr3y1PcanYEHsz9CgdRaTvFNpGJAr3qgGCIjQlgng-7xjB_Y9DnZcdnydnHLTdPsBRVTkYB8NZerS9tQwcpXP9kTZYFj6Khrd1iy8W_88GkkSSg05GI1E" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d62994becf.mp4?token=octFfi7WEZj4MfoNf0gUfvmJnbEOE3nWB9HSL_Q6JBR288aFl0HKVQUx1-Dd_pCYMvilxbMMtMV06fP0H_PpdzG3cZXmauDzIcXANO0bBpdXW49wGS7vqwRReo07Igo0Yz0sB7BkG62jmBaqARlxSoEGpOOZp3cvPw7YwoIN6G1fXzV03sz1p5FgiklFuprp-WON4azT4psrt61WsKdljF06d4WvEByjb5JYwowISg2wcQMKkLrUlNqCaOVz8WLWEp5C41lDnNEN9dAA9z8RVYggQwGh-mHC0BC7XlTJlsdUj1F9z8wRycSxEl8AjhO_FIGFUbBchlffNWVc6V1gV3eYJm6JR7YpRHXpSu7vVcipFqQWkc_wNVK9TqJA2ejHnCydKOs089AdWTYDzNp2ZDSxbVUN80LNcz4lC4MFQcbDwYij4sZtK6yG3-sOPFFmXt1DDcIE-wiT5T6jIk5zikqfjT4XIJd1swp0RaMc117Fo27bxV0Y-1MZxcB2EwWCtzMkamuyQvVCm_6owhy6ejc2cBEmQyPoA0t5myFpCnO3OWAhHt5O5RKr3y1PcanYEHsz9CgdRaTvFNpGJAr3qgGCIjQlgng-7xjB_Y9DnZcdnydnHLTdPsBRVTkYB8NZerS9tQwcpXP9kTZYFj6Khrd1iy8W_88GkkSSg05GI1E" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
🌟
قتل ترامب في أعناقنا.. الحشود الغفيرة في مصلى طهران تهتف للثأر من قتلة الإمام الشهيد.</div>
<div class="tg-footer">👁️ 3.34K · <a href="https://t.me/naya_foriraq/81012" target="_blank">📅 07:38 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81011">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e97e131c24.mp4?token=YdIOQSAgnoEtIMrVLOlXyQST691JPYCQan6vB_torGJA1EZ5pGxMlviHglgi3xp90rzaB3SgFJt48lYcl4wTufM8_gkH-OcMgVjmPE2tDlK_368cCTvBWFYtncB2bPITYpu7gbLtORUhLKlVXOYcW00xzyrPOdxYQ5bg_u6RuVM37hjHZjZkJjIVMUhnDYasdR0f-JPr5S5XpImVHby_UkJ5Qh0xpJcuLALn6Uc1nAYPNVaRfdNpOwyOdhtop4a7iT0yY7WtjA5phuZi3PhFxJfn26DvBrt-N7QJutJoxMmW0JK1WnnVdBBp8RhB2vgdb1MxkzUbDNfY3KQqoKAv8DaCGBS1TkttGfRgOTB7fjdIbiJKansqZU2Bo8JxIw8_4r3GkO61zZOlW4S4mlBWbgVhfRNnRKTf57U36XbDWqbUIoFz-B2HUevGO5xJH78BYBxdyasHbU0_jJfzLEZyrjiNl8j5pdKaetIsu0zXtUwtbNi2BKo_PKJu5M0HxKn2ScoLqJyEivqiIfQ0aZ4eKV_LNqUdXR_1NbJF-ilkH0GeZUZEupPuwBaXfPipXvLZGIzIwdAwSuEHtCQrHN4h-tyh4cbRfsAHCKx1u59HnefsEo7DiS0XEhATU4RdrCG16kyq-wzkWDxZHyLtrLVQp14T5nTI5PVT3yFuonFO-HE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e97e131c24.mp4?token=YdIOQSAgnoEtIMrVLOlXyQST691JPYCQan6vB_torGJA1EZ5pGxMlviHglgi3xp90rzaB3SgFJt48lYcl4wTufM8_gkH-OcMgVjmPE2tDlK_368cCTvBWFYtncB2bPITYpu7gbLtORUhLKlVXOYcW00xzyrPOdxYQ5bg_u6RuVM37hjHZjZkJjIVMUhnDYasdR0f-JPr5S5XpImVHby_UkJ5Qh0xpJcuLALn6Uc1nAYPNVaRfdNpOwyOdhtop4a7iT0yY7WtjA5phuZi3PhFxJfn26DvBrt-N7QJutJoxMmW0JK1WnnVdBBp8RhB2vgdb1MxkzUbDNfY3KQqoKAv8DaCGBS1TkttGfRgOTB7fjdIbiJKansqZU2Bo8JxIw8_4r3GkO61zZOlW4S4mlBWbgVhfRNnRKTf57U36XbDWqbUIoFz-B2HUevGO5xJH78BYBxdyasHbU0_jJfzLEZyrjiNl8j5pdKaetIsu0zXtUwtbNi2BKo_PKJu5M0HxKn2ScoLqJyEivqiIfQ0aZ4eKV_LNqUdXR_1NbJF-ilkH0GeZUZEupPuwBaXfPipXvLZGIzIwdAwSuEHtCQrHN4h-tyh4cbRfsAHCKx1u59HnefsEo7DiS0XEhATU4RdrCG16kyq-wzkWDxZHyLtrLVQp14T5nTI5PVT3yFuonFO-HE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">من مصلى الإمام الخميني.. "أين نصر الله أينَ ليتَهُ في الحاضرين".</div>
<div class="tg-footer">👁️ 4.28K · <a href="https://t.me/naya_foriraq/81011" target="_blank">📅 07:03 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81010">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">من مصلى الإمام الخميني.. "أين نصر الله أينَ ليتَهُ في الحاضرين".</div>
<div class="tg-footer">👁️ 4.23K · <a href="https://t.me/naya_foriraq/81010" target="_blank">📅 06:57 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81009">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/15b4c155b1.mp4?token=KPW4DCJL5Y5Is__QR7WDnibSfR8ygaMlqIzH4vkdAX1Dc5xpctBY_kJRnqdLhC8PmtJH0hBLTFJdBLb30bXPCOODADxJP3hcJ4le9prxMV0lZSynuZPQkenEfZ9PJpxAKVXV-WIx4uvmOYXiOT-8S-24IOeOpZ6J8v-O2neoiaj6KbKY8Z5D2vKSgi5q2mjxGb2nclmqil7fauXivJeeQ05FMkl5SwrsrmtSLJQMNd8SqCi0dfF_RUfgnhM7TZme9KXPzFeUtpQkOOwveK-vOXh0357aE4D_pu12eWN0YpipEVItHG753gVsqluM5ANqR2v-cH2UR1Hw3YdnOAoy9YKJUU8AC2Q8Up-vYy6UKlhPB1hv9OV7tlhkPWaAIN3Z3g0XNP1nbuCrqoW8wvJWuOPv8xaiHwS1NF6l7E8LiUfmipEJZ6O_66vPS33-ekaNWnf4CkFJpBlaG3zl5kDIBilMIKJ7x2WTEPJZ2XEdZl3QYuR60qNxVOGW51Rfh7lwwCp6_c8HAkvAi0yckxClhqBJsf-H6X2IH6RfgYIZUU06WX6_XfZ6EyDseymi2PBr5TMu098Jl1rAFPopr_Tyhz6jEwLuXo0speSQJRNRqJhf9mlxL3GXL_re7JbKVQXkxE_wip9afZpx5Kj0qUFGw25M6u3F5mhhZBiwhvBqDOo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/15b4c155b1.mp4?token=KPW4DCJL5Y5Is__QR7WDnibSfR8ygaMlqIzH4vkdAX1Dc5xpctBY_kJRnqdLhC8PmtJH0hBLTFJdBLb30bXPCOODADxJP3hcJ4le9prxMV0lZSynuZPQkenEfZ9PJpxAKVXV-WIx4uvmOYXiOT-8S-24IOeOpZ6J8v-O2neoiaj6KbKY8Z5D2vKSgi5q2mjxGb2nclmqil7fauXivJeeQ05FMkl5SwrsrmtSLJQMNd8SqCi0dfF_RUfgnhM7TZme9KXPzFeUtpQkOOwveK-vOXh0357aE4D_pu12eWN0YpipEVItHG753gVsqluM5ANqR2v-cH2UR1Hw3YdnOAoy9YKJUU8AC2Q8Up-vYy6UKlhPB1hv9OV7tlhkPWaAIN3Z3g0XNP1nbuCrqoW8wvJWuOPv8xaiHwS1NF6l7E8LiUfmipEJZ6O_66vPS33-ekaNWnf4CkFJpBlaG3zl5kDIBilMIKJ7x2WTEPJZ2XEdZl3QYuR60qNxVOGW51Rfh7lwwCp6_c8HAkvAi0yckxClhqBJsf-H6X2IH6RfgYIZUU06WX6_XfZ6EyDseymi2PBr5TMu098Jl1rAFPopr_Tyhz6jEwLuXo0speSQJRNRqJhf9mlxL3GXL_re7JbKVQXkxE_wip9afZpx5Kj0qUFGw25M6u3F5mhhZBiwhvBqDOo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">إِنَّا لَا نَعْلَمُ مِنْهُ إِلَّا خَیْراً</div>
<div class="tg-footer">👁️ 4.47K · <a href="https://t.me/naya_foriraq/81009" target="_blank">📅 06:49 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81008">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6862495e50.mp4?token=YUpijnoIp2YFeiKa5diy2QkDUJf3TRgVYXOQ2Jp3s0IDaKJcKHxaKLWwmNWBso1O2jYpRtvgZiuh365yCFUSIkFNmblnUL40qd9Af98tPsD0AWLH99sheBgXz7UOtWR667c_TQo_7kZTVEKDkjTxqWZEW61XGuSwRpPcpgqlUqrr_kBzxQ9HaXX33CGNeZ_bLo_87nP0bT4bth4m2gSGerOso0g3VKPPNjRwDlBQ2zOW0bgi-pDJ__mx6zekghuIyTLmNP5TYIGtwlRnl9yEwn2wBWUDqsGt-phN4k80SR1m1xwfAAlPlDf6g89EXTad-DCPSizPlj0aCogZ_s-Yhw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6862495e50.mp4?token=YUpijnoIp2YFeiKa5diy2QkDUJf3TRgVYXOQ2Jp3s0IDaKJcKHxaKLWwmNWBso1O2jYpRtvgZiuh365yCFUSIkFNmblnUL40qd9Af98tPsD0AWLH99sheBgXz7UOtWR667c_TQo_7kZTVEKDkjTxqWZEW61XGuSwRpPcpgqlUqrr_kBzxQ9HaXX33CGNeZ_bLo_87nP0bT4bth4m2gSGerOso0g3VKPPNjRwDlBQ2zOW0bgi-pDJ__mx6zekghuIyTLmNP5TYIGtwlRnl9yEwn2wBWUDqsGt-phN4k80SR1m1xwfAAlPlDf6g89EXTad-DCPSizPlj0aCogZ_s-Yhw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
هتافات "الموت لأمريكا" باللغة الإنجليزية في مترو مصلى طهران.</div>
<div class="tg-footer">👁️ 4.57K · <a href="https://t.me/naya_foriraq/81008" target="_blank">📅 06:38 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81007">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e07ba323bb.mp4?token=EfbX6pk166sgV2ZPD3R15aUdWdlhznWasvbdq9ZrWes_ebzTGtfYTO-FOOpI8ARzS2xZw8nCoLqJZX__0e5hVdLE-BYXg2cfh7sipYbia-a1mbhGcgOkNUJ1nB-1l33fTieHGi8JK7AqQC9HNK02K4uDAzItQk-EyGGs4371XdRnGUzzBh2OZhjLokUDhOw_G0uXrkHLL8AgNnMTiCv0MdKs-S-kEo0fVOVVyrMndPgEFUFuD0MbTU8WDRm3rB9BlbUi22mVzQlGK1zVlRs2J-Pt3ahvG-6OJereZS8Y07eFWmlOZGk4Xe1oAYK7s8aTnZSTo7sO5v2fsxkXx4zhHw-akL_mGz8hGmb25pvJ3ybRkL1AJmvOSyflXiooRxRNAenPQCZ656lklLHYORiSbzMOoKoQbeD8OXkh-OJpRzzAUrMkTAkTItrQOu41CGsMZugIvqhhupj1Mvm9QfQDnQmcYQveU9eKF8iMDzd-wUoVRKWIvJK1VOTooF1ibEYxI44VBfQaWeoFOBjCz5wfxgrkGN-uovtgtRFF0tu6mdmR6b3ujbMF47BgN36VddHrTXgBM14OOniqCMJ3Gfs2vCvis41GdAbThjqXP3MSHRP5xZLJ0Ss3ofxgXx5vMYGUXfst7tl_xaGTsmOg7VSO5ne3seZT6PVv9cvp-QBOC4k" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e07ba323bb.mp4?token=EfbX6pk166sgV2ZPD3R15aUdWdlhznWasvbdq9ZrWes_ebzTGtfYTO-FOOpI8ARzS2xZw8nCoLqJZX__0e5hVdLE-BYXg2cfh7sipYbia-a1mbhGcgOkNUJ1nB-1l33fTieHGi8JK7AqQC9HNK02K4uDAzItQk-EyGGs4371XdRnGUzzBh2OZhjLokUDhOw_G0uXrkHLL8AgNnMTiCv0MdKs-S-kEo0fVOVVyrMndPgEFUFuD0MbTU8WDRm3rB9BlbUi22mVzQlGK1zVlRs2J-Pt3ahvG-6OJereZS8Y07eFWmlOZGk4Xe1oAYK7s8aTnZSTo7sO5v2fsxkXx4zhHw-akL_mGz8hGmb25pvJ3ybRkL1AJmvOSyflXiooRxRNAenPQCZ656lklLHYORiSbzMOoKoQbeD8OXkh-OJpRzzAUrMkTAkTItrQOu41CGsMZugIvqhhupj1Mvm9QfQDnQmcYQveU9eKF8iMDzd-wUoVRKWIvJK1VOTooF1ibEYxI44VBfQaWeoFOBjCz5wfxgrkGN-uovtgtRFF0tu6mdmR6b3ujbMF47BgN36VddHrTXgBM14OOniqCMJ3Gfs2vCvis41GdAbThjqXP3MSHRP5xZLJ0Ss3ofxgXx5vMYGUXfst7tl_xaGTsmOg7VSO5ne3seZT6PVv9cvp-QBOC4k" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لبيك ياحسين</div>
<div class="tg-footer">👁️ 5K · <a href="https://t.me/naya_foriraq/81007" target="_blank">📅 06:21 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81005">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gFU8rlgySUcimdcx2cyD3wSAElAw-5RXeahi51BJ7jHhzIGiDQ06FBk-KW8hj-G1vQUieksZuMXZmlW5unMpqKz59Yd92SCANZIfu-NeTsCtIEaAxBMu9kHweHKe1f0XD-939fgVRcRP4StT64Pd-FRPvLJIM4WQXhqQ7Q-XofKN1ibAiE-EanwRVs7SS6uI92Nn1eg58xvM3aOYluGdXDviEafDtTkiYK4tavto-02QrRx8ONVPUlE0JmtQbLqddhZNNe_S1pyP9EELyfFEP7xoHy6zUGRyzkdKS6XpTJWAAbvSVrH-xxFUrP9Pc_jjpEM85wd0z8-ca9hxDZpiXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AJw0YOXsGySK70ob55jjYMHrQRlVyr7NdteVlWVMDrFBaQQyviL9BV_t1vc7hDX3qND7cQQpJKUAf6p-UVTSSZEZYhB4TI_2jQHFBX8WBj7WZLjEB_TVe2UA-A_wuoM7oKOB48zuezu6GiC_s9VlYGJ1fY1-CnKVYT2PwwRkXtcGRkBAVobE9001SZmV8hhNkuDBHVIdKmg19iYQfw4Ob_yW1War8AKc3nquTp68roxdywejwPLT3AYW2yw6zZPyFCths82fVBf9zShdY-7ZijdOGOlRN-YpIGiUZ7Yo3jFpZruOv0KSSDgPTtbyYPhlx3ashWmUXjXUhJuXLkFgOg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پرچم‌ سرخ انتقام تا نابودی اسرائیل برافراشته می‌ماند.</div>
<div class="tg-footer">👁️ 5.39K · <a href="https://t.me/naya_foriraq/81005" target="_blank">📅 06:07 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81004">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a4ca7ed0e3.mp4?token=o4rIebDQ1ynxdbq3IFbhj-UjVXjxnsobsUUH0wKpb576ditmhd4TGjkWubBN606k_ropnFau-1QZQuhVbaYSqIGep_HCdh5rUr7sGHQWebv3u2os0HeojPpaYRUXUzP8hPQukVFWlwGNv3tiFDaMgbENrl0BPcq7-4LMfz-w67QpHd9iguFp7r8gZ7BwRuYMVYLtnubMTko1WilSGvPVNNvZ6CsDlb2K-qtZNZ0MSQ-TNblTjLaH5tqbXMAjsk2DSO2Fe0qf8BZxJLVwssX2fGdbJ3huuNTkvBs_Q2IIwAPqCX7mAJrzncqgHBO-QOYOLET--x0a3y30dBhSYVXG1pdWGWKSzV2_Y7dAiNKXvQFGQ33LqIT1o29oVLYVyKsdhsVyLQgIbHoeWC7igMyt4YlUAaoTNQENBQacD2C1MXwieQsJ_DEnJIeQMEYdGl3qXBCIYj43-DiotJmaif5-W5GSqGYRFt7tFTNFTMbdbr-RT0YOKMoHIdUuFJJWr6c9OOCk-TTLkwrEUACKbtbdENtltjDX0MIT-vDFm5rMKo64nAWJsl0z3pJFFEge6bF13f8VlrW-Gj4SZaSH4XSmS5nhY7fp4QlPQl5AFl8NNKoijQ6fNLrDFFGYv2MNblp-Z00mRT8c24yPpPu8prtV1fH_eEu8HZsDQfHfSrmE4Ts" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a4ca7ed0e3.mp4?token=o4rIebDQ1ynxdbq3IFbhj-UjVXjxnsobsUUH0wKpb576ditmhd4TGjkWubBN606k_ropnFau-1QZQuhVbaYSqIGep_HCdh5rUr7sGHQWebv3u2os0HeojPpaYRUXUzP8hPQukVFWlwGNv3tiFDaMgbENrl0BPcq7-4LMfz-w67QpHd9iguFp7r8gZ7BwRuYMVYLtnubMTko1WilSGvPVNNvZ6CsDlb2K-qtZNZ0MSQ-TNblTjLaH5tqbXMAjsk2DSO2Fe0qf8BZxJLVwssX2fGdbJ3huuNTkvBs_Q2IIwAPqCX7mAJrzncqgHBO-QOYOLET--x0a3y30dBhSYVXG1pdWGWKSzV2_Y7dAiNKXvQFGQ33LqIT1o29oVLYVyKsdhsVyLQgIbHoeWC7igMyt4YlUAaoTNQENBQacD2C1MXwieQsJ_DEnJIeQMEYdGl3qXBCIYj43-DiotJmaif5-W5GSqGYRFt7tFTNFTMbdbr-RT0YOKMoHIdUuFJJWr6c9OOCk-TTLkwrEUACKbtbdENtltjDX0MIT-vDFm5rMKo64nAWJsl0z3pJFFEge6bF13f8VlrW-Gj4SZaSH4XSmS5nhY7fp4QlPQl5AFl8NNKoijQ6fNLrDFFGYv2MNblp-Z00mRT8c24yPpPu8prtV1fH_eEu8HZsDQfHfSrmE4Ts" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پرچم‌ سرخ انتقام تا نابودی اسرائیل برافراشته می‌ماند.</div>
<div class="tg-footer">👁️ 5.43K · <a href="https://t.me/naya_foriraq/81004" target="_blank">📅 05:36 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81003">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e165ad798d.mp4?token=fnMp15fLCURm23UOMGmOzVtf_ahIDeZHtpnV9tMY-b0eJtBdcNlTW5pdJlh1VQ42g9jx2QQgm6RwGk2TjChNonfCGJ4lAgMTU_zQkg8q4BNhXDNn8NL_bkYWu8dJUUrfkEnHbIZIBhnfTBMvFv8hj9lprsVLkoUFvbGhoRwjP5P4siRdJUyo4din0rcmrju4LGnE6LC9h-wBiKEx_ToqgXql0FCi9LBKTnRoeeFqQfFMsoF7DQ2GLucjM09PyV0hMrBArb-rj-f-SeZibaswVFcDBLJboXDM_Wc7YcU5x6k3DiLMp-qYsv0OzeOB6tBVVAdPTKtKCgIdqL_atPHEvw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e165ad798d.mp4?token=fnMp15fLCURm23UOMGmOzVtf_ahIDeZHtpnV9tMY-b0eJtBdcNlTW5pdJlh1VQ42g9jx2QQgm6RwGk2TjChNonfCGJ4lAgMTU_zQkg8q4BNhXDNn8NL_bkYWu8dJUUrfkEnHbIZIBhnfTBMvFv8hj9lprsVLkoUFvbGhoRwjP5P4siRdJUyo4din0rcmrju4LGnE6LC9h-wBiKEx_ToqgXql0FCi9LBKTnRoeeFqQfFMsoF7DQ2GLucjM09PyV0hMrBArb-rj-f-SeZibaswVFcDBLJboXDM_Wc7YcU5x6k3DiLMp-qYsv0OzeOB6tBVVAdPTKtKCgIdqL_atPHEvw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">أجواء مليئة بالحزن تعم مصلى الإمام الخميني قُبيل إقامة صلاة الجنازة على جثمان الإمام الشهيد (رضوان الله عليه).</div>
<div class="tg-footer">👁️ 5.64K · <a href="https://t.me/naya_foriraq/81003" target="_blank">📅 05:34 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81002">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d616b39370.mp4?token=NB9KaxMOJrXzUf_bE-1eW__PO-FulwJcaxgM8qGu6ANIBxDzH482r7T8MHSBdqtIeUjXJj1PfZHXcDGssq2DUbE8cacNqddxr1_7Z_eUFmXG0cOWHJLiQHyc51Dll8g00gxg0q3LSuKDXoBW8d50XZhCWuvv3m_7RhZKMK4A3QQ0-Uf5-iOFponPDl3WaKzk2E1cjRRIMMepIGEVms5ygOef559UrbIOHfFqWdTRsZ_7UFRfGa-p_94D7MCMVtZP4kAlfwTkOgU7TfsjYsdhC6hAHB2pEZqGjR8jiGrH993qwybPE82MmBv9aUN9rKmlKK5MZAjpMUVPkjcsPJ2N8XV4DX0gzcf3su6cohUqprN3FgEHqZLslNxWyPrdL2zKaUGD6SIpiuJTQcPZLwIEaIbHoG2xYlkPPMIp4pPMpjN0DVCQslNV-Cd2v26nmZfQkqAaOPRnsPKkY7JLJlHAvKmmEZDBbHfElxi7KeXDX_tHc9shP09_Utdi7Yf9wqcK4ky_fzqmTeegXDSAG0a2MJAlAaOc_sRiVOW6b_sxze82lSh-hnVY6YRUjEkvEamMZIKwB0iibb3Yda4cbyuy3oUGNuTsfl1l0D5qD_9tX43IyG264jhWJBqJrEHl2OWY1BgUNMkR4l5IYJhURTAsjPobDJkUJHqh0E4Fh3Yxbwk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d616b39370.mp4?token=NB9KaxMOJrXzUf_bE-1eW__PO-FulwJcaxgM8qGu6ANIBxDzH482r7T8MHSBdqtIeUjXJj1PfZHXcDGssq2DUbE8cacNqddxr1_7Z_eUFmXG0cOWHJLiQHyc51Dll8g00gxg0q3LSuKDXoBW8d50XZhCWuvv3m_7RhZKMK4A3QQ0-Uf5-iOFponPDl3WaKzk2E1cjRRIMMepIGEVms5ygOef559UrbIOHfFqWdTRsZ_7UFRfGa-p_94D7MCMVtZP4kAlfwTkOgU7TfsjYsdhC6hAHB2pEZqGjR8jiGrH993qwybPE82MmBv9aUN9rKmlKK5MZAjpMUVPkjcsPJ2N8XV4DX0gzcf3su6cohUqprN3FgEHqZLslNxWyPrdL2zKaUGD6SIpiuJTQcPZLwIEaIbHoG2xYlkPPMIp4pPMpjN0DVCQslNV-Cd2v26nmZfQkqAaOPRnsPKkY7JLJlHAvKmmEZDBbHfElxi7KeXDX_tHc9shP09_Utdi7Yf9wqcK4ky_fzqmTeegXDSAG0a2MJAlAaOc_sRiVOW6b_sxze82lSh-hnVY6YRUjEkvEamMZIKwB0iibb3Yda4cbyuy3oUGNuTsfl1l0D5qD_9tX43IyG264jhWJBqJrEHl2OWY1BgUNMkR4l5IYJhURTAsjPobDJkUJHqh0E4Fh3Yxbwk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
🇮🇶
بعدسة نايا | المواكب العراقية في طهران تستنفر لخدمة مشيعي قائد الثورة الشهيد</div>
<div class="tg-footer">👁️ 5.62K · <a href="https://t.me/naya_foriraq/81002" target="_blank">📅 05:21 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81001">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd7aa532cd.mp4?token=Asa23_131JWVg4RnrVo_zHJwWsILHfJ4_5fPmczO7m99bK1Bi71j6D9X4Ux8Nhj5seqlN9eJ6Pb3tTcZAUq2mMHLJdBoV8XYB2LELe5r4Mm33v2xxcjbVfO9A70jn37X0RqGMGARXzt5atKhzde5DseKIl_Fdis5MQi-pNpgJz5wLQ03pAG9_LEwENr4Uz7q2ieHTLFb7okc2hW3eLulFWZDL_E9QxNxDYss-XbvOey-eqbsJdJixwD5Q7_dhEoJ2sQRV6hv9pLRcue1BfAaTUcJc2FF6wqvE2iPAhIia2YkoIy6DINbvSfwmVV_Fd_7E3A7X7dZ9XNge7ls990SSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd7aa532cd.mp4?token=Asa23_131JWVg4RnrVo_zHJwWsILHfJ4_5fPmczO7m99bK1Bi71j6D9X4Ux8Nhj5seqlN9eJ6Pb3tTcZAUq2mMHLJdBoV8XYB2LELe5r4Mm33v2xxcjbVfO9A70jn37X0RqGMGARXzt5atKhzde5DseKIl_Fdis5MQi-pNpgJz5wLQ03pAG9_LEwENr4Uz7q2ieHTLFb7okc2hW3eLulFWZDL_E9QxNxDYss-XbvOey-eqbsJdJixwD5Q7_dhEoJ2sQRV6hv9pLRcue1BfAaTUcJc2FF6wqvE2iPAhIia2YkoIy6DINbvSfwmVV_Fd_7E3A7X7dZ9XNge7ls990SSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
🇮🇶
بعدسة نايا |
المواكب العراقية في طهران تستنفر لخدمة مشيعي قائد الثورة الشهيد</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/naya_foriraq/81001" target="_blank">📅 01:44 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81000">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2eda2a08b1.mp4?token=KuYU4_KsFrS_FC1wC-9pTMS1UEU6iEj2Dg1rMnFU3n1B3uW8w74mH9CeAxVBFX_zmAqimM2RspHCBfvtQqkRr_NUaCJAOQ9v5R2UpKiyYb33-G7zfInrmi2pgPGfZzkrLpB_E6NGVRtK1q7YLX2WdlTYNnLhg1F1d__SpxDhJICSd8TaUToHYWg1LAz8ttSIJniWl3m6RTueAG5WCk632pweIhYHsgZcdbwRa5Sluc8EbrdZZ6yIp-cBNK6-0cxx4zbMrU8Zj9RXeMzptH99_rkqQ_pmdQmjGcntNC8M9_a_GoGeppZf7jm7dFrUPlzpB9fWObSGkYSzVHjY35SG2oERG5Wz8MRhI71tW5jseFbKWcVFYriQOzeITyTwCLXf1l4qPf3ykol6XpMI6Ypz_qrRndytPTkOeB6MnezxpA9pw260mkRK8P8S-v06Qhw8ptWfRKoixr7_bgTyqz_OL--Ehqzrd5kRzy5zh3W1pMli4_w9UEwSAzS8CputAeLVabQx99wOz7XyztNcajlUMwMpSJTzwUWVMpOqmpLf7ZiKOxbldIp0IU1-zM3YuTFOywh-MmD29fFbonW58M1SobcDdGiEsmI7YnJS94rLsnHA3ltHKCkX3zdYQciRAu4oYnsmHKl02xmhStFIvyq3kdlJsx2eqD7eLt9r-GuDC0s" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2eda2a08b1.mp4?token=KuYU4_KsFrS_FC1wC-9pTMS1UEU6iEj2Dg1rMnFU3n1B3uW8w74mH9CeAxVBFX_zmAqimM2RspHCBfvtQqkRr_NUaCJAOQ9v5R2UpKiyYb33-G7zfInrmi2pgPGfZzkrLpB_E6NGVRtK1q7YLX2WdlTYNnLhg1F1d__SpxDhJICSd8TaUToHYWg1LAz8ttSIJniWl3m6RTueAG5WCk632pweIhYHsgZcdbwRa5Sluc8EbrdZZ6yIp-cBNK6-0cxx4zbMrU8Zj9RXeMzptH99_rkqQ_pmdQmjGcntNC8M9_a_GoGeppZf7jm7dFrUPlzpB9fWObSGkYSzVHjY35SG2oERG5Wz8MRhI71tW5jseFbKWcVFYriQOzeITyTwCLXf1l4qPf3ykol6XpMI6Ypz_qrRndytPTkOeB6MnezxpA9pw260mkRK8P8S-v06Qhw8ptWfRKoixr7_bgTyqz_OL--Ehqzrd5kRzy5zh3W1pMli4_w9UEwSAzS8CputAeLVabQx99wOz7XyztNcajlUMwMpSJTzwUWVMpOqmpLf7ZiKOxbldIp0IU1-zM3YuTFOywh-MmD29fFbonW58M1SobcDdGiEsmI7YnJS94rLsnHA3ltHKCkX3zdYQciRAu4oYnsmHKl02xmhStFIvyq3kdlJsx2eqD7eLt9r-GuDC0s" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
بعدسة نايا | حشود غفيرة تتوافد عبر المترو باتجاه مصلى الإمام الخميني للمشاركة في مراسم تشييع السيّد الولي</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/naya_foriraq/81000" target="_blank">📅 01:37 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80999">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a596566298.mp4?token=JgOdpAWveN89A_VLnUvtPE6dXVzYu2D_1U4IOJQDWQdGwKs1syJoXxOx3W6nYnkwYGFZ6f7-SUpJWtiH8OM-xmgTZHuLV28koKS3P4BaOEROu2-Hf3e4INMWrgBsiiRJ4i2esnHSmGjdhM3ujqwJs2_Gh13-RmlhTJYfA0phC9Pd7gzCOD7adOk7DtVfdyIzF8OJnCdi7MlC5t78HEwoqJjn1rdurnFpVrnNl2a34EVhUDnmoFv3iw21DYoLsg6x1ftPVi6CuxwJh7UNlbG4KQQ3NEmRaHAJerpC82rCg6PtpaOUY5UOXTZjOnloTzqyoUnJV4qj5ATPRxb0Xni_Wg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a596566298.mp4?token=JgOdpAWveN89A_VLnUvtPE6dXVzYu2D_1U4IOJQDWQdGwKs1syJoXxOx3W6nYnkwYGFZ6f7-SUpJWtiH8OM-xmgTZHuLV28koKS3P4BaOEROu2-Hf3e4INMWrgBsiiRJ4i2esnHSmGjdhM3ujqwJs2_Gh13-RmlhTJYfA0phC9Pd7gzCOD7adOk7DtVfdyIzF8OJnCdi7MlC5t78HEwoqJjn1rdurnFpVrnNl2a34EVhUDnmoFv3iw21DYoLsg6x1ftPVi6CuxwJh7UNlbG4KQQ3NEmRaHAJerpC82rCg6PtpaOUY5UOXTZjOnloTzqyoUnJV4qj5ATPRxb0Xni_Wg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇾
"ياعلي مدد"..
توتر امني تشهده مدينة السلمية في ريف حماه الشرقي بعد قيام عصابات الجولاني باختطاف عدد من ابناء الطائفة العلوية.</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/naya_foriraq/80999" target="_blank">📅 01:11 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80995">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I5noxvQSX4FYhTFdcyzJAfNsI1-hwIAYKOhKg03u3tsW-0R9s4bEl0e7bR7w70jwA7yuYqenDISLE5vFSk3YS6QZ_5aQKWF4UmUU2zmfbxNTpNs68YZJq0TvYmgQ64qUsnrZWPbxTxYcW4OdD1RJjHghnEvAoTLlR2cQGEWZK0CfGeEoNtLrFE8zvAaWPCyZ505bYQfLGWbJMOOfsZtpCDDtmfJ1YC-wvdinp3d9Sxc578-tS9v0ZiZ9WOAC9vBq65YozrxSubHuPuH1pPUUryBHd-N2_D1x9OgC2TH8N5Sr8Mqg6LuoWLs8ge24r0X_ocY7MdEtiRGElPS5tNc7cA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/19ac2ad5e5.mp4?token=LuW-9ZrT0ohE-wwGQ4sMxGGBFe2UZWeZE4qCAsNuCu8XovnVXNY5zE1kBuhJw0QEz-e3iH8--yk4Pp6hoDjLYynwFY3Q3YY1M9kuLlaubm_uy6HC14XuhFWODfXcFqYgn82lkdocJDIGaSWUED3-fuxAo92edzo3FQKcq4ysi6mx-KeUZhok1jKmWzkgdJp0P0ZJxoL1u9NlTaMzdZErtLEqMeYy5A_oj83Dj1nPnn0cflanyPhMd8bfJSjWkW6uwMLXGdFhwOhFo1Nsmw47AoCmUH0x1IOzVYfpBkOkvUFLRpqfo-9juqb1sLkqLVgtqLJiu0rxDYbUS-4Q7gTYig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/19ac2ad5e5.mp4?token=LuW-9ZrT0ohE-wwGQ4sMxGGBFe2UZWeZE4qCAsNuCu8XovnVXNY5zE1kBuhJw0QEz-e3iH8--yk4Pp6hoDjLYynwFY3Q3YY1M9kuLlaubm_uy6HC14XuhFWODfXcFqYgn82lkdocJDIGaSWUED3-fuxAo92edzo3FQKcq4ysi6mx-KeUZhok1jKmWzkgdJp0P0ZJxoL1u9NlTaMzdZErtLEqMeYy5A_oj83Dj1nPnn0cflanyPhMd8bfJSjWkW6uwMLXGdFhwOhFo1Nsmw47AoCmUH0x1IOzVYfpBkOkvUFLRpqfo-9juqb1sLkqLVgtqLJiu0rxDYbUS-4Q7gTYig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
بعدسة نايا |
حشود غفيرة تتوافد عبر المترو باتجاه مصلى الإمام الخميني للمشاركة في مراسم تشييع السيّد الولي</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/naya_foriraq/80995" target="_blank">📅 00:32 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80994">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c808640a81.mp4?token=XHE7XWMv8wkovYNbVcKgvP38bH20spcGm97cBPLYypBpS3XMV6UiiWR4m4AzAHy7x2in60Bu_Eia9Y_0fj3Azyj3qedNELOoiYEakan6H1xflrvnDDxP6R8IHeeusc4oBH55PbhgygcLvdHf6wvkHdmvt27-x1f-FJEEzHVOJF_lNIQ9ud1evhxf4Dsw0tzOagWVbR__bfMTHn5uuux5lgvp5NDvCmqkaZqUc0tvuhwPl_zjD_CE8OVSieLEYtDb6baW6z42IeFldBU_y9-M4n6BxrEc6fH-E8-lo4UiAaKyDEG3iAErP8judWgw7pkWPUFKi3WSvVq84mrNmoxhuw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c808640a81.mp4?token=XHE7XWMv8wkovYNbVcKgvP38bH20spcGm97cBPLYypBpS3XMV6UiiWR4m4AzAHy7x2in60Bu_Eia9Y_0fj3Azyj3qedNELOoiYEakan6H1xflrvnDDxP6R8IHeeusc4oBH55PbhgygcLvdHf6wvkHdmvt27-x1f-FJEEzHVOJF_lNIQ9ud1evhxf4Dsw0tzOagWVbR__bfMTHn5uuux5lgvp5NDvCmqkaZqUc0tvuhwPl_zjD_CE8OVSieLEYtDb6baW6z42IeFldBU_y9-M4n6BxrEc6fH-E8-lo4UiAaKyDEG3iAErP8judWgw7pkWPUFKi3WSvVq84mrNmoxhuw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇾🇪
وفود جماهيرية من حركة انصار الله اليمنية تشارك في مراسم توديع قائد الثورة الشهيد</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/naya_foriraq/80994" target="_blank">📅 00:27 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80993">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e739239b93.mp4?token=KyXk9ioEZ8ijZlFlWmcu7ePlsygdS1OhxYyTWgbIqiYbwpkxIu_lq-IhMigmrBFYQ-gytacAvy1MslZDrGk4VUI5PCyElfevX-s7TbT4KSsWRxxBZeRaDQ_e74NODIHSFvnq6eJwhu0k2lC-BCf0nbG7lu5zizMlxE4nlmiVZXXub5E1Cras9hv2JOlR96ojT-jt6N7EIKkkt_gvSgsAV5-EQiV0Uzt_DgKG01XXwUb3EJZSODClzYL78eec67NX_lsj9SD_3M3Rn6qmi91hFmTrTuhnol2DTlzAE9jbvuEiMJQPjx4_klL_fgVmoe-zzHxisCkOVPAYz-cA_idz4zzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e739239b93.mp4?token=KyXk9ioEZ8ijZlFlWmcu7ePlsygdS1OhxYyTWgbIqiYbwpkxIu_lq-IhMigmrBFYQ-gytacAvy1MslZDrGk4VUI5PCyElfevX-s7TbT4KSsWRxxBZeRaDQ_e74NODIHSFvnq6eJwhu0k2lC-BCf0nbG7lu5zizMlxE4nlmiVZXXub5E1Cras9hv2JOlR96ojT-jt6N7EIKkkt_gvSgsAV5-EQiV0Uzt_DgKG01XXwUb3EJZSODClzYL78eec67NX_lsj9SD_3M3Rn6qmi91hFmTrTuhnol2DTlzAE9jbvuEiMJQPjx4_klL_fgVmoe-zzHxisCkOVPAYz-cA_idz4zzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فتح ابواب جديدة في مصلى الإمام الخميني بسبب توافد حشود غفيرة</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/naya_foriraq/80993" target="_blank">📅 00:19 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80991">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40d71ccc51.mp4?token=CWJNLzJZ9-PihTg7XiFXJD4Q9aMqOi4bGpMqNcE0tAAXQPH5u6LNA-wRWZTxBJP99pfxpUJshVanEq6gorlrJolgQo2SIInc6VY-39xNs2CNROv5Evp9-VQzfVjNwo3Wwcplzf5B1ZAbpjs21VvE0CAain2_HW_vJSoSl4Fpusn2pUfii7R7zLyZR5PERCVuQMzIT8PyD-CxzkXK9tkjfFRd8EaJzZaUtZ8qiveOrJL93L4-uu8hFoKy43Fl1p7lodIBqKvIOfKt-dlRrlR_Tqb0fB9ACRRtvyLSYegrHaucc8UZOIbMU_BR-JxlkcDCi67-7onkxfCW9b-Pgr8hlw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40d71ccc51.mp4?token=CWJNLzJZ9-PihTg7XiFXJD4Q9aMqOi4bGpMqNcE0tAAXQPH5u6LNA-wRWZTxBJP99pfxpUJshVanEq6gorlrJolgQo2SIInc6VY-39xNs2CNROv5Evp9-VQzfVjNwo3Wwcplzf5B1ZAbpjs21VvE0CAain2_HW_vJSoSl4Fpusn2pUfii7R7zLyZR5PERCVuQMzIT8PyD-CxzkXK9tkjfFRd8EaJzZaUtZ8qiveOrJL93L4-uu8hFoKy43Fl1p7lodIBqKvIOfKt-dlRrlR_Tqb0fB9ACRRtvyLSYegrHaucc8UZOIbMU_BR-JxlkcDCi67-7onkxfCW9b-Pgr8hlw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عصابات كردية تعتدي على العلم العراقي في محافظة اربيل بالتزامن مع قيام الجيش التركي بتعذيب شباب اكراد داخل الاقليم وتهجيره للمواطنين الاكراد من منازلهم وتجريفه للغابات واقامة المعسكرات.</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/naya_foriraq/80991" target="_blank">📅 00:03 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80990">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🌟
مجلس الوزراء العراقي يقرر إضافة (25) ألف برميل من النفط الخام إلى الاتفاقية العراقية الصينية وفتح حساب لها لضمان سد وتسديد الالتزامات المالية للجانب العراقي للمحافظة على موقف العراق الائتماني واستمرار تمويل المشروعات من الجانب الصيني</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/naya_foriraq/80990" target="_blank">📅 00:01 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80986">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B2Cc1gbAd8eboz-hkqBhQQOVJi2F29R4FIVqStPSHdC_AEUoxIlTOCY9PlbiD1mPZPzCHnBOLFpY2I7McsXeYbHA9yMaDWLsLsECjyK3Or5cvkc0asb9OS1ax_OkTeOwZZb7bGeIEH3BrF0tdmq5GB_K4wpMpZF-3F7F7fXxU4uOKS_ccl_XNaA7i5_jv-P_oCz70qtjQkqVIakinzLkXG2BYVfMD1joBHbkLFK0o1ZudqVOJq3YnrWD5wgi1WTjlwO1cubPyGl4jwfiu7V_2cc8enaiXHzi8KpZqLA247xmQD-QAuc2YsMG7kA0fdIt04DJSN4ntr_yzv1tRmYG_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8b91b0b8e.mp4?token=sv9Cv-bv7AhF2PiCesjgdEMJDMjevqajalWEpgvk83Qlkx3nSioHR88W0c-qiKib8EqGXhxsMGIfIYW4_NC_-lX5FKCfIlKLHx5CQHlFPE2J3Q-lmhghnuQ4Vav1Z8JGUq_MKmG9CaBIMQVmJUSPvYvpLCZv3DwU7VQMSB5npu-6rgSwLcP6FnQdXPR14WOQmfKnYJnMQyjBnOdlvQ5qwS7o2Mehhw2NfMPGVN2CzAsrOU2CBEn6wd30h4ZRXOjRiA72NyIfjR4QQhIp1v_xdtZfWsHgpmFUQ68fvIHyvESSjaXi9oXw-hUEFa_rFV70n7m0iMyWVHVwvpaGpvhsDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8b91b0b8e.mp4?token=sv9Cv-bv7AhF2PiCesjgdEMJDMjevqajalWEpgvk83Qlkx3nSioHR88W0c-qiKib8EqGXhxsMGIfIYW4_NC_-lX5FKCfIlKLHx5CQHlFPE2J3Q-lmhghnuQ4Vav1Z8JGUq_MKmG9CaBIMQVmJUSPvYvpLCZv3DwU7VQMSB5npu-6rgSwLcP6FnQdXPR14WOQmfKnYJnMQyjBnOdlvQ5qwS7o2Mehhw2NfMPGVN2CzAsrOU2CBEn6wd30h4ZRXOjRiA72NyIfjR4QQhIp1v_xdtZfWsHgpmFUQ68fvIHyvESSjaXi9oXw-hUEFa_rFV70n7m0iMyWVHVwvpaGpvhsDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
بعدسة نايا |
حشود مليونية تواصل القاء نظرة الوداع على قائد الثورة الشهيد في طهران.</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/naya_foriraq/80986" target="_blank">📅 23:55 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80985">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🌟
محافظة المثنى تعلن تعطيل الدوام الرسمي يوم الأربعاء المقبل لإفساح المجال أمام أبناء المحافظة للمشاركة في تشييع الجثمان الطاهر لآية الله العظمى سماحة السيد الشهيد علي الخامنئي (رضوان الله عليه)</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/naya_foriraq/80985" target="_blank">📅 23:35 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80984">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🇾🇪
عضو المكتب السياسي لأنصار الله محمد الفرح:
إصرار السعودية على تجرع الخسارة يدل على أن قرارها ليس بيدها وأنها مدفوعة ولا تراعي مصالح شعبها ولا تهتم لأمنها وطموحها، السعودية تبدد أموالها في شراء التافهين في اليمن ولبنان وتراهن على شخصيات لا تملك وزناً ولا احتراماً وتريد أدوات ومرتزقة</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/naya_foriraq/80984" target="_blank">📅 23:17 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80983">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">طلب_العشائر_والقبائل_العراقية_تشييع_جثمان_قائد_الثورة_الشهيد_بالعراق.pdf</div>
  <div class="tg-doc-extra">5.1 MB</div>
</div>
<a href="https://t.me/naya_foriraq/80983" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">#بالوثائق_للتأريخ
🇮🇶
🇮🇷
العشائر والقبائل العراقية تقدمت بطلب رسمي إلى قائد الثورة الإسلامية السيد مجتبى الخامنئي لإقامة مراسيم تشييع جثمان والده الشهيد السيد علي الخامنئي (رضوان الله عليه) على أرض العراق العظيم؛ وتعاهده على مواصلة السير على نهج الإمام الشهيد والتمسك بالمقاومة.</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/naya_foriraq/80983" target="_blank">📅 23:00 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80982">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OdQxI0niwbEyMZzBgMIp5P7TryWq_hNp2gBsBEXH4yyJof4f50CYtED-4zKcZCKffCg0X4EngBEyx6sEF4K3Ri008F33zMwOETdVvi5pHlLHqYP3wjH_y-MDQoJGlQnMHzvIOeb2y9ZuUrW1fqhHkfINBulEVCSkkQIgQrOA9mdWyXPP0YsV-4xJehIBcGuE-BPUKCaz_hKlteSlJYliAV4cd38Tcn5G7KG09fbVaotidL9Krp5035EXtnXuUmOxOmzSS67sB-SPnQU9nO9yi-mir2gW5z1vTgEaGxU6RT7mapvVs-SbONdxNKLxrdcrtMPalJybs4fR6mVh0ey6Ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامب:
تعلم أوروبا أنه عندما تستقبل مجرمين من العالم الثالث، فإنك تصبح دولة من العالم الثالث. يحدث ذلك بسرعة، في غمضة عين. تم انتخابي في الوقت المناسب!!!</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/naya_foriraq/80982" target="_blank">📅 22:36 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80981">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🇲🇦
المغرب تتأهل الى ربع نهائي كأس العالم بعد فوزها على كندا بـ3 اهداف مقابل لا شيء</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/naya_foriraq/80981" target="_blank">📅 22:32 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80980">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ldMaYMV6YxjCbz7artujpRgpK9IVTbL0d2MKJ8RG5sQVdeBhkFoG-PIMPp6pI6ya2RWF9adZd49BR1FthY6WFAF4S0sFoOBn8-B8H4LZ-dRVU0-yl12VkJAk6WKqWf8uLULw8iTdLOI85Aae2oSdamNT2max79cFBEqoZi46mbOlXDyj9Sv_3esCMlcILb1pHQkGbzqVlUUHXwohhzkQrAe8L7Kl1FVzsfMKIkqrsQZWkZAqE0YX2E0opOc6KSygeHC9V_6e_YYwLVPHzg2JuFYLOeCnWG8LbxyVbxAe3WlLdVzvYx_tP4i14jsvg3hNcHuuRUmbXLQP_K5ZLszmbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
وزير الخارجية الايراني عباس عراقجي:
‏يسرّ إيران أنها استقبلت ممثلين من أكثر من سبعين دولة ممن اختاروا المشاركة في تكريم قائدنا الأعلى الشهيد، آية الله العظمى خامنئي، ومن بينهم إخواننا العرب الأوفياء. ‏وسيظل هذا الإحياء التاريخي ذكرى خالدة في مسيرة علاقاتنا المشتركة.</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/naya_foriraq/80980" target="_blank">📅 22:19 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80979">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iMBS0yqLlFH_oHgCzPhp1jn_SMwte8usRU7iaN4BiBcl3y8Ws9UQ3dm4LIs1_ocsAWdrqykyzasLkN3xQZAyTKfxp4PqZOvQh417u6bFpBcAAa5L45XmC2zk0nk_hdoWrTZ5HC6PQiE8fYeZUTeEj4lHknPZLUIYniK-CQYkteuYtJ7lddjTouFe8FBXNGP8aI8WWRqCSFQb_3dOzFJLmWRsN2AYbXWiCkpcE6XrfNLgEApwqVofyNPCF9zH5aj9qCiNq3j7T7xtB7vVW1JrK0HffotnqZgtCGheQtd_Yq_euC2-LBR1dFTTzDZNaPsER6J3QMYtyJMKxcLKIqTgPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
🇺🇸
بعد اغلاق ايران الممر الذي وافقت عليه الولايات المتحدة لعبور مضيق هرمز.. عدة طائرات تكتيكية تابعة لسلاح الجو الأمريكي تحلق فوق خليج فارس:
‏- طائرة إنذار مبكر محمول جواً من طراز E-3B عدد 1
‏- 6 طائرات تزويد وقود من طراز KC-135R
‏- طائرتان للتزود بالوقود من طراز KC-46A</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/naya_foriraq/80979" target="_blank">📅 22:13 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80978">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a987a11e90.mp4?token=HMHdQD27hRwsBRxbds956Zfv3TBDQCSft7cM-r-_0Gr_fbYAeT1PDNgs5CDFXe9noH2Lu-FPs1bKoo1I9J_VLpd7fPZihBUoMuEECpvBaba27lGOC7iDByWUXklP4L2DkMVEUacvPQO5aEKtKESiEc0cN4-jpiKNyK9HpXIku4u2VKH4H2GVeKeLfyAO7Pp3G_gGJdFA8uiBRLEafJRSDGcgTy4lgxkpgcVKLLH2iM0Y6vXuBUmXUDqpKhtLfYcKm8hjtiX7qgMCmAvDlzsgZsgVjkx58meLEGkN-Ou8V1g0MkLGeOeRGwHuCPSkcLqXuZTLsab7n6G-3C62mz45Zw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a987a11e90.mp4?token=HMHdQD27hRwsBRxbds956Zfv3TBDQCSft7cM-r-_0Gr_fbYAeT1PDNgs5CDFXe9noH2Lu-FPs1bKoo1I9J_VLpd7fPZihBUoMuEECpvBaba27lGOC7iDByWUXklP4L2DkMVEUacvPQO5aEKtKESiEc0cN4-jpiKNyK9HpXIku4u2VKH4H2GVeKeLfyAO7Pp3G_gGJdFA8uiBRLEafJRSDGcgTy4lgxkpgcVKLLH2iM0Y6vXuBUmXUDqpKhtLfYcKm8hjtiX7qgMCmAvDlzsgZsgVjkx58meLEGkN-Ou8V1g0MkLGeOeRGwHuCPSkcLqXuZTLsab7n6G-3C62mz45Zw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الحشود المليونية في طهران تطالب بالثأر</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/naya_foriraq/80978" target="_blank">📅 22:00 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80977">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🏴‍☠️
اعلام العدو:
وفقًا لتقديرات الجيش، يوجد حتى الآن نحو 1,200 عنصر مسلح جنوب نهر الليطاني.</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/naya_foriraq/80977" target="_blank">📅 21:44 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80975">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">⭐️
خوفا من رد فعل إيران.. إعلام العدو:
نتنياهو طلب تأجيل العملية بمنطقة علي الطاهر جنوبي لبنان بطلب من ترامب.</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/naya_foriraq/80975" target="_blank">📅 21:14 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80974">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d7783221b7.mp4?token=Q9mH8zUTPUG6OjTiFzmIrgbT7DFhvmiBFQMjgCznNjM0NI12yG4TCDYjeZYezldZvANmpOrROfULWVnop1HR3TitszkYcWDmfGx5kg4vp9UCu3PAdjGHGK-xnoh8sHOx3oWfUm2xxJ5jalHDud8pBlYE6OYWlYbBxWxsaddaAcTJE3odej6Lu8a1WipPhD3-8dsvwmXqo6wtIUaajehGvYyP-YFTOnZBUcKl7WjPyTagrXZSj-l0NLMFvbQVGVH-Wqb3xfKJxufzeq0d9R_g2H_OwIOMeOG0mbBbqS2M9cKYe2mLjLHh4DzkjzGKYsFNryTfZvhWoegRM-l4JwC96UTcq7y1R9-m34zZX6ojxIdx_W9psb1iYAM8hj3l4C4uoea7KkYKOhUmSZbTUhdKDVG0GtA9I9dc9vX_VCfc-u370hILfQd9Go6Kbm9NApHvNY6eETTmJZIRXiQVr_QS2WAzr1mkDMvBxJeGeATRwQLEUYkqmf-fG4kS4-ZL1JgLmDGDsYXW60JWsl4MzH6YC_I-WT0y905mRZ5ndNxn_CGqNmfwZqDOyqAzRlAvZOv7TISHU2DJQqXbOBsrUnGPEYRgP3Ff25UPKkLJP8KNLIUc8E1VGwxUtsQp-_lxIgDoRVj792_qX6iBKOIUONuoKxKBOuRo5cSQdOwInu7JbFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7783221b7.mp4?token=Q9mH8zUTPUG6OjTiFzmIrgbT7DFhvmiBFQMjgCznNjM0NI12yG4TCDYjeZYezldZvANmpOrROfULWVnop1HR3TitszkYcWDmfGx5kg4vp9UCu3PAdjGHGK-xnoh8sHOx3oWfUm2xxJ5jalHDud8pBlYE6OYWlYbBxWxsaddaAcTJE3odej6Lu8a1WipPhD3-8dsvwmXqo6wtIUaajehGvYyP-YFTOnZBUcKl7WjPyTagrXZSj-l0NLMFvbQVGVH-Wqb3xfKJxufzeq0d9R_g2H_OwIOMeOG0mbBbqS2M9cKYe2mLjLHh4DzkjzGKYsFNryTfZvhWoegRM-l4JwC96UTcq7y1R9-m34zZX6ojxIdx_W9psb1iYAM8hj3l4C4uoea7KkYKOhUmSZbTUhdKDVG0GtA9I9dc9vX_VCfc-u370hILfQd9Go6Kbm9NApHvNY6eETTmJZIRXiQVr_QS2WAzr1mkDMvBxJeGeATRwQLEUYkqmf-fG4kS4-ZL1JgLmDGDsYXW60JWsl4MzH6YC_I-WT0y905mRZ5ndNxn_CGqNmfwZqDOyqAzRlAvZOv7TISHU2DJQqXbOBsrUnGPEYRgP3Ff25UPKkLJP8KNLIUc8E1VGwxUtsQp-_lxIgDoRVj792_qX6iBKOIUONuoKxKBOuRo5cSQdOwInu7JbFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
استمرار تدفق الحشود إلى مصلى الإمام الخميني في العاصمة طهران لوداع قائد الثورة الشهيد.</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/naya_foriraq/80974" target="_blank">📅 21:11 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80973">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">حضور القادة التاريخيين للمقاومة في مراسم وداع قائد الأمة الشهيد
من الإمام موسى الصدر إلى نيلسون مانديلا وغيرهما…
أحرار العالم في خيمة الحسين ع
#قوموا_لله</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/naya_foriraq/80973" target="_blank">📅 21:01 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80972">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ddef9fba30.mp4?token=P-Op3RA6oSWJ_ibXNxEnIgS__ULxt_SwUxeM0qbuv7MHTUFoZvS3ahp6W8yGAQbb0k0BzXAI5ursM2i4kQfMv-YwXkjhzaT2YUJoJPqOToJH9mLunNNybxRXRSBv1QlQflMchLdx6tNh8WmKVVeLcaRUvewUrZd-Z_tTUEjd3maBSFUWC9mVMbY22IiR1xMctlvwRxwqYpuLbqCCb0g95qA2ViYJ8kKjZOPMNDNhjG9wlEDCvqz8NQPucJKSzKU_9hOuLejiVOJZn8zeA10ZduADcsrKcgogWjfoeMFHl14b-Ea1Y4XKGb_evWiORwQiRQ1HtwP1Us-o0OGJdYYTeQ3Myo0tXPZ-WQu31AwHNKtOL6QEGnVGdmUHXUElEXCsa8E8rFBwaCFjNSQ6qufshEaEMJglR_tubUFPuHkdoZyliYJPxMeAT3jmAfaaHVTlHCCyIP_KhL8xVMVkl7RClTdwCpJ7S5_yip3PKyEJd83BlGNtA0rC843gE0RqPT3INMJWUWlaLuYXK7VSjkhQcghPZd7bzHm5jXx7hucd6s-mmWcSLheTb6WGDIj2qiTEUqE8waMm6RjVcxX-eYD6GPywAfm0ld4yHTT_h9P6yZKu3BvfaqepNwh-ZQjSgGhW27aJKK_j0DqxueO7Vqcihy9ep9MbuFzGOmoCNU15iOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ddef9fba30.mp4?token=P-Op3RA6oSWJ_ibXNxEnIgS__ULxt_SwUxeM0qbuv7MHTUFoZvS3ahp6W8yGAQbb0k0BzXAI5ursM2i4kQfMv-YwXkjhzaT2YUJoJPqOToJH9mLunNNybxRXRSBv1QlQflMchLdx6tNh8WmKVVeLcaRUvewUrZd-Z_tTUEjd3maBSFUWC9mVMbY22IiR1xMctlvwRxwqYpuLbqCCb0g95qA2ViYJ8kKjZOPMNDNhjG9wlEDCvqz8NQPucJKSzKU_9hOuLejiVOJZn8zeA10ZduADcsrKcgogWjfoeMFHl14b-Ea1Y4XKGb_evWiORwQiRQ1HtwP1Us-o0OGJdYYTeQ3Myo0tXPZ-WQu31AwHNKtOL6QEGnVGdmUHXUElEXCsa8E8rFBwaCFjNSQ6qufshEaEMJglR_tubUFPuHkdoZyliYJPxMeAT3jmAfaaHVTlHCCyIP_KhL8xVMVkl7RClTdwCpJ7S5_yip3PKyEJd83BlGNtA0rC843gE0RqPT3INMJWUWlaLuYXK7VSjkhQcghPZd7bzHm5jXx7hucd6s-mmWcSLheTb6WGDIj2qiTEUqE8waMm6RjVcxX-eYD6GPywAfm0ld4yHTT_h9P6yZKu3BvfaqepNwh-ZQjSgGhW27aJKK_j0DqxueO7Vqcihy9ep9MbuFzGOmoCNU15iOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
قصف جوي مجهول يستهدف حدود بردي بمحافظة كركوك شمالي العراق.</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/naya_foriraq/80972" target="_blank">📅 20:59 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80971">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/51c217e1cd.mp4?token=lkSpLab03IHxFKzvBcslWgpHM8gAQ32j0fvQdaZn-qT8lYWXiWLHc17iago6H7BQiVzGLQU_HHhJg2Rz6sVByOM3RCUUQkJ6UNOLJ7LtCxdHnHgtn3B5ExLvixbYr13KJzhEyJ2lCSI8Hrj6gXMmPAEXpt6xVyRxG2cRJFlXO2HsjJVn5bj5O8RyG8s7Zap2g6o1kH4bK0sm8WkBdP3Jc6GGiCy9kIGcLvFEAhn_zCaIBGHVIriK493UzV4EcAyHKjsE0Oaq5EumXyZKmVNsozO6dHzSJAyII9R_wN9rgusW7W287jrFh7e6CNIdFK7sd7iiIcUvmf7i3U4TlDUPy0TZ7V7fY1u33kXOZjxv29pchiaHgdyZwUwZ5K-tTVxq4sOM2dP_954lJYGtDjytxC0IWbpAp5sAYvELmZDJ6m-bLbYUkQjvZQihtufPBI3KsUfy7SdlIHcGRXfBuUjYfUSQsH_UeYppk7KbtOAuuCb4HkAo6AzACdyNG-QwdbqObmZIwP1cVURKlUgFgl4gwhu10pEL3SJ493zZG5JF73XMwb6KEcB3cnfQ2YYuHogrB7pfYOaa4w_M_7kcTSvMCx4Ttzh7cmxauRivaf1htO9hvb3-L7OUEpU55fXK7PAfBrXEnAZKvZPqOVXwr6Mdjgj8XKerKvhKRzpXzcId9-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/51c217e1cd.mp4?token=lkSpLab03IHxFKzvBcslWgpHM8gAQ32j0fvQdaZn-qT8lYWXiWLHc17iago6H7BQiVzGLQU_HHhJg2Rz6sVByOM3RCUUQkJ6UNOLJ7LtCxdHnHgtn3B5ExLvixbYr13KJzhEyJ2lCSI8Hrj6gXMmPAEXpt6xVyRxG2cRJFlXO2HsjJVn5bj5O8RyG8s7Zap2g6o1kH4bK0sm8WkBdP3Jc6GGiCy9kIGcLvFEAhn_zCaIBGHVIriK493UzV4EcAyHKjsE0Oaq5EumXyZKmVNsozO6dHzSJAyII9R_wN9rgusW7W287jrFh7e6CNIdFK7sd7iiIcUvmf7i3U4TlDUPy0TZ7V7fY1u33kXOZjxv29pchiaHgdyZwUwZ5K-tTVxq4sOM2dP_954lJYGtDjytxC0IWbpAp5sAYvELmZDJ6m-bLbYUkQjvZQihtufPBI3KsUfy7SdlIHcGRXfBuUjYfUSQsH_UeYppk7KbtOAuuCb4HkAo6AzACdyNG-QwdbqObmZIwP1cVURKlUgFgl4gwhu10pEL3SJ493zZG5JF73XMwb6KEcB3cnfQ2YYuHogrB7pfYOaa4w_M_7kcTSvMCx4Ttzh7cmxauRivaf1htO9hvb3-L7OUEpU55fXK7PAfBrXEnAZKvZPqOVXwr6Mdjgj8XKerKvhKRzpXzcId9-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الحشود المؤمنية المشاركة في مراسيم توديع إمام الأمة تقيم صلاة المغرب والعشاء في مصلى العاصمة طهران.</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/naya_foriraq/80971" target="_blank">📅 20:43 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80970">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🌟
المجرم ترامب: أتابع مراسم تشييع خامنئي وبإمكاننا القضاء على الجميع لكن لن يبقى أحد للتفاوض معه.  نحن والإيرانيون قررنا أخذ استراحة لمدة أسبوع من المحادثات إلى حين انتهاء مراسم التشييع.</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/naya_foriraq/80970" target="_blank">📅 20:35 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80969">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🌟
المجرم ترامب:
أتابع مراسم تشييع خامنئي وبإمكاننا القضاء على الجميع لكن لن يبقى أحد للتفاوض معه.
نحن والإيرانيون قررنا أخذ استراحة لمدة أسبوع من المحادثات إلى حين انتهاء مراسم التشييع.</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/naya_foriraq/80969" target="_blank">📅 20:34 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80968">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🇮🇶
محافظة ميسان تعلن تعطيل الدوام الرسمي يومي الأربعاء والخميس وذلك لإتاحة الفرصة أمام المواطنين للمشاركة في تشييع الشهيد السيد علي الخامنئي رضوان الله عليه.</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/naya_foriraq/80968" target="_blank">📅 20:32 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80967">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5e0993873.mp4?token=bVkqWzMTqMYbfO6ZvkTscA-afhrz1tw610BD4bnRGlH_jTVWc_jbw8ZHPDNpB_zIta_a3mWZ1HRFb7EmLkjGSGsZpiRSfdxiAcLMlveUfsENRgp-YA6tlJplO665sKUFPr9DOE2jSIl50QCdTZPhhAarFNisu8wRjWtt7nV9hcXMKT3zbIVJYbmsG42Fsu4Q6h8EHwhWT9VIZy0gall7oi7BmPfmE09DQb4EfWilTFXR7dNmBqwPL6CsJdF2DlXvmAC31SvCXNoEKdttzkIuF3lGGc8Ylwoe8AYJI1V77q53_MIkFYejho-hu294DZH3U6IZ2hEg9D73VHMfhLECkTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5e0993873.mp4?token=bVkqWzMTqMYbfO6ZvkTscA-afhrz1tw610BD4bnRGlH_jTVWc_jbw8ZHPDNpB_zIta_a3mWZ1HRFb7EmLkjGSGsZpiRSfdxiAcLMlveUfsENRgp-YA6tlJplO665sKUFPr9DOE2jSIl50QCdTZPhhAarFNisu8wRjWtt7nV9hcXMKT3zbIVJYbmsG42Fsu4Q6h8EHwhWT9VIZy0gall7oi7BmPfmE09DQb4EfWilTFXR7dNmBqwPL6CsJdF2DlXvmAC31SvCXNoEKdttzkIuF3lGGc8Ylwoe8AYJI1V77q53_MIkFYejho-hu294DZH3U6IZ2hEg9D73VHMfhLECkTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الحشود المؤمنية المشاركة في مراسيم توديع إمام الأمة تقيم صلاة المغرب والعشاء في مصلى العاصمة طهران.</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/naya_foriraq/80967" target="_blank">📅 20:26 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80966">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/427bde8bb7.mp4?token=lXfBMIVd98vD53x8V4AH6flllvfcxR9p248sY2H6Rc-a2qDC48Yalf-PATNzPoSaRwJLO9AudCFqFCMr7aCcJzSCVXjEXM11OpaRtBMHR7Yha6oF_Ry_Ncg9Kw2aJB-30YJYign66cVu8RLr9YilIwF7AutMnkxzb4gP8HcgKr6Xwg4vsJq_tpzSSuU5QTiWCYU9dci_uRT3LYJjvesLRJO-_k3dmd3LICMmvMqrPLEi6cviMpN-AymeX0_5Fng57gnqwyB7R0xwlPXgdk-Hu4RijwHbtjhg5nBekknzHbj-RWMqYyre8QHqMDyAF2V5IYqx0QK8Uz-tf0AFHqthbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/427bde8bb7.mp4?token=lXfBMIVd98vD53x8V4AH6flllvfcxR9p248sY2H6Rc-a2qDC48Yalf-PATNzPoSaRwJLO9AudCFqFCMr7aCcJzSCVXjEXM11OpaRtBMHR7Yha6oF_Ry_Ncg9Kw2aJB-30YJYign66cVu8RLr9YilIwF7AutMnkxzb4gP8HcgKr6Xwg4vsJq_tpzSSuU5QTiWCYU9dci_uRT3LYJjvesLRJO-_k3dmd3LICMmvMqrPLEi6cviMpN-AymeX0_5Fng57gnqwyB7R0xwlPXgdk-Hu4RijwHbtjhg5nBekknzHbj-RWMqYyre8QHqMDyAF2V5IYqx0QK8Uz-tf0AFHqthbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آقای خامنه‌ای خداحافظ
السيد الخامنئي… وداعًا</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/naya_foriraq/80966" target="_blank">📅 20:15 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80965">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DSWWGr9PxXr49QmH0klpFruivVkWtJ7eTrFzUXy_G-Hv-fE3Rso3rZkl7KY604Hzz8DQGjuYpv60NuzLGtq_xJ_w9pyxAb6ZxrfD1GB6ONx2TA6PdmbmREKzCcGEzLo30zjGBfKyRlBA-Q4QQFoqzUVVSYbPF_CTNFbfCbxHkwTFcXbNZyKqk15rOh0LVtkuAeX5WWhjhsUBltUt9L31jvKEBIbA3jWj2rB__wcjiWodRm39h6Tph4huHEpY0EqtC9l_pEnjNGX1EQLGw_IqHyytos1Hd55_XIthAAL18AITGw-0Mm2Z9rSZgVtx_7Z6Uy4NS3-CheIRr5uLlS9-tQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الأمين العام لحركة أنصار الله الأوفياء الشيخ حيدر الغراوي يدعو إلى المشاركة في تشييع جثمان قائد الثورة الإسلامية الشهيد السيد علي الخامنئي.</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/naya_foriraq/80965" target="_blank">📅 20:10 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80964">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🇮🇷
الرئيس الإيراني مسعود بزشكيان:
نحن المسلمون لن ننحني أمام الظلم والطغيان.</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/naya_foriraq/80964" target="_blank">📅 19:58 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80963">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e792efbf43.mp4?token=bggZY-D4FwXOrwRc1J0YSI9zEA_hYTfGD580vuZGzK4Hrgn0zjXUvOOBPh1Ib2cnuKtGd1AhL7ddUEFS-qZBTOWJfiQsHbZ_5HTo0Q64g1ActnrngG1-waA7JVsI56drWusxgmf1Fc7uTYwcUak3LdLkfNRmDSwbC0wHT59_qOs8fCL-Hf_6CmYsk29qMQnaYPYrt-XX4CyieW9dqIimBGRDGF8mB1qgRfntPnfttQPlY8ivxnevGObFZcjV-P7QEuC5LdVCF2PdHzZAQMDPDeWW9_YGfsjlHyaM0MhvQ13E1dgUq2eC5NOxoxNHkP73T1eo1wmNYhQ18PZ1uNyQ-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e792efbf43.mp4?token=bggZY-D4FwXOrwRc1J0YSI9zEA_hYTfGD580vuZGzK4Hrgn0zjXUvOOBPh1Ib2cnuKtGd1AhL7ddUEFS-qZBTOWJfiQsHbZ_5HTo0Q64g1ActnrngG1-waA7JVsI56drWusxgmf1Fc7uTYwcUak3LdLkfNRmDSwbC0wHT59_qOs8fCL-Hf_6CmYsk29qMQnaYPYrt-XX4CyieW9dqIimBGRDGF8mB1qgRfntPnfttQPlY8ivxnevGObFZcjV-P7QEuC5LdVCF2PdHzZAQMDPDeWW9_YGfsjlHyaM0MhvQ13E1dgUq2eC5NOxoxNHkP73T1eo1wmNYhQ18PZ1uNyQ-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
قصف جوي مجهول يستهدف حدود بردي بمحافظة كركوك شمالي العراق.</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/naya_foriraq/80963" target="_blank">📅 19:20 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80959">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ef85f6290f.mp4?token=gZLv5xSg8olEzE0UkMBEbyhVdmkOQClXAaKBUi3n1p-Vom43oPjToGh79CiLZfTd360xW4VQE3cC6q5AYYrRRaK0h8eFtMjzOkHcVHm3wRh_D-uLQhaFwryKp3hLvwR60Qt6eTxpHXEIvuOOkvtmeDie_SZ4C7wXk2EC7xQo60MmugkYvQqYUlEQHfg-SQI6C-VS5yqOrBIrsRRkqcwwFArvrNQYdJtS7RrMTFWbksyhpFBHLIgXDBpwFllcfwHT_Tfb2IOu1SHpcHrHn47AwEtY46I0fAp8PjXW0OY1X04w1KkayWy6FsOSUI2ceZluwY7uY0jU9Y5U-y8cuwbZ7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ef85f6290f.mp4?token=gZLv5xSg8olEzE0UkMBEbyhVdmkOQClXAaKBUi3n1p-Vom43oPjToGh79CiLZfTd360xW4VQE3cC6q5AYYrRRaK0h8eFtMjzOkHcVHm3wRh_D-uLQhaFwryKp3hLvwR60Qt6eTxpHXEIvuOOkvtmeDie_SZ4C7wXk2EC7xQo60MmugkYvQqYUlEQHfg-SQI6C-VS5yqOrBIrsRRkqcwwFArvrNQYdJtS7RrMTFWbksyhpFBHLIgXDBpwFllcfwHT_Tfb2IOu1SHpcHrHn47AwEtY46I0fAp8PjXW0OY1X04w1KkayWy6FsOSUI2ceZluwY7uY0jU9Y5U-y8cuwbZ7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
آلافُ المعزّين يكتظّون في المصلّى بانتظار انطلاق مراسم التشييع.</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/naya_foriraq/80959" target="_blank">📅 19:18 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80958">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iHFSofMZzOTwYVODctsFn3amzS9yxQRMjlohOVcf6YKRFJSVIhbzfSX8CpPbV0t_1fpa3S6FXu9RynnuNqtq3btyBsncCf20R_rty6FLsKIYMUjnlaPzNnOV37bDrEpIssJ94QoxViEyqhD6j4fbVuMDlA1E4qgsCgeYMvO5mt_jKDhVm12JDqND9fDr3GHLfJuQbcGS_Vl55vT3dByWJ2gvKEfIv7nZWpIVFGBAnlqrAFbC7gcTyYlkQO_p26nPvXBG8hj3WLRS0pk8WoKgZJoLzchum1zZzMTeaBQmswq4zZyiw9wYNxv4SrU1_1XQjaa_AnalRmzn9ODLNv019g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
قصف جوي مجهول يستهدف حدود بردي بمحافظة كركوك شمالي العراق.</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/naya_foriraq/80958" target="_blank">📅 19:03 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80957">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🔻
‏سفير إيران في الصين:
بكين ستحصل على تسهيلات في مضيق هرمز.</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/naya_foriraq/80957" target="_blank">📅 19:02 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80956">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🔻
مفوضية حقوق الإنسان في محافظة البصرة تناشد الجهات المعنية بالتدخل العاجل لإنقاذ عراقيات عالقات في الكويت بعد سحب جنسيتهن مؤكدة أنهن بلا هوية أو مستمسكات ما فاقم أوضاعهن الإنسانية وحرم بعضهن من الحصول على الخدمات الصحية الأساسية.</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/naya_foriraq/80956" target="_blank">📅 18:51 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80955">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pDfq_WFhS_ECdhlA5cfhj4hgfCU6oL4wgwN3GdtVSvW2Bv3z35e7PXXBFp-Oy5MeQ8ilCgheRicCY2-G1SROl79qe3UnX8kvJqU3j9Jp4M1nCcNOU2taFuERXG9Me16cAUToZ8esipnE-UW9XracDxdeLW24yOEXJmjhOE4hoaKCyKSfQ9qFkakuQ0-IwQNzf08EVH-lCe-eocjJIo6akGGRbA1T7uMRltaHVjq52YRyZV6JV1fMiA9WYLbLTx7uH3cgCyMX02KnlsZb6pyB5nYFcqpBFEVhNOhk_kVUNytHy94u7fSW3YjsVeNEcsJInaEa8syFViBJs_fu5Ercjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
آلافُ المعزّين يكتظّون في المصلّى بانتظار انطلاق مراسم التشييع.</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/naya_foriraq/80955" target="_blank">📅 18:29 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80954">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🔻
أردوغان
: يجب عدم السماح للحكومة الإسرائيلية الحالية بأن تفشي رائحة البارود والدماء في منطقتنا مرة أخرى</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/naya_foriraq/80954" target="_blank">📅 17:50 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80953">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aqOl-US87Abm8duuql7z1LH7u9Uvd-lSvewVU355zMo4DUVJYfcr5WFCxfSTruC9EkGnilfOnwYg6pyJyDx9kV-qKEkvVTC0ydIfD-15PS_1eLYW7BNcwpAnV56LQ97eiutxKqw8dk0RAfZp1n3O3Cx2Sz56b7f894zGfMQT6sArxccioXAzGU0ZZzZBTLjdZKzUSjIhNqPLUbY8pwskf11kCgh9uC5TXu2tTjkle5qi6hFdPSF0ivBz8eXIl-x37sSkYJ3M36B5DP_kY2rx9Ko0U2F-pBflT1SeoO_oDbezMk49HFOoKqpc5ZUAJFfUr5i2opLXZpcRxEwW_JSd5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
في غضون ساعات قليلة، أغلق الحرس الثوري الإيراني الممر الملاحي المدعوم من الولايات المتحدة تماماً، لا تعبر أي سفينة تجارية المياه العمانية لعبور المضيق.</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/naya_foriraq/80953" target="_blank">📅 17:19 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80952">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/721fa47854.mp4?token=Jz77bC5kckI_7V5kQzrkcJd_T8leyHVVXCpfeAcMeeCWAeqVzfSUqPnjJaIo5il2eK4BVlSHbIqdVSSQWa5A06VivpQ36g-NsXJ_gshBbxt_L7SC0owg-ekiuhimTXHTjxuUizwyVF3wXMevW5ZXfxq4pFTOjeTlbXiW94ItnnnUp5FNJXLWnGVmhoZWckQS_IP8X_wJOTHkrgdEmGpfJkRfOP5bI1eITshuc0dR4iSObPOVuv0RTlmw4c44HbH6TRM92jyRXEsRodYakerLfjSPLR6w55sIuN0i0qq45tHwsQ8cVOlmSuR3xZmk-7qgQlnF15D8K3QGZXkD5n99tJxIhgHRVM8z0rBGofpgMTd9YhxU-dv2cVrJtOS0j-IBMiQkNH5ZJ9G7tVlCnmSd6BZt3MMd6hfq3bR9FdBPh95Qb6QiDh_q6QsgeVg78ArrJ3AXaA34bJ01y31GRqLkueFKwIWnl-LBwvD4v9zPNmjjrQTu-KGoGXqSSI4_9X4r36HLZDQMJr9Yp_VaB_Icbf2spzHXvK6OrE4mzewyJ87BvVue3cg719QEt2EThdygdyqL4_oIXpjvppAp-Ma7vKPBKyWMEAvbEfgggOmwHksbnJM99H6La6OyT5nWUTUgclJNozOnn_AWtydik7tlDKomOsJyJ-X1bvbSNEh05es" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/721fa47854.mp4?token=Jz77bC5kckI_7V5kQzrkcJd_T8leyHVVXCpfeAcMeeCWAeqVzfSUqPnjJaIo5il2eK4BVlSHbIqdVSSQWa5A06VivpQ36g-NsXJ_gshBbxt_L7SC0owg-ekiuhimTXHTjxuUizwyVF3wXMevW5ZXfxq4pFTOjeTlbXiW94ItnnnUp5FNJXLWnGVmhoZWckQS_IP8X_wJOTHkrgdEmGpfJkRfOP5bI1eITshuc0dR4iSObPOVuv0RTlmw4c44HbH6TRM92jyRXEsRodYakerLfjSPLR6w55sIuN0i0qq45tHwsQ8cVOlmSuR3xZmk-7qgQlnF15D8K3QGZXkD5n99tJxIhgHRVM8z0rBGofpgMTd9YhxU-dv2cVrJtOS0j-IBMiQkNH5ZJ9G7tVlCnmSd6BZt3MMd6hfq3bR9FdBPh95Qb6QiDh_q6QsgeVg78ArrJ3AXaA34bJ01y31GRqLkueFKwIWnl-LBwvD4v9zPNmjjrQTu-KGoGXqSSI4_9X4r36HLZDQMJr9Yp_VaB_Icbf2spzHXvK6OrE4mzewyJ87BvVue3cg719QEt2EThdygdyqL4_oIXpjvppAp-Ma7vKPBKyWMEAvbEfgggOmwHksbnJM99H6La6OyT5nWUTUgclJNozOnn_AWtydik7tlDKomOsJyJ-X1bvbSNEh05es" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">٨ تمّوز... موعدُ أطفالِ العراقِ للوفاءِ للسيدِ القائدِ الشهيد...
بعدَ سبعينَ عاماً من الشوق.
إرفع قبضة يَدَكَ | أَنشِدْ قُوموا لله | وَاحْمِلْ رايَتَكَ
🚩
🚩
🚩
#قوموا_لله</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/naya_foriraq/80952" target="_blank">📅 17:17 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80949">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ce101f4641.mp4?token=IJq5sFIDSypAEnJD5ZEhv4Ilm4eCNM-s08lVx7pjBImElgPBrqV6pQHOq2IEXlKlggwowl42vmsVBaxiIzrZhd4OTgg9xlFwx8fA1Tt7pjAImLWOe1Qbr31rDdg2hvOwrH8TgW-L5XDKhzJXX6h-WVjAvzuGtQug-gQnZMdfzp-HkVOlvDKQAYwgMpIO791SMXPZ6mD094b-7m3_hF5BBdYmDUZL_jcBCdSizUy5Q_VLeanjEmSm7h_75Vl86_BqW_88aaSGtPi7h1PCA0LEVV1hhe9JlKdT3MfQmYW5pb6SVHGA-_W1_MiPuY2-0qyzy5vobc-yGuS7nWJoCaLU4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ce101f4641.mp4?token=IJq5sFIDSypAEnJD5ZEhv4Ilm4eCNM-s08lVx7pjBImElgPBrqV6pQHOq2IEXlKlggwowl42vmsVBaxiIzrZhd4OTgg9xlFwx8fA1Tt7pjAImLWOe1Qbr31rDdg2hvOwrH8TgW-L5XDKhzJXX6h-WVjAvzuGtQug-gQnZMdfzp-HkVOlvDKQAYwgMpIO791SMXPZ6mD094b-7m3_hF5BBdYmDUZL_jcBCdSizUy5Q_VLeanjEmSm7h_75Vl86_BqW_88aaSGtPi7h1PCA0LEVV1hhe9JlKdT3MfQmYW5pb6SVHGA-_W1_MiPuY2-0qyzy5vobc-yGuS7nWJoCaLU4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
كل بقعةٍ في إيران تهتف الموت للأميركان.</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/naya_foriraq/80949" target="_blank">📅 17:09 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80947">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tckCTWEWiHUb2CL_9L4qHctX7kyu-p-hm96oz06aFH42U9h6T1yyszerZ7R1J807LpzTPb6fXipPNE9dXEmGmt4wFQhlXhRhKy1yOTBn2jHp6GngqQOWYW1gtlKVH2Fqd8H5mYb3JIbODXUQH0HTBGVCEsrD4TQIaKm-hZoRTIhe4HtJEN-Q4nm4lyV-pTC_l6IfDbsKdS5R60UfHcy8BQVxfXC4yfPz6U8ZncFLixUViRHjRMBgfddswf1I2A5BJWa4nF03IUJI2z6F8uPTYhJEtaGzQChLL0VzBpYSFGjHIE5JdfOEm8KlYhJ7TCAXDYXxvi5FUcF2L41vpDXYXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭐️
الإرهابي الذي قتل خلال الإشتباكات مع القوات الأمنية العراقية في كركوك شمالي العراق.</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/naya_foriraq/80947" target="_blank">📅 16:10 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80946">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🔻
أعلنت وزارة العدل العراقية استرداد أكثر من 25 مليون دولار من أموال العراق المنهوبة خلال العامين الماضيين، مؤكدةً مواصلة إجراءاتها القضائية لاستعادة الأموال والأصول المهربة في الخارج.</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/naya_foriraq/80946" target="_blank">📅 15:45 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80945">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uPLQv02PFDmzElnSV9xDXXd0KHoWkwBZSAfTtEKC9q2cXKx2ecYumt03612joH51jOgsWp-ACmDzF-wA4xYsrhcbM1ynkR0d1cylzuIV9zHHc217H1pSn5xXoDbvUF-eTutCH-ziNjQBA7IA1GGUGdNM9LFZ-UZJGtMIM_rTG1BZ8pk7srLZrnQKlK0s4xS2ICu9CG5pH_Qdfc-CdSxdfvXshhx9gxLBJI7o8mJuohiHsapTDk8KwVMMpivq-mMg1CR6F8dt_GfSCl6WFbki7_Uc5R8aFoLcB8djgcQdfZDzE-CT0CZdntuG4AaHXzqNWizq86HL_Rc3IAtv7KcmmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
القوات الامنية العراقية تطيح بتاجر  للمخدرات بحوزته 14 ألف حبة كبتاجون في بغداد</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/naya_foriraq/80945" target="_blank">📅 15:39 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80944">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0532608c1e.mp4?token=KNDBbpBXl1V_7DQIjzl81TIaYnCL84EDTltauCKheSdk6Dbi_RW5QFklRsZ1axUGTWuEbEV16g7ih1E2xNfhaixPQSS38w044cyvtI-rb8cmzJAP3fteWZ6CteAJTn1rRxK7F_0UCWHPL-kDnJZsxKeChrZcMG7UT5SY5skRhh_2677S_59gcBC2uf-KpVNvsoVrs1E5OHFDnAUlWVw2sQ6pCBh_-tEgpJxokIkLMas3BCBr45-nhPzLfH_yHAWaMKfWAsrX8LQmWdv538qmT7auTiNzodosvJLeAH_ZiGCOTCkB-W7CtnjXwDjs-92FfMwpgcN-2-QM-BqqXo5Qnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0532608c1e.mp4?token=KNDBbpBXl1V_7DQIjzl81TIaYnCL84EDTltauCKheSdk6Dbi_RW5QFklRsZ1axUGTWuEbEV16g7ih1E2xNfhaixPQSS38w044cyvtI-rb8cmzJAP3fteWZ6CteAJTn1rRxK7F_0UCWHPL-kDnJZsxKeChrZcMG7UT5SY5skRhh_2677S_59gcBC2uf-KpVNvsoVrs1E5OHFDnAUlWVw2sQ6pCBh_-tEgpJxokIkLMas3BCBr45-nhPzLfH_yHAWaMKfWAsrX8LQmWdv538qmT7auTiNzodosvJLeAH_ZiGCOTCkB-W7CtnjXwDjs-92FfMwpgcN-2-QM-BqqXo5Qnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
كل بقعةٍ في إيران تهتف الموت للأميركان.</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/naya_foriraq/80944" target="_blank">📅 14:40 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80943">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">نايا - NAYA
pinned «
جمهورنا العزيز..  القناة الوحيدة المعترف بها من اللجنة الإعلامية العليا بخصوص التشيع المركزي هي على الرابط أدناه   https://t.me/KhameneiMediaIQ
»</div>
<div class="tg-footer"><a href="https://t.me/naya_foriraq/80943" target="_blank">📅 13:46 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80942">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">جمهورنا العزيز..
القناة الوحيدة المعترف بها من اللجنة الإعلامية العليا بخصوص التشيع المركزي هي على الرابط أدناه
https://t.me/KhameneiMediaIQ</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/naya_foriraq/80942" target="_blank">📅 13:45 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80941">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🇮🇷
المتحدث باسم الدفاع المدني الإيراني:
لم يتم الإبلاغ عن أي حوادث حتى الآن خلال مراسم وداع السيد القائد الشهيد.</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/naya_foriraq/80941" target="_blank">📅 13:28 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80940">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🔻
سيقيم صلاة الجنازة على جثمان الإمام الخامنئي في طهران آیة الله سبحاني (حفظه‌الله) ؛ في قم: آیة الله مکارم الشیرازي(حفظه‌الله) وفي مشهد آیة الله نوري الهمداني(حفظه‌الله).</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/naya_foriraq/80940" target="_blank">📅 13:19 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80937">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lygn6Gpft4LY3PeEYLERmRv8bLdlU_GTq0dESAAll3-h6JjKxtewraDm-yaegCUntzbBeg80J3pPLo9iPNyAO-Y1hwNuxmdKJCqM28HFLmLKygD43ziGtK3RGIDEHB4OVa-WXqk-Ummviw-zDnXmU6ODVyYqguvg69lbbT79L6M8BIXE2iTLOf2Ce271E5AiWL2iM6zraEQIYHNqirp1cuhVLuwDjbW4nhqEMAhhuQwId80aOINEz3oq-dtVoK5qH5KB-c3csdAQqR7_c_I50L7W8rA4LW2VvJuQIwXZr4W1ic7tiAtvnJ5_lnmk0-zhd4mVKAi6siuvI7wFpSzT4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ffdff87be6.mp4?token=lmrIYrwIZpLSInJAAygbwV0rcZEhZexiJ5EEeJKk6OWRD6qVJ1aLnXT4UMA7iuHXxr8y5PNPgFx9Dw88mv12NkF1tyn4OljI_4FhLuGhkssLhUOXhlObL0kJcLKXuAmre4rDZbl2R1sgfC8exqT7s6MVKhThXtvrzi3q2O-d5ta1HVowLoLum1IYUXkLNsHFJHvqdILQ2CXearbRQ_JGa-CxIT8g6lA5Meso9lulZ06NlaNv6C18e4IIKi-4_DfjR2WW7zAxAGVjG3wglxcMdMTCQ_kXppKH3o-seXSmZp-Uj--pSYckqL7sqV7P1RCIkZ_pc_HpSq9z1kwN4XiUWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ffdff87be6.mp4?token=lmrIYrwIZpLSInJAAygbwV0rcZEhZexiJ5EEeJKk6OWRD6qVJ1aLnXT4UMA7iuHXxr8y5PNPgFx9Dw88mv12NkF1tyn4OljI_4FhLuGhkssLhUOXhlObL0kJcLKXuAmre4rDZbl2R1sgfC8exqT7s6MVKhThXtvrzi3q2O-d5ta1HVowLoLum1IYUXkLNsHFJHvqdILQ2CXearbRQ_JGa-CxIT8g6lA5Meso9lulZ06NlaNv6C18e4IIKi-4_DfjR2WW7zAxAGVjG3wglxcMdMTCQ_kXppKH3o-seXSmZp-Uj--pSYckqL7sqV7P1RCIkZ_pc_HpSq9z1kwN4XiUWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇷🇺
🇮🇷
في العاصمة الإيرانية، قام المنظمون الروس بإقامة خيمة خاصة لاستقبال جميع المواطنين والضيوف من روسيا، الذين جاءوا لتوديع الشهيد الإمام خامنئي وأفراد عائلته.
على القماش الأبيض للخيمة، مكتوب باللغتين الفارسية والروسية: "الأتباع المحبون للشهيد من روسيا".</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/naya_foriraq/80937" target="_blank">📅 12:59 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80936">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M45Q-7SEEwMskZTXi5zJOHVX177pkEpqd9DZy_hqySM2WHV44uP-jcs2AHcn9_5J3j56BRku-_5wOqLMuTVJm_UKCoFOXI8B8Ej9ffshr45H8x3Q4_SoqjbaHZPIuFk8lsMWoSCEHYdrAVs8YL14xmIHmC3QsJktiHRJMEdg-kJMVujTDuothLLH4APurXjdhTIG5t45dmTwRq5nevEm8jSi1L3Cpt0x6601aoiAA-7cwjnUsg84H4eXUcdKCJqrWYHeepkWwKXEKraGOtWoaWl3M52CHe5D7vxDjBa7KbCw6oMf9kBMGyquBMHpM5VNloDJyt4DV_u4CQxpehUtmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏رئيس العراق : بعد الانتهاء من ملف الفساد سنتجه إلى "سلاح الفصائل والملف الأمني مع تركيا"</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/naya_foriraq/80936" target="_blank">📅 12:51 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80935">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🇮🇶
معاون رئيس أركان هيئة الحشد الشعبي لشؤون العمليات، ياسر حسين العيساوي:
اكتمال الاستعدادات التنظيمية الخاصة بمراسم تشييع آية الله العظمى السيد الشهيد علي الخامنئي (قدس سره)، والمقرر إقامتها يوم الأربعاء المقبل في محافظتي النجف الأشرف وكربلاء المقدسة.
الخطط شملت محافظتي النجف الأشرف وكربلاء المقدسة، وجرى إعدادها بالتنسيق بين تشكيلات الحشد والقوات الأمنية والجهات المعنية، إلى جانب وضع خطط تنظيمية وخدمية بديلة لضمان انسيابية مراسم التشييع، والاستعدادات تعكس مستوى عالياً من الجاهزية والإمكانات المسخرة لإنجاح المناسبة.
مراسم التشييع تمثل رسالة وفاء لدماء الشهداء الذين ارتقوا جراء العدوان الصهيو-أميركي.
العراق يتشرف باحتضان هذه المناسبة واستقبال المشاركين فيها، لما يمثله الشهيد السيد علي الخامنئي من مكانة دينية وإسلامية كبيرة.</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/naya_foriraq/80935" target="_blank">📅 12:45 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80934">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F8fo5ThK6gn2jEHcSoyXkvXORE4tdmTY4i9robs08zkTv4LWMjDDk2fFMiVSgI1D6XBph3p6uxvzHhzFFZrBeYIEjtkPO2VTsmcNit7srdZNuFfiMOh8GIi1ZY50-kUMyMfHYw71_eLUKnnKRyFcq8qKQbBGdEpK5Dc9gfR1OXEKl4NU5a0Qz_WWIXZxhbRU9nbbtb3A593yEBWK9JT0AUqa2zyBVlvzU60E5ygQ0tCA-F7wEElUFkzl8C8LcfEEEuMbPPzizTKenm79BHbF42YvLuRpf4lkMbm2oypMoJ_vY8zCNoXcxf8ClPo-6c8-c-iuRr0dAu_6XN6zGWQo2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭐️
إشتباكات بين القوات الامنية العراقية وعناصر تنظيم داعsh الإرهابي في محافظة كركوك شمالي العراق؛ مقتل إرهابي كحصيلة أولية.</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/naya_foriraq/80934" target="_blank">📅 12:41 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80933">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zt8HTY4JijYmVmuRRkCmIpw9QNfhUC1nZO1d9L6-belWdJ5rybUmD3dxEJvLN7hkx3jczQaUhgPSSqsSrK6QzLsqufzEtHDJlfuS8WY1lNRydsUqbfXvul57_1Es-NYMXjVZy2BpwxcJKqmhro2JX8KsMYAz6i1sOEL9rOu4I9ofs9DiNcYJ7uY-V00mX8UNnWbATAKreXFXTmRhwwBXpPZuOAD6EFv7imW8BbmeyVdwXAb7hN0J0t6u6Zfm6osgM9XyZiKziCV_rJCV2Np_xI6zD8EW6OlXOEGsgwVkxquxncUXr7nGdQVZTJ1Et_vLQiwYURZir1F5O6c1m5Mh-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
هيئة الحشد الشعبي:
عمليات الفرات الأوسط بالحشد تعقد اجتماعًا لاستكمال خطة مراسم تشييع الشهيد السيد الخامنئي (قدس سره).</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/naya_foriraq/80933" target="_blank">📅 12:30 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80932">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">المرثية التاريخية للشاعر الفلسطيني البارز تميم البرغوثي في رثاء قائد الثورة الإسلامية الشهيد.
#قوموا_لله</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/naya_foriraq/80932" target="_blank">📅 12:21 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80931">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/15cbaa4687.mp4?token=BvQsUjQzrzxWiPz3PRs4I1T9YnFkYg7Ul0rlAEnOm0ikA9s1WdFsuZ2T_7qKPtLtr0h9PlZ4biM4WX5KBcz7pME9iAhTNjxXXphPq_ZM40eiHZ80l5oUOpyWm1xfvR3_czJD36C94ueMxmDbkrUNRoe31xRV_AL-Df3cWFeXSB4J-q5Hd-XZOz2qKEYN_J7ocbDqde8PrYqq50UPvoyNM2kp0SYjokP15XVrXBnIC2wTj9LEwE4LD4Y-ZhhNg6ctZ1i6apqIarW6YSGZsP15FNsH5MbFcUrcKALF2ORdDG1khZkIi8VijU1IYsxnmoqPVm7v9jHc6484MKLIm_uu4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/15cbaa4687.mp4?token=BvQsUjQzrzxWiPz3PRs4I1T9YnFkYg7Ul0rlAEnOm0ikA9s1WdFsuZ2T_7qKPtLtr0h9PlZ4biM4WX5KBcz7pME9iAhTNjxXXphPq_ZM40eiHZ80l5oUOpyWm1xfvR3_czJD36C94ueMxmDbkrUNRoe31xRV_AL-Df3cWFeXSB4J-q5Hd-XZOz2qKEYN_J7ocbDqde8PrYqq50UPvoyNM2kp0SYjokP15XVrXBnIC2wTj9LEwE4LD4Y-ZhhNg6ctZ1i6apqIarW6YSGZsP15FNsH5MbFcUrcKALF2ORdDG1khZkIi8VijU1IYsxnmoqPVm7v9jHc6484MKLIm_uu4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⭐️
في حادثة أخرى.. عصابات داعsh الإرهابية تقدم على إختطاف مواطن في منطقة التون كوبري بمحافظة كركوك شمالي العراق، وتقتاده الى جهة مجهولة.</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/naya_foriraq/80931" target="_blank">📅 12:06 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80930">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">⭐️
إشتباكات بين القوات الامنية العراقية وعناصر تنظيم داعsh الإرهابي في محافظة كركوك شمالي العراق؛ مقتل إرهابي كحصيلة أولية.</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/naya_foriraq/80930" target="_blank">📅 11:49 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80929">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">⭐️
رئيس الوزراء العراقي "علي الزيدي":
سنعالج ملف الفصائل المسلحة بطريقة حكيمة ومقاربة عراقية تضمن منع إراقة الدماء.
‏أميركا شريك استراتيجي والعراق يقرر علاقاته وفق مصالحه الوطنية.
‏العراق سيقيّم احتياجاته الأمنية بعد انتهاء مهمة التحالف الدولي.‏
العراق سيحدد ما إذا كان سيعقد اتفاقيات أو مذكرات تفاهم مع أميركا أو غيرها.‏
سنعالج الملفات الأمنية العالقة مع تركيا وإيران وفي مقدمتها "حزب العمال وسنجار".</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/naya_foriraq/80929" target="_blank">📅 11:46 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80928">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🔻
جانب أخر من التشييع الرمزي لقائد الثورة الإسلامية، في نيجيريا.</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/naya_foriraq/80928" target="_blank">📅 11:43 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80923">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rN7WwXkL9S_QxFA3fWrC8UWzJBoK8e1LMlqbfjC4Yh9zwKvIA5EIJ2CFxi2GEMsZDzfBm4LWYzzojYrr6E9YiXOGWJldiwxIB-GsIfO4skv-7czjf0tsHCpgQgQ_gdu9u6mphqShiTFeIIkMeh2CIX8-lCqWy-9qES75WFlnWJkI4XjihhfXck9RAeLL9u2cYFJ4vVbMvx3TySUENX4_RnP8b_TwgUB04SCb19lG86CLcMc1GGt1_xMo94gbKQmJQEuP1HBpXMY4TQaca96OvTqyksjFZ__9jeVv7ySNA_UcXcqFr5bMtTXzjrJxrr5U4w1gbxbT4W5AsAsePncAlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FxdYW80rybzMVadlHErks1HPsDro8pRS278QzZMcsT4VLGnhPkEWOS-mwibGQUsXfWP9_Fcu_bLfUX56PAqdFKOnkQGWleN9PdKcdPoyOekJCE56omyEmPzfRYoxIr4Qb-eg6X8gs-XhQkSF4u94wg8BGSOscPxVMejlJG2d0R6jU3B3X3XvydUhwKaaFERSzpXfygieJnOvR1OIHOHIB4_oQxe4YvY_cuGkgKb717n8uZO-DymTHB0AutkTq8sWtEbOOZBxwoZFGup-FEPoakeh5x4Ga8Ag5X22XObtf_gEloQTgTcdrAWnNta_TlZzLEAAJ0n4jNFuQVUfL9IEww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Zvd2Z7LFug3xtDMEBWtMPUHuG8DOcEZWbVSyUBSIM9HjUl1rWa_408WoseO6inpuRLdTmhwZ4CuVVBxA9DgALwaxfJtTLDgfwC1kiQR2EJMaLNUcKmMvukNcYlhZdNBJOS2wYnf3A-W8BcKGVOc5gF9EQTj1jd8_GgwFZS1Qdyv0888pCdw691jnmgqzhCbXO_cIQR9VSzdXT2P5TJdsNs4ogSPxrr-hFLbQmcn5psFFegpkAV3_6-udTNHDIUdS7peK02bwe3EaMC6RVpl3OJFRD7uWj3S3kx23BJHdgQ6plUEqTuYjAgr_xyMN8WqzZ205DSMWgP05FzuDezD7-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Fg2RaBPfs61eyI2d3wb-S36ZsQxHoWfxPhYwAs1d7vD4iqwezeVYck2w6ulvdg4mTEKVmm24mVe39zJo98tZRsKXl7e5zI36zZIA-pVAnLkD6-5nAiP31QxvbLZOzVFH0xqb6nqSdOJuuYQqrP1A8vP-7mmunu4dNZ7P-WCuC4NAEi2qgnPojlND-UrTy98vxI3q_kqD6sQp2-uBECznbbZa7yY9tzgC-nup77K63FLaMI0IuSwEsotyOJpoSXgz4Sjv3qoA8BHVLcGNqQv5_lPjQ5jtX6qE-dZRu0NZtywwI6TlzjLZLakb7QymWWRyu6cso9GGFHQKyQCRj14H4Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f68d37552a.mp4?token=kWN00JUbNCFSUbRFO4KwYZrCWLcymoQOGm-nRp3pAd16RvHkkRZ8M61RVirhbAWT1GX-UZadOap4UigIw84iUZbHLG6HLH6h1hwkG7HfIc8Bz_H6c55apMBB9uI3dkPTUyZfw8s9OEen2Tgxqyx3R7CHDFAbJCOcZ-UZPvkMkzmo4S7TwVUUXBdTMZvzeTkYAYYvll2Y5uPhRCavs8yh3eOAlQwZ9T8r93Ijrag54LH26slYNr57RuEsvwN3-XQKrEm4y1S8e-NQCA2z_velnLMzSB3BQaFrO1o-cQPMn9tFLq334SZk5rpir-2g0Q-YWVo_Y9DJB4atC9qNj3FaNYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f68d37552a.mp4?token=kWN00JUbNCFSUbRFO4KwYZrCWLcymoQOGm-nRp3pAd16RvHkkRZ8M61RVirhbAWT1GX-UZadOap4UigIw84iUZbHLG6HLH6h1hwkG7HfIc8Bz_H6c55apMBB9uI3dkPTUyZfw8s9OEen2Tgxqyx3R7CHDFAbJCOcZ-UZPvkMkzmo4S7TwVUUXBdTMZvzeTkYAYYvll2Y5uPhRCavs8yh3eOAlQwZ9T8r93Ijrag54LH26slYNr57RuEsvwN3-XQKrEm4y1S8e-NQCA2z_velnLMzSB3BQaFrO1o-cQPMn9tFLq334SZk5rpir-2g0Q-YWVo_Y9DJB4atC9qNj3FaNYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">على طريقة خدمة زوار الإمام الحسين.. المواكب الحسينية تقدم الخدمات للمشاركين في مراسيم توديع قائد الثورة الإسلامية بالعاصمة الإيرانية طهران.</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/naya_foriraq/80923" target="_blank">📅 11:35 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80922">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dsEQPDQM0ntULBupv9Pe2Wvdf9KkqFeRkZFrpuEdYn0l1t0cAPdTh1ES2j3iiS9mmU080KSl4m9qMLC2fN3qJvjCBp9zJ_kY13Dm_7nIcgl1i1IyF45p1wGWrromfkRkOXGWwjVvkLaFqR9M805TOOfFqrQuZDN289U7L26YxL6S8k7mBj_8CuiTDSHVaPovlPngiTPX9w3_a-KC8VD77aN_5qdjnwFgL7LK4do3akk38dhHT73vUP8-HciYvpMvJIIlvjzrGBoLyDoKvxr9WTnAFS1798bZed3W-RrCkkQdrOls5JHAn5S1Ym586FUtqN4fMx7BGM0_TSY5k595zA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭐️
إرهابيي ماتسمى "وحدات حماية شرق كردستان" الإنفصالية تعلن عن هوية عناصرها الذين تم قتلهم على أيدي القوات الأمنية الإيرانية في مدينة مهاباد بالقرب من الحدود الإيرانية العراقية.</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/naya_foriraq/80922" target="_blank">📅 11:32 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80921">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">⭐️
إشتباكات بين القوات الامنية العراقية وعناصر تنظيم داعsh الإرهابي في محافظة كركوك شمالي العراق؛ مقتل إرهابي كحصيلة أولية.</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/naya_foriraq/80921" target="_blank">📅 11:25 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80920">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🇮🇷
غدا الساعة 6 صباحاً بتوقيت طهران ستقام صلاة الجنازة على جثمان الشهيد المجاهد الإمام الخامنئي والشهداء من عائلته في مصلى الإمام الخميني.</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/naya_foriraq/80920" target="_blank">📅 10:58 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80919">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BQcc45SXv7IUsqPYrmFezZU7sbW1NqdWcZD0G6IVHeQxVK1a3m3SfwpE-dx5zJWgvTfkx65eLjUI-9a-hZGNHLoqlcuFwqiVF9NN0y4mXjbqJy5pGcPT1NosKXCHNdGUA19WXOKY2-SlwdWQ7BxINd7o609hGGzN6E1hvHiVVcEH_jtyS__BE4PpFZH0IY0wuNTensKzXRbLeQqmhkCqsImF8X_5_B-4fVfiEzWgevZnpDzNA6_v1_gOp3RsVTLk7WspEcV1LBWNsJ3IGfaWiWGBV7V9oNA_OHvGCvcsnypaukGshedKDQLwxBo1QJQj8l1L5lsNsr0hk-ro-iDdQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لازالت الجموع الغفيرة تتدفق نحو مصلى الإمام الخميني في العاصمة الإيرانية طهران للمشاركة في توديع جثمان قائد الثورة الإسلامية.</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/naya_foriraq/80919" target="_blank">📅 10:23 · 13 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
