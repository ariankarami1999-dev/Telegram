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
<img src="https://cdn4.telesco.pe/file/ClMgDAwcwIDs63KMp_3H8KfFmE7yoLtxxWy_04Z-o-i7lc77JT_-cKdLm5BK9fz1s7Q9XIm-rcXzs5tWVOQSBPYuw4gGgTkrZzgB1DApQL1aB4mfoQWYWkKuNxlVymBS-BcljUsldLrBQShGnaq03KYnUoy8HzJjTaOxZ3flRhOsdsN_o5yayyOnkwEaBCDNDgeq7XMcuVBArDeILqoFI3Zsghs__SND9oKInhfa5ZDjrSDEOmNEyY9XGqIwN3Lhu-1YeQkJEfSHSz13oeGyeBeNPISYWdX8rIEo-dT2x6buBALNjLyoSeHAl9ZPdWTukVIh8MOdQ4wK1biUFsiTvQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 273K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-08 00:13:06</div>
<hr>

<div class="tg-post" id="msg-86247">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9bbcf1f5b1.mp4?token=QfmvkUGGkWlCWXFOVsjc7B3hZy4b9ZK3y81jV6Jna8M08bq2YanbvAgXUF8EgMSi4YNGhcTjkA1a6_AXYWlH_6a9OdPabyBhcpAYmlRI7VvCe_EA5YVZb1AxtdPjHNWN5JVZd_4n78MmIYHcjYU1HVMfqpxmX3qHckANeyU8xBAtc_eUCogXOme4oDH_ilKMpurvexly0xSWeIlvNhxhG62QFSsQYhmIEjxJ21j_QATN6pwB0Rg3LKwQWpYv2AZLVpG8lkz0F4uXfAXDXuXdann_EB-pNcpQHD6Chl2eEmnAD2QxP0Gn7lRbkUOx6YQotI1hyjCCwF4Jjb7lKIJUAqdXE6nzICodshs9XgYFto6b2IU7qIegQBKkFbJ_nFmlodHdTQxqJeQMsu2i2g7Xe3-Cq5ypuhl9HQhl0_ITMVaVKtmSjiUKkqYu9Y_ux-mbFE9T8FT54puCPVkLN0CmoOlbToV2NZ1WxhiuIOr-43Zt6NqCnFYA0ag95GcG_N0PCtjotAk8-QDJHCS4QwEMkWNmIk-THLcwYoOA820otey1rK7TGECnycb_VjaYhr7cedVDjS5ClaCFDKurpGSYcj8v5G3-xkLDjM9j9E8JKAQg8UTep6ubnrr0HAyMrH9vcA6UbwEdCphw33gOqGUq3ku_gbgLXCc3u-QAZK88tV8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9bbcf1f5b1.mp4?token=QfmvkUGGkWlCWXFOVsjc7B3hZy4b9ZK3y81jV6Jna8M08bq2YanbvAgXUF8EgMSi4YNGhcTjkA1a6_AXYWlH_6a9OdPabyBhcpAYmlRI7VvCe_EA5YVZb1AxtdPjHNWN5JVZd_4n78MmIYHcjYU1HVMfqpxmX3qHckANeyU8xBAtc_eUCogXOme4oDH_ilKMpurvexly0xSWeIlvNhxhG62QFSsQYhmIEjxJ21j_QATN6pwB0Rg3LKwQWpYv2AZLVpG8lkz0F4uXfAXDXuXdann_EB-pNcpQHD6Chl2eEmnAD2QxP0Gn7lRbkUOx6YQotI1hyjCCwF4Jjb7lKIJUAqdXE6nzICodshs9XgYFto6b2IU7qIegQBKkFbJ_nFmlodHdTQxqJeQMsu2i2g7Xe3-Cq5ypuhl9HQhl0_ITMVaVKtmSjiUKkqYu9Y_ux-mbFE9T8FT54puCPVkLN0CmoOlbToV2NZ1WxhiuIOr-43Zt6NqCnFYA0ag95GcG_N0PCtjotAk8-QDJHCS4QwEMkWNmIk-THLcwYoOA820otey1rK7TGECnycb_VjaYhr7cedVDjS5ClaCFDKurpGSYcj8v5G3-xkLDjM9j9E8JKAQg8UTep6ubnrr0HAyMrH9vcA6UbwEdCphw33gOqGUq3ku_gbgLXCc3u-QAZK88tV8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
فيديو من الذاكرة للاعلامي القطري عبد العزيز آل إسحاق، الحشد الشعبي العراقي قادر على احتلال السعودية من خلال تطبيق أوبر.
﴿أَلَيْسَ الصُّبْحُ بِقَرِيبٍ﴾</div>
<div class="tg-footer">👁️ 2.25K · <a href="https://t.me/naya_foriraq/86247" target="_blank">📅 00:08 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86246">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🇮🇷
الحرس الثوري في محافظة مازندران:
الخبر المتعلق بهجوم على سفينة شحن في منطقة خزرشهر، فریدونکنار، غير صحيح، ولم يحدث أي حادث أمني في هذه المنطقة.</div>
<div class="tg-footer">👁️ 7.85K · <a href="https://t.me/naya_foriraq/86246" target="_blank">📅 23:48 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86245">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">إعلام غربي : تعمل السعودية على تشكيل تحالف دولي يهدف إلى حماية طرق الشحن في البحر الأحمر من هجمات الحوثيين، وفقًا لمصادر مطلعة على المناقشات.</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/naya_foriraq/86245" target="_blank">📅 23:27 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86243">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🇮🇷
إغلاق حساب العلاقات العامة للحرس الثوري الإيراني دليل على خوف جبهة الغطرسة من البيانات الدقيقة والتنسيق بين شعوب المنطقة المحبة للحرية.
بيان العلاقات العامة للحرس الثوري الإيراني:
يا أمة المنطقة النبيلة الواعية، يا أمة الإسلام العظيمة، يا شعوب العالم المحبة للحرية!
بعد أن قام شعوب دول المنطقة الغيورة الشريفة، وخاصة إخواننا وأخواتنا الأعزاء في الأردن والكويت، بدافع من المسؤولية التاريخية والغيرة الإسلامية، بإرسال معلومات قيّمة ودقيقة حول تحركات وقواعد النظام الأمريكي إلى الحساب الذي أعلنه الحرس الثوري الإيراني على تطبيق تيليجرام، لم يستطع الأعداء المتعجرفون تحمل هذه الظروف والروابط بين الشعوب، فأظهروا، بإغلاقهم حساب العلاقات العامة للحرس الثوري الإيراني، خوفهم مجدداً من البيانات الدقيقة والقيّمة للأمة الإسلامية العزيزة والتنسيق بين شعوب المنطقة المحبة للحرية.
...هذا العمل المشين والجبان، شأنه شأن سائر أفعالهم الدنيئة، مدانٌ بشدة، وهو دليلٌ واضحٌ على انحدار جبهة الغطرسة ويأسها.
🔹
لن يُسكت إغلاق الحساب صوت الحق وإرادة شعوب المنطقة الصلبة.
يُعلن قسم العلاقات العامة بالحرس الثوري الإسلامي عن إطلاق بوابة إلكترونية جديدة آمنة وموثوقة للتواصل المباشر مع شعوب العالم المحبة للحرية، وذلك لضمان استمرار تبادل المعلومات والتوعية بشكلٍ أقوى من ذي قبل.
نؤكد أن درب المقاومة والنصر سيستمر بلا هوادة، بعون الله تعالى وجهود الأمة الإسلامية.
قسم العلاقات العامة بالحرس الثوري الإسلامي</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/naya_foriraq/86243" target="_blank">📅 23:20 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86242">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c1df8c6c9a.mp4?token=b4TuOJXWPmJLu-WPXB1NDpAoWgNMEeEsUhb4kQe_gWfSMgmY5Xjun6dFjvEwQFmBwpY-027D5WY-rjLa-D1H-54u1kcl-ZUwIyFbIiq9dE0maNa0uE9CynyW_7jph3Qq0t9zvtU-5SVOE3C1v7GuEROara3PnySc0IJxJSxzbjR2usSDFaLVoaT7NUEdIOX2EcasV0s8Dsf5KZ-6bGyBx4Q5L7i4g7Cxwr3HgYFABqC63WpRWzMQtmATFLPJ8A3-mWtajR6s6JfxN6mmNsOn6Ap1BadznuYAj0OhEW4cxKOOyAIEyQcUudYfX3-JzSJDx0vIBZVTmWXUo1J-lXRZTqmMREXY1ZfLKVbHxDFgC4xcmA0fYFBlw7pzj1XpRzq6ckDx8Dd83VOudhPZ5y0-oZpa2VJNQABMb-EDovGz0dZjWu__gUcrNsoyD6uPW24qmCRFdtPt3fRyAUFBo1B5XtNJrtyGIYlVIGoRyji_HekCHBvL5koivIW29dZN2H8BnMvZ0_31uDamKA3JpDANYtToga486suReKSwUFEhn4J7GGOivxjsecHiRBpfkT3kXXif_FjXSusGzcefWwYpPCglzHRdGS9Tw4d7NJCfeDrrUS_4ER_rR7WmQPMkhd88UcALLcpc9izF5PchVJAIlotNzMxcB5XgcYoxJZuq1CI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c1df8c6c9a.mp4?token=b4TuOJXWPmJLu-WPXB1NDpAoWgNMEeEsUhb4kQe_gWfSMgmY5Xjun6dFjvEwQFmBwpY-027D5WY-rjLa-D1H-54u1kcl-ZUwIyFbIiq9dE0maNa0uE9CynyW_7jph3Qq0t9zvtU-5SVOE3C1v7GuEROara3PnySc0IJxJSxzbjR2usSDFaLVoaT7NUEdIOX2EcasV0s8Dsf5KZ-6bGyBx4Q5L7i4g7Cxwr3HgYFABqC63WpRWzMQtmATFLPJ8A3-mWtajR6s6JfxN6mmNsOn6Ap1BadznuYAj0OhEW4cxKOOyAIEyQcUudYfX3-JzSJDx0vIBZVTmWXUo1J-lXRZTqmMREXY1ZfLKVbHxDFgC4xcmA0fYFBlw7pzj1XpRzq6ckDx8Dd83VOudhPZ5y0-oZpa2VJNQABMb-EDovGz0dZjWu__gUcrNsoyD6uPW24qmCRFdtPt3fRyAUFBo1B5XtNJrtyGIYlVIGoRyji_HekCHBvL5koivIW29dZN2H8BnMvZ0_31uDamKA3JpDANYtToga486suReKSwUFEhn4J7GGOivxjsecHiRBpfkT3kXXif_FjXSusGzcefWwYpPCglzHRdGS9Tw4d7NJCfeDrrUS_4ER_rR7WmQPMkhd88UcALLcpc9izF5PchVJAIlotNzMxcB5XgcYoxJZuq1CI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
🇺🇸
ترامب عن إيران: سنضربهم بقوة، لقد حان دورنا، أُطلقت علينا 5 صواريخ الليلة الماضية، وتم إسقاطها جميعاً. حان دورنا.</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/naya_foriraq/86242" target="_blank">📅 23:16 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86241">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🇷🇺
🇺🇦
‏
زيلينسكي
: روسيا تستعد منذ أيام لتنفيذ ضربة واسعة وهناك احتمال كبير بأن تنفذ الليلة.</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/naya_foriraq/86241" target="_blank">📅 23:05 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86240">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">بعد مضيق هرمز وباب المندب تتجه انظار المحور إلى قناة السويس.</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/naya_foriraq/86240" target="_blank">📅 23:00 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86239">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🇪🇬
🇺🇸
ترمب بخصوص حادثة مصر: جرى إطلاعي على ما حدث في مصر</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/naya_foriraq/86239" target="_blank">📅 22:57 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86238">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🇪🇬
شركة أمبري للأمن: تعرضت ناقلة غاز طبيعي مسال يونانية، ترفع علم برمودا، لهجوم من طائرة مسيرة واحدة على الأقل أثناء رسوها في ميناء دمياط التابع للشركة المصرية القابضة للغاز الطبيعي في مصر.</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/naya_foriraq/86238" target="_blank">📅 22:54 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86237">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🇮🇷
🇺🇸
ترامب عن إيران:
سنضربهم بقوة، لقد حان دورنا، أُطلقت علينا 5 صواريخ الليلة الماضية، وتم إسقاطها جميعاً. حان دورنا.</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/naya_foriraq/86237" target="_blank">📅 22:52 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86236">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/34f901ff18.mp4?token=jNTS1cRWRitJpORWdQNocvPIO6n9RgygDJsqSQepVU9CBOoncckAbImQ0e3drS9w4P7UgqB3mfUjq4sqvQtIXoU9QE29wqDICyWp18n5byJiz2oMpTKrX8niBykOS4bkggBUBXOIjEJvUQx5_KBj62ZsYb-oGV-5iMhq8hzrPC_QtjGf4ABKougBFzqbNddD7JtaYLVgtwu5O7syuxyAA3RaJcoW0fkVd1gA6KBwSB0IQ62gACKAU5CNpwcvDde4g3r1DpQfwB3NkrrvAu_sVevx0Y113B6fo0JBSoOpCYFdpCUj6aHDe6ADKGtrRaf0u9A67hElXbPj08Z9ndsXsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/34f901ff18.mp4?token=jNTS1cRWRitJpORWdQNocvPIO6n9RgygDJsqSQepVU9CBOoncckAbImQ0e3drS9w4P7UgqB3mfUjq4sqvQtIXoU9QE29wqDICyWp18n5byJiz2oMpTKrX8niBykOS4bkggBUBXOIjEJvUQx5_KBj62ZsYb-oGV-5iMhq8hzrPC_QtjGf4ABKougBFzqbNddD7JtaYLVgtwu5O7syuxyAA3RaJcoW0fkVd1gA6KBwSB0IQ62gACKAU5CNpwcvDde4g3r1DpQfwB3NkrrvAu_sVevx0Y113B6fo0JBSoOpCYFdpCUj6aHDe6ADKGtrRaf0u9A67hElXbPj08Z9ndsXsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
انفجارات قوية مجددا في قضاء رانية بمحافظة السليمانية شمالي العراق.</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/naya_foriraq/86236" target="_blank">📅 22:36 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86235">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XPVnpnAZhqvHvOM5dqIxbotzxQ1K54Ry8O85OcFbsUaK9i9LeT8OtUYThFZXQK41o6xJaeucQGJVPBduK-Q7j6TM1_fhTS2Bz06fEqlSAGsEQQYnf3EUv6DD-Cx9Zp51EL_7npGi1Zv6MFmvpBOHRrCCa6dhMxY71kVD5bGJDQliKnrq90o4XtbqIsSnKAEqANx8Z8_ci9i7k3FLy3CQvQCUrrtFT0rRDb1uYLwlVaaEzX-MhDzcD0v9BVccM7Ux63KfAcHPXkM5Uh9hjSymUjPJXBDfbdOaBay9T2hfxSU6zysFKLCyse_z9nI5AN4L_mR_hcmM52PGsEWDVT3A_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">يوماً ما ستنقلب الموازين يا ابن سلمان فلا تظن أن بلد العم سام سيبقى إلى جانبك حتى نهاية الطريق راجع صفحات التاريخ وسترى كيف تخلّت الولايات المتحدة عن حلفائها عندما اقتضت مصالحها ذلك.  ﴿أَلَيْسَ الصُّبْحُ بِقَرِيبٍ﴾</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/naya_foriraq/86235" target="_blank">📅 22:22 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86234">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🇮🇶
مشاهد مصورة توثق آثار الدمار الذي طال أحد مقار الحشد الشعبي ضمن قاطع قيادة عمليات البصرة عقب العدوان الأمريكي - السعودي حيث أظهرت اللقطات حجم الأضرار التي لحقت بالموقع نتيجة الاستهداف.</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/naya_foriraq/86234" target="_blank">📅 22:07 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86233">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🇮🇶
انفجارات قوية مجددا في قضاء رانية بمحافظة السليمانية شمالي العراق.</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/naya_foriraq/86233" target="_blank">📅 21:37 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86232">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🇮🇶
انفجارات قوية مجددا في قضاء رانية بمحافظة السليمانية شمالي العراق.</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/naya_foriraq/86232" target="_blank">📅 21:24 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86231">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">توقف تطبيق التلغرام مجددا في العراق !</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/naya_foriraq/86231" target="_blank">📅 21:16 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86230">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">تشيع شهداء الحشد الشعبي نتيجة اجرام ال سعود</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/naya_foriraq/86230" target="_blank">📅 21:16 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86229">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">انفجارات تهز سليمانية</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/naya_foriraq/86229" target="_blank">📅 21:14 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86228">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🇪🇬
شركة أمبري للأمن:
تعرضت ناقلة غاز طبيعي مسال يونانية، ترفع علم برمودا، لهجوم من طائرة مسيرة واحدة على الأقل أثناء رسوها في ميناء دمياط التابع للشركة المصرية القابضة للغاز الطبيعي في مصر.</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/naya_foriraq/86228" target="_blank">📅 21:07 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86227">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🇮🇶
رئاسة هيئة الحشد الشعبي:
الحشد الشعبي جاهز لتنفيذ جميع توجيهات القائد العام لمواجهة أي اعتداءات تستهدف العراق ومؤسساته الأمنية.</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/naya_foriraq/86227" target="_blank">📅 21:00 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86226">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🇮🇷
هزة أرضية بقوة 3.4 درجة ضربت منطقة قريبة من مدينة كوزران في محافظة كرمانشاه.</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/naya_foriraq/86226" target="_blank">📅 20:53 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86225">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">رضا بهلوي:
سنجد أفضل مكان لسفارة إسرائيلية لائقة في طهران بمجرد سقوط النظام الايراني.</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/naya_foriraq/86225" target="_blank">📅 20:52 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86224">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🇮🇶
الناطق باسم القائد العام للقوات المسلحة العراقية:
الاعتداء السعودي – الأمريكي عرقل جهود التحقيق فيما أثير بشأن استهداف السعودية، ونطالب بتقديم الدلائل والبراهين بشأن انطلاق الاعتداءات من العراق ولم تقدم أية جهة أية أدلة، والحكومة لن تسمح بأي انتهاك من خارج العراق او تصرفات فردية.</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/naya_foriraq/86224" target="_blank">📅 20:45 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86223">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jznnNgGITLwcwL82V2QsdvG9fEDsX0lOzYT0LCgnalKph1hG750pyCmpxekuDujVp_uUNA4TVYZC9NtiXq6F2oNl0urfm5C8RVLVpQY8oy4QlAZ_9MsVjgFeuah1jVBaSa6WfS5g8pj6ZvkswNatUwYK_iVEvmMqTUkWLtaT5J_38zL7Nm_zqr41x41SrnDbefEo7GPXCZSTS_QWUiGQakDurQ0eFKWteiS-5i_A0JLR4OQtabXma4ipqc97YIZwuvav_BJFTTPLsVG40a_MSPmNSzQVmhCj-x_KDTMAByIkg41WeDACxhFoAmqvH6bTmrcqZ_TB7kg84PPSCvLyhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
حركة انصار الله الاوفياء
أن مراجعة العلاقات مع النظام السعودي أصبحت ضرورة وطنية، في ظل ما يحمله تاريخها من ارتباطات بمرحلة دامية دفع فيها العراقيون أثماناً باهظة نتيجة الإرهاب والتطرف والفكر التكفيري الذي استهدف أبناء هذا الوطن على مدى سنوات.</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/naya_foriraq/86223" target="_blank">📅 20:37 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86219">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RGgyfLUt3IZkn_w8mUD2wZsr3ZzziF63xQbCDQsTkfZvBJYDs79lGoV8HDFEZEg6rhbsEmIacdT0DGI7e-tt4saigux8rEUuhpkhdAMkcvmoURHdOofaEZSkFrqNhVgSe7Urz7LLE48wf_ch5vsdii3CVC223T9eyBT5YkbwlgXfhhI61mkTRqpAu41NUt5zDBprkmIc5lDyNGJBnzlTIKA-RcnipoEB4k7d96ZLEVf_A1_4wuP4Awhc19bgFk1OKDD-tHBrn5Q19bpgO0jRaerY95qxxKHZdQIBIad48zQowFvi_mwmscyhMlG-La16zHU4MQwWFOgQjSIkpRLc_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uHcHzGJobrxoZ7THfVvwg2W9gMiwnhg2Arc-32VNZpzk8GGcKCeMH4u2yVObiKFrbe-GyT08O1Fc2V25Nza7gfUS7OnC_gEbLVN3RYaK-r0Qgszy-Ed-2-khvDZLSXSn4i9wOCci2AZhKOy3n0PHEomC0w59G22xt-dRDMMDxadg8SMvDGYU5AueHys9hz33Rvsm3NLwJ6CMuT7V4asz0dJBBWdcFpFjoHPYe-akpJfu0TIec_manjfVB50WOyqLnqUXaiNRbIoHws6HaaP54ob-liHn5OWM9PeixygfYXfXvzVQwDoc0_XhSZNPUkmy4D3g846dRQJPTLJMBFlaeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vT2XsbqeQbfnd1Ax2utFmKYsDONfIyYxirZtPtV65IwAZkAJD1sRqQpnz_hmZOSTWnBZmFKRmjhFmsBsxBa9ZQk3d63Gn7Iy3DaBdXh7rlXLCmFLt3xFrbjpz0idLRufuqxevffZV6MPQKcs4Mwjr5W9tWwKwnaVHxvux7lDnDfd6i6jofdQltZtauq34Q0759Je2Uedq2Un6LqEyYzWsWbHE8ikcEzZi1z5ssycMLHQwHDIf_AzKzIUWqu8fgBe9S5uf6h_sNcIiEBg-948uuFtQ6QtGtlacZ5-JGGHpDOC-BE1T1yoSyvZDyjB9fBbejrEZGYyQhnlsSlrkuQh9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WnmHJxmvnUiLGgmXPtPA-AAytW02gs2BLhrWfKSpUVOiV6gJ55s4UaWykAj1JIaCtV4941s0-_cdV6LrilfaTKJDOUGYXjITsTlf1u6HjbJNxnr7H3DZmD-3uZObrebKOQc46VTkyQkyO4g-GfJRFkpmGgVhjZgRrmMTob3xvYBGIn8J_wbPSZDm0M3GkOj9j9-jNO6xeiXfRpNVSYnBOhp4fiMB3rYq5FMoBUeDtR-CDpwk7859gc1ACjzUVks-gCfkagoM1lVhjJsCgDfjYptqrLhDwMrAgQF-a_U8Clw2IgBbQUT36otQZCUJX-NfsDE5K7xQFLE0C1stfIFvpQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">استُشهد أربعة من مقاتلي حرس الثورة إثر العدوان الامريكي السعودي على مقرات الحشد الشعبي، وذلك أثناء قيامهم بمهامهم بصفة مستشارين قانونيين إلى جانب مقاتلي الحشد الشعبي.</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/naya_foriraq/86219" target="_blank">📅 20:26 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86216">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mBFEv9xZBbS6bIwFwU3abEXHPOi_HcMJFvPkm1wd9UOy7qCKlM-oymWQrjWRlAKle0KgkqHy6oc0KYizqDJXZ6dwWi-sF9uw80U0RnLxuP0_MJmBL-K5RDKeOVLhjZGZ06YUGFAEQSoBHk9xn08MzfV0AY6AD8mebCSHNdSD7HQIHgtJy-5XsYA96-6Aww597cVXfo0wS-6-Tb5tRkVy_7WBalckOJa1Uf9spCRrk32afIFvlrqQfcw22klu7u13-Y2xbIDCjHyoPaX1NudmmGraEzJzenHyxe8osnEoapUAQ4E1k49Crpu_E557z9iy9cR3HbQOx10Y0WgzY-aOcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fpMR3UHnW6G5alHmHgdRwsTeNgfQzUku8Y_A0Fel4OHAgVyAI3HIIiOytciBrp2PQUZ-wpp0M7ncwLNzCAuVchIw754kejerOZ5BrmVbXyyxS4pljk-OJAt-Q6YNK47reR1ex7Q6ycTDW_VSggV68pd7q2SwyzKWbQKe217E9lbcW9WzpvfoOjgLBHzjdJOA5SRUHpRxuwvcypXpPG_lLKZKF5b9DAWr-8lzSkZ6CsmAkqhsxCMSBnphjCZcBdOqg3W5ToBTHAqeuN4tVl_q74JOJ0_mEpXKS3iugzpXlZwdqFC2lZan8dMOyv-2X2HaR0mlWJLGXdoHpZ6a9ULcMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lqr6L1c4RG4MiTAZMU8J5OMtJxKsIDW4xfyxHFwC6IHOhtSgaqQyc9hBofEmh0qiGadG_OvZzoW9o52DIkjXtPDmwW4463V6z3Mb56XsxdUGqYlz7XOGMxRhx2lkU8wVKSLilrb5rgwKFUSc0hFY6GdfrZUws9zjkhnsxAEHJJE_6M6apuhR_PxVb9XMPsJ6rSidHo4ZoBRMnyQSGnXp93FlSuoGV3ZNZ_sIQiOKPJKpQ511M0899ccuwgU7SmHupPUxolyY1M02zBT0zbfNVr80ySrhl3EiiSaoNIfsi16g8YAbZaNI9PC-JRYOb6RjWpfdk-hAJJiZ5gHab_9VZg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇮🇶
النجف الأشرف...
تشييع شهيدين ارتقيا جراء العدوان الأميركي السعودي.</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/naya_foriraq/86216" target="_blank">📅 20:22 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86215">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ameyfbnkZk5Q2eea15MXMZMnszCGEEYAPxEnQMlEjrDczLmn3d0T6yEBNqjOtDFoF2QIFWh4NzuTqqBdKXDhO2g7PrYW4Axyj8BBxQOI_9CP9xhXk1hm8OOSffxQvpV05PidScpHc06BIvsB-iGqXTVyychxh2XtR5dG_GTssM6uv8RlymKSsZ8SfaVw3NQy4_5gQt8WzS6VC2yHqCRDY1V72sOglzPsJEF6qmavLal5c-ts77RHy0cgsF4fSwZr5vTwGV5zXeWZd0bzriE3-nGw6WE8F_Dz0g7zadpPjcguLMU-JsS6jdXBGgD_erpTyCQ3or02cA1Mk5iVWqUpiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">يوماً ما ستنقلب الموازين يا ابن سلمان فلا تظن أن بلد العم سام سيبقى إلى جانبك حتى نهاية الطريق راجع صفحات التاريخ وسترى كيف تخلّت الولايات المتحدة عن حلفائها عندما اقتضت مصالحها ذلك.
﴿أَلَيْسَ الصُّبْحُ بِقَرِيبٍ﴾</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/naya_foriraq/86215" target="_blank">📅 20:17 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86214">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a7529a921.mp4?token=p_HfIhOPXW4FygDGQ2Az5dECUD5HI93QsiWrv9Qe8GM3FZo7oSTVaeZim1jpM1Hzosyg99aM8Z4DLdi4PcIz3GbaztrTEDDmnh1d0wSFrPhIlutye4cIdHU0FVtEjE-VyrZZx-r9HvUdmJScRA5ZvFcc0VOy4W3unLEQt2uzSjqY1CZP8X8AIQXZTpQ-zi1-gjD8MQINWMAuOPiZkrtgobWbsDV-ZqIzqYU9aboCTcqGkrwokb_qEvDxpCvb2Ln61yGYDHaTALd2ptSMMUkqlb0TZeMK-7EfSGNOYLY9fKF62RHmO8eHsP9LZA81RPONU5NghLKMdBZsOadq-RZbww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a7529a921.mp4?token=p_HfIhOPXW4FygDGQ2Az5dECUD5HI93QsiWrv9Qe8GM3FZo7oSTVaeZim1jpM1Hzosyg99aM8Z4DLdi4PcIz3GbaztrTEDDmnh1d0wSFrPhIlutye4cIdHU0FVtEjE-VyrZZx-r9HvUdmJScRA5ZvFcc0VOy4W3unLEQt2uzSjqY1CZP8X8AIQXZTpQ-zi1-gjD8MQINWMAuOPiZkrtgobWbsDV-ZqIzqYU9aboCTcqGkrwokb_qEvDxpCvb2Ln61yGYDHaTALd2ptSMMUkqlb0TZeMK-7EfSGNOYLY9fKF62RHmO8eHsP9LZA81RPONU5NghLKMdBZsOadq-RZbww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
تشييع مهيب في محافظة واسط للشهيد منتظر عيدان العتبي الذي استشهد على اثر العدوان السعودي على الاراضي العراقية.</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/naya_foriraq/86214" target="_blank">📅 20:13 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86213">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u1BGq2AkNveAPr30r0queokoIUj_5bxW-g4-A0A4bfldDOC4fr5GuplcGRSPA3I0u5HY_ZUW_l-DDoD74najwxqE6BEIwoPG55SD0uF0vZG3eZ-d7iOveJ1MYSCKP4TX6drzuhLlTyuJ5j3bMRw7vsfFaloKuTqF7BD6G9C9oBcB6lyTbX-fycDikUUEwlf6ObWSO6GAi39REbwVsJ1XFXHlcUAR-8a_OMCidc2Quih3rqHkmLFIOoGS2W9p3jbI_Qnobyz5AcoqcDhM-wAg9d8n4udPdJxIrLYpCTyFkcxQ2CZerwgMEAW7f_k8-X5ZbZznDGk5nVVZDwTiEsX2HA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇱🇧
🇮🇱
رئيس أركان جيش الصهيوني في جنوب لبنان:
"إذا لزم الأمر، سنتوجه إلى مناطق إضافية. نحن مستعدون لمجموعة واسعة من السيناريوهات.</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/naya_foriraq/86213" target="_blank">📅 20:08 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86211">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/286802a563.mp4?token=e58F1ylmrwWi4Ay9z3b67nnhJDAT3ECmr13jM-jrj3ScyBBN_gn7YrZgHq2QIRrJAGwJTyKgG11w4rOqO3b88AaNX_FjQwAVXa-Xpfxdy2q6eiik-hFRAWq-JIWpF7U8HwHTXzrNxit031KmsdEDmFtoncGKx_S7ONFqYZ_BPhNsG9tfBQkltdP2S-YMjcz-ZZLggU1Xz69GAZmmHrFvd-x3MEHfTZ4psqM8BEMpUVioUJoVGdJj0CpFf_KZfv5p25JtGtomxsMwTTDvP5oDGEkgquHqvZ_baRaJJoBKU3ET9PbLXGcclgnb46rWa7TnPgJFJXt8tYikje53Jwx0QQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/286802a563.mp4?token=e58F1ylmrwWi4Ay9z3b67nnhJDAT3ECmr13jM-jrj3ScyBBN_gn7YrZgHq2QIRrJAGwJTyKgG11w4rOqO3b88AaNX_FjQwAVXa-Xpfxdy2q6eiik-hFRAWq-JIWpF7U8HwHTXzrNxit031KmsdEDmFtoncGKx_S7ONFqYZ_BPhNsG9tfBQkltdP2S-YMjcz-ZZLggU1Xz69GAZmmHrFvd-x3MEHfTZ4psqM8BEMpUVioUJoVGdJj0CpFf_KZfv5p25JtGtomxsMwTTDvP5oDGEkgquHqvZ_baRaJJoBKU3ET9PbLXGcclgnb46rWa7TnPgJFJXt8tYikje53Jwx0QQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇬
الله اكبر السلطات المصرية تعترف: تم اخماد الحريق.</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/naya_foriraq/86211" target="_blank">📅 19:39 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86210">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/801f3d5794.mp4?token=Ve-ahyrGkRwCu9RucGswDhnuTHMewrXN8J71ZW1drHggcGzgPFWCkarznQhbVMEtbFB6e0dpNcEqq96yAELQudOLiERdpfl6qkIOGZ5r6legcixAWzgBElxQwcdBgeqWRldDeZz3HjiYWjRZY-wH5pcda6PxqO8HPk_Y90Zm_UAOc2GF7tL2iKDgNIkPHBvP0o-BYkIp7Nr5A3ANINvx1pbMCRN5b6ottuiTN82zQJMIlKMLXlYyT3T6FVntyOtcRROJQUAFFxyA6hyCw15q6-eS5kuFQ8K5lHKVGoO6kbIjKLZzppoo0uRjg3BSX-tgPMguWsz7f-MOa3R_YKTbLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/801f3d5794.mp4?token=Ve-ahyrGkRwCu9RucGswDhnuTHMewrXN8J71ZW1drHggcGzgPFWCkarznQhbVMEtbFB6e0dpNcEqq96yAELQudOLiERdpfl6qkIOGZ5r6legcixAWzgBElxQwcdBgeqWRldDeZz3HjiYWjRZY-wH5pcda6PxqO8HPk_Y90Zm_UAOc2GF7tL2iKDgNIkPHBvP0o-BYkIp7Nr5A3ANINvx1pbMCRN5b6ottuiTN82zQJMIlKMLXlYyT3T6FVntyOtcRROJQUAFFxyA6hyCw15q6-eS5kuFQ8K5lHKVGoO6kbIjKLZzppoo0uRjg3BSX-tgPMguWsz7f-MOa3R_YKTbLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">منو ياخذ السلاح يا زلمة، الحاج ابو فدك المحمداوي</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/naya_foriraq/86210" target="_blank">📅 19:34 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86209">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🇪🇬
رويترز: ‏تعرض مرفق عائم لتخزين الغاز الطبيعي المسال مملوك ومدار من الولايات المتحدة لهجوم بطائرة مسيّرة أثناء وجوده في دمياط المصرية.</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/naya_foriraq/86209" target="_blank">📅 19:32 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86208">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🇪🇬
انفجار بمحطة الغاز الطبيعي المسال في ميناء دمياط بمصر أثناء تفريغ شحنة</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/naya_foriraq/86208" target="_blank">📅 19:24 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86207">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🇪🇬
انفجار بمحطة الغاز الطبيعي المسال في ميناء دمياط بمصر أثناء تفريغ شحنة</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/naya_foriraq/86207" target="_blank">📅 19:23 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86206">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">الجبان ابن الوطن سموه
واخوي استشهد يسمونة هسة الذيل؟
مشاهد من تشييع الشهداء في العاصمة بغداد</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/naya_foriraq/86206" target="_blank">📅 18:33 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86205">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالإعلام الحربي</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dyNjhqZ80AGHN_mvgycpMIbsEcN3X4v4i34Bo0rZVOhby0zJxlZf3OnnCgDuH3KlVImORtBknwxWHl6mDV_wD36FZ63gn_TLT7WDhFTCx01IpINQ5XscQWE_U0PiWVYdhWUe-1ylQzeul5RzrTU8SgKmcUozyM1uqgyE0MfJUELrkVW0X2zg-ogvmJGYkrYkMnEsTBbLl6ncjObiGoTukKyN06mqw5Mct0dxZK9_tJBxjDdGzCd3wX9SSOj8hSfRbX9VlfV7H3V5DpLH5FgQi2sKhm6E45A7rfFOwYYut6UMMcK6wr3ISvHQeHlCQfhhE-q-Olreb-kT80dQiUbFRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بسم الله الرحمن الرحيم
(وَقَاتِلُوا فِي سَبِيلِ اللَّهِ الَّذِينَ يُقَاتِلُونَكُمْ وَلَا تَعْتَدُوا ۚ إِنَّ اللَّهَ لَا يُحِبُّ الْمُعْتَدِينَ)
بعد أن أكدت المقاومة الإسلامية نفيها القاطع لأي استهداف طال الكيان السعودي ومنشآته، اقترف العدو الأمريكي جريمة جديدة، استهدف فيها رجال الحشد الشعبي وموكباً لخدمة زوار الإمام الحسين (عليه السلام) في كربلاء المقدسة، راح ضحيتها عشرات الشهداء والجرحى.
إننا نؤكد بلا ريب أن النظام السعودي لم يكن ولن يكون إلا خنجراً غادراً أو أداةً قذرةً تُدار من البيت الأبيض وأجهزته الاستخبارية المشبوهة؛ فكما سخّر إمكانياته بالأمس لتفويج الانتحاريين لسفك دماء العراقيين، ها هو اليوم يجدّد مرغماً عقد العمالة لتنفيذ جرائم سادته وإملاءاتهم الإجرامية، للنيل من إرادة شعبنا الأبي.
ولو سلّمنا جدلاً بصحة ادعائهم: أن مصدر ضرب منشآتهم النفطية جاء من العراق. فهل يعقل أن يُرد على محاولة (غير ناجحة) لاستهداف حقل نفطيّ بقتل وجرح العشرات من الأبرياء؟!
ولو افترضنا في هذه المرحلة المفصلية أننا سلّمنا سلاحنا وصواريخنا إلى السلطة الحكومية، كي تتولى هي زمام الدفاع عن سيادة العراق وحرمة أراضيه وشعبه؛ فما الذي ستتخذه من مواقف حازمة أمام هذا الاختبار الميدانيّ الحقيقي، لتثبت للجميع قدرتها على ردع المعتدين، والاقتصاص ممّن سفك دماء الشهداء الزكية، بدلا من رجال المقاومة، وكما فعل المجاهدون ذلك مراراً في العراق؟
وبناءً على ذلك، نعلن الآتي:
أولاً: نمهل الجهات الحكومية التي طالبت المقاومة بنزع سلاحها مهلةً أقصاها حتى الثالث والعشرين من شهر صفر؛ لنرى ما هم فاعلون.
ثانياً: حرصاً منا على حفظ أمن زوار أبي عبد الله الحسين (عليه السلام) وأرباب المواكب الكرام، ومنعاً لأي إرباك لزيارة الأربعين المباركة قبل إتمام مراسمها؛ فإن ردّنا على العدو الأمريكي قادم لا محالة، وقد ينال أدواته في السعودية متى ما استدعت المقتضيات ذلك.
الرحمة والرضوان لشهداءنا الأبرار، والشفاء العاجل للجرحى الكرام.
المقاومة الإسلامية في العراق
29 تموز 2026</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/naya_foriraq/86205" target="_blank">📅 18:25 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86204">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b8c2INJNL6IPvNwNeEgH2dETgXhVcwctqGWm8MZ_Pe71sEJRALquxoIxyZHnXx2gPdkugTm40tX7TzpYoLlK9-Wmkk0S2vs4AsvUbvaZVzNRQl_DzgHhr7vBUOoMWs2joS2-a9nnS8iJmdGOzSwpj82QqlxsIu6qZXFWJqrxX-_sRNYTk9Jdb9QZ8c1SFnuJPFJXE_xMDbgSbWHcn4lxPGsWfSKjbdvjY_DtGFg-wPLdtgFwheu2RQ5boY2Zx42ZyTbQmmWaxXDfLtbOZtIvY_BPf9kac_n9l6NN5bYBxR9RlI42W4Sy5vRmk8MvzmsG-MBSnuI9RsA1YyZvnMBj3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سعر برميل النفط يتجاوز الـ90 دولارا</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/naya_foriraq/86204" target="_blank">📅 18:18 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86203">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">عوائل الشهداء توجه رسالة إلى امين عام حركة النجباء الشيخ أكرم الكعبي: ثأر ولدنا ما يبات هاي الليلة</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/naya_foriraq/86203" target="_blank">📅 17:56 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86202">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C4eLQ5mJvXDwj7l3Bss9rtEbNj5_1WnocxEx6LeVzNyUpmF8joGZwzeTe93MjIeUSo7T6bMZ6BYzNKVXmIvrKEVs-7Xi-E2PfDThQAkTwYDbltP058TWrGTCwpRI58cvBxyBZFq9qoIXl7CVVSnIj4gvGQFtJAzFCDPkseJlZsiq1lbDzOKyiHkfpt55OFiJeAcy27gPcDaXkYgnxNXFD_rYCUknBIq67IUz5tpuRMOignAA_axGw4JZtTq3400lFAJVwQEjNRK7mjUmFl62uhLsltNKFwQo2gYbPxXmDcBAJdUzm-kobEBXage_qUWQmjIU6ZnXss6wbiE7CbGcZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استُشهد أربعة من مقاتلي حرس الثورة إثر العدوان الامريكي السعودي على مقرات الحشد الشعبي، وذلك أثناء قيامهم بمهامهم بصفة مستشارين قانونيين إلى جانب مقاتلي الحشد الشعبي.</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/naya_foriraq/86202" target="_blank">📅 17:50 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86201">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">صحيفة التيليغراف: الصين سترسل صواريخ إلى إيران.</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/naya_foriraq/86201" target="_blank">📅 17:48 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86200">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">استُشهد أربعة من مقاتلي حرس الثورة إثر العدوان الامريكي السعودي على مقرات الحشد الشعبي، وذلك أثناء قيامهم بمهامهم بصفة مستشارين قانونيين إلى جانب مقاتلي الحشد الشعبي.</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/naya_foriraq/86200" target="_blank">📅 17:48 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86199">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالمقاومة الاسلامية في العراق</strong></div>
<div class="tg-text">🔴
سيصدر بعد قليل بيان هام للمقاومة الإسلامية في العراق.</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/naya_foriraq/86199" target="_blank">📅 17:44 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86198">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">وصول رئيس أركان الحشد الشعبي ابو فدك إلى مراسم تشييع شهدائنا الأبرار</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/naya_foriraq/86198" target="_blank">📅 17:38 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86197">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">بيان مجلس الأمن الوطني العراقي:
عقد مجلس الأمن الوطني اجتماعاً طارئاً برئاسة  القائد العام للقوات المسلحة، رئيس مجلس الوزراء السيد علي فالح الزيدي، اليوم الأربعاء، لمناقشة تطورات الوضع الأمني والاعتداء الذي شنته القوات الجوية الأمريكية والسعودية صباح هذا اليوم، والذي أسفر عن سقوط كوكبة من الشهداء والجرحى الأبرياء.
وعبر المجلس عن استنكاره وإدانته لهذا الاعتداء، الذي جاء في الوقت الذي كانت الحكومة العراقية تتواصل فيه مع الأطراف المعنية للتحقق والمعالجة لكل ما أثاره الجانبان السعودي والامريكي في ما يتعلق باستهداف الاراضي السعودية.
وقرر مجلس الامن الوطني وضع خطة أمنية متكاملة لمسك الارض للتصدي لأي انتهاك لسيادة العراق، ومنع اي مصدر من أن يعمل على تهديد دول الجوار.
ووجه المجلس وزارة الخارجية للتحرك وفق القانون الدولي وميثاق الأمم المتحدة لتوثيق الحالة وتثبيت حقوق العراق المشروعة.
واكد الاجتماع موقف الحكومة الثابت والرافض  للأعمال العدائية كافة، بصرف النظر عن الجهة المنفذة لها أو المبررات المستندة إليها، مشددا على أن التعاطي مع مثل هذه الاعتداءات ومواجهتها يُعد مسؤولية حصرية للحكومة العراقية ومؤسسات الدولة الدستورية دون سواها.
كما جدد المجلس التزام الحكومة بترسيخ الاستقرار في المنطقة، والمساهمة بفاعلية في حفظ الأمن والاستقرار الدوليين، وتبني سياسة خارجية قائمة على الحوار والتعاون واحترام القانون الدولي ومبادئ حسن الجوار، وتوظيف الوسائل الدبلوماسية سبيلاً لحل النزاعات، وفق نهج استراتيجي للنأي بالعراق عن الصراعات الإقليمية، بما يحفظ مصالحه الوطنية ويصون أمن شعبه وسيادته.
ومن هذه المنطلقات وتحملاً لمسؤولياتها الوطنية، باشرت الحكومة منذ الأيام الأولى لتشكيلها بجهود حثيثة لتعزيز سيادة القانون وتأطير العمل الأمني ضمن المؤسسات الرسمية للدولة. وفي الوقت ذاته، تؤكد الحكومة رفضها لهذه التصرفات الاحادية غير المبررة، التي لا تقتصر آثارها على المساس بالسيادة الوطنية، بل تعيق أيضا المساعي الحكومية الجادة في ترسيخ دعائم الأمن والاستقرار على المستويين الوطني والإقليمي.
تدعو الحكومة جميع الأطراف إلى عدم الانجرار إلى مسارات تؤدي إلى تفاقم حالة عدم الاستقرار في المنطقة وتقوض خطة انفاذ القانون التي تبنتها الحكومة منذ تسلم مسؤوليتها.
ويؤكد المجلس المضي في تنفيذ الاتفاق الأمني لانسحاب التحالف الدولي في نهاية شهر أيلول 2025 واستكمال إجراءات خطة حصر السلاح بيد الدولة.
ويعرب المجلس عن بالغ تعازيه لعوائل الشهداء ، ويتمنى الشفاء العاجل للجرحى مؤكدا ان دماء العراقيين تحظى بأعلى درجات الاهتمام والمسؤولية.
•••••
صباح النعمان
الناطق الرسمي للقائد العام للقوات المسلحة
29-تموز 2026</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/naya_foriraq/86197" target="_blank">📅 17:19 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86196">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/790bac9e55.mp4?token=Pxq4bgCoL0a0IkbxarfYTnvECOj1rVNoA57JpE9wQuwY-LekB1iDt__JYAzZG3axja7g_q7QSKHTrE6GXjgBcl1DSyZKCJMtTdlBLbXgWHIpEwzbhYN3JNptOyU9kbCKQCXIScMtyPkFaQ3woVlceAxFR1mqCPWVWKSc_N-vki99t-5wQAXeIPS2SObdNFZ2QZFasiyVhv08_WYcmWuGnqE6kLyJrb0VAhixAmwN8iRz-rSWfl-c4J1AMto15Cs1qcHmVhU0fvHT3IlNZEK0UG0dItHMIHv9kRaxQAfAzZuy9aEadopFOS8HKtcXS6C8Mk0ib4ObfKwCxKQhHv9pMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/790bac9e55.mp4?token=Pxq4bgCoL0a0IkbxarfYTnvECOj1rVNoA57JpE9wQuwY-LekB1iDt__JYAzZG3axja7g_q7QSKHTrE6GXjgBcl1DSyZKCJMtTdlBLbXgWHIpEwzbhYN3JNptOyU9kbCKQCXIScMtyPkFaQ3woVlceAxFR1mqCPWVWKSc_N-vki99t-5wQAXeIPS2SObdNFZ2QZFasiyVhv08_WYcmWuGnqE6kLyJrb0VAhixAmwN8iRz-rSWfl-c4J1AMto15Cs1qcHmVhU0fvHT3IlNZEK0UG0dItHMIHv9kRaxQAfAzZuy9aEadopFOS8HKtcXS6C8Mk0ib4ObfKwCxKQhHv9pMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وصول رئيس أركان الحشد الشعبي ابو فدك إلى مراسم تشييع شهدائنا الأبرار</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/naya_foriraq/86196" target="_blank">📅 17:18 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86192">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/I7KYja4o-NXa7O2lKfUwDdXRt1pq-1UnpEVeM0yPF8_3gTmxgaEzq6ge8IH79TZW8HUpbkf1TsxVmhYs8avHgCz965XP95hOxK7kfHITu9TD3kM0zm51VosdAu3L_kEiFHMIYEzfDoVQr6SoTvxoQxxH7M6nrQqY3oogCEqmmim6cHx2iPzgpyirAK3cC0SmB7BKFq6YIU5yn-gg-xUgHaPYw3skUYVC4mcx1uuOssRzMn3NKv_Yc-GHPB9379L6qhLVboAxaLWP1QSaohUl7EOrPWZvHt3MC4CvruVP3iYGuYajCZ4iRV1WflgsKdPo-ZGWNEOLuWGm1cp5pDcpBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vITnbSRTAQ8hNnPPJwShvo6NniYTwg_3zukDAAGH9LI0kmwWAEUlupBjlTKVp9s4C9HZRg4739bi2zcnX4kshUNYViFz-w6Yx-pHRZ0_uC9vJPtVXi116yNHWrrDBPppBOJ8oXUZiWQ4yyLzIab6TimBCUAfvhSYu57rCU9rBLQGEsnRQZweWpy8zjNv6LhDi4g2bNfiyNWf5zotqGfyOb9p4xQ51qXGGmiR5NtriNCbHAwaXyrwzvyVF6VIC_aKEhfdsvTx4AkrWZOuJVeOi4q2GSPOJ9BrRoCpM50oyR7RFrdeJi6rdaITrvbhPryzfjG1MQpYF43Ijr5BIbWm8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/A9hN6b0s3ch7zJXFO6lX0869aSTcn-wByMcfIYD1lC7PFzTbvbrD8zeQfHbcltpf49NHxkJhTqbMBgpHKE4Y4ecxoAllPMWCe7qsB2wKBk1tCSjWf7DVhnIV6NNYPjD0-3gpR8z5BWN7o1Nn9iLIjVFzRt3mt_1ZluO_qt11Cz-Ds8q4zitOaW7WQLwz9RnJ2tB2auZhR9_4Re4c_9TzrRqd7XoVJlLOxUtlpjDhIF40ipv1mLvgBz0Gtqh03XT7XDMpBL_tyDU4o4wzZ9VifQSh0Y0Sox1W17feies5LQzibiYn81ui1rrT5GSBi-oMozOcrWzxlR2tZyP7tGK2QQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pw7BTFcAUuoRyq2MELmN5eDwKlhQEfu5hVkf8AS63sFOuiF18NTSvI2zKMmRUCG6oAoPedEho3KstMICcbZNmHqOXfZ4ZnBzCQYO7U4tIEHWFrGgwej4iekO5J4NX9iLywfLTREWz7zWxstTq4NfX7V2qCJ7D_3EEDeceo5u35xOR3PbKx7s95VWbNolfVPYZb4klYY9FLKdvW_pQWmCMLukR6kRFLdny6FRpdV63C3mj-ENlxKEN5F1dHo4jRj3M5dth2e3wwae4cfCAucgiFTQcbEU6hpk_AmUeVtRMvnh8l_p6DPR-gm6dYyWiNE6ULuRiIZqhkpmHgDY-9nK9Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">مشاهد من وصول جثامين الشهداء الى مديرية اعلام الحشد الشعبي</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/naya_foriraq/86192" target="_blank">📅 17:08 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86191">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/06322628f9.mp4?token=Q8hdflpjA9959bMRvxyOyyn6yN0UizybM_AIgL_-_16aUwAc8BfVsvyQdppvQ9-ifZwf3yXNJkRFSfriJqo8kE0_MvNmR2yqxdcSEL3s22KiJIhNv76zhLkAt7WeniDyY7NTzLRcZPX-ggowiNwx9LcuIyOilRt4RM4E4F2cVpUyk8zKltjhFWq-2pUhGSzk85iTcvr1lfDUyjwrl5DRpSjnUqUBXNZVE_HwzvNfvm4Vp1ZX5IKZEUgS7t2rXXADlI4RUk7uAw252MSy7olXPA4UK6FnI00FipBS0OEO4zs89zIP137fgMWtqFUsYBSehvHGVpzemD3JTHW4QR20Ag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/06322628f9.mp4?token=Q8hdflpjA9959bMRvxyOyyn6yN0UizybM_AIgL_-_16aUwAc8BfVsvyQdppvQ9-ifZwf3yXNJkRFSfriJqo8kE0_MvNmR2yqxdcSEL3s22KiJIhNv76zhLkAt7WeniDyY7NTzLRcZPX-ggowiNwx9LcuIyOilRt4RM4E4F2cVpUyk8zKltjhFWq-2pUhGSzk85iTcvr1lfDUyjwrl5DRpSjnUqUBXNZVE_HwzvNfvm4Vp1ZX5IKZEUgS7t2rXXADlI4RUk7uAw252MSy7olXPA4UK6FnI00FipBS0OEO4zs89zIP137fgMWtqFUsYBSehvHGVpzemD3JTHW4QR20Ag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وصول شهداء العدوان الامريكي السعودي الى مديرية اعلام الحشد الشعبي</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/naya_foriraq/86191" target="_blank">📅 17:03 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86190">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/99ad472b55.mp4?token=tQ2GmRrPBWdWO5UzZ19PRR5_iSFvJQ40N4eZXZ4SZr9jPLMlsxXk89Kvlt1IlqWTEgL2jxVTS9eeHk2FX4-38zsDf4gzM9MmrdN3C_QUDMOkXHbIl4kUBmobg6Pgl3fyGVdolV5UgkbFbyt1rKHSxznNVtAX2gVuOQuyXUSm6u93MFqw8DA3tBgUjrK7mLgsTPyCb4HSZXz_tXdj3NPwQ8bema5JzPjS14OkVvaV4sVh-H3-E6wJuEWptndINZawytlmUvqasTYnEZ_lC4UdjR2opD_mLlqwM2Uw5-_Nmu-ahxOhwxGepxO1R_9nFm1Js_MoqwUHGjt0JjBJgSNEVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/99ad472b55.mp4?token=tQ2GmRrPBWdWO5UzZ19PRR5_iSFvJQ40N4eZXZ4SZr9jPLMlsxXk89Kvlt1IlqWTEgL2jxVTS9eeHk2FX4-38zsDf4gzM9MmrdN3C_QUDMOkXHbIl4kUBmobg6Pgl3fyGVdolV5UgkbFbyt1rKHSxznNVtAX2gVuOQuyXUSm6u93MFqw8DA3tBgUjrK7mLgsTPyCb4HSZXz_tXdj3NPwQ8bema5JzPjS14OkVvaV4sVh-H3-E6wJuEWptndINZawytlmUvqasTYnEZ_lC4UdjR2opD_mLlqwM2Uw5-_Nmu-ahxOhwxGepxO1R_9nFm1Js_MoqwUHGjt0JjBJgSNEVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انطلاق التشييع الذي تقيمه هيئة الحشد الشعبي للشهداء الغيارى في العاصمة بغداد</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/naya_foriraq/86190" target="_blank">📅 17:00 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86189">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6b0f8e1812.mp4?token=OaxJ9pMsrShboTRMbytcg2_g0z1_fBZXOrv1o3bkxJkYoS2Pmh9hvv3auHCPYYp2pu69yl4tv0wKaavC4rH2_4rw-G7WgIlWsSVUrzMazQzMfqTj-Wfeo8GutxFu003s0UKhfvzkBE_oCN7LLDKlhOuQNSHUeiVpXqHiC-8cFA4L3MtX6V8LGr6TaPv-zGsbHYqIyT1nQHVhPb-hzktStO6YJ5nm85gAGOnkMiB5h_6fIJC86rl7euT3KynkRY7nsIZ7DAe6ciECBGXnq2XCf-UxI9uwoUTwi_Q3q3r5s3EA_AgfjKpP2IEzUMOiCsgfzLNPQTI97aDHkbxlihslcw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6b0f8e1812.mp4?token=OaxJ9pMsrShboTRMbytcg2_g0z1_fBZXOrv1o3bkxJkYoS2Pmh9hvv3auHCPYYp2pu69yl4tv0wKaavC4rH2_4rw-G7WgIlWsSVUrzMazQzMfqTj-Wfeo8GutxFu003s0UKhfvzkBE_oCN7LLDKlhOuQNSHUeiVpXqHiC-8cFA4L3MtX6V8LGr6TaPv-zGsbHYqIyT1nQHVhPb-hzktStO6YJ5nm85gAGOnkMiB5h_6fIJC86rl7euT3KynkRY7nsIZ7DAe6ciECBGXnq2XCf-UxI9uwoUTwi_Q3q3r5s3EA_AgfjKpP2IEzUMOiCsgfzLNPQTI97aDHkbxlihslcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انطلاق التشييع الذي تقيمه هيئة الحشد الشعبي للشهداء الغيارى في العاصمة بغداد</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/naya_foriraq/86189" target="_blank">📅 16:41 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86187">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f065102a3a.mp4?token=h0BVCuyZLZ3cWXM1vsGo80a9KoeQql0mlwP76CjZBjM-duImtafKG6Lr3GEmbExRluZOIBWk9nN4KBTVeQoJbv0cHyQquSTtLhfqgIIhyH7Ss6UVK6gfXUAMMnutxRSsvEHVaJ-tSLguWAB2IYGEPtbScJMzB_wU3wR1-j-MRjKVVC_-W03fcys3FlecvwLOlHE_oW87Eanoqg2KFrOfwkBPoQuLyVh3VueKB-nhx9-8fjSwF_9CblEJqqdQDNtTt7-HLj0-1G8bzvDvK9515Drx5CIrULqJWGZyaOZ2nWqCjx36SiEx7yWwIRzYwzJnHPBcuFnLGm4BKaiJHCnIKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f065102a3a.mp4?token=h0BVCuyZLZ3cWXM1vsGo80a9KoeQql0mlwP76CjZBjM-duImtafKG6Lr3GEmbExRluZOIBWk9nN4KBTVeQoJbv0cHyQquSTtLhfqgIIhyH7Ss6UVK6gfXUAMMnutxRSsvEHVaJ-tSLguWAB2IYGEPtbScJMzB_wU3wR1-j-MRjKVVC_-W03fcys3FlecvwLOlHE_oW87Eanoqg2KFrOfwkBPoQuLyVh3VueKB-nhx9-8fjSwF_9CblEJqqdQDNtTt7-HLj0-1G8bzvDvK9515Drx5CIrULqJWGZyaOZ2nWqCjx36SiEx7yWwIRzYwzJnHPBcuFnLGm4BKaiJHCnIKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وصول عدد من الشهداء الى المغتسل الحيدري في محافظة النجف الاشرف</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/naya_foriraq/86187" target="_blank">📅 16:40 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86186">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/39d127a159.mp4?token=O5cFnk2wm-n4UuhrUlzsKvYUV8CI_yjPUW-lDoxJtquryt-TiHUd4y9cgsfVkSIIjkM7fW9P7sxQAByYfAhGCktn8Okqc6Cga0yYArQyMdu1_92khFfK-_o5HJuOk5rLakYL8jji3o7s5Bjm5qW2__QYdJt-fFS0LS4k29tjfoel286zcgXUrnebpLi8R1FVFzJtHYUZTuIflqH46bYDTggMjEce-QSFsZ9WXhCiCgSfUo40_1JsMBa_HceMnvIZedN3PYsfHy_BOfaa6wqqT2Fqvt98jT2s7tDE0vjYbo-7L8gtUqmUIzSRvUhDhFCdTmjY4Z7VNwa_gTMonKg4fQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/39d127a159.mp4?token=O5cFnk2wm-n4UuhrUlzsKvYUV8CI_yjPUW-lDoxJtquryt-TiHUd4y9cgsfVkSIIjkM7fW9P7sxQAByYfAhGCktn8Okqc6Cga0yYArQyMdu1_92khFfK-_o5HJuOk5rLakYL8jji3o7s5Bjm5qW2__QYdJt-fFS0LS4k29tjfoel286zcgXUrnebpLi8R1FVFzJtHYUZTuIflqH46bYDTggMjEce-QSFsZ9WXhCiCgSfUo40_1JsMBa_HceMnvIZedN3PYsfHy_BOfaa6wqqT2Fqvt98jT2s7tDE0vjYbo-7L8gtUqmUIzSRvUhDhFCdTmjY4Z7VNwa_gTMonKg4fQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاهد من مستشفى الحسين العسكري في العاصمة بغداد لجثث الشهداء</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/naya_foriraq/86186" target="_blank">📅 16:35 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86184">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HmDU22ybfrUdRJSoEN81-cwDjsq9O2xOGLRQHxVbwDB-cABgHR6tF3icJbwZJEGd-yxhJzISFkg8g3HS11Qz5LC4VeerJ77eDKQKc-aT5zEnwJJD0hGsezObpKGjP73RCuetpg3CgRU15na7MlM3fR4fBPy2r_ExFC8iWV9D_HZGGHOtAOD0pMq1Z1b_wi6ZGPukDndKlrOIF3oeeouJX33NaDBuBvY7z2JIVI1FZvhPOeeHHymlbJKDG0DUQk03HKcEmaw2hPX6znebsQ42mxYjUwn5nbrlQW5sc7_UINSKfsNotLguR_2YvWUar9btVjZ5JGY5ks0MXyka_zhYGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cZHUPLNEieDH3fYitONzFzwtjJOZKrw-dgZ34y66f8I9wauSzEeOvuWwiFg8_dIjTGHJ4aD6yRgb9MhLGGCev1TE0ilEebsRYshpt1z_NMUBQ3hwKKA08M9aJ6EQCzhVoCjC5z90nN8eK8ZnmV5mvjdKZtaEDMEsPi56LZGsTX9ke0KG2jWR-ce9XaAZCKrkuB-ch_nLr48w5oZA1XegrdQGA29--hXKOy8AUt1Zfi2GBLCCFEXLCmuC4QoCI8euaT-VFUDs8ETbDxHSwhlpiJx_VC7SjXJDSOZgy78Q9Enl-ROBcd5hEC92--FRQMfBEe_2F-fMEkrEbavdWJTARA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">استعدادات للتشييع في العاصمة بغداد وغضب يعم المشيعين وسط مطالبات للرد والثأر</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/naya_foriraq/86184" target="_blank">📅 16:32 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86182">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iSPOro0X-orLcGaFCVyvIf7kwuCqeB4O4HJJy0_ke0OtKWX7jdpEEFeLVsdVZnjL7uiHIUszdK-DuFwsKOOQ0-jA9YPzhMi7QVievpEasGqSg-OifoNa1rdGhlcb7AAZC2tb1B41UWkOoIwULaT_uw4e4G5sfEOsa0bMsLDmd-0y02wNJehb6_y3Va8NsjH8KWXFFiya2vjozSNWzgn-lfluZwMVrUVZnVo_i9QFG6_GkVemhPpjQ8NByZf0y7EmF4v7nuwDQXAQTNCcjKbaIGPYSo1GF4IzDSA2sLJii-bxOESRlkzVvpHPEvNexPWX07_YeC7ZoUcQDlG1LXKeUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kqoenx3NYWZkX94yobgZS0ftLxxQ5KJjE0EaYNAsdRwCS3ML_81pmd5Yzo9HW6C0M_EMFIn43E4oBGwfrE843BmW6onwyoWLS5lodH_wtrxCE7Gv_d8FhT9cQEo4CDWQvfm2K6L-2bzLRq2hUpJF4aOe7bejpZzPKT3i0X27kEia8Q1TswxyvrnAYgG6KUzT6Qs6E1yMKPYhzlAn6KoL6DbvFMo3A3dLp552_VeagN0nmsd2VfDFfwIBP5Vt1WPi2nX6Jtj_Gywr6A8wHExxL5lftU0CZUYGjn2R4o9LeFH9leYY1PegaG82un4F2KJ3MT6CI6gFiudZ9eo_MSzhuw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">تحركات امريكية واسعة في الشرق الاوسط ‏استعدادا للهجوم على الجمهورية الاسلامية</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/naya_foriraq/86182" target="_blank">📅 16:23 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86181">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">نايا - NAYA
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/naya_foriraq/86181" target="_blank">📅 16:17 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86180">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromابو مهدي الجعفري</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bJWCShKardVaTUX2i1RRh5mfB1BfeVWcVhLby4ao_xrvs2C3uxCUOJ9JRMzxwRu-S0zBw5K2EcRkteqhzKPBi_pf5OkD8AbMzJT2R3klI_B2_o2dGHkWJz3cupDRw49oYEZs8sKThs-yDgdhY0HkMgfRYxCmQisekRpACtNt7IcLiFlLHO_fcxu0ZTeCAZuXwgvS3-PxZQxMztSJAeDbgy3NeZthV0RWV7JlO2ZxR3Vl14FtULyQnhxC32Ai-MPDzosQPN6Vf1dHqhaoXfKX7CZ9f7DwTAvh8JxK7rQFQLdc9rU3grRmKSQ2QKA1jPBjwq_rE0h4_q-uKnOQ-9wm_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بسم الله الرحمن الرحيم
﴿فَلَا تَهِنُوا وَتَدْعُوا إِلَى السَّلْمِ وَأَنْتُمُ الْأَعْلَوْنَ وَاللَّهُ مَعَكُمْ وَلَنْ يَتِرَكُمْ أَعْمَالَكُمْ﴾
صدق الله العلي العظيم
لا حول ولا قوة إلا بالله العلي العظيم وإنا لله وانا اليه راجعون، الرحمة للشهداء والشفاء العاجل للجرحى، ونؤكد على ما يلي:
1- إن الدولة العراقية لا تُدار بمنطق الصفقات التجارية أو المصالح الاقتصادية عندما يتعلق الأمر بسيادة الوطن وكرامة شعبه؛ فسيادة العراق ودماء أبنائه ليست محل تفاوض أو مساومة، وهي تعلو على جميع الاعتبارات الأخرى.
2- ندعو الحكومة العراقية إلى إعادة النظر في جميع الاتفاقيات والعقود التي أُبرمت مؤخرًا مع الولايات المتحدة الامريكية، وإلغاء الزيارة المقررة الى الحجاز.
3- إننا في المقاومة الاسلامية سرايا اولياء الدم لازلنا ننتظر موقفًا رسميًا من الحكومة العراقية يرتقي إلى حجم الحدث، ويعبّر عن الوفاء لتضحيات الشهداء.
4- يجب طرد السفير السعودي من العراق فورًا، وقطع العلاقات الدبلوماسية والاقتصادية مع السعودية.
5- في حال تقاعست الحكومة عن اداء واجبها فعلى الشعب العراقي الغيور المطالبة بحصر سلاح الحكومة بيد المقاومة.</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/naya_foriraq/86180" target="_blank">📅 16:16 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86179">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cs6TlbG3_HStQ3__LcjsD3M7eFcFGXABoeItPsXnmi5RwuMRLnFflWba3Z-CbwcrI_jjM1EDgc5RfLK8_fnd_F1x3qhVX0VxeVlk4feXU-kVHkvDwE9xbsboViskdhcnYBwO_2t_H5fkrJqoN1hGAhYMXml2Wwr30J9xXwCtUpL2xHJ2R5h9iWZI52MtFDw4xtDIXOuO2SXyr24XrfZuybMhnbaBCymw7ebG0lZNGi9WQVe4yMSc7K5H6GMWXkwjzj8juUjRwmB9scwJqAvgKJIlNu6rL6TJ_p_tBpSrazNqPJjEssr32pqSYzqCAtXF6kO8X-TJTTy4XOUsSsCS0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
خاص لنايا | مشاهد من الاردن لتصاعد اعمدة الدخان بعد الهجوم الصاروخي والمسير.</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/naya_foriraq/86179" target="_blank">📅 16:12 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86178">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">بيان لرئيس البرلمان العراقي هيبت الحلبوسي يرفض ايضا تحديد هوية العدوان:
ندين بأشد العبارات الاعتداء الذي استهدف مواقع تابعة للقوات الأمنية العراقية، والذي أسفر عن سقوط عدد من الشهداء والجرحى، ونؤكد أن هذا الاعتداء يمثِّل انتهاكاً مرفوضاً لسيادة العراق، ومساساً بأمنه واستقراره، وتجاوزاً على مؤسسات الدولة الأمنية التي تؤدِّي واجباتها في حماية الوطن والدفاع عنه.
ونشدِّد على أن سيادة العراق ووحدة أراضيه تمثِّلان خطاً أحمر لا يجوز المساس به، وأن احترام القانون الدولي وميثاق الأمم المتحدة يقتضي الامتناع عن أي أعمال عسكرية تنتهك سيادة الدول أو تهدِّد أمنها واستقرارها.
وفي الوقت ذاته، ندعو القائد العام للقوات المسلحة إلى إجراء تحقيق شامل وشفَّاف في هذا الاعتداء، واتخاذ جميع الإجراءات الدبلوماسية والقانونية التي تحفظ حقوق العراق وسيادته، بالتوازي مع كشف الجهات المتورطة في أي أعمال عدائية تنطلق من الأراضي العراقية باتجاه دول الجوار، ومحاسبة المسؤولين عنها وفق أحكام القانون، التزاماً بما نصَّ عليه الدستور العراقي من عدم استخدام الأراضي العراقية مقراً أو ممراً لأي اعتداء على أي دولة، وعدم السماح باستخدامها منطلقاً للإضرار بأمن واستقرار الدول المجاورة.
ونجدِّد التأكيد على ضرورة تحييد العراق عن الصراعات الإقليمية والدولية، وعدم جرِّه إلى أتون الحروب، فالمصلحة الوطنية العليا تقتضي أن يبقى العراق ساحةً للاستقرار والحوار والتعاون، لا ميداناً لتصفية الحسابات أو تبادل الرسائل العسكرية.
خالص التعازي والمواساة إلى عوائل الشهداء، ونتمنَّى الشفاء العاجل للجرحى، سائلين المولى عزَّ وجلَّ أن يحفظ العراق وشعبه، وأن يديم عليه نعمة الأمن والاستقرار، ويوفق الجميع إلى ما فيه خير الوطن وسيادته ووحدته.
هيبت الحلبوسي
رئيس مجلس النواب
29 تموز 2026</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/naya_foriraq/86178" target="_blank">📅 15:57 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86177">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6c54053f3.mp4?token=nM0A6j9ZJlnFWtOXkRwruAab4UHFI_KqSVHg46PumN1uZYZRuJaGUQd_u-It4ghMVm8L5P2BDkCsiJTbYdvXAAZE8WJIERdqpHySG3OaDPd8ybcjMbBMXJ-RHZ7lJKTKTDk4H9xB2gHNNMbgQ5SPvohx9ipqfslxjgXEijUj-DvusRhTiFPLrYBUQax7PbOUuiIN7KWqjB_WSe1_EDx7wOe46vtrCMV8s0w-Ru2HqR-cCvSvJvYSQQL0QkqCJslH_8QVO93L7WjviEhWsbiDlXjo-OZxVFESC-ibeKBRBOaDoHdYmxX0V90olvJ9S-_sWSypKZUpLvnFA-U6hwmL1HTqjbKvLq65eJgl9O_LKtdqnqxafKz6i_zw8d7VKc3QXvlnElDB_U7UoIhyI-1FFHkNxQKlPALikdMlSfRserJZ1OflnmAwg4FsW5sBgcROh6ynqs_GTCcTY318SwrPQA2qgiLQhX24P99ks3H9xvcK5yw04BwPEHLZsUrliyrPMmpUdrcmI9yllJgPY8YEDSBac38aFOZcdp668pxvd5k29lgQ6iVMHlx8Rs5eBnfhQS_FkdRU_dBrCoEZ7NsPbMrQf-JW35zPiOoWmx2hdkG1zROkNJe6Oec2W5XEmgZBuj8JdMSlsRyQ0dlnvjOEu809sYSqGrYp3fBhKbaCvNs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6c54053f3.mp4?token=nM0A6j9ZJlnFWtOXkRwruAab4UHFI_KqSVHg46PumN1uZYZRuJaGUQd_u-It4ghMVm8L5P2BDkCsiJTbYdvXAAZE8WJIERdqpHySG3OaDPd8ybcjMbBMXJ-RHZ7lJKTKTDk4H9xB2gHNNMbgQ5SPvohx9ipqfslxjgXEijUj-DvusRhTiFPLrYBUQax7PbOUuiIN7KWqjB_WSe1_EDx7wOe46vtrCMV8s0w-Ru2HqR-cCvSvJvYSQQL0QkqCJslH_8QVO93L7WjviEhWsbiDlXjo-OZxVFESC-ibeKBRBOaDoHdYmxX0V90olvJ9S-_sWSypKZUpLvnFA-U6hwmL1HTqjbKvLq65eJgl9O_LKtdqnqxafKz6i_zw8d7VKc3QXvlnElDB_U7UoIhyI-1FFHkNxQKlPALikdMlSfRserJZ1OflnmAwg4FsW5sBgcROh6ynqs_GTCcTY318SwrPQA2qgiLQhX24P99ks3H9xvcK5yw04BwPEHLZsUrliyrPMmpUdrcmI9yllJgPY8YEDSBac38aFOZcdp668pxvd5k29lgQ6iVMHlx8Rs5eBnfhQS_FkdRU_dBrCoEZ7NsPbMrQf-JW35zPiOoWmx2hdkG1zROkNJe6Oec2W5XEmgZBuj8JdMSlsRyQ0dlnvjOEu809sYSqGrYp3fBhKbaCvNs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامب: تم تنسيق الضربات الأمريكية والسعودية مع الحكومة العراقية</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/naya_foriraq/86177" target="_blank">📅 15:56 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86176">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">ترامب يقول ان الهجمات بموافقة الحكومة العراقية</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/naya_foriraq/86176" target="_blank">📅 15:54 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86175">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">بعد قليل ...
بيان هام للمتحدث العسكري للمقاومة الاسلامية سرايا اولياء الدم
ابو مهدي الجعفري .</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/naya_foriraq/86175" target="_blank">📅 15:53 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86174">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">ترامب: تم تنسيق الضربات الأمريكية والسعودية مع الحكومة العراقية</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/naya_foriraq/86174" target="_blank">📅 15:50 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86173">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">ترامب: ردًا على الهجمات التي استهدفت أهدافًا أمريكية في الأردن، سيتم تنفيذ هجمات على إيران.</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/naya_foriraq/86173" target="_blank">📅 15:49 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86172">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">‏ترامب: سنضرب إيران بقوة.</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/naya_foriraq/86172" target="_blank">📅 15:48 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86171">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">‏ترامب: سنضرب إيران بقوة.</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/naya_foriraq/86171" target="_blank">📅 15:47 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86169">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sdihB0WqOATaYZSghIw7qpWnfyncWLEsovuUX9SBHoiUDldS318lMt4zI0zIVFcUTW7t8CTDNe_QkFjQpW08aXUjILpUH6VATXEmlJkTIgf68NE-pnFikRhmLsfBJkUy2Z1zlfi0cGqY5TD7pbCVtNUMIhSMAYjdPkcRvVk_qQBM1OfIA_H9EltOL7lMqvdGkyaVI-kTkgRc3co8tr_a1BG8CpWXCK1LRBwW0FIRtPZ4_eGohTUQgvlNYXUCBgbo3PvkdQvmxULT--0Y-bH0rE0jwfwS-IKDYw0BZsahTC8fM-99CwufRqifzKySLfhkethV3ftNMjRDh3XIwjMxpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tS5wyCf1k-eEPFzdNyBs3urVy00wqAC-ErD0cZXJc8J5lK-Px7qJb61b-NDGBs_hU-VHgihnqkbMbi7_TKmX0Qf3gxipDcluklGbm6lnHLL_53LRASNCZFDzQW9haoinC2h0wi5W_mQ7bIa286hqY18WdfeOjdit2n-qvmtxA3hW9YoIy1Q_hWmtRd3LAKUHXAXUR_pZBFI5aOXhmlni29C1PXjHzn_8KNCc9-qiaHj1nMBc19EB4hZORvS4F24XV_aQvr9sDfx8IQ3c8xChwCLDxEwkaNCR6PZ9ULyYx5ISHtwdW7ZKBWBEB6DDCfEzd4nA5rqVpPew4lESHp3iHg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇮🇶
النائب سعود الساعدي يوجه اسئلة إلى كل من رئيس الوزراء ووزير الخارجية:
ما الإجراءات العسكرية والقانونية والدبلوماسية التي تعتزم الحكومة اتخاذها، بما في ذلك إمكانية إلغاء زيارة رئيس الوزراء إلى السعودية واستدعاء السفير السعودي وتسليمه مذكرة احتجاج واتخاذ إجراءات بحق السفارة السعودية فضلاً عن تقديم شكوى رسمية إلى الأمين العام للأمم المتحدة على خلفية الهجمات.</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/naya_foriraq/86169" target="_blank">📅 15:41 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86168">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">كلمة الشيخ حسن الشبكي آمر الفوج الرابع في لواء 30 سهل نينوى الان بعد وصول جتْمامـ...ين السّْهداء الى العاصمة بغداد...</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/naya_foriraq/86168" target="_blank">📅 15:24 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86167">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">نايا
المجاهدون العراقيون الذين تقدمت بهم السن يظنون أنه إذا فرّوا من المعركة، فإن المعركة أيضاً ستهرب منهم!
كان الخطأ الأكبر في حسابات جبهة المقاومة أننا كنا نظن أن خفض مستوى التوتر سيجعل العدو يتراجع أو يغض الطرف.
لكن العدو يستهدف وجودنا نفسه، ولا يفرّق بالنسبة له بين ….. والكعبي.</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/naya_foriraq/86167" target="_blank">📅 15:23 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86166">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">نايا
إنّ التجارة مع الولايات المتحدة، ولقاء السفير الأمريكي، والانحناء أمام ترامب، لن تحمي الإخوة العراقيين من الضربات.
لقد انتهت فكرة الحفاظ على النظام الشيعي في العراق عبر مسك العصا من الوسط بين إيران والولايات المتحدة، صباح يوم استشهاد قاسم سليماني!</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/naya_foriraq/86166" target="_blank">📅 15:22 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86165">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">المجلس الأعلى الإسلامي العراقي
نستنكر بشدة العدوان الأمريكي- السعودي على العراق، واستهداف قواته الامنية الرسمية في الحشد الشعبي، وما أسفر عنه من سقوط عدد كبير من الشهداء والمصابين، ونستغرب ان يأتي هذا العدوان تزامناً مع تحرك حكومي عراقي جاد لفتح صفحة جديدة من العلاقات مع دول الخليج، بعد ايام من زيارة السيد رئيس الوزراء للولايات المتحدة وإبرام 48 مذكرة تفاهم ضمن توجه لبناء شراكة اقتصادية، والانتقال الى مرحلة جديدة من العلاقات.
إن ما حدث من عدوان قد يندرج ضمن مسعى "صهيوني أمريكي" لمنع دول المنطقة من بناء تفاهمات مشتركة لمستقبلها الامني والاقتصادي بعيداً عن التدخل الاجنبي، فضلاً عن الحيلولة دون استقرار العراق، وبناء اقتصاده، واستعادة دوره كمحور التقاء دول المنطقة، وكوسيط إيجابي لتذويب خلافاتها وبناء تفاهمات دولها.
نؤكد ثقتنا بأن العدوان لن ينال من إرادة قواتنا الامنية، ولا عزيمة شعبنا، ولا مكانة العراق ودوره، وإن كل المؤامرات مصيرها الفشل أمام إرادة شعبنا العظيم.
نسال الله ان يرحم شهدائنا الأبرار من أبناء حشدنا الغيارى، ويمنّ على المصابين بالشفاء العاجل باذنه تعالى.
د. على فاضل الدفاعي
الناطق الرسمي للمجلس الأعلى الإسلامي العراقي
٢٩/٧/٢٠٢٦</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/naya_foriraq/86165" target="_blank">📅 15:18 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86164">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">مقطع يوثق آثار العدوان الأميركي - السعودي على مقرٍ للحـشد الشعبي في سهل نينوى</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/naya_foriraq/86164" target="_blank">📅 15:12 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86163">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">الشيخ قيس الخزعلي: إن قيام دول أجنبية، يدعي بعضها أنها حليفة، والأخرى أنها شقيقة، بمهاجمة قواتنا الأمنية وقتل أبنائنا فيها، بدعاوى لم يتم إثبات صدقيتها، ولم يترك المجال للقائد العام للقوات المسلحة لاتخاذ الإجراءات القانونية والأمنية المطلوبة في حال ثبوتها، هو انتهاك، بل استهتار، بالسيادة العراقية والكرامة الوطنية، وهذا أمر لا يقبله أي عراقي شريف.</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/naya_foriraq/86163" target="_blank">📅 15:08 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86162">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rzz2J-YKuLWYllcdKBFBUe4Lf872hEvKpKqpsurP-ZpF9BJMinAHu1Zd-GIvt2qcDZ82q2tJ7-R3cyqSx8ZLt-sHZVSZw7VioBycUWi3mK0M74i4Fr79T1Z4iTcJtO7YCYa4IGVw0LWblXkRWNbLstmGQfc_tDQFfQacb8Q_DzL8R63YypNHXRFixZC7Qrc8LYE85qmNWR0ywuTOSimX_sAo6wu3Nx6mM-_i3ynu_f4tfADXunGkBiKOMwDz1kDpgx0o5LKtaNMX8nwiumE4_ofXnlRIcnJNC3uaoCfA592Ef4F8ajrmKxmwq_aieHwaMRso8w7Ue-VPhb4o5fr2Tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">A night before the incident</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/naya_foriraq/86162" target="_blank">📅 15:07 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86161">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p3eFZ86ZRZiA5nRaHcaxaUyBBdM7GG5vW_TrW5uye_IvVdMD3TkP_WPDD1RxGoT93gYZXbLMHqpfC_-PcokFGn_Bq_XpWiV3FXcQjii2h5jlBL_PP6xy5rkF6eP7M8LjZbnFuNy1EPItItizQWceUBONyf1tJfjDVbyGg0PXuzunVRvLu0lq4dXv7xTvuwW-lkxg-ZLmMDWZ5901zG0eEU0pP80J-dr5xk5YXcAXGlEteYnapsCfD6Wryi_JkLv4arGETtKTaoPNNw9Wx_abQ8_uQdaOqdDFBceMBDwAgokl1oLIYnUs6W4LUNv5WEm_IlGlFYnz_HDWRJKx4PLpUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حسين مؤنس رئيس حركة حقوق ينشر</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/naya_foriraq/86161" target="_blank">📅 15:05 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86160">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ef8Bf69eISsObtMNocwG7LUv1wqu4j-8_hczxDOQpuqSPfyJkdkdp27VIEc8D09vbgKZl4wRx5OhVWzZQFpywkICU34bw_e9DnWnYUSQyFML1Is3-YwRxJJfkHjQtSFvpa2cNmpEpCTaaHMo2xhjipYTU5IFdWzi8a1E0YccOMGTDvdVc0AITQ40nK7PWbmqT17WugQT0Gj8KfzkMJGjZ7RSVG9u30kGIrteXy0nnH8AMe_NrryCO0Ew4Q3UocgYHpkHYx94bsQAEp98oquCHvstzThxQwiDdSrfrT1a_Z6bADnXmBqnNQh5Npb6ItL2Yct4b0QFbtxmIXnOfz5V1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🐦
بيان صادر عن حركة النجباء
:
بسم الله الرحمن الرحيم
﴿وَسَيَعْلَمُ الَّذِينَ ظَلَمُوا أَيَّ مُنقَلَبٍ يَنقَلِبُونَ﴾
تطل علينا قوى الاستكبار العالمي والتبعية ممثلة بالاحتلال الأمريكي الغاشم والتحالف السعودي المأجور، لتؤكد مجدداً وجهها القبيح وعقيدتها الدموية القائمة على الغدر متجاوزة كل أعراف السيادة وكرامة الأوطان..
فجر اليوم امتدت أيدي الخيانة والإجرام لتستهدف بطائراتها وصواريخها الحاقدة عمق المدن العراقية الآمنة في عدوان سافر يؤكد بما لا يدع مجالاً للشك أن هذا الحلف المشبوه لا يعترف بسيادة ولا عهود، بل يسعى يائساً لإركاع هذا الشعب الأبي الذي قهر طغاة الأرض..
إن المقاومة الإسلامية حركة النجباء إذ تدين وتستنكر هذا العدوان الأمريكي السعودي الآثم، فإنها تؤكد للجميع أن دماء شهدائنا الأبرار لن تذهب هباء وأن الأقنعة قد سقطت إلى الأبد تحت وطأة الحديد والنار، وأمام هذا المنعطف التاريخي الخطير نطلق مطالباتنا الحاسمة وغير القابلة للمساومة، موجهين رسالتنا المباشرة والحتمية للحكومة العراقية والجهات الرسمية بما يأتي:
أولاً: طرد المحتل وقطع دابر العمالة: إن بقاء القواعد والمقرات التابعة للاحتلال الأمريكي على الأراضي العراقية بات خطراً داهماً يهدد أمن البلاد واستقرارها.
ثانياً: قطع جميع أشكال التعاون مع النظام السعودي المجرم الذي أثبت أنه رأس الأفعى وممول الإرهاب ضد العراق وأهله.
ثالثاً: نطالب الحكومة العراقية بالخروج الفوري عن صمتها وعدم الاكتفاء بيانات الشجب والاستنكار التي تغري المعتدي وتدفعه إلى التمادي.
رابعاً: نطالب بتأمين منظومات دفاع جوي متطورة وحماية سيادة البلاد وأجوائها بشكل فوري وفعال ومحاسبة كل من تسبب في ترك سماء الوطن مستباحة لرغبات القتلة.
خامساً: إننا في حركة النجباء لن نسمح بأن يدنس أرض العراق طغاة واشنطن وأعراب السعودية من دون ثمن باهظ يدفعونه من مصالحهم وأمنهم.
الخلود للشهداء الأبرار.. والشفاء للجرحى..
المقاومة الإسلامية حركة النجباء
14 صفر 1448 هـ
29 تموز 2026 م</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/naya_foriraq/86160" target="_blank">📅 14:52 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86159">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">رئاسة الجمهورية في العراق:  ندين القصف الذي استهدف مقرات قوات الحشد الشعبي في عدد من المناطق، والذي أسفر عن استشهاد وإصابة عدد من المنتسبين، وتعدّه اعتداءً مرفوضاً وانتهاكاً صارخاً لسيادة العراق واستهدافاً لمؤسساته الأمنية الرسمية بما يتعارض مع قواعد القانون…</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/naya_foriraq/86159" target="_blank">📅 14:49 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86158">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">رئاسة الجمهورية في العراق:
ندين القصف الذي استهدف مقرات قوات الحشد الشعبي في عدد من المناطق، والذي أسفر عن استشهاد وإصابة عدد من المنتسبين، وتعدّه اعتداءً مرفوضاً وانتهاكاً صارخاً لسيادة العراق واستهدافاً لمؤسساته الأمنية الرسمية بما يتعارض مع قواعد القانون الدولي وميثاق الأمم المتحدة.
وفي الوقت الذي نؤكد فيه رفض العراق القاطع الاعتداء على أراضيه، نجدد موقفنا الثابت الرافض لاستخدام الأراضي العراقية منطلقاً أو ساحةً للاعتداء على دول الجوار أو لتصفية الحسابات الإقليمية والدولية، انطلاقاً من الالتزام بمبادئ حسن الجوار واحترام سيادة الدول وعدم التدخل في شؤونها الداخلية.
وتدعو رئاسة الجمهورية جميع الأطراف إلى احترام سيادة العراق والامتناع عن أي أعمال من شأنها زعزعة أمنه واستقراره، وضرورة تغليب لغة الحوار لمعالجة الأزمات بما يحفظ أمن المنطقة ويجنب شعوبها مزيداً من التصعيد والتوتر.</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/naya_foriraq/86158" target="_blank">📅 14:48 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86157">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🇮🇶
🇮🇷
ايران تدين العدوان على العراق  أدانت وزارة الخارجية بجمهورية إيران الإسلامية، بأشد العبارات، الهجمات العدوانية التي شنتها الولايات المتحدة الأمريكية والمملكة العربية السعودية على بعض المناطق في العراق، بما في ذلك الهجمات على المنشآت والأماكن التابعة للمؤسسات…</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/naya_foriraq/86157" target="_blank">📅 14:43 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86156">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t7lqGi4id_aC1y45Zg4magML4xNaRdaJQA1k1Y4vjcRR_6OZBgSZBSE_iCYO3sJ-dC6YtmAb3s949Qg1iOoBJFUGsdLElFXWfUfXvKPz5TIw61qNn4ZsTGi4SuHTHzMkbeefJYlqw6T5uWMZ0lBB-UKjowYay-kjQ0VGSFarCrgg5WvnxE8Pc_KoDfi9bB-4oT4NvNc3O_m5RUv3qKjg_8araupKgrXOPJ9KrzlicX1KyaiwhyinV5hUjF2bA2_3led8saOHIx8YhiydZmnctwSJl06TpJeJGGPwGzk8f2l0wzNWMm9f_SjTN_E-CH7UbeM-ftKE2c-YZakwTiBfkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
🇮🇷
ايران تدين العدوان على العراق
أدانت وزارة الخارجية بجمهورية إيران الإسلامية، بأشد العبارات، الهجمات العدوانية التي شنتها الولايات المتحدة الأمريكية والمملكة العربية السعودية على بعض المناطق في العراق، بما في ذلك الهجمات على المنشآت والأماكن التابعة للمؤسسات الرسمية العراقية، وكذلك على مخيمات ومحطات استقبال زوار زيارة الأربعين الحسينية.
تُعد هذه الهجمات انتهاكًا صارخًا للسيادة الوطنية وسلامة الأراضي العراقية، وتُشكل خرقًا جسيمًا للبند الرابع من المادة الثانية من ميثاق الأمم المتحدة وقواعد القانون الدولي الأساسية، وهي جزء من طموحات الولايات المتحدة وإسرائيل لتوسيع نطاق الحرب والصراع في منطقة غرب آسيا.
وعلى الرغم من إعلان وزارة الخارجية عن تعزيتها في استشهاد مجموعة من أبناء الشعب العراقي الشرفاء في سياق هذه الهجمات العدوانية، تؤكد الجمهورية الإسلامية الإيرانية على دعمها وتضامنها الكاملين مع الحكومة والشعب العراقي، وتعتبر النظام الأمريكي المثير للحروب وحلفاءه في المنطقة مسؤولين عن العواقب الخطيرة لهذه الأعمال الإجرامية وغير الإنسانية والتحريضية.</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/naya_foriraq/86156" target="_blank">📅 14:32 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86155">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p7Tr0MmzyV5EW0iXgkymypUr_UvuiCFIzjfec7g5gYpAN8yxLqelxXpUbtPEVO7DWPLh6Fhs5ga_eH-3KfTykpuTgQsbTkHXWUwL8k1J0WGuUz_YkqoJqBpoJ_0pKgaGm18U73Axn7BSMGm2dspjHzRJZYfr2ZvnwCN5pJCU1gTh8SLpAqvWHNRwJCmQmrZU5qIsdPejao6f0uU97-VzxtR2Y8W3kJuJEdgz3bxytEnIDlSA0cPO38U8oe7b0OxjuEfqKp71jg13QopsfWQ88QoN8AbbENsHtQ454b6UWzvg2HujAJv9KB8N3unuejjirO-_DyO31XPbn5g3P8x6hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سوف تدفعون ثمن استهداف العراق غالياً</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/naya_foriraq/86155" target="_blank">📅 14:23 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86154">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🇮🇷
وكالة فارس عن مصدر:
مضيق هرمز مغلقًا بالكامل، ولا يحق لأي سفينة عبور
المضيق.</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/naya_foriraq/86154" target="_blank">📅 14:19 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86153">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">طيرهن يا ابو الاء ..
الشعب كله معكم</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/naya_foriraq/86153" target="_blank">📅 14:18 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86151">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">نايا - NAYA
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/naya_foriraq/86151" target="_blank">📅 14:13 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86150">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/elOQAt0QakbxgOxUaB_GkWZCMcZMiA4jHPbXm13c_kW1rkXSJex3JY39RywpSFOZfyJhLeTYYoPKkgasSkoTn4lX9y9V7eeEjd9_t_bFrfuvj9rdpHGmfKIlkQ-r-IilW7SXJ3yXBETTMOCFrGQ3DVvXdQrgPomvdyTIDwrGyY6t1DTE3Rnq-KYw2z0BRDoAq62OXeD-W6Zhp2QBLHJH_Y4okDNumZLcLF82PSh8r68nWHOQckmsUCwv6kfnjtcpRhQnC2FYpzJKnpraiBue8Yv2EUEIvfJzUHxfZy2UJpWVkwLFYW79JtVNawKTI26mAzGYVIYZi6jHOchWLYIc5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">إِنَّا مِنَ الْمُجْرِمِينَ مُنتَقِمُونَ
وعدٌ إلهي لا يسقط بالتقادم، ولا تُطفئه الجرائم ولا يغيّبه الزمن</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/naya_foriraq/86150" target="_blank">📅 14:13 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86149">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🇾🇪
🇮🇶
وزارة الخارجية اليمنية: للجمهورية العراقية ومقاومته المجاهدة وشعبه المسلم الحق المشروع في الرد على هذه الجريمة وفق الأعراف والقوانين الدولية.</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/naya_foriraq/86149" target="_blank">📅 14:11 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86148">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🇾🇪
🇮🇶
وزارة الخارجية اليمنية:
للجمهورية العراقية ومقاومته المجاهدة وشعبه المسلم الحق المشروع في الرد على هذه الجريمة وفق الأعراف والقوانين الدولية.</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/naya_foriraq/86148" target="_blank">📅 14:11 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86147">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A81wf95pBRS2VSSIXWbdlAVbOrK7RAnKSJwSCjp9HWn8CX1VHgcbUHjZgguZDvX4lLadiizIUwRrZnyvB0jNK4Hfug9E8gvS-r0VlhyyvOLIaGpB0wVVs5lYCyivlnWjfvG03wiu2JMVc4ZSytWeYRAuB3Bo7s_IcXJeCqqlNYKEzF76KBQUS8-MvTVDCfHWsVxkpF0lY32C09pU-fM8eRYhrUK1G1c8UHj_ieOYS_pMxTqUpYCyi-O9URRhZfoX_hf1ztFywupaPAlDQ5de4yP5D0kkDxVZ1RVeyw12yv0AMeIv1z26sPA0pVjWy5a2Y5wCzP9gzEzalI8JP07GTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">من بوت نايا   ...أمانه من احد متابعينكم شنو تريد المقاومه بيتي والله ابيعه الهم وانطي فلوسه ويقصفون ال سعود وأمريكا نفسي ودمي فدوة الهم عائلتي فدوة الهم شنو يريدون مكانات بديوانية وسماوة  حاضره اني واهلي وكل عائلتي فدوة للدماء الطاهره يشهد الله حاضرين حتى…</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/naya_foriraq/86147" target="_blank">📅 13:56 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86146">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🔻
الحشد الشعبي العراقي يدعو جماهيره للمشاركة في التشييع الرسمي للشهداء اليوم من امام مبنى المديرية العامة للإعلام – شارع كريم الندى الساعة الرابعة عصراً.</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/naya_foriraq/86146" target="_blank">📅 13:55 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86145">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">هجوم مسير يستهدف موقع الحزب الديمقراطي الكردستاني الإيراني المعارض شمال شرق محافظة أربيل شمالي العراق</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/naya_foriraq/86145" target="_blank">📅 13:51 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86144">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">اعلام العدو:
تعرض آلية عسكرية من نوع "D9" تابعة للجيش الإسرائيلي للضرر الليلة نتيجة اصطدام طائرة مسيرة متفجرة تابعة لحزب الله.</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/naya_foriraq/86144" target="_blank">📅 13:38 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86143">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OM5wVZ60JCZfM7YX-n8EM_S3v5QycqXpid9lV7Q08JIg6MMrF5NSpldtUHN4rDgw57dRUoReFqaAAxI54Nb73w0Ja6KQ2G9_G2WHH9EyF5VVP3HvFJieKBUAsWHnMqP-eY0CmHqcgLGNSZLrhSyIC71Lt1aGxYlh463yimjgAyJP8EJ5Lqjci1r5JzR53kAFXxssrOQLG20a6Jyx6BVz_tdOEvfVrqER0zt9ffezGC-P_-3hFt3wdbkAm8tEh-ZDXX3rPvTDDvfSz9Y4JP3Arp6T4K8HPf5XViHuz348nY9Inm9KfNY4mHJI0Hs7iAkDkZXHhR_8JKRZIFaUaU1Bxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
خاص لنايا | تصاعد اعمدة الدخان من الاردن</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/naya_foriraq/86143" target="_blank">📅 13:23 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86142">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8c7587bf80.mp4?token=nodHRyTPG5iQ-sR_4GV1-0yFHNQ1OmSqZLvVTfwc7NF7jJBZntu7XW1rwnfJ1sUWshelhsDSw207MgiZv52gfVl7qG5l15zFhqkfZuJZQMliwrWKnEmI-kAVc4ig-sRgjhJPgH8dImxEs44Qf3DQEhb5xCHqgTCPX1SGHxMfTjl4nsbmSjDMFGGgtwH2tDGDkZAa8xTk_PFl8uQfoKxozBNrrd0CPphDW3VCL5lqrRbTyVdTH7BL5paPD9uAH5LfQi1blD61k9da__oztt-EOWLy7Lw8eMS1vubxwcvgpFfY2riTk0pC2C-e1Q2dWMyxU27QsNfu_fY_8E3ZkLdOBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8c7587bf80.mp4?token=nodHRyTPG5iQ-sR_4GV1-0yFHNQ1OmSqZLvVTfwc7NF7jJBZntu7XW1rwnfJ1sUWshelhsDSw207MgiZv52gfVl7qG5l15zFhqkfZuJZQMliwrWKnEmI-kAVc4ig-sRgjhJPgH8dImxEs44Qf3DQEhb5xCHqgTCPX1SGHxMfTjl4nsbmSjDMFGGgtwH2tDGDkZAa8xTk_PFl8uQfoKxozBNrrd0CPphDW3VCL5lqrRbTyVdTH7BL5paPD9uAH5LfQi1blD61k9da__oztt-EOWLy7Lw8eMS1vubxwcvgpFfY2riTk0pC2C-e1Q2dWMyxU27QsNfu_fY_8E3ZkLdOBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاعد اعمدة الدخان من الاردن ويمكن مشاهدتها من محافظة درعا السورية</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/naya_foriraq/86142" target="_blank">📅 13:23 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86141">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">انفجارات تهز الاردن</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/naya_foriraq/86141" target="_blank">📅 13:22 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86140">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">انفجارات تهز الاردن</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/naya_foriraq/86140" target="_blank">📅 13:22 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86139">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">وزير الاتصالات العراقي مصطفى سند: منطق السياسة وأبجديات بناء الدول، هي ردع المُعتدين بما يتناسب مع الأعتداء، لا يُرد الشر إلا بالشر. رحم الله شهداءنا واللعنة على القَتلة والمُتخاذلين.</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/naya_foriraq/86139" target="_blank">📅 13:09 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86131">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EEAEGKuHNoKs-epEeXmOPL9GKznuqGlDzbMAp75AzDDDq_eVG3YR9mtov4DpEX88_080S4f8-OYvfADxLhSssAPBQ-l_uaaUDkXPI452Ls9uclwoRfLiEn3CW8lxP7APKz5Pk1RONtxabICjwfvWdmsRaZuzrL0ziUyf4nKtgSV6phInJM1MyZ9d7DRRz9NjI0-4fGVnOANpxY3BaISVQK5VamuxfIs7lA4n8hVrwrANiGhTuOSzIKBtGBR1Jd96wk-1c29CTQUysqn5zB5qgsnn9qEuC27aUZ7EBlIMFyksrWGyBysrQTVOdLT_ogTrumGnPcXN3EBLn4p27TZkUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mlY-Y1VNVSjuP9z-RcWKYUWahYUphEaT50GkTSTHjy5qLO7bYG74AFWJgPGOocgN0qFMkMzKNu7TymZfPg4rMzvIPG1XZf1fFnsKRWULLnYUZtOG0bYDczNjrlVCyj8ObssKsYBQjFagYFBHuAcz-TM053ekBzdhBEmFrEriE_u6PglgHowLiyVXs5oabCeEf5V-ICTwmELUOHjw5Hw2UKT7Xfs6U7CJsryjFE0rV9nHX-gF6bzM_fBLeQgvJiy4rvZyAOzXednZhOYDAnn5VTFDCkrrNfUaI6r6leg_ECArqYwHpDg5nlO2Bl4bBgMT371earxtwKRCj5qS4DisyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GmQ7K3Qk2Ej5a7zq-Qx3TZl2cdOVS6WE5GmSOIXfDHkGnP99fxS6nXOxKJOmFbFxdsEukXsmwzkwC0-qbJ6uaP5ZAhVudGH1cUzX26X_jOg8vLuA3AqYMVmUnTnhT3pyQxHSgpAJD_3-HPUjBsfrbaWP8f3wPuQSe_EYJw2pys2dUjbEdu4hGY1AGY2p1-sIF8UmLn-Wz-Yo8hlSH62ycoomiaWMoQtXWS2posxLQ5kXm5n-x5DCGV3jwKprd4-Mt_0xhKZQTAZMHnYlNV8QMxns_xHa30n8uNNzqwUmevMYBACxGKtn6DO9X6UeaTwOjZrj_H7oFkr0sfFzy6r2JA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/p2HtY97-_gGlrwI9BmX6ez2uB-v1zDYyux5Kz2p_AI_9gX9tEB93S7YzS64hROuyswQ_uo4wHPDBFKs2NORace0t_mSF5vRKbh1otxoP4v7qZqCcVdp14IgHvmFPwrJRK0QU732NsI6gA9gp-8c_ghvg_gZlKHedgEHzb_KBr4Gi3neCSPSa7th2skmQQiPDxNKU34ufQfW9hS-viF7-OLv9tggmn2tiiGDSxY3q-WGnT_QBx9Av1FucVB4zA44bXiwdCfWTIBrjaL4Lm5Drny_ZIrHwpl2o2Y8hi_hLtZr6UmXsLgm8Z24V9tBTaFVw5zuprtKrbmxhycGTrvSuKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TofkL1vg_dFYDN4BDatgAPHISFhwIG6tn8LaFNGN_96orUeFJfMozNU1kY46UhaB6PNZp3n3WFbXgs2sgW-LAeOL8n8MdL80u4PaNHTCs_iV1cGv-H2nqL_Fixp3FI8tnvA_3obavzA0tBmNkMWOKJtscV-dTW8-qb18nxuQWGK_gnKqzGXGnsDZqBQqgyl0RtdmPvH88kQyzkQJPCQtarpCTlfM0CS-wdKPNyyjwJVXBW4slFZho1MTwxM3psKzk72LiRuV8DPWAeBNy9PCPPVC2rSAU941Tfi-8YesDKkWnN0uOcNyiG8SGEnnHcXu5OkKNz649mev2_83G61CNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XY_1NlaIEvi942UwNKor54nmUEsc0M1WXW-K7Jz66I0M4xmXCetN8qWzPQB6dq04DCRJc0BnPAWEvgXR8BITK2VYjAzboWyNLaXzTgz7ThEFL2KFB5Bua_f8YlMkDzmi6qDLTNbzICif5xhlscCIHVrQZX4gIaqBKbMXIcoCDymyGp3c-vycK8YwZLuctdvpR-MSmuft_ntXNC8OnlLC7MkIsGZ2TIs7Euh9HUm-DFNjEYd22dTjWQtoBUyQx7BJ-nxe4MmFuWvTNChOmvf_GPqkGM-P_255QBgpOAtIS27Bfiht_txKKB6CfnMJt-H-WnMo1Ry9bKfEY_LqawQE5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JZHTxDl0aH9U7n8v3IpJ4Cd1rgk5_w8K1mcbsUtE2Xr7in-R2uQSxKQdQ4UP4HLAARrSOx0f_lUhPEE1d-p_S9D6LewXhAL9VSaElDvMeqxgFPqyTQhFagJGyIaiLj1PSfyUfe4ekcMsar9JLvItAYMSiRoG77aMaoZp13cIjlCYWq6HeuECQKxuCcbUJGBtppQOlnSZRPPp5YclhB-OQBCA-QaByuvoC2ZslHFw9aT2Hz5fU91fYz4GLQaxmUwV-w4Ogl0DCauQ30lZYLdpAPhOECPoPvrgBBO1yUkB-OY7jNa4jynATzk0Qjp_luhN4pg288fgf_DrmvsLnM8SiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jxpD3EbopQ0r7dw3CqLkW8m3QwuJXeWaJIn4gM_vcZHS1gz2ej4b2U_cekAJSa1VSvqQn-ztFss82zRm5_67swhZMT9QU7waAja0KUcLehjL1ktXvlPjFVb1-OsuCVrvRa2aZwk51GrtK0AGM5RHjP8fdzqLsDxpZ5bSlbPfPINWsPyh22Fg_9wUf9uaa5QsupElNsarob727ezSKEIcKP7Tkpjc24nWZ1JWEuPOXBaRRXzSbB60gmCfWK85nXxdFcAw7knSIwmJL6SbxLHbVeIl6oBLNfj4Kwtn-vIe6MeFBl-MxfBsXoAd5yO-75ToWP6Bw_9jDwmy17P5iqI1Fw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">مشاهد من الدمار الذي حدث جرّاء الهجوم الإرهابي الهمجي الذي شنّته السعودية والولايات المتحدة، واستهدف المقرات الرسمية التابعة لهيئة الحشد الشعبي، في سياق مسلسلٍ متواصل من انتهاك السيادة العراقية.</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/naya_foriraq/86131" target="_blank">📅 13:05 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86130">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gePBlzEnbOeiHh1FWiqVMl2NvxnU6x3ABOpWqhYlCyKys1TXcTKLqjDXvkOkIaxBygguPmt9NHl--jlO7s5PGIk4dnHllN67mQ4HtruYmj39ipj52e7EdOLOjZDAQ0Iplr_SIxBt0c_qtQoVkYHcANzVCcWWC8hXdbXN9XwAW9C0zgeMqD3pJDx1scIh8mOZlVrOC_z0RBLS6RmGxHMo266Ts25R2d6jRSFcl7dz9cHlGIjlLXCsamx9DdCTZ3Z-1qMQ85pDLhodw_rIsx3tol_PHgMzAsnRq3aHhMX6zbufTc3FetbHj8c4-dRjAPiKrqFmgw4_qjrToZZB_9qzFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
🇮🇶
الحشد الشعبي العراقي:
امتدّ العدوان الإرهابي ليطال حتى بيوتَ الله، في انتهاكٍ صارخ لكل القيم والمواثيق.</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/naya_foriraq/86130" target="_blank">📅 12:59 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86129">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/05368b5b56.mp4?token=WGNRySribZwLliFdxGSLT1uK-8XB_rNRQCk6UcNvwSCkTeG8Cn9iuk85iIeJ01vbmSDVsHsPzMJO1MO9icIfdlLN1X9VdMJqwFGlszixdjOYLpBbgZ5407o0J29i3YmobodzQY4fOb7PbJEKi_FClyiwPVDFaR94nsV8N_QUuN8JLpIWvzsbeJZHEiksKJj2VwqzDrUAsuLVjpyeE5jlmloKeX11RoEP9NgJnwoLhgP0q2gWCfR8EehQwC94zfq2chCkVoDLkEsdImHLTxeHHrPAvddNZy2t-hF4-5jA2jFgo34qoa9Q5czohRWgH3a-BxF2RS5eAnLPcaVQsxam3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/05368b5b56.mp4?token=WGNRySribZwLliFdxGSLT1uK-8XB_rNRQCk6UcNvwSCkTeG8Cn9iuk85iIeJ01vbmSDVsHsPzMJO1MO9icIfdlLN1X9VdMJqwFGlszixdjOYLpBbgZ5407o0J29i3YmobodzQY4fOb7PbJEKi_FClyiwPVDFaR94nsV8N_QUuN8JLpIWvzsbeJZHEiksKJj2VwqzDrUAsuLVjpyeE5jlmloKeX11RoEP9NgJnwoLhgP0q2gWCfR8EehQwC94zfq2chCkVoDLkEsdImHLTxeHHrPAvddNZy2t-hF4-5jA2jFgo34qoa9Q5czohRWgH3a-BxF2RS5eAnLPcaVQsxam3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صور من لحظة إطلاق الصواريخ الباليستية في عملية "سحر" التي نفذتها اليوم القوات الفضائية التابعة لحرس الثورة، وذلك في إطار عملية "النصر 2" التي تستهدف قاعدة جوية ومركز قيادة مركزي للجيش الأمريكي في الأردن.</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/naya_foriraq/86129" target="_blank">📅 12:55 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86128">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🇷🇺
🇮🇶
السفارة الروسية في العراق
:
تتقدم سفارة روسيا الاتحادية لدى جمهورية العراق بخالص التعازي وصادق المواساة إلى ابناء الشعب العراقي الصديق وبالأخص إلى هيئة الحشد الشعبي في استشهاد وإصابة الأبناء الأبطال نتيجة الضربات على مقراتها في عدد من المحافظات العراقية العزيزة.
إن حياة كل ابن الشعب العراقي هو كنز ونشارك ألم اسر الشهداء والمصابين وندعو الله سبحانه وتعالى ان يعطي لذويهم وأقربائهم الصبر والسلوان في هذا الفقدان المؤلم والموجع.
الله يرحم شهداء الشعب العراقي الصديق ويغفر لهم ويسكنهم فسيح جناته. ونتمنى الشفاء العاجل لجميع المصابين.
انا لله وانا اليه راجعون</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/naya_foriraq/86128" target="_blank">📅 12:48 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86127">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G8kxpFdPP1D6emJe889RDEVBYFJ7rua_7WQEwdroQHpEf2iXNuXSAmG525NjTI5OCUw2yWJBOiYJ8riSqBaNo_0PIOe_Cbvkmqp549EHUQ0cNavObqGwltHfUkEfpTGU-b4cLlDuw6raGHdVKFwt-Uf5JLZSEYgctPe40siX9voDhRUtM-hDlHJh9-SKmlYJKtFEgBc5IHp17PAVQyUpJi_5RVPJRc9asmgsL2oNVPCtdd6wBmaFCaPFa8r2NtS6yCO3kfaNvAvcWISGO7U8Wz2SFL0tTwRIuDtHwZluDKZL_Svp2Nv0CaSO5lB3NSiU9_8oYxiAPfRDphdEcaJyoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الحاج العامري ديالى تعرضت للقصف   هل سوف تصمت بدر التي حررت تلك المدينة بدمائها عن عدوان ال سعود ؟!</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/naya_foriraq/86127" target="_blank">📅 12:39 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86126">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EeYjnmEqLkn1XdrU_6t-xKZLSl3-7Htk2TWrCWn-X-XL9Mdbfb-NV7aswat0lYu_90T9alxDVbMj2jGM9jtt9vGZL_y0DFtBDbFmJ7HoaQ4cuYBadILE8dUdLmYOuDPFHlqg-PV1OqIFgSlYuudGT4ham3QGwmKmSNcTRJw2Md-A2d3xf9d1el-2y50C8-Ya2vCx19dlJqtBssofUYY_94ZLtMKPVA-66AEdeoTpmzq34xNqCovYdZ-01p-9OCEiXf0Bgai9CZ9hr-Rfv-y-42EKFWLYm48lsbrlAp7Ez0ah9SnYaQ19MEExUXr1HhL0WjoJ2JRR6Z-GwWFVkGRStQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">السيد مقتدى الصدر: استنكر استهداف الأراضي العراقية وأدعو الحكومة العراقية لضبط الأمن وفرض السيادة والعمل الجاد</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/naya_foriraq/86126" target="_blank">📅 12:04 · 07 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
