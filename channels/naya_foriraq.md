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
<img src="https://cdn4.telesco.pe/file/lALVgBpkwCEtDDIZx9z1z4K7WSrlVQZ_qMHlJveep48HFiUOv3Ox8cib4arAlGnnjD1_6Zt1Ij7Cs_E-MfDyx2r031wpGxaVeAqz5TZzFmVcSUSX061_0VrU1Rarh3diDYmkFkmBwy9W6Ljd_Virk0OTRz0cY5x4KE9pIdBK_L9VZYn8bEOk99N6KuWmc_y-9g_bH6Atwz4l7jn1pZYb0H--D1SyAhqv5J62qN_MueAPJxFy5AidT4f7zoPH8rQK3k7X13Zua9PoMhrHGCfFIbvH6EbgViZ4t-itpYhttwWvh1Nx2eOFhjLpi-pZuLTZIAoebo2nlMftSzC2ripsYg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 265K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-22 05:31:08</div>
<hr>

<div class="tg-post" id="msg-93636">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b42f603e9.mp4?token=VpD1CsGzAtSZGyamJDfEAVeWRjtNGebSqOYXatAO4rHr1eTnq5l8n-HEmFBdrtCp-tl1m8-AqS2DDSGlhdw3PcICaMb4e3Vgnx9S-f4kDdohIsI1Ttla6g5E036DbyLl1ed1wvx2s0j448XL5XhlBKTj24_5ND3RVU6SJCCJrvfPJthScdvxmtQkPimdEhTsvRHZK-GtjX7I4OG4s5yVAIi_S5B-idrvjAbuOaFCQ7bWrE-wDx4tEVa4YGDcBgHDYs3C0LmINVeMmKcIANk2FucblDu-QQtdd3nPvobEMncljqyFRW1lvRL1DvkK9zmC_wdEaNozmW0u4kVNFa-4Mg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b42f603e9.mp4?token=VpD1CsGzAtSZGyamJDfEAVeWRjtNGebSqOYXatAO4rHr1eTnq5l8n-HEmFBdrtCp-tl1m8-AqS2DDSGlhdw3PcICaMb4e3Vgnx9S-f4kDdohIsI1Ttla6g5E036DbyLl1ed1wvx2s0j448XL5XhlBKTj24_5ND3RVU6SJCCJrvfPJthScdvxmtQkPimdEhTsvRHZK-GtjX7I4OG4s5yVAIi_S5B-idrvjAbuOaFCQ7bWrE-wDx4tEVa4YGDcBgHDYs3C0LmINVeMmKcIANk2FucblDu-QQtdd3nPvobEMncljqyFRW1lvRL1DvkK9zmC_wdEaNozmW0u4kVNFa-4Mg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لحظة إصابة صواريخ القوات اليمنية المسلحة اهدافها في الرياض وسط السعودية  https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 4.27K · <a href="https://t.me/naya_foriraq/93636" target="_blank">📅 03:54 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93633">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">لحظة إصابة صواريخ القوات اليمنية المسلحة اهدافها في الرياض وسط السعودية
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 7.88K · <a href="https://t.me/naya_foriraq/93633" target="_blank">📅 02:47 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93632">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MSQ8njANFx-KWb7gwkSe3kIZLVBdFnZN3WjTcnB7tCt7jybS1SgmDzOv0r3sjR4O90A3gpDixojuoLjNOIYd9BkfjnezsEdDgFrpGD-2w9PUUvgsdRcprkx493GJK9t1SDxvYOzTnmR7Eb7e2LARSYJCIsxUNjO6bptV2v6zQc049on0ic_8ckbFZaX9Wgomju_AtOKDoFLNGlLoVhmVQGpsFqz5tut66Hhrcu7MpmLc8KBeoVwj3OFOqFERd1TWaCr3mJGj1MncSTVuHOqgsRGjXgvvYIKD80z_zrJKcElLzjdl0Dia2GoiVpuvszskbNCdSKGBTG5scqe_rsDx1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
🇸🇦
التحقيقات الفدرالية الأمريكية تعتقل مواطن سعودي كان يتجسس مع زوجته على شركة بمجال الذكاء الصناعي في امريكا والتحقيقات الاولية تشير ان محمد بن سلمان قد كلفه بذلك !</div>
<div class="tg-footer">👁️ 8.58K · <a href="https://t.me/naya_foriraq/93632" target="_blank">📅 02:30 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93631">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">انفجارات تهز مدينة الخرج في السعودية،صاروخ كروز مجنح يصيب هدفه بشكل مباشر
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/naya_foriraq/93631" target="_blank">📅 01:42 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93630">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/99fd1b9c49.mp4?token=Woj8X4NNe3xm4J-8EYkvI-jeGi0E6681shyyBkCKmgB6snYfNYcetdIZXyYZ1oYXw68n0ZZQZv1r4JbWInjCUwkzJ2TeIpXCRxkvlK6IFh6FnqexA13rjMIHkADcU7QbaJRUcXCatKGZdA6DwpfvnNBFi94lGP8ELPi1N_h-QduYTCmnHs0ODbrKSgobnwtsf7z9oPkyeuF71spN0FtKt_6tpWG1LtB7RRc0OITXA3DZ85LsBpRgZqoYNqkRcmfagI420B1mRbyry5ZAOSOEb2bW46ccT-7x4a6vi2z2_IqJdsaAGizk9ZMIWFbz5izBhF5KoLyLMReTZwxyXJfb7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/99fd1b9c49.mp4?token=Woj8X4NNe3xm4J-8EYkvI-jeGi0E6681shyyBkCKmgB6snYfNYcetdIZXyYZ1oYXw68n0ZZQZv1r4JbWInjCUwkzJ2TeIpXCRxkvlK6IFh6FnqexA13rjMIHkADcU7QbaJRUcXCatKGZdA6DwpfvnNBFi94lGP8ELPi1N_h-QduYTCmnHs0ODbrKSgobnwtsf7z9oPkyeuF71spN0FtKt_6tpWG1LtB7RRc0OITXA3DZ85LsBpRgZqoYNqkRcmfagI420B1mRbyry5ZAOSOEb2bW46ccT-7x4a6vi2z2_IqJdsaAGizk9ZMIWFbz5izBhF5KoLyLMReTZwxyXJfb7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الله أكبر
🇸🇦
وزارة الطاقة السعودية: استهداف مبنى إداري تابع لشركة أرامكو السعودية في الظهران.  https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/naya_foriraq/93630" target="_blank">📅 01:21 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93628">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ed9d03570d.mp4?token=dLAniFLITafgW5b4RuXEIxnR_PPhsMVC_Sa9rtjd-QyA18SccjbjnjlN1O7ZHzlHcSNL506mx3E57SfSv6eYHOw2vO35jk62xS_6DX8301e3ZpUQCxmBlXEGSPkLe4LylawdU9fFSRtaZhOVMMWpfLvdvoyag7lrwgtx6pUtDKwNJi1kqxzVOVgnGUGyVL75nT9Whe_Gp_uYbIOD57l18i81psh4hyVHUUv9jZtIik_w-dQcieVMhlcfi0l-CCxm3QRudXS5m7W6kwzES8BNAEdghbno4opQ3ScQrIxyLHIAbVcwyfaFjH3z75RBhL9GyjMCQGegm_pLDfHlBmvtc2McULMxTEm47oQqT0k48K0ibL2-bfqsFHbtT6dtLCvSmRhyI0laDx8Cf-l3Ozn7ADzkk2n8iYwMdppDMQ46zImxlRn01UCwjtvrEGEky-n5WaG74f3fi91m5mup9OJS1YelAxA-dfirWFNghHtJCR-HymrpxsGBM2LmTpG_rqQglaztWx5HWIllcL991UYOn7rJUSuas-lrXwhNatQz-SN_xq-7yFHh3xNLqy1NHVM3UQO1ZqF5EzGcrj35D3WUkkRxOouJ9QRM6WPPtrf59Q0_gIMTLGjBTwuIRl60PPEW7jfTR1TSHvA3kErEkhkMOJqzisFNHsPzE9F-18cJ8hU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ed9d03570d.mp4?token=dLAniFLITafgW5b4RuXEIxnR_PPhsMVC_Sa9rtjd-QyA18SccjbjnjlN1O7ZHzlHcSNL506mx3E57SfSv6eYHOw2vO35jk62xS_6DX8301e3ZpUQCxmBlXEGSPkLe4LylawdU9fFSRtaZhOVMMWpfLvdvoyag7lrwgtx6pUtDKwNJi1kqxzVOVgnGUGyVL75nT9Whe_Gp_uYbIOD57l18i81psh4hyVHUUv9jZtIik_w-dQcieVMhlcfi0l-CCxm3QRudXS5m7W6kwzES8BNAEdghbno4opQ3ScQrIxyLHIAbVcwyfaFjH3z75RBhL9GyjMCQGegm_pLDfHlBmvtc2McULMxTEm47oQqT0k48K0ibL2-bfqsFHbtT6dtLCvSmRhyI0laDx8Cf-l3Ozn7ADzkk2n8iYwMdppDMQ46zImxlRn01UCwjtvrEGEky-n5WaG74f3fi91m5mup9OJS1YelAxA-dfirWFNghHtJCR-HymrpxsGBM2LmTpG_rqQglaztWx5HWIllcL991UYOn7rJUSuas-lrXwhNatQz-SN_xq-7yFHh3xNLqy1NHVM3UQO1ZqF5EzGcrj35D3WUkkRxOouJ9QRM6WPPtrf59Q0_gIMTLGjBTwuIRl60PPEW7jfTR1TSHvA3kErEkhkMOJqzisFNHsPzE9F-18cJ8hU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاهد حديثة من سماء الرياض أثناء الهجوم الصاروخي اليمني.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/naya_foriraq/93628" target="_blank">📅 01:17 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93627">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🇸🇦
الدفاع المدني السعودي يعلن عن إصابات مباشرة للصواريخ اليمنية في العاصمة الرياض وسقوط عدة إصابات.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/naya_foriraq/93627" target="_blank">📅 01:17 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93626">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">بمن نصدق؟!
التحالف يقول تم التصدي
ووزارة الطاقة تقول تعرضنا لاعتداء!</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/naya_foriraq/93626" target="_blank">📅 01:16 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93625">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">مقرات شركة ارامكو في الظهران تتعرض للقصف  https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/naya_foriraq/93625" target="_blank">📅 01:05 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93624">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">الله أكبر
🇸🇦
وزارة الطاقة السعودية:
استهداف مبنى إداري تابع لشركة أرامكو السعودية في الظهران.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/naya_foriraq/93624" target="_blank">📅 01:03 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93620">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/010a765bc9.mp4?token=V1DcTdPqankdbgVbQhlzUsPJLfle5AtaAzYvKxrnkeSJdXB4LI69Smhfv8WtXuIiXUSVBjdVBwJDFp3mkNTGY1JXRQnOAR4I_xT18Cp0_35-W-pAGCx5oLcjYpQCTWYjT7X1Ir9P6QsYOIuABftDwQdJzYac3d1hQ5LxfvfLdzWWdta2_rkiTTGUlb28yJ81-zugeBWoYdC-PuwCaxkNhdN6ZR5BeSx2vJcqCGY2wZL2rEleKXKDGZxf1zrxugB-cjpT-ijQQ4KDrBO2Gmnrp0t1_t1c5nm68KKzeTDuX6XsKHuZvueX-HPhryH774cqehgXab1MfPIesjkxfWPtUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/010a765bc9.mp4?token=V1DcTdPqankdbgVbQhlzUsPJLfle5AtaAzYvKxrnkeSJdXB4LI69Smhfv8WtXuIiXUSVBjdVBwJDFp3mkNTGY1JXRQnOAR4I_xT18Cp0_35-W-pAGCx5oLcjYpQCTWYjT7X1Ir9P6QsYOIuABftDwQdJzYac3d1hQ5LxfvfLdzWWdta2_rkiTTGUlb28yJ81-zugeBWoYdC-PuwCaxkNhdN6ZR5BeSx2vJcqCGY2wZL2rEleKXKDGZxf1zrxugB-cjpT-ijQQ4KDrBO2Gmnrp0t1_t1c5nm68KKzeTDuX6XsKHuZvueX-HPhryH774cqehgXab1MfPIesjkxfWPtUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بعد مناشدات عديدة من السلطات السعودية لحجب التوثيقات،مجموعة جديدة من المشاهد لنايا من مراسليها في الرياض والدمام
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/naya_foriraq/93620" target="_blank">📅 00:32 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93619">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">أعلن الفاتيكان عن تشخيص إصابة البابا ليو الرابع عشر، البالغ من العمر 71 عامًا، بسرطان الرئة. وأكدت الفحوصات التي أجريت أثناء الجراحة إصابته بسرطان غدي رئوي. وقد استأصل الجراحون الفص السفلي من رئته اليمنى في مستشفى جيميللي بروما. تكللت العملية بالنجاح، ولم تُسجّل أي مضاعفات.</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/naya_foriraq/93619" target="_blank">📅 00:17 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93618">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">صافرات الانذار تدوي في وادي الدواسر  والسليل في السعودية</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/naya_foriraq/93618" target="_blank">📅 00:04 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93617">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/naya_foriraq/93617" target="_blank">📅 23:59 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93616">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/naya_foriraq/93616" target="_blank">📅 23:59 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93615">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0611040fa2.mp4?token=q928dInZfVcUB3wNo_iEkbJjZgNTfRvwaN61Nef3azwv8SsKtTtFm7RU5KEFkYFrj5qRXz8IppY5QhWLKU3QedhgdD-14KK82Q_dpQotyfDLU-DZs04_PNeIN-_sDFgmvaVrR9pygjXdrC2lftxdW7kdjH4kG8VVIqRmcXLY5k7pFZapSDvSwkiDesBgZo5Udw3B5SMdC3HMsDZ4MRZFnMfzqmgIwI3AXa-RxBR708Gqwr9t7O6-vEaDrxyVqlQd11OqFzARnTKM2d8QW4CkoK5aqHmRjtQO5h0hN0HMEinqIyHknNzLSUDqsILURyfkAndr5WkFp-YGhlrCkDfRhQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0611040fa2.mp4?token=q928dInZfVcUB3wNo_iEkbJjZgNTfRvwaN61Nef3azwv8SsKtTtFm7RU5KEFkYFrj5qRXz8IppY5QhWLKU3QedhgdD-14KK82Q_dpQotyfDLU-DZs04_PNeIN-_sDFgmvaVrR9pygjXdrC2lftxdW7kdjH4kG8VVIqRmcXLY5k7pFZapSDvSwkiDesBgZo5Udw3B5SMdC3HMsDZ4MRZFnMfzqmgIwI3AXa-RxBR708Gqwr9t7O6-vEaDrxyVqlQd11OqFzARnTKM2d8QW4CkoK5aqHmRjtQO5h0hN0HMEinqIyHknNzLSUDqsILURyfkAndr5WkFp-YGhlrCkDfRhQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الصواريخ اليمنية تصيب اهدافها،اصوات انفجارات هائلة تُسمع في الرياض وسط السعودية
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/naya_foriraq/93615" target="_blank">📅 23:54 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93614">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">اعتقال موظف بمستوى رفيع بوزارة التربية العراقية وسط العاصمة العراقية بغداد اثناء استلامه الرشوى .
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/naya_foriraq/93614" target="_blank">📅 23:48 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93612">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/227ecb5731.mp4?token=QCBPGRXYyjzOdyYECg3J5G1jrF7uqInXiU0Q5GxSu_j2MgjFb3j4aD5khOxMNHhR288GD8Ed_UxYM_NXAlPExyBIl_-brxzcIpfTTgZ9GapNjUHH3ub8uKMw9R19bbo-Iy-GQ65yOZ6SHDuVBKZwcqaWJfHwt9TfBJp4cpH9z8IMTNSjbLj50byIoSm3WocLaP9XR9oliz1qe6Qkn6GtgIwgXEzSBDE7cwT2WrSqAoHFOUDbA6J5Df3vnipxTiAIjkxmWCaBEbbGnp71FPSUcYac-YTExeKJvoA5MNr_ENhEao2B44K09F1TVqX6yv28a7VjUk180Ra2viy8JNCFAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/227ecb5731.mp4?token=QCBPGRXYyjzOdyYECg3J5G1jrF7uqInXiU0Q5GxSu_j2MgjFb3j4aD5khOxMNHhR288GD8Ed_UxYM_NXAlPExyBIl_-brxzcIpfTTgZ9GapNjUHH3ub8uKMw9R19bbo-Iy-GQ65yOZ6SHDuVBKZwcqaWJfHwt9TfBJp4cpH9z8IMTNSjbLj50byIoSm3WocLaP9XR9oliz1qe6Qkn6GtgIwgXEzSBDE7cwT2WrSqAoHFOUDbA6J5Df3vnipxTiAIjkxmWCaBEbbGnp71FPSUcYac-YTExeKJvoA5MNr_ENhEao2B44K09F1TVqX6yv28a7VjUk180Ra2viy8JNCFAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇦
🇾🇪
مشاهد من انطلاق الدفاعات الجوية السعودية في العاصمة رياض.  https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/naya_foriraq/93612" target="_blank">📅 23:40 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93611">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🇸🇦
🇬🇧
🔻
🇺🇸
إعلام أمريكي :
فشل ذريع آخر لقوات الدفاع الجوي السعودية الليلة! من المرجح أن يلقي باللوم على الولايات المتحدة وبريطانيا وفرنسا في ذلك!
‏وبحسب التقارير، فشلت أنظمة الدفاع الجوي السعودية باتريوت باك-3 وثاد في منع الصواريخ الباليستية الحوثية من ضرب أهدافها المقصودة.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/naya_foriraq/93611" target="_blank">📅 23:33 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93610">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/79ee8793ee.mp4?token=WdU7vJCeXER5NnYn1xIWmuvsA7xNY43xca0FUA9bv6br1VrQMAdlEWZapd9_71QMRW3jDw-Yd5Z9vwRmZpxQzpe3XdpuzrB7hjvxNntLtPG8AXQoIEASzxfilDVahad6zIg2byoxcNKSx99mJA_P7X625zdlxvK00FDWPbtppcBEspYa8YU3_t5ECLz9SFAgMy9WNQs229vk2UyA-TiqH4AifscCQVQ_f-onMl2vhoGIWwOZU8uXnQbk6vwthvPo9A1jO_bApejY6nf2W0DLvkQzKbGJN337U9GVaUxEUlKL19EbG6-Jfx8nTyDmOj91fmFT-BXOSExKJW5qs9zKVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/79ee8793ee.mp4?token=WdU7vJCeXER5NnYn1xIWmuvsA7xNY43xca0FUA9bv6br1VrQMAdlEWZapd9_71QMRW3jDw-Yd5Z9vwRmZpxQzpe3XdpuzrB7hjvxNntLtPG8AXQoIEASzxfilDVahad6zIg2byoxcNKSx99mJA_P7X625zdlxvK00FDWPbtppcBEspYa8YU3_t5ECLz9SFAgMy9WNQs229vk2UyA-TiqH4AifscCQVQ_f-onMl2vhoGIWwOZU8uXnQbk6vwthvPo9A1jO_bApejY6nf2W0DLvkQzKbGJN337U9GVaUxEUlKL19EbG6-Jfx8nTyDmOj91fmFT-BXOSExKJW5qs9zKVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇾🇪
صاروخ كروز رابع يستهدف الرياض.  https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/naya_foriraq/93610" target="_blank">📅 23:29 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93609">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🇾🇪
ثلاثة صواريخ مجنحة تستهدف العاصمة السعودية الرياض.  https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/naya_foriraq/93609" target="_blank">📅 23:13 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93608">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🇸🇦
رويترز: تصاعد اعمدة الدخان من مقر شركة ارامكو في الظهران.  https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/naya_foriraq/93608" target="_blank">📅 23:00 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93607">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🇸🇦
رويترز:
تصاعد اعمدة الدخان من مقر شركة ارامكو في الظهران.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/naya_foriraq/93607" target="_blank">📅 23:00 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93606">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🇾🇪
مصدر لنايا يمني   الضربة الأخيرة تم استخدام سلاح جديد نوعي دخل للخدمة موخراً في ترسانة القوات المسلحة اليمنية .   https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/naya_foriraq/93606" target="_blank">📅 22:56 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93605">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🇾🇪
مصدر لنايا يمني   الضربة الأخيرة تم استخدام سلاح جديد نوعي دخل للخدمة موخراً في ترسانة القوات المسلحة اليمنية .   https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/naya_foriraq/93605" target="_blank">📅 22:55 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93604">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🇾🇪
🇸🇦
الرياض تتلقى الجزء الأكبر من الرد اليمني.  https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/naya_foriraq/93604" target="_blank">📅 22:46 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93603">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e039ec716.mp4?token=jiicq4PMbl74nuv2ynBI3WEMnYKj5G3P-2mhQnUIK-LGE5ax4hBC2fAiZ5sTsKwBFI1Q9M8gK95_Iz6_HTXV0eITvSEVW8zcEt-FfL4fsLo1KoW8MwMDSE5rx7vkEwq4Gg7FCySAZFGHv_VIC2POVN_8vagaAhBj8j62PjxYs3MaHQ5RWMX91Fx2LnvsryVVNfjo7pWcV11wx7773ISYUhK-_-razZE3lqx0Ho5qp3RrRicms-puMJBqrQUFPfMUcz5iIDAS618eLwil_WNzvUB68ZTdGJ9sLP_29r5mWDQZddvwnmZS3CVsXrnoZFOb35kHuaPm18Qt1c2LE84l5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e039ec716.mp4?token=jiicq4PMbl74nuv2ynBI3WEMnYKj5G3P-2mhQnUIK-LGE5ax4hBC2fAiZ5sTsKwBFI1Q9M8gK95_Iz6_HTXV0eITvSEVW8zcEt-FfL4fsLo1KoW8MwMDSE5rx7vkEwq4Gg7FCySAZFGHv_VIC2POVN_8vagaAhBj8j62PjxYs3MaHQ5RWMX91Fx2LnvsryVVNfjo7pWcV11wx7773ISYUhK-_-razZE3lqx0Ho5qp3RrRicms-puMJBqrQUFPfMUcz5iIDAS618eLwil_WNzvUB68ZTdGJ9sLP_29r5mWDQZddvwnmZS3CVsXrnoZFOb35kHuaPm18Qt1c2LE84l5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇾🇪
🇸🇦
الرياض تتلقى الجزء الأكبر من الرد اليمني.  https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/naya_foriraq/93603" target="_blank">📅 22:39 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93602">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LOryk7ehNGinoVTwPzj9IFCyy3tkIpDRkvHg_XfS9VS13lYcqIquPES3BK-oKYNN8y7598f4SnoiiIewi6CeOfJFKtHoBKuM0M1_RccR2uDilENLj1E1Fulj9wc7pltcEBxmZap6LxrkWUmYpWAeLW3dzemzcqHIQaF_mDSgMhHkr_JESfJZv-OCB2ONZ9F30DcS13aZllwD-pTtkivxd1QLeswi4SMlvay4kUgPwquMAIDtdIA0BBlzcfaFDlN27dY_CIQM0pAXEise-zMbU9Bat0YWwD2XX7eC2C_OgNDQ_FzDkMULOx_dQxwXlJihXrZcJsu1mXpcIoIqx6uR2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استهداف سفينتي شحن في مضيق هرمز.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/naya_foriraq/93602" target="_blank">📅 22:32 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93601">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9e74ad2dea.mp4?token=VP45G29sJVKRF_PVKOZ0U-FyaaH_W9jUAN3qtBOhezVLocJ3wJelit4VVR7px9NS-JkwLyR74xQh5C1_9UEAfmTbWjRe2jN8_erhI9qeztMsLXvCkffiDO3CBaq80chkZN7eXKlSvjzw7tfAkYXCWpZM1TriQdmieVHtyTX5ldlseDzSIo-aUG5ymZiSro5T4RTkGZDaOoV5_iSt-QnJnXNc8Y25OytoftFHopC3mMcSFX8od2petKDXZ02pqMl0IU4wRM_W7VA7gzYuwqw5hlmh8MC9qnNWieEpwvSDEVbxvoMJQZ6dFCQRv11DP032if9uA5oTRTMNkhKp6qpsnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9e74ad2dea.mp4?token=VP45G29sJVKRF_PVKOZ0U-FyaaH_W9jUAN3qtBOhezVLocJ3wJelit4VVR7px9NS-JkwLyR74xQh5C1_9UEAfmTbWjRe2jN8_erhI9qeztMsLXvCkffiDO3CBaq80chkZN7eXKlSvjzw7tfAkYXCWpZM1TriQdmieVHtyTX5ldlseDzSIo-aUG5ymZiSro5T4RTkGZDaOoV5_iSt-QnJnXNc8Y25OytoftFHopC3mMcSFX8od2petKDXZ02pqMl0IU4wRM_W7VA7gzYuwqw5hlmh8MC9qnNWieEpwvSDEVbxvoMJQZ6dFCQRv11DP032if9uA5oTRTMNkhKp6qpsnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجارات تجدد في الرياض  https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/naya_foriraq/93601" target="_blank">📅 22:31 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93600">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t7zVT27MGEJcjVNtBh7ekzm3p0cQ3MTIJ4gcgzDPyZehGMv2l3a-LgILEhqpfV0KA50YaleYItltJ5VZ9yQ-ekxeVmY5_oGJUYWxFUvdfStJ_2HDky_GDbwgSRyF2_1CAAcEFoTlAvpPDlkpAU84Yrl4XWyHAh_RS3KRCmoF3rFmtPCOaZQjBAAMW9vASXyX3Kh7ux4DbqTx2dei_NvVJZEYogjzy3bPRFBJQAbmWnfi_n9vjarX83CmDUjaevNQdSukwdc08B5YTm2onboyyCZ91yoz0TpxJ_4P6QT1c3uZzodA-DHw-gydnlpsNmpjP7gOMivBUiHeLbQ8nv58UQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد تركيا وباكستان وبريطانيا واوروبا ومصر وكمبوديا وبوركينا فاسو واوغندا.. وزير الدفاع السعودي يطلب الحماية من بولندا !</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/naya_foriraq/93600" target="_blank">📅 22:29 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93599">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🇸🇦
🇾🇪
توقف العمليات الجوية في مطار فهد الدولي بالدمام</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/naya_foriraq/93599" target="_blank">📅 22:27 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93598">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a07e6ef21d.mp4?token=PNmyMjPkQ-KGEQ3tSV0E9VXev1uyRi1gjH-a4CrpAIqeVA8GqmHdJpCdSWh8vNSAhBskaqOKWFEJ2hisJU5YGJW05BDjEPEdmkVwouuFR0RZHsP6p83XSZwVYGarRi0dyIp166maQM4WeMuJKC6GA18MihAGWdteo_HfXaZeFA35gyrq7LFbPGq7tJuq2Z2XXqFy4PQm6pnOvjQHaCEWaGcI6LdZl-95z2bz2r3HaYrkIZdmx0flh3jsY7gu92gRhERQxWpSw1mqnz2fWIvRRJAImBgyYzMiNU4yOEm6_AzJooDlD8DcO6I3j7gutuedYms6mOgNUwyCQ9mHRJPT2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a07e6ef21d.mp4?token=PNmyMjPkQ-KGEQ3tSV0E9VXev1uyRi1gjH-a4CrpAIqeVA8GqmHdJpCdSWh8vNSAhBskaqOKWFEJ2hisJU5YGJW05BDjEPEdmkVwouuFR0RZHsP6p83XSZwVYGarRi0dyIp166maQM4WeMuJKC6GA18MihAGWdteo_HfXaZeFA35gyrq7LFbPGq7tJuq2Z2XXqFy4PQm6pnOvjQHaCEWaGcI6LdZl-95z2bz2r3HaYrkIZdmx0flh3jsY7gu92gRhERQxWpSw1mqnz2fWIvRRJAImBgyYzMiNU4yOEm6_AzJooDlD8DcO6I3j7gutuedYms6mOgNUwyCQ9mHRJPT2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">النظام السعودي يهدد من يقوم بتصوير مواقع سقوط الصواريخ بالاجراءات القانونية
طبعا الاجراءات على طريقة خاشقجي</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/naya_foriraq/93598" target="_blank">📅 22:24 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93597">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🇸🇦
🇾🇪
توقف العمليات الجوية في مطار فهد الدولي بالدمام</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/naya_foriraq/93597" target="_blank">📅 22:24 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93596">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">انفجارات تهز الرياض  https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/naya_foriraq/93596" target="_blank">📅 22:21 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93595">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">مقرات شركة ارامكو في الظهران تتعرض للقصف  https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/naya_foriraq/93595" target="_blank">📅 22:20 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93594">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">سماع دوي انفجارات في مطار الرياض
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/naya_foriraq/93594" target="_blank">📅 22:15 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93593">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">استهداف مصفاة الرياض  https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/naya_foriraq/93593" target="_blank">📅 22:14 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93592">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">استهداف مصفاة الرياض
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/naya_foriraq/93592" target="_blank">📅 22:14 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93591">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">الرياض وما بعد الرياض
لبيك يا ابو جبريل</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/naya_foriraq/93591" target="_blank">📅 22:14 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93590">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromنايا - NAYA</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Audio</div>
  <div class="tg-doc-extra"></div>
