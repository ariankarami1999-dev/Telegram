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
<img src="https://cdn4.telesco.pe/file/neMkp4YDm-U23zIJe-Tbtsa75mqsOMphTGny4Uf9MtoekQeIRBrSjewvCPhMDotLbNti7u3rt4sGcZTB3gnBcKYW-SGhbg8bSauArVBIdx7SrmdfR513ydZGOrCWNrbQ9GOph69Mj85P9ggxIFHw3NsJepbnCD50R9ylzQRbAtgRZjNOY0cuLhB8Ot009QHLohLu9RcniwUwrEXE_JKWj1SivOZ3aC1oaaMTq4a2rId0DLYZyzTq0mFOuJzO61oC9YiQnyg5NuL818ivWpKH44XL5_5W1Xdxgrzz5xN1ysAluHipHcs50VU-OzKkSuVStD3rhFqtNUysXAJ9amjVoQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 263K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-24 00:04:59</div>
<hr>

<div class="tg-post" id="msg-83055">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🇺🇸
‏جيش الاحتلال الأميركي: أكثر من 20 سفينة حربية ومئات المقاتلات تعمل في الشرق الأوسط</div>
<div class="tg-footer">👁️ 7.25K · <a href="https://t.me/naya_foriraq/83055" target="_blank">📅 23:36 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83054">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">عودة ما يسمى الحصار الأمريكي لإيران</div>
<div class="tg-footer">👁️ 9.22K · <a href="https://t.me/naya_foriraq/83054" target="_blank">📅 23:31 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83053">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🔻
بنداء يا زهراء...
مشاهد من الاطلاقات الاخيرة للحرس الثوري تجاه قواعد الاحتلال الاميركي في البحرين والكويت.</div>
<div class="tg-footer">👁️ 9.95K · <a href="https://t.me/naya_foriraq/83053" target="_blank">📅 23:30 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83052">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">الدفاعات الجوية تستبسل بالتصدي للعدوان الاميركي في الاهواز</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/naya_foriraq/83052" target="_blank">📅 23:20 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83051">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">عدوان أمريكي على سيريك في هذه الأثناء</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/naya_foriraq/83051" target="_blank">📅 23:17 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83050">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">انفجارات في بهبهان بمحافظة خوزستان</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/naya_foriraq/83050" target="_blank">📅 23:12 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83048">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/328f9e1449.mp4?token=QUfP8NdcfGRyPCfTM62X8mBOrrepO0LigyC9s4Xr0Acl1aYB9B1kppuaNXrE8fYutydbpKHz7E2lqIP9hC9lWMhwOYycXtI_Kvw3WSvCEVMD4evecp0ro4H6mY3R81M64HyWMRcgrS1685keyB4qesmQQjfJdveFIp7CqkNGeeWPkfEOWBdu6cVUpyBdaSzEEI_k05UlQMFKkwyxDVbk1rW4ruaQt2dxgg7dIZ83TmKo5VAv8ujN3uTwQHGiMF7Gy5RpLAgWKBBKaDLCV5E920weY0zZLUijlsxBcaFmAI9ZZu0J4QgVXZyVBMAIMIkcMT3rAu0w3_nBSjnOkU_mnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/328f9e1449.mp4?token=QUfP8NdcfGRyPCfTM62X8mBOrrepO0LigyC9s4Xr0Acl1aYB9B1kppuaNXrE8fYutydbpKHz7E2lqIP9hC9lWMhwOYycXtI_Kvw3WSvCEVMD4evecp0ro4H6mY3R81M64HyWMRcgrS1685keyB4qesmQQjfJdveFIp7CqkNGeeWPkfEOWBdu6cVUpyBdaSzEEI_k05UlQMFKkwyxDVbk1rW4ruaQt2dxgg7dIZ83TmKo5VAv8ujN3uTwQHGiMF7Gy5RpLAgWKBBKaDLCV5E920weY0zZLUijlsxBcaFmAI9ZZu0J4QgVXZyVBMAIMIkcMT3rAu0w3_nBSjnOkU_mnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صواريخ إضافية تنطلق من الكويت نحو الأراضي الإيرانية.</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/naya_foriraq/83048" target="_blank">📅 23:07 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83047">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🇮🇷
صور تظهر إطلاق طائرات مسيرة وصواريخ "خيبرشكن" و "ذوالفقار" في الموجة الثالثة من عملية "نصر 2".</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/naya_foriraq/83047" target="_blank">📅 23:04 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83046">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d1bef5385a.mp4?token=ndfijsC3fIAp9vRwtHI77f5x5E7MBl_5xdzYSX8heAgGkbOTGwtt2eMNnFFriPKK-oIh-v704lkX8OS9t9w9o1-xElrICdhBN-vcBfFy97qhqNEkboWwEHSrqDXRrifV1jwxrFjiiJDIEU89vN5KYhER7wBpFDJ4C8qmK-YdHwE0aS9mOqDeFJG1mRrj3R8Z6ZEV6LDMJA-dmzHtWd9iCSrPjwVQFpyomrEbmLCb2dIHe8dBOGHBtyLsqECoGF5R9hjtmDXnOxn3Q-XfcbXhHoQl1YTupovYz5kuUCtfuXaKD7tWpaEsPOXA3cdzANGDy9dtgtEr76wlcxcpE9wIPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d1bef5385a.mp4?token=ndfijsC3fIAp9vRwtHI77f5x5E7MBl_5xdzYSX8heAgGkbOTGwtt2eMNnFFriPKK-oIh-v704lkX8OS9t9w9o1-xElrICdhBN-vcBfFy97qhqNEkboWwEHSrqDXRrifV1jwxrFjiiJDIEU89vN5KYhER7wBpFDJ4C8qmK-YdHwE0aS9mOqDeFJG1mRrj3R8Z6ZEV6LDMJA-dmzHtWd9iCSrPjwVQFpyomrEbmLCb2dIHe8dBOGHBtyLsqECoGF5R9hjtmDXnOxn3Q-XfcbXhHoQl1YTupovYz5kuUCtfuXaKD7tWpaEsPOXA3cdzANGDy9dtgtEr76wlcxcpE9wIPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توثيق يظهر إطلاق صواريخ من الكويت نحو الجمهورية الإسلامية الإيرانية.</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/naya_foriraq/83046" target="_blank">📅 23:01 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83045">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HoU6QGsKrextx5uYRWyie3BwtVC0ZjpnJ6l-uDacOeFiN6ZPb0uqAsUxuUUbAH63JbxlWdInNOGXSJvRYZBA978xAweJ2dbVn8DUT9YhJZNWz4pv52wqgw0AML-_Ay9A_ZQbnlQi7xJzxVlTYPIh5A7uGNJSVuTin1OXR4bI8b-DdRB5HGVNe6f94_c7_8-RwHv-x7qF4TH__U4U1K1XyFIpnq4XoyUl-iXTXkJ9kDa5iWsqoKwl46VRyhHMb_K-9DzJgl6Q88uuQRkisjPYS2v9ivDtJljAJRXF1j1eSPTcGtZPLDyMXoXtzAHne_TScH_821sOX1hYJ1X1GDOtSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مطالبات شعبية من ساحات العاصمة طهران بالانتقام من فريق ترامب</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/naya_foriraq/83045" target="_blank">📅 23:00 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83044">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">الجيش الأمريكي:
‏
في تمام الساعة الثالثة مساءً بتوقيت شرق الولايات المتحدة اليوم، بدأت قوات القيادة المركزية الأمريكية جولة إضافية من الضربات الجوية ضد إيران، بهدف مواصلة تقويض قدراتها المستخدمة في مهاجمة السفن التجارية في مضيق هرمز. وتأتي هذه الضربات في الوقت الذي تستعد فيه القوات الأمريكية لاستئناف الحصار البحري المفروض على الموانئ والمناطق الساحلية الإيرانية، والذي يبدأ سريانه في تمام الساعة الرابعة مساءً بتوقيت شرق الولايات المتحدة.</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/naya_foriraq/83044" target="_blank">📅 22:59 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83043">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EhLGEUs1xp8Y9UtUPGsvANOR45gbgsXnIMF97xJocn30jg8bC06X3INKua2JGvpAuTFEWZpLnuxHg8oqsA_h-Z_9CjeXydFCqyd8Iptjdhratz8UNKMF5u7tOIRDlXKl02lEDTpHZXp_nccZRBn0ilRNqEfej7ohhMaEi1bj2O3eluzfZGFiUVC_Y6mJ-YsZWwfG8-aBJFR9Tx7M_0FACciSn1dNh0zWKXAAxFgA3TP0Q-anwMUXgOmzuUVaaguz7xaEbWnNDZr2r57IhpUljvyXbtMiX-rBAZ7oDJkQEFwRIw8IdI3K8NniUBB9la8Y4ku8Le76jknuIx9N6B3kfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انفجارات في مدينة الأهواز جنوبي إيران</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/naya_foriraq/83043" target="_blank">📅 22:58 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83042">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/15b3fd282d.mp4?token=ZGWfwP8dG3Xmn7-i8wY6o2VtcdsZTAcjrkVzbx-G2_xYvSCas4xQv6eYZZKCLDn8yD0Wr7_7Y-IXd24mBZXspJYHRmOnci9zU40k2gr8jeOnxpaIRoK6xgBBxwZlG_YRMyT8IND_axxZgvm0hrtXQpCZ3nxbucpvE9PUlvvIFFprKRqzHiCtTSGeoOYYkN018z0vR3FF9oWRo-CY7pG9BM2_UzVIlHH6QHEvj0uAYBUAxSHCL-N7aOCL-MBhxkgbOWYFhFH8R5TwCo-DSEJtLUIu6m9Yx08A44H5D6I3yZd_MHt2lzdpUu_SAqc4hOhTtmcpG06vwTSx0mwthzNF_CnL4pWIdECJFe4mfet1pMlv9xyYwo0C6eN7cs82ZNXoHrL_gtEChVWqFPmWMutXGvV4GmtydPWKRXiNXphy_vVPLFllGOPfU_EnR01I-wdzdKauutRyE5SeUTxDD-3-wmLtYn1SzpZjunGw31wiSVml2lKCVzFQdchx-PoD7nS1goufDTKxK31yUV95LRZySkINpEook7bMLdr6osP9jFkZNk6wMd9Ji0IjBcuM9VuW0acNi3UoIjE1YbENvCi0w-mI0_FFms4-TB3iDTbswGCdDlBBG9zS3S3_pXB3Y3j3BFZFa5438V72Jxp6QSbF_-uzmUw-bGXdHP3-N7z7DpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/15b3fd282d.mp4?token=ZGWfwP8dG3Xmn7-i8wY6o2VtcdsZTAcjrkVzbx-G2_xYvSCas4xQv6eYZZKCLDn8yD0Wr7_7Y-IXd24mBZXspJYHRmOnci9zU40k2gr8jeOnxpaIRoK6xgBBxwZlG_YRMyT8IND_axxZgvm0hrtXQpCZ3nxbucpvE9PUlvvIFFprKRqzHiCtTSGeoOYYkN018z0vR3FF9oWRo-CY7pG9BM2_UzVIlHH6QHEvj0uAYBUAxSHCL-N7aOCL-MBhxkgbOWYFhFH8R5TwCo-DSEJtLUIu6m9Yx08A44H5D6I3yZd_MHt2lzdpUu_SAqc4hOhTtmcpG06vwTSx0mwthzNF_CnL4pWIdECJFe4mfet1pMlv9xyYwo0C6eN7cs82ZNXoHrL_gtEChVWqFPmWMutXGvV4GmtydPWKRXiNXphy_vVPLFllGOPfU_EnR01I-wdzdKauutRyE5SeUTxDD-3-wmLtYn1SzpZjunGw31wiSVml2lKCVzFQdchx-PoD7nS1goufDTKxK31yUV95LRZySkINpEook7bMLdr6osP9jFkZNk6wMd9Ji0IjBcuM9VuW0acNi3UoIjE1YbENvCi0w-mI0_FFms4-TB3iDTbswGCdDlBBG9zS3S3_pXB3Y3j3BFZFa5438V72Jxp6QSbF_-uzmUw-bGXdHP3-N7z7DpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مباشر..
ساحة انقلاب وسط العاصمة الإيرانية طهران الشعب الإيراني يطالب بالانتقام.</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/naya_foriraq/83042" target="_blank">📅 22:54 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83041">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">انفجارات في بندرعباس وجزيرة قشم جنوبي إيران.</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/naya_foriraq/83041" target="_blank">📅 22:47 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83039">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🔳
الجيش الكويتي:
القوات المسلحة رصدت، منذ مساء اليوم وحتى الآن، عدد (1) صاروخ باليستي، وعدد (5) صاروخ جوال، وعدد (33) طائرة مسيرة معادية، وقد تم اعتراضها والتعامل معها.
وأسفر العدوان الإيراني الآثم عن استهداف عدد من المنشآت الحيوية والمدنية، وسقوط شظايا في عدد من المواقع بالبلاد، مما أدى إلى وقوع أضرار مادية.
كما تم استهداف إحدى القطع البحرية التابعة للقوة البحرية الكويتية، وأصيب على إثر ذلك عدد (4) من منتسبي القوات المسلحة، حيث تلقوا الرعاية الطبية والعلاج اللازم، وحالتهم مستقرة.</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/naya_foriraq/83039" target="_blank">📅 22:39 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83038">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">انفجارات في مدينة الأهواز جنوبي إيران</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/naya_foriraq/83038" target="_blank">📅 22:32 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83037">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🇺🇸
مسؤول أمريكي:
القوات الأمريكية نفذت ضربات إضافية على أهداف عسكرية بإيران في وقت سابق اليوم
الضربات الأمريكية على إيران نفذت للقضاء على التهديدات الناشئة</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/naya_foriraq/83037" target="_blank">📅 22:18 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83036">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4bc3a98f98.mp4?token=WsrkC9jTil9ZTJftrhKxPGUu4ZBODiHUhVz5Pmh7YIkrcbL-xIl_rFlC4lsL1rXLqu_xKZN4ysymle1M5Y0n1MkFTGF_Nu4eaP_QA4HBgZ561pFu7nTZMUiLOnkT4TgZXIsmgi9Kbez79u13Hk8qi9U-f-dRKZHzLg9I_2abCS6ycJJGLqSWUWiv3zuWjKh5XyPBDwloMOgLRJ_b65XdYuH6hibwRYhW5AwRDLy3tdBwydqYXd3jAE1DeZX2Qy8yE1juQ1TPZFOOTYvJwQQ1oW8FEnmP-de3R9SQl9I5bv4XdBjhsNnRJfDTHpT5YYw81Fa5D5kmkg_wTkBTmKZZHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4bc3a98f98.mp4?token=WsrkC9jTil9ZTJftrhKxPGUu4ZBODiHUhVz5Pmh7YIkrcbL-xIl_rFlC4lsL1rXLqu_xKZN4ysymle1M5Y0n1MkFTGF_Nu4eaP_QA4HBgZ561pFu7nTZMUiLOnkT4TgZXIsmgi9Kbez79u13Hk8qi9U-f-dRKZHzLg9I_2abCS6ycJJGLqSWUWiv3zuWjKh5XyPBDwloMOgLRJ_b65XdYuH6hibwRYhW5AwRDLy3tdBwydqYXd3jAE1DeZX2Qy8yE1juQ1TPZFOOTYvJwQQ1oW8FEnmP-de3R9SQl9I5bv4XdBjhsNnRJfDTHpT5YYw81Fa5D5kmkg_wTkBTmKZZHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇾
معارك طاحنة بين عصابات الجولاني إثر خلافات داخلية فيما بينهم في بلدة ذيبان بمحافظة دير الزور.</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/naya_foriraq/83036" target="_blank">📅 22:17 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83035">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🇮🇷
الحرس الثوري:
أيها الشعب الإيراني الشجاع والرصين؛ قام مقاتلو القوة البحرية والفضاء التابعة لحرس الثورة الإسلامية، في الموجة الثالثة من عملية "النصر 2"، تحت شعار "يا زين العابدين" (علي السلام)، وتكريماً للشعب، بتدمير عدة مستودعات لتخزين الأسلحة وقطع السفن والطائرات المعادية في قاعدة الشيخ عيسى في البحرين، وذلك في عملية متزامنة باستخدام الصواريخ والطائرات بدون طيار قبل ساعات. كما هاجموا منصة إطلاق طائرات MQ9 بدون طيار التابعة للعدو في قاعدة علي السالم في الكويت، مما أدى إلى تدمير عدد من الطائرات أو إلحاق أضرار بها.
سيستمر الرد بالمثل ومعاقبة المعتدين طالما استمرت جرائم أمريكا، وإذا تكررت هذه الاعتداءات، فستواجه ردودًا مفاجئة.
طالما استمرت أعمال الشر التي تقوم بها أمريكا في المنطقة، فلن يتم تصدير قطرة واحدة من النفط والغاز من المنطقة، ولن تؤدي هذه التجاوزات إلا إلى تأخير إعادة فتح مضيق هرمز.</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/naya_foriraq/83035" target="_blank">📅 22:15 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83034">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">انفجار ضخم في مدينة صحنايا بريف دمشق</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/naya_foriraq/83034" target="_blank">📅 22:06 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83033">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">دوي انفجارات في دمشق</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/naya_foriraq/83033" target="_blank">📅 22:05 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83032">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">دوي انفجارات في دمشق</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/naya_foriraq/83032" target="_blank">📅 22:04 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83031">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">⭐️
المتحدث باسم المنظمة البحرية الدولية:
نشعر بقلق بالغ إزاء الهجمات الأخيرة على السفن في مضيق هرمز وحوله.</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/naya_foriraq/83031" target="_blank">📅 22:04 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83030">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">هزة أرضية قوية تضرب سوريا وتركيا</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/naya_foriraq/83030" target="_blank">📅 22:03 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83028">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🔳
‏
الكويت
:
الاعتداء على قنصليتنا يقوض جهود حكومة العراق للوفاء بالتزاماتها الدولية.
‏على حكومة العراق اتخاذ إجراءات فورية لمحاسبة المتورطين بالاعتداء على قنصليتنا.
استمرار عدوان إيران ووكلائها في العراق انتهاك صارخ لسيادة الكويت.</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/naya_foriraq/83028" target="_blank">📅 21:58 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83027">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">سماع دوي انفجارات جديدة في البحرين</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/naya_foriraq/83027" target="_blank">📅 21:47 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83026">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/20a1709eea.mp4?token=u-lLfnD1LX9ALCpr-WsjTdgfeeMlSxdUPL5m7FxnmL2heQoCLZAtP7WMkTJqE5f1uN_2apNoAMpjBUTSHNyuDN6g0JghZU0GQlkqTV3Z7O8cxfo5m5dpkiFLlTFVktQhSCd9LejNz5bRetWRIXrxuQ6JI-PNqsQIQUt1hJraO2ZaJEi1hCieqWnuJk0WDum1K7euDiqdYDY41qvPEPPYuzjkGll4jGgW6wnTnrwV70b4xq4yH9LeG5lmpaSmEhvJSwWD0AycjOoF-_GFqOQjRVb63DNcOyL1ZmACbpP0zkn4KLt_udh4OsRy64SXfsMHYZ5KdtZ_Zbg4O7VcfH9iwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/20a1709eea.mp4?token=u-lLfnD1LX9ALCpr-WsjTdgfeeMlSxdUPL5m7FxnmL2heQoCLZAtP7WMkTJqE5f1uN_2apNoAMpjBUTSHNyuDN6g0JghZU0GQlkqTV3Z7O8cxfo5m5dpkiFLlTFVktQhSCd9LejNz5bRetWRIXrxuQ6JI-PNqsQIQUt1hJraO2ZaJEi1hCieqWnuJk0WDum1K7euDiqdYDY41qvPEPPYuzjkGll4jGgW6wnTnrwV70b4xq4yH9LeG5lmpaSmEhvJSwWD0AycjOoF-_GFqOQjRVb63DNcOyL1ZmACbpP0zkn4KLt_udh4OsRy64SXfsMHYZ5KdtZ_Zbg4O7VcfH9iwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">السلطات البحرينية تفرض طوق امني كبير لمنع اي توثيق يخرج لمنصات التواصل الاجتماعي يفضح الخرق في تصدي للهجمات الايرانية</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/naya_foriraq/83026" target="_blank">📅 21:33 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83025">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">الله أكبر
إصابة مباشرة الان في البحرين</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/naya_foriraq/83025" target="_blank">📅 21:32 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83024">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">مسؤول أمريكي: الوضع الحالي مع إيران مماثل للوضع الذي كان بين حزب الله وإسرائيل.</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/naya_foriraq/83024" target="_blank">📅 21:30 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83023">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">سيارات الإطفاء تنتشر في منطقة الجفير حيث يقع مقر دعم البحرية في البحرين</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/naya_foriraq/83023" target="_blank">📅 21:30 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83022">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ujR3WT_tzMidtYAxlFB9LZW1uBsG0L7XMWaXBXUKoL1eeT-xMhlkRpC_4KEFslo2M0KvrxkSxYpvGFFYhC0bJCpQ81H5ykO1SsgkvGxScL34VBcZGZav-dGn1LaUhbc42nacYdQ2rStLsY2EBArIhMsyI6D5kzgjrUyrJrT9sJsMmoGPYwH0PTQg5jspaw8AQj152-_xo9NwsShvySZkWoXPkucuke2t0s-bWnuZn8V9sjEeEZrk0oyDS8fFHvdRZWr2nlew0cLzDGuhXaRJDFTQ7nDmbFz45YACZsUb-v7E9S3HQzdCwutsxsqr-b5lb6eaHHeDdzlbjH0E_xtLKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خروج مطار المنامة عن العمل وتوقف عمليات الهبوط</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/naya_foriraq/83022" target="_blank">📅 21:27 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83021">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🌟
🌟
بعد فشل منظومة الباتريوت.. طائرات حربية أمريكية تقوم بدوريات ومحاولات تصدي فوق الاجواء البحرينية</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/naya_foriraq/83021" target="_blank">📅 21:27 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83020">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🌟
🌟
بعد فشل منظومة الباتريوت.. طائرات حربية أمريكية تقوم بدوريات ومحاولات تصدي فوق الاجواء البحرينية</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/naya_foriraq/83020" target="_blank">📅 21:27 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83019">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">مسؤول أمريكي: القوات الأمريكية تشن حاليا غارات جوية في إيران.</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/naya_foriraq/83019" target="_blank">📅 21:24 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83018">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">صافرات الانذار مستمرة في دويها بالقاعدتيين ارباك كبير في دفاعات الجوية الاميركية</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/naya_foriraq/83018" target="_blank">📅 21:18 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83017">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">قواعد الاحتلال الاميركي الشيخ عيسى والاسطول الخامس في البحرين تتعرض لهجمات شرسة بصواريخ نوعية</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/naya_foriraq/83017" target="_blank">📅 21:13 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83016">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">انفجارات تهز البحرين من جديد</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/naya_foriraq/83016" target="_blank">📅 21:12 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83015">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">صواريخ انشطارية إيرانية استهدفت البحرين</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/naya_foriraq/83015" target="_blank">📅 20:58 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83014">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ehkyvmACseNy3XZscZUYtflXm6c4TQd3td_u2IZiC8aIb0uYbmTobHY_p-j7NwDY6IRDHYEAF3lFOKRN578puDNj_ONyQZzCTjON9VwtiL9AeK-SmDnlpN9DPe6-KqvlvQLnHCNmaDGH2K9OUu7PpKyT8f6lNPtwkma802nO4qdYPxqUWJSVE6NqXD_85XnSump_Rd-RIwQsrpGxbRcqu7cjSVXX3bMrSdfbyXnsis6mRmUyUSgVf4F1-5TroOS_g8SotA2r5wKOMW9_43jN3k76UjD_SmjiO3Gbe49TfHjAxb2yEIBVKTgTFqM7EpW_7ZjOMd7mf-bYnK291jtvBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الصواريخ الإيرانية في سماء البحرين قبل دكها للمصالح الأمريكية</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/naya_foriraq/83014" target="_blank">📅 20:57 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83013">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">الكويت تتعرض لهجوم صاروخي جديد</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/naya_foriraq/83013" target="_blank">📅 20:55 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83012">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d618e17934.mp4?token=J-IHHflBgO7eEiFKPFCAsqc73aoC2KKRrNu-7HTE3hROZ3NerLAZQ8V8AD5dWeCIssjFUPfZkkLCuu87r1UFUdLuWP1VUDm35DVVrJ4ePaVc6Z0nS5imTteMuPbAbVpJiLLucUFEXp1AwI_YqH3Emi6GcILYdjYF4eG__odVqB7mhNMNGBk9BYtxcLVCthCUWt_66VuJ3xXSGb9p4ew2qttSAMsrUgXn_f5cif001ZFfuH6E2-108Hy6_t9ZrSjOiN-v8A3BOaDSiLXwRzYChf2M-EG1vmjN0pVWAiPb_pKiTzopFRJFCRQkBHV6KyJt2MtzdMBX-no4IP5-3VM-eQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d618e17934.mp4?token=J-IHHflBgO7eEiFKPFCAsqc73aoC2KKRrNu-7HTE3hROZ3NerLAZQ8V8AD5dWeCIssjFUPfZkkLCuu87r1UFUdLuWP1VUDm35DVVrJ4ePaVc6Z0nS5imTteMuPbAbVpJiLLucUFEXp1AwI_YqH3Emi6GcILYdjYF4eG__odVqB7mhNMNGBk9BYtxcLVCthCUWt_66VuJ3xXSGb9p4ew2qttSAMsrUgXn_f5cif001ZFfuH6E2-108Hy6_t9ZrSjOiN-v8A3BOaDSiLXwRzYChf2M-EG1vmjN0pVWAiPb_pKiTzopFRJFCRQkBHV6KyJt2MtzdMBX-no4IP5-3VM-eQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجارات تهز البحرين</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/naya_foriraq/83012" target="_blank">📅 20:54 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83011">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🇮🇶
النزاهة العراقية تطيح بمدير الأشغال العسكرية إثر مخالفات ومغالاة بعقد تأهيل مستشفى القوة الجوية - الرستميَّة بقيمة (92) مليار دينار. حيث تم القاء القبض على عميد وعقيدة و 5 موظفين</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/naya_foriraq/83011" target="_blank">📅 20:51 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83010">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">إعلام خليجي عن ‏مصادر أميركية: واشنطن تراقب احتمال تدخل حزب الله في أي تصعيد إيراني</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/naya_foriraq/83010" target="_blank">📅 20:47 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83009">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">انفجارات تهز البحرين</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/naya_foriraq/83009" target="_blank">📅 20:42 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83008">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/naya_foriraq/83008" target="_blank">📅 20:42 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83007">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🔻
مصدر خاص لنايا ينفي وقوع انفجارات في تبريز أو شيراز.</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/naya_foriraq/83007" target="_blank">📅 20:22 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83006">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">انفجارات تهز الكويت مجدداً</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/naya_foriraq/83006" target="_blank">📅 20:15 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83005">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">انفجارات تهز الكويت مجدداً</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/naya_foriraq/83005" target="_blank">📅 20:14 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83004">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">‏‌ترامب بشأن مشروع قانون العقوبات على روسيا: "هذا تكريماً لليندسي. كان هذا مشروعه... وهناك احتمال كبير أن يتم إقراره، لكنهم يرغبون في إضافة إيران وحزب الله إليه."</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/naya_foriraq/83004" target="_blank">📅 20:04 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83003">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">‏ترامب عن الشهيد أبو مهدي المهندس: سليماني - لقد قتلته... وصادف أن قُتل شخصٌ سيءٌ للغاية من العراق في نفس الحادثة. لذا لا أعرف إن كنت قد أسديت لك معروفاً أم لا. لم أسألك هذا السؤال قط.</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/naya_foriraq/83003" target="_blank">📅 19:54 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83002">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">ترامب: يمثل النفط العراقي أولوية لنا، وسنُشرك شركاتنا بشكل أوسع في العمليات النفطية داخل العراق</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/naya_foriraq/83002" target="_blank">📅 19:51 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83001">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">‏ترمب: شركات نفط أميركية كبرى ستدخل إلى العراق  ‏سيبرم الكثير من الصفقات مع العراق وسيسحب كميات كبيرة من النفط.</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/naya_foriraq/83001" target="_blank">📅 19:50 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83000">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">‏ترامب: لا أؤيد فكرة فرض رسوم، ولكن في الوقت نفسه، ليس من العدل أن نحمي هذا المضيق للعالم أجمع، ثم لا نحصل على أي تعويض، ونحن نفعل ذلك منذ سنوات عديدة. لقد أزعجني هذا الأمر منذ 25 عامًا...</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/naya_foriraq/83000" target="_blank">📅 19:47 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82999">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">ترامب عن رئيس الوزراء العراقي: ‏"لقد كان مقاتلاً عظيماً وكان من أشد المعجبين بأمريكا... لديهم احتياطيات نفطية هائلة... لديهم ثروة هائلة."  ‏"لديهم قائد عظيم، رئيس الوزراء الجديد. إنه قائد عظيم. أعتقد أنه سيبقى في منصبه لفترة طويلة... إنه شاب ووسيم، وهذا لا…</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/naya_foriraq/82999" target="_blank">📅 19:43 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82998">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">أنباء عن تفعيل الدفاعات الجوية الإيرانية في محافظة خوزستان</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/naya_foriraq/82998" target="_blank">📅 19:42 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82997">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">‏ترمب: شركات نفط أميركية كبرى ستدخل إلى العراق  ‏سيبرم الكثير من الصفقات مع العراق وسيسحب كميات كبيرة من النفط.</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/naya_foriraq/82997" target="_blank">📅 19:39 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82996">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">‏ترمب: شركات نفط أميركية كبرى ستدخل إلى العراق  ‏سيبرم الكثير من الصفقات مع العراق وسيسحب كميات كبيرة من النفط.</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/naya_foriraq/82996" target="_blank">📅 19:37 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82995">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">‏ترامب: لا نعتقد أننا بحاجة إلى وجود جيشنا هناك الآن</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/naya_foriraq/82995" target="_blank">📅 19:37 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82994">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">‏ترامب: نحن موجودون من أجل العراق إذا احتاجوا إلى الحماية</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/naya_foriraq/82994" target="_blank">📅 19:35 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82993">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">ترامب: نحن نحب العراق</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/naya_foriraq/82993" target="_blank">📅 19:35 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82992">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🇾🇪
القوات المسلحة اليمنية: إسقاط طائرة استطلاع نوع "وينق لونق 2" (Wing Loong II) تابعة للعدو السعودي وذلك أثناء قيامها بمهام عدائية فجر اليوم في أجواء محافظة البيضاء وسط البلاد.</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/naya_foriraq/82992" target="_blank">📅 19:34 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82990">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/C7YYWnoPLGFnCOQ5gKvpp7iJduXxlkHv7qVaZJtAVnWkYbIYZfqXhFBQusQFFHiDok8ceHgbx6K6-_D5iXna1Y4m2zTMbDRdgJy3md6TE3vTzCDsPvVZptF9NHt0_l9orWWX_jiL2noT_4fsBSHyJ8hyQ4M5bNzJzuaVBqJTtJ487XCSDVryJCJW74xFTEqGeigfmhmVrz16EqvNffx00gpenyry-vDiZPciKWZoElH3vvH3Dd8RO_CtboHilCGrqz2GtEg3QsE26zHbXg2hG4dFnY3XrSH4UEG-qdnjjz1vfZ5lrsE_BYbSFULciQvKxHwCU0bQMCUnsrf2Sk_Ywg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/s57qNaUiUEAQLtAwDihspomtI9Nfpz-i7oHmqqA8HZqPpYlUWwA93SoYrmSQzHrjGwPizGqjncTX9Qs9NHazLjTkXcJD0fmeJgbZojlh2n6uqu0g8foWblLOSQIfi-4Ga86wO_qzGa7RiSxspfGn4iY5RIr0IRwgepxmL3D8MdDsPPw6GfSr9l-czQ0NwUpHbqwRm_Puy0MP2l0HpItMA0gDAS-rQejuP3nKFxJOP1rOltSMnK1sMBy4wjp8ekAxEZiNQAA_CDpElx85CKKVHguYK6M3bsZPhy7OWHvDqmJSYdjRRYHRUuY64WrdJz4Ia0rlTVP8y-0_lOn0Y13KDQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔻
مشاهد من سماء الكويت بعد الهجوم الصاروخي الذي تعرضت له قبل قليل</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/naya_foriraq/82990" target="_blank">📅 19:33 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82989">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/939d8150e4.mp4?token=W_imUD3INL7NEFx38es_nkW6rdlO-gCYjcYtOOzXkuJvPgFUGBA60tEj-Bkv9uckW3tcURa53OrYzYhjrVqcVc1U5cQastrtm0WGqj9f5T1w70vpXxmmzBOqhzUkHRmuvbzhTqwpRDfLpnuda03h-gfGbrxT_wu8nYxrm2sHP5mrSJki3kTGuX9V-E6f9KYrha4lPJJLWDMi6onXsjrIYgtvLuCqPMfv3vyUUu7bb6Ew1aMpalCT2bRcBUQJ04l6-NjbxRj7Gdn9AomqO67REHY4WZZsZ1VN3CxVqcigS4EgOtip5q0EMoFo29GeVORmttoXNfYM7R_2kbgsdoZmjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/939d8150e4.mp4?token=W_imUD3INL7NEFx38es_nkW6rdlO-gCYjcYtOOzXkuJvPgFUGBA60tEj-Bkv9uckW3tcURa53OrYzYhjrVqcVc1U5cQastrtm0WGqj9f5T1w70vpXxmmzBOqhzUkHRmuvbzhTqwpRDfLpnuda03h-gfGbrxT_wu8nYxrm2sHP5mrSJki3kTGuX9V-E6f9KYrha4lPJJLWDMi6onXsjrIYgtvLuCqPMfv3vyUUu7bb6Ew1aMpalCT2bRcBUQJ04l6-NjbxRj7Gdn9AomqO67REHY4WZZsZ1VN3CxVqcigS4EgOtip5q0EMoFo29GeVORmttoXNfYM7R_2kbgsdoZmjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجارات تهز الكويت من جديد</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/naya_foriraq/82989" target="_blank">📅 19:31 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82988">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VNf2lve20IT3k6Ug2vD75CuHuCJUtSugH4Brbq0c8mHVDI5RjMje2m7WDoRoZfnllpzcgO7D31h9G7KMxos9ZYhoflifLe2eEG2IWu0kXVcdhve8ObLpOvuQLJgpC9GaKdMEHaqytQz_IChbUUS-ewmFSBbYc8n2ZjGvm3iDgNZlg3X_1Xl0P3xtvKdvmOuLjpya1c7sKNFh-pgbKk-zHRiygpm3VXlKkOXIu67nVEIzZXuOz6MA3tb7Z9XVwMPovNgmKqJrCZ3kE0AXCjxo9EWCKi4i_L1GqgLaWiPIaZWTdlaFkHYjqZSFOrA1aM2b3JQ6sl8q2e947blwflW9bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
أبو مجاهد العساف لأنصار الله في اليمن: نعلن تأييدنا المطلق لخطواتهم المباركة وتصرفات ممالك الخليج وعصابات الجولاني لن تمر مرور الكرام وسيبقى الحساب مفتوحا
▫️
مشاركة قوى المقاومة ستكون فورية وحازمة إذا اندلعت حرب ضد الجمهورية الإسلامية</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/naya_foriraq/82988" target="_blank">📅 19:26 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82987">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qXJKR2ATexx1L_tjlo3s4OxfaH1x7f-LqOOeVhE58x5R_tegDBZBxDRUcwmdUhWuHB4HA21tyeJbkOoYRHK7fhjWwueeiUaOVupTNPzl4fgkSlrLMGQn96gbHSEXqTR0MkfyxAh7XX8XD_deZKy8BUm0608t0d_gNHNeDoflEfP5GHqKyQe4DI4yrvO0COaBW3ymAnixhIkIOkt9SNTUqdsHsWOOkkswEPoSZFidQ2sJUG-0sc6P6q8HRqJKRXM_tt2Nr7LOPJaT_NJyVadsuWRqeLmMIQOysAxc4hd25ycJ0c2OnRcTg3B8kTv3YVuXbiMLSnAUIlNJQyZIiDdZgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
ترامب ينشر صورة تظهر بها خريطة أمريكا الجديدة حيث تضم كندا وغرينلاند.</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/naya_foriraq/82987" target="_blank">📅 19:25 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82986">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">الفرار الفرار حيدر آمد شكار _ شور مزلزل _ الفرار الفرار جاء حيدر…</div>
  <div class="tg-doc-extra"></div>
