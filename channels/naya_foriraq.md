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
<img src="https://cdn4.telesco.pe/file/QxZbwXXNeCBFvbuyWenAKyN9JyRxVk26L8PFhBRc-8LpVMUA57E9mORtsWLNoEvF9MRMVKH827V63AGFDexNKslURKAKGvLJoWYErF1NOIiq7-dKzPR6nwFbwzIVJMe1otcqwDPQr7gbUpml3R-g6wi2n4hkjvY1cO6lmdexow2hCeZI_de641Fq-hGck-5wByAA_MHenfzi_XqVyOHHIPTuMOxFZELLAIYu5Fn4kdus7MQ5xLKDWsmkfJFcVd3eEiuuvFi4HX8K0uSJVSuY1Us3NDqfjciUUpzsyG3b6KXIWN4yOu7Lley3PW_M2vPuxAujPIk2kANE53N-Jv_Q_Q.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 267K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-27 05:13:26</div>
<hr>

<div class="tg-post" id="msg-83808">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b56dc8ee8e.mp4?token=fHwZqdt8S3icvRQVWWXhTvLpK4jCp7h6m85WVontGoaGU8cNpMAAwOwwpjYwgxeDat09xEOVSqjyrhtkSmOiFrC4Yby_hYRT8RV3nDoXmWvU4PBBJLsnoCpQG8yjcPsalGCy5nssKwaW3XWERkJ_cObXyIPWNjves6vLWRPy_jZRXEEQOPo3voJTXcFhyb6jtCtFaJZBuo-HUTv-0RbS_sFr8zIoZnMkWPvF3bv2LzNlr3woggOIoCrAMP6IPvcNno33GJt9kihu0q-fNVbNy5gb18LRI3j_4QXVFw7u0kHJRSk3ug3TPsdgDQ2hXO1sKWkV6K0SsM1_CyzIZvSZIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b56dc8ee8e.mp4?token=fHwZqdt8S3icvRQVWWXhTvLpK4jCp7h6m85WVontGoaGU8cNpMAAwOwwpjYwgxeDat09xEOVSqjyrhtkSmOiFrC4Yby_hYRT8RV3nDoXmWvU4PBBJLsnoCpQG8yjcPsalGCy5nssKwaW3XWERkJ_cObXyIPWNjves6vLWRPy_jZRXEEQOPo3voJTXcFhyb6jtCtFaJZBuo-HUTv-0RbS_sFr8zIoZnMkWPvF3bv2LzNlr3woggOIoCrAMP6IPvcNno33GJt9kihu0q-fNVbNy5gb18LRI3j_4QXVFw7u0kHJRSk3ug3TPsdgDQ2hXO1sKWkV6K0SsM1_CyzIZvSZIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
الجيش الأمريكي:
تامبا، فلوريدا - أنهت القوات الأمريكية الليلة السابعة على التوالي من الغارات الجوية على إيران في 17 يوليو/تموز الساعة 9:30 مساءً بتوقيت شرق الولايات المتحدة.
استهدفت القيادة المركزية الأمريكية (سنتكوم) مواقع مراقبة، وبنية تحتية لوجستية عسكرية، ومخازن أسلحة تحت الأرض، وقدرات بحرية. واستخدمت القوات الأمريكية طائرات مقاتلة، وطائرات مسيرة، وسفن حربية، بالإضافة إلى أصول أخرى.
وتواصل سنتكوم محاسبة إيران بتوجيه من القائد الأعلى للقوات المسلحة، مع فرض حصار بحري كامل على الموانئ الإيرانية.
وينتشر أكثر من 50 ألف جندي أمريكي في جميع أنحاء الشرق الأوسط، وهم على أهبة الاستعداد وجاهزون للقتال.</div>
<div class="tg-footer">👁️ 971 · <a href="https://t.me/naya_foriraq/83808" target="_blank">📅 05:09 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83807">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">إطلاق صواريخ من الأراضي الكويتية تجاه الجمهورية الإسلامية الإيرانية</div>
<div class="tg-footer">👁️ 3.07K · <a href="https://t.me/naya_foriraq/83807" target="_blank">📅 05:00 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83806">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">إنفجارات عنيفة و‏دوي صفارات الإنذار في البحرين</div>
<div class="tg-footer">👁️ 3.35K · <a href="https://t.me/naya_foriraq/83806" target="_blank">📅 04:58 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83805">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">إنفجارات عنيفة و‏دوي صفارات الإنذار في البحرين</div>
<div class="tg-footer">👁️ 3.64K · <a href="https://t.me/naya_foriraq/83805" target="_blank">📅 04:57 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83804">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c6d561a6a.mp4?token=RykcnyfxybzqoRRAlESjyi0S3hOA8UVJRlRnHuCvo6yk_S1MnUDypF52HwBVI-PLYTFxWNvzCNHfFUsnDxzm-vUE-I2MtDTWDkW0ABXKX-VUXoPFaYPPcGWBHymbwoXK84ey120EpD_W7xIO9V29iC-Ls8HbafUWMOr4lYTwXGUJR2pFFbT9DhMwJnG4mt4AxlQkzXFcALd4aEhP1XfkS780e2xCU2OZx3DOvqOH1ROgtmO7Pe3isWQzeV3v_x1y1tLvT32WSxtjoTDI3F9byVMizfGtmiZkhk-rkkoANme8f1cZYOyl1gtS_e5CQTMeg35kN1KZTBZvbVM8d45PVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c6d561a6a.mp4?token=RykcnyfxybzqoRRAlESjyi0S3hOA8UVJRlRnHuCvo6yk_S1MnUDypF52HwBVI-PLYTFxWNvzCNHfFUsnDxzm-vUE-I2MtDTWDkW0ABXKX-VUXoPFaYPPcGWBHymbwoXK84ey120EpD_W7xIO9V29iC-Ls8HbafUWMOr4lYTwXGUJR2pFFbT9DhMwJnG4mt4AxlQkzXFcALd4aEhP1XfkS780e2xCU2OZx3DOvqOH1ROgtmO7Pe3isWQzeV3v_x1y1tLvT32WSxtjoTDI3F9byVMizfGtmiZkhk-rkkoANme8f1cZYOyl1gtS_e5CQTMeg35kN1KZTBZvbVM8d45PVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">إطلاق صواريخ من الأراضي الكويتية تجاه الجمهورية الإسلامية الإيرانية</div>
<div class="tg-footer">👁️ 4.07K · <a href="https://t.me/naya_foriraq/83804" target="_blank">📅 04:55 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83803">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">عدوان أمريكي على محيط ميناء جاسك في جنوب إيران.</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/naya_foriraq/83803" target="_blank">📅 04:49 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83802">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/807f084436.mp4?token=f6MyuPFqdd_XwpR58YPJYBF9xEcbhcoCuHl7icCGSL1qM2f9wkZbSUJdQ4h9cTw82J4S9mVkVYWbcYghjJM08Z99bCzwtR7iMni92iDU8fByAG0819aKK3Awxf7gMvEhdAIxGZmQNOhzXU_1nG6Y_jAGQnQfyxd2aTn8-QRUSOOd_RVF_kUUiMlm5GywLmnn6bcQNj3Y8t4TMjVFtUzFO1xtCU7VUCg_wDtolp4Qw-dFwJDqc_kxP-0FwgtSmh6_ZHMTiKlnxNnJEGFPdUeyqDCb8du7DcCR8kEV4VNr2lB1DDpobIrwyWDNpaBVIQrWN-pUMiMRXZYHmkP1BBBajQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/807f084436.mp4?token=f6MyuPFqdd_XwpR58YPJYBF9xEcbhcoCuHl7icCGSL1qM2f9wkZbSUJdQ4h9cTw82J4S9mVkVYWbcYghjJM08Z99bCzwtR7iMni92iDU8fByAG0819aKK3Awxf7gMvEhdAIxGZmQNOhzXU_1nG6Y_jAGQnQfyxd2aTn8-QRUSOOd_RVF_kUUiMlm5GywLmnn6bcQNj3Y8t4TMjVFtUzFO1xtCU7VUCg_wDtolp4Qw-dFwJDqc_kxP-0FwgtSmh6_ZHMTiKlnxNnJEGFPdUeyqDCb8du7DcCR8kEV4VNr2lB1DDpobIrwyWDNpaBVIQrWN-pUMiMRXZYHmkP1BBBajQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">إطلاق صواريخ من إيران نحو القواعد والأهداف الأمريكية في المنطقة.</div>
<div class="tg-footer">👁️ 7.47K · <a href="https://t.me/naya_foriraq/83802" target="_blank">📅 04:29 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83801">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb7e23eb44.mp4?token=gJguCDP-Vzn3jhccuEJoob8IA_1YP2XdNYYORMcPw-cFOInUj5yLFcD_REBC8r8GA2S9sXuowjskhZm-NJZ4HCCMdqXc9lRCkPvRgW5FpnWxAjMcI6iZgSCHzob7VrVKy0NcIglJkdtzT9kN6L1U82zXlMPtyumVraRAPiG6GnJBWTAOU4VaUyPYHQ3v5IQK4cWmgXzFCoRjw0qvz3uhJ6GKsGim6M4AgQD5m-LrEdZRSCWi7EWTUMRXD8NvDzkD53h_sSXqCS_sneYOz-CridBo23YbtY1XNIq_DwEdp-vHcpXxcZDQzuy5q14lUi3mdoSpXXsMdmkd6ZtnjufWFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb7e23eb44.mp4?token=gJguCDP-Vzn3jhccuEJoob8IA_1YP2XdNYYORMcPw-cFOInUj5yLFcD_REBC8r8GA2S9sXuowjskhZm-NJZ4HCCMdqXc9lRCkPvRgW5FpnWxAjMcI6iZgSCHzob7VrVKy0NcIglJkdtzT9kN6L1U82zXlMPtyumVraRAPiG6GnJBWTAOU4VaUyPYHQ3v5IQK4cWmgXzFCoRjw0qvz3uhJ6GKsGim6M4AgQD5m-LrEdZRSCWi7EWTUMRXD8NvDzkD53h_sSXqCS_sneYOz-CridBo23YbtY1XNIq_DwEdp-vHcpXxcZDQzuy5q14lUi3mdoSpXXsMdmkd6ZtnjufWFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الله أكبر  من الهجوم الصاروخي العنيف الذي دك القاعدة الأمريكية في الأردن وسط فشل تام لمنظومة الباتريوت.</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/naya_foriraq/83801" target="_blank">📅 04:00 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83800">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">انفجارات في بندرعباس جنوبي إيران</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/naya_foriraq/83800" target="_blank">📅 03:58 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83799">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SxG6J-G0Fvb_JVGHIWfHnyeKsW1CkOO6ZqX8dg6DLWbzSN2_QT49g_zRtoSpR2gLRksU8USsBgJLM4Mr2gnqhEh_SQIIeTUcv0lZiWx3HM_oPkAdIco_vf4S4QWeNnv_oYn2yuVjpYDwwD4V2m6kBC-QLT3MS7JhqEDaR_OVFFQUhASpnq-vWso2ou5mTFH6hB_pnh9ok7gHw2Puj_MmJ1Hy-FMpkvbt8hJ30V0rOrX8TkdCOfNZmYi-DoWb9mmPQYgMJhVf1dizKDmr5WuD8sOQD-HhTjhJl-QICCnbncKsT5uK6-yj7giEfxJjGQcPeCHDN4CxM6xtYErTI_NezQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انفجارات تهز الكويت</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/naya_foriraq/83799" target="_blank">📅 03:54 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83798">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">انفجارات تهز الكويت</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/naya_foriraq/83798" target="_blank">📅 03:52 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83797">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">انفجارات تهز الكويت</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/naya_foriraq/83797" target="_blank">📅 03:52 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83796">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1009bdb1ce.mp4?token=UCtcxHbiHO9kWdnIais0rU7E021DK7xKMfJu8Vb9VNFKA0A56wgNvpNZfbyLIEq3YwE4M_Lrcst-kHXY7XD881p0bN8kVUD5xnNY6PBAVXKEoyJrnnTcn5yMm5reqZqnMBYtKUO2ZstoUc1m-Qxjf5B5YlKxrauzB88RkMjXQ3kNKBROtfOtWyP_McHXL1YaigotrDndvT2fiwYYzfsKs9BwYxhtjf3YYebvzmalylSGwnMQa7vtKSAo7eb1gMHEcCDJM3HsjxpJyGd4Z1h4UKMK0vU1ZCHy1UVMCG2LDkHHIf1AQ2WWQ_hlu0tHaQuNhwOg0vDGHEDCHHFBTPqjkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1009bdb1ce.mp4?token=UCtcxHbiHO9kWdnIais0rU7E021DK7xKMfJu8Vb9VNFKA0A56wgNvpNZfbyLIEq3YwE4M_Lrcst-kHXY7XD881p0bN8kVUD5xnNY6PBAVXKEoyJrnnTcn5yMm5reqZqnMBYtKUO2ZstoUc1m-Qxjf5B5YlKxrauzB88RkMjXQ3kNKBROtfOtWyP_McHXL1YaigotrDndvT2fiwYYzfsKs9BwYxhtjf3YYebvzmalylSGwnMQa7vtKSAo7eb1gMHEcCDJM3HsjxpJyGd4Z1h4UKMK0vU1ZCHy1UVMCG2LDkHHIf1AQ2WWQ_hlu0tHaQuNhwOg0vDGHEDCHHFBTPqjkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
مصدر أردني لنايا: لم يتم صد أو إعتراض أي صاروخ إيراني خلال الموجة الصاروخية الأخيرة التي أطلقت نحو القواعد الأمريكية وجميعها أصابت الأهداف بشكل مباشر.</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/naya_foriraq/83796" target="_blank">📅 03:47 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83795">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">إستهداف قواعد الأمريكان في الأردن من زاوية أخرى</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/naya_foriraq/83795" target="_blank">📅 03:28 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83794">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nycoItEXpgrMds4hE9uNvrJDjgVES0vNQCwC1-1FHsTkePsDwaM4-jreFJoOYTT7luvtuNvzjoq45OfxRlbkR8kvIJcHzWszNXoDBM3QMll8DsA_MVjHqQ-5BmrdiiaKX3Sp12xtDE00wtq78wyARl6GgOVrZtNSlz-eYzS6ufPavmnMm1zFLB3nufvk5LfcVbi1LsMHVOK52vQvJJtGs4XiERzWbQfc9HKB9_GgWPOm51WVEOmcXEtsNmpDYkQkKFWFUN0T7kFJkwwUK1zaDqmwyf1rrsqxQZWVjXVnmb5qXp05h6jwXONSe9VjSGfPV_YyQFZMl8isgdfc4e2eDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انفجارات عنيفة تهز البحرين وصافرات الانذار تدوي</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/naya_foriraq/83794" target="_blank">📅 03:25 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83793">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e9785ba849.mp4?token=p3Nv3CESx5EpjglcaujkmIf08YpcVq42Jk4s-XhuKk88ABVPD-1w3KzI7h7aMkmEJRvMg0Mv28gUdhk_qWiK4nWPVct2tSO3-yOYO1h-cfhoZL8Phd3qBTtHPhE9JiPEpiqIio8Qbkth6SL81O1vtw1ma8TgrxmQrUu4equNSXUiSGHBbr9-xwmjLkK7omTd0xSfmhjXuykknonPtMreEYnuBjszJWPIJvBU_5PiKQLrJCYJLcvV7hwgXfEkSqnP8kmEkT7KMZpAPTbxY6rnoosTFNGSIhntSuVCmzkuVSXeLvfmDh9votS6GsG5m_3TTEGh_LRAdVkk9FaMVKIA3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e9785ba849.mp4?token=p3Nv3CESx5EpjglcaujkmIf08YpcVq42Jk4s-XhuKk88ABVPD-1w3KzI7h7aMkmEJRvMg0Mv28gUdhk_qWiK4nWPVct2tSO3-yOYO1h-cfhoZL8Phd3qBTtHPhE9JiPEpiqIio8Qbkth6SL81O1vtw1ma8TgrxmQrUu4equNSXUiSGHBbr9-xwmjLkK7omTd0xSfmhjXuykknonPtMreEYnuBjszJWPIJvBU_5PiKQLrJCYJLcvV7hwgXfEkSqnP8kmEkT7KMZpAPTbxY6rnoosTFNGSIhntSuVCmzkuVSXeLvfmDh9votS6GsG5m_3TTEGh_LRAdVkk9FaMVKIA3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الصواريخ الإيرانية تمر بسلام نحو القواعد الأمريكية في الأردن وتصيبها بدقة وبشكل مباشر</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/naya_foriraq/83793" target="_blank">📅 03:23 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83792">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4b58dee1b.mp4?token=SUpqWJ8JgkEs56j-6p9xw4g2GBZ0nU1B8sanHN23BSYtvobSBXNdBBsNcfVLjXYWt28-8IXyUi1nZKAqmFT9QXpGjhAo8m1SProgXsBS7uglhoqpJx0PCF-ZEhp_QWsZBYw_qGqlyFH_-LNChktg0md6UAUIm5PBHD42TQByVdJ1Ejd1gU4rkSB-vkgTajCFnsJlErIwwgioEzEe42crSm_-sLxZxAbyxT0aSCL5KliQcLzVa2btfhRrWLWV9HOw4gUg99fHxQn5rXt3_b9dFxcM5sImPYJca05z89uEO9Bw1IsgkFkqAqjI7vP7XBkWxwhrWQIuloU9sxSv_6dOnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4b58dee1b.mp4?token=SUpqWJ8JgkEs56j-6p9xw4g2GBZ0nU1B8sanHN23BSYtvobSBXNdBBsNcfVLjXYWt28-8IXyUi1nZKAqmFT9QXpGjhAo8m1SProgXsBS7uglhoqpJx0PCF-ZEhp_QWsZBYw_qGqlyFH_-LNChktg0md6UAUIm5PBHD42TQByVdJ1Ejd1gU4rkSB-vkgTajCFnsJlErIwwgioEzEe42crSm_-sLxZxAbyxT0aSCL5KliQcLzVa2btfhRrWLWV9HOw4gUg99fHxQn5rXt3_b9dFxcM5sImPYJca05z89uEO9Bw1IsgkFkqAqjI7vP7XBkWxwhrWQIuloU9sxSv_6dOnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الله أكبر  الصواريخ الإيرانية تنقض على قاعدة موفق السلطي</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/naya_foriraq/83792" target="_blank">📅 03:19 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83791">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a287fd1d97.mp4?token=N8-P-r7PXPqMaqTlmVOG-G4RVqWANNTd1wq0QDiQQpJfcg2hpmcH0l5GyfbuG3W7EC_vWlmms8YAMLge5ZUxtrI9ZSCgj4vMuZv7aUAWH5W0t1X9voORnqhNVUAmwqkKohS7iWthibnm8wsXf23c054QyXaFxy0U2iUvelDWTIaZRFLokTBChYJTa2nI8VjTLclAdZxT8WTkikHZq9WPnKvQIkd2VtkWOaK4cjr9QzE1_P9Ztt25nlBpkH6gfXA8vwxJ2LFKsx2L1Ac0vHKaxsICoAIQpA3Oaj4XPG_DbfFkNBxmMZCigZIZb_bBl5GwiKv9ocNg9DfNEG9sMd8zKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a287fd1d97.mp4?token=N8-P-r7PXPqMaqTlmVOG-G4RVqWANNTd1wq0QDiQQpJfcg2hpmcH0l5GyfbuG3W7EC_vWlmms8YAMLge5ZUxtrI9ZSCgj4vMuZv7aUAWH5W0t1X9voORnqhNVUAmwqkKohS7iWthibnm8wsXf23c054QyXaFxy0U2iUvelDWTIaZRFLokTBChYJTa2nI8VjTLclAdZxT8WTkikHZq9WPnKvQIkd2VtkWOaK4cjr9QzE1_P9Ztt25nlBpkH6gfXA8vwxJ2LFKsx2L1Ac0vHKaxsICoAIQpA3Oaj4XPG_DbfFkNBxmMZCigZIZb_bBl5GwiKv9ocNg9DfNEG9sMd8zKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
الجيش الإيراني:
قبل ساعات، استهدفت طائرات مسيرة تابعة للجيش، في المرحلة الرابعة عشرة من عملية "صاعقة"، مخزن ذخيرة تابع للجيش الأمريكي المتجاوز في معسكر العدي، والمباني التابعة لقيادة هذا الجيش القاتل، ومخازن الذخيرة في قاعدة علي السالم، وعدد من نقاط الاتصال في الكويت.
🔻
يعتبر معسكر العدي أحد المراكز الهامة لدعم وإعادة تنظيم القوات الأمريكية، كما تعتبر قاعدة علي السالم واحدة من أكبر المراكز لدعم وتنسيق العمليات الجوية الأمريكية في منطقة الخليج العربي.
🔻
وفي إطار هذه الهجمات، استهدفت أيضًا خزانات الوقود التابعة للجيش المتجاوز في قاعدة الأزرق في الأردن بواسطة طائرات مسيرة تابعة للجيش.
🔻
أصبحت قاعدة الأزرق الجوية في الأردن، نظرًا لموقعها وبنيتها التحتية ونشر المعدات العسكرية الحديثة والاستثمارات الضخمة الأمريكية، قاعدة حيوية للولايات المتحدة، تلعب دورًا رئيسيًا في السيطرة على المنطقة والعمليات العسكرية في غرب آسيا.</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/naya_foriraq/83791" target="_blank">📅 03:15 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83790">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">انفجارات عنيفة تهز البحرين وصافرات الانذار تدوي</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/naya_foriraq/83790" target="_blank">📅 03:14 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83789">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">عدوان أمريكي غاشم على جزيرة لارك جنوبي إيران.</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/naya_foriraq/83789" target="_blank">📅 03:13 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83788">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/94ace3b7e5.mp4?token=Gy3622LXf2xvCWvVzzkmRSSEhaF1T-p6N7wMm-_QtAUwrltL6f-kKfG_oQwXU-XO4zKwET9LljWU4pmf323Lujd7SUR73yXndctvzut6C3zFqqjogM8-kJHGU2YqkCl64XIup2VlP-C7wFSN6tOTEFrlSUKBKaIDEbAPAvCd-SRgSG-BcKpTWi1_8Pn3ZIsfLTS4H_HfyQLgAvgH1YBqUrYwJU_maBdL14EgYIev7VjC2efiCQC5YPN9Tivob8eOlFqjprxDo4gGl7DI4_UZwvxqEGhq6_NokNH2yBCUXVNJiM0PMHx5_cYXstJChgV-sFxm0s3jar8H3Xt_qvmkWYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/94ace3b7e5.mp4?token=Gy3622LXf2xvCWvVzzkmRSSEhaF1T-p6N7wMm-_QtAUwrltL6f-kKfG_oQwXU-XO4zKwET9LljWU4pmf323Lujd7SUR73yXndctvzut6C3zFqqjogM8-kJHGU2YqkCl64XIup2VlP-C7wFSN6tOTEFrlSUKBKaIDEbAPAvCd-SRgSG-BcKpTWi1_8Pn3ZIsfLTS4H_HfyQLgAvgH1YBqUrYwJU_maBdL14EgYIev7VjC2efiCQC5YPN9Tivob8eOlFqjprxDo4gGl7DI4_UZwvxqEGhq6_NokNH2yBCUXVNJiM0PMHx5_cYXstJChgV-sFxm0s3jar8H3Xt_qvmkWYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الصواريخ الإيرانية تستهدف القاعدة الأمريكية في الأردن</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/naya_foriraq/83788" target="_blank">📅 03:11 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83787">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9d32c27bc.mp4?token=ou9fcjvmgFJ_LSLRY1fTG1O7PUjP2Te9RtUshP0VQ05-FX5uLLgiEQK6o75ImDpQGKBiIjkZtzaJfyTK7GYpQ9oOnmDsaXZO1hJ5ZM3eRBMCvGWUIGxfM58vUxOn9sRVL7JQYv8djEJEaYsm71FweBn2CUZfkG4NLsQueXuEvdQ52MTtp_HP9QTqBgkciKT08KP57nMStifOo0J6abyHn3T7NfVsLx3FBQdIvdXq6PgVR1fzo2_ExeFg8HhE6a_CNlmMa7DKO3zwaBPb59WIBhGvpI_EayjsecZTqQA8cCN2fWQ2prEeEqgSbRvg-7mh5B1kOeAnHehVTPvqUc91RA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9d32c27bc.mp4?token=ou9fcjvmgFJ_LSLRY1fTG1O7PUjP2Te9RtUshP0VQ05-FX5uLLgiEQK6o75ImDpQGKBiIjkZtzaJfyTK7GYpQ9oOnmDsaXZO1hJ5ZM3eRBMCvGWUIGxfM58vUxOn9sRVL7JQYv8djEJEaYsm71FweBn2CUZfkG4NLsQueXuEvdQ52MTtp_HP9QTqBgkciKT08KP57nMStifOo0J6abyHn3T7NfVsLx3FBQdIvdXq6PgVR1fzo2_ExeFg8HhE6a_CNlmMa7DKO3zwaBPb59WIBhGvpI_EayjsecZTqQA8cCN2fWQ2prEeEqgSbRvg-7mh5B1kOeAnHehVTPvqUc91RA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محاولات فاشلة لمنظومة الباتريوت الأمريكية في اعتراض الصواريخ الإيرانية التي تنقض على قاعدة موفق السلطي بالأردن</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/naya_foriraq/83787" target="_blank">📅 03:02 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83786">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/454271fe9c.mp4?token=bvQckXNi_qAJLnGNMrgWZAzoASJjFVj-5aOvKaL1NDHGUq2r5OvgIT8p_6aeSlSF5ZRwygS1WkP7LOK8_Iv94oUjzirbeceRsRUw5vOIFiu3V04q_xl9oPLA2jkQehW-mf-5Yf1TwU3Qi4IgFjG2HWJBzbt6eXAUTGjEe9jD_03UZEUeeaPeZj4o8UwIu_XGy_g8bxiLyrL4ir5HIcngTl6CfYNNVe2jSUMIaV9O49ZiWTlYQlWlSSkeMeqZUi_eOcbRCjafy9LQ-ZfXER-wYM5cjMBzAgoq_lx1HeIq1LlH32WW4QGtUT4VWfB4JbmzKQgX31q-aOrmhb6o5ZMSMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/454271fe9c.mp4?token=bvQckXNi_qAJLnGNMrgWZAzoASJjFVj-5aOvKaL1NDHGUq2r5OvgIT8p_6aeSlSF5ZRwygS1WkP7LOK8_Iv94oUjzirbeceRsRUw5vOIFiu3V04q_xl9oPLA2jkQehW-mf-5Yf1TwU3Qi4IgFjG2HWJBzbt6eXAUTGjEe9jD_03UZEUeeaPeZj4o8UwIu_XGy_g8bxiLyrL4ir5HIcngTl6CfYNNVe2jSUMIaV9O49ZiWTlYQlWlSSkeMeqZUi_eOcbRCjafy9LQ-ZfXER-wYM5cjMBzAgoq_lx1HeIq1LlH32WW4QGtUT4VWfB4JbmzKQgX31q-aOrmhb6o5ZMSMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجار عنيف يشعل قاعدة موفق السلطي في الأردن</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/naya_foriraq/83786" target="_blank">📅 03:00 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83785">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b3b6b0ad7.mp4?token=dTb2dEIn9y3m8TBMDpKjlllVUJrqD4t5ifp_07BteAZ4iU-pctpEUa0LedGqdhVZFhSXl7Ux1y8it8wWY3SBB89IKIs5hOc7ljMliRDyPgxCF0nzy4WGCCk9DymE9A-RiJM362JbbI9Sn6XFWAkyzSdVCt94q-VsLKq7byhxFuGgqYNKNNzmpJ9mLk7xauXaEBdybEs10QS1McCOJl6eoz0R8Zmp23UofqYvgLv4S3m2bQ4eS19zaTloOcW2VB1nYu5u1oIoTV16ehOcZU0YtHoTY-nFjXK9KXVklZW225I_gEbpWhV8azzbKz3S9C_ICYoRLvreT2AfMoX5eVSYZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b3b6b0ad7.mp4?token=dTb2dEIn9y3m8TBMDpKjlllVUJrqD4t5ifp_07BteAZ4iU-pctpEUa0LedGqdhVZFhSXl7Ux1y8it8wWY3SBB89IKIs5hOc7ljMliRDyPgxCF0nzy4WGCCk9DymE9A-RiJM362JbbI9Sn6XFWAkyzSdVCt94q-VsLKq7byhxFuGgqYNKNNzmpJ9mLk7xauXaEBdybEs10QS1McCOJl6eoz0R8Zmp23UofqYvgLv4S3m2bQ4eS19zaTloOcW2VB1nYu5u1oIoTV16ehOcZU0YtHoTY-nFjXK9KXVklZW225I_gEbpWhV8azzbKz3S9C_ICYoRLvreT2AfMoX5eVSYZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الله أكبر  الصواريخ الإيرانية تتجاوز منظومة الباتريوت وتستهدف قاعدة موفق السلطي في الأردن.</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/naya_foriraq/83785" target="_blank">📅 02:59 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83784">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b3aede10e2.mp4?token=MUbK8Aum05w3GlADZtTBQMDln5Lrrsde5lH5m3uOuiV2pGaJHwx-ojxjlQ2d5gTScWKr-la89__v9tblMJusE8udMmW0HLOWAUav-Qr3hbRr6iN182jb6DYB7qVQnK4bdmGYu_zlEejapXy8Op3FsYysGMBvjiL3l047X9-tjywKoVPSrs2fL3imoR07kfxfLsQmE78ok0tFhydNJzbNlxy-KoBRAPUKAq14LuKSvA0O-CnXmFaGNoPAnUgxdfmWFyvsjC7KpEmyyH--u9Bq-ux-fszWnJeboCN5wlyirJqld7YyIEkIa5Oe4qmYVbJc_XYDanjoN53UfX3dwOX1IIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b3aede10e2.mp4?token=MUbK8Aum05w3GlADZtTBQMDln5Lrrsde5lH5m3uOuiV2pGaJHwx-ojxjlQ2d5gTScWKr-la89__v9tblMJusE8udMmW0HLOWAUav-Qr3hbRr6iN182jb6DYB7qVQnK4bdmGYu_zlEejapXy8Op3FsYysGMBvjiL3l047X9-tjywKoVPSrs2fL3imoR07kfxfLsQmE78ok0tFhydNJzbNlxy-KoBRAPUKAq14LuKSvA0O-CnXmFaGNoPAnUgxdfmWFyvsjC7KpEmyyH--u9Bq-ux-fszWnJeboCN5wlyirJqld7YyIEkIa5Oe4qmYVbJc_XYDanjoN53UfX3dwOX1IIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/naya_foriraq/83784" target="_blank">📅 02:58 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83783">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">الصواريخ الإيرانية تستهدف قاعدة موفق السلطي الأمريكية في الأردن وسط تفعيل منظومة الباتريوت لإعتراض الهحوم.</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/naya_foriraq/83783" target="_blank">📅 02:56 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83782">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9ebaff0c2c.mp4?token=AaPqglCXn4CEmHtVfiw7E5Rzj9uGL2umQLq1f0Qjt8bQjL8tn9snAbilSol1xbO3R5fWOnnwMP8stIsUi5Ya-LGtElCZeENL10wDCA49oQJmFpcMyuabR2c0l5RWbKo1vHuLgB9B572M9siwEvyY3x1uJbIH71noKkf5yWRWEqC0bDHk2ErK_2v3LEWycaBX3tSomUpr85OR_4GLBjHvdJyl-CFgT79Qnz4zJsPfGULrJP52NqhGjn7Spj2abIvfxp2JYST5ayGgZgxdyukZvsMZoAFDb-DcS5mhDSJ76nKXYEQe6neCMDhN2_HrA8mtEAR5PLFxCkTQBJ9JJP70oA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9ebaff0c2c.mp4?token=AaPqglCXn4CEmHtVfiw7E5Rzj9uGL2umQLq1f0Qjt8bQjL8tn9snAbilSol1xbO3R5fWOnnwMP8stIsUi5Ya-LGtElCZeENL10wDCA49oQJmFpcMyuabR2c0l5RWbKo1vHuLgB9B572M9siwEvyY3x1uJbIH71noKkf5yWRWEqC0bDHk2ErK_2v3LEWycaBX3tSomUpr85OR_4GLBjHvdJyl-CFgT79Qnz4zJsPfGULrJP52NqhGjn7Spj2abIvfxp2JYST5ayGgZgxdyukZvsMZoAFDb-DcS5mhDSJ76nKXYEQe6neCMDhN2_HrA8mtEAR5PLFxCkTQBJ9JJP70oA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">موجات صاروخية أطلقت من إيران تجاه القواعد الأمريكية في الأردن</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/naya_foriraq/83782" target="_blank">📅 02:54 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83781">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🌟
🇮🇷
جراء العدوان الأمريكي الغاشم..
إرتقاء 3 شهداء و8 اصابات في محافظة هرمزغان كحصيلة أولية.</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/naya_foriraq/83781" target="_blank">📅 02:37 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83780">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🇮🇷
🌟
🌟
مسؤول أمريكي: إيران أطلقت صاروخا باليستيا على قاعدة أمريكية في السعودية.  هجوم صاروخي إيراني طال منطقتي الخرج وينبع السعودية.</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/naya_foriraq/83780" target="_blank">📅 02:31 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83779">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">انفجار في اميدية بمحافظة خوزستان جنوب ايران</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/naya_foriraq/83779" target="_blank">📅 02:28 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83778">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">انفجارات تهز السعودية وصافرات الانذار تدوي</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/naya_foriraq/83778" target="_blank">📅 02:27 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83777">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tnvy9BkhaAD1_UiPeqA5Tt18XtPG6HHezjeatovTrr0y-W5VZXMggTvg0bEk8NmN-QQgOf9Cfj_8AAhNflP5bG9l9xFCv_Y2X_jv-8orGRcY--bgi-E_bKJ1cESY1ZPqp2HEXxn2u5LdUZdM2Dw1GZrZv4n065Z3e60gtsNp6aj5VoyK4kugo3iec9F9aryJKBqatbhAAH1f_myd4OKkKi_HdMTk6juleE5RCs9A4fQCT5XLYT7EBWz60_qYxitShnGZW_r4cccTS2XPQ0wCk-5SylthInsxULSijzXc6uAuyW27ZELZTMBAJ7hwgALhJdAjbBirU1NLvGDj2E-NNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عدوان أمريكي غاشم يطال طرق وجسور  بين محافظتي كرمان وهرمزغان جنوبي إيران.</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/naya_foriraq/83777" target="_blank">📅 02:26 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83776">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f45172ab3b.mp4?token=PZBLQu8WpGnrqg0Axd6N5A92mgZtn-N4cSog8faP_Eu_qpIkD5J_MBmXDx25xyJ2jQz6bOjPVVT_82UblG-6CcU7A7DFy1kAIf_l2rzoRoFl-qtfSDz0LHhWTcIKx1iwWFIhHtS2L0wFmj7t2gZMrlfB5E1ixJal0BIEqQe423tSfHVF8CDjS7OXtmpqBAdaFAncgyczZJGviDgNSeRMP9ACBqpwjMczQ2C6j_RNgdLYCOO6toP2irb7r3EF47tRR8LJjAWil8iBun5PsJ6PP3Ggo_jmy52gCo5ndZKLtd2HI67fV2776QDk73scI1Zrxdl19_1VycFUOLDD8oiEfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f45172ab3b.mp4?token=PZBLQu8WpGnrqg0Axd6N5A92mgZtn-N4cSog8faP_Eu_qpIkD5J_MBmXDx25xyJ2jQz6bOjPVVT_82UblG-6CcU7A7DFy1kAIf_l2rzoRoFl-qtfSDz0LHhWTcIKx1iwWFIhHtS2L0wFmj7t2gZMrlfB5E1ixJal0BIEqQe423tSfHVF8CDjS7OXtmpqBAdaFAncgyczZJGviDgNSeRMP9ACBqpwjMczQ2C6j_RNgdLYCOO6toP2irb7r3EF47tRR8LJjAWil8iBun5PsJ6PP3Ggo_jmy52gCo5ndZKLtd2HI67fV2776QDk73scI1Zrxdl19_1VycFUOLDD8oiEfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">موجات صاروخية واسعة تنطلق من إيران</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/naya_foriraq/83776" target="_blank">📅 02:25 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83775">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/21f8353d4f.mp4?token=GxaEproDAtPQRPO3atM1MN_WkoK71DwKiVXc5kfPuRonii82asF9vlpEEraGCgh3PNSxS9EqRqBALHH7mnLKmRBQ7lwsC6kTQ5FzjLLgIpLKN-MrtdNeVpScrTnPyYLjPy4ntKRmFGeqNGCT_N2sPRb48lygRiTppiRokdxtvkx7BFObm9eSiNcVeDFe4oLVJPkpCdkb2IcrLuA_tsTGuS6QbMmsb1aredNzwrc3rUJnC13yVEp5brF9kAYFRZb88DuyNWOy3b3xGoerBJ2SGKT0EtbEoE-gMVBY1hwe3unb2B257gyZd4lrpTdfxazddaEDZkSmtYVEsAgSI-xW_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/21f8353d4f.mp4?token=GxaEproDAtPQRPO3atM1MN_WkoK71DwKiVXc5kfPuRonii82asF9vlpEEraGCgh3PNSxS9EqRqBALHH7mnLKmRBQ7lwsC6kTQ5FzjLLgIpLKN-MrtdNeVpScrTnPyYLjPy4ntKRmFGeqNGCT_N2sPRb48lygRiTppiRokdxtvkx7BFObm9eSiNcVeDFe4oLVJPkpCdkb2IcrLuA_tsTGuS6QbMmsb1aredNzwrc3rUJnC13yVEp5brF9kAYFRZb88DuyNWOy3b3xGoerBJ2SGKT0EtbEoE-gMVBY1hwe3unb2B257gyZd4lrpTdfxazddaEDZkSmtYVEsAgSI-xW_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الله أكبر  موجة صاروخية اخرى تنطلق</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/naya_foriraq/83775" target="_blank">📅 02:24 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83774">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cae985645c.mp4?token=v8WeiIWtBEYPp2fZ9GWewiVPEZyxWNvqOAEOyiB46ZU-VHeG1TWaiWlgLsXEej25f9wyvoiSdrI5qAkkH3gaBJSswGnOCxuAapObcFvJ5-MP4VGsJwQMQfwbsp6paFwUifT3RYJ78dDvv56V-ysaq8sHxXtNFNMut2a2-9IsYwTYWXO2J8VU1GSSLRDbuel_uEoEKujmo77FQCeHP50AVbxr-xKUprYrxft_gmh-TRVWEl3nmEmVgA2GPYi3Z9DTthGNcxs6mrIvS1kWWV8UFq7qJ2b9_aydNmwCXEyc2gZzY6Uf5WeWOMwawMKeRtKvn38AnwtmRrMnKrPtRN5Zbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cae985645c.mp4?token=v8WeiIWtBEYPp2fZ9GWewiVPEZyxWNvqOAEOyiB46ZU-VHeG1TWaiWlgLsXEej25f9wyvoiSdrI5qAkkH3gaBJSswGnOCxuAapObcFvJ5-MP4VGsJwQMQfwbsp6paFwUifT3RYJ78dDvv56V-ysaq8sHxXtNFNMut2a2-9IsYwTYWXO2J8VU1GSSLRDbuel_uEoEKujmo77FQCeHP50AVbxr-xKUprYrxft_gmh-TRVWEl3nmEmVgA2GPYi3Z9DTthGNcxs6mrIvS1kWWV8UFq7qJ2b9_aydNmwCXEyc2gZzY6Uf5WeWOMwawMKeRtKvn38AnwtmRrMnKrPtRN5Zbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الله أكبر
موجة صاروخية اخرى تنطلق</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/naya_foriraq/83774" target="_blank">📅 02:23 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83773">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">السعودية</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/naya_foriraq/83773" target="_blank">📅 02:22 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83772">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">السعودية</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/naya_foriraq/83772" target="_blank">📅 02:22 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83770">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fbbb6ed794.mp4?token=tMhGVCZTcy6Os5u-sRbZfL0SHP61jTNpylyQoy1uoRGcCsbt6jPaMVyivs7RcjOMKwsLaRR49stL5DzHjy3B1LNRA0ti6zSpHQQ1erz95xRP5bVm0ggLgK5amLa38sNweHH-MuMtrd4DHrLsepeu2RcAkLmAwscxYoQuopYNysROC8XMCGsezCJTWxy52R4Rt1S4uAoNMuq_-z8sHU-cw5CA4hH0N8QKt9cEfb2p-a24MmnLtX0Ckh_5UUA3UQqYSpE_2-XlxLkoDmjZcVUnJtciaABDaC8t4GC8-c5mv2xROvmR8jt_izlvRPfQr2fXbAhEJKsMAH73H-xMDjKrLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fbbb6ed794.mp4?token=tMhGVCZTcy6Os5u-sRbZfL0SHP61jTNpylyQoy1uoRGcCsbt6jPaMVyivs7RcjOMKwsLaRR49stL5DzHjy3B1LNRA0ti6zSpHQQ1erz95xRP5bVm0ggLgK5amLa38sNweHH-MuMtrd4DHrLsepeu2RcAkLmAwscxYoQuopYNysROC8XMCGsezCJTWxy52R4Rt1S4uAoNMuq_-z8sHU-cw5CA4hH0N8QKt9cEfb2p-a24MmnLtX0Ckh_5UUA3UQqYSpE_2-XlxLkoDmjZcVUnJtciaABDaC8t4GC8-c5mv2xROvmR8jt_izlvRPfQr2fXbAhEJKsMAH73H-xMDjKrLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لازالت المسيرات الإنتحارية تحلق في سماء محافظة السليمانية شمالي العراق.</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/naya_foriraq/83770" target="_blank">📅 02:21 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83769">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c5f0a10461.mp4?token=SD4HNLgQnA0-UKLx5ggaGmLo9ScaClQRLOmBSZH2iu6INxvyhGwhJfyq5yTBk0m0Xte-k6VfcTjEGeenKaP-m8-OT7hZmYzBSwH_Oro-6uUB4AkxEUvMMUG7ZPP4N5pI0nQnOTkX7SNrwhCaOmvsq8FB0eUu6k1szW3FbDXAZyorurqZrw1IOtF0dktmAw2QJFBAG9bJ_U9YEKUYeIbREaMNRT6pZVadJDXURmzLFFMbdiXXM2utB9yi1urcdR9dUaXidmKp3hWiJbLplhqaLxAuEDgIeTw3q-V1RXRaq_LbEDIcBPSMdK7PYiMVtXbm6_Qzagq-wpRwbanZ03khYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c5f0a10461.mp4?token=SD4HNLgQnA0-UKLx5ggaGmLo9ScaClQRLOmBSZH2iu6INxvyhGwhJfyq5yTBk0m0Xte-k6VfcTjEGeenKaP-m8-OT7hZmYzBSwH_Oro-6uUB4AkxEUvMMUG7ZPP4N5pI0nQnOTkX7SNrwhCaOmvsq8FB0eUu6k1szW3FbDXAZyorurqZrw1IOtF0dktmAw2QJFBAG9bJ_U9YEKUYeIbREaMNRT6pZVadJDXURmzLFFMbdiXXM2utB9yi1urcdR9dUaXidmKp3hWiJbLplhqaLxAuEDgIeTw3q-V1RXRaq_LbEDIcBPSMdK7PYiMVtXbm6_Qzagq-wpRwbanZ03khYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رشقات صاروخية تنطلق من إيران صوب القواعد المعادية</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/naya_foriraq/83769" target="_blank">📅 02:19 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83768">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8018ed7cf3.mp4?token=vamDRa9j0nQzNjb8Nkduqa4PYz9DO59_HN6D8kxJ6Eszmeuxrr45zKeI6OiiS8Rrh1vnVPRnVIScqzDgrtMuZAuRqG_CqHoJYLcQqIvvm1mhtkowMywDMoDKEQnIZ9cxsZqE5Md84pyZR8z3hKtIeyHkdn53Wp2xVM2I666MOLXEm-m6XlohFqSY9tQD98nYEwkH3_Bjw7DYZWIvWxVqMWLwm7hrhjAGXFWi1Yz1hFWQfLPpoP8kjNpuJrl1shUOKsvfXVLLNJWmO7eeZM3404tv1O2kSOGemaN34PkdAYUh7WpgJDWz2R6KaFS4VWfZ8d8Ka1N97-OiH80ijThE7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8018ed7cf3.mp4?token=vamDRa9j0nQzNjb8Nkduqa4PYz9DO59_HN6D8kxJ6Eszmeuxrr45zKeI6OiiS8Rrh1vnVPRnVIScqzDgrtMuZAuRqG_CqHoJYLcQqIvvm1mhtkowMywDMoDKEQnIZ9cxsZqE5Md84pyZR8z3hKtIeyHkdn53Wp2xVM2I666MOLXEm-m6XlohFqSY9tQD98nYEwkH3_Bjw7DYZWIvWxVqMWLwm7hrhjAGXFWi1Yz1hFWQfLPpoP8kjNpuJrl1shUOKsvfXVLLNJWmO7eeZM3404tv1O2kSOGemaN34PkdAYUh7WpgJDWz2R6KaFS4VWfZ8d8Ka1N97-OiH80ijThE7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">موجة صاروخية تنطلق من إيران نحو القواعد الأمريكية في المنطقة</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/naya_foriraq/83768" target="_blank">📅 02:18 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83767">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b3210d2d30.mp4?token=Nn-NYQJj3l8ga6NxRyUupvtF-KNy4UR3QFxvukwSv9lqLqiLj9L9uiatnVmhqd23X02n6Tgy0pz_br8wgiBmhEZ1K8j8ovzDvBbk8Asqhith_rK9QX7abW__StMoh_5QBT0pdR7EA-iA_PzeaPYPssXyTCVDUYFNqqGZekjjjAlqoWlhJxZNqCc6ZpuIEfUzDDi8OHCYaz_9r1ha4BD2mlSQRH4_DyGUqfiFe8CtDuvXlFMjoPC7ZqDU0MidRc3i0kIUNDDXKUKN1H23po1u2qx4PpEGAFx8YFVWLGjt8ka5N5IwxHUKEqA8AV1kjVh0-mGEbuQmkPE-CA080F4KXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b3210d2d30.mp4?token=Nn-NYQJj3l8ga6NxRyUupvtF-KNy4UR3QFxvukwSv9lqLqiLj9L9uiatnVmhqd23X02n6Tgy0pz_br8wgiBmhEZ1K8j8ovzDvBbk8Asqhith_rK9QX7abW__StMoh_5QBT0pdR7EA-iA_PzeaPYPssXyTCVDUYFNqqGZekjjjAlqoWlhJxZNqCc6ZpuIEfUzDDi8OHCYaz_9r1ha4BD2mlSQRH4_DyGUqfiFe8CtDuvXlFMjoPC7ZqDU0MidRc3i0kIUNDDXKUKN1H23po1u2qx4PpEGAFx8YFVWLGjt8ka5N5IwxHUKEqA8AV1kjVh0-mGEbuQmkPE-CA080F4KXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رشقات صاروخية تنطلق من إيران صوب القواعد المعادية</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/naya_foriraq/83767" target="_blank">📅 02:18 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83766">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9ce5db5c99.mp4?token=YQt8cFvQxXWEItwBXm220d4JpgtUfq__7xqR8DJ0UR0psuuJ57_VDBQYRuUngOtpveeJVFZxMFa_FyJBm3SQvjkaKvSqZDGxWZ6wLRsAiRUW4u1Zeav_k6A59Bd91SxdGq5cZle09l2W-oWI8pHIK5CVGADspmssWgI3t6DSdT5XYngARgpOxYJbPyJ7kK9mqCd8_u42qhBQgXb1Z0CcBKhNUiGKNML1jO3k4VOIFZotZ9LJV3kZmg6Sn_TxiM_liwTAcT3MEm5nFWy93rmEnjGcGsqrlIgEMFHfWHVqo0BwIxSoxH0HXuyqnYRePwwT5i0GlSGvhlIptleaB_X_kQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9ce5db5c99.mp4?token=YQt8cFvQxXWEItwBXm220d4JpgtUfq__7xqR8DJ0UR0psuuJ57_VDBQYRuUngOtpveeJVFZxMFa_FyJBm3SQvjkaKvSqZDGxWZ6wLRsAiRUW4u1Zeav_k6A59Bd91SxdGq5cZle09l2W-oWI8pHIK5CVGADspmssWgI3t6DSdT5XYngARgpOxYJbPyJ7kK9mqCd8_u42qhBQgXb1Z0CcBKhNUiGKNML1jO3k4VOIFZotZ9LJV3kZmg6Sn_TxiM_liwTAcT3MEm5nFWy93rmEnjGcGsqrlIgEMFHfWHVqo0BwIxSoxH0HXuyqnYRePwwT5i0GlSGvhlIptleaB_X_kQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">موجة صاروخية تنطلق من إيران نحو القواعد الأمريكية في المنطقة</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/naya_foriraq/83766" target="_blank">📅 02:18 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83765">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/naya_foriraq/83765" target="_blank">📅 02:15 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83764">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/naya_foriraq/83764" target="_blank">📅 02:15 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83763">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/68c455d6a4.mp4?token=kdA3ENjTWhF9hwXk7Pe-eLdMAiRy7qjjZLZR03hiDP-wKN0UFT2_jn_8a6Twhcx2MyFZ-H6wI1pikZoZWBsqHEwpmVLcW8afxO2LgeFIFabxv8cIfJPRFvwUHIF58pR3C39EinG_Vbi7LoEbcZ1cqFeu6TnWcZIQWa7G3kDCvZcHgx61uCZa0OVUuLYpL1g9ZrLRhTvyb82neE4E-bwrh8vgoCn-BMTawZ0Vg7K7gKcsEv9-FhU75oviWEycuUlEmqIJQ0eCeVVG9j0NeysbDagxUqZCjw4iqoyQKOrizGGxTN7e5wXCUqfDjUYPHuZ5QA9639NT37FRyhUvbki4Pg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/68c455d6a4.mp4?token=kdA3ENjTWhF9hwXk7Pe-eLdMAiRy7qjjZLZR03hiDP-wKN0UFT2_jn_8a6Twhcx2MyFZ-H6wI1pikZoZWBsqHEwpmVLcW8afxO2LgeFIFabxv8cIfJPRFvwUHIF58pR3C39EinG_Vbi7LoEbcZ1cqFeu6TnWcZIQWa7G3kDCvZcHgx61uCZa0OVUuLYpL1g9ZrLRhTvyb82neE4E-bwrh8vgoCn-BMTawZ0Vg7K7gKcsEv9-FhU75oviWEycuUlEmqIJQ0eCeVVG9j0NeysbDagxUqZCjw4iqoyQKOrizGGxTN7e5wXCUqfDjUYPHuZ5QA9639NT37FRyhUvbki4Pg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عدوان أمريكي غاشم يطال طرق وجسور  بين محافظتي كرمان وهرمزغان جنوبي إيران.</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/naya_foriraq/83763" target="_blank">📅 02:14 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83762">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🇮🇱
إعلام العدو:
حدث أمني في جنوب لبنان ومروحيات الجيش الإسرائيلي تنقل عدد من الجنوب إلى مستشفى رمبام.</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/naya_foriraq/83762" target="_blank">📅 02:11 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83761">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">انفجارات في مدينة جغادك جنوبي إيران.</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/naya_foriraq/83761" target="_blank">📅 02:10 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83760">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ensxm-Mkl0mzuYWILjs19dW8Xwh-gjpjOOUREk9a_s1adHoorDSTiGcOBrZRJ67xBf1uk6Fucx5w1FB4pLBglPs7oD3pcF309Un3VRoM1EQgDu2RIB6cbkft8_p-qI_DXq3Q9XpI-h0cI8qW0sSucHApdDXy_O9xtKIOGTjqyQ2Pk3Bssb0E3oFCy-ruN4q6TTJdlpmLwDfm2DT6mXguNDtMa07nX-ID5rjeTBScZIFIskznD94LnMLm57OcG06SmdDp9WtJhg5Uo-Emhm8_4ZkZ_KGVOHDGWBhdxw8ckVZVmaAW7gDbzqz5Of7mGRX6LSlsqjg5cv2ajJlS453SzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
بحرية الحرس الثوري:
خلال الساعات القليلة الماضية، حاولت أربع سفن، مدعومة بالجيش الأمريكي الإرهابي، عبور مضيق هرمز. وخلال عملية مشتركة بالصواريخ والطائرات المسيّرة، تم إيقاف السفن الأربع في مكانها.</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/naya_foriraq/83760" target="_blank">📅 02:06 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83759">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">⭐️
مكافحة الإرهاب في إقليم كردستان العراق:
تم استهداف أربيل بخمسة طائرات مسيرة إنتحارية.</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/naya_foriraq/83759" target="_blank">📅 02:04 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83758">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromنايا - NAYA</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">الفرار الفرار حيدر آمد شكار _ شور مزلزل _ الفرار الفرار جاء حيدر…</div>
  <div class="tg-doc-extra"></div>
