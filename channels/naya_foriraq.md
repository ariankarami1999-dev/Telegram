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
<img src="https://cdn4.telesco.pe/file/t39hrraEYRoNkc6VkKUwTQXS4VxA544xA_qd241Odc-9cxonTwCjHsJG9775harmsOHjYPkt28HRI5MDgdd6vFlA9oYLKhre0Bjsof5FAl5YJod8JJo5__MBNXdoevXXvIlprIcUKkisqmE5fog7UadyO94Jz4bD3bNheqAYBNa0FSeUimR2xbGXfBfn1TSAVRSgnSW9pG0Zkcx6JtR1B9WTXgVrR8as0TkagJxBkd0i7dAC_WCm8eoDktBAjok7SZriJu7RIRPXr18ohDJZoiqymR3Jk6BbYEYiUZXtx7KMry3fvIvd99xU3Nf08ihbFBDhLllrszxf8JYgvGD3qw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 268K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-22 16:28:12</div>
<hr>

<div class="tg-post" id="msg-90373">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UjIxnL0IUHgUWp7k8-bGeqS9IJhVvKRFIEhMkRuEXiqKQhj_CjYhNmi3eH-yiDuuW--W2gm3NiJ72dCzOVHY4F_N0e4QjlVUINuDSyBmGfwOaDxkwiqD7tIBlpjMFNTdHojr6px169bUoNLenBGZxiC85_CQZ42kZzkNnaUHZoqR-BVUzoTu4z_WQqtJ2PAEB7o-wB7TEjNciXWG9Fp6EY3b2cap-yhQhj4Vz6F9Sdsg2wVA0ei-Rz9wb0fsLPd5yImvKkzu69rwaRT9CJkkfZH3hXpvx6ireqHjWb5qxF-BAAIa6aMRrwdgEmmwYKNeWKnC8SYRZTVc3UG9LzGpTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترفيهي
تربية واسط تصرف مبالغ عن طريق الخطأ وتطالب باعادة المبالغ</div>
<div class="tg-footer">👁️ 1 · <a href="https://t.me/naya_foriraq/90373" target="_blank">📅 16:28 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90372">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iDhmGVievPHYX-40iUMsGCk4vj7_cthgFA17A-aAc5-0ELUJimfogOCYlPXQLeNf_YdL-e2GdazcECzB8eBXBxDgoIX_cwlpPdP8jKGandjNakkyYlc6mW2pwQDN8E1h_DsJYJ3CZrVjGUx09gF-EyZP73xujfn85LlflhByqbzE1eRAzmynC3DgWW1fjS7z9g898-nW2vT97fO5JI88qZaUw-_gE-9vpCD3ZYbvGPnGvJvyMzSvJ05SIh5fOGQNuiTrX5DAeVL8ajGGDC1o3CDXxzZnwD-UbALI5CjYCMz0pNH3WUchtp2uhTAB6QJHFONXzPaelAbn4z3Z3G8oSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مجبوس الدياي ويانه غير …
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 1.42K · <a href="https://t.me/naya_foriraq/90372" target="_blank">📅 16:23 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90371">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🇮🇷
الرئيس الايراني مسعود بزشكيان:
أجرينا حوارًا جيدًا مع ولي عهد أبوظبي، واتفقنا على تجاوز الماضي وبناء مستقبل أفضل.</div>
<div class="tg-footer">👁️ 3.75K · <a href="https://t.me/naya_foriraq/90371" target="_blank">📅 16:07 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90370">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">الاعلام الامريكي:
وقف خط أنابيب في المملكة العربية السعودية يهدد خسارة بنسبة 4% من توريدات النفط العالمية ما لم تبدأ الاستخراج مرة أخرى في الأيام القادمة</div>
<div class="tg-footer">👁️ 5.65K · <a href="https://t.me/naya_foriraq/90370" target="_blank">📅 15:50 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90369">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a08f0e1a58.mp4?token=qwN56tNdT3jFqLSNLycj0q5U-TBHMfzWRfErkAN1k7WAIRIPlsYIRsPdpZMI8PcgAWoVFEoZiq7gJ4Adg5eUdsRP22K_dYjo-w8ICmxOKO-tJeEY2VdZzUshEOUyq_4vzq44d51euQjlC56Q9IJ9bMWz-HmxZFKoWbtIzi97AE1zcLr3ZdMTOy46vrF_t9-NR8DaAddcIcF4kT_xztiM55ZoC6dtdbGBxyLzvAYyLGZwRodl5OJXv9XFwSHHZR9ptskzPWseM3TecOm9J9Og2h8gSWa3MWqH3jeB6_BwYlIMSkRISIDF3ZT7CQZw1061C9Dp-AvLMD9N6HGevBZl7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a08f0e1a58.mp4?token=qwN56tNdT3jFqLSNLycj0q5U-TBHMfzWRfErkAN1k7WAIRIPlsYIRsPdpZMI8PcgAWoVFEoZiq7gJ4Adg5eUdsRP22K_dYjo-w8ICmxOKO-tJeEY2VdZzUshEOUyq_4vzq44d51euQjlC56Q9IJ9bMWz-HmxZFKoWbtIzi97AE1zcLr3ZdMTOy46vrF_t9-NR8DaAddcIcF4kT_xztiM55ZoC6dtdbGBxyLzvAYyLGZwRodl5OJXv9XFwSHHZR9ptskzPWseM3TecOm9J9Og2h8gSWa3MWqH3jeB6_BwYlIMSkRISIDF3ZT7CQZw1061C9Dp-AvLMD9N6HGevBZl7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رئيس الوزراء الباكستاني لمحمد بن سلمان: نؤكد دعم باكستان الكامل لأمن السعودية.
باكستان وتركيا:</div>
<div class="tg-footer">👁️ 6.24K · <a href="https://t.me/naya_foriraq/90369" target="_blank">📅 15:47 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90368">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/27850023e2.mp4?token=rOyc1vOjLv47gaPJ9KOen3q2pKe5qyPcFd9thK81rKeY-fFAQnLDyHWNEOjQB3Dm6UK9iLBc6X6MDr0hRZUcM9U7Z05p2LPu4fbBjAfeEIReMLk5zxt8GOJ5ntrxZAyOYwXCkbS6qMVNLpbaczvsbUVjjbaIdu5MEgvc7X5_6bSb9-W0uMWbytQSui36dVZo7NsHHqtn2_pBEVQT0Dq98mBFJF8FQ7bRmIRZXvTvHsG0LGDlR5N-sRwNua0W30HGl4nu1Dawg8m6OfmL1w-CbfdVUP7IrdATLOTj9t1JY9HYw0MfiWZXdj8T4-rkpcAVOOQ4THG95AW2XPGCdprK9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/27850023e2.mp4?token=rOyc1vOjLv47gaPJ9KOen3q2pKe5qyPcFd9thK81rKeY-fFAQnLDyHWNEOjQB3Dm6UK9iLBc6X6MDr0hRZUcM9U7Z05p2LPu4fbBjAfeEIReMLk5zxt8GOJ5ntrxZAyOYwXCkbS6qMVNLpbaczvsbUVjjbaIdu5MEgvc7X5_6bSb9-W0uMWbytQSui36dVZo7NsHHqtn2_pBEVQT0Dq98mBFJF8FQ7bRmIRZXvTvHsG0LGDlR5N-sRwNua0W30HGl4nu1Dawg8m6OfmL1w-CbfdVUP7IrdATLOTj9t1JY9HYw0MfiWZXdj8T4-rkpcAVOOQ4THG95AW2XPGCdprK9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
🇮🇷
عدوان أمريكي يطال سفينة تجارية إيرانية بالقرب من جزيرة  قشم جنوبي إيران؛ إستشهاد مواطن وإصابة 3 أخرين كحصيلة أولية.</div>
<div class="tg-footer">👁️ 6.9K · <a href="https://t.me/naya_foriraq/90368" target="_blank">📅 15:40 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90367">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BIwtuaLnh4lZPDlF5QyhqcfHWhQvL7TVhH0Yyx7eo6iVAKES-_KveUhAGvx7sU0Ntjj1C4ujLrDSnN1szqBl4sKEOwVWH7TCVM3vwiO0Ifm4Q5Zzh3lm_WswXsmqdtQIQUmuSs7pEUu9FbbU81SJo5qglo7-dcmjecouzRhxR4qfb2RE3Ts0x0MHBdF6XjvFPNaQfHfijviHDKPDQCIAoSAB467oXWroW0xYkE16CKfpjpeckTm02p25XpJMQkMco5zDoSDo--I-UFUpHi1K6sry7GalKv7SrjHoP9659bN42Wq2KcCT4DX8byADic-E19XRH380ujASHfDDhEyrPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇱
قصف إسرائيلي يستهدف محيط بلدة بيت جن جنوب غربي ريف دمشق.</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/naya_foriraq/90367" target="_blank">📅 14:12 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90366">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Me4mVI-dLNCcbR9rfkxV6PYSk1rBmbCh32857g2rnbKWc7gwY3lZgF87_6aoGCY6d7jm0W8OLI4_KNOobvE4IHLyIr7oM2puN7Iin6evUSPNNu8HX2jvS17z6M7l8jY-z2Gv_3Uz9_ojfkpql-Hbv29CdG0OIC08vhK4IKKKLM3BCqhzdaCptIcT-wEYB6p_Ke0GRHXuVOWgwVt_X17boTgcgIeYJmIngOJBV3UyVGjNm6xFs-gb9Y-A80s_uhwmfgcfpTEL65WbRS3sj8Wmvunbfbh6npTLw5kcebDd1ITeQZsEMwRlytsGcyhrh0xDnAWY7E7mGH2n9Ye2VLRK0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انفجارات تهز ينبع السعودية واعمدة الدخان تتصاعد</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/naya_foriraq/90366" target="_blank">📅 13:58 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90365">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🇹🇷
🇮🇶
عدوان تركي يطال مقتربات قرية گلاله في محافظة السليمانية شمالي العراق.</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/naya_foriraq/90365" target="_blank">📅 12:36 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90363">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aH1RiuCy_cOFZOkATaufHhdidQcYP3_nqa5A8jUvf22-oWaYHQf_4VM9qnx1ssXEF14tXS3r9-0gthHGO2g-kJQ9t1JNs35GGY3-FTJrFGzJqMpqe27MSQhsX-eDEyJcM5oUnt_MVH0F-thq-Qce9jL8QmVVqTxabNUjQGLIfX4IXlUo_7zqSZty2y6fMdjAFoOnTycnL7jl5jMFz02ro3XLZk4TWtLSBjOKHNbA2b1T79pLO0CAZ1oBbvqMdTmFiwLeKbO-7UCGCG4RHpJ4A2SUxBnlmLaHRxrgoTrjQempU1wfgWMcOFEIooJSdXzCYUWss0ykMUnNwpdKUtqt2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الكبسة معنا غير
😆
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/naya_foriraq/90363" target="_blank">📅 09:35 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90362">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8041f170b.mp4?token=gHw03ZpOYoRFdszqhA2cBG8ssKhoBTBcGdGyCVQkyiz4yPKPU3-Gv7Ph5mpcK4YOUW50N6cBAbdlVUbs8snOTBAqB8jfkMfJokG70mOy7HO3nrpiJ3lze0H2rgSMbK1o_H-J60D_hTKhNVBGef9wEKLoe2U5H6FaNKCeifGj0iPNL3w3mSwVB7lP5PorAybxi8_gYfe83m0annzb114nvqAiI7YAMz8WEcYt-VkNMrT1ls9BrITuBNfAFtOnl3IqxjxP9Mbp0mfRX0LPZkZoPSerEs5No8OcmNj4xzsMLtIlFnrGlGNDP3fmcCEcwR22f7W_04Q_uK85OYxwaiiEcC5VRZxcrq0tmiKF-cGe_ktFTziAJZe17zQW-mRpEWCzaL19pqfMW1OWJ66TxqPix6109yZvpbCJkwNvvluGvpSJh1zesdbIxeklB8weohVas-zpOcEK4kBzJzVZzGVhWtkyAs9z7eZCpDuFd_dmCzhxQhZzLX604RVRbqKOK8NfWd037Ya4z-QxGCnCKHNjrPxw5g2kPFrggMf9e2x-SUwH4xv-IIuCyQXK_sEtcTalSdCA2aEBqnxUPzqSe5qiH5ls6PjzmkLr6VcLSa1v3HZpjI6TVlUfwpnGvVjunDsdVUn83qWY1M0Z0vohKOPqqKbvc0u_OJ-b30SHhNmdME4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8041f170b.mp4?token=gHw03ZpOYoRFdszqhA2cBG8ssKhoBTBcGdGyCVQkyiz4yPKPU3-Gv7Ph5mpcK4YOUW50N6cBAbdlVUbs8snOTBAqB8jfkMfJokG70mOy7HO3nrpiJ3lze0H2rgSMbK1o_H-J60D_hTKhNVBGef9wEKLoe2U5H6FaNKCeifGj0iPNL3w3mSwVB7lP5PorAybxi8_gYfe83m0annzb114nvqAiI7YAMz8WEcYt-VkNMrT1ls9BrITuBNfAFtOnl3IqxjxP9Mbp0mfRX0LPZkZoPSerEs5No8OcmNj4xzsMLtIlFnrGlGNDP3fmcCEcwR22f7W_04Q_uK85OYxwaiiEcC5VRZxcrq0tmiKF-cGe_ktFTziAJZe17zQW-mRpEWCzaL19pqfMW1OWJ66TxqPix6109yZvpbCJkwNvvluGvpSJh1zesdbIxeklB8weohVas-zpOcEK4kBzJzVZzGVhWtkyAs9z7eZCpDuFd_dmCzhxQhZzLX604RVRbqKOK8NfWd037Ya4z-QxGCnCKHNjrPxw5g2kPFrggMf9e2x-SUwH4xv-IIuCyQXK_sEtcTalSdCA2aEBqnxUPzqSe5qiH5ls6PjzmkLr6VcLSa1v3HZpjI6TVlUfwpnGvVjunDsdVUn83qWY1M0Z0vohKOPqqKbvc0u_OJ-b30SHhNmdME4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
بحرية الحرس الثوري:  ادعى ترامب، في حملته الإعلامية، أن مضيق هرمز تحت سيطرة أمريكا؛ إذا كان الأمر كذلك، تقدموا وأرسلوا إحدى سفنكم إلى مسافة 100 كيلومتر.  الأمريكيون يعلمون أنه إذا اقتربت سفنهم، فسوف يواجهون ردًا من القوات الإيرانية، وقد حدث ذلك في الأيام…</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/naya_foriraq/90362" target="_blank">📅 09:04 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90361">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🇮🇶
الإعلام الأمني العراقي:
​1- استئناف دخول المسافرين من منافذي (الشيب والشلامجة) اعتباراً من فجر يوم الأحد 2026/9/13 الساعة السادسة صباحاً. ​2- استئناف التجارة في منفذ الشلامجة اعتباراً من يوم الاثنين المصادف 2026/9/14 الساعة السادسة صباحاً. ​3- استئناف التجارة في منفذ مندلي اعتباراً من يوم الثلاثاء المصادف 2026/9/15 الساعة السادسة صباحاً. ​4- استئناف التجارة في منفذ الشيب الحدودي يوم الخميس المصادف 2026/9/17 الساعة السادسة صباحاً. ​كما نؤكد أن حركة العبور والتجارة مع الجانب الإيراني لم تتوقف، ومستمرة بالعمل على مدار 24 ساعة في منفذي زرباطية والمنذرية.</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/naya_foriraq/90361" target="_blank">📅 08:13 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90360">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🇺🇸
🇮🇷
عدوان أمريكي يطال سفينة تجارية إيرانية بالقرب من جزيرة  قشم جنوبي إيران؛ إستشهاد مواطن وإصابة 3 أخرين كحصيلة أولية.</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/naya_foriraq/90360" target="_blank">📅 08:09 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90359">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🔻
بحرية الحرس الثوري:
ادعى ترامب، في حملته الإعلامية، أن مضيق هرمز تحت سيطرة أمريكا؛ إذا كان الأمر كذلك، تقدموا وأرسلوا إحدى سفنكم إلى مسافة 100 كيلومتر.
الأمريكيون يعلمون أنه إذا اقتربت سفنهم، فسوف يواجهون ردًا من القوات الإيرانية، وقد حدث ذلك في الأيام الأخيرة.</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/naya_foriraq/90359" target="_blank">📅 07:29 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90358">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🇾🇪
إسقاط مسيرة معادية في سماء محافظة الجوف اليمنية.</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/naya_foriraq/90358" target="_blank">📅 04:33 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90357">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/feda8091af.mp4?token=lIcM01BHDm5345rPj-tO26euv7RzaFetmSkoUJOCmrdVPfVqkl1MZ8fcVOdBT1HiSG_5ZVQhlCeo4F--zpFsvNjIFzpkFNsK7rcxRT8TvgKkPzGg9M-CiL4hbXyba87xL9NAavOrQIO7S_vtfR7owiVWZxnTlxf2noYRPcsVDn1nKfKJKALJWViu9lBPBithEGt-ZzpHERC0-MqMvPHAIQBEq2jdCt7giwLhNuCeQlIh_OEZN8t-4nJe6OF1E1AJF49mkWmV7Oz3YNl86L6IxnINeIvmBL36KHkQUJERcwrRaATiXRQT4RuTRCbJ3revsdEuRP3_B6AuDW4ePjlMTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/feda8091af.mp4?token=lIcM01BHDm5345rPj-tO26euv7RzaFetmSkoUJOCmrdVPfVqkl1MZ8fcVOdBT1HiSG_5ZVQhlCeo4F--zpFsvNjIFzpkFNsK7rcxRT8TvgKkPzGg9M-CiL4hbXyba87xL9NAavOrQIO7S_vtfR7owiVWZxnTlxf2noYRPcsVDn1nKfKJKALJWViu9lBPBithEGt-ZzpHERC0-MqMvPHAIQBEq2jdCt7giwLhNuCeQlIh_OEZN8t-4nJe6OF1E1AJF49mkWmV7Oz3YNl86L6IxnINeIvmBL36KHkQUJERcwrRaATiXRQT4RuTRCbJ3revsdEuRP3_B6AuDW4ePjlMTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇾🇪
🇸🇦
الدفاعات الجوية اليمنية تتصدى للطيران الحربي السعودي.</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/naya_foriraq/90357" target="_blank">📅 03:48 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90356">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WByN3FHdWeol4IlEo29RN3KhZ2lVwfCHr4F_DBAIOf2oLE1zrZncJa8xO9U_3OMReR5wwPfLih-InmhfEP0iKqIr8fUEQp1MFCCkFnXfesBvUh25yautr6WhPWG_iugc_s7tHoGum5KWsV0kmmBL6gZwRDJjcMhRY6KK3zKGA6C-dEJFUnQcP1CUp3pl2IxmvWAexnfiS8q--89XK8VgxHggidlzpf5toHvr22DAZG3aScxndNgkgIHXc8tBhyGdHPfmNXLsxGbTajqeMlhOaQe4vkuwwh3UZE8fuHpGwfQGXze9_ZoYNMdv-sbYFh01kfANgObeZDyKhTC4uMQFVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
بعد مخالفتها للأوامر الإيرانية..
إستهداف صاروخي من قبل بحرية الحرس الثوري يطال سفينة في مضيق هرمز، أدى إلى تعطلها عن العمل.</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/naya_foriraq/90356" target="_blank">📅 03:09 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90355">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ce949aeb8c.mp4?token=hPzjEZGk_d8-89PM7m-CbsOSNLnWboRKfY52bziwVxlmuWVzMdLNo54wUVk5EfGeJwUn2MDT0d3iJaYu19a12geAGfo6CYtoqq_73ZGAwG_anaWrjBmcA8mi_XD02sKhlUG6jBNsgyzGXdD9xUCmqrv-yzUTBhBQ4aFg4PlkpmVuqxTm3i9T4JehTcbdDFPtFV4Ct7QfmR1alJqdYCNdmsL0WbnIse5iQRoKwjqFQjtT4rIOgC-s3BpHydS03IFpwCgF0KmpsSk0-uSOLB8Ybo1GLlBwV04kQLPjlQGF4oGtuIYEtwffzkrZiGf_JJ-WU8VosS6Xlcpj0GyuduRfeQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ce949aeb8c.mp4?token=hPzjEZGk_d8-89PM7m-CbsOSNLnWboRKfY52bziwVxlmuWVzMdLNo54wUVk5EfGeJwUn2MDT0d3iJaYu19a12geAGfo6CYtoqq_73ZGAwG_anaWrjBmcA8mi_XD02sKhlUG6jBNsgyzGXdD9xUCmqrv-yzUTBhBQ4aFg4PlkpmVuqxTm3i9T4JehTcbdDFPtFV4Ct7QfmR1alJqdYCNdmsL0WbnIse5iQRoKwjqFQjtT4rIOgC-s3BpHydS03IFpwCgF0KmpsSk0-uSOLB8Ybo1GLlBwV04kQLPjlQGF4oGtuIYEtwffzkrZiGf_JJ-WU8VosS6Xlcpj0GyuduRfeQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
حكومة إقليم كردستان العراق:
بعد اشتباكات عنيفة ألقت القبض القوات الامنية على وحدتين مسلحتين و21 عنصراً سرياً من تنظيم داعش في محافظة حلبجة، وصادرت كمية كبيرة من الأسلحة الثقيلة والمتوسطة والخفيفة.</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/naya_foriraq/90355" target="_blank">📅 01:06 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90354">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🇾🇪
القوات المسلحة اليمنية:
رداً على استمرار العدو السعودي المجرم في عدوانه على بلدنا نفذت القوات المسلحة اليمنية عملية عسكرية نوعية استهدفت من خلالها مخازن الأسلحة  وغرف القيادة والسيطرة التى تدير العدوان على بلدنا وشعبنا في القاعدة العسكرية بمنطقة شرورة السعودية.
وقد نفذت العملية بدفعة كبيرة من الصواريخ الباليستية والطائرات المسيرة وكانت الإصابة دقيقة ومباشرة بفضل الله وعونه.
نؤكد للعدو السعودي المجرم أن استمرار عدوانه على شعبنا سيقابل بعمليات أشد وأكبر فى عمق أراضيه وستكون عواقبها عليه وخيمة بإذن الله وقوته.</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/naya_foriraq/90354" target="_blank">📅 00:59 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90353">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🇸🇦
الاعلام الاجنبي:
‏أفادت تقارير بأن القوات المدعومة من السعودية في اليمن تضم بعض الكتائب التي تتألف من نحو 80% من "الجنود الوهميين"، وهم جنود مزيفون موجودون على الورق فقط لتحصيل رواتبهم.</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/naya_foriraq/90353" target="_blank">📅 00:36 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90352">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🇷🇺
🇺🇦
الكرملين
: اجتماع بين فلاديمير بوتين و زيلينسكي في قمة مجموعة العشرين التي ستعقد في الولايات المتحدة أمر مستحيل.</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/naya_foriraq/90352" target="_blank">📅 00:34 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90351">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dfe21f1049.mp4?token=v_cz2VPo1NEglovCxhd1cIDUSI3QDUwsHGV7eKp23_lb_ulw3IKr-J-l2csfnow-uyCrJcWaC_E4Jbgyxy5LAOcN3_n_dszk6lQ1yq-3RlZwLxpCLjLU-Ol69sO4vQo1mJaDD9dJgMnV9xqEOBeXEcxdtPA6Jly7zSYMO0FTUFVlVboEMhU6b65btKL7_EMxa9ABVZViW7IfMHuiOVrscCUdRsMdQKkfvf15vDU5W0U-Z_aQkEyCb2HKOBegsY3mAlfxOAoynIFJzxlHpIcuPKzkGlIxLr23aQ9FQuJEwOrcs2nMxnXHbY7aIySMUJ6egOTafBRJYoplsGvGTIerPllzprDZGc5dBCT9qQjk8oH_WnwRKFUz_mVgfjaE7ws9OunDgO6Z2ueUVn4coVWQEG53io6gnV7B_BWysvOwCvaLMAsT8sjj5SKISzYIY5bIUbY1znUzlx0FOs8-KAvSMRVD-BIpiy0qqo0b038nUdlNk0GiDAhKpcRIzP2-q3OpLU9Z4WyKUeSbIgoS09WuW7gg74gf0raY7DmG13tZaJYe6OpLLOnUz3UUd14_FPOX8wssTjliUianjtdcs4W6qG2b4Juw6iWk9zAOA0Tksil3z0d0FGcoaomWOz2wP721qNK6YdE2kyio7SZZJqRiNyYIGIJhTW1Uv0m1OjbY08k" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dfe21f1049.mp4?token=v_cz2VPo1NEglovCxhd1cIDUSI3QDUwsHGV7eKp23_lb_ulw3IKr-J-l2csfnow-uyCrJcWaC_E4Jbgyxy5LAOcN3_n_dszk6lQ1yq-3RlZwLxpCLjLU-Ol69sO4vQo1mJaDD9dJgMnV9xqEOBeXEcxdtPA6Jly7zSYMO0FTUFVlVboEMhU6b65btKL7_EMxa9ABVZViW7IfMHuiOVrscCUdRsMdQKkfvf15vDU5W0U-Z_aQkEyCb2HKOBegsY3mAlfxOAoynIFJzxlHpIcuPKzkGlIxLr23aQ9FQuJEwOrcs2nMxnXHbY7aIySMUJ6egOTafBRJYoplsGvGTIerPllzprDZGc5dBCT9qQjk8oH_WnwRKFUz_mVgfjaE7ws9OunDgO6Z2ueUVn4coVWQEG53io6gnV7B_BWysvOwCvaLMAsT8sjj5SKISzYIY5bIUbY1znUzlx0FOs8-KAvSMRVD-BIpiy0qqo0b038nUdlNk0GiDAhKpcRIzP2-q3OpLU9Z4WyKUeSbIgoS09WuW7gg74gf0raY7DmG13tZaJYe6OpLLOnUz3UUd14_FPOX8wssTjliUianjtdcs4W6qG2b4Juw6iWk9zAOA0Tksil3z0d0FGcoaomWOz2wP721qNK6YdE2kyio7SZZJqRiNyYIGIJhTW1Uv0m1OjbY08k" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انباء اولية غير موكدة عن سماع دوي انفجار في محافظة ديالى</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/naya_foriraq/90351" target="_blank">📅 00:26 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90350">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/654afe11fd.mp4?token=qjJ5u7twXWTYHMxDJ91uqDyMmMHpvR8AA0pAn0PXjphhXUW5i_VlDX5j4upYbdofuf-xyk2xH0STuD7cHyrduO7SXHBpN9fNjAwKPOjm_9u0kaseXo3ifcWJEOzoJ-8bHC3YLxQvvJdc2Bs6oepKveP7JjGC-Rw4oerC0FY-qv7_SE2f_Kjimvs_wiB3DjJCCqMrhF1suPQZ-4q7jaWT7TaBWSRBoowYj1NqHo6CCmYxWJ4UM5DvQ9YzqLzf_4FgLr96rA9mv6e-SY-YO4ynTfz7sD0lZ37JAODOwkK9foU_9QTdGJ_nwuN_L-m7iyCpQfB1Wpu-i54a-2YFN0BrMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/654afe11fd.mp4?token=qjJ5u7twXWTYHMxDJ91uqDyMmMHpvR8AA0pAn0PXjphhXUW5i_VlDX5j4upYbdofuf-xyk2xH0STuD7cHyrduO7SXHBpN9fNjAwKPOjm_9u0kaseXo3ifcWJEOzoJ-8bHC3YLxQvvJdc2Bs6oepKveP7JjGC-Rw4oerC0FY-qv7_SE2f_Kjimvs_wiB3DjJCCqMrhF1suPQZ-4q7jaWT7TaBWSRBoowYj1NqHo6CCmYxWJ4UM5DvQ9YzqLzf_4FgLr96rA9mv6e-SY-YO4ynTfz7sD0lZ37JAODOwkK9foU_9QTdGJ_nwuN_L-m7iyCpQfB1Wpu-i54a-2YFN0BrMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
توثيق من الجانب العراقي للطريق المؤدي إلى منفذ الشلامجة، حيث يظهر خاليًا تمامًا من حركة الوافدين والمغادرين عقب إغلاق المنفذ.</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/naya_foriraq/90350" target="_blank">📅 00:07 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90349">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">كمين محكم على قوة مكونة من عشر آليات أثناء محاولة فرارها
عملية "والله أشدُ بأساً وأشدُ تنكيلاً"</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/naya_foriraq/90349" target="_blank">📅 23:51 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90348">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa40032226.mp4?token=PjUESaeWfMffsqiS2JQSRRdLsCw0gRhV7y90OPanRFhUEn192-DetFSymf0TkqVHARopmnVzAEEON4L-H7-9lnP3TkFGe1XwVa12zInGKI3iXu6UM8XNZGMgF4poVwe2nmr-TiYob-9EllmZvIHzYB-3ZOCsDImeXw4vhuzi9FJdqyoXU2fsrCtCykFhP_9j7E2RRC-Ulr7yz1GadU4q1EVea1r7t82gh4n3WTvtEPqwJpVRSAcdU0fbkybwGX8okptW9FWIW41HoIH2y3NsplBujnbJXlke3Uab-lM1PUXuDfYVTJKOfMoIihPL518MjY7X4vzzeS-O6Y6bz4z1rw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa40032226.mp4?token=PjUESaeWfMffsqiS2JQSRRdLsCw0gRhV7y90OPanRFhUEn192-DetFSymf0TkqVHARopmnVzAEEON4L-H7-9lnP3TkFGe1XwVa12zInGKI3iXu6UM8XNZGMgF4poVwe2nmr-TiYob-9EllmZvIHzYB-3ZOCsDImeXw4vhuzi9FJdqyoXU2fsrCtCykFhP_9j7E2RRC-Ulr7yz1GadU4q1EVea1r7t82gh4n3WTvtEPqwJpVRSAcdU0fbkybwGX8okptW9FWIW41HoIH2y3NsplBujnbJXlke3Uab-lM1PUXuDfYVTJKOfMoIihPL518MjY7X4vzzeS-O6Y6bz4z1rw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انباء اولية غير موكدة عن سماع دوي انفجار في محافظة ديالى</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/naya_foriraq/90348" target="_blank">📅 23:32 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90347">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">انباء اولية غير موكدة عن سماع دوي انفجار في محافظة ديالى</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/naya_foriraq/90347" target="_blank">📅 23:27 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90346">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">حدث امني في محافظة كركوك</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/naya_foriraq/90346" target="_blank">📅 23:00 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90345">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🇺🇸
الاعلام الاميركي:
ضغط مكتب وزير الدفاع بيت هيغسيث من أجل ظهور اثنين من الطيارين الأمريكيين الذين تم إنقاذهم بعد إسقاط طائرتهم من طراز إف-15 فوق إيران في مقابلة مع برنامج "60 دقيقة" للحديث عن عملية الإنقاذ.
كان لدى الطيارين في البداية مخاوف بشأن المشاركة وكشف تفاصيل عسكرية حساسة. بعد التحدث مع هيغسيث، وافق أحدهما على إجراء المقابلة بينما رفض الآخر.
كما أعرب بعض المسؤولين العسكريين عن مخاوفهم من أن المقابلة قد تكشف معلومات سرية أو تستخدم لأغراض سياسية.</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/naya_foriraq/90345" target="_blank">📅 22:55 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90344">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">الله اكبر
سقوط مباشر في جيزان بالسعودية</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/naya_foriraq/90344" target="_blank">📅 22:27 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90343">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🇮🇶
تعرض ارهابي على نقطة تابعة للجيش العراقي في محافظة كركوك شمالي العراق</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/naya_foriraq/90343" target="_blank">📅 22:22 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90342">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">حدث امني في محافظة كركوك</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/naya_foriraq/90342" target="_blank">📅 22:19 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90341">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">حدث امني في محافظة كركوك</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/naya_foriraq/90341" target="_blank">📅 22:18 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90340">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🇮🇶
الناطق باسم القائد العام للقوات المسلحة العراقية
: متأهبون لعدم تكرار مثل هذه الاعتداءات على السعودية.</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/naya_foriraq/90340" target="_blank">📅 21:58 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90339">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">مشاهد أولية من عملية "والله أشدُ بأساً وأشدُ تنكيلاً" العسكرية النوعية الواسعة من عدة مسارات متزامنة - 12 سبتمبر 2026م</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/naya_foriraq/90339" target="_blank">📅 21:45 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90338">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🇾🇪
مشاهد الإعلام الحربي من عملية "والله أشد بأسا وأشد تنكيلا" العسكرية النوعية تعرض عند الـ 9:00م بعد قليل</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/naya_foriraq/90338" target="_blank">📅 21:45 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90336">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">انفجارات قوية في خميس مشيط</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/naya_foriraq/90336" target="_blank">📅 21:31 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90335">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/naya_foriraq/90335" target="_blank">📅 21:30 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90334">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">انفجارات في سعودية</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/naya_foriraq/90334" target="_blank">📅 21:30 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90333">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🇾🇪
مشاهد الإعلام الحربي من عملية "والله أشد بأسا وأشد تنكيلا" العسكرية النوعية تعرض عند الـ 9:00م بعد قليل</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/naya_foriraq/90333" target="_blank">📅 21:27 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90332">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">اطلاق صاروخي نحو مضيق هرمز</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/naya_foriraq/90332" target="_blank">📅 20:41 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90331">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e4cadf14a.mp4?token=SsOcTTCvy3xrQLsYew0epdHKV4ZcD_Dc-P_OLj_ZeZZpQ_kzk-KEmaQu6JnvJxYnJJgCBNxFrnrkiB1o5erUju3bO-fPCsUhGmRp3-sY6u3uPScBy6QGW0JwULnl3F2OFCZ97cCy7I6HgYil4Q_BmD4G8OBHmqecXAOlD4_1gBiUx_3yqAb4uk1vrP9ifuJuwSsQjxYB-Botyre6uaYnl34nMIYfY0QP3JzcXRbFyWqF7G_SHoNIUdGS8YNxDWmJFjiO6I-N2LOIhZoWufVylUoG6du3ufw83Sp2290XIxQ5oyBbyiyzpE7lmM15OuvwRErEoF2-9B9GRKS7NCTZEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e4cadf14a.mp4?token=SsOcTTCvy3xrQLsYew0epdHKV4ZcD_Dc-P_OLj_ZeZZpQ_kzk-KEmaQu6JnvJxYnJJgCBNxFrnrkiB1o5erUju3bO-fPCsUhGmRp3-sY6u3uPScBy6QGW0JwULnl3F2OFCZ97cCy7I6HgYil4Q_BmD4G8OBHmqecXAOlD4_1gBiUx_3yqAb4uk1vrP9ifuJuwSsQjxYB-Botyre6uaYnl34nMIYfY0QP3JzcXRbFyWqF7G_SHoNIUdGS8YNxDWmJFjiO6I-N2LOIhZoWufVylUoG6du3ufw83Sp2290XIxQ5oyBbyiyzpE7lmM15OuvwRErEoF2-9B9GRKS7NCTZEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇾🇪
🇸🇦
من الاضرار التي لحقت بمصفى جيزان التابع لشركة ارامكو السعودية اثر الضربات اليمنية.</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/naya_foriraq/90331" target="_blank">📅 20:23 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90330">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">وكالة تسنيم:
أشار المصدر المطلع إلى أن العراق سيحضر الاجتماع أيضاً، إلى جانب إيران وعمان والدول الأخرى المطلة على الخليج الفارسي. ومع ذلك، سيقتصر دور هذه الدول على الاطلاع على نتائج المفاوضات الإيرانية العمانية، حيث تم حسم القرارات المتعلقة بتفاصيل الاتفاق خلال جلسات فنية بين الجانبين الإيراني والعماني، مضيق هرمز لن يعاد فتحه بموجب التفاهم مع عمان.</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/naya_foriraq/90330" target="_blank">📅 20:04 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90329">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🇾🇪
القوات المسلحة اليمنية:
شن طيران العدو السعودي خلال الـ48 ساعة الماضية 129 غارة جوية توزعت على محافظات تعز ومأرب والحديدة والجوف وصعدة وعمران وحجة.
تم تنفيذ هذه الغارات بواسطة طائرات F15 وتايفون وأقلعت من القواعد العسكرية للعدو السعودي في خميس مشيط والطائف.
إن هذه الاعتداءات على شعبنا لن تمر دون رد وعقاب بإذن الله وقوته.</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/naya_foriraq/90329" target="_blank">📅 20:01 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90327">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a60a908ab2.mp4?token=Qqzvgu7Akr9aEpX_n_aaGcCJWK4t6MNL4cv8KKMDgyGIPLwpjAocCx40lnyGp0dn8SW7yFM7XdQFEo0q6d4CeumU8SdMh3t0kGH0UlvZq3JJLrjUMI_CoSlmjg1JN-yqjW4mc8XGcbSeW6SbUFk_oK7PBeFAjKCjzJJY3rUUBVe-xY_TyJJCCPP5gDRZXKIwvZJyAvDFKzD1pZcy5at47gBaC8JtH2XFRYi1Yyh_yO8sX9X2ujCXeQ_J2XoArtGZs2g-wb2PxvteGavQxcRCQOJBWVFqfjhfIWIC-KYq4428xppuLYewEEnZ2f5ytkVRXr41wUP7RupXAyiDKDyfnA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a60a908ab2.mp4?token=Qqzvgu7Akr9aEpX_n_aaGcCJWK4t6MNL4cv8KKMDgyGIPLwpjAocCx40lnyGp0dn8SW7yFM7XdQFEo0q6d4CeumU8SdMh3t0kGH0UlvZq3JJLrjUMI_CoSlmjg1JN-yqjW4mc8XGcbSeW6SbUFk_oK7PBeFAjKCjzJJY3rUUBVe-xY_TyJJCCPP5gDRZXKIwvZJyAvDFKzD1pZcy5at47gBaC8JtH2XFRYi1Yyh_yO8sX9X2ujCXeQ_J2XoArtGZs2g-wb2PxvteGavQxcRCQOJBWVFqfjhfIWIC-KYq4428xppuLYewEEnZ2f5ytkVRXr41wUP7RupXAyiDKDyfnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇾🇪
🇸🇦
غارات من طيران العدو السعودي يستهدف محافظة البيضاء.</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/naya_foriraq/90327" target="_blank">📅 19:54 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90326">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MM4yXNr3xrSxdu9gXCTmrgjamPaYessoBVERay2YMO2Udt--nUBcd8ut5Afhg2sv6fpBCVtZdKrC70OUknsy6U-eQKEcr--TZQtndYTpfy-hIQVlHLH_JfE8sNMH9T9cguoPFlAAS1NC9aUe03X1OqNuuzUJtjAYIDLGCefaNHlqJ4N1GJxdVQ9z9c3R4eWkjYrqNbFk1QGzWuzSUWpRF9isfP-rpCPC91xDIEboBU3vICxnX1aMrVn5g8j2HxKrQhpw818r1vEMQp4VsSDK5M0ci9Vzhd-6IM7bwa6dmWVcIP-4cdDCwkHNb3BNtGFqLeVwTA_7pgQo5IR0sqI-cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇾🇪
🇸🇦
غارات من طيران العدو السعودي يستهدف محافظة البيضاء.</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/naya_foriraq/90326" target="_blank">📅 19:53 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90325">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/85a33591f6.mp4?token=D7qdEbQMH5ntUG3qDZar-9DgTLGhxpZqIoKg8TmI1p31G1dqitQMfGIzzIYDBTD59uH5tNnFRgrGo4EfFmUKTSekxWe0_SxmNPtydGM1KL_3mSLKsiJPRYsAltg85gZ1SjyOqnDUd6bUzpOcSDd25RGe_V29n1_FLbhIgPdkskx8vTAH6Fgvi6jt7eixZ5uq5oB74W2PsA1L6VvPoTDfMOhZIgcj_18XGrwf7aypYJsUCcFDYha4iSPRaZLctY33Pn8q944cSDHklzdyPRzYuhZ5Lmrh38G5_D84lZrrPrnTm16iAonrzb59ugfJUEkmRdwS4R6QNeqVRTCbLZQvyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/85a33591f6.mp4?token=D7qdEbQMH5ntUG3qDZar-9DgTLGhxpZqIoKg8TmI1p31G1dqitQMfGIzzIYDBTD59uH5tNnFRgrGo4EfFmUKTSekxWe0_SxmNPtydGM1KL_3mSLKsiJPRYsAltg85gZ1SjyOqnDUd6bUzpOcSDd25RGe_V29n1_FLbhIgPdkskx8vTAH6Fgvi6jt7eixZ5uq5oB74W2PsA1L6VvPoTDfMOhZIgcj_18XGrwf7aypYJsUCcFDYha4iSPRaZLctY33Pn8q944cSDHklzdyPRzYuhZ5Lmrh38G5_D84lZrrPrnTm16iAonrzb59ugfJUEkmRdwS4R6QNeqVRTCbLZQvyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تدمير 6 خزانات نفط على الاقل في ابها</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/naya_foriraq/90325" target="_blank">📅 19:41 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90324">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6722e8cb2c.mp4?token=aMZ19wtOaIBLX_stzX_DJ9xv0lCQXTHR6Lde9LSty8nDJUqpoAw7EerlEhA5bNebGtdUszieBZeVsqFSJ6xUL_BVWVZoDAoKeMXWr1C2WCsmJmTVucMfz0RU3dcWqtgr_7GoRqF-XDgMLsRLBMKdD0znCw6HURF7wsNrDzdNL_mmMiMxW2u4vGtzDO4oO1hkNOEy1sc65dIvHxANGQc_L6MV-42ZNIbukzhmjIxRHOgVxVZ2_y69-ijIdXk2hx5KlByLouX76j1lkXEDWJs5VbD8CdYR2ElV-YurNk6T7vu4BCWR2dDBnp21vh1WoJGQmr9-hSEroj9rRme9JJPk2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6722e8cb2c.mp4?token=aMZ19wtOaIBLX_stzX_DJ9xv0lCQXTHR6Lde9LSty8nDJUqpoAw7EerlEhA5bNebGtdUszieBZeVsqFSJ6xUL_BVWVZoDAoKeMXWr1C2WCsmJmTVucMfz0RU3dcWqtgr_7GoRqF-XDgMLsRLBMKdD0znCw6HURF7wsNrDzdNL_mmMiMxW2u4vGtzDO4oO1hkNOEy1sc65dIvHxANGQc_L6MV-42ZNIbukzhmjIxRHOgVxVZ2_y69-ijIdXk2hx5KlByLouX76j1lkXEDWJs5VbD8CdYR2ElV-YurNk6T7vu4BCWR2dDBnp21vh1WoJGQmr9-hSEroj9rRme9JJPk2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صور الأقمار الصناعي تظهر حدوث أضرار جسيمة في محطة أبها التابعة لشركة أرامكو في أعقاب هجمات انصار الله، حيث تم تدمير ستة خزانات نفط على الأقل بالكامل وتعرض ثمانية خزانات أخرى لأضرار طفيفة.</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/naya_foriraq/90324" target="_blank">📅 19:19 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90323">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KXeSsTMQt_PiEVj99v2PwADfmHow_TdPQA-FQO8j2mTenLiKeET7pBO1XvMb4mibBGCr8LvOnMF44lR4DFTSOed8ZsuCMmJY8SKWPDSFspqpjRTgoTICzRKaMOfcSIm0lN9s8zM1c8cioz62dwFcsVMXUnmAu5FKGRcCXtFYYFv8IfSFfo7vEQ981xOWD2r_VcTMLmULjqSJHAK7Uhp8M2ZVJDI_VpmgsFNLWcZZyDg42JUdL0CBi6ywq_7tIUWyWwG7SH3stPbyoXoj6jRRFU2ZtzkHB1s6GCy6sbS5TN50jwCv5qhwIlenCBwO2FCiUJTBZ_jbae5Ot9uINiphug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صور الأقمار الصناعي تظهر حدوث أضرار جسيمة في محطة أبها التابعة لشركة أرامكو في أعقاب هجمات انصار الله، حيث تم تدمير ستة خزانات نفط على الأقل بالكامل وتعرض ثمانية خزانات أخرى لأضرار طفيفة.</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/naya_foriraq/90323" target="_blank">📅 19:18 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90322">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">العراق يعيد اغلاق منفذ الشيب مع ايران</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/naya_foriraq/90322" target="_blank">📅 18:50 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90321">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🇾🇪
🇾🇪
وزارة النقل اليمنية: باب المندب سجل عبور 36 سفينة في 10 سبتمبر و37 سفينة في 11 سبتمبر.</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/naya_foriraq/90321" target="_blank">📅 18:01 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90320">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🇮🇷
وزارة الخارجية الإيرانية:
تفاهمنا مع عمان بشأن ممرات العبور في مضيق هرمز لا يعني بالضرورة أن المضيق آمن للملاحة.</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/naya_foriraq/90320" target="_blank">📅 17:59 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90319">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🇾🇪
🇾🇪
وزارة النقل اليمنية:
باب المندب سجل عبور 36 سفينة في 10 سبتمبر و37 سفينة في 11 سبتمبر.</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/naya_foriraq/90319" target="_blank">📅 17:58 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90318">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/69e86b9dc9.mp4?token=LL9oS5UmKv_tHzo01dalNKhqLs3T8b2Is5l5apw4d8WsL-TwVmVwmpT4X9QBhqByJGD-NV8TAWS8-Wbi0AqSAKRgK9IvqPa5pVgDIza1RyWuDEPZMYT1wNw8qElL82WVFeWGEVddbWmPM1QDzPkneZioK3atqos6xk1pL4JwrxXls3jK9p1JNXX2EFSiIERL7rgLXHFJ4--C_5j4K0TMuxyl0omI0lCQqv_VLgI6XZNuEO8jmlxTckmeio3PvY1hw0cs7y4hb0KCaoR8Wx1Y-Coq6_qO9ZfQAp6lRoBtBIMDStEjQzyEQWdgsd0RHELFD1fEYqBH99UnYiSnCsQ2zg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/69e86b9dc9.mp4?token=LL9oS5UmKv_tHzo01dalNKhqLs3T8b2Is5l5apw4d8WsL-TwVmVwmpT4X9QBhqByJGD-NV8TAWS8-Wbi0AqSAKRgK9IvqPa5pVgDIza1RyWuDEPZMYT1wNw8qElL82WVFeWGEVddbWmPM1QDzPkneZioK3atqos6xk1pL4JwrxXls3jK9p1JNXX2EFSiIERL7rgLXHFJ4--C_5j4K0TMuxyl0omI0lCQqv_VLgI6XZNuEO8jmlxTckmeio3PvY1hw0cs7y4hb0KCaoR8Wx1Y-Coq6_qO9ZfQAp6lRoBtBIMDStEjQzyEQWdgsd0RHELFD1fEYqBH99UnYiSnCsQ2zg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">القوات المسلحة اليمنية تتقدم في تعز وتسيطر على مواقع استراتيجية بعد اشتباكات مع مرتزقة السعودية</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/naya_foriraq/90318" target="_blank">📅 17:31 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90317">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">القوات المسلحة اليمنية تعثر في باب المندب على احدى سفن العدو الامريكي والاسرائيلي التي دمرتها القوات المسلحة اليمنية</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/naya_foriraq/90317" target="_blank">📅 17:08 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90316">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">انفجارات سمعت بوضوح بالجانب الشرقي من السعودية</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/naya_foriraq/90316" target="_blank">📅 17:03 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90315">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/naya_foriraq/90315" target="_blank">📅 17:02 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90314">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/354f2e2cdd.mp4?token=LccoP2RjHaKbA0SACbpVj0OPd4eYZWyhG3bCASpmYGnY-YUFE52l_i0x0cABmsg2nHjnkWsdzFAuCFgwzD_0-D9Rg86oFBaHceQPlm7JQqDmCS1odVir8x_v3ZOSFmS4pJfZ8HmzzfNe3B9O0nWghtbekBMEZcYwVM4c7l9RbglxA-Dg2GDSPCB5AEBL2-e09y40QIs-6YW6IW-zOv-TjoQ-Km4k5CBS-VEPvtdzy6-SViM_0f8fGZNQ_EaqQzVdGaR5zGe2SRRErfL1oztKf_HYHjF_4IbYlqfotFDObv8GeATxBltE27dGAMfoSbpJ5CNBp0gZKgskq2de0B-DgwnC8b274143NjzAFH2dw_MT9kZrRUjvr7l3pG-11s8pt0fkNx2nMXy1guWCtsBUS67xwhRyirlso8HGP5joQKy3ebwgmMg2vfIk-qlVgMxf7cUzOMz1__ZtIFj60-Uxkg2TQBmYWbJLChhV88HGqrWc_E9YeOR0sFX8bpgS17HAvGmEDcU647fEdVP2fvaNuN4VC6nHc6FXkw_tz85_uGRPl4aBHhq9OIiNA4i9s8bmES10FGBQ1KDTpwTZbS1RXY0-fGiPX1VyPhnMj0mJEPeVqCX7Q2Dw8UHvk-vN9El-1adIt4wZQZlJbw6oYFdLZy4oss-_KyXN2IbcrNqTxEY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/354f2e2cdd.mp4?token=LccoP2RjHaKbA0SACbpVj0OPd4eYZWyhG3bCASpmYGnY-YUFE52l_i0x0cABmsg2nHjnkWsdzFAuCFgwzD_0-D9Rg86oFBaHceQPlm7JQqDmCS1odVir8x_v3ZOSFmS4pJfZ8HmzzfNe3B9O0nWghtbekBMEZcYwVM4c7l9RbglxA-Dg2GDSPCB5AEBL2-e09y40QIs-6YW6IW-zOv-TjoQ-Km4k5CBS-VEPvtdzy6-SViM_0f8fGZNQ_EaqQzVdGaR5zGe2SRRErfL1oztKf_HYHjF_4IbYlqfotFDObv8GeATxBltE27dGAMfoSbpJ5CNBp0gZKgskq2de0B-DgwnC8b274143NjzAFH2dw_MT9kZrRUjvr7l3pG-11s8pt0fkNx2nMXy1guWCtsBUS67xwhRyirlso8HGP5joQKy3ebwgmMg2vfIk-qlVgMxf7cUzOMz1__ZtIFj60-Uxkg2TQBmYWbJLChhV88HGqrWc_E9YeOR0sFX8bpgS17HAvGmEDcU647fEdVP2fvaNuN4VC6nHc6FXkw_tz85_uGRPl4aBHhq9OIiNA4i9s8bmES10FGBQ1KDTpwTZbS1RXY0-fGiPX1VyPhnMj0mJEPeVqCX7Q2Dw8UHvk-vN9El-1adIt4wZQZlJbw6oYFdLZy4oss-_KyXN2IbcrNqTxEY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">النقطة الاهم في العالم - مضيق باب المندب</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/naya_foriraq/90314" target="_blank">📅 16:56 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90310">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vkRdcCEu-_jdvWfLHG-Jmjeh5Wb-4qtdhHms7GFW-SI32XI8rULAITYzYj-tyqeEAah2bmnBS7aLY9_-LUDXExRU9qtgpbkn1n6WBEFqzXYca4EZemgYU2130kjroIYs4qI6QlQ41po3vhKA3mVxKB3dJy_G54uvqf8MtlO7cLUZ6iXgIXfNK3zYcK029qEe0Nhi6oauTlf6COQAiSa1zB7TUFTOecjcWRR5V2nZE-QmQXreZgB-Tu6ltWocjPQhIsFCalFyKF7Ytcky6CT1rjgacKOSe48ppQ4xoFhSDCA0DkHGmZiD6i0jyolGGspVcmYtlKlFL8ez77kDFRKr2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QZD1q5hPu7tPOD9mytmJ4ztZdlTNdgL4U9uWCT5JYp-gD9C0PJyqx4uX-zRWoX_Mt-FhuLNfbGIszfe40Hz33CfYZc3jx5YTE2Z2R5J0AriZ2UQXh1tlAlSQCFxQ_kqSf_rshK0sAAeR7lqIcF7ECB3ori-83NTFbktoWbCzSL1fXnMgRLebR8Dr_wWS1kw077NbRlSUzaBm_kl-s-047FiaHtdrl-Z8GbLe0ZE6owMcedsHWh5XCrS7qd7NY0KSaedXjglQJm8vB4GmeXyq1sPfxgPus0vDNeDAN20VNJ9zGohKEg4mO2ON9eMk7vkwpq3IxYz20OUbBJOMxNyNxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DUsYoLM-72KswNoia4xwrJOzo8S2JRRrKqWER57hUdDN97aXBt-zggLR5hRHOfRq1AWOcig4i1N9JUofJ02UoAfoeV9Wufa7cVXU_YzOnN-K2J6ymazqPHEnpu3ibLKsmnJ9-qfllE8uHoyMDVdDrAMcM0unm3YLbFEwAaNTXONfjxEf2RwAmqUuorVJimu9xrsNxVHfMsxXt_VF3FhsEz0QnJSoM9dRIx2WMj3T7xV8p5WMfGZWmYhjkncZDkXilC_yOXjCYeWBeK5d0r0qUHOflnrVH5oDNnQlrMnYuTIGHFKcVhkujiIN6NhQ4tAQW-rbEnnDn5a0HflbifDafw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BObLPwF21YqYyU-khCaRtXno5ZZMYsKeKsQgaPvk6Oxi-NMVoTxbTJV4kHmReuhrHSfAuiUk49OU4vpOOp0OW-3mQRxS60xDAXVmA6k7QQWj7kGDhFj_kSzxyXZyXYT2pIchOC96-YoY2Cni0QiFdnw2tPiPUST_-xWPv8yU-lpj-u_Ee1HDahUphZnY2TgxZBneToFs7gF-k4hM4q4TCKSRX3DZ8pov-N9vzB5gb77o30qtfIzQnuPXOV7tBHzy2hq-lyvjzgnEDJWTzocy0G9FT494EZdPrIWQKexwzLmXIqUoCkzgEB21pyDY3g4Zeq-S6n0X559OFHiPgbsR8w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">بعد ادعاء المرتزقة يوم امس انها سقطت بيدهم.. محافظ البيضاء التابع لانصار الله يتفقد أحوال المرابطين في مديرية الزاهر.</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/naya_foriraq/90310" target="_blank">📅 16:46 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90309">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🇮🇶
🇮🇷
مكتب رئيس الوزراء العراقي:
الموافقة على طلب الجانب الإيراني لإجراء تحقيق مشترك بشأن العثور على منصات إطلاق طائرات مسيّرة قرب الشريط الحدودي العراقي الإيراني.</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/naya_foriraq/90309" target="_blank">📅 16:20 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90308">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">المدن اليمنية تواصل استقبال الاسرى المحررين من سجون مرتزقة السعودية</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/naya_foriraq/90308" target="_blank">📅 16:19 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90307">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🇮🇷
المتحدث باسم الخارجية الإيرانية: خطط لعقد اجتماع إقليمي يضم العراق ودول الخليج الفارسي.</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/naya_foriraq/90307" target="_blank">📅 16:14 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90306">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">استقبال يمني رسمي وشعبي للاسرى المجاهدين المحررين من سجون مرتزقة السعودية</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/naya_foriraq/90306" target="_blank">📅 16:10 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90305">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🇾🇪
🇾🇪
نائب وزير الخارجية اليمني:
النظام السعودي يسعى لتخويف المجتمع الدولي وتضليله، ونؤكد التزام صنعاء بالحفاظ على سلامة الملاحة الدولية.</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/naya_foriraq/90305" target="_blank">📅 15:37 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90304">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🇷🇺
السفير الروسي لدى اليمن:
نؤكد دعم بلادنا للجهود الرامية لخفض التصعيد وتحقيق السلام في اليمن والتخفيف من المعاناة الإنسانية.</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/naya_foriraq/90304" target="_blank">📅 15:37 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90303">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">التلفزيون العراقي يقول ان لجنة أمنية رفيعة المستوى وصلت إلى منفذ الشلامجة للمباشرة بـ"التحقيقات في الخروقات".</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/naya_foriraq/90303" target="_blank">📅 15:07 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90302">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">استقبال يمني رسمي وشعبي للاسرى المجاهدين المحررين من سجون مرتزقة السعودية</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/naya_foriraq/90302" target="_blank">📅 15:01 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90301">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mGrKkqj9_Ws5wqPirN4jLm3b5Xu3fj6uSC1UfoxuUnAw8vfxkA6nic5MgZX6a3g_hGq3PF-QxCwiUt-r9YLO-x8U4TI9uom9DtSAW6N-Q1dXyxpcq0p1_jAxhtSZQWoNKeZiEZZrbhnCLPW7lWoo9GF251DVlNPBaNqHJy5-YapLDUJvfUzikrsspgtUFwoNrsoTGkS8NyIPYV_xGJ3O5uKvjt_wbnl51V475bf1ynMbDJ3WIlyvQysrApUBlZnEbtGi5pxqlI7-JplVqAXU7w1KSLGvgsjcBaQdaW_0kZKT3Dl1BO_sZ3iwpT3lHWrJO5m4cu3A9-8lHu67bxeCTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامب حول الهجوم على خط الأنابيب السعودي: الحوثيون يتجنبون الصدام مع الولايات المتحدة.</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/naya_foriraq/90301" target="_blank">📅 14:41 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90300">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🇾🇪
🇾🇪
القوات المسلحة اليمنية:
ترقبوا مشاهد من عملية "والله أشد بأساً وأشد تنكيلا" العسكرية النوعية.</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/naya_foriraq/90300" target="_blank">📅 14:16 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90299">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">اعفاء قائد شرطة ميسان من منصبه</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/naya_foriraq/90299" target="_blank">📅 13:32 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90298">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">اعفاء قائد شرطة ميسان من منصبه</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/naya_foriraq/90298" target="_blank">📅 13:31 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90297">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">رئيس الوزراء العراقي يوجه بالسماح بدخول العالقين من المسافرين في الجانبين بمنفذي الشيب والشلامجة الحدوديين</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/naya_foriraq/90297" target="_blank">📅 13:25 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90296">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">ترامب حول الهجوم على خط الأنابيب السعودي: الحوثيون يتجنبون الصدام مع الولايات المتحدة.</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/naya_foriraq/90296" target="_blank">📅 13:21 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90295">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c12c317f4b.mp4?token=IZFYVq8vsqwsX5POCk1UayDN9jueSZBkWU5ZRcLfXtMwBZzEGSAXmJFcSX8ZcF5xnEfMOQOxOod7XyxBv0jstep3jPuKZyznlmXddBurq-OcVcNsbzwjpF97BA_cdR_OZLqS_ziHRiukRIC7_Rk1NuKBrlQ7LQ4IgN8UWmQl1VFOj4IDQ3y2U4qu_u5ifQ5tEOQY12UbUplQwA46ZPVltxZAVCzJ8IvUkMVeAqJdzbBaNBIPDMrXn2iWiCp3huUq_b2tzUJvM6t2rnZPqUeeUkcpTgVl1_5-H4tKvGZiMIo_MHTxcQmBdEFm8MQrcahzgbtRXBQM1CjI9GodfBripQOirBNtSny-VB53q-QGui2FGH4fz0eDsj1MQc7TCab-0UCpKhafbHz4eO1C0Rw7515NYObs2X90gYhw8hrrt3qGVRAgxJuFCzAunbYu2ZDpHxdiaT6vmT9AnZ2Dj_QL8HOk2tslzsc5yEb4tWvTX0M0PnTcIdPBnx6uVF2QLH2m5REadmOizpnNNBX-LVt-D8iog3GXe5i1kQ4oumJM1ERShBgEhktNRXGqd1mCwghuLdQL-EqB6JDBP6b0DX35bHaV23W0XRq68P_WaAedRh2kFyHD4YZt7b7XkKOIiTktz0T92dKbNPgSn4AabFN2IUwNUYFraZia4CQ9KL7sYRM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c12c317f4b.mp4?token=IZFYVq8vsqwsX5POCk1UayDN9jueSZBkWU5ZRcLfXtMwBZzEGSAXmJFcSX8ZcF5xnEfMOQOxOod7XyxBv0jstep3jPuKZyznlmXddBurq-OcVcNsbzwjpF97BA_cdR_OZLqS_ziHRiukRIC7_Rk1NuKBrlQ7LQ4IgN8UWmQl1VFOj4IDQ3y2U4qu_u5ifQ5tEOQY12UbUplQwA46ZPVltxZAVCzJ8IvUkMVeAqJdzbBaNBIPDMrXn2iWiCp3huUq_b2tzUJvM6t2rnZPqUeeUkcpTgVl1_5-H4tKvGZiMIo_MHTxcQmBdEFm8MQrcahzgbtRXBQM1CjI9GodfBripQOirBNtSny-VB53q-QGui2FGH4fz0eDsj1MQc7TCab-0UCpKhafbHz4eO1C0Rw7515NYObs2X90gYhw8hrrt3qGVRAgxJuFCzAunbYu2ZDpHxdiaT6vmT9AnZ2Dj_QL8HOk2tslzsc5yEb4tWvTX0M0PnTcIdPBnx6uVF2QLH2m5REadmOizpnNNBX-LVt-D8iog3GXe5i1kQ4oumJM1ERShBgEhktNRXGqd1mCwghuLdQL-EqB6JDBP6b0DX35bHaV23W0XRq68P_WaAedRh2kFyHD4YZt7b7XkKOIiTktz0T92dKbNPgSn4AabFN2IUwNUYFraZia4CQ9KL7sYRM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامب حول الهجوم على خط الأنابيب السعودي: الحوثيون يتجنبون الصدام مع الولايات المتحدة.</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/naya_foriraq/90295" target="_blank">📅 13:21 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90294">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V-LBlfIeKZ-JldGPS68QMXBVFpY7zq3eM0VyswCLhqUnyD7bj5bynw_r65P43tEiXjbHL2d4ZZqDE6JQ2bUHr4u3pTQNzucZDwOZnnNMzALO7vndDp8KSCA99IlmRLZYrPwt0vBUahwVYG4EmNghMIJCC25tUqeeOJFLM5UeRp763lxzzblE-im-W2ojh36oLucZOCarWqDSlo1dyqkiVAhUSqUssqPbJvLHyPSLABn_JymnqCCdbK0AbFH6LDKhOyiJRuv8OxUaZjIwaDMgZJM3IkLiVz1JcxhCTpEz6H8mBCdzS9cxFXUgKAylaTXfCWhwjDGrZ9XOnBbqzQh5bA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
🔻
رئيس المجلس السياسي لحركة النجباء مغردا:
نشعر بالفخر والاعتزاز ونحن نرى هامات اليمنيين مرفوعة بانتصاراتهم المؤزرة.</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/naya_foriraq/90294" target="_blank">📅 13:01 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90293">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/38811a403c.mp4?token=EOV9kNLBPwmyPn7fKwTvMzn6KWHtVVlBwv3HXz4k20E60I3HPGyxfoZTpk5KAK19-kosFkt-hk-ngIQ3tkbiBJeyjuEYnOuBbCz0Fyxmto517g4xbB2G3xmYtQ7_RaWcM4OcMfSSfPxKup9Qql4gybhO96RY-_cRcrCd4MiwN6PAo4Q2dMX9d_qaAmsF3a8lJcwLBX63SYBISmMFEacsKhlEWgFVG4tZmTBt16b9a_XOyUJEoTeXtgEy6yUb4QCdX1_q5_cXfi8uClyGMzOlCfFo7KFclrhwT0jSeL3MqJKnkO6DWLsdGinZXN6-gyl6vEc8mPztyWEOQgg598aC9p9fh1DBERT7rqSNTyzZuBhP7-1Qqp5ckEug4AOj0XPrGq-zoKCyaSvdTyzoJ5WSaObipBPX0hIsbUCQpm1HQqmgw8EQaeKMD4feyIhhESrHHJe6DhZRCuPk3Qsh7BRSnKP7_5Bc7kxNXHT6meBwI9loXHhV8uOe-lfLHGGg8Vc6HROP-zz091RqdtsOlKlYEe5h3JyBj7i2JWnl5UJi-S-_IHzGi_klcwwN4DGDFojlav8j-fKjx37bavgv_Msvcp9XyppfwMkgxV_9Nq-Xg0dyUK376Hd0b0UVEH0P3IE2iQodTvlqswPtmaz6mAoqreg4DwZ_8evB0rKSJTKXSNE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/38811a403c.mp4?token=EOV9kNLBPwmyPn7fKwTvMzn6KWHtVVlBwv3HXz4k20E60I3HPGyxfoZTpk5KAK19-kosFkt-hk-ngIQ3tkbiBJeyjuEYnOuBbCz0Fyxmto517g4xbB2G3xmYtQ7_RaWcM4OcMfSSfPxKup9Qql4gybhO96RY-_cRcrCd4MiwN6PAo4Q2dMX9d_qaAmsF3a8lJcwLBX63SYBISmMFEacsKhlEWgFVG4tZmTBt16b9a_XOyUJEoTeXtgEy6yUb4QCdX1_q5_cXfi8uClyGMzOlCfFo7KFclrhwT0jSeL3MqJKnkO6DWLsdGinZXN6-gyl6vEc8mPztyWEOQgg598aC9p9fh1DBERT7rqSNTyzZuBhP7-1Qqp5ckEug4AOj0XPrGq-zoKCyaSvdTyzoJ5WSaObipBPX0hIsbUCQpm1HQqmgw8EQaeKMD4feyIhhESrHHJe6DhZRCuPk3Qsh7BRSnKP7_5Bc7kxNXHT6meBwI9loXHhV8uOe-lfLHGGg8Vc6HROP-zz091RqdtsOlKlYEe5h3JyBj7i2JWnl5UJi-S-_IHzGi_klcwwN4DGDFojlav8j-fKjx37bavgv_Msvcp9XyppfwMkgxV_9Nq-Xg0dyUK376Hd0b0UVEH0P3IE2iQodTvlqswPtmaz6mAoqreg4DwZ_8evB0rKSJTKXSNE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاهد لغنائم القوات المسلحة اليمنية من مرتزقة السعودية بعد فرارهم</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/naya_foriraq/90293" target="_blank">📅 12:51 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90292">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالإعلام الحربي</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SOfQs-xX7o41nb8X3o1P_5XGcL_QEjMSC4Sfi6eT2aSUrcVf_Tr3bcD9Kgs8R1Ze68JDakP8K1VW4sIc4Ek2kWeEb1Ro6NWxmwvTwp0z3dIUtcWueTpkZV98e_xnVXY2bwf3yXuvN4HL29MntYFSGOuWN9FwFygDu_nkuAQbR-cA0a4miHN43jmOE64UWpwFbvW8akr-3dzlajtvBN043-R9D7gJOZ4haG7BLFabfN7amIbJNDwSZRAZoSsliPkkkfYfHhmrOET7QKz8TBUPvDPxauGrUz8fvmWZwdlmt-BxsafkokkWx9Lv5us1VHfikKFn781XKiUsWl4X0wThCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بسم الله الرحمن الرحيم
​في الوقت الذي نبارك فيه للشعب اليمني الأبي انتصاراته الميدانية المتواصلة ضد القوات السعودية ومرتزقتها، نؤكد: أن الاتهامات الموجهة للمقاومة العراقية بشأن استهداف المنشآت الحيوية السعودية يوم الجمعة الماضي هي (شرفٌ لا ندّعيه)؛ ونُعرب في الوقت ذاته عن استغرابنا من تسرّع الحكومة العراقية في تبنّي هذه المزاعم دون الاستناد إلى أدلة موثوقة أو تحقيقات ملموسة.
​إن تكرار سياسة إلقاء التهم وصرف الأنظار لا يعدو كونه محاولة فاشلة للتغطية على الهزائم المتلاحقة التي تتكبدها القوات السعودية وأدواتها على أيدي أبناء اليمن الأباة.
​وإذ نجدّد تأكيدنا على الموقف الثابت للمقاومة العراقية في مساندة الشعب اليمني المظلوم والمحاصر من قبل النظام السعودي منذ أكثر من عقد، فإننا نحذّر من الانجرار خلف المخططات الصهيو-أمريكية الخبيثة التي تسعى لزجّ العراق في أزمات لا تخدم إلا أعداءه.
​وختاما، نُعلن استعدادنا  للمشاركة في أي لجنة تحقيق حكومية بقصد  الوقوف على الحقيقة، بدلاً من الانسياق وراء الروايات المشبوهة.
المقاومة الإسلامية في العراق
12 أيلول2026</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/naya_foriraq/90292" target="_blank">📅 12:46 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90291">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/97ae1f3afd.mp4?token=jDmQOKgno-koiuFugfuK8UiIJfOUReUp0WmU4KLZWHpXuC5wbOG2CecjsYNUp7Bx7617OdT3Xij3or9gK4V--SeAlVbzUxl3khsowYpn8FEIV4fhyE2zU4w6rETGg0wtTwbDlRcId8Lttw6T_pGK7L_EQf4L23HbMl9UhAgDxLNDpuScFDoTKUi6ZQaPcfD7U55whyF15jJqFUD46c93vc9c1SJM-6XutuzKwpJ023XBWz3RPGSCHL0U411hSCy7bYUEdwfFrRQ-YTvw9sj_jHdBvReC1kevo5H5BaaDBsoqk60ncYnfIJhE-Fhd8gkjSHV0nCwTrulORF2LfkZGdHJmmQp1OAiWvZLwb2T1YQVUEVwHrkuBoO3UcGbCoUJAKUVLIQ3bjobwSfproms3QlXCA-AOSh5rggGhYtpW3wueSnK1ZLG8YOUhkNl8mVdOGebr6Jq01LBJ_Hmc_Svl0KmxmrOmiIUT-jthK-MoVEeU1h-fe6vJBdGaXDUbiOGqmRzhUf3NUf9XvwvKXmfdIH3bHPkWw6mh6EuaAGwlvESIgaEY6ltGlL7_ho86rm4LEVgWLPxlaGa0X-HSXABfPwmbZDi3rTg4vuIDt7-tyftoiDzYKHq2ZZif7Ac4pwZDcYY2QZNgcJ-JCVVvkQWkC23Sa5_jPKpHhR2jforDx0M" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/97ae1f3afd.mp4?token=jDmQOKgno-koiuFugfuK8UiIJfOUReUp0WmU4KLZWHpXuC5wbOG2CecjsYNUp7Bx7617OdT3Xij3or9gK4V--SeAlVbzUxl3khsowYpn8FEIV4fhyE2zU4w6rETGg0wtTwbDlRcId8Lttw6T_pGK7L_EQf4L23HbMl9UhAgDxLNDpuScFDoTKUi6ZQaPcfD7U55whyF15jJqFUD46c93vc9c1SJM-6XutuzKwpJ023XBWz3RPGSCHL0U411hSCy7bYUEdwfFrRQ-YTvw9sj_jHdBvReC1kevo5H5BaaDBsoqk60ncYnfIJhE-Fhd8gkjSHV0nCwTrulORF2LfkZGdHJmmQp1OAiWvZLwb2T1YQVUEVwHrkuBoO3UcGbCoUJAKUVLIQ3bjobwSfproms3QlXCA-AOSh5rggGhYtpW3wueSnK1ZLG8YOUhkNl8mVdOGebr6Jq01LBJ_Hmc_Svl0KmxmrOmiIUT-jthK-MoVEeU1h-fe6vJBdGaXDUbiOGqmRzhUf3NUf9XvwvKXmfdIH3bHPkWw6mh6EuaAGwlvESIgaEY6ltGlL7_ho86rm4LEVgWLPxlaGa0X-HSXABfPwmbZDi3rTg4vuIDt7-tyftoiDzYKHq2ZZif7Ac4pwZDcYY2QZNgcJ-JCVVvkQWkC23Sa5_jPKpHhR2jforDx0M" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
مشاهد من محافظة الانبار..
ازمة الوقود مستمرة في مختلف المحافظات العراقية.</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/naya_foriraq/90291" target="_blank">📅 12:38 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90290">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🇨🇳
🇺🇸
ترامب بشأن الرئيس الصيني: «يقول البعض إنه يتجسس علينا، لكننا نتجسس عليه أيضًا، ونحن جيدون في ذلك كذلك. نحن على علاقة جيدة. حقيقة أننا ننسجم معًا أمر جيد. نحن نتعامل بشكل جيد مع الصين الآن.»</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/naya_foriraq/90290" target="_blank">📅 12:30 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90289">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9397297397.mp4?token=vWGX4Pjakk5PPFRr7cxCE1tZYJSlYJB71UsjFdj--fExTcfXp7Iy8Hdar2Fz5U8Xq6CzjOOp6eHOdbe6k4nDFTmZTbKpMAK6kv90CTh8H3Zc-UhEQA-tOhIR_HDofo0W4--ZQFLaR7wnNg29p7Yno4jiwU1QWF4_N__6UIsQrRTJDNns77rkkMREgmm9iKbf1B8ctimUlEFyTp-xcDn9_nlpn66dUAtADR_vYnEjEF5zXDIxRzu2kTxJgGTz2RoS0PChkb7F3jLqvWTZgU29kinnAmYmU4XIaMMPFQ2Sai-jdAHA4Xxjakn3lDHYl9IUYVixs_0MvI5P_fOS5Ncycg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9397297397.mp4?token=vWGX4Pjakk5PPFRr7cxCE1tZYJSlYJB71UsjFdj--fExTcfXp7Iy8Hdar2Fz5U8Xq6CzjOOp6eHOdbe6k4nDFTmZTbKpMAK6kv90CTh8H3Zc-UhEQA-tOhIR_HDofo0W4--ZQFLaR7wnNg29p7Yno4jiwU1QWF4_N__6UIsQrRTJDNns77rkkMREgmm9iKbf1B8ctimUlEFyTp-xcDn9_nlpn66dUAtADR_vYnEjEF5zXDIxRzu2kTxJgGTz2RoS0PChkb7F3jLqvWTZgU29kinnAmYmU4XIaMMPFQ2Sai-jdAHA4Xxjakn3lDHYl9IUYVixs_0MvI5P_fOS5Ncycg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇨🇳
🇺🇸
ترامب بشأن الرئيس الصيني:
«يقول البعض إنه يتجسس علينا، لكننا نتجسس عليه أيضًا، ونحن جيدون في ذلك كذلك. نحن على علاقة جيدة.
حقيقة أننا ننسجم معًا أمر جيد. نحن نتعامل بشكل جيد مع الصين الآن.»</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/naya_foriraq/90289" target="_blank">📅 12:26 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90288">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🇮🇶
مديرية شؤون المخدرات العراقية تعلن ضبط 150 كغم من المواد المخدرة وضبط 3 متهمين بينهم أجنبي بعملية أمنية في مياه الخليج الفارسي.</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/naya_foriraq/90288" target="_blank">📅 12:23 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90287">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🇮🇶
رئيس وزراء العراق يعفي قائد عمليات ميسان من منصبه، على خلفية ثبوت انطلاق الاعتداءات التي طالت المملكة العربية السعودية من أحد المواقع داخل المحافظة.</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/naya_foriraq/90287" target="_blank">📅 12:06 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90286">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sm8fHALHNkTsbKnBJ-1g2EUFkY5Qhm-ZOKhXeEvOSaxsH7kQEOxiEkZJuQUU_PikxPp_gVQj6RzLSo9fok0mGcy6YHfCLCXF55JGFTFaWSNgaFFTo3-zIrr6j639drZhIvCZ3-m5O_Z6H2Rr0qPW-VPbLQewLnLYUmrXksM5LJBsSIGDIPGsoLQBK5l2X9Fn5qM2HxTrfwM4C4A93rd96NunlU76yyzx_CZHMQzkk1Ky9M2kLtimmYrbhfY1YZdVEV5qMzRBKrdv4KFaQO3UYZtuthn8GALDP37brQTdkk8sceUGIgwJGB-sCPWL1-m37kFo_zS9AEX62R4sGb1GLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
طائرات النقل العسكري الاميركية تتوالى في الهبوط بمحافظة اربيل شمالي العراق.</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/naya_foriraq/90286" target="_blank">📅 11:42 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90285">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🇮🇷
مصدر ايراني...
انفجار مسيطر عليه في محافظة اصفهان.</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/naya_foriraq/90285" target="_blank">📅 11:39 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90283">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dDgtJwqORc5US0wlams33i9U-UZhuzFRc-A5OSMrWjQ_AOTetArmeY8Xh7MXPHD9Jl9oF5jFWsQczzNRXdeoF6ntYMOyxtqHMGU0P7ZXZIHb75t2y7NIOkAFPxaaoWLkWe1EfuQ-5X0DZEWYjIQklXRcP_Z0_ub6IjhNKdJdf9qad3jPmLdYsJWiCIQ5vtD75Vtvdxh_d3qzJnUHDoSCe0CuIQdP4ZOwR65NbIA5n-HE5OXoWvYwK40-anheewG055hYv_3Umy_cd4YI6qguyWB_ma9qjiq9GOFYMBICojTFE_K_ktg7K7C6WLlEZynAzlsWD89pQwz36wcBRhQOKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eGWYSnFnSDpGdlXn6nVxM5BCiL8_iMFEjBw8NWtpbe9-Xz2ZwHCfBCr6R5ZzIeEdhzpOcoEQq-GdoqAIz766ncaIUA1T_W7eIXMqGTTVSWHMTVlD6UTfsnbH7-CsQqjBfPKd01NPFjOns0nICM5N_L9F5kj130oLY-cgO41faQJ5Cul9CE2R0vS1JKOEGJfAemKPvfoyBRgG05bsSMRqHFh7j5n04Z2u8cq5nudjWDP-dQooMexUac5Y2mdMi-XMrZKmCbHT1NbfuN5GCX-6DfZ-e4P4DRp2LvnA-zPhSPW27WP075YDSdpTJY--8FJxa1li0FBb0U1emr2DNd9h7A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇾🇪
🇸🇦
لليوم الثالث على التوالي...
استمرار اندلاع الحرائق في حقل خريص النفطي التابع لارامكو في السعودية بعد استهدافه من قبل القوات المسلحة اليمنية.</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/naya_foriraq/90283" target="_blank">📅 11:16 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90282">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eIYSakHpq7vE83DnFzeIAnRhJel7SFeMIiUJCuIm5PTS3CKaXPrKRS0E0Wrlg-wC8M2lVvwS3_-uc-8UO1iNDVEPrzFR9wezamptNfH-PdwAdLduJQNJyIRTIFLSAXP8WwU4XYPsWC7CWEsnMvAV3K02dQyxjImv74mluHUXuU3m34o_aOoyW1-OPdjJPDWekm6AwoFMwGCsSHHXb5nL7cXT3QZ7Wy2o8_YXNs6pI5UbdLcWN3dg8DN2g18CpIsvsy1yr7ZXdQ4_vo3Mls4S-MSwZg-fGbjbrSoqh5-iKfSeunx3W0u3_O3QoPljhoRMnvrD0UK95abchCz_JSdRsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
السيد مقتدى الصدر:
بسمه تعالى
لا يستفزنكم القوم
فهم يريدون تغطية سوءتهم بفتنتكم
فلا تكونوا عوناً للفاسدين ولمن يريد النيل من سلامة العراق العظيم
وحافظوا على وحدتكم وعلى وطنكم.. واتركوهم في غيهم يعمهون.
نحن وانتم فوق ما يقولون والله فوقنا يحكم بالعدل والإحسان.. وهو يحكم بيننا وبينهم بالحق في الدين والدنيا والآخرة.</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/naya_foriraq/90282" target="_blank">📅 11:11 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90281">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D2A8pcNO6tldCujDtTIce61mbsnEyBFgpvM4EUfYvyx2FJi4Z-Ggg1DzjDhqPJ7lsr0h3BlECc9XzLq0_wv_edNWvHa9S4RkWLwjF76HuZcSS6q2qowQne-EfsK_e9J8_FnmOUn6MNj7oDvsUY8aDN236Rua5gj_TDBqBXIRSMBIqFuI36mUh08OGB17ugFCZGcgEmjOK-Vmlr_JaujeGrTYgm5MwajCUtoJISN_O2jf2T4ONxW3XuP1Bl8XvHgggKcDu-9OZX6OKuZETcc-3Gb4S1zeoSNejqEshxTKblGIydkg88WEQa7lcVHbBe_fdoocrPUCp8Kqlody2PHZVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الأردن يدين استهداف الفصائل العراقية حسب ادعائهم للسعودية</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/naya_foriraq/90281" target="_blank">📅 11:08 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90280">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">طيران مسير أمريكي مكثف في بادية السماوة جنوبي العراق</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/naya_foriraq/90280" target="_blank">📅 10:31 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90279">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🇮🇶
الإعلام الأمني العراقي:
اتخاذ سلسلة من الإجراءات القانونية اللازمة وتكثيف العمل الاستخباري والتحقيق والتدقيق لمعرفة ملابسات الخروقات والمخالفات التي حصلت في هذه المنافذ ووضع الحلول والمعالجات المناسبة لها.</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/naya_foriraq/90279" target="_blank">📅 10:29 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90278">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🇷🇺
بوتين
: نشر قوات أوروبية في أوكرانيا سيعني دخول هذه الدول في حرب مع روسيا.</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/naya_foriraq/90278" target="_blank">📅 10:07 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90277">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c984e675ec.mp4?token=Ft7GdvtSIhsPPPyv4hIgBvjjg80iLZwjW8uU5LUqHlQ69Zdi26_K_4VcwfF_wTEdopgN2Om-QRhQKTM65easWnhyMyiMwn31Z2c9JlaEgnNnMRoAQAKTChccg5DWnHEhY9NwEiFNAhiwTBJ1Tv9vaICDd9YfrYknkzxpl1bRfYRrHO-9kGgLw_L94yd2ttTGbURJO8PJpmnO6iET5ZmbZvljKzApbdVU6AdN1Q6OhgfpcSReyvxD78eX000SYQhWZQ_5JlQtqzBNudcNy31YudLGCn0rcimJIABhi0WeO25yUdesOZ5m7U5e5KzGUEir2pT7_eDVsHx-ZJxUurN4Rg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c984e675ec.mp4?token=Ft7GdvtSIhsPPPyv4hIgBvjjg80iLZwjW8uU5LUqHlQ69Zdi26_K_4VcwfF_wTEdopgN2Om-QRhQKTM65easWnhyMyiMwn31Z2c9JlaEgnNnMRoAQAKTChccg5DWnHEhY9NwEiFNAhiwTBJ1Tv9vaICDd9YfrYknkzxpl1bRfYRrHO-9kGgLw_L94yd2ttTGbURJO8PJpmnO6iET5ZmbZvljKzApbdVU6AdN1Q6OhgfpcSReyvxD78eX000SYQhWZQ_5JlQtqzBNudcNy31YudLGCn0rcimJIABhi0WeO25yUdesOZ5m7U5e5KzGUEir2pT7_eDVsHx-ZJxUurN4Rg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
استمرار إستهداف العناصر الإرهابية التي تكمن في إحدى مناطق مدينة سراوان من قبل القوات الأمنية الإيرانية.</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/naya_foriraq/90277" target="_blank">📅 09:08 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90276">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🇮🇷
حاكم مدينة مهران الإيرانية:
معبر مهران مفتوح، والأنشطة المتعلقة بالسفر والجمارك مستمرة فيه، ولا يوجد أي إغلاق أو توقف في عمل المعبر مع العراق.
خلال الـ 24 ساعة الماضية، عبر هذا المنفذ 17 ألف شخص، مما يدل على استمرار عمل قسم السفر في منفذ مهران.
الجمارك في مهران تعمل كالمعتاد، ولا توجد أي مشاكل في عملية تصدير البضائع.</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/naya_foriraq/90276" target="_blank">📅 09:02 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90275">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7eb9c722a5.mp4?token=q-MEpUACI_guckuvWHj9pXT-E8v8uk9_f9Rr9Cl8n9YcIvMGUtH45uJDAC51MICAvk3NtHX1XjF7vg0kR_LaZlToEqqgpTL0JuM3qBRXey6i4txmLsEwGbyYN40_BfVjycZMKU5u2zQMxCED2_MZ2bEOLypcarXsbr3xYSw8RA00gSLsPuUEbyLwwGBK4H0sWd5nih5QSALO35zLtuc1_AJ2F9BCgykL3-R5W2jLkX5_rnPRpnc-E3_gZxGscqId7xE53dG0fLRCufnf9R-9ssCiqNDKthJ8reqnEdXgcAosnaBC0ZKhBNhIi6kx9Wz4yRlU0JKz6LTxtSUJNEwxroWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7eb9c722a5.mp4?token=q-MEpUACI_guckuvWHj9pXT-E8v8uk9_f9Rr9Cl8n9YcIvMGUtH45uJDAC51MICAvk3NtHX1XjF7vg0kR_LaZlToEqqgpTL0JuM3qBRXey6i4txmLsEwGbyYN40_BfVjycZMKU5u2zQMxCED2_MZ2bEOLypcarXsbr3xYSw8RA00gSLsPuUEbyLwwGBK4H0sWd5nih5QSALO35zLtuc1_AJ2F9BCgykL3-R5W2jLkX5_rnPRpnc-E3_gZxGscqId7xE53dG0fLRCufnf9R-9ssCiqNDKthJ8reqnEdXgcAosnaBC0ZKhBNhIi6kx9Wz4yRlU0JKz6LTxtSUJNEwxroWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
نائب محافظ خوزستان الإيرانية: وفقًا لإعلان السلطات العراقية، تم إغلاق حدود الشلامچة والشيب في محافظة خوزستان اعتبارًا من صباح اليوم وحتى إشعار آخر، ولا يتم حاليًا أي حركة بضائع أو مسافرين عبر هذه الحدود.</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/naya_foriraq/90275" target="_blank">📅 08:54 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90273">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tF9R7OxNVV97Ayln0TgY91BZNeYUqkvM1D9Kpnoe-ermH1HXZLTC7MoPeX-vhtEJsCpTuy4ChlZ5RvLsJbnFnlz15-A13vns7mNFc0he4JL2hjwRCL_clyKEydGnR5_FSs0w-Owv1i1vS96sdI2hLaIR_4bHFqnx3G21M2Xf0TxJ1JnHJDhwviMeWgLTzF5FMOY3bZI5lA8XaN4e4hK4n9i7_LIuKT7gMhxUrbNXucw0EehBifKFLnwD9laUnZ633CwzSHqTYctTw1Hl2RJafnK9hQzpoRVjkABSg2r9xVvcsaNNH9zFHeld0FljNioqoJHDlQ7RZ14UzylM3Xi9og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9a79629eb3.mp4?token=PrpS3557cZSGejb3myP8GAlSwQa-CeYnId9O1OJojBcUKFeeeIzJeFCMlaXVvqkPLKaKZ7miBgeH_LTLYoHGtwVZIww5YYg685mOVuhq1efSnH8yt3w0EgiRSrCdxA54Ix58SvWUZcJ7p-gGGYOQ3XB6oqJ1U9OtqVGPCMi2k96M4lhLheDvoH832BUWnpm19Z8ga8qtIcYQF-70eit24bQc_eA69QJYt1NvvtI1-2rb_5iH58PYNwievMnUDOxlqWV8qRyKhoaqVh7e7_KNl9_zASr_jtZXFnyU6_7zGXQ9U_aLKkDOG5JMDybWNNP7q8dwlmhkM1WvnZOYalbtUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9a79629eb3.mp4?token=PrpS3557cZSGejb3myP8GAlSwQa-CeYnId9O1OJojBcUKFeeeIzJeFCMlaXVvqkPLKaKZ7miBgeH_LTLYoHGtwVZIww5YYg685mOVuhq1efSnH8yt3w0EgiRSrCdxA54Ix58SvWUZcJ7p-gGGYOQ3XB6oqJ1U9OtqVGPCMi2k96M4lhLheDvoH832BUWnpm19Z8ga8qtIcYQF-70eit24bQc_eA69QJYt1NvvtI1-2rb_5iH58PYNwievMnUDOxlqWV8qRyKhoaqVh7e7_KNl9_zASr_jtZXFnyU6_7zGXQ9U_aLKkDOG5JMDybWNNP7q8dwlmhkM1WvnZOYalbtUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
🇮🇷
منفذ مهران الحدودي مازال مفتوحا أمام الجميع وحركة دخول وخروج المسافرين تسير بشكل طبيعي.</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/naya_foriraq/90273" target="_blank">📅 08:49 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90272">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6bfc5f64ec.mp4?token=CLichoYEy5k7JzTYeeb_Rs39ot_beZTuqXhH7bH8hVVU9Oo5BE4VTiXskP5Pqe-b45Pb5FlEoO34cH0xN8THMDR4Y-fPiyBISiJ6s1G3PySsnWICwTxMdJK3jw51hL0ahuFOqSkCQRzQ9HUoQZnTaKY-cRiB2oc5HyDaN_ukON_ZFIoJSr8HnQzb7iiVWKCNuekgxTpIm391idmkUoNB_x7dUzAekKWKMUq8pxMlJMDmI6-Lmc7WzpZEes__dBZRR545EvYZHEVWD2hXSin3pqvzDPK6ewNDhbskH7UWgnKK8VXedXJ73nYwPB4cI_xdmMSeRq60Rb3jJs3eFQUwMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6bfc5f64ec.mp4?token=CLichoYEy5k7JzTYeeb_Rs39ot_beZTuqXhH7bH8hVVU9Oo5BE4VTiXskP5Pqe-b45Pb5FlEoO34cH0xN8THMDR4Y-fPiyBISiJ6s1G3PySsnWICwTxMdJK3jw51hL0ahuFOqSkCQRzQ9HUoQZnTaKY-cRiB2oc5HyDaN_ukON_ZFIoJSr8HnQzb7iiVWKCNuekgxTpIm391idmkUoNB_x7dUzAekKWKMUq8pxMlJMDmI6-Lmc7WzpZEes__dBZRR545EvYZHEVWD2hXSin3pqvzDPK6ewNDhbskH7UWgnKK8VXedXJ73nYwPB4cI_xdmMSeRq60Rb3jJs3eFQUwMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
نائب محافظ بلوشستان: إن المجموعات المعادية لنظام الجمهورية الإسلامية الإيرانية، والتي كانت تسعى إلى زعزعة الأمن العام وتنفيذ أعمال تخريبية وإرهابية، قد تجمعت في منطقة من مدينة سراوان، حيث تمكنت القوات الأمنية، بفضل المعلومات الاستخباراتية والدقة، من مفاجأتهم…</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/naya_foriraq/90272" target="_blank">📅 08:05 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90271">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🇮🇷
نائب محافظ بلوشستان:
إن المجموعات المعادية لنظام الجمهورية الإسلامية الإيرانية، والتي كانت تسعى إلى زعزعة الأمن العام وتنفيذ أعمال تخريبية وإرهابية، قد تجمعت في منطقة من مدينة سراوان، حيث تمكنت القوات الأمنية، بفضل المعلومات الاستخباراتية والدقة، من مفاجأتهم وإلحاق ضربة قوية بهم.</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/naya_foriraq/90271" target="_blank">📅 07:56 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90270">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🇮🇶
مصدر لنايا: توجيه فوري وصل للبصرة الان من القيادة العامة للقوات المسلحة يقضي بغلق منفذ الشلامجة المتآخم لايران بشكل نهائي من الان والى إشعار اخر. الإغلاق يشمل المسافرين والبضائع.</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/naya_foriraq/90270" target="_blank">📅 07:39 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90267">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa850a0397.mp4?token=n6N822KpzKpyvrwiOzW22BQykWUUxT9FtyB0A9Y24nCgz0X8V-uG538tnKq9N_CQWf7hgH8HEuASi4zMGajV01e-vTcAJCzO2R7iTBzfzdiCQaiG67Btc_uMXBQrhL36GChQYPTHT-WQ0WPTQMERKYVILaKGQPy5PCmf4I9A32KdLk8vVSpCvq9iGDtqpTx-ITVp3jytiZhmrKTKbS4BUIBXoXR_iGH7X6vL-qDxDjZbSq9NKP1v_vmcN4ojNTIIWayXU0y-bzXEPBo7s-6sxqaitrA6pBizU8snRyd4007LpCla9LpDmj_OxAcz1o83g8ehQEhoJDXN5qqUl-hqtQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa850a0397.mp4?token=n6N822KpzKpyvrwiOzW22BQykWUUxT9FtyB0A9Y24nCgz0X8V-uG538tnKq9N_CQWf7hgH8HEuASi4zMGajV01e-vTcAJCzO2R7iTBzfzdiCQaiG67Btc_uMXBQrhL36GChQYPTHT-WQ0WPTQMERKYVILaKGQPy5PCmf4I9A32KdLk8vVSpCvq9iGDtqpTx-ITVp3jytiZhmrKTKbS4BUIBXoXR_iGH7X6vL-qDxDjZbSq9NKP1v_vmcN4ojNTIIWayXU0y-bzXEPBo7s-6sxqaitrA6pBizU8snRyd4007LpCla9LpDmj_OxAcz1o83g8ehQEhoJDXN5qqUl-hqtQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
استمرار الإشتباكات بين الأمن الإيراني ومجاميع إرهابية في سراوان بمحافظة بلوشستان.</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/naya_foriraq/90267" target="_blank">📅 07:01 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90265">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0e64b1fb2b.mp4?token=Z1s32JAJSmOu-AjC4feY_3wNVhjdNmgD86qjIaaX3wf-PEkZ4XFLdDT3_Y4MYar_T1Uq6b2aPlx4qYD8wj-uOV8BqHFwICP1gg7UkE-EYN1dk88W9eEaRCp0LsKsq5wfFoXtRZ3PwdxgAl2td3PGCGeKeJSsnA59LBfNwOFYcbpZXnO7U6PKPQ7m45wvsH1oMfj_1pzKM20oauDkP52yMcLsnvq7-xreyL6pVMA0_W050y7PzhYzJC_tIFdwAgzVZPS0Oz_WuIGl6g_smleVoyfCyVumaBvLLrMiv__TKCzyEkuGSsga1aIpssQbE14FFldgG6XwQq6R2Cei0ivVcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0e64b1fb2b.mp4?token=Z1s32JAJSmOu-AjC4feY_3wNVhjdNmgD86qjIaaX3wf-PEkZ4XFLdDT3_Y4MYar_T1Uq6b2aPlx4qYD8wj-uOV8BqHFwICP1gg7UkE-EYN1dk88W9eEaRCp0LsKsq5wfFoXtRZ3PwdxgAl2td3PGCGeKeJSsnA59LBfNwOFYcbpZXnO7U6PKPQ7m45wvsH1oMfj_1pzKM20oauDkP52yMcLsnvq7-xreyL6pVMA0_W050y7PzhYzJC_tIFdwAgzVZPS0Oz_WuIGl6g_smleVoyfCyVumaBvLLrMiv__TKCzyEkuGSsga1aIpssQbE14FFldgG6XwQq6R2Cei0ivVcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
تعزيزات إضافية للقوات الأمنية الإيرانية تصل إلى مكان الإشتباكات في سراوان جنوب شرق البلاد.</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/naya_foriraq/90265" target="_blank">📅 06:57 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90264">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f85ebf565a.mp4?token=Y2kwKIsxwlwVvmPe0o-NQty0nXE3BqfoJux6jTBE1PfYLAHK7tdMmBXz4rJ7PzgiLvv3ogAOC_8QsGkkoMVGKsM-ofQdQGi4ka2WklVX9b_XILejZYYoFusxiWeLtcOjeEvZEixny1HeaM8JntU08qLL60RuQ00JVnlt9MrvHr44YyFPaQ4HwY4WuKqYfwF9OerBcPj5GCLS9bvpJzgqotQEJwufdHdDN7K7KffDkR5YlZL8Rl-mJO4xs5fQYiNLeshzwWFH0Dxy_fEn8NVEuLIv_msw8A6rlYzJKZmrfmqeFFp0legqEnWWiatzii9i_XQnArsl8yFmzywCNmYZmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f85ebf565a.mp4?token=Y2kwKIsxwlwVvmPe0o-NQty0nXE3BqfoJux6jTBE1PfYLAHK7tdMmBXz4rJ7PzgiLvv3ogAOC_8QsGkkoMVGKsM-ofQdQGi4ka2WklVX9b_XILejZYYoFusxiWeLtcOjeEvZEixny1HeaM8JntU08qLL60RuQ00JVnlt9MrvHr44YyFPaQ4HwY4WuKqYfwF9OerBcPj5GCLS9bvpJzgqotQEJwufdHdDN7K7KffDkR5YlZL8Rl-mJO4xs5fQYiNLeshzwWFH0Dxy_fEn8NVEuLIv_msw8A6rlYzJKZmrfmqeFFp0legqEnWWiatzii9i_XQnArsl8yFmzywCNmYZmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
تعزيزات إضافية للقوات الأمنية الإيرانية تصل إلى مكان الإشتباكات في سراوان جنوب شرق البلاد.</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/naya_foriraq/90264" target="_blank">📅 06:47 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90260">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/839ea30161.mp4?token=eJPvpRfad0aqUkUGohf2bOEsTKzeGBQH107L8gm6-FD1JXTec_-rLTcAQ-QE2fKCpk1lGuW7aKgMqSWcdHYr09y8FLbuZR-BVB0Qpvmx-LQ49JhzOmyAVxH0U2wS4jcUPETgJe4TmRWa9z51KvXgvSZqfTGUtXtvjoxObGBTfwcR4BUDt0iCfWuvgFS4G22o1VVmaeXuCCFiBk-JZ7A2OEQLnLEC2iCdmlEqRZtT8QqGbZkBsKz5yZ6XQGNYvXlTZvt0zGe6IzLKvWWR3HSVDQQzOcthMdvhMT3c3U6J4nBNxxMpYPIV8PoRjAd6Lj9atb5E0ipwHHQxZmyR1_ATrw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/839ea30161.mp4?token=eJPvpRfad0aqUkUGohf2bOEsTKzeGBQH107L8gm6-FD1JXTec_-rLTcAQ-QE2fKCpk1lGuW7aKgMqSWcdHYr09y8FLbuZR-BVB0Qpvmx-LQ49JhzOmyAVxH0U2wS4jcUPETgJe4TmRWa9z51KvXgvSZqfTGUtXtvjoxObGBTfwcR4BUDt0iCfWuvgFS4G22o1VVmaeXuCCFiBk-JZ7A2OEQLnLEC2iCdmlEqRZtT8QqGbZkBsKz5yZ6XQGNYvXlTZvt0zGe6IzLKvWWR3HSVDQQzOcthMdvhMT3c3U6J4nBNxxMpYPIV8PoRjAd6Lj9atb5E0ipwHHQxZmyR1_ATrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
مشاهد أخرى من الإشتباكات العنيفة التي تدور بين القوات الأمنية ومجاميع إرهابية في مدينة سراوان بمحافظة بلوشستان الإيرانية.</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/naya_foriraq/90260" target="_blank">📅 06:38 · 21 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