</div>
<a href="https://t.me/naya_foriraq/82986" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔻
الفرار الفرار..</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/naya_foriraq/82986" target="_blank">📅 19:22 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82985">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/naya_foriraq/82985" target="_blank">📅 19:20 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82984">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/naya_foriraq/82984" target="_blank">📅 19:19 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82983">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🇮🇷
🇺🇸
شركة الهندسة المائية والكهربائية في جزيرة كيش: الاحتلال الامريكي استهدف إنتاج المياه والكهرباء في جزيرة كيش.</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/naya_foriraq/82983" target="_blank">📅 19:11 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82982">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🇮🇷
أنباء عن سماع انفجارات في جزيرة قشم جنوب إيران</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/naya_foriraq/82982" target="_blank">📅 19:05 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82981">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">انفجارات تهز الكويت</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/naya_foriraq/82981" target="_blank">📅 18:58 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82980">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">انفجارات تهز الكويت</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/naya_foriraq/82980" target="_blank">📅 18:56 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82979">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">انفجارات تهز الكويت</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/naya_foriraq/82979" target="_blank">📅 18:55 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82978">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/naya_foriraq/82978" target="_blank">📅 18:55 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82977">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">مشاهد من لقاء رئيس مجلس الوزراء العراقي علي الزيدي  بترامب</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/naya_foriraq/82977" target="_blank">📅 18:50 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82976">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1de22772ff.mp4?token=QamZzz_KR1oM2QJ9Si8vF8zmgyrzsW0HwV2gdqXwa6RmahiZmfAFQ5guzGog6hMbnkRiIvGm1UeY5VDtZCWoV_jln8C9iSqYV1uPMx-MdnKSAdjuBfW72foU3Ptc2QvfV6TJ4PiRYcYegmfivh9WVfmK0lc_l6BEyVwfijgfFY25M-O6hWDGpqIsGZnzcmVkw2QlSX6r2ZFMujC3VOmYlbfvm6os-lnrGktOubiqCrm5RkrwInEIFwZyvbTP5vcGLinLsL_Fsa6KnzA9Eu5OBguYiv9Rw2rl_y0ZoH2164SH_tBIZnq5tMkU5h6bWxfvaHdjPTi38qX8EiWafGNcuSamQj4itgTFyZNHdjbAGPbeXe_1ReA-rYlZReXBzA8CVr47g7k7zHyRGladRkTkvhOK4FArT3pP20IrJrQyhuBcMD1dCTpbfIXvk972SG0yF3qthCjrUiSF-8KCUG_xpNBO4aMPlk3MxOh931nuQnhlv1DgjwuDABwOgdZKe3jrLCm_xg2RfyamjzwpORE2hHxyIbLouQ5vYbr4BhBrPWUuEdMCV2rfL8m_HPIQ-iJ40AOW6zd7fuEavZzQ4l4iboMiXTVvz9YVlgzmd-0iURpiyzwvhhj6DqiP9uxyU8DajDhIl_srmy0V9mcy_vetSmrhNq6kzYdzdXsYcLkjKHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1de22772ff.mp4?token=QamZzz_KR1oM2QJ9Si8vF8zmgyrzsW0HwV2gdqXwa6RmahiZmfAFQ5guzGog6hMbnkRiIvGm1UeY5VDtZCWoV_jln8C9iSqYV1uPMx-MdnKSAdjuBfW72foU3Ptc2QvfV6TJ4PiRYcYegmfivh9WVfmK0lc_l6BEyVwfijgfFY25M-O6hWDGpqIsGZnzcmVkw2QlSX6r2ZFMujC3VOmYlbfvm6os-lnrGktOubiqCrm5RkrwInEIFwZyvbTP5vcGLinLsL_Fsa6KnzA9Eu5OBguYiv9Rw2rl_y0ZoH2164SH_tBIZnq5tMkU5h6bWxfvaHdjPTi38qX8EiWafGNcuSamQj4itgTFyZNHdjbAGPbeXe_1ReA-rYlZReXBzA8CVr47g7k7zHyRGladRkTkvhOK4FArT3pP20IrJrQyhuBcMD1dCTpbfIXvk972SG0yF3qthCjrUiSF-8KCUG_xpNBO4aMPlk3MxOh931nuQnhlv1DgjwuDABwOgdZKe3jrLCm_xg2RfyamjzwpORE2hHxyIbLouQ5vYbr4BhBrPWUuEdMCV2rfL8m_HPIQ-iJ40AOW6zd7fuEavZzQ4l4iboMiXTVvz9YVlgzmd-0iURpiyzwvhhj6DqiP9uxyU8DajDhIl_srmy0V9mcy_vetSmrhNq6kzYdzdXsYcLkjKHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رئيس الوزراء العراقي علي الزيدي يلتقي ترامب</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/naya_foriraq/82976" target="_blank">📅 18:47 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82975">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🇺🇸
ترامب:
لقد قررت استبدال الرسوم البالغة 20٪ التي تفرضها الولايات المتحدة على سفن مضيق هرمز باتفاقيات تجارية واستثمارية
سنفرض حصارا كاملا ولكن فقط على السفن القادمة من الموانئ الإيرانية والمغادرة منها</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/naya_foriraq/82975" target="_blank">📅 18:37 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82974">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🔻
حدث أمني اخر في عمان</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/naya_foriraq/82974" target="_blank">📅 18:37 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82973">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">نايا - NAYA
pinned a video</div>
<div class="tg-footer"><a href="https://t.me/naya_foriraq/82973" target="_blank">📅 18:37 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82972">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6f8332e5e9.mp4?token=MILUNOEkfkH0UJEp421PEqZJHS0AjcQybcQnnznB75hKmLmCZHlFw7LvmNtHTanKbmu8qgJsWDet9AMZBV9V8Ksw4rWKfUVDUUTnJWr2qZgiP0Em-Z8Y5vplOByvKtF_0CK_rmJJRqYI1cg9W5Uf6QpP0J6F-e95a1igzf34KHAnnqzvMP5mX8T7nuWhM3GnOHlEdRmew_dOluTp5NkmSSUdzd5FK7R48EJ_UghU7rfZ2lNopLTfzJh420xYchaJqIGysMl57aLiLmF430EGmpMHQ9zuTtLi8g7iZTS7M-8xosNOzscLYq0x_1r3FVeLNo5eURYPBZQI0qlYMWOi9xja_4tIdb2Zl93o0MS8MWWIIHtRZ7PQ6ztDOue-LYeu8_FJ85vuBsTSx16gjZaUtzRZ7KgqqPKZ1ysfjILYb0K5Y8MS1gKTEE4AhTeSver2gW-DdMkQFoMNxqOznatbbtqWVw9KEoCpCFMzZSU0y8fAl-fo1OrMeuKgGFFRt3lq35tj5PUkksSXcMl0vsBOuFKchkkUsfEzaeNpMn-89Cf8ggNVSWTpCn7NK48bnzwJ6p6G_kNDKmkNfObU7ZUqe2M4DGpcP19gjcrGZUIfFws78TLcG4_uVl9G4uS5Z7R8wA1cdZEx6ATOB1Ns7GbXk_M3wJH7rhBYUofFcDtBnsU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6f8332e5e9.mp4?token=MILUNOEkfkH0UJEp421PEqZJHS0AjcQybcQnnznB75hKmLmCZHlFw7LvmNtHTanKbmu8qgJsWDet9AMZBV9V8Ksw4rWKfUVDUUTnJWr2qZgiP0Em-Z8Y5vplOByvKtF_0CK_rmJJRqYI1cg9W5Uf6QpP0J6F-e95a1igzf34KHAnnqzvMP5mX8T7nuWhM3GnOHlEdRmew_dOluTp5NkmSSUdzd5FK7R48EJ_UghU7rfZ2lNopLTfzJh420xYchaJqIGysMl57aLiLmF430EGmpMHQ9zuTtLi8g7iZTS7M-8xosNOzscLYq0x_1r3FVeLNo5eURYPBZQI0qlYMWOi9xja_4tIdb2Zl93o0MS8MWWIIHtRZ7PQ6ztDOue-LYeu8_FJ85vuBsTSx16gjZaUtzRZ7KgqqPKZ1ysfjILYb0K5Y8MS1gKTEE4AhTeSver2gW-DdMkQFoMNxqOznatbbtqWVw9KEoCpCFMzZSU0y8fAl-fo1OrMeuKgGFFRt3lq35tj5PUkksSXcMl0vsBOuFKchkkUsfEzaeNpMn-89Cf8ggNVSWTpCn7NK48bnzwJ6p6G_kNDKmkNfObU7ZUqe2M4DGpcP19gjcrGZUIfFws78TLcG4_uVl9G4uS5Z7R8wA1cdZEx6ATOB1Ns7GbXk_M3wJH7rhBYUofFcDtBnsU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎮
جیل Z من شاشات الألعاب الی ميادين الجهاد!
المقاومة الإسلامية حركة النجباء تحذر: آلاف الشباب ومحلقات FPV على أهبة الاستعداد لتنفيذ العمليات ضد قواعد الاحتلال الأمریکي
🔥
"Coming soon: FPV drone operations in Iraq."</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/naya_foriraq/82972" target="_blank">📅 18:37 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82971">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🔻
حدث أمني بحري قبالة عمان</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/naya_foriraq/82971" target="_blank">📅 18:36 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82970">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🔻
استهداف ناقلة نفط مقرها الامارات ترفع علم ليبيريا</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/naya_foriraq/82970" target="_blank">📅 18:36 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82969">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OkMUwLecXalQ8Q0EiGzCmiKDJYjra33rYQKjZwKnUnnQIaETM2Xuoq5zHtVthzel9aud-zBoDmxrY2pjfJ7SUIJXPJkOoZY1hqL_zoJbb8jnaT7Gi5PqvKS8SMK45wpnLfPcqEqnjodzptsTaXS0D3RS0H32rWP6HTI_8PGSpr9oF0KQSj954FPbMr6ns9jKG6TM1vtJ71Rg5W7rvMNwJcXTKl2bNhuLWmOKexmOTcK3vTuh8Ja-Fz9jQoWbhW7MiHAq_MEPNZXe41yQPwXkSsl4wT5kyLN-EAWC2pdnFsHD9KuCOT1i4cFFUNjNrthC2VauaHeipbYfUZehFSWdFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
حدث أمني بحري قبالة عمان</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/naya_foriraq/82969" target="_blank">📅 18:35 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82968">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🔻
حدث أمني بحري قبالة عمان</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/naya_foriraq/82968" target="_blank">📅 18:34 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82967">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">رئيس الوزراء العراقي علي الزيدي يلتقي ترامب</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/naya_foriraq/82967" target="_blank">📅 18:27 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82966">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">قوة مسلحة تابعة لعصابات الجولاني تحتجز السائقين العراقيين في مصفاة حمص والسائقين يناشدون الحكومة العراقية لانقاذهم واعادتهم الى البلاد</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/naya_foriraq/82966" target="_blank">📅 18:10 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82965">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🇺🇸
‏مندوب أميركا لدى مجلس الأمن: إيران والحوثيون يهاجمون السفن ويهددون مضيق هرمز.</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/naya_foriraq/82965" target="_blank">📅 17:43 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82964">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🇺🇸
‏
مندوب أميركا لدى مجلس الأمن:
إيران والحوثيون يهاجمون السفن ويهددون مضيق هرمز.</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/naya_foriraq/82964" target="_blank">📅 17:39 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82963">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromنايا - NAYA</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">محمد القحوم | زامل تنورة | 2023 Mohammed Al-Qahoum</div>
  <div class="tg-doc-extra">محمد القحوم | Mohammed Al-Qahoum</div>
