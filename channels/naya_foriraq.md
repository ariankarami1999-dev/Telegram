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
<img src="https://cdn4.telesco.pe/file/KKrb8egOgHuqKidT3erqmFf4gEvE0w2IJb-s0g7Mq7TTDPoEE4Bb4JN_nujb5BbLQO3NyKcJV-XmzQZjEJfggXU13_xRlXzXm8pUpHg-qSr10blaLZFpvgWoVCf29ul_kd-WcA_YUlJ8bOpTi2F9SffiFvH2I68ubufnksRGmokNa-nkLBeW7_zVBKFiDfMPnsc_haa7Zv7NMnCo6r_qVaVjyY9Jo0wnsvn-emY6n-mwHWpcKzDQa3XAH46ciQkrIxqhSIA_Jyan30KQJzDWK4eyZ_ZnR4rpBoEq_K1q9iCqfaNy3Br5PAxHGzeAQ6IXraPjLsUysuJmGijZfUVCAQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 272K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-23 16:13:33</div>
<hr>

<div class="tg-post" id="msg-87779">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">وزارة الخزانة الأمريكية: الولايات المتحدة ستفرض على إيران عزلة اقتصادية غير مسبوقة</div>
<div class="tg-footer">👁️ 2.28K · <a href="https://t.me/naya_foriraq/87779" target="_blank">📅 16:00 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87778">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">وزارة الخزانة الأمريكية: الولايات المتحدة ستفرض على إيران عزلة اقتصادية غير مسبوقة</div>
<div class="tg-footer">👁️ 2.57K · <a href="https://t.me/naya_foriraq/87778" target="_blank">📅 15:58 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87777">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🔻
كلمة مرتقبة للأمين العام لحزب الله الشيخ نعيم قاسم اليوم الجمعة عند الساعة 18:30 بمناسبة ذكرى الانتصار يتناول فيها آخر التطورات.</div>
<div class="tg-footer">👁️ 6K · <a href="https://t.me/naya_foriraq/87777" target="_blank">📅 15:15 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87776">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">اكسيوس:  في الأسابيع الأولى من الحرب مع إيران، كان بعض أقرب مستشاري ترامب مقتنعين بأن ترامب سيدعم نتنياهو في الانتخابات.  في ذلك الوقت، كان ترامب يُطالب بشدة بالعفو عن نتنياهو لإنهاء محاكمته الجنائية.   لكن مع مرور الوقت وازدياد تعقيد الحرب، بدأت مصالح ترامب…</div>
<div class="tg-footer">👁️ 6.99K · <a href="https://t.me/naya_foriraq/87776" target="_blank">📅 15:07 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87775">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">📰
اكسيوس: تشير غالبية استطلاعات الرأي حاليًا إلى عدم فوز نتنياهو. الرئيس الأمريكي ومستشاروه يدركون ذلك. وحتى الآن، لم يُبدِ ترامب لنتنياهو الدعم العلني الذي يأمل في الحصول عليه، رغم تكرار سؤال الصحفيين له عن ذلك.</div>
<div class="tg-footer">👁️ 7.04K · <a href="https://t.me/naya_foriraq/87775" target="_blank">📅 15:06 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87774">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">📰
اكسيوس:
تشير غالبية استطلاعات الرأي حاليًا إلى عدم فوز نتنياهو. الرئيس الأمريكي ومستشاروه يدركون ذلك. وحتى الآن، لم يُبدِ ترامب لنتنياهو الدعم العلني الذي يأمل في الحصول عليه، رغم تكرار سؤال الصحفيين له عن ذلك.</div>
<div class="tg-footer">👁️ 7.02K · <a href="https://t.me/naya_foriraq/87774" target="_blank">📅 15:05 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87773">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 8.23K · <a href="https://t.me/naya_foriraq/87773" target="_blank">📅 14:49 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87772">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 7.88K · <a href="https://t.me/naya_foriraq/87772" target="_blank">📅 14:49 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87771">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🇮🇶
‏
رئيس لجنة الإعلام الأمني العراقي:
التحقيقات مستمرة لتحديد مكان إطلاق المسيّرات باتجاه أربيل ولا مؤشرات على إطلاق المسيّرات باتجاه أربيل من داخل الأراضي العراقية.</div>
<div class="tg-footer">👁️ 8.91K · <a href="https://t.me/naya_foriraq/87771" target="_blank">📅 14:32 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87764">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cGIWNVAwDNy1c_ntpCKv3Gl1V1v5dzcqnxqM9U2SGGjRJy_Iak_fUCPM-fIsBRPS6Ds1LeEJKkmjy3KRIXQeNRo4JYRB6CHfS0IUft_UH9z5DgR_hmPqE8qeQbJww_IvZ6LWrPxOnHGev-chLxXPj7fEV66kLDgclNGHvuY8c6w6HLTjlB7pNAzNLPcT7NzrNvsXuZXvJ2oD2keQ05LKZ0-tHjmrJH0hheDBYrCEdofBlRig7In9tpVCKT6DpyCRBdOaOLiZ63cAgRGytnGe5-dn-DkhaCdgisUGQA-aZxRwx5FF-kqeqv4Qc0aH2VUtpAmkhYDQPZBmtyxQDqYm6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/b5dcH2SUvNrzj1rNNxoXeTZ5y4ucqcY3S7n2oycjShrIZpA5u_Y0OY8_GM8opzygVy-iLzv9CeGMQ1eaPREZ9ki03_2WzQFyCfrl1KTgyDeWALYbvxaf3em6djcL8XuQVqc2qpIWiUBuifCx7I_4rUEUSukjhwXCpKzLjnCAjUzcVWPQFahriwgEKotvXwP6L8qIlCFcYficmGwnl_oI8CNX4_EXNNXMgPWHbH_T5352E4MrnEsFBRcHv-ae-dUMs0GnOjMz5musIE8ctF8FWfJbpSCy4XiLXZtSN7gzVy3ruLz50_UZ2MtAYOZkGNjUn3zhVMRmQtuuATmDFSi0lQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/p30vn_LzSWRFxN5RengilYHcgeaqJyTXB4u3vueBh_mF7_Rs9-yJ70fYIT--XSUzgZYgyoDWLe8Iq97KE7kLU23DRxpFdeHsja0sX8ph7A-3zRyH5t5hbrCYT4QS0oXe2Uhk9-45WjFAdALfzvtjt8WgE6pJFzMi-uCUIyXvr_EbbduCzgan0mpQrld2WyInDSYM6bKLo42SQMO4QdNeDse0fbZAN8TDxkhW6kDARMkpjUjUFrZXSQunEH6AOGpyhRDa1aXKdCiRVKJIYIzSV7ZrcAZhik25fAv9dhnuQ9un861f1y087ewHtc1o_a0rVJ3GxQWSkd_GqdvNdsC2Pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bSDiKnjQyDg0cv31qmk_ZuMZgzTlUK91TaD32QuZ6hKlGQrRA3u6zOR9R8PIN9Nv1INYW_fodefsnrydG7lizjhqrYGdojqsdO6rXjNbStvDnohKxm0yEsY3OXKJt6qD4wVGJSf865PiXNdSRZX15oJDnxaNyae2a54AdydgbrKR9tU2uf63t-7PiWJTNEzRmYFJl5hdEzRkR1U0b1JZ3KyIsXsS8AzB6dw7LZIVJ8OXjJqq7he7CTNhxPeZQ44AjciL3fs4x91j3cDi2VupdwUu8Ad7wPiu25nqtXQEy6r4R6qJq-O0ORbUTcvi9T5bMpu_rcFPUe708neKl2Fa5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pfHsbTyxuOsPzEaoL2XJNtTkyDIMbB1P35DAj0w3s-oquOzcFWsv71EAPnOgpF8tVy5A1hfW1lqrvYk0SKg3G1Q6y0Nd2p3bS8F70NNcXReIBpRihL2gp5hZhJYbdsigrwqlUm3BA2Nxuj7sltSch_cF511j48pfF-_bEXD8XZlyyNEEs4Wgo91zagCYVIeMTKWwsQeHgnku-aCBH3sD-V8UULexDdpYmzx1AljUZwVZrzSRfZtg0gC39CCQZXxF0qdqBFgfBG2BNLymuHmuWpGu2FyM3z4W5ipprhaB6SligRu41GMV_xmyF30S9HxcOGSRe-KD94JdRp5iC5YPkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gwOcq_uCYtmdDMjmnpDIA8-CnSNgwUjCGSruBCBGVRVDb2n1LJK65nmWrzp-X74SBdretjNTLKIua0HGPwu39TOuTNdcbvag3uLC_4MqR5n1nUrr0uJcXgpzU_UFVTqZXeJqEVFCAmoxASlTCUqTvewB-BhD6SuE9gVqPIWzssMOu59BNrS0-uqF6XpKnwMMR33j3xnvgoLV2ve5rlRkcCbeKpzNfahY6oX8VW3ls-qPz5ANxfNAXdyXyyo0RyNstrgVPLst0-aZpRGbEXvW2lO_5bTX9yqP-NIi30FneW36rjXmz56hrKSG3z5YhuKDWyPz2MegEC8911a2JviDFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lym_qTsMNVo3PsxDfn9SE6oIUsJFWpMBJFH_frLwB1yNOZljXy-UMDn_IAzeahb25mnPgRktZqfGR7ObGGUvouUIhiY5cBROTO-vnV9PZGlaxtJwfgH3qU7PqYUiS23cr8qT7j8Nqjbg-nPUZL6Tqu_7CUi5t1xbV8vJVWnaQN4SYLwJI6T-_9cQavdl2bVmtAfRoeHVKU0gw35qEvgf6roLW2pLdXdqOsbEyV-lH9Z7QHd7kNwiPNUg9IdWOBRcw99Waw5H9QyscaNQIQRv8xawJTceVDymcKiykmOURTcAbPhEnRl4Cgv-cIeFRGKfyzMtJpDfSi0fImd3jp5cEw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇮🇷
صور لطائرات مسيرة وطائرات مقاتلة أمريكية إسرائيلية تم تدميرها بواسطة
الدفاعات الجوية الايرانية</div>
<div class="tg-footer">👁️ 9.53K · <a href="https://t.me/naya_foriraq/87764" target="_blank">📅 14:22 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87763">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">مسلحين يهاجمون وزير الداخلية في إقليم بلوشستان الباكستاني في منطقة مستونغ.</div>
<div class="tg-footer">👁️ 9.02K · <a href="https://t.me/naya_foriraq/87763" target="_blank">📅 14:16 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87762">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">الله أكبر
🔻
إستهداف سفينة "ناقلة نفط" في مياه مضيق هرمز والنيران تشتعل فيها.</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/naya_foriraq/87762" target="_blank">📅 12:54 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87761">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🇷🇺
وزير الخارجية الروسي
لافروف:
لن يكون هناك هدنة في أوكرانيا. موسكو لا تنوي إيقاف العمليات القتالية على خط التماس الحالي.</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/naya_foriraq/87761" target="_blank">📅 12:39 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87760">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GNngoU1ZygIRuMuyS_LNznjWqYDfyJWFz6QxewB4qW-7GTO-Q78BdX4b-4nt_zMQ20r0N_h4wixPC9kfjBR2cxShuGhyxfPmOWyVDvHFA1zJ6RsAmPOnpzc7HgG8jS8DjhPhI0n6_HqD4Stdy4texu5cfR3GJIysagz6ufSu5nusCkfovrteFfbMcbbOLoyk267gGcPW20HHJQ0nvUzmYDyQyTzQ9pkJJvnOYSL4FE0GIfCihLZL1qbaMk9Oj9tB-nyuONoj7pdYGKSjyf9WXo3_Zbq3HJ1YsBVNNTZ1rvcuWrEia4nRfD_5YYhABDGpn8s1JFpugaOL7faKE_2N3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الله أكبر
🔻
إستهداف سفينة "ناقلة نفط" في مياه مضيق هرمز والنيران تشتعل فيها.</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/naya_foriraq/87760" target="_blank">📅 11:30 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87759">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🇮🇷
المتحدث باسم لجنة الشؤون البرلمانية في مجلس النواب الإيراني:
تمت مراجعة مشروع "الإجراءات الاستراتيجية لتأمين مستقبل مضيق هرمز وخليج فارس" في لجنة الشؤون البرلمانية، وبعد الاستماع إلى الآراء، تم اعتماد مبادئه العامة.
أحد القرارات التي تم اتخاذها يتعلق بمنع مرور المعدات والمستلزمات التي تملكها الولايات المتحدة وإسرائيل والدول المعادية عبر مضيق هرمز؛ وذلك لأن هذه الدول استخدمت مضيق هرمز لتنفيذ أعمال عدائية ضد بلدنا، وارتكبت انتهاكات وهجمات غير أخلاقية ضد الشعب الإيراني.</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/naya_foriraq/87759" target="_blank">📅 11:20 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87758">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🇷🇺
🇺🇦
وزارة الدفاع الروسية:
استهداف سفينتين كانتا ترافقان سفناً تحمل أسلحة إلى أوكرانيا.</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/naya_foriraq/87758" target="_blank">📅 09:16 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87757">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4ed4908a7c.mp4?token=CTzoxchOFNQQxsf-f3pURDrU7m_qPBNc3TS_hsEy5DEVTXWt1LSDg9gO7A93QYQIQre1VQ7O7JKasQBxPKClJvw6cJ8xbBG_4lrzkqiog4I2tPFDt63OXxhyxHKmBIAJSyVHENZcilOo7XIPSHHi3zQ6RZWI0VMkrE2WimCkVecj3QJIwY6oSVHW5xJmghx4I-ZGsUZTFal66t-aDjoMbzyMnvQuAc7pfHgINbyg6EAuaE6uDXnrVTOubIgDaNTvlab0imppFMYPjdZ_BRJE4MKRvPCYRBmcx-v7Zobd0LRfjkDvOHonSt_iwzdzqeqP8V5E3xPjTdJglBM6LRkbRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4ed4908a7c.mp4?token=CTzoxchOFNQQxsf-f3pURDrU7m_qPBNc3TS_hsEy5DEVTXWt1LSDg9gO7A93QYQIQre1VQ7O7JKasQBxPKClJvw6cJ8xbBG_4lrzkqiog4I2tPFDt63OXxhyxHKmBIAJSyVHENZcilOo7XIPSHHi3zQ6RZWI0VMkrE2WimCkVecj3QJIwY6oSVHW5xJmghx4I-ZGsUZTFal66t-aDjoMbzyMnvQuAc7pfHgINbyg6EAuaE6uDXnrVTOubIgDaNTvlab0imppFMYPjdZ_BRJE4MKRvPCYRBmcx-v7Zobd0LRfjkDvOHonSt_iwzdzqeqP8V5E3xPjTdJglBM6LRkbRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الله أكبر  لحظة انقضاض المسيرة الانتحارية والانفجار العنيف في مخبئ للقوات الأمريكية بمحافظة أربيل شمالي العراق</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/naya_foriraq/87757" target="_blank">📅 03:16 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87756">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb53d6775a.mp4?token=Bg-xq7HQJPz68Zt6I1S65VlCMh19YOx9wPN8rH4r4yAOZiijisIszkANQmURkuk5de7xDByT6xUYvi_T4PyJ98n5y3VtX3UOVbv0LkqqrsdcLF3wHlKadJfMAkLErgsv7CZ7vFkvvCDnVKCUkqC8j5xxk_9t1kqH96X91c-3a4qaUp-LLgc7tg3HM9N7k3YE7SuSNNyjHvbHrAc8QvwatTzYqyHNu9o9ydj9N57eHSg7L93oJgkPWl9gqSjyJO2q4Bzo2VgCuqkLZkfrjVlz4ae518gsjHCaOwBAYGLLgESNHh0PHq0Wk4ZPMU61xSXgrAcqk5rxBxRG_wwJfUXBPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb53d6775a.mp4?token=Bg-xq7HQJPz68Zt6I1S65VlCMh19YOx9wPN8rH4r4yAOZiijisIszkANQmURkuk5de7xDByT6xUYvi_T4PyJ98n5y3VtX3UOVbv0LkqqrsdcLF3wHlKadJfMAkLErgsv7CZ7vFkvvCDnVKCUkqC8j5xxk_9t1kqH96X91c-3a4qaUp-LLgc7tg3HM9N7k3YE7SuSNNyjHvbHrAc8QvwatTzYqyHNu9o9ydj9N57eHSg7L93oJgkPWl9gqSjyJO2q4Bzo2VgCuqkLZkfrjVlz4ae518gsjHCaOwBAYGLLgESNHh0PHq0Wk4ZPMU61xSXgrAcqk5rxBxRG_wwJfUXBPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجارات عنيفة تشعل سماء أربيل شمالي العراق</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/naya_foriraq/87756" target="_blank">📅 03:11 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87755">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0fe85afd9a.mp4?token=MewM0JkubLKc33BjFgLm_cLbmk1kX5cpKv1fX0Sa0tgG-nt8ZNf9JoDYQo_lAoj8ZxRZ_hcJokcyBMWJSoBzGK4cUjhRU3e1tecFHZb2bDLDTM1NrP66v_hapaRRKDoqWOk_VwlPUlDDuKksx7gcm3ZAR7qMZt6PJ38-ZVI7a3j8wTv6ve3rTccVtgmUuaiqoxA3k7asbK0BUvn9QlkgHLeFVMXQeeP5g5mpgT1JVJgR5A8TOhnAYYv1AVuatzeUwtAjLksYJPJVFIGr6RjW1ZRGmzA1l4TE83lBcM6ggrHuCmmnBozAf5skPIpcoz49tT7HlO5R2BmTdrPILiZSPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0fe85afd9a.mp4?token=MewM0JkubLKc33BjFgLm_cLbmk1kX5cpKv1fX0Sa0tgG-nt8ZNf9JoDYQo_lAoj8ZxRZ_hcJokcyBMWJSoBzGK4cUjhRU3e1tecFHZb2bDLDTM1NrP66v_hapaRRKDoqWOk_VwlPUlDDuKksx7gcm3ZAR7qMZt6PJ38-ZVI7a3j8wTv6ve3rTccVtgmUuaiqoxA3k7asbK0BUvn9QlkgHLeFVMXQeeP5g5mpgT1JVJgR5A8TOhnAYYv1AVuatzeUwtAjLksYJPJVFIGr6RjW1ZRGmzA1l4TE83lBcM6ggrHuCmmnBozAf5skPIpcoz49tT7HlO5R2BmTdrPILiZSPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الله أكبر  لحظة استهداف مخبئ للقوات الأمريكية في محافظة أربيل شمالي العراق</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/naya_foriraq/87755" target="_blank">📅 03:07 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87752">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ba4fbc1059.mp4?token=AjbBlgQu3_is7Ij9D0UmJXTmHo-nNSJnBiuuuOFLLDj6n0RJs0s_Y_sToTF6L2goqgZ5pH8fpsDlp6bB3oJbgJlpzSLe-qL_EJgc_F1UUc-u-p_57IPAdDCJ-8VqDg6ZS3UtlkckjM_Uy16TCn9f12GzP9v4HP-Q4C2WKgi5roSCgAIQIfVnFFsjdN8XzFUQp16qlYCRoR3ZVS_6loZ8M4wjOGQldNWtpmKRZHTKwKyVM_y2YQFMdX4ek9iJ7tnNTlE6CkWh-YQyWgmR1pAyMW8YNoH83LeQHtLTdduN7r0DYNlA8Umu8_UxQGGeFW8eZXAB7wQYXdjN8pPWO_R4mw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ba4fbc1059.mp4?token=AjbBlgQu3_is7Ij9D0UmJXTmHo-nNSJnBiuuuOFLLDj6n0RJs0s_Y_sToTF6L2goqgZ5pH8fpsDlp6bB3oJbgJlpzSLe-qL_EJgc_F1UUc-u-p_57IPAdDCJ-8VqDg6ZS3UtlkckjM_Uy16TCn9f12GzP9v4HP-Q4C2WKgi5roSCgAIQIfVnFFsjdN8XzFUQp16qlYCRoR3ZVS_6loZ8M4wjOGQldNWtpmKRZHTKwKyVM_y2YQFMdX4ek9iJ7tnNTlE6CkWh-YQyWgmR1pAyMW8YNoH83LeQHtLTdduN7r0DYNlA8Umu8_UxQGGeFW8eZXAB7wQYXdjN8pPWO_R4mw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">استهداف فندق يتواجد بداخله عناصر من القوات الأمريكية في أربيل شمالي العراق</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/naya_foriraq/87752" target="_blank">📅 03:04 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87751">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b228489921.mp4?token=camgN_YyJnPHltueWUz0GTfovG3T-6PA77MkxrROpCQXx0CM6oyp-5As6u2PioaEfrJB5pT4ruB1jy-6CUtMGsfMuPqudkChHuUm8O9PpoSEOdkVGfs5Di-6qV8BG6XHdfLm1PZQfp92KFhj9-bZTowemty-N1a6jo1rpiwq6Ub7t8O9ekk0ENa0OUWoBNgxxVPJmih4JjUJ2O0_PM2GWom9VYNck1ttRrCH4vB5DJNMMfsofrg1qEtcpInCX5wGbMnV2ccPv9AtX-CEI9hM9QS9s9kYKq1ohBAM9CPU6CI4ILv7_Ece6HKZKPvKzXUOLQdl8PGsKnpenX6b970gaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b228489921.mp4?token=camgN_YyJnPHltueWUz0GTfovG3T-6PA77MkxrROpCQXx0CM6oyp-5As6u2PioaEfrJB5pT4ruB1jy-6CUtMGsfMuPqudkChHuUm8O9PpoSEOdkVGfs5Di-6qV8BG6XHdfLm1PZQfp92KFhj9-bZTowemty-N1a6jo1rpiwq6Ub7t8O9ekk0ENa0OUWoBNgxxVPJmih4JjUJ2O0_PM2GWom9VYNck1ttRrCH4vB5DJNMMfsofrg1qEtcpInCX5wGbMnV2ccPv9AtX-CEI9hM9QS9s9kYKq1ohBAM9CPU6CI4ILv7_Ece6HKZKPvKzXUOLQdl8PGsKnpenX6b970gaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">استهداف أمكان تواجد قوات أمريكية في أربيل</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/naya_foriraq/87751" target="_blank">📅 02:59 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87750">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e85c067dbd.mp4?token=PU-DpTBCPY63JWnj62ZdzCrOhf_7Lp_sxEIlOVFxpRU_gjIGoWBWqrtiHkzRO0vV7ut0xVCMQT2l10Vv90DKmXjF1l9BbDTMlfwVB3c5UtVzuGgPP7a_q_sFJiyNWfddL7DMYBcpoZj-w4__fPH18pHo672OBB4GE2C0KdGrZbnrMY26kuYfdGdYXgOHDZ_AHwRAmWIu59Zp7OeH5xqfEA5umm7TzdaBYZnFNwi7I5zjaUGzXF4Yl8AtaeiTSY7IkTubifUA2K9cwuVeJJkwycqA0k_5_dFRq3yY2HmhSftJ0K_flJjekJ6ppeFX9uON4oJxO2WbDLJMSsza11Ma_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e85c067dbd.mp4?token=PU-DpTBCPY63JWnj62ZdzCrOhf_7Lp_sxEIlOVFxpRU_gjIGoWBWqrtiHkzRO0vV7ut0xVCMQT2l10Vv90DKmXjF1l9BbDTMlfwVB3c5UtVzuGgPP7a_q_sFJiyNWfddL7DMYBcpoZj-w4__fPH18pHo672OBB4GE2C0KdGrZbnrMY26kuYfdGdYXgOHDZ_AHwRAmWIu59Zp7OeH5xqfEA5umm7TzdaBYZnFNwi7I5zjaUGzXF4Yl8AtaeiTSY7IkTubifUA2K9cwuVeJJkwycqA0k_5_dFRq3yY2HmhSftJ0K_flJjekJ6ppeFX9uON4oJxO2WbDLJMSsza11Ma_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">استهداف أمكان تواجد قوات أمريكية في أربيل</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/naya_foriraq/87750" target="_blank">📅 02:59 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87749">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/naya_foriraq/87749" target="_blank">📅 02:58 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87748">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/naya_foriraq/87748" target="_blank">📅 02:58 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87747">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ac3c86dbe.mp4?token=aQ5q4JVak56zcE9mG3EsxoFGgnPyCYtosc_YHc7-YSMh5jItPw1ND0NUaj-bCFKwj4is86DCTK4xUeJAErwg3aFe82_O3gLpRKDqYp2Fmx7XQLrmD9IzeYPKC1OZ5OKNLJM2231zEDV9KqynzU6WXgSx-oboEe6NoMpEZcNF7udo_1K9Ho7FqfYIKSzW8seMf4zZV-I4_bvaYKN-GUuBIk3clJ38nZcmptBAKslbh2AH7cuKMeDeMhQ6OgZEw9RRu-wmlOEYj5TPWfKjRkNvx0B-k8CkPT2VSwPVaRHs8nld4KDzDm1MgxDWjaLaWtno4znitup3YOxBCXGWsLthQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ac3c86dbe.mp4?token=aQ5q4JVak56zcE9mG3EsxoFGgnPyCYtosc_YHc7-YSMh5jItPw1ND0NUaj-bCFKwj4is86DCTK4xUeJAErwg3aFe82_O3gLpRKDqYp2Fmx7XQLrmD9IzeYPKC1OZ5OKNLJM2231zEDV9KqynzU6WXgSx-oboEe6NoMpEZcNF7udo_1K9Ho7FqfYIKSzW8seMf4zZV-I4_bvaYKN-GUuBIk3clJ38nZcmptBAKslbh2AH7cuKMeDeMhQ6OgZEw9RRu-wmlOEYj5TPWfKjRkNvx0B-k8CkPT2VSwPVaRHs8nld4KDzDm1MgxDWjaLaWtno4znitup3YOxBCXGWsLthQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">المسيرات الإنتحارية تشعل سماء أربيل</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/naya_foriraq/87747" target="_blank">📅 02:56 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87746">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e026876dc.mp4?token=urTT6j8o0iU6j07Yd_uX4oL0Y-TEPIOq3ETqCPVa8iMFFFJyyObwfYEdppTfjDqcDZqWx9OM746zYrzlw3H4B2IU_BAPjXoxhKi55Rz7DQlbNcKhJGwheBh7p0edaPIxZZFw1Ob_3kPe0rj5jrUug4FQ_29Nza5AwUdDtM-LwmQN4Q9kSVjQkcq7UnCLf6ISWpStRnjSzOqh7xX3_k4grGA0RdNyJl9TNR2xmmYDP-hzttQoYjfDC8DHnrVq01KrPBAsedFnd54DibhKL4jkXaIoJ18I5HN_RbzawxZ80e4O4ESNtNCgliPuSVCVZQFCdbYK-Dgf3IPpZXsQ02qjNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e026876dc.mp4?token=urTT6j8o0iU6j07Yd_uX4oL0Y-TEPIOq3ETqCPVa8iMFFFJyyObwfYEdppTfjDqcDZqWx9OM746zYrzlw3H4B2IU_BAPjXoxhKi55Rz7DQlbNcKhJGwheBh7p0edaPIxZZFw1Ob_3kPe0rj5jrUug4FQ_29Nza5AwUdDtM-LwmQN4Q9kSVjQkcq7UnCLf6ISWpStRnjSzOqh7xX3_k4grGA0RdNyJl9TNR2xmmYDP-hzttQoYjfDC8DHnrVq01KrPBAsedFnd54DibhKL4jkXaIoJ18I5HN_RbzawxZ80e4O4ESNtNCgliPuSVCVZQFCdbYK-Dgf3IPpZXsQ02qjNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هجوم عنيف بالطائرات المسيرة الإنتحارية يستهدف مواقع الانفصاليين في أربيل</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/naya_foriraq/87746" target="_blank">📅 02:53 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87745">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b53b0dfcfc.mp4?token=Bk2MyRBemw1dHJZ9u_xk52bD8momK8-xJVYcWFccOxpcpIcV3V7H2vjin9kgGcSeD0ns5G3_DXUWmpNHDxR8SrABXpvWEjViLTTL1T4Iqr0wUvrgJngHFGPrs7DGiBBIDNemPSFkKo67xPfoZZ70HRxIrzmXIkiNMaRKi02Q0HYTwlcAar7Um3msTc80WkGhJ7_Yb11VyZFvMgF6p9LoPhJKXhW_3OWFUGG43QF3ZWJjeoyW8M2SJvl2vBRncWnGDcXMAbfNrq-aeIXW_USBonR-3Iz0v2cXp5ZK_JOTdQN-dVbLy9xc1z6-QeE5gjMU8JsKWAOCs1n9qxRVY4FPMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b53b0dfcfc.mp4?token=Bk2MyRBemw1dHJZ9u_xk52bD8momK8-xJVYcWFccOxpcpIcV3V7H2vjin9kgGcSeD0ns5G3_DXUWmpNHDxR8SrABXpvWEjViLTTL1T4Iqr0wUvrgJngHFGPrs7DGiBBIDNemPSFkKo67xPfoZZ70HRxIrzmXIkiNMaRKi02Q0HYTwlcAar7Um3msTc80WkGhJ7_Yb11VyZFvMgF6p9LoPhJKXhW_3OWFUGG43QF3ZWJjeoyW8M2SJvl2vBRncWnGDcXMAbfNrq-aeIXW_USBonR-3Iz0v2cXp5ZK_JOTdQN-dVbLy9xc1z6-QeE5gjMU8JsKWAOCs1n9qxRVY4FPMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تستمر الانفجارات في محافظة أربيل شمالي العراق</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/naya_foriraq/87745" target="_blank">📅 02:52 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87744">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/557c261eaa.mp4?token=KUNt4erueYHJMfDpcL6vPZFU3qLQmI6D18f-JfEnEB_QYrDVqCKnvvRTuZDEBzFwrdwmPAFtn-_6v9OOak0XJRzqTWUq0yGpLbhfjs5QzhNrzASoJLYFxxzCTyoGCmdWZdqViRduzGpW57eK6Z-NF_myabEOwF9woB4NFaRu8MqRtDWKnjzT4NM-AJqX_NPUth4Nw8kmpiUaFkHV2GEcDAYmwNeB5xgtm-m0p2Bm8yo_CNTl4e8cJ72FrKfY-LvhlWjuLdiWdBg64raT4zhNY3wr_zMIxrHOPBh_aOQ9RM5zNrnNnu9QMmDAz9cypkBQBicK8TaGYkm2XQlONik22w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/557c261eaa.mp4?token=KUNt4erueYHJMfDpcL6vPZFU3qLQmI6D18f-JfEnEB_QYrDVqCKnvvRTuZDEBzFwrdwmPAFtn-_6v9OOak0XJRzqTWUq0yGpLbhfjs5QzhNrzASoJLYFxxzCTyoGCmdWZdqViRduzGpW57eK6Z-NF_myabEOwF9woB4NFaRu8MqRtDWKnjzT4NM-AJqX_NPUth4Nw8kmpiUaFkHV2GEcDAYmwNeB5xgtm-m0p2Bm8yo_CNTl4e8cJ72FrKfY-LvhlWjuLdiWdBg64raT4zhNY3wr_zMIxrHOPBh_aOQ9RM5zNrnNnu9QMmDAz9cypkBQBicK8TaGYkm2XQlONik22w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">استمرار طائرات مسيرة في التوجه نحو مقرات</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/naya_foriraq/87744" target="_blank">📅 02:52 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87743">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64f1e06b63.mp4?token=JM2W5j7maXd4lYltB5MRxyaYCdg3s8Lt0hLSNKtcas8r2kZlDVaXvFD46tv6A59411bFYQVIMONjFxZdrYfPlNkxQg6IDYDtXsx1V-uIqmdldt56WIaYv5jpU5OoHlZVpbRD23FfhSs_eV5YadzyWWsLKkiqk2txJfh8q-3itHAkp-1mIKVFxezb2dy4X67V5tbyPDjmDs2TL1gg6h9FVuxl0g5yoB4oVEyKhoVJnsnKrrshevS3xSx3_o84PbIyTyl65aUSJufrEwCqZPukPdIzl4lzyCvfxzLhtvsNcXVvc8Fc_inP6sAsR3BwFKTq74sI-MxFnlP92guKxY5LmA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64f1e06b63.mp4?token=JM2W5j7maXd4lYltB5MRxyaYCdg3s8Lt0hLSNKtcas8r2kZlDVaXvFD46tv6A59411bFYQVIMONjFxZdrYfPlNkxQg6IDYDtXsx1V-uIqmdldt56WIaYv5jpU5OoHlZVpbRD23FfhSs_eV5YadzyWWsLKkiqk2txJfh8q-3itHAkp-1mIKVFxezb2dy4X67V5tbyPDjmDs2TL1gg6h9FVuxl0g5yoB4oVEyKhoVJnsnKrrshevS3xSx3_o84PbIyTyl65aUSJufrEwCqZPukPdIzl4lzyCvfxzLhtvsNcXVvc8Fc_inP6sAsR3BwFKTq74sI-MxFnlP92guKxY5LmA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تستمر الانفجارات في محافظة أربيل شمالي العراق</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/naya_foriraq/87743" target="_blank">📅 02:52 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87742">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">استمرار طائرات مسيرة في التوجه نحو مقرات</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/naya_foriraq/87742" target="_blank">📅 02:49 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87741">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee52060d77.mp4?token=pLBiYgl0msv7aV9JClqeYphE-AyjHBrY0U4rfcUtVKdZMCeKPFcCT5iNz8c6sgFP_M923ZuWF1zcRG6YIwJQsO5HgWkBX2Z_D1I_xUZRzUmMHufXb08OoTtC4VfTv17o3d2S0DPyGZC9oYu-kWxtJTEcyFtxCzsqkMJM3QBXclrTecYo5mOgraPn__zvSTcQQot23WjS6GdUlpvIaG8OtT9Tah-bbh6g0l3TPD9Dx3wotjf5blVa7Wu4_N7SdhH3RpQMy1yBDJdksuvaZIfvIrP-6h-nHjDfGvDKyDSJ3THZKzBMQJce8vXIo9Jc0YlaW9zl0dHn4_4Yd3J-zDVdNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee52060d77.mp4?token=pLBiYgl0msv7aV9JClqeYphE-AyjHBrY0U4rfcUtVKdZMCeKPFcCT5iNz8c6sgFP_M923ZuWF1zcRG6YIwJQsO5HgWkBX2Z_D1I_xUZRzUmMHufXb08OoTtC4VfTv17o3d2S0DPyGZC9oYu-kWxtJTEcyFtxCzsqkMJM3QBXclrTecYo5mOgraPn__zvSTcQQot23WjS6GdUlpvIaG8OtT9Tah-bbh6g0l3TPD9Dx3wotjf5blVa7Wu4_N7SdhH3RpQMy1yBDJdksuvaZIfvIrP-6h-nHjDfGvDKyDSJ3THZKzBMQJce8vXIo9Jc0YlaW9zl0dHn4_4Yd3J-zDVdNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجارات متتالية في محافظة اربيل</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/naya_foriraq/87741" target="_blank">📅 02:48 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87740">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf3518d796.mp4?token=sOARB31MylyDqPCH4lim1TggUBvYUoGf0Wzg0wv2RT44dJWDV5nmzWafkX5OLNZ0ge8LCJDNK2vnMIffXaToqJ8Xl12UzcZ3sCbmLhApddQInaRiEQygO4y8-1hpKSz_OPLkWUDyE0T8TTnoHSGTR3GjlbcUTv-7i2iaKp8zEjpzTns4q_uzJUaQsvf-fdQw84OkgqEodxVaq3ei0MutGrtMyM4DZqwhXR_m_4pcPQ2KrezP-iZt0ubeTOiKsAHrLw_jdRaOyaVFMDKhLjQ1Xq_lM7R5gLk3O4Q8Kg2TYsTUMzvVZOMoUKeUisXiT3wRx2B6sBA4fxLuKqvlj7bnTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf3518d796.mp4?token=sOARB31MylyDqPCH4lim1TggUBvYUoGf0Wzg0wv2RT44dJWDV5nmzWafkX5OLNZ0ge8LCJDNK2vnMIffXaToqJ8Xl12UzcZ3sCbmLhApddQInaRiEQygO4y8-1hpKSz_OPLkWUDyE0T8TTnoHSGTR3GjlbcUTv-7i2iaKp8zEjpzTns4q_uzJUaQsvf-fdQw84OkgqEodxVaq3ei0MutGrtMyM4DZqwhXR_m_4pcPQ2KrezP-iZt0ubeTOiKsAHrLw_jdRaOyaVFMDKhLjQ1Xq_lM7R5gLk3O4Q8Kg2TYsTUMzvVZOMoUKeUisXiT3wRx2B6sBA4fxLuKqvlj7bnTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">إنفجارات في محافظة أربيل شمالي العراق.</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/naya_foriraq/87740" target="_blank">📅 02:48 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87739">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">إنفجارات في محافظة أربيل شمالي العراق.</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/naya_foriraq/87739" target="_blank">📅 02:48 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87738">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🇮🇶
دعوة جماهيرية في محافظة بابل  ردًّا على محاولات إثارة الفتنة والتحريض الطائفي، ودفاعًا عن أمن المحافظة واستقرارها، تُنظَّم دعوة جماهيرية شعبية في محافظة بابل للتأكيد على رفض عودة الإرهاب والعنف، والحفاظ على الهدوء والأمن الذي شهدته المحافظة خلال الفترة…</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/naya_foriraq/87738" target="_blank">📅 02:06 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87737">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">زلزال في جمجمال وكركوك شمالي العراق</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/naya_foriraq/87737" target="_blank">📅 02:00 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87736">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🇮🇶
دعوة جماهيرية في محافظة بابل
ردًّا على محاولات إثارة الفتنة والتحريض الطائفي، ودفاعًا عن أمن المحافظة واستقرارها، تُنظَّم دعوة جماهيرية شعبية في محافظة بابل للتأكيد على رفض عودة الإرهاب والعنف، والحفاظ على الهدوء والأمن الذي شهدته المحافظة خلال الفترة الماضية.
وتأتي هذه الدعوة في محافظة بابل التي عانت من أعنف المعارك ضد تنظيم داعش الإرهابي خلال عام 2014، وما خلّفته تلك المرحلة من مآسٍ وتضحيات كبيرة.
📍
المكان: بابل – المسيب، قرب سيطرة التحرير
🕒
الزمان: الساعة الثالثة ظهرًا
يدًا بيد من أجل أمن بابل واستقرارها، ورفضًا لكل خطاب يدعو إلى الفتنة والعنف والطائفية.</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/naya_foriraq/87736" target="_blank">📅 01:52 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87734">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hc9CBoBQYivvEVj7NdSh4pWzfN6No6nJUqnbfzlWQC7STZOt-oG2zrM3qEiPyaREpVGLHq411Pi4i7T3buQ_QUhNSPw3uffT6XknCs1gCUAQQcsCLNtpdy-El1QYG4DhSxvDgodzxp-_vvFdW_4r5slM3YP5rhHTT5TiedAwVC3DfDq5bUj-dYljIp1kKAKHso32O1UGSO_U1BQe0Yv1dJ1nn_9mZ-rUVKUGG5lhmRz_T1pIVkLh540OCcXptUWCkquPIZDfPQWq2BAmr3NKTxU5Su8UI3i9c--HE3zIhVqtgZttmTDgNyYeC72R5zL418rq7B2JNGlpTqRNfuLPPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qc6_-KoFPtOv33ozPix5EC2ISGGLjX3Zl1317Wqru95xlN1APydkRC1dT__HjdeJCwtS82yJVGT2TeoXJ6e-fJztcY8X_p5a3tjuEQjt4FEttNiOepdYV8jPckNN3t5yySW7AQHfZaLTFpdXlVpaR7C1QZownbGQZboVEiwaJ9uToVPMP8wrwpGKQqwIphGzPIqu4VIzPNS---eXoARL-EBKebgWXY5D9KMuZnTlpvUz9kCK-XHSD59_6f_WJFllibR85Dpvlru5Ldr2dBjsTuyltn-KYV5fWz_Bj8Ud6CCoQ0kR33Yp7rVEqTtJzPUENzf1aZz_heCD_jfL1fqFQA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇮🇶
إشادات شعبية في الأوساط الحشدية بمواقف مدير المكتب السياسي لمنظمة بدر، ودفاعه عن سلاح فصائل المقاومة العراقية.</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/naya_foriraq/87734" target="_blank">📅 01:50 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87733">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🇺🇸
‏
وزارة الحرب الأميركية:
نراجع حاليا استراتيجيتنا النووية</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/naya_foriraq/87733" target="_blank">📅 01:50 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87732">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fSQ5cLzvdjznYHGeLPDuK0_ldpc_BpwG8p1ouywwF3fibgwgZBq0Mb-iZNge4hL-M1ntsiVxPIuT7N2Dga5-NIYPYr1oFpFHaD2LiqzIt82pNb8lbjPyP9Ien7LD2eGYGFJhECgd6VmvGBsZzHspk0VcK7b8gOnRIpSzYo2OizJV1X4kbeL_h3y9ZFGHxfx5_ocdqI4Jy5qTBWeLgBjk2uc606Aa73OXhkF7J0rFpbDQSAeASm_ZriuGDjMqcF4ncwb-fa-lfN_DSwNBc7uEqPieMX_jg1bn8SCJQtLhwrDZnw8xTb_5e0ExPQ_LxapaGfBXW05Yc2PxvZ-UpSTTcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
الأوساط الثقافية والسياسية والإعلامية العراقية ترحّب بتكليف الدكتور عباس العنبوري وكيلاً لوزارة الخارجية ..</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/naya_foriraq/87732" target="_blank">📅 00:59 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87731">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">شركة أدنوك الإماراتية:
تعرض سفينتين تابعتين لنا لهجوم أثناء عبورهما مضيق هرمز دون إصابات.</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/naya_foriraq/87731" target="_blank">📅 00:02 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87730">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🇺🇸
‏
نائب الرئيس الأمريكي فانس بشأن إيران:
هذا الأمر ينتهي بنا في موقف قوي.</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/naya_foriraq/87730" target="_blank">📅 23:50 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87729">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">هجوم سيبراني استهدف منصة دائرة الضرائب الفرنسية</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/naya_foriraq/87729" target="_blank">📅 23:40 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87728">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fClYvf8HX2EJCIF1nR0f9THl0T5kpySHadFLBXWqxOz8fMn__EpC1LNagxLh-Jc_Mdp43R5v3034yD-ME-g9NwQe1jO4vRmrUfT7dwglmQmG_RgBv7eHXWOeAwB4UzAMZ4ALaPVh3HP1IpxndxbGEGk6ZtPWWRLe2VxnhUu3iwDOSlAjpecR-I0Lds0uGsBU1MeF_iooBaq7SiBs_Qugl75Th6urwD5mWkEaHd6g2ZJq76lR6HWfBtU4S7o88_-wh8grRZYqUOX0cOGwDNiOIrOrPkjTNEi4KYNaDJsLCirj-Mpky5T7dsSFnGpMCpALLx2ahlQzjItg9FWhDdBNWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
🔻
جرف النصر .. كعبة المنجز الأمني العراقي الحشداوي
دول إقليمية تريد عودة مثلث الموت ؛ دار استراحة المقاتلين العرب ؛ مضافات ما يسمى ولاية جنوب بغداد الارهابية ..</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/naya_foriraq/87728" target="_blank">📅 23:38 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87727">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">هجوم سيبراني استهدف منصة دائرة الضرائب الفرنسية</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/naya_foriraq/87727" target="_blank">📅 23:38 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87726">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🇮🇶
طيران حربي مجهول يحلق في سماء محافظات العراقية.</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/naya_foriraq/87726" target="_blank">📅 22:01 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87725">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e936a851a.mp4?token=aSSUuQ-yA9dtiJo4laKCjLw-w2b0ax01WrgNgD3KngkCCfP1I6yLYo4-Wp-s8mZaYdgHgTp08NE15q5aT3xncMJQLFzoVG92WINdB3-sxjdk7YZplZBW9y-wnohUSCX5jYKvnSA1U29x9YIP-Ke6CIaTKrYGmWTWFpsC85zKe3lfJx4k-iyqsPYpcVgZ5SSHOThwBmNTPymi-PC1Yx-ZB6yZlxgBT4B0gj7nrJR7dQDyE-EhTCKqZz1nSdfW58PTigFRTbIxV9Ad6N3It_uk-R5D3QU5sbcBw1WgELSghOtD3o7UUnvw5lGhuQCJ01kPVCZAIOYpgcJNaXEXzwRIvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e936a851a.mp4?token=aSSUuQ-yA9dtiJo4laKCjLw-w2b0ax01WrgNgD3KngkCCfP1I6yLYo4-Wp-s8mZaYdgHgTp08NE15q5aT3xncMJQLFzoVG92WINdB3-sxjdk7YZplZBW9y-wnohUSCX5jYKvnSA1U29x9YIP-Ke6CIaTKrYGmWTWFpsC85zKe3lfJx4k-iyqsPYpcVgZ5SSHOThwBmNTPymi-PC1Yx-ZB6yZlxgBT4B0gj7nrJR7dQDyE-EhTCKqZz1nSdfW58PTigFRTbIxV9Ad6N3It_uk-R5D3QU5sbcBw1WgELSghOtD3o7UUnvw5lGhuQCJ01kPVCZAIOYpgcJNaXEXzwRIvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇾🇪
مشاهد لصواريخ الباليستية التي تم اطلاقها من قبل انصار الله نحو الاهداف الحيوية في مناطق تمركز عصابات السعودية في اليمن.</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/naya_foriraq/87725" target="_blank">📅 21:41 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87724">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ms0dRtZE4s666_OD3VmXtORAqPWn-XOx-fHcffTdZv3lklGF1Xq4W31fPthvQ1c-47bCupG68BKNufad3rBir8i8P1-5ccL6RInlPIMaBw1a53CJlFzmGqYjVfwmGRrhGnGT6mcsQ2icYQTE3uImgRhHgvd59PjRSk5fHqR3pGkDU37vLQHBOVtV9lPmt0IwTTqzePeB0Yah17s0UO8JLxI13FFK3MNHcb5xZV62z5OubdjvKk8ceQ0_EOY2NtWn88wwedXo6sCfbKY2Zak4bDsUgRX_sA9cM9d1genRVgSC-QtWk_Cm1BrqxZCQPa7qebtyn4biUujWtlN61C7Uow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇾🇪
انصار الله يستهدفون منشأة حيوية بالحريقية قرب باب المندب بصاروخين باليستيين.</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/naya_foriraq/87724" target="_blank">📅 21:33 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87723">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vodx0iV8xBnUICUlb1XPzYdU3fzKUBXbFsCfWfFmvys5-X3r-i3jQgebIU3PDf5t891MDpU_MCYuaJukDKMgxonIIePKlKZJ3ptpBIqr_OaUSByzcU9ivVqza0S6G4Yqz7wbhmo6lz8dnJe-uXyxy_1LfhbHYelImt7oaKs07lsVO-ba3df6MyY6Fnh4r2dhlEjYPzRB99YL-w4wwH5Jl46rebqlaEczIbm3AGigpB_PC4DgHuAxekMqHiczbCpPFN3uGinF00xzoLmqpFCBhF3nG9HaUvvYv3SCzYv-6KC2ZMIn1vHXl5-f6gTqBEa4IvQnQjQk4mU0oWd_AsZEFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
تخوف جماهيري من عودة مضافات ولاية جنوب بغداد
حملة إعلامية مدعومة من دول إقليمية دعمت ظهور داعش إبان أعوام ٢٠١٤ تطالب بعود تسليم جرف النصر شمال بابل بيد الدواعش .</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/naya_foriraq/87723" target="_blank">📅 21:32 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87722">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rdFmbF5xQdl-pbmyI5JPEVoL_ovGu7tbkPnwahCWNhyFyRYLzfqvZCPxujw--Z37diPkXWGIR4XyGFDBS46fd7UaV_lLtgu5WrfyX_eDOCcRd-R2ZXOzAYLWbtV8majlAMtckxgDgRlN9UNNvUedJ13m8ybrqy_JVa0ocWkB4G9NVFKT5ga7_qHZDRXzIbGZlupWhXUQgwIWfXhL9CDGagX6MHMYQKrcfNlkPzV3RWdYCnqLUwS3AjdDsCejV84uffl-wlkrHK9n0M1Azua0erm2eYvbzyFzvsTLHULd2lOQtGPHa2kpEKHmbW16T6e3_xs9w5kDVMZeGUZHdO7FvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇾🇪
انصار الله يستهدفون منشأة حيوية بالحريقية قرب باب المندب بصاروخين باليستيين.</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/naya_foriraq/87722" target="_blank">📅 21:24 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87721">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🇾🇪
انصار الله يستهدفون منشأة حيوية بالحريقية قرب باب المندب بصاروخين باليستيين.</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/naya_foriraq/87721" target="_blank">📅 21:22 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87720">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🇮🇱
‏
الاعلام العبري:
قائد سنتكوم أبلغ إسرائيل أن واشنطن قد تضطر لاستئناف الحرب "إذا لم يكن لديها خيار.</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/naya_foriraq/87720" target="_blank">📅 21:13 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87719">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ee43d192c.mp4?token=aMqWSuGFkD-yiAdPpPclS7nuwAsbvu92rnvZdTb_RIbZPe4Ya0zomOuXGbWecNahvXkNvpikoE-bGAa1GFtQmS0EwaCpOFk9tlirjgIG0Y2MngITRJb0QraZLXXB_vcl5nDLKSKLLdAM30QPVa7EQg8oW3eDpbVpDC4WD3Q_97bzMy-MCFI-AUbyfAtrBBmR2dFtEZp7Elo-nr-SFvBcbTgouTuxXC2uVrM4L3iXufuQpqoU-WDXE6FeDLxj7iB5E_7mkFAHmZSLap4wG0DQ0yD9pcTCpYlq2R3p9PVPzJd5z1Fop9Nz1sTuWxqNHPi1M3_myqX7QS_tHYkST4Mbnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ee43d192c.mp4?token=aMqWSuGFkD-yiAdPpPclS7nuwAsbvu92rnvZdTb_RIbZPe4Ya0zomOuXGbWecNahvXkNvpikoE-bGAa1GFtQmS0EwaCpOFk9tlirjgIG0Y2MngITRJb0QraZLXXB_vcl5nDLKSKLLdAM30QPVa7EQg8oW3eDpbVpDC4WD3Q_97bzMy-MCFI-AUbyfAtrBBmR2dFtEZp7Elo-nr-SFvBcbTgouTuxXC2uVrM4L3iXufuQpqoU-WDXE6FeDLxj7iB5E_7mkFAHmZSLap4wG0DQ0yD9pcTCpYlq2R3p9PVPzJd5z1Fop9Nz1sTuWxqNHPi1M3_myqX7QS_tHYkST4Mbnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
🔻
السلاح الذي حرر امرلي والجرف وسامراء و بلد وصلاح الدين والأنبار حينما هرب الآخرين هو الحصن المنيع للشعب العراقي بوجه اي مخطط خارجي يستهدف الأمة العراقية ..</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/naya_foriraq/87719" target="_blank">📅 20:43 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87718">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🇮🇶
الناطق باسم القائد العام صباح النعمان:
رئيس الوزراء العراقي وجه بإنشاء صندوق لتطوير الدفاع الجوي العراقي.</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/naya_foriraq/87718" target="_blank">📅 20:42 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87717">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🇺🇸
سنتكوم
: إنشاء أول قوة مهام متعددة المجالات ومتعددة الجنسيات للطائرات المسيّرة الهجومية.</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/naya_foriraq/87717" target="_blank">📅 20:17 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87716">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bdJopgIvBvhsD7SAtMMD6TfLlQaVXmgIJ_-AjCGWkOONJkZLe4sg28wksx4qlhQm5Hn-Qsp-0TppmBqe9ctl1Dfsrn-a2BXs6HMyDMhQ23ZxoLcpOBHL81fzc8sh5bjKmQ5cTO51dqcbFuP8XTy8qgc6xAX0Lbly7HGQ-wUMQ6_ibIevLRWssX9BQ9tIpG_nfDZNhA4Su0xe1PmGmK_11pnuod3M47jD3aniyKfB4NMn3NaxmU0hQpIDZ-23_EetYzohddVjiXyQ7Ae8BxNufdwDGPaEonm0l-Lcz-801LQRlhkmaPGH8B80ZKXa-92gcva7vOGRmoY4EBE8OT17WA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الحضور الإعلامي للمتحدث باسم المقرّ المركزي لخاتم الأنبياء، مع ميدالية تحمل الاسم المبارك للإمام الرضا عليه السلام.</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/naya_foriraq/87716" target="_blank">📅 20:01 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87715">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🇮🇶
أعلنَ مكتبُ سماحة السيد السيستاني (دام ظلّه) في النجف الأشرف أن يوم غدٍ الجمعة هو المكمّل لشهر صفر ، ويوم السبت الموافق  (١٥-٨-٢٠٢٦ م) هو الأول من شهر ربيع الاول لعام ١٤٤٨ للهجرة.</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/naya_foriraq/87715" target="_blank">📅 19:54 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87713">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🇸🇦
‏
وزير الدفاع السعودي:
العراق سيبقى جارا عزيزا تربطنا بحكومته وشعبه روابط الأخوة والتضامن.</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/naya_foriraq/87713" target="_blank">📅 19:45 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87712">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L_nHU2AZttpyqcNfdnUK2PM4SSXAJ3SUs951Z1BZkMkrYMPhWWsRAX31Bq1YX9-mTKvyEGWaPyfI7poRKVQkt-Kp3u8DoOA3F86-3EsyA_tDfEKdK4p6VHGU1sbFeDSwtdo1B0rvnuTgNZB8PDtw9dA2vpIkIcbnba9vYQlsCmBkt6WapdjTirE2erC0mZNLb4VvS7Ng8l47QBaBwtr6_LtF4FFeFAGsbRKinRQliiBfqXZ7VZXh5xdgZfG2ZTDGXJfseBMeBaBKZUS9G2TAi4HznGNSAcrUO6_D1VJ10uW6_fFiB-eBLdjTD-VAtkAGswX_ONYWgnRpgM2dZdBCCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
الاعلام الاميركي:
الجيش فقد 45 مسيرة إم كيو 9 في الحرب مع إيران ما يعادل نحو 25 % من أسطوله.</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/naya_foriraq/87712" target="_blank">📅 19:28 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87711">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🇾🇪
🇸🇦
نتيجة الهجمات التي تشنها القوات اليمنية.. السعودية تستمر في إغلاق مطارات جيزان ونجران وأبها حتى إشعار أخر.</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/naya_foriraq/87711" target="_blank">📅 18:41 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87710">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/naya_foriraq/87710" target="_blank">📅 18:23 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87709">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/naya_foriraq/87709" target="_blank">📅 18:21 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87708">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🇺🇸
‏ كبير الديمقراطيين في مجلس الشيوخ لشؤون القوات المسلحة السيناتور جاك ريد يدعو وزير الحرب بيت هيغسيث للإدلاء بشهادته أمام الكونجرس بشأن حوادث سقوط ضحايا مدنيين جماعيين ناجمة عن الضربات الأمريكية في اليمن وإيران (مدرسة ميناب للبنات).
‏
يلقي ريد باللوم على قيادة هيغسيث في هذه الحوادث، ويتهم وزارة الحرب بتأخير تقرير الشؤون المدنية اليمنية لأشهر ولم تقدم حتى الآن بياناً منفصلاً عن ضرب مدرسة ميناب</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/naya_foriraq/87708" target="_blank">📅 18:15 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87707">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rVY9i7kgdOzosCPyh2tJ6fghCmgMhlbtuy90IiRNyr_3Jp1S0uVkjVDurfRwc4mYKcjnZPI_9H8Xobc0tL6BSjg2NfVH3yViie62Wepg27cyjnn1voeLsvFJQ31wJaS8J7jVD-4ZUOcGCpSPhky3qmElCe-DH520fRPRuLwOrUlPbCqqrGbWD4B1JASJOho9qERh5FF3gJ6Y1Xz4LPqYX1Ntg5VXr_LksDb5IFcsjCE3hcVt5Zr4nenOUkt5liFKbMweMkJDan3lt6k2Kap80YmHNFkbDvT0UjTBsis5n2Soto3rdmODlNMtMwU8ZoF4laG2gfA-VKsrOb9nGb1zQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قادمة من سوريا.. العراق يحبط محاولة تهريب (45) ألف حبة مخدرة كانت في طريقها للترويج داخل البلاد</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/naya_foriraq/87707" target="_blank">📅 18:04 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87706">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">لحظة إنفجار كدس عتاد في كوليفررو جنوب روما الايطالية</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/naya_foriraq/87706" target="_blank">📅 18:03 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87705">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mqgFeiWJVxIavZGChdfRFgrYbqL7hiHrNwnfrWvryYFdFyiI9PAacXGE8-_dq6tq_sLNTUPkiJk71U4d-FyoGchQFj4upJJuu9hg2sR-6C012go3Jr-RrXD3ps7ZZ67Z7PY9kEGsDugYONAPADnKaXRLYSKiiKYkgKcl1t7k3hpv9LdEQcDiK3WmurXUc-Ctgrek3xqrXEoz-9qc97H5asBWWgqcvIyCPY-1ikAAwI5H1PA6zQ4ESztia7I_l43MK7ekXGfmuJO_OGQHDMQqIBDbFDDam0pZTmjBbJ8xStUQxAoZGJJYn0nkzGC5O7pC-Q2jeMATzA46jFGJuT0OAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ملك السعودية المرحوم سلمان بن عبد العزيز يعفي نفسه من رئاسة مجلس الوزراء ويكلف محمد بن سلمان برئاسة المجلس</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/naya_foriraq/87705" target="_blank">📅 17:16 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87704">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">السعودية تقرر اغلاق (‏مطار أبها الدولي - مطار جازان الدولي - مطار نجران الدولي)</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/naya_foriraq/87704" target="_blank">📅 16:59 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87703">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">ملك السعودية
المرحوم
سلمان بن عبد العزيز يعفي نفسه من رئاسة مجلس الوزراء ويكلف محمد بن سلمان برئاسة المجلس</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/naya_foriraq/87703" target="_blank">📅 16:46 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87702">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">بيان مرتقب للسيد القائد عبدالملك بدرالدين الحوثي حول الإساءة الأمريكية للقرآن الكريم</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/naya_foriraq/87702" target="_blank">📅 15:50 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87701">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/43381c63c7.mp4?token=DHUTXEIPDL4kKY_JoVA3CM_qRyRBzeRaSt8M3UZ0UNbFmUmRlLXczuaHhpPH-lVK3LkKG56c2oWy_1Q-uCZek7yZrqnMPj6MQ8SwcP9whmXMdPpwwWAwKSRen0IPlTpt5KRKp6wNuQsM-ZjE9dZdCulx_BFn8clLnPH54XqPuqww_YJVp0U7BB47y-34iUMs7KV6DQe_7Rpwy6DjZVNy8OV426xk3NL9H1xxy7zeUVNnBueh8SA-njv7TjlPV6Ql4_z3WO3ER6lUNBhGnFbHpIxPXSPYC9z02Jels3BlWD6LzD9MTzvJ7uR6UxETbPw1Ri6nLDpw3vdTgypemiBHZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/43381c63c7.mp4?token=DHUTXEIPDL4kKY_JoVA3CM_qRyRBzeRaSt8M3UZ0UNbFmUmRlLXczuaHhpPH-lVK3LkKG56c2oWy_1Q-uCZek7yZrqnMPj6MQ8SwcP9whmXMdPpwwWAwKSRen0IPlTpt5KRKp6wNuQsM-ZjE9dZdCulx_BFn8clLnPH54XqPuqww_YJVp0U7BB47y-34iUMs7KV6DQe_7Rpwy6DjZVNy8OV426xk3NL9H1xxy7zeUVNnBueh8SA-njv7TjlPV6Ql4_z3WO3ER6lUNBhGnFbHpIxPXSPYC9z02Jels3BlWD6LzD9MTzvJ7uR6UxETbPw1Ri6nLDpw3vdTgypemiBHZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الهندي اللي يكضي الفلم يتمرن بالجم حتى يواجه خصومه وتالي ينضرب بمسيرة</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/naya_foriraq/87701" target="_blank">📅 15:48 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87700">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">‏هجوم لانصار الله بالمسيّرات على مواقع مرتزقة السعودية بمنطقة العبر في حضرموت</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/naya_foriraq/87700" target="_blank">📅 15:43 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87699">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🇮🇶
🔻
هيئة الحشد الشعبي:
تودّ هيئة الحشد الشعبي أن توضح للرأي العام، وللمهتمين، ولمجاهديها الأبطال، أن الجرحى من منتسبي الهيئة قد استوفوا حقوقهم المستحقة ضمن صلاحيات الهيئة، وبنسبة شبه كاملة، سواءً ما يتعلق بالرواتب أو العلاج داخل العراق وخارجه، وذلك من خلال الجهات المختصة في هيئة الحشد الشعبي.
أما الاعتصام القائم هذه الأيام أمام دائرة التقاعد العامة، فإنه يتعلق بملف منفصل عن حقوق الجرحى لدى الهيئة، ويتمثل بالمطالبة بتطبيق أحكام قانون مؤسسة الشهداء رقم (57) المعدل لسنة 2020، ولا سيما الفقرة (ثانيًا)، التي أجازت الجمع بين الراتب التقاعدي وراتب الإصابة، أسوةً بأقرانهم في بعض المؤسسات الأمنية.
وتؤكد الهيئة أن هذا الملف لا يدخل ضمن صلاحياتها القانونية أو الإدارية، وإنما يقع ضمن اختصاص وزارة المالية وهيئة التقاعد الوطنية، باعتبارهما الجهتين المعنيتين بتنفيذ الأحكام القانونية الخاصة بهذا الاستحقاق.
ومع ذلك، وانطلاقًا من مسؤوليتها تجاه مجاهديها، تواصل قيادة هيئة الحشد الشعبي تنسيقها واتصالاتها مع الجهات المختصة، بهدف الإسهام في معالجة هذا الملف، والوصول إلى حل يضمن حقوق الجرحى وفقًا للقانون.</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/naya_foriraq/87699" target="_blank">📅 15:41 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87698">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🇮🇷
مقر خاتم الأنبياء المركزي:
الادعاءات الأمريكية الزائفة حول حركة السفن الاعتيادية عبر مضيق هرمز، والتي تعكس اليأس والعجز للجيش في ذلك البلد، ليست سوى أكاذيب.
نعلن أن مضيق هرمز، كما هو الحال دائمًا، يخضع للإدارة والسيطرة الكاملة للجمهورية الإسلامية الإيرانية، ولا يمكن لأي سفينة تجارية أو ناقلة نفط العبور بأمان عبر هذا المضيق دون إذن ومراقبة القوات المسلحة الإيرانية القوية، ولن يتمكنوا من ذلك.</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/naya_foriraq/87698" target="_blank">📅 15:39 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87697">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/naya_foriraq/87697" target="_blank">📅 15:35 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87696">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/naya_foriraq/87696" target="_blank">📅 15:35 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87695">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">‏رئيس وزراء السلطة اللبنانية نواف سلام يغرد: تم اختراق حسابي وحذف التغريدة</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/naya_foriraq/87695" target="_blank">📅 15:34 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87694">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">مجلس النواب العراقي يؤجل النظر في الطعون المقدمة بشأن صحة عضوية بعض النواب إلى جلساته المقبلة لعدم تحقق نصاب ثلثي أعضاء البرلمان</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/naya_foriraq/87694" target="_blank">📅 15:22 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87693">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">رئيس وزراء السلطة اللبنانية يحذف تغريدة له ادان فيها الغارات الصهيونية على لبنان</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/naya_foriraq/87693" target="_blank">📅 15:21 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87692">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">رئيس وزراء السلطة اللبنانية يحذف تغريدة له ادان فيها الغارات الصهيونية على لبنان</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/naya_foriraq/87692" target="_blank">📅 15:21 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87691">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🇳🇱
الشرطة الهولندية:
قتيل ومصابون في انفجار بميناء روتردام.</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/naya_foriraq/87691" target="_blank">📅 15:10 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87690">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🇮🇶
ريبوار رحمن صالح يؤدي اليمين الدستورية نائباً في مجلس النواب العراقي.</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/naya_foriraq/87690" target="_blank">📅 15:07 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87689">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1d0499f575.mp4?token=LAxc1XYIArahg5OBNCJlHiIP4uKxfe28JeGuOCXm72_o25cgzzcRGShwRyc8uyhGWaCk1WLf8phMbwuvc_YkR_MaoBRoihWPnxnlHamesxia0PcleHWgZdQ8yELmEQ_nJMUwwbUpf7Hul4-UbzBvNcg6h-FEEM6_sx5HVyG8_TBw49mTs_iTksDbP-J48rpWf1ZstZvzP3ro-F91l1d2atwOURWmbl96TBdo39vRNAxbTsPe6YvdeqFtSoEAy_7C4K3xwYw9l_j39kEe7sMgx-LrFyDClFGsWQNcA0VpChpi9YsXdsQUlnOgsMgnw2b-lW_EImCfShdw2X02XgZiazzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1d0499f575.mp4?token=LAxc1XYIArahg5OBNCJlHiIP4uKxfe28JeGuOCXm72_o25cgzzcRGShwRyc8uyhGWaCk1WLf8phMbwuvc_YkR_MaoBRoihWPnxnlHamesxia0PcleHWgZdQ8yELmEQ_nJMUwwbUpf7Hul4-UbzBvNcg6h-FEEM6_sx5HVyG8_TBw49mTs_iTksDbP-J48rpWf1ZstZvzP3ro-F91l1d2atwOURWmbl96TBdo39vRNAxbTsPe6YvdeqFtSoEAy_7C4K3xwYw9l_j39kEe7sMgx-LrFyDClFGsWQNcA0VpChpi9YsXdsQUlnOgsMgnw2b-lW_EImCfShdw2X02XgZiazzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
الناطق باسم وزارة الدفاع العراقية ينفي انسحاب الجيش العراقي من النقاط العسكرية بين طوزخورماتو وكركوك مؤكدا ان ما جرى هو إعادة انتشار وتبديل ومناورة للقطعات العسكرية إلى جانب تعزيز بعض المواقع بقطعات إضافية ضمن الخطط والإجراءات العسكرية المعتمدة.</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/naya_foriraq/87689" target="_blank">📅 15:02 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87688">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">اوكرانيا تزعم استهداف مطار ساكي ومنصات إطلاق المسيرات في شبه جزيرة القرم</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/naya_foriraq/87688" target="_blank">📅 14:57 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87687">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XY1urEtRxwutxz7K3mR92hzccqKpk17ddeSDEQUfPTCvzzOtK3GoZH5Tyom8wJPhxkyVl7-ms8CaQ3YIOrqtqDrCkVN56voMDhmMtnDW4eMk1Q-TQAiOQ5_S05IU0iguOIUAr3XbnL5wggKD1wBrDKqVIUIDBVjRe4kJI2MiS5nGpoxgXVk0KQOgvZztAf0nr6Zto6owrzoWtUSjEKKUJqR-UjUFxbJjmH0D5shp-ogfLTVNR2F4NUmXSkO_cpv0TYGLm8LYZOayWGmUaIKxZkRGKCDNxnZwHqdPgBESrQU_WLOHE15NXXNF5LRqVjfDNJK_nSCVlOLNUJXcelXqgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">أمين عام كتائب سيد الشهداء في العراق يشارك جرحى الحشد الشعبي مظاهراتهم امام دائرة التقاعد بعد اعتصامهم لمدة ثلاثة ايام دون إصغاء من الجهات ذات العلاقة.</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/naya_foriraq/87687" target="_blank">📅 14:51 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87686">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EF5OHCqwtteTg3j5wKRGe8p6_XQk8UnF1R5AYI2FlSpsECxFZnTWCK61VDYA4s5XwFhAGK02TVNyr8uTbeHvZJeDYy57ChLi2X_Dm9D6cpLDTygqE2Rb023ft0kdcXc_mjGKsXASHLTtQ-IcbRYEe9Ut_2-eUs0uEMBDxHntHzl0jLbAhU_e937dgqlJWMwP2kfyW-_6GQwPnpBiKrD4Qcp28VEIkLiOMqtiENuXxBKST2ufn9fOl81cai93i33WyvpGG5y3VksZjgEqiBI9xbr-sidynmLQ3sfabrBqoYMjBCBT5AG4UlmwRNZwcszVVhHj2yu5iizPHSOU29j5_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
رئيس مجلس القضاء الاعلى العراقي القاضي فائق زيدان يلتقي وزير العدل السوري.</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/naya_foriraq/87686" target="_blank">📅 14:40 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87684">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🇮🇶
الناطق باسم وزارة الدفاع العراقية ينفي انسحاب الجيش العراقي من النقاط العسكرية بين طوزخورماتو وكركوك مؤكدا ان ما جرى هو إعادة انتشار وتبديل ومناورة للقطعات العسكرية إلى جانب تعزيز بعض المواقع بقطعات إضافية ضمن الخطط والإجراءات العسكرية المعتمدة.</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/naya_foriraq/87684" target="_blank">📅 14:32 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87683">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🇮🇱
اعلام العدو:
في إطار الجهود لدعم استعداد الجيش الإسرائيلي لمواجهة جميع السيناريوهات: آلاف الأطنان من المعدات العسكرية وصلت إلى "إسرائيل".
أكملت وزارة الحرب استلام وتفريغ سفينة شحن أخرى في ميناء حيفا، كانت تحمل آلاف الأطنان من المعدات العسكرية ووسائل القتال.
تشمل الشحنة، من بين أمور أخرى: جرافات D9 ضرورية، ومركبات هامر، ومركبات مدرعة من طراز JLTV، وشاحنات من طراز أوشكوش، ومعدات أخرى كثيرة.</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/naya_foriraq/87683" target="_blank">📅 14:21 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87682">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🇮🇱
نتن ياهو:
يمكنكم أن تسموا بريطانيا بـ "الجمهورية الإسلامية لبريطانيا". قال أحدهم إن أول جمهورية إسلامية تمتلك أسلحة نووية ستكون "الجمهورية الإسلامية لبريطانيا". نحن نتأكد من ألا تحدث أخرى - تعرفون، في إيران.</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/naya_foriraq/87682" target="_blank">📅 14:13 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87681">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🇺🇦
زيلينسكي:
هذا العام، لدينا أقل بنسبة ثلاثة أضعاف ونصف من عدد الصواريخ الاعتراضية التي كانت لدينا في عام 2025. روسيا لديها الآن ضعف عدد الصواريخ الباليستية شهريًا مقارنة بما كانت عليه من قبل. إذا باعت الولايات المتحدة لنا 5٪، فسنتمكن من تجاوز فصل الشتاء وإنقاذ حياة الناس. وإذا تمكنت من بيع لنا 10٪ فسنتمكن من تدمير جميع الصواريخ الباليستية الروسية حاليًا، لدي 1٪.</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/naya_foriraq/87681" target="_blank">📅 13:51 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87680">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🇮🇶
وكالات: الوفد سيترأسه مدير مكتب القائد العام للقوات المسلحة الفريق أول ركن عبد الأمير الشمري ورئيس جهاز المخابرات حميد الشطري.</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/naya_foriraq/87680" target="_blank">📅 13:15 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87679">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🇮🇶
شركة تسويق النفط العراقية:
شركة طاقة رائدة في أبوظبي من بين الجهات التي تشتري النفط الخام العراقي وتنقل شحناته عبر مضيق هرمز.</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/naya_foriraq/87679" target="_blank">📅 13:07 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87678">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🇮🇱
وزير الحرب الصهيوني كاتس:
نخرّب منازل اللبنانيين في الجنوب ونبني الاستيطان في الضفة</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/naya_foriraq/87678" target="_blank">📅 13:04 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87677">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🇺🇸
اعلام خليجي:
واشنطن رفعت وتيرة الأرتال المنسحبة من إقليم كردستان العراق تجاه دول الجوار.</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/naya_foriraq/87677" target="_blank">📅 13:00 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87676">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🇾🇪
🇸🇦
إعلام سعودي: ‏اشتباك بحري بين زوارق سعودية وزوارق أنصار الله في الساحل الغربي في اليمن.</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/naya_foriraq/87676" target="_blank">📅 12:01 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87675">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/En2dQscWNucTAMqnkgy4D8xEfuIxcCRjiuvROvcrs4VqK2VgTygdSRZzEcg2LYvwyKUiMEf2d7_NrM24gqhfRUhTV6v21hDcXw3pNqqp6Ki8WAyri8nADF3gUuvPDrVvgXxO4FcjXtZGGllejt8Wcsfo8DgjBPxzdU41hA4N7CtTf9NBM0bFcCzVv5Y3uJgH2uiecV3LCzQMh0u1FxalHEOJ5bdD_d0v40YU60SyVYz2TvdBYuX84uRJmZE0N_ResgbZD6urj5oLz2VdCRvicYnD1EtfrTdx98ggSnH---d6KrJZEUU8JZSTHLTJGACI4QKxPW1Gw_V67RO14Ov8qQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
رئيس مجلس القضاء الاعلى العراقي القاضي فائق زيدان يلتقي وزير العدل السوري.</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/naya_foriraq/87675" target="_blank">📅 11:44 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87674">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dzPr6dm6WYfcP8zNYfNKyshLC35JWe_B7KDMcspXKIXfF338sscljIfxQ7YaTJcOzRthtEcFOglV4Lr-BSpQk0lPommqTAFA7oJnrXxME-q8sKs8fjsDiWAKIi0ENNJFbKgeIuiHSBy5eWNQoBhVDWLEPjwQuujripd_2bmkBTlBBh6O8AFaVSjVwlpn7IN9PvCO-ZPTtRJ3xf7_QI9xTu6eYNc2XuOwzqJRnSSnwnUsOamGuUsWhwEkRuVZ9u2LJJkqXvpeJS4W4z0pLr7AAFNkiXqfzMETWMz_2_8HMXWjFtNgNXsspe-gN9KxHMYy_LdyqtvPgPPBE8icb3Kn9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عراقجي:
لطالما أخطأت الولايات المتحدة في حساباتها بسبب قصور في الاستخبارات. خير مثال على ذلك: الحرب على إيران. والآن، خطأ أكبر في مضيق هرمز.
‏أسوأ من الأخبار الكاذبة هي المعلومات الاستخباراتية الزائفة. كن حذراً.
‏الله أكبر، أعظم من أي قوة على وجه الأرض. بالله نتوكل.</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/naya_foriraq/87674" target="_blank">📅 11:28 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87672">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">أمبري للأمن البحري:
نشارك في عمليات إنقاذ ناقلة نفط منكوبة قبالة ساحل عمان وسفن الإنقاذ في طريقها إلى الموقع
أفراد متخصصون صعدوا إلى متن ناقلة النفط لتقييم الأوضاع</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/naya_foriraq/87672" target="_blank">📅 09:48 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87671">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hwlmPpvpLM-xadGv93962xFQ3s5M5pP1Z2OM9zVdLinsAAU6oQ4rWVbInLC-RcUoV9kfZT7rjGVtO9X45M4Gz3Suy5HoD7z3yH4yoF7cffLWpYcZ2lK1KvlQa7rLp5TBjhnW3JwYx6QOXTJL5lQwX9eol2KophscbcmPCKwEvZBgVJsZQ1oxLxLWBG1ng4zCeMOjETp2i3HtNqTKjGKqJikJraOZY7DbhGOPSDuWVDi82RA3x8ORWyo4zvXTO6WbNY2kbNOcZdsZs67-okpJsY3h-JEc3nEShqnI3x20dtgJ8MQVYSDY97UYA-3WGJ2gXq4u1jMmY56utGO-i44VTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇪
😎
بسبب القصف الإيراني مؤخراً الذي تسبب بهروب وفرار رجال الوطن الإماراتيين ؛ وزارة الدفاع الاماراتية تستعين بفتيات الإمارات وتدعوهن للالتحاق بالكليات العسكرية.</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/naya_foriraq/87671" target="_blank">📅 09:00 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87670">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🔻
هزة أرضية بقوة 4,7 على مقياس ريختر تضرب الحدود العراقية السورية.</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/naya_foriraq/87670" target="_blank">📅 08:54 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87669">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🔻
عصابات الجولاني تطلق قذائف الهاون ورمي بالأسلحة الثقيلة على الحدود السورية اللبنانية بذريعة التدريبات العسكرية.</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/naya_foriraq/87669" target="_blank">📅 08:40 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87668">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mj7flQl4iWLlv-Kws7h8rUEyLP17dnvy40Gv97k7sUJpJP-ETV9jGSaOTYyEdXWlvMULbjHrjUXYcQQ6LmNQK5YcJW5-HwSpUnIO3r19_sAsYXhBZFNaauBu1s_TPTdHh5Nb7soT2ToVv86LBTEGXZfmygI0by2sTQnVeazvYv6ajM8Cw6PaYAhHjiV_SJNwaVbtAwwqOAPstrcPJg0NInkx8AYXVUu70mZHU0koTkLPFSKwvKDX68je_ABRZZfZi_ahBhdwFVjevdnhcHJc9DqIzx2moRoZnCDhtIi53ZSWunux7wphjvg21r4dzt-Blh6x48siYag2m3JKSRRkpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
عراقجي:
دول مثل فرنسا يجب أن تتوقف عن إلقاء المواعظ على العالم بشأن "حقوق الإنسان" والقوانين الدولية. هذا نفاق واضح ومخزي. دعمكم للإبادة الجماعية التي ترتكبها إسرائيل في غزة، والهجمات العدوانية على إيران، قد قضى على أي اعتبار أخلاقي كنتم تتصورون أنكم تتمتعون به.</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/naya_foriraq/87668" target="_blank">📅 06:12 · 22 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
