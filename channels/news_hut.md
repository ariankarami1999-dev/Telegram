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
<img src="https://cdn4.telesco.pe/file/s5lKNLKN_QUChbChMKQrt6y_rMJIgKRsieIlWeXi1R2DVBGMU_baC25V12IJ6GLOMgfAui7Vo2kNXjOMBMGupdKDFpmSM6z3GFYegW8tBoTMyyZx0KvtyP1FxBq1temqZ7Leo6na8bOG4sduRPXwFCkxpZm08nQQRpUbOZ13rXhfvGUHWXHwt0PW4j5DhJUw35ezan5SHlBtAloeH3vWq3nYMbYKLbvlGZNMT01v4fl5E4vPRMzAKrtAEHLOSSAqy_c_PPj_7aEmD_HuC0HYCzQOa2jVPL5CHB3sGNukvIgkkkloTG-pMgH0eMuWfKhNmPxg7ENvoC_UM3v3aTKsyA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 140K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-09 01:08:36</div>
<hr>

<div class="tg-post" id="msg-69279">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V-jgn4McnGbfkKBqgKnfRKvH0aLELVdkQLtZ-FX3x0IWzLhlqwFq6v_ue7JEEgEvyLaN8Hs3SnUkUqhcd58I1U89XebJtKgEThqXHdY41QyXh7x7dV_OkPvDEosuqA4T7uyHRVBtdpllzWn975-bTZx7DR29-iw_MSbYA_kbIT3qvX1q5ytWNoqAeW-bMXIppm7u_vn4zi4WPGEs1_D51T1h-cZ1toaGDXalYBk9S7HHPl4KX7lNSNIhIg0iW6c-M-6lkh7K96zJIre0pWyDySHC5nvTPdjku0TAOlY3vFGACLe_h8yDYBV8dFJb9-6pqZ9pVSSO7TVHXZ51U01kRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
قالیباف:
«آمریکا هر روز یه جنایت جدید انجام میده. حمله به خونه‌های مردم عادی توی جزیره قشم، ادامه همون جنایت‌هاییه که قبلاً توی لبنان و غزه انجام داده.
آمریکایی‌ها عادت دارن هر وقت توی میدان نبرد کم میارن، با ریختن خون آدم‌های بی‌گناه جبرانش کنن.
ولی بابت این کارشون، تاوان پس میدن.
@News_Hut</div>
<div class="tg-footer">👁️ 2.8K · <a href="https://t.me/news_hut/69279" target="_blank">📅 00:58 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69278">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cba260d124.mp4?token=ZjXp0E8KdO1mmPySwHypSWf1r6RYcz2i7GfCf0uQgy4eYWMKzeq0UEhVcMHdgpj16KlX3t3MScoZB_3C1UECdWFpGR8et2AdsroxQNc0tvelP27-ATIucuxtY1P1-CBMndEaxevsuLy-2ZnemH2CDy2ztHEyoKRw6kcuLJjAhzapdndt-zp5L1pyys87q-yrb4OnsEG9-5Il7U5gRGyf1Xo3lnzc0ns-b0Lh-waJ6NFZOUm40ies__UxbYZCFY-DjgtV-iJzCNlxJUYU-rNUKfL7vSYQhJL-2-Cybl3ytAQxRrcJsk376UDxA14Xb4Jp_3-ULnFThgOeSo9UokOAFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cba260d124.mp4?token=ZjXp0E8KdO1mmPySwHypSWf1r6RYcz2i7GfCf0uQgy4eYWMKzeq0UEhVcMHdgpj16KlX3t3MScoZB_3C1UECdWFpGR8et2AdsroxQNc0tvelP27-ATIucuxtY1P1-CBMndEaxevsuLy-2ZnemH2CDy2ztHEyoKRw6kcuLJjAhzapdndt-zp5L1pyys87q-yrb4OnsEG9-5Il7U5gRGyf1Xo3lnzc0ns-b0Lh-waJ6NFZOUm40ies__UxbYZCFY-DjgtV-iJzCNlxJUYU-rNUKfL7vSYQhJL-2-Cybl3ytAQxRrcJsk376UDxA14Xb4Jp_3-ULnFThgOeSo9UokOAFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
سنتکام:
یک فروند هواپیمای P-8 Poseidon(هواپیمای شناسایی تخصصی) نیروی دریایی ایالات متحده در حین گشت‌زنی در خاورمیانه، برای سوخت‌گیری به یک فروند هواپیمای KC-135 Stratotanker نیروی هوایی ایالات متحده نزدیک می‌شود.
@News_Hut</div>
<div class="tg-footer">👁️ 7.51K · <a href="https://t.me/news_hut/69278" target="_blank">📅 00:25 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69277">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QUEJnDH9HXr0cieQHnodAj_9-BeXy74jdBGw3-4N5KjIkYN_yhL1XjhLr-zQRuJi2iHnzki6q5CvdBIqnKDBnzhtTtRIR-6xxHqfQfLOBD207ftCAiM-NgcW2s2c-QwmHK0soYcJmap0A0kn1VyBa4yBqsI8Gemf0oqSF-q13VLie2PH-P3OA23S_4pObzx_4_1N8MdV9l2_cbi74bR9mdwEpO7u9ar5f6JGoZ06nWHX1tk3wZI9ZQur9_DRVvts_3LqIaeJRd7KQnnzP8heE0-dcvUIg3Cpn9unR3Z8JvgMlRrRUCD9j0H0lm4nX1G56-Dun-oCafeDNmh4LkYBJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
آی‌24نیوز:
اسرائیل کاتس، وزیر دفاع اسرائیل، روز پنج‌شنبه به همراه ایال زامیر، رئیس ستاد کل ارتش، جلسه‌ای برای ارزیابی وضعیت امنیتی برگزار کرد.
در این جلسه، تصویری از وضعیت اطلاعاتی و عملیاتی، سطح آمادگی ارتش و طرح‌های عملیاتی برای سناریوهای گوناگون در عرصه‌های مختلف به کاتس ارائه شد.
@News_Hut</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/news_hut/69277" target="_blank">📅 23:54 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69276">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/89da715482.mp4?token=MizoIJkJDFPq5VVsjSDHPZTgzZUzNt_UeddQPb7MnKPWyFyc10-SJ0MxHCFHunORBi8oLjhYxAFXmz_FEpsExPNMgbbV-YA2bfGvJyXbh1f5NOss-joIbHcVaBxBeHLQ0eFLrtcIM5_b7Wrh1_lQp2rl3ATKEh2ZwSF92eQn_skgzr8xdqsT7gg86au29WzmpvD-bFigEslbYDC_wCBxOgOQV1yEuHnz8KUN9BllTqhjvR06CI8wOX3YcuAlLzj77keog4sSuvjSRH_D9eNoL4bXmYrndWSXB98mCIzBrfIJ_3xCsBJcauWwsQmtIvzB8Apl_L3zhyhLj9KzA_BauQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/89da715482.mp4?token=MizoIJkJDFPq5VVsjSDHPZTgzZUzNt_UeddQPb7MnKPWyFyc10-SJ0MxHCFHunORBi8oLjhYxAFXmz_FEpsExPNMgbbV-YA2bfGvJyXbh1f5NOss-joIbHcVaBxBeHLQ0eFLrtcIM5_b7Wrh1_lQp2rl3ATKEh2ZwSF92eQn_skgzr8xdqsT7gg86au29WzmpvD-bFigEslbYDC_wCBxOgOQV1yEuHnz8KUN9BllTqhjvR06CI8wOX3YcuAlLzj77keog4sSuvjSRH_D9eNoL4bXmYrndWSXB98mCIzBrfIJ_3xCsBJcauWwsQmtIvzB8Apl_L3zhyhLj9KzA_BauQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
چند روز پیش یه پسر بچه به اسم امیرحسین رو آورده بودن صداوسیما که اینجوری جواب سوال مجریا رو داد
:
مجری:
منو عروسیت دعوت میکنی؟
امیرحسین:
معلومه که نه
مجری:
کارشناس برنامه، خانم دکتر رو چی؟
امیرحسین:
فرقی نداره، اونم نه.
مجری:
مامانت چی؟ اونو که دیگه دعوت میکنی؟
امیرحسین:
وقتی زن بگیرم مامانمو میخوام چیکار
@News_Hut</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/news_hut/69276" target="_blank">📅 23:40 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69275">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/671ccf87ea.mp4?token=E4JVqhuAe32Exf_E2nbTTHpxaSbBr2p-ZneLycmxxXwYZfNPf-uNPR4Cd1C8fSfkN6VfzPe-OZTI6vcEqhEyYiek1wOi8IJdrKqlXht3cfu9Ioi0IBTsGn7u4jRCjOn2wSSTaRnGJBnezs1QOh_YOR6DDnbie4I61g_YgV00aholN1u--f-mAakEa-WfUsBut9NCNv7ACjNlwqHwbX4mLy1G1QedpxiIKGbJ3fYuQfRDYzp8pPp0nL3CeI7KMYCqAQxPJAqQLZGgMup8wkNQwsvNlkHbw3j__RdT9lJwHNGoHYUJCNUioIKw7IXr2V1JDWpZk8yHTW0_inpOZidHxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/671ccf87ea.mp4?token=E4JVqhuAe32Exf_E2nbTTHpxaSbBr2p-ZneLycmxxXwYZfNPf-uNPR4Cd1C8fSfkN6VfzPe-OZTI6vcEqhEyYiek1wOi8IJdrKqlXht3cfu9Ioi0IBTsGn7u4jRCjOn2wSSTaRnGJBnezs1QOh_YOR6DDnbie4I61g_YgV00aholN1u--f-mAakEa-WfUsBut9NCNv7ACjNlwqHwbX4mLy1G1QedpxiIKGbJ3fYuQfRDYzp8pPp0nL3CeI7KMYCqAQxPJAqQLZGgMup8wkNQwsvNlkHbw3j__RdT9lJwHNGoHYUJCNUioIKw7IXr2V1JDWpZk8yHTW0_inpOZidHxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
نقدعلی، نماینده مجلس:
با وضعیت حجاب میخوایم چیکار کنیم؟ والله جوابی برای خدا نداریم.
یه نماینده مجلس به من گفت از درد بی‌حجابی هر شب تو خونه گریه میکنه و خواب و خوراک نداره
😂
@News_Hut</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/news_hut/69275" target="_blank">📅 23:15 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69274">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sbPsQsEVkNz9xGHFrVecsYFoobWugQwnqydtiVyE4i8wQy-nEtzORAikhRLOd-kqVBuGfvgIwzxo5PZxfZd8j0FHxOxDEBLLGoSEHxjj9BpGjLf6Kf-6bHJL5vd0Zx_SmvQeMhzWCj6tK_qOJF-EhBx-FssLtLqyRY5-1hA5CsyTjgbjGPWwwl7kMM8C8KCmTB5tYvnYakZFVdI_sPk43YvgjkCxNLEH9QOtE3RlHsmpAhON3URyV4aDFnIjNFLnmlugsF32Be67o7TCDcOVgCXGNQZ79SN2fNyZEsF7n8QXl5oj1QLpwRl_Yn2E6KQPgrqYInS1cYZvBInTTPk1-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اعدام می‌کنید؟ به‌به چه کتلت های تر و تازه‌ای داریم امشب  #hjAly</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/news_hut/69274" target="_blank">📅 23:04 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69273">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b3fe31b5c.mp4?token=ESpWshazxF0XtRX3D4ET_Y-o6KnPRpcblGphqvzGUvhVN2e0a3hyw6txk6Yc4H-NoCM4R2K599BaWxao6rhwASaBN3xq9h_IgwQXVbUguG0DFSFUuHJreeBCQOFMy3arFEkSqqelQrVrVDpPq4hpchb8gYCqfjyhnb5rZqmq6nbv2H9RACbkxnRoAz59YMLc_HO1v4IwFyKM8Y_KKPenrgcfcMlcb0txcnM-5HZpoGu4BYUtF1RPbhq2R69azTShVEb3hKiIBx5uvP_AsvRXFUIB6Ozc6k5ouXNwSeYGSY8XZ-5WG36NSjYBSl8Fwp-wslz5waa4yEoY9BRSSR7ZhjyFT6gMZv7Z4-rRHzr9Oyel3rjCum-sVWMBAgobXboL3-kApL9ZmkR73-NPMF_3Mvp8LFLvvYh2nByIWOSiMAIsf_s9iCBQ-s1xIZ0lLOKaFhKqbk27VwONs1Hql7PpTs6lM4mPFU2BWEj36tosatrNUIbGzLxoZ69s7K3MFMckb-EfE96JpY3ypw_g6oa5T5q7n5CgzWh0cz_PQroNIu1sOBF3LD_xRtfhqkwNIb-xaENBzBRgyRfmBHl9AaUVTEdj_GAc3289Ef2lipikT-oq3tI70GD0yCPYG-0Lo6QBW3PaoPWBFg39MSB08kjOQJxIVcdGnP8q04pBtULCsOo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b3fe31b5c.mp4?token=ESpWshazxF0XtRX3D4ET_Y-o6KnPRpcblGphqvzGUvhVN2e0a3hyw6txk6Yc4H-NoCM4R2K599BaWxao6rhwASaBN3xq9h_IgwQXVbUguG0DFSFUuHJreeBCQOFMy3arFEkSqqelQrVrVDpPq4hpchb8gYCqfjyhnb5rZqmq6nbv2H9RACbkxnRoAz59YMLc_HO1v4IwFyKM8Y_KKPenrgcfcMlcb0txcnM-5HZpoGu4BYUtF1RPbhq2R69azTShVEb3hKiIBx5uvP_AsvRXFUIB6Ozc6k5ouXNwSeYGSY8XZ-5WG36NSjYBSl8Fwp-wslz5waa4yEoY9BRSSR7ZhjyFT6gMZv7Z4-rRHzr9Oyel3rjCum-sVWMBAgobXboL3-kApL9ZmkR73-NPMF_3Mvp8LFLvvYh2nByIWOSiMAIsf_s9iCBQ-s1xIZ0lLOKaFhKqbk27VwONs1Hql7PpTs6lM4mPFU2BWEj36tosatrNUIbGzLxoZ69s7K3MFMckb-EfE96JpY3ypw_g6oa5T5q7n5CgzWh0cz_PQroNIu1sOBF3LD_xRtfhqkwNIb-xaENBzBRgyRfmBHl9AaUVTEdj_GAc3289Ef2lipikT-oq3tI70GD0yCPYG-0Lo6QBW3PaoPWBFg39MSB08kjOQJxIVcdGnP8q04pBtULCsOo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
کویتی‌پور، معروف‌ترین مداح دوران جنگ ایران و عراق، دیگه حتی مداحی گوش نمیده
@News_Hut</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/news_hut/69273" target="_blank">📅 22:33 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69272">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HcxD3gHylBdltS7-z2FzbdSblFwvrryUX0SCyMOV83nU76OXxeVh8xovRXchGcESvaF7ZXTELAZQ6Q76BZ0TIlgk_JQromIwQicBtSilP_9x3aqaCgRu6U4piVDCUlqmLDfIxFUwlkCzEHphmKlQjSJfSSXXq6LkqhfKYUXy4JaxoHRmF3k9lHFiQwQTmX9OZ02GK_6FQYf5cb3GI_KSiBw1rfWihv4sVHRYnQ2FQUgc023XU4FFUJMy5rm4BpTlv7O-xnR4P9UaQ-IOZguP3f9Nk64RNDuuUhJfVyMMkNtUzEVqmAEuiuylGkXYQRUKRtJNchFLdnKBhWAU2NCIEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😄
مالک تلگرام ، پاول دورف :  روسیه به‌دلیل اینکه حاضر نشدم خواسته‌هایش برای نظارت گسترده و سانسور در تلگرام را بپذیرم، مرا در فهرست «تروریست‌ها» قرار داده است. طبق قوانین روسیه، من از «انتشار هرگونه اطلاعات در اینترنت» منع شده‌ام.  ظاهراً مقام‌های روسیه هنوز…</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/69272" target="_blank">📅 21:58 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69271">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/o3D_aSjMu6hcimYnpDq_vb_1zcNVKaFw4PBQJoK0dVtOcPd46rzHKTYnY8zXKwRnU_T8IB6kj7zyFzeBeYjpUkHvDRU32q3tRXPBJHKTD6WDp1AVYlyjx21TN2HQU0UgmYk7tXUbJGRXn05IEfyRuIQMRMMzpy7pTQsOx4agmjVX3h79ZDvjpr_qMrDHfEXAnY57gfvmx9qDfXeYJCx2BifI243rG4ek3lxQDXoyiFrtj3yWvHZVgM85pHgD9h37faQ2Bb75bCV_LyecJacFqMurF-Az-pAOgUmCorjCx_yO32uHEO4O_f05sFwjN69FOIZ8SQn5QjKGhY4XNydg6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😄
مالک تلگرام ، پاول دورف :
روسیه به‌دلیل اینکه حاضر نشدم خواسته‌هایش برای نظارت گسترده و سانسور در تلگرام را بپذیرم، مرا در فهرست «تروریست‌ها» قرار داده است.
طبق قوانین روسیه، من از «انتشار هرگونه اطلاعات در اینترنت» منع شده‌ام.
ظاهراً مقام‌های روسیه هنوز نمی‌دانند که چه کسی می‌تواند چه کسی را از اینترنت محروم کند.
@News_Hut</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/69271" target="_blank">📅 21:39 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69270">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7ad22e432.mp4?token=aKfwenQoRhZmgr63_e5QNrDWY-CKDiSg4bpq38szTfchGXsnc3JSpd8t6VOMfGpg0thrZ1cs3Kw_hSf7CNUvjSY7PukHmnCTgj-PBlXOR46DostSjhSEbDg2dmLPLsJ7iVCY_3lpyevBpyCf9O5T-yU56Vi8knIRlOIYWsdx89NW4ylQ36juITr37VphfVqZpx3mtU279PZf8VNF93l-QbWisfc_3abGDzUdiEw7Yr0rNT-Nmz_a80UAufuW2c65WGaa5jKkpsDM8Nagt2DBVlQFubAzay6Fz1GnHzdYRG6nEusdTZecUy6wkurWznxaEaEDNmAWGMygBw9rZgp4Fw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7ad22e432.mp4?token=aKfwenQoRhZmgr63_e5QNrDWY-CKDiSg4bpq38szTfchGXsnc3JSpd8t6VOMfGpg0thrZ1cs3Kw_hSf7CNUvjSY7PukHmnCTgj-PBlXOR46DostSjhSEbDg2dmLPLsJ7iVCY_3lpyevBpyCf9O5T-yU56Vi8knIRlOIYWsdx89NW4ylQ36juITr37VphfVqZpx3mtU279PZf8VNF93l-QbWisfc_3abGDzUdiEw7Yr0rNT-Nmz_a80UAufuW2c65WGaa5jKkpsDM8Nagt2DBVlQFubAzay6Fz1GnHzdYRG6nEusdTZecUy6wkurWznxaEaEDNmAWGMygBw9rZgp4Fw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🔝
سنای آمریکا به طرح قطعنامه‌ای برای توقف عملیات نظامی علیه ایران، مگر با کسب مجوز از کنگره، رأی منفی داد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/69270" target="_blank">📅 21:12 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69269">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64cd6ef9d4.mp4?token=MqcDt6-UdhoGF_TnqCIahQXMIk_7IRwOBhMH2cyF0CQyBP55auIpARcusjE7uTy3fduAr_E1nMVx9uYv6PMSosu500dKf5KnYpCNQumrbWcR8VNhazwZMeJ2gjy5Wwi7qE8-VKpj_ZZbL1ew1p9XX-qJecnETZAAZc4NryMufrgMDxoEGuFlvrGWOLvmfGTMq4RA-Ega6Dqc3BY92f0BxKIwoUYQnLD7svEdQ-D3CqPsMlAiu2Ik61mVxKZ_oz962w95a90NX1DGufWVYiZU8Qc25l1i3KM8R4wAMT-5jkZ5ArVlgD7Q756vQsbqyE3iaLfyz6dks0FgmXgJ2yYEag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64cd6ef9d4.mp4?token=MqcDt6-UdhoGF_TnqCIahQXMIk_7IRwOBhMH2cyF0CQyBP55auIpARcusjE7uTy3fduAr_E1nMVx9uYv6PMSosu500dKf5KnYpCNQumrbWcR8VNhazwZMeJ2gjy5Wwi7qE8-VKpj_ZZbL1ew1p9XX-qJecnETZAAZc4NryMufrgMDxoEGuFlvrGWOLvmfGTMq4RA-Ega6Dqc3BY92f0BxKIwoUYQnLD7svEdQ-D3CqPsMlAiu2Ik61mVxKZ_oz962w95a90NX1DGufWVYiZU8Qc25l1i3KM8R4wAMT-5jkZ5ArVlgD7Q756vQsbqyE3iaLfyz6dks0FgmXgJ2yYEag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
📚
عمران عباسی، عضو کمیسیون آموزش مجلس
:
قطعا تو مهرماه باز شدن مدارس رو نخواهیم داشت.
چون برگزاری آزمون‌ها تقریبا یک ماه تاخیر داشته.
حالا همه تلاش‌مون رو می‌کنیم که اول آبان یا تو خودِ آبان ماه مدارس رو باز کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/69269" target="_blank">📅 20:55 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69268">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1dca29ad7e.mp4?token=IcADLEpyFDv0Zd1WCJlYSymZk-ST343KSgJOhcwp_SBsPz-NMNC32L1FJyU3kGHys-7hs2y-s5k_yPBpf4qPwGErZYQX7S7hKzFKXpFtFmhLhq-WR-KFlAinb5LEa6PNUrdKvIr1MWnDrBQ1L3t3yb3mCeNLdDaU6eHMZ5CTb7a6Pw8ODuBFqs7t-UtTI74HxtOwS_z9cjnM8uOx1JytI0zynSlHis6H82iVEAA2A67va40Hzfgz6z1uH3oKCyrssqR8F36ym-2BfHD68KxQ7mIz2n9Lgkd2GSTadbQFLmV2YqA6Pld1NfKBgZpmIgBDLuWILs1cUOKJYq9quz2sOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1dca29ad7e.mp4?token=IcADLEpyFDv0Zd1WCJlYSymZk-ST343KSgJOhcwp_SBsPz-NMNC32L1FJyU3kGHys-7hs2y-s5k_yPBpf4qPwGErZYQX7S7hKzFKXpFtFmhLhq-WR-KFlAinb5LEa6PNUrdKvIr1MWnDrBQ1L3t3yb3mCeNLdDaU6eHMZ5CTb7a6Pw8ODuBFqs7t-UtTI74HxtOwS_z9cjnM8uOx1JytI0zynSlHis6H82iVEAA2A67va40Hzfgz6z1uH3oKCyrssqR8F36ym-2BfHD68KxQ7mIz2n9Lgkd2GSTadbQFLmV2YqA6Pld1NfKBgZpmIgBDLuWILs1cUOKJYq9quz2sOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
حکومت از امروز یه طرحی رو شروع کرده که بتونه فضای مجازی رو به صورت کامل به دست بگیره؛
طبق این طرح؛ قراره بلاگرها، اینفلوئنسرها و بقیه فعالای فضای مجازی ثبت و ساماندهی بشن.
در عوض می‌تونن از مزایایی مثل بیمه استفاده کنن، اما از اون طرف هم قراره نظارت روی محتوایی که منتشر می‌کنن بیشتر بشه و هر کسی خارج از چارچوب قوانین جمهوری اسلامی فعالیت کنه، صفحش بسته و با برخورد قانونی روبه‌رو میشه.
@News_Hut</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/69268" target="_blank">📅 20:50 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69267">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46911d7dc4.mp4?token=oXrHfeqV2s0UU-Irhs_RNosN-sV1ggQWDORH1ZZhCuiQ2w47Qsb04k__7mvZd1mx7CbrwfWzon9ELPymh9VZJgSNqrQm7avxM7Y2m58Slc37S44jLHUUlKLnEfo2E-fBNp62qQqKKuv6TD8uCzE8vcSutWxvxEO6UjnenWb1GTn1Yo5hLGTPbEDW-R9-rbuWLdQSQzaCtrAhBsY4HRhDmx6lfP0jZJe7kPSaWOWvdlvjj0fyqUGEm2Uu5WhHggI1NPP2HXxP3lW2V8wbyg3nU16SqLF045XmzQph2Hfe1TueT760ohKvd3r_twk8ENE-qwhtVoGaEWH4dZCPGrP4Rw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46911d7dc4.mp4?token=oXrHfeqV2s0UU-Irhs_RNosN-sV1ggQWDORH1ZZhCuiQ2w47Qsb04k__7mvZd1mx7CbrwfWzon9ELPymh9VZJgSNqrQm7avxM7Y2m58Slc37S44jLHUUlKLnEfo2E-fBNp62qQqKKuv6TD8uCzE8vcSutWxvxEO6UjnenWb1GTn1Yo5hLGTPbEDW-R9-rbuWLdQSQzaCtrAhBsY4HRhDmx6lfP0jZJe7kPSaWOWvdlvjj0fyqUGEm2Uu5WhHggI1NPP2HXxP3lW2V8wbyg3nU16SqLF045XmzQph2Hfe1TueT760ohKvd3r_twk8ENE-qwhtVoGaEWH4dZCPGrP4Rw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
آفرود سواری هم تو ایران ممنوع شد؛سازمان منابع طبیعی:
از این به بعد هر کسی بدون مجوز یا خارج از مسیرهای مشخص وارد مناطق طبیعی بشه، باهاش برخورد می‌کنیم. اگه هم آفرود به‌عنوان یه ورزش به رسمیت شناخته بشه، براش دستورالعمل و چارچوب مشخص تعیین می‌کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/69267" target="_blank">📅 20:14 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69266">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/acbbb58fbc.mp4?token=asUybxu1EgJrfN25tDdO_JMxCe7_TSsBpMGtHw8GsOmoeTcUmJx7L0P2VkWbOR0R-6NRdMvaie-Id8Aw4r2CRp4Ty7ImVL5F0kYb-oaeOTvAs5oaAkxycZYCApCZByT2BaUvapiVyCoKlWGSQ5ZTbc3GHdmOYyrD9smW7WT87JmWfbRYh-8Dq74RNnBfbNj8CH80T1uWgeNRuCpXkIfy89nUM97_Cc5LBMUtEQfSaTcM_wYi5WVGlWYjO45JBF6ZmXzlDWyKcbk1_hiP5DaGVFXG7iPMzCg-g-_xFgx94KFPgmuuPs6CaNcjgdm-HKAjLpzWDcabIddkDZ7nVpl_8Gtk89ORLtNLS9KOhO2fyhYYNPReqwGaInFqlxAsf-wf7FpxovBISjdZkqM-lvoMGCYJswhjzhaxaGG3Qwl0f4ZkbHVAhahZPs9oKIRSbikoulEU93ev3n1RCLPwYySdA1DaOvb_fArsBB91Oo30LrZ5yatsXkg6fpWA8fX_cSsU1FPR_LOBXKt0l2SwT_Ske9qWSq63mQ1tS3kxE2Mtwmk_icH5qict3ZpR6ngeSCejZPH7xp15fanjElTjXtWqWw18xYgl7rbSfJp92YsUxB5UrWcTJ8MRgyUZqMz00nWO2PzYv6YNn3O8qebdHQ6jWHV_oVao0ee9IuFOuXe2AG0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/acbbb58fbc.mp4?token=asUybxu1EgJrfN25tDdO_JMxCe7_TSsBpMGtHw8GsOmoeTcUmJx7L0P2VkWbOR0R-6NRdMvaie-Id8Aw4r2CRp4Ty7ImVL5F0kYb-oaeOTvAs5oaAkxycZYCApCZByT2BaUvapiVyCoKlWGSQ5ZTbc3GHdmOYyrD9smW7WT87JmWfbRYh-8Dq74RNnBfbNj8CH80T1uWgeNRuCpXkIfy89nUM97_Cc5LBMUtEQfSaTcM_wYi5WVGlWYjO45JBF6ZmXzlDWyKcbk1_hiP5DaGVFXG7iPMzCg-g-_xFgx94KFPgmuuPs6CaNcjgdm-HKAjLpzWDcabIddkDZ7nVpl_8Gtk89ORLtNLS9KOhO2fyhYYNPReqwGaInFqlxAsf-wf7FpxovBISjdZkqM-lvoMGCYJswhjzhaxaGG3Qwl0f4ZkbHVAhahZPs9oKIRSbikoulEU93ev3n1RCLPwYySdA1DaOvb_fArsBB91Oo30LrZ5yatsXkg6fpWA8fX_cSsU1FPR_LOBXKt0l2SwT_Ske9qWSq63mQ1tS3kxE2Mtwmk_icH5qict3ZpR6ngeSCejZPH7xp15fanjElTjXtWqWw18xYgl7rbSfJp92YsUxB5UrWcTJ8MRgyUZqMz00nWO2PzYv6YNn3O8qebdHQ6jWHV_oVao0ee9IuFOuXe2AG0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
زنده‌یاد مانوک خدابخشیان:
"اگر رژیم مذاکره کنه باخته و اگر مذاکره نکنه هم باخته"
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/69266" target="_blank">📅 19:36 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69265">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cce71ed1d1.mp4?token=lVGrkgrwP8pW15USyxGS1c4CrWXTf48X4aWuOYZBd2Axl4po5jUEr_0ffvVzA49LoCmbG0X3Ppxr4b4WXwhntEEz0cfFVH4Y8WW65bcM13IvD1jceo1S0IHI1gZxeq7rxet37AcKSHD3apGr99GKaPBpr0Hh93_Wd3qjZOKjsJs2G8PmMDbrneIyiLoKAbCBmdyyWdN_TT8cbcPtUGb3nrY9wDZFsZSfSwJ99B1evL96K8HU43jSek4iJTuCUCV-jwuw9I0_CYKDiajjzPGuFs_7WbXu5CWHz5t6kYXiCLQsl1z1oJLEM52qiU0PqzFJYEaZrvidzMh8B77M0EedDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cce71ed1d1.mp4?token=lVGrkgrwP8pW15USyxGS1c4CrWXTf48X4aWuOYZBd2Axl4po5jUEr_0ffvVzA49LoCmbG0X3Ppxr4b4WXwhntEEz0cfFVH4Y8WW65bcM13IvD1jceo1S0IHI1gZxeq7rxet37AcKSHD3apGr99GKaPBpr0Hh93_Wd3qjZOKjsJs2G8PmMDbrneIyiLoKAbCBmdyyWdN_TT8cbcPtUGb3nrY9wDZFsZSfSwJ99B1evL96K8HU43jSek4iJTuCUCV-jwuw9I0_CYKDiajjzPGuFs_7WbXu5CWHz5t6kYXiCLQsl1z1oJLEM52qiU0PqzFJYEaZrvidzMh8B77M0EedDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
⁉️
سنتکام:در ساعات گذشته، رسانه‌های دولتی ایران به انتشار ادعاهای نادرست سپاه پاسداران انقلاب اسلامی (IRGC) ادامه داده‌اند؛به‌ویژه سه مورد زیر:
❌
ادعای اول: سپاه پاسداران (بار دیگر) مدعی است که مسیرهای آزاد و باز در تنگه هرمز برای کشتی‌های تجاری خطرناک هستند.
✔️
واقعیت: خطرات فوری که کشتی‌های تجاری و خدمه غیرنظامی آن‌ها را تهدید می‌کند، ناشی از تهدیدهای لفظی و تلاش‌های سپاه برای انجام حمله است.
❌
ادعای دوم: سپاه پاسداران مدعی است که سه جنگنده رادارگریز اف-۳۵ (F-35) و سه فروند هواپیمای دیگرِ ایالات متحده در جریان حمله اخیر ایران به یک پایگاه هوایی آمریکا منهدم شده‌اند.
✔️
واقعیت: هیچ‌یک از هواپیماهای ایالات متحده در تلاش‌های اخیر ایران برای حمله، منهدم یا دچار آسیب نشده‌اند. تمامی موشک‌ها و پهپادها رهگیری شدند یا به مناطق هدف‌گذاری‌شده نرسیدند.
❌
ادعای سوم: رسانه‌های دولتی ایران گزارش می‌دهند که یک نفتکش تجاری به نام «ام‌تی نورا» (M/T Nora) موفق شده است محاصره ایالات متحده را بشکند.
✔️
واقعیت: این کشتی تجاری موفق به شکستن محاصره مستحکم (دیوار فولادی) ایالات متحده نشده است. بیش از ۲۰ ناو جنگی، صدها هواپیما و هزاران نیروی نظامی آمریکا همچنان هوشیارانه به اجرای کامل این محاصره ادامه می‌دهند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/69265" target="_blank">📅 19:04 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69264">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/906e47e12d.mp4?token=SQWQxD80COsxZM7kzBEhb4e4VxuMG7T5zKUy4GuPTMiApFqwrZyGZdvt8q8EZSmBiInP1Er4DoyIip8T5GwAlOtqCb1dw13Esw_lf6rjGzGw-Y-WUoCaF46HAmXbq9bVcI1vPT3w6WpI4ZnzbCbIINP2WXd8Vw9AVdqmhCBRylOuuc7RXQPurbuMsLUX0dXSksMZwI30w-2PMwCoThqYRTtQEC48QH6IJjII0pi9MuJPeOiZ1ZQD00-Fd43yo_DAGHgVNSrm50Zagg-THyqJ-P3dGoJGjuk3iu5ZzkP1rgPYi-Wv0bX2fKisFEVBCcd0svou2ZVWiN-k9rr9FCO1ag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/906e47e12d.mp4?token=SQWQxD80COsxZM7kzBEhb4e4VxuMG7T5zKUy4GuPTMiApFqwrZyGZdvt8q8EZSmBiInP1Er4DoyIip8T5GwAlOtqCb1dw13Esw_lf6rjGzGw-Y-WUoCaF46HAmXbq9bVcI1vPT3w6WpI4ZnzbCbIINP2WXd8Vw9AVdqmhCBRylOuuc7RXQPurbuMsLUX0dXSksMZwI30w-2PMwCoThqYRTtQEC48QH6IJjII0pi9MuJPeOiZ1ZQD00-Fd43yo_DAGHgVNSrm50Zagg-THyqJ-P3dGoJGjuk3iu5ZzkP1rgPYi-Wv0bX2fKisFEVBCcd0svou2ZVWiN-k9rr9FCO1ag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یه پسر جوون ایرانی رفت پشت فرمون ماشینش ی خر گذاشته رانندگی کنه خودشم داره از رانندگی خره فیلم‌ میگیره
😳
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/69264" target="_blank">📅 18:33 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69263">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🚨
انفجارهایی در صنعا، پایتخت یمن رخ داد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/69263" target="_blank">📅 18:30 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69262">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G-bylJvyGsbdiWQ85IhiwJm0OD9q3ERz6-uiis0JrKka9YhZL94xx5mJngNv5b1ChVKXLPRKU9kmPR0JyvJZoEwhLcw4qupC2UVIabKJVrSt11ALJ3N5qCrH-eDyH6JZ4CvpnjQOFFTug_euw9HISuKJRqNr7XFPvs_rSnS7FKds8UrKJO5gWwJBn9keLfrpu4DDSmOoIqyr0FC_zR3It_OcY3WToeHGEMgLYFyecWwQoofGuNeyrWuPZNyVU_3rcSjlAEUrqtvdnIsaRAT7S3bZv8JcQh_JJ-JAo92THdWEnYrlesmptAYdC4cUujfVrq7c0wfcmD5ogtocYYdQKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سه تا از تروریستای مفعول حشد‌الشعبی که در حمله مشترک آمریکا و عربستان به عراق کشته شدن!
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/69262" target="_blank">📅 17:56 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69261">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FYj2uDZdxuB9WUMjDEXDk0GODgOnFkyZlYdpKh_2mWAGpLRo4Mr_Y8gHIjk92Iu1o6UjVr6RrTFI0pNam4fd7JY03sHO_eOpPNfXE0AIswyZP3C57slxkqUU65gDGQW80IOQZ6GcpnVSUSMmuzxMvIiE3M_DOF-BKSOOfyLPh-rZKPjUomL9-exu4lqqELKv16WFAOLTSqbXNq-HLMcJbZbycgLEfpTQnZF4BzbMu8gpKRinZzj90hNHfbRq44UB26h0aMtf4BL1WvRpx6KmjJGWoYfpXsVpP2UXeq3oG9sf4JcbSvFTwRR9hpBmrXXqCQXo0kBgek4ooBSboozTDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
روابط عمومی سپاه پاسداران؛اطلاعیه شماره ۵۶:
دو آشیانه پهپادی و یک مخزن سوخت هواپیما و بالگردهای نظامی در پایگاه علی السالم به آتش کشیده و منهدم شدند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/69261" target="_blank">📅 17:44 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69260">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/262bb95a39.mp4?token=hCOUfUQ_17Vzuw-8NWPN16Q3joZzNjjfpyESUG1BxPjOx5DieO4ul4hH8Z1nihXv0E2tr7ojNq_6FkCT7yvweZmd_1m0uXr8gem0UopsmOJQazjOFf3sRbtnFz-LWFV094gMHcJrdxrbcWgVhOB5P7w5wNMKMGUvx5QT1VuuHAKbuF_hNimU_SD_k97kTLCO9vkbzLU64_HDXJUJejHVVKTVaplPExFFK4Z-xY_TYbdeKlF7akarO4sGOeca75E9vmLjVKoEZP2xXJJijxpKn7gHt85Kuad6MJ4pHJ73vnWCiVVkix8hl7txZ9UgZKpMz163TZIiMuKOcLmQuTvcbQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/262bb95a39.mp4?token=hCOUfUQ_17Vzuw-8NWPN16Q3joZzNjjfpyESUG1BxPjOx5DieO4ul4hH8Z1nihXv0E2tr7ojNq_6FkCT7yvweZmd_1m0uXr8gem0UopsmOJQazjOFf3sRbtnFz-LWFV094gMHcJrdxrbcWgVhOB5P7w5wNMKMGUvx5QT1VuuHAKbuF_hNimU_SD_k97kTLCO9vkbzLU64_HDXJUJejHVVKTVaplPExFFK4Z-xY_TYbdeKlF7akarO4sGOeca75E9vmLjVKoEZP2xXJJijxpKn7gHt85Kuad6MJ4pHJ73vnWCiVVkix8hl7txZ9UgZKpMz163TZIiMuKOcLmQuTvcbQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ویدویی از لحظه دستگیریِ نوید زیادخان قره‌داغی وسط خیابون بعد از شلیک دو گلوله به پا؛ این همون شخصیه که تو لایو دخترارو کتک می‌زد و...
⚠️
‌ ‌ ‌
حاوی خون و خون‌ریزی
🔗
‌
مشاهده ویدیوی کامل بازداشت
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/69260" target="_blank">📅 17:24 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69257">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cea20ae2a1.mp4?token=EiACp6k7Fvx5cPIpvmAzZho7T6ZnaRSQAfL2Naq8uPgFY-rgNJ5MGm_A4DH7F7w3EhaSQdMPBPy7VTE6wx07urPSQNJss62MNoPJ2W6j0PqHy1y-xLso44KE_0V3k0hJh9aWTSy_ddgBs-TUgsctDFrGfqnoEu8arBZpgXOR7z-LkzGZ6t1FLkSmuvh_GuBT5EwULfXdPQQhwF9xHjjgmzyso5_4lYFqgIKkzaOW5NmiFSN9rUQ2Bb7-XVlUXACao8sjMpJBHQQdeHOIhl_JCzd_EEZb9UEDEfdK9cfpOVsyIzhPMmmWFIJXDKMkvKDTTQBupVsh1BzMcTiaQPg9Hw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cea20ae2a1.mp4?token=EiACp6k7Fvx5cPIpvmAzZho7T6ZnaRSQAfL2Naq8uPgFY-rgNJ5MGm_A4DH7F7w3EhaSQdMPBPy7VTE6wx07urPSQNJss62MNoPJ2W6j0PqHy1y-xLso44KE_0V3k0hJh9aWTSy_ddgBs-TUgsctDFrGfqnoEu8arBZpgXOR7z-LkzGZ6t1FLkSmuvh_GuBT5EwULfXdPQQhwF9xHjjgmzyso5_4lYFqgIKkzaOW5NmiFSN9rUQ2Bb7-XVlUXACao8sjMpJBHQQdeHOIhl_JCzd_EEZb9UEDEfdK9cfpOVsyIzhPMmmWFIJXDKMkvKDTTQBupVsh1BzMcTiaQPg9Hw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇷🇺
❌
🇺🇦
حملات شبانه سنگین روسیه به کی‌یف، پایتخت اوکراین
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/69257" target="_blank">📅 17:14 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69256">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d31a669dbb.mp4?token=H6Es2S7_TqoIAtsvO5obVB6grslvU_69dsQEVeLZGR7bQMvdUYfNDDqABCMXBCisPM9XhIFLCR9clcIwAtPdtWrFM3e3lsDroqfBfHQuLWvHWyTuq_0urphQIaPU9gDgt5hOfpSGwFOcSJvdZOl7fQflfX6SXGjoWSixv4ePqkw87kmSC2kG2onL2KHAEPkWlm_2oAW1tipbwHqGi_7Nm_oCrjnU9oIE6MzfLMvxwD7pJ8zvysQyw8VRhB27dUfYPFB-epaezJD-bR9hXFYmNu5h6HKFg8PSDoeD-4OLPoLp8ykdGEGyRMWGwhciAQWGyadIYO2PURaww_ca6Jj1JA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d31a669dbb.mp4?token=H6Es2S7_TqoIAtsvO5obVB6grslvU_69dsQEVeLZGR7bQMvdUYfNDDqABCMXBCisPM9XhIFLCR9clcIwAtPdtWrFM3e3lsDroqfBfHQuLWvHWyTuq_0urphQIaPU9gDgt5hOfpSGwFOcSJvdZOl7fQflfX6SXGjoWSixv4ePqkw87kmSC2kG2onL2KHAEPkWlm_2oAW1tipbwHqGi_7Nm_oCrjnU9oIE6MzfLMvxwD7pJ8zvysQyw8VRhB27dUfYPFB-epaezJD-bR9hXFYmNu5h6HKFg8PSDoeD-4OLPoLp8ykdGEGyRMWGwhciAQWGyadIYO2PURaww_ca6Jj1JA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
صبح امروز ارتش آمریکا به یک پایگاه پدافند هوایی سپاه‌پاسداران در اهواز حمله کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/69256" target="_blank">📅 16:33 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69255">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/21d6f2f438.mp4?token=TbRQO886i4V_LQVV2kdwevnoS_tC6KnMIGvM08SEdyBaujyDHBSEMUDtuLBuTbtQWBIRXXikAT98whSTx8OlYbZ1KAjZq1RqE7LGpTSi22EC0cItZ-4nkseSGk_v2ERJ4yKhyBCeA4VbPFEaDy3nJ20q2aNx1dOCkqdFQHvG7WyeX_gMjoQi1h--W-2OA6meu1IINN62It0IIrX2z7oZMj58titNXmpI8-hanikW_86UKt_BZ4ZAC-KZaqAZxjvWVmjEGn3fqRhkiMWXX2quA7Yp7vdhT8izgAXfOG3kNIhKETxEgF23X_V3RhU5KaKn_nL116GSbi4g0kA_Ys1LDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/21d6f2f438.mp4?token=TbRQO886i4V_LQVV2kdwevnoS_tC6KnMIGvM08SEdyBaujyDHBSEMUDtuLBuTbtQWBIRXXikAT98whSTx8OlYbZ1KAjZq1RqE7LGpTSi22EC0cItZ-4nkseSGk_v2ERJ4yKhyBCeA4VbPFEaDy3nJ20q2aNx1dOCkqdFQHvG7WyeX_gMjoQi1h--W-2OA6meu1IINN62It0IIrX2z7oZMj58titNXmpI8-hanikW_86UKt_BZ4ZAC-KZaqAZxjvWVmjEGn3fqRhkiMWXX2quA7Yp7vdhT8izgAXfOG3kNIhKETxEgF23X_V3RhU5KaKn_nL116GSbi4g0kA_Ys1LDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
ویدویی از لحظه دستگیریِ نوید زیادخان قره‌داغی حرومزاده چهل پدر وسط خیابون:
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/69255" target="_blank">📅 15:55 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69254">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f1666d9190.mp4?token=goEVbw4PE5kL_4Dwed_ysLRCVTvbOoJ8xsI2RQUI02QDg5i3jGNLA5sVjBt-nxCJeTvOPnDxrY_4Fq_DiOANm9m_M03b1sgfL71ZZNGd_ryu3eoV07VMt3wDgCbmiMmAcJAQnOLyGMQja1Om5W5e7Vezk0IXRJ1EakQeYTOvuYqwQwtZCaf41zWS2TQNS3BQiN7c1X-LdLx91stAmr-6RvwmBPv6gE1OtiLbfK97srtMduEXJmmrsSMIPL5cCR3JI7rreLQaL1ryxdFJHsF5piZ69mvM9870JcknyTvWJDC-sKJJWLpEpbtviGhE4rffW1lvk1nmhfsFzD94D7qtqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f1666d9190.mp4?token=goEVbw4PE5kL_4Dwed_ysLRCVTvbOoJ8xsI2RQUI02QDg5i3jGNLA5sVjBt-nxCJeTvOPnDxrY_4Fq_DiOANm9m_M03b1sgfL71ZZNGd_ryu3eoV07VMt3wDgCbmiMmAcJAQnOLyGMQja1Om5W5e7Vezk0IXRJ1EakQeYTOvuYqwQwtZCaf41zWS2TQNS3BQiN7c1X-LdLx91stAmr-6RvwmBPv6gE1OtiLbfK97srtMduEXJmmrsSMIPL5cCR3JI7rreLQaL1ryxdFJHsF5piZ69mvM9870JcknyTvWJDC-sKJJWLpEpbtviGhE4rffW1lvk1nmhfsFzD94D7qtqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت صداوسیما بعد از هر حمله آمریکا
🤣
🤣
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/69254" target="_blank">📅 15:20 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69253">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">‼️
🇨🇳
🇮🇷
رویترز:به گفته منابع، ایران ظرف چند هفته آینده سامانه‌های موشکی دوش‌پرتاب چینی دریافت خواهد کرد.  ۲۹ ژوئیه (رویترز) - سه منبع آگاه از این قرارداد به رویترز گفتند که انتظار می‌رود ایران ظرف چند هفته آینده، نخستین محموله از مجموع ۴۰۰ دستگاه پرتابگر موشک…</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/69253" target="_blank">📅 15:06 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69251">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/C-KxsF8sYGnQRsUxDIBUz0Muuleo3CGCUUnX7NY91EnrxWjAWfGzFFSepYUk83AJ1OyPOn815_lzkoLByJMIemUubB0jX4B0GwrYgvVreYyhtrKl7wuVACHsNDH6e0lRszO77HHhstLxFYpi2Hy_zpKNkE5FcQaHbVc7JecZty2U0AnLVolwdanc4iI88jJYe9iQUSpxU44MTmIJ4_U2Df6-r6liReddCYNCpuUD2hF4bPQe9bNGHj_-7L-tydOwAwSP7it53K0mlPlwBynl6rTf7GlZwvjd24voB1rJc0Mp2OMx4HXkrDKAx6LF4KLhcclreDgC9EW5CNfPGJBAIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/8b887c1d39.mp4?token=o2G4gjLhXl9j7ctf6McAaGhxR5lulS1zSjI_HpEFJY6Gd0UTxDUsd9w7Z6YQjgi7IPhx2_i3laC_8eV4yPupMgQAoFI7LTyNulkNWMv-8XOeCW03w1oqc9f22wLrAglRmEN5TaktyWfYgHssAsiLV7B1Am4gExuVrCbIWpkyjYrBPsSNZnwtRAV1Ks_qnPScH64GFfjiJMMLT5V0lYrQuUUVW-aS3NxkcCn4wNHwPb_16gzDx8UjW1Z_G16oEfu4IkHUmyhiBR2K6AZZe4b6XjgpHQQeB22pvaaayrhVDxxwFFFE2wDcy814SaCcQkTFPBbW5fFXTjz1N6519VpHrw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/8b887c1d39.mp4?token=o2G4gjLhXl9j7ctf6McAaGhxR5lulS1zSjI_HpEFJY6Gd0UTxDUsd9w7Z6YQjgi7IPhx2_i3laC_8eV4yPupMgQAoFI7LTyNulkNWMv-8XOeCW03w1oqc9f22wLrAglRmEN5TaktyWfYgHssAsiLV7B1Am4gExuVrCbIWpkyjYrBPsSNZnwtRAV1Ks_qnPScH64GFfjiJMMLT5V0lYrQuUUVW-aS3NxkcCn4wNHwPb_16gzDx8UjW1Z_G16oEfu4IkHUmyhiBR2K6AZZe4b6XjgpHQQeB22pvaaayrhVDxxwFFFE2wDcy814SaCcQkTFPBbW5fFXTjz1N6519VpHrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
مادر جاوید‌نام ابوالفضل سپاهی، که توی میدان علیخانی اصفهان اعدام شد:
خطاب به یه نفر به اسم هادی: بگم برات که تیر زده بودن تو پای ابوالفضل؟ بگم برات که زیر چشماشو با فندک اتمی سوزونده بودن؟
بگم برات که ۲۰ روز بهش آب ندادن؟ بگم برات که فکشو شکسته بودن؟ بگم برات که دماغشو له کرده بودن و آویزون شده بود؟
هنوزم تحمل شنیدنشو داری که بگم برات...؟
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/69251" target="_blank">📅 14:50 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69250">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🚨
🇮🇷
سپاه‌پاسداران:
تخریب کامل سه فروند هواپیمای اف 35 و ورود خسارت سنگین به سه فروند دیگر در الازرق در پاسخ به جنایت دشمن آمریکایی در قشم.
همچنین چند افسر و کادر فنی و تعمیرات دشمن نیز در این حمله کشته شدند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/69250" target="_blank">📅 14:20 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69249">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/daa6076311.mp4?token=hWVgGUmx9xuMHJr9UWVDgso0cJFZ6705vyWCXzWA1qxtSD-Hz-eWbm8PfSLUY_0-qb4xlWhZ0AElMH0LI7saqslKolekKZCEk49iH_Jj3F3stb0E-E62kO2yC1skkOSCFWsT7MYmUmU_8y_rD_MrPu48ldU2b1-RjjwHjdizlYOE2g3Akyut4-SLBD4_LKiy5CZi8LeIbAgZpym2Nqi1DetUcT4qnt6bNw0oHm9Nb1Np2i6648q3XTsdQDAqd5jo4LMQdyuEMQOenxbsDySceDoH9-DWpj36LYv4I5U_lVYlSRikGVpKmMARGO6rWLC7SozboLlK6_v4buCyCFJSRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/daa6076311.mp4?token=hWVgGUmx9xuMHJr9UWVDgso0cJFZ6705vyWCXzWA1qxtSD-Hz-eWbm8PfSLUY_0-qb4xlWhZ0AElMH0LI7saqslKolekKZCEk49iH_Jj3F3stb0E-E62kO2yC1skkOSCFWsT7MYmUmU_8y_rD_MrPu48ldU2b1-RjjwHjdizlYOE2g3Akyut4-SLBD4_LKiy5CZi8LeIbAgZpym2Nqi1DetUcT4qnt6bNw0oHm9Nb1Np2i6648q3XTsdQDAqd5jo4LMQdyuEMQOenxbsDySceDoH9-DWpj36LYv4I5U_lVYlSRikGVpKmMARGO6rWLC7SozboLlK6_v4buCyCFJSRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
فرود دیدنی یک F/A-18 Hornet بر روی ناو هواپیمابر.
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/69249" target="_blank">📅 14:14 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69248">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ksj5yMnYN2sV0x2rXX1aAXIpP7pcPLHVRJ2A-JtHMq8sCmT1EVBtGAb98IgkFHvroPPRGFcJCkP7PpbBEq_PlVditkUoT331Ju6tP4B5MLBNjTzwL6ct_2jalAT2uGU4NtKY_UboG2MfHUZPx15Vif1LRubkAnettIlF7i10CgVgMDld8vFQ-YYY1299IzLX1xIc1DUoiq8kad3PX4qJSQC2Mi_56e8T43ZasACnwH8ynN1j2DdzzO82I61ybIC7cg_WUCAbbgTUGKEn-DWPtN-Gl84t46oekBlo2Ln2MHF9YxLnYVVs2iVyoS7aCHTlQBninYgPhZTISXKt7LLkcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⁉️
⏺
ان‌بی‌سی‌ نیوز:
به گفته منابع آگاه، ترامپ در قبال مسئله ایران «به‌شدت کلافه» شده است، چرا که مقامات ارشد بر سر راهبرد واحدی توافق ندارند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/69248" target="_blank">📅 13:29 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69247">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/a176457914.mp4?token=tNcqeZN-TWIsV7lxlf1ikVyONxB0L1UWveLJiGsEIxoIjSHXlNAkTCwzXBTZqwJTXkv9XhTyR7WHSHrOavCfobpe8tYwaQR_zffvKubhydszUOPELy_YhnathR-EYGfdwi2TqRRqkuDX2KruKLgD5qVM1c4MWpk4CSsz-Y89LHD8UV_hPCxZbg2dF-ac_TNLG4Q-A8iKWi4lqWknbVHT-4T0tiWqE9CqtzrSGu-k7_GTiRwUFSn16DbfSuvbmxcebUlwnOfzG5-nLYq7mrWx3NW3h71vZLCpP1Q5SxVP7AlWWeeAfwT2jh2J6B5zp2jkwZGjv9tfEfh-3w4t1O7-3LYcwM-D7NTBuFYycR1ZiE-RHrpFTDpr6ptrY3c70SHKcLXrry17_CMKOES_Mx2_VDA8KIcEEuwGYCF3LEOcDsansFLEmLV2RZ-GYIHNUIpgUs7dNpRX5k_h-gZK5ma-O1wCfBW7C9SG5bFvE1X4e31V9VP5tK4Nov60cZj_JlUYITgs7PYlkP5JceuqF-nFsP2p1B27ItuFKOTTwu6KHnY1LQHLjzKCssUFRMwoAROCXqkI8qyArEKXbMdc5zbKdfG1v8xSopUJR-04Zy-st8wjHn6UQ-bNDrRD8lm7R-mAKFF005k_Tn1zPywmPNkYAc3IeKEIbgdIw-bO8xos1Xk" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/a176457914.mp4?token=tNcqeZN-TWIsV7lxlf1ikVyONxB0L1UWveLJiGsEIxoIjSHXlNAkTCwzXBTZqwJTXkv9XhTyR7WHSHrOavCfobpe8tYwaQR_zffvKubhydszUOPELy_YhnathR-EYGfdwi2TqRRqkuDX2KruKLgD5qVM1c4MWpk4CSsz-Y89LHD8UV_hPCxZbg2dF-ac_TNLG4Q-A8iKWi4lqWknbVHT-4T0tiWqE9CqtzrSGu-k7_GTiRwUFSn16DbfSuvbmxcebUlwnOfzG5-nLYq7mrWx3NW3h71vZLCpP1Q5SxVP7AlWWeeAfwT2jh2J6B5zp2jkwZGjv9tfEfh-3w4t1O7-3LYcwM-D7NTBuFYycR1ZiE-RHrpFTDpr6ptrY3c70SHKcLXrry17_CMKOES_Mx2_VDA8KIcEEuwGYCF3LEOcDsansFLEmLV2RZ-GYIHNUIpgUs7dNpRX5k_h-gZK5ma-O1wCfBW7C9SG5bFvE1X4e31V9VP5tK4Nov60cZj_JlUYITgs7PYlkP5JceuqF-nFsP2p1B27ItuFKOTTwu6KHnY1LQHLjzKCssUFRMwoAROCXqkI8qyArEKXbMdc5zbKdfG1v8xSopUJR-04Zy-st8wjHn6UQ-bNDrRD8lm7R-mAKFF005k_Tn1zPywmPNkYAc3IeKEIbgdIw-bO8xos1Xk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
فیلم گوه خوردن نوید حرومزاده هزارپدر که دخترا رو کتک میزد اومد بیرو
ن؛
از همه عذرخواهی میکنم ، گوه خوردم غلط کردم!
بذارید برم توبه کنم ، درمان بشم و برگردم به زندگیم برسم.
اتفاقاتی که بین من و اون خانم‌ها میفتاد رو تو ذهنم الکی بزرگ می‌کردم و دیگه کنترلم رو از دست میدادم.
خانم‌هایی که کتک میزدم، من رو درک میکردن و هیچ شکایتی ازم نمی‌کردن.
اتفاقا مردم خوب کاری کردن که انقدر واکنش نشون دادن؛ باعث شد یک بار واسه همیشه به خودم بیام و خیلی مسائل رو کنار بذارم.
از تَه قلبم از همه مردم عذرخواهی میکنم.
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/69247" target="_blank">📅 12:46 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69246">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ba1958bb40.mp4?token=CrSU8s-WQo0_tYgQ3bVInTg9NvbwqZVI2iJ-3ghuc_ODXTL1S4ZBzHjH3ccWaR1mofdQZo-1LbVdIEuW6yLQqjEMCkiqhROQXigOLYeMOjmJXgThctdpSc96m1j0Hhqgf5zTNeW713NioHRIJUK7peuL5KRqcPzsVo0Q8OHbvw5Pf3QYvUmTjX6UwPBcSvMd_gV0nkWap0AAnkvX-kvuDCPC6HoWesLRqsACdFxiWM5flSHkBYwkRkC56rbF59_KRE9rM4Yf7fgsNl9Lhrx03wtN8bZadF2yGDWuH4AwKrHB1zAwxQfigjbG2XXQbSOOu9IdPNBwrLdQ3ET7Rg1xPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ba1958bb40.mp4?token=CrSU8s-WQo0_tYgQ3bVInTg9NvbwqZVI2iJ-3ghuc_ODXTL1S4ZBzHjH3ccWaR1mofdQZo-1LbVdIEuW6yLQqjEMCkiqhROQXigOLYeMOjmJXgThctdpSc96m1j0Hhqgf5zTNeW713NioHRIJUK7peuL5KRqcPzsVo0Q8OHbvw5Pf3QYvUmTjX6UwPBcSvMd_gV0nkWap0AAnkvX-kvuDCPC6HoWesLRqsACdFxiWM5flSHkBYwkRkC56rbF59_KRE9rM4Yf7fgsNl9Lhrx03wtN8bZadF2yGDWuH4AwKrHB1zAwxQfigjbG2XXQbSOOu9IdPNBwrLdQ3ET7Rg1xPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
خبرنگار صداوسیما حین گزارش پرید توی آب و فاز کوسه گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/69246" target="_blank">📅 12:13 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69245">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ubMKrthaITLjMmdcLVaSfhBII81bPws0kfUcmub6dUpGKHyfH2g6_ydEjLE2d2Kq0cuV0cyUkGzRyqXBtId8LT75CH_CHJ3bmnp1HGinT-RmGKRASrYTtrJ5VT95Ih5EggDopfwTR7umDWSqQc3OBxetXjZONYhmQFV5jaeSBCqdOYQtjDgO8Po82vdeliiBeSW306rxddhj9zfMTfF2rXNjPGD4i-NMvVfP57UZTpXV0Dp-OgjvF6QTHxAvgumAkyGVotZr3nMtljh7_nlVxUe1-BWNAVlED1HqXVBBPBoiquDWbzkrtS6hs8OM7Q4VJgNMkORfpQOpHLZ4BQIgNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
سپاه پاسداران:
متجاوز رو همین امروز تنبیه میکنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/69245" target="_blank">📅 11:36 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69243">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Uuhnit9uiKubewgznC6EWOEPRiqLZQ84jtJWXnyb0mrZjKXm15I-TXwqLzouN1MADTPRWWqmaiZnAaleq7h8p3327JIz78qSEsk6jmWOzjN9tEQMHxKbvljwbrKSmWhd4dXPP8VWK06oqJw3by0f2zhfDlnBD-2CDfe4zvdFKtS8ozs4Pdqm-mX50h8WX69cCpdxDXO0qc3Ieqscm4JaCMktgx4TKgZxQNn-jqM3-gnjszZhq_GDPtTxpagRdpvGod8WpDA2U4T2YngfsaEYP8jcLmsPb9G_43H_Jonszhf8BBGFX74kNbAx9WDyA90wSH2wadt3FWwOFnpP28Il4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/854dca423a.mp4?token=HEWSr-eavLse0nYXRXTra-WHyPxhu8UOwEjgA3JsfhHh2ml7gQMheXliLu9L4FN3Kr-bf6G_Ts5pza6j-DVJg3bdoyfS3gxiozf0T-nqPhBonQd73mrif-oMQdLXOD-69N6WWgJusPdw0eRUV-gPDr_BggDyR8oXYOyNP5xJaiI_M4n9TkTIpqMlhT7zFSmFEU9ysJ4UWkcrk0lFTV3NeGTiRYxaTXd94YzRyT26eGP7Wq46P3aKZZJpServ8pxia_9SiQBJeNSCTcsqVJinZHcJ1Ab9QPwgoIKMHJlRagO7t9purOi0XeODZhwRsHb2LC4wV-hHJS_HW2ZiR-QRpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/854dca423a.mp4?token=HEWSr-eavLse0nYXRXTra-WHyPxhu8UOwEjgA3JsfhHh2ml7gQMheXliLu9L4FN3Kr-bf6G_Ts5pza6j-DVJg3bdoyfS3gxiozf0T-nqPhBonQd73mrif-oMQdLXOD-69N6WWgJusPdw0eRUV-gPDr_BggDyR8oXYOyNP5xJaiI_M4n9TkTIpqMlhT7zFSmFEU9ysJ4UWkcrk0lFTV3NeGTiRYxaTXd94YzRyT26eGP7Wq46P3aKZZJpServ8pxia_9SiQBJeNSCTcsqVJinZHcJ1Ab9QPwgoIKMHJlRagO7t9purOi0XeODZhwRsHb2LC4wV-hHJS_HW2ZiR-QRpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🔞
ویدیوی وحشتناک از یه حرومزاده به اسم «نوید زیادخان قره‌داغی» داره همه‌جا پخش می‌شه، تو لایو اینستاگرامش چند تا خانم رو خیلی بد کتک می‌زنه و کلی بهشون فحش می‌ده.  هنوز دقیقاً مشخص نیست چرا این کار رو کرده و اطلاعات موثقی بیرون نیومده، بعضی‌ها می‌گن دخترا…</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/69243" target="_blank">📅 11:28 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69242">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/15118cd8c7.mp4?token=UJxXBAMSFlK2MKlg-ZnTz39ih3NkQZjyR8nWRkIkCcKRj4xB0GNwzZs1T9sl53ribEIgKXa9myNLFOIAdtz1sBxy5gSEzp8JOPq2RvsUtBN3UZRABnE5JjZ7VscDDEhEPawmI7eW7I6pB_XUQZ0qOLqmHeHsaMEMQC_-SbHY6tROUU1_OBhLjSEyuskAmJEdlTl9XvpkxqhrjnUxcCcwxB7NNLxQDjLKqGl4DtQPXN7UgZzwPkxEzKXk4SdS-gpLuPF7KrnWJhKi36-o5RHO-OdkqnOq4Sdn06w0OSopFXcvhras-0V-F0cI6-K6d_7-jYp1P6IbE1RsqKJCH-OH2w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/15118cd8c7.mp4?token=UJxXBAMSFlK2MKlg-ZnTz39ih3NkQZjyR8nWRkIkCcKRj4xB0GNwzZs1T9sl53ribEIgKXa9myNLFOIAdtz1sBxy5gSEzp8JOPq2RvsUtBN3UZRABnE5JjZ7VscDDEhEPawmI7eW7I6pB_XUQZ0qOLqmHeHsaMEMQC_-SbHY6tROUU1_OBhLjSEyuskAmJEdlTl9XvpkxqhrjnUxcCcwxB7NNLxQDjLKqGl4DtQPXN7UgZzwPkxEzKXk4SdS-gpLuPF7KrnWJhKi36-o5RHO-OdkqnOq4Sdn06w0OSopFXcvhras-0V-F0cI6-K6d_7-jYp1P6IbE1RsqKJCH-OH2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مصاحبه این خانم در الجزایر و تبریکش به یکی از کاندیدای انتخابات بابت پیروزیش خیلی وایرال شده.
"
منم کلی سوال دارم
🙂
"
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/69242" target="_blank">📅 11:26 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69241">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🎙
خبرنگار:
نیویورک‌تایمز گزارش داده قبل از شروع جنگ، شما به ترامپ گفته بودید برنامه موشک‌های بالستیک ایران ظرف چند هفته نابود می‌شه، بدون اینکه تنگه هرمز بسته بشه و حتی ممکنه به تغییر رژیم هم منجر بشه.
اما الان بیشتر از پنج ماه از شروع جنگ گذشته، ایران هنوز موشک‌هاش رو داره، رژیم همچنان سر کاره و عملاً تنگه هرمز هم بسته شده. چرا ارزیابی اولیه‌تون این‌قدر اشتباه از آب دراومد؟
🇮🇱
نتانیاهو:
این اصلاً ارزیابی من نبود و چیزی که نقل کردید، درست نیست.
فقط یه پیش‌بینی می‌کنم؛ بعد از این شکاف عمیقی که بین مردم و حکومت ایجاد شده و اتفاقاتی که رخ داده، فکر می‌کنم این رژیم در نهایت سقوط خواهد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/69241" target="_blank">📅 10:44 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69240">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e988916503.mp4?token=YRH9DNH1U-JXu9FSvahOWAksvQzYH2Nq1aaTU1YRh5ZMyt4hEYp_yIMbBd0SMnxYtxSjuWoOwGl9OmwAlHb_zIF1EwWM_1VEKNiXng0CapeITCCnXUhDk4OFg80GcnhfCGh5dt0krBuCHthjaPlmCCu1LvdcYxRbCsWJPKzs9BBw_R-k6PT_G1SbROO0Dprp_KmBR-dW56-RK213Pt6gU22KXnzZW6Ve5PFYBGIO2hQCfDwlNvpYiSLUzrevtGQAjjdeasa-T88bdwbcNk80XBmEAzHiLYEMusIKJKgoAlP61hCwJv2Mj5Q85-gvozGpp5yOuWemhMM8BcUMUW68nw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e988916503.mp4?token=YRH9DNH1U-JXu9FSvahOWAksvQzYH2Nq1aaTU1YRh5ZMyt4hEYp_yIMbBd0SMnxYtxSjuWoOwGl9OmwAlHb_zIF1EwWM_1VEKNiXng0CapeITCCnXUhDk4OFg80GcnhfCGh5dt0krBuCHthjaPlmCCu1LvdcYxRbCsWJPKzs9BBw_R-k6PT_G1SbROO0Dprp_KmBR-dW56-RK213Pt6gU22KXnzZW6Ve5PFYBGIO2hQCfDwlNvpYiSLUzrevtGQAjjdeasa-T88bdwbcNk80XBmEAzHiLYEMusIKJKgoAlP61hCwJv2Mj5Q85-gvozGpp5yOuWemhMM8BcUMUW68nw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
سؤال: آیا هدف شما همچنان تغییر رژیم است؟
🇮🇱
نتانیاهو:
هدف من این است که اطمینان حاصل کنم ایران، با وجود این رژیم، به سلاح هسته‌ای دست پیدا نمی‌کند.
این موضوعی است که من و ترامپ هر دو بر سر آن توافق داریم، چرا که در غیر این صورت، با دنیای متفاوتی روبرو خواهیم بود.
آن‌ها با سایر کشورها و جوامع دیگر متفاوت هستند.
🎙
سؤال:
همین دیروز گفتید که به نظر شما دستیابی به یک راه‌حل دیپلماتیک بعید است. چرا فکر می‌کنید ارزیابی‌های شما تا این حد با یکدیگر متفاوت است؟
🇮🇱
نتانیاهو:
خب، نمی‌دانم آیا واقعاً بعید است یا نه، اما می‌دانید، من نسبت به شیوه عملکرد ایران تردید دارم.
آن‌ها همیشه دروغ می‌گویند، همیشه تقلب می‌کنند و همیشه وقت‌کشی می‌کنند. آیا ممکن است این رویه با اعمال فشار کافی دیپلماتیک و اقتصادی تغییر کند؟ باید امتحان کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/69240" target="_blank">📅 10:38 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69239">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S-jv7eOOkJjCzlPNptYOVocojpIkUaRT4rQQeqCoqmctQVFMsZ6JyZm4U158sPIePa03GonWN08nhQRALiHKI_e-mOf5Er8YgfrfhzLFSdkcb0wIuSIvygNKbJrtKPf-goIa7q3g6coDhVOyA0DzTKPn9DKEcxBw4SPJxOIDW6MZ3hU5PNPnmjp8bIV9clyoYyEYqd-CFBJS2Xn5nt713Kit2-wdbPJyw8qfxmJwGVwQctR8mz4Ga-BCpL6V7unIImUKFIVJwgXRm_8rWTXpBaxfAXvV20XFf-cJ8jrVxrp73E_9p4xW5vb5hj92Gq8kRfvcFErzh6_N-zIihNFCYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⁉️
🇺🇸
تحلیل مرکز مطالعات استراتژیک و بین‌المللی (CSIS):
ایالات متحده اکنون تقریباً ۸۲۷ موشک پاتریوت و ۲۷۸ موشک رهگیر دفاع هوایی ارتفاع بالای ترمینال (THAAD) باقی مانده دارد که نسبت به تخمین‌های قبلی به ترتیب ۲۳۳۰ و ۴۵۲ کاهش یافته است.
تحلیلگران هشدار می‌دهند که با وجود تلاش‌های گسترده برای تولید، تکمیل مجدد این موجودی موشک‌های پیشرفته می‌تواند سال‌ها طول بکشد و در صورت بالا ماندن تقاضا، ظرفیت محدودی برای سایر موارد احتمالی عمده باقی می‌گذارد.
سی‌ان‌ان گزارش می‌دهد که منابع پنتاگون می‌گویند این تخمین‌ها نزدیک به ارقام داخلی هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/69239" target="_blank">📅 10:33 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69237">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8d926097b7.mp4?token=AxUKP24hW8hCTYCj8hcwAOYZdqaKyPsyr9XiimL8j5YMtSZkrk_WarEvE1QFHroTl9xZOWJbM26-bPWL5cyu4MVzi1r2hChN_XNKGIfaE2QhIKwTITjftYVFIn5a8Uyne5HFf2JgL2P4eUb29aKWSpuCvXtH3yqSjgecV4co3UO0gX7IBbJVngLrnNYkjPKT3tkxuGcvjbGjVdSMHyFK1Kx27xwVVnYAhQi7v72dDw6vp3jGA3tE9h8EC7G50M5A8LHdimwqZqVyoT2iRkm-ypOo86Af9O2rO-DMtEdEEuoZr4aw6eULoKLTWoISe9cgEoEMWGMephYwfAR6WLrUsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8d926097b7.mp4?token=AxUKP24hW8hCTYCj8hcwAOYZdqaKyPsyr9XiimL8j5YMtSZkrk_WarEvE1QFHroTl9xZOWJbM26-bPWL5cyu4MVzi1r2hChN_XNKGIfaE2QhIKwTITjftYVFIn5a8Uyne5HFf2JgL2P4eUb29aKWSpuCvXtH3yqSjgecV4co3UO0gX7IBbJVngLrnNYkjPKT3tkxuGcvjbGjVdSMHyFK1Kx27xwVVnYAhQi7v72dDw6vp3jGA3tE9h8EC7G50M5A8LHdimwqZqVyoT2iRkm-ypOo86Af9O2rO-DMtEdEEuoZr4aw6eULoKLTWoISe9cgEoEMWGMephYwfAR6WLrUsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
ویدیو ای از حملات دیشب آمریکا به نقاطی از کشور
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/69237" target="_blank">📅 09:55 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69233">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/04e8c731a4.mp4?token=p3a8jpBwVjq_lbirIWdO0otbhvfPiy7XiAFPWWcNo3lr-eMzP9oShuAC-nz2seXvCBdGEkVbYaDP4c50SgX-UPmpF7E9Yix-fg4eWkg-5jqKzF3pWbKAOkQouEqN0JqLAnXLEO24WwioHWLSJSk967M15c6BkT5wNXgG7EXPxgOtq3jWfgoAkdjlqmR3PmIv_UauXfERxO9WJY-3xkx919WFMbcPDQtZy0qP7psCA-TBd6aVYJR2KqamdQtLIPqfdFUa30T7GFtAf-DQpAtzrTUNVCn6Ww4sDgNkv-bV-0NedgHE3Rvj4KulgOYdd0UYsVsEo6IFJMIYdU8zMZXuBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/04e8c731a4.mp4?token=p3a8jpBwVjq_lbirIWdO0otbhvfPiy7XiAFPWWcNo3lr-eMzP9oShuAC-nz2seXvCBdGEkVbYaDP4c50SgX-UPmpF7E9Yix-fg4eWkg-5jqKzF3pWbKAOkQouEqN0JqLAnXLEO24WwioHWLSJSk967M15c6BkT5wNXgG7EXPxgOtq3jWfgoAkdjlqmR3PmIv_UauXfERxO9WJY-3xkx919WFMbcPDQtZy0qP7psCA-TBd6aVYJR2KqamdQtLIPqfdFUa30T7GFtAf-DQpAtzrTUNVCn6Ww4sDgNkv-bV-0NedgHE3Rvj4KulgOYdd0UYsVsEo6IFJMIYdU8zMZXuBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
🇺🇸
هواپیمای باری C-2A Greyhound متعلق به نیروی دریایی ایالات متحده، دیروز آخرین پرواز خود را انجام داد و اکنون پس از حدود 60 سال خدمت، رسماً از خدمت نظامی خارج شده است.
🗣️
با از رده خارج شدن هواپیمای C-2A Greyhound، تمام هواپیماهای نظامی که توسط شرکت Grumman قبل از ادغام آن با شرکت Northrop Corporation ساخته شده بودند، اکنون از خدمت نظامی خارج شده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/69233" target="_blank">📅 09:15 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69232">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🔴
چالش ۳۰ روزه: از صفر تا سود مستمر با فوتبال!  ما یک چالش ۳۰ روزه رو شروع کردیم که توش با تحلیل‌های روزانه و مدیریت ریسک، موجودی حسابمون رو چند برابر کنیم. تمام تحلیل‌ها و فرم‌ها کاملاً رایگان در کانال قرار می‌گیره تا خودت روند سوددهی رو ببینی.
➕
پیش‌بینی…</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/69232" target="_blank">📅 03:01 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69231">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/316f36114d.mp4?token=r9BeJo0yohspzJPx43n74CVJsLMrCZARgFxCwKph6r5zqsdIsZOjL8RuB6abv5nKUVFWyh0cG123c9ETfdxJv7sH7bN6Dd-5aqvct9kEpAXXd4RF7qwrE46S-12LzlX_7VBv_QLDoGgUCJQAhxbcC-mgsT4q9o9-v7eY3wwmvC3hRqHivjjKQz-oUL3GGfa2fny8OXj0QMFxskxIzB0OL6PsF1wVFrDBnhnLGkIwARaa1b-TCFcZBEmCVF6-Hd6WfBl8Xa49rS8Wm0nLl6dIl1ZobklDJNFiCcn-JiaQNAokAVSIRlGQ8FHLYwoKCxVXCU6miEKwAMiwTg-CC-e2QQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/316f36114d.mp4?token=r9BeJo0yohspzJPx43n74CVJsLMrCZARgFxCwKph6r5zqsdIsZOjL8RuB6abv5nKUVFWyh0cG123c9ETfdxJv7sH7bN6Dd-5aqvct9kEpAXXd4RF7qwrE46S-12LzlX_7VBv_QLDoGgUCJQAhxbcC-mgsT4q9o9-v7eY3wwmvC3hRqHivjjKQz-oUL3GGfa2fny8OXj0QMFxskxIzB0OL6PsF1wVFrDBnhnLGkIwARaa1b-TCFcZBEmCVF6-Hd6WfBl8Xa49rS8Wm0nLl6dIl1ZobklDJNFiCcn-JiaQNAokAVSIRlGQ8FHLYwoKCxVXCU6miEKwAMiwTg-CC-e2QQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
چالش ۳۰ روزه: از صفر تا سود مستمر با فوتبال!
ما یک چالش ۳۰ روزه رو شروع کردیم که توش با تحلیل‌های روزانه و مدیریت ریسک، موجودی حسابمون رو چند برابر کنیم. تمام تحلیل‌ها و فرم‌ها کاملاً رایگان در کانال قرار می‌گیره تا خودت روند سوددهی رو ببینی.
➕
پیش‌بینی تخصصی بازی‌های دوستانه باشگاهی و تورنمنت‌های معتبر
➕
فرم‌های گلزنی (بله/خیر) و گل بالا/پایین با تحلیل آماری
اگر می‌خوای از روز اول چالش همراه ما باشی، همین الان وارد شو:
🔗
https://t.me/+L5I8ulM6jEc2YmE0</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/69231" target="_blank">📅 03:01 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69229">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oRPXrajGTa-tsgM5CVTlm5qfAVi99LcI8vmULa0thzmm_WcKYGtbw0t3el3o0GqtCZjp_bjY_qMVOkA3HtAwCzx5Xxi-hTEUCwxl5uDnRBlLTkSID3fMuGJ5T_1HGewYktMMQpCxAY3bx2Adosjl7Gw3_2eCiCfSof5HYK-ZKJ3bTzSc6mq_DA4ywY6h2ke52PxNYyz_KINSxgCXcgpaPaXz98nFHBjQBMNFIKMDv7UFQ2hy4V1BDItIvwgNxH95M-Wj7ye3pjaJ8kd82AkKmr--f_J-beFkWsbtIwnUbdrXdetQACDdDrl8yJqRj4ptr4j-tNKyJso-Uzz4DjR62g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/miHtZHvWltXcuCk_VO3DHOJ4FabRKLTAPR0pOTKB8JRGrqg4fe2Tf-1r-95F3uACKCzZuInGpzfIYk8weeO325tX9DN3oxf0welYoFIp7Wqj5ORqbM8oGL1oLvDz0qPEUJU2l7PSUIl8DoFGj0q8Q3Zl9TDaLZC8FBqcMMt4iNT0bVsv1-lRPoXWT2rByK6bwf0kodC-oni66yMYOzOrCU11hz6lnUs-90wUEISxxNEQ-XznmJYgmrVkjPFTvi4iogZQd3oHKW_ILfAprkr3Vm2Kcvg1cIlIoI4hPbn4HHwSlA3ViKXJylJWPe9cnymoSa_A3ZkMG-jU9m1Z9SzYmw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
وال‌استریت ژورنال: دریاسالار برد کوپر گزینه‌ای را برای یک کارزار هوایی تنبیهی علیه ایران آماده کرده است که می‌تواند تا دو هفته به طول انجامد.
کوپر معتقد است اگر ایالات متحده خواهان اثربخشی اقدام نظامی است، باید برای شکستن بن‌بست موجود، حملات هوایی خود را تشدید کند تا بدین‌وسیله تهدید موشکی ایران را به‌طور قابل‌توجهی تضعیف نماید.
این رویکردِ «اقدام گسترده» — که یکی از چندین گزینه تدوین‌شده توسط اوست — نیاز آمریکا به استفاده از مهمات پدافندی را کاهش خواهد داد، زیرا توانایی ایران برای انجام حمله کمتر خواهد شد.
- مقامات گفته‌اند که در صورت تصمیم دولت ترامپ برای بازگشت به عملیات‌های رزمی عمده، نیروهای اسرائیلی نیز ممکن است در حمله بزرگ احتمالی آمریکا مشارکت داده شوند.
- کوپر در جریان تشریح گزینه‌های مربوط به یک کارزار هوایی شدید، از حمایت «هگ‌ست» برخوردار شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/69229" target="_blank">📅 02:45 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69228">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DrXcDz2q7wKxw1dta7vS1BGi4Xg6sd1VkuCImjNr_eC5OJj6x-Y9HNbkZmmW8zrkkuI1g_7uw_N31oUiUWG2kmcMkWEi7-xZYPYStTHwlNsjq0PAact3spMSbJJLpJIUenVS3PJe7cvMmKiRM4SRIWjsJPrjNN5CGsukrqiqtZMEaFgo6-tHHfwdvlZZNWJfsT__vY28BRt6v0u5VJAbE_zSrMvqAmCrbu0-y_EpuR66WDM5oQ47XmWhNJMm-G41MpyImtEkay4C2B1Phwa64VmF2bHlqXK0behORcbvS2INo8AWOVJkPpBqQpr60UT4UTscfG0FTHwnq_v5hs_8NQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
#فوووری
؛باراک‌راوید:
یک مقام آمریکایی به من گفت که ارتش ایالات متحده در حال انجام حملات هوایی در ایران است.
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/69228" target="_blank">📅 02:44 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69227">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🚨
🚨
🚨
گزارش های اولیه از انفجار در نورآباد ممسنی استان فارس
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/69227" target="_blank">📅 02:28 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69225">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G1bGq3rqvhEZgBWovsfFijS1uRCkDQSQ783zMJ6vmdaybAACegBzO6AZ0DJdvyVs6ZcJqO0ghSf9ukgGgT4P1KheRTj5j8OhD0JjSDzJm4d79s5DP1u3wtMwFoJdTRovwAZ19-Zrq102wZq57fIOMTBlsCBmZNc6O0-nfo8_hu9BRnhmaDlJeG0rF02Wi_rFuQLOn3hgQXYstk213JrhNtDRB-XGgcM2bo5c-0wauwGPwoGb066soLlvCVGxcAOMwVmK4OiJ9TioXMho5xDRF518CV3Dqle7oIbNsxsaH8-8g0mFpWjOncu6f7vlYCzqHLKQ1zTHlxpAmgMWSNXQFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
بعد از توییت عراقچی درباره اوکراین، خبرگزاری رجانیوز، عراقچی رو ماله‌کش خطاب کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/69225" target="_blank">📅 01:56 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69224">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QlaOrSCrg03YdhA8dspaXX0G7HYqkmbmTQX8SQtEKW6_1ZLMkPk0o6P17tcuPBqwDCteaVyyQvH4G6qYhCCFaCdcJEE4EP4HaGQ0QWCk7dAN_NgpQQwqwROfrF_0CwMhZ4V2o8yQsxOb8F-mYrhUOCyJ8pNbN3Ae-bYSJSdCPprAc3jSvJsalDuWvf6yyj1w-93pVcSL6h067cHdi5lyIKqXYCwvr4dVrH0IVL5z0YRgUFiphNl6R0A5_9tDeKJDTJExMqAxRkZA_Kf70fX7oNbf42S4H9bRdwQyHti_Gzx4Fl7UhyPp6S_QuxBSdml4oAtAWIDiSMwPpa-bB5XyuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
حساب توییتر خبرگزاری تسنیم وابسته به سپاه بسته شد.
@News_Hut</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/news_hut/69224" target="_blank">📅 01:08 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69223">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y_X7fEi1uAly44gDtp8_mmBYgtt8aitDpsKFfaxjSn-72Ec7L7eznoOFCbBuFy5z8YY84DWYETxeg2WbNmtagRPn_RTqeL_6DNstj20Nl6jE68rFpwbBPcFlaPAw518G6_eTaFZUTfb4MrI3Qsh9VLNRS09idh3jIe2QKIL9hl8C-jvinmD6vjQTlnsiPPgtTfOF9iuBKMTYjLlkuUeykSyVKIslRKkaEuhQggpO_Z3eH3dvy35Fe29g20ga_WjlDcgnoOcIWDO879KKpVjNBYxToSRIujotRy8JmASKnDeeHCvzQRu62S2Bv9tOcEh6fDhXgnXrEJTozqcGu7Ke9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‏9 فروند هواپیمای تانکردار آمریکایی و یک فروند هواپیمای هشدار اولیه مدل E-3B در حال پرواز بر فراز خاورمیانه هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/69223" target="_blank">📅 01:03 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69222">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X5lhqSI_Zc0_wqCFFSrZ0SmGduu7f2v3DDVVU-kBZppFm6VOSiG_fu2w_khD_Fh4UhLid2KfMhmI5NZUj93ZVGUl7L67mlUjphDosDNYmzrCtC1701HglDCKwhayVi1ATw1p7Shy8oL8wzYVQtrMut0OYWXTqJoj_Urgen-rUz7rwkW6MdPipBm8r3fHkzjkPALizlgudG1NVE8JOM3DUn-_e4F4onNmsHGw5BHyeOujahT7ifq6BHsCmubVLma7r7jFTgLe46HdzeTFJ9FIVGrc11sQF56Qkq8cLdb_jFgPayAkmgbOqTu478PYhG9_GvktiIwIcCixAii44XImoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
شش سوخت‌رسان آمریکایی در آسمان منطقه در حال پرواز هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/news_hut/69222" target="_blank">📅 00:47 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69221">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🚨
🚨
🚨
❌
گزارش های غیر رسمی از شلیک موشک از یزد  @News_Hut</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/news_hut/69221" target="_blank">📅 00:44 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69220">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K3dSe_gAH-Xhx332C_MbLRXA7zi_BBbFnh5600KZqxQS8_s3bG5TWTm7vS7GwO6g1tvWp9B34UmqDFcg1EZvxsC8d30zhDpNEg7dXVJ9pUwATncFSskBcmqdCl0AhnnHrAtK4kcajHYor-A9VVtUSBOHknBjYm9By9CeDQoX-vALJT_HqRc4u1I5CMpSl6W-V-HKl31uSGqDnBSXx50zPvAwvEh2dG-3D6Opxdo-N4jvnKSjaKKEzDwoIG65yb5EZ9316MImCbjrL-NHYLdoZOKXWPmjELWGJrI_n3Vj6simX_hryFAITT1RX4BpIMehOsZNRB6CNWQ-CLuSyqSfuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
سپاه تو تلگرام یک کانال و اکانت ساخته بود گفته بود هرکی تو اردن و کویت تحرکاتی از نظامی های امریکایی دید گزارش بده؛
لحظاتی پیش تلگرام سیک اکانتشو زد.
@News_Hut</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/news_hut/69220" target="_blank">📅 00:39 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69219">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🚨
🚨
🚨
❌
گزارش های غیر رسمی از شلیک موشک از یزد
@News_Hut</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/69219" target="_blank">📅 00:34 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69217">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/c08d37ce36.mp4?token=t7xzHaRhPAAug2su1FemBHvNElLzjgqmXiikXXz5kQv7YUyOq8ejt_6a4PMK5nqV-tMqSWvKbFklRMVIGwAJJxgPWhp9sGCwFepD_HQRlgXokiWkM1Jl6vg9acvfzqtqdpgVogdggDkCD1vgqw8T1WhY4vxzfdH2PLFvFZqeUn3koIa80yFF_7o3kTght8ghM_HL47T8p5aOZIkwjsEzjjN4sPThm9mMkPq03C50ei-HxxDcNtYIwGZbRhsLUGWfEJ2TWI0cFFFr5HINe07z4dypPsOGUSBkOEn-17ImRJSTyE5Jyt19Kl6vuyyJM3DBhdj9LJGzkl3BIHy3yvqaeA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c08d37ce36.mp4?token=t7xzHaRhPAAug2su1FemBHvNElLzjgqmXiikXXz5kQv7YUyOq8ejt_6a4PMK5nqV-tMqSWvKbFklRMVIGwAJJxgPWhp9sGCwFepD_HQRlgXokiWkM1Jl6vg9acvfzqtqdpgVogdggDkCD1vgqw8T1WhY4vxzfdH2PLFvFZqeUn3koIa80yFF_7o3kTght8ghM_HL47T8p5aOZIkwjsEzjjN4sPThm9mMkPq03C50ei-HxxDcNtYIwGZbRhsLUGWfEJ2TWI0cFFFr5HINe07z4dypPsOGUSBkOEn-17ImRJSTyE5Jyt19Kl6vuyyJM3DBhdj9LJGzkl3BIHy3yvqaeA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
فیلمی عجیب از تجمعات چند شب پیش خرم آباد!
@News_Hut</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/news_hut/69217" target="_blank">📅 23:53 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69216">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">این گروه با گروهی که ما با آن سر و کار داریم فرق داشت. آنها قبلاً عذرخواهی کرده‌اند،</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/69216" target="_blank">📅 23:21 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69215">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e6df873441.mp4?token=UviN458alps1cZx6CQNfBnkasnlWAXz94XrieoGkrf9M_1fQZK5FexCmoHI3-47jVDnBTQLt8b-cB6tRpwKaRJRyd2gAfe6Z8eoOms_k6_ljhpJHisrQaz137F2-D0UbZOzQFVxX5tcqmuJ98brGlrpS8RksavlO7Nx5qVErPz7iClOiaM4UCJW341hDoKvaSl5g06CnYZADASjink9JjbWK7cJ-hdeQPfGbBHC4KPJGxgaM-sE9wTrr5OfczcSbR37NDFW7rnLvo4luV-yHCz4LbjQrpW3C7Hwlup01YYRSuHtOekYSeUZNQq0mi3BgK-fgByBokbi7ByV3_N9YFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e6df873441.mp4?token=UviN458alps1cZx6CQNfBnkasnlWAXz94XrieoGkrf9M_1fQZK5FexCmoHI3-47jVDnBTQLt8b-cB6tRpwKaRJRyd2gAfe6Z8eoOms_k6_ljhpJHisrQaz137F2-D0UbZOzQFVxX5tcqmuJ98brGlrpS8RksavlO7Nx5qVErPz7iClOiaM4UCJW341hDoKvaSl5g06CnYZADASjink9JjbWK7cJ-hdeQPfGbBHC4KPJGxgaM-sE9wTrr5OfczcSbR37NDFW7rnLvo4luV-yHCz4LbjQrpW3C7Hwlup01YYRSuHtOekYSeUZNQq0mi3BgK-fgByBokbi7ByV3_N9YFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ درباره ایران:
ما ضربه بسیار سختی به آن‌ها خواهیم زد. این را می‌توانم بگویم، چرا که کار زیادی از دستشان برنمی‌آید.
این گروه با گروهی که ما با آن سر و کار داریم فرق داشت. آنها قبلاً عذرخواهی کرده‌اند، اما، می‌دانید، باید کمی آنها را تنبیه کنیم.
شی به شما گفته بود که چین هیچ‌گونه سلاحی به ایران نمی‌دهد یا نمی‌فروشد. گزارش جدیدی حاکی از آن است که ایران ۴۰۰ پرتابگر راکت از چین دریافت خواهد کرد. ترامپ: این موضوع تعجب‌آور خواهد بود. او به من گفته بود که در این کار مشارکت نمی‌کند. او می‌داند که من بسیار ناامید خواهم شد.
@News_Hut</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/69215" target="_blank">📅 23:19 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69214">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad144cccc8.mp4?token=Gf-SPpNnU2iJq11yMdfNfZXRACAmQF5uAnU_WFro0PAJFDmA70edBLCFHbCSleyX4oBxV0NlCXsSM8sySY4afGc3nbROsk0VcDFf0whJuxDdmdj7YmNvGgs2fZJW6dmYNzDOwgpd9rrLIfCQ4p7HpWIHeRUFHjKjN01MnttM7ixqSXDycIqa-MCrR1hlWxkyAhcOs3T_YzQB3Qnu_qFVsOQF4qnM-aBm4_crsigZhFhFedSuvuteu25UQBVOKwln-53dXpU9TQrLs3NfYz9tusWcYFTmK_Mh8gFQP4cFJOaVs9Wlv4wJomKDWAHLio6GocenW_a8Q0GxaY4WHhsnbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad144cccc8.mp4?token=Gf-SPpNnU2iJq11yMdfNfZXRACAmQF5uAnU_WFro0PAJFDmA70edBLCFHbCSleyX4oBxV0NlCXsSM8sySY4afGc3nbROsk0VcDFf0whJuxDdmdj7YmNvGgs2fZJW6dmYNzDOwgpd9rrLIfCQ4p7HpWIHeRUFHjKjN01MnttM7ixqSXDycIqa-MCrR1hlWxkyAhcOs3T_YzQB3Qnu_qFVsOQF4qnM-aBm4_crsigZhFhFedSuvuteu25UQBVOKwln-53dXpU9TQrLs3NfYz9tusWcYFTmK_Mh8gFQP4cFJOaVs9Wlv4wJomKDWAHLio6GocenW_a8Q0GxaY4WHhsnbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
این ویدیو رو بفرستید واسه اون تعداد از رفیق‌هاتون که عشق دعوان:
دیه‌ی شکستن کامل بینی : 2 میلیارد و 100 میلیون تومن
شکستن فک بالا : 160 میلیون تومن
شکستن فک پایین : 640 میلیون تومن
شکستن هر دندون : 105 میلیون تومن
شکستن دست : 160 تا 210 میلیون تومن
شکستن سر : 120 میلیون تومن
شکستن پا : 210 میلیون تومن
شکستن گوش : 350 میلیون تومن
کبودی صورت : 6 میلیون تومن
@News_Hut</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/news_hut/69214" target="_blank">📅 23:14 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69213">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3687c44382.mp4?token=TOjxXkpALMAYVvAv0ZgTsdonnLy5n1vhha0KqY26EJU8dRLT64J6tEfIbM1y0F42nLIIuBxge1kvfBBx2Hbb5w5mFvyoFak6JAgcda2Yj1xYFvV4FESXr5Oh4Nv6177n4KJDwAWxsr5rSnEWZ35MKlpF913d1-FNI_MmTmG5IgCBceBekUBY_jSZ48UR9DXLr2ER1nfUo-GyQz_AGWIKqiOJOemiRhn9-XJYyRhotTzQyc3QdPXbP7ayslSNmzvw0vAJfUr9GpcYTmDb4r40JugyBYnDT74i_2HqKIaFp9kfmzeEIIIjqHzQzoIS7XJBPG7mfZzK94VGRLv7T9vnPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3687c44382.mp4?token=TOjxXkpALMAYVvAv0ZgTsdonnLy5n1vhha0KqY26EJU8dRLT64J6tEfIbM1y0F42nLIIuBxge1kvfBBx2Hbb5w5mFvyoFak6JAgcda2Yj1xYFvV4FESXr5Oh4Nv6177n4KJDwAWxsr5rSnEWZ35MKlpF913d1-FNI_MmTmG5IgCBceBekUBY_jSZ48UR9DXLr2ER1nfUo-GyQz_AGWIKqiOJOemiRhn9-XJYyRhotTzQyc3QdPXbP7ayslSNmzvw0vAJfUr9GpcYTmDb4r40JugyBYnDT74i_2HqKIaFp9kfmzeEIIIjqHzQzoIS7XJBPG7mfZzK94VGRLv7T9vnPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
پرزیدنت ترامپ درباره ایران:
ما ضربه بسیار سختی به آن‌ها خواهیم زد، چرا که نوبت ماست که به آن‌ها ضربه بزنیم.
آن‌ها می‌دانند که این اتفاق در راه است و از ما می‌خواهند که چنین کاری نکنیم.
آن‌ها دیشب تلاش کردند با ۵ راکت به ما شلیک کنند؛ ما همه آن‌ها را رهگیری کردیم.
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/69213" target="_blank">📅 23:07 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69212">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">ویدیو وایرال شده از یک پژو405 که درحال فرار از دست مامور هاست اونم بدون لاستیک!
@News_Hut</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/69212" target="_blank">📅 22:34 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69211">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DkNhCYn34_6w1ecj2VOG_fxSGAkSQesyrRcOa63a1XH536bw7KXKePUp8oJp7fLJNc2p4jp5534wWZJspzmT1UKMifZOWDhazYxttqg-YGtSgDynhuT7lAo8tiFg37JiF9FUfgJ5Pyc5WmvgFo1-yiKmDINY_oe4HqyAhA753DGkbzwrTnb62wm99n6T3mTBiKZNw0LXxawxNfM02TDwC4g2qPZiVwrmFCnHFrNKo947ongrYqfoF8XzMac5bf1gDUL_M3K6ecM3fdKAf6bJ0hW7JoGRLSZYntv10aNBz7yPzwBCaNKiRDyUvhigLmROP-PbkEOazAE_7eB85c8W1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
در حمله دیشب آمریکا به حشد شعبی عراق، ۵ تا از نیروهای سپاه قدس هم کشته شدن.  حالا حامیان حکومت میگن واسه اعدام اون جوونای اصفهانی خوشحالی کردیم، خدا چوبمون زد!  @News_Hut</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/69211" target="_blank">📅 21:59 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69210">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pElJj7wZ3h24d3WcOa_uXIhlvjEGbmOP0JAwluq9GrmLEfmvlRRUdNGkz0YXMXI3FDOlGSclg6mPSm2dXn4A5n2dKQcpxnXJgfd5E7gH7EQpKjsw-Bjs_CPKE-oeuTydzTmfY7NDD53qofEG-jfJFVyCSt2QzWsQlLFJhuJsGHfaZdxX17Si9UZuAt6ADMSkPCPmU9CLZfbGs43-B743OJ8I91jO4_J3fm8DWg1_heBGH3SqAIrsXJNSoBNgw9XBwqVxnZd_Filjrrw5PGXFvfJ0OtT86YZWR7MsdG-JmwW5zIZByJlJaklP5S1d7tcgwpTMyFSjpGY16LzYIZ5IVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
🇺🇸
❌
🇸🇦
نیویورک‌تایمز:
حدود ۲۰ مستشار ایرانی در جریان حملات شبانه آمریکا و عربستان به شبه‌نظامیان مورد حمایت ایران در عراق، کشته شدند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/69210" target="_blank">📅 21:55 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69209">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/pBiEL0e4dspgIwiq86GPnFB-nIq_xQ2N1dmuvJyGEaZSZ9JRbfjTQnsHB1HIYp9W11_mv1EDNRD5wIqV7WRuORUOmSZBNh93Hhx4ab37tCVJj1gngJQtYqTsphHVrmzJ_rfOj-Pgfhylc6-bUXSG7s8b6ocq71vPyKIojz6JoBaQ2yPTRTIeBiJwl2tK3_pJPe2U7rdH24hFiEi7eqeRrDWsz7_aoEcNQxxcwmDnE0-ncneG_p679tyrbOdlv98a39VCQEJKIKPdGPHQxtchU95GO9YU17r_-0J6i0mqYmK6cS2jPsTTY77dg__ECjqbCMiAR3Ep4C3WVQtHbroXIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
در حمله دیشب آمریکا به حشد شعبی عراق، ۵ تا از نیروهای سپاه قدس هم کشته شدن.
حالا حامیان حکومت میگن واسه اعدام اون جوونای اصفهانی خوشحالی کردیم، خدا چوبمون زد!
@News_Hut</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/69209" target="_blank">📅 21:28 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69208">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f3f736bc6e.mp4?token=CBQYJu8h34f3edIJw7ZLIrjnO5XLLpV6DxD0S8Pfl4eoUMR7jPKClebvjvViGTa9Brb4olA35JmifeZ1BIuulFXqW4263oZfikYoX2tm4lSEdnqPudmhGx_HLeOUlreqRVCo_TFhOIS21n62IXP686_3OQx6riP3ohv9UOJ17oRrrKVYd4OKbU4xk_9B96VlY88RJJDd9y0gR966lJ2ZSaS8KamhGJ1YSDbv73TYDO_S9nmTDZHpIb4jduqLUJt9xusZ9nLjcJiLOTNyARIXfUF_2pbOlF6GSrS1-8-uNLZVLuFq-La3oeGtpTi1c57o-T_3NeNiQw-kKbkoft70Y0T3oxcPDov11qHc-b_AcjHF7zrMAlCDbqPMnSbvNrIZ9iLIiBzUKmmWHNwz3OWfRgaZNjL7PNs4MCnWksxEWMA-9cWBbV0VwSrZ-OqbRzO37DG7e_j-SFaudW_LHkUuUnjcpS0k7lxc-tFkYhySSK-5sdfLbzx8yLSuabgpEtQTHzK7QReqprmCvgtHKxVQ_aV38SvzPuitkSJSLaHfTiKGE048X8xbzV4siW1Don1QsEn7M2Qe1S1yPH4ppGbZRr2e70sMmLqKWKXg9teMlwggryT-l8qlG6Ssu78ifdM22ZeWFlvFVdDFT71fZWx1Yh2o56tdAbRxFJTD0monWCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f3f736bc6e.mp4?token=CBQYJu8h34f3edIJw7ZLIrjnO5XLLpV6DxD0S8Pfl4eoUMR7jPKClebvjvViGTa9Brb4olA35JmifeZ1BIuulFXqW4263oZfikYoX2tm4lSEdnqPudmhGx_HLeOUlreqRVCo_TFhOIS21n62IXP686_3OQx6riP3ohv9UOJ17oRrrKVYd4OKbU4xk_9B96VlY88RJJDd9y0gR966lJ2ZSaS8KamhGJ1YSDbv73TYDO_S9nmTDZHpIb4jduqLUJt9xusZ9nLjcJiLOTNyARIXfUF_2pbOlF6GSrS1-8-uNLZVLuFq-La3oeGtpTi1c57o-T_3NeNiQw-kKbkoft70Y0T3oxcPDov11qHc-b_AcjHF7zrMAlCDbqPMnSbvNrIZ9iLIiBzUKmmWHNwz3OWfRgaZNjL7PNs4MCnWksxEWMA-9cWBbV0VwSrZ-OqbRzO37DG7e_j-SFaudW_LHkUuUnjcpS0k7lxc-tFkYhySSK-5sdfLbzx8yLSuabgpEtQTHzK7QReqprmCvgtHKxVQ_aV38SvzPuitkSJSLaHfTiKGE048X8xbzV4siW1Don1QsEn7M2Qe1S1yPH4ppGbZRr2e70sMmLqKWKXg9teMlwggryT-l8qlG6Ssu78ifdM22ZeWFlvFVdDFT71fZWx1Yh2o56tdAbRxFJTD0monWCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
کشتی ترابری گاز آمریکا نزدیک بندر دمیاط مصر با پهپاد هدف قرار گرفت
.
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/69208" target="_blank">📅 20:52 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69207">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f541b0693c.mp4?token=cClpAcGu4gLXssQX_BtFxwvlZpj8dB7HlbUbfvUNb1xXS2vSZr3cVZlKsr4hP60vkXPSXFL_Ufpuhk68THUe7p1WPYfwMMogfPfqO_wPrEeY-IDRpgcF9H2heFSJTkDhtbdiLnJg4NQyv26U1H-IL3sb5q-WbOWfpPi28NtiUWpcOS3UlgGUxR8TBFtXne3bnMaXFZUzPjcQuV9SxfWQqWuAMmlGHE3-LXQe6Ut2tvIkOk0L9uW4RuSFiSSAE_9HVhNFGMjK8PDRbONTLuvhFGA9e04vmR51sY8fV_ElXenNWytaSI1AgEiKU8si5OGd_tjsnvigDp2iy4TmGrn3RTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f541b0693c.mp4?token=cClpAcGu4gLXssQX_BtFxwvlZpj8dB7HlbUbfvUNb1xXS2vSZr3cVZlKsr4hP60vkXPSXFL_Ufpuhk68THUe7p1WPYfwMMogfPfqO_wPrEeY-IDRpgcF9H2heFSJTkDhtbdiLnJg4NQyv26U1H-IL3sb5q-WbOWfpPi28NtiUWpcOS3UlgGUxR8TBFtXne3bnMaXFZUzPjcQuV9SxfWQqWuAMmlGHE3-LXQe6Ut2tvIkOk0L9uW4RuSFiSSAE_9HVhNFGMjK8PDRbONTLuvhFGA9e04vmR51sY8fV_ElXenNWytaSI1AgEiKU8si5OGd_tjsnvigDp2iy4TmGrn3RTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇱
نخست‌وزیر نتانیاهو:
«سفرم به آمریکا فوق‌العاده بود.
همیشه درباره موج نفرت از اسرائیل در آمریکا می‌شنوید، اما احتمالاً کسی از موج حمایت و علاقه‌ای که نسبت به اسرائیل وجود داره براتون نمیگه.
همین الان هم با وزیر دفاع آمریکا،
پیت هگست
، صحبت کردم.
اون یه حرف جالب بهم زد. گفت: "توی دنیا کشورهایی هستن که اراده دارن کنار آمریکا بجنگن، اما توانش رو ندارن.
از اون طرف، کشورهایی هم هستن که توانش رو دارن، ولی اراده‌ای برای این کار ندارن."
بعد گفت: "فقط در اسرائیل هر دو رو با هم می‌بینیم؛ هم اراده و هم توانایی."»
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/69207" target="_blank">📅 20:26 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69203">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SMO-MKzcP1qQgC6708VsUQR1opcVlcn9c72skMjz7ON3bj8GLAgm9IdTEl2tBRGKXoacGQi5vYAFbHst5HRMcvRp8SeN7-0Tc0XfbUTgBCJdlHsTBpSiZksm3wyJMPL6oU7yRQvxKZsEIjLmm1LvKHzdeUnV75jQLfoUQT1RISwVTssv3UbMPzQjt5GwXvt1VRwF7w4rNPDGn1pxtDPVYf_8LrdBJNTgjKZ6C3akLADNjlSljT5ZD8w9VEwrPz75Kpe_LKkv2F8ePwcu0l8OZbShQjTsAvQefa711xWyUiV-ROef17Sfo0SOXOyy16bolrz2bUq2ewDI_3uALGfaZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c1f829b75e.mp4?token=A_wViQGe6EdE1T5i9bPrwoYVCT7frORHfUTunlncWMSWMuXeCDH6Qh3qIfCSRl6Ke0Q8jw_DAY8T_uQKwVVXB4qhoaOXis6SgaZeszKX8yDqo1NCBcMFi2SEYyd_tXyzSTNR75NBI8XNvRNHh8mFufjJcxdvBLRjryt2aL0OoUXAd7TsK8zAmXCBKs6Er0LVLypa7CYLhQeOxX445MOw1mp-jtl7JRle24_PeeNHs8pyKXwm7N0Q3O27-P7tFtK1vHVbAbThCkvehxGiUAKCwEQtvESjQxqQ1mDlxMfycxWlQR7Ms0x7Vv6aZgcMkXOGPYBcRpcZbEHvhL1wq1I1NA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c1f829b75e.mp4?token=A_wViQGe6EdE1T5i9bPrwoYVCT7frORHfUTunlncWMSWMuXeCDH6Qh3qIfCSRl6Ke0Q8jw_DAY8T_uQKwVVXB4qhoaOXis6SgaZeszKX8yDqo1NCBcMFi2SEYyd_tXyzSTNR75NBI8XNvRNHh8mFufjJcxdvBLRjryt2aL0OoUXAd7TsK8zAmXCBKs6Er0LVLypa7CYLhQeOxX445MOw1mp-jtl7JRle24_PeeNHs8pyKXwm7N0Q3O27-P7tFtK1vHVbAbThCkvehxGiUAKCwEQtvESjQxqQ1mDlxMfycxWlQR7Ms0x7Vv6aZgcMkXOGPYBcRpcZbEHvhL1wq1I1NA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇦
❌
🇷🇺
اوکراین با حمله‌ای گسترده و پهپادی، منطقه ریازان روسیه را هدف قرار داد؛ در این حمله، یک مرکز لجستیکی بزرگ متعلق به شرکت «وایلدبریز» (Wildberries) آسیب دید و بنا بر گزارش‌ها، پالایشگاه نفت ریازان که تحت مدیریت شرکت «روس‌نفت» (Rosneft) قرار دارد نیز هدف قرار گرفت.
آشکارترین خسارت در انبار حدوداً ۱۸۰ هزار مترمربعی «وایلدبریز» در نزدیکی شهر «ریبنویه» (Rybnoye) رخ داده است.
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/69203" target="_blank">📅 19:56 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69202">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🚨
⁉️
آمبری:
یک تأسیسات شناور ذخیره‌سازی گاز طبیعی مایع (LNG) با مالکیت آمریکایی و پرچم جزایر مارشال، در دمیاط مصر هدف اصابت دست‌کم یک پهپاد قرار گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/69202" target="_blank">📅 19:51 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69201">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50c2f2b488.mp4?token=hLvCzaR_DSf5omVtHEyhwXezcUYvQAMFLkPTiyAUZ3K-xeeTAzdQyGqKn8wjC-38FiLb2Gwu6-T7E4AkWr2JunfNQrFAorroIyaGninf_38l6XdqQA7qlxLvx61lJgM46Vf3g3hk4bEbCX5KWk5dUAZ-2AT4MGwo2xnm_B24kmM7wEUXATqSi41VLGgITmp6KC37uY2A2Zwcv24AtsvzE6LheSgdZ7lgdMWMAXEg65M51SoVTRi9lFnXcjH_hzj3KWEPruLBFxzCr7XTg-x5h38_SayWesVRlU84lbettSSHtRIPcnPcyD_QSnEIEsP_8hK-eICSAiIyFx_RKVezNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50c2f2b488.mp4?token=hLvCzaR_DSf5omVtHEyhwXezcUYvQAMFLkPTiyAUZ3K-xeeTAzdQyGqKn8wjC-38FiLb2Gwu6-T7E4AkWr2JunfNQrFAorroIyaGninf_38l6XdqQA7qlxLvx61lJgM46Vf3g3hk4bEbCX5KWk5dUAZ-2AT4MGwo2xnm_B24kmM7wEUXATqSi41VLGgITmp6KC37uY2A2Zwcv24AtsvzE6LheSgdZ7lgdMWMAXEg65M51SoVTRi9lFnXcjH_hzj3KWEPruLBFxzCr7XTg-x5h38_SayWesVRlU84lbettSSHtRIPcnPcyD_QSnEIEsP_8hK-eICSAiIyFx_RKVezNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
🇺🇸
نخست‌وزیر اسرائیل، بنیامین نتانیاهو، با پیت هگست، وزیر جنگ آمریکا، در واشنگتن دیدار کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/69201" target="_blank">📅 19:25 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69200">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P52E2XNtsMyL9lJkoPHaNjFxHgMOCf3fM1tgJzH699jjAHNF_T5UZlKiSB2ljQ_ZE8m2gJkKPlFSoxtOVFeE-TFBhbDszvgeOzknIIUPPfV4_RrqyGnMmUV3yuEmMVM44nfL6cbOrlLmYgkC9EViIQIvt9QcZih6eSlyJ4Y792okKWQ9z_fF0dSn6eq_nZC0feB10OqhvIM0mMD2iqxbqJZ3bDlBsyKQo0nXE_RpzY2CUo09e83kRY92umv_VjKoV8wdgybBXNUDjbPtEkpoagn7bHgRN3UrlmZlfELcAZS8DW8nf0XuBOkSIPZx2ihpdKqa2niMZ8C2DCoqV8YcTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
سنت‌کام:
❌
ادعا: سپاه پاسداران انقلاب اسلامی ایران (IRGC) پس از تهدید و تلاش اخیر برای حمله به کشتی‌های تجاری و دریانوردان بی‌گناهی که از تنگه هرمز عبور می‌کردند، همچنان مدعی است که دریانوردان بین‌المللی باید تنها از مسیرهای مورد نظر سپاه استفاده کنند.
✔️
واقعیت: تنگه هرمز یک آبراه بین‌المللی است. سپاه پاسداران هیچ‌گونه اختیاری برای تعیین مسیر جهت تردد آزاد و باز ندارد. کشتی‌های تجاری همچنان با حمایت نظامی ایالات متحده از این تنگه استفاده می‌کنند. از اوایل ماه مه، نیروهای «سنتکام» (CENTCOM) به عبور حدود ۱۰۰۰ فروند کشتی و ۵۰۰ میلیون بشکه نفت خام از این آبراه باریک کمک کرده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/69200" target="_blank">📅 19:12 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69199">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🚨
🇮🇱
یک مقام ارشد اسرائیلی:
ایرانی‌ها سانتریفیوژها را به «پیک‌اکس» (Pickaxe) منتقل کرده‌اند، اما اسرائیل از انجام هرگونه غنی‌سازی اورانیوم در آنجا بی‌اطلاع است.
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/69199" target="_blank">📅 19:02 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69198">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GKypVckndDD2uWSL2mDRBV39H6xUixmIWJZyPle5NdK0pAbS7w-d9d5-UIwxZEEXcMYRYa_WiWgt7u1XYF3HxhFWlGxAdzFHTuyoxNcOamjFf1Dy9Fvg75X14LEzKYjNlMIyr67QVQoWGLIaHXs67Ezt3sK11dLu4i-ss4dCMmKDhMgQhaPStHszKI5TUcWXCdzGkZaHMeKeYjK6qHMReWl_3SrQhkMo8zpptzw1FIlj8qzJ5CRTKvMbNpUVHDZvEwbwPNBj7VZQ7YzG4B12k2JLgOcU_OBDryxxgWvkvknHi9mIfkilTueVq0Pr_7s_zu5Xw9sTksyy2tklsPUahQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
باراک‌راوید:
معاون رئیس‌جمهور، ونس، روز سه‌شنبه با بنیامین نتانیاهو، نخست‌وزیر اسرائیل، دیدار کرد. یک مقام اسرائیلی اعلام کرد که هگست، وزیر دفاع، امروز با نتانیاهو دیدار خواهد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/69198" target="_blank">📅 18:51 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69197">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/euNpXp9RdMlVxETEkRNKlh3x2kH6gZQct-Wg4HQC5vDjBgC13ti2Qv3gCQDhWsFPJl7a2wOom4Iu2KSfzNnwJYUETgdIIF1685FytN6yHZ3YbYo3p60FVi7VAphVYvzFGP1FqKij1GVcCeVdSzWN9cyWYbGEZqaDMYkdl8zYHxqHvGPLpwi0CBuQttLaGRkdAydeOt02OaYYuvlCjfOB73F_iEb-cOoWEAItMJIo_1IvCajPtYtPcDKQYmqX_4c702AziZmuW_KTGg1kO6BZVu4NhFqa4HKPS7SAtoYlAX0W4e57Gx9nmHZIKMHB2Dyj0uVablWwcgtJZJqPiYLMww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
تلفات حمله مشترک آمریکا و عربستان به حشدالشعبیِ عراق تا اینجای کار؛
- 20 کشته
- 32 زخمی
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/69197" target="_blank">📅 18:15 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69196">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TWGlm4hZz-zB6dveiuh7DhsvIIFVBxpu-GtQrbPl6S9fKhFctNVFBKJKzAIPuGhs12OpvzARDNHWDkY0ValSI8obn73KcGtcSSQazE0WfTqsamz1QbCfXbRdt5fSBv0HsNLChXp1bAroRG2uPEejJNe5d7ACdMDDCbcYNDNnK-v3oVE_J0_GaN78OutwDTrlTb5MIMu_slafow2LEv8CrF_CiVbjDTPokLizubPMlwC33ar7mxt7PRgoy-Wu5V3c3qWChhPMWohJXJb0iz46QHrW8WdFn2UiZx4UkaDnCmh-VTgFWK5iLeIp61KuDZ89msiMW_01do2lQ_KSz8R-tQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🇷🇺
پروفایل عجیب پاول دوروف مالک تلگرام در واکنش به تحت تعقیب قرار گرفتنش
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/69196" target="_blank">📅 17:45 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69195">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b07d2f0b1a.mp4?token=g0jsMsUirUPb4YAzYjfISvIsACpSSM8H6AGzLvI0Ce8Q6d9mtHeu-GbyszQElbOkHkW8A2im6HKdDMZ17A3x9amgaKkExZUU1H5M0boa3D89zGTzYZpAyZ7AJpsveC7Q9TguLt7BTSAjKZo6___DDf_BX3yvrYOzQ7GV8_skINwoICVKTOmsYFyhXA0RkjZDegiCKU3ztSpRMxCeqj5OQC-_aSXWJo63e0ee21rnBu39QPoLjT6uA-zgUqHezoiWYI5C485INruDzD7znu2-dGcwBz7sgaEhWELpSNwz6ixM0Ll-JmkmMkAzkk2GklwNgUAHrUYRRZ8QT6IKiNdw3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b07d2f0b1a.mp4?token=g0jsMsUirUPb4YAzYjfISvIsACpSSM8H6AGzLvI0Ce8Q6d9mtHeu-GbyszQElbOkHkW8A2im6HKdDMZ17A3x9amgaKkExZUU1H5M0boa3D89zGTzYZpAyZ7AJpsveC7Q9TguLt7BTSAjKZo6___DDf_BX3yvrYOzQ7GV8_skINwoICVKTOmsYFyhXA0RkjZDegiCKU3ztSpRMxCeqj5OQC-_aSXWJo63e0ee21rnBu39QPoLjT6uA-zgUqHezoiWYI5C485INruDzD7znu2-dGcwBz7sgaEhWELpSNwz6ixM0Ll-JmkmMkAzkk2GklwNgUAHrUYRRZ8QT6IKiNdw3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🔞
ویدیوی وحشتناک از یه حرومزاده به اسم «نوید زیادخان قره‌داغی» داره همه‌جا پخش می‌شه، تو لایو اینستاگرامش چند تا خانم رو خیلی بد کتک می‌زنه و کلی بهشون فحش می‌ده.
هنوز دقیقاً مشخص نیست چرا این کار رو کرده و اطلاعات موثقی بیرون نیومده، بعضی‌ها می‌گن دخترا رو گول زده و برده خونه
⚠️
ویدویوی کاملش ده دقیقه‌ست اگه خواستین می‌زارم ربات ببنید
🔗
🔞
مشاهده ویدیوی کامل
@News_Hut</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/69195" target="_blank">📅 17:42 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69194">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RILV_Fzex5g-JIV5cGx8wtgA32dV-ca6StYg57_FrJUBbx2TpS7_O0Pprk-z5Lvy19SO0Em0aIYBoxZsh_tW9G-sGGBEab3FAFHSZk_nCdJigra-lUBAGNef_Z5uLyFePvGMUU3iOnwH-SmWZQFEwQWvURklsu5v0Dbo69n7tQCHaErESoP84HjtF8-6gHGc783tqu2uM1Iym4qJly23q-B-2Wa4WAHS0sR7B_2HYt0MxC-ag9XPSONdjsSwDLcwH8WLpWzyrdJLZGeh7uw1PuZuylvkjE0TAxX4E7sxmMPqJZ5Zi56GB3koux8bAh1FNgrTBGX6HHLih1BBPe-i_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نیروی هوایی ارتش جمهوری اسلامی   اعلام کرد بقایای پیکر امیر سرتیپ خلبان مجید کاظمی یکی  از  خلبانهای  2 جنگنده سرنگون شده Su-24MK که توسط F-15Q های قطری سرنگون شده بودند را در خلیج فارس پیدا کرده است و از سرنوشت ۳ خلبان دیگر اطلاعی در دست نیست.
@News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/69194" target="_blank">📅 16:56 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69193">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b9f57d9f95.mp4?token=p_W1mUyvXJx7kzCTKq4Pih5fS_eHVfqDYv9uu9Haq1EEXJH4pn6Bexq4i4CqnRcRerW3EXQtWk1Q7rOszV9XhPgcWLDFseOiTt1BanFUmM4ScQAAidMczbPiejCCH6xvNdWjRga7CNN-owl0nGHVK6AXR0E4QN4fcz2nwriVt4mfOCv40BzLge-e4a8DV4AKL1_q9dimNoRpa2SBaD3pFQJBoerL8jRPHJXftaKFHcTIIMXS8RqBmipFgAPM8EE8Imkda4UnO3u2Z6eZL6A3CpEkQ-ViCE6sOCUuJO-XGelHgES_a1aedSR2s-gp3Civ1Eja0wrdlZqEAWSyuaUJkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b9f57d9f95.mp4?token=p_W1mUyvXJx7kzCTKq4Pih5fS_eHVfqDYv9uu9Haq1EEXJH4pn6Bexq4i4CqnRcRerW3EXQtWk1Q7rOszV9XhPgcWLDFseOiTt1BanFUmM4ScQAAidMczbPiejCCH6xvNdWjRga7CNN-owl0nGHVK6AXR0E4QN4fcz2nwriVt4mfOCv40BzLge-e4a8DV4AKL1_q9dimNoRpa2SBaD3pFQJBoerL8jRPHJXftaKFHcTIIMXS8RqBmipFgAPM8EE8Imkda4UnO3u2Z6eZL6A3CpEkQ-ViCE6sOCUuJO-XGelHgES_a1aedSR2s-gp3Civ1Eja0wrdlZqEAWSyuaUJkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ درباره حمله اخیر ایران به اردن:
این یک حمله غافلگیرانه بود. نیروهای آمریکایی تنها چند دقیقه فرصت داشتند تا موشک‌های ایرانی را رهگیری کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/69193" target="_blank">📅 16:10 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69192">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c969cbc6b9.mp4?token=bVcsqKAaMtK5g_qy4IPssF4r0ZbQODs-oFy74WXgUXNbxu7jeoXCqDUkF9H1I8V1W2nJKxwgCgI-QP0bTArjvxpVjWPr8qy4FWzjErwIhM7wGfoLywfB3Wp5aT7I97W1DXVSEfmZfLgiHva2WpjnO3AK3t7dbE3bFC9IHu7K3CiduJlNfadfaOQEI828RPaXjnkh8gTyWJ5Z88kRcIVoIv8stBKsd3Rdl4mmE59dDeuNV9_zfviYVNWIqhIAkmCqeDTd2E7JnvNOVcqFioNSpLVsi2n0es0GDWqAkbojv4P9Ns9Y_ZbGNdGokM6AM3HfK1repqzITRnl4wMVJViQFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c969cbc6b9.mp4?token=bVcsqKAaMtK5g_qy4IPssF4r0ZbQODs-oFy74WXgUXNbxu7jeoXCqDUkF9H1I8V1W2nJKxwgCgI-QP0bTArjvxpVjWPr8qy4FWzjErwIhM7wGfoLywfB3Wp5aT7I97W1DXVSEfmZfLgiHva2WpjnO3AK3t7dbE3bFC9IHu7K3CiduJlNfadfaOQEI828RPaXjnkh8gTyWJ5Z88kRcIVoIv8stBKsd3Rdl4mmE59dDeuNV9_zfviYVNWIqhIAkmCqeDTd2E7JnvNOVcqFioNSpLVsi2n0es0GDWqAkbojv4P9Ns9Y_ZbGNdGokM6AM3HfK1repqzITRnl4wMVJViQFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ به شبکه فاکس نیوز:
گروه‌های شبه‌نظامی مورد حمایت ایران در عراق، یک آفت جهانی هستند.
من در حال بررسی صدور هشدارهای بیشتری علیه عوامل نیابتی ایران هستم.
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/69192" target="_blank">📅 16:08 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69191">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ:
در پاسخ به حملاتی که اهداف آمریکایی در اردن را مورد هدف قرار داد، حملاتی علیه ایران انجام خواهد شد.
ما ایران را به شدت مجازات خواهیم کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/69191" target="_blank">📅 16:04 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69190">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dQBLz6dcE7DJiy9j-uDtq3LuT8f9ehCqZeawXgAPlsiCCiuoj4UK6BvfHd_bXMltALpR8NKW_cZjVd_scb7DyZCzcf8EVIgvsMRHCQ1oEG54pc6xRju6jkywT9WXuVpj86xIeFu7tfMxLCm_DQBzIlR6c6Lm6aLRkHsyta9Ud6ocX6dCOxnEaQwAVTAsjkcn928pWNiPdy10iIWDUjU987PGVUlOA6OS4qmGC2ZRnd9SSScTTGj6cA0FheMak8tAL1A7Nls9r_H3WA5EdWXWJbXw-lkvUAoR32u05SqZpJjufZDvsxv_j46rfuiiRXCCWgTmsnUefYVCFjSn2IyI4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پس تنش های دیشب، قراردادهای آتی نفت خام آمریکا ۴.۴ درصد افزایش یافت
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/69190" target="_blank">📅 16:03 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69189">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/640b7bb0a7.mp4?token=qZ2G1jA7wrxs58D6_Y7WT0xceHPleYTlTYm5tBem9dzqz0sfXlgYqcGPI-ZI5rWCLSudhVn9lkd5nvMCpODcJvm-FtEwUbo2efCH_pxNlLgWPjBgpZQ98kDKX5NxFeil09bK3AfjQwortI6AkRlJk3zNt3cqonAY6jqqhlLGOQXkUD4x1f9e9pegBwcJrbaCaEuTJ4N0Hf29us8l34xKViVv37cuYU7FGGeXnCOmeXZuzsfFkAKZ9jndXMmnwgyWfZROxucsYSc7UL66M8H-duHQKnqvKAdRbe5B9FZsYSGbo_k5AWpH0AdThbRoIfguXM7A90SDEz6HWs4_ogIs0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/640b7bb0a7.mp4?token=qZ2G1jA7wrxs58D6_Y7WT0xceHPleYTlTYm5tBem9dzqz0sfXlgYqcGPI-ZI5rWCLSudhVn9lkd5nvMCpODcJvm-FtEwUbo2efCH_pxNlLgWPjBgpZQ98kDKX5NxFeil09bK3AfjQwortI6AkRlJk3zNt3cqonAY6jqqhlLGOQXkUD4x1f9e9pegBwcJrbaCaEuTJ4N0Hf29us8l34xKViVv37cuYU7FGGeXnCOmeXZuzsfFkAKZ9jndXMmnwgyWfZROxucsYSc7UL66M8H-duHQKnqvKAdRbe5B9FZsYSGbo_k5AWpH0AdThbRoIfguXM7A90SDEz6HWs4_ogIs0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تو مراسم ختم اکبر عبدی، مهوش وقاری وقتی داشت درباره مرحوم عبدی مصاحبه می‌کرد، یه پیرمرده تصمیم گرفت وسط مصاحبه باهاش یه سلفی بندازه
🌟
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/69189" target="_blank">📅 15:15 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69188">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ismst3gTERWc3otolYcbW0XH6HK4zQO9t8ezey-v17rwgD9nz9E_T3Bd-JM0QAOKo5ZmfDFEdAa9llK3MPLpiKcNl5ijtMFneVclUavZ0_tWDhFHoIfJGUNcKaUFdJNE8EMs1fz91-Vk-Hh7sMJAATj43ihh6vnEwpwmbeUqF9pVHDEO098sN6QUYiSG4jii-_afsZ608Iv-Ib0e4IuolxbCIYzS-Urd2DY4RqjDDUzyWzwqEsDK-2tzxHsX7ZFiTBWWWM2wP-ugwQ4qsoPrzd3gtHNJE0jt4HsVR9T073dSRLvqGKvJ9Q5kTakmGbka-JPDH9v3uCR6tJCPdlGDPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇨🇳
🇮🇷
رویترز:به گفته منابع، ایران ظرف چند هفته آینده سامانه‌های موشکی دوش‌پرتاب چینی دریافت خواهد کرد.
۲۹ ژوئیه (رویترز) - سه منبع آگاه از این قرارداد به رویترز گفتند که انتظار می‌رود ایران ظرف چند هفته آینده، نخستین محموله از مجموع ۴۰۰ دستگاه پرتابگر موشک پدافند هوایی دوش‌پرتاب ساخت چین را دریافت کند؛ اقدامی که در راستای بازسازی توان دفاعی این کشور در بحبوحه مناقشه با ایالات متحده صورت می‌گیرد.
این خرید که ارزشی بین ۶۰ تا ۷۰ میلیون دلار دارد، یکی از بزرگ‌ترین اقدامات شناخته‌شده تهران برای تقویت سامانه‌های پدافند هوایی کوتاه‌برد از زمان آغاز درگیری با ایالات متحده و اسرائیل محسوب می‌شود؛ درگیری‌هایی که کاستی‌های موجود در توانایی ایران برای حفاظت از تأسیسات نظامی و زیرساخت‌های راهبردی را آشکار ساخت.
به گفته این منابع، این قرارداد شامل خرید ۳۰۰ تا ۴۰۰ سامانه پدافند هوایی قابل‌حمل توسط نفر (MANPADS)، از جمله موشک‌های چینی QW-12 و FN-16 است.
این قرارداد با شرکت «ژونگ‌چینگ بائوشانگ اینترنشنال اینوستمنت» (Zhongqing Baoshang International Investment) امضا شد؛ شرکتی مستقر در هنگ‌کنگ که به گفته منابع، به عنوان واسطه میان طرف ایرانی و تأمین‌کننده چینی عمل می‌کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/69188" target="_blank">📅 14:30 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69187">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GxLnvgxdWEZya8LhVY7YsLY5xTnccbfY86Ie2iWhTIVk1Sw3vt1ZDMH8iktGYws4vIvU7qdvKUiOvCY4rdXEVIW62Friu2kCtbdT5Pemku9eT7yaKYIXudL-V5a779t4kIWcrBq3WIb1Yi3PsQaXgH5ZZxT7Ql6SD2A39dD-RRXBQTzyKNm4nTHTGpmzREJ7o5kUXl80iNSb5Sp2-xPtcRp85n7E7aGKkcdosBOoJpRnA0Yg5VHTfcTEmMd1ubLxLAxZL9-oRoV-o1CLeld9hLe_84DeLi566q8q3wZsVpnizcDut1ocTcf4fdiulu-4FZ5s4ylTUzelqyrZsoWNSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
عباس عراقچی:
وزیر خارجه اوکراین به من اطمینان داد که
حمله به کشتی ایرانی عمدی نبوده
و اوکراین هم
دنبال تشدید تنش نیست.
ایران هم قصد تشدید تنش نداره، اما
به‌صراحت اعلام کرد هرگونه حمله به شهروندان یا منافع ایران غیرقابل قبوله.
خسارت‌های واردشده هم باید جبران بشه.
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/69187" target="_blank">📅 13:51 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69186">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e78f023144.mp4?token=eu5Gqq7OovaQYh0HFMtW9-AcjWw2vC4QOWnAHmUBxvdWJJvKDpEK05DsP1JsZgd4Wu6qp_nJLDtIRudGPu1EK2cn77GSG7bNpj8wcyL5CjJHHri1Cvx-rrmceO9bg7jMqJ-i0dNdlfcfRnfE7GN2wRaQRdNu1HpNj55OP9BtB2kTFQmkJ--WrdzMTY19jO0SdfoSeVxol0d7w0Nr41i2rcFVqoesRtXlwbE-FE1riOIDQyPHD0KqqlKR9KIL47Yk20wbENIQE5bhVgFo3klsXATg3bqFlpdhGjNBnM9wC_dbR-uB0letcmXLisO18nutNfezbDVt8sFDjyPTtR2ouA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e78f023144.mp4?token=eu5Gqq7OovaQYh0HFMtW9-AcjWw2vC4QOWnAHmUBxvdWJJvKDpEK05DsP1JsZgd4Wu6qp_nJLDtIRudGPu1EK2cn77GSG7bNpj8wcyL5CjJHHri1Cvx-rrmceO9bg7jMqJ-i0dNdlfcfRnfE7GN2wRaQRdNu1HpNj55OP9BtB2kTFQmkJ--WrdzMTY19jO0SdfoSeVxol0d7w0Nr41i2rcFVqoesRtXlwbE-FE1riOIDQyPHD0KqqlKR9KIL47Yk20wbENIQE5bhVgFo3klsXATg3bqFlpdhGjNBnM9wC_dbR-uB0letcmXLisO18nutNfezbDVt8sFDjyPTtR2ouA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بسیار کسان به این سرزمین روی آوردند ولی‌ همه آنان رفتند و ایران ماند؛
جاوید و پاینده ایران
🫡
@News_Hut</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/news_hut/69186" target="_blank">📅 13:13 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69185">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CoukaaOySLfvNFrPC6s9Ub7TDhqT1eh10KgZhb9H3iJmzYGbCWvp-B0a9mqG9CVh2EKwCZjAokTHXnifUZUiz5px1mSNM9_hVzyq5BCdZUAAz6toAdpTt3jgjBmRhR6wFydwdS4ApcDE2QnJKzzauJbIoNcqdIULMAdDZgycP0rstOhBZAUT4GuWeaP0G1r2ESdo13rCWAFOx2qyeItlhHLcKtRPaBPbjkpn7IrAieIL1AazTb0EzTcFvCoHW8tX6HBU5xEJe-PJkTnuRAn0FTaDFwassahRIrRSZXgqPQgB2GA5VdnJXarEREvKErs9-Lge-lGUCc8673RCiyzyMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
ایران پیشنهاد عمان برای مدیریت مشترک تنگۀ هرمز را رد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/69185" target="_blank">📅 12:27 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69184">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HaQkmv_WugOctyGiF7mtbeMIYe-f38jUove20F2L7uMTQkkj4Vz5um24__yU_G7CcTvQiJ4k0MSKSI5oADIxNxAITrPYqoYfR7rRjhoJmI5vugN8x1wAc_69W70weUljs0wADwnBlh3BnSFFIbxYFNDhdOTStohdcF33jsTtGDFTwWLEL8ou0xgHDJYp1mIJH5U-s1bWfCBKcTaFIsVwpHdTRMsJHdtZ0O2ZYMiavEFQwScP1nBZiUbrSU4Boko_mJYjGGx3LpGNoS6T_rJVJDoVWevoWaqDDHcK9-SV21rkUs8nVLB0dqpWg38mCC2v5W3wE1AQr3fprZpDQ1BFKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⁉️
نایا
:
موشک‌های ایران، همسر دوم رو لو دادن!
یه زن اردنی میگه موقع حمله موشکی به پایگاه موفق السلطي، متوجه خیانت شوهرش شده
😳
ماجرا از این قرار بوده که هشدارهای یه
گوشی دوم
که شوهرش داخل کمد قایم کرده بوده، موقع حمله شروع به زنگ خوردن کرده و همین باعث شده بفهمه اون گوشی رو برای ارتباط با
همسر دومش
استفاده می‌کرده.
@News_Hut</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/69184" target="_blank">📅 11:45 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69183">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8245e9f66a.mp4?token=PzgqAL4qf-DZgNf1PNddetUR6QKDUDelDgbzlB0O8qYekwmjHwam7zy4-vXxr15Y6TVo8ZPTLBi6h-KQiwtsleiyLfenPv4aol0H8yC_88W6aeqcHN7MG-nOR4-hHHFb60bqSY0snZoIdumZzRxFKZWDcKWqZ1ufhMtXgl0cK0xzr596o3dyCteC0a9KoZjkKaMRefeb1N16K5kLXPi5c6rqgd5sgD86KSqS5AY94dxVcnlkuz9tf12kSzsgoKSQ1dWTRC5fxOA0gLXrSYlY4jTAuWHUqewbBZw4K7hMKJ8RpNypYOzGDeAFpIBnF8YITnqK8HmzK9o7OIv2MDBKyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8245e9f66a.mp4?token=PzgqAL4qf-DZgNf1PNddetUR6QKDUDelDgbzlB0O8qYekwmjHwam7zy4-vXxr15Y6TVo8ZPTLBi6h-KQiwtsleiyLfenPv4aol0H8yC_88W6aeqcHN7MG-nOR4-hHHFb60bqSY0snZoIdumZzRxFKZWDcKWqZ1ufhMtXgl0cK0xzr596o3dyCteC0a9KoZjkKaMRefeb1N16K5kLXPi5c6rqgd5sgD86KSqS5AY94dxVcnlkuz9tf12kSzsgoKSQ1dWTRC5fxOA0gLXrSYlY4jTAuWHUqewbBZw4K7hMKJ8RpNypYOzGDeAFpIBnF8YITnqK8HmzK9o7OIv2MDBKyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
بنیامین نتانیاهو، نخست‌وزیر اسرائیل، درباره ایران:
من نسبت به این توافق تردید دارم و این را آشکارا می‌گویم؛ اما تنها راه دستیابی به آن، درکِ درستِ ایران از این جناح‌های گوناگون است. به گمان من، تفاوت این جناح‌ها بیش از آنکه ایدئولوژیک باشد، ناشی از ارزیابی‌های متفاوت آن‌ها درباره میزان سرسختی ماست.
کسانی که رئیس‌جمهور ترامپ را بسیار سرسخت می‌دانند، معتقدند که «نباید با این فرد درگیر شد»؛ اما کسانی که تصور می‌کنند «نه، می‌توان آمریکا را بازی داد»، معمولاً خواسته‌های بیشتری دارند. با این حال، به باور من، در نهایت آنچه تعیین‌کننده است، عزم و اراده ماست.
عزم مشترک ما این است که اطمینان حاصل کنیم ایران به سلاح‌های هسته‌ای دست نمی‌یابد تا بتواند با آن، تک‌تک آمریکایی‌ها را تهدید کند.
به اعتقاد من، رئیس‌جمهور ترامپ در این زمینه کاملاً قاطع و صریح عمل می‌کند و من به همین دلیل، عمیقاً برای او احترام قائلم.
آنها باید بدانند که اگر به ما حمله شود، با نیرویی وحشتناک پاسخ خواهیم داد.
آنها به خاطر آنچه که من گفتم، در دورهای اخیر درگیری‌ها به ما حمله نکرده‌اند.
به عملکرد امروز این رژیم نگاه کنید. این رژیم به هر کسی که در دسترسش باشد حمله می‌کند؛ به عربستان سعودی، کویت، بحرین، امارات متحده عربی و دیگران حمله می‌کند.
این رژیم به هر چیزی که در برابرش باشد حمله می‌برد و ده‌ها هزار نفر از شهروندان خود را به قتل رسانده یا دچار نقص عضو کرده است. این کاری است که رژیم ایران امروز، بدون در اختیار داشتن سلاح هسته‌ای، انجام می‌دهد.
حال تصور کنید اگر آن‌ها سلاح هسته‌ای داشتند، با جهان چه می‌کردند. این همان چیزی است که باید اطمینان حاصل کنیم از وقوع آن جلوگیری می‌کنیم؛ و گمان می‌کنم ما در این باره کاملاً هم‌نظر و مصمم هستیم.
مایلم کسانی را که به دنبال ایجاد تفرقه میان ما هستند ناامید کنم، چرا که من و رئیس‌جمهور ترامپ در این مورد کاملاً با یکدیگر هم‌عقیده هستیم.
@News_Hut</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/69183" target="_blank">📅 11:12 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69182">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be2265e1ef.mp4?token=dknzyxWQvntbpwoiOyBOkn2_30_ktuA61BRbOkQN1HGExYvipMmj_MxYO9bnCU2fnov7eh6frR9Bo9ErFzRZm3w9dx05fFDf05eq30-4_dLk86crVYteDUdJGM_YZD72iGyp0KoPQN-ZLBWdoZzYrpFHvGZuPaah0LAqxXGFS9a_PQY9RPEqYAMj4JuP9yK98rUQ8sUcwBf4ARXHrdQjqHURq92PzR7imQLDDsiMvVWFr0RsGLHAqZVXHWF-nX322Ec5KQIONN3v1APlAnwN-mOB8gvu6tQZBGDlzUfNitv0Mzb8w5Ue3qhv6i7al7_mB_yJo7W3UlGcBNzwMMU0aQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be2265e1ef.mp4?token=dknzyxWQvntbpwoiOyBOkn2_30_ktuA61BRbOkQN1HGExYvipMmj_MxYO9bnCU2fnov7eh6frR9Bo9ErFzRZm3w9dx05fFDf05eq30-4_dLk86crVYteDUdJGM_YZD72iGyp0KoPQN-ZLBWdoZzYrpFHvGZuPaah0LAqxXGFS9a_PQY9RPEqYAMj4JuP9yK98rUQ8sUcwBf4ARXHrdQjqHURq92PzR7imQLDDsiMvVWFr0RsGLHAqZVXHWF-nX322Ec5KQIONN3v1APlAnwN-mOB8gvu6tQZBGDlzUfNitv0Mzb8w5Ue3qhv6i7al7_mB_yJo7W3UlGcBNzwMMU0aQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
این خانمِ باردار رفته بود سونوگرافی ولی به دکتر سپرده بود که جنسیت بچه رو لو ندن تا اینکه با این صحنه‌ مواجه شدن؛
شومبول آقا پسرشون انقد بزرگ بود که تا دوتا اتاق اون‌ طرف‌تر هم همه فهمیدن بچشون پسره.
@News_Hut</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/69182" target="_blank">📅 10:52 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69181">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZHIboMqbSdaJUsCwcYL-aPaXDMhuM-kdUDQeaY9ouoGbNDgMiVULfAL_-P-3Bdq_waxCS_df0ngMT8WSefuKDKpfBl5kXgcGfn8z2qfo3fRfCfWbW7_eIpp_WO02_bF8-xfi_DnhKf44QOzmI_3-afEz1l0KFKnUIROW7YMKCBekv7sfXWyGkDVswWitGEjS8v9ZaUltQk9LNYoXPsITAWr50aeHsLj-U--v5Z01HUhs7eXfeuMKZmY7yzxRTOBdMERVdnY2Ike6xtQZRoo6R5f8SFAR01cT5pBjJP6dTmaD8fOeUTgtSskhCPBcSIT4KHcW2FtJQlKNxZtPVfqiEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
نیروی دریایی سپاه:
سه کشتی متخلف میخواستن از تنگه عبور کنن که مورد هدف قرار گرفتن.
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/69181" target="_blank">📅 10:15 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69179">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b39375dc32.mp4?token=Raeuz3CNNWS4SA5fgAtWxK-5zgp9VFMsjLhmP3UCgTqM3LicPgcfn707AVDav7ZV-TuYHkDUdxQ9ZW-yyutZZLlU6aVP5VKfR6ysgBrTC7mAt279IDFzTIddp7JgrwIAtKbdl5Rw0p-n4eFq-8LeWg-LmRYFmac7BGeEetZ_9fjIfQS4LnMacsdU5X2BwIZaljIH67qrw0gGp7_9_R0s6IrQ11ffD2JrQk9EwJ_cNRqpEKl_Iyf2uKKd7w-qH6GlMs5BRzhRA9txGH20bcRV6WZSmENtYTAbGnUIbH7aG6anpuijALAMLXWNWijDcF9673sRJsByojlug5Ibh1daXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b39375dc32.mp4?token=Raeuz3CNNWS4SA5fgAtWxK-5zgp9VFMsjLhmP3UCgTqM3LicPgcfn707AVDav7ZV-TuYHkDUdxQ9ZW-yyutZZLlU6aVP5VKfR6ysgBrTC7mAt279IDFzTIddp7JgrwIAtKbdl5Rw0p-n4eFq-8LeWg-LmRYFmac7BGeEetZ_9fjIfQS4LnMacsdU5X2BwIZaljIH67qrw0gGp7_9_R0s6IrQ11ffD2JrQk9EwJ_cNRqpEKl_Iyf2uKKd7w-qH6GlMs5BRzhRA9txGH20bcRV6WZSmENtYTAbGnUIbH7aG6anpuijALAMLXWNWijDcF9673sRJsByojlug5Ibh1daXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
کاخ سفید پست جدیدی از ترامپ با متن «کار این جنگ رو یه‌سره کن» منتشر کرده!
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/69179" target="_blank">📅 09:45 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69178">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/305091e76a.mp4?token=kOLYAbR-SVj34tolyMaK1CGKDvonoZ1N4l19mIsU_BuHaKz3Ob6M_fKQKNIkKmjos-KzNh-gj2cQKFJnnCECfmHVgVua39tmyJlCOw9sHrjxj4LpJIVg6Ba8Duzm2p4YZcAXSsZkCzSbPAcsh2HFZRUbDO6uzs2nIPePinloPGKsDmtLNn0QItoWSJtDpZVngOfRRznFtibdFL-C5m6pFO-bTy2N02OOJKVE-2z2eo3QdKIwtuMTwq162ls6J0NG0tMjIwc3uChT7ccmZUCqnF_v4HH6ysILBn37GyEEC4rY65pt7BDYA7JBq3-AvVrAhYYkfToXigYq9l5AA23VgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/305091e76a.mp4?token=kOLYAbR-SVj34tolyMaK1CGKDvonoZ1N4l19mIsU_BuHaKz3Ob6M_fKQKNIkKmjos-KzNh-gj2cQKFJnnCECfmHVgVua39tmyJlCOw9sHrjxj4LpJIVg6Ba8Duzm2p4YZcAXSsZkCzSbPAcsh2HFZRUbDO6uzs2nIPePinloPGKsDmtLNn0QItoWSJtDpZVngOfRRznFtibdFL-C5m6pFO-bTy2N02OOJKVE-2z2eo3QdKIwtuMTwq162ls6J0NG0tMjIwc3uChT7ccmZUCqnF_v4HH6ysILBn37GyEEC4rY65pt7BDYA7JBq3-AvVrAhYYkfToXigYq9l5AA23VgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیویی از لحظه‌ی حملات عربستان و آمریکا به مواضع حشدالشعبی عراق تو استان واسط، که توسط دوربین مداربسته گرفته شده.
@News_Hut</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/69178" target="_blank">📅 09:27 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69177">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/74196ace24.mp4?token=BAAf0XnyVOj0Nzl3jsszGLuTaERNjanD-K4_kVPBHlQobqk-C-4XyKwrbWC1ruwKdu9WEKBIs88pcbvsJr49Oco4yZPaBzHIqwvN4kusyB8qC-T1KTFIywlXn-TbiJ70Lpba-VBRRXOwz8ZpWLk-xDv3sKYarMyrcc48kn5MbrBfE-SQK4FezFeHzGFo_nXo62iMub_o_la0W2RKb7xaKGe_4iPPvyMApgOr-A6hrp_1gme12QEfbTXIsHtDgyzffX0XJwWPQ1i3EmykiIHJiaWEmGg3XUB22amcXdmQVKU04KAMBeQTj86jauAeASE4AEC3Uf9gZpT_nBM9U_Xsig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/74196ace24.mp4?token=BAAf0XnyVOj0Nzl3jsszGLuTaERNjanD-K4_kVPBHlQobqk-C-4XyKwrbWC1ruwKdu9WEKBIs88pcbvsJr49Oco4yZPaBzHIqwvN4kusyB8qC-T1KTFIywlXn-TbiJ70Lpba-VBRRXOwz8ZpWLk-xDv3sKYarMyrcc48kn5MbrBfE-SQK4FezFeHzGFo_nXo62iMub_o_la0W2RKb7xaKGe_4iPPvyMApgOr-A6hrp_1gme12QEfbTXIsHtDgyzffX0XJwWPQ1i3EmykiIHJiaWEmGg3XUB22amcXdmQVKU04KAMBeQTj86jauAeASE4AEC3Uf9gZpT_nBM9U_Xsig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
❌
خداییان، رئيس سازمان بازرسی : بعضی تراستی‌ها خیانت کردن و با پول رفتن!
یه تراستی (شخص یا شرکتی که حکومت بهش واسه نگهداری یا انتقال پول، اعتماد میکنه) فقط 200 میلیون دلار پول مملکت رو برداشته و از کشور خارج شده!
معادل38.1همت!
@News_Hut</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/69177" target="_blank">📅 09:15 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69176">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">اگه فوتبال رو فقط نگاه نمی‌کنی و تحلیلش می‌کنی، این کانال برای توئه!
⚽
🔥
تو این کانال هر روز داریم: تحلیل تخصصی بازی‌ها بررسی فرم تیم‌ها آمار مهم قبل بازی پیش‌بینی مسابقات مهم نکات کاربردی برای فوتبال‌دوست‌های حرفه‌ای اگه دنبال تحلیل واقعی و بدون حاشیه‌ای،…</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/news_hut/69176" target="_blank">📅 02:14 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69175">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/316f36114d.mp4?token=s1VYhp6KdR0nNFei2Jz_lH3y6hnK9E4MtBRTUGhzpiiVD4vQ-hP8gNKTlEY2cGVfAD_cssSqch3S2fU2nPwYMEXxMQayb09KIh5c25z7REz6d4dArW-CB05MW7yZBpmP0pDYAkCC0lOJM6u43jVsQnOA6gxgYYcP1RKvjhv4gaMH2MAHGSSOWDnCtQ3gGKmQJ8aUUstE9P0D04xQ2m005bZqslpHwPV7DhSfBQxZiJ6do0TRrmqzOVOC8GdZCeUhAMkhXZ6_-K-VSOol1EX79wPLMP-PnWDPoMod0vPoWZ3Jl5-xHTNStVj5qmPqRYL1j6qWqZnqLt26z7raeO9ssA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/316f36114d.mp4?token=s1VYhp6KdR0nNFei2Jz_lH3y6hnK9E4MtBRTUGhzpiiVD4vQ-hP8gNKTlEY2cGVfAD_cssSqch3S2fU2nPwYMEXxMQayb09KIh5c25z7REz6d4dArW-CB05MW7yZBpmP0pDYAkCC0lOJM6u43jVsQnOA6gxgYYcP1RKvjhv4gaMH2MAHGSSOWDnCtQ3gGKmQJ8aUUstE9P0D04xQ2m005bZqslpHwPV7DhSfBQxZiJ6do0TRrmqzOVOC8GdZCeUhAMkhXZ6_-K-VSOol1EX79wPLMP-PnWDPoMod0vPoWZ3Jl5-xHTNStVj5qmPqRYL1j6qWqZnqLt26z7raeO9ssA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اگه فوتبال رو فقط نگاه نمی‌کنی و تحلیلش می‌کنی، این کانال برای توئه!
⚽
🔥
تو این کانال هر روز داریم:
تحلیل تخصصی بازی‌ها
بررسی فرم تیم‌ها
آمار مهم قبل بازی
پیش‌بینی مسابقات مهم
نکات کاربردی برای فوتبال‌دوست‌های حرفه‌ای
اگه دنبال تحلیل واقعی و بدون حاشیه‌ای، همین الان عضو شو
👇
https://t.me/+L5I8ulM6jEc2YmE0</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/news_hut/69175" target="_blank">📅 02:14 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69172">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/deb0Oldjvjavi67LMVBYX7qFf5vFqptdkdZyPtmQp6zOMjVFMd5t3DLGh7_wrpyjJcJ2MXHZBZarhOMcGrtTfNHwN9zYUoknKQMqip45wXTmO00xT9wg8tfmlrY-btFFpi13NS-l81_cLCrRLsl58yVebztmdUDJJmYrqaIAB5bFDja9V8i8ai2Dw1Yl5DcQRIRKBL93Zkt7DvgyNMwnkufygEFbO1ivM5T5a_nCySMk074-_KspZhkIFJsC8-1giQ4i5XFZpPZlT_O_D_LwEwMYrH6Fut0ndMA4AIh4nuvchAYzR4Ep9lo9YWIEabwN2O4tx7p_M0qvS0WRiZ68lQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فرماندهی مرکزی ایالات متحده:
امروز ساعت ۵:۴۵ بعدازظهر به وقت شرقی، نیروهای سپاه پاسداران انقلاب اسلامی در تلاشی برای انجام یک حمله غافلگیرانه علیه نیروهای آمریکایی مستقر در خاورمیانه، چندین موشک بالستیک از خاک ایران شلیک کردند. تمامی موشک‌های ایران با موفقیت رهگیری شدند. نیروهای آمریکایی همچنان هوشیار و در وضعیت آمادگی بالایی قرار دارند.
@News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/69172" target="_blank">📅 02:00 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69171">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W159W-8s2t9fgjCOAJdgxRHIj2SUgnD0FkQVOiVTK-uQ_nZlLTSkaXkm8kA0ZgjTTgFY4CRaUY9DKTSaPadhAo1bORFfXraGM3t4_rfSMn7bbyhTiC0XWeu4PrNb-qG9N4UOwG5NCgt45doWold_75x6X2MZmZx4_xhbJjnR08T7ZQKDlZHvD87RK5APj5TTZxiC3V8zlJUgYK0SMPx0GrRCyIrjr6XrWcpFl9GWcgjqaxBVni0AR7BTnK6jfNet3pauN-UQ2e7gzY7YrZV87Ga6s93C5qeZJZt834fB_7ZXGvRAItDSJ6Y4ZkbTLo4notlZNGm00WhtahzKEI_M-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مرندی:
ایران برای جنگ تمام‌عیار کاملاً آماده است.
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/69171" target="_blank">📅 01:57 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69170">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/58608400cb.mp4?token=K-N2Wi8mmONtARC1KweB7bNTtGHdN_l8NZKb4EDM2vQkFLnlqradru7O3KtfBHt12WAdDc9M2KWPuMF6o3E8Digc8hjN2_jYJ-6v15GLJuEmN3K-gS2xPDB8ppZ-ZTXslKyPwu36YaqBKX6ABD-h4QBti-pmQ_0UaYTuu7NPcfmd0vPCVatvjllATrS3RI9Pci36rwngGoL4SSywqQBZ_wWs9VeNMFAu2UaKWJqVul0Y90_Nmv11tu3Pk3qTVCAvZzgmCN1nB0dMKOcTKz6ope9H5utDss-lw3lX1k7Fj_OdJuHvEI0oh_ueKOy-sRTh53v6oG5OS9QGDcHCMRuMzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/58608400cb.mp4?token=K-N2Wi8mmONtARC1KweB7bNTtGHdN_l8NZKb4EDM2vQkFLnlqradru7O3KtfBHt12WAdDc9M2KWPuMF6o3E8Digc8hjN2_jYJ-6v15GLJuEmN3K-gS2xPDB8ppZ-ZTXslKyPwu36YaqBKX6ABD-h4QBti-pmQ_0UaYTuu7NPcfmd0vPCVatvjllATrS3RI9Pci36rwngGoL4SSywqQBZ_wWs9VeNMFAu2UaKWJqVul0Y90_Nmv11tu3Pk3qTVCAvZzgmCN1nB0dMKOcTKz6ope9H5utDss-lw3lX1k7Fj_OdJuHvEI0oh_ueKOy-sRTh53v6oG5OS9QGDcHCMRuMzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامپ خطاب به مجتبی:
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/69170" target="_blank">📅 01:55 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69169">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sKxZdV78LrlenmJkzs06aNZfQfWMyFI78qOkLKt2NeDSLaOdQ2ZRL-5g3leNF-ACDfkNtmkHj4LMVZhdzVuMS2RxSZC2VdP_CKDmDWqNr6Fdu9FQb9poj6HzlVZj5pX_o2uAOaBdeMr-3PpNcHia_oOA9nfEi-uFByjoB8lxhl54h1FVQYyXD0NJiy1FG1My-P2EzlJS8OFeHZ_hQSRfA4kHyUHcKjqRLpEtl6TuLfrZ0p_TV5le11O67jLwPeV1ZscNfQhthPLKfcvHsn2k-r0VK7Y31yrOICYsUCT9kpy7fUj8KxicBtxf8yxgYbU4cni83GD1LjxSJ4NHu-pouA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
باراک راوید:
ایران چند موشک به سمت پایگاه آمریکا در اردن شلیک کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/69169" target="_blank">📅 01:48 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69168">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🚨
لحظه پرتاب چند موشک از خمین</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/69168" target="_blank">📅 01:44 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69167">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AthdwTwRgVt3xgb-YfyQmjWPAv9G-iD_EO563pDu5h5L5WEVbanUUnICS4_R-tFqfCJEqIVODPiHtE2ZJ7wUszVsZ910a8K1zf4v8aF4aRMZBhfLA85UMwU_LSOBUutUuD8_18yIkyfRbfiFgDr6vsYpkkyQOrxITgE5scBq64LMAr3zLBYDCN-yo9HngQWGUr6fG4TtLa7-hURpkoTzMGu1xrlyC-YUKweC9UOBuwMqid1OgkV9NEqvewzpPm3K9yLwrQ3f9qiwyZQsci0LrXCQIZivLxYhNymE29S8cnGJ_Bd69yeIDvi2pvPurkDnyaFo6u7rTrjoD_7pp2eV8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آقای پهلوی در کنار یکی از طرفدارانش تو مراسم لیندزی گراهام
#hjAly
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/69167" target="_blank">📅 01:36 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69163">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/v2XWGJN-33l1A1JOLeC_P22uImhHXlnLX8T8Gq8Nyeyg4VTI30Tius0WyhenajG8l7ORdOzLitfKFwsoANOdX_tB6JsFREvE6w6-6xxcmm-qPYyFI8n0ifuQmOPj59tmojH7NCmDh9BkzcDlJYSKCROmfPcvGYyCdm1tUn0yRllIjHb0zZGHKjEV8jYOcUIBkv4iars6oWtIK1qh6q6uv8MK9EL-p10wMOtVjTO-Y50GAzbEXwnyrUo0N95MxzcI0iqrDilt05WlmvwmiG0yP80tTD8Baug4zIlCWAhMDkGjfR_7Y6KUo3hon7MM8WpLf-foeMDYQILRqaZ0razltg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/P9kQMGpKkbCrz7-NmnP0ElVpe9QwXW8izNY9Ktb65n2rxvsJMy62ZGrARaGm76Wipnz4jSdbQEpoA2S9o3bWumXlZkackrqBKSrUEcrxwZpv4euvYlogZZ6PXYaXdjx41QwslcmtDWa694RzLhiEiWtqOtHuBaZW9mR9yebNKp6C0JsuZ10iR-7Z1JiOicOIBnUeSpFjdV_vEz5DCvHc2RClsGyHM3vxFC29VYD_84QVM1-T7Md-YL4A-i9xapz2Sjs0JrvtHQ5QGhIVt4wzOV-worBzA58RJOdUJelCdkqGHx_OerDVBvtE5CwbVFgtFl1tgyBunc6h-WPOw5_JvQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/41f8819418.mp4?token=lDuvvwcFZA5nMWKM6yus7Dus7UeJyZqzkcERu1I1_H7k81bZufM6e7SFPtiSK87AOUziFlukpjHuzVojFQle441Vd5yurD-k8b5S9ZuWgoKABfjdvQwaF-YY1gZzjP3cWBtglL8hO9TvfPTEXRTJNF4SWUBUO6WNooDTRMF3GCGQT290qDUBzajR220uLHgNv7Kth9GK0-l20ONqEwhpWsTQEEAIO1WxYK_KSBBEWeS3Zn_Y1s0c4kyX_YyirciZqNLhm_auKbYKrqiLQ9ZcrLmFwreb9i5grpLaPTMe6DdM5utcVMGV8R5XvaJYZCbbSivqDVje9Qr1I64EV5MR8w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/41f8819418.mp4?token=lDuvvwcFZA5nMWKM6yus7Dus7UeJyZqzkcERu1I1_H7k81bZufM6e7SFPtiSK87AOUziFlukpjHuzVojFQle441Vd5yurD-k8b5S9ZuWgoKABfjdvQwaF-YY1gZzjP3cWBtglL8hO9TvfPTEXRTJNF4SWUBUO6WNooDTRMF3GCGQT290qDUBzajR220uLHgNv7Kth9GK0-l20ONqEwhpWsTQEEAIO1WxYK_KSBBEWeS3Zn_Y1s0c4kyX_YyirciZqNLhm_auKbYKrqiLQ9ZcrLmFwreb9i5grpLaPTMe6DdM5utcVMGV8R5XvaJYZCbbSivqDVje9Qr1I64EV5MR8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
لحظه پرتاب چند موشک از خمین
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/69163" target="_blank">📅 01:31 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69162">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/JYLmVZ8q2JtweQpFa4NGp7KOllDn_i7IB76iho2PmSq-BOAV8nhfc9MrTy_SKMUqNqy_CspY56c_UAoSivw9b1xvNLm6luXzQXq1UxxtgUdzJEgh2JWMELU6xonnxk3mrSG7KhBNXIDnT7obCwUND0s9B43U4OBSr2F6jg1DiPxeVZTFJzvxURNQiv1-r-R70gJ70hUV4i-ZK5lpdlT1sbNkXNq_bVtpTdFsmu7wEyQcIN_DnehLodutitWM96_OOXnOPvte0R5vHDOx9XIC3668XKJ2yv-6PcEqd2Xf_s-FNX3rmiC7MboPGVo9mpf7Ao70CjeTBq9ylXej1yB67A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سریع‌ترین مرگ رهبر و حاکمان دنیا در تاریخ پس از شروع جنگ:
1_ علی خامنه‌ای:
1 ثانیه پس از آغاز جنگ.
2_ هاردرادا پادشاه نروژ: 5 روز بعد از آغاز جنگ.
3_ جیمز چهارم پادشاه اسکاتلند: 19 روز پس از آغاز جنگ.
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/69162" target="_blank">📅 01:27 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69161">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/03145bc392.mp4?token=DPTiamp39NEy8sMY5pVPOi_NhihOPAIKHaeO5dPsCO69TGQhO2JEkGWp8Hdzt0vuJ4vn6FMydC3gju3OdxQvJHnKJh6lj49QtMNLHzwJ0g-28H8cv_9mQ0GmrZX36QXnpTzfcHYhxXtz3v0nZ_7-1RvpTLUvPDN5K_yPxYfOMn24o561UJuGpB_BrfillULRd-_6DJ-j1285Ys3eoFA1cplAdIwUsEu9ULutqgUVTtsj1SMC0qC6XRfd-wFk1vjLWtBoUrr_OmcH0SGuxHQIstF4ILpXyrolirSIOKBVXHSyiRgnROrDHoi4QT6kKmqi7X7rVkBt02oYcPGnLTEN9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/03145bc392.mp4?token=DPTiamp39NEy8sMY5pVPOi_NhihOPAIKHaeO5dPsCO69TGQhO2JEkGWp8Hdzt0vuJ4vn6FMydC3gju3OdxQvJHnKJh6lj49QtMNLHzwJ0g-28H8cv_9mQ0GmrZX36QXnpTzfcHYhxXtz3v0nZ_7-1RvpTLUvPDN5K_yPxYfOMn24o561UJuGpB_BrfillULRd-_6DJ-j1285Ys3eoFA1cplAdIwUsEu9ULutqgUVTtsj1SMC0qC6XRfd-wFk1vjLWtBoUrr_OmcH0SGuxHQIstF4ILpXyrolirSIOKBVXHSyiRgnROrDHoi4QT6kKmqi7X7rVkBt02oYcPGnLTEN9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
آسمان اردن
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/69161" target="_blank">📅 01:23 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69160">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🚨
🚨
منابع عربی میگن سپاه به اردن حمله کرده.
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/69160" target="_blank">📅 01:20 · 07 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
