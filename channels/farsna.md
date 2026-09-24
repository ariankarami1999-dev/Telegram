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
<img src="https://cdn4.telesco.pe/file/JnpM3YVN64uN6jPkbTswR9taA5G22TE8y8I3sAfvxEdY6j_c1uaoaU22rPRc1lOE2MZudya2H31X3V639shbgttLARl0clpa-YAHxYnqmSR3NSTKAH3ocM6WQgkZ2ViVd1mHZ1Kfxq0nGU_qumRrQ9shkixIMNjU_y-q2lqyKngGmyQ-rhsIPV_gTZexlhMmrodpd2ffcIpu9ZMN_ONxOfZxlQF7JLHVWUIlIakRDt6RI9wmx4fywRS9daTdvbDUvDKtcIaWDK4ipXqLFdJSDLe3gaqaOd7lnZ_Lw1aqqhpxL-MjQBMREYBHA5wKbrkZCdO2UtQUgP4Gs8wIbX80xA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.79M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/farsnews.agencyتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-02 19:06:26</div>
<hr>

<div class="tg-post" id="msg-464194">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e7c9509a2.mp4?token=jbSO1EhFSk6WraeqbrjNO8_WdGLfGwSzWxQMWjJuxUX3VDZprHRCMIQ1VsmIG3tSR30p8E3MlsJcIadcjVPo4LioswQKxDsgXkNBh340L3_lT4h7Gc_fzuE1m_t3vLFEBL4FBkPLl1X19ImdWQOumRfPwSMD6-fU7mYx7NOQeoEFIa6NoGX8NOFpHJnRafaylP3sh8xq_aolkIc2zYpmkNnFAKqbHNF6Ro6J_dz9SeAVBdl1c-LO9Y-rkSW1jDiG5MCC1Wj_JYgpK6ZkIABGa-VJrDTj8cF1VlRuTgTPxBoacvnrjVdbYqLU2BAt8B9odJuiMTLqPc6a89rPZO_jVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e7c9509a2.mp4?token=jbSO1EhFSk6WraeqbrjNO8_WdGLfGwSzWxQMWjJuxUX3VDZprHRCMIQ1VsmIG3tSR30p8E3MlsJcIadcjVPo4LioswQKxDsgXkNBh340L3_lT4h7Gc_fzuE1m_t3vLFEBL4FBkPLl1X19ImdWQOumRfPwSMD6-fU7mYx7NOQeoEFIa6NoGX8NOFpHJnRafaylP3sh8xq_aolkIc2zYpmkNnFAKqbHNF6Ro6J_dz9SeAVBdl1c-LO9Y-rkSW1jDiG5MCC1Wj_JYgpK6ZkIABGa-VJrDTj8cF1VlRuTgTPxBoacvnrjVdbYqLU2BAt8B9odJuiMTLqPc6a89rPZO_jVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیدار پزشکیان و نخست‌وزیر هلند در حاشیهٔ هشتاد و یکمین مجمع عمومی سازمان ملل  @Farsna</div>
<div class="tg-footer">👁️ 661 · <a href="https://t.me/farsna/464194" target="_blank">📅 19:04 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464192">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be55119aec.mp4?token=R2zsemhst-2Q7BWuh2UuJAAMOYUW1r-1s9Ijf2P5k-3Z9rLVhCZfNYM3zrCerFhLDMyxOTxTQPz-6jsfqfglqc4lQK-1oTKXD3nqnKvy9YW11tT8r3EX7N2rKSs8ikaC4kUeOdvDDx8EnKb6BNx_Yf23XXUL8y8xwvlZwUftAGp7fzupzSzin7EywWJz16ajFhz5rH-xGZLo4lQskQlSikf9sTcMIzkok77AEKT7z2D6a8FLTSf_85bVQBBUKIhOOUxu_7yq_K3hkaeaH5muj7DC716kbiGycAnBmgzfN1fM-9O1iPKLGIxelJUBAG4RzgGP-fRLBqe0ROAqubgMuw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be55119aec.mp4?token=R2zsemhst-2Q7BWuh2UuJAAMOYUW1r-1s9Ijf2P5k-3Z9rLVhCZfNYM3zrCerFhLDMyxOTxTQPz-6jsfqfglqc4lQK-1oTKXD3nqnKvy9YW11tT8r3EX7N2rKSs8ikaC4kUeOdvDDx8EnKb6BNx_Yf23XXUL8y8xwvlZwUftAGp7fzupzSzin7EywWJz16ajFhz5rH-xGZLo4lQskQlSikf9sTcMIzkok77AEKT7z2D6a8FLTSf_85bVQBBUKIhOOUxu_7yq_K3hkaeaH5muj7DC716kbiGycAnBmgzfN1fM-9O1iPKLGIxelJUBAG4RzgGP-fRLBqe0ROAqubgMuw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ورود رئیس‌جمهور چین به کاخ سفید  @Farsna</div>
<div class="tg-footer">👁️ 1.35K · <a href="https://t.me/farsna/464192" target="_blank">📅 18:59 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464190">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ycwu1R5x-c0G8WuLJIRDrQUkZ2RN9VDd5zeIpbEbtPviU-Sqi5iWz4675O84n2sVgXjm0Sl-IerwWqJq2LMIvtjaKXpxwAlGTXh6EOzdsR0byicXTELYH2ilm2BbOAB5JklxyLeBbOd_gtsaTkRJK81R30vZf5FhMig39q3cdbTxenhRWkVGxeP-6ABdYjF1e9bFvCjr0HcVMtPAAxeRAzn9NJWKibdewlrxTM-RRnVhL3-rP8P-xWw_5UkLNJj5LlBdL6_pMf-TaQZBjZ8NILzvzbMn0aB18Ep1KrWjNaMY6CUIehZna3Eej7eqRlMM060kWrg_BGcWlmf75_RXaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/c-zSXD5MsbwmWp2qU-p5GYgvLbuCY3YqWE4bh4x4Jbzwwllz3GF1zG-2k5kAFUILISEec5DKvAQiNtGv-IbxxLJYjaZ6JEQpHV2wjdUIjUCfTzPzmMizQuddYyW6JCbCLtQ1DuI3QuwiGAVUrgYH9hTcQj9TVFJRVQLDQXL05WT9Al4J2E91JTbdiVFr7h5vQ-8A-PjhxgMEiRW3GifjDiA8dVwGni9xm3vB6N6slI2vb7XE7mpKzeNCpR162wON194prDaNIS90kx6N1NGECmN50JK7OeGOp2wBUKtJYyvjUpMfgKxSHfL7-4HLceAjXUKYV3n9Q85D52QmW0dMAQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">حضور قالیباف در منزل شهیدان خادمی و نصیرزاده
@Farsna</div>
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/farsna/464190" target="_blank">📅 18:52 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464189">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f3c3356fb.mp4?token=DIJLMP4qTTW6DEhAOFauQUFXOZr-1GoYzrAHCnls6MhigosTlNYeVEhitpWRkGJWg7pLFaAST72Nd06igGKTEd8EFL3S712OAsq6cll3DbQj28pdv-Tdd1uYA3vGpQsZItO6M09m_A8474kgDF7oIxtduexDRgXo_-MUukCbGatCrzxEzu9kJIKagTb9nE1kIvqy-NSO8Wkq9gKAQ-wERbuTsVJb9-0aTr9zbijjoProDBce7w2EyCnDoujmfB_1pjaLxpOcqo2WcbhRYV1KK26XWJhR07hbBNj_dj-m4aXoKykKaQLKBTMJF9ih9_k7sq-CpEuBNLjUjlWa0XYr2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f3c3356fb.mp4?token=DIJLMP4qTTW6DEhAOFauQUFXOZr-1GoYzrAHCnls6MhigosTlNYeVEhitpWRkGJWg7pLFaAST72Nd06igGKTEd8EFL3S712OAsq6cll3DbQj28pdv-Tdd1uYA3vGpQsZItO6M09m_A8474kgDF7oIxtduexDRgXo_-MUukCbGatCrzxEzu9kJIKagTb9nE1kIvqy-NSO8Wkq9gKAQ-wERbuTsVJb9-0aTr9zbijjoProDBce7w2EyCnDoujmfB_1pjaLxpOcqo2WcbhRYV1KK26XWJhR07hbBNj_dj-m4aXoKykKaQLKBTMJF9ih9_k7sq-CpEuBNLjUjlWa0XYr2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گل تساوی توسط رامین رضائیان در دقیقه ۴۹
⚽️
ازبکستان ۱ - ۱ ایران @Farsna</div>
<div class="tg-footer">👁️ 2.38K · <a href="https://t.me/farsna/464189" target="_blank">📅 18:50 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464188">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df85455efc.mp4?token=m8quk2lwOkF_rqb9OJTY_V2c8hvSQyQZ-LXSNz65QSojqVcBgRaw0aQ-Vs9qWebdQEqkoMTJ9pBC21R3jM91MXc7Vp_1gdSOdGkxAFyQP7p9CdvlNBOS8T5zX5pdZOSQS3aA-brlVfWNdDB9ab-8eHvu4g09PgH79u9pQc9r6OwB4PO30t_wxwmEoKcvbsbMTCgfBm2vfwOflYmgP2Qk4KR3qBGhj4Odd0hXqQTjMSDH2wnSvZxe6sDXBDCEV_EHgY7aqy2ZwFyvGc6KOe09GsOFHXUxCXGRPXOfLO3LdToXheB3dzdJpLcTqv5APyn-y8d5_zXTCpwOsbk1tCkLLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df85455efc.mp4?token=m8quk2lwOkF_rqb9OJTY_V2c8hvSQyQZ-LXSNz65QSojqVcBgRaw0aQ-Vs9qWebdQEqkoMTJ9pBC21R3jM91MXc7Vp_1gdSOdGkxAFyQP7p9CdvlNBOS8T5zX5pdZOSQS3aA-brlVfWNdDB9ab-8eHvu4g09PgH79u9pQc9r6OwB4PO30t_wxwmEoKcvbsbMTCgfBm2vfwOflYmgP2Qk4KR3qBGhj4Odd0hXqQTjMSDH2wnSvZxe6sDXBDCEV_EHgY7aqy2ZwFyvGc6KOe09GsOFHXUxCXGRPXOfLO3LdToXheB3dzdJpLcTqv5APyn-y8d5_zXTCpwOsbk1tCkLLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حاج‌صفی سازنده گل شومرودوف در دقیقه ۱۰ شد
⚽️
ازبکستان ۱ - ۰ ایران @Farsna</div>
<div class="tg-footer">👁️ 3K · <a href="https://t.me/farsna/464188" target="_blank">📅 18:44 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464187">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cG1bUlHgOtl_W0iTrtESf6U9SbT7UFPDgfNEn-QzeXjgLsgLL1ZKp4LLTOzGsIiE11VvwnY8_WtNvh1EGzYtsW0_oxsm4mWKFTz8JA1CKOL7BtAzppLIMh7B9zjzybX6L-8_3_N48csVqFOpWAqfhcSagyBNRQEl-a1AdEgI-TW3cT01o9lfmJLVrI4XF0Q3zTu0VBO9azPMfQhbOtx99tfI-43Rwff7f6t51ecLIOmmqGfG8EPuUpw2GIKCYrOK4lReuG-A7j6krwwUBUyJSjaDR1Or3DPmOuR8iV5DZQsI3P6odKnDchjwDtpNeZD34texgMeCn2B5CAycdkICTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنگوی نیروهای مسلح یمن: عملیات پیش‌دستانهٔ گسترده‌ای علیه نیروهای سعودی در جیزان اجرا کردیم
🔹
سخنگوی نیروهای مسلح یمن: یک عملیات پیش‌دستانهٔ گسترده را با ده‌ها فروند موشک بالستیک و پهپاد علیه تجمع نیروهای سعودی در منطقه «الطوال» در جیزان اجرا کردیم.
🔹
این…</div>
<div class="tg-footer">👁️ 3.35K · <a href="https://t.me/farsna/464187" target="_blank">📅 18:36 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464186">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VU0nN_e8X-RNpSawdI9M-PGwuynAFNM8jM7mxnl-a3nIRqWO97YulfG25GJMeBn561RZKFWg9woOEhdNoAGuLctGwpsqZflK6OlZei6SFp04OTaBgabK9xzgnVo7SCtA8r-yQD-hzIF36Q3CPhYGt9c_PhPuNy8vugiqhwgYebVHxBb1kBSCub0jDl6weFdAklVKn6uxcWKDPIVIV3qIAGbd96yDa1HTEOjhj8LYo2NMR7MyGOI5eKdYYRQcLvUF4mLSp_qCbavJ3V14nTNUZsz08FsF7QwplEQrJQbnS6IccZrWWZ6rbeWiPWg893TSQ8Mc1NECoIRLJjb5ZHk7cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنگوی نیروهای مسلح یمن: عملیات پیش‌دستانهٔ گسترده‌ای علیه نیروهای سعودی در جیزان اجرا کردیم
🔹
سخنگوی نیروهای مسلح یمن: یک عملیات پیش‌دستانهٔ گسترده را با ده‌ها فروند موشک بالستیک و پهپاد علیه تجمع نیروهای سعودی در منطقه «الطوال» در جیزان اجرا کردیم.
🔹
این عملیات، اتاق‌های عملیات، مراکز فرماندهی و کنترل، انبارهای سلاح و مواضع مهم دیگری را هدف قرار داد.
🔹
مواضع و سکوهای پرتاب موشک در اردوگاه «الدغاغیر» در جیزان را هدف قرار دادیم.
🔹
در این عملیات همچنین چندین پایگاه متعلق به عربستان در منطقه جیزان را هدف قرار دادیم و اصابت‌ها دقیق و مستقیم بود.
@Farsna</div>
<div class="tg-footer">👁️ 3.38K · <a href="https://t.me/farsna/464186" target="_blank">📅 18:30 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464185">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ha3Bj7eZyyEh7cOrkrtpRJF96aIJF8OniWpmeLKRCftKLdSnwS4PZG8H4Pc3fy-no7pGx4r8FCo6KGtXbL6_ScaQB3npDKBc2o3onCPsCVbaHFaa0Z1W77gZC8vy5NS84Yxqe0D4FNt8In7lHBQZAUcuun3YSMf__phEd51osQWtDMQeQQKBA_D95jKLo5J9ghJkVzuez22X8NOpj01zjPfavaMCunV0ybvdIWDsTzMhsufln4tmW2fUQWOBG_9JQh07Pw7abCbSZcv0s34xfnZLH7I9-DZnkUdnLpcJ4V2NrFoJEhyfUMp0p0oc5CUzw7itX53jqYlLiNYN8vk6Hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس سازمان برنامه و بودجه: منابع ارزی مورد نیاز برای تامین دارو از همان ابتدا توسط بانک مرکزی کنار گذاشته شده و ارز دارو همچنان ترجیحی است
@Farsna</div>
<div class="tg-footer">👁️ 4.05K · <a href="https://t.me/farsna/464185" target="_blank">📅 18:13 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464184">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ded4f96c1a.mp4?token=LoxJDMbx8m7pCwPaB4mYXpH6OvlB3yePcX8cm9mH3pFgxfWitIeJaOAnk5b5BW1Dmn30GkhHYVccgP8QPg8V8IgzG2q-zVFJrFBAMhhjPsH8urZYb6Y9QMZYGo17NU-yQyUEys4DhEPOjFwkEx76eFf37OKPTXrT-EhNL57IaO5OxOINkPMxZ3JnL_r2PPrMMAndhjbtyKDqOFcnq65xP3oU_gGWPXzCvaeItpabm3dIjiX2q6ZeyLoZ9VtrBN-AmP2_qT8ISrz3OzbF0slczDoEafetgvE83L0knX141j_Q8Z_5tM76kYEpPcXFfZH_GHIzoATlMTIHRkVSMtPqeoV913dRoKEoSWIKxBisxsLLJML9-c3Ur2Gd7giW9BdJ3dOKq9SWemgB3v3sFhoSFuywj7lBb_fvMAr5q5dkRQq5gBfIY4rtArHLmQ909qlTXRHVTTJl9zFn4vqnW4G_YJfEY8-PZOVtKwr-ecH-yK6wXvTzFzzwSxE1sHMH0ITicwnDA5gIkcuMfOVn1wFUQqdg5mBNdno_yJwI3XtXxJz9n8OqB2kRURRvWNFCz5OA1MGAfag8q_vguxFdY7tOT7d-DY6rueIWDGWyY_FJdR-2o9gH774hcXL5cDpO3n85YjkjLyAUiua_5PyDZ5Ue87gonUC5IJKnTP7O_hjgBQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ded4f96c1a.mp4?token=LoxJDMbx8m7pCwPaB4mYXpH6OvlB3yePcX8cm9mH3pFgxfWitIeJaOAnk5b5BW1Dmn30GkhHYVccgP8QPg8V8IgzG2q-zVFJrFBAMhhjPsH8urZYb6Y9QMZYGo17NU-yQyUEys4DhEPOjFwkEx76eFf37OKPTXrT-EhNL57IaO5OxOINkPMxZ3JnL_r2PPrMMAndhjbtyKDqOFcnq65xP3oU_gGWPXzCvaeItpabm3dIjiX2q6ZeyLoZ9VtrBN-AmP2_qT8ISrz3OzbF0slczDoEafetgvE83L0knX141j_Q8Z_5tM76kYEpPcXFfZH_GHIzoATlMTIHRkVSMtPqeoV913dRoKEoSWIKxBisxsLLJML9-c3Ur2Gd7giW9BdJ3dOKq9SWemgB3v3sFhoSFuywj7lBb_fvMAr5q5dkRQq5gBfIY4rtArHLmQ909qlTXRHVTTJl9zFn4vqnW4G_YJfEY8-PZOVtKwr-ecH-yK6wXvTzFzzwSxE1sHMH0ITicwnDA5gIkcuMfOVn1wFUQqdg5mBNdno_yJwI3XtXxJz9n8OqB2kRURRvWNFCz5OA1MGAfag8q_vguxFdY7tOT7d-DY6rueIWDGWyY_FJdR-2o9gH774hcXL5cDpO3n85YjkjLyAUiua_5PyDZ5Ue87gonUC5IJKnTP7O_hjgBQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ورود رئیس‌جمهور چین به کاخ سفید
@Farsna</div>
<div class="tg-footer">👁️ 4.37K · <a href="https://t.me/farsna/464184" target="_blank">📅 18:08 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464182">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NXdBMoL-g7roi1jAmmYwCoQQb5eTTtMmERGgtmbOlFg0xinTcFmt1uBMLqGn0ZEOyobXf4JXsSirCboP-Ai0QPWPUNw2IadnZEyXKEfmOAGC31-P3582TLJG-fwy1cRzSJIS63dqXrCymXeQxc1aYacco2fKyYjwm4m0BX2U2ekQyQ5ajAIXi9sfomE6fNqP-TobpprHVz4mOB8a2Oo48XItm650DH8Ant1TR9P_vGMuSbAqXedCewKeKAfXtXksqb11YAhf99-cP7rmTWqHg4PiFLGGya6JzcURuCLxxOtJDtMjGWf9gZZfRoCq9_l3Xou7UX5Ef8OuOxSItbX9Qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TG04C4cEtf72cVcIjDgi9lrx0hZFSlvVuvulIk7EYZU_DnDjGGtd6oPnZa75UlmyXFE5fIt6xgrtSIoDJv1qih-v-er1NPa1l1_M-r-RzjrAZBckmckO6dvdhIAOUrDO5N4HJ48FK3SU35L8UVNtnkHfJCXLU1jVQPv5kM4ocQ5-EvFtUyQKWimDIMNpTgxEs-oHCl6vdyoJu5_gLOx2pu3JK6nJ1_lftJBxolX1ldM-b64SAqp2IHOBGZ7CrfaAMhLICrc5qR-3To1vbi9EqvNHP_bGmlw6VqoY9c_Fl1qiqIu90I1kA1yPy4QxP7PMkHFv6AUj-BVBI5haLQxVlw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دیدار پزشکیان و نخست‌وزیر هلند در حاشیهٔ هشتاد و یکمین مجمع عمومی سازمان ملل
@Farsna</div>
<div class="tg-footer">👁️ 4.36K · <a href="https://t.me/farsna/464182" target="_blank">📅 18:02 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464181">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">بسته خط ۱۳۸.pdf</div>
  <div class="tg-doc-extra">3.1 MB</div>