</div>
<a href="https://t.me/naya_foriraq/93590" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">قولو له الرياض اقرب</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/naya_foriraq/93590" target="_blank">📅 22:13 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93589">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">انفجارات تهز الخبر المنطقة الشرقية من السعودية المحتلة .
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/naya_foriraq/93589" target="_blank">📅 22:12 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93587">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">انفجارات تهز الرياض
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/naya_foriraq/93587" target="_blank">📅 22:10 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93586">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">صاروخ باليستي يستهدف حرض
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/naya_foriraq/93586" target="_blank">📅 22:10 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93585">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">الرد اليمني بدأ
المحطات بالمحطات
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/naya_foriraq/93585" target="_blank">📅 22:07 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93584">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Audio</div>
  <div class="tg-doc-extra"></div>
</div>
<a href="https://t.me/naya_foriraq/93584" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🇾🇪
نقسم برب العرش
#شاركها</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/naya_foriraq/93584" target="_blank">📅 22:07 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93583">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">الله اكبر
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/naya_foriraq/93583" target="_blank">📅 22:06 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93582">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">منشأت ارامكو في المنطقة الشرقية السعودية تحت رحمة صواريخ القوات المسلحة اليمنية  https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/naya_foriraq/93582" target="_blank">📅 22:06 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93581">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🇮🇷
🇬🇧
استدعت الخارجية الإيرانية السفير البريطاني في طهران، ردًا على اتهامات بريطانية نسبت حادثة مزعومة في قاعدة «فيرفورد» العسكرية إلى إيران.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/naya_foriraq/93581" target="_blank">📅 22:00 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93580">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bBzO08Mv4AdAMVpBk9Npfmt13siKjc0tqQH2I2-1pv4YHxc9kT2MSmOwwGttsz2w-ZeoRGKhQeDnjsvnt-M78jKTwxqZ4UTY5GB43XigPnd_CPF9N4vKcVzL9wQKaA8Py29Mv6EOxEDkKpROq-c78m_yb05yluugfAUT59xaczRkK4KUZfZ_4yCig8xEp12AH-w8rWylkOR8XZ5GPYrWnalV0mlcTp4sIIfGdWtPyLa99mknoGgiFmF74fFAExdbaX5HBISMxqprNyt3OQsCV4sYUg16zXUOODfrpFw8qRDe9pJmcjydixthuZaSEjX4TBS3_2jRpgTVV9_c0db6Hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
الرصد اليومي لطلعات العدو الجوية التي يخرق بها السيادة العراقية.
يستمر العدو في انتهاكه الصارخ لسيادتنا الجوية، انطلاقا من قواعدهم في الأردن والاراضي المحتلة.
- طائرة (KC-135) عدد 1.
- طائرة (MQ9) عدد 1.
- طائرة (E-11) عدد 2.
- طائرة (MQ1) عدد 1.
🔻
يوم الاثنين 12-10-2026
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/naya_foriraq/93580" target="_blank">📅 21:58 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93579">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">منشأت ارامكو في المنطقة الشرقية السعودية تحت رحمة صواريخ القوات المسلحة اليمنية  https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/naya_foriraq/93579" target="_blank">📅 21:45 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93578">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/naya_foriraq/93578" target="_blank">📅 21:20 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93577">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/naya_foriraq/93577" target="_blank">📅 21:20 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93576">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🇾🇪
🇸🇦
السعودية تناشد المعنيين داخل انصار الله:
يجب على الحوثيين الوقف الفوري لكافة العمليات الإرهابية والتي تستهدف المدنيين والأعيان المدنية بما فيها المطارات والموانيء والمنشآت النفطية والبنية التحتية.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/naya_foriraq/93576" target="_blank">📅 21:16 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93575">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">سوالف الگهوة
بنكين خارج منصب نائب رئيس الوزراء ؛ الحجي العامري زعلان بسبب الدفاع و مشارب الجاي في اجتماع الاطار ..</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/naya_foriraq/93575" target="_blank">📅 21:15 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93574">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/naya_foriraq/93574" target="_blank">📅 21:09 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93573">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🇾🇪
العميد يحيى السريع:
شن الطيران الحربي السعودي خلال الـ24 ساعة الماضية 104 غارات جوية وصواريخ، استهدف بها الأعيان المدنية في العاصمة صنعاء ومحافظات ذمار وتعز وعمران ولحج والجوف ومأرب وصعدة والحديدة من خلال طائرات "F-15" و "تايفون" أقلعت من قاعدتي خميس مشيط والطائف، والعدوان الصاروخي من نجران، وخلفت شهداء وجرحى من المدنيين.
ليبلغ إجمالي غارات العدوان السعودي منذ بدء التصعيد على بلدِنا 2281 غارة جوية وصاروخاً.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/naya_foriraq/93573" target="_blank">📅 20:02 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93572">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U4CWLagTG7ve5KSigUPJMmYiRtKOYXauwCI37In5KCCvjoasCnH43YU_AHGivgvQDBnTJTtPzL-9CjMFgXlFpvWlI3nxv4WteQJM7RZ_9OKcKqATmJp9fM958aaZcg1ISc4L5Z10qFMvHW6eJcQhATsQ8cu9XFcO4dzn4_x31QFaWSw6t0lEEIS1zf5U-AVIIL2guvD7LVMVfVJdvm8GfBMoJro4h7ObsHKxyjlwTmpyjtGszg-hgTILdDmTQMT8WcfNtNUdsIU87Jy1Mk4qPvbjpi5bS4Yr-OdcnEWK1GU_V8x-fMq-tHGeKg4qb0eK7Q48K6xetOq9zMad2A0xsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
‏ترامب: الحوثيون يتصرفون بشكل سيء للغاية،نعم، لقد تحدثت مع ولي العهد السعودي،ربما اطلب من تركيا التدخل في اليمن.  https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/naya_foriraq/93572" target="_blank">📅 19:35 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93571">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/845c9be631.mp4?token=R-FEB0M9OBiRDVFmenaRMxIDT1_eJxDaE4vVB9EM_UvoqKT2nusaVeeWZ6hh2xP2qOzHgn6Xbii6-SQHxNzwRE3ZliVW5ZBhn-mVWzXNwCqlU-oon7a_PNOFIOYvVmRitozO2EUPSihTU35hNoXL2F8oN8jDGsWkOM9aq6D4SRoM0TSW-hpE5NLMRqEM9MwuTY1JxDSpdYdNV9gT7AxVnRBXirTXfjtxIoBGEuf74-ssd9MQo1zI4AGTYSbkph6q6bsy6jgZ3Ow8WmYQJLXTA8aGGw7bSDL6d-DulmVeavs1s8CZUBpsZTs7iaxs0K-hEokwpiRs9MDHuINePODmGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/845c9be631.mp4?token=R-FEB0M9OBiRDVFmenaRMxIDT1_eJxDaE4vVB9EM_UvoqKT2nusaVeeWZ6hh2xP2qOzHgn6Xbii6-SQHxNzwRE3ZliVW5ZBhn-mVWzXNwCqlU-oon7a_PNOFIOYvVmRitozO2EUPSihTU35hNoXL2F8oN8jDGsWkOM9aq6D4SRoM0TSW-hpE5NLMRqEM9MwuTY1JxDSpdYdNV9gT7AxVnRBXirTXfjtxIoBGEuf74-ssd9MQo1zI4AGTYSbkph6q6bsy6jgZ3Ow8WmYQJLXTA8aGGw7bSDL6d-DulmVeavs1s8CZUBpsZTs7iaxs0K-hEokwpiRs9MDHuINePODmGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
‏ترامب: الحوثيون يتصرفون بشكل سيء للغاية،نعم، لقد تحدثت مع ولي العهد السعودي،ربما اطلب من تركيا التدخل في اليمن.  https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/naya_foriraq/93571" target="_blank">📅 19:14 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93570">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/09b1cdcb24.mp4?token=aTKjmAVPcS5QRWh-Y0t3JkzYukG8mTMn9_HRSsoqNHNsXWFUTHFdFYRWYrdNP6kdTcYwI0S1jrQ35lXp1UWWp0QEfwxw3ttNNuNZa4mGoYNU3Ga2o7gvt8SoKKM4Ld3T_DlvRTdlS2KYA7N0YAnDFVTU6gNvScv5s4e5a6X1-nNVEVQ0yJ78_gctkvuQ6laHWAEAFaVukddwacUWOFJkLnrbZvty9LPDXcNIjbgOrAXfu3qq4rUWWQRU6VjUgof2enQ0UzagN5gG1htyn5TzAyFkjVbz6h73hQh_e2ngn_IbgCDlvGaXdGd9CYlTrbGdRpJvcSrkn7Avih_Mv_QQZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/09b1cdcb24.mp4?token=aTKjmAVPcS5QRWh-Y0t3JkzYukG8mTMn9_HRSsoqNHNsXWFUTHFdFYRWYrdNP6kdTcYwI0S1jrQ35lXp1UWWp0QEfwxw3ttNNuNZa4mGoYNU3Ga2o7gvt8SoKKM4Ld3T_DlvRTdlS2KYA7N0YAnDFVTU6gNvScv5s4e5a6X1-nNVEVQ0yJ78_gctkvuQ6laHWAEAFaVukddwacUWOFJkLnrbZvty9LPDXcNIjbgOrAXfu3qq4rUWWQRU6VjUgof2enQ0UzagN5gG1htyn5TzAyFkjVbz6h73hQh_e2ngn_IbgCDlvGaXdGd9CYlTrbGdRpJvcSrkn7Avih_Mv_QQZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
‏
ترامب
: الحوثيون يتصرفون بشكل سيء للغاية،نعم، لقد تحدثت مع ولي العهد السعودي،ربما اطلب من تركيا التدخل في اليمن.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/naya_foriraq/93570" target="_blank">📅 19:06 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93569">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🇮🇶
العراق يوجه برفع مستوى الجاهزية القتالية لقواته المسلحة إلى أعلى المستويات.</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/naya_foriraq/93569" target="_blank">📅 18:22 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93568">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0e752ab5a3.mp4?token=FjCQuf39IWuVgn9BotVm7iyhdnurmxhWBY-dTTIFH3TGoKPrcFjdXrmeI_vXSE-LSTfnotNLtiq4SguHGMB_0yNQOUqlYzbJgcaHPW9r8qzKcFNb9Fg7vzCJYEyeRQRheswH0yBGlJ6bmsPiBnNC08aiGQyqPY-vJM4uLJKDjH4HKMpr5E8IKt9OaCaqV1v60lbX5t3KEKt_PqbSS0tWRiyO6zX5CfsSWTVunSnjCP3B1Mwe5MJ5LLIJRSE8HZ36NJXEpmDH7-N0nhlRDD6gY8BEZJ7cmGMEFEtNX2MilcgCb90nj34XYPHTkIpqNNXc8X_Rp4tmcZt8uNrUVSVYnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0e752ab5a3.mp4?token=FjCQuf39IWuVgn9BotVm7iyhdnurmxhWBY-dTTIFH3TGoKPrcFjdXrmeI_vXSE-LSTfnotNLtiq4SguHGMB_0yNQOUqlYzbJgcaHPW9r8qzKcFNb9Fg7vzCJYEyeRQRheswH0yBGlJ6bmsPiBnNC08aiGQyqPY-vJM4uLJKDjH4HKMpr5E8IKt9OaCaqV1v60lbX5t3KEKt_PqbSS0tWRiyO6zX5CfsSWTVunSnjCP3B1Mwe5MJ5LLIJRSE8HZ36NJXEpmDH7-N0nhlRDD6gY8BEZJ7cmGMEFEtNX2MilcgCb90nj34XYPHTkIpqNNXc8X_Rp4tmcZt8uNrUVSVYnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">القوات المسلحة اليمنية من مداخل مدينة تعز والتقدم مستمر</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/naya_foriraq/93568" target="_blank">📅 18:21 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93566">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">اعلام العدو: المشتبك مصاب</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/naya_foriraq/93566" target="_blank">📅 18:09 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93565">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">انباء اولية عن استشهاد المقتحم</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/naya_foriraq/93565" target="_blank">📅 18:07 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93564">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">اصابة صهيوني بجروح خطيرة كحصيلة اولية</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/naya_foriraq/93564" target="_blank">📅 18:05 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93563">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">انباء اولية عن استشهاد المقتحم</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/naya_foriraq/93563" target="_blank">📅 18:04 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93562">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">اشتباكات مسلحة في مطار رامون</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/naya_foriraq/93562" target="_blank">📅 18:04 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93561">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">مسلح يقتحم مطار رامون الاسرائيلي</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/naya_foriraq/93561" target="_blank">📅 18:03 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93560">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">مسلح يقتحم مطار رامون الاسرائيلي</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/naya_foriraq/93560" target="_blank">📅 18:02 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93559">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">رويترز عن مصدر دبلوماسي تركي:
اتصال بين وزيري خارجية تركيا وإيران لبحث الجهود الجارية لحل النزاعات الإقليمية.</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/naya_foriraq/93559" target="_blank">📅 17:58 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93558">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/87f5f511f2.mp4?token=su3mil2WhKCLALyGKMOpf9pbk6qMO8Wz2ediSpT7hfrI116l4C-SawORYbgmhFQQ8HH1tO0Lrofb5C5LLCqkvu5irzXl6i5c0Z4WSLaj_bvfM9GCSl_qkm6vAOO2fMUXTWN3MuKuZMcLWLV-1ShT8K0_ipdpVQ41LJlAnnz-kR_Rk8TE09fBNgTQ8LRODIxJPqv09jt_2P-NTW_G0yyYBIQ4rpjzvuMz0DzBg0aXR6HocHx3QmcPGPgdkI8misovkBuYta1d87WhQNIqK1HbdwuDSnqK75cbiv_SkkQ-eX_suM-e19expzaRio8caqUDB-WD8f-kX1B34WWJXxhu-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/87f5f511f2.mp4?token=su3mil2WhKCLALyGKMOpf9pbk6qMO8Wz2ediSpT7hfrI116l4C-SawORYbgmhFQQ8HH1tO0Lrofb5C5LLCqkvu5irzXl6i5c0Z4WSLaj_bvfM9GCSl_qkm6vAOO2fMUXTWN3MuKuZMcLWLV-1ShT8K0_ipdpVQ41LJlAnnz-kR_Rk8TE09fBNgTQ8LRODIxJPqv09jt_2P-NTW_G0yyYBIQ4rpjzvuMz0DzBg0aXR6HocHx3QmcPGPgdkI8misovkBuYta1d87WhQNIqK1HbdwuDSnqK75cbiv_SkkQ-eX_suM-e19expzaRio8caqUDB-WD8f-kX1B34WWJXxhu-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اشتعال سفينة نفطية مخالفة في شرق مضيق هرمز</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/naya_foriraq/93558" target="_blank">📅 17:50 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93555">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/So9kde9fE32s-AFFgTH6nwM7CHvLjBd_bs6Wa65yJMT2GwfVvGhxSqIM1O6G5PFP_v204hG0rwHiBf4cOo0it2Sxw2oq2hHYN0r03gJLwDhurxvDQZ9vw-EQ9BM6jkA-PiVmILgU89vMohVTX45xRZIlDGMxfh39EUAuMPJQbG_Yn2MrLfsmPR8J2RrQah1xzCHBt5oaNw_M_Jy0dTVMkc54WoMG1_-Fj1v8aLA20MM26DYEl5S03O-uEoXzkGgnX1f4MHeLClWp6xXbP3ctriPlEl2q3Plk6_UVK8WXWB3A2s_S4qV0-jnEg3i6Z2jSBUmWP7HOqriNgSNVQiIHwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OiT7oM6BKocePqFA9WGOO8vFgtQjV5SzHYuVFRnTdpJFKqwLrNwSVqSviNlO3IIyCqTS68x_vtokCwYqnCHwjgZCQ5iV4iGNKS5UcQM07SgjoW1ecZSNUzyFn7XAY0dO_ew2qzvjRAGuYTeS8aQwl3B_H3IxupjU7OdV6TUT7YLs7FJXkQJUuwzxR74CFJD_22h2nGQ5yY7qIIgMF0Xl3AhJotf1zzzSANFXoFidWE92D-sd7FYLOX3cdqaxSMiLV9o-iaxzd-6-H6ERRfXOH4unUlLDsz_kZcKjsfCaprqRWVq02iGpsQU5qeBXjIKGjifQwUOQVDB42qZeoHqAAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HGRuU_hWG3YN5WKd_DvnGRW_PpcR_7Zj7bFw-0kyaxs9MHj7wciF-3UyP5eEo_Xe1dIHXUYFMwrpVCVAKp0W7b7H8-q19dK-UauEhlH4NIrHYxrl9Gt5mvU6OIUI9wFPLrMtqQXYozIwKVIsjgWRQlqKgjS2VjJ0chcKpNrmVeTRhQhsIkKrkju7ME4TkwVh6UtyFtwTqlnbXg6hKCUUa_VEgy0HIi3xu-SveKm5zchiuRtWfWVKj_Oercx-G8rFrky4X32Nz8gXLL-UbXATvjJ9if77ZIzyAjueznjL1bftcn5EFIIpe-NfC4RgbzD4hNAO5SzeNECnpUEnmzDdcw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">القوات المسلحة اليمنية تدعو لاخلاء عدد من الاهداف في السعودية</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/naya_foriraq/93555" target="_blank">📅 17:48 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93554">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">انفجارات تهز مضيق هرمز</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/naya_foriraq/93554" target="_blank">📅 17:47 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93553">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">انفجارات تهز مضيق هرمز</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/naya_foriraq/93553" target="_blank">📅 17:47 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93552">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f2Rau3-lvhTaHshg7vXpOmCDBUsJLX5PF2ONIz7qJY3qxtjjTLQUrOsNLQ0w6_4suJGMTFy2vxi9cEjWKRMWM1Sh1QGUAHI1b8JI1GiIwvf_hiC_JQd-xRqj6lNhemdT8TC2mYd0B_yYLrbO_WP8jcfqjlbgOHgiXtuePFp59y5tpPiGn6j51k9p8rSlPenmkyigmERyux1Fsn4eLnQZQRqVGZIVMjb6z9_MwZauUQeEu7LlFdS-WH66jfPe2lBCANnUJ1agHplgF8jHZZSd1qan4ZxWGNI43tL6UUGBlyDYm3JZmiJdtDkTlLS5CQwCDQIevpeOOhJwoV01mFKyTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">القوات المسلحة اليمنية في مداخل تعز</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/naya_foriraq/93552" target="_blank">📅 17:44 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93551">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🇾🇪
🇾🇪
العميد يحيى سريع:
قواتنا المسلحة تتصدى في هذه الأثناء لتشكيلات العدو السعودي القتالية التى تستهدف العاصمة صنعاء.</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/naya_foriraq/93551" target="_blank">📅 17:29 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93550">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🇾🇪
🇾🇪
شركة النفط اليمنية:
تؤكد شركة النفط اليمنية أنها اتخذت مسبقاً كافة الإجراءات والتدابير الاحترازية اللازمة لمواجهة أي طارئ، بما يضمن استقرار الوضع التمويني في المناطق الحرة واستمرار تلبية احتياجات المواطنين بصورة طبيعية.
وتوضح الشركة أن منشآت الصباحة لا تحتوي على أي مخزون من المشتقات النفطية في الوقت الراهن، وبالتالي فإن استهدافها لا يؤثر على المخزون النفطي أو الإمدادات التموينية، حيث تتوافر احتياجات المواطنين من المشتقات النفطية في منشآت ومواقع آمنة، وبكميات كافية لتغطية الاحتياجات لفترات طويلة.
وتطمئن الشركة المواطنين بأن الوضع التمويني مستقر تماماً، وأنها مستمرة في اتخاذ التدابير اللازمة لضمان استمرار توفر المشتقات النفطية وعدم تأثر احتياجات المواطنين.</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/naya_foriraq/93550" target="_blank">📅 17:27 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93549">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">انباء اولية عن سماع دوي انفجار في صنعاء</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/naya_foriraq/93549" target="_blank">📅 17:22 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93548">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">انباء اولية عن سماع دوي انفجار في صنعاء</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/naya_foriraq/93548" target="_blank">📅 17:17 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93546">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/R95S-2zGdV4AqWSXe47sk5M-bnv7F0D3p9bPy26nDi4R1YNyIb8hU1pl45UCtwGADEMQQ2MwsAVj_a_4GjDUGZmuGsgkcPXzoY2wr3ASoKcKYM_HMnY6ouWuQLTuUZ16jQI5wyUDoH2Ar5JYUJgQh7sKaGWeNiMBOAul21yGmTR7iYTskDGDOalUwx4zpTahyWqzAUP4ECIs-LdZm0m1tSAOfFrHM8klQ_C6e_kMAYh03ak1azcpFa7igJiN_rVewZqK7f5SzAwm56d-egRiX7T3K9-1d9h-SxyxKLFWkJgQTTgTCOg8x2Cwp0zRQwVSJJOb9pvQFzGpjqltT5rVEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fYjeiTvtWbc3Tt30Wkn7ixdGKAf_MpubFTasTdGs6BJCft3OZysz3SeQsKXnvfELMQmp1-WHXBfRH9_0UCGk8oJEHBlupxtFfQi7c4QRsf199sWwEQAFrZGmRPQToG1aRVsooyrEkfRQEnTayHJG9NwrjvtPI_DqNQdO3W9kn3zP_YYMJmJqp45Xyrs1x0Z3FJiBThxZgKyiK5OKycVf6V7JBd9hhBJXGUrA6u-8Zpt7e7QWSO3ONdVNdUwMltXTesP2saAca9fLDclgp0Tj9LDB39chNZwjL7ai-Nd4DS-Ffoq0fCsuZUSiRFJQFwCVbYZkFfRwfE-ZKeRDkusahw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">تجدد اضطرابات الرحلات الجوية فوق الإمارات لاسباب غير معروفة</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/naya_foriraq/93546" target="_blank">📅 17:16 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93545">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd6a89816f.mp4?token=cMnVNak-ntWXgp_tUDJGnd1oNrCqt9fvBwLoqSyEoVFIa5yRt5_G0dfKl8OBT_SmarkyydPBziR3xDEzLXFzVwcLKMIgXm6oTLL7zYOwpiYM1z08RbpyNTsseyRFfPV-xwv3mxRHCbBHOKFC04PCmDKe-VfNWyl1k-g6lFoX0IKV15x5W0IfSxGzREkGHku6l9gBKw7nibwZZvVFixL9UhZgITjBW46quD_Qnt8JcVDsoWGYMAui3HgbDW4G7fs-CpI2oBsQTroC6gz7ZDjF5S-SaJ_fsJ5dQurOV1crAuPyNiG-7uIrFdHaUHMLmMFzb49os1e2J3kNlHI3LCPcf4JLNgurTci4Ps_Zu0Z5zUat27oUd_2Y4RPy4xuiBstfRKhD49bvE2mQjbE4wQ9ktrIvPh8QnBAOf9LGRDU8goO5VEkQqVHpAHla-Z0vsQXhddQlIoZjPiCQA9SMA5FobcnLqfN5L7Lg5407rtHY9EiBUFII7QkWZX7tFOXt5yfrv-5U_SGM-awrnRipysOQdJqPNRPqvu2kYjvjPubq6mx68oHIr_LVLyfnJXgBoAXYJsye8ucgQ6AWGkMZCi8bSrVWns7OxFrelEwSbgThS_FUNh895r2zX75ZPotTg00aJAaH-mpN7VcKziT3X0hiqodJJK-GBeFxK-8T7Wngb5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd6a89816f.mp4?token=cMnVNak-ntWXgp_tUDJGnd1oNrCqt9fvBwLoqSyEoVFIa5yRt5_G0dfKl8OBT_SmarkyydPBziR3xDEzLXFzVwcLKMIgXm6oTLL7zYOwpiYM1z08RbpyNTsseyRFfPV-xwv3mxRHCbBHOKFC04PCmDKe-VfNWyl1k-g6lFoX0IKV15x5W0IfSxGzREkGHku6l9gBKw7nibwZZvVFixL9UhZgITjBW46quD_Qnt8JcVDsoWGYMAui3HgbDW4G7fs-CpI2oBsQTroC6gz7ZDjF5S-SaJ_fsJ5dQurOV1crAuPyNiG-7uIrFdHaUHMLmMFzb49os1e2J3kNlHI3LCPcf4JLNgurTci4Ps_Zu0Z5zUat27oUd_2Y4RPy4xuiBstfRKhD49bvE2mQjbE4wQ9ktrIvPh8QnBAOf9LGRDU8goO5VEkQqVHpAHla-Z0vsQXhddQlIoZjPiCQA9SMA5FobcnLqfN5L7Lg5407rtHY9EiBUFII7QkWZX7tFOXt5yfrv-5U_SGM-awrnRipysOQdJqPNRPqvu2kYjvjPubq6mx68oHIr_LVLyfnJXgBoAXYJsye8ucgQ6AWGkMZCi8bSrVWns7OxFrelEwSbgThS_FUNh895r2zX75ZPotTg00aJAaH-mpN7VcKziT3X0hiqodJJK-GBeFxK-8T7Wngb5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">أمير دولة قطر
: انخفضت الإيرادات الإجمالية بنسبة 42٪ في النصف الأول من العام.</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/naya_foriraq/93545" target="_blank">📅 17:12 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93544">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/68b06ae644.mp4?token=PTwt1RHggurQvoXs2tn2DMQ38KjN63B8sRg4qyffNeG_6vkqg34Nt66YmiSbrMypwX9ewBIUD0pZCm_1hl2bGyUdrxOSrh9P5r2_04P5gtSWFIgi0R3ANUYPjPB6sbcZdl41nVvSRqOhKeYvOMuvio5pqKfDRXRurSqv7z8mZj7Dw-D3h4Zmxjlx0OBWh8w-W3x8jmsxqUgPe-kQfF1HJqizoX3ykCbkQkrZVdp_Z28uya8Jhe4mQKdqDQMmEMAtfsAOYA-EwMUtJxecnQacnV1LBTi2RABd9vpPCpQelDKVEvio2InaXIuhlP_KaCRV1wgubOBLa94KW_zWamSb0WE2Wr-l8xlX0oMhz4ac4bDT9ZGEN5OTLwgR818MVRF1XBKKode8J_LHYDamc1DjKta9NBFrbQTfyv_wUQeIEWq0iWQqNKaBbM7BrmCewQu-DPQpZwYC3XLv4_Qr2iym6YY821jE25oES1EPLumFTcwDmEV5KOMmnyfD3xJziqthsZcuuOuoDfPPZ8h275cNAlbvcNyXX3Ifq7L7Ps6kdE1FqeRA5noIsJPx2K-fwMorsETOHevE_bDVhcsycXFJZyFzEw-8z_TeZU2PtpgRGcqEhuW1DWVDswj8mof7gCmHrBUTsiR74aa8BsTyh_ehDeAzp4NRDgHv0VgrReBlGyU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/68b06ae644.mp4?token=PTwt1RHggurQvoXs2tn2DMQ38KjN63B8sRg4qyffNeG_6vkqg34Nt66YmiSbrMypwX9ewBIUD0pZCm_1hl2bGyUdrxOSrh9P5r2_04P5gtSWFIgi0R3ANUYPjPB6sbcZdl41nVvSRqOhKeYvOMuvio5pqKfDRXRurSqv7z8mZj7Dw-D3h4Zmxjlx0OBWh8w-W3x8jmsxqUgPe-kQfF1HJqizoX3ykCbkQkrZVdp_Z28uya8Jhe4mQKdqDQMmEMAtfsAOYA-EwMUtJxecnQacnV1LBTi2RABd9vpPCpQelDKVEvio2InaXIuhlP_KaCRV1wgubOBLa94KW_zWamSb0WE2Wr-l8xlX0oMhz4ac4bDT9ZGEN5OTLwgR818MVRF1XBKKode8J_LHYDamc1DjKta9NBFrbQTfyv_wUQeIEWq0iWQqNKaBbM7BrmCewQu-DPQpZwYC3XLv4_Qr2iym6YY821jE25oES1EPLumFTcwDmEV5KOMmnyfD3xJziqthsZcuuOuoDfPPZ8h275cNAlbvcNyXX3Ifq7L7Ps6kdE1FqeRA5noIsJPx2K-fwMorsETOHevE_bDVhcsycXFJZyFzEw-8z_TeZU2PtpgRGcqEhuW1DWVDswj8mof7gCmHrBUTsiR74aa8BsTyh_ehDeAzp4NRDgHv0VgrReBlGyU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">القوات المسلحة اليمنية في مداخل تعز</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/naya_foriraq/93544" target="_blank">📅 17:05 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93543">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5be32e104c.mp4?token=PQNEgCUz5sEEUcZewi7AdiTor2J7vj6OF5dr_-eK5viy_3Q18UkflN3-wBsAPuA5Wot9Tc3_RRmEsbxbDJcigqEDoI81H0SRBbPeyLJ3lmMkvLFNnDjUt7iQ8KXADK00Gi7fDt-ezIlVNByhAvCfWWp34l_JP5Aau3-qgyf7aADJRdpE4hLOFCfmSP8Y0MLhP4MGh1n6_orxJSEn5J9YJsJM6BmqlkaVnstcYYLO25gAvJhzHMw1yHufTLZXJVjbJbJBYOiCnHvjY8NPYVNuolC03xGRKTE8q8zcD7EK73y1O-npYw2UFEVeiDWxcnBkDSm7AoKq1QxyzUhmq1eN_lwJDST9NuB1lVBYKODADYTH3Yj9eOSyBq4YsYFYiyHslciBb_TRAww4C1iiG1fXA3xt-WRKyMdyiTncRR2dUq5ESVPjUJZh1K5gf99xnDjX_elOZcCK32iCXFCTgnWx2RuPCDq4V0xif8qrzVGjiIbLmPqBZNxoJHRYujZ58FDcWfOjWkbo3i2J5XNkEbAcf2hEwOpqOPapHoEnWPGnoskIrBWVc3iN2sGew0Nxjn0iiQI5h9y4_B6vW9LWu2FCIt_YHTKAXCAnR6UGc6Iy5UY9Uh2jhn9p_RlWT9LnXhHAMzbqcpyCAvlDn4IdmvzG4bK1ZvOdqMCxDgTkRdiWF68" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5be32e104c.mp4?token=PQNEgCUz5sEEUcZewi7AdiTor2J7vj6OF5dr_-eK5viy_3Q18UkflN3-wBsAPuA5Wot9Tc3_RRmEsbxbDJcigqEDoI81H0SRBbPeyLJ3lmMkvLFNnDjUt7iQ8KXADK00Gi7fDt-ezIlVNByhAvCfWWp34l_JP5Aau3-qgyf7aADJRdpE4hLOFCfmSP8Y0MLhP4MGh1n6_orxJSEn5J9YJsJM6BmqlkaVnstcYYLO25gAvJhzHMw1yHufTLZXJVjbJbJBYOiCnHvjY8NPYVNuolC03xGRKTE8q8zcD7EK73y1O-npYw2UFEVeiDWxcnBkDSm7AoKq1QxyzUhmq1eN_lwJDST9NuB1lVBYKODADYTH3Yj9eOSyBq4YsYFYiyHslciBb_TRAww4C1iiG1fXA3xt-WRKyMdyiTncRR2dUq5ESVPjUJZh1K5gf99xnDjX_elOZcCK32iCXFCTgnWx2RuPCDq4V0xif8qrzVGjiIbLmPqBZNxoJHRYujZ58FDcWfOjWkbo3i2J5XNkEbAcf2hEwOpqOPapHoEnWPGnoskIrBWVc3iN2sGew0Nxjn0iiQI5h9y4_B6vW9LWu2FCIt_YHTKAXCAnR6UGc6Iy5UY9Uh2jhn9p_RlWT9LnXhHAMzbqcpyCAvlDn4IdmvzG4bK1ZvOdqMCxDgTkRdiWF68" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">القوات المسلحة اليمنية تصل نقطة الهنجر في المدخل الغربي لمدينة تعز</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/naya_foriraq/93543" target="_blank">📅 17:04 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93540">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BNW5SR9Z6nh7K2r-N36ezJN57HueWfpotub-hLSczGINeRNh1u3EP8EWFvgejJ4kXRsY5CZHGJ9xqETui-YjGWCXDiFzjNWVX-xW-sM24eIYpOYMjVzQZKKHSBcXtTMxrdLC_47ZFQMeATKrwxuROL_OR17RBA_-f3snI-GoXlWw9mTG24Jhg46NrfDoS2czHwyylLZ7gBA82NnIf9bvloXhmUKbfLV0vDbbG_QTL_LzjjXYbKd1utoufNsz44LoSnvjNAnYXYjGJ24AvVHvfPWmh8leV5rQKArM02di66AmSOp81-NiZLEv4HjRuC_fuFPc5YM32LID2dGsioEYvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Hk1Dz2UYHIUySHFw5eIwjQoYJAj8tIL2doyCVoCxhyM5bsjB9yA4cPUL6sYmHN8fBL4xrWOUQqyk1w6JxtrILEO7lCPNCG6qZ49n0RRxy8kBbXjX3IAdraE6ET_z2evdq1mslchPqPR-C0bi8Ns4acgQTTl7gEVx_lnRDycFhqVZoQJpqI5seGdKVFhOYVcDK_LcnybPU3GRo7Zl71ibmHjsscGSQy3bxBun4QCSWXxIo0nyKGlM9lVj8eK_Yt2Z0F-gC1ro2HdAHVg0pybRY2b5fuFzSzkE4NITLlN8zxnR2qLJkZ6IJSRJufp6HJiEmCgIhY922yQiqs6gSV1NDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BS4kbZD9u6K-pXqYHfqLPH3CVpwB6swSPqkRIIrkA6HLAwkXF0Gu8bW3di-P8XRpWpjRaHPbl92_YoNHI8eepmbQN_da0G7nH4UMZC_TnewbMNDhmoTD27jSEOeGjpLd5rjxVaCIDP1rOQSjDSLTTzmdJ3LXOLFkSQrVow7G4msCD6Zb2JWIRzBvTOUir8y93DHRvA6FMEpokoet7y5ai9ILTytFD4l80b-M_HgYZydYiEV2cw8yNsa6V0OaBq2_bvXbhg6r-Cj3WTF_SNgOzsv8pSX8Rr91UNgFM42p6ltT4zbOpPoZD2ASa2-nRvC989Mjd-nBJpDdexkkIkKXgw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">القوات المسلحة اليمنية تصل نقطة الهنجر في المدخل الغربي لمدينة تعز</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/naya_foriraq/93540" target="_blank">📅 16:58 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93539">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🔻
نايا تدعو جميع المصابين بأمراض تنفسية في السعودية والدول المجاورة إلى اتخاذ أقصى درجات الاحتياط خلال الليلة مع توقعات بتصاعد كثيف للدخان ما قد يؤدي إلى تفاقم الأعراض التنفسية.</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/naya_foriraq/93539" target="_blank">📅 16:55 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93538">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🇾🇪
🇾🇪
القوات المسلحة اليمنية:
تهيب القوات المسلحة اليمنية بجميع المواطنين بالإخلاء الفوري والابتعاد عن الأهداف التى ستقوم قواتنا المسلحة باستهدافها في حال أقدم العدو السعودي على استهداف ما أعلن عنه في العاصمة صنعاء
مقر شركة أرامكو في الدمام
مطار خالد في الرياض
مصفاة الرياض التابعة لشركة أرامكو</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/naya_foriraq/93538" target="_blank">📅 16:45 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93537">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🇾🇪
🇾🇪
القوات المسلحة اليمنية:
مشاهد من استهداف تحشيدات وآليات تابعة للعدو السعودي بطائرات رجوم المسيرة في عدد من الجبهات</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/naya_foriraq/93537" target="_blank">📅 16:31 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93536">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🇾🇪
🇾🇪
العميد يحيى سريع:
القوات المسلحة اليمنية تجدد تحذيرها لجميع الموظفين من الخبراء والمهندسين والعمال في جميع المنشآت النفطية السعودية من التواجد في الأماكن التي تمثل أهدافا لقواتنا حتى لا يعرضوا حياتهم للخطر سواء التي تم استهدافُها من قبل أو غيرها كما تجدد تحذيرها لشركات الملاحة الجوية في المجالات والمطارات والمسافرين والعاملين فيها التي تم الإعلان عنها سابقا.</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/naya_foriraq/93536" target="_blank">📅 16:22 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93535">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🇮🇶
اعتقال وكيل وزارة الصناعة والمعادن العراقية ناصر كاظم جبر متلبسا بالرشوة.</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/naya_foriraq/93535" target="_blank">📅 16:22 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93534">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromنايا - NAYA</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Audio</div>
  <div class="tg-doc-extra"></div>
