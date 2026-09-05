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
<img src="https://cdn4.telesco.pe/file/pN92NQ0T26amhuP1boo27BF9terOd49sZsj359y8-SBbR_RTkx6DMeCssEBkfokW2n9wqpq6zLLbpTCrmDMM8DFE-VPvVppJZ3SxavpIgtlGqkRn1dB3qi6fVlFn0DIWTAkXSflUIZLqFyNfZ6LiND6aMhvwKvvNntUieLnq8NIBNHv9zWO5GJ32I9Ob72VwitZJdiuK6eL6i60INtO44iNqEjWSLzZxzxTkFcz9anIMQOG2DOtb4BW95wv9pIf4hvf7gQDnOSwmlHQREBCl0RVNSv9jfnADtBwb_nf2NnVs9yc3ZMfoxowo4QjQL9oqE9gKQgdAmE0qC5ZuMzFdmQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 268K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-14 14:49:11</div>
<hr>

<div class="tg-post" id="msg-89413">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">نتن ياهو يزعم احباط عملية لاغتيال نجله</div>
<div class="tg-footer">👁️ 1 · <a href="https://t.me/naya_foriraq/89413" target="_blank">📅 14:49 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89412">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">نتن ياهو: لقد هاجمت قطر - كما قمت بقصفها وهاجمتها خلال الحرب، وهم هاجموني. كل هذه القضية المتعلقة بقطر هي مجرد تلاعب. قطر دولة معادية، ولكن قطر ليست دولة فرضت أي شيء هنا.</div>
<div class="tg-footer">👁️ 723 · <a href="https://t.me/naya_foriraq/89412" target="_blank">📅 14:47 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89411">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🇮🇶
وزارة الداخلية العراقية تتوعد مستخدمي الذكاء الاصطناعي لصنع فيديوات خادشة للحياء أو تحتوي على كلمات وإيحاءات لا تمتَّ بصلة إلى ثقافة وأخلاق المجتمع العراقي.</div>
<div class="tg-footer">👁️ 1.4K · <a href="https://t.me/naya_foriraq/89411" target="_blank">📅 14:44 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89410">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">نتن ياهو: لقد هاجمت قطر - كما قمت بقصفها وهاجمتها خلال الحرب، وهم هاجموني. كل هذه القضية المتعلقة بقطر هي مجرد تلاعب. قطر دولة معادية، ولكن قطر ليست دولة فرضت أي شيء هنا.</div>
<div class="tg-footer">👁️ 2.06K · <a href="https://t.me/naya_foriraq/89410" target="_blank">📅 14:41 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89409">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">نتن ياهو يتوسل لانتخابه: من سيُنهي ما يجب أن يُنهى؟ من سيُنهي هذا النظام في إيران؟ من سيُنهي حزب الله؟ من سيُنهي حماس؟ خصومي السياسيون يستسلمون لكل ضغط. أمريكا تقول لهم "لا"، وهم يرتجفون على الفور. هل سيفعلون ذلك؟ لا. لن يفعلوا ذلك. نحن سنفعل ذلك.</div>
<div class="tg-footer">👁️ 2.18K · <a href="https://t.me/naya_foriraq/89409" target="_blank">📅 14:40 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89408">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ee42d895b.mp4?token=TgHD-MnXdIFoomtQDIi17WY-K-hXYrfHWNkI-s07lm38MPWvYFV13mNGq2rIwbqYCiaJwDN8dmquqhCHZeaTDd3wJmWMv4DTwNc7POaGLuj7s_7GJMR7onpqAf1j8-ZENjmI7g3wwiWNPz2r_Cat4o5L5ajMpXXlOR1HkihHOqhuKtNwsJuMZoXZ52eVfxpacCyjZApFL-lHYp81kzXb9feciMN3xWMqVV7ANiS8zdxs2NaMddiRRirrmkgMmliE2ueKKQyxy0kYRquHiYNa9X-vRIlAOxk9FLf1os40xS_GlSMyV3dw7Nv5FzS0mKob6JT6zyj57a83mSCpBqnzkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ee42d895b.mp4?token=TgHD-MnXdIFoomtQDIi17WY-K-hXYrfHWNkI-s07lm38MPWvYFV13mNGq2rIwbqYCiaJwDN8dmquqhCHZeaTDd3wJmWMv4DTwNc7POaGLuj7s_7GJMR7onpqAf1j8-ZENjmI7g3wwiWNPz2r_Cat4o5L5ajMpXXlOR1HkihHOqhuKtNwsJuMZoXZ52eVfxpacCyjZApFL-lHYp81kzXb9feciMN3xWMqVV7ANiS8zdxs2NaMddiRRirrmkgMmliE2ueKKQyxy0kYRquHiYNa9X-vRIlAOxk9FLf1os40xS_GlSMyV3dw7Nv5FzS0mKob6JT6zyj57a83mSCpBqnzkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">أزمة البنزين تتوسع في العاصمة العراقية بغداد وطوابير الوقود تمتد إلى مسافات طويلة</div>
<div class="tg-footer">👁️ 3.02K · <a href="https://t.me/naya_foriraq/89408" target="_blank">📅 14:33 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89407">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🇮🇶
العراق يعلن نجاحه في تفكيك مخيم الهول السوري ويعلن اغلاقه قريبا.</div>
<div class="tg-footer">👁️ 4.99K · <a href="https://t.me/naya_foriraq/89407" target="_blank">📅 14:14 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89406">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63fa90f779.mp4?token=lT3qQQj0ly_JZVFtclIE1GP7eilhum-SyvohEKUt7uQvBjeRGP78fdxdFr12pD9ZWZwK8WbZm4XNSBW04XRAEAoSrToFUr-zFhqUYozYPJ8DX5cxvjyy-2J_vp5TisP0zk3XK58_1p4SLTZv8OEFCPYdB3UYm2pA7GxDdPaDn4UMLoR_QdZYDRcmoowc97EvLi9v30m__dNSXoV4niFsrqG4hpG1wdmi0ihJ255NhP8mwAIRS0OA6zKVSalY8j7URWPgTYnTBAtfk-881WFyWaFB0ARKc_tn1sLIcqwgwMU1kQ5bj04UYM3scJ1w3wVX1jo9fv7sIpxf1FXZkA2EZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63fa90f779.mp4?token=lT3qQQj0ly_JZVFtclIE1GP7eilhum-SyvohEKUt7uQvBjeRGP78fdxdFr12pD9ZWZwK8WbZm4XNSBW04XRAEAoSrToFUr-zFhqUYozYPJ8DX5cxvjyy-2J_vp5TisP0zk3XK58_1p4SLTZv8OEFCPYdB3UYm2pA7GxDdPaDn4UMLoR_QdZYDRcmoowc97EvLi9v30m__dNSXoV4niFsrqG4hpG1wdmi0ihJ255NhP8mwAIRS0OA6zKVSalY8j7URWPgTYnTBAtfk-881WFyWaFB0ARKc_tn1sLIcqwgwMU1kQ5bj04UYM3scJ1w3wVX1jo9fv7sIpxf1FXZkA2EZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
طائرة عسكرية امريكية تهبط في مطار اربيل الدولي شمالي العراق.</div>
<div class="tg-footer">👁️ 6.91K · <a href="https://t.me/naya_foriraq/89406" target="_blank">📅 13:52 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89405">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🇵🇰
البرلمان الباكستاني وللمرة الأولى في تاريخ البلاد يمنح قائد الجيش عاصم منير سلطة قيادة رسمية على جميع القوات المسلحة الثلاث: الجيش والبحرية والقوات الجوية.</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/naya_foriraq/89405" target="_blank">📅 12:48 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89404">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9faa2ed76c.mp4?token=NQjlIynnDcqgfUWBp5ofzE5lvJRJ2j_SaJpO5pd1jyEF9blfLUc-loVIScq-ugK1ZW7KQ-p03FQVbHf1g1MgbuVulPdkW9wYJnr9-hjOcX_hJmkLdykvQsTZY314F_ofv1jITpLW5H816rqNEynzvFNapFvzG9hZF3esfebkRK9eEgZSHBwD1mczvo6YDDOLeq6baZljUKGfUM4o1JOsFNiwVTOAHChTizLjcyU2bzSGrUqNBla8PCrBTNX0Oht6B4U5GdfK3Rv9T_qznx0EwNwuinil65xmYA7mV1ohAnBJ76FKunRd6_jV61I_hIxbam2RePbZ2aiTKatf89ZcoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9faa2ed76c.mp4?token=NQjlIynnDcqgfUWBp5ofzE5lvJRJ2j_SaJpO5pd1jyEF9blfLUc-loVIScq-ugK1ZW7KQ-p03FQVbHf1g1MgbuVulPdkW9wYJnr9-hjOcX_hJmkLdykvQsTZY314F_ofv1jITpLW5H816rqNEynzvFNapFvzG9hZF3esfebkRK9eEgZSHBwD1mczvo6YDDOLeq6baZljUKGfUM4o1JOsFNiwVTOAHChTizLjcyU2bzSGrUqNBla8PCrBTNX0Oht6B4U5GdfK3Rv9T_qznx0EwNwuinil65xmYA7mV1ohAnBJ76FKunRd6_jV61I_hIxbam2RePbZ2aiTKatf89ZcoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏
زيلينسكي:
روسيا استهدفت مطارين في كييف و بوريسبيل قبيل وصول ويتكوف وكوشنر</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/naya_foriraq/89404" target="_blank">📅 12:42 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89403">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dd5042640b.mp4?token=oRoy8gDYS01s1HgQp3ONfNnEOA3xeXo-XtbVg3wMHZDYLnD55Ts8aL94xYDnSndNsIa01qiDKIbrWfOvGMDvZpKF61_lQGrBXXEMAvsUs6QksQyC7IerGdIvCFnuzPNEIXdlPz_Te6afnG-ynXG0oLIfCdjWSj4zAsYSim0ZDPEH6PtljEpWzpp-IbW9M-rBVMRf4rdtwCuHbELxb6-aBSXBatwq7Bfw2-o53WOiiHxw4kl5OjbrCStUVMmeNYKVS4h42TepuyTB3KlLwPFBOsoAk0FkpfHwxfP2gNnS-z5Pa6ToDffevac904P573HcD4Hru-McUIf_lBSaE7-3olU0H2pEbWOXO85f-2t_eO53b5PV-lKjPksqXZsIE-qpMpCV-ICtrXKTHQxDts29unyYP6JW-d2uNnGUx-4XPCjRQTba3k9sAdjcgijDcv-UNOiqMZ-Rpl58fVgcjbFP9uQYuifHc-dzcDXcfkXne2S8ZvK1rsO0SHlZOpoL78nQGWb2oqhC0X1p1gZVMW6MwhU6haE_9gHxm2KQQG1MReZZCN0_ZXhXOAfaweNeYDW5GAgKon3e4PQp_PNBvvytszgLTw-jrZNQ1mI5OMELBfwNALExvfvpasBgl9shWQh7w1h9rRBC8n3JogfSkBUWu_hBDyhWb7gXRYybcTMLhOI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dd5042640b.mp4?token=oRoy8gDYS01s1HgQp3ONfNnEOA3xeXo-XtbVg3wMHZDYLnD55Ts8aL94xYDnSndNsIa01qiDKIbrWfOvGMDvZpKF61_lQGrBXXEMAvsUs6QksQyC7IerGdIvCFnuzPNEIXdlPz_Te6afnG-ynXG0oLIfCdjWSj4zAsYSim0ZDPEH6PtljEpWzpp-IbW9M-rBVMRf4rdtwCuHbELxb6-aBSXBatwq7Bfw2-o53WOiiHxw4kl5OjbrCStUVMmeNYKVS4h42TepuyTB3KlLwPFBOsoAk0FkpfHwxfP2gNnS-z5Pa6ToDffevac904P573HcD4Hru-McUIf_lBSaE7-3olU0H2pEbWOXO85f-2t_eO53b5PV-lKjPksqXZsIE-qpMpCV-ICtrXKTHQxDts29unyYP6JW-d2uNnGUx-4XPCjRQTba3k9sAdjcgijDcv-UNOiqMZ-Rpl58fVgcjbFP9uQYuifHc-dzcDXcfkXne2S8ZvK1rsO0SHlZOpoL78nQGWb2oqhC0X1p1gZVMW6MwhU6haE_9gHxm2KQQG1MReZZCN0_ZXhXOAfaweNeYDW5GAgKon3e4PQp_PNBvvytszgLTw-jrZNQ1mI5OMELBfwNALExvfvpasBgl9shWQh7w1h9rRBC8n3JogfSkBUWu_hBDyhWb7gXRYybcTMLhOI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
🇺🇦
بسبب زيارة كوشنر صهر ترامب لأوكرانيا   ‏تم أمر وحدات من قوات الأوكرانية المدعومة من الناتو بالالتزام بنظام الصمت على الخط الأمامي من الساعة 00:00 يوم 5 سبتمبر إلى الساعة 23:59 يوم 8 سبتمبر ..</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/naya_foriraq/89403" target="_blank">📅 12:13 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89402">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2665ced0fb.mp4?token=apE6ex1zZnl16EJlv_q8Wf0zehfKtvspjYTRJScbBZeurBdAd65d254oIfXBLMOFmvkHKOsNTRUOTar4Bc170McVWuDZaXLPctBSXXKSUFSlA2kgDSfRrsimngjypz3ucCXGTTwRglaLsEqRLoFOTEdIBWiAyWo-Z4XbXyzemOxCAQ9jAWiTL7Uf08_b67YDW1FXshJLAUqZYtw2DOyXcAQ77AB0SUsXnLt2Tno-B6rIFZoZZ_DroPpcr2SyOE27m6RTEFIAUY_jJKpkb4i4oRhDXsTGo3Kx0e1oev3bIosameiEAjol_ZIt_MKDjFaoNsLVSE18kLC9zI1uRIlOSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2665ced0fb.mp4?token=apE6ex1zZnl16EJlv_q8Wf0zehfKtvspjYTRJScbBZeurBdAd65d254oIfXBLMOFmvkHKOsNTRUOTar4Bc170McVWuDZaXLPctBSXXKSUFSlA2kgDSfRrsimngjypz3ucCXGTTwRglaLsEqRLoFOTEdIBWiAyWo-Z4XbXyzemOxCAQ9jAWiTL7Uf08_b67YDW1FXshJLAUqZYtw2DOyXcAQ77AB0SUsXnLt2Tno-B6rIFZoZZ_DroPpcr2SyOE27m6RTEFIAUY_jJKpkb4i4oRhDXsTGo3Kx0e1oev3bIosameiEAjol_ZIt_MKDjFaoNsLVSE18kLC9zI1uRIlOSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
سماع دوي انفجار في جزيرة خارج.</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/naya_foriraq/89402" target="_blank">📅 11:53 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89401">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🇷🇺
🇺🇦
دخول اتفاق وقف إطلاق النار المحلي في منطقة محطة زابوريجيا النوويةحيز التنفيذ.</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/naya_foriraq/89401" target="_blank">📅 11:11 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89400">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🇮🇷
مصدر امني ايراني...
الانفجارات في محافظتي طهران واصفهان ناتجة عن تفجيرات مسيطر عليها.</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/naya_foriraq/89400" target="_blank">📅 10:56 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89399">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🇮🇷
سماع دوي انفجار في جزيرة خارج.</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/naya_foriraq/89399" target="_blank">📅 10:09 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89398">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🇺🇸
نيويورك تايمز:
تحقيق مع نحو 50 عضوا في هيئة الأركان المشتركة بشأن تسريب معلومات للصحافة عن حرب إيران.
التحقيق مع العسكريين يتركز على تسريب معلومات عن تراجع مخزون الجيش من الذخائر الحيوية.</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/naya_foriraq/89398" target="_blank">📅 04:24 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89397">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🇺🇦
زيلنسكي يتوسل: أدعو روسيا لوقف هجماتها على أوكرانيا خلال زيارة المبعوثين الأمريكيين ويتكوف وكوشنير إلى كييف الأحد.</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/naya_foriraq/89397" target="_blank">📅 00:17 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89396">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🇮🇱
🔻
جيش الاحتلال يدعي اعتراض مسيّرة أطلقها حزب الله باتجاههم في جنوب لبنان.</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/naya_foriraq/89396" target="_blank">📅 23:41 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89395">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">اصوات انفجارات في سيريك</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/naya_foriraq/89395" target="_blank">📅 23:26 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89394">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">اصوات انفجارات في سيريك</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/naya_foriraq/89394" target="_blank">📅 23:25 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89393">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8295dd1410.mp4?token=YWKIuCZUuldPy7yjv3EXwbNz9yogl-kP8CVSMq0D169qhUAm1Of4fLRP7EeANwNWUWQ3zR697wCvXHXrxmrunWMSF3sm4vtGs0S0vVLk0IM7rIfcHMXSqXTsJWskQJk1ZDbwRCVKYnzlr34yFH7NfE789t6oDmUdkN55CRD43My4nS_UzsXkjbJ4pGNsdEJJJ5yiTlY2TrztRG2x8bUlzEvjXTz3LC5YwWGbRaVuai7aa2ZDcByRgK_7jw4r1Uwf-f7APANw7sVZjq1JtvGeVWEnhdRbW9HB0TwTfluJ8Qu3rUrZVCWpvPe4tskbmIMOrQ6R2gRovcl3OeW9r34k4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8295dd1410.mp4?token=YWKIuCZUuldPy7yjv3EXwbNz9yogl-kP8CVSMq0D169qhUAm1Of4fLRP7EeANwNWUWQ3zR697wCvXHXrxmrunWMSF3sm4vtGs0S0vVLk0IM7rIfcHMXSqXTsJWskQJk1ZDbwRCVKYnzlr34yFH7NfE789t6oDmUdkN55CRD43My4nS_UzsXkjbJ4pGNsdEJJJ5yiTlY2TrztRG2x8bUlzEvjXTz3LC5YwWGbRaVuai7aa2ZDcByRgK_7jw4r1Uwf-f7APANw7sVZjq1JtvGeVWEnhdRbW9HB0TwTfluJ8Qu3rUrZVCWpvPe4tskbmIMOrQ6R2gRovcl3OeW9r34k4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
🇷🇺
ترامب: أتحدث إلى بوتين، وهو لا يسعى إلى مهاجمة حلف شمال الأطلسي (الناتو)، ويتكوف وكوشنر سيقدمان مقترحًا لإنهاء الحرب في روسيا.</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/naya_foriraq/89393" target="_blank">📅 22:26 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89392">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/94f4f649a5.mp4?token=AzafVlq9ivmH-MXr7BetRTCG1zkbaJGo1PECi7FVu2zfJGA0VrbnXMtV2MkEiJADhs8SHjgtxKsZTLL29UBiavBZq_RL0NH0S1aPoZMVRAlnmPm-AA1L4zV_eL2CG3BW3hiDTIP7IGx4EqsRqLeIe_LzH4IaFyK2Ay02Hvr7bMjcjAvqfAnqBFMaFNHwsp2DFu22HkYj3m94h0uJG-v4pw0Azt5DtxDPAVElm9pVJP6mcz3i93cY_3N5r0e4Vm1kUvfep-qMUxyvuVbwpif1h2U00fwRTXORclhy8oQRrNvirr0rAcRgMtwYKNIQuSXx1k5_lvg5Z90TpQr7A4bvcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/94f4f649a5.mp4?token=AzafVlq9ivmH-MXr7BetRTCG1zkbaJGo1PECi7FVu2zfJGA0VrbnXMtV2MkEiJADhs8SHjgtxKsZTLL29UBiavBZq_RL0NH0S1aPoZMVRAlnmPm-AA1L4zV_eL2CG3BW3hiDTIP7IGx4EqsRqLeIe_LzH4IaFyK2Ay02Hvr7bMjcjAvqfAnqBFMaFNHwsp2DFu22HkYj3m94h0uJG-v4pw0Azt5DtxDPAVElm9pVJP6mcz3i93cY_3N5r0e4Vm1kUvfep-qMUxyvuVbwpif1h2U00fwRTXORclhy8oQRrNvirr0rAcRgMtwYKNIQuSXx1k5_lvg5Z90TpQr7A4bvcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
🇮🇷
ترامب: قد نضرب "جبل الفأس" قريبًا جدًا.</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/naya_foriraq/89392" target="_blank">📅 22:15 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89391">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de7cc3a576.mp4?token=Kwosmkt1t2cSBbV7Iy33hsitoECQUV3ybY96KCLcG14GGLoFMPVL_xsRBDBIDGjeVuWvsezl4CuKz_v37IQ6DxmMw_U21lXlgiXPfi6erpn6O0H6rcWmXIQFGjPsEqrF5_0arkasmSmP4Uor22GMNy15b20n5DwnvqOVvjMpwkUyfhopZP3CaH87_BhL2s4Q-B_xuN9SqH1z-bCmy-bSridsRh2U79T6lX2uMlZ0rBhGqkier65e3xDDiAoU7aThN3TWvEnVoAE8EDhcnAgR5ulYBpEEE_xs0RD-0iZwGmjp4SXByncOyGdmb92P9QtgLG2y9qupSjPH3a56qV6Fow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de7cc3a576.mp4?token=Kwosmkt1t2cSBbV7Iy33hsitoECQUV3ybY96KCLcG14GGLoFMPVL_xsRBDBIDGjeVuWvsezl4CuKz_v37IQ6DxmMw_U21lXlgiXPfi6erpn6O0H6rcWmXIQFGjPsEqrF5_0arkasmSmP4Uor22GMNy15b20n5DwnvqOVvjMpwkUyfhopZP3CaH87_BhL2s4Q-B_xuN9SqH1z-bCmy-bSridsRh2U79T6lX2uMlZ0rBhGqkier65e3xDDiAoU7aThN3TWvEnVoAE8EDhcnAgR5ulYBpEEE_xs0RD-0iZwGmjp4SXByncOyGdmb92P9QtgLG2y9qupSjPH3a56qV6Fow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">المراسل: إذا لم يكن الصراع مع إيران حربًا، فما هو بالضبط؟  ترامب: أصفه بأنه صراع عسكري لأننا نعتبره أمرًا بسيطًا بالنسبة لنا؛ إنه ليس شيئًا كبيرًا،  نقوم بشنّ ضربات متقطعة في إيران. نحن نستهدف كميات كبيرة من النفط، الحرب مع إيران أمر بسيط بالنسبة لأميركا.</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/naya_foriraq/89391" target="_blank">📅 22:14 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89390">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6fd38aba6f.mp4?token=gFHEay4XivbgTvUKgn_RxlGE3rQLkBz_6uM3yISmR2XrH0Vt1mLC2b1pVQ4bGS2gt9dxP0VMn8_torfSN9WHZAJkmqWqRaclTI-C93-56RHTxhYyN1knVrCbCEK3Ab-G7OJSLXbO2yRIgK-UMgkJ3KEQGpFjQ9L_CGM7h0526xwg0BHpQnf0oKyO7QuvHiJvAGhszxw8Zj58X7842967DQTMmG09Zoe2guQ4X6UWvoaegJg5HOMDazxoHpi4zE8LQ-JIopJ2rA2LkIN88KHwlwHNQnqw_zgIc-yG9DVj0ucURN_yYNieUkbu-VpGCGIAGluKj1dwQ_JC4T5hRTkpA4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6fd38aba6f.mp4?token=gFHEay4XivbgTvUKgn_RxlGE3rQLkBz_6uM3yISmR2XrH0Vt1mLC2b1pVQ4bGS2gt9dxP0VMn8_torfSN9WHZAJkmqWqRaclTI-C93-56RHTxhYyN1knVrCbCEK3Ab-G7OJSLXbO2yRIgK-UMgkJ3KEQGpFjQ9L_CGM7h0526xwg0BHpQnf0oKyO7QuvHiJvAGhszxw8Zj58X7842967DQTMmG09Zoe2guQ4X6UWvoaegJg5HOMDazxoHpi4zE8LQ-JIopJ2rA2LkIN88KHwlwHNQnqw_zgIc-yG9DVj0ucURN_yYNieUkbu-VpGCGIAGluKj1dwQ_JC4T5hRTkpA4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">المراسل
: إذا لم يكن الصراع مع إيران حربًا، فما هو بالضبط؟
ترامب
: أصفه بأنه صراع عسكري لأننا نعتبره أمرًا بسيطًا بالنسبة لنا؛ إنه ليس شيئًا كبيرًا،  نقوم بشنّ ضربات متقطعة في إيران. نحن نستهدف كميات كبيرة من النفط، الحرب مع إيران أمر بسيط بالنسبة لأميركا.</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/naya_foriraq/89390" target="_blank">📅 22:11 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89389">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bbuTEa1maiwr-mn7XWKSBkCcLE10Jt65BLI-GGO-QUEplQUze6ihbA3-MT8l4OrG301BPsXNeZnN5Ewcr0QIEqejdzB5MsPP-SvegvvwGfsyggP-w6lTw8W1vt8GolHz1BBnsvK8K-zmMDF2-7mVcm7SpgLvo0JlL3cjyLOz_LTJrjhhyrOcKVoR23rDUKeutgcAV4DRuADtnnrN-DpMZhYUp9EANV6DTfERRrj-Q9ve-4GDjQZOb0zqgMX5gHh2aByeNVSQVhRkZCywace6CcDl4gNpSjvPSGKZa4Eb6_x68u6MFzyk3Ok1Woq1O8ivJ5v3DVmrwDSpsbkZ6eOtLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
حشدُ الله.. حُماةُ الأرض، حُماةُ العراق.</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/naya_foriraq/89389" target="_blank">📅 22:07 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89388">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🇮🇶
🇺🇸
‏
الخارجية الأميركية:
صفقة طائرات هليكوبتر بيل 412 إلى العراق تقدر بـ 150 مليون دولار ‌.</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/naya_foriraq/89388" target="_blank">📅 21:42 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89387">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/127f5c1af7.mp4?token=frBuqdxlL895ghym3QDbZVRQo1i0eQnJ9PSMeach5KRu31AS3HuETQAylQ8dPNKceo_in_-6BdvK2pEW12Pcbzq1hVDpfI67IpqOO3Ece81Zg2CUDz8gY7aE1RMwbPT93DTiGanIwD-gLLtkHJvmnfQJI69in60OLxTA36DeA3oqmwB0zC5yyAEH6Gx9P0kzfi581Hj0x3rTmxEooXedlzAVOSblS3PiRHT4b5_KkFLyzLdWmSGxKFxX_KK844_uLdCXsyfE6iH6m_vdWtI4o1vWBp0DIcWZSEYP9tf4hFVhpQGg01A2eQ3pztH0UQxisZm7KM-SRS76mQyi_Uz78w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/127f5c1af7.mp4?token=frBuqdxlL895ghym3QDbZVRQo1i0eQnJ9PSMeach5KRu31AS3HuETQAylQ8dPNKceo_in_-6BdvK2pEW12Pcbzq1hVDpfI67IpqOO3Ece81Zg2CUDz8gY7aE1RMwbPT93DTiGanIwD-gLLtkHJvmnfQJI69in60OLxTA36DeA3oqmwB0zC5yyAEH6Gx9P0kzfi581Hj0x3rTmxEooXedlzAVOSblS3PiRHT4b5_KkFLyzLdWmSGxKFxX_KK844_uLdCXsyfE6iH6m_vdWtI4o1vWBp0DIcWZSEYP9tf4hFVhpQGg01A2eQ3pztH0UQxisZm7KM-SRS76mQyi_Uz78w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجارات قوية تسمع في الاردن</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/naya_foriraq/89387" target="_blank">📅 20:57 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89386">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">موجة انفجارات جديدة في سماء قاعدة الأزرق بالأردن</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/naya_foriraq/89386" target="_blank">📅 20:57 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89385">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/naya_foriraq/89385" target="_blank">📅 20:56 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89384">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XDHwRecAqS7_F8DHETXCnsA2qB1AEKEm9Rby_WlG3MLt7FG09q5Fm7UuiAlDhWyYJZxNSQcnaobD5LIPRQDD57J0Ivk1kYOE3HlNlF2BP8qX-FNYYpBJ5C1fhj3gyFnooZDCrJ52WsaYpdV5X_QdEZ_hDWVE_8uZ6Hcz0alxnSqF1QB4q2UnzA6pCNC5Kz71H0fk6wzNjUY4zGqmeS_SmT3izf7MZ5LVBIvpQBov2W7AN7ht5-i286e_x17pGSUUNoIv5TxpOmkyqjXlnq5AR8gYCXzZgCvUUy-psR81g7fznOX9PA27qYod9igHOOYsVvwoTDxfWOV9q8yu4xS2qA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اطلاق صاروخي من ايران</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/naya_foriraq/89384" target="_blank">📅 20:55 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89383">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🇷🇺
طائرة روسية مسيرة تشن غارات على مقر جهاز الأمن الأوكراني (SBU) في كييف.</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/naya_foriraq/89383" target="_blank">📅 20:47 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89382">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UnqiIrr9jzXPDbYEHhhdHbXDo4QSOYruScHv1jkrEgQdppXRZxBaV3tyuM6f6JXaXfbxZ49iuPy3q_g7wWGofm5Cv_u_uVBWfvRBHIyWLpn9zxXzm0CoiDycPRlCD4k3K3YxNFZmq3bUSAS57Hhs1i2pSz9BWK9OrvVjfG4TcPxyGJ2Dcbu3WUUrOb-jgsxKfEhvUTZFjP8d1t2x7cpm8Bt6NHPq-7x--Yjnx_7zNIK3_6bOFgslOenz6gD6rv5zDNygPujgAblPsu92cKzdaWPlmt10orPt8YMjTupspQ8jOujf1h-Jy7i0Z0YtF64fYbjX19-jU7-oLiArNAto3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
🇨🇳
قاليباف
: ‏إن تركيز الصين على تعزيز الأمن المشترك يعكس مبدأً لطالما دافعت عنه إيران.‏يجب على دول المنطقة أن تتولى زمام مستقبلها بنفسها، ولن يتحقق الاستقرار الحقيقي إلا من خلال بنية أمنية جديدة محلية المنشأ. إيران على أهبة الاستعداد.</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/naya_foriraq/89382" target="_blank">📅 20:27 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89381">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c44ad22364.mp4?token=Bl9ufSLmLxQJFih18sTvDsMU_sJbrP08-aSNPOmwGbeYtdzCh9xKdiZq27ctq0Vl8SFzdWIBAtJrVP9wzrN6IirsNhBaamMD5VXsinrMMbUn8Ar5CD6yOgS7OSAx3YJ-NXJLu39VXNpJdlwnxRwAEXbTQFklIjDDoidsZobEsdUlck0aFb1DlhXfoTodE7Nm5xMj1CzHsGhQUChyJdjI_Y-vKWYOxA9fbC_VQY_FtArJwuOLm2H_1Km0FJbuuescHdazeDflexvMvVPQ03l3vdDMsTPsdwnBEY-V_iShtki-Qu40bsxNmywFygxUEyLUgYNMPLrEOfx-W_Tv6uu5-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c44ad22364.mp4?token=Bl9ufSLmLxQJFih18sTvDsMU_sJbrP08-aSNPOmwGbeYtdzCh9xKdiZq27ctq0Vl8SFzdWIBAtJrVP9wzrN6IirsNhBaamMD5VXsinrMMbUn8Ar5CD6yOgS7OSAx3YJ-NXJLu39VXNpJdlwnxRwAEXbTQFklIjDDoidsZobEsdUlck0aFb1DlhXfoTodE7Nm5xMj1CzHsGhQUChyJdjI_Y-vKWYOxA9fbC_VQY_FtArJwuOLm2H_1Km0FJbuuescHdazeDflexvMvVPQ03l3vdDMsTPsdwnBEY-V_iShtki-Qu40bsxNmywFygxUEyLUgYNMPLrEOfx-W_Tv6uu5-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اطلاق صاروخي من ايران</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/naya_foriraq/89381" target="_blank">📅 20:10 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89380">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/naya_foriraq/89380" target="_blank">📅 20:10 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89379">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">الصواريخ الايرانية تصل الى الاردن</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/naya_foriraq/89379" target="_blank">📅 20:10 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89378">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🇺🇦
زيلنسكي يتوسل:
أدعو روسيا لوقف هجماتها على أوكرانيا خلال زيارة المبعوثين الأمريكيين ويتكوف وكوشنير إلى كييف الأحد.</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/naya_foriraq/89378" target="_blank">📅 19:45 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89377">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pUO6ODgFfN04Dl5njowqqAcXVObE-W4Y4z1Ly2BKQxhqmWdq07RQeV-lZIdE79PITB18EKCaa5L3rS0kYUqXhc7Zx6L4XkJw-j07o75zEyBLHvvuL487Wqw641xoUuUKQA07T37SZO3T9MBUivghYpXcA8S-ySLP8d9DB6uMB-J-m3ObImPJU37O8i3moqV07aQ8-7n3OO1NfLLAWwnJbn3SSj8uhjb9v8UP2sK8I5bwAf25UFxEJkmp6HAyU_M3c0xFWMBEf8vxX9EBIh4O3kjRHsaFgFa8BIL5LMwS7qjc8e5Z_lt7BDEH2fDC1HvzLWFROYFsiAH0mHogXlzGpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامب
:
يفضل المتطرفون اليساريون والديمقراطيون والشيوعيون أن نخسر الحرب في إيران على أن يربح الرئيس دونالد ج. ترامب الحرب من أجل أمريكا. بعبارة أخرى، يفضلون أن نخسر على أن نربح! هؤلاء أشخاص مرضى للغاية يعانون من متلازمة جنون ترامب الخطيرة، والتي يشار إليها أحيانًا باسم متلازمة جنون ترامب.</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/naya_foriraq/89377" target="_blank">📅 19:39 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89375">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🇺🇸
الاعلام الامريكي:
‏تسعى الولايات المتحدة، في أعقاب الأضرار الجسيمة التي لحقت بطائرات MQ-9 Reaper المسيّرة وتدميرها خلال النزاع مع إيران، إلى إيجاد بديل أقل تكلفة لهذه الطائرات.</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/naya_foriraq/89375" target="_blank">📅 19:26 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89374">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">اطلاق صاروخي من ايران</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/naya_foriraq/89374" target="_blank">📅 19:22 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89373">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🇮🇷
دبلوماسي إيراني:
أي استهداف للبنية التحتية الإيرانية من القواعد الأميركية في الدول الإقليمية سيواجه برد من إيران.</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/naya_foriraq/89373" target="_blank">📅 18:59 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89372">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🇮🇶
مجلس نقابة المحامين العراقيين يقرر منع قبول انتماء المقيمين بصورة دائمة في إقليم كردستان العراق.</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/naya_foriraq/89372" target="_blank">📅 18:41 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89370">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d722832d1c.mp4?token=bA6hAnhmhk7bc2vinyGWHq6gYzqUIZCHTjH3AZD4FEE8trWs6E7gQjvATroj0fIhsXZf4SedIQW8wSUkHmfvWBvdMAaLhm0rj-bshHuIopykrLiYGAApbXex4i1BpkH0iPeViSfyymFt0acop3Y5OtNb99ij6o14F4HhGHgE3Ivi7k9ePe6cVHNOleFpOhYMWpEdZjVPLRTdtfgBlh27Tn7yR0lXr2mWLFapmO5pvqTt10_lmLA5qVBmPqgQZqz9TwQ8q3JjWAszDhBAl_Y8h8TcG2PdnOrYOtRJagtFHk9Jd1LvG3V36gNuOVp7CgUr2eG5IoQ-ejTKQY8GplDEqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d722832d1c.mp4?token=bA6hAnhmhk7bc2vinyGWHq6gYzqUIZCHTjH3AZD4FEE8trWs6E7gQjvATroj0fIhsXZf4SedIQW8wSUkHmfvWBvdMAaLhm0rj-bshHuIopykrLiYGAApbXex4i1BpkH0iPeViSfyymFt0acop3Y5OtNb99ij6o14F4HhGHgE3Ivi7k9ePe6cVHNOleFpOhYMWpEdZjVPLRTdtfgBlh27Tn7yR0lXr2mWLFapmO5pvqTt10_lmLA5qVBmPqgQZqz9TwQ8q3JjWAszDhBAl_Y8h8TcG2PdnOrYOtRJagtFHk9Jd1LvG3V36gNuOVp7CgUr2eG5IoQ-ejTKQY8GplDEqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انباء عن اطلاق صواريخ باتجاه مضيق هرمز</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/naya_foriraq/89370" target="_blank">📅 18:03 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89369">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wish_1Pzm2H36I8DOueg4S0SlIl0XxkitEMC0gnQYbL_CEKMsvaPAwpOSD9y0Fbhsz3KLSsqVLsncPvNMDWADfXtXgCV_bKh269S-xyNb_yaBwcfn145mmQ4Z0KZbFnICKTJWa-gP-933QTqoAoqWYUwnRS2Q7XXng54jLjDp6PntrZsJtwaEEBce_EJe4vrVyq8RIaqXsTEMoKLqeMlmLF6NO_4gYexZxntIZdFyx7cW3d_yUXX7OHf9p-liSFPyLPtZuf3cHww3JdMYTj6Qr1OjTq0euqoW40BpNuTqm4zrjVL9NCezvbPlpwX2SdCHVWqu9YM790NfejtH_dXEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
🔻
منصات التتبع:
‏لم تُرصد أي سفينة اليوم تعبر مضيق هرمز عبر المسار "الآمن" للولايات المتحدة  ويمكن رؤية ثلاث سفن فقط، سبق أن تعرضت لهجوم إيراني مهجورة وراسية.</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/naya_foriraq/89369" target="_blank">📅 17:53 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89368">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🇮🇶
وزارة النفط العراقية تعلن تحقيق أعلى معدل صادرات وواردات منذ اندلاع الحرب في آب الماضي حيث وصل التصدير قرابة 70 مليون برميل.</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/naya_foriraq/89368" target="_blank">📅 17:45 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89367">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">الولايات المتحدة تفرض عقوبات جديدة مرتبطة بإيران تستهدف ثلاث جهات</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/naya_foriraq/89367" target="_blank">📅 17:38 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89366">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">الولايات المتحدة تفرض عقوبات جديدة مرتبطة بإيران تستهدف ثلاث جهات</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/naya_foriraq/89366" target="_blank">📅 17:35 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89365">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🇮🇱
اعلام العدو:
يعتقد أن إيران وحماس تكثفان جهودهما لمهاجمة صهاينة في الخارج قبل الأعياد اليهودية.</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/naya_foriraq/89365" target="_blank">📅 17:30 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89364">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/238d7c563a.mp4?token=HbbEtZKls2Ztfv5zVJJRASQFQ4OwoG6ir-N8D6tI0wexwEyw4j1YMsKF0QN1lkRPAs3SjyoMqIkT_hULrkMMOWOkKj-5pPaWsZAqIsLSc1UAdY5bMcTZZxLiVccgxfCSc2rEvt2WKGX154sduKZx8WYuXWJMVj20uEp6QmGOiFvynC2WXbub3Vm_5KCDsJSyoukpzaDwqrVUYKVWYCMPfuYtP12J98GJrAYA1RHyfKIBs2j--aQ7gYGVS3JN6GbChvGAucCaVHVqIcmo_FDMESoFYLaAr902njNNuLMWki-2j9uNgWgQkPlK8R9-JUeY4FU5U4RykrJEjt5p68kmOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/238d7c563a.mp4?token=HbbEtZKls2Ztfv5zVJJRASQFQ4OwoG6ir-N8D6tI0wexwEyw4j1YMsKF0QN1lkRPAs3SjyoMqIkT_hULrkMMOWOkKj-5pPaWsZAqIsLSc1UAdY5bMcTZZxLiVccgxfCSc2rEvt2WKGX154sduKZx8WYuXWJMVj20uEp6QmGOiFvynC2WXbub3Vm_5KCDsJSyoukpzaDwqrVUYKVWYCMPfuYtP12J98GJrAYA1RHyfKIBs2j--aQ7gYGVS3JN6GbChvGAucCaVHVqIcmo_FDMESoFYLaAr902njNNuLMWki-2j9uNgWgQkPlK8R9-JUeY4FU5U4RykrJEjt5p68kmOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇷🇺
طائرة روسية مسيرة تشن غارات على مقر جهاز الأمن الأوكراني (SBU) في كييف.</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/naya_foriraq/89364" target="_blank">📅 17:21 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89363">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🇺🇸
وكالة رويترز:
‏تسعى الولايات المتحدة ودول أوروبا الثلاث إلى التوصل إلى قرار في اجتماع مجلس محافظي الوكالة الدولية للطاقة الذرية الأسبوع المقبل، يقضي بإبلاغ مجلس الأمن التابع للأمم المتحدة عن إيران لخرقها التزاماتها المتعلقة بعدم انتشار الأسلحة النووية.</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/naya_foriraq/89363" target="_blank">📅 17:20 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89362">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">انباء عن اطلاق صواريخ باتجاه مضيق هرمز</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/naya_foriraq/89362" target="_blank">📅 17:15 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89361">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🇷🇺
طائرة روسية مسيرة تشن غارات على مقر جهاز الأمن الأوكراني (SBU) في كييف.</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/naya_foriraq/89361" target="_blank">📅 16:47 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89360">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🇮🇷
الجيش الإيراني:
سنقوم بعمليات استباقية في أي مكان نشعر فيه بالتهديد.</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/naya_foriraq/89360" target="_blank">📅 16:15 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89359">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🇮🇶
ازمة وقود تضرب العاصمة العراقية بغداد وعدة محافظات اخرى.</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/naya_foriraq/89359" target="_blank">📅 15:55 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89358">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c841790a8a.mp4?token=h-NvMDoSGIkwLStjGm59uAe8uH3mgrQBCbn6953YyHFWlOj6drW7dBsWuQsDBwdYxUI4KQNNE4Z4mQxk5HnXtZTEYZi74CoFHymXWrZ3fdmSicEYmIeP_4MNJZV2ag5QW3hX9SCw5wjDkcj5K8bvZE4F89ipPdSi4_ZMIkk6zZb8W_pzwTdjqmQkEhH4nEJn5kgLuyTp9gQOwX4tuNWlLnBPDmD9DsLrPtyN1oDFnZ4hd5__L0Ld5vmUu1UeIYFnBAMSVxhcrzmtnU2ey2URANSUBTnjms9hqJfT3DF2wZUerFDx-S9Gj35ckUG62o5C7YMfTbgWPAkC38028EI94A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c841790a8a.mp4?token=h-NvMDoSGIkwLStjGm59uAe8uH3mgrQBCbn6953YyHFWlOj6drW7dBsWuQsDBwdYxUI4KQNNE4Z4mQxk5HnXtZTEYZi74CoFHymXWrZ3fdmSicEYmIeP_4MNJZV2ag5QW3hX9SCw5wjDkcj5K8bvZE4F89ipPdSi4_ZMIkk6zZb8W_pzwTdjqmQkEhH4nEJn5kgLuyTp9gQOwX4tuNWlLnBPDmD9DsLrPtyN1oDFnZ4hd5__L0Ld5vmUu1UeIYFnBAMSVxhcrzmtnU2ey2URANSUBTnjms9hqJfT3DF2wZUerFDx-S9Gj35ckUG62o5C7YMfTbgWPAkC38028EI94A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فرحة كبيرة في صفوف الارهابيين التكفيريين داخل سجن رومية اللبناني بعد إقرار العفو العام داخل مجلس النواب اللبناني</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/naya_foriraq/89358" target="_blank">📅 15:34 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89357">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a4fe167d53.mp4?token=luhLxdxb1WHmx5TTBmAVUxWAzmWjw9toWqqojtTwilq6B9gpFOHg4SPpI6c5KdNxJlGT7dkDWu2hK0YzNK-jx-v5-RWp6kGgtF2eOaDSpzqgUL6VkyleYY3TuAlxoiJePffjg9zn-8e4C0CmMJzHZXBjnhn2ggGkbJSkwuGsUAk98xbaKCxhLoO2yXqsyucLxVBYh66Ih8dxD1JCXrpc9sAHxblCTLBfGL0nzUfxsRQ1hDqXPhXHDuZt3WzXzRjKIFPETPZDtGB6c7pdQyOwyuvnxWudjQtWr8QnkwkG3dpiRTXJztuUwLVWUBGexZrj_4naXo-NFep0gy_QrWyLyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a4fe167d53.mp4?token=luhLxdxb1WHmx5TTBmAVUxWAzmWjw9toWqqojtTwilq6B9gpFOHg4SPpI6c5KdNxJlGT7dkDWu2hK0YzNK-jx-v5-RWp6kGgtF2eOaDSpzqgUL6VkyleYY3TuAlxoiJePffjg9zn-8e4C0CmMJzHZXBjnhn2ggGkbJSkwuGsUAk98xbaKCxhLoO2yXqsyucLxVBYh66Ih8dxD1JCXrpc9sAHxblCTLBfGL0nzUfxsRQ1hDqXPhXHDuZt3WzXzRjKIFPETPZDtGB6c7pdQyOwyuvnxWudjQtWr8QnkwkG3dpiRTXJztuUwLVWUBGexZrj_4naXo-NFep0gy_QrWyLyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#ترفيهي
🇮🇶
سرقة صندوق تبرعات احدى جوامع مدينة الموصل شمالي العراق اثناء صلاة الجمعة وامام الجامع يناشد لارجاع الصندوق.</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/naya_foriraq/89357" target="_blank">📅 15:27 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89356">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c75c9ac861.mp4?token=OaP4AAGjJbRjKedpqBf-TxGNr5OChiQjDhO9HKqHszRcucAVpxesNpRE7avxr2CyHB9cd0XBxDeR3SFt79QwLeLG7LWDYQ3KgxMWkc32fJq23_VzZN8GNzYYxY0GSJ23DufoeMFbUXaawjn-56_RuF58ZroMHAxGu-N6Pa3zpLcKxm2jtiteZht_nXdf62ODpht-uTKAeDAqZ9VNJbKWxNxZBeR-CW1Af4aRxbVCh6KhAtaikv9BgXrS-i04wSbpvu3XXTHohJfzslqSuiPcYCqEaKRdsp3v9l1kCGy5HV2ontSIiE5AJoVY42GvUYmoC08nEtszTNKZyg7yMGiImQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c75c9ac861.mp4?token=OaP4AAGjJbRjKedpqBf-TxGNr5OChiQjDhO9HKqHszRcucAVpxesNpRE7avxr2CyHB9cd0XBxDeR3SFt79QwLeLG7LWDYQ3KgxMWkc32fJq23_VzZN8GNzYYxY0GSJ23DufoeMFbUXaawjn-56_RuF58ZroMHAxGu-N6Pa3zpLcKxm2jtiteZht_nXdf62ODpht-uTKAeDAqZ9VNJbKWxNxZBeR-CW1Af4aRxbVCh6KhAtaikv9BgXrS-i04wSbpvu3XXTHohJfzslqSuiPcYCqEaKRdsp3v9l1kCGy5HV2ontSIiE5AJoVY42GvUYmoC08nEtszTNKZyg7yMGiImQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
عودة ازمة شحة الوقود من جديد... ازدحامات خانقة وطوابير طويلة أمام محطات الوقود في عدة محافظات عراقية.</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/naya_foriraq/89356" target="_blank">📅 14:55 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89355">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🇮🇶
تطورات تسليم حزب العمال الكردستاني لسلاحه ومغادرته الاراضي العراقية:
جهاز الاستخبارات التركي سيتولى الإشراف على تسليم حزب العمال الكردستاني لأسلحته في العراق
المخابرات التركية ستشرف ميدانياً على إخلاء 72 موقعاً ومخبأ تابعاً لحزب العمال الكردستاني
سيتم تحديد 5 نقاط لتسليم السلاح على الحدود بين أربيل والسليمانية
بعد إخلاء المناطق من حزب العمال الكردستاني ستنتشر قوات حرس الحدود العراقية مع البيشمركة</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/naya_foriraq/89355" target="_blank">📅 14:17 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89354">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🇺🇸
اعلام العدو:
أُوقف مواطن إسرائيلي للتحقيق لدى الشاباك والشرطة على خلفية الاشتباه بارتكاب مخالفات أمنية. وتبيّن خلال التحقيق أنه جرى تشغيل المذكور من قبل جهات استخبارات أجنبية، وأنه كان ضالعًا في نشاط تأثير أجنبي. ومع انتهاء التحقيق معه، قُدّمت بحقه لائحة اتهام وطلب لتمديد توقيفه حتى انتهاء الإجراءات القانونية، على خلفية مخالفات أمنية نُسبت إليه بسبب تشغيله من قبل جهات استخبارات أجنبية ضد "إسرائيل".
وبقية تفاصيل القضية ممنوعة حاليًا من النشر.</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/naya_foriraq/89354" target="_blank">📅 12:57 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89353">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🇮🇷
🇺🇸
فايننشال تايمز:
- مسؤولون أميركيون أبلغوا الوسطاء بأن واشنطن تريد فتح مضيق هرمز بالكامل بغض النظر عما تتفق عليه طهران ومسقط
- واشنطن غيرت شروطها بعدما أُبلغت بأن إيران وعُمان تحرزان تقدماً في محادثاتهما بشأن المضيق
- طهران تصر على أنها لن تعيد فتح المضيق إلا بعد رفع الحصار الأميركي وإعادة العمل بإعفاء يسمح لها ببيع النفط والسماح لها بالوصول إلى بعض أصولها المجمدة في الخارج</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/naya_foriraq/89353" target="_blank">📅 12:52 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89352">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sYb1cRytQYdwKY-yNwDp64Nphm5Q1rANe_pHCuec9ePsvFfHjVzJJs362eAwTvl5upmTrR2kdYxASc1MyJsthWi5BCDBTkvK5G7-hQ3MogKTG0eRmZ9KN8zvTbw7oGp4bfD5bJzJi4mmlNH9-LvKHcXk9krF5StYDc_YKfuCSPYDVstwF89FsHX3jJDg-CEUnn77Fqt7t3kLCJcjxV3YKWCW42oVVfNenvFrrC6xDzzXRQvtYWZ5DPNsftnZTJ_ZgCI5eqRldIOwpxH0ZwcOfomhtPn127GI55kiF1xv-4XdJTEGYGrcwIt4P2YBxQ5AeRzpgZnsJs8j-n62-6gyrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
جمهورنا الكريم
...
🔻
لغرض التواصل معنا ونقل مشاكلكم وارسال الاخبار والمواد الصورية والفديوات ، سنكون على مدار الساعة معكم نجيبكم.
للمراسلة
@Nayaforiraq_bot</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/naya_foriraq/89352" target="_blank">📅 12:23 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89351">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🇺🇸
‏فانس: لا أعتقد أن لدينا أي معلومات بخصوص هجوم الزفاف، الولايات المتحدة لا تستهدف المدنيين أبدًا في القتال، ولن نفعل ذلك أبدًا.</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/naya_foriraq/89351" target="_blank">📅 12:10 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89350">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🇷🇺
🇺🇦
بعد تهديد زلينسكي باستهداف الطيران المدني
طيران تنزانيا توقف رحلاتها لموسكو</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/naya_foriraq/89350" target="_blank">📅 12:01 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89349">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eC2Iwox8xj4nfBWST1MhaOUahVGE6aEByl3Q2c6nngW-qzRDVpvGXKHSnSGtj220csTsCCUxr6sRs_f0Rma8nIAY1vi5egNNFtluIWE3-aDAgEGDZLu4SMJYPvUy7ldbDf1Rd3nfFZ3QC9Dy9fGOZD05cxvVOf215XtrCY6iljh-RhZGEnmN09-l6ftlLH291j8aWlVuUmFXG07wDR0Ew1tNfwyylsas2NhQNFYAC-hIR6ITL2prRHFtnX8mRFNX0mEfKjXfGjJ21Dm2wxb4Dz-J5gZ_3T04GSVnLzVeaPpkTcxetPwUx7ZbrX7KtGlgcIxYPFWQ6qkT35qvN0DgLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
عراقجي
يرد على وزير الخارجية الاردني:
كم من الوقت يرى وزير الخارجية الأردني أنه يتعين على إيران أن تنتظر قبل أن ترد على معتد لا يحترم سيادة العرب
وهل هو حقا غير مدرك أن المجال الجوي والأراضي والمياه العربية استخدمت في الهجمات الأمريكية الأولى التي أسفرت عن مقتل إيرانيين أبرياء ؟</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/naya_foriraq/89349" target="_blank">📅 11:06 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89348">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ada3f1a49.mp4?token=VYbZ9KuWMofrj5Ben2O-zyXIK-nmJLyv5kNzVf85Yw7usbpuKEI1nXj8KvQBQCHrZIy6Deif-tWMsSzqa_pklB5RgH0I-zIhn4THOBad6R8i0V-fYleuut-yhewtv77l-demTk0_W5qFiWa3Q13yCcjjq7MeyZ4i2zh7smoJnl7dHUyCi1gPN10IzTLQml8OdkPeEwW87Rrpg0yWpARagKLAKP5ykPZTOxjrFKobaYGWEyBzFz6_I1X_JM5wgGF-deLj-lds14ckbX6agU07kiemBwNfcXCMED7_Aq2w3t4M3kEkEG6tbWCiSJbtAMLAd-MoaPk7EawHzRT2va2dgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ada3f1a49.mp4?token=VYbZ9KuWMofrj5Ben2O-zyXIK-nmJLyv5kNzVf85Yw7usbpuKEI1nXj8KvQBQCHrZIy6Deif-tWMsSzqa_pklB5RgH0I-zIhn4THOBad6R8i0V-fYleuut-yhewtv77l-demTk0_W5qFiWa3Q13yCcjjq7MeyZ4i2zh7smoJnl7dHUyCi1gPN10IzTLQml8OdkPeEwW87Rrpg0yWpARagKLAKP5ykPZTOxjrFKobaYGWEyBzFz6_I1X_JM5wgGF-deLj-lds14ckbX6agU07kiemBwNfcXCMED7_Aq2w3t4M3kEkEG6tbWCiSJbtAMLAd-MoaPk7EawHzRT2va2dgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
عودة ازمة شحة الوقود من جديد...
ازدحامات خانقة وطوابير طويلة أمام محطات الوقود في عدة محافظات عراقية.</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/naya_foriraq/89348" target="_blank">📅 10:17 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89347">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🇺🇸
وزير الخزانة الأمريكي:
الاتحاد الأوروبي انضم رسميا لعملية المنبوذ الاقتصادي ضد إيران ونقدر موقفه القوي والمبكر.</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/naya_foriraq/89347" target="_blank">📅 03:02 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89346">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n1ja4BMc1s6nkr4TcLq7MvupuvyNusaFDz8f5UaUa4W_-PZKosaTXxXuL8stCZ2OXn4VJFcC1FcxpcicGcVyPVYdADGLygEHPyVDbe33Q1C9S7t4jIOsVp1Dg3DtesMKacebUJXOT7wD6-Y0k5PdHfXWN1ghbM86tYt0MMYvzyJ7czuG8QSb-Lb5mPX1YXgtkoVOrMmHgms7erLEeLLL_lpVYshYltkh5N3S0o_IqdXOGH2h8yIc0sTLbadA5t8ctpPo1MdgvvCzbViV2J49SC0D0XupGlhzoUGnSMX01hIbBxrkEbgx9z5F6K01WCe2Ur_doA59PPA59i9mI-FIDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامب:
لقد أصدرت المحكمة العليا في ميزوري حكمًا سخيفًا لصالح إعادة الخرائط إلى ما كانت عليه منذ زمن بعيد. هذا ما يُسمى بالتاريخ القديم! المشكلة، بحسب فقهاء القانون، ليست فقط أن الحكم كان فظيعًا وسخيفًا وغير دستوري، بل لن يكون هناك وقت كافٍ لإعادة الخريطة مع اقتراب الانتخابات في فترة وجيزة جدًا. العملية الانتخابية، كالعادة، تتعرض للتشويش في أمريكا! يجب أن تتمكن ميزوري من استخدام الخريطة التي كانت سارية قبل شهرين فقط، في الانتخابات التمهيدية.
‏هذا يوم أسود للعدالة في ميسوري! شكرًا لاهتمامكم بهذه المسألة.</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/naya_foriraq/89346" target="_blank">📅 02:49 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89345">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🇮🇱
جيش الإحتلال الإسرائيلي:
رصد إطلاق نار باتجاه قوات الجيش الإسرائيلي التي تعمل شرق الخط الأصفر في شمال قطاع غزة. مسلحون في غزة يخططون لتنفيذ أعمال معادية ضد قواتنا.</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/naya_foriraq/89345" target="_blank">📅 02:32 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89344">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🇮🇷
الاطلاقات نحو مضيق هرمز.</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/naya_foriraq/89344" target="_blank">📅 01:27 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89343">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🇮🇶
اصوات طائرات مسيرة في محافظة اربيل شمالي العراق.</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/naya_foriraq/89343" target="_blank">📅 01:25 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89342">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/144436e58e.mp4?token=l8Tpam8BV80DzUbuav_ZrvU8yAjl62qQIq4dfZeZyuiGMiYYa1kiYrhhLTh9ckEHIHsB-vxWGgWuot-X5u8YuG1Xjr4LpevLBvQXuP27CSjQe6M5BAEglQbomyzAEo_2SD4E0CHO30DdfHJy1gLFMAwEIp2itDK-w2QWjPacDJ1SuLHz_JGGsYrLYofC_wlf4QnVfK2TOjZmp6q-nN4HqOaVZKS5qV5mwegvalXefsdamfgM2EE-icHKlMLglb2NqLb5OrulnsObEOeecFBWvaE8hqT_bjfritdgX2jyGV-cra5NL1vC3F1sFYQ3ev6_oVKbV9tfxETgAH2wGBTulg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/144436e58e.mp4?token=l8Tpam8BV80DzUbuav_ZrvU8yAjl62qQIq4dfZeZyuiGMiYYa1kiYrhhLTh9ckEHIHsB-vxWGgWuot-X5u8YuG1Xjr4LpevLBvQXuP27CSjQe6M5BAEglQbomyzAEo_2SD4E0CHO30DdfHJy1gLFMAwEIp2itDK-w2QWjPacDJ1SuLHz_JGGsYrLYofC_wlf4QnVfK2TOjZmp6q-nN4HqOaVZKS5qV5mwegvalXefsdamfgM2EE-icHKlMLglb2NqLb5OrulnsObEOeecFBWvaE8hqT_bjfritdgX2jyGV-cra5NL1vC3F1sFYQ3ev6_oVKbV9tfxETgAH2wGBTulg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇾🇪
🇸🇦
اشتباكات عنيفة بين القوات اليمنية والمليشيات الموالية للسعودية في اليمن عندة جبهات محافظة الحديدة.</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/naya_foriraq/89342" target="_blank">📅 01:23 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89341">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🇮🇷
اطلاق عدة صواريخ ايرانية.</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/naya_foriraq/89341" target="_blank">📅 00:35 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89340">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🇮🇷
اطلاق عدة صواريخ ايرانية.</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/naya_foriraq/89340" target="_blank">📅 00:34 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89339">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/naya_foriraq/89339" target="_blank">📅 00:33 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89338">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/95c097e8b2.mp4?token=ayLX3DW3y1sVnAvjAoQta7H-qa6xdXczo6Qx2zx1imxbfZWc1se-dpQlx1r0Ti05500jQBzizAH92HK-SvunSKquh-S3VYwb631Atx3IK38J-Y1shAuFbahL8PZMUCzC21P6QKosA57L3M0IOzDe3NtfVlONcRf8c6TFkyCSqC5AsHIfo2ZGIga6Bxrrz7rr3iP6TJM2jjG85IdvAutOA-zoChAahqY62z_d7rd4fFa8TWaIYQPZL80BKimJ_Klgrmu9FmJ0pDaoAIFwP6j0JMq2kxWNlyPfJcpsDv3zNlZrbYKYbXa8EOAd4ET6cuw_G2yUAz_n4yAKg8EL4K4rkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/95c097e8b2.mp4?token=ayLX3DW3y1sVnAvjAoQta7H-qa6xdXczo6Qx2zx1imxbfZWc1se-dpQlx1r0Ti05500jQBzizAH92HK-SvunSKquh-S3VYwb631Atx3IK38J-Y1shAuFbahL8PZMUCzC21P6QKosA57L3M0IOzDe3NtfVlONcRf8c6TFkyCSqC5AsHIfo2ZGIga6Bxrrz7rr3iP6TJM2jjG85IdvAutOA-zoChAahqY62z_d7rd4fFa8TWaIYQPZL80BKimJ_Klgrmu9FmJ0pDaoAIFwP6j0JMq2kxWNlyPfJcpsDv3zNlZrbYKYbXa8EOAd4ET6cuw_G2yUAz_n4yAKg8EL4K4rkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇹🇷
اشتباكات مسلحة مع عنصر من تنظيم داعش الارهابي في مدينة اسطنبول التركية واصابة شخص واحد كحصيلة اولية.</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/naya_foriraq/89338" target="_blank">📅 00:16 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89337">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🇮🇷
الخارجية الايراني:
‏
أكدت الحكومة القطرية، في وثيقة رسمية قدمت إلى الاتحاد الدولي للاتصالات، أن الضربات الدفاعية الإيرانية ضد القوات الأمريكية المتمركزة على الأراضي القطرية "كانت موجهة نحو المنشآت العسكرية الأمريكية. [...] ولم يتم استهداف أي مناطق مدنية".
‏الاستثناء الوحيد الذي ادّعته قطر هو الهجوم على منشأة غاز في 18 مارس/آذار. لكن تجدر الإشارة إلى أن المنشآت التي استُهدفت في ذلك اليوم كانت تخدم العدوان العسكري الأمريكي على إيران.
‏يتناقض هذا بشكل صارخ مع سجل الولايات المتحدة الطويل في شن هجمات متعمدة على أهداف مدنية - المدارس والمستشفيات والأحياء السكنية وحفلات الزفاف والجسور وغيرها.
‏هناك فرق شاسع بين أمة متحضرة تعلمت أهمية الالتزام بالمبادئ الأخلاقية والإنسانية حتى في ظل الظروف الأكثر إيلاماً، وبين الحكام المتعطشين للحرب الذين لا يلتزمون بسيادة القانون أو الأخلاق في ممارسة سلطتهم.</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/naya_foriraq/89337" target="_blank">📅 23:24 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89336">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🇺🇸
ترامب:
كان لديهم ثلاثة مواقع، والآن ربما يكون لديهم جبل الفأس. لقد تم تدمير المواقع الثلاثة... لدينا كاميرات في كل منطقة رئيسية من المواقع الثلاثة الأولى، ولدينا أيضًا كاميرات على جبل الفأس. نحن نعرف كل من يدخل ويخرج.</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/naya_foriraq/89336" target="_blank">📅 23:21 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89334">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🇺🇸
ترامب
: لقد فعلت الصواب بشأن إيران، أريد فقط إنهاء الحرب في أوكرانيا، لم تكن المملكة المتحدة موجودة لمساعدتي.</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/naya_foriraq/89334" target="_blank">📅 21:53 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89333">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">انفجار عبوة ناسفة في صحراء محافظة الانبار غربي العراق</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/naya_foriraq/89333" target="_blank">📅 21:41 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89332">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/857088ab20.mp4?token=Iv7Wi-ymEgnKWxMc7A688RX0v4rDVLCF7bEqz0_LQCL9yW48oBGMV-oFrrYw_-nzVZvJ07tp-zu2GeL7kdkmCVjl8619RW5bDfaiAD8LLjswQW7Gq-sakA5fl74DKzhRtGcpBvmOvupKU9uT5bR-EUZ10eIGfGBWNlYDEvpRqsSonb-VIBw55l8a8UyPVDPPO-VwBmhTx-of_q8jruMR-Mcj0QROKoSMLsK7MWKwvP4VpQEeeEiJ6l0cDp_W8eYDo73zQ2GALRP0IyJhwdXqAaC9xg5gPqvTifd9YVtpe1rZgyL9IUyaw8PvALddm_1dcaza4IDxNoTAEnaSrZHCnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/857088ab20.mp4?token=Iv7Wi-ymEgnKWxMc7A688RX0v4rDVLCF7bEqz0_LQCL9yW48oBGMV-oFrrYw_-nzVZvJ07tp-zu2GeL7kdkmCVjl8619RW5bDfaiAD8LLjswQW7Gq-sakA5fl74DKzhRtGcpBvmOvupKU9uT5bR-EUZ10eIGfGBWNlYDEvpRqsSonb-VIBw55l8a8UyPVDPPO-VwBmhTx-of_q8jruMR-Mcj0QROKoSMLsK7MWKwvP4VpQEeeEiJ6l0cDp_W8eYDo73zQ2GALRP0IyJhwdXqAaC9xg5gPqvTifd9YVtpe1rZgyL9IUyaw8PvALddm_1dcaza4IDxNoTAEnaSrZHCnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
‏فانس: لا أعتقد أن لدينا أي معلومات بخصوص هجوم الزفاف، الولايات المتحدة لا تستهدف المدنيين أبدًا في القتال، ولن نفعل ذلك أبدًا.</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/naya_foriraq/89332" target="_blank">📅 21:33 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89331">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🇺🇸
وكالة فارس: ارتفاع عدد الشهداء في الهجوم الأمريكي على حفل زفاف في سيريك إلى 5 أشخاص.</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/naya_foriraq/89331" target="_blank">📅 21:32 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89330">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BABPz_Lr9o4wCTdETRbCcq1B6kqoPmQ7jfbG4r44HAHOtKEo8B34bJMdmMvZOIHirkbOL1vyAp1MC5DE2eytgMjgYt_b6zJXBgffhYl3PWrDm3z8Jx7jqlcLIMQA2arBvVW2uo3N3c7vHcmRGQb-y0lfAANAXy1hpTA2cO2XwFimPTyvkNhnM4zfu7Fsph78UyU8LPdvZIHp1Lk5PSNOPVSeHH9FGj09NhIh_yd_81pfvEzIOSODc3w_3OlnVAB2_TbUDHpdAKlEwe0Qn0nMcjvyFqZv2HjwubhTwyitHLdPpXa6eBYQknpCLBJaNEtz15XJDI7987Zvg9CgF5VZvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
🇦🇪
طائرة مسيرة مجهولة المصدر تحلق قبالة سواحل الجمهورية الإسلامية في إيران وبسبب التشويش تظهر كانّها داخل اجواء ايران .</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/naya_foriraq/89330" target="_blank">📅 21:06 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89329">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🇮🇷
انباء متداولة عن إطلاقات من ايران نحو المصالح الاميركية في المنطقة.</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/naya_foriraq/89329" target="_blank">📅 20:58 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89328">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🇺🇸
الاعلام الاميركي: ‏
قال ترامب إنه سيطلب من الدول الأوروبية تعويض الولايات المتحدة عن المساعدات العسكرية والذخائر التي سبق إرسالها إلى أوكرانيا، في حين بدا أنه يشير إلى وقف المزيد من المبيعات للدول الحليفة.</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/naya_foriraq/89328" target="_blank">📅 20:54 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89327">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🇺🇦
زيلينسكي
: روسيا أحرقت مصنعًا لشركة "كوكا كولا" - وهي إشارة واضحة إلى أمريكا
😫</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/naya_foriraq/89327" target="_blank">📅 20:53 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89325">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vkw-q-SHnK8gVUnPLS9m0NF5OeW9f7wKLzgKPsFUD7_JX8atFCy0uFX23EaGHNVdCFnvslnGMRE36lmF9lykALIijVygEf1tsQNbZcOphr92rPIP6LdOruvnBInjmcAHLAoV0eJQMn4ckDX2weyhfN4Z1x67xeAIOXklZmmPx27MrLe4U9fryMi8Iz-MuKyDTOHYRaS5NEAt5zy-Fe3hEGx4Q3wLhm1a3eHUrjVHaf0wZsv0RswMvd7TwX9WKvN7e2fe1BpHeyXteqpzKvxuYAi83XXeCx4kOq27PMIecYdx1Fd3s08alepds75H4qBFXiQOlevmUdthnnyhHx7arw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
‏
قاليباف
: ابذل جهدًا أكبر يا بطل. كأن مستقبلك المهني يعتمد على ذلك (لأنه كذلك بالفعل). أو استنزف مواردك إلى ما دون مستوى الخطر وشاهد كهوفك تنهار (مع مستقبلك المهني). أو صلِّ لآلهة الملح في برايان ماوند.
‏العالم لديه بالفعل ما يكفيه من الفشار</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/naya_foriraq/89325" target="_blank">📅 20:15 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89324">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🇮🇶
وزارة الاتصالات العراقية:
وجهنا بتخفيض أسعار الإنترنت المزود لدوائر الدولة كافة بنسبة تخفيض 40% (السعات ثابتة والسعر منخفض -40%).
كما وجهنا بزيادة سرعات إنترنت الأبراج المزود للمواطنين في المناطق التي لم تُغطَّ بخدمة الكيبل الضوئي وبنسبة زيادة قدرها 40% (السعر ثابت والسعات مرتفعة +40%)، وتلتزم الشركات المزودة للإنترنت بسياسة الوزارة المتضمنة باقتين فقط (باقتين لاشتراكات الأبراج واربع باقات لاشتراكات الكيبل).</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/naya_foriraq/89324" target="_blank">📅 20:06 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89323">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lUjXcwZgrKs6M_VA5Jf1KryNuciWY8YKl32T1pVPwrSlUhjwRwVgcU5GZn94jv-ypZeZ5j0cKXE8I6qFQp9HS3F2DuGwtNaxSf0Lhr5ilAw9WqAotNhm2BRUlXx66j_yY96qvmHGJ-OpQuRI8EHY48O6GCOBPA8pGo1gAxJPWdJDUVPQ9Uw4Xvo00lCD2xzkzHYc1170qgtDKmI9eoY5rK_HfSWMl0_1qaRZcTGNrQpRLFG3pSr27HKAM0vyf5aMcxIn6ajbi132u52-Zsa62_yrSZkIphKFhgh7dpX0kDxuLowq0uGvvkVx0crc09fZm18yemS9cwgkR0CwzuNhMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
🇺🇸
الولايلت المتحدة تضع مكافأة لمن يدلي بالمعلومات عن قائد قيادة العمليات السيبرانية التابعة للحرس الثوري الإسلامي، لاستهدافه البنية التحتية الحيوية للولايات المتحدة.</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/naya_foriraq/89323" target="_blank">📅 20:01 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89322">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e7aabb08e2.mp4?token=q0SzXyIF3Ui3beZZq7aM44xspbOTp1aGReP50xF0DRpROVizh4I0WPhrd2Xj8H3pb5ZckBiVI-5L2pBaPt6si6aOhFJpjTeHg6R9-iKzxOYA_GBubxiwJbYYjL9vadRf8YueZW8qyfbMABmC1Sxk3tJQKifLGE9OHEt49sHsxlAJxa3mBXOGy-bWwpUrQ8UiHJMlLiaiENjbthk9mCxRBSKzh9zZMNtv1ZTDxrtnnndzy7fEjza8l9Ptd1fWtCWsbKQ9dFy--nF_C0pfcKNxZ23ENzduUl45zHmpGyGEVFCyr1EQsrHeO-u1gkGUM9f21MvJWvqbcr3L33aGjIPEXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e7aabb08e2.mp4?token=q0SzXyIF3Ui3beZZq7aM44xspbOTp1aGReP50xF0DRpROVizh4I0WPhrd2Xj8H3pb5ZckBiVI-5L2pBaPt6si6aOhFJpjTeHg6R9-iKzxOYA_GBubxiwJbYYjL9vadRf8YueZW8qyfbMABmC1Sxk3tJQKifLGE9OHEt49sHsxlAJxa3mBXOGy-bWwpUrQ8UiHJMlLiaiENjbthk9mCxRBSKzh9zZMNtv1ZTDxrtnnndzy7fEjza8l9Ptd1fWtCWsbKQ9dFy--nF_C0pfcKNxZ23ENzduUl45zHmpGyGEVFCyr1EQsrHeO-u1gkGUM9f21MvJWvqbcr3L33aGjIPEXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇱
🇸🇾
في خبر معتاد...
الاحتلال الصهيوني يشن غارة جوية على العاصمة السورية دمشق.</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/naya_foriraq/89322" target="_blank">📅 19:51 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89321">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🇮🇱
‏
نتن ياهو للمرة المليار:
نحن على ثقة بقدرتنا على إسقاط النظام الإيراني. هذه هي المهمة الأساسية، وهي وشيكة التنفيذ.</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/naya_foriraq/89321" target="_blank">📅 19:39 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89320">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">انباء عن اطلاق صواريخ باتجاه مضيق هرمز</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/naya_foriraq/89320" target="_blank">📅 19:28 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89319">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f-5Cz3H2UA7MuphOtj1Dvmov2fScpmZ04rs9EoHT6wY9Mo4Kvass6SKmrXXIkKtP9G7Ss_oENBGvxOSgscSwrJe_4LAnH-tB30iZ4222Tzwcur-k0t5CRZ9IaUndl5ruQdqxGeRPn2_OoHQfyOwVdfdoxy_KSDxLh3zEi9LTw2C5wpM94mN-6aCvfmMNoclfM9IA4GLnScPyHAN1xgbRcqlQ2bc6CMI3Htrtubw2t2TxGiYAhFYEv5mjyX-ojZebWxiIa-aOjgYUzMoVJgDKGmg_eYIDFXOzSA19ZrvUoUcgi5IpZ1pes5cww95NHg5lbqzUjm4XP8_R3sdPJLTArQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامب يهدد كندا:
من الجيد جدًا للسياسيين الكنديين مثل رئيس الوزراء كارني أن يجعلوا الرئيس دونالد ج. ترامب "عدوًا"، إلى أن ينهار اقتصادهم، وعندها سيثبت أنه سيء ​​للغاية للسياسة، أسوأ من أي شيء حدث لسياسي كندي على الإطلاق. ترقبوا فقط!</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/naya_foriraq/89319" target="_blank">📅 18:46 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89318">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">توقف ادوات الذكاء الاصطناعي Claude وGrok ايضا</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/naya_foriraq/89318" target="_blank">📅 18:33 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89317">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y5RA6yn5xXaoS2H27Li0BpEyu0QPzyRCpsAwU6cXDkxTykEoKzG1Vi9ELrT5FwMyR4YyA8J_JYNv0jOMkyGhmshdWhvdAnbVGWGhGjiqKFE63VdAyC3WIKIlHHtfF_UGqD1qFMvuB6WEM7QFy5alzAZSFMUhumSWmc9dRZuZ_FM1i6mLLDKIxnolkfzFAACnFvt0XWJul6v50wC4_bTlB96Orx9mANF-JqW2aCVxC6mn17VkyIyC9S-zYWtujPOFoceTzHocyop8weNUkBtvKrtZvjJtpIOvQYf6_JXDTm3l2a9UG-LLk6-e9Q8QwPophwuLytutoxpfzMPLDG4hnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
🇺🇸
ترامب:
بالنسبة للخونة الأوغاد الذين يرفضون الإبلاغ بدقة عن عمليتنا العسكرية في إيران، لدينا كميات غير محدودة تقريبًا من الذخيرة متوسطة إلى عالية الجودة، أكثر بكثير مما يمكننا استخدامه في هذه الحرب، أو في أي حرب أخرى (وهو أمر مستبعد للغاية!)، والتي قد تندلع بشكل غير محتمل. بالإضافة إلى ذلك، فإننا ننتج الذخائر بمستويات لم نشهدها من قبل. نحن نخزنها ونستعد لأي طارئ قد يحدث. نحن نأخذها لأنفسنا، الولايات المتحدة الأمريكية، بدلاً من بيعها للآخرين، لكن المبيعات للحلفاء ستبدأ قريبًا مرة أخرى. أيضًا، يرجى العلم أن إدارة بايدن قدمت ذخائر لأوكرانيا أكثر بكثير، دون أي تكلفة عليها على الإطلاق، مما استخدمناه في إيران. تم منح مئات المليارات من الدولارات لأوكرانيا وحلف شمال الأطلسي مجانًا، والتي كانت أوروبا ستدفع ثمنها لو طُلب منها ذلك، لكننا سنطلب تلك الأموال، وإن كان ذلك متأخرًا بعض الشيء!</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/naya_foriraq/89317" target="_blank">📅 18:30 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89316">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S6_drTesdzkELLV8VyM_lAF_0jzNzzTTc6B81DiPuwb64DSDAuh8gLaAbYW9hOMxQmQRS-9zBYorhy7sNfRAURm5uLpdP9NP5mhGEqDAvOHWnQW4RgOj48zaeR3SthsU0ev_MWZkSmluvqy5m0TEuRcDb-CweYw7NmLlGRTgKlDpD0gL_KxlG3vQkV7XRZ4CQMx5ck8d6AYWbePHmN93IPTJV0eTqrbnRE7LAxuRSM3zc22zLfH5A1BeTJ4lyYF7UAlptvKY5PmNMw77KVjGRxgQeR89Qg3xprEe_3B_lXjWXfMjO7peOmXpPpj52Or6lFngKwIJ2b3Uoe4oGuSfgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#تقني
▫️
توقف تطبيق الذكاء الاصطناعي ChatGPT عن العمل لاسباب غير معروفة.</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/naya_foriraq/89316" target="_blank">📅 18:29 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89315">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/snr4C70IRsRR7SrNZII-dJSkCBv9ORKiOKg09GESJmGT37W3xx3UBqNjtYELRCOphTK8ONrpzTon6T4H-EqinSPb4k0XbCYh5hZQLUjmI0RnLsDBeXJNFZ2N2ZsGxL9KK9ZHWp-gQc5bFUnUlVbIDBnamNopmz4KFLu2KQaN9wkzlb_-as1ekQNediU2N92oGdcy0zzLve8W1VRpxRHscn4cFmzwv0W4YbcnUq4e67VyhQ1EceIyt2WI3X9XmyYAbKkU3GiaPzybO3afA-d-sE2LNuMo81_cU9WUtucOCgdmGisoAfhdo_XHNIqamT0xq6OEfjuop_LPoodjj7ttSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
🇺🇸
‏
ترامب:
إنّ الأشخاص ووسائل الإعلام الذين يصرّون على حقيقة أننا لا نملك ذخيرة (وهم مخطئون تمامًا!)، هم في الواقع خونة. يفعلون ذلك لأنهم يفضّلون أن تخسر الولايات المتحدة حربًا ننتصر فيها بسهولة، على أن يروني أنتصر!</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/naya_foriraq/89315" target="_blank">📅 18:28 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89314">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">#تقني
▫️
توقف تطبيق الذكاء الاصطناعي ChatGPT عن العمل لاسباب غير معروفة.</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/naya_foriraq/89314" target="_blank">📅 18:27 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89313">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🇺🇸
وكالة فارس:
ارتفاع عدد الشهداء في الهجوم الأمريكي على حفل زفاف في سيريك إلى 5 أشخاص.</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/naya_foriraq/89313" target="_blank">📅 18:19 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89312">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🇮🇶
ارتفاع صادرات العراق من النفط الخام إلى 2.340 مليون برميل يوميا وهو ما يعادل 71% من الصادرات النفطية قبل اغلاق المضيق.</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/naya_foriraq/89312" target="_blank">📅 18:07 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89311">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sd_SJgNISFTic9_ogmnfpPVYQEce96HWLiupP8bvY8S9alcCkUdD3jS8eyHEkC9xeBWb6FhnQhWT17Bg-l8jzyleeuSKbfzMeZln-1l-JfmJfJBZ9cXDlLOZSG1TeVk13qb1x6IK28sv65YljXzF1gCAqokdvY7L5INxFIQwF_F6psm90d0s0v42Xh32DLPhV2K67J-r9mfQ0IrR4TUhwX_24ZTx_wO9Mehpj2ZnCKZxkISZoV90koIzeqVp0XDgTf2w45qU_qtCUTbOm836iTXzF-l7dibIJdk7WzUAQ64vDTPudQLMqmEEKt0SAGWkwPQaZ5fg6gaXkw6Li7VHgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارحلوا أيها الجبناء
تسقط الوصاية الأمريكية على العراق</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/naya_foriraq/89311" target="_blank">📅 17:39 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89310">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">اعلام العدو يقول ان السلطة اللبنانية سلمت الكيان خرائط وصورا لمقابر ومواقع أخرى يحتمل أن تكون فيها أدلة أو رفات لجنود صهاينة</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/naya_foriraq/89310" target="_blank">📅 17:29 · 12 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