</div>
<a href="https://t.me/farsna/464181" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">بسته خط ۱۳۷.pdf</div>
<div class="tg-footer">👁️ 4.37K · <a href="https://t.me/farsna/464181" target="_blank">📅 18:01 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464180">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/31bb417428.mp4?token=Dmm3h4kVC_B52j-7FlqVRln6CkqGX6WDwAIPIN436ULo5OY-rqcrmClLiGcze_eabSxw5UZlU9qRC7JhufIgD1SRSfD3V81hc01O9Mr0u6Yv4Pv9P_7wINj-o29SYvsDn2vEKEZ-9DY31YowSptI_osu30Uiqxn2VhwaM9fb8i15gqCOkWJGtSufv7J380Te1NmK00W6aR2KNW199ah86UUFP8OB5j2ytQ1zYq_FP98IL7uQzBRWEg6nPkNdATxTzDHNYLU1xI5SYuImBfcdjBFlfr3auNQd-kWu5GUdM18QHkjEVjmswrMsRHpLwJHtuAnoxCdm4Hzu3kB8EJChyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/31bb417428.mp4?token=Dmm3h4kVC_B52j-7FlqVRln6CkqGX6WDwAIPIN436ULo5OY-rqcrmClLiGcze_eabSxw5UZlU9qRC7JhufIgD1SRSfD3V81hc01O9Mr0u6Yv4Pv9P_7wINj-o29SYvsDn2vEKEZ-9DY31YowSptI_osu30Uiqxn2VhwaM9fb8i15gqCOkWJGtSufv7J380Te1NmK00W6aR2KNW199ah86UUFP8OB5j2ytQ1zYq_FP98IL7uQzBRWEg6nPkNdATxTzDHNYLU1xI5SYuImBfcdjBFlfr3auNQd-kWu5GUdM18QHkjEVjmswrMsRHpLwJHtuAnoxCdm4Hzu3kB8EJChyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وزیر نیرو: ذخایر نیروگاهی در وضعیت خوبی است
@Farsna</div>
<div class="tg-footer">👁️ 4.69K · <a href="https://t.me/farsna/464180" target="_blank">📅 17:53 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464179">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">الحشد الشعبی یک طرح تروریستی را در غرب عراق خنثی کرد
🔹
سازمان الحشد الشعبی امروز از خنثی‌سازی یک طرح تروریستی برای حمله به مواضع نظامی در استان الانبار خبر داد.
🔹
این سازمان در بیانیه‌ای خبر داد که یک گروه از تیپ ۵۵، یک مأموریت امنیتی و بازرسی را در محدوده مسئولیت خود در استان الانبار انجام داد؛ این عملیات شامل مناطق بیابانی در جنوب بزرگراه بین‌المللی بود.
🔹
به گفته الحشد، در جریان اجرای این مأموریت و با استفاده از دستگاه‌های کشف مواد به‌جای‌مانده از جنگ، تعدادی گلوله خمپاره و تجهیزات جانبی که برای حمله به پادگان‌ها و مواضع نظامی آماده شده بود، کشف و ضبط شد.
🔹
این سازمان خاطرنشان کرد که مواد ضبط‌شده توسط مراجع ذی‌صلاح مورد رسیدگی قرار گرفت و اقدامات قانونی لازم طبق روال و دستورالعمل‌های مصوب انجام شد.
@Farsna</div>
<div class="tg-footer">👁️ 4.74K · <a href="https://t.me/farsna/464179" target="_blank">📅 17:50 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464178">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a005a31d8.mp4?token=aZoEJLc32qw4XDQcGG4pki-fmka2EWBBkmWaz7eTJhCc1nHESJkjLbe_36iCS3GXPXu81M8LsdbUZf7ADuAuYZqgncQx5DXXxkuKAPfQXa_CX9LXsvmWsTaVHbIBfdtOhk5_VHOGLxXWR8UK0bLiF7nk-KrfrXQXM9SpUvwRTzvDL31l2TUXyaup1zO7wJcSYBO-Kt4txce4MEGS1wVGDA_asolKjfKsce9xPDNfUyij8F73UhZ2bXS-mPgsh-2fQbQKqdVd4W_3McM62-ttHhuHIsmy68hh38sJVbekq44cucKfoGoLaD3cczmXyDC2ZupcdjfPDgPgvEn2RMaIKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a005a31d8.mp4?token=aZoEJLc32qw4XDQcGG4pki-fmka2EWBBkmWaz7eTJhCc1nHESJkjLbe_36iCS3GXPXu81M8LsdbUZf7ADuAuYZqgncQx5DXXxkuKAPfQXa_CX9LXsvmWsTaVHbIBfdtOhk5_VHOGLxXWR8UK0bLiF7nk-KrfrXQXM9SpUvwRTzvDL31l2TUXyaup1zO7wJcSYBO-Kt4txce4MEGS1wVGDA_asolKjfKsce9xPDNfUyij8F73UhZ2bXS-mPgsh-2fQbQKqdVd4W_3McM62-ttHhuHIsmy68hh38sJVbekq44cucKfoGoLaD3cczmXyDC2ZupcdjfPDgPgvEn2RMaIKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حاج‌صفی سازنده گل شومرودوف در دقیقه ۱۰ شد
⚽️
ازبکستان ۱ - ۰ ایران
@Farsna</div>
<div class="tg-footer">👁️ 4.75K · <a href="https://t.me/farsna/464178" target="_blank">📅 17:46 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464171">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uDuB93sf_uU-xha5U26dOuVfF_Sm5haMqMrcUCf6Lty4SxoPZeGym4dpfWEORHIXZzUFPW0RXj1VNM3EWhRgK7B---AfC2u49BxQv33ep2vjcnbKpCYgXaJsRYA65peQfKas8cqYzb3rigtnpIh9Y3hMgpRWN3SfpmfDpgKACEUToD-tac-cuBhl3IpURwBs_a4gKcnS1vlXg_wQvaZVieqtXdbQ3KZTOLSP7DGQ46qPtQTgGJOKjkniit_da_xhZfaCf7nOzR9HsTrrHmR4ohRsUjkCpSEuIAsOlDHxtPguk9MfV7Klb7LNZhIchGI6e0tppJzsA1qVv9CfG_kn0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OXPBeyhQrlol4m4QNYbVnOxCe49DezhBUJmM-n7rn-mCEJNvqdmKbWD58HIgeMEsPwzAIg1hT577Sh7Ys0yyDcwhIM1s5QlEqhqh6gpzqT-bWogkuMzDuA5Vs42LRwRy_IlLC0ia7iv5ciTkancnQ-pm0-CZA8MLeO_0S5jI4uTyJ2tf-1t8zwx-2XlOCnsUiyhgqwaatdTRv_POlTNt_lgHlmATP3png3gBpYjWx-k8VZ9JOLMwiqrd757Toof7z8-tEbgrGc_Xp8fu_D3oOw_Q6F9OH4ONG2SaJaZ26woewggAakINVhXTemHnKRGa3SlU2sZCuOHALZUJWBGG-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HG9c0IAQg6-3sMOq3WQTd9lSgZEZQrEojwYc_z-w5K4Nzlm5s-ZI0q4hx5tl47uIhfMwetm9LM67Yy6MENPNelwpNuksYgDUnu6voqui8r06P03r-0-c8jDaql-z1qnzlFb_OysbAIL7DVT_6Rve5rCzPMnBsxcUsYhQ_8Gy3k8BM5rAIrL3FAxjoW5xW1h1HNYZCw07wquQ2ONCdk1oK0e56No4k3VGYemFSx6d6U4f03papwcYaQRsvHwMLyWi1AlKhF8rHWEyj2A6yP7MwmQnu3v9Z0exw3RL5uGcCmYOx2DVA88p4URGD9WQs6Unyf5iVXwqrZK1kC7zTpAeLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eqeOHrWGRIPJCw7KwyqzQBqmd7ITyUesDUKHqofzLqjj-E4SsW1cq3cixLl1i4hzpEPcFf1YWnPjSJROv7cM2yfFf3NW3a-8hObP8MwRoxniPWPWYQVJjzrIbHNxHDkJswIl5sLPeTvsoqQtj_gIm9wiRQFGP3UuDspKrA9JH3BdgN6L_qSPq2dcqQtX9vya2pou5FLdVBrrNDj2NEkEH9XG9YK-2kDwo8-t1fNMUq0_7vrOR5PMRVkYTN-kno7vGLn6TFuD7aDBhPWC0yNT4Ru_fWW347EZoXD6OuxakwiCBgmaf-8cZhBp-wds7I-kNUH04zNiB0rQkkDP7Yv65g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/V_JTluAu0Piq3m2FIdSl7TxK3x6EQYKIasL610W39mkkuEsnAYSIvsoHYNdEphhfXYLiTwcRO1x59Ggsz4Ejfbc4KMqPfRnrxinj-4DCLwdwJcDn4jhG0LDgK9TsDYfce0uarbnwMz6E_SJdlrYyWUnMaJQVZ89n28VuCCVAfytvTdGxFCObpkMQEDpC8fyb4kZrZo1MgKCRYOXGWAvIXPR9v-7KjL0lTxSgfpStpsk5mbn4kjjpM3YM4rrTs3dM_KmgiGj59ujIrePAKRfM4rZYP_4-RKED3TwNsOZ3xLMxPeGwMbF9f2JyNjfNL39WhVCKBKyuVlSYda9f-PT_qA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tG_sHeyR63R_VQwjLNt234PYYsuRaFfAxvriN3BS4_CAKSIoGJG25ZsGEPjsdK0hZZqIiEEfo5FEjt08hC-bgCa6QdzPqk-CiYdQfU6Kjz8OBY_3iGUw_cIuR1T-z2AjfS4jSXEAUpcN-FdUNKOWFilov0tc_mFQZXXRHS9NZ8QOvlm7DJx0kZ9iFu2syvfaJX_VJ3CVZe1kyhMQvSibU396BEREqQpNd5WotJ9W_G-XAK-kxr_Bv2VItxKsd23aP5ERJ64i8TQvxaJQayxbFGCxY3S_F6YhrjwaKewOP6NJGkdhbhXsR3M_AbLv1gNobQkDp5aauE3QOcf0fDUdgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RKGs_SHGDa8Ol3p2XeoRLK26DOkBcSLBRy-1O_BguUBYNJSjLljJvZMa0KVAKnUp30doySu10B3Av5kK9qr_EGhcAVvxEBDqXtobLbP8JSonfJp508S4m2FQ7KkBwB2vOaSYwtfyRv3GnzFLSNxJBNK5YTc30rFMHPNwB8NNdgpY16JmdBJi7ZsAkcCLZw9AiJQ8S2Sah_vwKS8ED_dEeSZdVArcw6zPWlfohfp_FJZPszTTGEWbYYdiKQgQL_PzIwbiXdZNdsu0SrPt0t-TI9SBTl8_TB8f-ACuulC-Qw2tZFJn0DuZAlzW9QDlITqgG7h6VxbG8MdUXF1omH4Vzw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
مسابقات کشتی آزاد خردسالان در همدان
عکس:
مبینا لطیفی
@Farsna</div>
<div class="tg-footer">👁️ 5.04K · <a href="https://t.me/farsna/464171" target="_blank">📅 17:40 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464170">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lh8D6DwtWbbFayzZrJvpVTghqtU23cScwOjb_KCwd2j0Xa-Kn06vvj9EFdGEskGOYdl-1c00pEWfmgUPNq9dhwd8MC_GLXu7N20-qpO3h0EDbOdA4IJYuETfErDs0tYQSmvmMMljh6xEsJ5FDbMU4lxeWXYS4YV3bQXseagjH_-v2MMc6urdiwJQJDwWWPkVDlhoCatPIY5FxqIkz_jGgMktBr0Z0YOwoxMhGwaHyPuaftWJlyd8Gh2Md9vDTHgFcG9XQ3_ZKfT7-pN-P87Zd2aZIao0f91P03RkCyS_Mu2rgtjB0F0msN_09P6GimqMcYB-z9k1jaRc8RlhWexPSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«کوله‌ات را کامل بچین»؛ پیشنهادهای ویژه همراه اول برای شروع سال تحصیلی
🔹
همراه اول همزمان با آغاز سال تحصیلی ۱۴۰۵، کمپین «کوله‌ات را کامل بچین» را با مجموعه‌ای از خدمات ارتباطی، آموزشی و دیجیتال برای دانش‌آموزان، دانشجویان، والدین، معلمان و اساتید اجرا کرده است.
🔹
این پیشنهادها در سه مسیر «وصل شو»، «مجهز شو» و «مسیرت رو بساز» ارائه می‌شوند، از سیم‌کارت‌ها و بسته‌های ویژه اینترنت و مکالمه گرفته تا تخفیف خرید مودم 5G و 4G، گوشی‌های به‌صرفه و فضای ذخیره‌سازی ابری.
🔹
در بخش آموزشی نیز تخفیف‌هایی برای «آکادمی همراه»، «فیدی پلاس»، «آی‌نو»، «چی‌بخونم»، رویداد «کی‌بُرد» و پلتفرم «کدیکا» در نظر گرفته شده است.
🔹
در پایان کمپین نیز از میان خریداران قرعه‌کشی می‌شود و ۱۰ نفر هر کدام کمک‌هزینه خرید لپ‌تاپ دریافت می‌کنند؛ هر ۱۰ هزار تومان خرید نیز یک امتیاز قرعه‌کشی دارد.
http://mci.ir/-GHNE9B
@mcinews</div>
<div class="tg-footer">👁️ 4.42K · <a href="https://t.me/farsna/464170" target="_blank">📅 17:38 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464162">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/udLAj9uw1xAOvJWgThMsAfKlTz0nzcb4PCCZUX2e50iPj9NXo7aUe-MdK5tYu6hTs0GphXHN5cgA_0QNWg1UHJka30Kh3LlyaJS5NG5biTXMiU439wEoEectP2tVsIzz9fzP7KqWwNth_Y-DjfzreYVozntEmJvfY4NhpKxqXa2U5v03zg1w5SLjXTwyB_HQ_-y1Uab6LUaxIlEOJNSwqbf0cV9zJ35uL8LjUxEsbzHB9RnO7JZmkQKreMmqCVdhwtjtBhwaMVMJGASaROFM4Qk0ZHcacn5RAjYARhvBiuByAfjBZ8uzZxr-nIyt3J244NfV2zbltBMmiCWGSznoyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/p1XJopN10jgS-x0KYN2E5kGhMJU5SlPhWnEZVAv8AggdoDEEdqvPd0DjCZqI6wI3XepuG-Hyjb4P--Zh1HvFfQxk8vq9oS24WBhQvvJS92aQuZxZIZh_Av5jxgZZ5l8VVFKn0e5Qq51KPCuJsUUdyzh5DujFPQKI-O6T7P6j0pxPLA1rczDuyFoS1YNZlz0FuC-51CnSAogAx0czkxkdA2DDCO5f4RTmfwisdVG0_vltPERBGMEIjSTDaxBCLONA7RBgfVzw3FpJq8PllodmT0eLBqX61MrqTW3M0dZlmCFYgcA6tFuE7iw7aodJzS34OKWMEWHm4RGsqnVIxkAQGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Jh6M6qBdo08ggHbBGYiSCp6hXSqXDmtDunc1K7Nqu3HIMc86tqcyz1sG88S8x043lWckk5Ox6UAqRufz0RNj7b5hU-62oeggNeM6JSyiBRxpxlHaOkywh8jvURFZezjiGO31_VaDwu8fXoNHJVVMVAfYjceC8ySfqgkJNoyUMW6tw0Tde7_hLzIQEOqfJrK07GErEEdgNWJgKBnq3uskYK-MLiUvWa4kDn2Buf2-neBFppzlzZ90RY2Bs5izyefdGK-MsgDDNCC5J3Rn0Z8Kc_4m1N1Pl47XMWi1V6qRlPT_LFxqr6nZ-iSzHe04zIxX8ue98hlM8BBBf8q2ADoI-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Y-TH02axlFNOanvoH5g_90qRfExaRM-jdb6wj9vwbNcwdEbrm5CZPbot9NwiVoTEmcofd08EIlMUOjGleFyVvMz1r6dLYoDFUjtLEgZTJdk9gvkEtocoV-EriWOdIVdl--0K3_27un5XtCn4PDIHXo7UfRjs9qRzb3IwE4siZrhEDU7kcrznV-fbQxUG6Y9ES9oiqlW8Lk1e8qP1_hqtUH4bySzKyhz622s4LEHsxZYK8G-wYAul-Osa5nUH9XvKrbMN-yjHG6S_vOkP-AsyC00Wdtq6ZzEegPYwbzUvAnGwI8HSbkpJmTIUAc9a4SaWPI7zBtO5FUISkzeri3Hq3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EUd_9xdrFyi45DN3jIZEjyneGWDH1NY7VxfjWptSqBConrxpD2f1ZHJ2G6S9_OHBNYLtSlDIUTY9xsyuvYnHzR-L6CnZvS481t24PT4Ihiw2T-HWld5Wavq77Pk-sSmWeD-JZOITZ7daeLDHmUqizYCZocCjCjkzr-I2WNSzUWctnmZ1h2xkA2oJMHS2_4NSkqrkI-FlqWdBrRqWT5awTbyE0liwkMks9ymj4tDFFtZrKxlbgujhurb0C44uAtAG47Myp2la66ck0vQ3yvt07UmxDIuQOJ7YBiq9vpgZuMv195joxUnUGG7kGNWzktMHwv88MZHZn7mMWrGhEWbgvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Oym_pbplSDeDip9mVjBARbemtzp2s5WNEFoCYg8YqEJas73TkXoueGU0LXjnaFD42yyOChA4qek5RNY1jDfCsX6tjmZyJ-s74B5uG3xnP7AGzfllbCdRoxmHzsRT24Z9baVC7X0lROQ8-rkmGt7J2OalKoTgmDCOsC5wtAaqm9f7S7qUkw8aSepa6D492DvVH0JD6qiRQdM4I0ald2qx51T_n0lMQaJ6A2rgwnl7Bp1g4Bm0ZvI4Zfo6Vl19ZZ-uZ7Hb7wHJQHF8xQhTRS9cUkIFLJxiMUACGKPRYZ2pBlA20NKqoErydhQU1nbgX90egLpzrniRGPsrpm3ndIjWPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nicfMOM-mYdcFTedsF9wdM3qc1-JeoTLwPLWpB92AHTN8shRKWh9ZXIHM0ldPEB_DyBac0eul3p2ySa1SNf6A6UCUhzpTT-xgJuVYcH93XJkHvb8qRSLPp3w3ts36ONgYvPlW-ierbpmpyBOcixLV54ot0niXJ_g0bV392ObNIRqXnpZDMhA9Rz0VCbcbZjt3qub47FfmgO50Oj4q_lwaCSShCfGq-FKDOeHhin0hFTLEwinoO0dXaa2V8rHkIMRZ29Cl0GQFfXkOYF367ePsFApkdghv-fyTeSeIffutxgy0Xx9D2BfLqfpu0AVjfRy2dbUzoGrU-hBWoEadJ787g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GHNNdxJLKvOU4cDopMR1UCgA96W4x_uOIIQi7fobKU58AIo-uiDbTK5-3hVGM6huWeta_dOMzivuvceTU7kdOH5mfRKuNe_lStRJkXm8HXJTSA1gW7DlMQWGIbnMc3fuhiWXeAbRK0P862t4rp_1LRfsUPAmYDgo5y1gHNVunQY56RASVg-8UjT7MSdTqh3g1_32i8oXxtow96QuO073tAAJZHBXm8pxkQ2YfqwdozX8io2C538TXVJsmIZfzPnD4Y50x7BIZ8etrgQfgEvRBI5rdskfD9CeUZ0S4autQS9cekhnMlQ3E0OQwCuwYQe1vIyJs854wpoNTy5Wm1PzjA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔰
فرش قرمز مترو برای دانش‌آموزان
🔻
به یاد دانش‌آموزان شهید مدرسه میناب
➕
@metro_farhang</div>
<div class="tg-footer">👁️ 4.01K · <a href="https://t.me/farsna/464162" target="_blank">📅 17:37 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464161">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-footer">👁️ 4.21K · <a href="https://t.me/farsna/464161" target="_blank">📅 17:36 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464160">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/01b9af8605.mp4?token=Em6rq8ceRPtUBS3fQCr6Xb2CZtRa55rrmBn374Iu36cCi-k9SeBb8LeUFizI9TylTUX7Zcb-WTYVftrRDec-GJ1ntdadAuC1nwTzQpmlGRiJgBVuM7KU0CEsqKpqVXYvjx2ky9UAQBXJaQKDO6fcSHKwI26Ryh46NZ-zHCXCm7Hlj1aBUztitGXZF5if236R4_36e8bE1TJ5SCD-MRt1L2cMySwhWclkRxBjeVFmdHnWx6MndohRhLEXy-AmcLc1DSEC7jUxY3Xr-dK4rCsBCaRtq9a6v4LuOaY-FNlrN3yCijn2o6YRjZyOqUzAclLeFdvegudsr993CB_REC1Ilg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01b9af8605.mp4?token=Em6rq8ceRPtUBS3fQCr6Xb2CZtRa55rrmBn374Iu36cCi-k9SeBb8LeUFizI9TylTUX7Zcb-WTYVftrRDec-GJ1ntdadAuC1nwTzQpmlGRiJgBVuM7KU0CEsqKpqVXYvjx2ky9UAQBXJaQKDO6fcSHKwI26Ryh46NZ-zHCXCm7Hlj1aBUztitGXZF5if236R4_36e8bE1TJ5SCD-MRt1L2cMySwhWclkRxBjeVFmdHnWx6MndohRhLEXy-AmcLc1DSEC7jUxY3Xr-dK4rCsBCaRtq9a6v4LuOaY-FNlrN3yCijn2o6YRjZyOqUzAclLeFdvegudsr993CB_REC1Ilg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اولین حضور فیکس درگاهی ترکیب تیم ملی ایران مقابل ازبکستان
⚽️
بازی تدارکاتی
⏰
ساعت ۱۷:۳۰  @Sportfars</div>
<div class="tg-footer">👁️ 4.6K · <a href="https://t.me/farsna/464160" target="_blank">📅 17:31 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464157">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/blyspS5RvVS28FfBn19hf9EwlxMJ9Hl91kp1kAGbLsXXBelSjFWfi_5MlYsHaNm9UyhWLAQYaoLwEVEhiuTC180QaBwr4WNnyCpwUJE10RrBmcawSQgPP3IODd9NiRnjbCFcPVMGb1WO7KBI7C5P61g0tX4C_HwV6uFof9ZgGmCR6pASQ0znpc2TXXWoWDXv9uSkTkweDQL26Y_LWigPLkHSRzgi2Ry3hURVoD85qGrnyt2xk7PY5zyhTSwq_c4UPdp7HY29-NCj2ybklWUzr7dR8qOvRESw1WfwRWHAR342UKGLVE_Iym_jSDJ0dcefEYQGQCG9ZModibcKP07iZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OIY-JBQV_kViLM6YPuBu2uWp1l9gXorTol9yPSyftNFwo7Ne2U_rFUZbDlJHxT5pzPNTzBzL7CyGbafz3Ywzx5MjtoPWoyBTtBz52G3wu5D4mr18d-7F_ubvLUTStKFw3a-l85Vao0mcMJZbYjHUZ0Sxn9E2nWuWbo_2QKWVhOrWR6GmRgbhqpMlMux9ZTQaYlNyAAAfuTloB1KISrX_3-1h2BHBVQZhpfOgu4Z0CFc9C-KZkE11078wPl53SWpIte84KRuf7oAkzaqRJwKc36CdBAMmJYlYruNA6sVBtNwsnpMezZJmw7aN3_jFq1c1s71AI-4HucxcE1cDoPH_ZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WR_YbSUR0x4Qq3uC26q-7cncZjxSDRTCFZdmthp9iQqapKS6kTYPwp08DBdoUVlxtyI2CMthsJfX0e_Yee47dnFYOtph9Qnw7E6okH126oVvU9z-dmXLgM-VkIyQtjMmdVkoZJ8pDr6nbNOeJWpR-twHzg-RgRhKlQ3i5B6w7wSljPHB1wKzyEHDzriI4Qb235VsX5WBFYz3Y9mLnaNvHV1PRTDbep2FEbsPHcsDSE7HsVcIZ931SvYKqBJ8h1FtEE9gpBQ76xLwPJn7Pn6pC5_jBECJY-ZRAbmHPhNGBJP4x1GWS18VPhCZ8a-hOlmIYPfR0w8kA9Q1dGnRkZbzsw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دیدار مدیران ارشد رسانه‌های آمریکایی با پزشکیان
@Farsna</div>
<div class="tg-footer">👁️ 5.28K · <a href="https://t.me/farsna/464157" target="_blank">📅 17:28 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464156">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1520ab7287.mp4?token=X-8fEOtO8r1q8xmQOMIcFnvPDXydnL4aGC-Iokt3Y5c9LTHxtzWwNUXBMcTQjHjWDzKdPHx3q5EpHa5rip1sEzsqlcbmzsFr1e6I-VQmLSqOjXa8_sbE31Z2QQLG2vCjqoT8_xnOg7e2NI2UJu7R3IU8g4w6KvjHNi2dFg2g9NXTNhXCp54RFluMdBwE3G_13WwdiJyEO5Pn0dFKGlb5ImeV4PK6N0rx7RiU5cmTZBi2IQDByKkho44qGOL50vSaRIDGvg31kLspvGjFX3y1llZT-B7NY_2661Pun0ARluR2AkKmtQJXHhML-lbmnnuT94JYtBMIKU8_FyechnC8ng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1520ab7287.mp4?token=X-8fEOtO8r1q8xmQOMIcFnvPDXydnL4aGC-Iokt3Y5c9LTHxtzWwNUXBMcTQjHjWDzKdPHx3q5EpHa5rip1sEzsqlcbmzsFr1e6I-VQmLSqOjXa8_sbE31Z2QQLG2vCjqoT8_xnOg7e2NI2UJu7R3IU8g4w6KvjHNi2dFg2g9NXTNhXCp54RFluMdBwE3G_13WwdiJyEO5Pn0dFKGlb5ImeV4PK6N0rx7RiU5cmTZBi2IQDByKkho44qGOL50vSaRIDGvg31kLspvGjFX3y1llZT-B7NY_2661Pun0ARluR2AkKmtQJXHhML-lbmnnuT94JYtBMIKU8_FyechnC8ng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
معاون حقوقی رئیس جمهور: پیگیر پروندهٔ دانش‌آموزان میناب در مجامع بین المللی هستیم
@Farsna</div>
<div class="tg-footer">👁️ 5.5K · <a href="https://t.me/farsna/464156" target="_blank">📅 17:12 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464155">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🎥
۲۵هزار بستهٔ تحصیلی برای دانش‌آموزان مناطق ساحلی جنوب کشور به همت سپاه
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.13K · <a href="https://t.me/farsna/464155" target="_blank">📅 17:11 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464154">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa0b4f1e70.mp4?token=PJNGVpwvEYzaqXnlYK6h-hPMcZav-H76zjY06T55MlJklYtMXt0ildItPup9vvVF1ndxVPrQi8lBJQmycKkG1F_U36_c2b-I8RU2k_onm8bw9JCxY3TQ-eB6LCqPMz3mL8lhIj7b3c6BUwFRKxUCK15fL-5JwZoD5vEdUoS1bVFTtAVUY30SPowADCyTURisXCH0o58WfeWvr6CZZxIFPJzW4jThzVLSJ3A_Bfc71laFqX_EdF3nb-CKcalyJDMMo-HNsfxnmQjV2_CDJW7hTOzmX2Z9Y4e8CkYqLA2-pXYvD7uYqF0gWd4Pb0sk6r7sVfEOjEpM9ew7f-UxX7lwUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa0b4f1e70.mp4?token=PJNGVpwvEYzaqXnlYK6h-hPMcZav-H76zjY06T55MlJklYtMXt0ildItPup9vvVF1ndxVPrQi8lBJQmycKkG1F_U36_c2b-I8RU2k_onm8bw9JCxY3TQ-eB6LCqPMz3mL8lhIj7b3c6BUwFRKxUCK15fL-5JwZoD5vEdUoS1bVFTtAVUY30SPowADCyTURisXCH0o58WfeWvr6CZZxIFPJzW4jThzVLSJ3A_Bfc71laFqX_EdF3nb-CKcalyJDMMo-HNsfxnmQjV2_CDJW7hTOzmX2Z9Y4e8CkYqLA2-pXYvD7uYqF0gWd4Pb0sk6r7sVfEOjEpM9ew7f-UxX7lwUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دیدا رعراقچی و وزیر امورخارجهٔ لهستان در نشست مجمع عمومی سازمان ملل متحد
@Farsna</div>
<div class="tg-footer">👁️ 5.58K · <a href="https://t.me/farsna/464154" target="_blank">📅 17:08 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464153">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ba0NqpydoXxurPUAiXPmRH5Ei0RX-BWjZtxn-ouHeXzisFgcBCAhwJ5S7Ejh4nSic-wSuuOJ5hjn3w5K-zm6USBBETXcr5kvOZThfUvzgu_O3Chn24I3ZgF3hGGetTuY-zPRjRPxPXx1uRTmAU6V3TK6BhNY2RYfiWnpM_lHBrqU7AlI_I4ednf5BOa2_WO7TdnIaHf6JXLFUcF_aBXnpFCE-2gjBrjSgOB_NJjER7YW1jwP0xHs4G6G7YPBQF41c75y6TONRkt24iTRYwJWrAg9CSvEVhrWxD_FlrsHPIGmEb85hEo_-Bgd3Jj2A84SiosOSbvp5WKqhSJAjeM9QQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
سرلشکر صفوی: پیوند تنگۀ هرمز و باب‌المندب صحنۀ جنگ را تغییر می‌دهد
🔹
دستیار و مشاور عالی فرمانده معظم کل قوا: جنبش انصارالله، خود دارای اهداف و استراتژی است و خودشان در زمینه تولید سلاح به پیشرفت‌های بسیار خوبی دست یافته‌اند.
🔹
من فکر می‌کنم که پیوند خلیج فارس و دریای سرخ، تنگۀ هرمز و تنگۀ باب‌المندب صحنه جنگ را تغییر خواهد داد.
@Farsna</div>
<div class="tg-footer">👁️ 6.45K · <a href="https://t.me/farsna/464153" target="_blank">📅 16:50 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464152">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mgQflT7Q1M4ZMTRXwgnjZZ7v8_6e5oBi8n_LkU9V-Vti3t96Izb1EaLkQ-mWC938txwLha8qknt40QKsY3ulEyPzz8iK8SFgOUyicp2o_w-3TuTeTX6kG2VYgTrUENZqojHYo06vBXyFI297_IBMfQEJLWTe9KxBgg-pi3Mw1rWz-iROIorqy1VL0Eoq6crpSBciUur4EkUx_ZyZWJ0SavTjpDKBLJUIZJ03cReqSnWKT5XorBAOZGtJ5HVBO6kmNIF-loJxgjIn2W77CJn4c2S8tcwgd9cIgDX5QCoBbTFe5l01Tlt9hlCUVEeJwQ_Qsof8dfHtaI9ZLxPyRjwKQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
رئیس مجمع تشخیص مصلحت نظام: مواضع صریح و انقلابی رئیس‌جمهور فریاد ملت مظلوم و مقتدر ایران بود. @Farsna</div>
<div class="tg-footer">👁️ 5.86K · <a href="https://t.me/farsna/464152" target="_blank">📅 16:48 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464151">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0aaab1592a.mp4?token=s_OW94wVxFHPEQAwGWAU07hUv2pfb2EGE_vrYvkLDPgZ_pbyjxbplNEsQ1TMFdecES6g3RXlmhghr-XLb2-p6rP6cH76_QqrXma6OGzC_VH9Z_M98nkDLpYOHQdCGBMKHEnVyIfnTNM08l81oosv-yGhwKzTQ_JNS94PGOQmhECm-THgGKW1VezWzMeIDRBNu6PpcXRiPJYfEfBMIteA7P_-Ao0PzDMls5hFfLGtN3AiQYWGnufG0wNFyIZPsRxCVtWKQUCH8IWpX4orGV7JMSNE5_Q5v7MEB4_jqfuTWNIaOFCKkvmu-1JILD1u0PWKpHxj8dtKZLETxIqxmFqapA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0aaab1592a.mp4?token=s_OW94wVxFHPEQAwGWAU07hUv2pfb2EGE_vrYvkLDPgZ_pbyjxbplNEsQ1TMFdecES6g3RXlmhghr-XLb2-p6rP6cH76_QqrXma6OGzC_VH9Z_M98nkDLpYOHQdCGBMKHEnVyIfnTNM08l81oosv-yGhwKzTQ_JNS94PGOQmhECm-THgGKW1VezWzMeIDRBNu6PpcXRiPJYfEfBMIteA7P_-Ao0PzDMls5hFfLGtN3AiQYWGnufG0wNFyIZPsRxCVtWKQUCH8IWpX4orGV7JMSNE5_Q5v7MEB4_jqfuTWNIaOFCKkvmu-1JILD1u0PWKpHxj8dtKZLETxIqxmFqapA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دیسک صمیمی برنزی شد
🔹
در رقابت‌های پرتاب دیسک بازی‌های آسیایی ناگویا، صادق صمیمی با قرار گرفتن در جایگاه سوم، مدال برنز این ماده را از آن خود کرد.
@Farsna</div>
<div class="tg-footer">👁️ 6.04K · <a href="https://t.me/farsna/464151" target="_blank">📅 16:40 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464150">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EVvBgZ7B9b5SIqsXnGU4Z4cV5XwKMtuPK9qBpkOunPPLSUd3unD94nd4wpOcwrTXancUJg-prv1JLbMeTt593XwwQyJz7bxe4Kex50a5pXTaNzzXjGksn0rDU8qrqLTKhR59T_8lDMTv_8IyuD0B0_5rf-BQmFn9GdXJ7bEfmgqEArgX5PRWbxNA4iRYnQQ0mRe9y2auYzaa7PVVuRZyY-b7n-UZ6Dy6hJUkgyTL8aW9pQkv1guNe2JPIxDxHallCghZ3LE1rBSp12F40_-8IY5LnBiXKJjnkjc6_i-vvs0kWcLEMYLE3fudxI5clMjBoK2VktanRqYv6ai9cYRRyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اولین حضور فیکس درگاهی
ترکیب تیم ملی ایران مقابل ازبکستان
⚽️
بازی تدارکاتی
⏰
ساعت ۱۷:۳۰
@Sportfars</div>
<div class="tg-footer">👁️ 6.33K · <a href="https://t.me/farsna/464150" target="_blank">📅 16:34 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464149">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eceb316f61.mp4?token=ISJzBotqNxWVsVU5iFw0XLY96Doz7IuPJ-GPUDRxX2utPxNFOVLn3EEhT_GNgUxERVDH-3WWj_27PWnaH2-Lo1X2zeeBJ1ThoGEBeninzk5uEiAU28Xr-PaDRRyhFeYcZAwh2s_fnLuAjqYIDzbXYiTi3xwOscCy_vPjb3uF8H6tGj3KaDB7O4A1G6UOanpk104QZFYn9P7eJhoSLCKnJRGX-LOfkTAb1nI0uEqaSUoW4q375h8uYbzwN65kBwftiwu4hMi5Q-ft3Wl_-WIyylcUz0SsqAmsCxsaGfTe9HazEtNPu9_mFgH4h2--Qp6s8-9QBKSSp4IFK7fkshZyzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eceb316f61.mp4?token=ISJzBotqNxWVsVU5iFw0XLY96Doz7IuPJ-GPUDRxX2utPxNFOVLn3EEhT_GNgUxERVDH-3WWj_27PWnaH2-Lo1X2zeeBJ1ThoGEBeninzk5uEiAU28Xr-PaDRRyhFeYcZAwh2s_fnLuAjqYIDzbXYiTi3xwOscCy_vPjb3uF8H6tGj3KaDB7O4A1G6UOanpk104QZFYn9P7eJhoSLCKnJRGX-LOfkTAb1nI0uEqaSUoW4q375h8uYbzwN65kBwftiwu4hMi5Q-ft3Wl_-WIyylcUz0SsqAmsCxsaGfTe9HazEtNPu9_mFgH4h2--Qp6s8-9QBKSSp4IFK7fkshZyzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نوحه‌سرایی پرشور آهنگران در جوار مزار رهبر شهید انقلاب
@Farsna</div>
<div class="tg-footer">👁️ 6.68K · <a href="https://t.me/farsna/464149" target="_blank">📅 16:26 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464148">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e579a8978.mp4?token=C5S-rUPgT-wSGWdnxL9m-VtDMH1dRWHt1P44G_1gm6OxL_UkiXMFUITR0RnuepjI4BowpHMye3Rf_k5m3JQkx_A817jDXhrLy5UEsMvR5ePNvVPJVWZ3lCk9vOVTHhGayGPquVStzB-QArp0zkxNTNWgMCPWrmPchD25xLxVqXQOTYrpLl8UvMzEpydGbYlBt1ZFuDPR2fgYwi-Sd1SMbFdeDAPxMgs5ch7-jbk9evaLNFhx5MLKNT_PQUMWZe_FVMpJRU-WD5A2sPKfHgSvrP_2gTdMtAgOKGJn9GmGKZnGsyw-rmr3YfV9yS_wTBOr0ABLbO6nOf41FCrKjStNqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e579a8978.mp4?token=C5S-rUPgT-wSGWdnxL9m-VtDMH1dRWHt1P44G_1gm6OxL_UkiXMFUITR0RnuepjI4BowpHMye3Rf_k5m3JQkx_A817jDXhrLy5UEsMvR5ePNvVPJVWZ3lCk9vOVTHhGayGPquVStzB-QArp0zkxNTNWgMCPWrmPchD25xLxVqXQOTYrpLl8UvMzEpydGbYlBt1ZFuDPR2fgYwi-Sd1SMbFdeDAPxMgs5ch7-jbk9evaLNFhx5MLKNT_PQUMWZe_FVMpJRU-WD5A2sPKfHgSvrP_2gTdMtAgOKGJn9GmGKZnGsyw-rmr3YfV9yS_wTBOr0ABLbO6nOf41FCrKjStNqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وزیر ورزش و جوانان: وام ازدواج برای سال آینده افزایش پیدا می‌کند
.
@Farsna</div>
<div class="tg-footer">👁️ 6.58K · <a href="https://t.me/farsna/464148" target="_blank">📅 16:18 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464147">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F7lGga5MK-Eot6tFbrYDbBkAF0Zs_w-jss95R6oxyDl2ti2j4bIqrzWNzqOlsozz1r44IVtbrZZBnL5vOKLPQBFGqOvvj8W1Y9gZ95dsxr2mLYUzcItNuC9oz9tPQCarafq_EpIZjybWj_iExlZSjpAs1omClRrQHvurVqLJ0jB9itlxmA9XhNE0RENZvXzIH6gRYlwD24bvIQ7p8W4hksRzbMPAP4I3_dzGKTTVwA6Dgsh0rkvP3RmXV02ReIBSM6uqiTeRhcOdDIfKPnERxDSZOdvdpYX7zteUSMx8kspoxEKP7WvtBcXIPfVc34Dl6PJpzVt7P9NA5jESGM-Qzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
نگاه دنیا به یک سخنرانی
🔹
سخنرانی دیشب رئیس‌جمهور در سازمان ملل بازتاب گسترده‌ای در رسانه‌های بین‌المللی داشت. @Farsna</div>
<div class="tg-footer">👁️ 7.23K · <a href="https://t.me/farsna/464147" target="_blank">📅 16:06 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464146">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac5f6d18f4.mp4?token=Ygn_OFds4zmGq2ZvGRt7hq0MyCJc_qa73e_vPb_AVz2HwgGtJyPUFU_Zr1qjFrGkZsSxQ9TamuwM4PyV9x0BYaQ4QzLdoSNWHAD3HCMPsOqk1IvP6GOO2xrcFffSNtTMewHmrKl_QVhUe7fnozYzzyh1-kgzoRhPgwbNpTyg0X3EqqN91_IyJsXvgkAG1ajc9mdvtybwa88sZR63o_k99UR6Xa6eNmEiP1f-tUDvgLBbbex9NfheU5WUSKVZXsG3wuVcymbC7mDlc1JrBvUlycbEPuazDnDXSJxanVGYII8yr_Xp6LjNe8vF0IqTPWHTHAQzyLkk0pgw46qvLBFfLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac5f6d18f4.mp4?token=Ygn_OFds4zmGq2ZvGRt7hq0MyCJc_qa73e_vPb_AVz2HwgGtJyPUFU_Zr1qjFrGkZsSxQ9TamuwM4PyV9x0BYaQ4QzLdoSNWHAD3HCMPsOqk1IvP6GOO2xrcFffSNtTMewHmrKl_QVhUe7fnozYzzyh1-kgzoRhPgwbNpTyg0X3EqqN91_IyJsXvgkAG1ajc9mdvtybwa88sZR63o_k99UR6Xa6eNmEiP1f-tUDvgLBbbex9NfheU5WUSKVZXsG3wuVcymbC7mDlc1JrBvUlycbEPuazDnDXSJxanVGYII8yr_Xp6LjNe8vF0IqTPWHTHAQzyLkk0pgw46qvLBFfLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اژه‌ای: تعیین تکلیف فساد تراستی‌ها و غیرتراستی‌ها اولویت جدی قوه‌قضاییه است
🔹
یکی از گلوگاه‌های فساد، می‌تواند موضوع ارزهای حاصل از صادرات باشد؛ ما طی مدت اخیر بر این مقوله متمرکز شده‌ایم؛ اعم از تراستی‌ها و غیرتراستی‌ها. تعیین تکلیف این موضوع یک اولویت جدی…</div>
<div class="tg-footer">👁️ 6.74K · <a href="https://t.me/farsna/464146" target="_blank">📅 16:02 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464145">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c41a160901.mp4?token=oGB8ylEmaL2bCvm2D_PXmzCMHH10NTq3JYUqFSxbfzpFfMpiQAohlHapdhoVdaE38th51UZHLXiaCJZL0VDMI1dgnODfajOtAHBYRqo1XZxJZxxcV_ZUfG-d2ForxfzeIGdpJSyZnafGRA7RauL0NnaVE92Fj5b_xPVMsbSxWJ7ysQ_pJxQx3nOOguHXUUW880ZfNSv-I3bBWrQWs4YhIv-knB8z7OS2AVZUpshccgNA0NTU3mqDvhw_CKhVT92oKOROt2hnag7CngdXSB4XO_XNq_PHFEcw4i-HitxGGuwz5PSlegVlrpfrozVmi-PUpIlPZUZ77PlBu_pcmHywEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c41a160901.mp4?token=oGB8ylEmaL2bCvm2D_PXmzCMHH10NTq3JYUqFSxbfzpFfMpiQAohlHapdhoVdaE38th51UZHLXiaCJZL0VDMI1dgnODfajOtAHBYRqo1XZxJZxxcV_ZUfG-d2ForxfzeIGdpJSyZnafGRA7RauL0NnaVE92Fj5b_xPVMsbSxWJ7ysQ_pJxQx3nOOguHXUUW880ZfNSv-I3bBWrQWs4YhIv-knB8z7OS2AVZUpshccgNA0NTU3mqDvhw_CKhVT92oKOROt2hnag7CngdXSB4XO_XNq_PHFEcw4i-HitxGGuwz5PSlegVlrpfrozVmi-PUpIlPZUZ77PlBu_pcmHywEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اقتدار ایرانیان در خلیج فارس؛ از شهید مهدی تا تنگسیری
🔹
نظم و ترتیبات ایرانی در خلیج فارس و تنگۀ هرمز نشان از اقتدار ایرانیان دارد.
@Farsna</div>
<div class="tg-footer">👁️ 6.86K · <a href="https://t.me/farsna/464145" target="_blank">📅 15:56 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464144">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5a88122ab7.mp4?token=olBKPKq5KOLKvBbvYfkCWY3p3eRJqb_PHbC5A79ofIJQIPCIkGQovlBmSNRjXVZbgAynEoe499ADtpOxIUeQdKUM-0r_9ndSqGW3q3TeBG-MJZknaTqAwyl4bV-80V3NLxcJ2e0fnRMMJ7VKuC0btPA9xffGtVSWUOqgDfHsVgNw4Aj9_wx5zvqH6taBSYtrR2QCh2uHvEU_Ep_hfIEn-MBtp8qyKEjr4pzpgHCEsLlHZWzjBxOO-kccgF5SBOqWefdXfrJwkvp8ZdRPRyosJqWQlrqwetQj1aPulPw2Wqn8-Ce_K83njVMF0dAoFwzlLFE7WcLlgfBDg5t5KSS2lA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5a88122ab7.mp4?token=olBKPKq5KOLKvBbvYfkCWY3p3eRJqb_PHbC5A79ofIJQIPCIkGQovlBmSNRjXVZbgAynEoe499ADtpOxIUeQdKUM-0r_9ndSqGW3q3TeBG-MJZknaTqAwyl4bV-80V3NLxcJ2e0fnRMMJ7VKuC0btPA9xffGtVSWUOqgDfHsVgNw4Aj9_wx5zvqH6taBSYtrR2QCh2uHvEU_Ep_hfIEn-MBtp8qyKEjr4pzpgHCEsLlHZWzjBxOO-kccgF5SBOqWefdXfrJwkvp8ZdRPRyosJqWQlrqwetQj1aPulPw2Wqn8-Ce_K83njVMF0dAoFwzlLFE7WcLlgfBDg5t5KSS2lA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
لحظۀ افتتاح پادگان آموزش نظامی جان‌فدا با شلیک حجت‌الاسلام طائب، فرماندۀ سازمان بسیج مستضعفین   @Farsna</div>
<div class="tg-footer">👁️ 7.3K · <a href="https://t.me/farsna/464144" target="_blank">📅 15:44 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464143">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UkcXXTe4NtyAbEWgx0rxY4yysntDnU29NoN0XiJ2xwUYrRvInoXm8WXPr003KA6A42rDl6wIPAn90zhOVUVjnZPsXypoJ7if-om8Cg6V2TVaM-6XkX6ps8bwqT4ZrnBGpXNsqFKLCxUtPWXgtuuAXfsjrf3xwBC6nu3e7BSoMx5c1vrGxLu9xfUvO9oDatHgzNbsoLDME52Rppx3ZtEGc57glzef-dRRjfooCDK14ZxlOHOsgZjRacwYv9N0awndZFaoTM8LEg8c0GvVS9eeQT68IpucTdGZ1O3bQ6ePTmFHAuR2dXg1xUwMwhRabqzHrzauwSKJbf-a3JnMx9tB2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
عراقچی با وزیر خارجۀ اوکراین دیدار و گفت‌وگو کرد.
@Farsna</div>
<div class="tg-footer">👁️ 7.86K · <a href="https://t.me/farsna/464143" target="_blank">📅 15:31 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464142">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fe3faed9dc.mp4?token=lkhcrJX0hPDrczwZHzcPV9M7dXhPTtOwL3_1I_1qGqIudWR5JNZddLdiqInx2VJkBvHqPTPZwSE0n3IWBLmVVIigxtBbhhUVyQpz8jeFEkuPLC7PEUloIJc1uN06OCVAeSV3fKgdsxOqhkt80Lg4tq5I6SbBgDVV1FmX1UXDCBgCrBs-u7af7FoRdnCmd0MxcgXkQirTIF0f9pH4FzvSm485mJQDcJDhSlUCBFp8IYtenU5EhS0hrw5w0CksQ2wdxQbTGowlW9VHXZWJbJDF0iAgASkRJefX4SiyFn0IsT070qsX59ac4ye_R64ePVlTe-LLFDvdgX3WCsBE_BcXOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fe3faed9dc.mp4?token=lkhcrJX0hPDrczwZHzcPV9M7dXhPTtOwL3_1I_1qGqIudWR5JNZddLdiqInx2VJkBvHqPTPZwSE0n3IWBLmVVIigxtBbhhUVyQpz8jeFEkuPLC7PEUloIJc1uN06OCVAeSV3fKgdsxOqhkt80Lg4tq5I6SbBgDVV1FmX1UXDCBgCrBs-u7af7FoRdnCmd0MxcgXkQirTIF0f9pH4FzvSm485mJQDcJDhSlUCBFp8IYtenU5EhS0hrw5w0CksQ2wdxQbTGowlW9VHXZWJbJDF0iAgASkRJefX4SiyFn0IsT070qsX59ac4ye_R64ePVlTe-LLFDvdgX3WCsBE_BcXOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
صورت‌حساب تابستان ترامپ برای زمستان آمریکا
@Farsna</div>
<div class="tg-footer">👁️ 7.56K · <a href="https://t.me/farsna/464142" target="_blank">📅 15:30 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464141">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/15262db003.mp4?token=Coms1cTIoW6zRvcBylf2e76O48lcHNA6pKWtDcBDwzMbzk0m92UgwVvQ7svntrjvFYtxCHVSZPeeTi0PzcyW2aUoJnwzOD1qKJFMe8FF0Wm7xU1NB_aPwu5kjBx9kfyZE4rm1JuZnYsz0H_JyV2PB0SIq7l9_f_L5WAgurw-0mY__dVFURVXaiJEjgDnlbVcfV9cTDdthW8GQQqrIN3rToPw9cYbkTwGoFk22EkGF49Eh-ODh1Ph0b3onI-Tf8EiJB2A4orX-Dc040oDu8KJGISiVrg1nmqXeILLBRYfZzlp3LWPRzEvHarXN1pyrCQlLSTSzXR17V1fDm1IRbwZ9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/15262db003.mp4?token=Coms1cTIoW6zRvcBylf2e76O48lcHNA6pKWtDcBDwzMbzk0m92UgwVvQ7svntrjvFYtxCHVSZPeeTi0PzcyW2aUoJnwzOD1qKJFMe8FF0Wm7xU1NB_aPwu5kjBx9kfyZE4rm1JuZnYsz0H_JyV2PB0SIq7l9_f_L5WAgurw-0mY__dVFURVXaiJEjgDnlbVcfV9cTDdthW8GQQqrIN3rToPw9cYbkTwGoFk22EkGF49Eh-ODh1Ph0b3onI-Tf8EiJB2A4orX-Dc040oDu8KJGISiVrg1nmqXeILLBRYfZzlp3LWPRzEvHarXN1pyrCQlLSTSzXR17V1fDm1IRbwZ9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نگاه دنیا به یک سخنرانی
🔹
سخنرانی دیشب رئیس‌جمهور در سازمان ملل بازتاب گسترده‌ای در رسانه‌های بین‌المللی داشت.
@Farsna</div>
<div class="tg-footer">👁️ 7.94K · <a href="https://t.me/farsna/464141" target="_blank">📅 15:24 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464140">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PI3kDkQCWunbTFKs4Yc7sBHxmlrOfoBjqgsZ-r2RENTPmr9obInSrUZAvRYDI6PEdqtT5-xiyaZnd__kxXREhxjXNZFSHG7vmsUAdG2PLMqrZG05umH8-OukLyvkdO0SWhBxJWGjb_sFNccUlUoYhfoDVPhZaEWDqqTmAM7qfaborR2Ud2LckbM3WkJ98OTwPGzsyoR6tr3bS4qjzQmIJFz69GQbtH3DMvenojbIxax0Ly_WYc0c8P3j92TVg9lcQW934j4v0Z0hAi5W1LJzTIDYcg7ATd0Oq4m6gQsglm_ch1rVZtbN5dApMEcR43B0At9p4wLyEgt-JYeup_bPng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیام سازمان بسیج در تقدیر از مواضع عزتمندانۀ پزشکیان در سازمان ملل
🔹
سخنان  رئیس‌جمهور و به نمایش گذاشتن تصویر رهبر شهید و تصاویر شهدای مظلوم میناب و لامرد، توانست صدای حق‌طلبی ملت ایران و مظلومان جهان را به گوش دنیا برساند و هیمنه پوشالی قدرت‌های سلطه‌گر…</div>
<div class="tg-footer">👁️ 8.18K · <a href="https://t.me/farsna/464140" target="_blank">📅 15:12 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464139">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ed3c1f9bf0.mp4?token=mQyP0qZCLyBgpitaxi_NhWfSccnCDMlTBF-3RjFVxRtMjVY3tdOjhBZwAfb-_luj3JLKL6zJAbJc94o7Ia2Oox685CQ1hxWtJwXsfO0fFjGjKKy1NEd0Y6CroAsbK1vydMetbx37ZRYbmsko8pf2oCPHrrxIg7J0YkwtPQr3NSmPFuzdIOHzxAB31XDOBIFuxK0fsBQsEbM7NjBMkt4A4JgjoYVnu3NXR6bEUeE3chJGbJPqUC3mFFFUYd7ZUA2-96M1O0DCHivvIlikrEMhlwA_nHtt-Lwep59vGXBPVO6Ddu_ppdISXNbjPZCyFuED3x9l7lgzznABN0J0_-J9Up5QT6jBJH2HYVJ3jdRM8zbY3UnXqNSU4YrmUm7mICp2T-3swRKcAHcFkK5EBYZcsBPxwn5o0hcyCHVeyt4uBiVi3NjYkTa6c4Fox8xkb3IzRyaLmdbT32OuTAjJUI50KYRHzAvir09VsfklabX0WIeLBSW0a8BO3A-zCvb7DuitCdmWAuMUiUqTHGApXBm4INZ7dUJLoYWNtsYT-gAXkZbeQZguENd6uC_BsgHOqyPYXWts_x_qKo6KwSbbKzf11UZ-CQH9FLBguFJaE2fMy4tYxm76EMcAjeHmLX5m7Q39DhWfX91HZ7fuoJk70zopkQO-gzfkfO4SQo5sqQVIIsE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ed3c1f9bf0.mp4?token=mQyP0qZCLyBgpitaxi_NhWfSccnCDMlTBF-3RjFVxRtMjVY3tdOjhBZwAfb-_luj3JLKL6zJAbJc94o7Ia2Oox685CQ1hxWtJwXsfO0fFjGjKKy1NEd0Y6CroAsbK1vydMetbx37ZRYbmsko8pf2oCPHrrxIg7J0YkwtPQr3NSmPFuzdIOHzxAB31XDOBIFuxK0fsBQsEbM7NjBMkt4A4JgjoYVnu3NXR6bEUeE3chJGbJPqUC3mFFFUYd7ZUA2-96M1O0DCHivvIlikrEMhlwA_nHtt-Lwep59vGXBPVO6Ddu_ppdISXNbjPZCyFuED3x9l7lgzznABN0J0_-J9Up5QT6jBJH2HYVJ3jdRM8zbY3UnXqNSU4YrmUm7mICp2T-3swRKcAHcFkK5EBYZcsBPxwn5o0hcyCHVeyt4uBiVi3NjYkTa6c4Fox8xkb3IzRyaLmdbT32OuTAjJUI50KYRHzAvir09VsfklabX0WIeLBSW0a8BO3A-zCvb7DuitCdmWAuMUiUqTHGApXBm4INZ7dUJLoYWNtsYT-gAXkZbeQZguENd6uC_BsgHOqyPYXWts_x_qKo6KwSbbKzf11UZ-CQH9FLBguFJaE2fMy4tYxm76EMcAjeHmLX5m7Q39DhWfX91HZ7fuoJk70zopkQO-gzfkfO4SQo5sqQVIIsE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📷
شیرازی‌ها لشکر جان‌فدای ایران  عکس: احمدرضا مداح @Farsna</div>
<div class="tg-footer">👁️ 8.19K · <a href="https://t.me/farsna/464139" target="_blank">📅 14:57 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464138">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6ca987a407.mp4?token=t9H1YsBIsWengKpb-FQjtD-niiWJJUaMyXGVJ4aXSkOJxJrkleXvn6PfIP2E5k2xKzQo0YHAtz6RclOojMJbzvw52dT9qZAXoXJoouraZgFuF_qiw9JqZ_hZKxv6vUk_IZ0FhOFLDayqgIFwEbcSQu8Ju6Q7I0MtQFlskFcUnvupl_85Jln548tsgphdVDSwMoMQPjaCCwu9nG3-Nm8sP4OLnjvTTBUqg03B-BcFcJ7qQIPnoGdbeTNTlz-N1XaN3C6wHZsLpHJwed75a0LWHK9mlU2FBAaiB6Q4u6_iaAzeoXu6t0DegtfVyhJ-3lfy7RhU_MultCfHKe_7BCSuqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6ca987a407.mp4?token=t9H1YsBIsWengKpb-FQjtD-niiWJJUaMyXGVJ4aXSkOJxJrkleXvn6PfIP2E5k2xKzQo0YHAtz6RclOojMJbzvw52dT9qZAXoXJoouraZgFuF_qiw9JqZ_hZKxv6vUk_IZ0FhOFLDayqgIFwEbcSQu8Ju6Q7I0MtQFlskFcUnvupl_85Jln548tsgphdVDSwMoMQPjaCCwu9nG3-Nm8sP4OLnjvTTBUqg03B-BcFcJ7qQIPnoGdbeTNTlz-N1XaN3C6wHZsLpHJwed75a0LWHK9mlU2FBAaiB6Q4u6_iaAzeoXu6t0DegtfVyhJ-3lfy7RhU_MultCfHKe_7BCSuqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رئیس سازمان برنامه‌وبودجه: منابع ارزی تامین دارو همچنان ترجیحی و ۲۸.۵۰۰ تومان است.
@Farsna</div>
<div class="tg-footer">👁️ 8.22K · <a href="https://t.me/farsna/464138" target="_blank">📅 14:53 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464137">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f88677e22e.mp4?token=f1T1Az3sVHp9ZVaokWj2Kydn6vh1pjJ7ZNdJfizMkW_jJ952Nic8s0Sw_UFW1mL-bMUR0NRd_AXPgUH4kv7e7U0QAmoceJh0ku10q20b4dGpTTgOpEHEFshhVPi5DpdyDgKYDdlqW54LuKIUmr0rYRvLUZzQMfdMPzAbkCaSB4JMnRp18v7OM8LvQHFyYBpU9NBBSF7fA_gax0IBvIetj0Rx27KDFXfLBPkyjZ3SCX8l8_m0wi01Gi-RAF460LSsbhH1-O3hnccNQ3pUsoUv4x6HAolou7R_hXkv7pFXoEK-2CPhVZ52C2DHjZnsv9ucRH7sgHYvBsfTtBUDjr7uDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f88677e22e.mp4?token=f1T1Az3sVHp9ZVaokWj2Kydn6vh1pjJ7ZNdJfizMkW_jJ952Nic8s0Sw_UFW1mL-bMUR0NRd_AXPgUH4kv7e7U0QAmoceJh0ku10q20b4dGpTTgOpEHEFshhVPi5DpdyDgKYDdlqW54LuKIUmr0rYRvLUZzQMfdMPzAbkCaSB4JMnRp18v7OM8LvQHFyYBpU9NBBSF7fA_gax0IBvIetj0Rx27KDFXfLBPkyjZ3SCX8l8_m0wi01Gi-RAF460LSsbhH1-O3hnccNQ3pUsoUv4x6HAolou7R_hXkv7pFXoEK-2CPhVZ52C2DHjZnsv9ucRH7sgHYvBsfTtBUDjr7uDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رئیس سازمان برنامه‌وبودجه: بخش عمده‌ای از مطالبات گندم‌کاران این ماه پرداخت می‌شود
.
@Farsna</div>
<div class="tg-footer">👁️ 7.99K · <a href="https://t.me/farsna/464137" target="_blank">📅 14:51 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464136">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JgCKBZc2BP13nHDlKq2vdhEBe14_UfAPFOhjeHwEXeHo2UraFyjAxNQTnOmP4Dh3qCkI1J6OXvJF8gJifDUI3JUubJ7IoUrRwD2iJtxnH5hpTyF8awtZr5dTSrC5-GBAff2OYmcOLdLB4cy5SWHntZ3GlEgPylMerfuwP01pPxJqpibIq64RoMQGRAHII44JumzYD_l2lFdWLNzQ_ofg6QgWywAR9kmczbC2RNHm4LPs1XcOf3VQuNz33RwVWlY_e0Fc1YOC10moZmCkF9-CECg2KDXHR0zFPN3HKhCwzoNiDq_jUokHzNfjrEQ699G7vXmyuoXYg7R4SmN9z_u88Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سرلشکر صفوی: ایران نیروهای آمریکایی را از دریای مدیترانه تا دریای سرخ و اقیانوس هند رصد می‌کند و از موقعیت ناوها، هواپیماها و نیروهای آنها اطلاع دارد.  عکس: مقداد مددی @Farsna</div>
<div class="tg-footer">👁️ 8.57K · <a href="https://t.me/farsna/464136" target="_blank">📅 14:45 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464135">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4414df7320.mp4?token=GVcuJMl05pqSvedRa1dLLnJWLTCXL_fwuLHF4zkE7056O_QYPkZ-9TxDY33n1HDBudP9rOL5Rp0XdpcntlZ8Fe9sgVWvGvrmFQOVCbapfNLSlUoV2bq5un5qJLORe8s-sif3oFIip8pBpV67HqT6qJmR_iPeFjYqgrup0KS7PdSavo3PGkmDgJdYMdSKOTII8uzZ6LIq1-8HYlCNptERkHjdl6E78FfSmmSb8HHrWAF7sLWSKBOAcVrE9GIDQsD9PQ2BQUg98NPvTbG8Ic-uppZ6jPEbltnVqnVsOPLyMlPLSxojeIdswQ-Vqo_zsUGVCrBPs5I37xMK40RCYZJ-nQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4414df7320.mp4?token=GVcuJMl05pqSvedRa1dLLnJWLTCXL_fwuLHF4zkE7056O_QYPkZ-9TxDY33n1HDBudP9rOL5Rp0XdpcntlZ8Fe9sgVWvGvrmFQOVCbapfNLSlUoV2bq5un5qJLORe8s-sif3oFIip8pBpV67HqT6qJmR_iPeFjYqgrup0KS7PdSavo3PGkmDgJdYMdSKOTII8uzZ6LIq1-8HYlCNptERkHjdl6E78FfSmmSb8HHrWAF7sLWSKBOAcVrE9GIDQsD9PQ2BQUg98NPvTbG8Ic-uppZ6jPEbltnVqnVsOPLyMlPLSxojeIdswQ-Vqo_zsUGVCrBPs5I37xMK40RCYZJ-nQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مدال تاریخی آرمان در پرش خرک
🔹
مدال نقرۀ آرمان خدایی در ناگویا، نخستین مدال تاریخ ژیمناستیک ایران در بازی‌های آسیایی در وسیلۀ خرک حلقه محسوب می‌شود.
@Farsna</div>
<div class="tg-footer">👁️ 8.33K · <a href="https://t.me/farsna/464135" target="_blank">📅 14:32 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464134">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/978621abd9.mp4?token=NBcBPUwI-bKiBfW_gcXGF2iug42PjloBjhFPc8UoCa4uYqtLgI9OVUrtDhjVMA8Eo4IVblmuslajclUf7X1edr5GiKH0yp0R9JKppQxueuL5GnpVTdTxl4q5QrCTSUCXF8dtLuRNjA7NitFyDXDPXPnzKLO6E1h9jJV0G4fxl9Ownn47svAuXTI-Wc1gdwBpRNNf5torqZqABvivl1Q4nYfpblgutgWyMMOLzlgKWtRDCx0hoFIEgSas1m_JBfBgnCfCJvp3i6d7Y2uT-GqRsEfNFf9vLJbkXPKzX0DHsWhIn9aapSWR2q7wo3p4tvz3QZeQF2yFyqnfT_D-25tF8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/978621abd9.mp4?token=NBcBPUwI-bKiBfW_gcXGF2iug42PjloBjhFPc8UoCa4uYqtLgI9OVUrtDhjVMA8Eo4IVblmuslajclUf7X1edr5GiKH0yp0R9JKppQxueuL5GnpVTdTxl4q5QrCTSUCXF8dtLuRNjA7NitFyDXDPXPnzKLO6E1h9jJV0G4fxl9Ownn47svAuXTI-Wc1gdwBpRNNf5torqZqABvivl1Q4nYfpblgutgWyMMOLzlgKWtRDCx0hoFIEgSas1m_JBfBgnCfCJvp3i6d7Y2uT-GqRsEfNFf9vLJbkXPKzX0DHsWhIn9aapSWR2q7wo3p4tvz3QZeQF2yFyqnfT_D-25tF8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: بعد از شنیدن سخنرانی رئیس‌جمهور آمریکا، متن آماده شده را تغییر دادیم
🔹
در مجمع عمومی سازمان‌ملل از حقانیت ملت ایران دفاع کردم. ملت ریشه‌دار و متمدن ایران نابود شدنی نیست.
🔹
ایران را نمی‌توانند نابود کنند؛ ایران کشوری است که ریشه در تاریخ دارد و…</div>
<div class="tg-footer">👁️ 8.86K · <a href="https://t.me/farsna/464134" target="_blank">📅 14:28 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464133">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a9eee73cef.mp4?token=pifUKBxR-wrXGqBS8yCJO-M6OG3hAzoA1TDuiY8TsMEMGXlxQ4-CG0bDvV0RKMCcIKsKVl3WoHFvUOHIeXd3kAsvu4xyv7kj3KG6NArBEWuoOqwU6SzZLz17d8yeLFwlhZZ0jaJcW-1uh3USFzzWPhfyvLbc-yS6mjtixtR-OXm9gGWLe74i9o5T-ZfObPHpAg3cMy-ysq52KAUrAsMDnDU1AKCHSA_ZUvObsfodiqPVxU5ZabLwvAzTvoRfUGjMnrDRdcjbgyNn_NL1fqnmrLxYyqvNLzQESkvaGzDXu_IZ5RdknjvrEtbw04aCzHmkvfXsX83igkXVpHNsyhXpmCylo3vvB5bsTnfBZ7306pYnIskClFfdGLd0I2y05o4yOajxPD8KPdo_CO_-_L1MWZ78LI-4Fa101UvwMM7eD4Wrc937DcpkjqRy4iL0DsCcdRmbWT6qpj26-hVB-ivoMO17Bx8GZKWpCySt5B4GLYeNERoJ5cJVuO899gDAk3OLZhfMVbKCSqRK9ZnbFJ3qiHPjhfZoMCjOGuzLdwRUnc6gVnS4gHNUHYInM53XQErpBOUQ3KEY7Xe33e8iQyH-1qRQYDlcjz4vDJu5DENu20Yus6qDRxAA-YD24LwKS8Sxq8HXj1AsvOAAZNvqJtvuS7jG7SlwHrQR1CwOE2BjdHY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a9eee73cef.mp4?token=pifUKBxR-wrXGqBS8yCJO-M6OG3hAzoA1TDuiY8TsMEMGXlxQ4-CG0bDvV0RKMCcIKsKVl3WoHFvUOHIeXd3kAsvu4xyv7kj3KG6NArBEWuoOqwU6SzZLz17d8yeLFwlhZZ0jaJcW-1uh3USFzzWPhfyvLbc-yS6mjtixtR-OXm9gGWLe74i9o5T-ZfObPHpAg3cMy-ysq52KAUrAsMDnDU1AKCHSA_ZUvObsfodiqPVxU5ZabLwvAzTvoRfUGjMnrDRdcjbgyNn_NL1fqnmrLxYyqvNLzQESkvaGzDXu_IZ5RdknjvrEtbw04aCzHmkvfXsX83igkXVpHNsyhXpmCylo3vvB5bsTnfBZ7306pYnIskClFfdGLd0I2y05o4yOajxPD8KPdo_CO_-_L1MWZ78LI-4Fa101UvwMM7eD4Wrc937DcpkjqRy4iL0DsCcdRmbWT6qpj26-hVB-ivoMO17Bx8GZKWpCySt5B4GLYeNERoJ5cJVuO899gDAk3OLZhfMVbKCSqRK9ZnbFJ3qiHPjhfZoMCjOGuzLdwRUnc6gVnS4gHNUHYInM53XQErpBOUQ3KEY7Xe33e8iQyH-1qRQYDlcjz4vDJu5DENu20Yus6qDRxAA-YD24LwKS8Sxq8HXj1AsvOAAZNvqJtvuS7jG7SlwHrQR1CwOE2BjdHY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
متفاوت‌ترین جشن آغاز سال تحصیلی در‌ حرم مطهر امام رضا(ع)
@Farsna</div>
<div class="tg-footer">👁️ 8.21K · <a href="https://t.me/farsna/464133" target="_blank">📅 14:25 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464132">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاخبار قزوین</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/beb4b65587.mp4?token=ZdQT0CEioY50t-L-Xa1cOqJostPXEuGWWAprVBUdWfO_1_JB3snF8evUgzjyFcT-HMOjWlRebAexHiYJaAJdIo7dx80CH0S5-ZCX8Azb1jE4DBbpHn_qYCCKVkpjsUozZQ0heQTDjyvhNQutjQdtkXpHbGcPnZ9FchQDELG_ERhzVjZfVB5f4ewi-RNcWYeyhW8P_0z9s8idZPmw8yTGBfqWUBywr8NstonTg-Of3QN5luNJe-7pC84fB6FTg99pmEvmjdSujiumv7IizL2Cou-wZvqrwttTC8-xQayL4fzw901dINGbHit1hJkYzpqBRLe1zXhLFbanO3NYrFke5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/beb4b65587.mp4?token=ZdQT0CEioY50t-L-Xa1cOqJostPXEuGWWAprVBUdWfO_1_JB3snF8evUgzjyFcT-HMOjWlRebAexHiYJaAJdIo7dx80CH0S5-ZCX8Azb1jE4DBbpHn_qYCCKVkpjsUozZQ0heQTDjyvhNQutjQdtkXpHbGcPnZ9FchQDELG_ERhzVjZfVB5f4ewi-RNcWYeyhW8P_0z9s8idZPmw8yTGBfqWUBywr8NstonTg-Of3QN5luNJe-7pC84fB6FTg99pmEvmjdSujiumv7IizL2Cou-wZvqrwttTC8-xQayL4fzw901dINGbHit1hJkYzpqBRLe1zXhLFbanO3NYrFke5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پدر نبود اما فرمانده تا مدرسه همراهش شد
@QazvinFars
-
Link</div>
<div class="tg-footer">👁️ 8.59K · <a href="https://t.me/farsna/464132" target="_blank">📅 14:20 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464131">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ibwlO1JwlL1fBAX6eVJxbtJxRLnAqSAFNp50Cid-0AKZkAJ6oexpbxLxNyaKLkduZv3cYfxAR8V76tjq679EMG55VmDlZwKaM7EE1Ux4rHEjwV9S4Ys4UTefTKreHlXn_xjUzsHr4L1fznt-GyS1NRRT11lw5c0teNJH3EZ3Gl0MEM8mZjBo4hMFAnKRVRfbznhdehxD_bV628Qcul2vN27PlrfAjtCewx68S78QlDSy_rJmO0gqAlyFsNQeNy2dAuCsnHsY9vruhp-orty6MW_E6PQrhjtsGEnvGSN5u27LZV9exF99lJuZ3lZCqUg18FXu3TPnJMiDL83kI9pjGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
سرلشکر صفوی: پیوند تنگۀ هرمز و باب‌المندب صحنۀ جنگ را تغییر می‌دهد
🔹
بیش از ۱۰۰ سال است که یمنی‌ها در مقابل هر نیروی مهاجمی که می‌خواست به نوعی به تمامیت ارضی آن‌ها دست‌درازی کند، ایستادند.
🔹
جنبش انصارالله، خود دارای اهداف و استراتژی است و خودشان در زمینه…</div>
<div class="tg-footer">👁️ 8.99K · <a href="https://t.me/farsna/464131" target="_blank">📅 14:09 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464130">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">ممنوعیت صدور چک رمزدار از ۷ مهر
🔹
بانک‌مرکزی: در راستای حذف چک رمزدار و جایگزینی آن با چک­‌های تضمین شده، صدور چک‌های رمزدار از سه‌شنبه، ۷ مهر ممنوع و همچنین پذیرش (واگذاری) چک‌های رمزدار در سامانه چکاوک از اول دی‌ ممنوع می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.7K · <a href="https://t.me/farsna/464130" target="_blank">📅 14:06 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464129">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8c7b4a05c1.mp4?token=DaxyyKS-V0kUuDYlByXyAfuSOi0nxUTdqRBBVTZ4Ed4pouu6xRXB3yy4-ir05BZcZq2V38SKSAu6g0ff5SPns5NrjvvKSUjIasDWjaMLf99xFRbxhc_bfbH89zPmb_QqhN_ESzt-kjKbB4hTdfR1DqV3_8uEqZ1tJFS0YsbqtvFEqlwLqsgd6-IXOZhwN423tIkewJiXIRT4eerINIe_OUw4yFw-0w10ZxvxHtxGg2vrD7LGhFw9yPFxKGOXqBTRS6Y6uWUYfwHnwK9jNnREmOY-eFw0CaqITIv-7hW_yo1X2x4oWpsaAmdgn1NQsbikXlLVsxtK_cZx5-CyerKnKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8c7b4a05c1.mp4?token=DaxyyKS-V0kUuDYlByXyAfuSOi0nxUTdqRBBVTZ4Ed4pouu6xRXB3yy4-ir05BZcZq2V38SKSAu6g0ff5SPns5NrjvvKSUjIasDWjaMLf99xFRbxhc_bfbH89zPmb_QqhN_ESzt-kjKbB4hTdfR1DqV3_8uEqZ1tJFS0YsbqtvFEqlwLqsgd6-IXOZhwN423tIkewJiXIRT4eerINIe_OUw4yFw-0w10ZxvxHtxGg2vrD7LGhFw9yPFxKGOXqBTRS6Y6uWUYfwHnwK9jNnREmOY-eFw0CaqITIv-7hW_yo1X2x4oWpsaAmdgn1NQsbikXlLVsxtK_cZx5-CyerKnKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حدس بزنید این‌ کارها کارِ کیه؟
@Farsna</div>
<div class="tg-footer">👁️ 8.85K · <a href="https://t.me/farsna/464129" target="_blank">📅 14:03 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464128">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/82dc15a2c3.mp4?token=XtRRCjpfFjwlP6ypUWVeLDxYZTcehXfB8O8A4Yw-2JQvu8zXdShb_ig4GuqlCIsb8bpzX3HEHsLXNg79L0Te1iEirW7zNy0LwyApvVzZBPbYPxYR6h4YmQQE71IXWBJltC2mXPm0cHpk0a4Cwt6037KYfo_Y5VkvDK3wfII9mJMigdQMWSRCe0QFmMl_TOaCVZW2-K8HSumqOXvVssHSRF1imnhFOaWuoXw1KN-kFB6yObgHXnHe1u_H03H_WohEbAnBFtz4r-xRdhECJnwyfm8ul84uYm39vFKUrZbA1mHWVDBA4RwbPpsZ5Y4oLLAp-dxZRPtNmjhcFzJ9eLZZ3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/82dc15a2c3.mp4?token=XtRRCjpfFjwlP6ypUWVeLDxYZTcehXfB8O8A4Yw-2JQvu8zXdShb_ig4GuqlCIsb8bpzX3HEHsLXNg79L0Te1iEirW7zNy0LwyApvVzZBPbYPxYR6h4YmQQE71IXWBJltC2mXPm0cHpk0a4Cwt6037KYfo_Y5VkvDK3wfII9mJMigdQMWSRCe0QFmMl_TOaCVZW2-K8HSumqOXvVssHSRF1imnhFOaWuoXw1KN-kFB6yObgHXnHe1u_H03H_WohEbAnBFtz4r-xRdhECJnwyfm8ul84uYm39vFKUrZbA1mHWVDBA4RwbPpsZ5Y4oLLAp-dxZRPtNmjhcFzJ9eLZZ3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دلنوشتۀ دانش‌آموزان اصفهانی برای هم‌شاگردیِ شهیدشان
@Farsna</div>
<div class="tg-footer">👁️ 8.96K · <a href="https://t.me/farsna/464128" target="_blank">📅 13:49 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464118">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FFHvlwPkRaabdrEyC7BAkmUJZUo5VYaWDDvetV8PJnUIoC7bnXT40oY_BKnsRbYFsYxdVM7SIK46DZKZqqoniRyw-3Rq8LjGoyaUlxriYMkzlkPKY8mUAeqKObtthwCHOXMBmtiO9LWFkvb_LP1jfg8lr0WvSlkpAs9xn16A2vmVM_8jlAqrVSrA-3VLDHjSIOufZTzfRqlXYmQVF9cUHcw9NTEqcHYxUR_jOemPfQfzKU9DRtfqeMY9uVQEVIToyJhgRDQBSH_Ncf5Xy4fwTL3fyrkWuzjteeI9Bn9cBVBZ-TfRHdxOPHwapaWNFnTatQm-Yd4jsyFA5bbMeZtSmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rTQfMco5lwh0fFrxw3TJhj-u5LqcA7HrmkSQZbLdLIlHsChnFRuczVuJu5WdXSbK4HfJitqA1Y3ZTJmoIAOELPF_24oejr35nbga7hSksuV4XQABgdifVnSLGp2CgIaNQ0jsP5bksWLFXedVnvEKeYPUauGoiUT6oLOL_zvp97ClRhEcaEVENr5sj5HxXPb8OvWAMSrUz1uOkaxlmEh-9C4IxvXrbZGKDKDT9ldcWI00sntOqbpiCY7Oy8SJ3dam7TZOm9MkxtNR9vHEYTNC9z3YDuSRdOzgqgMbGso1YBzsa4-fA33qOhyxivrO9UMcQgOeapWFDcPIcfuGEakHtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qrZI89tuo-3fJnl_qf2OSqi93djCQnLqno6gmgJDVVG1jwwN_z15b7AKkZ8WPpKnvC3glMWgzkC8YefFnGqtkh5SsqOlrCyZ7nuBa8aLGQS0w2dtIlyUDQE7y4cMMKGKjduMGXwyCYKECc6GGbVIkI9QhGS46aR1oOGN-8hobQV_ZDEGCHowEjXAn7drsX_wq-tRPoTlinjrJbx7Co21xe_3JVOIsOlElu1QDpH6Y0PTJwC15-q6OmKN4tWqCMdnL_GT8YWe7V14zx0763sIaLew-09qHimkyaYXC3k5zzY5g31jq9KFuR7R81SnVQrY7cg0dLn641xsv4xItkQIqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Gvu3GUH9CJmQBL5aH0rSmPYV_bvtan1R8JGQEKTB0e_U_K8MOqHlpFSj44kFf88BLj7u-hb4OEXOnVK1IzhVMXm5JCZSt4Qu5zkU89LUslRS8ZkFLzoC0nm5S9MTOWNozkr0y-9pzKjI_0o8Z-q5Jfz-Tx4zgCoT6Pt35Y7RBASPOwiri-VlpOtwKjL6T63GZV_W_LNUMvcrM01UXSP6ugdssImu7ESyukRzWYE90KhK44bKSu-An5zZyH2QTbb2_vDQahnftVwRxRBAiKr40mMT4FGYnPd9_rhsL0fndrwLezF7lQR-zL-HAvqksVUlIJB7-ugOIqHdK5domLSPCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/COWw8PMWRxR8mXVWFNYyOHl5P-ZMWbLkrIbAP4qgRf8gN98VnXJ-cn2gv4Jts9vALIgBTFABrTE2snAP0JITz4tsSLVaHJu39XVLq_YHhQLuOf-InyiUP0DUkGPpSDh-Y1mCyNMYqv3Rq5yrrPviqKTJyRkxQj-LjJPmn-AvkP-T5E7WDWKMES5j2LnqWEvjD59c857vMjhy68yqehYg7L_kNHGy82le62RvobmSd0Vtt5STHec7GlwhxuTubEU3G9W63K9weW4c6_crxvLsqer6IABb9-BqBmkvyzXX82FCA793yNkpnTZd_YeMjr9elJMMW0pyQ34M0xpwB7b-7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Upgogs8FHxfe4EfTpGQ9NR9a3Lfli6s9WQg1523jGNYGr8iS_ZrPx_96lHz023BAI-wRR7YENIVVQFbLpLfLpw9J-EagUxluH0NDTKv67JO4wgsFKng19edV-E5t4guPjSWtbX4fZhQs97QUr076qv5rJtK_C6cHn050VJrM6woMZzmlcxytZdbwnqOw-1SechxoFE-pZinX7TZ9c_tMB48q2uWX_vUu4E9Cef6Vp7i3THLab4htD01x-JP97ziuMTC2j3B4mO8qlwRO0xA9cM71DzILPt55xNZPDPycRHB-thzZoTk01ZXkD3__-takO9X2uBgenc2nqbwHR4JFeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TIpKmohFpLbODOlJKTtjJbdHDPgZbPOcIuptHrjjvrrh2tvRdyf7gewRpDzo7FsPB29Wl7erK-m1QxxDhXgMDbcg53ko00jYc65nqRFwKPb8I2VpaU3jwHuhT6Jpf3k6Z4h6lNslyStgCYPDpkatTZ1NFgQauabbsg5c3Yde8VEzufylHRA5CmmuWGqiIob0-0TdmRU92RNzQBfInnClGRnCGfrhpMzCJFjIzlERPrVUwIhI41lMWzzYHwNB07N7B3OCmgudLAtnv80R1ZN02kKaGKpbOLsadt7M08C_R-CwMI16PDMhsXjIYn9BgFHdImUqqkiNSQML6GBZhPS5eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UTGYEmbJCqBCflAfx_QDuyYcGKLgN4sNhU2wdnXtzdaQq8SG29AIGivRjuqteJxz3OP4nD6kFZ87JkiAySqpG5y26AyGLUfm03PR_YUzTh6HpXI5OAahSRpryiHg1Dv7JBKEDMXYWQ7YxfCFpqVHnNFfaxDq3zAr20-6AvJDzBAd7RMOWQtQdu0eikZJq8C4swyet_KvMho3KzAWJccO5yAaUh0AC0sn2YiHCKQ50p0OTx_ukbi_PHNoF9UA-Y-JdqGbTykorsHNqlXaSrSP2kKST1MJP--IA0cwBv10PGXN_q3-ZSCwGWXq0LH7DQNWPrCPQcKeqVqlA91tpOhVsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rxP8Z6kR7jG1iSfQquMv5YMLiC5ZVShndGmUpFp2fooJDchRX3qfL4Jb0kxdcP9huxVJO1vVXx1AGAEQePmoXiRfNubciSay0T1a--LkOULJjkLY4v1XhfObfkehnM-BSVWP4_IkZ48TDSHexgzgeVGdA3VwKiR7sVSvP_1x4yFaOQ1rACiQ-X9BZW_Put07L3UwuyTeNHnsMBpccSxx18NxPTUVOKJf1u181sbQtw__tmAxPDLrSd1fL2UlnU0EK30Pa0wvDtwtBl9RZ5wHPvS6Qfng1E7sZkEf7SyQ5T8xTUAk140md3ktWaw2AZmUDyI6KZ2c5SxxZ9Niz65ldg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eUgAnfXJiZlNnFTUCNviZQVDbAs4PzdqYR1g3BA0SI0xYHfINlSAchWnWD1PKjl-BGxNL62_HPnpqhOh2bXxDlwMNX8PIwU3iFVqV8HF4GMnJbOLOs5peqJiNrKEKhAKzP2967jJtAZk9cVcc8x4VvVgn85-0kRvlxSW6JQ0ra8nxIqfU9mM8gUYfYg5zLf3BvjIjLFmfSM4bFrRcdN6UMLJdV8q2K4W4ZS_tDlnMOc8baN6ZAqUiS9VCPqpmMVDCn1XWhqtkvzpD-J3aRaBa5otW-XZgNv8mQjcIjEZkgKmf_5RSgrmbxJw-ay6k2isox3G58NxiWxbe8Xbs6GKXQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
رزمایش جان‌فدایان در اهواز  عکس : محمد‌آهنگر @Farsna</div>
<div class="tg-footer">👁️ 8.58K · <a href="https://t.me/farsna/464118" target="_blank">📅 13:48 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464117">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f8jM4-2VshwbRySeJcxtlZBGC0alX3Og7pTRfciz_HQUhmF7D86qI4OLqVNOJdnntRuwkDgZL25oUtX_N3r-Vga5gfmJ_eKgRWi_rL3vZeXsKgbEQ7jLdQgwphIjr2ssK1cJkDoXmbKaBJkroPNLItFkSP4o4XkFvqxNxZQSOcg4YUiXB12_55rJie-K87J-pH8mPW-qjvWwF4VZLggscWbAgC_FuPRAgJMQ7i7XrE5CeSACdxgW5CmWUu-fXAvT5MZ7VgJMxpAUoEm1gpfqZM9al_S6kxN8hvYgJkzzZfJIPlecv3vN8GE_RI162-A8GT8SSxA28YbFNaNRpAQ79Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همتی: انگلیس روغن ریخته را نذر امام‌زاده کرد
🔹
رئیس بانک مرکزی در خصوص اقدام دولت انگلیس برای تشدید محدودیت‌های مالی علیه پنج بانک ایرانی در این کشور، در همراهی با سیاست اقتصادی آمریکا، گفت: این همان مصداق روغن ریخته نذر امام‌زاده کردن خودمان است.
🔹
به نظر می‌رسد خزانه‌داری آمریکا در فشار اقتصادی به ایران به آخر خط رسیده باشد و کشورهای مختلف نیز برای نشان دادن همراهی و تبعیت خود از آمریکا، فعالیت بانک‌هایی را که بعضاً سال‌هاست در چارچوب تحریم آمریکا هیچ‌گونه عملیات بانکی در ارتباط با ایران ندارند، برای خوش‌آمد آمریکا مجدداً محدود کرده‌اند.
🔹
البته خود ما نیز برنامه داشتیم که برای کاهش هزینه بانک‌های غیرفعال در خارج از کشور، محدودیت‌هایی را بر آنها اعمال کنیم.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.73K · <a href="https://t.me/farsna/464117" target="_blank">📅 13:41 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464116">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dpYT4iZETOLWf8aHrWOs87TS_8rUCWXgUZQasZ5KnFRQt4DBEm-xMocbDKyxOSRMioRm26KvjhoHMAmwdAOo7TXGpAR9OgH9rWzpO5fTjjqXCCdx5R9IY1lVL-AJwGZpS6l51-vpZXOSbtdRCn_8mflaft3MCSE0pcCBq0CFK6lcwihu6ObTReiyNHX-_3PP9oVEYld6-gFXLGNmZ8bGM6d-w9_nldSKJx_ij-il-CHovdbTGuAm-vOtuaVZldePbwW9bD220dCQk5iZsMT1pj8x7j97hSD2ugZb5YQUQA1-hZkPkGiKbJ1_YtO9APJdjze-FV2WFrWwBimsMR2PHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیام سازمان بسیج در تقدیر از مواضع عزتمندانۀ پزشکیان در سازمان ملل
🔹
سخنان  رئیس‌جمهور و به نمایش گذاشتن تصویر رهبر شهید و تصاویر شهدای مظلوم میناب و لامرد، توانست صدای حق‌طلبی ملت ایران و مظلومان جهان را به گوش دنیا برساند و هیمنه پوشالی قدرت‌های سلطه‌گر را به چالش بکشد.
🔹
بی‌تردید تبیین مواضع ایران با تکیه بر منطق، عزت و صراحت، بخشی از صیانت از منافع ملی در عرصه بین‌المللی است؛ از این رو، سازمان بسیج مستضعفین، ضمن قدردانی از این موضع‌گیری انقلابی و شجاعانه، بر این باور است که چنین رویکردی نشان‌دهنده مسیر روشن و استوار نظام اسلامی در دفاع از استقلال، امنیت و پیشرفت کشور است.
🔹
بسیجیان و آحاد ملت همیشه در صحنه ایران، با حمایت از این سیاست‌های عزت‌مدارانه، آمادگی خود را برای پاسداری از دستاوردهای نظام و ایستادگی در برابر هرگونه زیاده‌خواهی دشمنان اعلام می‌دارند و معتقدند که ادامه این مسیر، ضامن سرافرازی ایران اسلامی در معادلات جهانی خواهد بود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.24K · <a href="https://t.me/farsna/464116" target="_blank">📅 13:19 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464109">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bmGpfJTe_RC_cemekOFy7Fl_vGs8gGBeZdGnFMBksD_y5Bgm4jz_MKW51IRCBYBj0SxsKwVzs8vBsTPxumujhAmTKoFfPKyCmLryLZ9EFUUXFH8PMcrL9UI4_662pVGfYFHmasb0LIjWkB16nh0w7KRKa0fxjn7MlH5oeEB6iMHt3a7yzC4cDzWE4yfLxT3z4b4ovb9RzzUFXDuy0129is_A_g71P2iIMdBG-1ennJtRPFKPYL7PBxbnDY3oBOf95PhjrKtnYcxfFEagFROMKZljnhPRR5KtTS6rQ9SLGHcubDMkZ947PwBq9cSzH8bVHK-IuWw8NkYDvkuIz4GCtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/r8J03sx4lhYFyfa0JhI1n6DCTVUxe8EZ0BxbRIYSYOweqiSCg4O8tkRYVPtyQu4xRqzKfbBuem1f_vW13rZAhFhtcCUP11cppxMqnOlx2AYzWCFUPLGIbALCY40slxw68tNPzP_GwNxqzD6LstiaWCh-cs1qau7JAXllkGwTWplriWu7G7p79lqCj4oF9OVKerw7QHKOj6mPd89Q_d9WOCwtzCxJTAKk3x8VE5R7OI9nOkP5MY9h-SQYpusI9wCALUa7QhOLWlea5ahXWrProeJh6wmqBbuT4OoZNnNhopc0bvfRuIAWhwTqaRpxaFDgCB3JUn0G8v57slqsLdDBWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sGewW7h2VuCfwqj9UKQkhv1UoK_MkYdbUml7ZW-JtAX8m7GygWCKoT4W9rCYa_jy5Au6qS_AspDuyANb9KYaljTIj4TdSGncCCYACSz2oyKD_Gzl3YuAHUwD3W6NnqPI3tlV24pEgyis-juNA_Q7DTxki3jYF9s8jWfqNifPWt3WzUDWinWcz8pmGoZNbBmRxGyehTK49pcQqFR_PhBUuuhvT8-d10XWaZjatGH9pBVfbMVyM3XI9D25Mf3wV6YeNiNS6kpvyrIcIRAKuu0ri-ct1uUNTUUXlXzfN2nBLX9G_rIa-EE5U1e6voP7Diflg-DW0USbnmOtKHMT8VbwSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/G6jyWmUguFcmR71MysNi8lP-0WHMkTvmfdh1meL5-FMxn-YFNl65hvL7LT7_xImiQIw9O28XXpo6F776gRuPoutX0LjFjsQDioaUchuENjcDKhvkKY_iAI-d3RE0A5OFJQ_YkL4ci3kWNJ-wLTbTeG0qseVW8-FoSw2pGJPnydoXepSdzvn267ZtTS8asAgPOjPLFWSyEfDLQcDwqtWC2eBNIlEA1mbVx2HlWAS0uRciRl5irZVTjuaEheD1xN5tmSLMBQblNjUoyVE12PROdx1sVyTMjlL3SWwBs9n7nkh3A69NIar0DcVQ1sRzfJss_dcuYw8-ejTYNZFa_U5gPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bPfAWlWkB_v5wlbj5UP9sAPJ1IeiGcIFLamyG3zevQLT1eDgUIIXFFiOfQop33GSdeDadwyiyKpxqaKqIH-fgHmAM_LSPANZR4CfgrrpsweN9165aJRkD3jnskB1aLmKnVSLTh88T2nBPK4wtr0RnZR39oUzv8Yeysd3bsuFt73omrpbfkWzfKHjKqE5G7bC5VNJ4nIPh0voc6dlDl3Y3ahGvF8wTNEEejQzSCB_eaNECXabOThw4HS_iIp1kx_Mws73Czvi-p5STg4J-F-zGkUWgA_vf7usq5Xhy2oKXkFqkxt92x9zy_qXJYLzYlcWW0_Sv427OzSAjcJmXFCThQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/f41tkvtT0NyVBPbfN1NlryJ1APLf945CJMG4tw8gTimKxOQknL3vVq7VO25FaFObhVQRScotBNCB83TVK96PvVtZKLwit10OJvAfVWIElBNH6lamQbHf_t3i2H1WZouc6-tOrrgDj73n2-zCv4hg7U-yIWT1XcjKci4pjkh-lr6sbIadDd1PBvJ7s7-FnQTZw_V949Vf2WsVj7t8i4ajcpCWTiU1Cxifoj2UHCGdHJ650OrYldaL3AUe-uRChwSi3TAXcQ8j0rZ2Yi4m0Nd3Obiu_XCMAg3hIzuxuMW5JRJKChX4Hct6hvJYS-QENYvWFfT7342iUGzMy5Lp8y8wmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OCm_JSLou10kGHkLm2t3pT8O6aCJedzOwlribUooBJbENQfuEP-ZtQBAA0tVG4QPdc3CxcF2mACP5FXBtItrmsTZomA6z0I975bVlr466uIh6NRDeonHvQ6s-8bo8k10nwxsVnKHCwycseIIcDzVkvq5t5kv9O4aq1MkdCsMCKlfo5_uato8poE9NLm4FJy45D8sV5ai6WU3dK3fdFlKhYBwtaVqCkOBmv_HFzq5L3eUjo_ZOZXQkL_IVTDmBG7zyx8vAcJubALLZv24mbGVoYifSoVkW8j1ZHeZxu06AMCQnIXCbXqKvgqYBJyRHJ0YwTgmtNO22DgjRoGuR5Ci0A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
رزمایش جان‌فدایان در اهواز
عکس :
محمد‌آهنگر
@Farsna</div>
<div class="tg-footer">👁️ 9.66K · <a href="https://t.me/farsna/464109" target="_blank">📅 13:01 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464108">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">پیشروی ترکیه در شمال عراق برای تصاحب اردوگاه‌های پ.ک.ک
🔹
منابع رسانه‌ای از حرکت یگان‌هایی از ارتش ترکیه در داخل استان دهوک در شمال عراق به سمت کوه‌های کاره و متین خبر دادند.
🔹
طبق گزارش‌ها، دلیل این تحرک تحویل‌گرفتن مقرها و اردوگاه‌های پ.ک.ک پس از خلع سلاح و عقب‌نشینی نیروهای آن است.
@Farsna</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/464108" target="_blank">📅 12:49 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464107">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/81d1f5367e.mp4?token=ogLKlVGaQbXlE2thFKOHhBJF5LRhgTecmS0vxXdILGNjRbtgKLKqIiGVwJ-Ei1s_CUUzJOPFyAdHsv2I-bbeDCQHqDmUmx2p86LDk2-LcV8eDt2ut5y8Sr0WQUuIgwpl29aafiixgF1tf-C-QtFEiMBNRld_sen3AtSntWx8S65YZZ7XxijFyv6uGIpqvSUE6QEX8PHVX9ENCV2SWyGFlXKXJNwZhIyTuV5ZgWisiJY7kelmBUFmqfNbP4yCtDzV_2eUOpC7g8eW1fQG0v_0TBGbrdmP_OZhwyVtbSI2di4fNgXpWZM6v0lOA3Idn3MRMZLtm4DyV5NvNiv9Ms0FQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/81d1f5367e.mp4?token=ogLKlVGaQbXlE2thFKOHhBJF5LRhgTecmS0vxXdILGNjRbtgKLKqIiGVwJ-Ei1s_CUUzJOPFyAdHsv2I-bbeDCQHqDmUmx2p86LDk2-LcV8eDt2ut5y8Sr0WQUuIgwpl29aafiixgF1tf-C-QtFEiMBNRld_sen3AtSntWx8S65YZZ7XxijFyv6uGIpqvSUE6QEX8PHVX9ENCV2SWyGFlXKXJNwZhIyTuV5ZgWisiJY7kelmBUFmqfNbP4yCtDzV_2eUOpC7g8eW1fQG0v_0TBGbrdmP_OZhwyVtbSI2di4fNgXpWZM6v0lOA3Idn3MRMZLtm4DyV5NvNiv9Ms0FQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نیکزاد: رئیس‌جمهور تصویر رهبر شهید را در مجمع سازمان ملل نشان دهد
🔹
نایب‌رئیس اول مجلس: رئیس‌جمهور حتما باید به نیویورک برود و تصویر «رهبر شهید» را در مجمع نشان دهد که چرای آقای ما را به شهادت رساندند؟ گناه او و خانواده‌اش چه بود؟   @Farsna - Link</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/464107" target="_blank">📅 12:30 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464106">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e1589e559.mp4?token=ECIsEBbHoJnF6V6yU602VaxeABZikH1WLm7ueOEOb9bMAqs6441rpzQcseO1YwV06kbKQFVa0VjtLNST96Ec9UDwLp9QoOE42L_sQ06RPR0t1fWOyzRgBoeDPFOdZOdcWPL5NWFxWzhFsJoYWs6Q1EYpbMTf42EF0WHvqh77VUUSfKRv1oedvO7GWYZXv9oSAKPacD22ICXhQZTUOOHIoBRrnfOnKkWUGAkqAjZJAA-6goCUuZ7xTklzkbGbMKXEKQHngWTZjmi5KTQ5NLQp_BO2MrcFREv3pHohE63cSoaaBy18yguYbujvMPNF7juISbIZ7pNYNlc_v-wNhRWBnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e1589e559.mp4?token=ECIsEBbHoJnF6V6yU602VaxeABZikH1WLm7ueOEOb9bMAqs6441rpzQcseO1YwV06kbKQFVa0VjtLNST96Ec9UDwLp9QoOE42L_sQ06RPR0t1fWOyzRgBoeDPFOdZOdcWPL5NWFxWzhFsJoYWs6Q1EYpbMTf42EF0WHvqh77VUUSfKRv1oedvO7GWYZXv9oSAKPacD22ICXhQZTUOOHIoBRrnfOnKkWUGAkqAjZJAA-6goCUuZ7xTklzkbGbMKXEKQHngWTZjmi5KTQ5NLQp_BO2MrcFREv3pHohE63cSoaaBy18yguYbujvMPNF7juISbIZ7pNYNlc_v-wNhRWBnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حملات جدید پاکستان به افغانستان
🔹
در ادامۀ تنش‌ها در روابط اسلام‌آباد و کابل، ارتش پاکستان خبر داد که «۱۰ نقطه در افغانستان» هدف حملات هوایی قرار گرفت.
🔸
بامداد دوشنبه ۳۰ شهریور بود که پاکستان به افغانستان حملۀ هوایی کرد. طبق گزارش رسانه‌های افغانستان، ۳ غیرنظامی در این حمله جان دادند اما منابع امنیتی پاکستانی گفتند ۲۸ شبه‌نظامی کشته شدند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/464106" target="_blank">📅 12:21 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464105">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EwTvXFz77Wlw9AMKqEj6JTGu-lesLANfLJwlotKXTh-M--zvolTfYvaV_He2dikZHPLQgD0Jq4fVh3K8e6VpPZiRGU740ICQIQKv3gQ1U9GoVBxTMI5Mu-DrVjJsSDyt0wCdiOvGRjS7i4-uR9is966Y50JewaqE2v0RlQx2bG-P5JzTDLYPGMAcD-YFY6oQEAjMHZSmDLB8F3M4RYyKnIT7t_T0ZV3duPg_rgachxQ9yBHIgMbK_DvadJa6ve3wdP-ErcdoKqFuSb5y--3S2TCNCIpEClzI_HeI0oLuJ9UJC-ORaC93qWAXnvmDJK6nKgL9RwdNJ_JzboqtHiKaUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سرلشکر عبداللهی: علم‌آموزی، ادامۀ راه شهیدان است
🔹
پیام رئیس ستاد کل نیروهای مسلح به فرزندان شهدا همزمان با آغاز سال تحصیلی جدید: امروز تلاش خستگی‌ناپذیر در سنگر علم و دانش و دستیابی به قله‌های علم، مهمترین نیاز ایران سربلند می‌باشد که فقط از طریق تلاش شما دانش‌آموزان عزیز به‌دست می‌آید و در این راه وظیفه دانش‌آموزان خانواده معظم شهداء که یادگار شهدای گران‌قدر هستند از اهمیت بیشتر و بالاتری برخوردار است.
🔹
یقین دارم در شرایط کنونی پیمودن موفق مسیر علم و دانش توسط شما دانش‌آموزان عزیز، ادامۀ راه شهدای گران‌قدر بوده و علاوه‌بر رضایت پدر شهید شما، رضایت خداوند متعال را به‌دنبال خواهد داشت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/464105" target="_blank">📅 11:51 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464104">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HeR9DafyDWOoMRtS1Zp6DEy2Wzdb7KypUMKBHdLCWCkqrGZ781Pm20nlL22C93yIbkjU_jVgKdee0mxrhMcuNadCqmY0LgJ4ZLhWcQSt17kUB67nZFd-fR41iwAi9OPJTh1Pa3CHgnqhJjeXWMatRfM4jfoFVAmBhF--olhr8INKIHIb8hiIeRqcz3OwULORLuezq4A6wjdI7CQ7eVIdxv-xibgvPm22ArvHlr4FOLFkurgsPIs9RU3IEOPBD7dbF3Wc9D52bTArMnZWW5KBKE_Mf9PIha_NTRHxyaMyaAVhAt2vBZUQ9gy_Zt3eu-EmMIMyvrxxybTJs3sftRcDAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
رئیس قوه‌قضائیه: پزشکیان در سازمان ملل جانیان آمریکایی و صهیونیستی را رسوا کرد
🔹
پزشکیان با استظهار به میراث معنوی امام خامنه‌ای شهید، با صلابت و استوار از حقوق حقه مردم ایران دفاع کرد و جانیان آمریکایی و صهیونیستی را رسوا ساخت؛ اکنون صدای عدالت‌خواهی ملت ایران در گوش آزادگان جهان طنین‌انداز است.
🔹
حقیقت امر آن است که ما از جامعه بین‌الملل و مجامع بین‌المللی، مطالبه‌گر و طلبکار هستیم؛ آنان در واکنش به جنایات جنگی عدیده آمریکا و رژیم صهیونیستی در قبال مردم ایران، سکوت و انفعال همراه با تأیید را پیشه کردند.
@Farsna</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/464104" target="_blank">📅 11:46 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464103">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RQ7JWAmKj8q8LdhIoemuirX18pyVq3pyIvf4T1sUkHtRSnely17YtPc06ATROoJIiZuFanrcysjcI8SBDb_T5jVGwP6TJDHr55B79vh5JcBcEBG-4V9a0rcgfBJSdNsjAnA-x2ofMTFblAklZTJX8hdIPTrBZYo9PTLwj8KYf2pGMzP_dxzpnM21sUCReIsfB7pHDlg_nzNAfPYztRMTFRcwQXxffP76ALd0ix8q8lQ15RNRhhvdCo270eMorBCV0_r20fUP83seZ9U7KzmTWaiPkROrj0WoA2ugTN8IZPRXbwAmWVhPXzGYs8qCMPtkKh4sApEArXUKFWzaarHWsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
سرپرست وزارت دفاع: پیام ایران از تریبون سازمان ملل روشن بود: دکترین دفاعی ایران تغییر کرده است.
🔹
سردار ابن‌الرضا: تولید قدرت دفاعی متناسب با این دکترین، با شتاب ادامه دارد و سبدی از ابتکارات و قابلیت های شالوده‌شکن و اقتدار آفرین در اختیار داریم. با ملت ایران نمی‌توان با زبان زور و تهدید سخن گفت.
@Farsna</div>
<div class="tg-footer">👁️ 8.86K · <a href="https://t.me/farsna/464103" target="_blank">📅 11:45 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464102">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/US5yClgt7ombtWe_p4OxdgYe4l94aJ2eez-Y8DPy1_RgNC8ont7QVfS5oQo5YSvkLoEx3HzPLNYR3Bs6wl5cMZx9rUO54oYrVXanW7-SnrkNcDyqcv2ldwPVA4zZ84lYuFplVe7sA-qG50HgJMUQApH2VDZ-wDWMZYRG72POJpwmAjNwxvKXYXzGW9isMUM-MppTlLfSeXhtz83lREUZDsRjU2yReXkS_1y4AS0tXhP8mFL2s67lwg2bNslvvJRB7xOIpJjMX1Cm5Le7DDysNp7dLt6yHX6Q8igCO2cySETe9tOs2y0id8lULI5eLrjRqx66op6dLIx9XoxvbaWAlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پزشکیان: دانشگاهیان، دانشگاه را به محیطی برای حل مسائل کشور تبدیل کنند
🔹
پیام رئیس‌جمهور به‌مناسبت آغاز سال تحصیلی دانشگاه‌ها: در این سال تحصیلی انتظار می‌رود دانشگاهیان با حفظ چراغ علم و پژوهش، اخلاق، گفت‌وگو و نقد مسئولانه، دانشگاه را به محیطی برای پیشرفت علمی، کرامت انسانی، نوآوری و حل مسائل کشور تبدیل کنند.
🔹
دانشگاه باید فضایی باشد که در آن دیدگاه‌های گوناگون در چارچوب قانون و اخلاق علمی مطرح شوند و اختلاف‌نظرها از مسیر گفت‌وگو و استدلال به فهم و راه‌حل مشترک تبدیل شوند.
@Farsna</div>
<div class="tg-footer">👁️ 9.57K · <a href="https://t.me/farsna/464102" target="_blank">📅 11:33 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464101">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec9ae3f81b.mp4?token=Bv8N7WUtXZX4QBad28IhS6p8BeETmhcwanVlWsHckQyMXJG6qvdj3dH8GiMQZy5K3lXwgOxhrHx6fJ8dbuvdOdH5qzNDiI8tgqVDD-1XKKLVcu374tB08iHyTM38ImxCVoNxKX5v9-5vIk9noCgthOAY12B0b8ol-coXH5CEG48oAyWzeTUhFZReJsFfQ1CSNY5WTi-n_7_rwTflCxLM_ox7lOutZCRVrFqvg4r_mWaL04JKCHK2xpqEkAvqFlPy4F5eRa5by3kgt9c-W-a7mgAq3O8oe56jwjzt0jRgzCiSnWk14ob5BurrLxpQ1SqNr_-_gI_1VIK-qm7TgWcYZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec9ae3f81b.mp4?token=Bv8N7WUtXZX4QBad28IhS6p8BeETmhcwanVlWsHckQyMXJG6qvdj3dH8GiMQZy5K3lXwgOxhrHx6fJ8dbuvdOdH5qzNDiI8tgqVDD-1XKKLVcu374tB08iHyTM38ImxCVoNxKX5v9-5vIk9noCgthOAY12B0b8ol-coXH5CEG48oAyWzeTUhFZReJsFfQ1CSNY5WTi-n_7_rwTflCxLM_ox7lOutZCRVrFqvg4r_mWaL04JKCHK2xpqEkAvqFlPy4F5eRa5by3kgt9c-W-a7mgAq3O8oe56jwjzt0jRgzCiSnWk14ob5BurrLxpQ1SqNr_-_gI_1VIK-qm7TgWcYZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دیدار پزشکیان با نخست‌وزیر ارمنستان در حاشیۀ اجلاس مجمع عمومی سازمان ملل
🔹
پزشکیان در این نشست گفت: سیاست قطعی جمهوری اسلامی گسترش همکاری‌ها با کشورهای منطقه و همسایه است، و در این خصوص دولت همۀ تلاش خود را برای اجرای توافقات به‌کار می‌گیرد.   @Farsna</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/farsna/464101" target="_blank">📅 11:18 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464100">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6b4aebe9d3.mp4?token=ABcSZsNPsot4KrTKx5TLK3i9KZRyT6JqgqJpiM9s4MyH_l4dzmuxe9eeZcI3z3Ax8ttzQ8pQhUkSc5EnntXGoHITlyQ_EHGkIGYSwUeYij7UT4meJrdjBV-embaGZ7EgHTeG0gIyREcLPTJxj4iBVDEal_Ft489cJW5-Hh4g7Ni-VSh-tqKC_k6_Ye-K6jpRCut8o-mGKdQ84XICgemMm-BpPdOlJdNQpTGSoTF_MFt1cwZcoqfoH1V2U5NNnW7w6o_maMC1glm9HFvepjjC5iQMWw0OFC_pTWwB8Eij07C8DxZ7GuugRG--vtqLDN9Yl47KkstTqgGL86IxDSq9FA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6b4aebe9d3.mp4?token=ABcSZsNPsot4KrTKx5TLK3i9KZRyT6JqgqJpiM9s4MyH_l4dzmuxe9eeZcI3z3Ax8ttzQ8pQhUkSc5EnntXGoHITlyQ_EHGkIGYSwUeYij7UT4meJrdjBV-embaGZ7EgHTeG0gIyREcLPTJxj4iBVDEal_Ft489cJW5-Hh4g7Ni-VSh-tqKC_k6_Ye-K6jpRCut8o-mGKdQ84XICgemMm-BpPdOlJdNQpTGSoTF_MFt1cwZcoqfoH1V2U5NNnW7w6o_maMC1glm9HFvepjjC5iQMWw0OFC_pTWwB8Eij07C8DxZ7GuugRG--vtqLDN9Yl47KkstTqgGL86IxDSq9FA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سرلشکر صفوی: برای دور جدید جنگ احتمالی با آمریکا آماده‌ایم
🔹
دستیار و مشاور عالی فرمانده معظم کل قوا: چون اطلاعات راهبردی نداریم، نمی‌دانیم در مغز ترامپ و نتانیاهو چه می‌گذرد.
🔹
نیرو‌های مسلح ما بسیار هوشمندانه سناریوپردازی می‌کنند و برای بدترین سناریو‌ها…</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/464100" target="_blank">📅 11:15 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464099">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/26777730d2.mp4?token=K86GXAFWcbL61RkQHJJPZ62QZu1oqHRpcLqVQaTNF2jwjIfKGFV4Ca8xMEG9q_UVS1O9CWa-xg_bMNaN9oAyENnymsO6UUK44JR_i9wCq8olsDt3-PNiMx2LyvCnAsc7i_r5i_hxRv9GHyPfJb3e663yXhgJ8EHxjuGMwWHLXZGG2rIToyNl1SrLT9pbQ1lTRPOb1CUay-xYQrIsaO0Q3bXd6cvZ_pHxXYint1Z-dCxEwNxGoUTRxrwSCIXofPpZBvrpQXIlavt-3x1N9vtibQX2lK4qM3proK2lDO1MvFkkrqkfdOG_QBymECcKemDMBOrg0bUvvNZlbHEuHiQXcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/26777730d2.mp4?token=K86GXAFWcbL61RkQHJJPZ62QZu1oqHRpcLqVQaTNF2jwjIfKGFV4Ca8xMEG9q_UVS1O9CWa-xg_bMNaN9oAyENnymsO6UUK44JR_i9wCq8olsDt3-PNiMx2LyvCnAsc7i_r5i_hxRv9GHyPfJb3e663yXhgJ8EHxjuGMwWHLXZGG2rIToyNl1SrLT9pbQ1lTRPOb1CUay-xYQrIsaO0Q3bXd6cvZ_pHxXYint1Z-dCxEwNxGoUTRxrwSCIXofPpZBvrpQXIlavt-3x1N9vtibQX2lK4qM3proK2lDO1MvFkkrqkfdOG_QBymECcKemDMBOrg0bUvvNZlbHEuHiQXcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سرلشکر صفوی: برای دور جدید جنگ احتمالی با آمریکا آماده‌ایم
🔹
دستیار و مشاور عالی فرمانده معظم کل قوا: چون اطلاعات راهبردی نداریم، نمی‌دانیم در مغز ترامپ و نتانیاهو چه می‌گذرد.
🔹
نیرو‌های مسلح ما بسیار هوشمندانه سناریوپردازی می‌کنند و برای بدترین سناریو‌ها هم طرح‌های خودشان را آماده کرده‌اند تا اگر به هر شکلی آمریکایی‌ها و صهیونیست‌ها مجدداً مراکز و منافع ملی ما را مورد هجوم قرار دادند، این دفعه هم جبهۀ جنگ گسترده‌تر شود.
🔹
حالا که جنگ از خلیج فارس و تنگه هرمز به دریای سرخ گسترش پیدا کرده، ممکن است در پاسخ‌گویی در مرحله بعدی جنگ احتمالی (با ایالات متحده آمریکا) این جبهه گسترده‌تر شود و تا اقیانوس هند و یا جا‌های دیگر هم گسترش پیدا کند.
@Farsna</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/464099" target="_blank">📅 11:05 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464095">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZN1_PMttGTx4Fhc6rHNRqgeI9AIGx1APG6b52QA_CjN-paUlk4SOjK07AWYBAJFiwVtB_SMVnM9eDyzFU8_BoQ9-fcOHlg9K3lloCGEcs7Nu3NTFjxYER60IKDxGO63gZyPqXcyqavHvsQ39whgDhpVtAfOZD5qxKCbwnu7kS2xWm2k_qIdBA3SICJo5kBvcC_fW0DPFUJqkvuugiVnp0S9MXDKu_LPOyWjDUWb7wGaj2tqXNJEj574jYX2t8AvkY9dxRnjq5V9TfWIVBAfySrvGNuaw9BWHy05Uodu8SRkKiUR3X_9WbsJQnzvgsacAACri1--14WC_nS9bzmhikg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gBsVfmqsw7nD77Vdy18YUjYPUmqMyILFZEnDTG4RYWKojY0HdJx7lMhn4mfnt3MFnIXWVtUioXser2hpXpauwOoLBCUyvni2Cy0NVFQkLszp6WHj2dLS8lvqYcScQ3Qq6FbZfInDkHAfPYs4eYKTEUc5ODrsr-e34FL5qaB6BwDJzTIDxSlS7Y-7HZyLVZQkzw1zyOkwv8IEC0eVp_8gTVDKFNWLe2HJULZxaYtKP_wfjeVt1LXPEYrqYD9kqDya5oMMUJnwwqmdj-lzV7d10XlEN4LuvIc3H_5JHVG0xG4H4LsvNCt2DTbRlN3m324_vPgL39gKNjx_O4_nYkcLfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vDRri8LBAvhE8S-uK6Y_t4BMBKasZd5QEzl4sCo-5zKyB8f5Ie07SRe9V06ItTKoPlRua__IRblCMJMXWgYh9S3pxyHHFckeRDY3tHsP-RLt6a4G0AsoVeePJKPwvI_HqaY40srXNNKu3qgGUn-MT4cx48PktO98JJI45L6QplullP4ZIO1mGi1idaDqOAX29aG0KuWUuBGfP48o6TrkQmYr4svXocib42U1KrcQ0NufTXZ7qCauXta2Ub9M0uDUhSxcafEzlti0vOlxI4u6EJzW-dopwKoBKM20QOscVN9xYKMGjskSNqwnKsleJ-qKZVpsCYnYDDYX4Jf-WIAgHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uJCQUWTmYlAjI3u3Gt0fGIFyshyu82D64nOI2QtV65gSU5fFnTmwsPCetQLL3DjQZx8UhohhHJiLbObQfE4Y9nl3s3WkVbL5UUmehijUikyz0dvuUo6EnzEsYKuGyPo-0C7DzE0GT9-EPwUHvvsdH05mnizeNC0zrRe6XD0nYTphfhORvYRClnacqYG-dAFNWtlxBwlnaPMkVS0766SPOH4gy20uoJ68wu6AcazfuJwoXbZvCqWOK11PIF068H5u8Ndcwu_00OUh4gQ6D6ebbS6yvpe2K1YxIrPRTSLV1FWKobtDlPxx-IrBcwImbxmnGUdfJ_6XsR8RCLw4I1M-8w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
چابهار در مسیر اتصال به شبکۀ ریلی کشور
🔹
همزمان با پیشرفت پروژۀ راه‌آهن چابهار ـ زاهدان و پایان ریل‌گذاری خطوط اصلی و فرعی، وزیر راه و استاندار سیستان‌وبلوچستان از ایستگاه راه‌آهن چابهار و روند اجرای این پروژه بازدید کردند.
🔹
با اجرای این پروژه، چابهار به‌عنوان تنها بندر اقیانوسی کشور، به شبکۀ ریلی سراسری متصل می‌شود.
🔹
پروژه راه‌آهن چابهار–زاهدان دارای ۶۳۰ کیلومتر طول مستقیم است و طول آن با احتساب خطوط فرعی پروژه به ۷۳۵ کیلومتر می‌رسد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/464095" target="_blank">📅 10:33 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464094">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/28109c764d.mp4?token=V8HGZgFcaxF8GsB7tY9FancnIJkbDzWT5QxgqEIB6nchc3udc3lX0tN1nq9X-gZryvpNce52AorGrcpiwpPAKHvJAqW1k5hoJtGPVPqu37vYJ5W4bTMmsyBiF5hd7woYtuGJvRBXpSGhM_AZnMEB_SILQUlSAkCnSfld-lnjguadmOBhJKtf3SzuBDC_UtlFoyq2QrRvk1ClCZ4yj_PYtTK524-PVDntAHv4Y9Vid_09LrHZmcWVGkCH-ADa4VAd___sT_ij5uk-HdmtfVACaon6ks-nYiiiZSlF122MJT-2B1KVKyOqcl2mOl_2_zu3rg5Ekwh3I9gZtvgz4z3Lcg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/28109c764d.mp4?token=V8HGZgFcaxF8GsB7tY9FancnIJkbDzWT5QxgqEIB6nchc3udc3lX0tN1nq9X-gZryvpNce52AorGrcpiwpPAKHvJAqW1k5hoJtGPVPqu37vYJ5W4bTMmsyBiF5hd7woYtuGJvRBXpSGhM_AZnMEB_SILQUlSAkCnSfld-lnjguadmOBhJKtf3SzuBDC_UtlFoyq2QrRvk1ClCZ4yj_PYtTK524-PVDntAHv4Y9Vid_09LrHZmcWVGkCH-ADa4VAd___sT_ij5uk-HdmtfVACaon6ks-nYiiiZSlF122MJT-2B1KVKyOqcl2mOl_2_zu3rg5Ekwh3I9gZtvgz4z3Lcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: بعد از شنیدن سخنرانی رئیس‌جمهور آمریکا، متن آماده شده را تغییر دادیم
🔹
در مجمع عمومی سازمان‌ملل از حقانیت ملت ایران دفاع کردم. ملت ریشه‌دار و متمدن ایران نابود شدنی نیست.
🔹
ایران را نمی‌توانند نابود کنند؛ ایران کشوری است که ریشه در تاریخ دارد و علی‌رغم تمام فشارهایی که وارد می‌کنند، مردم ما در صحنه حاضرند.
🔹
متنی را از پیش آماده کرده بودیم تا قرائت کنیم، اما وقتی سخنرانی رئیس‌جمهور آمریکا را شنیدیم، نگاهمان از آن متن فراتر رفت.
🔹
سعی کردیم واقعیت‌هایی را که آمریکا بر ملت ما و دنیا اعمال می‌کند، بیان کنیم؛ چرا که آن‌ها بر خلاف تمام قوانین بین‌المللی و چارچوب‌های انسانی عمل می‌کنند و جز اعمال زور و کارهای ضد بشری، اقدام دیگری انجام نمی‌دهند.
@Farsna</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/464094" target="_blank">📅 10:17 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464093">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UYBicIYdEIzm3kWD5nPaC5ZHymxNHEKakSRUU_VyDzdjanT_89JNva2AF263lRojGz8rYQzJ5lvqL2pLJFgOmjsuwJ6R5erUaojDU8jLSUhpxkOEu9Z0BBrMkDG7LU07yewVP14cXfd3NtPdbGszkrmlQjSdazJcVYMXfuXioqsD7f3XN_eE7OHYtGpCFOAQ04s5SyUatrzHm66QZupX0gIBP6yMYUvA8qximtqV0OlpktUAWwgFwnfrMrs-T83aTieLK4tn8PhreqEnmnBatFc3bbi6uWohitRXbaoKWxrAJAfu5y3YyWH1CuQ3ZviUEp0Zwi1uVekjymEee2iNpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
تحسین بروجردی از سخنرانی پزشکیان در سازمان ملل
🔹
عضو کمیسیون امنیت ملی مجلس: پزشکیان از موضع اقتدار و شان ملت بزرگ ایران و از جایگاه ریاست جمهوری اسلامی ایران در سازمان ملل سخن گفتند و بازتاب گسترده‌ای داشت.
🔹
هم دل ملت را شاد کردند، هم نخبگان جامعه تحسین…</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/464093" target="_blank">📅 10:10 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464092">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">متهم پروندۀ شهادت حسین حمامیان دستگیر شد
🔹
رئیس‌ دادگستری سمنان: یکی از لیدر‌ها و متهمان اصلی حوادث و اغتشاشات دی‌ماه ۱۴۰۴ در شهرستان شاهرود که متواری شده و مدتی در استان‌های مختلف مخفی بود، ساعتی قبل دستگیر شد.
🔹
این متهم در ارتباط با پروندۀ شهادت مظلومانۀ شهید حسین حمامیان، از شهدای مدافع امنیت شهرستان شاهرود، تحت تعقیب بود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/464092" target="_blank">📅 09:56 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464091">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">صدای شنیده شده در آبادان به‌دلیل نقص فنی در پالایشگاه است
🔹
استانداری خوزستان: صدای شنیده‌شده در برخی مناطق شهری آبادان به‌دلیل نقص فنی در یکی از واحدهای صنعتی پالایشگاه است.
🔹
متخصصان درحال برطرف کردن مشکل هستند. هیچ‌گونه خللی در تولید بنزین ایجاد نخواهد شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/464091" target="_blank">📅 09:47 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464090">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c42d5eae8.mp4?token=GAZkd7QCfPH66o63mjW3i1UU0xW0KfzU7sHpcEbYss58WcKXnn204u-koLfypLypxYgru3ZVGSQDZZgWfcyWc7HtlVjmSIFEUj7t1WzNEjjsUl5ldeMtD2DgswVNMvo7oRlYAffpads3AUetchve9elH9AT4YfP252pjqXxQkF9_B6S8H70VxaOs-5z7EXwM3au7M0tPqHNe8yjP3TUzrZY8S02OStvSWrmowDJvpxKYL7ctf5Qx4gGCLyI9zHh4zLJfFqcubYvJIeIZ697__i3lXF5bTd4c15vFXUo2kWGgaP4yWuJfIe8cuXJYv2nwg9yDsiJQIY_T8JOz_W9DuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c42d5eae8.mp4?token=GAZkd7QCfPH66o63mjW3i1UU0xW0KfzU7sHpcEbYss58WcKXnn204u-koLfypLypxYgru3ZVGSQDZZgWfcyWc7HtlVjmSIFEUj7t1WzNEjjsUl5ldeMtD2DgswVNMvo7oRlYAffpads3AUetchve9elH9AT4YfP252pjqXxQkF9_B6S8H70VxaOs-5z7EXwM3au7M0tPqHNe8yjP3TUzrZY8S02OStvSWrmowDJvpxKYL7ctf5Qx4gGCLyI9zHh4zLJfFqcubYvJIeIZ697__i3lXF5bTd4c15vFXUo2kWGgaP4yWuJfIe8cuXJYv2nwg9yDsiJQIY_T8JOz_W9DuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بازتاب گستردۀ سخنان رئیس‌جمهور در اجتماعات شبانه  @Farsna</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/464090" target="_blank">📅 09:23 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464089">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kJzb83Red-veKuPJSQZ2MnAR5OhkLMbdlDyZZRtv7LiavlMcB9EzC-rBBvYJsBiwSQJJvetm9OKuDNNf4sBR2hk297GI7g4ccVXElgHkt9zdNsQ3m_qBSIMUa_rq62SkhxnK2_MXtAOEDA-MlgOaPw36TFTizvAxGrWWjwQmdDrzf4K3NyyQB5l7J5Y72Fv3OPpaVXstRKqCrewgpQpCSzcDZpPxtp-dB7ZZ0fK0xIHHZXbgbwncFDhfdBD6IDa8SAhr_7AWlXv_6MJ01sdYehJKcAdSwivfr5168PD0TbdjMbaihnhLryhi1ekGEBxO2Ayr4v3Tpc7TmQuWBiYTGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بانوی روئینگ‌سوار، چهارمین طلای ایران را صید کرد
🔹
فاطمه مجلل در فینال تک‌نفرۀ سبک‌وزن زنان با ثبت زمان ۷:۲۴.۵۷ به مدال طلا دست یافت.
🔹
این اولین مدال روئینگ و چهارمین طلای کاروان ایران است. @Farsna - Link</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/464089" target="_blank">📅 09:18 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464088">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fbe6f0800c.mp4?token=B5KmlqBDflVvfYt8tRQq9RsapLN-vcFQkOnuG8ZaYhEMJ8RpQOIM9s6F_v2GNUcWqHzLOJyQwfZsH1Kx1tT5X6qb_9jLgzoe1HWVfw8QuHQdCJiX6nrcpzmALB096uzFHNV7jqfPgUTEE0X7c779C3oF8q3HmAkWvgbKWBmDD3IIqTW9X3R6karc_ScbnZVqGxadklY2hTs6zvI2refZ8wKTz0_ElfLRihzNLnkQusu8ZH8VjbHI3f6Hl1am0XdBmbXoZit6rBO3-D-Q4FDPRyExbaku-GAzPkyZRgYBgVNHFjn0hSQ7AvhSXLCZhgZdrnGBlEEB56NHaRSGYY8n3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fbe6f0800c.mp4?token=B5KmlqBDflVvfYt8tRQq9RsapLN-vcFQkOnuG8ZaYhEMJ8RpQOIM9s6F_v2GNUcWqHzLOJyQwfZsH1Kx1tT5X6qb_9jLgzoe1HWVfw8QuHQdCJiX6nrcpzmALB096uzFHNV7jqfPgUTEE0X7c779C3oF8q3HmAkWvgbKWBmDD3IIqTW9X3R6karc_ScbnZVqGxadklY2hTs6zvI2refZ8wKTz0_ElfLRihzNLnkQusu8ZH8VjbHI3f6Hl1am0XdBmbXoZit6rBO3-D-Q4FDPRyExbaku-GAzPkyZRgYBgVNHFjn0hSQ7AvhSXLCZhgZdrnGBlEEB56NHaRSGYY8n3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
هواشناسی: از فردا بارندگی‌ها در شمال کشور آغاز می‌شود
و تا روز دوشنبه ادامه دارد.
@Farsna</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/464088" target="_blank">📅 08:53 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464087">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e2cb105f6.mp4?token=FJ7HT-yH_aN2J30xIdIMUMHnC8iJYDJNveaf1UzzJYsu5t60CjJmzQ5Lj0CnB5YilBBuAK6d97_7EVlstFdKgXbYwySgohxLfcKw73lTjC6q54E9M3QXDFgtHZ8Lgixn13ZwLMSTGrTUNDPeQ7F2m_GhO9sVOj5-DZYqUvFTsQdIaCjgNZM1aXlJW--eNZlqiZFR0NFnrHkLtftfKtdjtl8oQZVsNWoBruHxf5CZn5bguS6RPUPPWJM0NKossZ4bfVNb_OZm_DmCKuRQd0sY-2rj1c_qDk4hFkP487-t3Hn8-RbcaTfjzu6e57PAk9-MpS6wx47i0UxONVNztEFZLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e2cb105f6.mp4?token=FJ7HT-yH_aN2J30xIdIMUMHnC8iJYDJNveaf1UzzJYsu5t60CjJmzQ5Lj0CnB5YilBBuAK6d97_7EVlstFdKgXbYwySgohxLfcKw73lTjC6q54E9M3QXDFgtHZ8Lgixn13ZwLMSTGrTUNDPeQ7F2m_GhO9sVOj5-DZYqUvFTsQdIaCjgNZM1aXlJW--eNZlqiZFR0NFnrHkLtftfKtdjtl8oQZVsNWoBruHxf5CZn5bguS6RPUPPWJM0NKossZ4bfVNb_OZm_DmCKuRQd0sY-2rj1c_qDk4hFkP487-t3Hn8-RbcaTfjzu6e57PAk9-MpS6wx47i0UxONVNztEFZLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
واکنش سرد رئیس‌جمهور چین به تلاش ترامپ برای قدرت‌نمایی
🔹
در جریان استقبال ترامپ از رئیس‌جمهور چین، یک جنگنده در ارتفاع پایین به پرواز در آمد تا به زعم ترامپ قدرت ارتش آمریکا به رخ شی کشیده شود اما تصاویر نشان می‌دهد خودش بیشتر تحت تاثیر قرار گرفت.
@Farsna</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/farsna/464087" target="_blank">📅 08:46 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464086">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee735f735f.mp4?token=i5hJGov7ScXp3m9JjPJEtpTI0CXwUzECgWOPW2-PSFD-XVdvlwer79ffnFHC42mabWr-xkFeBC478oYPi7HgoZIg0nji4B16eNAyP-ScPLe9cR68GyDep_xmblUQDrmBcH6kPo0DI-EybxbPlFCopQDyuHDxngxC_-_iwlW7VKLEE0ntgqz-Q3ARxcip3vWwwk9bglNk68exs3l7-D0-GMmETBSoNPd9yQL-F-eMYJecq4SQ6qICR1OPA5eEl_xoITGNeCW4ht_u0ofF5uK0fwxaGXDrX9w3wypjwk_HKXO7Py3KxVz5IKJffzsy-SP66YQ9TnUvGxfoHHM8ZgLiQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee735f735f.mp4?token=i5hJGov7ScXp3m9JjPJEtpTI0CXwUzECgWOPW2-PSFD-XVdvlwer79ffnFHC42mabWr-xkFeBC478oYPi7HgoZIg0nji4B16eNAyP-ScPLe9cR68GyDep_xmblUQDrmBcH6kPo0DI-EybxbPlFCopQDyuHDxngxC_-_iwlW7VKLEE0ntgqz-Q3ARxcip3vWwwk9bglNk68exs3l7-D0-GMmETBSoNPd9yQL-F-eMYJecq4SQ6qICR1OPA5eEl_xoITGNeCW4ht_u0ofF5uK0fwxaGXDrX9w3wypjwk_HKXO7Py3KxVz5IKJffzsy-SP66YQ9TnUvGxfoHHM8ZgLiQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: ثابت کرده‌ایم که از جنگ نمی‌ترسیم و تا پای جان برای دفاع از ایران ایستاده‌ایم
🔹
بمب اتم در دست اسرائیل است اما آژانس از ایران بازرسی می‌کند. اسرائیل ۷۰ هزار نفر را در غزه قتل‌عام کرد اما ایران بمباران شد. @Farsna</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/farsna/464086" target="_blank">📅 08:15 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464085">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e440cbc01.mp4?token=bbFljElDWWOSF54Ciq6XuIQWGFYv3WI2Fx7lED1JrG9ZJevRoriyRVZDLss83I3TdEVGo9Ug7IVR4Mq7HU5FNbJ5ZcLqwnFDpRjxzLWGR-snEUZ3tiUuZFSknTPiL3V_SY9f4gM0LBwp87zjnEhNn2l0Bp548qh1P0ym56J80916nYtEOIsxwepeL9C0bHSIEBJDEI16jUDk3zIPNPi4gyBhxbadj--NiaC3EPUv-qtXChIhXSoGS2MEL-_Y-uqaQHjeP44fR0c452MLiip0QOhuZWb28CrRk6XqcA2l5RDSCBtRPA8ThN-O9pOvCqSHFmLaBzC0PT1rCxuICHYC9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e440cbc01.mp4?token=bbFljElDWWOSF54Ciq6XuIQWGFYv3WI2Fx7lED1JrG9ZJevRoriyRVZDLss83I3TdEVGo9Ug7IVR4Mq7HU5FNbJ5ZcLqwnFDpRjxzLWGR-snEUZ3tiUuZFSknTPiL3V_SY9f4gM0LBwp87zjnEhNn2l0Bp548qh1P0ym56J80916nYtEOIsxwepeL9C0bHSIEBJDEI16jUDk3zIPNPi4gyBhxbadj--NiaC3EPUv-qtXChIhXSoGS2MEL-_Y-uqaQHjeP44fR0c452MLiip0QOhuZWb28CrRk6XqcA2l5RDSCBtRPA8ThN-O9pOvCqSHFmLaBzC0PT1rCxuICHYC9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
افسردگی و اضطراب یکی از عوامل مهم اعتیاد است
@Farsna</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/farsna/464085" target="_blank">📅 08:04 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464084">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6ab34188e7.mp4?token=jleMakeLuZzcS9U6nRIR2QKeCVQr7d53IkWA0RJ-Bz9MMUZt14g8J4SFPvL1dm8kpFaNfpCmTbe1UdTXIv1E9hbFKKafsHNpbY36db3wRHj0FU-YZzeAl6f8BeAWIplAqayRmWAqlNLxCttgQ5dnFxsI1x6IlQXm4G4ijs0-dUu3JI6jE9o3XHi_QV2WBk0Tw9n9IegXzNQEfRvLHRZiFoXE4iukAT8l9kqryTBQDblVoP28ora0eNZNTXGX4vrJWSEewYVFJAlmNptbWRGi4IuPm67bh_7alNEONdA9XrD4GEIELwENQ9qkc4wqEBqpJH5vR6li7yeSIELHpHxdoa-LdlRkz-Z6iTQNERvMZAT9ke8gZ_PXttBatKtDvyC1S13aVUc-9TQ5dd2jvhMEOWRrk-n__H2SetPXbXtoKi6YdH8FZ-d2cIiijWBK_0bDuJyMI8VxOGWSbzytyaIZerFkqDEBLwNpsQBCFQgoZsz5gT43cSQZPWwiX6KL9dahVd4V3TzF18dwYrOX40I3vVT1HNtMkp-gQtPwEidPbTUyPRUqf_6Kq0uSQrVNL7ea6H4GnBrAs6fr5CBTId-bCi1jwL0HHmaTg9nhl1JwzQ-GdXBP25F3BfILQrzbu-YGaQSyCoe4UrwnCTOxXlT1rzifFq3Xi7RN7JjX9C7fxA0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6ab34188e7.mp4?token=jleMakeLuZzcS9U6nRIR2QKeCVQr7d53IkWA0RJ-Bz9MMUZt14g8J4SFPvL1dm8kpFaNfpCmTbe1UdTXIv1E9hbFKKafsHNpbY36db3wRHj0FU-YZzeAl6f8BeAWIplAqayRmWAqlNLxCttgQ5dnFxsI1x6IlQXm4G4ijs0-dUu3JI6jE9o3XHi_QV2WBk0Tw9n9IegXzNQEfRvLHRZiFoXE4iukAT8l9kqryTBQDblVoP28ora0eNZNTXGX4vrJWSEewYVFJAlmNptbWRGi4IuPm67bh_7alNEONdA9XrD4GEIELwENQ9qkc4wqEBqpJH5vR6li7yeSIELHpHxdoa-LdlRkz-Z6iTQNERvMZAT9ke8gZ_PXttBatKtDvyC1S13aVUc-9TQ5dd2jvhMEOWRrk-n__H2SetPXbXtoKi6YdH8FZ-d2cIiijWBK_0bDuJyMI8VxOGWSbzytyaIZerFkqDEBLwNpsQBCFQgoZsz5gT43cSQZPWwiX6KL9dahVd4V3TzF18dwYrOX40I3vVT1HNtMkp-gQtPwEidPbTUyPRUqf_6Kq0uSQrVNL7ea6H4GnBrAs6fr5CBTId-bCi1jwL0HHmaTg9nhl1JwzQ-GdXBP25F3BfILQrzbu-YGaQSyCoe4UrwnCTOxXlT1rzifFq3Xi7RN7JjX9C7fxA0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رزمایش ۴۰ هزار موتورسوار «جان‌فدا» جمعه از میدان امام حسین(ع) تا میدان آزادی برگزار می‌شود
🔹
ثبت‌نام علاقه‌مندان تا ساعت ۲۴ امشب در مساجد و پایگاه‌های بسیج انجام می‌شود.
@Farsna</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/464084" target="_blank">📅 07:56 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464083">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">محدودیت‌های پلیس برای ترافیک پایان هفتۀ جاده‌های شمال
🔸
تردد موتورسیکلت‌ها از ساعت ۱۲ امروز تا ساعت ۶ صبح شنبه در محورهای کرج-چالوس و هراز ممنوع است.
🔹
تردد تریلر، کامیون و کامیونت در محور کرج-چالوس همچنان ممنوع است. روزهای پنج‌شنبه و شنبه درصورت افزایش حجم ترافیک، محدودیت یک‌طرفۀ مقطعی در مسیر رفت یا برگشت، اجرا می‌شود.
🔸
از ساعت ۱۴ روز جمعه تردد خودروها به مقصد چالوس از ابتدای آزادراه تهران-شمال محدود می‌شود و از ساعت ۱۵ نیز مسیر در محدودۀ پل‌زنگوله به سمت چالوس به‌طور کامل مسدود خواهد شد.
🔹
از ساعت ۱۶ روز جمعه، مسیر مرزن‌آباد به سمت تهران یک‌طرفه می‌شود و این محدودیت تا ساعت ۲۴ ادامه دارد.
🔸
تردد کلیۀ تریلرها در محور هراز ممنوع است و عبور کامیون‌ها و کامیونت‌ها، به‌جز خودروهای حامل مواد سوختی و فاسدشدنی از ساعت ۸ تا ۲۴ امروز پنجشنبه و جمعه امکان‌پذیر نیست.
⚠️
امکان تغییر محدودیت‌ها باتوجه به شرایط و حجم تردد وجود دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/464083" target="_blank">📅 07:48 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464082">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nR7fgY7ZBLEByIrm1waOlBpuxu6g6GWlYwbBgkVsHLkNVsHT-bGRPiTUqbK5GYfJWWf5S1NwwMfMxb_rL8tux-RU8pWnupZu9LBV5hrNWvAT-cfZY9a9gVXrIeP7pjVGRLwvEgLCJDi8LOzQgYd6VBkhyCjiOBR81KsJRZCK4dCLrVZMSySTniyAR2mXOWhc3kGOQU94TM35Wf8ihSOTmcqFhyooiBPFk2VRlDcjpiVvn_xDKxd6MJB6aIfbYLGYTCUccQ_CtF-ffHptQzI9JaFOJXIdOBtamDTuNpZYvH7gSd1YVj8E2NU2Xaf2ajPvHMLT7wdzf9f0-_yUnQCFWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاهش دورۀ آموزشی سربازی متعهدین خدمت آموزش‌وپرورش به یک‌هفته
🔹
متعهدین به خدمت آموزش‌وپرورش که از سال ۹۳ به بعد تعهد خود را آغاز کرده و هم اکنون دورۀ تعهد خود را به اتمام رسانده‌اند، می‌توانند دورۀ ۲ماهۀ آموزشی را در یک هفته طی کنند.
🔹
وزارت آموزش‌وپرورش باید قبل از بکارگیری فارغ‌التحصیلان در دانشگاه‌های فرهنگیان و شهید رجایی، برای برگزاری دوره‌های آموزش رزم مقدماتی در مراکز آموزش سپاه اقدام کند.
🔹
افراد واجد شرایط باید با هماهنگی اداره کل آموزش‌وپرورش استان محل سکونت، درخواست اعزام به خدمت خود را از طریق دفاتر پلیس+۱۰ ثبت کنند.
🔸
سایر متعهدین آموزش‌وپرورش نیز باید قبل از شروع تعهد خود نسبت به ثبت درخواست اعزام به خدمت و طی دورۀ آموزش رزم مقدماتی از طریق دفاتر پلیس+۱۰ اقدام کنند‌.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/464082" target="_blank">📅 07:22 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464081">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">هوای تهران «قابل‌قبول» است
🔸
شاخص امروز کیفیت هوای پایتخت روی عدد ۸۴، و در وضعیت قابل‌قبول قرار دارد.
@Farsna</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/464081" target="_blank">📅 07:11 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464071">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XNdmp30wrclqkhHtkLIoej-vArOOtlEEu5kTzSF39gu_cuO_2ZjXdx1Z7yDPWc9dx6Mhu10c7JeBXQTY8cRBb-B82OrGCdSc3ACbeGc1YWofh6wfvbb3HZlE9ndMFErJtXp0nHNhEIfNp9LjPpAxgQ3DpC0yJOKiPse2nVXekfolGGV2x9D-x6ErczBMZwX9hcMDKFrSO3gxk02gjorgoOncUGbG_dy6cjCx0e2Y1r_7btOqWsg99RPwlyG26V60cjliT6-b8wbNqa6JLVGRmzlBkG0SB-X_rnockIlFH0qhKgWzAHcMPtKV5pO1Yz-91SLOjRh_XSH0Pi6M-Gnytw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RXj40naIzQ9itxm6OAhQzGr9CellEp2KX9E9cFXjSlgKkkweaFIe_hFahyvg0PBQmWd6Ukba3T_Mi8nP_QhtiWFnGLprbfKtcwdjCsvwvbFwI8iwThQiqUPXI4LRZg8hbblKtqyEBdvp0jYuBXDAVLfC0FX94QUYM_genG0hLGpe_CFOn33jGJdJqxWTYKXXqPtqX-rK_K-7IIVRO_Nijlz1e0jm7J_Xwywth3QGsonQDpzmXe59-a0WfAl9IQJmGkPoUmCFNU7bBj9xSd9-40hm2hYNUsy5cuH6LEc5SBctd2tjiq8y0vN1kfOJTspd6Z-yXVsMmJkBlDmNBVuApA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MdcDMuC5uZke5v-jY5DSO1zKgy6KLjVo108zwB8GSaQrl6R7kxaM4eyNSB3MjrZL3C-JAXanvMm6B18RFh5edGkK7LShc5cuOU5JgErNHtQAp83ptXFWV7nGTdYX7OueOKKvaTWrjErGoEXaZnljeqp5ofPah8rvIMZpKblbh2kJcuCwlZ6UtomUD_7zzoAsdk5SjtPEth8jhKKoCAvNpGrM00p6V-tYREQpdfQ2Yul3ekAkEKBFMZsyW7tivdBytjtplQV0eV2suzT-NiqRAp-3TlOW2Jm3rNEwD9awXMv_8Ix_p3rwahhVRmO1In_wCFKkiMKCgu3A9-cgJKYGQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ppDSHYQuR-Ft8OkaAE4xWui64ML_wR_F-P20SHJplMsI_-0IAfkMRZ0wElMJmmdP-HDBnxC9xFIOWUhPmHQs613yQg8KBnhRbh9qbDjyhJoa5gJqwFi8IBjxz9wY5Rqb_-odtDWRsQ1Ik5f2lBPDQjSnuYdz6AC54Hi8gEz-CMoTJZ8fQmX6j4qhl1V23v6wHtJXa4sXC53m0TysfTHWBecqLUPEIyjpbFRrV83zpv8ReXkNsPZH1Mbjv6imCMTQyv-_8qf3h22sWYAgX9TM9v15uPU2r0P3TmXX64R60HhrjK6iLujo_nltS9tsPolR4Tv49b7Rvfg_Gu3jSCSueg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Y6-f8s_nYf0NjW4zg21BK5rUzA6LUbyaXM3-2gbVTmJvgPSNHT0DMal9fndgG8IrE_WH7NHcfbYWDAnGcHcnNFzBHRLVgWWr324rNHCgSnlZlFJMvcXwtaZ-2k_p0qxS-AyEISQQYF73gfVf6BdVuoA2C3xtT6ZBGkAkd6VIMLJwGWi1ZItfEya0qkkxOWVCvS22YjL50cygprpXtUDAiGYOYAwWvwSpkBS9koFEgqqmMG9EFfmg-w41JXqRoaGpXY8rAqNYxzQDjLDbu_Dt2rThVnYyqw7Ey_cKsvkxp_we8m2_rErFPNO2d6q6oIBKfoP0ZfxdjFXKsgDfNv1D3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/J1HdJ2Htv5I22HhjgSLSQ-5MfVhpiZenCR0zuL9ib-Rkhgm8LmjgnLRHJoWomsFpip2OjO1YNOMwapEOE-lkza5BeHuQisnWErodpMpqLVHDOKSUNf0QTKVudgPvrAe7u5ePFB4oS9AUVfhKG2FEOfrPwjx0D_3a2CMQnp-S04bf7P21Bh9L5L6PsXR_p1sAtsoQhc_tUVH8XElxCI7sPEtl1oworg4VnpBV_2dEVXnw1P-Q_10zCSJDuRibwQvEszvQrKtlJqgKwhjHScA_PGxDL0UvjCiQ2CP93_7h5DwI8E_blosSQ_slfHBk6a5jjSRskQJ0peXYviggtofNIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JVEa2hQwLXbm31AspnGUup2MHpds4NneLYrVNcmyRcibNg_g9GDvc1AfYbGZps6VfD44j_sN3M0FM5YJsRDdz4NomTRbx_bQ2zHpazxMB5BZxyE_2QVBYooDFXRxTyIrq26vw9B4JuMRv7aL9FMSC85BMI01M20ZXYsLJy0tDUNRxDSRVp-CdpPFhGy7eB7dUZ5a6whk2K-6YvfqJlR5f0kuDt_gqcHjxWLBbKqfKsHYT7bI4oJVDpUGAs2sSs2I5Oanc3zUwDCK4gomhgA91lqCIVbOgzSG0va3ti_Pi1pGsW3rp8JRwXVRFlhnngxyeTmBUN-XNiz4dKnQ-QLvOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Uy7TLEBXuop_ZFqSzY0KMbuhXQ2I6_5O4VnUAq_bO961YJhbCVnSjY1ZlzRFRWEJ-4RTKHXD0C4oTkniibznh6LofFgTki-NrXpj7QALIVQwWn6aC1WmAnOUrY4bW23dkrn9Fg85dpS4SLXfMoRqD0fmQHfXHtiiYwFUS4OZ07WSlKOHmx0AXLtKiJx8JiGzFvUriRy4jSYzX2DaRZWbSKdDHwKX31k5tHTwF2uN8Mcl2dZUd-6mxUwUiZO2m40yZalEnIUdOkaitaJoGOQU4R2wVskq6kQxd4XYfSOR1S3LpVg5vfKAWaKwyWT05lWQQkpqiPxAqK6Y8dUBzKqzgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UISc-GRQ274iPT2-HbzG_odUafoFDo4BMbblQ6LAOBBqG5dP-DSQMVFLAjKRCwV1QG22L3TPNyRWqWq5o6wbRU4H2c1l419dZetwrxsRDXbAk9-yPOKATS_TEl9AxsJCTiViWCKfr84WreFRIdqs7prfFJ1mZNJ6JIQQYswt_vQ-i3nlpSAUa6kYrWcuxUm89IlZ2c_6cJzh8jhUBOYYljNqI0k83kIfCCYCGWyfPSk8Ej2TLo_2OYRcLDpVvnIDpBCqQvMup8plmuG7Gq-zosOH_emQ8j29ml3UAaUfEWNi8tsEmlUFo4OTcSJS04ZmhbVW_ckGMhDvZ-3pPI0oaQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
برداشت پسته‌ در خراسان شمالی
عکس:
رضا خبازان
@Farsna</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/464071" target="_blank">📅 07:01 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464070">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KcakAyiw3rVsDZVvcVKDqeHc9uF6KbTnJ2kUU0OljcSDbcMkiJPnE40mfeyoeQJwpGYBe4xkJSxvTv5megaUBavQvqykuuuz4ArsgvcKXmebkfbYikXPP7ScO5ptYITuQTKPnQ1uAT6HTh-hVpIiG2m9z56rVaZDJn7TKSH3lbT8w19BnzEPIdZki6nnWpZo65_do4nSY5mj_A-AMPhb4cwB-_91PmsGImwEyY7XtyW30i9_5UYd_rROXqSQx29nCK4cOuqSTbgW5LI36bSqF3VUHc9-I8HdrCQii_rx_GUfUnkFxOxmYsdQdUmqtpWVzBRRQg7npIjJYDebF6TRsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی امواج، پیکر نگهبانان خزر را بازمی‌گردانند
🔹
فوک خزری نگهبان سلامت اکوسیستم خزر بار دیگر دو پیکر بی‌جان خود را به ساحل بابلسر سپرد تا نشان دهد که توازن حیات در این منطقه بیش از هر زمان دیگری در لبۀ پرتگاه قرار دارد.
🔸
با کشف این دو لاشۀ جدید، آمار مرگ‌ومیر…</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/464070" target="_blank">📅 06:37 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464069">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OhhTWfIkDOpsAo-7sNjp5u0CxfzAkznH-FNCXAuyGkkreATVyJhKUSMBCE2XYPd08DJmn80UFKwFsr9l_xGu8OoE9XDWxON8wGPCNOl9ubfTraZ993RHRxX0G50swFj2pR5eN9S581tLfiHJ607611pPULOltH9xlR52lQcHlplgXnCFB2QQLpnJdFVGmv6SFCmJDiJ4iCDN7Vid7RdoSUUyeY_da96nL9954rMTYTXzK3BscF6V7MWj3TL_Fr7y1SF1-C6i_JHwqrbS8R-7_mV_lZhwdVVxfjXhH3wVIjv4Fi5EtTCoI-Y1EVkipVxcozrwUyaCv2leYmiUrbDJpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">واکنش بقائی به اظهارات نخست‌وزیر کانادا در توجیه اظهارات جنگ‌طلبانۀ رئیس‌جمهور آمريکا علیه ایران
🔹
سخنگوی وزارت خارجه: نخست وزیر کانادا به جای محکوم‌کردن تجاوز و جنگ‌افروزی آمریکا در صدد توجیه آن برآمده و تهدید به از بین بردن یک کشور را به‌عنوان «زبان دوران جنگ» معرفی کرده است.
🔹
مارک کارنی باید بداند زمان بی‌رحم‌تر از آن است که اجازه دهد توهم و نفاق برای همیشه ادامه یابد. روزی به آنان که زیر سایۀ قلدری آمریکا ایستادند و گمان کردند با تکرار زبان زورمندان می‌توانند خود را از گزند زور در امان نگه دارند، نشان خواهد داد که چشم بستن بر حقیقت و فروختن عزت‌نفس و کرامت، آدمی را نجات نمی‌دهد؛ فقط او را بی‌سلاح‌تر تحویل زورگو می‌دهد.
🔹
شاید آن روز به ایران امروز نگاه کنند و بفهمند کشوری که روزی برای کوبیدنش با زورگویان هم‌صدا شده بودند، همان کشوری بود که با ایستادن در برابر زور، مشعلی را روشن نگه داشت؛ مشعلی که اگر خاموش شود، دیگر چیزی جز قدرت عریان میان انسان‌ها باقی نمی‌ماند و راهِ متمدنانه و انسانی بشر برای حل اختلاف، زیر پای منطق بی‌رحم زور دفن خواهد شد.
@Farsna</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/464069" target="_blank">📅 06:15 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464068">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iEX-GsT4Z_0nyAbZmjDUNxudIbqL1tZJ4lP1i2CPu9RTSpOryzqT3wGHqeTwuczJvzT2FXJkw7yAKQ14RQsVa4-cv2x-gWH4-gizLVOY_0xIxXtaiPRFRhixYxtPu4XXa8UAOO6BwbHYR0Q9h5863XOVPXeb5UlyExuScTeBOEPpDw1k7OsWos3yq6mW2fhWxtDVO85m7mZLzjIon348wIbWizFd0Ap7s5V9DWvJwyTli5i86HacF-2na_7GJlt3kvEu6nSKvoBao0qeTyKPD69vTB_LhgTKhaa13A_EQj4dxKvJYQVQHrerzExJOQabBy7MMS_r1Q37izvY5kS2SA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نخست‌وزیر اسپانیا: نتانیاهو به قتل‌عام در غزه ادامه می‌دهد
🔹
نخست وزیر اسپانیا طی سخنرانی در مجمع عمومی سازمان ملل متحد، به انتقاد از سکوت و انفعال این سازمان در بحران‌های مختلف جهان پرداخت.
🔹
پدرو سانچز در این‌باره گفت، من برای دفاع از اصول و آرمان‌هایی که الهام‌بخش تأسیس این سازمان بودند، آمده‌ام. اصول و آرمان‌هایی که توسط دولت‌های مختلف حاضر در اینجا نادیده گرفته یا تضعیف می‌شوند.
🔹
او با بیان اینکه بنیامین نتانیاهو، نخست‌وزیر رژیم صهیونیستی به کشتار جمعی و قتل‌عام در نوار غزه ادامه می‌دهد، گفت که من شاهد بوده‌ام قدرت‌های جهانی، جنگ‌های غیرقانونی را آغاز می‌کنند و مرتکب قتل‌عام علیه غیرنظامیان بی‌گناه می‌شوند.
🔹
وی در واکنش به تهدید آمریکا برای تحریم دادگاه لاهه به دلیل صدور بازداشت مقام‌های صهیونیست نیز گفت نهادهایی مانند دیوان کیفری بین‌المللی باید تقویت شوند تا کسانی را که قوانین بین‌المللی را نقض می‌کنند، تحت پیگرد قانونی و مجازات قرار دهند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/464068" target="_blank">📅 06:07 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464067">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">‌بانوان ایرانی بازهم طلایی شدند
🔹
کیمیا زارعی و زینب نوروزی در فینال دونفرۀ سبک‌وزن روئینگ زنان ایران با زمان ۶:۵۳.۹۳ اول شدند و مدال طلا گرفتند.  @Farsna</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/464067" target="_blank">📅 05:41 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464066">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lGhXJoEvXX-INAEE8QbsE7gacmI_tGQ80OsiOhhZeCe85h9pycbc133goCE62J9hgOhAin5Dt0OTIs5EHwzADkSubCemWDzDSUrixuUSDU2M3A_1uzs0J5mXdOr2zWUSjcDFILR5mVrO_qX7lLVqX3VrajtFbzzE6ablcXsO4YaztY-7fdX6ggG1SxUxrLlQU10KPwDLDOe8UjgLhM4y5OVHVpaSZHAxMPk5886VijD1X4sHbE1-_Oc5Zy9CNkCobKfNxHQ0srcrWf5iams8WqweGBa7EG4HcJEbroBxfbsyx_J4Kmjl1jyzSbrXxkKZlZLSyYIbdix-okjJ8U7e8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
دیدار پزشکیان با رئیس‌جمهور سوئیس در حاشیۀ نشست سازمان ملل  @Farsna</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/464066" target="_blank">📅 05:21 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464064">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nPKpRVttooIVJ0qbwfSLR4YU6LYROATLqVfQPCBO7aEfaV093VMWd-rHJWvN7-AOJSkjZtwz7VdyuhfuytjbhVWKDMx0O4h6V0BhBigiCW2TeaF4NPdPOgSVJp3uwqQufizBJl1yELwdpWm3y9Iae9JhHIHn_mulGRlQtAgkc0ohLtvNCYLEaBY7HMq4Q6reWviu5JQeIGOCwmzZrP3-UsQHCu8Lx9KFI6ybSpiFXsxLx8xO41ZMdTShB3wPdLnn-sY6b4wZqXLZYKjy1p8vMsWmdj1z5OeRSp7aZKzXmJdKy2MoFSr4C7VA5dchjB8QQjSkGWOzgbxICm1v2kzPBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هت‌تریک نقرۀ ووشو
🔹
عرفان محرمی در وزن منفی ۷۰ کیلوگرم ساندا سومین مدال نقرۀ تیم ووشوی ایران را کسب کرد. @Farsna</div>
<div class="tg-footer">👁️ 9.95K · <a href="https://t.me/farsna/464064" target="_blank">📅 05:14 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464063">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hWTr2EzTU7sIIDcN1-8ZLz25UZsZa5O1tF4Wm_oSZ56f-7ymXLs-LHPWbJWLPxuZWR5ZDx4t_6P-SErVsWZRmSKzkRkpyt3Oc_Gg-RDEafSPTdJh8NUW15o-Z8u2awI3J141KTQL9Pui1_fmafCxq4OUwGzuK9SQH2jvzcWWG730RzBtFJcyth2FwPvYaguZ02AszFHj2IWrVstonudf2T8WG21SBuM7zIiQIAnM3m1hK5lbigAjnXrTHEqF1SSqLohypBZKlgmq4hiZOWD7lCUtPMuVF-d0QcJkvaNgcheIfnAdn13gf8m6FvFqC9O5buJ7Wg_GVc8dtSGbYSdEgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دومین مدال ووشو هم نقره شد
🔹
شجاع پناهی در وزن منهای ۶۵ کیلوگرم مردان مدال نقره کسب کرد. @Farsna</div>
<div class="tg-footer">👁️ 9.55K · <a href="https://t.me/farsna/464063" target="_blank">📅 05:05 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464062">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ffd249604.mp4?token=HRABiKoKW1fgjjSm2zag3xEbyC6lnZpg0Vfkzg-p4vFN4lk9klB0VinKwDDw_cPwfcxJ4IH8NcRrbk58OjPrDNoNjDmKPKf1MbVfGjsn5EAVaEFNIudG5_uoxxR5xx-am3JWcn7w_j6ghq4ipn71R2f7PVMkBF1LvzTOlXWUNG8gE1jhoX3a-duAsh8Rk_OKypkCgHTGGsIlTrA3qXOJCF0plEY89AjrLxY8m8tZtusyIJ90MKIXlw2e2GCOlPZ-P7yDrA3EQxKmA5VXY65xN2olx0APO4lSbzD7F1i6MRKWxR_un21EvhHsuLQFMxLQG44ezchyO3cdW2iTz87WxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ffd249604.mp4?token=HRABiKoKW1fgjjSm2zag3xEbyC6lnZpg0Vfkzg-p4vFN4lk9klB0VinKwDDw_cPwfcxJ4IH8NcRrbk58OjPrDNoNjDmKPKf1MbVfGjsn5EAVaEFNIudG5_uoxxR5xx-am3JWcn7w_j6ghq4ipn71R2f7PVMkBF1LvzTOlXWUNG8gE1jhoX3a-duAsh8Rk_OKypkCgHTGGsIlTrA3qXOJCF0plEY89AjrLxY8m8tZtusyIJ90MKIXlw2e2GCOlPZ-P7yDrA3EQxKmA5VXY65xN2olx0APO4lSbzD7F1i6MRKWxR_un21EvhHsuLQFMxLQG44ezchyO3cdW2iTz87WxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فاطمه مجلل: مدالم را به دختران ایرانی تقدیم می‌کنم
🎙
خیلی خوشحالم که توانستم پرچم کشورم‌‌ را بالا ببرم خوش‌رنگ‌ترین رنگ مدال را گرفتم و از این بابت خیلی خوشحالم.
🎙
مدالم را به دختران ایرانی تقدیم می‌کنم. امیدوارم تمام دختران ایران در همۀ زمینه‌ها موفق باشند.
@Sportfars</div>
<div class="tg-footer">👁️ 9.6K · <a href="https://t.me/farsna/464062" target="_blank">📅 05:01 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464061">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bztDUrEtCrYOZAZHBuVaAEHSKZx6BC5jaqcauU97VH0nudVvRnd7aRq4U-ZPG-n7ifKsVsErnifGL9qneM_qu5qOXXmeeNf0mqlItfIa5GaWPD7bJHEBvexkyj_acXv914AO_Qdm5XAGiTPuRHWoX89Q7FiodHEtBvSYz0mJNwVMA8NuvBm7f8k3dxt05KfiHpMTxLXY_13JaxqKMtr-NNnXvqBvP8gV60W_8vKEqiyS9lRd_pR26oW5RtmdTb3YXAH4fi3hK_-Cy5HmPMCvGAloUsZS5YFohRSaH9_GENwUV0m6xiHM7NYwxUR56rTck6JNeMPb872879Hs_SymFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بانوی ووشو کار ایرانی نقره‌ای شد
🔹
در مبارزۀ فینال وزن منهای ۵۲ کیلوگرم ووشوی بانوان، سوگند سینکایی به مدال نقره دست یافت.  @Farsna - Link</div>
<div class="tg-footer">👁️ 9.63K · <a href="https://t.me/farsna/464061" target="_blank">📅 04:59 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464060">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/311f23114b.mp4?token=TggbOJkATxwfJxSVDGX8NJNibKBZgDPZ2y7D1XnHFbyHHrvG0ckQmuD2u88RbNcEy69XNKvo9cOOM_bblp8p4tdKuPKHEwRedmHN5tozTYQ6UxBK2OFtAeVSqxx0Hmzf6FZVunOHEjM5NkruTmgtPPfGyr2GIGWbSN45RsUoprWBgpODZnuc8IpnqZ6BuGoJk91MFioR5EumH3LyVurSWeLjRthbzW1MxFEYeLHOManpx0GCjrx4n1ZJu3Z7eUWTwSSV1Z_zmtllPIgyYVOHSDI2pAB4HxQcs-3NNMoSAfSK4r_z-JoSCM65BRqpiZ32FqjtLP6CBPxhPe5s4DJgjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/311f23114b.mp4?token=TggbOJkATxwfJxSVDGX8NJNibKBZgDPZ2y7D1XnHFbyHHrvG0ckQmuD2u88RbNcEy69XNKvo9cOOM_bblp8p4tdKuPKHEwRedmHN5tozTYQ6UxBK2OFtAeVSqxx0Hmzf6FZVunOHEjM5NkruTmgtPPfGyr2GIGWbSN45RsUoprWBgpODZnuc8IpnqZ6BuGoJk91MFioR5EumH3LyVurSWeLjRthbzW1MxFEYeLHOManpx0GCjrx4n1ZJu3Z7eUWTwSSV1Z_zmtllPIgyYVOHSDI2pAB4HxQcs-3NNMoSAfSK4r_z-JoSCM65BRqpiZ32FqjtLP6CBPxhPe5s4DJgjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اعتراض فرماندار کالیفرنیا به یاوه‌گویی‌های ترامپ دربارۀ ایران
🔹
فرماندار کالیفرنیا به یاوه‌گویی‌های رئیس‌جمهور تروریست آمریکا دربارۀ ایران در مجمع عمومی سازمان ملل متحد اعتراض کرد.
🔹
گوین نیوسام در همایشی در حاشیۀ اجلاس مجمع عمومی خطاب به مردم آمریکا گفت [ترامپ] تقریباً خواستار نسل‌کشی ۹۳ میلیون نفر (کل جمعیت ایران) شد.
🔹
وی با کنایه به مشکل روانی ترامپ، گفت این‌گونه اظهارات عادی نیست! هیچ‌چیز عادی در آن وجود ندارد!
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/464060" target="_blank">📅 04:40 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464059">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dfoPaEdvgQKXUdb8RKCEs7sVUpw0NF7pa2_85mCwQGMCJP5NERDe8W6nL0RdZea6BRnqVIkxqp6wAdyzgvqthUGlm7vyCbA1Cr7niY3sDNgk7XEOn_97Pa5gVCodLGkNmrdTqFL8AKSVBDHJ80NjYDkhS9j3bjkPNmQo1RFyr1v-tA4T8QRklfxUvP6Ei_dSY5Vwzwv3A_J1gJE9mHCIjGZTl5WgaNdfVY9bj3-ADvV3nOlwMz7Hdx9rDeLjwBltsxXwv8w0GNML5kBXFSPqWEOR3KjBdDnr7j6ff8OkuacmNIVRf9elkPFjmqFhqX2SxGkE0nSSF0iQQEsR7pQD8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بانوی روئینگ‌سوار، چهارمین طلای ایران را صید کرد
🔹
فاطمه مجلل در فینال تک‌نفرۀ سبک‌وزن زنان با ثبت زمان ۷:۲۴.۵۷ به مدال طلا دست یافت.
🔹
این اولین مدال روئینگ و چهارمین طلای کاروان ایران است. @Farsna - Link</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/farsna/464059" target="_blank">📅 04:32 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464058">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">حملات هوایی پاکستان به ۳ استان افغانستان
🔹
به گزارش منابع محلی،‌ پاکستان حملاتی را به ۳ استان شرقی افغانستان انجام داده است.
🔹
همچنین گفته می‌شود قندهار به‌عنوان دومین شهر بزرگ افغانستان، هدف حملات هوایی جنگنده‌های پاکستانی قرار گرفته است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.79K · <a href="https://t.me/farsna/464058" target="_blank">📅 04:25 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464057">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qNQk08lTMaaq5DGfrJ4DcJUS29I-CWgpsVI0jaVf6h3TXgxdphzQDaY8MtgUGYBRyb0ZoGWHvJ7LefT9XQ8m5APNvGIIhawbLyWGEi7HHpxqhtJz5OLmyq-nH0PlBVE5WZmS4-aHmUuzvxym6rMFczu2j3TH_b1Lg0rZbDUiXiW6ypAU6o1GF6WfRlb41_WzBWgvXb5c7rOYXJwiJJookD6PnqtJl6gvP8ojiZ8zdTr9002sIy-hB1f5PF3j5eMKtzlVQL5eAsLFttNtvVzdsetqKh2Eem2DIvEFyTYGoufCreSQNL6LPE-6bn-GF6ciO57np7I5xnS85rrIiwGQmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بانوی ووشو کار ایرانی نقره‌ای شد
🔹
در مبارزۀ فینال وزن منهای ۵۲ کیلوگرم ووشوی بانوان، سوگند سینکایی به مدال نقره دست یافت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/464057" target="_blank">📅 04:17 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464056">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bAp2hYf0-ZUIC0UKyTik2DW9olbs5t53fRWUG0e7TRjddeQYRsFpz2chdxVYNyVqUVzR7CVw92uChahgvUpU31b_6S9G7Eqe8U8dmfTst9LMEfkR0CH3GS2_a-unLarh4VfDQfSyecDClOyTEc3lXJAQGo-BsKiLxJAmfJPqfVyNfwQW6nnQ69fijTQY0aN2kWIFPoUyc8DDukCh41m7HE7T7BrWEpHNuHi2U0G4jkCtxPb__MmBHbN3ucOjoqLBqKTrrNSReybBcP_GqguDVBzZvtAbOPegjFAdsa8A1x5X6SGwp7EPhfOLlxz0oRwannfyqZv78TuCnAAgPCglhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پزشکیان در دیدار با رئیس شورای اروپا: دخالت دولت‌های غربی امنیت دنیا را تحت تأثیر قرار داد
🔹
دخالت دولت‌های غربی باعث شد امنیت کل دنیا تحت تأثیر قرار بگیرد. اگر کسی دنبال علت اتفاقات اخیر است باید به رفتارهای دولت‌های غربی دقت کند.
🔹
انتظار داریم کشورهای اروپایی در رفتارهای خود تجدیدنظر کنند و استقلال خود را حفظ کنند. ما در جنگ اخیر از برخی کشورها بی‌عملی دیدیدم ولی بی‌طرفی ندیدیم.
🔹
اقدامات اروپایی‌ها در اسنپ‌بک و برجام، و قرارگرفتن زیر سایۀ اقدامات خصمانۀ آمریکا باعث شد از چرخۀ تاثیرگذاری در تحولات بین‌المللی خارج شوند.
@Farsna</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/464056" target="_blank">📅 04:15 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464055">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ebd1704d80.mp4?token=ObOiUxffWyDjR_VONPqoyhe93UEyn6NANkrPHznJ9zqd5me2cSxVZYlPf5WDc5QqDsGHzwUthGBpJFx-427gkevd8abASxzzmAgPKbi8_Qf4HzXLpDpt7-Gd9uptrP0U7cXHUqXN6MpYftTd3LnosVIkCrlpZCKrzY_y0Sq9SSGg-6A8pyJV6w08V89XSyDiz8_fQudNnNa3wCFsHr6R8npBccvA-n6qUx6p6dt21JQba3HRDdAXbKBqWcxYLyYmkeRqX6OuAeTSjjhVTZsWvgoisCoYGM4hrQuCsJnrantVRum_4pHlR4XGroIuYJB4ngtjjTat8IUevzabk0KYWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ebd1704d80.mp4?token=ObOiUxffWyDjR_VONPqoyhe93UEyn6NANkrPHznJ9zqd5me2cSxVZYlPf5WDc5QqDsGHzwUthGBpJFx-427gkevd8abASxzzmAgPKbi8_Qf4HzXLpDpt7-Gd9uptrP0U7cXHUqXN6MpYftTd3LnosVIkCrlpZCKrzY_y0Sq9SSGg-6A8pyJV6w08V89XSyDiz8_fQudNnNa3wCFsHr6R8npBccvA-n6qUx6p6dt21JQba3HRDdAXbKBqWcxYLyYmkeRqX6OuAeTSjjhVTZsWvgoisCoYGM4hrQuCsJnrantVRum_4pHlR4XGroIuYJB4ngtjjTat8IUevzabk0KYWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دیدار پزشکیان با نخست‌وزیر ارمنستان در حاشیۀ اجلاس مجمع عمومی سازمان ملل
🔹
پزشکیان در این نشست گفت: سیاست قطعی جمهوری اسلامی گسترش همکاری‌ها با کشورهای منطقه و همسایه است، و در این خصوص دولت همۀ تلاش خود را برای اجرای توافقات به‌کار می‌گیرد.
@Farsna</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/farsna/464055" target="_blank">📅 04:06 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464054">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GreMoxUcQKOaOUM8fCWS0A1ssieISeC9yCVP-dXpLL9HJ0LrJbQw_9L9-gx2JV29GZokfaLIPGU_ePT4b-V4oHw7PMgIrk40XMMzUo1nhQEqKMsdad7BLsDEvOckEn4f14p1WswifquFH7a1SjAaVa-9hXjk10_4_LKW6J2Z4CF5iHqmalSpLxA6mvq4DENNP1IPxKH5_PTsi8JMyVoKp0HbUgZyecwFfbkcxx_DsTJ7aPWxrnsRaGOuU60by35TaRH30VGxDoGNeQj5Xa9MC23mkITB1MgE-0i_0YtsM1wjztsLPhSJC1-DCGPoNEFOsSPUEWT7LLMoPExC-EnuQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بانوی روئینگ‌سوار، چهارمین طلای ایران را صید کرد
🔹
فاطمه مجلل در فینال تک‌نفرۀ سبک‌وزن زنان با ثبت زمان ۷:۲۴.۵۷ به مدال طلا دست یافت.
🔹
این اولین مدال روئینگ و چهارمین طلای کاروان ایران است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/464054" target="_blank">📅 04:01 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464053">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">انفجار در مقر گروهک‌های تجزیه‌طلب در اربیل عراق
🔹
رسانه‌های عراقی گزارش دادند که مقر گروهک‌های تروریستی تجزیه‌طلب ضد ایرانی در شهرستان «سوران» در مرکز منطقۀ کردستان عراق هدف قرار گرفته شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/464053" target="_blank">📅 03:46 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464052">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس معارف</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c61e7ff434.mp4?token=QgqKySbyNrIIUNjpSiAvjTNKjY8IWIKYLFtoMc10c7IPR601ZNPWzOxnjb7mqYTTW3LWRM-yTRBO8iokszLq6XtHa8Ve_uurvTAr63J89W_HuMwkyf1JUV2yKgLNja0wsUbiJ5BgVxoZlI8UMA9EDb-6qDdf24BzGB3OBn_NBbd7IrytOP4GnKbeANRzOCqxXKcXzF5VNlhRpk_WzQggx-_32sIlWsVczp-70coGn1_tizyHu9hnvBDwCvIlC000G9JYS38DfGTePz9RrMCju7y5PR9vax-NcD0JU7CUobS4gxJJnsxoTW9Y3xcf3aQDTYOkOeOegHjDldN_0Rfrgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c61e7ff434.mp4?token=QgqKySbyNrIIUNjpSiAvjTNKjY8IWIKYLFtoMc10c7IPR601ZNPWzOxnjb7mqYTTW3LWRM-yTRBO8iokszLq6XtHa8Ve_uurvTAr63J89W_HuMwkyf1JUV2yKgLNja0wsUbiJ5BgVxoZlI8UMA9EDb-6qDdf24BzGB3OBn_NBbd7IrytOP4GnKbeANRzOCqxXKcXzF5VNlhRpk_WzQggx-_32sIlWsVczp-70coGn1_tizyHu9hnvBDwCvIlC000G9JYS38DfGTePz9RrMCju7y5PR9vax-NcD0JU7CUobS4gxJJnsxoTW9Y3xcf3aQDTYOkOeOegHjDldN_0Rfrgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خدای ترسناک
🎙
حجت‌الاسلام رمضانی
@FarsMaaref
💠</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/464052" target="_blank">📅 02:58 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464051">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZGglC3xoF8SKp5e_H-TKqYWLMhXrQbQWWSaiVgsbX2q2x6WINzcPsF6CnwyVpp32z2qNc-ckyEVXNxk3imO4PHxcMyP94IjwTShpruPC3oPDJTm4IjPPh_AOouEX25ynBeGa5SiKKeQz7Ygzo0xbcGickFexxGavrQdG5LUlf2I1aCKZ1DtdY-N7Bo81IsrpgwiQGQl0dxXQrWJG8_b8V_WMrzC7fKnzuDqljjg-nVs8E8x8Vdjiaxw7kyn8Aj7Qh7n9CPYjwPVykiEfe917vAhkAWiQ23z4eHvzCVi5Ls5BkSOBEJ7cAlKhiQ55BiOPm3N-BIAR3ox1Ghx94zxKEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تأمین‌اجتماعی: بازنشستگان نگران پیامک اشتباهی واریز حقوق نباشند
🔹
سازمان تأمین‌اجتماعی: پیامک اشتباه واریز حقوق شهریور برخی بازنشستگان و مستمری‌بگیران، ناشی از اختلال در شبکه بانکی بوده و حقوق کامل افراد امروز به‌صورت خودکار اصلاح و واریز می‌شود.
🔹
برخی بازنشستگان…</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/464051" target="_blank">📅 02:38 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464050">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/464050" target="_blank">📅 02:20 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464049">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">صدای انفجارهایی در کی‌یف پایتخت اوکراین شنیده شد.
@Farsna</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/464049" target="_blank">📅 02:06 · 02 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