</div>
<a href="https://t.me/naya_foriraq/93534" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🇾🇪
نقسم برب العرش
#شاركها</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/naya_foriraq/93534" target="_blank">📅 16:11 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93533">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🇾🇪
🇾🇪
يحيى سريع: القوات المسلحة اليمنية تحذر جميع الموظفين والمواطنين المتواجدين قرب أي منشئة تابعة لأرامكو النفطية بإخلائها والابتعاد عنها كونها هدفاً مشروعا لقواتنا.</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/naya_foriraq/93533" target="_blank">📅 16:11 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93532">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🇾🇪
🇾🇪
يحيى سريع:
القوات المسلحة اليمنية تحذر جميع الموظفين والمواطنين المتواجدين قرب أي منشئة تابعة لأرامكو النفطية بإخلائها والابتعاد عنها كونها هدفاً مشروعا لقواتنا.</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/naya_foriraq/93532" target="_blank">📅 16:09 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93531">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">هل يستطيع السعودي الذي تمثل الطاقة عصب اقتصاده تحمّل كلفة هذه المغامرة؟</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/naya_foriraq/93531" target="_blank">📅 16:06 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93530">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">المحطات بالمحطات</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/naya_foriraq/93530" target="_blank">📅 16:00 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93529">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">النظام السعودي: ‏نطلب إخلاء موقع شركة النفط اليمنية / محطة الصباحة المركزية بصنعاء بحسب الخارطة التوضيحية للموقع.</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/naya_foriraq/93529" target="_blank">📅 15:53 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93528">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JHFAU71JTH_1Q8UBNdmU0ooz6nYSNRZlOuAjj6IL6YKvqa9N9w96Prs559oDHDMPvkOqh7fi2RPHKyskDbIGbPKpXPY-TBWtDXa8bZNYh59pqZPp2cPn3ZaMgiSstAAhPJzSshFPYHwuIkjD74eieganJqpmeH7DaJZIdq_1_yg5Qml7lbwta1LclYkvTUlieEgWwZiVks4HhfHCikVrOvW-trdvctUacGy_nJXvPAJtlP2KUyyhKdY2r7DIUS3Hgdk3jkb__Jio_OHOdNUdJCRiq3gC1ix8xUBBu3Gyb27Ca1DBwWJGGtNtnyo5_sWDt6X3HqyMJZ3Oa1BC8a8EEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">النظام السعودي: ‏نطلب إخلاء موقع شركة النفط اليمنية / محطة الصباحة المركزية بصنعاء بحسب الخارطة التوضيحية للموقع.</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/naya_foriraq/93528" target="_blank">📅 15:52 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93527">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">النظام السعودي مقلدا النظام الصهيوني: سنصدر بعد قليل انذار بإخلاء موقع بصنعاء بهدف تنفيذ عملية نوعية.</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/naya_foriraq/93527" target="_blank">📅 15:42 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93526">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">‏مدير جهاز الاستخبارات الداخلية البريطاني: إيران تسعى لاستهداف مواقع كالمنشآت العسكرية ببريطانيا وخارجها</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/naya_foriraq/93526" target="_blank">📅 15:40 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93525">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">النظام السعودي مقلدا النظام الصهيوني:
سنصدر بعد قليل انذار بإخلاء موقع بصنعاء بهدف تنفيذ عملية نوعية.</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/naya_foriraq/93525" target="_blank">📅 15:31 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93524">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/148343f45b.mp4?token=UaPGgetxjpif6cADUbH0pxDUkvy1uEZ_CzR7gqSOAnI4f8YK31IY1M8ZjL-aMNkNN2GeVXVT54HXtQwIDcg_yFRzyzX_v_dZXWCJXwyqsEtUnIZZsnrC9-03OAroN0TFL3uUAkLa3tVnfYszSUEDN4jqDwIruDOvAyz3db0szq-mVUsThAeZ03mTM50eZLK7mk19n3W8Aas9FWCu3uGigomt-iRpZsaN7mkLhRkzl-Hnjja08aaz2sc0NGzEbc60M0CPbQLxmDoB9AnHb7aDI_ltHTwXGb3ixYvjMCtOT0xfC-tDsnYdcqeQGGkjnWxJPMLnnwtzIad2QSW1kW_VKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/148343f45b.mp4?token=UaPGgetxjpif6cADUbH0pxDUkvy1uEZ_CzR7gqSOAnI4f8YK31IY1M8ZjL-aMNkNN2GeVXVT54HXtQwIDcg_yFRzyzX_v_dZXWCJXwyqsEtUnIZZsnrC9-03OAroN0TFL3uUAkLa3tVnfYszSUEDN4jqDwIruDOvAyz3db0szq-mVUsThAeZ03mTM50eZLK7mk19n3W8Aas9FWCu3uGigomt-iRpZsaN7mkLhRkzl-Hnjja08aaz2sc0NGzEbc60M0CPbQLxmDoB9AnHb7aDI_ltHTwXGb3ixYvjMCtOT0xfC-tDsnYdcqeQGGkjnWxJPMLnnwtzIad2QSW1kW_VKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سماع دوي الانفجارات بوضوح في شمال الرياض</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/naya_foriraq/93524" target="_blank">📅 15:31 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-93523">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">في خبر غير مهم
🇪🇬
وزير الخارجية المصري بدر عبدالعاطي: كل ما ستطلبه السعودية سنلبيه.. ومستعدون لتقديم كل أشكال الدعم للمملكة بما في ذلك الدعم العسكري</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/naya_foriraq/93523" target="_blank">📅 15:22 · 21 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
