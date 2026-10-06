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
<img src="https://cdn4.telesco.pe/file/vXP3iZspqdUIhG4iePhfWfQTA4TZKZqL0BMbi6bAwlf6gxDU7rJS5y5fcDSOBNJvktjKbvncAJcHpOSJC0MZhl6TBo6vm1YBL2CYeZzXUDrNLpym5kYFB_4Tiu1GBjKsS0PSNVq4DAktzNZXmZoVs2H69_Qqh0Hzvk-c0O_f512i7Uvo0x3Zf8q64oe5zo2jy-3w51H-ZWLyXO28_7J-KASjhdo0koc1Ezjl_L4avsnKRCkT0U-Jaf2k9TCEOkhrS9ETdEebw0ZcXRF0j1DWLVNS12d3AFJenzARhX2Jw7TZxWX71epkMTYqy53mzzumwGnvTuIs0vjcs3sBXd-XaQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 264K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-14 17:18:01</div>
<hr>

<div class="tg-post" id="msg-92721">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🇾🇪
🇾🇪
القوات المسلحة اليمنية:
استهداف التحشيدات التابعة للعدو السعودي في رأس العارة بصواريخ باليستية.</div>
<div class="tg-footer">👁️ 5.59K · <a href="https://t.me/naya_foriraq/92721" target="_blank">📅 16:04 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92720">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">الشرطة البريطانية تعلن اعتقال بريطاني عمره 22 عامًا بشبهة التحضير لعمل إرهابي متعلق بقاعدة "فيرفورد"</div>
<div class="tg-footer">👁️ 6.62K · <a href="https://t.me/naya_foriraq/92720" target="_blank">📅 15:51 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92719">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/41aff32781.mp4?token=DDJcLLd9SMP1GOFd7hksdX5U8vf9W6ZGBFn-Ayp_57kPpjeCuk3qGJ77DFcHwRI_WMTOA50dY-3tlitug0vavIhFaOFT0D33u6mgidSQNcuYFx_pcKBD22FhwaqSlNcxYK9I8EPyRWoAVr6SimvKfVNgS00x9ZfgKSpVNmLeiItlIaaeOE7p-xBWELuLjkem5HVLUngimKBNUHecwlOEOzd8PP0nzxFVeS8CRTrvvWBlFS0MXFpauOJe0QcHGba1O1HfZaTituAvvKflC_kpn6MvPWLFTmye8g91J1QpxS_qoS6QzJQ-N25M1pSCCZTW9H1w0j5tpmZbsVU3ITD2_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/41aff32781.mp4?token=DDJcLLd9SMP1GOFd7hksdX5U8vf9W6ZGBFn-Ayp_57kPpjeCuk3qGJ77DFcHwRI_WMTOA50dY-3tlitug0vavIhFaOFT0D33u6mgidSQNcuYFx_pcKBD22FhwaqSlNcxYK9I8EPyRWoAVr6SimvKfVNgS00x9ZfgKSpVNmLeiItlIaaeOE7p-xBWELuLjkem5HVLUngimKBNUHecwlOEOzd8PP0nzxFVeS8CRTrvvWBlFS0MXFpauOJe0QcHGba1O1HfZaTituAvvKflC_kpn6MvPWLFTmye8g91J1QpxS_qoS6QzJQ-N25M1pSCCZTW9H1w0j5tpmZbsVU3ITD2_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">القوات المسلحة اليمنية تتقدم في تعز وسط انهيار دفاعات العدو السعودي ومرتزقته</div>
<div class="tg-footer">👁️ 6.62K · <a href="https://t.me/naya_foriraq/92719" target="_blank">📅 15:51 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92718">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">حدث بحري في مضيق هرمز</div>
<div class="tg-footer">👁️ 6.46K · <a href="https://t.me/naya_foriraq/92718" target="_blank">📅 15:44 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92717">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gR2t99lqwX5mwLOYmSvy_k0RpvNPUfAFwRsO7kqRv6kkpCT-maLusruxTsBL8q6zdIj1GsuKpf1ajXaDlEPQrGZCkBIGhPguDwOtqvr0cHxQ_3DYHfBadWuqYCyjhVegp4SjBlHmjDE1g9Mba3QoRkJyjUvvFlptIbqFuzRQVWl0T9AX0bays_lur1V1mwr53ofviitOfHWnS04ufIvHXdR6_HxXZEiONtgQWg47o3d5FOvPD2CN70n6WmhfjMb_blLgmXypdQlRS24L5J8PPBOriqspkVKB2Ugs2xCzmkWqoSnHVOYO0QAGR3Y3ACPM89aJvDByIu3G7RbhERq0Yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حدث بحري في مضيق هرمز</div>
<div class="tg-footer">👁️ 6.43K · <a href="https://t.me/naya_foriraq/92717" target="_blank">📅 15:43 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92716">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🇾🇪
القوات المسلحة اليمنية:
سيتم عرض مشاهد استهداف التحشيدات التابعة للعدو السعودي في رأس العارة الساعة 3:30م بعد قليل.</div>
<div class="tg-footer">👁️ 6.38K · <a href="https://t.me/naya_foriraq/92716" target="_blank">📅 15:40 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92714">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oD9f5VOEX0FGDf5QVpThzzJz9j1TBeC5I1X2gY8PpeQrfNluZvOTyCKe07nuCrA6DMe-gQN-OHfJn8Kx6z2hUV9sZHCj53jnltCE5WZGP8PzqaboMycrty49ErigIXGjKygGsEf6gpYXPxtbYPHx3k28jVVEpjav8D9irBHRiZifGwGHOzcx7vCi5PI6PlaSP9NqydE9dFBjCJlKTG4CsEvTtvv6qaNeszmcdV8wx3mZ-HmrC8dc1cGfDd4vHiAbQzpTbNExsvtRhMF5cFd0ygJUTwIDK4oPJr3PWjSNXpU5J9YRx1b_egMnTJPiWIYSqbXCC9lslmYqA_3CcuWoVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e778f783a6.mp4?token=sGQmWDUcJhROP7ZXPPAOdEzt7HFrsPUovUhxhP4WO3rdlsD1vmfPeyZcFvAh7Be155kc1d6J1lo6BnoMU7k2SuxzM2-wnvLdZkGaOIjYK3Hml-0TRSPTS2iQdGls9EwEHmoDFcJms7zq6gVKsOzJl7eEHBpY5sas54hiwpg5wqYUfYPuaNqtKfG2oDTchqxOyDydf6USJqWPXDRoCiYuBkTxIQu5S6pMiqC5VrsH1VjBfdJtOOGVBD8WsLqVF6fR3O1KtPMY62oWW1AvuAQ8AM5l6pWdRT1vITjc4hgp6SJ6GTvoc8Z0Jj78B34spRQJsTYW7aB67PAGqW5RvlChFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e778f783a6.mp4?token=sGQmWDUcJhROP7ZXPPAOdEzt7HFrsPUovUhxhP4WO3rdlsD1vmfPeyZcFvAh7Be155kc1d6J1lo6BnoMU7k2SuxzM2-wnvLdZkGaOIjYK3Hml-0TRSPTS2iQdGls9EwEHmoDFcJms7zq6gVKsOzJl7eEHBpY5sas54hiwpg5wqYUfYPuaNqtKfG2oDTchqxOyDydf6USJqWPXDRoCiYuBkTxIQu5S6pMiqC5VrsH1VjBfdJtOOGVBD8WsLqVF6fR3O1KtPMY62oWW1AvuAQ8AM5l6pWdRT1vITjc4hgp6SJ6GTvoc8Z0Jj78B34spRQJsTYW7aB67PAGqW5RvlChFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇾🇪
🇾🇪
الاقمار الصناعية تظهر ان هجمات القوات المسلحة اليمنية استهدفت منشآت شركة إيسكو في مطار الملك خالد الدولي بالرياض، حيث تظهر آثار حروق على أحد المستودعات أو حظائر الطائرات. شركة إيسكو هي شركة تابعة لشركة سامي للإلكترونيات المتقدمة</div>
<div class="tg-footer">👁️ 6.5K · <a href="https://t.me/naya_foriraq/92714" target="_blank">📅 15:38 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92711">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec18e4b397.mp4?token=GA2egOc1cceOVO1VRPKJ-DoyZnPKsMzJdJyHnrl-zm2jtdPVe8_6Xu-mg9wpNGBXFLidtvEylH2pT-igJJxE-F0eX4-PraRKmDhNMINoNf1BFfukQImOj3LA9RgJ17oDDvPs3yQcAL5z4qU2AV8RDxSVpG5Wrmo8j8r8MWMB1YGyYGW6AgFn9fDcC5kbXINiP2sCy_O6mk5Vl3rCHJjT9gfKFRCWJm3SpgjhpDbM9tSk_vy_wSMQRVF-Stklqzgcr_BaQfAE3fJsI-rZzSB9If_8xC5Wqln4jHtMHz4J9UCdavjPTaL6RuImkTUM19TXVdUTOVF9625fby7X3wzul6u798iEUBAPu5fvQx3U3JwvgE0-TnW17aY6lho2USfNLrc3RFuT-8nP2ye7YF8XVQk91eUp-qx2H7ynhCyVcdfkf678d9LBx1s-VaDjSI-q6WrVyFqk0nhfq7p_v8sE30eu_xZUOGw9ryWlL7us2qAc7_AUOG2oGTdwyFnm12hm4i5hVkXtJR2xlqgV0PcgnJFwthNKsd-0F3D5lkC0CgsvL-dnXDrqGoMd32DVmiIBMMbbahGq_RxRjOmYIGwMsrv1w9-wUz1juG-1_GmG5FJO7Wytcks0Dn22BtisLHMlCnBjN7JmEVpP0jVCAJv1qXJSV2800XMB0dK-SdRs6zQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec18e4b397.mp4?token=GA2egOc1cceOVO1VRPKJ-DoyZnPKsMzJdJyHnrl-zm2jtdPVe8_6Xu-mg9wpNGBXFLidtvEylH2pT-igJJxE-F0eX4-PraRKmDhNMINoNf1BFfukQImOj3LA9RgJ17oDDvPs3yQcAL5z4qU2AV8RDxSVpG5Wrmo8j8r8MWMB1YGyYGW6AgFn9fDcC5kbXINiP2sCy_O6mk5Vl3rCHJjT9gfKFRCWJm3SpgjhpDbM9tSk_vy_wSMQRVF-Stklqzgcr_BaQfAE3fJsI-rZzSB9If_8xC5Wqln4jHtMHz4J9UCdavjPTaL6RuImkTUM19TXVdUTOVF9625fby7X3wzul6u798iEUBAPu5fvQx3U3JwvgE0-TnW17aY6lho2USfNLrc3RFuT-8nP2ye7YF8XVQk91eUp-qx2H7ynhCyVcdfkf678d9LBx1s-VaDjSI-q6WrVyFqk0nhfq7p_v8sE30eu_xZUOGw9ryWlL7us2qAc7_AUOG2oGTdwyFnm12hm4i5hVkXtJR2xlqgV0PcgnJFwthNKsd-0F3D5lkC0CgsvL-dnXDrqGoMd32DVmiIBMMbbahGq_RxRjOmYIGwMsrv1w9-wUz1juG-1_GmG5FJO7Wytcks0Dn22BtisLHMlCnBjN7JmEVpP0jVCAJv1qXJSV2800XMB0dK-SdRs6zQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">القوات المسلحة اليمنية من وسط المدن المحررة في الساحل الغربي تكشف زيف الاعلام السعودي الذي ادعى دخولها</div>
<div class="tg-footer">👁️ 6.84K · <a href="https://t.me/naya_foriraq/92711" target="_blank">📅 15:25 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92709">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db9df5fb72.mp4?token=IRTlM77WkwpU-x_s0VqrgVOWcbts-p0cMuIf6jYVkwwmMwtYwUQGupGNBa9U6GGci_lrqlO5SXYb9ZYOMpdr_AAabj2SR0J9Ik3vlnwUFggdVL5OS9_TykPh8_Lnob9LiUDPlhskMPFYYVWuZQ-YzrnVpwIYJcC6Lg3xiuJeEKaLth9UwPz9lxzGaS8Bu96sR62ebb1x7RyZQ6M05ZNM5lG2Am2V1qcQTzsiKTGDaN88TfY9vZhkj4d9YQiz9p8b4Wr8baeXOeXXOWqLpO1aighRQEc3z3U5gdwkvktOZHur7u5BcE2gbQz_Ce8uk0OAv0rIMUGhPZnPGjuJuDgcD4KvSr3UTQyXTtVrKrh3nmYt6fogTK35QtUG4ar6jAhlyBkH9PNdMP4VotGlabuR1QOy4zDWrdTsnMHIBz3UHfsDrI95uyoRR2soD100seHxFPOjX455KeXRsyG3pN6STpikfaMSuMnXzkwz_RRZbvJfdpnMIRmn2yRBsySkhI-ErwvdFWm9KIxZ8zkm2bM7Hm4SCRokghJzYmOgnJMpHld6PC8SxP76qKf7Bmmueqi5jdQ6IjpPtnA6b6YmmTgLuV2B7QIUDtU0qC8Fc_uzk_wxppgGCdvuzMVYk1jV9fYDwJPAz9PR87vi4Ik0pkaJOnoJQzW8hX-xsjKou1FjMuM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db9df5fb72.mp4?token=IRTlM77WkwpU-x_s0VqrgVOWcbts-p0cMuIf6jYVkwwmMwtYwUQGupGNBa9U6GGci_lrqlO5SXYb9ZYOMpdr_AAabj2SR0J9Ik3vlnwUFggdVL5OS9_TykPh8_Lnob9LiUDPlhskMPFYYVWuZQ-YzrnVpwIYJcC6Lg3xiuJeEKaLth9UwPz9lxzGaS8Bu96sR62ebb1x7RyZQ6M05ZNM5lG2Am2V1qcQTzsiKTGDaN88TfY9vZhkj4d9YQiz9p8b4Wr8baeXOeXXOWqLpO1aighRQEc3z3U5gdwkvktOZHur7u5BcE2gbQz_Ce8uk0OAv0rIMUGhPZnPGjuJuDgcD4KvSr3UTQyXTtVrKrh3nmYt6fogTK35QtUG4ar6jAhlyBkH9PNdMP4VotGlabuR1QOy4zDWrdTsnMHIBz3UHfsDrI95uyoRR2soD100seHxFPOjX455KeXRsyG3pN6STpikfaMSuMnXzkwz_RRZbvJfdpnMIRmn2yRBsySkhI-ErwvdFWm9KIxZ8zkm2bM7Hm4SCRokghJzYmOgnJMpHld6PC8SxP76qKf7Bmmueqi5jdQ6IjpPtnA6b6YmmTgLuV2B7QIUDtU0qC8Fc_uzk_wxppgGCdvuzMVYk1jV9fYDwJPAz9PR87vi4Ik0pkaJOnoJQzW8hX-xsjKou1FjMuM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
مشاهد خاصة لنايا تظهر تصاعد اعمدة الدخان من الرياض وجدة بعد هجمات للقوات المسلحة اليمنية</div>
<div class="tg-footer">👁️ 6.84K · <a href="https://t.me/naya_foriraq/92709" target="_blank">📅 15:22 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92707">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf09f757cc.mp4?token=VhPXmuF3dtecmCwsd14QT9Ehzb3H18AuXyUs_Z8ivaTuhU3vh9AUr1al4F7IoZ0VhhpheK2drR3tYGr7wxleRs15vb-f6vkW2P5R1LhUU_Reuj3y1Nu1o83zghXHu-5KahwF3cKFQjtZFKItaMIoIwYIc8qwyOrr3BvaThH5bGFNwh_Yet3pzxEj2O3hvemSGHtfVs2T4qoXVQEafdIWpSLoZrnuJJe44nWNU-R4odYIVOjE9hb_AGlcvI5PeFLYihtsVxIuPmCukoOwjoN_HzBp20pe6Lwu2oKWthVuwnGBDhqKKEfLuPQ-jQg0MrXes7Gtg4VB2ZvRKFuH9XwrXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf09f757cc.mp4?token=VhPXmuF3dtecmCwsd14QT9Ehzb3H18AuXyUs_Z8ivaTuhU3vh9AUr1al4F7IoZ0VhhpheK2drR3tYGr7wxleRs15vb-f6vkW2P5R1LhUU_Reuj3y1Nu1o83zghXHu-5KahwF3cKFQjtZFKItaMIoIwYIc8qwyOrr3BvaThH5bGFNwh_Yet3pzxEj2O3hvemSGHtfVs2T4qoXVQEafdIWpSLoZrnuJJe44nWNU-R4odYIVOjE9hb_AGlcvI5PeFLYihtsVxIuPmCukoOwjoN_HzBp20pe6Lwu2oKWthVuwnGBDhqKKEfLuPQ-jQg0MrXes7Gtg4VB2ZvRKFuH9XwrXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">القوات المسلحة اليمنية في ذو باب وباب المندب</div>
<div class="tg-footer">👁️ 7.3K · <a href="https://t.me/naya_foriraq/92707" target="_blank">📅 15:13 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92706">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🇮🇱
وزير الحرب الصهيوني كاتس:
في حال وجهت أجهزة السلطة الفلسطينية أسلحتها ضد المستوطنين وقوات الجيش في الضفة الغربية ومستوطنات خط التماس سنعلن الحرب على السلطة الفلسطينية، وسنشن هجوما شاملا وفق خطة منظمة جرى إعدادها والمصادقة عليها مني ومن رئيس الحكومة نتنياهو. ستكون المعركة قصيرة وعنيفة، وستشمل استخدام قوات برية وجوية ووسائل خاصة، واغتيال مسؤولين كبار ونفيهم، وتدمير الأسلحة والعتاد الحربي، وإجلاء السكان على نطاق واسع، وتدمير البنى التحتية.</div>
<div class="tg-footer">👁️ 7.89K · <a href="https://t.me/naya_foriraq/92706" target="_blank">📅 15:03 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92705">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">القوات المسلحة اليمنية تسيطر على جبل مطران بمديرية الصلو بمحافظة تعز وتغتنم عتاد عسكري كبير من الآليات والأسلحة المتنوعة</div>
<div class="tg-footer">👁️ 8.93K · <a href="https://t.me/naya_foriraq/92705" target="_blank">📅 14:43 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92704">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">مشاهد من جريمة العدو السعودي وإبادة أسرة المواطن علي عضلي في حرض بمحافظة حجة</div>
<div class="tg-footer">👁️ 9.98K · <a href="https://t.me/naya_foriraq/92704" target="_blank">📅 14:22 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92703">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🇾🇪
🇾🇪
القوات المسلحة اليمنية:
ترقبوا الساعة الرابعة عصرا مشاهد لاستهداف التحشيدات التابعة للعدو السعودي في رأس العارة</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/naya_foriraq/92703" target="_blank">📅 14:08 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92702">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🇶🇦
الخارجية القطرية:
من المبكر الحديث عن احتمال انضمام قطر لحلف مكة.</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/naya_foriraq/92702" target="_blank">📅 14:01 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92701">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">أ ف ب عن مصادر هندية: إصابة 12 شخصًا بعد تعرض ناقلة لهجوم قبالة سواحل سلطنة عمان</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/naya_foriraq/92701" target="_blank">📅 13:56 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92700">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🔻
الـ100 دولار امريكي تسجل ارتفاعا كبيرا في الاسواق العراقية وتصل لـ161,500 الف دينار عراقي</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/naya_foriraq/92700" target="_blank">📅 13:54 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92698">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🇾🇪
مصدر يمني: مقتل عبد الرحمن الشمساني قائد اللواء ٣٥ مدرع في جبل مطران بمحافظة تعز.</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/naya_foriraq/92698" target="_blank">📅 13:33 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92697">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🇾🇪
🇸🇦
وسط إنكسارات وفرار مرتزقة السعودية.. القوات المسلحة اليمنية تستمر في تقدمها وتسيطر على مناطق شرجب وهيجة العبد ويافق والشوار وتبدأ دخول مديرية المقاطرة وبني يوسف بمحافظة تعز من عدة اتجاهات.</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/naya_foriraq/92697" target="_blank">📅 13:29 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92696">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/685539bddd.mp4?token=S6-nSHz9n9qfOd8s7vOTg_nXL97IB6jbKygPkbwzPGsmIGcG-GhQdMreW5Fu5oFAOdam8iKkBmppxgjOFL_VN1ozooYy0xxmCgn3eQb-SLK9OLaShVaCbXnoWnvv2i26Vjt_-l3qVqNqPfKfMe_FybHKW08DP0QQlfruEBXPgsPfQN4igi1BnM6ftlFq5_xz0w06INYqNySBe2o1Du-V8wPmqQQOBz1AdVOADbzd1d5W29ClclBsCL1kq4nVMocojrTEwSrBGPQuj4iH1MZNneFzz2VtysPkn-0hhPgPKx0O4HaTPUypyd-bIabRTTJIFJM8Lny8WLEahNRfGepq3Z233y734OJ_VHqKuljIbSaXNOzUPHRwRwKyRcluiBRy0Mw95ateBYqDz9mso69eXjUaISTJwjnayB7XEydJFVziW5lKHzmrcjAT9jSQjP_Ndg5bGZEU96lvVWWnNsB7Bq16MNjmcgL1LvMr8j0ddA5ctNePg3JtfDAhjIpqPI-ZyIci-laOtgE5-bYd-Srakp3UUmdCBwEH3leO2cu_qu3-i3eaKuss95S3WulhvfyLW-ejhtdf7vHSTjrf54mEkxSkonUp5cbSHYPTuZO5TWBeW3NSbfn_UigxdSdSTRrrM51iXsdNI5LcSX9rYG3d35v4CLeSU8DnfymPikCRCjk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/685539bddd.mp4?token=S6-nSHz9n9qfOd8s7vOTg_nXL97IB6jbKygPkbwzPGsmIGcG-GhQdMreW5Fu5oFAOdam8iKkBmppxgjOFL_VN1ozooYy0xxmCgn3eQb-SLK9OLaShVaCbXnoWnvv2i26Vjt_-l3qVqNqPfKfMe_FybHKW08DP0QQlfruEBXPgsPfQN4igi1BnM6ftlFq5_xz0w06INYqNySBe2o1Du-V8wPmqQQOBz1AdVOADbzd1d5W29ClclBsCL1kq4nVMocojrTEwSrBGPQuj4iH1MZNneFzz2VtysPkn-0hhPgPKx0O4HaTPUypyd-bIabRTTJIFJM8Lny8WLEahNRfGepq3Z233y734OJ_VHqKuljIbSaXNOzUPHRwRwKyRcluiBRy0Mw95ateBYqDz9mso69eXjUaISTJwjnayB7XEydJFVziW5lKHzmrcjAT9jSQjP_Ndg5bGZEU96lvVWWnNsB7Bq16MNjmcgL1LvMr8j0ddA5ctNePg3JtfDAhjIpqPI-ZyIci-laOtgE5-bYd-Srakp3UUmdCBwEH3leO2cu_qu3-i3eaKuss95S3WulhvfyLW-ejhtdf7vHSTjrf54mEkxSkonUp5cbSHYPTuZO5TWBeW3NSbfn_UigxdSdSTRrrM51iXsdNI5LcSX9rYG3d35v4CLeSU8DnfymPikCRCjk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇾🇪
🇾🇪
رجال أبوجبريل من مطار المخا الدولي ترد وتنفي مزاعم وأكاذيب إعلام دويلات الخليج حول تقدم المرتزقة نحو المدن اليمنية.</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/naya_foriraq/92696" target="_blank">📅 13:15 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92695">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🇷🇺
الكرملين:
روسيا سوف تضطر للتصرف لحماية أمنها إن استضافت ليتوانيا أسلحة نووية أو قاعدة على أراضيها.</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/naya_foriraq/92695" target="_blank">📅 13:09 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92694">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🇮🇷
مقتل عدد من العناصر الإرهابية على يد القوات الأمنية في محافظة بلوشستان جنوب شرق إيران.</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/naya_foriraq/92694" target="_blank">📅 13:01 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92693">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mW2SQSryB-42B5vXguO7qZ4f39mOni1ndAU0HLMo6xatc1fTX3aT4GIVOG02SVTLIMjYJdDQc5XvL-ji07swc-PBOtw4JfTtF_J33jQ9MiLCYwkySdu1XUGW340MY1VIMNeWt1CengZDAiLEVxtgxvRfMoBUpNDR-qr9tdf6CkTpO5VMFzfx_nmjSspiAkfoJaS_G29bazaxsiv8zci9fxuPYn77oBIi8eTJwb9kwGkEYV_EVdR-tXQhZci8QejSxpN_9RAFvIbGZY2u0YxDKSyvnc_Psf0YIo0pKAABOBK1IJK-NHryBAvG8WQLol3RlEWuR0i7DClGHTF3zkk2Ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇾🇪
مراسل قناة المسيرة في باب المندب يعلن سيطرة القوات المسلحة اليمنية عليه.</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/naya_foriraq/92693" target="_blank">📅 12:56 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92692">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🇾🇪
القوات المسلحة اليمنية:  تمكنت قواتنا المسلحة بفضل الله من استهداف تحشيدات العدو السعودي في معسكر الدغارير في جيزان بعدد من الصواريخ الباليستية وكانت الإصابات دقيقة ومباشرة بفضل الله وخلفت عشرات القتلى والجرحى في أوساطهم وهروع سيارات الإسعاف إلى المكان المستهدف،…</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/naya_foriraq/92692" target="_blank">📅 12:48 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92691">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🇾🇪
القوات المسلحة اليمنية:
تمكنت قواتنا المسلحة بفضل الله من استهداف تحشيدات العدو السعودي في معسكر الدغارير في جيزان بعدد من الصواريخ الباليستية وكانت الإصابات دقيقة ومباشرة بفضل الله وخلفت عشرات القتلى والجرحى في أوساطهم وهروع سيارات الإسعاف إلى المكان المستهدف، وسط حالة من الإرباك في صفوف العدو.</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/naya_foriraq/92691" target="_blank">📅 12:42 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92690">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🇮🇶
مسرور بارزاني:
لا نشعر بالقلق حيال أي مشاكل أمنية قد تنشأ (بعد انسحاب التحالف). القضية الوحيدة التي تهمنا هي تأمين أنظمة مكافحة الطائرات المسيّرة والحصول عليها، أي تعزيز قدرات الدفاع الجوي. أعتقد أننا بحاجة إلى مزيد من المساعدة من حلفائنا في هذا الشأن. ما زلنا على تواصل مع الحكومة الاتحادية، ونجري أيضًا مناقشات مستمرة مع حلفائنا لتأمين القوات وقدرات الدفاع الجوي."</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/naya_foriraq/92690" target="_blank">📅 12:25 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92689">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🇾🇪
القوات المسلحة اليمنية تسيطر على مناطق شريع والمخعف وبلعان والميسار وجاحصه وجبل زنم في محافظة تعز.</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/naya_foriraq/92689" target="_blank">📅 11:09 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92688">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🇸🇦
هيئة الطيران المدني السعودية تزعم:
إصابة 3 أشخاص في استهداف مطاري نجران وجازان مساء أمس.</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/naya_foriraq/92688" target="_blank">📅 11:04 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92687">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/39a7d65637.mp4?token=DcOglo2qotzCKn19qyLRDbHUilzoC4atR0EXT-VxOC1JXZrqZQ3gTJ1TdoLA-NerSWj4w0jwkWhwEOcFVJ39EAhSZJZ6S-H5nPcgPzBrjfEv6vJvZiiS13nNsdU4GtjHzKVjkaRmIuTiswYFGvsknbsSN2dM2Jj4nlvGCSN0tZCgkqUMyC8FTj1_NLgHAVK0KGsrH3lsyJZV8PDLlVPVHUs61iFsLO7eEQnVUWG7uX0bXO_gXsW0me9iMFxn1bGUK_tLselIZBXe1St5GYvJeZOMwpJ72yQ9LXL3EYniYyXVIkyXU6gJb6KpkyXvyLQuquaptQzKgBmp0LfyLe4HEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/39a7d65637.mp4?token=DcOglo2qotzCKn19qyLRDbHUilzoC4atR0EXT-VxOC1JXZrqZQ3gTJ1TdoLA-NerSWj4w0jwkWhwEOcFVJ39EAhSZJZ6S-H5nPcgPzBrjfEv6vJvZiiS13nNsdU4GtjHzKVjkaRmIuTiswYFGvsknbsSN2dM2Jj4nlvGCSN0tZCgkqUMyC8FTj1_NLgHAVK0KGsrH3lsyJZV8PDLlVPVHUs61iFsLO7eEQnVUWG7uX0bXO_gXsW0me9iMFxn1bGUK_tLselIZBXe1St5GYvJeZOMwpJ72yQ9LXL3EYniYyXVIkyXU6gJb6KpkyXvyLQuquaptQzKgBmp0LfyLe4HEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇾🇪
🇸🇦
مصدر يمني: عدد القتلى والجرحى في رأس الغارة يتجاوز 100 مرتزق.</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/naya_foriraq/92687" target="_blank">📅 10:36 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92686">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a87fXXPV8HfRJTUxD0m8_nITQbc01aE6DsIp_sUYvlMw-jZsYau8CN3NqxbD0T9NC_ajrdWUoJGNIGKYW4bRuYM3cOgwxeqR8olFbCDO6BowiDeQDilE4KOdaiL-lZxGUbX6XgmGzh4_SxpOSOTgpopm1pu-q3QINYggAkewGQBfecDNP1mIIlWGW_D5o9Sih4vXq_Xe9IluaYsUcaD-jiRxbDP0LirEcyuNdnnp6I1MiDMWjVM72Vu86rKuGR6lZ2U7XBCDjaAMPTcVi9bwXEktYf0dG_VJw-i9vV8ULuvK_SrvuvYId0bdbytgJTCiUjlb5xW2_M17SYLv2vtaQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
🇦🇪
🇺🇸
بحرية الحرس الثوري تجبر سفينة إماراتية بالعودة عن مسارها أثناء محاولة عبور للممر الجنوبي في مضيق هرمز، وذلك بالتزامن مع مرافقة الطيران الأمريكي لها.</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/naya_foriraq/92686" target="_blank">📅 10:32 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92685">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🔻
‏إصابة سفينتين بمسيّرات في البحر الأسود قبالة سواحل بلغاريا.</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/naya_foriraq/92685" target="_blank">📅 10:27 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92684">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EZll4NYT4GA_VB4pNur91KSlkN8qSlRo8fEUNPAbQWn-lF3m-Pg1i6RyIw_yws274kXifCs6j0_umsCJPmoV5K0reFvoDHlVR6kl1M97gI5Hp0w1xPFx27XK7b155Ac3D083VHF5Z-hDBi7nq-3A5yoE90chIDUchHUdgjbuKvdGEc-3SH6gUCJCJrWfWJnlOSqiFgtUFpc8XDfI-J4J82790vtBo9I8NXZ8EiJ-VQaI0GJKxgvMv07FJ0ZxMgtoCJD9FFH_HZTnLROFQFU8snjM85zext5RpQwJrYxqgEH59vMXC586ioZ6xjip8SGz3-DmGuOBKzE5f36mF3U3Lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇸🇦
توقف العمليات الجوية في مطار الملك خالد الدولي في الرياض.</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/naya_foriraq/92684" target="_blank">📅 10:25 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92683">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cvYPfurK412_UhTOImK4z20YiUcv5H2JLgRv_lD8e0o8Hw_AnjDZyYwt_UvCdOrVW-aYFjUfMGTfadAoCLy8FtjN6VUSu_tjDpyKAjr0C5UOjyZ_VjC-MsO88kKHcMUcuk2UIRRyjUzNEbKXEI47IqzlDifWUn053s45Nkisp-6_jbjYk6uHGGap73Ps0Q_uSNQtveWXUoED7lMzNVY2LG9ESQV_WWDwJlLSN5hufAZSYOghQK7BHBxrl0Vh3xfmCL_R0a4eXAyc01ovwKnmVZdRr12gcrBOENT4mWZIrouQ_eIscBmqEB4XObaKxKPm0sCq5RvxGQKSDNO3OpCdYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
مقتل عدد من العناصر الإرهابية على يد القوات الأمنية في محافظة بلوشستان جنوب شرق إيران.</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/naya_foriraq/92683" target="_blank">📅 10:23 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92682">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🇾🇪
القوات المسلحة اليمنية: تواصل القوات المسلحة مطاردة تحشيدات العدو السعودي في ما تبقى من مديريات محافظة تعز وسط حالة إرباك كبيرة في أوساط تلك التحشيدات وهروب عدد منهم.</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/naya_foriraq/92682" target="_blank">📅 10:08 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92681">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🇾🇪
مباشر من مديرية ذوباب، وسط سيطرة تامة للقوات المسلحة اليمنية عليها.</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/naya_foriraq/92681" target="_blank">📅 10:00 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92680">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🇾🇪
🇸🇦
مجدداً..
مصافي النفط في جدة تحت رحمة الصواريخ اليمنية.</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/naya_foriraq/92680" target="_blank">📅 09:24 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92679">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67d2663057.mp4?token=pAubpagVXxKdqsC6cwR8S6I4XF1o4IefzXeZ-thDsUbk4ysYfKmrY8xrC9e6dj6mHqF6HlIwDAawiBvG0WB9lglHER8hbbZm0JjFYyqhnnoDWanzeQThh48Bm_Wxl8DOeSx-cZWvhqAJH--2r5rLx64FfH98YoRD-84nkLaedtF4TSZtTMUIizwaI8ugzD20Fqc08TDMO6V4VJhhv7bQ16NGSHF8UiWwVYEA8XvTCfVW6OgJkCxcq4JXmvBcPHNgVAw9sPrvu2-qidzLIwcSxUoz2llT_i9PujNfAeQ3Imp7ibNxDpkLA4anDMbUj_bKnOZA98zBpWO6dfRCg_BbxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67d2663057.mp4?token=pAubpagVXxKdqsC6cwR8S6I4XF1o4IefzXeZ-thDsUbk4ysYfKmrY8xrC9e6dj6mHqF6HlIwDAawiBvG0WB9lglHER8hbbZm0JjFYyqhnnoDWanzeQThh48Bm_Wxl8DOeSx-cZWvhqAJH--2r5rLx64FfH98YoRD-84nkLaedtF4TSZtTMUIizwaI8ugzD20Fqc08TDMO6V4VJhhv7bQ16NGSHF8UiWwVYEA8XvTCfVW6OgJkCxcq4JXmvBcPHNgVAw9sPrvu2-qidzLIwcSxUoz2llT_i9PujNfAeQ3Imp7ibNxDpkLA4anDMbUj_bKnOZA98zBpWO6dfRCg_BbxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇱
إنفجار سيارة في القدس المحتلة؛ سقوط عدة إصابات كحصيلة أولية.</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/naya_foriraq/92679" target="_blank">📅 09:02 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92678">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🇾🇪
مناطق كحاح ونجد العود في محافظة تعز تحت سيطرة القوات المسلحة اليمنية.</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/naya_foriraq/92678" target="_blank">📅 08:15 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92677">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fdc64f78bd.mp4?token=chjG2slC6_-WaMtuKrOdTCAab5LmMr6ah2Pb_hwAHgQQt9Wp_8WmIJYNZtaz7YaMYiyEee294PHyrZrcR7_aP3JMAGvSX6F3TWvsJWGyTZr_3KFL4nv3UUvCDwpUd135oaWEtnuurxt1JtqNxFV3byeNX1pdAajSd3H4djdATKHgDcYNPLgecfM9FCKegSOu43tUqbMetj0qXhfBfo8xRH5zYKMWp_On3hv_ci1wOxbZJ6Hz59AmLI6S3K1e8BoTZQ-llDjLyg2xD1-A20a74iea86pGIP3ekzz-zOR4HuILaVbR8kwpREJ38Uk7BBUthGwA3EUo_njnkhG1aC69eg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fdc64f78bd.mp4?token=chjG2slC6_-WaMtuKrOdTCAab5LmMr6ah2Pb_hwAHgQQt9Wp_8WmIJYNZtaz7YaMYiyEee294PHyrZrcR7_aP3JMAGvSX6F3TWvsJWGyTZr_3KFL4nv3UUvCDwpUd135oaWEtnuurxt1JtqNxFV3byeNX1pdAajSd3H4djdATKHgDcYNPLgecfM9FCKegSOu43tUqbMetj0qXhfBfo8xRH5zYKMWp_On3hv_ci1wOxbZJ6Hz59AmLI6S3K1e8BoTZQ-llDjLyg2xD1-A20a74iea86pGIP3ekzz-zOR4HuILaVbR8kwpREJ38Uk7BBUthGwA3EUo_njnkhG1aC69eg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇦
مشاهد حصرية من داخل إحدى الطائرات التي تلقت تنبيهًا بعدم الهبوط في مطار الملك خالد بالرياض.  https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/naya_foriraq/92677" target="_blank">📅 04:43 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92676">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🇾🇪
🇸🇦
وسط فرار مرتزقة السعودية.. منطقة بني حماد في محافظة تعز تحت سيطرة القوات المسلحة اليمنية.</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/naya_foriraq/92676" target="_blank">📅 03:18 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92675">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57f0671c1b.mp4?token=PgUs-N4mmz8loFLcrzAPXOUKg2INT4M4fHrKM1RTUxzElsnCRWrPOqUJwQDfXAMv7PTrOxDTwNYzBhHN7aMRa3euO5dtvSJ0K6drDYTEqmfgJ6KAHa5uXRcjNup7PlX9PlcHvUVDQPF9RyOJiK3SKorngnmk6G_ZVwiVSI1C4_PzNgxEZ1vc9ep9M3Sdtbs5EXuAenLq6M8v_kZ3mbJw3XFNmS-4jy1aVq98bFBXqPvMBbK4vxAy3ms21exsYm_lcC2A0VOJ0tc4aOooRkrE0ApcLzYplhpIPRxiNNyr9dn-2C_UlPQNKqRC09bP7tHk-fa3JvJ_onw5ytZlblCK0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57f0671c1b.mp4?token=PgUs-N4mmz8loFLcrzAPXOUKg2INT4M4fHrKM1RTUxzElsnCRWrPOqUJwQDfXAMv7PTrOxDTwNYzBhHN7aMRa3euO5dtvSJ0K6drDYTEqmfgJ6KAHa5uXRcjNup7PlX9PlcHvUVDQPF9RyOJiK3SKorngnmk6G_ZVwiVSI1C4_PzNgxEZ1vc9ep9M3Sdtbs5EXuAenLq6M8v_kZ3mbJw3XFNmS-4jy1aVq98bFBXqPvMBbK4vxAy3ms21exsYm_lcC2A0VOJ0tc4aOooRkrE0ApcLzYplhpIPRxiNNyr9dn-2C_UlPQNKqRC09bP7tHk-fa3JvJ_onw5ytZlblCK0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
بعد إستهداف 13 سفينة خلال أقل من إسبوع من قبل البحرية الإيرانية.. ترامب: استطعنا القضاء على قدرات إيران العسكرية وتأمين مضيق هرمز.</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/naya_foriraq/92675" target="_blank">📅 03:07 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92674">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">ترامب حول إيران: بالمناسبة، نحن نهزم إيران. ألا تعلمون ذلك؟</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/naya_foriraq/92674" target="_blank">📅 03:05 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92673">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e77dc63a0.mp4?token=mew7sj2WB_NkTkcmKePEUWzs8ENQPsrBeiGGsdP9RdTJGh0tlFIRvRt3pkQRtPMXYSHHe4BjjvKNWqg6MAIEmA-cVWbO9o2q2Iih7hn803fcK4IhiAm5FgAWgT6B4hdg94_F9mA16X9UgAu_wVo7WVLA6Mmjl6vIuBvXEEMb4z7eCkuXudaWpVCzM-8rSi5JPkuRibgQnTn9iqeuk99rPoHlwl8cWyDkZXzwpt96_rrbZP-_L5Pvp_W8WvBVC8HNeralQsTngBOc5WKvWGgnu9JvBDIij_n_cOxtBmqfPr7nF-wUhcNMiivuoZthvXTRbWSNWUncAiWYFqVx-UtGCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e77dc63a0.mp4?token=mew7sj2WB_NkTkcmKePEUWzs8ENQPsrBeiGGsdP9RdTJGh0tlFIRvRt3pkQRtPMXYSHHe4BjjvKNWqg6MAIEmA-cVWbO9o2q2Iih7hn803fcK4IhiAm5FgAWgT6B4hdg94_F9mA16X9UgAu_wVo7WVLA6Mmjl6vIuBvXEEMb4z7eCkuXudaWpVCzM-8rSi5JPkuRibgQnTn9iqeuk99rPoHlwl8cWyDkZXzwpt96_rrbZP-_L5Pvp_W8WvBVC8HNeralQsTngBOc5WKvWGgnu9JvBDIij_n_cOxtBmqfPr7nF-wUhcNMiivuoZthvXTRbWSNWUncAiWYFqVx-UtGCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامب حول إيران: بالمناسبة، نحن نهزم إيران. ألا تعلمون ذلك؟</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/naya_foriraq/92673" target="_blank">📅 03:02 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92672">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🇾🇪
🇸🇦
بعد قتل وأسر العشرات من مرتزقة السعودية.. مشاهد لسيطرة رجال أبوجبريل على منطقة رأس الغارة.</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/naya_foriraq/92672" target="_blank">📅 02:56 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92671">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a73627067.mp4?token=XrP7RvPJkwWHm1GKFS-BUjBogoeUkP6q2j_wwuYTXtegajX9HQ62YdExVcsHUlfl-JDiqRyLbVwYj76gDGg9UTIL7wOM8fNp0ctFD5cRqaLXTkNFceIGTMKIBKDIPsLCgQFEWmqF9Znmk8P2kt1JjJEZnSX24PQZuaX46urWMgMJNy2zh5_lU52Kx5mpb8KlGWRLR_PBfqsa1cc6vmQtv7C8SzqCTfpnTGRUZWy6GxlUnmm8MjQuwms1AV_TWDC7OJBApIyFRgNPdnAUsyrKEyOKla_zhGTAnEUnZbaCVuP30OsCQca5HXAyHRMdegVSJYVpMtN3P55ax0olkPZreQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a73627067.mp4?token=XrP7RvPJkwWHm1GKFS-BUjBogoeUkP6q2j_wwuYTXtegajX9HQ62YdExVcsHUlfl-JDiqRyLbVwYj76gDGg9UTIL7wOM8fNp0ctFD5cRqaLXTkNFceIGTMKIBKDIPsLCgQFEWmqF9Znmk8P2kt1JjJEZnSX24PQZuaX46urWMgMJNy2zh5_lU52Kx5mpb8KlGWRLR_PBfqsa1cc6vmQtv7C8SzqCTfpnTGRUZWy6GxlUnmm8MjQuwms1AV_TWDC7OJBApIyFRgNPdnAUsyrKEyOKla_zhGTAnEUnZbaCVuP30OsCQca5HXAyHRMdegVSJYVpMtN3P55ax0olkPZreQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇾🇪
🇸🇦
قصف صاروخي عنيف للقوات المسلحة اليمنية على تجمعات مرتزقة السعودية في منطقة "رأس العارة"، والقتلى بالعشرات.</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/naya_foriraq/92671" target="_blank">📅 02:47 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92670">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Audio</div>
  <div class="tg-doc-extra"></div>
