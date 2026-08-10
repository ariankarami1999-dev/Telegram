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
<img src="https://cdn4.telesco.pe/file/vaRanIZNDwf-QqZfTsARwZwpyuHFubtXuM08ej6fT4jwyu3azQKFU87FAb-_4b89rf2YYubXM3C6xkPWc3K6Qikr_VvKWe1U8Tq7fzFoDC2B8WS-eT9_7r06HCZG32Pb8hoIZmBwfVyZ-4VHcp0rEghtzDU59J4TEQJvLMgFZwA8L9Ss2u3TneCBcWBO2GgakCcHAfuuo7VUKsPHZ6yCQAQEdTfLsM7CCYJ-9HJd5iPPVieocTVisme8hhYXk8BF6bF-oJMI7pmT-KNsxkB8cgOQ1NdOV_iaO1AFIYrLkAvoijhmFKVXtL9-gfZNCMyumURwLEUavQ2JvnUAseef9w.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 273K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-19 10:18:45</div>
<hr>

<div class="tg-post" id="msg-87440">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">هجوم بالمسيرات وانفجارت قرب قصر المعاشيق بعدن جنوبي اليمن.</div>
<div class="tg-footer">👁️ 7.2K · <a href="https://t.me/naya_foriraq/87440" target="_blank">📅 08:26 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87439">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🇮🇱
🇺🇸
إعلام العدو عن مصادر سياسية: خلافات بين الولايات المتحدة وإسرائيل على خلفية وثيقة الـ15 نقطة بشأن غزة</div>
<div class="tg-footer">👁️ 7.74K · <a href="https://t.me/naya_foriraq/87439" target="_blank">📅 08:15 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87437">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🇾🇪
🇸🇦
مرتزقة السعودية تعلن عن مقتل 7 وإصابة 30 مرتزق، جراء هجوم يمني بالصواريخ والطائرات المسيرة الإنتحارية طال مواقع عسكرية في مدينة المخا اليمنية.</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/naya_foriraq/87437" target="_blank">📅 04:48 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87436">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🇾🇪
🇸🇦
إنفجارات عنيفة تهز معسكرات مرتزقة السعودية في مدينة مأرب اليمنية.</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/naya_foriraq/87436" target="_blank">📅 03:50 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87435">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vVzxXobTMZPOSkFauxa1H4V978UJipXIw-C7kEhH85uGHgcwYTgXQE9NAVaHcdRWWqHqbiVghKzqOR4CFFikUL9L59W71NDk1_al2gaHcgvantJgEGU-1vl0yJm_W_81UmE-UT4FyBql15BBCZd3om9QXnXMNiLrENEmA1ZpwMxbgBTWbzTBwwhrQF_aiSeImw1IuXskv39hHOMZVRX9AWgA4l2elYu4v0ybp0BoP4mCvzpyVXyecmHCO4Lbx_zqb9rPNQb_RKGhoc8JX0-opzoxSvltr7CM64Q7xnMl6rUU5LpDFXJ5_O4fsLDIo6iWdIuhuAsZ6wuPGxe2PpoZvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇾🇪
🇸🇦
نتيجة الهجمات التي تشنها القوات اليمنية..
السعودية تستمر في إغلاق مطارات جيزان ونجران وأبها حتى إشعار أخر.</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/naya_foriraq/87435" target="_blank">📅 02:47 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87434">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oQOEmV80qhpPWDUwwR-w7P7LRVSJWP6SoIzg9JXJcg1qS2nkZqjgRoTiF2uKOZoe5JStAcFXWCh7lR01ZKb4icSAuT0qD6Z5PFtPofA57kyU1MRfj5-WI-YjlTnaZ-EX1Xxnzn_RQ6xBheM8Yple4xFyL54Xim3kZ-YPb9EI1vJE6goYBgJAKaknDKP5U3swsseSBOAIrVyTXTNZzYITx1S5pBFZWy_VMyf1CG79IU0M43-nFGdOXtKFvZSHcNRXV2mkyO9cfrAD4kvYwZcd2l2L0mzQID4wEPZZM-ken5xTTi2vjtyb1Vscvnnbe71ggSeGT6ro0rv9I8co7XYT7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مشاهد اخرى من السفينة المشتعلة قبالة سواحل عمان بعد دكها بالصواريخ من قبل بحرية الحرس الثوري.</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/naya_foriraq/87434" target="_blank">📅 01:39 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87433">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TkWCXfEXvkuA4_ml4hpVtUk827EQBgduc9GbCdpzfwCWixGM7OxuqN9gZxr6yrsyMQ4u9dsJro65aBx3Weu1zQ-Y7Njsa7HeBrpSulv4-Bd16G_CZT9T_LNBseMSjhBd0CX3-60_Z6wE1k5q3ny9NR9tCAHbYq2DlRvjgGkZ_UTP3HvmI6oaRVAj8Cyg123wuKdRJ8Qu3jWS-48lHBTBseDGIu8x1Dt6JXMdPISvxesclFV0xkgzLdTB4QCGetCBhPHZYOnmfbC1QFg8fJ4dtz7_-Qz5qaJZWgRisTgSmYJwkYv-J6CsbFTw_D0Zk7pK4ZPdjKhI5V5BEjWXq_pUSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
🔻
تعرف على محسن رضائي ؟!</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/naya_foriraq/87433" target="_blank">📅 01:37 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87432">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">الحادثة بالمختصر ، ووقعت قبل أقل من ثلاثة أسابيع في محافظة واسط، حيث تم ضبط سيارتين محمّلتين بطائرات مسيّرة.   وهذا يعني ان الرواية التي أنتجتها قناة العربية السعودية هي رواية كاذبة بالمطلق واستخدمت صور قديمة من واسط وركبتها على بابل لأسباب سياسية كون بابل…</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/naya_foriraq/87432" target="_blank">📅 01:32 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87431">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">مسيرة معادية ثانية تم استهدافها وإسقاطها من قبل الدفاعات الجوية الإيرانية في أجواء جنوب البلاد.</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/naya_foriraq/87431" target="_blank">📅 01:09 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87430">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/naya_foriraq/87430" target="_blank">📅 01:07 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87429">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/naya_foriraq/87429" target="_blank">📅 01:06 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87428">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0db1cb8610.mp4?token=mR1xbo0KTYA3wdNfmZm3jdMlwDjo-Rfuf_CVFmZ30R497v_2_dJN_elKllh62RWySBJfft0kQgZFnXZ9tdyzJda5CXk_DiDh4u8mTLDXYO2PTWMqpG-E14_D9GUS-oyiex8dqQlnUgL7-E7eFNY9Cbby3iP5v7rsKL0KWheCxwY8SL0Z8OubX_gPfs6Z80lkk88H-zOK7xXJH6FjCALuMf-Gl4ZDGOP1PLJaZNdv9Y__kxG3FnRf3crIib-7QLXSkpqjjWWbVb_2NDv4UMvk4wK4KBgd_OuKgqjaOOREy-Pz73---hfXp02_ID58oOOFKD1UG0mqPrgXp5tBGOWlLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0db1cb8610.mp4?token=mR1xbo0KTYA3wdNfmZm3jdMlwDjo-Rfuf_CVFmZ30R497v_2_dJN_elKllh62RWySBJfft0kQgZFnXZ9tdyzJda5CXk_DiDh4u8mTLDXYO2PTWMqpG-E14_D9GUS-oyiex8dqQlnUgL7-E7eFNY9Cbby3iP5v7rsKL0KWheCxwY8SL0Z8OubX_gPfs6Z80lkk88H-zOK7xXJH6FjCALuMf-Gl4ZDGOP1PLJaZNdv9Y__kxG3FnRf3crIib-7QLXSkpqjjWWbVb_2NDv4UMvk4wK4KBgd_OuKgqjaOOREy-Pz73---hfXp02_ID58oOOFKD1UG0mqPrgXp5tBGOWlLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاهد من استهداف سفينة واشتعال النيران فيها قبالة سواحل عمان بالقرب من مضيق هرمز.</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/naya_foriraq/87428" target="_blank">📅 01:03 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87427">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HzX4e4ooYOhNrkqvEfNe_wuaNy8ZHQdnMiWAVOlpnb8DPOfNbwF3ePYDONCN7D4RoDACcy6grHJ_EUnrUvbeH6mqWRDvllH8Zr4DrlHCVXL9X1E0Cy8HFjOVsXpjulygMqk9N6lw_juR5cJCCfPWcwzXxX3rP08b54LQpTE4fyjPBwSuKc_-6HUNpUnz5ioMrWEWPngCOI9huO1xWqjg86HLjJVJ9ZjbtXYrlmrGDTR95AwoAE9owTadIZUEcMuGPxe8R99IfzllepK4FG_s9806O83kogVWAz0GiaBS2tz-0uix6NQIb-kp8pwjypG9gnaQaHqatFyjezWT53xr-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامب يستغني عن فريقه تدريجيا
تعيين ويل شارف مساعداً جديداً للرئيس ومستشاراً للبيت الأبيض، ليحل محل ديفيد وارينغتون الذي سينتقل إلى القطاع الخاص.</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/naya_foriraq/87427" target="_blank">📅 01:02 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87426">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">مصدر امني لنايا
عملية نوعية في منطقة الكرادة خارج بالعاصمة بغداد ؛ العثور على مبلغ مالي كبير يخص وزير العمل والشؤون الاجتماعية السابق .</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/naya_foriraq/87426" target="_blank">📅 00:58 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87425">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">أنباء عن أن المسيرة التي تم اسقاطها في أجواء جنوبي إيران تابعة للسعودية.</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/naya_foriraq/87425" target="_blank">📅 00:53 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87423">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OKLP4ugmHA09hLkQ6vrXxJOrkaTCPI2Yft1YgAMdaEUObhDsUiBAtF-THBkbJ3mcPBQRawMZGb-y7qV2iA5WMOHDoR_HWXOZVff4pB60wxLvvp0d8aJZq2Wl4dV30PekYqG_M-Ei7MuCxsfdhBQ5_JuJK5jTLnUk6bp2GxV8dP2PTXSwqDqUIO0kc5fZ6p_jJhdz-KtttSmjk45TDlqkqr71FB2amSl6PvL7H-HYvTiLb1pY9jSsFkhganezKjBchUNBHeRJEuBH-5rtmakUqBez7hWxRkr1vhpLN-gqNgQcREnBMkTgWyjPdL6Ii4eZcmcmgQJYYhgSAEWL2X9OSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/94eb35c039.mp4?token=nqKammMKb-VA55AAbHvZKVrX7wAbl0q1SPpNS7ufrmVMy7W-wGcaei9QwcF-CRPpKvGQ8Ieb7o-LNAxhJM25mm5VA4_hFAF0IH2aBT2J6zWaSf17FdodRV4IJw9jm3qE0LhdsSM2Al0oaaUQTX-4AcNCS7kgyjIH66qg5TYGukvANgCtuS2ljs8-QL_LT0181TtSt-VGF24ySd7Ve9tYFJjShCXR965aBQ0FvyOhIKA5sgAVebIjn3LoC33FWVu2pYDX5pYYi5TQo8ctmfr9eYbI_9pSWHWib4Q9ahdkDp1Kzk6hHqbgi8EbAnz2OVMP0jzA9jocs-E19CauCJjJxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/94eb35c039.mp4?token=nqKammMKb-VA55AAbHvZKVrX7wAbl0q1SPpNS7ufrmVMy7W-wGcaei9QwcF-CRPpKvGQ8Ieb7o-LNAxhJM25mm5VA4_hFAF0IH2aBT2J6zWaSf17FdodRV4IJw9jm3qE0LhdsSM2Al0oaaUQTX-4AcNCS7kgyjIH66qg5TYGukvANgCtuS2ljs8-QL_LT0181TtSt-VGF24ySd7Ve9tYFJjShCXR965aBQ0FvyOhIKA5sgAVebIjn3LoC33FWVu2pYDX5pYYi5TQo8ctmfr9eYbI_9pSWHWib4Q9ahdkDp1Kzk6hHqbgi8EbAnz2OVMP0jzA9jocs-E19CauCJjJxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">استهداف واسقاط مسيرة أمريكية في جنوب إيران</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/naya_foriraq/87423" target="_blank">📅 00:44 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87422">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/naya_foriraq/87422" target="_blank">📅 00:42 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87421">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1dbf391292.mp4?token=cCZLzvw0cUsWGivrqzX51XRAPBQPWwDt3g9i78XXod_KlSuAnDsJpsOyRM2xqKpob-84BvbourA1QuBRKLjM9SfiZ0h1ZcgMgGt_5Jjrf8zi0PhQvfxRNiu2fNJgj5wpkC9vByog4SfKzw-X2Kwmq37HTll5lEEA6UUxWjP7ocqjhzOhbvx3ek03zBnunW8HUywMywxR-w8rbrhpG7ywiOrwtkWt3tQERJve4tO28SfZzXM37GCK0LPkDT0G6z0lsEOw93CTWZnOf4e-9dkP15dTKyXKF-mf9XuzdyJwaBQHbd13Lw57vGN3k4ntQER3rEZgAzK9hQEADf5LUkTjsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1dbf391292.mp4?token=cCZLzvw0cUsWGivrqzX51XRAPBQPWwDt3g9i78XXod_KlSuAnDsJpsOyRM2xqKpob-84BvbourA1QuBRKLjM9SfiZ0h1ZcgMgGt_5Jjrf8zi0PhQvfxRNiu2fNJgj5wpkC9vByog4SfKzw-X2Kwmq37HTll5lEEA6UUxWjP7ocqjhzOhbvx3ek03zBnunW8HUywMywxR-w8rbrhpG7ywiOrwtkWt3tQERJve4tO28SfZzXM37GCK0LPkDT0G6z0lsEOw93CTWZnOf4e-9dkP15dTKyXKF-mf9XuzdyJwaBQHbd13Lw57vGN3k4ntQER3rEZgAzK9hQEADf5LUkTjsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ضربة تطال سفينة مخالفة قبالة سواحل عمان</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/naya_foriraq/87421" target="_blank">📅 00:42 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87420">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/naya_foriraq/87420" target="_blank">📅 00:41 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87419">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">انفجارات بالقرب من مضيق هرمز</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/naya_foriraq/87419" target="_blank">📅 00:41 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87418">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">انفجارات بالقرب من مضيق هرمز</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/naya_foriraq/87418" target="_blank">📅 00:39 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87417">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">مصدر امني لنايا
اعادة انتشار وتموضع قطعات جهاز مكافحة الارهاب والشرطة الاتحادية في مداخل المنطقه الخضراء وسط العاصمة بغداد</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/naya_foriraq/87417" target="_blank">📅 00:27 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87416">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">سليت سيفي في سبيل الله #سالم_المسعودي#100K</div>
  <div class="tg-doc-extra">العباد Abou Al Fadl</div>
