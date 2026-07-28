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
<img src="https://cdn4.telesco.pe/file/AncggfiCU95rumxzJa7ML3cTDnN1NjH_nk7JcelTkrhZjO7enmJUsOKAqv_vNfmJtVRP-VzzBYfXKO__qSmzR7Nd02wBlpzM8Wflc95ZDWtdEwQ5ZcPC7gg-uN7MJQQH_q3cLY2c4NWAHgMwTQqWJURgCyGlDrWw4Q-aMAHQdCLNTmyTKPrWg50eEzQMWnN4WI_iVbT_nV3ZxedVv3hHBdf3nBXcn9sFTCtdMAPPikzAp2tenASRdpbhztlL9d3w5Rn5ZrK4KIiorvnv1II4EI0n4Rp4Z3N3CLlcK8iO-IWpBl5Epue2MQ58CebKjzRBlqVT9MvYVEbTMgoV7FoZGg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 272K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-06 23:27:51</div>
<hr>

<div class="tg-post" id="msg-85924">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🇮🇶
انفجارات في محافظة اربيل قضاء كوية شمالي العراق.</div>
<div class="tg-footer">👁️ 2.34K · <a href="https://t.me/naya_foriraq/85924" target="_blank">📅 23:19 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85923">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">ستة انفجارات سمعت بوضوح قرب مؤسسات نفطية و غازية دون تفعيل صافرات الإنذار بالمنطقة الشرقية في السعودية</div>
<div class="tg-footer">👁️ 2.94K · <a href="https://t.me/naya_foriraq/85923" target="_blank">📅 23:19 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85921">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">ستة انفجارات سمعت بوضوح قرب مؤسسات نفطية و غازية دون تفعيل صافرات الإنذار بالمنطقة الشرقية في السعودية</div>
<div class="tg-footer">👁️ 8.1K · <a href="https://t.me/naya_foriraq/85921" target="_blank">📅 23:03 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85920">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DCOvfEBh8EGVNo1xYr7Qc1nby5uDkwuxxhBGZwEjVTf2l0xE-OlQwaR-ps40q1hg8B1TtahQodyDfi1_VchPQ5FVWtkvOuaIegwFeClGWBkvWdNA_3tElKFIMcUTSiaoT827fK4PQtae_Vy7sTslzX7kzmWrKMEeCsPx9i0iESTMZxamBFBtjm0AGwqoM2jNa1yOHah9EuyOV5P7uasBc-q5QYrCtWyocYfMUAu5QWWObdiwrLvtYWTEWyRjAoVIXt1cuMqx_u_Xl9BT3NwjobsYALvEr95NEUGSQnKJfMOXyrkemztwdq9iEilzBZtNVbD9DEIminRIfFVzTa79aQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حدث بحري استهداف سفينة في البحر الاحمر</div>
<div class="tg-footer">👁️ 8.13K · <a href="https://t.me/naya_foriraq/85920" target="_blank">📅 23:02 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85919">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">انفجارات عنيفة تهز المنطقة الشرقية من السعودية</div>
<div class="tg-footer">👁️ 7.35K · <a href="https://t.me/naya_foriraq/85919" target="_blank">📅 23:02 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85918">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">انفجارات عنيفة تهز المنطقة الشرقية من السعودية</div>
<div class="tg-footer">👁️ 7.07K · <a href="https://t.me/naya_foriraq/85918" target="_blank">📅 23:02 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85917">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">حدث بحري
استهداف سفينة في البحر الاحمر</div>
<div class="tg-footer">👁️ 7.37K · <a href="https://t.me/naya_foriraq/85917" target="_blank">📅 23:01 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85916">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">السعودية تعترف</div>
<div class="tg-footer">👁️ 7.26K · <a href="https://t.me/naya_foriraq/85916" target="_blank">📅 23:00 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85915">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 7.26K · <a href="https://t.me/naya_foriraq/85915" target="_blank">📅 23:00 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85914">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 7.2K · <a href="https://t.me/naya_foriraq/85914" target="_blank">📅 23:00 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85913">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/91015376f1.mp4?token=QzqxxVD9YMsl0LkNFp5vMZ9VnnxAai3k6-UDZpQbTCbZ_Ha8obMySo6Uj8ADlJ8ajACybVbac8JZh7EKMWMhAyHrAHxqfJ_FZXsUYQ6Yxgn7DeLGSTI8hRLR0okjgiq7DeMrY9p0GDW4H_x2mkkTcfm3fFdx4S53ZzwgjLuNpZQ9ZhMxpXy7J_5CFnzO2ay_MM5pqb_VUzHUpr85-GQDK-4tDC3JwjI2xaRRCTnXzJFzKMWJyPuDrX5q_Ue92Bvb3WvCT6Kfr8L_dOi79Mbtl0P8P4xhd_Qo3tC9b6A0ZqALutttbqgOd89xKI8Tw8ILS8bSAKv_NFIuVM3Aey-eqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/91015376f1.mp4?token=QzqxxVD9YMsl0LkNFp5vMZ9VnnxAai3k6-UDZpQbTCbZ_Ha8obMySo6Uj8ADlJ8ajACybVbac8JZh7EKMWMhAyHrAHxqfJ_FZXsUYQ6Yxgn7DeLGSTI8hRLR0okjgiq7DeMrY9p0GDW4H_x2mkkTcfm3fFdx4S53ZzwgjLuNpZQ9ZhMxpXy7J_5CFnzO2ay_MM5pqb_VUzHUpr85-GQDK-4tDC3JwjI2xaRRCTnXzJFzKMWJyPuDrX5q_Ue92Bvb3WvCT6Kfr8L_dOi79Mbtl0P8P4xhd_Qo3tC9b6A0ZqALutttbqgOd89xKI8Tw8ILS8bSAKv_NFIuVM3Aey-eqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
🇺🇸
النيران تشتعل من قاعدة الاحتلال الاميركي بمحافظة اربيل شمالي العراق عقب استهدافها بطائرة مسيرة.</div>
<div class="tg-footer">👁️ 9.27K · <a href="https://t.me/naya_foriraq/85913" target="_blank">📅 22:39 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85912">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">صفارات الانذار تدوي في غلاف غزة على اثر اطلاق صاروخ.</div>
<div class="tg-footer">👁️ 8K · <a href="https://t.me/naya_foriraq/85912" target="_blank">📅 22:36 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85911">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">صفارات الانذار تدوي في غلاف غزة على اثر اطلاق صاروخ.</div>
<div class="tg-footer">👁️ 8.39K · <a href="https://t.me/naya_foriraq/85911" target="_blank">📅 22:33 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85910">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ba0ebc773e.mp4?token=JUTcSMnnli0IKSRYcMUW1Kg5TNKFHSqKwb020CCU0BxmY7mqnDtLy5hrvzw_-4KyXGYcsaIrCzSkNUkVUdCD0AtSKS04TB9w-G6m9imrW195jn8vTwMs53FyRP0zqaIplY-UhXeoO6UP0C1ODduktKLWGnucISdSfxYCE-xq0lWvMcbYUGc5NEm7Pi8rd5baz_EbLCwwugH3ffUZZIKf26YiDnFdMqXEJCPCMfDzJecjxhhcPaWHpj7DQVc9qjxVBngQwt8nwDDCdIQWkxMxH29y1H6sJfbUevsX00EXZN0-F1nxHk9rlLu-K2Dhdb7Ebeze0u2I4RVzALM5Gkuy6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ba0ebc773e.mp4?token=JUTcSMnnli0IKSRYcMUW1Kg5TNKFHSqKwb020CCU0BxmY7mqnDtLy5hrvzw_-4KyXGYcsaIrCzSkNUkVUdCD0AtSKS04TB9w-G6m9imrW195jn8vTwMs53FyRP0zqaIplY-UhXeoO6UP0C1ODduktKLWGnucISdSfxYCE-xq0lWvMcbYUGc5NEm7Pi8rd5baz_EbLCwwugH3ffUZZIKf26YiDnFdMqXEJCPCMfDzJecjxhhcPaWHpj7DQVc9qjxVBngQwt8nwDDCdIQWkxMxH29y1H6sJfbUevsX00EXZN0-F1nxHk9rlLu-K2Dhdb7Ebeze0u2I4RVzALM5Gkuy6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
ارتفاع اعمدة الدخان قرب قاعدة الحرير في محافظة اربيل شمالي العراق.</div>
<div class="tg-footer">👁️ 8.67K · <a href="https://t.me/naya_foriraq/85910" target="_blank">📅 22:32 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85909">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🇮🇶
ارتفاع اعمدة الدخان قرب قاعدة الحرير في محافظة اربيل شمالي العراق.</div>
<div class="tg-footer">👁️ 7.47K · <a href="https://t.me/naya_foriraq/85909" target="_blank">📅 22:32 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85908">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 7.88K · <a href="https://t.me/naya_foriraq/85908" target="_blank">📅 22:31 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85907">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lyy4WsZ7tIrwMDOGdeLd5qzM3m05ADxGhDq6ZrS6sTTA1o__i0BQP98WybyHLTpg1MbbPt290C82ZYgUsF8SZC-n6XUb5VSCE8Vkjaf9KjfoK5w7If9zc0ZzwMx76FpzxQdLSQpGWyaxneSAKtk2klVYitjtmSC4oDx6zcSQq_dzk-imw0x-InXFhDXs41maH76T02E0WMoQw1sMG1Gl92BDutDNLvHR5-JR0qEzZyy6J3p34l7V6-JQBkfPKSRzs1_LYm3rA_SUBu1CETfUTueyDjo0GS4GqGEZhqKs-hG5OeQS-Xka13sUdKBIUUY8gtXKXtFmroPg-jeixpHF1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇦
وزير الخارجية الأوكراني متخوفا
😆
: اتصلت بنظيري الإيراني لإجراء محادثة صريحة وشددت على أن هدفنا هو تجنب أي تصعيد.</div>
<div class="tg-footer">👁️ 8.62K · <a href="https://t.me/naya_foriraq/85907" target="_blank">📅 22:26 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85906">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a504ea0426.mp4?token=kepUtw_r8ekAtu6tEce3TWqkd4bBZtduGx1Kw0Qfb7fvBmYWwa4qEkI1bG3lrkNacM9N39VXfLOgC8c2Cy9_vLSrR-hE8bhBb5uszzqDIiBc94ZkUEziiBuL-MOfvrXSjccKPLCVtXM9_2SLug1mdngkGBRpoPxQnCfTSDfUi1nANhCzZPtxuMPwB4qWHk-QFQ7yVDGsyTMT89IU1M8qKYheTu_gIwvCCfqwMzP59SkVLQ-t1WcGZI6crSv7sbgZ21_RJ1ngIgKKmRaLG69-5HGT2VTIpJEExw_uOcWHDK3aizosZrj87KO0kCdun0dRDBnQL92UZ1AALYYytUae3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a504ea0426.mp4?token=kepUtw_r8ekAtu6tEce3TWqkd4bBZtduGx1Kw0Qfb7fvBmYWwa4qEkI1bG3lrkNacM9N39VXfLOgC8c2Cy9_vLSrR-hE8bhBb5uszzqDIiBc94ZkUEziiBuL-MOfvrXSjccKPLCVtXM9_2SLug1mdngkGBRpoPxQnCfTSDfUi1nANhCzZPtxuMPwB4qWHk-QFQ7yVDGsyTMT89IU1M8qKYheTu_gIwvCCfqwMzP59SkVLQ-t1WcGZI6crSv7sbgZ21_RJ1ngIgKKmRaLG69-5HGT2VTIpJEExw_uOcWHDK3aizosZrj87KO0kCdun0dRDBnQL92UZ1AALYYytUae3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
‏ترامب يخوض معركة شرسة مع النعاس خلال مراسم العزاء لغراهام.</div>
<div class="tg-footer">👁️ 7.59K · <a href="https://t.me/naya_foriraq/85906" target="_blank">📅 22:26 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85905">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🇮🇱
العثور على جثة مجندة صهيونية في جنوب الكيان الصهيوني.</div>
<div class="tg-footer">👁️ 9.36K · <a href="https://t.me/naya_foriraq/85905" target="_blank">📅 21:57 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85902">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qMykCnt9MUergqgfWgjmrLXFr6_NOqqx-2Jj48RJ-fpKvgoy8BzGr6JNm1Dc_xOpFGkkrqJfj-sLNiIMeXG55nysZMAI6Rj1PeVn6PN6Mux0SPjlkGECgqNADj0p2W4NGR3VZ5GMSMo1FCg7BVLHREL6PD_Jgj8-gGv6GlKEuFpUDRyEp7LW-q2CI1Ly-vO_NnCQ0dqopQLxvV6ycix8n6oiYSBZrnGAzCmGw9WF-MdLgorWAO_ZWiuOCprRsKCLBn1cjSyZiYMaF7Z-WuTmP_05zjrixX8NY41OMYnGmTRCHD74-5DtcKFLVf_MeAZ5jEPQfLbPom-gfgFmglL4vQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/27343411e7.mp4?token=osF3Sf81K8p-xaS0N9pMwNM7qeiDGKCUaZAXwsLWy1FqxhzSmhbl06-5u52icLcog8qi8TAhVZNmhycwVtNWYk4TtJ1sM93XSz6gSu1qJ6hLm5O-7BwWyKf6gRDE-jJsuf9NswzKjJjTqgZAJJ4r6KX-9k9QUPzDRHgwaOOJEAxpctrBGtdM_y3-tPSUdkL0fY_htyFxCrw8cDqUxJh8Sn2Gh5Dt6q4Zq9ILdP6A6DtR3SrCqDr0VZ6Czp2bUYb_Gf8pX0Wjn8ZZJ6pgjimFHFYjCo2dp3N7o28dT1o0GVGIhTaCN5vKDo2DjBCmQKK_U-5xOqGcimuiLypAwnY_HA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/27343411e7.mp4?token=osF3Sf81K8p-xaS0N9pMwNM7qeiDGKCUaZAXwsLWy1FqxhzSmhbl06-5u52icLcog8qi8TAhVZNmhycwVtNWYk4TtJ1sM93XSz6gSu1qJ6hLm5O-7BwWyKf6gRDE-jJsuf9NswzKjJjTqgZAJJ4r6KX-9k9QUPzDRHgwaOOJEAxpctrBGtdM_y3-tPSUdkL0fY_htyFxCrw8cDqUxJh8Sn2Gh5Dt6q4Zq9ILdP6A6DtR3SrCqDr0VZ6Czp2bUYb_Gf8pX0Wjn8ZZJ6pgjimFHFYjCo2dp3N7o28dT1o0GVGIhTaCN5vKDo2DjBCmQKK_U-5xOqGcimuiLypAwnY_HA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇾🇪
🇸🇦
مشاهد من الاقمار الاصناعية تضهر تدمير في محطة تحلية المياه المالحة وتوليد الطاقة بمدينة ينبع السعودية بعد القصف من قبل انصار الله في اليمن.</div>
<div class="tg-footer">👁️ 9.44K · <a href="https://t.me/naya_foriraq/85902" target="_blank">📅 21:57 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85901">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/teyvVMaiQumvjwp0AJcG4g52eHtc8xKc-BEG8GeAk9AI4yvdLyNTZ0iYB9pyY6LwORwuIk0TLIe1-BVICetCZJna3kwI6UeItjPNpRTpwcilfKDspUia_flyXitNd2YSRWhRhdDNrhpXjYHGyi6LithixgQbF-UeBJOzqxTQO9fImeVCnO2z2JKt3BFKQugtdv_1tyav2koWPsB4Ic01c11QaKmw7X8jQyD6s38VybrrEMBxAnkKykeiOa31FrsBjkC6JI8-Li7_NfoX14lsCJ_sJpvdyiP0krjt6yRc5LlerQ9MNjS98o_F_hIzt4ZtHz72ddKlqrbBKLKfQPDEdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇾🇪
🇸🇦
‏السفينة التي استهدفها انصار الله في اليمن تم إيقاف تشغيل نظام التعرف الآلي (AIS) الخاص بالناقلة منذ 5 أيام، عندما كانت راسية آخر مرة في ينبع.</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/naya_foriraq/85901" target="_blank">📅 21:18 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85900">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🇱🇧
🇮🇱
اعلام العدو:
اطلاق صاروخ اعتراضي من كريات شمونة حول هدف جوي مشبوه انطلق من جنوب لبنان.</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/naya_foriraq/85900" target="_blank">📅 21:06 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85899">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/epmliGkCMICWwlknxpiXvV7ydvv9ymE38rsphd4AYQqJxvC-7gZOz6mh19YDlI13HqiOjSZcFmnjdX1OvNTe-P8MiNC7PeXjbRHguyXiRMXkpYuhw4GOtmyHugTdN1Vnt7UKKxOPv6A0iU_yRMZlHCdjyZKTfJheyLKv-a2C00yP6VNrcx5xDEqs33QUX6ps5yrvttojkjS66Qv22NgDcR7YJCJdGHhcCFL41yK0JEFiZTNcPes_ZXipBQnUTDLJY_Glhh-i7GBQCrzfor5BLEEhxcsCfI46FBeAUpEG4ZpNSGO1SaFBZxKlOur8TkcD3F_PfVjCZPJWI_nLNVyFcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇾🇪
🇸🇦
‏السفينة التي استهدفها انصار الله في اليمن تم إيقاف تشغيل نظام التعرف الآلي (AIS) الخاص بالناقلة منذ 5 أيام، عندما كانت راسية آخر مرة في ينبع.</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/naya_foriraq/85899" target="_blank">📅 20:51 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85898">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cepD3fXpV8zir-1DGgsw3F9RcmcYGGGZLJXLV5U0Wxd8QFcVfsgyb7Vszt7jxYuCAiCfbVskaxxML04cG9F9t7bam7S0OhGlBP-RpO5Fb9B-Z7vrNODwNa8QDeC41A-bp1i31Zq2N-SAgnHRhx85RbbzjSv0zp1-AtlbC5QaqO2jVaFCVRovEmTPTxFQ9AWypVWYulLUPQeXC2ayYm3YVEp336d9sCwHeWUvcquCcRHCKedI5ly-WKICQZs87VMn8aUzMIbe1E2nF6M2tDUOFBN963m93at70MxeP5d3JY4FtYwF21KxpfyByOepnNuZ5x8gVs43_mhYucbcalQAYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇾🇪
🇸🇦
‏السفينة التي استهدفها انصار الله في اليمن تم إيقاف تشغيل نظام التعرف الآلي (AIS) الخاص بالناقلة منذ 5 أيام، عندما كانت راسية آخر مرة في ينبع.</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/naya_foriraq/85898" target="_blank">📅 20:47 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85897">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">زيلينسكي المهرج يزعم: استهدفنا سفنا في بحر قزوين تنقل شحنات عسكرية لها صلة بإيران.</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/naya_foriraq/85897" target="_blank">📅 20:38 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85896">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🇮🇷
عراقجي:  أن العمل الانتهازي الذي انطلق من أوكرانيا لن يمر دون رد.  هاجم زيلينسكي سفينة تجارية إيرانية وقتل بحارًا. هذا العمل يُعد انتهاكًا صريحًا لميثاق الأمم المتحدة، ونُفذ بتحريض من إسرائيل لجرّ أوروبا إلى حرب معها.  خلال اتصالات هاتفية مع كايا كالاس،…</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/naya_foriraq/85896" target="_blank">📅 20:34 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85895">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P5AS893n-WHiQ3s98OWsYBuVNn4rR3qUi-YaJKmR5pkwWYE5Vb3ZbOJTvX3qyShIo8CMXOEr4Taf-HFWHpD-MZQcF3YZyR_RfRzyNWR7YdH6Nwtq8teIB7E1Uf4OXBWaJO0rNYT0g7rpL_Ck0SHKZqGwib0tl3AkPRJZ-O-zYiCAkhAthWaYrzIzNBbjsQKAu97lcUgwh2aXc7Nqvjq6sI_CTRGja_nDUOGTLPmzb1r1YdHJIHuoMS049vBe19Uio4eH8xfxHBn0T7aL789AFSjFXbKlML44MbU7n-kXQ46fByZAz9PduCs298JX8NEsoc3wUWv-P1ouelkNa-uLFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
🇮🇱
(أمريكا، لا تثقي به)
شعارات على شاشات عرض متجولة نصبت امام البيت الابيض اثناء لقاء نتنياهو وترامب.</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/naya_foriraq/85895" target="_blank">📅 20:29 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85894">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🇸🇦
مجلس الوزراء السعودي:
ندين اعتداء الميليشيات التابعة لإيران باليمن والعراق على منشآت نفطية وسفن بالبحر الأحمر.</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/naya_foriraq/85894" target="_blank">📅 20:14 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85893">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🇮🇶
وكالة أمن حكومة إقليم كردستان العراق:
خلال الأربع والعشرين ساعة الماضية، تعرضت خمس طائرات مسيرة لهجمات في كويا ومحيطها، وطائرة مسيرة أخرى لهجوم في شربازهر.</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/naya_foriraq/85893" target="_blank">📅 18:50 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85892">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LGBcYMB7kdY-SV302MgAV36TaRfmHqm6lekEB70U8z1YcpoCOGdKs5WhwM8dqoaOi5D19fsmjQPo9PZ_wRTq2v_dThQEVN85Lytf-7xTr8l5ZmzVKGrOpnYza4ITzqvBJy2zoAJVANNzxO99mZyBm8CUzo6pq18moXUNx483gecGr6z92KoGEZfNICCV6ToCY74bS6DRXoczXI-ioYUl2Ayca6HL-jTAo7zM3PkMQjaw8etuXGm0yNQlvn00guiWNqHqE1Re94Sz_hu9pU-7EAallUA-FKPgSS7Cnduo7Xokh8OM_696csFbKx_rm-1f_r-zk2QwSGDvXh2YuW-XBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
قائد فيلق القدس اسماعيل قاأني:
من المتوقع أن تتعلم الحكومة السعودية من سلوك أمريكا غير الحكيم والمكلف وأن تنهي الحصار المفروض على دولة مسلمة يبلغ عدد سكانها أكثر من 38 مليون نسمة.
إن توقعات المسلمين في جميع أنحاء العالم من المملكة العربية السعودية، التي تعتبر نفسها حامية الحرمين الشريفين، هي أنه بدلاً من مواصلة الحرب والضغط على أمة مسلمة مضطهدة، ينبغي عليها استخدام قوتها ومواردها لدعم الشعب الفلسطيني ومواجهة جرائم الكيان الصهيوني.
إن محاولة إنقاذ غزة المضطهدة مسألة شرف، وليس استمرار الحصار على الشعب اليمني المضطهد.</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/naya_foriraq/85892" target="_blank">📅 18:30 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85891">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🇮🇱
🇺🇸
اذاعة جيش العدو: ترامب يقول قبل ساعات من لقائه بنتنياهو: "لا أحتاج إلى أن يقدم لي نتنياهو معلومات استخباراتية عن إيران، إنه سيقدمها لأنه يريد أن يبقى مشاركا في الحرب."</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/naya_foriraq/85891" target="_blank">📅 18:29 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85890">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b2c4d8863e.mp4?token=GNfj_AHyK7ic7SG48d-LhgpA0ICVr17-D48qkHUpH_ftQPmQ6Wo1pX1HIb30ZdHpNXomjAtSuOjoDrDgHz5538cvjbCBKUEg89T--oefIQ6Y0OuFH71et9B6PnZG1tYO-GC3bzyxepPXgMD1bJJqWqRzYaxiOKqt3OAxSPh_NJsRaLtdLw4rIUNjEMi7clakIPIuyXcQrwXKbMyg-fiBj6azC5QLKcMkzxzTEED36pP3_zQRcuym1DXFPp5C1anbAd31mWJo4E3Tts_n7RNPX74EG86fbid4OTyYh4FOPifKYuqrQXrefRVb91LpiMIloMKKNOSeSeMD2YLVM-tjiw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b2c4d8863e.mp4?token=GNfj_AHyK7ic7SG48d-LhgpA0ICVr17-D48qkHUpH_ftQPmQ6Wo1pX1HIb30ZdHpNXomjAtSuOjoDrDgHz5538cvjbCBKUEg89T--oefIQ6Y0OuFH71et9B6PnZG1tYO-GC3bzyxepPXgMD1bJJqWqRzYaxiOKqt3OAxSPh_NJsRaLtdLw4rIUNjEMi7clakIPIuyXcQrwXKbMyg-fiBj6azC5QLKcMkzxzTEED36pP3_zQRcuym1DXFPp5C1anbAd31mWJo4E3Tts_n7RNPX74EG86fbid4OTyYh4FOPifKYuqrQXrefRVb91LpiMIloMKKNOSeSeMD2YLVM-tjiw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صور الأقمار الصناعية تظهر اثار هجمات انصار الله على البنية التحتية النفطية في ينبع السعودية على طول البحر الأحمر. ‏تظهر آثار حروق واضحة حول خزان تخزين كروي تابع لشركة أرامكو السعودية في محطة ينبع مما يشير إلى احتمال حدوث أضرار في الموقع.</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/naya_foriraq/85890" target="_blank">📅 17:22 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85889">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/faf5eced14.mp4?token=IWPsWhIF9riL2hvjnFUL7vbFRtFiAO1x_Ovn5PXDToTqjr_GTY-Ijlui_8KXLDPZ3PANNqev3wjEPZYZd06NJ3cyLAj-m2bseCJZe29OyQpIi5QFxs0HV-BEC8P1QwoFCqDdxXUQIwt9rQgbQjdIY-YSsHCuzEgn_pwDUo63YgiAjAWPIJDrIamYxK2uDr1pFVWIWeKZDYN2LInXX1M4VCg481CIZ7j5AJCTRVbKvzl4u2v_WunfvnG-2fUc31Mzj3Cg_kc7Kwn54Fy84UhlSOWJkFR6-CQcjTlreEVCxuQHL84gJOBWHI_OEthsADdZ_mw11EghtELbnc3VuyE68w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/faf5eced14.mp4?token=IWPsWhIF9riL2hvjnFUL7vbFRtFiAO1x_Ovn5PXDToTqjr_GTY-Ijlui_8KXLDPZ3PANNqev3wjEPZYZd06NJ3cyLAj-m2bseCJZe29OyQpIi5QFxs0HV-BEC8P1QwoFCqDdxXUQIwt9rQgbQjdIY-YSsHCuzEgn_pwDUo63YgiAjAWPIJDrIamYxK2uDr1pFVWIWeKZDYN2LInXX1M4VCg481CIZ7j5AJCTRVbKvzl4u2v_WunfvnG-2fUc31Mzj3Cg_kc7Kwn54Fy84UhlSOWJkFR6-CQcjTlreEVCxuQHL84gJOBWHI_OEthsADdZ_mw11EghtELbnc3VuyE68w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صور الأقمار الصناعية تظهر اثار هجمات انصار الله على البنية التحتية النفطية في ينبع السعودية على طول البحر الأحمر. ‏تظهر آثار حروق واضحة حول خزان تخزين كروي تابع لشركة أرامكو السعودية في محطة ينبع مما يشير إلى احتمال حدوث أضرار في الموقع.</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/naya_foriraq/85889" target="_blank">📅 17:21 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85888">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/937ee85070.mp4?token=DJ5QVYZ4-3SWd3FR7c1rR6UysTmSOffRrP1kGFddy0DBEpYCvLOnQXhw6AafiXrWq295uJ9jIymIymmGF51r4mjDWK5r0_fyFt6P1UDP5xXCPRLVPC15L9RdW8IGtnxTi1tJdfThsfAZJ9tTNtOUEEpfrBcdiYtrUw9sc0qYg-3YeZ8b55135INeuRP7Qw3yXCTRxgE5Nh6TZxeXmLowFV3EiDRUxWBDz25NQmdNwWXGrQJWblmKGFdewcH7EHbDVedSCirnBgZxSuGGd1nWX0cg08H2BJFvbd45o_pnAc83jXyEpQ6BigE9wAg9zAPmLX-TiStjDh347AZb96EQ5mgv1NP8TtSYjqM0OBmvWoFkxxpjRDkeHV93jqPOZbFVN1besEoDADcvrPZbApTp-8uG1NPGN1ZRqppQ4Mu2LzH2D1LOfyAxDkJcC_EjShk4AIwvPcE4u7VyFjddIQF-8YQxzc1clGsVm92o2H9isaTposoVe580SErLSTTedVJ6bcEVzsjFWj6JQCVDUt4-M9xgJc0p1wYd-TEFTnNuiIkRpAUMFjeyFS2OhQEEyOMeGRnxAxv5G989SROqUHrH1zlQUHpqmVrLRuKMpZWFgebSau14NzLJPlUUH4R6FU6rb-b1HjkkiSGKjiWUvd_Rj2PQlCFISO5dEQPVtnIFFng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/937ee85070.mp4?token=DJ5QVYZ4-3SWd3FR7c1rR6UysTmSOffRrP1kGFddy0DBEpYCvLOnQXhw6AafiXrWq295uJ9jIymIymmGF51r4mjDWK5r0_fyFt6P1UDP5xXCPRLVPC15L9RdW8IGtnxTi1tJdfThsfAZJ9tTNtOUEEpfrBcdiYtrUw9sc0qYg-3YeZ8b55135INeuRP7Qw3yXCTRxgE5Nh6TZxeXmLowFV3EiDRUxWBDz25NQmdNwWXGrQJWblmKGFdewcH7EHbDVedSCirnBgZxSuGGd1nWX0cg08H2BJFvbd45o_pnAc83jXyEpQ6BigE9wAg9zAPmLX-TiStjDh347AZb96EQ5mgv1NP8TtSYjqM0OBmvWoFkxxpjRDkeHV93jqPOZbFVN1besEoDADcvrPZbApTp-8uG1NPGN1ZRqppQ4Mu2LzH2D1LOfyAxDkJcC_EjShk4AIwvPcE4u7VyFjddIQF-8YQxzc1clGsVm92o2H9isaTposoVe580SErLSTTedVJ6bcEVzsjFWj6JQCVDUt4-M9xgJc0p1wYd-TEFTnNuiIkRpAUMFjeyFS2OhQEEyOMeGRnxAxv5G989SROqUHrH1zlQUHpqmVrLRuKMpZWFgebSau14NzLJPlUUH4R6FU6rb-b1HjkkiSGKjiWUvd_Rj2PQlCFISO5dEQPVtnIFFng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">أزمة الوقود متواصلة في محافظة أربيل باقليم كردستان شمالي العراق وسط استمرار طوابير المركبات أمام محطات التعبئة في ظل شكاوى المواطنين من صعوبة الحصول على الوقود وامتداد فترات الانتظار دون بوادر واضحة لانفراج الأزمة حتى الآن.</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/naya_foriraq/85888" target="_blank">📅 17:15 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85887">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d8db80c386.mp4?token=DsF-RRh72B6QxZHcRDQPBnKlWbGETli5VVe1Ys4-JT5I4GratYz-COyoDm4uKPhYrMOkA68T2o4pPYLCGu_Jw3Jcnnx_of42zgGpT6JrnHEZEHXx9L3bc3wL14kKkWijLvmfLw8nB9nRndETnp0kAmxH53ULH7mp6sOfMs6RMaCCLTtBe2Cl-GVrAR8r0pOpqQm7G5yorX7vtZI720Zpvb9E7Ukb0C_cFP7KlWRJDlHhO3jaZT5Gqi_cn96aqVU2dNxF_IbUYAOugnEvY_fAPwY4gyZ53PichSLM4MfIU5vJr_4ZOmOlQtsgxXQze0D920TOPoD242JIZI1i5a6y_gm5lzBCsV9xEpuiTXjvtrFdRjXlUntqG_J1DAZ1m0y8-j07l1rholZLO45kCrysdGTcqiIPccx8EKPWQ-2rz6UgGmKYBSAYNCDNnCyrUy8ZYUcRDyky0b3rnWOO8vQ7E732DLP7XO39ejb665AwFO9CoHxJP7zkuSNW6i3Mm3co43Rkv6aBlRV3wXaIrcJN4BZUunU6yCccCN73VVZ7N4QJ7G18GZHm_Y9lZLOm6RoRCbUXqKx0YkfdZwJrTWYo8nH695lPuH-UBV-yYcaJ7dwPAgWIGuXXlW7KOtHvBWSBZY4Nhg7Ot2xwyYbXafH0TGFhiWWriYFtVLkHSab0VZo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d8db80c386.mp4?token=DsF-RRh72B6QxZHcRDQPBnKlWbGETli5VVe1Ys4-JT5I4GratYz-COyoDm4uKPhYrMOkA68T2o4pPYLCGu_Jw3Jcnnx_of42zgGpT6JrnHEZEHXx9L3bc3wL14kKkWijLvmfLw8nB9nRndETnp0kAmxH53ULH7mp6sOfMs6RMaCCLTtBe2Cl-GVrAR8r0pOpqQm7G5yorX7vtZI720Zpvb9E7Ukb0C_cFP7KlWRJDlHhO3jaZT5Gqi_cn96aqVU2dNxF_IbUYAOugnEvY_fAPwY4gyZ53PichSLM4MfIU5vJr_4ZOmOlQtsgxXQze0D920TOPoD242JIZI1i5a6y_gm5lzBCsV9xEpuiTXjvtrFdRjXlUntqG_J1DAZ1m0y8-j07l1rholZLO45kCrysdGTcqiIPccx8EKPWQ-2rz6UgGmKYBSAYNCDNnCyrUy8ZYUcRDyky0b3rnWOO8vQ7E732DLP7XO39ejb665AwFO9CoHxJP7zkuSNW6i3Mm3co43Rkv6aBlRV3wXaIrcJN4BZUunU6yCccCN73VVZ7N4QJ7G18GZHm_Y9lZLOm6RoRCbUXqKx0YkfdZwJrTWYo8nH695lPuH-UBV-yYcaJ7dwPAgWIGuXXlW7KOtHvBWSBZY4Nhg7Ot2xwyYbXafH0TGFhiWWriYFtVLkHSab0VZo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامب عن الاعمال النووية الجارية في جبل بيك آكس الايراني: أنا لا أحتاج إلى أن يخبرني نتنياهو أشياء عن هذا الموضوع. نتنياهو يخبرني ذلك لأنه يريد أن يبقى متورطًا في الأمر. قلت له: "لماذا تحتاج إلى أن تخبرني بهذا؟" إذا لم تكن هناك صفقة، فسنقوم بتدمير هذا الموقع…</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/naya_foriraq/85887" target="_blank">📅 16:37 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85886">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3aab2d7d62.mp4?token=L8VTUfCjYxaSdoDV4eCJMSiWFTF6EOwUlFkIveyb8LE-yBgLDRthdrdDKjf1ZrDWQ3GPZwimmY_2REY-WUZAU0Hm00mWm6uAUQl9Z3XnmXsx_1raI7NwknExgLpzKWp7svvM0wzVpUPb12ck_TKQAxK7EudXDh7dX9kGm4boEJZEMdVjuRCW7s6LnNTeZ9bM1yMIu0X_wtnCi3CARChFiWIVTbwXZNQfz4pzDPD9E_vxFKmAfniphIS6oO24-PEbU6S9B4VfklMZ4mawhmQ6MUer6avKuQ2mPDuPfvpLE9D1O5zEirogNY-evYXHWANHeJoFL8c6MWlfo6QVTWQolp-aBlTNMXXLMqrDMnMLEQJ0PbW3W09m7OwwqijvxAcE_pAhosc5M7tInW3TqY4UNjkZeEbKa6prDPtnMqy6RnzI-7E3WWQq524pdYayGfOubU_ysTLZVjBg5wccn_KEpMN0BKThNpOR132Ysa2z_P5MjE6QPoENpXlPOEuAl6RF15gz3Bg2vtpzgdqtnkChdemqep1oetQY1GLA5BSHyUKNLh4VfZ2p9-c8kc-TTiDB2Vb1M1fbEJ0_2p7HZneos1qv5jjUM7tRqO0qBeWOkKS9HNXxKZ4K5sMCISbwhpWsTmHog7Pm41ptWyhJaSg35h5gZ72ycIsGrQ8DI3R9Urc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3aab2d7d62.mp4?token=L8VTUfCjYxaSdoDV4eCJMSiWFTF6EOwUlFkIveyb8LE-yBgLDRthdrdDKjf1ZrDWQ3GPZwimmY_2REY-WUZAU0Hm00mWm6uAUQl9Z3XnmXsx_1raI7NwknExgLpzKWp7svvM0wzVpUPb12ck_TKQAxK7EudXDh7dX9kGm4boEJZEMdVjuRCW7s6LnNTeZ9bM1yMIu0X_wtnCi3CARChFiWIVTbwXZNQfz4pzDPD9E_vxFKmAfniphIS6oO24-PEbU6S9B4VfklMZ4mawhmQ6MUer6avKuQ2mPDuPfvpLE9D1O5zEirogNY-evYXHWANHeJoFL8c6MWlfo6QVTWQolp-aBlTNMXXLMqrDMnMLEQJ0PbW3W09m7OwwqijvxAcE_pAhosc5M7tInW3TqY4UNjkZeEbKa6prDPtnMqy6RnzI-7E3WWQq524pdYayGfOubU_ysTLZVjBg5wccn_KEpMN0BKThNpOR132Ysa2z_P5MjE6QPoENpXlPOEuAl6RF15gz3Bg2vtpzgdqtnkChdemqep1oetQY1GLA5BSHyUKNLh4VfZ2p9-c8kc-TTiDB2Vb1M1fbEJ0_2p7HZneos1qv5jjUM7tRqO0qBeWOkKS9HNXxKZ4K5sMCISbwhpWsTmHog7Pm41ptWyhJaSg35h5gZ72ycIsGrQ8DI3R9Urc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
مقر خاتم الانبياء المركزي:
بسم الله الرحمن الرحيم
أعلن رئيس الولايات المتحدة، في أعقاب أعمال عدوانية وجهود متواصلة لزعزعة استقرار المنطقة، ما يلي:
‏سيتم دفع التعويضات من الأصول الإيرانية التي تم تجميدها عن الأضرار التي لحقت بالسفن التي تضررت خلال الحرب المفروضة على إيران، بسبب انعدام الأمن الذي خلقه الجيش الأمريكي، وانتهاكات الطرق غير القانونية وغير الآمنة في الجزء الجنوبي من مضيق هرمز.
‏وبينما نحذر الرئيس الأمريكي المجرم من عواقب هذا العمل غير القانوني، فإننا نعلن لجميع الشركات والدول التي ترحب باقتراح ترامب وتستخدم الأصول الإيرانية المجمدة تحت هذا الذريعة أنه من الآن فصاعدًا، لن تسمح القوات المسلحة للجمهورية الإسلامية الإيرانية لأي من سفنها بالمرور عبر مضيق هرمز.
‏ولا نصر إلا من الله العزيز الحكيم.</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/naya_foriraq/85886" target="_blank">📅 16:27 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85885">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">نايا - NAYA
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/naya_foriraq/85885" target="_blank">📅 16:22 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85884">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromنایا به فارسی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ga-j2AEXXP00_v8SyAXQOQoaKs0y8fNzSk9GrnJ8lA-DxqtYViwb-wV7H6VVnO4INmAqcDO_OKKGjozTcREnM6X4Ht0u6ZdML_IaRyyM9hZQlAHBAhmNN_f99A9iZLjH-Lf1OjW8h2wHK8s1g8JQp0f4ayjenESBfPbre8kcNpkzE5LPiQdRwMQbNzEN0UNQJBi_YutMtadz3KOl6cbCqKl---KMJUTdX70ePDZQWCoSuRu_8s75qm66u2sseNspA_zfhokD98JLgXok_SkpekmLl0AidmddTcrY8MkeNJWfWUapB2a2ItLGQYUKGeljievv0lABuXUNtg-JkyLASQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
کانال خبری ما در روبیکا و بله راه اندازی شد.
🔹
لینک کانال روبیکا:
rubika.ir/Naya_Fa
🔹
لینک کانال بله:
ble.ir/Naya_Fa
کانال سروش و ایتا به زودی ..</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/naya_foriraq/85884" target="_blank">📅 16:22 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85883">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KrgkSBaapXRfG85lYa3i7YWWOJdE_EA6SDlmmyM91lrBmbHbrM8b1l9Fa6Iu4QFkGc2HgXiVM0LUfcMd4gleNyS9IEhcr5qm1t9cVpYSWZNEwCBJs-qsCqW3DtAFU6Zw2h-WHA4vCdC3-YRylzogyMGUg0J58BVmh_LqvNeq_esZkU23jTxjhAFxap8mB92SxYqbwrh6KnKvb-dtUBJuS7w8DhOquKjiMzRNlxp8VUdNGqC1Luze3bTMzig-Jn0fotUMxaMuNUxhOqTjgFaMNBvHL0qBvaLOCu9Rmqh1OFiYj2aqZ0AG5T2e72QSN_oDIaeuLBnKkoLmUYn4ZZ2yDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامب عن الاعمال النووية الجارية في جبل بيك آكس الايراني: أنا لا أحتاج إلى أن يخبرني نتنياهو أشياء عن هذا الموضوع. نتنياهو يخبرني ذلك لأنه يريد أن يبقى متورطًا في الأمر. قلت له: "لماذا تحتاج إلى أن تخبرني بهذا؟" إذا لم تكن هناك صفقة، فسنقوم بتدمير هذا الموقع…</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/naya_foriraq/85883" target="_blank">📅 16:17 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85882">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">الأردن تعرضنا لهجوم بسبعين صاروخ و ٢٥ مسيرة خلال ١٦ يوم</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/naya_foriraq/85882" target="_blank">📅 16:13 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85881">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">‏الاعلامي: سمعنا أنكم تتحدثون مع قادة من إيران. لكن إيران صرحت علنًا قائلةً: "نحن لا نتحدث مع الولايات المتحدة".  ‏ترامب: حسناً، لقد خرجوا للتو وقالوا إننا نتحدث  ‏الاعلامي: هل يمكنك إذن أن تخبرني مع من تتحدث؟  ‏ترامب: لقد أجرينا بعض المحادثات الجيدة جداً</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/naya_foriraq/85881" target="_blank">📅 16:12 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85880">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">‏الاعلامي: سمعنا أنكم تتحدثون مع قادة من إيران. لكن إيران صرحت علنًا قائلةً: "نحن لا نتحدث مع الولايات المتحدة".
‏ترامب: حسناً، لقد خرجوا للتو وقالوا إننا نتحدث
‏الاعلامي: هل يمكنك إذن أن تخبرني مع من تتحدث؟
‏ترامب: لقد أجرينا بعض المحادثات الجيدة جداً</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/naya_foriraq/85880" target="_blank">📅 16:11 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85879">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🇰🇼
بسبب انقطاع التيار الكهربائي..
إغلاق بعض أجزاء مصفاة "الأزور" النفطية في الكويت والتي تبلغ طاقتها الإنتاجية 615,000 برميل يوميًا
الكويت تعورت</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/naya_foriraq/85879" target="_blank">📅 16:07 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85878">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🇯🇵
انفجار يهز المركز التجاري في اليابان وتسجيل عدة وفيات وفقدان اخرين على خلفية الزلزال الذي ضرب البلاد وانهيار المباني.</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/naya_foriraq/85878" target="_blank">📅 15:58 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85877">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🇾🇪
وزارة الخارجية اليمنية: إن إسقاط طائرات مسيرة تابعة للنظام السعودي في المجال الجوي اليمني يثبت انتهاك النظام السعودي للمجال الجوي، ويمنح اليمن الحق في الرد بالمثل. ولمن يستنكرون رفض اليمن انتهاك أجوائه: افتحوا أجواءكم للطيران السعودي يسرح فيها ويمرح كما…</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/naya_foriraq/85877" target="_blank">📅 15:52 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85876">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🇾🇪
وزارة الخارجية اليمنية:
إن إسقاط طائرات مسيرة تابعة للنظام السعودي في المجال الجوي اليمني يثبت انتهاك النظام السعودي للمجال الجوي، ويمنح اليمن الحق في الرد بالمثل.
ولمن يستنكرون رفض اليمن انتهاك أجوائه: افتحوا أجواءكم للطيران السعودي يسرح فيها ويمرح كما يشاء ويستهدف من أراد.</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/naya_foriraq/85876" target="_blank">📅 15:49 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85873">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TBvmc-Cz1bXKAQlwki-MOBdIGMpJNcorcgrddorFaTbuVUepgZM7CYplfpB_8zMSdtxAzbP18fvB4MFYc4vbaRomO9pBy3-_e1V4G3tqmr7KFzgiABbC31rWGotBSqG2QxjyGKzw1Z0-WFs0cNRVWwWbap6QBnRqFt_WE0_aLaAqD6oQZYCKD7tkbDNawnElycxQ0S4uCg9Z_cnZth5bsRR2dSI3wpuSnqk_CIY4Usq9VJX5l9jvvNHQJEwP8QiXNXJBUF5hTDpUX_fmDJlry_MrZr8XHlcSKztWhtDYFhLkPmG1j_DwPYkTcLMyLr0PMaj0o51fbqeZ-xWfwTcRHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HAtXbjTbTRSv9xtCtA9YUftP7NwqAlHYoWEU33zCUaoEhHbVJ01CjmXJEKN5FcxIOwuiuoeoD4eEL70LlQiVXg-Yukwl4nSrnWbZEu20LtWdm4OOhJUyHB0-qriQw0tOg0CaihYmCxOuddsOFS3EuQg9PQ3d_BpRO2cphXozGp0FBD8jLNys9oAqrShoA_b6LYn8nhF4MwFoGStrMJ4QLTUk75gTXGatM2tCG-tLAusN88LeK_oPU9178oTcfvQWyxR5caq3g6MJGCpieyHq1udjtNTag6WVsFZ9uq6IRQPsngiFqMD0XB-RRfiip-2w56Zkm7hvSJVMng-1u0Y0_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/q5GSyDwjYnQ2gSlvCD4Piz1oylUHlWtLfTFh87ZoIAxOPHqLjXLGoMdZyP7RdCDShce1B6ZTopL4nLgxln7-wf-RjB1ARQmtm9A89ij4UdFip-okeOuQ3jJ17iO1oGSLa-8mS8O76Nt-ehDtBsmN8h_TQpno-T38Abi-TLKpUcPK6IAqYIQiXiraDgsYvvGMb6lj5MJN3hajOh9DdiTRBsZqJoCslfkFHBaVTDF9NVCSNQDmp5ODnJbHf4gCkLVydkKQXbKX_48AI0sLkYZqEMuFBeIRzQ_FRQtVLUhY3EIvkxO-Z0w5bYc6rbGzL2ldWBBy8vr7PceRW_mtubDdPA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇮🇶
🇸🇾
هيئة المنافذ الحدودية العراقية تحبط محاولة إدخال أسلحة داخل شاحنة قادمة من سوريا.</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/naya_foriraq/85873" target="_blank">📅 14:56 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85872">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gd6LQiIxrxwaDXbx0RErreSHA6a235IrbZKTdMh2TJfcG0qFxP8WWdzwXF1_rL1Lke7HBYEfwlHmNEAeYpW7z6KkDDLJZFqA4bAh-7mWUtB4EhvET45BmrH84F6ARs3GxUyeFX-Dt0ZbC5WUEY7sIHe5dnqWDtELIJoiZizjJQ4MfcV4OaSkHL0Ex-zU7MBcc3JC-TFPEYzrkHaJ3nHcUXU0J5igI9L2O4_9roeiJ4M302gLd_MNh3eWS3W-FrPlosRMLgGi8_VKUUBep8AfGMSFN341UsAmmV8_dHxsCDHt9xzg45N8UGuSYdPH7ShsDhiAaHfUPCwDV8xf0lw8KQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
🇸🇾
هيئة المنافذ الحدودية العراقية تحبط محاولة إدخال أسلحة داخل شاحنة قادمة من سوريا.</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/naya_foriraq/85872" target="_blank">📅 14:47 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85871">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">شركة أرامكو السعودية تغلق مصفاة جازان للنفط التي تبلغ طاقتها الإنتاجية 400 ألف برميل يومياً عقب هجوم انصار الله قبل ايام.</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/naya_foriraq/85871" target="_blank">📅 14:35 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85870">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🇮🇱
وزير الشتات الإسرائيلي:
مشكلة إسرائيل الأساسية الآن هي سوريا خصوصا مع التمويل التركي.</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/naya_foriraq/85870" target="_blank">📅 14:29 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85869">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🇩🇿
🇦🇪
الرئيس الجزائري يهاجم الامارات:
هناك دويلة كل ما تضع قدمها تسيل الدم ولدينا أدلة ولا نريد زيادة الطين بلة في العالم العربي لما يشهده من انشقاقات ولو غير ذلك لقطعنا العلاقات معها منذ زمن بعيد</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/naya_foriraq/85869" target="_blank">📅 14:05 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85868">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">وزير الحرب الصهيوني المجرم كاتس متفاخرا: اليوم، لم يعد هناك حي "الشجاعية" في غزة، ولم يعد هناك مخيم "جباليا". كل تلك الأماكن لم تعد موجودة. لقد قال رئيس القيادة الجنوبية لي: "لا أرى أي منازل، بل أرى شاطئ البحر." لقد دمرنا غزة. في غزة، نحن ندمر ليس فقط ما هو…</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/naya_foriraq/85868" target="_blank">📅 13:39 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85867">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">وزير الحرب الصهيوني كاتس: تم تكليف "الشاباك" لحماية نتنياهو والقيادة السياسية والعسكرية الإسرائيلية من التهديد الايراني الخطير.</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/naya_foriraq/85867" target="_blank">📅 13:37 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85866">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🇮🇱
وزير الحرب الصهيوني يهاجم اردوغان: نحن لسنا الإمبراطورية المسيحية المتهاوية. القدس ليست القسطنطينية، التي غزوتموها عندما أسسستم الإمبراطورية العثمانية. لا تحاولوا استفزازنا. نصيحتي لأردوغان هي ألا يحاول استفزازنا، وألا يضع نفسه في الموقف الذي وضعته فيه إيران.…</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/naya_foriraq/85866" target="_blank">📅 13:34 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85865">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">هل سترد اسرائيل على الطائرة المسيرة التي أُطلقت في وقت سابق من اليوم من العراق؟!
🇮🇱
وزير الحرب الصهيوني كاتس: نحن نعرف كيف ندير الأمور - نحن مستعدون.</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/naya_foriraq/85865" target="_blank">📅 13:31 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85864">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🔻
صرف رواتب مجاهدي هيئة الحشد الشعبي.</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/naya_foriraq/85864" target="_blank">📅 13:21 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85863">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🇮🇱
🇮🇶
إعلام العدو عن مسؤول أمني: الطائرات المسيرة التي أسقطها الجيش يوم الأمس واليوم على الحدود مع الأردن، أطلقت من العراق.</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/naya_foriraq/85863" target="_blank">📅 13:15 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85862">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8d7bffd9c2.mp4?token=nA-p1K0-yeGT24rj2k9LHHhFUtrnIG0TCtiwD-8rihLdJOYERv9kU9XKPFZdAO1e3sQw9xrcZCY3xLtOVESuSdaP1Rip_xSgePbjbuzogpjvbxxSSq6NYdrwqeRNr9HUQqcbGdqELHqaEGYaHsI2I-Ab2UM7FPKvbZLkoInhE8BoUIWV8RJtPsWJvD_d4-YCVrjmxMw21uof_87Z-oBjnYUWG5sPF4pPbVYeW5OMzguUQ8YnS5uJPsWz_8ByABws5AYhVRLQ6YjO3dIVl9Kd6U6x2l0WeZ2jB5DkCpSDawE1HW64er0__qazG7SZrvq4Vs7tT77Ds9lYuC1TgyrAXULCIbG6gVtx9kuEuKzDMdX4fn1hoDWdLQwIamQ7OryofTq6RiFWJEmWB3g7giEAMycG37-M4nQEoDzojZQQGQBL137FYT8Sv1oohmi6W0EchIdALCZYxXd-UfcxJko6cMw6jqcaaoN0wBoU712iehgFrxBLLXZ-DblAudEbs9LaLlfyLRSX6h_Qk1gbVXoJW8phw-Pi3nI5gesjmi9xN91D2nTIFYAc9-9Sl9s8RggST4s2us2W3tRcl1tBH3deE7sUhtsgIHZ5lhi_6NVBD4K5IiLA5tRqC6z5cjgYnbzR8b0zm5VPP4042oqeUXbBeB_4RZUvRFgkIfEHfEsmLEM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8d7bffd9c2.mp4?token=nA-p1K0-yeGT24rj2k9LHHhFUtrnIG0TCtiwD-8rihLdJOYERv9kU9XKPFZdAO1e3sQw9xrcZCY3xLtOVESuSdaP1Rip_xSgePbjbuzogpjvbxxSSq6NYdrwqeRNr9HUQqcbGdqELHqaEGYaHsI2I-Ab2UM7FPKvbZLkoInhE8BoUIWV8RJtPsWJvD_d4-YCVrjmxMw21uof_87Z-oBjnYUWG5sPF4pPbVYeW5OMzguUQ8YnS5uJPsWz_8ByABws5AYhVRLQ6YjO3dIVl9Kd6U6x2l0WeZ2jB5DkCpSDawE1HW64er0__qazG7SZrvq4Vs7tT77Ds9lYuC1TgyrAXULCIbG6gVtx9kuEuKzDMdX4fn1hoDWdLQwIamQ7OryofTq6RiFWJEmWB3g7giEAMycG37-M4nQEoDzojZQQGQBL137FYT8Sv1oohmi6W0EchIdALCZYxXd-UfcxJko6cMw6jqcaaoN0wBoU712iehgFrxBLLXZ-DblAudEbs9LaLlfyLRSX6h_Qk1gbVXoJW8phw-Pi3nI5gesjmi9xN91D2nTIFYAc9-9Sl9s8RggST4s2us2W3tRcl1tBH3deE7sUhtsgIHZ5lhi_6NVBD4K5IiLA5tRqC6z5cjgYnbzR8b0zm5VPP4042oqeUXbBeB_4RZUvRFgkIfEHfEsmLEM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇱
🇺🇸
وزير الحرب الصهيوني كاتس:
نريد جدا معاودة شن الحرب على إيران لكن الولايات المتحدة تمنعنا، طائرات أميركية تشن غارات في إيران انطلاقا من مطارات إسرائيلية.</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/naya_foriraq/85862" target="_blank">📅 12:55 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85860">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a51c4750bb.mp4?token=i5Mw7LOn67ZWW9giA_E3s_mPDHHW2GNBjZUl6rj6Ywu_zU5TgQb-N4bRQX914ZvtQw7YPeIMuoFEiEvkWL5YY-m5TAzNrdo15FnxVgiagtw3IrwNcim994fw_By7Sb68j2P4HZgxWP0E5icSnvIx1IJbZ-KZc615aU1HmMDTxOGqdpS0GEavRvPq2Wq4r49tQiXHgfZ7QgKhwhhTmkg4TT1ReMhK79yxYcSgoY_aq3HNPHLLXDclbISNC9Naq5Lwt2VZD7J9OGmHwL-EO1B-mtktuK_Cza_eQDe3xL6QqpidGWb0HI_w9S_7ZrNIC90P2QuK6Fh7SW_eVExNOyVMHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a51c4750bb.mp4?token=i5Mw7LOn67ZWW9giA_E3s_mPDHHW2GNBjZUl6rj6Ywu_zU5TgQb-N4bRQX914ZvtQw7YPeIMuoFEiEvkWL5YY-m5TAzNrdo15FnxVgiagtw3IrwNcim994fw_By7Sb68j2P4HZgxWP0E5icSnvIx1IJbZ-KZc615aU1HmMDTxOGqdpS0GEavRvPq2Wq4r49tQiXHgfZ7QgKhwhhTmkg4TT1ReMhK79yxYcSgoY_aq3HNPHLLXDclbISNC9Naq5Lwt2VZD7J9OGmHwL-EO1B-mtktuK_Cza_eQDe3xL6QqpidGWb0HI_w9S_7ZrNIC90P2QuK6Fh7SW_eVExNOyVMHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">طيران مسير مجهول الهوية يحلق في اجواء مدينة الناصرية جنوبي العراق</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/naya_foriraq/85860" target="_blank">📅 12:39 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85859">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🇮🇱
🇮🇶
إعلام العدو عن مسؤول أمني: الطائرات المسيرة التي أسقطها الجيش يوم الأمس واليوم على الحدود مع الأردن، أطلقت من العراق.</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/naya_foriraq/85859" target="_blank">📅 11:58 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85858">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🇮🇱
🇮🇶
إعلام العدو عن مسؤول أمني:
الطائرات المسيرة التي أسقطها الجيش يوم الأمس واليوم على الحدود مع الأردن، أطلقت من العراق.</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/naya_foriraq/85858" target="_blank">📅 10:54 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85857">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🇮🇶
قيادي في حزب المعارضة الإيراني
: تعرضت مقراتنا في وادي آلانة لهجوم ب 5 طائرات مسيرة على الأقل فجر اليوم.</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/naya_foriraq/85857" target="_blank">📅 10:52 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85856">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">‏
🇮🇷
🇮🇱
🇦🇪
فايننشال تايمز:
مع انهيار وقف إطلاق النار الهش بين الولايات المتحدة وإيران، قامت الإمارات العربية المتحدة بمقامرة جريئة: إعادة تنشيط القنوات الدبلوماسية والاقتصادية مع إيران وإعادة الخطوط الجوية الإيرانية و ٢٠ الف مقيم بشكل مؤقت مع مضاعفة العلاقات العسكرية مع إسرائيل والولايات المتحدة.</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/naya_foriraq/85856" target="_blank">📅 10:20 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85855">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">إعلام أمريكي: سلطنة عُمان قدمت لإيران مقترحاً لآلية إقليمية مشتركة لإدارة مضيق هرمز تعتمد على رسوم طوعية</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/naya_foriraq/85855" target="_blank">📅 09:58 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85854">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🇮🇱
إذاعة جيش الاحتلال: الجيش الإسرائيلي قلّص عدد الجنود في كتيبة احتياط على الحدود اللبنانية بنسبة تقارب 30٪ مقارنة بالعدد الأصلي ؛ وأوضح قائد الكتيبة أنهم يواجهون أزمة حادة في عدد الأفراد تؤثر على قدرتهم على أداء المهام.</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/naya_foriraq/85854" target="_blank">📅 09:40 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85853">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">انفجارات تهز الأردن</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/naya_foriraq/85853" target="_blank">📅 08:58 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85852">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">انفجارات تهز الأردن</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/naya_foriraq/85852" target="_blank">📅 08:57 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85851">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">انفجارات عنيفة تهز المنطقة الشرقية من السعودية</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/naya_foriraq/85851" target="_blank">📅 08:51 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85850">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">انفجارات عنيفة تهز المنطقة الشرقية من السعودية</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/naya_foriraq/85850" target="_blank">📅 08:49 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85849">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b37b70352.mp4?token=Mn84UtWv1ZL1fYz8gQhCVTgpRaXIED6oFg1I3652jthfyYImzRcU-msLst3-wRfq2jiRkS0kCq78BN8MIbDWd94uKhMmsPaNx504xUzYV4wMZTP_heO1WaWeHokgpvpqGaNkQ81zUE7rHedStOc_qg-4SJLLWWwA5CP7RseTJci2aKPr76HEP2xNr4Gptwb5LSOoVTrxmKyOTfhZFwKsXZg6MnECCb6zAhxoyPaBT09bvAjb9fZXXytz97RMC70cfQjL0SqgMUZpq4xAWLPWELfCbtlNYfhAq43Fi77Khu-WX2_G29s58BirI1uOtVFmG3PnexLPrmS5flFHzqQWWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b37b70352.mp4?token=Mn84UtWv1ZL1fYz8gQhCVTgpRaXIED6oFg1I3652jthfyYImzRcU-msLst3-wRfq2jiRkS0kCq78BN8MIbDWd94uKhMmsPaNx504xUzYV4wMZTP_heO1WaWeHokgpvpqGaNkQ81zUE7rHedStOc_qg-4SJLLWWwA5CP7RseTJci2aKPr76HEP2xNr4Gptwb5LSOoVTrxmKyOTfhZFwKsXZg6MnECCb6zAhxoyPaBT09bvAjb9fZXXytz97RMC70cfQjL0SqgMUZpq4xAWLPWELfCbtlNYfhAq43Fi77Khu-WX2_G29s58BirI1uOtVFmG3PnexLPrmS5flFHzqQWWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
مشاهد أخرى لحظة حدوث الانفجارات في أحد مخازن الأسلحة التابعة لحزب المعارضة الإرهابي في محافظة السليمانية شمال العراق.</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/naya_foriraq/85849" target="_blank">📅 07:47 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85848">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🇮🇱
🇺🇸
هارتس العبرية: ‏يزور نتنياهو ترامب اليوم وهو يملك عدداً أقل من الحلفاء وخيارات غير جيدة.</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/naya_foriraq/85848" target="_blank">📅 07:33 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85847">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🇨🇳
زلزال بقوة 6 درجات يضرب مقاطعة تشينغهاي في الصين.</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/naya_foriraq/85847" target="_blank">📅 07:01 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85846">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a50630e63.mp4?token=eBqHznnBNUkhTkFypf8vyi_kVEQbPeEMQGyF7hdhvhpwb9PI8GlPICZGR-LZ1or6UPE-zNfAayaWIIhhRJ3PfVesf41X6OR47e8PBZIx-O_fAKUbWak6DXvx5Cg54-pKVk2NCZ3r0ZNeM0cIQfbt-Vgk20XxEh1TRDVml85803hxrIJCGK0lVmUpr38zG-Yit4PsonNPSkyHFnR4Y1KVG1BGS__CFyhhY3GKijBXUhtPGf7SjFWgTCuS7V9ubH88DMYAuCd4SSTZZYANNVAPcx780az7Hym5zS5EbQXqKTAa3mujQQTBjFuEzDswlxmyeYDDzaQ0BQH7oAK5MJwE3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a50630e63.mp4?token=eBqHznnBNUkhTkFypf8vyi_kVEQbPeEMQGyF7hdhvhpwb9PI8GlPICZGR-LZ1or6UPE-zNfAayaWIIhhRJ3PfVesf41X6OR47e8PBZIx-O_fAKUbWak6DXvx5Cg54-pKVk2NCZ3r0ZNeM0cIQfbt-Vgk20XxEh1TRDVml85803hxrIJCGK0lVmUpr38zG-Yit4PsonNPSkyHFnR4Y1KVG1BGS__CFyhhY3GKijBXUhtPGf7SjFWgTCuS7V9ubH88DMYAuCd4SSTZZYANNVAPcx780az7Hym5zS5EbQXqKTAa3mujQQTBjFuEzDswlxmyeYDDzaQ0BQH7oAK5MJwE3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
انفجارات ثانوية عنيفة في مخازن السلاح التابعة لإرهابيي المعارضة الكردية الإيرانية في محافظة السليمانية شمال العراق.</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/naya_foriraq/85846" target="_blank">📅 06:50 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85845">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🇮🇶
تصاعد أعمدة الدخان من داخل مقر تابع للإنفصاليين الأكراد في محافظة السليمانية شمالي العراق.</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/naya_foriraq/85845" target="_blank">📅 06:49 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85844">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🇮🇱
جيش الإحتلال الصهيوني:
إعتراض طائرة مسيرة عند الحدود الأردنية؛ التحقيقات تجري لمعرفة مصدر إطلاقها.</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/naya_foriraq/85844" target="_blank">📅 06:30 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85843">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RYMWY-TbaTorEjlhq2euZAOsf1RoFcHuQFViSxVeljfyDehjd12puV69PVWP4MLj1oP3mE85DcqVZqAYs_s3sutzWYwRv5m_oMqBFb-bE-sEfN_e3exKMt6IwIkim62GAfeiH2I-H4d4bW7ZqdosVl6XxiG30KshSjgFg1mfX3jBrlI7qepihmIIrZX5XVaHMpreNDOLRoPWtTBkaFIUW9N7jar3mwaYEnvZIJoKDdU6IqQnLl5_o_obOE32XCgmgDNxS1GkYaADcP81wB_Y8ek0MPpsKpQanozxy89FEFoR5MvG1M6VD9L7BHkyiKEgLU1ZsAFv65n57RK8QPCOAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
مع أول ساعات الصباح.. إستهداف أحد مقرات المعارضة الكردية الإرهابية في محافظة السليمانية شمالي العراق بسرب من الطائرات الإنتحارية.</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/naya_foriraq/85843" target="_blank">📅 05:56 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85842">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🇮🇶
مع أول ساعات الصباح..
إستهداف أحد مقرات المعارضة الكردية الإرهابية في محافظة السليمانية شمالي العراق بسرب من الطائرات الإنتحارية.</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/naya_foriraq/85842" target="_blank">📅 05:55 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85841">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">صافرات الانذار في غلاف غزة</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/naya_foriraq/85841" target="_blank">📅 05:54 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85840">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🇺🇸
مسؤول أميركي:
العقوبات والحصار البحري الأميركي سيستغرقان وقتا أطول لإجبار طهران على الجلوس إلى طاولة المفاوضات.</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/naya_foriraq/85840" target="_blank">📅 04:10 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85839">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c2655270d3.mp4?token=I6sY7CBzpWu3yVGdF8rGHXfQ4LpXiHqgFTqYoOs2sT7pYuSgb5p6ho6Uy3tb7CZfYnDFfsIJsHBldgdDWDQZzzvCfm-ef4SqjvpgVkd2kXwesFTGizmpnMJHMEGMbapiag_OpsgDFcDQlIicNpQ3jXhfkP39aI_f6NJIKT-1Uj4I66mmWYeir4fjhbrzaxJa11pHwW0fvUCT8pvCLdLan5e3gMWWVOmTSSTLsE9RzOHbbNH5w1ksE2oS3CeiCKpVGX4yd4Dpx-7WGGVyI1q1ZoA9rqVxup0rYVVadK48QOt0kPEuzN5rWFAyf-bDUVf4h0nN26h-b2VU7rvmodOF_0mdyvFIvd73Bv1tr_cSZY1KtorAWWTeOXm2FVJnsEbJwQ47m__9Oyx-D8NjkUP7iiD2MIPkGOavy8WX9Ds-ITtT4xt_jVPL0axFMHleG0Pnbg7bLoUIRmRR2CUU323UaWxmCHdqchFJr5ox-qhJ4hl3q1jgu68sMhC7Yf534KZMPFEHeu7FoHdpTRpCBeVshDZYnvq3iEf5l98rJZmCN-fYrZR062hA4zrYwKC_VEMcJrcS_m8pNrKFKq4xkjicps847Knpksk103BxeYCCjVyx18CqsT8omTU8VPpBrTVS7cRscOb4khHD0UWk547N-Le3Nt1e8RRtYMtHqDEwPZY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c2655270d3.mp4?token=I6sY7CBzpWu3yVGdF8rGHXfQ4LpXiHqgFTqYoOs2sT7pYuSgb5p6ho6Uy3tb7CZfYnDFfsIJsHBldgdDWDQZzzvCfm-ef4SqjvpgVkd2kXwesFTGizmpnMJHMEGMbapiag_OpsgDFcDQlIicNpQ3jXhfkP39aI_f6NJIKT-1Uj4I66mmWYeir4fjhbrzaxJa11pHwW0fvUCT8pvCLdLan5e3gMWWVOmTSSTLsE9RzOHbbNH5w1ksE2oS3CeiCKpVGX4yd4Dpx-7WGGVyI1q1ZoA9rqVxup0rYVVadK48QOt0kPEuzN5rWFAyf-bDUVf4h0nN26h-b2VU7rvmodOF_0mdyvFIvd73Bv1tr_cSZY1KtorAWWTeOXm2FVJnsEbJwQ47m__9Oyx-D8NjkUP7iiD2MIPkGOavy8WX9Ds-ITtT4xt_jVPL0axFMHleG0Pnbg7bLoUIRmRR2CUU323UaWxmCHdqchFJr5ox-qhJ4hl3q1jgu68sMhC7Yf534KZMPFEHeu7FoHdpTRpCBeVshDZYnvq3iEf5l98rJZmCN-fYrZR062hA4zrYwKC_VEMcJrcS_m8pNrKFKq4xkjicps847Knpksk103BxeYCCjVyx18CqsT8omTU8VPpBrTVS7cRscOb4khHD0UWk547N-Le3Nt1e8RRtYMtHqDEwPZY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
من تصدي دفاعات الإنفصاليين لهجوم أسراب المسيرات الانتحارية على مقراتهم في أربيل
😆</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/naya_foriraq/85839" target="_blank">📅 01:46 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85837">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/293704c82e.mp4?token=TF2dem_Pzc1arDSoubGf9rwrySiPuWkmfi_--Qa6YD6xPB8oke2ojW3hCTgwp-2RJogGLZDMX2gHQALkMFO7xVGR9fPe2alchCcYTfAN0B7KDYcoQx3-jxj4ROfXPYjgTqXoy7szqJxqZcKCue7jQUbIhsLRvDpU63i76mdq5Yi_O7Ew4ag1Xix4J4s6hRRveU8JxTAtyNdN7totHAeF-MFlRfLtaFyHIzAWS1woTO2GOD9bQiuqvlGuqhCZwJuMdOQisai5KYstG-tSSiFBkLEGsUvDq97Fp8n82ganWkSSoC5KbJtINxPio8diYpSHiZPoPGao00WsWbmEgXnfPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/293704c82e.mp4?token=TF2dem_Pzc1arDSoubGf9rwrySiPuWkmfi_--Qa6YD6xPB8oke2ojW3hCTgwp-2RJogGLZDMX2gHQALkMFO7xVGR9fPe2alchCcYTfAN0B7KDYcoQx3-jxj4ROfXPYjgTqXoy7szqJxqZcKCue7jQUbIhsLRvDpU63i76mdq5Yi_O7Ew4ag1Xix4J4s6hRRveU8JxTAtyNdN7totHAeF-MFlRfLtaFyHIzAWS1woTO2GOD9bQiuqvlGuqhCZwJuMdOQisai5KYstG-tSSiFBkLEGsUvDq97Fp8n82ganWkSSoC5KbJtINxPio8diYpSHiZPoPGao00WsWbmEgXnfPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توثيق يظهر لحظة وصول المسيرة الانتحارية إلى هدفها والانفجار الكبير داخل مقر الانفصاليين الأكراد في محافظة أربيل شمالي العراق.</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/naya_foriraq/85837" target="_blank">📅 01:39 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85836">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a1c105dc2.mp4?token=o6EgeeaERy3SFVjoJX9xLHKvccc2sQDXPeC1n09rbzmgVBZ_4M1xhun6rXty9cir_mz5BpiJfErT8MHj7OqC6miaxrOAAk4wBFLhfm77YdsSdoNtnLEy3NDPnJmAcrhvqyykrSwc5FQalaPn7I87KCjfFnLZTt2uunjAggKqaSRO57HY3m087n2F51FqkT2_i61rEpZm-Pbj49Wtd4eDDDkCvDF8XczMGAwKeu2i79QbbkPQqLT62eFoQfgZLAtI90X00-tNQ9fcyfWrc33NlXvvUK0dCmiLvxKWwrkzPTUvGKydAZ4K8H16N-P27YCGFPdHUaHStVAXDLzkYeH-2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a1c105dc2.mp4?token=o6EgeeaERy3SFVjoJX9xLHKvccc2sQDXPeC1n09rbzmgVBZ_4M1xhun6rXty9cir_mz5BpiJfErT8MHj7OqC6miaxrOAAk4wBFLhfm77YdsSdoNtnLEy3NDPnJmAcrhvqyykrSwc5FQalaPn7I87KCjfFnLZTt2uunjAggKqaSRO57HY3m087n2F51FqkT2_i61rEpZm-Pbj49Wtd4eDDDkCvDF8XczMGAwKeu2i79QbbkPQqLT62eFoQfgZLAtI90X00-tNQ9fcyfWrc33NlXvvUK0dCmiLvxKWwrkzPTUvGKydAZ4K8H16N-P27YCGFPdHUaHStVAXDLzkYeH-2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صافرات الانذار تدوي في القنصلية الامريكية بمحافظة أربيل</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/naya_foriraq/85836" target="_blank">📅 01:36 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85835">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40c75dde8d.mp4?token=D_0YQMrSSXnRi7Gliv1SKuJU5xoR6_NK220ehTtuP74wwXsz6ASm_7J0aEfWUCHj8dS3VJhMBuAWxSgkeJmTWv6jsgDTKJwASgKpYbjly7WsqY4toghDrkFMDK-EX68Sp6eTCZo5Ld-ay_dvASyJeGcU9CH8he71Pi6D2nRnUgyC_4qxApzb48XsOh-SixrmXryc2LLdvWrKUAtmk2ouUxLBCsCJv1kKoZRaNyP2vRAujuQ0yrC2Kka2p2119BwBhb9ZG5SfN567TaDhQ9g6KZkOGOP-Eaaeos4Vb_lk9e2P8XBAqKLBQ1d0Eao5UMh5PxsjK_A3A-gt_SglOsDFQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40c75dde8d.mp4?token=D_0YQMrSSXnRi7Gliv1SKuJU5xoR6_NK220ehTtuP74wwXsz6ASm_7J0aEfWUCHj8dS3VJhMBuAWxSgkeJmTWv6jsgDTKJwASgKpYbjly7WsqY4toghDrkFMDK-EX68Sp6eTCZo5Ld-ay_dvASyJeGcU9CH8he71Pi6D2nRnUgyC_4qxApzb48XsOh-SixrmXryc2LLdvWrKUAtmk2ouUxLBCsCJv1kKoZRaNyP2vRAujuQ0yrC2Kka2p2119BwBhb9ZG5SfN567TaDhQ9g6KZkOGOP-Eaaeos4Vb_lk9e2P8XBAqKLBQ1d0Eao5UMh5PxsjK_A3A-gt_SglOsDFQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صافرات الانذار تدوي في القنصلية الامريكية بمحافظة أربيل</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/naya_foriraq/85835" target="_blank">📅 01:34 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85834">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🇱🇧
🇮🇱
غارة صهيونية تستهدف تلة علي طاهر جنوبي لبنان.</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/naya_foriraq/85834" target="_blank">📅 01:27 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85833">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1dbfd07761.mp4?token=njMJKIE7SHLwfzZS393NRxlXYSqBt4bs7vWIhN1ZS-hNN58yGbdXOa2_x1W4qZQ1Q1ncmid_u9HV36qCNTbKaeDj84UM3L-p-jnmoIW6U0XPco1vhfSBw9yn3ThbYrV9AMxA7qJJx0xfY59PYGI1BnMR09YHfBwHR_hQfx6N55LBuB9V4UMek0kIedZrjq9_pfS0DliB5MNY3gMzmTq1OhYovw1sCdNcS6WwaOLHysyhdDAuHM6A_nAHGexkBk2U9Hf-DtbJocozhKlNEOeZp9Xhw50rLyr56g82ZAGYJ7llh26J67T7gEEMsLzbBVoaFUhcir1wvKi-rZFtO29MpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1dbfd07761.mp4?token=njMJKIE7SHLwfzZS393NRxlXYSqBt4bs7vWIhN1ZS-hNN58yGbdXOa2_x1W4qZQ1Q1ncmid_u9HV36qCNTbKaeDj84UM3L-p-jnmoIW6U0XPco1vhfSBw9yn3ThbYrV9AMxA7qJJx0xfY59PYGI1BnMR09YHfBwHR_hQfx6N55LBuB9V4UMek0kIedZrjq9_pfS0DliB5MNY3gMzmTq1OhYovw1sCdNcS6WwaOLHysyhdDAuHM6A_nAHGexkBk2U9Hf-DtbJocozhKlNEOeZp9Xhw50rLyr56g82ZAGYJ7llh26J67T7gEEMsLzbBVoaFUhcir1wvKi-rZFtO29MpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اندلاع حريق واسع جراء الهجوم المسير الانتحاري الذي طال مقرات المعارضة الكردية في محافظة دهوك شمالي العراق.</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/naya_foriraq/85833" target="_blank">📅 01:11 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85831">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cef242c138.mp4?token=kmStgG5onBLKYfcgpfQnLSK6_c1yzVuhdVcpPsDUCG4gQ2XEheYa6eWqlHR7ZO_sO04Q_olz6MOp027haA4bU1ScqiHx2dzM8t5R6EoNkL1ZYBuezrRTsQh4mDnoeQzeeAndkPTsxbG-aUDscIH6JfpLQCcrIgNmi16Yw_iK46NNhYQt95CFeZEsxEWcbryiooH_SL34-2mDGBdQorr8rKGRrAYCYwI2YxWGyBNVEBHNTny6m1XdgTyqwWBjCsWgohMyVB341yW-QziePWF9DW7kh-NyYcF-T5h6u54UYBfznVCzI9ljLWHtEaAFy-rPweCtK6PhAfrdm5hsZipTAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cef242c138.mp4?token=kmStgG5onBLKYfcgpfQnLSK6_c1yzVuhdVcpPsDUCG4gQ2XEheYa6eWqlHR7ZO_sO04Q_olz6MOp027haA4bU1ScqiHx2dzM8t5R6EoNkL1ZYBuezrRTsQh4mDnoeQzeeAndkPTsxbG-aUDscIH6JfpLQCcrIgNmi16Yw_iK46NNhYQt95CFeZEsxEWcbryiooH_SL34-2mDGBdQorr8rKGRrAYCYwI2YxWGyBNVEBHNTny6m1XdgTyqwWBjCsWgohMyVB341yW-QziePWF9DW7kh-NyYcF-T5h6u54UYBfznVCzI9ljLWHtEaAFy-rPweCtK6PhAfrdm5hsZipTAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">استهداف مباشر وانفجار عنيف أخر يطال مقر تابع للانفصاليين الأكراد في محافظة أربيل</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/naya_foriraq/85831" target="_blank">📅 01:07 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85830">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6577c5fe83.mp4?token=Gar-9XhZ350vqtnKkXRTm5Av_GW_ziQYsacCcaHdzEuabRR4cf0JU3u7o_Pgu2iRzj2aQvUaDQoTgnZyQJdcstBg1aG9A1mdAcJtBcq25Qo-SaoRTOGDP2ulU7dIvvJhZLY_Msh6dbbUEWvyUMh4mo76xbDcfAFXOfFr508OOo-sIEvZ0j-lzswg_1AFEczMR08A-vBJJWd_dAeu0TP4LdAbOOQHLNqC0XJgp8DAiarvJEKxzXAo0CY0W10qtlH5aNTv7x4dNGora5ltQACr1WGMXsjdQwzDljQfxTUNhiZsTVhhGOkllvjdAP-nEkgchfX1zyW4J1Zwe-98EPmJ6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6577c5fe83.mp4?token=Gar-9XhZ350vqtnKkXRTm5Av_GW_ziQYsacCcaHdzEuabRR4cf0JU3u7o_Pgu2iRzj2aQvUaDQoTgnZyQJdcstBg1aG9A1mdAcJtBcq25Qo-SaoRTOGDP2ulU7dIvvJhZLY_Msh6dbbUEWvyUMh4mo76xbDcfAFXOfFr508OOo-sIEvZ0j-lzswg_1AFEczMR08A-vBJJWd_dAeu0TP4LdAbOOQHLNqC0XJgp8DAiarvJEKxzXAo0CY0W10qtlH5aNTv7x4dNGora5ltQACr1WGMXsjdQwzDljQfxTUNhiZsTVhhGOkllvjdAP-nEkgchfX1zyW4J1Zwe-98EPmJ6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">استمرار الانفجارات العنيفة داخل مقرات المعارضة الكردية الإرهابية في محافظة أربيل شمالي العراق</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/naya_foriraq/85830" target="_blank">📅 01:04 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85829">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2bba43befb.mp4?token=o9O7V9SIat46tDZZpJfyQCY-FHj-bBg8DbbM7l3HjKNJ5pGx1j1-vqbLMfx3AONmB0MVZ1fHjj24Ef4rq0Eew3WUdHWXHDz0Ke2eZqGQIF7ZsyvE7oopaE_LB4UQ245RtVztYRFfLPlouQFW86GOYSlvSHYL9xfhM_rWnvp1VbYZqo2P77-qRY98sQKzOHrsWbrecgts6X9D4iknE1RWJ7zeFNzPeVaTtxY6v8la1xnVCab3RjTBufaG1H5dQFugMsU-w63tysIdq2hRMBF5Vub8KzyBxoMt0coiuF1Mv93sSvzArQmfIjV3qvw_DHx6qXVLyMvtDnpiuVeqA4b_6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2bba43befb.mp4?token=o9O7V9SIat46tDZZpJfyQCY-FHj-bBg8DbbM7l3HjKNJ5pGx1j1-vqbLMfx3AONmB0MVZ1fHjj24Ef4rq0Eew3WUdHWXHDz0Ke2eZqGQIF7ZsyvE7oopaE_LB4UQ245RtVztYRFfLPlouQFW86GOYSlvSHYL9xfhM_rWnvp1VbYZqo2P77-qRY98sQKzOHrsWbrecgts6X9D4iknE1RWJ7zeFNzPeVaTtxY6v8la1xnVCab3RjTBufaG1H5dQFugMsU-w63tysIdq2hRMBF5Vub8KzyBxoMt0coiuF1Mv93sSvzArQmfIjV3qvw_DHx6qXVLyMvtDnpiuVeqA4b_6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نشوب حرائق واسعة داخل مقرات المعارضة الكردية الإيرانية في محافظة أربيل العراق عقب استهدافها بالطيران المسير الانتحاري.</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/naya_foriraq/85829" target="_blank">📅 01:02 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85828">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/32f8527a49.mp4?token=pXmt0GzCB7P5Nhv6FLaXXQzmZ_wzgpRFnTMmJ5d8r82FDXDMZucuX0-lrTBee2GRH47pqcqdEuGGJ-H8SdpQ69ohlB6DT5OXuzaTaofqVW49CgtcYY8regaBb79sKpDI7WoHGqCVRo13tO9o4d_Eb94qCD9A-Xajut16SpwBhOtt0lEcQWyR2KbIjI8638sBeYG6eBeZiYB5-TIPYNZsR8qjMohs8ybvh-jRnwRHECWMkVuEhBnwE5924-ChCo9XbCx8F8COBzBd3X5lxKbmAel00XOWTFc8_s9d_e_QjIKRVy0-N0s-XFjHSgV5B2BV3HrVQvcfB0BUKO3fHezoig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/32f8527a49.mp4?token=pXmt0GzCB7P5Nhv6FLaXXQzmZ_wzgpRFnTMmJ5d8r82FDXDMZucuX0-lrTBee2GRH47pqcqdEuGGJ-H8SdpQ69ohlB6DT5OXuzaTaofqVW49CgtcYY8regaBb79sKpDI7WoHGqCVRo13tO9o4d_Eb94qCD9A-Xajut16SpwBhOtt0lEcQWyR2KbIjI8638sBeYG6eBeZiYB5-TIPYNZsR8qjMohs8ybvh-jRnwRHECWMkVuEhBnwE5924-ChCo9XbCx8F8COBzBd3X5lxKbmAel00XOWTFc8_s9d_e_QjIKRVy0-N0s-XFjHSgV5B2BV3HrVQvcfB0BUKO3fHezoig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آتش سوزی در مقرهای تجزیه طلبان تروریست در اربیل عراق.</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/naya_foriraq/85828" target="_blank">📅 01:00 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85827">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/84a82d562b.mp4?token=bwLTrsRTIJdLxKkCLWemLkWo2zB3bH-zNGzX_Aw94n74mlEwcSzEVckBY3mG5Sgaf6debLqQWOO5raSVyGhiALsDMp5yX1OdNwIkCHUqQwqlprUjqhJYadbzi6p5VYrxN5CPKdcefr09iGV4Rub8aDGgycQCbbpy5tW4QXvQhZINK3Gy7OV81QSJShruBfL0el_a8YMaLNIObFiw4srrRYw3rx5PBu4I4o1ymaqnscaUNsVPbKWVTeO8OmReD_Wri92zxEqe74AiHOOrtiKrJd-WZhCFZLlBOJrUqR2tM4PD1aCarJ4Sd3jOsGZGzESqroGqezrZFRwJQI6k1ml_-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/84a82d562b.mp4?token=bwLTrsRTIJdLxKkCLWemLkWo2zB3bH-zNGzX_Aw94n74mlEwcSzEVckBY3mG5Sgaf6debLqQWOO5raSVyGhiALsDMp5yX1OdNwIkCHUqQwqlprUjqhJYadbzi6p5VYrxN5CPKdcefr09iGV4Rub8aDGgycQCbbpy5tW4QXvQhZINK3Gy7OV81QSJShruBfL0el_a8YMaLNIObFiw4srrRYw3rx5PBu4I4o1ymaqnscaUNsVPbKWVTeO8OmReD_Wri92zxEqe74AiHOOrtiKrJd-WZhCFZLlBOJrUqR2tM4PD1aCarJ4Sd3jOsGZGzESqroGqezrZFRwJQI6k1ml_-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عملیات لت و پار کردن تروریست‌های تجزیه طلب در شمال عراق ادامه دارد.</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/naya_foriraq/85827" target="_blank">📅 01:00 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85826">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a3b235c206.mp4?token=igY3Axcu6SZImd_l2WlI3HhxeDDAuWtIRdB3dJdXVSKLzm9FAT3-MZOE4pttbtHtfuwWW70spxwOt-72lAqbHElvtdO5ARmgpWpo1CE_Q_MoMET5wAduScId42MRt7NwgFdDG4Tm4CqHJkUGqO-67cWYe6UaDAoeJfZTeFqTWtEQXUyxeXm70o9vB8qZFvXAqevzA7sZBzfuiPewpZwTpmP1Tx1LDG2BRWGqQkUABBgOevmcKuCWkM3GW6VsBVoGRziRzc2zdH_OYcORq1uqrD-kgfFAmqtSLvKtLZRFWWx-XdwsyxDpEYLQCsZWHcxBri2zYsxl-fpMWnKwHWks_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a3b235c206.mp4?token=igY3Axcu6SZImd_l2WlI3HhxeDDAuWtIRdB3dJdXVSKLzm9FAT3-MZOE4pttbtHtfuwWW70spxwOt-72lAqbHElvtdO5ARmgpWpo1CE_Q_MoMET5wAduScId42MRt7NwgFdDG4Tm4CqHJkUGqO-67cWYe6UaDAoeJfZTeFqTWtEQXUyxeXm70o9vB8qZFvXAqevzA7sZBzfuiPewpZwTpmP1Tx1LDG2BRWGqQkUABBgOevmcKuCWkM3GW6VsBVoGRziRzc2zdH_OYcORq1uqrD-kgfFAmqtSLvKtLZRFWWx-XdwsyxDpEYLQCsZWHcxBri2zYsxl-fpMWnKwHWks_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توثيق للحظة إستهداف مقر تابع للإنفصاليين في محافظة أربيل شمالي العراق</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/naya_foriraq/85826" target="_blank">📅 00:59 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85825">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/decaacf8b1.mp4?token=ggSXo-kzfkoqvhceiwv9AX7QTDnDrXoAyyA79Chllvb36Pq33iUfiogPEonde4maM9B_9jGLWgH9CDFvnBN_9WGIXImgnTU4q-K6XNh6qectsra8F7fQlSmKwGlUwc6ebw_vb_645jd_Xi1Ohv1YFT0AOupETLJW0m10c-aAZPAMJTDMVcfDRQtCT6oCeK11RQvlXihtpt62kDfqbKuguYIrSkX06nicsqm0Vj0aVWfFL_1d20ZSFAA2_mHbNo3U9Cd-B3ZVzo7_JEkU1BiuGmYxMjzvhltbmQPB4gFYRdWM8CICHywh731tyWkq0cYYR2zrDFWz6TK8GrCN7k_s2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/decaacf8b1.mp4?token=ggSXo-kzfkoqvhceiwv9AX7QTDnDrXoAyyA79Chllvb36Pq33iUfiogPEonde4maM9B_9jGLWgH9CDFvnBN_9WGIXImgnTU4q-K6XNh6qectsra8F7fQlSmKwGlUwc6ebw_vb_645jd_Xi1Ohv1YFT0AOupETLJW0m10c-aAZPAMJTDMVcfDRQtCT6oCeK11RQvlXihtpt62kDfqbKuguYIrSkX06nicsqm0Vj0aVWfFL_1d20ZSFAA2_mHbNo3U9Cd-B3ZVzo7_JEkU1BiuGmYxMjzvhltbmQPB4gFYRdWM8CICHywh731tyWkq0cYYR2zrDFWz6TK8GrCN7k_s2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/naya_foriraq/85825" target="_blank">📅 00:58 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85824">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/naya_foriraq/85824" target="_blank">📅 00:58 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85823">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a653f7d251.mp4?token=KjjagAIOcDqw0oIkDcoT9vKYm2nh0pqggYmT_7OWTDXX4ybmDYzTcxyXnvTZkEl8w9J60VCCN12IiVKOO6qsMv51zCq2VkYYGfB50zEdHgT70POCDVDB1zDsuXM3qP8HNmTQu-AiOkG56gyn6YjKzxMOz5Uy55IW393acVTVHS-Tbh_yHZCnV0vXgkQepuPBS6_BkCj4c49E1qIGJcecHrWO4LjbH8yzgt7aWRhydyF6zGJJKPxvph1rVh5WPK8BVACjoFYUBjDrBcT9IyK15fXrcmCPzmXp26Ozz8iNIRH4RY9gdvik8KJqD9mvUQ4dSFcxXESYUTrVbZd17InAgg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a653f7d251.mp4?token=KjjagAIOcDqw0oIkDcoT9vKYm2nh0pqggYmT_7OWTDXX4ybmDYzTcxyXnvTZkEl8w9J60VCCN12IiVKOO6qsMv51zCq2VkYYGfB50zEdHgT70POCDVDB1zDsuXM3qP8HNmTQu-AiOkG56gyn6YjKzxMOz5Uy55IW393acVTVHS-Tbh_yHZCnV0vXgkQepuPBS6_BkCj4c49E1qIGJcecHrWO4LjbH8yzgt7aWRhydyF6zGJJKPxvph1rVh5WPK8BVACjoFYUBjDrBcT9IyK15fXrcmCPzmXp26Ozz8iNIRH4RY9gdvik8KJqD9mvUQ4dSFcxXESYUTrVbZd17InAgg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مرة اخرى استهداف مقرات الاحزاب المعارضة في محافظة اربيل شمالي العراق.</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/naya_foriraq/85823" target="_blank">📅 00:57 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85822">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">مشاهد اخرى لاستهداف مقرات الاحزاب المعارضة في محافظة اربيل شمالي العراق.</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/naya_foriraq/85822" target="_blank">📅 00:53 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85821">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/79187ad90d.mp4?token=Pp43leM-P4q4vJOJkosuktHcatj3VdY9Xqr02Y_JXC44WYvecVQoBdCjobax-CYSkbA3-w6oxt0uOGTRulkw5jc3G4Zy-4x6pZOMzeMDPlJIpZF70L6gE4_pihKbN04VSnFx4-hqGmlJwAEAOnJGNV6H-a_f6m1QVkujM8dsbPd8g5-e_5eJpTN4A04sq39JxO12CA0fvNd4pvFNQ1OKNKR38J8grg-UNyFj2opL_fhoGIEoW_9FNn7TehrI8whqpUhacW0Q9c0ezv8LXpe55AVrOR3QMREeUhKzSpJ1wSUvF-MNfKpG1Fn6TGE2-Pk38O4YHbx943GJjx4ZPIeV7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/79187ad90d.mp4?token=Pp43leM-P4q4vJOJkosuktHcatj3VdY9Xqr02Y_JXC44WYvecVQoBdCjobax-CYSkbA3-w6oxt0uOGTRulkw5jc3G4Zy-4x6pZOMzeMDPlJIpZF70L6gE4_pihKbN04VSnFx4-hqGmlJwAEAOnJGNV6H-a_f6m1QVkujM8dsbPd8g5-e_5eJpTN4A04sq39JxO12CA0fvNd4pvFNQ1OKNKR38J8grg-UNyFj2opL_fhoGIEoW_9FNn7TehrI8whqpUhacW0Q9c0ezv8LXpe55AVrOR3QMREeUhKzSpJ1wSUvF-MNfKpG1Fn6TGE2-Pk38O4YHbx943GJjx4ZPIeV7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هجوم عنيف يستهدف مقرات الاحزاب المعارضة في محافظة اربيل شمالي العراق.</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/naya_foriraq/85821" target="_blank">📅 00:51 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85820">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0af9e5cd42.mp4?token=eO1LpZYw4x9pwsCW2lzZ7tR25mYFg2vHKKfiXSezvg6W9NjEerEMWaMih2dM-qI4d26hu9I1gaSkB21oVUVi8CMWCH7UXSRreQJCIRiLKSdqxvHyqHtRslqmm7kfnV4mTd9vK_m-SEjw4Z5us4st-VRVcwp-fCNH7qlFv-cL5afUJoeo8ESfm-fI15V-xbwZwm3B6ofzoritCDW3jVJCCR6ngkMgXRy69-_7knwX17oYKnvIaXE6ErCBVLs0PyUNpxxQEC9Pq1kKsc1Vbepvy5Rr1mb0zn1hErcwWCcL7aExOM0pW-p38cBJ61csxF7BjqUPBYAgYVAmUZOl1z0K0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0af9e5cd42.mp4?token=eO1LpZYw4x9pwsCW2lzZ7tR25mYFg2vHKKfiXSezvg6W9NjEerEMWaMih2dM-qI4d26hu9I1gaSkB21oVUVi8CMWCH7UXSRreQJCIRiLKSdqxvHyqHtRslqmm7kfnV4mTd9vK_m-SEjw4Z5us4st-VRVcwp-fCNH7qlFv-cL5afUJoeo8ESfm-fI15V-xbwZwm3B6ofzoritCDW3jVJCCR6ngkMgXRy69-_7knwX17oYKnvIaXE6ErCBVLs0PyUNpxxQEC9Pq1kKsc1Vbepvy5Rr1mb0zn1hErcwWCcL7aExOM0pW-p38cBJ61csxF7BjqUPBYAgYVAmUZOl1z0K0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">استمرار طيران المسير في محافظة اربيل شمالي العراق</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/naya_foriraq/85820" target="_blank">📅 00:49 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85816">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/207797b8fe.mp4?token=tQUGCcmlrUGnqg13q7fGnwRQnxNw5Zl4JJaVn0ekGiCDXPBdlUmbekBI3Bt8Wkz4vxJ826w08TqeyGGaP4idnDly8F3pwZxBr-CxBt6QkbJc7ddMDuhkTSU72EeElpWxwKFhKVaCEO5xrQOhLenUigdrV1VDA81Htt8KOuXJLA72uY2PK1A7GdkiiSYT-JWZOSjLWyccmdWuYaZhTP9xZ92moD09Z_bL1-NhYvdoAsWFsMqltNIEXq2kevKgPE46rF3QngfLsoImTLYQcok40uo6fo_s-oww_DXiM3iIsdDxXB91rsFLIHMzUkU8PxW7Dhjb9LnDoaRvmBX8e5Qenw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/207797b8fe.mp4?token=tQUGCcmlrUGnqg13q7fGnwRQnxNw5Zl4JJaVn0ekGiCDXPBdlUmbekBI3Bt8Wkz4vxJ826w08TqeyGGaP4idnDly8F3pwZxBr-CxBt6QkbJc7ddMDuhkTSU72EeElpWxwKFhKVaCEO5xrQOhLenUigdrV1VDA81Htt8KOuXJLA72uY2PK1A7GdkiiSYT-JWZOSjLWyccmdWuYaZhTP9xZ92moD09Z_bL1-NhYvdoAsWFsMqltNIEXq2kevKgPE46rF3QngfLsoImTLYQcok40uo6fo_s-oww_DXiM3iIsdDxXB91rsFLIHMzUkU8PxW7Dhjb9LnDoaRvmBX8e5Qenw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">استمرار محاولات الاعتراض والتصدي لمسيرات في سماء مدينة حمص السورية.</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/naya_foriraq/85816" target="_blank">📅 00:49 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85814">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8c4a468f9f.mp4?token=qhOJJzw4O3dT9fGfTYcnSMt1qjbvCZtIhGSM2n36GjVfXGmuH1l06pFNXvieX_mOjWkfpmQtt9OKcWoetNH5kSo1CQ3goFmAh80XWlTQvA_dsuHS4epzEA24Ocaz2gMOe1vicWI1-Ylxuwnm0lYV0SwhtGl6KKA0L97i7ehimsNOvKVmIXuvs0TUfa-KW9c7VG3xkEVOTVGrhK9ySBxm6_aHeBt_c52JW5VvjyUKgVA43AlTwUmNl6tkk-wpsDBx_01XDMf50Rv0OquGHZwCmUPa1klXoVDTUeR1MR2fMYFovZ7iD-gp9lHqBst803rNJ2j-7Zv2mmAUBv3BpvfZfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8c4a468f9f.mp4?token=qhOJJzw4O3dT9fGfTYcnSMt1qjbvCZtIhGSM2n36GjVfXGmuH1l06pFNXvieX_mOjWkfpmQtt9OKcWoetNH5kSo1CQ3goFmAh80XWlTQvA_dsuHS4epzEA24Ocaz2gMOe1vicWI1-Ylxuwnm0lYV0SwhtGl6KKA0L97i7ehimsNOvKVmIXuvs0TUfa-KW9c7VG3xkEVOTVGrhK9ySBxm6_aHeBt_c52JW5VvjyUKgVA43AlTwUmNl6tkk-wpsDBx_01XDMf50Rv0OquGHZwCmUPa1klXoVDTUeR1MR2fMYFovZ7iD-gp9lHqBst803rNJ2j-7Zv2mmAUBv3BpvfZfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سماء محافظة اربيل تشتعل اثر الهجوم على مقرات الاحزاب المعارضة الايرانية.</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/naya_foriraq/85814" target="_blank">📅 00:43 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85813">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d950af84df.mp4?token=oHxCGLITYAIwuNOOG7NAo_PBB6jsUWpYOyMdTR0MMBeM2smmELtWxXOwZtMTevbR1XgLwd_wCiL_B6pI8QWvZsU7aqZPraRWMryShFR_Hk0kqDDQw-R8dPsPSiOC2sAFrdpbItZON64z7x7LEfemVS8ExgsQ_UXu3vQ2R_lMv_TnoW09OtEhXTlWaR-fx6cP0E-oQJsNkKk1Im3AQPMumIy5TfLYqephJd9-fNaovTYoXD6vvk8U6Eehd8KXESPCIgBKPk0PINX8ZWvxOQSocLKR5b1Pk_sGBhZuPsPnfpqVKwJN5WNxhbxs7Wvhk9vwJ_r4uulsBBZbW6nZplXEMrbDaS3C6iQw6FJDLt7KrykXCGInaQG6sKUj4z6xd5y2Pe0PXjnEw70C-K0GPMiXi324u5o2pc1Jc06YVujfzcy8NcShMrZ71N2VOiag1CXEfps1MqnVH7ijCJbm_0FZir91nTOi0YhKYKGyKJuI40GPflhU9kvQ2FcfcflCT6nCJAGzp0rYF9r-oi2UUAoxgUPvxByVUOKqdhWc5NUmuoG5jwLQoNwPtNI9SKVKHfAfr84EsbWd9nucVVcGYoJ6y4IYkAYnIJVTd1V3GPGlwbPkCX1JpF6yvpUMBDYdLN95mKf_3W2zI51idOjgsEw_-64RtIxw_7isSMH_aME3Jvs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d950af84df.mp4?token=oHxCGLITYAIwuNOOG7NAo_PBB6jsUWpYOyMdTR0MMBeM2smmELtWxXOwZtMTevbR1XgLwd_wCiL_B6pI8QWvZsU7aqZPraRWMryShFR_Hk0kqDDQw-R8dPsPSiOC2sAFrdpbItZON64z7x7LEfemVS8ExgsQ_UXu3vQ2R_lMv_TnoW09OtEhXTlWaR-fx6cP0E-oQJsNkKk1Im3AQPMumIy5TfLYqephJd9-fNaovTYoXD6vvk8U6Eehd8KXESPCIgBKPk0PINX8ZWvxOQSocLKR5b1Pk_sGBhZuPsPnfpqVKwJN5WNxhbxs7Wvhk9vwJ_r4uulsBBZbW6nZplXEMrbDaS3C6iQw6FJDLt7KrykXCGInaQG6sKUj4z6xd5y2Pe0PXjnEw70C-K0GPMiXi324u5o2pc1Jc06YVujfzcy8NcShMrZ71N2VOiag1CXEfps1MqnVH7ijCJbm_0FZir91nTOi0YhKYKGyKJuI40GPflhU9kvQ2FcfcflCT6nCJAGzp0rYF9r-oi2UUAoxgUPvxByVUOKqdhWc5NUmuoG5jwLQoNwPtNI9SKVKHfAfr84EsbWd9nucVVcGYoJ6y4IYkAYnIJVTd1V3GPGlwbPkCX1JpF6yvpUMBDYdLN95mKf_3W2zI51idOjgsEw_-64RtIxw_7isSMH_aME3Jvs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">إطلاقات دفاعية في سماء مدينة حمص السورية.</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/naya_foriraq/85813" target="_blank">📅 00:41 · 06 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