</div>
<a href="https://t.me/naya_foriraq/83758" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔻
الفرار الفرار..</div>
<div class="tg-footer">👁️ 9.84K · <a href="https://t.me/naya_foriraq/83758" target="_blank">📅 02:03 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83757">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/naya_foriraq/83757" target="_blank">📅 02:01 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83756">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/naya_foriraq/83756" target="_blank">📅 02:01 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83755">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">انفجارات في بندرعباس جنوبي إيران</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/naya_foriraq/83755" target="_blank">📅 01:58 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83754">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a2972407f9.mp4?token=ZLnFgNPIj2a2rl1gtI_WFkOvDuSOuL4fqYlzurjbCND6KKQZvnjysYKDpl47ljDyLAOvZY6GLsbOzRdZn45bo9jg8kzwD-XPO-RJwjdhfhrTbxVNEU5J1iduNMtFeqWOw-58adpWgGY7SzNTfmqCmjT3Ft_E5ZclUMwwFXEBxRBKTW6T6KjWCbRYiyeXECPAX_js1awx8JZBrvBYmjh8UVlMlW8gzT02Va0dTwtZT4Xyw-Hd9T5t-W35JytHwpsYcjAkGoHLRlN8qdIiWeDkQ-97mhOAQrzq3mfik5RP00nAXVVMs6-1cQAQpTmGoqWSqvXjoI3vFIwWSw5uQO4eyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a2972407f9.mp4?token=ZLnFgNPIj2a2rl1gtI_WFkOvDuSOuL4fqYlzurjbCND6KKQZvnjysYKDpl47ljDyLAOvZY6GLsbOzRdZn45bo9jg8kzwD-XPO-RJwjdhfhrTbxVNEU5J1iduNMtFeqWOw-58adpWgGY7SzNTfmqCmjT3Ft_E5ZclUMwwFXEBxRBKTW6T6KjWCbRYiyeXECPAX_js1awx8JZBrvBYmjh8UVlMlW8gzT02Va0dTwtZT4Xyw-Hd9T5t-W35JytHwpsYcjAkGoHLRlN8qdIiWeDkQ-97mhOAQrzq3mfik5RP00nAXVVMs6-1cQAQpTmGoqWSqvXjoI3vFIwWSw5uQO4eyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">أسراب المسيرات تعاود إجتياح سماء السليمانية</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/naya_foriraq/83754" target="_blank">📅 01:57 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83753">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🇮🇷
الحرس الثوري:
قبل ساعة، انفجرت واشتعلت بالنيران سفينتان نفطيتان كانتا تحاولان عبور مسار ميني في جنوب مضيق هرمز، بعد أن تعرضتا لخداع من قبل منظمات التجسس الأمريكية.
🔹
البحرية التابعة لحرس الثورة الإسلامية تعلن بصرامة أن مضيق هرمز شديد الخطورة وغير آمن بسبب جرائم الجيش الأمريكي الذي يقتل الأطفال، وهو مغلق تمامًا. طالما أن تجاوزات أمريكا الإجرامية مستمرة، فإنه لا يمكن تصدير أي كمية من الأسمدة أو حتى قطرة واحدة من النفط والغاز من هذه المنطقة.
يجب على السفن ألا تقع في فخ الخداع، وأن تحافظ على أصولها، والأهم من ذلك، على أرواحها، وألا تدخل المسار الميني.</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/naya_foriraq/83753" target="_blank">📅 01:25 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83752">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">انفجار في جزيرة قشم جنوبي إيران</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/naya_foriraq/83752" target="_blank">📅 01:23 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83751">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">انفجارات في بندرعباس جنوبي إيران</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/naya_foriraq/83751" target="_blank">📅 01:10 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83750">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">أسراب المسيرات تعاود إجتياح سماء السليمانية</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/naya_foriraq/83750" target="_blank">📅 01:10 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83749">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/naya_foriraq/83749" target="_blank">📅 01:08 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83748">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/naya_foriraq/83748" target="_blank">📅 01:08 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83747">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b035495f0f.mp4?token=trO0amckmN1FLmlZ25dx3CAaZC71hXPxgx5uKYTorawqDk-eAiqjNu2yVdxyp8XjFhJ922vYvacQiqvckkPHBk3Am3hvjROerM9V1COToGwIocS7HdyUO51mAWDFRSvEoLaRWtf_JDBeIjz0OnpBFEZa7E75An0TyINamGHtbQYJdggwSZQP36Boqz5RYYUO_HG4k6yUq957mf7G9OW4L2hmIRBwqjOWhm6itVwgsFskIgoxKyhgKC1rIjq_jpFLFVcMApH7fhRME0KlurFsNeH_I-mmncygEVPmRw_MGUqx5DwqTDD_shdSZkFgOoXlNYHblmyRXFxPjkIeNMYgKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b035495f0f.mp4?token=trO0amckmN1FLmlZ25dx3CAaZC71hXPxgx5uKYTorawqDk-eAiqjNu2yVdxyp8XjFhJ922vYvacQiqvckkPHBk3Am3hvjROerM9V1COToGwIocS7HdyUO51mAWDFRSvEoLaRWtf_JDBeIjz0OnpBFEZa7E75An0TyINamGHtbQYJdggwSZQP36Boqz5RYYUO_HG4k6yUq957mf7G9OW4L2hmIRBwqjOWhm6itVwgsFskIgoxKyhgKC1rIjq_jpFLFVcMApH7fhRME0KlurFsNeH_I-mmncygEVPmRw_MGUqx5DwqTDD_shdSZkFgOoXlNYHblmyRXFxPjkIeNMYgKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تفعيل منظومة الباتريوت الامريكية مجددا في سماء محافظة أربيل</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/naya_foriraq/83747" target="_blank">📅 01:02 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83746">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">انفجارات في محافظة اربيل</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/naya_foriraq/83746" target="_blank">📅 00:57 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83745">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c436c7643b.mp4?token=Z-_VQd7-ic2fBTqcjRAWLOsYKoFODkHE_f-qg-fLTPLOzOYEzrr5XAcVfoWerh-GHucARH_K13mEhHqoorrrmoQikpJAo7jZ7dh7cnaev1XsT6AbyepJEQMuPCiLBKMIACbJdxICK2ooIEDX6yhpDNlbrjkKhiHJRC1rYafy8aTZe4NRAZYGCMdd5s7cYNlY-4PEmrftBdIiypxfPrr0PBHIpO58RiC9PkKEDVEfDv2kX-0XDjinn3OfDbZdf13yEm-JfzUstjqRt3fPEsuryfImjkj0QKhRlEZzoNLf0BEGMExUlg8Wzo0S_e4leS1J-F_fKC1bCwscgEEM2lI_Iw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c436c7643b.mp4?token=Z-_VQd7-ic2fBTqcjRAWLOsYKoFODkHE_f-qg-fLTPLOzOYEzrr5XAcVfoWerh-GHucARH_K13mEhHqoorrrmoQikpJAo7jZ7dh7cnaev1XsT6AbyepJEQMuPCiLBKMIACbJdxICK2ooIEDX6yhpDNlbrjkKhiHJRC1rYafy8aTZe4NRAZYGCMdd5s7cYNlY-4PEmrftBdIiypxfPrr0PBHIpO58RiC9PkKEDVEfDv2kX-0XDjinn3OfDbZdf13yEm-JfzUstjqRt3fPEsuryfImjkj0QKhRlEZzoNLf0BEGMExUlg8Wzo0S_e4leS1J-F_fKC1bCwscgEEM2lI_Iw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاهد متداولة لإنفجار في مدينة لار الإيرانية</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/naya_foriraq/83745" target="_blank">📅 00:56 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83744">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">انفجارات في محافظة اربيل</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/naya_foriraq/83744" target="_blank">📅 00:56 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83741">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bbd34a1aa8.mp4?token=GMyDjt3jLNSl1x8AzVa00RbuTFZdldyRbNCpP4O-pMP6UKZ0aifhAtZaHCHR_Tz7JMMpsF9gtoZLRIsYuQD5bLIokwzNjc9pHW_maWjSfOIbvYujLw5chi5O-IYjrhfoZGWNw9S9jA5_xNNRwHqE-Uf2X2MlscYXbYnVTNkSs_Y7Abd6pw3n6cfmqk28cEmXO56xbRzz0qmfYG5KWG0urP_QzQpPX5-_DRulsRVGfLX4gd5B32CfoXJPnW1OMZjH43LaOCKSEgIJNjxPWaSDYlwLzOFs0SDy2W-MrVOnc39x9t6Z8a6q_hWXPXBS_dPJ__9MYvw54N_sWKUxa5LmVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bbd34a1aa8.mp4?token=GMyDjt3jLNSl1x8AzVa00RbuTFZdldyRbNCpP4O-pMP6UKZ0aifhAtZaHCHR_Tz7JMMpsF9gtoZLRIsYuQD5bLIokwzNjc9pHW_maWjSfOIbvYujLw5chi5O-IYjrhfoZGWNw9S9jA5_xNNRwHqE-Uf2X2MlscYXbYnVTNkSs_Y7Abd6pw3n6cfmqk28cEmXO56xbRzz0qmfYG5KWG0urP_QzQpPX5-_DRulsRVGfLX4gd5B32CfoXJPnW1OMZjH43LaOCKSEgIJNjxPWaSDYlwLzOFs0SDy2W-MrVOnc39x9t6Z8a6q_hWXPXBS_dPJ__9MYvw54N_sWKUxa5LmVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاهد اخرى لقاعدة الحرير الاميركية في محافظة اربيل شمالي العراق وهي تحترق بعد استهدافها بالمسيرات.</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/naya_foriraq/83741" target="_blank">📅 00:53 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83740">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tPOKvjJMzl7IoDOYcAVdfgDiGJGNYSnHs8OyaaBI1zTfB4PRdEa0PaXCfhpN5YBI8rbOsLoOBGuTBOc73arunzdIau1jR5YMy9UMGlU7ghpESOH1_FQTI7hd32MCpBGpCB2wCBXTqE42bQ5USbghW5K-JOuWQz5BA-3ndadOf2oUXvqO0GK_Ib66pmjISnNHdGuxL60MGKWNDiClMDe49r-qFsmJ8lpC0JSK-eH2rkcI9HCjUZVN27pFQIBTk3JCPPWWRY3hkLB_HZJzPh_FDNwGIK5EDouoOoNOZ_uaNDIkyT-X84iASW82d6FrJBUXIlcy_ZquDUaq0qtaux_eTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
عضو المكتب السياسي لأنصارالله "حزام الأسد":
يتحمل النظام السعودي، عميل أمريكا، تبعات التلوث البيئي الذي سينتج عن اشتعال الآبار، وخطوط النقل، والصهاريج والمصافي، وموانئ التصدير، والمحطات، ومصانع البتروكيماويات.. والذي سيرى سكان المنطقة أدخنته ولهيبه.</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/naya_foriraq/83740" target="_blank">📅 00:51 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83739">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">مصدر إيراني: لا يوجد نشاط للدفاعات الجوية في أصفهان.</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/naya_foriraq/83739" target="_blank">📅 00:48 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83738">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/68ce7f38bb.mp4?token=u7hxomHyBGjwVuekpvPcKj8_pQohpd1YHACFmSPDA0BlVuRQ6Ww23baAPJCn9HzDhVaLbEbcElR3StUKrCB295oydfyXq92UeDibFZaZxAcdb5esc4XCnA1r5YDklZf64DIK_2ApvQHWHqULq-yV-hvga1TehS-_qVqLniYRvpw3KrySO_qokBwCkeb8WRfA7GhfLtLtG_UN2SQN1wqbOcEvlW1kuNez0HYOkBoYiVdsphF_AGhvtzToLsZyMiYCApgQQ-qDUZG-qmnSRrb2BA9YH-EkBT9YbZkFRkcd_TNAiTkx55eC68OmZLCvIFmhd7P-8K21H8fF-w3MRmdNnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/68ce7f38bb.mp4?token=u7hxomHyBGjwVuekpvPcKj8_pQohpd1YHACFmSPDA0BlVuRQ6Ww23baAPJCn9HzDhVaLbEbcElR3StUKrCB295oydfyXq92UeDibFZaZxAcdb5esc4XCnA1r5YDklZf64DIK_2ApvQHWHqULq-yV-hvga1TehS-_qVqLniYRvpw3KrySO_qokBwCkeb8WRfA7GhfLtLtG_UN2SQN1wqbOcEvlW1kuNez0HYOkBoYiVdsphF_AGhvtzToLsZyMiYCApgQQ-qDUZG-qmnSRrb2BA9YH-EkBT9YbZkFRkcd_TNAiTkx55eC68OmZLCvIFmhd7P-8K21H8fF-w3MRmdNnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">من الانفجارات العنيفة في مقرات المعارضة الكردية بمحافظة السليمانية شمالي العراق</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/naya_foriraq/83738" target="_blank">📅 00:46 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83737">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bab1e4a863.mp4?token=m4b-OmP0AL_-FA5q7Q0rMsPYdrqfMnannmkuwJOdfy3JWovV5L7g7qDOf41cQ28-__fzquPT7RA8kKHQItBazmWvKlT73YvIjOIQOBCajnQBxIOpOzN3RsPdFrvViAo2RR7-6q3L77t9k6FfyXgOWGA8g_DirCvEz7-RsTMP-FV9iknWcQgyoiIW1BiSel2wCI9VaNF5_v01Rl2fr1r8wcLYjRmrdV9QABJ-x_xa8K3AmaWFOQj8_XznP05rKRJyP9ccTHMDVc1Y3eUibuYnV3PI1lUH2VLTz8x6HALgVoJRqeKu5D4yCxHFKAN5EE86FPfcFlJJ--IWQ91vZvk8Hw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bab1e4a863.mp4?token=m4b-OmP0AL_-FA5q7Q0rMsPYdrqfMnannmkuwJOdfy3JWovV5L7g7qDOf41cQ28-__fzquPT7RA8kKHQItBazmWvKlT73YvIjOIQOBCajnQBxIOpOzN3RsPdFrvViAo2RR7-6q3L77t9k6FfyXgOWGA8g_DirCvEz7-RsTMP-FV9iknWcQgyoiIW1BiSel2wCI9VaNF5_v01Rl2fr1r8wcLYjRmrdV9QABJ-x_xa8K3AmaWFOQj8_XznP05rKRJyP9ccTHMDVc1Y3eUibuYnV3PI1lUH2VLTz8x6HALgVoJRqeKu5D4yCxHFKAN5EE86FPfcFlJJ--IWQ91vZvk8Hw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
محاولة الإسقاط طائرة مسيرة في محافظة السليمانية بصاروخ باتریوت، إلا أن المحاولة باءت بالفشل ما أدى إلى سقوط الصاروخ داخل ملعب خماسي</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/naya_foriraq/83737" target="_blank">📅 00:45 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83736">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">دوي انفجار في الاهواز جنوبي إيران</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/naya_foriraq/83736" target="_blank">📅 00:36 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83735">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/914da55464.mp4?token=nucNkP4BQvpFEOmtadiCH0KKjkt0JlObEUEE2r0oLE_8iM2HYpdqeGeNQ6rEZGMGuukCTr3rhl1SN-j8Cc94F5n69Kxf4rSTYvcTBKWQ6dP-4ORO1FjgD2lt5AzBZCbPBWWmnv_yagSoSJKjxQfhYwAKvkl4gn-l0uEaMPEYxTYjmb4gSmt-b6gsru9MpZXqqu7r5QsZVu_wbEpLqzF67RMWCE3BwUY2Y2BQJGikuubcbHhs38jQDLQUAsRKROZxqDwSSkB3cNRZ003_PuY8OqyfsBUBU7d_qyb8oa4jS2MadAZeeMVAf2bIPpNdSYNGByYkxNvxGGPZp3-atmPX3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/914da55464.mp4?token=nucNkP4BQvpFEOmtadiCH0KKjkt0JlObEUEE2r0oLE_8iM2HYpdqeGeNQ6rEZGMGuukCTr3rhl1SN-j8Cc94F5n69Kxf4rSTYvcTBKWQ6dP-4ORO1FjgD2lt5AzBZCbPBWWmnv_yagSoSJKjxQfhYwAKvkl4gn-l0uEaMPEYxTYjmb4gSmt-b6gsru9MpZXqqu7r5QsZVu_wbEpLqzF67RMWCE3BwUY2Y2BQJGikuubcbHhs38jQDLQUAsRKROZxqDwSSkB3cNRZ003_PuY8OqyfsBUBU7d_qyb8oa4jS2MadAZeeMVAf2bIPpNdSYNGByYkxNvxGGPZp3-atmPX3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجارات في مدينة يزد الإيرانية</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/naya_foriraq/83735" target="_blank">📅 00:33 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83734">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e7e4e699ab.mp4?token=XMIYbE9QHDmSGJgw6Xcpp0Dy0ZEXyAHZ580QvkLtN8NDcB5KQ8stDQMIpJmry9myAQ393sD9hGldoYhi_P926BnDMTicM1rheP66iZ8a2wgI3HjkiJLetHMGfV3bSr6IvibT-k0WR3PAFsQb4F76_2C95VVmQ9k520OdXBqjInxnujFboZgiwES6UJFj9-_9M3Bkog70DLNW-J6m_3w8weCPFRvnnTrvLqf5Qca2hnR5FdSmY8fiYAfwaR3C9jGaG5w-Nn_gSLTC8-ozzX91gjQFVUDvr9fJuKdUkV0J2CAcG1oKEGXM10baIWrckWwwzDQzNonh4w0eWWdBnfzXyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e7e4e699ab.mp4?token=XMIYbE9QHDmSGJgw6Xcpp0Dy0ZEXyAHZ580QvkLtN8NDcB5KQ8stDQMIpJmry9myAQ393sD9hGldoYhi_P926BnDMTicM1rheP66iZ8a2wgI3HjkiJLetHMGfV3bSr6IvibT-k0WR3PAFsQb4F76_2C95VVmQ9k520OdXBqjInxnujFboZgiwES6UJFj9-_9M3Bkog70DLNW-J6m_3w8weCPFRvnnTrvLqf5Qca2hnR5FdSmY8fiYAfwaR3C9jGaG5w-Nn_gSLTC8-ozzX91gjQFVUDvr9fJuKdUkV0J2CAcG1oKEGXM10baIWrckWwwzDQzNonh4w0eWWdBnfzXyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجار مهيب در یکی از مقر‌های تروریست‌های تجزیه طلب در شمال عراق</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/naya_foriraq/83734" target="_blank">📅 00:31 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83733">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9dd4636b92.mp4?token=aultytX1J0hxbfz8LTl4p57lrtYydeE9vnKw0Wmps4W2LTl8p3k-vpyMr35mVyjR4H3nKDj-m867hXM7ptJUbtoqWcOJ6KbOjN_UijHL1zxShIOzb5_AxEpF1BF5S165Cykuci0r4R7BifDl13LFzYHQymYR_g75wA58MuFREbDaNP1XRlXxxmKDaL3OVieJEwwbQq08qbBqy5LoUKqRHhFiYC0UnmGAN9_WaoT0CYjQupMgNOQG6ojOnPtN6KFjy6gDonfzOfdBea2iZEtu5MWcLQltSK6fKDRe6yKjGeiqmBqW2zLzxUwJqOGhlhoiidKNZ5KtFPxiZCXzDL1qww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9dd4636b92.mp4?token=aultytX1J0hxbfz8LTl4p57lrtYydeE9vnKw0Wmps4W2LTl8p3k-vpyMr35mVyjR4H3nKDj-m867hXM7ptJUbtoqWcOJ6KbOjN_UijHL1zxShIOzb5_AxEpF1BF5S165Cykuci0r4R7BifDl13LFzYHQymYR_g75wA58MuFREbDaNP1XRlXxxmKDaL3OVieJEwwbQq08qbBqy5LoUKqRHhFiYC0UnmGAN9_WaoT0CYjQupMgNOQG6ojOnPtN6KFjy6gDonfzOfdBea2iZEtu5MWcLQltSK6fKDRe6yKjGeiqmBqW2zLzxUwJqOGhlhoiidKNZ5KtFPxiZCXzDL1qww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجار في مدينة لار بمحافظة فارس الإيرانية</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/naya_foriraq/83733" target="_blank">📅 00:25 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83732">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd64a5c717.mp4?token=CZ5MxCNJbHCJxwMfWUh-VPleqkublbzRDGfWcV_Hs_o3R5sjTUg9BzlfGzEEBpGnghlk3BNQ9YHfunk86m4FqYPdD-4aZ-lVKatwVczBorrS-8DfebeMtYh482iBsAZzWT8W6NfPEtIvTlG6gyx6-gvJu-daKMX-Self_gRKOL7zFo-A3qeFrqc07tjRMGYXicZn_D-OYQmGb8i7b7eckdmlUzlyNWXbm3tCREdjcocH5myXZtNGqPokmTSoQ3u-ZQHn2MYBvblMeGTnoQjP4tqIafjcYQVeGHrsect65sE_7LWLJCgPDLi81aXhc9QXQHDoHvLHPGKOa8KukCMAhw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd64a5c717.mp4?token=CZ5MxCNJbHCJxwMfWUh-VPleqkublbzRDGfWcV_Hs_o3R5sjTUg9BzlfGzEEBpGnghlk3BNQ9YHfunk86m4FqYPdD-4aZ-lVKatwVczBorrS-8DfebeMtYh482iBsAZzWT8W6NfPEtIvTlG6gyx6-gvJu-daKMX-Self_gRKOL7zFo-A3qeFrqc07tjRMGYXicZn_D-OYQmGb8i7b7eckdmlUzlyNWXbm3tCREdjcocH5myXZtNGqPokmTSoQ3u-ZQHn2MYBvblMeGTnoQjP4tqIafjcYQVeGHrsect65sE_7LWLJCgPDLi81aXhc9QXQHDoHvLHPGKOa8KukCMAhw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجار مهيب در یکی از مقر‌های تروریست‌های تجزیه طلب در شمال عراق</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/naya_foriraq/83732" target="_blank">📅 00:24 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83730">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f61c9d6284.mp4?token=FFqblqZAhNgQZAUrPDH2w0jusIS_FANCvyyKsnotP7_SZqYufEiUjW4f-b0H34VJuwDlx6IFZ-zswXS8xt2DWsXYgsHARs7qj0qwBridVB1tSS0sYOUMC8nkPAa8AqEEZ5tIVCdl7AiT4RoXzhb2yxNkWlUfoACst7hvdQHIVEJHEECkwUlwMHF1TBQ6XK4Bxl9Li__O3ONwN4sjcFJB5JS08emY-_asogjdWWEndpqdYPJPoBLfI1H844Hk5hmudzI1G_0s_iP3DgrRghM5zvGnkRh-2lHoAJhjI_ZWt1T5gIWS9YR75QOoMDKK3GySwYg6LkS8boZfcDZNBWfr6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f61c9d6284.mp4?token=FFqblqZAhNgQZAUrPDH2w0jusIS_FANCvyyKsnotP7_SZqYufEiUjW4f-b0H34VJuwDlx6IFZ-zswXS8xt2DWsXYgsHARs7qj0qwBridVB1tSS0sYOUMC8nkPAa8AqEEZ5tIVCdl7AiT4RoXzhb2yxNkWlUfoACst7hvdQHIVEJHEECkwUlwMHF1TBQ6XK4Bxl9Li__O3ONwN4sjcFJB5JS08emY-_asogjdWWEndpqdYPJPoBLfI1H844Hk5hmudzI1G_0s_iP3DgrRghM5zvGnkRh-2lHoAJhjI_ZWt1T5gIWS9YR75QOoMDKK3GySwYg6LkS8boZfcDZNBWfr6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فرزندان "ایران زمین" در حال لت و پار کردن تجزیه طلب‌های تروریست هستند</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/naya_foriraq/83730" target="_blank">📅 00:18 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83729">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">انفجار في مدينة لار بمحافظة فارس الإيرانية</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/naya_foriraq/83729" target="_blank">📅 00:15 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83728">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">ارتفاع النيران من وسط مقرات المعارضة في محافظة السليمانية شمالي العراق</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/naya_foriraq/83728" target="_blank">📅 00:13 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83727">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63eaf1d224.mp4?token=SwGwY0KZXRHOOZIQsApnR0DL65IYHkgIQG9YVlD9nVdaqcIOsHtzFqHf9WbfWP5_xhvVxmV9yxKEHnON8Gz7k4AZAkefbczA1kNNJ8RmC1hQ5cUEkcCE5MAHP53nvhp6EZl3Su-J7Fqoxwi47uS1X8VQqSzW6ngqO06S5fwMpP_57ws1wC0pHnxQ2EhkPpsgBCc3dF6gx5Y2S1A4To3GaqDVMcV1lOjG6DXdKNthFFe4stEAnrFX2oQv1JP6am9JrQiqSRQO6X_O4uFAekBtQcq-HRjzZnNoQ15jys5frHOfEUGI3m3V_mH9Kup7gB6atE9cE4KJCWdr5ay4n3rjmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63eaf1d224.mp4?token=SwGwY0KZXRHOOZIQsApnR0DL65IYHkgIQG9YVlD9nVdaqcIOsHtzFqHf9WbfWP5_xhvVxmV9yxKEHnON8Gz7k4AZAkefbczA1kNNJ8RmC1hQ5cUEkcCE5MAHP53nvhp6EZl3Su-J7Fqoxwi47uS1X8VQqSzW6ngqO06S5fwMpP_57ws1wC0pHnxQ2EhkPpsgBCc3dF6gx5Y2S1A4To3GaqDVMcV1lOjG6DXdKNthFFe4stEAnrFX2oQv1JP6am9JrQiqSRQO6X_O4uFAekBtQcq-HRjzZnNoQ15jys5frHOfEUGI3m3V_mH9Kup7gB6atE9cE4KJCWdr5ay4n3rjmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هجوم جديد دك مقرات المعارضة الكردية في السليمانية شمالي العراق</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/naya_foriraq/83727" target="_blank">📅 00:10 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83726">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🇮🇷
الحرس الثوري:
في الموجة السابعة عشرة من عملية "النصر 2" تحت الشعار المبارك "يا صاحب الزمان، أدركني"، تم في فجر اليوم تدمير منصة طائرات الاستطلاع الأمريكية (الطائرات بدون طيار) في البحرين، واشتعلت فيها النيران.
🔹
بالإضافة إلى ذلك، تم تدمير بالكامل مركز الذكاء الاصطناعي الرئيسي في البحرين، والذي كان يستخدمه "الشيطان الأكبر" في استهداف العدو لارتكاب جرائم حرب، وذلك عن طريق عدة صواريخ باليستية وأكثر من عشرات الطائرات بدون طيار.</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/naya_foriraq/83726" target="_blank">📅 00:09 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83725">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">انفجارات في سليمانية</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/naya_foriraq/83725" target="_blank">📅 00:07 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83724">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">انفجارات في سليمانية</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/naya_foriraq/83724" target="_blank">📅 00:06 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83723">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">انفجارات في سليمانية</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/naya_foriraq/83723" target="_blank">📅 00:04 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83722">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">النيران تحرق مقرات الاحزاب المعارضة بعد استهدافها بالطيران المسير بمحافظة اربيل شمالي العراق</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/naya_foriraq/83722" target="_blank">📅 00:02 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83721">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/753518dea0.mp4?token=ppiopVNJ6Pdx9lMfxmovtBs0wSeqmGmqX-FP-hEAR5oxQI_HBAnDTdDaEeg39KPbcTcrJ3kMkq9KAyQELuCa8zz9m5dVWYRI_tE7AC6CuBSdKUTcaEN_KAfk_uucGWbK4ktt4AbovXPqjb7g-GuZtqnoQYmqkWMYYnU4afShIBVzSxcZ1pR4mH4vHuXuYovmxcRo3OUhHtEgU7i3YZFI2MzCVW90YR9FoQa2WPLtY-qww6ftf9BvhSraiSFvkwL88EQs5dIlubCml6lSVv-erWfi9FZBKOKz07DZaAY-p7Wjhojqf6gwInH-jm-Po0WRqtO8K-NR0VZ2_UUETcddfg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/753518dea0.mp4?token=ppiopVNJ6Pdx9lMfxmovtBs0wSeqmGmqX-FP-hEAR5oxQI_HBAnDTdDaEeg39KPbcTcrJ3kMkq9KAyQELuCa8zz9m5dVWYRI_tE7AC6CuBSdKUTcaEN_KAfk_uucGWbK4ktt4AbovXPqjb7g-GuZtqnoQYmqkWMYYnU4afShIBVzSxcZ1pR4mH4vHuXuYovmxcRo3OUhHtEgU7i3YZFI2MzCVW90YR9FoQa2WPLtY-qww6ftf9BvhSraiSFvkwL88EQs5dIlubCml6lSVv-erWfi9FZBKOKz07DZaAY-p7Wjhojqf6gwInH-jm-Po0WRqtO8K-NR0VZ2_UUETcddfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لحظة انقضاض المسيرة على احد مقرات المعارضة في محافظة اربيل شمالي العراق</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/naya_foriraq/83721" target="_blank">📅 23:59 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83720">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/41b6019723.mp4?token=Xt5LNwJSsavwHuPEivzxs-Q_qGYCCSRI7ScdXYo52wSTuKF8XKPgHwaVkNnc1slDDp8JD9RAYWRQWUs9sF_zMzSjEXYihksmp3tpoGMWCkCbZdddEFtttwj8Ct7qTdT7vyRy0l4g_FaT-i9_BvdqeAewiFAgCUKqC1S-JVHo03LTctEvvf3UTxpVBgZvWp743wSG4hVVYgQ0UhcABk4kkBCaYsT3Y4wIEcqV1gQiQDDKzYI541J7kha2LGD94Vafj3OlSUtQcLxjjfVbASTTPx5gv5hbRX0I1iGfCInfUblMK46C1ruBpY_dH-HwQ_33FCeeL78-iAThtXHXdMw6KA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/41b6019723.mp4?token=Xt5LNwJSsavwHuPEivzxs-Q_qGYCCSRI7ScdXYo52wSTuKF8XKPgHwaVkNnc1slDDp8JD9RAYWRQWUs9sF_zMzSjEXYihksmp3tpoGMWCkCbZdddEFtttwj8Ct7qTdT7vyRy0l4g_FaT-i9_BvdqeAewiFAgCUKqC1S-JVHo03LTctEvvf3UTxpVBgZvWp743wSG4hVVYgQ0UhcABk4kkBCaYsT3Y4wIEcqV1gQiQDDKzYI541J7kha2LGD94Vafj3OlSUtQcLxjjfVbASTTPx5gv5hbRX0I1iGfCInfUblMK46C1ruBpY_dH-HwQ_33FCeeL78-iAThtXHXdMw6KA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الله اكبر  اصابة مباشرة لمسيرة انتحارية على مقر إرهابيي المعارضة الكردية الإيرانية في محافظة أربيل شمالي العراق.</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/naya_foriraq/83720" target="_blank">📅 23:54 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83719">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">الله اكبر
اصابة مباشرة لمسيرة انتحارية على مقر إرهابيي المعارضة الكردية الإيرانية في محافظة أربيل شمالي العراق.</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/naya_foriraq/83719" target="_blank">📅 23:53 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83718">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🇮🇷
دوي انفجارات في بوشهر وقشم وسيريك جنوبي إيران.</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/naya_foriraq/83718" target="_blank">📅 23:48 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83717">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MgoP5Z1HWHICVkzckfYnfhzQoxXocRMoR0MpNTGr__wk4wiKjVVmaxd2LYkcW_56pKl7fGP-6w6AR3_VMP9sdzVqC_aBBnpSNWj_dpNYNhVChL_HuZUjo10BQf-L45ggPiuabF5Sx95BWHR3yQrRCMmaCwXFI_RobevxOJlxUl5Tt6mQQUy_Brzs5lHw4fVh2xprAz6vbTIpT8NvhmgqN_SFVycT8wIQIBlrHljPCFiFncPWE3nFGtrUq41r5v97wnTq_9_xESMp8wo5J0RZCwqJcUvPA1tFUf5jo3aNgHETXPETADN_Ms4lL5it4fnI0i5_AjfLUIXmYH1Xm4SG4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">من مرتفاعات خليفان التي تتواجد فيها قواعد الاحتلال الاميركي بمحافظة اربيل شمالي العراق.</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/naya_foriraq/83717" target="_blank">📅 23:46 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83716">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af37c54961.mp4?token=f-mRowLSgUq1O_yUom3Nw4a0o6JHbrL732OymiYrR3ZtkHmvBDo5QSSJ-PfMte9HhKS1fKLpVVF2VM2gLSQUXbBJ3zjqYAHznwcSTTChnm5UiDqBrs550VAwXMM7woocTFUSQN7pqdMUvcJF5fBr99fy3mbwimkWMT-5qTaKPDex6zpPmevDVMY_09m97bOCgxapiCMClHSih6CWQ8fPINEv1xUbi4j04y2zANGhFJfvWPxmWs3daN1avExWJmTCsvA1f0PwJTNPcTUx-uy8hY0Bd2hQsVNjTHnYstIm8ZisqRqXtPxA0KbFiTEwN5GwMNMmm84l4Zors7qoJnjvJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af37c54961.mp4?token=f-mRowLSgUq1O_yUom3Nw4a0o6JHbrL732OymiYrR3ZtkHmvBDo5QSSJ-PfMte9HhKS1fKLpVVF2VM2gLSQUXbBJ3zjqYAHznwcSTTChnm5UiDqBrs550VAwXMM7woocTFUSQN7pqdMUvcJF5fBr99fy3mbwimkWMT-5qTaKPDex6zpPmevDVMY_09m97bOCgxapiCMClHSih6CWQ8fPINEv1xUbi4j04y2zANGhFJfvWPxmWs3daN1avExWJmTCsvA1f0PwJTNPcTUx-uy8hY0Bd2hQsVNjTHnYstIm8ZisqRqXtPxA0KbFiTEwN5GwMNMmm84l4Zors7qoJnjvJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محاولة الإسقاط طائرة مسيرة في قضاء خبات من قبل الانفصاليين في محافظة أربيل شمالي العراق.</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/naya_foriraq/83716" target="_blank">📅 23:43 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83715">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BNYmcRbtfIz6wWCFXovjIf_XOWlAyLNmAN8cL9qAuVyLW0k5Sg4SApYaRus2bFBbIzy-04jz7hMQbuk-nulk179qD0xMoYHQKxxwwE6Pnn8WOAQDSP8VKV7sWuJmuS7uKVbBegwzkTWQI4AKJ6xGLIr9wDT9I3GEPUWFqwGbIYbFTiHRN1oyVh9joF9ifVInBqcPuaoa6i2vTj1eeYkBNrjeZmGacS4HcJgcqYQ2enqZk2w7b0DL799oxiMFXAYZ8RZYzuBPQvV_MZGYPRtrfQdJ9SjsV0FVvVG0BkubHhgAnvqVKB67JMszBLFMOJxBewFe03SIbGXUuEP5QtqfFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قاعدة الحرير في محافظة اربيل شمالي العراق تحترق</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/naya_foriraq/83715" target="_blank">📅 23:41 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83714">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🇮🇷
دوي انفجارات في بوشهر وقشم وسيريك جنوبي إيران.</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/naya_foriraq/83714" target="_blank">📅 23:33 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83713">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dca765a6f9.mp4?token=dihTA0Ni3ylVNqJs7ClgHbf7ezPN1SRIkLqyH_rQGGooOG9AMNmW69NwUvpTQGD2sR_U56d2U3DLKE4b34YT6vmmSl9S2wdZuQziBspBc4q2oZ-SKqIQaVXEL3aFw5RjUL0aSG266ihfISJhFV_7QukGax-azPd47jDm2FO9-nmlyy-SawyBBC1v8j2cM5ROXkVBXgwebBw9uc51lxHJi4RFZ8lmr01NRJuB5xpBVrbymV09kmPk0t-XJqN0FH7y32COxqzUcRvhCnu-_8j5uiwYYWU8_c8h51M6hkHptJ89F7Zr9TokHLwU6Mqrs29igCFoUBBPodhtrvakS5S__Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dca765a6f9.mp4?token=dihTA0Ni3ylVNqJs7ClgHbf7ezPN1SRIkLqyH_rQGGooOG9AMNmW69NwUvpTQGD2sR_U56d2U3DLKE4b34YT6vmmSl9S2wdZuQziBspBc4q2oZ-SKqIQaVXEL3aFw5RjUL0aSG266ihfISJhFV_7QukGax-azPd47jDm2FO9-nmlyy-SawyBBC1v8j2cM5ROXkVBXgwebBw9uc51lxHJi4RFZ8lmr01NRJuB5xpBVrbymV09kmPk0t-XJqN0FH7y32COxqzUcRvhCnu-_8j5uiwYYWU8_c8h51M6hkHptJ89F7Zr9TokHLwU6Mqrs29igCFoUBBPodhtrvakS5S__Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاهد تُظهر مقذوفات حربية متناثرة عقب قصف استهدف مقرات للمعارضة مع سقوط أجزاء منها على منازل مدنيين.</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/naya_foriraq/83713" target="_blank">📅 23:30 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83712">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/naya_foriraq/83712" target="_blank">📅 23:29 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83711">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v26zPrdTaBWcdqvVnQf4Wg_7sbry0eSvIT4hjUdCYb6_2e35jFROADH0eLcSbiBL_7I3kexb5s-eg7y8a-bpLdVIGNx3h5XyiEP0TQtd-TVC_ZPaVtofueI48GyxAFFlKAGwb7qsLF2LU1sEtRICgGTnTRPPngbVTgU9pI6ePk1cvy0U0ZO8FbIEWWKx5mwv65zayPeDyP2Iw5Yt6wv6J00lKReZl_OiSGnySXktt07U9B699p5yBk9yUWrjeJqwgpo2v6eogpe3JKytareLwguBPwcQlsfbnrhnHzgwQs2zYAdzx7fHAIlH0StXBVS5dugp6z1FtE7isggwFjazhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
بعد فشل الباتريوت.. تفعيل منظومة السيرام في قاعدة الاحتلال الاميركي بمحافظة اربيل شمالي العراق.</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/naya_foriraq/83711" target="_blank">📅 23:29 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83710">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🇺🇸
سنتكوم:
‏شنت قواتنا جولة من الضربات على ايران.</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/naya_foriraq/83710" target="_blank">📅 23:23 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83709">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1d75be90d6.mp4?token=G4s1wVEaDxgOvEmMJzQVgcelizsjXpLsxaIL6K2Vy0JtQ0MXvO7kLEkH8DpiLQAUvwQdoyrYHu3t024tAcaXIN_eDenXsbF9i9UCl4Qtpb3_zgWNZFkw9B30r54NnrchFUT6vH_s77ZqtS04-N8dbqfvkAeQwFG6yiiMsm0gn6dJbkytL4fSDDjv-zTuiN117RxeqrgL7tpHOwnd7GI3KQik7Ub76G4AX0lbAQls-284KXHmdBbE2ZKyV6sJ-_3vYMUF3QycbTPKGuYHvrNuiQAxzy9F2Hxyi1xFjkUr-s8GBTDNOY97WWMjW3hVEj3R1mqlTtO7aINeHBA8j_z87Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1d75be90d6.mp4?token=G4s1wVEaDxgOvEmMJzQVgcelizsjXpLsxaIL6K2Vy0JtQ0MXvO7kLEkH8DpiLQAUvwQdoyrYHu3t024tAcaXIN_eDenXsbF9i9UCl4Qtpb3_zgWNZFkw9B30r54NnrchFUT6vH_s77ZqtS04-N8dbqfvkAeQwFG6yiiMsm0gn6dJbkytL4fSDDjv-zTuiN117RxeqrgL7tpHOwnd7GI3KQik7Ub76G4AX0lbAQls-284KXHmdBbE2ZKyV6sJ-_3vYMUF3QycbTPKGuYHvrNuiQAxzy9F2Hxyi1xFjkUr-s8GBTDNOY97WWMjW3hVEj3R1mqlTtO7aINeHBA8j_z87Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حرائق على مرمى البصر في محافظة اربيل شمالي العراق</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/naya_foriraq/83709" target="_blank">📅 23:21 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83708">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">الكويت تعترف بضرب موقعين من قبل الصواريخ الايرانية واشتعال النيران فيها</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/naya_foriraq/83708" target="_blank">📅 23:16 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83707">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dd773bd281.mp4?token=bdhddtQHaAUEBql_iB16s1tV1e9eTUZYRkFQrYNgcEbyqJF1o0_LVlvuraa6B0GhFSnq6Z9sTzSFGurxtr9lGgiv_NjBYSHqYURfczqSjn0ZSaq60dL60DSjHLCbTqAuOb-teNzvFekAkfvBwdJVhKK0BpGErIAQ5xGdU1fAxfJlQJfgNm5TkxpqdnRoty-e3xQdon8O8jl5k7y-jdnkLGNGGJAFyOQirE70JE6q4ZVHFSdMWyzVntQtRyW0pYV892tZizZkzr8Mi57FDiaE17Pu_lA1CeBonKKPuJFW5dNOQ0z3P6bMQ39mUYOQv51PWvcNKbwiHlCRI4erPncaWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dd773bd281.mp4?token=bdhddtQHaAUEBql_iB16s1tV1e9eTUZYRkFQrYNgcEbyqJF1o0_LVlvuraa6B0GhFSnq6Z9sTzSFGurxtr9lGgiv_NjBYSHqYURfczqSjn0ZSaq60dL60DSjHLCbTqAuOb-teNzvFekAkfvBwdJVhKK0BpGErIAQ5xGdU1fAxfJlQJfgNm5TkxpqdnRoty-e3xQdon8O8jl5k7y-jdnkLGNGGJAFyOQirE70JE6q4ZVHFSdMWyzVntQtRyW0pYV892tZizZkzr8Mi57FDiaE17Pu_lA1CeBonKKPuJFW5dNOQ0z3P6bMQ39mUYOQv51PWvcNKbwiHlCRI4erPncaWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاهد تُظهر مقذوفات حربية متناثرة عقب قصف استهدف مقرات للمعارضة مع سقوط أجزاء منها على منازل مدنيين.</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/naya_foriraq/83707" target="_blank">📅 23:14 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83706">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5d9b38c78d.mp4?token=mzKykHLkQb63txQPl16Q7AxbNhx58keAyRisbQGM1rz6VzREm5xf18NUUq6IWGygKlt3290rhukbq2VJ8dNbFuj75jcUDo7VouJo_PHeSHXz6DYfTbRS_8gcO5DnV1HKHXn_8rsbW9eQ4-GARUkpAPU_rzlRnIvI2sBCjEcmtWK7xkwR3kkCNJvz_b_eqQWk0xpDOoLAdAftXGRQ5EE-WQHy-7KcqxX5YghfqTB1wquE8_mx60JEQqOgrnkipdG7iiZzyYrL-ZnaQyvFLEaFqHc_W4ocAQFpdSNIDjpltHlIQOFe58eAvkF6LP0rAIjxtA8vYUWMxVdgoChzzH-KAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5d9b38c78d.mp4?token=mzKykHLkQb63txQPl16Q7AxbNhx58keAyRisbQGM1rz6VzREm5xf18NUUq6IWGygKlt3290rhukbq2VJ8dNbFuj75jcUDo7VouJo_PHeSHXz6DYfTbRS_8gcO5DnV1HKHXn_8rsbW9eQ4-GARUkpAPU_rzlRnIvI2sBCjEcmtWK7xkwR3kkCNJvz_b_eqQWk0xpDOoLAdAftXGRQ5EE-WQHy-7KcqxX5YghfqTB1wquE8_mx60JEQqOgrnkipdG7iiZzyYrL-ZnaQyvFLEaFqHc_W4ocAQFpdSNIDjpltHlIQOFe58eAvkF6LP0rAIjxtA8vYUWMxVdgoChzzH-KAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
بعد فشل الباتريوت.. تفعيل منظومة السيرام في قاعدة الاحتلال الاميركي بمحافظة اربيل شمالي العراق.</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/naya_foriraq/83706" target="_blank">📅 23:10 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83705">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/98829d79b7.mp4?token=MRUS0-Ltrybt7wpKFU_iavig9lZz1PWc6A0jENADisH3esKNZiON3wcEczrCnkBHJNo4h-f3xCPn-FS4zG-8ZbhYLroyG1rKVwkUinbQj8CKgnwrxkeHLOMIwE0E28vzaxGtIAxzFSS4iuElSDcCrpxlffOydqBy0idE0Awy-9sFdQQcwveuPHWAu8NSrhpqKPdMg-E7cOkF_--lWC6KGL05RIfRI0fluqBC3IM5tC2U2eN50zfigp9Dsuifk-YiPhklazh_ZOGoFIk3p1Sal-L-IRL-TkdCbxIwoUbsXQ0H6Knbc7600p5XdF01UOSCLBNztLqDVT7qWAw8LmU5iA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/98829d79b7.mp4?token=MRUS0-Ltrybt7wpKFU_iavig9lZz1PWc6A0jENADisH3esKNZiON3wcEczrCnkBHJNo4h-f3xCPn-FS4zG-8ZbhYLroyG1rKVwkUinbQj8CKgnwrxkeHLOMIwE0E28vzaxGtIAxzFSS4iuElSDcCrpxlffOydqBy0idE0Awy-9sFdQQcwveuPHWAu8NSrhpqKPdMg-E7cOkF_--lWC6KGL05RIfRI0fluqBC3IM5tC2U2eN50zfigp9Dsuifk-YiPhklazh_ZOGoFIk3p1Sal-L-IRL-TkdCbxIwoUbsXQ0H6Knbc7600p5XdF01UOSCLBNztLqDVT7qWAw8LmU5iA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الجيش الإيراني:
قبل ساعات، وفي المرحلة الثالثة عشرة من عملية "صاعقة"، استهدفت وحدة الصواريخ التابعة للقوات البحرية للجيش، سفينة معادية تابعة للعدو المعتدي، في شمال المحيط الهندي، بصاروخ كروز أُطلق من الشاطئ إلى البحر.
أدى إطلاق صاروخ كروز من قبل القوات البحرية للجيش إلى إثارة الخوف والرعب لدى العدو، وإبعاد السفينة المعادية عن مرمى جنود هذا القطاع الشجعان.</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/naya_foriraq/83705" target="_blank">📅 23:09 · 26 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