</div>
<a href="https://t.me/naya_foriraq/92670" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">قولو له الرياض اقرب</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/naya_foriraq/92670" target="_blank">📅 02:45 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92669">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/88dade42c2.mp4?token=tR4BGJjmNu4l8I_j4t_VtmRrzUTgB46n6iCcCrimW59LlCH534SkvNg4Vp8QsEtF4_Ph8GnQyO14uz00mX8AaWdAC69y0hr94G2lK199avPuLiD80tNYnrv_ZrA1H9OrbKn0uekDqmb-9AfPfg_8e_zUsZ_bPewcJvtP0DC-VzJZhBnmINP8IhZ3k-HJd8rPo6HI7oHY3w8cHxXKIGlxRFXQBOh323SWEUXiY7z-x7AXpqpiE8UrIJlqINXiXSb03C4jAGEuboe26vt6msXnSYUm1kwMh7M5sbyXZnynNxvqLxoKyD0_2endqNGv_qD_Ai3MYNLw-w61kHJaKwYMKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/88dade42c2.mp4?token=tR4BGJjmNu4l8I_j4t_VtmRrzUTgB46n6iCcCrimW59LlCH534SkvNg4Vp8QsEtF4_Ph8GnQyO14uz00mX8AaWdAC69y0hr94G2lK199avPuLiD80tNYnrv_ZrA1H9OrbKn0uekDqmb-9AfPfg_8e_zUsZ_bPewcJvtP0DC-VzJZhBnmINP8IhZ3k-HJd8rPo6HI7oHY3w8cHxXKIGlxRFXQBOh323SWEUXiY7z-x7AXpqpiE8UrIJlqINXiXSb03C4jAGEuboe26vt6msXnSYUm1kwMh7M5sbyXZnynNxvqLxoKyD0_2endqNGv_qD_Ai3MYNLw-w61kHJaKwYMKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الله اكبر طائرات عدة تتلقى تنبيه جديد بعدم الهبوط في مطار الملك خالد في الرياض</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/naya_foriraq/92669" target="_blank">📅 02:42 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92668">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">خروج مطار الرياض عن العمل وتوقف اغلب الرحلات عن الهبوط والاقلاع بسبب هجمات أنصار الله في اليمن</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/naya_foriraq/92668" target="_blank">📅 02:41 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92667">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k31KqMrOP5nDl8WjALeiYoXJ-bLYJgFQK9f_x4vN1CL8IckyoZqifmbQUg1-KOo0JoXzxQnV8wZc4vf2-bOZOhx0BnRks1otaQY20Z91toJNmTrnOcc3UUbe2-mEnb83kIE0R_m_p5oms4hSpIHMdnr_wy5GMfaIDdFQJ1QLnUXeMorqyzNqDv-JVG0H9V2iBOn959nxp8aEdXlRcshrHLFgHARZ4te1nAmx7o74vdyeoD5rj_HyVvKRJYF_XRBrgvrYH14W6OYu-IUKZ_sv8xO6zBeofVo1N3IEt9JU7SKP3S0UbHofwuXUrymuGpvdQg7nvX2Gn0-5xpFCKb5zMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الله اكبر   انفجارات عنيفة تهز الرياض مجددا</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/naya_foriraq/92667" target="_blank">📅 02:30 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92666">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">الله اكبر
انفجارات عنيفة تهز الرياض مجددا</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/naya_foriraq/92666" target="_blank">📅 02:28 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92665">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">‏
🇹🇷
🔻
🇷🇺
وصلت طائرات يوروفايتر الألمانية وطائرات إف-16 التركية المقاتلة إلى لاتفيا في وقت سابق من هذا الأسبوع كجزء من مهمة لحلف الناتو لحماية المجال الجوي للحلفاء.</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/naya_foriraq/92665" target="_blank">📅 02:24 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92664">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">الله أكبر
🇺🇸
مروحية تابعة للبحرية الأمريكية من طراز MH-60S تُطلق إشارة استغاثة برقم 7700 أثناء تحليقها فوق البحر الأحمر، بالقرب من ينبع.</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/naya_foriraq/92664" target="_blank">📅 02:17 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92663">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🇾🇪
🇸🇦
قصف صاروخي عنيف للقوات المسلحة اليمنية على تجمعات مرتزقة السعودية في منطقة "رأس العارة"، والقتلى بالعشرات.</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/naya_foriraq/92663" target="_blank">📅 01:58 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92662">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🇾🇪
🇾🇪
حزام الأسد:
الأجواء السعودية غير آمنة .."قد أَعذَرَ من أَنذَر".</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/naya_foriraq/92662" target="_blank">📅 01:49 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92658">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nW8BHo0PYUjwOwbjfGyH14YKE4Ur7E5mE50AlwwnDLbwBqkJr4N-QfFEJsmV-0RoWscvOeXV-M0NgG6pMzjxp_KUPGx7A1-tmqKxf0YPWn8y_pxiWeEFjDGOc9sWQT5w1lLqR-ELQerYH_lqYA9hnHwK0aKgk8ILZ_dwYC9N5swuyBX-FhKC49vQDJXdcpmGTUOxFugHM8s-5Mfx-fHI6gHLX1uFz03odZu0ToO7HaK1WkuLZ-TrkONq-qpgJmpzoKGH4EzO9B_HnKO7W-uHq124OghbXGcU3L_H_5ORnI7fJwzna-FPmXP9xGFobFK9z6FqfIrLt0MtTPly9KSPog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Sqd7810qdQ-JlFHjYeML5uZgQfzqSkoJbQomShsB6AahPPjqE6i7rD936mw258QYjouo3FYmxyiN-7XPbZP0z43ajEBIGvH8ZEIT4SfGyr4gDhVw3xHcxRK5l4J_b0c_IlRaNVOucLfxlxzVvA1iaBtX2dxSbA0uX-51gzOLHwWiJWt9X3NhR_HyyCooBj8dWVn9EVje__rpp6gCY2aHJSr1HIUuSN-JwnryV7obU61oh6lz6G7g-bX9ZAF4haKMjaqwY7B9wyE21GcUip4thSALeEyomLvyBd_RTmMtl4p-9jx41y4--ew__rqYxw3lSZbBpp4vR0fD8qh4qcLhog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cEQNc5YXiDEC7aEM897XKckj9xTiPPVb4Pd3XdCmOJLaKuEUgYNrfNTPEfDkaiHkWex49j4mpVnVoeoHnjo6SJFr8DXezp29w8r4VnE-MFjcYW--4WgxCGJ92dUszWosJhBa7VffKnS3LOK-i3KLOQ_ipZ89rLmbw3PMohYH881rovKU0vjLZaz9BoNyOgYE6KG2_PX391AnuKcOzGt2FgE32Rm2xHbqgBgOJutiOtTjlKddnZB4m7XBQ_z_4oBPOjRwaDc0dR3julW9bXSCzymNVIl4lMSLpbnFBEMHSkvBl1wYBk5XVbQHkjojx8l2d6o7GgpVVI1CVmGLcsARHw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a4530fd20e.mp4?token=j2Eh9woP3zLtOVlfniMZvD7lfn92uyci9XFzm59Dk9gAsW-NDV0QsCoz3UhE_cHo9gxhM7opM0yEc_sjAyMuPsuy6M_fGy7EWgk2qqwCu9JDzwfI9rJ_q0amWT3XOgc2ALh8cZfHD-rU5J4GAkqYnIMuCS1NMr4aKLpvY-J-qAjKIaCt46TJE-KKhRZdkbhh0piQwSqZeSFK-exh9XYbf73pl2tx7zzyijlxq9vQazcM7YL4LyqIPwSFEB5spN_t6fFri7vZeS863FbASP5P6jzLef_pUQ6RY_FOy0Nr5gyhiPDIbldAfq76j62rtN7pHCpRTzeEpjHOTOEVP8eQZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a4530fd20e.mp4?token=j2Eh9woP3zLtOVlfniMZvD7lfn92uyci9XFzm59Dk9gAsW-NDV0QsCoz3UhE_cHo9gxhM7opM0yEc_sjAyMuPsuy6M_fGy7EWgk2qqwCu9JDzwfI9rJ_q0amWT3XOgc2ALh8cZfHD-rU5J4GAkqYnIMuCS1NMr4aKLpvY-J-qAjKIaCt46TJE-KKhRZdkbhh0piQwSqZeSFK-exh9XYbf73pl2tx7zzyijlxq9vQazcM7YL4LyqIPwSFEB5spN_t6fFri7vZeS863FbASP5P6jzLef_pUQ6RY_FOy0Nr5gyhiPDIbldAfq76j62rtN7pHCpRTzeEpjHOTOEVP8eQZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇦
🇾🇪
توثيق للإصابات الصاروخية المباشرة التي طالت مصفاة النفط التابعة لشركة أرامكو في مدينة الجدة السعودية.</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/naya_foriraq/92658" target="_blank">📅 01:47 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92657">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🇺🇸
🇮🇷
مسؤولين أمركيين:
قاذفات B-1 الأمريكية أُجليت من قاعدة بريطانية بسبب تهديد هجوم بطائرات مسيرة إيرانية.</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/naya_foriraq/92657" target="_blank">📅 01:27 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92656">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nxKXEOH1wstjJfZzUietkTEwI2dLFCIXpfD1VsTA_5ZhaNQRHmxRzTXweemAIW6SlNz3kBhEmywj1tjKiZcQjAQZITtQF8ZGL_jfS_-U9oUkPg348tzkMRIpA_yDF5Mu8TkC_xiynCA-q6h_777UjRTx9BwNv4q3bQSGD9MSks0OCOzjrK0k7pfKCin49qRBCl-XxJ6TGSZL98G9mczm1HnhyINons38dM0Zsp-AcqmVqKRJhUE8STtOhetCtG2rmzaVdhwczDfS9C4PEb2lqyX1DrsiQiE-XHYJGcSjtdszDp49M1UCYlDGWU6ogy30B6SD9Whm3r6YdDdSoNlryg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الله أكبر
🇺🇸
مروحية تابعة للبحرية الأمريكية من طراز MH-60S تُطلق إشارة استغاثة برقم 7700 أثناء تحليقها فوق البحر الأحمر، بالقرب من ينبع.</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/naya_foriraq/92656" target="_blank">📅 01:17 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92655">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🇾🇪
🇸🇦
بعد دحر مرتزقة السعودية.. القوات المسلحة اليمنية تتمكن من السيطرة على مناطق عليافة وجبل صبران واهجوم قدس والمذاحج في محافظة تعز.</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/naya_foriraq/92655" target="_blank">📅 01:03 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92654">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U18RplTBcHHd2sYe3mOm5eSNuJ-ebXTvouBQZbenWlcfMxPA1ubGenkq9WnqFGWiAbATKlt9XF3B9ljoupO9Jt70K21NRTaf024pACX1qxKhjgW_hzJPhwePcQ0eBkJUwA9JqDTRNAtIkcVMTaWXSHIlmathoyPez2BKcWqszp0rlok4ZR3ngB7RLXsSzXXOr3MUCVUx1mdlkcKNs0YhdMWw0WKeaRnRvCIh0pCMN7sCE9T2pZXF_CQJeod9-JXtYbecGuSiIKOGn1IAi535oLrUo6BP9MAH7BkGEdoJAkCvTTbDwxDT8ki5za4_OsKwLaQHAHeov6akj2Tij0FfAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الله أكبر
🇺🇸
مروحية تابعة للبحرية الأمريكية من طراز MH-60S تُطلق إشارة استغاثة برقم 7700 أثناء تحليقها فوق البحر الأحمر، بالقرب من ينبع.</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/naya_foriraq/92654" target="_blank">📅 01:01 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92651">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/796fe880c9.mp4?token=U-4Vl_l04eqVz4LlxngAnHUuRh2IKuE84Z_U6sIsPMRDhkJcZLNe_YaadcruzhPhkQU-VAqj5cniZaE1UR329hAWkXOV9dolnxIztHo7cv4v8GXU8jRfxcPxalbK3zNWo-5nz7Z36OGFXRSvdi5zDqm5UpvNmz603INOgTu65tZzkv80EP576au8Q26ysOufEiGAk8RXV7CU1zOoH5uxwS5fJQ4tMOheWSBvxosHcqfVn8yVC3PSPW3UglhNNAKPxNWtOqTScyDvVXZcSBFOP7JtNDngq0VdDftncB52S7nErbUOqVjbGwQABdqcyria3xTIk7RvJ1_IzsQr7fiBPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/796fe880c9.mp4?token=U-4Vl_l04eqVz4LlxngAnHUuRh2IKuE84Z_U6sIsPMRDhkJcZLNe_YaadcruzhPhkQU-VAqj5cniZaE1UR329hAWkXOV9dolnxIztHo7cv4v8GXU8jRfxcPxalbK3zNWo-5nz7Z36OGFXRSvdi5zDqm5UpvNmz603INOgTu65tZzkv80EP576au8Q26ysOufEiGAk8RXV7CU1zOoH5uxwS5fJQ4tMOheWSBvxosHcqfVn8yVC3PSPW3UglhNNAKPxNWtOqTScyDvVXZcSBFOP7JtNDngq0VdDftncB52S7nErbUOqVjbGwQABdqcyria3xTIk7RvJ1_IzsQr7fiBPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مدينة ذوباب تحت سيطرة أبطال القوات المسلحة اليمنية.</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/naya_foriraq/92651" target="_blank">📅 00:56 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92650">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🇾🇪
القوات المسلحة اليمنية تؤكد استمرار سيطرتها الكاملة على مدينة المخا وتنفي أكاذيب الإعلام السعودي.</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/naya_foriraq/92650" target="_blank">📅 00:51 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92649">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/224b355f7a.mp4?token=sfbmqDY43MI7NAXoRV2mDE-nbH-jZoTOeA-7XU0RONX_RCDiSDZoFxY4t6y9YA8LpezOgMj7MKt67ZdtzZB2tAn2Wp5GVkYxzBxHKxBh3ZrjftAGPG_dCYQmTAPrD8LCmQxlZ1dfEd1S8IMtNVnERhEeZCy-kgV6acC3vw8N8ygl-3FN5opMtba6m1ZVb6SKcYsR_rP0TZ8-nlQ3N-30LFTvxE7yrLDqYhZnly3uJennN-4yrZg1kAZXnoq1_mVzUDwKOfXKY3vmmnRKxTs4lOhQxMN_aoYMmEQg2hNG9fu9MFT79_ymTY5jpnU_gYxblWi1LqvTmrSX6GbCDgIu42xhPnkhEkv7fSdn3huoAd-mgorFyBcIMcD47XEHzuIBzzWdUURbvAKX-aKF49_aSt-CGuB-fD2vzHkKhthsyhvyC5y7gL9gb8RbwaqUJaKnlcj2Crb628Uym6f5wAPiIoojIbo9OkGwtLSoNx64_haAkj9CGa_X2L1qBbqpmxpNovf3IkHqO8mNL8lYwhVWV9Bo3HiPLd5YS88cmphxYjlr8LtNe45LSGSkDaOQXt3EYW72M8g4u_yGi6r7wT8oAKcikbs-uydoSqUIrCGurphrt2QWKuiMNB3VMsI7CzzWDFNHYTfi2pAS4S8GsWRBPfsBJJ1Dtdt1KkRTlEKNAKI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/224b355f7a.mp4?token=sfbmqDY43MI7NAXoRV2mDE-nbH-jZoTOeA-7XU0RONX_RCDiSDZoFxY4t6y9YA8LpezOgMj7MKt67ZdtzZB2tAn2Wp5GVkYxzBxHKxBh3ZrjftAGPG_dCYQmTAPrD8LCmQxlZ1dfEd1S8IMtNVnERhEeZCy-kgV6acC3vw8N8ygl-3FN5opMtba6m1ZVb6SKcYsR_rP0TZ8-nlQ3N-30LFTvxE7yrLDqYhZnly3uJennN-4yrZg1kAZXnoq1_mVzUDwKOfXKY3vmmnRKxTs4lOhQxMN_aoYMmEQg2hNG9fu9MFT79_ymTY5jpnU_gYxblWi1LqvTmrSX6GbCDgIu42xhPnkhEkv7fSdn3huoAd-mgorFyBcIMcD47XEHzuIBzzWdUURbvAKX-aKF49_aSt-CGuB-fD2vzHkKhthsyhvyC5y7gL9gb8RbwaqUJaKnlcj2Crb628Uym6f5wAPiIoojIbo9OkGwtLSoNx64_haAkj9CGa_X2L1qBbqpmxpNovf3IkHqO8mNL8lYwhVWV9Bo3HiPLd5YS88cmphxYjlr8LtNe45LSGSkDaOQXt3EYW72M8g4u_yGi6r7wT8oAKcikbs-uydoSqUIrCGurphrt2QWKuiMNB3VMsI7CzzWDFNHYTfi2pAS4S8GsWRBPfsBJJ1Dtdt1KkRTlEKNAKI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رشقات صاروخية تدك العاصمة السعودية ومطار الرياض يوقف عمليات الهبوط والإقلاع.</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/naya_foriraq/92649" target="_blank">📅 00:41 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92648">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🇾🇪
🇸🇦
بعد دحر مرتزقة السعودية..
القوات المسلحة اليمنية تتمكن من السيطرة على مناطق عليافة وجبل صبران واهجوم قدس والمذاحج في محافظة تعز.</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/naya_foriraq/92648" target="_blank">📅 00:35 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92647">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/870d4d1562.mp4?token=vCvnrw70ZRxYzby87u4dge_oSxFfisO8_YxkDRV23kWTFRcM6opPin3pCvK572qs6S3MQARAtYPfrpOyWePifgp6kVMg_gkcfV7dQYLyx4bCtEs0vDyDSnA-XLpYXE0lQ7Ii7MTLvcEl2KEjrv_HGaqbxQcBMQazad_NGsD69KjkMHGBnHkoTDUaEPuDPtM2wLWIbce8c9lhlamtDX68rR4eI6HzADd8FA6ZRol2drU-PL-6cCfR0brvityZ5DTwf2e995gcN7fd76cx7WA9PO6-xyTAysnAbhaNkpemNrHi0kbbGwocvvpKB575fZGYLpSomiMEdiH_KVfhAVnv5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/870d4d1562.mp4?token=vCvnrw70ZRxYzby87u4dge_oSxFfisO8_YxkDRV23kWTFRcM6opPin3pCvK572qs6S3MQARAtYPfrpOyWePifgp6kVMg_gkcfV7dQYLyx4bCtEs0vDyDSnA-XLpYXE0lQ7Ii7MTLvcEl2KEjrv_HGaqbxQcBMQazad_NGsD69KjkMHGBnHkoTDUaEPuDPtM2wLWIbce8c9lhlamtDX68rR4eI6HzADd8FA6ZRol2drU-PL-6cCfR0brvityZ5DTwf2e995gcN7fd76cx7WA9PO6-xyTAysnAbhaNkpemNrHi0kbbGwocvvpKB575fZGYLpSomiMEdiH_KVfhAVnv5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇾🇪
القوات المسلحة اليمنية تؤكد استمرار سيطرتها الكاملة على مدينة المخا وتنفي أكاذيب الإعلام السعودي.</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/naya_foriraq/92647" target="_blank">📅 00:34 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92646">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🇺🇸
الجيش الأمريكي:
في 5 أكتوبر، قامت قوات القيادة المركزية الأمريكية (CENTCOM) بتغيير مسار السفينة التجارية رقم 130 في الشرق الأوسط، وذلك في إطار التطبيق الصارم للحصار البحري الأمريكي المستمر المفروض على إيران.</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/naya_foriraq/92646" target="_blank">📅 00:26 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92645">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🔴
الرصد اليومي لطلعات العدو الجوية التي يخرق بها السيادة العراقية.
الرصد بتأريخ
4
-10-2026</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/naya_foriraq/92645" target="_blank">📅 00:23 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92644">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">رشقات صاروخية تدك العاصمة السعودية ومطار الرياض يوقف عمليات الهبوط والإقلاع.</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/naya_foriraq/92644" target="_blank">📅 00:14 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92643">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r8Ckxom4oT4nBl0QFvvADeqHFtLslpW_zsbcCJ_SCsRfneSYlbIOv424AMEy27fVUN_8W9ELzFLyzjnekVq_2SgCAG6CFXw76CT6T7-JGWeyJkkVhEwse3CQ96HTEBpI1aVgt-aXQ92GjhzpFps5J_M5pfaxRNqgcZgOw74hLlh9jtN7S7tEZGCCS0MSdmJRKEerEucu3reM2UeB_8aLCMB-iZFaF9vkprNG0mKDCbY1rMuiBbKWHt0LQR_dJMn1vq696lKPDtMTvWfyu227BRV7HTiUnMnmV5H-SKzN2Hik5WQGp6IxLsZOs5iS5TEfngZvwk3yVr3BD3Mvy41VEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انفجارات تهز الرياض</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/naya_foriraq/92643" target="_blank">📅 00:08 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92642">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">انفجارات تهز الرياض</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/naya_foriraq/92642" target="_blank">📅 00:08 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92641">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🇸🇦
🇾🇪
عدوان سعودي على ميناء الصليف بمحافظة الحديدة.</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/naya_foriraq/92641" target="_blank">📅 00:04 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92640">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🇾🇪
بيان القوات المسلحة اليمنية بشأن تنفيذ ثلاث عمليات عسكرية نوعية استهدفت مطار الملك خالد في الرياض ومصفاةَ أرامكو في رابغ ومطار أبها وقاعدة خميس مشيط ومعسكر عاكفة في عسير ومواقع حساسة أخرى في نجران وجيزان.
بيانٌ صادرٌ عن القواتِ المسلحةِ اليمنيةِ
بسمِ اللهِ الرحمنِ الرحيمِ
قالَ تعالى: {فَمَنِ اعْتَدَى عَلَيْكُمْ فَاعْتَدُوا عَلَيْهِ بِمِثْلِ مَا اعْتَدَى عَلَيْكُمْ} صدقَ اللهُ العظيم
في إطارِ الردِّ على العدوانِ السعوديِّ على بلدِنا والذي شنَّ خلالَ الـ24 ساعةً الماضيةَ 60 غارةً جويةً وصاروخًا مستهدفًا بها العاصمةَ صنعاءَ ومحافظاتِ الجوفَ وتعزَ وحجةَ وصعدةَ ومأربَ، وخلَّفت شهداءَ وجرحى من المدنيينَ بينهم نساءٌ وأطفالٌ.
ليبلغَ إجمالي غاراتِ العدوِّ السعوديِّ على بلدِنا منذُ بدءِ التصعيدِ 1576 غارةً جويةً وصاروخًا
نفذتِ القواتُ المسلحةُ اليمنيةُ ثلاثَ عملياتٍ عسكريةٍ نوعيةٍ وذلك بعددٍ كبيرٍ من الصواريخِ الباليستيةِ والمجنحةِ والطائراتِ المسيرةِ الأولى استهدفت مطارَ الملكِ خالدٍ في الرياضِ وكانتِ الإصابةُ دقيقةً ومباشرةً بفضلِ اللهِ وأدت إلى تعطلِ حركةِ الملاحةِ فيهِ.
والثانيةُ استهدفتْ مصفاةَ أرامكو في رابغَ، وكانتِ الإصابةُ دقيقةً ومباشرةً وأدتِ العمليةُ إلى اشتعالِ النيرانِ في الموقعِ المستهدفِ.
فيما استهدفتِ العمليةُ الثالثةُ مطارَ أبها وقاعدةَ خميسِ مشيط ومعسكرَ عاكفة في عسير ومواقعَ حساسةً أخرى في نجرانَ وجيزانَ وكانتِ الإصاباتُ دقيقةً بفضلِ اللهِ.
تحذرُ القواتُ المسلحةُ كلَّ شركاتِ الطيرانِ العالميةِ التي تستخدمُ الأجواءَ السعوديةِ من مواصلةِ استمرارِ رحلاتِها الجويةِ لأنها أصبحتْ مسرحاً لعملياتِنا باستثناءِ الأجواءِ المقدسةِ لمكةَ المكرمةِ والمدينةِ المنورةِ ونخلي مسؤوليتَنا من تبعاتِ تجاهلِ هذا التحذيرِ.
تؤكد القواتُ المسلحةُ لكافةَ أبناءِ شعبِنا المؤمنِ العزيزِ الكريمِ الصامدِ المجاهدِ أنها تمتلكُ من القدراتِ والإمكاناتِ ما يجعلُها بعونِ اللهِ تعالى وبالتوكلِ عليهِ قادرةً على مواجهةِ هذا التصعيدِ العدوانيِّ.. وأنها أعدتِ العدةَ لمثلِ هذا اليومِ .. فالقولُ لميدانِ المعركةِ والكلمةُ لساحاتِ البطولةِ والجهادِ.
واللهُ حسبُنا ونعمَ الوكيلُ، نعمَ المولى ونعمَ النصيرُ.</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/naya_foriraq/92640" target="_blank">📅 23:40 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92639">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🇸🇦
🇾🇪
عدوان سعودي على جزيرة كمران ومديرية الصليف في الحديدة.</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/naya_foriraq/92639" target="_blank">📅 23:32 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92638">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🇮🇶
حدث امني خطير في الدجيل جنوب محافظة صلاح الدين
العثور على عبوة ناسفة وكدس جاهز للاستخدام يعود لعصابات داعش الارهابية .</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/naya_foriraq/92638" target="_blank">📅 23:18 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92637">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">انفجارات اخرى في مضيق هرمز</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/naya_foriraq/92637" target="_blank">📅 23:13 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92636">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🇮🇷
هجوم صاروخي يطال ناقلة نفط في مضيق هرمز، والنيران تشتعل فيها.</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/naya_foriraq/92636" target="_blank">📅 23:13 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92635">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🇺🇸
‏ترامب: إذا امتلكت إيران طائرات قتالية بدون طيار في المملكة المتحدة، فسوف تعاني كثيراً، أعرف الأشخاص الذين وجهوا التهديد في المملكة المتحدة.</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/naya_foriraq/92635" target="_blank">📅 23:03 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92634">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🇺🇸
‏ترامب: الأمور ستسير على ما يرام بالنسبة للسعوديين والحوثيين.</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/naya_foriraq/92634" target="_blank">📅 22:57 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92633">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5db87f3af3.mp4?token=ZbCB4lZkR4eTixIjUuo3K_8YSE00yX4EbftsJO8wRZa9i1IKmkgkD_-0KW4uTAy9zbvpmKFtPbeATQWj9g2XL9NZHs7JQkP0ElAMq4zp_2NO4_eZRN0V9FZfbs1j4rTXe0CRThDGH96Dixsy-wuf_Oi9yY8xJKAc5xTN-6QyAJHT26p2gGUEDaJ59iy3cHBLExMNL5ic_ZeMM2wq6WtJ14l4bNMO8oA3GJDijaOpHtKsTfzHC5UErr8ftN2sRT7hhlOkswk09VzsxSxq7uKUmz52VoU-AmymQIySZTgSm8in4-tog1h-byPXK_OosmilPFzyQQxRnlHKaCZazIYxOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5db87f3af3.mp4?token=ZbCB4lZkR4eTixIjUuo3K_8YSE00yX4EbftsJO8wRZa9i1IKmkgkD_-0KW4uTAy9zbvpmKFtPbeATQWj9g2XL9NZHs7JQkP0ElAMq4zp_2NO4_eZRN0V9FZfbs1j4rTXe0CRThDGH96Dixsy-wuf_Oi9yY8xJKAc5xTN-6QyAJHT26p2gGUEDaJ59iy3cHBLExMNL5ic_ZeMM2wq6WtJ14l4bNMO8oA3GJDijaOpHtKsTfzHC5UErr8ftN2sRT7hhlOkswk09VzsxSxq7uKUmz52VoU-AmymQIySZTgSm8in4-tog1h-byPXK_OosmilPFzyQQxRnlHKaCZazIYxOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
🇮🇷
‏ترامب بشأن إيران: منفتح دائماً على المحادثات المباشرة.</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/naya_foriraq/92633" target="_blank">📅 22:56 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92632">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65c3d4d161.mp4?token=RuFr0nJc8uuQEPXj78NZ1kTa76At6Yl_pZR7lKiNHwXRQwcuSKbl2N1s1N1ymDUbtmLHsuxhNzFdqJ_Nz8Tv4Nq0Sc8zcChEx2xsKQ3QtP6f0u2Dnathpf4BmF-EAcVqhcTVRfkHdPssJjVosLHAodaahGF-e9xo5ASzvwtBDhwdWNAQ5uhRndW_JSgtItBe7fPTIy_NRn5rKjlsPMOim9npvF5-1QvfIlej0yz9Q3Ez2iBXB6dUbTcwlV2neYL-oqiFMZysivLoZvQQ3zjKwawmEAHmtTUUFA93lJuo1E9VKzTWVNZCgY0rhhzWSe0ZxahktZ7HcOBwr_S1rjI4wr9arPOnqZBIQj9rWR_ULzPomNB9zBcjdwawFYhHYS2YEj7TCTPqSluLPb0-htJMNKvEcvh1eFs0KiXt6KKFlmRjJ0j_D_smkjjoM6Kiu6XgLJRVIbOqxQqrOxudl2elTfKW0O9wwJpIh5qZTibIp84jKOoCpCBwrdbSl_rn6dMjIe4r5e54i6ru4TuhIH_lZ2sF80XVpb1fMiP8xfNUBUv1wFUlX23HRzfkDdwxkytluNwnfGd4Tq5RJ-qgsjrBCH_MrKcM1ZBvAOPFzS_FIQfdJm516oLVhJp2GmQrwYCinCedR0pKy5sfW8uTrkUk6V-YOodvkEQuJf2j9yIozWc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65c3d4d161.mp4?token=RuFr0nJc8uuQEPXj78NZ1kTa76At6Yl_pZR7lKiNHwXRQwcuSKbl2N1s1N1ymDUbtmLHsuxhNzFdqJ_Nz8Tv4Nq0Sc8zcChEx2xsKQ3QtP6f0u2Dnathpf4BmF-EAcVqhcTVRfkHdPssJjVosLHAodaahGF-e9xo5ASzvwtBDhwdWNAQ5uhRndW_JSgtItBe7fPTIy_NRn5rKjlsPMOim9npvF5-1QvfIlej0yz9Q3Ez2iBXB6dUbTcwlV2neYL-oqiFMZysivLoZvQQ3zjKwawmEAHmtTUUFA93lJuo1E9VKzTWVNZCgY0rhhzWSe0ZxahktZ7HcOBwr_S1rjI4wr9arPOnqZBIQj9rWR_ULzPomNB9zBcjdwawFYhHYS2YEj7TCTPqSluLPb0-htJMNKvEcvh1eFs0KiXt6KKFlmRjJ0j_D_smkjjoM6Kiu6XgLJRVIbOqxQqrOxudl2elTfKW0O9wwJpIh5qZTibIp84jKOoCpCBwrdbSl_rn6dMjIe4r5e54i6ru4TuhIH_lZ2sF80XVpb1fMiP8xfNUBUv1wFUlX23HRzfkDdwxkytluNwnfGd4Tq5RJ-qgsjrBCH_MrKcM1ZBvAOPFzS_FIQfdJm516oLVhJp2GmQrwYCinCedR0pKy5sfW8uTrkUk6V-YOodvkEQuJf2j9yIozWc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
🇷🇺
ترامب حول مصافي النفط الروسية:
المشكلة تكمن في نقص المصافي. لدينا كميات هائلة من النفط تتدفق من مضيق هرمز. ونعاني من نقص في المصافي بسبب الحرب.</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/naya_foriraq/92632" target="_blank">📅 22:53 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92631">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🇺🇸
🇮🇷
‏ترامب بشأن إيران:
منفتح دائماً على المحادثات المباشرة.</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/naya_foriraq/92631" target="_blank">📅 22:53 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92630">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🇮🇶
ثلاثة اصابات بإطلاقات نارية لمنتسبي جهاز الأمن الوطني نتيجة عبث خاطئ بالسلاح.</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/naya_foriraq/92630" target="_blank">📅 22:33 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92629">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/68d3b3ad3b.mp4?token=BvamllLJA3PDiQrJozoeQUjwxgEIHxgR0TJEhN72-F69f1xHQ_6RbuHwprqfEQ-rrm5xUIwY0J3a5254G2Rs8-ds1qZEKdvqtcsKnF7tymqfxnxayh7t4WlVEIJSiwNVFHXQa-ZGWrd2a-7VhgX52HnnO31Nwl0uKPDnfIpQdV88tk-HzYx0MLdWqnlUSgXuPl6wlEjhCCM8JPFknP4062X6Y6fbMK2h2Bwitavpg7Mcdxfpt8VMQ85U2_xPOu5kwxSo-73jSiodWD4gbEJ_Ta8DlP5Gj8fp89Hr3bv5FoSOxmbcCMQx--wfvZ2qJEBpOF2x9Xjf5oycDm_bn3FZ0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/68d3b3ad3b.mp4?token=BvamllLJA3PDiQrJozoeQUjwxgEIHxgR0TJEhN72-F69f1xHQ_6RbuHwprqfEQ-rrm5xUIwY0J3a5254G2Rs8-ds1qZEKdvqtcsKnF7tymqfxnxayh7t4WlVEIJSiwNVFHXQa-ZGWrd2a-7VhgX52HnnO31Nwl0uKPDnfIpQdV88tk-HzYx0MLdWqnlUSgXuPl6wlEjhCCM8JPFknP4062X6Y6fbMK2h2Bwitavpg7Mcdxfpt8VMQ85U2_xPOu5kwxSo-73jSiodWD4gbEJ_Ta8DlP5Gj8fp89Hr3bv5FoSOxmbcCMQx--wfvZ2qJEBpOF2x9Xjf5oycDm_bn3FZ0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
العثور على ملاحظة تشير إلى وجود مواد متفجرة على متن طائرة الركاب AJET 4180 المتجهة من أنقرة إلى شانلي أورفا، والتي هبطت بسلام في مطار شانلي أورفا.</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/naya_foriraq/92629" target="_blank">📅 22:31 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92628">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4826619499.mp4?token=gBwF15902WybgL8LvwIElo3nVzv9jYaz3S8a6htx6MB7gUxwi5I6fZQTIRuxbU-f36WbqJvgDR9HtZCqQIEzKAimg0xB6OrCiw6HSn5z4BIx_O710dBeI8103YoYK2oy8nqV4TqY0uJ9Wrm13QfJ5RnoNPSk4mvSxa_ipm20zNkMLTJeRWstTwb-nNhINKS-JSfUIc4JW9MD5IZq5IvWu6_QDrdRlzM4KTBI4J75Jg66wwxRJW9h-wa1w4epJ4KdhGcHh92JL4gPb3H3uGd8z2cTla67k3T8YBaoU1xlaG4fINYCsF4SuBvKdY_cEgOdOSc_Ev3kN1YLosUjp2JyeQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4826619499.mp4?token=gBwF15902WybgL8LvwIElo3nVzv9jYaz3S8a6htx6MB7gUxwi5I6fZQTIRuxbU-f36WbqJvgDR9HtZCqQIEzKAimg0xB6OrCiw6HSn5z4BIx_O710dBeI8103YoYK2oy8nqV4TqY0uJ9Wrm13QfJ5RnoNPSk4mvSxa_ipm20zNkMLTJeRWstTwb-nNhINKS-JSfUIc4JW9MD5IZq5IvWu6_QDrdRlzM4KTBI4J75Jg66wwxRJW9h-wa1w4epJ4KdhGcHh92JL4gPb3H3uGd8z2cTla67k3T8YBaoU1xlaG4fINYCsF4SuBvKdY_cEgOdOSc_Ev3kN1YLosUjp2JyeQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇾🇪
القوات المسلحة اليمنية من وسط مدينة المخا تنفي الاشاعات السعودية بخصوص سيطرة السعودية على المخا.</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/naya_foriraq/92628" target="_blank">📅 22:19 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92627">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P3J9P144Jz_cj_7tsILDXSxvE3GWUy1umBiUP2uWKTBO1zSpg6AKnBAbzgt7d7xY6ZEuwJeZWVf7DPKyKChaOjmLAxFZm86-mA9RBxm0FwSKbTeGoo3DdFbL2K97yWG3lg07ksH0nte4kYWfZhBYpY6z9olcf1Z5R1OCYbZ76R73csaPft9SmXomrEPPhdXyKC52Znw1CxeIc86J63VHU-SdgCM2vhOT02J2xuDscbSP7nhD-tLX3bxO4HKU7eBE6W_7pK2gTFnhI3x-Iqc8aoeC5rJE9jeELwdcaALPA5dlDzm_J-HgfPzUD4w0s_KYthAIBXCJGBWOMn-1sav6jA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇸🇦
وزارة الدفاع السعودية: اجتماع حلف مكة يؤكد تفعيل الردع الجماعي ضد هجمات اليمنية وضد كل من يقف وراءها.</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/naya_foriraq/92627" target="_blank">📅 21:40 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92626">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🇸🇦
وزارة الدفاع السعودية: اجتماع حلف مكة يؤكد تفعيل الردع الجماعي ضد هجمات اليمنية وضد كل من يقف وراءها.</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/naya_foriraq/92626" target="_blank">📅 21:37 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92625">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🇸🇦
وزارة الدفاع السعودية:
اجتماع حلف مكة يؤكد تفعيل الردع الجماعي ضد هجمات اليمنية وضد كل من يقف وراءها.</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/naya_foriraq/92625" target="_blank">📅 21:35 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92624">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jZ_bQADMihBNFhLV-qy0mrUlj9Hn8U8UjuaDzrcQWjfez2N8S-yQtTf9sEOf5BIuFFUXjkIalMIKkTEVWUvg-7wovirc6giEWCtUUGktEq9NcEjSHcM7PyZzIxnHm01F30ABKO9kVRxSUbaQr2NUrSOVS7FRz3KnWwRk2bbjRJMXZ6a-gI7CTgW1C1bGnFUnunS-KYcgc3DNwquWnXcQL7HobWwDhtQpeTtPpZ8fPExZtw9ImF6Zru_HnNSGAaUlAmRo0mOcx5XZI55xdQ_K265fbpS2aaTuMOyC2Tu25hHnCu63jZWGEBRMoYIUM9H30kIH1TXiospiyLIhsaoXrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
هجوم صاروخي يطال ناقلة نفط في مضيق هرمز، والنيران تشتعل فيها.</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/naya_foriraq/92624" target="_blank">📅 21:23 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92623">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🇮🇶
أنباء أولية عن تعرض في محافظة كركوك على اللواء التاسع بالشرطة الاتحادية بمنطقة تقاطع الدناديش.</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/naya_foriraq/92623" target="_blank">📅 21:11 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92622">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a67504163.mp4?token=rLYqZR-igvx24YLromZw8oNb_MbbWjS0gw9sIAUZ9iaZ3pumSJRuKH2PHcZjezajc43helIk4YRJTS7DtkkEG8pfQvuRg_WTa9zzwRj8-tfM6B-xrR_0ygoT71uFoO3J_icZXOYDIEncg9kfStCSOJhHERukiuuFFcuMZEJrv85sE83TiroUhwuR94b9VGDwQ0hUU4363Xc2CJkZZ6nPbVctC7vVMiA9weGW7yp4n3my_3gcNvRjJbuZfjlPCG6H3K1bPq8MKlY5FGNxN5WLGKxBtZZ4tGRJ8sL60Zb2kEMrQvnH6vAhU-cj7Q1d-COZRIse71t2cf7uS9oq5llEHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a67504163.mp4?token=rLYqZR-igvx24YLromZw8oNb_MbbWjS0gw9sIAUZ9iaZ3pumSJRuKH2PHcZjezajc43helIk4YRJTS7DtkkEG8pfQvuRg_WTa9zzwRj8-tfM6B-xrR_0ygoT71uFoO3J_icZXOYDIEncg9kfStCSOJhHERukiuuFFcuMZEJrv85sE83TiroUhwuR94b9VGDwQ0hUU4363Xc2CJkZZ6nPbVctC7vVMiA9weGW7yp4n3my_3gcNvRjJbuZfjlPCG6H3K1bPq8MKlY5FGNxN5WLGKxBtZZ4tGRJ8sL60Zb2kEMrQvnH6vAhU-cj7Q1d-COZRIse71t2cf7uS9oq5llEHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇾🇪
القوات اليمنية من مدينة ذوباب تكذب روايات السعودية.</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/naya_foriraq/92622" target="_blank">📅 21:03 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92621">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🇮🇶
أنباء أولية عن تعرض في محافظة كركوك على اللواء التاسع بالشرطة الاتحادية بمنطقة تقاطع الدناديش.</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/naya_foriraq/92621" target="_blank">📅 21:01 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92620">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">السفارة الامريكية تحذر : ‏المملكة العربية السعودية: نظراً للوضع الأمني ​​الراهن في المملكة العربية السعودية واحتمالية وقوع هجمات جوية بطائرات مسيرة أو صواريخ عليها، تحثّ البعثة الأمريكية جميع المواطنين الأمريكيين بشدة على توخي الحذر واتباع إرشادات التنبيهات الوطنية الصادرة عن الدفاع المدني السعودي. للمزيد، تفضلوا بزيارة</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/naya_foriraq/92620" target="_blank">📅 20:55 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92619">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d1sKXUmN_M3x8si622Ue4fz-oPeh10Ue-11iKI0mujFBktzmnWGbiIverh2xCqNKkD9XDrGgDgdYYuJEnmDmlJL0zXmUjLWGRljuN8e1oWOKx5IJijhfYVOKQR6_3MaDkuo_aWXOGRrWlgJ7PZDDad68UhGxP3BOvcfJJhLEen0KIplgc0yag2py6QQ9UJTwEs0QjTOEBub_c8L5pEUysRAbR01g0A1UeWgqoRwFgYmn112xbMMVH60OK5nMA44Gy_m3nqW_rfsyzxjV_Btlb-9NOOyrK2MXou95ss1mMPqQwyf5ysMDwqJxmi5gIu8ktCDAbbB_XWmAKI1olqbgCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇾🇪
حزام الاسد:
لا يوجد في باب المندب وذوباب والمخا إلا رجال القوات المسلحة اليمنية.</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/naya_foriraq/92619" target="_blank">📅 20:49 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92618">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64aab362af.mp4?token=ZXp8H3co9-Lpd6UlXQU4PMWspTVatRH11pKV9ffnn1gd0Z2TcFhKz4qYDDGvbOHckpVDtxl2JiVI4gGO_8kOyDO-7LM-uu9BhQ3UuBibIC8TD3n-qDOQqidLL1qeZDfkFUcHlSdvr56NfIbDqZLjMp6tWTE6uRLxb3lY7oe-KHRcNe5yNU3P7GuvfmD91IiRvxDcE-9RGWHMxfTkXdFbguPL_lAdk_sbNoKCNjP9QVUC9VE-6VOmFzTaTuGcqlt3NZE7YJUzUw2lgRPdjwLEIRbYh-DU2-_yUCa4KohhcVh097tYmSXZJmajXBIbbEgxi-XssPFRi2UkDCtYUZFkihw1xXsg9W-haXWgFr741c_fUvn4Q8k47K8GaUNCKifSsRxM6bu5d4SQCRG9uTSm3hllwWK05fOwfPxxBuWr4DUzT1Q64nnx-_SZYhhiMSRx9ikB4HLJS7zv1CId1MAH6_ovFeVt6OfXDi2xq9wV8YuNAblfW3SR1x-heUFbafneeMdusTJI43zgf2ryN6AOXoFGsZc1zSyDXBoJV_22hkBLMgS-fe7U4BhCkQjWkJTS3yIOqjxNiKPy-RJO5vllzJfSIKMN9w0VICZrZIEVubgZtGWOLu4-lEj7DbfNSEX0oOeV5lzsYYvHP9734jFmRbMWosGd_vD_X0khqKKh7sw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64aab362af.mp4?token=ZXp8H3co9-Lpd6UlXQU4PMWspTVatRH11pKV9ffnn1gd0Z2TcFhKz4qYDDGvbOHckpVDtxl2JiVI4gGO_8kOyDO-7LM-uu9BhQ3UuBibIC8TD3n-qDOQqidLL1qeZDfkFUcHlSdvr56NfIbDqZLjMp6tWTE6uRLxb3lY7oe-KHRcNe5yNU3P7GuvfmD91IiRvxDcE-9RGWHMxfTkXdFbguPL_lAdk_sbNoKCNjP9QVUC9VE-6VOmFzTaTuGcqlt3NZE7YJUzUw2lgRPdjwLEIRbYh-DU2-_yUCa4KohhcVh097tYmSXZJmajXBIbbEgxi-XssPFRi2UkDCtYUZFkihw1xXsg9W-haXWgFr741c_fUvn4Q8k47K8GaUNCKifSsRxM6bu5d4SQCRG9uTSm3hllwWK05fOwfPxxBuWr4DUzT1Q64nnx-_SZYhhiMSRx9ikB4HLJS7zv1CId1MAH6_ovFeVt6OfXDi2xq9wV8YuNAblfW3SR1x-heUFbafneeMdusTJI43zgf2ryN6AOXoFGsZc1zSyDXBoJV_22hkBLMgS-fe7U4BhCkQjWkJTS3yIOqjxNiKPy-RJO5vllzJfSIKMN9w0VICZrZIEVubgZtGWOLu4-lEj7DbfNSEX0oOeV5lzsYYvHP9734jFmRbMWosGd_vD_X0khqKKh7sw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇾🇪
القوات اليمنية من مدينة ذوباب تكذب روايات السعودية.</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/naya_foriraq/92618" target="_blank">📅 20:42 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92617">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🇾🇪
مشاهد أولية من وصول القوات المسلحة اليمنية إلى منزل الغوي الخائن للوطن رشاد العليمي - 05 أكتوبر 2026م.</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/naya_foriraq/92617" target="_blank">📅 20:25 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92616">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">اصوات انفجارات في الرياض</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/naya_foriraq/92616" target="_blank">📅 20:19 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92615">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/naya_foriraq/92615" target="_blank">📅 20:18 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92614">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">اصوات انفجارات في الرياض</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/naya_foriraq/92614" target="_blank">📅 20:18 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92613">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/10dfda8f58.mp4?token=EhMu_7z5lnPkJxaicrpMbh3Ek-6hZnrcF-MGKlc_LVgkv23PIstU1g8ua8gKxSaQuG6_zkLVQmuB-8o7pDO5appYe6cwGKPErACeaVhQzFIRhLsz7EFA2MrBMNdRo5X8pLzo2zKTpsPU6CT4uM6eXBVnrO2ag2jD28-XJCP-FCVBiF3PYfq89ccutMVy1oVROUNsO0vNUJSlETwUDTO5f7sL6m_POj8O_4GuCVLWEIq_nlO9-kh3VK2m7kOE0eLS5_QxvbuZKzb0lfPv0JgWW97VWWVSUfnPZnIgOTEGHRW4HNgauFxMva8JJhA_He0BZfEWHiJuMhCe676p4iEqZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/10dfda8f58.mp4?token=EhMu_7z5lnPkJxaicrpMbh3Ek-6hZnrcF-MGKlc_LVgkv23PIstU1g8ua8gKxSaQuG6_zkLVQmuB-8o7pDO5appYe6cwGKPErACeaVhQzFIRhLsz7EFA2MrBMNdRo5X8pLzo2zKTpsPU6CT4uM6eXBVnrO2ag2jD28-XJCP-FCVBiF3PYfq89ccutMVy1oVROUNsO0vNUJSlETwUDTO5f7sL6m_POj8O_4GuCVLWEIq_nlO9-kh3VK2m7kOE0eLS5_QxvbuZKzb0lfPv0JgWW97VWWVSUfnPZnIgOTEGHRW4HNgauFxMva8JJhA_He0BZfEWHiJuMhCe676p4iEqZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
الاعلام الاجنبي يتداول فيديو لاشتعال غرفة القيادة بسفينة شحن في مضيق هرمز.</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/naya_foriraq/92613" target="_blank">📅 20:09 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92612">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I-b9DP1NNpkhzr7zMu63GDmhHgjwdCgk2B-z90D3kBQ9mImj_3Of87DDjfwn2fOdTluyKJtDKKp6LWt2OQ0z0c9s0DEk2M8hK0N149f3EdGTgejneFWP7JE8NBRgBPXWF6TrTkoFGGGj9ywRX4zhM8EkgGizG5YGHk5_upXoSl-FLfLNYfJ_nZLMhUhLmO_Ya64EuufoSw197Macn-loVZHMYjGznZ2AuLKLUexaMsEWHRUud0E4Avci7c-wAMOfTSoz088EeWT_7YSuh6SzvQoDvFGD6Isa9-cU6P-1llSRBdr3wsALrjNd4pjF3bdyoYoA_dbcgK6CQVsMwbc93A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامب
:
‏لم يعد مضيق هرمز هو ما يرفع أسعار البنزين، لأن أعداداً قياسية من البراميل تُصدّر منه الآن بشكل شبه يومي، بل كلمة "مصافي التكرير"، حيث تُفجّر أوكرانيا مصافي التكرير الروسية، وتُغلق مصافينا في الولايات الديمقراطية، مثل كاليفورنيا، على يد الديمقراطيين. الرئيس دونالد جيه. ترامب.</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/naya_foriraq/92612" target="_blank">📅 20:04 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92611">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c814447da4.mp4?token=PbVQN5ImBdRehdDgiKWcdbmrP9Ic-94CIi8vBIpnGPkCdmIag3ZGs7X64UVb_ihbZluZmJoHxq31PvdIvRQvRk91XauuUNKEG-czcZXvsn3TGaCwyf1251AX6WB081uv3OQliMnivEaYPiGX_DPeV9Ga7_Qcm-lMqVf27u7B2z2xMXLgUNFW_AUArZV2w9wveFAvMszTAchyqRZ1NbfGsyug5eouxAiaDtF3ue2EXkGpcsAySHO0Qt6mTR1_VYyVwXZqJoMLWMfyetsXOYywYTXnf8lWMzboTfj2dlFjVk-HuA_weYVVuxEDO1BJ6PKvnboleeRDqlbJ8BjDyo_3Tg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c814447da4.mp4?token=PbVQN5ImBdRehdDgiKWcdbmrP9Ic-94CIi8vBIpnGPkCdmIag3ZGs7X64UVb_ihbZluZmJoHxq31PvdIvRQvRk91XauuUNKEG-czcZXvsn3TGaCwyf1251AX6WB081uv3OQliMnivEaYPiGX_DPeV9Ga7_Qcm-lMqVf27u7B2z2xMXLgUNFW_AUArZV2w9wveFAvMszTAchyqRZ1NbfGsyug5eouxAiaDtF3ue2EXkGpcsAySHO0Qt6mTR1_VYyVwXZqJoMLWMfyetsXOYywYTXnf8lWMzboTfj2dlFjVk-HuA_weYVVuxEDO1BJ6PKvnboleeRDqlbJ8BjDyo_3Tg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇾🇪
استمرار الانفجارات في عدن وعدة مسيرات تسقط بشكل مباشر على اهدافها.</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/naya_foriraq/92611" target="_blank">📅 19:53 · 13 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