</div>
<a href="https://t.me/naya_foriraq/82963" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">دكوا عروش الأسرة المغرورة</div>
<div class="tg-footer">👁️ 7.27K · <a href="https://t.me/naya_foriraq/82963" target="_blank">📅 17:35 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82962">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">نادي النصر السعودي يلغي معسكره التدريبي في ابها ويعود الى الرياض بعد هجوم انصار الله</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/naya_foriraq/82962" target="_blank">📅 17:30 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82961">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">مواقع متخصصة في تتبع حركة الملاحة الجوية تظهر استمرار إغلاق مطار أبها السعودي</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/naya_foriraq/82961" target="_blank">📅 17:18 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82957">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JIk087OGv21E1kbTzoeJUbCqfHhOUmjmlAvLyTPdUxG8y4jtEctOpVjsDtIAsu-LO43LnefrOYEhs3-kmD_TWrAoVWuwY54VbenXAQxrMifErcGaXkK0EG1_r_p_egv6Gojte-zTMfgOA1TIqPONqKVP5MFEI76vpvU-GeI4UFHYjWCmbljlAXh6SY8ZE7zuWGyKjyk3r2o4mGoMJZWCUi2GWiiyqTG9RuhjwajY7OUhdbIcWiWYQkYIoHyGUdz3IYeMqyhb8J6sCByMUJo6x4J5Y6oqavTuyTIdgZtzV0x9lu3ZXSBGZAh8Qi9me1Rjgtszf9Ux9s7Wxgn4aYf9xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇾🇪
الاعلام الحربي اليمني ينشر:
نحذر جميع شركات الطيران من العبور في الأجواء السعودية وعليها أخذ تحذيراتنا على محمل الجد حتى رفع الحصار عن مطار صنعاء الدولي
We warn all airlines against crossing in Saudi airspace and they should take our warnings seriously until the blockade of Sana'a International Airport is lifted</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/naya_foriraq/82957" target="_blank">📅 16:56 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82956">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e95a70b7f0.mp4?token=fDuYJIuhnc2Tdhx_nlBrwsa0gXuhX6-BjVOMiRMXbRq9l3nJDEvQTzxfjZiXMLjAjf_ZGlUhtb81SAnE4I5DTVcFokEzy9ykvQEWxPGt7j-2ParZMwrpVwX1JbURxQeVeQ_ywwKcL_E0FG0ofy6Qo1o_lTEGqskFeFK6YtEuBaYuJVYIkCcNX0seHyBw9DBrTcmzejI0bVMOiGvCyzInJM9IpLRzXMIZozCl5ja43ubYDGGttZQZrcx4XxHfxeB9DNbgu3WAzl6BnX4HVSsCHC6z_nYQKPCl54FXawruaNna7PtZxIX7IZI63rSqe-J6yg8njStlKrHNy0mSh5dPqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e95a70b7f0.mp4?token=fDuYJIuhnc2Tdhx_nlBrwsa0gXuhX6-BjVOMiRMXbRq9l3nJDEvQTzxfjZiXMLjAjf_ZGlUhtb81SAnE4I5DTVcFokEzy9ykvQEWxPGt7j-2ParZMwrpVwX1JbURxQeVeQ_ywwKcL_E0FG0ofy6Qo1o_lTEGqskFeFK6YtEuBaYuJVYIkCcNX0seHyBw9DBrTcmzejI0bVMOiGvCyzInJM9IpLRzXMIZozCl5ja43ubYDGGttZQZrcx4XxHfxeB9DNbgu3WAzl6BnX4HVSsCHC6z_nYQKPCl54FXawruaNna7PtZxIX7IZI63rSqe-J6yg8njStlKrHNy0mSh5dPqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
قوة امنية من بغداد تدخل ناحية الزوية ضمن محافظة صلاح الدين شمالي العراق وتبدأ حملة تفتيش واسعة عن (احمد اسماعيل فرحان) احد المتورطين في قضية عدنان الجميلي</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/naya_foriraq/82956" target="_blank">📅 16:46 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82955">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">سوالف الگهوة  رئيس الوزراء العراقي علي الزيدي يعتزم زيارة طهران الأسبوع المقبل تلبيةً لدعوة بزشكيان</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/naya_foriraq/82955" target="_blank">📅 16:46 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82954">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">سوالف الگهوة
رئيس الوزراء العراقي علي الزيدي يعتزم زيارة طهران الأسبوع المقبل تلبيةً لدعوة بزشكيان</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/naya_foriraq/82954" target="_blank">📅 16:36 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82953">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kaWMcqCR0RESGBnth05AfRzZ1wOr_OryBZ8bpFiyfZixpoiYKngDBpOHpJXIWqyimDi7LTQ-73vAava-4_dWKXi3cjVlx25aJ3nBSp64mhLaejTKBDaHi8OHUDgF4WGbt7PZBqE89AtmWVje6lyjwGjtjgEC1aTEyoG7w4KZCgZGzT67VxcUpXCtHlai1DgbzdxzRmn4qlswhzvne4K4kVB23-KElpe9IUynyqCzQpMBbNz34dLc2XunHsSrWp9ojPP98deGKHXhe5Y3fBnfajum2kD8IVTnarZe-hPnzBxglDdcto7wbLWzVau0bHIcOWHB3qUjq-lyC_YsYSTh0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
نحو 180 نائب ايراني يوقعون للمطالبة بإعلان انتهاء اتفاقية إسلام آباد مع الولايات المتحدة ومواصلة عمليات الانتقام لقائد الثورة الشهيد وسائر الشهداء</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/naya_foriraq/82953" target="_blank">📅 16:25 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82952">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">نتن ياهو يجري زيارة الى مفاعل ديمونا ويقول:
لقد أزلنا حاجز الخوف. لا أستطيع أن أقول ماذا سيحدث في إيران حاليا، ويمكن أن تحدث أمور كثيرة. نحن مستعدون لكل سيناريو.
أقول لقادة إيران: لا تراهنوا على أن يسود الهدوء إذا هاجمتمونا، لا تراهنوا على أن تكون هناك إعادة للرد نفسه، سيكون ردنا مختلفا، وأقوى بكثير.
انتهت الأيام التي يقصفنا فيها أحد ولا نرد عليه بضربة مضاعفة. هكذا سنفعل</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/naya_foriraq/82952" target="_blank">📅 16:20 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82951">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🇮🇷
الهيئة الإيرانية لإدارة مضيق هرمز:
قبل التصعيدات الأخيرة التي قامت بها القوات الأمريكية في المنطقة، والتي أدت إلى إغلاق مضيق هرمز، خلال فترة ثلاثة أسابيع بعد توقيع مذكرة التفاهم، قامت أكثر من 200 سفينة غير إيرانية بالتنسيق معنا، وقد حصلت معظمها على تصاريح العبور والتأمين.</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/naya_foriraq/82951" target="_blank">📅 16:12 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82949">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">اندلاع حريق داخل مطار البصرة الدولي</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/naya_foriraq/82949" target="_blank">📅 15:28 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82948">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">‏وكالة سلامة الطيران الأوروبية: يُمنع على مشغلي الطائرات العمل ضمن المجال الجوي للبحرين والكويت وقطر والإمارات العربية المتحدة، أو المجال الجوي فوق مياه خليج عُمان.</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/naya_foriraq/82948" target="_blank">📅 14:35 · 23 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
