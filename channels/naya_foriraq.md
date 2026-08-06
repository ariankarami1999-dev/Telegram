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
<img src="https://cdn4.telesco.pe/file/bpdICK3Vn72c9XrO51ro5gZI_SDxzBcsvfIsb_aZsNM1pJkXoZa_Zuma_NzyfF_dfaGlQuLSQOJUY3EHR_RSECY43tjUM53j0Z5Tt6Y3A65AvIbLPgGuYenmJCj7HKW03B3rK_CqVLeCZcgu-JjDjxFE9JvZ8LgYrEdsjPwYzTsWVDWZvOlvste4zMe76-iDXGwB3G2S8BPKLVlhINi9O6e-9xdWzUqtwEVoOJOQXnZioYjilJfR4EovTphuIalVAs-lEjkwu-M98weAi_y_XodsRhGnbePNI7kCmKjIFzb98ZH85vT92rZbolRW-ait7B8SeHjr5PeWYR3Latix4Q.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 273K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-15 15:56:08</div>
<hr>

<div class="tg-post" id="msg-87111">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d6675bcd19.mp4?token=IGITscJuyaoezYLInIhQudA2KfgJT0HaAtccsTKcxDiGT941OeCTuIOTs-RHiJ6FBGh0DE-lv9tzYzCNY_zFWNiQEPgJah5McZd3k-CznSbbUq8wmky27Kt5s5K0tKKPoKuOQhy60VcVpjonD94F_qEBotcGGFg1-kkiN8MgV3kukAmmCEHkTV8cUaJvCk-fI6ZhuoH_FRs4TTIGe4u8nmkPsHAgJWkgV4uDP_rWQ-51sdZBke8EzwCq_08J4bvP6DhTIYjizRtAXSqTORr98CSGHAEzilon8wHUihPdsYC3_2HfNLxmB0aU_qwEbNyXnxyOwxvInmwNQ68H1ZtpMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d6675bcd19.mp4?token=IGITscJuyaoezYLInIhQudA2KfgJT0HaAtccsTKcxDiGT941OeCTuIOTs-RHiJ6FBGh0DE-lv9tzYzCNY_zFWNiQEPgJah5McZd3k-CznSbbUq8wmky27Kt5s5K0tKKPoKuOQhy60VcVpjonD94F_qEBotcGGFg1-kkiN8MgV3kukAmmCEHkTV8cUaJvCk-fI6ZhuoH_FRs4TTIGe4u8nmkPsHAgJWkgV4uDP_rWQ-51sdZBke8EzwCq_08J4bvP6DhTIYjizRtAXSqTORr98CSGHAEzilon8wHUihPdsYC3_2HfNLxmB0aU_qwEbNyXnxyOwxvInmwNQ68H1ZtpMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏رويترز عن مصادر يمنية: 30 قتيلا على الأقل في استهداف حوثي لمواقع مرتزقة السعودية بحضرموت ومأرب</div>
<div class="tg-footer">👁️ 1.28K · <a href="https://t.me/naya_foriraq/87111" target="_blank">📅 15:52 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87110">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🇾🇪
بيان مرتقب للقوات المسلحة اليمنية للإعلان عن عملية عسكرية واسعة ونوعية.</div>
<div class="tg-footer">👁️ 3.63K · <a href="https://t.me/naya_foriraq/87110" target="_blank">📅 15:38 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87109">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🇾🇪
انصار الله في اليمن يطلقون 8 صواريخ بالستية باتجاه معكسرات مرتزقة الفرقة الأولى التابعة للسعودية.</div>
<div class="tg-footer">👁️ 4.61K · <a href="https://t.me/naya_foriraq/87109" target="_blank">📅 15:34 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87108">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qtbL5-QkU52XDUvM3USNFwPip5d3YVDlrgiqMlbJ3Soef1oxMnOxvD9YByAIMGP0hwe5FgQnLQBGKpGWkQQICk5tM9FQcL1saQaHglGV1ca4f7C2A-nitmzyL35AiRJzmNDCK_oKNkuRAoipzo8ZkCbE45PNlXYFjdnF6LqWoY_AjNJrh4oB0-co7H101Z7yc7beUFP2WxfkmDLwoCcxa-9y2hLJDUl44zgIHITtEVATLWW_D4aA-FFTDODA8-9JEzgTlMgcFN4Nsdn0Ec9EU9ZdHjpNet7EsjNh0pnrPeXKmnlG8lOWOkAc94kM-tlLNzY1-aMOxc4E9EJFar-wXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
وزير النقل العراقي يوجه بإعفاء مدير الشؤون البحرية ومديرة هيئة ميناء الفاو الكبير من منصبيهما في موانئ العراق.</div>
<div class="tg-footer">👁️ 4.83K · <a href="https://t.me/naya_foriraq/87108" target="_blank">📅 15:31 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87107">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">في اول رد كويتي مزلزل
🇰🇼
السلطات الكويتية تلغي ترخيص المدرسة الايرانية في الكويت.</div>
<div class="tg-footer">👁️ 5.23K · <a href="https://t.me/naya_foriraq/87107" target="_blank">📅 15:30 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87106">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z7OcZoY2mwIbDZOubfx4fXFQmVEPRvs3zwjJyWsVZ5wBk78zmQZJ2b4FZaEKQbu8mDd8iNCcxGNTWxjalXKTxc2zKGDjDK1T2qy50AdvbedrQGB1dcaXk7V3jbQgpT8O4-kWNZ4g_tJqbe1U6n2m86koD490wFeLALvustNv65r-uzB_7bzfPYVO_BraQZSYnX1jPXJkqe1UOQLOO0eAO3EVmgcqiaQjqOqRfNdkEiztdujHwTyCSB7puTYI9rEIgahNjmgFmManxf4ZQnAeKPAgwfzZL_LYsbb7VBnGjDA6yi-pwnIH3sMUP0WEvwGJ7bUDZxH-XfQummapI1Qshw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇷🇺
دميتري ميدفيديف:
من العار أن يتم تذكر القصف النووي لهيروشيما وناجازاكي مؤخرًا، ولم يذكر رئيس الوزراء الياباني أو أي مسؤول ياباني آخر ولو مرة واحدة من الذي قام بذلك. اليابان هي تابع للولايات المتحدة، وفي مرحلة ما، ستصبح دولة مارقة.</div>
<div class="tg-footer">👁️ 8.78K · <a href="https://t.me/naya_foriraq/87106" target="_blank">📅 14:43 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87105">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">السيناتور الامريكي برني ساندرز:
عندما كنت طفلاً، كانت المعركة ضد حرب فيتنام، التي قتلت 59 ألف أمريكي في الحرب، وأكثر من ذلك عندما عادوا إلى الوطن وناموا في شوارع هذا البلد. كانت تلك الحرب مبنية على كذبة.
الحرب في العراق، التي صوتت ضدها عندما كنت في الكونجرس، كانت مبنية على كذبة.
الحرب في إيران - "أوه، إيران ستمتلك سلاحًا نوويًا غدًا وستهاجم الولايات المتحدة" - مبنية على كذبة.</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/naya_foriraq/87105" target="_blank">📅 14:24 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87104">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🇮🇶
مديرية مخدرات محافظة الأنبار غربي العراق تُفكِّك شبكةً مكوَّنةً من 19 متهماً وتضبط 408 آلاف حبة كبتاجون</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/naya_foriraq/87104" target="_blank">📅 13:48 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87103">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🇹🇷
وزير الخارجية التركي هاكان فيدان:
بإذن الله، ستنتهي المفاوضات بين إيران وأمريكا اليوم بأخبار جيدة. يتم حاليًا مناقشة فترة مدتها 60 يومًا. إذا تم التوصل إلى اتفاق خلال هذه الفترة التي تبلغ 60 يومًا، فيمكن التوصل إلى اتفاق دائم بين الأطراف.</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/naya_foriraq/87103" target="_blank">📅 13:48 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87102">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/55c345b1d2.mp4?token=sjdqpHnQ_uD9VyPQx85VxhJNATiA08B47rK6lG2y4LfEzd_0yQLFRqkRlJ0eH-a-BfTCqSiffDs5nVXnBKjoiLrrez-KoDDheLrizRtsqq6R2sE7-a5_UFRWt3rsHRO6TcDehKGumWtLh-grcLaOMxKYojo6e1WqLq0kVr1N8F-vPklGxbWu4lhPOE1ZC85tGxKqEOPu_U88ktOfdoyodZuY-3S8CcMqVPwooLTHP1eCcMgX32K2jAZ579QXOGe3enk67g84NCxogz1IVQ3w0C60pVca2cgGDDIeDvv42_vUEdducSOcHoAGb2TTmEUuMUKCqE-I9n4dSaQMfDExVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/55c345b1d2.mp4?token=sjdqpHnQ_uD9VyPQx85VxhJNATiA08B47rK6lG2y4LfEzd_0yQLFRqkRlJ0eH-a-BfTCqSiffDs5nVXnBKjoiLrrez-KoDDheLrizRtsqq6R2sE7-a5_UFRWt3rsHRO6TcDehKGumWtLh-grcLaOMxKYojo6e1WqLq0kVr1N8F-vPklGxbWu4lhPOE1ZC85tGxKqEOPu_U88ktOfdoyodZuY-3S8CcMqVPwooLTHP1eCcMgX32K2jAZ579QXOGe3enk67g84NCxogz1IVQ3w0C60pVca2cgGDDIeDvv42_vUEdducSOcHoAGb2TTmEUuMUKCqE-I9n4dSaQMfDExVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇾🇪
انصار الله في اليمن يطلقون 8 صواريخ بالستية باتجاه معكسرات مرتزقة الفرقة الأولى التابعة للسعودية.</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/naya_foriraq/87102" target="_blank">📅 13:11 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87101">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🇸🇾
صحيفة لبنانية: الجولاني لا يريد دخول قوات سوريا إلى لبنان بشكل منفرد ويرى أن أي وجود عسكري أو أمني يجب أن يأتي ضمن إطار عربي  وجود طرف سوري منفرد في لبنان قد يعيد إلى الأذهان مرحلة الوجود السوري السابق، وهو أمر قد يواجه رفضاً من أطراف لبنانية ودولية</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/naya_foriraq/87101" target="_blank">📅 12:29 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87100">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🇸🇾
صحيفة لبنانية: الجولاني لا يريد دخول قوات سوريا إلى لبنان بشكل منفرد ويرى أن أي وجود عسكري أو أمني يجب أن يأتي ضمن إطار عربي
وجود طرف سوري منفرد في لبنان قد يعيد إلى الأذهان مرحلة الوجود السوري السابق، وهو أمر قد يواجه رفضاً من أطراف لبنانية ودولية</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/naya_foriraq/87100" target="_blank">📅 12:28 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87098">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🇰🇵
🇯🇵
توجيهات صادرة عن مكتب الدفاع الياباني للتعامل مع حادثة إطلاق صاروخ باليستي مشتبه به من قبل جمهورية كوريا الديمقراطية الشعبية</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/naya_foriraq/87098" target="_blank">📅 12:19 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87097">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LXjysYNPzI30jVTRsPSD6A0UJDIxtQdAts4BlYcjTBFSN00f_OC9IA6_7wusQmK5Vv5GnTJUmnxf55PpHPAFWrk69b0vxem_F84zu9T3wo2ymu9IH25cENw2wi4OlYrrzcgnaC3923m6hK5UvHXYYuRmxoaOEnC6oOy7PA4FBMIkz5W_o2lMawCldChHPSZgO9_xderXSDKFLPJ8oZa2KXjBqGcQJzCKVEx3XeiBwigbewj8KJ5xCpC1oWkSt3cVf7x-3YOSnYFin11xx8w_GrfYoITpEs1EP8cYAI9HjM2pGAyltNmhaDTtbvQJiXkI2baaUlgftKfPMdQi3bRLBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇰🇵
🇯🇵
توجيهات صادرة عن مكتب الدفاع الياباني للتعامل مع حادثة إطلاق صاروخ باليستي مشتبه به من قبل جمهورية كوريا الديمقراطية الشعبية</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/naya_foriraq/87097" target="_blank">📅 12:08 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87096">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">إعلام خليجي:  تفاهم بين طهران ومسقط على الخطوط العريضة لإعادة فتح هرمز.  اتفاق فتح هرمز لا يزال بحاجة لموافقة المجلس الأعلى للأمن القومي الإيراني  الإعلان عن اتفاق إعادة فتح مضيق هرمز قد يتم خلال أيام  السفن الداخلة إلى هرمز ستستخدم الممر الملاحي الأقرب إلى…</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/naya_foriraq/87096" target="_blank">📅 12:06 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87095">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">إعلام خليجي:
تفاهم بين طهران ومسقط على الخطوط العريضة لإعادة فتح هرمز.
اتفاق فتح هرمز لا يزال بحاجة لموافقة المجلس الأعلى للأمن القومي الإيراني
الإعلان عن اتفاق إعادة فتح مضيق هرمز قد يتم خلال أيام
السفن الداخلة إلى هرمز ستستخدم الممر الملاحي الأقرب إلى إيران
‏السفن المغادرة من هرمز ستستخدم الممر الملاحي الأقرب إلى عُمان
‏أطراف إقليمية قد تشارك في إزالة الألغام والإجراءات الفنية اللازمة</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/naya_foriraq/87095" target="_blank">📅 12:00 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87094">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🇮🇱
🇺🇸
أمريكا تبدأ بإخلاء عدد من طائرات التزود بالوقود من مطار "بن غوريون" في الكيان المحتل.</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/naya_foriraq/87094" target="_blank">📅 11:59 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87093">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🇮🇱
إعلام العدو: حزب الله يحاول خوض حرب عصابات على الأرض و"الجيش" الإسرائيلي تصرف يوم الأربعاء ببطء وارتباك</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/naya_foriraq/87093" target="_blank">📅 11:45 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87091">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/q_cJluozQKZpIOrr3guUG0cb--qRY11SLA8TXhW5iHxdO2WRJcLm6_fGMfuZgLjTX958hSHfh-YY-bNwbyx-Z9lYvxnbkrXmgQHCaQia1RfEVY2dl2piOjGFlkGseKd8UCyv_UoThs2IoGtW-6JkcnnlUeXtTHvIdz1D4sNleWC-3AJtlp_RQT9V4RkhW36yKpgSFOWUHnSCgxyE5TI613F_vp0TpLr8s06lZBZVqAST0mkPX9aII_NlpXAxH5Qw7dgIQZGzZeHeQK3jLUh5Uq-2M_KsSsvbCb88NErAyraAl6lpEAa4zi-3Ol5okM1P7Eu2ij0C5AN07wX96-mF9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UZgt-rHiZsydya0LYsEtIu0F8Z9i0wh32IXcWmKvreIyUCEZzgIKBlrZhn5OBA8BpKvnSosJIcwdEULVhCzS3OaCbBLkKszJwHvUMstgiaEsIMriiwrSYk_x0OWBSy3oBvA44YW5P4E58XqJNe5Mtqa-Lfv-iODMBYAC3GI2qEWQhLkGNsJQVCKG89Qhkjxt1dc4I_Jws_R8iNjXfWCnN9RVNOIAXxrapxqiFYg-MKtmzHl3NyJ2mKsY-F9NBDZRcg1Qg84PA8vrZMjd38UlQsGyQoNVPy3BHDHkAcySY52L2pT1ZF4ELXzeYgHsEbzTTW6bCDnGKI7p4CLaEr0pww.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">مشاهد أخرى من انطلاق الصواريخ اليمنية نحو أهدافها</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/naya_foriraq/87091" target="_blank">📅 11:30 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87090">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SNz0R1NF5eVe4U_DoD4q7-7AUhQkZ9iY3Th1GqCMfZ6PU8NWsOlyQc-zjPBvtCyegUwPR6_b3Qi8IDDY2UGtz4sFUkClYSEi654CDgj7jTIIS88iGU1ds_FA45UWmUvg5eeQ6d7gCjxdWuiBZgDU18EeoqRLHVwyqBFa4DPPMUnro4kqeZZVlZM3H-D2vhm4ntShPm-BJRF1FkgGEt9fguE6UY6RUCHvokNr9SQt0nZVyKXqQgY0voTl9RkbnE9wUhFD6vjFFgCNMbwoSoBIqpj2mAf_vGD1SA8NwIRaN8sxFLssD5HyYt0F5u2KoshR-Ocgv0BlfoOY3cg4HAy-Aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حدث بحري جنوب شرق كومزار في عمان.</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/naya_foriraq/87090" target="_blank">📅 11:19 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87089">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">حدث بحري جنوب شرق كومزار في عمان.</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/naya_foriraq/87089" target="_blank">📅 11:19 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87086">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZA8-F9c8lS5I0-rqIixPdeNp27NCXPdmtGVMKealBgAnUq9PWn0S-t2UIDPaQ0plJLrxNmfLjflTuxgcWv6WLHRXHbgKX1fjkmqt2t6BjPkUWS4oiQqdOMtJ_G2yzXtS98UxhYuuFwTKhJCcqnBwekGifsJtxKbMxAa3f_by8ys1Zpm1Pa9e_rSOqN0UlfEE0wxpzV79lFtYHn2QdI_JJ9psI2ahg1QPkbiLnK46si2kaW0Vp_mBzRkb55goUN2sdLMijo3qMhhweHqgCKA0JmJLaPpWzvj3JApsYYS3aOJg_AIg1yaGcGaxFU3ahWAIRTpZ4QZv2a55Jutq6kpsDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oycabtlM-7j2okk-LAhaeA-oBA-zgJLZCKuL0ki4gH0RYP03G99dldxes7ZpCHpJwHd8gP3KrlutyAt75lofEozhNbEJy4GwC6Vba1HSVJKZPEJ8poiblx_eRiXAjaNffYvk03wSm221a7-1VziUyXzKDIzqLQDm63cjOs522Gu-AG8SuG7rJD99eFY2uof5aMmV9sazz5trxZ3dIiRrEkpCqe_SWFjsEqdZXjO3VWOrChjyjn1O9g6jraqJlsldP89bKAhT_wN86hRVw-Mi9rZUn_YOGtpu4_C_V0CchMX7wLI8obGVFfIumYbqFTsorhSL07szUCXrWxVP_4HNQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AFP5F5XAwf9Q1BDLgIcbgvimbx-eS8_-g683ugdbGoD0fVc-MK-knDDrr1N-tyPLGuAlxRQ7B5sUVXgMEy_5fqrtVxhGriT3GboKjOG4iekNo7932eyBtOiBIozVyPjkVspiF-49PMTY4T-M90LOxU62X80qkMH3biB1t31ETpzAn7AT1bKloCKNFunjlcOHWaOg8JF8fTgOUyzMPMpkE7pB78gKG1-JzgARDUfnASURKMZVnGtUks4U-g5TXGRrD4uGySnsRcOzIeTU_gVapniDxZiAKIcxjGCBe1PSmCU3cqDbS1yhGiBtnnTR2I8puy9uLXm9z4nitnaQkTYKIA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">إطلاق صاروخي من اليمن</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/naya_foriraq/87086" target="_blank">📅 11:17 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87085">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">إطلاق صاروخي من اليمن</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/naya_foriraq/87085" target="_blank">📅 11:16 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87084">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/naya_foriraq/87084" target="_blank">📅 11:16 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87083">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🇮🇶
وزارة العدل العراقية تعلن كسب دعوى قضائية أمام المحاكم الأردنية لصالح شركة أدوية وتسديد مبالغ مالية إلى الشركة.</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/naya_foriraq/87083" target="_blank">📅 10:36 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87082">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🇵🇰
المتحدث باسم الخارجية الباكستانية: لا نزال منخرطين مع الدول الأخرى بشأن الأزمة في الشرق الأوسط والوضع في هرمز</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/naya_foriraq/87082" target="_blank">📅 10:14 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87081">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">‏ترامب: نقوم ببناء أكبر عدد من مصانع الذخائر في تاريخ الولايات المتحدة
‏سنصدر أحكاما بالسجن بحق مسربي التصريحات "الخائنة"</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/naya_foriraq/87081" target="_blank">📅 08:18 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87080">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🇮🇱
حدث أمني في حي بارك تساميريت بتل أبيب</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/naya_foriraq/87080" target="_blank">📅 07:56 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87079">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🇮🇱
حدث أمني في حي بارك تساميريت بتل أبيب</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/naya_foriraq/87079" target="_blank">📅 07:44 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87078">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9fb71ce607.mp4?token=BHjOsO-FXy1M9FrkV9ArxDlnl4pVOr6057Ep9tud-ul3B5ZJJFOgfcMp40aY04S7iD-BFo7OoFi7Gh81VWizEO9pzobe6-WagEtouvuHxiQ7WrYW9b69M6TKAFQUXiIR6m-wBYuRUuwCqGQFh8J39VvwuCJ8Ukd0aHWqcZ8ai2g9A-qVo00Ounx80CQRLyj0QLVqJ7bQkcHQYTTeYw6G9vk99eWioOdWdajIjj5Wn9WIlbmXjDJDDdFOzQ8L_OGFwNyKaagkdpxDW-FYfjj3lommGycEUGw9LxK37UG9NSmNK4yXKzEXraDw-fn9slT8m1K4mEVxC5_qY2716KXX5rvky30fLgegrn09cLRfqI56_hZ-If_YIk3uVfzaV4RSFpppalTAbStgjUD1zC8EGThSUQcwHMQXEZa9QciYHIv2W4TIpCj_iiPcV0-iihc9Y4Nb8HYlYIZhrB66063FZ4WSOthHT_7STivQQATz9NzKVDHrhX3ppcFfiapPjaSdBCN6abwOmuZSCj82eU5S6Dn1UDqY4-tStPufP3DCwt_8mtJZ3o-zRT3hLnSiA1RpvPi7f7X3L_A4z6m5I86oDhpjEB19EnNOcOwJpgzh1zP3SuRTujhPo28axCu54T8luidWwtrkFIfp6A0bY6JrUnC6uV2I2uJclOi89ZOoS5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9fb71ce607.mp4?token=BHjOsO-FXy1M9FrkV9ArxDlnl4pVOr6057Ep9tud-ul3B5ZJJFOgfcMp40aY04S7iD-BFo7OoFi7Gh81VWizEO9pzobe6-WagEtouvuHxiQ7WrYW9b69M6TKAFQUXiIR6m-wBYuRUuwCqGQFh8J39VvwuCJ8Ukd0aHWqcZ8ai2g9A-qVo00Ounx80CQRLyj0QLVqJ7bQkcHQYTTeYw6G9vk99eWioOdWdajIjj5Wn9WIlbmXjDJDDdFOzQ8L_OGFwNyKaagkdpxDW-FYfjj3lommGycEUGw9LxK37UG9NSmNK4yXKzEXraDw-fn9slT8m1K4mEVxC5_qY2716KXX5rvky30fLgegrn09cLRfqI56_hZ-If_YIk3uVfzaV4RSFpppalTAbStgjUD1zC8EGThSUQcwHMQXEZa9QciYHIv2W4TIpCj_iiPcV0-iihc9Y4Nb8HYlYIZhrB66063FZ4WSOthHT_7STivQQATz9NzKVDHrhX3ppcFfiapPjaSdBCN6abwOmuZSCj82eU5S6Dn1UDqY4-tStPufP3DCwt_8mtJZ3o-zRT3hLnSiA1RpvPi7f7X3L_A4z6m5I86oDhpjEB19EnNOcOwJpgzh1zP3SuRTujhPo28axCu54T8luidWwtrkFIfp6A0bY6JrUnC6uV2I2uJclOi89ZOoS5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇪
رصدت الأقمار الصناعية آثار اسوداد وحريق واسع في منطقة جبل علي عقب انفجارات متتالية شهدتها دبي منذ يومين ؛ حيث أرجعت السلطات الرسمية الحادث لـ "حريق صناعي" وسط تكهنات مستمرة حول الأسباب الحقيقية.</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/naya_foriraq/87078" target="_blank">📅 07:25 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87077">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d964adb32.mp4?token=pTtqWN2MMqD4u2BwN12JZfOg4Wn4ltQAzA1ow0a6Ua0HlrelPBgkC78KUwAUnphAWDuCImOB0VQDmAfuVg2d9J77GeidZkF4XW7mLZF7cNZFOxVXyRInWbxsarDOmjhOu2WFE9cNz6K1ViYogaXsFa-TPA342hBH3XsHbmcSAzi-FfTNVX21OSSirR800vWP3BXpB4LhuHggzQHmffgSXDS5opfpJEygWFwubOpQhfDWsPQAwn_nsShD9JqK8reND6JnFlblQI-lGCuH-67E_zfTJBrD4ODoh3hbmj269yqKuS2x6Wis8b7ankIzwEohsJb3sp1XpAaZl1wKOz35mQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d964adb32.mp4?token=pTtqWN2MMqD4u2BwN12JZfOg4Wn4ltQAzA1ow0a6Ua0HlrelPBgkC78KUwAUnphAWDuCImOB0VQDmAfuVg2d9J77GeidZkF4XW7mLZF7cNZFOxVXyRInWbxsarDOmjhOu2WFE9cNz6K1ViYogaXsFa-TPA342hBH3XsHbmcSAzi-FfTNVX21OSSirR800vWP3BXpB4LhuHggzQHmffgSXDS5opfpJEygWFwubOpQhfDWsPQAwn_nsShD9JqK8reND6JnFlblQI-lGCuH-67E_zfTJBrD4ODoh3hbmj269yqKuS2x6Wis8b7ankIzwEohsJb3sp1XpAaZl1wKOz35mQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامب: "سعر النفط هو 75 دولارًا. قد نضطر إلى رفعه مرة أخرى. أنتم تعرفون ما الذي يحدث عندما نرفع السعر."</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/naya_foriraq/87077" target="_blank">📅 04:56 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87076">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hSJFhuwpAivUe6RIq0BWUUnAZQKBleZUqsKBEHhR8s_brSxdSzW5tBqcpAX3_ceC_Lidat67XoI-oi8LGJlyXfHH9gZJs0CebjIjNoBJ1-HHrZvUL_UUxbIgBGvC-f0LTyenoy7217h6ICzZoyBYXWQ7sOSTiVSYdGoIb0vad_mS9JDHdlmeHQAxTXPjKfaHWAKO2phBCY2_E69sNXikKXDpmisqAlxrsNBmp60CyFnIYTJ5tFBAr0eIok1oIyFSD0SbLQIWmzL1cJLM473RBKFp_C0F3hdA3Q2i6xuVoB3nCvRYP7rgLbVNQVHae0ZNJFm16OmyKrIzJYbER7pKig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
صور الأقمار الصناعية تظهر اندلاع حريق داخل سفينة بالقرب من مضيق هرمز.</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/naya_foriraq/87076" target="_blank">📅 04:13 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87075">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QrKlVsxvdKY29gWgcSbOzcgy8qeIC3w1ZHvMcxsHC3x2q7G8ujLL0yqX8cENWPULusG6bZZxocHYMuskn0oOzmWPnoMk3AO7Ss5JkEhVuBrepn27I3IvYrOvV9Hds6tgWzyxsnoJvpu_ZkjFkag4icmPfn_GgSkh-8ikBhkDpZIQJSFmPDzyVqJPYohiwdPtl0FXow9tBfPpzq0ynPT49Kk6KgvTdNksLEIePzmIJxYerdKpi6Ti-y8PiN3z6JJVQB_fvizzcNJh0esY6KqGCe5ugHtFAy1BDt_7MMPaoK6buB3S73elNmlDcqWn7uEEdq69EatQrG087WkJMQvmxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامب:
كان مايكل مور، "المحلل" السياسي الفاشل الذي يخسر أمامي منذ سنوات، يصرخ قائلاً: "لقد خسرنا في عام 2024، ولم نعد نطيق ذلك". كلا يا مايكل، فقط تعوّد على المزيد من الخسارة! لقد كنت خاسرًا طوال حياتك، ولن يتغير شيء
لن يتمكن عبدول، رفيقك الشيوعي الجديد، من إنقاذك. إنه يعلم أنك شخص فاشل وحقير، ويريد أن يكمل من حيث توقفت. على مدى آلاف السنين، لم ينجح مفهوم السياسات الشيوعية قط، ولن ينجح الآن، خاصة في ظل النجاح التحويلي الهائل الذي حققته إدارة ترامب، ليراه العالم أجمع ويتبعه: أفضل الأرقام الاقتصادية على الإطلاق، وأفضل أرقام التجارة، وأفضل أرقام الصادرات، وأكبر استثمار في بلدنا، والقائمة تطول. هذا هو العصر الذهبي لأمريكا، ولن تتمكن مجموعة صغيرة من المنبوذين، مثلك يا عبدول وغيرك، من تدميره وتغيير مجرى التاريخ. إنه أكبر من أن يُدمر، وأقوى من أن يُدمر، وأفضل من أن يُدمر. نراكم في ساحة المعركة السياسية. لنجعل أمريكا عظيمة مرة أخرى!</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/naya_foriraq/87075" target="_blank">📅 04:04 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87074">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">استهداف سفينة قبالة عمان</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/naya_foriraq/87074" target="_blank">📅 03:55 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87073">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/naya_foriraq/87073" target="_blank">📅 03:55 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87072">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/naya_foriraq/87072" target="_blank">📅 03:54 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87071">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🇺🇸
مسؤولين أمريكيين:
استياء ترامب من وزير دفاعه تزايد لأن هيغسيث كان من أبرز المؤيدين للعمل العسكري ضد إيران.
هيغسيث أقنع ترامب بأن العمل العسكري ضد إيران سيكون بمثابة انتصار سريع وسهل نسبيا.
هيغسيث دافع عن نفسه أمام ترمب بشأن النقص الحاد في مخزون الأسلحة وألقى باللوم على نائبه.</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/naya_foriraq/87071" target="_blank">📅 03:37 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87070">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🇺🇸
نائب الرئيس الأمريكي:
هناك أشخاص في النظام الإيراني يريدون إنهاء الحرب وهناك متطرفون يريدون استمرارها.
الإيرانيون عسيرو المراس والنظام متصدع ومهمتنا تحقيق أفضل النتائج الشعب الأمريكي.
سنستخدم كل الأدوات العسكرية والاقتصادية والدبلوماسية من أجل التوصل لحل مناسب مع إيران.</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/naya_foriraq/87070" target="_blank">📅 03:23 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87069">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🇺🇦
🇷🇺
الإعلام الأوكراني:
هجوم روسي بالصواريخ البالستية يستهدف العاصمة كييف.</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/naya_foriraq/87069" target="_blank">📅 02:06 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87068">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🔻
جمال الحلبوسي:
‏
السعودية والكويت تقدمان مذكرة احتجاج جديدة لدى الامم المتحدة ضد خارطة المجالات البحرية العراقية وطالبوا بسحب الخارطة و قوائم الاحداثيات و تؤكد السعودية والكويت بان هذه الخارطة تسبب تداعيات جسيمة بالعلاقة مع العراق ، والسبب هو للاستحواذ على حقول النفط والغاز العراقية.</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/naya_foriraq/87068" target="_blank">📅 02:03 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87067">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/38c964d83f.mp4?token=p2DORtvgw4lAbJmNYX6TpxKFk6sdwX1SvevHsgWT9G6cYjkuYvG-rtU-I0yX8u6_sarpcW7iDiL3OMsByeu3qS_uVWitFTzESOwfglP7k6Y4BVXgJjf3LBPtLZd4gKrLOjkTmqUTaF1BK3OpGlDDuD2f9ipYVN9KpspOQ2T5AV-GmxmixYw0reoRh39y9_1OPELuyblhekgp6FhJJkY9RI9aZILDDvBxzHDNH_-5V1EF75F1QrSLHBjqpV2AUHXr_UTSWRxflmbQuIFwkJltrbyA2jqg0Bp7VbCovQU_d-sKAZ1V4Ix67y99eSTUBDSsAKyDFADben17K4Ti8EaKOp4Bl0WlhBihFJJnXY4sg7KOrXC5llhkVE3VVI4WUwK9lPO-9Rdc-i6DvuP6QO0CTltP7eFl63t1eUvKOAj34xIgnutiwn3PmePTsLpvLKw5U0LFf4mxABNhVX3anAHGsSH4uYl4BF4B7gv9sMqSJveyLzppTRNl9jJwuGlvubaH4LL2sm0XdGlCyAL7Ao0ObrMWH_OQmyT-u-TysHb7LmUo4py0LvMc-ZEpqhOv0ZX-G1577gJH8V6aEHCJ-8UP5FSPiXOo4WMApr72zW7m4GP54wHkutyL0RXvRHukIJa7IXeVQ9QBrbtkEijIj6a6xCKMzSdpQ7cAma41WY19VLE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/38c964d83f.mp4?token=p2DORtvgw4lAbJmNYX6TpxKFk6sdwX1SvevHsgWT9G6cYjkuYvG-rtU-I0yX8u6_sarpcW7iDiL3OMsByeu3qS_uVWitFTzESOwfglP7k6Y4BVXgJjf3LBPtLZd4gKrLOjkTmqUTaF1BK3OpGlDDuD2f9ipYVN9KpspOQ2T5AV-GmxmixYw0reoRh39y9_1OPELuyblhekgp6FhJJkY9RI9aZILDDvBxzHDNH_-5V1EF75F1QrSLHBjqpV2AUHXr_UTSWRxflmbQuIFwkJltrbyA2jqg0Bp7VbCovQU_d-sKAZ1V4Ix67y99eSTUBDSsAKyDFADben17K4Ti8EaKOp4Bl0WlhBihFJJnXY4sg7KOrXC5llhkVE3VVI4WUwK9lPO-9Rdc-i6DvuP6QO0CTltP7eFl63t1eUvKOAj34xIgnutiwn3PmePTsLpvLKw5U0LFf4mxABNhVX3anAHGsSH4uYl4BF4B7gv9sMqSJveyLzppTRNl9jJwuGlvubaH4LL2sm0XdGlCyAL7Ao0ObrMWH_OQmyT-u-TysHb7LmUo4py0LvMc-ZEpqhOv0ZX-G1577gJH8V6aEHCJ-8UP5FSPiXOo4WMApr72zW7m4GP54wHkutyL0RXvRHukIJa7IXeVQ9QBrbtkEijIj6a6xCKMzSdpQ7cAma41WY19VLE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامب: قد أكون الشيوعي الأكبر في التاريخ.</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/naya_foriraq/87067" target="_blank">📅 01:53 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87066">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🇮🇶
إئتلاف إدارة الدولة:
المجتمعون أدانوا الاعتداءات التي تعرضت لها قطعات القوات المسلحة العراقية واستشهاد عدد من منتسبيها ودعوا الى الالتزام بتوقيتات خطوات حصر السلاح بعد 30 ايلول 2026 والتي سيتم التعامل بعدها بقانون مكافحة الارهاب مع اي سلوك مسلح خارج اطار الدولة.</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/naya_foriraq/87066" target="_blank">📅 01:43 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87065">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/54a22e27b0.mp4?token=nFqBNHAxMVFRFne089ErliXNSWYCoiX8eGOOPfETkBBGzvcSzIhnjRX7ukgtI-6JSNzi-GGHfyomyXlCmti33TGQnhX8FG45cTxxZQVqLeV_SLQmeAa1thhSYXOEsiH6dNvQa80dm5HPLnULUAHqL7jQzabBykCzvchTc-OWd2eRHitkVScsmIsx-t5__ACh-78ey9PkVIk24bV-_vXF6WwYtKyG6L585WaLtoF_QTs1rq5zdWfc324lC5nuCWEkIoeFfpr-4LE8CFGZ9zUhaPlCAWtD7ron-T9Ypymi59-bSIVZU0pXTu4gJUAQz7xprRNOj7ow8ARFHZfp263C4TzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54a22e27b0.mp4?token=nFqBNHAxMVFRFne089ErliXNSWYCoiX8eGOOPfETkBBGzvcSzIhnjRX7ukgtI-6JSNzi-GGHfyomyXlCmti33TGQnhX8FG45cTxxZQVqLeV_SLQmeAa1thhSYXOEsiH6dNvQa80dm5HPLnULUAHqL7jQzabBykCzvchTc-OWd2eRHitkVScsmIsx-t5__ACh-78ey9PkVIk24bV-_vXF6WwYtKyG6L585WaLtoF_QTs1rq5zdWfc324lC5nuCWEkIoeFfpr-4LE8CFGZ9zUhaPlCAWtD7ron-T9Ypymi59-bSIVZU0pXTu4gJUAQz7xprRNOj7ow8ARFHZfp263C4TzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامب: "نحن نستولي على كميات كبيرة من النفط من فنزويلا - مليارات البراميل من النفط. الغنيمة تعود للفائز."</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/naya_foriraq/87065" target="_blank">📅 01:24 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87064">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f8a8d43d8.mp4?token=H2s9ujBbBCuWOM1cHvMRDgES2b753mZUPjtGK1pokdcnB2jZNxwng_z_kHOpIpN4hZddVJi00OWQgXOz720WYOMuuGdg3djf5y_EOExrel5wwHGXH-CNOKe0B9NxGa1pNtbwdvKmbTE508dxsIv7Yyqw3VJQKY6MyVnDwicoe4vLX_7-1yfD0IEA-GK4cbxEWGRAa0Heqdzww3nDo9iOoVfcUHdxXurYmzWl2H2t7bqxErqjOB5XKurLdVVlC09afdBAKQDzCq6SZgBx2ToykHy58ZpA9mIznu807EO89I3SfjODdxD53EZjSAmPI25c8RE51hCPJjhriaijDJ5aH4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f8a8d43d8.mp4?token=H2s9ujBbBCuWOM1cHvMRDgES2b753mZUPjtGK1pokdcnB2jZNxwng_z_kHOpIpN4hZddVJi00OWQgXOz720WYOMuuGdg3djf5y_EOExrel5wwHGXH-CNOKe0B9NxGa1pNtbwdvKmbTE508dxsIv7Yyqw3VJQKY6MyVnDwicoe4vLX_7-1yfD0IEA-GK4cbxEWGRAa0Heqdzww3nDo9iOoVfcUHdxXurYmzWl2H2t7bqxErqjOB5XKurLdVVlC09afdBAKQDzCq6SZgBx2ToykHy58ZpA9mIznu807EO89I3SfjODdxD53EZjSAmPI25c8RE51hCPJjhriaijDJ5aH4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
🇮🇷
‏ترامب:  أفضل إبرام صفقة مع إيران. ‏نحن نتحدث مع إيران، فلنرَ ما سيحدث. ‏لا يمكن لإيران أن تمتلك سلاحاً نووياً.  كنا نستعد لشن أكبر هجوم منذ الحرب العالمية الثانية لكن الإيرانيين طلبوا مني إجراء المحادثات.</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/naya_foriraq/87064" target="_blank">📅 01:19 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87063">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🇺🇸
ترامب عن كندا: كندا دولة سيئة. إنهم أناس سيئون. أنا أحب الشعب الكندي، ولكن قيادتهم سيئة.</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/naya_foriraq/87063" target="_blank">📅 01:16 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87062">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d5cb415232.mp4?token=MSOBGnlKA6z1oaWpEFjjVe5BRi2HmXnQm6fMak6LnVGu44w9N3QDuFHt1dmarCCF0W9_2C-tSXjjnJUXQvXp8c2cXziylcr_Gm-Ip8Equ6pir5GoqG8SI62hX1dgHbn_3SZCX7zNm936eBuyWlE4XnlYQ4hTffsNItMfOy-YVJj35-vk4GjO4LA11Qevl6--9Mv_zN1FhAKH_uen1a31tWGqg-gpbnbBrYJSTtgiyIZ-lsloQ6BgmjyWtTG4ywk3Mha6DxJY6ZMhOCOqiYRdsYj-KNhMDHULh6aOd1ITcoF5gSymeP5on3nzIF7j7wtqKbo9gR4602WsmddKE8hE0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5cb415232.mp4?token=MSOBGnlKA6z1oaWpEFjjVe5BRi2HmXnQm6fMak6LnVGu44w9N3QDuFHt1dmarCCF0W9_2C-tSXjjnJUXQvXp8c2cXziylcr_Gm-Ip8Equ6pir5GoqG8SI62hX1dgHbn_3SZCX7zNm936eBuyWlE4XnlYQ4hTffsNItMfOy-YVJj35-vk4GjO4LA11Qevl6--9Mv_zN1FhAKH_uen1a31tWGqg-gpbnbBrYJSTtgiyIZ-lsloQ6BgmjyWtTG4ywk3Mha6DxJY6ZMhOCOqiYRdsYj-KNhMDHULh6aOd1ITcoF5gSymeP5on3nzIF7j7wtqKbo9gR4602WsmddKE8hE0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامب عن كندا:
كندا دولة سيئة. إنهم أناس سيئون. أنا أحب الشعب الكندي، ولكن قيادتهم سيئة.</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/naya_foriraq/87062" target="_blank">📅 00:53 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87060">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ozmga3yvkIFCzMwnpaDm2AP-68O_MLZltSjI56_CNx1C6xR6M30DEZiFwwOmWRIe-CIaVq9gbHwKbv_AfRBnERgm7Nms9irB6ST5_xJsQVJkVW5e0Rz04czPBDhuTrFr87hYTNDvLcC5PQAFKagcW8RJJMVxI-pz4fIit0VjB6Py_OLfqOejaticYZ50l9HuvkPdo6K_bSN9sjZiq0Lm90B4dmCvmPQ8SDISvvJQBpsxc88r78mejqitQn_i52pIWyhLWzlH0aWr3-NOqALRCgTBtQcM0RIXZ4tVDMknEOT3tea3valYVO0a1qb1AEEcaqc9iSamttMlK5NMP2-VTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامب
:
أمس، كانت احتمالات فوزي في الانتخابات بناءً على التوقعات هي 28 إلى 1، وكان العديد من هذه التوقعات بعيدة عن الواقع، ولكن إذا قرأتم "الأخبار الكاذبة"، فستظنون أنها عكس ذلك تمامًا، أي 1 إلى 28.
كل ما تحدثوا عنه هو هذا الاحتمال الواحد، ولهذا السبب يطلقون عليه "الأخبار الكاذبة".</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/naya_foriraq/87060" target="_blank">📅 23:48 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87059">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ojv0lkRqkaidHVkYZLRqVJnchMtq1qtC5QFuqh49EZuSiHPPZJerXOwGbMh-jx5NsKTneT2JYz-E85hYx2I1prIOZgaBvr5IzvrAUCDVLXKvM04VtDaBXxCwnEbz_bvjJCUBkobBFpBfMQdoDPwFRNMWrF5fneyOkVY0UGCFrs-_QEovgskV4_0itVyNTikrISymq-gUPG67_ZuhetnTSt3pkIHO_dNUryjjtUALkvbavG413tYPQqf_V2aftuvZy2j5iwE7zdLzTe1OZ3kXK8sdRRtpj_-3epWCFD5gHTY6QCVefRrbJy17uNlikW52WkfjxPvWdoxNjaYEWGoVUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هبوط طائرة في مستشفى "رمبام" بمرافقة ثلاث سيارات إسعاف بعد انفجار عبوة ناسفة بقوة إسرائيلية في بلدة مجدل زون جنوبي لبنان.</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/naya_foriraq/87059" target="_blank">📅 23:44 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87058">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/61da47e607.mp4?token=CV13Ia4S_cRZ7HHN2cQY9SbgjEnx23exAkJEz564aDxFL7Ubblvx97eqXduj8JHToyb09pLbyATbjDBBmacSMeQSr1pGCfOklfyGqAlnbM5Hs9s6VA5Zup05EeckWtw_oo5zDGyhgqwC6XZ9t38lNwI5tKigJuTiEyEPUYqMRlTLbhIuc7TkMbeay9Y-AbpX954dk2NJrlWTwnaZr8FHaFOp1Dj2kJbBp2PCgPDQUPpBaWuktVJBcO39ZObeJuYmkM1Is88L_XNC4CUBXDdbCWeQOQDwJdhvJkHxC5WI392tQkSPljTqCJIAIEgJTXLwFE12vYI4zKfv8woxYLgppQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/61da47e607.mp4?token=CV13Ia4S_cRZ7HHN2cQY9SbgjEnx23exAkJEz564aDxFL7Ubblvx97eqXduj8JHToyb09pLbyATbjDBBmacSMeQSr1pGCfOklfyGqAlnbM5Hs9s6VA5Zup05EeckWtw_oo5zDGyhgqwC6XZ9t38lNwI5tKigJuTiEyEPUYqMRlTLbhIuc7TkMbeay9Y-AbpX954dk2NJrlWTwnaZr8FHaFOp1Dj2kJbBp2PCgPDQUPpBaWuktVJBcO39ZObeJuYmkM1Is88L_XNC4CUBXDdbCWeQOQDwJdhvJkHxC5WI392tQkSPljTqCJIAIEgJTXLwFE12vYI4zKfv8woxYLgppQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
السياسي العراقي اراس حبيب يهدد بغزو السعودية: نحتلكم مشي على الاقدام.</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/naya_foriraq/87058" target="_blank">📅 23:24 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87057">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ece2d0da1.mp4?token=nxbUE_Np_ZglemKySPHYJX87WbPkAWHuCwXqkGZPeAU2E0XuMavizASHEPftEM0VXl1VxQ6J7P5a6hDJSn74bbpbU2DwV97ERUFDJImeKbs2H2i9UksiRJ7WjxowDx39oIHMe8PF-jMEE1E5SwyW4hqkiWtanKrl8nXSsYAl5y8KQUerL3EA2SGzYyO3EstVvvES_R4fml3xcW76oUcP9hDpfUqOqvjHgDyCNzpGVEAwNv3YZZfg6hho1iodbBvAo9g8f8a4D82qWBEXMxAYjLkPwFTY6VLbs6QZ4zlkof4cMrpDHGGSW275uqLmyvDfZPAbS82yu3UWf4gChd_TeA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ece2d0da1.mp4?token=nxbUE_Np_ZglemKySPHYJX87WbPkAWHuCwXqkGZPeAU2E0XuMavizASHEPftEM0VXl1VxQ6J7P5a6hDJSn74bbpbU2DwV97ERUFDJImeKbs2H2i9UksiRJ7WjxowDx39oIHMe8PF-jMEE1E5SwyW4hqkiWtanKrl8nXSsYAl5y8KQUerL3EA2SGzYyO3EstVvvES_R4fml3xcW76oUcP9hDpfUqOqvjHgDyCNzpGVEAwNv3YZZfg6hho1iodbBvAo9g8f8a4D82qWBEXMxAYjLkPwFTY6VLbs6QZ4zlkof4cMrpDHGGSW275uqLmyvDfZPAbS82yu3UWf4gChd_TeA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
السياسي العراقي اراس حبيب يهدد بغزو السعودية:
نحتلكم مشي على الاقدام.</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/naya_foriraq/87057" target="_blank">📅 23:16 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87056">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gRVI7WtAB3GVrhtL0VHkWJQu4e2jS2abjYoBcOsu9mu7MgHtl8w8HZGz8ex5jSez-nMzagtZEGQm9RXtr5BjBzrCJyejiNbRdzZYb6X_8rhW1qUWO9L5r9XsIohJJ-pMVAI1yR3g7l9ADiK_u0f8U9eiRC_kQOEPcTfMzZEgSo7Xg7oobcDWRuPVkYiHNFUCT7xojrOY-i8tj5UrHNKCSQqL8AhVMBJ9i5W1-K3LFam1qXWrWp_wZEQI0aqDGCDDqQx22l9Tca84RG-5TWPucXk07Fs9i_Y8DaTphAdN1FMonwID0WqDypS9zlp7PJESQwB_AeKtbrgd9Y7BIXuxng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇾🇪
متحدث القوات المسلحة اليمنية العميد يحيى سريع: تمكنت القوات المسلحة اليمنية بفضل الله من استهداف سفينة "Daisy" النفطية السعودية في خليج عدن وذلك بصاروخ باليستي وقد حققت العملية هدفها بنجاح بفضل الله، وتم إصابة السفينة وإجبارها على العودة.  يأتي هذا الاستهداف…</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/naya_foriraq/87056" target="_blank">📅 22:11 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87055">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🇾🇪
متحدث القوات المسلحة اليمنية العميد يحيى سريع:
تمكنت القوات المسلحة اليمنية بفضل الله من استهداف سفينة "Daisy" النفطية السعودية في خليج عدن وذلك بصاروخ باليستي وقد حققت العملية هدفها بنجاح بفضل الله، وتم إصابة السفينة وإجبارها على العودة.
يأتي هذا الاستهداف في إطار فرض قرار حظر الملاحة البحرية على العدو السعودي وفق معادلة "الحصار بالحصار".
تؤكد القوات المسلحة اليمنية أنها ترصد بدقة كل تحركات السفن السعودية النفطية ولن تسمح بمرور أي سفينة سواء من جنوب البحر الأحمر أو من شماله حتى تتم تلبية مطالب شعبنا المحقة ويرفع الحصار عنه.</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/naya_foriraq/87055" target="_blank">📅 21:44 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87053">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iCxcR06TEeWPnB-5XBNGtRFthwDktQRQ7wkT3S_54f5_BqCuSOnsJT52zLpM-6AUxyzwhOKlR2Lez_GZ0LBUS_8PadkiVGUK48Tz0k-ofCIvTEZjOSNgnrxpI48DUG7UXOVtXU3HjWmwSqwgxjAy60NI7ZIVA4uKQ0fMofBnc26bJ3ViYNpeHKy3LWAjn-Okh5U7g_g2gv9eEcZxTTYjY7rL10KYwdZCQbJmwQLdM6m3PbEPNd54Cj7e52NMOtst-xS30GaQ0KmQ2aO3Zw8mVfbkGTjNnS14P4LejhKD8ypxOxJz8Lx7As2Rve8KiDzdBv-VJ8r4Gxuj5DyjtvmhOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حدث بحري في البحر الاحمر</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/naya_foriraq/87053" target="_blank">📅 19:38 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87052">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">حدث بحري في البحر الاحمر</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/naya_foriraq/87052" target="_blank">📅 19:37 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87051">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🇧🇭
بحسب المستشار الاعلامي لملك البحرين: البحرين تعرضت للقصف من قبل ايران قبل وقت قصير.</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/naya_foriraq/87051" target="_blank">📅 19:12 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87050">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🇧🇭
بحسب المستشار الاعلامي لملك البحرين:
البحرين تعرضت للقصف من قبل ايران قبل وقت قصير.</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/naya_foriraq/87050" target="_blank">📅 19:10 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87049">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pzjeh3dml2QRWiCqdOx_OD8Uf7_x1BWLX04-5bnHD2bm4Xom7xS18mnFH3u_esbzo6hoxWkvXBF19_oeQOgJiE5Y_VKtG7x-yWDisryVeNLffMINjaSYkgO4Y5kG0ltIVfy4tHWtUyuKqYbCS269jDHPSns9IPgP4Mo4jX7wAbZc1ushQ0a1IdirKPR-UVM2_bg9uUUM37Svua6-Yt-FPY8FuPlds8e8BpeSN26SBTXbwV4NdJ6c_2SD3NACuU01A4j_uEcII9Vrticjp-rpYuT2kIYfVEWeNXphXUeJX4sTm0RheMZh8NKOMH-8hVfFx--JG589YGvA4XPFDiGOtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
بعض أهالي سهل نينوى بمحافظة نينوى شمالي العراق تلقوا هذه الرسالة وهي تتعلق بالابتعاد عن الاحداثية التي تتضمن موقع الفوج نفسه الذي تعرّض سابقًا للاعتداء من قبل العدو السعودي ما أدى إلى استشهاد 10 من منتسبيه.</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/naya_foriraq/87049" target="_blank">📅 19:09 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87048">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XhSgy4RBwisWCpQumnFNIHXUUKoUVIP1vr2nucAxHSOBiVoDOz9JadlDXS_muDA4krp9keGXgOuspg7UwMbsFgfH0Yq8PUcYEKj3CqwshYXbIqYR5_vtCkOuLi0zsjerYuiiOdTADRsY21gqEOQ4lYh4d9eSHRetjWGGwE8ucztJkE8VKz5rO7EH9e0NkCCZitaR1u3K_LeIR6ZBXL1lGCa_owL_w2YiTH4m8EpcXd98QNpvTL_TrwFwfqFk02HFtNxx2OQ5JXKb0B_LMUQn5L4YnIqy7Zc8X6YEUNTvDydsIZYDgS6COmOw27Y9z32TmHqBEyKTfwzYAQ_kh12bBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇱
الاعلام العبري
اطلاق صاروخ اعتراضي في اشدود نتيجة تجربة للدفاعات الجوية.</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/naya_foriraq/87048" target="_blank">📅 18:50 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87047">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🇮🇷
‏
الخارجية الإيرانية:
تم الاتفاق مع عُمان على الخصائص الجغرافية للمسار الملاحي في هرمز.
وهذا لا يعني ان المضيق آمناً لعبور السفن، لأن العوامل التي تجعل مضيق هرمز غير آمن من قبل الولايات المتحدة، ولا سيما الحصار البحري وغيره من الأعمال العدوانية والتهديدية ضد إيران ومصالحها، لا تزال قائمة.</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/naya_foriraq/87047" target="_blank">📅 18:33 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87046">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">اعلام العدو: قتيلين كحصيلة اولية في الحدث الامني جنوبي لبنان.</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/naya_foriraq/87046" target="_blank">📅 18:29 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87045">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🇮🇶
الاتحاد العراقي لكرة القدم:
تجديد عقد غراهام أرنولد لـ7 أشهر لقيادة المنتخب العراقي في بطولتي الخليج وأمم آسيا.</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/naya_foriraq/87045" target="_blank">📅 18:24 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87044">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🇮🇱
نتن ياهو:
ترامب صديق جيد جدًا لنا، ونحن نقدر الجهود المبذولة لمواجهة طموحات إيران ولكن وجود إسرائيل لا يمكن مناقشته.</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/naya_foriraq/87044" target="_blank">📅 18:14 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87043">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🔻
هيئة الحشد الشعبي:
تنفي هيئة الحشد الشعبي ما تم تداوله عبر بعض منصات التواصل الاجتماعي بشأن وقوع اشتباكٍ مسلح بين قوات الحشد الشعبي وأي قوة أخرى في مدينة سامراء المقدسة، وتؤكد أن هذه الادعاءات عارية عن الصحة، ولا تستند إلى أي وقائع ميدانية.
وتدعو الهيئة إلى توخي الدقة في نقل المعلومات، واعتماد المصادر الرسمية، وعدم الانجرار وراء الشائعات والأخبار غير الموثقة.</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/naya_foriraq/87043" target="_blank">📅 18:04 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87042">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">الخزانة الامريكية ترفع العقوبات عن شركة فلاي بغداد</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/naya_foriraq/87042" target="_blank">📅 18:01 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87041">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">وزارة الخزانة الأميركية تعلن إلغاء عقوبات مرتبطة بإيران</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/naya_foriraq/87041" target="_blank">📅 17:59 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87040">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">📰
وكالة رويترز:
صادرات النفط الخام السعودي من ينبع انخفضت إلى أقل من 3 ملايين برميل يومياً بعد هجمات الحوثيين، بانخفاض قدره 0.8 مليون برميل يومياً. وكان إجمالي صادرات النفط الخام السعودي يبلغ حوالي 4.5 مليون برميل يومياً لشهر يوليو/تموز قبل هجمات 26 يوليو/تموز.</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/naya_foriraq/87040" target="_blank">📅 17:56 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87039">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IeUSwTtSqNtlb2SHXEQY7hCIF2q5gZd9OYMDvVeod-VwFsWFC5GgnBIhrBN8y3ovqamrmXkMVwJFN3wUJa0ga2iwg0mv7gZullC0_-nNaQ1s1pRFaBQ6EgYaRRVcdxutct-J54JnSAS_IvdW5RRPXBnSzgpdtLdFMzFxwJOxIfhpXCC1vvi80NZNX6hoGkkqgc5-hvPFPUP3bIX4pS3PIoP9udZLe7JwjXwk3TMOVMDLP9AuWSYnZsiV2l71NcF6jeq77gyIpvqaL5nCFI_PArm2fXC8PIjmfJfLXrEoX1LFDPG3TdOWPNDyIwYejSIF4H8xO3AhXZ3pE6JCycTl0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامب: خبر رائع للحزب الجمهوري. السيد، الخاسر الشيوعي الذي يكره اليهود وإسرائيل، هو الفائز المتوقع في سباقه مع الاشتراكية. وكالعادة، كانت استطلاعات الرأي خاطئة تمامًا في هذه الحالة. لم يكن متوقعًا أن تحقق أداءً جيدًا كما فعلت. الآن، ستزداد سياسات الديمقراطيين المجنونة سوءًا!</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/naya_foriraq/87039" target="_blank">📅 17:45 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87038">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">وزارة الخزانة الأميركية تعلن إلغاء عقوبات مرتبطة بإيران</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/naya_foriraq/87038" target="_blank">📅 17:41 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87037">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a5f37d7808.mp4?token=D_-kaVx4U-Ek0Zm4bJsrzW17B8NVmDpwv-zgwiI7dQbwg2TiWx1hktIigeZFcw8sJJCi38ubn6gxKn4B0upFgNxM3nM4qYrJ85WgbsLxK_LI65zh7sQ5h7HPbKm9C5RVDLQcLYPXaqGAdfFNbL_XHKHylZlYRoABqMpxfzFrVZnXw3l1k9KJ9wgUKc4Yi1UWiUW4KzPlxEyRy2jIBHihYmI4fBtiAJXuP4J72FNG_PZntNQnUKPcSSWH5u9Fer4LZJWQjRWqglZRWHd1uP2zfmaMB0EWV13m2XIkuoGvFbj9nwlk25nyCR2AXfDti0gJjZ_Lgdk8e1Ro4QmJ9EP13w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a5f37d7808.mp4?token=D_-kaVx4U-Ek0Zm4bJsrzW17B8NVmDpwv-zgwiI7dQbwg2TiWx1hktIigeZFcw8sJJCi38ubn6gxKn4B0upFgNxM3nM4qYrJ85WgbsLxK_LI65zh7sQ5h7HPbKm9C5RVDLQcLYPXaqGAdfFNbL_XHKHylZlYRoABqMpxfzFrVZnXw3l1k9KJ9wgUKc4Yi1UWiUW4KzPlxEyRy2jIBHihYmI4fBtiAJXuP4J72FNG_PZntNQnUKPcSSWH5u9Fer4LZJWQjRWqglZRWHd1uP2zfmaMB0EWV13m2XIkuoGvFbj9nwlk25nyCR2AXfDti0gJjZ_Lgdk8e1Ro4QmJ9EP13w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترفيهي
🇦🇪
السلطات الاماراتية تقول ان ما حدث فجر اليوم في دبي هو حريق داخل ورشة.</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/naya_foriraq/87037" target="_blank">📅 16:55 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87036">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/836d56fab5.mp4?token=oNqvhVB71cCbyGADGq6Eoch1EWob-0cXFs157B57tak-sRZFLFgS61gxUXdQNktbTPZlf4_4ktFyGDkBX7vhPsReWKcBFvQSEgjU5Qu3CqC3JFMcyYPiZbD7vduAjt1vjBAFazHQcbPTWw9qR2IpnwXyUM2noyQkjMVgvx1vC4a5TIYdYTZcstP2BQZK1EWYzQY3NX52A6eg2tUIPJaJ_ir2L1J1KM604DAW4rm4gMaDZLCo7eyUmoNP2oXxjtRxCcGJdpza8ZfYsUdHglZU7pRPknuPUM2I163Y_vd7DaEvUYOd9D8Zhd2TRc3ScDcKhyzLEjdK9wwpJU8dVaXN8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/836d56fab5.mp4?token=oNqvhVB71cCbyGADGq6Eoch1EWob-0cXFs157B57tak-sRZFLFgS61gxUXdQNktbTPZlf4_4ktFyGDkBX7vhPsReWKcBFvQSEgjU5Qu3CqC3JFMcyYPiZbD7vduAjt1vjBAFazHQcbPTWw9qR2IpnwXyUM2noyQkjMVgvx1vC4a5TIYdYTZcstP2BQZK1EWYzQY3NX52A6eg2tUIPJaJ_ir2L1J1KM604DAW4rm4gMaDZLCo7eyUmoNP2oXxjtRxCcGJdpza8ZfYsUdHglZU7pRPknuPUM2I163Y_vd7DaEvUYOd9D8Zhd2TRc3ScDcKhyzLEjdK9wwpJU8dVaXN8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏جيش الاحتلال: البدء بتنفيذ غارات في جنوب لبنان</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/naya_foriraq/87036" target="_blank">📅 16:44 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87035">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">جيش العدو يصدر انذارات في جنوب لبنان</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/naya_foriraq/87035" target="_blank">📅 16:42 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87034">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">شركة يورو وينجز للطيران تعلق رحلاتها الى مطار اربيل الدولي</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/naya_foriraq/87034" target="_blank">📅 16:15 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87033">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TieUE2FTVmajOHpsJ5ksvJsEnOIBwwlUwborzw2Hk2culJj8UX2npYgVodiECx8_YtFuHH1QJ4Jel9GxxAtrulzuOj2v3hfXxQlp5Ev3RW2glEnKF-61xygth7ze0U_rZ_s9v_IlFipkLP-hMXr2YPF1yTZ26AMKjzfnZQaMVWv_9tSUMTxFRzJkpOpIdBq_opRZ831i_7CqFwwNG5w4c6eGV0DixNgeJ4Uw9eQI-qTvdhU-Uaxjf3fMbnu4n7sPN1CyGmadF6axSYKD7rv_Ye-Dw5paqujca0mMYsQAPJsbZrEOmU68K2IUkvT9jKZviQPuhJ070-v5JEAwpcndYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جيش العدو يصدر انذارات في جنوب لبنان</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/naya_foriraq/87033" target="_blank">📅 16:08 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87032">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UElkBGLrN7iVhYQDwDm6-gEN2j3E402khrngthrR0Kwv7X5qW-epIUOiIsbtEkrTnH6NCrquAqT_GMJ3jFIGC8nnggV1fWEMJW1X_ySYxOsfCOw6yJqsEdaGAL-O6oZxiF7v9rAEcLk_CrF5m4Pu2wYIXVr5s8VWsvQFglF7o3-DUCoezhr_CQBuSkoerH0csiu6JWgoftD3ei5dfNw2Ro5Xu7MZTxi2iyU4WVCjJPEz6SwCbhWa8nSLhf0nqfetiYyVD8o64HW5OWDumyqC92e2WLC0p6rBwGxHpzQ7Fwz9qBEJBXRe6w0hmQ4g5DfNYrA7nNzFK6BNr663HlYgRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏وزير الخارجية العراقي يلتقي نظيره السعودي في عمّان رغم عدم مرور ايام على العدوان على البلاد والذي اسفر عن 20 شهيد واكثر من 30 جريح</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/naya_foriraq/87032" target="_blank">📅 15:45 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87031">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">‏وزير الخارجية العراقي يلتقي نظيره السعودي في عمّان رغم عدم مرور ايام على العدوان على البلاد والذي اسفر عن 20 شهيد واكثر من 30 جريح</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/naya_foriraq/87031" target="_blank">📅 15:43 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87030">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40f6ede8eb.mp4?token=dBzZf1sxUsP-jtmbHx__aGxxWg-BIatXLYrdA69ZIuJCJx3Q6PwqVnx_1WaYtbF3lwovh1IdvQjxulQyya5o1R6LZYbiYbqDhHnfiv-NBMbN2UtfzJI76qQDEu_SseX-PWaP87nRrN_0d-wIHqs6hVLYRkZAsKxcxNjo3wvNUBF0-KUVRofVWvKwKr_HgrLt3jTjSLUmjdz-DZGxPBtjWgL4wwfXk4fkbbWZ9pnRfbbSLG4uz2OrPRDv1bmcCznqw1mrFPaKDfI22_7V-9BsMaSy74w6yZ1sa5YDTjOOeRS6RwjIMKDOb5KlUJtyvY0rP2lEPT5X-q7PSL5ubMrXKHM3N6wPna9DXYz_sdRTPfxtPPsvEszQmlLaEXOPJmTk06r6sl_jOVqVktpMGiIWQ-G6IHJ_NBpmynPBSWF7vmD1UKExXmsBoGzQumNLi0NS4FVV29zvYCffCdK5vKlvhaLcwNEIU7pPOiCQoCWupPpZRBr8fbxlPM5vxddl9r0ZMUWkN__-3SjU7Ypvb6Q89NEWJuuuN02UlbFdHeVD1As8KMe0YTKC3C6BGwiwONELAw90ov8Sc9cFGCsD-qaqOwP8j6r7T4DZUvo8mw9PZJkyeqx17oP7OptJeKtI4oXJTlbTvB7BtmIsuDuGg7WhVF7jEUOBEfyzcMaVnfLP56E" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40f6ede8eb.mp4?token=dBzZf1sxUsP-jtmbHx__aGxxWg-BIatXLYrdA69ZIuJCJx3Q6PwqVnx_1WaYtbF3lwovh1IdvQjxulQyya5o1R6LZYbiYbqDhHnfiv-NBMbN2UtfzJI76qQDEu_SseX-PWaP87nRrN_0d-wIHqs6hVLYRkZAsKxcxNjo3wvNUBF0-KUVRofVWvKwKr_HgrLt3jTjSLUmjdz-DZGxPBtjWgL4wwfXk4fkbbWZ9pnRfbbSLG4uz2OrPRDv1bmcCznqw1mrFPaKDfI22_7V-9BsMaSy74w6yZ1sa5YDTjOOeRS6RwjIMKDOb5KlUJtyvY0rP2lEPT5X-q7PSL5ubMrXKHM3N6wPna9DXYz_sdRTPfxtPPsvEszQmlLaEXOPJmTk06r6sl_jOVqVktpMGiIWQ-G6IHJ_NBpmynPBSWF7vmD1UKExXmsBoGzQumNLi0NS4FVV29zvYCffCdK5vKlvhaLcwNEIU7pPOiCQoCWupPpZRBr8fbxlPM5vxddl9r0ZMUWkN__-3SjU7Ypvb6Q89NEWJuuuN02UlbFdHeVD1As8KMe0YTKC3C6BGwiwONELAw90ov8Sc9cFGCsD-qaqOwP8j6r7T4DZUvo8mw9PZJkyeqx17oP7OptJeKtI4oXJTlbTvB7BtmIsuDuGg7WhVF7jEUOBEfyzcMaVnfLP56E" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
طيران حربي مجهول يحلق في اجواء محافظة المثنى جنوبي العراق.</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/naya_foriraq/87030" target="_blank">📅 15:28 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87029">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HW6mjtJySk2i_iQF3SzwC_513DnzvNmhO7yUesybgzbv3i2YHZky1KMXuBgyQJtmfgbyoyhRw83HiDvEFgfCPDP9VM82Lf_u_U_zqD3tQS-Fy4OqO3EWeDq6W0wtPuXOpfPkx_2U_g2bN92LLQe61FsEcp3Qk6UuDQkrVkyBCV-frrwEeSaKjBB_WZcdo_f1IO76xEBFPvrv_4OK1nYMCBVFnFw6LvDrO2YN5lTYyHneExDWCEDp3TveJ1jdsFlFj-XTv3JXDvndJm2ZQkPlfJOiquacK9VLmhuoc9hLQGZb0nydWdzdbM1fz_YNoI1XNhYsFxZKTYWE-wJ1tSN95A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
🇮🇷
تيمّنًا بالسيد مجتبى الخامنئي..
مواطن عراقي يختار اسم "مجتبى علي" لمولوده الجديد.</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/naya_foriraq/87029" target="_blank">📅 15:26 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87028">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">غرق سفينة امام السواحل اليمنية</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/naya_foriraq/87028" target="_blank">📅 15:20 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87027">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UDP7O8Ue3ZShQtdqCAPP9vOvEXSwFiKCxzfF-JDbg0Gkhbt27-YhMp-rglZInXbGdtf9smfyFDpKqMIn93xJ_ylv5Y4crSqd3V9Vkgc9Uy_F1TlXNc4PYfn5oLomTJc3XJgnrEofhd3rfU6LzaPwMkMD3liSOYz0gzQf8baLykFHbcld3KjxFwcuHTMRsc9xyI2haWqEffOKMpI5szTMjYCfp3ZEgZD5PBb_kOHQxXhrJDZ9tcKnkzFjfd0wQo0gRaxtvFxdOQy1KqntI518TYIVvPnUkcsaQtMUKkdc6gbTm4llcHChoWQnPqDjW2OG_KU-cdrBvJTujH78TnhXMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حدث امني في البحر الاحمر</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/naya_foriraq/87027" target="_blank">📅 15:19 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87026">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/naya_foriraq/87026" target="_blank">📅 15:19 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87025">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/naya_foriraq/87025" target="_blank">📅 15:18 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87023">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IOUDiR32Z2dCqlO0PoGgu_ZS4-YAGrDr1fQQKsGHO3q1hHGPRRtAHAZ5T5vbGhHhEYt7iAzCdqc_77YBfy6t_Y_-wR5RC6DdV0Rf26mmYnUZpCwQ50Urs871YZnCydkvgh67jX3CE4fHgj-_VbWMQxOMH4WqbGrjRrbrmPovXlti8Ku9BV9ekV756pyECjsBWDxmA9rw0ukJg_DFJikZG68qq0bHtPGpF_l8BcNreEBsbUontS4zzPJ4E5Fa31ykvQMrAdWXVb3HBHMmnM00BynK3B4AHm7XJMMFJXS9ilUEWc0FNTbl9VxxhFg4_Au3ePBjZiHwVPrWGPvDWnJOOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QMyoyRVzFFFyYtTTo_0VvYZqRMfuhLEgzm6PoE3_bh95N77eSL-HqnM731hNKfNm1dpketqN0UkiyXCneplxSjbkcHxxfufMM58VEh4xLdk5DCsrf7PSVw3DHMkSZTqKbrtL5Mlv9FDVWEItAm2LOveVKnaMyV9-DC16jufBUWsY2ZCLhSZaqrWIJRP_6YLjX78pH2dNfmfmIEsTIGGiPhCzW9PsWnZzjfn2nwXXybOqC2lWqruz0KPzff-p3iKScE-Z5fuhg1ahKNHeFV3suH2141UbZJKA2qwkcmWJ0lfj6zKfxrtluHT9Aez-45iFwpVXBDCL0GB3wOsEOAtx5g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇮🇶
شبكة الإعلام العراقي تفتح تحقيق مع الموظفة "مينا أمير جواد" على خلفية نشرها مقطع فيديو يسيء لزوار الأربعينية.</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/naya_foriraq/87023" target="_blank">📅 15:16 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87022">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🌟
🇺🇸
ترامب للامريكيين الغاضبين من ارتفاع اسعار الوقود:
وضعنا الاقتصادي ليس سيء.. سينخفض سعر البنزين إلى حوالي 2.50 دولارًا للجالون في حال التوصل إلى اتفاق مع جمهورية ايران الاسلامية</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/naya_foriraq/87022" target="_blank">📅 15:07 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87021">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">حرائق وأعمدة دخان واسعة تملأ سماء المدينة الصناعية في جبل علي الإماراتية</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/naya_foriraq/87021" target="_blank">📅 15:02 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87020">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">وزير الخارجية العراقي ونظيره المصري يبحثان أهمية مشروع مد أنبوب النفط إلى العقبة
احلب يا طويل العمر
راحت النفطات</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/naya_foriraq/87020" target="_blank">📅 14:59 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87019">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bNxva3smZtlp0eHEmBnEEhAD4TqycuC9Ui2k8Wy3nk24EdLfhGiecTertYq-Dx4AvLDz8pkKYj7JfEkKQFk5oU3lbZTvg68_vPVgkWY1X2MgrwT6MtrXBS0cyWWsY5Nxwtg9k_1Tyyng4c3JWyIRoUPYilWm7077NVsOx_V7bNlJdtK-9uAZnHomjwclMbSjM22FAVdvhNoQd0Ji1AazcRJcn8dkPGgKKhf-WZZ9IvM9s5pt6eUe-0vpUiy51-5JoY2M7neEABdqtkQXMBrOLgGpkUz0sluTKdbXmFTOwOSCHQJDTO-B2FisTFycm3XyxE_ELJK5L5GijWJ9N6zJSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇷🇺
اصابة فلاديمير تكاتشوك رئيس الشركة الروسية المصنعة للطائرات المسيرة FPV بجروح خطيرة وادخاله العناية المركزة بعد محاولة اغتيال بالقرب من يكاترينبورغ حيث ‏انفجرت عبوة ناسفة مزروعة أسفل سيارته المرسيدس مما أدى إلى تدمير السيارة ومقتل سائقه.</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/naya_foriraq/87019" target="_blank">📅 14:52 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87018">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">دوي انفجارات في محافظة اللاذقية السورية</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/naya_foriraq/87018" target="_blank">📅 14:12 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87017">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">اعلام العدو: من المحتمل وجود قتلى بين الجنود.</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/naya_foriraq/87017" target="_blank">📅 14:04 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87016">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">هبوط طائرة في مستشفى "رمبام" بمرافقة ثلاث سيارات إسعاف بعد انفجار عبوة ناسفة بقوة إسرائيلية في بلدة مجدل زون جنوبي لبنان.</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/naya_foriraq/87016" target="_blank">📅 13:58 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87015">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4638e6b712.mp4?token=vD5rh16uQEBHdaM8e0b_U9ckgLmwblDjPJxfdERoInqNVeU12RF6LyUqGJeaE7RTsfTlKAzowO2XLMcLlwzNN0wbRoFB55lWDVsEZ5nIAfdMJMQqs6N8dm-jIvbBgZpNb8BCbYz1jidgmDudfhmSM8SJpV4lcE2TnaC9PKdywEXTbN3umMwLrig0tL5nIK7Bt4AzZ1erXBdJ0H1YGhzBADa5q5MpClAum7TfiEImEgdLg7gJOIiMvYYxwnDpTpo-gHl0VAMKkIo--YkaZTZm6wqOk9nYXOTayV9QQIj5ojUK9i3-x_O3OY19NVK0IMq6O4e1alA6MAxQ3ZNb0SfS9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4638e6b712.mp4?token=vD5rh16uQEBHdaM8e0b_U9ckgLmwblDjPJxfdERoInqNVeU12RF6LyUqGJeaE7RTsfTlKAzowO2XLMcLlwzNN0wbRoFB55lWDVsEZ5nIAfdMJMQqs6N8dm-jIvbBgZpNb8BCbYz1jidgmDudfhmSM8SJpV4lcE2TnaC9PKdywEXTbN3umMwLrig0tL5nIK7Bt4AzZ1erXBdJ0H1YGhzBADa5q5MpClAum7TfiEImEgdLg7gJOIiMvYYxwnDpTpo-gHl0VAMKkIo--YkaZTZm6wqOk9nYXOTayV9QQIj5ojUK9i3-x_O3OY19NVK0IMq6O4e1alA6MAxQ3ZNb0SfS9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هبوط طائرة في مستشفى "رمبام" بمرافقة ثلاث سيارات إسعاف بعد انفجار عبوة ناسفة بقوة إسرائيلية في بلدة مجدل زون جنوبي لبنان.</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/naya_foriraq/87015" target="_blank">📅 13:56 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87014">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">إقليم كردستان يقرر احتساب كل سنة من خدمة عناصر ميليشيات البيشمركة بسنتين ويشمل هذا القرار جميع سنوات الخدمة الممتدة من عام 1960 حتى عام 2003</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/naya_foriraq/87014" target="_blank">📅 13:43 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87012">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/k5RBt4Ib1UECQTfgrpj4Bb4F7DbjUX3O570boB2BovdXuYpNaaGyhwRz_wjLwykFS4AuCktt74ZvIjpc-HE8VZ6DONqNT_0f6JxXhP22p7vfAj-KKifb8CP68HpXSx0Pqhz_szxWy_vU5HlLjW-3GYw3WFL0pIPUwwXSTLIbkO-xdLc0fzQzr5-Hy2dwpGwp6-LLJLADkmeM3i3fHZE1XQZ3OtnoFHS9l06O-h2zpBcpfI5ZoUa_iHWrkZNqFffes1-grAHyluzaa8Xpmr_4nxBgoizg4baqGYEI3fE9IUA2_0Gg5aF-hvxY8O1AltQjcj7qf6YFfRoA3c7kRWhDTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FAx4IcF56oWTmokwzs3AY8Ftbf9Idv9odEErSPAOWTFOoK_lu6C5G57qN_BIAcaBKPst8ox6neeZBjiGTg0oAIOJiWjIe6TLXL7x1Bnq0N6Qr6Hw7DEDdStLZZu_kMwiBlXzo1_3pYOjblmgeLDe33c9gYNXqJ1B48RciAtKlUFWY7wLSNaxR_sc9j98vV56iXjYInmIrI3Sf7WnSrgRNdqo4gVZCmLcTvO6yVSVQyPlLRgmQzenmehDBf62lsH5SWIm_OmlL2Qy-SuKU5wJJRoaPQtqkakPfd6N4nIudEJbVb7LMHfkOUiP7l-1aOPHdx7ZoQ3KjNuUdfTLi5KmHQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇩🇪
ألمانيا: اكتشاف طائرة مسيّرة مزودة بفتيل متفجر ليلة الأربعاء على أراضي مطار لايبزيغ/هاله، والذي واجه قيودا في عمله.</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/naya_foriraq/87012" target="_blank">📅 13:35 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87008">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N3jyx1gLvo5apdUwJ7TmSjTrR-T9ksstcHISvEVR6TUSy2o6xRIxCifGUhPlRdkopJXIknMcQjyWHqpK_IR1xjBHoJ5Xcm6GsZi_iFGjtYJf7EYCPzQB6Bh25LqNORwguHZ_dlTP9Z47stZ9SkMlTIoJBzbp5gjdfS8q1gCBZSPGMYfBTPHfhlmbvh7_HztompWfKldM-dSEO3oI9s_bqCKz2PigYahXSJC_AGR7Bwn_vQSyg49p2UjloD6hjyYpUSwkK7KZOG2i5HUXNSF9oLDYfQOQ-ziXSQC2_jMsfx46hr9NIFYXi8ftUjoxGmCKk3oBxl8uf14VYkxxMKSRtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">إنتحار المعارض الكردي الايراني (مصطفى قاسمي حسنون)د في ناحية بحركة ضمن محافظة أربيل أمام مبنى الأمم المتحدة اعتراضاً على عدم قبولة كمهاجر سياسي وعدم توطينة في دولة أخرى كلاجئ سياسي</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/naya_foriraq/87008" target="_blank">📅 13:27 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87007">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mVYOwR-_hJFnjjWTpis6QdPqgj5Quwffarbh2IxKl9N-JKyqYAA0WzjHexcxzxQAG1iChc09rwvkRtZsNUha7wyMShdVgFhvo8QJ5-t_RGjTSXt2qSapYwSpkyiuHca7OAJLBXYeyZOAFr_tU4QdQ5P3wlhLN-PcK46XuAg6-7atmRR5oiKsYr4UIe97LMCdpdSjV8BGJqKtJcWneLw5n8YpShZgKMWlIlifPZ8N-gtApmxNKZ5b9Pus6StRcBabYdXT6NeAcyjfow7fDnR3bs_7aeCDLSHKimcTSwHiI09N4KFTj7Sx0srMA0Dkfn63DYuD6UqnizqhM_P7AD8xfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">More time , more 48 hours softie
😆</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/naya_foriraq/87007" target="_blank">📅 12:07 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87006">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F1mfVwcEPWswCE-yEbsR9EsZ8puDsEYjxqO1GLq8ExdypG-Ki5crRdIyjG-J9ksmDSS9JEXsHXvyh6Ecibaz3zzxuPOuiIukBFUh-TCvuPUo4-BeuxVIGF3Mrmu9UB-TUYv4pbTqwPHPsvenGKdjKB3CjU5DukKwugJ44YAa1XVO02IJUcDLGTGDdyByDtQB9ZxGdWHjB8-lgBhQJyDB2Sv11nGDKJfvtYZt7r7BTRUSWJyyiIzfq2xJHChFtviLHhaLkZJcHSPi8Z-oenwzsuu1X7V9bbqqYEYAZaVzmuG6yH-aKKdO-dv1ZufQhh7L5vdcQVx1s0mwpE0ZqbrfVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
🇮🇶
شكراً إيران  بموافقة الحرس الثوري ؛ عبور ناقلة تحمل النفط العراقي من مضيق هرمز.</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/naya_foriraq/87006" target="_blank">📅 11:58 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87004">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🇩🇪
ألمانيا:
اكتشاف طائرة مسيّرة مزودة بفتيل متفجر ليلة الأربعاء على أراضي مطار لايبزيغ/هاله، والذي واجه قيودا في عمله.</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/naya_foriraq/87004" target="_blank">📅 11:34 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87003">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iDNPTzJ04TgjKay4J1xgybFGO-d4x-Rzs1hK7yLBUaCpTdJkCALGXjcJo9RjAxnheqvJNDffrmltuuZPLqX3J06FjEOSvXEkmmPk-R5ORlQrclxrrdRwvQc6aiEfnsAAXMAbY7j40ilCuXSDGncXlLFwFMu820qDC86t8m0RZYIvKbUQRChWouDItcRlxCFu947zLpa32suo23H-5CvZF5HG8z2-JKOnyJ9vDdiSD0RUPlX0CTpLkhLThqRNP3DHrRQqg9g8IxD7teP_U7GI1uMnk1RQ-RXN95EyBVMOHTDrellKfJl0Vqj42fo9zgYszdqIQDnSiohzrLCDqg_gmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
🇮🇶
شكراً إيران
بموافقة الحرس الثوري ؛ عبور ناقلة تحمل النفط العراقي من مضيق هرمز.</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/naya_foriraq/87003" target="_blank">📅 11:15 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87002">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🇾🇪
بيانٌ صادرٌ عنِ القواتِ المسلحةِ اليمنيةِ:  في إطارِ تنفيذِ قرارِ القواتِ المسلحةِ اليمنيةِ بحظرِ الملاحةِ البحريةِ على العدوِّ السعوديِّ وتثبيتاً لمعادلةِ الحصارِ بالحصارِ تمكنتِ القواتُ المسلحةُ اليمنيةُ بفضلِ اللهِ منْ استهدافِ سفينةِ "وفاءَ" النفطيةِ…</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/naya_foriraq/87002" target="_blank">📅 11:09 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87001">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">ترامب: مضيق هرمز قد يفتح اليوم أو غدا الخميس</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/naya_foriraq/87001" target="_blank">📅 11:05 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87000">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ix1sx38owcLxOtEtEpedkkGaSxIKqr8JqUb-1q7sK0IK_y443yj1DYDZgp0b852R646vF3ZstsxR6iaYR4HQWG8KMxT6k8Ijg0XSVNayUiPzN-Khj3Lv7eJkZhB15N3Hl6N5Q76TlY3smftq3q1qhyVKpvrnW4MAohnwHrTscSJ9m9NuHgSTsXLQ0XflFlu-NIMeGtWErpL8wlWeYwG5wtxoBV-B01Lnzj21pFNM443C8ugBrumE6w2AqZIDcxs_kYo46cDDBjQL6EpeCto1AbZfMQeqNRfvhI2TA-pmm0JnLcVSD2OnSodclNCLnhGYnaeDoVuFaR77yZncqKqS6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
استمرار اندلاع الحريق في سفينة تجارية تعرضت لهجوم بسبب مخالفتها لقوانين حرس الثورة الإسلامي واشتعلت النيران فيها أثناء عبورها الممر المائي قبالة سواحل شبه جزيرة مسندم العُمانية.</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/naya_foriraq/87000" target="_blank">📅 10:34 · 14 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
