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
<img src="https://cdn4.telesco.pe/file/PGqyEqUtd610dwLFnQxhjIAX8EZDXSSnPsmic5sQp4kiXpSxBFjnoLFjOZna8MCyfIlIijoEg8AMlvqfBAGLBwD-WedCcKluuXbRpS1-IpWmAD04ONSs3wfoKYwLntoqxOqOg1rGbMZj6FqWoppj-w7VryBayZSoSN9NV4YtYbmtCJnbweab0h6ZVDmf-ZTnCKzciRV5cn9xpa4GtaXlMWNP1HWjwhdxXMna5gjLinBLcHQR0Q4RHHWXzgSmD-wtBfTzesCGUeLZDKb8olSrl0iX4sRVdypmLYKgxsrFji2MOw4b9DXMDRyvnbnG622dV3PtoQVyaTbhdgfkWILkJg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 257K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-19 21:58:03</div>
<hr>

<div class="tg-post" id="msg-77960">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">الناطق باسم القائد العام للقوات المسلحة صباح النعمان:
عملية حصر السلاح بلغت ذروتها المُلزِمة ولا خيار خارج مظلة القانون.
-إنهاء المهمة العسكرية للتحالف الدولي أواخر أيلول المقبل استحقاق غير قابل للإرجاء.</div>
<div class="tg-footer">👁️ 9 · <a href="https://t.me/naya_foriraq/77960" target="_blank">📅 21:58 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77959">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromنايا - NAYA</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JcMxIF4eihdNiO9Sr8qwFKaxATdbpJ4O1InmYH-UESJBOMsCnMPCG51BPrFjXsQwVF_ggCrQiX8WyjtWYJoZlaPHbI3Njz2U8Uaecmy9reGD-4RPilL-tbzE0hEN-cUlc52yhr_84IS3wN9Dd4x5wmr0h6tbywnPBiPZs2zceKRKkqps1DKlrjqCPMbAbAR7y68sQ-C4I4zf7cEcQ4Cvx29PxKJIGcW4uXgW8h9TRptqfZUicsJ2mSofTJT09q4PzZsg1g7Jm3cZn-HSV-o3zagxJJRwwFhbVnYX_DKmwzDYZ_1tb2Omd7l1bRuOet1KFSZnIHzfG2E_HOMIBNzhpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سنجعل عاليها سافلها
بلا أسقف بلا خطوط حمراء بلا قيادة بلا تفاوض ، سوف نشعل المنطقة .</div>
<div class="tg-footer">👁️ 22 · <a href="https://t.me/naya_foriraq/77959" target="_blank">📅 21:57 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77958">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">ترامب بشأن إيران: الأمر في الواقع بسيط للغاية. الفائز هو من يمتلك القوة. نحن نمتلك كل القوة.</div>
<div class="tg-footer">👁️ 955 · <a href="https://t.me/naya_foriraq/77958" target="_blank">📅 21:56 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77957">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">ترامب بشأن إيران: الأمر في الواقع بسيط للغاية. الفائز هو من يمتلك القوة. نحن نمتلك كل القوة.</div>
<div class="tg-footer">👁️ 1.9K · <a href="https://t.me/naya_foriraq/77957" target="_blank">📅 21:55 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77956">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromنايا - NAYA</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f5b4b73175.mp4?token=QLAUOOTSP-IDGaYT99B2tYSDIJ9gbwPSruQ-2MVWrVatVE7CMntjKZQdf_CANzAtegayn3VvN1fjQXDclfLeIfzlvX6yYW44C6IhEOsWZK2mmuyTmUKnUIA-XZrN3yD0yFRVsQzWMNJpkVPAWqmcG5AFTdpPrFJlE7YKfrZpjY3cFgIDO2p1J7McWXLxfERwtyxXd3q5b86EckH9Z5xgTaRPT0xpO0TruLIYfCe7KwBpjCe4MfZEF5sa03CEWyiSOk529Fh2mYI-_-dT_8v2JVLAvK4tl1-Zft5D5PaMKn9qU5cbpv614YH_j-E2WnjgaKWz0X2_Rv8Go8m0fDH10agk6GXHToN9VlhVSQN336PddtrLNEdXdZvqbn8f_25CWkyLG5xugF0MkSvZ0XHxAiYvoumWZFOK1p5Pb0OmSW-6nNWRjKN672dsLZjS5bw_OzvkqywGk7kaZeAkCAwEX7DUj3XMCma80a7Qt86l8MXx0vFalVxFYco4u98EVo7U6tiU3Hh4kI7EvUjRl0pGNVdDcofnjGLoRzg8pYWhOwCIQ_TuWTsQ_9l_0ylLy0FVvi5pTsYS9jCKpH3LmPvaE8oSeQgliJv0oO9Y-EL0M6xCIqzypsQAkPHZHmZlDEOtcZPemmiNQL5PmQAnjnAFW3ayjlTqCHVFboGnKLiSW8M" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f5b4b73175.mp4?token=QLAUOOTSP-IDGaYT99B2tYSDIJ9gbwPSruQ-2MVWrVatVE7CMntjKZQdf_CANzAtegayn3VvN1fjQXDclfLeIfzlvX6yYW44C6IhEOsWZK2mmuyTmUKnUIA-XZrN3yD0yFRVsQzWMNJpkVPAWqmcG5AFTdpPrFJlE7YKfrZpjY3cFgIDO2p1J7McWXLxfERwtyxXd3q5b86EckH9Z5xgTaRPT0xpO0TruLIYfCe7KwBpjCe4MfZEF5sa03CEWyiSOk529Fh2mYI-_-dT_8v2JVLAvK4tl1-Zft5D5PaMKn9qU5cbpv614YH_j-E2WnjgaKWz0X2_Rv8Go8m0fDH10agk6GXHToN9VlhVSQN336PddtrLNEdXdZvqbn8f_25CWkyLG5xugF0MkSvZ0XHxAiYvoumWZFOK1p5Pb0OmSW-6nNWRjKN672dsLZjS5bw_OzvkqywGk7kaZeAkCAwEX7DUj3XMCma80a7Qt86l8MXx0vFalVxFYco4u98EVo7U6tiU3Hh4kI7EvUjRl0pGNVdDcofnjGLoRzg8pYWhOwCIQ_TuWTsQ_9l_0ylLy0FVvi5pTsYS9jCKpH3LmPvaE8oSeQgliJv0oO9Y-EL0M6xCIqzypsQAkPHZHmZlDEOtcZPemmiNQL5PmQAnjnAFW3ayjlTqCHVFboGnKLiSW8M" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">We are ready for them …</div>
<div class="tg-footer">👁️ 3.5K · <a href="https://t.me/naya_foriraq/77956" target="_blank">📅 21:49 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77955">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p8I0EA0-LH3hoNcNm2JwnsT-ScafHhCV5Gu4Fce-MhRKAxQUigFq9hqj16-he5h4eZoPFJ9FvMxp7zHRITGf7hz58omzbosFrPLXobrX9aVhQnAMa8f1s7D-Ht4IP6_v4FUlRJ2HJEWr65k8bCh5OJ-eN8sPZIio7QYcrn3H6axUdFoDnSu3g0SXemtcm6e02hp-Lp5jBQvqpXOxL3qoFOUTX2UiZgDbPHmDBsJPXcK0pSzlJmbS9m5TA9Nf-kobJsrmIq-mJ10UuSuujsZp6Y9eeh3y8yoG_0BuYaq1usTCaS9RP7jl213vDa1_n6vZnQnpySgxKHyNRvJVWcDYSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عراقجي:
‏
إن القوات الأجنبية القريبة من أراضينا معرضة لخطر دائم بسبب أخطائها البشرية، أو الحوادث العرضية، أو احتمال وقوعها في تبادل إطلاق النار.
‏لتقليل المخاطر، فإن الحل الأمثل هو رحيلهم.
‏نحن نفضل لغة الدبلوماسية، لكننا نتحدث لغات أخرى أيضاً.</div>
<div class="tg-footer">👁️ 4.78K · <a href="https://t.me/naya_foriraq/77955" target="_blank">📅 21:44 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77954">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🇮🇷
عضو في البرلمان الإيراني:
إذا كان الأمريكيون يعتزمون انتهاك وقف إطلاق النار أو شنّ أي عدوان، فلن تتهاون إيران مع أي طرف في الدفاع عن نفسها. جميع القواعد العسكرية الأمريكية في المنطقة تقع ضمن نطاق قدراتنا الدفاعية، وسترد إيران بحزم وحسم على أي تهديد إذا تجرأ العدو.</div>
<div class="tg-footer">👁️ 6.05K · <a href="https://t.me/naya_foriraq/77954" target="_blank">📅 21:36 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77953">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">⭐️
إعلام العدو:
أمريكا سلمت ايران عبر ابو ظبي ٣ مليار دولار لكي لا تقصف اسرائيل مجددا.</div>
<div class="tg-footer">👁️ 7.28K · <a href="https://t.me/naya_foriraq/77953" target="_blank">📅 21:31 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77952">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🏴‍☠️
إطلاق صواريخ اعتراضية فوق نهاريا دون تفعيل صافرات الإنذار.</div>
<div class="tg-footer">👁️ 9.29K · <a href="https://t.me/naya_foriraq/77952" target="_blank">📅 21:11 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77951">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🇺🇸
مسؤولين أمريكيين:
غير واضح إن كانت المفاوضات مع إيران ستستأنف بعد تعهد ترمب بالرد على إسقاط المروحية.</div>
<div class="tg-footer">👁️ 9.26K · <a href="https://t.me/naya_foriraq/77951" target="_blank">📅 21:09 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77950">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🇺🇸
إعلام أمريكي:
أفاد مصدر مطلع بأن طائرة أباتشي تعرضت لهجوم بطائرة إيرانية مسيرة من طراز شاهد. كما أكد مسؤولان أمريكيان أن طائرة مسيرة إيرانية هي التي أسقطت المروحية.</div>
<div class="tg-footer">👁️ 9.54K · <a href="https://t.me/naya_foriraq/77950" target="_blank">📅 21:07 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77949">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 9.2K · <a href="https://t.me/naya_foriraq/77949" target="_blank">📅 21:07 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77948">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🇺🇸
ترامب: تلقيتُ للتوّ معلوماتٍ من جيشنا العظيم تفيد بأنّ الإيرانيين أسقطوا ليلة أمس إحدى طائراتنا المروحية المتطورة من طراز أباتشي أثناء قيامها بدورية فوق مضيق هرمز. كان على متنها طياران، وكلاهما بخير ولم يُصب بأذى. ‏مع ذلك، يتعين على الولايات المتحدة، بالضرورة،…</div>
<div class="tg-footer">👁️ 9.17K · <a href="https://t.me/naya_foriraq/77948" target="_blank">📅 21:06 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77946">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fea4dbbdb9.mp4?token=B1hHcbKrBhjWTcNqto_6RKMqGZ71n4W-98DJ__j1WQ7TgjP4IHOce-s_vRpRQ79ZNF6qPawNCcJseA3w3D5BDr5mk_kBLJgFuxvgUOF10sEklV6dcQ815olMAW43TKpNq5k8Qt7hNXnH89N9SBeX86gM14I2buhTSBJDgCBO4xl9HQp-hxF4mJDfYyiSyRHi7mDaD62xMvJk49mEeFtbKJYm0Wt5s3aXSfCcGWxRI-1ohTgAOlKBrIyeHvOVTeDjui-KEiI38y7GXNyQfD-ZNojQOxbtcTO4Zx5e4XtaPIgyt13KRlfUXYTcZtShdq7QnM1x5zsvGHzvn1qVq6se3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fea4dbbdb9.mp4?token=B1hHcbKrBhjWTcNqto_6RKMqGZ71n4W-98DJ__j1WQ7TgjP4IHOce-s_vRpRQ79ZNF6qPawNCcJseA3w3D5BDr5mk_kBLJgFuxvgUOF10sEklV6dcQ815olMAW43TKpNq5k8Qt7hNXnH89N9SBeX86gM14I2buhTSBJDgCBO4xl9HQp-hxF4mJDfYyiSyRHi7mDaD62xMvJk49mEeFtbKJYm0Wt5s3aXSfCcGWxRI-1ohTgAOlKBrIyeHvOVTeDjui-KEiI38y7GXNyQfD-ZNojQOxbtcTO4Zx5e4XtaPIgyt13KRlfUXYTcZtShdq7QnM1x5zsvGHzvn1qVq6se3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⭐️
إنفجارات تطال خط أنابيب الغاز الرئيسي في جمهورية داغستان.</div>
<div class="tg-footer">👁️ 8.52K · <a href="https://t.me/naya_foriraq/77946" target="_blank">📅 21:05 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77945">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/97029f70e0.mp4?token=sjrKinvUjVPjMlirF4YJf4fgLmsvqn85e52c4zVOpyf_yZRH9N5-YTBsEpVltb7E3P6KNFF0tZ10f0Gqn5DreuHnQtlvLmAgvWybDRbjFjLb2j0YgI-nWcIfyOvappndXkAUuBzK_5zG3eF1PUmKu4d8WYOfyaQU3n4eWIie7Zhlt7UYrif90Ic_75ETXmf4dCHFBZpTuRxXn3i1VetkEwf4o2-wxMIa_aFbzffkkpHvVYV5E19JjDMDnPcbD3lH5EuBs6ys5CFiu8NhArn71SmDiiOPUhMWLkuwci7SaQSyHUtZAf19pReP-L1ydjXBBu_paJwtuCb5pe2Rmng1ZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/97029f70e0.mp4?token=sjrKinvUjVPjMlirF4YJf4fgLmsvqn85e52c4zVOpyf_yZRH9N5-YTBsEpVltb7E3P6KNFF0tZ10f0Gqn5DreuHnQtlvLmAgvWybDRbjFjLb2j0YgI-nWcIfyOvappndXkAUuBzK_5zG3eF1PUmKu4d8WYOfyaQU3n4eWIie7Zhlt7UYrif90Ic_75ETXmf4dCHFBZpTuRxXn3i1VetkEwf4o2-wxMIa_aFbzffkkpHvVYV5E19JjDMDnPcbD3lH5EuBs6ys5CFiu8NhArn71SmDiiOPUhMWLkuwci7SaQSyHUtZAf19pReP-L1ydjXBBu_paJwtuCb5pe2Rmng1ZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴‍☠️
إطلاق صواريخ اعتراضية فوق نهاريا دون تفعيل صافرات الإنذار.</div>
<div class="tg-footer">👁️ 9.13K · <a href="https://t.me/naya_foriraq/77945" target="_blank">📅 20:56 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77944">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🏴‍☠️
إعلام العدو:
تحذير نتنياهو لمجلس الوزراء - قد نضطر للتعامل مع الإيرانيين بمفردنا، دون دعم أمريكي، وبكل ما يترتب على ذلك من تكاليف.</div>
<div class="tg-footer">👁️ 9.08K · <a href="https://t.me/naya_foriraq/77944" target="_blank">📅 20:50 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77943">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">⭐️
‏
شركة CMA CGM للشحن:
تكلفة تجنب مضيق هرمز وصلت لـ 300 مليون دولار في 2026.</div>
<div class="tg-footer">👁️ 9.06K · <a href="https://t.me/naya_foriraq/77943" target="_blank">📅 20:49 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77941">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ewK9Q1G4lzsCqGuDCDFw-9niVj7eE58DUj_v57ydWxYHWLRhopld1GFveKH97MMtUUTpRwp-TYMjBXTp7Ti9C6ZCoDyNIG1e-6SpbQwrZ0sW5Wu2eKEVZ8D5w-SS0uh2hGprQhfrOgF8l8gxrIMr84VILcP4Ah_O56DLc2W5Qh5MW_bAra4900fTZNH4qCpsS9mwKbYICD3D6WD3kuX9xQvaTvXLUh7FTSsRdOWoE8jvT3FSoyEWiSUKHIul8kQVLafVsU011fYUwJIH6qMoE696ZILaktYQ4CfCukWKUAOjboJra-kCOSZiaS3vrpDTb4KLQqEZ6ixvwE33lBZ-Sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b837162cfc.mp4?token=BEw7QTqcc3hpBDnh6AYRSeiA-DdPB0idbSB2Ta0nF8yQ1jZGm6xomzqqw04ydSp5z9EMZca_3INlwO--_UBsCexNt-9kyaCQASrV-P0UhPNqhVdKKYVrtvUseE2MlYGI5mHYcDDqDkoviQeWC231Vy_7aneHW1ee1zI-GezWy0MUudnz1Q1jIJij-p5xca1N26XWlUPSej9NJcm5_OSkLEx8CrX2-E6hr3AJ33YhcFUZEIA3AAt670N06TTdT2wasYO3HvJZ8Moi-R0m8_p2rqp10mT6mSaztJpjtWvWC3OQ0lEP-VyKDfiPTgNg1oULBqdX-ZsT4III6CvRbgjzHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b837162cfc.mp4?token=BEw7QTqcc3hpBDnh6AYRSeiA-DdPB0idbSB2Ta0nF8yQ1jZGm6xomzqqw04ydSp5z9EMZca_3INlwO--_UBsCexNt-9kyaCQASrV-P0UhPNqhVdKKYVrtvUseE2MlYGI5mHYcDDqDkoviQeWC231Vy_7aneHW1ee1zI-GezWy0MUudnz1Q1jIJij-p5xca1N26XWlUPSej9NJcm5_OSkLEx8CrX2-E6hr3AJ33YhcFUZEIA3AAt670N06TTdT2wasYO3HvJZ8Moi-R0m8_p2rqp10mT6mSaztJpjtWvWC3OQ0lEP-VyKDfiPTgNg1oULBqdX-ZsT4III6CvRbgjzHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⭐️
صور الأقمار الصناعية تظهر أضرار في رصيف نقل الغاز الطبيعي المسال التابع لشركة أدنوك داس آيلاند في أبوظبي بالإمارات؛ ‏يظهر على اليسار ضرر أصغر في صندوق التبريد، بينما يظهر على اليمين سواد أكثر وضوحًا على المعدات المساعدة.</div>
<div class="tg-footer">👁️ 9.66K · <a href="https://t.me/naya_foriraq/77941" target="_blank">📅 20:44 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77940">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🇺🇸
ترامب: تلقيتُ للتوّ معلوماتٍ من جيشنا العظيم تفيد بأنّ الإيرانيين أسقطوا ليلة أمس إحدى طائراتنا المروحية المتطورة من طراز أباتشي أثناء قيامها بدورية فوق مضيق هرمز. كان على متنها طياران، وكلاهما بخير ولم يُصب بأذى. ‏مع ذلك، يتعين على الولايات المتحدة، بالضرورة،…</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/naya_foriraq/77940" target="_blank">📅 20:25 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77939">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">⭐️
نيويورك تايمز:
كانت إحدى العقبات الرئيسية في التوصل إلى اتفاق مع إيران هي مطالب ترامب المتغيرة وإحباطه من عملية التفاوض.
وفقًا للوسطاء، شعر ترامب بالإحباط بسبب عدم قدرته على التحدث مباشرة مع المرشد الأعلى الإيراني، مجتبى خامنئي، وبسبب بطء وتيرة المفاوضات من جانب طهران. ويقولون إنه قام مرارًا وتكرارًا بتغيير الشروط التي ناقشها فريقه بالفعل مع المسؤولين الإيرانيين.
في الجولة الأولى من المحادثات بعد وقف إطلاق النار في أبريل، أفادت التقارير أن مبعوثي ترامب - ستيف ويتكوف وجي دي فانس - اقترحوا اتفاقًا تعلق إيران بموجبه تخصيب اليورانيوم لمدة 10 سنوات.
يقول المسؤولون الإيرانيون إنهم قبلوا هذا الإطار، لكن ترامب طالب لاحقًا بتعليق لمدة 20 عامًا، مما ساعد على إخراج المحادثات عن مسارها.
في الآونة الأخيرة، وبينما كان المفاوضون ينتظرون رد خامنئي على مشروع الاتفاق، أفادت التقارير أن ترامب أضاف شروطًا جديدة متعلقة بالبرنامج النووي الإيراني والوصول إلى الأصول المجمدة، مما زاد من انعدام الثقة الإيرانية في المفاوضات.</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/naya_foriraq/77939" target="_blank">📅 20:22 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77938">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E6QINPBE5dAnZMTXV6ph3aZNCx9YMFaAvotwYm0PwBlB3LUFP95AkPY5akDUTDH2Rbr9JxSlPy-oEEbPka9b3lIa2utfN0_imfOrq0NN98xlYhMcii5scfifqtRKuIF0loG_JI7R_wwt5ndWxuYOkN3b6JNuWwFEDmhjB0e82likmqjBUEgL811mxh8bCSCS1djf9TjUfHSx8U_txsW2k5crkOVqsRdOvm0aymaxtFnw_rJomq7S1Ecy8YjQb8PXLzntQR__hnbqTAD4xWfZ-vk6QAfa1W7phJwtSA1-RMDReeSgKTJu6Z6797quls3CLEPd8UNYJ6kyR7KKPrkDjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامب:
تلقيتُ للتوّ معلوماتٍ من جيشنا العظيم تفيد بأنّ الإيرانيين أسقطوا ليلة أمس إحدى طائراتنا المروحية المتطورة من طراز أباتشي أثناء قيامها بدورية فوق مضيق هرمز. كان على متنها طياران، وكلاهما بخير ولم يُصب بأذى. ‏مع ذلك، يتعين على الولايات المتحدة، بالضرورة، الرد على هذا الهجوم. شكرًا لاهتمامكم بهذا الأمر!</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/naya_foriraq/77938" target="_blank">📅 20:10 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77937">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pc7W6FPatMFfY5bltFB1LXvxDzZYu11h6WKUzB6rsyoYMtBC-bkaX_Rjqz66GHuj3Kb3DfyXmzS7QhOlhKccmqb1sKDklJBZZJ0Hi-YVRpjXwIcHW3CXCV5unU1xCcHuulkvPkvhDS64tgynqV5akOxx0TBS9FYtobMXRudqty_BsXFYLxj4hwcwRvx6iXZI8emL-TVTa3chCu8ZsuGM-5PjfkSp_BMe3_b8AbuO6MqvyzvIuSRelLH7bxcvk3sUYMYuOCobJfVcUbIjQjWwYMzF6ZB37gugjGDOnUG9f17_aD6m7CVU4GUOaMhdlwaLhqmV5woSMx6vnU9EesT09Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
المتحدث بإسم الخارجية الإيرانية:
تتضح الأمور بسرعة ملحوظة.
‏لقد نفذوا عملية "علم زائف" من خلال نشر طائرة بدون طيار مقلدة من طراز "لوكاس" لضرب مطار الكويت - مما خلق ذريعة مثالية لتسويق أنظمة الدفاع الجوي المضادة للطائرات بدون طيار التي طورتها شركة "باوروس" تحت ستار الحماية من الهجمات الإيرانية.
‏مربح بالفعل!</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/naya_foriraq/77937" target="_blank">📅 20:10 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77936">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/czNCc9Q4sPqEhA1n4O4ssgcbEUXg7SCvxJu4UIojyAwtdboc4u8ZrXYZLOFRq-rtCHphvWKCYWGCvk0Vs5bAw7fYohsjm8mXmGaPfJ_eXMfFL5ky-fAueTNdF_1AV5LF8JzPCVQ3QNOCBqI_ER5tdvaME2z5YDo9fdfjenfVgCjZ_VDfVSh5vFqf6CHHv0jnedKikIyZn5q34KeK0Ml4KK4IxUSfnkeySAFj3lb1WNAWE9QbXYEUDgeQh-nATHKN8a15CczOzIdkITI4cFJlmMk6nC4hLunRp_1Q4WoTsj340T4odsD66a1mEK5oZ67ECMYOhUjmNE1WR1Y0YV-rKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
رئيس البرلمان الإيراني محمدباقر قاليباف:
‏نُفضّل لغة الدبلوماسية، لكننا نتحدث لغات أخرى بطلاقة أكبر. إذا أخلفتم بتعهداتكم، فسنتحول إلى اللغة التي نُجيدها.
‏أنت تركب الحصان الذي سرجته!</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/naya_foriraq/77936" target="_blank">📅 20:04 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77935">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de89130b37.mp4?token=cVYXB49otI8bjbrRQmWPhVXbSzy5LLnN2b2BCsj4RvyiVZoxOoSyN5hlHX64rBSjOw_7cawKcyOk0MVQhIuK1I54baL0-njkJ39BXVoKhjOxsLtA2fj1bT-9rkpGW1BDSGhY7Q09btnZRxdxyFzBu8d9qOHbakjH0KzSG2FPFEtvv0IES3qU_nkoiE2yVxGTRoxgA3Gc1wQ2T9GElGgIIOd60UZLA-KaN-LJ1kCxYIYyv0EVxmuEtetvpjsLH-AquJleEyfBrsjIc5-_SZo5zGRPyqqPMqljVnB5lFIQDbMEeKdxAYpV05-R1kVsNawavRB5-AofHk5wstuQpUhMnW6dEKo7mjoMLgcYu6EzafFm1xr4sdj5SIiFO-yEvLHMrwpZ2fvDdXtHWNilzunyNYd5o0MxpPjZOfSm8qxGKtC-lEei_kCQNVx_VJiRN3GZsGRKmipb2swXgoPUkdWSQbq_RHnTqB2ZqxgYhMpeAfhk2llYg1cU-15lklloz71PcBNfgaDyiLkbSJMsY7SPCdmMNvH5YhrJ_EXpVmpDxT71j2cFy1QtdJEVg0OwZEBfoNFdQ2qnrCAAW2A3UmEWtrcrLJVCFfBVl4_nenX_BThUAHbAMHz5SR0U0ET3N6-GCsnHeLpWzlzLF1jkQ2hxSeT3j6AT51pgm9AX0jJW6W4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de89130b37.mp4?token=cVYXB49otI8bjbrRQmWPhVXbSzy5LLnN2b2BCsj4RvyiVZoxOoSyN5hlHX64rBSjOw_7cawKcyOk0MVQhIuK1I54baL0-njkJ39BXVoKhjOxsLtA2fj1bT-9rkpGW1BDSGhY7Q09btnZRxdxyFzBu8d9qOHbakjH0KzSG2FPFEtvv0IES3qU_nkoiE2yVxGTRoxgA3Gc1wQ2T9GElGgIIOd60UZLA-KaN-LJ1kCxYIYyv0EVxmuEtetvpjsLH-AquJleEyfBrsjIc5-_SZo5zGRPyqqPMqljVnB5lFIQDbMEeKdxAYpV05-R1kVsNawavRB5-AofHk5wstuQpUhMnW6dEKo7mjoMLgcYu6EzafFm1xr4sdj5SIiFO-yEvLHMrwpZ2fvDdXtHWNilzunyNYd5o0MxpPjZOfSm8qxGKtC-lEei_kCQNVx_VJiRN3GZsGRKmipb2swXgoPUkdWSQbq_RHnTqB2ZqxgYhMpeAfhk2llYg1cU-15lklloz71PcBNfgaDyiLkbSJMsY7SPCdmMNvH5YhrJ_EXpVmpDxT71j2cFy1QtdJEVg0OwZEBfoNFdQ2qnrCAAW2A3UmEWtrcrLJVCFfBVl4_nenX_BThUAHbAMHz5SR0U0ET3N6-GCsnHeLpWzlzLF1jkQ2hxSeT3j6AT51pgm9AX0jJW6W4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
🏴‍☠️
مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ
04-06-2026
دبّابة ميركافا تابعة لجيش العدو الإسرائيلي في محيط قلعة الشقيف التاريخيّة جنوبيّ لبنان بمحلّقة أبابيل الانقضاضيّة.</div>
<div class="tg-footer">👁️ 9.88K · <a href="https://t.me/naya_foriraq/77935" target="_blank">📅 20:01 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77934">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ae1a9c1cd.mp4?token=q9P9ws2MmWsa9P6V6LTJHNC2zpf8iDve9VCRZQSHD1MUnlw9cV3pN0i08GzSjhC0L7_5RyjdZArYqeapfxbdPmjFQMJyxf5LfSI2fZXIyukR0ZqtVybbWafWIa1X849_6fVvDQl78w6qrCUlg_7_KSwJxidUse-GxOSp6YFr3Av1bmUkSXPkmUQwhnxcw85lTvynZ1e0AKt8PC-HCVY0HP3eHGqI-6YAuzb0HUY0FrJDTV2zfQ7f9SEF8vI37IPE5Ufdb9e606AdGcVO3HCyYhObl-rOiqi-dNRoX9mmsg-SAYsSrKHG0QyTOX3pZiTC0ciobI1ARDZ5-a6-X2F-1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ae1a9c1cd.mp4?token=q9P9ws2MmWsa9P6V6LTJHNC2zpf8iDve9VCRZQSHD1MUnlw9cV3pN0i08GzSjhC0L7_5RyjdZArYqeapfxbdPmjFQMJyxf5LfSI2fZXIyukR0ZqtVybbWafWIa1X849_6fVvDQl78w6qrCUlg_7_KSwJxidUse-GxOSp6YFr3Av1bmUkSXPkmUQwhnxcw85lTvynZ1e0AKt8PC-HCVY0HP3eHGqI-6YAuzb0HUY0FrJDTV2zfQ7f9SEF8vI37IPE5Ufdb9e606AdGcVO3HCyYhObl-rOiqi-dNRoX9mmsg-SAYsSrKHG0QyTOX3pZiTC0ciobI1ARDZ5-a6-X2F-1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⭐️
مرور رتل عسكري كبير في قضاء بيجي بمحافظة صلاح الدين العراقية.</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/naya_foriraq/77934" target="_blank">📅 19:54 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77933">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🇺🇸
وزارة الطاقة الأمريكية:
لا نتوقع ارتفاع الحركة عبر مضيق هرمز لمستويات ما قبل الحرب قبل أوائل 2027.
نتوقع أن يظل جزء من إنتاج النفط بالشرق الأوسط معطلا حتى نهاية 2027.
الاضطرابات بمضيق هرمز أدت لخفض الإنتاج بأكثر من 11 مليون برميل يوميا في مايو.</div>
<div class="tg-footer">👁️ 9.7K · <a href="https://t.me/naya_foriraq/77933" target="_blank">📅 19:48 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77932">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">#عاجـــــــــــــل
🇮🇶
قوة من الحشد الشعبي تفكك عبوة ناسفة كانت موضوعة على طريق حديثة – بيجي في محافظة الأنبار غربي العراق.</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/naya_foriraq/77932" target="_blank">📅 19:43 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77931">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pRb9wx5wOwyDymiawLN4A7m_9DA04RbGKWl9t0Ds8Kxbg3FIagf0izw-wcNYWAvxp-iySQzwDLgBqz4JoNJ5qPvtCTs4BmF7g7Qfqpng55dH5jTZN_IL0K1YyqksSotEMi8XsHzgH0VsYUdv_U9nLi16eo64Xu33lS-dOeZIad0GK3AwKvzi9uyGONch096jWi-Np5wdU2tVvhn9bjBah88Q0avINLMaXYxn3ynS5m-FpnOmCr8qUKJeCI_O-9mkuHRrTZPsUV7_71PJWu-oiZS6oz9SDTvUvRkRBx5jbO1sTUycdbBwgZ5kui1ec7QzjCqSN6D3cfNoFCX3cQx3cQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭐️
غارات صهيونية على مرتفعات الريحان بجنوب لبنان.</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/naya_foriraq/77931" target="_blank">📅 19:38 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77930">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🇮🇷
الإنفجارات التي سمع دويها في مدينة أصفهان الإيرانية ناتجة عن تفجير ذخائر غير منفخرة ولايوجد حدث أمني.</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/naya_foriraq/77930" target="_blank">📅 18:54 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77929">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">⭐️
إندلاع حريق بوزارة الصحة العراقية في العاصمة بغداد.</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/naya_foriraq/77929" target="_blank">📅 18:44 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77928">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">#عاجـــــــــــــل
🇮🇶
محافظة صلاح الدين توجه بتعطيل الدوام الرسمي يوم الخميس 11 حزيران 2026 استعداداً لإحياء ذكرى جريمة سبايكر.</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/naya_foriraq/77928" target="_blank">📅 18:35 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77927">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b0AkWfO_Wgjz97fwNo9USwPJAOKTsFAN1K_WRXtx7F-zAmaDqym_xm_5VH0ib92-TZ3MPhiNDf-GmKWHtqdVj3aoXDsg9WCt1c0rwPQxB0Lh_hfuse4t6K1E9QVeG820l9HSE4snTywQu9nMmATujyohHveT9TnJQsq-2JAPWFYjZbMNfxvgWKQDLZYQGOye4sLH8znqHgqY2LsZqWlpWanDTjniHy2eQILwIz5bOzS7nfOtmY2t9eXG8GcM5ZSyzgUL0bCr9Bkoz3e3u9EamR-fU3GIyIP7CyGM4i7e9N_d1mZVqyl3iKlgja2coLqgX9qxN4um0dIbCGi021bsBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حزب الله يستهدف قوة الإخلاء بصليات صاروخية</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/naya_foriraq/77927" target="_blank">📅 18:16 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77926">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">مجلس محافظة النجف الاشرف يصوت على توصيات لفتح منفذ بري مع السعودية من بينها احالة المنفذ الى الاستثمار!</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/naya_foriraq/77926" target="_blank">📅 17:57 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77925">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🏴‍☠️
‏
رئيس الأركان الإسرائيلي
: الضربة التي نفذناها في إيران كانت تمهيداً لضربة أشد وأوسع بكثير</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/naya_foriraq/77925" target="_blank">📅 17:47 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77924">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🏴‍☠️
رئيس مستوطنة مرجليوت إيتان ديفيدي:
كان يجب أن تحترق الضاحية الجنوبية في بيروت، إذا لم يتم الرد بشدة على التسلل الارهابي إلى أراضي إسرائيل، فمن المحتمل أننا فعلاً مواطنون من الدرجة الثانية</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/naya_foriraq/77924" target="_blank">📅 17:45 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77923">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">اعلام العدو: حدث أمني في جنوب لبنان.. إصابة قوة عسكرية إسرائيلية بنيران حزب الله جنوب لبنان</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/naya_foriraq/77923" target="_blank">📅 17:43 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77922">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">اعلام العدو:
حدث أمني في جنوب لبنان.. إصابة قوة عسكرية إسرائيلية بنيران حزب الله جنوب لبنان</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/naya_foriraq/77922" target="_blank">📅 17:33 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77921">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d11e7f87e0.mp4?token=GOB3glqwfvvgnPB6OO4xRNwqEcYttCowzq8jo51AMP1_xS_aaKti7Fd1NPypUMvx_lULGVznZFVaHn4MmE5HNBO66jT7PxMBCPAvDEiWA9Ep7DtPD-dwqHXCH9AnRd3LuJk5Lxzt5oH37aowkh5BUeoaKRj7mKsnW35ZOelqZm_nZH3uyeTWIcC3iVmCKX0HO9BEqsziU1yG3Mnzq6sOAXptzKk5VmU7Ghpg0kysMV84ZvnA1qmn4vnKEmbZqKcnnKYSVMQssJH8RbPEilE-OTcu9Cxk_FTmdaBV6aoc1yzAFvz6ZGc19C3dym0gMHJtyb0xqgR_He2Lc_Ibjm9M5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d11e7f87e0.mp4?token=GOB3glqwfvvgnPB6OO4xRNwqEcYttCowzq8jo51AMP1_xS_aaKti7Fd1NPypUMvx_lULGVznZFVaHn4MmE5HNBO66jT7PxMBCPAvDEiWA9Ep7DtPD-dwqHXCH9AnRd3LuJk5Lxzt5oH37aowkh5BUeoaKRj7mKsnW35ZOelqZm_nZH3uyeTWIcC3iVmCKX0HO9BEqsziU1yG3Mnzq6sOAXptzKk5VmU7Ghpg0kysMV84ZvnA1qmn4vnKEmbZqKcnnKYSVMQssJH8RbPEilE-OTcu9Cxk_FTmdaBV6aoc1yzAFvz6ZGc19C3dym0gMHJtyb0xqgR_He2Lc_Ibjm9M5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حادث سير جديد على طريق (الحمزة - ديوانية) في محافظة الديوانية جنوبي العراق يسفر عن وفاة 4 اشخاص كحصيلة اولية.</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/naya_foriraq/77921" target="_blank">📅 17:18 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77920">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🏴‍☠️
جيش العدو:
إصابة 48 ضابطا وجنديا في معارك جنوبي لبنان خلال الأيام الـ5 الماضية.</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/naya_foriraq/77920" target="_blank">📅 17:15 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77919">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🏴‍☠️
اعلام العدو:
بعد تحقيق أولي - تفاصيل إضافية عن حادثة تسلل المهاجم إلى أراضي
إسرائيل
في منطقة سلسلة جبال راميم
1. خلال نشاط لقوات جيش الدفاع داخل جنوب لبنان - رصدت القوات إطلاق نار تجاههم. تم إطلاق النار على القوات التي كانت تعمل داخل لبنان، وتبادل إطلاق النار جرى مباشرة على سياج الحدود.
2. بعد أن قضت القوات على المهاجم وفحصت المنطقة، تم العثور على جثة المهاجم في الجيب الإسرائيلي خلف سياج الحدود. أي: رسميًا تسلل المهاجم إلى داخل أراضي إسرائيل - ولكن حسب المعلومات المتوفرة، لم يخترق سياج النظام ولم يدخل إلى المنطقة المدنية. الجيب خلف سياج الحدود هو بالطبع منطقة عسكرية.
3. كان المهاجم الذي عُثر على جثته يرتدي زيًا عسكريًا لحزب الله، وتم العثور على سلاح وسكين بحوزته.
4. في هذه المرحلة لم يتم العثور على أي أدلة إضافية. الفحوصات مستمرة - باستخدام طائرات بدون طيار من الجو، وقوات خاصة وقوات مشاة في الميدان، ولكن حتى الآن لم يتم العثور على شيء</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/naya_foriraq/77919" target="_blank">📅 17:12 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77918">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">📰
أكسيوس عن مسؤولين أمريكيين:
نحقق لمعرفة إن كان إطلاق نار إيراني تسبب بسقوط مروحية أباتشي قرب مضيق هرمز الاثنين.</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/naya_foriraq/77918" target="_blank">📅 17:03 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77917">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🇱🇧
حزب الله:
مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ 07-06-2026 تجمّع آليات وجنود جيش العدو الإسرائيلي في بلدة رشاف جنوبيّ لبنان بصليةٍ صاروخيّة.</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/naya_foriraq/77917" target="_blank">📅 17:00 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77915">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CCRfIno8ELcg8Lk4aFNDw2YDKYcL-fk66N6F5FLsOmxHmmpxp7NicI2oGe9jFhTKuNYZ7mq1HKQ1LOt8jz7ahSD60izrs1mVYt1DtYcR7s4ltemOhKh32tmRWiWHO11zahldGwhDZKOXZp4i_mTX9p9lvgzTSf1Y_x3o4z3aG2593s1L3AOifSvlEBeqH3JScpJtPUtMlIXkgq1Hh4xx-hZqgHOGOI3kUPjhkzklbWt4iJTI4IO88pSwFzKwCdmuCAj4_SNxaqOs_qtcatY56VW-Xi29YIu0HP2k42tUvmR2uy18Ciy9DtKaCOi1YrKgT2qFbEpZfsx-abmXUzvhWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MNOYcDOweqITnY7s0QSTgKlhGLzY7M0cEmbPlEB9RDqCQmlh7-nbiCSUAjTYXZSIUk_JD156sDVMI4E5H8NZy0cftxmEzSJ7P8mqyBVfIPi1sK64xmLmQm7v_LEdi1POv8Rgfxr_xdFX0GPr5W5qr0bGpK_R4jDV7udAQzE7Owbbr9LKR0DJbkw3ief7yPAOPuhu9tEfG5ySjhGgPq4ukPJZNUVNyM_hbUUCFnIWwPElfkyq5Dpg2u67YzKEz2zh1cY9VXMfLYBxlu28J3f1Rk3bpu2-9tIHQJN4lvVA-KDpclFcLc0QwfnUSBi5go7O6ybBN-8Aq6re_lv928Sm7A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇮🇷
البنك المركزي الإيراني يطبع عملة جديدة بقيمة 100 ألف تومان عليها صورة الحرم الشريف للسيدة معصومة وعلى الجهة الخلفية نصب تذكاري لمدرسة ميناب.</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/naya_foriraq/77915" target="_blank">📅 16:50 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77914">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">رئيس وزراء الإسرائيلي السابق
إيهود أولمرت:
المستوطنون بالضفة الغربية ينفذون تطهير عرقي ضد الفلسطينيين في الضفة الغربية بدعم من المسؤولين الإسرائيليين.</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/naya_foriraq/77914" target="_blank">📅 16:43 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77913">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">الحكومة البريطانية تعلن عن عقوبات تستهدف شبكات أسهمت في تمويل أعمال عنف للمستوطنين بالضفة الغربية</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/naya_foriraq/77913" target="_blank">📅 16:38 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77912">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🏴‍☠️
اعلام العدو:
الحكم بالسجن 11 سنة مع غرامة مالية بحق عدد من المستوطنين سرّبوا معلومات لإيران بما في ذلك مواقع القوات، تحركات الدبابات وسقوط الصواريخ.</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/naya_foriraq/77912" target="_blank">📅 16:37 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77911">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">اعلام العدو: التقديرات تشير إلى أن المسلح كان يختبئ في المنطقة منذ فترة طويلة، وهناك شبوهات قوية تدور حول وجود "خلية كاملة" تتحرك في المكان، ويُحتمل أنه خرج من نفق في المنطقة.</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/naya_foriraq/77911" target="_blank">📅 16:25 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77910">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🏴‍☠️
اعلام العدو: هذا حدث غير مسبوق منذ بداية الحرب، كانت المرة الأخيرة التي تسلل فيها مسلحون من لبنان إلى أراضي إسرائيل في يناير 2024 الى منطقة معزولة. اليوم حدث تسلل مسلحين فعليًا عبر السياج الأمني إلى داخل إسرائيل إلى منطقة مدنية بالقرب من المستوطنات.</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/naya_foriraq/77910" target="_blank">📅 16:13 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77909">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">إذاعة جيش العدو: هذا استثنائي بالتأكيد، خاصة في ظل حقيقة أن قوات الجيش الإسرائيلي تحتفظ بشريط أمني بعمق عدة كيلومترات داخل الأراضي اللبنانية مقابل سلسلة جبال راميم</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/naya_foriraq/77909" target="_blank">📅 16:11 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77908">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/281276ba1e.mp4?token=qUH-6H-wgO207WiQz3IrmWBuO-RsHGsQqU41weFSNfd3hpT1GIq-IO7CArb0sCLQ6ePuRDsZ3UffcDZPcG1tenaUWlvJfhqCci-36EoFaSMfrr_75OAlPL0Ic9TErfpVSSA4De05UirprZ68RdlevDQkSNvP242HuYyflRbk6oK4RZOr0IZMgvI9dSi0vmJQnVFA26MbShvEca7BSCgOWnLx7N1JQNfBxJgyJFEEZBE4rEQMSVB6_Bc-tYFj2wDsDArM6C21XtbllLD48Iupk3KNdYjQDVPcnn56I-EZjjKTSfS8fUyaGEiwhFbJ-54SYSlU6hGnYHVozT_D6NvqOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/281276ba1e.mp4?token=qUH-6H-wgO207WiQz3IrmWBuO-RsHGsQqU41weFSNfd3hpT1GIq-IO7CArb0sCLQ6ePuRDsZ3UffcDZPcG1tenaUWlvJfhqCci-36EoFaSMfrr_75OAlPL0Ic9TErfpVSSA4De05UirprZ68RdlevDQkSNvP242HuYyflRbk6oK4RZOr0IZMgvI9dSi0vmJQnVFA26MbShvEca7BSCgOWnLx7N1JQNfBxJgyJFEEZBE4rEQMSVB6_Bc-tYFj2wDsDArM6C21XtbllLD48Iupk3KNdYjQDVPcnn56I-EZjjKTSfS8fUyaGEiwhFbJ-54SYSlU6hGnYHVozT_D6NvqOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجار سيارة في مستوطنة حولون</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/naya_foriraq/77908" target="_blank">📅 16:10 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77906">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">اعلام العدو: تم القضاء على اثنين من مسلحي حزب الله المتسللين في منطقة مرجليوت وهناك مؤشرات على وجود مسلحين إضافيين.</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/naya_foriraq/77906" target="_blank">📅 16:00 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77905">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">اعلام العدو: مسلح تمكن من الدخول الى اسرائيل واطلق النار على القوات الاسرائيلية من الجانب الاخر من الحدود</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/naya_foriraq/77905" target="_blank">📅 15:58 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77904">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">وزيرة خارجية بريطانيا:
على حزب الله إنهاء هجماته وإلقاء سلاحه
.
صار تكرموا</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/naya_foriraq/77904" target="_blank">📅 15:58 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77903">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">منصات للمستوطنين تتحدث عن خشية لدى جيش الاحتلال من إمكانية وجود مجموعة أخرى من المقاومين نجحت بالتسلل من لبنان إلى داخل الأراضي المحتلة.</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/naya_foriraq/77903" target="_blank">📅 15:57 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77902">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">إعلام العدو : للتوضيح كان هناك محاولة تسلل من قبل مسلحي حزب الله إلى المستوطنات الليلة الماضية - واختاروا إخفاء ذلك عن الجمهور ولم ينشر اي تفاصيل.</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/naya_foriraq/77902" target="_blank">📅 15:56 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77901">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🏴‍☠️
جيش العدو في بيان: الحدث لا يزال مستمرا. تواصل قواتنا عمليات المسح، بالإضافة إلى طائرات سلاح الجو التي تم إرسالها إلى المنطقة. نحن على اتصال مستمر مع السلطات المحلية.</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/naya_foriraq/77901" target="_blank">📅 15:53 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77900">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">إعلام العدو : للتوضيح كان هناك محاولة تسلل من قبل مسلحي حزب الله إلى المستوطنات الليلة الماضية - واختاروا إخفاء ذلك عن الجمهور ولم ينشر اي تفاصيل.</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/naya_foriraq/77900" target="_blank">📅 15:52 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77899">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">إعلام العدو : للتوضيح كان هناك محاولة تسلل من قبل مسلحي حزب الله إلى المستوطنات الليلة الماضية - واختاروا إخفاء ذلك عن الجمهور ولم ينشر اي تفاصيل.</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/naya_foriraq/77899" target="_blank">📅 15:47 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77898">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/naya_foriraq/77898" target="_blank">📅 15:47 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77897">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">كريات شمونه مسكاف عام المطلة   مغلقة حتى إشعار آخر بأمر قوات الرضوان</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/naya_foriraq/77897" target="_blank">📅 15:42 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77896">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bc3a3d474b.mp4?token=T9rLE_S7ePBer3S72JRgukTl4vg5KjyvacAkx8WJnNHV77mEpWzplVE-3RImQr998GwAzdL12s4ABiNI-OxRv2GFhehjoYCvpd0qxgLT3MfnBFXfv9i_Vt9GGaJOgrFnL65UTrPniHNygfjtoHWY5dhHEt0d1_BuWoXK0uB9B8-hr_02U-RH83dSp8xAM3iTAsY63mN3UC_Yao75DhiTvEv_dbK5g6LA4ZA5ETRVxHU42c5P_BfKyjY9BMmbslGbQw42hf80MgITR3pyV10E2JcVBzDXai_EoJF3_P2ScEmx4SOQyLTUbs5lOKe7-c1seGc8hkUh2FNrclq-dYum8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bc3a3d474b.mp4?token=T9rLE_S7ePBer3S72JRgukTl4vg5KjyvacAkx8WJnNHV77mEpWzplVE-3RImQr998GwAzdL12s4ABiNI-OxRv2GFhehjoYCvpd0qxgLT3MfnBFXfv9i_Vt9GGaJOgrFnL65UTrPniHNygfjtoHWY5dhHEt0d1_BuWoXK0uB9B8-hr_02U-RH83dSp8xAM3iTAsY63mN3UC_Yao75DhiTvEv_dbK5g6LA4ZA5ETRVxHU42c5P_BfKyjY9BMmbslGbQw42hf80MgITR3pyV10E2JcVBzDXai_EoJF3_P2ScEmx4SOQyLTUbs5lOKe7-c1seGc8hkUh2FNrclq-dYum8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇾
عدد من انصار الجولاني يقطعون الطريق على صهاريج النفط العراقية في بلدة الهول</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/naya_foriraq/77896" target="_blank">📅 15:41 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77895">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">كريات شمونه مسكاف عام المطلة
مغلقة حتى إشعار آخر بأمر قوات الرضوان</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/naya_foriraq/77895" target="_blank">📅 15:40 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77894">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/naya_foriraq/77894" target="_blank">📅 15:40 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77893">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">إعلام العدو : نبحث عن مسلح ثاني داخل الجليل</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/naya_foriraq/77893" target="_blank">📅 15:38 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77892">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">من طيبة إلى العديسة حتى مسكاف عام
المقاومة تشتبك من مسافة صفر …</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/naya_foriraq/77892" target="_blank">📅 15:37 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77891">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">شبح عماد مغنية في مسكاف عام</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/naya_foriraq/77891" target="_blank">📅 15:37 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77890">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">المقاومين تسللوا باتجاه مسكاف عام ..</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/naya_foriraq/77890" target="_blank">📅 15:36 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77889">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">اعلام العدو: عدد المتسللين اكثر من واحد</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/naya_foriraq/77889" target="_blank">📅 15:36 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77888">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">من العديسة إلى مسكاف عام
كمين العديسة اصبح داخل الجليل</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/naya_foriraq/77888" target="_blank">📅 15:36 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77887">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">هجوم بري من قوات الرضوان على مستوطنات الشمال</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/naya_foriraq/77887" target="_blank">📅 15:35 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77886">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">قوة الرضوان تخترق الجليل</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/naya_foriraq/77886" target="_blank">📅 15:35 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77885">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/naya_foriraq/77885" target="_blank">📅 15:35 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77884">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">الكيان الصهيوني يصدر عدد من التعليمات بعد حادثة تسلل في منطقة شمال سلسلة جبال رميم:  - على سكان مستوطنات مسكاف عام ومرغليوت ومنارة الالتزام بتعليمات مسؤول الأمن المحلي، والبقاء داخل المنازل وعدم التجول داخل البلدة. تعمل وحدات الدفاع والجيش الإسرائيلي في المنطقة.…</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/naya_foriraq/77884" target="_blank">📅 15:35 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77883">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">اعلام العدو: المسلح كان يقاتل ببندقية وسكين.</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/naya_foriraq/77883" target="_blank">📅 15:33 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77882">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">‏
الإليزيه:
ماكرون يستقبل توم برّاك ويبحث معه أوضاع سوريا والعراق ولبنان</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/naya_foriraq/77882" target="_blank">📅 15:32 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77881">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u-zZAPIchVs-ueXljhv8uZPjiC4M0HPTkSCdnN79RGp6k328AO1e6zkFskT7wUfWZirqO2rcYkMyFKcaXitDvlyIaBRorF2vu86MFHENzaKUB-Bk6ZQyB9PnkXWIMTMgtCbBOqlNeT07ZYuHGp_XMVdsmFuCUMB8xf9YeXoH0Qv-9tXZX32QGz4hvFrkeLX0nzhL7spL3F_PHksqPul3UHpj4UCHnVR1L3oIZSk7qg5z16WDLwcMzCgUouWtSyP7hp0ll8_JaI59Vvqtmry0ACFFI9F7wRf_Qm4k1UbcSRiU5f4jH2IsCvEDAHun9hAwyEB1kvO-J0Cv5FSZkA6aoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اعلام العدو: تبادل لإطلاق النار بعد تسلل مسلح عند الحدود مع لبنان قرب سلسلة جبال راميم بالجليل الأعلى.</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/naya_foriraq/77881" target="_blank">📅 15:30 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77880">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">اعلام العدو:
تبادل لإطلاق النار بعد تسلل مسلح عند الحدود مع لبنان قرب سلسلة جبال راميم بالجليل الأعلى.</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/naya_foriraq/77880" target="_blank">📅 15:25 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77879">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🏴‍☠️
🇺🇸
اعلام العدو:
وزير الخارجية الأميركي ماركو روبيو لعب دورا محوريا بإقناع ترمب بدعم الضربة الإسرائيلية لإيران مبررا ذذلك بأن عدم الرد سيمنح إيران ميزة ويشجعها على المزيد.</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/naya_foriraq/77879" target="_blank">📅 15:23 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77878">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🇮🇶
ماذا حدث البارحة ؟!
الطيار وكيل جهاز الامن الوطني العراقي هو احد عناصر حزب الدعوة تنظيم الداخل .. دخل الجهاز مع عبد الكريم العنزي وكان من مؤسسي الجهاز بعد ٢٠٠٣ ..
بعد فضيحة سوداني وتر غيت بوقتها التي انتشرت في الإعلام ؛ تم اعتقال شخص بالدائرة القانونية و شخص آخر بجهاز الامن بالجهاز اعترفوا انهم يتلقون أوامر للتجسس من قبل الطيار ؛ اغلقت القضية انذاك بسبب تدخل إقليمي وكون ان السلطة التنفيذية هي المتهمة استعصيت تطبيق مذكرات إلقاء القبض ؛ ابرز الشخصيات التي تم التجسس عليها " القاضي الأستاذ فائق زيدان ، الوزير مصطفى سند المرياني ، الشيخ قيس الخزعلي وعدد من أفراد أسرته ُ ، عبد اللطيف رشيد واخرون "
البارحة طبق جهاز امني مذكرة استقدام وتحري قد حركها نائب سابق على الطيار الذي استقدم وبعد التحقيق تم إصدار امر اللقاء القبض ..</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/naya_foriraq/77878" target="_blank">📅 15:21 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77877">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🇫🇷
‏فرنسا تمنع سموتريتش و4 من قادة الاستيطان و21 مستوطنا من دخول أراضيها.</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/naya_foriraq/77877" target="_blank">📅 15:18 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77876">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🏴‍☠️
إذاعة جيش العدو تكشف عن تفاصيل جديدة حول طلعة الهجوم الجوي التي كان مخططًا لها أن تنطلق أمس نحو إيران وتم إيقافها بقرار من المستوى السياسي:
- كان الحديث يدور عن طلعة هجومية كبيرة، جرى الاستعداد لها في المؤسسة الأمنية منذ اللحظة التي بدأت فيها إيران بإطلاق النار على إسرائيل أول أمس عند الساعة 22:00، واستمرت التحضيرات طوال الليل وحتى ساعات الصباح.
- كان من المقرر أن تنطلق الطلعة الجوية إلى إيران أمس في ساعات بعد الظهر.
- من بين الأهداف المخطط مهاجمتها: البنى التحتية الوطنية الإيرانية، بهدف تعميق الضرر الاقتصادي الذي يلحق بالنظام الإيراني (وذلك بعد الهجوم المحدود الذي نُفذ على المنشأة البتروكيميائية). كما كانت هناك أهداف أخرى لا يمكن الكشف عنها.
- التغريدة التي نشرها ترامب والتي دعا فيها إلى وقف الهجمات عند الساعة 12:30 بتوقيت إسرائيل، جاءت قبل وقت قصير — أي قبل ساعات قليلة فقط — من موعد إقلاع الطائرات، ولذلك بقيت الطائرات على الأرض وهي مسلحة ولم تنطلق نحو إيران.</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/naya_foriraq/77876" target="_blank">📅 15:14 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77875">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tXEFfaJ2w7tGtTrl4IVnvzc1bzW_ORTBkTsf79r5LUrlzL7jevACY5tlfcfTRu47icztKPxcKeX8Y3DTuefNikdEmA92QQp7zZ_S5E-Nhnjf01SK-DTJzvPH_SWg6VXpReIeG8X1jjbJ-CRy7CaF2b2HMqFmb7lgwkWQjuVsNqhqKyfVEq0aUHFhEiOfwkW4lQBY-kKLaBVomaQwWqjHLpQhOs7JYCv8fTe2ffD_B0hN3xFIBKtxvSebUYNjHlhYqmx1nQgze7r7T4Rfy17MwDvXHoHJkR9zmH4p-VuzcOoldgQ7U4RQF2u4gCVTd_0R8BPnWm2OHR9AbTK8Qi1t_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">غارات صهيونية على جنوب لبنان</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/naya_foriraq/77875" target="_blank">📅 15:09 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77874">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🏴‍☠️
اعلام العدو:
المجلس الوزاري المصغر قرر أن أي صاروخ يطلق من لبنان سيقابل بهجوم على بيروت دون موافقة من القيادة السياسية.</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/naya_foriraq/77874" target="_blank">📅 14:59 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77873">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BvzidcfXPivJ2VDTvyLP0GDT4ufUmUvD7qNir3Ouee1i7petu4QK3KVMaWFTUImrsFY2s8GrOrrPUoLHrwqCU3CjbPeHOTMZsySq0S3Szkf01nwG2VxJFBq5pi9i_j5Vw6nRB0kc2r6jeWm6WCSQ48v9vwgzdTlgulTsZ_OQ-TSjAoE2Rt0o__-4ZC-KU396em9X1QXwrYgdLlTVlvnIgmaHrhLFzrj6l6XU57n2xYH7U8G4bboRYKVqzUoU1GgB0u6fH9Zq-QqfbGN6QYzorDse8kVj49IQY0Se-DZBHLM4OoYLaF3e7LRfI_mG7fQMRbG_Zq3F8LPOiGXaB-T4CA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
🌟
وكالة مهر:
تعيين (ياسر الحجاج) سفيراً جديداً لجمهورية العراق في طهران.</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/naya_foriraq/77873" target="_blank">📅 14:47 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77872">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db1cd39643.mp4?token=nMFdy8nFl0zC0M5IGCCWm4TzTNj-15m3Q5ROZhqIXdroF5foGawIbI6agYGyLZ7DptG6Kumt5_L6NkyHL36CDDM0A6NpwBns4QnDRIo6YEbfblFIQESu_YaQ_x7yuQXgP7ThqO1BPP68ph3RSRlQUu8gaNBxixBlsJYyAm4pWtrWDAUmJP_eNLHazN6WjHOMryYykygZK4VH7IR_8BANOg21u9gDff9_bb9J4m-rxbKrfUePdT7jVPmCgMt1Hn1yA6gTz8ihDu34ibFFyxnmdVRDeem-k7mVITJqC24cIFTXJtZz-0JmNsW1hP2VfDo1bMryk7VYficSdr1GMgyTvw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db1cd39643.mp4?token=nMFdy8nFl0zC0M5IGCCWm4TzTNj-15m3Q5ROZhqIXdroF5foGawIbI6agYGyLZ7DptG6Kumt5_L6NkyHL36CDDM0A6NpwBns4QnDRIo6YEbfblFIQESu_YaQ_x7yuQXgP7ThqO1BPP68ph3RSRlQUu8gaNBxixBlsJYyAm4pWtrWDAUmJP_eNLHazN6WjHOMryYykygZK4VH7IR_8BANOg21u9gDff9_bb9J4m-rxbKrfUePdT7jVPmCgMt1Hn1yA6gTz8ihDu34ibFFyxnmdVRDeem-k7mVITJqC24cIFTXJtZz-0JmNsW1hP2VfDo1bMryk7VYficSdr1GMgyTvw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عدة حوادث سير لصهاريج النفط العراقية في الاراضي السورية بسبب سوء البنى التحتية في سوريا مما خلف خسائر كبيرة</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/naya_foriraq/77872" target="_blank">📅 14:41 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77871">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GlDeqwPzMSv9RRITTbp6Dq3yV6Azc9zZ7FzvFhjIJYgR4Dn3QMbdahHsK-pluQSshqsopCshXXD-YvJgXMlbOBdpX14jeCR9o27xeDSYxfXh7CWLLQIYBTuWLMnHff_-OKeSiGcUCa3gVGhKgIqhQemBHp8-npCZM3KABIvFTf1zcFdiHCsEU_5Qi8UI0W-fUNfjMq4Fuy3BsulwdhOORJdEGHtJ3v-xXWAANs7pMbLu5rVciiix6KLWvC5igkEksmX402uiVUwRQTgO6L7DwXay0gEWuHjtfhZZe_GWvChV4Cs_za4UfGT7JowDcZ2N7WbBMLf89yJspv5hwzBhGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اعلام العدو: بموافقة الرقابة، تُظهر صور الأقمار الصناعية إصابة دقيقة لحظيرة داخل قاعدة رامات ديفد الجوية بصاروخ إيراني قبل يومين.</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/naya_foriraq/77871" target="_blank">📅 14:25 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77870">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🌟
وسائل اعلام لبنانية:
قائد الجيش الباكستاني يرغب في الاطلاع من نظيره اللبناني على حقيقة الأوضاع في جنوب لبنان، المشير منير يريد الاطلاع من نظيره اللبناني على قدرات الجيش اللبناني على الانتشار في المناطق الجنوبية. زيارة قائد الجيش اللبناني إلى باكستان لا يمكن أن تتم من دون موافقة وضوء أخضر من الرئيسين عون وسلام</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/naya_foriraq/77870" target="_blank">📅 14:11 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77869">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🌟
قادمة من اقليم كردستان..
هيأة المنافذ الحدودية تحجز 13 شاحنة في محافظة كركوك تحمل بضائع مستوردة تم تزوير الباركود الخاص بها الى محلي.</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/naya_foriraq/77869" target="_blank">📅 13:55 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77868">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🇷🇺
‏
الكرملين:
الوساطة الأميركية بشأن أوكرانيا متوقفة حاليا.</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/naya_foriraq/77868" target="_blank">📅 13:49 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77867">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🇮🇷
وكالة إرنا:
بعثة إيران أكدت أن الوكالة الذرية هي التي أوقفت التفتيش بالمنشآت النووية عقب العدوان على إيران، إيران تعد مشروع القرار الأمريكي الأوروبي ضدها في مجلس محافظي الوكالة الذرية مسيسا واستفزازيا.</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/naya_foriraq/77867" target="_blank">📅 13:40 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77866">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bawIlm0zBYWaD0wt6ibWQyW9t4N3wrXDebRTpREci4Qp4AZscKE318tQuwIoJ6is39D22y8RHtkTUdWZc1YdkijazsLOjkm7r9xaspZfTSU8PR1ZmhwEEgN9uAvt22EhjwS58snYht-cHsLDsv6g5eM4yXduhPKS1by5EuZrJ7ruwD_aK63dcu0cspOVjYlmiyFal03C09KWkY_LJFAZgG7q4yGrN1AA_fWIQlbZHeky1Y0m2BeKkezXl5NN8ML099UbLH4txFYKTqQRKYOFaGoJSNVoVGOpSqcvlS_0N8N2bdJdRao-UACP7o7JYE1n-U0m4wQlrozlZEyND3rQRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🐦
الشيخ اكرم الكعبي يحيي الجمهورية الاسلامية وابطال اليمن على تأديب الكيان الصهيوني.</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/naya_foriraq/77866" target="_blank">📅 13:07 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77865">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">لجنة تحقيق رسمية للأمم المتحدة:
السلطات الإسرائيلية متورطة بشكل مباشر في هجمات المستوطنين التي أدت إلى قتل وإصابة وتهجير فلسطينيين في الضفة الغربية، في حين أن قوات الأمن الإسرائيلية توفر الحماية للمستوطنين. وأكد التقرير أن السلطات الإسرائيلية سمحت لهجمات المستوطنين من خلال دعم مالي وعسكري، في ظل أجواء من الحصانة من العقاب التي خلقتها أنظمة القضاء وإنفاذ القانون.</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/naya_foriraq/77865" target="_blank">📅 13:00 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77864">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🇱🇧
بيان صادر عن حزب الله حول الرد الصاروخي الإيراني على الكيان الصهيوني:
إنَّ الرد الصاروخي الإيراني على الكيان الصهيوني دفاعًا عن شعبنا اللبناني هو رسالة التزام أخلاقي وسياسي وميداني من الجمهورية الاسلامية اتجاه لبنان بعدما تمادى هذا العدو بغطاءٍ كامل من الإدارة الأميركية في ارتكاب جرائمه ضدَّ بلدنا، وعاود استهداف الضاحية الجنوبية، في إطار خروقه المستمرة  لاتفاق وقف النار بما يؤكد استخفافه بكلِّ الاتفاقات الدَّولية، ولذلك جاء الرد الايراني للتأكيد أنَّ مصلحة استقرار المنطقة ودولها هو بذل كلِّ جهد ممكن كي تُصان الاتفاقات وأن يلتزم بها العدو الصهيوني قبل غيره، وهذه هي الرسالة التي أرادت إيران أن تبعثها بوضوح وقوة إلى كل المعنيين بجهود دعم الاستقرار في منطقتنا. وقد تزامن مع الدعم المشكور من حركة أنصار الله في اليمن في إطار العمل المشترك لردع الكيان الصهيوني وإفهام الإدارة الأميركية أنَّ دعمها للعدوان الصهيوني على بلدنا سيطيح بكلِّ الاتفاقات التي تسعى إليها خصوصًا في ظلِّ إصرار الجمهورية الإسلامية على تضمين أي اتفاق معها وقفًا شاملًا لإطلاق النار في كل الجبهات وبالأخص في لبنان، كمقدِّمة لفرض انسحاب العدو من أرضنا اللبنانية وعودة النازحين وإعادة الاعمار وإطلاق الأسرى.
إنَّ هذا الدعم الإيراني لحقوقنا المشروعة، وتحمُّل تكلفته الماديَّة والسياسيَّة يؤكد مرَّة جديدة أنَّ ايران هي من تساند لبنان وليس العكس، وذلك انطلاقًا من مبادئها وقيمها الإنسانيَّة، ومن عمق العلاقة التاريخية بين الشعبين اللبناني والإيراني، فإيران كانت على الدوام تريد الخير لبلدنا، وأسهمت في دعم مقاومته  لتحرير أرضه وفي إعادة إعمار ما هدَّمه العدوان الصهيوني، وموقفها المشرِّف إلى جانب لبنان يستحق من سلطته الشكر وليس التنكُّر والإساءات المتعمدة  استجابة لإملاءات خارجية، فكلِّ الأصوات المدفوعة بتلك الإملاءات  لن تؤثر على صدقية هذا الموقف الإيراني الشجاع والوفاء النادر في زمن تغليب المصالح على المبادئ، فالاتهامات الباطلة التي صدرت عن بعض جهات السلطة ضدَّ الدَّور المشرِّف لإيران الساعي إلى وقف العدوان الصهيوني على لبنان، مرفوضة بالكامل لأنَّها تجافي الحقيقة وضدَّ مصلحة لبنان،  فالتهجم الظالم على إيران بما في ذلك البيان المشترك مع العدو والإدارة الأميركية ضدَّها هو خارج عن كلِّ قواعد العلاقات الديبلوماسية واصطفاف مرفوض ومدان، ولم يخدم سوى العدو الصهيوني.
إنَّنا ندعو السلطة اللبنانية إلى اغتنام الفرصة المتاحة وتصحيح علاقتها الرسمية مع الجمهورية الإسلامية بما يخدم مصالح الدولتين، والاستفادة من هذا الدعم الإيراني من أجل تحقيق أهدافنا الوطنية خصوصًا على ضوء تشكُّل المظلة الإقليمية الجديدة المنبثقة من مفاوضات إسلام آباد، وبذلك تتمكَّن الدولة في لبنان من خلال مفاوضات غير مباشرة مع العدو، ومستندة إلى تلك المظلّة وعوامل القوّة التي تشكلها المقاومة وصلابة الموقف الشعبي وثباته والتفاهمات الدَّاخليَّة من تحقيق مطالب شعبنا في تحرير أرضه وعودة النازحين وإعادة الإعمار وصون السيادة الوطنية.
إنَّنا في حزب الله وباسم شعبنا وعائلات شهدائه والصامدين والنازحين وباسم كلِّ حرٍّ وشريف في وطننا نقدِّر عاليًا هذا الوفاء من قبل ايران ونحيي شجاعة هذا الموقف النبيل للولي الفقيه ولرئيس الجمهورية والحكومة والبرلمان وللجيش والحرس الثوري ولأبناء الشعب الايراني على وقفتهم المشهودة إلى جانب حقوقنا المشروعة وقضيتنا الوطنية، وهي الحقوق التي سنواصل الدفاع عنها من خلال مقاومتنا البطولية حتَّى تحقيقها مهما غلت التضحيات ليبقى شعبنا على أرضه يعيش بعزَّة وكرامة وحريَّة.</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/naya_foriraq/77864" target="_blank">📅 12:35 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77863">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">إطلاق صاروخ أرض جو على طائرة حربية صهيونية جنوب لبنان
وإسقاط مسيرة فوق جبل الريحان الآن</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/naya_foriraq/77863" target="_blank">📅 12:06 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77862">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v8a2MXVivfeBhZmt-n8t4LYsD9IkC5GaKzdAnD9sc7-6FgrP-8P_bunA_Flzs8xJlkyLeESVl-fS7uhue5twE-WWIB41TQFt6aOQRu2W0zW8vAOm8m02wIV7TMt3BWkTqbwA-xEpJZsBtRSH1vcrC0cxqxoNe04jxbzEOgCAvKq_CUld8XvFuRE_dV8elfNst5_CF6zTpTwGJd2Q_kltS58YXVwZGgoa7RZu2GcHh6_zt2qjX-eAvglAKygXQus7sWq3uPVdbXhbAw5mMGDfxKnlQtN0ZtigR5TTJd-5FonSVcw4fnkkun6nkkn5LZHVkaVw-e0icZfPLc0ettvy7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استهداف صهيوني لسيارة على طريق المصيلح جنوبي لبنان</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/naya_foriraq/77862" target="_blank">📅 11:38 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77861">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9adf9e6a56.mp4?token=ZH6IuNOzu6xoGqn1e3HOlgCudoFOqyNSHe812lCUBpFIQFrvD9arShZofyIa17OtgPK2aC4fE8Hs35nRyQU7kBtD6rKfB_M53e0T0km2Hn95UFqE1VGS8LZVMcTuMgEV94KdRh9unZ7R7fWjYaR_KslN0S6H3uvPCYn7QGHwsxJlhWuu7rznLjRH075SYKs4RfDho3kwlwuNiMg2Xs7PWPGUYzw_8vjoNPFoQfX__bq3rgkIUzoTf6wGRF7_VUjQw2uWj0xREfWJzHOIE99RsL5YNO-WkDadK-CQns6Q2O1NjkaWutqjHKiBST30zrk67uVAnVL9FoEcBmrS_DOpaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9adf9e6a56.mp4?token=ZH6IuNOzu6xoGqn1e3HOlgCudoFOqyNSHe812lCUBpFIQFrvD9arShZofyIa17OtgPK2aC4fE8Hs35nRyQU7kBtD6rKfB_M53e0T0km2Hn95UFqE1VGS8LZVMcTuMgEV94KdRh9unZ7R7fWjYaR_KslN0S6H3uvPCYn7QGHwsxJlhWuu7rznLjRH075SYKs4RfDho3kwlwuNiMg2Xs7PWPGUYzw_8vjoNPFoQfX__bq3rgkIUzoTf6wGRF7_VUjQw2uWj0xREfWJzHOIE99RsL5YNO-WkDadK-CQns6Q2O1NjkaWutqjHKiBST30zrk67uVAnVL9FoEcBmrS_DOpaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
‏ترامب ظهر على الكاميرا أثناء عزف النشيد الاميركي، يتعرض لهتافات استهجان عالية في قاعة الغناء اثناء حضورة لنهائي مباريات احد الرياضات.</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/naya_foriraq/77861" target="_blank">📅 10:37 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77860">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/adbc31aabd.mp4?token=V3fRKX9YvetEdnNUfgc9mdSJzgp1coo2OIbvFV447dmzMAjgwr9aqOIz3C74H2O5TbdhLgEiJ_JPtxNiE3sQjCVjMG1KNWkOha7MygojtsKnIjwyxke8byFfJeGL3aDsszRg-iF7J2owDA-aF-uYuDvzMk-8mOP6o0o7xuR5dF2Ue7PuZWzbVqES_zt_oUOkYOqDU_kRtyvZrIfrl-dqzlB6XPcX7i3NilWDQoao68Qrgo2D5yozthEFH3fnS8jpoMF_ZPKVe9vEyk1A9HUWgRVSTtc73WovcFObAC2lWLRQ1gm6gmSQbaExoTSGbAqht5a7GHyXq5fNou1mss6tXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/adbc31aabd.mp4?token=V3fRKX9YvetEdnNUfgc9mdSJzgp1coo2OIbvFV447dmzMAjgwr9aqOIz3C74H2O5TbdhLgEiJ_JPtxNiE3sQjCVjMG1KNWkOha7MygojtsKnIjwyxke8byFfJeGL3aDsszRg-iF7J2owDA-aF-uYuDvzMk-8mOP6o0o7xuR5dF2Ue7PuZWzbVqES_zt_oUOkYOqDU_kRtyvZrIfrl-dqzlB6XPcX7i3NilWDQoao68Qrgo2D5yozthEFH3fnS8jpoMF_ZPKVe9vEyk1A9HUWgRVSTtc73WovcFObAC2lWLRQ1gm6gmSQbaExoTSGbAqht5a7GHyXq5fNou1mss6tXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">المراسل: هل طلبت من نتنياهو ألا يرد؟  ترامب: لا، قلت افعل ما هو صحيح، لكنني أريدك أن تتوقف بأسرع ما يمكنك لأنهم يجب أن يتوقفوا.  كان ذلك يتعلق بلبنان ويجب أن يتوقف. نريد أن ننهي ذلك.</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/naya_foriraq/77860" target="_blank">📅 10:30 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77859">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e4ab89cd65.mp4?token=hUNki83OzULepjtNHstYUpf6tBpqS4BDde0xQ0Qw-DUBxo0ZZegAtwP8XmKElCHJZW2nLJqZkDYRtzxgRR5sWAjFPBW0TpLzib3Ot5sZNF55KlSY3yLwRxWANT3qtVx-CES6uiHQoYoTrac1MUxE0tUNuHUa_Fta6OCQgh1LQFXfc4c_SS3r3Xr9i9V-yw4kNr224aZBSyVQYMmLX7NVPBN16THIJKa0oSyNcoXH29gvX9nLgB1YwIApzINVfIGKbpbr_TTZ5Hx2dbKrcGVQg93Yvmtj9hqxn1WxBGm0huvkgc8hw54zNM5h5LGrYBuux0tvf97hZsfiudpnMYom-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e4ab89cd65.mp4?token=hUNki83OzULepjtNHstYUpf6tBpqS4BDde0xQ0Qw-DUBxo0ZZegAtwP8XmKElCHJZW2nLJqZkDYRtzxgRR5sWAjFPBW0TpLzib3Ot5sZNF55KlSY3yLwRxWANT3qtVx-CES6uiHQoYoTrac1MUxE0tUNuHUa_Fta6OCQgh1LQFXfc4c_SS3r3Xr9i9V-yw4kNr224aZBSyVQYMmLX7NVPBN16THIJKa0oSyNcoXH29gvX9nLgB1YwIApzINVfIGKbpbr_TTZ5Hx2dbKrcGVQg93Yvmtj9hqxn1WxBGm0huvkgc8hw54zNM5h5LGrYBuux0tvf97hZsfiudpnMYom-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامب بشأن إيران:  إذا ذهبنا وقمنا بالقصف، وهو ما يمكننا فعله بسهولة كبيرة إذا أردنا، وقضينا أسبوعين أو ثلاثة أسابيع أخرى في القصف، فلن يتبقى لهم أي شيء على الإطلاق.   لكن لن يظل المضيق مفتوحًا لأشهر. اه، إذا قمنا بالقصف، فستُقتل الكثير من الناس. من يريد أن…</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/naya_foriraq/77859" target="_blank">📅 10:27 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77858">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">ترامب بشأن إيران:
إذا ذهبنا وقمنا بالقصف، وهو ما يمكننا فعله بسهولة كبيرة إذا أردنا، وقضينا أسبوعين أو ثلاثة أسابيع أخرى في القصف، فلن يتبقى لهم أي شيء على الإطلاق.
لكن لن يظل المضيق مفتوحًا لأشهر. اه، إذا قمنا بالقصف، فستُقتل الكثير من الناس. من يريد أن يفعل ذلك؟ أنا لا أريد ذلك.
وسيكون لدينا - سيكون لدينا وثيقة موقعة تكون في الواقع أقوى من القصف.</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/naya_foriraq/77858" target="_blank">📅 10:25 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77857">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hs1kH1gh91eR57CxwzlJRqB4y6aerfBWd1OcfY0gdwywoAyjgOwIly8cp6-fsuqWAhc8T7Q-IoZ54lhoIca6Na2q3HJ3KR9ySKeq1-5I0qrg4teR_S9x259hphsLIolIpoGib9lMxmocLKXuWXb8vGVnqwA3rY_YmGLohu3sP4G5Oy0smbBGME-KCWlYho1NbBFwke0jrSOM6VDCY200IYj6fG3uEZsao0OtKTRsYQ-L5l6A1ctj5glOiomlmU4TmdCU1EMbCfAeJj1eVLu_ZgG0B24RnqmoRyLPoB8jRhq0yvJyVthoTwIIm8CUvMwjJwvcRHw0bVE0q5i_ZivZIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📰
سي إن إن: كم مرة ادعى ترامب أن الاتفاق مع إيران "بات وشيكًا"؟
- أعلن دونالد ترامب منذ بداية المواجهة مع إيران ما لا يقل عن 37 مرة أن التوصل إلى اتفاق "أصبح قريبًا"، إلا أن هذه التصريحات لم تترجم حتى الآن إلى نتائج ملموسة على أرض الواقع.
- ويرى محللون أن هذا النهج يمثل "استراتيجية فاشلة".
- ويعتبر أن ترامب، من خلال المبالغة في الترويج وتكرار الوعود غير المدعومة بنتائج، أضرّ بمصداقيته الدبلوماسية.
- كما أنه بات عالقًا في محاولة الحفاظ على صورة "صانع الصفقات الكبير"، بهدف طمأنة الأسواق المالية وإظهار نفسه بمظهر القائد القوي، إلا أن تكرار هذه الوعود جعل المراقبين الدوليين والرأي العام أقل اكتراثًا وأكثر تشككًا تجاه تصريحاته.</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/naya_foriraq/77857" target="_blank">📅 10:14 · 19 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