</div>
<a href="https://t.me/naya_foriraq/87416" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">سليت سيفي
#شاركها</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/naya_foriraq/87416" target="_blank">📅 23:34 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87415">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🇾🇪
انصار الله يعاودون استهداف ميناء المخا بالصواريخ والمسيّرات.</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/naya_foriraq/87415" target="_blank">📅 23:34 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87414">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🇾🇪
انصار الله يعاودون استهداف ميناء المخا بالصواريخ والمسيّرات.</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/naya_foriraq/87414" target="_blank">📅 23:26 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87413">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">مصدر امني لنايا
العثور على مبلغ يقارب مليار دينار عراقي في منزل مدير الشركة العامة لتجارة السيارات في العاصمة بغداد منطقة الوزيرية .</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/naya_foriraq/87413" target="_blank">📅 23:21 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87412">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">مشاهد إطلاق عدد من الصواريخ الباليستية والطائرات المسيرة على تحشيدات العدو السعودي ومخازن أسلحته في المخا</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/naya_foriraq/87412" target="_blank">📅 22:58 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87405">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/H5ERs6tA0y5jUklcFjglIHsAtjMVnjU4pe44sFbJIjeFQ0G-p0yjS_dKziu4uNrs6bn7hul23lYuCaobPkCQ_TpYTA5Gyz4o5rd9oQxpHH14-El23r90qFDgjv_5mtbwNkRRu0DbPfLyN3GpnBOXD6WOtGn3MyNvYkfQLxf5yic1Fqk_RC8QVlechqNpyUpNOSDyu-DA0nsv3eI6zkB618P4l9EG00oEFXNaIcSzgppCFBzcOdygRalUURfoF-29D-dX723YrAd3pJfcjg3WqDvZrvlRSjgUhEaoZgpPLdfEkMDt3vkrQOTreV8YRiLIq9Z4nEePi5NQfn01TqW7KQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/a_w6SDkp0O2YG3kTL_jdgwa8aXCFrSJYO7QbjMYrg6O1OrrBls8vAO6fiEWXcLslMZLRmn0aGCKftEUNCjH3bXWzxHpj24U4E5rIq9bii9ZyBKmcEng2YA-RWHpWTn9FppAUZmWg-XIN9setb19YPEl7F5L15Prtw_bOe2nkShPPSOKwGjumNDTVDU3sR5l8hRPEGFlgw2BS21mrv-iQLRKDZuFHSFT4dR_DFMiJYNn13KRXsgIzQsIoJraslWX63PaaZzJDHhZXxfQ5MvkAtohmiwNE1J9FyYdsel0bCW98DZy4L3I96yiH6U47fLZ0s3DOi2Cxxl7fGfHMUBnasA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PIunMt-jlz3nkIKGkS8MvVvo3NIqb5CyXYEJd-R2zb_0rbpV9pU2rwvw6vzp73c3sOk4twlZk9qyAE8AmiRwRrFrsiEzo31LW4_4I0ks8DpJVbai-8jL_Lz62HZUM0yaYffgoI4yTEMs98NcNc4InjCGPN6XFleYfG5fzqJxfgtPS0PnxYCNkASZ22lzhq5uJgJ3e_HPPmvmtPHniWVu6RKUAIxBPhzkq_tkbL8Xlcn5sz8EUCuFpenurUtJzqHCER6B71RNdP4OX1xeLNLRIk_aiRw-555dVK9J_ouecSHE2U-2toXDomoPx0gqgT9pBOgGRVG37WRBO5TlyhwAwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/f4zXouxahclXqyBR9r0o-VDExzFElHCH9kQFUHF5wz8v61RgDk98jQOmI_6UcGpM2paR1E0-7GsZR0STCBD1QWrS2nrefd15fXS2fwiDB3ts4ewdOr_3UksJmReHHID_z_kO5f_J64yaMoDbZA1MS_Rolwq5lNylrDCv_ReOyVLxYJqBxcvKLIi1iGTo-vZLd7gIiU0koZvYVeJOMw_rPmsgMAkJJKWQEP6K3jz298dqCuagEgyxVHxrlmWMc1DLbzUhYWo_OQiyAq5xbxI44sTl5hd9mR9g1eL4TIqGkNF-tpMZBhlZc6p0mLWRJv6bdVb1zA4fVH_HJ0bQ3Mp0Ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CLxkTQs0xPVMu-2rycegDV8pQf6CRucY3UoGDw0VjXDvXVb02yVJJnaVfEel8M5J73-abt9QpM9RADtDo3gufBzgPeSRU8l31xg1qcNqPSNJZa22rhL5B9byUhIFBcNej_5GbLh6iO5vEfcwnhWO-OA6kn6I8MF12mRuh8jAmJu82tS1vSH6OTKRFuVFvkWbz91QfR52oU2ZIRrdKzENTS9ViJYJp-yRu0qKWBshqOn4J3CBr5xEWhosg6YiA_zFaCPeSUb5rPqwRW1yzt0Fvq5plMlZi3CXt0vBty-hZ9d5RwwsdIT66aTXSBxktAlvpowOyf1_NOk8qi792LU4lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/g1JV9LfIs7VUDFkFtmmXx_6SeQgoJBKUXnLWWnD_ubh-I6grGvBO9ATz42AT9MeopBJSDSZc0dzC1KB48ZAzxhVbDJV9OzInONEpyc1xSimWFf9-ssFIXbd32RldvYHjfmn5MPldCmhW0hlG2KU7-bXpB8ONLfdNtZTOF2Yavpz3CP_7RCGNdGlFSX7_oLT0j3oW-YbEHN_8ipBgnm8oWST6bc9OQmDqDd6FMJmdqRF7mPno4nOlVgop6ybUDlNyeuihicyiayrEOV5Hh1xGpK2UlNby-RQX1Y9VvCsMTdbrkqBy7XPStUF2JAhf7nnjoJFhXVz4uuPg3H7Om0fndw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/C1puQVV-r70zGsl-w33mtNHVtcT08NebfD-lge6mLh6_coI4j85mkTZx3Hx8RftauqCONltT1zg76dLeHxflfb91gCbd0HUMgmnUhAMnmwv0Re2uQ_bregYc_OIwUtMaJSVTCkLQWT6uPd7t3ZyuoOzKgdRYuCfWQbjuYoRO2xyWrRu11HazuRTrE87Mjx1aQs_Y6FQybDvpZ9q98kEAAnLjYkSpQBiQnFu3xDTzk2puL5uTgbJCEQW0GJcZGx8wTBqDW9zuA-kSGwbqH2RHH-9vZ4eA5nbSL_Xi2oQJjf-76EqkMIb_oh-blnjle8MYTv1O0uS0SldTWD-87em3ew.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">صور | إطلاق عدد من الصواريخ والطائرات المسيرة على تحشيدات العدو السعودي ومخازن أسلحته في المخا</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/naya_foriraq/87405" target="_blank">📅 22:56 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87404">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uP-aUemVmpkEePkNHU126XBarxP1WKdU9S-RcLrYt0-LdcLbPRyP6SvgF2lskM6AvNJAPEFvznz-BYYqs7cbOBd0FrAIbCfCAumHbxB1lEle2M6hDCdx6oSdvz0FBiS3KMlsW7g1Io3KrhxEVmKxqfQCNDqgH0JBQbNT7TwFOlUVHic16WFsH9T1wDt56g9SBUmvcuchBQ0WXvvY7zhh3IM_BUR9nWjWqib4PBJsI2it7ouUfHX18D4e7NGHxm8I5d7-w246efIU6wH38eNToxyLM7ExKlXHtUvOU66atf8Yk_AhUpLC-tQy-9Y_ZbDvcsQha24Wq9Fj_6OoKAa_gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇾🇪
عضو المجلس السياسي لانصار الله:
وجود كميات كبيرة من اسلحة السعودية في المخا تحضيرا لاستخدامها لقصف اليمن.</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/naya_foriraq/87404" target="_blank">📅 22:50 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87403">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🇾🇪
بعد قليل.. مشاهد لإطلاق عدد من الصواريخ والطائرات المسيرة على تحشيدات العدو السعودي ومخازن أسلحته في المخا
.</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/naya_foriraq/87403" target="_blank">📅 22:38 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87402">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f6d683e056.mp4?token=nFYE9f0AxopxDwua53luXZWNZyrErghN5mkqR1DFFuqOAF6j6HcXU2qfmSgxgUDHzpQUq9r5x7xy3-mVwjhY3Rd9eZ1Iay6fct1sQaNUlwmSGVNS9g4jKQaGDl1TC9phxWuV_DgPOo_CItUR4XkIJlCZyGM4YvGnHg294_lRzUj_M6d8H4SOAF2JJryKSwaYAH37AZIHFS1ySmpYbVSnoT601n5QzPwdU25bxsqW22xHwbWlIxoOOWGlgntSf3og1EJeoEIZWfuYkOATUi9aLMNaiHzEwSg3vr3-kzpFCOx62ngkewZhNOWAo9Ex9xaBlv5TTIg6arU3CHbuUbY5eYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f6d683e056.mp4?token=nFYE9f0AxopxDwua53luXZWNZyrErghN5mkqR1DFFuqOAF6j6HcXU2qfmSgxgUDHzpQUq9r5x7xy3-mVwjhY3Rd9eZ1Iay6fct1sQaNUlwmSGVNS9g4jKQaGDl1TC9phxWuV_DgPOo_CItUR4XkIJlCZyGM4YvGnHg294_lRzUj_M6d8H4SOAF2JJryKSwaYAH37AZIHFS1ySmpYbVSnoT601n5QzPwdU25bxsqW22xHwbWlIxoOOWGlgntSf3og1EJeoEIZWfuYkOATUi9aLMNaiHzEwSg3vr3-kzpFCOx62ngkewZhNOWAo9Ex9xaBlv5TTIg6arU3CHbuUbY5eYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حدث امني بالقرب من نادي بيدمينستر للجولف التابع للرئيس ترامب في ولاية نيو جيرسي.</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/naya_foriraq/87402" target="_blank">📅 22:20 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87401">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jud29CwTfugboOkwU5jJ-xSLj8I69nQLXZfcrUTlN1qv1UV_bwQOF8klBcBHDi8pQ24wXIY2Yd9CRxRyfQKDRtjdVkmetXQm_z0DZyZUE4kZ3Fkyjpqa0FmcH-taHTcaNnidz8u_LwSgjPC3frqiIfyarDCwfxcm5TUFVRJ47N9xUmYCvP71YMcGH-47Fo7xw9ReAvCBlNvqBrC5z09-tO9MoVaxYGRmE5riVN8Zj2S52JyMtXoTwPwQb6qb4oS79Jq3HXoT_c8KAsCwkbfsynjPCS5fly8JYx0hZrnZM8kuUagnhicWUwwQIbp-Fq-qxgRseHuS6IFCBAfEVvrcFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/naya_foriraq/87401" target="_blank">📅 21:58 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87400">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">حدث امني بالقرب من نادي بيدمينستر للجولف التابع للرئيس ترامب في ولاية نيو جيرسي.</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/naya_foriraq/87400" target="_blank">📅 21:55 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87399">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">حدث امني بالقرب من نادي بيدمينستر للجولف التابع للرئيس ترامب في ولاية نيو جيرسي.</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/naya_foriraq/87399" target="_blank">📅 21:54 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87398">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/naya_foriraq/87398" target="_blank">📅 21:54 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87397">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Audio</div>
  <div class="tg-doc-extra"></div>
</div>
<a href="https://t.me/naya_foriraq/87397" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">اخ الشهداء
#شاركها</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/naya_foriraq/87397" target="_blank">📅 21:53 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87396">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PUp16iH4plDj9MeiOYzGMWzDpr0-6vnoZw_X36PKm0W9Q7RQxPq23lNpps7lrkn29srKCRzs125e3JE2fv-8sx3H6z3b2EP-Kaddo1BJ79eSiYdJkxXfvHZhkxjVzKT11Uq_5RXvc5vTlQClhJEAWGvbSDBCDfoOrhETvYE0cY1iWsitE9MiKpZey9Zxze4b6PSVW57UT6S6f4I2FL8DKHF7WlzARDWFIXn4VXO1XJg2T8AtAcpAUVd6ku6hMmO9ABKAmpZIaEmTwPmT-XlzGPVlysgShNop5Kf6XmyYlb990rzyNCZEgQCMAOZZrAIFtafAQiyHqxXEZIUXsydRxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#
توم_باراك_السارق</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/naya_foriraq/87396" target="_blank">📅 21:40 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87395">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">▫️
شقشقة هامة لذلك نسترعي الانتباه</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/naya_foriraq/87395" target="_blank">📅 21:36 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87394">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a679b54bf.mp4?token=TdG-W9-DIfmY-wLBzlw0ISZXB_6mSTAGz-cwsuhhM26M0GhW01upaHv_liutsTYG6uDQ_yhiIHNzhw3bhcqvpeGta2j7dLkudgC1SeXvwUX4HV9iKoEfJWmCGd-W7VOScISvksyZdTolujKgepg5-ppIp6MdwJICRpmrgEJB2ELOcBKsN3qaTcAimY94yZDJ5ydzUQYNgfvD3QjwDSdQ2lvnaGnpdGO7dY0vRK1eh7d7K7uCFRtseoxgXiFgWMlb9aVQ9_6lymvIHbH9GQbToOPEB85FDHb4DuNL3avnxYo_DpVZAJX9PzLjYilMX3LLZNCo9RWJbgOgaCrEKo6Xag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a679b54bf.mp4?token=TdG-W9-DIfmY-wLBzlw0ISZXB_6mSTAGz-cwsuhhM26M0GhW01upaHv_liutsTYG6uDQ_yhiIHNzhw3bhcqvpeGta2j7dLkudgC1SeXvwUX4HV9iKoEfJWmCGd-W7VOScISvksyZdTolujKgepg5-ppIp6MdwJICRpmrgEJB2ELOcBKsN3qaTcAimY94yZDJ5ydzUQYNgfvD3QjwDSdQ2lvnaGnpdGO7dY0vRK1eh7d7K7uCFRtseoxgXiFgWMlb9aVQ9_6lymvIHbH9GQbToOPEB85FDHb4DuNL3avnxYo_DpVZAJX9PzLjYilMX3LLZNCo9RWJbgOgaCrEKo6Xag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
🔻
قليلة التداول
الشهيد الحاج قاسم سليماني رضوان الله تعالى عليه يشكر الشيخ اكرم الكعبي ويصفه بالاخ المجاهد… السلام على نجباء أهل العراق</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/naya_foriraq/87394" target="_blank">📅 21:00 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87393">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">‏
الناتو
: مستعدون للردع والدفاع في مواجهة أي تحرك روسي عند الضرورة.</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/naya_foriraq/87393" target="_blank">📅 20:37 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87392">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rb1i7vVnAS_jmd8_vWyGdgZjn4-jscnbu2w0J2GhCGJVPVLB073W270GvIaNTSxvHa0Sv-3YdO54zTpGRbXDBI6K719fJG8Tev0r8yQZ1BWNnF0DL93X-omW6A2A25KD-pZRtKsf81cYABy1fk2vYhifcfAi5G9unv0Xwj5yKdmjcN1tjwis6sZFEdT8YyvMpU63FEGf-zVJ_p64xfmG_yPxfRgZltXKn6v4ort5PxEHB7_j8sCTdnO9YJwinN3CMag_nv70y4jMSWTTGjPkVPVyAvogoYR487chmBT8knUR_3GH3s6T8VjqFtnsd4C0PAyE6D2eD0gr4wW60iDywA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
تعيين الدكتور محسن رضائي ممثلاً لقائد الثورة الإسلامية في المجلس الأعلى للأمن القومي.</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/naya_foriraq/87392" target="_blank">📅 20:32 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87391">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🇾🇪
انصار الله في اليمن يطلقون موجة جديدة من صواريخ نحو المخا</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/naya_foriraq/87391" target="_blank">📅 19:04 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87390">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">اعلام سعودي: انصار الله استهدفوا المرتزقة في المخا بـ30 صاروخا باليستيا</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/naya_foriraq/87390" target="_blank">📅 18:27 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87389">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb4033ae6c.mp4?token=Ge7qjQl-OSWqHhsJ7bnHia47cKjChb-UR_9LmQ45BKQC5Q3p9yWLCBnDIH35esRHa8es4Hw1zy4bolGLLuedjqFLkpJDP1K1tNriXMRJGbL_I749uCSYODgEZilzzWHo6oDdptkY7bWINN4mqlLBcHO6FTx1TRI8sK1Dkq8lPUwHM_WIhKepgVml6JEozfeJdSY0RNdyswOjxwTDQXJiUDxa1UZu6tQ6mHzfRcWFue3FtEhlQotGcwTh76EPQ8DL464aokHWOVc7mM7N-5Lzjk8mEBeYR86bQizXyXW_wFR8zO7zbsJyVdMxqO1y1qj93OiSxOHNyPZ2wOzwXT2gzhPDwk7BH1G_0dEHtWFv0xda0HBTXaHerP6-vi5RtF4ja5gYOOyk8Z_2H5P7hFxVwDxjBSpFQB6hgOABp6aK4k3KBkt5HX96h_7M50ZXhAR4ziAskkJD9vUHvYjPjDAcEhF9ZV1O2JkRm65DksvXSsg4v-raxCijJphpYAom1-tcsbgHLOMpukPt23RIJ7XlqSKHPgfgJlT7NjIVnsBOnggVOjqxOG9k_DBDmt42lIh5PIGXTmxB4hU4OqlxoFZKkoddN1MSpijXzOcNXQVGTAnGXOSydUTcNWFvNP0seKM2NDqI0dm6FtyewOmdwkDQNBdSTKY5GPXb0qLqjVK2b9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb4033ae6c.mp4?token=Ge7qjQl-OSWqHhsJ7bnHia47cKjChb-UR_9LmQ45BKQC5Q3p9yWLCBnDIH35esRHa8es4Hw1zy4bolGLLuedjqFLkpJDP1K1tNriXMRJGbL_I749uCSYODgEZilzzWHo6oDdptkY7bWINN4mqlLBcHO6FTx1TRI8sK1Dkq8lPUwHM_WIhKepgVml6JEozfeJdSY0RNdyswOjxwTDQXJiUDxa1UZu6tQ6mHzfRcWFue3FtEhlQotGcwTh76EPQ8DL464aokHWOVc7mM7N-5Lzjk8mEBeYR86bQizXyXW_wFR8zO7zbsJyVdMxqO1y1qj93OiSxOHNyPZ2wOzwXT2gzhPDwk7BH1G_0dEHtWFv0xda0HBTXaHerP6-vi5RtF4ja5gYOOyk8Z_2H5P7hFxVwDxjBSpFQB6hgOABp6aK4k3KBkt5HX96h_7M50ZXhAR4ziAskkJD9vUHvYjPjDAcEhF9ZV1O2JkRm65DksvXSsg4v-raxCijJphpYAom1-tcsbgHLOMpukPt23RIJ7XlqSKHPgfgJlT7NjIVnsBOnggVOjqxOG9k_DBDmt42lIh5PIGXTmxB4hU4OqlxoFZKkoddN1MSpijXzOcNXQVGTAnGXOSydUTcNWFvNP0seKM2NDqI0dm6FtyewOmdwkDQNBdSTKY5GPXb0qLqjVK2b9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
طيران حربي مجهول الهوية في سماء محافظة ذي قار جنوبي العراق.</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/naya_foriraq/87389" target="_blank">📅 18:19 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87388">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/796dadaeaf.mp4?token=ma4hJ-PXxnEE59gjJyqc2PZpdiVGUyDPSry50XzI_JWtsxkbSVJAQ86EUhZeAbj7KDJsXIoN16-7204nkvvV-enThOKG6B7LkuCqB1Fv1NQKlZknnJ3FdbjlRLw5jcQ5k1IkpAfUwCRLRj9y5czC02y9pert3b65-2h-Ihp_jNdNDO_8U4-amN62Oqp3j8COf70SZybksyQ7lan6tQy1GQuEx61Ali3o4rOjUBxFHMd9YdotA4Nk7d_ipChVXM2Za09Pj-Ss4ByVtT-zzb9Lz6RM--IOQlzbplYRWpBG5Ehs_rk5VhEpel1vlAA87UjAJkwpRsuWlYwrSM82yS-PDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/796dadaeaf.mp4?token=ma4hJ-PXxnEE59gjJyqc2PZpdiVGUyDPSry50XzI_JWtsxkbSVJAQ86EUhZeAbj7KDJsXIoN16-7204nkvvV-enThOKG6B7LkuCqB1Fv1NQKlZknnJ3FdbjlRLw5jcQ5k1IkpAfUwCRLRj9y5czC02y9pert3b65-2h-Ihp_jNdNDO_8U4-amN62Oqp3j8COf70SZybksyQ7lan6tQy1GQuEx61Ali3o4rOjUBxFHMd9YdotA4Nk7d_ipChVXM2Za09Pj-Ss4ByVtT-zzb9Lz6RM--IOQlzbplYRWpBG5Ehs_rk5VhEpel1vlAA87UjAJkwpRsuWlYwrSM82yS-PDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
عضو مجلس النواب العراقي غالب محمد:
تستمر عمليات تهريب المشتقات النفطية من مصفى «لاناز» في أربيل إلى تركيا، عبر شاحنات تركية، رغم أن هذه الكميات مخصصة لتلبية احتياجات المواطنين في إقليم كردستان، وليس لتهريبها إلى خارج العراق.</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/naya_foriraq/87388" target="_blank">📅 18:05 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87387">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">اعلام سعودي: انصار الله استهدفوا المرتزقة في المخا بـ30 صاروخا باليستيا</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/naya_foriraq/87387" target="_blank">📅 17:46 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87386">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">انباء عن سقوط طائرة MQ-9 أمريكية في جيبوتي ولم يتم تحديد سبب سقوط طائرة الى الان</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/naya_foriraq/87386" target="_blank">📅 17:38 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87385">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/86225a79fb.mp4?token=hyq6EElAiB6FhylB-No3BxanYbi0hzSBIQDVlPpHPwQutdZUF_Nm_aFh5AiQoVfpczjYI4TypjmDxSUAvebGMk1td1iuHwL3ZcxnB6T5Xd-wxmsDbw4maDIUAYQ9A4T05aCI0KFuKT4yvg_yArOZdJlfYvyAVZGS5GpBMusuHds9F9u5UTo6ovCjvMQ_2JCnUrTvqKSzok1LL94jQRbPkeGy15uosLAsKLYZlIegpc-NK-ZsA1avyVBhb_0SvuOGZdZhcBiA8hAI_5jHLrRKoh3kb_8XhUUdfv5qu4UDvhy0_1e4AryaMjtF-FKhCCsbKkRs7JN-BdJ8m7s7VNivNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/86225a79fb.mp4?token=hyq6EElAiB6FhylB-No3BxanYbi0hzSBIQDVlPpHPwQutdZUF_Nm_aFh5AiQoVfpczjYI4TypjmDxSUAvebGMk1td1iuHwL3ZcxnB6T5Xd-wxmsDbw4maDIUAYQ9A4T05aCI0KFuKT4yvg_yArOZdJlfYvyAVZGS5GpBMusuHds9F9u5UTo6ovCjvMQ_2JCnUrTvqKSzok1LL94jQRbPkeGy15uosLAsKLYZlIegpc-NK-ZsA1avyVBhb_0SvuOGZdZhcBiA8hAI_5jHLrRKoh3kb_8XhUUdfv5qu4UDvhy0_1e4AryaMjtF-FKhCCsbKkRs7JN-BdJ8m7s7VNivNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اعلان حالة طوارئ امريكية في جيبوتي</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/naya_foriraq/87385" target="_blank">📅 17:37 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87384">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🇾🇪
🇾🇪
مصدر يمني رفيع في صنعاء:
ضربات القوات المسلحة اليمنية على المخا ومأرب فتكت بالضباط السعوديين وتحشيداتهم، الجيش اليمني سيحول كل تجمع للضباط السعوديين إلى هدف وضربة اليوم وصلت رسالتها بقوة.</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/naya_foriraq/87384" target="_blank">📅 17:33 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87383">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">اعلام العدو الامريكي يقول ان ترامب يتجه ‏الى تمديد وقف إطلاق النار بشرط كبح البرنامج النووي واستئناف الملاحة في مضيق هرمز</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/naya_foriraq/87383" target="_blank">📅 16:40 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87382">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">اعلام العدو الامريكي يقول ان ترامب يتجه ‏الى تمديد وقف إطلاق النار بشرط كبح البرنامج النووي واستئناف الملاحة في مضيق هرمز</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/naya_foriraq/87382" target="_blank">📅 16:37 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87381">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">طائرة امريكية كانت متجهة الى قاعدة إيلسون الجوية في الولايات المتحدة تعلن حالة الطوارئ لاسباب غير معروفة</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/naya_foriraq/87381" target="_blank">📅 16:32 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87380">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RgYi7eiiHiQt4v8CObwLNaZpNQp53pUreroSMwtbHXu7yHXwkwJn1aHmLuwcNtOtxnmKJ_fCbri53YFx9FVPwaV4QsjtKUaky-p71-rVywaiDI77xIBAsjXJCNdkPzOaxRRV6mrLFdL8kXOS9TbCr4zDrA4uHS9Rups1WjJ29tFLv5noTMfLihh5-g8IXjjdEXkzhBp7oOPNbW9SUBrFUlXG_4cKZF_HR2P57-Rgil1PeCM-G0572FndRLgp9vOmIe00QRPe42zRs2ZkqFC3WW9EYJHO9n4OrlGJtcSBtPtEnmqZAI2O_amGGisjCjO0sMvjY_d9-NyMcoZvsIYo-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد وصفها شهداء الحشد بـ"القتلى" وقتلى مرتزقة السعودية في اليمن بـ"الشهداء"
النائب احمد شهيد:
تقدمنا بكتاب رسمي إلى هيئة الإعلام والاتصالات بإيقاف قناة خنجر العْدر قناة الفلوجة الطائفية</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/naya_foriraq/87380" target="_blank">📅 16:08 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87379">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">القوات المسلحة اليمنية تطلق صاروخًا باليستيًا على منزل حاكم الحديدة المدعوم من السعودية وانباء اولية عن نجاته</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/naya_foriraq/87379" target="_blank">📅 15:47 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87378">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">عصابات الجولاني تقول انها توصلت الى مذكرة تفاهم مع روسيا بشأن القواعد في طرطوس وحميميم</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/naya_foriraq/87378" target="_blank">📅 15:46 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87377">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">عصابات الجولاني تقول انها توصلت الى مذكرة تفاهم مع روسيا بشأن القواعد في طرطوس وحميميم</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/naya_foriraq/87377" target="_blank">📅 15:44 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87376">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/45ecba7daa.mp4?token=JfCn0SPRi_YKpN4UI2zfUkVvtzph24J66zRSjA78DdPcHBH87IDFp2eUTwu7zDkokZoQ19gVuae4iftS4lQH7tnHxvffk9x8ApY3-tjCxm3Bc3rIs3vSe7HDdu2cJgtSrOpfix1VuhPsuMy3Ydcn6YBkyTEIZCOSad-rQAiwATXppi56_duCRn5Tvv9cb1NNm1rxU2aGtQw87BVMMCc3s7HPOjoylnaee93nz4CCpdPeUsxudpkRSkJ1_jiiex78LG021UDQDnVKKQ_cDC76lFizfWc-UB7ecFYPx4q_XT6BbOLT5KweLpIIdsGd6GQC22R_LkINuolCeQAHEt39Og" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/45ecba7daa.mp4?token=JfCn0SPRi_YKpN4UI2zfUkVvtzph24J66zRSjA78DdPcHBH87IDFp2eUTwu7zDkokZoQ19gVuae4iftS4lQH7tnHxvffk9x8ApY3-tjCxm3Bc3rIs3vSe7HDdu2cJgtSrOpfix1VuhPsuMy3Ydcn6YBkyTEIZCOSad-rQAiwATXppi56_duCRn5Tvv9cb1NNm1rxU2aGtQw87BVMMCc3s7HPOjoylnaee93nz4CCpdPeUsxudpkRSkJ1_jiiex78LG021UDQDnVKKQ_cDC76lFizfWc-UB7ecFYPx4q_XT6BbOLT5KweLpIIdsGd6GQC22R_LkINuolCeQAHEt39Og" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مصرع 7 اشخاص و35 جريح من المرتزقة في ضربات أنصار الله على المخا كحصيلة اولية</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/naya_foriraq/87376" target="_blank">📅 15:19 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87375">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">رصد إطلاق صاروخين باليستيين من قبل بواسل انصار الله باتجاه المخا والانفجارات تهز الميناء</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/naya_foriraq/87375" target="_blank">📅 15:17 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87374">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HcKOhwLmyaPyXHEqpl1r_UDMZVxffkk-nw1h59lWKKI8x0oEuZdFXJGOjVUHCHgixyOFthYBYUBT0hXED_smvPdAT3t1Zj9_PLR26vFAyngY3DZS5Gh8bsiQxVAOSM6bhxIofwuaNIlpJfA_X_VF3i5jFbbz3fmhjzYk7D_tHNfEWkdJR5esyEvZ8i7PJHQvKAxRSlV4N2SirOqxxBatzlrcqf9u4fArlHYWqgb0k2t8EYv2gmBpiMMNCM1ffqta-UNxqZGlidFJYVCTcJnGV83haxrDPOPO_aySK5bPynATIlsTbAfo-2ST3GBuT8wngVkDh0OIj7O4ZyNMjgC0Kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رصد إطلاق صاروخين باليستيين من قبل بواسل انصار الله باتجاه المخا والانفجارات تهز الميناء</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/naya_foriraq/87374" target="_blank">📅 14:55 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87373">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3801856749.mp4?token=r_N02k5ZBVTMWyFsPF5GyegX5XClbSkHPGlodf_Ne35xCRAxGTt4kgtwY9IKJJq5Hkxjl2_c7Oe7dbi8UkZQ2i-rAKTBj7vKubXdnNI7vKHMuZTqeGwjfy-yP5WHusfMI5eyB0RYDUSLAa4Nm3HFrtdenCcNa7ipuRj-ObVgTDTdfHSQinxQvx9sD4X1aUQBtJyJc_XslI1JpK4OZk3HWdCi7sMN8N7Uy_3ErDsgaH_e8dII8KriikJ01kZq37vcdpUO2L9fDUET-7CH5apVEL8265xaVZ1Il9tlM8E4Rhy--dCpgoF-yRyHOXLmnFGdgHrIsKkyIxSojs3jcBeJXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3801856749.mp4?token=r_N02k5ZBVTMWyFsPF5GyegX5XClbSkHPGlodf_Ne35xCRAxGTt4kgtwY9IKJJq5Hkxjl2_c7Oe7dbi8UkZQ2i-rAKTBj7vKubXdnNI7vKHMuZTqeGwjfy-yP5WHusfMI5eyB0RYDUSLAa4Nm3HFrtdenCcNa7ipuRj-ObVgTDTdfHSQinxQvx9sD4X1aUQBtJyJc_XslI1JpK4OZk3HWdCi7sMN8N7Uy_3ErDsgaH_e8dII8KriikJ01kZq37vcdpUO2L9fDUET-7CH5apVEL8265xaVZ1Il9tlM8E4Rhy--dCpgoF-yRyHOXLmnFGdgHrIsKkyIxSojs3jcBeJXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتن ياهو: أود أن أكون دقيقًا. إسرائيل ترفض الوثيقة المكونة من 15 نقطة. سمعت بعض الناس يقولون: "لم تقله." لقد قلناه، ولكنني هنا أكرر: إسرائيل ترفض الوثيقة المكونة من 15 نقطة!</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/naya_foriraq/87373" target="_blank">📅 14:40 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87372">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa310c312d.mp4?token=UbPEaAzXTH-X_xgFZCYtB95UswHrLXJOz8pDBgBENU2Dhk_rRTChwIixmDOj1N5SCE0DcuRCC62k5PKoQUBHvA85X20JBYV7heZjz_8PmUBr7ILM72Ve_Y4k5q1JDRwo3A-RSmFhSjJKcJJkYVFQzSSvmyUxo7Ik2hmBSvaY--Ho4ihu9E2X3kLnIzfxIIO92fGrb5GBTdVG-osz1bnrcbL1xX-ExJdeBQecv5BG16372ZuXY76auihmJN-gB5-ur8bIRPrEtSqjLwI2rjTFll2yyyBSufTrEQK_K_9japB7EZNc7rhPzTgBUwn9ILLEykDEYwOCrJ1iC1n_FdcSY2t-jWsjf866jkxaic-d5SIIQ7YJ2112vmCHmlhDIMAew9SrDRo2hqXVYjluP07FLssqPUBT5PRiHmety4eEesE1BeBN3urYOFmXyfiaw8PJbdW5zNfDC8pdBB5DJrFkUp1Jp43UC1tzBTFFgGRQXwukR9_emDn805HdTAVYveM3QQiWy1H5X-yr-k3BgNYXet0qQsJ0ZlETL8R8Gx8KSL4Vk_znYbx4E-B6cSjKjHYvbxB4ZZx37VSH-Vn84DjIuDvwG51kTBzOej_TFCYcrNZ6nN_AAGGj3K7EadL4dbXRWB76F2xLGC2Ig5GQGcCmsLEiW20YgVcERG1YKz8l_Io" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa310c312d.mp4?token=UbPEaAzXTH-X_xgFZCYtB95UswHrLXJOz8pDBgBENU2Dhk_rRTChwIixmDOj1N5SCE0DcuRCC62k5PKoQUBHvA85X20JBYV7heZjz_8PmUBr7ILM72Ve_Y4k5q1JDRwo3A-RSmFhSjJKcJJkYVFQzSSvmyUxo7Ik2hmBSvaY--Ho4ihu9E2X3kLnIzfxIIO92fGrb5GBTdVG-osz1bnrcbL1xX-ExJdeBQecv5BG16372ZuXY76auihmJN-gB5-ur8bIRPrEtSqjLwI2rjTFll2yyyBSufTrEQK_K_9japB7EZNc7rhPzTgBUwn9ILLEykDEYwOCrJ1iC1n_FdcSY2t-jWsjf866jkxaic-d5SIIQ7YJ2112vmCHmlhDIMAew9SrDRo2hqXVYjluP07FLssqPUBT5PRiHmety4eEesE1BeBN3urYOFmXyfiaw8PJbdW5zNfDC8pdBB5DJrFkUp1Jp43UC1tzBTFFgGRQXwukR9_emDn805HdTAVYveM3QQiWy1H5X-yr-k3BgNYXet0qQsJ0ZlETL8R8Gx8KSL4Vk_znYbx4E-B6cSjKjHYvbxB4ZZx37VSH-Vn84DjIuDvwG51kTBzOej_TFCYcrNZ6nN_AAGGj3K7EadL4dbXRWB76F2xLGC2Ig5GQGcCmsLEiW20YgVcERG1YKz8l_Io" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتن ياهو: أود أن أكون دقيقًا. إسرائيل ترفض الوثيقة المكونة من 15 نقطة. سمعت بعض الناس يقولون: "لم تقله." لقد قلناه، ولكنني هنا أكرر: إسرائيل ترفض الوثيقة المكونة من 15 نقطة!</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/naya_foriraq/87372" target="_blank">📅 14:39 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87371">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vBRK6-10JU8QrMwoIlzfmzEiZVl79P6PdXjzfwE27ff48XGsOrz1oyweMy6fBISa3NwxLIk44ItlhpmHSP9g4P8e6UHATOo1oJiEacNGDkqzPhIGXVzarmUg-MSKBAdKZRyJVlPamuRzGg_Pr_3A0yNL6XKdfZ0BnB_-9-QE5frbHt6OV7tw18oj_SVVgLuAzytqz8widYU8Y0YUmlDSAPdklfQsJes6QFbW-NhSwWezLTdJHnvDWXk32GuN9Kh2wa7P0HrmEbgfEpmmqxNWrNlRtBV4UTCz4xtqpp22LnDcfpufKIT8nAcXgYJJDJJncc1y7DwcOtYt_e1beWnuVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">القضاء العراقي يطلب من البرلمان رفع الحصانة عن النائب ناظم الأسدي</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/naya_foriraq/87371" target="_blank">📅 14:30 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87370">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">اعلام سعودي: القصف مستمر على ميناء المخا</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/naya_foriraq/87370" target="_blank">📅 14:20 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87369">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">اعلام سعودي: القصف مستمر على ميناء المخا</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/naya_foriraq/87369" target="_blank">📅 14:16 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87368">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">الرئيس الايراني مسعود بزشكيان يلتقي قائد الثورة الاسلامية</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/naya_foriraq/87368" target="_blank">📅 14:03 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87367">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">الرئيس الايراني مسعود بزشكيان يلتقي قائد الثورة الاسلامية</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/naya_foriraq/87367" target="_blank">📅 14:02 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87366">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🇮🇷
وكالة تسنيم:
تكليف محسن رضائي ممثلاً للقيادة العليا للثورة في المجلس الأعلى للأمن القومي الايراني.</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/naya_foriraq/87366" target="_blank">📅 13:54 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87365">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p6yhgM3c6oOe0R1fDq_ww2x2kr_IiYLH-7ZCHCu4hUjbYhBvVfn006JKDdeCshOsxheo4WKS89DLWKHR3KCl5OGK7Fyc3Wc7bK6o9Oj7kK3gOw3Q4XGXPYAe1apS6IFwRK3jQCz06eRXrZuosnSI9ZH5LQmXO_6za-4JGo38QBW0ni3wrxmBrlcocl2Y9Y0T6XJBgZ2uZeCeUJwqX8QWIvvKZuLPhdB4kT9xLOEiz4qPfkNNKpkuXMlhl5SopSAusx5Dt_fJ2XnPNTOtcfSf6wFmEVrpmOUMGklx1dXUIbwwsNUA0c-8e4tn2oRQfMZ6Y3Cf9Rf2-7_04UdjrhufZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
مصدر إيراني لنايا
‏في إطار التغييرات الجارية على مستوى صناعة القرار الأمني والاستراتيجي في إيران، تمّ تعيين اللواء محسن رضائي ممثلاً لقائد الثورة الإسلامية في المجلس الأعلى للأمن القومي.</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/naya_foriraq/87365" target="_blank">📅 13:48 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87364">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🇮🇶
🔻
بيان صادر عن هيئة الحشد الشعبي
:
تستنكر هيئة الحشد الشعبي، بأشد العبارات، ما صدر عن بعض السياسيين من اتهامات باطلة طالت رئيس الهيئة السيد فالح الفياض، والادعاء بامتلاكه معلومات مسبقة عن استهداف مقرات الحشد الشعبي وعدم إبلاغ القطعات العسكرية، وهي ادعاءات عارية عن الصحة ولا تستند إلى أي دليل أو حقيقة.
وتوضح الهيئة أنها، منذ بدء الأحداث في المنطقة قبل أشهر ولغاية اليوم، وضعت جميع قواتها في حالة إنذار، كما جرى، قبل يومين من الاعتداء، إبلاغ جميع القطعات بضرورة أخذ أقصى درجات الحيطة والحذر، وهو ما أسهم في حقن الكثير من الدماء وتقليل حجم الخسائر.
وفي المقابل، لم يتخذ الفوج الرابع في اللواء 30 جميع الإجراءات الوقائية المتبعة، ما أدى إلى استشهاد العدد الأكبر من منتسبيه خلال الهجمات. وقد وجّهت رئاسة الهيئة بفتح تحقيق مع المسؤولين هناك للوقوف على ملابسات هذا التقصير وتحديد المسؤوليات.</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/naya_foriraq/87364" target="_blank">📅 13:48 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87363">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">اعلام سعودي: القصف مستمر على ميناء المخا</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/naya_foriraq/87363" target="_blank">📅 13:41 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87362">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">بيانٌ صادرٌ عنِ القواتِ المسلحةِ اليمنيةِ   بسمِ اللهِ الرحمنِ الرحيم   قال تعالى: {فَلَا عُدۡوَ ٰ⁠نَ إِلَّا عَلَى ٱلظَّـٰلِمِینَ} صدق اللهُ العظيم  رداً على استمرار العدو السعودي في التحشيد لأدواته وتعزيزها بالأسلحة والمعدات واعتداءاته المستمرة في الساحل…</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/naya_foriraq/87362" target="_blank">📅 13:37 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87361">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O41mO--63bhyHsKDUaZbxTs7urGizA4zojjtP8k8t9c4EN9h0CgjBeKUHTwmet-0j4ygz4p16_lLuyC0xQ-XP9XQcaCsLoVtn0mkin2BAhEQE8PuYXXqb68aH8Kl7w-lqmkJTqeMa2By-7TRS3jSd45zeWLhJUbQPRAPvR-esUKDKm3YRqvK27_ZIktIPP9kOvjvvLQD3MlJD4ojsCLpd9yTwV8yQ2G47188KOLrQoUWRdbh5OQzMUSgiolaoYT-xQPaHG0mzvmHlKZ3mWq4GxsKVyEgXNBGUArDpuqqmdte6VinmeXXe14Vj14_piIH5GUpKaCdwAJWwJrNopmqFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هل الطائرة اصيبت بهجوم يمني؟</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/naya_foriraq/87361" target="_blank">📅 13:36 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87360">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">بيانٌ صادرٌ عنِ القواتِ المسلحةِ اليمنيةِ
بسمِ اللهِ الرحمنِ الرحيم
قال تعالى: {فَلَا عُدۡوَ ٰ⁠نَ إِلَّا عَلَى ٱلظَّـٰلِمِینَ} صدق اللهُ العظيم
رداً على استمرار العدو السعودي في التحشيد لأدواته وتعزيزها بالأسلحة والمعدات واعتداءاته المستمرة في الساحل الغربي ومحافظة تعز وذلك لثني شعبنا العزيز عن تحركه المشروع لمواجهة الحصار الظالم والعدوان الغاشم المستمر عليه منذ اثني عشر عاماً
نفذت القوات المسلحة بعون الله تعالى عملية عسكرية واسعة ونوعية استهدفت تحشيدات  العدو السعودي ومخازن أسلحته في منطقة المخا وقد كانت الإصابة دقيقة بفضل الله وأدت إلى تدمير واسع في تلك المعدات والأسلحة ومصرع وإصابة العشرات بينهم سعوديون وذلك بعدد كبير من الصواريخ الباليستية والطائرات المسيرة.
لن نسمح للعدو السعودي بتحقيق أهدافه المتمثلة في استهداف شعبنا والزج بأبنائه إلى محارق الموت خدمة لأجندته التآمرية لصالح أعداء الأمة وستستمر القوات المسلحة بعون الله تعالى وبالتوكل عليه في رصد وتتبع كافة التحركات والتحشيدات السعودية واستهدافها بشكل دقيق ومباشر، وسيمضي شعبنا اليمني وقواته المسلحة وفقا للمعادلة المعلنة "الحصار بالحصار والتصعيد بالتصعيد،  واستهداف أي تحشيدات تستهدف الشعب اليمني والمحافظات الحرة"
والله حسبنا ونعم الوكيل، نعم المولى ونعم النصير.​
عاش اليمن حرا عزيزا مستقلا،
والنصر لليمن ولكل أحرار الأمة.​
صنعاء، 26 صفر 1448هـ
الموافق 9 أغسطس 2026م.​
صادر عن القوات المسلحة اليمنية</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/naya_foriraq/87360" target="_blank">📅 13:29 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87359">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ClCNWRSiU6C0KrjuMKHnlUnOQOMx09RLUEXlufw2XVgwb0IpbOl9ZIjaqxvWpdegsTcnVxzhCy8VLopvldXAfrxdbMrjSxz8YHNpAAL628qoqVHHBa-BOgoWQUQrC9-tVVbIMN3RVsXykilorz5ZOGcKl7UKj34WYOMDVXa0ajYlCerr4cBgtbPVpBhYK-A2tulDm7eYmLNwVlEEWu6mHwOpY_fLYZkyQC9udjUUMinotNwmLXupbw5UGqckuPUB1TjrPYHGdoQzbaLjiZE1CWvZrJZn6rTpbRoodmHfkkp60nsP0nPCvU2L3DorQyFxmWmT4tjU9bDcoOFlbTNHdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هل الطائرة اصيبت بهجوم يمني؟</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/naya_foriraq/87359" target="_blank">📅 13:20 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87358">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">السفارة الامريكية في جيبوتي: طائرة امريكية في حالة طوارئ باجواء جيبوتي</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/naya_foriraq/87358" target="_blank">📅 13:14 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87357">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">اعلان حالة طوارئ امريكية في جيبوتي</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/naya_foriraq/87357" target="_blank">📅 13:13 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87356">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">اعلان حالة طوارئ امريكية في جيبوتي</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/naya_foriraq/87356" target="_blank">📅 13:12 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87355">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d94b1eab85.mp4?token=Wk3f_K3fc6iR5VnyPPi45gf2xzxIULWE6FgiCCm7Vwdq85t3K4y0etnDpj1CUL1JCInOKqGMTxrMT5APkDbHNYsC-K5NhyczmxWok0ATmBw0PCXt7qcoPK9NFxlDrVEp9ii6-Du-4BqwDfo6pxIpNml2X27lbBRb6CyVOhsZuaw2Ona-h0a8pHIn5QFkO4XfwJosDiyqyEInvJYx3BxdkDhPcXx-AOtCxr9ExhdQVzT8oVWSpPjqXUvgxj7DNa1jJ1rVpJNCUS7ww1laxDEPdOQyMswi_RB6ZQUq3esgAzmK74vZGv-YRvWoWK4P_3MSuE9PWfjCyHBOC7O1InMctw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d94b1eab85.mp4?token=Wk3f_K3fc6iR5VnyPPi45gf2xzxIULWE6FgiCCm7Vwdq85t3K4y0etnDpj1CUL1JCInOKqGMTxrMT5APkDbHNYsC-K5NhyczmxWok0ATmBw0PCXt7qcoPK9NFxlDrVEp9ii6-Du-4BqwDfo6pxIpNml2X27lbBRb6CyVOhsZuaw2Ona-h0a8pHIn5QFkO4XfwJosDiyqyEInvJYx3BxdkDhPcXx-AOtCxr9ExhdQVzT8oVWSpPjqXUvgxj7DNa1jJ1rVpJNCUS7ww1laxDEPdOQyMswi_RB6ZQUq3esgAzmK74vZGv-YRvWoWK4P_3MSuE9PWfjCyHBOC7O1InMctw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاهد من ميناء المخا الاستراتيجي على البحر الأحمر بعد استهدافه من قبل انصار الله</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/naya_foriraq/87355" target="_blank">📅 12:36 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87353">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">انفجارات جديدة تهز ميناء المخا</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/naya_foriraq/87353" target="_blank">📅 12:35 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87352">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">‏بيان مهم للقوات المسلحة اليمنية بعد قليل.</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/naya_foriraq/87352" target="_blank">📅 12:30 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87351">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">أنصار الله يستهدفون إمدادات عسكرية فور وصولها إلى مرتزقة السعودية في ميناء المخا</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/naya_foriraq/87351" target="_blank">📅 12:29 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87350">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MKrxowmHRtiUawQbM828GWzYw0RHlNPnziU0HSF6IHdg5-vna8IwC3EroePFFsb7uJ12MUsXQnsR3m4o5NNDXpArpxvp3l-Z4RxZygWI1rKAgKjLUYGTrAXfiFnYavGcYkj3zkRRJkwX7aCZKfOvu761glgz6HRGFPNYgfi9g8BhMzJbiiU_6msgBjiHBgdPLTaGLUbWFtR0uFizpCn83GQSZYlzOf6DI4vm_T_HWXq_CTnlGJ6YsrvtztSWgD8UVbJTEGacfuOWj4Iu9ZmJP6TUqoAJEyMTiS7iI7RrWv-_2TgMBZ2CUbGvb3YO_Y8Bno_bzPqrhaRJZMVxaTHaNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استمرار دوي الانفجارات من ميناء المخا عقب دكه بالصواريخ</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/naya_foriraq/87350" target="_blank">📅 12:07 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87349">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d20a240712.mp4?token=TTqNmrec5SYYxU1T8WqPNTDVzhKC9RRATDNV-BC1dOPmixCEI8bEO3Kpdy5Le2zzZsF8S9OppxWUJcpO-Z8LoSZoW0Lxl8PpMHtoz_bvq_QjXH1onraheYaNfH4DS5f6EwhWim4CrRZuIFevIg3CoIXwRWcFpXvTfYK1BL1uldZGErSuROww438X-WyrQX9jxUU94XCL2VdW6CjzlPqgqZm0r3g3ZFGa7mfGY-s-KbTB-HFgHiTNWQ_GqDWT5tcvbqRQX-Fl7L9VQ4NFl1hGNhaa8e9zw0gm_7KCfliHIXW3TGyskB4UlQ90shHqq3XZu0C5NO7yE6mv2QKd6V8zpi1kKUtCtycAiz0OdjW7uicqF0Uj_LV50CzLPlhDPzTBnCL30qh_QPw9u-6yQ6HM_Rg4P9Wekzd5tf_zkUgXyHEpXLQo0tpnZmWe3HHN_2PUmwYEym99ARGbmpuDQ1WheBFPWY75xWb0q1glxsjCUAkPoqSVn1sDbv_U-r2JQXX1kIOpsiixKWYFdFV15rtTfLi9CALynsvkwsUXR-ixnYv6NPimeUyLfEsveH7vYjP3ldx3AefNEn2VWO2i-9Zq_Zqc1EqBBT_WQRHIrMkl1PLOAny2G59di95uTj6AMqNN5nJhk4DYluZOOzczpn9wjDTdDO1k_NzFNVqZkpOFOUk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d20a240712.mp4?token=TTqNmrec5SYYxU1T8WqPNTDVzhKC9RRATDNV-BC1dOPmixCEI8bEO3Kpdy5Le2zzZsF8S9OppxWUJcpO-Z8LoSZoW0Lxl8PpMHtoz_bvq_QjXH1onraheYaNfH4DS5f6EwhWim4CrRZuIFevIg3CoIXwRWcFpXvTfYK1BL1uldZGErSuROww438X-WyrQX9jxUU94XCL2VdW6CjzlPqgqZm0r3g3ZFGa7mfGY-s-KbTB-HFgHiTNWQ_GqDWT5tcvbqRQX-Fl7L9VQ4NFl1hGNhaa8e9zw0gm_7KCfliHIXW3TGyskB4UlQ90shHqq3XZu0C5NO7yE6mv2QKd6V8zpi1kKUtCtycAiz0OdjW7uicqF0Uj_LV50CzLPlhDPzTBnCL30qh_QPw9u-6yQ6HM_Rg4P9Wekzd5tf_zkUgXyHEpXLQo0tpnZmWe3HHN_2PUmwYEym99ARGbmpuDQ1WheBFPWY75xWb0q1glxsjCUAkPoqSVn1sDbv_U-r2JQXX1kIOpsiixKWYFdFV15rtTfLi9CALynsvkwsUXR-ixnYv6NPimeUyLfEsveH7vYjP3ldx3AefNEn2VWO2i-9Zq_Zqc1EqBBT_WQRHIrMkl1PLOAny2G59di95uTj6AMqNN5nJhk4DYluZOOzczpn9wjDTdDO1k_NzFNVqZkpOFOUk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">استمرار دوي الانفجارات من ميناء المخا عقب دكه بالصواريخ</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/naya_foriraq/87349" target="_blank">📅 12:07 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87348">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">مراسل نايا في اليمن: أنصار الله يطلقون أكثر من 20 صاروخ باتجاه مواقع مرتزقة السعوديين وجميع الصواريخ تصيب أهدافها</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/naya_foriraq/87348" target="_blank">📅 12:02 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87347">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PT77JUqTAFMdL_ifJxd9pUZvOkb9LRaIdVYacVpwGuLJopgqu-kzjcqVgcVQrBUTsJ3_EG-fM9cO-SX_6RHdah4HNlG28eMN9ghgtg3A7tz6EqJTs-5D2zc4kDAEPcjuWYVHAhlJmQRRzAaPi_WTpENHmdejcbYcJMPR9TsPGAuxHT2MiBWiXSAq-XXXNr-M7D8CvdBj-clKO9xBJ-M9ZjrGLeW4nh4u1k6BOV_tOF8xj8kF6lziB5v6wwgNzYxTvPtvGw1L6vh4aiqIw-xV8GoGjMV8-BHt2M_Vw8EGc_YQqzJxJG6rIxPk6EmkcHFAqORQ-E9ax--4RyWkyiSrsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انفجار متتالية تهز ميناء المخا</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/naya_foriraq/87347" target="_blank">📅 12:00 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87344">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QmTlP9OEYEjo9YmlI4F-3vMBWt6_83hEhfZjaq4KlaQjKMbSvn9BSm0OfuWtVoeuAOcanJJaQwkxCp3mUvQHaxzEYsw9nW_ynWrq9YlFPCbTHDRUPAlQHEJNNaJYyjqkhD2L7JT3h_0BTcPZJHhxZEoEaDfI3Xv8sBJs6DGEgnnbhGtUuXMPKDqpbhC2Se-p04FxPufotUojGHfT1q0tvjVCzd6COVTGz4pjdpcUXRc7KZ6L__1aH-I8FME1JKTGIx_P47wYsos6ckoKH3RIPFk9X0hQ637orPUuGpefPErU23rQ3KX03ysbGK_ZMzdyruEPh3A1F90wh3cKhK-QxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NbUpHmRXZGSuzXq_Gjno6doQ8SjBnn63kAitOmHZu3nHqDyzaDRWmtQkuU_K0iMS26FUFSxx5VVquaM8HoeAMRWNV8dlRXp8zejF-m51jshgXwESp-YV58JMoxK2tBA3eK3UONzrjyd5mGoOejQ3knkS5E_Fxlz4tR7HKQybm9P1VlM643K401SSmCkOwhF7hc2InJyLBobkRcvevjb-QECa9uyEh-_9FQ5_Hsdhp8QFtVpSh5zacDy1N-BplzTMpiLGLN_J-js47aTa1EZvBXPP4ts-1rKuO8kjtvWISg45r-xfGOQKsehFmFQMb7Rj2GEzlbGztDw8jEV4WIpXsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mvkyBdw2WoJ9BGPXWTja7k8XHbf9Jsxialf4qXuear8v2wGAZuRujjqi_Vqzz3u1uazSLcZ2Q_HOkhqpigdigRPndjiZ8yGxLflR8eOjiqHn9TlnLssibhcw35fsbjs4-imj9SWQb_WQ-6HYngB7QyXF5VLG6SlSEOb-zk64Mrn1w8Bs8Kbj7Dy43g32NE9Fxy_4hpmkUl_-tCw16YxJswX7NVIpS0SqAZYKl8Y5bf2yHrepQof0A3qp9sW9Tq1rWJ4NIn-2Oo0_IPvWRkSJO22MvlPvbMS21SDdCNOyKXdV8kYCFqn7f0_s7I7-_E0KRrm7IhqRWCgDX32GVThSFg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">انفجارات عنيفة غرب تعز</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/naya_foriraq/87344" target="_blank">📅 11:57 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87343">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">انفجارات عنيفة غرب تعز</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/naya_foriraq/87343" target="_blank">📅 11:56 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87341">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FX6tmso7haY7YLUudPGztu_8cVnDm5bq86DsEamttRoxulcfIbFy3Lh2yteqEtdSPc6dEwl_2DCMaWn7-jfpMyv7j6UsRrJcTA6M2VMUzUDGzS8o7OY0Jv_k7rRA_YUV8XNTOgNVpPLwMzqagsf_pbPY6hWwvxtLv1DEmtCectGhaqo91JSoYlM157ZQF3mF-HXdIz48v7kG4Z-hoa0Pt4xq8l-jyjggFaanxccFK6uTw1TLlUHF0wdq7CHaxK8jw2qhAxPCodIbLS_s5CTe343Sleol1rbzsZ0oUSjnyBfSH3ekU4Ltl9z63rFlC6Vys80KTKVMGuLYH2vdaGnocA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MpPY9h5FEttV-MHDvD4n8snp_ELsNyN-UV6N66AiB0nxY_O4mIQMIyMH5vjthxuGQ5FjCZpecSygtPn3sPf8RO5NSTtPPP3U3JbGEHjtib4UFQhQyw6ITrvH8-B6JROkuvMD7OvNgXIJ4TxxybHkC_F_Tc5_RX_YAp_MZWDOLYw5qvdL6hQ2Ewq_zXFHGwnXTCajvddoc9G9OD5ikG98SS2LEqLvozDAbtYa5JWTXJBs7xhw32ovhaApk7-M2UKrwq7P4bhhqg-KwbIRsbWDmRAXksNbpL8-wJidiUZ1X0rlE40Ernm_3Hy7fKsd1U2tvUcIhlysuN3K-66fA1yIhw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">الله أكبر   أنصار الله في اليمن يطلقون الصواريخ باتجاه مواقع المرتزقة</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/naya_foriraq/87341" target="_blank">📅 11:53 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87340">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">الله أكبر
أنصار الله في اليمن يطلقون الصواريخ باتجاه مواقع المرتزقة</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/naya_foriraq/87340" target="_blank">📅 11:52 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87339">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🇹🇷
🔻
🇸🇾
إعلام العدو عن تقارير لبنانية: تركيا تدعو إلى اجتماع بين سوريا وحزب الله، معربةً عن استعدادها لشراكة اقتصادية وعسكرية في إطار قوة ستتمركز في لبنان.</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/naya_foriraq/87339" target="_blank">📅 11:44 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87338">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jj12E1tgebYweqzRT9HkII6AjJ7nZozMWHyLPed_SX44mpXjStMXF640_-VNRQ6EpMQa0H40TCtrAag4TPmbJnV0H-0_8HLggStvEsXPOO09GDRO9IPpD5RcNvannFPlNTxNcw8ulpSKdlKVGCVtTi38TqW2FSqrcH4y3af2vFOtEqFl1NzV5rY4o-3nBuRyGxp5ntmuAGf-uTyneS2pWnxUMVYZ3JtDVpvy7nWfKXitVxpuyfTvSTpZt0yiBDRKRmMVDIceMl_N_YuAq0kkkqoUZUU4kDA4v3cRurMNjf_T6rUecfGbteyCrqZqphti1NrpDNdlsmWxTrQuGSy5Ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الحصار بالحصار
القصف بالقصف
الصاروخ بالصاروخ
هذا ولم ولن ننسى دماء ٢٠ شهيد من الحشد الشعبي العراقي على يد ال سعود الظلمة</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/naya_foriraq/87338" target="_blank">📅 10:34 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87337">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">والعين كل العين على مدينة الملك سلمان
الأغوار وما بعد بعد بعد الأغوار
صديك هندي حضر كاميرا انت نفر زين</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/naya_foriraq/87337" target="_blank">📅 10:31 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87336">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">لبيك يا ابو جبريل
لبيك يا اكرم الكعبي</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/naya_foriraq/87336" target="_blank">📅 10:27 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87335">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">المتحدث باسم الحرس الثوري الإيراني: استراتيجيتنا هي الحفاظ على المضيق إلى حين موافقة العدو على جميع شروطنا</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/naya_foriraq/87335" target="_blank">📅 10:22 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87334">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromنايا - NAYA</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">سليت سيفي في سبيل الله #سالم_المسعودي#100K</div>
  <div class="tg-doc-extra">العباد Abou Al Fadl</div>
</div>
<a href="https://t.me/naya_foriraq/87334" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">سليت سيفي
#شاركها</div>
<div class="tg-footer">👁️ 8.62K · <a href="https://t.me/naya_foriraq/87334" target="_blank">📅 10:09 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87332">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🇸🇦
وزارة الطاقة السعودية: اندلاع حريق في إحدى المرافق التابعة لمصفاة أرامكو بجازان.</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/naya_foriraq/87332" target="_blank">📅 10:08 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87331">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">الله أكبر
🇾🇪
تمكنت القوات المسلحة اليمنية بفضل الله من استهداف مصفاة أرامكو في جيزان بطائرة مسيرة وكانت الإصابة دقيقة.
‏يأتي هذا الاستهداف ردا على اختراق العدو السعودي بمسيراته أجواء محافظتي صعدة وحجة.</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/naya_foriraq/87331" target="_blank">📅 10:07 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87328">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/evQqQipclgHgj_g1bZjxOtHKe9WkXLiuXOb-CnNFgObGAO8pvJeVRcPncdLH_2_huGrgkK-le9rWK0JUipfcdob9TcxJmuL-JmI-GxynKsAz3IqPgUgQpiD9FYeIyp7dlMwAYDgJ5Da2Zz_rfCirS7fhStd46Uq4hTU7ViYpN5cbNK5BWauSPb6FpIIBci-RHRVg-Sdl-ClzfccGdWLcAWYQ3pbCna13USC8Douof1ZKfYrG0U8nDqZ6W958iE6xTAacn3LqBV6XHJUkQ1gydGFCgZyo_4G4XbCnnuyg9jLnRX_Q3ZWSmJcQuhq8iTY3rrsemZZ9YD95NT31QSj3iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/g2fS0h92Ij0AVGhhFF2Pdk_MdKNv17t8zji84xs2ag4Q49LKS_uS_lKL5SEfAvBHbFnNh8k7ousTsoGug6iJgKtePaueZsDURLdhMrQy877SgJKxusFTAx0fb606anXYLj_hpmCd2OdTpmNS7c86S82COJ-8NEEOBF_u0Vq06HR57zlmkhS6BjWXuPippTq5kpTeqN4A5NrYe4hKBLIQnCbgKOlrXz98IRN4bc-oZKy4eJxLIaeXzlLkNL-p3mzTaPQEVVq3sD68aLe03PqwHZfJFcMqMSjHiEHt5ACtler5rpu4bbXOFFVJFZwfh_dxIjjyLQSzXWT1pKDI1Z5YUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Q8EImpA3lzLOVY30clBT2JvKazy8KrXmDJ-JyOvn_nsMvsEe-mqzeGu2mdqHTYsADyWJjIj0c9lcbvLrQ9ZiDdiwDF6HN1-V-f_ML6tS2W8KVmzQAWzY4zAhc5gNv5mban4t1eiMir-AvacPXqgcmhQ9JVIpVU38FeNb0WxBq2idxI9PHxbAsWFruiwi2b0V2SdCXHx_ypYg1NCNO77UoaXezT3u0hK2J0VtGyzf1Mhi7eQtB08Zj-O5R2fyn6slwq9Cqepms5h51mLhcKmow28us1nGT4IPmSlPkfSAx5-2D5p27gWiKgorteKl2R9MOz24M5AtLiDdfenk93BXVg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇾🇪
أظهرت بيانات نظام مراقبة الحرائق التابع لوكالة الفضاء الأمريكية اندلاع حرائق وتوهج حراري داخل مقر قاعدة اللواء الخامس العسكرية الواقعة بالقرب من منفذ الوديعة على الحدود اليمنية وذلك عقب تعرض القاعدة لسلسلة من الضربات الصاروخية والجوية بالطائرات المسيرة والتي نفذتها قوات "أنصار الله حيث أسفر الاستهداف عن انفجارات متتالية واشتعال النيران في مخازن للأسلحة والعتاد العسكري داخل الثكنة.</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/naya_foriraq/87328" target="_blank">📅 10:04 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87327">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🇱🇧
صحيفة لبنانية: إندونيسيا، وسويسرا، وبريطانيا، وأذربيجان تدعم تفكيك حزب الله عن أسلحته بينما رفضت إسرائيل أي دور لفرنسا.</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/naya_foriraq/87327" target="_blank">📅 08:34 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87326">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🇸🇦
إستهداف محطة غاز في مدينة الجبيل الصناعية بالسعودية والنيران تشتعل فيها.</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/naya_foriraq/87326" target="_blank">📅 05:12 · 18 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
